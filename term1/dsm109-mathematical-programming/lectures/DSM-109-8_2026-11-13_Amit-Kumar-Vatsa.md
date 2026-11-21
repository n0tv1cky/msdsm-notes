---
course: DSM 109
date: 2026-11-13
start: 7:00pm
session: "8"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 9 (2026-11-16)](DSM-109-9_2026-11-16_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Session 8: Red Brand Canners (Formulation, Solver and Sensitivity) and the Signs of Shadow Prices

**Instructor:** Amit Kumar Vatsa  **Session file:** DSM-109-8_2026-11-13

---

## 1. Overview

This session finishes the **Red Brand Canners** case. The previous class showed that the dispute between managers was about how to cost tomatoes. The 3 million pounds were already bought at 18 cents/lb, so that cost is **fixed and sunk** and does not belong in the contribution per case. The class then:

- computed the contribution per case for whole tomatoes, juice and paste,
- built a 6-variable linear programme (LP) with supply, demand and quality (ratio) constraints, including how to linearise the ratio constraints,
- solved it in Excel Solver with Simplex LP and interpreted the Sensitivity Report:
  - shadow prices of grade A and grade B supply (the maximum price worth paying for extra tomatoes),
  - the shadow price of paste demand (a ceiling on the marketing budget),
  - the reduced cost of the unused variable.

The session closed with a small two-variable graphical example. It shows why a $\le$ constraint in a maximisation problem can never have a negative shadow price, while an equality constraint can. This leads into formal duality theory next class, followed by two classes on integer programming.

---

## 2. Topics Covered (in order taught)

### 2.1 Sunk cost vs. variable cost

- **Test for a variable cost:** "If I don't produce a single unit, does this cost disappear?"
  - The tomato cost is $3{,}000{,}000 \text{ lb} \times 0.18 \text{ dollars/lb} = 540{,}000$ dollars. It was paid as a bulk purchase.
  - It does **not** disappear if nothing is produced. It is therefore a **fixed / sunk cost** and must **not** be subtracted when computing contribution.
- **Contribution** = selling price − all *variable* costs. Tomato cost is excluded.

### 2.2 Contribution per case (from the case exhibits; Exhibits 2 and 3 agree once tomato cost is excluded)

| Product | Contribution (dollars/case) | lb per case | Contribution (dollars/lb) |
|---|---|---|---|
| Whole tomatoes (product 1) | $4.44$ | $18$ | $4.44/18 \approx 0.2467$ |
| Juice (product 2) | $3.96$ | $20$ | $3.96/20 = 0.198$ |
| Paste (product 3) | $5.55$ | $25$ | $5.55/25 = 0.222$ |

### 2.3 Case data used in the model

- **Supply** (total 3,000,000 lb):
  - grade A: $600{,}000$ lb
  - grade B: $2{,}400{,}000$ lb
- **Demand forecasts:**
  - whole tomatoes: $800{,}000$ cases
  - juice: $50{,}000$ cases
  - paste: $80{,}000$ cases
- **Quality requirements** (derived in the previous class by the alligation / weighted-average principle):
  - whole tomatoes: grade A to grade B ratio at least $3:1$
  - juice: grade A to grade B ratio at least $1:3$
  - paste: no quality restriction, so it can be made entirely from grade B
- **Extra purchase option:** $80{,}000$ lb of extra grade A is available in the market at $25.5$ cents/lb.

### 2.4 LP formulation

**Choosing decision variables.**
- A student suggested omitting $x_{A3}$, since paste can be made entirely from grade B.
- The instructor kept $x_{A3}$ deliberately: using grade A in paste is not prohibited, so "let Solver decide."
- Solver later set $x_{A3}=0$ on its own.

**Decision variables** (all in **pounds**):

- $x_{A1}$ = lb of grade A tomatoes used for whole tomatoes
- $x_{B1}$ = lb of grade B tomatoes used for whole tomatoes
- $x_{A2}$ = lb of grade A tomatoes used for juice
- $x_{B2}$ = lb of grade B tomatoes used for juice
- $x_{A3}$ = lb of grade A tomatoes used for paste
- $x_{B3}$ = lb of grade B tomatoes used for paste

**Objective.** In words, maximise total contribution. This is equivalent to maximising profit, because the fixed cost cannot be changed.

The units work out as (dollars/case) ÷ (lb/case) × lb = dollars:

```math
\max Z = \frac{4.44}{18}(x_{A1}+x_{B1}) + \frac{3.96}{20}(x_{A2}+x_{B2}) + \frac{5.55}{25}(x_{A3}+x_{B3}) \quad \text{(dollars)}
```

**Subject to:**

*Supply constraints (lb):*

```math
x_{A1}+x_{A2}+x_{A3} \le 600{,}000 \quad \text{(grade A available)}
```

```math
x_{B1}+x_{B2}+x_{B3} \le 2{,}400{,}000 \quad \text{(grade B available)}
```

*Demand constraints.* Cases are converted to lb so both sides are in pounds:

```math
x_{A1}+x_{B1} \le 800{,}000 \times 18 = 14{,}400{,}000 \quad \text{(whole tomatoes)}
```

```math
x_{A2}+x_{B2} \le 50{,}000 \times 20 = 1{,}000{,}000 \quad \text{(juice)}
```

```math
x_{A3}+x_{B3} \le 80{,}000 \times 25 = 2{,}000{,}000 \quad \text{(paste)}
```

- Using $\le$ for demand is fine in a profit-maximisation problem: if a product is profitable, the model will try to meet as much demand as possible.
- In a cost-minimisation problem, $\le$ demand constraints would give the trivial answer "produce nothing."

*Quality (ratio) constraints, linearised:*

- Whole tomatoes: $\dfrac{x_{A1}}{x_{B1}} \ge 3$ is non-linear. Multiply through and move everything to the left:

```math
x_{A1} - 3x_{B1} \ge 0
```
- Juice: $\dfrac{x_{A2}}{x_{B2}} \ge \dfrac{1}{3}$ is linearised the same way:

```math
3x_{A2} - x_{B2} \ge 0
```

*Non-negativity:*

```math
x_{A1},x_{B1},x_{A2},x_{B2},x_{A3},x_{B3} \ge 0
```

The model has 7 constraints: 2 supply, 3 demand and 2 quality.

### 2.5 Excel Solver setup

1. **Data and variable cells.**
   - Yellow cells hold the 6 decision variables.
   - The objective coefficients are entered as formulas: $=4.44/18$, $=3.96/20$, $=5.55/25$.
2. **Formulas.**
   - Objective cell (coloured blue): `SUMPRODUCT` of the coefficients and the variable cells, using `$` absolute references so the formula can be copied.
   - Each constraint gets a LHS cell (a `SUMPRODUCT` of its coefficients) next to its RHS.
3. **Solver dialog.**
   - Set Objective: the total-contribution cell. Choose **Max**.
   - By Changing Variable Cells: the yellow cells.
   - Constraints:
     - all five $\le$ constraints entered together as one block (LHS range $\le$ RHS range),
     - the two quality constraints entered together as $\ge$ RHS (= 0).
   - Make unconstrained variables non-negative: checked.
   - Solving method: **Simplex LP**.
   - Request the **Sensitivity Report**.

### 2.6 Optimal solution

The pounds per product were stated in class. The split by grade and the dollar totals below were computed from the model and **were not read out in class**.

| Product | Total lb | Grade A | Grade B |
|---|---|---|---|
| Whole tomatoes | $700{,}000$ | $x_{A1}=525{,}000$ | $x_{B1}=175{,}000$ |
| Juice | $300{,}000$ | $x_{A2}=75{,}000$ | $x_{B2}=225{,}000$ |
| Paste | $2{,}000{,}000$ | $x_{A3}=0$ | $x_{B3}=2{,}000{,}000$ |

- All 600,000 lb of grade A and all 2,400,000 lb of grade B are used.
- Paste demand is fully met. Whole-tomato and juice demand are **not** binding.
- Solver set $x_{A3}=0$: grade A should not go into paste.
- **Total contribution** (computed): $700{,}000(0.2467)+300{,}000(0.198)+2{,}000{,}000(0.222) \approx 676{,}067$ dollars.
- **Profit after tomato cost** (computed): $676{,}067 - 0.18\times 3{,}000{,}000 \approx 136{,}067$ dollars. The instructor noted that the plan "is profit-making even after subtracting tomato cost."

### 2.7 Sensitivity report: shadow prices

**Grade A supply: shadow price $\approx 0.271$ dollars/lb (27.1 cents).** All 600,000 lb are used.

- **Meaning:** one more pound of grade A, obtained free, raises total contribution by 27.1 cents.
- **Verification in class:**
  - The RHS was raised by 100 lb to 600,100 and the model re-optimised.
  - Contribution rose by exactly $100 \times 0.271 = 27.1$ dollars.
- **Puzzle:** the 27.1 cents exceeds every product's per-lb contribution (the highest is $0.2467$). Why?
  - With +100 lb of A, whole tomatoes went from $700{,}000$ to $700{,}150$ lb, an increase of **150**, not 100.
  - Juice went from $300{,}000$ to $299{,}950$ lb, a decrease of **50**.
  - Paste was unchanged.
  - The extra grade A lets grade B be **shifted** from juice into whole tomatoes, keeping the 3:1 ratio. So the gain comes from a change in product mix:

```math
150 \times 0.2467 - 50 \times 0.198 = 37.0 - 9.9 = 27.1 \text{ dollars}
```

**Grade B supply: shadow price $\approx 0.173$ dollars/lb (17.3 cents).** Grade A is more valuable to the business than grade B.

**Willingness to pay.**
- Because tomato cost is not in the contribution, these shadow prices are the value of a **free** extra pound.
- Pay **less than 27.1 cents/lb** for extra grade A and **less than 17.3 cents/lb** for extra grade B. Paying less still increases profit.
- This is also the rule for setting the variable price paid to farmers for extra supply.

**Decision on the market offer of 80,000 lb of grade A at 25.5 cents/lb.**
- The allowable increase for grade A supply is 600,000 lb. (The figure was garbled in the transcript; it is consistent with the model, because juice would drop to zero after 600,000 extra lb.)
- 80,000 lb is within the allowable increase, so the shadow price stays valid over that range.
- $25.5 < 27.1$, so **buy it**.
- Net gain (computed) $\approx 80{,}000 \times (0.271-0.255) \approx 1{,}280$ dollars.

**Comparison with Myers' implied costs.**
- Myers (in the case) allocated the sunk cost by quality points and got about **27.96 cents** for grade A and **15.54 cents** for grade B, as quoted in class.
- Recomputing gives approximately: $9Z(600{,}000)+5Z(2{,}400{,}000)=540{,}000 \Rightarrow Z\approx 0.0310$, so A $\approx 27.9$ cents and B $\approx 15.5$ cents.
- The instructor's point:
  - The near-match for grade A is essentially a coincidence.
  - Myers' numbers are **accounting allocations of a sunk cost**. Shadow prices are the true **marginal value to the business**.
  - Grade B is actually worth more (17.3 cents) than Myers calculated.

**Demand constraints.**

- **Whole tomatoes and juice: shadow price = 0.**
  - These constraints are not binding.
  - Spending on advertising to raise their demand is pointless.
- **Paste: shadow price $\approx 0.0483$ dollars per lb of demand** (about 4.8 cents/lb).
  - Each extra pound of paste demand raises contribution by about 4.83 cents.
- **Marketing example from class:**
  - Suppose marketing promises +1 lb of paste demand for every 5 cents spent.
  - Reject this, because $5 > 4.83$.
  - Marketing spend per extra pound of paste demand must stay **below 4.83 cents**. The shadow price is a guide for designing the marketing budget.

**Quality (ratio) constraints.**
- These have **negative** shadow prices: about $-0.0243$ each (computed; not read out in class).
- Interpreting them is convoluted ("one more pound of A beyond the 1:3 ratio"), so they were not discussed in depth.
- **Observation stated in class:**
  - In a maximisation problem, $\le$ constraints never have negative shadow prices.
  - $\ge$ constraints can have negative shadow prices.
  - This will be formalised next class.

### 2.8 Sensitivity report: reduced costs

- All reduced costs are 0 except for $x_{A3}$. The basic variables (those with positive values) have zero reduced cost.
- **$x_{A3}$ has reduced cost $\approx -0.097$.**
  - For a maximisation problem, a variable at value zero has a reduced cost that is $\le 0$.
  - **Meaning 1:** forcing one lb into $x_{A3}$ lowers the objective by about 0.097 dollars.
  - **Meaning 2:** the objective coefficient of $x_{A3}$ would have to rise by more than 0.097 for $x_{A3}$ to enter the optimal solution.
- **Demonstration in class:**
  - The instructor added $0.098$ to the $x_{A3}$ coefficient and re-solved.
  - $x_{A3}$ became positive: much of grade A went into paste.
  - In that re-solved run, whole-tomato production went to zero.

### 2.9 Case takeaway

- The core mistake in the case was arguing over how to split a **sunk** tomato cost between grade A and grade B. Such accounting allocation is meaningless for decisions.
- Use contribution that **excludes** sunk costs, solve the LP, and use **shadow prices** to value resources and make purchasing and marketing decisions.

### 2.10 Student Q&A

**Question:** Juice demand is 1,000,000 lb but only 300,000 lb are produced. Should we buy grade B to meet market demand?

**Answer:**
- Juice demand is **not the bottleneck**. The bottlenecks are the two supply constraints and paste demand.
- If supply bottlenecks were relieved, juice demand might eventually become binding.
- A shadow price, such as 17.3 cents for grade B, holds only within the **allowable increase**. Beyond that, a different constraint becomes binding and the shadow price changes. You do not keep gaining 17.3 cents per extra pound indefinitely.

### 2.11 Graphical example: can a shadow price be negative in a maximisation problem?

**Version 1: inequality constraints**

```math
\max Z = 20x_1 + x_2
```

```math
\text{s.t.} \quad x_1 + x_2 \le 10 \quad \text{(constraint 1, shadow price } u_1\text{)}
```

```math
x_2 \le 4 \quad \text{(constraint 2, shadow price } u_2\text{)}
```

```math
x_1, x_2 \ge 0
```

Here $x_1$ is a highly profitable product and $x_2$ is barely profitable.

- **Feasible region:** a quadrilateral bounded by the two axes, the line $x_2=4$, and the line $x_1+x_2=10$.
- **Corner points** (labelling inferred from the sketch):

| Point | $(x_1,x_2)$ | $Z$ |
|---|---|---|
| $A$ | $(0,0)$ | $0$ |
| $B$ | $(0,4)$ | $4$ |
| $C$ | $(6,4)$ | $124$ |
| $D$ | $(10,0)$ | $200$ |

- The objective line is very steep and improves toward larger $x_1$.
- **Optimum:** $D$, with $x_1^\ast =10$, $x_2^\ast =0$, $Z^\ast =200$. This is the primal solution.
- **Shadow prices (dual variables):**
  - $u_1 = 20$. Raising RHS 1 to 11 moves the optimum to $D'=(11,0)$, and $Z$ rises by 20.
  - $u_2 = 0$. Moving the line $x_2=4$ does not affect corner $D$.

**Version 2: constraint 2 becomes an equality, $x_2 = 4$**

You are now **forced** to consume this resource completely.

- **Feasible region:** the line segment $BC$, from $(0,4)$ to $(6,4)$.
- **Optimum:** $C$, with $x_1^\ast =6$, $x_2^\ast =4$, $Z^\ast =124$.
- **$u_1 = 20$.** RHS 11 gives $(7,4)$, so $Z=144$.
- **$u_2 = -19$.** RHS 5 forces $x_2=5$, so $x_1=5$, $Z=20(5)+5=105$, and $105-124=-19$.

**Interpretation.**
- Think of resource 2 as something obnoxious, smelly or chemically reactive that cannot be left unused, and that only $x_2$ can consume.
- More of it forces more of the low-profit $x_2$. Since $x_1+x_2\le 10$, this crowds out the high-profit $x_1$, so profit falls.

**Rules:**
- **Maximisation with a $\le$ constraint:** shadow price $\ge 0$. Extra resource can always be left unused, so it can never hurt.
- **Equality constraint:** the shadow price can be **positive or negative**.
- **$\ge$ constraint (in a maximisation problem):** the shadow price can be negative, as seen with the quality constraints in Red Brand.

---

## 3. Exam / Assignment Pointers and What's Next

No explicit exam announcement was made. The instructor emphasised these points:

- **Exclude sunk costs** from contribution. Use the test: "does the cost disappear if nothing is produced?"
- **Keep units consistent.**
  - Convert dollars/case to dollars/lb by dividing by lb/case.
  - Convert demand in cases to lb by multiplying by lb/case.
- **Linearise ratio constraints.** For example, $x_{A1}/x_{B1}\ge 3$ becomes $x_{A1}-3x_{B1}\ge 0$.
- **Interpreting shadow prices:**
  - the maximum price worth paying for extra resource (compare with the market price, e.g. 25.5 vs 27.1 cents),
  - the maximum marketing spend per unit of extra demand,
  - valid only within the allowable increase/decrease.
- **Interpreting reduced costs:** how much an objective coefficient must improve before a zero variable enters the solution.
- **Sign rules for shadow prices:**
  - $\le$ in a maximisation problem: never negative.
  - $\ge$ or $=$: can be negative.

**Next sessions:**
1. Formal dual / shadow price theory: when shadow prices are positive or negative, and a better understanding of reduced cost, continuing the example above.
2. Integer programming, over the following two sessions.

<!-- nav -->
← [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 9 (2026-11-16)](DSM-109-9_2026-11-16_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
