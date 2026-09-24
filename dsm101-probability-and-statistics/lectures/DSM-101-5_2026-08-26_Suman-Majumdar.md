# DSM-101 — Session 5 (2026-08-26, Prof. Suman Majumdar)
## Population vs. Sample, Moments, and the Binomial Distribution

---

## 1. Overview

This session bridges the previous lecture's discussion of **moments** of a probability distribution with the practical problem of **estimating** those moments when the underlying distribution is unknown. The lecturer first reviews why moments (zeroth = normalisation, first = mean, second = variance, third = skewness, fourth = kurtosis) are the mathematical handle on a distribution's characteristics, and notes the special property of the Gaussian that only its first two moments carry independent information. He then contrasts the **population** (infinite trials, exact/analytic values) with a **sample** (finite trials, estimated values), using interactive simulations — coin tossing, dice rolling, and card drawing — to show that sample estimates *fluctuate around* the true value and "plateau" once enough samples are collected; the plateau of an estimator plotted against sample size is the practical diagnostic for "how many samples are enough". Real-world motivation is given (insurance risk/premium setting, census-gap sample surveys) for why **sampling strategy** is a whole field of research. The lecture then begins the formal treatment of standard distributions, starting with the **binomial distribution** — "the mother of all distributions" — deriving it from the expansion of $(p+q)^N$, writing down the binomial coefficient as a statistical weight, and deriving its mean $\langle n\rangle = N p_1$. The stated roadmap is: **Binomial → (approximations) → Poisson → (approximations) → Gaussian → Central Limit Theorem.**

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Recap: Moments as the way to characterise a distribution

- Given a probability distribution function (PDF) $P(x)$, if you know its **full functional form** you can (for 1-D) simply plot it; mathematically, you extract its characteristics by computing **moments**.
- **Zeroth moment — normalisation / sum rule.** Verifies the PDF is correctly normalised:
$$\int_{-\infty}^{\infty} P(x)\,dx = 1$$
  (discrete version: $\sum_i P(x_i) = 1$). If you cannot do this analytically, do it **numerically** and check it comes out to $1$ or very close to $1$.
- **First moment — mean / expectation value:**
$$\langle x \rangle = E[X] = \int_{-\infty}^{\infty} x\,P(x)\,dx$$
- **Second moment → variance:**
$$E[X^2] = \int_{-\infty}^{\infty} x^2 P(x)\,dx, \qquad \mathrm{Var}(X) = E[X^2] - \left(E[X]\right)^2$$
  *(Lecturer explicitly flagged a typo on the reference webpage: the first term of the variance formula must have the **square**, i.e. $E[X^2]$, not $E[X]$.)*
- **Third moment → skewness; fourth moment → kurtosis**, and so on. General $k$-th moment:
$$\langle x^k \rangle = \int_{-\infty}^{\infty} x^k P(x)\,dx$$
- **Key property of the Gaussian:** a true Gaussian has only **two unique moments** — the mean and the variance. From the **third moment onwards, all moments can be expressed in terms of the first two**. So skewness, kurtosis etc. are either zero or fully determined by mean and variance. ⇒ *For a genuinely Gaussian PDF, mean and variance are the only information you need.*

### 2.2 When you do **not** know the functional form: sampling

- In most real problems you cannot evaluate $P(x)$ at all $x \in (-\infty, \infty)$.
- Two consequences: (i) verifying normalisation becomes non-trivial, (ii) moments must be **estimated**, not **calculated**.
- **Sampling** = probing $P(x)$ at a finite, hopefully *representative*, set of values of $x$.
- Sampling is an active research field in applied statistics; new techniques appear constantly, especially for high-dimensional problems (PDF depending on $n$ variables with $n$ large).
- **Terminology / core distinction:**
  - **Population** → infinite number of trials → population mean, population variance (never actually attainable).
  - **Sample** → finite number of trials → **sample mean**, **sample variance** (estimates).
- **Uniform sampling** works when all outcomes are equally probable / the PDF is simple; for complex, multi-peaked PDFs uniform sampling is **not optimal** and clever sampling schemes are required.

### 2.3 Worked simulation 1 — Coin toss (unbiased coin)

True population: $P(\text{head}) = P(\text{tail}) = 0.5$ (50%/50%).

Observed in the live simulation:

| Number of flips | Result |
|---|---|
| 1 | head → 100% heads (1 out of 1) |
| 2 | 50 / 50 |
| 102 | 50 heads, 52 tails → $0.49$ / $0.51$ |
| ~200 | $0.52$ / $0.48$ |
| 302 | $0.51$ / $0.49$ |

- **Lesson:** estimates from a finite sample **never exactly** match the ideal value; they give a *close estimate*. How close/how good the estimate is can be judged from the **variance** of the distribution.
- The sample must be "large enough" to represent the underlying population — the justification for this comes from the **Central Limit Theorem** (to be covered later).

### 2.4 Worked simulation 2 — Rolling a die (expectation value)

- **Definition given:** the expectation value of a random variable is *"the number that attempts to capture the centre of the random variable's distribution"* — i.e., the value of $x$ around which most outcomes cluster (the location of the peak of $P(x)$).
- Fair die: each of the 6 faces has probability
$$p = \frac{1}{6} \approx 0.166\ldots \approx 0.17$$
- Because the variable is **discrete**, the integral is replaced by a sum, and since all probabilities are equal, $\tfrac16$ factors out:
$$E[X] = \sum_{i=1}^{6} x_i\,P(x_i) = \frac{1}{6}\,(1+2+3+4+5+6) = \frac{21}{6} = 3.5$$
- The simulation plots the **running average** versus **number of rolls**; the dashed reference line sits at $3.5$.
- Observed behaviour: the running mean **fluctuates around $3.5$** and never lands exactly on it, but by roughly **100 rolls** the curve **flattens/plateaus** with only small oscillations.
- **Classroom aside (simulation artefact):** the first roll was always a 6 because the animation uses **pseudo-random numbers** with a **hard-coded seed** in the underlying Python script (scripts available on the linked GitHub page). Not a statistical effect.

> **Practical diagnostic — "how many samples are enough?"**
> Plot your estimated statistic (mean, variance, …) as a function of the number of samples/trials. When the curve **flattens out / saturates / only oscillates mildly** around some level, you have collected enough samples. In real problems the true (dashed-line) value is unknown — but the **shape of the running-estimate curve** still tells you when you have converged.
> - Few possible outcomes (e.g. 6 for a die, 2 for a coin — **discrete** variables) ⇒ saturation after only ~hundreds of samples.
> - Many possible outcomes / high-dimensional problems ⇒ far more samples needed.
> The fluctuation about the true expectation value is explained by the **variance** of the distribution.

### 2.5 Worked simulation 3 — Drawing cards (variance)

Setup: 10 cards of a single suit with values $1,2,\dots,10$, all equally probable, drawn at random (with replacement).

- The **analytical** (population) variance for this uniform-on-$\{1,\dots,10\}$ case was quoted in class as **≈ 8.5**.
  *(Note: the exact textbook value for the discrete uniform on $1..10$ is $\frac{10^2-1}{12} = 8.25$; the simulation's converged values below hover near this. Use $\mathrm{Var} = E[X^2] - (E[X])^2$ if asked to compute it yourself.)*
- Running estimate of the variance from the simulation:

| Number of draws | Average (sample) variance |
|---|---|
| 1 | (meaningless — variance from a single draw is ill-defined) |
| 2 | $1.25$ |
| 100 | $9.25$ |
| 200 | $8.49$ |
| ~300 | $8.32$ – $8.35$ |

- **Lesson:** as the sample size grows, the running variance settles into a band; the value about which it saturates is taken as the variance of the underlying distribution. Combined with the converged mean, you can then state: *"for this PDF, this many samples suffice to recover mean and variance."*

### 2.6 Why sampling strategy matters — real-world examples

- **Insurance (car/health):** a new customer is **one sample drawn from a giant population**. Many variables matter (the car itself, the driver, driving skill, health, …). You estimate moments (means, variances) from **historical data** for the industry/company, then place the new individual within that risk PDF to set risk class and **premium**. How the historical data was sampled therefore plays a "humongous role".
- **Surveys:** the choice of survey questions and demographic to survey *is* the sampling strategy.
- **Census / sample surveys:** a census is meant to run every ~10–15 years and underpins welfare and policy decisions (not just head-counting). When no census has been run for 15–20 years, governments use **sample surveys** — a sampling strategy picks a group based on various criteria/variables and historical experience, and the collected data feeds policy-making. The sampling algorithm is critical.
- **Course note:** sampling strategies and designing sampling algorithms are treated in depth in **DSM-407**, which is **compulsory for all**.

### 2.7 Why study "textbook" distributions at all?

- Real-life PDFs will **not** exactly be Gaussian/binomial/Poisson.
- But standard distributions have known characteristics that can be applied **approximately**, under **stated conditions and assumptions**, to real PDFs to extract inference/conclusions. That is the justification for studying them.
- **Plan for this course:** three standard distributions —
  1. **Binomial** (discrete) → 2. **Poisson** (discrete, via approximations to binomial) → 3. **Gaussian** (continuous, via approximations to Poisson) → then the **Central Limit Theorem**, understood through their properties.

---

## 3. The Binomial Distribution

### 3.1 Setting

- Applies to **binary-outcome** events: win/lose, head/tail — exactly **two** possible outcomes per trial.
- Binomial is called the **"mother of all probability distribution functions."**
- Setup: perform an experiment $N$ (capital) times; count $n$ (small) **successes**. Define head = success, tail = failure (the labelling is arbitrary).
- Let
  - $p$ (or $p_1$) = probability of success (attribute present),
  - $q$ (or $p_2$) = probability of failure (attribute absent), with $q = 1-p$.
- **Question answered by the binomial:** *If I toss the coin 100 times, what is the probability of getting exactly 52 heads?*
- **Equivalence:** tossing one identical coin $N$ times ≡ tossing $N$ identical coins simultaneously.

### 3.2 Derivation from the $N=2$ case

Two coins tossed together. Raw outcomes: HH, HT, TH, TT. If the coins are identical, **HT and TH are indistinguishable** (only the *number* of heads matters).

Because successive tosses are **independent**, joint probabilities factorise:

$$P(HH) = P(H)\,P(H)$$
$$P(HT \text{ or } TH) = P(HT) + P(TH) = P(H)P(T) + P(T)P(H) = 2\,P(H)\,P(T)$$
$$P(TT) = P(T)\,P(T)$$

These are exactly the terms of the binomial expansion:

$$\left(P(H) + P(T)\right)^2 = P(H)^2 + 2P(H)P(T) + P(T)^2$$

Generalising: if the experiment is performed $3$ times the exponent becomes $3$; for $N$ trials the exponent becomes $N$. The multiplicities ($1, 2, 1, \dots$) are simply the **coefficients of the binomial expansion of $(p+q)^N$**.

### 3.3 The binomial formula

The number of permutations giving $n$ successes is the $n$-th coefficient in the expansion of $(p+q)^N$; each such permutation has probability $p^{n} q^{\,N-n}$ (since $n$ successes ⇒ $N-n$ failures). Hence

$$\boxed{\;P(n) = \binom{N}{n}\, p^{\,n}\, q^{\,N-n}, \qquad 0 \le n \le N \;}$$

with the **binomial coefficient**

$$\binom{N}{n} = \frac{N!}{n!\,(N-n)!}$$

Using $q = 1-p$:

$$P(n) = \frac{N!}{n!\,(N-n)!}\; p^{\,n}\,(1-p)^{\,N-n}$$

- **Interpretation:** the binomial coefficient $\binom{N}{n}$ acts as the **statistical weight** of the specific outcome "exactly $n$ successes".
- Because the variable is discrete/binary, the distribution appears as a set of discrete steps.
- As $n \to N$ (demanding more and more successes out of the same $N$ trials), $P(n)$ falls off — hence the distribution peaks at some intermediate $n$ and decays on both sides.

### 3.4 Mean of the binomial — quick argument

Let each trial give an indicator variable $x_i$ with
$$x_i = 1 \ \text{(success)}, \qquad x_i = 0 \ \text{(failure)}$$
Then the number of successes is $n = \sum_i x_i$, and since $E[x_i] = p_1$ for every trial,

$$\langle n \rangle = E\!\left[\sum_{i=1}^{N} x_i\right] = \sum_{i=1}^{N} E[x_i] = N\,p_1$$

$$\boxed{\;\langle n \rangle = N p_1 \;}$$

i.e. **mean = (total number of trials) × (probability of success)**.

### 3.5 Mean of the binomial — the "robust/tedious" derivation

For a **discrete** variable the moment integral $\int_{-\infty}^{\infty}$ is replaced by a **summation**, and the limits are *not* $\pm\infty$: $n$ can only run over the physically allowed range $0 \le n \le N$:

$$\langle n \rangle = \sum_{n=0}^{N} n\,P(n) = \sum_{n=1}^{N} n\,\frac{N!}{n!\,(N-n)!}\,p_1^{\,n} p_2^{\,N-n}$$

(then substitute $p_2 = 1-p_1$, use $n! = n\,(n-1)!$ to cancel the factor $n$, and apply the sum rule) $\;\Rightarrow\; \langle n \rangle = N p_1$.

**Q&A points raised in class:**
- *Why did the integral become a summation?* Because the random variable is discrete and is not free to range over $(-\infty,\infty)$ — here it is restricted by the finite number of trials $N$. Whenever we speak of an *expectation value estimated from a finite number of samples/trials*, the sum runs over those finite trials.
- *Why does the lower limit change from $n=0$ to $n=1$?* Two complementary answers given:
  1. There is a factor $n$ multiplying the terms; writing $n! = n\,(n-1)!$ cancels the $n$, leaving $(n-1)!$ — which is **undefined at $n=0$** (you would need $(-1)!$). Hence the sum starts at $n=1$.
  2. The $n=0$ term contributes nothing to $\sum n P(n)$ anyway (it is the "zero successes" scenario).
  *(This was initially set as a think-about-it exercise and then resolved by a student in class — see §5.)*

### 3.6 Shape of the binomial and the link to the Gaussian

- The distribution **peaks around $n = N p_1$**.
- **As $N$ becomes large, the shape of the envelope around the maximum becomes more and more symmetrical and tends towards a Gaussian distribution.** This is an explicit **manifestation/implication of the Central Limit Theorem** (to be developed later).
- **Symmetry vs. bias:**
  - Unbiased coin ⇒ $p_1 = p_2$ ⇒ symmetric distribution.
  - Biased coin ⇒ $p_1 \ne p_2$; if $p_1 > p_2$ the distribution is **asymmetric**, with more weight on the success side (peak shifted toward larger $n$).

---

## 4. Roadmap Announced for Coming Lectures

- **Next class:** Poisson distribution and Gaussian distribution.
  - Current stage: **binary** discrete outcomes (binomial).
  - Next: **non-binary but still discrete** outcomes (Poisson).
  - Then: **continuous** outcomes (Gaussian) — how we get there from the discrete cases.
- **Then:** the **Central Limit Theorem**.
- Materials for this session to be uploaded to the **LMS**.

---

## 5. Exam / Assignment Flags

- ⚠️ **Central Limit Theorem:** the lecturer has prepared a full derivation but says *"that is not very important — rather you should focus on the **implications** of the Central Limit Theorem."* Expect questions on consequences/uses, not the proof.
- ⚠️ **Think-about-it exercise set in class:** *Why does the summation in the binomial-mean derivation start at $n = 1$ rather than $n = 0$?* (Answer arrived at in class: the $n$ in $n!$ cancels against the explicit factor $n$, leaving $(n-1)!$, which does not exist for $n=0$; equivalently, $n=0$ contributes nothing.)
- ⚠️ **Known errata on the reference website's animations/documentation:** the variance formula there is missing the square — it must be $\mathrm{Var}(X) = E[X^2] - (E[X])^2$. Also, the dice animation always starts with a 6 due to a hard-coded random seed (a coding flaw, not statistics). The Python scripts for the animations are on the linked GitHub page.
- 📌 **Course logistics:** sampling techniques / designing sampling algorithms are the main subject of **DSM-407**, which is **compulsory for everyone** — so detailed sampling algorithms are not examined here.

---

## 6. Formula Sheet (all formulas used in this session)

$$\int_{-\infty}^{\infty} P(x)\,dx = 1 \quad \text{(zeroth moment / normalisation, sum rule)}$$

$$\langle x \rangle = E[X] = \int_{-\infty}^{\infty} x\,P(x)\,dx \quad \text{(first moment, mean)}$$

$$\langle x^k \rangle = \int_{-\infty}^{\infty} x^k P(x)\,dx \quad (k\text{-th moment})$$

$$\mathrm{Var}(X) = E[X^2] - \left(E[X]\right)^2 \quad \text{(second central moment)}$$

Discrete analogue: $\displaystyle E[X] = \sum_i x_i P(x_i)$, $\displaystyle \sum_i P(x_i)=1$.

**Fair die:** $\displaystyle P(x_i)=\frac16$, $\;E[X]=\frac16(1+2+3+4+5+6)=3.5$

**Two-coin expansion:** $\left(P(H)+P(T)\right)^2 = P(H)^2 + 2P(H)P(T) + P(T)^2$

**Binomial PDF:** $\displaystyle P(n)=\binom{N}{n}p^{\,n}q^{\,N-n}=\frac{N!}{n!(N-n)!}p^{\,n}(1-p)^{\,N-n},\quad 0\le n\le N,\; q=1-p$

**Binomial mean:** $\displaystyle \langle n\rangle=\sum_{n=1}^{N} n\,P(n)=N p_1$

**Indicator-variable construction:** $x_i\in\{0,1\}$, $E[x_i]=p_1$, $n=\sum_{i=1}^{N}x_i \Rightarrow \langle n\rangle = N p_1$

**Large-$N$ limit:** binomial $\xrightarrow[\;N\to\infty\;]{}$ symmetric, Gaussian-like envelope about $n=Np_1$ (Central Limit Theorem in action).