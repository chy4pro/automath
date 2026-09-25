# Task: attempt a proof of Candidate Lemma C1-W (angle: pivot/algebraic tracking via the sum identity, NOT direct case listing)

This is a proof-attempt task on the same target as a parallel independent attempt, but we want a
genuinely DIFFERENT strategy from you: instead of directly enumerating the finitely many ways two
raised entries interact with one Havel–Hakimi step (a combinatorial case analysis), we want you to
try an **algebraic / invariant-tracking** approach centered on the pivot and the sum identity
below. If you find yourself doing a long case enumeration on head-block positions, that is fine
too if it is the route that actually closes the proof — but please attempt the algebraic route
first and report honestly if it does not get you there.

If you cannot complete the proof, say so plainly and describe exactly where the argument breaks.
We would much rather have an honest "I could not close this, here is the obstruction" than a
proof sketch that hides a gap. Give reasoning and a verdict, not confidence language.

## Background definitions (self-contained — identical framework to the direct-case-analysis version)

A **list** is a finite multiset of nonnegative integers `L = (a_1 ≥ ... ≥ a_n)`.

**Havel–Hakimi step.** Given `L = (a_1 ≥ ... ≥ a_n)` with `a_1 > 0`: let `p = a_1` ("the pivot").
Delete `a_1`; subtract 1 from each of the next `p` largest remaining entries; re-sort to get `L'`
(length `n-1`). If `p > n-1` or any entry would go negative, the step ABORTS.

**Havel–Hakimi run / terminating list / residue `R(L)`.** Repeat the step until either it aborts,
or the list reaches `0^r` (all zeros, `r ≥ 0` of them) — in the latter case the run TERMINATES and
`R(L) := r`. If `s(L)` is the number of steps to termination and `n = |L|`, you may use as an
**already-proved fact**:

> **Lemma C1-X.** `R(L) = n - s(L)`, and `2 · Σ_{t=1}^{s(L)} p_t = sum(L)`, where `p_1, ..., p_s`
> are the successive pivots used along the run. (Proof: each step deletes the pivot entry `p` and
> subtracts 1 from `p` other entries, so the total sum drops by exactly `2p` per step; the run
> ends at sum 0. And each step removes exactly one entry, so after `s` steps `n-s` entries remain,
> all zero.)

**Head-block lists.** For `c ≥ 1`:
```
W+(c) := [c, c, c, c-1, ..., c-1]   (three c's, then c copies of c-1; length c+3)
W-(c) := [c, c, c-1, ..., c-1]      (two c's, then c+1 copies of c-1; length c+3)
```
A **head-block list** is `W^ε(c) ∪ tail` for `ε ∈ {+,-}`, `tail` any list with all entries `≤ c-1`.

**`UP2` move.** Given `L`, pick two POSITIONS and add 1 to each entry there, re-sort, to get `L'`.
`L'` is "`L` with two entries raised by 1."

**The population you must handle (measured, `w61_r39_monodd.out` block `[1]`):**
- **S1 ("head_parity_flip")**: `A = W-(c) ∪ tail → B` via `W-(c) → W+(c)`: one HEAD entry
  `c-1 → c`, one TAIL entry `t → t+1`.
- **S2 ("max_rises")**: `A = W-(c) ∪ tail → B` via `W-(c) → W+(c+1)`: the head block changes
  SIZE.

## The claim to prove: Candidate Lemma C1-W

> Let `(A_0, B_0)` be a pair with `A_0` a head-block list and `B_0 = A_0` with two entries raised
> by 1 (shape S1 or S2). Run the Havel–Hakimi step on `A_0` and `B_0` in lockstep (independently,
> synchronized by step count), giving `A_0,A_1,...` and `B_0,B_1,...`. Then at every stage `s`
> where both are defined: either `A_s = B_s` (and this persists for all later stages — EQ is
> absorbing), or `B_s` is again `A_s` with two entries raised by 1 (not necessarily the same
> positions/values as before).

**Measured evidence (census, not proof): 6,469 lockstep state pairs checked, 0 breaks.**

## What we want from you — Angle B: the algebraic / pivot-tracking route

Try to build the induction not by hand-enumerating head-block positions, but by using the
following structural facts as levers:

1. **The sum gap is exactly 2, always.** `sum(B_0) = sum(A_0) + 2` (two entries raised by 1 each).
   If `A_s, B_s` are both defined and still `UP2`-related at stage `s`, is `sum(B_s) - sum(A_s)`
   forced to stay `2` until they merge? Try to prove this as an invariant of the induction
   (using Lemma C1-X's sum-drop-per-step fact: each step drops the sum by `2p` for that list's own
   pivot `p` — so if `A_s` and `B_s` ever use DIFFERENT pivots at some step, the sum-gap of 2 could
   change; part of your job is to show it does not, or to find exactly when it can).
2. **Constrain the pivot of `B_s` in terms of the pivot of `A_s`.** Since `B_s` differs from `A_s`
   in at most 2 positions, argue about how large `B_s`'s maximum entry can be relative to `A_s`'s:
   it is either identical to `A_s`'s pivot, or it is one of the (at most two) raised entries. Use
   this together with (1) to pin down the pivot of `B_s` almost forced by the pivot of `A_s` and
   the invariant "the two lists differ in a bounded, structured way."
3. **Try to show EQ is absorbing directly from the step definition**, i.e. that if `A_s = B_s` as
   multisets then the Havel–Hakimi step is a well-defined function of the multiset alone, so
   `A_{s+1} = B_{s+1}` automatically. (This part should be easy — do it first as a warm-up and
   confirm it in one line, then move to the harder non-EQ branch.)
4. Only fall back to enumerating explicit head-block cases if the algebraic route genuinely
   cannot be pushed through — and if you do, say explicitly that you switched strategies and why.

Structure your answer as: (1) which invariant(s) you tried to carry through the induction, (2)
where the algebraic argument succeeds or where it needs a case split it cannot avoid, (3) the
full argument or the precise point of failure. End with exactly one of: **PROOF COMPLETE**,
**PROOF INCOMPLETE (state exactly which step/case is unresolved)**, or **CONJECTURE APPEARS
FALSE (explicit counterexample pair and the step that breaks it)**.
