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

# DSM-109 · Session 7 (2026-11-11) · Amit Kumar Vatsa
## Study Notes: Objective-Coefficient Ranging (Merton Truck), Origin of "Reduced Cost", and the Red Brand Canners Case

> **Transcript notes.** The ASR text renders "Merton Truck" as *Murtantrak* or *modern truck*, "Dantzig" as *Danzig/Dostanzig*, "Pentagon" as *Pentagan*, "Red Brand Canners" as *red brand canvas*, "Myers" as *Myers/my says*, and "Cooper" as *Koopa*. "Juice" appears as *Jus/Jews*, and the paste demand appears as *peach rate*.
>
> Some numbers below come from the standard published versions of the cases, not from the lecture. These are marked **[inferred]**.

---

## 1. Overview

This session first finishes the **Merton Truck** sensitivity analysis. It explains what the **allowable increase/decrease** of an objective-function coefficient means: the range over which one coefficient can change, with all else fixed, while the current optimal corner point stays optimal.

The instructor shows this two ways:
- **In Excel Solver.** Raising the Model 101 profit from 3000 to 4999 keeps the optimum, but 5001 moves it to another corner.
- **Graphically/algebraically.** The objective's slope must stay between the slopes of the two **binding constraints**, which gives ranges for each coefficient.

The session then summarises the meaning of **reduced cost** through Dantzig's **diet problem** (the origin of the term) and briefly revisits **shadow price**.

The second half introduces the **Red Brand Canners** case. The case covers:
- the tomato supply, split into grade A and grade B, with quality ratings;
- blending (mixture) requirements for whole tomatoes, juice and paste;
- two competing cost analyses: Cooper's Exhibit 2 and Myers' Exhibit 3.

The class concludes that **both cost analyses are flawed**. The tomatoes are a **sunk cost**, so apportioning that cost between grades (or products) should not drive the product-mix decision. The true value of grade A should come from the **shadow price** of the grade A supply constraint in an LP. That LP will be formulated and solved next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Merton Truck model

**Decision variables**
- $x_1$ = number of Model 101 trucks produced (units/month)
- $x_2$ = number of Model 102 trucks produced (units/month)

**Model**

```math
\begin{aligned}
\max\quad & Z = 3000\,x_1 + 5000\,x_2 && \text{(total contribution, \$)}\\
\text{s.t.}\quad & x_1 + 2x_2 \le 4000 && \text{(engine assembly hours)}\\
& 2x_1 + 2x_2 \le 6000 && \text{(metal stamping hours)}\\
& 2x_1 \le 5000 && \text{(Model 101 assembly hours) [inferred]}\\
& 3x_2 \le 4500 && \text{(Model 102 assembly hours) [inferred]}\\
& x_1,\ x_2 \ge 0
\end{aligned}
```

The lecture states the engine assembly ratio $1:2$ and the metal stamping ratio $2:2$ directly. The two assembly-line constraints come from the standard case and are consistent with the corner points quoted in class.

**Optimal solution:** $x_1 = 2000$, $x_2 = 1000$, giving $Z = 3000(2000)+5000(1000) = \text{USD }11{,}000{,}000$.
- The binding constraints are **engine assembly** and **metal stamping**.
- At one point the transcript says "1000, 1000". This is a slip; the optimum is $(2000, 1000)$.

**Reduced costs**
- Both $x_1$ and $x_2$ are positive (basic) at the optimum, so their **reduced cost is 0**.
- Forcing $x_1 \ge 1$ would be a redundant constraint, so the objective would not change.
- **Model 103** (extended version of the case) had a **reduced cost of $-350$**. Forcing one unit of Model 103 into production lowers total profit by \$350, because it is "loss-making" relative to the current use of resources.

### 2.2 Allowable increase/decrease of objective coefficients

**Definition.** The allowable increase and decrease tell you how far you can change one objective-function coefficient (one at a time, all else fixed) while the **current corner point remains optimal**. The optimal *values of the variables* stay the same. The objective *value* does change.

**Solver report for $x_1$:** coefficient 3000, allowable increase 2000, allowable decrease 500.

**Excel demonstration**
| Change made | Result |
|---|---|
| $c_1 = 4999$ | Optimum still $(2000, 1000)$ |
| $c_1 = 5001$ | Optimum jumps to corner **E** $= (2500, 500)$ |

### 2.3 Graphical intuition

The feasible region is a polygon. Its corner points, with the objective values at the original coefficients, are below. The lecture names only C, D and E; the other labels are **[inferred]**.

| Corner | Constraints that intersect there | $(x_1, x_2)$ | $Z$ |
|---|---|---|---|
| A | origin | $(0,0)$ | 0 |
| B | $x_1=0$ and Model 102 assembly | $(0,1500)$ | 7.5M |
| C | Model 102 assembly and engine assembly | $(1000,1500)$ | 10.5M |
| **D** | engine assembly and metal stamping | $(2000,1000)$ | **11M (optimal)** |
| E | metal stamping and Model 101 assembly | $(2500,500)$ | 10M |
| F | Model 101 assembly and $x_2=0$ | $(2500,0)$ | 7.5M |

**How the optimum moves as the objective line rotates**
- **When $c_1$ increases**, the iso-profit line gets steeper. D stays optimal until the line becomes **parallel to segment DE** (the metal stamping line). At that moment D and E are both optimal. Any steeper, and E alone is optimal.
- **When the line becomes flatter**, D stays optimal until the line is **parallel to segment CD** (the engine assembly line). At that moment C and D are both optimal. Any flatter, and C alone is optimal.

**Key rule:** The slope of the objective-function line must lie **between the slopes of the binding constraints** (here, engine assembly and metal stamping) for the current corner to stay optimal.

### 2.4 Algebraic ranging using coefficient ratios

Instead of slopes, compare the ratios (coefficient of $x_1$)/(coefficient of $x_2$):
- Engine assembly: $\tfrac{1}{2}$
- Metal stamping: $\tfrac{2}{2}$
- Objective: $\tfrac{3000}{5000}$

The objective's ratio must lie between the two constraint ratios.

**Range for the coefficient of $x_1$.** Replace 3000 by $k$:

```math
\frac{1}{2} \le \frac{k}{5000} \le \frac{2}{2} \;\Longrightarrow\; 2500 \le k \le 5000
```

- The allowable decrease is $3000 - 2500 = 500$.
- The allowable increase is $5000 - 3000 = 2000$.
- This explains the demo: 4999 is inside the range, but 5001 is outside.
- At exactly $k = 5000$, D and E tie.

**Range for the coefficient of $x_2$.** Replace 5000 by $k'$:

```math
\frac{1}{2} \le \frac{3000}{k'} \le \frac{2}{2}
```

Taking reciprocals reverses the inequalities:

```math
2 \ge \frac{k'}{3000} \ge 1 \;\Longrightarrow\; 3000 \le k' \le 6000
```

So the allowable increase is $1000$ and the allowable decrease is $2000$ (since $5000-2000=3000$).

### 2.5 Summary of Merton Truck insights
- The optimal solution is not the only output that matters. Sensitivity analysis supports **negotiation**: with workers, suppliers, or about any constraint.
- **Shadow prices** tell you what it is worth to relax a constraint or add capacity.
- **Reduced costs** tell you which alternative products would be loss-making if forced into production.

### 2.6 Origin of the term "reduced cost": Dantzig's diet problem
- **Context.** George Dantzig worked for the US Air Force (Pentagon). One early problem was how to feed soldiers at minimum cost.
- **Decision variables:** number of servings of each food item (egg, milk, maize, …).
- **Constraints:** minimum and maximum levels of each nutrient (calories, minerals, protein, vitamins, carbohydrates, …).
- **Objective:** minimise the cost of the diet per person.

General form:

```math
\min \sum_j c_j x_j \quad \text{s.t.}\quad L_i \le \sum_j a_{ij} x_j \le U_i\ \ \forall i,\qquad x_j \ge 0
```

Here:
- $x_j$ = servings of food $j$;
- $c_j$ = cost per serving of food $j$;
- $a_{ij}$ = amount of nutrient $i$ per serving of food $j$;
- $L_i$ and $U_i$ = the minimum and maximum required amounts of nutrient $i$.

**Meaning of reduced cost.** Suppose milk is 0 in the optimal diet. That means other foods supply the same nutrients more cheaply. The **reduced cost** of milk is how much its cost per serving must be **reduced** before milk enters the optimal diet. Hence the name.

Equivalently, the reduced cost is how much the objective changes if a non-participating variable is forced to take one unit.

**Shadow price (recap).** The change in the optimal objective per marginal unit increase in a constraint's right-hand side. In other words, it is the worth of one extra unit of a resource.

### 2.7 Red Brand Canners: case facts

**Products** (tomato products only; the peach and apple items in the case are ignored): whole tomatoes (canned), tomato juice, tomato paste.

**Supply**
- 3,000,000 lb of tomatoes, contracted at the average price of **\$0.18/lb**.
- 20% is **grade A**: $600{,}000$ lb.
- 80% is **grade B**: $2{,}400{,}000$ lb.

**Quality ratings** (scale of 1–10): grade A = **9**, grade B = **5**. Grades can be mixed, and the blended rating is assumed to be a linear (weighted) average.

**Minimum rating required**
| Product | Minimum rating |
|---|---|
| Whole tomatoes | 8 |
| Juice | 6 |
| Paste | 5 (pure grade B suffices, so this is not a concern) |

**Pounds per case:** whole tomatoes 18; juice 20; paste 25.

**Demand forecasts:** whole tomatoes 800,000; juice 50,000; paste 80,000. The lecture says "pounds", but the case gives these in **cases [inferred]**.

**Additional offer:** 80,000 lb of extra grade A is available at **25.5 cents/lb**.

### 2.8 Blending (mixture) constraints

Let the mix ratio be $A:B = \lambda : 1$.

**Whole tomatoes (rating at least 8)**

```math
\frac{9\lambda + 5(1)}{\lambda+1} \ge 8 \;\Rightarrow\; 9\lambda + 5 \ge 8\lambda + 8 \;\Rightarrow\; \lambda \ge 3
```

So $A:B \ge 3:1$. That means **at least 75% grade A** and at most 25% grade B.

The alligation shortcut gives the same answer: 8 is 3 units from B (5) and 1 unit from A (9), so the ratio is $A:B = 3:1$.

**Juice (rating at least 6)**

```math
9\lambda + 5 \ge 6\lambda + 6 \;\Rightarrow\; \lambda \ge \tfrac{1}{3}
```

So **at least 25% grade A** and at most 75% grade B.

**Paste (rating at least 5):** can be made entirely from grade B, so no constraint is needed.

### 2.9 Cooper's analysis (Exhibit 2)

Contribution = selling price minus variable costs. The variable costs are:
- **Direct labour** (variable if it is contract or hourly labour);
- **Variable overhead**;
- **Variable selling** (e.g., commission per case to sales channels);
- **Packaging material**;
- **Fruit cost**.

**Fruit cost = \$0.18/lb × lb per case:**
- Whole tomatoes: $18 \times 0.18 = \text{USD }3.24$ per case
- Juice: $20 \times 0.18 = \text{USD }3.60$ per case
- Paste: $25 \times 0.18 = \text{USD }4.50$ per case

**Whole tomatoes:** selling price \$12.00, total variable cost \$10.80, so contribution = $12 - 10.80 = \text{USD }1.20$ per case. Selling price minus non-fruit variable costs is about \$4.44 (the lecture says 4.4).

**Allocated (fixed) overhead** should be ignored for this decision. This lesson carried over from Merton Truck: keep fixed costs separate.

### 2.10 Myers' analysis (Exhibit 3)

**Argument.** Grade A is premium quality, so it should carry a higher cost than grade B. Let $Z$ = cost per lb of grade A and $Y$ = cost per lb of grade B. Myers uses two equations.

1. **Total cost is preserved:**

```math
600{,}000\,Z + 2{,}400{,}000\,Y = 3{,}000{,}000 \times 0.18 = \$540{,}000
```

2. **Cost is proportional to rating:**

```math
\frac{Z}{9} = \frac{Y}{5} \;\Rightarrow\; Z = 1.8\,Y
```

**Solving:**

```math
3{,}480{,}000\,Y = 540{,}000 \;\Rightarrow\; Y \approx \$0.1552/\text{lb}, \quad Z \approx \$0.2793/\text{lb}
```

The transcript says "27.96 cents" and "1.154"; both are ASR or slip errors. The case values are about 27.93¢ and 15.52¢.

**Fruit cost per case under Myers**

Whole tomatoes (75% A, 25% B):

```math
18\,(0.75\times 0.2793 + 0.25\times 0.1552) \approx \$4.47
```

Juice (25% A, 75% B):

```math
20\,(0.25\times 0.2793 + 0.75\times 0.1552) \approx \$3.72
```

Paste (all B):

```math
25 \times 0.1552 \approx \$3.88 \;(\text{"3.9" in lecture})
```

**Comparison with Cooper**
| Product | Cooper (\$/case) | Myers (\$/case) | Why it changes |
|---|---|---|---|
| Whole tomatoes | 3.24 | 4.47 | Uses at least 75% premium grade A |
| Juice | 3.60 | 3.72 | Only a slight change: the 25:75 mix is close to the 20:80 supply mix |
| Paste | 4.50 | 3.88 | Large drop: uses only cheap grade B |

**Myers' conclusion.** Whole tomatoes now show a contribution of about $4.44 - 4.47 = -\text{USD }0.03$ per case, a loss. So he says: don't produce whole tomatoes; use grade A for juice and paste.

### 2.11 Class discussion: who is right?

**Student views raised**
- Myers considers quality as well as quantity, so he looks more logical.
- The "cost proportional to rating" assumption is made up.

**The instructor's critique of Myers.** The logic spirals:
1. If whole tomatoes are dropped, all the grade A shifts into juice.
2. Juice's fruit cost then rises, so juice also looks unprofitable.
3. Then nothing uses grade A, and it is effectively thrown away.

The artificially inflated cost of grade A makes every product that uses it look unprofitable.

**Analogy: the expensive expert on the bench.** A company hires a costly expert to contribute across several software products.
- Each product manager refuses the expert's hours, because billing those hours makes their product look loss-making.
- The expert sits on the bench while the salary is paid anyway.
- The error: for the organisation, the salary is a **sunk/fixed cost**. It is paid regardless, so the resource should not go to waste.

A student (Rahul) described practice-area leads charged as a fraction (e.g., 0.25) of overhead across projects. The instructor's point: apportioning a fixed overhead may be fine for long-term strategic purposes, but it **should not drive short-term tactical or operational decisions**. This is the same as allocating fixed overhead to one product in Merton Truck.

**Resolution**
- The 3M lb were bought under contract at 18¢/lb. That cost is **sunk**, and the grading into A and B happened afterwards.
- **Both Cooper and Myers are incorrect.**
  - Cooper ignores that grade A is **scarce**.
  - Myers apportions a sunk cost.
- Grade A's best use is whole tomatoes. Use the grade A you already hold; don't let the allocated purchase cost decide.
- The meaningful question is what grade A is **worth to the business**. Answer it with **sensitivity analysis**:
  1. Add the supply constraints: grade A ≤ 600,000 lb and grade B ≤ 2,400,000 lb.
  2. Look at the **shadow price** of the grade A constraint.
  3. If the shadow price is greater than \$0.255/lb, buy the extra 80,000 lb at 25.5¢. If it is less (e.g., 23¢), don't buy.

**General principle.** Accounting "tricks" (apportioning) are only possible with **fixed costs**. A variable cost is simply the incremental cost per extra unit, so it cannot be apportioned arbitrarily.

### 2.12 Preview: likely LP for next class [inferred, not formulated in this session]

**Decision variables:** $x_{ij}$ = lb of grade $i\in\lbrace A,B\rbrace $ used in product $j\in\lbrace W,J,P\rbrace $, where $W$ = whole tomatoes, $J$ = juice, $P$ = paste.

**Objective.** Maximise contribution *excluding fruit cost* (the fruit cost is sunk). Per-lb contributions are taken from the case exhibits **[inferred]**:
- Whole: $4.44/18 \approx 0.2467$
- Juice: $(13.50-9.54)/20 = 0.198$
- Paste: $(11.36-5.85)/25 \approx 0.2204$

```math
\begin{aligned}
\max\quad & 0.2467(x_{AW}+x_{BW}) + 0.198(x_{AJ}+x_{BJ}) + 0.2204(x_{AP}+x_{BP})\\
\text{s.t.}\quad & x_{AW}+x_{AJ}+x_{AP} \le 600{,}000 && \text{(grade A supply, lb)}\\
& x_{BW}+x_{BJ}+x_{BP} \le 2{,}400{,}000 && \text{(grade B supply, lb)}\\
& x_{AW} \ge 3\,x_{BW} && \text{(whole tomatoes rating} \ge 8)\\
& 3\,x_{AJ} \ge x_{BJ} && \text{(juice rating} \ge 6)\\
& x_{AW}+x_{BW} \le 800{,}000\times 18 && \text{(whole tomatoes demand, lb)}\\
& x_{AJ}+x_{BJ} \le 50{,}000\times 20 && \text{(juice demand, lb)}\\
& x_{AP}+x_{BP} \le 80{,}000\times 25 && \text{(paste demand, lb)}\\
& x_{ij} \ge 0
\end{aligned}
```

The shadow price of the grade A supply constraint answers the question about buying the extra 80,000 lb at 25.5¢.

---

## 3. Exam / Assignment Pointers
- **Read the case before class.** The instructor stressed that participation in case discussions is expected, and that non-preparation makes the class "very difficult".
- **Know how to derive objective-coefficient ranges** from the slopes or coefficient ratios of the binding constraints, including the reciprocal step. Be able to interpret Solver's allowable increase and decrease.
- **Distinguish clearly:**
  - **Reduced cost:** how much a non-basic variable's coefficient must improve, or the objective change per forced unit.
  - **Shadow price:** the value of one extra unit of a resource.
  - **Allowable increase/decrease:** the range over which the current corner stays optimal.
- **Blending constraints** via weighted average or alligation: whole tomatoes need at least 75% grade A, juice at least 25% grade A.
- **Key conceptual takeaway:** sunk or fixed costs should not be apportioned to drive tactical decisions. Value scarce resources using **shadow prices**.
- **Next class:** formulate and solve Red Brand Canners as an LP, and use sensitivity analysis to decide on the extra grade A purchase.

<!-- nav -->
← [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
