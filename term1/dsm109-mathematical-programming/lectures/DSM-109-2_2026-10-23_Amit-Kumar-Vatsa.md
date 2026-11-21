---
course: DSM 109
date: 2026-10-23
start: 7:00pm
session: "2"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 1 (2026-10-22)](DSM-109-1_2026-10-22_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 3 (2026-10-28)](DSM-109-3_2026-10-28_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Session Notes: Computational Complexity, Brute Force vs. Optimisation, and a First LP in Excel Solver

*Session: DSM-109-2, 2026-10-23, Amit Kumar Vatsa*

---

## 1. Overview

The session starts with a recap: a revenue-management pricing problem solved with calculus, and a flight-booking problem with multiple optimal solutions. It then asks why we need systematic optimisation methods instead of brute-force enumeration. Through the dozer-to-site assignment problem ($n!$ alternatives), the Travelling Salesman Problem ($n!$ routes), and a truck-loading (subset-sum) problem ($2^n$ subsets), the instructor shows how factorial and exponential growth make enumeration impractical. He uses the chessboard-and-wheat legend to illustrate exponential growth and a "computing power doubles" thought experiment to compare $\log n$, linear, quadratic and exponential algorithms. He then shows that Excel Solver solves the assignment problem quickly as an LP (Simplex LP, integrality property) and the subset-sum problem as a binary integer program, which is NP-hard. The session ends with the first formal linear-programming formulation, a table-and-chair product-mix problem. It covers decision variables versus parameters, why non-negativity is needed, and a step-by-step Excel Solver setup giving the optimum of 30 tables and 40 chairs. Sensitivity analysis and the reasons LP is popular are previewed. Next class covers the Merton Truck case, the graphical method and more formulations.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap of the previous class

- **Revenue management / pricing problem.**
  - It was solved with calculus or curve fitting.
  - Setting the derivative of revenue (or profit) to zero gives the stationary point, which is the optimal price. This is a closed-form, formula-based solution.
  - **Caveat:** even when a closed form exists, keep "out-of-the-box" thinking. Don't focus so narrowly on the mathematical optimisation that you lose sight of the bigger business goal.
- **Flight ticket booking problem.**
  - It had multiple optimal solutions, each with total cost Rs. 30,000.
  - Trial and error (hit-and-trial) might never find them.
  - **Key motivation:** when we have a solution, we want a proof (or at least strong conviction) that it is the best one.

### 2.2 Why brute force fails: factorial growth

- **Dozers-to-sites (assignment) problem.**
  - With $n$ dozers and $n$ sites (one dozer per site), there are $n!$ possible assignments.
  - One way to guarantee optimality is to evaluate every alternative, i.e. $n!$ of them.
  - Even for $n = 20$ or $25$, $n!$ is enormous. For example, $20! \approx 2.43 \times 10^{18}$ (value added for illustration, not stated in class).
  - Even supercomputers would take years. Any method that needs about $n!$ steps is impractical as $n$ grows.
- **Travelling Salesman Problem (TSP)**, a classic routing problem.
  - A salesman starts at city 0, visits $n$ cities exactly once each, and returns to city 0, minimising total distance.
  - The $n$ cities can be ordered in $n!$ ways. Brute force is again impossible for $n \approx 20$–$30$.

### 2.3 The truck-loading (subset-sum) problem: exponential growth

**Problem.** You manage logistics, have 10 items with given weights (in tons), and a 40-ton truck. Can you fill the truck exactly, choosing a subset of items whose weights sum to exactly 40?

**Feasible subsets found by students in class:**

| Subset | Check |
|---|---|
| $\lbrace 3, 7, 10, 11, 9\rbrace $ | $3+7+10+11+9 = 40$ |
| $\lbrace 17, 14, 9\rbrace $ | $17+14+9 = 40$ |
| $\lbrace 3, 7, 10, 14, 6\rbrace $ | $3+7+10+14+6 = 40$ |

> ⚠️ **Inferred data:** the full list of 10 weights was shown on screen but not read out. From the answers, the items include weights $3, 6, 7, 9, 10, 11, 14, 17$. The remaining two weights are unknown.

**Counting the possibilities.**
- With $n$ items, each item is either in the subset or not, so there are $2^n$ subsets. These include the empty set $\emptyset$ and the full set.
- If the answer is **"yes"**, you can stop once you find a subset.
- To answer **"no"** correctly, in the worst case you must check all subsets.

**Enumeration as an algorithm.**
1. Check single items: $\binom{n}{1} = n$ checks.
2. Check pairs: $\binom{n}{2}$ checks.
3. Check triples, then quadruples, and so on.

Total number of checks:

```math
\binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{n} = \sum_{k=1}^{n} \binom{n}{k} = 2^n - 1
```
This uses $\sum_{k=0}^{n}\binom{n}{k} = 2^n$ and excludes the $k=0$ (empty) term. The work grows **exponentially** in $n$. For $n = 100$, $2^{100}$ is astronomically large.

### 2.4 Story: the chessboard and grains of wheat (exponential growth)

- Sissa invented *chaturanga* (early chess) and presented it to the king.
- The king offered a reward. Sissa asked for 1 grain of wheat on the 1st square, 2 on the 2nd, 4 on the 3rd, 8 on the 4th, doubling each time across all 64 squares.
- The king thought this was only a few grains and agreed. The treasurer later said it could not be paid.
- Square $k$ holds $2^{k-1}$ grains: square 1 has $2^0$, square 2 has $2^1$, …, square 64 has $2^{63}$.
- Total (not computed in class; added for completeness):

  $$\sum_{k=1}^{64} 2^{k-1} = 2^{64} - 1 \approx 1.8 \times 10^{19} \text{ grains.}$$

- **Lesson:** the king underestimated **compounding**, i.e. exponential growth. It feels small at the start and explodes at the end; he should have thought about the *last* square.
  - One version says Sissa was rewarded; another says he was executed.
- Exponential growth is slower than factorial growth but still overwhelming.

### 2.5 How problem size scales when computing power doubles (Big-O intuition)

**Setup.** Today we can solve problem size $n = 100$ in a given time. In about 4 years, computing power doubles, so twice as many steps fit in the same time. What new size $n'$ can we solve? Let $k$ be a constant.

| Time complexity | Equation | New solvable size $n'$ |
|---|---|---|
| $O(\log n)$ | $\log n' = 2\log 100$ | $n' = 100^2 = 10{,}000$ |
| $O(n)$ (linear) | $k\ n' = 2 \cdot k \cdot 100$ | $n' = 200$ |
| $O(n^2)$ (quadratic, e.g. basic sorting) | $k\ n'^2 = 2 \cdot k \cdot 100^2$ | $n' = 100\sqrt{2} \approx 141$ |
| $O(2^n)$ (exponential) | $k\ 2^{n'} = 2 \cdot k \cdot 2^{100} = k \cdot 2^{101}$ | $n' = 101$ |

**Working for the exponential case.**

```math
2 \cdot k \cdot 2^{100} = k \cdot 2^{n'} \;\Rightarrow\; k\,2^{101} = k\,2^{n'} \;\Rightarrow\; n' = 101
```
Four years of hardware progress gives exactly **one** more city in the routing problem.

A factorial algorithm is even worse (my remark, not from class): since $101! = 101 \times 100!$, doubling compute does not even reach $n' = 101$.

**Takeaways.**
- Polynomial-time (and $\log n$) algorithms scale well as your organisation or problem grows.
- Exponential and factorial algorithms do not scale.
- We want efficient methods, ideally polynomial-time.

### 2.6 Solving the assignment problem with LP (Excel Solver demo)

**Excel setup.**
- A $4\times 4$ distance matrix: dozers 1–4 (rows) by sites A–D (columns).
- A $4\times 4$ grid of yellow decision cells, where 1 means "this dozer goes to this site".
- Total distance = `SUMPRODUCT(distance matrix, assignment matrix)`.

**Worked numbers.**
- Arbitrary assignment 1→A, 2→B, 3→C, 4→D: total distance = **255**.
- An infeasible example: dozer 3 assigned to both C and D. Its row sum is 2, but each dozer must go to exactly one site.
- Solver's optimal solution: total distance = **150**.

> ⚠️ **Missing data:** the individual entries of the distance matrix were not read out. Only the totals 255 and 150 are known.

**Model.**

*Indices:* $i \in \lbrace 1,2,3,4\rbrace $ (dozers), $j \in \lbrace A,B,C,D\rbrace $ (sites).

*Parameters:* $d_{ij}$ = distance from dozer $i$ to site $j$ (distance units).

*Decision variables:*

```math
x_{ij} = \begin{cases} 1 & \text{if dozer } i \text{ is assigned to site } j \\ 0 & \text{otherwise} \end{cases}
```

*Model:*

```math
\begin{aligned}
\min \quad & Z = \sum_{i}\sum_{j} d_{ij}\, x_{ij} && \text{(total distance travelled)}\\
\text{s.t.} \quad & \sum_{j} x_{ij} = 1 \quad \forall i && \text{(each dozer goes to exactly one site: row sums = 1)}\\
& \sum_{i} x_{ij} = 1 \quad \forall j && \text{(each site receives exactly one dozer: column sums = 1)}\\
& x_{ij} \ge 0 \quad \forall i,j && \text{(non-negativity; binary not required, see below)}
\end{aligned}
```

**Solver settings.**

| Setting | Value |
|---|---|
| Set Objective | Total-distance cell, **Min** |
| By Changing Variable Cells | The 16 yellow cells |
| Constraints | Row-sum cells $= 1$; column-sum cells $= 1$ |
| Make Unconstrained Variables Non-Negative | ✔ |
| Solving Method | **Simplex LP** |

**Integrality property.** We do not need to declare the variables binary. The assignment problem's constraint structure guarantees that the LP optimum is already integer (0/1). You may still declare binary if you want.

**How did Solver do it?**
- It did *not* enumerate all $n!$ assignments.
- It used the **simplex method**, which does not evaluate every alternative but still guarantees optimality.
- *Why* simplex guarantees optimality is a core topic of the course.

### 2.7 Solving the subset-sum (truck) problem with integer programming

**Model.**

*Parameters:* $w_i$ = weight of item $i$ (tons), $i = 1,\dots,10$. Target $T = 40$ tons.

*Decision variables:*

```math
y_i = \begin{cases} 1 & \text{if item } i \text{ is loaded} \\ 0 & \text{otherwise} \end{cases}
```

*Feasibility version (no objective):*

```math
\begin{aligned}
\text{Find } \; & y_1,\dots,y_{10}\\
\text{s.t.} \quad & \sum_{i=1}^{10} w_i\, y_i = 40 && \text{(weight selected = target weight)}\\
& y_i \in \{0,1\} \quad \forall i && \text{(each item either loaded once or not)}
\end{aligned}
```

**Excel setup.**
- Yellow cells hold $y_i$.
- "Weight selected" = `SUMPRODUCT(weights, y)`. For example, selecting the 7 and 10 items gives 17.
- "Number of items selected" = `SUM(y)`.
- The objective box in Solver is left **empty**.

**Step-by-step demo.**
1. **First run: forgot the binary constraint.** Solver (Simplex LP) returned a value of about 5.7 for a single item. That means 5.7 copies of one item (e.g. $5.71 \times 7 \approx 40$), which is meaningless because you cannot load fractional or multiple copies.
2. **Added the binary constraint** $y_i \in \lbrace 0,1\rbrace $. Solver found five items: $7 + 10 + 3 + 14 + 6 = 40$.
   - Requiring binary variables is what makes this problem hard.
3. **Variant: minimise the number of items** (pack heavy items first).

   $$\min \sum_{i=1}^{10} y_i \quad \text{s.t.} \quad \sum_{i} w_i y_i = 40,\  y_i \in \lbrace 0,1\rbrace$$

   Optimum: **3 items**, $14 + 17 + 9 = 40$.

**Complexity notes.**
- Subset-sum is **NP-hard**. No polynomial-time algorithm is known for such problems.
- Integer programming (introduced in the last two classes of the course) is not polynomial-time but is fast in practice for course-sized problems.
- The assignment problem looks harder ($n!$ vs $2^n$ alternatives), but it is actually easier. Neither problem is solved by brute force, and the assignment problem has an efficient (polynomial) method via LP. The subset-sum problem does not.

**Q&A: can Solver list all subsets that reach 40?**
- No. Solver returns one solution.
- How integer programming works internally (branch and bound):
  - It solves the **LP relaxation** first (which is why 5.7 appeared).
  - It keeps track of **upper and lower bounds**.
  - It **branches** on a fractional variable, e.g. a variable at 0.4 is split into the cases $=0$ and $=1$.
- Solution pools can be built with extra effort.
- Similarly in LP, Solver can indicate that **alternate optima** exist but reports only one. Later we learn how to construct alternate optima.

**Q&A: does Solver always give the same combination?**
- Excel Solver is **deterministic**, so repeated runs give the same solution.
- Commercial solvers (Gurobi, CPLEX) may use randomised choices, e.g. which fractional variable (0.4 vs 0.45) to branch on. If that is switched on, runs can differ.

### 2.8 First LP formulation: furniture product mix (tables & chairs)

**Business problem.**
- A furniture shop makes **tables** and **chairs** using two limited weekly resources: woodwork (carpentry) and painting (varnishing).
- Goal: choose weekly production to maximise total profit without exceeding resource availability.

**Data.**

| | Table | Chair | Hours available / week |
|---|---|---|---|
| Woodwork (hrs/unit) | 4 | 3 | 240 |
| Painting (hrs/unit) | 2 | 1 | 100 |
| Profit per unit | 7 | 5 | |

> ⚠️ **Inferred:** the profit figures 7 and 5 come from the objective $7x_1 + 5x_2$ stated in class. The currency unit was not specified.

**Definitions.**
- **Decision variables:** quantities management has to decide, or that we want Solver to find. We must be able to write the objective and all constraints in terms of them.
- **Parameters:** known problem data (coefficients 4, 3, 2, 1, 7, 5 and capacities 240, 100).

**Decision variables.**
- $x_1$ = number of tables produced per week (units)
- $x_2$ = number of chairs produced per week (units)

**LP model (standard form).**

```math
\begin{aligned}
\max \quad & Z = 7x_1 + 5x_2 && \text{(total weekly profit)}\\
\text{s.t.} \quad & 4x_1 + 3x_2 \le 240 && \text{(woodwork hours used} \le \text{available)}\\
& 2x_1 + x_2 \le 100 && \text{(painting hours used} \le \text{available)}\\
& x_1,\, x_2 \ge 0 && \text{(non-negativity)}
\end{aligned}
```
This is the "mathematical programming" or "linear programming" formulation.

**Why non-negativity? (class discussion)**
- Quantities produced cannot be negative here.
- A negative $x_1$ (e.g. $-10$) would mean buying tables from the market instead of producing them.
- If the resources were **materials** (e.g. 240 kg iron, 100 kg aluminium), buying tables and disassembling them would return material. Then negative values might make sense.
- **Hours cannot be recovered** by disassembling a purchased table. So negative $x_1, x_2$ make no sense, and we must declare $x_1, x_2 \ge 0$.
- **Counter-example: portfolio problems.** A variable of $+10$ lakh means investing in an asset; $-10$ lakh means **shorting** (selling) it. There, negative values may be allowed.
- **Rule:** decide from the use case whether variables are sign-restricted.

**Excel Solver implementation (step by step).**
1. **Lay out the data.**
   - Columns headed $x_1$, $x_2$ with the coefficient rows: objective (7, 5), woodwork (4, 3), painting (2, 1).
   - A RHS column: 240, 100.
2. **Decision cells.** Yellow cells for $x_1$, $x_2$, to be filled by Solver.
   - Trial values were typed only to check the formulas. These are not assumptions.
   - With $x_1 = 1, x_2 = 2$: profit $= 7(1) + 5(2) = 17$ and woodwork $= 4(1) + 3(2) = 10$.
   - With $(1,1)$: profit $= 12$, woodwork $= 7$, painting $= 3$.
3. **Objective cell** (colour-coded blue): `=SUMPRODUCT(coefficients, decision cells)`.
4. **LHS cells** (hours used): `=SUMPRODUCT(row coefficients, $decision cells$)`. Use `$` absolute references on the decision cells so the formula can be copied down.
5. **Enable Solver if it isn't visible** (it ships with Excel):
   - **Windows:** File → Options → Add-ins (or type "Solver"/"Add-ins" in the search bar) → enable Solver Add-in. It then appears under the **Data** tab.
   - **Mac:** Tools → Excel Add-ins → tick Solver Add-in.
6. **Solver dialog:**

| Setting | Value |
|---|---|
| Set Objective | Profit cell, **Max** |
| By Changing Variable Cells | $x_1$, $x_2$ yellow cells |
| Subject to | LHS cells $\le$ RHS cells (both rows entered together) |
| Make Unconstrained Variables Non-Negative | ✔ |
| Solving Method | **Simplex LP** (everything is linear: all variables appear to power 1 in objective and constraints) |

**Optimal solution:** $x_1^\ast  = 30$ tables and $x_2^\ast  = 40$ chairs.

```math
Z^* = 7(30) + 5(40) = 210 + 200 = 410
```

Resource check:
- Woodwork: $4(30) + 3(40) = 240$ (binding, fully used).
- Painting: $2(30) + 40 = 100$ (binding, fully used).

**Graphical view (supplementary; the graphical method is next class).**

The feasible region is the polygon in the first quadrant bounded by the axes, the woodwork line $4x_1 + 3x_2 = 240$ and the painting line $2x_1 + x_2 = 100$.

| Corner point | How obtained | $Z = 7x_1 + 5x_2$ |
|---|---|---|
| $(0, 0)$ | origin | 0 |
| $(50, 0)$ | painting line meets $x_1$-axis | 350 |
| $(30, 40)$ | woodwork line ∩ painting line | **410 (optimal)** |
| $(0, 80)$ | woodwork line meets $x_2$-axis | 400 |

**Shadow prices (supplementary; not covered in class).**
- Solving the dual, or both constraints as binding, gives a shadow price of 1.5 per woodwork hour and 0.5 per painting hour.
- Check: $240(1.5) + 100(0.5) = 410$.
- This answers the "how much should I pay for an overtime hour?" question previewed in class.

**Preview of sensitivity analysis.** Solver's report gives:
- **shadow prices**: the value of one extra hour of woodwork or painting, i.e. what to pay for overtime;
- **reduced costs**: insight into which product mixes are viable;
- **allowable increase/decrease**: whether price fluctuations of tables or chairs change the optimal product mix.

The instructor stressed that *the optimal solution is not the most interesting part; the insights are.*

### 2.9 Why linear programming is so popular (three reasons)

1. **Wide applicability.** Even nonlinear problems can be approximated linearly, e.g. using tangents.
2. **Efficient solution methods.** Karmarkar (1984) gave a polynomial-time (interior-point) algorithm. LPs with millions of variables solve fast.
   - Side note: Khachiyan's ellipsoid method of 1979 was the first polynomial-time LP algorithm; Karmarkar's was the first practical one.
3. **Rich insights.** Sensitivity and dual information support managerial interpretation and decision-making.

---

## 3. Important for Exams / Assignments / Next Class

- **Prepare the Merton Truck case** ("mant/Martin truck" in the transcript) before next class. Understand the problem context thoroughly. The discussion will cover pitfalls managers face when solving real problems and the insights that can be generated.
- **Practice Excel Solver.** Make sure the add-in is enabled and that you can reproduce the furniture LP ($x_1 = 30$, $x_2 = 40$, $Z = 410$) on your own.
- **Next class:** graphical solution method (to build intuition for LP concepts), more formulation practice, and the Merton Truck case.
- Concepts likely to recur (emphasised in class):
  - the distinction between decision variables and parameters;
  - when non-negativity is or isn't appropriate;
  - why binary restrictions make problems hard (LP relaxation vs IP);
  - polynomial vs exponential vs factorial complexity;
  - the integrality property of assignment problems;
  - sensitivity terms: shadow price, reduced cost, allowable increase/decrease.
- No explicit exam statement was made in this session.

<!-- nav -->
← [Session 1 (2026-10-22)](DSM-109-1_2026-10-22_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 3 (2026-10-28)](DSM-109-3_2026-10-28_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
