# DSM-103 Session 10: Algorithms and Time Complexity (Big-O)

*Lecturer: Surya Prakash · 2026-09-21*

---

## 1. Overview

This session introduces **algorithms** and how to measure their **efficiency**. It begins with the definition of an algorithm and how it differs from a program. It then lists the required characteristics of an algorithm: uniqueness, finiteness, precision, input/output, and generality. The main topic is **time complexity**. The lecturer explains why wall-clock execution time is a poor way to compare algorithms, because it depends on the machine, compiler, and so on. Instead, efficiency is measured by counting **elementary steps** as a function of input size $n$, written $T(n)$. Using vector addition as the example, he shows that the same algorithm on different machines gives $T(n) = c_1 n$ and $T(n) = c_2 n$. Both grow linearly, so constants can be ignored and only the **growth rate** matters. This leads to **asymptotic analysis** and the formal definition of **Big-O notation**, with a worked proof that $n^2 + 3n + 1 = O(n^2)$. The session then covers common complexity classes (constant, logarithmic, linear, $n\log n$, quadratic) and a step-counting analysis of a summation algorithm, $T(n) = 2n + 4 = O(n)$. Everything up to and including this session is on the **midterm**.

---

## 2. Topics Covered (in order)

### 2.1 What is an algorithm?

- **Definition:** An algorithm is a *sequence of unambiguous instructions (steps) for solving a problem*. It produces the required output for any legitimate input in a **finite amount of time**.
- **Unambiguous** means each instruction has only **one possible interpretation**, so it can be executed without confusion.
- Algorithms are usually written in **pseudocode**.
  - Pseudocode uses programming-like constructs such as `if/else` and `for i = 1 to 10`.
  - It does not follow any language's syntax rigidly.

### 2.2 Algorithm vs. program

- An **algorithm** describes the steps to be followed. It is language-independent.
- A **program** is an implementation of an algorithm in a specific language (C, Pascal, …).
- One algorithm can have many programs. A C program and a Pascal program for the same algorithm differ because the language constructs differ, but the algorithm stays the same.
- **Examples already seen in class:** the stack operations (push/pop) and queue operations (enqueue/dequeue). These were written in pseudocode with `if/else`, so they are algorithms, not programs.

### 2.3 Characteristics of an algorithm

1. **Uniqueness:** every step is uniquely defined, with no ambiguity.
2. **Finiteness:** it executes a finite number of instructions and **must terminate**. Something that runs forever is not an algorithm.
3. **Precision:** steps are precisely defined, with no vagueness.
4. **Input/Output:** it takes **zero or more inputs** and produces **at least one output**.
   - An output is required because the algorithm exists to accomplish a task.
   - *Zero-input example:* a random-number generator. You call it with no input and still get a random number. Optionally, you could give inputs such as "between 1 and 10".
5. **Generality:** it must work for **all** valid inputs, not just specific ones.
   - *Counter-example:* an even/odd checker that only works for numbers up to 100 lacks generality.

### 2.4 Why not measure execution time?

- **Scenario:** algorithm $A_1$ takes 5 s and $A_2$ takes 10 s. This does **not** mean $A_1$ is better.
  - $A_1$ may be running on a high-end processor.
  - $A_2$ may be running on an old machine.
- Execution time depends on processor speed, disk speed, instruction set, compiler, and more.
- **Solution:** measure complexity by the **number of elementary steps** executed. This measure is independent of machine and implementation.
  - *Example:* $A_1$ solves the problem in 10 steps and $A_2$ in 20 steps, so $A_1$ is more efficient.
- **Assumption:** every elementary step takes the **same constant time**.

### 2.5 Time complexity, space complexity, and asymptotic analysis

- **Time complexity** $T(n)$ is a function giving time (number of steps) versus **input size** $n$.
- **Space complexity** is how much memory the algorithm needs to run.
- Both fall under **computational complexity**.
- **Asymptotic analysis** studies performance as $n \to \infty$ (very large inputs).
  - For small $n$, such as adding 5 or 10 numbers, the time is negligible.
  - What matters is behavior for large $n$, such as adding a million numbers or finding the maximum of a million numbers.

### 2.6 Worked example: adding two vectors (arrays) of size $n$

- **Problem:** arrays $A$ and $B$, each with $n$ elements, are added element by element into array $C$.
- **Diagram (described):** two arrays are drawn one above the other. Element $i$ of the first is added to element $i$ of the second to give element $i$ of a third array. Each such pairwise addition is one elementary step.

**Pseudocode:**
```
for i = 1 to n
    C[i] = A[i] + B[i]      // one elementary step
```

- **Total steps:** $n$.
- If $c$ is the time for one elementary step, then
$$T(n) = c \cdot n$$
- **Two machines:**
  - A fast machine with $c_1 = 1$ s per step gives $T_1(n) = c_1 n$.
  - A slow machine with $c_2 = 2$ s per step gives $T_2(n) = c_2 n$.
- **Plot (described):** the $x$-axis is $n$ and the $y$-axis is $T(n)$. Both are straight lines through the origin with different slopes, the steeper one being the slow machine. Each has the form $y = mx$, with $y = T(n)$, $x = n$, and slope $m = c$.
- **Key observation:** although the lines differ, in **both cases $T(n)$ grows linearly with $n$**.
  - So we ignore $c_1, c_2$ and treat the two as having the same performance: linear.
- **Big idea (emphasized as very important):**
  - Abstract away implementation details.
  - Represent the rate of resource usage purely as a function of input size $n$.

### 2.7 Asymptotic notations

- The notations named were **Big-O ($O$)**, **Big-Omega ($\Omega$)**, and **Big-Theta ($\Theta$)**. Only Big-O was defined in this session.
- **Procedure:**
  1. Count the steps to get an expression for $T(n)$.
  2. Convert it to a compact notation.
  - *Example:* $T(n) = 2n^2 + 3n + 5$ is written as $O(n^2)$.

### 2.8 Big-O notation (formal definition)

- Big-O gives an **upper bound** on a function, within a constant factor.
  - The running time never exceeds $c \cdot g(n)$ for large $n$.
- Here $f(n)$ is the step-count expression and $g(n)$ is a simpler function such as $n^2$, $n^3$, or $\log n$.

**Definition:** $f(n) = O(g(n))$ if there exist a positive constant $c > 0$ and a threshold $n_0$ such that
$$f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0.$$

- **Graphs (described):**
  - *Case 1:* the curve $c \cdot g(n)$ lies above $f(n)$ for all $n$. Then $f(n) = O(g(n))$.
  - *Case 2:* the curves cross. $c \cdot g(n)$ is below $f(n)$ for small $n$ but lies above it from the crossing point $n_0$ onward. We **still** say $f(n) = O(g(n))$, because only large $n$ matters. This is why the definition includes $n_0$.
- *Note:* the transcript at one or two points says "$f$ above $g$" or "$cg(n)$ less than $f(n)$". These are slips. The correct condition is always $f(n) \le c\,g(n)$, meaning $c\,g(n)$ bounds $f(n)$ from **above**.

### 2.9 Worked example: prove $n^2 + 3n + 1 = O(n^2)$

- Here $f(n) = n^2 + 3n + 1$ and $g(n) = n^2$.
- **Goal:** find $c$ and $n_0$ such that $n^2 + 3n + 1 \le c \cdot n^2$ for all $n \ge n_0$.
- **Choose $c = 5$ and $n_0 = 1$:**
  - At $n = 1$: LHS $= 1 + 3 + 1 = 5$ and RHS $= 5 \cdot 1^2 = 5$. They are equal, so the condition holds.
  - At $n = 2$: LHS $= 4 + 6 + 1 = 11$ and RHS $= 5 \cdot 4 = 20$. Since $11 \le 20$, it holds.
  - For any $n \ge 1$ the inequality continues to hold. (Justification: $3n \le 3n^2$ and $1 \le n^2$ for $n \ge 1$, so LHS $\le 5n^2$.)
- **Conclusion:** $n^2 + 3n + 1 = O(n^2)$.
- **Similarly**, a linear expression like $3n + 5$ is $O(n)$.

### 2.10 Common complexity classes

| Order | Name | Example / note |
|---|---|---|
| $O(1)$ | Constant time | No dependence on $n$, e.g. summing the fixed numbers 1 to 5 |
| $O(\log n)$ | Logarithmic time | Binary search |
| $O(n)$ | Linear time | Vector addition, the summation loop below |
| $O(n \log n)$ | Called "poly-logarithmic" in lecture (a polynomial term times a log term) | Many sorting algorithms, covered after the midterm |
| $O(n^2)$ | Quadratic time | Some sorting algorithms |

- *Terminology note:* $n\log n$ is more commonly called **linearithmic** in textbooks. "Polylogarithmic" usually refers to $(\log n)^k$.

### 2.11 Worked example: step-counting a summation algorithm

The algorithm, reconstructed from the transcript (step numbers approximate):
```
1. int n, i, sum          // 1 step (declare)
2. sum = 0                // 1 step
   i = 1                  // 1 step
   input n                // 1 step
3. Repeat steps 3–5 while i <= n:
4.     sum = sum + i      // 1 step
5.     i = i + 1          // 1 step
6. output sum
```

- **Steps outside the loop:** 3 setup steps (declaration, `sum = 0`, `i = 1`) plus 1 input step, for 4 steps.
- **Steps inside the loop:** 2 basic steps per iteration.
- **Number of iterations:** the loop runs for $i = 1, 2, \dots, n$, which is $n$ times, giving $2n$ steps.
- **Total:**
$$T(n) = 2n + 4 = O(n)$$
- The loop-condition checks and the output step were not counted separately. This simplification does not change the order.
- **Space:** only a constant number of variables are used. (This is standard, not stated explicitly in lecture.)

### 2.12 Rule of thumb for finding the order

- **Keep the highest-order term** and drop lower-order terms and constant coefficients.
  - $n^2 + 3n + 5$ gives $O(n^2)$.
  - $2n + 4$ gives $O(n)$.
- **Example:** $T(n) = 3n\log n + 5n + 20$ gives $O(n\log n)$, since $n\log n$ grows faster than $n$.
- This shortcut agrees with the formal $c, n_0$ proof, which can always be done.

---

## 3. Exam / Assignment Notes

- **Midterm syllabus:** everything covered **up to and including this session** is on the midterm exam.
- **Exercise given in class:** find $c$ and $n_0$ showing $2n + 4 \le c\cdot n$, which proves $2n + 4 = O(n)$.
  - The lecturer's hint: $c = 10$ works from $n = 1$ onward.
  - Check: $2n + 4 \le 10n \iff 4 \le 8n$, which is true for all $n \ge 1$.
- **Emphasized as important:**
  - Why step-counting beats execution time.
  - Abstracting away constants to focus on the growth rate.
  - The formal Big-O definition with $c$ and $n_0$.
- **Coming after the midterm:** sorting algorithms, with $O(n\log n)$ and $O(n^2)$ complexities.