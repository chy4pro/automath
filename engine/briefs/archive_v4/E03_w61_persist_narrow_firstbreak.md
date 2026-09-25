# Task: prove a step-invariance statement about two Havel–Hakimi runs stepped in lockstep

**Brief E03 (RESTATED 2026-08-23 by owner-w61, round 43).** The previous framing of E03 —
*"attack the contrapositive on the terminal signature `0^r` vs `(1,1,0^{r−2})`"* — is **STRUCK as
obsolete**, for reasons recorded at the end of this file (§8). What is below is a different target.
Nothing this line holds is withheld: every definition, every proved lemma, every measurement and
every known counterexample relevant to the question is written out here.

This is a genuine open question from an active research effort in graph/partition combinatorics.
Everything you need is in this file. **You have no internet access and no access to any repository —
do not cite a source you cannot reconstruct here.** We want a real proof attempt. **If you cannot
prove it, say so plainly and say exactly where you got stuck** — "I could not close it, and here is
the precise step that resisted" is a valued, useful answer, not a failure. The failure mode we
specifically guard against is a **fluent wrong proof**: a confident, fully-worked derivation that
does not survive reconstruction. Everything you send back is checked line by line by an independent
reviewer who rebuilds each load-bearing step. **Give reasoning and an honest verdict, not confidence
language.**

---

## 1. The process (verbatim; assume no other context)

Work with finite lists of non-negative integers, treated as multisets and always written weakly
decreasing. One **Havel–Hakimi step** on a list `L`:

```
sort L weakly decreasing  ->  s
if s is empty or s[0] == 0 :  TERMINAL   (the run stops here)
d    := s[0]                              (the PIVOT)
rest := s[1:]
if d > len(rest) :            ABORT       (the list is not graphic)
blk  := rest[:d] ;  tail := rest[d:]
if any entry of blk is 0 :    ABORT
next := sort_desc( [x-1 for x in blk] + tail )
```

A run **terminates** if it reaches `TERMINAL` without ever hitting `ABORT`. For a terminating list:

* `s(L)` := the number of steps taken,
* `R(L)` := the number of entries remaining at `TERMINAL` (they are all `0`). `R` is the **residue**.

**Note the step deletes exactly one entry — the pivot — and subtracts `1` from `d` other entries.**

### Lemma C1-X (PROVED; elementary and standard, given here because it is used constantly)
For a terminating list `L` of length `n`, with pivots `p_1,…,p_s`:
> **(i)** `R(L) = n − s(L)`.  **(ii)** `2·(p_1 + … + p_s) = sum(L)`.

*Proof.* (i) One step deletes exactly one entry and the run stops precisely when every remaining
entry is `0`; after `s` steps the list has `n − s` entries, all zero. (ii) A step with pivot `p`
deletes an entry equal to `p` and subtracts `1` from `p` other entries, so `sum` drops by exactly
`2p`; the run ends at `sum = 0`. ∎

> **Corollary (used everywhere below).** `R` is **constant along a trajectory**:
> `R(L_t) = (n − t) − s(L_t) = R(L)`.

---

## 2. The family of lists this question is about

For an integer `c ≥ 1` define the two **head blocks**

```
W+(c) = [c]*3 ++ [c-1]*c        length c+3,   sum c(c+2)
W-(c) = [c]*2 ++ [c-1]*(c+1)    length c+3,   sum c^2+2c-1
```

For a partition `T = (T_0 ≥ T_1 ≥ … ≥ T_{k−1})` with `c := T_0`, set

```
head(T) = W+(c) if sum(T) is EVEN,   W-(c) if sum(T) is ODD
L(T)    = head(T) ++ (T_1, …, T_{k-1})          ("a head-block list")
f(T)    = R( L(T) )
```

The statement the whole effort is reducing is

> **(MON)**  `f(T) − f(T + e_i) ∈ {0,1}` for every part index `i` — raising one part of `T` by `1`
> never raises `f`.

Raising a part flips the parity of `sum(T)`, so the head block switches branch. This splits (MON):

* **`sum(T)` EVEN** — `L(T+e_i)` is `L(T)` with one unit transferred **down** (`W+→W−` lowers a head
  entry, the tail entry rises). Separate statement, **not this brief.**
* **`sum(T)` ODD** — `L(T+e_i)` is `L(T)` with **two entries raised by `1`**. **This brief.**

Inside the odd half there are exactly two shapes:

* **S1** — the raised part is **not** the maximum. Then `c` is unchanged, `W−(c) → W+(c)` raises one
  head entry, and the tail entry `T_j → T_j + 1` is the other. **Same length, sum `+2`.**
* **S2** — the raised part **is** the maximum (or a copy of it). Then `c → c+1` and
  `L = W−(c) ++ tail`, `L′ = W+(c+1) ++ tail`. These have **different lengths** and sums differing
  by `2c+4`, so `(L, L′)` is **never** a "raise two by 1" pair. **PROVED**, and it is arithmetic:
  `|W+(c+1)| − |W−(c)| = (c+4) − (c+3) = 1` and `ΣW+(c+1) − ΣW−(c) = (c+1)(c+3) − (c²+2c−1) = 2c+4 ≥ 6`.

### Lemma S2-STEP (PROVED — this converts S2 into the same shape as S1)
For every `c ≥ 1` and every weakly decreasing `tail` with entries in `[0,c]`, one Havel–Hakimi step
on `L′ = W+(c+1) ++ tail` neither terminates nor aborts, and produces

```
L'_1  =  L  with exactly TWO entries equal to c-1 replaced by c,      L = W-(c) ++ tail
```

so `len(L'_1) = len(L)` and `sum(L'_1) = sum(L) + 2`.

*Proof.* `W+(c+1) = [c+1]³ ++ [c]^{c+1}` and every entry of `tail` is `≤ c`, so the pivot is
`d = c+1` and, with `m := #{j : tail_j = c}`,
`rest = [c+1]² ++ [c]^{c+1+m} ++ tail_{<c}`, of length `c+3+|tail| ≥ c+1 = d`, so no length abort.
`blk = rest[:c+1] = [c+1]² ++ [c]^{c−1}` (this uses `c+1+m ≥ c−1`, true for all `c ≥ 1`), and every
entry of `blk` is `≥ c ≥ 1`, so no zero abort. Subtracting `1` gives `[c]² ++ [c−1]^{c−1}`; the
untouched remainder is `[c]^{2+m} ++ tail_{<c}`. As multisets
`L'_1 = {c: 4+m} ∪ {c−1: c−1} ∪ tail_{<c}` and `L = {c: 2+m} ∪ {c−1: c+1} ∪ tail_{<c}`, which differ
exactly by moving two copies of `c−1` up to `c`. `L` carries `c+1 ≥ 2` copies of `c−1`, so the move is
always available. ∎

*(The `c = 1` boundary is inside the lemma: there `c−1 = 0` and the two raised entries are the two
zeros of `W−(1) = [1,1,0,0]`. Worked: `L′ = W+(2) = (2,2,2,1,1) → (1,1,1,1) = L'_1`, `L = (1,1,0,0)`.)*

Because `R` is a trajectory invariant, `R(L′) = R(L'_1)`. **So both shapes reduce to the same
question about a pair of equal-length lists differing by "raise two entries by `1`".**

---

## 3. The lockstep, and the classifier

Given a pair `(A_0, B_0)` where `B_0` is `A_0` with two entries raised by `1`, step **both** lists,
one step each, in **lockstep**: `A_{t+1} = step(A_t)`, `B_{t+1} = step(B_t)`. The lockstep ends when
either list reaches `TERMINAL` or `ABORT`, or when `A_t = B_t` (call this **EQ**).

Since `R` is a trajectory invariant, `R(A_0) − R(B_0) = R(A_t) − R(B_t)` at every joint stage — so the
quantity (MON) is about can be read off **any** joint state.

`relation(A,B)` classifies how `B` differs from `A` (`A`, `B` sorted decreasing):

| value | exact condition |
|---|---|
| `EQ` | `A == B` as multisets |
| `UP2` | `len(A) = len(B)`, `sum(B) = sum(A)+2`, and there are positions `x ≤ y` with `B = sort(A with A[x]+1 and A[y]+1)` |
| `UNIT_DOWN` | `len` equal, `sum` equal, every partial sum of `B` is `≤` that of `A`, and the multiset difference is `{d₁,d₂}` down / `{u₁,u₂}` up pairing as `u = d − 1` twice with `d₁ − 1 ≥ d₂ + 1` — i.e. **one unit moved from a larger entry to a smaller one** |
| `DOM` | `len` equal, `sum` equal, every partial sum of `B` is `≤` that of `A`, but not the `UNIT_DOWN` shape |
| `OTHER` | none of the above |

`EQ` is **absorbing**: the step is a function of the multiset alone, so once `A_t = B_t` the two
trajectories coincide forever and `R(A_0) = R(B_0)`.

### Lemma C1-Y (PROVED)
For `r ≥ 2`: `R(0^r) = r` and `R((1,1,0^{r−2})) = r − 1`, hence the difference is exactly `1`.
*Proof.* `0^r` is already `TERMINAL`, so its residue is `r`. For `(1,1,0^{r−2})` the pivot is `1`; the
step deletes it and subtracts `1` from the other `1`, leaving `0^{r−1}`, which is terminal. So
`s = 1` and `R = r − 1` by C1-X (i). ∎

### The two-branch theorem (PROVED)
Let `B_0` be `A_0` with two entries raised by `1`, suppose **the difference is `UP2` at every joint
state**, and suppose both runs terminate. Then **exactly one** of:

1. **`EQ` occurs** at a finite stage — then `delta := R(A_0) − R(B_0) = 0`;
2. **`EQ` never occurs** — then the lockstep ends with `A_s = 0^r` terminal and
   `B_s = (1,1,0^{r−2})`, and Lemma C1-Y gives `delta = 1`.

The third branch — `B` terminal while `A` is not — is **empty by proof**: `B = A` with two entries
raised, so `B = 0^m` would force two entries of `A` to equal `−1`. ∎

> **Read the hypothesis carefully. The theorem needs `UP2` at every joint state — the NARROW
> relation. That is what this brief asks you to prove.**

---

## 4. ⚠️ THE STATEMENT TO PROVE

> ### (PERSIST-NARROW)
> Let `A_0 = L(T)` and `B_0 = L(T+e_i)` be a head-block pair of the odd half in shape **S1**
> (equivalently: `A_0 = W−(c) ++ tail`, `B_0 = W+(c) ++ tail'` where `tail'` is `tail` with one entry
> raised by `1`), or the S2-derived shifted pair `(L, L'_1)` of Lemma S2-STEP. Step them in lockstep.
> Then **either the lockstep reaches `EQ`, or `relation(A_t, B_t) = UP2` at every joint state up to
> the exit.**

Equivalently, and this is the form we believe is the right handle:

> ### (G2) — the same statement, localized to one step
> Put `g_t := sum(B_t) − sum(A_t)`. By Lemma C1-X (ii) applied to one step,
> ```
> g_{t+1} = g_t − 2·( p_B(t) − p_A(t) )          where p_A(t) = max(A_t), p_B(t) = max(B_t)
> ```
> and `g_0 = 2`. Prove:
> **(G2-a)** at every joint state, `p_B(t) − p_A(t) ∈ {0, g_t/2}` — i.e. the pivots are equal, except
> that when `g_t = 2` the `B`-pivot may be one larger. Consequently `g_t ∈ {0,2}` for all `t`, `g` is
> non-increasing, and it drops `2 → 0` at most once.
> **(G2-b)** while `g_t = 2` the difference is `UP2`; when `g_t = 0` it is a unit transfer down.
>
> **(G2-a) + (G2-b) ⟹ (PERSIST-NARROW)**, via the already-proved Lemma G0-EXIT below.

### Lemma G0-EXIT (PROVED — supplied, do not re-derive)
If at some joint state `g_t = 0` and the relation is `UNIT_DOWN` or `DOM`, then `A_t` and `B_t` have
**equal sums and equal lengths**. Any exit other than `EQ` requires one of the two lists to be
`TERMINAL`, i.e. all-zero. All-zero forces its sum to be `0`, hence the other list also has sum `0`,
hence (equal length) it is all-zero too — so the two are equal and the exit is `EQ`. **Therefore once
`g = 0`, the lockstep can only exit at `EQ`** (given that neither run aborts). ∎

**So the whole of (PERSIST-NARROW) reduces to the local pivot statement (G2-a) plus (G2-b).**

---

## 5. What is MEASURED (so you attack the argument, not data we already have)

These are censuses over stated finite populations. **They are not proofs and are not what you are
asked to check.** They are given so you do not spend effort rediscovering agreement.

**Population P1 — the `709` S1 head-block pairs** (`sum(T)` odd, `sum(T) ≤ 14`, raised part not the
maximum, both residues defined). Exclusions: none.

| measured | result |
|---|---|
| lockstep exits | `EQ` **551**, `A` terminal **158**, nothing else (no abort, no runaway) |
| pairs that ever leave `{EQ, UP2}` | **51** — every one into `UNIT_DOWN`, and **every one of the 51 goes on to reach `EQ`** |
| pairs covered by branch 1 / branch 2 / neither | **551 / 158 / 0** |
| `g` values seen over all `4 352` joint states | `{0: 616, 2: 3736}` — **no other value** |
| `p_B − p_A` over all `3 643` stepped joint states | `{0: 3092, 1: 551}` — **never negative, never ≥ 2** |
| cross-tab `(g_t, p_B − p_A)` | `{(0,0): 65, (2,0): 3027, (2,1): 551}` — the `+1` pivot gap occurs **only** at `g = 2` |
| cross-tab `(g_t, relation)` | `{(0,'UNIT_DOWN'): 65, (2,'UP2'): 3578}` — **`DOM` never occurs**, and `OTHER` never occurs |
| pairs where `g` returns to a nonzero value after reaching `0` | **0** |

**Population P2 — the `686` S2-derived shifted pairs `(L, L'_1)`.** Relation-persistence holds
**686 of 686**; joint-state relations over the whole run `{EQ: 626, UP2: 3394}`, i.e. **0 of 4 020
joint states need `UNIT_DOWN` or `DOM` at all**; delta `{0: 626, 1: 60}`. Exclusions: none.

> **A warning that matters.** The general "raise two entries by `1`" statement is **FALSE** without
> the head block. Over all terminating partitions of `N ∈ [2,16]`, `R(L′) ≤ R(L)` fails on **97** of
> **732** distinct such pairs. Minimal counterexamples, given so you do not "prove" something false:
> ```
> (2,2,2,1,1)   -> (3,3,2,1,1)     residue 2 -> 3
> (2,2,1,1,1,1) -> (3,3,1,1,1,1)   residue 3 -> 4
> (3,2,2,2,1)   -> (4,3,2,2,1)     residue 2 -> 3
> ```
> **Any proof of (PERSIST-NARROW) must use the head-block structure of `A_0`.** A proof that never
> uses it is wrong, and the three lists above will show where.

---

## 6. What has already been tried and did not work (told so you do not repeat it)

1. **"Both sums reach `0`, so `g = 0` at the end."** FALSE as an argument: the two runs need not
   terminate at the same stage. On `158` of the `709` pairs `A` reaches `0^r` while `B` still holds
   `(1,1,0^{r−2})`; `g ≡ 2` throughout and is simply evaluated at the last **joint** stage. Smallest:
   ```
   stage 0  A=(3,3,2,2,2,2,2)  B=(3,3,3,3,2,2,2)   g=2
   stage 1  A=(2,2,2,2,1,1)    B=(2,2,2,2,2,2)     g=2
   stage 2  A=(2,1,1,1,1)      B=(2,2,2,1,1)       g=2
   stage 3  A=(1,1,0,0)        B=(1,1,1,1)         g=2
   stage 4  A=(0,0,0)          B=(1,1,0)           g=2
   stage 5  A TERMINAL, B=(0,0) -- the lockstep ends here
   ```
2. **"The two raised entries sit strictly below the pivot, so `p_B = p_A`."** **Not an invariant**:
   over the `3 736` `UP2`-related joint states reachable from population `P1` (this count includes
   each pair's final joint state), `max(B) = max(A) + 1` at `709` of them; over the `3 578` `UP2`
   states that are actually *stepped* (final states excluded, which is the population of §5's
   cross-tab), it is `551` of them. Both counts are of the same phenomenon on two populations that
   differ by exactly the `158` final states. **(G2-a) is the correct weakening** — the gap is `0` or
   `1`, never more, never negative — and that is exactly what is unproved.
3. **"The maximum occurs once or twice, and that is what excludes the counterexamples."** REFUTED as
   stated: `13` of the `97` counterexample lists have max-multiplicity `≥ 3`, and `12` of those
   contain a head block. **The real exclusion is WHICH pair of entries is raised**, not how many
   copies of the maximum exist. In an S1 pair one raised entry is in the head block (`c−1 → c`) and
   the other is a tail part; in an S2-derived pair **both** raised entries are copies of `c−1` inside
   the head block.

---

## 7. What to send back

1. A proof of **(G2-a)**, or of **(G2-b)**, or of **(PERSIST-NARROW)** directly — whichever you can
   close. Partial credit is real: **(G2-a) alone is worth having**, and so is a proof restricted to
   the S2-derived family (where `DOM` and `UNIT_DOWN` never occur at all).
2. If you cannot close it: the precise step that resisted, stated so someone else can start there.
3. If you believe the statement is **false**, an explicit `(c, tail, i)` with the joint state at which
   it fails, and the two full Havel–Hakimi trajectories. A counterexample is as valuable as a proof —
   **but check it against §5's measured populations first**, because a counterexample inside `P1` or
   `P2` contradicts a completed census and is far more likely to be an arithmetic slip.
4. Do **not** report agreement with §5's numbers as a result. They are already in hand.

---

## 8. Why the previous E03 framing was struck (recorded for the file, not part of your task)

The earlier E03 asked to *"attack the contrapositive on the terminal signature `0^r` vs
`(1,1,0^{r−2})`"*. That target no longer exists:

* the terminal-signature dichotomy is **no longer conjectural** — it is the proved two-branch theorem
  of §3, including the proof that the third branch is empty;
* the statement the old brief called "C1-W" is **false as it was worded** (it asserted "`EQ` or two
  entries raised" at every state, which fails on `51` of `709` pairs) — so an engine sent at it would
  have been sent at a false sentence;
* what the line actually lacks is the **hypothesis** of that theorem, not its conclusion; and the
  hypothesis that was being called open (`the difference stays in {EQ, UP2, UNIT_DOWN, DOM}`) is
  **weaker than the one the theorem needs** (`UP2` at every state). (PERSIST-NARROW) is the first
  written statement of the hypothesis that actually closes the argument.
