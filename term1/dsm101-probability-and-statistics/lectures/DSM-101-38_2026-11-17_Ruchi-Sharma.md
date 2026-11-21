---
course: DSM 101
date: 2026-11-17
start: 7:00pm
session: "38"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 37 (2026-11-11)](DSM-101-37_2026-11-11_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-101 · Session 38 Study Notes: Rank Correlation, Partial Correlation, and an Introduction to Regression

**Instructor:** Ruchi Sharma | **Date:** 2026-11-17

---

## 1. Overview

The session opens with a recap of the Pearson correlation coefficient: its range, how to interpret its sign and size, and why zero correlation does not imply independence. It then introduces **Spearman's rank correlation coefficient**. The instructor derives the formula from the facts that ranks are the first $`n`$ natural numbers, so their mean is $`\frac{n+1}{2}`$ and their variance is $`\frac{n^2-1}{12}`$. Two worked examples follow. The first compares three judges ranking 10 contestants. The second shows how to handle tied (repeated) ranks, including the correction term $`\frac{m(m^2-1)}{12}`$. The instructor then covers the assumptions and limitations of rank correlation and briefly mentions partial and multiple correlation. The session ends by introducing **regression**: its origin in Francis Galton's work on inherited height ("regression towards mediocrity"), and the difference between deterministic relationships (natural sciences) and statistical relationships (economics and data science). The class ended slightly early; regression continues over the next two lectures.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Pearson correlation coefficient

- **Definition.** The correlation coefficient is the covariance divided by the product of the standard deviations:

  $`\displaystyle r = \rho = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y}`$

- **Range.** $`-1 \le r \le 1`$.
- **What $`r`$ tells you:**
  - **Sign:** the direction of the relationship (positive or negative).
  - **Magnitude:** the strength of the relationship. You can describe this as, for example, "moderate" or "highly correlated".
- **Independence vs. zero correlation:**
  - If $`X`$ and $`Y`$ are independent, then $`r = 0`$.
  - The converse does **not** hold. If $`r = 0`$, we **cannot** conclude that $`X`$ and $`Y`$ are independent.
  - The reason is that Pearson's $`r`$ only measures **linear** relationships. For nonlinear relationships, you need other measures.
- **Correlation matrix.** With many variables, a correlation matrix is a useful starting point for any analysis.

### 2.2 Spearman's rank correlation coefficient

**Setting.** $`n`$ individuals are ranked on two criteria. Examples:
- students ranked on mathematics marks and on science marks;
- two judges ranking contestants in a beauty pageant.

Let $`x_i`$ and $`y_i`$ be the ranks of the $`i`$-th individual under the two criteria. Each takes values $`1, 2, \dots, n`$.

**Purpose.** Measure whether the two sets of ranks agree:
- whether two judges "think alike";
- whether students who do well in maths also do well in science.

**Key insight.** Ranks are always the first $`n`$ natural numbers. With 10 people, the ranks are exactly $`1, 2, \dots, 10`$. This makes the means and variances of both series fixed and equal, which simplifies the formula.

#### Derivation (as done in class)

**Step 1: Mean of the ranks.** The sum of the first $`n`$ natural numbers is $`\sum_{i=1}^{n} i = \frac{n(n+1)}{2}`$. So

```math
\bar{x} = \bar{y} = \frac{1}{n}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2}
```

**Step 2: Variance of the ranks.** The sum of squares of the first $`n`$ natural numbers is $`\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}`$. Then

```math
\sigma_X^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2 = \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2
```

Take the common denominator 12 and simplify:

```math
\sigma_X^2 = \frac{(n+1)\left[2(2n+1) - 3(n+1)\right]}{12} = \frac{(n+1)(n-1)}{12}
```

So

```math
\sigma_X^2 = \sigma_Y^2 = \frac{n^2 - 1}{12}
```

**Step 3: Rank differences.** In general $`x_i \ne y_i`$, since two judges rarely agree on every individual. Define

```math
d_i = x_i - y_i
```

Because $`\bar{x} = \bar{y}`$, this can be rewritten as

```math
d_i = (x_i - \bar{x}) - (y_i - \bar{y})
```

- Summing the raw differences gives $`\sum d_i = 0`$ always. The instructor noted that this is a useful check that your arithmetic is on the right track.
- Because the raw differences cancel out, we **square** them.

**Step 4: Expand the sum of squared differences.**

```math
\sum d_i^2 = \sum (x_i - \bar{x})^2 + \sum (y_i - \bar{y})^2 - 2\sum (x_i - \bar{x})(y_i - \bar{y})
```

Divide both sides by $`n`$, and use $`\operatorname{Cov}(X,Y) = \rho\,\sigma_X\sigma_Y`$:

```math
\frac{1}{n}\sum d_i^2 = \sigma_X^2 + \sigma_Y^2 - 2\rho\,\sigma_X\sigma_Y
```

**Step 5: Simplify using equal variances.** Since $`\sigma_X = \sigma_Y`$:

```math
\frac{1}{n}\sum d_i^2 = 2\sigma_X^2 - 2\rho\,\sigma_X^2 = 2\sigma_X^2(1-\rho)
```

Rearranging:

```math
\rho = 1 - \frac{\sum d_i^2}{2n\sigma_X^2}
```

**Step 6: Substitute the variance.** Put $`\sigma_X^2 = \frac{n^2-1}{12}`$ into the expression. The 12 and the 2 cancel to leave 6.

> **Spearman's rank correlation coefficient:**
> $`\displaystyle \rho = 1 - \frac{6\sum_{i=1}^{n} d_i^2}{n(n^2-1)}`$

**Procedure:**
1. Compute the rank differences $`d_i`$.
2. Square them and sum.
3. Multiply by 6.
4. Divide by $`n(n^2-1)`$.
5. Subtract the result from 1.

#### Worked Example 1: Three judges, 10 contestants (Question 1 of the shared problem file)

- **Data.** Judges A, B and C each ranked 10 contestants. The full rank table was in the shared file and was not read aloud.
- **Goal.** Find which pair of judges thinks most alike. Compute $`\rho_{AB}`$, $`\rho_{AC}`$ and $`\rho_{BC}`$; the highest one indicates the most similar pair.
- **Steps:**
  1. For each pair, compute $`d_i`$: $`A - B`$, $`A - C`$ and $`B - C`$.
  2. Square the differences and sum them, giving $`\sum d_i^2`$ for each pair.
  3. Multiply each sum by 6.
  4. Denominator: $`n(n^2-1) = 10 \times (100 - 1) = 990`$.
  5. $`\rho = 1 - \frac{6\sum d_i^2}{990}`$.
- **Results (as quoted in class):** the three coefficients were about 0.21, 0.63 and 0.296.
  - For pair **A–C**, $`6\sum d_i^2 = 360`$:

    $`\displaystyle \rho_{AC} = 1 - \frac{360}{990} \approx 0.636`$

    This is positive and moderately high.
  - The pairs **A–B** and **B–C** came out **negative**, at roughly $`0.21`$ and $`0.30`$ in magnitude. The transcript does not say exactly which value belongs to which pair; check against the file.
- **Interpretation:**
  - Judges **A and C think more or less alike**: positive sign, coefficient about 0.63, moderately high.
  - **Judge B is something of an outlier.** B is negatively related to both A and C, so B ranks in a somewhat different direction. Those coefficients are not very large in magnitude.

**Student question.** "Why not just compute the ordinary (Pearson) correlation between columns A, B and C? I did it in Excel and got the same numbers."

- **Answer:** Spearman's $`\rho`$ *is* the Pearson correlation applied to ranks.
- When the data are untied ranks $`1, \dots, n`$, every column has the same mean and the same standard deviation. Pearson's formula on these ranks therefore reduces exactly to the Spearman formula.
- The instructor's caution: if you have actual continuous data (such as marks), compute Pearson on the raw data instead. Converting to ranks **loses information**.

#### Worked Example 2: Tied (repeated) ranks (Question 2)

**Rule for ties.** Give each tied value the **average** of the rank positions they would have occupied. Then **skip** those positions for the next value.

**Ranking series X** (values in descending order; the top value's mark was unclear in the audio):

| Value | Positions occupied | Rank assigned |
|---|---|---|
| highest value | 1 | 1 |
| 75, 75 | 2nd and 3rd | $`\frac{2+3}{2} = 2.5`$ each |
| 68 | 4th | 4 |
| 64, 64, 64 | 5th, 6th, 7th | $`\frac{5+6+7}{3} = \frac{18}{3} = 6`$ each |
| 55 | 8th | 8 |
| 50 | 9th | 9 |
| lowest value | 10th | 10 |

Rank 3 is skipped after the 2.5 tie, and ranks 5 and 7 are not used separately after the 6 tie.

**Ranking series Y:**

| Value | Rank assigned |
|---|---|
| 81 | 1 |
| 70 | 2 |
| 68, 68 | $`\frac{3+4}{2} = 3.5`$ each |

Ranking then continues at 5, 6, 7, 8, 9, 10 for the remaining values.

**Tie correction.** For each group of tied values, let $`m`$ be the number of times that value is repeated. Add a correction term to $`\sum d_i^2`$:

```math
\frac{m(m^2-1)}{12}
```

- **Series X** has two tie groups:
  - $`m = 2`$: $`\frac{2(2^2-1)}{12} = \frac{6}{12} = \frac{1}{2}`$
  - $`m = 3`$: $`\frac{3(3^2-1)}{12} = \frac{24}{12} = 2`$
  - Subtotal for X: $`\frac{5}{2}`$
- **Series Y** has one tie group:
  - $`m = 2`$: $`\frac{1}{2}`$
- **Total correction:** $`\frac{5}{2} + \frac{1}{2} = 3`$

> **Spearman's $`\rho`$ with tied ranks:**
> $`\displaystyle \rho = 1 - \frac{6\left[\sum d_i^2 + \sum \frac{m(m^2-1)}{12}\right]}{n(n^2-1)}`$
> The sum of corrections runs over every tie group in **both** series.

With ties, the plain formula is no longer exact. The derivation relied on the ranks being exactly $`1, \dots, n`$, which gave equal means and equal variances; ties disturb this, so the correction is needed. Even so, $`\sum d_i = 0`$ should still hold as a check.

#### Assumptions, properties and limitations

- **Pearson's $`r`$ (also called the Karl Pearson coefficient)** assumes that the parent population from which the sample is drawn is **normal**.
- **Spearman's $`\rho`$ is distribution-free (non-parametric).** It makes no assumption about the population distribution. It is easy to understand and easy to apply.
- **Interpretation** is the same as for Pearson's $`r`$: sign gives direction, magnitude gives strength, and the range is $`[-1, 1]`$.
- **When to use it.** Mainly for **qualitative** attributes that have been ranked, such as beauty, proficiency or judges' assessments.
- **Limitations:**
  - It becomes cumbersome to calculate when $`n > 30`$.
  - If you already have continuous data, **do not convert to ranks**. You lose information; use Pearson instead.

### 2.3 Partial correlation (concept only)

- Partial correlation is used when there are more than two variables.
- It measures the correlation between two variables **while holding a third constant**.
- Notation: $`r_{12.3}`$ is the correlation between $`X_1`$ and $`X_2`$ with $`X_3`$ held constant.
- Like Pearson's $`r`$, it captures **linear** relationships and assumes normality.
- The formula was not covered in class. For reference, the standard formula is:

  $`\displaystyle r_{12.3} = \frac{r_{12} - r_{13}\,r_{23}}{\sqrt{(1-r_{13}^2)(1-r_{23}^2)}}`$

- It is not very commonly used. Explore it further only if your own work needs it.

### 2.4 Multiple correlation

- This was announced as the third topic, "definition only", but the instructor did not elaborate before moving on to regression.

### 2.5 Introduction to regression

**Origin.**
- Introduced in the 19th century by **Sir Francis Galton**, a biometrician who worked with data on human heights and the inheritance of stature.

**Galton's finding.**
- The children of very tall parents, and of very short parents, tend to **regress**, or "step back", towards the **average height of the population**.
- Galton called this **"regression towards mediocrity"**. It is also known as **Galton's law of universal regression**.
- **Karl Pearson** later confirmed it.

**Illustration from class.**
- Father's height goes on the x-axis (5 ft 1 in, 5 ft 2 in, 5 ft 3 in, and so on); son's height goes on the y-axis.
- For each father-height group there is a spread of sons' heights.
- The line through the group averages is what will later be called the **regression line**.
- The sons of very tall fathers are, on average, less tall than their fathers.
- The sons of very short fathers are, on average, taller than their fathers.
- So both groups converge towards the population average.

**Regression in practice.**
- It is one of the most widely used tools in **econometrics** and data science.

**Deterministic vs. statistical relationships:**
- **Natural sciences** (for example, chemistry) can run controlled, repeatable experiments. The relationships they find are largely **deterministic**: doing A, B and C reliably leads to X, Y and Z.
- **Social sciences, economics and data science** usually cannot run such experiments. Variables are **random**: at best we assume they are normal, or they follow some other distribution. The relationships are therefore **statistical**, not deterministic.

**Example: crop yield.**
- This year an El Niño has led to an overall deficit of about 13% nationally (the transcript does not say a deficit of what; presumably rainfall), reaching as high as 20% in some places. Crop yields may therefore be low.
- Yield could be related to temperature, rainfall, sunshine, seed quality and other variables.
- Even with all possible data, an agro-economist would not get an exact relationship. There will always be **errors**.

**Sources of error in a statistical relationship:**
- omitted (missing) variables;
- the collective effect of, and interdependence among, the variables;
- intrinsic random variability.

Details of how regression handles these errors are deferred to the next class.

---

## 3. Exam and Assignment Notes

- **Problem file:** a question file has already been shared with the class.
  - **Question 1** is the three-judge problem (A, B, C; 10 contestants).
  - **Question 2** is the tied-ranks problem.
- **Submitted answers:**
  - Some students have already sent answers. The instructor will check the answer sheets and return them.
  - Answers will be reviewed on the last day if time permits. Otherwise, answers will be emailed; write to the instructor with any doubts.
- **Points likely to matter for exams and assignments:**
  - The Spearman formula, $`\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}`$, and its derivation using $`\bar{x} = \frac{n+1}{2}`$ and $`\sigma^2 = \frac{n^2-1}{12}`$.
  - The tie-handling procedure (average ranks, then skip positions) and the correction term $`\frac{m(m^2-1)}{12}`$.
  - The check that $`\sum d_i = 0`$.
  - The fact that zero correlation does **not** imply independence.
  - The difference between Pearson (assumes normality) and Spearman (distribution-free), and when to use each.
- **Schedule:** regression will be covered over the next 2 to 2.5 lectures, starting tomorrow.

<!-- nav -->
← [Session 37 (2026-11-11)](DSM-101-37_2026-11-11_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
