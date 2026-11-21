---
course: DSM 101
date: 2026-11-04
start: 7:00pm
session: "34"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 33 (2026-11-03)](DSM-101-33_2026-11-03_Ruchi-Sharma.md) · [All lectures](./) · [Session 35 (2026-11-09)](DSM-101-35_2026-11-09_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 Probability & Statistics: Session 34 Study Notes

**Session file:** DSM-101-34_2026-11-04_Ruchi-Sharma
**Topic:** Discrete distributions, continued (Geometric, Negative Binomial, Hypergeometric) and a summary of all discrete random variables covered so far.

> **Note on the transcript:** The ASR has several errors, such as "9 choose 1" for $`\binom{19}{1}`$, "0.6" for $`0.3`$, and "1 by B" for $`1/p`$. These notes correct them. Where the instructor did not finish a calculation in class, the notes give the computed value and mark it *(computed for these notes)* so you can tell it apart from what was said.

---

## 1. Overview

This session finished the unit on discrete random variables. It began with a worked **geometric distribution** example: the first CPR-trained person is the 6th person sampled. That example covered the PMF, mean, variance, an Excel table of the PMF, and the CDF $`F(x) = 1-(1-p)^x`$. The session then introduced the **negative binomial distribution**, which generalises the geometric to "the $`r`$-th success occurs on the $`n`$-th trial." It was compared with the binomial and worked through basketball and telephone-survey examples. Next came the **hypergeometric distribution**, the first distribution in the course based on sampling **without replacement**, with doctors/nurses and used-components examples. The lecture closed with a recap of all six discrete random variables (Bernoulli, Binomial, Poisson, Geometric, Negative Binomial, Hypergeometric) and their PMFs, means and variances. It also briefly revisited a tagged-fish question from a previous class using the hypergeometric model.

---

## 2. Topics Covered (in order taught)

### 2.1 Geometric Distribution: CPR Example

**Setup:** In a large population, 30% of adults are trained in CPR. Adults are sampled at random, one at a time, and each draw is independent.

- **Random variable:** $`X`$ = the number of the person sampled who is the **first** one with CPR training.
- **Parameters:** success probability $`p = 0.3`$, failure probability $`q = 1-p = 0.7`$.

**Question:** What is the probability that the 6th person sampled is the first with CPR training?

For this to happen, the first 5 people must be failures (untrained) and the 6th must be a success:

```math
P(X = 6) = (0.7)^5 \times (0.3)^1 = 0.16807 \times 0.3 \approx 0.0504
```

**General geometric PMF:**

```math
P(X = x) = (1-p)^{x-1}\,p, \qquad x = 1, 2, 3, \dots
```

**Mean and variance** (recalled from the previous class):

```math
E[X] = \frac{1}{p}, \qquad \mathrm{Var}(X) = \frac{1-p}{p^2}
```

- The intuition given in class: for a fair die, $`P(\text{a particular face}) = 1/6`$, so on average you need 6 rolls to get one success.
- For the CPR example:
  - $`E[X] = 1/0.3 \approx 3.33`$
  - $`\mathrm{Var}(X) = 0.7/0.09 \approx 7.78`$ (the instructor said "around 7.7")

**Excel exercise:**
- Tabulate $`P(X=x)`$ for $`x = 1, 2, \dots, 10`$ (or 11).
- The instructor corrected her own sheet: the PMF must start at $`x = 1`$, not $`x = 0`$, because the first success cannot occur on trial zero.
- **Shape:** the distribution is strongly **right-skewed**.

**Modified question:** What is the probability that the first CPR-trained person occurs on or before the 3rd person sampled?

There are two ways to solve it:

1. **Add the PMF values:**

```math
P(X \le 3) = P(X=1) + P(X=2) + P(X=3)
```
2. **Use the complement:**

```math
P(X \le 3) = 1 - P(X > 3) = 1 - \big[P(X=4) + P(X=5) + \cdots\big]
```

**CDF of the geometric distribution:** it has a simple closed form.

```math
F(x) = P(X \le x) = 1 - (1-p)^x
```

This works because $`P(X > x) = (1-p)^x`$, which is the probability that the first $`x`$ trials are all failures.

For the CPR example: $`P(X \le 3) = 1 - 0.7^3 = 1 - 0.343 = 0.657`$ *(computed for these notes)*.

---

### 2.2 Negative Binomial Distribution (NBD)

**Motivating example:** A coin is tossed repeatedly. What is the probability that the 6th head appears on the 15th toss?

**How the NBD relates to the distributions already covered:**

| Distribution | What is random | What is fixed |
|---|---|---|
| **Binomial** | Number of successes | Number of trials $`n`$ |
| **Geometric** | Number of trials needed to get the **1st** success | 1 success |
| **Negative Binomial** | Number of trials needed to get the **$`r`$-th** success | Number of successes $`r`$ |

- The NBD **generalises the geometric**: the geometric is the NBD with $`r = 1`$.
- All three are built on **independent Bernoulli trials**. Each trial is either a success or a failure (mutually exclusive), and $`p`$ stays constant across trials.

**Where the name comes from:** The instructor said a long proof exists showing that the NBD's PMF can be written using binomial coefficients with a negative exponent, which is why it is called the "negative" binomial. The proof was not covered.

**Student question:** If the binomial $`n`$ is unknown and you solve the binomial formula for $`n`$, is that the NBD?

**Answer (paraphrased):** No. The NBD is a distribution over the trial number at which the $`r`$-th success occurs. It is not "the binomial with $`n`$ unknown." The NBD also has the extra condition that the last trial must be a success.

**Derivation of the PMF:** "The $`r`$-th success occurs on trial $`n`$" means two things must both happen:

1. The first $`n-1`$ trials contain exactly $`r-1`$ successes. This is a binomial probability:

```math
\binom{n-1}{r-1}\,p^{\,r-1}\,(1-p)^{(n-1)-(r-1)}
```
2. The $`n`$-th trial is a success, which contributes one more factor of $`p`$.

Multiplying these together gives:

```math
\boxed{P(X = n) = \binom{n-1}{r-1}\,p^{\,r}\,(1-p)^{\,n-r}, \qquad n = r, r+1, r+2, \dots}
```

**Mean and variance:**

```math
E[X] = \frac{r}{p}, \qquad \mathrm{Var}(X) = \frac{r(1-p)}{p^2}
```

Compare with the geometric's $`1/p`$ and $`(1-p)/p^2`$: both are simply multiplied by $`r`$.

#### Worked Example 1: Basketball player

**Setup:** A player makes a basket with $`p = 0.7`$ and misses with probability $`0.3`$.

**Question:** What is the probability that her 6th successful basket comes on her 7th shot? Here $`r = 6`$ and $`n = 7`$.

- **What must happen:** the first 6 shots must contain **exactly** 5 successes (the transcript says "at least five", but it must be exactly 5). The 7th shot must then be a success.
- **Exponent check:** there was some confusion in class about the exponent on $`0.3`$. It is $`n - r = 7 - 6 = 1`$, which is the same as $`(n-1)-(r-1) = 6 - 5 = 1`$.

```math
P(X=7) = \binom{6}{5}(0.7)^6(0.3)^1 = 6 \times 0.117649 \times 0.3 \approx 0.2118 \quad \text{(computed for these notes)}
```

#### Worked Example 2: Telephone survey

**Setup:** A surveyor must get 3 completed surveys before stopping for the day. Each call completes a survey with probability $`p = 0.09`$ (9%).

**Question:** What is the probability that the 3rd completed survey occurs on the 10th call? Here $`r = 3`$ and $`n = 10`$.

1. Write out the formula:

```math
P(X=10) = \binom{10-1}{3-1}(0.09)^{3}(1-0.09)^{10-3} = \binom{9}{2}(0.09)^3(0.91)^7
```
2. Where the pieces come from: the 9 earlier calls give $`(0.09)^2 (0.91)^7`$, and multiplying by the successful 10th call turns $`(0.09)^2`$ into $`(0.09)^3`$.
3. Evaluate:

```math
= 36 \times 0.000729 \times 0.5168 \approx 0.01356 \;(\approx 1.36\%)
```

**Follow-up:** On average, how many calls must the surveyor make per day?

```math
E[X] = \frac{r}{p} = \frac{3}{0.09} \approx 33.33 \text{ calls}
```

- **Rounding question from a student:** If the result were 33.8, should you round to 33 or 34? The instructor said to follow normal rounding rules: below .5 round down, .5 or above round up. So 33.33 rounds to about 33 calls.
- Like the geometric, a table of $`P(X = x)`$ for $`x = 3, 4, 5, \dots`$ gives a **right-skewed** distribution.

---

### 2.3 Hypergeometric Distribution (sampling *without replacement*)

All distributions covered before this one assumed independent trials, which is effectively sampling with replacement. The hypergeometric is the first case **without replacement**.

#### Worked Example 1: Doctors and nurses

**Setup:** A conference has 6 doctors and 19 nurses, 25 people in total. Five people are selected at random without replacement.

**Question:** What is $`P(\text{4 doctors and 1 nurse})`$?

- **Denominator:** the number of ways to choose 5 people from 25 is $`\binom{25}{5}`$.
- **Numerator:** choose 4 of the 6 doctors and 1 of the 19 nurses.

```math
P(X=4) = \frac{\binom{6}{4}\binom{19}{1}}{\binom{25}{5}} = \frac{15 \times 19}{53130} = \frac{285}{53130} \approx 0.00536 \quad \text{(computed for these notes)}
```

#### General form

A population has two types of items. Examples: doctors and nurses, red and white balls, good and defective batteries.

- $`N`$ = number of items of the type of interest (e.g., doctors)
- $`M`$ = number of items of the other type (e.g., nurses)
- $`n`$ = sample size, drawn without replacement
- $`X`$ = number of items of the type of interest in the sample

```math
\boxed{P(X = i) = \frac{\binom{N}{i}\binom{M}{n-i}}{\binom{N+M}{n}}}
```

- Any random variable with this PMF is a **hypergeometric random variable**.
- The key parameters are $`N`$, $`M`$ and $`n`$. The value $`i`$ is the outcome, not a parameter.

**Terminology reminder from the instructor:** for discrete random variables we say **probability mass function (PMF)**. "Density" (PDF) is reserved for continuous random variables.

**Mean and variance:** let $`p = \dfrac{N}{N+M}`$ be the proportion of the type of interest.

```math
E[X] = np, \qquad \mathrm{Var}(X) = np(1-p)\left[1 - \frac{n-1}{N+M-1}\right]
```

The bracketed factor is the finite-population correction. Without it, the variance would be the binomial $`np(1-p)`$.

#### Worked Example 2: Used components (functional system)

**Setup:**
- A 6-component system is built by randomly choosing 6 components from a bin of 20 used components.
- 15 of the 20 components work and 5 do not.
- The system is functional if **at least 4** of its 6 components work.

**Question:** What is $`P(\text{system functional})`$? Here $`N = 15`$ (working), $`M = 5`$ (not working) and $`n = 6`$.

```math
P(X \ge 4) = \sum_{i=4}^{6} P(X=i) = \frac{\binom{15}{4}\binom{5}{2} + \binom{15}{5}\binom{5}{1} + \binom{15}{6}\binom{5}{0}}{\binom{20}{6}}
```

Term by term:
- $`i=4`$: 4 working and 2 not working, $`1365 \times 10 = 13650`$
- $`i=5`$: 5 working and 1 not working, $`3003 \times 5 = 15015`$
- $`i=6`$: all 6 working, $`5005 \times 1 = 5005`$

```math
P(X\ge 4) = \frac{33670}{38760} \approx 0.8687 \quad \text{(computed for these notes)}
```

The instructor noted that if the condition had been exactly 4, only the first term would be needed.

---

### 2.4 Recap: The Six Discrete Random Variables (summary chart)

| RV | Situation | PMF | $`E[X]`$ | $`\mathrm{Var}(X)`$ |
|---|---|---|---|---|
| **Bernoulli** | A single trial ($`n=1`$) | $`P(X=0)=1-p,\; P(X=1)=p`$ | $`p`$ | $`p(1-p)`$ |
| **Binomial** | Number of successes in $`n`$ fixed independent trials | $`\binom{n}{x}p^x(1-p)^{n-x}`$ | $`np`$ | $`np(1-p)`$ |
| **Poisson** | Approximates the binomial when $`n\to\infty`$ and $`p`$ is small, with $`\lambda = np`$ | $`\dfrac{e^{-\lambda}\lambda^x}{x!}`$ | $`\lambda`$ | $`\lambda`$ (mean = variance) |
| **Geometric** | Trial on which the 1st success occurs ($`n`$ not fixed) | $`(1-p)^{x-1}p`$ | $`\dfrac{1}{p}`$ | $`\dfrac{1-p}{p^2}`$ |
| **Negative Binomial** | Trial $`n`$ on which the $`r`$-th success occurs | $`\binom{n-1}{r-1}p^r(1-p)^{n-r}`$ | $`\dfrac{r}{p}`$ | $`\dfrac{r(1-p)}{p^2}`$ |
| **Hypergeometric** | Sampling without replacement from $`N+M`$ items | $`\dfrac{\binom{N}{i}\binom{M}{n-i}}{\binom{N+M}{n}}`$ | $`np`$, with $`p=\frac{N}{N+M}`$ | $`np(1-p)\left[1-\frac{n-1}{N+M-1}\right]`$ |

**How the distributions connect:**
- Bernoulli becomes Binomial when you go from 1 trial to $`n`$ trials.
- Binomial is approximated by Poisson when $`n`$ is large, $`p`$ is small and $`\lambda = np`$.
- Geometric applies when $`n`$ is unknown and you want the first success.
- Negative Binomial applies when you want the $`r`$-th success at trial $`n`$.
- Hypergeometric is in a separate category: it covers sampling without replacement.

---

### 2.5 Revisited Practice Question: Tagged Fish (from a previous class)

**Setup:**
- A lake has 50 fish, of which 10 are tagged and 40 untagged.
- 7 fish are caught. What is $`P(\text{exactly 2 tagged})`$?
- In an earlier class this was treated as binomial. Today it was redone as hypergeometric (without replacement), with $`N=10`$, $`M=40`$ and $`n=7`$.

```math
P(X=2) = \frac{\binom{10}{2}\binom{40}{5}}{\binom{50}{7}}
```

The instructor briefly said "$`\binom{7}{2}`$" and then corrected it to $`\binom{10}{2}`$, because you choose 2 from the 10 tagged fish.

**Answer check:**
- A student quoted **0.319**.
- Computing the formula above gives $`\frac{45 \times 658008}{99884400} \approx 0.296`$ *(computed for these notes)*.
- The binomial version, $`\binom{7}{2}(0.2)^2(0.8)^5`$, gives $`\approx 0.275`$.
- Check the original question's numbers against the problem file.

---

## 3. Exam / Assignment Notes and Logistics

- **Likely exam question type:** *identify which random variable applies* to a scenario, then use its PMF, mean and variance. Be clear on the distinctions:
  - Binomial: fixed $`n`$, count the successes.
  - Geometric: trial of the first success.
  - Negative Binomial: trial of the $`r`$-th success.
  - Poisson: large $`n`$ and small $`p`$.
  - Hypergeometric: without replacement.
- **Practice file:** the instructor will send a file of practice questions on everything covered, with more hypergeometric questions. Answers will be discussed next class. Hypergeometric can be revisited at the end of the course if needed.
- **Formulas to memorise:** the means and variances in the table above, especially the hypergeometric variance with its correction factor $`1-\frac{n-1}{N+M-1}`$.
- **Reading:**
  - Sheldon Ross, *Probability and Statistics for Engineers and Scientists*, Chapter 5.
  - If you use the other Ross introductory statistics text, the topics are around pp. 127–155 (appendix).
- **Next topic:** continuous random variables and distributions.
- **Schedule:** no class Saturday (Diwali). The next class is **Monday**, and there are three classes next week (9th, 10th, 11th).

<!-- nav -->
← [Session 33 (2026-11-03)](DSM-101-33_2026-11-03_Ruchi-Sharma.md) · [All lectures](./) · [Session 35 (2026-11-09)](DSM-101-35_2026-11-09_Ruchi-Sharma.md) →
<!-- /nav -->
