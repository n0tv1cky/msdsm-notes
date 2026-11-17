---
course: DSM 102
date: 2026-11-13
start: 7:00pm
session: "18"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 17 (2026-11-02)](DSM-102-17_2026-11-02_Abhirup-Datta.md) · [All lectures](./) · [Session 19 (2026-11-14)](DSM-102-19_2026-11-14_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 · Session 18: Red Brand Canners Case, LP Formulation and Excel Solver

**Instructor:** Abhirup Datta · **Date:** 2026-11-13

> **Note on content:** This course is listed as *Programming Fundamentals for Data Science*, but this session contains **no Python**. It continues a linear-programming (LP) case study, the **Red Brand Canners** case. The problem is formulated by hand on an iPad and then solved in **Excel Solver**. The only "code" is Excel formulas and Solver settings, which are reconstructed below. A Python equivalent is added at the end as a clearly labelled supplement. It was **not** shown in class.

---

## 1. Overview

This session continues the Red Brand Canners case from the previous class. It first recaps why the tomato cost is **not** a variable cost. The 3 million lb of tomatoes were already bought in bulk at 18¢/lb, so that cost does not disappear if nothing is produced. It is therefore excluded when computing **contribution per case** for the three products: whole tomatoes, juice and paste. The instructor then builds a full LP model:

- **Decision variables:** six, one per grade (A/B) per product.
- **Objective:** maximize total contribution.
- **Constraints:** supply (2), demand (3) and quality/ratio (2), plus non-negativity.

The ratio constraints are rewritten in linear form. The model is entered in Excel using `SUMPRODUCT` with absolute (`$`) references and solved with Solver (Simplex LP). The results are read off: the optimal production mix, profit after subtracting the sunk tomato cost, and the fact that grade A is never used for paste. The class then starts reading the **Sensitivity Report**, beginning with the shadow price of grade-A supply ($0.271/lb). The recording ends just as the instructor is about to test the shadow price by raising grade-A supply by 100 lb.

---

## 2. Topics Covered (in order)

### 2.1 Recap: Fixed (sunk) vs. variable cost

- **Test for a variable cost:** ask "If I produce **zero** units of this product, does this cost go away?"
  - If **no**, it is fixed or sunk, not variable.
- The tomatoes were already procured: $3{,}000{,}000 \text{ lb} \times \$0.18/\text{lb} = \$540{,}000$.
  - This cost is incurred whether or not whole tomatoes, juice or paste are produced.
  - It is therefore **not** subtracted when computing contribution.
- The same reasoning was applied to the earlier "Modern Press" example.

### 2.2 Contribution per case

**Definition:**
$$\text{Contribution} = \text{Selling price} - \text{all variable costs}$$

The tomato cost is excluded from the variable costs. Exhibits 2 and 3 of the case agree on these values:

| Product | Contribution ($/case) | lb per case | Contribution ($/lb) |
|---|---|---|---|
| 1. Whole tomatoes | 4.44 | 18 | $4.44/18 \approx 0.2467$ |
| 2. Juice | 3.96 | 20 | $3.96/20 = 0.198$ |
| 3. Paste | 5.55 | 25 | $5.55/25 = 0.222$ |

### 2.3 Decision variables

The variables are measured in **pounds of tomatoes of each grade used for each product**:

- $x_{A1}$, $x_{B1}$: lb of grade A / grade B used for **whole tomatoes**
- $x_{A2}$, $x_{B2}$: lb of grade A / grade B used for **juice**
- $x_{A3}$, $x_{B3}$: lb of grade A / grade B used for **paste**

**Discussion point about $x_{A3}$:**
- A student (Rahul, per the transcript) suggested dropping $x_{A3}$. The case says paste can be made entirely from grade B.
- The instructor kept it anyway. Using grade A for paste is *not prohibited*, so the solver is left to decide.
- The solver later confirmed $x_{A3} = 0$.

### 2.4 Formulation in words

- **Objective:** maximize total contribution.
  - Maximizing contribution is preferred to maximizing profit. Profit also includes fixed costs, which cannot be changed, so it is simpler to maximize contribution.
- **Constraints:**
  - Supply
  - Demand
  - Quality (ratio constraints derived by the *alligation* method in the previous class)

### 2.5 Objective function (unit conversion)

The coefficient is in \$/case and each variable is in lb. Divide by lb/case so that the case and lb units cancel, leaving \$:

$$\max \; Z = \frac{4.44}{18}(x_{A1}+x_{B1}) + \frac{3.96}{20}(x_{A2}+x_{B2}) + \frac{5.55}{25}(x_{A3}+x_{B3})$$

### 2.6 Constraints

**Supply (lb):**
$$x_{A1}+x_{A2}+x_{A3} \le 600{,}000$$
$$x_{B1}+x_{B2}+x_{B3} \le 2{,}400{,}000$$

**Demand.** Demand is given in cases. Multiply by lb/case so that both sides of each inequality are in pounds (*dimensional consistency*):
$$x_{A1}+x_{B1} \le 800{,}000 \times 18 \quad (=14{,}400{,}000)$$
$$x_{A2}+x_{B2} \le 50{,}000 \times 20 \quad (=1{,}000{,}000)$$
$$x_{A3}+x_{B3} \le 80{,}000 \times 25 \quad (=2{,}000{,}000)$$

**Why "$\le$" is safe for demand here:**
- This is a **maximization** problem. If a product is profitable, the solver will try to meet as much demand as possible.
- In a **cost-minimization** problem, "$\le$" demand constraints would give the trivial answer "produce nothing, zero cost".

**Quality (ratio) constraints.** These come from the alligation result in the previous class.

- Whole tomatoes need grade A : grade B at least 3 : 1:
$$\frac{x_{A1}}{x_{B1}} \ge 3 \;\Longrightarrow\; x_{A1} - 3x_{B1} \ge 0$$
- Juice needs grade A : grade B at least 1 : 3:
$$\frac{x_{A2}}{x_{B2}} \ge \frac{1}{3} \;\Longrightarrow\; 3x_{A2} - x_{B2} \ge 0$$

**Key technique: linearizing a ratio constraint.**
- A ratio of variables is **non-linear**, so LP cannot use it directly.
- Multiply through by the denominator (valid because the variables are $\ge 0$).
- Move every term to the left-hand side, leaving 0 on the right.

**Non-negativity:**
$$x_{A1}, x_{B1}, x_{A2}, x_{B2}, x_{A3}, x_{B3} \ge 0$$

The model has 7 functional constraints (2 supply + 3 demand + 2 quality) plus non-negativity.

### 2.7 Excel implementation (live demo)

**Spreadsheet layout:**
- Yellow cells hold the variables (the solver fills them in).
- One row holds the objective coefficients.
- Each constraint is one row with its LHS and RHS.
- A blue cell holds the objective.

Cell addresses were not spoken, so the ones below are **illustrative**:

```excel
' Objective coefficients (row 3), variables (yellow, row 4):  B..G = xA1 xB1 xA2 xB2 xA3 xB3
B3: =4.44/18    C3: =4.44/18    D3: =3.96/20    E3: =3.96/20    F3: =5.55/25    G3: =5.55/25

' Objective cell (blue) — total contribution
H3: =SUMPRODUCT($B$3:$G$3, B4:G4)

' Constraint LHS (one row each), RHS typed alongside
Supply A:        =B4+D4+F4              <=  600000
Supply B:        =C4+E4+G4              <=  2400000
Demand whole:    =B4+C4                 <=  800000*18
Demand juice:    =D4+E4                 <=  50000*20
Demand paste:    =F4+G4                 <=  80000*25
Quality whole:   =B4-3*C4               >=  0
Quality juice:   =3*D4-E4               >=  0

' Profit after sunk tomato cost
=H3 - 0.18*3000000
```

The objective cell is certain to be `SUMPRODUCT` with `$` references; that was stated in class. Which range carried the `$` signs is my inference. Typing every LHS as a plain sum is also my simplification. The instructor may have used `SUMPRODUCT` for the constraint rows too.

**Solver dialog (Data → Solver):**

1. **Set Objective:** the blue cell, set to **Max**.
2. **By Changing Variable Cells:** the yellow cells.
3. **Subject to the Constraints:**
   - Add all five `<=` rows together in one entry (LHS range `<=` RHS range).
   - Add both `>=` rows together in a second entry.
4. Non-negativity was not explicitly mentioned. In Excel it is normally the checkbox *"Make Unconstrained Variables Non-Negative"* (inferred).
5. **Solving Method:** Simplex LP.
6. Click Solve, then select the **Sensitivity Report**.

### 2.8 Results

**Pounds used per product (stated in class):**

| Product | lb of tomatoes |
|---|---|
| Whole tomatoes | 700,000 |
| Juice | 300,000 |
| Paste | 2,000,000 |

**Notes on the results:**
- Paste is at its demand limit.
- $x_{A3} = 0$: the solver chose not to use grade A for paste.
- The grade-A/B split below was **not read out**. It is my derivation from the binding constraints, so check it against your own solution:
  - $x_{A1}=525{,}000$, $x_{B1}=175{,}000$
  - $x_{A2}=75{,}000$, $x_{B2}=225{,}000$
  - $x_{A3}=0$, $x_{B3}=2{,}000{,}000$
- The total contribution value was not read aloud. Computed from the above, it is about $\$676{,}067$.

**Profit after the sunk cost:**
$$\text{Profit} = \text{Contribution} - 0.18 \times 3{,}000{,}000$$
This is about $\$136{,}067$ (my computation). The instructor noted it is still profitable.

### 2.9 Sensitivity report: shadow prices (started at the end)

- **Grade-A supply constraint:**
  - LHS = RHS = 600,000, so all grade A is used and the constraint is **binding**.
  - **Shadow price = 0.271.**
- **Interpretation:** if grade-A supply increased by **1 lb**, total contribution would rise by **\$0.271**. This holds only within the report's *allowable increase/decrease* range.
  - A student phrased this as "at most 0.271". The correct reading is that the objective changes by **exactly** the shadow price per unit, within the allowable range.
- **Planned demo (cut off):**
  - Note the current solution.
  - Raise grade-A supply by 100 lb.
  - Re-solve. Contribution should rise by $100 \times 0.271 = \$27.10$.
- **Extra values (my own dual calculation, not stated in class):**
  - Grade-B shadow price $\approx 0.174$.
  - Paste-demand shadow price $\approx 0.048$.

---

## 3. Functions, Operators and Tools Introduced

| Item | Meaning |
|---|---|
| `SUMPRODUCT(range1, range2)` | Multiplies matching cells of two ranges and sums the results. Used here as coefficients × variables for the objective. |
| `$` (e.g. `$B$3`) | Absolute reference. It freezes the row and/or column so a formula can be copy-pasted without the reference shifting. |
| `<=`, `>=` | Constraint relations entered in the Solver dialog. |
| Solver: *Set Objective / Max / By Changing Variable Cells* | Defines what is optimized and which cells the solver may change. |
| Solver: *Add Constraint* | Constraints of the same direction can be added as one block (LHS range vs RHS range). |
| Solver: *Simplex LP* | The solving engine for linear models. Use it whenever the model is linear. |
| Sensitivity Report | Shows final values, shadow prices and allowable ranges for each constraint. |
| Shadow price | Change in the optimal objective per unit increase in a constraint's RHS, valid within the allowable range. |

---

## 4. Rules, Common Mistakes and Tips

- **Do not treat sunk or bulk-purchased costs as variable costs.** Use the "produce zero, does the cost vanish?" test.
- **Keep units consistent.** $/case coefficients must be divided by lb/case when the variables are in lb. Demand in cases must be multiplied by lb/case.
- **Linearize ratios** before entering them in an LP: $\frac{x}{y} \ge k \Rightarrow x - ky \ge 0$.
- **"$\le$" demand constraints are fine in maximization**, but they produce a trivial zero solution in cost minimization.
- **Keep a questionable variable** (like $x_{A3}$) if it is not prohibited. The solver will set it to zero if it is not useful.
- **Use `$` absolute references** in the `SUMPRODUCT` so the formula can be copied to the constraint rows.
- **Group constraints of the same type** in Solver to save entry time.
- **Choose Simplex LP** and request the Sensitivity Report.

## 5. Exam/Assignment Flags

Nothing was explicitly flagged as "on the exam". The instructor emphasized these as the key takeaways:

- The variable-vs-fixed cost reasoning
- The contribution-per-case values (4.44, 3.96, 5.55)
- Linearizing the quality constraints
- Interpreting shadow prices from the sensitivity report

Analysis of the sensitivity report continues next session.

---

## Supplement (NOT from lecture): Python equivalent

This is provided for practice in this Python-focused course.

```python
from scipy.optimize import linprog

c = [-4.44/18, -4.44/18, -3.96/20, -3.96/20, -5.55/25, -5.55/25]  # negate to maximize
# variable order: xA1, xB1, xA2, xB2, xA3, xB3
A_ub = [
    [1, 0, 1, 0, 1, 0],    # supply A
    [0, 1, 0, 1, 0, 1],    # supply B
    [1, 1, 0, 0, 0, 0],    # demand whole
    [0, 0, 1, 1, 0, 0],    # demand juice
    [0, 0, 0, 0, 1, 1],    # demand paste
    [-1, 3, 0, 0, 0, 0],   # xA1 - 3xB1 >= 0  ->  -xA1 + 3xB1 <= 0
    [0, 0, -3, 1, 0, 0],   # 3xA2 - xB2 >= 0  ->  -3xA2 + xB2 <= 0
]
b_ub = [600_000, 2_400_000, 800_000*18, 50_000*20, 80_000*25, 0, 0]
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)]*6, method="highs")
print(res.x, -res.fun, -res.fun - 0.18*3_000_000)
print(res.ineqlin.marginals)  # shadow prices; sign flipped because the objective was negated
```

**Notes on the code:**
- `linprog` only minimizes, so the objective is negated to maximize.
- `>=` rows must be multiplied by $-1$ to become `<=` rows.

<!-- nav -->
← [Session 17 (2026-11-02)](DSM-102-17_2026-11-02_Abhirup-Datta.md) · [All lectures](./) · [Session 19 (2026-11-14)](DSM-102-19_2026-11-14_Abhirup-Datta.md) →
<!-- /nav -->
