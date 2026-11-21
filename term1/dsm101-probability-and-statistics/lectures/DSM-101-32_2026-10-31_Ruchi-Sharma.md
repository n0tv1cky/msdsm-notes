---
course: DSM 101
date: 2026-10-31
start: 2:45 pm
session: "32"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 31 (2026-10-27)](DSM-101-31_2026-10-27_Ruchi-Sharma.md) · [All lectures](./) · [Session 33 (2026-11-03)](DSM-101-33_2026-11-03_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 Session 32: Binomial Distribution (Mean, Variance, Mode) and Introduction to the Poisson Distribution

*Notes reconstructed from an ASR transcript. Obvious speech-to-text errors have been corrected. Anything inferred or added by the note-writer is marked as such.*

---

## 1. Overview

The session continues from the previous class on the **binomial random variable**. It opens with a student question on whether the "tagged fish" problem is really binomial when sampling is "without replacement." The instructor then:

- states the **binomial theorem** (the binomial probabilities sum to 1) and checks it on the earlier 6-coin-flip example;
- derives the binomial **mean** $`E[X] = np`$ and **variance** $`\mathrm{Var}(X) = np(1-p)`$;
- states (without proof) a result about where the binomial PMF reaches its **peak (mode)**.

The class works through practice questions:

- deciding whether a scenario is binomial, and *which condition is violated* if it is not;
- recovering $`n`$ and $`p`$ from a given mean and variance;
- direct PMF calculations.

The last part introduces the **Poisson random variable**: its use for counts per unit of time, distance, area or volume; its conditions; its status as a limiting case of the binomial; its PMF; and a worked example on typographical errors. A binomial-vs-Poisson comparison problem is set as homework.

---

## 2. Topics Covered (in order)

### 2.1 Recap: Binomial PMF

For $`X \sim \text{Binomial}(n, p)`$:

```math
P(X = x) = \binom{n}{x} p^{x} (1-p)^{n-x}, \quad x = 0, 1, \dots, n
```

### 2.2 Student question: the tagged-fish problem (from the last class)

- **Setup:** A pond has 50 fish, of which 10 are tagged. A fisherman's catch consists of 7 fish selected at random. What is the probability that exactly 2 are tagged?
- **Instructor's treatment:** The "10 out of 50" information is there to give $`p = \frac{10}{50} = 0.2`$. Then $`n = 7`$, $`x = 2`$, and the problem is treated as binomial.
- **Justification:** Think of a net pulling 7 fish out of the pond at random in one go. The chance that any one fish is tagged is then not affected by the others, so $`p`$ stays constant.
- **Caveat (important):** Suppose the fish are drawn **one at a time without replacement**. Then the probability that the next fish is tagged depends on whether earlier ones were tagged, so $`p`$ changes and the problem is **not binomial**.
  - *(Note-writer's addition: that case is the hypergeometric distribution.)*
- **Instructor's promise:** Exam questions will be worded clearly. If a question explicitly says "without replacement" in a sequential sense, the answer is "not binomial."

### 2.3 Binomial theorem (sum of probabilities = 1)

Stated without formal proof:

```math
\sum_{x=0}^{n} \binom{n}{x} p^{x}(1-p)^{n-x} = 1
```

- **Intuition:** If you add up the probabilities of every value the random variable can take, the total must be 1.
- **Check using the earlier example** (6 flips of a fair coin, $`p = 0.5`$, $`X`$ = number of tails):

| $`x`$ (tails) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $`P(X=x)`$ | $`\frac{1}{64}`$ | $`\frac{6}{64}`$ | $`\frac{15}{64}`$ | $`\frac{20}{64}`$ | $`\frac{15}{64}`$ | $`\frac{6}{64}`$ | $`\frac{1}{64}`$ |

- The total is $`\frac{64}{64} = 1`$.
- *(Correction: the transcript garbles the order of these values. The table shows the correct values.)*

### 2.4 Parameters of the binomial

- The distribution is fully determined by two parameters, $`n`$ and $`p`$.
- The key summary statistics are the **mean** and the **variance**.
- The instructor will derive these **only for the binomial**. For the other distributions the class will take the results as given, focus on intuition, and concentrate on applied questions.

### 2.5 Derivation: $`E[X] = np`$

The strategy is to rewrite the sum so that it becomes another binomial sum, which equals 1 by the binomial theorem.

1. Start from the definition:

```math
E[X] = \sum_{x=0}^{n} x\binom{n}{x}p^x(1-p)^{n-x}
```

2. The $`x = 0`$ term is zero because it is multiplied by $`x`$. So start the sum at 1:

```math
E[X] = \sum_{x=1}^{n} x\binom{n}{x}p^x(1-p)^{n-x}
```

3. Simplify $`x\binom{n}{x}`$ using two facts:
   - $`n! = n\,(n-1)!`$
   - $`n - x = (n-1) - (x-1)`$

   This gives:

```math
x\binom{n}{x} = \frac{x \cdot n\,(n-1)!}{\big((n-1)-(x-1)\big)!\; x\,(x-1)!} = n\binom{n-1}{x-1}
```

4. Split $`p^x = p \cdot p^{x-1}`$ and write $`(1-p)^{n-x} = (1-p)^{(n-1)-(x-1)}`$.

5. Pull out the constants $`n`$ and $`p`$ (they do not depend on $`x`$):

```math
E[X] = np\sum_{x=1}^{n}\binom{n-1}{x-1}p^{x-1}(1-p)^{(n-1)-(x-1)}
```

6. Substitute $`a = x - 1`$ and $`b = n - 1`$:
   - when $`x = 1`$, $`a = 0`$;
   - when $`x = n`$, $`a = n - 1 = b`$.

   The sum becomes:

```math
E[X] = np\sum_{a=0}^{b}\binom{b}{a}p^{a}(1-p)^{b-a}
```

7. The remaining sum is a full set of binomial probabilities, so it equals 1 by the binomial theorem. Therefore:

```math
\boxed{E[X] = np}
```

### 2.6 Derivation: $`\mathrm{Var}(X) = np(1-p)`$

1. Use the variance formula:

```math
\mathrm{Var}(X) = E[X^2] - (E[X])^2, \qquad (E[X])^2 = n^2p^2
```

2. The difficult part is $`E[X^2]`$. Write $`x^2 = x(x-1) + x`$, so that:

```math
E[X^2] = E[X(X-1)] + E[X]
```

3. Compute $`E[X(X-1)]`$ using the same trick as for the mean.
   - The $`x = 0`$ and $`x = 1`$ terms vanish, so the sum starts at $`x = 2`$.
   - The instructor asked the class to spot this step, which she had initially skipped.

```math
E[X(X-1)] = \sum_{x=2}^{n} x(x-1)\binom{n}{x}p^x(1-p)^{n-x}
```

4. Expand the factorials:
   - $`n! = n(n-1)(n-2)!`$
   - $`x! = x(x-1)(x-2)!`$
   - $`n - x = (n-2) - (x-2)`$

   The $`x(x-1)`$ factors cancel, giving:

```math
x(x-1)\binom{n}{x} = n(n-1)\binom{n-2}{x-2}
```

5. Split $`p^x = p^2 \cdot p^{x-2}`$ and write $`(1-p)^{n-x} = (1-p)^{(n-2)-(x-2)}`$.

6. Substitute $`a = x - 2`$ and $`b = n - 2`$:

```math
E[X(X-1)] = n(n-1)p^2\sum_{a=0}^{b}\binom{b}{a}p^a(1-p)^{b-a} = n(n-1)p^2
```

7. Put the pieces together:

```math
\mathrm{Var}(X) = n(n-1)p^2 + np - n^2p^2 = n^2p^2 - np^2 + np - n^2p^2 = np - np^2
```

```math
\boxed{\mathrm{Var}(X) = np(1-p) = npq, \quad q = 1-p}
```

- Some textbooks write the variance as $`npq`$.

### 2.7 Result: shape and peak (mode) of the binomial PMF

Stated without proof.

- **Statement:** Let $`X \sim \text{Binomial}(n, p)`$ with $`0 < p < 1`$. As $`k`$ goes from 0 to $`n`$, $`P(X = k)`$ first **increases monotonically** and then **decreases monotonically**.
- **Location of the peak:** The largest value occurs when $`k`$ is the **largest integer less than or equal to $`(n+1)p`$**.
- **Check with the coin example:** $`n = 6`$ and $`p = 0.5`$, so $`(n+1)p = 7 \times 0.5 = 3.5`$. The largest integer $`\le 3.5`$ is 3, and indeed $`P(X=3) = \frac{20}{64}`$ is the maximum in the table.
- **Proof hint (given verbally):** Look at the ratio $`\dfrac{P(X=k)}{P(X=k-1)}`$ and see when it is greater than or less than 1.
  - *(Note-writer's addition:* the ratio is $`\dfrac{(n-k+1)\,p}{k\,(1-p)}`$. It is $`\ge 1`$ exactly when $`k \le (n+1)p`$.)*

### 2.8 Practice questions on the binomial

**Conditions for a binomial experiment (recap):**

1. Each trial results in exactly two mutually exclusive outcomes (success or failure).
2. The trials are independent.
3. The probability of success $`p`$ is constant from trial to trial.
4. The number of trials $`n`$ is fixed and finite.

**Q1–Q3: Is $`X`$ binomial?** None of them are.

- **Q1:** From a standard 52-card deck, a person draws 9 cards **without replacement**. $`X`$ is the number of queens drawn.
  - **Not binomial.** The trials are not independent, so $`p`$ changes from draw to draw.
- **Q2:** A similar without-replacement scenario.
  - **Not binomial**, for the same reason.
- **Q3:** In a game, a turn consists of rolling a pair of six-sided dice until both dice show the same number. $`X`$ is the number of rolls in one turn.
  - **Not binomial.** The number of trials is not fixed; it is potentially infinite.

**A student's computation (context unclear in the transcript; labelled "Section B, first question"):**

```math
\binom{5}{4}\left(\tfrac{1}{6}\right)^4\left(\tfrac{5}{6}\right)^{1} \approx 0.0032 = 0.32\%
```

**Q4: Recover $`n`$ and $`p`$ from the mean and variance.**

- **Given:** mean $`= 4`$, variance $`= \frac{4}{3}`$. Find $`P(X \ge 1)`$.
- **Solution:**
  - From $`np = 4`$ and $`npq = \frac{4}{3}`$, we get $`q = \frac{4/3}{4} = \frac{1}{3}`$.
  - So $`p = \frac{2}{3}`$ and $`n = \frac{4}{2/3} = 6`$.
  - Use the complement:

```math
P(X \ge 1) = 1 - P(X = 0) = 1 - \left(\tfrac{1}{3}\right)^6 = 1 - \tfrac{1}{729} = \tfrac{728}{729} \approx 0.9986
```

**Q (the "second" question): direct PMF calculation.**

- **Given:** $`n = 8`$, $`p = 0.1`$, find $`P(X = 2)`$.
- **Solution:**

```math
P(X=2) = \binom{8}{2}(0.1)^2(0.9)^6 = 28 \times 0.01 \times 0.531441 \approx 0.1488 = 14.88\%
```

**Q6: Goals scored.**

- **Setup:** 5 goals, each equally likely to go either way, so $`n = 5`$ and $`p = q = \frac{1}{2}`$. Compute the full distribution.
- **General term:**

```math
P(X=k) = \binom{5}{k}\left(\tfrac{1}{2}\right)^k\left(\tfrac{1}{2}\right)^{5-k} = \binom{5}{k}\tfrac{1}{32}
```
- **First term:** $`P(X=0) = \binom{5}{0}\left(\tfrac12\right)^0\left(\tfrac12\right)^5 = \tfrac{1}{32}`$.
- **Repeat for $`k = 1, \dots, 5`$.** *(Note-writer's computation:)* the values are $`\tfrac{1}{32}, \tfrac{5}{32}, \tfrac{10}{32}, \tfrac{10}{32}, \tfrac{5}{32}, \tfrac{1}{32}`$.

The remaining questions will be shared as a file for practice.

### 2.9 The Poisson random variable

**Use case:** counting the **number of occurrences of an event in a given unit** of time, distance, area or volume.

**Examples given in class:**

- number of cars passing under a bridge in a day;
- number of patients visiting a hospital in a day;
- number of misprints on a page of a book;
- number of patents filed by a company or academic institution in a year.

**Name:** after the French mathematician and physicist **Siméon Denis Poisson**.

**Conditions:**

1. **Events occur independently.** For example, one patient's arrival has nothing to do with another's.
   - *Counter-example:* in a pandemic, contagion makes arrivals dependent, so the Poisson model may not be valid and another distribution would be needed.
2. **The probability that an event occurs in a given length of time (or space) does not change.** The instructor stressed this condition.

**Poisson as a limiting case of the binomial:**

- The number of trials $`n \to \infty`$ (indefinitely large).
- The probability of success $`p`$ is constant on every trial and very small.
  - *(Correction: the transcript says "very large," which is an ASR or speech slip. In the Poisson limit, $`p \to 0`$.)*
- The product $`\lambda = np`$ stays a **finite, positive real number**. The whole distribution depends on $`\lambda`$.
- Equivalently, $`p = \dfrac{\lambda}{n}`$.
- The full derivation is postponed to the next class.

**Poisson PMF:**

```math
P(X = x) = \frac{e^{-\lambda}\lambda^{x}}{x!}, \quad x = 0, 1, 2, \dots
```

### 2.10 Worked example: typographical errors

- **Setup:** The number of typographical errors on a single page follows a Poisson distribution with $`\lambda = \tfrac{1}{2}`$. Find the probability of **at least one** error on a given page.
- **Method:** Use the complement.

```math
P(X \ge 1) = 1 - P(X=0) = 1 - \frac{e^{-1/2}\left(\tfrac12\right)^0}{0!} = 1 - e^{-1/2} \approx 1 - 0.6065 = 0.3935
```
- The answer is roughly **39–40%**.

---

## 3. Homework, Exam Notes, and What Comes Next

### Homework (to be discussed next class)

- **Problem:** The probability that an item produced by a certain machine is defective is $`0.1`$. Find the probability that a sample of 10 items contains **at most one** defective item.
  - *(The transcript says "its most"; "at most one" is the likely wording.)*
- **Task:** Solve it **both** with the binomial and with the Poisson approximation, and compare the answers.
- *(Note-writer's answer for self-checking:)*
  - Binomial: $`(0.9)^{10} + 10(0.1)(0.9)^9 \approx 0.3487 + 0.3874 = 0.7361`$
  - Poisson with $`\lambda = np = 1`$: $`e^{-1}(1 + 1) \approx 0.7358`$

### Exam notes

- **"Is it binomial?" questions:** You must say **which condition is violated** (independence, constant $`p`$, finite or fixed $`n`$, two outcomes), not just answer yes or no.
- **"Without replacement":** If an exam question clearly states sequential sampling without replacement, $`p`$ changes, so the variable is **not binomial**. Exam wording will be clearer than in the fish problem.
- **Formulas to know:**
  - $`E[X] = np`$
  - $`\mathrm{Var}(X) = np(1-p) = npq`$
  - Mode: largest integer $`\le (n+1)p`$
  - Poisson PMF: $`\dfrac{e^{-\lambda}\lambda^x}{x!}`$
- **Useful technique:** For "at least one" questions, compute $`1 - P(X = 0)`$.

### What comes next

- Derivations are done only for the binomial. For other distributions the course will use the results and focus on applications.
- The next one or two classes will finish discrete distributions, including the Poisson-as-limit-of-binomial derivation.
- After that, the course moves to continuous distributions. More time will be spent there because the **normal distribution** is used heavily in later analysis.

<!-- nav -->
← [Session 31 (2026-10-27)](DSM-101-31_2026-10-27_Ruchi-Sharma.md) · [All lectures](./) · [Session 33 (2026-11-03)](DSM-101-33_2026-11-03_Ruchi-Sharma.md) →
<!-- /nav -->
