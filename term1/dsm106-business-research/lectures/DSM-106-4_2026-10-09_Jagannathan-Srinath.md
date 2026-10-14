---
course: DSM 106
date: 2026-10-09
start: 7:00pm
session: "4"
faculty: Jagannathan Srinath
---

# DSM-106 Business Research: Session 4 Study Notes

**Session file:** DSM-106-4_2026-10-09 (Jagannathan Srinath)
**Running case:** Performance, creativity, teamwork and intention to quit for 30 middle-level managers. The analysis combines survey data with qualitative performance appraisals.

---

## 1. Overview

This session continues the middle-manager case from the previous class. It first recaps how factor analysis grouped seven survey items into two constructs: **performance** (I1, I4, I5, I6) and **intention to quit** (I2, I3, I7).

It then introduces **computer-aided text (content) analysis** of qualitative performance appraisals using the software **DICTION**. The five DICTION "master variables" (Activity, Optimism, Certainty, Realism, Commonality) are explained with research applications. Activity (a proxy for creativity) and Commonality (a proxy for being a team player) are computed for selected employees (6, 7, 11, 15) and compared with their survey scores.

All four variables are then **standardized into z-scores** so they share a common scale. Finally, **cluster analysis (k-means)** is introduced to segment the 30 employees. An elbow-type plot suggests 6 clusters, and the session ends after interpreting Cluster 1. The remaining clusters will be covered on Monday.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Factor analysis of the 7 survey items

- The analysis was run in R on survey responses for 30 middle managers. The items split into **two factors**.

**Factor 1 = Performance (I1, I4, I5, I6):**
- I1: She/he is an excellent interface between top and operational management.
- I4: She/he is able to accurately assess the potential applicability of new ideas.
- I5: She/he is able to energize people around her/him.
- I6: She/he demonstrates clarity and commitment in terms of what needs to be done and how to move forward quickly.

**Factor 2 = Intention to quit (I2, I3, I7):**
- I2: Of late, she/he has been talking about positive aspects of the culture in other organizations.
- I3: Of late, she/he has become more formal and official in interactions with colleagues.
- I7: Of late, she/he has been talking about how well her/his MBA batchmates are doing in their careers.

**Composite scores** are simple averages of the items, computed in Excel:

$$\text{Performance} = \frac{I_1 + I_4 + I_5 + I_6}{4}$$

$$\text{Intention to Quit (ITQ)} = \frac{I_2 + I_3 + I_7}{3}$$

- Qualitative performance-appraisal text is also available for the same 30 employees. This is the next layer of the analysis.

### 2.2 Worked example: Employee 15 (survey + qualitative)

**Appraisal text (about 47 words):**
> "He is often irregular and unaccountable to his colleagues. He behaves strangely and incompatible with his team. His dissent adds to dissonance in the team. He has a strategic mind in identifying long-term opportunities. He can also be fairly enterprising in finding solutions to nagging problems."

**Survey scores (Employee 15 is in row 16 of the sheet):**
- Performance = **9.28**
- ITQ = **10**

**Class reading:** He is a well-performing employee who wants to leave, and he does not get along with his team or colleagues.

### 2.3 Computer-aided text analysis / content analysis with DICTION

- **Content analysis** is the systematic analysis of qualitative data such as text. It can be done with DICTION, R, or many other platforms. DICTION is not the only tool.
- **Procedure in DICTION:**
  1. Input or edit the text. The trial version only allows editing an existing file, not adding a new one.
  2. Run **Standard Analysis**.
  3. Name the report (e.g., "Report 15").
  4. Open it with the **Compare Viewer**.
- The report contains many outputs. The focus here is the **five master variables** reported at the end of the table.
- Each master variable is reported with a **normal (usual) range**, so a text's score can be judged as low, normal or high.

### 2.4 The five DICTION master variables

#### (1) Activity

- **What it measures:** Language featuring movement, change, implementation of ideas and avoidance of inertia. In other words, goal-orientedness, transformation, action, change-orientedness, creativity and innovation.
- **Interpretation:** High score means an innovative or creative text. Low score means a less innovative text.
- **Normal range:** **46.74 to 55.48**.
- **Employee 15:** **49.61**, which is within range and slightly on the higher side (near 50). This indicates reasonable creativity.

**Formula (DICTION dictionary composition):**

$$\text{Activity} = (\text{Aggression} + \text{Accomplishment} + \text{Communication} + \text{Motion}) - (\text{Cognitive Terms} + \text{Passivity} + \text{Embellishment})$$

Why some components are subtracted:
- **Passivity** is subtracted because inert language is not creative.
- **Embellishment** is subtracted because decoration, exaggeration, dramatization and rhetoric do not indicate innovation.
- **Cognitive terms** are subtracted because an idea must have practical, concrete implications, not merely be cognitive.

How the algorithm works:
- Each component is a **dictionary of words**. For example, the Accomplishment dictionary includes "advances", "creates", "manages", "continuing".
- Word occurrences add to or subtract from the score, and context matters.
- **Standardization step:** whatever the text's length, the score is standardized as if the text were **500 words long**. The Employee 15 text was 47 words.

**Research applications:**
- *AACSB-accredited business schools.* The example given was IIM Indore, which holds EQUIS, AMBA and AACSB accreditations. AACSB requires all processes (admissions, hiring and promoting faculty, curriculum, teaching, course evaluation) to align with the school's vision and mission. Researchers scored vision/mission statements on Activity. **Higher Activity was associated with better graduate outcomes:** better placements, career progress 5 years later, and more alumni in leadership positions 10 years later.
- *Startup business plans.* An Activity score can act as a screening filter for whether a plan is innovative before an investor engages further.
- *Job applications for creative roles.* Statements of purpose or open-ended answers can be scored on Activity to help shortlist candidates for interview.

#### (2) Optimism

- **What it measures:** Hope and positivity.
- **Dark side:** Above a certain threshold, it signals **hubris, overconfidence, authoritarianism** and narcissism.
- **Normal range:** **46.37 to 52.25**.
- **Example:** Donald Trump's speeches start at around **65**, meaning far above the normal range.
- **Research application:** All public utterances of a CEO in a quarter were scored. These included press interviews, minuted investor calls and AGM speeches. **High CEO optimism (hubris) was negatively correlated with next-quarter financial performance**, measured by ROI and ROA.

#### (3) Certainty

- **What it measures:** Willpower, staying power and persistence in sticking with a decision rather than rolling it back after setbacks.
- **Dark side:** Above a threshold, it signals **rigidity, resistance to change and inflexibility**.
- **Research application (change management):** This applies during environmental, technology or consumer-preference shifts, new competitor entry, and mergers and acquisitions. Researchers scored employee emails, chats and grapevine or informal gossip. High certainty indicates employees resisting change, which impedes change management.

#### (4) Realism

- **What it measures:** Language that is concrete, tangible, present-oriented and practical.
- **Interpretation:** High score means concrete content. Low score means abstract content without present practical implications.
- **Research application (Learning and Development):** Post-training qualitative feedback from employees was scored. High realism indicates that the learning has concrete, implementable implications for day-to-day work, meaning the training worked.

#### (5) Commonality

- **What it measures:** Cooperation, rapport, togetherness, solidarity, identification with the group or organization, and being a good team player.
- **Research application:** Transcripts or emails of top-management-team interactions (board, strategy and review meetings) were scored. High commonality indicates high cooperation and group/organizational identification, meaning good team players.
- **Employee 15:** **16.98**, which is very low. This indicates a poor team player.

> **Student summary (Aditya):**
> - Activity: high means innovative or creative.
> - Optimism: confidence, with a dark side of overconfidence.
> - Certainty: willpower, with a dark side of rigidity or inflexibility.
> - Realism: concrete, tangible, present-oriented.
> - Commonality: togetherness, cooperation, team player.

### 2.5 Operationalizing the qualitative constructs for the case

For this case, two DICTION scores are used as variables alongside the two survey composites:

| Construct | Source | Measure |
|---|---|---|
| Creativity | DICTION, qualitative appraisal | Activity |
| Team player | DICTION, qualitative appraisal | Commonality |
| Performance | Survey | mean(I1, I4, I5, I6) |
| Intention to quit | Survey | mean(I2, I3, I7) |

### 2.6 Worked comparisons of individual employees

**Employee 15 (survey and DICTION scores):**
- Activity 49.61, Commonality 16.98, Performance 9.28, ITQ 10.
- Profile: creative, poor team player, performs well, wants to leave.
- **Student question (Arya):** "Strategic mind" and "enterprising" are positive statements, so shouldn't Activity be higher? The answer was that 49.61 is already on the higher side of the 46.74 to 55.48 range.

**Employee 6:**
- **Appraisal text:** "very arrogant, small-minded, cast off, disconnected", "does not feel the need to [be] empathetic", "brazen and shameless in pursuing her self-interest", "can pick up fights and create a nasty atmosphere", "not willing to work hard to find creative solutions", "half-hearted … lazy efforts", "uses the same yardstick to solve all issues".
- **DICTION scores:** Activity **41.92**, which is below the normal range, so not creative. Commonality **44.98**.
- **Survey scores:** Performance **10**. ITQ was not read out as a number, but the lecturer described her as wanting to **remain**.
- **Commonality compared with Employee 15:** 44.98 is poor in itself but higher than Employee 15's 16.98. So she is a poor team player, but a *better* team player than Employee 15. At one point the lecturer misspoke, saying she "appears to be a worse team player". The scores (44.98 vs 16.98) and the rest of the discussion indicate the intended conclusion is "better than Employee 15".

**Comparison of 6 vs 15:**
- Employee 6: less creative, comparatively better (but still poor) team player, high performer, wants to stay.
- Employee 15: creative, very poor team player, good performer (9.28), wants to leave.
- **Key lesson:** "People are complicated." Each profile mixes strengths and weaknesses, so interventions must differ. Arya would retain Employee 6 and work on improving her teamwork.

**Employee 7:**
- **Appraisal text:** popular among colleagues for organized action and steady performance; brings laughter; easygoing; creates no tension; inventive about solving problems; prevails over critiques with overwhelming support for his plans; shrewd in managing difficult issues.
- **Prediction (Jasraj):** high Activity and high Commonality.
- **DICTION result (updated version):** Commonality **51.68**, which is high. Activity came out slightly lower than the value stored in the spreadsheet.
- **Version discrepancy:** The spreadsheet values were produced with an earlier DICTION version. Most employees' scores match across versions, but some differ.

**Employee 11:**
- **Appraisal text:** a strength to the team through socialization and an accommodating nature; uplifts spirits when energy sags; complements others' synergies and creates unanimity; inspires under stress; strategic foresight in anticipating client issues; "interesting solutions … often amazing".
- **DICTION result:** Activity reasonably high, Commonality very high. The numbers read out were **48.97** (Activity) and **59.76** (Commonality). The transcript attributes these to "employee 7", but in context they appear to be Employee 11's spreadsheet values.

**Lecturer's reading of the language (7 vs 11):**
- Employee 11's wording signals stronger activity: "strategic foresight", "anticipating client issues", "interesting solutions", "amazing", "inspire", "create unanimity", "uplift spirit".
- Employee 7's wording is weaker by comparison: "inventive", "shrewd", "support for his plans".

**Survey scores for 7 and 11:** Both have Performance **10** and ITQ **10**.
- Profile: creative, good team players, top performers, but both want to leave.
- **Intervention:** Make every effort to retain them, find out what they need, and possibly support their further-education (MSDSM) fees.

### 2.7 Standardization: z-scores

**Problem:** The four variables move in different ranges, so they cannot be compared directly.

| Variable | Observed range | Mean | SD |
|---|---|---|---|
| Commonality | about 16 to 78 | **44.77** | computed in Excel, value not read out |
| Activity | about 35 to 61 | not stated | not stated |
| Performance | 6.78 to 10 | not stated | not stated |
| ITQ | 1.42 to 10 | not stated | not stated |

**Formula:**

$$z_i = \frac{x_i - \bar{x}}{s}$$

where $\bar{x}$ is the sample mean of the variable and $s$ is its sample standard deviation.

**Excel steps:**
1. Compute `AVERAGE` and `STDEV` of the column.
2. Write the z-score formula for the first row.
3. Lock the mean and SD cells with **`$`** (absolute references) so the formula can be dragged down.

**Interpretation:** z-scores typically lie between $-3$ and $+3$.

| z-score | Meaning |
|---|---|
| $z \approx 0$ | average |
| $z \approx +1$ | above average |
| $z \approx +2$ | high |
| $z \approx +3$ | very high |
| $z \approx -1$ | below average |
| $z \approx -2$ | low |
| $z \approx -3$ | very low |

**Small-sample caveat:**
- The fine graded distinctions in the table only emerge with large samples (300, 400 or 3,000 employees).
- With only $n = 30$, **just the sign matters**:
  - Positive z means high (e.g., good team player).
  - Negative z means low (e.g., poor team player).
- In R, the next four lines of code create the four standardized variables:
  - z(Commonality)
  - z(Activity)
  - z(Performance)
  - z(ITQ)

### 2.8 Cluster analysis (k-means)

**Factor analysis vs cluster analysis:**
- **Factor analysis** groups *variables* (survey questions).
- **Cluster analysis** groups *cases* (here, employees) into segments, using the four z-scored variables.

**Other applications:**
- *Marketing:* segmenting customers by demographics, income, preferences, education and culture, then designing products and services for each segment, which may differ in capacity to pay.
- *Strategy:* grouping organizations by resource use, strategy, size (number of employees), financial strength, leadership, family-owned vs professionally run, and shareholding pattern.

**Choosing the number of clusters (elbow-type plot from R):**
- The y-axis shows information gained, and the x-axis shows the number of groups.
- One group gives little information. Information improves as groups increase, up to a point.
- Nihal read the plot as levelling off at **6**, with no further gain beyond it. So **k = 6**.

**k-means clustering:**
- It is the simplest, "manual" form of clustering: the analyst specifies k, and the algorithm assigns employees to groups.
- More sophisticated, automated clustering methods also exist.

**Result:** 6 clusters, with **5 employees in each cluster** (as stated in class).

**Cluster 1 profile (signs of mean z-scores):**
- Commonality is negative, so they are poor team players.
- Activity is negative, so they show low creativity or innovation.
- Performance is negative, so they are poor performers.
- ITQ is positive, so they have a high intention to quit.
- **Managerial implication:** Let them leave. The class joked about whether to warn the MSDSM admissions office.

The remaining 5 clusters will be interpreted next session.

---

## 3. Analytical Pipeline Summary

1. **Survey items (I1 to I7):** run factor analysis to get 2 constructs (Performance; Intention to Quit), then average the items.
2. **Qualitative appraisals:** run DICTION content analysis to get Activity (creativity) and Commonality (team player).
3. **Standardize** all 4 variables with z-scores to put them on a common scale.
4. **Run k-means cluster analysis:** choose k from the elbow plot (k = 6), then profile each cluster by the signs of its z-scores.
5. **Design HR interventions per segment.** Examples:
   - Retain high performers who want to quit (Employees 7 and 11).
   - Let go of low-everything employees who want to quit (Cluster 1).

---

## 4. Flagged for Assignments / Follow-up

- **Hands-on practice (encouraged):**
  - Download DICTION (shared in class and by email).
  - Input all 30 employees' appraisals and compute their scores.
  - Experiment further, with DICTION or any other text-analysis tool such as R.
  - Write to or WhatsApp the instructor with results. The number and email were shared in chat; the email is also in the course outline.
- **Additional DICTION literature** will be sent by the instructor. You can also explore DICTION's help contents and dictionary viewer to see the words in each dictionary.
- **Key concepts to be able to explain:**
  - What each of the five master variables measures, including the dark side of Optimism and Certainty.
  - The Activity formula: which components are added and which are subtracted, and why.
  - Standardization to 500 words.
  - The z-score formula and how to interpret it, including the small-sample "sign only" rule.
  - Factor analysis vs cluster analysis.
  - How to choose k in k-means.
- **Next session (Monday):** Interpret Clusters 2 to 6, see which employees fall in each, wrap up the case, then move to a new exercise.
- No explicit exam statements were made in this session.