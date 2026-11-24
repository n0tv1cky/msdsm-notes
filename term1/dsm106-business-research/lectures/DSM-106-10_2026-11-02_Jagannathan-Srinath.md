---
course: DSM 106
date: 2026-11-02
start: 7:00pm
session: "10"
faculty: Jagannathan Srinath
---

<!-- nav -->
← [Session 9 (2026-10-21)](DSM-106-9_2026-10-21_Jagannathan-Srinath.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-106 Business Research, Session 10: The stickK ("Stick") Case

## Overview

This session works through the **stickK** case, which the transcript calls "Stick." stickK is a startup that turns principles of **behavioral economics** into a business built on **commitment contracts**. The class first described how stickK's consumer product works. It then identified **six behavioral-economics barriers** that stop people from overcoming bad habits and mapped each barrier to a stickK product feature, for both the B2C and the B2B offerings. Next came the main **business research question**: should stickK focus on retail consumers (B2C) or corporate and non-profit clients (B2B)? The class answered it with a **revenue analysis** using the case exhibit data. B2C yields about \$220,000 a year and B2B about \$720,000 a year. The class then discussed the operational implications of going B2B (staffing, marketing, customization), compared the decision with the earlier **Basecamp** case, critiqued the incentive problem in the B2C revenue model, and closed the course with logistics for the interim exam and the group assignment.

---

## Topics, Concepts, and Worked Examples (in order taught)

### 1. The company and its two offerings

- stickK uses behavioral economics to help people keep commitments they make to themselves. Typical goals are weight loss, fitness, quitting smoking, finances and relationships. Most users chose fitness and weight goals.
- **B2C offering:** consumers sign up on the public website and create commitment contracts.
- **B2B offering:** stickK builds a dedicated website for a company's wellness program or a non-profit's change program (e.g., the American Cancer Society).
  - Employees earn **points** for meeting goals.
  - They exchange the points for **prizes** from the employer or organisation.
- **Strategic question:** should stickK serve retail consumers, businesses, or both? The class compared this with the first case of the course, **Basecamp**, which chose to serve only small and medium-sized customers.

### 2. How a commitment contract works (B2C)

**Example from the lecture:**
- A user signs a 30-week contract worth \$360.
- The weekly stake is:

```math
\frac{360}{30} = 12 \text{ dollars per week}
```

- The weekly target might be "go to the gym 3 times a week, for at least 1 hour each time."
- If the user meets the target that week, they keep the \$12. If they miss it, they forfeit that week's \$12.

**The four steps on the website:**

1. **Set a goal.** Preset options include lose weight, maintain weight, exercise regularly, quit smoking, and complete a marathon or race in a given time.
   - For health and safety reasons, weight-loss goals are always *ongoing* (spread over weeks).
   - Example: lose 20 lb in 20 weeks means a commitment to lose 1 lb per week, reported weekly.
2. **Set the stakes.** The user wagers money on achieving the goal.
   - The total wager is divided evenly across the weeks.
   - Each week the user misses, they lose that week's fraction.
   - The user chooses who receives forfeited money:
     - a **friend**;
     - a **charity** the user supports;
     - an **anti-charity**, meaning a cause the user dislikes.
   - Anti-charity example: in the 2008 US elections, the two options were the Bill Clinton Library and the George W. Bush Library. In a polarised country, Democrats hated the idea of funding the Bush library, and Republicans the Clinton library. The anti-charity option was very popular and produced the best results.
3. **Appoint a referee.** The referee can be a friend, co-worker or anyone else, and monitors whether the user is adhering to the goal.
   - The user submits **self-reports**.
   - If the self-report and the referee's report clash, the **referee's report prevails**, because the referee has actually observed the behaviour.
4. **Add supporters.** Other people can follow the user's goal, comment on the page and give encouragement.

**Payment design:**
- The user provides credit card details, but the card is **not charged upfront**.
- Charging upfront and refunding successful users would have cost stickK the card processors' **3% fee** on every charge, which would have been a large amount.
- So the card is charged only for the amount actually forfeited.

**Revenue model (B2C):**

| Recipient of forfeited money | stickK's commission |
|---|---|
| Friend | 0% |
| Charity | 19.5% |
| Anti-charity | 29.5% |

**Key case facts:**
- The average stake is \$360.
- **32%** of commitment contracts include stakes.
- Overall, about **80%** of staked contracts succeed and about **20%** fail.

### 3. Why people fail to overcome bad habits: six behavioral-economics barriers

The opening class suggestion was "comfort zone." The instructor accepted this and then introduced the formal principles below.

1. **Time inconsistency / hyperbolic discounting**
   - The benefits of breaking a bad habit are deferred: months, years, or a lifetime later. Examples are lower risk of diabetes and heart disease, which are not very salient to a 25- or 35-year-old.
   - The pleasure of the bad habit, such as eating, is immediate.
   - People heavily discount delayed benefits and overvalue immediate pleasure, so they choose the temporary pleasure.
   - *Supplementary, not stated in the lecture:* the standard hyperbolic discounting form is

```math
V = \frac{A}{1 + kD}
```

     where $`V`$ is the present value, $`A`$ is the reward amount, $`D`$ is the delay, and $`k`$ is the discount rate.

2. **Progress is invisible**
   - Especially early in behaviour change, results are hard to see.
   - This is worst when the link between a single behaviour and the outcome is unclear. Examples given: how much does skipping one cigarette on a coffee break reduce lung-cancer risk? How much weight does one more potato chip add?
   - Without progress information, people feel they are "flailing." Their motivation is dampened and they stop trying.

3. **Social pressure**
   - Many bad habits, such as smoking and overeating, happen in groups and social gatherings.
   - Quitting can feel like withdrawing from the group's interaction.

4. **Vague goals**
   - Without specific goals, success cannot be defined.
   - Vague goals are a major impediment to breaking bad habits.

5. **Over-optimism**
   - People are notoriously overconfident about achieving their goals, especially health goals.
   - As a result they undervalue **commitment devices** and decline help they would benefit from.

6. **Resisting temptation / the licensing effect**
   - Successfully resisting temptation can make people feel they have earned a "license" to overindulge later.
   - Example 1: skipping dessert at lunch leads to eating many sweets at dinner. Rationing (a small portion at lunch) would have avoided the licensing effect.
   - Example 2: cutting screen time to zero for a week leads to a binge the next week and a complete loss of control.
   - Advertising and constant enticements keep temptation all around us.

### 4. Mapping the six barriers to stickK's product (B2C)

| Barrier | How stickK addresses it |
|---|---|
| Time inconsistency | The long-term goal (e.g., 6–12 months of weight loss) is converted into **weekly targets**, such as 3 gym sessions per week or about 250–500 g lost per week. Reward and punishment become **immediate** rather than deferred. **Loss aversion**: people hate losing their stake, so after losing money one week they try harder the next. |
| Progress invisible | Mandatory weekly **self-reports and referee reports** make progress **salient**. Users who fail to report forfeit their deposit, which is a further use of loss aversion. stickK's research showed that simply **monitoring and tracking** behaviour helps change it; for example, recording food intake curbs consumption. stickK can also exploit the **"progress illusion"**: the mere *perception* of progress facilitates goal attainment. |
| Social pressure | Negative social pressure is turned into positive pressure through **referees**, which bring accountability (the "stick"), and **supporters/cheerleaders**, who bring encouragement (the "carrot"). Supporters receive alerts and cheer the user on. |
| Vague goals | Users **must specify a goal** as the first step before using the site. The 30-week contract is broken into weekly and daily goals, such as 1 hour at the gym plus a diet. *Suggested improvement:* force goals to be more concrete. For example, "spend more time with family" should become a specific weekly target. |
| Over-optimism | Signing the contract **locks in the stakes**. Users cannot arbitrarily rewrite the stake or change the goal, so they are putting real money on their confidence. |
| Resisting temptation | The instructor said stickK currently does **not directly address** the licensing effect and needs novel features for it. Students raised two partial counterpoints, both accepted: an **independent referee** helps, provided the referee genuinely cares; and the **contract itself**, with its penalty, deters giving in. Nothing *beyond* the contract was identified. |

### 5. Mapping the barriers to the B2B product

- **Time inconsistency:**
  - B2C imposes an **immediate cost for bad behaviour**, because users lose their own money.
  - B2B offers an **immediate benefit for good behaviour**: points that convert to prizes, and employees lose nothing.
  - A penalty could be built into B2B too, for example by granting points upfront and deducting them for lapses.
- **Progress invisible:** the B2B product can also make progress visible. The difference is that B2C users risk real money, while B2B users are incentivised by rewards.
- **Social pressure:** the boss and close colleagues provide accountability.
- **Vague goals:** goals are still defined upfront.
- **Over-optimism:** this is harder to counter in B2B, because employees lose nothing.
- **Resisting temptation:** no money is at stake, so this barrier is an open problem for B2B.

### 6. Business research analysis: B2C vs B2B revenue

**Data from the case exhibits (success rates by stake type):**

| Contract type | Success rate | Failure rate |
|---|---|---|
| No stakes | 42.7% | — |
| Stakes to friend | 75.7% | 24.3% |
| Stakes to charity | 80.1% | 19.9% |
| Stakes to anti-charity | 87.1% | 12.9% |

The anti-charity option, the "most painful" stake, produces the highest success rate.

#### Worked example: B2C annual revenue (2012)

**Step 1. Total contracts:** 70,000 per year.

**Step 2. Contracts with stakes (32%):**

```math
0.32 \times 70{,}000 = 22{,}400
```

**Step 3. Split of staked contracts by recipient:**

| Recipient | Share | Number of contracts | Commission |
|---|---|---|---|
| Friend | 26.3% | — | 0%, so no revenue |
| Charity | 21.6% | $`0.216 \times 22{,}400 \approx 4{,}838`$ | 19.5% |
| Anti-charity | 52.1% | $`0.521 \times 22{,}400 \approx 11{,}670`$ | 29.5% |

**Step 4. First-pass revenue, which wrongly assumes every staked contract forfeits its full \$360:**

For charity:

```math
4{,}838.4 \times 0.195 \times 360 \approx 339{,}656
```

For anti-charity:

```math
11{,}670.4 \times 0.295 \times 360 \approx 1{,}239{,}397
```

The total is about \$1.58 million. The class quoted this as "roughly \$1.5 million."

**Step 5. Correction.** Money is forfeited **only when a contract fails**, so each stream must be multiplied by its failure rate:
- charity: $`0.199`$;
- anti-charity: $`0.129`$.

**Step 6. Deduct the 3% credit card fee** by multiplying by $`0.97`$. (The lecture applied the 3% to the total; strictly, the fee applies to the amounts actually charged.)

The full B2C formula is:

```math
R_{B2C} = 0.97 \times 360 \times \left[(0.216)(22{,}400)(0.199)(0.195) + (0.521)(22{,}400)(0.129)(0.295)\right]
```

Working this through:

```math
R_{B2C} \approx 0.97 \times (67{,}592 + 159{,}882) \approx 0.97 \times 227{,}474 \approx 220{,}650
```

**B2C revenue ≈ \$220,000 per year.** The lecture assumed that a failed contract forfeits the full \$360 average stake, which is a simplification.

#### Worked example: B2B annual revenue

The class used the following assumptions:
- **Current clients:** 4.
- **One-time setup fee:** \$20,000–\$50,000. The class used an average of \$35,000.
- **Monthly website maintenance fee:** average \$15,000 per client.

**One-time setup revenue (not recurring, so excluded from annual revenue):**

```math
35{,}000 \times 4 = 140{,}000
```

**Recurring annual revenue per client:**

```math
15{,}000 \times 12 = 180{,}000
```

**Recurring annual revenue across all clients:**

```math
R_{B2B} = 180{,}000 \times 4 = 720{,}000
```

**B2B revenue ≈ \$720,000 per year**, compared with about \$220,000 for B2C. B2B is clearly more lucrative with only 4 clients.

### 7. Implications and recommendation

**What scaling B2B requires.** Suppose stickK adds a new client every 2 months, reaching about 25 clients in 2 years. It would then need:
- **Dedicated staff per client:** about 5–10 people each. The class put salaries at roughly \$85,000–\$90,000 per staff member (the transcript reads "\$85,000, \$9,001").
- **A marketing and sales team** with a marketing strategy, to actively approach companies.
- **Customization** for each client.
- Budgets for compensation and employee growth, i.e., building **human capital**.

**B2C by contrast:**
- runs on the website with roughly 10–15 employees;
- acquires users through word of mouth and Facebook;
- the main need is to keep improving product value and onboarding.

**Basecamp comparison:** Basecamp refused large clients and customization so that it could stay small (about 50 employees) and serve SMEs. The same kind of research led to a **different decision** for stickK.

**Student recommendation (accepted):** go B2B because the upside is much larger. Keep B2C running for now and shift emphasis over time.

**Actual outcome:**
- stickK did focus on B2B and grew from **4 to 16 B2B clients within one year**.
- At \$180,000 per client, 16 clients is about \$2.9M. The instructor said "\$3–4 million."
- The startup became **cash-flow neutral**.
- It explored apps and integration with **wearable devices**, and invested a little in B2C.

### 8. Two roles of business research, and a critique

**Business research played two roles in this case:**

1. **Creating the business model itself.** stickK came out of Yale. Two professors, one in economics and one in law and management, were researching commitment contracts and behavioral economics. They gave the idea and **\$150,000 seed money** to a student entrepreneur. The six principles were then built into the product.
   - *Takeaway:* the case gives a **toolkit for converting behavioral-economics principles into a business model**.
2. **The strategic choice of segment.** The B2C vs B2B revenue analysis above.

**Critique of the B2C revenue model: misaligned incentives.**
- stickK earns money **only when users fail**, so it has a vested interest in failure.
- With an 80% success rate, it has little incentive to improve success to 90%.
- *Suggested fix:* charge an **upfront fee** regardless of outcome, so the company also earns when users succeed.

---

## Exam, Assignment, and Course Logistics

- **Interim exam:**
  - covers the cases discussed in the course;
  - **individual**;
  - **open book, open notes, open internet**.
  - The instructor will send **model questions with model answers**.
- **Remaining cases** not discussed in class are "fairly self-explanatory"; the solutions are contained in the case and reading. Read them.
- **Assignment:**
  - a **group assignment**;
  - based on course content such as financial analysis, market analysis, or what kind of business should be built;
  - the question and a broad deadline will be set by the instructor.
- **The stickK case PDF is not in the Session 9 reading materials.** Session 9 contains only the "rise of behavioral economics" reading. The instructor will ask the office to circulate the case.
- **A summary sheet** will be provided, mapping each business research method to the case it was covered in, with its implications.
- **Doubts and support:**
  - contact by email or WhatsApp (number shared in chat);
  - an optional doubt-clearing online session can be arranged for those who need it.
- **Likely exam-relevant material:**
  - the six behavioral barriers and how stickK addresses each, for both B2C and B2B;
  - the B2C vs B2B revenue calculation;
  - the B2B scaling implications;
  - the Basecamp vs stickK contrast;
  - the incentive-misalignment critique.

<!-- nav -->
← [Session 9 (2026-10-21)](DSM-106-9_2026-10-21_Jagannathan-Srinath.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
