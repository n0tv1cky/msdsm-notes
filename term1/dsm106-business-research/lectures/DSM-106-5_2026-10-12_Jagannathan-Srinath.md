---
course: DSM 106
date: 2026-10-12
start: 7:00pm
session: "5"
faculty: Jagannathan Srinath
---

# DSM-106 Business Research: Session 5 Study Notes
**Session:** DSM-106-5, 2026-10-12, Instructor: Jagannathan Srinath
**Topics:** Wrapping up the middle-manager cluster analysis case (factor, text and cluster analysis) and an introduction to causal maps

---

## 1. Overview

This session finished the multi-method analysis of 30 middle-level managers that began in earlier classes. In those classes, survey data was reduced by **factor analysis** into two constructs: performance and intention to quit. Qualitative text was scored with the **DICTION** software for creativity (activity) and team play (commonality). All four measures were standardised into **z-scores**, and **cluster analysis** produced **six clusters**.

In this session, students interpreted the six clusters three ways: from the cluster-means table, from a 2-D cluster visual, and from an R-generated Excel sheet mapping each employee to a cluster. The clusters were mapped onto the case's typology (Resonant/Dissonant × Embedded/Disembedded × Champion/Inert), and a targeted **HR retention intervention** was proposed for each type.

The instructor then summarised the main lesson: combining qualitative and quantitative techniques gives richer insights than any single technique.

The second half introduced **causal maps**, a small-sample (about 20 or fewer respondents) data-collection and analysis method. Respondents select key issues from a pre-identified list, draw signed arrows (from $-3$ to $+3$) between them, and the map is converted into a matrix so different people's mental models can be compared. Matrix comparison continues next class (Friday).

---

## 2. Topics and Concepts (in order taught)

### 2.1 Recap: The Middle-Manager Dataset (from previous sessions)

- **Sample:** 30 middle-level managers.
- **Survey:** 7 questions. **Factor analysis** split them into 2 groups (factors):
  1. **Performance** of the manager.
  2. **Intention to quit (ITQ)** the organisation.
- **Qualitative data:** analysed with the text-analysis software **DICTION**. Other qualitative-analysis software could also be used. Two DICTION scores were used:
  - **Activity score**, a proxy for **creativity / innovation**.
  - **Commonality score**, a proxy for whether the manager is a **good team player**.
- **Resulting four indicators per manager:** performance, intention to quit, creativity (activity), and team play (commonality).

### 2.2 Standardising with Z-Scores

- **Why:** the four indicators were on different ranges, so they were converted to a common scale.
- **Formula** (standard; the lecture referred to "converting to z-scores" without writing it out):
$$z_i = \frac{x_i - \bar{x}}{s}$$
  Here $\bar{x}$ is the sample mean and $s$ is the sample standard deviation of that indicator.
- **Interpretation scale** (z-scores generally range from $-3$ to $+3$):

| z-score | Meaning |
|---|---|
| $-3$ | Extremely low |
| $-2$ | Low |
| $-1$ | Below average |
| $0$ | Average |
| $+1$ | Above average |
| $+2$ | High |
| $+3$ | Very high |

- **Small-sample caveat:** with only $n = 30$, these fine gradations may not behave as expected. The class therefore used a simple binary rule:
  - $z > 0$ means **high**.
  - $z < 0$ means **low**.
- **Important sign convention for ITQ:** a **positive** ITQ z-score means the person **wants to leave**, not that they want to stay. Rahul initially read this the other way round and was corrected.

### 2.3 Cluster Analysis Output: Six Groups (from the cluster-means table, volunteer Nihal)

| Group | Team play (commonality) | Creativity (activity) | Performance | ITQ | Interpretation |
|---|---|---|---|---|---|
| 1 | Low | Low | Low | Just above average, so wants to leave | Poor on everything and leaving |
| 2 | Low | Above average | Good | Wants to leave | Good, creative performers who are poor team players and want to leave |
| 3 | Good | Good | Good | Wants to leave | Everything good, but they want to leave |
| 4 | Low | Low | Good | Does not want to leave | Good at **routine tasks** but not creative tasks; poor team players; staying |
| 5 | Good | Average to good | Average to good | Does not want to leave | **Ideal group**: you want as many employees here as possible |
| 6 | Below average | Low / average | Low | Does not want to leave | **Problem group**: poor performers who want to stay |

### 2.4 Rahul's Own Supplementary Analysis (Python / Colab)

- Rahul assumed (hard-coded) **2 clusters**, A and B.
  - He noted that cluster count would normally be chosen with the **elbow method**. He said "K nearest neighbours", but the elbow method is normally used with **k-means** clustering. KNN is a classification method.
- He computed standardised scores and **correlation coefficients**, then plotted pairwise relationships among performance, resonance (ITQ-related), commonality (embeddedness / team play) and activity (creativity). He drew them as density-style curves.
- **Findings:**
  - Performance against commonality, and performance against activity: a **steady positive slope**.
  - Resonance against commonality, and resonance against activity: **roughly flat lines**.
- **Conclusion** (as rephrased by the instructor):
  - A high-performing employee is likely to be **creative** and a **good team player**.
  - You **cannot** say anything about intention to quit from team play or creativity.
  - Caveat stated explicitly: **correlation does not imply causation.**

### 2.5 The Case's Six-Category Typology

Rahul noted that the six clusters match the classification given in the case. The building-block definitions are:

| Term | Definition |
|---|---|
| **Champion** | High performance **and** high creativity |
| **Inert** | Low performance **and** low creativity |
| **Resonant** | Low intention to quit (wants to **stay**) |
| **Dissonant** | High intention to quit (wants to **leave**) |
| **Embedded** | Good team player |
| **Disembedded** | Poor team player |

Combining these gives the six categories:

| Category | Performance | Creativity | Team play | ITQ |
|---|---|---|---|---|
| **Resonant Embedded Champions** | High | High | Good | Low (stay) |
| **Dissonant Embedded Champions** | High | High | Good | High (leave) |
| **Resonant Disembedded Champions** | High | High | Poor | Low / moderate (stay) |
| **Dissonant Disembedded Champions** | High | High | Poor | High (leave) |
| **Resonant Inerts** | Low | Low | Moderate / low (unclear) | Low / moderate (stay) |
| **Dissonant Inerts** | Low | Low | Low | High (leave) |

For resonant inerts, the instructor noted we cannot tell whether they are good or bad team players.

### 2.6 Reading the Cluster Visual (2-D plot, volunteer Rahul)

- **Cluster 1** (bottom-left): employees **25, 27, 24, 26, 28**.
  - Team play, creativity and performance are all negative. ITQ is positive.
  - Classified as **Dissonant Inerts**.
- **Cluster 3** (bottom-right, green): employees **2, 12, 5, 7, 11**.
  - Performance, creativity and team play are all high, but ITQ is high (**ITQ $z \approx 0.96$**).
  - Classified as **Dissonant Embedded Champions**.
- **Cluster 5** (top, blue): employees **3, 10, 1, 8, 9**.
  - Everything else stays high, and ITQ is low.
  - Classified as **Resonant Embedded Champions**.
- **How to read the axes of the visual:**
  - **Left to right:** team-play ability, creativity and performance all **improve**. Moving from cluster 1 to cluster 3, ITQ stays high.
  - **Bottom to top:** intention to quit **declines**. Moving from cluster 3 to cluster 5, ITQ falls while the other measures stay high.
- **Value of the visual:** you can see at a glance where any employee sits.

> **Note:** the cluster numbering in the visual does not line up perfectly with the group descriptions in 2.3 (for example, Group 1 in 2.3 was "low on all, ITQ just above average", which matches cluster 1 = dissonant inerts). Rely on the definitions in 2.5 to classify a cluster from its z-score signs.

### 2.7 Employee-to-Cluster Excel Output (R output, volunteer Jasraj)

- R produced an Excel sheet assigning each employee to a cluster. For example, **employee 1 is in cluster 5**.
- **Worked comparison of two randomly chosen employees:**
  - **Employee 9:**
    - Commonality is positive (good team player).
    - Creativity is positive and performance is positive.
    - ITQ is low (does not want to leave).
    - Result: **cluster 5** (resonant embedded champion).
  - **Employee 11:**
    - Good team player, good creativity and good performance, but wants to leave.
    - Result: **cluster 3** (dissonant embedded champion).
- **Policy implications:**
  - **Cluster 5:** safe. These are the employees you want, so keep doing what works.
  - **Cluster 3:** these are good employees at risk of leaving, so **intervene**. Talk to them and ask whether they want a pay rise or something else. Then check whether the organisation can provide it and retain them.

### 2.8 HR Interventions by Category (volunteer Dakshish)

- **Resonant Embedded Champions**
  - These people should never leave. If they do, it signals that the **organisational culture is deteriorating** or the organisation has stopped evolving.
  - Examples:
    - **ISRO:** a very strong organisation. A champion there would leave only if they felt ISRO's positive culture was declining.
    - **Google:** once seen as a "dream company" that would never lay people off. Under competitive pressure it has started layoffs, so even its resonant embedded champions may now leave. This is a cultural question.
- **Dissonant Embedded Champions**
  - If they leave, it reflects the organisation's **failure to "enchant"** or persuade them.
  - Because they perform well, the organisation should actively try to retain them.
- **Resonant Disembedded Champions**
  - These are high performers and highly creative, but poor team players. Such people do exist in organisations.
  - The organisation must **act like a community**: support, accept and acknowledge them. Otherwise they leave.
  - In class the instructor at one point said this group "wants to leave", but by the definition "resonant" means they want to stay.
- **Dissonant Disembedded Champions**
  - Often **eccentric** people with unique personalities who don't gel with others.
  - Retain them by **embracing and accepting their unique personality**, including some eccentricities, and giving them support.
- **Resonant Inerts**
  - They want to stay but perform poorly.
  - Retain them only by **training and learning support**, to **"cognitively transform" their performance**.
  - If that fails, the organisation itself will ask them to leave.
- **Dissonant Inerts**
  - Poor performers who also want to leave.
  - If you want to retain them, provide **peer support**: colleagues help them improve their work and performance.
  - Otherwise, let them go.
- **General principle:** where an employee falls determines the HR intervention. You can also choose not to intervene and let the employee leave.

### 2.9 Summary of the Integrated Analysis (volunteer Manish/"Many")

Three techniques were combined in this exercise:

1. **Factor analysis** on the survey: the 7 indicators were reduced to 2 factors (performance and intention to quit), grouped to capture the maximum information.
2. **Text analysis** (DICTION) on the employee descriptions: activity (creativity) and commonality (team play).
3. **Cluster analysis**: 30 employees grouped into 6 clusters on resonance, embeddedness, creativity and performance, which led to HR interventions.

**Key takeaway:** in business analytics you should combine **qualitative and quantitative data** and **multiple analysis techniques**. One technique alone gives less rich insight. Richer insights allow concrete decisions that create business value.

---

### 2.10 Causal Maps: A New Methodology

**Positioning against earlier methods**

- Factor analysis, text analysis, cluster analysis, the earlier "AB method", the **Van Westendorp Price Sensitivity Meter** survey and similar methods all **scale to large samples** (thousands, 1 lakh, 10 lakh respondents). Big data is not a constraint for them.
- **Causal maps are a small-sample method.**
  - Typical targets: about 10 top managers, top plus key middle managers, about 10 board members, or about 10 large clients.
  - **Sample size should be restricted to roughly 20.** Beyond 20 it becomes difficult to implement.

**When to use causal maps**

- When **surveys** don't work well, because people respond inaccurately or the choices are too limited.
- When **qualitative interviews** don't work well either, because people say whatever they want and the responses are hard to analyse systematically.
- A causal map is a **different, systematic method of data collection**.

**Procedure**

1. **Identify issues.** Run qualitative interviews with about **5–10 people** in the organisation and ask them for issues important to them. Compile **at least 50 issues** (the instructor's own classroom demo used only 15).
2. **Selection.** Give each respondent the list of about 50 issues and ask them to **choose about 10** they consider most important, eliminating about 40.
3. **Draw the map.** The respondent connects the chosen issues (nodes) with **arrows**.
   - Not every pair needs to be connected; they connect only issues they believe are related.
   - Arrows can be **reciprocal** (A to B and B to A, possibly with different values).
4. **Arrow weights** range from $-3$ to $+3$:

| Weight | Meaning |
|---|---|
| $-3$ | Very high negative (inverse) relationship |
| $-2$ | High negative relationship |
| $-1$ | Moderate negative relationship |
| No arrow ($0$) | No relationship |
| $+1$ | Moderate positive relationship |
| $+2$ | High positive relationship |
| $+3$ | Very high positive relationship |

   A negative weight means that if one issue rises, the other falls, and vice versa.

5. **Convert the map into a matrix** $A = [a_{ij}]$, where $a_{ij}$ is the weight of the arrow from issue $i$ (row) to issue $j$ (column):
$$a_{ij} \in \{-3, -2, -1, 0, +1, +2, +3\}$$
   Use $a_{ij} = 0$ where there is no arrow.
6. **Compare matrices across respondents** to find the extent of agreement or disagreement between people. Then derive insights and decide what the business should do to resolve disagreements.

**Important caveat:** a causal map is the respondent's **subjective opinion, not objective truth**. Another person would likely draw a completely different map from the same issues.

### 2.11 Worked Example 1: A Single Causal Map (volunteer Rahan)

- The respondent was given 50 issues, asked for 10, and **chose only 8**.
- **Nodes shown:** 5, 35, 20, 3, 33, 30, 47, 43.
- **Issues listed:** vision and strategic direction; competition in market; knowledge of market needs; bank connections; market share; leadership in organisation; brand recognition; efficiency and productivity.
- **Identified node labels:**
  - **3** = vision and strategic direction
  - **5** = market share
  - **20** = competition in market
  - **30** = leadership in organisation
  - **33** = knowledge of market needs
  - **47** = read out as "vision"
  - The labels for 35 and 43 were not stated explicitly.

**Arrows discussed**

| Arrow | Weight | Interpretation |
|---|---|---|
| 5 to 3 | $+3$ | Market share has a very high positive relationship with vision and strategic direction |
| 30 to 3 | $+3$ | Good leadership gives a very good vision and strategic direction; poor leadership gives a poor one |
| 30 to 47 | $+2$ | High positive |
| 20 to 33 | $+1$ | More competition pushes you to learn more about market needs. Only moderate, because you may lack the capability and other factors also matter |
| 33 to 20 | $-1$ | More market knowledge helps overcome competition. Only moderately, because you also need vision, leadership, brand recognition and efficiency |
| 5 to 20 | $-2$ | High market share lets you withstand competition to a high extent. Not $-3$, because without leadership, efficiency or vision, competitors can still overtake you |
| 3 and 47 | none | According to this manager the two issues are not directly related |

The 20 and 33 pair shows **reciprocal (recursive) arrows with opposite signs**.

**Matrix translation**

- **Row 30:** $a_{30,3} = +3$ and $a_{30,47} = +2$. All other entries in the row are $0$.
- **Row 47:** no outgoing arrows, so the whole row is $0$.
- **Row 5:** $a_{5,3} = +3$. It should also show $a_{5,20} = -2$, but the matrix on the slide **omitted it**. The instructor pointed this out as an error.

Once maps are converted into matrices, you can check whether two people think alike or very differently.

### 2.12 Worked Example 2: Comparing Matrices (Entrepreneur Data, volunteer Mugdha)

- **Data source:** causal maps collected from another class on **what entrepreneurs need to succeed**.
- **Issues:** 15 factors, for example fear of failure, stigma attached to failure, shame if the business fails, and (lack of) confidence.
- Each respondent **chose 5 of the 15** issues and drew causal maps, which were converted into matrices.
- **Coding convention:**
  - **100** (a deliberately large number) means the issue was **not chosen**.
  - **0** means the issue **was chosen** but has no connection on that pair.
  - Otherwise the entry is the arrow weight from $-3$ to $+3$.
- **Respondent "Ion":**
  - Chose issues **5, 8, 10, 12, 13**.
  - Issue 1, for example, is coded 100 because it was not chosen.
- **Respondent "Aditya":**
  - Chose issues **7, 9, 10, 11, 12**.
  - Issue 7 is chosen but has no connections, so it appears as zeros rather than 100.
- **Step 1 of matrix comparison:** read each matrix to determine which issues each person chose and which they did not.
- The next steps of the comparison (measuring agreement and disagreement) are deferred to Friday.

### 2.13 Q&A (Asurul): How Is the Issue List Prepared?

- Through **prior qualitative interviews** with about 5–10 people in the organisation, asking them which issues matter.
- Compile **at least 50 issues**. Each respondent then picks about 10.
- **Full pipeline:**
  1. Qualitative interviews.
  2. Issue list.
  3. Selection of about 10 issues.
  4. Causal map.
  5. Matrix.
  6. Compare matrices.
  7. Insights and business action.
- A **case study** of a business that successfully used this method will be covered later.

---

## 3. Exam / Assignment Pointers

No item was explicitly labelled "on the exam", but the following were emphasised or assigned:

- **Before Friday:** review the Excel sheets the instructor will share. These are the R cluster-assignment output and the causal-map matrices. Try to work out how matrices can be compared, so the Friday discussion goes faster.
- **Know the typology** cold: Champion/Inert, Resonant/Dissonant and Embedded/Disembedded definitions, the six combined categories, and the **HR intervention for each**. This was tested repeatedly via volunteers.
- **ITQ sign convention:** a positive z-score on intention to quit means the person wants to **leave**.
- **Small-sample z-score rule:** with $n = 30$, use $z > 0$ as high and $z < 0$ as low, rather than the $-3$ to $+3$ gradations.
- **Mixed methods message:** be able to name the three techniques (factor, text, cluster) and explain why combining qualitative and quantitative methods yields richer insights.
- **Causal maps essentials:**
  - Small samples only (about 20 or fewer).
  - When to prefer causal maps over surveys or interviews.
  - The steps: 50 issues, choose 10, draw map, matrix, compare.
  - The $-3$ to $+3$ arrow scale, with no arrow coded as 0.
  - The 100 code for unchosen issues.
  - Maps are subjective, not objective truth.
  - Be able to translate a map into a matrix (and spot omissions like the missing $a_{5,20} = -2$).
- **Correlation does not imply causation:** flagged in Rahul's analysis.
- **Next class (Friday):** continue the causal map matrix comparison, followed by a business case study using causal maps.