# DSM-101 — Probability & Statistics
## Session 4 — 2026-08-24 — Instructor: Suman Majumdar

---

## 1. Overview

This session picks up from the previous lecture's discussion of probability distribution functions and marginalization, and builds up the concept of the **probability density function (PDF)** from first principles. The instructor motivates the PDF as the continuous limit of a **histogram** ("a poor person's probability density function"), walking through the mechanics of binning data and assigning bin heights by frequency with explicit numerical examples. He then develops the **mass/volume analogy** for probability density, explains why an "average probability density" is meaningless, and uses a height–weight–BMI example to explain when a **multivariate (joint) distribution** is actually required (i.e. when the observable is derived from more than one random variable), including 3D surfaces, contour/iso-contour plots, and how marginalization recovers a 1-D slice. The second half moves to the **population vs. sample** distinction: since we can never access the infinite population, we approximate its distribution from finite samples. This leads into **statistics as data reduction** and the formal definition of **moments** as the minimum set of numbers needed to fully specify a distribution — zeroth moment (sum rule), first moment (mean), higher moments, **centered moments**, skewness and kurtosis, and why the **Gaussian** needs only μ and σ. The lecture ends by flagging that the next class will cover estimating moments from finite samples, and that the "how large is large enough?" question will be answered later via the **Central Limit Theorem**.

---

## 2. Topics & Concepts, in order taught

### 2.0 Administrative / Course Logistics
- **LMS is now live**: `lms.iiti.ac.in` — log in with your **IIT Indore email ID**.
- Course page: **DSM-101 Probability and Statistics**. Lecture slides for the **first three lectures** already uploaded; slides will be updated after each session.
- **Everyone must log in at least once and verify their account works.** Assignments and, in particular, the **midterm test will be conducted via LMS**.
- Report access problems to the **MSDSM office**.
- Note on slides: the uploaded PDFs contain all **definitions and core content**. The instructor's live annotations/sketches on the slides are **NOT captured** in the uploaded files — they are supplementary explanation only.
- Repeated forward references to **DSM-407** (a *compulsory* course, "Advanced Mathematical and Statistical Techniques"), where the instructor teaches **Bayesian inference**, numerical marginalization, and **sampling techniques**.

---

### 2.1 Recap: Probability Distribution Function & Marginalization
- **Probability distribution function** tells you *how probability is distributed over the range of values of a random variable*.
- Distributions may arrive as **joint distributions over many random variables** — where the "random variables" may in fact be **parameters of a model** (this connection will be made explicit when **Bayes' theorem** is covered later).
- Problem: a joint distribution over many variables contains all the information, but is **hard to visualize** and hard to read off the dependence on any single variable.
- **Marginalization** = integrate the joint distribution over **all variables except the one of interest**, leaving a 1-D distribution for that variable.
  - "You marginalize the multi-dimensional probability distribution function down to one dimension."
- **Practical caveat (flagged):** sometimes marginalization integrals are **not feasible** — e.g. you only have the joint distribution sampled at discrete points (a histogram), with **no integrable analytic functional form**. Numerical/algorithmic tricks for this case are taught in **DSM-407** for real-life problems.

---

### 2.2 Histogram as the "poor person's PDF"

**Construction recipe:**
1. Take the random variable $X$ of interest.
2. Divide the **range of $X$ into small bins** (typically of **equal width**).
3. For each bin $[x_1, x_2]$, **count how many observations of $X$ fall inside it** — call it $n_1$; repeat for $[x_2,x_3] \to n_2$, $[x_3,x_4] \to n_3$, etc.
4. The **bin height = the frequency (count) of observations in that bin**. The **bin width is fixed**.

**Key points made:**
- With **equal-width bins**, the count in a bin is **proportional to the density of probability within that bin**.
- If the sample correctly represents the underlying population, the histogram **approximates the underlying PDF**.
- Repeated/duplicate values all count — "if a number repeats, you drop it in the box again and count it again." Values can be integers or fractions.
- Analogy used: **bins are boxes**; you sort every number from a big bag into its box and then count how many numbers landed in each box.
- Replacing the hard-edged discrete bins with a **smooth fitted continuous curve** gives you (approximately) the **probability density function**.

#### Worked numerical example A — binning by hand
- Bin boundaries on $X$: **0, 10, 20, 30, 40, 50, 60, 70** → each bin has **width 10**.
- Example data falling in bin **[0, 10]**: `5, 6, 7, 8, 2, 1, 3, 2` → the instructor counts **6 numbers** in this bin → **height of first bin = 6**.
- Bin **[10, 20]**: count = **8** → height = 8.
- Bin **[20, 30]**: count = **15** → height = 15.
- Bin **[30, 40]**: count ≈ **12** → height = 12.
- Bin **[40, 50]**: count = **8**.
- Result: heights rise then fall → the shape traced by the bin tops, when smoothed, is the PDF.

#### Worked numerical example B — heights of people (student question)
- Random variable: **height (ft)**. Bin width = **0.5 ft**.
- Bins: 4–4.5, 4.5–5, 5–5.5, 5.5–6, 6–6.5, 6.5–7, 7–7.5.
- Hypothetical counts: 4–4.5 → **6**; 4.5–5 → **8**; 5–5.5 → **15**; 5.5–6 → **12**; 6–6.5 → **8**; 6.5–7 → **6 (or 5)**.
- Conclusion read off the histogram: the **most probable height range is 5–5.5 ft**.
- Do the **same exercise separately for weight** → a second, independent 1-D histogram.

---

### 2.3 Probability Density: the mass/volume analogy

- Think of **total probability as a mass $M$** spread over the **total range/volume $V$** of the variable (the full range of $X$).
- **Average density:**
$$\bar{\rho} = \frac{M}{V}$$
  This is *independent of $X$* — it's just $\bar\rho$, a constant.
- But some regions of **parameter space carry more "mass" (probability)** than others → hence a *local* density that varies with position. That local quantity is the **probability density**.
- **Dimensionality:** density need **not** be 3-dimensional. It is defined in whatever dimension the problem has:
  - 1 random variable → PDF defined in **1-D space**; the "volume" element is just a **length** (the bin width $x_2 - x_1$).
  - 2 random variables → the element is an **area**.
  - $n$ random variables → PDF defined in **$n$-dimensional space**, element is an $n$-volume.

#### Formal statement given for the 2-variable case (H = height, W = weight)
Let $dB$ be the amount of probability contained in the region where $H \in [H, H+dH]$ and $W \in [W, W+dW]$. Then the **probability density** is
$$\text{density} = \frac{dB}{dH\, dW}$$
i.e. *(amount of probability mass in the element) ÷ (elementary volume of that element)*.

For the 1-D (strip) case: cut the strip between $H$ and $H+dH$, compute the **area under that strip** = $dB$, then divide by $dH$.

#### Why "average probability" is meaningless (student question)
- By the **sum rule of probability**, all probabilities sum to **1**.
- So "average probability density" = $1 / V$, where $V$ is whatever total volume you chose to spread it over.
  - Spread over a **large** volume → a very small number.
  - Spread over a **small** volume → a large number.
- Hence it carries **no information** — it's just an arbitrary rescaling of 1. **Only the local density is meaningful.**

---

### 2.4 When do you actually need a multivariate distribution? (BMI example)

Student question: *"I have height and weight of several people — how do I plot two variables together?"*

**Instructor's answer / rule:**
- Height and weight observed independently are **two separate observables** → plot **two separate 1-D histograms**. (They may or may not be correlated; a joint histogram is hard to visualize and often not what you want.)
- A **multivariate/joint distribution is needed when your data/observable depends on more than one random variable.**
- **BMI** is a *derived* observable: $B = B(h, w)$ — a function of **both height $h$ and weight $w$** via a known formula. (The instructor notes as an aside that current research suggests BMI is not a great health measure — irrelevant to the maths.)
- So the distribution of BMI over a population is written
$$P(B) \equiv P(x, y) \equiv P(h, w)$$
  — a **multivariate distribution function**.

**Visualization:**
- It is a genuine **3-D plot**: 
  - **x-axis = height $h$**
  - **y-axis = weight $w$**
  - **z-axis = the value of BMI / the probability (histogram height)** — i.e. a **2-D histogram**.
- Because a 3-D "mountain" can't be drawn on a 2-D board, it is projected as a set of **nested closed curves = contours / iso-contours**. Each contour marks the locus where the surface exceeds a given height.
  - Inner contour = **highest-probability region**; next contour out = "**one sigma less probable**" region; and so on.
  - **Contours need NOT be circles or ellipses** — their shape is entirely determined by the functional form of $P(h,w)$.

**Getting back to 1-D from the joint distribution (marginalization in action):**
- Sum rule in 2-D:
$$\iint P(x,y)\, dx\, dy = 1$$
  (Integrating over *both* variables must return the total probability = 1.)
- To get **BMI as a function of height only**: integrate $P(h,w)$ **over all values of weight**.
- To get **BMI as a function of weight only**: integrate $P(h,w)$ **over all values of height**.
- To then ask *"what is the probability of BMI for people with height between 4.5 ft and 5 ft?"*: after marginalizing over weight, **select the strip** $h \in [4.5, 5]$, compute the **area under that strip** ($=dB$), divide by the strip width $dH$.
- In the full 2-D case the analogue is cutting a **chunk out of the "mountainous cake"**: the width and breadth of the chunk are the height- and weight-ranges, and the cake's height gives the BMI/probability value.

---

### 2.5 Practical note on histograms in code
- The **first thing** anyone does with a fresh dataset in a Python notebook is **plot a histogram**.
- **NumPy `hist` / histogram functions** compute the counts and let you set the **bin width**.
- **Vary the bin width and replay** — see how the apparent shape of the PDF changes with binning choice.

---

### 2.6 Population vs. Sample

- **Population = the truth = an infinite number of observations.** Practically unobtainable.
  - Illustration: to know the *true* BMI distribution of humans you'd need every human from the dawn of civilisation to today — and at any point in history there are **more dead people than living people**, so the required set is effectively infinite.
- Consequence: the **frequentist definition of probability**, which rests on the population concept, **breaks down when you don't have a large number of samples**.
- What we actually do: use a **finite sample** to **approximate** the true population PDF.
- A **histogram** built from finite data:
  - has **hard bin boundaries** — it is **not a continuous function**;
  - will often have **empty bins** where samples are lacking;
  - **converges to the true population PDF as the sample size grows large.**
- **"How large is large enough?"** — explicitly flagged as a **valid question deferred to the Central Limit Theorem** discussion. The chain given: **statistics of large numbers ← Central Limit Theorem ← Gaussian distribution.**
- Whether a finite-sample approximation is acceptable is **problem-dependent**; this will be revisited when solving problems.

---

### 2.7 Statistics and Moments

**Definition (from previous class, restated):** a **statistic** is a measure/summary of your data that you hope represents some characteristic of the data.

> **Key definition given:** A statistic represents the **minimum number of numbers you need to represent a set of data.**
> Correspondingly, **moments represent the minimum number of numbers you need to know everything about a probability distribution function.**

#### The Gaussian as the motivating case
- For a **Gaussian (bell curve)** $P(X)$ vs $X$, the distribution is **completely specified by two numbers**:
  - the **mean $\mu$**
  - the **variance $\sigma^2$ / standard deviation $\sigma$** (the width)
- With just $(\mu, \sigma)$ you can **re-create the entire curve from scratch** — amplitude, width, peak location are all determined. You don't need the infinite set of observations of $P(X)$.
- So the **functional form of the Gaussian itself tells you it needs only two numbers**.

#### General moments — the formula
For a distribution $P(X)$ over random variable $X$, the **$n$-th moment** is the expectation value of $X^n$:

$$M_n = \langle X^n \rangle = \int_{-\infty}^{+\infty} x^n \, P(x)\, dx$$

(limits = whatever the actual range of $x$ is).

| $n$ | What you get |
|---|---|
| $n = 0$ | $\displaystyle \int_{-\infty}^{\infty} P(x)\,dx = 1$ — this is just the **sum rule**. The zeroth moment is **always 1 for every distribution**, so it carries **no information**. |
| $n = 1$ | $\displaystyle \int_{-\infty}^{\infty} x\, P(x)\,dx = \langle x\rangle$ — the **mean** / expectation value of $x$. |
| $n = 2$ | $\displaystyle \int_{-\infty}^{\infty} x^2\, P(x)\,dx$ — the **second moment**, associated with the **variance**. |
| $n = 3, 4, \dots$ | third, fourth, … moments — keep going as needed. |

> ⚠️ *Careful:* the instructor first misspoke ("moment 0 is the mean") and then corrected himself — **zeroth moment = sum rule = 1; first moment = mean.** Also note that the *raw* second moment $\langle x^2\rangle$ equals the variance only when the mean is zero; in general variance is the **centered** second moment (see below).

#### Higher-order shape descriptors
- Not every distribution is pinned down by $\mu$ and $\sigma$ alone. "Weird" distributions need more numbers:
  - **Skewness** (3rd-order)
  - **Kurtosis** (4th-order)
- If mean, variance, skewness and kurtosis are enough — excellent. If not, go on to the **fifth** moment, and so on.
- Philosophy stated: **Gaussian occupies the central place in applied statistics.** We therefore like to view any other distribution as a **distortion of the Gaussian** — bending it, stretching one leg, squeezing it. The higher-order moments quantify **how much the distribution deviates from Gaussian**.

#### Centered moments
- **Procedure:** shift the origin of the $X$-axis so that **zero sits exactly at the mean (the first moment $M_1$)**.
- After the shift:
  - Values that were to the **left of the mean become negative**; values to the right stay positive.
  - **The distribution function itself is unchanged** — this is purely a change of the measurement origin / coordinate system.
  - The **mean is now zero for every distribution**.
- All **higher-order moments computed in this shifted frame are called centered moments** (centered *about the mean*).
- Consequence for the Gaussian: once centered, a Gaussian is described by **one number only — $\sigma$**.
- **Emphasis:** "The centered moment doesn't have any other special standing in statistics — it is just convenience."

---

### 2.8 From Moments (population) to Estimates (samples) — preview of next class

- With **infinite data** you can literally **compute** the integrals $\int x^n P(x)\,dx$ and get the moments exactly.
- With **finite data** you can never do that integral from $-\infty$ to $+\infty$. Instead you:
  - Build an approximation to the PDF from the data — a **histogram**, or a **kernel density estimate** (transcribed as "carel density function" — *kernel density estimation*, to be covered), and
  - Perform **finite sums** rather than integrals.
- From that approximate PDF you **estimate** (not calculate):
  - the **mean**, the **standard deviation**, the **skewness**, the **kurtosis**, etc.
- **Terminology point stressed:** these are **estimations, not calculations**, precisely because no integral is performed — only a finite sum over a finite dataset.
- **Next class:** visual treatment of (i) samples, (ii) how to estimate moments approximately from samples, and (iii) how to draw conclusions about the underlying PDF from those approximate moments; plus under what conditions the finite sample gives a good approximation to the infinite population.

---

### 2.9 Closing remarks — sampling and its relevance to AI/ML

- Sampling remains an **open, active research problem** in applied statistics — "even in the age of AI/ML, it is all a game of samples."
- **The better your samples, the better your understanding of the underlying distribution.**
- Direct link made to **training datasets** for **LLMs / AI / ML models**:
  > "A good training dataset is nothing but one that approximately represents the true characteristics of the underlying probability distribution function. A good training dataset is nothing but a finite sample."
- Testing whether a training set is "good enough" = **testing whether your samples are robust**.
- **Sampling techniques are NOT covered in DSM-101.** They are covered (a selected subset, due to time limits) in **DSM-407**. New sampling techniques appear monthly in arXiv/statistics journals.

---

## 3. Flagged as Important for Exams / Assignments

- ✅ **LMS access is mandatory.** Log into `lms.iiti.ac.in` with your IIT Indore email **at least once** and confirm your account works. **Assignments and especially the MIDTERM TEST will be conducted through LMS.** Escalate any access failure to the MSDSM office immediately.
- ✅ **Lecture slides are the authoritative source** for definitions and core content; they are posted on LMS after each lecture. The instructor's hand-drawn annotations are *not* saved, so take your own notes on those.
- 📌 **Deferred but promised topics** (i.e. they *will* come back):
  - **Bayes' theorem** — will explain the "random variables as model parameters" idea.
  - **Central Limit Theorem** — will answer *"how large a sample is large enough?"*; approached via the Gaussian distribution.
  - **Kernel density estimation** and **estimation of moments from finite samples** — **next class**, with visual aids; flagged as "crucial."
- 📌 **Out of scope for DSM-101, covered in DSM-407 (compulsory course):** Bayesian inference, marginalization when the integral is intractable, and sampling techniques.

---

## 4. Quick Formula Sheet

| Concept | Formula |
|---|---|
| Sum rule (1-D) | $\int_{-\infty}^{\infty} P(x)\,dx = 1$ |
| Sum rule (2-D / joint) | $\iint P(x,y)\,dx\,dy = 1$ |
| Marginalization | Integrate the joint PDF over **all** variables except the one of interest |
| Average (probability) density | $\bar{\rho} = M/V$ — *constant, carries no information* |
| Probability density (2 variables) | $\dfrac{dB}{dH\,dW}$ = (probability mass in the element) / (elementary volume) |
| $n$-th moment | $M_n = \langle x^n\rangle = \displaystyle\int_{-\infty}^{\infty} x^n P(x)\,dx$ |
| Zeroth moment | $\int P(x)\,dx = 1$ (always) |
| First moment | $\langle x\rangle = \int x\,P(x)\,dx$ = **mean** |
| Second moment | $\int x^2 P(x)\,dx$ → **variance** (when centered) |
| Gaussian | fully specified by **$(\mu, \sigma)$**; if centered on the mean, by **$\sigma$ alone** |
| Beyond Gaussian | add **skewness** (3rd), **kurtosis** (4th), … |
| Histogram bin height | = **frequency (count) of observations falling in that bin**; bin width fixed |