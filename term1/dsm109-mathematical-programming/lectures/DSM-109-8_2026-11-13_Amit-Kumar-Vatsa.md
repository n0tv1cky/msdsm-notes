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

# DSM-109 Session 8: Sensitivity Analysis (Red Brand Canners) and the Signs of Shadow Prices

**Session file:** DSM-109-8_2026-11-13_Amit-Kumar-Vatsa

> **Note on sources:** The ASR wrote the case name as "red brand Canvas". It is the classic **Red Brand Canners** tomato case. Some case data was never read aloud in this session; it was covered in the previous class. Those numbers are reconstructed from the standard case and checked against the Solver outputs quoted in class. They are marked **(inferred)**.

---

## 1. Overview

The session finishes the Red Brand Canners case by reading the Solver **sensitivity report**.

- **Shadow prices** are interpreted with units and used for decisions:
  - **Grade A supply** is worth about 27.1¢/lb. The reason is not a single product's margin; it is a *change in product mix*.
  - **Grade B supply** is worth about 17.3¢/lb.
  - **Paste demand** is worth about 4.83¢/lb.
- Two business decisions follow: whether to buy extra Grade A tomatoes on the market, and how large a marketing budget is justified.
- **Reduced cost** of an unused variable ($x_{AP}$, Grade A into paste) is interpreted and verified in Solver.
- The case closes with a **sunk-cost** lesson: the tomato purchase cost is irrelevant to the product-mix decision.

The instructor then starts the theory. A small two-variable LP is solved graphically and its shadow prices are found by hand. Changing a $\le$ constraint to an $=$ constraint shows why:

- in a **maximisation** problem, a $\le$ constraint can never have a negative shadow price;
- $\ge$ and $=$ constraints can.

The next class formalises this through **duality**, after which the course moves to **integer programming**.

---

## 2. Topics Covered (in order)

### 2.1 Red Brand Canners: the model (recap, reconstructed)

**Business problem.** Red Brand Canners has already bought 3,000,000 lb of tomatoes. It must decide how to split Grade A and Grade B tomatoes among three products:

- whole canned tomatoes (W)
- tomato juice (J)
- tomato paste (P)

The aim is to maximise contribution.

**Data**

| Item | Value | Source |
|---|---|---|
| Total tomatoes | 3,000,000 lb (20% Grade A, 80% Grade B) | inferred (standard case) |
| Grade A supply | 600,000 lb | inferred; consistent with the optimal solution and the "allowable increase 600,000" quoted |
| Grade B supply | 2,400,000 lb | inferred |
| Quality points | A = 9, B = 5 | inferred (standard case) |
| Minimum average quality | W ≥ 8, J ≥ 6, P ≥ 5 | inferred (standard case) |
| Demand (lb) | W: 14,400,000; J: 1,000,000; P: 2,000,000 | J = 1,000,000 stated by a student; P = 2,000,000 consistent with the binding solution; W inferred |
| Contribution per lb, excluding tomato cost | W ≈ \$0.2467; J = \$0.198; P ≈ \$0.222 | J stated in class; W ≈ 0.246–0.247 stated (ASR garbled "24.246"); P back-calculated from the shadow prices (see 2.3) |

**Decision variables.** $x_{ij}$ = pounds of grade $i \in \{A, B\}$ used in product $j \in \{W, J, P\}$ (lb).

**Linearising the quality requirements.** Each average-quality requirement becomes a ratio constraint:

- **Whole tomatoes:** $\dfrac{9x_{AW} + 5x_{BW}}{x_{AW} + x_{BW}} \ge 8 \;\Rightarrow\; x_{AW} \ge 3x_{BW}$
- **Juice:** $\dfrac{9x_{AJ} + 5x_{BJ}}{x_{AJ} + x_{BJ}} \ge 6 \;\Rightarrow\; 3x_{AJ} \ge x_{BJ}$
- **Paste:** an average of at least 5 is always met, since both grades score $\ge 5$.

**Model (objective in \$, all constraints in lb)**

$$
\begin{aligned}
\max\ Z =\ & 0.2467(x_{AW}+x_{BW}) + 0.198(x_{AJ}+x_{BJ}) + 0.222(x_{AP}+x_{BP}) \\[4pt]
\text{s.t.}\quad & x_{AW}+x_{AJ}+x_{AP} \le 600{,}000 && \text{(Grade A supply)}\\
& x_{BW}+x_{BJ}+x_{BP} \le 2{,}400{,}000 && \text{(Grade B supply)}\\
& x_{AW}+x_{BW} \le 14{,}400{,}000 && \text{(whole-tomato demand)}\\
& x_{AJ}+x_{BJ} \le 1{,}000{,}000 && \text{(juice demand)}\\
& x_{AP}+x_{BP} \le 2{,}000{,}000 && \text{(paste demand)}\\
& x_{AW} - 3x_{BW} \ge 0 && \text{(whole-tomato quality} \ge 8)\\
& 3x_{AJ} - x_{BJ} \ge 0 && \text{(juice quality} \ge 6)\\
& x_{ij} \ge 0 \quad \forall i, j
\end{aligned}
$$

The Solver model entered the quality constraints in **ratio form**, e.g. $x_{AW}/x_{BW} \ge 3$. That is why the instructor said their shadow prices are "managerially too convoluted" to interpret.

**Optimal solution (consistent with all numbers quoted in class)**

| Product | Total (lb) | Grade A | Grade B |
|---|---|---|---|
| Whole (W) | 700,000 | 525,000 | 175,000 |
| Juice (J) | 300,000 | 75,000 | 225,000 |
| Paste (P) | 2,000,000 | 0 | 2,000,000 |

- **Binding constraints:** Grade A supply, Grade B supply, paste demand, and both quality ratios.
- **Non-binding constraints:** whole-tomato demand and juice demand.

### 2.2 Shadow price of Grade A supply: 0.271 \$/lb

**Experiment in Solver**

1. The Grade A right-hand side was raised by 100 lb and the model re-optimised.
2. The objective rose by exactly \$27.1, which is $100 \times 0.271$.
3. The RHS was then reverted to the original value.

**Puzzle.** No product earns 27.1¢/lb (W ≈ 24.6¢, J = 19.8¢). How can one pound of Grade A be worth more than any product's margin?

**Explanation: the product mix shifts.** With 100 more lb of Grade A:

- Whole tomatoes: $700{,}000 \to 700{,}150$, an increase of **150 lb**.
- Juice: $300{,}000 \to 299{,}950$, a decrease of **50 lb**.
- Paste: unchanged (it is at its demand limit).

Grade A lets more Grade B be "upgraded" into whole tomatoes. The quality ratio is 3 A : 1 B, so some B is pulled out of juice.

Check that the resources balance:

- Grade A used: $0.75(150) - 0.25(50) = 100$ ✓
- Grade B used: $0.25(150) - 0.75(50) = 0$ ✓

Net change in contribution:

$$
\Delta Z = 150(0.2467) - 50(0.198) \approx 37.0 - 9.9 = 27.1
$$

**Business meaning**

- Extra Grade A obtained free is worth 27.1¢/lb.
- The company should therefore pay **less than 27.1¢/lb** for additional Grade A.
- The tomato cost is *not* in the objective, which is why "free" is the reference point.

**Case decision.** The case offers **80,000 lb of Grade A at 25.5¢/lb**.

- Is the purchase within the range where the shadow price holds? Yes: $80{,}000 \le$ allowable increase of $600{,}000$.
- Is the price acceptable? Yes: $25.5 < 27.1$.
- **Buy it.**

### 2.3 Shadow price of Grade B supply: 0.173 \$/lb

- One more lb of Grade B (obtained free) raises contribution by about 17.3¢.
- Pay **less than 17.3¢/lb** for extra Grade B.

Check, with paste fixed at its demand: solve $0.75\Delta W + 0.25\Delta J = 0$ and $0.25\Delta W + 0.75\Delta J = 1$. This gives $\Delta W = -0.5$ and $\Delta J = 1.5$, so

$$
\Delta Z = -0.5(0.2467) + 1.5(0.198) \approx 0.173 \checkmark
$$

**Comparison with Myers's implied costs** (from the previous class):

| Grade | Myers's implied cost | Shadow price |
|---|---|---|
| A | 27.96¢ | 27.1¢ |
| B | 15.54¢ (ASR also mentions "15.90"; unclear) | 17.3¢ |

- The closeness for Grade A is "like an accident".
- Grade B is worth *more* to the business than Myers estimated.
- Shadow prices are the meaningful measure. They tell you the maximum rate at which to compensate farmers for extra supply, which is a variable cost.

### 2.4 Shadow prices of the demand constraints

**Whole-tomato and juice demand: shadow price 0.** These constraints are not binding (for example, juice uses 300,000 lb against 1,000,000 lb demand).

- Do not spend on advertising to raise these demands.
- You cannot even meet the current demand, so more demand adds nothing.

**Paste demand: shadow price 0.0483 \$/lb.**

- *Units:* the constraint is in lb and the objective in \$. So each extra **pound** of paste demand raises contribution by about **4.83¢**.
- *Marketing question:* marketing promises +1 lb of paste demand for every 5¢ spent. Should you do it?
  - **No**, because $5 > 4.83$.
  - The marketing spend per lb of extra demand must stay below 4.83¢.
  - This is how shadow prices guide the **marketing budget**.

**Deriving the paste contribution (inferred).** Raising paste demand by 1 lb uses 1 lb of Grade B, which is worth 0.173. So

$$
c_P - 0.173 = 0.0483 \;\Rightarrow\; c_P \approx 0.222
$$

### 2.5 Shadow prices of the ratio (quality) constraints

- These are **$\ge$ constraints**, and their shadow prices came out **negative**.
- The managerial interpretation of "one more unit of the ratio" is convoluted, so it was not pursued.
- **Observation:** in a maximisation problem, $\le$ constraints never have negative shadow prices, but $\ge$ constraints can. This is formalised in 2.8.

### 2.6 Reduced cost

- All reduced costs are 0 except for $x_{AP}$ (Grade A into paste), which is the only variable at 0. Its reduced cost is **−0.097**.
- **Rule (maximisation):** a variable at zero has a reduced cost $\le 0$. Basic (positive) variables have a reduced cost of 0.

**Meaning 1: penalty for forcing the variable in.** Forcing one lb of $x_{AP}$ into the solution changes the objective by −0.097. Check, using the shadow prices of Grade A supply and paste demand:

$$
c_P - u_A - u_P \approx 0.222 - 0.271 - 0.0483 \approx -0.097
$$

**Meaning 2: the threshold for entry.** The objective coefficient of $x_{AP}$ must rise by more than 0.097 before it enters the optimal solution.

**Solver demonstration**

1. Add **0.098** to the coefficient of $x_{AP}$ and re-solve.
2. $x_{AP}$ becomes positive.
3. Much of the Grade A goes into paste.
4. Whole-tomato production drops to **zero**, because whole tomatoes need Grade A.

### 2.7 Case conclusion: sunk cost

- The tomato cost (\$540,000 for 3,000,000 lb at 18¢/lb in the standard case, **inferred**) has already been incurred.
- Accounting schemes that split this cost between Grade A and Grade B, as Myers did, are a "meaningless exercise". The cost is **sunk** and does not disappear even if nothing is produced.
- The correct objective therefore **excludes the tomato cost**.

### 2.8 Theory: when can shadow prices be negative? (graphical example)

**Problem 1 ($\le$ constraints).** $x_1$ is the highly profitable product.

$$
\begin{aligned}
\max\ Z =\ & 20x_1 + x_2\\
\text{s.t.}\quad & x_1 + x_2 \le 10 && \text{(Constraint 1, shadow price } u_1)\\
& x_2 \le 4 && \text{(Constraint 2, shadow price } u_2)\\
& x_1, x_2 \ge 0
\end{aligned}
$$

*Feasible region:* a quadrilateral bounded by the axes, the line $x_2 = 4$, and the line $x_1 + x_2 = 10$.

| Corner point | $(x_1, x_2)$ | $Z$ |
|---|---|---|
| A | (0, 0) | 0 |
| B | (0, 4) | 4 |
| C | (6, 4) | 124 |
| D | (10, 0) | **200** |

- The objective line is very steep and improves in the direction of increasing $x_1$.
- **Optimum:** $x_1^* = 10$, $x_2^* = 0$, $Z^* = 200$ at corner D.

Shadow prices (also called **dual variables**):

- **$u_1 = 20$.** Raising the RHS of Constraint 1 to 11 moves D to D′ = (11, 0), and $Z$ rises by 20.
- **$u_2 = 0$.** Moving the line $x_2 = 4$ does not affect corner D. More of this resource gives no gain, but no loss either.

**Problem 2 (Constraint 2 becomes an equality).** Change Constraint 2 to $x_2 = 4$, so the resource *must* be fully consumed.

- *Feasible region:* the **line segment BC** only, from (0, 4) to (6, 4).
- **Optimum:** corner C, with $x_1^* = 6$, $x_2^* = 4$, $Z^* = 124$.

Shadow prices:

- **$u_1 = 20$.** RHS 11 gives (7, 4) and $Z = 144$, an increase of 20.
- **$u_2 = -19$.** RHS 5 forces $x_2 = 5$, so $x_1 = 5$ and $Z = 20(5) + 5 = 105$. The change is $105 - 124 = -19$. (The ASR says "shadow price is 19", but the value is **−19**.)

**Intuition**

- Think of resource 2 as something "obnoxious" (smelly, chemically reactive) that must be used up.
- Only the low-profit product $x_2$ consumes it.
- More of it forces more $x_2$, which displaces the profitable $x_1$. So profit falls.

**Bottom line (maximisation problems)**

| Constraint type | Sign of shadow price | Reason |
|---|---|---|
| $\le$ | $\ge 0$, never negative | Extra resource can be left unused, so "I will never complain." |
| $\ge$ | can be negative ($\le 0$) | e.g., the Red Brand ratio constraints |
| $=$ | positive or negative (unrestricted) | Extra resource must be consumed, which may force an unprofitable mix |

### 2.9 Student Q&A: juice demand

**Question.** Juice demand is 1,000,000 lb but only 300,000 lb is produced. Should we buy Grade B tomatoes to meet it?

**Answer.**

- Juice demand is **not the bottleneck**. The bottlenecks are the **supply constraints** (A and B) and **paste demand**.
- Relieve the supply bottlenecks first. Only at some later point might juice demand become binding.
- Buying extra Grade B gains 17.3¢/lb **only up to its allowable increase**. Beyond that, another constraint becomes binding and the shadow price changes, so you will not keep gaining 17.3¢ per extra pound.

---

## 3. Exam and Assignment Pointers (from emphasis in class)

No explicit exam statement was made. The following were stressed:

**Interpreting shadow prices**

- Always state the **units**, e.g. \$ per lb.
- Use them as the **maximum price to pay** for extra resource. The Grade A purchase is the example: 80,000 lb at 25.5¢ is less than 27.1¢ and within the allowable increase of 600,000, so buy.
- Use them as the **maximum marketing spend** per unit of extra demand: 4.83¢/lb for paste, so a 5¢ campaign is rejected.
- Check the **allowable increase/decrease** before relying on a shadow price.

**Explaining a shadow price via product-mix substitution**

- Example: +150 lb whole tomatoes and −50 lb juice gives \$27.1 per 100 lb of Grade A.

**Reduced cost**

- It is 0 for basic variables and $\le 0$ for non-basic variables in a max problem.
- It equals how much the objective coefficient must improve before the variable enters. Example: 0.097, so adding 0.098 brings $x_{AP}$ in.

**Sunk costs** must be excluded from the objective.

**Sign rules for shadow prices** (max problem): $\le \Rightarrow \ge 0$; $\ge \Rightarrow \le 0$; $= \Rightarrow$ unrestricted. Be able to show this graphically, as in 2.8.

**Agenda ahead**

1. Next class: formal treatment of shadow-price signs through **duality** (dual variables), plus a deeper look at reduced cost.
2. The following ~2 sessions: **integer programming**.

<!-- nav -->
← [Session 7 (2026-11-11)](DSM-109-7_2026-11-11_Amit-Kumar-Vatsa.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
