---
course: DSM 101
date: 2026-10-24
start: 2:45 pm
session: "30"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 29 (2026-10-23)](DSM-101-29_2026-10-23_Pritee-Sharma.md) · [All lectures](./) · [Session 31 (2026-10-27)](DSM-101-31_2026-10-27_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 · Session 30: CLT Applications, Sampling Distributions & Sample Size Determination
**Instructor:** Prof. Pritee Sharma  **Date:** 2026-10-24

---

## 1. Overview

The session opened by finishing the previous class's worked example. It applied the **Central Limit Theorem (CLT)** to a right-skewed e-commerce delivery-time population to find:
- the sampling distribution of $\bar{X}$,
- the standard error,
- two probabilities using z-scores and the standard normal table,
- a 95% confidence interval.

The lecture then moved from descriptive to **inferential statistics**. It explained that every sample statistic (mean, proportion, median, and so on) has its own sampling distribution, which can be used to estimate the matching population parameter. Three further topics were covered briefly:
- the **sampling distribution of proportions**, via the binomial distribution,
- a summary table of estimation formulas,
- the **sampling distribution of differences (and sums)** of statistics from two populations.

The final main topic was **sample size determination**, $n = z^2\sigma^2/E^2$. Worked examples covered estimating a mean and a proportion, and showed why opinion polls typically use about 1,000 respondents. The instructor ended by stating the exam syllabus boundary and the marks breakdown.

---

## 2. Topics Covered (in order taught)

### 2.1 Worked Example: E-commerce Delivery Times (CLT application)

**Problem setup**
- Individual order delivery times (in days) across the country are **right-skewed**.
- Population mean $\mu = 4.5$ days.
- Population standard deviation $\sigma = 2.3$ days.
- Managers draw random samples of size $n = 30$ and compute the sample mean delivery time $\bar{X}$.

**Key idea:** The population is skewed, but by the CLT the sampling distribution of $\bar{X}$ is approximately normal for large $n$. Here $n = 30$ is treated as large enough.

#### Part 1: Sampling distribution (mean and standard error)

Mean of the sampling distribution:

```math
E[\bar{X}] = \mu_{\bar{X}} = \mu = 4.5 \text{ days}
```

Standard error, which is the standard deviation of the distribution of $\bar{X}$:

```math
SE = \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{2.3}{\sqrt{30}} = \frac{2.3}{5.477} \approx 0.42 \text{ days}
```

So $\bar{X} \sim N\left(4.5,\ 0.42^2\right)$ approximately.

#### Part 2: $P(\bar{X} \le 5)$

Compute the z-score:

```math
z = \frac{\bar{x} - \mu}{SE} = \frac{5 - 4.5}{0.42} \approx 1.19
```

Look up $z = 1.19$ in the standard normal table (row 1.1, column 0.09). The table gives the area between $0$ and $z$:

```math
P(0 \le Z \le 1.19) = 0.383
```

"Less than or equal to" means we also include the entire left half of the curve, which has area $0.5$:

```math
P(\bar{X} \le 5) = P(Z \le 1.19) = 0.5 + 0.383 = 0.883
```

(One student's answer in class was garbled in the transcript. The correct answer is about **0.883**, or 88.3%.)

#### Part 3: $P(4 \le \bar{X} \le 5)$

1. For $\bar{x} = 5$: $z = +1.19$, so $P(Z \le 1.19) = 0.883$.
2. For $\bar{x} = 4$:

```math
z = \frac{4 - 4.5}{0.42} \approx -1.19
```
3. By symmetry, the area to the left of $z = -1.19$ is $1 - 0.883 = 0.117$.
4. The area between the two z-values is:

```math
P(4 \le \bar{X} \le 5) = 0.883 - (1 - 0.883) = 0.883 - 0.117 = 0.766
```

The result is about **77%**. The instructor quoted 0.7662, and a student answered "77%", which matches.

Equivalent shortcut: $2 \times 0.383 = 0.766$.

#### Part 4: 95% confidence interval for the true mean delivery time

- For 95% confidence, cut off 2.5% in each tail. The z-value corresponding to a cumulative area of $0.975$ is

```math
z_{\alpha/2} = 1.96
```
- This reflects the general fact that in a normal distribution, $\mu \pm 1.96\sigma$ covers 95% of the area.
- Margin of error:

```math
1.96 \times 0.42 \approx 0.823
```
- Confidence interval:

```math
4.5 \pm 0.823 \;\Rightarrow\; [3.677,\ 5.323] \approx [3.68,\ 5.32] \text{ days}
```

General form of the interval:

```math
\bar{x} \pm z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}
```

In this example the value $4.5$ was used as the sample mean. The student answer of roughly 3.6 to 5.3 days was accepted as correct.

---

### 2.2 Transition to Inferential Statistics

**Statistic vs. parameter**
- A **statistic** is computed from observed sample values.
- It is used to estimate a **parameter**, which describes the population.

**Every statistic has its own sampling distribution.**
- Draw many samples from a population.
- Compute the statistic for each sample.
- The distribution of those values is the sampling distribution of that statistic.

Examples, each pairing a sampling distribution with the parameter it estimates:

| Sampling distribution of… | Used to estimate… |
|---|---|
| sample means $\bar{X}$ | population mean $\mu$ |
| sample proportions | population proportion |
| sample medians | population median |
| sample standard deviations | population standard deviation |

**Statistical inference** means drawing conclusions about population parameters from sample statistics, **without conducting a census**. It includes:
- **estimation** of a population parameter, such as $\mu$,
- **hypothesis testing** about $\mu$, which asks how close or true a claimed value is to the population mean.

The instructor noted that the rest of the course from this point is about inferential statistics.

---

### 2.3 Sampling Distribution of Proportions *(not in syllabus; "for understanding only, no need to memorize")*

**Setup**
- In $n$ trials, count the "successes".
- Probability of success: $p$.
- Probability of failure: $q = 1 - p$.

**Example:** A box holds red, blue and green balls. Drawing a red ball counts as a success. Not drawing red is a failure, with probability $q = 1 - p$.

**Binomial distribution parameters**
- Mean:

```math
\mu = np \qquad (n = \text{number of trials},\ p = \text{probability of success})
```
- Standard deviation:

```math
\sigma = \sqrt{npq} = \sqrt{np(1-p)}
```

Note: the audio sounded like "$n \times p \times q$". The correct formula has the square root.

**Normal approximation**
- As sample size increases, the binomial distribution approaches the normal distribution.
- Mean of the sampling distribution of proportions:

```math
\mu_{\hat{p}} = p
```
- Standard deviation (standard error) of proportions:

```math
\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}
```

---

### 2.4 Summary of Estimation from Sampling Distributions *(slide browsed quickly)*

The instructor listed four situations. Each has a formula for an **infinite** population and for a **finite** population.

**Caution:** The slide formulas were not read aloud. The formulas below are the standard textbook versions, reconstructed for completeness. Check them against the slide deck.

The **finite population correction (FPC)** below uses $N$ = population size and $n$ = sample size:

```math
\sqrt{\dfrac{N-n}{N-1}}
```

| # | Situation | Infinite population | Finite population |
|---|---|---|---|
| 1 | Estimating $\mu$, **$\sigma$ known** | $\bar{x} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ | $\bar{x} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}\sqrt{\dfrac{N-n}{N-1}}$ |
| 2 | Estimating $\mu$, **$\sigma$ unknown, large sample** ($n > 30$) | $\bar{x} \pm z_{\alpha/2}\dfrac{s}{\sqrt{n}}$ | $\bar{x} \pm z_{\alpha/2}\dfrac{s}{\sqrt{n}}\sqrt{\dfrac{N-n}{N-1}}$ |
| 3 | Estimating $\mu$, **$\sigma$ unknown, small sample** | $\bar{x} \pm t_{\alpha/2,\ n-1}\dfrac{s}{\sqrt{n}}$ | $\bar{x} \pm t_{\alpha/2,\ n-1}\dfrac{s}{\sqrt{n}}\sqrt{\dfrac{N-n}{N-1}}$ |
| 4 | Estimating population proportion, **large sample** | $\hat{p} \pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ | $\hat{p} \pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}\sqrt{\dfrac{N-n}{N-1}}$ |

The choice of formula depends on three questions:
- Is $\sigma$ known?
- Is the sample large or small?
- Is the population infinite or finite?

---

### 2.5 Sampling Distribution of Differences (and Sums) of Statistics

**Setup**
- There are two populations.
- From population 1, draw many samples of size $n_1$ and compute a statistic $S_1$ for each (for example, the sample mean).
- From population 2, draw many samples of size $n_2$ and compute $S_2$ for each.
- Sampling distribution of $S_1$: mean $\mu_{S_1}$, standard deviation $\sigma_{S_1}$.
- Sampling distribution of $S_2$: mean $\mu_{S_2}$, standard deviation $\sigma_{S_2}$.

**Building the distribution of differences**
- Pair the samples and take differences, e.g. $\bar{x}_{1} - \bar{x}_{2}$ for each pairing.
- Plot all these differences.
- The result is the **sampling distribution of differences of the statistic**.

Mean of the differences:

```math
\mu_{S_1 - S_2} = \mu_{S_1} - \mu_{S_2}
```

Standard deviation of the differences:

```math
\sigma_{S_1 - S_2} = \sqrt{\sigma_{S_1}^2 + \sigma_{S_2}^2}
```

**Special case: difference of sample means** ($S_1 = \bar{X}_1$, $S_2 = \bar{X}_2$), infinite populations:

```math
\mu_{\bar{X}_1 - \bar{X}_2} = \mu_1 - \mu_2
```

```math
\sigma_{\bar{X}_1 - \bar{X}_2} = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
```

- These results also hold for finite populations sampled **with replacement**.
- **Assumption:** the samples are **independent**.

**Sums** (named on the slide, not elaborated):

```math
\mu_{S_1 + S_2} = \mu_{S_1} + \mu_{S_2}, \qquad \sigma_{S_1 + S_2} = \sqrt{\sigma_{S_1}^2 + \sigma_{S_2}^2}
```

**Slide example (skipped for time):** comparing average daily sales for a **metro** area and a **suburban** area.

---

### 2.6 Determining Sample Size *(in syllabus; probably not covered in later classes)*

**Motivation:** Opinion polls often survey about 1,000 people and project election outcomes from that. This section shows why about 1,000 is appropriate.

**What you need to know**
1. The **desired precision**, $E$.
2. The **population standard deviation**, $\sigma$.

**Derivation**

A confidence interval for $\mu$ has the form:

```math
\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
```

Its half-width is:

```math
E = z\,\frac{\sigma}{\sqrt{n}}
```

- $E$ is the **half-width of the confidence interval**, i.e. the precision.
- $E$ is also called the **sampling error**: the maximum error between the sample estimate and the true parameter that we are willing to accept.

Rearrange:

```math
\sqrt{n} = \frac{z\,\sigma}{E} \quad\Longrightarrow\quad \boxed{\,n = \frac{z^2\,\sigma^2}{E^2}\,}
```

**Rounding rule:** Always round $n$ **up** to the next whole number, even if the decimal part is small. Sample size cannot be fractional, and rounding down would fail to achieve the required precision.

#### Worked Example 1: Estimating a mean

- From previous studies, $\sigma = 20$.
- We want to estimate $\mu$ within $\pm 10$ of its true value, so $E = 10$.
- Significance level $\alpha = 0.05$, i.e. 95% confidence, so $z = 1.96$ (from the z-table, as in Part 4 of the delivery-time example).

```math
n = \frac{(1.96)^2 (20)^2}{(10)^2} = \frac{3.8416 \times 400}{100} = 15.37 \approx 15.4
```

Rounding up gives $\mathbf{n = 16}$.

#### Sample size for a proportion

Applying the same half-width logic to a proportion:

```math
E = z\sqrt{\frac{p(1-p)}{n}} \quad\Longrightarrow\quad \boxed{\,n = \frac{z^2\,p(1-p)}{E^2}\,}
```

If $p$ is unknown, use **$p = 0.5$**. This choice maximizes the variance $p(1-p)$, which gives the most conservative (largest) sample size.

#### Worked Example 2: Political poll

A pollster wants 95% confidence, so $z = 1.96$, and uses $p = q = 0.5$.

**(a) Maximum error $E = 0.01$ (very high precision):**

```math
n = \frac{(1.96)^2(0.5)(0.5)}{(0.01)^2} = \frac{3.8416 \times 0.25}{0.0001} = 9604
```

This is a very large sample.

**(b) Maximum error $E = 0.03$ (slightly less precision, acceptable for polls):**

```math
n = \frac{(1.96)^2(0.5)(0.5)}{(0.03)^2} = \frac{0.9604}{0.0009} \approx 1067.1
```

- The instructor quoted 1067.
- Applying the round-up rule strictly gives 1068.

**Takeaway:** This is why pollsters typically use a sample size of about **1,000**.

---

### 2.7 Other Slide Examples Mentioned *(not worked; out of syllabus)*

**CLT for proportions: customer preference for a new soft drink**
- $p = 0.6$, $q = 1 - p = 0.4$, $n = 100$.
- Applying the formulas from 2.3 (not done in class):

```math
\mu_{\hat{p}} = 0.6, \qquad \sigma_{\hat{p}} = \sqrt{\frac{0.6 \times 0.4}{100}} \approx 0.049
```

**Consulting firm: estimating average weekly working hours $\mu$**
- Past records suggest employees work roughly 35 to 55 hours per week.
- Case 1: $\sigma$ known, large/infinite population.
- Case 2: $\sigma$ unknown, small sample, infinite population.
- Uses the formulas in the table in 2.4.

---

## 3. Exam / Assignment Information

### Syllabus boundary
- The syllabus runs **up to and including sample size estimation**. Know $n = z^2\sigma^2/E^2$, the round-up rule, and the worked examples.
- **Excluded:** population proportions, the sampling distribution of proportions, CLT for proportions, and the related estimations.
- The instructor said the binomial and proportion formulas need not be memorized.

### Likely exam-style skills, based on the worked example
- Find $\mu_{\bar{X}}$ and $SE = \sigma/\sqrt{n}$ using the CLT.
- Compute z-scores and read areas from the standard normal table.
  - Note that this class's table gives the area from $0$ to $z$, so add $0.5$ for cumulative probabilities.
- Find probabilities of the form $P(\bar{X} \le a)$ and $P(a \le \bar{X} \le b)$.
- Construct a 95% confidence interval using $z = 1.96$.

### Marks breakdown (this instructor's share: 25 marks)
| Component | Marks |
|---|---|
| End-semester exam (this instructor's part of the question paper) | 15 |
| Individual assignment (titles to be shared, allocated by roll number) | 5 |
| Class participation | 5 |

### Exam format
- The question paper will be shared as a **PDF**.
- Write your answers by hand on **white paper**.
- Combine all pages into **one file** and **upload** it.

<!-- nav -->
← [Session 29 (2026-10-23)](DSM-101-29_2026-10-23_Pritee-Sharma.md) · [All lectures](./) · [Session 31 (2026-10-27)](DSM-101-31_2026-10-27_Ruchi-Sharma.md) →
<!-- /nav -->
