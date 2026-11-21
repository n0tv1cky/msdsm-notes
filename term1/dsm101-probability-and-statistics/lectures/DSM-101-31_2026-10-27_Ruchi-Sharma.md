---
course: DSM 101
date: 2026-10-27
start: 7:00pm
session: "31"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 30 (2026-10-24)](DSM-101-30_2026-10-24_Pritee-Sharma.md) · [All lectures](./) · [Session 32 (2026-10-31)](DSM-101-32_2026-10-31_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 · Lecture 31 · Bernoulli and Binomial Distributions

**Session:** DSM-101-31 · 2026-10-27 · Instructor: Dr. Ruchi Sharma (IIT Indore, School of Humanities & Social Sciences)

---

## 1. Overview

This is the first of ten lectures by a new instructor. It begins with course logistics: the syllabus for her portion and the marks breakdown. It then reviews discrete random variables, the probability mass function (PMF), expectation, and variance. The **Bernoulli distribution** is introduced with a poll example, and its mean $p$ and variance $p(1-p)$ are derived. The lecture then covers the **Binomial distribution**: its four conditions, the coin-flip example ($n=6$) showing the shape of the distribution, and a general PMF derived from a basketball example. Two worked problems follow: defective disks with a money-back guarantee, and tagged fish in a pond. The fish problem is used to show when the binomial model breaks down because sampling is without replacement. The binomial distribution will be completed next class (Saturday), followed by the Poisson distribution.

---

## 2. Course Logistics and Syllabus (this instructor's 10 lectures)

**Lectures 1–5: Probability distributions**
- Discrete distributions: Bernoulli, Binomial, Poisson, and possibly Negative Binomial.
- Continuous distributions: Uniform and Normal.
- Links between these distributions (Bernoulli → Binomial → Poisson → Normal).

**Lectures 6–10: Correlation and Regression**
- The focus is the reasoning behind bivariate association, not software output.
- Topics: basic formulas and types of correlation, then a brief introduction to regression.

**Assessment for this portion (25 marks total):**
- **Assignment: 10 marks.**
  - Must be **handwritten** (mandatory).
  - Questions will be simple but more descriptive than usual.
- **End-term exam: 15 marks.**
  - Combined with Preeti's portion (the instructor before this one).
  - Scheduled for about **23 November**, per the timetable.
  - Format: the exam is sent as a PDF. You write your answers by hand and upload them. The exam is camera-proctored.

---

## 3. Topics Covered (in order)

### 3.1 Random variables (review)

- A **random variable** $X$ is defined by a *rule* that maps outcomes of an experiment to real numbers.
  - Example: on a die roll, "the number shown is less than 3" defines a different random variable from "the number shown is even."
- A random variable takes **real values**. It can be **discrete** or **continuous**.
- **Discrete random variable:** takes at most a **countable** number of possible values.
- Each type has its own probability function:
  - Discrete → **probability mass function (PMF)**.
  - Continuous → **probability density function (PDF)**.
- The PMF is defined as

```math
p_X(a) = P(X = a).
```

### 3.2 Expectation and variance of a discrete random variable

- **Expected value:**

```math
E[X] = \sum_{x} x\, p_X(x)
```
  - The sum runs over all possible values of $X$, for example $x = 0, 1, \dots, n$.
- **Variance (definition):**

```math
\mathrm{Var}(X) = E\big[(X-\mu)^2\big], \qquad \mu = E[X]
```
- **Variance (computational form):**

```math
\mathrm{Var}(X) = E[X^2] - \big(E[X]\big)^2
```

### 3.3 Bernoulli distribution

**Setup:**
- A **single** trial or experiment with exactly two outcomes: success or failure.
- $X = 1$ means success; $X = 0$ means failure.

**PMF:**

```math
P(X=0) = 1-p, \qquad P(X=1) = p, \qquad 0 \le p \le 1
```
- $p$ is the probability that the single trial is a success.

**Notation:** $X \sim \text{Ber}(p)$, also written $B(1, p)$.
- The "1" means the experiment is performed **once**. In the binomial case it becomes $n$.

**Worked example (poll):**
- A poll finds that 60% say NDA will return to power in 2029 and 40% say it will not.
- Pick **one** person at random. The probability that this person gives the favourable answer is $p = 0.6$, so $1-p = 0.4$.
- **Interpretation (instructor's emphasis):** $X$ describes the outcome for *one randomly chosen person*. It does **not** mean that one person believes there is a 60% chance.

**Mean:**

```math
E[X] = 0.4 \times 0 + 0.6 \times 1 = 0.6 = p
```
- In general, $E[X] = p$.

**Variance (numerical check with the definition):**

```math
\mathrm{Var}(X) = 0.4\,(0-0.6)^2 + 0.6\,(1-0.6)^2 = 0.144 + 0.096 = 0.24
```
- This matches $p(1-p) = 0.6 \times 0.4 = 0.24$.

**Variance (general derivation):**
1. Find the second moment:

```math
E[X^2] = 0^2(1-p) + 1^2 \cdot p = p
```
   - Note: in class this was briefly misspoken as "$p^2$"; the correct value is $p$.
2. Substitute into the computational form:

```math
\mathrm{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)
```

### 3.4 Binomial distribution: conditions

A Bernoulli random variable is the special case of a binomial with one trial. A **binomial experiment** satisfies all four of the following conditions:

1. **Two outcomes per trial.** Each trial results in two **mutually disjoint** outcomes, success or failure.
   - Example: a coin shows head or tail, never both.
2. **Fixed number of trials.** The number of trials $n$ is **finite** and known in advance.
3. **Independence.** The outcome of one trial does not affect any other trial.
   - Example: getting a head on the previous toss does not change the next toss.
4. **Constant probability.** The probability of success $p$ is the **same for every trial**.
   - Example: for a fair coin, $P(\text{head}) = 0.5$ on every toss.

**Counter-example (cards drawn without replacement):**
- After one card is drawn from 52, only 51 remain.
- The probabilities for the next draw therefore depend on the first draw.
- This violates both independence and constant $p$, so it is **not binomial**.

The binomial distribution has wide applications in statistics and serves as the base from which many other distributions are developed.

### 3.5 Worked example: 6 coin flips

**Setup:**
- Tail = success, head = failure; $X$ = number of tails.
- Total number of possible sequences: $2^6 = 64$.

**Probabilities:**

| $x$ | $\binom{6}{x}$ | $P(X=x)$ |
|---|---|---|
| 0 | $\frac{6!}{0!\ 6!} = 1$ | $1/64$ |
| 1 | $\frac{6!}{1!\ 5!} = 6$ | $6/64$ |
| 2 | $\frac{6!}{2!\ 4!} = 15$ | $15/64$ |
| 3 | $\frac{6!}{3!\ 3!} = 20$ | $20/64$ |
| 4 | 15 | $15/64$ |
| 5 | 6 | $6/64$ |
| 6 | 1 | $1/64$ |

**Observations:**
- If you plot $x$ against $P(X=x)$, the graph rises to a peak at $x=3$ and falls **symmetrically**.
- The numbers $\binom{n}{x}$ are called **binomial coefficients**.
- As $n$ becomes very large, the gaps between bars fill in. The shape approaches a **bell-shaped curve**, similar to the **normal distribution**.

### 3.6 Deriving the binomial PMF: basketball example

**Setup:**
- A player scores with probability $p = 0.7$ and misses with probability $1-p = 0.3$.
- She makes 6 attempts. Find $P(\text{exactly 2 successes})$.

**Key point: order does not matter.**
- Sequences such as $0.7, 0.7, 0.3, 0.3, 0.3, 0.3$ or $0.3, 0.7, 0.3, 0.7, \dots$ all count.
- Each such sequence has probability $p^2(1-p)^4$.
- The number of such sequences is $\binom{6}{2}$.

**Result:**

```math
P(X=2) = \binom{6}{2}(0.7)^2(0.3)^4 = 15 \times 0.49 \times 0.0081 \approx 0.0595
```
- The final number was not computed in class; it is added here for completeness.

**General binomial PMF:**

```math
P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \qquad x = 0, 1, \dots, n
```

```math
\binom{n}{x} = \frac{n!}{x!\,(n-x)!}
```

**Definitions and notation:**
- Any random variable with this PMF is a **binomial random variable** (also called a binomial variate).
- Notation: $X \sim B(n, p)$.
- Parameters:
  - $n$ = number of trials.
  - $p$ = probability of success on each trial.

### 3.7 Worked problem: defective disks

**Setup:**
- Each disk is defective with probability $p = 0.01$, independently of other disks.
- Disks are sold in packages of $n = 10$.
- $X$ = number of defective disks in a package, so $X \sim B(10, 0.01)$.

**Note on the wording:**
- In class the guarantee was stated as "at most one defective."
- The calculation actually done was $1 - [P(X=0) + P(X=1)]$, which is the probability of **more than one** defective.
- This matches the standard textbook version of the problem (Ross): a package is returned if **more than one** disk is defective.

**(a) What proportion of packages is returned?**

```math
P(\text{return}) = 1 - \left[\binom{10}{0}(0.01)^0(0.99)^{10} + \binom{10}{1}(0.01)^1(0.99)^9\right]
```

```math
= 1 - (0.9044 + 0.0914) = 1 - 0.9957 \approx 0.0043
```
- In class, students got $0.995$ for the bracketed sum and about $0.0043$ for the answer.
- The instructor rounded this to about $0.005$.

**(b) If someone buys 3 packages, what is the probability that exactly one is returned?**
- Each package is now one Bernoulli trial with success probability equal to the answer from (a).
- So the number of returned packages is $B(3,\  0.0043)$.

```math
\binom{3}{1}(0.0043)(1-0.0043)^2 \approx 0.0128
```
- Using the rounded value $0.005$: $3(0.005)(0.995)^2 \approx 0.015$.
- **Point stressed in class:** part (b) cannot be solved without part (a). The probability found in (a) becomes the $p$ for (b).

**Clarification from Q&A:**
- "At most $k$" means $\le k$.
- "At least $k$" means $\ge k$, i.e., that value or more.

### 3.8 Worked problem: tagged fish (when binomial fails)

**Version 1, as solved in class:**
- A pond has 50 fish, 10 of them tagged.
- A catch of 7 fish is taken at random. $X$ = number of tagged fish.
- Using $p = 10/50 = 1/5$:

```math
P(X=2) = \binom{7}{2}\left(\tfrac{1}{5}\right)^2\left(\tfrac{4}{5}\right)^5 = 21 \times 0.04 \times 0.32768 \approx 0.275
```

**Caution (not stated in class):**
- Strictly, catching 7 distinct fish is sampling **without replacement**.
- The exact model is **hypergeometric**:

```math
P(X=2) = \frac{\binom{10}{2}\binom{40}{5}}{\binom{50}{7}} \approx 0.296
```
- The binomial answer above is only an approximation.

**Version 2:**
- The fisherman catches one fish at a time, does **not** return it, and catches 10 fish in total. What is $P(\text{2 tagged})$?
- This is **not binomial**. The first catch changes the composition of the pond, e.g., $10/50$ becomes $9/49$ or $10/49$.
- So the trials are **not independent** and $p$ is **not constant**.
- The binomial PMF cannot be used. The class stopped here; it will continue next session.

---

## 4. Exam and Assignment Notes

- **Marks for this portion:** 25 total (10 for the handwritten assignment, 15 in the end-term exam combined with Preeti's portion). End-term is about 23 November; PDF download, handwritten answers, upload, camera-proctored.
- **Choosing the right distribution:** after covering a few distributions, the instructor will give mixed examples. You will need to decide whether a situation is Bernoulli, binomial, Poisson, etc. Know the **four binomial conditions** well. Checking independence and constant $p$ (e.g., with vs. without replacement) is the usual test.
- **Interpreting $p$:** $p$ is the probability for one randomly selected trial or individual, not a belief held by that individual (poll example).
- **Multi-part problems:** an earlier answer often becomes the $p$ for a later part (disk problem).
- **Results to memorise:**
  - Bernoulli: $E[X]=p$ and $\mathrm{Var}(X)=p(1-p)$.
  - Binomial PMF: $\binom{n}{x}p^x(1-p)^{n-x}$.
  - Variance: $\mathrm{Var}(X)=E[X^2]-(E[X])^2$.

---

## 5. Formula Summary

| Concept | Formula |
|---|---|
| PMF | $p_X(a) = P(X=a)$ |
| Expectation (discrete) | $E[X] = \sum_x x\ p_X(x)$ |
| Variance | $\mathrm{Var}(X) = E[(X-\mu)^2] = E[X^2] - (E[X])^2$ |
| Bernoulli PMF | $P(X=1)=p,\  P(X=0)=1-p$ |
| Bernoulli mean / variance | $E[X]=p,\  \mathrm{Var}(X)=p(1-p)$ |
| Binomial coefficient | $\binom{n}{x} = \dfrac{n!}{x!\ (n-x)!}$ |
| Binomial PMF, $X\sim B(n,p)$ | $P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}$ |

**Next class (Saturday):** finish the binomial distribution, then the Poisson distribution.

<!-- nav -->
← [Session 30 (2026-10-24)](DSM-101-30_2026-10-24_Pritee-Sharma.md) · [All lectures](./) · [Session 32 (2026-10-31)](DSM-101-32_2026-10-31_Ruchi-Sharma.md) →
<!-- /nav -->
