---
course: DSM 101
date: 2026-11-10
start: 7:00pm
session: "36"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 35 (2026-11-09)](DSM-101-35_2026-11-09_Ruchi-Sharma.md) · [All lectures](./) · [Session 37 (2026-11-11)](DSM-101-37_2026-11-11_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 Probability & Statistics: Session 36 Study Notes
**Instructor:** Ruchi Sharma  **Date:** 10 Nov 2026

---

## 1. Overview

This session finishes the unit on the **normal distribution** and then starts **correlation**. It opens with a recap of the normal and standard normal distributions: the $Z$-transformation, the PDFs, the CDF $\Phi(z)$ and the symmetry property. It then sets out a three-step procedure for making inferences with $z$-scores. The instructor lists the characteristics of the normal curve and uses an Excel simulation to show how the mean and variance change the curve's shape. She explains why the normal distribution matters: it underlies large-sample approximations, sampling distributions, small-sample tests, hypothesis testing and quality control. She covers the **area property**, including the key critical values $\pm 1.96$ and $\pm 2.58$. Two worked examples follow: a $N(12, 4^2)$ probability problem and an agricultural-yield problem with $\mu = 662$, $\sigma = 32$ and a batch of 1000 plots. The second half introduces **bivariate distributions and correlation**: positive and negative relationships with examples, scatter diagrams and their limitations, and the assumptions behind the **Karl Pearson correlation coefficient**, which the class will continue next session.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Normal and Standard Normal Distribution

- A random variable $X$ is **normally distributed** with mean $\mu$ and variance $\sigma^2$, written $X \sim N(\mu, \sigma^2)$, if its PDF is:

```math
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad -\infty < x < \infty
```
  - The denominator of the exponent uses $2\sigma^2$, which is twice the **variance**, not the standard deviation. The instructor corrected herself on this point.

- **Standard normal variate:** this is defined as

```math
Z = \frac{X - \mu}{\sigma}
```
  It has these properties:
  - $E[Z] = 0$ and $\mathrm{Var}(Z) = 1$, so $Z \sim N(0, 1)$.
  - $Z$ is created from $X$. Probability tables are therefore looked up for the **standard normal** distribution, not for the original $N(\mu, \sigma^2)$. This point came up because a student asked about it.
  - Interpretation: you "normalize" a variable by subtracting its mean and dividing by its standard deviation.

- **PDF of the standard normal:**

```math
\varphi(z) = \frac{1}{\sqrt{2\pi}}\, e^{-z^2/2}, \qquad -\infty < z < \infty
```

- **Distribution function (CDF)** is the area under the curve up to $z$:

```math
\Phi(z) = P(Z \le z) = \int_{-\infty}^{z} \varphi(u)\, du
```

- **Symmetry property:** the curve is symmetric about its mean of $0$, so

```math
\Phi(-z) = 1 - \Phi(z)
```
  - The class used this property earlier in a marks example involving the values 73 and 77, where one student scored 87. Full details are in the previous lecture.

### 2.2 Making Inferences with the $z$-Score (three steps)

1. **Calculate the $z$-score:** $z = \dfrac{x - \mu}{\sigma}$.
2. **Find the critical value or probability** from the standard normal probability tables.
3. **Make the assessment or inference** based on that value.

### 2.3 Characteristics of the Normal Distribution (recap)

- The curve is bell-shaped.
- It is symmetrical about the mean.
- Mean = median = mode.
- As $x$ moves away from $\mu$ numerically in either direction, $f(x)$ decreases.
- A linear combination of independent normal variates is also normally distributed. The transcript says "independent" here, but the standard result is that the combination is *normal*.
- The $x$-axis is an asymptote to the curve: the curve never touches it.

### 2.4 Excel Simulation: Effect of Mean and Variance

- Starting setup: mean $= 0$, standard deviation $= 2$ (variance $= 4$). The instructor generated random values and computed the CDF and probabilities.
- Changing the **mean** from $0$ to $2$ **shifts the curve to the right**. A decrease would shift it left.
- **Increasing the variance** (for example to $10$) makes the curve **wider and flatter**, meaning more spread.
- Takeaway: the mean controls **location**, and the variance controls **spread**, i.e. how tightly values cluster around the mean.

### 2.5 Student Question: Comparing Sales of Two Companies

- **Question:** Can $z$-scores be used to decide which of two companies has better sales?
- **Answer:**
  - Comparing the two means alone shows a difference but **not whether it is statistically significant**.
  - Example given: monthly data for 10 years gives 120 points per company. The averages are ₹23 lakh vs ₹23.5 lakh. Whether that gap is real or just sampling noise depends on the variances and the number of data points.
  - The method for this is **hypothesis testing**, which is built entirely on the normal distribution.
    - You start from a null hypothesis: "no difference between the average sales."
    - The same framework will be used for tests of difference of means, difference of proportions, and correlation and regression coefficients.

### 2.6 Importance of the Normal Distribution

1. **Approximation of other distributions:** distributions such as the binomial (and Poisson) can be approximated by the normal as $n$ grows.
2. **Sampling distributions:** $t$ and $\chi^2$ tend to normality as $n \to \infty$, i.e. "these distributions tend to normality for large samples."
3. **Sample statistics:** the sampling distributions of the sample mean and sample variance also tend to normality for large $n$.
4. **Small-sample tests** ($t$-test, $F$-test, $\chi^2$-test) rest on the fundamental assumption that the **population from which the sample is drawn is normally distributed**.
5. **Applications:** it is used widely in **statistical quality control**, for example in setting control limits in operations management.

### 2.7 Area Property of the Normal Curve

The area under the curve within $k$ standard deviations of the mean is:

| Interval | Area (probability) |
|---|---|
| $\mu \pm \sigma$ | $\approx 0.6826$ (about 68%) |
| $\mu \pm 2\sigma$ | $\approx 0.9544$ (about 95.4%) |
| $\mu \pm 3\sigma$ | $\approx 0.9973$ (about 99.7%) |

Some important standard normal values:

| $z$ | Central area covered |
|---|---|
| $\pm 0.6745$ | 50% |
| $\pm 1.96$ | 95% |
| $\pm 2.58$ | 99% |

Transcription corrections:
- The transcript says "2.9544" for the $2\sigma$ area; the correct value is $0.9544$.
- It also says "0.745"; the standard value for 50% coverage is $0.6745$.

**$\pm 1.96$ and $\pm 2.58$ become critical in hypothesis testing.** If a computed $z$-score reaches 1.96, you are at the 95% boundary.

### 2.8 Worked Example 1: $X \sim N(12, 16)$

**Given:** $\mu = 12$, $\sigma = 4$, so $\sigma^2 = 16$. (The audio garbled "12" as "L".)

**Find:** $P(X \ge 20)$, $P(X \le 20)$ and $P(0 \le X \le 12)$. The audio said "0", but the class solution used 20 for the first two parts.

**(a) $P(X \ge 20)$:**

```math
z = \frac{20 - 12}{4} = 2
```

```math
P(X \ge 20) = 1 - P(X \le 20) = 1 - \Phi(2) \approx 1 - 0.9772 = 0.0228
```

**(b) $P(X \le 20)$:** this is the area to the left of $z = 2$.

```math
P(X \le 20) = \Phi(2) \approx 0.9772
```

**(c) $P(0 \le X \le 12)$:** the bounds convert to

```math
z_1 = \frac{0-12}{4} = -3, \qquad z_2 = \frac{12-12}{4} = 0
```

```math
P = \Phi(0) - \Phi(-3) = 0.5 - 0.00135 \approx 0.4987 \;(\approx 49.87\%)
```
- One student got 49.85% because tables differ slightly in rounding.

### 2.9 Worked Example 2: Agricultural Yield

**Problem:** The mean yield of a one-acre plot is **662 kg** with standard deviation **32 kg**. Assume yield is normally distributed. In a batch of **1000** one-acre plots, how many plots would you expect to have:
- (i) yield **greater than 760 kg**?
- (ii) yield **less than 650 kg**?
- (iii) A third part ("what would be the lowest yield of the best …") was **postponed** and not solved.

**(i) Yield $> 760$:**
- Step 1, $z$-score:

```math
z = \frac{760 - 662}{32} = \frac{98}{32} \approx 3.06
```
- Step 2, table lookup: $\Phi(3.06) \approx 0.9989$.
- Step 3, right-tail probability:

```math
P(X > 760) = 1 - 0.9989 = 0.0011
```
- Expected number of plots: $0.0011 \times 1000 \approx 1.1$, so **about 1 plot**.
- Note on percentages: the table value is a probability, not a percentage. Multiply by 100 for a percentage, or by 1000 to get a count out of 1000.

**(i′) Side calculation with 700:** a student misheard 760 as 700, and the class also solved this version.

```math
z = \frac{700 - 662}{32} = \frac{38}{32} = 1.1875 \approx 1.19
```

```math
P(X > 700) = 1 - \Phi(1.19) \approx 1 - 0.8830 = 0.1170
```
- Expected number of plots: $0.117 \times 1000 \approx$ **117 plots**.

**(ii) Yield $< 650$:** this is the area to the left of 650, which lies below the mean.

```math
z = \frac{650 - 662}{32} = \frac{-12}{32} = -0.375
```

```math
P(X < 650) = \Phi(-0.375) = 1 - \Phi(0.375) \approx 0.354
```
- Expected number of plots: $0.354 \times 1000 \approx$ **354 plots**. The class arrived at 354.

### 2.10 Introduction to Correlation: Bivariate Distributions

- So far the course has dealt with **univariate** distributions, which involve one variable.
- Correlation and regression deal with **bivariate** distributions, which involve two (or more) variables.
  - Regression will only be started in this course.
  - Full regression and hypothesis testing come in the Research Methods course.
- **Correlation** is **co-variation**: a change in one variable is associated with a change in another. It does **not** imply that one causes the other; it is only co-movement.

**Motivating example: car sales of two companies.**
- The data are monthly for 20 years, giving 240 points per company.
- The two series move together even though one is consistently higher. Possible reasons:
  - **Seasonal** variation: few people buy cars during inauspicious periods (Pitru Paksha), and purchases pick up around Navratri and festivals.
  - **Trend:** both series rise over time.
  - **Cyclical** factors: periods of rise and fall.
  - **Random or irregular** components.
- **Domain intuition and theory**, such as management theories of firm performance, should guide your hypotheses. This is where human judgment enters data analysis.

### 2.11 Types of Correlation

1. **Positive (direct):** both variables move in the same direction. Examples:
   - Height and weight of children up to about age 18.
   - Education and income per capita (or GDP per capita).
   - Income and consumption.
   - Supply and price: as price rises, supply rises.
2. **Negative (inverse/indirect):** the variables move in opposite directions. Examples:
   - Speed and travel time.
   - Price and quantity demanded. This is the **law of demand**, written $Q_d = f(P)$: as price rises, quantity demanded falls.
   - Vehicle weight and fuel efficiency.

### 2.12 Scatter Diagram (Visual Method)

- Plot one series ($X$) against the other ($Y$). The typical patterns are:
  - Positive linear
  - Negative linear
  - No relationship
  - Non-linear: for example, rising and then falling
- **Limitations of the scatter diagram:**
  1. It gives **no quantitative measure** of strength. You cannot say whether the relationship is 0.75, 0.5 or 0.4.
  2. **Subjectivity:** the choice of scale or omitted initial values can change how the graph looks.
  3. It **cannot test statistical significance** of the relationship.

### 2.13 Karl Pearson Correlation Coefficient: Introduction and Assumptions

- The Karl Pearson coefficient puts a **number** on the relationship between two variables.
- It measures **only linear** relationships. Non-linear patterns are not captured.
- Karl Pearson was a British biometrician who lived from 1857 to 1936. The transcript's "1867–1836" is a transcription error.
- It is typically the **first step** in any analysis of relationships.
- The formula has not been covered yet; it is expected next class.

**Assumptions:**
1. **Linear relationship:** the two variables are linearly related.
2. **Many independent causes leading to normality:** each variable is affected by a large number of independent contributory causes, so that each tends toward a normal distribution.
   - Examples: height, weight, firm profit, sales, prices, patenting intensity, market capitalization.
3. **Common forces:** the forces acting on the two variables are not entirely independent of each other. Some common forces must link them; otherwise there would be no correlation.
   - Example: the sales of two firms are both affected by seasonal, trend and cyclical factors, and by exogenous macroeconomic shocks such as a war or state closures.

**Next class preview:** a recap of these assumptions, then **spurious or "funny" correlations**. An example given was intelligence vs. physical size, where data may show a correlation with no real link.

---

## 3. Exam and Assignment Notes

- **Exam date: 23 November.** The instructor noted the gap between the end of the syllabus and the exam is short, so bring doubts to class.
- **Practice question file:** to be emailed soon. It covers binomial, Poisson, other distributions done in class, and normal-distribution questions such as marks and height/weight problems.
- **Assignment:** to be sent once the syllabus is completed, for practice and exam preparation.
- The instructor will also share her handwritten notes by **email** for recap.
- **Values to remember:**
  - $\pm 1.96$ covers 95% and $\pm 2.58$ covers 99%. These will be used heavily in hypothesis testing.
  - $\mu \pm \sigma$ covers about 68%, $\mu \pm 2\sigma$ about 95.4%, and $\mu \pm 3\sigma$ about 99.7%.
- **Skills to practise:**
  - The three-step $z$-score procedure.
  - Choosing left vs. right tail correctly: use $1 - \Phi(z)$ for "greater than".
  - Using symmetry, $\Phi(-z) = 1 - \Phi(z)$.
  - Converting a probability into an expected count, e.g. multiplying by 1000 for a batch of 1000 plots.

<!-- nav -->
← [Session 35 (2026-11-09)](DSM-101-35_2026-11-09_Ruchi-Sharma.md) · [All lectures](./) · [Session 37 (2026-11-11)](DSM-101-37_2026-11-11_Ruchi-Sharma.md) →
<!-- /nav -->
