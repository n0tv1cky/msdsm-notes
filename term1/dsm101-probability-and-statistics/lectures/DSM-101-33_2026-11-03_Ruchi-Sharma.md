---
course: DSM 101
date: 2026-11-03
start: 7:00pm
session: "33"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 32 (2026-10-31)](DSM-101-32_2026-10-31_Suman-Majumdar-Prof-Arshad-Prof-Ruchi-Sharma-Prof-Pritee-Sharma.md) · [All lectures](./) · [Session 34 (2026-11-04)](DSM-101-34_2026-11-04_Ruchi-Sharma.md) →
<!-- /nav -->

# DSM-101 (Probability & Statistics), Session 33: Poisson Distribution (Limit, Mean, Variance) and the Geometric Distribution

**Session file:** DSM-101-33_2026-11-03_Ruchi-Sharma

---

## 1. Overview

This session finishes the **Poisson distribution** and introduces the **geometric distribution**. It opens with an intuitive derivation, using cars passing under a bridge, of the Poisson as a **limiting case of the Binomial** when $n \to \infty$ and $p \to 0$ with $\lambda = np$ held fixed. The derivation uses the standard limit $\lim_{n\to\infty}(1 + x/n)^n = e^x$. The instructor then derives $E[X] = \lambda$ for the Poisson, sketches why $\mathrm{Var}(X) = \lambda$, and recaps the Binomial for comparison. Several Poisson problems are worked: a Binomial-vs-Poisson comparison, radioactive decays with $\lambda = 4.6$, and people entering a building with $\lambda = 50$. The second half defines the **geometric random variable** (number of trials until the first success), its PMF, mean $1/p$ and variance $(1-p)/p^2$, and contrasts it with the Binomial. A set of "Binomial, geometric, or neither?" classification problems and geometric probability calculations follow. The next class covers the **negative binomial** and **hypergeometric** distributions, wraps up discrete distributions, and then moves to continuous ones.

---

## 2. Topics Covered (in order)

### 2.1 Poisson as a limiting case of the Binomial: the bridge/cars example

**Setup**
- Let $X$ be the number of cars passing under a bridge (or along a stretch of road) in **1 hour**.
- The goal is to find the probability distribution of $X$.

**Assumptions** (the instructor noted these are limiting, e.g., rush hour breaks them):
1. The probability of a car passing is the **same** in every small sub-interval of time (constant $p$).
2. Events are **independent**: one car passing does not affect the probability of another.

**Parameters**
- Let $\lambda$ be the average number of cars per hour.
- Since $\lambda = np$, we have $p = \dfrac{\lambda}{n}$.

**Discretising the hour**
- **Split into 60 one-minute trials.** Each minute is a trial with success probability $\lambda/60$:
$$P(X = x) = \binom{60}{x}\left(\frac{\lambda}{60}\right)^x\left(1 - \frac{\lambda}{60}\right)^{60 - x}$$
- **Split into 3600 one-second trials.** Each second is a trial with success probability $\lambda/3600$:
$$P(X = x) = \binom{3600}{x}\left(\frac{\lambda}{3600}\right)^x\left(1 - \frac{\lambda}{3600}\right)^{3600 - x}$$
- **Key idea:** keep making $n$ larger and $p$ smaller with $np = \lambda$ fixed. The Binomial then converges to the Poisson.

### 2.2 The derivation

**Step 1: start from the Binomial PMF and substitute $p = \lambda/n$.**
$$P(X = x) = \binom{n}{x}p^x(1-p)^{n-x} = \frac{n!}{(n-x)!\,x!}\left(\frac{\lambda}{n}\right)^x\left(1 - \frac{\lambda}{n}\right)^{n-x}$$

**Standard result needed** (the instructor mentioned it is also used for continuous compound interest):
$$\lim_{n\to\infty}\left(1 + \frac{x}{n}\right)^n = e^x$$

**Step 2: rearrange into three factors.**
$$P(X=x) = \frac{\lambda^x}{x!}\cdot\frac{n(n-1)(n-2)\cdots(n-x+1)}{n^x}\cdot\left(1-\frac{\lambda}{n}\right)^{n-x}$$

- This uses $\dfrac{n!}{(n-x)!} = n(n-1)(n-2)\cdots(n-x+1)$, which is a product of exactly $x$ terms.
- **Illustration used in class:** with $n = 7$ and $x = 5$,
$$\frac{7!}{2!} = 7\cdot 6\cdot 5\cdot 4\cdot 3,$$
which is 5 terms, and the last term is $n - x + 1 = 3$.
- Because the numerator has $x$ terms, divide each one by $n$ (using up the $n^x$):
$$\frac{n}{n}\cdot\frac{n-1}{n}\cdots\frac{n-x+1}{n} = 1\cdot\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)\cdots\left(1-\frac{x-1}{n}\right)$$

**Step 3: take the limit of each factor as $n \to \infty$.**
1. $\dfrac{\lambda^x}{x!}$ does not depend on $n$, so it comes out of the limit unchanged.
2. $\left(1-\frac{1}{n}\right)\cdots\left(1-\frac{x-1}{n}\right) \to 1$, since each $k/n \to 0$. Intuitively, $n$ grows from 60 to 3600 and beyond.
3. Split the last factor: $\left(1-\frac{\lambda}{n}\right)^{n-x} = \left(1-\frac{\lambda}{n}\right)^{n}\cdot\left(1-\frac{\lambda}{n}\right)^{-x}$.
   - $\left(1-\frac{\lambda}{n}\right)^{-x} \to 1$.
   - $\left(1-\frac{\lambda}{n}\right)^{n} \to e^{-\lambda}$, by the standard limit with $x$ replaced by $-\lambda$.

**Result: the Poisson PMF.**
$$\boxed{P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}, \quad x = 0, 1, 2, \dots}$$

**Conclusion:** the Poisson is the limit of the Binomial when $n$ is very large and $p$ is very small.

**Typical Poisson applications** (recapped from the last class):
- cars passing a point per hour or minute
- patients visiting a hospital
- patents filed by a company
- misprints on a page

### 2.3 Mean of the Poisson: $E[X] = \lambda$

1. Write the definition:
$$E[X] = \sum_{x=0}^{\infty} x\,\frac{e^{-\lambda}\lambda^x}{x!}$$
2. The $x = 0$ term is 0, so start the sum at $x = 1$:
$$E[X] = \sum_{x=1}^{\infty} x\,\frac{e^{-\lambda}\lambda^x}{x!}$$
3. Take $e^{-\lambda}$ outside. Use $x! = x\,(x-1)!$ and $\lambda^x = \lambda\cdot\lambda^{x-1}$, then cancel the $x$:
$$E[X] = \lambda e^{-\lambda}\sum_{x=1}^{\infty}\frac{\lambda^{x-1}}{(x-1)!}$$
4. Substitute $a = x - 1$. When $x = 1$, $a = 0$:
$$E[X] = \lambda e^{-\lambda}\sum_{a=0}^{\infty}\frac{\lambda^{a}}{a!} = \lambda e^{-\lambda}\cdot e^{\lambda} = \lambda e^{0} = \lambda$$

### 2.4 Variance of the Poisson: $\mathrm{Var}(X) = \lambda$ (left as an exercise)

- Use
$$\mathrm{Var}(X) = E[X^2] - (E[X])^2,$$
and write $E[X^2] = E[X(X-1)] + E[X]$.
- Follow the same trick as for the mean, but pull out **two** factors: $x! = x(x-1)(x-2)!$.
- This gives $E[X(X-1)] = \lambda^2$, so
$$\mathrm{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda.$$
- The full proof will be shared in the instructor's notes.

### 2.5 Recap: Binomial vs Poisson

| | Binomial | Poisson |
|---|---|---|
| PMF | $\binom{n}{x}p^x(1-p)^{n-x}$ | $\dfrac{e^{-\lambda}\lambda^x}{x!}$ |
| Mean | $np$ | $\lambda$ |
| Variance | $npq$, where $q = 1-p$ | $\lambda$ |

- For the Poisson, **mean equals variance**. The instructor called this "a bit limiting."

### 2.6 Worked examples: Poisson

**Example A (homework Q2): Binomial vs Poisson approximation, with $n = 10$, $p = 0.1$, so $\lambda = np = 1$.**
- Using the Binomial:
  - $P(X=0) = 0.9^{10} \approx 0.3487$
  - $P(X=1) = \binom{10}{1}(0.1)(0.9)^9 \approx 0.3874$
  - Sum: $\approx 0.736$
- Using the Poisson with $\lambda = 1$:
$$P(X\le 1) = e^{-1} + e^{-1} = \frac{2}{e} \approx 0.7358$$
- The two answers are very close.

**Example B: radioactive decays, with $\lambda = 4.6$ decays in 2 seconds.**

(i) Exactly 3 decays in 2 seconds:
$$P(X=3) = \frac{e^{-4.6}(4.6)^3}{3!} \approx 0.1631$$

(ii) No more than 3 decays in 2 seconds, i.e. $X = 0, 1, 2, 3$:
$$P(X\le 3) = e^{-4.6}\left(\frac{4.6^0}{0!} + \frac{4.6^1}{1!} + \frac{4.6^2}{2!} + \frac{4.6^3}{3!}\right) \approx 0.3257$$

- **Suggested exercise:** compute the probabilities for each value of $X$ (for example in Excel) and plot them.
- The plot is **right-skewed**, whereas the Binomial examples seen earlier were more symmetric.

**Example C (Q4): people entering a building.**
- People enter according to a Poisson process at **5 per minute**. The building starts empty.
- Question: what is the probability of finding no one in the building after 10 minutes?
- The rate scales with time, so $\lambda = 5 \times 10 = 50$:
$$P(X=0) = \frac{e^{-50}\,50^0}{0!} = e^{-50} \approx 1.93\times 10^{-22}$$
- This is essentially zero.
- The instructor stressed understanding how $\lambda$ is obtained (4.6 here, 50 there) by scaling the rate to the time window.

### 2.7 Geometric random variable

**Definition**
- Independent trials are performed, each with the same success probability $p$, where $0 < p < 1$.
- Trials continue **until the first success**.
- $X$ is the number of trials required until the first success.

**PMF**
$$\boxed{P(X = n) = (1-p)^{n-1}\,p = q^{n-1}p, \quad n = 1, 2, 3, \dots}$$

- **Reasoning:** the first $n-1$ trials are failures and the $n$-th trial is a success. This condition is necessary and sufficient, and independence lets us multiply the probabilities.
- **Example:** if the first success comes on the 9th trial, then trials 1 to 8 failed, so the probability is $(1-p)^8 p$.

**Probabilities sum to 1** (a geometric series):
$$\sum_{n=1}^{\infty}(1-p)^{n-1}p = p\cdot\frac{1}{1-(1-p)} = \frac{p}{p} = 1$$

So, with probability 1, a success eventually occurs.

**Mean and variance** (proofs to be shared in the notes):
$$\boxed{E[X] = \frac{1}{p}}, \qquad \boxed{\mathrm{Var}(X) = \frac{1-p}{p^2}}$$

- **Intuition:** if $P(\text{rolling a six}) = 1/6$, the expected number of rolls to get a six is 6.

### 2.8 Binomial vs Geometric

**Illustration**
- $X$ = number of sixes in 12 rolls of a fair die. This is **Binomial**.
- $Y$ = number of rolls until you get a six. This is **Geometric**.

| Feature | Binomial | Geometric |
|---|---|---|
| Two outcomes (success/failure) | Yes | Yes |
| Same $p$ on each trial | Yes | Yes |
| Independent trials | Yes | Yes |
| Number of trials | **Fixed** $n$ | **Not fixed** |
| Question asked | How many successes in a fixed number of trials? | How many trials until the first success? |
| Support | $0, 1, \dots, n$ | $1, 2, 3, \dots$ (min 1, no upper bound) |

### 2.9 Classification problems and geometric calculations

1. **Pair of dice rolled until doubles; $X$ is the number of rolls in one turn.**
   - Classification: **Geometric**, with $p = 1/6$.

2. **Roll 7 six-sided dice and count the fives; $F$ is the number of fives.**
   - Classification: **Binomial**, with $n = 7$, $p = 1/6$.
   - Example probability:
$$P(F=5) = \binom{7}{5}\left(\frac{1}{6}\right)^5\left(\frac{5}{6}\right)^2$$

3. **Class of 25 students; a different student is randomly selected each week to bring a snack; 8% have food allergies; $T$ is the number of weeks until an allergic student is selected.**
   - Classification: **Neither.**
   - Several students first treated it as geometric and got $1/0.08 = 12.5$ weeks. That is **wrong**.
   - Selection is **without replacement**, so trials are not independent and $p$ changes from week to week. That rules out geometric.
   - There is also no fixed number of trials, which rules out Binomial.
   - $T$ is still a discrete random variable.
   - The instructor noted it is not hypergeometric either, as more information would be needed. The hypergeometric is the only without-replacement distribution the course will cover.

4. **Survey representative calls random numbers until someone answers; $P(\text{answer}) = 0.22$; $N$ is the number of calls.**
   - Classification: **Geometric**, since the number of calls is not fixed.
   - Probability the 10th call is the first success:
$$P(N=10) = (0.78)^9(0.22)$$
   - This evaluates to $\approx 0.0235$. (Computed for these notes; not stated in class.)

5. **Ram makes 25% of three-point attempts. Probability the first success is on the 3rd attempt:**
$$P(X=3) = \frac{3}{4}\cdot\frac{3}{4}\cdot\frac{1}{4} = \frac{9}{64} \approx 0.1406$$
   - The first two attempts fail and the third succeeds. (Decimal value computed for these notes.)

6. **Teacher draws a name at random with replacement from 20 students; $X$ is the number of draws until Sohan's name is drawn. Probability the first draw of Sohan is the 7th:**
   - Because the name is replaced, $p$ stays constant, so this is **Geometric**.
   - $p = \dfrac{1}{20}$ and $q = \dfrac{19}{20}$:
$$P(X=7) = \left(\frac{19}{20}\right)^6\left(\frac{1}{20}\right) \approx 0.0368$$

---

## 3. Exam / Assignment Notes

- **Not examined:** the derivation of the Poisson as a limit of the Binomial, and the proof of the Poisson variance. Understand them intuitively.
- **Know:** the PMF, mean and variance for the Binomial, Poisson and Geometric distributions:
  - Binomial: mean $np$, variance $npq$
  - Poisson: mean and variance both $\lambda$
  - Geometric: mean $1/p$, variance $(1-p)/p^2$
- **Be careful computing $\lambda$:** scale the rate to the time window, e.g. $5/\text{min} \times 10\text{ min} = 50$.
- **Be able to classify** a scenario as Binomial, Geometric or neither. Watch for **sampling without replacement**, which breaks independence and constant $p$ (the snack example).
- **Suggested exercise:** compute and plot Poisson probabilities for $\lambda = 4.6$ (e.g. in Excel) and observe the right skew.
- **Next class (tomorrow, 7 o'clock):**
  - Negative binomial
  - Hypergeometric
  - Recap of discrete distributions
  - Then the move to continuous distributions
- The instructor will share the answers to the in-class questions and the proofs of the means and variances in the notes.

<!-- nav -->
← [Session 32 (2026-10-31)](DSM-101-32_2026-10-31_Suman-Majumdar-Prof-Arshad-Prof-Ruchi-Sharma-Prof-Pritee-Sharma.md) · [All lectures](./) · [Session 34 (2026-11-04)](DSM-101-34_2026-11-04_Ruchi-Sharma.md) →
<!-- /nav -->
