---
course: DSM 101
date: 2026-11-19
start: 7:00pm
session: "40"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 39 (2026-11-18)](DSM-101-39_2026-11-18_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-101 · Lecture 40 — Simple Linear Regression: Estimation by OLS

**Session:** DSM-101-40 · 2026-11-19 · Instructor: Ruchi Sharma

---

## 1. Overview

This session completes the course's coverage of regression. It opens with a short recap of the previous class: Galton's "regression to mediocrity", how correlation differs from regression, the steps of an econometric analysis, and conditional expectation. It then covers a point skipped last time: what "linear" means in linear regression. The answer is that the model must be linear in the **parameters**, not necessarily in the variables.

The main part of the lecture distinguishes three things:

- the unobservable **population regression function (PRF)**,
- the **estimated (sample) regression function** that we actually observe,
- the related quantities: predicted values, errors and residuals.

From there, the **Ordinary Least Squares (OLS)** principle is motivated and stated: minimise the sum of squared residuals. The OLS estimators $`\hat\beta_0`$ and $`\hat\beta_1`$ are derived step by step from the first-order conditions and re-expressed as a ratio of sample covariance to sample variance. The lecture briefly extends the idea to multiple regression in matrix form. It closes with a numerical example (price vs. quantity demanded) giving $`\hat\beta_1 = -2.376`$, followed by logistics on the exam and assignment.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap of the previous class

**Galton's "regression to mediocrity"**
- Tall parents had children who were tall, but *on average less tall* than the parents.
- Short parents had children who were short, but *on average less short* than the parents.
- In both cases, outcomes "regress" toward the average.

**Correlation vs. regression.** The two were distinguished by:
- the role of the variables: correlation is symmetric, while regression separates a dependent variable from explanatory variables;
- range;
- purpose.

**Anatomy of econometric analysis.** The analysis proceeds sequentially:
1. Theoretical foundation
2. Mathematical model / hypothesis
3. Data
4. Estimation
5. Hypothesis testing
6. Forecasting / policy considerations

**Expectation vs. conditional expectation.** This was illustrated with consumption expenditure versus income.

### 2.2 What "linear" means in linear regression

The basic model is:

```math
Y_i = \beta_0 + \beta_1 X_i + u_i
```

**Key definition:** "Linear" refers to **linearity in the parameters** ($`\beta`$'s), *not necessarily in the variables* ($`X`$). A model linear in the $`\beta`$'s can be estimated with the same OLS tools, even if it is non-linear in $`X`$.

**Models that count as linear (linear in parameters):**

- Quadratic in $`X`$:

```math
E(Y \mid X) = \beta_0 + \beta_1 X^2
```

- Log–log model:

```math
\log Y_i = \beta_0 + \beta_1 \log X_i + u_i
```

- Shapes covered by such models include U-shaped, inverted-U, and S-shaped curves (e.g., cost curves in economics). These are non-linear in the variables but linear in the parameters, so they are still "linear regression".

**Models that are NOT linear (non-linear in parameters):** these require non-linear regression and are *not* covered by OLS in this course.

```math
E(Y \mid X) = \beta_0 + \beta_1^2 X
```

```math
E(Y \mid X) = \beta_0 + \sqrt{\beta_1}\, X
```

```math
E(Y \mid X) = \beta_0 \, e^{\beta_1 X}
```

### 2.3 Specification recap and the test-score example

The model is:

```math
Y_i = \beta_0 + \beta_1 X_i + u_i, \qquad i = 1, \dots, n
```

Previously covered material:
- data types: cross-section, time series, panel;
- dependent variable, independent variable, error term, intercept, slope.

**Worked example (from the previous class):**

```math
\widehat{\text{TestScore}} = 698.9 - 2.28 \times \text{STR}
```

Here STR is the student–teacher ratio.

- As students per teacher increase, test scores decline.
- The **sign** of a coefficient gives the **direction** of the relationship.
- The **magnitude** of a coefficient gives the **size** of the relationship.

### 2.4 Population regression function vs. estimated regression function

**Population regression function (PRF).** This is the true relationship:

```math
E(Y \mid X_i) = \beta_0 + \beta_1 X_i
```

- It is **unobserved**. We know it exists, but we never see it.

**Estimated (sample) regression function.** This is obtained from data:

```math
\hat Y_i = \hat\beta_0 + \hat\beta_1 X_i
```

- The hats denote *estimated* values of $`\beta_0`$ and $`\beta_1`$.
- The data are a **sample** drawn from the population.
- In practice, the estimated line is always what we actually observe and work with.
- The estimated line is generally **not equal** to the PRF. The goal is for it to be as close as possible.
- Later topics (in a research methods course) include **hypothesis testing** and **goodness of fit**.

The lecture used a sketch with two lines: blue for the true PRF and another for the estimated line. The axes were income ($`X`$) and consumption expenditure ($`Y`$).

**Three key quantities** (for a given $`X_i`$):

| Quantity | Definition | Based on |
|---|---|---|
| **Predicted (fitted) value** | $`\hat Y_i = \hat\beta_0 + \hat\beta_1 X_i`$ (plug $`X_i`$ into the estimated line) | Estimated regression function |
| **Error** | $`u_i = Y_i - (\beta_0 + \beta_1 X_i)`$ | True PRF (unobservable) |
| **Residual** | $`\hat u_i = Y_i - \hat Y_i`$ | Estimated regression function (observable) |

Two ways of writing the same observation:

```math
Y_i = \beta_0 + \beta_1 X_i + u_i \quad \text{(true)}
```

```math
Y_i = \hat\beta_0 + \hat\beta_1 X_i + \hat u_i = \hat Y_i + \hat u_i \quad \text{(estimated)}
```

In general, $`\hat\beta_0 \neq \beta_0`$, $`\hat\beta_1 \neq \beta_1`$ and $`\hat u_i \neq u_i`$. The objective is to make the estimates as close as possible to the true values.

### 2.5 The least squares principle: why we square

- We want the gap between the actual $`Y_i`$ and the fitted $`\hat Y_i`$ to be as small as possible. That is, we want to minimise the residuals $`\hat u_i`$.
- Residuals can lie **above** the line (positive) or **below** it (negative).
- **Problem with simply summing residuals:** positive and negative residuals **cancel each other out**, so $`\sum \hat u_i`$ is not a useful criterion.
- **Solution:** **square** the residuals and minimise their sum. This is where the name **"least squares"** comes from, hence **Ordinary Least Squares (OLS)**.

**Sum of squared residuals (SSR).** Using $`b_0, b_1`$ as candidate values:

```math
SSR(b_0, b_1) = \sum_{i=1}^{n} \hat u_i^2 = \sum_{i=1}^{n} \left(Y_i - b_0 - b_1 X_i\right)^2
```

The OLS estimators are the values of $`b_0, b_1`$ that **minimise SSR**.
- These values exist and are unique.
- They are easy to derive.
- They can be computed by computer or by hand for small samples.

### 2.6 Derivation of the OLS estimators

**Step 1: First-order condition with respect to $`\hat\beta_0`$**

```math
\frac{\partial SSR}{\partial \hat\beta_0} = -2 \sum_{i=1}^{n} \left(Y_i - \hat\beta_0 - \hat\beta_1 X_i\right) = 0
```

Divide by $`-2`$ (move the 2 to the other side) and expand the summation:

```math
\sum Y_i - n\hat\beta_0 - \hat\beta_1 \sum X_i = 0
```

```math
n\hat\beta_0 = \sum Y_i - \hat\beta_1 \sum X_i
```

Divide by $`n`$:

```math
\boxed{\hat\beta_0 = \bar Y - \hat\beta_1 \bar X}
```

The intercept is easy to compute once you have the slope: just take the means of the two series. The lecturer's example was crop yield across plots in about 200 districts as a function of seed variety or precipitation.

**Step 2: First-order condition with respect to $`\hat\beta_1`$**

```math
\frac{\partial SSR}{\partial \hat\beta_1} = -2 \sum_{i=1}^{n} X_i\left(Y_i - \hat\beta_0 - \hat\beta_1 X_i\right) = 0
```

Substitute $`\hat\beta_0 = \bar Y - \hat\beta_1 \bar X`$. The sign flips to a plus because of the minus in front of $`\hat\beta_0`$:

```math
\sum X_i\left(Y_i - \bar Y + \hat\beta_1 \bar X - \hat\beta_1 X_i\right) = 0
```

Multiply through by $`X_i`$ and split the sums:

```math
\sum X_i Y_i - \bar Y \sum X_i - \hat\beta_1 \left(\sum X_i^2 - \bar X \sum X_i\right) = 0
```

Use the result $`\sum X_i = n\bar X`$:

```math
\sum X_i Y_i - n\bar X \bar Y - \hat\beta_1\left(\sum X_i^2 - n\bar X^2\right) = 0
```

Solve for $`\hat\beta_1`$:

```math
\boxed{\hat\beta_1 = \frac{\sum X_i Y_i - n\bar X \bar Y}{\sum X_i^2 - n\bar X^2}}
```

**Step 3: Equivalent deviation-from-mean form.** Expanding shows that this is identical to:

```math
\boxed{\hat\beta_1 = \frac{\sum_{i=1}^{n}(X_i - \bar X)(Y_i - \bar Y)}{\sum_{i=1}^{n}(X_i - \bar X)^2}}
```

**Interpretation.**
- The numerator is (proportional to) the **sample covariance** of $`X`$ and $`Y`$.
- The denominator is (proportional to) the **sample variance** of $`X`$.
- Any $`\frac{1}{n-1}`$ factors cancel, so:

```math
\hat\beta_1 = \frac{\widehat{\operatorname{Cov}}(X, Y)}{\widehat{\operatorname{Var}}(X)}
```

Both estimators are built entirely from **deviations from the mean**. The lecturer linked this back to Galton's idea of regression toward the average.

**Summary of OLS estimators (simple regression):**

```math
\hat\beta_0 = \bar Y - \hat\beta_1 \bar X
```

```math
\hat\beta_1 = \frac{\sum X_i Y_i - n\bar X\bar Y}{\sum X_i^2 - n\bar X^2} = \frac{\sum (X_i - \bar X)(Y_i - \bar Y)}{\sum (X_i - \bar X)^2}
```

In practice, these are computed with R, Stata, or Excel. The point of the derivation is to understand *why* the method is called least squares and where the formulas come from.

### 2.7 Extension: multiple regression (brief)

The model with $`k`$ regressors is:

```math
Y_i = \beta_0 + \beta_1 X_{1i} + \beta_2 X_{2i} + \cdots + \beta_k X_{ki} + u_i
```

- The same objective applies: minimise SSR.
- The solution uses matrix algebra. As the lecturer recalled it:

```math
\hat{\boldsymbol\beta} = (X'X)^{-1} X'Y
```

- The underlying idea is unchanged: OLS chooses coefficients that minimise the squared deviations.

### 2.8 Worked example: price vs. quantity demanded (Excel)

**Setup**
- There were six data points on price ($`P`$) and quantity demanded ($`Q`$). They are also in the course Excel sheet.
- Prices were read out partly as 40, 35, 30, 30, 20, … The full table was not captured clearly in the audio, so check the Excel sheet.
- True model, which is unobservable:

```math
Q_i = \beta_0 + \beta_1 P_i + u_i
```

- The six observations are a sample from the population. We expect a downward-sloping demand line.

**Procedure** (using the deviation form):
1. Compute $`\bar P`$ and $`\bar Q`$.
2. For each observation, compute $`(P_i - \bar P)`$ and $`(Q_i - \bar Q)`$.
3. Compute the product $`(P_i - \bar P)(Q_i - \bar Q)`$ and sum it. This is the covariance term, cell F9 in the sheet.
4. Compute $`(P_i - \bar P)^2`$ and sum it. This is the variance term, cell G9 in the sheet.
5. Compute the slope as the ratio of the two sums:

```math
\hat\beta_1 = \frac{\sum (P_i - \bar P)(Q_i - \bar Q)}{\sum (P_i - \bar P)^2} = \frac{F9}{G9} = -2.376
```

6. Compute the intercept:

```math
\hat\beta_0 = \bar Q - \hat\beta_1 \bar P
```

**Interpretation:** A one-unit increase in price reduces quantity demanded by about 2.376 units.

---

## 3. Exam / Assignment Notes

- **Exam on 23 November.** The exam period ends on 28 November.
- **Practice exercise:** The class chose to receive answers rather than go through them in class. The instructor will email the answers along with all lecture material (PPT made from her notes plus handwritten notes).
- **Assignment:**
  - It will be sent by Saturday.
  - It is due after the exams, around **3–4 December**, so as not to add stress before the exam.
- **Likely examinable**, given the emphasis in class:
  - the definition of linearity in parameters vs. variables, with examples of linear and non-linear models;
  - the distinction between PRF and estimated regression function, and between error and residual;
  - why residuals are squared;
  - the full derivation of $`\hat\beta_0`$ and $`\hat\beta_1`$ from the first-order conditions;
  - the covariance/variance form of $`\hat\beta_1`$;
  - computing $`\hat\beta_1`$ and $`\hat\beta_0`$ from a small dataset, as in the price–quantity example.

<!-- nav -->
← [Session 39 (2026-11-18)](DSM-101-39_2026-11-18_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
