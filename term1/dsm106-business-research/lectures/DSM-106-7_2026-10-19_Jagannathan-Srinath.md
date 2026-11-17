---
course: DSM 106
date: 2026-10-19
start: 7:00pm
session: "7"
faculty: Jagannathan Srinath
---

<!-- nav -->
← [Session 6 (2026-10-16)](DSM-106-6_2026-10-16_Jagannathan-Srinath.md) · [All lectures](./) · [Session 8 (2026-10-20)](DSM-106-8_2026-10-20_Jagannathan-Srinath.md) →
<!-- /nav -->

# DSM-106 Business Research – Session 7 Study Notes
**Session file:** DSM-106-7_2026-10-19_Jagannathan-Srinath
**Topics:** Causal maps (results and interpretation), choosing among research methods, multidimensional scaling visualisation, conjoint analysis (laptop exercise)

---

## 1. Overview

The session finishes the **causal maps / cognitive distance** case study of a UK healthcare organisation. Its strategic environment changed after 2010, and an 18-month consultant intervention was used to build strategic consensus among its 12 key leaders.

The instructor first answers a student question (Rahul) about **when to use clustering and when to use causal maps**. The short answer is large data versus small groups. He then walks through the Phase 1 vs. Phase 2 results:
- in-direction (ID) scores and rank points,
- the gaps between top-ranked issues as a signal of clarity,
- changes in average cognitive distance within and across hierarchical levels,
- multidimensional scaling (MDS) plots.

The second half introduces **conjoint analysis** using a fictional laptop survey that the class filled in. It covers:
- experimental design: attributes and levels, full factorial versus a reduced 36-profile design,
- respondent fatigue,
- part-worth utilities estimated by multiple regression,
- relative importance of attributes and the 70% cut-off rule,
- market-share simulation for a new brand, "Ethos."

The session ends with a proposed conjoint assignment and preparation for the next class (Whole Foods Market case, financial analysis).

---

## 2. Topics and Concepts (in order taught)

### 2.1 Recap: Cognitive Distance Classification

Cognitive distance (CD) ranges from 0 to 1. The interpretation bands are:

| Cognitive distance | Group type | Interpretation |
|---|---|---|
| $0 \le CD \le 0.15$ | **Groupthink** | One person dominates. Diverse perspectives are ignored. Unhealthy. |
| $0.16 \le CD \le 0.40$ | **Functional group** | Different perspectives are considered. Frank debates take place. Decisions rest on diverse opinions. Ideal. |
| $0.41 \le CD \le 0.70$ | **Threshold group** | Still acceptable. Diversity of views and strong decision-making. Risk: it may cross 0.7. |
| $0.71 \le CD \le 1$ | **Dysfunctional group** | Too many differences: politicking, factions, anxieties. Coherence is lost and no coherent strategy emerges. |

### 2.2 Recap: The UK Healthcare Organisation Case

**Context**
- The Labour Party, in power for a long period, lost power in **2010**.
- The Conservative government changed the NHS system to rely on **competitive tendering**.
- The organisation had long received contracts from several healthcare-sector organisations. It now had to compete with other organisations **on cost** to win tenders. This was a new strategic challenge.

**Participants (12 key people)**
- 2 trustees
- 4 top managers (TM01–TM04)
- 6 middle managers (MM01–MM06)

**Method**
- Each person chose **10 issues out of 50**.
- Each drew a causal map linking those issues, with arrow magnitudes and signs.
- The maps were converted to matrices, and cognitive distances were computed.

**Phase 1 (before intervention): average cognitive distance**
- Between the 2 trustees: $0.97$
- Among the 4 top managers: approximately $0.85$–$0.86$
- Among the 6 middle managers: approximately $0.80$
- All are above 0.7, so the groups were dysfunctional and the organisation could not adapt strategically.

**Intervention**
- Consultants worked with all 12 people for about **1.5 years (18 months)**.
- The result was more consensus on strategic priorities. Qualitative quotes from top managers showed greater agreement.

### 2.3 Student Question: When to Use Clustering vs. Causal Maps (Choosing a Method)

**Recap of the case studies so far**

1. **Basecamp (marketing/pricing case)**
   - **Experiment (A/B test), a field experiment on price.** Large sample: more than about 5,000 people registered, about 1,600 in the control group, and many in the treatment group.
     - Weakness: customers who see different prices complain to customer support, and the firm has to explain it was an experiment.
     - So a price experiment can be run **only once or twice, for brief periods**.
   - **Survey: Van Westendorp Price Sensitivity Meter**, with about 700–800 responses.
     - Consumers show **anchoring bias**. A consumer already paying a price is unwilling to say they would pay more.
     - Raw results therefore tend to say "reduce the price," which may not be in the firm's interest.
     - Solution: interpret the results using **interquartile ranges**. These show how far consumers are willing to stretch the price, which tells the firm how much it can raise prices.

2. **Employee attrition (HR case)**
   - Survey interpreted with **factor analysis**, which groups the survey questions.
   - **Text analysis** of performance appraisal text.
   - **Cluster analysis** of employees, so that different HR interventions can target different clusters.
   - The demo used 30 employees, but the method scales. Example given: an organisation with **3 lakh (300,000) employees**.

3. **Healthcare organisation (causal maps)**: the current case.

**Answer**

- **Large-data methods**: experiments, interquartile ranges, factor analysis, text analysis, cluster analysis. Use these with large-scale survey or text data covering thousands of respondents.
- **Causal maps** suit **small data**, typically **20 or fewer people**:
  - top management teams,
  - boards,
  - key R&D project members.
- **Causal maps are also an intervention methodology.** They are used to build consensus, agreement, a common vision, and strategic coherence.
- **Why causal maps sit between surveys and qualitative interviews:**
  - A survey gives respondents **too little autonomy**. They are forced into the questionnaire and cannot express their own perspectives.
  - A qualitative interview gives respondents **too much autonomy or discretion**, even when analysed systematically with software such as DICTION.
  - A causal map is the **middle path**. It combines respondent autonomy (choose 10 of 50 issues and draw your own map) with structured, systematic data collection and analysis (matrix, cognitive distance).
- **Realistic expectations:**
  - Cognitive distance does not fall in a day. It took 18 months in this case.
  - It will not drop dramatically (for example, from 0.85 to about 0.36–0.37).
  - Even a **10–15% reduction** makes the group much more manageable.
- **Other applications:** sports teams, family counselling, and any small-group setting where you want better group dynamics.

### 2.4 In-Direction (ID): Measuring Issue Importance

**Definition:** The **in-direction (ID)** of a node (issue) in a causal map is based on the arrows **coming into** that node.

- A node with many incoming arrows is a more important issue.
- ID is computed by **summing the magnitudes** of incoming arrows. **Signs are ignored** (whether + or −, only the magnitude counts):

$$ID_j = \sum_{i \to j} |w_{ij}|$$

where $w_{ij}$ is the weight of the arrow from issue $i$ to issue $j$.

**Worked example (one causal map, with student Nihal)**
- **Node 3** has the most incoming arrows: 3 arrows. Their magnitudes sum to $ID_3 = 8$.
- Node 20 has only 2 incoming arrows, as the instructor corrected.
- Only arrows coming *into* a node count. Arrows going out do not.

**Aggregating:** Add the ID values across all **12 causal maps** to get each issue's total ID score (for example, 87 and 64 in the table).

### 2.5 Rank Points

Each respondent also **ranked** their 10 chosen issues. Points were assigned as follows:

| Rank | 1 | 2 | 3 | 4 | … | 10 |
|---|---|---|---|---|---|---|
| Points | 10 | 9 | 8 | 7 | … | 1 |

In formula form:

$$\text{Points} = 11 - \text{rank}$$

The points are summed across the 12 respondents to get each issue's total rank points.

**ID vs. rank points**
- The two measures usually correlate broadly but can conflict.
  - Example: issue 4 had lower ID than issue 3 but a higher rank than issues 3 and 2.
- **Conflicts are resolved by prioritising ID.** In the causal map methodology, ID is considered the more important measure.

### 2.6 Phase 1 vs. Phase 2 Issue Tables (Interpretation)

**Top four issues by ID**

| Rank | Phase 1 (before) | ID | Phase 2 (after 18 months) | ID |
|---|---|---|---|---|
| 1 | Helping clients achieve recovery | 87 | **Service quality** | 125 |
| 2 | Target focused | 64 | Helping clients achieve recovery | 60 |
| 3 | Planning ahead | – | Motivation of staff | – |
| 4 | Service quality | 43 | Relationship with partners | – |

- "Service quality" rose from **43 to 125**.
- "Helping clients achieve recovery" fell from **87 to 60**.

**Insight 1: The gap between issue #1 and issue #2 measures clarity**
- Phase 1 gap: $87 - 64 = 23$. This is narrow, so the group was confused and could not clearly prioritise the top issue.
- Phase 2 gap: $125 - 60 = 65$. This is wide, so there was clear prioritisation. All 12 now agree that **service quality** is the most important issue.

**Insight 2: The gap between issue #4 and issue #5 shows whether the "top 4" is clear**
- Phase 1, issues 4 onward: ID values of about **43, 41, 37, 36, 35, 33**. The differences are tiny, so the top four could not be clearly distinguished from the rest.
- Phase 2, from issue 4 onward: values were read as about **56, 45, 31, 28, 27**. Points drop off sharply after the top four. The same separation appeared in rank points (figures read as roughly 18 vs. 40 and 31 vs. 45).
  - *Note:* The exact Phase 2 numbers are unclear in the transcript. The key idea is a large drop after the 4th issue in both ID and rank points.
- **Conclusion:** After the intervention, the organisation could clearly name both the **single most important issue** and the **top four issues**. It could do neither before.

**General rule:**
- Large gaps between successive ranked issues mean consensus and clarity.
- Small, evenly spaced gaps mean confusion and an inability to prioritise.

### 2.7 Change in Cognitive Distance After Intervention (with student Ashi)

| Group | Phase 1 | Phase 2 | Phase 2 category |
|---|---|---|---|
| All 12 people (average) | $0.813$ | $0.726$ (about 0.72) | Still dysfunctional, but improved |
| 2 trustees | $0.97$ | $0.67$ | Threshold |
| 4 top managers | about $0.85$–$0.86$ | $0.69$ | Threshold |
| 6 middle managers | about $0.80$ (dysfunctional) | reduced into threshold range | Threshold |

**Key lessons**
- The overall reduction is about 10% ($0.813 \to 0.726$). This is a realistic improvement for experienced people with 15–20 years in their roles. The instructor expects reductions of about 10–20%, not dramatic ones.
- **Change management proceeds within hierarchical levels first, then across levels.**
  - Consensus forms first among peers: trustees with trustees, top managers with top managers, middle managers with middle managers.
  - Over time, cross-level consensus grows. The overall 0.726 is likely to fall into the threshold range eventually.
- The threshold category is acceptable. People can debate and disagree but still reach fruitful conclusions.

### 2.8 Visualisation via Multidimensional Scaling (MDS) (with student Jessica)

**Phase 1 MDS plot**
- **Blue square (trustees):** the 2 trustees sit diagonally opposite each other, showing a huge distance.
- **Red square (top managers TM01–TM04):** spread in four different directions.
- **Green square (middle managers MM01–MM06):** spread all across the square.
- A horizontal line through the middle splits the plot into top and bottom halves. These represent **two conflicting factions**, which the instructor called "gang war" inside the organisation. This destroys value.

**Phase 2 MDS plot (after 18 months)**
- Trustees, top managers, and middle managers each **cluster closely within their own level**. They are now "on the same page" and prioritising similar issues.
- They are in the threshold group, not the functional group, so they have healthy disagreements that converge.
- Convergence **across** levels is not yet achieved and will take more time.

### 2.9 Methods Recap So Far

The course has now covered:
1. Experiments / A/B testing
2. Price sensitivity meter (Van Westendorp) with interquartile range analysis
3. Factor analysis
4. Text analysis
5. Cluster analysis
6. Causal maps and cognitive distance
7. Multidimensional scaling (visualisation)
8. Qualitative interviews and quotes
9. **Conjoint analysis** (introduced today)
10. Financial analysis (next session)

---

### 2.10 Conjoint Analysis: Laptop Case (Fictional Design)

**Research question:** A **new laptop brand, "Ethos,"** is about to launch. The firm wants to know:
- which features consumers value,
- how much each feature level is worth,
- what market share Ethos could win against established brands.

**Step 1: Experimental design (attributes and levels)**

There are **7 attributes**, with the levels vector written in the code as **6, 2, 3, 3, 3, 2, 2**:

| # | Attribute | No. of levels | Levels |
|---|---|---|---|
| 1 | Brand | 6 | Apple, Lenovo, Acer, Asus, **Ethos** (new brand), **Other** (locally assembled) |
| 2 | Cores | 2 | Dual core, Quad core |
| 3 | RAM | 3 | 4 GB, 8 GB, 16 GB |
| 4 | Hard drive | 3 | 256 GB, 512 GB, 1024 GB |
| 5 | Display size | 3 | 12 in, 14 in, 15.2 in |
| 6 | Display quality | 2 | Normal, HD |
| 7 | Touchscreen | 2 | Yes, No |

**Full factorial (all possible combinations):**

$$6 \times 2 \times 3 \times 3 \times 3 \times 2 \times 2 = 1296$$

No respondent can rate 1,296 profiles, so this is infeasible.

**Reduced (optimal) design:**
- The computer generated an **optimal design of 36 profiles**. The instructor first said 18, then corrected himself to 36.
- The 36 profiles still cover every level of every attribute in combination with others. For example, Asus appears with dual and quad core; 4, 8 and 16 GB; 256, 512 and 1024 GB; 12, 14 and 15.2 in; Normal and HD; with and without touchscreen.
- **36 is the minimum** that captures all combinations for this design.

**Data collection**
- Respondents rated each profile on a **1–10 scale**. Alternatives are a 1–5 scale or ranking all profiles.
- In real-world practice, firms show **pictures** of each profile (for example, cycling through them on a tablet) or even the physical products.
- Class response: only **9 of about 28–29 students** responded (labelled V1–V9). The instructor also kept backup data from 89 other people.

**Respondent fatigue**
- More profiles mean fewer responses and more random answers. Even 36 caused fatigue; Mohammad, one respondent, confirmed this.
- Remedy: split the task into batches of **5–6 profiles per sitting**, run across 5–6 rounds.

**Two cautions about today's results**
1. The sample size is too small ($n = 9$).
2. Respondents were fatigued, so some answers are random.

**Step 2: Part-worth utilities, estimated by multiple regression**
- Ratings are regressed on the attribute levels using multiple regression models.
- The output is a **utility** for each level, measured in **utils**. This was linked to the economics idea of the law of diminishing marginal utility (discussed with student Jasraj).

Results from the class data of 9 respondents (several are counter-intuitive, which shows the randomness):

| Attribute | Finding |
|---|---|
| Brand | **Acer has the highest utility.** One brand had the lowest utility (likely Asus; unclear in transcript). Apple's utility was surprisingly low, below locally assembled "Other." The instructor said this is unlikely in reality. |
| Cores | Dual core preferred over quad core. Highest core utility was about **0.5**. |
| Display quality | Normal preferred over HD. Highest utility only about **0.1**. |
| Display size | **14 in preferred.** 15.2 in seen as too bulky, 12 in as too small. The instructor considered this plausible. |
| Hard drive | All levels had essentially **zero utility**, so no distinction. |
| RAM | 8 GB preferred. Surprisingly, 4 GB was also rated above 16 GB. |
| Touchscreen | Preference unclear in transcript. |

Comparing utility ranges across attributes gives a rough hint of importance. For example, cores (max about 0.5) appear more important than display quality (max about 0.1). Relative importance must be computed formally to be sure.

**Step 3: Relative importance of attributes (%), summing to 100%**

| Attribute | Approx. importance |
|---|---|
| Brand | about 40% (most important) |
| Cores | about 15–17% |
| RAM | about 15% |
| Display size | about 12–13% |
| All others | below 10% each |

- *Standard formula (not stated explicitly in class):*

$$\text{Importance}_k = \frac{\max(u_k) - \min(u_k)}{\sum_{m}\left[\max(u_m) - \min(u_m)\right]} \times 100\%$$

- **70% rule:** Take attributes in order of importance until the cumulative total crosses **70%**. Those are the attributes to concentrate on and build strongly.
  - Brand + cores + RAM ≈ 40 + 15 + 15 = **about 70%**, which is borderline.
  - Adding display size decisively crosses 70%.
  - So **focus on brand, cores, RAM, and display size**.

**Step 4: Market share simulation**
- The firm cannot easily change Ethos's brand utility, since that requires advertising. It *can* control the other features (display quality, touchscreen, hard drive, and so on).
- So it builds the **best feature combination** for Ethos and simulates market share against the other brands.
- Results:
  - **Acer** has the highest share, consistent with its highest brand utility.
  - **Apple** has a low share.
  - **Ethos** reaches about **10% market share**, matching Apple.
  - **Other** (locally assembled) also has a good share.

**Missing attribute: price**
- Price was not included because this was a fictional design.
- In real studies, **price should be included** so the analysis can identify the launch price point.

**What conjoint analysis delivers (summary)**
1. The **utility of each level of each feature** (for example, 4/8/16 GB RAM; 256/512/1024 GB disk; touchscreen yes/no).
2. The **relative importance** of attributes (for example, is brand more important than display size?).
3. **Market-share simulation** for a new product configuration and price point, which helps position a brand in the marketplace.

---

## 3. Exam and Assignment Pointers

**Assignment (proposed; the formal question will be framed and shared later)**
- Run a small conjoint survey yourselves, either inside the class or outside it.
- Example suggested: launching a **new soft drink** against existing ones, with features such as pack size (500 ml, 200 ml, …).
- Collect **about 20–40 responses**.
- Use **only about 5–10 profiles at most**, not 36, to avoid fatigue.
- Do the conjoint analysis: utilities, importance, simulation.
- The instructor will confirm the assignment in the next class.

**Likely exam and understanding points**
- The cognitive distance bands (0–0.15, 0.16–0.4, 0.41–0.7, 0.71–1) and their labels.
- Case numbers:
  - Phase 1: overall 0.813; trustees 0.97; top managers about 0.85; middle managers about 0.8.
  - Phase 2: overall 0.726; trustees 0.67; top managers 0.69.
  - Intervention length: 18 months.
- How **ID** is computed: sum of absolute magnitudes of incoming arrows, summed across respondents. ID takes priority over rank points.
- How **rank points** are computed: rank 1 = 10 points through rank 10 = 1 point.
- Using **gaps between ranked issues** to judge clarity (87 vs. 64 compared with 125 vs. 60).
- Change happens **within levels first, then across levels**.
- **When to use which method:**
  - Large data: experiments, IQR, factor, text, cluster analysis.
  - Small groups of 20 or fewer: causal maps, as an intervention.
  - Causal maps as the middle path between surveys and qualitative interviews.
- **Conjoint design:**
  - Full factorial = product of levels ($1296$).
  - Reduced optimal design = 36.
  - Respondent fatigue.
  - Utilities via multiple regression.
  - Importance percentages and the 70% cut-off.
  - Market-share simulation.
  - Include price in real studies.

**Next session**
- **Whole Foods Market** case, which begins **financial analysis** as a business research method.
- The case is 13 pages and is in the course material under session 6.
- **Read the first 5 pages** (the exhibits start on page 6) for about 15–20 minutes before class. There is no need to analyse the exhibits; that will be done in class.
- Class is at the usual evening time (7–8 pm) despite the festival.

<!-- nav -->
← [Session 6 (2026-10-16)](DSM-106-6_2026-10-16_Jagannathan-Srinath.md) · [All lectures](./) · [Session 8 (2026-10-20)](DSM-106-8_2026-10-20_Jagannathan-Srinath.md) →
<!-- /nav -->
