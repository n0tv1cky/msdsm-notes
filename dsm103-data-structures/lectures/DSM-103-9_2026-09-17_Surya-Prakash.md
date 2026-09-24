# DSM-103 Data Structures — Session 9
**File:** `DSM-103-9_2026-09-17_Surya-Prakash`
**Topic:** Stacks (continued) — operations, array implementation, and applications (string reversal, arithmetic expression notation & evaluation)

---

## 1. Overview

This session continues the discussion of the **stack** ADT begun in the previous class. It starts by recapping the general framework for defining any data structure (what data is stored, how it is stored, what operations are allowed), then establishes the stack as a *restricted, linear, LIFO* data structure with `push` and `pop` as its core operations, plus auxiliary operations `status`, `isEmpty`, `isFull`, and the error conditions **overflow** and **underflow**. A large part of the class is spent on the array-based implementation: the need for a `top` index variable, why `top` is initialised to **−1**, and a full hand-trace of a sequence of pushes and pops. The second half covers applications: reversing a string (and hence palindrome checking) using a stack, and then **arithmetic expressions** — infix vs. prefix vs. postfix notation, why postfix is preferred for machine evaluation (no parentheses needed, directly stack-evaluable), the operator precedence/associativity table, several worked infix→postfix/prefix conversions, and finally the **stack-based postfix evaluation algorithm**, traced on the expression `2 3 4 + *`.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap — How we define any data structure
For **every** data structure (array, linked list, stack, queue, and later tree-based structures) we must specify three things:
1. **What data** we are going to store.
2. **How** the data is stored (the physical/logical organisation).
3. **What operations** are possible on the structure.

### 2.2 Stack as a "restricted" data structure
- **Restricted** = you do **not** have free/random access for insertion and deletion. You cannot insert or delete at an arbitrary position; you must obey a rule.
- **Stack is a linear data structure** → it has two ends, but **insertion and deletion both happen at only ONE end**.
- *Visual described in class:* draw a vertical container (like a bucket) open at the top. An arrow labelled "insert" points into the top; an arrow labelled "delete" points out of the same top. The bottom is closed.
- Consequence: a newly added element **sits on top of the current topmost element**; a removed element is always the **topmost** element.

### 2.3 LIFO principle
- **LIFO = Last In, First Out.** The element added last is the element removed first.
- Contrast flagged for later: queues use different operation names and a different principle.

### 2.4 Stack operations

| Operation | Meaning | Notes |
|---|---|---|
| **push** | Insert an element at the top | Name is stack-specific |
| **pop** | Remove the topmost element | Name is stack-specific |
| **status** | Returns state of stack: full / empty / how much is occupied | Meaningful for **both** array and linked-list implementations (for linked list it returns the *number of elements* currently in the stack) |
| **isEmpty** | Returns true/false — is the stack empty? | Really only meaningful for the **array** implementation |
| **isFull** | Returns true/false — is the stack full? | Really only meaningful for the **array** implementation |

### 2.5 Overflow and underflow
- **Stack overflow**: the stack is already full (`isFull` returns *true*) and you attempt a **push**. → *Overflow is associated with `push`.*
- **Stack underflow**: the stack is empty (`isEmpty` returns *true*) and you attempt a **pop**. → *Underflow is associated with `pop`.*

### 2.6 Array vs. Linked-list implementation (student question, answered in class)
- Two implementations were covered last class: **using an array** and **using a linked list**.
- In most programming languages an **array must be declared with a fixed size** → so "full" is a real state → `isFull` / `isEmpty` are meaningful.
- A **linked-list based stack is dynamic** → there is no fixed capacity → `isFull` has **no meaning**; `isEmpty` is also discussed as not meaningful in the same fixed-capacity sense. **`status` still makes sense** (it returns how many nodes/elements are present).

---

### 2.7 Array implementation — the two required variables

To implement a stack with an array you need **exactly two things**:
1. An **array** (of type `int`, `float`, `char`, … depending on what you store) to hold the data items.
2. An **integer variable `top`** (the "top pointer" / top index) which records the index of the current topmost element.

**`top` decides everything:**
- **To pop:** remove the element at index `top`.
- **To push:** the free slot is at index `top + 1`.

**Core rules (order matters!):**
```
PUSH(x):
   1. top = top + 1        // increment FIRST
   2. array[top] = x       // then store

POP():
   1. value = array[top]   // read/remove FIRST
   2. top = top - 1        // then decrement
   3. return value
```

### 2.8 Why `top = -1` for an empty stack (extended Q&A)
- Array indices are `0, 1, 2, 3, …` — all **valid** positions.
- If we set `top = 0` on an empty stack, that would *claim* there is a topmost element sitting at index 0 → wrong, because `top` by definition always points at the topmost **existing** element.
- Therefore the empty-stack sentinel must be a value that is **impossible as an index** → a **negative** number.
- `-2`, `-3`, … would also work as "empty" markers, **but `-1` has a special advantage**: the general push rule `top = top + 1` then automatically yields index **0** for the very first element pushed. So *the same push logic works for the first element as for every other element* — no special case needed.

**Emptiness / fullness tests (array implementation):**
```
isEmpty()  :  return (top == -1)
isFull()   :  return (top == SIZE - 1)      // "top equals the size of the stack"
```
*(Lecture phrasing: "if the top value is equal to the size of the stack then we say stack is full.")*

---

### 2.9 Worked example — trace of a push/pop sequence

Array drawn horizontally with indices `0 1 2 3`. `top` is an arrow beneath the array pointing at the current topmost cell.

**Operation sequence:** `push 8`, `push 3`, `pop`, `push 2`, `push 5`, `pop`, `pop`, `push 9`, `push 1`

| Step | Operation | top before | top after | Array contents (index 0 →) | Comment |
|---|---|---|---|---|---|
| 0 | (initial) | — | **−1** | `[ _ , _ , _ , _ ]` | empty, top points nowhere |
| 1 | push 8 | −1 | **0** | `[ 8 , _ , _ , _ ]` | top←−1+1=0, store 8 |
| 2 | push 3 | 0 | **1** | `[ 8 , 3 , _ , _ ]` | top←1, store 3 |
| 3 | pop | 1 | **0** | `[ 8 , _ , _ , _ ]` | removes 3 (the topmost), then top−− |
| 4 | push 2 | 0 | **1** | `[ 8 , 2 , _ , _ ]` | |
| 5 | push 5 | 1 | **2** | `[ 8 , 2 , 5 , _ ]` | |
| 6 | pop | 2 | **1** | `[ 8 , 2 , _ , _ ]` | removes 5 |
| 7 | pop | 1 | **0** | `[ 8 , _ , _ , _ ]` | removes 2 |
| 8 | push 9 | 0 | **1** | `[ 8 , 9 , _ , _ ]` | |
| 9 | push 1 | 1 | **2** | `[ 8 , 9 , 1 , _ ]` | **final stack** |

**Invariant emphasised:** *at every point `top` points to the topmost element of the stack.*

> Complexity: `push` and `pop` in the array implementation are constant-time index operations (the lecture did not state O-notation explicitly, but each is a single increment/decrement plus one array access → **O(1) time, O(1) extra space**; the array itself is O(n) space).

---

### 2.10 Application 1 — Reversing a string

**Idea:** read the string left→right, push each character; then pop everything. Because of LIFO, characters come out in reverse order.

```
REVERSE(S):
   1. create empty stack
   2. for each character ch in S (left to right):
          push(ch)
   3. while stack not empty:
          output pop()
```

**Worked example from class:** string `A B C D`
- Push `A` → stack: `A`
- Push `B` → stack: `A B` (B on top)
- Push `C` → stack: `A B C`
- Push `D` → stack: `A B C D` (D on top)
- Now pop repeatedly → `D`, `C`, `B`, `A` → output `D C B A` = reversed string.

**Use case mentioned:** **palindrome checking** — reverse the string using a stack, then compare the reversed string with the original; a palindrome reads the same first→last and last→first.

---

### 2.11 Application 2 — Arithmetic expressions

#### 2.11.1 The three notations

| Notation | Form | Example (`a` plus `b`) |
|---|---|---|
| **Infix** | `operand operator operand` — operator **between** the operands | `a + b` |
| **Prefix** (Polish) | `operator operand operand` — operator **first** | `+ a b` |
| **Postfix** (Reverse Polish) | `operand operand operator` — operator **last** | `a b +` |

General template used on the slide: infix `arg1 op arg2`; prefix `op arg1 arg2`; postfix `arg1 arg2 op`.

- All three express **exactly the same expression and give the same result** — only the *writing order* differs.
- **Unary operators** (e.g. `++a`, `a++`): there is **no infix form**; only **prefix** and **postfix** exist.

#### 2.11.2 Why bother with postfix? (two advantages)
1. **A stack can evaluate a postfix expression easily**; a stack cannot directly evaluate an infix expression.
2. **Postfix needs no parentheses.** The evaluation order is encoded implicitly in the operand/operator ordering.

*Motivating discussion:* In infix, `a + b * c` means "multiply b and c first, then add a", because `*` has higher precedence than `+`. If you want the addition first you **must** write `(a + b) * c`. In postfix no brackets are ever needed.

*Why humans use infix:* Infix is natural for people; postfix is convenient for the machine. Analogy given: we write programs in a high-level language, the **compiler** converts to low-level language for the machine — similarly, the infix expression we write is converted to postfix so the computer can evaluate it with a stack.

#### 2.11.3 Worked conversions — simple cases

**Case A: `(2 * 3) + 4` (multiply first)**
1. Innermost/highest-priority sub-expression: `2 * 3` → postfix `2 3 *`
2. Now the expression is `(2 3 *) + 4` → operand1 = `2 3 *`, operand2 = `4`, operator = `+`
3. Result: **`2 3 * 4 +`**

**Case B: `2 * (3 + 4)` (add first)**
1. Innermost bracket: `3 + 4` → postfix `3 4 +`
2. Now: `2 * (3 4 +)` → operand1 = `2`, operand2 = `3 4 +`, operator = `*`
3. Result: **`2 3 4 + *`**

*Point made:* the two postfix strings differ, and each one **implicitly** fixes the evaluation order — **no parentheses required**.

#### 2.11.4 Worked conversion — nested brackets

**Infix: `A - (B - (C - D))`**

| Step | Work | Result |
|---|---|---|
| 1 | Innermost bracket `C - D` → `C D -` | `A - (B - (C D -))` |
| 2 | Next bracket: operand1 = `B`, operand2 = `C D -`, operator = `-` → `B C D - -` | `A - (B C D - -)` |
| 3 | Outermost: operand1 = `A`, operand2 = `B C D - -`, operator = `-` | **`A B C D - - -`** |

- Equivalent prefix (by the same procedure, operator written first at each step): **`- A - B - C D`**
- **Rule used:** brackets are resolved exactly as in school algebra — **innermost bracket first**.

#### 2.11.5 Student question — multi-digit numbers
- On paper, `1 2 23` could be misread as `1 22 3`. Remedy when writing by hand: **leave extra space between numbers**, or **put multi-digit numbers in brackets**, e.g. `1 2 (23)`.
- **Inside the computer there is no ambiguity**, because each number `1`, `2`, `23` is stored as a separate item (a separate stack slot / token).

---

### 2.12 Operator precedence and associativity table

| Precedence (highest → lowest) | Operator | Associativity |
|---|---|---|
| 1 (highest) | `^` (power / exponentiation) | **Right to left** |
| 2 | `*` , `/` (multiplication, division) | **Left to right** |
| 3 (lowest) | `+` , `-` (addition, subtraction) | **Left to right** |

- **Brackets override everything** — resolve brackets first; *inside* a bracket, apply this same precedence/associativity table.
- **Precedence** decides *which of two different operators* goes first.
  - Example: in `a + b * c * d`, `*` beats `+`, so the multiplications happen first.
- **Associativity** decides *which of two equal-precedence operators* goes first.
  - In `a + b * c * d` there are two `*`'s → left-to-right → the **leftmost** `*` (`b * c`) is evaluated first.
  - `a + b + c` → left-to-right → `(a + b)` first, then `+ c`.
  - `a ^ b ^ c` → **right-to-left** → `b ^ c` first, then `a ^ (…)`.

**Worked example using associativity: `a ^ b ^ c` → prefix**
1. Right-to-left, so handle `b ^ c` first → prefix `^ b c`
2. Remaining: `a ^ (^ b c)` → operator `^`, operand1 = `a`, operand2 = `^ b c`
3. Result: **`^ a ^ b c`**

---

### 2.13 Algorithm — Evaluating a postfix expression with a stack

**Input:** an arithmetic expression in **postfix** form.
**Data structure:** one stack.

```
EVALUATE_POSTFIX(expr):
   1. create an empty stack
   2. scan the expression LEFT to RIGHT, one item (token) at a time
   3. for each item read:
        a. if the item is an OPERAND:
               push(item)
        b. if the item is an OPERATOR:
               arg2 = pop()            // FIRST value popped = SECOND argument
               arg1 = pop()            // SECOND value popped = FIRST argument
               result = arg1 <operator> arg2
               push(result)
   4. when the whole expression has been scanned,
      the single value left on the stack is the answer
```

> **Critical detail stressed in the lecture:** the **first** element popped becomes **argument 2 (the right operand)** and the **second** element popped becomes **argument 1 (the left operand)**. The operation performed is `arg1 op arg2`.
> This does not matter for `+` and `*`, but it is **essential for `-` and `/`** (otherwise you compute `b − a` instead of `a − b`).

> Complexity (not given numerically in class, stated here for completeness): each token is processed once with O(1) stack work → **O(n) time**, **O(n) space** in the worst case for the stack.

#### Worked trace: evaluate `2 3 4 + *`

| Token read | Type | Action | Stack after (bottom → top) |
|---|---|---|---|
| `2` | operand | push 2 | `2` |
| `3` | operand | push 3 | `2 3` |
| `4` | operand | push 4 | `2 3 4` |
| `+` | operator | pop → arg2 = 4; pop → arg1 = 3; compute `3 + 4 = 7`; push 7 | `2 7` |
| `*` | operator | pop → arg2 = 7; pop → arg1 = 2; compute `2 * 7 = 14`; push 14 | `14` |

**Final answer = 14.** (Note the stack contents `2 3 4` collapse to `2 7`: the 3 and 4 are replaced by their sum.)

---

## 3. Flagged as Important / Likely Exam or Assignment Material

The lecturer explicitly used the words "remember", "important", "must", or returned to a point repeatedly for the following:

1. **"Please remember: implementing a stack requires TWO things — the array (to hold data) and the `top` integer variable."**
2. **Why `top` is initialised to −1** — must be a *negative (impossible) index* so it can flag "empty", and −1 specifically so that `top+1 = 0` makes the first push use the *same* general rule. (Asked twice by students; explained at length.)
3. **Order of operations inside push and pop**: push = *increment `top` first, then store*; pop = *remove/read first, then decrement `top`*.
4. **Invariant:** `top` always points at the topmost element of the stack.
5. **`isFull` / `isEmpty` are meaningful only for the array implementation**; for linked-list stacks only `status` is meaningful (it returns the element count). This came directly out of a student question — likely viva/exam material.
6. **Overflow ↔ push; underflow ↔ pop** — know which error goes with which operation.
7. **"Remember, this is important"** (verbatim) — in postfix evaluation, **the first popped operand is argument 2, the second popped operand is argument 1**, because it changes the answer for subtraction and division.
8. **The precedence/associativity table** — power highest and **right-to-left**; `* /` then `+ -`, both **left-to-right**; brackets first, innermost bracket first.
9. **Two advantages of postfix** (stack-evaluable; no parentheses needed) — asked about by a student and answered directly.
10. **Practice instruction given in class:** "you can just try out and convert the expression to prefix" — i.e., redo the `A - (B - (C - D))` example (and the `(2*3)+4` / `2*(3+4)` examples) in **prefix** notation yourself.

---

## 4. Quick Reference Sheet

```
STACK (array implementation)
  data:  array A[0..SIZE-1], int top
  init:  top = -1

  isEmpty()  :  top == -1
  isFull()   :  top == SIZE - 1
  push(x)    :  if isFull() -> OVERFLOW
                top = top + 1 ; A[top] = x
  pop()      :  if isEmpty() -> UNDERFLOW
                x = A[top] ; top = top - 1 ; return x
  Principle  :  LIFO (Last In, First Out)

NOTATIONS        a + b
  infix   : a + b        (operator between)
  prefix  : + a b        (operator first)
  postfix : a b +        (operator last)

PRECEDENCE:  ^  >  * /  >  + -
ASSOCIATIVITY: ^ = right-to-left ;  * / + - = left-to-right
BRACKETS: innermost first, always

POSTFIX EVAL:  operand -> push
               operator -> arg2 = pop(); arg1 = pop();
                           push(arg1 op arg2)
```