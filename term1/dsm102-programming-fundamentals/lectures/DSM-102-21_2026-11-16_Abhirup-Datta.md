---
course: DSM 102
date: 2026-11-16
start: 8:15pm
session: "21"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 20 (2026-11-14)](DSM-102-20_2026-11-14_Abhirup-Datta.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-102 – Session 21 (2026-11-16, Abhirup Datta): Course Logistics & Term-Project Check-in

> **Important note for readers:** This session contained **no new technical content**. No code was written or traced, no new Python functions or keywords were introduced, and no formulas were derived. The whole session covered administrative updates (end-semester exam, grading, term project rules) and a group-by-group progress check on the term projects. The sections below reflect that. Two short reference items at the end (a formula box and a code sketch) are **not from the lecture**. They are clearly labelled and included only because several groups said they plan to use those techniques.

---

## 1. Overview

The instructor announced that all lecture notes and notebooks are now on the LMS. He confirmed the end-semester exam date (Wednesday, 25 November) and its format: an online take-home, released around 7 pm and due before midnight. He then explained the tentative grade weightage and how relative grading works, and why small mark differences can change letter grades. He gave detailed rules for the group term project: deadlines, presentation format, and an individual 1–2 page report. He stressed that the project is meant to be **exploratory data analysis (EDA)** using course techniques, not machine learning. Finally, each of the 8 groups briefly described its dataset, size, and planned analysis, and the instructor commented on scope and on fair contribution among members.

---

## 2. Topics Covered (in order)

### 2.1 Course materials
- All lecture notes and notebooks are now uploaded to the **LMS portal**.
- An assignment link is still active. The instructor said he will **extend its deadline**.

### 2.2 End-semester exam
- **Date:** Wednesday, **25 November** (the transcript says "CSM 102", an ASR error for DSM-102).
- **Format:** online, take-home style. It appears on the LMS end-semester exam page.
  - Released at about **7:00 pm** (possibly a little later).
  - Due **before midnight** the same day. The instructor said this is sufficient time.
- Students asked for **practice problems** on the lecture topics before the exam. The instructor appeared to agree to share some typical problems and suggestions. The exact reply is unclear in the audio.

### 2.3 Grading scheme (tentative)
- Tentative weightage (the audio is garbled, so this is a best reconstruction):
  - Mid-semester exam: about **30%**
  - Term project: about **30%** (later confirmed: "Weightage is very high. 30% is not bad.")
  - End-semester exam: about **40%**
- The final split is **not fixed**. It will be chosen to benefit students. For example, if a group did very badly in the mid-sem, its weight might be reduced.
- **Relative grading:**
  - Marks are given by the instructors, but letter grades follow the institute's rules.
  - Only a certain percentage of the class can receive an A-range grade. Within that range, quotas split into A+, A, and A−.
  - High marks for everyone does **not** mean everyone gets an A.
- **Why small differences matter:**
  - Coding exams tend to have near-**binary marking** (right or wrong), so scores are usually very close.
  - A difference of **0.5–1.5 marks** has, in past batches, shifted grades by one or two levels.
  - Students from an earlier batch complained about this. When shown the calculation, they were satisfied.
- The **term project is the main place to differentiate yourself**.

### 2.4 Term project – rules and expectations
- **Structure:** 8 groups of 4 students each. Students formed the groups themselves.
- **Submission deadline:**
  - Originally around **30 November**, which is a Monday. The transcript also says "38th of November", likely meaning 28th or 30th.
  - It can be extended to **4 December at the latest**. The instructor will update the LMS once the class decides.
  - Students can submit earlier.
- **Presentations:**
  - Each group has about **20 minutes**. That is roughly 4 or more hours for 8 groups, so it will probably be **split over two evenings**, around **1–2 December** (4 groups per day, about 1.5 hours per session).
  - The class must agree on dates among themselves and tell the instructor **as soon as possible**. Delaying is discouraged because term 2 and the campus immersion (from 14 December) follow soon after.
  - **Every member must present** a part. It is not acceptable for one person to present while others don't attend.
  - Divide the presentation into roughly equal parts and **state clearly who did which part**.
- **What can be shared vs. what must be individual:**

| Item | Shared among group? |
|---|---|
| Notebook / code | Yes, common is fine |
| Presentation (PPT) | Yes, common is fine |
| **Report** | **No. Each member writes their own** |

- **Report details:**
  - Short: **1–2 pages maximum**, not a 50-page report.
  - It should summarise what you learned, what information you extracted, and how the analysis could be improved.
  - It gives your feedback on the **whole project** and may outline **which part you did**.
  - It must **not be copied** between members. The techniques will be similar, but the writing must be your own.
  - The instructor will share a **report template/structure** on the project assignment page on the LMS.
- **Honesty about contributions:**
  - The contributions claimed in the presentation and in the report must **match**.
  - For example, if the group says everyone did equal parts, someone should not then claim "I did 80%" in their report.
  - If some members did not contribute, say so **beforehand**.
  - Behind-the-scenes work such as **data cleaning** is acknowledged as significant even though it does not show visually. Say explicitly who did it.
- **Scope: EDA, not ML (important):**
  - The expected methods are **what was taught in this course**:
    - visualising data in different formats
    - basic correlations
    - basic probability and statistics
    - pair plots and similar plots
    - framing a clear question
  - **Machine learning** (e.g., random forest) is **not required**. It earns **no extra points**; at most it is "over and above", possibly a bonus. ML is covered later in DSM-302 (Foundations of Machine Learning).
  - Marks reward **novelty and care in the EDA**, not "suddenly applying some ML technique".
  - Using ML you understand is allowed. If you **copy** a technique you cannot explain, it counts **against** you, because members will be questioned on their parts.
  - A student noted that linear regression was the last topic taught. The instructor said it was shown to demonstrate Python for statistics, and is not a project requirement.
- **Help:** email the instructor with **"DSM-102" in the subject line**.
- Saturdays are mostly free. Use them to meet as a group.

### 2.5 Group progress reports

| Group | Dataset / topic | Size (as stated) | Planned analysis |
|---|---|---|---|
| 1 | E-commerce customer behaviour dataset | not stated | Dataset shared on 28 Oct (via Vikyath Raj); no analysis yet. Instructor warned against delaying. |
| 2 | Market data (exact dataset unclear in audio) | not stated | Market efficiency, price volatility, impact of factors such as arbitrage and storage (audio garbled). |
| 3 | IPL ball-by-ball match data, 2008–2026 | 64 columns | Cleaning done. Questions: runs per season, whether winning the toss helps win, best stadium for batting. **Linear regression to predict the final (20th-over) score from the score after 10 overs**; a fantasy-team ("Dream11"-style) idea. |
| 4 | Supply chain dataset | about 180k rows, 53 columns (some redundant or non-numeric, e.g., product image placeholders, to be dropped) | Predict late deliveries and profit leaks from bad discounting, using order, customer demographic, shipping/logistics, and region/shipping-mode columns. Planned random forest; the instructor responded with the EDA-scope comments above. |
| 5 | Global AI jobs dataset | 5,000 rows, 37 columns (17 numeric, 20 categorical/text/dates) | Pre-written questions (shared as a PPT) to be answered with visualisations and correlation plots. The instructor said all of them can be answered by plotting. |
| 6 | Customer segmentation | about 50,000 rows, 53 columns | Demographics (age, gender, income bracket, education), behavioural features, and value metrics (profitability, segment). Basic cleaning done. Goal: relationships between demographics, behaviour, and value. |
| 7 | District-wise cyber crime data (from 2017) | about 681 records (as heard) | State-wise distribution, types of cyber crime (financial fraud, hacking, cyberbullying), annual trends, the predominant crime type. |
| 8 | E-commerce public dataset (2 years of data) | 9 CSV files, 52 columns | First challenge: **combining, grouping, and aggregating** the 9 files. Then cleaning, sales trends (monthly/yearly), category rankings, seller comparisons, correlation of sales with KPIs, customer segments by geography and age. The presenter said teammates had been hard to reach; the instructor told all members to contact the presenter and contribute. |

---

## 3. Exam / Assignment Flags

- ⚠️ **End-sem exam:** Wed **25 Nov**, released about 7 pm, due before midnight, on the LMS.
- ⚠️ **Grading is relative.** 0.5–1.5 marks can change your letter grade. Be careful and precise.
- ⚠️ **Term project:** about 30% weight. Submit by **30 Nov** (extendable to **4 Dec at the latest**). Presentations around **1–2 Dec**, about 20 minutes per group, and everyone must present.
- ⚠️ **Individual report:** 1–2 pages, written by **each member separately**, consistent with the presentation's claims about who did what.
- ⚠️ **Focus on EDA** with course techniques. ML is optional and gives no extra credit. Never use what you can't explain.
- Action items for the class:
  - Agree on presentation dates and tell the instructor soon.
  - Watch the LMS for the report template.
  - Expect an extended assignment deadline.

---

## 4. Functions, Keywords, Operators, Syntax Introduced

**None in this session.** No code was written, traced, or dictated. Students mentioned in passing:
- data cleaning
- grouping/aggregation
- correlation
- pair plots
- linear regression
- random forest

These were project-plan descriptions, not taught material.

---

## Appendix (NOT from the lecture, for reference only)

These are standard reference items related to methods the groups mentioned. They were not presented in this session.

**Pearson correlation** (basis of correlation heatmaps):
$$r_{xy} = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\,\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}, \qquad -1 \le r_{xy} \le 1$$

**Simple linear regression** (as in Group 3's idea, predicting the final score $y$ from the score after 10 overs $x$):
$$\hat{y} = \beta_0 + \beta_1 x, \qquad \hat\beta_1 = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x$$

**Illustrative pandas sketch** for combining multiple CSVs and running basic EDA, relevant to Group 8. The file and column names are hypothetical placeholders, not from the lecture:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

orders = pd.read_csv("orders.csv")            # hypothetical file names
items  = pd.read_csv("order_items.csv")

df = orders.merge(items, on="order_id", how="inner")   # join tables on a shared key

monthly = (df.assign(month=pd.to_datetime(df["order_date"]).dt.to_period("M"))
             .groupby("month")["price"].sum())          # monthly sales trend
monthly.plot(title="Monthly sales")

sns.heatmap(df.select_dtypes("number").corr(), annot=True)  # correlation heatmap
plt.show()
```

- `pd.merge` / `.merge()`: joins two DataFrames on a key column.
- `.groupby(...).sum()`: aggregates values per group.
- `.corr()`: computes the pairwise Pearson correlation matrix of numeric columns.
- `sns.heatmap`: visualises a matrix, such as a correlation matrix, as a colour grid.

<!-- nav -->
← [Session 20 (2026-11-14)](DSM-102-20_2026-11-14_Abhirup-Datta.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
