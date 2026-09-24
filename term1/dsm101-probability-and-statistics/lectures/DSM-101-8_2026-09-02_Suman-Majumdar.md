# DSM-101 — Probability & Statistics
## Session 8 (2026-09-02) — Bayes' Theorem in Practice: Monty Hall & the "You Are the Barrister" Problem
**Instructor: Suman Majumdar**

---

## 1. Overview

This session is a purely applied follow-up to the earlier lectures on Bayes' theorem. The instructor begins by re-deriving/restating Bayes' theorem in its Bayesian-inference form (posterior = likelihood × prior / evidence), with special attention to the **evidence** term $P(\text{data})$ — what it means, why it is a sum (discrete case) or an integral (continuous case) over all ways of producing the observed data, and why it will matter later for **model selection**. The librarian-vs-farmer example from the previous class is revisited numerically to make the evidence term concrete. The bulk of the lecture is then a careful, step-by-step Bayesian solution of the **Monty Hall problem**, emphasising that *every step of the game supplies information* (you chose door A; the host knows where the prize is; the host may not open your door or the prize door) and that these facts are implicit conditioning information. The conclusion: sticking gives $1/3$, switching gives $2/3$ — a result the instructor stresses cannot be obtained by naive frequentist "two doors left, so 50/50" reasoning. The class ends with a second Bayesian-reasoning problem, the **barrister / stolen cheese problem**, a classic example of a defence lawyer suppressing a crucial piece of prior information (that a theft definitely occurred), where correct Bayesian accounting flips a claimed probability of $0.0004$ into a near-certainty. Homework: additional Bayes problems in the posted slides and Sheldon Ross's textbook.

---

## 2. Topics and Concepts, in Order of Presentation

### 2.1 Restatement of Bayes' Theorem (inference form)

$$P(\theta \mid \text{data}) = \frac{P(\text{data} \mid \theta)\, P(\theta)}{P(\text{data})}$$

with

$$P(\text{data}) = \int P(\text{data} \mid \theta)\, P(\theta)\, d\theta$$

Naming of each term (write these down — used throughout):

| Term | Name |
|---|---|
| $P(\theta \mid \text{data})$ | **Posterior** — probability of the parameter/model given the data |
| $P(\text{data} \mid \theta)$ | **Likelihood** — how likely the data is to match your model |
| $P(\theta)$ | **Prior** — information held *before* the experiment/observation |
| $P(\text{data})$ | **Evidence** (a.k.a. probability of the data / marginal likelihood) |

- Clarification given in response to a student question: the posterior sits alone on the **left-hand side**; on the right you have likelihood × prior **divided by** the evidence.
- The evidence is literally the **numerator integrated (or summed) over all possible $\theta$** — i.e. all the ways the observed data could have arisen, each weighted properly.
- **Discrete vs continuous:** if $\theta$ takes discrete values (e.g. population split into two groups), the evidence is a **plain sum**; if $\theta$ is a continuous variable, it becomes an **integral**. Nothing else changes.
- Flagged as important: the evidence term **will be returned to later in the course when discussing model selection**.

### 2.2 Recap Worked Example — Librarian vs. Farmer (illustrating the evidence term)

Setup: you meet a person on the street described as orderly, meek, keeps to themselves. Call this set of characteristics **$A$**. Assume the population consists *only* of librarians and farmers.

Given numbers used in class:
- Characteristic $A$ matches **40%** of librarians → $P(A \mid \text{librarian}) = 4/10$
- Characteristic $A$ matches **10%** of farmers → $P(A \mid \text{farmer}) = 1/10$
- Population ratio: **20 farmers for every 1 librarian** → priors $P(\text{librarian}) = 1/21$, $P(\text{farmer}) = 20/21$

(The instructor first wrote $1/20$ and $20/20$, then corrected on the fly to $1/21$ and $20/21$ so the priors sum to 1. Concrete counting version used: out of 210 people, 10 are librarians and 200 are farmers; of the 10 librarians, 4 have characteristic $A$; of the 200 farmers, 20 have characteristic $A$.)

Numerator (likelihood × prior) for librarian:
$$P(A \mid \text{librarian})\,P(\text{librarian}) = \frac{4}{10}\times\frac{1}{21}$$

Evidence (what is the probability of *seeing characteristic $A$ at all*, regardless of occupation):
$$P(A) = \frac{4}{10}\times\frac{1}{21} \;+\; \frac{1}{10}\times\frac{20}{21}$$

Posterior:
$$P(\text{librarian}\mid A) = \frac{\frac{4}{10}\cdot\frac{1}{21}}{\frac{4}{10}\cdot\frac{1}{21} + \frac{1}{10}\cdot\frac{20}{21}}$$

**Key conceptual point:** the evidence is the probability of observing the feature **irrespective of which group produced it** — you sum over *all possible ways* the observation could occur. This is exactly why the integral/sum appears in $P(\text{data})$.

### 2.3 The Monty Hall Problem — Setup and Story

- Historical/cultural framing: a famous British game show (later copied in the US and parts of Asia, including India). The instructor notes an ancient Indian street-bazaar version: a coin hidden under one of three bowls, the performer reveals one empty bowl, then asks whether you want to switch.
- Game show version: host **Monty Hall**, three doors, a car (or, in the slide's version, a bottle of Irn-Bru, the Scottish soft drink) behind one door and junk (Coca-Cola) behind the others.
- Sequence of play:
  1. Contestant picks a door.
  2. Monty opens **one of the other doors**, revealing junk.
  3. Contestant is asked: **stick or switch?**
- The question to answer **quantitatively**: what is your winning probability if you stick, and what if you switch?
- **The frequentist/naive intuition:** two doors remain, so it's 50/50, and switching gains nothing. **The Bayesian answer:** switching *increases* your winning probability. The lecture works out why.

### 2.4 Monty Hall — The Implicit Prior Information (stressed heavily)

"Every step of the game is providing you some information, and most people miss those vital pieces of information."

The three pieces of information that must be carried through every conditional probability:

1. **You chose door $a$ at the very start.** All subsequent probabilities are conditioned on this. (The instructor notes that strictly this should appear as an extra conditioning symbol after a comma in every conditional probability — analogous to the $M$ (model) and $I$ (background information) symbols in the full-form Bayes' theorem written in an earlier lecture.)
2. **Monty knows where the prize is.** He is not guessing.
3. **Rules of the game:** Monty will *never* open (a) the door you chose, nor (b) the door containing the prize — either would end the game immediately.

### 2.5 Monty Hall — Notation and Priors

Label doors $a$, $b$, $c$. Player chooses **door $a$**.

Definitions:
- $P(a)$ = probability that door $a$ hides the prize (similarly $P(b)$, $P(c)$).
- Before anything happens, all doors are equally likely:
$$P(a) = P(b) = P(c) = \tfrac{1}{3}$$
- **Event $B$ (capital B):** "door $b$ gets opened and leads to worthless junk."

**What we want to know** (the instructor's advice from the previous class: *write down as precisely as possible exactly what you want to know*):

$$P(a \mid B) = \text{probability that door } a \text{ has the prize, given that door } b \text{ was opened and revealed junk}$$

### 2.6 Monty Hall — Applying Bayes' Theorem

$$P(a \mid B) = \frac{P(B \mid a)\, P(a)}{P(B)}$$

**Term 1: $P(B \mid a) = \dfrac{1}{2}$**

Reasoning: you chose door $a$, so Monty cannot open $a$. If the prize *is* behind $a$, then both $b$ and $c$ contain junk, and Monty is free to open either one — he picks at random between two options. Hence $1/2$.

**Term 2: $P(a) = \dfrac{1}{3}$** (the prior).

**Term 3: the evidence $P(B)$** — expand over all mutually exclusive ways door $b$ can be opened and reveal junk:

$$P(B) = P(B \mid a)P(a) + P(B \mid b)P(b) + P(B \mid c)P(c)$$

Evaluating each conditional:

- $P(B \mid a) = \dfrac{1}{2}$ (as above).
- $P(B \mid b) = 0$ — **impossible**: event $B$ says door $b$ contains junk, while the conditioning says door $b$ contains the prize. Contradiction.
- $P(B \mid c) = 1$ — **the crucial one.** If the prize is behind $c$, and you have chosen $a$ (so Monty can't open $a$), and Monty won't reveal the prize (so he can't open $c$), then Monty has **no choice at all**: he *must* open door $b$. Probability 1.

Substituting:
$$P(B) = \frac{1}{2}\cdot\frac{1}{3} \;+\; 0\cdot\frac{1}{3} \;+\; 1\cdot\frac{1}{3} = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$$

Therefore:
$$P(a \mid B) = \frac{\frac{1}{2}\cdot\frac{1}{3}}{\frac{1}{2}} = \frac{1/6}{1/2} = \frac{1}{3}$$

**Conclusion:**
$$P(\text{win if you stick}) = \frac{1}{3}, \qquad P(\text{win if you switch to } c) = 1 - \frac{1}{3} = \frac{2}{3}$$

**Switching doubles your probability of winning.**

Interpretive remark: probability here is a **degree of belief** about which door hides the prize, and Bayes' theorem is the machinery for **updating that degree of belief given newly acquired data**. The instructor emphasises this result is unreachable by frequentist reasoning, and that this is what makes the Bayesian approach both powerful and practical.

### 2.7 Monty Hall — Q&A Clarifications (worth reproducing in notes)

A student asked whether $P(B\mid b)=0$ and $P(B\mid c)=1$ represent *Monty's* knowledge. The instructor's answer:

- The analysis is entirely from the **player's perspective**, not Monty's. (From Monty's own perspective there is no probability at all — he knows deterministically where the prize is; all his "probabilities" are 0 or 1.)
- The player has exactly **two observations**:
  1. I chose door $a$.
  2. Door $b$ was opened and contained junk.
- Everything else — that Monty knows the prize location, that he cannot open your door, that he cannot open the prize door — is **prior information encoded in the rules of the game**, which the player also knows.
- Because you chose $a$, Monty's option set shrinks. If the prize is behind $c$, his option set shrinks to a *single* door ($b$), which is exactly why $P(B\mid c) = 1$ rather than $1/2$. **This asymmetry between $P(B\mid a)=1/2$ and $P(B\mid c)=1$ is the entire source of the 1/3 vs 2/3 result.**

### 2.8 Monty Hall — Simulation Check (demonstrated live)

- Search "Monty Hall problem simulator" online — many exist; several versions of the rules.
- Single-trial demo: chose door A, host opened door B (goat), switched, won the car.
- Bulk simulation over **1000 trials**:
  - **Keep the choice:** win $\approx 34\%$, lose $\approx 66\%$
  - **Change the choice:** win $\approx 68\%$, lose $\approx 32\%$
- These match the theoretical $1/3$ and $2/3$.
- **Suggested exercise:** write your own small Python simulator — the rules are very straightforward to implement.

### 2.9 Second Worked Problem — "You Are the Barrister" (stolen cheese)

**Scenario.** A known thief (person with a criminal record) is staying in a lodging house when a piece of (fancy) cheese is stolen.

**Defence lawyer's argument.** Only **1 in 2,500** known thieves who are in lodgings steal cheese from their hosts, i.e.
$$P(S \mid T) = \frac{1}{2500} = 0.0004$$
Therefore (claims the defence) the fact that the man is a known thief is irrelevant and should be ignored by the judge.

**Additional data available to you (the prosecution barrister)** from large criminal records: the general background rate of a theft/burglary occurring in such lodgings is
$$\frac{1}{20{,}000}$$

**Events:**
- $S$ = the lodger-thief stole the cheese
- $\tilde{S}$ = the cheese was stolen by someone *other* than the known thief
- $T$ = the lodger is a known thief
- $C$ = the cheese has (definitely) been stolen

**Hint / the key point.** *What piece of information has the defence lawyer ignored — probably deliberately?* Answer: **that a theft has definitely occurred.** (Analogy given: if there's a dead body, a murder definitely happened.) Every probability must be **conditioned on the fact that the cheese actually was stolen**.

**Quantity to compute:**
$$P(S \mid C, T)$$
— the probability that the lodger is the culprit, given that the cheese *was* stolen and given that he is a known thief.

**Bayes expansion:**
$$P(S \mid C,T) = \frac{P(C \mid S,T)\,P(S\mid T)}{P(C\mid S,T)\,P(S\mid T) + P(C\mid \tilde{S},T)\,P(\tilde{S}\mid T)}$$

**Evaluating each term:**

- $P(C \mid S, T) = 1$ — if the known thief stole the cheese, then the cheese was certainly stolen. (The theft actually happened.)
- $P(S \mid T) = \dfrac{1}{2500} = 0.0004$ — the defence lawyer's own number, taken at face value.
- $P(\tilde{S}\mid T) = 1 - 0.0004 = 0.9996$
- $P(C \mid \tilde{S}, T) = \dfrac{1}{20{,}000}$ — the probability that a cheese theft occurs given the perpetrator is *not* the known thief; we use the general-population background theft rate, which is very small.

**Substituting:**
$$P(S \mid C,T) = \frac{1 \times 0.0004}{1\times 0.0004 \;+\; \frac{1}{20{,}000}\times 0.9996}$$

Numerically: numerator $= 4\times10^{-4}$; second denominator term $= 0.9996/20000 \approx 4.998\times10^{-5}$; so
$$P(S\mid C,T) \approx \frac{4\times10^{-4}}{4.4998\times10^{-4}} \approx 0.889$$

**Conclusion (as stated in class):** the probability comes out **very, very high** — nowhere near the $0.0004$ the defence lawyer claimed. Bayes' theorem lets you accumulate *all* the available information and give each piece its proper weight in your overall belief system, which is how you counter an argument that deliberately or unknowingly suppresses a crucial prior.

**Q&A clarification.** A student asked what $P(C\mid \tilde S, T)$ means. Answer: $C$ is the event "the cheese was stolen"; the tilde means "the theft was *not* done by the known thief". So this is the probability that a random person (not the known thief) committed the cheese theft — hence the very small general-population figure $1/20{,}000$. (Note: the general theft rate and the general cheese-theft rate are being approximated as the same number here.)

---

## 3. Formula Sheet

$$P(\theta \mid \text{data}) = \frac{P(\text{data}\mid\theta)\,P(\theta)}{P(\text{data})}, \qquad P(\text{data}) = \int P(\text{data}\mid\theta)\,P(\theta)\,d\theta$$

Discrete (two-hypothesis) form of the evidence:
$$P(D) = P(D\mid H_1)P(H_1) + P(D\mid H_2)P(H_2)$$

Monty Hall:
$$P(a)=P(b)=P(c)=\tfrac13,\quad P(B\mid a)=\tfrac12,\quad P(B\mid b)=0,\quad P(B\mid c)=1$$
$$P(B)=\tfrac12\cdot\tfrac13+0\cdot\tfrac13+1\cdot\tfrac13=\tfrac12,\qquad P(a\mid B)=\frac{\tfrac12\cdot\tfrac13}{\tfrac12}=\tfrac13,\qquad P(\text{switch wins})=\tfrac23$$

Barrister:
$$P(S\mid C,T)=\frac{P(C\mid S,T)P(S\mid T)}{P(C\mid S,T)P(S\mid T)+P(C\mid\tilde S,T)P(\tilde S\mid T)}=\frac{1\times\frac{1}{2500}}{1\times\frac{1}{2500}+\frac{1}{20000}\times\left(1-\frac{1}{2500}\right)}\approx 0.89$$

---

## 4. Flagged as Important for Exams / Assignments

- **Method flagged repeatedly:** before doing any algebra, **write down as precisely as possible exactly which (conditional) probability you want to compute.** Only then decompose it with Bayes' theorem. The instructor said this is how he ended the previous class and repeated it here.
- **Do not lose the implicit conditioning information.** In Monty Hall, the fact that *you chose door $a$* should formally appear (after a comma) in every conditional probability, exactly like the $M$ (model) and $I$ (prior information) symbols in the full-form Bayes' theorem given in an earlier lecture. Most errors come from dropping this.
- **The evidence term $P(\text{data})$ will be revisited later in the course in the context of model selection.** Understand it now.
- **Homework / self-study (explicitly requested):**
  - Work through the **two additional problems** included in the same posted slide deck (slides will be posted).
  - Go to **Sheldon Ross's book** (referenced in the very first lecture's slides), find the **Bayes' theorem chapter**, and work through **at least the example problems** — plus exercises if possible. The instructor said "these sort of problems you will encounter in your mid-sem."
  - Optional but recommended: write your own **Python Monty Hall simulator**.
- **Next class:** a few more Bayes problems, then beginning the **Central Limit Theorem (CLT)**. Over the next two classes: some CLT, plus more problems.
- Students are invited to email the instructor or raise Bayes' theorem difficulties at the start of the next class (Saturday).