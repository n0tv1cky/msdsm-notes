# DSM-106 Business Research — Session 1
### Case: Basecamp (Project Management SaaS) — Pricing Research
**Date:** 2026-08-24 | **Instructor:** Jagannathan Srinath

---

## 1. Overview of the Session

This opening session of a 10-session Business Research course introduces how business functions rely on research methods to create, optimise and sustain value. The vehicle is a live case on **Basecamp**, a highly successful project-management software product (c. 2015–16: ~15 million users, ~7,000 new users per week, only ~50 employees). The company's founders want to know whether their three-tier subscription price is **too low**, whether a price increase would raise **customer lifetime value (CLV)** even at the cost of losing some customers, and what the optimal price is — all under strict constraints set by the founder (no price cuts, no feature changes, no reliance on historical data). The class works through two business research methods the company actually used: (a) a **field experiment / A/B test** in which a randomly selected group of website visitors was shown **double** the normal price, and (b) a **Van Westendorp Price Sensitivity Meter (PSM) survey**. Students interpret the actual conversion tables and PSM curves, compute *value per sign-up*, discover that doubling the price destroys value, and then learn why the survey results must **not** be taken at face value because of **anchoring bias** — which leads to a better, "relative price" (multiples-of-current-price, interquartile-range) way of presenting the same survey data. The session ends mid-analysis; that final graph (case p. 11) will be resumed next class.

---

## 2. Topics & Concepts, in Order Taught

### A. Course framing
- Business research as an enabler across business functions: creating value, optimising value, sustaining the firm, building value propositions for multiple stakeholders.
- 10 sessions; a range of business research methods will be covered.

### B. The Case Company — Basecamp (facts to memorise)
- **Product:** Basecamp — a project management software/platform (SaaS).
- **Decision point:** ~2015–2016.
- **Scale:** ~**15 million users**; adding ~**7,000 users per week**; only ~**50 employees**.
- **USP — deliberate simplicity:** they do *not* keep adding features. Only ~**5–6 core features**, e.g.:
  - ability to communicate with each other
  - scheduling visibility
  - idea generation / collaboration
- **Users are extremely diverse:** small businesses, mid-size firms, large companies, schools, hospitals, and **NASA project management teams**.

#### Current pricing structure (three tiers + free)
| Tier | Price | What you get | Limits |
|---|---|---|---|
| Free | $0 | Basic use | **Only 1 project** |
| Tier 1 | **$29 / month** | **Unlimited projects, unlimited users**, 100 GB storage | **Cannot** distinguish internal employees from external clients |
| Tier 2 | **$79 / month** | Unlimited projects/users, 100 GB storage | **Can** distinguish internal interface vs. client interface |
| Tier 3 (enterprise) | **$3,000 / year ( = $250 / month)** | Unlimited projects, **2 TB storage**, a **dedicated resource** for setup/support | — |

> *Note: early in the lecture the instructor once says "$59" for Tier 2, then consistently corrects to **$79**. Use $79. The doubled test price for Tier 2 is $149, confirming $79 as the base.*

- **Pricing is NOT indexed to number of users or number of projects.** A firm with 10,000 employees and 100 projects pays the same $79/month as a firm with 20 employees and 5 projects. Project count matters *only* for the free tier (1 project).

#### Marketing / go-to-market
- **Point of purchase = the website**; heavy **inbound traffic**; users download/sign up from the site.
- Early mover on **Google AdWords** advertising; also an early mover in the project-management software category itself.
- Price is low relative to competing project-management brands; product is easy to use.
- **Word of mouth** is a major driver.
- Both founders are **highly regarded, charismatic influencers** in the software community — successful blogs, inventors of important technologies, conference speakers. Their public commentary itself is a marketing driver.

#### Ownership & philosophy (constrains the research)
- Founders own virtually the entire company; **only one external investor: Jeff Bezos (Amazon), a minority investor**.
- Not publicly listed; **no near-term liquidity event** — no IPO, no stake sale to raise cash.
- **Profitability model, not a valuation model** — they value running a profitable business over valuation.
- **Product company, not a service/consulting company.** They refuse customisation — even if a large client offers **$100,000** for a customised build — because customising would turn them into a services/consulting firm.

### C. The Research Question
1. Is Basecamp **priced appropriately** / is it **under-priced**? Can it charge more?
2. If it charges more, it will lose some customers — but does **overall profit** still increase?
3. What is the **lifetime value (CLV)** a customer brings over their entire relationship with the firm, and what price **maximises** it?

### D. Founder's constraints on the research (important — these rule out several analyses)
1. **Price signals quality.** Reducing price would signal that quality has been compromised → **no price reduction is permitted**, under any circumstances.
2. **No change to product features.** The question is: *given the current feature set*, what is the optimum price / possible price increase?
3. **"Don't be afraid to be ambitious."** Think big — e.g., consider **not adding tiers but clubbing tiers** (e.g., merge the $29 and $79 tiers into one tier in which the internal/client distinction is a built-in standard feature).
4. (From a case exhibit) **Do not rely on historical data.** The company has ~10–12 years of data, but the founder says historical data anchors you to what has already happened; he wants radical, non-historically-anchored possibilities.

---

### E. Research Method 1 — The A/B Test (Field Experiment)

**Definition:** An A/B test is an **experiment** — specifically a **field experiment / live experiment**, not a laboratory experiment. Price point **A** vs price point **B**: how many consumers are willing to buy at each?

**Design as executed:**
- Run over **3 days** on the live website; ~**5,000 sign-ups** in that window.
- **Random assignment** of visitors to two groups.
- **Control group:** shown the real prices — $29 / $79 / $3,000.
- **Test group:** shown **double** the prices — **$59 / $149 / $6,000**.
- **Measurement window:** wait **one week** and see how many free sign-ups convert to a paid plan. (Baseline behaviour: users typically sign up free first; roughly 50% convert to paid about a week later, the rest continue free or churn.)
- **Ethics / debrief:** anyone who bought at the doubled price was **informed it was an experiment** and charged only the normal price.

**Why it can't be repeated:** the experiment generates **customer grievances** (one firm sees $29, another sees $59 at the same moment). Resolving these falls on a support team — and Basecamp has only 50 employees for 15 million users. Price experiments in particular are hard to repeat; by contrast, lab experiments on *product features* during new-product development can be repeated freely.

#### Results table (actual numbers)

| | **Control group** (normal price) | **Test group** (2× price) |
|---|---|---|
| Sign-ups (n) | **3,438** | **1,573** |
| Conversions to paid | **120** | **28** |
| Conversion rate | **3.49%** | **1.78%** |
| Average plan value | **$42.25** | **$71.14** |
| **Value per sign-up** | **$1.47** | **$1.27** |

*(3,438 + 1,573 ≈ 5,011 ≈ the ~5,000 sign-ups over 3 days.)*

#### Key formula
```
Value per sign-up = Conversion rate × Average plan value
```
Worked:
- Control: **$42.25 × 3.49% = $1.47**
- Test:    **$71.14 × 1.78% = $1.27**

#### Interpretation (as developed in class)
- **Average plan value** = the blended average across the three tiers actually purchased. In control, the 120 buyers split across $29 / $79 / $250(=$3,000 pa) → average $42.25. In test, the 28 buyers split across $59 / $149 / $500(=$6,000 pa) → average $71.14.
- **The benchmark test:** if you double all prices and the *mix* were unchanged, average plan value should at least **double from $42.25 to $84.50** (and ideally go higher, to cover lost volume). It only rose to **$71.14** — an increase of only ~**60–70%**, not 100%.
- **Why:** the test-group buyers skewed to the **cheapest tier** ($59). Very few bought $149; almost none bought the $500 enterprise plan. So the mix deteriorated *as well as* the volume.
- **Double penalty:** conversion fell (3.49% → 1.78%) *and* the average value failed to double. The two effects do **not** offset.
- **Conclusion:** value per sign-up **falls from $1.47 to $1.27**. **Doubling the price is not feasible — it erodes value and would cause losses.**

#### What the A/B test does *not* tell us
- We only learn that a **100% increase** fails. We have **no data** on 90%, 80%, 70%, 50%, 25%, or 10% increases. Any number in that range is **guesswork/speculation**.

#### Student proposals debated (and why they were constrained)
- **Jasraj:** raise the $29 "hero" plan by only **10–20%** (it's the main revenue product), and **double the enterprise tier** from $250/month to $500/month since few buy it and those buyers can afford it.
  - *Instructor's response:* practically, many (even large) companies do exactly this — supplement an experiment with a guess. But the 10–20% figure is **guesswork**; the true optimum could be 50% or 75%. Basecamp chose a more rigorous route: a survey.
- **Rahul:** run a **Pareto / ABC analysis** (as in supply chain) — classify products A/B/C by volume vs. value, cut price on the low-value/high-volume item to drive volume, hold the high-value item constant.
  - *Instructor's response:* Perfectly legitimate and widely practised — **but blocked by the founder's constraints**: (i) it requires a **price reduction** (forbidden — price signals quality), and (ii) it requires **historical data** (forbidden). You may debate the founder's rationality, but as an employee you must work within the stated constraints.

**Transition:** The company **supplements the experiment with a survey** — i.e., combining two business research methods (experiment + survey).

---

### F. Research Method 2 — The Van Westendorp Price Sensitivity Meter (PSM) Survey

**What it is:** A very popular marketing survey / business research method containing **only four questions**. Respondents answer using a **sliding meter** (here, a slider ranging from **$0 to $500**). Its advantage is that it is **very simple and cheap to conduct**.

**The four questions (as read out):**
1. **Too cheap:** "At what total monthly price would you consider Basecamp to be priced *so low* that you feel the quality can't be very good?"
2. **Cheap / bargain:** "At what total monthly price would you consider Basecamp to be *a bargain — a great buy for the money*?"
3. **Expensive:** "At what total monthly price would you say Basecamp is *starting to get expensive* — not out of the question, but you would have to give some thought to buying it?"
4. **Too expensive:** "At what total monthly price would you consider Basecamp to be *so expensive that you would not consider buying it*?"

So each respondent reports **four prices**: cheap(too cheap), inexpensive(bargain), expensive, very expensive.

#### The four cumulative curves and their intersections
| Curve (colour used in class) | Meaning | Shape |
|---|---|---|
| **Red** | Too cheap | Downward sloping (few say a high price is "too cheap") |
| **Orange** | Cheap / bargain | Downward sloping |
| **Blue** | Expensive | Upward sloping |
| **Green** | Too expensive | Upward sloping |

**Named intersection points (as stated in class):**
- **Red × Green → Optimal Price Point (OPP)**
- **Orange × Blue → Indifference Price Point (IPP)**
- **Orange × Green → Highest acceptable price point**
- The lower intersection gives the **lowest acceptable price** (below it, quality is deemed too poor and people won't buy).
- Together these define a **range of acceptable prices** within which the firm can move.

#### Survey results as presented
**For the $29 tier:**
- Lowest acceptable price ≈ **$20** (below $20, quality is deemed compromised)
- Optimal price point ≈ **$20**
- Highest price point ≈ **$30**
- ⇒ Implied maximum increase over the current $29 = **$1**. A "meaningless," non-substantial increase.

**For the $79 tier (interpreted by a student):**
- Optimal price ≈ **$45**
- Indifference / "would continue at" price ≈ **$52.50**
- "Too expensive" / highest ≈ **$70**
- ⇒ For a product currently sold at $79, respondents say **$70 is the most they'd pay**. Clearly implausible — those customers are already paying $79.

#### The critical methodological lesson: **ANCHORING BIAS**
- **Definition (as given):** Consumers are **anchored to the current price**. They do not want the price to rise, so they systematically report that the current price is *already* expensive or too expensive.
- Evidence in the data: at $29, essentially **nobody** falls on the red ("too cheap") line, and **very few** on the orange ("bargain") line. **No consumer ever reports that the price they currently pay is too low.**
- Instructor's teaching analogy: if the MSDSM programme office surveyed students on how much the programme fee could be increased, students would say the current fee is already too high. Respondents answer in their own interest.
- ⇒ **PSM survey results must be interpreted with caution and not taken at face value.** Taken naively, the survey says "no price increase is possible" — which contradicts the business question and is likely an artefact of bias.

---

### G. A Better Presentation: Relative Price (Multiples of Current Price) with Interquartile Ranges

To strip out the anchoring problem and to make the three tiers comparable, the same survey data is re-plotted as **multiples of the customer's own current price** (x-axis roughly **0x to ~2x**), shown as **box-and-whisker / interquartile-range** bars per question.

**Statistical vocabulary explicitly used:**
- Three **measures of central tendency**: **mean, median, mode**.
- The line inside each box is the **median** (here: the position of the middle respondent, robust and similar in spirit to the average).
- **Quartiles / interquartile range**: the box is divided into quartiles (0–50th, 50th–75th, 75th–100th as the instructor described them); whiskers reach the extremes.

**Readings given in class:**
- **"Too cheap" bar:** median sits about **⅓ of the way from 0x** (i.e., ~**0.33x**, about a **66% discount** off the current price). Meaning: the median customer says that only a **66% discount** would make the product look poor-quality. Some respondents in the **highest quartile** say even **80% of the current price** is "too cheap."
  - **Managerial implication:** Since even large discounts are needed before quality perception collapses — and since many respondents feel *any* reduction signals poor quality — this graph **supports the founder's position that price should not be cut.**
- **"Cheap / bargain" bar:** median around **0.7x** (≈ a **30% discount**) is seen as a bargain — **but** a large mass of respondents extends **up to 1.0x (the current price is already a bargain)**, and the **top quartile extends to ~1.8x — i.e., an 80% price increase would still be considered "cheap."**
  - **Managerial implication:** unlike the raw PSM curves, this presentation reveals **real headroom for a price increase** among a meaningful segment of customers.

**Why this presentation is superior:** it normalises across the $29 / $79 / $250 tiers and exposes the distribution (spread and tails) rather than a single anchored intersection point.

---

### H. Summary of the Analytical Logic (framework to reproduce)
1. Define the **business decision** (what price maximises CLV?) and the **constraints** imposed by management.
2. **Method 1 — Field experiment (A/B test):** random assignment, control vs test, one clean manipulation (2× price), measure conversion over a fixed window.
   - Compute **conversion rate**, **average plan value**, and **value per sign-up = conversion rate × average plan value**.
   - Test against the "should-have-doubled" benchmark ($42.25 → $84.50).
   - **Limitation:** cannot be repeated frequently; generates customer grievances; gives only a binary answer about one price point (100% increase fails) with no information on intermediate increases.
3. **Method 2 — Survey (Van Westendorp PSM):** 4 questions, cheap/bargain/expensive/too-expensive; derive OPP, IPP, and acceptable range.
   - **Limitation:** **anchoring bias** — self-interested respondents anchored to the current price; results not to be taken at face value.
4. **Re-express survey data in relative terms (multiples of current price) with medians and interquartile ranges** to reveal the distribution and identify a segment that will tolerate an increase.
5. **Triangulate**: use the experiment (rules out 2×) + the survey distribution (shows headroom up to ~1.8x for some) to set a defensible price move, subject to founder constraints (no cuts, no feature change, possible tier clubbing).

---

## 3. Flagged as Important for Exams / Assignments / Next Class

- **Read the Basecamp case before the next session.** The instructor explicitly urged the class to read it.
- **Focus on ALL the graphs in the case**, and **especially the final relative-price / interquartile-range graph, which is on PAGE 11 of the case.** This will be re-interpreted and completed at the start of next class.
- **Next class: next Friday** (after a break). The case will be discussed for **at least 15 more minutes** before moving to the next case/activity.
- Concepts explicitly named and worth knowing cold:
  - **A/B test / field experiment vs. laboratory experiment**; control group vs. test group; random assignment.
  - **Value per sign-up = conversion rate × average plan value** (and the actual numbers: 3.49%, 1.78%, $42.25, $71.14, $1.47, $1.27, 120/3,438, 28/1,573).
  - **Customer lifetime value (CLV)**.
  - **Van Westendorp Price Sensitivity Meter** — the four exact questions, the four curves, and the **Optimal Price Point (red × green)**, **Indifference Price Point (orange × blue)**, **highest price point (orange × green)**, lowest acceptable price.
  - **Anchoring bias** in survey research — why survey price data cannot be taken at face value.
  - **Measures of central tendency (mean, median, mode)**, **quartiles / interquartile range** and why the median is used here.
  - **Price signals quality** as a strategic constraint.