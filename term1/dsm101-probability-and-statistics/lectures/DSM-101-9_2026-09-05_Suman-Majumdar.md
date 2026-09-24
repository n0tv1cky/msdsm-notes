# DSM-101 — Probability & Statistics
## Session 9 (2026-09-05, Instr. Suman Majumdar): **The Central Limit Theorem (CLT)**

---

## 1. Overview

This session is devoted entirely to the **Central Limit Theorem (CLT)** — described by the instructor as "the pinnacle of applied statistics," without which "all our understanding and interpretation of data would collapse." The lecture begins with an informal statement of the theorem (repeatedly draw $n$ samples from *any* parent distribution with **finite variance**, sum/average them, and the histogram of those sums/averages tends to a Gaussian), then demonstrates it live using the *Seeing Theory* CLT simulator — first with a uniform parent distribution, then with deliberately skewed and bimodal ("blow-up at both ends") parent distributions — showing that (i) convergence to Gaussianity always happens regardless of parent shape, (ii) larger sample size $n$ ⇒ narrower resulting Gaussian and faster convergence, and (iii) with sample size $= 1$ there is no summing and hence no CLT. The consequences are then drawn out: the **standard error** $\sigma_{\bar X}=\sigma_X/\sqrt{n}$, why Gaussians are ubiquitous in nature (human heights, ocean-wave heights, consumer behaviour, stock-index fluctuations — all sums of many random influences), and a **graphical/convolution proof sketch** (rectangle $*$ rectangle = triangle, triangle $*$ rectangle ≈ bell, repeat ⇒ Gaussian), with side remarks on convolution in phone cameras, AI image generation, and CNNs. The session closes with a fully worked numerical problem on New Jersey teacher salaries contrasting $P(X<50{,}000)$ for a single teacher versus $P(\bar X<50{,}000)$ for a sample of 100.

---

## 2. Topics and Concepts, in order taught

### 2.1 Informal statement / setup of the CLT
- Setting: there is a **population distribution** (the "parent distribution"). You **randomly sample** from it — e.g. 5 samples, 10 samples.
- **Coin-toss illustration** used to set up the idea:
  - Parent distribution = distribution of heads/tails for an unbiased coin, $P(\text{H}) = P(\text{T}) = 0.5$.
  - Assign numbers to outcomes: e.g. head $\to 1$, tail $\to 2$.
  - Toss the coin 5 times, **add up the 5 numbers** → one value.
  - **Repeat this whole exercise a large number of times** and histogram the sums.
  - **Result:** that sum follows a **Gaussian distribution with predictable variance.**
- **Caveat / assumption (essential):** the parent distribution **must have finite variance**. If the variance is not finite, the theorem does **not** apply (such distributions are called **pathological distributions**).

### 2.2 Formal statement (as dictated in lecture)
> The **sum of $n$ random values drawn from a probability distribution function with finite variance** tends to be **Gaussian distributed** about the **expectation value of the sum**, with variance $n\sigma^2$.

- Equivalently, the **mean of a large number of values tends to follow a normal distribution regardless of the probability distribution from which the values were drawn** — hence *the sampling distribution is known even when the underlying probability distribution is not*.
- The normalized sum written in lecture:
$$X \;=\; \frac{x_1 + x_2 + \cdots + x_n}{\sqrt{n}}$$
  follows a Gaussian distribution (for large $n$).
- Also noted: distributions such as the **Binomial** and **Poisson** arise from multiple drawings from an underlying distribution, and they **all tend to look Gaussian as the number of drawings increases** — consistent with the earlier derivation in the course of the Gaussian as a limit of the Poisson.

### 2.3 The live simulation (Seeing Theory CLT applet)
Setup of the applet:
- Parent distribution controlled by two shape parameters $\alpha$ and $\beta$ (Beta-type family); the yellow patch is the **population distribution**.
- The applet takes $n$ samples, sums them, and **divides by $n$** (i.e. takes the **average** rather than the raw sum) so that different sample sizes are normalized onto a comparable scale. Average $=$ sum$/n$.
- It then builds a **histogram of these averages** — that histogram is what CLT says becomes Gaussian.

**Terminology clarified in response to a student question:**
- **Sample size** = the number of values summed/averaged in *one* draw (e.g. 15 values → average → one point).
- **Number of draws** = how many times you repeat that procedure (e.g. 50 draws → 50 points in the histogram).
- The plotted histogram = frequency of each average value.

**Experiment A — uniform parent ($\alpha=1$, $\beta=1$), sample size $=1$:**
- 50 draws, then another 50, etc.
- Histogram **reproduces the parent (uniform) distribution**, *not* a Gaussian. Theoretical prediction curve is also uniform.
- **Reason:** no summing takes place when sample size $=1$ ⇒ CLT does not apply.

**Experiment B — uniform parent, sample size $=3$:**
- Draw 3 samples, sum, divide by 3, plot; repeat.
- After 50 draws: non-uniform but clearly not Gaussian. After ~100 draws: still not Gaussian "at least in my eyes." After ~150 draws: **begins to look Gaussian**, matching the theoretical prediction curve.

**Experiment C — uniform parent, sample size $=15$:**
- Converges to a Gaussian with **far fewer draws**.
- The resulting Gaussian is **much narrower** than the sample-size-3 case.

**Conclusions drawn from A–C:**
- The **width (standard deviation $\sigma$) of the resulting Gaussian depends on the sample size**, and the relation is **inverse**: increase sample size ⇒ width decreases; decrease sample size ⇒ width increases.
- **Gaussianity is achieved faster (fewer draws needed) when sample size is bigger**; with small sample size you need many more draws.
- Convergence speed depends on **only two things: the sample size and the number of draws** — *not* on the shape of the parent distribution.

**Experiment D — deliberately skewed / "weird" parent distribution:**
- Keep sample size high. Histogram of averages quickly looks Gaussian (slightly skewed at first, converging to the theoretical Gaussian prediction).

**Experiment E — parent distribution with peaks blowing up at both ends (bimodal):**
- Again, with high sample size the histogram already approaches a Gaussian; with more draws it converges further.

**Bottom line:** *It really doesn't matter what the nature of the underlying distribution is* — **as long as the parent distribution has finite variance**, the distribution of the sums/means is Gaussian for a large number of draws.

### 2.4 Consequences of the CLT
- **You do not need to know the underlying distribution to know the sampling distribution.** Provided the parent has finite variance, the sampling distribution is determined.
- **Sampling distribution of the mean:**
  - Centred at $\bar X$ (tending to the true mean),
  - With **standard error**
  $$\sigma_{\bar X} \;=\; \frac{\sigma_X}{\sqrt{n}}$$
  where $\sigma_X$ is the parent-distribution standard deviation and $n$ is the number of samples summed/averaged. Valid as $n \to \infty$ (i.e. large $n$).
- **Interpretation:** estimating the mean from a sample tends towards the true mean, and the **uncertainty in the estimate decreases as the sample gets bigger** — exactly what was seen when the applet sample size was raised from 3 to 15.
- (As stated in lecture) the sample standard deviation/"sample variance" quantity scales as $1/\sqrt{n}$: $\sigma/\sqrt{n}$.

### 2.5 Why Gaussians are everywhere in nature (qualitative examples)
The repeated logic: *any observed quantity is the sum of many random influences, hence Gaussian.*
- **Human height:** measure everyone's height in a room (a random sample of the population) and bin it — the histogram is Gaussian. Height is determined by genetics + nutrition + many other processes, i.e. it is already a **sum of many random influences** drawn from different distributions. Outliers exist, but usually have identifiable causes.
- **Ocean/sea-wave height:** measure wave height above the (flat) sea bottom, either at one location over a long time or at many locations at one time. Histogram is Gaussian, because waves arise from random air motion, currents, undercurrents, etc.
- **Consumer behaviour:** a shopper's purchasing outcome is influenced by many random factors — hungry or not, had a fight at home, start of the month vs. empty bank account — so it is a sum of random processes and can be modelled as Gaussian.
- **Stock market / Sensex fluctuations:** intraday fluctuation is a sum of many random processes.
- **General rule stated:** whenever you observe the outcome of an experiment or natural phenomenon, you can safely expect it to follow some random distribution, because no observation comes from a single draw of one parent distribution — it is always influenced by many physical processes.
- **Temperature example:** record the temperature at a fixed time of day for 30 days and histogram it — expect a Gaussian. If each daily record is itself the mean of, say, 5 readings taken 5 minutes apart, the uncertainty on each such measurement is the measured value's $\sigma$ divided by $\sqrt{n}$ (here $\sqrt{5}$). Each measurement is treated as a discrete sample from the parent distribution — analogous to the Poisson treatment of point-like/discrete events done earlier in the course.
- **Why it matters:** CLT is what lets us quote an **uncertainty on a measurement**; any prediction must come with a statement of how likely it is.

### 2.6 Derivation — what is and isn't required
- The **derivation is NOT covered and explicitly declared "not important"** for this course. Interested students may read it in the slides or textbooks.
- The most elegant derivation route: **Fourier transforms** + the **convolution theorem** (skipped because Fourier-transform background was not assumed).
- The instructor's remark: CLT "sounds like a magic / dark art" at first, but the derivation shows it is ordinary science.

### 2.7 Convolution — graphical "proof" of the CLT
- **Definition given:** *convolution is scanning one function with another*; denoted by the **star symbol**, e.g. $f * g$.
- **Procedure described:**
  1. Hold one rectangle function fixed in space.
  2. Bring the second rectangle in from $+\infty$ and slide it, in small steps, towards $-\infty$.
  3. At each position, record the **overlapping area** between the two functions.
  4. Before any overlap, the overlap area is $0$; as they begin to overlap the area increases; it is **maximum when the two identical boxes coincide exactly**; then it decreases back to $0$ as the sliding function moves away.
- **Results of repeated convolution:**
  - rectangle $*$ rectangle $=$ **triangle**
  - triangle $*$ rectangle $\approx$ **bell-shaped curve**
  - keep convolving ⇒ you **eventually land on a Gaussian**
- This is **shape-independent**: as long as the shapes have finite boundaries, convolving any shape with any shape repeatedly gives a Gaussian. This is a **straightforward graphical proof of the CLT** (and mirrors what the simulation showed).
- Note: many alternative graphical/sampling demonstrations of the CLT exist online.

**Side applications of convolution mentioned (context only, not examinable content):**
- **Mobile phone cameras:** the photo app convolves a **smoothing filter** with the raw image, so photos look good despite hand-shake or poor light. This is a form of **smoothing / averaging**.
- **Early AI-generated images:** looked unnaturally smooth (skin tone, hair, boundaries) because the model was effectively **convolving many internet images/filters together**, averaging away the roughness/irregularity of real skin and hair. Larger training databases later allowed the roughness to be reproduced.
- **Convolutional Neural Networks (CNNs)** use the same convolution idea.

---

## 3. Worked Numerical Example (done in full in class)

### Problem statement
> The average teacher salary in New Jersey is \$52,174. Suppose the distribution is **normal** with standard deviation \$7,500.
> **(a)** What is the probability that a randomly selected teacher makes **less than \$50,000 per year**?
> **(b)** If we sample **100** such teachers, what is the probability that the **sample mean** is less than \$50,000 per year?
> **(c)** Why is the probability in (a) higher than the probability in (b)?

Given:
$$\mu = 52{,}174, \qquad \sigma = 7{,}500$$

### Part (a) — single teacher, $n=1$
Convert \$50,000 to a $z$-score (how many $\sigma$ away from the mean it lies):
$$z = \frac{50{,}000 - 52{,}174}{7{,}500} = -0.2899$$
The standard normal is centred at $0$; the negative sign puts \$50,000 on the **left** of the peak, $0.2899\sigma$ below the mean.

Required probability is the **cumulative distribution function (CDF)** value — i.e. the **area under the curve to the left of \$50,000**:
$$P(X<50{,}000) = P(Z < -0.2899) = \int_{-\infty}^{-0.2899} p(z)\,dz \approx 0.3860$$

- Interpretation given in class: the whole left half (up to the mean) is $0.50$; being slightly below the mean already drops the probability a little below 50 %, to $\approx 38.6\%$.
- (The instructor also referenced the one-tail value $0.159$ associated with the $1\sigma$ point while sketching the $1\sigma$, $2\sigma$, $3\sigma$ marks on the curve.)

### Part (b) — sample mean of $n=100$ teachers
Now the relevant distribution is the **sampling distribution of the mean**, which has the **same centre** but a **much smaller** spread:
$$\sigma_{\bar X} = \frac{\sigma}{\sqrt{n}} = \frac{7{,}500}{\sqrt{100}} = \frac{7{,}500}{10} = 750$$

New $z$-score:
$$z = \frac{50{,}000 - 52{,}174}{750} = -2.8987 \approx -2.90$$

i.e. **almost $3\sigma$ below the mean** — far out in the tail, where very little area remains.
$$P(\bar X < 50{,}000) = P(Z < -2.8987) \approx 0.0019$$

### Part (c) — explanation
- The two parts refer to **two different distributions with different $\sigma$'s**:
  - (a) the parent salary distribution, $\sigma = 7{,}500$;
  - (b) the distribution of the mean of 100 salaries, $\sigma_{\bar X} = 750$.
- Averaging 100 salaries makes the distribution **much narrower/thinner**, so the same \$50,000 cut-off moves from $0.29\sigma$ away to $\approx 2.9\sigma$ away from the mean, and the tail area collapses from $0.3860$ to $0.0019$.
- **"This is the main point here. Nothing else."** — the whole problem is about (i) identifying *which* distribution you are working with, (ii) computing its $\sigma$ via $\sigma/\sqrt{n}$, and (iii) reading off the area under the curve.

---

## 4. Formula sheet (everything stated in this session)

| Concept | Formula |
|---|---|
| CLT (general form) | Sum of $n$ i.i.d. values from a pdf with **finite variance** $\to$ Gaussian, centred on $E[\text{sum}]$, with variance $n\sigma^2$ |
| Normalized sum | $X = \dfrac{x_1+x_2+\cdots+x_n}{\sqrt{n}} \sim$ Gaussian for large $n$ |
| Sample mean | $\bar X = \dfrac{1}{n}\sum_{i=1}^{n} x_i$ (i.e. average $=$ sum$/n$) |
| **Standard error of the mean** | $\sigma_{\bar X} = \dfrac{\sigma_X}{\sqrt{n}}$ |
| Cumulative distribution function | $P(X < a) = \displaystyle\int_{-\infty}^{a} p(x)\,dx$ |
| $z$-score / standardization | $z = \dfrac{x-\mu}{\sigma}$ (for a single observation), $z = \dfrac{\bar x - \mu}{\sigma/\sqrt{n}}$ (for a sample mean) |
| Convolution notation | $f * g$ — "scanning one function with another"; area of overlap as a function of displacement |
| Fair-coin parent distribution | $P(\text{Head}) = P(\text{Tail}) = 0.5$ |

---

## 5. Flagged as important for exams / assignments

- **Core examinable idea:** the CLT statement, the **finite-variance condition**, the dependence of the result on **sample size** and **number of draws**, and the **standard error $\sigma/\sqrt{n}$**. Described as "very, very important" because it is what lets you quote uncertainties on measurements.
- **The derivation of the CLT is explicitly declared NOT important** ("Derivation is not important. If you are really interested, you can go through the derivation yourself"). Fourier-transform/convolution-theorem derivations are in the posted slides for optional reading.
- **Homework:** a **similar problem is attached at the end of the slides** (same structure as the New Jersey teacher-salary problem) — solve it yourself. The class-worked problem will also be attached to the posted slides.
- **Recommended self-study:** go through the **Seeing Theory CLT animation** yourself and experiment with sample size and number of draws; other online demonstrations also exist.
- **Next class:** a **Q&A session at the start**, then more CLT practice problems. Students are asked to **write down questions in advance** (especially on *where the CLT can and cannot be applied, and how it should be applied*) and ideally email them beforehand. Remaining practice problems will be posted on the **LMS**.