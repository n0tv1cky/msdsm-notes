---
course: DSM 109
date: 2026-10-22
start: 7:00pm
session: "1"
faculty: Amit Kumar Vatsa
---

<!-- nav -->
← (first lecture) · [All lectures](./) · [Session 2 (2026-10-23)](DSM-109-2_2026-10-23_Amit-Kumar-Vatsa.md) →
<!-- /nav -->

# DSM-109 Mathematical Programming: Session 1 Study Notes
**Instructor:** Prof. Amit Kumar Vatsa (IIM Indore) · **Session file:** DSM-109-1_2026-10-22

---

## 1. Overview

This first session introduced the course and the field of Operations Research / Management Science (OR/MS). It covered:

- **Logistics:** grading, textbooks, and course scope (LP, LP applications, ILP, MILP).
- **History:** OR began in WWII military operations, through Enigma code-breaking and George Dantzig's simplex method, and then spread to business.
- **Three motivating problems:**
  1. **Airline revenue management.** A single-variable pricing problem solved by calculus, graphing, or search. It led into *convex vs. non-convex* optimisation. It also showed how "out-of-the-box" thinking (price discrimination) beats the mathematical optimum.
  2. **Five-week consulting flight-booking puzzle.** This showed why we need a *guarantee of optimality* rather than trial and error.
  3. **Bulldozer-to-site assignment problem.** This showed that greedy heuristics can be poor and brute force is computationally impossible ($`n!`$ growth). A smarter exact method, to be covered next class, solves very large instances in milliseconds.

---

## 2. Topics Covered (in order taught)

### 2.1 Course logistics

**Instructor background**
- B.Tech, IIT Kharagpur (2005), then Engineers India Ltd (EIL), New Delhi.
- MBA, IIM Lucknow (2010), then industry.
- PhD (2015), then Functional Architect at JDA Software (now Blue Yonder) for about 3 years.
- Now at IIM Indore. Teaches linear/integer programming, convex optimisation, large-scale optimisation and algorithms.

**Format:** 10 sessions of 1 hour each. The class will meet in person during the December campus visit to IIM Indore.

**Evaluation**

| Component | Weight |
|---|---|
| Class participation | 10% |
| Quiz (ASR said "quiz on mercel"; likely a mid-term quiz, so confirm) | 20% |
| Group assignment | 30% |
| End-term examination | 40% |

**Content:** Linear Programming (LP), applications of LP, Integer Linear Programming (ILP), Mixed-Integer Linear Programming (MILP). The course is *applied*: it covers techniques, but the emphasis is on applications, modelling pitfalls, and drawing managerial inferences.

**Textbooks**
- **Main:** Anderson, Sweeney & Williams, *An Introduction to Management Science*.
- **Advanced:** Taha, *Operations Research: An Introduction*.
- **Advanced:** Bazaraa, Jarvis & Sherali, *Linear Programming and Network Flows*. This is the standard text at IITs.

**Cameras:** Students are requested to keep cameras on.

### 2.2 What is OR / Management Science, and why the name?

**Definition:** OR is the discipline that applies advanced analytical methods to help make better decisions.

**Why "operations"?** The word comes from *military operations*, not from "operations management" (a student's guess, which the instructor corrected).

**WWII origins**
- The Allies (e.g., the UK) assembled teams of mathematicians, logicians, statisticians and code-breakers.
- **Enigma example:** Treat the password as 10 letters (simplified for class). The number of possibilities is

```math
26 \times 26 \times \cdots \times 26 = 26^{10} \approx 1.41 \times 10^{14}.
```
- Germans reset the setting every midnight, so exhaustive manual search was futile.
- Turing's team built an early computer. Even that could not brute-force the space.
- Known repeated words in the 6 a.m. weather reports ("weather", "Heil Hitler") drastically cut the search space.
- Recommended film: *The Imitation Game* (Alan Turing).
- OR scientists also accompanied troops at the Normandy landings.

**Post-war**
- **George Dantzig** (US Air Force) invented the **simplex method** for LP.
- The instructor remarked it is "not an efficient method." Context: it has exponential worst-case complexity in theory but is very fast in practice.
- Military problems fit the pattern "minimise/maximise an objective subject to constraints," e.g. minimise travel time, maximise damage, under limited ammunition and manpower.
- **Business adoption:** firms have objectives (maximise profit, minimise cost) and constraints (limited hours, budget, resources).
- **Management Science** is the applied side; **Operations Research** is the more mathematical side. They are essentially the same field.

### 2.3 Problem 1: Airline revenue management (single price)

**Setup:** Demand is linear in price, estimated by regression on historical data:

```math
D(p) = a - b\,p, \qquad a, b > 0 \text{ constants.}
```
Capacity is assumed **not** to be a constraint.

**Model**
- **Decision variable:** $`p`$ = ticket price (₹ per ticket).
- **Objective (₹):** maximise revenue = quantity × price.
- **Constraints:** non-negative price, and price low enough that demand is non-negative.

```math
\begin{aligned}
\max_{p} \quad & R(p) = p\,(a - b\,p) = a\,p - b\,p^2 \\
\text{s.t.} \quad & 0 \le p \le \tfrac{a}{b}
\end{aligned}
```

**Method 1: Calculus (closed-form solution)**
1. First-order condition:

```math
\frac{dR}{dp} = a - 2b\,p = 0 \;\Rightarrow\; p^* = \frac{a}{2b}.
```
The ASR wrote "$`a - 2b`$"; the correct derivative is $`a - 2bp`$.
2. Second-order check:

```math
\frac{d^2R}{dp^2} = -2b < 0 \;\Rightarrow\; \text{maximum}.
```
The ASR said "$`-2`$"; it is $`-2b`$, which is negative since $`b>0`$.
3. Implied values (follow directly; not stated in the lecture):

```math
Q^* = a - b\cdot\frac{a}{2b} = \frac{a}{2}, \qquad R^* = \frac{a^2}{4b}.
```

A **closed-form solution** is a formula: plug in $`a, b`$ and get the answer. Completing the square gives the same result.

**Method 2: Curve plotting**
- $`R(p)`$ is a downward parabola with roots at $`p = 0`$ and $`p = a/b`$.
- It is symmetric, so the peak is at the midpoint $`p^* = a/(2b)`$.

**Method 3: Trial-and-error or gradient-based search**
- Start at any price and step in the improving direction, shrinking the step size. This converges to $`p^*`$ from either side.
- The search may not land *exactly* on $`p^*`$. Since $`p^*`$ is a stationary point, a ±1–2% deviation barely changes revenue, so the answer is robust.

### 2.4 Convex vs. non-convex optimisation

- **Easy case:** the single-peak revenue curve. Search cannot get trapped. This is a **convex optimisation** problem: maximising a concave function.
- **Hard case:** a function $`f(x)`$ with many peaks.
  - Search can get stuck at a wrong **local maximum**.
  - Calculus finds all stationary points, which must then be checked with second derivatives and compared.
  - This is a **non-convex optimisation** problem.
- **Key fact:**
  - In convex optimisation, **every local optimum is a global optimum**.
  - In non-convex optimisation, a local optimum **may not** be global.
- **Course scope:** problems solvable by calculus or closed form are *not* the focus; those belong to ML and numerical optimisation courses. LP problems generally have no closed-form solution, so calculus is not the tool. Convex and non-convex problems will be revisited later.

### 2.5 "Can we beat $`p^*`$?": out-of-the-box thinking

**The limitation:** With a **single price**, nothing beats $`p^*`$. Revenue is the largest rectangle $`p \times Q`$ that fits under the demand line (price on the vertical axis, quantity on the horizontal axis).

**The opportunity**
- The whole area under the demand curve is "money on the table."
- Some customers would pay more than $`p^*`$.
- Charging them a higher price $`p_1`$ captures extra revenue, shown by the additional area.

**How to do it:** Use **customer segmentation / price discrimination**. Sell *different offerings*, so customers have a reason to pay more:
- **Airlines:** priority boarding, snacks, refreshments. These cost little but are valued.
- **FMCG (HUL Surf Excel):** many variants (hand wash, machine wash, top-loader, front-loader). The front-loader variant costs about ₹10–20/kg more for marginal product differences.
- The same logic applies to hotels and many other industries.

**Another example: JIT/Lean vs. EOQ**
- US firms computed the **Economic Order Quantity** (EOQ). This order size balances inventory holding cost against ordering/setup cost.
  - The standard formula, not derived in class, is $`Q^* = \sqrt{2DS/H}`$. Here $`D`$ = demand rate, $`S`$ = setup cost per order, and $`H`$ = holding cost per unit per period.
- Toyota/Japanese firms asked: why can't the order quantity be **one unit**? This led to lean / just-in-time manufacturing, which minimises cash tied up in inventory.

**Takeaway:** Mathematical optimisation and out-of-the-box thinking must balance each other. Don't get so absorbed in the math that you miss the bigger picture.

### 2.6 Problem 2: Five-week consulting flight puzzle

**Data**
- 5-week assignment in Delhi. Each week you fly Indore→Delhi on Monday morning and Delhi→Indore on Wednesday evening.
- That makes 10 flight legs in total:
  - Outbound legs $`O_1,\dots,O_5`$.
  - Return legs $`R_1,\dots,R_5`$.

| Ticket type | Cost |
|---|---|
| One-way | ₹5,000 |
| Round trip within the same week | ₹8,000 |
| Round trip spanning a weekend | ₹6,000 |

Airlines offer the weekend-spanning discount because such travellers look like leisure customers. They want to keep business travellers paying more, which links back to §2.5.

**Solutions discussed**

| Solution | Construction | Cost |
|---|---|---|
| (a) | 5 same-week round trips $`(O_k, R_k)`$ | $`5 \times 8{,}000 = ₹40{,}000`$ |
| (b) | 4 weekend-spanning round trips + 2 leftover one-ways | $`4 \times 6{,}000 + 2 \times 5{,}000 = ₹34{,}000`$ |
| (c) | Same as (b), but the two leftover one-ways are also clubbed into a weekend-spanning round trip | $`5 \times 6{,}000 = ₹30{,}000`$ |

- **Solution (b) details:** the 4 round trips are Delhi→Indore→Delhi, i.e. $`(R_k, O_{k+1})`$ for $`k=1..4`$. The leftover one-ways are $`O_1`$ and $`R_5`$.
- **Solution (c) details:** $`O_1`$ and $`R_5`$ become an Indore→Delhi→Indore round trip spanning weekends.

**Why ₹30,000 is optimal (lower-bound argument)**
- Every leg must be covered. Covering 2 legs costs at least ₹6,000 (one weekend round trip), versus ₹8,000 or $`2 \times 5{,}000`$ otherwise.
- There are 10 legs, so

```math
\text{Cost} \ge 5 \times 6{,}000 = ₹30{,}000.
```
- Solution (c) attains this bound, so it is **optimal**.

**Alternative optima exist.** For example:
- Pair $`(O_k, R_{k+1})`$ for $`k = 1..4`$, giving Indore-origin weekend round trips.
- Club the leftover $`R_1`$ and $`O_5`$ into a Delhi→Indore→Delhi round trip.
- This also costs ₹30,000.

**Lesson**
- Trial and error can get stuck at ₹34,000 with no way to know a better answer exists. That is embarrassing if a boss or client finds one in 2 minutes.
- A **guarantee of optimality is priceless**. You need a *systematic* method.

**Optional formal model** (my addition; not written in class): a set-partitioning integer program.
- **Legs:** $`L = \{O_1..O_5, R_1..R_5\}`$.
- **Ticket options $`T`$:** each one-way leg (₹5,000); each same-week pair $`(O_k,R_k)`$ (₹8,000); each weekend-spanning pair $`(O_k,R_m)`$ or $`(R_k,O_m)`$ with $`m>k`$ (₹6,000).
- **Decision variables:** $`y_t \in \{0,1\}`$, equal to 1 if ticket option $`t`$ is purchased.
- **Parameters:** $`c_t`$ = cost (₹) of option $`t`$; $`a_{\ell t}=1`$ if option $`t`$ covers leg $`\ell`$.

```math
\begin{aligned}
\min \quad & \sum_{t \in T} c_t\, y_t && \text{(total ticket cost, ₹)}\\
\text{s.t.} \quad & \sum_{t \in T} a_{\ell t}\, y_t = 1 && \forall \ell \in L \quad \text{(each leg flown exactly once)}\\
& y_t \in \{0,1\} && \forall t \in T
\end{aligned}
```

**Optimal value:** ₹30,000.

### 2.7 Problem 3: Bulldozer assignment

**Business problem**
- A construction company has 4 dozers parked at different locations and 4 sites (A, B, C, D).
- Each site needs exactly one dozer for the whole day: a one-to-one matching.
- Goal: minimise total distance travelled, since distance drives fuel cost.

**Distance data (km)**
- **Stated in the lecture:** $`d_{1A}=60`$, $`d_{1B}=45`$, $`d_{2A}=5`$, $`d_{2C}=25`$.
- **Inferred from the arithmetic** (⚠ verify against the slide): $`d_{2D}=35`$, $`d_{3C}=55`$, $`d_{4D}=85`$, $`d_{4A}=15`$.

**Greedy, site-by-site heuristic** (pick the closest available dozer for each site)

| Site | Dozer chosen | Distance (km) |
|---|---|---|
| A | Dozer 2 (closest) | 5 |
| B | Dozer 1 | 45 |
| C | Dozer 3 (dozer 2's 25 already taken) | 55 |
| D | Dozer 4 | 85 |

Total: $`5 + 45 + 55 + 85 = 190`$ km.

**Student's (Aditya's) improved solution**

| Dozer | Site | Distance (km) |
|---|---|---|
| 1 | B | 45 |
| 2 | D | 35 |
| 3 | C | 55 |
| 4 | A | 15 |

Total: $`45 + 35 + 55 + 15 = 150`$ km.

- **Improvement:** $`(190-150)/190 \approx 21\%`$, which the instructor called "about 20%, a huge number."
- **Instructor's confirmation:** 150 km is optimal, and he believes it is the unique optimum.

**Assignment model** (the class referred to its structure; the solution method comes next class)
- **Decision variables:** $`x_{ij} = 1`$ if dozer $`i`$ is sent to site $`j`$, else 0.
- **Parameters:** $`d_{ij}`$ = distance (km) from dozer $`i`$'s location to site $`j`$.

```math
\begin{aligned}
\min \quad & \sum_{i=1}^{4}\sum_{j \in \{A,B,C,D\}} d_{ij}\, x_{ij} && \text{(total km travelled)}\\
\text{s.t.} \quad & \sum_{j} x_{ij} = 1 && \forall i \quad \text{(each dozer goes to exactly one site)}\\
& \sum_{i} x_{ij} = 1 && \forall j \quad \text{(each site gets exactly one dozer)}\\
& x_{ij} \in \{0,1\} && \forall i,j
\end{aligned}
```

### 2.8 Why brute force fails: combinatorial explosion

**Brute force** means evaluating every alternative and picking the best. With $`n`$ dozers and $`n`$ sites:

```math
\#\text{alternatives} = n \times (n-1) \times \cdots \times 1 = n!
```

**Excel demo**

| $`n`$ | $`n!`$ | Feasibility |
|---|---|---|
| 4 | 24 | about 5 minutes by hand |
| 5 | 120 | 1–2 hours by hand |
| 10 | 3,628,800 | needs a computer |
| 50 | $`\approx 3.04 \times 10^{64}`$ | see calculation below |
| 200 | Excel cannot display it | — |

**Calculation for $`n = 50`$**
1. Assume the fastest supercomputer is about 1 exaflop ($`10^{18}`$ operations per second). Generously, assume it evaluates $`10^{18}`$ alternatives per second.
2. Seconds needed:

```math
\frac{3.04\times10^{64}}{10^{18}} \approx 3.04\times 10^{46}\ \text{s}.
```
3. Years needed:

```math
\frac{3.04\times10^{46}}{365 \times 24 \times 3600} = \frac{3.04\times10^{46}}{3.15\times10^{7}} \approx 9.6 \times 10^{38}\ \text{years}.
```
4. Comparison: the universe is about $`1.4 \times 10^{10}`$ years old. A computer running since the Big Bang would have checked only a vanishingly small fraction (about $`10^{-29}`$) of the alternatives.
5. To finish in 1 year, you would need about $`9.6\times10^{38}`$ computers running in parallel. This is absurd.
   - The instructor said "$`10^{38}`$ particles don't exist in the universe." The observable universe actually has about $`10^{80}`$ particles, but the point stands: this is physically infeasible.

**Punchline**
- Smart methods solve assignment problems of size $`1{,}000 \times 1{,}000`$, or even $`10{,}000 \times 10{,}000`$, in milliseconds, *with* a guarantee of optimality.
- The method will be shown **next class**. Likely candidates are LP/simplex or the Hungarian method.

---

## 3. Points Flagged as Important

**Grading:** 10% participation, 20% quiz, 30% group assignment, 40% end-term.

**Recurring themes the instructor stressed**
1. **Convex vs. non-convex:** in convex problems a local optimum is the global optimum; in non-convex problems you can get trapped at a wrong local optimum.
2. **Guarantee of optimality matters.** Trial and error or greedy methods can leave you at a sub-optimal answer (₹34,000 vs ₹30,000; 190 km vs 150 km) without your knowing it.
3. **Brute force is infeasible.** $`n!`$ explodes. Systematic algorithms give optimality without enumeration.
4. **Balance math with business judgment.** Segmentation and price discrimination beat a single optimal price. JIT challenged EOQ assumptions.

**Next session:** tomorrow. It will cover the systematic method for solving the assignment problem.

---

## 4. Formula Sheet

**Linear demand and revenue**

```math
D(p) = a - bp, \qquad R(p) = ap - bp^2
```

**Optimal single price**

```math
\frac{dR}{dp} = a - 2bp = 0 \;\Rightarrow\; p^* = \frac{a}{2b}
```

```math
\frac{d^2R}{dp^2} = -2b < 0 \;\Rightarrow\; \text{maximum}
```

```math
Q^* = \frac{a}{2}, \qquad R^* = \frac{a^2}{4b}
```

**Enigma toy search space**

```math
26^{10}
```

**Number of possible assignments**

```math
n!
```

**EOQ** (mentioned conceptually only)

```math
Q^* = \sqrt{2DS/H}
```

**Flight lower bound**

```math
\text{Cost} \ge \frac{10 \text{ legs}}{2 \text{ legs per ticket}} \times ₹6{,}000 = ₹30{,}000
```

<!-- nav -->
← (first lecture) · [All lectures](./) · [Session 2 (2026-10-23)](DSM-109-2_2026-10-23_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
