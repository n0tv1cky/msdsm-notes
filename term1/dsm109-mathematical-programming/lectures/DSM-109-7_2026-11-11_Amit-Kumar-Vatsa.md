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

# DSM-109 · Session 7 · Red Brand Canners (Part 1): Tomato Quality Blending, Cooper vs. Myers Costing, and Sunk Costs

*Lecture: Amit Kumar Vatsa, 11 Nov 2026. The source is an ASR transcript. I corrected obvious mis-transcriptions ("Jews" → juice, "hold tomatoes" → whole tomatoes, "Koopa" → Cooper, "allegation" → alligation, "sum cost" → sunk cost, "food cost" → fruit cost). Any number I had to infer is marked ⚠️.*

---

## 1. Overview

This session continued the **Red Brand Canners** case. The company has already contracted to buy 3 million lb of tomatoes at 18¢/lb. The tomatoes are split into Grade A (quality rating 9) and Grade B (rating 5). They must be turned into three products, each with a minimum average quality rating:

- canned whole tomatoes,
- tomato juice,
- tomato paste.

The lecture first derived the **minimum blending proportions** of Grade A needed for each product, using both mixtures-and-alligation and a weighted-average inequality. It then compared two managers' costings:

- **Cooper (Exhibit 2):** charges fruit at a flat 18¢/lb.
- **Myers (Exhibit 3):** splits the 18¢ average into a higher Grade A cost and a lower Grade B cost, in proportion to quality rating.

Under Myers' numbers, whole tomatoes appear to lose money. The class discussed why both approaches are flawed. The key insight is that **the tomato purchase is a sunk cost**, so apportioning it across grades or products is meaningless for the decision. This was illustrated with an "expensive expert sitting on the bench" analogy and with the fixed-overhead issue from an earlier case.

The **correct value of Grade A** should come from the **shadow price** of the Grade A supply constraint in an LP (sensitivity analysis). That value then decides whether to buy an extra 80,000 lb of Grade A at 25.5¢/lb. The LP formulation and solution are deferred to the next class.

---

## 2. Topics Covered (in order taught)

### 2.1 Case data used in this session

| Item | Value |
|---|---|
| Total tomatoes contracted | 3,000,000 lb |
| Contract price (average delivered) | 18¢/lb ($0.18/lb), signed in May with growers |
| Grade A : Grade B split | 20 : 80, i.e. 600,000 lb A and 2,400,000 lb B |
| Quality rating, Grade A | 9 |
| Quality rating, Grade B | 5 |
| Minimum average rating, whole tomatoes | 8 |
| Minimum average rating, juice | 6 |
| Minimum average rating, paste | 5 (never binding) |
| Weight per case: whole / juice / paste | 18 lb / 20 lb / 25 lb |
| Extra Grade A on offer | 80,000 lb at 25.5¢/lb |

**Why paste is "not a concern":** paste can be made entirely from Grade B (rating 5 ≥ 5). Even the worst raw material meets its requirement.

### 2.2 Blending requirement: whole tomatoes (rating ≥ 8)

**Method 1: Mixtures and alligation**

- The target rating 8 is 1 away from A's rating 9 and 3 away from B's rating 5.
- The blend must sit closer to A, so the quantities are in inverse ratio to these distances: $A : B = 3 : 1$ at the boundary.
- Because the requirement is "8 or above":
$$\frac{A}{B} \ge \frac{3}{1} \quad\Longleftrightarrow\quad A \ge 75\%, \; B \le 25\% .$$
- (The transcript says "28%"; this is an ASR error for 25%.)

**Method 2: Rigorous weighted average**

- Let $A : B = \lambda : 1$.
- Require the weighted-average rating to be at least 8:
$$\frac{9\lambda + 5(1)}{\lambda + 1} \ge 8 \;\Longrightarrow\; 9\lambda + 5 \ge 8\lambda + 8 \;\Longrightarrow\; \lambda \ge 3 .$$
- Therefore $A : B \ge 3 : 1$, i.e. at least 75% Grade A in whole tomatoes.

### 2.3 Blending requirement: juice (rating ≥ 6)

- Target 6 is 3 away from A (9) and 1 away from B (5).
- So:
$$\frac{A}{B} \ge \frac{1}{3} \quad\Longleftrightarrow\quad A \ge 25\%,\; B \le 75\% .$$
- Weighted-average check:
$$\frac{9\lambda+5}{\lambda+1}\ge 6 \;\Rightarrow\; 3\lambda \ge 1 \;\Rightarrow\; \lambda \ge \tfrac{1}{3}.$$

### 2.4 Cooper's fruit cost (Exhibit 2): quantity only

Fruit cost per case = (lb per case) × \$0.18/lb:

- Whole: $18 \text{ lb/case} \times \$0.18/\text{lb} = \$3.24$/case
- Juice: $20 \times 0.18 = \$3.60$/case
- Paste: $25 \times 0.18 = \$4.50$/case

The pounds cancel, giving dollars per case. Quality plays no role.

### 2.5 Myers' fruit cost (Exhibit 3): quality-weighted

Myers' argument is that Grade A is premium, so it should carry a higher cost. Let $Z$ = cost per lb of Grade A and $Y$ = cost per lb of Grade B. He uses two equations in two unknowns.

1. **The total spend must be recovered:**
$$600{,}000\,Z + 2{,}400{,}000\,Y = 3{,}000{,}000 \times 0.18 = \$540{,}000$$
2. **Cost is proportional to quality rating:**
$$\frac{Z}{9} = \frac{Y}{5}$$

**Solving:**

- Substitute $Z = \tfrac{9}{5}Y$ into the first equation: $1{,}080{,}000\,Y + 2{,}400{,}000\,Y = 540{,}000$.
- This gives $Y \approx \$0.1552$/lb and $Z \approx \$0.2793$/lb.
- The lecturer quoted $Z = \$0.2796$ and $Y = \$0.1554$.
  - ⚠️ My exact solution gives 27.93¢ and 15.52¢. The difference is rounding or ASR.
  - Either pair gives the same case costs below.
- The weighted average still equals 18¢: A is above it, B below it.

**Myers' fruit cost per case**, using the minimum-A blends:

- **Whole** (75% A, 25% B):
$$18\,[\,0.75(0.2796) + 0.25(0.1554)\,] \approx \$4.47/\text{case}$$
  This is up from \$3.24, because whole tomatoes use mostly premium A.
- **Juice** (25% A, 75% B):
$$20\,[\,0.25(0.2793)+0.75(0.1552)\,] \approx \$3.72/\text{case}$$
  This is only slightly up from \$3.60. The 25:75 blend is close to the 20:80 availability ratio.
- **Paste** (100% B):
$$25 \times 0.1552 \approx \$3.88/\text{case}$$
  The lecturer said "≈ 3.9". This is a large drop from \$4.50.

**Myers' conclusion:**

- For whole tomatoes, (selling price − variable cost excluding fruit) ≈ \$4.44. ⚠️ The transcript says "4.4"; I inferred 4.44 from the stated result.
- Subtracting fruit cost gives $4.44 - 4.47 = -\$0.03$/case, a loss of 3 cents per case. (The transcript's "0.3 dollars" should read \$0.03.)
- So Myers says: don't produce whole tomatoes; use Grade A for juice and paste.

### 2.6 Class discussion: who is right?

**Student views:**

- **Nehaal:** Myers is better because he considers quality as well as quantity.
- **A second student:** agreed premium grade should carry more value, but was uncomfortable with the made-up "cost ∝ rating" ratio.
- **Another student:** Cooper ignores that **Grade A is scarce**. Myers ignores that the **18¢/lb is already committed** and so shouldn't drive decisions. Hence **both approaches are incorrect**, not merely "non-optimal."

**Instructor's critique of Myers (the domino effect):**

1. Inflating A's cost makes whole tomatoes look unprofitable, so you drop them.
2. All Grade A then flows into juice, which pushes juice above the 25:75 mix. Juice's fruit cost rises and it may also look unprofitable.
3. If you drop juice too, Grade A has no use. You would "throw it down the drain," even though it was already paid for.
4. The root error is **artificially apportioning a sunk/fixed cost** across raw materials.

**Analogy: the expensive expert on the bench.** (The lecturer referred to his former software company; the employer's name is garbled in the transcript.)

- A VP hires a costly expert to contribute across many products.
- Each product manager refuses to have the expert's hours billed to their product, because it would push their P&L into the red.
- Result: the expert sits idle, but the salary is paid anyway. For the organisation the salary is a **sunk cost**, so the resource should be used.

**Rahul's example:** his previous company allocated "practice area leads" across projects as an overhead charge (e.g. 0.25 of project cost).

**Instructor's response and link to the previous case:**

- This mirrors the **fixed overhead in the earlier ("Modern Truck"?) case**.
- Allocating fixed overhead to a product makes that product look unprofitable.
- Spreading it may be fine for **long-term strategic** pricing, but it is wrong for **short-term tactical or operational** decisions.

### 2.7 The key principle: sunk costs and the value of a resource

- **What is sunk is sunk.** The 3M lb at 18¢ is a contractual, already-incurred cost.
  - Do not decide how to "distribute" it between Grade A and Grade B.
  - If Grade A is in hand, use it where it is most valuable. Its best use is whole tomatoes.
- **Accounting tricks are only possible with fixed costs.**
  - Variable costs are genuinely incremental: each extra unit costs that much more. You cannot reallocate them arbitrarily.
- **The right question:** what is the *value* of Grade A to the business?
  - Answer it with **sensitivity analysis** on an LP containing the supply constraints:
$$\text{Grade A used} \le 600{,}000 \text{ lb}, \qquad \text{Grade B used} \le 2{,}400{,}000 \text{ lb}$$
  - The **shadow price** of the Grade A constraint is the increase in optimal profit per extra lb of Grade A.
- **Decision rule for the 80,000 lb offer at 25.5¢/lb:**
  - Buy if the shadow price exceeds \$0.255/lb (within its allowable increase range).
  - Do not buy if it is lower, e.g. 23¢.
  - The lecturer noted the shadow price "may be similar to Myers' numbers, or may be different. We'll see."

### 2.8 Preview: LP formulation

⚠️ **This model was *not* written in class.** It is the standard formulation implied by the discussion, included so you have the full model. The next class will formulate and solve it.

**Decision variables** (lb of fruit), with $i \in \{A, B\}$ and $j \in \{W, J, P\}$ (whole, juice, paste):

- $x_{ij}$ = pounds of Grade $i$ tomatoes used in product $j$, with $x_{ij} \ge 0$.

**Parameters** (⚠️ not stated in this session apart from case weights and whole-tomato margin):

- $w_W = 18,\ w_J = 20,\ w_P = 25$ lb/case.
- $c_j$ = contribution per case **excluding fruit cost**, in \$/case. Fruit cost is excluded because it is sunk. For whole tomatoes, $c_W \approx 4.44$ ⚠️; others are from the case exhibits.
- $D_j$ = demand forecast for product $j$, in cases, from the case exhibits.

**Model:**

$$
\begin{aligned}
\max \quad & \sum_{j\in\{W,J,P\}} \frac{c_j}{w_j}\,(x_{Aj}+x_{Bj}) && \text{(total contribution, \$)}\\[4pt]
\text{s.t.}\quad & x_{AW}+x_{AJ}+x_{AP} \le 600{,}000 && \text{(Grade A supply, lb)}\\
& x_{BW}+x_{BJ}+x_{BP} \le 2{,}400{,}000 && \text{(Grade B supply, lb)}\\
& 9x_{AW}+5x_{BW} \ge 8\,(x_{AW}+x_{BW}) \;\Leftrightarrow\; x_{AW} - 3x_{BW} \ge 0 && \text{(whole quality} \ge 8)\\
& 9x_{AJ}+5x_{BJ} \ge 6\,(x_{AJ}+x_{BJ}) \;\Leftrightarrow\; 3x_{AJ} - x_{BJ} \ge 0 && \text{(juice quality} \ge 6)\\
& 9x_{AP}+5x_{BP} \ge 5\,(x_{AP}+x_{BP}) && \text{(paste quality} \ge 5\text{, always satisfied)}\\
& \frac{x_{Aj}+x_{Bj}}{w_j} \le D_j \quad \forall j && \text{(demand, cases)}\\
& x_{ij} \ge 0 \quad \forall i,j && \text{(non-negativity)}
\end{aligned}
$$

The **shadow price of the Grade A supply constraint** is what gets compared with \$0.255/lb.

---

## 3. Exam / Assignment Flags

No explicit "this will be on the exam" statement was made. The following were emphasised:

- **Sunk vs. relevant costs.** Know why both Cooper's and Myers' costings are incorrect for decision-making:
  - Cooper ignores the scarcity of Grade A.
  - Myers apportions a sunk cost by an arbitrary rule.
- **Blending constraints.** Be able to derive "≥ 75% A for whole" and "≥ 25% A for juice" using both alligation and the weighted-average inequality, and write them as linear constraints.
- **Shadow prices as the value of a resource.** Use them to evaluate buying extra Grade A at 25.5¢/lb.
- **Fixed-cost allocation.** Allocation is only for long-term strategic purposes, not short-term tactical or operational decisions. This connects to the earlier case's fixed overhead.
- **Next class:** formulate Red Brand Canners as a mathematical program, solve it, and draw the insights. Re-read the case exhibits (selling prices, variable costs, demand forecasts) beforehand.

<!-- nav -->
← [Session 6 (2026-11-09)](DSM-109-6_2026-11-09_Amit-Kumar-Vatsa.md) · [All lectures](./) · [Session 8 (2026-11-13)](DSM-109-8_2026-11-13_Amit-Kumar-Vatsa.md) →
<!-- /nav -->
