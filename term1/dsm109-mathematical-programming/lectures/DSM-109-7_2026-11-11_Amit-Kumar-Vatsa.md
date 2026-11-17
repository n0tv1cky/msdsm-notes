---
course: DSM 109
date: 2026-11-11
start: 7:00pm
session: "7"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Session 7: Objective-Coefficient Ranging (Merton Truck) and the Red Brand Canners Case

**Session file:** DSM-109-7_2026-11-11_Amit-Kumar-Vatsa
**Course:** Mathematical Programming / Operations Research (graduate)

---

## 1. Overview

The session finishes the **Merton Truck** sensitivity-analysis discussion. Earlier classes covered the optimal solution, shadow prices and reduced costs. The remaining piece was the **allowable increase and allowable decrease of objective-function coefficients**. The instructor first shows in Excel Solver that pushing the Model 101 profit coefficient past its allowable increase moves the optimum to a different corner point. He then explains the result graphically: the objective line's slope must stay between the slopes of the binding constraints. Using this, he derives the ranges algebraically, $2500 \le c_1 \le 5000$ and $3000 \le c_2 \le 6000$. Next he gives the origin of the term **"reduced cost"** through Dantzig's **diet problem** and recaps **shadow price**. The second half opens the **Red Brand Canners** case. The class covers:

- the tomato supply and its quality grades;
- blending (mixture) constraints for each product;
- two competing cost calculations, Cooper's (Exhibit 2) and Myers's (Exhibit 3).

The main conclusion is that **both approaches are flawed**. The tomato purchase is a **sunk cost** and should not drive the product-mix decision. The real economic value of grade A tomatoes should come from the **shadow price** of the grade A supply constraint in an LP. Formulating and solving the LP is deferred to the next class.

---

## 2. Topics Covered (in teaching order)

### 2.1 Recap from the previous class

- **Shadow price:** the change in the optimal objective value per unit increase in a constraint's right-hand side (RHS). It is the marginal worth of one more unit of a resource. It tells you how much it is worth paying to relieve or add capacity to a constraint (useful in negotiations, e.g., with workers).
- **Reduced cost:** for a variable at zero in the optimal solution, the change in the optimal objective if that variable is forced to take one unit.
  - Equivalently, it is how much that variable's objective coefficient must improve before it enters the optimal solution.
  - In Merton Truck, **Model 103** had a reduced cost of $-350$. Forcing production of one unit of Model 103 lowers total profit by 350, so Model 103 is loss-making at the margin.
  - Models 101 and 102 ($x_1, x_2$) are both positive in the optimum, so their reduced cost is $0$.
  - Adding a constraint such as $x_1 \ge 1$ would be **redundant** (already satisfied), which is consistent with a reduced cost of $0$.

### 2.2 Allowable increase/decrease of objective coefficients: Merton Truck

#### The model (two-variable version used for the graph)

> **Flag:** The objective coefficients (3000, 5000) and the constraint coefficient ratios (engine assembly $1:2$, metal stamping $2:2$) were stated in class. The RHS values and the two department-capacity constraints are **inferred from the standard Merton Truck case**. They reproduce every corner point quoted in class, $(2000, 1000)$ and $(2500, 500)$. Model 103 ($x_3$) was in the Excel model but is $0$ at the optimum, so the graph uses only $x_1, x_2$.

**Decision variables**
- $x_1$ = number of Model 101 trucks produced per month (trucks)
- $x_2$ = number of Model 102 trucks produced per month (trucks)

**Model**

$$
\begin{aligned}
\max\quad & Z = 3000\,x_1 + 5000\,x_2 && \text{(total contribution, in dollars per month)}\\
\text{s.t.}\quad & x_1 + 2x_2 \le 4000 && \text{(engine assembly hours)}\\
& 2x_1 + 2x_2 \le 6000 && \text{(metal stamping hours)}\\
& 2x_1 \le 5000 && \text{(Model 101 assembly hours)}\\
& 3x_2 \le 4500 && \text{(Model 102 assembly hours)}\\
& x_1,\ x_2 \ge 0
\end{aligned}
$$

#### Feasible region and corner points (graphical solution)

The feasible region is a convex polygon in the first quadrant. It is bounded by:
- the axes;
- the line $x_2 = 1500$ (Model 102 assembly);
- the engine assembly line $x_1 + 2x_2 = 4000$;
- the metal stamping line $x_1 + x_2 = 3000$;
- the line $x_1 = 2500$ (Model 101 assembly).

Corner-point labels C, D, E are as used in class; A, B, F are inferred.

| Corner | $(x_1, x_2)$ | Binding constraints | $Z = 3000x_1 + 5000x_2$ |
|---|---|---|---|
| A | $(0, 0)$ | non-negativity | $0$ |
| B | $(0, 1500)$ | $x_1 \ge 0$, Model 102 assembly | $7{,}500{,}000$ |
| C | $(1000, 1500)$ | Model 102 assembly, engine assembly | $10{,}500{,}000$ |
| **D** | **$(2000, 1000)$** | **engine assembly, metal stamping** | **$11{,}000{,}000$ (optimal)** |
| E | $(2500, 500)$ | metal stamping, Model 101 assembly | $10{,}000{,}000$ |
| F | $(2500, 0)$ | Model 101 assembly, $x_2 \ge 0$ | $7{,}500{,}000$ |

**Optimum:** corner D, $x_1 = 2000$, $x_2 = 1000$, $Z = 11{,}000{,}000$.

#### Excel/Solver demonstration (numbers used)

- The Solver sensitivity report shows the coefficient of $x_1$ = 3000 with **allowable increase = 2000**.
- Change the coefficient of $x_1$ to **4999**. Re-solving still gives D = $(2000, 1000)$ as optimal.
- Change it to **5001**. The optimum moves to **E = $(2500, 500)$**.
  - Check at $c_1 = 5001$: $Z_E = 2500(5001) + 500(5000) = 15{,}002{,}500$.
  - This exceeds $Z_D = 2000(5001) + 1000(5000) = 15{,}002{,}000$.
- **Definition:** the allowable increase/decrease of an objective coefficient is how far that single coefficient can change, **one at a time, others held fixed**, while the current corner point stays optimal.
  - The optimal *solution* (the corner point) stays the same within this range.
  - The optimal *objective value* does change.

#### Graphical intuition

- Raising $c_1$ (Model 101 more profitable) makes the iso-profit line **steeper**.
  - D stays optimal for a while, which shows the solution has some robustness.
  - When the objective line becomes parallel to segment DE (the metal stamping line), D and E are **both** optimal.
  - Any steeper, and E alone is optimal.
- Making the line **flatter**:
  - D stays optimal until the line is parallel to CD (the engine assembly line), where C and D are both optimal.
  - Any flatter, and C becomes optimal.
- **Rule:** the current corner point stays optimal as long as the slope of the objective-function line lies **between the slopes of the binding constraints** at that corner. Here the binding constraints are engine assembly and metal stamping.

#### Algebraic derivation using coefficient ratios

Use coefficient ratios (coefficient of $x_1$ : coefficient of $x_2$) instead of slopes:
- Engine assembly: $1:2 = \tfrac{1}{2}$ (slope $-\tfrac12$)
- Metal stamping: $2:2 = 1$ (slope $-1$)
- Objective: $3000:5000 = 0.6$, which lies between $0.5$ and $1$, confirming D is optimal.

**Range for $c_1$** (replace 3000 by $k$):

$$\frac{1}{2} \le \frac{k}{5000} \le \frac{2}{2} \;\;\Longrightarrow\;\; 2500 \le k \le 5000$$

- Allowable increase $= 5000 - 3000 = 2000$. This is why 4999 kept D optimal and 5001 did not.
- Allowable decrease $= 3000 - 2500 = 500$.

**Range for $c_2$** (replace 5000 by $k'$):

$$\frac{1}{2} \le \frac{3000}{k'} \le \frac{2}{2}$$

Taking reciprocals reverses the inequalities:

$$2 \ge \frac{k'}{3000} \ge 1 \;\;\Longrightarrow\;\; 6000 \ge k' \ge 3000$$

- Allowable increase $= 6000 - 5000 = 1000$.
- Allowable decrease $= 5000 - 3000 = 2000$.

#### Summary of Merton Truck lessons

- The optimal solution is not the only output that matters. Sensitivity analysis (shadow prices, reduced costs, ranges) supports:
  - negotiation over constraint capacities;
  - judging which alternative products are loss-making.
- Fixed costs should be kept separate and not allocated to products when making the product-mix decision.

### 2.3 Where the term "reduced cost" comes from: the diet problem

- **George Dantzig** (ASR: "Tansik", "Josh Nansik") worked for the US Air Force at the Pentagon. One early problem was how to feed soldiers at minimum cost.
- **Generic diet model**

  Decision variables: $x_j$ = number of servings of food item $j$ (eggs, milk, maize, ...), in servings per person.

  Data:
  - $c_j$ = cost per serving of food $j$;
  - $a_{ij}$ = amount of nutrient $i$ per serving of food $j$;
  - $L_i, U_i$ = minimum and maximum requirement of nutrient $i$ (calories, protein, minerals, vitamins, ...).

$$
\begin{aligned}
\min\quad & \sum_j c_j x_j && \text{(cost of one person's diet)}\\
\text{s.t.}\quad & \sum_j a_{ij} x_j \ge L_i \quad \forall i && \text{(minimum nutrient requirement)}\\
& \sum_j a_{ij} x_j \le U_i \quad \forall i && \text{(maximum nutrient requirement)}\\
& x_j \ge 0 \quad \forall j
\end{aligned}
$$

- **Interpretation:** suppose milk has $0$ servings in the optimal diet. Milk is not a cheap enough source of its nutrients, because other foods supply them more cheaply.
  - The **reduced cost** of milk is how much milk's cost per serving must **reduce** before milk enters the optimal diet. Hence the name.
  - Equivalently, it is the change in the optimal objective if one serving of milk is forced into the diet.

### 2.4 Red Brand Canners (RBC) case

ASR rendered the name as "red brand canvas". The case was opened by student Raj: RBC must choose a product mix and resource allocation, and its executives disagree on how to do it.

#### Business problem and data

- **Products of interest (tomato products only):** canned whole tomatoes, tomato juice, tomato paste. Peach and apple products in the exhibits are ignored.
- **Raw material:**
  - 3,000,000 lb of tomatoes, contracted with growers at an average delivered price of **18 cents/lb**.
  - Total spend: $3{,}000{,}000 \times 0.18 = 540{,}000$ dollars.
- **Quality mix:**

| Grade | Share | Quantity (lb) | Quality rating (0–10 scale) |
|---|---|---|---|
| A (premium) | 20% | 600,000 | 9 |
| B | 80% | 2,400,000 | 5 |

- **Product requirements (from Exhibit 2):**

| Product | Minimum average rating | lb per case | Demand forecast* | Cooper fruit cost per case |
|---|---|---|---|---|
| Whole tomatoes | 8 | 18 | 800,000 | $18 \times 0.18 = 3.24$ |
| Juice | 6 | 20 | 50,000 | $20 \times 0.18 = 3.60$ |
| Paste | 5 (no real restriction) | 25 | 80,000 | $25 \times 0.18 = 4.50$ |

\*The instructor read the demand figures as "pounds". In the RBC case the demand forecasts are in **cases**: 800,000, 50,000 and 80,000 cases. Verify against your exhibit.

- **Additional offer:** RBC can buy another **80,000 lb of grade A** at **25.5 cents/lb**. Whether to accept will be decided later via the shadow price.

#### Blending (quality) constraints: mixtures and alligation

Assume ratings blend linearly (weighted average).

**Whole tomatoes (need rating $\ge 8$):**
- Alligation view: A (9) is 1 unit from 8, and B (5) is 3 units from 8. So $A : B \ge 3 : 1$.
- Rigorous view: let $A : B = \lambda : 1$. Then

$$\frac{9\lambda + 5(1)}{\lambda + 1} \ge 8 \;\Longrightarrow\; 9\lambda + 5 \ge 8\lambda + 8 \;\Longrightarrow\; \lambda \ge 3$$

- So grade A must be at least 75% and grade B at most 25% of the mix.

**Juice (need rating $\ge 6$):** distances are 3 (from A) and 1 (from B), so

$$\frac{9\lambda+5}{\lambda+1} \ge 6 \;\Longrightarrow\; 9\lambda + 5 \ge 6\lambda + 6 \;\Longrightarrow\; \lambda \ge \tfrac{1}{3}$$

- So grade A must be at least 25% and grade B at most 75%.

**Paste (need rating $\ge 5$):** it can be made entirely from grade B, so no quality constraint is needed.

#### Cooper's calculation (Exhibit 2): quantity only

- Fruit cost = 18 cents/lb × lb per case, regardless of grade.
- Example, whole tomatoes: $0.18 \ \tfrac{\text{dollars}}{\text{lb}} \times 18 \ \tfrac{\text{lb}}{\text{case}} = 3.24$ dollars per case.
- Whole-tomato contribution per case:
  - Selling price is 12.00.
  - Variable costs are direct labour (about 3.54; ASR said "3.4"), variable overhead, variable selling (e.g., sales commissions), packaging material, and fruit (3.24).
  - Total variable cost is **10.80**, so contribution is $12 - 10.80 = 1.20$.
- Allocated fixed overhead is shown below this line but should be ignored, as in Merton Truck.
- Direct labour can be variable if labour is contractual or paid hourly. Variable selling and packaging rise with each additional case.
- Implied margin before fruit cost: $12.00 - (10.80 - 3.24) = 4.44$ (the instructor said "4.4").

#### Myers's calculation (Exhibit 3): quality-weighted fruit cost

Myers argues that grade A is premium and should carry a higher cost per lb. Let $Z$ = cost per lb of grade A and $Y$ = cost per lb of grade B (dollars). He uses two equations.

1. **Total spend is preserved:**
$$600{,}000\,Z + 2{,}400{,}000\,Y = 3{,}000{,}000 \times 0.18 = 540{,}000$$

2. **Cost proportional to quality rating:**
$$\frac{Z}{9} = \frac{Y}{5}$$

**Solution:** set $Z = 9t$ and $Y = 5t$. Then $5{,}400{,}000t + 12{,}000{,}000t = 540{,}000$, so $t \approx 0.031034$. This gives:
- $Z \approx 0.2793$ dollars/lb (about 27.93 cents);
- $Y \approx 0.1552$ dollars/lb (about 15.52 cents).

They average 18 cents over the whole crop.

> **Flag:** The instructor wrote $0.2796$ and $0.1554$. The exact solution of these equations is $0.2793$ and $0.1552$. Both round to the same per-case costs.

**Myers fruit costs per case:**
- Whole tomatoes (75% A, 25% B): $18\,[0.75(0.2793) + 0.25(0.1552)] \approx 4.47$ (vs Cooper 3.24).
- Juice (25% A, 75% B): $20\,[0.25(0.2793) + 0.75(0.1552)] \approx 3.72$ (vs Cooper 3.60).
  - The change is small because the 25:75 recipe is close to the crop's 20:80 availability.
- Paste (100% B): $25 \times 0.1552 \approx 3.88$, shown as about 3.9 (vs Cooper 4.50).
  - This is a big drop because paste uses only cheap grade B.

**Myers's conclusion:** whole tomatoes now earn $4.44 - 4.47 = -0.03$ dollars per case, a 3-cent loss. Since revenue no longer covers variable cost, he says: don't produce canned whole tomatoes. Use grade A for juice, and make paste.

#### Class discussion: who is right?

- **Neha (Singasami):** Myers is more logical because he considers quality as well as quantity.
- **Another student:** the premium concept is fine, but dividing cost in proportion to the rating ratio is a made-up allocation rule.
- **Instructor's critique of Myers (a self-defeating spiral):**
  1. If whole tomatoes are dropped, all grade A goes into juice.
  2. Juice's recipe then shifts above 25% A, so its fruit cost inflates too, and juice may look unprofitable.
  3. If juice is also dropped, grade A, the best raw material, has no use and gets "thrown down the drain".
  4. The artificially inflated grade A cost makes every product that uses grade A look unprofitable.
- **Student diagnosis (accepted):**
  - **Cooper** ignored that grade A is **scarce** (only 600,000 lb).
  - **Myers** ignored that the 18 cents/lb is **already committed (sunk)** and should not drive the decision.
  - Both approaches are **incorrect**. The question is not whether one is "optimal" but whether the reasoning is right.

#### Analogies used

- **Expensive expert in a software product company** (instructor's example):
  - A VP hires a costly expert to contribute across products.
  - Each product manager refuses the expert's hours because charging that salary makes their product's P&L look red.
  - The expert ends up "on the bench" while the company still pays the salary.
  - The error: the salary is **sunk/fixed** for the organisation, irrespective of which product uses the person. Allocating it in short-term tactical or operational decisions leads to wasting the resource.
- **Rahul's experience:** "practice area leads" were charged to projects as a fractional overhead (e.g., 0.25). The instructor relates this to Merton Truck's fixed overhead:
  - Loading it onto one product makes that product look unprofitable.
  - Spreading it may be acceptable for long-term strategic accounting, but not for short-term tactical decisions.

#### Correct way to think about it

- RBC contracted in May to buy the growers' crop at 18 cents/lb, and grading happened afterwards. **That money is sunk.** How to split it between grades A and B is a meaningless question for the product-mix decision.
- What matters is the **economic value of grade A to the business**. The best use of grade A is whole tomatoes, which need at least 75% A.
- **Use sensitivity analysis.** Put supply constraints in the LP (grade A $\le 600{,}000$ lb, grade B $\le 2{,}400{,}000$ lb). The **shadow price** of the grade A constraint gives the profit gain per extra lb of grade A.
  - If the shadow price is **> 25.5 cents/lb**, buy the extra 80,000 lb.
  - If it is lower (e.g., 23 cents), don't buy.
- **General principle:**
  - Variable costs don't allow "accounting tricks", since each extra unit genuinely incurs them.
  - Apportioning fixed or sunk costs across products or raw materials distorts decisions.

#### Preview: likely LP formulation (to be done next class)

> **Flag:** This model was **not written in class**. It is a sketch consistent with the data discussed, to help you prepare. The per-lb margins $m_W, m_J, m_P$ = (selling price − non-fruit variable cost) / (lb per case). Only $m_W = 4.44/18 \approx 0.2467$ dollars/lb is implied by lecture numbers. Take $m_J$ and $m_P$ from Exhibit 2. Fruit cost is excluded because it is sunk.

**Decision variables** (lb of tomatoes used):
- $x_{WA}, x_{WB}$: grade A and B used in whole tomatoes
- $x_{JA}, x_{JB}$: grade A and B used in juice
- $x_{PA}, x_{PB}$: grade A and B used in paste

$$
\begin{aligned}
\max\quad & m_W(x_{WA}+x_{WB}) + m_J(x_{JA}+x_{JB}) + m_P(x_{PA}+x_{PB})\\
\text{s.t.}\quad & x_{WA}+x_{JA}+x_{PA} \le 600{,}000 && \text{(grade A supply)}\\
& x_{WB}+x_{JB}+x_{PB} \le 2{,}400{,}000 && \text{(grade B supply)}\\
& x_{WA} - 3x_{WB} \ge 0 && \text{(whole tomatoes: avg rating } \ge 8)\\
& 3x_{JA} - x_{JB} \ge 0 && \text{(juice: avg rating } \ge 6)\\
& x_{WA}+x_{WB} \le 800{,}000 \times 18 && \text{(whole-tomato demand, lb)}\\
& x_{JA}+x_{JB} \le 50{,}000 \times 20 && \text{(juice demand, lb)}\\
& x_{PA}+x_{PB} \le 80{,}000 \times 25 && \text{(paste demand, lb)}\\
& x_{WA},x_{WB},x_{JA},x_{JB},x_{PA},x_{PB} \ge 0
\end{aligned}
$$

The rating constraints are linearised versions of $\dfrac{9x_{WA}+5x_{WB}}{x_{WA}+x_{WB}} \ge 8$ and $\dfrac{9x_{JA}+5x_{JB}}{x_{JA}+x_{JB}} \ge 6$.

---

## 3. Formula Sheet

- **Optimality range (two variables):** a corner point stays optimal while
$$\text{(ratio of the flatter binding constraint)} \le \frac{c_1}{c_2} \le \text{(ratio of the steeper binding constraint)}$$
  - Merton Truck: $\dfrac{1}{2} \le \dfrac{c_1}{c_2} \le 1$.
- **Merton Truck ranges:**
  - $2500 \le c_1 \le 5000$ (allowable increase 2000, decrease 500).
  - $3000 \le c_2 \le 6000$ (allowable increase 1000, decrease 2000).
- **Blending rule:** with $A:B = \lambda:1$,
$$\frac{9\lambda + 5}{\lambda + 1} \ge r$$
  - $r = 8$ gives $\lambda \ge 3$ (A at least 75%).
  - $r = 6$ gives $\lambda \ge \tfrac13$ (A at least 25%).
- **Myers's cost split:**
$$600{,}000Z + 2{,}400{,}000Y = 540{,}000, \qquad \frac{Z}{9} = \frac{Y}{5}$$
  This gives $Z \approx 0.2793$ and $Y \approx 0.1552$ dollars/lb.
- **Buy-extra-grade-A rule:** buy if $\text{shadow price}_{A} > 0.255$ dollars/lb.

---

## 4. Flagged for Exams, Assignments and Next Class

- **Come prepared:** read cases before class. The instructor stressed that case sessions depend on participation, and few students had read RBC.
- **Know how to compute allowable increase/decrease by hand** (ratio-of-coefficients method) and how to read it from the Solver sensitivity report. Remember that it applies one coefficient at a time.
- **Know the meanings and interpretations** of reduced cost (including the diet-problem story) and shadow price.
- **Key conceptual takeaway for RBC:** sunk or fixed costs must not be allocated in tactical product-mix decisions. Explain why both Cooper and Myers are wrong.
- **Next class:** formulate RBC as an LP, solve it, and use shadow prices to decide whether to buy 80,000 lb of extra grade A at 25.5 cents/lb.

---

## 5. ASR Corrections and Inferences

**ASR corrections**
- "Murtantrak / Martin Troy / Merton truck" → **Merton Truck** case
- "red brand canvas" → **Red Brand Canners**
- "Tansik / Josh Nansik", "Pentagan" → **George Dantzig**, **Pentagon**
- "Koopa" → **Cooper**
- "Jews / jums / pace" → **juice / paste**
- "allow vapor increase" → **allowable increase**
- "4 trip a line" → **4999**
- "5000 1" → **5001**
- "sum cost" → **sunk cost**
- "gradient grade B" → **grade A and grade B**
- "$1.18 per pound" → **0.18 dollars per pound**
- "28%" → **25%** (grade B share for whole tomatoes)

**Inferred values**
- Merton Truck RHS values and department-assembly constraints.
- Corner labels A, B, F.
- Exact Myers costs (27.93 / 15.52 cents vs. the stated 27.96 / 15.54).
- Demand units (cases).
- Direct labour value (3.54).
- The preview LP.

<!-- nav -->
← [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
