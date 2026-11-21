---
course: DSM 109
date: 2026-11-18
start: 7:00pm
session: "10"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 9 (2026-11-16)](DSM-109-9_2026-11-16_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-109 Session 10: Primal–Dual Demo and Integer Programming Applications

**Session file:** DSM-109-10_2026-11-18_Amit-Kumar-Vatsa

---

## 1. Overview

This was the final teaching session of the course. A quiz was held at 9:30 pm, right after the lecture.

The session opened by finishing the primal–dual topic from the previous class. The instructor wrote the **dual of the Merton Truck problem**, solved it in Excel Solver, and showed that it gives the same information as the primal:

- the dual variables are the primal's shadow prices;
- the dual's shadow prices are the primal's optimal production quantities.

A student asked when to solve the primal versus the dual. This led to a short discussion of how commercial solvers (Gurobi, CPLEX) run primal simplex, dual simplex and interior-point methods in parallel.

The rest of the class covered **applications of integer linear programming (ILP)**:

1. A **capital budgeting (project selection)** problem with binary variables and logical constraints ("if–then", "at most one of").
2. An **either–or constraint** using a binary variable and the **big-M** technique, to decide whether to invest in a technology that reduces raw-material use.
3. A **bin-packing (truck loading)** problem, solved in Excel Solver and then in Google Colab with AI-generated Gurobi code.

The session closed with administrative notes on group projects and the end-term exam format.

---

## 2. Topics Covered (in order)

### 2.0 Recap of the previous class: three uses of integer programming

1. **Discrete quantities:** a variable must take integer values only.
2. **Binary (0/1) decisions:** yes/no choices.
3. **Logical conditions:** "if–then", "either–or" and "at most one" conditions turned into linear constraints using binary variables.

---

### 2.1 Primal–Dual demonstration: Merton Truck Company

> ⚠️ **Inferred data:** The transcript only reads out the objective coefficients of the dual (4000, 6000, 5000, 4500) and the primal profits (3000, 5000). The technology coefficients and the resulting shadow-price values below come from the standard Merton Truck case used earlier in the course. They are consistent with the optimum quoted in class ($`x_1 = 2000`$, $`x_2 = 1000`$).

#### Primal (maximise contribution)

**Decision variables**

- $`x_1`$ = number of Model 101 trucks produced (units/month)
- $`x_2`$ = number of Model 102 trucks produced (units/month)

**Model**

```math
\max\; Z = 3000x_1 + 5000x_2 \quad (\text{\$ contribution})
```

subject to:

| Constraint | Meaning |
|---|---|
| $`x_1 + 2x_2 \le 4000`$ | Engine assembly hours |
| $`2x_1 + 2x_2 \le 6000`$ | Metal stamping hours |
| $`2x_1 \le 5000`$ | Model 101 assembly hours |
| $`3x_2 \le 4500`$ | Model 102 assembly hours |
| $`x_1, x_2 \ge 0`$ | Non-negativity |

**Primal optimum**

- Production: $`x_1 = 2000`$, $`x_2 = 1000`$.
- Contribution: $`Z^* = 3000(2000) + 5000(1000) = \text{\$}11{,}000{,}000`$.
- Binding constraints: engine assembly ($`2000 + 2000 = 4000`$) and metal stamping ($`4000 + 2000 = 6000`$).
- Non-binding constraints: Model 101 assembly ($`4000 < 5000`$) and Model 102 assembly ($`3000 < 4500`$).

#### Dual (minimise the total value of resources)

**Dual variables**

$`u_1, u_2, u_3, u_4`$ = the worth (\$ per hour) of one additional hour in each department. These are the shadow prices of:

- engine assembly ($`u_1`$),
- metal stamping ($`u_2`$),
- Model 101 assembly ($`u_3`$),
- Model 102 assembly ($`u_4`$).

**Model**

```math
\min\; W = 4000u_1 + 6000u_2 + 5000u_3 + 4500u_4
```

subject to:

| Constraint | Meaning |
|---|---|
| $`u_1 + 2u_2 + 2u_3 \ge 3000`$ | Resources used by one Model 101 must be worth at least its \$3000 contribution |
| $`2u_1 + 2u_2 + 3u_4 \ge 5000`$ | Resources used by one Model 102 must be worth at least its \$5000 contribution |
| $`u_1, u_2, u_3, u_4 \ge 0`$ | Non-negativity |

**Primal → dual conversion rules shown in class**

- A primal max problem becomes a dual min problem.
- The primal right-hand sides (4000, 6000, 5000, 4500) become the dual objective coefficients.
- The primal constraint coefficient matrix is **transposed**. In Excel: Copy → **Paste Special → Transpose**.
- The primal objective coefficients (3000, 5000) become the dual right-hand sides.
- Primal $`\le`$ constraints become dual $`\ge`$ constraints.

**Excel Solver setup for the dual**

- Objective cell: `SUMPRODUCT(coefficients, variable cells)`, using `$` absolute references. Set to **Min**.
- Changing cells: the yellow cells $`u_1, \dots, u_4`$.
- Constraints: LHS (two rows) $`\ge`$ RHS.
- Tick non-negativity.
- Solving method: **Simplex LP**.

**Result (inferred values)**

The two dual constraints are solved simultaneously:

- Subtracting the first from the second gives $`u_1 = 2000`$.
- Substituting back gives $`u_2 = 500`$.
- $`u_3 = u_4 = 0`$, because those departments have slack in the primal.

```math
W^* = 4000(2000) + 6000(500) = \text{\$}11{,}000{,}000 = Z^*
```

**Key observation from the sensitivity reports**

- The dual's **variable values** are the primal's **shadow prices**.
- The dual constraints' **shadow prices** are 2000 and 1000, which are the primal's optimal quantities of Model 101 and Model 102.
- What appeared in the "constraints" section of one report appears in the "variables" section of the other.
- Conclusion: **the primal and the dual are the same problem; solving either gives the same information.**

#### Student Q&A: when to solve the primal or the dual?

- With 3 variables and 4 constraints, the choice makes little difference.
- The number of constraints drives the work in simplex. Each constraint needs a slack or surplus variable to become an equation.
  - **2 variables and 100 constraints** → 100 slack/surplus variables → **102 variables in 100 equations**. This is large.
  - **100 variables and 2 constraints** is algebraically much easier.
  - So the formulation with **fewer constraints is preferable**. This can be the dual.
- For very large LPs (millions of variables and constraints), commercial solvers such as **Gurobi** and **CPLEX** use a **concurrent** strategy:
  - one CPU core runs **primal simplex**;
  - one core runs **dual simplex**;
  - the remaining cores run the **interior point method** (Narendra **Karmarkar**, 1984);
  - the solver stops when the fastest one finishes. You can also tell modern solvers which algorithm to use.

---

### 2.2 Capital budgeting: project selection with binary variables

**Problem**

- Five projects are evaluated over a **3-year horizon**.
- Once a project is started, it must continue for all three years.
- Each project has a known expenditure in each year and an overall profit (net of expenses, time value considered).
- Available funds are **\$20 million in each year**. Spending in any year must not exceed this.

> ⚠️ **Data not read out:** The per-project expenditure and profit table was pasted into Excel and is not in the transcript. Write it as $`c_{ij}`$ (expense of project $`i`$ in year $`j`$) and $`p_i`$ (profit of project $`i`$). The numerical results quoted in class are recorded below.

#### Formulation

**Decision variables**

```math
x_i = \begin{cases} 1 & \text{if project } i \text{ is undertaken} \\ 0 & \text{otherwise} \end{cases} \qquad i = 1,\dots,5
```

**Model**

```math
\max\; Z = \sum_{i=1}^{5} p_i x_i \quad (\text{\$ million total profit})
```

subject to:

```math
\sum_{i=1}^{5} c_{ij} x_i \le 20 \qquad j = 1, 2, 3 \quad (\text{funds used in year } j \le \text{funds available})
```

```math
x_i \in \{0,1\} \qquad i = 1,\dots,5
```

**Excel layout**

- One row of yellow decision cells $`x_i`$ ("Project undertaken?").
- "Used funds" for year $`j`$ = `SUMPRODUCT(expense row of year j, x cells)`.
- "Available funds" = 20 for each year.
- "Total profit" = `SUMPRODUCT(profit row, x cells)`. This is the blue objective cell, set to Max.
- Constraint: Used funds $`\le`$ Available funds.

#### Step 1: LP relaxation (common mistake shown in class)

- If you only impose $`x_i \ge 0`$ and do **not** declare the variables binary, Solver returns fractional values, e.g. $`x = 1.8`$ (one value displayed as $`10^{-16}`$, which is effectively 0).
- That solution uses all funds exactly, with total profit 20.
- It is **not acceptable**: you cannot do a project 1.8 times.

#### Step 2: Binary model

- Add the constraint "$`x_i`$ = bin" in Solver.
- Optimal solution: **Projects 1, 2 and 3**, total profit = **16** (\$ million). Not all funds are used in every year.
- Swapping in another project (e.g. dropping one and adding another) violates a year's budget (used funds > 20). So 16 is the best possible.

#### Condition (a): Project 5 must be selected if either Project 1 or Project 3 is selected

**Truth table**

| $`x_1`$ | $`x_3`$ | Allowed $`x_5`$ |
|---|---|---|
| 1 | 1 | must be 1 |
| 1 | 0 | must be 1 |
| 0 | 1 | must be 1 |
| 0 | 0 | 0 **or** 1 (free) |

- If neither 1 nor 3 is chosen, Project 5 may still be chosen.
- So you **cannot** impose "$`x_1 + x_3 \ge 1`$ AND $`x_5 \ge 1`$". That wrongly forces Project 5 (and one of 1/3) always.
- An "if" statement or a $`\max`$ function cannot go into an LP directly, because it would be nonlinear.

**Linearisation (two equivalent routes discussed)**

- Logically: $`x_5 \ge \max(x_1, x_3)`$. This is nonlinear.
- Split it into two linear constraints. If $`x_5`$ is at least the max, it is at least each one:

```math
x_5 \ge x_1, \qquad x_5 \ge x_3
```

- Or add them, as a student suggested:

```math
x_1 + x_3 \le 2x_5 \quad \Longleftrightarrow \quad 2x_5 - x_1 - x_3 \ge 0
```

- Check: if $`x_1 = 1`$ and $`x_3 = 0`$, then $`2x_5 \ge 1`$, so $`x_5 = 1`$ for a binary variable. Both forms are valid for 0/1 variables.
- Aside (not from the lecture): the two separate constraints give a tighter LP relaxation.

**Excel implementation**

- Add a cell computing $`2x_5 - x_1 - x_3`$. Before adding the constraint, it showed $`-2`$, which violates the condition.
- Add the constraint "cell $`\ge 0`$" and re-solve.

**Result**

- Profit falls from **16 to 14**.
- Solution: **Projects 2 and 5**.
- Principle: *adding a constraint can never improve the objective; it can only worsen it or leave it unchanged.*
- Project 5 is taken without 1 or 3, which the condition allows.

#### Condition (b): At most one of Projects 2 and 3 can be selected

```math
x_2 + x_3 \le 1
```

- The current solution (Projects 2 and 5) already satisfies this.
- It is not cut off, so the optimum stays at **14**.

---

### 2.3 Either–or constraints with big-M: technology investment decision

**Problem**

- A company makes Products 1 and 2.
- Unit contributions are **\$15** and **\$20**.
- Both products use two raw materials, RM1 and RM2:

| | Product 1 | Product 2 | Available |
|---|---|---|---|
| RM1 (units/unit) | 2 | 5 | 100 |
| RM2, current technology | 3 | 4 | 80 |
| RM2, after improvement | 2 | 3 | 80 |

- A technology investment reduces RM2 usage from (3, 4) to (2, 3).
- Its amortised fixed cost is **\$180 per planning period** (e.g. weekly).
- **Question:** should we invest?

**Naive approach**

- Solve two LPs: one with RM2a, one with RM2b.
- If the improvement in objective exceeds \$180, invest.
- The instructor instead solved it as **one** model with a binary variable.

**Why a single model needs a trick**

- All constraints given to a solver act together as an **AND**.
- The feasible region is the intersection of all constraints' regions.
- So the "either RM2a or RM2b" choice must be built in using $`y`$ and big-M.

#### Formulation

**Decision variables**

- $`x_1`$ = units of Product 1 produced
- $`x_2`$ = units of Product 2 produced
- $`y = 1`$ if the technology investment is made, $`0`$ otherwise
- $`M`$ = a large constant ("big M"). In class, $`M = 1000`$; 100 was mentioned as possibly enough.

**Model**

```math
\max\; Z = 15x_1 + 20x_2 - 180y \quad (\text{\$ net contribution})
```

subject to:

| Constraint | Meaning |
|---|---|
| $`2x_1 + 5x_2 \le 100`$ | RM1 availability |
| $`3x_1 + 4x_2 \le 80 + My`$ | RM2a (old technology); active only if $`y = 0`$ |
| $`2x_1 + 3x_2 \le 80 + M(1-y)`$ | RM2b (new technology); active only if $`y = 1`$ |
| $`x_1, x_2 \ge 0`$, $`y \in \{0,1\}`$ | Non-negativity and binary |

**How the big-M switch works**

- When $`y = 0`$:
  - RM2a reads $`3x_1 + 4x_2 \le 80`$ and is active.
  - RM2b's RHS becomes $`80 + M = 1080`$, which is effectively $`\infty`$, so it is redundant.
- When $`y = 1`$:
  - RM2a's RHS becomes $`1080`$ and is redundant.
  - RM2b reads $`2x_1 + 3x_2 \le 80`$ and is active.

**Excel layout**

All variables are moved to the left-hand side (useful on Mac Solver):

| Row | $`x_1`$ | $`x_2`$ | $`y`$ | | RHS |
|---|---|---|---|---|---|
| Objective | 15 | 20 | $`-180`$ | max | |
| RM1 | 2 | 5 | 0 | $`\le`$ | 100 |
| RM2a | 3 | 4 | $`-1000`$ | $`\le`$ | 80 |
| RM2b | 2 | 3 | $`+1000`$ | $`\le`$ | 1080 |

- RM2a: $`3x_1 + 4x_2 - My \le 80`$.
- RM2b: $`2x_1 + 3x_2 + My \le 80 + M = 1080`$.

**Solver settings**

- Objective: `SUMPRODUCT` of coefficients and variable cells, set to **Max**.
- Changing cells: $`x_1, x_2, y`$.
- Constraints: LHS $`\le`$ RHS, and $`y`$ = **bin**.
- Note: for an integer program, Excel Solver gives **no sensitivity report**.

#### Solution (verified graphically)

**No investment ($`y = 0`$)**

- Constraints: $`2x_1 + 5x_2 \le 100`$ and $`3x_1 + 4x_2 \le 80`$.
- Feasible region corners:
  - $`(0,0)`$: $`Z = 0`$
  - $`(26.67, 0)`$: $`Z = 400`$
  - $`(0, 20)`$: $`Z = 400`$
- The RM1 and RM2a lines meet at $`(0, 20)`$, so RM1 adds no further corner.
- The objective is parallel to RM2a, since $`15/20 = 3/4`$. So the whole RM2a edge is optimal with $`Z = \text{\$}400`$ (alternative optima).

**Investment ($`y = 1`$)**

- Constraints: $`2x_1 + 5x_2 \le 100`$ and $`2x_1 + 3x_2 \le 80`$.
- Feasible region corners:
  - $`(0,0)`$: $`Z = 0`$
  - $`(40, 0)`$: $`Z = 600`$
  - $`(25, 10)`$: $`Z = 575`$ (intersection of RM1 and RM2b)
  - $`(0, 20)`$: $`Z = 400`$
- Best is $`(40, 0)`$ with gross $`Z = 600`$. Net of investment: $`600 - 180 = \text{\$}420`$.

**Decision**

- Since $`420 > 400`$, **invest** ($`y = 1`$, $`x_1 = 40`$, $`x_2 = 0`$).
- The gross gain is \$200. Investing pays off whenever the fixed cost is below \$200.

**Constraint status in Excel (matches the class output)**

- RM2b: $`2(40) = 80`$, **binding**.
- RM2a: LHS $`= 3(40) - 1000 = -880 \le 80`$, redundant by a huge margin. This is by design.
- RM1: $`80 \le 100`$, slack.

**Sensitivity check done in class**

- Changing the fixed cost to **\$250** makes investment unprofitable.
- Solver then sets $`y = 0`$. RM2a becomes the constraint that matters, and RM2b becomes badly non-binding.

> Aside (not from the lecture): $`M`$ only needs to exceed the largest possible violation. Here $`3x_1 + 4x_2 \le 150`$ given RM1, so any $`M \ge 70`$ works. Overly large $`M`$ values can cause numerical trouble in solvers.

---

### 2.4 Bin packing: minimising the number of trucks

**Problem**

- A dispatch manager at an e-commerce warehouse must load **10 pre-packed cartons** onto trucks.
- Each truck has capacity **25 tons**.
- Items **cannot be split**.
- Goal: **minimise the number of trucks used.**

| Item $`i`$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Weight $`w_i`$ (tons) | 7 | 10 | 3 | 11 | 8 | 14 | 15 | 17 | 6 | 9 |

**Bounds**

- Total weight $`= 100`$ tons.
- Lower bound $`= 100/25 = 4`$ trucks, if the packing is perfect.
- 5 trucks were made available ($`j = 1,\dots,5`$), which is certainly enough.

#### Formulation

**Decision variables**

```math
y_j = \begin{cases} 1 & \text{if truck } j \text{ is used} \\ 0 & \text{otherwise} \end{cases} \qquad j = 1,\dots,5
```

```math
x_{ij} = \begin{cases} 1 & \text{if item } i \text{ is loaded on truck } j \\ 0 & \text{otherwise} \end{cases}
```

**Model**

```math
\min\; Z = \sum_{j=1}^{5} y_j \quad (\text{number of trucks used})
```

subject to:

```math
\sum_{j=1}^{5} x_{ij} = 1 \qquad i = 1,\dots,10 \quad (\text{each item goes on exactly one truck})
```

```math
\sum_{i=1}^{10} w_i x_{ij} \le 25\,y_j \qquad j = 1,\dots,5 \quad (\text{capacity; an unused truck carries nothing})
```

```math
x_{ij} \in \{0,1\}, \quad y_j \in \{0,1\}
```

**Notes on the formulation**

- In Excel, the assignment constraint was entered as $`\sum_j x_{ij} \ge 1`$. At the optimum this is equivalent to $`= 1`$. The Gurobi code used $`= 1`$.
- The capacity constraint links $`x`$ and $`y`$:
  - if $`y_j = 0`$, the RHS is 0 and nothing can be packed in truck $`j`$;
  - if $`y_j = 1`$, the RHS is 25.

**Excel layout and tips**

- A 10 × 5 grid of yellow binary cells $`x_{ij}`$, plus a row of $`y_j`$ cells.
- "Used capacity" for truck $`j`$ = `SUMPRODUCT(weights, column j)`.
- "Available capacity" = $`25 \times y_j`$. Do not put the fixed 25 in a yellow cell; yellow is for decision variables only.
- **Mac Solver workaround:** keep all variables on the LHS. Define "Capacity left" = $`25y_j - \sum_i w_i x_{ij}`$ and require **Capacity left $`\ge 0`$**. On Windows you can enter Used $`\le`$ Available directly.
- **Debugging moments in class:**
  - The instructor first typed "capacity left $`\ge 1`$", which is wrong; it must be $`\ge 0`$.
  - A bad formula (a multiplication instead of a subtraction in one cell) made Solver report that **linearity conditions are not satisfied**. Fixing "Capacity left = Available − Used" resolved it.
- Solver settings:
  - Objective: Min (sum of $`y_j`$).
  - Changing cells: $`y_j`$ and $`x_{ij}`$.
  - Constraints: row sums $`\ge 1`$, capacity left $`\ge 0`$, both variable sets = bin.
  - Method: **Simplex LP**.

#### Excel solution: 4 trucks, each loaded to exactly 25 tons

| Truck | Items (weights) | Total |
|---|---|---|
| 1 | unused | 0 |
| 2 | 8 + 17 | 25 |
| 3 | 7 + 3 + 6 + 9 | 25 |
| 4 | 10 + 15 | 25 |
| 5 | 11 + 14 | 25 |

**Why truck 1 is empty (student question)**

- All trucks are identical, so Solver may leave any one unused.
- To force trucks to be used in order (1 before 2, etc.), add **symmetry-breaking constraints**:

```math
y_1 \ge y_2 \ge y_3 \ge y_4 \ge y_5
```

- These were not included in class.

#### Same problem with AI + Gurobi (Google Colab)

- The prompt to Gemini in Colab was roughly: *"Solve a bin packing problem, bins have capacity 25 each, item weights 7, 10, 3, 11, 8, 14, 15, 17, 6, 9; use the Gurobi solver and solve as integer programming."*
- The generated code ran `pip install gurobipy` and built the same model:
  - each item assigned to exactly one bin;
  - $`\sum_i w_i x_{ij} \le 25\,y_j`$.
- Gurobi also found **4 bins**, e.g. bin 1 = $`\{10, 6, 9\}`$ = 25. Its packing differed from Excel's but was equally optimal.
- The instructor encouraged using AI tools, and Gurobi/CPLEX, for the course projects.

---

## 3. Exam, Assignment and Admin Notes

- **Quiz:** at **9:30 pm**, right after this session.
- **End-term exam:** **MCQ-based**, with **no Excel modelling** in the exam ("lots can go wrong there").
  - You **may be given Excel output, e.g. a sensitivity report**, and asked to interpret it and draw insights.
  - Be comfortable reading shadow prices, final values and slack. Know the primal–dual relationship: dual values = primal shadow prices, and vice versa.
- **Group project:**
  - Form **groups of four**.
  - The **CR must email the instructor** the group list.
  - Topics and instructions will follow by email.
  - Use Excel Solver, Python/Gurobi/CPLEX, and AI assistance as appropriate.
- This was the last lecture. The instructor plans to offer another course in second year and is open to working with students on problems of interest.

---

### Quick-reference: integer-programming modelling tricks from this session

| Logic | Linear constraint (binary variables) |
|---|---|
| If $`x_1 = 1`$ or $`x_3 = 1`$, then $`x_5 = 1`$ | $`x_5 \ge x_1,\ x_5 \ge x_3`$ (or $`x_1 + x_3 \le 2x_5`$) |
| At most one of projects 2 and 3 | $`x_2 + x_3 \le 1`$ |
| Constraint A applies if $`y = 0`$, constraint B if $`y = 1`$ | $`g_A(x) \le b_A + My`$; $`g_B(x) \le b_B + M(1-y)`$ |
| Fixed cost $`F`$ incurred only if $`y = 1`$ | Subtract $`Fy`$ in the objective |
| Item $`i`$ assigned to exactly one bin | $`\sum_j x_{ij} = 1`$ |
| Use a bin's capacity only if the bin is opened | $`\sum_i w_i x_{ij} \le C\,y_j`$ |
| Symmetry breaking for identical bins | $`y_1 \ge y_2 \ge \cdots`$ |

<!-- nav -->
← [Session 9 (2026-11-16)](DSM-109-9_2026-11-16_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
