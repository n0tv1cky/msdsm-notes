# DSM-101 — Probability & Statistics
## Session 1 (2026-08-17) — Instructor: Prof. Suman Majumdar
### Introductory Lecture: Why Statistics? Inverse Problems and the Concept of Probability

---

## 1. Overview

This is the opening session of DSM-101, a foundational probability-and-statistics course placed at the start of the programme because probability, statistics and linear algebra sit at the core of machine learning and AI. The lecture is almost entirely conceptual/motivational — no formal derivations yet. The instructor first covers course logistics (10 lectures + 1 tutorial by him, then 10 by Dr. Arshad, joint mid-term via the LMS portal worth ~50% of the grade, remaining 50% after mid-term by two other faculty). He then motivates the whole subject by introducing the idea of the **inverse problem**: in any empirical science (and in data science/business analytics) you only observe *effects* (data) and must infer the *causes* (the law/model/theory behind them). He illustrates this with Newton and gravity, Tycho Brahe's naked-eye declination measurements of Mars leading to Kepler's laws, and a supermarket-shopping-behaviour analogy. He classifies inverse problems into three types — **hypothesis testing, parameter estimation, and model selection** — with US stock-market crash examples for each. He argues that astronomers have been data scientists since antiquity (citing a telescope producing 7.2 TB/s), lists astronomer-founded analytics firms, and finally introduces **probability** as the tool for reasoning under uncertainty, distinguishing sources of randomness (noise, intrinsic/quantum randomness, effective randomness of complex systems) and two philosophical stances: **epistemic** and **aleatory**. The session closes with Q&A on plotting/fitting data (points vs. model curves) and on the non-static, non-coplanar nature of planetary orbits. The historical development of probability and the two competing modern views (frequentist vs. Bayesian) are deferred to the next lecture.

---

## 2. Topics & Concepts, in order of teaching

### 2.1 Course logistics and administration
- **Course**: DSM-101, Probability & Statistics. One of the basic/foundational courses of the programme; deliberately scheduled at the beginning.
- **Rationale**: Basic probability, statistics and linear algebra are "at the core of machine learning and artificial intelligence." Course = revision of these concepts + how they connect to ML/data-analytics ideas.
- **Teaching team & structure**:
  - Prof. Majumdar: **first 10 lectures + ~1 tutorial**.
  - **Dr. Arshad**: next 10 lectures.
  - Total 4 faculty across the course.
  - **Mid-term exam**: conducted jointly by Majumdar + Arshad via LMS; 50% of that exam from each instructor's portion. Decides **~45–50% of the grade**.
  - Remaining ~50% of grade: two more faculty after the mid-term.
- **LMS portal**: `lms.iiit.ac.in` (as pronounced) — all slides, supplementary material, assignments posted there; assignments submitted through LMS.
- **Exam format** (flagged explicitly):
  - **Almost no theory — essentially all problem solving** (at least in Majumdar's part).
  - Question types: **multiple choice, fill-in-the-blank, and "write a number / percentage / probability"** type answers.
  - **Proctored**; questions and options may be **jumbled/randomised** per student ("almost like JEE").
  - Explicit warning: do not copy from each other; do not use an AI bot.
- **Follow-on courses mentioned**:
  - **DSM-407** — compulsory advanced probability & statistics course (next term); goes deeper into **Bayesian statistics and its ML applications**.
  - A further **elective** on advanced Bayesian applications (course code to be announced).

### 2.2 Reference books (recommended)
- **Sheldon Ross — *Introduction to Probability and Statistics for Engineers and Scientists***. Strongly recommended; especially the **worked examples and problems** in the relevant sections after each lecture.
- **Bonamente — *Statistics and Analysis of Scientific Data***.
- Both said to be easily findable online.

### 2.3 Why statistics? — Data and empirical science
- **Empirical branch of science** = any field built on **observations or experiments** (physics, chemistry, biology, astronomy).
- **Data = observations.** Examples given: whether a person wears a white or blue shirt; the exact time of sunrise on each day of the year.
- The fundamental problem in such fields: *given the data, infer the law/process/mechanism that produced it.*

### 2.4 The **Inverse Problem** (central concept of the lecture)
- **Definition**: The class of problems where you have a set of observations/data and must **conclude or infer the law, process, or method that produced them** — i.e. you have access only to the **effect**, and must reason backwards to the **cause**.
- Contrast: the **forward/direct problem** — predicting outcomes when the model *and* its parameters are known — is **much easier**.
  - *Example*: an **unbiased coin**, P(head) = P(tail) = **50%** (0.5). Since the model and parameters are known, you can predict/simulate outcomes trivially — "two lines of Python code." You'd be right ~50% of the time.
- Inverse problems are hard because **two completely different, unrelated causes can explain the same observation** (e.g. "theory of gravity" vs. "theory of magic" both explain a falling apple). The discriminator is **whether the theory survives testing against more and more diverse, independent observations, and across scales.**

#### Worked illustration A — Newton and gravity
- Observation: an apple falls **down**, not up. Repeated over many days/weeks/months, and for *any* released object.
- Inference: something on the ground pulls objects → theoretical model named **gravity**.
- Later validation **across enormously different scales**: apple-to-ground (a few feet) → Earth orbiting the Sun → the Sun's position/motion in the Milky Way → the Milky Way's rotation about its own axis → the Milky Way's motion toward the local cluster. All explained by the **same** force/law.
- Moral: a theory gains credibility by holding across scales and across **independent** datasets.

#### Worked illustration B — Tycho Brahe, Mars, and Kepler
- **Data**: the **declination angle of Mars, measured between 1582 and 1600** by **Tycho Brahe**, with the **naked eye** (pre-telescope), from an observatory he built himself (compared to a "Jantar Mantar"-like structure), located on an island in the **Baltic Sea** (frequent rain/snow/cloud → gaps in the data).
- Plotting declination vs. year gives a **cyclic/oscillatory curve with peaks**, peaks reaching roughly **20°–28°** (the 20° line was pointed out on the plot; some peaks go above 20°, one near ~28°).
- At that time: Copernicus' heliocentric principle had been *proposed* but not established; **Kepler's laws had not yet been discovered**.
- **Kepler** later used Tycho's data to conclude the **planets move around the Sun in (almost) elliptical orbits**, which explains the variation of Mars' declination and its "kinks."
- **Key point**: inferring "elliptical orbits" *from* this raw plot requires extraordinary modelling/imaginative ability — that's the difficulty of the inverse problem.
- **Validation**: Kepler had one of the best planetary datasets of the era and verified the same law on **other planets / independent datasets**.
- Kepler's laws are not ad hoc — they ultimately follow from **Newton's law of gravitation combined with Newton's laws of motion**.

#### Worked illustration C — Supermarket / consumer behaviour (data-science analogue)
- **Hypothesis**: "If I go to the supermarket on an empty stomach, my probability of buying potato chips and Coca-Cola (impulse/junk purchases) is higher."
- Problem: this is based only on personal bias → must be **tested with independent data**.
- **Proposed study design**:
  1. Survey a large number of random supermarket-goers **before entry**: are you hungry or not?
  2. Follow/record what they actually buy.
  3. Compare **% of hungry people buying junk/fast food** vs. **% of non-hungry people buying junk/fast food**.
  4. Collect data **over a long period**, because behaviour varies with **time of day**.
- Other candidate causal "theories" for a supermarket visit: routine groceries (empty fridge), casual browsing (full fridge), just entering for the **air conditioning** because it's hot.
- Observable consequences used as data: did they buy **potato chips** or **raw potatoes**?
- Real-world tie-in: phone/app tracking; **Zomato**-type targeted offers timed to when you're likely hungry; Amazon/marketplace recommendations — all built on such inferred causes.

#### Worked illustration D — The ant and the finger (limits of inference)
- You are an ant in an effectively one-dimensional world; a human finger is placed in your path.
- Your data: a gigantic pillar blocks your road; it moves when you move; it has a shiny white surface where it touches the ground.
- Your inferred model: it's a giant animal, the white part is a tooth, it will eat me.
- Reality (inaccessible to you): a human with a brain, playing a prank.
- **Moral**: from limited observations you build a model; **when new data arrives (the finger squashes you, or you climb over it harmlessly) the model is tested and must be updated.** ← This foreshadows **Bayesian updating**.

### 2.5 The three types of inverse problems
All three illustrated with the **US stock market** (historical index data since **1900**).

| Type | Question form | Worked example given |
|---|---|---|
| **1. Hypothesis testing** | Is a proposed statement consistent with the data? | *Observation*: how many times has the US stock market crashed since **1900**? *Hypothesis*: "Once stock-market indices go up, they must eventually come down, and they come down **crashing** (not a soft landing) — crashes are inevitable." First you must **define a metric for what counts as a 'crash'** vs. a mere decline; then test the hypothesis against the historical crash years. |
| **2. Parameter estimation** | What is the value of a parameter, and does crossing a threshold predict an outcome? | *Observation*: the **2007–08** US crash. *Question*: could one have **foreseen/predicted** it by looking at the **TD spread** (one specific metric)? If the parameter goes above/below a threshold, you declare a crash imminent. |
| **3. Model selection** | Among several candidate models that all fit the data, which is best? | Using data **1900–2007** only, build, say, **7 or 8 mathematical models** that all fit the index history well. Which of them would have **predicted the 2007–08 crash**, and which would not? Choose the model that is most consistent/physical/logically justified. |

- **Flagged as important**: **model selection is one of the hardest tasks** in statistics, because it requires certain quantities that are often very difficult or **almost impossible to compute**. To be returned to later in the course.

### 2.6 Why an astronomer teaches statistics (motivation aside)
- Astronomers are among the oldest data scientists; the lecture started with Tycho's dataset.
- Origin of record-keeping: **Sumerian/Mesopotamian clay tablets** were largely **ledgers of food grain** (who gave how much grain, what was received in exchange) — i.e. **data collection for financial purposes came first**; sky observation followed close behind.
- Modern astronomy is highly data-driven and used "big data" long before the term became fashionable. Example: the telescope the instructor works with produces **≈ 7.2 TB of data per second**, requiring enormous transfer/automated-analysis infrastructure.
- Many basic statistical concepts were **developed by astronomers**.
- **Cosmology example of model selection in action**: maps of tiny fluctuations in the **earliest/"baby" phase of the universe** are used to decide which cosmological model fits the data → leads to the presently accepted model of cosmology. Analysis output is typically shown as **error contours on model parameters** from different observational datasets.
- The instructor has taught a course called **Astrostatistics** for ~7–8 years — one of a kind in India, and rare worldwide, despite statistics being essential to astronomy.
- Astronomer-founded / astronomer-staffed analytics organisations cited:
  - **PolyChord** (Cambridge/London; founded by astronomers) — **Bayesian inference**-based solutions for clients from British Rail to UK government economic affairs.
  - **Mix AI** — startup founded by astronomers.
  - **Winton Capital** (UK hedge fund) — many PhDs in astronomy in its data-analytics team, several leading those teams.
  - **Two Sigma** — boasts **200+ PhDs**, including a **2014 Math Olympiad medallist**; many PhDs in astronomy, physics, mathematics.

### 2.7 The concept of Probability
- **Why we need it**: to build the model that explains the data, in the presence of uncertainty.
- **Role of probability** (as stated): probability is central to empirical science because *it allows us to apply logical reasoning to the data in order to deduce, with a particular and **calculable** degree of certainty, properties of the wider universe* (i.e. the overall system generating the observations).
- **The general question probability answers**: **"How do you reason in a situation where it is not possible to argue with absolute certainty?"**
- **No universally agreed definition of probability exists**, even after centuries.
- **The epistemological tension**: in science we want to apply **deductive reasoning** (consequences of general principles, everyday experience, pure mathematics, **Boolean logic**) to problems that actually require **inductive reasoning** — going from effect/observation back to possible cause.

#### Sources of lack of certainty ("random influences")
1. **Noise** — any fluctuation or unwanted interference affecting your data.
2. **Intrinsic randomness / intrinsic quantum randomness** — inherent variability in any process.
   - *Illustration*: two people with identical lives, jobs and surroundings still differ (tie left shoe first vs. right; brush teeth before vs. after breakfast).
   - *Nature illustration*: all petals of a single flower differ; two flowers of the same age on the same tree differ slightly.
3. **Effective randomness of a complex system** — systems deliberately engineered to be unpredictable, e.g. a **lottery machine**: numbered balls in a rotating drum, one drawn at random; built so the outcome cannot be predicted.
- **Consequence**: uncertainty means **many probable causes** can explain a single observation → the number of candidate causes grows → you need probability to draw conclusions.
- **Contrast with determinism**: if a person brushes their teeth at exactly 7:00 a.m. every single day, there is a one-to-one correspondence — a deterministic solution, no probability needed. Real processes have intrinsic randomness, so this doesn't happen.

#### Two stances on probability
- **Epistemic stance**: probability is used to describe the property or effect of a system **when the causative circumstances for that property are unknown or uncertain**.
  - *Example*: the **age of the universe = 13.7 billion years ± (some uncertainty)**. Many different parameter values, or combinations of parameters, in the cosmological model could produce the same age — the causes leading to this observation are uncertain.
- **Aleatory stance**: probability as used in **games of chance** — predicting the future outcome of **random physical processes**. Sub-divided into:
  - phenomena that are **in principle predictable**, and
  - phenomena that are **in principle not predictable**.
  - *Example*: "it will rain tomorrow with **40% probability**" — the number depends on context (month = August; location = central vs. northern vs. southern vs. western India).
- **Key caveat**: all these stances tell you **how probability is used**, not **what it actually is**.

### 2.8 Explicitly deferred to the next lecture
- **Historical development of the idea of probability.**
- **Two specific modern views of probability** (frequentist vs. Bayesian, as implied), including the **usability and drawbacks of each**, and why people still do not agree on what probability is.
- From those views the class will **derive something used on a day-to-day basis in essentially every machine-learning algorithm/application** — i.e. **Bayes' theorem**.

---

## 3. Q&A (points raised in class)

- **"How do you convert raw information into insights?"**
  - First, define what you call *information*. "The Sun rises in the east and sets in the west" is an **observation**, not yet information/insight.
  - From that observation an early human might conclude "the Earth is a fixed flat disc and the Sun and stars revolve around it" — supported by nightly star-position records (cave paintings of star positions do exist).
  - That **condensed conclusion** is what gets passed on as "information", and later peddled as truth — even though the conclusion may be wrong.
  - **Take-away: there is a real difference between raw observation and (inferred) information; conclusions drawn from limited data can be wrong and must be tested against new data.**

- **"In the Mars plot, all the points are joined by a single line — is that valid?"**
  - **No — you should not simply join data points with lines.**
  - In the plot shown, the **discrete points are Tycho Brahe's observations**; the **smooth white curve is NOT a fit/interpolation of those points.** It is itself a dense set of **much later, much more precise telescopic measurements** (last ~60–70 years) of Mars' declination, taken at very small time intervals, so closely spaced that they look like a continuous line. The curve was shifted in time to align with Tycho's epoch.
  - Tycho's points cluster near the peaks because of observing conditions (cloud, rain, snow, time of year, observing site).
  - **Distinction to remember: data points = observation; curve = model or denser observation. Do not conflate them.**

- **"Which year does the declination reach ~20°?"**
  - The declination is in **degrees, not percent**. The signal is **cyclic**, so it reaches 20° in **many** years (e.g. around 1595–1597 in the region discussed); some peaks exceed 20°, reaching ~28°.

- **"Elliptical orbits are not stagnant — the orbit itself changes. Is that why the peaks have different heights?"**
  - **Yes, precisely.** Additional point: the usual textbook picture showing all planets in a single plane is **incorrect** — planets orbit in **different planes**, tilted with respect to e.g. the Sun–Earth plane, and the overall motion is more like a **spiral** than a simple closed ellipse. This produces the varying angular deviations seen in the declination data.

---

## 4. Exam / assignment notes flagged in this session

- **Mid-term** (joint, Majumdar + Arshad) delivered on the **LMS portal**; worth **~45–50% of total grade**; the other ~50% is decided post-mid-term by two other faculty.
- **Format**: overwhelmingly **problem-solving, essentially no theory questions**; MCQ, fill-in-the-blank, numeric/percentage/probability answers; **proctored**; **question and option order may be randomised**.
- **Integrity warning**: no copying, no AI assistants.
- **Assignments**: posted on and submitted via **LMS**; all slides and supporting material also posted there.
- **Study advice**: after each lecture, read/skim the corresponding sections of **Sheldon Ross**, focusing on the **worked examples and problems**.
- **Conceptual emphasis for the course**: **Bayes' theorem** is the single idea the instructor will stress most, because of its pervasive use in machine learning — expect it to be central in the coming lectures.
- **Flagged as hard / to revisit**: **model selection** given observational data.