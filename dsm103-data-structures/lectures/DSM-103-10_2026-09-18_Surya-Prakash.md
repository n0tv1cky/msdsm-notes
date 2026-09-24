# DSM-103 Data Structures — Session 10 (2026-09-18, Instructor: Surya Prakash)
## Topic: The Queue Data Structure (Array Implementation)

---

## 1. Overview

This session introduces the **queue** as a new linear data structure, positioned against the array, linked list and stack studied in earlier classes. The instructor first recaps the two questions that must always be answered for any data structure — *how is the data stored in memory* and *how is it manipulated (insert / delete / update)* — and shows that array → linked list → stack → queue is a progression of increasing **restriction** on where manipulation may occur. The queue is defined as a linear collection where elements are **added at one end (rear/tail)** and **removed from the other end (front/head)**, giving **FIFO (First In, First Out)** behaviour, in contrast to the stack's **LIFO (Last In, First Out)**. Real-world and computing applications are discussed (toll booths, bank queues, printers, email servers, multi-user/resource-sharing systems). The bulk of the class is the **array-based implementation**: an array `Q[1..N]` with two index variables `FRONT` and `REAR`, the conventions for empty/full/non-empty states, and full pseudocode for `ENQUEUE_ARRAY` and `DEQUEUE_ARRAY`, including the special cases of inserting the *first* element and deleting the *last* element. A full worked trace of 10 operations on a size-10 queue exposes the key drawback of this naive implementation — the queue is falsely reported "full" while free space remains at the front. Three remedies are outlined: (a) modify ENQUEUE to do compaction, (b) modify DEQUEUE to shift left after every deletion, (c) treat the queue as a **circular queue** using the mod operator — the last of which is deferred to the next class.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Recap — what we ask of every data structure
Two standard questions for any data structure:
1. **How is the data stored in memory?** (linear vs non-linear arrangement)
2. **How is the data manipulated?** (insertion, deletion, updation — and *where* they are allowed)

Data structures covered so far, all **linear** (items placed one after another):
- **Array** — insertion, deletion and updation possible at **any** position. "Complete freedom."
- **Linked list** — insertion, deletion and updation possible at **any** position. Complete freedom.
- **Stack** — linear, so it has two ends, but manipulation is **restricted to one end only**; nothing can be done at the other end.
  - Insert operation = **PUSH**; delete operation = **POP**.
  - Discipline: **LIFO** (Last In, First Out).

Key framing idea stated by the instructor: *moving from array → stack → queue, we progressively impose restrictions on how the stored data may be manipulated.*

### 2.2 Definition of a Queue
- A **queue** is a collection whose elements are **added at one end and removed from the other end**.
- It is a **linear** data structure ⇒ it has exactly two ends.
- **Rear / tail** end → insertions happen here.
- **Front / head** end → deletions happen here.
- Operation names:
  - **ENQUEUE** (often written `INQ` / `ENQ` in the transcript) — insert at rear. **Takes a value as input.**
  - **DEQUEUE** (`DQ`) — remove from front. **Takes no value as input** (it always removes whatever is at the front) — exactly analogous to `POP` in a stack needing no argument, while `PUSH` does.
- Discipline: **FIFO — First In, First Out.** The item that entered first is removed first.
  - Contrast: **Stack = LIFO**, **Queue = FIFO**.
- **No update operation exists for a queue.** You may only add at the rear or remove from the front — you may *not* reach into the middle and change a value. (Arrays and linked lists do allow this; queues deliberately do not.)

**Visual (described):** Picture a horizontal row of boxes. The leftmost occupied box is the FRONT; the rightmost occupied box is the REAR. An arrow labelled "ENQUEUE" points **into** the right side (after REAR); an arrow labelled "DEQUEUE" points **out of** the left side (at FRONT). Contrast with the stack diagram, where both PUSH and POP arrows attach to the **same** end.

### 2.3 Applications of Queues
Real life:
- Toll booth / toll plaza lanes
- Bank counters (person who arrives first is served first)
- Grocery store checkout / billing counter
- Traffic control
- Assembly line in manufacturing (object moves along, components added in order)

Computing:
- **Email delivery** — a mail server with many outgoing requests queues the mails and sends them in arrival order.
- **Multi-user environment / server** — many users' requests to one machine are queued; *arrival time* determines position in the queue, and processes are served in that order.
- **Resource sharing in a computer centre**, e.g.:
  - **Printer spooling** (raised by a student and confirmed by the instructor) — print requests from many users are queued and served first-come-first-served.
  - **Memory / I/O access** in threading and multiprocessing — a memory location or I/O device accessible by multiple processes; access requests are queued (student contribution).
  - **Disk access** — multiple users reading from disk are ordered by a queue.

Instructor's point: in these applications you **do not want** the complete freedom of an array or the single-end restriction of a stack; you want the restricted, order-preserving discipline of a queue.

---

## 3. Array Implementation of a Queue

### 3.1 Storage model and conventions
- Underlying storage: an **array named `Q`**.
- **Size = N** (capital N).
- **Indices run from 1 to N** (note: for the stack, the class had used 0-based indexing starting at 0).
  - `Q[1]` = first cell, `Q[2]` = second cell, …, `Q[N]` = last cell.
- **Two index variables (pointers) are maintained:**
  - **`FRONT`** — holds the **index of the element at the front** (the one that will be deleted next).
  - **`REAR`** — holds the **index of the last element** currently in the queue (the new element goes at `REAR + 1`).
- **Why two pointers?** In a stack only **`TOP`** was needed because both PUSH and POP act at the same end. In a queue, insertion and deletion act at *different* ends, so both ends must be tracked.

**Visual (described):** A row of N boxes numbered 1 … N. A block of consecutive occupied boxes sits somewhere inside. An arrow labelled FRONT points at the leftmost occupied box; an arrow labelled REAR points at the rightmost occupied box. Boxes to the left of FRONT are *freed* (already dequeued); boxes to the right of REAR are *unused*. Both pointers only ever move **left → right** in this naive scheme.

### 3.2 State conditions (write these out exactly)

| State | Condition |
|---|---|
| **Empty queue** | `FRONT = 0` **and** `REAR = 0` |
| **Full queue (simple/naive test)** | `REAR = N` |
| **Full queue (true test, when compaction is used)** | `FRONT = 1` **and** `REAR = N` |
| **Queue contains elements** | `1 ≤ FRONT ≤ REAR ≤ N` , i.e. `FRONT ≤ REAR` |
| **Exactly one element** | `FRONT = REAR` |

- **Why 0 marks "empty":** valid indices are 1 … N, so `0` is an *impossible* index and can safely be used as a sentinel meaning "points to nothing." (Analogy: in the stack implementation, where indices started at 0, `TOP = −1` was used as the empty sentinel — one step back from the first valid index. Same idea, shifted.)
- **Caution on "full":** testing only `REAR = N` can wrongly declare the queue full while cells 1 … FRONT−1 are free. Testing `FRONT = 1 AND REAR = N` is the logically correct fullness test, but it is only meaningful if the implementation performs **compaction** (shifting elements left to fill vacated front cells).

### 3.3 Number of elements in the queue — formula

```
Number of elements = REAR − FRONT + 1
```

**Worked example given:** if `FRONT = 5` and `REAR = 10`, the count is `10 − 5 + 1 = 6` elements.

*(Note: the instructor flagged that `FRONT ≤ REAR` and this count formula hold only for the flat/linear queue. For a **circular queue** they will **not** hold — to be covered next class.)*

---

## 4. Algorithm: ENQUEUE (insertion) — `ENQUEUE_ARRAY`

Name convention explained: the algorithm is called `ENQUEUE_ARRAY` (suffix `_ARRAY`) because this particular implementation is array-based; a linked-list version would be named differently.

### Logic
1. Check whether the queue is **full**. If full → overflow, no insertion.
2. If not full, check whether this is the **first element** being inserted (queue currently empty). If so, `FRONT` must be moved from 0 to 1 as well — because normally ENQUEUE only touches `REAR`.
3. Otherwise, just advance `REAR` and store the item.

### Pseudocode
```
ENQUEUE_ARRAY(Q, N, FRONT, REAR, ITEM)

1.  IF REAR = N THEN
        PRINT "Queue is FULL (overflow)"
        EXIT
2.  IF FRONT = 0 AND REAR = 0 THEN      // queue is empty -> inserting the FIRST element
        FRONT ← 1
3.  REAR ← REAR + 1
4.  Q[REAR] ← ITEM
5.  EXIT
```

### Notes stressed in class
- **In the normal course, ENQUEUE manipulates only `REAR`.** The `FRONT ← 1` line in step 2 is the *special case* that runs only for the very first insertion into an empty queue.
- The instructor explicitly walked through "delete step 2 and see what's left": the core algorithm is just *"if full → reject; else increment REAR and place the item."* Step 2 is then bolted on for the empty-queue case.
- Frequency of paths: step 3–4 runs most of the time; step 1's error path runs only when full; step 2 runs only on the first insertion.
- **Complexity (not stated explicitly in the lecture, but implied):** O(1) time, O(1) extra space. If the compaction variant (§7.1) is used, the worst case becomes O(N).

---

## 5. Algorithm: DEQUEUE (deletion) — `DEQUEUE_ARRAY`

### Logic
1. Check whether the queue is **empty**. If empty → underflow, no deletion.
2. Fetch the item at `FRONT` into `ITEM` (this is what is returned/removed).
3. Check whether the element just removed was the **last remaining element** (`FRONT = REAR`). If yes, reset **both** pointers to 0 (queue becomes empty). Otherwise, just advance `FRONT`.

### Pseudocode
```
DEQUEUE_ARRAY(Q, N, FRONT, REAR)

1.  IF FRONT = 0 THEN                  // (equivalently FRONT = 0 AND REAR = 0)
        PRINT "Queue is EMPTY (underflow), no deletion possible"
        EXIT
2.  ITEM ← Q[FRONT]
3.  IF FRONT = REAR THEN               // the last element is being deleted
        FRONT ← 0
        REAR  ← 0
    ELSE
        FRONT ← FRONT + 1
4.  RETURN ITEM
```

### Notes stressed in class
- **In the normal course, DEQUEUE manipulates only `FRONT`** (`FRONT ← FRONT + 1`).
- **The one case where DEQUEUE must also change `REAR`** is when the **last element** is deleted — the empty state is represented by `FRONT = 0, REAR = 0`, so `REAR` must be explicitly reset to 0.
- **How do you detect "this is the last element"?** When `FRONT = REAR` — both pointers indicate the same cell, so exactly one item remains. (Instructor derived this by repeatedly deleting from a block of elements until FRONT climbed up to meet REAR.)
- **Complexity (not stated explicitly):** O(1) time, O(1) extra space; the shift-left variant (§7.2) becomes O(N) per deletion.

---

## 6. Worked Example — full trace

**Initial configuration**
- Array `Q` of size **N = 10**, indices 1…10.
- Two elements present: `Q[8] = 23`, `Q[9] = 21`.
- Therefore `FRONT = 8`, `REAR = 9`. Cells 1–7 and 10 are free.

**Operation sequence:** `DQ, NQ(24), NQ(27), DQ, DQ, DQ, NQ(22), NQ(28), DQ, DQ`

| # | Operation | What happens | FRONT | REAR | Queue contents |
|---|---|---|---|---|---|
| 0 | *(initial)* | — | 8 | 9 | Q[8]=23, Q[9]=21 |
| 1 | `DEQUEUE` | FRONT(8) ≠ REAR(9); remove `23`; FRONT ← 9 | 9 | 9 | Q[9]=21 |
| 2 | `ENQUEUE(24)` | REAR(9) ≠ N; REAR ← 10; `Q[10] = 24` | 9 | 10 | 21, 24 |
| 3 | `ENQUEUE(27)` | **REAR = 10 = N ⇒ "QUEUE IS FULL"** — insertion rejected (even though cells 1–8 are free!) | 9 | 10 | 21, 24 |
| 4 | `DEQUEUE` | FRONT(9) ≠ REAR(10); remove `21`; FRONT ← 10 | 10 | 10 | Q[10]=24 |
| 5 | `DEQUEUE` | FRONT = REAR = 10 ⇒ last element; remove `24`; **FRONT ← 0, REAR ← 0** | 0 | 0 | empty |
| 6 | `DEQUEUE` | FRONT = 0 ⇒ **"QUEUE IS EMPTY"**, no deletion | 0 | 0 | empty |
| 7 | `ENQUEUE(22)` | Queue empty ⇒ first element: FRONT ← 1, REAR ← 1, `Q[1] = 22` | 1 | 1 | 22 |
| 8 | `ENQUEUE(28)` | REAR ← 2, `Q[2] = 28` | 1 | 2 | 22, 28 |
| 9 | `DEQUEUE` | remove `22`; FRONT ← 2 | 2 | 2 | Q[2]=28 |
| 10 | `DEQUEUE` | FRONT = REAR = 2 ⇒ last element; remove `28`; **FRONT ← 0, REAR ← 0** | 0 | 0 | empty |

### The critical observation from this trace
At **step 3**, `ENQUEUE(27)` was refused with "Queue is full" even though **8 of the 10 cells were free** (cells 1–8). Because `REAR` and `FRONT` only ever move rightwards and the vacated front cells are never reused, this naive array queue **under-utilises memory**. This is the central drawback motivating the rest of the lecture.

---

## 7. Three Solutions to the "false full / wasted space" Problem

### 7.1 Solution 1 — Modify ENQUEUE (compaction on "full")
- Do not declare the queue full merely because `REAR = N`.
- The **true full condition is `REAR = N AND FRONT = 1`.**
- Revised behaviour: when `REAR = N`, test `FRONT`:
  - If `FRONT = 1` → genuinely full → overflow.
  - If `FRONT > 1` → **compaction**: shift *all* elements left so that the first element lands at index 1, update `FRONT` and `REAR` accordingly, thereby freeing cells at the tail end; then insert the new item.

Sketch of the revised algorithm:
```
ENQUEUE_ARRAY_WITH_COMPACTION(Q, N, FRONT, REAR, ITEM)
1. IF REAR = N THEN
       IF FRONT = 1 THEN  PRINT "Queue FULL"; EXIT
       ELSE
           shift Q[FRONT..REAR] left so that it starts at index 1
           REAR  ← REAR − FRONT + 1
           FRONT ← 1
2. IF FRONT = 0 AND REAR = 0 THEN FRONT ← 1
3. REAR ← REAR + 1
4. Q[REAR] ← ITEM
```
Cost: the shift is O(N) when it occurs.

### 7.2 Solution 2 — Modify DEQUEUE (shift left after every deletion)
- After **every** deletion, shift all remaining elements one position to the **left**, so there is **never** any free space at the beginning of the array.
- Then `FRONT` always equals 1 for a non-empty queue, and the **simple test `REAR = N` becomes a genuinely correct fullness test.**

Sketch:
```
DEQUEUE_ARRAY_WITH_SHIFT(Q, N, FRONT, REAR)
1. IF FRONT = 0 THEN PRINT "Queue EMPTY"; EXIT
2. ITEM ← Q[1]                          // FRONT is always 1 here
3. IF FRONT = REAR THEN FRONT ← 0; REAR ← 0
   ELSE
       FOR i = 1 TO REAR − 1:  Q[i] ← Q[i+1]
       REAR ← REAR − 1        // FRONT stays 1
4. RETURN ITEM
```
**Visual (described):** boxes `[ 21 | 24 | _ | _ ]` → delete 21 → instead of leaving `[ _ | 24 | _ | _ ]`, every remaining element slides one cell left giving `[ 24 | _ | _ | _ ]`.
Cost: O(N) per deletion.

### 7.3 Solution 3 — Circular Queue (preview; detailed next class)
- Instead of a flat linear strip that "ends" at index N, the array is treated **logically as a circle**: the cell after index N is index 1. "Like a circle, there is no end — you keep moving."
- So when `REAR = N` and cell 1 is free, `REAR` wraps around to 1, then to 2, etc., reusing the freed front cells. `REAR` therefore never gets stuck at the end.
- **Empty condition is still `FRONT = 0` and `REAR = 0`**; a non-empty circular queue has `FRONT` and `REAR` somewhere in 1 … N.
- **Important:** in a circular queue the relation `FRONT ≤ REAR` **no longer holds** (nor does the simple `REAR − FRONT + 1` count formula) — `FRONT` may be to the *right* of `REAR`.
- **Pointer advancement uses the MOD operator**, so that after N the index automatically comes back to 1. (The exact wrap-around formula, e.g. `REAR ← (REAR MOD N) + 1`, and the corresponding full/empty tests, will be developed in the next session.)

**Visual (described):** the N array cells drawn around the circumference of a circle; index N sits immediately counter-clockwise/adjacent to index 1, so a pointer sweeping clockwise passes … N−1, N, 1, 2, … indefinitely.

---

## 8. Comparison Table (Stack vs Queue) — useful for revision

| | Stack | Queue |
|---|---|---|
| Arrangement | Linear | Linear |
| Insert at | one end (TOP) | **REAR** |
| Delete from | **same** end (TOP) | **FRONT** (opposite end) |
| Discipline | **LIFO** | **FIFO** |
| Operation names | PUSH / POP | ENQUEUE / DEQUEUE |
| Pointers maintained | 1 (`TOP`) | 2 (`FRONT`, `REAR`) |
| Empty sentinel (as used in class) | `TOP = −1` (0-based array) | `FRONT = REAR = 0` (1-based array) |
| Update operation | not used | **does not exist** |
| Argument needed | PUSH needs a value; POP does not | ENQUEUE needs a value; DEQUEUE does not |

---

## 9. Additional / Auxiliary Operations Mentioned
Besides ENQUEUE and DEQUEUE (the two primary operations):
- **`isEmpty()`** — check whether the queue is empty (`FRONT = 0`).
- **`isFull()`** — check whether the queue is full (`REAR = N`, or `FRONT = 1 AND REAR = N`).
- **`status()`** — reports how many elements are currently in the queue / how much space is occupied vs free (uses `REAR − FRONT + 1`).

**Two implementation routes for a queue** (same as for a stack):
1. **Using an array** (covered in detail this session).
2. **Using a linked list** (mentioned, not covered here).
Instructor's remark: fundamentally, to store multiple items you need an array or a linked list; a queue is that storage **plus additional restrictions** on where insertion and deletion may occur.

---

## 10. Flagged as Important / For Exams & Assignments

The instructor did not announce a formal exam or assignment item in this session, but the following were explicitly emphasised as the points to know:

- **Memorise the state conditions:** empty ⇒ `FRONT = REAR = 0`; full (naive) ⇒ `REAR = N`; full (true) ⇒ `FRONT = 1 AND REAR = N`; non-empty ⇒ `FRONT ≤ REAR`; single element ⇒ `FRONT = REAR`.
- **The count formula `REAR − FRONT + 1`** (verified with the 5→10 = 6 elements example).
- **The two special cases** you must handle correctly, and which are the most common exam trap:
  - ENQUEUE into an **empty** queue ⇒ must set `FRONT = 1` as well as `REAR`.
  - DEQUEUE of the **last** element (`FRONT = REAR`) ⇒ must reset **both** `FRONT ← 0` and `REAR ← 0`.
- **Be able to trace an operation sequence** on a fixed-size array queue exactly as in the §6 example, recording FRONT and REAR after every operation.
- **Be able to state the drawback** of the naive linear array queue (false "queue full" / wasted front cells) **and the three remedies** (modify ENQUEUE with compaction, modify DEQUEUE with left-shift, or use a circular queue).
- **Remember that `FRONT ≤ REAR` and the simple count formula break down for circular queues** — this was called out twice.

**Next session:** detailed treatment of the **circular queue**, including the **MOD-based pointer update** and its empty/full conditions.