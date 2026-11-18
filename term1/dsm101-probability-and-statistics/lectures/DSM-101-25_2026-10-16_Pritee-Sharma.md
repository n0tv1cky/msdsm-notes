---
course: DSM 101
date: 2026-10-16
start: 7:00pm
session: "25"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 24 (2026-10-12)](DSM-101-24_2026-10-12_Pritee-Sharma.md) · [All lectures](./) · [Session 26 (2026-10-17)](DSM-101-26_2026-10-17_Pritee-Sharma.md) →
<!-- /nav -->

# DSM-101 (Probability & Statistics), Session 25: Study Notes
**Session file:** DSM-101-25_2026-10-16_Pritee-Sharma

---

## 1. Overview

The session finished the previous lecture's discussion of **levels of measurement**. The main principle was that a researcher should always collect data at the **highest level of measurement possible**. This was shown with a smoking-behaviour questionnaire and a soft-drink preference questionnaire. The lecture then began a new section on **describing numerical data for a single variable**. It outlined the three families of summary measures (location, dispersion and shape) and covered **measures of central tendency** (mean, median and mode) in detail, with emphasis on how each behaves when there are **outliers**. It then introduced **non-central location measures (quantiles)**: quartiles, quintiles, deciles and percentiles, with a worked quartile example. The session ended with computing the **mean from an ungrouped frequency distribution**. **Grouped data**, further quantile examples and **shape of the data** are deferred to the next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Levels and Scales of Measurement

Each data type is measured on its corresponding scale:

| Data type | Scale |
|---|---|
| Nominal | Nominal scale |
| Ordinal | Ordinal scale |
| Interval | Interval scale |
| Ratio | Ratio scale |

**Key principle:** As a researcher, the goal is to **use the highest level of measurement possible**. Higher levels allow more kinds of analysis.

#### Example 1: Measuring smoking behaviour

- **Option A:** "Do you smoke?" gives Yes/No.
  - This is **nominal** data.
  - The most you can do is count frequencies and report the **mode**. No further analysis is possible.
- **Option B:** "How many cigarettes did you smoke in the past 3 days (72 hours)?" gives an exact count.
  - This is **ratio** data.
  - You can compute the mean, median, mode and frequencies.
- **Option B is better** because it puts you in a much stronger position to study smoking behaviour.

#### Example 2: Comparing soft drinks (Coke, Pepsi, 7 Up, Sprite, Dr. Pepper)

- **Scale A (ranking):** "Please rank the taste of the following soft drinks from 1 to 5" (1 = best).
  - This gives **ordinal** data.
  - **Problem:** someone who dislikes all soft drinks is still forced to rank one as 1st, one as 2nd, and so on. You cannot tell whether a respondent dislikes them all or is neutral to all of them.
- **Scale B (rating):** "Please rate each of the following brands" on the categories Excellent / Very good / Good / Fair / Poor / Very poor / Awful.
  - This gives approximately **interval** data, and means can easily be computed from the responses.
  - Someone who hates all five drinks can tick "Awful" for every one, so you can detect that they do not like soft drinks at all.
- **Rating scales** like Scale B:
  - Researchers often **treat them as interval scales**.
  - Strictly, they are **ordinal, but better than ordinal and slightly poorer than interval**.
  - The reason is that responses are still subjective. You cannot say how much better "Excellent" is than "Very good", or how much worse "Awful" is than "Very poor".
  - They still give much clearer information than pure ranking.

---

### 2.2 New Section: Describing Numerical Data (One Variable)

The focus is now only on **numerical data for a single variable**: the observations recorded from a sample drawn from a population. Numerical data can be summarized by these characteristics:

1. **Measures of location**
   - Measures of **central tendency**: mean, median, mode.
   - Measures of **non-central tendency**: quantiles (quartiles, quintiles, deciles, percentiles).
2. **Measures of dispersion**: range, interquartile range (IQR), variance, standard deviation, coefficient of variation.
3. **Measures of shape**: skewness.
4. **Summary indicators and displays**:
   - five-number summary;
   - box-and-whisker plot;
   - stem-and-leaf display;
   - standardizing the data.

---

### 2.3 Measures of Central Tendency

**Definition:** For a data set on the scale of real numbers, a measure of central tendency is **one centrally located value that represents the entire data set**. The three such measures are the mean, median and mode.

#### (a) Mean (arithmetic / sample mean)

Observations are recorded as $X_1, X_2, \dots, X_n$, where $n$ is the sample size. For example, heights of $165$ cm, $180$ cm and $170$ cm.

$$\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n} = \frac{X_1 + X_2 + \cdots + X_n}{n}$$

- Data does **not** need to be ordered to compute the mean.
- **Example 1:** a small data set (values partly garbled in the recording) whose mean was $4$.
- **Example 2 (outlier):** data $1, 1, 1, 1, 51$.
  $$\bar{X} = \frac{1+1+1+1+51}{5} = \frac{55}{5} = 11$$
  Four of the five values are $1$, yet the mean is $11$.
- **Key point:** the **mean is affected by extreme values (outliers)**.
- A student asked how to handle outliers, using the example $1, 3, 5, 6, 64$. The answer is that when extreme values may be present, we use the **median**.

#### (b) Median

**Definition:** The median is the **middle value of the ordered data**.

- Order the data first. Ascending order is conventional, but descending is also acceptable.
- The **position** of the median in the ordered data is
  $$\text{Median position} = \frac{n+1}{2}$$

**Case 1: $n$ odd.** The median is the $\frac{n+1}{2}$-th observation directly.

- Example: ordered data $0, 2, 3, 5, 20, 99, 100$, so $n = 7$.
- Position $= \frac{7+1}{2} = 4$, so the 4th observation gives **median $= 5$**.
- If the last value is changed from $100$ to $5000$, the **median is still $5$**.

**Case 2: $n$ even.** Position $\frac{n+1}{2}$ is a half-position, so average the two middle values.

- Example: $n = 6$, so position $= \frac{6+1}{2} = 3.5$.
- Take the 3rd observation ($30$) and the 4th observation ($40$):
  $$\text{Median} = \frac{30 + 40}{2} = 35$$

**Three properties of the median (stressed as important):**

1. The median is **not affected by extreme values on either side**, low or high. It depends only on the number and order of observations.
2. Any observation selected at random is **equally likely to be greater than or less than the median**.
3. The **sum of absolute deviations about the median is minimum**. That is, for any other value $c$:
   $$\sum_{i=1}^{n} |X_i - \text{Median}| \le \sum_{i=1}^{n} |X_i - c|$$

**In-class exercise.** Use the data $0, 2, 3, 5, 20, 99, 1000$.

- **Task:** compute $\sum |X_i - \text{Median}|$, $\sum |X_i - \bar{X}|$ and $\sum |X_i - \text{Mode}|$, and identify the smallest.
- **Method:** for each observation compute $X_i - \text{Median}$, take the absolute value, then add them up. Repeat with the mean (and the mode).
- The mode is not applicable here because no values repeat.
- **Conclusion given in class:** the sum about the median is the minimum.

*Worked solution (computed for these notes; not read out in class):*

- **Median** $= 5$ (the 4th of 7 values).
  - Absolute deviations: $5, 3, 2, 0, 15, 94, 995$.
  - $$\sum |X_i - 5| = 1114$$
- **Mean** $= \frac{1129}{7} \approx 161.29$.
  - Absolute deviations: $\approx 161.29,\ 159.29,\ 158.29,\ 156.29,\ 141.29,\ 62.29,\ 838.71$.
  - $$\sum |X_i - \bar{X}| \approx 1677.43$$
- **Result:** $1114 < 1677.43$, which confirms that the median minimizes the sum of absolute deviations.

#### (c) Mode

**Definition:** The mode is the **value that occurs with the greatest frequency** in the data.

- Data $1, 1, 1, 1, 51$: $1$ occurs four times, so **mode $= 1$**.
- Another data set where $1$ appears three times: **mode $= 1$**.
- A data set where $5$ appears 3 times and $10$ appears 3 times is **bimodal** (modes $5$ and $10$).
- **No mode:** if all values are different (e.g., 10 distinct observations), there is no mode. A value must appear **at least twice** to be a mode.
  - *Note:* the lecturer at one point called an all-distinct data set "multimodal", but later stated clearly that **there is no mode** in that case. "No mode" is the correct convention.
- **Mode may not be unique:** in one example, six different values each appeared twice, giving **six modes**.
- A data set can be **unimodal** (one mode), **bimodal**, **multimodal**, or have **no mode**.

**Comparison of uniqueness:**

| Measure | Uniqueness for a given data set |
|---|---|
| Mean | Always exactly one value |
| Median | Always exactly one value |
| Mode | May be one, several, or none |

#### Q&A: How do we know if data has outliers (mean vs. median)?

- **Simple check:** compute both the mean and the median.
  - If they are **very close**, there are probably not many outliers.
  - If the data is **normally distributed**, then $\text{Mean} = \text{Median} = \text{Mode}$.
  - If the data is **positively or negatively skewed**, there will be a large difference between the mean, median and mode.
- The distance between the measures alone is not enough to decide. You should also:
  - **plot the data**;
  - compute all three central tendency measures;
  - compute quartiles and other quantiles;
  - look at dispersion, shape and summary statistics.
- These measures together tell you which representative value to choose. This is covered in upcoming lectures (skewness and shape).
- Hand calculations are only meant to show what happens "behind" software computations on large data sets.

---

### 2.4 Measures of Non-Central Location: Quantiles

**Definition:** Quantiles **split the ordered data into equal parts**. They summarize the data through non-central locations, which shows how the data is spread.

| Quantile | Parts | Number of cut points |
|---|---|---|
| Quartiles | 4 | 3 ($Q_1, Q_2, Q_3$) |
| Quintiles | 5 | 4 |
| Deciles | 10 | 9 |
| Percentiles | 100 | 99 |

- **Analogy:** to cut a chocolate bar into 4 equal pieces you need **3 cuts**. In general, $k$ parts need $k-1$ cuts.
- Always **order the data first**.

**Quartiles:**

- $Q_1$ (first quartile): 25% of observations are smaller and 75% are larger.
- $Q_2$ (second quartile) is the **median**: 50% below and 50% above.
- $Q_3$ (third quartile): 75% of observations are smaller and 25% are larger.
- Like the median, a quartile either equals one of the observations or lies halfway between two observations.
- **Idea:** after finding the median, find the "median" of the lower half to get $Q_1$ and of the upper half to get $Q_3$.

**Worked example: quartiles with $n = 10$** (only some of the data values were audible in the recording)

- **Median ($Q_2$):**
  - Position $= \frac{10+1}{2} = 5.5$, so average the 5th and 6th values, which are $225$ and $235$.
  - $$Q_2 = \frac{225 + 235}{2} = 230$$
- **$Q_1$:**
  - Compute $\frac{n}{4} = \frac{10}{4} = 2.5$.
  - The rule as stated was that $Q_1$ is "halfway between the $\frac{n}{4}$-th observation and the next". In the example, $Q_1$ was taken as the **3rd observation**.
  - In effect, $2.5$ was rounded up to the next whole position.
- **$Q_3$:**
  - By symmetry, $Q_3$ is the **3rd observation from the top** (the 8th observation).
  - Its value was $250$.
- **Caution:** Excel and other software may give slightly different quartile values on large data sets, because they use different interpolation conventions.

The lecturer will share slides with more quantile examples to practise. Quintile, decile and percentile examples continue next class.

---

### 2.5 Worked Example: Five Summary Statistics, and the Mean from a Frequency Distribution

**Context:** an 8th-standard class has **16 students**, each given a reading-level score.

- **Method 1 (raw data):** arrange the scores from lowest to highest. Then compute the sum, the **mean, median, mode, $Q_1$ and $Q_3$**. These describe the centre and spread of the data.
- **Method 2 (ungrouped frequency distribution):**
  - List each distinct score $X_i$ with its frequency $f_i$. For example, the lowest score $5$ was obtained by $2$ students, so $f = 2$.
  - The sum of frequencies must equal the number of observations:
    $$\sum f_i = n = 16$$
  - Compute $X_i f_i$ for each score, then sum. The mean is
    $$\bar{X} = \frac{\sum X_i f_i}{n} = \frac{\sum X_i f_i}{\sum f_i}$$
  - For large data sets this is more efficient than summing every individual value.
  - "Ungrouped" means each individual score value gets its own row with its frequency.

---

## 3. Exam / Assignment Notes and Follow-ups

- No explicit exam announcement was made.
- **Emphasized as important:**
  - The **three properties of the median**, especially that the **sum of absolute deviations about the median is minimum**.
  - The **mean is sensitive to outliers**, while the **median is robust**.
  - **Uniqueness:** mean and median are always unique; the mode may be multiple or absent.
  - The **principle of using the highest level of measurement**, with the smoking and soft-drink examples.
- **Practice:**
  - The in-class exercise on absolute deviations using $0, 2, 3, 5, 20, 99, 1000$.
  - The quartile, quintile, decile and percentile examples on the slides the lecturer will share.
- **Next class:**
  - mean for **grouped data**;
  - more quantile (quintile) examples;
  - **shape of the data** (skewness);
  - then dispersion measures and the five-number summary / box plot.

<!-- nav -->
← [Session 24 (2026-10-12)](DSM-101-24_2026-10-12_Pritee-Sharma.md) · [All lectures](./) · [Session 26 (2026-10-17)](DSM-101-26_2026-10-17_Pritee-Sharma.md) →
<!-- /nav -->
