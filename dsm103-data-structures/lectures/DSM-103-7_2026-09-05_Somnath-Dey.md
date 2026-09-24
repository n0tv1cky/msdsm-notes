# DSM-103 Data Structures — Session 7
**Date:** 2026-09-05 · **Instructor:** Somnath Dey
**File:** DSM-103-7_2026-09-05_Somnath-Dey

---

## 1. Overview

This session completes the linked-list block of the course. It opens with a discussion of **real-world applications of linked lists** (playlists, queue implementation, insertion into a sorted sequence, polynomial representation, and free-space/memory management), then introduces the **doubly linked list (DLL)** — its node structure (left link / data / right link), header node, and the **circular doubly linked list**. The class derives, line by line and interactively, the algorithms for **traversal (forward and backward)**, **insertion after the header (front)**, **insertion at the end**, and **insertion at the end of a circular DLL** (showing how the header's left link gives $O(1)$ access to the last node instead of $O(n)$). A concrete address-level example (header at 100, new node at 200, existing node at 300) is used to clear up confusion about what `NEW`, `NEW->RLINK` and `PTR->LLINK` actually store. The second half applies multi-linked lists to the **sparse matrix problem**: why triangular/diagonal array representations fail, the memory comparison between a dense array and a linked representation, the five-field node `(i, j, data, row link, column link)`, row headers / column headers / main header, and the resulting $O(n+n)=O(n)$ element-access cost versus $O(1)$ for an array. The lecture closes with an impromptu **introduction to asymptotic ($O$) notation** for a student new to it, plus detailed **exam format information**.

---

## 2. Topics Covered (in teaching order)

### 2.1 Real-life applications of linked lists (opening discussion)

- **Music playlist (e.g., Spotify) with next/previous:**
  - A *singly* linked list cannot go backward → you need a **doubly linked list** to support "previous song".
  - "Play in the order entered" behaviour = **queue** (FIFO). Point made: a **queue is an abstract data type (ADT)**; its *internal implementation* can be done with a linked list (doubly linked list was used as the example).
- **Insertion into a sorted list:**
  - Example given: sorted list `1 2 4 5 6 7 8`, insert `3` between `2` and `4`.
  - **Array:** you must locate the position, then shift every element after that position one slot to the right to free a space → expensive, $O(n)$ data movement.
  - **Linked list:** go to the position, create a node, re-link → **no shifting of elements**. This is the key advantage of a linked list over an array for insertion.
- **Polynomial representation:**
  - Example polynomials: $f_1(x) = a_5x^5 + a_3x^3 + a_1x + b$ and $f_2(x) = a_4x^4 + a_3x^3 + b_1x + c$.
  - **Node layout:** `[ coefficient | exponent | link ]` — one field for the coefficient $a_i$, one for the exponent (power), one link to the next term.
  - Operations such as **addition and multiplication of two polynomials** create new exponent/coefficient terms, which can simply be inserted as new nodes into a result list.
- **Memory management (free-list):**
  - A large memory block may have **non-contiguous free spaces**. You keep track of them by **linking each free block to the next free block** — i.e., a linked list of free regions. This is a standard OS/memory-manager use of linked lists.

---

### 2.2 Doubly linked list (DLL) — structure

- Each node maintains **two pointers**:
  - **Forward pointer** → drawn on the right, called **RLINK** (right link).
  - **Backward pointer** → drawn on the left, called **LLINK** (left link).
- **Node layout (pictorial):** `[ LLINK | DATA | RLINK ]`.
  - Note from instructor: the *declaration order* in code is arbitrary (`data, LLINK, RLINK` is fine); the left/right drawing is only a convention. What matters is that **one link stores the address of the previous node and the other the address of the next node**.
- **Header node:** a special node marking the start of the list.

**Diagram described (linear DLL with values 20, 30, 40):**

```
  +------+        +-----------+        +-----------+        +-----------+
  |HEADER| <----> | NULL?|20| | <----> |  |30|    | | <----> |  |40|NULL|
  +------+        +-----------+        +-----------+        +-----------+
```
- **Header:** its LLINK is `NULL` (nothing to its left), its RLINK points to the first node (20).
- **Node 20:** LLINK = address of HEADER, RLINK = address of node 30.
- **Node 30:** LLINK = address of node 20, RLINK = address of node 40.
- **Last node (40):** RLINK = `NULL`, LLINK = address of node 30.

**Why DLL:** in a singly linked list, once you are at a node you cannot go back. Many applications (playlist, undo/redo-style movement) need **both backward and forward movement**, hence two pointers per node.

---

### 2.3 Circular doubly linked list (CDLL)

- The **last node's RLINK points to the HEADER**, and the **HEADER's LLINK points to the last node**.
- Consequence: from *any* position (header or last node) you can move in **either direction** and wrap around.
- **Key practical benefit** (used later): the last node is reachable in **constant time** via `HEADER->LLINK` — no traversal needed.

---

### 2.4 Traversal in a DLL

The traversal algorithm is **structurally the same as for a singly linked list**; only the link name changes (`LINK` → `RLINK`), and you gain the ability to walk backward.

**Forward traversal**
```
1. PTR = HEADER->RLINK
2. while (PTR != NULL)
3.     process PTR->DATA
4.     PTR = PTR->RLINK
5. end while
```

**Backward traversal** (from any node, or from the last node)
```
1. PTR = <current node>            // e.g. the last node
2. while (PTR != NULL)             // or != HEADER, depending on convention
3.     process PTR->DATA
4.     PTR = PTR->LLINK
5. end while
```

- Only **one pointer** is needed for traversal (a student asked whether two are required — answer: no). The same `PTR` is reused; the direction is chosen by whether you assign `PTR = PTR->RLINK` or `PTR = PTR->LLINK`.
- **Termination condition:** `PTR != NULL` for a linear list. For a **circular** list the test becomes `PTR != HEADER` instead of `PTR != NULL`.
- **Complexity:** $O(n)$ time, $O(1)$ extra space.

---

### 2.5 Insertion **after the header** (at the front) in a DLL — derived in class

Goal: insert a new node between HEADER and the current first node (20).

```
0. NEW = GETNODE()                 // returns the ADDRESS of a newly created node
   NEW->DATA = item
1. PTR = HEADER->RLINK             // PTR now points at the old first node
2. NEW->RLINK = HEADER->RLINK      // new node points forward to old first node
3. NEW->LLINK = HEADER             // new node points backward to header
4. PTR->LLINK  = NEW               // old first node points backward to new node
5. HEADER->RLINK = NEW             // header points forward to new node
```

- Steps 4 and 5 can be written **without** the temporary pointer as
  `(HEADER->RLINK)->LLINK = NEW;` followed by `HEADER->RLINK = NEW;`
  but the **order matters** — you must fix the old first node's LLINK *before* overwriting `HEADER->RLINK`.
- The instructor recommended introducing `PTR = HEADER->RLINK` as an **initialization (step 0/1)** precisely to avoid the confusing double-dereference `(HEADER->RLINK)->LLINK`.
- **Four links are touched in total:** two outgoing from `NEW`, one in HEADER, one in the old first node.
- **Complexity:** $O(1)$.

#### Address-level worked example (clarifying what a pointer stores)

Confusion in class: *"why is it `PTR->LLINK = NEW` and not `PTR->LLINK = NEW->RLINK`?"*
Resolution: `NEW` **is** an address (the address of the new node); `PTR->LLINK` must hold the **address of the new node**, not the contents of one of its link fields.

Suppose:

| Object | Address |
|---|---|
| HEADER | 100 |
| NEW node | 200 |
| Node `20` (old first node, = PTR) | 300 |

After the insertion:

| Field | Value stored |
|---|---|
| `NEW->RLINK` | $300$ (address of node 20 / PTR) |
| `NEW->LLINK` | $100$ (address of HEADER) |
| `PTR->LLINK` (node 20's left link) | $200$ (address of NEW) |
| `HEADER->RLINK` | $200$ (address of NEW) |

---

### 2.6 Bug hunt: inserting into an **empty** doubly linked list

The instructor asked the class to find the line at which the above algorithm **breaks for an empty list**.

- An empty DLL is just `HEADER` with `HEADER->LLINK = NULL` and `HEADER->RLINK = NULL`.
- **Line 1** assigns `PTR = HEADER->RLINK`, so `PTR = NULL`.
- **Line 7 in the slide version** (the `PTR->LLINK = NEW` step) then **dereferences a NULL pointer** → run-time error.

**Correction required (flagged as the fix):**
```
1. PTR = HEADER->RLINK
2. if (PTR == NULL)                     // list is empty
3.     NEW->RLINK = NULL
4.     NEW->LLINK = HEADER
5.     HEADER->RLINK = NEW
6.     return
7. else
8.     ... normal 4-step insertion as above ...
```
- Important nuance stated: for an empty list you must **not** print "list is empty and stop" — insertion into an empty list is always legal; you simply need a **separate, slightly different branch** for it.

---

### 2.7 Insertion at the **end** of a (linear) DLL

```
1. PTR = HEADER                     // NOT HEADER->RLINK  (see note)
2. while (PTR->RLINK != NULL)
3.     PTR = PTR->RLINK
4. end while                        // PTR now points at the LAST node (e.g. 40)
5. NEW = GETNODE(); NEW->DATA = item
6. NEW->RLINK = PTR->RLINK          // = NULL
7. NEW->LLINK = PTR
8. PTR->RLINK = NEW
```

- **Why `PTR = HEADER` and not `PTR = HEADER->RLINK`:** the instructor stressed that if you start at `HEADER->RLINK` and use this loop form, on an empty list the loop breaks with `PTR` sitting on `NULL`, which is not what you want — you want `PTR` to end up on the **last real node**.
- Student question: *"what about the left link of NULL?"* — **Answer: `NULL` is not a node**; it is a single value with no `LLINK`/`RLINK` structure. You cannot and need not assign anything to it.
- Order note discussed in class: you may write `NEW->LLINK = PTR` before or after `PTR->RLINK = NEW`, because `PTR` itself is not being modified — it still points at the old last node either way.
- **Complexity:** $O(n)$ (dominated by the traversal to reach the end), $O(1)$ extra space.

---

### 2.8 Insertion at the end of a **circular** DLL — the $O(1)$ trick

Key insight: **you do not have to traverse at all.** The header's left link already holds the address of the last node.

```
1. PTR = HEADER->LLINK              // PTR = last node, in O(1)
2. NEW = GETNODE(); NEW->DATA = item
3. NEW->RLINK  = HEADER
4. NEW->LLINK  = PTR
5. PTR->RLINK  = NEW
6. HEADER->LLINK = NEW
```

- Explicitly stated in class: **"instead of $O(n)$ we reduce it to $O(1)$ — that's the advantage of the circular doubly linked list."**
- Also noted: in a circular list the traversal **terminating test** changes from `PTR != NULL` to *"has PTR come back to the header?"*, i.e. `PTR != HEADER`.
- General remark: **deletion, search and insertion at an arbitrary position** in a DLL follow exactly the same logic as in a singly linked list, except that you must additionally maintain the left links. These were **left for self-study** ("you have to study this one").

---

### 2.9 Sparse matrices with multi-linked lists

#### Motivation
- A **sparse matrix** = a matrix in which the **majority of elements are zero** and only a few (e.g. `a, b, c, d, …`) are non-zero, scattered at arbitrary positions.
- **Can the special array representations be reused?** (lower-triangular array, upper-triangular array, diagonal/band array, from an earlier lecture) — **No.** Those work only when the non-zero elements lie entirely on one side of the diagonal or hug the diagonal. A sparse matrix has non-zeros at arbitrary positions.

#### Memory comparison (worked numbers)
Assume a $10{,}000 \times 10{,}000$ matrix with only **100 non-zero elements**, each element occupying **8 bytes**, and each address/pointer also **8 bytes**.

- **Dense 2-D array:**
  $$10^4 \times 10^4 \times 8 = 10^8 \times 8 = 8\times10^8 \text{ bytes}$$
- **Actual useful data:** $100 \times 8 = 800$ bytes → almost all of the array is wasted.
- **Linked representation** (node = data + 2 addresses, as first sketched):
  $$8 \times 3 = 24 \text{ bytes per node}, \qquad 24 \times 100 = 2400 \text{ bytes total}$$
- Conclusion: the linked representation is **vastly more memory-efficient** *provided the matrix is genuinely sparse* (large dimensions, few non-zeros).

#### Trade-off (asked by a student)
- **Array advantage:** you can access element $(i,j)$ **directly by index in $O(1)$**.
- **Linked-list disadvantage:** there is no direct indexing; you must walk **row-wise or column-wise** to reach a given element.

#### The sparse-matrix node (5 fields)

```
+-------+-------+--------+-----------+--------------+
|   i   |   j   |  DATA  | ROW LINK  | COLUMN LINK  |
+-------+-------+--------+-----------+--------------+
```
- `i` — **row index** of the element
- `j` — **column index** of the element
- `DATA` — the actual value
- **ROW LINK** — address of the **next non-zero element in the same row**
- **COLUMN LINK** — address of the **next non-zero element in the same column**

**Worked example from the board** (rows and columns indexed from 1, matrix roughly $6\times7$):

| Element | `i` | `j` | ROW LINK | COLUMN LINK |
|---|---|---|---|---|
| `J` | 4 | 4 | address of node `L` (next element in row 4) | `NULL` (no further element in column 4) |
| `C` | 2 | 2 | address of `D` | reached *from* column header 2 |
| `D` | 2 | 4 | address of `E` | linked from column header 4 |
| `E` | 2 | 6 | in a **circular** design → back to `RH2`; otherwise `NULL` | next node in column 6 |

#### Row headers, column headers, main header

- Each **row** is itself a linked list → it needs a **row header** node `RH1, RH2, …`, using **the same 5-field structure**.
  - `i` = the row number (1 for `RH1`, 2 for `RH2`, …)
  - `j` = **0 / null** — this marks the node as a **header**: *"if either `i` or `j` is zero, that node is a header, because every real data node has a genuine index in both fields."*
  - `DATA` field of a header is reused to store the **number of non-zero elements present in that row** (e.g. `2` if that row has two non-zeros) — so an index lookup immediately tells you how many entries the row has.
  - **ROW LINK** → the **first non-zero node of that row**.
  - **COLUMN LINK** → the **next row header** (`RH1 → RH2 → RH3 → …`).
- Symmetrically, each **column** has a **column header** `CH1, CH2, …`, chained together, each pointing to the first non-zero node of its column.
- A **main header** node sits on top:
  - stores the **total number of rows and number of columns** of the matrix,
  - its **row link** → the first row header `RH1`,
  - its **column link** → the first column header `CH1`.

**Overall picture (described):** a grid-like mesh. Along the top runs the chain of column headers; down the left runs the chain of row headers; both chains hang off a single main header node. Every non-zero element sits at the intersection of its row chain and its column chain, threaded horizontally by ROW LINK and vertically by COLUMN LINK. If the design is made circular, the last node of a row links back to its row header, and the last node of a column links back to its column header.

#### Insertion of a new element $X$ at position $(i,j)$
1. Walk down the **row-header chain** (via column links) to reach row header `RH_i`.
2. Walk along the **column-header chain** to reach column header `CH_j`.
3. From `RH_i`, follow **row links** to find the correct horizontal position (the node whose `j` is just less than the new `j`).
4. From `CH_j`, follow **column links** to find the correct vertical position.
5. Create the node with `(i, j, data)` and splice it into **both** the row chain and the column chain (four link updates, analogous to a DLL insertion but in two dimensions).

#### Complexity of element access in this representation
- Worst case: to reach element $(n,n)$ you traverse at most $n$ steps down the headers and $n$ steps along the chain:
  $$T(n) = O(n + n) = O(2n) = O(n)$$
- Contrast: an array gives element $(i,j)$ in $O(1)$ / constant time.
- Motivation stated for this design: **avoid $O(n^2)$** work (scanning all $n \times n$ positions) — the header structure brings it down to $O(n)$.

#### Student question: a linked list with **four** pointers?
- Asked: can we have a node with pointers in all four directions (left, right, up, down) so we can traverse backwards along a row and upwards along a column?
- **Answer:** Yes. As described above, the sparse-matrix node is effectively a *singly* linked structure in two dimensions (you can only move right along a row and down a column). To move backwards/upwards you need **four links**, named e.g. `forward row link`, `backward row link`, `downward column link`, `upward column link`.
- **Caveat given:** managing four pointers correctly becomes "a nightmare" — only do it if the application genuinely needs it.
- **Sudoku example:** since a Sudoku grid ends up with a value in **every** cell, it is *not* sparse → use a **plain 2-D array**, not a linked representation.
- The linked sparse representation is appropriate when you have a **genuinely sparse matrix** and mostly perform matrix operations / analyses (e.g. **SVD — singular value decomposition**) with **little insertion of new elements in between**.

---

### 2.10 Impromptu primer on asymptotic ($O$) notation

Given in response to a student unfamiliar with Big-O.

**Constant time $O(1)$**
- Example: a **sorted** array $a_1, a_2, \dots, a_n$ (say $n=10$).
  - Minimum = $a_1$; maximum = $a_n$. Both are found by direct access.
- Now **double the input** to $2n$ (20 elements), still sorted. Do you need to look at more elements to find min/max? **No.**
- Therefore the cost **does not depend on $n$** → *constant time*.
- Notation: strictly this is $O(c)$ for some constant $c$, but **we always write $O(1)$**. Even if the operation performs 4 or 5 fixed steps, it is still $O(1)$ because the count does not grow with $n$.
- Linked-list example: **inserting at the front of a singly linked list** performs a fixed 4–5 operations regardless of list length → $O(1)$.

**Linear time $O(n)$**
- Example: finding the **maximum in an *unsorted* array**. You must compare every element; the maximum may be the last one, so you cannot stop early.
  - 10 elements → 10 comparisons; 1000 elements → 1000 comparisons → cost depends directly on input size $n$.
- If the algorithm actually performs $2n$ comparisons plus a constant, it is **still $O(n)$**: constant multipliers are dropped.
  $$2n + c \in O(n)$$

**Dominant-term rule**
- If an algorithm costs $n^2$ operations for one part, $n$ for another, and some constants:
  $$T(n) = an^2 + bn + c \;\Rightarrow\; T(n) = O(n^2)$$
- Reason given: **we take the highest-order term** because it dominates; $n^2 \ge n$ (for $n$ greater than some threshold $n_0$).
- $O$ is described as an **upper bound** — "the maximum number of comparisons that would be required."
- The **formal mathematical definition** (with constants $c$ and $n_0$) was deliberately deferred: *"those mathematical formulations will be taught by Professor Surya"* — the instructor wanted students habituated to the intuition first.

**Applied back to the sparse matrix:** reaching the last element requires $n$ steps in one direction plus $n$ in the other → $O(n+n) = O(2n) = O(n)$.

---

## 3. Formula / Complexity Sheet

| Operation | Structure | Time | Notes |
|---|---|---|---|
| Traversal (forward or backward) | DLL | $O(n)$ | one pointer; `PTR = PTR->RLINK` or `PTR = PTR->LLINK` |
| Insert after header (front) | DLL | $O(1)$ | 4 link updates |
| Insert at end | Linear DLL | $O(n)$ | must traverse to last node |
| Insert at end | **Circular** DLL | $O(1)$ | reach last node via `HEADER->LLINK` |
| Insert front | Singly linked list | $O(1)$ | fixed number of steps |
| Find max in sorted array | Array | $O(1)$ | $a_n$ |
| Find max in unsorted array | Array | $O(n)$ | must scan all |
| Access element $(i,j)$ | 2-D array | $O(1)$ | direct indexing |
| Access element $(i,j)$ | Linked sparse matrix | $O(n+n)=O(n)$ | walk headers + chain |

**Memory formulas used**

- Dense array storage: $\text{rows} \times \text{cols} \times \text{bytes per element}$; e.g. $10^4 \times 10^4 \times 8 = 8\times 10^8$ bytes.
- Linked node (data + 2 pointers, 8 bytes each): $8 \times 3 = 24$ bytes; total for $k$ non-zeros $= 24k$; e.g. $24 \times 100 = 2400$ bytes.
- Useful data only: $100 \times 8 = 800$ bytes.

**Asymptotic rules stated**

- $O(c) \equiv O(1)$
- $2n + c \in O(n)$
- $an^2 + bn + c \in O(n^2)$ (keep the highest-order term, drop constants)
- $O(\cdot)$ = **upper bound**, valid for $n > n_0$

**Indexing / addressing formulas (referenced, not re-derived this session)**
The instructor referred back to earlier lectures on **row-major vs column-major addressing** and on **lower-triangular, upper-triangular and diagonal (band) array** representations, and confirmed these formulas **will be examined** ("mathematical calculation questions like indexing calculation — I have shown a lot of formulas, you have to use those formulas to calculate some index value"). Revise those from the earlier slide decks; they were not restated here.

---

## 4. Exam / Assignment Information (explicitly flagged)

**Assignments**
- The circular-linked-list homework questions shared earlier **do need to be submitted** — a submission link (like the one for Assignment 1) will be created on the **LMS portal** for **Assignment 2**.
- No hard one-week deadline; ample time will be given and deadlines may be extended, **but everything must be submitted before the exam**.
- **Self-study items from this lecture:** deletion in a DLL, search/insertion at arbitrary positions in a DLL, and the full sparse-matrix problem ("I'm not going to discuss it — you have to study this one").
- Slides for this session will be posted on the **LMS portal**.

**Exam format (online)**
- Question types:
  1. **MCQ** and **true/false** questions.
  2. **Mathematical calculation** questions — especially **indexing/address calculations** using the formulas taught (row-major/column-major, triangular/diagonal arrays).
  3. **Fill-in-the-algorithm**: an algorithm will be given with **missing steps**, and you must supply them — delivered as **drag-and-drop** (not MCQ; you drag the correct statements into the blanks). These are also the "long answer" questions.
- The exam is split into **2–3 parts / slots**, approximately: MCQ part ~10–15 min, short-answer part ~20 min, long-answer part ~30–40 min, with a **5-minute break between slots**.
- Questions appear **sequentially and you cannot go back** to a previous question ("just like a singly linked list") — this is an anti-cheating measure.
- **Randomization:** each student gets the same logical questions but with **different numeric values**, and question order may differ. Answers are auto-checked; **a single wrong value gives zero** for that question.
- **Open-slide policy (online exam):** you *may* download and use the lecture slides during the online exam.
- **Offline exams:** slides will **not** be available; you are expected to **know the procedure / be able to derive** the formulas rather than rote-memorize everything, and **extra time will be given** for derivation.

**Course logistics**
- The **next five lectures** will be taken by **Professor Surya**, who will cover **complexity analysis / asymptotic notation formally**.
- Doubts by email, or via the **class representatives (CRs)** on WhatsApp; when messaging, state your **name** and **"MSDS DSM-103"** so the instructor recognizes the number.

**Language note for writing algorithms**
- No specific programming language is mandated. The pseudocode uses C-like `if/else` and the **arrow operator (`->`)** purely to denote "follow this link". You may translate it into any language (`.` notation, asterisks/dereferencing, etc.).