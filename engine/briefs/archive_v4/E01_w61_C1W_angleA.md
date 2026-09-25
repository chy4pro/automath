# Task: attempt a proof of Candidate Lemma C1-W (direct one-step case analysis)

You are being asked for a genuine proof attempt of a specific, precisely-stated combinatorial
claim about the Havel–Hakimi algorithm. Work carefully. If you cannot complete the proof, say so
plainly and report exactly how far you got and what is blocking you — a clear "I could not close
this, here is the obstruction" is much more useful to us than a confident-sounding argument that
skips a case. Do not pad with hedging language; give reasoning and a verdict.

## Background definitions (all you need — this brief is self-contained)

A **list** is a finite multiset of nonnegative integers, written in weakly-decreasing order
`L = (a_1 ≥ a_2 ≥ ... ≥ a_n)`. Write `n = |L|`.

**Havel–Hakimi step.** Given a nonempty list `L = (a_1 ≥ ... ≥ a_n)` with `a_1 > 0`, let
`p = a_1` (the "pivot"). Delete `a_1`. Subtract 1 from each of the next `p` largest remaining
entries `a_2, ..., a_{p+1}`. Re-sort into weakly-decreasing order to get the new list `L'`
(length `n-1`). If `p > n-1`, or if any entry would go negative, the step **ABORTS** (undefined).

**Havel–Hakimi run.** Repeat the step starting from `L =: L_0`, producing `L_1, L_2, ...`, until
either a step aborts, or the current list is all zeros, `0^r` (r zeros, possibly r=0, the empty
list). In the latter case the run **TERMINATES** and `L` is called a **terminating list**. If
`s(L)` is the number of steps taken to reach `0^r`, define the **residue** `R(L) := r`.

**Proved fact you may use freely (Lemma C1-X, already established):** for every terminating list
`L` of length `n`, `R(L) = n - s(L)`. Also: `R` is invariant along a trajectory, i.e.
`R(L_t) = R(L)` for every `t` in a terminating run (since `R(L_t) = (n-t) - s(L_t)` and
`s(L_t) = s(L) - t`).

**Head-block lists.** For an integer `c ≥ 1`, define two specific lists:
```
W+(c) := [c, c, c, c-1, c-1, ..., c-1]     (three copies of c, then c copies of c-1; length c+3)
W-(c) := [c, c, c-1, c-1, ..., c-1]         (two copies of c, then c+1 copies of c-1; length c+3)
```
A **head-block list** is any list of the form `W^ε(c) ∪ tail` (ε ∈ {+,-}), meaning: take
`W^ε(c)`, append an arbitrary further list `tail` all of whose entries are `≤ c-1`, and re-sort
into one weakly-decreasing list.

**The "raise two entries by 1" operation (called `UP2`).** Given a list `L`, choose two
POSITIONS `i ≠ j` in `L` (not necessarily equal values) and form `L'` by adding 1 to the entries
at those two positions, then re-sorting. `L'` is said to be obtained from `L` by "raising two
entries by 1."

**The two concrete shapes actually in play (measured, `w61_r39_monodd.out` block `[1]`,
reproduced here verbatim as the population you must handle):**
- **Shape S1 ("head_parity_flip")**: `A = W-(c) ∪ tail`, and `B` is obtained from `A` by the
  `UP2` move that sends `W-(c) → W+(c)`: one HEAD entry moves `c-1 → c`, and one TAIL entry moves
  `t → t+1` (a fixed entry of `tail`, unchanged in position otherwise). Concretely: if
  `A = [c,c,c-1,c-1,...,c-1] ∪ tail` (2 copies of c, `c+1` copies of `c-1`), then
  `B = [c,c,c,c-1,...,c-1] ∪ tail'` where `tail'` is `tail` with one entry incremented by 1 (and
  one `c-1` promoted to `c` in the head block, i.e. `B = W+(c) ∪ tail'`).
- **Shape S2 ("max_rises")**: `A = W-(c) ∪ tail`, and `B` is obtained from `A` by the `UP2` move
  that sends `W-(c) → W+(c+1)`: the head block changes SIZE (not just a swap within it), i.e.
  `B = W+(c+1) ∪ tail''` for the appropriate `tail''` (two of `A`'s entries equal to `c-1` or `c`
  are raised so that the count of `(c+1)`-copies becomes 3 and `c`-copies becomes `c+1`).

In both shapes, `A` is a head-block list and `B = A` with exactly two entries raised by 1 (an
`UP2` pair), and `A, B` both have the same length `n`.

## The claim to prove: Candidate Lemma C1-W

> **(C1-W).** Let `(A_0, B_0)` be any pair where `A_0` is a head-block list (as defined above)
> and `B_0` is obtained from `A_0` by one `UP2` move of shape S1 or S2 (as defined above). Run
> the Havel–Hakimi step on `A_0` and on `B_0` **in lockstep**, producing `A_0, A_1, A_2, ...` and
> `B_0, B_1, B_2, ...` (apply the step independently to each list at each stage `s`). Then **at
> every stage `s` for which both `A_s` and `B_s` are defined**, exactly one of the following
> holds:
> 1. `A_s = B_s` (as multisets), and once this happens it holds forever after (`A_t = B_t` for
>    all `t ≥ s`) — call this **EQ**, and note it is **absorbing**.
> 2. `B_s` is again obtainable from `A_s` by raising exactly two entries of `A_s` by 1 (an `UP2`
>    pair, not necessarily at the same positions or values as at stage 0).

Equivalently: the relationship "`B` = `A` with two entries raised by 1" is **preserved by one
simultaneous Havel–Hakimi step on both lists**, until (if ever) the two lists become equal, after
which they stay equal.

**Why this matters (context only, not something to re-derive):** if C1-W holds, it combines with
already-proved facts (residue is a trajectory invariant, and a proved terminal-case computation
showing that if `A,B` run all the way to termination while staying `UP2`-related, they must end at
`A = 0^r` vs `B = (1,1,0^{r-2})`, giving `R(A) - R(B) = 1` exactly) to prove a monotonicity
theorem about Havel–Hakimi residues. You do not need any of that background to attack C1-W itself
— it is a pure, self-contained statement about one Havel–Hakimi step.

**Measured evidence (a census, not a proof — this is what you are asked to upgrade to a proof):**
tested on 6,469 `(A_s, B_s)` state pairs generated by running the above lockstep procedure
starting from all S1/S2-shaped `(A_0,B_0)` pairs over head-block lists built from partitions of
size ≤ 16 (with tails ranging over all valid combinations in that range): 0 breaks of the
invariant found.

## What we want from you

**Angle A — a direct, one-step case analysis.** Attempt to prove: for ANY pair `(A, B)` where `A`
is a head-block list and `B` is `A` with two entries raised by one (of shape S1 or S2, or more
generally any `UP2` pair whose "raised" entries lie in the head block or in the transition between
head block and tail — describe precisely which cases you need), applying ONE Havel–Hakimi step to
each produces a new pair `(A', B')` that again satisfies "`A'=B'`" or "`B'` is `A'` with two
entries raised by 1." Do this by directly tracking: what is the pivot of `A` (its largest entry)?
What is the pivot of `B`? Since `B` differs from `A` in only two positions, the pivot of `B` is
either equal to the pivot of `A`, or is one of the two raised entries. Enumerate the resulting
finitely many cases (which entries get subtracted from, whether the two raised positions are
among the "first p" entries that get decremented, etc.) and show each case lands back in
"equal" or "two entries raised by 1."

Please structure your answer as: (1) a precise enumeration of the cases your induction needs,
(2) the argument for each case, (3) an explicit statement of which cases you were NOT able to
close, if any, and why. End with one of: **PROOF COMPLETE**, **PROOF INCOMPLETE (state exactly
which case fails or is unresolved)**, or **CONJECTURE APPEARS FALSE (give an explicit
counterexample pair (A,B) and the step that breaks it)**.
