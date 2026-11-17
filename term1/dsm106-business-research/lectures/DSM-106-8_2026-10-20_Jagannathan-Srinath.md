---
course: DSM 106
date: 2026-10-20
start: 7:00pm
session: "8"
faculty: Jagannathan Srinath
---

<!-- nav -->
← [Session 7 (2026-10-19)](DSM-106-7_2026-10-19_Jagannathan-Srinath.md) · [All lectures](./) · [Session 9 (2026-10-21)](DSM-106-9_2026-10-21_Jagannathan-Srinath.md) →
<!-- /nav -->

# DSM-106 Business Research, Session 8 (2026-10-20): Whole Foods Market Case and Financial-Ratio Analysis

*Instructor: Jagannathan Srinath. Notes reconstructed from an ASR transcript. Garbled numbers are flagged as such. Currency is written as "USD" in running text so it isn't mistaken for math notation.*

---

## 1. Overview

This session opened the **Whole Foods Market (May 2014)** case. Deutsche Bank had a "buy up to ~USD 60" call on Whole Foods. A quarterly earnings miss then caused a roughly 20% share-price drop, and the bank had to decide whether to keep its buy recommendation or switch to sell. The research question is whether Whole Foods can keep its price premium and profitability as competition in organic groceries intensifies.

The class worked through three analyses using the case exhibits, which the instructor had copied into Excel:

1. **Competitive benchmarking** using same-store sales growth and store counts against organic, mid-level, and large retail peers.
2. **Return on Capital (ROC)**, including a sensitivity analysis on the EBITDA margin forecast.
3. **Cost of capital (WACC)** using CAPM, credit ratings and beta, which ROC is compared against. This led into a discussion of leverage.

The **EBITDA multiple** analysis was announced but deferred to the next session.

---

## 2. Topics and Concepts (in order taught)

### 2.1 Case Setup: Whole Foods Market (WFM)

**Company**
- US grocery retailer specialising in organic products: meat, eggs, vegetables, milk and other groceries.
- Operates many stores, historically in high-income and upper-middle-income neighbourhoods.

**The dilemma**
- WFM stock was trading at about USD 48–49.
- Deutsche Bank's advice: keep buying up to about USD 60, and stop buying only above USD 60.

**Quarterly report (May 2014)**

| Item | Expected / Earlier | Actual / New |
|---|---|---|
| EPS | USD 0.41 | USD 0.38 |
| Dividend per share | USD 0.10 (planned) | USD 0.12 |
| Share price | about USD 48 | about USD 38 |

- The share price fell by roughly 20%.

**Derived figures** (Rahul's calculation, plus checks):

- EPS shortfall:
$$\frac{0.38 - 0.41}{0.41} \approx -7.32\%$$
- Dividend increase:
$$\frac{0.12 - 0.10}{0.10} = 20\%$$
- Payout ratio ("almost a third of earnings"):
$$\frac{0.12}{0.38} \approx 31.6\%$$
- Price drop:
$$\frac{38 - 48}{48} \approx -20.8\%$$

**Rahul's insight:** a firm can still be profitable and raise its dividend, yet see its share price fall. Investors read the earnings miss as a sign of weakening competitive position.

**Research question:** Should Deutsche Bank keep its *buy* recommendation or move to *sell*? Put differently, will WFM sustain its profitability and price premium in the future?

### 2.2 Industry Context and the Bull/Bear Debate

**Growth rates**
- The organic segment has grown about 20% per year since 1990 (point added by Jasraj).
- The overall grocery sector grows only about 3–4% per year, roughly in line with population growth.
- WFM sells at a premium and earns large profits on the "organic" positioning.

**Bear arguments**
- What counts as "organic" is debatable, so the premium may amount to consumer exploitation.
- Organic food may be less nutritious than conventional or GM/fertiliser-grown food.
- Organic farming may use more water, which makes it environmentally questionable.
- Competition is rising:
  - Walmart says it can sell organic more cheaply.
  - Organic specialists **Sprouts** and **The Fresh Market** are expanding.
- The result is margin squeeze: WFM can no longer charge its former premium.

**Bull argument**
- WFM is the innovator and market leader.
- It uses about **75 criteria** to define "organic" and educates consumers.
- It argues that competitors such as Walmart cannot meet all 75 criteria.

**Key uncertainty:** Will consumers care whether all 75 criteria are met?
- If yes, WFM keeps its premium.
- If consumers accept "mostly organic but cheaper," WFM's profitability and share price keep falling.

**Demand profile:** Buyers are mainly high-income and upper-middle-class consumers motivated by health.

### 2.3 Analysis 1: Competitive Benchmarking (volunteer: Minakshi)

The data came from case exhibits on same-store sales growth and store counts for 2008–2013.

**Peer groups**

| Group | Companies |
|---|---|
| Organic peers | Sprouts, Fresh Market (plus an organic-segment industry average) |
| Mid-level conventional grocers | Kroger, Safeway, SuperValu (about 2,000–2,500 stores each) |
| Large retailers | Walmart, Costco |

**Same-store sales growth findings**
- **2008–09:** growth was negative across the industry because of the financial crisis. This was not specific to WFM.
- WFM generally beat:
  - the organic industry average,
  - the mid-level grocers, and
  - Walmart and Costco.
- Sprouts beat WFM in some years but not all.
- **Competitors are catching up.** Comparison figures read out in class:

| Year | WFM | Organic competitor figure |
|---|---|---|
| 2010 | 7 | 3.7 |
| 2011 | 8 | 5.3 |
| 2012 | 8 | 7.7 |
| 2013 | 7 | 7 |

**Store count findings**
- Walmart is a behemoth by store count. Compared with it, WFM is minuscule, but it serves a niche.
- Sprouts grew from **36 stores (2008) to 167 stores (2013)**, still only about half of WFM's count. (A WFM figure was read as "275 to 84"; the exact numbers are garbled in the transcript.)
- WFM's store growth is slower than its organic peers' growth.
- Mid-level grocers are being squeezed by Walmart and are closing stores, so their growth is negative.
- Walmart and Costco keep adding stores.

**Conclusion:** Competition is increasing, so WFM's profit margin is likely to be squeezed unless it can credibly differentiate.

**Side discussion: BCG matrix (raised by Rahul)**
- The four quadrants are Stars, Cash Cows, Question Marks and Dogs.
- WFM is not a cash cow; it sits as a **Star**.
- Rising competition could push it toward **Question Mark**.
- The instructor's view: WFM can hardly justify any strategy other than "Star." If it moves away, it loses both its price premium and its organic credibility.
- WFM did try two moves:
  - **Private labels** at more affordable prices.
  - **Stores in middle and lower-middle-income neighbourhoods.** This largely failed because those households are less keen on organic.

### 2.4 Analysis 2: Return on Capital (ROC) (volunteer: Tejas)

**Data source:** Case Exhibit 7, with 2011–2013 actuals and 2014–2015 forecasts.

**Forecast assumptions**

| | 2014F | 2015F |
|---|---|---|
| Sales growth | 11.1% | 14% |
| EBITDA margin | 9.4% | 9.8% |

**Definitions**
- **EBIT:** earnings before interest and taxes. The instructor glossed it as "earnings before income tax" or "gross profit."
- **EBITDA:** earnings before interest, taxes, depreciation and amortisation.
- **Depreciation:** assets such as ACs, lights, computers and storage lose value over time and must eventually be replaced.

**Formulas used**

EBITDA margin:
$$\text{EBITDA margin} = \frac{\text{EBITDA}}{\text{Sales}}$$

After-tax operating profit (NOPAT). In the Excel sheet this is `=C21*(1-C10)`, where C21 is EBIT and C10 is the tax rate:
$$\text{NOPAT} = \text{EBIT} \times (1 - t)$$

Net working capital:
$$\text{NWC} = \text{Current Assets} - \text{Current Liabilities}$$
- **Current assets:** mainly inventory held in stores (groceries, milk, meat, vegetables).
- **Current liabilities:** stock bought on credit from suppliers, with bills settled weekly or monthly.

Invested capital, the "value of the company" or the investment needed:
$$\text{Capital} = \text{PP\&E} + \text{NWC}$$

Return on capital:
$$\text{ROC} = \frac{\text{NOPAT}}{\text{Capital}}$$

Earnings per share:
$$\text{EPS} = \frac{\text{Net income}}{\text{Shares outstanding}}$$

**Worked example (first year column, USD million)**

> **Year labelling discrepancy.** The instructor said "2010" here. However, the 13.2% ROC was later cited as **2011**, and the 2011 EBITDA margin used sales of about 10,108. Treat this column as FY2011.

| Item | Value |
|---|---|
| EBIT | 548 |
| Tax rate | 38.1% (rises to about 39% in later years) |
| Tax | about 209 |
| NOPAT | 339 |
| Current assets | 1,453 |
| NWC | 573 |
| PP&E | 1,997 |
| Capital | about 2,500 |
| Shares outstanding | 350 million (no debt) |
| EPS | about 0.97 |

The calculations behind the table:
$$548 \times (1 - 0.381) \approx 339$$
$$\text{Capital} = 1{,}997 + 573 = 2{,}570 \approx 2{,}500$$
$$\text{ROC} = \frac{339}{2{,}570} \approx 13.2\%$$
$$\text{EPS} = \frac{339}{350} \approx 0.97$$

**Interpretation:** for every 100 invested, the company earns about 13.2 in after-tax operating profit.

**EBITDA margin check for 2011:**
$$\frac{859}{10{,}108} \approx 8.5\%$$
The sales figure was transcribed as "10,98"; 10,108 fits the 8.5% result.

**Margin and ROC trend**

| | 2011 | 2012 | 2013 |
|---|---|---|---|
| EBITDA margin | 8.5% | 9.0% | 9.5% |
| ROC | 13.2% | about 14.8% (garbled as "2018 8%") | 16.3% |

- Shares outstanding later rose by 22 million, to 372 million.
- EPS and net income also rose.

**Key principle:** Never view net income in isolation; always compare it with capital invested. If capital rises a lot while net income rises only slightly, the business is not very profitable. You might as well put the money in a fixed deposit.

**Sensitivity analysis on the 2014 EBITDA margin**

The forecast holds only if the EBITDA margin forecast holds. With more competition, selling prices fall and so does the EBITDA margin.

| 2014 EBITDA margin | ROC | EPS |
|---|---|---|
| 9.4% (base forecast) | about 17.1% | about USD 1.45 |
| 6.3% (Tejas's stress case) | about 9.3% | about USD 0.87 |

- The 6.3% case is an extreme assumption; the margin is unlikely to drop that far suddenly.
- In that case EPS falls by roughly 40%. Shareholders would ask why they should stay invested, sell, and the share price would fall: "everything goes for a toss."

**Instructor's red line**
- WFM needs ROC of at least about **13%**.
- That requires an EBITDA margin of at least about **9%**.
- **Below a 9% EBITDA margin is the red line for this company.**

### 2.5 Analysis 3: Cost of Capital and WACC (volunteer: Shivam)

**Core idea:** Capital is not free.
- **Debt** costs **interest**.
- **Equity** costs **dividends** (shareholder returns).
- These are the only two sources of finance.
- ROC must exceed the cost of capital. For example, borrowing at 15% to earn 13.2% makes no sense.
- If the cost of capital exceeds ROC, it is better to sell off the business.

**Assumptions, taken from the case's last exhibits**

| Parameter | Value | Source / meaning |
|---|---|---|
| Tax rate $t$ | 39% | Case |
| Risk-free rate $r_f$ | 3.4% | 30-year US Treasury bond, treated as risk-free |
| Market risk premium (MRP) | 5% | Market return carries risk (could be +5% or −5%) |
| WFM cost of debt $K_d$ | 4.29% | AA credit rating, 30-year maturity |

**Why WFM's cost of debt is 4.29%**
- WFM has **zero debt**, so it gets the highest (AA) rating.
- An AA-rated firm pays 4.29% versus 3.4% on Treasuries.
- Debt market basics:
  - Companies issue **corporate bonds**.
  - Corporate bonds are the main example of **fixed-income securities**: interest is paid every year and the principal is repaid at maturity (for example, 30 years).
  - Buyers are mostly banks and financial institutions, but retail investors can also buy.

**Comparison: Sprouts**
- Rating: **BB−**.
- Cost of debt: **6.83%**.
- Reason: about USD 304 million of existing debt against only about USD 2,400–2,500 million in annual sales. (The debt figure was transcribed as "34 million" but read as "304".)

**Beta ($\beta$)**
- Measures how a company moves relative to the market. It is a risk measure.
- $\beta = 0.7$ (WFM): if the market rises or falls 1%, WFM rises or falls 0.7%. This is less risky than the market.
- $\beta = 1.3$: higher return when the market rises, but larger losses when it falls. Higher risk goes with higher return.
- Beta is readily published by financial institutions, just as credit ratings are.

**Cost of equity (CAPM)**
$$K_e = r_f + \beta \times \text{MRP}$$

**Weighted average cost of capital**
$$\text{WACC} = \frac{D}{V}\,K_d\,(1 - t) + \frac{E}{V}\,K_e, \qquad V = D + E$$
- $E$ is the market capitalisation of equity and $D$ is debt.
- Debt is multiplied by $(1-t)$ because interest payments are tax-deductible.

**Worked example 1: Whole Foods**

$$K_e = 3.4\% + 0.7 \times 5\% = 6.9\%$$

- $V = 14{,}481$ (USD million), all equity.
- $D/V = 0$.

$$\text{WACC} = K_e = 6.9\%$$

**Worked example 2: Walmart**
- Debt $D = 55{,}245$ and market cap $E = 251{,}747$ (USD million).
- Walmart still holds an AA rating because it is large and trusted.
- $\beta = 0.6$ and $K_d = 4.29\%$.

$$K_e = 3.4\% + 0.6 \times 5\% = 6.4\%$$
$$\frac{D}{V} = \frac{55{,}245}{251{,}747 + 55{,}245} = \frac{55{,}245}{306{,}992} \approx 0.18$$
$$\text{WACC} \approx 0.18 \times 4.29\% \times (1 - 0.39) + 0.82 \times 6.4\% \approx 0.47\% + 5.25\% \approx 5.72\%$$

> **Transcript errors in this example.** The instructor said "72% multiplied by 6.4"; the equity weight is $1 - 0.18 = 0.82$. A "3.72%" was also mentioned, but the computed result is **5.72%**.

Walmart can raise capital more cheaply than WFM.

**Worked example 3: SuperValu (mid-level conventional grocer)**
- $\beta = 1$, so it carries the same risk as the market.

$$K_e = 3.4\% + 1 \times 5\% = 8.4\%$$

- Raising equity is more expensive for SuperValu because it is seen as riskier.

**Conclusion on WFM**
- WFM's ROC (13–16%) is roughly **double, sometimes triple**, its WACC (6.9%), so it is a profitable business.
- The reason is its organic positioning: high perceived quality supports a high margin, which supports a high ROC.
- **Bare-minimum rule:** ROC must exceed about **7%**. Above that the company can survive, but shareholders won't be happy with thin margins.
- Even the 6.3% EBITDA stress case gives ROC of about 9.3%, which is still above 6.9%. The company could still run, but the market would punish the EPS fall from USD 1.45 to USD 0.87.
- If competition squeezes margins, ROC falls toward WACC. This is the future risk.

### 2.6 Q&A Clarifications

**Maturity matching (Shivam)**
- The 3.4% risk-free rate and the 4.29% cost of debt are both 30-year.
- The assumption is long-term debt, with maturities matched.

**What is the market risk premium? (Jasraj)**
- A Treasury gives a guaranteed 3.4% per year.
- The market offers no guarantee. On average it is expected to grow about 5%, with risk attached, and each company carries a different level of risk via its beta.
- The instructor said the 5% is taken as the **average growth rate of the retail market** (organic, mid-level and large chains combined) from the sales-growth exhibit.

> **Supplementary note:** in standard finance, MRP is the expected market return minus the risk-free rate, usually estimated from historical equity returns. The class treated it as about 5% via retail growth.

**How is beta calculated? (Siddharth)**
- Look at the company's historical performance versus the market, including the correlation and the relative volatility of its growth.
- Volatility is measured by standard deviation. If the company's standard deviation is below the market's, the company is less risky and has a lower beta.
- Intuition given: roughly $\sigma_{\text{company}} / \sigma_{\text{market}}$. The instructor stressed this is **not the exact formula**.

> **Supplementary note:** the standard formula is
> $$\beta = \frac{\operatorname{Cov}(R_i, R_m)}{\operatorname{Var}(R_m)}$$

**Zero debt: discount at the cost of equity or a target-structure WACC? (Nihal)**
- With zero debt, WACC is essentially $K_e$.
- WFM has room to take debt. Because $K_d$ (4.29%) is below its WACC (6.9%), adding debt would lower its cost of capital and raise firm value. This is **leverage**.

| Company | Room to lever up |
|---|---|
| WFM, Fresh Market, Walmart | Lots of room |
| Sprouts | Little room (6.83% cost of debt vs 6.92%) |
| Safeway | Cannot |
| SuperValu | None; negative leverage, with $D/V = 0.57$ (57% of value is debt), which is unsustainable |
| Walmart | $D/V = 0.18$ is manageable and prudent; its $K_d$ is still below its cost of capital, so it can borrow easily in a crisis |

- **Indian examples:**
  - Adani Enterprises carries about ₹2 lakh crore of debt, which gives it little room for leverage.
  - Reliance considered selling a stake to Aramco to reduce its debt-to-value ratio.

**Why use the 30-year rate rather than 5-year? (Nihal)**
- The analysis concerns long-term corporate debt.
- Strong, trusted firms can issue 30-year bonds, much like an individual's 15–20 year EMI loan.
- The instructor's claim: short-term loans are always more expensive, and a long tenor means a lower rate and lower total interest.

> **Caveat:** in practice, under a normal upward-sloping yield curve, long-term rates are often *higher* than short-term rates. Treat the instructor's claim as the class's position, not a general rule.

---

## 3. Flagged as Important / Takeaways for Exams and Assignments

No explicit "this will be on the exam" statement was made. These points were repeatedly emphasised:

- **Always compare ROC with the cost of capital (WACC).**
  - If ROC is above WACC, the business creates value.
  - If ROC is below WACC, it is better to sell the business.
- **Never judge net income in isolation.** Judge it relative to capital invested.
- **The EBITDA margin is the critical driver for WFM.**
  - The red line is about **9% EBITDA margin**, which corresponds to about **13% ROC**.
  - The bare minimum ROC is above about 7%, just over the 6.9% WACC.
- Know these formulas and how to apply them:
  - NOPAT
  - NWC
  - Capital
  - ROC
  - EPS
  - EBITDA margin
  - CAPM
  - WACC, including the tax shield on debt
- Understand how **credit rating** drives cost of debt, and how **beta** drives cost of equity.
- Understand the **leverage** concept: when $K_d$ is below WACC, there is room to add debt.
- **Assumptions and sensitivity analysis:** forecasts (e.g., a 9.4% margin) are only as good as their assumptions, so stress-test them.
- **Next session:** continue the WFM case with the **EBITDA multiple** valuation, then reach a buy/sell recommendation. Come having read the case exhibits, especially Exhibit 7 and the final exhibits on ratings, betas and debt.

<!-- nav -->
← [Session 7 (2026-10-19)](DSM-106-7_2026-10-19_Jagannathan-Srinath.md) · [All lectures](./) · [Session 9 (2026-10-21)](DSM-106-9_2026-10-21_Jagannathan-Srinath.md) →
<!-- /nav -->
