---
course: DSM 101
date: 2026-10-03
start: 10:45am
session: "21"
faculty: Pritee Sharma
---

# DSM-101 · Session 21: Descriptive Statistics Foundations and Data Sources

**Lecturer:** Prof. Pritee Sharma, Professor of Economics, School of Sustainability, IIT Indore. The transcript renders the school's name as "Meta Family School of Sustainability." Her examples come mainly from economics, agricultural economics and environmental economics.
**Session file:** DSM-101-21_2026-10-03_Pritee-Sharma

> **Note on scope:** This session was conceptual. It did **not** cover named theorems or distributions. There was no CLT, Bayes' theorem, Gaussian, Poisson, Binomial, or standard-error formula. Those are not in these notes because they were not taught. The only numerical computation was a sample proportion (the LED bulb example). A few standard formulas are included below for reference, and each is clearly labelled as not derived in class.

---

## 1. Overview

This session opens the descriptive statistics part of the course. It first revisits key vocabulary: population ($N$) versus sample ($n$), and parameter ($\mu$, $\sigma$) versus statistic ($\bar{x}$, $s$). It then explains how statistical inference uses sample statistics to estimate population parameters. The lecturer contrasts this with descriptive statistics, which summarises only the sample and draws no conclusions about the population. The second half covers where data come from:

- **Primary data:** surveys, experiments, in-depth interviews, observation and focus groups.
- **Survey modes:** mail, personal, telephone and web, each with its own trade-offs.
- **Primary vs secondary data:** advantages and disadvantages of each, illustrated with Indian data sources (Census, NSSO, IHDS, IMD, Forest Survey of India).

The session ends with a class discussion. Its key point is that whether data count as "primary" or "secondary" depends on who collected them and for what purpose. Most real research combines both kinds.

---

## 2. Topics Covered (in order taught)

### 2.1 Population

- **Definition:** The universe, meaning the entire set of elements under consideration that we want to study, characterise, or draw conclusions about.
  - It includes data we have not fully examined but want to draw conclusions about.
- **Notation:** Population size is written as capital $N$.
- **Examples given:**
  - Every lawyer in the country.
  - All Tamil-speaking women in India.
  - All engineering graduates of Madhya Pradesh.

### 2.2 Sample

- **Definition:** The portion of the population that is available, or made available, for analysis.
- **Representativeness:** A good sample should be representative of the population.
  - Later in this part of the course, the class will study sampling techniques, both **probability** and **non-probability** sampling.
  - They will also study how sampling affects the third part of the course (inferential statistics).
- **Notation:** Sample size is written as small $n$.
- **Worked example (laptops):**
  - A company manufactures 1 million laptops and cannot test every one.
  - It tests a sample of 500 for quality.
  - So $N = 1{,}000{,}000$ and $n = 500$.

### 2.3 Parameter

- **Definition:** A characteristic or feature of the **population**.
- **Examples:**
  - Population mean: $\mu$
  - Population standard deviation: $\sigma$
- **How to obtain one:** You need a **census**, meaning you measure the feature for every member of the population.
  - Example: measuring the height of all engineering graduates in Madhya Pradesh, then computing $\mu$ and $\sigma$.
- **Drawback:** A census is very costly in both time and money. That is why statisticians usually work with samples instead.

### 2.4 Statistic

- **Definition:** A measure derived from **sample** data, not from the population.
- **Examples:**
  - Sample mean: $\bar{x}$
  - Sample standard deviation: $s$
- **Purpose:** Statistics are used to **estimate population parameters**. Hence the phrase "estimated population parameters."
- **Workflow:**

$$\text{draw sample} \;\rightarrow\; \text{compute statistic } (\bar{x},\, s) \;\rightarrow\; \text{estimate parameter } (\mu,\, \sigma)$$

| | Population | Sample |
|---|---|---|
| Size | $N$ | $n$ |
| Mean | $\mu$ (parameter) | $\bar{x}$ (statistic) |
| Standard deviation | $\sigma$ (parameter) | $s$ (statistic) |
| How obtained | Census (costly) | Sampling |

### 2.5 Statistical Inference

- **Definition:** The process of using sample statistics to draw conclusions about population parameters. It is a measure of performance in which a sample measurement is used to estimate a population parameter.
- **Example (generic):**
  - Draw a sample of $n = 1{,}000$ and compute $\bar{x}$ for a feature such as height or weight.
  - Use it to draw conclusions about $\mu$ for a population of about 300 million.
- **Example (election polling):**
  - Pollsters do not ask every voter, because that is too time-consuming and expensive.
  - Instead they survey a representative sample of about **1,000 people** and use those responses to predict the likely winner.
  - The lecturer said: "Why 1,000? That also we will see." This will come in a later session.
- **Worked example (LED bulb quality control):**
  - A manufacturer (rendered as "G" in the transcript) makes $N = 1{,}000{,}000$ LED bulbs per year.
  - It samples $n = 500$ bulbs, and **5** of them are defective.
  - The sample proportion of defectives is:

    $$\hat{p} = \frac{5}{500} = 0.01 = 1\%$$

  - This statistic is used to estimate the true population proportion of defectives. About 1% of the 1 million bulbs may be defective:

    $$0.01 \times 1{,}000{,}000 = 10{,}000 \text{ bulbs}$$

  - The lecturer said "1% of 1 million"; the figure of 10,000 is that arithmetic carried out.
- **Course placement:** Inferential statistics is taught in a **later part** of the course, not this one.

### 2.6 Descriptive vs Inferential Statistics

- **Descriptive statistics:** Computations that summarise and describe **only the sample**.
  - Examples: mean, standard deviation, median, proportions, range.
  - It also includes presenting data as graphs, charts and tables, and the question of how data are collected.
- **Inferential statistics:** Theory and methods for drawing inferences about the population. Descriptive statistics does **not** extend sample calculations to population parameters.
- **Emphasis:** Everything in this part of the syllabus is about describing the sample: how it behaves and what its features are. No inference to population parameters is made here.
- **Example (classroom exam):**
  - A teacher gives an exam to a class of **35 students**.
  - She computes the class average, median grade and standard deviation to assess the class's performance.
  - She makes no inference about the wider university, college or programme. This is descriptive statistics.

### 2.7 Primary Data

- **Definition:** Data compiled by the researcher themselves.
- **Main collection techniques:**
  - Surveys
  - Experiments
  - In-depth interviews
  - Observation
  - Focus groups

**Experiments in natural vs social sciences**

- **Natural sciences** (biology, physics, chemistry) can run fully **controlled** experiments with replications.
  - Example: measuring the melting temperature of solid samples drawn from different places.
  - Example: growing a microorganism culture at a set temperature, relative humidity, or medium.
- **Social sciences** run experiments that are usually not controlled. They involve large populations, and the researcher does not control the "treatment."

**Natural experiment using secondary data (worked illustration)**

- **Question:** How does a government policy of directly transferring unemployment benefits affect household consumption expenditure?
- **Problem:** The researcher cannot introduce the policy and cannot know in advance when it will come.
- **Approach:**
  1. Identify the key variable: consumption expenditure.
  2. Choose units: households, villages, blocks or districts. The lecturer's example used about 1,000 households.
  3. Use existing survey data. Example: NSSO (National Sample Survey Organisation, under the Ministry of Statistics and Programme Implementation), which runs household consumption expenditure surveys covering goods and services.
  4. Suppose the policy was introduced in **2016**. Compare observations from about **3 years before** with about **3 years after**.
- **Why it works:** This mimics a before/after treatment experiment, using secondary data.

**In-depth interviews and observation**

- The researcher personally conducts interviews or makes observations.
- Example: astronomers record events with their own equipment, but also rely heavily on historical secondary records.

**Focus group discussions**

- Used to gather perspectives from different stakeholders.
- Example: "What is the role of education in generating employment in India?" Participants could include teachers, students, employers, employees, and educated people who are unemployed.

### 2.8 Types of Surveys (Primary Data Collection)

| Mode | Advantages | Disadvantages |
|---|---|---|
| **Mail** (originally postal hard-copy questionnaires) | Low cost; can reach many people | Response is outside your control; respondents may not reply |
| **Personally administered** | Researcher interacts directly with respondents | Very expensive (travel, time); **interviewer effect** |
| **Telephone** | Fast; less expensive | Interviewer and respondent cannot see each other; hard to judge whether responses are genuine or the respondent is engaged |
| **Web** | Very fast and inexpensive | Number of responses uncertain; truthfulness uncertain |

- **Interviewer-effect example:**
  - A senior-looking, well-dressed interviewer asks students about cheating in exams.
  - Students may fear their answers will be used against them, so they answer less candidly.
  - A younger, informally dressed, student-like interviewer would likely get different, more honest answers.

### 2.9 Class Discussion: Surveys Students Have Taken Part In

- **Census participation:** Officials visiting a household. The officials said it was not technically the census.
- **Shopping-mall feedback at the billing counter:**
  - Smiley signs or a **10-point scale** (1 = worst, 10 = excellent).
  - Used to measure customer satisfaction on service level, products and staff behaviour.
  - The student noted that such ratings are relative and subjective.
- **Exam-platform feedback form:** Completed after the midterm, rating the experience of the exam portal (web survey).
- **Google Form for a psychology college project:**
  - Collected demographics (including age bands such as 25–30 and 30–35), then mental-health questions.
  - Stated its objective and asked for consent first.
  - Spread person to person (snowball-style), so it was **not random**. It was mainly students' contacts, though it seemed aimed at the working population.
- **Lecturer's takeaways:**
  - Educated people, and people who understand why surveys matter, are more willing to respond.
  - Populations that are contacted too often, or given long and very in-depth questionnaires, often do not respond to web surveys.

### 2.10 Advantages and Disadvantages of Primary Data

**Advantages**

1. Likely to be **more accurate** than secondary data.
2. The **purpose is known** to you, so observations are recorded specifically for your research question.
   - Example: an anthropologist compares villages near a forest with villages far from one. The aim is to see how each interacts with forest resources and how willing each is to conserve them.
3. **Easier to replicate**, since you hold records for every respondent and can repeat the survey (e.g., next year).

**Disadvantages**

1. Very **time-consuming**.
2. Very **expensive**.
3. Sometimes the same researcher cannot replicate it, so it becomes a **one-time study**.
4. If an error occurs or something is missing, it is **hard to identify** afterwards.

### 2.11 Secondary Data

- **Definition:** Data compiled and published by someone else, such as another organisation, researcher or team.
  - Example: Census data, which you did not collect or publish.
- **Key caveat:** The data may have been collected for a **different purpose** than yours.
  - Example: NSSO consumption surveys focus on food and nutrition: grains, vegetables, animal and protein products, purchased versus home-produced food.
  - That serves nutritional poverty or food security research.
  - A researcher studying the unemployment-transfer policy instead wants to know whether extra money went to food or non-food spending.

**Advantages**

1. **Quick to gather**, since it is already published.
2. **Less expensive** than collecting data yourself.
3. **Lets you build on past research.** You can learn from earlier studies that used the same sources and compare across survey rounds.
   - Census: every **10 years**.
   - NSSO: roughly every **4–5 years**, sometimes with intermediate rounds.
4. **Lets you build panel data:**
   - Cases (e.g., District 1, District 2, District 3, … across all districts of Madhya Pradesh) observed over time (e.g., 1990, 1995, 2000, …).
   - Building a panel from primary data is very hard. Repeating observations on the same individuals over many periods is expensive and slow, and researchers face short deadlines.

**Disadvantages**

1. **May be outdated.**
   - Example: The IHDS household survey (rendered "ISDS" in the transcript) has its latest publicly available round from **2012**. A later re-survey has not been published.
   - Poverty or inequality research based on 2012 data and published in 2026 would be considered outdated.
   - COVID intervened, pushing many non-poor households into poverty. Poor households were partly protected by social security and transfer schemes.
2. **Definitions of terms may differ.**
   - Example: Census "occupation" may not match the definition needed for research on occupational hazards or climate-prone occupations.
3. **Units of measurement may differ.**
4. **Scale or aggregation may differ.**
   - Household-level data may be hard to translate into state-level inferences.
   - State-level data hides variation across geographic, agro-climatic or climatic zones within the state.

**Student example (Ashi): environmental and climate data**

- Temperature and global-warming data are better taken from secondary sources such as the **Indian Meteorological Department (IMD)** website.
- Surveying people about temperature gives subjective answers: some feel it is very hot, others do not.

### 2.12 Research-Design Advice

When stating any research problem, be as specific as possible about:

- What element, parameter or variable you are measuring.
- The location and the size.
- Why you are measuring it.
- What impact you expect, and **how you will measure that impact**.
- Why primary or secondary data is the better choice for that variable.

### 2.13 Q&A: Who Counts as Collecting "Primary" Data?

- **Literature, citations and published datasets** used in undergraduate research papers count as **secondary** data.
- **Data from your own research group:** If it has already been published and you reuse it, it is secondary.
- **"Raw vs published" as a rule of thumb:** Roughly acceptable. The cleaner rule is that data **you collect for your own research are primary**.
- **Primary or secondary is relative to the user:**
  - The Ministry of Statistics collects census data. For the ministry it is primary; for us it is secondary.
  - Ministries (Environment & Forest, Statistics, Finance, Water Resources) collect data through their own offices. For them it is primary; once it is posted on their websites, it is secondary for others.
  - A state forest department official studying wildlife movement using the department's own data is doing primary-data research. If the lecturer used the same data, it would be secondary for her.
- **Myntra example:**
  - A company collected customer-feedback data for one purpose and later reuses it for a new product launch.
  - This is still **primary**, because the company collected it itself, even though the original objective was different.
- **Metadata:**
  - The relevance of a data source's objective shows up as either an advantage or a disadvantage. If your objectives match the collector's (e.g., Census age and occupation used for age-and-occupation research), your results are more robust.
  - Agencies publish **metadata** ("data about the data"). It covers the purpose, how the survey was conducted, how households were selected, sample and population sizes, the sampling ratio, and the sampling method used.
  - Use metadata to judge whether their purpose matches yours.
- **Do you need both kinds of data?** It depends, but most social-science research combines them.
  - Worked illustration: "How does infrastructure development affect forest conservation in India?"
    1. India is too big for a nationwide primary survey.
    2. Use secondary data (Forest Survey of India and state forest reports covering 30–50 years) to find the five states with the largest forest area. Madhya Pradesh ranks first or second.
    3. Use the same secondary data to judge which states have conserved or degraded their forests.
    4. Select Madhya Pradesh, for its large forest area and consistent conservation.
    5. Narrow down to districts, then random-sample by forest proximity.
    6. Conduct the **primary** survey.
  - **Purely secondary research example:** Manufacturing-sector studies, such as whether tax rebates for reinvested profits or credit schemes actually turn into investment. These could be supplemented by primary surveys of willing firms.
  - **Purely primary research example:** Field trials of a newly created organic fertiliser or pesticide on crop yield and productivity. This is typical of biological and agricultural sciences.

---

## 3. Exam / Assignment Flags

No specific exam or assignment items were announced. The points the lecturer stressed most were:

- **Notation:** $N$ vs $n$, $\mu$ and $\sigma$ (parameters) vs $\bar{x}$ and $s$ (statistics). Parameters require a census; statistics are used to estimate parameters.
- **"Please remember":** Descriptive statistics in this part of the course is only about the sample. No inference to population parameters is drawn.
- **Statistical inference:** Know the definition and the examples (election polling with $n \approx 1{,}000$; LED bulbs with $\hat{p} = 5/500 = 1\%$).
- **Primary vs secondary data:** Know the definitions, the advantages and disadvantages of each, and that the classification depends on who collected the data.
- **Survey modes:** Know the trade-offs of each, including the **interviewer effect**.
- **Coming later:**
  - Sampling techniques (probability vs non-probability) and representativeness.
  - Why polls use samples of about 1,000.

---

## 4. Formula / Notation Sheet

**Taught in class**

- Population size: $N$; sample size: $n$
- Population mean: $\mu$; population standard deviation: $\sigma$
- Sample mean: $\bar{x}$; sample standard deviation: $s$
- Sample proportion (LED example):

$$\hat{p} = \frac{\text{number of defectives}}{n} = \frac{5}{500} = 0.01$$

- Estimated number of defectives in the population:

$$\hat{p} \times N = 0.01 \times 1{,}000{,}000 = 10{,}000$$

**For reference only (standard definitions, not written out in this lecture)**

- Population mean: $\mu = \dfrac{1}{N}\sum_{i=1}^{N} x_i$
- Sample mean: $\bar{x} = \dfrac{1}{n}\sum_{i=1}^{n} x_i$
- Population standard deviation: $\sigma = \sqrt{\dfrac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}$
- Sample standard deviation: $s = \sqrt{\dfrac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$