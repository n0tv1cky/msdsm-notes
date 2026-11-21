---
course: DSM 109
date: 2026-11-06
start: 7:00pm
session: "5"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← [Session 4 (2026-10-30)](DSM-109-4_2026-10-30_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 · Session 5: Convex vs. Non-Convex Optimisation, and Shadow Prices in the Merton Truck LP

*Lecture: DSM-109-5, 2026-11-06, Amit Kumar Vatsa. These notes are rebuilt from an ASR transcript. Where a number or term was garbled or had to be inferred, it is flagged ⚠️.*

---

## 1. Overview

The session opened with a recap. In the previous class an LP was solved graphically, and it was established that if an optimal solution exists (the problem is not infeasible or unbounded), it occurs at a corner point.

The first half explained why some optimisation problems are easy and others hard. In a **convex optimisation problem**, every local optimum is also a global optimum. Any improving search therefore cannot get stuck at a wrong solution. The instructor showed this with pictures: 1-D functions, LP versus non-convex polygonal regions, and convex versus non-convex nonlinear programs.

The second half returned to the **Merton Truck** case (ASR: "modern truck"). It covered:

- binding versus non-binding constraints;
- the formal meaning of a **shadow price**;
- an algebraic "delta method" that derives the shadow prices (USD 2,000/hr for engine assembly, USD 500/hr for metal stamping) from the binding constraints;
- the additivity of shadow-price effects;
- a managerial question about how much overtime premium to pay workers;
- a graphical explanation of why shadow prices hold only within the **allowable increase/decrease** range of the sensitivity report.

The exact calculation of those ranges is deferred to the next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: Corner-point property of LPs
- An LP may be **infeasible** (no feasible point) or **unbounded** (no finite optimum).
- Otherwise, if an optimal solution exists, **at least one corner point is optimal**.

### 2.2 Why convex optimisation problems are "easy"
- **Key fact:** in a convex optimisation problem, **local optimum ⟹ global optimum**.
- **Local optimum:** a feasible point that is at least as good as every feasible point in a small neighbourhood (a "small ball") around it.
- **Global optimum:** a point at least as good as every feasible point.
- **Consequence:** any method that keeps moving in an improving direction and stops when no neighbour is better has found the true optimum. You never need to check other candidate regions.

### 2.3 Three related but distinct definitions

**(a) Convex function.** For any two points $x_a, x_b$ and any $\lambda \in [0,1]$:

```math
f\big(\lambda x_a + (1-\lambda)x_b\big) \;\le\; \lambda f(x_a) + (1-\lambda) f(x_b)
```
- The value at any in-between point $x_0 = \lambda x_a + (1-\lambda)x_b$ is no higher than the weighted average of the endpoint values.
- Geometrically, every **secant (chord) lies on or above the curve**. Picture a "bowl" shape.
- A function is **concave** if the inequality is reversed, i.e. $-f$ is convex.
- **Linear functions are both convex and concave.**

**(b) Convex set / convex feasible region.** A region is convex if, for any two points in it, the **entire line segment joining them lies inside the region**.
- Counter-example (drawn in class): a region with a "dent". You can pick two points whose connecting segment partly leaves the region, so it is **not** convex.

**(c) Convex optimisation problem.** The standard form is

```math
\begin{aligned}
\min_{x}\quad & f(x)\\
\text{s.t.}\quad & g_i(x) \le 0, \qquad i = 1, 2, \dots, m
\end{aligned}
```
where $f$ and all $g_i$ are **convex functions**.
- Why this works: a constraint of the form "convex function $\le$ constant" always produces a convex feasible region.
- Example: $x^2 + y^2 \le 5$ gives a filled disc, which is convex. ⚠️ The right-hand side was garbled in the audio ("phi"); "5" is a guess, and any positive constant gives a disc.
- **Maximising a concave function** can be rewritten in this form, so it is also convex optimisation. Example:

```math
\max\; -x^2 - y^2 \;\;\Longleftrightarrow\;\; \min\; x^2 + y^2
```
- **Every LP is a convex optimisation problem.** Linear objective and constraints are convex (and concave), whether you minimise or maximise.
- Standard textbook extension, not stated in the lecture: equality constraints are allowed if they are affine (linear).

### 2.4 Student question: a "calculus" definition?
- **Student's proposal:** if $f(a) \le f(a^-)$ and $f(a) \le f(a^+)$, that defines a minimum. If $f(a) \ge f(a^-)$ and $f(a) \ge f(a^+)$, that defines a maximum.
- **Instructor's answer:** that condition defines a **local minimum/maximum at a point**. It is not the definition of convexity.
- A convex function need not have a finite minimiser. Example: $f(x) = e^{-x}$ is convex and keeps decreasing, so its "minimum" is only approached as $x \to \infty$.

### 2.5 Pictorial examples: easy (convex) vs. hard (non-convex)

| # | Problem | Picture | Easy/Hard | Why |
|---|---|---|---|---|
| 1 | $\min f(x)$, $x_{L} \le x \le x_{U}$, $f$ bowl-shaped (convex) | U-shaped curve on an interval | **Easy** | From any start, moving downhill reaches the bottom. That point is both local and global minimum. |
| 2 | $\max f(x)$, same bowl, same interval | Same U-shape | **Hard** | Starting left of the bottom you climb to the left endpoint; starting right you climb to the right endpoint. Both are local maxima, and you must compare all such extreme candidates. In large problems there can be very many. |
| 3 | $\max f(x)$, $f$ concave (∩-shaped) | Hill | **Easy** | Convex optimisation in disguise. The local maximum is the global maximum. |
| 4 | $\max f(x)$, $f$ wavy with several peaks | Multi-hump curve | **Hard** | Every peak is a local maximum, and only one is global. When you reach a peak that beats all its neighbours, you cannot know whether to stop. |

- **One remedy for example 4:** split the domain into "boxes", each of which makes a convex sub-problem. Solve each box, then compare the results.
- This is far more work, because you must handle every subset/box in which the problem becomes convex.

### 2.6 LP (convex) vs. non-convex polygonal region

**LP with a convex polygon.**
- The objective improves in a fixed direction (iso-profit lines move outward).
- Moving corner to corner, e.g. $A \to B \to C \to \dots$, each step strictly improves the objective until no improving direction remains.
- The final corner is both local and global optimum.
- You can never get stuck, because there is always an improving direction until the true optimum is reached. This is the intuition behind the simplex method.

**Non-convex region with corners $A, B, C, D, E$.**
- The objective improves in the direction drawn.
- **Corner $C$** beats $D$ and every feasible point in a small ball around it, so $C$ is a **local optimum**.
- **Corner $E$** has a strictly better objective. $E$ is the **global optimum**.
- A local search stopping at $C$ would wrongly conclude it is optimal. This cannot happen in a convex problem.

### 2.7 Convex NLP vs. non-convex NLP
- **Convex NLP:** a curved but convex feasible region with a linear objective. The tangency point is local and global optimum.
  - Remark: solving convex nonlinear programs is **today about as easy as solving LPs**.
- **Non-convex NLP:** a similar region with a non-convex dent. One tangency point is only a local optimum, and the global optimum lies elsewhere.
- Takeaway: **non-convexity, not non-linearity, is what makes a problem hard.**

---

### 2.8 Merton Truck case: model (from previous class)

**Business problem.** Merton Truck makes two truck models, Model 101 and Model 102. It must decide the production mix that maximises total contribution. Production is limited by four departments: engine assembly, metal stamping, the Model 101 assembly line and the Model 102 assembly line.

**Decision variables.**
- $x_1$ = number of Model 101 trucks produced per period (trucks).
- $x_2$ = number of Model 102 trucks produced per period (trucks).
- ⚠️ The period (per month) comes from the standard case, not the transcript.

**Model.**

```math
\begin{aligned}
\max\quad & Z = 3000\,x_1 + 5000\,x_2 && \text{(total contribution, USD)}\\[4pt]
\text{s.t.}\quad & 1\,x_1 + 2\,x_2 \le 4000 && \text{(engine assembly hours)}\\
& 2\,x_1 + 2\,x_2 \le 6000 && \text{(metal stamping hours)}\\
& 2\,x_1 \le 5000 && \text{(Model 101 assembly-line hours)}\\
& 3\,x_2 \le 4500 && \text{(Model 102 assembly-line hours)}\\
& x_1,\, x_2 \ge 0
\end{aligned}
```

Notes on the data:
- ⚠️ The ASR once read the objective as "$3000x_1 + 4000x_2$". The instructor's later arithmetic ($3000 \cdot 2000 + 5000 \cdot 1000 = 11$ million) confirms the coefficient of $x_2$ is **5000**.
- ⚠️ The coefficients for the two assembly lines ($2x_1 \le 5000$ and $3x_2 \le 4500$) are inferred from the standard Merton Truck case. They are consistent with everything said in class: the RHS 5000 is mentioned, and the allowable decreases of 1000 and 1500 match these slacks exactly.
- Integrality is ignored, i.e. the LP relaxation is used, as is standard for this case.

**Equality (standard) form with slacks.**

```math
\begin{aligned}
x_1 + 2x_2 + s_1 &= 4000\\
2x_1 + 2x_2 + s_2 &= 6000\\
2x_1 + s_3 &= 5000\\
3x_2 + s_4 &= 4500\\
x_1, x_2, s_1, s_2, s_3, s_4 &\ge 0
\end{aligned}
```
Each $s_i$ is the number of unused hours in department $i$.

**Optimal solution.** $x_1 = 2000$, $x_2 = 1000$, $Z^\ast  = \text{USD } 11{,}000{,}000$.
- Slacks at the optimum: $s_1 = 0$, $s_2 = 0$, $s_3 = 5000 - 4000 = 1000$, $s_4 = 4500 - 3000 = 1500$.

**Graphical solution.** The feasible region is a convex polygon. ⚠️ The corner labels and the other corners' values below were reconstructed by me. The lecture only states that **corner D = (2000, 1000)** is optimal, at the intersection of engine assembly and metal stamping.

| Corner | Defining constraints | $(x_1, x_2)$ | $Z$ (USD) |
|---|---|---|---|
| A | axes | $(0, 0)$ | $0$ |
| B | $x_2 = 0$, 101-assembly | $(2500, 0)$ | $7{,}500{,}000$ |
| C | 101-assembly, metal stamping | $(2500, 500)$ | $10{,}000{,}000$ |
| **D** | **engine assembly, metal stamping** | **$(2000, 1000)$** | **$11{,}000{,}000$** ✔ |
| E | engine assembly, 102-assembly | $(1000, 1500)$ | $10{,}500{,}000$ |
| F | $x_1 = 0$, 102-assembly | $(0, 1500)$ | $7{,}500{,}000$ |

### 2.9 Binding vs. non-binding constraints
- **Binding (bottleneck) constraints** are used 100% at the optimum (slack = 0). Here these are **engine assembly** and **metal stamping**.
  - The optimal corner D is exactly their intersection.
  - Moving either line moves the optimal point.
- **Non-binding constraints** have positive slack: the Model 101 and Model 102 assembly lines.
  - Adding an hour to them changes nothing, because hours are already left unused.
  - Their shadow price is **0**.

### 2.10 Shadow price: definition
**Shadow price** of a constraint = the change (increase) in the optimal objective value per unit (marginal, small $\delta$) increase in that constraint's right-hand side.
- Every constraint has a shadow price. It may be **positive, zero, or negative**.
- **Excel check shown in class:** raising engine-assembly hours from 4000 to 4001 and re-optimising increased the objective by USD 2,000.
  - ⚠️ ASR said "11 million 200". The correct value is USD 11,002,000.

**Shadow prices from the Excel sensitivity report.**

| Constraint | Shadow price (USD/hr) | Status |
|---|---|---|
| Engine assembly | 2000 | binding |
| Metal stamping | 500 | binding |
| Model 101 assembly | 0 | non-binding |
| Model 102 assembly | 0 | non-binding |

### 2.11 Deriving shadow prices by the "delta method" (worked example)

**Idea.** Since corner D is optimal and is defined by the two binding constraints, keep only those two as equalities. Then perturb their RHS by $\delta_1$ (engine assembly) and $\delta_2$ (metal stamping):

```math
\begin{aligned}
x_1 + 2x_2 &= 4000 + \delta_1 && (1)\\
2x_1 + 2x_2 &= 6000 + \delta_2 && (2)
\end{aligned}
```

**Step 1. Eliminate $x_2$.** Compute (2) − (1):

```math
x_1 = 2000 - \delta_1 + \delta_2
```

**Step 2. Substitute into (1).**

```math
2x_2 = 4000 + \delta_1 - (2000 - \delta_1 + \delta_2) = 2000 + 2\delta_1 - \delta_2
```

```math
\Rightarrow\quad x_2 = 1000 + \delta_1 - \tfrac{1}{2}\delta_2
```
Check: with $\delta_1 = \delta_2 = 0$ we recover D $= (2000, 1000)$.

**Step 3. Substitute into the objective.**

```math
\begin{aligned}
Z &= 3000(2000 - \delta_1 + \delta_2) + 5000\left(1000 + \delta_1 - \tfrac{1}{2}\delta_2\right)\\
&= \underbrace{6{,}000{,}000 + 5{,}000{,}000}_{11{,}000{,}000} + (-3000 + 5000)\,\delta_1 + (3000 - 2500)\,\delta_2
\end{aligned}
```

```math
\boxed{Z = 11{,}000{,}000 + 2000\,\delta_1 + 500\,\delta_2}
```

The coefficient of $\delta_1$ is the **shadow price of engine assembly (2000)**. The coefficient of $\delta_2$ is the **shadow price of metal stamping (500)**.

**Interpretation.** One extra engine-assembly hour moves the optimum from D to a new corner D′:
- $x_1$ falls by 1 and $x_2$ rises by 1;
- net gain $= -3000 + 5000 = \text{USD } 2000$.

**Additivity, demonstrated in Excel.** Take $\delta_1 = 1$ and $\delta_2 = 2$:

```math
\Delta Z = 2000(1) + 500(2) = 3000
```
Re-optimising in Excel confirmed the objective rose by USD 3,000.

**Important prerequisite:** the method needs the optimal corner, and hence the set of binding constraints, to be known first.

### 2.12 Managerial use: overtime negotiation
- **Scenario:** workers offer overtime in engine assembly. Their regular wage is already included in the contribution figures (direct labour cost).
- Each extra hour therefore adds USD 2,000 **after** paying the regular wage.
- The firm should be willing to pay a **premium of up to USD 2,000 per extra hour**, over and above the regular wage.
  - Paying more than USD 2,000 makes overtime unprofitable.
  - Paying exactly USD 2,000 leaves the firm indifferent (a point a student raised).
  - In practice, negotiate to share less than that.
- This holds only within the allowable increase (see 2.13).

### 2.13 Validity range: allowable increase/decrease

**Why shadow prices have a range.** A shadow price holds only while the **same set of constraints stays binding**, i.e. the optimal corner is still the intersection of engine assembly and metal stamping.

**Graphical explanation.**
- **Increasing engine-assembly hours:** the line shifts outward and D moves to D′ with higher $Z$.
  - If it shifts too far, the optimal corner becomes the intersection of **Model 102 assembly** and metal stamping.
  - The binding set changes, so the shadow price changes.
  - Beyond that point extra hours do not reduce profit. They just go unused, and the gain stops accruing at USD 2,000/hr.
- **Decreasing engine-assembly hours:** D′ moves the other way and profit falls by USD 2,000 per hour lost.
  - If it falls too far, the optimal corner becomes the intersection of **Model 101 assembly** and engine assembly.
  - Again the binding set, and therefore the shadow price, changes.

**Sensitivity-report values quoted in class.**

| Constraint | RHS | Shadow price | Allowable increase | Allowable decrease | Valid RHS range |
|---|---|---|---|---|---|
| Engine assembly | 4000 | 2000 | 500 | 500 | 3500 – 4500 |
| Metal stamping | 6000 | 500 | 500 | 1000 | 5000 – 6500 |
| Model 101 assembly | 5000 | 0 | $\infty$ | 1000 | $\ge 4000$ |
| Model 102 assembly | 4500 | 0 | $\infty$ | 1500 | $\ge 3000$ |

**Quick check using the delta-method formulas** (the instructor will formalise this next class). The binding pair defines the optimum only while the other two constraints stay satisfied:

- **Engine assembly** ($\delta_2 = 0$):
  - The 102 line requires $x_2 = 1000 + \delta_1 \le 1500$, so $\delta_1 \le 500$.
  - The 101 line requires $x_1 = 2000 - \delta_1 \le 2500$, so $\delta_1 \ge -500$.
- **Metal stamping** ($\delta_1 = 0$):
  - The 101 line requires $x_1 = 2000 + \delta_2 \le 2500$, so $\delta_2 \le 500$.
  - The 102 line requires $x_2 = 1000 - \tfrac{1}{2}\delta_2 \le 1500$, so $\delta_2 \ge -1000$.
- **Non-binding constraints:**
  - The allowable increase is $\infty$, because extra capacity is never used.
  - The allowable decrease equals the slack (1000 and 1500). Cutting more than that makes the constraint binding.

---

## 3. Exam / Assignment Pointers

- **Merton Truck case questions** at the back of the case: go through all of them. They will be discussed in class, and the overtime/shadow-price question is typical.
- **Be able to:**
  - define a convex function, a convex set and a convex optimisation problem;
  - explain why local optimum implies global optimum makes convex problems easy, with examples of how non-convex problems trap local search;
  - identify binding vs. non-binding constraints and explain why non-binding ones have zero shadow price;
  - **derive shadow prices with the delta method**, as in 2.11;
  - interpret shadow prices managerially (maximum premium to pay for an extra resource unit) and state that they are valid only within the allowable increase/decrease range.
- **Next class (Monday, after Diwali):**
  - deriving allowable increase/decrease algebraically and graphically;
  - allowable ranges for **objective-function coefficients** (reduced costs / optimality ranges).

<!-- nav -->
← [Session 4 (2026-10-30)](DSM-109-4_2026-10-30_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
