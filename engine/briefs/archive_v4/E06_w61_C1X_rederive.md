# Task: independent re-derivation / adversarial check of Lemma C1-X

This is a verification task, not a hard open problem: we have a short proof of a lemma already in
hand, and we want you to independently re-derive it from scratch (without looking at "our" proof,
since we are not giving it to you — only the statement and the definitions) and then compare. Your
job is to either (a) produce your own correct proof and confirm the statement, or (b) find a
genuine counterexample or gap, if the statement as given is actually false or needs an extra
hypothesis. Be precise about edge cases (empty lists, length-1 lists, lists that are already all
zero, etc.) — that is exactly the kind of place a lemma like this can go wrong, and exactly the
kind of place we want an independent check to catch.

Give reasoning and a plain verdict. If you find the statement true but only under an extra
hypothesis we didn't state, say exactly what hypothesis is missing and why.

## Definitions (self-contained)

A **list** is a finite multiset of nonnegative integers, written in weakly-decreasing order
`L = (a_1 ≥ a_2 ≥ ... ≥ a_n)`, `n = |L| ≥ 0` (the empty list, `n=0`, is allowed).

**Havel–Hakimi step.** If `L` is empty or `a_1 = 0` (i.e. `L = 0^n`), the run has already reached
its terminal state — do not apply a step. Otherwise (`a_1 > 0`): let `p = a_1` ("the pivot").
Delete the entry `a_1`. Subtract 1 from each of the next `p` largest of the remaining `n-1`
entries. Re-sort into weakly-decreasing order to get `L'`, a list of length `n-1`. **The step
ABORTS** if `p > n-1` (not enough remaining entries to subtract from) or if subtracting 1 from
some chosen entry would make it negative (this can't actually happen if you always pick the `p`
LARGEST remaining entries and `p ≤ n-1`, but state explicitly whether/why this case is vacuous in
your write-up).

**Havel–Hakimi run.** Starting from `L_0 := L`, repeatedly apply the step: `L_0, L_1, L_2, ...`.
The run **TERMINATES** if at some point the current list equals `0^r` (`r` zeros, `r ≥ 0`,
including possibly `r=0`, the empty list) — no further steps are applied once this state is
reached. It **ABORTS** if some step along the way aborts per the rule above. Let `s(L)` be the
number of steps actually taken before termination (so `L_{s(L)} = 0^r` for some `r`), defined only
when the run terminates. Define the **residue** `R(L) := r = |L_{s(L)}|` (the number of entries
remaining at termination, all necessarily 0).

**Pivots.** If the run from `L` terminates in `s(L)` steps, let `p_1, p_2, ..., p_{s(L)}` be the
successive pivot values used (`p_t = a_1` of `L_{t-1}`, the largest entry at step `t`).

## The statement to re-derive: Lemma C1-X

> **(i)** For every terminating list `L` of length `n`: `R(L) = n - s(L)`.
>
> **(ii)** For every terminating list `L`: `2 · Σ_{t=1}^{s(L)} p_t = sum(L)`, where `sum(L)` is
> the sum of all entries of `L` (equivalently of `L_0`) and `p_1,...,p_{s(L)}` are the pivots as
> defined above.

**Measured evidence supporting it (not a proof, just what has been checked computationally):**
209 terminating lists, built from all partitions of every `N` in `[2,16]`, 0 counterexamples to
either (i) or (ii). Also checked indirectly on 732 related list pairs via the identity
`R(L) - R(L') = s(L') - s(L)`, 0 failures.

## What we want from you

1. Give your own from-scratch proof of (i). (Hint direction, but derive it yourself: think about
   how many entries the list loses per step, and what "terminates" means in terms of list length
   versus the all-zero state.)
2. Give your own from-scratch proof of (ii). (Hint direction, but derive it yourself: think about
   how much the total sum of the list changes in one step, as a function of the pivot `p`.)
3. Explicitly check the boundary cases: `L` = the empty list (`n=0`); `L` already `0^r`
   (`s(L)=0`); a list of length 1, e.g. `L=(0)` vs a list that would immediately abort, e.g.
   `L=(1)` (n=1, pivot p=1, but there are 0 remaining entries to subtract from — does this abort,
   or is it a degenerate case where "subtract from the next p=1 largest remaining entries" is
   vacuously fine because there's nothing to check? Resolve this precisely and say which reading
   the statement needs to be true.)
4. State plainly: is the lemma TRUE AS STATED (with your own proof), TRUE BUT NEEDS AN EXTRA
   HYPOTHESIS (state which), or FALSE (give an explicit counterexample list `L` and show the
   computation)?

End with exactly one of: **CONFIRMED (proof given)**, **CONFIRMED WITH AN ADDED HYPOTHESIS (state
it)**, or **REFUTED (explicit counterexample)**.
