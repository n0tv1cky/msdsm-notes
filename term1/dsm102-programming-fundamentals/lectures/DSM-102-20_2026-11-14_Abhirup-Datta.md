---
course: DSM 102
date: 2026-11-14
start: 12:00pm
session: "20"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 19 (2026-11-13)](DSM-102-19_2026-11-13_Abhirup-Datta.md) · [All lectures](./) · [Session 21 (2026-11-16)](DSM-102-21_2026-11-16_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 · Session 20: Linear Regression with scikit-learn

*Lecturer: Abhirup Datta · Session file: DSM-102-19_2026-11-14*

---

## 1. Overview

This session revisited regression from earlier classes, which had covered least-squares fitting, probability distributions, and calculus for optimization. This time the work was done with **scikit-learn** instead of hand-written NumPy code. The running case study was scikit-learn's built-in **diabetes dataset**: 442 patients, 10 baseline features, and a target that measures disease progression one year later. The question was whether a patient's first-visit measurements can predict how much the disease will progress.

The session covered:

- the math of simple and multiple linear regression, and the least-squares objective;
- a NumPy `polyfit` refresher and a Seaborn `regplot` visualization;
- the scikit-learn workflow: train/test split, standardization with `StandardScaler`, then **create → fit → predict → evaluate**;
- converting standardized coefficients back to original units;
- evaluating fits with MSE, RMSE, and $`R^2`$;
- extending to multiple linear regression (age, BMI, blood pressure) with a correlation heatmap.

The session ended with Q&A on `fit_transform` vs `transform`.

---

## 2. Topics, in the order taught

### 2.1 Recap: what is regression?

- One student answered with **regression testing** (software QA: re-testing so that new changes don't break existing features). **This is a different concept.** Don't confuse the two.
- **Correct definition:** regression is the process of **modeling the relationship between a dependent variable and one or more independent variables**, usually to predict an outcome.
- **How many parameters?** A student said "two." That is true only for a straight line with one input: slope plus intercept. In general the count depends on the model and the number of independent variables.

### 2.2 scikit-learn: introduction

- A free, open-source machine learning library for Python.
- Started in 2007. The transcript says "developed by David"; this is most likely David Cournapeau.
- Built on the core scientific Python stack: **NumPy, SciPy, Matplotlib** (the audio said "NumPy, SAP and method").
- It is the standard toolkit for *classical* ML. It provides a clean, consistent interface, so you don't have to write the math algorithms from scratch.
- Core capabilities: **classification, regression**, and clustering/anomaly detection. The audio said "data detection", so the exact word is uncertain.
- The plan for the session: fit a straight line to real data by minimizing the error (linear regression). This uses ideas from the previous classes (distributions and calculus/optimization).

### 2.3 The case study: predicting diabetes progression

- Doctors have records for **442 diabetic patients**.
- At the first visit they record age, BMI, blood pressure, and blood tests.
- **One year later** they measure how much the disease progressed, as a single number. Higher means worse.
- **Question:** from the first visit alone, can we predict that number?

### 2.4 Linear regression: definitions and formulas

**Supervised learning.** The model learns from past cases where the answer is already known.

**Core assumption.** The output is a **weighted sum of the inputs**. Each feature is multiplied by a number (its coefficient), and the results are added. This is a *linear combination* of the input features.

**One-feature example** (illustrative numbers from the slide):

```math
\text{blood sugar} = 80 + 0.5 \times \text{age}
```

**Simple linear regression** (one feature):

```math
y = \alpha + \beta x
```

**Multiple linear regression** ($`n`$ features):

```math
y = \alpha + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
```

What each symbol means:

- $`y`$ is the **dependent variable**, or target. Here it is disease progression after one year.
- $`x_1, \dots, x_n`$ are the **independent variables**, or features: BMI, blood pressure, blood sugar, and so on.
- $`\alpha`$ is the **intercept**: the predicted $`y`$ when every feature equals $`0`$.
- $`\beta_j`$ is the **coefficient** of feature $`j`$: the change in $`y`$ when $`x_j`$ rises by one unit and all other features stay unchanged.

How to read the coefficients:

| Value of $`\beta_j`$ | Meaning |
|---|---|
| $`\beta_j > 0`$ | as the feature grows, $`y`$ grows |
| $`\beta_j < 0`$ | as the feature grows, $`y`$ falls |
| $`\beta_j = 0`$ | the feature has no effect |

- A larger $`|\beta_j|`$ means a stronger effect.
- ⚠️ **You can only compare coefficient sizes when the features are on the same scale.** This is one reason to standardize.

**Least-squares objective.** The model picks $`\alpha, \beta`$ to make the **sum of squared errors** as small as possible:

```math
\min_{\alpha,\,\beta} \; \sum_{i=1}^{N} \big(y_i - (\alpha + \beta x_i)\big)^2
```

A **residual** is $`y_i - \hat{y}_i`$, the vertical distance from a data point to the fitted line. Fitting means minimizing the sum of squared residuals.

### 2.5 Refresher: least squares with `np.polyfit`

The instructor reused the least-squares demo from a previous class. He generated synthetic BMI-like `x_demo` values and noisy `y_demo` values, fitted a line, and plotted it.

*Reconstruction note:* the exact data generation (seed, ranges, true slope/intercept, noise scale) was not read out. The values below are placeholders.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)              # seed: inferred
x_demo = rng.uniform(18, 40, 50)             # "BMI values" -- range/size inferred
y_demo = 20 + 5 * x_demo + rng.normal(0, 10, 50)   # true line + Gaussian noise -- values inferred

b, a = np.polyfit(x_demo, y_demo, 1)         # degree 1 -> straight line; returns [slope, intercept]

plt.scatter(x_demo, y_demo, label="data")
xs = np.linspace(x_demo.min(), x_demo.max(), 100)
plt.plot(xs, a + b * xs, color="red", label="least-squares fit")
plt.xlabel("BMI"); plt.ylabel("y"); plt.legend(); plt.show()
```

**Q&A on this code:**

- **What is `rng.normal`?**
  - It draws random numbers from a **normal (Gaussian) distribution**.
  - Here it adds realistic noise to the demo data.
- **What does `polyfit` do?**
  - It performs a **least-squares polynomial fit**.
  - The third argument is the **degree**:
    - `1` gives a first-order fit, $`y = \alpha + \beta x`$ (a straight line, 2 parameters).
    - `2` adds a quadratic term, $`y = \alpha + \beta x + \gamma x^2`$ (3 parameters, a curve).
    - `3` adds a cubic term $`\delta x^3`$, and so on.
  - It returns coefficients from the **highest power down**. For degree 1 that is `[slope, intercept]`.

**Live demo of degree choice:**

- The instructor switched the degree to `2` (three parameters, a curve). He said that curve did not pass well through the data, so "the fitting is not good."
- With degree `1`, the line passed through the bulk of the points, which he called a good ("perfect") fit.
- The audio is garbled here. The takeaway: **choose the polynomial degree that matches the data.** The demo data was generated from a line, so degree 1 is appropriate.

### 2.6 Imports and loading the dataset

The instructor installed scikit-learn, then imported the pieces he would use. He said he would explain each one later.

```python
# pip install scikit-learn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

He then loaded the built-in dataset and inspected it.

```python
diabetes = load_diabetes(as_frame=True, scaled=False)   # see note on scaled= below
print(diabetes.DESCR)            # dataset description: columns, meanings, units
print(diabetes.feature_names)    # names of the 10 features
X_all = diabetes.data            # pandas DataFrame of features
y = diabetes.target              # disease progression one year after baseline
print(X_all.shape)               # (442, 10)
```

- **Shape is (442, 10):** 442 patients and 10 features.
  - The features are age, sex, BMI, BP, and six blood-serum measurements.
- The **target** is a quantitative measure of disease progression **one year after baseline**.
- A student asked "what is `DSC`?" This is `.DESCR`, the dataset's text description.
- A student asked whether `feature_names` is just the column names.
  - The instructor's answer was unclear in the audio.
  - In practice, `feature_names` lists the names of the feature columns. These match the DataFrame columns when `as_frame=True`.

*Inference note on `scaled=`:*

- By default, `load_diabetes()` returns features that are **already mean-centered and scaled**.
- The instructor later reported a BMI mean of about 26 and a standard deviation of about 4.5. Those are raw units, so he most likely loaded the data with `scaled=False`.
- Check this in your own notebook.

### 2.7 Exploring the target

```python
print(y.describe())     # count, mean, std, min, 25%, 50%, 75%, max

sns.histplot(y, bins=30, kde=True)     # histogram + smooth KDE curve
plt.xlabel("Disease progression score"); plt.show()
```

- `.describe()` gives summary statistics: count, mean, standard deviation, min, the 25%/50%/75% quartiles, and max.
- `sns.histplot(..., bins=30, kde=True)` draws a histogram with 30 bins plus a **kernel density estimate (KDE)** curve that smooths the distribution.

### 2.8 BMI vs. target: scatter plot and `regplot`

- He plotted BMI against progression.
  - The points are **not purely random**.
  - They show a rough upward linear trend, with lots of spread.
- He then used Seaborn's `regplot`, which overlays the best-fit line and a **confidence interval (CI)** band. The CI level was left at the default; `regplot` uses 95%.

```python
sns.regplot(x=X_all["bmi"], y=y, ci=95,
            scatter_kws={"s": 18, "alpha": 0.5},     # alpha value inferred
            line_kws={"color": "red", "linewidth": 2})
plt.show()
```

The plotting parameters he explained:

- `scatter_kws` passes options to the scatter points.
  - `s` is the marker size. He used 18 and showed that 30 gives bigger points.
  - `alpha` is transparency. Lower values make the points more see-through.
- `line_kws` passes options to the regression line.
  - `linewidth=2` gives a thicker line; changing it to 1 makes it thinner.

**Q: How is `regplot` different from `polyfit`?**

- With `polyfit` you write the fitting and plotting code yourself.
- `regplot` is built on NumPy, Matplotlib, and statistical routines. It does the fit and the CI band automatically.
- Both perform the same least-squares fit underneath.

### 2.9 Simple linear regression in scikit-learn (BMI only)

**Step 0a: choose X and y, then split the data.**

- 80% of the rows are used to train (learn).
- 20% are held out for validation/testing.

```python
X = X_all[["bmi"]]      # double brackets -> 2-D DataFrame (sklearn requires 2-D X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
print(len(X_train), len(X_test))     # 353, 89
```

- The resulting sizes are **353 training rows and 89 test rows**, out of 442. The audio said "533"; 353 is correct.

**What is `random_state`?**

- The split shuffles the data randomly. `random_state` **fixes the random seed**, so you get the **identical split every time you rerun** the code. This makes results reproducible.
- The instructor described `0` as "no randomness or noise." A more precise statement is:
  - any fixed integer makes the split reproducible;
  - different integers give different (but repeatable) shuffles;
  - leaving it as `None` gives a different split every run.
- It does **not** add or remove noise from the data.

**Step 0b: standardize the features (z-scores).**

For each feature, subtract the mean and divide by the standard deviation:

```math
z = \frac{x - \mu}{\sigma}
```

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # learn mu, sigma from TRAIN, then scale train
X_test_scaled  = scaler.transform(X_test)        # reuse train's mu, sigma to scale test
print(scaler.mean_[0], scaler.scale_[0])         # ~26 (mean BMI), ~4.5 (std)
```

**The four-step scikit-learn pattern: create → fit → predict → evaluate.**

**Step 1: create the model.**

```python
model = LinearRegression()
model      # notebook shows default params: fit_intercept=True, copy_X=True, n_jobs=None, positive=False
```

- At this point the model is "empty": no data has been plugged in yet.

**Step 2: fit the model.**

```python
model.fit(X_train_scaled, y_train)
alpha_std = model.intercept_
beta_std  = model.coef_[0]
```

- `alpha_std` and `beta_std` are the intercept and slope **in standardized BMI units**.

**Converting back to original BMI units.** Since $`z = (x-\mu)/\sigma`$:

```math
\hat{y} = \alpha_{\text{std}} + \beta_{\text{std}}\,\frac{x-\mu}{\sigma}
\;\Rightarrow\;
\beta_{\text{raw}} = \frac{\beta_{\text{std}}}{\sigma}, \qquad
\alpha_{\text{raw}} = \alpha_{\text{std}} - \beta_{\text{raw}}\,\mu
```

```python
beta_raw  = beta_std / scaler.scale_[0]
alpha_raw = model.intercept_ - beta_raw * scaler.mean_[0]
```

Reported results:

- **Standardized model:**
  - The standardized intercept was read as "one … 49", most likely about 149–152.
  - This equals roughly the mean of `y_train`, which is what you expect after standardizing.
- **Original units:** the instructor read the equation as

  $`\displaystyle \text{progression} \approx -180 + 10 \times \text{BMI}`$

- ⚠️ **Sanity check on the −180:**
  - A correct intercept should satisfy $`\alpha_{\text{raw}} + \beta_{\text{raw}}\,\mu \approx \bar{y}_{\text{train}} \approx 152`$.
  - With $`\beta_{\text{raw}} \approx 10`$ and $`\mu \approx 26`$, that implies $`\alpha_{\text{raw}} \approx -110`$ to $`-120`$.
  - The "−180" may be a transcription error. Verify with your own run.

**Step 3: predict.**

```python
y_pred = model.predict(X_test_scaled)

compare = pd.DataFrame({
    "BMI": X_test["bmi"].values,
    "Actual progression": y_test.values,
    "Predicted progression": y_pred,
})
compare["Error"] = compare["Actual progression"] - compare["Predicted progression"]
compare.round(1).head()
```

- Some predictions are close, but **errors of 50–100 points are common**.
- The average progression is about 152.

**Predicting for new patients.** New inputs must go through the *same* fitted scaler.

```python
new_bmi = pd.DataFrame({"bmi": [22, 28, 35]})        # example values inferred
new_pred = model.predict(scaler.transform(new_bmi))
```

**Plotting the result:**

- training points in blue;
- test points in red;
- the fitted line on top.

Some red test points sit near the line, but many are far from it.

### 2.10 Evaluation metrics: "how good is the fit?"

**Mean squared error:**

```math
\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2
```

**Root mean squared error.** This is in the same units as $`y`$, which makes it easier to interpret:

```math
\text{RMSE} = \sqrt{\text{MSE}}
```

**Coefficient of determination:**

```math
R^2 = 1 - \frac{\sum_i (y_i - \hat{y}_i)^2}{\sum_i (y_i - \bar{y})^2}
```

$`R^2`$ compares your model against a baseline model that **always predicts the average** $`\bar{y}`$:

| $`R^2`$ | Meaning |
|---|---|
| $`R^2 = 0`$ | no better than predicting the mean |
| $`R^2 = 1`$ | perfect fit |
| $`R^2 < 0`$ | worse than predicting the mean (possible on test data) |

He computed the metrics manually and then confirmed them with `sklearn.metrics`:

```python
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)
```

**BMI-only result:**

- $`R^2 \approx 0.19`$, so BMI alone explains only about **19%** of the variance in progression. The audio said "90%"; the correct figure is 19%.
- **Conclusion: a poor fit.** BMI is related to progression, but many other factors matter too.

### 2.11 Multiple linear regression (age, BMI, BP)

Progression doesn't depend on BMI alone, so three features were used:

```math
\text{progression} = \alpha + \beta_1\,\text{age} + \beta_2\,\text{BMI} + \beta_3\,\text{BP}
```

The audio once said "blood sugar". The feature list he built was age, BMI, and BP.

**Correlation heatmap:**

```python
feats = ["age", "bmi", "bp"]
corr = pd.concat([X_all[feats], y.rename("target")], axis=1).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")      # cmap inferred
plt.show()
```

How to read the heatmap:

- The diagonal is always 1, because each variable is perfectly correlated with itself.
- BMI vs. age is about **0.19**, a weak correlation.
- Target vs. BMI is about **0.6**, a moderately strong correlation.
- Target vs. age is very weak, essentially no correlation.

**Same pipeline, with more columns:**

```python
X_multi = X_all[feats]
X_train, X_test, y_train, y_test = train_test_split(
    X_multi, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

model = LinearRegression().fit(X_train_scaled, y_train)
print(model.intercept_)                                   # ~151
coefs = pd.Series(model.coef_, index=feats)
coefs.plot(kind="bar"); plt.show()                        # bar plot of standardized betas

y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred); rmse = np.sqrt(mse); r2 = r2_score(y_test, y_pred)
```

- The intercept is $`\alpha \approx 151`$.
- The standardized coefficients are shown as a bar plot. Because all features are standardized, their bar heights **can be compared**.

**Reported metrics (the audio is ambiguous here):**

- The instructor read MSE ≈ 4150, RMSE ≈ 64, and an $`R^2`$ heard as "49" / "point two-something".
  - The MSE and RMSE are consistent with each other ($`\sqrt{4150} \approx 64`$).
  - The exact $`R^2`$ is unclear; recompute it yourself.
- The clear message: **$`R^2`$ improved over BMI alone, but it is still far from 1.**

**Final plot:** actual vs. predicted progression on the test set, with the original values in blue and the fitted values overlaid.

### 2.12 Q&A at the end

**Q1: What is the difference between `fit_transform` and `transform`?**

- `fit_transform(X_train)` does two things:
  - it **learns** the mean and standard deviation from the training data;
  - then it scales that training data.
- `transform(X_test)` **only applies** the already-learned training mean and standard deviation.
- Why not `fit_transform` on the test set? The test set is held out purely to **validate** the model, as stand-in ground truth. It must not influence fitting in any way, including the scaling statistics.
- Fitting the scaler on test data would leak information from the test set into the model. This is called **data leakage**.

**Q2: Why build the fitted line manually instead of just using `sns.regplot`?**

- `regplot` and `polyfit` are fine for simple one-feature visualizations.
- Real datasets have many columns (here, 10). You need a proper model object for:
  - fitting multiple features;
  - getting the coefficients;
  - predicting new cases;
  - computing metrics.
- scikit-learn provides this through built-in functions, without writing the math from scratch.

---

## 3. Functions, keywords, and built-ins introduced

**NumPy**

| Item | What it does |
|---|---|
| `np.random.default_rng(seed)` | creates a random number generator |
| `rng.normal(loc, scale, size)` | draws Gaussian (normal) random numbers; used here to add noise |
| `np.polyfit(x, y, deg)` | least-squares polynomial fit; returns coefficients from the highest power down |
| `np.sqrt` | square root; used to get RMSE from MSE |

**scikit-learn**

| Item | What it does |
|---|---|
| `load_diabetes()` | loads the built-in diabetes dataset (442 × 10) |
| `.data`, `.target`, `.feature_names`, `.DESCR` | the dataset's features, target, feature names, and text description |
| `train_test_split(X, y, test_size, random_state)` | splits the data into train and test sets |
| `StandardScaler()` | z-score standardization: $`z=(x-\mu)/\sigma`$ |
| `.fit_transform()` | learns $`\mu`$ and $`\sigma`$, then scales; use on **train only** |
| `.transform()` | scales using the stored $`\mu`$ and $`\sigma`$; use on test and new data |
| `.mean_`, `.scale_` | the learned mean and standard deviation per feature |
| `LinearRegression()` | ordinary least-squares linear model |
| `.fit(X, y)` | learns $`\alpha`$ and $`\beta`$ |
| `.predict(X)` | returns predictions $`\hat{y}`$ |
| `.intercept_` | the fitted $`\alpha`$ |
| `.coef_` | array of fitted $`\beta`$ values, one per feature |
| `mean_squared_error(y_true, y_pred)` | computes MSE |
| `r2_score(y_true, y_pred)` | computes $`R^2`$ |

**pandas**

| Item | What it does |
|---|---|
| `.describe()` | count, mean, std, min, quartiles, max |
| `.shape` | (rows, columns) |
| `.corr()` | correlation matrix |
| `pd.DataFrame({...})` | builds a comparison table |
| `.round()` | rounds displayed values |
| `.head()` | shows the first rows |

**Seaborn and Matplotlib**

| Item | What it does |
|---|---|
| `sns.histplot(..., bins=30, kde=True)` | histogram plus a KDE curve |
| `sns.regplot(..., ci=..., scatter_kws=..., line_kws=...)` | scatter plot plus regression line plus confidence band |
| `scatter_kws`: `s`, `alpha` | marker size and transparency |
| `line_kws`: `color`, `linewidth` | line color and thickness |
| `sns.heatmap(..., annot=True)` | correlation heatmap with the numbers written in |
| `plt.scatter`, `plt.plot`, `plt.xlabel`, `plt.ylabel`, `plt.legend`, `plt.show` | basic Matplotlib plotting |

---

## 4. Syntax rules, common mistakes, and debugging tips

- **`X` must be 2-D** for scikit-learn. Use `df[["bmi"]]` (double brackets), not `df["bmi"]`. A 1-D `X` raises a "Expected 2D array" error.
- **Never call `fit_transform` on test data or new data.** Use `transform` with the scaler fitted on the training data. Otherwise you get data leakage and inconsistent scaling.
- **New inputs must be scaled with the same scaler** before calling `.predict()`.
- **Coefficients from a standardized model are in standardized units.** Convert them with $`\beta_{\text{raw}} = \beta_{\text{std}}/\sigma`$ and $`\alpha_{\text{raw}} = \alpha_{\text{std}} - \beta_{\text{raw}}\mu`$ to interpret them in real units.
- **Compare coefficient magnitudes only when features share a scale.** Standardizing makes this valid.
- **Set `random_state`** so your split, and therefore your metrics, are reproducible.
- **`np.polyfit` returns coefficients highest power first.** For degree 1 that is `[slope, intercept]`, not `[intercept, slope]`.
- **Pick the polynomial degree to match the data.** A higher degree is not automatically better.
- **Check your numbers:** RMSE should equal $`\sqrt{\text{MSE}}`$, and the line in original units should predict roughly $`\bar{y}`$ at $`x=\mu`$.
- `load_diabetes()` features are **pre-scaled by default**. Use `scaled=False` if you want real BMI values (mean about 26).
- "Regression" in ML is **not** "regression testing" in software QA.

---

## 5. Exam and assignment notes

- **No explicit exam hints were given** in this session.
- **Project:** the instructor said the next class might discuss **the project to be submitted**, or continue the remaining material. Students asked about the submission date and were told it would be covered then. **Bring questions about the project to the next class.**
- Concepts worth knowing cold (from emphasis in class):
  - the 4-step create → fit → predict → evaluate workflow;
  - the purpose of a train/test split;
  - `fit_transform` vs. `transform`;
  - formulas and interpretation of MSE, RMSE, and $`R^2`$, including what $`R^2 = 0`$ and $`R^2 = 1`$ mean;
  - interpreting the sign and magnitude of $`\beta`$;
  - the least-squares objective.

<!-- nav -->
← [Session 19 (2026-11-13)](DSM-102-19_2026-11-13_Abhirup-Datta.md) · [All lectures](./) · [Session 21 (2026-11-16)](DSM-102-21_2026-11-16_Abhirup-Datta.md) →
<!-- /nav -->
