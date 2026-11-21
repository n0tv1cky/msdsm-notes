---
course: DSM 109
date: 2026-10-28
start: 8:15pm
session: "3"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 2 (2026-10-23)](DSM-109-2_2026-10-23_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 4 (2026-10-30)](DSM-109-4_2026-10-30_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 (Session 3): The Merton Truck Case: Contribution vs. Apportioned Profit, and LP Formulation

**Instructor:** Amit Kumar Vatsa  **Date:** 28 Oct 2026

---

## 1. Overview

This session analysed the **Merton Truck Company** case before moving on to more linear programming. Merton makes two truck models (101 and 102) and must plan its monthly production mix across four departments with limited machine hours. Two managers disagree:

- The **sales manager** says Model 101 loses money on every unit and should be dropped.
- The **controller** says Model 101 output should be increased.

The class showed that the sales manager's argument rests on an **incorrect profit expression**. That expression spreads the fixed overhead across each truck as if it were a per-unit cost. The correct expression uses **contribution margins** (price minus variable cost) and subtracts total fixed cost separately. The instructor illustrated the same error with a Delhi–Indore flight example, and showed how Merton had apportioned the engine-assembly fixed overhead.

The problem was then solved by **logical reasoning (a "swap" argument)**. This raises profit by USD 0.5 million, moving production from $(x_1, x_2) = (1000, 1500)$ to $(2000, 1000)$. The class then discussed the drawbacks of that approach and wrote the **LP formulation**. Solving it with Excel Solver and the graphical method, along with sensitivity analysis, is planned for the next class.

---

## 2. Topics Covered (in order)

### 2.1 Context and tools
- In the previous class an LP was formulated and solved in **Excel Solver**.
- In future sessions the class will use **AI to help formulate** problems and solve them with **Google OR-Tools** or the **Gurobi** library on **Google Colab**.

### 2.2 Merton Truck case data

**Products:** two truck models, Model 101 and Model 102. The planning horizon is **one month**.

**Four departments** (abbreviations used in class):

| Abbrev. | Department |
|---|---|
| EA | Engine Assembly |
| MS | Metal Stamping |
| A101 | Model 101 Assembly line |
| A102 | Model 102 Assembly line |

**Table A: machine hours required per truck, and monthly capacity**

| Department | Model 101 (hrs/truck) | Model 102 (hrs/truck) | Available hrs/month |
|---|---|---|---|
| Engine Assembly | 1 | 2 | 4,000 |
| Metal Stamping | 2 | 2 | 6,000 |
| Model 101 Assembly | 2 | 0 | 5,000 |
| Model 102 Assembly | 0 | 3 | 4,500 |

**Current production:** 1,000 units of Model 101 and 1,500 units of Model 102 per month.

**Prices and costs per truck (USD)**

| Item | Model 101 | Model 102 |
|---|---|---|
| Selling price | 39,000 | 38,000 |
| Direct material | 24,000 | 20,000 |
| Direct labour | 4,000 | 4,500 *(inferred, see note)* |
| Total overhead (fixed apportioned + variable) | 12,205 *(inferred)* | 11,430 *(inferred)* |
| of which variable overhead | 8,000 | 8,500 |
| **Total "cost" as reported by the company** | **40,205** | **35,930** |

> **Inferred numbers.** The ASR garbled several figures ("40,25", "12,25", "4205").
> - Model 101 total cost is 40,205. This matches the stated loss of 1,205 per unit, since $39{,}000 - 40{,}205 = -1{,}205$.
> - Model 101 overhead is then $40{,}205 - 24{,}000 - 4{,}000 = 12{,}205$.
> - Model 102 direct labour of 4,500 is back-calculated from the stated contribution of 5,000: $38{,}000 - 20{,}000 - 8{,}500 - 5{,}000 = 4{,}500$.
> - Model 102 overhead is then $35{,}930 - 20{,}000 - 4{,}500 = 11{,}430$.

**Other data mentioned**
- Total fixed overhead across all departments is **USD 8.6 million per month**.
- Fixed overhead in Engine Assembly alone is **USD 1.7 million**. Fixed overheads for the other departments were not read out.
- Engine Assembly overhead per Model 101 truck is **USD 2,525**. Of this, **USD 2,100 is variable** and **USD 425 is apportioned fixed overhead**.
- The case states Metal Stamping is running at **83.3% capacity**.

### 2.3 Cost concepts (definitions discussed in class)
- **Direct material cost.** The cost of materials that go directly into each truck, such as metal sheets, tyres and gearboxes.
- **Direct labour cost.** The cost of labour working directly on each truck at a work centre.
  - Supervisors and managers are *indirect* labour, or fixed overhead.
  - Caveat: if workers were on a fixed monthly salary, direct labour would not be variable. The case does not say, so the class **assumed hourly/contractual labour**, making direct labour a **variable cost**.
- **Variable overhead.** Overhead that varies with output. Examples: electricity consumed in production, coolants, consumables used per truck.
- **Fixed overhead.** Costs incurred whether or not anything is produced. Examples: management and supervisor salaries, rent, office air-conditioning.
- **Apportioned overhead.** The reported overhead figure per truck (e.g. 2,525) is the variable part (2,100) plus a share of fixed overhead allocated per unit (425).

### 2.4 Decision variables
- $x_1$ = number of Model 101 trucks produced per month (units/month)
- $x_2$ = number of Model 102 trucks produced per month (units/month)
- Current plan: $x_1 = 1000$, $x_2 = 1500$.

### 2.5 The sales manager's argument ("Profit Expression A")
The sales manager's quote was: *"Why don't we just stop making Model 101 trucks? As I see it, we are losing \$1,205 for each Model 101 truck we sell."*

His argument uses the company's full (apportioned) unit costs:

```math
\text{Profit}_A = (39{,}000 - 40{,}205)\,x_1 + (38{,}000 - 35{,}930)\,x_2 = -1{,}205\,x_1 + 2{,}070\,x_2
```

On this expression, every extra Model 101 truck appears to reduce profit by USD 1,205.

### 2.6 The controller's argument
- The controller recommends **increasing** Model 101 production.
- Reasoning: few Model 101s are made, so fixed cost (e.g. of the Model 101 assembly line) is absorbed by few units. This inflates the per-unit cost.
- Making more units spreads the fixed cost over a larger base, so Model 101 would "look" profitable.

The instructor's key point was that the maths must be checked first. If Expression A were correct, the sales manager would be right. **"Garbage in, garbage out":** an optimisation model built on a wrong expression gives wrong answers.

### 2.7 The correct profit expression ("Profit Expression B"), using contribution margin
Subtract only the **variable costs** (direct material + direct labour + variable overhead) inside the brackets, then subtract total fixed cost once:

```math
\text{Profit}_B = (39{,}000 - 24{,}000 - 4{,}000 - 8{,}000)\,x_1 + (38{,}000 - 20{,}000 - 4{,}500 - 8{,}500)\,x_2 - 8{,}600{,}000
```

```math
\boxed{\text{Profit}_B = 3{,}000\,x_1 + 5{,}000\,x_2 - 8{,}600{,}000}
```

- The contribution margin of Model 101 is USD 3,000 per truck.
- The contribution margin of Model 102 is USD 5,000 per truck.

**Which expression is correct?** Test it with zero production, $x_1 = x_2 = 0$:
- Expression A gives profit $= 0$.
- Expression B gives profit $= -8.6$ million.

Fixed costs do not disappear when nothing is produced, so **Expression B is correct**.

**How the two expressions relate**
- Expression A is what you get when some apportioning logic folds the fixed cost term into the per-unit coefficients.
- The two expressions agree **only at the production level used for the apportioning** $(1000, 1500)$. Check:
  - A: $-1{,}205(1000) + 2{,}070(1500) = 1{,}900{,}000$
  - B: $3{,}000(1000) + 5{,}000(1500) - 8{,}600{,}000 = 1{,}900{,}000$
- Because the analysis is about *changing* $x_1$ and $x_2$, we must use Expression B.

**Conclusion:**
- Model 101 has a **positive contribution**, so it is not loss-making. The sales manager's argument fails.
- Both models are worth producing. The real question is the **right balance (product mix)**.
- "Once you resolve the conflict, about 80–90% of the job is done; the rest is analysis."
- This error is common in industry.

### 2.8 Illustration: Delhi–Indore flight example
- Flight with 100 seats. Fixed cost of flying is Rs. 4,00,000 (4 lakh). Variable cost is Rs. 200 per passenger. Let $x$ = number of passengers.
- **Expression A (apportioned):** spread the fixed cost over 100 seats, giving $400{,}000/100 = 4{,}000$ per seat. Then

  $$C_A = (4{,}000 + 200)\ x = 4{,}200\ x$$

- **Expression B (correct):**

  $$C_B = 200\ x + 400{,}000$$

- **B is correct.** At $x = 0$, A says cost is 0, but the 4 lakh fixed cost does not vanish.
- The two expressions agree **only at $x = 100$**: $4{,}200 \times 100 = 420{,}000 = 200 \times 100 + 400{,}000$. They differ at every other value.

### 2.9 How Merton apportioned fixed overhead (Engine Assembly example)
This was shown for understanding only. It is not needed for the analysis, because **fixed cost should not be apportioned at all**.

- Fixed overhead in Engine Assembly is USD 1.7 million.
- Engine Assembly hours used at current production:
  - Model 101: $1 \times 1000 = 1{,}000$ hrs, which is **25%** of the 4,000 hrs used.
  - Model 102: $2 \times 1500 = 3{,}000$ hrs, which is **75%**.
- Fixed overhead per Model 101 truck:

  $$\frac{0.25 \times 1{,}700{,}000}{1000} = 425 \text{ USD/truck}$$

- Fixed overhead per Model 102 truck:

  $$\frac{0.75 \times 1{,}700{,}000}{1500} = 850 \text{ USD/truck}$$

- Hence the Model 101 Engine Assembly overhead is $2{,}100 + 425 = 2{,}525$.

Any such allocation rule is "made-up logic" and leads to incorrect decisions. This is where Merton went wrong.

### 2.10 Method 1: Logical reasoning (brute force / first principles)

**Step 1: Capacity utilisation at current production $(1000, 1500)$**

| Dept | Hours used | Available | Utilisation |
|---|---|---|---|
| EA | $1(1000) + 2(1500) = 4{,}000$ | 4,000 | 100% (bottleneck) |
| MS | $2(1000) + 2(1500) = 5{,}000$ | 6,000 | 83.3% (1,000 hrs spare) |
| A101 | $2(1000) = 2{,}000$ | 5,000 | 40% |
| A102 | $3(1500) = 4{,}500$ | 4,500 | 100% (bottleneck) |

The naive conclusion is that EA and A102 are the bottlenecks, so we should add capacity there. The instructor warned this is the **wrong approach**. Do not think about expanding capacity until the problem has been solved optimally, because the true bottleneck may be different once resources are used well.

**Step 2: Define a "swap"**
- EA is full, so raising $x_1$ requires freeing EA hours.
- One swap means **decrease Model 102 by 1 unit and increase Model 101 by 2 units**.

Effect of one swap on each department:
- **EA:** frees $1 \times 2 = 2$ hrs and uses $2 \times 1 = 2$ hrs, so net change is **0**.
- **MS:** uses $2 \times 2 - 1 \times 2 = 4 - 2 = +2$ hrs per swap.
- **A101:** uses $2 \times 2 = +4$ hrs per swap. *(Not computed in class; 3,000 spare hrs would allow 750 swaps, so A101 does not limit.)*
- **A102:** frees 3 hrs per swap, so it is no longer a constraint.

**Step 3: Profit change per swap**, using contribution margins:

```math
\Delta \text{Profit} = +2(3{,}000) - 1(5{,}000) = 6{,}000 - 5{,}000 = +1{,}000 \text{ USD per swap}
```

**Step 4: Maximum number of swaps.** Metal Stamping is the limiting department:

```math
\frac{1{,}000 \text{ spare hrs}}{2 \text{ hrs/swap}} = 500 \text{ swaps}
```

**Step 5: Result**
- Profit increase: $500 \times 1{,}000 = 500{,}000$ USD, i.e. **USD 0.5 million**.
- New production plan:
  - $x_1 = 1000 + 2(500) = 2000$
  - $x_2 = 1500 - 500 = 1000$
- The instructor stated that no further improvement is possible from here.

*Check (my own, not done in class):*
- New contribution is $3{,}000(2000) + 5{,}000(1000) = 11{,}000{,}000$.
- New profit is $11{,}000{,}000 - 8{,}600{,}000 = 2{,}400{,}000$, up from 1.9 million.
- Hours used at $(2000, 1000)$: EA $= 4{,}000/4{,}000$; MS $= 6{,}000/6{,}000$; A101 $= 4{,}000/5{,}000$; A102 $= 3{,}000/4{,}500$.
- So the **binding constraints at the improved plan are EA and MS**, not EA and A102. This confirms the warning about identifying bottlenecks too early.

A student asked where the 3,000 and 5,000 came from. Answer: they are the **coefficients of Profit Expression B** (contribution margins).

**Disadvantages of the logical-reasoning approach** (from class discussion):
1. It is **tedious**. Every time the data change you must start afresh.
2. It is **impractical for large problems**. With many variables and constraints there are exponentially many trade-offs to examine.
3. It **cannot be automated** and is hard to teach to others.

These drawbacks are why we use a **systematic LP formulation plus a solver**.

### 2.11 Method 2: LP formulation (to be solved next class)

**Decision variables**
- $x_1$ = number of Model 101 trucks produced per month (trucks/month)
- $x_2$ = number of Model 102 trucks produced per month (trucks/month)

**Objective.** Maximise total monthly contribution in USD/month. The fixed cost of 8.6 million is a constant, so maximising contribution also maximises profit.

```math
\max \; Z = 3{,}000\,x_1 + 5{,}000\,x_2
```
Equivalently, maximise profit $= 3{,}000\ x_1 + 5{,}000\ x_2 - 8{,}600{,}000$.

**Constraints.** In each department, hours used must not exceed hours available (machine-hours/month).

```math
\begin{aligned}
\text{subject to}\quad
& 1\,x_1 + 2\,x_2 \le 4{,}000 && \text{(Engine Assembly hours)}\\
& 2\,x_1 + 2\,x_2 \le 6{,}000 && \text{(Metal Stamping hours)}\\
& 2\,x_1  \le 5{,}000 && \text{(Model 101 Assembly hours)}\\
&  3\,x_2 \le 4{,}500 && \text{(Model 102 Assembly hours)}\\
& x_1,\; x_2 \ge 0 && \text{(non-negativity)}
\end{aligned}
```

Integrality was not imposed in class; trucks are discrete, but the LP relaxation is used.

**Equality (standard) form with slack variables.** This was not written in class but is useful for simplex and sensitivity work later. $s_1, \dots, s_4$ are the unused hours in EA, MS, A101 and A102:

```math
\begin{aligned}
\max\; Z &= 3{,}000\,x_1 + 5{,}000\,x_2 + 0\,s_1 + 0\,s_2 + 0\,s_3 + 0\,s_4\\
\text{s.t.}\quad & x_1 + 2x_2 + s_1 = 4{,}000\\
& 2x_1 + 2x_2 + s_2 = 6{,}000\\
& 2x_1 + s_3 = 5{,}000\\
& 3x_2 + s_4 = 4{,}500\\
& x_1, x_2, s_1, s_2, s_3, s_4 \ge 0
\end{aligned}
```

At current production $(1000, 1500)$ the slacks are $s_1 = 0$, $s_2 = 1{,}000$, $s_3 = 3{,}000$, $s_4 = 0$.

*Preview, my own corner-point check (the graphical method is planned for next class).* The feasible region in the $(x_1, x_2)$ plane has these corner points:

| Corner point | How it arises | $Z$ (USD) |
|---|---|---|
| $(0, 0)$ | origin | 0 |
| $(2500, 0)$ | A101 limit on the $x_1$-axis | 7.5 M |
| $(2500, 500)$ | A101 meets MS | 10.0 M |
| $(2000, 1000)$ | MS meets EA | **11.0 M** |
| $(1000, 1500)$ | EA meets A102 | 10.5 M |
| $(0, 1500)$ | A102 limit on the $x_2$-axis | 7.5 M |

The optimum is $x_1 = 2000$, $x_2 = 1000$ with $Z = 11$ million, so profit is $2.4$ million. This matches the swap result.

---

## 3. Important Points / What's Coming

**Explicit exam flags:** none were mentioned. The instructor did emphasise these points:
- **Use contribution margin (price minus variable cost) in LP objectives. Never use costs that include apportioned fixed overhead.** Fixed cost is a separate constant term.
- **Test any cost or profit expression at zero output.** Fixed costs must remain.
- An apportioned expression matches the true one **only at the production level used for apportioning**. It is invalid when the decision variables change.
- **"Garbage in, garbage out":** formulate the correct expression before optimising.
- **Do not decide where to add capacity before solving optimally.** Apparent bottlenecks at the current plan (EA and A102) are not the binding constraints at the optimum (EA and MS).
- Resolving the conceptual conflict is "80–90% of the job."

**Next class**
- Solve the Merton LP with **Excel Solver** (students are encouraged to try it beforehand).
- Solve it **graphically** and use the graph to introduce **sensitivity analysis**.

**Admin:** lecture notes will be uploaded as PDFs to the shared Google Drive folder.

<!-- nav -->
← [Session 2 (2026-10-23)](DSM-109-2_2026-10-23_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 4 (2026-10-30)](DSM-109-4_2026-10-30_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
