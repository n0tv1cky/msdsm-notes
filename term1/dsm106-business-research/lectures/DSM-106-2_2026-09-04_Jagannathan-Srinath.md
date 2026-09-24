# DSM-106 Business Research — Session Notes
**File:** DSM-106-2_2026-09-04_Jagannathan-Srinath
**Topics:** Basecamp pricing case (conclusion) — interpreting Van Westendorp price-sensitivity data via interquartile ranges; A/B testing vs. survey research; introduction to the second case (30-manager, 7-item survey dataset)

---

## 1. Overview

This session completes the **Basecamp (BC3) pricing case study** that was begun in the previous class. The class recaps the company's three-tier price structure ($29 / $79 / $250 per month), the **A/B test** which showed that doubling prices destroys revenue, and the follow-up **Van Westendorp Price Sensitivity Meter (PSM) survey**. Because survey respondents suffer from **anchoring bias** (nobody voluntarily tells a researcher they'd pay more), the PSM results cannot be read off conventional Van Westendorp intersection graphs; instead the class interprets **interquartile-range (box-plot style) distributions** of the four PSM curves (too cheap, cheap, expensive, too expensive) expressed as multiples of the current price (1x). Students volunteer readings of each curve's median, Q3 and whisker, and then propose pricing decisions; the instructor then reveals what Basecamp actually did (killed tiers 1 and 3, raised tier 2 from $79 to $99, added a 10% annual discount) and works through a **100-customer revenue scenario** showing an ~20–25% revenue gain, plus a counter-scenario at 2x pricing showing a revenue loss. The methodological takeaway is **method triangulation**: experiments tell you what *won't* work, surveys narrow the range, and scenario analysis fills the remaining gap — evidence-based decision-making still contains guesswork. The last 15 minutes introduces the **next case**: a dataset of 30 middle managers rated 1–10 on 7 survey items (I1–I7), with the assignment of grouping the items into constructs (leading into factor analysis next session).

---

## 2. Topics & Concepts, in order taught

### A. Recap — the Basecamp case setup
- **Company/product:** Basecamp, a **project management software platform** (BC3).
- **Scale facts used in the argument:** more than **1 million customers**; adding roughly **5,000–6,000 new customers per week**; therefore a **high-volume business** → management philosophy is **no customization of the product for individual clients**.
- **Current three-tier price structure:**

| Tier | Price | Features |
|---|---|---|
| Tier 1 | **$29/month** | Unlimited projects, unlimited users; **cannot distinguish** between own company and the client for whom the project is delivered |
| Tier 2 | **$79/month** | Unlimited projects, unlimited users; **can distinguish** company vs. client organisation |
| Tier 3 (Enterprise) | **$250/month = $3,000/year** (paid up front) | Unlimited users/projects, **1 TB storage**, **one dedicated employee** for setup and issue resolution |

- **Billing at the time:** monthly or annual subscription, but **no discount for annual payment** (except Tier 3, which must be bought as $3,000 up front).

### B. Research method 1 — the A/B test (experiment)
- **Definition/procedure:** two different prices are offered **as if they were real prices**; the consumer **does not know** it is a simulation/experiment; the consumer makes a genuine purchase decision; the researcher compares **conversion ratios** across the two arms.
- **The test run:** double all prices → $29 → **$59**, $79 → **$150**, $250/month → **$500/month** ($3,000 → **$6,000**).
- **Result:** at 2x, conversion falls so far that **overall revenue declines**. Conclusion: **2x is out of the question; any increase must be less than 2x.**
- **Limitation (why it wasn't repeated):**
  - It is a **real-time experiment** → customers compare notes, raise grievances ("another customer is paying half what you're charging me").
  - The firm must later explain/refund, which requires heavy **customer support capacity** that Basecamp does not have.
  - Even firms with support find **repeated A/B tests** hard to implement.
  - **Crucially, the A/B test gives no information about the intermediate range** — it says nothing about whether +80% or +90% would have worked.

### C. Research method 2 — Van Westendorp Price Sensitivity Meter survey
- A **short, four-question price survey** → cheap and easy to run compared with an experiment.
- Four price constructs (colour-coded in the class graphs):
  - **Too cheap (red)** — so cheap you'd doubt the quality/legitimacy of the product.
  - **Cheap / bargain (yellow)** — a good deal; you would buy.
  - **Expensive (blue)** — expensive, but many would still buy.
  - **Too expensive (green)** — at this price you stop buying.
- **Respondents:** all **current users** of Basecamp, across all three tiers (see §F on pooling).

#### Anchoring bias (key definition)
> **Anchoring bias:** customers anchor on the price they already know and will **never indicate a willingness to pay more** for the same product; they systematically respond in ways that **push the stated price downward** (they fear that saying a higher number will cause the price to rise).

- **Consequence:** the **conventional Van Westendorp intersection graph cannot be used** to read off an acceptable price range. Instead, build and interpret **interquartile ranges (IQRs)** of each of the four distributions, expressed as **multiples of the current price (1x)**.

### D. Interpreting the four IQR/box plots (the core worked exercise)

All values are **multiples of the current price**, where **1x = current price**.

**1. TOO CHEAP (red) — read by Nihal**
- **Median ≈ 0.33x** (one-third of current price) → the average consumer only starts doubting quality if you discount by **more than ~66%**.
- **Whisker/quartile ends ≈ 0.9x** → a few consumers feel that **even a 10% discount** destroys the product's legitimacy.
- **Outlier dots at ~1.2x–1.5x** → a tiny minority consider even the current price (and above) "too cheap."
- **Interpretation:** it takes a *huge* discount to make the product look cheap-and-nasty → **there is headroom to increase price.**

**2. CHEAP / bargain (yellow) — read by Harshita**
- **Median ≈ 0.67x (2/3 of current price)** → the average consumer thinks 2/3 of today's price is a "bargain" price.
- **Q3 (51st–75th percentile) runs almost up to 1x** → a quarter of users think the **current price itself** is already cheap.
- **Fourth quartile / whisker extends to ≈ 1.8x**; scattered outliers at **2x, 2.5x, 3x, even 4x** who still call that "cheap."
- **Interpretation:** the whole yellow box sits **at or below** the current price and is already labelled "cheap" → **potential to increase price**; consumers lost to the increase can be compensated by the higher price paid by those who remain.

**3. EXPENSIVE (blue) — read by Mohammad**
- **Median ≈ 1.4–1.5x** → the average consumer only begins to call it "expensive" at **1.5x**, and expensive ≠ stops buying.
- **Q3 ends ≈ 2x**; **fourth quartile/whisker extends to ≈ 3.5x**.
- **Interpretation:** the median consumer may still buy at 1.5x. Some drop out, but the higher price from those who stay **compensates or increases revenue** → **potential to increase price**.

**4. TOO EXPENSIVE (green) — read by Aditi**
- **Median = 2x** → the **median consumer stops buying only at twice the current price**.
- **Q3 ≈ 3x** → the 51st–75th percentile group stops buying only at **3x**.
- **Fourth quartile/whisker ≈ 5.3x**; a minority stretch to **6x**.
- **Interpretation:** substantial margin for price increase. *Note the instructor's terminology:* "average consumer" here means the **median**, not the mean.

**Instructor's contrast/intuition check:** if the same PSM survey were run on **MS-DSM students about the programme fee**, the green (too expensive) median would **not** be 2x — it would be around **1.1x–1.2x**, because students would call even a 10–20% fee hike "too expensive." The fact that Basecamp's green median is at **2x** is what signals genuine pricing headroom.

**General decision rule stated:**
> If the **green curve sits close to 1x** and the **blue curve sits where the yellow curve currently is**, there is **no room to increase price**. Room exists precisely because blue median = 1.5x and green median = 2x.

### E. Student-proposed pricing decisions (before the reveal)
- **Rahul:** the customer base is **divided/segmented** — some accept the increase, some refuse. Recommendation: **raise price but justify it with added feature benefits** (e.g., extra integrations), even within the "no customization" philosophy; treat free vs. paid tiers as segmentation.
- **Subrat:** $29 → **$45** (≈1.5x); keep Tier 2 at **$79**; Tier 3 $3,000 → **$5,500** (<2x) with added benefits.
- **Another student:** keep $29 (treat it as **customer acquisition / trial**); $79 → **$150** (1.4–1.5x); $3,000 → **$6,000** (2x) with added features (these are high-value, committed customers).
- **Open design questions posed by the instructor** (things "under consideration"):
  - Do you **merge tiers** or **raise each tier independently**?
  - Should you introduce an **annual-payment discount** (none existed)?
  - Should you move to **per-user or per-project pricing** instead of unlimited users/projects?

### F. What Basecamp actually did
1. **Eliminated Tier 1 ($29) entirely** — it refused to sell a version that cannot distinguish internal team from client organisation. "$29 is too cheap for me."
2. **Eliminated Tier 3 ($3,000/yr) entirely** — only ~**1%** of customers were in it, and serving it means customization/dedicated support, which conflicts with the **high-volume, non-customized** strategy.
3. **Kept only Tier 2** and raised it **$79 → $99** — a **25% increase**, even though the blue-curve median said a **50% increase** was tolerable (deliberately **conservative**).
4. Introduced a **10% annual (prepay) discount** — the only "feature" added. Effective annual price ≈ **$90/month**, i.e. only about a **10–14% effective increase** over $79.
5. **Effects claimed:** overall revenue **optimized/increased (~20%)**; plus **annual prepay = customer lock-in**, **cash up front**, and no monthly renewal risk for a full year.
6. **Migration logic:** former $29 customers are **forced up to ~$90** but receive a **genuine additional feature** (company-vs-client distinction). Former $79 customers face only a ~10% effective rise, so **almost none churn** (at most ~10%).

### G. Worked revenue scenarios (the numbers used in class)

**Simple illustration (with Aayushi):**
- 10 customers × $29 = **$290**
- If only **50%** (5 customers) convert to the $90 annual-equivalent plan: 5 × $90 = **$450** → substantial gain even losing half the base.
- Break-even framing: "even if only **30%** of the $29 customers convert, that's fine, because each pays roughly **3x** more."

**Full 100-customer scenario (with Jasraj), using the tier mix 66 : 33 : 1**
- **Status quo revenue:**
  - 66 × $29 = $1,914
  - 33 × $79 = $2,607
  - 1 × $250 = $250
  - **Total = $4,771**
- **Post-change scenario (Tier 1 and Tier 3 killed, everyone on $99 with 10% annual discount = $90; assume 50% of the 66 convert, ~zero churn from the 33):**
  - Converts: 50% of 66 = 33; plus the existing 33 → **66 customers × $90 = $5,940**
  - **Gain ≈ +$1,169 ≈ +20–25% revenue**

**Counter-scenario tested (Jasraj's "why not go to 2x?"): price Tier 2 at $150**
- Conversion of existing $79 users at 2x: assume **60% of 33 ≈ 20 customers**
- Conversion of $29 users to $150 (a **~5x jump** for them): only a small minority — the blue curve shows 5x is held by only **~5–10%** of respondents → assume **~10 customers**
- Total = 30 customers × $150 = **$4,500**
- **$4,500 < $4,771 → revenue falls.** This is why the aggressive 2x option was rejected.

**Why $90 and not $150 for the ex-$29 customer:** a jump from $29 → $90 (~3x) is well inside the distribution (blue 4th quartile extends to ~3.5x; green Q3 to 3x), whereas $29 → $150 (~5x) sits in the far minority tail.

**Instructor's caveat (repeated):** Basecamp's solution was **not necessarily the optimal** solution — it was **logically justifiable** and did in fact raise revenue ~20%. Other options might have earned more but carry unknown risk.

### H. Q&A clarifications (Vikat's and Jasraj's questions)
- **Q: Is the IQR graph pooled across all three tiers? Doesn't the 66:33:1 mix skew it?**
  A: Yes, pooled. The case also contains **separate IQR graphs for the $29 and $79 cohorts**, and they produce **broadly the same conclusions**. Pooling is acceptable because **anchoring bias affects every user identically** regardless of tier.
- **Q: Respondents already know the prices ($29/$79/$250) — doesn't that form an opinion?**
  A: Yes — these are all **current users**, which is precisely the source of anchoring bias; the IQR method is the workaround.
- **Q: Was there a specific pricing model behind $99?**
  A: **No formal pricing model** — only these PSM graphs plus **multiple scenario simulations** with different assumed conversion probabilities and their associated risks. The scenario table is **not in the case**; students must generate it.

### I. Methodological summary (examinable core)
- Two research methods were used **in combination**: an **experiment (A/B test)** and a **survey (Van Westendorp PSM)**. Experiments and surveys are the **two major business research methods**, used extensively in marketing and management.
- **Principle of triangulation:** *never rely on a single research method for the same problem.*
  - The **experiment** only told the firm that **2x is too high**. It gave **no evidence** about +80%, +90%, etc.
  - The experiment **cannot easily be repeated** → switch to the **survey**.
  - The **survey must not be read straightforwardly** (anchoring bias) → use **interquartile ranges**, which reveal *whether* there is room to raise price.
  - The remaining gap (*how much* to raise, *how many* customers you lose) is closed with **scenario analysis / informed guesswork**.
- **Evidence-based decision-making** still involves guesswork, because **you will never have complete information** — but you will have *some* information to bound the decision.

### J. New case introduced — the 30-manager, 7-item survey dataset
- **Data:** an Excel sheet shared with the readings. **Rows 1–30 = 30 middle managers** in one organisation. **Columns I1–I7 = 7 survey items.**
- **Measurement:** each item on a **rating scale of 1 to 10** (1 = very low, 10 = maximum). Ratings supplied by the manager's **supervisors and peers**. Survey administered **monthly**; the sheet contains the **annual average** per manager per item.
- **The seven items (verbatim as read out):**
  - **I1** — She/he is an **excellent interface between top and operational management**.
  - **I2** — Of late she/he has been **talking about positive aspects of the culture in other organisations**.
  - **I3** — Of late she/he has become **more formal and official in her/his interactions with colleagues**.
  - **I4** — She/he is able to **accurately assess the potential applicability of new ideas**.
  - **I5** — She/he is able to **energize people around her/him**.
  - **I6** — She/he **demonstrates clarity and commitment in terms of what needs to be done and how to move forward quickly**.
  - **I7** — Of late she/he has been **talking about how well her/his MBA batchmates are doing in their career**.
- **The task set for next session:** Can these 7 items be **grouped**? Into one group, two groups, three groups… or are all seven distinct (i.e., 7 separate groups)? If grouped, **which item belongs to which group**? (This is the set-up for factor/construct analysis.)
- **Discussion of I2 (with Harshita):** an employee praising another organisation's culture typically signals *"I find another organisation more attractive than mine."* It is a **leading indicator of attrition / dissatisfaction**.
  - Key clarification: **an indicator need not be a "positive" indicator** — it just needs to be **worth measuring**. Managers want lead indicators of whether an employee is satisfied/dissatisfied and therefore likely to **stay or leave**.
  - (I7 — comparing oneself with MBA batchmates' careers — is a parallel item in the same spirit.)

---

## 3. Flagged for exams / assignments / next class

- **Assignment given to the whole class:** construct **8–10 alternative pricing scenarios** for Basecamp (different price points × different assumed conversion rates for the $29 and $79 cohorts) and compute the revenue for each, to see which would have been best. Two scenarios were done in class ($90 and $150); the rest are **left to students**. Bring these to the next session for discussion.
- **Pre-work for the next session:** locate the **shared Excel dataset** (30 managers × I1–I7) in the readings and think about **how to group the seven items**. The next class **begins exactly at this point** — categorising the indicators.
- **What the instructor says actually matters for assessment:**
  > "To us what is important is **not the decision per se** but the **research techniques** we have been able to learn."
  Be able to explain: the **A/B test** (design, what conversion ratios tell you, its limitations), the **Van Westendorp PSM survey** (4 questions, four price constructs), **anchoring bias**, why conventional PSM graphs fail, and how to **read medians, Q1–Q4 and whiskers** off the four curves in multiples of 1x.
- **Next class: 10:45 a.m. the following day** (first class of the day).
- Instructor shared **email ID and WhatsApp number** on screen and invited offline discussion of alternative scenarios.