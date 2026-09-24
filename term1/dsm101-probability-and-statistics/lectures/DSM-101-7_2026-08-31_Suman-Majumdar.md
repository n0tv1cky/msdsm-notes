# DSM-101 — Probability & Statistics
## Session 7 — Bayes' Theorem and Bayesian Inference
**Instructor:** Suman Majumdar | **File:** DSM-101-7_2026-08-31

---

## 1. Overview

This session introduces **Bayes' theorem** as the engine of *Bayesian inference*, i.e. the framework for solving **inverse problems** — situations where we have observed data and must infer the truth (a model and its parameters) behind that data. The lecture begins by contrasting the frequentist view of probability (long-run frequency of events) with the Bayesian view (**probability = degree of belief**), then dissects Bayes' theorem term by term: **posterior, likelihood, prior, evidence**, stressing that every probability in the theorem is *implicitly* conditioned on unspoken prior information *I* and a chosen model *M*. It explains when the proportional form (posterior ∝ likelihood × prior) suffices and when the full normalized form (with the evidence) is required (model selection). A large part of the class is spent on the **power and danger of the prior**, illustrated by two counter-intuitive worked examples with explicit numbers: the **"Steve the librarian vs. farmer"** problem from Kahneman & Tversky, and a parallel **repeat-offender / crime** problem. The session ends with a derivation showing that **Bayesian updating** turns yesterday's posterior into today's prior (so old data is never discarded), and a practical "rule number one" for approaching any real-world inference problem.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 The inverse problem and the Bayesian viewpoint
- **Inverse problem:** we observe data, and from it must infer the underlying truth — i.e. a *model* that describes/fits the truth and the *parameters* of that model.
- Can be attacked frequentist-style, but the Bayesian view brings a unique angle:
  - **Bayesian probability = degree of belief**, *not* frequency of an event.
  - Every probability appearing in Bayes' theorem must be *interpreted* as a degree of belief.
- Historical note: **Thomas Bayes** — a reverend; no portrait is verified as genuinely his. Being attached to a church gave him free time, which he devoted to applied statistics.

### 2.2 Bayes' theorem — the full form with unspoken conditioning
Popular (incomplete) form:

$$P(\theta \mid D) = \frac{P(D \mid \theta)\, P(\theta)}{P(D)}$$

Full form, with the **normally unspoken** conditioning made explicit:

$$P(\theta \mid D, I, M) = \frac{P(D \mid \theta, I, M)\; P(\theta \mid I, M)}{P(D \mid I, M)}$$

where:
- **θ** = the parameters of the model you are using to describe the data
- **D** = the data / observations
- **I** = **prior information** (everything you knew about the phenomenon *before* the experiment)
- **M** = the **model**

**Key emphasis:** θ is *always tied to a specific model M*. The moment you change M, θ and its conditional distribution change completely. I and M are "absorbed"/hidden in the notation but never go away.

*(ASR note: at one point the transcript reads "divided by P of theta" for the denominator — the denominator is the evidence P(D | I, M).)*

### 2.3 The four named terms
| Term | Expression | Name |
|---|---|---|
| Left-hand side | P(θ \| D, I, M) | **Posterior** |
| First factor on RHS | P(D \| θ, I, M) | **Likelihood** |
| Second factor on RHS | P(θ \| I, M) | **Prior** |
| Denominator | P(D \| I, M) | **Evidence** (probability of the data) |

### 2.4 The working form — *important note flagged in class*
> **Posterior ∝ Likelihood × Prior**
> $$P(\theta \mid D, I, M) \;\propto\; P(D \mid \theta, I, M)\, P(\theta \mid I, M)$$

- This proportional form is what you will use **most of the time**: for **parameter estimation** and **hypothesis testing**, where normalization is unnecessary.
- The **equality** form (i.e. including the evidence) is needed only for **model selection** — when comparing model 1 vs. model 2 vs. model 3, because P(D) depends on M. You compute the posterior separately for each model and compare.
- Computing the evidence integral analytically or numerically is **very difficult**; tricks exist, but avoid it when you can.

### 2.5 Posterior — detailed
- Represents the **state of knowledge about the system in the light of the data** (and given the model and prior information).
- This is normally **exactly what you want** — whatever quantity you wish to conclude about, you want *its posterior*.
- Examples given: concluding about customer behaviour; concluding about a trend in the share market.
- Physical example: *an apple falls from a tree*. Given this observation, what do you conclude about the force of gravity? → you want the **posterior of the force of gravity** (or of the parameters of your gravity model).

### 2.6 Likelihood — detailed
- Almost the *reverse* question of the posterior:
  - Posterior asks: *given the data, what can I say about the model/parameters?*
  - Likelihood asks: *assume the model is true and its parameters take the specific value θ — what is the probability that this would give rise to the data I actually observe?*
- So: posterior is the **posterior of the parameters**; likelihood is the **likelihood of the data**.
- **Combining multiple data sets:** for many data points drawn from the *same* model, the total likelihood is the **product** of the individual likelihoods:
  $$L(\theta) = \prod_i P(d_i \mid \theta, I, M)$$
- **Q&A clarification (student question):** you may multiply likelihoods **only when each data point was obtained via an independent experiment** — independent draws from the same underlying population probability distribution function (i.i.d.).
  - Illustration: seeing an apple fall from one tree is one experiment; walking to a different tree at a random location and seeing another apple fall is a second, uncorrelated experiment → independent → multiply.

### 2.7 Worked conceptual example: straight-line model
- Suppose the data are fitted by
  $$y = mx + c$$
- Parameters of this model: **m** and **c**.
- What you want: **P(m | data)** and **P(c | data)** — the posteriors of the slope and intercept.
- Using Bayes: on the RHS you need the **likelihood of the data given a specific value of m**, and given a specific value of c.
- Procedure: **vary m and c**, generate predicted data points for each, compare with the actually observed data ("data-bar"), and thereby determine which values of m and c are more likely to have produced the observed data. *This is the whole exercise of the inverse problem.*
- Target quantity: constrain θ (e.g. its expectation value) given data D, model M and prior information I.

### 2.8 Prior — detailed
- **Definition:** P(θ | I, M) contains **all information known before the experiment is performed** — about the system, the model, the universe.
- Gravity example of prior: before you ever saw an apple fall, you had already observed the Sun and other celestial bodies apparently moving relative to the Earth → you already believe some force acts between Earth and other objects. That is prior information; don't forget it when interpreting the falling apple.
- **Key claim (underlined in class):** *In most problems we actually have far more prior information than we think we have*, and most of the time people **forget to include it**, leading to devastating conclusions.
- **Why we forget it — evolutionary aside:** human brains evolved (from cave-dwelling times, over thousands/millions of years) for instant reaction/reflex thinking as a survival defence mechanism. This reflex extends to *thought*, not just physical movement, so we react to observations faster than warranted and skip the prior. This is the "thinking fast" failure mode.

### 2.9 Evidence — detailed
- P(D | I, M) = **probability of the data** = the integral (marginalization) of the numerator over *all* parameters:
  $$P(D \mid I, M) = \int P(D \mid \theta, I, M)\, P(\theta \mid I, M)\, d\theta$$
- Interpretation: **all possibilities via which the data could have been obtained** — including possibilities the model allows *and* those it does not.
- Needed only for **model selection** (see §2.4).

### 2.10 Worked Example 1 — "Steve": librarian or farmer? (Kahneman & Tversky)
**Setup (the survey statement):**
> "Steve is very shy and withdrawn, invariably helpful but with very little interest in people or in the world of reality. A meek and tidy soul. He has a need for order and structure and a passion for details."

**Question asked to respondents:** Is Steve more likely a **farmer** or a **librarian**?
**Typical answer:** librarian (matches the stereotype).

**Sources / credits:**
- Survey by **Amos Tversky** and **Daniel Kahneman**, USA.
- Kahneman won the **2002 Nobel Prize in Economics** "for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty." Tversky did not share it — he died in **1996**.
- Famous paper: **"Prospect Theory: An Analysis of Decision under Risk."**
- Book: ***Thinking, Fast and Slow*** (Kahneman) — the source of this example.
- Recommended: the **3Blue1Brown** YouTube video that works this example with these numbers and graphics (URL on the slide).
- Their demonstration: humans **do not think logically** (they neglect base rates).

**The missing prior:** the **relative population of farmers vs. librarians** (and the location where you might encounter the person).

**Numbers used in class:**
- Assumed farmer : librarian ratio = **20 : 1** (deliberately generous to librarians; the lecturer notes the true US ratio might be more like 200 : 1, but the conclusion is unchanged).
- Representative sample: **200 farmers + 10 librarians = 210 people**.
- Assume **40% of librarians** fit Steve's description → 0.40 × 10 = **4 librarians**.
- Assume **10% of farmers** fit the description → 0.10 × 200 = **20 farmers**.
- Total people fitting the description = 20 + 4 = **24** out of 210.
  - P(fits description) = **24/210**
- P(librarian | fits description) = **4 / 24 = 16.7%**
- Therefore P(farmer | fits description) ≈ **83.3%**

**Conclusion:** A randomly encountered person fitting that description is **more likely a farmer than a librarian** — the opposite of the intuitive answer. This is the power of the prior (base rate).

### 2.11 Worked Example 2 — Repeat offenders vs. new offenders (the "flipped" version)
**Common belief:** ex-criminals are much more likely to re-offend (more inclination, jail contacts/encouragement, fewer legitimate earning routes) — so police round up local known criminals after a crime.

**Numbers used in class:**
- Population ratio non-criminal : criminal = **20 : 1** → **200 ordinary people + 10 known criminals**.
- Among criminals, probability of re-offending = **50%** → 0.5 × 10 = **5**.
- Among the general population, probability of committing a crime = **10%** → 0.10 × 200 = **20**.
- Total potential offenders = 5 + 20 = **25**.
- P(offender is a known criminal | a crime occurred) = **5 / 25 = 1/5 = 20%**
- P(offender is someone new from the general population) = **80%**

**Conclusion:** Even with a high re-offence rate, because criminals are a small minority, a new crime is **80% likely** to have been committed by someone with no prior record. Counter-intuitive — this is "thinking slow" / Bayes' theorem in action.
**Moral stated:** Ignoring the prior → **biased answer → biased action → aggravation of a section of society → chaos and disorder.**

### 2.12 Kinds of priors and practical guidance
- **Uniform / flat / non-informative prior:** when you know nothing about the experiment or model before performing it, take
  $$P(\theta) = \text{constant}$$
  i.e. all values of θ equally probable. Reasonable as a starting point; has advantages *and* disadvantages (to be discussed later).
- **Effect of the prior diminishes with data:** as the experiment gathers more and more data, the likelihood becomes **more robust and narrower**, and the influence of the prior shrinks.
- **Rule of thumb (flagged):**
  > *If changing your prior to another (reasonable) prior changes your inference significantly, you do not have enough data — you need more data.*
- **Caution:** in complicated multi-dimensional problems (say 4–5 parameters, not just 2–3), the **shape of the prior can have subtle effects** you may not notice. This is the source of much of the controversy around Bayesian statistics — because we are explicitly dealing with *states of belief*.

### 2.13 Bayesian updating — posterior of old data becomes the prior for new data
**Setup:** data set **D1** obtained one year ago; new survey gives data set **D2**, obtained independently.

**Step 1 — posterior from D1 alone:**
$$P(\theta \mid D_1) \;\propto\; P(D_1 \mid \theta)\, P(\theta)$$

**Step 2 — posterior from both data sets:**
$$P(\theta \mid D_1, D_2, I, M) \;\propto\; P(D_1, D_2 \mid \theta)\, P(\theta)$$

**Step 3 — use independence of the two experiments:**
$$P(D_1, D_2 \mid \theta) = P(D_1 \mid \theta)\, P(D_2 \mid \theta)$$

**Step 4 — regroup:**
$$P(\theta \mid D_1, D_2) \;\propto\; P(D_2 \mid \theta)\, \underbrace{\big[\,P(D_1 \mid \theta)\, P(\theta)\,\big]}_{\displaystyle \propto\; P(\theta \mid D_1)}$$

$$\boxed{\,P(\theta \mid D_1, D_2) \;\propto\; P(D_2 \mid \theta)\; P(\theta \mid D_1)\,}$$

**Interpretation (the key takeaway):**
- The **posterior obtained from the old data set becomes the prior for the new data set**.
- P(D2 | θ) is the likelihood of the *new* data alone.
- Bayes' theorem **never discards** conclusions drawn from old data; it *uses* them as the base on which belief is updated in the light of new data.
- This is why Bayes' theorem is considered one of the most important theorems in applied statistics and why it gives such robust results — from everyday practical problems to the development of fundamental laws of physics.
- The whole procedure of concluding from observations via Bayes' theorem = the **Bayesian inference framework**.

### 2.14 Rules of Bayesian analysis (practical problem solving)
> **Rule 1:** Write down the **question as accurately as possible**. *What do you want to know?*
> **There are no rules for n > 1.**

- Writing down the right question is **"99.99% of the work."** Once written, the rest is mechanical: identify that quantity as the **posterior (LHS)**, then write the **RHS** of Bayes' theorem and estimate the **likelihood** and the **prior**.
- This is exactly what was done in the Steve problem: the question posed was *"What is the probability that the person I encountered is a librarian?"* — and it was answered graphically, but the graphical procedure *was* Bayes' theorem.

### 2.15 Mentioned but not worked through
- A slide/worked example on the **interpretation of the mean of a distribution** in the Bayesian sense of probability vs. the frequentist sense — students told to look at it on their own (slides on LMS).
- The Steve problem also written out fully in explicit Bayes'-theorem notation on a slide (students to read; not covered aloud).

---

## 3. Exam / Assignment / Admin Notes

- **Slides will be posted on the LMS.**
- **Next class:** we will **solve problems using Bayes' theorem** — specifically to practise whether we can correctly *write down the question we want answered*, which is the hard part.
- Explicitly flagged as **"an important note, not a side note"**: the working form **posterior ∝ likelihood × prior**, and the fact that the equality form (with the evidence) is required **only for model selection**.
- Things repeatedly emphasized as "keep this in mind" / "very important":
  - Every probability in Bayes' theorem is implicitly conditioned on **I (prior info)** and **M (model)**; θ is meaningless without a specified M.
  - Probabilities here are **degrees of belief**, not frequencies.
  - You may multiply likelihoods **only** for **independent** experiments/observations.
  - The prior is the most commonly neglected element and can completely reverse a conclusion (Steve; crime example).
  - Rule-of-thumb: prior sensitivity ⇒ insufficient data.
  - Rule 1 of analysis: write the question precisely; there is no Rule 2.
- **Self-study / recommended:** *Thinking, Fast and Slow* (Kahneman); the **3Blue1Brown** video on the Steve/librarian Bayes example; the mean-of-a-distribution slide.