# DSM-103 — Data Structures
## Session 6 — 03 Sep 2026 — Instructor: Somnath Dey
### Topic: Singly Linked List (copy / concatenate / search) → Circular Singly Linked List

---

## 1. Overview

This session continues the linked-list unit. After a quick recap of insertion/deletion on a **singly linked list (SLL)**, the instructor develops three new SLL algorithms in detail: **copying (duplicating) a linked list**, **concatenating (merging) two linked lists**, and **searching for a key**. Considerable attention is given to *boundary conditions* (empty list, key located at the last node) and to the difference between `GETNODE` (allocating from the heap / free-storage list) and `RETURNNODE` (returning memory to the heap) — and why "return" is not the same as "remove". The second half introduces the **circular singly linked list (CSLL)**, in which the last node points back to the header instead of to `NULL`, and the class works line-by-line through *which lines of each SLL algorithm must change* for traversal, insert-at-front, insert-at-end, insert-after-key, delete-first, delete-last and delete-key. The session is delivered largely as Socratic Q&A — the instructor states he "has not taught anything here, only asked questions" — and ends by assigning four CSLL conversion problems as homework/Assignment 2 material.

---

## 2. Administrative notes

- **Assignment 1**: deadline extended — submission portal open until **10 September**.
- **Assignment 2**: will be announced shortly; can be done in parallel. Based on the CSLL conversion problems given at the end of this lecture (Section 9).
- **Next class**: day after tomorrow, **2:45 – 3:45 pm**; the following slot **3:45 – 4:45 pm** is kept as an **open doubt-clearing session**.
- Slides/recordings for the previous lecture and this lecture have been uploaded.
- Housekeeping: students joining online must set a **proper display name** (many join with video off).

---

## 3. Recap (previous lecture)

Operations already covered on a singly linked list with a **header node**:

- Insert a node: (a) at the front, (b) at the end, (c) after a given key node.
- Delete a node: (a) the first node, (b) the last node, (c) a node containing a given key.

**Structure assumed throughout:** a *header node* whose `data` field is unused/`NULL` and whose `link` field points to the first real node. The last node's `link = NULL` (for SLL). Example list used in slides: `header → 20 → 30 → ... → 40 → NULL`.

---

## 4. Copying / duplicating a linked list

### 4.1 Problem
Given a linked list, build a **second, independent** linked list containing the same data.

**Key constraints stressed in class:**
- The original list must **not** be modified or deleted.
- The new list needs its **own header node** (a list cannot exist without a header).
- The two lists must remain **completely separate** — you must **not** link the new list into the old one (i.e., don't just copy pointers; allocate a fresh node for every element).

### 4.2 Idea / picture
- `ptr` walks along the **original** list, node by node.
- `header1` is a newly created header for the **new** list; `ptr1` walks along the new list (we never move `header1` itself, because we must be able to return it).
- For every node visited by `ptr`, call `GETNODE` to allocate a new node, copy `ptr→data` into it, hook it onto `ptr1→link`, set the new node's `link = NULL`, then advance **both** `ptr1` and `ptr`.

*Visual:* two horizontal chains drawn one above the other. Top chain = original (`header → 20 → 30 → ...`). Bottom chain = copy, growing from left to right in lock-step as `ptr` slides right along the top chain. There is **no** vertical/diagonal arrow between the two chains — only data values are copied downward.

### 4.3 Algorithm (as presented)

```
COPYLIST(header)
1.  ptr  ← header.link          // ptr at first node of ORIGINAL list
2.  header1 ← GETNODE()         // new header for the DUPLICATE list
3.  ptr1 ← header1
4.  ptr1.data ← NULL            // header node carries no data
5.  while (ptr ≠ NULL) do
6.        new ← GETNODE()
7.        new.data ← ptr.data   // copy the data
8.        ptr1.link ← new       // attach to duplicate list
9.        new.link  ← NULL      // new node is currently the last
10.       ptr1 ← new            // advance in duplicate list
11.       ptr  ← ptr.link       // advance in original list
12. end while
13. return header1
```

Loop terminates when `ptr` reaches the `NULL` at the end of the original list.

---

## 5. Concatenating (merging) two linked lists

### 5.1 Problem
Two lists: `header1 → 20 → 30 → ... → 40` (5 elements) and `header2 → 22 → 33 → 55 → 65 → 80` (5 elements). Objective: append the whole of list 2 to the end of list 1, i.e. after `40` must come `22, 33, 55, 65, 80`.

Student's first (correct) instinct: *"give the address of 22 to the link field of 40"* — i.e. `last_node_of_list1.link ← header2.link`.

### 5.2 Two boundary problems discussed at length

**Problem A — overshooting the last node.**
If you write
```
ptr ← header1.link
while (ptr ≠ NULL) do ptr ← ptr.link
```
then when the loop breaks, `ptr` is **already `NULL`** — it has "crossed 40" — so you have *lost track of the last node's address* and cannot perform `ptr.link ← header2.link`.

**Fix:** test the *link* instead of the pointer:
```
while (ptr.link ≠ NULL) do ptr ← ptr.link
```
Now the loop stops **with `ptr` sitting on node 40**.

**Problem B — empty first list.**
If list 1 is empty (`header1.link = NULL`) and you initialise `ptr ← header1.link`, then `ptr = NULL`, and the very first test `ptr.link ≠ NULL` dereferences `NULL.link` → **access to an undefined address** (crash).

**Fix:** initialise the pointer at the **header itself**, not at the first node:
```
ptr ← header1
```
If the list is empty, `ptr` simply stays on the header and the concatenation attaches list 2 directly after the header — which is exactly what we want ("that means, from which position I want to insert").

### 5.3 Final algorithm

```
CONCATENATE(header1, header2)
1.  ptr ← header1                  // NOT header1.link  (handles empty list 1)
2.  while (ptr.link ≠ NULL) do     // stops ON the last node
3.        ptr ← ptr.link
4.  end while
5.  ptr.link ← header2.link        // splice list 2 behind the last node of list 1
6.  header2.link ← NULL            // FIRST break the old link ...
7.  RETURNNODE(header2)            // ... THEN return the now-orphaned header node
8.  return header1
```

> **Order matters (instructor's explicit warning):** set `header2.link ← NULL` *before* `RETURNNODE(header2)`. Otherwise "if your return node is not written properly there would be a problem" — the freed header would still be pointing into the live list, and you risk returning more than the single node you intend to free.

### 5.4 `GETNODE` / `RETURNNODE` vs. "remove" (student question)

- **Heap memory / free-storage pool**: the region of computer memory holding all currently unused blocks.
- **`GETNODE`** = take a block **out of** the heap (free list) and move it into the *allocated* list, so the program can use it.
- **`RETURNNODE`** = give a node **back to** the heap because the application no longer needs it. The memory itself is *not* destroyed — it stays in your computer; you have simply created free space that can be reused and overwritten later.
- **There is no concept of "removing" memory.** That is why the algorithms say *return* the node, not *remove* it.

---

## 6. Searching an element in a linked list

### 6.1 Idea
Same walk as the first half of "delete a key node", but we **stop as soon as the key is found** and report the node's location; otherwise we report "key not found". Two different reasons can break the loop, and they must be **distinguished**:
1. the key was found (`ptr` points to the node containing the key), or
2. `ptr` reached `NULL` (end of list) — key absent.

### 6.2 Variables
- `ptr` — traversal pointer.
- `flag` — 0 = not yet found, 1 = found.
- `location` — pointer that is returned; holds the address of the node containing the key (e.g. if key `25` is found, `location ← ptr`), `NULL` if not found.

### 6.3 Algorithm

```
SEARCH(header, key)
1.  ptr ← header.link
2.  flag ← 0
3.  location ← NULL
4.  while (ptr ≠ NULL) AND (flag = 0) do
5.        if (ptr.data = key) then
6.              flag ← 1
7.              location ← ptr
8.              print "Search successful"
9.        else
10.             ptr ← ptr.link
11.       end if
12. end while
13. if (flag = 0) then print "Search unsuccessful / key not present"
14. return location
```

> Note: the loop must continue **only while both** conditions hold — `ptr ≠ NULL` **and** `flag = 0`. (In the audio this was said loosely as "either … or"; the break happens when *any one* condition fails.)

### 6.4 Two test cases the class checked
- **Empty list:** `header.link = NULL`, so `ptr = NULL`; the `while` test fails immediately, we never enter the body, we never dereference `ptr.data`, and the algorithm correctly reports "unsuccessful". ✔
- **Key not present (e.g. search 45 in a list without 45):** `ptr` advances via `ptr.link` until it becomes `NULL`; the `while` test is checked **before** `ptr.data` is examined, so no invalid access occurs, and "unsuccessful" is reported. ✔

> **General principle emphasised:** always be conscious of **where you initialised the pointer** (`header` vs. `header.link`) — the correct loop condition (`ptr ≠ NULL` vs. `ptr.link ≠ NULL`) depends on it.

---

## 7. Circular Singly Linked List (CSLL)

### 7.1 Definition
> In a singly linked list the **last node's link field holds `NULL`**.
> In a **circular singly linked list** the **last node's link field holds the address of the header node**, so the chain closes into a ring.

Terminology used interchangeably in the course: *circular singly linked list*, *singly circular linked list*, *CSL/CSLL*.

*Visual:* the usual left-to-right chain `header → 20 → 30 → 40`, but instead of `40 → NULL`, a long arrow curves back from node `40` to the **header** box.

**Consequence:** if you run a naive `while (ptr ≠ NULL)` loop over a CSLL it never terminates — "your linked list will circulate within all these nodes" forever.

### 7.2 How to detect the end
The header's address is **fixed** (e.g. suppose header lives at address 1000). Traversal starts at `ptr ← header.link`. When, after advancing, `ptr` again equals `header` (address 1000 again), you have processed the last node and come back to the start. So:

> **End-of-list test for CSLL: `ptr ≠ header` replaces `ptr ≠ NULL`.**
> (and correspondingly `ptr.link ≠ header` replaces `ptr.link ≠ NULL`; `link ← header` replaces `link ← NULL`.)

An empty CSLL satisfies **`header.link = header`** (not `header.link = NULL`).

### 7.3 Traversal of a CSLL

```
TRAVERSE_CSLL(header)
1.  ptr ← header.link
2.  while (ptr ≠ header) do
3.        process / print ptr.data
4.        ptr ← ptr.link
5.  end while
```

---

## 8. Converting each SLL operation to CSLL (line-by-line, as worked in class)

The general rule derived in class: *wherever the SLL algorithm tests for or assigns `NULL` **as an end-of-list marker**, replace `NULL` by `header`.* But every such change must be re-verified against boundary cases — one of them (insert-after-key) actually needs a **different** fix.

### 8.1 Insert at the FRONT — **no change required**

SLL version:
```
1. new ← GETNODE()
2. new.data ← item
...
6. new.link ← header.link
7. header.link ← new
```
**Reasoning given:** this algorithm contains **no test for the end of the list** at all — it never asks "have I reached the last node?". Since the only difference between SLL and CSLL is what the *last* node's link holds, and we never touch the last node, the algorithm works unchanged. (Several students first guessed line 6 would change; the instructor showed it does not.)

### 8.2 Insert at the END

SLL version (schematic):
```
1. new ← GETNODE()
2. new.data ← item
3. ptr ← header
4. while (ptr.link ≠ NULL) do        ← end-of-list test
5.       ptr ← ptr.link
6. end while
7. new.link ← NULL                   ← the "last node" marker
8. ptr.link ← new
```
**Changes for CSLL:**
- **Line 7:** `new.link ← NULL` → **`new.link ← header`**. *Reason (student, confirmed):* "in a circular linked list the last node points to the header; if you put `NULL` you break circularity — it will no longer be a circular linked list."
- The **traversal condition** (referred to in the discussion as the other line / "step 12") must likewise become **`while (ptr.link ≠ header)`**, otherwise the search for the last node never terminates.

### 8.3 Insert AFTER a key node — the interesting case

SLL version (schematic, with the line numbers used in class):
```
 ...
 6.  ptr ← header.link
 7.  while (ptr.link ≠ NULL) AND (ptr.data ≠ key) do
 8.        ptr ← ptr.link
 9.  end while
10.  if (ptr.link = NULL) then
11.        print "Key is not available in the list"
12.  else
13.        new ← GETNODE(); new.data ← item
14.        new.link ← ptr.link
15.        ptr.link  ← new
16.  end if
```

**Step 1 (mechanical conversion):** line 7 → `while (ptr.link ≠ header) AND (ptr.data ≠ key)`, line 10 → `if (ptr.link = header)`.

**Step 2 — the bug the class discovered.** Suppose the key **is the last node** (e.g. key = 40, the last element). Then when `ptr` reaches node 40:
- `ptr.data = key` → first sub-condition false, **and**
- `ptr.link = header` → second sub-condition false.

Both fail, the loop breaks with `ptr` on node 40 — correct. **But** the following `if (ptr.link = header)` is **true**, so the algorithm wrongly prints *"key is not available"* even though the key exists. The insertion is never performed.

**Step 3 — the correct fix (credited to a student, Arita):** do **not** test the link; test the **data**:

```
10.  if (ptr.data ≠ key) then
11.        print "Key is not available in the list"
12.  else
13.        ... perform the insertion ...
```
This distinguishes the *real* reason the loop ended and works for **all** cases (key first, middle, last, or absent).

**Important sub-point raised and corrected:** a student proposed `if (ptr.link ≠ key)`. The instructor rejected it:
> `ptr.link` is an **address**; `key` is a **data value**. **You cannot compare an address with a data value.** The comparison must be `ptr.data ≠ key`.

**Also noted:** when the key node happens to be the last node, the statement `new.link ← ptr.link` automatically copies the value `header` into the new node's link, so circularity is preserved with no extra code. Nothing special is needed there.

### 8.4 Delete the FIRST node — essentially no change

Only the **empty-list / underflow test** changes:
- SLL: `if (header.link = NULL) then underflow`
- CSLL: `if (header.link = header) then underflow`

Everything else (`ptr ← header.link; header.link ← ptr.link; RETURNNODE(ptr)`) works unchanged.

### 8.5 Delete the LAST node — three changes

SLL version (schematic):
```
 1. if (header.link = NULL) then print "Underflow / empty list"; exit
 ...
 5. ptr ← header.link ;  ptr1 ← header
 6. while (ptr.link ≠ NULL) do          ← change
 7.       ptr1 ← ptr
 8.       ptr  ← ptr.link
 9. end while
10. ptr1.link ← NULL                    ← change
11. RETURNNODE(ptr)
```
**Changes for CSLL:**
1. **Underflow test** (line 1): `header.link = NULL` → `header.link = header`.
2. **Line 6 (loop condition):** `ptr.link ≠ NULL` → `ptr.link ≠ header`.
3. **Line 10:** `ptr1.link ← NULL` → **`ptr1.link ← header`** — "because I have to make sure that it becomes circular again" after the old last node is removed.

### 8.6 Delete a KEY node — two lines change

The SLL version keeps two pointers, `ptr` (current) and `ptr1` (predecessor), and — in the slide version shown — used **two separate loop/test lines (lines 3 and 4)**: one testing for end-of-list and one testing for the key. Both must have `NULL` → `header`.

**Question posed by the instructor (→ becomes homework):** *can the two conditions be merged into a single `while` loop?* Proposed merged form:

```
3.  while (ptr ≠ header) AND (ptr.data ≠ key) do
4.        ptr1 ← ptr ;  ptr ← ptr.link
5.  end while
```
Students must **verify this merged version for every case**: key in the **first** position, key in a **middle** position, key in the **last** position, and key **absent** — and, if it fails, state exactly what modification is needed.

---

## 9. Homework / Assignment 2 problems (explicitly assigned)

Convert each of the following **singly linked list** algorithms into the corresponding **circular singly linked list** algorithm, and *verify all boundary cases*:

1. **Delete a key node from a CSLL**, using the **merged `while` condition** `while (ptr ≠ header) AND (ptr.data ≠ key)` in place of the original lines 3 and 4. Check that deletion works when the key is the **first** element, in **any middle** position, and in the **last** position. If it does not work, write down the required modification; if it does, justify that it works.
2. **Copy / duplicate a linked list** — modify the SLL `COPYLIST` algorithm (Section 4.3) for CSLL.
3. **Merge / concatenate two linked lists** — modify the SLL `CONCATENATE` algorithm (Section 5.3) for CSLL.
4. **Search an element** — modify the SLL `SEARCH` algorithm (Section 6.3) for CSLL.

> These are to be attempted before the doubt-clearing session; the formal Assignment 2 will be created from them.

---

## 10. Complexity summary

*(The instructor did not quote complexities explicitly in this session; these follow directly from the algorithms above and are worth writing in your notes.)*

| Operation | Time | Extra space |
|---|---|---|
| Traverse (SLL or CSLL) | O(n) | O(1) |
| Copy / duplicate list | O(n) | O(n) — one new node per element + 1 header |
| Concatenate two lists (m + n nodes) | O(m) — only list 1 is walked | O(1) |
| Linear search for key | O(n) worst/average, O(1) best | O(1) |
| Insert at front | O(1) | O(1) |
| Insert at end / after key | O(n) | O(1) |
| Delete first | O(1) | O(1) |
| Delete last / delete key | O(n) | O(1) |

---

## 11. Key takeaways / likely exam points

- **SLL vs CSLL in one line:** last node's `link` = `NULL` (SLL) vs. = address of **header** (CSLL).
- **Conversion rule:** replace every end-of-list `NULL` by `header` — *but always re-test the boundary cases*, because the `insert-after-key` test `if (ptr.link = header)` becomes **wrong** and must be replaced by `if (ptr.data ≠ key)`.
- **Never compare an address (`ptr.link`) with a data value (`key`).**
- **Pointer initialisation determines the loop condition:** `ptr ← header` pairs with `while (ptr.link ≠ …)`; `ptr ← header.link` pairs with `while (ptr ≠ …)`. Choosing `ptr ← header` is what makes the concatenation algorithm safe for an **empty first list**.
- **Don't overshoot:** to stop *on* the last node use `ptr.link ≠ NULL`, not `ptr ≠ NULL`.
- **`RETURNNODE` before/after unlinking:** break the link (`header2.link ← NULL`) **first**, then return the node.
- **`GETNODE` = allocate from heap/free list; `RETURNNODE` = give back to heap. Memory is never "removed".**
- **Distinguish the two exit reasons of a search loop** (found vs. end-of-list) using a `flag`, and return the found node through a `location` pointer.
- Empty-CSLL test is `header.link = header`, **not** `header.link = NULL`.