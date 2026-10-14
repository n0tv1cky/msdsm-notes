---
course: DSM 101
date: 2026-10-12
start: 7:00pm
session: "24"
faculty: Pritee Sharma
---

# DSM-101 · Session 24: Types of Data and Levels of Measurement

**Lecturer:** Pritee Sharma · **Date:** 2026-10-12

---

## 1. Overview

This session continued from the previous class on sampling (probability vs. non-probability samples) and introduced **types of data**. The lecture first distinguished **qualitative (categorical/nominal)** data from **quantitative (numerical)** data, and split quantitative data into **discrete** and **continuous**. Along the way it defined a **variable** and stressed that response options must be **exhaustive and unambiguous**, using an employment-survey example. It then covered the four **levels of data**: **nominal → ordinal → interval → ratio**. Measurement precision increases at each step, and so does the set of statistics you can legitimately compute. Much of the discussion centred on what separates **interval** from **ratio** data, which is the presence of a **true (absolute) zero**. Students offered and debated several examples. The next class will connect these four data types to the four corresponding **measurement scales** and to their use in research and statistical analysis.

> **Note:** No probability distributions or named theorems (CLT, Bayes, etc.) were covered. This is a measurement and data-classification lecture.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap and context
- The previous class covered probability samples vs. non-probability samples.
- Data are usually classified as **primary vs. secondary**, depending on the source.
- Today's classification is a different one: **qualitative vs. quantitative**.

### 2.2 Qualitative data
- **Definition:** data resulting from **categorical responses**. In the natural sciences these are categorical **observations**.
- Also called **nominal data** or **categorical data**.
- **Example:** gender, with options such as male / female / third gender / prefer not to disclose. Whichever box the respondent ticks is the response.

### 2.3 What is a variable?
- **Definition:** an entity that **assumes varying values**. The variation can happen in two ways:
  - for the **same case at different points in time**, or
  - for **different cases at the same point in time**.
- **Example (Human Development Index / well-being index / GDP):**
  - Measuring HDI for **several countries in one year** (e.g., 2025–26): the *countries* vary, so it is a variable.
  - Measuring HDI for **one country (India) across years** (e.g., 2000–01 to 2025–26): *time* varies, so it is a variable.
- If the variable is recorded in a **categorical/nominal system**, the data are qualitative.

### 2.4 Defining variables and response options (research-design point)
- First, **define your variables** for your study.
- Expected responses must be **exhaustively defined**, covering all possible options.
- Questions should be **as specific as possible**, and responses **as exhaustive as possible**, so nothing is ambiguous or left out.
- **Gender example:** older research treated "male / female" as exhaustive. Society now expects more options, so they must be added. The same applies to religion.
- **Employment example (worked through in class):**
  - "Employed / Unemployed" alone is ambiguous. Employed *when*? Specify a period, e.g., "in the last financial year."
  - Someone who worked **4.5 months** last FY would not know which box to tick. Define a threshold:
    - worked **more than 180 days** → employed;
    - worked **180 days or fewer** → not employed.
  - Someone who worked more than 180 days but only **4 hours/day** still doesn't fit. Add a **part-time employment** option.

### 2.5 Quantitative data
- **Definition:** responses are **numerical**. Contrast: qualitative = categorical, quantitative = numerical.
- Quantitative data are either **discrete** or **continuous**.
  - **Discrete data:** countable values only.
    - Example: *How many courses have you taken this semester?* The answer is 1, 2, 3, …, never 1.5 or 2.5.
  - **Continuous data:** arises from a **measuring process**. It can be measured continuously, with as many decimal places as you like.
    - Examples: your weight; the weight of six-month-old babies across populations or geographies (e.g., a child-nutrition study).

**Class discussion of examples:**
- **Petrol pump** (fuel quantity vs. amount paid):
  - Fill a fixed quantity (e.g., 7 L) → the bill comes out like ₹700.xx.
  - Pay a fixed amount (e.g., ₹100) → the fuel delivered might be about 0.97 L.
  - **Conclusion agreed in class:** if one of the two (fuel or bill) is fixed/discrete, the other is continuous.
  - The lecturer noted that prices are quoted to two decimals, which is part of why the bill can look continuous.
- **Retail store:** footfall (number of visitors) is **discrete**. A student proposed that sales revenue is continuous. The lecturer questioned how often prices really take continuous values (e.g., loose groceries priced in paise) and asked students to **"go back and think about both examples again."**
- **Cricket runs scored:** discrete. **Temperature or body weight** (e.g., 25.x °): continuous.

### 2.6 Levels of data: Nominal → Ordinal → Interval → Ratio
- Moving up the levels **increases the precision of measurement** and the range of permissible statistics.

#### (a) Nominal data
- Same as qualitative/categorical data. Responses fall into categories that you can **code** (i.e., classify).
- **Examples:**
  - Jersey numbers of football/cricket players. They only identify a player and carry no numeric meaning.
  - Gender, occupation, ethnicity, marital status.
- **Drawback:** it is the easiest type to collect, but **almost no mathematical operations** are meaningful.
- **Worked example (religion in a class of 50):** 20 Muslim and 30 Hindu.
  - Code Muslim = 1 and Hindu = 2. The codes are labels only; you cannot multiply, divide, or average them. "Average religion of the class" is meaningless.
  - Record the frequency for each respondent: Hindu, Hindu, Muslim, …
  - Here the frequencies are 30 (Hindu) and 20 (Muslim), so the **mode** is Hindu.
- **Appropriate statistics:** **frequency** and **mode** only.

#### (b) Ordinal data
- Arises from **ranking**. Observations can be arranged in **ascending or descending order**.
- The **intervals between values are not equal**. You know the order, but not *how much* more or less one value is than another.
- **Examples:**
  - **Hurricane categories:** Cat 5 is worse than Cat 4, and Cat 4 is worse than Cat 3. But Cat 2 is **not** "half" of Cat 4.
  - **Social class.**
  - **Hardness of minerals (Mohs scale):** talc is softest and diamond is hardest, with gypsum and others in between. The next mineral is not "double" talc's hardness.
  - **Class standing:** scores of 92, 82, 81 give ranks 1st, 2nd, 3rd, but the gaps (10 marks vs. 1 mark) are unequal.
  - **Military ranks:** General > Colonel > Major > Lieutenant > Sergeant. The order is descending, but the distances are not necessarily equal.
  - **Income as categories:** below USD 20,000 / USD 20,000–49,999 / USD 50,000 and over. A very rich person and someone earning exactly USD 50,000 both choose the top category.
- Unlike nominal data, the *observations themselves* can be ordered. With nominal data you can only order the frequencies.
- **Appropriate statistics:** **mode** and **median**, but **not the mean**.
- **Ranking scales** are widely used in management and marketing research for subjective attributes such as tastes and preferences (important in consumer theory).
  - Rankings are **relative, not absolute**. You can't be "doubly sure" or "half sure."
  - Your top choice depends on what else is in the choice set. Ranking from basket {A, B, C, D, E} can give a different top choice than ranking from {C, D, E, X, Y}.
  - **Humorous slide example:** "Rank 1–4: being hit in the face with a dead rat; being buried up to your neck in cow manure; failing this course; eating nothing but chopped liver for a month." It illustrates how hard it is to rank all-unpleasant options.

#### (c) Interval data
- Observations are ordered, **and the intervals between consecutive values are equal**.
- **There is no true zero.** Zero does not mean complete absence of the characteristic.
- **Key test given in class:** when you change measurement scales, the **zero of one scale does not match the zero of another**.
  - Example: $0^\circ\text{C} \neq 0^\circ\text{F} \neq 0\ \text{K}$.
- **Consequence:** you **cannot form meaningful ratios**.
  - Example: New York at $40^\circ$ and Buffalo at $20^\circ$ does **not** mean one city is "twice as hot or cold" as the other.
  - Likewise, you cannot say $10^\circ$ is half of $20^\circ$, or $20^\circ$ is half of $40^\circ$.
- **Body temperature illustration:** about $98^\circ$F is normal and $100$–$101^\circ$F is fever. These values don't line up numerically with Celsius, where normal is about $37^\circ$C.
- **Appropriate statistics (as stated):** **mode** and **arithmetic mean**. Median is also valid, since interval data are ordered.

**Student examples discussed (with the lecturer's verdicts):**

| Proposed example | Lecturer's verdict |
|---|---|
| Time on a 12-hour clock (2–4 pm and 6–8 pm are both 2 hours) | Rejected: time spans are measured exactly (120 min each). Whether the time was "productive" is a separate question. |
| Hemoglobin levels / normal ranges in medical reports | Uncertain: likely measurable exactly; the lecturer couldn't confirm either way. |
| BMI as a measure of health | Rejected: BMI is an exact value. "Health" is a subjective construct that would need definition. |
| Monthly rainfall | Rejected: $0\ \text{L} = 0\ \text{gallons}$, so it has a true zero (ratio data). |
| GDP growth rate (quarterly) | Rejected: GDP has a true zero. Zero rupees = zero dollars = zero yen. Quarters are time, which is a separate matter. |
| Hardness of minerals | Initially grouped with temperature by the lecturer. A student (Subra) **corrected this at the end: hardness is ordinal** (Mohs scale). The lecturer agreed. |

#### (d) Ratio data
- Consecutive intervals are equal **and there is a true (absolute, non-arbitrary) zero**.
- All scales for the quantity start at the same zero, e.g., $0\ \text{kg} = 0\ \text{lb}$ and $0\ \text{km} = 0\ \text{miles} = 0\ \text{ft}$.
- Because of the true zero, **ratios are meaningful** (doubling and halving make sense):
  - $100\ \text{lb} = 2 \times 50\ \text{lb}$, and equally $100\ \text{kg} = 2 \times 50\ \text{kg}$.
  - USD 100 is half as much as USD 200.
- **Examples:** height, weight, length, distance, mass, monetary values (income, GDP), units sold.
- **Caveat on units sold:** flow commodities such as fuel are continuous, so "units sold" only applies if sold in whole units (1 L, 2 L, 3 L, …).
- **Kelvin (student question):** Celsius and Fahrenheit are interval, but **Kelvin is ratio**, because it has an absolute zero.
  - In class this was stated as "300 K is half of 150 K." That is a slip: the correct statement is $150\ \text{K} = \tfrac{1}{2} \times 300\ \text{K}$.

### 2.7 Linking data types to scales (preview of next class)
- Each data type is measured on its matching scale:
  - nominal data → nominal scale
  - ordinal data → ordinal scale
  - interval data → interval scale
  - ratio data → ratio scale
- **Order of decisions in research:** identify the **variable** → determine what **kind of data** (responses/observations) it yields → choose the **scale**. You cannot pick the scale first.
- A true zero matters because it allows **comparisons across scales** and conversion into ratios.

---

## 3. Summary Table

| Level | Ordered? | Equal intervals? | True zero? | Ratios meaningful? | Appropriate statistics | Examples |
|---|---|---|---|---|---|---|
| Nominal | No | No | No | No | Frequency, mode | Gender, religion, jersey numbers, marital status |
| Ordinal | Yes | No | No | No | Mode, median (not mean) | Hurricane category, class rank, military rank, Mohs hardness, income brackets |
| Interval | Yes | Yes | No | No | Mode, (median), arithmetic mean | Temperature in $^\circ$C or $^\circ$F |
| Ratio | Yes | Yes | Yes | Yes | All of the above, plus ratios | Height, weight, distance, money/GDP, rainfall, Kelvin |

**Supplementary (not stated in lecture):** temperature conversions show why $^\circ$C and $^\circ$F zeros don't coincide:

$$F = \tfrac{9}{5}C + 32, \qquad K = C + 273.15$$

So $0^\circ\text{C} = 32^\circ\text{F} = 273.15\ \text{K}$.

---

## 4. Exam/Assignment Pointers

No explicit exam announcements were made. Likely-testable points and follow-ups:

- **Follow-up task from the lecturer:** rethink the **petrol pump** and **retail store (footfall vs. sales revenue)** examples. Which quantity is discrete and which is continuous, and why?
- **Key distinguishing test, interval vs. ratio:** does a **true zero** exist, so that zeros coincide across units and ratios ("twice as much") are meaningful?
- Know the **permissible statistics** for each level (nominal: mode/frequency; ordinal: + median; interval: + mean; ratio: ratios as well).
- Be able to **classify examples** correctly. Common traps:
  - hardness → ordinal
  - $^\circ$C/$^\circ$F → interval, but Kelvin → ratio
  - GDP and rainfall → ratio
  - jersey numbers → nominal
- **Survey-design principle:** variables must be clearly defined and response options **exhaustive and unambiguous** (employment: 180-day threshold plus a part-time option).
- **Next class:** the four measurement scales and where each type of data is used in research and statistical analysis.