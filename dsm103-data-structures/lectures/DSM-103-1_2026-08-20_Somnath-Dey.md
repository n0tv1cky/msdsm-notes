# DSM-103 — Data Structures
## Session Notes: Arrays — Basic Operations (Traversal, Sorting, Searching)
**File:** DSM-103-1_2026-08-20_Somnath-Dey**

---

## 1. Overview

This session continues from the previous lecture's introduction to data structures and the one-dimensional (1-D) array. It begins by recapitulating array terminology (finite, ordered, homogeneous collection; size, type, base, index, range of indices) and the size/index/address mapping formulas for a 1-D array. The instructor then enumerates the common operations performed on arrays — **traversal, sorting, searching, insertion, deletion, merging** — and works through the first three in detail. For each, he stresses the discipline of first identifying *input*, *output*, and *data structure used*, then writing language-independent pseudocode using generic bounds `L` (lower index) and `U` (upper index) rather than C-style 0-based indices. Along the way there is a digression comparing `while`, `for`, and `do-while` loops (and why `do-while` always executes its body at least once). Bubble sort is developed from first principles (adjacent-pair comparison and swapping, with the array "shrinking" by one after each pass) and hand-traced on the arrays `7 9 5 4 10 8` and `5 9 7 6`. Linear search is developed with a `found` flag and a `location` variable, followed by a discussion of duplicate keys, worst-case behaviour, and two take-home modifications (find the *last* occurrence; find *all* occurrences). The session ends with administrative notes about LMS accounts and course material upload.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Recap — Array Storage Model
- An array stores its elements in a **contiguous memory location** — there are **no gaps/blank spaces** inside the array.
- All elements are of the **same data type** (homogeneous).
- **Worked addressing example given in class:**
  - If the first element is at address **453** and each element occupies **1 byte (or 1 word)**, the next element is at **454**.
  - If each element occupies **2 bytes**, the first element is at **453** and the second element is at **455**.
  - (General rule implied: consecutive elements are `w` bytes apart, where `w` = size of one element.)

### 2.2 Array Terminology (recapitulated definitions)
| Term | Definition as given |
|---|---|
| **Array** | A **finite**, **ordered** collection of **homogeneous** data. |
| **Finite** | The number of elements is fixed. |
| **Ordered** | Stored in continuous (contiguous) memory locations. |
| **Homogeneous** | All elements are of the same type (all integer, or all float, etc.). |
| **Size** | Number of elements in the array (also called length / dimension). |
| **Type** | The data type of the elements to be stored. |
| **Base** | The starting memory location — the address of the first element. |
| **Index (subscript)** | Used to refer to a particular element. |
| **Range of indices** | The indices vary from a lower bound **L** to an upper bound **U**. E.g. if indices run 1…10 then `L = 1`, `U = 10`. |

### 2.3 Formulas for a 1-D Array — **write these down**

**Size (number of elements):**
```
Size = U − L + 1
```
*Example:* L = 1, U = 10 → Size = 10 − 1 + 1 = 10.

**Referring to the i-th element (i counted from 1):**
```
A[L + i − 1]
```

**Address / mapping function (the "indexing formula" referred to from the previous lecture):**
```
Address(A[i]) = Base + w × (i − L)
```
where `Base` = base address of the array and `w` = size (in bytes/words) of one element.
> The instructor referred back to "the indexing formula / mapping function already discussed" rather than re-deriving it; the class was told that given an index, this formula yields the memory address of that element.

### 2.4 List of Common Array Operations (the agenda)
1. **Traversing** — accessing/visiting each element of the array once.
2. **Sorting** — arranging a given set of elements in order.
3. **Searching** — finding the position of a particular *key* element.
4. **Insertion**
5. **Deletion**
6. **Merging**

> Methodological point stressed: before writing/implementing any algorithm, identify **(a) the input, (b) the output, (c) the data structure(s) used**.

---

## 3. Operation 1 — Traversal

### 3.1 Specification
- **Input:** An array `A` with lower index `L` and upper index `U`.
- **Output:** Each element "processed" — e.g. printed, or used in some other computation. The word **"process"** is used generically so the algorithm is not tied to printing.
- **Data structure:** 1-D array.

### 3.2 Idea (described visually)
Picture the array as a row of boxes labelled with indices `L, L+1, L+2, …, U`. Take a **temporary index variable** (called `I` in the algorithm, `J` in the informal walk-through) and point it at the first box. Read the value with a statement like `V = A[J]` — this returns whatever value currently sits at position `J` — then use `V` (print it, or compute with it). Then move the pointer one box to the right and repeat until you fall off position `U`.

Example array used: `7 8 9 5 4 10` at indices `1 2 3 4 5 6` (so `L = 1`, `U = 6`).

### 3.3 Algorithm (Traversal)
```
TRAVERSE(A, L, U)
1. I ← L                       // initialize temp variable to the lower index
2. while (I ≤ U) do            // if false, steps 3–4 are skipped entirely
3.     process A[I]            // e.g. print A[I], or V ← A[I]; use V
4.     I ← I + 1               // move to next position
   end while
5. stop
```

### 3.4 Hand-trace (with L = 1, U = 6)
- `I = 1` → `1 ≤ 6` true → print `A[1]` → `I = 2`
- `I = 2` → `2 ≤ 6` true → print `A[2]` → `I = 3`
- … continues until `I = 7` → `7 ≤ 6` false → loop exits.

**Complexity:** one pass over `n = U − L + 1` elements ⇒ **O(n) time, O(1) extra space**.

---

## 4. Digression — `while` vs `for` vs `do-while`

Asked whether the traversal could use a `for` loop: **yes**, but be careful with `do-while`.

**`while` loop — order of steps**
1. Initialization is done **outside** the loop.
2. Condition is checked.
3. If condition is true, execute all statements inside the loop body; go back to step 2.

**`for` loop — order of steps**
1. Initialization (inside the `for` header) — step 1.
2. Condition check — step 2.
3. If true, enter the body; then the increment — step 3; then back to the condition check.

**`do-while` loop — order of steps**
1. Initialization outside the loop.
2. Execute **all statements inside the `do` block first** (step 1 of the loop).
3. *Then* check the condition (step 2). If true, repeat the body; if false, exit.

**Key consequence (with the numeric example used):**
Let `I = 5` and the loop condition be `5 < 4` (false).
- With `while` / `for`: the body is **never executed** (condition checked first).
- With `do-while`: the body is **executed once** before the condition is checked, *irrespective of the condition*.

⇒ There are situations where `do-while` will produce wrong behaviour because of this guaranteed one execution.

---

## 5. Operation 2 — Sorting (Bubble Sort)

### 5.1 Informal development
Sample input array `A` (indices 1…6, so `L = 1`, `U = 6`):

```
index :  1   2   3   4   5   6
value :  7   9   5   4  10   8
```

Goal: **ascending order**. Approach suggested in class: compare **adjacent** elements only (not every element with every other element) and **swap if out of order**, so that the larger element keeps "bubbling" to the right.

**Rule used (ascending):** compare `A[i]` with `A[i+1]`; **swap if `A[i] > A[i+1]`**; do nothing if `A[i] ≤ A[i+1]`.
(Equivalently, as written in the algorithm: *swap when the test `A[i] < A[i+1]` is **false***.)

**Pass 1 trace on `7 9 5 4 10 8`:**
| Compare | Test | Action | Array after |
|---|---|---|---|
| 7, 9 | 7 > 9? No | no swap | 7 9 5 4 10 8 |
| 9, 5 | 9 > 5? Yes | swap | 7 5 9 4 10 8 |
| 9, 4 | 9 > 4? Yes | swap | 7 5 4 9 10 8 |
| 9, 10 | 9 > 10? No | no swap | 7 5 4 9 10 8 |
| 10, 8 | 10 > 8? Yes | swap | 7 5 4 9 8 10 |

**After pass 1 the largest element (10) is guaranteed to be at position `U`.**

**Shrinking the working array:**
- After pass 1 → treat the array as `L … U−1` (last 1 element already sorted).
- After pass 2 → `L … U−2` (last 2 elements sorted).
- After pass 3 → last 3 elements sorted, and so on.
- When only a single element remains, no comparison is needed — it is sorted by default, and the whole array is sorted.

### 5.2 Contrast with selection sort (mentioned in passing)
An alternative approach: pick one element, compare it with **all** other elements, keep the largest in a variable, then place it at the end. That is a different logic — **selection sort** (the instructor first mis-said "insertion sort", then corrected to selection sort). Bubble sort, by contrast, only ever compares **adjacent pairs**.

### 5.3 Descending order / other variants
- To get descending order (or to bring the smallest element to the front), simply **reverse the comparison operator** (`<` instead of `>`). "There is no fixed algorithm for sorting — sorting is an operation; how you do it depends on the implementation."

### 5.4 Algorithm (Bubble Sort)
```
BUBBLE_SORT(A, L, U)
1. I ← U                              // I marks the last unsorted position
2. while (I > L) do
3.     J ← L                          // J walks the unsorted part
4.     while (J < I) do               // equivalently J ≤ I−1, so that A[J+1] exists
5.         if ( order(A[J], A[J+1]) is FALSE ) then
6.             swap A[J] and A[J+1]
           end if
7.         J ← J + 1
       end while
8.     I ← I − 1                      // shrink the unsorted region by one
   end while
9. stop
```
Where `order(x, y)` is:
- `x < y` → sorts in **ascending** order (swap when the "<" test fails),
- `x > y` → sorts in **descending** order.

**Why `J < I` and not `J ≤ I`:** `J` is the index used for the *pair* `(A[J], A[J+1])`. If `J` were allowed to reach the last position, `A[J+1]` would be **undefined** (no such element). So `J` must stop at the second-to-last element.

**Why the outer variable `I`:** it records how far the "unsorted" portion of the array extends. Initially `I = U`; each pass reduces it by 1, so the inner loop never re-touches the already-sorted tail.

### 5.5 Full worked trace: `A = 5 9 7 6`, indices 1…4, `L = 1`, `U = 4`, ascending
Using `order = (A[J] < A[J+1])`, swap when **false**.

**Pass 1 — `I = 4` (`4 > 1` true), `J ← 1`:**
| J | Test `A[J] < A[J+1]` | Result | Array |
|---|---|---|---|
| 1 | 5 < 9 → true | no swap | 5 9 7 6 |
| 2 | 9 < 7 → false | **swap** | 5 7 9 6 |
| 3 | 9 < 6 → false | **swap** | 5 7 6 9 |
| 4 | `4 < 4` false → exit inner loop | | 5 7 6 9 |

`I ← 3`.

**Pass 2 — `I = 3` (`3 > 1` true), `J ← 1`:**
| J | Test | Result | Array |
|---|---|---|---|
| 1 | 5 < 7 → true | no swap | 5 7 6 9 |
| 2 | 7 < 6 → false | **swap** | 5 6 7 9 |
| 3 | `3 < 3` false → exit inner loop | | 5 6 7 9 |

`I ← 2`.

**Pass 3 — `I = 2`, `J ← 1`:** `5 < 6` true → no swap; `J = 2`, `2 < 2` false → exit. `I ← 1`.
Outer condition `1 > 1` false → **done. Sorted: 5 6 7 9.**

**Complexity:** nested loops over the array ⇒ **O(n²) time** (worst and average), **O(1) extra space** (in-place, swaps only).

### 5.6 Note on indexing conventions (asked in class)
- In C, indices start at **0**, so you would set `L = 0` and `U = n − 1`.
- In the lecture's **general/pseudocode** form, `L` and `U` are abstract — the instructor assumes implementation from `1` to `n`. **When writing algorithms, do not hard-code programming-language index conventions**; use `L` and `U`.

---

## 6. Operation 3 — Searching (Linear / Sequential Search)

### 6.1 Idea
Array used in the example: `5 8 6 4 2`, with **KEY = 6**; we want the *position* at which the key occurs.

Start with `J` at the first element; test `A[J] == KEY`. If equal, return `J`. If not, increment `J` and repeat, up to `U`.

**Question raised by a student:** if we scan all the way to `U` even after finding the key, what's the problem?
- **Answer:** wasted time (poorer time complexity). Scanning the whole array is only needed if you want the *frequency* of the key; if you want the first (or a single) occurrence, you should break out of the loop.
- Also: if you keep looping without a flag, the returned index gets **overwritten/reset** on each iteration — you'd only correctly report something for the last element. Hence you must use a **flag** to record that the key was found and to stop.

### 6.2 Algorithm (Linear Search with flag)
```
LINEAR_SEARCH(A, L, U, KEY)
1. I ← L
2. FOUND ← 0                 // 0 = not yet found
3. LOCATION ← 0              // 0 is an index that does not exist (sentinel);
                             //   alternatively use a negative value
4. while (I ≤ U  AND  FOUND = 0) do
5.     if (A[I] = KEY) then
6.         FOUND ← 1
7.         LOCATION ← I
       end if
8.     I ← I + 1
   end while
9. if (FOUND = 0) then
10.        print "KEY is not in array"
   else
11.        print "KEY is in array at position LOCATION"
   end if
12. stop
```

**Loop exit analysis (explicitly discussed):** the `while` can terminate for two reasons —
1. `I > U` (ran off the end) → `FOUND` is still `0` → key **not present**;
2. `FOUND = 1` → key **found**, and `LOCATION` holds its index.
That is why step 9 must test `FOUND` to decide which message/result to produce.

**Sentinel choice:** `LOCATION = 0` works if valid indices start at 1; if index 0 is valid (C), initialize `LOCATION` to a **negative value** instead, so that "a positive value means a real index".

**Complexity:** **O(n) time** in the worst case (key absent, or key at the last position), **O(1)** extra space. Best case O(1) (key at first position).

### 6.3 Duplicate keys — discussion
- With the algorithm above, if the key occurs multiple times, you get the **first appearance** (because the loop breaks on the first match).

**Ways to get the LAST occurrence:**
1. **Scan backwards:** initialize `I ← U` and decrement, breaking on the first match (the "tricky" but efficient version).
2. **Scan forwards without the `FOUND` break:** remove `FOUND = 0` from the loop condition, and every time `A[I] = KEY`, overwrite `LOCATION ← I`. At the end, `LOCATION` holds the index of the last match. (Cost: you must always scan the whole array, since you don't know in advance how many duplicates exist.)

**Worst-case comparison:** if there is only a single occurrence and it is at the **last** position, both versions scan the entire array — so in the worst case they cost the same; the early-break version is only better on average/in favourable cases.

**Getting ALL indices of a repeated key:**
- Maintain an **auxiliary array of the same size** as `A`. For every index where the key is found, set the corresponding tag/flag to **1**; all other positions remain **0**. At the end, the positions holding `1` give all the indices of the key.
- **Trade-off:** this costs **O(n) extra space** (space complexity), which is why the point was raised in class.
- (Another suggestion made: keep a **counter** to record the number of appearances / frequency.)

---

## 7. Diagrams Described in Words

- **1-D array layout:** a horizontal row of equal-sized boxes. The leftmost box is labelled index `L` (base address), then `L+1`, `L+2`, …, and the rightmost is `U`. The size of the row is `U − L + 1` boxes. Memory addresses increase left to right in steps of `w` bytes (e.g. 453, 454, 455 … for `w = 1`; 453, 455, 457 … for `w = 2`).
- **Traversal pointer diagram:** a single arrow labelled `I` (or `J`) starting under the leftmost box and stepping one box to the right per iteration until it moves past `U`.
- **Bubble sort diagram:** two adjacent boxes under comparison, with `J` pointing at the left box and `J+1` at the right box; the pair "window" slides rightwards. A second marker `I` sits at the right end of the *unsorted* region and moves one box left after every pass; the region to the right of `I` is shaded as "already sorted", and the "bubble" metaphor is that the largest element rises/travels to the right end each pass.

---

## 8. Flagged as Assignment / Exam-Relevant

1. **Assigned task (explicit homework):** *Modify the linear-search algorithm so that, when the key occurs multiple times (2, 3, 4 … occurrences), it returns the index of the **last** occurrence.* Two hinted routes: search from the back (`I ← U`, decrement), or drop the `FOUND` early-exit and keep overwriting `LOCATION`.
2. **Follow-up exercise posed in class:** *If the key appears, say, three times, return **all three indices**.* Expected answer: use an additional array of flags (same size as `A`), setting 1 at each matching index — note the resulting **space complexity** cost.
3. **Conceptual points emphasised:**
   - Always state **input, output, and data structure** before writing an algorithm.
   - Write algorithms **generically with `L` and `U`**, not with language-specific 0-based indices.
   - Know **why `J < I`** (not `J ≤ I`) in bubble sort — otherwise `A[J+1]` is undefined.
   - Know the difference between `while`/`for` and `do-while` (body executed at least once).
   - Understand best/worst case reasoning for search (early break vs full scan) and the time–space trade-off when collecting all occurrences.
4. **Announced next topic:** searching was introduced here; more search techniques (and insertion/deletion/merging) to follow.

---

## 9. Administrative Notes
- LMS accounts were created; an activation email was sent on **17 August** to IIT (institute) email IDs — **check the spam folder** if not seen in the inbox.
- Students confirmed they can log in and see the courses but that **no material was uploaded yet**; the instructor said he will now **upload this lecture's material** to the LMS.