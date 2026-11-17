---
course: DSM 107
date: 2026-10-15
start: 7:00pm
session: "16"
faculty: Deepak Sethia
---

<!-- nav -->
← [Session 15 (2026-10-14)](DSM-107-15_2026-10-14_Deepak-Sethia.md) · [All lectures](./) · [Session 17 (2026-10-27)](DSM-107-17_2026-10-27_Deepak-Sethia.md) →
<!-- /nav -->

# DSM-107 Managerial Economics, Session 16 (15 Oct 2026, Deepak Sethia)

## Money Multiplier, Interbank Markets, Bond Prices, Monetary Policy Tools (CRR, OMO, Repo), Bank Balance Sheets and Runs, SLR

---

## 1. Overview

This session continues from the previous class's derivation of the **money multiplier**. It opens with a quick recap and a numerical exercise ($rr = 10\%$, $cr = 30\%$, giving a multiplier of 3.25). It then explains why **banks are unique financial institutions**: they create money, while bond and equity markets only transfer savings. A ₹1,000 example with a 10% reserve requirement shows how withdrawals and transfers leave individual banks with reserve surpluses or deficits. That gap is why **interbank markets** exist and why banks borrow from or park money with the RBI.

The lecture then sets up the **inverse relationship between bond prices and interest rates** using a perpetual bond. It uses this to show that "RBI sells bonds", "money supply falls" and "interest rates rise" are one and the same event. The two RBI tools are compared:

- **CRR**, which changes the multiplier.
- **Open market operations / repo**, which change the monetary base.

The session also covers:

- Why RBI would expand or contract money (inflation vs. recession).
- US vs. India money-multiplier data, including **demonetization**.
- The **bank balance sheet**, leverage, "skin in the game", and the order of loss absorption.
- **Bank runs** as self-fulfilling prophecies, liquidity vs. solvency, the **lender of last resort**, and deposit insurance.
- **Government bonds** and the India-specific **Statutory Liquidity Ratio (SLR)**.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Money Supply and the Money Multiplier

**Money supply** means the things we use for transactions. There are two components:
- **Currency** ($C$), held by the public.
- **Deposits** ($D$), held in banks.

**How deposits are created:** banks keep part of each deposit as **reserves** ($R$) and lend out the rest.

**What the central bank creates:**
- Currency in people's wallets ($C$).
- Currency in bank vaults ($R$).

Together these form the **monetary base**. Three names are used for the same thing: **high-powered money = monetary base = M0** (narrow money):

$$B = C + R$$

**Broad money / money supply:**

$$M = C + D$$

**Money multiplier.** Divide each term of the numerator and denominator by $D$:

$$m = \frac{M}{B} = \frac{C + D}{C + R} = \frac{\frac{C}{D} + 1}{\frac{C}{D} + \frac{R}{D}} = \frac{cr + 1}{cr + rr}$$

where:
- $cr = \frac{C}{D}$ is the **currency–deposit ratio**.
- $rr = \frac{R}{D}$ is the **reserve–deposit ratio** (set via the CRR requirement).

Therefore:

$$M = m \times B$$

**Intuition: a smaller $rr$ means a larger multiplier.**
- Each unit of reserves supports more deposits.
- Banks keep a smaller fraction and lend out more.

**Intuition: a smaller $cr$ means a larger multiplier.**
- One unit of central-bank money held as currency supports only one unit of transactions money.
- One unit held as bank reserves supports many units of deposits.
- So the more central-bank money sits in wallets, the less is available as reserves, and the smaller the multiplier.

**What determines $cr$ (it varies):**
- How close ATMs are.
- How widely online/UPI payments are accepted. More digital payments mean lower $cr$.
- Festival and holiday seasons (Diwali, Christmas, travel). People hold more cash as a safety margin, so $cr$ rises.

**What determines $rr$:**
- Set by the central bank as the **CRR (Cash Reserve Ratio)**.
- In India it is currently about **4%**: for every ₹100 deposited, the bank keeps ₹4.

**Fractional reserve system:** banks hold only a fraction of deposits and lend the rest. If RBI creates ₹100 and it reaches you as income:
- You deposit it; the bank keeps about 4–5% and lends out about 95–96%.
- You can still transact using your ₹100 deposit.
- The borrower can also transact with the loan.
- So money multiplies.

#### Worked Example 1: Money multiplier

Given $rr = 0.10$ and $cr = 0.30$:

$$m = \frac{0.30 + 1}{0.30 + 0.10} = \frac{1.30}{0.40} = 3.25$$

#### Worked Example 2: Change in money supply from an open market purchase (US Fed)

- The Fed makes an open market purchase: it buys government bonds and issues **\$40 million** of new reserves/cash to banks.
- Banks lend out the surplus. Borrowers deposit it. Banks keep a fraction and lend again, and the cycle repeats.
- Using the multiplier from Example 1:

$$\Delta M = m \times \Delta B = 3.25 \times \$40\text{ million} = \$130\text{ million}$$

- The Fed created only \$40 million directly. The deposit and loan creation process raised the money supply by \$130 million.

---

### 2.2 Why Banks Are Unique Financial Institutions (Tata Motors example)

Tata Motors wants to build a car factory and has two ways to raise funds.

**Option 1: Capital markets (bonds or equity, e.g., via your mutual fund SIP).**
- Your savings go to Tata Motors, which buys steel and cement.
- You receive a piece of paper (a share or bond).
- You **cannot** buy toothpaste with that share or bond.
- Only Tata Motors can transact with the money.

**Option 2: Bank.**
- You deposit money and the bank lends it to Tata Motors.
- Tata Motors buys steel and cement.
- **You can also still spend your deposit**, for example on toothpaste.
- **Both parties can transact.**

**Conclusion:**
- All financial institutions mobilize savings toward investors.
- **Only banks create money**, because their liabilities (deposits) are themselves a means of payment.

---

### 2.3 Reserve Requirements, Withdrawals and Interbank Markets

**Setup:** the CRR is 10%. You deposit ₹1,000. The bank keeps ₹100 as reserves and lends ₹900.

**Banks hold the bare minimum reserves.**
- Reserves earn no interest; loans earn interest.
- So banks keep reserves at exactly the CRR, not 15–25%.

**Case A: You withdraw ₹1,000 cash from an ATM.**
- Deposits fall by ₹1,000 and reserves fall by ₹1,000.
- But the bank held only ₹100 in reserve against your deposit. It now has a **reserve deficit of ₹900**.
- The bank **cannot recall long-term loans**. For example, it cannot demand early repayment of a 10-year housing loan.

**Case B: You transfer ₹1,000 from SBI to HDFC (cheque or UPI).**
- Both banks hold accounts at the RBI or a clearing corporation, and reserves move between them.
- **SBI:**
  - Loses ₹1,000 of deposits and ₹1,000 of reserves.
  - It held only ₹100 in reserve, so it has a **₹900 deficit**.
- **HDFC:**
  - Gains ₹1,000 of deposits and ₹1,000 of reserves.
  - It needs only ₹100 in reserve, so it has a **₹900 surplus**.
- Both must maintain the 10% CRR. So SBI can **borrow from HDFC for a short duration**.
- This is temporary:
  - HDFC needs time to find new borrowers.
  - SBI needs time to be replenished by new deposits or loan repayments.

**Interbank market logic:**

| Situation | What happens |
|---|---|
| One bank in surplus, another in deficit | They lend to and borrow from each other (interbank market) |
| Entire banking system in deficit (e.g., cash withdrawn via ATM, so no bank gains reserves) | Banks borrow from the **RBI window** |
| Entire system in surplus (e.g., cash deposited from wallets) | Banks **park the surplus with RBI** and earn interest |

---

### 2.4 Bond Prices and Interest Rates Are Inversely Related

**Bond:** a piece of paper issued by a borrower that says "I will pay you back."
- **Perpetual bond:** pays a fixed amount forever.
- **Fixed-term bond (10, 20 or 30 years):** pays interest until maturity, then repays the principal.

**Pricing a perpetual bond** (the present value of a perpetuity):

$$P = \frac{C}{i}$$

where $C$ is the annual coupon and $i$ is the market interest rate.

#### Worked Example 3: Perpetual bond

- You lend ₹1,000 to the Government of India at **10%**. You receive ₹100 per year forever, since $\frac{100}{0.10} = 1000$.

**If the interest rate falls to 8%:**
- A new ₹1,000 bond now pays only ₹80 a year.
- Would you sell your ₹100/year bond for ₹1,000? **No**, because ₹1,000 now buys only ₹80 a year.
- What price matches your bond? Solve $0.08 \times X = 100$:

$$X = \frac{100}{0.08} = ₹1{,}250$$

- So your bond's price **rises to ₹1,250**.

**If the interest rate rises to 12%:**
- No one will pay ₹1,000 for your bond.

$$P = \frac{100}{0.12} \approx ₹833$$

- The lecturer said "around ₹850 or so"; the exact value is about ₹833.

**Gold analogy:**
- Gold bought 5 years ago and gold bought today sell at the same price today. Nobody discounts the old gold as "second-hand".
- Likewise, an old bond paying ₹100/year and a new bond paying ₹100/year are the same asset.
- **The original purchase price is irrelevant; only future payments matter.**

**Student question:** is this discounting future ₹100 payments to present value?
- **Yes, precisely.** It is the same present-value idea.

**Key takeaway:**

$$i \uparrow \;\Rightarrow\; P_{\text{bond}} \downarrow \qquad\qquad i \downarrow \;\Rightarrow\; P_{\text{bond}} \uparrow$$

---

### 2.5 Open Market Operations: Several Statements, One Event

**To reduce the money supply (contractionary).** The following all describe the **same thing**:
1. RBI reduces the money supply.
2. RBI raises interest rates.
3. RBI sells government bonds (in the lecturer's framing, a reverse repo, which absorbs liquidity).

**Mechanism:**
- RBI sells bonds it holds from the past, so **bond supply increases**.
- People buy the extra bonds only at **lower prices**, so the bond price falls.
- A lower bond price means a **higher yield / interest rate**. People demand, say, 9–10% instead of 8%.
- Buyers pay RBI with cash or reserves, so **money in circulation and bank reserves decline**.
- With less money in the system, lenders charge higher rates.

**To increase the money supply (expansionary).** Again, these are synonyms:
- RBI **buys** bonds.
- RBI issues currency.
- **Bond demand rises**, so bond prices rise.
- **Interest rates fall.**
- More money enters the system.

**Lecturer's point:** a paragraph saying "RBI is buying bonds. RBI is issuing currency. RBI is reducing interest rates. Bond prices have gone up." says **only one thing**.

**Implied bond-market graph:**
- Axes: price of bonds (y-axis) vs. quantity of bonds (x-axis).
- An RBI sale shifts bond supply **right**, so the equilibrium price falls and the yield rises.
- An RBI purchase shifts bond demand **right**, so the price rises and the yield falls.

---

### 2.6 Why Does RBI Change the Money Supply?

1. **Inflation control.**
   - More money chasing the same amount of goods creates inflationary pressure.
   - RBI **reduces** the money supply.
2. **Recession / demand deficiency.**
   - Either the government spends more, or investment must rise.
   - Investment rises when interest rates fall.
   - So RBI **increases** the money supply and lowers rates to incentivize firms to build factories, roads and so on.

**Principle:** *"The financial sector is not the master; it is the servant. The real economy is the master."*
- The purpose of monetary policy is to produce goods and services, use existing capacity, and create jobs.
- In inflation, RBI contracts money. In recession, RBI expands money.

---

### 2.7 RBI's Two Instruments: CRR vs. Open Market Operations / Repo

| Tool | What it changes | Mechanism |
|---|---|---|
| **CRR (Cash Reserve Ratio)** | The **money multiplier** (via $rr$) | A lower CRR means banks hold fewer reserves, so they create more loans and deposits. Loan supply rises and interest rates fall. |
| **Open market operations / repo and reverse repo** | The **monetary base** (high-powered money, $B$) | RBI buys or sells government bonds, which adds or removes reserves and cash. |

**Banks prefer repo-type operations to CRR changes.**
- CRR locks up their funds and earns **no interest**.

**Repo (expansionary).**
- RBI buys government bonds and gives cash to banks. For example, it buys a ₹100 bond and the bank gets ₹100.
- The bank does not need idle cash, which earns nothing, so it lends out the full ₹100.
- The public keeps part as currency and deposits the rest.
- Banks keep reserves per the CRR and lend the remainder, and the multiplier process continues.
- **Money supply rises and interest rates fall.**

**Reverse (RBI sells bonds).**
- Liquidity is withdrawn from the system and interest rates rise.

**Advice:** "Just read the definitions" of repo and reverse repo. You now understand the logic behind them.

**Student question (Aushi):** why is the dollar "powerful"?
- Deferred to a later session on international economics.
- Brief hint: "Basically, it is about trust."

---

### 2.8 When the Multiplier Doesn't Work: US vs. India Data

#### US graph (2000–2025)

**Axes:**
- x-axis: time.
- y-axis: index with 2000 = 100.

**Lines and their shape:**
- **Blue line (monetary base, M0):**
  - Rose about 9–10×.
  - **Two sharp jumps**: after the **Global Financial Crisis (2008)** and during **COVID (2020)**.
  - These jumps reflect the central bank pushing liquidity into the system ("printing notes").
- **Red line (money supply, M):**
  - Rose much more gradually.
  - Only a slight jump, far smaller than the base's.
- **Green line (money multiplier):**
  - Fell from **about 8 to about 4.2**.

**Data:**

| | Jan 2000 | Now | Growth |
|---|---|---|---|
| Monetary base | about \$600 billion | about \$5 trillion | about 8–9× |
| Money supply | \$4.6 trillion | about \$22 trillion | about 5× |

- The numerator ($M$) grew about 5×, while the denominator ($B$) grew about 9×.
- So the ratio $m = M/B$ **declined**.

**Why banks didn't lend the new reserves:**
1. The US pays **interest on reserves**, so banks are happy to hold them.
2. In a **recession or COVID environment**, many borrowers are defaulting. Banks avoid the risk of fresh loans.
   - They keep the money in vaults, deposit it with the central bank, or buy government bonds.

**Lesson:** the central bank can expand the base, but it **cannot force banks to lend**.

#### India graph

**Lines and their shape:**
- **Blue line (monetary base):** grew at a **slower** pace.
- **Red line (money supply):** grew **faster**.
- **Money multiplier:** **rose** over the period compared with the initial years.

**Visible feature: a dip in M0 and a jump in the multiplier around demonetization (Nov 2016).**
- People deposited their currency, so **currency in circulation fell**.
- Banks could not find borrowers fast enough for the sudden flood of deposits. They parked the excess with RBI via the **reverse repo window**.
- So the **monetary base fell**, effectively "destroyed".
- But $M = C + D$ **did not change**. Currency was merely converted into deposits.
- The red line continued its normal path. The denominator fell, so the **multiplier jumped**.
- This is a neat way to capture demonetization in money-multiplier terms.

---

### 2.9 Bank Balance Sheet, Leverage and "Skin in the Game"

| Assets | Liabilities and Equity |
|---|---|
| Reserves (cash kept per CRR, e.g., about 4%) | Deposits (must be repaid) |
| Loans (to be recovered in future) | Borrowings (debt via market instruments) |
| Securities (bonds etc.) | Owners' equity |

**Bad loans.**
- When loans go bad, assets shrink, so something on the liability side must shrink too.
- **Order of loss absorption:**
  1. **Equity holders** (bank owners) absorb losses first.
  2. **Debt holders** are next.
  3. **Depositors** are last.
- Rationale: the bank decides who gets loans, so its owners should suffer first if it lends badly.

**Banks are highly leveraged.**
- Small equity supports large loans made with depositors' money.

**Skin in the game.**
- Bankers should be the first to suffer losses.
- Depositors do not monitor lending day to day.
- Equity holders do monitor it, because share prices and profits depend on loan quality.

**Genuine borrowers can also default** because of economic shocks:
- A steel plant when steel prices collapse.
- Airlines with grounded planes under COVID restrictions, which must still pay interest.
- Hotels during lockdown.
- Home-loan borrowers who lost their jobs during COVID. The bank may even foreclose on the house.

---

### 2.10 Bank Runs, Liquidity vs. Solvency, Lender of Last Resort

**Bank run.**
- A rumor says a bank is in trouble.
- Each depositor rationally rushes to withdraw before others do.
- The bank's money is tied up in long-term loans (for example, 10-year housing loans), which it cannot recall.

**Self-fulfilling prophecy.**
- "Just because people think the bank has a trouble, the bank will have a trouble."
- Expectations become reality, like believing you feel unwell until you actually do.

**Forbearance example.**
- You lose your job but expect to be re-employed in 3–6 months.
- The bank gives you time to repay.
- Depositors withdrawing all at once would break this arrangement.

**Liquidity vs. solvency.**
- A bank can be **illiquid**: no immediate cash, because loans are long-term.
- It can still be **solvent**: its loans are good and their value covers deposits.

**Lender of last resort (RBI or any central bank).**
- RBI supervises banks' balance sheets and loan profiles monthly or quarterly.
- During a run it can lend to solvent banks.
- It can also publicly assure depositors that the books are sound. That assurance alone can stop the run.
- Banks should avoid needing this facility as far as possible.

**Deposit insurance in India.**
- Deposits are guaranteed up to **₹5 lakh** per bank account, as stated in lecture.
- Strictly, the guarantee is per depositor per bank.
- Purpose: to stop rumor-driven withdrawals.

---

### 2.11 Government Bonds

**Bond:** a promise that "I borrowed from you today; I will repay you tomorrow."

**The government is the biggest borrower.**
- Usually spending > taxes, i.e., a fiscal deficit.
- It borrows from the public by issuing bonds.

**Collateral.**
- Private loans need collateral (for example, a house for a housing loan).
- **The government's collateral is its word.**

**Link to monetary policy:**
- The government issues bonds to the public.
- RBI then buys or sells these bonds when it intervenes.

---

### 2.12 Statutory Liquidity Ratio (SLR): an India-Specific Concept

**Definition:** banks must hold a certain share of deposits as **government securities**, in addition to the CRR.

**Current figures:**
- CRR is about **4%** and SLR is about **18%**.
- Locked share of deposits:

$$4\% + 18\% = 22\%$$

- Loanable share:

$$100\% - 22\% = 78\%$$

**Purpose: a captive market for government securities.**
- When the government runs fiscal deficits and wants to borrow at rates below what the market would demand, a high SLR **forces banks to lend to the government**.
- Your deposits are channelled to the government via SLR.

**Why it was needed historically.**
- Private borrowing cost about 12–13%, while government bonds paid about 5–6%.
- Few would lend voluntarily at those rates.

**History in India.**
- SLR ranged from about **25% to 37–38%** before interest-rate liberalization.
- It is now about **18%**.

**Today it is not really binding.**
- Banks hold *more* government bonds than required, because government bond rates are now competitive.

**Not found in US textbooks.**
- SLR appears in Indian macro textbooks but not in US ones, including the course's prescribed text.
- US banks are not forced to hold government debt.
- "A Nobel laureate from outside may not be able to tell you what SLR is."

---

## 3. Exam, Assignment and Interview Pointers

**Interview prep.** Know **repo, reverse repo, CRR and SLR**. The lecturer assumed students had prepared these for interviews.
- "Just read the definitions." The logic was covered in class.

**Money multiplier calculation** (likely exam-style):
- Use $m = \frac{cr+1}{cr+rr}$ and $\Delta M = m \times \Delta B$.
- Practice: $rr = 10\%$, $cr = 30\%$ gives $m = 3.25$. A \$40m open market purchase then gives $\Delta M = \$130$m.

**Core relationship to master.** Bond prices and interest rates move inversely.
- "RBI sells bonds = money supply falls = interest rates rise = bond prices fall" are **one event**, not four.

**Know which tool affects which part of the formula:**
- CRR affects the **multiplier**.
- OMO / repo affects the **monetary base**.

**Interpret money-multiplier data:**
- The US multiplier fell from about 8 to 4.2. Reasons: interest on reserves and risk aversion.
- The Indian multiplier jumped at demonetization. Reason: currency converted into deposits while banks parked the excess at RBI.

**Next session(s):**
- How monetary policy transmits to the real economy.
- Later: international economics and why some currencies (e.g., the dollar) are "powerful".

<!-- nav -->
← [Session 15 (2026-10-14)](DSM-107-15_2026-10-14_Deepak-Sethia.md) · [All lectures](./) · [Session 17 (2026-10-27)](DSM-107-17_2026-10-27_Deepak-Sethia.md) →
<!-- /nav -->
