---
course: DSM 101
date: 2026-10-19
start: 7:00pm
session: "27"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 26 (2026-10-17)](DSM-101-26_2026-10-17_Pritee-Sharma.md) · [All lectures](./) · [Session 28 (2026-10-21)](DSM-101-28_2026-10-21_Pritee-Sharma.md) →
<!-- /nav -->

# DSM-101 (Probability & Statistics): Lecture 27 Study Notes
**Session:** DSM-101-27 · 2026-10-19 · Instructor: Pritee Sharma
**Topic:** Measures of dispersion (standard deviation, variance, coefficient of variation), shape and skewness, and standardization with z-scores

---

## 1. Overview

This session continued the discussion of **measures of dispersion** from the previous class. It first reviewed the definition and properties of the **sample standard deviation**:
- squaring the deviations,
- the least-squares property,
- dividing by $`n-1`$ (loss of one degree of freedom).

A sales-team example showed how two data sets with identical means can have very different spreads. The lecture then covered **variance** (why it is useful for theory, and its drawback of squared units) and the **coefficient of variation** (for comparing variability across different units or scales), using a two-stock example. Students worked an in-class exercise computing summary statistics for a set of test scores. The second half covered the **shape** of a distribution:
- left, right and zero skewness,
- **Pearson's coefficient of skewness**, with an employee task-time example,
- **z-score standardization**, its use for detecting outliers and data-entry errors,
- the normal-distribution coverage rules ($`\pm 1.96`$, $`\pm 3`$, $`\pm 4`$ SD) and the worst-case (Chebyshev) bound.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Sample Standard Deviation

**Definition (sample standard deviation):**

```math
s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}
```

The definition is built from three steps:
1. Take each deviation from the mean, $`x_i - \bar{x}`$.
2. **Square** each deviation, because the raw deviations always sum to zero: $`\sum_{i=1}^{n}(x_i - \bar{x}) = 0`$.
3. Sum the squares, divide by $`n-1`$, and take the square root to return to the original scale.

**Three properties/merits discussed:**
1. **Squaring removes the zero-sum problem.** Unsquared deviations about the mean always cancel out.
2. **Property of least squares.** The sum of squared deviations is a minimum when measured from $`\bar{x}`$. If any other value $`a \neq \bar{x}`$ is used, $`\sum (x_i - a)^2`$ is larger:

```math
\sum_{i=1}^{n}(x_i - \bar{x})^2 \le \sum_{i=1}^{n}(x_i - a)^2 \quad \text{for any } a
```
3. **Divide by $`n-1`$, not $`n`$ (loss of one degree of freedom).**
   - $`\bar{x}`$ is itself a statistic estimated from the data, and it is then used to compute another statistic ($`s`$).
   - Using one estimated component to estimate another costs one degree of freedom.
   - Dividing by $`n`$ would systematically **underestimate** the population spread. The instructor said "overestimating" at this point, but the $`n-1`$ correction exists because dividing by $`n`$ makes the estimate too small.

---

### 2.2 Worked Example: Sales Teams A and B

**Setup:** A sales director compares the monthly sales (in ₹ lakhs) of two regional teams over the past 6 months.
- Team A's sales are recorded as variable $`X`$.
- Team B's sales are recorded as variable $`Y`$.

**Step 1: Means.** Both are identical:

```math
\bar{x} = 52.5, \qquad \bar{y} = 52.5
```
The mean alone cannot distinguish the teams.

**Step 2: Squared deviations.** For each month, compute $`x_i - \bar{x}`$ and square it, then sum. Do the same for $`y_i - \bar{y}`$.
- $`\sum (x_i - \bar{x})^2 = 437.5`$
- $`\sum (y_i - \bar{y})^2 = 5087`$

**Step 3: Standard deviations.** With $`n = 6`$, so $`n - 1 = 5`$:

```math
s_X = \sqrt{\frac{437.5}{5}} = \sqrt{87.5} \approx 9.35
```

```math
s_Y = \sqrt{\frac{5087}{5}} = \sqrt{1017.4} \approx 31.9
```

> ⚠️ **Discrepancy:** During the interpretation the instructor quoted Team B's SD as **30.28**, and she also mentioned a slide typo. Using the stated sum of squares, $`\sqrt{5087/5} \approx 31.9`$. Check the slide.

**Interpretation:**
- The average sales are identical, but **consistency differs drastically**.
- **Team A** ($`s \approx 9.35`$): sales typically lie within about 9.35 lakhs above or below 52.5 lakhs. This is a stable team.
- **Team B** (large SD): large fluctuations on both sides of the mean. Using 30.28, the range is roughly $`52.5 + 30.28 \approx 82.8`$ lakhs on the high side and $`52.5 - 30.28 \approx 22.2`$ lakhs on the low side.
- **Decision:**
  - If the company values **stability and predictability**, Team A is better.
  - If it values **high potential and risk-taking**, Team B is more suitable.

---

### 2.3 Population vs. Sample Standard Deviation (why $`n-1`$)

| | Symbol | Formula | Mean used | Denominator |
|---|---|---|---|---|
| Population SD (parameter) | $`\sigma`$ | $`\sigma = \sqrt{\dfrac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}`$ | $`\mu`$ (population mean) | $`N`$ |
| Sample SD (statistic) | $`s`$ | $`s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}`$ | $`\bar{x}`$ (sample mean) | $`n-1`$ |

- **Population formula:** used only when every observation in the population is recorded, as in a census. This is rare in practice.
- **Sample formula:** used most of the time.
  - The $`n-1`$ correction makes the sample statistic an **unbiased estimator of the population parameter**.
  - **The instructor stressed this point:** $`s`$ is used to estimate $`\sigma`$, the population SD. It is *not* an "unbiased estimate of $`s`$". A sample statistic is used to estimate a population parameter.

> 📝 *Technical note (not from the lecture):* Strictly, $`s^2`$ is an exactly unbiased estimator of $`\sigma^2`$, i.e. $`E[s^2] = \sigma^2`$. The square root $`s`$ is only approximately unbiased for $`\sigma`$.

---

### 2.4 Variance

**Definition:** variance is the square of the standard deviation.

```math
s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}, \qquad s = \sqrt{s^2}
```
The population variance is $`\sigma^2`$.

**Why use variance?**

1. **Additivity for independent random variables.** For independent random variables $`X`$ and $`Y`$:

```math
\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)
```
   - The instructor compared this to the associative property of addition.
   - **Standard deviation does NOT have this property.** Since $`\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}`$:

```math
\operatorname{SD}(A + B) = \sqrt{\operatorname{Var}(A) + \operatorname{Var}(B)} \neq \operatorname{SD}(A) + \operatorname{SD}(B)
```
   - So when forecasting, comparing or projecting with **two independent random variables at the same time**, work with **variances**, not SDs.
2. **Theoretical importance.**
   - Variance is a fundamental measure of dispersion, directly related to the **moments** of a distribution.
   - It appears in formulas for many statistical tests and models, including the **chi-square ($`\chi^2`$) distribution**.

**Drawback: units.**
- **SD** is in the same units as the data. If height is measured in m, the SD is in m. This makes SD better for **reporting, comparison and visualization**.
- **Variance** is in squared units, e.g. $`\text{m}^2`$, which is hard to interpret when reporting differences, for example in heights between two samples.

---

### 2.5 Coefficient of Variation (CV)

**Motivation:**
- The mean, SD and variance are all tied to the original units (or their square).
- This makes it hard to compare variability across data sets that:
  - are measured in **different units** (e.g. one stock in US dollars, another in Japanese yen), or
  - are in the same units but have **very different magnitudes** (e.g. a stock priced in hundreds of dollars vs. one priced in fractions of a dollar).

**Formula:**

```math
CV = \frac{s}{\bar{x}} \times 100\%
```
- It is expressed as a **percentage**.
- It is unit-free, so it allows comparisons across scales.
- **$`CV = 100\%`$** means the standard deviation equals the mean ($`s = \bar{x}`$). This indicates a great deal of variability.
- A higher CV means relatively more variability.

**Worked example: two stocks (both priced in US dollars)**
- Stock A has small prices: e.g. 1, 1.5, 1.9, …
- Stock B has large prices: e.g. 180, 188, 190, 200, …

| Statistic | Stock A | Stock B |
|---|---|---|
| Mean | $`\$1.70`$ | $`\$188.8`$ (also quoted as $`188.88`$) |
| Variance | $`2.61`$ | $`128.41`$ |
| SD | $`1.62`$ | $`11.33`$ |
| CV | $`\dfrac{1.62}{1.7}\times 100 \approx 95\%`$ | $`\dfrac{11.33}{188.8}\times 100 \approx 6.0\%`$ |

**Interpretation:**
- Judged by SD alone, Stock B ($`11.33`$) looks more volatile than Stock A ($`1.62`$).
- However, relative to its price level, **Stock A is far more volatile** (CV 95% vs. 6%).
- Use CV whenever scales differ substantially, even if the units are the same.

---

### 2.6 In-Class Exercise: Test Scores (Descriptive / Summary Statistics)

**Task:** for a data set of test scores with $`n = 10`$, compute the mean, median, mode, quartiles, interquartile range (IQR), variance, standard deviation and CV.

**Answers confirmed in class:**

| Statistic | Value |
|---|---|
| Mean $`\bar{x}`$ | $`56`$ |
| Mode | $`0,\ 50,\ 100`$ (multimodal) |
| $`Q_1`$ | $`40`$ |
| $`Q_2`$ (median) | $`55`$ |
| $`Q_3`$ | $`90`$ |
| IQR $`= Q_3 - Q_1`$ | $`90 - 40 = 50`$ |
| SD $`s`$ (with $`n-1`$) | $`36.27`$ |
| Variance $`s^2`$ | $`\approx 36.27^2 \approx 1315.5`$ (*derived; not stated in class*) |
| CV | $`\dfrac{36.27}{56}\times 100 \approx 64.8\%`$ |

- One student initially gave $`Q_1 = 49`$, $`Q_2 = 65`$, and the IQR as 100. These were incorrect. The confirmed values are $`Q_1 = 40`$, $`Q_2 = 55`$, $`Q_3 = 90`$, IQR $`= 50`$.
- Together, the mean, median, mode, quartiles, range, IQR, variance, SD and CV are called **descriptive statistics** or **summary statistics**.

**Q&A: $`n`$ or $`n-1`$?**
- **By default, treat the data as a sample and use $`n-1`$.**
- Use $`N`$ only if the question explicitly says the data is the population.
- A small data set such as $`n = 10`$ is conventionally assumed to be a sample.

---

### 2.7 Shape of a Distribution: Skewness

**Skewness** describes the degree of (a)symmetry of a distribution. The median is treated as the central location, and skewness is judged by where the mean lies relative to it.

| Case | Name | Description |
|---|---|---|
| $`\bar{x} < \text{median}`$ | **Negative / left skew** | The mean lies to the left of the median. It is pulled down by unusually **low** values. |
| $`\bar{x} = \text{median}`$ | **Zero skew (symmetric)** | Symmetric shape. For a symmetric unimodal distribution, mean $`=`$ median $`=`$ mode. |
| $`\bar{x} > \text{median}`$ | **Positive / right skew** | The mean lies to the right of the median. It is pulled up by unusually **high** values. |

**Pearson's coefficient of skewness:**

```math
Sk_P = \frac{\bar{x} - \text{Mode}}{s}
```
- **Negative** means left-skewed, **zero** means symmetric, **positive** means right-skewed.
- The SD in the denominator is itself measured about the arithmetic mean.

**Q&A: bimodal data.**
- If the data are **bimodal** (two modes), this mode-based Pearson coefficient **cannot be applied**.

> 📝 *Not covered in class, for reference:* a common alternative is Pearson's second coefficient, $`Sk = \dfrac{3(\bar{x} - \text{Median})}{s}`$, which avoids needing a single mode.

**Worked example: employee task times**
- **Data:** a sample of 12 employees all did the same task, and the hours each took were recorded in ascending order.
- **Mean:** $`\bar{x} = \dfrac{180}{12} = 15`$ hours.
- **Median:** $`10`$ hours.
- **Outlier:** one extremely slow employee took **63 hours**.
- **Skew:** since $`\bar{x} = 15 > \text{median} = 10`$, the data are **right-skewed (positively skewed)**. The unusually high value pulls the mean to the right.
- **Other statistics:**
  - Variance $`= 260.79`$
  - SD $`= 16.25`$ as quoted
  - CV $`= 107.7\%`$

> ⚠️ **Check:** $`\sqrt{260.79} \approx 16.15`$ (not 16.25), and $`16.15/15 \approx 107.7\%`$. The correct SD is therefore likely **16.15**.

---

### 2.8 Standardization with z-Scores

**Purpose:**
- Convert the original scores into new scores with **mean $`0`$** and **SD $`1`$**.
- The result is a **pure number with no units**.

**Units summary:**

| Measure | Units |
|---|---|
| Mean | original units |
| SD | original units |
| Variance | squared units |
| CV | percentage |
| z-score | unit-free |

**Formula:**

```math
z_i = \frac{x_i - \bar{x}}{s}
```
For a population, $`z = \dfrac{x - \mu}{\sigma}`$.

**Sign of a z-score:**
- Score below the mean gives $`z < 0`$.
- Score equal to the mean gives $`z = 0`$.
- Score above the mean gives $`z > 0`$.

**Worked example (six observations):**
- $`\bar{x} = 5`$ and $`s = 3.74`$.
- Each $`z_i = (x_i - 5)/3.74`$. For example, the first value gives $`z_1 \approx -1.3`$.
- Three of the z-scores are negative (below the mean) and three are positive (above the mean).

**Application: detecting outliers and data-entry errors**
- **Context:** exam scores for a large number of students. In raw data it is hard to spot errors or outliers.
- **Method:** compute z-scores, and values that are extreme relative to the rest stand out.
- **First flagged case:** an extreme z-score of about $`-2.89`$ (the instructor said "2.89 / minus 2.89").
  - Checking the answer sheet showed an **entry error**; the true score was **97**.
  - After correction, the z-score fell within the expected range.
- **Second flagged case:** a z-score of $`-3.12`$ was flagged. The original data were rechecked and the error was corrected.
- **Effect of corrections:** the mean changed (quoted as $`75.57`$) and the **SD declined**, meaning the data became more uniform.
- **Rule of thumb:** for any type of data, a z-score **greater than $`+5`$ or less than $`-5`$** is a very unusual score and warrants attention.

**Normal-distribution coverage (for z-scores of normally distributed data):**

| Interval of $`z`$ | Approx. % of data |
|---|---|
| $`-1.96 \le z \le +1.96`$ (about $`\pm 2`$ SD) | $`95\%`$ |
| $`-3 \le z \le +3`$ | $`99.7\%`$ |
| $`-4 \le z \le +4`$ | $`99.99\%`$ |

**Worst case, for any distribution (Chebyshev's inequality):**
- At least **$`75\%`$** of the data lie within **2 standard deviations of the mean**, i.e. $`-2 \le z \le +2`$.
- The instructor phrased this as "two SD above the mean"; the bound is for $`\pm 2`$ SD.
- General form (named here for reference): at least $`1 - \dfrac{1}{k^2}`$ of the data lie within $`k`$ SD of the mean. For $`k = 2`$ this gives $`1 - \tfrac{1}{4} = 75\%`$.

---

## 3. Exam / Assignment Notes

- **Sample vs. population:** by default, assume the data are a **sample** and divide by **$`n-1`$**. Use $`N`$ only if the question explicitly states the data are the population.
- **Unbiased estimation (emphasized):** $`n-1`$ makes the sample statistic an unbiased estimator of the **population parameter** $`\sigma`$ (strictly, $`s^2`$ is unbiased for $`\sigma^2`$). It is not an "unbiased estimate of $`s`$".
- **Know when to use each measure:**
  - **SD** for reporting and visualizing, because it keeps the original units.
  - **Variance** for theory and for combining independent variables: $`\operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)`$.
  - **CV** for comparing variability across different units or very different scales.
  - **z-scores** for unit-free comparison and for detecting outliers.
- **Pearson's skewness:** $`(\bar{x} - \text{Mode})/s`$ is not applicable to bimodal data.
- **Practice:** the in-class test-score exercise (mean, median, mode, quartiles, IQR, variance, SD, CV) is representative of expected problems.
- **Next class:** summary of descriptive statistics and applications of these concepts.

---

## Quick Formula Sheet

```math
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
```

```math
s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}, \qquad \sigma = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}
```

```math
s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}, \qquad \operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)\ \ (X, Y \text{ independent})
```

```math
CV = \frac{s}{\bar{x}} \times 100\%
```

```math
IQR = Q_3 - Q_1
```

```math
Sk_P = \frac{\bar{x} - \text{Mode}}{s}
```

```math
z_i = \frac{x_i - \bar{x}}{s}
```

```math
P(-1.96 \le Z \le 1.96) \approx 0.95, \quad P(-3 \le Z \le 3) \approx 0.997, \quad P(-4 \le Z \le 4) \approx 0.9999
```

```math
\text{Chebyshev: } P(|z| \le k) \ge 1 - \frac{1}{k^2}, \quad k = 2 \Rightarrow \ge 75\%
```

<!-- nav -->
← [Session 26 (2026-10-17)](DSM-101-26_2026-10-17_Pritee-Sharma.md) · [All lectures](./) · [Session 28 (2026-10-21)](DSM-101-28_2026-10-21_Pritee-Sharma.md) →
<!-- /nav -->
