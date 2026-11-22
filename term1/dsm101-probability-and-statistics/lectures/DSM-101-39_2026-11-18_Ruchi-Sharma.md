---
course: DSM 101
date: 2026-11-18
start: 7:00pm
session: "39"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 38 (2026-11-17)](DSM-101-38_2026-11-17_Ruchi-Sharma.md) · [All lectures](./) · [Session 40 (2026-11-19)](DSM-101-40_2026-11-19_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 (Probability & Statistics), Session 39: Introduction to Regression Analysis

*Session file: DSM-101-39_2026-11-18_Ruchi-Sharma*

---

## 1. Overview

This session moved from correlation to **regression analysis**. It began with a recap of the historical idea of "regression to mediocrity" and of statistical (as opposed to deterministic) relationships. It then covered:

- the vocabulary for the variables on each side of a regression equation;
- how research moves from a concept to operationalised, proxied variables;
- the overall "anatomy" of an econometric modelling exercise (theory → model → data → hypothesis testing → prediction/policy);
- a systematic comparison of correlation and regression;
- why the measurement scale of the dependent variable and the data structure (cross-section, time series, panel) matter for choosing models and tests.

The core technical content was **conditional expectation** $`E[Y \mid X]`$, shown with an income–consumption table, and the **population regression function (PRF)** $`Y_i = \beta_0 + \beta_1 X_i + u_i`$. The role of the error term was discussed in detail. The session ended with interpreting an estimated regression of test scores on the student–teacher ratio. The *estimation* of $`\beta_0`$ and $`\beta_1`$ is deferred to the next class.

---

## 2. Topics Covered (in teaching order)

### 2.1 Recap: Regression to mediocrity
- This is the origin of the term "regression" (the classic father–son height study, usually attributed to Galton).
- Sons' heights tend toward the overall average of the group:
  - The average height of sons of **short** fathers was **greater** than their fathers' height.
  - The average height of sons of **tall** fathers was **less** than their fathers' height.

### 2.2 Recap: Statistical vs. deterministic relationships
- **Example (agro-economist):** crop yield depends on temperature, rainfall, soil quality, and so on.
- Even with many variables, we cannot explain *all* the variation in yields. The relationship is **statistical**, not deterministic.

### 2.3 Variables in regression: dependent vs. independent
- In **correlation** the two variables $`X`$ and $`Y`$ have no labels. We only measure their association.
- In **regression** there is a notion of *dependence*. The dependent variable goes on the left-hand side (LHS) and the independent variables on the right-hand side (RHS).
- Crop yield example:

```math
\text{Yield} = f(\text{Temperature}, \text{Rainfall}, \text{Soil quality}, \dots)
```

- **Caution on causality:** some people read regression as causal (the independent variables "cause" the dependent one). Modern practice is careful about this. Once we see how the coefficients are derived, it becomes clear that regression captures **conditional association / conditional expectation**, not causation. Causality requires much more than explaining variation in one variable with another.

**Alternative names for the two sides of the equation:**

| LHS ($`Y`$) | RHS ($`X`$) |
|---|---|
| Dependent variable | Independent variable |
| Explained variable | Explanatory variable |
| Endogenous | Exogenous |
| Predicted | Predictor |
| Regressand | Regressor |
| Response | Stimulus |
| Outcome | Covariate |

### 2.4 Motivating examples
- **Sales:** take sales of *all* firms in an industry (e.g., automobiles), $`\text{Sales}_i`$. Relate them to raw materials, energy and fuel use, component inputs, and possibly managerial efficiency (a new variable you add because you think it matters).
- **Firm performance:**

```math
\text{Performance} = f(\text{Innovation}, \text{Manager's experience}, \text{Global exposure})
```

  "Global exposure" is a broader idea than exporting alone.

### 2.5 From concept to operationalisation to proxy
- **Conceptual level:** state the relationship in terms of ideas (e.g., performance depends on innovation, experience, global exposure).
- **Operationalisation:** decide how each concept will actually be measured with data.
  - *Performance* could be measured by profit before tax, beta, market capitalisation, or return on assets (ROA).
    - Each indicator captures some aspects of performance and misses others. You can use several indicators.
    - You must state your assumptions and what information each choice emphasises (e.g., market cap vs. ROA).
  - *Innovation* could be measured by new products introduced, R&D expenditure (from the balance sheet), patents (the outcome of R&D), or total factor productivity (TFP: how productively the firm uses all its resources).
  - *Managerial experience* could be measured by the promoter's or manager's background and years of experience.
  - *Global exposure* could be measured by exports and/or imports.
- **Proxy:** a measurable variable that stands in for a broad concept. For example, innovation is proxied by R&D expenditure, patents, new products, or TFP. A key question is always *how good the proxy is* as an indicator of the underlying concept.

### 2.6 Anatomy of econometric modelling
1. **Theory:** review the literature and research papers to identify the relationship. Possibly build a mathematical model (not always done).
2. **Econometric model:** write the testable equation, e.g., Performance $`= f(\cdot)`$, Sales $`= f(\cdot)`$, Yield $`= f(\cdot)`$.
3. **Data:** collect data, choose the relevant variables, and operationalise and proxy them (some information will not be available).
4. **Hypothesis testing:** we usually have a *sample*, not the population. Even a large sample has challenges. We test how well sample results represent the **population relationship** (population regression vs. sample regression). This covers how to build and check hypotheses and what distributional assumptions to make.
5. **Prediction / policy implications / recommendations:** e.g., having estimated the model on 100 firms in period $`t`$, predict firm performance next year.

**Advice:** avoid pure "data mining" (throwing variables together to see what correlates). Good work starts from theory, a model if possible, and stated hypotheses.

**Estimation vs. inference:**
- *Estimation* means obtaining the regression coefficients. This is done in this course.
- *Inference* means hypothesis testing and confidence intervals for the coefficients. This is done in the Research Methods course in the 3rd trimester, taught by the same instructor.

### 2.7 Correlation vs. regression

| Aspect | Correlation | Regression |
|---|---|---|
| **Purpose** | Measures the **degree and direction of the linear relationship**. Degree comes from the size of the coefficient, direction from its sign. | Estimates the **average relationship**, so that one variable can be predicted from another. |
| **Variables** | No dependent/independent labels. | Labelled: $`Y`$ is dependent and $`X`$ is independent. The labelling comes from theory or prior studies. |
| **Output** | A single coefficient $`r`$. | An **equation**, simple or multiple (see below). |
| **Range** | $`-1 \le r \le 1`$ | No fixed range. Depends on the units of $`Y`$. |
| **Units** | Unit-less, a pure number, because $`r = \dfrac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}`$. | Expressed in units of $`Y`$, e.g., whether $`Y`$ is logged or not. |
| **Causality** | Says nothing about cause. | Also not causal, but it tells the expected change in $`Y`$ for a change in $`X`$ (conditional association: "$`X`$ explains part of $`Y`$"). |
| **Prediction** | Cannot predict. | Can predict the dependent variable to some extent. |

Example regression equations:
- Market capitalisation on R&D expenditure:

```math
\text{MarketCap}_i = \alpha_0 + \alpha_1 \, \text{R\&D}_i + u_i
```

  The coefficient $`\alpha_1`$ tells how market cap changes when R&D changes (e.g., by 1%, depending on how the variables are measured, such as in logs).
- Simple regression output:

```math
Y = \beta_0 + \beta_1 X
```

- Multiple regression output:

```math
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots
```

### 2.8 Measurement scales (recap, class examples)

| Scale | Ratio meaningful? | Distance meaningful? | Natural ordering? | Class examples |
|---|---|---|---|---|
| Nominal | No | No | No | Gender (male/female), blood type |
| Ordinal | No | No | Yes | Poor/average/good; education level (high school, bachelor's, …) |
| Interval | No | Yes | Yes | IQ |
| Ratio | Yes | Yes | Yes | Market capitalisation, GDP (per capita), return on assets, sales |

**Why it matters:** the choice of regression model depends on the **measurement scale of the dependent variable**. The model for a nominal $`Y`$ is not the same as for a ratio-scale $`Y`$, because the distribution differs. The course focuses on the general case of a **ratio-scale** dependent variable.

### 2.9 Types of data (for ratio-scale variables)
- **Cross-section:** many units at one point in time. Example: sales of 100 firms in 2025.
  - Typical problem: **heteroscedasticity**, arising from heterogeneity across units.
- **Time series:** one unit over many periods. Examples: one company from 1962 to 2025; India's GDP per capita over 30–40 years.
  - Typical problems: **(non-)stationarity**, and shocks over time.
- **Pooled / panel data:** the two combined. A **panel** follows the *same* cross-section over time, e.g., the same 100 companies for 20 years.
  - A panel can show the problems of both cross-section and time-series data.
- **Why it matters:** each data type poses different problems. You must run the corresponding diagnostic tests and use appropriate methods for **both estimation and inference**.

### 2.10 Conditional expectation: the income–consumption example
- Cross-section of families: $`X`$ is monthly family income and $`Y`$ is consumption expenditure.
  - Income levels are $`X = 80, 100, 120, 140, 160, \dots, 260`$, where 80 means ₹80,000 per month. Income is treated as continuous, so intermediate values can exist.
- Several families share each income level but spend different amounts. The numbers below are illustrative and only partly audible in the recording:
  - **Income 80:** expenditures around 55, 60, 65, 70, 75. The column total is about 325, so the mean is about 65.
  - **Income 100:** expenditures around 65, 70, 75, 80, 85, 90. The total is about 462–465, so the mean is about 77.
- **Conditional expected value:** the mean of $`Y`$ for a given value of the conditioning variable $`X`$.

```math
E[Y \mid X = 80] \approx 65, \qquad E[Y \mid X = 100] \approx 77
```

- Each conditional mean also has a conditional variance around it.
- **Unconditional expectation** $`E[Y]`$: the average of *all* consumption values, ignoring income.
- Regression is interested in $`E[Y \mid X]`$, not $`E[Y]`$.
- On a scatter plot of income ($`X`$-axis) against consumption ($`Y`$-axis), higher income goes with higher expenditure. The conditional means trace out the relationship we want to model.

### 2.11 Population regression function (PRF)

```math
Y_i = \beta_0 + \beta_1 X_i + u_i, \qquad i = 1, 2, \dots, n
```

- $`i`$ indexes the $`i`$-th unit (firm or household). There are $`n`$ observations on both $`X`$ and $`Y`$.
- $`Y_i`$ is the dependent variable and $`X_i`$ the independent variable.
- $`\beta_0`$ is the **intercept**.
- $`\beta_1`$ is the **slope**, i.e., the regression coefficient.
- $`u_i`$ is the **error term** (written $`\mu_i`$ in the transcript). It plays a very important role:
  - It captures **all factors that explain $`Y_i`$ over and above $`X_i`$**. For example, if only one of the crop-yield variables is included, the others go into $`u_i`$.
  - It also absorbs measurement and proxy problems. For example, R&D expenditure used as a proxy for new products does not guarantee a product was launched, so the gap goes into $`u_i`$.
  - It also absorbs **model specification errors**.
- **Main interest:** the *expected effect on $`Y`$ of a unit change in $`X`$*. Examples:
  - income up by one unit → change in consumption;
  - managerial experience up by one year → change in market cap;
  - rainfall up by one unit → change in crop yield.
  - This is often called a "causal effect", but more precisely it is a **conditional expectation / association**.
- For consumption on income:

```math
\text{Consumption}_i = \beta_0 + \beta_1 \text{Income}_i + u_i
```

```math
\beta_1 = \frac{d\,\text{Consumption}}{d\,\text{Income}}
```

  So $`\beta_1`$ is the slope of the PRF: the change in consumption for a one-unit change in income.
- $`\beta_0`$ and $`\beta_1`$ are **unobserved population parameters**. The goals are:
  1. **Estimation** of $`\beta_0`$ and $`\beta_1`$, i.e., fitting a line through the scatter (how to fit it, and how good the fit is).
  2. **Inference** about $`\beta_0`$ and $`\beta_1`$: hypothesis tests (e.g., is $`\beta_1 = 0`$?) and confidence intervals built using the normal distribution.
- The focus is usually on $`\beta_1`$, the coefficient of the key independent variable.

### 2.12 Worked example: test scores and student–teacher ratio
- **Data:** districts in India (government schools). $`X`$ is the student–teacher ratio (STR) and $`Y`$ is the average Class 10 test score. The scatter slopes downward.
- **Estimated regression line (sample estimate of the PRF):**

```math
\widehat{\text{TestScore}} = 698.9 - 2.28 \times \text{STR}
```

  so $`\hat\beta_0 = 698.9`$ and $`\hat\beta_1 = -2.28`$.
- **Slope interpretation:**

```math
\frac{d\,\text{TestScore}}{d\,\text{STR}} = -2.28
```

  - A district with **one more student per teacher** has average test scores about **2.28 points lower**. (The lecturer also said "2.1" and "2.2" aloud; the coefficient on the board was $`-2.28`$.)
  - The sign gives the direction (negative) and the magnitude gives the size, just as in correlation.
  - Intuition: more students per teacher means more burden on the teacher and lower scores. The education literature debates ideal ratios of about 25–30.
- **Intercept interpretation:**
  - Literally, a district with STR $`= 0`$ would have a predicted score of 698.9.
  - This has **no economic meaning** here. It only **extrapolates the fitted line outside the range of the data**.
  - The constant is included to pin down where the line sits. In some other models it may have a meaningful interpretation.

---

## 3. Exam / Assignment Pointers and Admin

- ⚠️ **"Please mark this":** the **measurement scale of the dependent variable determines the appropriate regression model**, because the distribution differs. The course focuses on ratio-scale $`Y`$.
- Be able to state the **differences between correlation and regression**: purpose, variable labels, output, range, units, causality, prediction.
- Know the **PRF** $`Y_i = \beta_0 + \beta_1 X_i + u_i`$, the meaning of each term, and especially **what the error term captures**: omitted factors, poor proxies, specification error.
- Know the difference between **conditional** $`E[Y \mid X]`$ and **unconditional** $`E[Y]`$ expectation.
- Be able to interpret slope and intercept, as in the STR example: $`\hat\beta_1 = -2.28`$, $`\hat\beta_0 = 698.9`$, and why the intercept may lack economic meaning.
- Regression shows **conditional association, not causation**.
- Know the data types and their typical problems: cross-section → heteroscedasticity; time series → stationarity; panel → both.
- Hypothesis testing and confidence intervals will be covered in **Research Methods (3rd trimester)**. This course covers **estimation**.
- **Next class:** estimating $`\beta_0`$ and $`\beta_1`$, which completes the regression topic. The class is scheduled at **8:15**; the lecturer also posted a note in the chat.

<!-- nav -->
← [Session 38 (2026-11-17)](DSM-101-38_2026-11-17_Ruchi-Sharma.md) · [All lectures](./) · [Session 40 (2026-11-19)](DSM-101-40_2026-11-19_Ruchi-Sharma.md) →
<!-- /nav -->
