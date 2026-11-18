---
course: DSM 101
date: 2026-11-11
start: 7:00pm
session: "37"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) · [All lectures](./) · [Session 38 (2026-11-17)](DSM-101-38_2026-11-17_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 · Lecture 37 — Correlation Analysis (Pearson's $r$): Derivation, Properties, and Interpretation

**Instructor:** Ruchi Sharma | **Date:** 2026-11-11 | **Session file:** DSM-101-37_2026-11-11_Ruchi-Sharma

---

## 1. Overview

This session continues **bivariate correlation analysis** from the previous class. It first motivates and derives the **Karl Pearson correlation coefficient** $r$: the covariance of $X$ and $Y$, normalised by the product of their standard deviations. It then simplifies the formula into a computational "shortcut" form. The rest of the session covers the main properties of $r$:

- **Bounds:** $-1 \le r \le 1$, proved with the **Cauchy–Schwarz inequality**.
- **Sign vs. size:** the sign gives direction and the magnitude gives strength.
- **Invariance:** $r$ does not change under a change of origin and scale.
- **Independence vs. zero correlation:** independent variables are uncorrelated, but uncorrelated variables need not be independent. This is shown with a $y = x^2$ example, because $r$ only captures *linear* relationships.

The lecture also covers spurious ("nonsense") correlation and why correlation does not imply causation. It includes a hands-on Excel exercise (manual computation, `CORREL`, and a correlation matrix) and ends with a set of true/false interpretation statements.

---

## 2. Topics and Concepts (in order taught)

### 2.1 Recap: what correlation measures
- Correlation analysis is **bivariate**: it looks at two series/variables $X$ and $Y$.
- It measures the **association** between them, which can be **positive** (direct) or **negative** (inverse).
- The measure used is the **Pearson correlation coefficient**, denoted $r$.

### 2.2 Motivation for the formula
- **Numerator:** $r$ should capture how $X$ and $Y$ co-vary, so the **covariance** goes in the numerator.
- **Denominator:** each series has its own level of variability. To normalise, divide by the **standard deviations** $\sigma_X$ and $\sigma_Y$.
- The instructor's reason for doing the maths, even though software computes $r$: the derivation shows the **limits** of the measure, so you don't over-claim from results.

### 2.3 Definitions

**Covariance** (population form):
$$\operatorname{Cov}(X,Y) = E\big[(X - E[X])(Y - E[Y])\big]$$

Sample/data version, also written as the product moment $\mu_{11}$:
$$\operatorname{Cov}(X,Y) = \mu_{11} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

**Variances:**
$$\sigma_X^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2, \qquad \sigma_Y^2 = \frac{1}{n}\sum_{i=1}^{n}(y_i - \bar{y})^2$$

**Pearson correlation coefficient:**
$$r_{XY} = \frac{\operatorname{Cov}(X,Y)}{\sigma_X\,\sigma_Y} = \frac{\mu_{11}}{\sqrt{\mu_{20}}\sqrt{\mu_{02}}}$$

Written out in full:
$$r_{XY} = \frac{\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})^2 \cdot \dfrac{1}{n}\displaystyle\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

### 2.4 Shortcut (computational) forms

**Numerator.**
1. Expand the product inside the sum: $(x_i - \bar{x})(y_i - \bar{y}) = x_i y_i - x_i\bar{y} - \bar{x}y_i + \bar{x}\bar{y}$.
2. Apply $\frac{1}{n}\sum$ to each term. Since $\bar{x}$ and $\bar{y}$ are constants, they come out of the sums.
$$\frac{1}{n}\sum x_i y_i \;-\; \bar{y}\cdot\frac{1}{n}\sum x_i \;-\; \bar{x}\cdot\frac{1}{n}\sum y_i \;+\; \frac{1}{n}\cdot n\,\bar{x}\bar{y}$$
3. Use $\frac{1}{n}\sum x_i = \bar{x}$ and $\frac{1}{n}\sum y_i = \bar{y}$. The terms become $-\bar{x}\bar{y} - \bar{x}\bar{y} + \bar{x}\bar{y} = -\bar{x}\bar{y}$.

$$\boxed{\operatorname{Cov}(X,Y) = \frac{1}{n}\sum x_i y_i - \bar{x}\,\bar{y}}$$

In words: multiply the two series term by term, sum, divide by $n$, then subtract the product of the means.

**Denominator (variance).**
1. Expand with $(a-b)^2 = a^2 - 2ab + b^2$.
$$\sigma_X^2 = \frac{1}{n}\sum (x_i - \bar{x})^2 = \frac{1}{n}\sum x_i^2 - 2\bar{x}\cdot\frac{1}{n}\sum x_i + \frac{1}{n}\cdot n\bar{x}^2 = \frac{1}{n}\sum x_i^2 - 2\bar{x}^2 + \bar{x}^2$$

$$\boxed{\sigma_X^2 = \frac{1}{n}\sum x_i^2 - \bar{x}^2}, \qquad \boxed{\sigma_Y^2 = \frac{1}{n}\sum y_i^2 - \bar{y}^2}$$

**Combined shortcut form.** This is a standard textbook equivalent obtained by multiplying through by $n^2$; it was not written out in class.
$$r = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{\sqrt{n\sum x_i^2 - \left(\sum x_i\right)^2}\;\sqrt{n\sum y_i^2 - \left(\sum y_i\right)^2}}$$

### 2.5 Property 1 — Limits of $r$: $-1 \le r \le 1$ (the most important property)

**Proof using the Cauchy–Schwarz inequality.**

1. Define deviations $a_i = x_i - \bar{x}$ and $b_i = y_i - \bar{y}$.
2. The $\frac{1}{n}$ factors cancel, leaving
$$r = \frac{\sum a_i b_i}{\sqrt{\sum a_i^2 \sum b_i^2}} \quad\Rightarrow\quad r^2 = \frac{\left(\sum a_i b_i\right)^2}{\sum a_i^2 \sum b_i^2}$$
3. The **Cauchy–Schwarz inequality** states that for real numbers $a_i, b_i$, $i = 1, \dots, n$:
$$\left(\sum_{i=1}^{n} a_i b_i\right)^2 \le \left(\sum_{i=1}^{n} a_i^2\right)\left(\sum_{i=1}^{n} b_i^2\right)$$
4. **Equality** holds if and only if the ratios are all equal:
$$\frac{a_1}{b_1} = \frac{a_2}{b_2} = \cdots = \frac{a_n}{b_n} = \text{constant}$$
   This corresponds to a perfect linear relationship.
5. Therefore $r^2 \le 1$, so $|r| \le 1$, which gives
$$\boxed{-1 \le r \le 1}$$

**Practical check:** if anyone reports a correlation outside $[-1, 1]$ (the instructor's example was "the correlation is 98"), question the method, because something has gone wrong.

### 2.6 Sign vs. size of $r$

**Sign = direction.**
- $r > 0$ means a direct relationship: both variables move in the same direction.
  - Both *decreasing* together is still a **positive** correlation.
  - Example from the previous class: better health is associated with higher income.
- $r < 0$ means an inverse relationship: one variable increases while the other decreases.
  - Example: price of a product vs. quantity demanded.

**Size (magnitude) = strength.** Textbooks give indicative ranges, and these vary by author (some use 0.3 cut-offs, etc.):

| $\lvert r \rvert$ | Interpretation |
|---|---|
| $0$ – $0.25$ | (almost) no relationship |
| $0.25$ – $0.5$ | weak |
| $0.5$ – $0.75$ | moderate / moderately strong |
| $> 0.75$ | strong |
| $\approx 0.9$ – $0.98$ | near-perfect |

- In general, $|r| < 0.5$ indicates a relationship that is not very strong.
- In interpretation, always distinguish the information given by the **sign** from that given by the **size**.

### 2.7 Property 2 — $r$ is independent of change of origin and scale

**Setup.** Define new variables
$$u = \frac{x - a}{h}, \qquad v = \frac{y - b}{k}$$
so that $x = a + hu$ and $y = b + kv$.
- $a$ and $b$ are changes of **origin**.
- $h$ and $k$ are changes of **scale**.

**Claim:** $r_{XY} = r_{UV}$.

**Student's intuition (accepted by the instructor):** $x$ is a linear function of $u$ (slope $h$, intercept $a$), and $y$ is a linear function of $v$ (slope $k$, intercept $b$). So however $u$ and $v$ co-vary, $x$ and $y$ co-vary in the same way. Since $r$ works on deviations from means, the shifts and scalings cancel out.

**Proof.**

1. Expectations:
$$E[X] = a + hE[U], \qquad E[Y] = b + kE[V]$$
2. Deviations (the constants $a$ and $b$ cancel):
$$X - E[X] = h\,(U - E[U]), \qquad Y - E[Y] = k\,(V - E[V])$$
3. Numerator:
$$\operatorname{Cov}(X,Y) = E\big[h(U - E[U])\cdot k(V - E[V])\big] = hk\,\operatorname{Cov}(U,V)$$
4. Denominator:
$$\sigma_X^2 = E\big[h^2(U - E[U])^2\big] = h^2\sigma_U^2 \;\Rightarrow\; \sigma_X = h\,\sigma_U$$
$$\sigma_Y = k\,\sigma_V$$
5. Therefore:
$$r_{XY} = \frac{hk\,\operatorname{Cov}(U,V)}{hk\,\sigma_U\,\sigma_V} = r_{UV}$$

> *Note added for completeness (not stated in class):* strictly, $\sigma_X = |h|\,\sigma_U$. So $r_{XY} = r_{UV}$ when $h$ and $k$ have the same sign, and $r_{XY} = -r_{UV}$ if exactly one of them is negative. The magnitude is always preserved.

**Applied economics example (deflating series).**
- Suppose you want the correlation between **sales** and **raw-material** series, both measured at current prices (price × quantity).
- To focus on quantities, you deflate both series using a price index.
- If **both** series are divided by the **same** WPI (Wholesale Price Index; India is moving toward a Producer Price Index), $r$ does **not** change. This is just a change of scale.
- If you correctly use **different** deflators (a WPI for the final good for sales, and a WPI for raw materials/intermediate goods for the raw-material series), the results can change.
- Lesson: understand why you are rescaling, and whether it will affect your results.

### 2.8 Property 3 — Independence vs. zero correlation

**Independent ⇒ uncorrelated.** If $X$ and $Y$ are independent, then $\operatorname{Cov}(X,Y) = 0$, so $r = 0$.

**Uncorrelated does NOT imply independent.**

**Worked example.** The data values were not read aloud. The reconstruction below is consistent with the stated totals: $\sum x = 0$, $\sum xy = 0$, $\sum y = 28$, and $y = x^2$.

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $y = x^2$ | $9$ | $4$ | $1$ | $0$ | $1$ | $4$ | $9$ |

1. Column totals:
   - $\sum x_i = 0$, so $\bar{x} = 0$.
   - $\sum y_i = 28$, so $\bar{y} = 28/7 = 4$. The transcript says "$\bar{y}$ is 0", which looks like a slip; the result does not depend on it.
   - $\sum x_i y_i = \sum x_i^3 = 0$.
2. Numerator:
$$\frac{1}{n}\sum x_i y_i - \bar{x}\bar{y} = 0 - 0\cdot 4 = 0$$
3. Hence $r = 0$.

Yet $y$ is completely determined by $x$ ($y = x^2$), so the variables are clearly **not** independent.

**Key point:** Pearson's $r$ captures only **linear** relationships. Quadratic, cubic, and other non-linear relationships can give $r \approx 0$. If $r = 0$, you cannot conclude independence; probe further for non-linear structure.

### 2.9 Recap of Karl Pearson's assumptions (covered in the previous class)
1. The relationship between $X$ and $Y$ is **linear**.
2. Each variable is affected by a large number of independent contributory causes, so that it follows a **normal distribution**. Examples: height, weight, supply, prices.
3. The forces operating on each variable series are **not independent of each other**; they are related in some causal way. If they were independent, $r$ would be $0$.

### 2.10 Spurious / nonsense correlation
- A non-zero $r$ does **not** automatically mean a real relationship exists.
- Examples of chance or nonsense correlations: shoe size vs. intelligence; marriage rate vs. rainfall.
- Any data with variation can produce some $r$. You need an **a priori, theory-based reason** for linking two variables (a model or at least a logical argument) **before** computing $r$.

### 2.11 Excel exercise (practice file emailed in class)

**Manual computation steps:**
1. Compute the mean of each series.
2. Add columns for $x^2$, $y^2$, and $xy$, and sum them.
3. Compute the numerator as $\frac{1}{n}\sum xy - \bar{x}\bar{y}$.
4. Compute the standard deviations, either from $\sqrt{\frac{1}{n}\sum (x_i - \bar{x})^2}$ or with Excel's STDEV functions.
5. Divide the numerator by $\sigma_X \sigma_Y$.

**Result:** the instructor obtained $r \approx 0.918$, a strong positive correlation. Students' values may differ slightly depending on whether the last rows of data (1989–90) were copied.

**Cross-check:** use `=CORREL(range_x, range_y)`, for example `=CORREL(B3:B25, C3:C25)`. Make sure both ranges start at the same row.

**Correlation matrix.** For several series (A, B, C, D), compute all pairwise $r$ values before regression or other analysis.
- The diagonal entries are all $1$.
- It is a good first diagnostic.
- It reports only *simple* (pairwise) correlations. **Partial correlation** coefficients are calculated and interpreted differently.

### 2.12 Interpretation exercise: true/false statements

1. **"A high positive $r$ between newspaper sales and number of crimes means newspaper reading causes crime."**
   **False.** The computation may be fine, but the inference is wrong. This is a spurious/nonsense correlation.

2. **"A high positive $r$ between cigarette smoking and lung cancer *establishes* that smoking causes lung cancer."**
   **False as stated.** The problem is the word *"establishes"*: correlation does not imply causation. Correlation only shows a strong **association**. Causality has since been established by other, more elaborate techniques, not by $r$ alone.

3. **"$r = 0.8$ means 80% of the variation is explained."**
   **False.** $r$ measures the strength and direction of a linear association. Explained variation is measured by $r^2$, the coefficient of determination; for example, $r = 0.8$ gives $r^2 = 0.64$.

4. **"Closeness of relationship is proportional to $r$."** Example: if $r_{XY} = 0.8$ and $r_{XZ} = 0.4$, is the $X$–$Y$ relationship twice as strong as $X$–$Z$?
   **False.** $r$ is not on a ratio scale. You can only say $X$–$Y$ shows a *higher* association than $X$–$Z$.

---

## 3. Exam / Assignment Pointers

- **Practice questions** were emailed before class. Attempt them over the weekend; the next class is on **Monday**.
- **Most emphasised property:** $-1 \le r \le 1$, including the Cauchy–Schwarz proof and the equality condition. Any reported $|r| > 1$ indicates an error.
- **Sign vs. size:** be able to state clearly what each tells you. This was stressed for interpretation questions.
- **Invariance proof:** know the change of origin and scale proof, and the deflation (WPI) application.
- **Independent ⇒ uncorrelated, but not conversely.** Know the $y = x^2$ example and that $r$ captures only linear relationships.
- **Interpretation statements are likely question material:**
  - correlation $\neq$ causation;
  - spurious correlation;
  - $r$ vs. $r^2$;
  - $r$ is not proportional to closeness of relationship.
- **Excel skills:** manual computation of $r$, `CORREL`, and building a correlation matrix.

**Next lectures:** rank correlation (Spearman), partial correlation coefficient, then **regression**.

<!-- nav -->
← [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) · [All lectures](./) · [Session 38 (2026-11-17)](DSM-101-38_2026-11-17_Ruchi-Sharma.md) →
<!-- /nav -->
