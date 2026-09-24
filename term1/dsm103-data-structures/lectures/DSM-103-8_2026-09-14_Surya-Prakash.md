# DSM-103 — Data Structures

## Session 8 · 2026-09-14 · Instructor: Surya Prakash

## Topic: The Stack Data Structure (Introduction, Representations, Push/Pop)

---

## 1. Overview

This session introduces the **stack** as an abstract, linear data structure, building on the two previously covered structures (**array** and **linked list**). The instructor first lays out a general framework for thinking about *any* data structure — (i) what data is stored, (ii) how it is arranged (linear vs. non-linear), and (iii) how it is manipulated (insert / delete / update) — and stresses that it is the **manipulation rules** that primarily distinguish one data structure from another. A stack is then defined as an *ordered collection of homogeneous data elements* in which **insertion and deletion are restricted to one end only**. Real-world analogies (stack of trays, stacked chairs) and computing applications (undo/redo, expression evaluation, infix→postfix conversion, parenthesis matching, string reversal, function-call handling, backtracking, syntax parsing) are given. The bulk of the lecture develops the two implementations — **array-based** and **linked-list-based** — with the `top` pointer/index, and gives algorithms for **push**, **pop**, and **status** in both. The session closes with a note that expression evaluation via stacks (infix / prefix / postfix) will be covered next class.

**Course logistics mentioned:** Surya Prakash takes the next five classes; Prof. Somnath then resumes for a few topics; Surya Prakash returns toward the end of the course. Reference textbook shown on the last slide (the same one previously recommended) — algorithms in the slides are taken from it.

---

## 2. Topics and Concepts, in Order Taught

### 2.1 General framework: what defines a data structure

Three things must be defined/considered when designing **any** data structure:

1. **What data is stored** — the set of elements/items: integer, floating-point, character, text/string, etc.
2. **How the data is stored** — the arrangement:
   - **Linear**: items come one after another in a sequence; for every item you can say who is *before* it and who is *after* it. Examples: **array**, **linked list**.
   - **Non-linear**: no before/after ordering; relationships are of a different kind. Example: **tree** — described as a structure with **parent–child relationships**, where for a given node you speak of its *parent* and its *children*, not its predecessor/successor. (Trees not yet covered in the course.)
3. **How the data is manipulated** — the permitted operations: **insertion**, **deletion**, **update** (and whether update is even permitted).

> **Key point (emphasized):** Point (3) — the manipulation rules — is what *primarily differentiates* one data structure from another. All data structures store data; the restrictions on how you insert/delete/update are what make a stack a stack rather than just an array.

### 2.2 Motivation: why a stack when we already have arrays and linked lists?

- In an **array** or **linked list** you have **complete freedom**: you may insert at any position and delete any element.
  - Example given: an array of size 4, entirely empty; you are free to place your element at, say, the 20th position of a 100-element array, or at the end of a 4-element array — no restriction.
- In many applications we **do not want** that freedom; we deliberately impose **restrictions**. The stack is the structure obtained by imposing the restriction "insert/delete at one end only."

### 2.3 Definition of a stack

> **Stack** = an **ordered collection of homogeneous data elements**, in which **insertion and deletion take place at one end only**.

- **Ordered collection** → there is an order among elements: you can identify the first, second, third element, and for any element who is before it and who is after it. Hence a **linear** data structure.
- **Homogeneous** → all elements are of the *same* type. A stack of integers holds only integers; a stack of characters holds only characters. You cannot mix, e.g., integers and text in the same stack.
- **One-end restriction** → both insertion and deletion happen at the *same single* end. You cannot insert into the middle.

### 2.4 Real-life analogies

- **Stack of trays**: a new tray must be placed *on top*; a tray can only be removed from the *top*. To insert a tray in the middle you would first have to remove the top three trays, insert, then replace them — i.e., direct middle insertion is *not allowed*.
- **Stacked chairs** — same behaviour.

### 2.5 Applications of stacks in computer science

- **Undo / Redo** features in editors (MS Office, Photoshop).
- **Evaluation of arithmetic expressions** (e.g. $a+b$, $a-b$, $a \times b + c / d$).
- **Conversion of infix notation to postfix notation** (required before machine evaluation).
- **Parenthesis matching** — checking that the number of opening and closing brackets is equal *and* that their order/nesting is valid.
- **String reversal**.
- **Function calls / nested function calls** — e.g. $f_1$ calls $f_2$, $f_2$ calls $f_3$, $f_3$ calls $f_4$, …; implementing these nested calls requires a stack.
- **Backtracking**.
- **Syntax parsing**.

### 2.6 Notations for arithmetic expressions (preview of next class)

Every arithmetic expression has **operators** and **operands**. In $a + b$: $a$ and $b$ are **operands**, $+$ is the **operator**. Three notations, classified by **where the operator is placed**:

| Notation | Form | Example |
|---|---|---|
| **Infix** | operand, operator, operand (operator *between* operands) | $a + b$ |
| **Prefix** | operator first, then operand1, then operand2 | $+\,a\,b$ |
| **Postfix** | operand1, operand2, then operator | $a\,b\,+$ |

- We *write* programs in **infix**, but internally the computer must convert to **postfix** to evaluate.
- **Both** the infix→postfix conversion **and** the postfix evaluation use a **stack**. (Detailed algorithms deferred to the next session.)

---

## 3. Representation 1 — Array-Based Stack

### 3.1 Structure and the `top` index

- The data items are physically stored in an **array**, e.g. $a[\,]$, with valid indices running from a lower bound $L$ to an upper bound $U$.
- **Diagram described:** picture a horizontal row of array cells. The first item, `item1`, goes into the leftmost cell (index $L$); `item2` into the next; `item3` next; and so on — items fill up in one direction only. Alternatively, picture the same structure vertically as a **bucket / open container**: elements pile up from the bottom, and the open mouth is the single end used for both insertion and removal. Under the vertical picture the bottom cell is $L$, the next is $L+1$, and so on.
- A separate variable, the **`top` pointer / `top` index**, is maintained alongside the array. `top` holds the **index of the last (topmost) element currently in the stack** — the element after which a new element will be inserted.
- To insert: compute `top + 1`, store the new item at that index, and update `top`.
- To delete: take the item at index `top`, then decrement `top`.

### 3.2 Status conditions (array version)

Given index range $L \ldots U$:

$$\text{Stack is EMPTY} \iff \text{top} < L$$

$$\text{Stack is FULL} \iff \text{top} \ge U$$

Valid data items occupy indices between $L$ and $U$ inclusive.

### 3.3 Algorithm: PUSH (array implementation)

Insert `item` into array `a` with index range $L \ldots U$ and index variable `top`.

```
PUSH(a, top, item):
1. if top >= U then
2.       print "Stack is FULL — no more elements can be pushed"
3.       exit / return overflow
4. else
5.       top <- top + 1          // move to next free location
6.       a[top] <- item          // store the item there
7. endif
8. Stop
```

Steps in words, as given in the lecture:
1. Check whether the stack is full (e.g. a 100-element stack already holding 100 elements → report "stack full", push fails).
2. If not full, **increment `top` by 1**.
3. Store `item` at index `top` of the array `a`.

### 3.4 Algorithm: POP (array implementation)

Remove and return the topmost element.

```
POP(a, top):
1. if top < L then
2.       print "Stack is EMPTY — nothing to delete"
3.       exit / return underflow
4. else
5.       item <- a[top]          // fetch the element pointed to by top
6.       top  <- top - 1         // next deletion will be at top-1
7.       return item
8. endif
9. Stop
```

Steps in words:
1. Check whether the stack is empty ($\text{top} < L$). If empty, deletion is impossible.
2. Otherwise fetch the item in array `a` at index `top`; this is the value returned by the pop.
3. **Decrement `top` by 1**.

> Symmetry noted in lecture: **push increases `top`, pop decreases `top`.**

### 3.5 Algorithm: STATUS (array implementation)

Reports how full / empty the stack is.

```
STATUS(a, top, size):
1. if top < L then
2.       print "Stack is EMPTY"
3. else if top >= U then
4.       print "Stack is FULL"
5. else
6.       freeSpacePercent <- ((size - top) / size) * 100
7.       print freeSpacePercent
8. endif
```

**Free-space formula (written out exactly as explained):**

$$\text{Free space (\%)} = \frac{\text{size} - \text{top}}{\text{size}} \times 100$$

where `size` = total number of elements the array can hold, and `top` = index of the current topmost element. $(\text{size} - \text{top})$ gives the number of free slots; dividing by `size` gives a fraction; multiplying by $100$ converts to a percentage.

- You may also implement separate standalone operations: **isEmpty()** (check $\text{top} < L$) and **isFull()** (check $\text{top} \ge U$).

### 3.6 Q&A — fixed vs. dynamic size

- **Question:** Like an array, must we declare the stack size in advance (unlike a linked list)?
- **Answer:** It depends on the implementation.
  - **Array-based stack**: assuming a language with fixed-size arrays (e.g. C-style), the size is **limited and must be fixed in advance**. In languages with dynamic arrays (e.g. Python) this is not a problem.
  - **Linked-list-based stack**: size is **not** fixed; memory is dynamically allocated.
- **Follow-up:** With dynamic allocation, can we still check status? — **No meaningful "status"** and **no meaningful "full"** condition under dynamic allocation (we assume ample memory). **"Empty" *is* still meaningful** (nothing in the stack). So for the linked-list version, `status` is reinterpreted as *counting the number of nodes*.

---

## 4. Representation 2 — Linked-List-Based Stack

### 4.1 Structure

- Each **node** has two compartments/fields:
  - **data** — stores the element;
  - **link (next)** — stores the **address of the next node** in the list.
- Pointers maintained:
  - **`stackhead`** — points to the head/front of the linked list (the opening of the stack);
  - **`top`** — points to the **topmost node** of the stack, i.e. the node at the insertion/deletion end.
- **Diagram described:** a chain of boxes, each split into a left (data) half and a right (link) half, with arrows from the link field of each node to the next node. The `stackhead` arrow and the `top` arrow both point at the front-most node (e.g. one holding value 20), which is followed by another node (e.g. 30), and so on, ending in a node whose link is `NULL`.
- Here the linked list does **not** behave like a general linked list: no arbitrary-position insertion or deletion. One end is designated as the "opening" of the stack, and all insertion/deletion happens there.

### 4.2 Algorithm: PUSH (linked-list implementation)

Insert `item` at the front (top) of the stack.

```
PUSH_LL(stackhead, top, item):
1. new <- GETNODE()        // allocate a new node; returns its address
2. new -> data <- item     // store the item in the data compartment
3. new -> link <- top      // new node points to the current top node
4. top  <- new             // top now refers to the new node
5. stackhead -> link <- top   // stackhead now refers to the new node
6. Stop
```

Walk-through given in class (new node inserted before an existing node holding 20):

1. `GETNODE()` allocates memory for a node with two compartments and **returns its address**; that address (e.g. $1024$) is stored in the variable `new`.
2. `new -> data` refers to the data compartment of the node whose address is in `new`; the pushed `item` is written there.
3. `new -> link` must point to the node that comes *after* it — currently the node holding 20, i.e. whatever `top` is pointing to. Hence `new -> link = top`.
4. `top` must always point to the topmost node, which is now the new node ⇒ `top = new`.
5. `stackhead`'s link must also be updated to the new topmost node ⇒ `stackhead -> link = top`.

### 4.3 Q&A — what happens to `new` afterwards? (pointer-variable semantics)

Important conceptual clarification made at length:

- There are **two distinct things**: (a) the **actual memory block** allocated for the node (say at address $1024$), and (b) the **variable `new`**, which is merely a variable holding that address — exactly like writing `x = 5` or `y = 20`, except `new` holds $1024$.
- `GETNODE()` performs the *actual allocation* in RAM and returns the address; `new` simply stores it.
- After the push completes, **`top` (and `stackhead`) hold that same address**, so the node remains reachable. The variable `new` is no longer needed — it is just a working/local variable, like temporaries used inside a function, and becomes obsolete after the function call ends. **The allocated node itself is not lost or freed**; only the temporary variable goes out of scope.
- Analogy to local vs. global variables: local variables inside a function vanish after the call; values you must retain across calls (like `top`) must be preserved, otherwise you lose track of the topmost element.

### 4.4 Algorithm: POP (linked-list implementation)

Remove the node pointed to by `top` and return its data.

```
POP_LL(stackhead, top):
1. if top = NULL then            // stack is empty
2.       print "Stack is EMPTY"
3.       exit
4. else
5.       item <- top -> data     // value returned by the pop
6.       ptr  <- top -> link     // address of the next node
7.       top  <- ptr             // top now points to the next node
8.       stackhead -> link <- ptr   // stackhead also updated
9.       return item
10. endif
11. Stop
```

Walk-through given in class (list: node 20 at top, node 30 next):

1. Check whether the stack is empty; if so, nothing can be removed.
2. The value returned is the data of the node pointed to by `top` ⇒ `item = top -> data`, here $\text{item} = 20$.
3. `top -> link` gives the address of the next node (the one holding 30); store it temporarily in `ptr`.
4. Set `top = ptr` and `stackhead -> link = ptr`, so both pointers now refer to the next node in the list.

### 4.5 Algorithm: STATUS / node count (linked-list implementation)

For the linked-list version, "full" and percentage-full are meaningless; instead we **count the number of nodes** in the stack — a simple traversal.

```
COUNT_LL(stackhead):
1. ptr <- stackhead            // or top
2. nodeCount <- 0
3. while ptr != NULL do
4.       nodeCount <- nodeCount + 1
5.       ptr <- ptr -> link    // move to the next node
6. endwhile
7. return nodeCount
```

Logic as stated: *as long as the pointer is not NULL, keep moving to the next node, and at every new node increment `nodeCount` by 1; stop at NULL (the last node). At the end `nodeCount` is the total number of nodes in the list.*

---

## 5. Summary Comparison

| Aspect | Array-based stack | Linked-list-based stack |
|---|---|---|
| Underlying storage | Array `a[L..U]` | Chain of nodes, each `{data, link}` |
| Position marker | `top` = **index** of topmost element | `top` = **pointer** to topmost node; plus `stackhead` |
| Push | check full; `top <- top+1`; `a[top] <- item` | `new <- GETNODE()`; `new->data <- item`; `new->link <- top`; `top <- new`; `stackhead->link <- top` |
| Pop | check empty; `item <- a[top]`; `top <- top-1` | check empty; `item <- top->data`; `ptr <- top->link`; `top <- ptr`; `stackhead->link <- ptr` |
| Empty test | $\text{top} < L$ | `top = NULL` |
| Full test | $\text{top} \ge U$ | Not meaningful (dynamic allocation) |
| Size | Fixed in advance (for fixed-size arrays) | Dynamic; not fixed |
| Status | $\dfrac{\text{size}-\text{top}}{\text{size}}\times 100$ % free | Count of nodes via traversal |

*(Note: the lecture did not state explicit big-$O$ complexities, but all of push, pop, isEmpty and isFull as given are constant-time — $O(1)$ — while the linked-list node count traversal is $O(n)$.)*

---

## 6. Flagged as Important / For Exams & Next Session

- **Prerequisites assumed:** you must already know **array** and **linked list** representations — the stack is built on top of them. Node structure (`data` + `next` pointer) and linked-list traversal are assumed known.
- **Most important conceptual point stated by the instructor:** among the three design components, the way data is **manipulated** (insert/delete/update rules) is what *primarily* distinguishes one data structure from another — this is why a stack is not "just an array."
- **Definition to memorise verbatim:** *a stack is an ordered collection of homogeneous data elements in which insertion and deletion occur at one end only.*
- **Core operations:** `push` (insert) and `pop` (remove) are the two *basic and defining* operations; `status`, `isEmpty`, `isFull` are additional/auxiliary.
- **Formulas to remember:** empty condition $\text{top} < L$; full condition $\text{top} \ge U$; free space $= \frac{\text{size}-\text{top}}{\text{size}}\times 100$.
- **Next class:** applications of the stack, in particular **evaluation of arithmetic expressions** — infix, prefix, postfix notations; **infix→postfix conversion using a stack**; and **postfix evaluation using a stack**.
- **Reference:** the textbook displayed on the final slide (same one recommended earlier in the course) — the algorithms presented are taken directly from it; slides alone are stated to be sufficient, the book is for further exploration.