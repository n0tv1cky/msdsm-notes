---
course: DSM 101
date: 2026-10-07
start: 7:00pm
session: "23"
faculty: Pritee Sharma
---

# DSM-101 · Session 23: Non-Probability Sampling

**Session file:** DSM-101-23_2026-10-07_Pritee-Sharma
**Topic:** Types of sampling, part 2: non-probability sampling methods
**Next session:** Data and types of data

> **Transcript fixes applied:** "non-robability" = **non-probability**; "Kota sample" = **quota sample**; "Hn / Hnot" = $H_0$ (null hypothesis); "desiles" = **deciles**; "Anderman Nikopars" = Andaman & Nicobar Islands; "Marauti" = Maruti.

---

## 1. Overview

This session continued the discussion of sampling designs. The previous session covered probability sampling (simple random, systematic, stratified). This one covered **non-probability sampling**, in which population elements do not have a known or equal chance of selection, so the sample cannot be claimed to be statistically representative of the population.

The lecturer explained why researchers still use these methods: practicality, cost, rare or hard-to-reach populations, and exploratory research. She then walked through seven methods, each with real-world examples:

1. Convenience / purposive
2. Judgment
3. Quota
4. Cluster / area
5. Multi-stage
6. Sequential
7. Snowball

The convenience-sampling discussion led into a short introduction to **hypothesis formation** (alternative vs. null hypothesis), described as the foundation of the inferential-statistics half of the course. There was also an economics digression on why car showrooms are called "distributors," based on **diminishing marginal utility**.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Probability vs. Non-Probability Samples

**Probability samples** (simple random, systematic, stratified):
- Every element in the **sampling frame** has a known or equal chance of being selected into the final sample.
- They require knowing the full population (universe) and building a sampling frame in which every element has a chance of inclusion.

**Non-probability samples:**
- Elements do **not** have a known or equal chance of selection.
- **Main demerit:** the sample may **not be representative** of the population. From a strict statistical perspective, you cannot claim representativeness.
- **Why use them anyway:**
  - In many research settings, probability sampling is very difficult or infeasible.
  - They save cost and effort.
  - They let you focus only on the specific problem or population of interest rather than the whole population.
- Any deviation from the probability-sampling requirements leads to a non-probability sample.

---

### 2.2 Convenience Sampling (also: Purposive / Deliberate / "Chunk" Sampling)

**Definition:** The researcher selects units based on ease of access or a specific purpose, not by random selection. The lecturer treated these names as synonyms; note that many textbooks distinguish *convenience* (ease of access) from *purposive* (researcher's purpose).

**Typical use: exploratory research**
- Exploratory research studies a group, community, or phenomenon that has **not been documented before**, so there is no prior literature or evidence. Example: checking whether a new species may exist on an island.
- Common in anthropological studies.
- The research objective determines the sampling type.
- Exploratory research is usually the first step and is used to **develop a hypothesis**.

**Example: an uncontacted community in the Andaman Islands**
- Suppose a community has not interacted with mainstream, economically developed society.
- You first run an exploratory study using convenience/purposive sampling.
- From that study you build a hypothesis, for example: "This community has been exposed to mainstream society."

#### Mini-topic: Hypotheses (preview of inferential statistics)

- **Hypothesis:** a statement the researcher wants to prove true.
- **Alternative hypothesis:** the researcher's own claim, written $H_a$ or $H_1$.
  - Example: $H_a$: the Andaman community *has been* exposed to mainstream society.
- **Null hypothesis:** the negation of the researcher's claim, written $H_0$.
  - Example: $H_0$: the community *has not* been exposed.
  - The lecturer misspoke here ("what would be the alternate hypothesis?") while describing $H_0$; the negation is the null.
- **Rule of thumb:** whatever negates your proposal is the null hypothesis.
- **Hypothesis testing** uses sample statistics to infer whether your hypothesis holds for the population.
- If the evidence supports your claim, you conclude **"the null hypothesis is rejected"**, meaning the alternative is supported.
- **Researcher's goal:** use literature review, exploratory study, and purposive sampling to form a hypothesis, then aim to reject $H_0$.
- The entire second part of the course (inferential statistics) is built on hypothesis testing.

**Other convenience-sampling examples**

1. **Classroom interview:** walk into a class unannounced and interview whoever is present. Not every student had a chance of selection, so it is a convenience sample.
2. **Tourists at a national park / tiger reserve (Travel Cost Method):**
   - The Travel Cost Method is a way to put a **monetary value on a natural resource**.
   - You interview tourists at the gate or in the queue, not inside the park, and only those willing to respond.
   - You record:
     - travel cost from home to the destination,
     - lodging and food expenses,
     - park entry charges.
   - The total spending shows how much visitors value the park.
   - It is a convenience sample because you only reach visitors who are present and willing.
3. **"Roadside research":**
   - In rural surveys, researchers often survey the first village next to the highway.
   - As a result, the same villages and households get surveyed repeatedly.
   - The same thing happens at district, city, and state levels.
   - Joke from the lecture: so much research is done in Kerala that "Kerala is a convenience sample."

---

### 2.3 Judgment Sampling

**Definition:** Selection is based on the **researcher's judgment** of what is representative.

**Example: a car dealer or distributor chain**
- A city (e.g., Delhi, Mumbai, Chennai) has **100** Honda distributors or franchises.
- The researcher decides that **20** specific stores represent the whole chain.
- The study might cover sales, salespersons' customer handling, or persuasion.
- The stores are not chosen randomly; the researcher picks them. That makes it a judgment sample.

#### Digression: Why are they called "distributors"? (Diminishing marginal utility)

**Student answers discussed:**
- **Rahul Nandi:** showrooms display a representative range of a brand's models.
- **Kev:** they sell to other shops or businesses.

The lecturer clarified that a **wholesaler is different**: a wholesaler stocks a commodity and sells to a **retailer**, who sells to the final consumer.

**Her explanation:**
- **Willingness to pay** depends on the satisfaction (utility) gained from consumption.
- Satisfaction in economic terms is called **utility**.
- The **first unit** consumed gives the highest satisfaction.
- With each extra unit (e.g., a second Royal Delicious apple), **total utility still rises, but at a diminishing rate**. This is the law of diminishing marginal utility.
  - A standard formalization (not written in lecture): marginal utility $MU_n = TU_n - TU_{n-1}$. Here $TU$ increases with $n$ while $MU_n$ decreases as $n$ increases.
- Consumers pay the most for their *first* unit. So sellers want to sell a first unit to as many people and places as possible, which means *distributing* widely. Hence the name "distributors."
- This also explains why companies keep adding new features: it lets them tell buyers they are the "first" to own a car with those features.

---

### 2.4 Quota Sampling

**Definition:** Divide the population into **strata** (classes or groups). Then draw sample units from each stratum **in proportion to the stratum's size**. Selection within a stratum does **not** need to be random.

**Worked example: urban households by income group, 10% sampling**

| Stratum | Population size | Sample at 10% |
|---|---|---|
| High-income group (HIG) | 200 | $0.10 \times 200 = 20$ |
| Middle-income group (MIG) | 500 | $0.10 \times 500 = 50$ |
| Low-income group (LIG) | 100 | $0.10 \times 100 = 10$ |
| **Total** | $800$ | $80$ |

General form: $n_h = f \times N_h$, where $N_h$ is the size of stratum $h$ and $f$ is the sampling fraction (here $f = 0.10$).

**Comparison with stratified sampling (its probability counterpart):**
- **Similarities:**
  - The population is divided into strata with roughly homogeneous elements.
  - Strata are **mutually exclusive and non-overlapping**, so no element can belong to two strata.
  - Stratum definitions must be clear so that every element is assigned.
- **Key difference:**
  - In **stratified** sampling, units within each stratum are chosen by **simple random sampling**.
  - In **quota** sampling, within-stratum selection can be purposive or convenient. The only rule is **proportionate size**.

**Student example (Rahul): global income distribution by deciles**
- Arrange countries or populations from poorest to richest.
- Split them into 10 **deciles**.
- Sample 10% from each decile.
- Compare rich-vs-poor shares (a ratio).

The lecturer's feedback: a good example, but it is structurally the same as the HIG/MIG/LIG example, just with 10 groups instead of 3.

---

### 2.5 Cluster / Area Sampling

**Definition:** Group the population by some criterion. Then **select one (or a few) entire group(s)** and survey **all units** in the selected group(s).

**Example 1: flood impact**
- Village households are grouped by location.
- One group lives on the low-lying side, nearest the river or drain.
- To study the economic loss from floods, select that group and interview **all** its households.

**Example 2: AI impact on computer science students** (developed with a student)
- Many colleges run CS programs.
- One college is in the news because its students built something with AI (or because of an AI-related fraud).
- Select that college and interview **all** its CS students.

**Student question:** Is cluster sampling only used when there is an observed impact?

**Answer: no.** The cluster can be defined by an **impact** (e.g., a policy change in taxation or evaluation affecting a group) or by a **shared feature** directly related to the research purpose. Feature-based examples:
- households located near a river bank;
- **industrial clusters**, e.g., the Morbi (Gujarat) ceramic cluster, where you survey all ceramic manufacturers there;
- geographic or economic clusters, e.g., surveying all households in a slum.

The lecturer recommended thinking in terms of a **specific common feature** tied to the research purpose.

**Practical refinement (comparison households):**
- Social science research often also surveys some **unaffected households** (e.g., poor households not flooded).
- This helps separate flood effects from other common factors.
- Example:
  - Both groups may lose **livelihood** if no river crossing is available in the rainy season.
  - Only the flooded group also loses **assets**.
  - So flooded households lose assets plus livelihood, while non-flooded households lose only livelihood.

---

### 2.6 Multi-Stage Sampling

**Definition:** Start with large **primary units**, then break them down into progressively smaller units at successive stages, and sample at the final stage.

**Example: agricultural productivity in India**
1. **Stage 1:** start with states. Keep only **general-category states** (those not under any special clause).
2. **Stage 2:** keep states with more than **30%** of area under agriculture. The lecturer first said 50%, then settled on 30%.
3. **Stage 3:** within those states, select districts with more than 30% of area under agriculture.
4. Continue to smaller units.

**Why the lecturer classifies this as non-probability:**
- States that fail the criterion are excluded.
- Their districts therefore lose any chance of selection, so not every unit has an equal chance.
- Note: standard textbooks often treat cluster and multi-stage sampling as *probability* designs when random selection is used at each stage. In this lecture they are non-probability because stages are chosen by criteria rather than randomly.
- This method is very common in social science research.

**Formula referenced:** agricultural productivity is yield per unit area:
$$\text{Productivity} = \frac{\text{Production}}{\text{Area under cultivation}}$$

**Student question:** Wouldn't including low-agriculture states dilute or lower the statistic?

**Answer:**
- Including all states enlarges the denominator (cultivated area) and greatly increases effort, since you would have to locate and measure small cultivated areas everywhere.
- That is often infeasible.
- **Key point:** non-probability sampling is chosen for **practical reasons**: to save cost and to focus on the problem being addressed rather than the whole population.
- Student's restatement (endorsed): for a study of wheat production, you would not sample states producing negligible wheat. They would act like outliers that pull down the mean. That is precisely why non-probability samples are used.

---

### 2.7 Sequential Sampling

**Definition:** A complex design in which the **sample size is not fixed in advance**. You start surveying and continue until, based on your experience and judgment, you decide enough units are covered.

**Contrast with systematic sampling (probability):**
- In systematic sampling you know population size $N$ and sample size $n$.
- You randomly select a start and then take every $k$-th unit, with $k = N/n$.
- In sequential sampling, $n$ (and sometimes $N$) is not known or fixed in advance.

**Rules of thumb mentioned:**
- Large survey: stop at around **1,000** respondents.
- Rare disease: stop once you find about **30** patients.

**Stopping criterion: saturation** (clarified in response to a student question)
- You do not stop when you "get results." You stop when **new responses stop adding diversity**.

**Worked example: willingness to pay (WTP) for clean drinking water**
- Setting: a rural area without water purifiers.
- Expected WTP range, from prior literature: ₹100 to ₹1,000.
- Observed responses go as low as ₹80 to ₹90 and do not exceed about ₹900 to ₹1,000. New responses keep falling in the same range.
- Suppose you have surveyed **500** households out of a village of **5,000**:
$$\frac{500}{5000} = 0.10 = 10\%$$
- You can stop on either basis:
  - responses are saturating within the range, or
  - 10% coverage is judged sufficiently representative.
- If a problem is very common (e.g., housing in urban areas), responses saturate quickly, so stop when no new types of responses appear.

---

### 2.8 Snowball Sampling

**Definition:** Used when sample units are **hard to find**.
1. Locate one unit.
2. Ask them to refer you to others like them.
3. Those people refer you to more, and the sample grows like a snowball.

**Examples:**
- A very rare religious community or practice: find one household and ask, "Do you know anyone else who follows this?"
- Network-marketing analogy (Amway): customers connect you to other customers, who connect you to more.
- **Sensitive or hidden behaviours** people won't admit publicly, such as bribe-taking or how thieves operate. Once you guarantee anonymity and gain trust, one respondent connects you to the next.

---

## 3. Exam / Assignment Pointers

No explicit exam or assignment instructions were given. The following were emphasized and are likely testable:

- **Core distinction:**
  - In probability samples, every element has a known or equal chance of selection.
  - In non-probability samples it does not, so they **cannot be claimed representative** of the population.
- **Why non-probability sampling is used:** practicality, cost-saving, focus on the specific problem, rare or hard-to-reach populations, exploratory research.
- **Quota vs. stratified:**
  - Both use mutually exclusive, proportionate strata.
  - Stratified uses simple random sampling within strata; quota does not.
  - Know the 200/500/100 → 20/50/10 calculation.
- **Hypothesis notation and logic:**
  - $H_a$ (or $H_1$) is the researcher's claim.
  - $H_0$ is its negation.
  - Supporting your claim means "the null hypothesis is rejected."
  - This underpins the upcoming **inferential statistics / hypothesis testing** part of the course.
- **Cluster sampling:** select an entire group by a common feature (or impact) related to the research purpose, and survey all its units.
- **Why the lecturer classifies multi-stage sampling as non-probability:** units are excluded at early stages by criteria.
- **Sequential sampling:** sample size is not fixed; stop at saturation of responses or at a judged-sufficient coverage (e.g., 10%).
- **Be able to give your own example** for each method. The lecturer repeatedly asked students for original examples and pushed back when an example merely repeated the structure of one already given.

**Next session:** Data and types of data.