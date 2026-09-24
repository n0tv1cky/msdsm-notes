# DSM-101 — Probability & Statistics
## Session 2 — 19 Aug 2026 — Instructor: Suman Majumdar
### Topic: What *is* Probability? A Historical Journey + Frequentist vs. Bayesian Views

---

## 1. Overview of the Session

This session picks up from the previous class, where we tried (and failed) to find a single, universally agreed **definition** of probability — we only found *descriptions* of how to *use* it. Instead of forcing a definition, the instructor takes the class on a short **history of the idea of probability**, from Pascal & Fermat (1654), through Bernoulli, Thomas Bayes, Gauss, Laplace, the frequentist reaction (Boole, Venn, Fisher, von Mises), and the 20th-century "neo-Bayesian" revival (Keynes, Jeffreys, Cox, Jaynes). The point of the history is to show *why* the meaning and usage of probability shifts from problem to problem depending on context. The session then contrasts the two surviving schools in detail — the **classical/frequentist** view (probability = relative frequency in an infinite ensemble of identical experiments, objective, gives a *point value*) versus the **Bayesian** view (probability = degree of belief in a proposition held by an observer given available information, subjective, gives a *probability distribution*). These are illustrated with several worked/conceptual examples: the naked-eye supernova problem (4 supernovae in 10 centuries), straight-line fitting `y = mx + c`, the bus-frequency problem, the probability of life on Mars, and the Drake equation. No heavy mathematics yet — this is the conceptual foundation before the calculus of probability and Bayes' theorem are developed in later sessions.

**Administrative notes:** LMS page not yet created; slides from the previous class and today's class will be **emailed** to all students (via institute email / batch coordinator / batch representative) at the end of the day, and posted on LMS once it exists.

---

## 2. Topics & Concepts, in Order Taught

### 2.1 Recap: What probability lets us do
- Working description (not a definition): **Probability allows us to apply logical reasoning to data in order to deduce, with a particular and calculable degree of certainty, the properties of the wider system.**
- The general question being answered: **"How do you reason in situations where it is not possible to argue with absolute certainty?"** (i.e., where no 100%-certain answer exists).
- **Sources of uncertainty** in real-life problems:
  1. Intrinsic randomness of the process being studied.
  2. Processes *designed* to be random (e.g., a lottery — a complex system).
  3. Noise in/over the data.

### 2.2 Recap: Inverse problems
- In practice we almost always deal with **inverse problems**: going *from the data* back *to the model/understanding*. We observe an outcome or effect; we don't know how it came about; we build a mental model of what could have caused that outcome.
- **Three classes of inverse problem:**
  1. **Hypothesis testing**
  2. **Parameter estimation**
  3. **Model selection**

### 2.3 Two philosophical stances on probability (pre-history)
- **Epistemic stance:** probability used to describe the property or effect of a system when the **causative circumstances for that property are not necessarily known**.
  - *Example given:* the age of the universe is ~13.6 (or "7") billion years with an error bar — we can *measure* the age, but we don't know what made the universe that old.
- **Aleatory stance:** associated with **games of chance** (tossing a coin, throwing a die). Deals with predicting the **future outcome of a random physical process**. Subdivides into:
  - phenomena that are **in principle predictable**, and
  - phenomena that are **inherently unpredictable**.
- *Example discussed:* "It will rain tomorrow with 40% probability." The number 40% depends on: **where** you are, **what time of year / which month and date**, the **historical record of rain on that date**, whether this year's weather/climate has deviated from previous years, or whether you should assume the trend continues. Many factors feed into that single number — which is exactly the point.

### 2.4 History of probability — timeline of key figures

| Year / Era | Person(s) | Contribution |
|---|---|---|
| **1654** | **Pascal & Fermat** | Asked by an aristocratic professional gambler: *how should the stakes be divided between players in a game of chance/cards if they quit before the game ends?* In a series of letters in 1654 they laid down the **basic calculus of probability**. They did **not** define probability — they found out how to *calculate/deal with* it. (Note: science then was funded by kings, queens, or the rich.) |
| — | **Bernoulli** | First to ask **how does one assign a probability?** Developed the **Principle of Insufficient Reason**. |
| — | **Thomas Bayes** | Solved Bernoulli's unsolved problem: **how to update probability** after new data. Probability of an event/hypothesis *given* additional information. |
| ~age 18 | **Carl Gauss** | Mathematical astronomer: invented the **method of least squares**; derived the **Gaussian distribution of errors**; formulated the **Central Limit Theorem (CLT)**. |
| — | **Laplace** | Rediscovered Bayes' theorem; applied it to **celestial mechanics** and **medical statistics**; marked a return to the idea that **probability is a lack of information**. |
| Reaction | **Boole, Venn (Venn diagram), Fisher, von Mises** | Mathematicians rejected Laplace's development; tried to **remove all subjectivity** from probability. For them **probability = a measured frequency**. Invented the whole apparatus of **statistics** for everyday problems. |
| 20th c. | **Keynes, Jeffreys, Cox, and in the 1980s "Steve G" / E. T. Jaynes** | **Neo-Bayesian movement** — return to the intuitive ideas of Bayes and Laplace: probability relates to the **amount of information (or lack of it)** we have in hand. Jaynes attacked the problem of *assigning* probability via the **Principle of Maximum Entropy**. |

> The instructor stresses this is a **flip-flop** history: frequentist ↔ Bayesian dominance keeps alternating.

#### Bernoulli — Principle of Insufficient Reason
- If an experiment/action has **n possible outcomes** and you have **no additional specific information** about any individual outcome, then you have **no sufficient reason to believe any outcome is special** or more likely.
- Therefore: **distribute probability equally among all n outcomes**, i.e. each outcome gets probability **1/n**.
- **Bernoulli's limitation:** he could not see how to **update** the probabilities after performing the experiment once and obtaining one outcome (one data point). Should the probabilities stay the same for the next trial, or change? He had no formulation.

#### Thomas Bayes — the key insight
- Provided the mechanism to **update probability** in the light of new data: the **probability of an event or hypothesis given that you have more information**.
- **Important nuance emphasised:** the **conditional-probability formula itself was NOT new** — it was already part of the basic algebra of probability introduced by Pascal and Fermat. Bayes' actual contribution was the **interpretation**: that this formula can be used as a **means of updating probability**. *"The contribution of Bayes is not that conditional probability formula, but how it should be interpreted."*
- Probability is thus a **measure of lack of information**.
- Bayes' theorem will be covered in much more detail later; the instructor notes he uses it constantly in his own work.

#### Gauss — three items to remember
- **Method of least squares** — used when fitting a curve to a set of data points (to be revisited).
- **Gaussian distribution of errors.**
- **Central Limit Theorem (CLT)** — "at the heart" of many assumptions people make when solving statistics or real-life problems. *"If you do not understand or appreciate the central limit theorem, it is very difficult to actually do any kind of statistics, machine learning, or AI-related work."*

### 2.5 The two schools — formal statements

#### A. Classical / Frequentist
- **Definition:** Probabilities are **measurable frequencies assigned to objects or events**. The **relative frequency** of an event arises from the number of times that event would occur relative to an **infinite ensemble of identical experiments**.
- i.e., repeat the experiment an infinite number of times, keeping **all surrounding conditions identical** (practically impossible); the relative frequency with which an outcome occurs **is** its probability.
- Intuitively linked to games of chance: you can toss a coin forever, roll a die forever.
- **Where it breaks down:**
  - **Single (one-off) events** — no frequency to measure.
  - Situations where you **cannot in practice measure the frequency**; you must then invent a **hypothetical ensemble** of events.
  - Mathematically it requires the notions of **infinity** and **randomness**, which are themselves not well-defined abstract concepts.
- **Output:** always a **point value** (a single number) for each parameter. Objective.

#### B. Bayesian
- **Definition:** Probability is the **degree of belief in a proposition**, allocated by an **observer**, given the **information/data available to that observer**. Uncertainty arising from **incomplete data or noise** determines the degree of belief.
- Consequence: **probability depends on the observer** ⇒ probability is **subjective** (which mathematicians dislike).
- **Output:** a **probability distribution** over parameters, not a point value.
- **Strength:** can assign probability in situations where the experiment **cannot be repeated**.

**Illustrations of observer-dependence:**
- **Magician example:** A magician vanishes a coin and pulls it from your ear. The magician *knows the method exactly*; you (the observer) do not. The probability you assign to "the coin will be produced from my hair" depends on how much information you have — the magician is **withholding information** from you.
- **Caveman vs. modern human and rain:** A caveman doesn't know the evaporation → cloud → rainfall mechanism. A modern person does, because of accumulated observation over thousands of years and a built-up model. Asked "will it rain tomorrow?", the caveman and the modern person assign **different degrees of belief to the same proposition**, purely because they hold **different sets of information/data**.
- **Life on Mars:** *"What is the probability that there is life on Mars?"* You **cannot** create many Mars-like planets, set up conducive environments, and watch their evolution from planetesimals to planets to see whether life forms. So this is **not** a frequency of an event — the frequentist approach **breaks down**. A Bayesian instead: states the proposition "there is life on Mars"; compiles all observations of Mars (from Earth, spacecraft, Mars rovers); compares with similar evidence inside and outside the solar system; **builds a model**; and only then quantifies a degree of belief. This requires a **complex belief-measure system** that simply does not exist in the frequentist framework.

---

## 3. Worked Example 1 — The Naked-Eye Supernova Problem

### Background physics given
- A **supernova** is the last stage of a star's life: the star explodes and spits out all the metals made in its core into its surroundings.
- Energetically like **several million nuclear explosions** ⇒ becomes **super bright**.
- A **single exploding star can outshine all the other stars in its galaxy combined**, so even a very distant, faint galaxy becomes visible at that moment.
- Naked-eye supernovae have been **recorded historically** — in **Chinese texts**, in **Europe**, and reportedly in the **Inca civilization** — all **before the invention of the telescope**.

### The data
- Up to **1987**, in the **preceding 10 centuries**, there were **4 naked-eye supernovae recorded** ("naked eye" = observed with no aid, no glasses, no lens).

### Question A
> Standing in **1987**: what is the probability of a bright (naked-eye) supernova occurring in the 20th century (i.e., in the remaining years up to 2000)?

**Frequentist answer (worked):**
- Data: 4 supernovae in 10 centuries.
- Assign equal probability per century (Principle of Insufficient Reason).
- **P(supernova in a given century) = 4 / 10 = 0.4 = 40%.**

**Critique of the frequentist answer (important):**
This calculation **assumes supernovae were equally likely to happen *and* to be observed throughout the last 10 centuries** — which need not be true:
- Humans may not have been equally interested in looking at the sky in every century. In a century when astronomy was fashionable, people watched vigorously and might have caught **more than one** supernova; in other centuries a supernova could have gone off with **nobody looking up**, lowering the *probability of reporting*.
- The **20th century** is special: humans are far more aware; **human population has grown enormously**; the **Industrial Revolution** in Europe and America had happened and its effects were being felt; **world wars** intervened.
- ⇒ **"You actually have more information than you think you have"** — this ignored information is the seed of the idea of **prior information**.

**Bayesian approach (structure, not a number):**
- Start with an **a priori assignment**: let **X = probability of seeing a supernova in the 20th century**.
- Then *model* the physics and the sociology:
  - How do supernovae form? How does a star die? ⇒ need **stellar physics**.
  - What is the **rate of star formation** in different galaxies?
  - **How many galaxies** are there in the universe?
  - How many are **bright enough to be seen with the naked eye**?
  - How many can **host** this kind of supernova, and **at what rate** do those supernovae go off?
  - How has **human curiosity** evolved over time? How has **human population** evolved? How many *curious* humans exist at any given time?
- Note carefully: the question is the **probability of *seeing* a supernova**, not the probability of a supernova *happening*. So it also depends on **how dark the night sky is**, the **density of human population in different regions**, **what fraction of the population looks at the sky**, and **how often they look**.
- The model **deals in populations of stars, not individual stars**, and assumes a group of stars can be identified which are **equally likely to explode at a certain time**.
- ⇒ A **complex belief-measure structure**, vastly more complicated than 4/10 — and this is exactly what solving an **inverse problem** looks like: observe the effect, build the model that caused it, then assign probability.

### Question B — the updating twist (Bayes' theme)
> Suppose in **1987** we *do* see a bright naked-eye supernova. Is the probability of there being *another* supernova later in the 20th century (the remaining **13 years**, 1987 → 2000) affected by this?

**Frequentist answer:**
- Previously 4 supernovae in 10 centuries; now **5 in 10 centuries**.
- **P = 5 / 10 = 1/2 = 50%.**
- But this takes **no account** of how human civilization or astronomy will develop over the next 13 years.

**Bayesian answer:**
- You **adjust some aspect of your complex belief-measure model in the light of this new, fresh data**.
- You **do not completely discard** your prior belief — you **update** it.

### Related aside — the Drake Equation
- Asked from the chat: the famous equation for the number/probability of **intelligent alien civilizations** in the universe is the **Drake equation**.
- It encodes a very complex belief-measure system, folding in everything from **our own curiosity** to the willingness/curiosity of more developed alien civilizations to expose themselves, and then yields a probability of **finding (intelligent) life** elsewhere.

---

## 4. Worked Example 2 — Straight-Line Fitting: Frequentist vs. Bayesian

(Arose from the question: *"Is the frequentist perspective used in AI, or is it always Bayesian?"* Answer: **frequentist methods are absolutely still used** — e.g. **least-squares / χ² (chi-square) minimization** is fundamentally a frequentist procedure. But the same task can also be done in a Bayesian way.)

**Setup:** Fit a set of data points, *y* versus *x*, with a straight line:

```
y = m x + c
```

with two parameters: **m = slope**, **c = intercept**. The **model is identical** for both schools — only the *inference* differs.

**Frequentist:**
- Find the **best-fit values** of *m* and *c* — a single "point value" for each parameter.
- **Problem:** the fit assumes the data you had was all the data there is. If tomorrow someone performs a different experiment and produces a **new data point**, the best-fit parameters may **change significantly**. This gives rise to the **bias–variance trade-off** problem familiar in curve fitting and AI/ML. *(Bias–variance trade-off will be treated with examples and exercises in DSM 407.)*

**Bayesian:**
- Does **not** hand you a single precise value; it gives a **probability distribution function (the posterior) for the slope and for the intercept**.
- There is a **width** around the slope value and a width around the intercept value (e.g. **2σ, 3σ widths**); every value under the distribution is a *possible* value, each carrying its own probability — some low, some high, depending on the shape of the **posterior distribution**.
- Because a finite amount of data is explicitly acknowledged, arrival of new data leads you to **update** the distribution rather than **drastically change** a point estimate ⇒ **more robust** answers (most of the time, not always).
- If a genuinely disruptive new dataset arrives, you may need to **change the model** — and Bayesian analysis lets you **introduce a new model and compare it against the old model within the same framework** (this is **model selection**).

**Neural-network analogy:**
- A standard **Artificial Neural Network (ANN)** outputs a **point value** (a number or a set of numbers).
- A **Bayesian Neural Network** outputs a **distribution** — analogous to a **posterior distribution over slope and intercept** in the straight-line example.

> **Core takeaway (stated explicitly as "the fundamental difference"):**
> **Even with the same model, the frequentist approach tries to find a single number for each parameter; the Bayesian approach tries to find a probability distribution for each parameter.**

---

## 5. Worked Example 3 — The Bus-Stop Problem (student question)

**Setup:** You reach a bus stop and ask a person standing there when the next **bus line number 15** will arrive. The person says: *"In the last 1 hour, three number-15 buses arrived."*

**Frequentist reasoning (worked numbers):**
- 3 buses in 60 minutes ⇒ **60 ÷ 3 = 20 minutes** between buses.
- Answer: "a bus every **20 minutes**," based on a **limited amount of observation** (1 hour).

**What the frequentist ignored:**
- It may already be **midnight** — the line may have stopped running, or the headway may change after (say) **9 p.m.**
- The observer had no data for that period and **never even allowed for the possibility of deviation** from the observed frequency.

**Bayesian reasoning:**
- Gives a **probability distribution for the bus interval, peaked around 20 minutes**, but with **breathing space / leeway** around it — it could be **15 minutes** or **25 minutes**.
- Reasons: the observed hour may have been the **busy period** with a denser schedule; the schedule may change by the time you actually want a bus; there could be a **traffic jam** or an **accident**.

**Key concept introduced here — *latent observations* / prior information:**
- **Latent observations** (instructor's own phrasing) = information you hold **unconsciously** — you *know* traffic jams happen, you *know* accidents happen — but which you don't consciously feed into a frequentist calculation.
- A Bayesian **does** fold these in, assigning extra uncertainty due to such possible events.
- ⇒ **"You actually have more prior information than you think you have."** This is **prior information**, to be developed formally when Bayes' theorem is covered.

---

## 6. Q&A Points Worth Noting

- **Q: Are successive supernova events dependent on each other?**
  A: It depends entirely on **how you model your belief-measure system**. You must ask: how does a star go through its life cycle; is that life cycle affected by neighbouring stars; given millions of stars in a galaxy, what is the probability that one explodes; what is the typical lifetime of a star; of a galaxy; hence how frequently should one see a supernova from one galaxy; how many galaxies are there and in which directions of the sky. Crucially, remember the quantity asked for is the probability of **seeing** a supernova, so night-sky brightness, human population density, fraction of the population interested in the sky, and observation frequency all enter. Intervals and patterns of past occurrences are legitimate parameters.

- **Q: Frequentist = objective, Bayesian = subjective?**
  A: **Yes.** But the subjectivity is **not vague** — it is grounded in observations the frequentist deems irrelevant to the problem (traffic jams, accidents, changing human curiosity, etc.). Mathematicians dislike the subjectivity; note that statistics was historically developed by **physicists, astronomers, and people applying it in biology**, not by pure mathematicians. That subjectivity is **crucial for solving many practical problems**.

- **Q: When does the subjectivity / updating end? Isn't it an infinite loop?**
  A: It **doesn't end — and that's the point.** It is **not** an infinite loop: the more information you get, the **more precise** your understanding becomes. Examples of progressive model refinement:
  - Sun revolves around Earth → Earth revolves around Sun → circular orbit → elliptical orbit → not exactly an ellipse, and planets are not all coplanar.
  - **Newton's laws of motion** (simple) → **General Relativity** (more complex). **GPS actually relies on general relativity**, which is why we can time events to the **millisecond** and locate an individual precisely on Earth's surface.
  - As we observe at ever smaller scales (atomic, electronic) and finer time resolution, our models become more complex and more accurate. *"Science is not about stopping somewhere. It is about pushing the boundaries of your understanding."*

---

## 7. Flagged as Important (for exams / later study)

- **Central Limit Theorem is at the heart of statistics, ML and AI** — explicitly flagged: without understanding/appreciating CLT it is very difficult to do any statistics or ML/AI work.
- **Bayes' theorem** — the instructor says he spends most of his time using it and **will definitely cover it in detail**, including a precise treatment of what a **posterior** is, with examples.
- **Prior information** — "you always have more prior information than you think you have" — to be elaborated with several examples when Bayes' theorem is taught.
- **Method of least squares** — "we will definitely visit it."
- **The basic calculus of probability** (Pascal–Fermat) — "we will go through this calculus very soon."
- **Not covered in this course:** the **Principle of Maximum Entropy** (Jaynes) — likely not in DSM-101.
- **Cross-course pointer:** **DSM 407** (a *compulsory* course) — half of it is application of **Bayesian statistics**, taught by this instructor; **bias–variance trade-off** will be worked through there with examples and exercises.
- **Materials:** slides from Session 1 and Session 2 will be **emailed** (via institute email IDs / batch coordinator) and later posted on the **LMS** once the page is created.

---

## 8. One-Page Summary Table — Frequentist vs. Bayesian

| | **Frequentist / Classical** | **Bayesian** |
|---|---|---|
| Probability is… | a **measurable relative frequency** of an event over an **infinite ensemble of identical experiments** | a **degree of belief** in a proposition, held by an **observer**, given available information |
| Nature | **Objective** | **Subjective** (observer-dependent) |
| Output of inference | A **point value** per parameter (best-fit m, c) | A **probability distribution (posterior)** per parameter, with widths (2σ, 3σ) |
| Handles single/unrepeatable events? | **No** — needs a hypothetical ensemble | **Yes** (life on Mars, Drake equation) |
| Uses prior/latent information? | No | **Yes** (prior information) |
| New data | Recompute; estimate may shift drastically (**bias–variance trade-off**) | **Update** belief; typically more robust; can also compare models |
| Key figures | Boole, Venn, Fisher, von Mises | Bayes, Laplace, Keynes, Jeffreys, Cox, Jaynes |
| Supernova example | 4/10 = 40%; after 1987 → 5/10 = 50% | Build full stellar-physics + human-observation model; update it with the 1987 event |
| Bus example | 60/3 = **20 min** exactly | Distribution **peaked at 20 min**, spread ~15–25 min |
| ML analogue | Standard ANN (point output), least-squares/χ² minimization | Bayesian Neural Network (distributional output) |