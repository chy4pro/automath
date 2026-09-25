# Task: find a CLOSED invariant for the Havel–Hakimi pivot-dominance statement (DOM-MAJ)

**Owner-drafted (owner-w61), PROTOCOL v4 §3b.**
**BUILT FROM: WOWII-61 owner round r45, 2026-08-23 (ledger §7.60, run
`problems/wowii/w61_r45_g0dom.py`).** Every measurement quoted below is from that round's run
and from no earlier one. If you have seen an earlier brief on this line, this one supersedes it:
r45 **refuted** the natural candidate invariant, and the refutation is the reason this brief
exists. Nothing has been withheld — you are being asked exactly the question we are stuck on,
in exactly the coordinates we are stuck in.

**§96 — READ THIS FIRST.** *"I could not finish, and here is exactly where I stopped"* is a
**valued answer, not a failure.** Three of our last four engine outputs stopped honestly and named
their stuck point, and the CONVERGENCE of those stuck points is what located the crux both times.
A confident finish that papers over a gap is worth **less than nothing** to us, because we rebuild
every construction by hand and the papering-over costs us a round to detect. If you get one lemma
and no theorem, send the lemma and say precisely what it does not reach.

**A counterexample is as valuable as a proof**, and it must come as **explicit integer lists** —
we rebuild every object in our own hand and never accept a described one.

---

## 1. The object. Everything is elementary and finite.

A **state** is a finite list of non-negative integers, always written sorted **decreasing**:
`X = (X₀ ≥ X₁ ≥ … ≥ X_{n−1})`, `X₀ =: d`.

**The step** (this is Havel–Hakimi laying-off, and it is deterministic — there is no choice):

```
step(X):
    if X is empty or X₀ == 0:        return TERMINAL
    d    := X₀
    rest := (X₁, …, X_{n−1})
    if d > len(rest):                return ABORT
    blk  := the first d entries of rest      # the d LARGEST, because rest is sorted
    tail := the remaining entries of rest
    if any entry of blk is 0:        return ABORT
    return sort_desc( [x − 1 for x in blk] + tail )
```

Two facts you should verify for yourself before using anything else:

* **the length drops by exactly 1 per step** (the head is removed and nothing is added);
* **the sum drops by exactly `2d`** (one `d` removed, `d` entries decremented).

`X` **terminates** iff iterating `step` reaches `TERMINAL` without ever hitting `ABORT`. Write
`X^{(k)}` for `X` after `k` steps. The **pivot sequence** is

```
p(X) := ( X^{(0)}₀ , X^{(1)}₀ , … , X^{(K−1)}₀ )      K = the number of steps to TERMINAL.
```

**Dominance.** For lists `A`, `B` (zero-padded to a common length), `A ⪰ B` means
`Σ_{i<m} A_i ≥ Σ_{i<m} B_i` for every `m`. When `sum(A) = sum(B)` this is the usual dominance
(majorization) order on partitions of that common sum.

## 2. Two facts we have already proved. Use them freely; re-derive them if you like.

> **(PIV-MONO).** `max(step(X)) = max(X₁ − 1, X_{d+1}) ≤ d`. Hence the pivot sequence `p(X)` is
> **already sorted decreasing** — no sorting is needed to regard it as a partition.
>
> *Proof.* `X₁ ≤ X₀ = d` gives `X₁ − 1 ≤ d − 1`; `X_{d+1} ≤ X₀ = d`. And `step(X)`'s entries are
> `{X_i − 1 : 1 ≤ i ≤ d} ∪ {X_i : i > d}`, whose largest is `max(X₁ − 1, X_{d+1})`. ∎

> **(PIV-SUM).** `Σ p(X) = sum(X)/2`, for every terminating `X`.
>
> *Proof.* Each step drops the sum by `2·(that step's pivot)`, and the terminal state is all-zero. ∎

**Consequence (the reformulation that makes the target concrete).** For two terminating lists with
`sum(A) = sum(B) = N`, the `k`-th prefix sum of `p(X)` equals `(N − sum(X^{(k)}))/2`. Therefore

> **`p(A) ⪰ p(B)`  ⟺  `sum(A^{(k)}) ≤ sum(B^{(k)})` for every `k`.**

Both `p(A)` and `p(B)` are partitions of `N/2`, so this is an ordinary dominance comparison.

## 3. THE STATEMENT

> **(DOM-MAJ).** Let `A` and `B` be lists with `sum(A) = sum(B)`, both terminating, and `A ⪰ B`.
> Then `p(A) ⪰ p(B)`.
>
> Equivalently, by §2: **`sum(A^{(k)}) ≤ sum(B^{(k)})` for every `k`** — the more dominant list
> sheds mass at least as fast, at every single step.

**Status: measured, never proved.** r45's own census, independent of the earlier one:
**`7 403` of `7 403`** dominance pairs of terminating partitions of `N ≤ 18` with `≤ 11` parts.
The reversed companion `p(B) ⪰ p(A)` **fails `6 595` times** on the same pairs, so the census is
not vacuous; and the `6 595` pairs with `p(A) ≠ p(B)` are exactly the sub-population that could
have come out the other way (the remaining `808` have `p(A) = p(B)` and could not).

**Prove it, or refute it with an explicit pair `(A, B)` of integer lists.**

## 4. WHAT WE TRIED, EXACTLY, AND EXACTLY HOW IT DIED

This is the heart of the brief. The obvious induction is to find a relation `R(A,B)` such that

* `A ⪰ B` with equal sums ⟹ `R(A,B)`;
* `R(A,B)` ⟹ `sum(A) ≤ sum(B)`;
* **`R` is closed under the joint step: `R(A,B)` ⟹ `R(step A, step B)`.**

Any such `R` proves (DOM-MAJ) immediately by induction on `k`. Here is the candidate we built,
why it is the natural one, and the explicit list on which it dies.

For a list `X` zero-padded to length `n`, let `T_m(X)` be **the sum of all but the `m` largest
entries** of `X` (so `T_0(X) = sum(X)`, and `T_m` is what dominance controls from the bottom).

> **(C1)** `T_m(A) ≤ T_m(B)` for every `m ≥ 0`.
> **(C2)** `sum(B) − sum(A) ≥ 2·( max(B) − max(A) )`.

* `A ⪰ B` with equal sums gives **(C1)** — it is literally dominance rewritten from the tail —
  and gives **(C2)**, since then `sum(B) − sum(A) = 0` and `max(B) ≤ max(A)`.
* **(C2) is exactly `sum(step A) ≤ sum(step B)`**, because a step drops the sum by twice the max.
* So **(C1)∧(C2) at every `k` IS (DOM-MAJ)** — the `m = 0` case of (C1) is the conclusion.

**(C1)∧(C2) IS NOT CLOSED.** r45 tested closure over all sorted lists of a common length `n` with
entries `≤ V`, restricted to **terminating** lists (equivalently: even sum, no abort — this filter
matters; without it the failures are dominated by odd-sum pairs no trajectory can reach, and our
first pass made exactly that mistake):

| `n`, `V` | pairs satisfying (C1) | (C1)∧(C2) preserved by the step | **VIOLATED** |
|---|---|---|---|
| 5, 4 | 436 | 414 | **14** |
| 6, 4 | 2 157 | 2 089 | **52** |
| 6, 5 | 4 600 | 4 309 | **229** |
| 7, 4 | 6 930 | 6 781 | **122** |
| 7, 5 | 23 620 | 22 625 | **851** |

**Every single violation has the same shape: (C1) survives the step and (C2) dies.** The smallest:

```
A = (4, 2, 2, 2, 2)        sum 12,  max 4
B = (4, 4, 2, 2, 2)        sum 14,  max 4
   (C1) holds:  T = (12,8,6,4,2,0) for A ;  (14,10,6,4,2,0) for B
   (C2) holds:  14 − 12 = 2  ≥  2·(4 − 4) = 0
step A = (1, 1, 1, 1)      sum 4,  max 1
step B = (3, 1, 1, 1)      sum 6,  max 3
   (C1) still holds
   (C2) FAILS:   6 − 4 = 2   <   2·(3 − 1) = 4
```

**The mechanism, stated plainly.** After a step the new maximum is `max(X₁ − 1, X_{d+1})` — it is
governed by the **second** entry, and (C1)∧(C2) place **no constraint whatever on `A₁` versus
`B₁`**. Here `A₁ = 2` and `B₁ = 4`. That is the whole failure.

**(C1) alone is not closed either** (62 losses at `n=6, V=5`), so (C2) is doing real work — just
not enough of it.

**AND YET THE INVARIANT IS TRUE WHERE IT IS NEEDED.** Walking every dominance pair of partitions
of `N ≤ 16` with `≤ 10` parts, both terminating, in lockstep: **`2 683` pairs, `10 470` joint
states, `0` violations of (C1), `0` violations of (C2).** As a control that the walk can see a
failure at all, the entrywise reading `max(A^{(k)}) ≥ max(B^{(k)})` **fails 2 301 times** along
those very trajectories.

> **So (C1)∧(C2) is a TRUE invariant of the reachable pairs and a FALSE closure property.**
> The pair `(4,2,2,2,2)`, `(4,4,2,2,2)` satisfies (C1)∧(C2) and **was not produced as
> `(A^{(k)}, B^{(k)})` by any of the 2 683 trajectories we walked** — we have not proved it is
> unreachable, only that our walk never produced it. Something about reachability appears to be
> excluding it, and we do not know what.

## 5. WHAT WE ARE ASKING FOR — in order of value

1. **A relation `R` meeting the three bullets of §4.** It must be strictly stronger than
   (C1)∧(C2) on the abstract pairs (it has to exclude `(4,2,2,2,2)` vs `(4,4,2,2,2)`) and weaker
   than or equal to "reachable". The obvious direction is to add something controlling `A₁`
   against `B₁`, or more generally `A_j` against `B_j`; note that the naive
   *"`sum(B) − sum(A) ≥ 2(B_j − A_j)` for all `j`"* **fails at `k = 0`** — take `A = (3,1,1,1)`,
   `B = (2,2,1,1)`, where `A ⪰ B`, sums equal, and `B₁ = 2 > 1 = A₁`. So a `j`-indexed
   strengthening must degrade with `j` in some way we have not found.
2. **A direct proof of (DOM-MAJ) by any other route.** A closed-form or max-min expression for
   `sum(X^{(k)})`, or for the partial pivot sums `Σ_{j<k} p(X)_j`, would do it — we know of none
   and would regard one as a major result in its own right.
3. **An explicit counterexample** to (DOM-MAJ) itself: two integer lists, same sum, both
   terminating, `A ⪰ B`, with `p(A) ⋡ p(B)`. Give the lists and both full pivot sequences.
4. **A proof under a stated extra hypothesis**, with the hypothesis named exactly and its cost
   made explicit.
5. **An honest stop.** See §96 above. Tell us which of §4's two facts — truth on the reachable
   set, failure of closure — you were unable to reconcile, and what you tried.

## 6. A ROUTE WE HAVE PARTLY CLOSED, WHICH YOU MAY PREFER

Dominance on partitions of `N` is generated by **single unit transfers down**: move `1` from a
larger part to a smaller (or to a new part). Call the one-transfer case

> **(PIVOT-MAJ).** If `B` is `A` with one unit moved down, both terminating, `sum` equal, then
> `p(A) ⪰ p(B)`.

Since `p`-dominance is **transitive**, (PIVOT-MAJ) gives (DOM-MAJ) **provided** every dominance
pair of terminating lists is joined by a chain of single unit transfers that **stays inside the
terminating set**. The obstruction is real: a unit transfer can leave it — `(3,3,1,1)` **ABORTS**
(pivot `3`, rest `(3,1,1)`, block `(3,1,1) → (2,0,0)`; then `(2,0,0)` has pivot `2` and block
`(0,0)`, which contains a `0`, so the abort lands on the SECOND step, not the first).

**r45 measured this.** Over all even `N ≤ 18`, terminating partitions with `≤ 11` parts:

* dominance pairs tested: **7 403**
* joined by a chain staying inside the terminating set: **7 403**
* not joined: **0**
* unit-transfer edges that DO leave the terminating set: **47** (so the obstruction fires and the
  census is not vacuous)

> **So on this population (PIVOT-MAJ) and (DOM-MAJ) are EQUIVALENT.** Proving (PIVOT-MAJ) plus
> this connectivity statement is a complete route. **Either half is a valued answer.** The
> connectivity half — *"the terminating partitions of `N`, ordered by dominance, are connected by
> single unit transfers within the terminating set"* — is a self-contained combinatorial question
> that does not mention pivots at all, and we would take a proof of it on its own.

## 7. Ground rules

* **No literature appeals as proof.** If you recognise the operation, say so and give the
  reference, but the argument must stand on its own text here. Assume no internet.
* **Every claimed identity must be checkable on a small explicit example that you supply.** We
  will recompute it. Constructions of yours have survived our rebuild before; derivations on top
  of them have failed four times on this line, so keep the two clearly separated and label which
  is which.
* **State your populations.** If you test something, say over exactly what set, and say which
  members of that set could have falsified the claim. A census over a population where the claim
  could not have failed is not evidence.
* **Do not exhaustively search a large space and report the absence of a counterexample as a
  proof.** Say "searched X, found none" and label it as such.
* If you find that a statement in **this brief** is wrong, say so — that has happened three times
  on this line and each time it was the most valuable thing in the reply.

## 8. Dispatch note (for whoever sends this)

Per the WOWII-61 charter's S2 rule, a dispatch to a web model must carry the S2 template set
(T1 competition disguise, no-internet clause, T8 persistence rider, T11 known-partial-results
preface) from `prompts/templates.md`. This brief is the mathematical payload only; it has not
been dispatched by the owner and no seat or lease has been taken for it.
