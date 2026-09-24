# DSM-103 — Session 11 (2026-09-19) — Circular Queues, Linked-List Queues, Comparison

---

## 1. Overview

This session completes the discussion of **queue implementations**. It begins by recapping why the two earlier array-based "fixes" for the queue-full problem (shifting elements on every dequeue, or shifting only when the rear hits the end) are wasteful — both require extra element-copying work to reclaim free space at the front of the array. The lecture then develops the **circular queue**, where the array is treated as wrapping around ($\text{index } n \to \text{index } 1$), so that space is reclaimed purely by **pointer manipulation** with no shifting, giving **constant-time** enqueue and dequeue. The key mechanism is replacing the update rule $r = r + 1$ with a **modular update** $r = (r \bmod n) + 1$. The instructor derives the queue-full and queue-empty conditions, walks through complete pseudocode for circular `ENQUEUE`/`DEQUEUE`, and traces a full worked example on a circular queue of length 4 through a sequence of enqueue/dequeue operations. The second half covers **queue implementation using a linked list** (enqueue at rear via `getnode()`, dequeue at front with pointer rewiring), explains why circular representation is unnecessary for linked lists, and gives a **side-by-side comparison** of circular array vs. linked-list queues on space utilization and speed. It closes with **queue overflow/underflow** definitions, an assigned **palindrome-checking problem using a stack and a queue together**, and a lengthy Q&A about the midterm exam format and logistics.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Recap: Why the earlier array-based queue solutions are inefficient

- **Solution 1 (shift-on-full):** We do not shift on every deletion. Instead, when `rear` reaches the last index $n$, we check `front`:
  - If `front == 1` → declare **queue full** (genuinely no space).
  - Otherwise → shift **all** elements leftwards (e.g., positions $3 \ldots n$ moved down to start at position 1) to free space at the end, then insert.
- **Solution 2 (shift-on-every-dequeue):** Every time an element is deleted from the front, **all** remaining elements are shifted one position to the left, so `front` always stays at index 1.
- **Cost of both:** with 100 elements in the queue, a shift costs ~100 copy operations.
- **Consequence for complexity:** enqueue/dequeue are **not constant time** in Solutions 1 and 2 — some operations are cheap (no shift needed), others are expensive (full shift required). The time per operation is **non-uniform**.
- **Circular queue advantage:** free space is *used*, not *created*. No shifting at all — only pointer arithmetic. Insertion and removal become **constant time**, $O(1)$.

> Key sentence from lecture: *"We are just utilizing the space which is free. We are not doing anything extra to make the space free."*

---

### 2.2 The circular array — the idea

- The array is **conceptually circular**: after the last index comes the first index.
  - Linear array: next after index $n$ is *nothing* (null / off-the-end).
  - Circular array: next after index $n$ is index **1**.
- **Diagram description:** Picture the array drawn as a ring of $n$ cells, labelled clockwise $1, 2, 3, \ldots, n$. Cell $n$ sits immediately adjacent (clockwise) to cell $1$, closing the loop. Two pointers, `front` (F) and `rear` (R), move clockwise around this ring. Physically it is still an ordinary linear array with indices $1 \ldots n$ — **the indices do not change**; only the *logical* successor relation wraps.
- **Size:** the capacity of the circular queue is $n$ = size of the underlying array (sometimes written as `LENGTH`). **Circularity does not increase capacity** — it only improves *utilization* of the existing $n$ slots.
- **Empty representation:** `front = 0` and `rear = 0` (same convention as the plain linear queue).
- **Index range assumed throughout:** array indices run from $1$ to $n$ (1-based).

---

### 2.3 The modular pointer-update formula ★ (central formula of the lecture)

Plain linear queue update rules:
$$r = r + 1 \qquad\text{(on enqueue)}, \qquad f = f + 1 \qquad\text{(on dequeue)}$$

Circular queue update rules:
$$r = (r \bmod n) + 1 \qquad\text{(on enqueue)}$$
$$f = (f \bmod n) + 1 \qquad\text{(on dequeue)}$$

where $n = \text{LENGTH}$ = size of the array.

**Why it works (as derived in class, with $n = 5$):**

- Wrap-around case: $r = 5$, so
 $$r_{\text{new}} = (5 \bmod 5) + 1 = 0 + 1 = 1$$
 → from the last cell we land on the **first** cell. ✔
- Normal case: $r = 2$, so
 $$r_{\text{new}} = (2 \bmod 5) + 1 = 2 + 1 = 3$$
 → the ordinary "next index" behaviour is preserved. ✔
- **General reasoning:** as long as $r < n$, $r \bmod n = r$, so the formula reduces to $r + 1$. As soon as $r = n$, $r \bmod n = 0$, so the formula yields $1$.
- Contrast: with plain $r = r+1$ and $n=5$, $r=5$ would give $6$ — an invalid index.

**Worked enqueue sequence shown for $n = 5$:** first insertion sets $f = r = 1$; then successively $r = 1+1 = 2$, $r = 2+1 = 3$, $r = 3+1 = 4$, $r = 4+1 = 5$; then the next increment must yield $1$, which only the modular form achieves.

> A student asked: "but index 1 may already hold a value." Instructor's answer: reaching index 1 and *being allowed to store there* are two separate issues — the pointer arithmetic gets you there; a separate **full-check** decides whether insertion is legal.

---

### 2.4 Queue-full condition (circular queue)

**Reasoning:** In a circular queue, when the queue is full the `rear` pointer sits in the cell **immediately before** `front` (going clockwise), i.e. `front` and `rear` end up adjacent. So if you tentatively increment `rear` and the result equals `front`, there is no free cell.

**Condition:**
$$\text{if } \big((\texttt{rear} \bmod \text{LENGTH}) + 1\big) = \texttt{front} \ \Rightarrow\ \textbf{queue is full}$$

Implementation note: compute the incremented value into a temporary variable (called `next` in the pseudocode), compare with `front`; insert only if `next` $\neq$ `front`.

---

### 2.5 Queue-empty condition and the last-element case

- **Empty is represented by:** `front = 0` and `rear = 0`.
- **When does the queue become empty?** When you delete the **last remaining** element. You detect this at deletion time by checking whether `front == rear` (i.e. front and rear point to the same, single element).
- In that case, after returning the item, set **both** `front = 0` and `rear = 0`.
- Otherwise, just advance `front` using the modular formula.

---

### 2.6 Circular queue — ENQUEUE pseudocode

```
ENQUEUE(CQ, item):
    if front == 0:                 // queue is currently empty
        front = 1
        rear  = 1
        CQ[rear] = item            // insert the very first element
    else:
        next = (rear mod LENGTH) + 1     // modular increment
        if next != front:                // there is a free cell
            rear = next
            CQ[rear] = item
        else:
            print "Queue is full"        // overflow
```

- The `mod LENGTH` is *only* needed to handle the case where `rear` is standing at the last array location and must wrap to location 1.
- **Complexity:** $O(1)$ time, $O(1)$ extra space.

---

### 2.7 Circular queue — DEQUEUE pseudocode

```
DEQUEUE(CQ):
    if front == 0:
        print "Queue is empty"           // underflow
        return
    else:
        item = CQ[front]                 // element to be returned
        if front == rear:                // deleting the LAST element
            front = 0
            rear  = 0
        else:
            front = (front mod LENGTH) + 1
        return item
```

- Deletion always happens at the cell pointed to by `front`.
- The `mod LENGTH` handles the case where `front` is at the last array location and must move to location 1.
- **Complexity:** $O(1)$ time, $O(1)$ extra space.

---

### 2.8 Worked example — circular queue with $\text{LENGTH} = n = 4$ ★

Array cells indexed $1, 2, 3, 4$, drawn as a ring. Start: **empty**, $f = 0$, $r = 0$.

| Step | Operation | Cell 1 | Cell 2 | Cell 3 | Cell 4 | front | rear | Notes |
|---|---|---|---|---|---|---|---|---|
| 0 | (initial) | – | – | – | – | 0 | 0 | queue empty |
| 1 | ENQUEUE A | **A** | – | – | – | 1 | 1 | first element: $f=r=1$ |
| 2 | ENQUEUE B | A | **B** | – | – | 1 | 2 | only `rear` moves |
| 3 | ENQUEUE C | A | B | **C** | – | 1 | 3 | |
| 4 | ENQUEUE D | A | B | C | **D** | 1 | 4 | `rear` now at last index |
| 5 | DEQUEUE | – | B | C | D | 2 | 4 | A removed; `front` → 2 |
| 6 | ENQUEUE E | **E** | B | C | D | 2 | 1 | $r=(4\bmod 4)+1=1$; cell 1 is free → wrap-around insert. **Now `rear` < `front`** |
| 7 | DEQUEUE | E | – | C | D | 3 | 1 | B removed |
| 8 | ENQUEUE F | E | **F** | C | D | 3 | 2 | $r=(1\bmod 4)+1=2$, cell 2 free |
| 9 | DEQUEUE | E | F | – | D | 4 | 2 | C removed |
| 10 | DEQUEUE | E | F | – | – | 1 | 2 | D removed; `front` was 4 → $(4\bmod 4)+1 = 1$, wraps to E. **Now `front` < `rear` again** |
| 11 | DEQUEUE | – | F | – | – | 2 | 2 | E removed; $f = r = 2$ (single element left) |
| 12 | DEQUEUE | – | – | – | – | 0 | 0 | F removed — last element, so both set to 0 → **queue empty** |

**Instructor's explicit question during the trace (step 6):** *"What is the value of `r` and `f`?"* → **`r = 1`, `f = 2`.**

**Key observations drawn from this trace:**
- In the **plain (linear) queue**, `rear` is *always* $\geq$ `front`; `rear` never precedes `front`.
- In the **circular queue**, no such guarantee exists. Over time you can have `front < rear`, `front == rear`, or **`rear < front`** (step 6, 7, 8, 9).
- At step 6, a linear implementation would have declared "queue full" (because `rear` was at index $n=4$) or would have had to shift B, C, D leftwards. The circular queue simply wrapped and used the already-free cell 1 — **zero shifting, zero extra work**.

---

### 2.9 Queue implemented with a linked list

**Q: Do we need a "circular" representation for a linked-list queue?**
**A: No.** The underutilization problem is purely an artefact of a fixed-size array. In a linked-list queue, only as many nodes are allocated as there are data items — there are no "free but unusable" slots. So there is no notion of a circular linked-list queue for this purpose.

**Node structure (diagram in words):** each node is a box with two fields — a **data** field (holding the item) and a **link** field (holding the address of the next node). The last node's link is `NULL`. A `front` pointer points at the head node, a `rear` pointer points at the tail node, and a `qhead` pointer is also maintained at the head.

#### ENQUEUE (linked list) — insert at the rear

```
ENQUEUE_LL(item):
    new = getnode()          // allocate a node; 'new' holds its address
    new->data = item
    new->link = NULL         // new node will be the last node

    if front == NULL:        // queue currently empty — this is the first node
        front = new
        rear  = new
        qhead->link = front  // qhead also points to the front
    else:
        rear->link = new     // attach new node after the current rear
        rear = new           // rear now points to the newly created node
```

- `getnode()` creates the space for a node and returns its address; all further references to that node are made through `new`.
- The new node is always attached at the **rear** side.

#### DEQUEUE (linked list) — delete from the front

```
DEQUEUE_LL():
    if front == NULL:
        print "Queue is empty"
        return
    else:
        item = front->data       // value to be returned
        ptr  = front->link       // address of the node AFTER the current front
        qhead->link = ptr        // rewire qhead to the new first node
        front = ptr              // advance front
        if front == NULL:        // we just deleted the last node
            rear = ptr           // i.e. rear = NULL as well
        return item
```

- **Pointer diagram in words:** before deletion, `qhead` and `front` both point at node $N_1$; $N_1\text{->link}$ points at $N_2$. We save $N_2$'s address in `ptr`, re-point `qhead->link` and `front` at $N_2$, and detach $N_1$.
- **Last-node detection:** if the queue held only one node, then that node's link is `NULL`, so `ptr` becomes `NULL`; after `front = ptr`, `front == NULL`, and we must also set `rear = NULL` so the queue is correctly recorded as empty.
- **Empty representation for the linked-list queue:** `front = NULL` (and `rear = NULL`).
- **Complexity:** both enqueue and dequeue are $O(1)$ (rear pointer maintained, no traversal).

---

### 2.10 Comparison: Circular array queue vs. Linked-list queue ★

| Criterion | Circular Queue (array) | Linked-List Queue |
|---|---|---|
| Amount of memory used | Fixed block of $n$ slots allocated up-front | **Always just enough** — one node per element, allocated on demand |
| Wasted space / capacity risk | May **waste unrequired space**, or may **run out of space**. Example given: allocate 100 slots but store only 10 → 90 slots idle; or need more than 100 → overflow | Neither problem: never idle, never (logically) out of space |
| Space **per element** | **Better** — each cell stores only the data | **Worse** — each node stores data **plus** the link/address of the next node, so more space per element |
| Speed of ENQUEUE / DEQUEUE | **Fast**, constant time — no shifting | **Fast**, constant time |
| Overall | Better per-element space utilization | Better overall flexibility (no wastage, no fixed cap) |

**Summary of the trade-off as stated:** the linked list is "better in some way" because space is never needlessly engaged and you never run out; but it uses **more memory per element** because of the stored pointer. Both are fast for enqueue/dequeue.

---

### 2.11 Queue overflow and underflow

- **Queue overflow:** attempting to insert when the queue is **full**.
- **Queue underflow:** attempting to delete when the queue is **empty**.
- These parallel the previously discussed **stack overflow** and **stack underflow**.

---

### 2.12 Assigned problem — Palindrome check using a stack AND a queue

**Definition:** A **palindrome** is a string that reads the same forwards and backwards. Examples given: `level`, `mom`, `noon`.

**Algorithm idea (given in outline; students asked to write the full algorithm):**

1. Create an empty **stack** and an empty **queue**.
2. Read the input string character by character. For each character, **push** it onto the stack **and** **enqueue** it into the queue.
3. Repeatedly: **pop** one character from the stack and **dequeue** one character from the queue; compare them.
4. If **all** compared pairs match, the string is a **palindrome**; if any pair mismatches, it is **not** a palindrome.

**Why it works:** the queue returns characters in original (left-to-right) order; the stack (LIFO) returns them in reverse order. Equality of the two sequences is exactly the palindrome property.

**Worked traces given:**
- Input `MOM` → stack (bottom→top): `M, O, M`; queue (front→rear): `M, O, M`. Pop `M` vs dequeue `M` ✔, `O` vs `O` ✔, `M` vs `M` ✔ → **palindrome**.
- Input `MON` → stack pops give `N, O, M`; queue dequeues give `M, O, N`. **First comparison `N` vs `M` already fails** → not a palindrome (no need to continue).

> **Homework:** "I request all of you to please explore this and try writing the algorithm for it."

---

## 3. Exam / Assignment Notes

### Assigned work
- **Write the algorithm** for the palindrome checker using a stack and a queue together (Section 2.12).

### Midterm exam information given in the Q&A
- **Date:** Tuesday, **29 September**.
- **Format:** **Take-home, un-proctored.** Question paper released on **LMS**.
- **Timing:** QP made available around **7:00 p.m.**; answers must be uploaded by **11:00 p.m.** (a ~4-hour window; instructor said the paper is designed to be doable in 2–3 hours). **LMS closes hard at the deadline — anything not uploaded by then counts as no submission.**
- **Submission artefact:** a **Python (Jupyter) notebook** (`.ipynb` / `.py`) uploaded to LMS. Any written explanations should be typed into **text/markdown cells inside the notebook** rather than in a separate answer sheet.
- **Question style:** mainly **code snippets / programming questions**, possibly plotting tasks — i.e. effectively **subjective/practical**, not purely MCQ. (Earlier in the conversation the instructor initially mentioned objective/MCQ/true-false/fill-in-the-blanks and ~25–30 questions for a 1-hour paper; this was later superseded by the take-home coding-notebook format described above.)
- **Marks:** the paper may be set out of a larger total (e.g. 60–70) and then **scaled down** to the course weightage (e.g. 50%).
- **Syllabus:** **everything covered up to and including today's session** (i.e. through circular queues, linked-list queues, and their comparison). Nothing beyond today will be examined.
- **Sample papers:** instructor agreed to try to share **sample questions** before the midterm.

### Conceptual points most likely to be tested (flagged by emphasis in lecture)
- The modular update formulas $r = (r \bmod n) + 1$ and $f = (f \bmod n) + 1$.
- The circular queue-full condition $\big((\texttt{rear} \bmod \text{LENGTH}) + 1\big) = \texttt{front}$.
- Empty condition `front = rear = 0`, and the rule to reset both to 0 when deleting the last element (`front == rear`).
- The fact that in a circular queue `rear` may be **less than** `front`, unlike in a linear queue.
- $O(1)$ enqueue/dequeue for circular queues vs. non-constant time for the shifting-based linear solutions.
- The circular-array vs. linked-list comparison table.