# DSM-101 — Session 3 (2026-08-22, Prof. Suman Majumdar)
## Data Compression, Statistics, and the Calculus of Probability

---

## 1. Overview

This session bridges the previous two "what is probability?" lectures and the formal machinery of probability theory. It opens by recapping the two schools of probability (frequentist = long-run frequency of repeatable events; Bayesian = subjective degree of belief updated with all available background information). It then argues that *more data is not automatically better* unless you can **compress** it — illustrated with a five-point scatter plot where joining points by line segments *increases* the parameter count (8 parameters for 5 points) while a single straight-line fit *reduces* it to $(m, c)$ plus uncertainties $(\Delta m, \Delta c)$. This motivates the formal distinction between **population** (infinite, holds the truth) and **sample** (finite, what we actually get), and the definition of a **statistic** as any summary computed from a finite sample. The second half is a systematic review of the calculus of probability: bounds, sum rule (discrete and continuous), conditional probability / product rule, addition of mutually exclusive probabilities, the law of total probability, and Bayes' theorem. The lecture closes with multivariate (joint) distributions, independence, **marginalization**, why continuous random variables can never be pinned to an exact value (measurement error), the interpretation of probability as a **density** per unit length/area/volume, and a worked urn problem (3 black + 1 white ball, drawing two without replacement).

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Two classes of definitions of probability

- There is **no single definitive definition** of probability; there are two classes of definition.
- **Frequentist:** applies where the experiment is *repeatable* (coin toss, die throw). Probability = frequency of an event in the limit of infinitely many repetitions of the experiment.
- **Bayesian / subjective:** probability encodes the **degree of belief** of an observer about an outcome, given a background model and whatever information the observer has.
  - Requires building a **belief measure system**, which is substantially more complex than a simple frequency count, because it must fold in *all* additional information about the scenario.
  - Lecturer's remark: *"we always have more information than we think we have."* The central task is to combine all of this information when building the **causal model** that produces the observed outcome.
- Both approaches agree that more observations → sharper conclusions; in the Bayesian case, the degree of belief becomes more concentrated / more definitive as data accumulate.

### 2.2 Is more data always good? The need for data compression

- More data carries more information, **but** making sense of more data is harder.
- Without compression you never arrive at a comprehensible answer → compression is mandatory for inference.

### 2.3 Worked example: five data points — two competing "models"

Setup: five points $(x_i, y_i)$, $i = 1,\dots,5$, plotted on an $x$–$y$ plane.

**Option A — join consecutive points by short straight segments.**
- Each segment is itself a model: the straight-line equation
$$y = mx + c$$
- With 5 points there are 4 segments → 4 values of $m$ and 4 values of $c$ → **8 numbers to describe 5 data points**.
- Conclusion: this is **not** data compression — we have *increased* the amount of information (added redundancy), and it yields no interpretable trend.

**Option B — fit a single straight line through all five points.**
- One value of $m$, one value of $c$.
- Compression: $5$ pairs $(x_i, y_i)$ $\;\to\;$ $1$ pair $(m, c)$.
- A statistically sound answer must also quote uncertainties:
$$m \pm \Delta m, \qquad c \pm \Delta c$$
where $\Delta m$, $\Delta c$ are the tolerance/allowance (variance) around the slope and intercept, estimated from the fit.
- This *is* compression and it supports an inference: "the trend has roughly this slope and this intercept."

**Real-world framing:** given ~1 million users of Amazon/Netflix with ~1000 variables each, the client does **not** want a scatter plot of a million points. They want a **summary** — a trend with respect to variables like age, demography, location — so that a business decision can be made.

### 2.4 Population vs. sample

- **Population:** the infinite pool of trials/experiments for a system. Population is *always infinite* and **holds the truth** about the system.
  - Example: tossing a coin an infinite number of times and getting 50% heads / 50% tails establishes the truth "this is an unbiased coin."
- **Sample:** a *finite*, countable set of $n$ outcomes actually drawn from that population (e.g. 100, 1000, or 10,000 tosses). The word **limited/finite** is essential.
- "Population always exists holding the truth; all we mortal humans can do is draw a finite number of samples from that population."
- In the earlier example, the 5 data points are 5 samples drawn from an infinite population.

### 2.5 Definition: statistic

- A **statistic** is a number (a summary) estimated from a *finite sample* drawn from the population — **without assuming a model**.
- "Statistic" is a **generic umbrella term** covering *anything* you derive from the finite data set. Examples given:
  - mean
  - variance
  - skewness
  - kurtosis
  - two-point correlation function
  - correlation functions in general
- Contrast: in the straight-line fit above we *assumed a model*, so the estimated $m$ and $c$ are **not necessarily statistics** in this strict sense.
- Another use of statistics: build a **histogram** of the sample to approximate the distribution of the population from which the samples were drawn (to be covered later).

### 2.6 Calculus of probability — basic rules

**(i) Bounds.** For $P(x)$ the probability of $x$ taking a certain value,
$$0 \le P(x) \le 1$$

**(ii) Sum rule / normalization.**
- Binary event (on/off, head/tail, present/absent): the probabilities of the two outcomes sum to 1.
- General discrete case:
$$\sum_i P(i) = 1$$
- Continuous random variable over an infinite range:
$$\int_{-\infty}^{\infty} P(x)\,dx = 1$$
- **Use:** the sum rule is the standard **normalization technique**. "If you do not have any other way of normalization, the sum rule comes in handy."

**(iii) Product rule / conditional probability.**
$$P(X,Y) = P(X\mid Y)\,P(Y)$$
and equivalently
$$P(X,Y) = P(Y\mid X)\,P(X)$$
- Verbal statement given in class: *the probability of two events $X$ and $Y$ both occurring is the product of the probability of one occurring and the probability of the other occurring given that the first has already occurred.*
- The two forms are interchangeable when we do not discriminate about which event happened first (mutually inclusive). **If the sequence of events matters for the problem, the two must be interpreted differently.**
- Conditional probability is what allows probability to be **updated in the light of new data** — the key Bayesian feature. A frequentist treats a new data point as just another independent data point; Bayes always views the new point *in the light of the existing data*.

**(iv) Addition of mutually exclusive probabilities.**
If $n$ events are mutually exclusive (none depends on the others), with probabilities $P(x_1), P(x_2), \dots, P(x_n)$, then the probability that **either** $x_1$ **or** $x_2$ ... **or** $x_n$ occurs is
$$P(x_1 \cup x_2 \cup \dots \cup x_n) = \sum_{i=1}^{n} P(x_i)$$
- Note: this is **derived from the sum rule**, not an independent axiom.

**(v) Law of total probability.**
If an event $E$ can only follow one of a set of independent preceding events $A, B, C, D, \dots$, then
$$P(E) = P(E\mid A)P(A) + P(E\mid B)P(B) + P(E\mid C)P(C) + \dots = \sum_i P(E \mid A_i) P(A_i)$$
- Logic: $E$ can only happen if one of the preceding events has happened; $E$ is conditioned on/connected to $A, B, C, \dots$
- It is a **consequence of conditional probability plus the sum rule**.

**(vi) Bayes' theorem.**
Starting from $P(X\mid Y)P(Y) = P(Y\mid X)P(X)$, Thomas Bayes' famous form is
$$P(Y \mid X) = \frac{P(X \mid Y)\, P(Y)}{P(X)}$$
- It is *just* a rearrangement of the product rule — **the mathematics is trivial; the interpretation is what matters** (to be covered in the next few classes, along with applications to updating probabilities in the light of new data).

### 2.7 Worked problem: urn with 3 black + 1 white ball (no replacement)

**Statement.** An urn holds **3 black balls and 1 white ball** (4 total). Two balls are drawn one after another **without replacing the first**. Find:
- $P(\text{black then white})$
- $P(\text{white then black})$

**Solution worked in class (black then white):**
1. First draw: $P(\text{black}) = \dfrac{3}{4}$ (3 black out of 4 balls).
2. The black ball is **not** returned → 3 balls remain, of which 1 is white.
   Second draw: $P(\text{white} \mid \text{black drawn first}) = \dfrac{1}{3}$.
3. Because the two draws are **connected (dependent) events**, apply the product rule / conditional probability rule:
$$P(\text{black, then white}) = P(\text{black}) \times P(\text{white}\mid\text{black}) = \frac{3}{4}\times\frac{1}{3} = \frac{1}{4}$$

**Symmetric case (white then black):**
$$P(\text{white, then black}) = \frac{1}{4}\times\frac{3}{3} = \frac{1}{4}$$

**Answer: both probabilities equal $1/4$.**

**Teaching point emphasised:** if the events had been *independent* you would have used the marginal probabilities $3/4$ and $1/4$ separately; here they are **connected**, hence the conditional-probability/multiplication rule. Also: *"intuition only has a limit"* — for simple problems intuition gives the answer, but you should always translate that intuition into the mathematical formula, because complex problems cannot be solved by intuition alone. The instructor stressed he cared more about **how** you derived it than the number.

### 2.8 Joint (multivariate) probability distributions

- For a single continuous random variable $X$, there is a population distribution / probability distribution function for $X$.
- For an event depending on two random variables $X$ and $Y$, define the **joint probability distribution function**
$$P(X, Y)$$
= the probability of finding $X$ in the range $[X,\, X+dX]$ **and** $Y$ in the range $[Y,\, Y+dY]$.

**Independence.** If $X$ and $Y$ "do not talk to each other" — no information exchange, no correlation — then
$$P(X,Y) = P(X)\,P(Y)$$

**Conditional distribution for a fixed value.** One can also write the conditional distribution of $X$ at a fixed $Y$:
$$P(X \mid Y = C)$$
- Caveat raised in class: this is **often not useful**, because for a continuous random variable we can never know $Y$ *exactly*.

**Normalization in the multivariate case.** The sum rule still applies: integrating the multivariate distribution over **all** variables gives 1, e.g.
$$\int\!\!\int P(x,y)\,dx\,dy = 1$$

### 2.9 Why you can never pin down a continuous random variable exactly

- Claim: you cannot precisely specify the value of a continuous random variable $X$ (or $Y$) at any instant.
- **Reason 1 (statistical):** to evaluate the probability *at a precise value* of $X$ you would need complete knowledge of the underlying population distribution — i.e. infinitely many samples of $X$ — which is practically impossible.
- **Reason 2 (measurement):** every measurement is made with an instrument (meter tape, laser range-finder, your eyes) that has a finite resolution.
  - Example: measuring the **length of a road**. If the meter tape's smallest division is **1 cm**, then there is a **1 cm** uncertainty $\Delta x$ that you must quote.
  - Improve to millimetre or **micron** precision — still $1\ \text{mm}$ or $1\ \mu\text{m}$, i.e. still a **finite** error.
- Therefore, however small, there is **always a finite $\Delta x$** for a continuous random variable.
- **Practical warning (emphasised):** people summarising data or presenting conclusions/strategies to a client frequently **forget to quote these errors**. Without the error, neither you nor the client can judge whether a strategy built on that conclusion is feasible. Errors will be treated in detail later in the course.

### 2.10 Marginalization

- Situation: your observation gives you the **joint** distribution $P(X,Y)$, but you are actually interested in $P(X)$ or $P(Y)$ alone.
- **Marginalization** = integrate the joint distribution over all the variables you are *not* interested in:
$$P(X) = \int P(X,Y)\, dY, \qquad P(Y) = \int P(X,Y)\, dX$$
- Generalises to any number of variables (integrate out all the nuisance variables).
- This also follows from the sum rule.
- **Why it matters / why it's hard:**
  - It is one of the hardest tasks in solving **inverse problems** (going from observation/data → theory/model), discussed in classes 1 and 2.
  - You often need $P(X)$ for one or a few variables, because in the full joint space you cannot see/interpret where most of the probability lies.
  - But to integrate over $Y$ you must know how the joint behaves in $Y$ — and often you don't, or you have only a limited number of samples of $P(x,y)$ with gaps you must fill in before integrating.
  - Numerical integration techniques exist, but in bad cases exact marginalization is nearly impossible; there are **"tricks of the trade"** giving approximate $P(X)$ or $P(Y)$. These look simple on the surface but rest on a sophisticated understanding of the joint distribution. To be covered under **Bayesian inference**.

**Visualization described:** $P(x,y)$ is a 3D surface; project it onto the $x$–$y$ plane and draw **1-sigma, 2-sigma and 3-sigma contours** to see where most of the probability lies. Then marginalizing over $y$ collapses this to a 1D curve of $P(x)$ vs. $x$.

### 2.11 Probability *density* function — why "density"?

- The "density" language is easiest to understand from the multivariate viewpoint.
- With $n$ variables you have an $n$-dimensional space; with 3 variables $(x,y,z)$ a 3D space.
- Take a small volume element $dx\,dy\,dz$ at a point $(x,y,z)$. The probability contained in that small element **per unit volume** is the **probability density** at that point.
- **1D case:** if $dx$ is a unit length, the probability lying in that interval is the probability density at that location of $P(x)$.
- **2D case:** for $P(x,y)$, take a small area element with $dx$ and $dy$ each of unit length at location $(x,y)$; the probability lying in that tiny area is the probability density there.
- **General:** density = the amount of probability within a unit length / unit area / unit volume in the multivariate space.
- Aside: spaces of more than 3 dimensions cannot be visualised directly (even 3D is awkward — we always draw a 2D projection on the board).

---

## 3. Formula Sheet (as stated in lecture)

| Concept | Formula |
|---|---|
| Straight-line model | $y = mx + c$; reported as $m \pm \Delta m$, $c \pm \Delta c$ |
| Probability bounds | $0 \le P(x) \le 1$ |
| Sum rule (discrete) | $\sum_i P(i) = 1$ |
| Sum rule (continuous) | $\int_{-\infty}^{\infty} P(x)\,dx = 1$ |
| Product / conditional rule | $P(X,Y) = P(X\mid Y)P(Y) = P(Y\mid X)P(X)$ |
| Mutually exclusive events | $P(x_1 \text{ or } \dots \text{ or } x_n) = \sum_{i=1}^{n} P(x_i)$ |
| Total probability | $P(E) = \sum_i P(E\mid A_i)P(A_i)$ |
| Bayes' theorem | $P(Y\mid X) = \dfrac{P(X\mid Y)P(Y)}{P(X)}$ |
| Independence | $P(X,Y) = P(X)P(Y)$ |
| Conditional distribution | $P(X \mid Y = C)$ |
| Marginalization | $P(X) = \int P(X,Y)\,dY$ |
| Joint normalization | $\int\!\!\int P(x,y)\,dx\,dy = 1$ |

---

## 4. Flagged as Important / Assignments / Resources

- **In-class exercise (do it yourself):** the urn problem — 3 black + 1 white ball, draw 2 without replacement; compute $P(\text{black then white})$ and $P(\text{white then black})$. The instructor explicitly said he is **"more interested in how you estimated it"** than in the number itself, because it exercises conditional probability. (Answer: $1/4$ each.)
- **Key conceptual takeaway stressed repeatedly:** always translate intuitive reasoning into an explicit probability formula, because intuition fails on complex problems.
- **Always quote uncertainties** ($\Delta m$, $\Delta c$, $\Delta x$) when reporting a summary/statistic — a recurring theme and a practical/professional requirement.
- **Recommended resource 1:** the website **"Seeing Theory"** (Brown University, `seeing-theory.brown.edu`) — developed by a Brown PhD student, now archived/frozen. Covers chance events, expectation, variance, joint/compound probability, probability distributions, frequentist inference, Bayesian inference, and regression analysis, all with visualizations. The instructor said he **will use it in the next class** and asked everyone to look through it in their spare time.
- **Recommended resource 2:** the YouTube channel **3Blue1Brown** — good visual explanations of probability, data science, ML techniques, maths and physics; the instructor draws examples from it. Caveat he added: good visualization helps to start with, but can also **limit your imagination** if you only ever think in that one picture.
- **Course logistics:** once the instructor is added as a teacher to the DSM-101 class page, all materials and these web links will be posted there.

---

## 5. Announced for Next Session

- Resume from **multivariate probability distribution functions** and **probability density functions**.
- Basic concepts: chance events, **expectation value**, **variance**.
- Deeper treatment of **Bayes' theorem: interpretation and application** (updating probability in the light of new data).
- Later in the course: errors/uncertainties in detail, histograms and recovering the population distribution, Bayesian inference and the approximate marginalization "tricks."