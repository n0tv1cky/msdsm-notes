# DSM-103 Data Structures — Session 5 (2026-08-29, Prof. Somnath Dey)
## Topic: Linked Lists — Representation, Traversal, Insertion, Deletion

---

## 1. Overview

This session introduces the **linked list** as a dynamic alternative to the array. The instructor motivates it from the memory-management problem: arrays need *contiguous* memory, which historically was often unavailable even when enough *scattered* free memory existed; a linked list solves this by storing each element wherever memory is free and keeping the address of the next element inside the node itself. The lecture defines the linked list formally (ordered, finite, homogeneous collection of nodes whose linear order is maintained by links), describes node structure (data part + link part), lists the four variants (singly, circular singly, doubly, circular doubly), and explains the role of the **header node** and the terminating **NULL** pointer. Two representations are then covered: **static** (two parallel arrays — one for data, one for the index/address of the next element) with a fully worked address-chasing example, and **dynamic** (real pointers, `getNode()` allocation, with a byte-level memory layout example). The bulk of the class is spent deriving, step by step, the algorithms for **traversal**, **insertion at front / at end / after a key**, and **deletion of first / last / key node**, including the boundary conditions (empty list, key at last node), the importance of the *order* of pointer assignments, the **two-pointer (current + previous)** technique for deletion, and the time complexities (O(1) for front operations, O(n) for end/key operations, with best/worst/average case discussion).

**Administrative note:** A student requested a doubt-clearing session. The instructor will arrange one **after his five lectures**, in a free slot (weekday daytime possibly, subject to timetable availability).

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Motivation — why linked lists exist
- In an **array**, elements are stored in **contiguous memory locations** (one after another).
- Old machines had very small memory → memory had to be managed efficiently.
- Problem: a large *contiguous* block may not be available, even though the same total amount of memory *is* available in a **scattered** manner.
- Linked-list idea: store each data item wherever free memory exists, and in each item **keep the address of where the next item is** (a *link*). This way all data is stored and all of it stays reachable.
- (Aside: with today's 16 GB+ memories you rarely hit this problem, but the data structure remains fundamental.)

### 2.2 Definition and terminology
- A **linked list is a dynamic data structure**; adjacency between elements is maintained by a **link** (you must *follow the link* to reach the next element).
- **Formal definition given in class:**
  > *A linked list is an ordered collection of finite, homogeneous data elements called **nodes**, where the linear order is maintained by links.*
- Term-by-term explanation given:
  - **Ordered collection** — data is kept one after another (logically).
  - **Finite** — no concept of infinite data.
  - **Homogeneous** — every node has the *same* structure/type. You cannot store an integer in node 1 and a character in node 2. A node *may* have multiple fields (e.g. one integer + one character + the link), but then **every** node has integer + character + link.
  - **Linear order maintained by link** — to get the next element you follow the current node's link; to get the one after, follow *that* node's link.
- **Node** = the whole unit consisting of the **data part** (actual data) + the **link part** (address of the next node).

### 2.3 Types of linked lists
1. **Singly linked list** — one link per node (forward only).
2. **Circular singly linked list** — same, but the **last node's link points back to the first node**.
3. **Doubly linked list** — two links per node: a **forward link** and a **backward link**.
4. **Circular doubly linked list**.

*(This lecture works entirely with the singly linked list.)*

### 2.4 Header node and NULL termination (diagram described)
Picture a horizontal chain of boxes. Each box is split into two cells: **left cell = data**, **right cell = link**. An arrow leaves the right cell of each box and lands on the next box.

- The leftmost box is the **header node**. It has the *same node type* as all other nodes, but its **data field is unused / set to NULL**; only its **link** matters — it stores the address of the **first real node**.
- Example used: five nodes storing five integers. Header → N1 → N2 → N3 → N4 → N5.
- The **last node's link field holds NULL** (drawn as a slash / ground symbol). This is essential: without it, during traversal you would keep reading past the end into **illegal memory** that was never allocated for your data. The NULL is the stop signal.

### 2.5 Static representation (two parallel arrays)
- Called **static** because arrays have a **fixed size** — you can store only as many nodes as the array length allows.
- Use **two parallel arrays of the same size**:
  - `DATA[]` — holds the actual data values.
  - `LINK[]` — at the **same index**, holds the **index/address of the next element** in `DATA[]`.

**Worked example given in class** (indices are the memory locations quoted by the instructor):

| Index | DATA | LINK (index of next) |
|-------|------|----------------------|
| 109   | 20   | 105 |
| 105   | 30   | 101 |
| 101   | 25   | 125 |
| 125   | 35   | 113 |
| 113   | (last value) | NULL / end marker |

Traversal walk-through as the instructor did it:
1. Start at index **109** → data **20**; its link says **105**.
2. Go to index **105** → data **30**; its link says **101**.
3. Go to index **101** → data **25**; its link says **125**.
4. Go to index **125** → data **35**; its link says **113**.
5. Go to index **113** → last element; link is NULL → stop.

- Summary rule: *in the data array position you get the actual data; at the same position in the link array you get the address/index of the next data.*

### 2.6 Dynamic representation (pointers) — memory layout example
Assume an integer requires **8 bytes** and a pointer (address) also requires **8 bytes**, so **one node = 16 bytes**.

Diagram described:
- **Header node** placed at address **100**, occupying bytes **100–116** (instructor's wording). Its data field holds nothing/NULL; its **link field holds 200**.
- **Next node** located at address **200**, holding data **20** and its own link field.
- In between (addresses 116–200) memory is *not* free/contiguous — there are other allocations and scattered free holes. That is exactly why the second node lands at 200 rather than immediately after 100.
- So `header->link` = 200 means "the next node lives at address 200".

**(Bit/byte refresher given: 1 binary digit = 1 bit; 8 bits = 1 byte.)**

### 2.7 Notation used in the course
- To access the fields of a node pointed to by pointer `ptr`:
  - `ptr->data` and `ptr->link`   ← **the instructor will use this arrow notation throughout**
  - (equivalent alternative: `ptr.data`, `ptr.link`)
- `ptr = header->link` sets `ptr` to the address of the **first real node**.
- `ptr->data` returns the **value**; `ptr->link` returns the **address** of the next node.

### 2.8 Student question — Python `list` vs linked list
- **Q:** Is Python's `list` the same concept?
- **A:** Yes in spirit — Python's built-in library stores data in this manner and provides the interface, but **you don't have to manage the pointers yourself**. In C/C++ you must manage many pointers explicitly; Python hides all the pointer manipulation. Same concept, invisible pointers.

### 2.9 Operations on a linked list (the full list stated)
1. **Traversing** the list (visit/process all nodes).
2. **Inserting** a node — (a) at the front (just after header), (b) at the end, (c) after/before a **key** node.
3. **Deleting** a node — (a) the first node, (b) the last node, (c) a **key** node.
4. **Copying** one linked list into another.
5. **Merging** two linked lists into a larger one.
6. **Searching** for an element (needed implicitly by key-based delete/insert).

**Important conceptual point:** unlike arrays, a linked list has **no indexing** — you cannot say "node i" or "node j". You must access nodes **one after another** starting from the header.

---

## 3. Algorithms (as developed in class)

### 3.1 Traversal

```
TRAVERSE(header):
1. ptr = header->link          // point to first real node
2. while (ptr != NULL):
3.       process(ptr->data)    // e.g. print the value
4.       ptr = ptr->link       // move to next node
5. stop
```
- Logic: the test `ptr != NULL` decides whether there is still a node to process; when `ptr` finally lands on NULL the traversal stops.
- **Time complexity: O(n)** (must visit every node).

---

### 3.2 Insertion at the FRONT (just after the header)

Worked example: existing list `header → 20 → 25 → 35 → 40 → NULL`; insert **10** at the front so that it becomes `header → 10 → 20 → …`.

Pointer surgery described: create the new node; make **new node's link point to 20** (i.e., copy the header's current link into it); then **break the header's link** and make **header point to the new node**.

```
INSERT_FRONT(header, x):
1. new = getNode()             // allocates memory, returns its address
2. if (new == NULL): print "memory overflow / no space"; stop
3. new->data = x
4. new->link  = header->link   // new node points to old first node
5. header->link = new          // header now points to new node
6. stop
```

- **`getNode()`** — allocates memory for one node and returns its **address**; if memory is entirely full it returns **NULL**. Hence step 2's validity check.
- **Order matters (asked as a class question):** if you swap steps 4 and 5 — i.e. do `header->link = new` first — you **lose the address of node 20** (the rest of the list becomes unreachable). *Student answer accepted: "We will lose the pointer of 20."*
  - Workaround if you must reorder: save `header->link` in a **temporary variable** first. But when directly manipulating pointers with no extra variable, the order above is mandatory.
- Steps 3 (assign data) may be done before or after linking; it doesn't matter.
- **Time complexity: O(1)** — fixed number of steps, no loop, **independent of list size**. (The class initially guessed "it depends"; corrected to constant time.)

---

### 3.3 Insertion at the END

Student-proposed steps (accepted as correct): traverse until you reach the last node, make the last node's link point to the new node, and set the new node's link to NULL.

Two boundary decisions were derived carefully:

**(a) Where to initialise `ptr`?** → `ptr = header` (**not** `header->link`).
**(b) What is the loop condition?** → `ptr->link != NULL` (**not** `ptr != NULL`).

*Reasoning given:*
- If the condition were `ptr != NULL`, the loop would walk **past** the last node onto NULL, and you cannot attach anything to a NULL node.
- With `ptr->link != NULL`: when `ptr` sits on node 40 (last node), `ptr->link` is NULL → loop breaks → `ptr` stays parked **on the last node**, exactly where you need it.
- If you started with `ptr = header->link` **and the list is empty**, `ptr` would be NULL and evaluating `ptr->link` would **access illegal memory / throw an error**. Starting at `header` makes the empty-list case work, because the header always exists.

```
INSERT_END(header, x):
1. new = getNode()
2. if (new == NULL): print "overflow"; stop
3. ptr = header
4. while (ptr->link != NULL):
5.       ptr = ptr->link            // ptr ends on the last node
6. new->data = x
7. new->link = NULL
8. ptr->link = new
9. stop
```
- **Time complexity: O(n)** — the loop runs as many times as there are nodes; list of 10 → 10 iterations, list of 100 → 100 iterations. Grows **linearly** with list size.

---

### 3.4 Insertion AFTER a KEY node

Goal: e.g. insert a new node **after** the node whose data = 25.

**Why "after the key" and not "before" (in a singly linked list):** a singly linked list keeps only the **forward** link, so from a node you cannot reach its predecessor. If you park the pointer on 35 and want to insert *before* it, managing the previous node is difficult. Therefore in a singly linked list we park the pointer **on the key node** and insert *after* it. (In a **doubly linked list** you may park before or after, either is fine.)

```
INSERT_AFTER_KEY(header, key, x):
1.  new = getNode()
2.  if (new == NULL): print "overflow"; stop
3.  ptr = header
4.  while (ptr->data != key  AND  ptr->link != NULL):
5.        ptr = ptr->link
6.  // loop breaks when EITHER key found OR end of list reached
7.  if (ptr->data == key):
8.        new->link = ptr->link
9.        new->data = x
10.       ptr->link = new
11. else:
12.       print "key not available in the list"
13. stop
```

Loop logic as stated: *"If both conditions are false I will move ahead; if any one of these conditions is true (found the key, or reached the end) I break the loop."*

**⚠ Bug discussed in class and its fix (likely exam point):**
- The **original** version of the algorithm tested (at line 10 of the slide) only whether the loop broke because `ptr->link == NULL`, and if so declared "key not found".
- **Failing case: the key is the LAST element.** Then the loop also breaks with `ptr->link == NULL`, and the algorithm wrongly reports "key not available" even though the key *is* there.
- **Fix 1 (student's, accepted):** also check `ptr->data`. i.e. structure it as `if (ptr->data == key) then insert  else "key not found"` — as written in the pseudocode above.
- **Fix 2 (instructor's alternative):** start one node later and swap the roles of the checks:
  - `ptr = header->link`
  - loop while `(ptr->data != key AND ptr->link != NULL)`
  - then check `ptr->link != NULL` / key condition appropriately.

**Complexity:** depends on where the key is.
- **Best case:** key is the first node → **O(1)**.
- **Worst case:** key is the last node → **O(n)**.
- **Average case:** somewhere in between.
- **Convention stated:** since we generally don't know the situation, **we always quote the worst-case complexity** → **O(n)**.

**Aside on notation:** this "order of n / big-O notation" will be covered properly later; for now, understand it as *time grows linearly with the size of the list*.

---

### 3.5 Deletion of the FIRST node

Diagram described: keep a temporary pointer on the first node so you don't lose it; make the header's link jump over it to the second node; then cut the deleted node's own link and return it to memory.

```
DELETE_FIRST(header):
1. ptr = header->link
2. if (ptr == NULL): print "list is empty, deletion not possible"; stop
3. header->link = ptr->link     // header jumps over the first node
4. ptr->link = NULL             // detach the node completely
5. return ptr to free memory    // (deallocate)
6. stop
```
- The instructor noted an extra pointer `ptr1` could be used to hold the second node's address, but it is unnecessary — `ptr->link` serves the same purpose directly.
- **Time complexity: O(1)**.

---

### 3.6 Deletion of the LAST node — the TWO-POINTER technique

**Key idea (explained twice on request):** to delete a node you need **both** the node itself **and its predecessor**, because the predecessor's link must be set to NULL. In a singly linked list you cannot go backwards, so you carry **two pointers**:
- `ptr` = current node,
- `ptr1` = the node **just before** `ptr`.

Each time you advance, you first copy the current `ptr` into `ptr1`, then move `ptr` forward.

```
DELETE_LAST(header):
1. ptr  = header
2. ptr1 = NULL
3. while (ptr->link != NULL):
4.       ptr1 = ptr           // remember the previous node
5.       ptr  = ptr->link     // advance
6. // now: ptr = last node (e.g. 40), ptr1 = its predecessor (e.g. 35)
7. ptr1->link = NULL          // predecessor becomes the new last node
8. // ptr->link is already NULL
9. return ptr to free memory
10. stop
```
- The condition `ptr->link != NULL` also covers the **empty list** case (with `ptr` starting at `header`, if the list is empty the loop never runs).
- Instructor's remark: *"This is a very simple approach if you use the two pointers."*
- **Time complexity: O(n)**.

---

### 3.7 Deletion of a KEY node

Same two-pointer logic, but the loop must **also** stop when the key is found.

```
DELETE_KEY(header, key):
1.  ptr  = header            // (or header->link, with the corresponding adjustments)
2.  ptr1 = NULL
3.  while (ptr->data != key  AND  ptr->link != NULL):
4.        ptr1 = ptr
5.        ptr  = ptr->link
6.  if (ptr->data == key):
7.        ptr1->link = ptr->link   // predecessor now points to successor (e.g. 25's predecessor → 35)
8.        ptr->link  = NULL        // detach the key node from the main list
9.        return ptr to free memory
10. else:
11.       print "key not found"
12. stop
```
- Diagram described: with the list `header → 20 → 25 → 35 → 40 → NULL` and key = 25, after the loop `ptr1` sits on **20** and `ptr` sits on **25**. Line 7 redirects 20's link to **35**, line 8 cuts 25 loose; 25 is then returned to free memory.
- **Time complexity: O(n)** worst case (same best/worst/average reasoning as key insertion).

---

## 4. Complexity Summary Table (as discussed)

| Operation | Complexity | Reason given |
|---|---|---|
| Traversal | O(n) | must visit every node |
| Insert at front | **O(1)** | fixed number of statements, no loop, independent of list size |
| Insert at end | O(n) | must traverse to the last node; loop runs once per node |
| Insert after key | O(n) worst (O(1) best if key is first) | search cost dominates; we quote worst case |
| Delete first | O(1) | constant pointer surgery |
| Delete last | O(n) | must traverse with two pointers |
| Delete key | O(n) worst | search cost |

---

## 5. Flagged as Important (exam / assignment relevance)

- **Order of pointer assignments in insertion at front** — swapping `new->link = header->link` and `header->link = new` **loses the rest of the list**. This was posed as a direct class question; be able to explain *why* and to give the temporary-variable workaround.
- **Boundary/borderline conditions must always be checked**, specifically:
  - `getNode()` returning NULL (memory overflow) before every insertion;
  - empty list before every deletion;
  - starting at `header` (not `header->link`) and using `ptr->link != NULL` (not `ptr != NULL`) for end-insertion/last-deletion, otherwise you dereference NULL and access **illegal memory**.
- **The buggy key-insertion algorithm** (fails when the key is the **last node**) and its two corrections — the instructor explicitly asked students to identify and rectify it.
- **Convention:** when reporting the time complexity of an algorithm we always report the **worst case** (assume the key is at the last position) → O(n).
- **Big-O / order notation** will be treated in detail in a later lecture.
- **Linked lists have no indexing** — you cannot refer to "node i"; all access is sequential from the header. Expect this to be contrasted with arrays.
- **Homework/next step stated at the end:** *"Please go through this slide"* (the deletion algorithms) before the next class; the instructor offered to repeat the deletion material if doubts remain.
- Still to be covered from the operations list: **copying** a list, **merging** two lists, and **searching**.