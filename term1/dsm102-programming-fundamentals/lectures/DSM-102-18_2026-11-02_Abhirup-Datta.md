---
course: DSM 102
date: 2026-11-02
start: 7:00pm
session: "18"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 17 (2026-10-30)](DSM-102-17_2026-10-30_Abhirup-Datta.md) · [All lectures](./) · [Session 19 (2026-11-13)](DSM-102-19_2026-11-13_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 Lecture 18: Continuous Distributions and Their Summary Statistics

**Instructor:** Abhirup Datta · **Date:** 2026-11-02

> **About this reconstruction:** The transcript is noisy. Many formulas were read aloud incorrectly or partially, and code was described rather than read out. In these notes:
> - Formulas are given in their standard correct form. Where the spoken version differed, this is flagged with ⚠️.
> - Code blocks are **best-effort reconstructions** using standard `numpy` / `scipy.stats` / `pandas` / `matplotlib` idioms. Exact variable names, parameter values and plot styling are **inferred** unless stated otherwise.

---

## 1. Overview

This session moves from discrete to **continuous probability distributions**. For a continuous distribution, probability is the *area under the probability density function (PDF)*.

The lecture first sets up a general toolkit for summarising any continuous PDF:
- raw and central moments;
- mean, median and mode;
- variance, standard deviation and coefficient of variation;
- skewness and (excess) kurtosis.

Each idea is visualised in Python with `scipy.stats`, `numpy`, `pandas` and `matplotlib`. The toolkit is then applied, mostly with astronomy examples, to these distributions:
- **exponential** (photon arrival gaps);
- **gamma**;
- **normal/Gaussian** (sky noise, $`3\sigma`$/$`5\sigma`$ detections, the Hubble tension);
- the **Central Limit Theorem** (Poisson photon counts becoming Gaussian);
- **uniform** (eclipsing-binary phase, isotropic gamma-ray bursts);
- **beta** (Galaxy Zoo spiral fractions, Bayesian posteriors);
- **chi-square** (goodness of fit);
- **log-normal** (stellar masses).

Results are checked both analytically and by numerical integration or simulation. The session ends with a comparison chart of all the distributions.

---

## 2. Topics Covered, in Order

### 2.1 Probability for continuous variables
- $`P(a \le X \le b) = \int_a^b f(x)\,dx`$, the area under the PDF.
- Normalisation: $`\int_{-\infty}^{\infty} f(x)\,dx = 1`$.
- The discrete analogue uses sums, e.g. $`\mu = \sum_i x_i\,p(x_i)`$. The instructor called this "the other side of the same coin."

### 2.2 Moments
- **Raw moment** of order $`n`$:

```math
\mu'_n = E[X^n] = \int_{-\infty}^{\infty} x^n f(x)\,dx
```
- **Central moment** of order $`n`$, where $`\mu`$ is the mean:

```math
\mu_n = E[(X-\mu)^n] = \int_{-\infty}^{\infty} (x-\mu)^n f(x)\,dx
```
- All the summary statistics below are built from these moments.

### 2.3 Mean, median, mode
- **Mean:**

```math
\mu = \int_{-\infty}^{\infty} x\,f(x)\,dx
```
  The instructor described this as the area under the curve $`y = x f(x)`$.
- **Median $`m`$:**

```math
\int_{-\infty}^{m} f(x)\,dx = \tfrac{1}{2}
```
- **Mode:** the peak of the PDF. It satisfies $`f'(x)=0`$, and the second-derivative check $`f''(x) < 0`$ confirms a maximum.

**Ordering rules (likely exam material):**

| Shape | Ordering |
|---|---|
| Symmetric | mean $`=`$ median $`=`$ mode |
| Right-skewed (long right tail) | mode $`<`$ median $`<`$ mean |
| Left-skewed (long left tail) | mean $`<`$ median $`<`$ mode |

**Astronomy context:**
- Stellar masses, photon gaps and galaxy luminosities give **right-skewed** curves.
- A fraction near an upper limit gives a **left-skewed** curve. An example is a beta distribution with $`\alpha > \beta`$.

**Pearson's empirical rule** (moderately skewed distributions):

```math
\text{mean} - \text{mode} \approx 3\,(\text{mean} - \text{median})
```
⚠️ The transcript only said "mean minus mode should be nearly equal to 3". The full rule is the one above.

### 2.4 Variance, standard deviation, coefficient of variation
- **Variance:**

```math
\sigma^2 = \int_{-\infty}^{\infty} (x-\mu)^2 f(x)\,dx = E[X^2] - \mu^2
```
- **Standard deviation** $`\sigma`$ has the same units as $`x`$, so it reads directly as an error bar.
- **Coefficient of variation:**

```math
\mathrm{CV} = \sigma/\mu
```
  It is unitless and measures spread relative to the mean.
- **Photon-count example (Poisson with mean $`\lambda`$):** $`\sigma = \sqrt{\lambda}`$, so

```math
\mathrm{CV} = \frac{\sqrt{\lambda}}{\lambda} = \frac{1}{\sqrt{\lambda}}.
```
  This is the reciprocal of the signal-to-noise ratio, $`\mathrm{SNR} = \sqrt{\lambda}`$.

### 2.5 Skewness and kurtosis
- **Skewness** is the standardised third central moment and measures asymmetry:

```math
\gamma_1 = \frac{\mu_3}{\sigma^3}
```

  | Value | Meaning |
  |---|---|
  | $`\gamma_1 > 0`$ | long right tail (right-skewed) |
  | $`\gamma_1 = 0`$ | symmetric |
  | $`\gamma_1 < 0`$ | long left tail (left-skewed) |

- **Kurtosis** is the standardised fourth central moment and measures how heavy the tails are:

```math
\beta_2 = \frac{\mu_4}{\sigma^4}, \qquad \gamma_2 = \beta_2 - 3 \quad (\text{excess kurtosis})
```
  For the normal distribution, $`\beta_2 = 3`$, so $`\gamma_2 = 0`$.

  | Value | Tails | Name | Outliers |
  |---|---|---|---|
  | $`\gamma_2 > 0`$ | heavier than normal | leptokurtic | more outliers |
  | $`\gamma_2 = 0`$ | normal | mesokurtic | — |
  | $`\gamma_2 < 0`$ | lighter than normal | platykurtic | few or no extremes |

- **Key insight:** "kurtosis lives in the tails". It shows up clearly when the PDF is plotted on a **log y-axis**.

### 2.6 Python demo: visualising skewness
Three PDFs were plotted with their mean, median and mode marked:

| Distribution | Mean | Median | Mode | Note |
|---|---|---|---|---|
| Right-skewed: gamma, $`k=2`$, $`\theta=1`$ | 2 | 1.68 | 1 | |
| Symmetric: standard normal | 0 | 0 | 0 | |
| Left-skewed: beta | 0.75 | $`\approx 0.77`$ | 0.83 | values consistent with $`\text{Beta}(6,2)`$ |

⚠️ The beta parameters are inferred. The spoken median was garbled ("0. … 1 2"); $`\text{Beta}(6,2)`$ gives median $`\approx 0.771`$ and mode $`5/6 \approx 0.833`$. The instructor noted you can change the parameters or ranges yourself.

```python
# Reconstruction (inferred): skewness demo
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dists = [
    ("Right-skewed: Gamma(k=2)", stats.gamma(a=2, scale=1), np.linspace(0, 10, 500)),
    ("Symmetric: Normal(0,1)",   stats.norm(0, 1),          np.linspace(-4, 4, 500)),
    ("Left-skewed: Beta(6,2)",   stats.beta(6, 2),          np.linspace(0, 1, 500)),
]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (label, d, x) in zip(axes, dists):
    ax.plot(x, d.pdf(x), "k")
    mean, median = d.mean(), d.median()
    mode = x[np.argmax(d.pdf(x))]          # numerical mode = argmax of PDF
    ax.axvline(mean, color="r", label=f"mean={mean:.2f}")
    ax.axvline(median, color="g", ls="--", label=f"median={median:.2f}")
    ax.axvline(mode, color="b", ls=":", label=f"mode={mode:.2f}")
    ax.set_title(label); ax.set_xlabel("x"); ax.set_ylabel("density"); ax.legend()
plt.tight_layout(); plt.show()
```

### 2.7 Python demo: same mean, same variance, different kurtosis
Four distributions were plotted on the same axes, all standardised to mean 0 and variance 1 so that only the tails differ:

| Distribution | Plot colour | Excess kurtosis $`\gamma_2`$ |
|---|---|---|
| Uniform | green | $`-1.2`$ |
| Normal | black | $`0`$ |
| Student-$`t`$, $`\nu = 5`$ degrees of freedom | — | $`6/(\nu-4) = 6`$ |
| Laplace | — | $`3`$ |

A second panel used a **log scale** to show the differences in the tails.

```python
# Reconstruction (inferred): kurtosis demo, all with mean 0, variance 1
x = np.linspace(-6, 6, 1000)
nu = 5
dists = {
    "Uniform":       stats.uniform(loc=-np.sqrt(3), scale=2*np.sqrt(3)),  # var = 1
    "Normal":        stats.norm(0, 1),
    "Student t(5)":  stats.t(df=nu, scale=np.sqrt((nu-2)/nu)),            # var = 1
    "Laplace":       stats.laplace(scale=1/np.sqrt(2)),                   # var = 2b^2 = 1
}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
for name, d in dists.items():
    m, v, s, k = d.stats(moments="mvsk")   # mean, variance, skewness, EXCESS kurtosis
    ax1.plot(x, d.pdf(x), label=f"{name}: γ2={float(k):.2f}")
    ax2.plot(x, d.pdf(x), label=name)
ax2.set_yscale("log")                      # tails become visible
ax1.legend(); ax1.set_ylabel("density")
plt.show()
```

### 2.8 Worked example: photon arrival gaps (exponential distribution)
**Setup:** photons from a sky patch hit a CCD at rate $`\lambda = 4\ \text{s}^{-1}`$. The gap $`x`$ between successive photons has PDF

```math
f(x) = \lambda e^{-\lambda x}, \quad x \ge 0.
```

⚠️ The instructor called this "a Poisson distribution". Strictly, the **counts** are Poisson and the **gaps between arrivals are exponential**.

**Analytic results:**

| Statistic | Formula | Value for $`\lambda = 4`$ |
|---|---|---|
| Mean | $`1/\lambda`$ | $`0.25`$ s |
| Variance | $`1/\lambda^2`$ | $`0.0625\ \text{s}^2`$ |
| CV | $`\sigma/\mu`$ | $`1`$ |
| Median | $`\ln 2/\lambda`$ | $`\approx 0.173`$ s (spoken as "0.175") |
| Mode | | $`0`$ |
| Skewness | | $`\gamma_1 = 2`$ |
| Excess kurtosis | | $`\gamma_2 = 6`$ |

⚠️ The variance was spoken as "$`2/\lambda^2`$". That is wrong; the correct value is $`1/\lambda^2`$. Later the mean was also misspoken as "$`1/\lambda^2`$"; it is $`1/\lambda`$.

**Numerical verification:** the instructor checked "every hand result by numerical integration of the PDF", computing the area, mean, variance, $`\mu_3`$, $`\mu_4`$ and median. The plot showed density on the y-axis against "gap between photons" on the x-axis.

```python
# Reconstruction (inferred): verify analytic results by numerical integration
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

lam = 4.0
f = lambda x: lam * np.exp(-lam * x)

area   = quad(f, 0, np.inf)[0]                                  # should be 1
mu     = quad(lambda x: x * f(x), 0, np.inf)[0]                 # 0.25
var    = quad(lambda x: (x - mu)**2 * f(x), 0, np.inf)[0]       # 1/16
mu3    = quad(lambda x: (x - mu)**3 * f(x), 0, np.inf)[0]
mu4    = quad(lambda x: (x - mu)**4 * f(x), 0, np.inf)[0]
sigma  = np.sqrt(var)
skew   = mu3 / sigma**3                                         # 2
exkurt = mu4 / sigma**4 - 3                                     # 6
median = brentq(lambda m: quad(f, 0, m)[0] - 0.5, 0, 5)         # ln2/4 ≈ 0.173
print(area, mu, var, sigma/mu, median, skew, exkurt)
```

**Simulation:** 10,000 photon gaps were drawn and stored in a `pandas` Series (unit: seconds). Counts, mean, median and standard deviation were computed. The histogram was overlaid with:
- the analytic PDF;
- a **KDE** (kernel density estimate; spoken as "skdt … estimate").

A DataFrame compared the simulated statistics with the theoretical ones.

**Results:** sample mean $`= 0.251`$, sample median $`= 0.174`$, both close to the theory.

```python
# Reconstruction (inferred): simulate photon gaps and compare with theory
import pandas as pd
rng = np.random.default_rng(42)
gaps = pd.Series(rng.exponential(scale=1/lam, size=10_000), name="gap_s")
print(gaps.describe())                     # count, mean, std, quartiles...

compare = pd.DataFrame({
    "simulated":   [gaps.mean(), gaps.median(), gaps.std()],
    "theoretical": [1/lam, np.log(2)/lam, 1/lam],
}, index=["mean", "median", "std"])
print(compare)

fig, ax = plt.subplots()
ax.hist(gaps, bins=60, density=True, alpha=0.5, label="10,000 simulated gaps")
xg = np.linspace(0, gaps.max(), 400)
ax.plot(xg, lam*np.exp(-lam*xg), "r", label="exponential PDF")
ax.plot(xg, stats.gaussian_kde(gaps)(xg), "k--", label="KDE")
ax.set_xlabel("gap between photons [s]"); ax.set_ylabel("density"); ax.legend()
plt.show()
```

### 2.9 How shape statistics change with the gamma shape parameter $`k`$
For a gamma distribution with shape $`k`$ and scale $`\theta`$:

| Statistic | Formula |
|---|---|
| Mean | $`k\theta`$ |
| Mode | $`(k-1)\theta`$ for $`k \ge 1`$ |
| Skewness | $`\gamma_1 = 2/\sqrt{k}`$ |
| Excess kurtosis | $`\gamma_2 = 6/k`$ |

⚠️ The excess kurtosis was spoken as "$`6/\sqrt{k}`$". The correct value is $`6/k`$.

The instructor spoke as if "$`k`$ is the mean". This holds for $`\theta = 1`$, where mean $`= k`$ and mode $`= k-1`$.

**Example, $`k = 2`$:** mean $`= 2`$, median $`= 1.68`$ (spoken as "7.68", an ASR error), mode $`= 1`$.

As $`k`$ increases, the skewness shrinks and the curve approaches a symmetric shape in which mean ≈ median ≈ mode.

```python
# Reconstruction (inferred): vary k
x = np.linspace(0, 30, 600)
for k in [1, 2, 5, 10, 20]:
    d = stats.gamma(a=k, scale=1)
    plt.plot(x, d.pdf(x), label=f"k={k}, γ1={2/np.sqrt(k):.2f}, γ2={6/k:.2f}")
plt.legend(); plt.xlabel("x"); plt.ylabel("density"); plt.show()
```

### 2.10 Normal (Gaussian) distribution
**PDF:**

```math
f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left[-\frac{(x-\mu)^2}{2\sigma^2}\right], \quad -\infty < x < \infty
```
- $`\mu`$ is the mean (location). Changing $`\mu`$ shifts the bell left or right.
- $`\sigma`$ is the standard deviation (spread).
- ⚠️ The transcript got the effect of $`\sigma`$ backwards ("as sigma is going high … almost delta function"). The correct statement: **larger $`\sigma`$ gives a flatter, wider curve; smaller $`\sigma`$ gives a narrower, taller curve that approaches a delta function.**

**Example: "Is it a real star or just noise?"**
- Sky background noise in an image is approximately normal.
- A bright pixel is $`z`$ standard deviations above the background.
- The chance that pure noise produces a fluctuation at least that large is the **one-sided tail probability**:

```math
P(Z \ge z) = 1 - \Phi(z) = \int_z^{\infty} \frac{1}{\sqrt{2\pi}}\, e^{-t^2/2}\,dt
```
  ⚠️ The normalising constant was spoken as "$`1/(2\sigma)`$". For the standard normal it is $`1/\sqrt{2\pi}`$.
- **Detection thresholds** are usually $`3\sigma`$ or $`5\sigma`$:
  - $`P(Z \ge 3) \approx 1.35\times10^{-3}`$, so an image with $`10^6`$ pixels gives roughly 1,350 false "$`3\sigma`$ detections" from noise alone.
  - $`P(Z \ge 5) \approx 2.9\times10^{-7}`$.
  - ⚠️ The $`10^6`$-pixel figure is an illustrative number, not from the transcript. The instructor asked "how many $`3\sigma`$ detections would you get from noise" without giving one.
- **Sigma bands** in the plot (central regions):

  | Band | Area | Plot colour |
  |---|---|---|
  | $`\pm1\sigma`$ | ≈ 68.27% | dark blue |
  | $`\pm2\sigma`$ | ≈ 95.45% | sky blue |
  | $`\pm3\sigma`$ | ≈ 99.73% | — |

  **Exercise given in class:** extend the plot to $`5\sigma`$ and see how the area/percentile changes.

**Example: the Hubble tension**

| Measurement | $`H_0`$ (km/s/Mpc) |
|---|---|
| Planck 2018 (CMB) | $`67.4 \pm 0.5`$ |
| SH0ES 2022 (Cepheids/supernovae; spoken as "choose to have" / "2s") | $`73.04 \pm 1.04`$ |

⚠️ The SH0ES uncertainty was spoken variously as "1.01" and "1.045". The published value is $`1.04`$, which also reproduces the instructor's combined error of $`1.154`$.

**Steps:**
1. Difference in means: $`\Delta = 73.04 - 67.4 = 5.64`$ (the instructor said "≈ 6").
2. Propagated (combined) error:

```math
\sigma_\Delta = \sqrt{0.5^2 + 1.04^2} \approx 1.154
```
   This is larger than either individual error.
3. Significance:

```math
z = \Delta/\sigma_\Delta \approx 5.64/1.154 \approx 4.9 \approx 5\sigma
```
4. The probability of a difference this large arising by chance is about $`10^{-6}`$.

This is "one of the biggest open questions in cosmology". In the plot, the two Gaussians were drawn side by side: Planck's is narrow and sharply peaked; SH0ES's is a wider bell.

```python
# Reconstruction (inferred): tail probabilities and Hubble tension
from scipy.stats import norm
for z in [1, 2, 3, 5]:
    print(z, "sigma: one-sided tail =", norm.sf(z),
          " central area =", norm.cdf(z) - norm.cdf(-z))

H_planck, s_planck = 67.4, 0.5
H_shoes,  s_shoes  = 73.04, 1.04
diff  = H_shoes - H_planck
sig   = np.sqrt(s_planck**2 + s_shoes**2)      # error propagation in quadrature
z     = diff / sig
print(diff, sig, z, 2*norm.sf(z))              # ~5.64, ~1.154, ~4.9, ~1e-6

x = np.linspace(64, 78, 1000)
plt.plot(x, norm.pdf(x, H_planck, s_planck), label="Planck 2018")
plt.plot(x, norm.pdf(x, H_shoes, s_shoes), label="SH0ES 2022")
plt.xlabel("$H_0$ [km/s/Mpc]"); plt.legend(); plt.show()

# sigma-band shading
x = np.linspace(-4, 4, 800)
for k, c in [(3, "lightblue"), (2, "skyblue"), (1, "darkblue")]:
    m = np.abs(x) <= k
    plt.fill_between(x[m], norm.pdf(x[m]), color=c, label=f"±{k}σ")
plt.plot(x, norm.pdf(x), "k"); plt.legend(); plt.show()
```

### 2.11 Central Limit Theorem: why bright stars have Gaussian noise
- Photon counts are **Poisson**. For a large mean, the Poisson distribution approaches a Gaussian.
- So astronomers can treat photon noise as Gaussian for **bright** sources, but **must be careful for faint ones**: with very few photons the distribution is not Gaussian.
- **Demo:** histograms of Poisson counts with mean 2, 10, 50 and 500 photons, each with a matching Gaussian overlaid.
  - At 2 photons the histogram is lumpy and skewed; no Gaussian description works.
  - As the count rises, the histogram converges to the Gaussian.
  - ⚠️ The transcript said "follow version [Poisson] distribution" at high counts. It should read **Gaussian** at high counts and Poisson at low counts.
- **Summary-statistics example:** repeated measurements of a standard star, with mean, variance $`\sigma^2`$, quartiles, IQR, skewness and kurtosis computed (no numbers given).

```python
# Reconstruction (inferred): CLT for Poisson counts
fig, axes = plt.subplots(1, 4, figsize=(16, 3.5))
for ax, lam in zip(axes, [2, 10, 50, 500]):
    counts = rng.poisson(lam, 10_000)
    ax.hist(counts, bins=range(counts.min(), counts.max()+2), density=True, alpha=0.6)
    xs = np.linspace(counts.min(), counts.max(), 300)
    ax.plot(xs, norm.pdf(xs, lam, np.sqrt(lam)), "r")   # Gaussian with mean λ, σ=√λ
    ax.set_title(f"mean = {lam} photons")
plt.show()
```

### 2.12 Exponential distribution (revisited)
- Models the waiting time between two photon arrivals:

```math
f(x) = \lambda e^{-\lambda x}, \quad x \ge 0
```
- Mean $`= 1/\lambda`$, variance $`= 1/\lambda^2`$, median $`= \ln 2/\lambda`$.
- The plot is the same as in §2.8.

### 2.13 Uniform distribution: random times and random sky directions
**Definition:** every value in $`[a, b]`$ is equally likely:

```math
f(x) = \frac{1}{b-a}, \quad a \le x \le b
```

| Statistic | Formula |
|---|---|
| Mean | $`(a+b)/2`$ |
| Variance | $`(b-a)^2/12`$ (equals $`1/12`$ on $`[0,1]`$) |
| Standard deviation | $`\sqrt{\text{variance}}`$ |
| Skewness | $`0`$ |
| Excess kurtosis | $`-6/5 = -1.2`$ (spoken as "negative 6 1 5") |

⚠️ The mean was spoken once as "1 plus a plus b by 2". It is $`(a+b)/2`$.

**Example 1: eclipsing binary**
- The star is in eclipse for 10% of its orbital period.
- Observing at a random moment, the orbital phase is $`\phi \sim U(0,1)`$.
- If the eclipse occupies $`0.45 \le \phi \le 0.55`$, then

```math
P(0.45 \le \phi \le 0.55) = 0.10
```
- ⚠️ The upper bound was spoken as "0.5". It must be 0.55 to give a width of 0.10.

**Example 2: isotropic gamma-ray bursts**
- Classical GRBs are spread isotropically over the sky, so $`\sin(\text{dec})`$ is uniform on $`[-1, 1]`$.
- Fraction of sky within $`\pm30^\circ`$ of the celestial equator:

```math
\frac{\sin 30^\circ - \sin(-30^\circ)}{2} = 0.5
```
- For an observer at latitude $`22.7^\circ`$ N (likely an Indian site), declinations above $`-(90^\circ - 22.7^\circ) = -67.3^\circ`$ can rise above the horizon. The visible fraction is

```math
\frac{1 + \sin 67.3^\circ}{2} \approx 0.96
```

**Plots:**
- Density vs orbital phase on $`[0,1]`$: a flat line (red).
- Simulated isotropic photon/burst directions in right ascension and declination. Both coordinates are needed.

**Uniform orbital-phase statistics:** mean $`= 0.5`$, median $`= 0.5`$, $`Q_1 = 0.25`$, $`Q_3 = 0.75`$. The PDF is flat, so every phase is equally likely.
- ⚠️ The transcript said "25% Q1 and 25% Q3 which are the skewness". The correct statement is the 25th and 75th percentiles, i.e. the quartiles.

```python
# Reconstruction (inferred): uniform examples
from scipy.stats import uniform
phase = uniform(loc=0, scale=1)
print(phase.cdf(0.55) - phase.cdf(0.45))       # 0.10
print(phase.stats(moments="mvsk"))             # 0.5, 1/12, 0, -1.2
print(phase.ppf([0.25, 0.5, 0.75]))            # Q1, median, Q3

N = 10_000
ra  = rng.uniform(0, 360, N)                   # right ascension uniform
dec = np.degrees(np.arcsin(rng.uniform(-1, 1, N)))  # isotropic: sin(dec) uniform
print(np.mean(np.abs(dec) <= 30))              # ≈ 0.5
print(np.mean(dec > -(90 - 22.7)))             # ≈ 0.96
```

### 2.14 Beta distribution: what fraction of galaxies are spirals?
- The beta distribution describes a quantity that is itself a probability or fraction on $`[0,1]`$. It is the standard tool for Bayesian estimation of fractions.
- **PDF:**

```math
f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, \qquad B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
```
- **Mean and variance:**

```math
\mu = \frac{\alpha}{\alpha+\beta}, \qquad \sigma^2 = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}
```
- **Mode:** $`\dfrac{\alpha-1}{\alpha+\beta-2}`$ for $`\alpha, \beta > 1`$.

**Example: Galaxy Zoo** (citizen-science classification into spiral, elliptical or barred galaxies)
- Start from a flat prior, $`\text{Beta}(1,1)`$.
- After observing $`s`$ spirals out of $`n`$ galaxies, the posterior is $`\text{Beta}(1+s,\,1+n-s)`$.

| Sample | Data | Posterior | Posterior mean |
|---|---|---|---|
| Field | 32 spirals out of 50 | $`\text{Beta}(33,19)`$ | $`33/52 \approx 0.63`$ (spoken as "0.65") |
| Rich cluster | 12 spirals, presumably out of 50 | $`\text{Beta}(13,39)`$ | $`13/52 = 0.25`$ ✔ |

⚠️ The cluster sample size of 50 is inferred; it is what makes the stated mean of 0.25 come out exactly.

**Plots:**
- Several prior shapes, spoken as "0.15, 0.5", "2 and 5", "5 and 5". These are probably $`\text{Beta}(0.5,0.5)`$, $`\text{Beta}(2,5)`$ and $`\text{Beta}(5,5)`$; inferred.
- The two posteriors. The instructor described the cluster posterior as having the higher $`\sigma`$, approaching a delta function, and the field curve as close to the flat (uniform) prior.
- ⚠️ This description is internally inconsistent: a higher $`\sigma`$ means a wider curve, not a delta-like one. In reality, both posteriors are fairly narrow with 50 galaxies each.

```python
# Reconstruction (inferred): Beta posteriors
from scipy.stats import beta
x = np.linspace(0, 1, 500)
for a, b in [(0.5, 0.5), (2, 5), (5, 5), (1, 1)]:
    plt.plot(x, beta.pdf(x, a, b), label=f"Beta({a},{b})")
plt.legend(); plt.show()

field   = beta(1 + 32, 1 + 50 - 32)
cluster = beta(1 + 12, 1 + 50 - 12)
for name, d in [("field", field), ("cluster", cluster)]:
    m, v, s, k = d.stats(moments="mvsk")
    print(name, m, np.sqrt(v), d.median(), d.interval(0.95))
```

### 2.15 Gamma distribution: how long to collect enough X-ray photons
- **PDF**, with shape $`k`$ (number of events) and scale $`\theta`$ (mean gap, $`\theta = 1/\text{rate}`$):

```math
f(x) = \frac{x^{k-1} e^{-x/\theta}}{\Gamma(k)\,\theta^{k}}, \quad x > 0
```
  ⚠️ The $`\Gamma(k)`$ in the denominator was not spoken but is required.
- Mean $`= k\theta`$; variance $`= k\theta^2`$.
- **Interpretation:** the waiting time for the $`k`$-th photon is the sum of $`k`$ exponential gaps.
- **Astronomy example:** a faint source observed with an X-ray telescope. This was rushed for time, so no numbers were captured. The instructor showed that Python (`scipy.stats.gamma`) reproduces the hand-calculated values.

### 2.16 Chi-square distribution (important: the backbone of goodness of fit)
- **Definition:** if $`Z_1, Z_2, \dots, Z_k`$ are independent standard normal variables, then

```math
Q = \sum_{i=1}^{k} Z_i^2 \sim \chi^2_k
```
  where $`k`$ is the degrees of freedom.
- **PDF:**

```math
f(x) = \frac{x^{k/2-1}e^{-x/2}}{2^{k/2}\Gamma(k/2)}, \quad x > 0
```
  This is a gamma distribution with shape $`k/2`$ and scale $`2`$.
- **Standard moments** (not all spoken):

  | Statistic | Formula |
  |---|---|
  | Mean | $`k`$ |
  | Variance | $`2k`$ |
  | Mode | $`\max(k-2, 0)`$ |
  | Skewness | $`\sqrt{8/k}`$ |
  | Excess kurtosis | $`12/k`$ |

- **Goodness-of-fit statistic** for data $`y_i`$, model values $`m_i`$ and uncertainties $`\sigma_i`$:

```math
\chi^2 = \sum_{i=1}^{N} \frac{(y_i - m_i)^2}{\sigma_i^2}
```
  - Degrees of freedom $`= N - (\text{number of fitted parameters})`$.
  - Reduced chi-square: $`\chi^2_\nu = \chi^2/\text{dof}`$. A value near 1 indicates a good fit.
- **Example:** two stars' magnitude measurements with $`\sigma = 0.02`$ mag (magnitudes around 9–10), each fitted with a model.
  - Star 1: $`\chi^2 = 3.99`$.
  - Star 2: $`\chi^2 = 0.93`$, the better fit.
  - The p-values come from `scipy.stats.chi2` (spoken as "chi 2 and PPF"). Use `.sf` for the p-value and `.ppf` for critical values.
  - ⚠️ The dof, star names and full data were not captured. Whether "better" holds strictly depends on the dof.

```python
# Reconstruction (inferred): chi-square goodness of fit
from scipy.stats import chi2
def chi_square(y, model, sigma):
    return np.sum(((y - model) / sigma) ** 2)

# y_obs, y_model: arrays of magnitudes (values not given in lecture)
# chisq = chi_square(y_obs, y_model, 0.02)
# dof   = len(y_obs) - n_params
# p_value  = chi2.sf(chisq, dof)      # probability of a chi^2 this large by chance
# critical = chi2.ppf(0.95, dof)      # 95% threshold
```

### 2.17 Log-normal distribution: stellar masses
- If $`\ln X \sim \mathcal{N}(\mu, \sigma^2)`$, then $`X`$ is log-normal. It looks Gaussian-like, but in $`\ln x`$ rather than $`x`$.
- **PDF:**

```math
f(x) = \frac{1}{x\,\sigma\sqrt{2\pi}} \exp\!\left[-\frac{(\ln x - \mu)^2}{2\sigma^2}\right], \quad x > 0
```
- **Summary statistics:**

  | Statistic | Formula |
  |---|---|
  | Mean | $`e^{\mu+\sigma^2/2}`$ |
  | Median | $`e^{\mu}`$ |
  | Mode | $`e^{\mu-\sigma^2}`$ |
  | Variance | $`(e^{\sigma^2}-1)\,e^{2\mu+\sigma^2}`$ |

- **Example: stellar initial mass function** (specific $`\mu, \sigma`$ not captured; "refer to at home"). The result is mode $`\ll`$ median $`\ll`$ mean, i.e. an extremely right-skewed curve.
- Python: `scipy.stats.lognorm(s=sigma, scale=np.exp(mu))`. A number "49.1" was spoken here in a garbled context and is unclear.

### 2.18 Summary chart comparing all distributions

| Distribution | Mean | Variance | Skewness $`\gamma_1`$ | Excess kurtosis $`\gamma_2`$ |
|---|---|---|---|---|
| Normal | $`\mu`$ | $`\sigma^2`$ | $`0`$ | $`0`$ |
| Exponential | $`1/\lambda`$ | $`1/\lambda^2`$ | $`2`$ | $`6`$ |
| Uniform | $`(a+b)/2`$ | $`(b-a)^2/12`$ | $`0`$ | $`-1.2`$ |
| Beta | $`\alpha/(\alpha+\beta)`$ | $`\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}`$ | depends on $`\alpha, \beta`$ | depends on $`\alpha, \beta`$ |
| Gamma | $`k\theta`$ | $`k\theta^2`$ | $`2/\sqrt{k}`$ | $`6/k`$ |
| $`\chi^2_k`$ | $`k`$ | $`2k`$ | $`\sqrt{8/k}`$ | $`12/k`$ |
| Log-normal | $`e^{\mu+\sigma^2/2}`$ | $`(e^{\sigma^2}-1)e^{2\mu+\sigma^2}`$ | $`>0`$ | $`>0`$ |

- For the normal distribution, mean = median = mode $`= \mu`$.
- The chart also plotted where mean, median and mode sit on each distribution. A $`\chi^2`$ example with some number of dof (spoken as "90"; unclear) was included.
- The instructor's remark for the uniform distribution, "no skewness but there is kurtosis", refers to its *negative* excess kurtosis.

---

## 3. Functions, Methods and Built-ins Used

| Name | What it does |
|---|---|
| `import numpy as np` | Numerical arrays and maths |
| `np.linspace(a, b, n)` | `n` evenly spaced points from `a` to `b` (the x-grid for PDFs) |
| `np.exp`, `np.log`, `np.sqrt` | Elementwise exponential, natural log, square root |
| `np.argmax(arr)` | Index of the maximum; used to find the mode numerically |
| `np.random.default_rng(seed)` | Creates a random generator |
| `rng.exponential(scale, size)` | Exponential samples; note `scale = 1/λ` |
| `rng.poisson(lam, size)` | Poisson counts |
| `rng.uniform(low, high, size)` | Uniform samples |
| `from scipy import stats` | Probability distributions module |
| `stats.norm`, `expon`, `uniform`, `beta`, `gamma`, `chi2`, `lognorm`, `t`, `laplace` | Distribution objects |
| `.pdf(x)` | Density at `x` |
| `.cdf(x)` | $`P(X \le x)`$ |
| `.sf(x)` | Survival function $`1 - \text{CDF}`$, i.e. the one-sided tail probability (more accurate than `1 - cdf` far in the tail) |
| `.ppf(q)` | Inverse CDF: quantiles, medians, critical values |
| `.stats(moments="mvsk")` | Mean, variance, skewness and **excess** kurtosis |
| `.mean()`, `.median()`, `.var()`, `.std()`, `.interval(c)` | Summary statistics; `.interval(c)` gives the central `c` credible/confidence interval |
| `.rvs(size)` | Random samples from the distribution |
| `stats.gaussian_kde(data)` | Kernel density estimate (smooth curve over a histogram) |
| `scipy.integrate.quad(f, a, b)` | Numerical integration; returns `(value, error)`, so take `[0]` |
| `scipy.optimize.brentq` | Root finder; used for the median (CDF $`= 0.5`$) |
| `import pandas as pd` | Tables and series (the transcript's "panda") |
| `pd.Series(...)` | 1-D labelled data, e.g. the simulated photon gaps |
| `pd.DataFrame({...})` | Table, e.g. simulated vs theoretical comparison |
| `.describe()` | Count, mean, std, min, quartiles, max |
| `.quantile(q)` | Quartiles / IQR |
| `.skew()`, `.kurt()` | Sample skewness and **excess** kurtosis (pandas) |
| `matplotlib.pyplot as plt` | Plotting |
| `plt.subplots(r, c)` | Figure plus axes grid ("define figure and axis") |
| `ax.plot`, `ax.hist(..., density=True)` | Line plot; normalised histogram (comparable with a PDF) |
| `ax.axvline` | Vertical line marking mean, median or mode |
| `ax.fill_between` | Shade $`1\sigma`$/$`2\sigma`$/$`3\sigma`$ regions |
| `ax.set_yscale("log")` | Log y-axis to reveal tail/kurtosis differences |
| `ax.set_xlabel`, `ax.set_ylabel`, `ax.legend`, `plt.tight_layout`, `plt.show` | Labelling and display |

---

## 4. Syntax Rules, Common Mistakes and Debugging Tips

- **`scipy.stats` parametrisations** (a common source of wrong answers):

  | Distribution | Correct call |
  |---|---|
  | Exponential | `expon(scale=1/lam)` (not `scale=lam`) |
  | Uniform on $`[a,b]`$ | `uniform(loc=a, scale=b-a)` (not `scale=b`) |
  | Gamma | `gamma(a=k, scale=theta)` |
  | Log-normal | `lognorm(s=sigma, scale=np.exp(mu))` |

- **Kurtosis conventions:** `scipy.stats` (`.stats(moments="mvsk")`, `stats.kurtosis`) and pandas `.kurt()` return **excess** kurtosis $`\gamma_2`$ by default. The normal distribution gives 0, not 3.
- **Use `density=True`** in `hist` when overlaying a PDF. Otherwise the heights are raw counts.
- **Verify analytic results** numerically with `quad`, and by simulation with large $`N`$ (the lecture used 10,000). Sample values like 0.251 and 0.174 should be close to the theoretical 0.25 and 0.173.
- **Tail probabilities:** use `norm.sf(z)` rather than `1 - norm.cdf(z)` for large $`z`$, because of numerical precision.
- **Combining errors:** independent uncertainties add **in quadrature**, $`\sqrt{\sigma_1^2 + \sigma_2^2}`$, not linearly.
- **Poisson vs exponential:** counts per interval are Poisson; gaps between events are exponential. The lecture conflated these.
- **Gaussian approximation:** valid for bright sources with large counts; unreliable for faint, low-count sources.

---

## 5. Exam and Assignment Pointers

No explicit "this will be on the exam" statement was captured. The following were emphasised or assigned:

- **In-class exercise:** extend the sigma-band plot to **$`5\sigma`$** and see how the enclosed area/percentile changes.
- **Self-study:** the log-normal stellar initial mass function example ("you can refer to at home").
- **Concepts stressed repeatedly** (likely examinable):
  - definitions of raw and central moments;
  - formulas for mean, median, mode, variance, CV, skewness $`\mu_3/\sigma^3`$ and kurtosis $`\mu_4/\sigma^4 - 3`$;
  - the mean/median/mode ordering for skewed distributions;
  - the sign interpretation of $`\gamma_1`$ and $`\gamma_2`$;
  - the per-distribution summary table (§2.18);
  - $`3\sigma`$/$`5\sigma`$ detection thresholds and the Hubble-tension calculation ($`z \approx 4.9 \approx 5\sigma`$);
  - the CLT (Poisson → Gaussian);
  - the $`\chi^2`$ goodness-of-fit formula and degrees of freedom.

<!-- nav -->
← [Session 17 (2026-10-30)](DSM-102-17_2026-10-30_Abhirup-Datta.md) · [All lectures](./) · [Session 19 (2026-11-13)](DSM-102-19_2026-11-13_Abhirup-Datta.md) →
<!-- /nav -->
