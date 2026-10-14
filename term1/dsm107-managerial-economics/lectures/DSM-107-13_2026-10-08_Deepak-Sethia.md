---
course: DSM 107
date: 2026-10-08
start: 7:00pm
session: "13"
faculty: Deepak Sethia
---

# DSM-107 Managerial Economics, Session 13 (08-Oct-2026, Deepak Sethia): Study Notes

---

## 1. Overview

This session finished the national-income measurement topic and started the theory of aggregate demand.

- **Nominal vs. real GDP.** The lecture worked a two-good numerical example (wheat and potato, 2010–2013) to show how nominal GDP mixes price changes with output changes. Real GDP at base-year prices isolates the change in volume.
- **Price indices.** It covered the Consumer Price Index (CPI) as a fixed-basket, expenditure-share-weighted index (Laspeyres type) and contrasted it with the Wholesale Price Index (WPI).
- **Who gains and loses from inflation.** It discussed indexation (DA), regressive redistribution through food inflation, and lender vs. borrower when actual inflation differs from expected inflation, using a nominal/real interest rate example.
- **India's data.** It looked briefly at India's long-run per capita GDP and discussed base-year selection and revision. Student questions covered how the CPI basket is built and single vs. double deflation.
- **Business cycles.** The second half introduced potential output, frictional unemployment, and the Keynesian reasons why output (not prices) falls in a recession: sticky wages and prices, and a flat short-run aggregate supply curve.
- **Consumption.** It introduced the consumption function $C = \bar{C} + cY$, which sets up the multiplier model for the next session.

---

## 2. Topics Covered (in order taught)

### 2.1 Nominal GDP vs. Real GDP

GDP can rise because **prices rise**, because **output rises**, or both. We care mainly about whether **output** (the volume of goods and services) is changing.

| Measure | Also called | Prices used |
|---|---|---|
| Nominal GDP | GDP at **current prices** | Each year's own prices |
| Real GDP | GDP at **constant prices** | Prices of a fixed **base year** |

**Formulas** (for $n$ commodities, $i = 1,\dots,n$; $t$ = current year, $b$ = base year):

$$\text{Nominal GDP}_t = \sum_{i=1}^{n} P_{i,t}\,Q_{i,t}$$

$$\text{Real GDP}_t = \sum_{i=1}^{n} P_{i,b}\,Q_{i,t}$$

Prices are used as weights because physical quantities of different goods cannot be added directly ("can't add apples and oranges").

#### Worked example: two goods, base year 2010

| Year | Wheat $Q$ | Wheat $P$ | Potato $Q$ | Potato $P$ |
|---|---|---|---|---|
| 2010 | 10 | 10 | 5 | 20 |
| 2011 | 10 | 20 | 5 | 40 |
| 2013 | 40 | 40 | 20 | 80 |

The 2011 prices are inferred from "prices doubled." 2012 values were not read out in the lecture.

**Nominal GDP**

- 2010: $10 \times 10 + 5 \times 20 = 100 + 100 = 200$
- 2011: $10 \times 20 + 5 \times 40 = 200 + 200 = 400$, so nominal GDP doubled.
- 2013: $40 \times 40 + 20 \times 80 = 1600 + 1600 = 3200$

Nominal GDP therefore rises from ₹200 to ₹3200, a **16-fold** jump.

**Decomposing the jump**

- Wheat quantity rose $10 \to 40$ ($4\times$) and potato quantity rose $5 \to 20$ ($4\times$). Volume rose 4 times.
- Wheat price rose $10 \to 40$ ($4\times$) and potato price rose $20 \to 80$ ($4\times$). Prices rose 4 times.
- So $16 = 4 \text{ (volume)} \times 4 \text{ (price)}$.

**Real GDP (at 2010 prices)**

- 2010: $200$
- 2011: $10 \times 10 + 5 \times 20 = 200$. Output did not change, so real GDP did not change even though nominal GDP doubled.
- 2013: $40 \times 10 + 20 \times 20 = 400 + 400 = 800$. This is exactly a $4\times$ rise over 2010, i.e., the pure volume change.

**Key points**

- Nominal GDP of 3200 reflects both price and volume changes; real GDP of 800 reflects only the volume change.
- Newspaper growth figures (e.g., "economy grew 7%" or "7.8%") always refer to **real GDP growth**.
- Rough relation: nominal growth ≈ real growth + inflation.
  - Lecture example: real growth about 7–7.5% plus inflation about 4–5%.
  - The lecturer said both "nominal ~14–15%" and "taken together ~12%". The sum of the stated components gives roughly 11–12.5%.
  - Approximation: $g_{\text{nominal}} \approx g_{\text{real}} + \pi$.
- The base year is "very crucial." Valuing every year's output at the same prices tells us whether people in later years are actually better off (have more goods).

---

### 2.2 Consumer Price Index (CPI)

**Definition:** the CPI is a **weighted average of proportionate price changes of a fixed basket** of goods and services. The weights are each item's **share in total expenditure in the base year**.

**Inflation** is the rate of change of the price level. You compare the cost of the same basket in consecutive years: inflation for 2013 compares 2012 with 2013. If the cost of the basket rises by 5%, inflation is 5%.

**Formula (weighted-average form):**

$$\text{CPI}_t = \sum_{i=1}^{n} s_{i,b}\,\frac{P_{i,t}}{P_{i,b}}, \qquad s_{i,b} = \frac{P_{i,b}\,Q_{i,b}}{\sum_{j=1}^{n} P_{j,b}\,Q_{j,b}}$$

- $\dfrac{P_{i,t}}{P_{i,b}}$ is the proportionate price change of item $i$.
- $s_{i,b}$ is item $i$'s share in base-year spending, so $0 < s_{i,b} < 1$ and $\sum_i s_{i,b} = 1$.
- The denominator of $s_{i,b}$ is **total spending in the base year**.

Illustration of shares: out of each ₹1 spent, perhaps 25 paise on health, 25 paise on education, 20 paise on food, and 10 paise on rent.

**Simplified form (after cancellation):** this is the Laspeyres index.

$$\text{CPI}_t = \frac{\sum_{i} P_{i,t}\,Q_{i,b}}{\sum_{i} P_{i,b}\,Q_{i,b}} \quad (\text{often} \times 100)$$

Interpretation:

- The **denominator** is what I spent on the base-year basket at base-year prices.
- The **numerator** is what I would need to spend today to buy the same base-year basket, at current prices $P_{i,t}$.

Inflation between $t-1$ and $t$:

$$\pi_t = \frac{\text{CPI}_t - \text{CPI}_{t-1}}{\text{CPI}_{t-1}} \times 100$$

**RBI target:** CPI inflation of 4% with a band of $\pm 2\%$, i.e., 2% to 6%. The 4% midpoint is the anchor.

---

### 2.3 Wholesale Price Index (WPI) vs. CPI

The method is the same (fixed-basket weighted index). The coverage differs:

| | CPI | WPI |
|---|---|---|
| Stage | Retail | Wholesale |
| Coverage | Goods **and services** (education, healthcare, haircuts, rent) | **Goods only**; services are not traded in wholesale markets |

**Purpose of WPI: an advance warning signal.**

- When wholesale prices rise, retail prices follow with a **lag**.
- Retailers find it hard to raise prices immediately because of already-printed menus and MRPs. The next batch, bought at higher wholesale prices, will carry a new price.

---

### 2.4 Does Inflation Make You Poor? Distributional Effects

**Baseline argument.** Your spending is someone else's income.

- If **all** prices rise by the same percentage (say 10%), incomes also rise 10%. People are neither worse off nor better off.
- A seller whose product price rises is not automatically better off: everything they buy has also risen 10%.
- Example from Q&A: a medical-product maker facing general inflation is **indifferent**.
- You gain only if your own product price (or your income) rises **faster** than the prices of what you buy.

**Why inflation is still bad**

1. **Not all prices rise at the same rate.** Relative prices change.
2. **Not all wages are indexed.**
   - Government employees get **DA (Dearness Allowance)**, which is inflation protection.
   - Maids, drivers, and most poor workers do not.
   - Those who are indexed benefit; those who adjust with a lag (usually the poor) lose.
   - So inflation is a **regressive redistribution**.

**The food-inflation and DA example** (flagged by the lecturer as *"a subtle point but a very important point"*):

- Richer person: earns ₹1 lakh/month and spends about ₹10,000–15,000 on food, roughly **15%**.
- Poorer person: earns ₹10,000/month and spends about ₹4,000–5,000 on food, roughly **50%**.
- The absolute food spending is higher for the rich, but the **share** is higher for the poor.
- CPI is a weighted average over **all** consumers. When food prices drive inflation, the DA compensates for the economy-wide basket.
- The richer, indexed person gets DA for inflation that mostly hits others. They can spend it on items that are not becoming expensive (iPads, phones).
- The poor face higher effective inflation and are not indexed.

**Efficiency concern.** Inflation adds **uncertainty**. This will be covered in the monetary policy sessions.

---

### 2.5 Nominal vs. Real Interest Rate: Lender vs. Borrower

**Setup**

- Income is ₹100. Consume ₹70 and lend ₹30 (saving means deferring consumption to tomorrow).
- You lend because you want the money back, and more than you gave, as compensation for waiting.
- In the example: lend ₹100 today and get ₹110 next year, so the **nominal interest rate** is $i = 10\%$.

**Case 1: expected inflation 6%**

- What ₹100 buys today costs ₹106 next year. An item priced ₹1 today costs ₹1.06.
- With ₹110 you buy more than today, with ₹4 extra.
- Real return: $\dfrac{110}{106} - 1 \approx 3.8\%$, which the lecturer described as "close to 4%" or "three point something."
- Approximation (Fisher relation): $r \approx i - \pi^e = 10\% - 6\% = 4\%$.
- Exact form: $1 + r = \dfrac{1+i}{1+\pi}$.

**Case 2: actual inflation turns out to be 12%**

- The same basket now costs ₹112, but the lender receives only ₹110.
- Real return: $\dfrac{110}{112} - 1 \approx -1.8\%$ (approximately $10\% - 12\% = -2\%$). The lender buys fewer than 100 "chocolates."
- The borrower (e.g., someone building a toffee factory) expected to sell 100 chocolates for ₹106 but actually gets ₹112, so they gain.

**Conclusions**

- When **actual inflation exceeds expected inflation**, wealth is redistributed **from lenders to borrowers**. Borrowers repay in "cheaper rupees."
- Inflation redistributes:
  - between savers (lenders) and borrowers: borrowers gain when inflation is high;
  - between sellers and buyers: sellers gain when prices of what they sell rise more than prices of what they buy.

---

### 2.6 India's GDP Over ~70 Years

- In 1950–51, per capita GDP was:
  - about **₹285** at current (1950) prices;
  - about **₹13,000** at constant **2011–12 prices**.
- Only the constant-price comparison is meaningful. By 2021–22, the average Indian earns roughly **8–9 times** the 1950–51 level in real terms.
- Composition: India was largely a **closed economy**. Exports and imports were a small share of GDP until the **1991 economic reforms**. After that, $X$ and $M$ rose as shares of GDP.
- This connects to $Y = C + I + G + X - M$ from earlier sessions.
- **Per capita** GDP, not absolute GDP, is the relevant welfare measure.
- **Flow vs. stock:**
  - **Income** is a flow, earned each year.
  - **Wealth** is a stock, the accumulated past income and savings.

---

### 2.7 Base Year: Selection and Revision (Q&A)

**History of India's base year:** 2004–05, then 2011–12, then **2022–23**. The latest revision was made in February 2026.

**Criteria**

1. **Representative/normal year.** Avoid abnormal years:
   - 2020 (COVID);
   - 2016–17 (demonetisation);
   - 2017–18 (GST introduction).

   Such years do not represent the long-run structure of the economy. A student pointed out that 2025 is also not ideal because of war and disruption.
2. **As recent as possible**, so comparisons are more sensible.

**Why revise at all?**

- The consumption basket changes. Mobile phones were rare before about 2004–05; an old base year would not contain many current products, and would contain items no longer consumed.
- Valuing new goods at old prices overstates growth.
  - A 512 MB pen drive cost about ₹2,000–3,000 around 2006–08.
  - Today much larger drives cost roughly the same.
  - Valuing today's drives at 2006 prices would make people look implausibly rich.
- Grandparents' vs. today's lifestyles (ACs, fridges vs. land, wooden furniture) are hard to compare across distant years. A base year of 2022–23 is much closer to 2025.

---

### 2.8 Other Q&A Points

**Purchaser/Producer Price Index:** for course purposes, treat the **WPI** as the closest substitute, since producers buy inputs in wholesale markets.

**Single vs. double deflation**

- 2011–12 series: single deflation for manufacturing, double deflation for agriculture.
- 2022–23 series: double deflation for both, partly because the IMF prescribes it.
- The issue is **debated in academia** (the lecturer compared it to Coca-Cola vs. Thums Up).
  - The lecturer's view is that single deflation may be better for manufacturing, because double deflation has serious conceptual challenges.
  - The argument for double deflation is that it measures volume change from both the output and input sides.

**How the CPI basket is constructed**

- It is based on the **Consumption Expenditure Survey** by the National Statistical Office (NSO), covering about **1.5 lakh households** via detailed questionnaires. The results are compiled into a representative national basket.
- There is no target number of items. An independent committee decides which items to cover, aiming for a representative and comprehensive basket.
- **Baskets vary across countries and even across states:**
  - CPI Kerala and CPI Bihar differ because of demographics and income levels.
  - In Bihar, food has a higher weight.
  - In Mumbai, rent has a higher weight. Rent is included in CPI.
  - Regional items such as betel leaf/supari appear in Assam's basket but may not appear in Rajasthan's.
- The weights reflect actual consumption, so the index is not easily manipulated by adding items.

---

### 2.9 Potential Output and Full Employment

**Potential output ($Y^*$):** the output producible using labour and capital at **full employment**, in the usual or normal fashion.

- Full employment does **not** mean 100% of workers working three 8-hour shifts.
- Analogy: just before exams your absorption ability peaks, but you cannot sustain that all 365 days. Potential is the **average sustainable** level over time.

**Unemployment exists even at full employment, at about 4–5%.** This is **frictional unemployment**: workers moving between sectors takes time. Examples:

- the auto industry shrinking as people shift to shared mobility;
- STD/PCO booths closing while delivery jobs open up;
- a locality's taste shifting from Chinese to Indian food, so chefs need retraining or new restaurants open while others close.

None of this means the economy is below full employment. The real problem is when workers are being **fired but no one is hiring**: resources sit idle because there is no demand for output.

**Graph: business cycle**

- Time is on the horizontal axis and output on the vertical axis.
- A smooth upward trend line shows potential output.
- Actual output fluctuates around it: **booms** above the trend and **contractions/recessions** below it.
- Central question: why does the economy fluctuate?

**Historical note:** Ben Bernanke (Nobel laureate), *Essays on the Great Depression*.

- The 1930s Great Depression showed that factories and workers can both exist, yet firms don't hire because they fear they cannot sell output.
- This gave birth to formal macroeconomics.

---

### 2.10 Why Recessions Cut Output, Not Prices: Keynesian AD–AS

**Graph**

- **Horizontal axis:** output, income, or spending $Y$. Income = expenditure, since someone's income is someone else's spending.
- **Vertical axis:** price level $P$.
- **Vertical (green) line at $Y^*$:** potential output (long-run supply). It does not shift with demand.
- In a recession, firms produce $Y_1 < Y^*$ because they believe they cannot sell $Y^*$ at prevailing prices.
- Simple micro logic says firms could cut prices and sell everything. In practice, firms **cut production first**.

**Why firms cut production rather than prices**

1. **Customer habituation.** If a ₹5,000 product is cut to ₹4,000, customers get used to the lower price. Raising it again when demand recovers is difficult.
2. **Cutting prices requires cutting wages,** because wages are a major part of costs, and **nominal wages are rigid downward**.
   - Example: a haircut sells for ₹100 and the barber is paid ₹3,000–5,000/month. To sell haircuts at ₹80, wages must fall, but workers resist.
   - Workers distrust the employer's claim of a recession and take wage cuts as a matter of personal prestige. It is **easier to fire than to cut wages**.
   - Fired workers eventually discover other firms aren't hiring either, then accept lower wages. Costs fall and the economy returns to equilibrium, but this takes months or years. The question is whether to wait that long.

**Short-run aggregate supply is flat when there is unemployment**

- In micro, the supply curve slopes upward (more output at higher prices).
- In a macro recession, many workers are unemployed and willing to work at **prevailing wages**. Firms can expand output **without raising costs**, so the SRAS is **horizontal**.
- At full employment, an extra worker must be **poached** from another firm with higher wages. Costs rise, so supply slopes upward.

**Keynes (Keynesian framework)**

- In the Great Depression, firms fired workers rather than cut prices because wages are rigid.
- Since wages are part of costs, **prices are sticky in the short run**.
- **Business cycles are driven by shifts in aggregate demand (AD).** $Y^*$ does not change.

**Policy implication:** boost AD, for example through government spending.

- Example: the government builds a highway, which raises demand for cement and steel.
- Factories recall laid-off workers at prevailing wages.
- Output expands **without higher costs** (movement along the flat SRAS toward $Y^*$).

---

### 2.11 Aggregate Demand: Planned vs. Unplanned Components

- Aggregate demand = output = income.
- **Planned demand** is output produced to meet expected demand.
- **Unplanned inventory accumulation** happens when goods are produced but not sold.
  - Workers must still be paid, and the unsold goods pile up as inventory.
  - Inventory counts as **investment**, but this part is **unplanned investment**.
  - Firms respond by **cutting production in the next round**. This is the adjustment mechanism.

---

### 2.12 Consumption Function

**Importance:** consumption is the **largest component of AD**, about **60%** of GDP in India and about **70%** in the US.

**Determinants of consumption**

- **Income**, the most important factor.
- Future income prospects.
- Social security and pensions.
- Interest rates.
- **Age** (life-cycle idea): the young consume less than their income, while the old or retired consume more than their income by drawing on past savings.

**Bidirectional relationship**

- Spending depends on income, especially consumption.
- Income at the economy level depends on spending, because someone's purchase is someone else's income.
- This feedback loop is the basis of the **multiplier**.

**Consumption function:**

$$C = \bar{C} + c\,Y$$

- $\bar{C}$ is **autonomous (baseline) consumption**, consumed even with zero income for survival.
- $c$ is the **marginal propensity to consume (MPC)**: the extra consumption out of each additional ₹1 of income, typically $0 < c < 1$:

$$c = \frac{\Delta C}{\Delta Y}$$

- So total consumption = autonomous part + income-induced part.

**Next session:** add investment and derive the **Keynesian multiplier model**.

---

### 2.13 Closing Q&A: Micro vs. Macro Shocks

A student asked whether unplanned inventory can sink a firm, especially for perishable goods such as preservative-free juice during the COVID lockdown.

**Micro problem:** a firm- or sector-specific demand shift. Examples:

- consumers switch from wheat to millets;
- consumers turn against sugary drinks.

One product loses demand while another gains.

**Macro problem:** all firms face similar challenges at once.

- Example: under COVID lockdowns, fresh juice and fresh ice cream with one-week shelf life expired.
- The milk and inputs were wasted, and inventories were written off across many firms.
- This is an aggregate demand problem, to be covered further next session.

---

## 3. Points Flagged as Important

No specific exam or assignment was mentioned. The lecturer emphasised these points:

- **The food-inflation and DA redistribution argument** was explicitly called *"a subtle point but a very important point."* Be able to explain why indexed, higher-income earners can gain from food-led inflation while the poor lose.
- **The base year is "very crucial."** Know why real GDP uses base-year prices, the criteria for choosing a base year (normal, recent), and why it is revised.
- **Real vs. nominal GDP calculation.** Be able to reproduce the wheat/potato example (200 to 3200 nominal; 200 to 800 real; $16 = 4 \times 4$).
- **The CPI formula** in both forms (weighted average of price relatives with base-year expenditure shares, and the Laspeyres ratio), and the CPI vs. WPI distinction.
- **Unexpected inflation redistributes from lenders to borrowers.** Know the $i = 10\%$, $\pi^e = 6\%$ vs. $\pi = 12\%$ example.
- **The Keynesian logic** of sticky wages, sticky prices, flat SRAS, and AD-driven cycles, plus the consumption function $C = \bar{C} + cY$. This is the foundation for **the multiplier model next session**.
- Monetary policy and inflation uncertainty will be covered in a later (fifth or sixth) session of the macro module.

---

### Quick Formula Sheet

$$\text{Nominal GDP}_t = \sum_{i} P_{i,t}Q_{i,t} \qquad \text{Real GDP}_t = \sum_{i} P_{i,b}Q_{i,t}$$

$$\text{CPI}_t = \sum_{i} s_{i,b}\frac{P_{i,t}}{P_{i,b}} = \frac{\sum_i P_{i,t}Q_{i,b}}{\sum_i P_{i,b}Q_{i,b}}, \qquad s_{i,b} = \frac{P_{i,b}Q_{i,b}}{\sum_j P_{j,b}Q_{j,b}}$$

$$\pi_t = \frac{\text{CPI}_t - \text{CPI}_{t-1}}{\text{CPI}_{t-1}}\times 100 \qquad g_{\text{nominal}} \approx g_{\text{real}} + \pi$$

$$1 + r = \frac{1+i}{1+\pi} \;\;\Rightarrow\;\; r \approx i - \pi^e$$

$$C = \bar{C} + cY, \qquad c = \text{MPC} = \frac{\Delta C}{\Delta Y}$$

$$Y = C + I + G + X - M$$