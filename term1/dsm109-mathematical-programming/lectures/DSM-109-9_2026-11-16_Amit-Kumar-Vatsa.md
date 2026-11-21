---
course: DSM 109
date: 2026-11-16
start: 8:15pm
session: "9"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-109 · Session 9 (16 Nov 2026) · Amit Kumar Vatsa
## Shadow-Price Signs, Primal–Dual Conversion, and an Introduction to Integer Programming

---

## 1. Overview

This session continues the previous class's discussion of **shadow prices**. It starts with one general principle:

- If the feasible region **expands**, the optimal objective cannot get worse.
- If the feasible region **shrinks**, the optimal objective cannot get better.

The lecturer uses this principle to work out the **sign of the shadow price** for every combination of constraint type ($\le$, $\ge$, $=$) and objective (max or min). Shadow prices are then shown to be the variables of a second, closely related LP called the **dual**. The dual is motivated by a "buy my resources" business story using a three-product, two-resource example.

The session then covers:
- which problem to solve in practice (primal or dual), depending on the solution method;
- the general **primal → dual conversion rules**, demonstrated on a deliberately messy minimisation problem with mixed constraint and variable signs.

The last part introduces **integer linear programming (ILP/MILP)**:
- why integrality is needed (count variables, binary decisions, either–or and if–then logic);
- a graphical comparison of the LP optimum with the IP optimum;
- the bound relationship $Z_{LP}$ vs $Z_{IP}$.

The session closes with announcements about the quiz, project groups and the next class (Excel Solver + AI/Python on Google Colab).

---

## 2. Topics Covered (in order taught)

### 2.1 Recap from the previous class
- **Question asked:** In a maximisation LP, if you get *more* of a resource, can profit *decrease*?
  - For a **$\le$ constraint**: no.
  - For an **equality constraint**: yes, it can. Shadow prices of equality constraints can therefore be **positive or negative**.

### 2.2 The general principle: feasible region vs objective value

> **Rule.**
> - When the feasible region **expands**, the optimal objective function **cannot worsen**. It stays the same or improves.
> - When the feasible region **shrinks**, the optimal objective function **cannot improve**. It stays the same or worsens.

**Reasoning (from the board sketch with constraint 1 and constraint 2):**
- **Expansion:** "Expand" means every previously feasible point is still feasible, plus some new points.
  - The old optimal corner point is still available, so you can always do at least as well as before.
  - If a new corner point is better (e.g. when constraint 1's line shifts outward), the objective improves.
  - If not (e.g. when constraint 2 is relaxed but the old optimum stays optimal), the objective stays the same.
- **Shrinkage:** You *may* lose the previous optimal corner point.
  - If you lose it, the objective gets worse.
  - If you only lose some other part of the region, the objective is unchanged.
  - Either way, you cannot do better than before.
- **Equality constraint:** Here the feasible region neither expands nor shrinks. It **shifts entirely**.
  - Board example: $x_2 = 4$ versus $x_2 = 4 + 1 = 5$.
  - The feasible set moves to a different line. No old point remains feasible, so the new region is neither "larger" nor "smaller", just different.

### 2.3 Effect of adding 1 to the RHS of a single constraint

The lecturer stressed that this is about the feasible region of **that one constraint alone**, not the intersection of all constraints.

**(a) $\le$ constraint: adding 1 to the RHS always expands the region**

- **Example 1:** compare $3x_1 + 2x_2 \le 8$ with $3x_1 + 2x_2 \le 8 + 1$.
  - Every point satisfying the first also satisfies the second.
  - A point with $3x_1 + 2x_2 = 8.5$ satisfies only the second.
  - So the second region is larger.
- **Example 2:** the signs of the coefficients do not matter. Compare $-3x_1 - 8x_2 \le -16$ with $-3x_1 - 8x_2 \le -16 + 1$.
  - Anything $\le -16$ is automatically $\le -15$.
  - So the region again expands.

**(b) $\ge$ constraint: adding 1 to the RHS always shrinks the region**

- **Example:** compare $3x_1 + 5x_2 \ge 25$ with $3x_1 + 5x_2 \ge 25 + 1$.
  - Anything $\ge 26$ is also $\ge 25$, but not the other way round.
  - So the first constraint has the larger region.
- **Graphical illustration:** compare $x + y \ge 1$ (line through $(1,0)$ and $(0,1)$) with $x + y \ge 2$ (line through $(2,0)$ and $(0,2)$).
  - The "$\ge 1$" region is larger.
  - So raising the RHS from 1 to 2 shrinks the feasible region.

**(c) $=$ constraint: adding 1 to the RHS shifts the region entirely**

- **Example:** $x_2 = 4$ becomes $x_2 = 5$, a completely different line.

### 2.4 Sign of the shadow price: the full table

Recall that the shadow price is the change in the optimal objective per unit increase in the RHS. Combining §2.2 and §2.3 gives:

| Objective | Constraint | Effect of RHS $+1$ | Objective can't… | Shadow price |
|---|---|---|---|---|
| **Max** | $\le$ | expands | decrease | $\ge 0$ |
| **Max** | $\ge$ | shrinks | increase | $\le 0$ |
| **Max** | $=$ | shifts | — | **unrestricted** (any real number, incl. 0) |
| **Min** | $\le$ | expands | increase (cost can't go up) | $\le 0$ |
| **Min** | $\ge$ | shrinks | decrease (cost can't go down) | $\ge 0$ |
| **Min** | $=$ | shifts | — | **unrestricted** |

**Reminder on "better" and "worse":**
- **Max:** worse means a lower objective value.
- **Min (cost):** worse means a higher cost, and better means a lower cost.

**"Standard" constraints (the memory aid):**
- **Maximisation:** the natural constraint is **$\le$**, because profit is limited by available resources. Standard constraints have **non-negative** shadow prices.
- **Minimisation:** the natural constraint is **$\ge$**, e.g. "minimise $x_1 + x_2$ such that $x_1 \ge$ something, $x_2 \ge$ something". These also have **non-negative** shadow prices.

### 2.5 Primal and dual: intuition via a product-mix example

**Key idea:** Every LP has a closely related LP.
- If one is called the **primal**, the other is the **dual**.
- The **shadow prices of the primal are the decision variables of the dual.**

**Primal model (product mix):**

Decision variables:
- $x_1, x_2, x_3$ = units of products 1, 2, 3 to produce this month (units/month).

Data:
- Unit profits are 8, 4 and 5.
- Resource 1 has 18 (machine-)hours available; resource 2 has 11.

```math
\begin{aligned}
\max\quad & Z = 8x_1 + 4x_2 + 5x_3 && \text{(total profit)}\\
\text{s.t.}\quad & 3x_1 + 5x_2 + 2x_3 \le 18 && \text{(resource / raw material 1, hours)}\\
& 2x_1 + 3x_2 + 1x_3 \le 11 && \text{(resource / raw material 2, hours)}\\
& x_1, x_2, x_3 \ge 0 && \text{(non-negativity)}
\end{aligned}
```

Let $u_1, u_2$ be the **shadow prices** of the two resource constraints.

**Business story for the dual:**
- Your batch offers to **buy (take over) my resources** at per-unit prices $u_1$ (per hour of resource 1) and $u_2$ (per hour of resource 2).
- You pay $18u_1 + 11u_2$ in total, and naturally you want to **minimise** this payment.
- The offer must be lucrative enough that I see no point in producing any product myself.
  - **Product 1:** each unit earns 8 and uses 3 h of resource 1 and 2 h of resource 2. I give it up if $3u_1 + 2u_2 \ge 8$.
  - **Product 2:** I give it up if $5u_1 + 3u_2 \ge 4$.
  - **Product 3:** I give it up if $2u_1 + 1u_2 \ge 5$.

**Dual model:**

Decision variables:
- $u_1$ = price offered per hour of resource 1 (shadow price of constraint 1).
- $u_2$ = price offered per hour of resource 2 (shadow price of constraint 2).

```math
\begin{aligned}
\min\quad & W = 18u_1 + 11u_2 && \text{(total payment for the resources)}\\
\text{s.t.}\quad & 3u_1 + 2u_2 \ge 8 && \text{(product 1 not worth making myself)}\\
& 5u_1 + 3u_2 \ge 4 && \text{(product 2 not worth making myself)}\\
& 2u_1 + 1u_2 \ge 5 && \text{(product 3 not worth making myself)}\\
& u_1, u_2 \ge 0
\end{aligned}
```

> ⚠️ **ASR note:** The transcript says "2 U1 plus 2 U2 ≥ 5" for product 3. In the primal, product 3 uses 2 h of resource 1 and **1** h of resource 2, so the correct constraint is $2u_1 + u_2 \ge 5$.

**Key claims (proof promised for next class):**
- The primal and dual are "two sides of the same coin". Solving either gives the same solution.

**Link to the Excel sensitivity report:**
- **Primal:** the *Variable Cells* section shows $x_1, x_2, x_3$ (with reduced costs and allowable increase/decrease of objective coefficients). The *Constraints* section shows the shadow prices $u_1, u_2$ (with allowable increase/decrease of RHS).
- **Dual:** the roles swap. $u_1, u_2$ appear as variables, and $x_1, x_2, x_3$ appear as shadow prices.
- Solving an LP gives not only the optimal plan but also the **worth of every unit of each resource**.

### 2.6 Which one should you solve: primal or dual?

The answer depends on the solution method. Running example: a primal with **2 variables and 30 constraints**, so the dual has **30 variables and 2 constraints**.

- **Graphical method:** only 2 variables can be plotted, so you **solve the primal**. The dual solution is then read off from the corresponding primal solution.
- **Simplex or another algebraic method:** every inequality must become an equation by adding a **slack** (for $\le$) or subtracting a **surplus** (for $\ge$).

| | Original | After slack/surplus |
|---|---|---|
| Primal | 2 vars, 30 constraints | **32 variables, 30 equations** |
| Dual | 30 vars, 2 constraints | **32 variables, 2 equations** |

  - Both have 32 variables, but the dual has only 2 equations. Its simplex tableau (matrix) is much smaller, so the **dual is much easier**.
- **Practical rule:** we rarely solve graphically. **Solve whichever problem has fewer constraints.**

### 2.7 Primal → dual conversion rules

1. **Objective sense flips:** max ↔ min. The dual of the dual is the primal again.
2. **Definitions:**
   - **Standard variable** = non-negative variable ($\ge 0$).
   - **Standard constraint** = $\le$ in a **max** problem, $\ge$ in a **min** problem.
3. **Standard variables ↔ standard constraints.** A standard primal variable gives a standard dual constraint, and vice versa.
4. **Non-standard variables ↔ non-standard constraints**, and **unrestricted variables ↔ equality constraints** (and vice versa).
5. **Mechanics:**
   - Primal objective coefficients become dual RHS values.
   - Primal RHS values become dual objective coefficients.
   - The constraint matrix is transposed: primal **column** $j$ gives dual **constraint** $j$.
6. **Shortcut for dual variable signs:** use the shadow-price sign table in §2.4.

**Summary table.** Primal is **Min**, so the dual is **Max**. Read the rows from left to right; read right to left if the primal is Max.

| Primal (Min) | Dual (Max) |
|---|---|
| constraint $\ge$ (standard) | variable $u_i \ge 0$ |
| constraint $\le$ (non-standard) | variable $u_i \le 0$ |
| constraint $=$ | variable $u_i$ unrestricted |
| variable $x_j \ge 0$ (standard) | constraint $\le c_j$ (standard for max) |
| variable $x_j \le 0$ (non-standard) | constraint $\ge c_j$ |
| variable $x_j$ unrestricted | constraint $= c_j$ |

### 2.8 Worked example: dual of a "complicated" minimisation problem

The lecturer chose a messy problem on purpose so that one example covers every case. He noted that feasibility doesn't matter for the conversion: every primal has a dual.

> ⚠️ **Inferred numbers:** The RHS values were spoken unclearly ("40, 50, 50"). The dual objective stated was $40u_1 + 80u_2 + 50u_3$, so the RHS values are taken as **40, 80, 50**. Constraints 2 and 3 were not fully dictated. Their coefficients were reconstructed from the dual constraints the lecturer wrote, which are the transposed columns. Constraint 2's dictated start, "$2x_1 + 3x_2 - \dots$", matches this reconstruction.

**Primal:**

```math
\begin{aligned}
\min\quad & Z = -4x_1 + 8x_2 - 5x_3 + x_4\\
\text{s.t.}\quad & 3x_1 - 2x_2 + 6x_3 - x_4 \ge 40 && (\text{C1, shadow price } u_1)\\
& 2x_1 + 3x_2 - 5x_3 + 2x_4 \le 80 && (\text{C2, shadow price } u_2)\\
& 3x_1 - 5x_2 + x_3 + 2x_4 = 50 && (\text{C3, shadow price } u_3)\\
& x_1 \ge 0,\; x_2 \le 0,\; x_3 \text{ unrestricted},\; x_4 \ge 0
\end{aligned}
```

**Step 1: signs of the dual variables** (primal is Min):
- $u_1$: C1 is $\ge$, which is standard for min, so $u_1 \ge 0$.
- $u_2$: C2 is $\le$ in a min problem. RHS $+1$ expands the region, so cost can only stay the same or fall. Hence $u_2 \le 0$.
- $u_3$: C3 is an equality, so $u_3$ is **unrestricted**.

**Step 2: dual objective.** The primal is Min, so the dual is Max, and the primal RHS values become the dual objective coefficients:

```math
\max\; W = 40u_1 + 80u_2 + 50u_3
```

**Step 3: dual constraints.** There is one constraint per primal variable. Its coefficients come from that variable's column, and its RHS comes from the primal objective coefficients $-4, 8, -5, 1$. The variable $x_j$ is the shadow price of dual constraint $j$.
- **From $x_1$** (column $3, 2, 3$): $x_1 \ge 0$ is standard, so the constraint is standard for max, i.e. $\le$.
  - Check: a $\le$ constraint in a max problem has a non-negative shadow price, matching $x_1 \ge 0$.
- **From $x_2$** (column $-2, 3, -5$): $x_2 \le 0$ is non-standard, so the constraint is $\ge$.
  - Check: a $\ge$ constraint in a max problem has a non-positive shadow price.
- **From $x_3$** (column $6, -5, 1$): $x_3$ is unrestricted, so the constraint is $=$.
- **From $x_4$** (column $-1, 2, 2$): $x_4 \ge 0$, so the constraint is $\le$.

**Dual:**

```math
\begin{aligned}
\max\quad & W = 40u_1 + 80u_2 + 50u_3\\
\text{s.t.}\quad & 3u_1 + 2u_2 + 3u_3 \le -4 && (\text{from } x_1)\\
& -2u_1 + 3u_2 - 5u_3 \ge 8 && (\text{from } x_2)\\
& 6u_1 - 5u_2 + u_3 = -5 && (\text{from } x_3)\\
& -u_1 + 2u_2 + 2u_3 \le 1 && (\text{from } x_4)\\
& u_1 \ge 0,\; u_2 \le 0,\; u_3 \text{ unrestricted}
\end{aligned}
```

> ⚠️ **ASR/slip note:** The transcript says the last constraint is "$\le -1$". The coefficient of $x_4$ in the primal objective is $+1$, so the RHS should be $+1$.

### 2.9 Why primal–dual matters for algorithms
- Many algorithms work with both primal and dual solutions, e.g. transportation-problem algorithms and some graph/network techniques.
- **Stopping criterion:** at a point where **both the primal and the dual are feasible**, the solution is **optimal**.
- The lecturer promised to show next class why solving the primal and the dual gives the same solution.

### 2.10 Introduction to Integer Linear Programming (ILP / MILP)

**Definition:**
- An ILP still has a **linear objective and linear constraints**.
- **Some (MILP) or all (pure ILP) variables are restricted to integer values** instead of continuous ones.
- In Solver, this is added as an **extra constraint** ("int", or "bin" for binary).

**Use cases:**
1. **Discrete quantities.** Is $x_1 = 3.5$, $x_2 = 4.5$ acceptable? It depends on what the variables are.
   - Not acceptable for counts: 3.5 cars or 4.5 trucks makes no sense.
   - Fine for divisible quantities: kg of milk, curd or yogurt.
2. **Binary (0–1) decisions**, where you either do something or you don't:
   - **Knapsack / truck loading:** an item is either in the truck or not.
   - **Capital budgeting:** a project is undertaken or not.
   - **Facility location:** you either locate a warehouse or hospital at a site or you don't. You cannot locate 0.35 here and 0.65 there.
3. **Logical conditions modelled with binary variables.** These turn non-linear-looking logic into **linear constraints**. Details next class.
   - **Either–or constraints.** Example: a technological improvement lowers per-unit resource consumption. Product 1 currently uses 3 and 4 hours, product 2 uses 4 units, and so on. So *either* the current constraint *or* the improved constraint applies.
   - **If–then constraints.** Example from the slides: "If interest payouts [of B] and C together exceed 6 million, then A will not lend more than 20 million." (The wording is partly garbled in the ASR.)
   - **Bin packing:** pack all items into the **minimum number of trucks**.

**Graphical comparison of LP and IP:**
- The LP feasible region is a polygon. The integer-feasible solutions are the **lattice (integer) points** inside it.
- The LP optimum is a **corner point** in the direction of objective improvement. Often this corner is *not* an integer point, so it is not IP-optimal.
- The IP optimum is then some integer point **inside** the LP region. Which one depends on the slope of the objective.
- The two coincide only if the LP optimal corner happens to be integer.

**Bound relationship.** Adding integrality is an *extra constraint*, so it can only remove feasible points. By §2.2, the objective cannot improve:

```math
\text{Max problem: } Z_{LP} \ge Z_{IP} \qquad\qquad \text{Min problem: } Z_{LP} \le Z_{IP}
```

Here $Z$ is the optimal objective value. For a max problem the IP is no better than the LP (lower or equal profit). For a min problem the IP cost is no lower than the LP cost (higher or equal).

---

## 3. Exam / Assignment / Admin Notes

**Quiz (coming soon; the MSDSM office will send the schedule):**
- Multiple choice (MCQ) plus some **small numericals**.
- **Pen and paper**: no Excel, Solver, AI or screen switching.
- The **graphical solution method** will be asked.
- Described as **simple, but time-limited**, so speed matters.
- Content covered in class is sufficient.

**Course assessment:**
- Quiz.
- Exam.
- **Project**, with a report and a **viva**. The viva will also check whether mid-term and quiz marks are genuine.

**Project:**
- Form groups. The lecturer suggested 5; the class has 32 students, so **groups of 4** were agreed. Send the group list to the instructor.
- The instructor will give the topic/technique. Groups can choose the industry and application area.
- Submission is **after the end-term**, before a deadline to be announced (tied to the grade-submission deadline).

**Next class (Wednesday):**
- Why the primal and dual give the same solution.
- Integer programming with either–or and if–then logic, and the truck packing problem.
- Solving with **Excel Solver** and with **AI + Python on Google Colab** (modern/commercial solvers).

**Other:** The calendar for the next term will be shared (via "Alpej", per the ASR).

---

## 4. Quick Formula & Rule Sheet

**Region and objective:**
- Region expands, so the objective cannot worsen.
- Region shrinks, so the objective cannot improve.

**RHS $+1$:**
- $\le$: the region expands.
- $\ge$: the region shrinks.
- $=$: the region shifts.

**Shadow-price signs:**
- **Max:** $\le \Rightarrow \ge 0$; $\ge \Rightarrow \le 0$; $= \Rightarrow$ unrestricted.
- **Min:** $\le \Rightarrow \le 0$; $\ge \Rightarrow \ge 0$; $= \Rightarrow$ unrestricted.

**Dual of the product-mix example:**
- Primal: $\max\  8x_1+4x_2+5x_3$ subject to $3x_1+5x_2+2x_3\le 18$ and $2x_1+3x_2+x_3\le 11$, with $x \ge 0$.
- Dual: $\min\  18u_1+11u_2$ subject to $3u_1+2u_2\ge 8$, $5u_1+3u_2\ge 4$, $2u_1+u_2\ge 5$, with $u\ge 0$.

**Conversion rules:**
- max ↔ min.
- RHS ↔ objective coefficients.
- Transpose the constraint matrix.
- Standard ↔ standard, non-standard ↔ non-standard, unrestricted ↔ equality.

**Which problem to solve:** the one with fewer constraints when using simplex; the primal if it has 2 variables and you are solving graphically.

**Optimality:** if the primal and dual are both feasible at a point, that point is optimal.

**IP bounds:**
- Max: $Z_{LP} \ge Z_{IP}$.
- Min: $Z_{LP} \le Z_{IP}$.

<!-- nav -->
← [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
