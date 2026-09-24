# DSM-101 — Probability & Statistics
## Session 6 — 29 Aug 2026 — Instructor: Suman Majumdar
### Topic: From Binomial → Poisson → Gaussian; Null Hypothesis; CDF; Rarity of Events

---

## 1. Overview

This session traces the logical chain from the **Binomial distribution** (the "mother of all distributions") to the **Poisson distribution** and then to the **Gaussian (Normal) distribution**, focusing not on the algebraic derivations (which are in the posted slides) but on *the assumptions under which each limit holds* and *how each distribution is used in practice*. The lecturer reviews the binomial setup (binary outcomes, probability $p$ and $q = 1-p$), then imposes the Poisson conditions ($p \to 0$, $N \to \infty$, $Np = \lambda$ finite) to obtain $P(n) = \lambda^n e^{-\lambda}/n!$. Along the way he introduces the concept of the **null hypothesis** (with highway-accident, Newton's-apple, and obesity/processed-food examples), the **cumulative distribution function (CDF)** and why it is useful when a PDF cannot be integrated in closed form, and the key Poisson property that **variance = mean** (so an estimate of $\lambda$ immediately gives its uncertainty $\lambda \pm \sqrt{\lambda}$). He then adds the further assumption of *large* $\lambda$ to reach the Gaussian, stresses the crucial conceptual shift from discrete to continuous random variables (for continuous $X$, $P(X = a) = 0$; only $p(x)\,dx$ over an interval is meaningful), and closes with the **68–95–99.7 (sigma) rule** and how tail positions quantify the *rarity* of an observed result — illustrated with a road-accident example and an astronomy photon-detection example. A brief preview: **Bayes' theorem** next class, then **Central Limit Theorem**, then problem sessions.

---

## 2. Topics & Concepts, in Order Taught

### 2.0 Course logistics / plan (stated at the start)
- Four classes remain. Roughly **two more theory classes maximum**; the other **two classes will be problem-discussion sessions**.
- Planned order: (today) Poisson + Gaussian → **Bayes' theorem** (next class, introduced via a worked problem) → problems on Bayes / distributions / practical scenarios → **Central Limit Theorem** if time permits → more problems.
- Derivations are in the slides; the lecture emphasises **assumptions + usefulness**, not algebra.
- Slides to be uploaded to **LMS** the same day.

---

### 2.1 Recap: Binomial distribution — conditions of use
- **Condition 1:** the outcome of a single trial is **binary** (e.g. heads or tails; success or failure).
- One outcome has probability $p$, the other has probability $q$.
- **Condition 2 (sum rule):** if only two outcomes are possible,
$$q = 1 - p$$
- Question answered by the binomial: *if the experiment is performed $N$ times, what is the probability of getting exactly $n$ successes?*
$$P(n) = \binom{N}{n} p^{n} q^{\,N-n} = \frac{N!}{n!\,(N-n)!}\, p^{n}(1-p)^{N-n}$$
- Binomial is a **discrete** distribution.
- Called the **"mother of all distributions"** — Poisson and Gaussian are both obtained as limiting cases of it.

---

### 2.2 Poisson distribution — the extra assumption
Poisson keeps *all* binomial properties (discrete, two outcomes labelled success/failure) and **adds one new condition**:

- **New condition:** the probability of success is very small,
$$p \ll 1 \quad\Longrightarrow\quad q = 1-p \gg p$$
 i.e. **most of the time you fail**; success is a **rare event**.

**Formal limits used:**
- $p \to 0$
- $N \to \infty$
- but the product must stay **finite**:
$$\lambda = N p \quad \text{(finite)} \qquad (\lambda = \text{mean})$$
- Additionally $n \ll N$ (number of successes is tiny compared with number of trials).

**Procedure (sketched, full algebra in slides):** write the binomial $P(n)$, break up the factorials, substitute $Np = \lambda$ so the expression is in terms of $N$, $n$, $\lambda$; impose $n \ll N$; take the limit $p \to 0$, $N \to \infty$. Result:

$$\boxed{P(n) = \frac{\lambda^{n} e^{-\lambda}}{n!}}$$

where $n$ = number of successes, $\lambda = Np$ = mean.

- Named after **Siméon Denis Poisson**.

#### Worked motivating example — highway accidents
- Take a cross-section of a wide highway. Suppose **~1000 cars per hour** cross it → $N = 1000$ (number of trials = number of cars performing the "experiment" of traversing that stretch).
- Observed over one hour: **10 breakdowns/accidents** → $n = 10$ successes (a "success" = the event being studied, here a breakdown).
- Therefore $N - n = 990$ cars had no breakdown.
- $p$ = probability of accident (very small); $q = 1-p \gg p$.
- Interpretation: if the highway is well designed (wide enough, built for foreseeable traffic), accidents are rare **by design** → Poisson regime.

---

### 2.3 The Null Hypothesis (introduced here as a companion concept)
- **Definition (as given):** the default assumption that the rare event will *not* occur — "I assume there won't be any accident." Scenarios where the probability of *not* seeing an event is very high define a natural null hypothesis.
- **Logic of hypothesis testing:** to test a theory, **start with its negation**. If the data strongly violate the null hypothesis, the null is rejected → your theory becomes *credible* (not yet proven) → then design an experiment/model to verify it.
- **Example 1 — Newton / gravity:** Theory: a force pulls the apple down. Null hypothesis: *there is no such force*. Observe many apple trees: do apples fall to earth or fly upward? Large-probability violation of the null ⇒ null rejected ⇒ the force hypothesis is credible ⇒ next, model the components of that force and re-verify.
- **Example 2 — obesity & processed food:** Claim: obese people eat too much processed food. Null hypothesis: *obesity is not linked to processed-food consumption*. Survey a large population, medically certify who is obese, record how frequently each group eats processed food, compare the **percentage of processed food** in the diets of the obese vs. non-obese groups.
- **Example 3 — road design:** Null: accidents on this road are rare (as designed). If a particular stretch shows accidents **more frequent than expected**, the null is violated ⇒ suspect a **design flaw**.
- Key statement: **the Poisson distribution allows us to test these null hypotheses cleanly**, especially for very rare events.

---

### 2.4 Behaviour of the Poisson distribution as $\lambda$ varies
(demonstrated live with the **"Seeing Theory"** interactive web page)
- **Small $\lambda$** (e.g. $\lambda \approx 1$ or less): distribution is **strongly asymmetric**, piled up near $n = 0$; for very small $\lambda$ it looks almost like a **delta function at 0**.
- **Increasing $\lambda$:** the **peak shifts to larger $n$**, and the shape becomes **progressively more symmetric**.
- **Large $\lambda$** (e.g. $\lambda \sim 6$–10 and above): nearly symmetric about the peak — visually approaching a **Gaussian**.
- **Caveat (emphasised):** increasing $\lambda$ alone does **not** give you a Gaussian — Poisson is **discrete**, Gaussian is **continuous**. You must additionally assume **continuity of the variable**.

---

### 2.5 Cumulative Distribution Function (CDF)
- **Motivation:** sometimes you cannot obtain/integrate the full functional form of $p(x)$ over $(-\infty, \infty)$, but you *can* integrate it up to some finite limit.
- **Definition:** for a PDF $p(x)$,
$$C(a) = \int_{-\infty}^{a} p(x)\,dx$$
 i.e. the **area under the curve from $-\infty$ up to $x = a$**.
- **Construction (graphical procedure described):** compute $C(a)$ for $x = a$, plot that value on a new graph (y-axis = CDF, x-axis = $x$); then shift the upper limit to $a_1$, $a_2$, … and plot each value. The curve rises monotonically and **saturates at 1** as $a \to \infty$.
- Any single $C(a) < 1$ because it is not the total area.
- **Normalisation / sum rule of probability (the origin of the CDF's saturation):**
$$\int_{-\infty}^{+\infty} p(x)\,dx = 1$$
- **Practical advantage:** probability that $X$ lies in $[a_1, a_2]$ is obtained by **subtracting two CDF values**:
$$P(a_1 \le X \le a_2) = C(a_2) - C(a_1)$$
- This lets you characterise a distribution's behaviour **even when its analytic form is unavailable/unintegrable**.
- In the Seeing-Theory demo, the **orange curve** overlaid on the Poisson bars is the CDF (the running sum of probabilities), approaching 1.

---

### 2.6 Moments of the Poisson distribution — the key property
- **Mean:** $\;\mu = \lambda = N p$ (students can prove this the same way as for the binomial).
- **★ HOMEWORK / EXERCISE:** *Show that the variance of the Poisson distribution equals its mean.*
$$\sigma^{2} = \lambda = \mu$$
- **Consequence (called "remarkable"):** the **second moment carries no new information beyond the first**. If you know the mean, you automatically know the variance — no extra measurement needed.
- **Uncertainty on a Poisson count:** if you measure $n$ events,
$$\text{result} = n \pm \sqrt{n}\qquad\text{(since } \sigma = \sqrt{\lambda}\text{)}$$

#### Worked numerical example — 5 accidents per hour
- 1000 cars pass per hour; on average **5 accidents observed per hour**.
- Mean: $\mu = \lambda = 5$.
- Because Poisson: $\sigma^{2} = 5 \;\Rightarrow\; \sigma = \sqrt{5}$.
- Quoted measurement with uncertainty:
$$5 \pm \sqrt{5}$$
- **Take-away:** knowing nothing else about the problem, as long as you can establish that it follows a Poisson distribution, **measuring the number of successes immediately gives both the mean and the uncertainty of that estimate.**

- **Application domain mentioned:** astronomy — detecting photons from a very distant source, where receiving a photon *from the target* is extremely rare compared with contamination from other sources. Rarity of success ⇒ Poisson ⇒ measured photon counts immediately come with uncertainties.

---

### 2.7 Gaussian distribution — the additional assumptions
Starting from the Poisson, to reach the Gaussian you need:
1. $N \to \infty$ (number of trials very large) — *same as Poisson*.
2. $p \to 0$ (individual event probability low) — *same as Poisson*.
3. **New:** the mean is **not merely finite but large**: $\lambda = Np \gg 1$.
4. You examine the region **near the mean**: the deviation from $\lambda$ considered is very small compared to $\lambda$.
5. Consequently large values of $n$ matter — successes are no longer necessarily rare — and $P(n)$ becomes effectively a **continuous** distribution.

- Result: a distribution with **mean $\lambda$** and **variance related to $\lambda$** — the Gaussian.
- **Other derivation routes mentioned (not done in class):**
 - Poisson → Gaussian via the **Fourier transform** route.
 - Poisson → Gaussian via the **Central Limit Theorem** (in the CLT limit Poisson becomes Gaussian).
- **Instruction:** *derive the Gaussian from the Poisson yourself at home* — the mathematics and the extra needed information are in the slides/footnotes.

---

### 2.8 ★ Discrete → Continuous: the conceptual trap (flagged as a common exam/problem mistake)
- For a **continuous** random variable $X$ with PDF $p(x)$:
 - **Wrong intuition:** "drop a perpendicular at $x=a$, read off $p(a)$ — that's the probability." **This is completely wrong.**
 - Asking for $P(X = a)$ means putting a **delta function at $a$**: it has **zero width**, hence **zero area under the curve**, hence
$$P(X = a) = 0 \quad \text{(exactly zero, for any specific } a\text{)}$$
 - **The correct question:** what is the probability that $X$ lies between $a$ and $a + dx$?
$$P(a \le X \le a + dx) = \int_{a}^{a+dx} p(x)\,dx$$
 which has a **finite** value.
- For a **discrete** distribution there *are* specific discrete outcomes, so the probability *of a specific value* is well-defined.
- Lecturer's warning: *"people make this mistake quite often while solving the problem."*

---

### 2.9 Properties and uses of the Gaussian
- **Why the mean is often ignored:** you may always choose your **origin/reference point at the mean**, since the Gaussian is **symmetric about its mean** (the classic **bell curve**). Any property derived from the shifted copy holds for the original. Hence textbooks often say: *"as long as I tell you the variance of a Gaussian, I have told you everything about the distribution."*
- Other derivable quantities: **centred variance, centred skewness, centred kurtosis**.
- **Normalisation trick:** integrating a Gaussian from $-\infty$ to $+\infty$ is **not analytically trivial in 1D**. The standard trick is to consider a **two-dimensional Gaussian** and **marginalise over one variable/dimension**, from which the normalisation follows. (Normalisation = requiring $\int_{-\infty}^{\infty} p(x)dx = 1$; if you cannot do the integral you cannot set it to 1.) The **CDF** re-enters here as a route to effective normalisation.

#### The sigma rule (areas under the Gaussian)
For a Gaussian centred at 0 (or at $\mu$) with standard deviation $\sigma$:
- Within $\mu \pm 1\sigma$: **≈ 68.2 %** of the area (**34.1 % on each side**).
- Going from $1\sigma$ to $2\sigma$ adds **13.6 % on each side** → within $\mu \pm 2\sigma$: $68.2 + 2\times 13.6 \approx 95.4\%$.
- (Continuing gives the familiar $\approx 99.7\%$ within $\pm 3\sigma$.)
- **Interpretation:** the width in units of $\sigma$ tells you **how rare an event is**.

---

### 2.10 Rarity of events / where does my result sit? (main practical use of the Gaussian)
General logic presented:
- An experiment whose result follows a Gaussian with mean $\mu$ and width $\sigma$ should yield results within, say, $\mu \pm 3\sigma$.
- If a single measured value is $x = \mu + 1.1\sigma$ (example used: "$\mu + \sigma + 0.1$"), it lies **between $1\sigma$ and $2\sigma$** → not among the most probable results, "one degree of rarity."
- If the result lands far out in the **tail**, it is **very rare / very unlikely** — you would not expect to reproduce it — and you should become **suspicious**.
- Conclusion: by seeing **where in the tail of the Gaussian your new result lies**, you judge whether the new data **belong to the same distribution** as the historical/archival data, or are anomalous.

#### Worked numerical example — accidents on a road
- Historical baseline: out of every 1000 (in one framing, 10,000) cars, on average **100 cars** have some sort of accident → this 100 plays the role of the **mean**, $\mu = 100$.
- You must also ask for the spread: suppose they tell you $\sigma = 5$ cars.
- Then $3\sigma = 3 \times 5 = 15$, so the $\pm 3\sigma$ band is
$$100 + 15 = 115 \quad\text{and}\quad 100 - 15 = 85$$
 i.e. results between **85 and 115** are "normal."
- Now suppose last year on one particular day, of the cars passing, **200 had accidents**.
- 200 lies far outside $\mu \pm 3\sigma$ — out where "the plot almost touches the x-axis" → an **extremely rare event**.
- **Inference:** either this result does **not come from the same distribution** (which was built from 5–10 years of traffic data on that road), or something changed — e.g. **a part of the road was repaired/remodelled** and has become more accident-prone, so the old data set can no longer be used to predict future incidents.

#### Astronomy example (Poisson + Gaussian tails) — assigned as reading
- You point a telescope at a distant star/galaxy. The field also contains **many other stars and galaxies**.
- The target emits photons **spherically symmetrically**; only a tiny fraction reaches Earth, and of that, only a tiny fraction reaches your telescope's (very small) collecting area.
- ⇒ probability of catching a photon from the *target* is **extremely low, almost negligible** ⇒ a **rare-success ⇒ Poisson** problem.
- Method: model what the **other stars contribute** to your telescope and what the **target star** might contribute; then determine whether the count you attribute to the target is **rare or not** using the **tails of the Gaussian**.
- *"I'll leave it to you to read"* — to be re-discussed briefly next class.

---

### 2.11 Central Limit Theorem (CLT) — preview / statement given
- **Why the Gaussian matters most:** because of its role in the CLT. Described as *"one of the most important theorems in applied statistics"* — without it you could not model natural phenomena, human behaviour, or the behaviour of human-made objects.
- **Loose statement given in class:** the CLT deals with the **sum of a large number of independent random variables**.
 > *The sum of a large number of independent random variables follows a Gaussian, regardless of what probability distribution each individual variable follows.*
- **Key point:** you do **not** need to know the individual distributions; the sum always behaves like a Gaussian.
- Full treatment deferred to a later class (time permitting).

---

### 2.12 Resources mentioned
- **Seeing Theory** (interactive visualisation web page) — used live to show Poisson shape vs. $\lambda$ and the CDF overlay.
- **3Blue1Brown** (YouTube channel + website) — recommended for: what Poisson/Gaussian are, moving from Poisson to Gaussian, real-life applications of the Gaussian, plus neural-network lessons, probability, geometry, and Python-based visualisation (they use a specific Python package). Caveat: *some concepts are abstract/involved; skip if not to your taste.*
- **Slides uploaded to LMS** — contain the full Binomial→Poisson and Poisson→Gaussian derivations, the rarity-of-events discussion, and the astronomy example.

---

## 3. Flagged as Important for Exams / Assignments

- **⚠ The exam will contain ONLY problems — "nothing else."** No theory questions. Hence two of the remaining four classes are devoted to problem discussion.
- **Homework / exercise explicitly assigned:** prove that for the Poisson distribution $\sigma^{2} = \mu = \lambda$ (variance = mean). Also, you can/should derive the mean $\lambda = Np$ the same way as done earlier for the binomial.
- **Self-study assigned:** the full derivation of the Gaussian from the Poisson (slides + footnotes); the astronomy photon-counting example (to be revisited briefly next class).
- **Common mistake explicitly warned about:** for a **continuous** random variable, $P(X=a)=0$; only $\int p(x)dx$ over an interval $[a, a+dx]$ is meaningful. *"People make this mistake quite often while solving the problem."*
- **Remember the key formulas:**
 - Binomial: $P(n) = \frac{N!}{n!(N-n)!}p^n(1-p)^{N-n}$, with $q = 1-p$.
 - Poisson: $P(n) = \dfrac{\lambda^n e^{-\lambda}}{n!}$, $\lambda = Np$, valid for $p\to0$, $N\to\infty$, $Np$ finite.
 - Poisson uncertainty: measured count $n$ → quote $n \pm \sqrt{n}$.
 - CDF: $C(a)=\int_{-\infty}^{a}p(x)dx$; $P(a_1\le X\le a_2)=C(a_2)-C(a_1)$; $\int_{-\infty}^{\infty}p(x)dx=1$.
 - Gaussian sigma rule: 68.2 % within $\pm1\sigma$ (34.1 % each side), +13.6 % each side out to $\pm2\sigma$ (≈95 %).
- **Next class:** Bayes' theorem, taught by starting from a problem and solving it — then extracting the meaning of the theorem. (Class resumes Monday.)