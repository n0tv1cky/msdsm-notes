---
course: DSM 103
date: 2026-11-17
start: 7:00pm
session: "19"
faculty: Surya Prakash
---

<!-- nav -->
← [Session 17-18 (2026-11-12)](DSM-103-17-18_2026-11-12_Somnath-Dey.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->

# DSM-103 · Session 19: Merge Sort, Divide & Conquer, and Recurrence Relations

*Lecture by Surya Prakash, 2026-11-17*

---

## 1. Overview

This session first recaps what sorting means: producing an ordered permutation of the input. It then introduces three ways of classifying sorting algorithms: **internal vs. external**, **in-place**, and **stable**. Stability is motivated with numeric and student-record examples. The main topic is **merge sort**, built on the **divide and conquer** paradigm (divide → conquer → combine). The lecture works through a 7-element example and presents the recursive `MERGE-SORT(A, p, r)` procedure, which introduces the idea of **recursion**. It then covers the `MERGE(A, p, q, r)` procedure, including the index arithmetic for $n_1$ and $n_2$, the auxiliary arrays $L$ and $R$, and its $O(n)$ cost. Finally, the lecture writes the merge sort recurrence $T(n) = 2T(n/2) + O(n)$ and solves it with the **substitution method**, giving $O(n \log n)$. Merge sort is concluded to be **stable but not in-place**, since it needs $O(n)$ extra space. Searching is deferred to the next session.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap: What sorting is

- **Input:** a sequence $a_1, a_2, a_3, \ldots, a_n$.
- **Output:** a **permutation** $a'_1, a'_2, \ldots, a'_n$ of the input such that $a'_1 \le a'_2 \le \cdots \le a'_n$ (ascending). Descending order is also acceptable.
- **Permutation** means the same numbers written in a different order.
  - Example with $10, 12, 9$: possible permutations include $(10, 12, 9)$, $(10, 9, 12)$, $(12, 9, 10)$ and $(9, 10, 12)$.
  - The sorted (ascending) permutation is $(9, 10, 12)$.
- **Worked example:** input $8, 2, 4, 9, 3, 6$ gives sorted output $2, 3, 4, 6, 8, 9$. Each element is $\le$ the element after it.

### 2.2 Internal vs. external sorting

- **Internal sort:** all the data being sorted must be in the computer's **main memory (RAM)** while the algorithm runs.
- **External sort:** some of the data may stay on a slower **external storage device** (e.g., hard disk) during sorting.

### 2.3 In-place sorting

- **Definition:** an in-place sort needs no extra space beyond the input. A **constant** amount of extra space, $O(1)$, is acceptable.
- If the extra space grows with the number of elements, e.g. $O(n)$, the sort is **not** in-place.
- Bubble sort and selection sort (previous class) are in-place.
- **Merge sort is NOT in-place.** Sorting $n$ numbers needs auxiliary arrays totalling $n$ elements.

### 2.4 Stable sorting

- **Definition:** a sort is **stable** if elements with **equal values (equal rank)** keep their original relative order in the output.

**Example 1**
- Input: $2, 5, 8, 5, 3$.
- Sorted: $2, 3, 5, 5, 8$.
- The sort is stable if the first $5$ in the output is guaranteed to be the first $5$ of the input, and the second is the second.

**Example 2**
- Input: $2, 8, 3, 7, 3, 9, 3$.
- Sorted: $2, 3, 3, 3, 7, 8, 9$.
- The sort is stable if the three 3s appear in the output in the same order (1st, 2nd, 3rd) as in the input.

**Why stability matters**
- For plain numbers it makes no visible difference.
- It matters when each key has **associated data (records)**.
- **Example:** student records with marks
  - Input (names partially reconstructed): A: 80, B: 70, C: 80, D: 60.
  - A stable sort by marks keeps **A's 80 before C's 80**, because A came before C in the input.
  - An unstable sort could put C ahead of A even though their marks are equal. It would unfairly "push back" someone who was ahead.

**Stability of known algorithms**

| Algorithm | Stable? | Discussed in this course? |
|---|---|---|
| Bubble sort | Stable | Yes |
| Merge sort | Stable | Yes (today) |
| Insertion sort | Stable | Mentioned only (not discussed) |
| Counting sort | Stable | Mentioned only |
| Selection sort | **Not stable** | Yes |
| Heap sort | Not stable | Not compulsory |
| Quick sort | Not stable | Not compulsory |

### 2.5 Divide and conquer paradigm

A general **algorithm-design strategy**, not specific to sorting. Quick sort also uses it, and the lecturer listed heap sort as well. It has three phases:

1. **Divide:** split the big problem into smaller sub-problems (2, 3, or more parts). Repeat the division over multiple levels until the sub-problems are easy to solve.
2. **Conquer:** solve the small sub-problems directly.
3. **Combine:** merge the sub-solutions to get the solution of the parent problem, level by level up to the original problem.

**Diagram described in words (problem tree)**
- The root is problem $P$.
- $P$ has two children, $P_1$ and $P_2$.
- $P_1$ has children $P_{11}$ and $P_{12}$; $P_2$ has children $P_{21}$ and $P_{22}$.
- The leaves are solved, giving solutions $S_{11}, S_{12}, S_{21}, S_{22}$.
- Combining $S_{11}$ and $S_{12}$ gives $S_1$, the solution of $P_1$. Combining $S_{21}$ and $S_{22}$ gives $S_2$.
- Combining $S_1$ and $S_2$ gives $S$, the solution of $P$.

### 2.6 Merge sort: worked example (7 numbers)

The input is $38, 27, 43, 3, 9, 82, 10$, reconstructed from the transcript.

**Divide phase (tree, top to bottom)**
- **Level 0:** $P$ = sort $[38, 27, 43, 3, 9, 82, 10]$ (7 elements).
- **Level 1:**
  - $P_1$ = sort $[38, 27, 43, 3]$ (4 elements).
  - $P_2$ = sort $[9, 82, 10]$ (3 elements). With an odd count, one half gets one more element.
- **Level 2:** $P_{11} = [38, 27]$, $P_{12} = [43, 3]$, $P_{21} = [9, 82]$, $P_{22} = [10]$.
- **Level 3:** $P_{111} = [38]$, $P_{112} = [27]$, $P_{121} = [43]$, $P_{122} = [3]$, $P_{211} = [9]$, $P_{212} = [82]$.
  - $[10]$ already has size 1, so it is not divided further. The lecturer labelled it $P_{221}$.

**Conquer phase**
- An array with **one element is already sorted**.
- So the solution of each size-1 sub-problem is the element itself. For example, $S_{111} = [38]$ and $S_{112} = [27]$.

**Combine (merge) phase, bottom to top**
- $[38] + [27] \to [27, 38]$, which is $S_{11}$.
- $[43] + [3] \to [3, 43]$, which is $S_{12}$.
- $[9] + [82] \to [9, 82]$, which is $S_{21}$.
- $[10]$ stays as $[10]$, which is $S_{22}$.
- $[27, 38] + [3, 43] \to [3, 27, 38, 43]$, which is $S_1$.
- $[9, 82] + [10] \to [9, 10, 82]$, which is $S_2$.
- $[3, 27, 38, 43] + [9, 10, 82] \to [3, 9, 10, 27, 38, 43, 82]$, which is the final $S$.

**Step-by-step merge of $[27, 38]$ and $[3, 43]$** (answer to a student's question)
1. Compare the fronts 27 and 3. The smaller is 3, so output 3 and remove it. Output: $[3]$.
2. Compare 27 and 43. Output 27. Output: $[3, 27]$.
3. Compare 38 and 43. Output 38. Output: $[3, 27, 38]$.
4. The left list is exhausted, so copy the remainder, 43. Output: $[3, 27, 38, 43]$.

**Why merging sorted arrays is cheap** (student Q&A)
- Both input arrays are already sorted.
- So the next element of the output **must** be the minimum of the left front or the right front. No other element can be smaller.
- That means **one comparison per output element**.
- Merging arrays of sizes $m$ and $n$ therefore takes $O(m + n)$. With $N$ total elements this is $O(N)$.
- If the arrays were not sorted, each element would need comparing with many others (as in bubble sort's $n - 1$ comparisons per pass). Sorting from scratch that way costs $O(n^2)$.

### 2.7 Recursion

- Normally one method calls a different method, e.g. `method1` calls `method2`, which calls `method3`.
- A **recursive** method **calls itself from within its own body**.
- `MERGE-SORT` is recursive: its body calls `MERGE-SORT` on the two halves.
- Each recursive call works on a different part of the same array. This is why the function needs the **range parameters $p$ and $r$**, not just the array $A$.
- Example: the top call is on $A[1..8]$. Its two inner calls are on $A[1..4]$ and $A[5..8]$, and so on.

### 2.8 `MERGE-SORT` algorithm

```
MERGE-SORT(A, p, r)          // sort subarray A[p..r]
1. if p < r                  // more than one element
2.     q = floor((p + r) / 2)    // midpoint
3.     MERGE-SORT(A, p, q)       // sort left half
4.     MERGE-SORT(A, q+1, r)     // sort right half
5.     MERGE(A, p, q, r)         // combine the two sorted halves
```

- The **initial call** for an $n$-element array is `MERGE-SORT(A, 1, n)`.
- **Worked example for an 8-element array:**
  - Initial call: `MERGE-SORT(A, 1, 8)`.
  - Midpoint: $q = \left\lfloor \frac{1+8}{2} \right\rfloor = \lfloor 4.5 \rfloor = 4$.
    - The lecturer briefly said "ceiling", then corrected it to **floor**: the largest integer $\le 4.5$.
  - Recursive calls: `MERGE-SORT(A, 1, 4)` and `MERGE-SORT(A, 5, 8)`.
  - Then `MERGE(A, 1, 4, 8)`.

### 2.9 `MERGE` algorithm (merging two sorted subarrays of the same array)

- The two sorted runs are **parts of the same array $A$**: $A[p..q]$ and $A[q+1..r]$.
- **Layout described in words:** array $A$ is drawn with index $p$ at the left end, $q$ at the midpoint, and $r$ at the right end. The left block $A[p..q]$ is sorted, and the right block $A[q+1..r]$ is sorted.

**Index-counting formulas (call these out)**
- The number of elements from index $x$ to $y$ inclusive is $y - x + 1$.
  - Example: indices 1 to 6 give $6 - 1 + 1 = 6$ elements.
- Left part $A[p..q]$: $n_1 = q - p + 1$.
- Right part $A[q+1..r]$: $n_2 = r - (q+1) + 1 = r - q$.

```
MERGE(A, p, q, r)
1.  n1 = q - p + 1
2.  n2 = r - q
3.  create auxiliary arrays L[1..n1] and R[1..n2]
4.  for i = 1 to n1:  L[i] = A[p + i - 1]    // copy left half
5.  for j = 1 to n2:  R[j] = A[q + j]        // copy right half
6.  i = 1; j = 1
7.  for k = p to r:                          // fill A[p..r]
8.      if L[i] <= R[j]:                     // take from L
9.          A[k] = L[i];  i = i + 1
10.     else:                                // take from R
11.         A[k] = R[j];  j = j + 1
```

**How the copy and the pointers work**
- Copying: $L[1] = A[p]$, $L[2] = A[p+1]$, and so on. The right half is copied into $R$ the same way.
- Pointers $i$ and $j$ always point to the **current front** (smallest remaining element) of $L$ and $R$.
- Each step compares the two fronts and writes the smaller one to $A[k]$. It then advances only the pointer of the array the element was taken from.

**Notes on the pseudocode**
- **Bounds:** the lecture did not address what happens when one of $L$ or $R$ runs out. In practice, either copy the leftover elements of the other array, or use the textbook trick of a sentinel value $\infty$ at the end of each of $L$ and $R$.
- **Stability:** the lecturer described the comparison as "$L[i]$ less than $R[j]$". For merge sort to be **stable**, use $L[i] \le R[j]$. On ties, the left (earlier) element must go first.

**Complexity of `MERGE`**
- Copy loops: $O(n_1)$ and $O(n_2)$.
- Merge loop: runs $r - p + 1 = N$ times, which is $O(N)$.
- Total time: $O(n_1) + O(n_2) + O(N) = O(N)$, i.e. **linear**.
- Extra space: $L$ and $R$ together hold $n_1 + n_2 = N$ elements, so **$O(n)$ auxiliary space**. This is why merge sort is not in-place.

### 2.10 Recurrence relation for merge sort

- Let $T(n)$ be the time to merge-sort $n$ elements.
- The work splits into three parts:
  - two recursive calls on halves, costing $2T(n/2)$;
  - one merge, costing $O(n)$.
- This gives the recurrence and its base case:

$$T(n) = 2\,T\!\left(\frac{n}{2}\right) + O(n), \qquad T(1) = a \ (\text{a constant})$$

- The base case holds because sorting one element takes constant time.

### 2.11 Solving the recurrence: substitution method

**Assumptions**
- Assume $n = 2^k$. This loses nothing, because a non-power of 2 (e.g. 17) can be padded with dummy elements up to the next power of 2.
- Replace $O(n)$ with $cn + c_0$ so the algebra can be done explicitly:

$$T(n) = 2T\!\left(\frac{n}{2}\right) + cn + c_0$$

**Step 1.** Apply the same equation with $n$ replaced by $n/2$:

$$T\!\left(\frac{n}{2}\right) = 2T\!\left(\frac{n}{2^2}\right) + c\frac{n}{2} + c_0$$

**Step 2.** Substitute back into the original:

$$T(n) = 2\left[2T\!\left(\frac{n}{2^2}\right) + c\frac{n}{2} + c_0\right] + cn + c_0 = 2^2\,T\!\left(\frac{n}{2^2}\right) + 2cn + (c_0 + 2c_0)$$

**Step 3.** Repeat the substitution. After $k$ steps the pattern is:

$$T(n) = 2^k\,T\!\left(\frac{n}{2^k}\right) + k\,cn + (2^k - 1)\,c_0$$

- The lecturer simply called the last term "some constant". Strictly it equals $(n-1)c_0$, which is $O(n)$, so it does not change the result.

**Step 4.** Use $2^k = n$, which gives $k = \log_2 n$ (taking logs of both sides), and $T(1) = a$:

$$T(n) = n \cdot T(1) + cn\log_2 n + (n-1)c_0 = an + cn\log_2 n + (n-1)c_0$$

**Step 5.** Keep the dominant term. $n \log n$ dominates both $n$ and the constants, so:

$$T(n) = O(n \log n)$$

### 2.12 Merge sort summary

| Property | Merge sort |
|---|---|
| Strategy | Divide and conquer, recursive |
| Time | $O(n \log n)$ |
| Merge step | $O(n)$ |
| Extra space | $O(n)$ (auxiliary arrays $L$ and $R$) |
| In-place? | **No** |
| Stable? | **Yes**. An element to the left of an equal element stays first. |

---

## 3. Exam / Assignment Pointers

- **Exercise (assigned):** Explain why **selection sort is not stable**. Construct an example where equal keys swap their relative order.
- **Exercise (assigned):** Solve, using the **substitution method**:

  $$T(n) = T(n-1) + O(n), \qquad T(1) = \text{constant}$$

  This is the recurrence for bubble sort and selection sort. (Hint: substituting gives $c(n + (n-1) + \cdots + 2) + \text{const}$, which is $O(n^2)$.)
- **Practice recommended:** look up more recurrence-relation problems and solve them with substitution until the method is comfortable.
- **Know these definitions and classifications:**
  - internal vs. external sorting;
  - in-place (constant extra space is allowed);
  - stable, and why it matters for records.
- **Know which algorithms are stable and/or in-place** (see the tables in 2.4 and 2.12).
- **Know the formulas and complexities:**
  - $n_1 = q - p + 1$ and $n_2 = r - q$;
  - $q = \lfloor (p + r)/2 \rfloor$;
  - merge is $O(n)$;
  - merge sort is $O(n \log n)$ time and $O(n)$ space.
- Heap sort and quick sort are **not compulsory** for this course and are optional reading.
- **Next session:** the remaining topic, likely searching.

<!-- nav -->
← [Session 17-18 (2026-11-12)](DSM-103-17-18_2026-11-12_Somnath-Dey.md) · [All lectures](./) · (latest lecture) →
<!-- /nav -->
