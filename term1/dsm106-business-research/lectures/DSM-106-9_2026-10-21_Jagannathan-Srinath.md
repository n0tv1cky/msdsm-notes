---
course: DSM 106
date: 2026-10-21
start: 7:00pm
session: "9"
faculty: Jagannathan Srinath
---

<!-- nav -->
← [Session 8 (2026-10-20)](DSM-106-8_2026-10-20_Jagannathan-Srinath.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-106 (Business Research), Session 9: Whole Foods Market Valuation (EV/EBITDA Multiples and Discounted Cash Flow)

**Session file:** DSM-106-9_2026-10-21_Jagannathan-Srinath
**Case:** Whole Foods Market (WFM), May 2014. Is Deutsche Bank's "buy up to USD 60" recommendation justified?
**Volunteers:** Nihal (multiples analysis), Jasraj (DCF analysis)

> **Transcription notes:**
> - "AIDA / EIDA / AITA / EMIDA" in the transcript is **EBITDA**.
> - Dollar amounts are written as "USD" so they don't clash with LaTeX math delimiters.
> - Figures are in USD millions unless stated otherwise.

---

## 1. Overview

This session continued the previous day's Whole Foods Market case. In May 2014, after a weak quarterly earnings report, WFM's share price fell from about USD 48–49 to USD 38.19. Deutsche Bank still recommended buying the stock up to USD 60. The class tested that claim with two valuation methods, each worked through in Excel with a student volunteer.

1. **Relative valuation using EV/EBITDA multiples.** WFM was compared with natural/organic grocers, conventional grocers and large wholesalers (Walmart, Costco).
2. **Discounted cash flow (DCF).** Free cash flows were projected for 10 years, a terminal value was added, everything was discounted at the cost of capital, and the result was divided by shares outstanding.

The central lesson is that both methods hinge on one assumption: **whether WFM can sustain its premium EBITDA margin** as competition increases. The class ran three scenarios:

| Scenario | Implied share price |
|---|---|
| Base case (Deutsche Bank-style) | USD 58.28 |
| Worst case | USD 16 |
| Middle case | USD 36.13 |

The class then compared these with what actually happened: margins fell, the stock stagnated, and Amazon acquired WFM. The session closed with a proposed EBITDA-multiple group assignment (Adani Enterprises) and administrative notes.

---

## 2. Topics and Concepts (in order taught)

### 2.1 Case context and research question

- **Timeline (2014):**
  - Before Q-results: WFM traded at about USD 48–49 (USD 48.61 in April 2014).
  - Q-results: earnings per share (EPS) disappointed and the share fell about 20% to USD 38.19.
  - Deutsche Bank recommendation: keep buying until the price reaches USD 60.
- **Research question:** Given rising competitive pressure on WFM's margins, is a USD 60 valuation justified?
- **Data sources:** case exhibits containing financial data for WFM and its competitors, plus Deutsche Bank's projections. The instructor will share the Excel sheets after class so students can change the assumptions themselves.

### 2.2 EBITDA and EBITDA margin

- **EBITDA** = Earnings Before Interest, Taxes, Depreciation and Amortization.
- The instructor equated EBITDA with "gross profit" and explained it as "selling price minus cost price."
  - *Caution:* in standard accounting, gross profit = Sales − COGS, which is not the same as EBITDA. For this case, follow the lecture's usage, but know the distinction for finance courses.
- Formula:

```math
\text{EBITDA margin} = \frac{\text{EBITDA}}{\text{Sales}}
```

- **WFM EBITDA margin = 9.5%.** **Walmart = 7.5%.** **Costco = 3.8%**, similar to conventional grocers.
- **Why WFM earns a higher margin:** it sells organic products positioned as premium, so consumers pay more. Its margin is higher even than Walmart's.

### 2.3 Enterprise Value (EV) and leverage

- EV is the market valuation of the firm:

```math
\text{EV} = \text{Equity value (market cap)} + \text{Debt}
```

- **WFM:** EV = 14,481. WFM carries no debt, so EV = equity value.
- **Walmart:** $\text{EV} = 251{,}747 + 55{,}245 = 306{,}992$.
- **Leverage:** the value of a firm is not just share price × number of shares; debt also adds to firm value. Taking on debt can raise the value of the firm.

### 2.4 EV/EBITDA multiple (relative valuation, Method 1)

- Formula:

```math
\text{EBITDA multiple} = \frac{\text{EV}}{\text{EBITDA}}
```

- **WFM:** $\dfrac{14{,}481}{1{,}222} \approx 11.9$. The market values WFM at 11.9 times its annual EBITDA.
- **A multiple means nothing by itself.** It must be compared with industry peers:
  - **Sprouts:** multiple = 23.6, with EBITDA of only 187 and EV of about USD 4.4 bn.
    - This suggests heavy overvaluation relative to peers.
    - A market correction (share price fall) is likely in the future.
  - **Walmart:** multiple = 8.6, despite being a very large firm.
  - **Costco:** multiple = 13.6, despite a thin 3.8% margin.
  - **The Fresh Market:** close to WFM.
- **Interpretation for WFM:**
  - Compared with natural/organic peers, WFM looks fairly valued.
  - Compared with conventional grocers, and with wholesalers other than Costco, WFM looks overvalued.
- **Size effect:** small firms (e.g., Sprouts) can carry high multiples. As firms reach scale, high multiples become hard to sustain and tend to fall. Walmart's 8.6 is a "reasonable" multiple for a giant.
- **Rule of thumb from the lecture:** a multiple far above the industry's suggests overvaluation. However, there is **no objective benchmark**; the choice of peers is a judgment call. (Nihal's question: shouldn't the analyst compare against all relevant competitors? Answer: yes, compare against a range.)

#### Worked example: re-pricing WFM at peer multiples (372 million shares outstanding)

**At Walmart's multiple (8.6):**

```math
\text{EV} = 1{,}222 \times 8.6 = 10{,}509 \text{ (about USD 10.5 bn)}
```

```math
\text{Share price} = \frac{10{,}509}{372} \approx 28.25 \text{ USD}
```

This is well below the USD 38.19 market price and the USD 60 target, so on this basis WFM looks overvalued.

**At Costco's multiple (13.6):**

```math
\text{EV} = 1{,}222 \times 13.6 = 16{,}619
```

```math
\text{Share price} = \frac{16{,}619}{372} \approx 44.7 \text{ USD (about USD 45)}
```

**Takeaway:** to justify its price, WFM must **consistently maintain a profit margin above Walmart's** (9.5% vs 7.5%). New competitors are squeezing that margin, which is why the share price is in question.

#### Intuition example: buying a company

- Suppose a company's annual EBITDA ("gross profit") is ₹200 crore.
- The seller asks ₹4,000 crore. This implies a multiple of $\frac{4000}{200} = 20\times$.
- The buyer replies that no competitor trades above 10×, so they offer $10 \times 200 = ₹2{,}000$ crore. This is how negotiations work.
- A shareholder buys only one share, not the whole firm. That is why analysts translate firm value into a **per-share price**.

#### How analysts use the method

1. Compute the multiple.
2. Judge whether it is under-, over- or fairly valued relative to peers.
3. Choose an "appropriate" multiple.
4. Project the share price from it.

This involves some speculation.

### 2.5 Discounted Cash Flow (DCF) method (Method 2)

#### (a) Inputs and assumptions

| Item | Actual (2011–2013) | Deutsche Bank 2014 | Deutsche Bank 2015 | Instructor's 10-yr extension | Steady state (perpetuity) |
|---|---|---|---|---|---|
| Store growth | from case | 10.5% | 12.6% | constant 10% | 3.4% |
| Sales growth | from case | 11.1% | 14% | declines from about 12% down to 8% by year 10 | 3.4% |
| EBITDA margin | ~9.5% historically | 9.4% | 9.8% | about 9.5%, then 9.3% if WFM stays competitive | 9.3% |
| Tax rate | — | 39% | 39% | 39% | 39% |

- **Steady-state growth of 3.4%** is the rate at which the firm grows forever. It was justified as approximately:
  - the risk-free/bond rate (about 3–4%),
  - US population/economic growth, and
  - retail-sector growth.
- All assumptions are debatable. If WFM is not competitive, the margin assumption should be lowered.

#### (b) Operating ratios used to project the balance sheet

**1. Current asset turnover**

```math
\text{Current asset turnover} = \frac{\text{Sales}}{\text{Current assets}}
```

- Actuals: 7.0, 5.6, 6.5. For example, sales of 10,108 divided by current assets gives 7.0.
- Projected to rise to 7.2 and then stay at 7.6.
- For a grocer, current assets are mainly perishable inventory held for days up to about two weeks.
- **High turnover** means inventory converts to sales quickly, which indicates efficient operations.
- **Low turnover** (e.g., 1–1.5) means goods sit too long, perish, and cause losses. (Jasraj's answer.)
- Interpretation depends on the industry. A furniture retailer can reasonably hold inventory for 3–4 months.

**2. Current liabilities turnover**

```math
\text{COGS} = \text{Sales} - \text{EBITDA}, \qquad \text{Current liabilities turnover} = \frac{\text{COGS}}{\text{Current liabilities}}
```

- Current liabilities are unpaid supplier bills for inventory.
- **Low turnover:** bills are settled slowly (30/60/90 days or longer).
  - Example: Walmart buys in bulk under stable long-term contracts, so it pays suppliers late.
- **High turnover:** bills are settled quickly.
  - Example: WFM sources from small and medium organic producers. These producers lack the staying power of large corporate farms, so WFM must pay them fast.
- "Neither is better or worse; it depends on business strategy."
- Projected at **10.5** for WFM.
  - For WFM, current liabilities turnover above current asset turnover is acceptable.
  - For Walmart, it would be about equal to, or much smaller than, current asset turnover.
- **Indian digression:** firms like Reliance (Jio) and Adani want agricultural law reform. Corporate farming would allow long-term credit agreements with suppliers, which lowers current liabilities turnover and raises profitability. Farmers fear losing their land, which creates a tension in the Indian economy.

**3. Net PP&E per store**

- Plant and equipment per store includes items such as air conditioning and cold storage.

```math
\frac{1{,}997}{311} \approx 6.4 \text{ USD million per store (2013)}
```

- Projected to decline to about USD 5.4 million per store as stores become smaller.

**4. Depreciation and amortization per store**

- Projected at about USD 0.89 million per store, roughly 15–16% depreciation of PP&E.

> These ratios are described as "crucial for financial analysis."

#### (c) Building the projection (actuals to 2013, projections from 2014)

1. Number of stores, from store growth.
2. Sales, from sales growth.
3. EBITDA = Sales × EBITDA margin.
4. D&A = stores × D&A per store.
5. EBIT (pre-tax profit) = EBITDA − D&A. The terminal-year figure is about 2,318.
6. Current assets = Sales ÷ current asset turnover.
7. Current liabilities = COGS ÷ current liabilities turnover.
8. **Net working capital (NWC):**

```math
\text{NWC} = \text{Current assets} - \text{Current liabilities}
```

   - NWC is inventory minus bills to be settled.
   - Slightly negative NWC is fine. It means inventory sells fast and bills are paid slowly; Walmart may have negative NWC.
   - WFM pays suppliers quickly, so its NWC is positive.
9. Net PP&E = stores × PP&E per store.
10. Revenue per store = Sales ÷ number of stores.

#### (d) Return on capital (ROC)

```math
\text{ROC} = \frac{\text{NOPAT}}{\text{NWC} + \text{Net PP\&E}}
```

- The denominator is the capital needed to run the business: short-term capital (working capital) plus long-term capital (plant and equipment). It is roughly what a buyer would pay at minimum.
- Last actual ROC: about 16.37%. Projected: **20.9%** (including perpetuity). This is very high compared with the **cost of capital of about 6.9–7%**.
- If competition squeezes margins, ROC falls. This is the **key assumption**.

**Other turnover ratios:**

```math
\text{NWC turnover} = \frac{\text{Sales}}{\text{NWC}}, \qquad \text{PP\&E turnover} = \frac{\text{Sales}}{\text{Net PP\&E}}
```

- Sales are well above NWC, so there are no short-term liquidity problems.
- Sales exceed long-term assets.

#### (e) Discount rate and present value

- **Steady-state growth:** $g = 3.4\text{%}$.
- **Discount rate:** $r = 7\text{%}$, the cost of capital of 6.9% rounded. It is the cost of raising money through shares or corporate bonds.
- **Time value of money:**

```math
PV = \frac{CF_t}{(1+r)^t}
```

- One dollar next year is worth $\frac{1}{1.07} \approx 0.93$ dollars today.
  - The lecturer said two years out would be "about 0.91–0.92." The correct figure is $\frac{1}{1.07^2} \approx 0.87$.
- Personal example: ₹1 crore received next year is worth about ₹93 lakh today.

#### (f) Free cash flow

```math
\text{NOPAT} = \text{EBIT} \times (1 - t)
```

- Example: $976 \times (1 - 0.39) \approx 596$.

```math
\text{FCF} = \text{NOPAT} - \Delta\text{Net PP\&E} - \Delta\text{NWC}
```

- From net profit, some money goes into PP&E for new stores and some into maintaining working capital. What remains is cash in hand.

#### (g) Valuation steps (base case)

**1. PV of the forecast period (10 years).** In Excel this is `=NPV(7%, FCF range)`.

```math
PV_{\text{forecast}} = \sum_{t=1}^{10} \frac{FCF_t}{(1.07)^t} = 4{,}328
```

**2. Terminal value (constant-growth / Gordon growth formula).** The terminal FCF of about 1,229 continues forever, growing at 3.4%.

```math
TV_{10} = \frac{FCF_{\text{terminal}}}{r - g} = \frac{1{,}229}{0.07 - 0.034} \approx 34{,}135
```

**3. Discount the terminal value to today.** The TV sits 10 years in the future.

```math
PV_{TV} = \frac{34{,}135}{(1.07)^{10}} \approx 17{,}352
```

**4. Enterprise value.**

```math
\text{EV} = PV_{\text{forecast}} + PV_{TV} = 4{,}328 + 17{,}352 \approx 21{,}681 \text{ (about USD 21.7 bn)}
```

**5. Equity value.** There is no debt, so equity value = EV.

**6. Share price.**

```math
\text{Share price} = \frac{21{,}681}{372} \approx 58.28 \text{ USD}
```

This explains Deutsche Bank's USD 60 target.

**7. Implied EBITDA multiple ≈ 10.8.** This is a spreadsheet ratio of a valuation figure to an EBITDA figure. The exact cell references were unclear in the recording.

#### (h) Scenario/sensitivity analysis on EBITDA margin (the critical assumption)

| Scenario | EBITDA margin path | Implied EBITDA multiple | Share price |
|---|---|---|---|
| Base case | about 9.4% → 9.8% → 9.3% | 10.8 | USD 58.28 |
| Worst case | falls by 0.5 percentage points every year | $\frac{8{,}121}{1{,}679} \approx 4.8$ | USD 16 |
| Jasraj's middle case | falls by 0.25 percentage points every year: 9.25, 9.0, 8.75, 8.5, 8.25, 8.0, 7.75, 7.5, 7.25, 7.0, then held at 7.0 | 8.6 (same as Walmart) | USD 36.13 |

- Jasraj guessed USD 30 for the worst case; the model gave USD 16.
- **Middle-case critique:** a multiple of 8.6 implies WFM earns no organic premium over a mass wholesaler. The instructor felt this may be too pessimistic, since an organic retailer should command some premium.
- Deutsche Bank itself later revised toward about USD 30–35.

#### (i) What actually happened

- Actual revenue growth (the red line in the chart) came in below expectations.
- ROC fell from 17% to 15%.
- EBITDA and operating margins fell to about 6–7%.
- WFM opened fewer stores than projected, so net assets grew less.
- The share price fell from USD 48.61 in April 2014 to about USD 38. It rebounded to about USD 54.55 in February 2015, which the market judged as overvalued. It then fell again and hovered at lower levels.
- WFM never recovered, and **Amazon acquired Whole Foods** when the price was depressed.
- The class's middle-case estimate (about USD 36) was close to reality; actual prices were slightly lower.

### 2.6 Closing lessons

- Everything depends on the profit-margin projection. That projection is always partly a guess, but it must be an **intelligent guess** informed by:
  - competitors' actions,
  - customer preferences,
  - whether the firm will stay valuable to customers, and
  - the intensity of competition.
- Practice independently: make projections, check them six months later, and learn from errors to build analyst intuition.
- Methods for projecting declining margins are not taught explicitly anywhere. Hints will come from strategy, marketing and finance courses, and students must combine them.

---

## 3. Exam / Assignment Flags

- **Possible group assignment:** an EBITDA-multiple analysis instead of (or alongside) **conjoint analysis**. Nihal preferred the EBITDA analysis. The group assignment has **not yet been finalized**.
- **Exercise (assigned to Nihal, possibly extended to the class):** do an EBITDA-multiple analysis of **Adani Enterprises**.
  - The share price is about ₹2,500.
  - Compute its EV/EBITDA, choose its competitors, compare multiples, and judge whether it is over-, under- or fairly valued.
  - The data is publicly available. It will be discussed next class.
- The Excel sheets (multiples and DCF) will be shared. Re-run the scenarios by changing the assumptions: margins, growth, and turnover ratios.
- **Concepts to know cold:**
  - EV, EBITDA margin, EV/EBITDA multiple and how to re-price a share from it
  - Leverage
  - Current asset and current liabilities turnover, and how to interpret them by industry
  - NWC, ROC vs cost of capital
  - NOPAT, FCF
  - Discount rate, NPV, the Gordon-growth terminal value $\frac{FCF}{r-g}$, discounting the TV by $(1+r)^{10}$
  - EV ÷ shares = share price
  - Scenario/sensitivity analysis on the margin assumption
- **Next (final) class** (the Monday about 10–12 days later, not the coming Monday):
  - The instructor will explain **all evaluation components**.
  - The instructor will summarize the remaining case studies.
  - **Read the remaining cases beforehand.** Extra classes will be scheduled if needed.

<!-- nav -->
← [Session 8 (2026-10-20)](DSM-106-8_2026-10-20_Jagannathan-Srinath.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
