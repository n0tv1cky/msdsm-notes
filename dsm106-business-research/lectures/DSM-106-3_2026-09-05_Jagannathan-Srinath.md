# DSM-106 Business Research — Session 3 (2026-09-05)
## Instructor: Jagannathan / Srinath
### Topic: Reducing Survey Items to Constructs — Factor Analysis / Principal Component Analysis (PCA) on a Middle-Manager Attrition Dataset

---

## 1. Overview

This session continues an applied analytics exercise begun in the previous class, built around a survey-based dataset on **middle-level managers** ("attrition" dataset). The survey consists of **7 indicator questions (I1–I7)** answered on a **1–10 scale** (10 = highest score on that indicator, 1 = lowest), with responses collected from multiple raters for each of **30 middle managers**, averaged over a year. The central research question is: **Can these seven survey questions be divided into meaningful groups (constructs)?** Students first proposed groupings intuitively (statistically via correlations, and qualitatively via the meaning of the statements), after which the instructor demonstrated **factor analysis / principal component analysis in R** as the formal statistical technique for grouping survey items. The class interpreted the proportion-of-variance table, the scree plot, the biplot, and the **factor loadings** table, arriving at a **two-factor solution**: I1, I4, I5, I6 = **Performance**, and I2, I3, I7 = **Intention to Quit (IQ)**. The seven items were then collapsed into two composite variables using simple averages, and individual managers were compared on the resulting two-dimensional map. The session closed with a discussion (anchored by a Yves Morieux-style TED talk on cooperation and the 4×100m relay) about why increasing formality/officialdom is a form of organizational withdrawal ("silent quitting") and why clarity, measurement and accountability can destroy cooperation and productivity.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 The case / dataset setup (recap from prior session)
- Survey about **middle-level managers**.
- **7 survey questions / indicators**, labelled **I1 … I7**.
- Data on **30 middle-level managers** (rows), stored in an Excel sheet, read into R; file named **`attrition`**.
- **Scale: 1 to 10**
  - 10 = highest possible score on that indicator
  - 1 = lowest possible score on that indicator
- **Multiple respondents** rated each middle manager; responses **averaged over a year** → each cell is an average rating.
- The dataset also contains **qualitative data**: narrative **descriptions from performance appraisal entries** for each employee (to be integrated in the October session).
- **Research question posed:** *Can these seven survey questions be divided into groups?*

### 2.2 Student-proposed groupings (pre-statistical intuition)
Captured because the instructor treats these as legitimate competing hypotheses:

- **Rahul (statistical/correlational logic):** two groups —
  - Group A: **I1, I4, I5, I6** (scores appear correlated)
  - Group B: **I2, I3, I7** (scores appear correlated)
- **Jasraj (qualitative logic):** same two groups, but justified by content —
  - I1, I4, I5, I6 = **positive descriptors** of a middle manager's performance
  - I2, I3, I7 = **negative** statements / negative impact on the firm
- **Tejas (qualitative, 3 groups):**
  - **Management/Leadership**: I1, I5, I6
  - **Innovation**: I4, I2
  - **Professional behaviour**: I3, I7

**Instructor's point:** different people can propose different groups with different criteria; a statistical procedure is needed to adjudicate.

### 2.3 Why grouping survey questions matters (methodological principle)
- **First analytical move after any survey** is to decide:
  1. *Into how many groups do the questions fall?*
  2. *What does each group actually measure (what construct/label)?*
- Trivial with 7 questions, essential with **50, 60, 70 questions**.
- The technique used: **Factor Analysis**, also referred to in the session as **Principal Component Analysis (PCA)**. (Instructor treats the two names as equivalent for this course.)

### 2.4 Software policy (exam-relevant framing)
- Demonstration done in **R**; the **R code was shared along with the reading**.
- **Knowledge/use of R is NOT mandatory for this course.** This is an *introductory* business research course.
- **What is assessed/important is the INTERPRETATION of results** — "no matter what software is used, the same results will emerge."
- Students are *encouraged* (not required) to experiment with **R, Python, or other open-source software** so they graduate familiar with them.

### 2.5 Reading the PCA output — Proportion of Variance table
Components labelled **Component 1 … Component 7**.

- **Component 1** = the solution in which all items collapse into **one group**; **Component 7** = each question stands alone as its own group (no grouping at all).
- **Core statistical principle stated:** *In statistics, what matters is **variance**. If there is difference, there is information. If everything is the same, there is no information.*
  - Relationship noted: **Variance = (Standard Deviation)²**
- Collapsing 7 indicators into fewer groups **loses information**; the **proportion of variance** tells you how much information is **retained**.

**Actual numbers used in class:**

| Solution | Variance added by that component | Cumulative proportion of variance |
|---|---|---|
| 1 group (Component 1) | **58.39 %** (≈58%) | **58 %** (42% of variance lost) |
| 2 groups (Component 2) | **≈35 %** | **93 %** (58 + 35) |
| 3 groups (Component 3) | **4.7 %** | **98 %** (≈98.4) |
| 4 groups (Component 4) | small increment | **≈99.7 %** |
| … | | |
| 7 groups (Component 7) | — | **100 %** (no information lost) |

- **Vikyat's interpretation:** the series goes 58 → 93 → 98 → 99.7 and then **plateaus**; after that it's **diminishing returns**. He suggests **3 or 4 groups** would suffice.
- **Instructor's rule of thumb (KEY):**
  > **Once cumulative proportion of variance crosses 90%, you can stop.**
  - Here, **2 components already reach 93% > 90%**, so a **two-group solution is acceptable**.
  - Explicitly flagged as **a rule of thumb** — "there is nothing right or wrong about this."

### 2.6 The scree plot (visualisation 1)
- Plot of variance/eigenvalue against component number.
- The **kink / elbow** occurs **after Component 3** — the fall begins after component 3, confirming Vikyat's intuition.
- **But:** statisticians would still argue **two components are enough**, because the 90% threshold is crossed at 2, and the third component adds very little information (its point is "very close to zero").

### 2.7 The biplot (visualisation 2)
- Shows the **item vectors (I1–I7)** and the **30 managers** plotted as numbered points (e.g., 4, 22, 23, 28, 29, 31) in the same space.
- Interpretation (with student Ashraful):
  - One bundle of vectors points to the **right**: **I1, I4, I5, I6**
  - Another bundle points to the **top-left**: **I2, I3, I7**
  - → Visually **confirms the two-group structure**.
- **Managers plotted as points:** the position of each of the 30 managers shows where they lie on the two dimensions.
- **Four-quadrant logic introduced:** treating the two dimensions as axes gives **four binary combinations**:
  1. High on attribute A, low on attribute B
  2. Low on A, high on B
  3. High on both
  4. Low on both
  - (With continuous data there are of course many more gradations.)

### 2.8 Factor loadings table (the confirmatory step)
- Output columns named **RC1** and **RC2** (= **Rotated Component 1 and 2** = Group 1 and Group 2). All other columns in the output ignored for this course.
- **Definition — Factor loading:** the value under each component column indicating how strongly a given item associates with that component.
  - **Range: 0 to 1** (in magnitude); loadings **can be positive or negative** — for this exercise **ignore the sign, consider only magnitude**.
- **Decision rule (rule of thumb, KEY):**
  > **If |factor loading| > 0.5 → the indicator BELONGS to that group/factor.**
  > **If |factor loading| < 0.5 → the indicator does NOT belong to that group/factor.**
  - Noted that some statisticians use stricter cut-offs such as **0.6 or 0.7**; 0.5 is the common rule of thumb.
- **Worked assignment of items (done live with student Minakshi):**
  - I1 → Group 1 (RC1)
  - I2 → Group 2 (RC2) — loading cited as **0.9**
  - I3 → Group 2
  - I4 → Group 1
  - I5 → Group 1
  - I6 → Group 1
  - I7 → Group 2
- **Final structure:**
  - **Group 1 = I1, I4, I5, I6**
  - **Group 2 = I2, I3, I7**
  - This confirms Rahul's and Jasraj's original intuition.

### 2.9 Labelling the factors (construct naming)
Multiple student proposals were entertained — an important part of the method, since **factor analysis gives you groups but NOT names; naming requires domain judgement.**

| Contributor | Label for I1, I4, I5, I6 | Label for I2, I3, I7 |
|---|---|---|
| Ashi | **Loyal** employees (likely to remain and contribute) | **Disloyal / dissatisfied** (likely to leave soon) |
| Rahul | **Performance**-related; **objective**, concrete figures | **Behaviour**-related; **subjective**, judgement-based (e.g., speaking badly, how one is perceived by colleagues) |
| Shivam | Overall **employee performance** | **Job satisfaction** |
| Ashraful | **Personal qualities / leadership** of the manager (interface between top & operational management; assessing applicability of new ideas; working with juniors/subordinates) | **Working environment** — organisational **culture** (I2) and **career growth** (I7) |
| Tejas | **Managerial ability / management & leadership** (coordination, evaluating ideas, motivating, giving direction) | **Organisational / professional behaviour** |
| **Instructor (adopted)** | **PERFORMANCE** | **INTENTION TO QUIT (IQ)** |

- Related literature pointer: loyalty is studied in the literature as **organizational commitment**, with different kinds/types of commitment.

**Instructor's justification for "Performance" (I1, I4, I5, I6):** These items capture what is expected of a middle manager —
- being an **interface between top and operational management**
- **accurately assessing the potential applicability of new ideas**
- **energizing people** around him/her
- **demonstrating clarity and commitment**
→ A well-performing middle manager scores high on all four; a poor performer scores low.

**Instructor's justification for "Intention to Quit" (I2, I3, I7):**
- Labelled as **intention**, **not behaviour**.
- **Theoretical basis (psychology / organizational behaviour):** *Intention precedes behaviour.* First the intention is formed; then the person acts. **Behaviour = action.**
- **Empirical regularity cited:** after the intention to quit forms, the **average lag before actually quitting is about 6 months** (broadly **6 months to 1 year** absent exceptional circumstances); in exceptional cases a person may quit within an hour or immediately.

### 2.10 Constructing the composite variables
- Options for combining items into a construct score:
  1. **Weighted average** using the **factor loadings** as weights
  2. **Simple (unweighted) average**
- **Choice made for this exercise: simple average**, to keep the analysis simple.
- **Formulas as used:**

```
Performance          = (I1 + I4 + I5 + I6) / 4

Intention to Quit    = (I2 + I3 + I7) / 3
```

- Practically: add **two new columns** to the Excel sheet — `Performance` and `Intention_to_Quit` — one row per manager. Replicated in R with two lines of code.
- **Result: 7 survey questions reduced to 2 parameters.** This is the payoff of factor analysis — **dimension reduction**.

### 2.11 Worked comparisons of individual managers (with student Mani)
Using the two computed columns:

- **Employee 1 vs Employee 2:** *Both are high performers*, but **Employee 1 is likely to stay**, **Employee 2 has a high intention to quit.**
- **Employee 9 (row 10 of the sheet): Performance = 10, Intention to Quit = 1.43**
  → Interpretation: **high-performing employee who is likely to stay.**
- **Employee 27 (row 28 of the sheet): Performance = 6.79, Intention to Quit = 10**
  → Interpretation: **mid/average (or below-average) performer who wants to leave.**
- Note the index offset used in class: **employee number n sits on row n+1** because of the header row.

### 2.12 The managerial payoff — the 2×2 intervention matrix
Having the two parameters lets you classify all 30 managers and **design different interventions for each cell**:

| | **Low Intention to Quit (stays)** | **High Intention to Quit (leaves)** |
|---|---|---|
| **High Performance** | Retain / develop (e.g., Employee 9) | **Critical risk** — highest-priority intervention (e.g., Employee 2) |
| **Low Performance** | Performance management needed | Possibly let go / low-priority (e.g., Employee 27) |

### 2.13 Formality vs. informality debate (Arya's challenge on I3)
- **Arya's objection:** I3 (becoming **more formal and official**) doesn't obviously signal a desire to quit — being formal and official could be a *positive* organisational thing, so I3 could arguably belong to Group 1.
- **Instructor's rebuttal (context of middle managers):**
  - Middle managers are **the coordinating link** between **senior leadership** and **frontline employees / subordinates**.
  - Beyond formal and official aspects, a coordinating link is expected to maintain **informal relationships of trust, reciprocity, mutual respect, and cooperation**.
  - Becoming more formal/official is read as **becoming more distant**; loss of informality and everyday communication.
  - **Concept introduced: "SILENT QUITTING"** (a.k.a. quiet quitting) — *doing only what is formally/officially necessary; not going beyond the call of duty or beyond official responsibilities to help or support colleagues.* The person has **not** quit, but is withdrawing.
  - **Key claim: withdrawal from an organization begins with withdrawal of informal participation.** Hence increased formality is treated as an indicator of intention to quit.

### 2.14 The productivity/cooperation video (Yves Morieux — "As work gets more complex, 6 rules to simplify")
Shown to support the formality/informality argument. Content the instructor wanted retained:

- **Paul Krugman quote:** *"Productivity is not everything, but in the long run it is almost everything."* Productivity is the principal driver of the prosperity of a society.
- **The productivity decline data (large European economies; same profile in Japan and the US):**
  - **1950s–early 1970s: ~5% per annum**
  - **1973–1983: ~3% per annum**
  - **1983–1995: ~2% per annum**
  - **Since 1995: <1% per annum**
- **Compounding implication:** at **3% p.a.**, standards of living **double every generation**; at **1% p.a.**, doubling takes **three generations** — and in the interim many people will be worse off than their parents (less housing, education, vitamins, antibiotics, vaccination).
- **The "Holy Trinity" of management that has become counterproductive: CLARITY, MEASUREMENT, ACCOUNTABILITY.**
- **The 4×100m relay worked example (World Championship final, 8 teams):**
  - The **US team** has the fastest individual runners — the **fastest woman on earth** (Christy Gaines, 2nd runner) and **Torri Edwards** (4th runner, that year's 100 m gold medallist). *"There are 3.5 billion women on earth — where are the two fastest? In the US team."*
  - Summing individual 100 m **personal bests**, the US team would finish **3.2 m ahead** of the French team.
  - Using that year's **best performances**, the US team would finish **6.4 m ahead** of the French team.
  - **Outcome: the faster team LOST.** The slower (French) team won.
  - **Explanation: COOPERATION.** *"Thanks to cooperation, the whole is worth more than the sum of the parts — this is not poetry, this is math."* **"Those who carry the baton are slower, but their baton is faster."**
- **How each element of the Holy Trinity destroys cooperation:**
  - **Clarity:** runners asking "where does my role start and end — 95 m, 96, 97?" If the answer is 97 m, the baton gets dropped at 97 m whether or not anyone is there to take it.
  - **Accountability:** appoint a dedicated person accountable for passing the baton between each pair of runners → you get a clear interface and a clear line of blame, **but you never win the race**. *"We pay more attention to knowing who to blame in case we fail than to creating the conditions to succeed."* Organisations are designed to **fail in a compliant way**.
  - **Measurement:** "what gets measured gets done." Energy put into the **arm** (passing) and the **throat** (shouting to the next runner) is energy **not** in the **legs** (your measurable speed). Since cooperation is invisible to metrics, rewarding measurable individual performance pushes energy into the legs — **and the baton falls.**
  - **No metric can attribute the next runner's speed to her own effort vs. the quality of the hand-off she received.**
- **Definition of cooperation given:** *Cooperation is **not** a super-effort; it is **how you allocate** your effort. It is **taking a risk** — sacrificing the protection of objectively measurable individual performance in order to make a difference to the performance of others with whom you are compared.* Therefore **"it takes to be stupid to cooperate — and people are not stupid, so they don't cooperate."**
- **Consequence in complex businesses:** multiplication of structures, processes, systems, **interfaces, middle offices, coordinators**; then summaries, proxies, reports, KPIs, metrics. **Finding cited: teams spend between 40% and 80% of their time wasting their time**, working harder and longer on less and less value-adding activity.
- **Prescriptions from the talk:** Don't blame mindsets/personalities — **look at the work situation** and ask whether it is **individually useful for people to cooperate**. Remove interfaces, middle offices, complicated coordination structures. **Don't go for clarity — go for fuzziness and overlaps.** Remove most quantitative performance metrics (the "what"/speed) and look at **the "how"** — how the baton was passed.
- *(Instructor's added note: blaming personalities instead of the system "adds injustice to ineffectiveness.")*

### 2.15 Post-video class discussion
- **Arya's takeaways:** effort follows a sense that "this environment belongs to me"; an **informal environment** encourages effort; **the whole is greater than the parts**.
- **Another student:** in the hand-off, the receiving runner's **speed was not reduced** — a good pass adds no friction.
- **Instructor's synthesis:** people **pass positive energy** (or negative energy) to each other in organisations and in personal life. Emphasis on **informality, trust, cooperation, keeping morale high**, and getting people to converge to produce more than the sum of individual outputs.

---

## 3. Key Definitions & Rules to Memorise

- **Factor Analysis / Principal Component Analysis (PCA):** a statistical technique for dividing a set of survey questions into a smaller number of underlying groups (factors/components) and identifying what each group measures.
- **Variance:** the carrier of information in statistics — no difference, no information. **Variance = SD².**
- **Proportion of variance:** the share of total information retained by a given component.
- **Cumulative proportion of variance:** running total; **rule of thumb — stop once it exceeds 90%.**
- **Scree plot:** variance vs. component number; look for the **kink/elbow**.
- **Biplot:** simultaneously plots item vectors and cases (here, the 30 managers); vectors bundling together belong to the same factor.
- **Factor loading:** association of an item with a component; **range 0–1 in magnitude, can be signed; use magnitude only.** **Rule of thumb: > 0.5 → item belongs to that factor; < 0.5 → it does not** (some use 0.6/0.7).
- **Construct score:** composite of the items loading on a factor, via **simple average** or **factor-loading-weighted average**.
- **Intention vs. Behaviour:** intention is formed first, behaviour (action) follows; typical **intention-to-quit → actual quit lag ≈ 6 months (up to 1 year)**.
- **Silent / quiet quitting:** performing only formally and officially required duties; withdrawal of informal, discretionary contribution.
- **Organizational commitment:** the literature construct corresponding to "loyalty."

---

## 4. Exam / Assignment-Relevant Flags

- **Explicitly stated:** *"For the purposes of this course, knowledge of R is not mandatory or the use of R is also not mandatory. What is important for this course is how do we interpret the results that emerge."* → **You will be assessed on interpretation of output, not on coding.** The same results appear in any software.
- **The R code has been shared along with the reading.** You are free (encouraged, not required) to run/replicate/experiment with it; the instructor will re-run it in class in October.
- **Rules of thumb you should be able to apply and state as rules of thumb (not absolutes):**
  - **90% cumulative variance** → stop adding components.
  - **0.5 factor loading cut-off** → item membership in a factor.
  - Scree plot **kink/elbow** as an alternative criterion (here it points to 3 components while the 90% rule points to 2 — be able to discuss this tension; the instructor accepted 2).
- **Be able to do the full chain on an output table:** number of components → proportion & cumulative variance → scree plot → biplot → loadings table → item-to-factor assignment → **naming/labelling the factors** → computing composite scores → comparing cases.
- **Course logistics:** There is a **break in the course; the class next meets in OCTOBER.** At that point the class will:
  1. Re-run the code in class,
  2. **Incorporate the QUALITATIVE data** — the narrative **performance appraisal entries** for each of the 30 employees — into the same analysis, and
  3. Complete this exercise and move to **another analytics exercise spanning sessions 3 and 4.**
- Come prepared having at least read/interpreted the shared code and the reading.