# Task: attempt to prove statement (RH) about Havel–Hakimi residues, via an explicit witness construction

We want a genuine proof attempt of a precise, self-contained claim about the Havel–Hakimi
algorithm on degree sequences. If you cannot complete it, say so plainly, and report exactly
which part of the construction you could not finish or verify — we would much rather have a
clear "here is exactly where I got stuck" than a proof sketch with a hidden gap. Give reasoning
and a verdict, not a confidence rating.

## Background (self-contained)

A **list** is a finite multiset of nonnegative integers, written `L = (a_1 ≥ a_2 ≥ ... ≥ a_n)`.

**Havel–Hakimi step.** Given `L = (a_1 ≥ ... ≥ a_n)`, `a_1 > 0`: let `p = a_1` ("the pivot").
Delete `a_1`; subtract 1 from each of the next `p` largest remaining entries; re-sort to get `L'`
(length `n-1`). If `p > n-1` or any resulting entry would be negative, the step ABORTS.

**Terminating list, residue.** Repeat the step from `L` until it either aborts or reaches `0^r`
(all zeros). In the latter case the run TERMINATES, taking `s(L)` steps, and the **residue** is
`R(L) := r`.

**Already-proved fact (Lemma C1-X)**: for a terminating list `L` of length `n`,
`R(L) = n - s(L)`.

**Elimination sequence (general, not just Havel–Hakimi).** Given ANY graphic degree sequence `π`
(i.e. realizable as a simple graph's degree list), an **elimination sequence** is a sequence of
"laying-off" moves: at each step, pick ANY entry `d` of the current list (not necessarily the
largest — this is the generalization beyond Havel–Hakimi), delete it, and subtract 1 from `d`
OTHER entries of your choosing among the current list, provided this keeps the list graphic (i.e.
realizable) at every step and never produces a negative entry. A **theorem you may use as given**
(Kleitman–Wang 1973, as cited in Hiller arXiv:2206.05820): for any graphic sequence, EVERY choice
of elimination sequence keeps the list graphic throughout and terminates at a list of all zeros.
So every graphic `π` has many valid elimination sequences (Havel–Hakimi's own greedy "always pick
the largest" rule is just one particular choice among them), and each ends at `0^r` for some `r`
depending on the sequence chosen; let `len(σ)` denote the number of steps of elimination sequence
`σ`.

**A second already-established fact you may use as given (Hiller's theorem, arXiv:2206.05820,
abstract quoted verbatim):** *"...the residue, defined as the number of zeros remaining when the
Havel-Hakimi algorithm is applied to a degree sequence, yields a lower bound on the independence
number... We now prove that for any degree sequence, the elimination sequence derived from the
Havel-Hakimi algorithm dominates all other elimination sequences. Our result implies a conjecture
posed by Michael Barrus in 2010: When iteratively laying off degrees from a graphic sequence until
only a list of zeros remains, the number of zeros is at most the residue of this sequence."*

Restated in our notation: **for every graphic sequence `π`, `s(π) = min_σ len(σ)`, the minimum
taken over ALL valid elimination sequences `σ` of `π`** (where `s(π)` is specifically the
Havel–Hakimi step count). Equivalently `R(π) = n - min_σ len(σ)`: the Havel–Hakimi residue is a
MINIMUM over the whole family of elimination sequences of the same list.

## The statement to prove: (RH)

> **(RH).** Let `π' ⋖ π` denote one **elementary unit transfer down the dominance
> (majorization) order**: `π'` is obtained from `π` by picking two entries `a_i ≥ a_j` of `π`
> (`i` and `j` are positions, `a_i` the larger-or-equal one) and replacing them with `a_i - 1` and
> `a_j + 1` (then re-sorting into a valid list — note this requires `a_i ≥ 1`; no constraint is
> placed on the relative order of `a_i-1` and `a_j+1` after the move). **Claim: if both `π` and
> `π'` are terminating (graphic) lists of the same length `n`, then `R(π') ≤ R(π)`.**

This is claimed to hold for ARBITRARY terminating lists — no "head block" structural assumption
is needed (unlike other open statements on this line). It is a general statement about
Havel–Hakimi residues and the dominance order.

**Evidence so far (a census, not a proof):** checked on 284 distinct `(π, π')` pairs built this
way over terminating lists from partitions of size ≤ 20: 0 violations found.

## The reduction we want you to use: construct ONE witness elimination sequence

By Hiller's theorem above, `s(π) = min_σ len(σ)`. So **to prove `R(π') ≤ R(π)`, i.e.
`s(π) ≤ s(π')`, it suffices to exhibit ONE elimination sequence `σ` of `π` (any valid one, not
necessarily Havel–Hakimi's) with `len(σ) ≤ s(π')`.** Because then, by the minimality property,
`s(π) ≤ len(σ) ≤ s(π')`, giving `R(π) = n - s(π) ≥ n - s(π') = R(π')`.

**The natural candidate construction, which you are asked to carry out precisely:** take `π''s`
own Havel–Hakimi laying-off order — the specific sequence of pivots `p'_1, p'_2, ..., p'_{s(π')}`
that Havel–Hakimi uses when run on `π'` — and **transport** it to `π`. Concretely: `π = π'` with
one entry `a_i` increased by 1 and one entry `a_j` (with `a_j < a_i` originally, i.e. after the
transfer `a_j+1 ≤ a_i`) decreased by 1 relative to `π'`... **wait, be careful with direction**:
`π' ⋖ π` means `π'` is obtained FROM `π` by lowering `a_i` and raising `a_j`. So `π = π'` with the
inverse move: take `π'`, raise its version of `a_i` back by 1 (undoing the lowering) and lower its
version of `a_j` back by 1 (undoing the raising). You need to construct a valid elimination
sequence FOR `π` (not `π'`) using at most `s(π')` steps. One natural idea: run Havel–Hakimi's
exact pivot sequence on `π'`, but apply the corresponding lay-off moves to `π` instead — at each
step, the two lists differ in a controlled, bounded way (initially in exactly the two positions
`i,j`), so track how that difference evolves as you apply `π'`'s pivot choices to `π`'s current
list, and show it never causes an abort and terminates within `s(π')` steps (possibly earlier, if
the perturbation "self-heals").

## What we want from you

Attempt the construction above rigorously:
1. Set up the tracked difference between `π`'s evolving list and `π'`'s evolving list, when both
   are stepped using `π'`'s Havel–Hakimi pivot sequence.
2. Prove (or find where it fails) that this never causes an abort on the `π` side, and that it
   reaches all-zeros within `s(π')` steps.
3. If this exact construction does not work, try a natural variant (e.g., swap which list's pivot
   order is used, or interleave), and report which variant (if any) succeeds.
4. State the population of cases your proof needs to check by hand (e.g., "the pivot chosen at
   each step is unaffected by the transfer" vs "the pivot choice coincides with position i or j"),
   and handle each.

End your answer with exactly one of: **PROOF COMPLETE** (give the full witness construction and
the argument that it works), **PROOF INCOMPLETE** (state exactly which step/case you could not
close), or **CONJECTURE APPEARS FALSE** (give an explicit counterexample pair `(π, π')` — note
this would also contradict the 284-pair census, so double-check any candidate against the rules
above before reporting it).
