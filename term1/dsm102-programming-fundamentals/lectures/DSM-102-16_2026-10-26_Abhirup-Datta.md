---
course: DSM 102
date: 2026-10-26
start: 7:00pm
session: "16"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 14 (2026-10-13)](DSM-102-14_2026-10-13_Abhirup-Datta.md) · [All lectures](./) · [Session 17 (2026-10-30)](DSM-102-17_2026-10-30_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 · Session 16 (2026-10-26, Abhirup Datta)
## Regression in Practice: Uncertainty, Physics Constraints, Weights, Generalization, and Traps (Astronomy Case Studies)

> **Note on the source:** This was reconstructed from a noisy speech-to-text transcript. Numbers that were garbled are flagged **[unclear]**. All code blocks are **best-effort reconstructions** from the spoken walkthrough. The instructor described the code but did not dictate it line by line, so exact function names, variable names and arguments are inferred.

---

## 1. Overview

This session continues from the previous class on linear regression via the normal equations and collinearity. It applies regression to real and simulated astronomy data, organised around four questions the bare formula $\hat\beta = (X^TX)^{-1}X^Ty$ cannot answer:

1. How sure are we of the answer?
2. What if physics already tells us part of the answer?
3. What if some data points are more trustworthy than others?
4. Will the model work on data it has never seen?

The lecture has four parts:

- **Part A – Hubble's 1929 data:** standard errors and confidence intervals, and fitting through the origin. A precise answer can still be badly wrong because of systematic error. This leads to the modern "Hubble tension".
- **Part B – Galaxy star-formation "main sequence" (Speagle et al. 2014, simulated survey):** log transforms for power laws, omitted-variable bias, interaction terms, why $R^2$ is not a significance test, interpreting coefficients when $\log M = 0$, and weighted least squares including intrinsic scatter.
- **Part C – Type Ia supernova Hubble diagram:** polynomial regression of increasing degree, training vs. test error, the noise floor, overfitting, k-fold cross-validation, the one-standard-error rule, and ridge regression with standardization.
- **Part D – Three traps where $R^2$ and residual plots look fine but the answer is wrong:** errors in $x$ (attenuation), cuts on $y$ (selection/truncation), and extrapolation.

A mid-lecture student question led to a beginner-level re-explanation of overfitting/underfitting, $\chi^2$, degrees of freedom, and reduced $\chi^2$. The session ended with a recap, review questions, and assignment logistics.

---

## 2. Topics, Concepts and Worked Examples (in order taught)

### 2.0 Motivation hook
- In 1929 Edwin Hubble fit a straight line through **24 galaxies** and discovered the universe is expanding. This was one of the first and most important regressions ever run.
- The same fit implied the universe is only about **2 billion years old**, younger than the rocks on Earth. The goal of the lecture is to explain *why a correct method gave a wrong answer* and how to avoid it.

### 2.1 Recap: uncertainty in OLS coefficients (from last class)

**OLS estimate (normal equations):**
$$\hat\beta = (X^TX)^{-1}X^Ty$$

**Step 1 – Estimate the noise variance from residuals.** Divide by $n-p$, not $n$:
$$\hat\sigma^2 = \frac{1}{n-p}\sum_{i=1}^{n}\left(y_i - x_i^T\hat\beta\right)^2$$
- $n$ = number of data points; $p$ = number of fitted parameters.
- **Why $n-p$:** every parameter you fit uses up one data point's worth of freedom.
- Example: with 2 points and 2 parameters, the line passes through both exactly. The residuals are 0, which tells you nothing about the noise.

**Step 2 – Covariance of the coefficients.** Multiply the noise variance by the *same* matrix that gave $\hat\beta$:
$$\mathrm{Cov}(\hat\beta) = \hat\sigma^2\,(X^TX)^{-1}$$

**Standard errors** are the square roots of its diagonal:
$$\mathrm{SE}(\hat\beta_j) = \sqrt{\left[\hat\sigma^2 (X^TX)^{-1}\right]_{jj}}$$

**t-value:**
$$t_j = \frac{\hat\beta_j}{\mathrm{SE}(\hat\beta_j)}$$

**95% confidence interval:** the estimate plus or minus about two standard errors. Precisely:
$$\hat\beta_j \pm t_{0.975,\,n-p}\,\mathrm{SE}(\hat\beta_j)$$

#### The "regression engine" (~15 lines)
The instructor showed a single function that solves the normal equations, then computes SEs, t-values and intervals. It has a `weights` argument, to be ignored until Part B.

```python
# RECONSTRUCTION — names and exact structure are inferred, not dictated.
import numpy as np
from scipy import stats

def fit_ols(X, y, weights=None, level=0.95):
    n, p = X.shape
    w = np.ones(n) if weights is None else np.asarray(weights)   # Part B: w_i = 1/sigma_i**2
    XtW = X.T * w                          # same as X.T @ diag(w)
    XtWX_inv = np.linalg.inv(XtW @ X)      # (X^T W X)^{-1}
    beta = XtWX_inv @ (XtW @ y)            # normal equations
    resid = y - X @ beta
    sigma2 = np.sum(w * resid**2) / (n - p)   # noise estimate, n - p degrees of freedom
    cov = sigma2 * XtWX_inv
    se = np.sqrt(np.diag(cov))             # standard errors
    t_vals = beta / se
    t_crit = stats.t.ppf(0.5 + level/2, df=n - p)   # ≈ 2 for 95%
    ci = np.column_stack([beta - t_crit*se, beta + t_crit*se])
    return beta, se, t_vals, ci
```

---

### 2.2 Part A — Hubble's 1929 data

**Data:**
- Hubble's actual 24 galaxies.
- **Distance** $d$ in megaparsecs (Mpc). 1 Mpc ≈ 3 million light-years (more precisely ≈ 3.26 million).
- **Velocity** $v$ in km/s, from redshift. Positive means moving away from us.

**Physical model (uniform expansion):** a galaxy twice as far away recedes twice as fast.
$$v = H_0\,d$$
$H_0$ is the **Hubble constant**, i.e. the slope we are looking for.

**Negative velocities:** some galaxies (e.g. **Andromeda**) are moving *toward* us, because Andromeda is falling into the Milky Way. This is real motion, not measurement error.

**Fit 1 – line with an intercept** (a two-column $X$: a column of ones and distance):
- Intercept ≈ $-40.784$ km/s
- Slope ≈ $454.158$ km/s/Mpc
- The 95% CI on the intercept includes 0. The data cannot tell the intercept apart from zero, and physics says it *is* zero.

**Fit 2 – through the origin** (intercept fixed at 0; $X$ is only the distance column):
- Slope drops from ≈ 454 to ≈ **424** km/s/Mpc.
- Pinning the left end at zero lifts it, so the line tilts less to reach the same data cloud.
- Plot: Fit 1 is dotted, Fit 2 (through origin) is solid. The two differ only slightly. A residual plot was shown on the right.
- **Lesson:** if physics tells you part of the answer, build it into the model.

```python
# RECONSTRUCTION
X1 = np.column_stack([np.ones_like(d), d])   # with intercept
X2 = d[:, None]                              # through the origin (no column of ones)
beta1, se1, t1, ci1 = fit_ols(X1, v)
beta2, se2, t2, ci2 = fit_ols(X2, v)
```

**Age of the universe from $H_0$.** If galaxies fly apart at constant speed, distance divided by speed is the time since they were together:
$$t_{\text{age}} \approx \frac{1}{H_0}$$
With unit conversion, for $H_0$ in km/s/Mpc:
$$t_{\text{age}}\,[\text{Gyr}] \approx \frac{977.8}{H_0}$$

Worked numbers:
- $977.8/424 \approx 2.3$ billion years.
- 95% interval ≈ **1.9 to 2.9 Gyr**. The interval is tight.
- But Earth is **4.5 Gyr** old (radioactive dating), and the universe cannot be younger than the Earth.

```python
# RECONSTRUCTION
age_gyr = 977.8 / beta2[0]
age_ci  = 977.8 / ci2[0][::-1]   # inverting flips the interval endpoints
```

**What went wrong: systematic error.**
- Hubble's distances were all too small by a large factor. The stars used as distance markers were misidentified, and this was only corrected in the 1950s.
- Every point was shifted the *same way*. So the scatter was small, the CI was small, and the answer was wrong.
- **Key message: precise ≠ accurate.** A confidence interval only covers *random* error. It cannot detect *systematic* error.

**Modern values and the Hubble tension:**
- Today $H_0 \approx 70$ km/s/Mpc, so Hubble was about 6× off.
- **Planck satellite** (cosmic microwave background): $H_0 = 67.4 \pm 0.5$.
- **SH0ES team** (Cepheid stars + supernovae): $H_0 = 73.04 \pm 1.04$.
- Each claims about 1% precision, yet they disagree by about **5 standard errors**. Check: $(73.04-67.4)/\sqrt{0.5^2+1.04^2}\approx 4.9$.
- This is the **Hubble tension**, an open research problem. Either one measurement hides a systematic error (as Hubble's did), or our model of the universe is missing something. Statistics alone cannot tell which.

---

### 2.3 Part B — The galaxy star-formation main sequence

**Quantities measured per galaxy:**
- **Stellar mass** $M_*$: the mass of all its stars.
- **Star formation rate (SFR):** solar masses of new stars made per year. The Milky Way makes about 1–2 per year.

**Two facts about star-forming galaxies:**
- Plotted against each other, they fall in a tight band called the **main sequence**. Heavier galaxies make more stars.
- In the past, when the universe was younger, every galaxy made stars faster.

**Speagle et al. (2014)** combined 25 published studies into one formula. Here $t$ is the age of the universe in Gyr and masses are in solar units:
$$\log \mathrm{SFR} = (0.84 - 0.026\,t)\,\log M_* - (6.51 - 0.11\,t)$$
- The age of the universe $t$ appears **twice**: once changing the slope, once changing the height (intercept).
- Reference points: the age of the universe today is ≈ 13.8 Gyr; at redshift $z = 3$ it was ≈ **2.1 Gyr**.

**Simulation design:** generate a survey of **800 galaxies** from this formula at various redshifts. Because the true answer is known, we can check whether regression recovers it.

```python
# RECONSTRUCTION — distributions, ranges and scatter values are inferred
rng = np.random.default_rng(0)
N = 800
z = rng.uniform(0.3, 3.0, N)
t = age_of_universe(z)          # e.g. via astropy.cosmology; t ≈ 2.1 Gyr at z = 3
logM = ...                      # higher-z galaxies drawn at higher mass (selection effect)
logSFR = (0.84 - 0.026*t)*logM - (6.51 - 0.11*t) + rng.normal(0, 0.2, N)
```

**Why logarithms:**
- A power law $y = A x^{\alpha}$ is a curve. Taking logs gives $\log y = \log A + \alpha \log x$, a straight line with slope $\alpha$.
- So **linear regression on log quantities fits a power law**.
- **dex:** one unit of $\log_{10}$. 1 dex = a factor of 10.

**Plot observations:**
- Colour = redshift. Yellow (high-$z$) galaxies are far away, seen when the universe was young.
- They sit *higher* (more star-forming) and start at *higher mass*.
- Reason: far away, a telescope only sees the heavy galaxies. The instructor said to remember this, because it causes a problem later.

**Model 1 – mass only:** $\log\mathrm{SFR} = \beta_0 + \beta_1 \log M_*$
- **Residual diagnostic:** if the model were complete, residuals vs. redshift would show random scatter around 0 with no trend.
- **Actual result:** the residuals climb by about 1 dex from $z = 0.3$ to $z = 3$. Time is missing from the model.
- **True slope** over the sample's epochs is between **0.58 and 0.79** (since $0.84 - 0.026t$ varies with $t$).
- **Model 1's slope ≈ 0.85**, steeper than the truth at *every* redshift.
- Leaving out time did not just add noise; it **corrupted** the coefficient that was kept. Distant galaxies are both heavier *and* more star-forming, so mass took credit for the time effect.

**Omitted variable bias (definition):** if you leave out a variable that is *correlated* with one you kept, the kept variable's coefficient is biased. As the instructor put it, "the one you kept lies to you."

**Interaction terms.** Multiplying out Speagle's formula:
$$\log \mathrm{SFR} = -6.51 + 0.84\,\log M_* + 0.11\,t - 0.026\,(t \cdot \log M_*)$$
- The last term is an **interaction**: just one more column of $X$, equal to the product of two other columns.
- Meaning: the slope of the main sequence is $0.84 - 0.026\,t$, so the relation **flattens as the universe ages**.

**Models 2 and 3:**
- **Model 2** adds $t$: $R^2$ jumps from **0.43 to 0.66**.
- **Model 3** adds $t \cdot \log M_*$: $R^2$ rises by only about **0.03** (tiny), but its t-value is large and negative (exact value not captured).
- **Lesson: $R^2$ measures overall fit. It is NOT a test of whether a particular effect is real.**

```python
# RECONSTRUCTION
ones = np.ones(N)
X_m1 = np.column_stack([ones, logM])                 # Model 1
X_m2 = np.column_stack([ones, logM, t])              # Model 2
X_m3 = np.column_stack([ones, logM, t, logM*t])      # Model 3 (interaction)
```

**Interpreting a "non-significant" main effect in Model 3:**
- The coefficient on $t$ has 95% CI ≈ $(-0.1,\ +0.39)$ [values approximate], which includes 0. That seems to say "not significant".
- Does time not matter? Of course it does; we just saw it.
- The catch: with an interaction present, this coefficient measures the effect of time **for a galaxy with $\log M_* = 0$**, i.e. a galaxy of exactly one solar mass. Nobody cares about that question.
- **Fix (from the recap): center the variables** (e.g. use $\log M_* - \overline{\log M_*}$). Each main effect then refers to a typical galaxy, and centering also reduces collinearity between $t$ and $t\cdot\log M_*$.

#### Weighted least squares (WLS)
**Problem:**
- Each galaxy has its own error bar (`sfr_err` column), ranging from **0.05 to 0.6** dex.
- OLS gives every galaxy an equal vote, which is unfair to the well-measured ones.

**Minimize chi-square**, where each squared residual is divided by that point's variance:
$$\chi^2 = \sum_{i=1}^{n} \frac{\left(y_i - x_i^T\beta\right)^2}{\sigma_i^2}$$

**Solution:** the same algebra as OLS with a $W$ in the middle:
$$\hat\beta_{\text{WLS}} = (X^TWX)^{-1}X^TWy, \qquad W = \mathrm{diag}\!\left(\frac{1}{\sigma_i^2}\right)$$

**Worked example of weights:**
- $\sigma = 0.1 \Rightarrow w = 1/0.01 = 100$.
- $\sigma = 0.5 \Rightarrow w = 1/0.25 = 4$.
- So the precise galaxy counts $100/4 = 25$ times more.

**Trap: include the intrinsic scatter.** $\sigma_i$ must include the real scatter of the relation itself, not just the measurement error:
$$\sigma_i^2 = \sigma_{\text{meas},i}^2 + \sigma_{\text{int}}^2$$
- The transcript says the intrinsic scatter is "2 dex". This is almost certainly **0.2 dex** [unclear].
- Otherwise a few very precisely measured galaxies dominate, even though each still scatters intrinsically about the relation.

**Results:**
- WLS standard errors drop by **20–30%**.
- **Reduced $\chi^2$** (defined in 2.5) is **1.04** with intrinsic scatter included. With measurement errors alone it is **2.6**, telling us the error model is missing something. **This is how astronomers detect intrinsic scatter.**
- scikit-learn's `LinearRegression().fit(X, y, sample_weight=w)` gives exactly the same coefficients as the hand-written engine.

```python
# RECONSTRUCTION
sigma_int = 0.2                                  # inferred (transcript: "2 dex")
w = 1.0 / (sfr_err**2 + sigma_int**2)
beta_w, se_w, t_w, ci_w = fit_ols(X_m3, logSFR, weights=w)

from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=False)       # X already contains a column of ones
lr.fit(X_m3, logSFR, sample_weight=w)            # same coefficients as beta_w
```

**Why bother with weights if both are unbiased? A Monte Carlo check:**
- The survey was re-simulated **300 times**.
- Histograms of the fitted slope from OLS and WLS are both centred on the truth (both unbiased).
- WLS has a narrower spread: **0.020 vs. 0.026**. Same telescope time, more precise answer.
- This is the **Gauss–Markov (Aitken) result** for unequal noise: the right weights give the **minimum-variance unbiased (linear) estimator**.

---

### 2.4 Part C — Type Ia supernovae: prediction and overfitting

**Change of goal:** we no longer want to understand coefficients. We want to **predict** data we have not seen.

**Background:**
- A **Type Ia supernova** is an exploding white dwarf. It always reaches nearly the same peak brightness, so how faint it looks tells you how far away it is.
- Astronomers plot the **distance modulus** $\mu$ (a logarithmic distance, in magnitudes) against redshift $z$.
- In 1998 two teams found distant supernovae fainter than expected, so the expansion of the universe is *accelerating*. This earned the 2011 Nobel Prize.

**Simulation:** **50 supernovae** (roughly the size of the 1998 samples) from the standard cosmological model, with **0.15 mag** scatter. The true curve is treated as unknown.

**Polynomial regression, degrees 1 to 15:**
- Is a degree-15 polynomial still *linear* regression? **Yes.** It is linear in the $\beta$s; $x^2, x^3, \dots$ are just more columns of $X$:
$$\mu = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_k x^k, \quad x = \log z \ (\text{likely})$$
- **Training error** keeps falling as degree increases. **Test error** (15 held-out points) does not:
  - ≈ **0.22** at degree 1
  - ≈ **0.165** at degree 2–3, flat for a while
  - shoots up to ≈ **0.42** at degree 15

**Overfitting (definition):** the model starts to memorize the noise in the training data instead of the underlying shape, so it does worse on new data.

**Noise floor:**
- No model gets test error below about **0.15**, because that scatter belongs to the supernovae themselves.
- The best possible model only gets the shape right; the noise floor always remains.
- **Debugging tip:** "If anybody shows you a model that beats the noise floor on new data, you should check the code." This usually signals test-data leakage or a bug.

**Problem with a single train/test split:** with only 15 test points, a different random split might give a different answer.

**k-fold cross-validation (k = 5):**
1. Cut the training data into 5 pieces (folds).
2. Fit on 4, test on the 5th.
3. Rotate so each fold is the test once, then average the 5 errors.
4. The real **test set stays locked away the whole time**.

**CV results:**
- The lowest average CV error is at **degree 3**.
- Error bars explode after **degree 7**. When a fold holds out the *edge* points, a high-degree polynomial must extrapolate and goes wild.
- Degree 2 is within one standard error of degree 3, so a cautious analyst picks **degree 2**.
- **One-standard-error rule:** choose the *simplest* model whose CV error is within one SE of the minimum.

```python
# RECONSTRUCTION
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.pipeline import make_pipeline

x = np.log10(z)[:, None]
x_tr, x_te, mu_tr, mu_te = train_test_split(x, mu, test_size=15, random_state=0)

kf = KFold(n_splits=5, shuffle=True, random_state=0)
cv_mean, cv_se = [], []
for deg in range(1, 16):
    model = make_pipeline(PolynomialFeatures(deg), LinearRegression())
    scores = -cross_val_score(model, x_tr, mu_tr, cv=kf,
                              scoring="neg_root_mean_squared_error")
    cv_mean.append(scores.mean())
    cv_se.append(scores.std() / np.sqrt(len(scores)))
# best degree = argmin(cv_mean); one-SE rule -> simplest degree with
# cv_mean <= min(cv_mean) + its SE
```

**Ridge regression — the other way to beat overfitting:**
- Keep the big flexible model but charge a penalty for large coefficients:
$$\hat\beta_{\text{ridge}} = \arg\min_\beta \ \|y - X\beta\|^2 + \lambda\|\beta\|^2 = (X^TX + \lambda I)^{-1}X^Ty$$
- $\lambda = 0$ gives ordinary least squares. A huge $\lambda$ pushes all coefficients toward 0.
- **Rule: standardize the columns first.** The penalty treats every coefficient the same, but $x$ and $x^{15}$ live on very different scales. This is the `StandardScaler` step in the pipeline.
- $\lambda$ is chosen by cross-validation.

```python
# RECONSTRUCTION
ridge = make_pipeline(PolynomialFeatures(15, include_bias=False),
                      StandardScaler(),
                      RidgeCV(alphas=np.logspace(-6, 3, 50)))
ridge.fit(x_tr, mu_tr)
```

**Ridge results:**
- **Left panel:** the degree-15 OLS curve wiggles at low redshift; the ridge curve (blue) stays smooth along the truth.
- **Right panel (log scale):** OLS coefficients are around **1000**; ridge coefficients are **below 3**.
- **Fingerprint of overfitting:** huge coefficients of opposite sign cancelling each other.
- **Test errors:**

| Model | Test error |
|---|---|
| Degree-15 OLS | 0.42 |
| Degree-15 ridge | ≈ 0.171 (a "0.292" was also spoken; likely a misread) |
| CV-chosen degree 3 | ≈ 0.165 (transcript says "065") |

- **Two routes, same destination:** either make the model smaller, or keep it big and shrink its coefficients.

**Slider demo:**
- At low degree the curve is almost linear; at higher degree it starts wobbling.
- At **degree 14** the curve bends between training points near $\log z \approx -1.8$ [unclear; transcript "1 - 8"] and misses the orange test points.

---

### 2.5 Interlude (student Q&A): beginner explanation

A student (Vikat Raj) noted that the class has diverse backgrounds and some students lack basics such as scikit-learn and overfitting/underfitting. The instructor re-explained:

**Fitting polynomials of increasing degree to ~14–15 points:**
- Degree 1 = straight line.
- Degree 2 = one gentle curve.
- Degree 3 = two bends, still fairly straight.
- Up to about degree 6 it still looks roughly like a line. From about degree 7, wiggles appear.
- With many coefficients for ~15 points, the curve bends to pass through the individual points. That is overfitting.

**Why it matters downstream:**
- Over- or underfitting gives wrong estimates of the coefficients ($\beta$, intercepts).
- These errors carry forward when the fitted values are used for calibration or applied to other datasets (e.g. real JWST data, the James Webb Space Telescope).

**Example: price vs. quantity.**
- The expected trend is downward (inverse relation).
- A few outliers (likely with large error bars) can make a high-degree fit curve the wrong way.
- Applied to new data, that fit might imply price *increases* with quantity, which is wrong.

**How to tell if you are over- or underfitting — reduced $\chi^2$:**
- $\chi^2$ measures how far the line passes from the data points, relative to their error bars (requires data with error bars):
$$\chi^2 = \sum_i \frac{(y_i - \hat y_i)^2}{\sigma_i^2}$$
- **Degrees of freedom:** $\nu = N - p$ (number of points minus number of fitted parameters).
  - Example: 4 points with a 2-parameter line gives $\nu = 4 - 2 = 2$. The transcript is muddled here ("divide by degree of freedom minus 2"); the correct formula is below.
$$\chi^2_\nu = \frac{\chi^2}{N - p}$$
- **Interpretation:**
  - $\chi^2_\nu \approx 1$ (not exactly 1): good fit, consistent with the error bars.
  - $\chi^2_\nu \gg 1$: **underfitting**, or the error model is missing something (as with the 2.6 in Part B).
  - $\chi^2_\nu \approx 0$: the line passes through all the points, i.e. **overfitting**.

The instructor agreed to briefly define terms when they come up.

---

### 2.6 Part D — Three traps (fit looks fine, answer is wrong)

In each trap, $R^2$ and the residual plot look fine, yet the answer is wrong.

**Trap 1 – Errors in $x$ drag the slope toward zero (attenuation / regression dilution):**
- In Part B, stellar mass was treated as exact. It is not: masses fitted from a galaxy's light typically carry **0.2–0.3 dex** error.
- Noise in $y$ averages out. **Noise in $x$ does not**: it spreads points sideways, so the cloud looks flatter than it is.
- Standard result (the "formula on the board"):
$$\hat\beta \to \beta\,\frac{\sigma_x^2}{\sigma_x^2 + \sigma_{u}^2}$$
  where $\sigma_x^2$ is the true spread of $x$ and $\sigma_u^2$ is the measurement-error variance in $x$.
- **Numbers:** true slope **0.71**. With **0.3 dex** mass error the fit gives ≈ **0.61**. A 0.5 dex case was also shown; that value was not captured clearly (it is smaller still).
- **More data does not help:** the shrinkage depends on the noise, not on the sample size.
- Dedicated methods exist: **BCES** and **LINMIX** (look them up).
- A plot showed fitted slope vs. mass error alongside the theoretical prediction.

**Trap 2 – Cutting on $y$ (selection / truncation bias):**
- Telescopes only detect galaxies bright enough, i.e. with SFR above a threshold. Analogy: a camera in a dark room cannot see until there is enough light.
- **Example:** keep only galaxies above an SFR cut of 0.9. Spoken as "four or five solar masses per year"; whether this is in log units is [unclear].
- Fitting only the points above the red line gives a slope of **0.63** instead of the true **0.71**.
- **Why:** at low mass, only the unusually high-SFR galaxies survive the cut, while at high mass all galaxies survive. This flattens the slope.
- **Lesson:** do not cut on $y$ without a reason. The cut here is only justified because it mimics what a real telescope sees. If the telescope could see all galaxies, the cut would not be allowed.

**Trap 3 – Extrapolation:**
- The supernova data stop at $z \approx 1.4$. All three good models (CV-degree, ridge, etc.) did well on the test set.
- Inside the data, at $z = 1$: all agree with the truth to within **0.05 mag**.
- At $z = 3$: predictions spread over almost **3 magnitudes**.
- A **degree-6** fit says a supernova at $z = 5$ is *closer* than one at $z = 1$. This is physically impossible.
- **Cause:** the model was trained on a limited range, and polynomials are controlled by the edges of the data.
- **Lesson:** a model built from physics extrapolates sensibly because its shape comes from theory, not from the edges of the data.

---

### 2.7 Recap (as given)
- **Part A:** every coefficient needs an error bar, but the error bar cannot see systematic error.
- **Part B:**
  - Logs turn power laws into straight lines.
  - A missing variable corrupts the ones you keep.
  - Centering fixes collinearity (and makes main effects interpretable).
  - Weights reward good data.
- **Part C:** training error always improves, so judge a model on data it has not seen. Either shrink the model (lower degree) or shrink its coefficients (ridge).
- **Part D:** errors in $x$, cuts on $y$, and extrapolation can all give **confident wrong answers**.

---

## 3. Functions, Keywords, Operators and Built-ins Referenced

Names are inferred from context unless spoken explicitly.

| Item | One-line explanation |
|---|---|
| `np.column_stack` | Builds the design matrix $X$ from 1-D columns (ones, $x$, $x^2$, interaction products…) |
| `np.ones` / `np.ones_like` | Column of ones for the intercept; omit it to force the line through the origin |
| `X.T`, `@` | Transpose and matrix multiplication, used for $X^TX$ and $X^Ty$ |
| `np.linalg.inv` (or `np.linalg.solve`) | Inverts or solves the normal equations; `solve` is numerically safer |
| `np.diag` | Extracts the diagonal of the covariance matrix (the variances) |
| `np.sqrt` | Square root of variances gives standard errors |
| `scipy.stats.t.ppf` | Critical t-value for the CI (≈ 2 for 95% with enough data) |
| `np.log10` | Log transform: power law → straight line; units in dex |
| `weights` argument | Per-point weights $w_i = 1/\sigma_i^2$ for WLS |
| `LinearRegression` (scikit-learn) | OLS model; `.fit(X, y, sample_weight=w)` does weighted least squares |
| `sample_weight` | scikit-learn's per-sample weight argument; gave identical coefficients to the hand-written WLS |
| `PolynomialFeatures(deg)` | Generates columns $x, x^2, \dots, x^{\text{deg}}$ (still linear regression) |
| `train_test_split` | Holds out a test set (15 points here) |
| `KFold(n_splits=5)` / `cross_val_score` | 5-fold cross-validation for model or degree selection |
| `StandardScaler` | Standardizes columns (mean 0, sd 1); required before ridge |
| `Ridge` / `RidgeCV` | Penalized least squares; `RidgeCV` picks $\lambda$ (called `alpha` in sklearn) by CV |
| `make_pipeline` | Chains PolynomialFeatures → StandardScaler → model so scaling is learned only on training folds |
| `numpy.random.default_rng` | Random generator for simulating surveys and 300-run Monte Carlo |

---

## 4. Syntax Rules, Common Mistakes and Debugging Tips

- **Divide residual sum of squares by $n-p$, not $n$**, when estimating noise.
- **To force zero intercept**, drop the column of ones (or use `fit_intercept=False` in sklearn). Do this only if physics justifies it.
- **If $X$ already contains a ones column**, set `fit_intercept=False` in sklearn to avoid a duplicate intercept.
- **Polynomial and interaction terms are still linear regression:** just add columns to $X$.
- **Interaction models:** main-effect coefficients refer to the other variable being 0. **Center** variables before interpreting them.
- **$R^2$ is not a significance test.** Use t-values or CIs for individual effects.
- **WLS weights are $1/\sigma_i^2$, and $\sigma_i^2$ must include intrinsic scatter.** Otherwise a few precise points dominate.
- **Reduced $\chi^2 \gg 1$** means the error model is missing something (e.g. intrinsic scatter) or the model underfits. **$\approx 0$** means overfitting.
- **Standardize before ridge (not needed for OLS).** Put the scaler inside the pipeline.
- **Never touch the test set during model selection.** Use CV on the training data only.
- **Beating the noise floor on new data is a red flag.** Check the code for leakage or bugs.
- **Huge, alternating-sign coefficients** are the fingerprint of overfitting.
- **Do not extrapolate** polynomial fits beyond the data range.
- **Do not cut on $y$** without a physical or observational justification.
- **Measurement error in $x$** biases slopes toward zero, and more data will not fix it (use BCES/LINMIX-type methods).

---

## 5. Flagged for Exams / Assignments

### Review questions the instructor said you should now be able to answer
1. **Hubble's 95% interval excluded today's $H_0$. Did his interval fail?**
   No. It correctly covered the *random* error; his distances had a *systematic* error, which CIs cannot detect.
2. **With columns $x$ and $x^2$ in $X$, is the model still linear regression?**
   Yes. It is linear in $\beta$.
3. **Why standardize before ridge but not before OLS?**
   The ridge penalty depends on each coefficient's scale. OLS predictions do not change under rescaling of the columns.

Likely also examinable: the $n-p$ reasoning, SE formula, omitted-variable bias, interpreting interaction main effects, WLS weights and intrinsic scatter, the one-SE rule, the noise floor, and the three traps.

### Assignment / logistics
- **Dataset choice deadline:** tomorrow (relative to 26 Oct 2026).
- **EDA work and presentation:** to be done before the "NSM" (probably an end- or mid-semester exam; also referred to as "post tensim/mitsim"; exact term unclear). That is roughly within the next ~3 weeks.
- **No class meetings** from about **November 7** for about 1.5 weeks; use that time to finish the work offline.
- **Presenting after the exam** is acceptable to the instructor if the class prefers; otherwise finish before.
- **Basics:** the instructor will add background material (scikit-learn, overfitting, $\chi^2$, degrees of freedom, etc.) to the course notebook for students who need it.

<!-- nav -->
← [Session 14 (2026-10-13)](DSM-102-14_2026-10-13_Abhirup-Datta.md) · [All lectures](./) · [Session 17 (2026-10-30)](DSM-102-17_2026-10-30_Abhirup-Datta.md) →
<!-- /nav -->
