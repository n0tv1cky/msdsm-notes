---
course: DSM 102
date: 2026-10-30
start: 7:00pm
session: "17"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 16 (2026-10-26)](DSM-102-16_2026-10-26_Abhirup-Datta.md) · [All lectures](./) · [Session 18 (2026-11-02)](DSM-102-18_2026-11-02_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 Lecture 17: Probability Distributions in Data Science

*Session: DSM-102-16, 2026-10-30, Abhirup Datta. Jupyter/Python demo using NumPy, SciPy, Matplotlib, Seaborn and ipywidgets, with astronomy examples throughout.*

> **Note on reconstruction:** The audio was heavily garbled. Formulas follow from standard definitions and are certain. Several numbers were checked by recomputing them, and that is noted wherever it applies. Code blocks are reconstructed from the spoken walkthrough. Exact variable names, array sizes and plot styling are inferred, and inline comments mark the uncertain parts.

---

## 1. Overview

This session introduced **probability distributions** as the tool for modelling uncertainty and variability in data. They are used in parameter estimation, hypothesis testing, inference and ML predictions.

The running theme was astronomy as a data science. Every measurement has noise, and a claimed "5σ detection" is really a probability statement.

The lecture covered the following, in order:

- **Random variables**, and the difference between discrete and continuous ones.
- The three descriptive functions: **PMF**, **PDF** and **CDF**.
- Discrete distributions:
  - **Bernoulli** (clear vs. cloudy night).
  - **Binomial** (planet transits among 20 stars).
  - **Poisson** (photon counts and photon noise).
- The **Normal/Gaussian** distribution (sky background noise, σ detection thresholds, 1σ/2σ/3σ shaded intervals).

Each idea was shown in Python using `numpy`, `scipy.stats`, `matplotlib`, `seaborn` and `ipywidgets`. Student questions led to explanations of `try/except`, `rng`, `.ravel()`, f-string format specifiers like `:.2f`, `math.comb`, and `enumerate` in a `for` loop.

The geometric distribution and the remaining continuous distributions were deferred to the next class.

---

## 2. Topics Covered (in order)

### 2.1 Why probability distributions?

- Before building models, you need to understand **how the values in a dataset are spread out**. Distributions describe this.
- They are used in:
  - statistical analysis: parameter estimation, hypothesis testing, inference;
  - ML algorithms: modelling uncertainty in predictions.
- Astronomy motivating questions:
  - Is a galaxy catalogue symmetric or clumpy?
  - How large is the **photon noise** in an observation?
  - What are the measurement errors?
  - What does a "**5σ detection**" mean? It is a probability statement derived from the normal distribution.

### 2.2 Notebook setup

The libraries loaded were NumPy, Matplotlib, Seaborn, `scipy.stats` and `ipywidgets` (optional, wrapped in `try/except`).

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import math

# Optional interactive widgets -- don't crash if not installed
try:
    from ipywidgets import interact, IntSlider, FloatSlider
except ImportError:
    print("ipywidgets not available -- install with: pip install ipywidgets")
```

**`try/except` explanation (from Q&A):**
- Put code that *might* fail inside `try`. Examples are a library that isn't installed or a variable that isn't defined.
- If it fails with the named error, here `ImportError`, Python runs the `except` block instead of crashing.
- In this notebook, the `except` block prints a message suggesting you install the package.

**`ipywidgets` explanation (from Q&A):**
- It renders interactive HTML controls (sliders) inside the notebook, which gives better visualisation.
- `interact` connects a function to those controls.
- `IntSlider` and `FloatSlider` create integer and float sliders.
- The instructor suggested reading the ipywidgets documentation for more detail.

### 2.3 Random variables: discrete vs. continuous

- A probability distribution tells you two things:
  1. **which values** a random quantity can take;
  2. **how likely** each value is.
- A **random variable** $X$ assigns a number to each outcome.

The instructor showed this table:

| Random variable | Type |
|---|---|
| Number of photons hitting one CCD pixel in 1 second | Discrete (a count) |
| Number of planets found around a star | Discrete (a count) |
| Apparent magnitude of a star measured on two nights | Continuous |
| "Rate" of a galaxy (audio unclear; probably **redshift**) | Continuous |

### 2.4 Demo: simulated CCD image of an empty sky

- **Setup:** an empty sky with no sources, where each pixel collects on average about **24 counts** (photons). The counts were drawn from a **Poisson** distribution.
- **Result:** the printed standard deviation was **4.52**.
- **Interpretation:** you cannot see any bright or faint sources. The image is **dominated by noise**. You need to know what "ordinary randomness" looks like before you can find real signals, and distributions give you that.

```python
rng = np.random.default_rng(42)          # random number generator, seed = 42

# Poisson-distributed counts, mean ~24 per pixel
# (size spoken as "40 by 40"; see note below)
sky = rng.poisson(lam=24, size=(40, 40))

print(f"mean = {sky.mean():.2f}, std = {sky.std():.2f}")

# 2D image
plt.imshow(sky, cmap="gray", origin="lower")
plt.colorbar(label="counts")
plt.title("Simulated empty-sky CCD image")
plt.show()

# Flatten 2D -> 1D, then histogram of pixel values
pixels = sky.ravel()
print(sky.shape, pixels.shape)
sns.histplot(pixels, discrete=True)
plt.xlabel("counts per pixel")
plt.show()
```

*Inferred details in this code:*
- The array size was spoken as "40 by 40", but the instructor also said the flattened length was "~106,000". Those two do not match: a 40×40 array has 1,600 elements.
- For a Poisson distribution with $\lambda=24$, the expected std is $\sqrt{24}\approx 4.90$. The printed 4.52 does not quite match, so the exact $\lambda$ or size may differ.
- The plotting style (`cmap`, `discrete=True`) is a guess.

**Q&A points from this demo:**

- **What is `rng`?**
  - It is a random number generator object created with `np.random.default_rng(seed)`.
  - The seed **42** makes results reproducible.
  - `rng.poisson(lam, size)` draws Poisson samples.
- **What is `sky.ravel()`?**
  - It flattens a 2D array (e.g. 40×40) into a 1D array, pixel by pixel.
  - This is needed to make a histogram of all pixel values.
  - Use `.shape` to check the dimensions before and after.
- **What does `:.2f` mean in `print(f"... {std:.2f}")`?**
  - It is a format specifier: show the value as a float with **2 decimal places**.
  - `:.0f` gives 0 decimals (looks like an integer), `:.3f` gives 3 decimals, and so on.
- **Why Poisson here, rather than another distribution?**
  - Pixel counts are discrete counts, and Poisson is the basic model for them.
  - With many samples or a large mean, a Gaussian could also be used. The choice depends on your data.

### 2.5 The three functions: PMF, PDF, CDF

**PMF (probability mass function)** applies to **discrete** variables:

```math
p(x) = P(X = x), \qquad \sum_x p(x) = 1
```
It gives the probability of each exact value.

**PDF (probability density function)** applies to **continuous** variables. Here probability is an **area**:

```math
P(a \le X \le b) = \int_a^b f(x)\,dx, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1
```

**CDF (cumulative distribution function)** works for **both** types:

```math
F(x) = P(X \le x)
```
It always lies between 0 and 1 and **never decreases**.

**Worked Example A (discrete): planets per star**

A small survey found:

| Planets per star | Probability |
|---|---|
| 0 | 50% |
| 1 | 30% |
| 2 | 15% |
| 3 | 5% |

*The probabilities were reconstructed. These values are consistent with every answer stated in class.*

- Exactly 2 planets: $P(X=2) = 0.15$.
- At most 2 planets: $F(2) = P(X\le 2) = 0.5+0.3+0.15 = 0.95$.
- At least one planet: $P(X\ge 1) = 1 - 0.5 = 0.5$.
- Expected value: multiply each value by its probability and sum.

```math
E[X] = \sum_x x\,p(x) = 0(0.5) + 1(0.3) + 2(0.15) + 3(0.05) = 0.75 \text{ planets per star}
```

**Worked Example B (continuous): repeated magnitude measurements**

- A standard star's measured magnitude scatters around $\mu = 12$ with error $\sigma = 0.05$ mag.
- The probability that one measurement lies between two values is the **area under the PDF**.
- Taking the interval as $\mu \pm 2\sigma$ (the bounds are inferred; the result was ≈0.95):

```math
P(11.9 \le m \le 12.1) = \int_{11.9}^{12.1} f(m)\,dm \approx 0.95
```
- **Key point:** for a continuous variable, $P(m = 12) = 0$ exactly. Only ranges have probability. $f(m)$ is a **density**, not a probability.

**Comparison figure (PMF vs PDF vs CDF)**

The instructor made three panels: the PMF bar chart of planets per star, the normal PDF of magnitudes, and the CDF.
- Use the **PMF** for discrete values.
- Use the **PDF** for continuous values and for intervals or confidence ranges.
- The **CDF** works for both.

```python
x_pl = np.array([0, 1, 2, 3])
p_pl = np.array([0.50, 0.30, 0.15, 0.05])

mu, sigma = 12, 0.05
m = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)

fig, ax = plt.subplots(1, 3, figsize=(14, 4))
ax[0].bar(x_pl, p_pl, color="tab:blue", label="PMF")
ax[0].set_xlabel("x (planets)")
ax[0].set_ylabel("P(X=x)")

ax[1].plot(m, stats.norm.pdf(m, loc=mu, scale=sigma), color="tab:orange", label="PDF")

ax[2].plot(m, stats.norm.cdf(m, loc=mu, scale=sigma), color="tab:green", label="CDF")

for a in ax:
    a.legend()
plt.show()
```

*Inferred: variable names `x_pl`/`p_pl` (spoken "XPL"/"PPL"), plotting details. The instructor said the PDF/CDF values came from `scipy.stats` normal functions.*

### 2.6 Bernoulli distribution

**Definition:** a single trial with exactly two outcomes.
- Success: $X=1$ with probability $p$.
- Failure: $X=0$ with probability $1-p$.
- It is the building block of the binomial and geometric distributions.

**PMF:**

```math
P(X = x) = p^{x}(1-p)^{1-x}, \qquad x \in \{0, 1\}
```

**Mean and variance (derivation shown in class):**

```math
E[X] = 0\cdot(1-p) + 1\cdot p = p
```

```math
E[X^2] = 0^2\cdot(1-p) + 1^2\cdot p = p
```

```math
\mathrm{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)
```

**Worked example: tonight at the observatory**
- The sky is clear (success) with $p = 0.6$ and cloudy with $1-p = 0.4$.
- Mean: $E[X] = 0.6$.
- Variance: $p(1-p) = 0.6 \times 0.4 = 0.24$.

```python
p = 0.6
p_clear  = stats.bernoulli.pmf(1, p)   # 0.6
p_cloudy = stats.bernoulli.pmf(0, p)   # 0.4
mean, var = stats.bernoulli.mean(p), stats.bernoulli.var(p)   # 0.6, 0.24

plt.bar(["cloudy (0)", "clear (1)"], [p_cloudy, p_clear])
plt.ylabel("P(X=x)")
plt.show()
```

The `stats.bernoulli.pmf(value, p)` argument order was stated: the outcome first, then $p$.

### 2.7 Binomial distribution

**Definition:** repeat a Bernoulli trial $n$ times, where the trials are **independent** and $p$ is the **same** each time. The number of successes $X$ is then binomial.

**PMF:**

```math
P(X = k) = \binom{n}{k} p^{k}(1-p)^{n-k}, \qquad k = 0, 1, \dots, n
```

**Binomial coefficient:**

```math
\binom{n}{k} = \frac{n!}{k!\,(n-k)!}
```

**Mean and variance:**

```math
E[X] = np, \qquad \mathrm{Var}(X) = np(1-p)
```

Here $n$ is the number of trials and $p$ is the success probability.

**Worked example: planet transits**

1. **Transit probability.** A planet transits only if its orbit is nearly edge-on to us. For random orientations:

```math
p \approx \frac{R_\star}{a}
```
2. **Plug in a hot Jupiter around a Sun-like star.**
   - Orbit: $a = 0.05$ AU.
   - Star radius: $R_\star = 6.96 \times 10^{5}$ km.
   - Conversion: $1\ \text{AU} = 1.496\times10^{8}$ km.
   - Result:

```math
p = \frac{6.96\times10^{5}}{0.05 \times 1.496\times10^{8}} \approx 0.093 \approx 0.1
```
3. **Set up the binomial.** Take $n = 20$ stars, each hosting a hot Jupiter. Then $X$, the number of transits, follows $X \sim \text{Binomial}(20, p)$.
4. **Exactly 2 transits (by hand, $p = 0.1$):**

```math
P(X=2) = \binom{20}{2}(0.1)^2(0.9)^{18} = 190 \times 0.01 \times 0.1501 \approx 0.285
```
5. **No transit:**

```math
P(X=0) = (0.9)^{20} \approx 0.122
```

**Code and results:**
- In code, the instructor computed $p$ from the constants (giving ≈0.093) and evaluated the PMF with `scipy`.
- Code values for $k=0,1,2$ were spoken but were not reliably audible. With $p=0.093$ you should get roughly $P(0)\approx0.14$, $P(1)\approx0.29$, $P(2)\approx0.28$.
- The hand calculation with $p=0.1$ gave 0.285. The instructor showed the code and hand values agree.
- He also simulated many 20-star surveys, histogrammed the number of transits, and overlaid the binomial PMF. The histogram matched it.

```python
R_star = 6.96e5            # km
AU     = 1.496e8           # km
a      = 0.05 * AU
p      = R_star / a        # ~0.093
n      = 20

# By-hand formula vs scipy
p2_hand  = math.comb(20, 2) * p**2 * (1 - p)**(n - 2)   # math.comb(20,2) = 190
p2_scipy = stats.binom.pmf(2, n, p)
print(f"P(X=2): hand = {p2_hand:.4f}, scipy = {p2_scipy:.4f}")
print(f"P(X=0) = {stats.binom.pmf(0, n, p):.4f}")
print(f"mean = {stats.binom.mean(n, p):.3f}, std = {stats.binom.std(n, p):.3f}")

# Simulation vs theory
sims = rng.binomial(n, p, size=10_000)
k = np.arange(0, 11)
plt.hist(sims, bins=np.arange(-0.5, 11.5, 1), density=True, alpha=0.6, label="simulated")
plt.plot(k, stats.binom.pmf(k, n, p), "o-", label="binomial PMF")
plt.xlabel("number of transits")
plt.ylabel("probability")
plt.legend()
plt.show()
```

*Inferred: the simulation size, bins, and x-range (the instructor mentioned "10"). A student asked about the line computing `comb(20, 2)`: it is $\binom{20}{2} = 190$.*

**Interactive version (ipywidgets):**
- The instructor applied the clear-night Bernoulli example to $n$ nights (e.g. 20) and plotted the binomial PMF of the number of clear nights.
- Sliders let you change $n$ and $p$, and the plot re-runs automatically.

```python
def plot_clear_nights(n=20, p=0.6):
    k = np.arange(0, n + 1)
    plt.bar(k, stats.binom.pmf(k, n, p))
    plt.xlabel("number of clear nights")
    plt.ylabel("probability")
    plt.show()

interact(plot_clear_nights,
         n=IntSlider(min=1, max=50, value=20),
         p=FloatSlider(min=0.0, max=1.0, step=0.05, value=0.6))
```

*Slider ranges are inferred.*

### 2.8 Poisson distribution

The instructor called this "the most important discrete distribution used in astronomy".

**Definition:**
- $X$ is the number of events in a fixed interval.
- Events occur **independently** at a **constant average rate** $\lambda$.

**PMF:**

```math
P(X = k) = \frac{\lambda^{k} e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \dots
```

Here $\lambda$ is the mean number of events per interval.

**Connection to the binomial:** take $n \to \infty$ and $p \to 0$ with $np = \lambda$ fixed, and the binomial PMF becomes the Poisson PMF.

**Key property:** the mean equals the variance.

```math
E[X] = \mathrm{Var}(X) = \lambda
```

**Why astronomers care (photon noise):**
- Photons arrive randomly and independently at a steady rate, so photon counts are Poisson.
- **Noise** is the standard deviation, $\sqrt{\lambda}$ (or $\sqrt{N}$ for $N$ counts).
- **Signal-to-noise ratio:**

```math
\text{S/N} = \frac{N}{\sqrt{N}} = \sqrt{N}
```

**Worked example: a faint star sending $\lambda = 4$ photons/s to one pixel**

Exactly 2 photons in 1 second:

```math
P(X=2) = \frac{4^2 e^{-4}}{2!} = 8e^{-4} \approx 0.1465
```

No photons:

```math
P(X=0) = e^{-4} \approx 0.0183
```

Exactly 6 photons (the audio said "six … 0.1"; checked by recomputing):

```math
P(X=6) = \frac{4^6 e^{-4}}{6!} \approx 0.104
```

```python
lam = 4
for k in [0, 2, 6]:
    by_hand = lam**k * math.exp(-lam) / math.factorial(k)
    print(k, f"{by_hand:.4f}", f"{stats.poisson.pmf(k, lam):.4f}")

k = np.arange(0, 15)
plt.bar(k, stats.poisson.pmf(k, lam))
plt.axvline(lam, color="red", ls="--", label=r"mean $\lambda$")
plt.xlabel("photons per second")
plt.ylabel("probability")
plt.legend()
plt.show()
```

### 2.9 Geometric distribution

This was mentioned only briefly as another discrete distribution built on Bernoulli trials. No details were given, and it is deferred to the next class.

### 2.10 Continuous distributions: Normal (Gaussian)

**General rule:** for continuous variables, probability is the **area under the PDF**.

**Description:**
- Symmetric and **bell-shaped**; values cluster around the mean.
- Measurement errors are usually normal.
- **Central Limit Theorem:** sums or averages of many independent random variables tend to be normally distributed.

**PDF:**

```math
f(x) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
```

Here $\mu$ is the centre (mean) and $\sigma$ is the spread (standard deviation).

**Z-score:**

```math
z = \frac{x - \mu}{\sigma}
```

**Worked example: sky background noise**
- Background noise is approximately normal.
- A pixel that is $k\sigma$ above the background could be a noise fluctuation. The chance that noise alone produces a value at least that high is the **one-sided tail probability**:

```math
P(Z \ge k) = 1 - \Phi(k)
```
- $\Phi$ is the standard normal CDF. In code this is `stats.norm.sf(k)` or `1 - stats.norm.cdf(k)`.

| Threshold | One-sided false-alarm probability |
|---|---|
| $1\sigma$ | $\approx 1.59\times10^{-1}$ (stated in class) |
| $3\sigma$ | $\approx 1.35\times10^{-3}$ |
| $5\sigma$ | $\approx 2.87\times10^{-7}$ |

*The 3σ and 5σ values are standard figures; the spoken numbers were inaudible.*

**Interpretation:**
- A 1σ "detection" happens by chance about 16% of the time, so it is meaningless.
- A 5σ detection is extremely unlikely to come from noise alone. This is why "5σ" is the discovery standard.

```python
for k in [1, 2, 3, 5]:
    print(f"{k} sigma: P(noise >= {k} sigma) = {stats.norm.sf(k):.3e}")
```

**Shaded-interval plot (1σ, 2σ, 3σ)**

| Interval | Area (probability) |
|---|---|
| $\mu\pm1\sigma$ | ≈ **68.27%** |
| $\mu\pm2\sigma$ | ≈ **95.45%** |
| $\mu\pm3\sigma$ | ≈ **99.73%** |

*The audio said "99.9%". The correct standard value is 99.73%.*

- Each area is computed from the CDF:

```math
P(\mu - k\sigma \le X \le \mu + k\sigma) = \Phi(k) - \Phi(-k)
```
- Vertical lines mark the mean and the ±5σ positions.

```python
x = np.linspace(-6, 6, 1000)
pdf = stats.norm.pdf(x)

plt.plot(x, pdf, color="black")

# Widest region first so narrower ones are drawn on top
for i, (z, c) in enumerate(zip([3, 2, 1], ["tab:blue", "tab:green", "tab:orange"])):
    mask = (x >= -z) & (x <= z)
    area = stats.norm.cdf(z) - stats.norm.cdf(-z)
    plt.fill_between(x[mask], pdf[mask], color=c, alpha=0.5,
                     label=f"±{z}σ: {area*100:.2f}%")
    print(i, z, c, f"{area:.4f}")

plt.axvline(0, color="red", ls="--")              # mean
for s in [-5, 5]:
    plt.axvline(s, color="gray", ls=":")          # 5-sigma lines
plt.xlabel("z (σ from mean)")
plt.ylabel("PDF")
plt.legend()
plt.show()
```

*Inferred: the exact colours (blue for 3σ was stated; 2σ appeared to be green), and whether `zip` was used alongside `enumerate`.*

**Q&A: the `for` loop with `enumerate`**
- `enumerate(seq)` gives pairs `(index, value)`.
- For the list of sigma levels `[3, 2, 1]`:
  - index 0 → 3σ (blue),
  - index 1 → 2σ,
  - index 2 → 1σ.
- The loop variables (`i`, `z`, `c` …) are just names you choose.
- The instructor's advice: **you can change the colours and play with the code** to see how it works.

---

## 3. Functions, keywords and operators introduced

| Item | One-line explanation |
|---|---|
| `import` / `from … import …` | Load libraries or specific names. |
| `try:` / `except ImportError:` | Attempt code; if the import fails, run a fallback instead of crashing. |
| `np.random.default_rng(42)` | Create a seeded random number generator (reproducible results). |
| `rng.poisson(lam, size)` | Draw Poisson-distributed random counts. |
| `rng.binomial(n, p, size)` | Draw binomial random counts (used for simulation). |
| `.mean()`, `.std()` | Array mean and standard deviation. |
| `.shape` | Dimensions of an array, e.g. `(40, 40)`. |
| `.ravel()` | Flatten a multi-dimensional array to 1D. |
| f-string `f"{x:.2f}"` | Format a number with 2 decimals (`.0f`, `.3f`, `.3e` for scientific). |
| `np.arange`, `np.linspace` | Integer ranges and evenly spaced float grids. |
| `math.comb(n, k)` | Binomial coefficient $\binom{n}{k}$. |
| `math.factorial(k)` | $k!$ |
| `math.exp(x)` | $e^{x}$ |
| `stats.bernoulli.pmf(x, p)` | Bernoulli PMF; also `.mean(p)`, `.var(p)`. |
| `stats.binom.pmf(k, n, p)` | Binomial PMF; also `.mean`, `.std`. |
| `stats.poisson.pmf(k, lam)` | Poisson PMF. |
| `stats.norm.pdf(x, loc, scale)` | Normal density. |
| `stats.norm.cdf(x)` | Normal CDF $\Phi(x)$. |
| `stats.norm.sf(x)` | Survival function $1-\Phi(x)$ (one-sided tail). |
| `plt.imshow`, `plt.colorbar` | Display a 2D array as an image, with a colour scale. |
| `sns.histplot`, `plt.hist` | Histograms. |
| `plt.bar` | Bar chart (for PMFs). |
| `plt.fill_between` | Shade the area under a curve. |
| `plt.axvline` | Draw a vertical line. |
| `for … in …:` | Loop over a sequence. |
| `enumerate(seq)` | Loop with index and value together. |
| `interact`, `IntSlider`, `FloatSlider` | ipywidgets: interactive sliders that re-run a plotting function. |

---

## 4. Syntax rules, common mistakes and tips mentioned

- **Wrap optional imports in `try/except ImportError`.** The notebook then still runs, and it tells you what to install.
- **Set a seed** (`default_rng(42)`) so random results are reproducible.
- **Flatten 2D arrays with `.ravel()` before making a histogram.** Check `.shape` before and after.
- **Use `:.Nf` to control decimal places** in printed output.
- **Check `scipy.stats` argument order.** For `pmf`, the outcome comes first, then the parameters: `bernoulli.pmf(1, p)`, `binom.pmf(k, n, p)`, `poisson.pmf(k, lam)`.
- **Verify library results with a hand calculation.** The binomial hand calculation was compared with `stats.binom.pmf` and they agreed.
- **Conceptual pitfall:** a PDF value is **not** a probability. For continuous variables $P(X=x)=0$; only intervals have probability.
- **Choosing a distribution:** Poisson or binomial for discrete counts; Gaussian for continuous data or large samples. "It depends on your sample."

---

## 5. Exam/assignment flags

- No exam or assignment emphasis was stated explicitly.
- Implicitly central (they were repeated or used as worked examples):
  - the mean and variance formulas for Bernoulli ($p$, $p(1-p)$), binomial ($np$, $np(1-p)$) and Poisson (both $\lambda$);
  - PMF vs PDF vs CDF;
  - the 68–95–99.7 rule;
  - the meaning of a 5σ detection.
- **Next class:** the geometric distribution and the remaining (continuous) distributions.

<!-- nav -->
← [Session 16 (2026-10-26)](DSM-102-16_2026-10-26_Abhirup-Datta.md) · [All lectures](./) · [Session 18 (2026-11-02)](DSM-102-18_2026-11-02_Abhirup-Datta.md) →
<!-- /nav -->
