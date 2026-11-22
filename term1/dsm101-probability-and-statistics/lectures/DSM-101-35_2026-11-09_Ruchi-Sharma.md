---
course: DSM 101
date: 2026-11-09
start: 7:00pm
session: "35"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 34 (2026-11-04)](DSM-101-34_2026-11-04_Ruchi-Sharma.md) · [All lectures](./) · [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 · Session 35: Continuous Random Variables (Uniform & Normal)
**Instructor:** Prof. Ruchi Sharma | **Date:** 2026-11-09

---

## 1. Overview

This session moves from **discrete** random variables (modelled with a probability mass function) to **continuous** random variables (modelled with a probability density function, PDF), where probabilities are **areas under a curve**. Two continuous distributions are covered. The first is the **uniform (rectangular) distribution**: its PDF, its CDF, the derivation of its mean and variance, and three worked examples (a $`U(0,10)`$ variable, a $`U(200,250)`$ variable with a percentile question, and a subway waiting-time problem). The second is the **normal (Gaussian) distribution**: its history (de Moivre, 1733, as a limiting case of the binomial; extended by Laplace via the Central Limit Theorem), its PDF, standardisation to the **standard normal variate** $`Z`$, its key properties, and how the mean and variance change the shape of the curve. The session ends with reading the **standard normal ($`Z`$) table**, worked through a midterm-score example.

---

## 2. Topics Covered (in order taught)

### 2.1 Discrete vs. continuous random variables
- **Discrete RV:** takes specific, countable values. It is described by a **probability mass function (PMF)**, $`P(X = x)`$.
- **Continuous RV:** can take **infinitely many values** within an interval. For example, between 3 and 4 it can take 3.1, 3.11, 3.111, … and so on up to 4.
  - Because of this, it cannot be modelled value-by-value as in the discrete case.
  - It is described by a curve $`f(x)`$, the **probability density function (PDF)**.
- **Probabilities are areas under the PDF curve.** That is why integrals are used:

```math
P(a \le X \le b) = \int_a^b f(x)\,dx
```
- The two conditions any valid PDF must satisfy:

```math
f(x) \ge 0 \quad \text{for all } x, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1
```
  The total area equals 1 because integrating over all possibilities captures the whole probability.

---

### 2.2 Uniform (rectangular) distribution

**Definition.** $`X`$ is uniformly distributed on the interval $`(\alpha, \beta)`$ (also written $`(a, b)`$) if its PDF is constant over that interval:

```math
f(x) = \begin{cases} \dfrac{1}{\beta - \alpha}, & \alpha < x < \beta \\[2mm] 0, & \text{otherwise} \end{cases}
```

- **Special case $`U(0,1)`$:** $`f(x) = 1`$ for $`0 < x < 1`$, and $`0`$ otherwise.
- **Why "rectangular":** the graph is a flat line at height $`\frac{1}{b-a}`$ between $`a`$ and $`b`$. That gives a rectangle of width $`(b-a)`$ and height $`\frac{1}{b-a}`$, so its area is $`1`$.

**Cumulative distribution function (CDF):**

```math
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt = \begin{cases} 0, & x < a \\[1mm] \dfrac{x - a}{b - a}, & a \le x \le b \\[2mm] 1, & x > b \end{cases}
```

- $`F(x)`$ has corners at $`x = a`$ and $`x = b`$, so it is **not differentiable** at those two points.
- Everywhere else, $`F'(x) = f(x)`$. This gives $`\frac{1}{b-a}`$ inside the interval and $`0`$ outside, which recovers the PDF.

#### Worked Example 1: $`X \sim U(0, 10)`$
Here $`f(x) = \frac{1}{10 - 0} = \frac{1}{10}`$ for $`0 < x < 10`$.

| Probability | Integral | Result |
|---|---|---|
| $`P(X < 3)`$ | $`\int_0^3 \frac{1}{10}\,dx = \frac{1}{10}(3 - 0)`$ | $`\frac{3}{10}`$ |
| $`P(X > 6)`$ | $`\int_6^{10} \frac{1}{10}\,dx = \frac{1}{10}(10 - 6)`$ | $`\frac{4}{10}`$ |
| $`P(3 < X < 8)`$ | $`\int_3^8 \frac{1}{10}\,dx = \frac{8}{10} - \frac{3}{10}`$ | $`\frac{5}{10} = \frac{1}{2}`$ |

- A student asked about $`P(X > 6)`$. The upper limit is the end of the support, **10** (not 8). So the integral is $`\int_6^{10}`$.
- Interpretation of the last row: there is a 50% chance that $`X`$ lies between 3 and 8.

#### Mean of the uniform distribution

```math
E[X] = \int_{-\infty}^{\infty} x f(x)\,dx = \int_\alpha^\beta \frac{x}{\beta - \alpha}\,dx = \frac{1}{\beta - \alpha}\cdot\frac{\beta^2 - \alpha^2}{2} = \frac{\beta + \alpha}{2}
```

- The mean is simply the **midpoint** of the interval.
- A student suggested a substitution leading to a logarithm. That approach is wrong: the denominator is the constant $`(\beta - \alpha)`$, not $`(\beta - x)`$. The integral is direct.

#### Variance of the uniform distribution
Use $`\mathrm{Var}(X) = E[X^2] - (E[X])^2`$.

**Step 1: compute $`E[X^2]`$.** Use the factorisation $`\beta^3 - \alpha^3 = (\beta - \alpha)(\beta^2 + \alpha\beta + \alpha^2)`$:

```math
E[X^2] = \int_\alpha^\beta \frac{x^2}{\beta - \alpha}\,dx = \frac{\beta^3 - \alpha^3}{3(\beta - \alpha)} = \frac{\beta^2 + \alpha\beta + \alpha^2}{3}
```

**Step 2: subtract the squared mean.**

```math
\mathrm{Var}(X) = \frac{\beta^2 + \alpha\beta + \alpha^2}{3} - \left(\frac{\alpha + \beta}{2}\right)^2 = \frac{(\beta - \alpha)^2}{12}
```

> **Summary:** $`E[X] = \dfrac{\alpha + \beta}{2}`$, $`\quad \mathrm{Var}(X) = \dfrac{(\beta - \alpha)^2}{12}`$

#### Worked Example 2: $`X \sim U(\alpha = 200, \beta = 250)`$
1. **PDF:** $`f(x) = \frac{1}{250 - 200} = \frac{1}{50}`$ for $`200 < x < 250`$.
2. **$`P(X > 230)`$:**

```math
P(X > 230) = \int_{230}^{250} \frac{1}{50}\,dx = \frac{20}{50} = \frac{2}{5}
```
3. **Percentile question:** set the CDF equal to the target proportion and solve, $`\frac{x - 200}{50} = p`$.
   - In class, the value $`0.8`$ was used: $`\frac{x - 200}{50} = 0.8`$, which gives $`x = 240`$. The class accepted **240** as the answer.
   - ⚠️ **Discrepancy:** $`0.8`$ corresponds to the **80th** percentile, but the question was stated as the **88th** percentile. For the 88th percentile, $`\frac{x - 200}{50} = 0.88`$, so $`x = 244`$. Check which value your instructor intends.

#### Worked Example 3: Subway waiting time
- **Setup:** between midnight and 6 a.m., trains come every 30 minutes. A person arrives at a random time (e.g., some time around 4–5 a.m.).
- **Question:** what is the probability that they wait **at least 20 minutes**?
- **Model:** the waiting time is $`X \sim U(0, 30)`$, so $`f(x) = \frac{1}{30}`$ for $`0 < x < 30`$, and $`0`$ otherwise.
- "At least 20 minutes" means $`X \ge 20`$:

```math
P(X \ge 20) = \int_{20}^{30} \frac{1}{30}\,dx = \frac{30 - 20}{30} = \frac{10}{30} = \frac{1}{3}
```

---

### 2.3 Normal (Gaussian) distribution

#### History and motivation
- First derived in **1733 by Abraham de Moivre**.
  - The slide said "English mathematician." A class check suggested French; he was French-born but worked in England.
- De Moivre obtained it as a **limiting case of the binomial distribution** as $`n`$ becomes large.
  - This connects to the earlier binomial example: as the gaps between the binomial bars narrow, the histogram approaches a smooth curve.
- **Contrast with the Poisson approximation:** for the Poisson, $`n`$ is large and $`p`$ is very small. For the normal approximation, $`n`$ is large but $`p`$ and $`q`$ are **not** small.
- It was later extended by **Laplace**, connected to the **Central Limit Theorem (CLT)**.
- Many real variables are approximately normal, for example height, weight, GDP, and various types of expenditure.
- The instructor stressed that this distribution is very important for most later analysis.

#### Definition
A random variable $`X`$ is normally distributed with parameters $`\mu`$ (the **mean**) and $`\sigma^2`$ (the **variance**) if its PDF is

```math
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \qquad -\infty < x < \infty
```

It is written as $`X \sim N(\mu, \sigma^2)`$.

#### Standard normal variate
To standardise $`X \sim N(\mu, \sigma^2)`$, compute

```math
Z = \frac{X - \mu}{\sigma}
```

Then $`E[Z] = 0`$ and $`\mathrm{Var}(Z) = 1`$, so $`Z \sim N(0, 1)`$. The PDF of $`Z`$ is

```math
\phi(z) = \frac{1}{\sqrt{2\pi}}\, e^{-z^2/2}
```

- A student (Nihal) asked whether the PDF has $`\frac{1}{\sqrt{2\pi\sigma^2}}`$ or just $`\frac{1}{\sqrt{2\pi}}`$.
- **Answer:** the $`\frac{1}{\sqrt{2\pi}}`$ form is for the **standard** normal only. The general normal has $`\frac{1}{\sigma\sqrt{2\pi}}`$.

#### Chief characteristics / properties of the normal curve
1. **Bell-shaped**, with its peak at $`x = \mu`$.
2. **Symmetric about $`x = \mu`$.** Consequently, mean = median = mode (they coincide).
3. **Values far from the mean are less likely.** As $`x`$ moves away from $`\mu`$ in either direction, $`f(x)`$ decreases.
4. **No part of the curve lies below the x-axis**, since $`f(x) \ge 0`$.
5. **Linear combinations stay normal.** A linear combination of **independent normal variates** is also a normal variate. This is used extensively later in **regression analysis**.
6. **The x-axis is an asymptote to the curve.** The curve approaches the x-axis but never meets it at any finite distance.
7. **Sum and difference of standard normals.** If $`X`$ and $`Y`$ are independent standard normal variates, $`X, Y \sim N(0,1)`$, then

```math
U = X + Y \sim N(0, 2), \qquad V = X - Y \sim N(0, 2)
```
   and $`U`$ and $`V`$ are **independent**. The instructor noted this is also important for regression.

- **Area properties** of the normal curve were deferred to a later class.

#### Effect of $`\mu`$ and $`\sigma^2`$ on the shape
- **Same mean, larger variance:** the curve is flatter and more spread out.
- **Same mean, smaller variance:** the curve is tall and narrow, with values concentrated around the mean.
- **Changing $`\mu`$** shifts the location of the curve along the x-axis.
- **Research illustration:** a student studied total factor productivity of "star" vs. "non-star" firms. The two distributions plotted as normal-like curves, with the star firms' curve shifted further right (higher mean).

---

### 2.4 Using the standard normal ($`Z`$) table
- The PDF is hard to integrate by hand, so probabilities are read from **standard normal tables**.
- The table used in class gives the **area to the left of $`z`$**, i.e. $`\Phi(z) = P(Z \le z)`$.
  - Rows give $`z`$ to one decimal place (e.g., 1.2).
  - Columns give the second decimal (e.g., 0.05).
- **Right-tail areas:** use symmetry or complements, $`P(Z > z) = 1 - \Phi(z)`$.
- **Negative $`z`$:** use $`\Phi(-z) = 1 - \Phi(z)`$.
- Some tables instead give the area from $`0`$ to $`z`$. In that case add $`0.5`$ for positive $`z`$ to get the left-tail area.

**General procedure:**
1. Compute $`z = \frac{x - \mu}{\sigma}`$.
2. Look up the area in the table.
3. Convert to the required area (left, right, or between).
4. Multiply by 100 for a percentage.

#### Worked Example 4: Midterm scores
**Given:** class mean $`\mu = 77`$, standard deviation $`\sigma = 8`$.

**(a) Rahul scored 87. What percentage scored below him?**

```math
z = \frac{87 - 77}{8} = \frac{10}{8} = 1.25
```
- Table lookup: row 1.2, column 0.05 gives $`\Phi(1.25) = 0.89435`$.
- Equivalently, $`0.5 + 0.39435`$, i.e. the left half plus the area from 0 to 1.25.
- **About 89.4%** of students scored below Rahul. In other words, Rahul beat about 89.4% of the class.

**(b) Raj scored 73. What percentage scored below Raj?**

```math
z = \frac{73 - 77}{8} = \frac{-4}{8} = -0.5
```
- $`\Phi(-0.5) = 1 - \Phi(0.5) = 1 - 0.69146 = 0.30854`$.
- **About 30.8%** scored below Raj.
- This area lies on the **left** side of the mean, a point clarified in Q&A.

**(c) What percentage scored between Raj and Rahul?**

```math
P(-0.5 < Z < 1.25) = 0.89435 - 0.30854 = 0.58581
```
- **About 58.6%** of students scored between Raj and Rahul.

---

## 3. Exam / Assignment Notes
- **The normal distribution is flagged as very important.** It will be used in most later analysis, and more questions on it will be done in class.
- **Know these formulas cold:**
  - The uniform PDF and CDF.
  - The derivation of the uniform mean $`\frac{\alpha + \beta}{2}`$ and variance $`\frac{(\beta - \alpha)^2}{12}`$.
  - The normal PDF.
  - Standardisation $`Z = \frac{X - \mu}{\sigma}`$.
- **Properties needed for regression later:**
  - Linear combinations of independent normals are normal.
  - $`X \pm Y \sim N(0, 2)`$ for independent standard normals.
- **Practice set:** the instructor will send a question set within a day or two. It includes continuous-distribution problems. Bring any doubts to the next class.
- **Next class:**
  - Step-by-step procedure for normal-table problems.
  - Resolving any doubts.
  - Area properties of the normal curve.
  - Wrapping up this topic before starting the next one.
- **Watch for the percentile discrepancy in Example 2:** 240 is the 80th percentile, while the 88th percentile is 244.

<!-- nav -->
← [Session 34 (2026-11-04)](DSM-101-34_2026-11-04_Ruchi-Sharma.md) · [All lectures](./) · [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) →
<!-- /nav -->
