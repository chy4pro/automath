# Task: find a mechanism for statement (S2) below, or prove that the obvious ones fail

This is a genuine open question from an active research effort on a combinatorial identity
(Havel-Hakimi elimination sequences on integer partitions). We want either a real proof attempt of
the statement in §8 below, or a careful accounting of why the natural proof strategies fail. An
honest "I could not do this, and here is exactly where every approach I tried broke" is far more
valuable to us than a fluent-sounding argument that skips a step — a cross-family reviewer checks
load-bearing steps by construction, so an unverified leap will be caught and simply costs us your
run. Give reasoning and a verdict, not confidence language.

**IMPORTANT PROVENANCE NOTE, stated up front because it is the reason this brief exists in its
current form:** an EARLIER brief on this exact shape (called "S2") described it incorrectly — as a
move where two entries of a list are each raised by 1 with the length held fixed. Two independent
engines correctly proved that description is unsatisfiable (impossible at any parameter value).
They were right, and the fault was entirely in how the earlier brief described the shape, not in
the underlying census data. **What follows below is the CORRECTED, self-contained, verbatim
specification, produced by re-deriving the shape directly from source code (not by re-describing
it in prose a second time), specifically so this kind of transcription error cannot recur.**
**Everything from "BEGIN VERBATIM SPEC" to "END VERBATIM SPEC" is quoted unchanged — do not treat
any paraphrase of it (including any prior description you may have seen elsewhere of something
called "S2") as authoritative. This document is authoritative.**

---

## BEGIN VERBATIM SPEC

# w61 -- SHAPE S2, SPECIFIED AT THE LIST LEVEL
**The authoritative, self-contained specification. Any brief that mentions Shape S2 cites or pastes
THIS file and nothing else.**

Written by owner-w61, round 41, 2026-08-23. Machine backing: `problems/wowii/w61_r41_s2spec.py` ->
`problems/wowii/w61_r41_s2spec.out`, `EXIT=0`, `.venv/bin/python3`, elapsed `0.2 s` against an
internal limit of `60 s`, `5 859` diffed `runA`/`runB` calls with `0` disagreements, `25` controls
all firing, `0` defects. Every number below is quoted from that `.out` with the block that printed it.

> ### WHY THIS FILE EXISTS
> `briefs/E01_w61_C1W_angleA.md` and `briefs/E02_...` described Shape S2 as a **`UP2` move** --
> "`B` is `A` with exactly two entries raised by 1", "`A, B` both have the same length `n`". **Two
> independent engines then concluded that S2 as literally stated is unsatisfiable. They were RIGHT
> about the brief.** No list of length `n` with two entries raised by `1` can be `W+(c+1) union
> tail`, at any `c`, ever -- see S4, which proves it rather than counting it. **The 1016 census
> instances are real; the brief's description of them was not.** The defect was in the brief, and
> the brief was planner-authored.

---

## 1. Ground definitions -- assume no other context

A **list** is a finite multiset of non-negative integers, always written weakly decreasing.

**One Havel-Hakimi step** on a list `L`:
1. Sort `L` weakly decreasing as `s`.
2. If `s` is empty or `s[0] = 0`: the run **TERMINATES**. Nothing further happens.
3. Let `d = s[0]` (the **pivot**) and `rest = s[1:]`.
4. If `d > len(rest)`: the run **ABORTS** (`L` is not graphic).
5. Let `blk = rest[:d]` (the `d` largest of the rest). If any entry of `blk` is `0`: the run **ABORTS**.
6. Otherwise the next list is `[x - 1 for x in blk] + rest[d:]`, re-sorted weakly decreasing.

`L` is **terminating** if iterating the step reaches TERMINATE (never ABORT). For a terminating `L`:
- `s(L)` = number of steps taken;
- the terminal list is `0^r` for some `r >= 0`;
- the **residue** is `R(L) := r`.

**Proved and free to use (Lemma C1-X):** `R(L) = n - s(L)` where `n = len(L)`; and `R` is constant
along a trajectory. One step deletes exactly one entry (the pivot).

## 2. The two head blocks -- and the count of maxima that caused the confusion

For an integer `c >= 1`:

```
W+(c) := [c, c, c] ++ [c-1] * c          -- THREE copies of c, then c copies of c-1.   len = c+3
W-(c) := [c, c]    ++ [c-1] * (c+1)      -- TWO   copies of c, then c+1 copies of c-1.  len = c+3
```

Both have length `c + 3`. Sums: `Sum W+(c) = c(c+2)`, `Sum W-(c) = c^2 + 2c - 1`.

> **The "three copies of the new max" is a property of how `W+(c+1)` is BUILT. It is not the result
> of raising entries of `W-(c)`.** `W-(c)` carries only two copies of its maximum, and no amount of
> raising two entries produces three copies of a *larger* value. That observation is correct and it
> is the observation both engines made. It refutes the brief, not the shape.

## 3. Where S1 and S2 come from -- the construction, in full

Let `T = (T_0 >= T_1 >= ... >= T_{k-1})` be a partition into **positive** parts. Define

```
head(T) := W+(T_0)  if sum(T) is even
           W-(T_0)  if sum(T) is odd
L(T)    := head(T) ++ (T_1, ..., T_{k-1})        [re-sorted weakly decreasing]
f(T)    := R(L(T))                            [and f(empty) := 2]
```

The open statement `(MON)` is: **`f(T) - f(T + e_i) in {0, 1}`** for every partition `T` and every
index `i`, where `T + e_i` means "add `1` to part `i`, then re-sort".

**The odd-sum half** (`sum(T)` odd, so `head(T) = W-(T_0)` and `head(T+e_i) = W+(.)`) splits into
exactly two shapes, by whether the raised part is a copy of the maximum:

| shape | condition on `i` | what happens to the head block |
|---|---|---|
| **S1** `head_parity_flip` | `i >= 1` **and** `T_i < T_0` | `W-(c) -> W+(c)` -- same `c`, same length |
| **S2** `max_rises` | `i = 0` **or** `T_i = T_0` | `W-(c) -> W+(c+1)` -- the head block is **REBUILT at c+1** |

*(A third shape is impossible: raising a part never changes the number of parts. A defect check for
it is armed in the script and does not fire.)*

### **S2, stated exactly, at the list level**

Write `c := T_0` and `tail := (T_1, ..., T_{k-1})` (weakly decreasing, entries in `[1, c]`, possibly
empty).

Because the raised part is a copy of the maximum, `U := T + e_i` satisfies `U_0 = c + 1` and
**`U_1, ..., U_{k-1} = tail`, unchanged** -- measured `1016` of `1016`, `w61_r41_s2spec.out` `[2](i)`.
Therefore

```
L  = L(T) = W-(c)   union tail        f(T)      = R(L)
L' = L(U) = W+(c+1) union tail        f(T+e_i)  = R(L')
```

-- measured `1016` of `1016`, `[2](ii)`. **The tail is literally the same list on both sides. The
entire difference between `L` and `L'` is that the head block is thrown away and rebuilt one level
up.**

## 4. S2 IS NOT A `UP2` MOVE. This is a proof, not a census.

`UP2` ("raise two entries by `1`") necessarily preserves length and raises the sum by exactly `2`.

```
len(L') - len(L)  = |W+(c+1)| - |W-(c)| = (c+4) - (c+3) = 1        for EVERY c >= 1
sum(L') - sum(L)  = (c+1)(c+3) - (c^2+2c-1) = 2c + 4 >= 6            for EVERY c >= 1
```

A `UP2` move needs `Delta-len = 0` and `Delta-sum = 2`. **Neither ever holds. There is no `c` at
which the brief's sentence is satisfiable.** QED.

Machine confirmation, `w61_r41_s2spec.out` `[3]`:
- S2 instances that **are** a `UP2` pair: **`0` of `1016`**.
- S2 instances with `len(L') = len(L)`: **`0` of `1016`**.
- S2 instances with `sum(L') = sum(L) + 2`: **`0` of `1016`**.
- **Exclusion list for those three `0`s: none** -- every one of the `1016` S2 instances of block
  `[1]` is tested; nothing skipped, nothing counted elsewhere.
- **The test is not vacuous:** the same positional `UP2` test run on the S1 population fires
  **`3057` of `3057`**. S1 really is a `UP2` move; S2 really is not.

> **Consequence for Candidate Lemma C1-W.** C1-W is a statement about stepping two lists *in
> lockstep* and asking whether their "raise two by `1`" difference survives the step. **That
> statement has no content for S2**, because `L` and `L'` have different lengths and are never
> `UP2`-related at stage 0. **C1-W covers S1 and only S1.** Any brief that puts S2 inside C1-W is
> asking for a proof of a statement about the empty set.

## 5. The census -- every count with its population

Source: `w61_r41_s2spec.out` `[1]`, reproducing `notes/proofs/wowii61_draft.md` S7.54 (c) exactly.

**Population:** every pair `(T, T+e_i)` with `T` a partition, `sum(T)` **odd**, `sum(T) <= 18`, and
`i` any index. Instances where either side's Havel-Hakimi run aborts are skipped on **both** sides
and counted nowhere else.

| shape | instances | `delta = f(T) - f(T+e_i)` histogram | violations of `0 <= delta <= 1` |
|---|---|---|---|
| **S1** `head_parity_flip` | **3057** | `{0: 2473, 1: 584}` | **`0`** |
| **S2** `max_rises` | **1016** | `{0: 836, 1: 180}` | **`0`** |
| total | **4073** | | **`0`** |

**Exclusion list for those `0`s: none.**
The `1016` S2 instances collapse to **`686` distinct `(c, tail)` pairs** (`[6]`) -- a `T` with `m`
copies of its maximum yields the same `(T, U)` for `m` different `i`.

## 6. Worked instances, from the census -- verbatim from `w61_r41_s2spec.out` `[4]`

### Instance A -- the smallest S2 instance in the census (empty tail)
```
T  = (1)          sum(T) = 1 (odd)          c = T_0 = 1     tail = ()
U  = (2)          sum(U) = 2
W-(1)   = [1, 1, 0, 0]
W+(2)   = [2, 2, 2, 1, 1]        <- three copies of the new max 2, then 2 copies of 1
L  = W-(1) union ()  = (1, 1, 0, 0)          |L|  = 4   sum(L)  = 2
L' = W+(2) union ()  = (2, 2, 2, 1, 1)       |L'| = 5   sum(L') = 8
HH(L)  : (1,1,0,0) -> (0,0,0)                                    TERMINATES, s = 1
HH(L') : (2,2,2,1,1) -> (1,1,1,1) -> (1,1,0) -> (0,0)              TERMINATES, s = 3
R(L)  = f(T)     = 3   (n = 4, s = 1, n - s = 3)
R(L') = f(T+e_0) = 2   (n = 5, s = 3, n - s = 2)
delta = 1.        Delta-len = +1,  Delta-sum = +6 = 2c+4.   NOT a UP2 pair.
```

### Instance B -- smallest S2 instance with a non-empty tail, `delta = 0`
```
T  = (2, 1)       sum(T) = 3 (odd)          c = 2          tail = (1)
U  = (3, 1)       sum(U) = 4
W-(2)   = [2, 2, 1, 1, 1]
W+(3)   = [3, 3, 3, 2, 2, 2]     <- three copies of the new max 3, then 3 copies of 2
L  = W-(2) union (1) = (2, 2, 1, 1, 1, 1)       |L|  = 6   sum(L)  = 8
L' = W+(3) union (1) = (3, 3, 3, 2, 2, 2, 1)    |L'| = 7   sum(L') = 16
HH(L)  : (2,2,1,1,1,1) -> (1,1,1,1,0) -> (1,1,0,0) -> (0,0,0)                  s = 3
HH(L') : (3,3,3,2,2,2,1) -> (2,2,2,2,1,1) -> (2,1,1,1,1) -> (1,1,0,0) -> (0,0,0) s = 4
R(L)  = f(T)     = 3   (n = 6, s = 3)
R(L') = f(T+e_0) = 3   (n = 7, s = 4)
delta = 0.        Delta-len = +1,  Delta-sum = +8 = 2c+4.   NOT a UP2 pair.
```

### Instance C -- smallest instance where the raised part is a **repeated** maximum (`i >= 1`), `delta = 1`
```
T  = (1, 1, 1)    sum(T) = 3 (odd)          c = 1          tail = (1, 1)
U  = (2, 1, 1)    sum(U) = 4                -- note U_1,U_2 = (1,1) = tail, unchanged
L  = W-(1) union (1,1) = (1, 1, 1, 1, 0, 0)        |L|  = 6   sum(L)  = 4
L' = W+(2) union (1,1) = (2, 2, 2, 1, 1, 1, 1)     |L'| = 7   sum(L') = 10
HH(L)  : (1,1,1,1,0,0) -> (1,1,0,0,0) -> (0,0,0,0)                              s = 2
HH(L') : (2,2,2,1,1,1,1) -> (1,1,1,1,1,1) -> (1,1,1,1,0) -> (1,1,0,0) -> (0,0,0)  s = 4
R(L)  = f(T)     = 4   (n = 6, s = 2)
R(L') = f(T+e_1) = 3   (n = 7, s = 4)
delta = 1.        Delta-len = +1,  Delta-sum = +6 = 2c+4.   NOT a UP2 pair.
```

**Note on Instance C:** here `tail = (1,1)` contains an entry equal to `c = 1`, i.e. **greater than
`c - 1`**. Any brief asserting "all tail entries `<= c - 1`" excludes this instance and `489` others
(S7 below).

## 7. Corrections that any earlier S2 text must carry

| earlier brief said | truth | measured at |
|---|---|---|
| S2 is a `UP2` move; `A, B` have the same length `n` | **false at every `c`** -- `Delta-len = 1`, `Delta-sum = 2c+4` | `[3]`, and proved in S4 |
| "two of `A`'s entries ... raised so the count of `(c+1)`-copies becomes `3`" | **impossible** -- `W-(c)` has two copies of `c`, and `W+(c+1)` needs three copies of `c+1` | S2, S4 |
| the `6469`-state-pair C1-W census covers "all S1/S2-shaped pairs" | **S1 only.** `w61_r39_monodd.py:237` appends to the lockstep list only when `sh == "S1_head_parity_flip" and sum(T) <= 14`. Actually stepped: the **`709`** S1 instances with `sum(T) <= 14`. Never stepped: the **`331`** S2 instances in that same range | `[5](a)` |
| the census ranges over "partitions of size <= 16" | the lockstep census is `sum(T) <= 14`; the shape census is `sum(T) <= 18` | `[1]`, `[5](a)` |
| a head-block list has `tail` entries `<= c - 1` | `tail = T[1:]` has entries `<= T_0 = c`. Entries equal to `c` occur in **`612` of `3057`** S1 and **`490` of `1016`** S2 instances | `[5](b)`, `[2](vi)` |

## 8. THE STATEMENT TO DISPATCH -- paste this, not a paraphrase

> **(S2).** Let `c >= 1` and let `tail` be a weakly-decreasing list of integers, each in `[1, c]`,
> possibly empty, such that `c + sum(tail)` is **odd**. Put
> ```
> L  = W-(c)   union tail        (length c+3+|tail|)
> L' = W+(c+1) union tail        (length c+4+|tail|)
> ```
> both re-sorted weakly decreasing. **If the Havel-Hakimi runs of `L` and of `L'` both terminate,
> then `0 <= R(L) - R(L') <= 1`.**
>
> Equivalently, via `R = n - s`: `s(L') - s(L) in {1, 2}` -- replacing the head block `W-(c)` by
> `W+(c+1)` adds exactly one or exactly two Havel-Hakimi steps.

**STATUS: CENSUS, NOT A THEOREM.** `686` distinct `(c, tail)` pairs from the range above, **`686`
satisfying, `0` violating**, `0` skipped for aborting (`w61_r41_s2spec.out` `[6]`). **Exclusion list
for that `0`: none among the `686`.** The corrupt companion -- the same claim with `L` and `L'`
swapped -- is violated `180` times, so the test is not vacuous.

**Things an attacking engine must be told and must not have to guess:**
- `L` and `L'` are **two separately constructed lists**, not a list and a perturbation of it. There
  is no "move" from one to the other. Do not look for one.
- The two lists have **different lengths**, so no invariant of the form "the difference is a fixed
  perturbation" can be stated at stage `0`, and stepping them in lockstep does not compare like with
  like. **This is exactly why C1-W does not cover S2 and why S2 still has no mechanism.**
- The equivalent `s`-form (`s(L') - s(L) in {1,2}`) is probably the better attack surface: it is a
  statement about the **lengths of two elimination sequences**, and Hiller (arXiv:2206.05820) makes
  `s` a minimum over all elimination orders of a fixed list -- so a **witness** elimination sequence
  of `L'` of length `<= s(L) + 2`, and one of `L` of length `<= s(L') - 1`, would settle the two
  halves. *(That is a strategy, explicitly not a proof, and nothing in this file discharges it.)*
- `(MON)`, `(RH)`, `(C1-P')`, `C1-M` and C1-W are all **open**. `(UP2)` is **REFUTED in general**.
  Nothing in this file is a theorem except S4's non-`UP2` arithmetic and Lemma C1-X as quoted.

## 9. Reproducing this file from nothing

```
.venv/bin/python3 problems/wowii/w61_r41_s2spec.py > problems/wowii/w61_r41_s2spec.out
```
The `W+/W-/head/L` definitions in that script are **lifted by source text** from
`problems/wowii/w61_r39_monodd.py` rather than retyped, so a transcription drift between the census
and this specification is not possible. The Havel-Hakimi step is likewise lifted from
`problems/wowii/w61_r29_c1audit.py` in two independent implementations, diffed on every call
(`5859` calls, `0` disagreements).

---

## 10. Addendum (same round) -- two further corrections any C1-W brief must carry

**(a) C1-W as usually worded is FALSE on its own census population.**
The wording *"at every state, `B_s` is either equal to `A_s` or again `A_s` with two entries raised
by `1`"* is contradicted by **`51` of the `709`** S1 lockstep pairs (`sum(T)` odd, `sum(T) <= 14`).
**Exclusion list: none.** Smallest instance, printed rather than excluded:

```
A_0 = (5,5,5,4,4,4,4,4,4,1)          B_0 = (5,5,5,5,4,4,4,4,4,2)
stage 3:  A_3 = (3,3,3,2,2,2,1)      B_3 = (3,3,2,2,2,2,2)
          sum(B_3) - sum(A_3) = 0, not 2  ->  not a "raise two by 1" pair
```

The census that reported `0` breaks accepted a state whenever its classifier returned `UP2` **or**
`UNIT_DOWN` **or** `DOM`. **The true statement, and the one to dispatch, is the wider one:** every
joint state is `EQ`, `UP2`, `UNIT_DOWN` or `DOM` -- the difference stays inside the union of the
`(UP2)` shape and the `(RH)`-covered shapes. `EQ` is absorbing.
Source: `problems/wowii/w61_r41_i4.out` `[6]`.

**(b) "If the relation persists and both runs terminate then EQ is forced" is FALSE.**
`158` of the `709` S1 pairs satisfy both hypotheses and never reach `EQ`. **Exclusion list: none.**
The two runs need not terminate at the same stage: `A` reaches `0^r` while `B` still holds
`(1,1,0^{r-2})`, and `B` then takes one further step outside the lockstep. Smallest instance:

```
A_0 = (3,3,2,2,2,2,2)  R = 3        B_0 = (3,3,3,3,2,2,2)  R = 2
(3,3,2,2,2,2,2)/(3,3,3,3,2,2,2) -> (2,2,2,2,1,1)/(2,2,2,2,2,2) -> (2,1,1,1,1)/(2,2,2,1,1)
   -> (1,1,0,0)/(1,1,1,1) -> (0,0,0)/(1,1,0) -> A TERMINAL, B = (0,0)
sum gap g = 2 at every joint stage, including the last.
```

**Correct form.** With `B_0 = A_0` + two entries raised, the relation holding at every joint stage,
and both runs terminating, **exactly one** of:
1. `EQ` occurs at a finite stage; `EQ` is absorbing, so `R(A) = R(B)`, `delta = 0`;
2. `EQ` never occurs; the lockstep ends with `A_s = 0^r` terminal and `B_s = (1,1,0^{r-2})`, so
   `R(A) - R(B) = 1`, `delta = 1`.

A third branch -- `B` terminal while `A` is not -- is **impossible**: `B = A` with two entries
raised, so `B = 0^m` would force two entries of `A` to be `-1`. QED. Verified: `158` of `158`
non-`EQ` pairs land on branch 2 with `delta = 1`; `0` land anywhere else; `0` pairs take the third
branch (`w61_r41_i4.out` `[3]`).

**(c) "Raises sit strictly below the pivot" is not an invariant.** `max(B) = max(A) + 1` occurs at
**`709` of `3736`** `UP2`-related joint states reached from those pairs (`[4]`).

*Reproduce (a)-(c): `.venv/bin/python3 problems/wowii/w61_r41_i4.py`.*

## END VERBATIM SPEC

---

## What we want from you

Section 8 above gives the exact statement — call it **(S2)** — that the census (686 of 686
sampled instances, `sum(T) <= 18`) supports but that has **no mechanism**: `C1-W` (the lockstep
"raise two entries" argument) provably has no content for it (S4), because `L` and `L'` have
different lengths and are not related by any simple perturbation at stage 0.

**We want one of two things:**

1. **A genuine mechanism** — a proof of (S2), by any route. Section 10's note pointing at the
   `s`-form (`s(L') - s(L) in {1,2}`, via constructing explicit witness elimination sequences,
   using Hiller arXiv:2206.05820's characterization of `s` as a MINIMUM over elimination orders)
   is a *suggested* attack surface, explicitly not a proof — feel free to use it, extend it, or
   ignore it for a different approach entirely (e.g. direct induction on `|tail|`, or on `c`, or
   a bijective/injective argument between the elimination sequences of `L` and `L'`).
2. **A precise account of why the obvious approaches fail.** If you attempt an approach and it
   breaks, tell us EXACTLY where and why (not "induction doesn't obviously work" but "the
   inductive step requires X, and here is a specific instance — construct one if you can, from
   the worked examples in S6 as a starting point or a fresh one — where X fails"). If you believe
   none of the standard techniques (direct induction, witness construction via Hiller's
   characterization, bijective argument, generating-function / algebraic approach) can work here,
   say so and explain the specific obstruction each one runs into.

Work through the three worked instances in S6 by hand first (Instance A, B, C) to build intuition
for how `s(L)` and `s(L')` relate before attempting the general case — in particular notice that
Instance A has `delta=1` (empty tail), Instance B has `delta=0` (tail=(1)), and Instance C has
`delta=1` (tail=(1,1), with a tail entry equal to `c`). If your approach naturally explains why
some instances give `delta=0` and others `delta=1`, say so explicitly — that would be strong
evidence of a real mechanism rather than a coincidental bound.

End your answer with exactly one of: **MECHANISM FOUND (state it and the full proof)**,
**PARTIAL MECHANISM (state what you can prove, e.g. a weaker inequality, or the result under an
extra hypothesis, and exactly where the general argument breaks)**, or **NO MECHANISM FOUND — here
is why each approach I tried fails** (list each approach tried and its specific obstruction).
An honest report of failure, with the obstructions named precisely, is exactly as valuable to us
as a proof — do not manufacture a proof that glosses over a step.
