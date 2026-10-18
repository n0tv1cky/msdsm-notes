---
course: DSM 101
date: 2026-10-17
start: 2:45 pm
session: "26"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 25 (2026-10-16)](DSM-101-25_2026-10-16_Pritee-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-101 Probability & Statistics: Session 26 Study Notes
**Date:** 2026-10-17 | **Instructor:** Prof. Pritee Sharma

---

## 1. Overview

This session finished the **descriptive statistics of location** and started **measures of dispersion**. It began by revisiting how to compute quartiles for ungrouped data, because students had asked about this. It then covered the positional rule for $Q_1$, $Q_2$ and $Q_3$, a class exercise, how percentiles are used in standardized tests, and the frequency-table method for the mean. Next came the formulas for **mean, median and mode of grouped data**, each with a worked example, including the continuity correction for class boundaries. The second half introduced **dispersion** (spread or variability). A computer-chip supplier example showed why averages alone can mislead. The session then covered **range** and **interquartile range (IQR)**, with merits and demerits, and introduced the **sample standard deviation**: why deviations are squared, the least-squares property, and why we divide by $n-1$ (degrees of freedom). Worked SD examples are deferred to the next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Central vs. non-central location measures

- **Central tendency measures** (mean, median, mode) give one value located at the "center" that represents the whole dataset.
- **Non-central (positional) measures** describe which values sit at various positions across the data. All of them are **quantiles**.

| Quantile type | Parts the data is split into | Number of cut values |
|---|---|---|
| Quartiles | 4 | 3 ($Q_1, Q_2, Q_3$) |
| Quintiles | 5 | 4 |
| Deciles | 10 | 9 |
| Percentiles | 100 | 99 |

- **Key rule:** splitting into $k$ parts needs $k-1$ cut values.
- **Interpretation of $Q_1$:** 25% of the observations lie below $Q_1$ and 75% lie above it.

### 2.2 Computing quartiles for ungrouped (raw) data

This uses the same idea as the median: either take the value at the exact position, or average two neighbouring values. Sort the data first.

Positions:
- $Q_1$: position $\dfrac{n}{4}$
- $Q_2$ (median): position $\dfrac{2n}{4} = \dfrac{n}{2}$
- $Q_3$: position $\dfrac{3n}{4}$

Rules (shown for $Q_1$; the same logic applies to $Q_2$ and $Q_3$):
1. **If $\dfrac{n}{4}$ is an integer:** $Q_1$ is halfway between the $\left(\dfrac{n}{4}\right)^{\text{th}}$ observation and the next one, i.e. their average.
2. **If $\dfrac{n}{4}$ is not an integer:** $Q_1$ is the observation at the **next highest integer** position.

> Remember: these are *positions* in the ordered data, not values.

**Worked example ($n = 10$, sorted data on slide):**
- **$Q_1$:** $\dfrac{n}{4} = \dfrac{10}{4} = 2.5$, which is not an integer. Round up to position 3. The 3rd observation is 225, so $Q_1 = 225$.
- **$Q_2$ (median):** $\dfrac{n}{2} = \dfrac{10}{2} = 5$, which is an integer. Average the 5th and 6th observations:
  $$Q_2 = \frac{225 + 235}{2} = 230$$
- **$Q_3$:** $\dfrac{3n}{4} = \dfrac{30}{4} = 7.5$, which is not an integer. Round up to position 8. The 8th observation is 250, so $Q_3 = 250$.

*(The full dataset was on the slide and not read aloud. The transcript gives 225 for both the 3rd and 5th observations, which is possible if values repeat. Check against the PPT.)*

### 2.3 Class exercise: mean, median, mode, quartiles

The dataset was on the slide only. The answers given in class were:
- Mean $\approx 6.33$ (a student answered "6"; the instructor gave 6.33. The transcript says "median 6.33", which is almost certainly a mis-speak for the mean.)
- Median $= 6.5$
- Mode $= 10$
- $Q_1 = 3.5$, $Q_2 = 6.5$, $Q_3 = 9.5$

Once you can compute $Q_1$ and $Q_3$, you can compute quintiles, deciles and percentiles the same way.

### 2.4 Where quantiles are used: percentiles in standardized tests

- Large-scale exams often report **percentiles** rather than raw marks.
- **Example:** a raw score of 40 out of 100 looks poor. If it is the **99th percentile**, the candidate is in the **top 1%** of everyone who took the exam. Few people scored close to 40 or higher.
- Percentiles rank you relative to other candidates' observed scores. They are not marks out of 100.
- **Quartiles as percentiles:**
  - $Q_1$ = 25th percentile
  - $Q_2$ = 50th percentile (the median)
  - $Q_3$ = 75th percentile

### 2.5 Recap example: reading levels of 8th-grade students

Setup: 16 students took a reading test, and the scores were sorted.

- **Mean:** $\bar{x} = \dfrac{\sum x_i}{n} = \dfrac{120}{16} = 7.5$
- **Median:** $7.5$
- **$Q_1$:** $6$; **$Q_2$:** $7.5$; **$Q_3$:** $9$
- **Mode:** $9$ (it appears 5 times)

**Alternative method: frequency distribution.** List each distinct score $x_i$ with its frequency $f_i$, then:
$$\bar{x} = \frac{\sum x_i f_i}{\sum f_i} = \frac{\sum x_i f_i}{n}$$
- Example row: score 5 obtained by 2 students gives $x_i f_i = 5 \times 2 = 10$.
- Summing all $x_i f_i$ gives $120$, and $120/16 = 7.5$, the same as before.
- This method is preferred when the **same values repeat often** in the data.

### 2.6 Mean of grouped data

**Example:** minutes employees take to reach the office.
- Classes: 0–10, 10–20, 20–30, 30–40, 40–50, each with a frequency (number of employees).
- **Step 1:** take each class **midpoint** as $x_i$: $5, 15, 25, 35, 45$.
- **Step 2:** compute $x_i f_i$ for each class (e.g. the first class multiplies the midpoint 5 by a frequency of 3).
- **Step 3:** apply
$$\bar{x} = \frac{\sum f_i x_i}{N}, \qquad N = \sum f_i$$
- **Result:** $\bar{x} = 21.8$ minutes.
- On a histogram, the mean falls in the middle class (20–30), slightly to the right.

### 2.7 Median of grouped data

**Example:** ages of patients and frequency of hospital visits.

| Class (as given) | Continuous class | $f$ | Cumulative frequency $cf$ |
|---|---|---|---|
| 51–60 | 50.5–60.5 | 4 | 4 |
| 61–70 | 60.5–70.5 | 8 | 12 |
| 71–80 | 70.5–80.5 | 15 | 27 |
| 81–90 | 80.5–90.5 | 8 | 35 |
| 91–100 | 90.5–100.5 | 5 | 40 |

**Continuity correction:**
- Classes like 51–60, 61–70 are *inclusive* and leave gaps.
- Age is a **continuous** variable. Someone aged 60.4 would fall between 60 and 61 and be missed.
- Fix: convert to continuous boundaries by extending each limit by 0.5 (50.5–60.5, 60.5–70.5, …).

**Steps:**
1. Compute cumulative frequencies (table above).
2. $N = 40$, so $\dfrac{N}{2} = 20$.
3. **Median class:** the class whose cumulative frequency is the first one at or just above $N/2$. Since $cf = 27 \ge 20$, the median class is **70.5–80.5**.
4. Apply the formula:
$$\text{Median} = L + \left(\frac{\frac{N}{2} - cf}{f}\right) \times h$$

where:
- $L$ = lower limit of the median class $= 70.5$
- $N$ = total frequency $= 40$
- $cf$ = cumulative frequency of the class *before* the median class $= 12$
- $f$ = frequency of the median class $= 15$
- $h$ = class width $= 10$

$$\text{Median} = 70.5 + \frac{20 - 12}{15} \times 10 = 70.5 + 5.33 = 75.83 \approx 75.8$$

> **Slide correction flagged by the professor:** the formula on the slide was missing the "$\times h$" term. Include it in your notes.

### 2.8 Mode of grouped data

**Example:** marks obtained by students, in classes 0–10, 10–20, 20–30, ….
- **Modal class:** the class with the highest frequency. Here that is **10–20**, with frequency 24.

**Formula:**
$$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$$

where:
- $L$ = lower limit of the modal class $= 10$
- $f_1$ = frequency of the modal class $= 24$
- $f_0$ = frequency of the preceding class $= 18$
- $f_2$ = frequency of the succeeding class (not read out; $f_2 = 8$ reproduces the stated answer)
- $h$ = class width $= 10$

$$\text{Mode} = 10 + \frac{24 - 18}{2(24) - 18 - 8} \times 10 = 10 + \frac{60}{22} \approx 12.73$$

- **Result:** Mode $= 12.73$, which falls inside the modal class 10–20 on the histogram.
- The spoken labels for $f_0$ and $f_1$ were muddled in the transcript. The definitions above are the standard ones and match the answer.

### 2.9 Quantiles of grouped data

A general formula for any percentile or quantile of grouped data was shown on a slide but not read aloud. The standard form, which mirrors the median formula, is:
$$P_k = L + \left(\frac{\frac{kN}{100} - cf}{f}\right) \times h$$
Here $L$, $cf$, $f$ and $h$ refer to the class containing the $\left(\dfrac{kN}{100}\right)^{\text{th}}$ observation. Check this against the shared PPT.

---

### 2.10 Measures of dispersion: introduction

- **Definition:** dispersion is the amount of **spread, variation or variability** in a dataset.
- Central and non-central measures describe *location*. Dispersion describes *how spread out* the data are.

**Motivating example: buying computer chips**
- A company needs chips with an average life of about 10 years and must choose between two suppliers.
- It samples 10 chips from each supplier, assuming representative probability samples, and records chip life in years.
- **Supplier A** has average life 10.8 years.
- **Supplier B** has a higher average (transcribed as "94.6", likely an ASR error, perhaps 14.6). On the mean alone, B looks better.
- **New information:** a 3-year warranty, under which chips failing within 3 years are replaced.
  - Supplier A: **0** chips fail within 3 years.
  - Supplier B: **4 of 10** chips fail (some within 1 year), so **40% returns**.
- **Lesson:** the mean alone is misleading. We need measures of spread to make better decisions.

**Measures of dispersion to be covered:**
1. Range
2. Interquartile range (IQR)
3. Standard deviation
4. Variance
5. Coefficient of variation

### 2.11 Range

$$\text{Range} = \text{Largest value} - \text{Smallest value}$$

- **Example:** monthly profits of a small firm over 10 months (₹ lakhs). The maximum is 32 and the minimum is 12, so Range $= 32 - 12 = 20$ lakhs.
- **Merits:** very simple to compute and easy to explain to others (e.g. "our monthly income ranges over …").
- **Demerit:** it is **strongly affected by extreme values (outliers)**.

### 2.12 Interquartile range (IQR)

$$\text{IQR} = Q_3 - Q_1$$

**Example: monthly sales revenue of 15 outlets (₹ lakhs), sorted ascending**
- $Q_1 = 22$ and $Q_3 = 35$, so $\text{IQR} = 35 - 22 = 13$.
- By contrast, Range $= 120 - 15 = 105$.
- The large range shows big differences in outlet performance, so some outlets may be doing poorly. The small IQR shows that the middle of the data is much less dispersed.

**Merit:** not distorted by extreme values.

**Demerit:** it uses only the **central 50%** of observations. Everything below $Q_1$ and above $Q_3$ is ignored, so half the data is thrown away.

**Exercise example: bank loan disbursements**
- A bank assesses consistency of monthly loan disbursements (₹ crores) across its **15 regional branches for June 2026** (data on slide).
- **Answer: IQR $= 1.2$** crores.
- Range $= 12.5 - 4.2 = 8.3$ crores, a wide gap. This is likely driven by a few large metropolitan branches disbursing high volumes. The IQR shows that most branches are fairly consistent.

### 2.13 Standard deviation (sample)

- Denoted by $s$. It measures a kind of "average deviation" about the mean, i.e. how far observations lie on either side of $\bar{x}$.
- **It is not literally the average deviation.**
  - The sum of raw deviations from the mean is always zero, because positive and negative deviations cancel:
$$\sum_{i=1}^{n} (x_i - \bar{x}) = 0, \qquad \text{where } \bar{x} = \frac{\sum x_i}{n}$$

**Definitional formula:**
$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}$$

**Procedure (column-by-column):**
1. List each $x_i$ and compute $\bar{x}$.
2. Compute each deviation $(x_i - \bar{x})$. These sum to 0.
3. Square each deviation: $(x_i - \bar{x})^2$. This removes the negative signs.
4. Sum them: $\sum (x_i - \bar{x})^2$.
5. Divide by $n - 1$, not $n$.
6. Take the square root to return to the original units.

**Three key properties emphasized:**
1. **Squaring solves the zero-sum problem.** Squared deviations cannot cancel out.
2. **Least-squares property.** $\sum (x_i - \bar{x})^2$ is a **minimum**: no other value $a$ gives a smaller sum of squared deviations.
$$\sum (x_i - \bar{x})^2 \le \sum (x_i - a)^2 \quad \text{for all } a$$
   - Contrast with the median, from an earlier class, which minimizes the sum of **absolute** deviations: $\sum |x_i - \text{Median}|$ is a minimum.
3. **Divide by $n-1$ because one degree of freedom is lost.**
   - We use $\bar{x}$, a statistic computed from the same data, to compute another statistic ($s$).
   - Each statistic estimated from the data and then used in another calculation costs one degree of freedom.
   - **Illustration:** if $2x + 3y = 12$, you are free to choose only one variable. Once you assume a value for $y$, $x$ is determined ($x = \frac{12 - 3y}{2}$). One constraint means one degree of freedom is lost.

**Variance and coefficient of variation:** listed among the measures but not yet covered. For reference, the standard definitions are:
- Sample variance: $s^2 = \dfrac{\sum (x_i - \bar{x})^2}{n-1}$
- Coefficient of variation: $CV = \dfrac{s}{\bar{x}} \times 100\%$

---

## 3. Important for Exams/Assignments

No explicit exam announcements were made. These points were stressed:

- **Quartile position rules:** average two neighbours if the position is an integer; round up to the next integer if not. Positions are not values.
- **Interpretation:** $Q_1$ means 25% of data lie below it and 75% above. $Q_1, Q_2, Q_3$ are the 25th, 50th and 75th percentiles.
- **Grouped median formula:** remember the $\times h$ term, which was missing on the slide.
- **Continuity correction** for inclusive classes of a continuous variable such as age (e.g. 51–60 becomes 50.5–60.5).
- **Median class:** the first class with cumulative frequency at or above $N/2$. $cf$ in the formula is the cumulative frequency of the class *before* it.
- **Merits and demerits:**
  - Range is simple but sensitive to outliers.
  - IQR is robust but ignores 50% of the data.
- **Three properties of standard deviation:**
  - squaring avoids the zero sum;
  - the least-squares property;
  - the $n-1$ divisor reflects the loss of one degree of freedom.

**Next class:** worked examples of standard deviation, then variance and coefficient of variation.

**Admin:** the PPT will be shared on the LMS group. Use it to check datasets that were shown only on slides (the $n=10$ quartile example, the class exercise, the chip-life data, the commute-time frequencies, the mode example's $f_2$, and the bank branch data).

---

### Formula Sheet

| Quantity | Formula |
|---|---|
| Quartile positions (raw data) | $Q_1: \frac{n}{4}$, $Q_2: \frac{2n}{4}$, $Q_3: \frac{3n}{4}$ |
| Mean (raw) | $\bar{x} = \dfrac{\sum x_i}{n}$ |
| Mean (frequency / grouped) | $\bar{x} = \dfrac{\sum f_i x_i}{\sum f_i}$, with $x_i$ = class midpoint for grouped data |
| Median (grouped) | $L + \left(\dfrac{\frac{N}{2} - cf}{f}\right) h$ |
| Mode (grouped) | $L + \left(\dfrac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) h$ |
| Percentile (grouped, standard form) | $L + \left(\dfrac{\frac{kN}{100} - cf}{f}\right) h$ |
| Range | $x_{\max} - x_{\min}$ |
| IQR | $Q_3 - Q_1$ |
| Sum of deviations | $\sum (x_i - \bar{x}) = 0$ |
| Sample SD | $s = \sqrt{\dfrac{\sum (x_i - \bar{x})^2}{n-1}}$ |

<!-- nav -->
← [Session 25 (2026-10-16)](DSM-101-25_2026-10-16_Pritee-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
