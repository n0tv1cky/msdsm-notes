---
course: DSM 101
date: 2026-10-23
start: 7:00pm
session: "29"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 28 (2026-10-21)](DSM-101-28_2026-10-21_Pritee-Sharma.md) · [All lectures](./) · [Session 30 (2026-10-24)](DSM-101-30_2026-10-24_Pritee-Sharma.md) →
<!-- /nav -->

# DSM-101 Lecture 29: Kurtosis, Sampling Distributions & the Central Limit Theorem
**Session:** DSM-101-29 | **Date:** 2026-10-23 | **Instructor:** Pritee Sharma

---

## 1. Overview

The session opened by finishing the previous lecture's material on the shape of data. The instructor added **kurtosis** (leptokurtic, platykurtic and normal curves) to the earlier discussion of skewness. The main topic was **sampling distributions**, specifically the sampling distribution of the sample mean. Suppose many samples of the same size are drawn from a population and the mean of each is computed. Those sample means follow a normal distribution centred on the population mean $\mu$, with standard deviation (the **standard error**) $\sigma/\sqrt{n}$. This holds even when the population itself is not normal, provided $n \geq 30$. This result is the **Central Limit Theorem (CLT)**.

The CLT was first demonstrated with a tiny population $\lbrace 1,2,3,4,5\rbrace $ to show **unbiasedness**, $E[\bar{X}] = \mu$. It was then applied through the **z-transformation** to three worked problems: steel-chain breaking strength, bulb lifetime claims, and hybrid motor life. The motor problem contrasted an individual observation with a sample mean. The class ended with an e-commerce delivery-time problem assigned for discussion next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Skewness (shape of data)
- Skewness depends on where the **mean** falls relative to the **median**:
  - Mean > median: positive (right) skew.
  - Mean < median: negative (left) skew.
  - Mean = median: symmetrical (normal) distribution with no skewness.

### 2.2 Kurtosis (newly added)
- **Definition (as given in class):** Kurtosis describes how strongly the data are concentrated near the centre (median) versus spread out away from it.
- There are three curve types, all symmetrical:
  - **Leptokurtic:** Many data points lie very close to the median, giving a tall, narrow, peaked curve.
  - **Platykurtic:** Data are dispersed on both sides, far from the median, giving a flat, wide curve.
  - **Normal curve** (standard term: *mesokurtic*): The normal distribution sits between these two.
- Note: "curtosis", "leptocortic" and "platic" in the transcript are ASR errors for *kurtosis*, *leptokurtic* and *platykurtic*.

### 2.3 From observed data to sampling distributions
- **Recap of the hierarchy:** population (all elements in the universe) → sampling frame → sample → statistics computed on the observed sample values.
- Until now, the course analysed only the observed values of a single sample. The new goal is for sample **statistics** to approximate population **parameters** robustly.
- **Setup:**
  - Draw many samples $S_1, S_2, S_3, \dots$ from the same population, with no overlap between samples. Each sample has size $n$ (for example $n = 30$).
  - "Sample" here means a set of $n$ units, not a single unit.
  - **Example:** Measure the heights of 30 grade-5 students in sample $S_1$ and compute $\bar{x}_1$. Then compute $\bar{x}_2$ for $S_2$, $\bar{x}_3$ for $S_3$, and so on.
  - Plot all the $\bar{x}$ values. This plot is the **sampling distribution of the sample means**.
- **Classroom illustration:** Each student samples marks from different IIT Indore engineering branches drawn from the same population. Each student gets a different mean, and together those means form a normal distribution around the population mean.
- **Practical use:** Draw several samples from population 1, several from population 2, and so on. You can then compare outcomes across populations and study how samples behave within one population.

### 2.4 Central Limit Theorem (CLT)
- **Statement:** For large samples ($n \geq 30$ by convention), the sampling distribution of $\bar{X}$ is approximately **normal and centred at $\mu$**. This holds **even if the population distribution is non-normal**.
- **Properties** of the sampling distribution of means, as $n$ grows large:
  1. **Mean of the means equals the population mean:**

  $$E[\bar{X}] = \mu_{\bar{X}} = \mu$$

  2. **Standard deviation of the means equals the standard error (SE):**

  $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

  Here $\sigma$ is the population standard deviation and $n$ is the sample size.
  3. **Shape:** The distribution is normal.
- **Consequence stated in class:** About 95% of sample means fall within $\pm 2$ standard errors of $\mu$.
  - The precise value for 95% is $\pm 1.96$; $\pm 2$ gives about 95.4%.

### 2.5 Worked Example 0: Small population (demonstrating unbiasedness)
- **Population:** $N = 5$ elements with values $1, 2, 3, 4, 5$. Take random samples of size $n = 2$.
- **Number of possible samples:** $\binom{5}{2} = 10$.
- **Population parameters** (the full population is known):

  $$\mu = \frac{1+2+3+4+5}{5} = 3$$

  $$\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}} = \sqrt{\frac{4+1+0+1+4}{5}} = \sqrt{2} \approx 1.41$$

  - Divide by $N$, **not** $N-1$, because this is the entire population.
- **All 10 samples and their means:**

| Sample | (1,2) | (1,3) | (1,4) | (1,5) | (2,3) | (2,4) | (2,5) | (3,4) | (3,5) | (4,5) |
|---|---|---|---|---|---|---|---|---|---|---|
| $\bar{x}$ | 1.5 | 2.0 | 2.5 | 3.0 | 2.5 | 3.0 | 3.5 | 3.5 | 4.0 | 4.5 |

- **Mean of the sample means:**

  $$E[\bar{X}] = \frac{\sum \bar{x}}{10} = \frac{30}{10} = 3 = \mu$$

- **Unbiasedness:** The mean of all possible sample means equals the population mean. This property is called **unbiasedness**.
- **Supplementary note (not covered in class):** The instructor did not finish the standard-error check for this example.
  - The SD of the 10 means is $\sqrt{7.5/10} \approx 0.866$.
  - This differs from $\sigma/\sqrt{n} = 1.41/\sqrt{2} = 1$ because the sampling is without replacement from a tiny population.
  - Applying the finite population correction recovers the exact value:

  $$\frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}} = 1 \times \sqrt{3/4} = 0.866$$

### 2.6 Standardising the sample mean (z-transformation)
- Because $\bar{X}$ is normally distributed, it can be converted to a standard normal $Z$:

```math
Z = \frac{\bar{X} - E[\bar{X}]}{\sigma_{\bar{X}}} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}
```
- If $n$ is large ($\geq 30$), the sample standard deviation $s$ can replace an unknown $\sigma$. It serves as an estimate of the population standard deviation.
- **Contrast** this with the z-score for a **single observation**, which has no $\sqrt{n}$:

```math
Z = \frac{X_i - \mu}{\sigma}
```

### 2.7 Worked Example 1: Steel chains
- **Given:**
  - Population mean breaking strength $\mu = 200$ lb.
  - Population standard deviation $\sigma = 10$ lb.
  - Sample size $n = 100$ chains.
- **Question:** What is $P(\bar{X} \leq 195)$? Equivalently, what proportion of sample means fall at or below 195 lb?
- **Solution:**

```math
Z = \frac{195 - 200}{10/\sqrt{100}} = \frac{-5}{1} = -5
```
- **Interpretation:**
  - Almost all sample means lie within $\pm 3$ to $\pm 4$ standard errors of $\mu$.
  - $z = -5$ is far in the tail, so the probability is approximately 0.
  - The question concerns the **sample mean** of 100 chains, not one individual chain.

### 2.8 Worked Example 2: Light bulbs (should the claim be revised?)
- **Given:**
  - Claimed mean life $\mu = 15{,}000$ h.
  - Claimed standard deviation $\sigma = 1{,}000$ h.
  - Sample size $n = 100$ bulbs.
  - Observed sample mean $\bar{x} = 14{,}000$ h.
- **Solution:**

```math
Z = \frac{14{,}000 - 15{,}000}{1{,}000/\sqrt{100}} = \frac{-1000}{100} = -10
```
- **Interpretation:** The sample mean is 10 standard errors below the claimed mean.
  - The instructor said nearly all sample means (stated as 99.9%) lie within $\pm 3$ to $\pm 4$ SE.
  - Anything beyond $-4$ is extremely unlikely.
- **Conclusion:** **Yes, the manufacturer should revise the claim.**
  - A student initially answered "no". The calculation shows why that is wrong.

### 2.9 Worked Example 3: Hybrid motors (individual observation vs. sample mean)
- **Given:**
  - Motor life is normally distributed with $\mu = 100{,}000$ miles (1 lakh).
  - Standard deviation $\sigma = 10{,}000$ miles.

**Part (a): What is the probability that one randomly selected motor lasts between 90,000 and 110,000 miles?**
- No sample is drawn here; this is a single unit from the population. Use $X_i$ and $\sigma$, **without $\sqrt{n}$**:

```math
Z_1 = \frac{90{,}000 - 100{,}000}{10{,}000} = -1, \qquad Z_2 = \frac{110{,}000 - 100{,}000}{10{,}000} = +1
```
- **Reading the z-table:** Find the units and first decimal of $z$ down the left column. Find the second decimal across the top row.
  - For $z = 1.00$, the area between $0$ and $1$ is $0.3413$.
- By symmetry, the area between $-1$ and $0$ is also $0.3413$:

```math
P(-1 \leq Z \leq 1) = 0.3413 + 0.3413 = 0.6826
```
- **Answer:** $0.6826$ (68.26%).

**Part (b): For a random sample of $n = 100$ motors, what is $P(\bar{X} < 98{,}000)$?**
- Now use the sample-mean formula, with the standard error:

```math
Z = \frac{98{,}000 - 100{,}000}{10{,}000/\sqrt{100}} = \frac{-2000}{1000} = -2
```
- The table gives an area of $0.4772$ for $z = 2.00$, measured between $0$ and $2$.
- The whole left half of the curve has area $0.5$. Subtract the area between $-2$ and $0$:

```math
P(\bar{X} < 98{,}000) = 0.5 - 0.4772 = 0.0228
```
- **Answer:** $0.0228$ (about 2.3%).

### 2.10 Student Q&A: reading the z-table
- **Q1: Where does the $0.5$ come from?**
  - The total area under the normal curve is $1$.
  - The curve is symmetric about $\mu$, so the area to the right of $\mu$ is $0.5$ and the area to the left is $0.5$.
  - For "less than $-2$": take the left-half area ($0.5$) and remove the area between $-2$ and $\mu$ ($0.4772$).
  - The entire right half is excluded because the question asks about "less than".
- **Q2: Doesn't $\Phi(-x) = 1 - \Phi(x)$ apply here?**
  - That identity is for a **cumulative** table, where $\Phi(z) = P(Z \leq z)$.
  - The table used in class is a **half-table**. It gives the area from the mean ($0$) to $z$.
  - Symmetry means the same value works for $-z$.
  - **Key half-table values:**

| $z$ | Area from $0$ to $z$ | Area within $\pm z$ |
|---|---|---|
| 1 | $0.3413$ | $0.6826$ |
| 2 | $0.4772$ | $0.9544$ |
| 3 | $0.4987$ | $0.9974$ |

  - The instructor stated that about 99% of the area lies within $\mu \pm 3\sigma$. The table value is 99.74%.
  - **Conversion between table types:** cumulative $\Phi(z) = 0.5 + \text{(half-table area)}$ for $z > 0$.
  - **Check:** $\Phi(-2) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228$. This matches the half-table method.

---

## 3. Exam / Assignment Notes

- **Assigned for next class** (take a screenshot; it will be discussed next session). **E-commerce delivery times:**
  - **Given:**
    - Individual order delivery times are **right-skewed**.
    - $\mu = 4.5$ days and $\sigma = 2.3$ days.
    - Samples of size $n = 30$.
  - **Questions:**
    1. What is the sampling distribution of $\bar{X}$, and what is the standard error?
    2. What is $P(\bar{X} \leq 5)$?
    3. What is $P(4 \leq \bar{X} \leq 5)$?
    4. Construct a 95% confidence interval for the true mean delivery time using the sample mean.
  - **Key point:** The population is skewed, but $n = 30$ means the CLT still applies.
  - **Self-check (my own working, not from the lecture):**
    - $SE = 2.3/\sqrt{30} \approx 0.420$, and $\bar{X} \approx N(4.5,\ 0.420^2)$.
    - For both 4 and 5, $z = \pm 0.5/0.420 \approx \pm 1.19$.
    - $P(\bar{X} \leq 5) \approx 0.883$.
    - $P(4 \leq \bar{X} \leq 5) \approx 0.766$.
    - 95% CI: $\bar{x} \pm 1.96 \times 0.420 = \bar{x} \pm 0.82$ days.

- **Points the instructor emphasised (likely exam material):**
  - **Two different formulas:** Use $\sigma/\sqrt{n}$ when the question is about a **sample mean**. Use $\sigma$ alone for a **single randomly selected unit**. Example 3(a) versus 3(b) was the deliberate contrast.
  - **Population vs. sample SD:** Divide by $N$ (not $N-1$) when computing $\sigma$ for a fully known population.
  - **CLT conditions and properties:** $n \geq 30$; normal shape regardless of the population's shape; $E[\bar{X}] = \mu$ (unbiasedness); $\sigma_{\bar{X}} = \sigma/\sqrt{n}$.
  - **Interpreting extreme z-scores:** Values like $-5$ or $-10$ mean the event is practically impossible, or that a claim should be rejected or revised.
  - **Half-table technique:** Know how to use the area-from-the-mean table, including the $0.5$ subtraction for tail probabilities.

<!-- nav -->
← [Session 28 (2026-10-21)](DSM-101-28_2026-10-21_Pritee-Sharma.md) · [All lectures](./) · [Session 30 (2026-10-24)](DSM-101-30_2026-10-24_Pritee-Sharma.md) →
<!-- /nav -->
