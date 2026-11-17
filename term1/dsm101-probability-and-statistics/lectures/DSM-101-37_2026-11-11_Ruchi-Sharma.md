---
course: DSM 101
date: 2026-11-11
start: 7:00pm
session: "37"
faculty: Ruchi Sharma
---

<!-- nav -->
← [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# Study Notes: DSM-101, Session 37 (2026-11-11, Ruchi Sharma)

> **Note on content:** The course is listed as *Probability & Statistics*, but this session's content is **Linear Programming (LP) sensitivity analysis and LP case studies**, which is operations research. No probability or statistics topics appear in the transcript, such as CLT, Bayes' theorem, or Gaussian, Poisson or Binomial distributions. Nothing on those has been added. Possible reasons: the session file is mislabeled, or the course includes an optimization module. Check against your syllabus.
>
> The transcript starts mid-sentence and ends mid-discussion. Items marked *(ASR-corrected)* were reconstructed from garbled speech.

---

## 1. Overview

The session finishes the **Merton Truck** case by explaining the **allowable increase and decrease of objective-function coefficients**. This is the range over which one profit coefficient can change, with everything else fixed, while the current optimal corner point stays optimal. The instructor first showed this numerically in Excel Solver. He then explained it graphically: the slope of the objective line must stay between the slopes of the binding constraints. He then derived it algebraically using coefficient ratios.

Next, the session recapped **reduced cost**, including where the term comes from in George Dantzig's **diet problem**, and **shadow price**. The second half introduced the **Red Brand Canners** case, a tomato-products product-mix and resource-allocation problem. That part covered the raw material data (grades A and B, quality ratings, quantities, cost), the demand forecasts, and Cooper's contribution-margin calculation (Exhibit 2). The session ended as the class began working out how much grade A and grade B tomato each product requires.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap of the previous class (Merton Truck)

- **Already covered:** shadow price and reduced cost.
- **Not yet covered:** allowable increase and decrease in objective-function coefficients. This is today's first topic.

**Setup as used in class:**
- Decision variables:
  - $x_1$ = units of Model 101
  - $x_2$ = units of Model 102
- Objective-function coefficients (profit per unit): $c_1 = 3000$, $c_2 = 5000$.
- Objective:
$$\max\; Z = 3000\,x_1 + 5000\,x_2$$
- Optimal solution: $(x_1, x_2) = (2000, 1000)$. This is corner point $D$.
  - *(ASR-corrected:* the transcript says "1000 comma 32,000 comma 1000"; the intended value is $(2000, 1000)$.)
- The two **binding constraints**, with coefficient ratios as stated in class:
  - **Engine assembly:** coefficients in ratio $1:2$, i.e. $x_1 + 2x_2 \le 4000$.
  - **Metal stamping:** coefficients in ratio $2:2$, i.e. $2x_1 + 2x_2 \le 6000$.
  - The right-hand sides are from the standard Merton Truck case. They are consistent with $D = (2000, 1000)$, because $2000 + 2(1000) = 4000$ and $2(2000) + 2(1000) = 6000$.

### 2.2 Reduced cost recap (from the Excel output)

- $x_1$ and $x_2$ are both positive in the optimal solution, so **both have reduced cost $= 0$**.
- **Model 103 has reduced cost $= -350$.**
  - Forcing production of one unit of Model 103 lowers the objective by \$350.
  - In other words, Model 103 is loss-making at the margin.
- Adding a constraint such as $x_1 \ge 1$ would be **redundant**, because $x_1$ is already positive. This is why its reduced cost is $0$.

### 2.3 Allowable increase/decrease: numerical demonstration (Excel Solver)

**Excel output for $c_1$:** allowable increase $= 2000$.

| Value of $c_1$ | Optimal solution | Comment |
|---|---|---|
| $3000$ | $(2000, 1000)$, point $D$ | Original problem |
| $4999$ | $(2000, 1000)$, point $D$ | Still optimal. *(ASR: "4 trip a line" = 4999)* |
| $5001$ | $(2500, 500)$, point $E$ | $D$ is no longer optimal. *(ASR: "5000 1" = 5001)* |

**Definition:** The **allowable increase/decrease** of an objective-function coefficient is how much that coefficient can change, **one at a time** with all other data fixed, while the **current corner point remains optimal**.

### 2.4 Graphical interpretation

- The current optimum is corner point $D$. Its neighbouring corner points are $C$ and $E$.
- **Making $c_1$ larger** (e.g. 4500) makes product 1 more profitable, so the objective line becomes **steeper**.
  - $D$ stays optimal for a while. The current solution is somewhat robust.
  - When the objective line becomes **parallel to segment $DE$**, both $D$ and $E$ are optimal. Segment $DE$ lies on the metal stamping constraint.
  - Any steeper line makes $E = (2500, 500)$ the only optimum. This matches the Excel result at $c_1 = 5001$.
- **Making the objective line flatter:**
  - When it becomes **parallel to segment $CD$**, both $C$ and $D$ are optimal. Segment $CD$ lies on the engine assembly constraint.
  - Any flatter line makes $C$ the optimum.

> **Key rule:** For corner point $D$ to stay optimal, **the slope of the objective-function line must lie between the slopes of the binding constraints** (here, engine assembly and metal stamping).

### 2.5 Algebraic method: ratio of coefficients

Instead of comparing slopes, compare **coefficient ratios** ($x_1$-coefficient divided by $x_2$-coefficient):

- Objective: $\dfrac{3000}{5000}$
- Engine assembly: $\dfrac{1}{2}$
- Metal stamping: $\dfrac{2}{2}$

**Condition for $D$ to remain optimal:**
$$\frac{1}{2} \;\le\; \frac{c_1}{c_2} \;\le\; \frac{2}{2}$$

**(a) Range for the coefficient of $x_1$.** Replace $3000$ by $k$ and keep $c_2 = 5000$:
$$\frac{1}{2} \le \frac{k}{5000} \le 1$$
Multiplying through by $5000$:
$$2500 \le k \le 5000$$

- Allowable increase $= 5000 - 3000 = 2000$. This matches Excel: 4999 is fine, 5001 is not.
- Allowable decrease $= 3000 - 2500 = 500$.

**(b) Range for the coefficient of $x_2$.** Replace $5000$ by $k'$ and keep $c_1 = 3000$:
$$\frac{1}{2} \le \frac{3000}{k'} \le \frac{2}{2}$$
Taking reciprocals reverses the inequalities:
$$\frac{2}{1} \ge \frac{k'}{3000} \ge 1$$
Multiplying by $3000$:
$$6000 \ge k' \ge 3000$$

- Allowable increase $= 6000 - 5000 = 1000$.
- Allowable decrease $= 5000 - 3000 = 2000$. The instructor's check: "$5000 - 2000 = 3000$".

### 2.6 Merton Truck: summary of insights

- The optimal solution is **not the only useful output**. Sensitivity analysis also gives:
  - **Shadow prices.** These show the value of relaxing or adding capacity to a constraint. They are useful when negotiating with workers or other parties who control constraints.
  - **Reduced costs.** These show which alternative products are loss-making and by how much.
  - **Allowable ranges.** These show how robust the current plan is to changes in profit coefficients.

### 2.7 Origin of the term "reduced cost": Dantzig's diet problem

- **George Dantzig** worked for the Pentagon (US Air Force). One of the early LP problems he solved was the **diet problem**: how to feed soldiers.
- **Decision variables:** number of servings of each food item (eggs, milk, maize, etc.).
- **Constraints:** nutritional requirements, each with a minimum and/or maximum. Examples are calories, minerals, protein and vitamins.
- **Objective:** minimize the total cost of the diet per person.
- **Example:** suppose the optimal diet contains **zero servings of milk**.
  - The reason is that milk is not a cheap enough source of the nutrients it provides.
  - Some combination of other foods supplies those nutrients at lower cost.
- **Reduced cost** = how much the cost per serving of milk must **reduce** for milk to enter the optimal diet. This is where the name comes from.

**General meaning of reduced cost:**
1. How much the optimal objective changes if a variable currently at zero is **forced to take one unit**.
2. Equivalently, how much a non-participating variable's objective coefficient must change before it enters the optimal solution.

### 2.8 Shadow price (recap)

- **Shadow price** = the worth of one more unit of a resource.
- Formally, it is the change in the optimal objective value per marginal unit increase in a constraint's right-hand side.

### 2.9 New case: Red Brand Canners (RBC)

**Context:**
- The company must choose a **product mix and resource allocation**.
- The case contains **disagreements among executives** about the right plan.
- Only the **tomato products** are relevant. Peach halves, peach nectar and cooking apples in the exhibits are ignored.

**Products:**
1. Whole tomatoes
2. Tomato juice
3. Tomato paste

**Raw material data:**
- Total crop purchased: $3{,}000{,}000$ lb.
- Purchase price: $\$0.18$ per lb (18 cents per pound).
  - A student first said $\$1.65$ per case; this was corrected to $\$0.18$/lb.
- Total raw material cost implied: $3{,}000{,}000 \times 0.18 = \$540{,}000$. This figure is derived here, not stated in class.

**Grade split:**

| Grade | Share | Quantity | Quality rating |
|---|---|---|---|
| A (superior) | $20\%$ | $0.2 \times 3{,}000{,}000 = 600{,}000$ lb | 9 |
| B | $80\%$ | $0.8 \times 3{,}000{,}000 = 2{,}400{,}000$ lb | 5 |

- Ratings are on a 10-point scale.
- Grades **can be blended** into a combined grade. The case assumes **linearity**, so the blend's quality is a weighted average of the inputs' ratings.

**Demand forecasts (as read in class):**

| Product | Demand forecast |
|---|---|
| Whole tomatoes | $800{,}000$ |
| Tomato juice | $50{,}000$ |
| Tomato paste | $80{,}000$ |

- The instructor said "pounds". In the original case these figures are in **cases**, so verify the units against the case document.

### 2.10 Cooper's analysis (Exhibit 2)

**Method:** contribution per case = selling price − total variable cost.

**Variable cost items and why they count as variable:**
- **Direct labor:** variable if labor is contractual and paid hourly. One more case incurs extra cost (≈3.4 mentioned for whole tomatoes).
- **Variable overhead.**
- **Variable selling cost:** e.g. a commission paid to the sales channel per box sold.
- **Packaging material:** one more unit packed means one more unit of packaging cost.
- **Fruit (food) cost:** the cost of the tomatoes.

**Worked figure (as stated in class):**
$$\text{Contribution} = 12 - 10.8 = 1.2$$

**Allocated overhead:** Cooper also subtracts allocated fixed overhead. The instructor said to **ignore this**, because fixed costs should be kept separate from contribution analysis. This is the same lesson as in the Merton Truck case.

### 2.11 Next steps (session cut off here)

- Exhibit 3 is **Myers' analysis**, still to be discussed.
- The class was beginning to determine **how much grade A and grade B tomato each product requires**. This feeds into the blending/quality constraints of the LP.

---

## 3. Exam / Assignment Flags

- **No explicit exam statements** appear in this portion of the transcript.
- **Participation is expected.** The instructor said that if students have not read the case and do not participate, "it will be very difficult". Read the Red Brand Canners case (Exhibits 2 and 3) before the next class.
- **Likely testable skills,** given the emphasis in class:
  - **Computing the allowable range of an objective coefficient.** The objective-coefficient ratio must lie between the binding constraints' coefficient ratios. Remember to flip the inequalities when taking reciprocals.
  - **Interpreting reduced cost and shadow price.** For example, Model 103 has reduced cost $-350$.
  - **Separating variable costs from allocated fixed costs** when computing contribution margins.

<!-- nav -->
← [Session 36 (2026-11-10)](DSM-101-36_2026-11-10_Ruchi-Sharma.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
