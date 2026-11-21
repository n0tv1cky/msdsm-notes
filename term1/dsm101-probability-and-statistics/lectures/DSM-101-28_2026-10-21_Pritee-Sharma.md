---
course: DSM 101
date: 2026-10-21
start: 7:00pm
session: "28"
faculty: Pritee Sharma
---

<!-- nav -->
← [Session 27 (2026-10-19)](DSM-101-27_2026-10-19_Pritee-Sharma.md) · [All lectures](./) · [Session 29 (2026-10-23)](DSM-101-29_2026-10-23_Pritee-Sharma.md) →
<!-- /nav -->

# DSM-101 — Session 28 (21 Oct 2026) — Prof. Pritee Sharma

**Topic:** Descriptive Statistics (continued): Z-score recap, Five-Number Summary and Box Plots, Principles of Experimental Design, Frequency Distributions and their Graphs, and Two-Variable Descriptive Statistics

---

## 1. Overview

This session picked up from the previous class on standardized data (z-scores) and the empirical coverage of the normal distribution. It then covered more tools for describing how data are spread out. First came the **five-number summary** and the **box plot**, including how to read skewness from them. As an aside, the lecture explained why box plots are useful for comparing many samples, and covered the **three principles of experimental design**: replication, randomization, and local control. The class did a hands-on box-plot exercise. The lecture then turned to **frequency, percentage, and cumulative distributions**, using a salary example, and to their graphs: the histogram, the frequency polygon, and the cumulative frequency curve. A student asked when to use a polygon instead of a histogram, and the lecturer gave an income-inequality (Lorenz-curve-style) example. The session ended with **descriptive statistics for two variables**:

* contingency tables and side-by-side bar charts for categorical data
* scatter plots for numerical data, covering positive, negative, zero, and spurious correlation

Next class covers sampling and how to choose sample size.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Standardized Data and Z-scores

* The previous class built up from the mean, to standard deviation, variance, and coefficient of variation, and then to **z-scores**:

```math
z = \frac{x - \mu}{\sigma}
```
* If the data are **normally distributed**, the share of standardized data within each range is:

| Range of $z$ | Approx. % of data |
|---|---|
| $-1.96 \le z \le 1.96$ | 95% (often rounded to "within $\pm 2$ SD") |
| $-3 \le z \le 3$ | 99.7% |
| $-4 \le z \le 4$ | ~99.99% (precisely $\approx 99.994\text{%}$) |

* **Why this matters:** if the standardized scores fall within the expected range, the data are consistent with a normal distribution. Values far outside it (e.g., $|z| > 3$) point to **outliers or measurement errors** that need attention.

### 2.2 Five-Number Summary

* This is a descriptive statistic that shows how the data are **dispersed** and what **shape** they take.
* **Procedure:**
  1. Sort the data in **ascending order**.
  2. Record the five numbers:

     $$X_{\text{smallest}},\quad Q_1,\quad Q_2\ (\text{median}),\quad Q_3,\quad X_{\text{largest}}$$

* $X_{\text{largest}} - X_{\text{smallest}}$ gives the **range**.

**Worked example (from slide):**

| $X_{\text{smallest}}$ | $Q_1$ | Median ($Q_2$) | $Q_3$ | $X_{\text{largest}}$ |
|---|---|---|---|---|
| 2 | 8 | 10 | 15 | 63 |

* **Conclusion: the data are right-skewed (positively skewed).**
* **Reasoning:** in a right-skewed distribution, the distance from $Q_3$ to $X_{\text{largest}}$ is much greater than the distance from $X_{\text{smallest}}$ to $Q_1$:

  $$X_{\text{largest}} - Q_3 = 63 - 15 = 48 \quad\gg\quad Q_1 - X_{\text{smallest}} = 8 - 2 = 6$$

* *(The audio once says "16.5 to 63", but the slide value of $Q_3$ is 15. Use 15.)*
* **General rule for reading shape from the five numbers:**
  * **Symmetric:** $Q_1 - X_{\text{smallest}} \approx X_{\text{largest}} - Q_3$ and $Q_2 - Q_1 \approx Q_3 - Q_2$
  * **Right-skewed:** the right side distances are larger
  * **Left-skewed:** the left side distances are larger

### 2.3 Box Plot (Box-and-Whisker Plot)

* A box plot is a graph of the five-number summary. It can be drawn **horizontally** (the convention used in class) or **vertically**.
* **Construction (horizontal):**
  1. Draw a horizontal axis with the observed values.
  2. Draw a line from $X_{\text{smallest}}$ (here 2) to $X_{\text{largest}}$ (here 63). This line shows the range.
  3. Mark $Q_1 = 8$, $Q_2 = 10$, and $Q_3 = 15$.
  4. Draw a **box from $Q_1$ to $Q_3$**, with a line at the median. Shade the $Q_1$–$Q_2$ and $Q_2$–$Q_3$ parts differently.
* **Use for comparing many samples:** draw several box plots side by side, stacked horizontally or arranged vertically on a common axis. This shows at once which samples behave similarly and which lie far apart.
* **Box plot of normally distributed data:** symmetric. The median sits in the centre of the box, and the two whiskers have about equal length.

### 2.4 Aside: Three Principles of Experimental Design

This came up while explaining why box plots of many samples are useful in research.

1. **Principle of Replication**
   * Repeat every experiment several times.
   * If you collect primary data through your own experiment, repeat it **at least three times**.
2. **Principle of Randomization**
   * Assign treatments to experimental units **at random**. This avoids errors caused by the researcher's own choices.
   * *Example:* when testing a crop, grow it on as many different soil types as possible and place the seeds randomly across plots. This reduces bias from how land plots are selected.
3. **Principle of Local Control**
   * Deliberately form **homogeneous groups (blocks)** of an extraneous ("exogenous") variable that is not part of the study. This removes the effect of that variable.
   * *Example:*
     * The treatment is **high-yielding variety (HYV) seeds**, compared with **conventional variety** seeds.
     * Soil quality is the extraneous variable.
     * Identify adjacent plots with the same soil type. Within each such pair, plant the HYV in one plot and the conventional variety in the other.
     * Any yield difference within a pair is then not due to soil.

### 2.5 In-Class Exercise: Box Plot

Students computed the five-number summary from a data set on the slide.

| Statistic | Value |
|---|---|
| Minimum | 59 |
| $Q_1$ | 64.5 (one student said 64; the lecturer used **64.5**) |
| Median $Q_2$ | 66 |
| $Q_3$ | 70 |
| Maximum | 77 |

* **Range:**

  $$\text{Range} = X_{\max} - X_{\min} = 77 - 59 = 18$$

* **Interquartile range (IQR):** this is the spread of the middle 50% of the data.

  $$\text{IQR} = Q_3 - Q_1 = 70 - 64.5 = 5.5$$

* **Width of each quarter:**
  * $59 \to 64.5$: width 5.5
  * $64.5 \to 66$: width 1.5 (**smallest spread**)
  * $66 \to 70$: width 4
  * $70 \to 77$: width 7 (**largest spread**)
* **How to interpret this:**
  * By definition, each quarter holds about **25% of the data**.
  * The quarters have very different widths, so the data are spread unevenly. In an ideal symmetric distribution, the corresponding widths would match.
* **Conclusion given in class:** the data are **not normally distributed** and are **positively (right) skewed**. The upper whisker (7) is longer than the lower whisker (5.5).

### 2.6 Frequency Distributions (Organizing Data)

A frequency or percentage distribution can be used in three situations:

1. Numerical data **grouped into class intervals**.
2. Numerical data where **the same value is observed many times**.
3. **Categorical** data.

**Worked example: weekly salaries (US data)**

* The sample is **200 professionals**. Weekly salaries range from **USD 520 to USD 590**.
  * *(The audio garbles this as "1520–1590" and "500–590". The class intervals and the range of 70 confirm 520–590.)*
* The goal is to group the data into **7 equal classes**.
* Class width:

  $$\text{Width of interval} = \frac{\text{Range}}{\text{Number of classes}} = \frac{X_{\text{largest}} - X_{\text{smallest}}}{k} = \frac{590 - 520}{7} = \frac{70}{7} = 10$$

* The classes are 520–530, 530–540, …, 580–590.
* **Frequency column:** number of people in each class. The first class has 6, followed by 30, 38, and so on. *(The audio says "60" but means 6, as the percentage below shows.)*
* **Percentage column:**

  $$\text{Percentage} = \frac{\text{class frequency}}{n} \times 100$$

  For example, $\frac{6}{200} \times 100 = 3\text{%}$.

**Cumulative distribution**

* This shows the number or percentage of cases **below (or above) a specified value**, rather than within an interval.
* It is built by adding up the frequencies:
  * $< 520$: 0
  * $< 530$: 6
  * $< 540$: $6 + 30 = 36$
  * … and so on, each time adding the next class.
* A **cumulative percentage** column is calculated the same way.

### 2.7 Graphs of a Frequency Distribution

* **Frequency histogram**
  * Bars show the frequency of each class (6, 30, …).
  * **Histogram vs. bar chart:** a histogram is for continuous or grouped data, so its bars are **adjacent, with no gaps**. A bar chart has **separated** bars.
* **Frequency polygon**
  * Take the **midpoint of each class** and plot it against that class's frequency.
  * **Join the points** with straight lines.
* **Cumulative frequency distribution (ogive)**
  * Plot cumulative frequency against the class boundaries (520, 530, 540, …).
  * It answers questions such as "how many earn USD 550 or less?" and, by subtraction, "how many earn more than USD 550?"

**Q&A: when to use a histogram vs. a frequency polygon?**

* **Histogram:** the usual choice for grouped/class data from a **single sample** of one variable.
* **Frequency polygon:**
  * Suitable when you have exact values that repeat (e.g., many people earning exactly 525 or 545).
  * Mainly better for **comparing several samples on the same graph**, since several polygons (lines) can be overlaid.
  * *Example:* income distributions for 10 US states, one line per state.
  * *Example:* number of countries in each GDP-per-capita class (0–50, 50–100, 100–150, 150–200 USD, …).

### 2.8 Application of Cumulative Frequency: Income Inequality (Lorenz-curve idea)

* Cumulative distributions are commonly used to measure **income inequality within a nation**.
* **Set-up:** plot the cumulative share of population against the cumulative share of income/GDP.
  * The lecturer's axes were improvised. The standard form is: cumulative % of population on the x-axis, cumulative % of income on the y-axis.
* **The 45° line is the line of equality.** On this line, income is distributed equally across the population.
* **The actual curve is the line of inequality.** It sags below the 45° line.
* **The larger the area between the two lines, the greater the inequality.**
  * *(Context, not named in class: this is the Lorenz curve. The ratio of that area to the total area under the equality line is the Gini coefficient.)*

### 2.9 Descriptive Statistics for Two Variables

| Data type | Tools |
|---|---|
| **Categorical** | Contingency table; side-by-side bar chart |
| **Numerical** | Scatter plot; correlation; regression line (cause and effect) |

#### (a) Contingency table: "Who would you vote for in the next election?" (US example)

* Two categorical variables: **gender** (Male/Female) and **party** (Republican/Democrat).
* The total sample is 1,000.

**Frequencies:**

| | Republican | Democrat | Total |
|---|---|---|---|
| Male | 250 | 150 | 400 |
| Female | 250 | 350 | 600 |
| Total | 500 | 500 | 1000 |

**Percentages of the total:**

| | Republican | Democrat | Total |
|---|---|---|---|
| Male | 25% | 15% | 40% |
| Female | 25% | 35% | 60% |
| Total | 50% | 50% | 100% |

* **Reading the table:**
  * Overall, 500 people vote Republican and 500 vote Democrat.
  * The voters include 400 males and 600 females.
  * Equal shares of males and females vote Republican (25% each).
  * Far more females than males vote Democrat (35% vs 15%).

#### (b) Side-by-side bar chart: server performance

* The chart compares **Windows 2000 Server** and **Windows 2003 Server**.
* Performance is measured as streaming speed in kbps.
* Three configurations were tested:
  * Broadcast
  * On-demand using a hardware RAID data disk ("HW rate" in the audio)
  * On-demand using a single data disk
* **Findings:**
  * The 2003 server performs **fairly consistently** across all three configurations.
  * The 2000 server does better in broadcast, but its **performance declines** in the two on-demand configurations.

#### (c) Scatter plot (numerical data)

* Plot one variable on the x-axis and the other on the y-axis.
* *Example:* students' **academic grades vs. height (inches)**. Each student is one point (e.g., "point A").
  * The real plot showed **no pattern**, so there is no relationship.
* **Possible patterns:**
  * **Positive correlation:** points rise from left to right.
  * **Negative correlation:** points fall from left to right.
  * **No (zero) correlation:** no discernible pattern.
  * **Spurious:** a relationship we expected (or that appears) is not a genuine one.
* **Where each analysis belongs, as stated by the lecturer:**
  * Scatter plots and correlation are **descriptive statistics**.
  * Establishing **cause and effect** with a **regression line** falls under **inferential statistics**.

---

## 3. Exam / Assignment Notes

* **Nothing was explicitly flagged for exams or assignments** in this session.
* Likely practice material based on emphasis:
  * Computing a **five-number summary, range, and IQR**, and **drawing a box plot**. This was the in-class exercise: 59, 64.5, 66, 70, 77, giving range 18 and IQR 5.5.
  * **Reading skewness** from the five-number summary or box plot.
  * The **class-width formula**, $\frac{\text{Range}}{\text{Number of classes}}$, and building frequency, percentage, and cumulative tables.
  * The **three principles of experimental design**: replication, randomization, and local control.
* **Next class:** sampling, and how to decide an appropriate **sample size**.

---

## Quick Formula Sheet

```math
z = \frac{x - \mu}{\sigma}
```

```math
\text{Range} = X_{\text{largest}} - X_{\text{smallest}}
```

```math
\text{IQR} = Q_3 - Q_1
```

```math
\text{Class width} = \frac{X_{\text{largest}} - X_{\text{smallest}}}{\text{number of classes}}
```

```math
\text{Percentage} = \frac{f_i}{n} \times 100
```

```math
\text{Cumulative frequency up to class } j = \sum_{i=1}^{j} f_i
```

```math
\text{Class midpoint} = \frac{\text{lower limit} + \text{upper limit}}{2}
```

**Normal coverage:**
* $\pm 1.96\sigma \to 95\text{%}$
* $\pm 3\sigma \to 99.7\text{%}$
* $\pm 4\sigma \to \approx 99.99\text{%}$

<!-- nav -->
← [Session 27 (2026-10-19)](DSM-101-27_2026-10-19_Pritee-Sharma.md) · [All lectures](./) · [Session 29 (2026-10-23)](DSM-101-29_2026-10-23_Pritee-Sharma.md) →
<!-- /nav -->
