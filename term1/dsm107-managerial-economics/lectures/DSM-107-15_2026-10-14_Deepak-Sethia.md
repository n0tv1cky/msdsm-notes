---
course: DSM 107
date: 2026-10-14
start: 7:00pm
session: "15"
faculty: Deepak Sethia
---

<!-- nav -->
← [Session 14 (2026-10-13)](DSM-107-14_2026-10-13_Deepak-Sethia.md) · [All lectures](./) · [Session 16 (2026-10-15)](DSM-107-16_2026-10-15_Deepak-Sethia.md) →
<!-- /nav -->

# DSM-107 Managerial Economics: Session 15 Study Notes
**Instructor:** Deepak Sethia | **Date:** 14 Oct 2026

---

## 1. Overview

The session finishes the **Keynesian income–expenditure (multiplier) model** and then begins **money and the monetary system**.

The first half covers several fiscal-policy ideas:
- How an increase in government spending moves an economy from a below-full-employment equilibrium toward potential output.
- How proportional income taxes reduce the spending multiplier. The worked example gives a multiplier of 2.5 with taxes, compared with 5 without.
- Why transfer and tax multipliers are smaller than the direct-spending multiplier.
- The debate over direct spending versus tax cuts and transfers, using the 2008 crisis.
- How the budget surplus depends on income.
- Procyclical versus countercyclical fiscal policy, illustrated with COVID-era borrowing.

The second half introduces money:
- Its functions.
- Commodity money versus fiat money.
- The real-resource cost of commodity money, illustrated with Mughal silver.
- Inflation from over-printing, illustrated with Zimbabwe.
- The idea that commercial banks also create money under fractional-reserve banking.
- The derivation of the **money multiplier** $\frac{1+cu}{cu+re}$, with a worked example where 1,000 of base money becomes a money supply of 5,000.

---

## 2. Topics and Concepts (in order taught)

### Part A: Keynesian Multiplier Model (continued)

#### A1. Recap: equilibrium below potential output
- **Potential output** is the output reached when all available labour and capital are used and factories work at normal capacity.
- Firms may produce **below capacity** because they fear they cannot sell more.
- At equilibrium, everything produced is sold:
  - If firms produce more than the equilibrium level, there is **unsold inventory**.
  - If they produce less, **inventories are depleted**.
- So the economy can be *in equilibrium* yet *below full employment*, which is a recession.

#### A2. Aggregate demand components
- Consumption has an autonomous part and a part that depends on **post-tax (disposable) income**.
- Investment, government transfers and government expenditure complete aggregate demand:

```math
AD = \bar{C} + c\left[(1-t)Y + \overline{TR}\right] + \bar{I} + \bar{G}
```

- Here:
  - $c$ is the marginal propensity to consume (MPC).
  - $t$ is the proportional income tax rate.
  - $TR$ is government transfers.
  - $G$ is government purchases.

#### A3. Keynesian cross graph (described verbally)
- **Axes:** output/income $Y$ on the horizontal axis and aggregate demand on the vertical axis.
- **The $45^\circ$ line** is the set of points where output equals demand. Any height on the line equals the corresponding horizontal base.
- **Starting point:** the economy is at **$E_1$**, where the AD line crosses the $45^\circ$ line, to the left of full-employment output.
- **Policy shock:** the government builds a **new highway**, so $G$ rises and the **AD line shifts up** in parallel.
- **Adjustment process:**
  1. At the old output level, demand now exceeds output. The AD height is above the $45^\circ$ line.
  2. Inventories are depleted, so firms raise production.
  3. Firms hire unemployed workers, who receive wages and consume more. This is induced demand.
  4. Output rises until the economy reaches the new intersection of the higher AD line with the $45^\circ$ line, closer to potential output.
- **No overshooting:** beyond the new intersection, output would exceed demand, so the economy does not move past it.
- **Other ways to raise AD:**
  - More government spending.
  - Incentives for business spending, such as **tax credits for investors**.
  - Improved investment sentiment, where firms see a "rosy picture" and invest more.

#### A4. Government spending multiplier
- If government spending rises by $\Delta G$:

```math
\Delta Y = \alpha_G \,\Delta G
```

- $\alpha_G$ is the **spending multiplier** introduced in the previous session.
- **Intuition:** one unit of spending generates more than one unit of output.
  - Workers produce the extra demand in the first round.
  - Their wages create **induced demand** in the second, third and later rounds.
- With proportional income taxes:

```math
\alpha_G = \frac{1}{1 - c(1-t)}
```

**Worked example (class answer: 2.5).** The parameters below are implied by the class discussion: $c = 0.8$ and $t = 0.25$.
- With taxes:

```math
\alpha_G = \frac{1}{1 - 0.8(1-0.25)} = \frac{1}{1-0.6} = \frac{1}{0.4} = 2.5
```
- With no taxes:

```math
\frac{1}{1-c} = \frac{1}{1-0.8} = 5
```
- **Takeaway:** a 25% tax cuts the multiplier from 5 to 2.5.

**Proportional taxes as an automatic stabiliser:**
- When income rises, spending does not rise proportionately, so output fluctuations are smoothed.
- In a recession this dampening is unhelpful. Governments may therefore **cut the tax rate** to raise the multiplier.

#### A5. Transfer multiplier
- Suppose transfers rise by $\Delta TR$.
- Households receive $\Delta TR$ but save the fraction $(1-c)$, so first-round spending is only $c\ \Delta TR$.
- The spending rounds are:

```math
c\,\Delta TR,\quad c^2\,\Delta TR,\quad c^3\,\Delta TR,\ \dots
```

- Hence:

```math
\Delta Y = c\,\alpha_G\,\Delta TR
```

- **Transfer multiplier $<$ direct spending multiplier.**
  - Direct spending creates first-round demand itself, such as demand for cement and steel, before wages are spent.
  - Transfers skip that first round of demand.

#### A6. Tax changes
- **Lump-sum tax change:** the effect is MPC times the spending multiplier, with the opposite sign:

```math
\Delta Y = -c\,\alpha_G\,\Delta T
```

- A tax rise reduces output and a tax cut raises it.
- **Raising the marginal (proportional) tax rate $t$ has two effects:**
  1. AD falls because disposable income falls.
  2. The multiplier itself becomes smaller.

#### A7. Direct spending vs. tax cuts and transfers (2008 financial crisis)
**Case for direct spending (Obama's argument):**
- It has a larger multiplier, because tax cuts or transfers are partly saved.
- The government acts as the **"buyer/demander of last resort"** in a recession.

**Case for transfers and incentives:**
- Direct spending is subject to **political-economy distortions**, such as "why not a project in my constituency?" The result can be useless roads.
- Government may spend on dying regions or old technologies. This addresses short-term unemployment but creates no lasting future benefit.
- Households and firms who receive transfers or incentives decide based on what they actually need.

#### A8. Budget surplus

```math
BS = tY - G - TR
```

- $tY$ is tax revenue.
- $G$ and $TR$ are the two types of government spending.

**Graph (described verbally):**
- **Axes:** income $Y$ on the horizontal axis and budget surplus on the vertical axis.
- **Intercept:** at $Y=0$, $BS = -(G+TR)$, which is negative.
- **Shape:** an upward-sloping straight line with slope $t$.

**Implication:** the budget surplus or fiscal deficit is **not independent of the business cycle**. Deficits widen automatically in bad times.

#### A9. Procyclical vs. countercyclical fiscal policy
**Graph (described verbally):**
- **Axes:** time on the horizontal axis and output on the vertical axis.
- **Blue curve:** the normal business cycle.
- **Red curve:** procyclical policy. It has larger swings than blue, with higher peaks and deeper troughs.
- **Green curve:** countercyclical policy. It is flatter than blue, which smooths the cycle.

**Procyclical policy (most undesirable):**
- In good times, higher tax revenue leads the government to spend more, which adds further to AD.
- In bad times, lower revenue leads the government to fire workers and cut spending. Government employees then spend less, so the recession worsens.
- This mirrors household logic ("earn less, spend less"), which is the wrong rule for governments.

**Countercyclical policy:**
- In a downturn, the government should **borrow and spend**.
- In a boom, the government should **cut spending and "tighten the belt"**, letting the private sector spend.
- This is the reverse of household logic.

**COVID example:**
- Tax revenue fell because of the lockdown.
- Spending ballooned, covering existing salaries for teachers, doctors and others, plus new health measures.
- Heavy borrowing followed, and rating agencies worried about repayment.
- Economists argue pandemics are not the time to worry about deficits.
- India's DEA (Department of Economic Affairs) Secretary explained to rating agencies why India's rating should not be cut for this borrowing.

---

### Part B: Money and the Monetary System

#### B1. What is money?
**Demonetised note example:**
- A discontinued note is not legal tender.
- If people still accepted it in practice, it would still function as money.

**Definition:**
- Money is whatever people use as a **medium of exchange**.
- Historical examples include gold, silver coins, cowries and seashells.
- Its value rests on the **belief that others will accept it**. In India, this belief comes from trust in the government.

**Double coincidence of wants:**
- Under barter, the professor needing a haircut must find a barber who wants an economics lecture.
- With money, you sell food to anyone and buy clothes from anyone.

#### B2. Functions of money
1. **Medium of exchange.** Money solves the double coincidence of wants.
2. **Store of value.** You can sell today and buy later.
   - This store is imperfect under inflation: 100 rupees buys less a year from now.
3. **Unit of account.** Prices are quoted in money.
4. **Standard of deferred payment.** Debts are denominated in money.

**Money as an asset:**
- Money is the **most liquid asset**.
- Houses, stocks and bonds must first be converted into money before you can buy things.

#### B3. Commodity money vs. fiat money
**Commodity money (gold, silver):**
- Has **intrinsic value**, so it retains value even without government backing.
- **Debasement example:**
  - Under a gold standard, 1 g of gold = 100 rupees.
  - The government declares 1 g of gold = 200 rupees.
  - Prices immediately rise: sellers ask 200 for goods previously sold at 100.
- This is like "shrinkflation", where a noodle packet keeps its 10-rupee price but shrinks in size.

**Fiat money:**
- Has **no intrinsic value**. The scrap value of a 2,000-rupee note is negligible.
- It is valuable only because of authorisation and trust.
- The government can create it "out of thin air".
- The "I promise to pay the bearer" clause just means the RBI will give you an equivalent note, not gold.
- **Who signs Indian notes:**
  - The ₹1 note is signed by the **Finance Secretary**. Authority rests with the Government of India in Delhi.
  - Other notes are signed by the **RBI Governor**. Printing has been delegated to the RBI in Mumbai.

**Problems with historical commodities:**
- Low-value items such as stones and shells require huge volumes to buy things.
- Gold makes **small denominations** hard.

**Student point on crypto:**
- Crypto has no backing asset, so it is like fiat money but without government legal-tender status.

#### B4. Why fiat money is better: the real-resource cost of commodity money
- India lacked good gold and silver mines.
- To obtain silver, India exported textiles and spices, then minted the imported silver into coins.
- **Mughal example:**
  - The Mughal Empire depended on silver currency.
  - Controlling the trade route through Mewar (transcribed as "Mayard"), running from Agra to the coast, meant controlling the currency supply.
  - If you do not control the trade route, you do not control your currency.
- **Modern analogy:**
  - If Infosys or TCS service exports were paid in silver just to run domestic transactions, those export earnings could not be used to import oil.
- With fiat money printed by the RBI, **no real resources are locked up in coins**. Export earnings are freed to import other goods.

#### B5. Danger of fiat money: over-printing and inflation
- A government does not need to declare notes worthless. It can simply **print more**, so more notes chase the same goods.
- **Zimbabwe example:**
  - People hold \$1 billion in notes.
  - The government prints \$1 trillion.
  - Existing holdings now buy about $\frac{1}{1000}$ of what they bought before.
- Printing money therefore amounts to **stealing from existing note-holders**.

#### B6. Measures of money
- Transactions use **cash and bank deposits**.
  - UPI transfers deposits from your bank account to the seller's account.
- **$M_0$** has three equivalent names: **high-powered money / monetary base / base money / narrow money**.
  - It is the cash created by the RBI.
- **$M_3$** is **broad money / money stock**: the money used for transactions, namely currency in circulation plus deposits.
  - This includes demand and time deposits. Cash is more liquid than time (fixed) deposits.
- **The RBI creates only cash.**
  - **Deposits are created by commercial banks** such as SBI, HDFC, Canara Bank and PNB.

#### B7. 100% reserve vs. fractional reserve banking
- **100% reserve:**
  - You deposit 1,000 and the bank keeps all 1,000 as reserves.
  - **Reserves** are currency held by banks.
- **Fractional reserve:**
  - Banks know not all depositors withdraw at once.
  - They keep a buffer and lend out the rest.
  - Instructor's illustration: 100 people deposit 1 rupee each; the bank keeps 20 and lends out 80.

#### B8. Worked example: deposit creation ($re = 20\text{%}$, no cash held by public)
**First round:**
- The central bank (RBI or Fed) creates 1,000, which is deposited in a bank.
- The bank keeps 200 as reserves and lends 800.
- Money supply after this round:

```math
\underbrace{1000}_{\text{deposits}} + \underbrace{800}_{\text{currency with public}} = 1800
```

- The 200 in the vault is **not** money supply, because it cannot buy toothpaste.
- The depositor can still spend the 1,000 via UPI or cheque. The borrower spends the 800.

**Second round:**
- The 800 is re-deposited.
- The bank keeps 160 and lends 640.

**Continuing rounds:**
- Deposits form an infinite geometric progression with common ratio $(1-re) = 0.8$:

```math
1000 + 1000(0.8) + 1000(0.8)^2 + \dots = \frac{1000}{1-(1-re)} = \frac{1000}{re} = \frac{1000}{0.2} = 5000
```

**Result:**
- Total money supply is **5,000**, so the **money multiplier is 5** in this case.
- In general:

```math
\text{Money supply} = \text{Monetary base} \times \text{Money multiplier}
```

**Key point:** private banks also create money, not just the RBI.

**Clarifications from Q&A:**
- **The "certificate":** your deposit is recorded in your passbook or online account. That record is what lets you transact via UPI, even though the bank has lent the cash out.
- **"Purchasing power":**
  - The instructor deliberately refused to say society gains \$5,000 of "purchasing power".
  - The correct phrasing is **"money available for transactions"**.

#### B9. General money multiplier (with currency holding)
**Definitions:**
- $CU$ is currency in circulation, held in the public's wallets.
- $D$ is deposits.
- $RE$ is bank reserves held in bank vaults. In India, the required part is set through the **CRR**.

**Money stock and base:**

```math
M = CU + D, \qquad H = CU + RE
```

**Dividing numerator and denominator by $D$:**

```math
mm = \frac{M}{H} = \frac{CU + D}{CU + RE} = \frac{\frac{CU}{D} + 1}{\frac{CU}{D} + \frac{RE}{D}} = \frac{cu + 1}{cu + re}
```

- Here:
  - $cu = \frac{CU}{D}$ is the **currency–deposit ratio**.
  - $re = \frac{RE}{D}$ is the **reserve–deposit ratio**, which corresponds to India's **CRR (Cash Reserve Ratio)**.

**Comparative statics:**

| Ratio change | Effect on $mm$ | Reason |
|---|---|---|
| Lower $re$ | Larger $mm$ | At 20%, each 1 rupee of reserves supports 5 of deposits. At 10%, it supports 10. |
| Higher $cu$ | Smaller $mm$ | This holds because $re < 1$. |

**Why higher $cu$ shrinks the multiplier:**
- One unit of high-powered money held as currency supports exactly one unit of transaction money.
- One unit held as bank reserves supports several units of deposits.
- So when more base money sits in wallets, less is available as reserves, and fewer deposits can be supported.

**Caveat from the instructor (Q&A):**
- This does **not** mean we "should" use UPI to get more money.
- **More money does not create more real goods.** Output depends on factories, steel and cement.
- With the same real output, more money just means higher prices, so each unit of money buys less.
- **Printing money fuels inflation**, as "helicopter money" would show.

**Q&A: what gives fiat money value without gold?**
- **Government discipline.**
- People hold US dollars because they trust the US not to over-print.
- They avoid Zimbabwean, Sri Lankan or Pakistani notes because those are printed excessively.
- The US left the gold link so it could print more.
- Doubts about current dollar stability were deferred to the exchange-rate sessions.

#### B10. Determinants of the ratios
**Currency–deposit ratio ($cu$):**
- It is **lower** when ATMs are nearby and UPI is widely accepted.
- It is **higher** when ATMs are far away or UPI is not accepted. Distance raises **shoe-leather costs**, so people hold more cash.
- **Seasonality:** during festivals such as Diwali, people hold more cash for gifting and transactions, so $cu$ rises.

**Reserve ratio ($re$):**
- It is set mainly by the central bank: the RBI sets the CRR.
- Banks may voluntarily hold **excess reserves** for safety against withdrawals.

---

## 3. Exam and Assignment Notes

No explicit exam or assignment announcements were made. Points the instructor stressed or tested in class:

**Fiscal policy:**
- **Be able to compute the spending multiplier with taxes.** The in-class quiz used $c = 0.8$ and $t = 0.25$, giving $\alpha_G = 2.5$ versus 5 without taxes.
- **Know why transfer and lump-sum-tax multipliers equal $c\ \alpha_G$** and are smaller than the direct-spending multiplier.
- **Know the two effects of raising the marginal tax rate:** lower AD and a smaller multiplier.
- **Be able to explain procyclical versus countercyclical policy**, including why a government should not behave like a household.

**Money:**
- **Be able to derive the money multiplier** $\frac{1+cu}{cu+re}$.
- **Be able to work the GP deposit-creation example:** with $re = 20\text{%}$, the base of 1,000 becomes a money supply of 5,000.
- **Know the comparative statics for $re$ and $cu$**, especially the intuition for why higher $cu$ lowers the multiplier.
- **Conceptual trap:** money is not real wealth, and more money does not mean more goods. Use the phrase "money available for transactions".

**Next session (tomorrow):**
- The monetary system continues.
- The bank-run question, "what if most customers want to withdraw?", will be taken up.
- Exchange rates and international issues come in later sessions.

<!-- nav -->
← [Session 14 (2026-10-13)](DSM-107-14_2026-10-13_Deepak-Sethia.md) · [All lectures](./) · [Session 16 (2026-10-15)](DSM-107-16_2026-10-15_Deepak-Sethia.md) →
<!-- /nav -->
