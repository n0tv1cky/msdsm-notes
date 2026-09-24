# DSM-101 — Probability & Statistics
## Session 10 (2026-09-07) — Instructor: Suman Majumdar
### Topic: Revisiting the Central Limit Theorem + Bayes' Theorem Problem Clinic

---

## 1. Overview

This session was driven by a student question emailed to the instructor, and is essentially a **conceptual re-explanation of the Central Limit Theorem (CLT)** using the teacher-salary problem from the previous lecture. The key distinction hammered home is between (a) the probability that *one randomly drawn individual* falls below some value — governed by the **population** standard deviation $\sigma$ — and (b) the probability that the *mean of a sample of $n$ individuals* falls below that value — governed by the **standard error** $\sigma/\sqrt{n}$. The instructor gives a graphical picture of how the sample mean $\mu_s$ converges to the population mean $\mu$ while the *uncertainty* on that estimate shrinks as $1/\sqrt{n}$, emphasising that we never have direct access to the population, only to sample estimates. A second CLT problem (sum of 50 bank-teller service times) is worked out. The rest of the class is a sequence of **Bayes' theorem** worked examples: the multiple-choice-guessing problem, a criminal-investigation / circumstantial-evidence problem (including a Bayesian *update* when the evidence itself becomes uncertain), and a COVID-era-style medical-test problem showing why a low false-positive rate matters far more than high sensitivity when the disease prevalence is low. Ends with exam logistics.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Set-up: Population vs. Sample

- The quoted mean and standard deviation of a distribution are treated as **population parameters** $\mu$, $\sigma$ (the "truth"), even though in reality they were themselves estimated by some survey/sampling.
- Key philosophical point repeated several times: *we never have access to the population.* All we ever have are the **sample mean** and **sample variance**. The CLT is the bridge from those estimates back to the population.

### 2.2 Worked Example 1 — Teacher Salaries (the CLT demonstration)

**Given:** Average salary of a teacher in a region is $\mu = 52{,}174$. Salaries are Normally distributed with $\sigma = 7{,}500$.

**Question (a):** What is the probability that a *randomly selected* teacher makes less than \$50,000 per year?

- Draw the population distribution $P(x)$, Gaussian, centred at $\mu = 52{,}174$, width set by $\sigma = 7{,}500$.
- A single random draw is most likely to land near the mean; the probability of landing within $1\sigma$, $2\sigma$, $3\sigma$ of the mean increases as you widen the band (covering essentially the whole distribution by $3\sigma$).
- Measure the distance of 50,000 from the mean **in units of $\sigma$**:
$$z = \frac{50{,}000 - \mu}{\sigma} = \frac{50{,}000 - 52{,}174}{7{,}500} = \frac{-2{,}174}{7{,}500} \approx -0.29$$
- The answer is the **area under the curve from $-\infty$ to 50,000**:
$$P(X < 50{,}000) = \int_{-\infty}^{50{,}000} P(x)\,dx = \Phi(-0.29) \approx 0.38 \quad (\approx 38\%)$$

**Question (b):** If we sample 100 teacher salaries, what is the probability that the **sample mean** is less than \$50,000 per year?

- The population is unchanged ($\mu$, $\sigma$ as before). What changes is *which random variable* we are asking about: $\bar{X}$, not $X$.
- **CLT statement used:** in the limit of large sample size, the sample mean approaches the population mean,
$$\mu_s \equiv \bar{X} \longrightarrow \mu \quad \text{as } n \to \infty$$
- But the spread of the *sampling distribution of the mean* is **not** $\sigma$. It is the **standard error**:
$$\boxed{\ \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}\ } \qquad \text{equivalently} \qquad \sigma^2_{\bar{X}} = \frac{\sigma^2}{n}$$
- For $n = 100$: $\sigma_{\bar{X}} = \dfrac{7{,}500}{\sqrt{100}} = \dfrac{7{,}500}{10} = 750$.
- Hence
$$z = \frac{50{,}000 - 52{,}174}{750} \approx -2.90 \qquad\Rightarrow\qquad P(\bar{X} < 50{,}000) = \Phi(-2.90) \approx 0.0019$$
- **Interpretation contrast:**
 - Case (a) asks: *if you take one random sample, where is it likely to be found?*
 - Case (b) asks: *how certain are you that your estimate of the population mean is correct?*

> **ASR/lecture caveat:** during the live explanation the instructor briefly rambled about "treating each sample as a Poisson-like point event" and wrote something like "$\sigma_s = $ sample mean $/\sqrt{n}$". A student correctly interrupted to say it should be $\sigma/\sqrt{n}$, and the instructor agreed. **Use $\sigma_{\bar X}=\sigma/\sqrt{n}$.** (The Poisson digression was about the case where the true $\sigma$ is unknown and must itself be estimated from the sample.)

### 2.3 Graphical Picture: Shrinking the Uncertainty Envelope

- Sample $n$ points from $P(x)$. Because the sampling is unbiased, more points land near $\mu$ than in the tails — the sample "traces out" the underlying pdf.
- As $n$ increases ($100 \to 10{,}000 \to 10^6$):
 - The **sample mean $\mu_s$ barely moves** after a certain point — it stays essentially pinned near the true $\mu$.
 - The **uncertainty $\sigma_s \propto 1/\sqrt{n}$ keeps shrinking.**
- Example given: with $n = 100$, $\sigma_s \propto \dfrac{1}{\sqrt{100}} = \dfrac{1}{10}$ — a wide uncertainty band. Go to $n = 10^4$ or $10^6$ and the band collapses to a narrow (green) region: you are now much more confident that $\mu$ lies inside it.
- Slogan: **your measurement may be *accurate* with 10 samples by luck, but it will not be *certain*.** Confidence / degree of belief grows with $n$.

**Q&A raised in class:** *Is there a standard sample size?*
> **No.** There is no universal sample size; it depends on the problem and on the underlying probability distribution. Best practice: always quote **both** the sample mean **and** the sample variance for any measured quantity, and if you have the luxury, repeat the experiment with progressively larger samples — you will see the mean fluctuate slightly while the sample variance steadily shrinks.

### 2.4 Worked Example 2 — Bank Teller (CLT for a *sum* of i.i.d. variables)

**Given:** A bank teller serves customers one at a time (serially). The service time $X_i$ for customer $i$ has
$$\mathbb{E}[X_i] = \mu = 2 \text{ minutes}, \qquad \operatorname{Var}(X_i) = \sigma^2 = 1 \ (\text{so } \sigma = 1)$$
Service times for different customers are **independent**. Let $Y$ be the total time to serve 50 customers:
$$Y = \sum_{i=1}^{50} X_i$$

**Question:** $P(90 < Y < 110)$?

- Naive expectation: if every customer took exactly the mean time, $Y = n\mu = 50 \times 2 = 100$ minutes.
- Standardise the sum (CLT for sums):
$$Z = \frac{Y - n\mu}{\sqrt{n}\,\sigma} \sim N(0,1) \quad \text{approximately}$$
- Lower limit: $\dfrac{90 - 100}{\sqrt{50}\cdot 1} = \dfrac{-10}{\sqrt{50}} = -\sqrt{2} \approx -1.414$
- Upper limit: $\dfrac{110 - 100}{\sqrt{50}\cdot 1} = \dfrac{+10}{\sqrt{50}} = +\sqrt{2} \approx +1.414$
- So
$$P(90 < Y < 110) = P(-\sqrt{2} < Z < \sqrt{2}) = \Phi(\sqrt{2}) - \Phi(-\sqrt{2}) \approx 0.8427$$
- **Method note:** this is just the difference of two CDFs — evaluate the cumulative distribution at 110 and at 90 and subtract.
- **Sanity check against the empirical rule:** $\pm 1\sigma$ covers $\approx 68.2\%$ ($34\% + 34\%$); the next band contributes $\approx 13.6\%$ per side. $84.27\%$ sits a bit beyond $1\sigma$ but well inside $2\sigma$ — consistent with $z = \pm 1.414$.
- **Interpretation:** it is highly likely that total service time falls in 90–110 minutes, but the interval is wide, i.e. the associated uncertainty is large.

### 2.5 Bayes' Theorem — general form used all session

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}, \qquad P(B) = P(B\mid A)P(A) + P(B \mid A^{c})P(A^{c})$$

The denominator is the **marginalisation** (law of total probability). For continuous parameters the instructor wrote it as
$$P(X \mid C) = \frac{P(C \mid X)\,P(X)}{\int P(C\mid X)\,P(X)\,dX}$$
with the pieces named: **likelihood $\times$ prior / evidence**.

### 2.6 Worked Example 3 — Multiple-Choice Test (Guessing)

**Setup:** A student either *knows* the answer or *guesses* it (binary).
- $P(K) = p$ — probability the student knows the answer.
- $P(K^c) = 1-p$ — probability the student guesses.
- A guesser is correct with probability $1/m$, where $m$ = number of multiple-choice alternatives (3 options $\Rightarrow$ 1/3, 4 options $\Rightarrow$ 1/4, etc.).

Let $C$ = event "answers correctly", $K$ = event "knows the answer".

**Question:** $P(K \mid C)$ — probability the student *knew* the answer, given they answered correctly.

$$P(K \mid C) = \frac{P(C\mid K)\,P(K)}{P(C\mid K)P(K) + P(C \mid K^{c})P(K^{c})}$$

- $P(C \mid K) = 1$ (if you know it, you get it right) $\Rightarrow$ numerator $= 1\cdot p = p$.
- $P(C \mid K^{c}) = 1/m$, $P(K^{c}) = 1-p$.

$$\boxed{\,P(K\mid C) = \frac{p}{p + \frac{1}{m}(1-p)} = \frac{mp}{1 + (m-1)p}\,}$$

**Numerical case:** $m = 5$ options, $p = 1/2$ (treat "knows / doesn't know" as 50-50):
$$P(K\mid C) = \frac{5 \times 0.5}{1 + 4\times 0.5} = \frac{2.5}{3} = \frac{5}{6} \approx 0.833$$

**Interpretation given:** the probability of being right by pure guessing is only $1/6$ vs. $5/6$ for genuine knowledge — this is *why* objective/MCQ-based competitive exams are trustworthy instruments (absent paper leaks): a correct answer really does indicate knowledge.

### 2.7 Worked Example 4 — Criminal Investigation (Circumstantial Evidence)

**Setup:** An inspector is **60% convinced** of a suspect's guilt. New evidence shows the criminal has a certain characteristic (left-handedness, baldness, brown hair, a particular *modus operandi*, hair found at the scene, etc.). **20% of the population** possesses this characteristic. The suspect turns out to be in that group.

Let $G$ = "suspect is guilty", $C$ = "suspect possesses the criminal's characteristic".

**Priors/likelihoods:**
- $P(G) = 0.6$, $P(G^{c}) = 0.4$
- $P(C \mid G) = 1$ (if the suspect is the guilty party, they necessarily have the criminal's established characteristic)
- $P(C \mid G^{c}) = 0.2$ (a random non-guilty person from the population has it with prob. 0.2)

$$P(G \mid C) = \frac{P(C\mid G)P(G)}{P(C\mid G)P(G) + P(C\mid G^{c})P(G^{c})} = \frac{1 \times 0.6}{(1)(0.6) + (0.2)(0.4)} = \frac{0.6}{0.6 + 0.08} = \frac{0.60}{0.68} \approx 0.88$$

**Interpretation:**
- Belief rises from $0.60 \to \approx 0.88$. **Bayes' theorem lets you quantify the *weight* of circumstantial evidence.**
- But it is **not** certainty: there remains $\approx 12\%$ probability the suspect is innocent. You cannot convict on this alone; you need additional evidence. What this result *does* justify is continuing the investigation — grilling the suspect, questioning other parties, collecting more evidence.

### 2.8 Worked Example 4b — Bayesian **Update** When the Evidence Itself Is Uncertain

**Modification:** The new evidence is open to interpretation — it only shows it is **90% likely** that the criminal possesses the characteristic (10% uncertainty).

Now $P(C \mid G) = 0.9$ instead of $1$; $P(G) = 0.6$, $P(C\mid G^{c}) = 0.2$, $P(G^{c}) = 0.4$ are unchanged.

$$P(G\mid C) = \frac{(0.9)(0.6)}{(0.9)(0.6) + (0.2)(0.4)} = \frac{0.54}{0.54 + 0.08} = \frac{0.54}{0.62} \approx 0.871$$

**Interpretation:** the posterior drops slightly (from $\approx 0.88$ to $\approx 0.87$). Bayes' theorem **updates** the degree of belief rather than discarding it wholesale — it does not suddenly declare the person innocent; it nudges the guilt probability.

### 2.9 Class Discussion Point — a common conceptual trap

A student (Ashraful) asked whether $P(C\mid G) + P(C \mid G^{c})$ should equal 1.

- **Answer: No.** Conditional probabilities only sum to 1 when you **hold the conditioning event fixed and vary the event**:
$$P(C\mid G) + P(C^{c}\mid G) = 1 \qquad \checkmark$$
$$P(G) + P(G^{c}) = 1 \qquad \checkmark$$
$$P(C\mid G) + P(C\mid G^{c}) \ne 1 \quad \text{in general} \qquad \times$$
- In $P(C\mid G)$ and $P(C\mid G^{c})$ the *conditioning* event changes — these are probabilities over two **different sub-populations** (the guilty group and the not-guilty group), so there is no reason for them to add to 1.
- Also clarified: the 20% figure is "has the characteristic **and** is not a criminal", because essentially the whole population is non-guilty (only a tiny fraction, ~1%, commits the crime).

### 2.10 Worked Example 5 — Medical Test / Base-Rate Problem (the COVID vaccine-&-test-efficacy analogue)

**Setup:** A laboratory blood test is **99% effective** at detecting a disease when it is present (sensitivity). The test also yields a **false positive rate of 1%** — i.e. 1% of healthy people test positive. **0.5% of the population** actually has the disease.

Let $D$ = "tested person has the disease", $E$ = "test result is positive".

- $P(E \mid D) = 0.99$
- $P(D) = 0.005$, $P(D^{c}) = 0.995$
- $P(E \mid D^{c}) = 0.01$

$$P(D\mid E) = \frac{P(E\mid D)P(D)}{P(E\mid D)P(D) + P(E\mid D^{c})P(D^{c})} = \frac{(0.99)(0.005)}{(0.99)(0.005) + (0.01)(0.995)}$$
$$= \frac{0.00495}{0.00495 + 0.00995} = \frac{0.00495}{0.01490} \approx 0.332$$

**Result: only about 33% of people who test positive actually have the disease** — despite the test being "99% effective".

**Now improve the false positive rate** to $0.01\% = 0.0001$:
$$P(D\mid E) = \frac{(0.99)(0.005)}{(0.99)(0.005) + (0.0001)(0.995)} = \frac{0.00495}{0.00495 + 0.0000995} \approx 0.98$$

**Interpretation (explicitly linked to COVID testing):**
- Because the probability of *not* having the disease is so overwhelmingly large in the population, even a tiny false-positive rate generates a huge absolute number of false positives that swamps the true positives.
- Therefore **driving the false-positive rate down matters more than sensitivity** for the positive predictive value. As $P(E\mid D^{c}) \to 0$, the ratio $P(D\mid E) \to 1$.
- This is exactly why COVID testing used a two-stage protocol: a quick (rapid antigen) test with a relatively high false-positive rate (~1%), followed by a slower confirmatory test (antibody/RT-type, ~3 days) with a far lower false-positive rate (~0.01%) to weed out false positives.
- Same logic applied to the "99% efficacy" claims made by different vaccine manufacturers from different clinical trials during COVID.

---

## 3. Formula Sheet (everything used today)

| Concept | Formula |
|---|---|
| Probability from pdf | $P(X < a) = \int_{-\infty}^{a} P(x)\,dx$ |
| Standardisation (single draw) | $z = \dfrac{x - \mu}{\sigma}$ |
| **CLT — sample mean** | $\bar{X} \to \mu$ as $n\to\infty$; $\bar{X} \sim N\!\left(\mu, \frac{\sigma^2}{n}\right)$ |
| **Standard error** | $\sigma_{\bar{X}} = \dfrac{\sigma}{\sqrt{n}}$, $\quad \sigma^2_{\bar{X}} = \dfrac{\sigma^2}{n}$ |
| Standardisation (sample mean) | $z = \dfrac{\bar{x} - \mu}{\sigma/\sqrt{n}}$ |
| **CLT — sum of $n$ i.i.d.** | $Y = \sum_{i=1}^{n} X_i$, $\ \mathbb{E}[Y] = n\mu$, $\ \operatorname{SD}(Y) = \sqrt{n}\,\sigma$, $\ Z = \dfrac{Y - n\mu}{\sqrt{n}\,\sigma} \sim N(0,1)$ |
| Probability in an interval | $P(a<Y<b) = F(b) - F(a)$ |
| Empirical rule | $\pm1\sigma \approx 68.2\%$ ($34\%+34\%$); next band $\approx 13.6\%$ per side |
| **Bayes' theorem** | $P(A\mid B) = \dfrac{P(B\mid A)P(A)}{P(B\mid A)P(A) + P(B\mid A^{c})P(A^{c})}$ |
| Bayes (continuous form) | $P(X\mid C) = \dfrac{P(C\mid X)P(X)}{\int P(C\mid X)P(X)\,dX}$ |
| Valid complement identity | $P(C\mid G) + P(C^{c}\mid G) = 1$ (NOT $P(C\mid G)+P(C\mid G^{c})$) |
| MCQ guessing result | $P(K\mid C) = \dfrac{p}{p + \frac{1}{m}(1-p)} = \dfrac{mp}{1+(m-1)p}$ |

**Numerical answers to remember:**
- Teacher salary, single draw: $z \approx -0.29 \Rightarrow \approx 0.38$
- Teacher salary, $n=100$ sample mean: $\sigma_{\bar X} = 750$, $z \approx -2.90 \Rightarrow \approx 0.0019$
- Bank teller: $\mathbb{E}[Y]=100$, $\operatorname{SD}(Y)=\sqrt{50}$, $z=\pm\sqrt{2} \Rightarrow 0.8427$
- MCQ, $m=5$, $p=0.5$: $5/6 \approx 0.833$
- Criminal: $0.60/0.68 \approx 0.88$; with 90% evidence reliability: $0.54/0.62 \approx 0.87$
- Blood test: $\approx 0.33$ at 1% FPR; $\approx 0.98$ at 0.01% FPR

---

## 4. Flagged for Exams / Assignments

- **The instructor explicitly said: "similar sort of problems will be there in the exam."** He has a set of additional problems with solutions and discussion (plus some *unsolved* ones) listed in the slides — **go through all of them at least once.** He will **post these problems**.
- **Source of problems:** many are taken from **Sheldon Ross's book**; a few from other sources.
- **Advice given:** "spend a bit more time solving problems."
- **Midsem logistics:**
 - Approximately **10 more lectures** from now, delivered by **Dr. Arshad**, before the midsem.
 - **Syllabus = everything covered by Prof. Majumdar so far + everything Dr. Arshad covers.**
 - The **entire midsem exam will be conducted via the LMS**; exact procedure to be announced.
- **Conceptually most likely to be tested (based on emphasis):**
 1. Distinguishing $P(X < a)$ for a single observation vs. $P(\bar{X} < a)$ for a sample mean — i.e. knowing when to divide $\sigma$ by $\sqrt{n}$. This was the whole reason the session started.
 2. CLT applied to a **sum** ($\sqrt{n}\sigma$) vs. a **mean** ($\sigma/\sqrt{n}$).
 3. Bayes' theorem with correct marginalisation in the denominator, and the trap that $P(C\mid G)+P(C\mid G^{c}) \neq 1$.
 4. The base-rate / false-positive insight in medical testing.