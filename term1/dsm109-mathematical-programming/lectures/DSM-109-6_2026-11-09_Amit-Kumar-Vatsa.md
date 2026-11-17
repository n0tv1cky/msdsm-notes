---
course: DSM 109
date: 2026-11-09
start: 8:15pm
session: "6"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 5 (2026-11-06)](DSM-109-5_2026-11-06_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Session 6: Sensitivity Analysis on the Mordern Truck Case (Ranging, Reduced Cost, Pricing Out, Overtime)

*Lecturer: Amit Kumar Vatsa · Session file: DSM-109-6_2026-11-09*

> **Notes on reconstruction:** The case was heard as "modern track" / "Murden" / "Martin". It is the truck-manufacturing product-mix case discussed in the previous class. Some numbers were garbled by ASR. Where I had to infer or correct a number, I mark it **[inferred]** or **[corrected]** and explain why. All money is in USD. I write "USD" instead of a dollar sign so it doesn't clash with LaTeX.

---

## 1. Overview

This session continues the sensitivity analysis of the truck product-mix LP. Shadow prices were covered in the previous class. The lecturer first shows how to compute the **allowable increase and decrease of a right-hand side (RHS)** in two ways:

- **graphically**, by sliding the engine-assembly constraint until it hits the neighbouring corner points;
- **algebraically**, by solving the binding constraints with a perturbation $\Delta$ and requiring every variable and slack to stay non-negative (done for metal stamping).

The class then answers the case's managerial questions:

- the value of one extra engine-assembly hour;
- whether to rent engine-assembly capacity from an outside supplier;
- whether to introduce a new **Model 103** truck. This introduces **reduced cost** and "pricing out" a new product using shadow prices.
- whether to use **overtime** in engine assembly, with two alternative LP formulations.

The recurring message: a single LP solve plus its sensitivity report answers many "what-if" questions without re-optimising. The session ends with a brief preview of objective-coefficient ranging, to be continued next class.

---

## 2. Topics covered (in order)

### 2.1 Recap: the base model

**Decision variables**
- $x_1$ = number of Model 101 trucks produced per month (units)
- $x_2$ = number of Model 102 trucks produced per month (units)

**Model**

$$
\begin{aligned}
\max\ & Z = 3000\,x_1 + 5000\,x_2 && \text{(total monthly contribution, USD)}\\
\text{s.t. }\ & x_1 + 2x_2 \le 4000 && \text{(engine assembly, hours/month)}\\
& 2x_1 + 2x_2 \le 6000 && \text{(metal stamping, hours/month)}\\
& 2x_1 \le 5000 && \text{(Model 101 assembly line, hours/month)}\\
& 3x_2 \le 4500 && \text{(Model 102 assembly line, hours/month)}\\
& x_1,\ x_2 \ge 0
\end{aligned}
$$

**Where the objective coefficients come from:**
- A student quoted "$2000x_1 + 3000x_2$", but the lecturer's formulation uses $3000x_1 + 5000x_2$.
- Only $3000x_1 + 5000x_2$ is consistent with the shadow prices of 2000 and 500 used throughout: $1(2000) + 2(500) = 3000$ and $2(2000) + 2(500) = 5000$.
- It is also consistent with "11 million" optimal profit.

**Graphical solution: feasible region and corner points**

The corner points other than D and E are **[inferred]** from the constraint lines.

| Corner | Intersection of | $(x_1, x_2)$ | $Z$ (USD) |
|---|---|---|---|
| O | axes | $(0, 0)$ | 0 |
| — | $x_2 = 0$ and Assembly 101 ($x_1 = 2500$) | $(2500, 0)$ | 7,500,000 |
| **E** | Assembly 101 and metal stamping | $(2500, 500)$ | 10,000,000 |
| **D (optimal)** | Engine assembly and metal stamping | $(2000, 1000)$ | **11,000,000** |
| — | Engine assembly and Assembly 102 ($x_2 = 1500$) | $(1000, 1500)$ | 10,500,000 |
| — | Assembly 102 and $x_1 = 0$ | $(0, 1500)$ | 7,500,000 |

**Status of each constraint at the optimum D $=(2000, 1000)$:**
- **Binding** (bottlenecks, RHS fully used): engine assembly and metal stamping.
- **Non-binding**: Assembly 101 has slack $s_3 = 5000 - 4000 = 1000$ hours. Assembly 102 has slack $s_4 = 4500 - 3000 = 1500$ hours.

**Shadow prices (from the previous class):**
- engine assembly: 2000 USD/hour
- metal stamping: 500 USD/hour
- Assembly 101: 0
- Assembly 102: 0

Increasing the RHS of a non-binding constraint does not change the objective.

### 2.2 Meaning of allowable increase / decrease (RHS ranging)

Definition, in plain English: *how far an RHS can change while the **set of binding constraints stays the same***. Equivalently, it is the range over which the **shadow prices stay unchanged**. Here that means engine assembly and metal stamping remain the binding pair.

### 2.3 Allowable change in engine-assembly RHS: graphical method

Current RHS = 4000. Move the line $x_1 + 2x_2 = 4000 + \Delta_1$ and track the optimal corner D′, which is the intersection with metal stamping.

**Increase.** As the line moves outward, D′ slides up along the metal-stamping line. It stops being the binding pair once it reaches the point where metal stamping meets Assembly 102:
- $x_2 = 1500$ from Assembly 102, so $x_1 = 3000 - 1500 = 1500$. The point is $(1500, 1500)$.
- New RHS: $1(1500) + 2(1500) = 4500$.
- **Allowable increase = 500 hours.**

**Decrease.** As the line moves inward, D′ slides down the metal-stamping line until it reaches E $=(2500, 500)$. Past E, the optimum becomes the intersection of Assembly 101 with the new engine line.
- New RHS: $1(2500) + 2(500) = 3500$.
- **Allowable decrease = 500 hours.**

So the 2000 USD/hour shadow price is valid for engine-assembly RHS in $[3500, 4500]$.

*Algebraic check* **[inferred, same method as 2.4]**:
- Solving the binding pair gives $x_1 = 2000 - \Delta_1$ and $x_2 = 1000 + \Delta_1$.
- $s_3 = 5000 - 2x_1 \ge 0$ gives $\Delta_1 \ge -500$.
- $s_4 = 4500 - 3x_2 \ge 0$ gives $\Delta_1 \le 500$.

### 2.4 Allowable change in metal-stamping RHS: algebraic method

1. **Write the binding constraints as equations and add slacks to the non-binding ones.**

$$
\begin{aligned}
x_1 + 2x_2 &= 4000\\
2x_1 + 2x_2 &= 6000 + \Delta_2\\
2x_1 + s_3 &= 5000\\
3x_2 + s_4 &= 4500
\end{aligned}
$$

2. **Solve the two binding equations for $x_1$ and $x_2$ in terms of $\Delta_2$.**
   - Subtract equation 1 from equation 2: $x_1 = 2000 + \Delta_2$.
   - Substitute: $2x_2 = 4000 - (2000 + \Delta_2)$, so $x_2 = 1000 - \tfrac{1}{2}\Delta_2$.

3. **Require every variable and slack to stay non-negative.**

| Condition | Expression | Gives |
|---|---|---|
| $x_1 \ge 0$ | $2000 + \Delta_2 \ge 0$ | $\Delta_2 \ge -2000$ |
| $x_2 \ge 0$ | $1000 - \tfrac12\Delta_2 \ge 0$ | $\Delta_2 \le 2000$ |
| $s_3 \ge 0$ | $5000 - 2(2000 + \Delta_2) = 1000 - 2\Delta_2 \ge 0$ | $\Delta_2 \le 500$ |
| $s_4 \ge 0$ | $4500 - 3(1000 - \tfrac12\Delta_2) = 1500 + \tfrac32\Delta_2 \ge 0$ | $\Delta_2 \ge -1000$ |

4. **Take the tightest bounds:**

$$-1000 \le \Delta_2 \le 500$$

**Metal stamping: allowable increase = 500 hours, allowable decrease = 1000 hours.** This matches the Excel Solver sensitivity report. The shadow price of 500 USD/hour holds for RHS in $[5000, 6500]$.

*Note* **[inferred, not discussed]**: for the non-binding constraints, the allowable increase is $\infty$. The allowable decreases equal the slacks: 1000 hours for Assembly 101 and 1500 hours for Assembly 102.

### 2.5 Case question (b): one extra unit of engine-assembly capacity

- Change the RHS to $x_1 + 2x_2 \le 4001$ and re-solve, or simply use the shadow price.
- Objective rises by 2000: from 11,000,000 to **11,002,000**.
- New mix **[inferred from §2.3 formulas]**: $x_1 = 1999$, $x_2 = 1001$.
- Capacity can be added at 2000 USD/hour up to the **allowable increase of 500 hours**, i.e. up to 4500 hours. Beyond that the shadow price changes.

### 2.6 Case question 2: rent engine-assembly capacity from an outside supplier

**The proposal.** Buy Model 101/102 engines from an outside supplier. The company supplies the materials and components and reimburses the supplier's labour and overhead. This amounts to renting engine-assembly hours.

**Should the company adopt it?** Yes. Engine assembly is a bottleneck worth 2000 USD/hour.

**Maximum rent.** Each outsourced engine-hour saves the company costs it would otherwise have incurred, such as direct labour and variable overhead in engine assembly.
- The ASR heard "2,000" and "2,100" for these per-unit amounts.
- The direct-labour figure is likely 1,200 USD per Model 101, consistent with §2.8 **[uncertain]**.

So the company should:
- reimburse the supplier those avoided costs, **plus**
- share part of the 2000 USD/hour profit gain.

The maximum premium above the reimbursed costs is **2000 USD per machine-hour**, the shadow price. This is because contribution margins are already net of these variable costs.

**Maximum hours to rent: 500**, the allowable increase. Beyond that the shadow price no longer applies.

The lecturer's analogy: it is like paying your own workers for overtime. You pay their costs and can share part of the extra profit.

### 2.7 Case question: introduce Model 103? Reduced cost and pricing out

**Data, derived from the case statements:**

- Contribution: 2000 USD per truck.
- Engine assembly: 4000 hours suffice for 5000 units, so $4000/5000 = 0.8$ h/unit.
- Metal stamping: 6000 hours suffice for 4000 units, so $6000/4000 = 1.5$ h/unit.
- Assembly: uses the **Model 101 line** and needs half the time of a Model 101 (2 h), so 1 h/unit.
- A student asked whether the 4000 hours change. No: available hours stay the same. Model 103 just competes for them.

**Approach 1: extend the LP and re-optimise.** Add $x_3$ = number of Model 103 trucks per month (units).

$$
\begin{aligned}
\max\ & Z = 3000x_1 + 5000x_2 + 2000x_3\\
\text{s.t. }\ & x_1 + 2x_2 + 0.8x_3 \le 4000 && \text{(engine assembly, h)}\\
& 2x_1 + 2x_2 + 1.5x_3 \le 6000 && \text{(metal stamping, h)}\\
& 2x_1 + x_3 \le 5000 && \text{(Model 101 line, shared by 103, h)}\\
& 3x_2 \le 4500 && \text{(Model 102 line, h)}\\
& x_1, x_2, x_3 \ge 0
\end{aligned}
$$

Solver result: $x_3 = 0$, so Model 103 is not produced and the solution is unchanged.

**Approach 2: pricing out with shadow prices (no re-optimisation needed).** Value each resource hour that Model 103 consumes at its shadow price.

| Resource | Hours per unit | Shadow price (USD/h) | Opportunity cost (USD) |
|---|---|---|---|
| Engine assembly | 0.8 | 2000 | 1600 |
| Metal stamping | 1.5 | 500 | 750 |
| Assembly 101 line | 1 | 0 | 0 |
| **Total** | | | **2350** |

**Reduced cost** of $x_3$ = contribution − opportunity cost of resources:

$$\bar c_3 = c_3 - \sum_i a_{i3}\, y_i = 2000 - (0.8 \cdot 2000 + 1.5 \cdot 500 + 1 \cdot 0) = 2000 - 2350 = -350$$

**Interpretation of reduced cost:**
- It is the change in the objective per unit if you force the variable into the solution. Each Model 103 built lowers profit by 350 USD, because it diverts hours from more profitable products.
- The lecturer verified this in Solver by adding $x_3 \ge 1$ (worded as "$x_3 = 1$"). The objective fell by about 350 ("ignore the fraction part").
- It is also how much the objective coefficient must improve before the product enters. Model 103's contribution must be **at least 2350 USD** (an increase of 350) before launching it makes sense.

**Rule:** produce a new product only if its contribution is at least the opportunity cost of the resources it uses, valued at shadow prices.

### 2.8 Case question: overtime in engine assembly

**Data:**
- 2000 machine-hours of engine-assembly overtime are available, with production efficiency unchanged.
- Direct labour cost is 50% higher on overtime. Variable overhead is unchanged.
- Monthly fixed overhead in engine assembly rises by **0.75 million** USD if overtime is used. The ASR said "0.75 million" first, later "0.7 million" for the fixed cost. The case figure is 0.75M; 0.7M is the benefit.

**Overtime cost per hour.** Engine-assembly direct labour is 1200 USD for Model 101 (1 h) and 2400 USD for Model 102 (2 h), so 1200 USD/hour. A 50% premium means **600 USD/hour extra**.

**Approach 0: logic with shadow prices.**
- Net gain per overtime hour: $2000 - 600 = 1400$ USD/hour.
- Useful overtime hours = allowable increase = 500 hours. The ASR said "100 hours", **[corrected]** to 500 per §2.3.
- Total benefit: $1400 \times 500 = 700{,}000 = 0.7$ million USD.
- Decision rule: overtime pays only if the fixed-overhead increase is **less than 0.7 million**.
- Since the fixed overhead rises by 0.75 million, which exceeds 0.7 million, **overtime is not worthwhile**. The lecturer's example of the extra fixed cost: "AC and all the bills will have to keep running."

**Formulation 1: overtime-hours variable** (suggested by Rahul)
- $x_1$ = units of Model 101 per month; $x_2$ = units of Model 102 per month.
- $y$ = engine-assembly overtime hours used per month (hours).

$$
\begin{aligned}
\max\ & Z = 3000x_1 + 5000x_2 - 600y\\
\text{s.t. }\ & x_1 + 2x_2 \le 4000 + y && \text{(engine assembly: regular + overtime hours)}\\
& 2x_1 + 2x_2 \le 6000 && \text{(metal stamping)}\\
& 2x_1 \le 5000 && \text{(Model 101 line)}\\
& 3x_2 \le 4500 && \text{(Model 102 line)}\\
& y \le 2000 && \text{(overtime availability [inferred, from case data])}\\
& x_1, x_2, y \ge 0
\end{aligned}
$$

Result as stated by the lecturer:
- $y = 500$ hours, and $x_1, x_2$ change (he first said "unchanged", then corrected himself).
- **[Inferred]** The new mix is $x_1 = 1500$, $x_2 = 1500$.
- Objective: $3000(1500) + 5000(1500) - 600(500) = 11{,}700{,}000$, an increase of 0.7 million.

The 0.75M fixed overhead is not in this LP and is compared separately. Modelling it inside the LP would need a binary variable.

**Formulation 2: separate regular and overtime production**
- $x_1, x_2$ = units of Model 101 / 102 whose engines are assembled in **regular** hours.
- $x_1', x_2'$ = units of Model 101 / 102 whose engines are assembled in **overtime**.
- Overtime reduces contribution by 600 per Model 101 (1 h) and by 1200 per Model 102 (2 h).
  - Model 101 overtime contribution: $3000 - 600 = 2400$.
  - Model 102 overtime contribution: $5000 - 1200 = 3800$.
  - **[Corrected]** The ASR read "3800 $x_1'$ and 3200 $x_2'$", which is inconsistent with the stated reductions.

$$
\begin{aligned}
\max\ & Z = 3000x_1 + 5000x_2 + 2400x_1' + 3800x_2'\\
\text{s.t. }\ & x_1 + 2x_2 \le 4000 && \text{(engine assembly, regular hours)}\\
& x_1' + 2x_2' \le 2000 && \text{(engine assembly, overtime hours)}\\
& 2(x_1 + x_1') + 2(x_2 + x_2') \le 6000 && \text{(metal stamping, regular only)}\\
& 2(x_1 + x_1') \le 5000 && \text{(Model 101 line)}\\
& 3(x_2 + x_2') \le 4500 && \text{(Model 102 line)}\\
& x_1, x_2, x_1', x_2' \ge 0
\end{aligned}
$$

This gives the same answer: totals of 1500 each, 500 overtime hours used, and an objective increase of 0.7M before fixed overhead. **[Inferred]** The regular/overtime split is not unique, because the overtime penalty is the same per engine-hour.

**Lecturer's point:** all three approaches are correct. Once you understand shadow prices, you can reason out such changes without re-optimising. One LP solve gives the value of every extra unit of each resource.

### 2.9 Preview: allowable increase/decrease of objective coefficients

- This asks how much a product's contribution can change before the optimal **product mix** (corner D) changes.
- Example: if Model 101's contribution moves from 3000 to 3100, 3200, 3300, the mix stays the same. The lecturer showed this by re-optimising in Solver. So small market-price fluctuations don't require replanning.
- Stated range: 3000 can rise by **2000**, to 5000, with D still optimal.
- **[Inferred] Geometric check.** D stays optimal while the objective slope $-c_1/c_2$ lies between the slopes of the two binding lines, $-1$ (metal stamping) and $-\tfrac12$ (engine assembly).
  - With $c_2 = 5000$: $2500 \le c_1 \le 5000$. Allowable increase 2000, allowable decrease 500.
  - With $c_1 = 3000$: $3000 \le c_2 \le 6000$.
- To be covered in detail next class.

---

## 3. Exam and assignment pointers

No explicit "this will be on the exam" statement was made. The lecturer repeatedly emphasised:

- **Be able to compute RHS ranging (allowable increase/decrease) both graphically and algebraically.** The algebraic method: solve the binding constraints with $\Delta$, then require $x_j \ge 0$ and $s_i \ge 0$.
- **Interpret shadow prices managerially**:
  - the value of an extra hour;
  - the maximum premium to pay for rented or outsourced capacity;
  - the shadow price is valid only within the allowable range.
- **Price out new products using shadow prices.** Know that **reduced cost = contribution − opportunity cost of resources consumed**, and what a negative reduced cost means.
- **Evaluate overtime or capacity expansion** as (shadow price − incremental variable cost) × usable hours, then compare with any fixed cost.
- Be able to **formulate overtime models** in either style: an overtime-hours variable, or separate regular and overtime production variables.
- **Key theme:** you usually do not need to re-optimise. Use the sensitivity report.

**Key numbers to remember for this case:**
- Optimum $(x_1, x_2) = (2000, 1000)$, $Z$ = 11 million USD.
- Shadow prices: 2000 / 500 / 0 / 0.
- Engine-assembly range: ±500 hours.
- Metal-stamping range: +500 / −1000 hours.
- Model 103 reduced cost: −350.
- Overtime: net benefit 0.7M versus 0.75M extra fixed overhead, so no overtime.

<!-- nav -->
← [Session 5 (2026-11-06)](DSM-109-5_2026-11-06_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
