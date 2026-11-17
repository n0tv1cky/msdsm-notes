---
course: DSM 107
date: 2026-10-27
start: 7:00pm
session: "17"
faculty: Deepak Sethia
---

<!-- nav -->
← [Session 16 (2026-10-15)](DSM-107-16_2026-10-15_Deepak-Sethia.md) · [All lectures](./) · [Session 18 (2026-10-29)](DSM-107-18_2026-10-29_Deepak-Sethia.md) →
<!-- /nav -->

# DSM-107 Managerial Economics, Session 17 (27 Oct 2026, Deepak Sethia): Study Notes

> **Note on the transcript:** "SDFC" is HDFC Bank, "kjen cross" is the Keynesian cross, "RBA" is RBI, and "FIS" is FIIs/FPIs (foreign institutional/portfolio investors). Where a number looks garbled by speech-to-text, it is flagged with ⚠️.

---

## 1. Overview

The session begins by wrapping up monetary policy. It recaps the RBI's tools: CRR, open market operations and SLR. It then explains the **policy rate corridor** (repo and reverse repo) and how it bounds the **interbank call rate**. Next it shows why all of this matters: lower interest rates raise **investment demand**, which shifts aggregate demand up in the **Keynesian cross** and pulls the economy out of recession. A worked project-viability example illustrates this.

The lecture then turns to the **open economy**. It covers India's growing trade openness after 1991 and the national income identity with net exports. It defines **balance of payments, current account, trade balance and capital account**, along with the credit/debit rules. It shows why the **current account and capital account sum to zero** and derives the **open-economy saving–investment identity** $S - I = CA$. It discusses whether a current account deficit is "good or bad" (it depends). Finally, it introduces **exchange rates** (fixed vs. flexible) and the **supply and demand for dollars** in the Indian forex market. Exchange rates continue next session.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: How the Central Bank Controls Money Supply

**Cash Reserve Ratio (CRR):** the fraction of deposits banks must hold as reserves with the RBI.

**Open Market Operations (OMO):** the RBI buys or sells government securities.
- **To increase money supply:** the RBI *buys* government securities. Banks get cash, lend it out, and the money multiplier operates.
- **To decrease money supply:** the RBI *sells* government bonds. Banks pay cash to the RBI.
- Through these operations the central bank controls **high-powered money** (the monetary base).

**Statutory Liquidity Ratio (SLR):**
- SLR is **not really a money-supply tool**. It is about *allocation* of bank lending: to the government (via government bonds) or to the private sector.
- A high SLR forces banks to hold more government securities, i.e., to lend to the government.
- Why would a government want a high SLR? Because it wants to borrow cheaply. If it offers low interest rates, voluntary lenders won't lend, so banks are forced to.
- This is a form of **financial repression**. Reducing it was part of the **1991 reforms**.

**Historical data (table shown, since the 1960s):**

| Period | CRR | SLR |
|---|---|---|
| Peak (≈1989–1996) | ≈ 15% | ≈ 38–38.5% |
| Today | 3% | ≈ 18% |

- A dash in the table means no change during that period.
- SLR is lower today because government borrowing now offers **competitive interest rates**. Insurance companies, mutual funds and others voluntarily buy government bonds, so banks need not be forced.

### 2.2 The Policy Rate Corridor (Repo / Reverse Repo)

**Basis point:** $1 \text{ bp} = \frac{1}{100} \text{ of } 1\% = 0.01\%$

**Rates as of October 2026, as stated in class:**
- Policy rate $= 5.5\%$.
- **Repo rate** (rate at which the RBI *lends* to banks) $= 5.5\% + 25\text{ bp} = 5.75\%$.
- **Reverse repo rate** (rate at which the RBI *accepts deposits* from banks) $= 5.5\% - 25\text{ bp} = 5.25\%$.
- CRR $= 3\%$ and SLR $= 18\%$.

The reverse repo must be below the repo:
$$\text{Reverse repo} < \text{Repo}$$
Otherwise banks would borrow from the RBI and re-deposit at the RBI for a riskless profit.

**Why banks borrow or lend reserves: worked example (illustrative CRR = 4%)**
- All banks hold accounts with the RBI, which is why the RBI is the **"banker's bank"**. Interbank payments settle by transferring reserves at the RBI.
- A customer writes a cheque for ₹1,000 from HDFC to SBI.
- **HDFC:**
  - Deposits fall by ₹1,000 and reserves fall by ₹1,000.
  - It had held only $4\% \times 1000 = ₹40$ as required reserves against that deposit.
  - So its **reserve shortfall = ₹960**.
- **SBI:**
  - Deposits rise by ₹1,000 and reserves rise by ₹1,000.
  - It needs only ₹40 as reserves, so its **surplus = ₹960**.
- **Options:**
  - HDFC borrows ₹960 from the RBI and SBI deposits ₹960 with the RBI, or
  - the two banks lend to each other in the **interbank (call money) market**.

**The interbank rate is bounded by the corridor:**
- If SBI asks HDFC for 6%, HDFC refuses and borrows from the RBI at 5.75%.
- If HDFC offers SBI only 5%, SBI refuses and deposits with the RBI at 5.25%.
- Therefore:
$$\text{Reverse repo} \;\le\; \text{Weighted Average Call Rate (WACR)} \;\le\; \text{Repo}$$
- **Repo is the ceiling:** no bank borrows above it.
- **Reverse repo is the floor:** no bank lends below it.
- By setting repo and reverse repo, the RBI determines the interbank rate, and through it the rates banks charge everyone else.

**Graph described: the policy corridor over time**
- A time series of the WACR moving between a **red line (repo, the ceiling)** and a **green line (reverse repo, the floor)**.
- **Tight liquidity** (system in deficit, banks end up borrowing from the RBI): the WACR is near the **ceiling** (red line).
- **Surplus liquidity** (many banks have surpluses, few want to borrow): the WACR is near the **floor** (green line).
- Occasional spikes outside the band happen because **non-bank participants** (e.g., mutual funds) also operate in the money market.

### 2.3 Why the RBI Does All This: Monetary Policy and the Real Economy

**Recession remedies (recap):**
- **Fiscal:** raise government spending (new projects) or give transfer payments.
- **Monetary:** lower interest rates.

**Aggregate demand components:** $C + I + G + (X - M)$.

**Mechanism for lowering rates:**
1. The RBI buys bonds through OMO.
2. Money supply rises and banks have surplus liquidity.
3. Banks charge borrowers lower interest rates.
4. Investment (and interest-sensitive consumption, e.g., auto and housing loans) rises.

**Two-panel graph described:**
- **Bottom panel: investment demand.**
  - Vertical axis: interest rate $i$. Horizontal axis: investment $I$.
  - The **investment demand curve slopes downward**. Interest is a cost to firms, so a lower rate raises profitability and investment.
  - Moving from $i_1$ to $i_2$ (with $i_2 < i_1$) increases investment.
- **Top panel: Keynesian cross.**
  - Vertical axis: aggregate demand. Horizontal axis: output $Y$.
  - The **45° line** shows where $AD = Y$.
  - The AD line slopes upward (consumption rises with income) and has intercept $\bar{A}$.
  - Initial equilibrium is at $Y_1$, below **potential output $Y^*$**, so the economy is in recession.
  - Lower $i$ raises $I$, which raises the intercept $\bar{A}$. The AD line **shifts up** and the equilibrium moves right toward $Y^*$.
- **Link to earlier sessions:** in Sessions 4–5, $\bar{A}$ included $G$, so fiscal policy shifted the intercept. Here the intercept shifts via investment instead.
  - The multiplier process "starts from Mumbai (RBI), not Delhi (government)."
  - Firms deploy idle resources, newly employed workers consume, and the multiplier kicks in.

**Key concept: equilibrium vs. potential output**
- Macro equilibrium means the economy *produces as much as it can sell*.
- It does **not** mean full capacity. There can be unutilized capacity, which is the gap $Y^* - Y_1$.

**Student Q&A (savings and interest rates):**
- The main channel is **firm investment demand**, not households saving less.
- In recessions (2008, COVID), people keep money in banks even at near-zero rates because of **uncertainty** (precautionary saving).
- Firms won't produce if they fear they can't sell. Rate cuts raise profit pools and make projects viable.

**Worked example: project viability**
- Investment: ₹1,000 borrowed. The project yields ₹70 per year, so $IRR = 7\%$.
- At an interest rate of **8%**:
  - Interest $= 0.08 \times 1000 = ₹80$.
  - Net $= 70 - 80 = -₹10$, a loss, so the project is **not viable**.
- At an interest rate of **6%**:
  - Interest $= 0.06 \times 1000 = ₹60$.
  - Net $= 70 - 60 = +₹10$, so the project is **viable**.
- **Crux:** many unviable projects become viable at lower interest rates.

**Housing loan intuition:**
- The RBI "wants you to take a housing loan during a recession." This creates jobs in housing, and those workers then spend.
- Once the economy recovers, the RBI will **raise** rates. Why is covered later.
- All financial-market activity on rates ultimately targets the **real economy**, i.e., this graph.

### 2.4 International Linkages and India's Openness

**Economies are interlinked:** a US recession hurts Indian IT demand. IT workers then spend less, which hits housing, tourism and other sectors.

**India's exports and imports as a share of GDP:**
- Pre-1991: largely closed. ⚠️ The transcript says "66% of GDP each"; this is almost certainly **≈6% each**.
- After the 1991 liberalization: about 12% in the first decade.
- Now: about 20–22%.

**National income identity:**
$$Y = C + I + G + NX, \qquad NX = X - M$$
- **Exports** are not part of $C$, $I$ or $G$, but domestic producers earn from them, so they are added as $+X$.
- **Imports** are already included inside $C$ and $I$ (e.g., an imported iPad bought by a household or a firm). They are not domestic output, so they are subtracted as $-M$.

**Financial linkages:** countries are also linked through investment flows. Examples:
- FIIs/FPIs investing in or withdrawing from India.
- Indians buying US stocks (e.g., Tesla, or an upcoming Anthropic IPO) where rules permit.
- Japanese funding of metro and bullet-train projects.
- A Canadian pension fund investing in India.
- Capital seeks the best return.

**Convergence:**
- Trade makes goods prices converge: the high-price country imports from the low-price country.
- Capital flows similarly make interest rates converge.

### 2.5 Balance of Payments: Key Terms

These are four **distinct** terms, not synonyms:
1. **Balance of Payments (BoP):** the record of *all* transactions with the rest of the world (imports, exports, borrowing, lending).
2. **Current Account (CA):** transactions completed at once, with no future obligation. It includes:
   - **Trade balance:** exports minus imports of **goods and services**. For example, importing an iPad and paying immediately.
   - **Net factor income from abroad (NFI):**
     - Honoraria (e.g., a professor lecturing at Harvard): counts in the GDP of the country where the activity took place, and in the GNP of the country where the factor owner resides.
     - Dividends paid by Maruti to Suzuki's Japanese shareholders.
     - **Residence, not citizenship,** is what matters.
   - **Net unilateral transfers (NUT):** one-directional flows such as remittances (children abroad sending money to parents in Kerala, UP or Bihar), scholarships and grants.
   - Oil imports are also a current account entry.
3. **Trade balance:** a sub-part of the current account (goods plus services only).
4. **Capital Account (KA):** borrowing, lending and asset purchases, where one leg happens now and the counter-leg happens later. Examples:
   - NRI **FCNR deposits** in Indian banks: Indian borrowing that must be repaid.
   - Indians buying foreign (e.g., FAANG) stocks: a right to future dividends.
   - Foreigners buying Government of India bonds or shares of HDFC, Reliance or Jio.
   - FDI into India.

**Credit/debit rule:**
- **Receive** foreign exchange = **credit** (+).
- **Pay** foreign exchange = **debit** (−).

The two classifications are independent and form a **2×2 matrix**:

| | Credit (forex in) | Debit (forex out) |
|---|---|---|
| **Current** | exports, remittances received | imports (e.g., oil) |
| **Capital** | Microsoft stake in Jio; FDI into India; FCNR deposits | Tata acquiring Jaguar (Indian investment abroad) |

### 2.6 External Accounts Must Balance

- If you spend more than your income (a current account deficit), you must **borrow** or **sell existing assets**.
- Analogy: a retiree breaking FDs or selling shares or a house to fund spending.
- Excess debits on the current account are matched by credits on the capital account. Borrowing from abroad brings in dollars, which is a credit today; repayment later is a debit.
- A **capital account surplus** means forex is flowing in, either via borrowing or via foreigners buying Indian assets.
- Therefore the two accounts are equal in magnitude and opposite in sign:
$$CA + KA = 0 \quad\Longleftrightarrow\quad CA = -KA$$

### 2.7 Saving–Investment Identity in an Open Economy

**Household (private) saving.** Add NFI and NUT to the closed-economy version:
$$S_{pvt} = (Y + NFI + NUT - T + TR) - C$$
where $T$ is taxes and $TR$ is government transfers.

**Government saving:**
$$S_{gov} = T - TR - G$$

**National saving:**
$$S = S_{pvt} + S_{gov} = Y + NFI + NUT - C - G$$

**Substitute $Y = C + I + G + X - M$:** $C$, $G$, $T$ and $TR$ cancel, leaving
$$S = I + \underbrace{(X - M + NFI + NUT)}_{CA}$$

Hence:
$$S = I + CA \qquad\Longrightarrow\qquad S - I = CA$$

**Interpretation:** whatever is produced but not consumed is either **invested at home** or **sent abroad** (a current account surplus).

### 2.8 Is a Current Account Deficit Good or Bad?

**Answer: it depends on how the borrowed funds are *used*.**
- From $S - I = CA$: if $I > S$, then $CA < 0$.
- A deficit driven by **rising investment** is less worrying.
- A deficit driven by **falling savings** is more worrying.

**Example: Japanese-funded metro or high-speed rail**
- **Today:** India borrows (capital account surplus) and imports (current account deficit).
- **Later:** the project generates revenue, India exports (current account surplus) and repays (capital account deficit).

**Rule:** borrowing is fine if the returns exceed the borrowing cost. **Do not attach "good" or "bad" to the word "deficit."**

### 2.9 Exchange Rates

**Basic example:**
- An Amul chocolate costs ₹50–60 and is paid in rupees directly.
- A Hershey's chocolate (US-made) must be paid for in dollars.
- With an exchange rate of ₹50/$, you convert **₹75 into \$1.50** to buy it.
- ⚠️ The transcript says "\$15"; the arithmetic ($1.50 \times 50 = 75$) shows the price is **\$1.50**.
- The lecturer uses ₹50/$ for simplicity instead of the actual ≈₹96. He will switch to ₹100 once the rupee crosses 100, which he expects; reasons come next session.

**Two regimes**, with hybrids in between:
- **Fixed exchange rate:**
  - The central bank buys or sells currency in unlimited amounts at the fixed price (e.g., ₹50/$).
  - Nobody will pay more than 50 elsewhere, and nobody can sell above 50.
  - The central bank absorbs any excess supply and meets any excess demand.
- **Flexible exchange rate:** the rate is set by supply and demand in the forex market (continued next session).

**Forex market graph (looks like a micro supply/demand graph):**
- Horizontal axis: quantity of **dollars**. Vertical axis: **₹ per \$** (the price of a dollar).
- **Direction convention:**
  - **Down** the axis is rupee **appreciation** (e.g., 50 → 40, or 90 → 80).
  - **Up** the axis is **depreciation** (e.g., 90 → 100, or 50 → 60).

**Supply of dollars (exporters, e.g., Infosys, TCS, Wipro): upward-sloping**
- These firms earn in dollars but pay salaries in rupees.
- When the rupee depreciates (50 → 60 → 70), they earn more rupees per dollar, so they supply more dollars.

**Demand for dollars (importers): downward-sloping**
- Example: a \$1,000 iPhone costs ₹50,000 at ₹50/$ (ignoring tariffs).
- If the rupee appreciates to ₹40/$, it costs ₹40,000. Imports become cheaper, so people demand more dollars.

(Vostro/nostro accounts were mentioned but explicitly not covered.)

---

## 3. Exam / Assignment Pointers

No explicit exam announcement was made, but the lecturer emphasized:
- **BoP, current account, trade balance and capital account are four different concepts.** Don't treat them as synonyms.
- **Credit vs. debit is separate from current vs. capital** (the 2×2 matrix). Expect classification questions like the in-class examples (FDI into India, Tata–Jaguar, Microsoft–Jio, FCNR deposits, remittances, oil imports).
- **$CA + KA = 0$** and **$S - I = CA$**: know the derivation.
- **"Don't put good or bad with deficit."** Judge a current account deficit by whether it comes from rising investment or falling saving, and by how the funds are used.
- **The interbank rate lies within the repo/reverse-repo corridor.** Know the reasoning and the tight vs. surplus liquidity interpretation.
- **Monetary transmission:** rate cut → investment up → AD intercept up → output toward $Y^*$. Equilibrium is not the same as potential output.
- **Next session:** flexible exchange rates in detail, and why the rupee will likely cross ₹100/$.

<!-- nav -->
← [Session 16 (2026-10-15)](DSM-107-16_2026-10-15_Deepak-Sethia.md) · [All lectures](./) · [Session 18 (2026-10-29)](DSM-107-18_2026-10-29_Deepak-Sethia.md) →
<!-- /nav -->
