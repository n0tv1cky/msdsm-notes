---
course: DSM 101
date: 2026-10-05
start: 7:00pm
session: "22"
faculty: Pritee Sharma
---

# DSM-101 Session 22: Sampling Design, Sources of Error, and Probability Sampling
*Instructor: Pritee Sharma · Date: 2026-10-05*

---

## 1. Overview

This session moved from the basic statistical vocabulary of the previous class (population/universe, parameter, sample, statistic, descriptive vs. inferential statistics, primary vs. secondary data) into **sampling design**. The instructor explained how a researcher moves from a research question to a defined population, then to a sampling frame, then to the actual sample, and finally to the observed responses. Each stage can introduce error. The session catalogued:
- **frame error**, **chance error**, and **response error** (together, sampling error), and
- **non-sampling/measurement error**, which combines with sampling error to give total error.

The session then covered survey-specific **response errors** and **nonresponse errors**. A worked comparison showed why a small sample with a high response rate can beat a huge sample with a low response rate. Finally, it introduced the three **probability sampling methods**: simple random, systematic, and stratified. Each came with a worked example, plus the use of random number tables. The session ended with a discussion of when *non-probability* sampling is more appropriate, which is the topic for the next class.

> **Note:** This session was conceptual. It covered research methodology and sampling, with no probability distributions, CLT, or Bayes' theorem. The only formulas are the systematic-sampling interval and the error decomposition.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap of the previous class
- **Universe/population** vs. **sample**; **parameters** (population values) vs. **statistics** (sample values).
- A census is usually infeasible, so we compute statistics from samples and use them to infer population parameters.
- If the sample is **not representative**, the inferences about population parameters will be wrong. This matters most in **inferential statistics**.
- **Descriptive statistics** only describe the observed sample values.
- **Primary vs. secondary data**: each has merits and demerits, and researchers often combine both.

### 2.2 From research question to sample: the "nested circles" framework
The instructor drew concentric circles. The real proportions differ greatly: the outer circle is much larger than the inner ones.

1. **Population/universe** is defined by the research question.
   - *Example:* For a question about the education system, the population could be **students**, **teachers**, or **education infrastructure/technology**, depending on the question.
2. **Sampling frame** is the set of elements that are eligible and have a chance of being selected.
   - *Example:* For a study of students with a **physical disability**, the frame is restricted to that subgroup.
   - Numbers used: population ≈ 5 lakh to 10 lakh students; sampling frame ≈ 1,000 students.
3. **Sample** is the set actually drawn from the frame using a chosen method (probability or non-probability).
   - *Example:* 100 students drawn from the frame of 1,000.
4. **Response** is the observation or measurement obtained from the sampled units.

**Running example: smartboards with live captions**
- Some classrooms get smartboards that show live captions as the teacher speaks. This helps students with hearing disabilities or limited language skills.
- **Treatment** = installing the captioning smartboard.
- **Treatment group** = students exposed to it.
- **Control (conventional) group** = students in ordinary classrooms.
- **Response** = the outcome measured afterwards, such as exam marks or any other evaluation of learning.
- Experimental designs (multiple treatments, levels of treatment, cross-sectional impact) have **not yet been covered**. The instructor said they will come in a later class or course.

### 2.3 Sources of error in sampling
Each stage of the nested framework has its own type of error.

| Error | Stage | Meaning | Example from lecture |
|---|---|---|---|
| **Frame error** | Defining the sampling frame | The frame is defined wrongly or too loosely | The frame says "physically disabled students" without specifying the type. Students with **visual impairment** would not benefit from on-screen captions, so the frame itself is flawed. |
| **Chance error** | Selecting units from the frame | Selected units are not representative even if their number is adequate | The right *number* of units is selected, but all come from **one geographic region**. |
| **Response error** | Recording observations | Errors when conducting interviews, tests, or evaluations | Mistakes made while recording or measuring responses. |

**Error decomposition (as presented by the instructor):**

$$\text{Sampling error} = \text{Frame error} + \text{Chance error} + \text{Response error}$$

$$\text{Total error} = \text{Sampling error} + \text{Non-sampling (measurement) error}$$

> Standard textbooks often classify frame and response errors as non-sampling errors. Use the instructor's taxonomy for this course, but be aware that other sources may group these differently.

**Researcher's goal: minimise total error.**
- First, **eliminate non-sampling/measurement error**. Be clear about *what* you are measuring and *with which instrument*. The instrument must be:
  - **reliable**,
  - **valid**, and
  - **appropriately constructed** to measure what it is supposed to measure.
- What remains is sampling error. Most sampling methodology is about reducing it, and well-established methods exist for this.

### 2.4 Survey errors: response errors vs. nonresponse errors
In the social sciences these are called survey errors. In natural or experimental sciences, the analogue is **experimental/observational error**, meaning errors in observing or recording data during experiments.

#### (a) Response errors
These are errors that arise from the survey responses themselves.

1. **Subject lies.** The respondent deliberately gives a false answer.
   - *Examples:* "Have you ever used an illegal drug?" or "Have you ever driven a car while intoxicated?"
2. **Subject makes a mistake.** The respondent honestly misremembers.
   - *Example:* "How much money have you invested in the stock market?" A frequent investor may not recall exactly.
3. **Interviewer makes a mistake** in recording or understanding the response.
4. **Interviewer cheats.** The interviewer makes up answers and attributes them to the respondent.
   - This is common with hired **field investigators** who are not invested in the research. They aim to finish schedules quickly and fill in answers mechanically.
   - *Example:* The investigator assumes a household "looks poor" and ticks "No" for "Do you own a refrigerator?" or "Do you own a motorbike?" without asking.
5. **Interviewer effects.** The interviewer's age, gender, race, clothing, mannerisms, or way of asking can influence answers.
   - *Example:* An elderly, conservatively dressed woman asking young people about illegal drug use will get very different answers from a young interviewer in jeans with tattoos and a nose ring.

**Student examples discussed in class (accepted as response errors):**
- **Survey location:** People answer differently at a police station than at a school. Informal settings may encourage honesty.
- **Hotel feedback:** Guests give hurried star ratings without reading the questions, or avoid honest criticism because staff are standing nearby.
- **College feedback:** Students rate the professor highly because the professor is nearby (response bias).
- **Emotional state/mood** of the respondent at the time of answering.
- **Employee burnout or mental-health survey by HR:** Employees under-report anxiety or burnout, fearing they will look like poor employees. They give the expected answer, not the real one.
- **Exercise self-report:** A respondent claims 3 hours of daily exercise when the real figure is under 1 hour, due to social desirability.
- **Anonymous medical lifestyle surveys** (e.g., cancer research): Anonymity can increase honesty about drug or alcohol use. Without an interviewer, the "subject lies to the interviewer" problem is reduced, but survey mistakes can still occur.

**Key distinction: instrument error vs. response error**
- A student suggested that a respondent might understand a question's terms differently from the researcher.
- The instructor classified this as **instrument error**, not response error. Instrument error means the questionnaire or measurement system itself is flawed.
- **Response error** means everything is clear: the question is simple and understandable, the interviewer states it clearly, and the respondent understands it. An error still occurs.

#### (b) Nonresponse errors
- If the **response rate is low**, the people who do respond may differ systematically from the rest of the population, so the sample becomes unrepresentative.
- *Example:* Only educated people interested in environmental conservation respond to an environmental survey. The instructor noted this assumption is itself a stereotype; the relationship need not hold.
- Nonresponse error is **not about wrong answers**. It is about **many people not answering at all**.

**Worked example: which sample is better?**

| | Sample size $n$ | Response rate | Approx. number of responses |
|---|---|---|---|
| Sample 1 | $n = 2{,}000$ | 90% | $0.90 \times 2000 = 1800$ |
| Sample 2 | $n = 1{,}000{,}000$ (10 lakh) | 20% | $0.20 \times 10^{6} = 200{,}000$ |

(The response counts are derived for clarity; the instructor gave only sizes and rates.)

- **Answer: Sample 1 is better.** A small, representative sample with a high response rate is more useful for inference than a large but probably unrepresentative sample.
- The intuition that "bigger $n$ is always better," or that $n \to N$ (approaching a census) guarantees accuracy, is **not true**. What matters is **how representative** the respondents are.

**Illustration of sample size $n$ vs. population size $N$:**
- $n = 100$, $N = 150$
- $n = 20$, $N = 25$
- $n = 20$, $N = 500$

When $n$ is close to $N$, the sample covers most of the population. However, the instructor stressed that representativeness, meaning a well-spread sample with high response, matters more than sheer size.
- *Example:* 50 well-distributed respondents can be better than 250 respondents clustered in one area.

### 2.5 Probability sampling
**Definition:** In probability sampling, every element in the population has a **known (non-zero) chance** of being selected. There are three methods.

#### (i) Simple random sampling (SRS)
- Every element has an **equal** chance of selection.
- SRS suits a **very large population** in which most units are relevant to the question.
- *Worked example (farmers and mandis):*
  - Question: how do **wheat farmers in Madhya Pradesh** choose which mandi (market) to sell in, when mandis are roughly equidistant or transport costs are similar?
  - There are many farmers, and every farmer sells at *some* mandi, so SRS is appropriate.

**Ensuring true randomness: the random number table.**
- Picking a house "randomly" by walking into a village is **not truly random**.
- Use a **table of random numbers** or a **random number generator**.
- *Worked example (horses):*
  1. Number the 380 horses from 1 to 380.
  2. Move through the random number table in sequence.
  3. Accept each number $\le 380$ and **skip any number $> 380$**.
  4. Continue until 100 horses are selected.

**Student examples of SRS:**
- Estimating the average height of a population.
- **Customer-support audit:** From 1,000 complaint tickets, randomly pick 10 to 20 and audit them to judge overall performance.
- Lottery winner selection. The instructor pushed for a genuine research question; the student suggested studying patterns in lottery winners.
- **COVID-19 data:** SRS is valid if sampling from **hospital records of already-confirmed positive patients**. If you trace infections person-to-person (one contact leads to the next), the sample becomes **non-probability**, because not all units have the same chance of selection.

#### (ii) Systematic sampling
1. Choose the **first element randomly**.
2. Then select **every $k$-th element**, where

$$k = \frac{N}{n}$$

Here $N$ is the population (universe) size and $n$ is the desired sample size. Both must be known in advance.

- *Worked example (school attendance):*
  - A village has 5,000 households and 1,000 children enrolled in school.
  - To study how regularly students attend school, and what affects regularity, draw $n = 100$ from $N = 1000$.
  - $k = \dfrac{1000}{100} = 10$.
  - Pick the first student randomly, then every **10th student**.

#### (iii) Stratified sampling
1. Divide the population into **non-overlapping, internally homogeneous groups (strata)** based on a feature on which the population is heterogeneous.
2. Then apply **simple random sampling within each stratum**.

- *Why stratify:* With plain SRS or systematic sampling, you do not know how many units from each group will end up in your sample, so key groups may be under- or over-represented.
- *Worked example (household consumption expenditure on food vs. non-food items):*
  - A rural area has 5,000 households, stratified by income group.
  - A 10% sample is drawn from each stratum (proportional allocation). The per-stratum sample sizes are computed from the 10% rule:

| Stratum | Households $N_h$ | Sample at 10% |
|---|---|---|
| Low income (LIG) | 1,000 | 100 |
| Middle income (MIG) | 3,500 | 350 |
| High income (HIG) | 500 | 50 |
| **Total** | **5,000** | **500** |

- Within each stratum, every household has an equal chance of selection. The overall sample is therefore still a **probability sample**, and it is proportionately representative of each stratum.

### 2.6 When to prefer non-probability sampling (lead-in to next class)
- If the characteristic of interest is **rare** in the population, probability sampling **wastes effort**, because you would interview or test many non-exposed people.
- *Example:* A diabetes drug manufacturer, where only 7 to 10% of the population has diabetes. Surveying the 90 to 93% without diabetes is wasteful, so non-probability sampling is better.
- Conversely, if **most of the population** falls in the relevant category, probability sampling is useful.
  - *Examples:* every farmer sells at some mandi; farmers' fertilizer or pesticide choices.
  - Rare non-relevant cases may drop out, and the sample still represents the population.
- **Contact tracing** (one infected person leading to the next) is a non-probability approach.

---

## 3. Exam/Assignment Notes and Things to Remember

No explicit exam or assignment instructions were given in this session. The following points were emphasised and are likely test material:

- **Population → sampling frame → sample → response**, and the error at each stage: frame error, chance error, response error.
- $\text{Total error} = \text{Sampling error} + \text{Non-sampling (measurement) error}$. Reduce non-sampling error first through a reliable, valid, well-constructed instrument.
- **Response vs. nonresponse vs. instrument error.** Know how to classify a given scenario. A question misunderstood because of its wording is **instrument error**, not response error.
- The five response-error types: subject lies, subject mistake, interviewer mistake, interviewer cheating, and interviewer effects.
- **Sample 1 ($n = 2000$, 90% response) beats Sample 2 ($n = 10^{6}$, 20% response).** Representativeness matters more than size.
- Systematic sampling interval: $k = N/n$.
- **Probability vs. non-probability samples:**
  - Probability sampling gives a known chance of selection; SRS gives an equal chance.
  - Stratified sampling uses non-overlapping homogeneous strata with SRS within each.
  - "Haphazard" selection is not random; use random number tables.

**Coming up:**
- Next class continues the sampling chapter with **non-probability sampling methods**.
- **Experimental designs** (treatment/control, levels of treatment) will be covered later, in this course or another.