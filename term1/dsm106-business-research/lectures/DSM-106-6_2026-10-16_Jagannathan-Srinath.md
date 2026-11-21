---
course: DSM 106
date: 2026-10-16
start: 7:00pm
session: "6"
faculty: Jagannathan Srinath
---

<!-- nav -->
← [Session 5 (2026-10-12)](DSM-106-5_2026-10-12_Jagannathan-Srinath.md) · [All lectures](./) · [Session 7 (2026-10-19)](DSM-106-7_2026-10-19_Jagannathan-Srinath.md) →
<!-- /nav -->

# DSM-106 Business Research, Session 6 (16 Oct 2026): Causal Mapping, Cognitive Distance and MDS

## Overview

This session finished the **causal mapping** method from the previous class. In this method, respondents pick a subset of issues from a list and draw signed, weighted connections between them. Each map becomes a matrix, and two people's matrices are compared with a **cognitive distance (distance ratio)** formula. The instructor worked an Excel example comparing two former students, **Aditya** and **Ion**. The numerator was $18$, the denominator $48$, and the cognitive distance $0.375$, which falls in the "functional" band. He then explained how to interpret cognitive distance in groups: groupthink, functional, threshold and dysfunctional bands.

He applied this to a **case study from the reading**: a UK voluntary-sector healthcare organisation that contracts for the NHS and had to adapt to price-based competitive tendering after 2010. Cognitive distances among its top managers, trustees and middle managers were plotted with **multi-dimensional scaling (MDS)**. The plot showed factions and incoherent strategy. The class then looked at how an 18-month consultant intervention produced convergence among the top managers. The session ended with a data-collection task: a laptop preference spreadsheet to be analysed on Monday.

---

## Topics Covered (in order taught)

### 1. Recap: the causal mapping data-collection method

- In a typical exercise, respondents get about **50 issues** and choose about **10**.
- They then **draw connections (a map)** among their chosen issues.
- The method sits between the two usual tools:
  - more detailed than a survey;
  - less detailed than an interview.
- Each map is reduced to a **matrix**. Matrices can then be compared to see whether people think alike or differently.

**Coding scheme for relationships (edge weights):**

| Relationship | Code |
|---|---|
| High positive | $+3$ |
| Moderate positive | $+2$ |
| Low positive | $+1$ |
| No connection indicated | $0$ |
| Low negative | $-1$ |
| Moderate negative | $-2$ |
| High negative | $-3$ |
| Issue **not chosen** by the respondent | $100$ (an arbitrary high placeholder; could equally be "NA") |

### 2. Worked classroom example: the Excel causal map data

This was a classroom version with a smaller list: **15 issues**, and each person chose **5**. The data came from an earlier MS-DSM batch.

**Issues referenced:**

| No. | Issue |
|---|---|
| 5 | Shame |
| 7 | Empowerment |
| 8 | Hope |
| 9 | Autonomy |
| 10 | Self-confidence |
| 11 | Micromanagement |
| 12 | Fear of failure |
| 13 | Family support |

**Aditya (Person A)** chose issues $7, 9, 10, 11, 12$: empowerment, autonomy, self-confidence, micromanagement and fear of failure. The class interpreted four of Aditya's relationships:

- **$9 \to 11 = -2$** (autonomy to micromanagement):
  - As autonomy increases, micromanagement decreases **moderately**.
  - Micromanagement means excessive control.
- **$11 \to 7 = -1$** (micromanagement to empowerment):
  - As micromanagement increases, empowerment decreases, but only to a **small extent**.
  - This is weaker than $-2$ or $-3$.
- **$11 \to 9 = -3$** (micromanagement to autonomy):
  - As micromanagement decreases, autonomy increases to a **high extent**.
- **$11 \to 10 = +1$** (micromanagement to self-confidence):
  - Aditya believes micromanagement increases self-confidence to a **low extent**.

**Key point: maps are directional and asymmetric.** $9 \to 11 = -2$ but $11 \to 9 = -3$. Two variables can affect each other, but not in the same proportion. The cell $a_{ij}$ (row $i$, column $j$) is the impact of issue $i$ on issue $j$.

**Ion (Person B)** chose issues $5, 8, 10, 12, 13$: shame, hope, self-confidence, fear of failure and family support.

**Counting the issues:**

- **Common issues:** $10$ and $12$, so $p_c = 2$.
- **Unique to Aditya:** $7, 9, 11$, so $p_{uA} = 3$.
- **Unique to Ion:** $5, 8, 13$, so $p_{uB} = 3$.

### 3. Computing the cognitive distance (distance ratio): step by step

**Step 1: Absolute difference matrix.**
- Subtract cell by cell: $|a_{ij} - b_{ij}|$.
- Only the magnitude matters, not the sign.

**Step 2: Recode cells involving 100 that should be $0$.**
- Some cells show $100$. This happens when an issue was not chosen by one person, and the other either also did not choose it or chose it but assigned no relationship ($0$).
- Example: the impact of $5$ on $8$ appeared as $100$. One person had not chosen the issue; the other had chosen it but marked no value.
- All such $100$s are recoded as **$0$**.

**Step 3: Recode large residual values as $1$.**
- Values such as $97, 98, 99, 101, 102, 103$ remain. They arise when one person did not choose the issue (code $100$) and the other assigned a non-zero value.
- Examples:
  - $|100 - 3| = 97$
  - $|100 - (-3)| = 103$
- The rule from the reading: such a difference counts as at most **$1$**, so all of these are recoded as **$1$**.

**Step 4: Actual differences stay as they are.**
- Where both people rated the relationship, the true difference is kept.
- Example: cell $10 \to 12$ (self-confidence to fear of failure).
  - Aditya gave $0$ and Ion gave $-3$.
  - The difference is $|0 - (-3)| = 3$.

**Step 5: Sum all cells to get the numerator.** In this example the numerator is $18$.

**Formula (from the reading):**

```math
D(A,B) = \frac{\displaystyle\sum_{i=1}^{p}\sum_{j=1}^{p} \left| a^{*}_{ij} - b^{*}_{ij} \right|}{6p_c^{2} + 2p_c\,(p_{uA} + p_{uB}) + p_{uA}^{2} + p_{uB}^{2} - (6p_c + p_{uA} + p_{uB})}
```

- $a^{\ast }_{ij}, b^{\ast }_{ij}$ are the (recoded) cell values for persons A and B.
- $p$ is the total number of issues, so $i, j$ run from $1$ to $p$.
- $p_c$ is the number of common issues.
- $p_{uA}$ and $p_{uB}$ are the numbers of issues unique to A and to B.
- The difference rule: $|a^{\ast }_{ij} - b^{\ast }_{ij}| = 1$ if one person did not choose the issue while the other chose it and gave it a value. Otherwise use the actual difference.

**Denominator with $p_c = 2$, $p_{uA} = 3$, $p_{uB} = 3$:**

```math
6(2)^2 + 2(2)(3+3) + 3^2 + 3^2 - (6\cdot 2 + 3 + 3) = 24 + 24 + 9 + 9 - 18 = 48
```

**Result:**

```math
D = \frac{18}{48} = 0.375
```

Notes on this calculation:

- The instructor said "0.0375" once; that was a slip, and the correct value is $0.375$.
- He also said "PC square" once in place of "PUA square" while reading out the formula. The calculation above follows the version that produces $48$.
- He corrected a mistake in the Excel sheet emailed to the class while lecturing. The corrected denominator is $48$, so update your copy.

**Interpretation:** $0.375$ lies in the **functional** band (see below). Aditya and Ion would work well together in the same team.

### 4. Interpreting cognitive distance

The cognitive distance ranges from **0 to 1**:

- **$0$** means two people think exactly alike and share beliefs to a very great extent.
- **$1$** means they think diametrically opposite and share no beliefs.

**Group context:**
- Compute the pairwise distances between all members, for example 8–10 people.
- The **average** of these distances is the group's average cognitive distance.
- The group could be a top management team, a board, senior or middle managers, or a project team.

| Average cognitive distance | Group type | Meaning |
|---|---|---|
| $0$ – $0.15$ | **Groupthink** | One person dominates and others comply. Diverse perspectives are not mobilised, hidden problems go unrecognised, and decision-making suffers. **Bad.** |
| $0.16$ – $0.40$ | **Functional** | Healthy debate and frank disagreement. A variety of perspectives is considered and decisions are good. **Ideal band.** |
| $0.41$ – $0.70$ | **Threshold** | Diverse views are still considered and decisions can still be good, but the group carries higher risk. It is on the threshold of becoming dysfunctional and could make a wrong decision. **Acceptable but risky.** |
| $0.71$ – $1.0$ | **Dysfunctional** | Too many differences and no agreement on key issues. Politics and infighting rise and people do not respect each other. **Bad.** |

In answer to Rahul's question: **both extremes are bad.** Near $0$ means groupthink and near $1$ means dysfunction. The ideal is $0.16$–$0.40$.

### 5. Case study (from the reading): a UK voluntary-sector healthcare organisation

**Context:**
- The organisation is a well-known healthcare body in the **voluntary sector**, not a private corporation. In the quotes it is called **"Health Change UK"**.
- It was a **contractor for several NHS hospitals**. The NHS (National Health Service) is government-funded.
- In **2010**, the Labour Party lost power after a long period in government (the lecturer said "14–15 years"). The Conservatives came in and changed NHS contracting policy.
- NHS contracts now required **price-based competitive tendering** against private-sector players. A provider wins the contract on price or loses it.
- The organisation therefore had to change its functioning, policies and practices.

**Research question:** Do the organisation's leaders and managers share a coherent understanding of how to respond to the environmental change? Is there strategic coherence or fragmentation?

**Participants:**
- 4 top managers: **TM01, TM02, TM03, TM04**.
- 2 trustees (board-level): **TR01, TR02**.
- 6 middle managers: **MM01 to MM06**.

**Methodology:**
1. Elicit **causal maps** from each person.
2. Compute pairwise **cognitive distances**, giving a distance matrix. This is **not a correlation matrix**, which was a student's initial confusion.
3. Plot the distances visually using **multi-dimensional scaling (MDS)**. The instructor ran this in R.

**Results before the intervention:**

- **Top managers:**
  - Average cognitive distance was about $0.856$, as read out by a student.
  - This is **dysfunctional**: they cannot agree and there is no strategic coherence.
  - An individual pairwise value of about $0.675$ was also mentioned from the matrix.
- **Trustees:** dysfunctional, and the **highest** distance of the three groups. The two trustees are diametrically opposed.
- **Middle managers:** also dysfunctional.

**What the MDS plot showed:**

- **Positions of individuals:**
  - TR01 is at the bottom and TR02 at the top, very far apart.
  - The four top managers spread in four different directions: TM01 on the left, TM02 at the bottom right, TM04 at the bottom, TM03 at the top.
- **Two camps form**, split by a line through the middle of the plot:
  - **Top camp:** TR02, TM03, MM03, MM04.
  - **Bottom camp:** TR01, TM02, TM04, MM01, MM06.
  - **Caught in the middle, belonging to neither camp:** TM01, MM02, MM05.
  - The instructor later listed the camps slightly inconsistently while speaking; the split above is the main version given.
- In the reading's figure, these appear as coloured squares:
  - the **blue square** holds the trustees, at opposite corners;
  - the **red square** holds the top managers, at four corners;
  - the **green square** holds the middle managers, also spread out.
- **Conclusion:** significant infighting and politics, two factions, and no common vision or strategy, all because cognitive distance is high.

**Why the top managers diverge (quotes before the intervention):**

| Manager | Statement (paraphrased) | Focus |
|---|---|---|
| TM01 | Look at competitors we meet in tenders and do what they do better or more cheaply. | **Competition** |
| TM02 | The change of government brought immense changes; government policy is integral to everything we do. | **Government policy** |
| TM03 | Without sufficient funding we can't offer anything; how do we motivate staff so it isn't just "targets, targets, targets"? | **Staff / motivation / people** |
| TM04 | Trustees are frightened of moving into new areas, but we must thrive in an increasingly difficult marketplace. | **Innovation / new markets** |

Four different emphases explain the four different positions in the MDS plot.

**Analogy: Mumbai Indians (IPL).**
- Hardik Pandya won an IPL title with Gujarat Titans and was brought back as Mumbai Indians captain.
- Rohit Sharma (former captain), Suryakumar Yadav (India captain at the time) and Jasprit Bumrah (who had captaincy ambitions) were unhappy.
- Camps formed and a talented team played as "11 individuals". It finished near the bottom of the table in recent seasons.
- The lesson: high cognitive distance leads to poor organisational performance.

**The intervention: consultant for 18 months.**
- The consultant aimed to build consensus among the top managers, trustees and middle managers, so that they prioritise the same issues.
- Shared priorities lower cognitive distance, which allows a common vision and strategy and better performance.

**Top managers after 18 months:**

| Manager | Statement after 18 months | Shift |
|---|---|---|
| TM01 | Service A had 55% turnover and serious problems; after the restructure, Service B had 21% turnover and Service C 6%. These were big wake-up calls for staff. | Competition → also **staff issues** |
| TM02 | 12 months ago the organisation was "myopic", unaware of competitors, and lost contracts; now it understands how competitors compete. | Government policy → **competition** |
| TM03 | Was anxious after losing the Service B contract; winning new contracts last year allayed this. | Staff → **competition / winning contracts** |
| TM04 | Under competitive tendering, if we are not good value or our price differential is too great, we won't win. Knowing competitors' prices is crucial. | Innovation → **competition / pricing** |

**Conclusion:** the top managers are converging, with competition as a shared focus. This shows greater coherence. The case continues next class (Monday).

**Methodology summary to remember:** causal maps, then cognitive distance calculation, then visual plotting by multi-dimensional scaling (MDS).

### 6. Doubt-clearing recap (Jasraj's question): the full Excel pipeline

1. Paste Aditya's matrix, built from her causal map.
2. Paste Ion's matrix.
3. Take the absolute cell-wise difference. Actual differences, such as the $3$ for cell $10 \to 12$, appear at this step.
4. Recode $100$ to $0$.
5. Recode the large residuals ($97, 99, 102, 103$, …) to $1$.
6. Sum the cells to get $18$.
7. Compute the denominator with $p_{uA} = 3$, $p_{uB} = 3$, $p_c = 2$ to get $48$.
8. Divide: $18 / 48 = 0.375$, which is **functional**.

---

## Assignments, Tasks and Exam-Relevant Points

**Task due before Monday's class (laptop preference spreadsheet):**
- A Google Sheet was shared before class. It lists **18 laptop combinations**.
- **Brands:**
  - well-known: Asus, Acer, Lenovo, Apple;
  - a **locally assembled** brand;
  - **Ethos**, an unknown new brand trying to launch.
- **Attributes:**
  - processor (dual-core or quad-core);
  - RAM;
  - hard drive;
  - display size;
  - display quality (normal or HD);
  - touchscreen (yes or no).
- **What to do:**
  - Add your name to a column, as the instructor did with his own.
  - Rate your preference for each of the 18 combinations from $1$ (least preferred) to $10$ (most preferred).
- The analysis method will be taught on Monday. The method was not named, but this set-up is typical of conjoint analysis.
- Dakshish volunteered to help classmates with the task.

**Housekeeping:**
- Use the corrected Excel calculation, where the denominator is $48$. The emailed sheet contained an error.
- Read the assigned reading. It contains the distance-ratio formula, the case study and the MDS figure with the blue, red and green squares.

**No explicit exam statements were made.** Based on emphasis, be able to:
- code causal maps;
- apply the recoding rules ($100 \to 0$, and large residuals $\to 1$);
- compute the distance ratio, including the denominator formula;
- interpret the four cognitive-distance bands;
- explain why both groupthink and dysfunction are bad;
- describe the case methodology (causal maps, cognitive distance, MDS) and the before-and-after findings.

<!-- nav -->
← [Session 5 (2026-10-12)](DSM-106-5_2026-10-12_Jagannathan-Srinath.md) · [All lectures](./) · [Session 7 (2026-10-19)](DSM-106-7_2026-10-19_Jagannathan-Srinath.md) →
<!-- /nav -->
