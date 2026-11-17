---
course: DSM 109
date: 2026-11-13
start: 7:00pm
session: "8"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-109 Session 8: Red Brand Canners (Solution and Sensitivity) and an Introduction to Shadow-Price Signs

*Session file: DSM-109-8_2026-11-13_Amit-Kumar-Vatsa*

---

## 1. Overview

This session completes the **Red Brand Canners** case started in the previous class. It first settles the cost debate: the tomatoes were already bought in bulk at 18¢/lb, so they are a **sunk (fixed) cost**, not a variable cost. The tomato cost is therefore left out of the per-case contributions. The instructor then:

- formulates a 6-variable linear program (pounds of grade A and grade B tomatoes going to each of three products),
- solves it in Excel Solver (Simplex LP),
- interprets the sensitivity report: shadow prices of the supply, demand and quality constraints, allowable increase, and reduced cost.

This leads to concrete business decisions:

- whether to buy an extra 80,000 lb of grade A at 25.5¢/lb,
- how to cap a marketing budget for paste,
- why Myers' "implied cost" accounting split is meaningless.

The session ends with a small two-variable graphical example. It shows why, in a **maximization** problem:

- a $\le$ constraint's shadow price can never be negative,
- an equality constraint's shadow price can be negative.

This sets up the next class on duality and dual variables.

---

## 2. Topics Covered (in order taught)

### 2.1 Sunk cost vs. variable cost (recap and resolution)

- 3,000,000 lb of tomatoes had already been procured at 18¢/lb, so the total spend is $3{,}000{,}000 \times \$0.18 = \$540{,}000$.
- **Test for a variable cost:** *"If I don't produce a single unit of any product, does this cost disappear?"*
  - For the tomatoes, no. They are already paid for.
  - So the tomato cost is a **fixed / sunk cost** and must **not** be subtracted when computing contribution.
- **Definition.** Contribution per case is the selling price minus all *variable* costs:
  $$\text{Contribution per case} = \text{Selling price per case} - \text{Variable costs per case}$$
- Contributions per case, excluding tomato cost (Exhibits 2 and 3 agree on these):

| Product | Contribution (\$/case) | lb per case | Contribution (\$/lb) |
|---|---|---|---|
| Whole tomatoes (product 1) | 4.44 | 18 | $4.44/18 \approx 0.2467$ |
| Juice (product 2) | 3.96 | 20 | $3.96/20 = 0.198$ |
| Paste (product 3) | 5.55 | 25 | $5.55/25 = 0.222$ |

### 2.2 Case data used in the model

| Item | Value |
|---|---|
| Grade A available | 600,000 lb |
| Grade B available | 2,400,000 lb |
| Demand: whole tomatoes | 800,000 cases ($= 14{,}400{,}000$ lb) |
| Demand: juice | 50,000 cases ($= 1{,}000{,}000$ lb) |
| Demand: paste | 80,000 cases ($= 2{,}000{,}000$ lb) |
| Quality rule: whole tomatoes | $A : B \ge 3 : 1$ (derived in the previous class by alligation) |
| Quality rule: juice | $A : B \ge 1 : 3$ |
| Quality rule: paste | No minimum; all grade B is acceptable |
| Extra grade A on market | 80,000 lb at 25.5¢/lb |

### 2.3 LP formulation (full standard form)

**Decision variables** (all in **pounds**):

- $x_{A1}$, $x_{B1}$: lb of grade A / grade B used for **whole tomatoes**
- $x_{A2}$, $x_{B2}$: lb of grade A / grade B used for **juice**
- $x_{A3}$, $x_{B3}$: lb of grade A / grade B used for **paste**

A student suggested dropping $x_{A3}$, because paste can be made entirely from grade B. The instructor kept it deliberately: using grade A in paste is *not prohibited*, so "let Solver decide." Solver did set it to 0.

**Objective.** Maximize total contribution in dollars, excluding the sunk tomato cost. Units cancel as \$/case $\times$ case/lb $\times$ lb = \$.

$$\max\; Z = \frac{4.44}{18}\,(x_{A1}+x_{B1}) + \frac{3.96}{20}\,(x_{A2}+x_{B2}) + \frac{5.55}{25}\,(x_{A3}+x_{B3})$$

**Supply constraints** (lb):

$$x_{A1}+x_{A2}+x_{A3} \le 600{,}000 \quad \text{(grade A available)}$$
$$x_{B1}+x_{B2}+x_{B3} \le 2{,}400{,}000 \quad \text{(grade B available)}$$

**Demand constraints.** Cases are converted to lb so both sides have the same units.

$$x_{A1}+x_{B1} \le 800{,}000 \times 18 \quad \text{(whole tomatoes)}$$
$$x_{A2}+x_{B2} \le 50{,}000 \times 20 \quad \text{(juice)}$$
$$x_{A3}+x_{B3} \le 80{,}000 \times 25 \quad \text{(paste)}$$

- Using $\le$ is safe here because this is *profit maximization*: the model will meet as much demand as is profitable.
- In a cost-minimization problem, $\le$ demand constraints would give the trivial answer "produce nothing."

**Quality (ratio) constraints, linearized.** The ratio form is non-linear. Moving every variable to the left-hand side makes it linear:

$$\frac{x_{A1}}{x_{B1}} \ge 3 \;\Rightarrow\; x_{A1} - 3x_{B1} \ge 0 \quad \text{(whole tomatoes)}$$
$$\frac{x_{A2}}{x_{B2}} \ge \frac{1}{3} \;\Rightarrow\; 3x_{A2} - x_{B2} \ge 0 \quad \text{(juice)}$$

**Non-negativity:**

$$x_{A1}, x_{B1}, x_{A2}, x_{B2}, x_{A3}, x_{B3} \ge 0$$

This gives 7 constraints in total (2 supply + 3 demand + 2 quality) plus non-negativity. No integrality is needed, because pounds are continuous.

### 2.4 Excel Solver set-up

1. **Variable cells:** six cells, coloured yellow, for $x_{A1},\dots,x_{B3}$.
2. **Objective coefficients:** entered as $4.44/18$, $4.44/18$, $3.96/20$, $3.96/20$, $5.55/25$, $5.55/25$.
3. **Objective cell** (coloured blue): `SUMPRODUCT(coefficients, variable cells)`, with `$` absolute references so the formula can be copied to the constraint rows.
4. **Constraint rows:** each left-hand side is a SUMPRODUCT of its coefficient row with the variable cells.
5. **Solver settings:**
   - Set Objective: the total contribution cell, set to **Max**.
   - By Changing Variable Cells: the yellow cells.
   - Constraints: all five $\le$ constraints added in one block; both $\ge$ quality constraints added in another block (right-hand side 0).
   - Make unconstrained variables non-negative (inferred, standard setting).
   - Solving method: **Simplex LP**.
6. Generate the **Sensitivity Report**.

### 2.5 Optimal solution

As stated in class: about 700,000 lb goes to whole tomatoes, 300,000 lb to juice, 2,000,000 lb to paste, and $x_{A3}=0$.

The split by grade below was not read out in class. It is my reconstruction: both supplies, paste demand and both ratio constraints are binding. It is consistent with all the numbers shown.

| Variable | Value (lb) |
|---|---|
| $x_{A1}$ | 525,000 |
| $x_{B1}$ | 175,000 |
| $x_{A2}$ | 75,000 |
| $x_{B2}$ | 225,000 |
| $x_{A3}$ | 0 |
| $x_{B3}$ | 2,000,000 |

Objective value (my calculation; the figure was shown on screen, not read out):

$$Z^* = 700{,}000(0.24667) + 300{,}000(0.198) + 2{,}000{,}000(0.222) \approx \$676{,}067$$

Profit after the sunk tomato cost:

$$\$676{,}067 - \$540{,}000 \approx \$136{,}067 \;(>0)$$

So the plan is still profitable after the sunk cost.

### 2.6 Sensitivity analysis: shadow prices

**Definition.** The **shadow price** of a constraint is the change in the optimal objective value per one-unit increase in that constraint's right-hand side. It is valid within the allowable increase/decrease range.

**Grade A supply: shadow price \$0.271/lb (binding: all 600,000 lb used).**

- Meaning: one extra pound of grade A, received free, raises contribution by 27.1¢.
- **Experiment:** the right-hand side was raised by 100 lb and the model re-optimized. Contribution rose by exactly \$27.10.
- **Puzzle:** no product earns 27.1¢/lb. The best is whole tomatoes at about 24.67¢/lb. So why is the shadow price higher?
- **Explanation: the product mix shifts.**
  - Whole tomatoes went from 700,000 to 700,150 (+150 lb).
  - Juice went from 300,000 to 299,950 (−50 lb).
  - Paste was unchanged.
  - Net effect: $150(0.24667) - 50(0.198) = 37.00 - 9.90 = \$27.10$.
  - The extra grade A lets some grade B move from juice into whole tomatoes while still meeting both ratio rules.

**Grade B supply: shadow price about \$0.173/lb.**

- Grade A is more valuable to the business than grade B.

**Willingness to pay.** Shadow prices exclude the tomato cost. So the most you should pay for an extra pound of each grade is:

- grade A: less than 27.1¢/lb,
- grade B: less than 17.3¢/lb.

These are the ceiling rates for paying farmers for extra supply.

**Business decision: extra grade A offer.**

- The offer is 80,000 lb of grade A at 25.5¢/lb.
- Allowable increase for grade A supply is 600,000 lb, and $80{,}000 < 600{,}000$, so the shadow price stays valid.
- Since $25.5 < 27.1$¢, **buy it**.
- Net gain (my calculation): $80{,}000 \times (0.271 - 0.255) \approx \$1{,}280$.

**Demand constraints.**

- **Whole tomatoes and juice:** shadow price 0. These constraints are not binding.
  - Do **not** spend on advertising to raise their demand. You cannot even meet current demand.
- **Paste:** shadow price \$0.0483/lb. Paste demand is binding: all 2,000,000 lb is produced.
  - One extra lb of paste demand adds about 4.83¢.
  - Marketing question: if \$0.05 of marketing raises paste demand by 1 lb, should you do it? **No**, because $5¢ > 4.83¢$.
  - So the marketing spend per extra pound of paste demand must stay below about 4.83¢. This is how the shadow price guides a marketing budget.

**Quality (ratio) constraints.**

- Their shadow prices are negative. The values were not read out; my calculation gives about $-0.024$ each.
- They are hard to interpret in management terms (one unit of right-hand side means "one more pound of A beyond the 3:1 ratio"), so the instructor did not pursue them.
- **Observation (to be formalized next class):** in a max problem, $\le$ constraints never have negative shadow prices, but $\ge$ constraints can.

### 2.7 Sensitivity analysis: reduced cost

All reduced costs are 0 except for $x_{A3}$, which is the only variable at zero.

**Rule.** In a maximization problem, a non-basic variable (value 0) has a reduced cost that is $\le 0$.

$x_{A3}$ has reduced cost $\approx -0.097$. This has two meanings:

1. Forcing 1 lb of grade A into paste would *lower* contribution by about 9.7¢.
2. Its objective coefficient would have to rise by about 0.097 before $x_{A3}$ enters the optimal solution.

**Demonstration:**

- The instructor added 0.098 to $x_{A3}$'s coefficient and re-solved. $x_{A3}$ became positive.
- The solution then sent much grade A into paste, and whole-tomato production dropped to zero.
- The change was then reverted.

### 2.8 Case takeaways

- The real issue in the case was the tomato cost, which is **sunk**.
- Allocating it across grade A and grade B (Myers' "implied cost" approach) is a meaningless accounting exercise.
- Myers' implied costs were about 27.96¢ (A) and about 15.5¢ (B). The B figure is unclear in the audio: it was heard as both "15.54" and "15.90."
- These were close to the shadow prices of 27.1¢ and 17.3¢, but the instructor called the similarity "an accident."
- The **shadow price is the meaningful measure**: it gives the value of each grade to the business and the maximum rate worth paying for more of it.
- Grade B is worth more than Myers calculated.

### 2.9 Mini-example: when can shadow prices be negative?

**Problem (version 1):**

$$\max\; z = 20x_1 + x_2$$
$$\text{s.t.}\quad x_1 + x_2 \le 10 \quad \text{(constraint 1, shadow price } u_1)$$
$$\phantom{\text{s.t.}\quad} x_2 \le 4 \quad \text{(constraint 2, shadow price } u_2)$$
$$x_1, x_2 \ge 0$$

Here $x_1$ is the highly profitable product.

**Graphical solution:**

- The feasible region is bounded by the axes, the line $x_1+x_2=10$, and the horizontal line $x_2=4$.
- Corner points and objective values:

| Corner | $(x_1, x_2)$ | $z$ |
|---|---|---|
| A | (0, 0) | 0 |
| B | (0, 4) | 4 |
| C | (6, 4) | 124 |
| D | (10, 0) | **200** |

- The objective line is very steep (it heavily favours $x_1$), so the optimum is **D**: $x_1^*=10$, $x_2^*=0$, $z^*=200$.

**Shadow prices for version 1:**

- $u_1 = 20$. Raising the right-hand side to 11 moves the optimum to $(11, 0)$, so $z$ rises by 20.
- $u_2 = 0$. Moving $x_2 \le 4$ does not affect corner D.
- More of resource 2 does not help, but it does not hurt either.

**Problem (version 2): constraint 2 changed to an equality, $x_2 = 4$.**

- The resource must now be fully consumed.
- The feasible region shrinks to the **line segment BC**.
- The optimum is **C**: $x_1^*=6$, $x_2^*=4$, $z^*=124$.

**Shadow prices for version 2:**

- $u_1 = 20$. With $x_2$ fixed at 4, $x_1$ rises to 7 and $z = 144$.
- $u_2 = -19$. With $x_2 = 5$, $x_1 = 5$ and $z = 100 + 5 = 105$. That is a change of $105 - 124 = -19$.
  - The audio says "shadow price is 19," but the sign is **negative**.

**Intuition.** Think of resource 2 as something undesirable (obnoxious, smelly, reactive) that *must* be used up. Only the low-profit product $x_2$ consumes it. More of it forces more $x_2$, which pushes out the profitable $x_1$, so profit falls.

**Bottom line (maximization problem):**

- **$\le$ constraint:** you may leave extra resource unused, so you never "complain."
  $$u_i \ge 0$$
- **$=$ constraint:** you are forced to use the resource, so the shadow price can be **positive or negative** (unrestricted in sign).
- **$\ge$ constraint:** the shadow price is $\le 0$. This was seen in the Red Brand Canners ratio constraints and will be formalized next class.

### 2.10 Student Q&A (end of class)

**Q:** Juice market demand is 1,000,000 lb, but only 300,000 lb is made. To meet it, should we buy extra grade B?

**A:**

- Juice demand is **not the bottleneck**; its shadow price is 0.
- The bottlenecks are the two supply constraints and paste demand.
- Relieve those first. Juice demand might become binding only later.
- Shadow prices hold only within the **allowable increase**. Beyond it, another constraint becomes binding and the shadow price changes. So you will not keep gaining about 17.3¢ for every extra pound of grade B indefinitely.

---

## 3. Exam / Assignment Pointers

No specific exam item was announced. The instructor stressed these as the key skills:

- **Sunk vs. variable cost test:** "If I produce nothing, does the cost disappear?" Exclude sunk costs from contribution.
- **Unit consistency:** convert cases to pounds and keep \$/case $\times$ case/lb $\times$ lb consistent in both the objective and the constraints.
- **Linearizing ratio constraints:** turn $x_A/x_B \ge k$ into $x_A - kx_B \ge 0$.
- **Interpreting shadow prices with units**, and using them for decisions:
  - maximum price to pay for extra raw material,
  - whether to accept an offer (check it is within the **allowable increase**),
  - marketing budget ceilings.
- **Explaining a shadow price that exceeds every product's unit contribution** through the product-mix shift (+150 whole, −50 juice).
- **Reduced cost** of a zero variable in a max problem is $\le 0`; it is how much its coefficient must improve before the variable enters the solution.
- **Shadow price sign rules for maximization:** $\le$ gives $\ge 0$; $\ge$ gives $\le 0$; $=$ gives unrestricted.

**Upcoming agenda (about three sessions):**

- Next class: formalize shadow prices as **dual variables** and better understand reduced cost.
- Following sessions: **integer programming**.

---

**Flags on inferred or computed numbers:**

- The grade-by-grade split of the solution, $Z^*$, the after-tomato profit, the \$1,280 gain, and the ratio-constraint shadow prices were computed by me, not read out in class.
- Myers' grade B figure is unclear in the audio (heard as both "15.54" and "15.90").
- In the audio, "0.246" was garbled as "24.246," "1/3 shadow price" reads as "19" without its negative sign, and "27.1" was misheard once as "20.2."

<!-- nav -->
← [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
