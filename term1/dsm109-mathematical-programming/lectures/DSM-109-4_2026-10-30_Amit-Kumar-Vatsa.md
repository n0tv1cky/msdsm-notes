---
course: DSM 109
date: 2026-10-30
start: 7:00pm
session: "4"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 3 (2026-10-28)](DSM-109-3_2026-10-28_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 5 (2026-11-06)](DSM-109-5_2026-11-06_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Session 4 (2026-10-30): Solving the Merton Truck LP with Excel Solver and the Graphical Method, and Why Corner Points Suffice

**Instructor:** Amit Kumar Vatsa

---

## 1. Overview

This session continued the **Merton Truck Company** product-mix case from the previous class. The model had already been formulated last time. The instructor stressed that the hardest step is writing the correct profit expression, which means separating variable from fixed costs. Once that is right, the problem is "almost solved."

The session covered three things:

- **Solving in Excel Solver.** The model was entered and solved with the Simplex LP engine. The optimal product mix was compared with the earlier sub-optimal plan. The binding ("bottleneck") constraints were identified, and a Sensitivity Report was generated but not yet interpreted.
- **Solving graphically.** The feasible region was plotted, its corner points were enumerated, and iso-objective lines were introduced.
- **Theory.** The instructor defined solutions, feasible and optimal solutions, convex regions and extreme (corner) points. He gave intuitive proofs that:
  - an LP feasible region is always convex;
  - the optimum of a linear objective occurs at a corner point;
  - for a convex optimisation problem, a local optimum is a global optimum.

The last result motivates "Method 3": stop at any corner point that is better than all its neighbours. This is the idea behind the simplex method.

Next class covers convex optimisation in more depth, then **sensitivity analysis**: shadow prices, reduced costs, and allowable increases and decreases, used for managerial insight and negotiation.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: the key formulation pitfall

- The most important step is the **correct profit expression**.
  - Identify which costs are **variable** (they change with the number of trucks) and which are **fixed**.
  - With a wrong expression (the earlier wrong version from last class), you reach wrong conclusions, e.g., that Model 101 should not be produced at all.
- Once the formulation is right, solving it is the easy part (Solver/AI tools).
- The optimal solution itself is **not the most interesting output**. The **insights** are: bottlenecks, shadow prices, and allowable ranges. These can be used, for example, to negotiate.
- Solving by "logical trade-off reasoning" (as done last class) reinvents the wheel. It becomes too tedious for large problems, because you don't know which constraint to relax or when to stop.

### 2.2 The Merton Truck LP model (standard form)

**Decision variables**

- $x_1$ = number of Model 101 trucks produced per period (trucks; per month in the case, see note below)
- $x_2$ = number of Model 102 trucks produced per period (trucks)

**Data used in lecture**

| | Model 101 ($x_1$) | Model 102 ($x_2$) | Capacity (hours) |
|---|---|---|---|
| Contribution per truck | \$3,000 | \$5,000 | — |
| Engine assembly (hrs/truck) | 1 | 2 | 4,000 |
| Metal stamping (hrs/truck) | 2 | 2 | 6,000 |
| Model 101 assembly (hrs/truck) | 2 | 0 | 5,000 |
| Model 102 assembly (hrs/truck) | 0 | 3 | 4,500 |

Fixed costs: \$8.6 million (\$8,600,000), treated as **sunk** for the optimisation.

> **Notes:**
> - The ASR initially reads "maximize 1 x 1 plus 2 x 2". This was a slip; the instructor immediately corrected it to $3000x_1 + 5000x_2$.
> - "Per month" is inferred from the original HBS Merton Truck case; it is not stated in this session.

**Model (total contribution)**

```math
\begin{aligned}
\max\; Z &= 3000\,x_1 + 5000\,x_2 && \text{(total contribution, \$)}\\
\text{s.t.}\quad x_1 + 2x_2 &\le 4000 && \text{(1) Engine assembly hours}\\
2x_1 + 2x_2 &\le 6000 && \text{(2) Metal stamping hours}\\
2x_1 &\le 5000 && \text{(3) Model 101 assembly hours}\\
3x_2 &\le 4500 && \text{(4) Model 102 assembly hours}\\
x_1,\; x_2 &\ge 0 && \text{(non-negativity)}
\end{aligned}
```

- Integrality was **not** imposed; it was solved as an LP. The optimum happens to be integer anyway.
- **Profit version:** $\max\  3000x_1 + 5000x_2 - 8{,}600{,}000$.
  - This gives the **same optimal $x_1, x_2$**, because subtracting a constant does not change which point is best.
  - Fixed cost is sunk: "nothing can be done about that."
  - The instructor demonstrated this in Solver: the results were identical.

### 2.3 Excel Solver implementation

**Sheet layout**

- **Yellow cells** are the decision variables $x_1, x_2$, which Solver fills in.
- **Blue cell** is the objective (total contribution), written as `=SUMPRODUCT(contribution row, decision cells)`.
  - Use **`$` absolute references** to freeze the decision-cell range, so the same SUMPRODUCT formula can be copied down to compute each constraint's "hours used" (LHS).
- Each constraint has an LHS ("used hours") and an RHS (available hours).

**Solver dialog** (Data → Solver)

- Set Objective: the blue cell → **Max**.
- By Changing Variable Cells: the yellow cells.
- Subject to the Constraints: used hours (LHS) $\le$ available hours (RHS).
- Solving method: **Simplex LP**.
- Non-negativity: presumably the "Make Unconstrained Variables Non-Negative" box (standard; not mentioned explicitly).
- After solving, generate the **Sensitivity Report**.

**Results: earlier plan vs. optimal plan**

| | Earlier plan (last class) | Solver optimum |
|---|---|---|
| $(x_1, x_2)$ | $(1000, 1500)$ | $(2000, 1000)$ |
| Total contribution | \$10.5M | \$11.0M |
| Total profit (− \$8.6M fixed) | \$1.9M | \$2.4M |
| Binding (bottleneck) constraints | Engine assembly, Model 102 assembly | Engine assembly, Metal stamping |

**Hours check** (useful to verify by hand):

| Department | Earlier plan $(1000,1500)$ | Optimum $(2000,1000)$ |
|---|---|---|
| Engine | $1000 + 3000 = 4000$ (**binding**) | $2000 + 2000 = 4000$ (**binding**) |
| Stamping | $2000 + 3000 = 5000$ (1,000 h slack) | $4000 + 2000 = 6000$ (**binding**) |
| 101 assembly | $2000$ (3,000 h slack) | $4000$ (1,000 h slack) |
| 102 assembly | $4500$ (**binding**) | $3000$ (1,500 h slack) |

**Insight**

- Optimising raises profit by about **\$0.5M**.
- The bottleneck set changes. Model 102 assembly, a bottleneck under the old plan, is **no longer binding** at the optimum.
- At the optimum, engine assembly and metal stamping are at 100% utilisation. **Extra capacity should be added to these two departments only.**

**Sensitivity report** (shown, interpretation deferred). It reports:

- shadow prices;
- allowable increase/decrease of constraint RHS;
- allowable increase/decrease of objective coefficients;
- reduced costs.

The instructor said the graphical method is needed to understand these properly.

### 2.4 Graphical solution method

- It works only for **2 variables**. Three variables need a 3D plot; four or more cannot be visualised. It is mainly for building intuition.
- Each $\le$ constraint is a straight line (the equality) plus **one feasible side** (a half-plane).

**Plotting each constraint**

- Find the two axis intercepts and join them.
- Test a point not on the line (e.g., the origin) to see which side is feasible.
  - Example: $0 + 0 \le 4000$ is true, so the origin's side is feasible.

| Constraint | Line | Intercepts |
|---|---|---|
| (1) Engine | $x_1 + 2x_2 = 4000$ | $(4000, 0)$ and $(0, 2000)$ |
| (2) Stamping | $2x_1 + 2x_2 = 6000$ | $(3000, 0)$ and $(0, 3000)$ |
| (3) 101 assembly | $x_1 = 2500$ | vertical line |
| (4) 102 assembly | $x_2 = 1500$ | horizontal line |

**Feasible region**

- It is the polygon **ABCDEF** (the ASR says "A, B, C, D, F"; the polygon has six corners).
- Every point inside, on an edge, or at a vertex satisfies all constraints, including non-negativity. Example: $(1000, 1000)$.
- There are infinitely many feasible solutions.

**Corner points and objective values**

| Corner | Defined by | $(x_1, x_2)$ | $Z = 3000x_1 + 5000x_2$ |
|---|---|---|---|
| A | origin | $(0, 0)$ | 0 |
| B | $x_1 = 0$ and 102 assembly | $(0, 1500)$ | \$7.5M |
| C | 102 assembly ∩ Engine: $x_2 = 1500$, so $x_1 = 4000 - 3000 = 1000$ | $(1000, 1500)$ | $3\text{M} + 7.5\text{M} =$ \$10.5M |
| **D** | Engine ∩ Stamping: $x_1 + 2x_2 = 4000$ and $x_1 + x_2 = 3000$ give $x_2 = 1000$, $x_1 = 2000$ | **$(2000, 1000)$** | $6\text{M} + 5\text{M} =$ **\$11M** |
| E | Stamping ∩ 101 assembly: $x_1 = 2500$, so $2x_2 = 6000 - 5000$, $x_2 = 500$ | $(2500, 500)$ | $7.5\text{M} + 2.5\text{M} =$ \$10M |
| F | 101 assembly and $x_2 = 0$ | $(2500, 0)$ | \$7.5M |

**Optimum: corner D, $(2000, 1000)$, $Z^\ast  = \text{USD }11$M.** This agrees with Solver.

#### Method 1: Corner-point enumeration

Find all corner points of the feasible region, evaluate the objective at each, and pick the best. This applies when the feasible region is bounded; the instructor flagged this "qualification" for later.

A student asked *why* only corners need checking. Method 2 and the theory below answer this.

#### Method 2: Iso-objective line

- An **iso-objective line** is a line on which every point has the same objective value ("iso" = same).
- **Example at $Z = 7.5$M:** $3000x_1 + 5000x_2 = 7{,}500{,}000$.
  - Intercepts are $(2500, 0)$ and $(0, 1500)$, so the line passes through **F and B**, both worth \$7.5M.
  - The ASR says the $x_2$-intercept is "5000"; the correct value is $7{,}500{,}000/5000 = 1500$.
- Shift the line **parallel**, in the direction of improvement (up and right for this max problem):
  - through **E**: $Z = 10$M, still many feasible points on the line;
  - through **C**: $Z = 10.5$M, still many feasible points;
  - through **D**: $Z = 11$M, **only D** is feasible on this line.
- Keep moving until the line is about to **exit the feasible region**. A straight line (or a plane, in higher dimensions) leaving a polygon always exits at a **corner point**. This is why Method 1 never gives a sub-optimal answer.

**Exercise: generic polygon with corners a, b, c, d, …** The instructor used the word "improvement" rather than max/min.

- Depending on the direction of improvement, the line exits at a different corner. Different directions made d, a, or c optimal.
- If you push the line further than the last corner, no point on it is feasible. So stop at the last corner.

**Alternate (multiple) optima**

- If the iso-objective line is **parallel to an edge**, it exits through two corners (e.g., c and d) simultaneously.
- Then **every point on the segment joining them is optimal**: there are infinitely many optimal solutions.
- Excel or any commercial Solver reports **only one corner** (c or d), never an in-between point. Certain signs in the Solver output reveal alternate optima; this is to be covered later.

### 2.5 Definitions

- **Solution:** any point in the $(x_1, x_2)$ plane, feasible or infeasible.
- **Feasible solution:** a point satisfying all constraints, including non-negativity.
- **Optimal solution:** a feasible solution with the best objective value.
- **Convex region:** a region $S$ is convex if for any two points $P, Q \in S$, the **entire line segment** $PQ$ lies in $S$.
  - Non-convex example: a shape with a notch (indentation), where part of the segment between two points falls outside the region.
- **Convex combination (weighted average)** of $x_P, x_Q$: $\lambda x_P + (1-\lambda)x_Q$ with $0 \le \lambda \le 1$.
- **Extreme point (corner point):** defined for convex regions. It is a point whose coordinates **cannot** be written as a weighted average of two *other distinct* points in the region.
  - Midpoints of edges and interior points are *not* corners. For example, an edge midpoint equals $0.5\times$ one endpoint $+ 0.5\times$ the other.
  - For a true corner, any pair you try either has a point outside the region or collapses onto the corner itself.
  - Every point in the region can be written as a combination of extreme points, but not the other way round.

### 2.6 Theorem 1: An LP feasible region is always convex

**Intuitive argument**

- Each linear constraint ($\le$, $\ge$, or $=$) keeps only **one side** of a line, or the line itself.
- A notched, non-convex shape would need a re-entrant corner. That requires both sides of some boundary line to be feasible, which a linear constraint can't produce.
- Students' comments ("CD should be extended totally") captured this: each boundary line extends fully, and only one side survives.

**Algebraic proof**

Let $P, Q$ be feasible, so $A x_P \le b$ and $A x_Q \le b$ (vector form, with non-negativity included). Take $\lambda \in [0,1]$.

1. Multiply the first inequality by $\lambda$ and the second by $(1-\lambda)$. Both multipliers are $\ge 0$, so the inequality direction is preserved.
2. Add the two:

```math
A\big(\lambda x_P + (1-\lambda)x_Q\big) \le \lambda b + (1-\lambda) b = b .
```
3. So any point $R$ on segment $PQ$, with $x_R = \lambda x_P + (1-\lambda)x_Q$, satisfies $A x_R \le b$ and is feasible. Hence the region is convex.

### 2.7 Why the optimum is at a corner: the weighted-average intuition

**Worked example**

- $P$ = midpoint of BC $= \tfrac12(0, 1500) + \tfrac12(1000, 1500) = (500, 1500)$.
- $Z(P) = 3000(500) + 5000(1500) = 1.5\text{M} + 7.5\text{M} = 9\text{M}$.
- The average of $Z(B) = 7.5$M and $Z(C) = 10.5$M is $9$M.

Is this a fluke? **No, it is by design**, because the objective is **linear**:

```math
Z(\lambda x_B + (1-\lambda)x_C) = \lambda Z(x_B) + (1-\lambda) Z(x_C).
```

**Generalisation**

- A point $P'$ that is 90% C and 10% B has $Z(P') = 0.9\ Z(C) + 0.1\ Z(B)$.
- A point inside triangle ABC, e.g., $0.33A + 0.33B + 0.34C$, has $Z$ equal to the same weighted average of $Z(A), Z(B), Z(C)$.
- Any interior point is a convex combination of corner points. So its objective value is a weighted average of corner objective values.

**Conclusion**

- A weighted average with weights in $[0,1]$ can never exceed the largest value or fall below the smallest.
- Therefore the max (or min) is always attained at a corner. Interior points only give "in-between" values.

### 2.8 Theorems 2 and 3, and Method 3

**Theorem 2 (corner-point optimality).** If the feasible region is an LP region (convex polygon or polyhedron) and the objective is linear, then **if an optimal solution exists, at least one corner point is optimal**.
- Implication: searching corners only never misses the optimum.

**Theorem 3 (convex optimisation).** For a **convex optimisation problem**, **any local optimum is a global optimum**.
- LPs are convex optimisation problems, because the region is convex and the objective linear. A precise definition is due next class.

**Method 3: Local search over corners.** You do **not** need to evaluate every corner.
- If you land on a corner that is **better than all its neighbouring (adjacent) corners**, stop. It is a local optimum, hence the global optimum.
- **Merton example:** suppose you happen to start at D.
  - The neighbours of D are C (\$10.5M) and E (\$10M). Both are worse than D's \$11M.
  - So D is optimal, even with no information about A, B, or F.
  - Even more simply, from D both edge directions decrease $Z$, so you could stop immediately.
- This answers the earlier question of whether Solver uses brute force. It does **not**; it moves between adjacent corners and stops at a local (= global) optimum. This is the logic of the Simplex method, the "Simplex LP" engine selected in Solver; the explicit link to simplex is an inference from the Solver setting used.

---

## 3. Exam and Assignment Pointers

The instructor flagged nothing explicitly as "on the exam," but emphasised these points:

1. **Correct profit and contribution formulation is the #1 pitfall.**
   - Separate variable from fixed costs.
   - Fixed (sunk) costs don't affect the optimal mix: maximising contribution and maximising profit give the same $x^\ast $.
2. **Be able to set up Excel Solver.**
   - Decision cells, a SUMPRODUCT objective with `$` references, LHS ≤ RHS constraints, Simplex LP.
   - Generate the Sensitivity Report.
3. **Identify binding (bottleneck) constraints** and say where extra capacity is worthwhile. Here: engine assembly and metal stamping.
4. **Graphical method.** Plot constraints via intercepts, test the feasible side with the origin, list corner points with coordinates and $Z$ values, and use iso-objective lines.
5. **Know the theory and intuition.**
   - Definitions of convex region and extreme point.
   - Proof that the LP region is convex: the $\lambda$, $1-\lambda$ argument.
   - The weighted-average argument for corner optimality.
   - Alternate optima: a whole edge is optimal, but Solver shows only one corner.
   - Local = global for convex problems (Method 3).
6. **Coming next:** convex optimisation, then **sensitivity analysis**.
   - Topics: shadow prices, reduced costs, and allowable increases/decreases for RHS values and objective coefficients.
   - These will be used for managerial decisions in the continued Merton Truck discussion.

<!-- nav -->
← [Session 3 (2026-10-28)](DSM-109-3_2026-10-28_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 5 (2026-11-06)](DSM-109-5_2026-11-06_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
