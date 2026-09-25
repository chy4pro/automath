# Task: a reusability audit of two proved lemmas — what each needs, what it does not, and where else it applies

**Brief E10 (drafted 2026-08-23 by owner-w61, round 43).**

This is **not** a proof task and **not** a refutation task. Both lemmas below are **proved**, and their
proofs have been checked. **You are explicitly asked NOT to re-validate them.** What we need is the
thing that is genuinely expensive for us and cheap for you: a careful, exhaustive **comparison and
completeness audit** — which hypotheses are load-bearing, which are decoration, what the lemma does
*not* give, and where else in partition / degree-sequence combinatorics it would apply.

**You have no internet access and no access to any repository.** Everything you need is in this file.
Work only from what is written here. **If a question below cannot be answered from what is given,
say "underdetermined by the brief" and say what is missing** — that answer is useful; a guess is not.
**Give reasoning, not confidence language.**

---

## 1. The process (verbatim; assume no other context)

Finite lists of non-negative integers, treated as multisets, always written weakly decreasing. One
**Havel–Hakimi step** on a list `L`:

```
sort L weakly decreasing  ->  s
if s is empty or s[0] == 0 :  TERMINAL   (the run stops here)
d    := s[0]                              (the PIVOT of this step)
rest := s[1:]
if d > len(rest) :            ABORT       (the list is not graphic)
blk  := rest[:d] ;  tail := rest[d:]      (blk = the d LARGEST remaining entries)
if any entry of blk is 0 :    ABORT
next := sort_desc( [x-1 for x in blk] + tail )
```

A run **terminates** if it reaches `TERMINAL` without ever hitting `ABORT`. Havel–Hakimi terminates on
a list exactly when that list is **graphic** (realizable as the degree sequence of a simple graph).
`s(L)` := number of steps; `R(L)` := number of entries remaining at `TERMINAL` (all `0`) — the
**residue**. Notation: `[x]^k` is `k` copies of `x`; `∪` and `++` both mean multiset union.

**Erdős–Gallai**, used by Lemma C1-N: a weakly decreasing list `d_1 ≥ … ≥ d_n` of non-negative
integers with even sum is graphic iff for every `r ∈ [1,n]`

```
LHS := sum_{i<=r} d_i     <=     r(r-1) + sum_{i>r} min(d_i, r)  =:  RHS.
```

---

## 2. Lemma C1-N (PROVED — supplied; do not re-validate)

For a partition `λ = (λ₁ ≥ λ₂ ≥ …)` define `M(λ) := [λ₁]^{λ₁+1} ∪ λ` — the list `λ` with a **head
block** of `λ₁+1` extra copies of `λ₁` planted in front.

> **Lemma C1-N.** For every partition `λ`, `M(λ)` terminates **iff `|λ|` is even**, where `|λ|` is the
> sum of the parts of `λ`.
>
> *Proof.* Write `w = λ₁`, `n = |λ|`. `Σ M(λ) = w(w+1) + n`, and `w(w+1)` is even, so `Σ M` is even
> iff `n` is; an odd sum cannot be graphic, and Havel–Hakimi terminates exactly on graphic sequences.
> For the converse it suffices that Erdős–Gallai holds at every `r`. `M(λ)` has **at least `w+2`
> entries equal to `w`** — the `w+1` planted copies **and `λ₁` itself**. For `r ≤ w` the top `r`
> entries are all `w`, so `LHS = rw`, while at least `w+2−r` further entries equal `w` contribute
> `min(w,r) = r` each: `RHS ≥ r(r−1) + (w+2−r)r = r(w+1) > rw`. For `r = w+1`, `LHS = (w+1)w` and
> `RHS ≥ r(r−1) = (w+1)w`. For `r ≥ w+2` every `d_i ≤ w < r`, so
> `RHS ≥ r(r−1) ≥ r(w+1) > rw ≥ LHS`. ∎

Backing already in hand (given so you do not re-derive it): `4 506` partitions with `n ≤ 22` checked,
parity ⇔ termination with `0` violations, and the Erdős–Gallai inequality verified directly at every
`r` on the same `4 506` lists, `0` violations. Controls: the Erdős–Gallai checker **does** reject
`[3,3,1,1]`; the corrupted claim *"`M(λ)` always terminates"* is refuted `388` times.

**Why it was wanted.** Every induction in this effort had been carrying a side-condition *"provided
the smaller list still terminates"*. C1-N discharges that structurally: removing two parts of equal
parity from `λ` keeps `|λ|` even, hence keeps `M(λ⁻)` terminating.

---

## 3. Lemma C1-R (PROVED — supplied; do not re-validate)

> **Lemma C1-R (the `(s,j)` descent).** For `s ≥ 1`, `x ≥ 2`, `0 ≤ j ≤ x+s`, and any partition `ν`
> with `max(ν) ≤ x−1`, put
> ```
> F_s(x, j; nu)  :=  [x]^j  u  [x-1]^{x+s-j}  u  nu          (size x + s + |nu| parts)
> ```
> Then **one Havel–Hakimi step** sends
> * **(interior)** `F_s(x, j; ν) ⟶ F_s(x−1, j+s−2; ν)` whenever `1 ≤ j ≤ x+1`;
> * **(entry)** `F_s(x, x+s; ν) ⟶ F_{s−1}(x, s−1; ν)` whenever `s ≥ 2`.
>
> *Proof (interior).* The head is `x`; the rest is `[x]^{j−1} ∪ [x−1]^{x+s−j} ∪ ν`, of size
> `x+s−1+|ν| ≥ x`. Its top `x` entries are the `j−1` copies of `x` together with `x−j+1` copies of
> `x−1` — available because `s ≥ 1` gives `x+s−j ≥ x−j+1`, and `j ≤ x+1` gives `j−1 ≤ x`. Exactly
> `s−1` copies of `x−1` and all of `ν` stay outside; **ties with parts of `ν` equal to `x−1` are
> immaterial — the resulting multiset is the same**, which is why the hypothesis is `max(ν) ≤ x−1`
> and not `≤ x−2`. Decrementing gives `[x−1]^{j−1} ∪ [x−2]^{x−j+1}`, and adjoining the `s−1` copies
> left outside gives `[x−1]^{j+s−2} ∪ [x−2]^{x−j+1} ∪ ν = F_s(x−1, j+s−2; ν)`. The block holds no
> `0` because `x−1 ≥ 1`. *(entry).* Head `x`, rest `[x]^{x+s−1} ∪ ν`; the top `x` entries are `x`
> copies of `x`, leaving `[x]^{s−1} ∪ ν` outside, so the result is `[x]^{s−1} ∪ [x−1]^x ∪ ν`, which
> **is** `F_{s−1}(x, s−1; ν)`. ∎

**What C1-R replaced.** Four separately-proved descents in this effort are single instances of it:

| earlier lemma | as `F` | what C1-R says |
|---|---|---|
| `[u]^{u+2} ∪ μ ⟶ [u−2]^u ∪ μ` | `F_2(u, u+2; μ)` | **entry** to `F_1(u,1;μ)`, then **interior** to `F_1(u−1,0;μ) = [u−2]^u ∪ μ` — its two steps are the two clauses |
| `Y(u;ν) ⟶ Y(u−1;ν)` where `Y(u;ν) = F_2(u,2;ν)` | `F_2(u,2;ν)` | `s = 2` makes `j+s−2 = j`: **`j` is invariant, which is exactly why `Y` reproduces itself** |
| `Q(u;ν) ⟶ Q(u−1;ν)` where `Q(u;ν) = F_2(u,1;ν)` | `F_2(u,1;ν)` | same, at `j = 1` |
| `[b]^{b+3} ∪ ν ⟶ Y(b;ν)` | `F_3(b, b+3; ν)` | **entry** with `s = 3` |
| `G_i ⟶ G_{i+1}` where `G_i = F_3(2q−i, 3+i)` | `F_3(2q−i, 3+i)` | `s = 3` makes `j+s−2 = j+1`: `G_i`'s index **is** `j−3` |

**The organizing observation:** `s` is the real parameter and `j` is the coordinate along the descent
— **the `[x−1]` block shrinks by `s−1` and the `[x]` block grows by `s−2` at every step.**

---

## 4. ⚠️ WHAT TO PRODUCE

A written reusability audit, answering **each numbered question below explicitly and separately**. If
a question is not answerable from this file, write **"underdetermined by the brief"** and name the
missing input. Do not skip a question; a missing answer is the failure mode we are auditing for.

### For Lemma C1-N
1. **Hypothesis audit.** List every hypothesis the statement and proof actually use. For each, say
   whether it is **load-bearing** (the conclusion fails without it) or **decoration** (removable).
   In particular: is the head-block multiplicity `λ₁+1` load-bearing, or would `λ₁` or `λ₁+2` do?
   Is `max(ν)`-style flatness used anywhere? Is `λ` required to be a partition (weakly decreasing) or
   would any multiset do?
2. **Exact generalization.** State the most general head block `[w]^k ∪ λ` for which the same proof
   goes through unchanged, with the constraint on `k` in terms of `w`, and say exactly which
   inequality in the proof pins `k` down.
3. **What it does NOT give.** Name at least three things a reader might wrongly infer from C1-N. (For
   example: does it say anything about `R(M(λ))`? about `λ` itself being graphic? about lists that
   are not of the form `M(λ)`?)
4. **Reuse targets.** Name concrete settings, off this effort, where "a planted head block forces
   graphicness, so the only obstruction is the parity of the sum" would be a usable tool. Threshold
   graphs, split graphs, degree-sequence packing, and the Erdős–Gallai / Ruch–Gutman literature are
   all fair game. For each, say what would have to be checked before using it.
5. **Sharpness.** Is the `r = w+1` case of the proof tight (`LHS = RHS = (w+1)w`)? If so, what does
   that tightness say about how much slack the lemma has, and about `k = w` (one fewer planted copy)?

### For Lemma C1-R
6. **Hypothesis audit**, as in 1. In particular: is `max(ν) ≤ x−1` (rather than `≤ x−2`) load-bearing,
   and where exactly? Is `x ≥ 2` load-bearing? What happens at `j = 0`, and why does the interior
   clause require `j ≥ 1`? What happens at `j = x+1` versus `j = x+s`?
7. **Boundary completeness.** The interior clause covers `1 ≤ j ≤ x+1` and the entry clause covers
   `j = x+s`. **Enumerate the `(s,j)` pairs covered by neither**, and for each say whether the step
   is undefined, aborts, terminates, or simply leaves the family `F`. This is the completeness
   question we most want answered.
8. **Closure of the family.** Starting from `F_s(x, j; ν)` and iterating, describe the full orbit:
   which `(s,j,x)` are reachable, does the orbit always reach `s = 1`, and does it always leave `F`
   before terminating or not?
9. **What it does NOT give.** C1-R describes **one step**. Name what it does *not* determine — e.g.
   does it give `R(F_s(x,j;ν))`? does it give `s(F_s(x,j;ν))`? does it give termination at all?
10. **Reuse targets**, as in 4: where else would a two-parameter family closed under one Havel–Hakimi
    step be useful? Say what makes `F` special — is it that it is a two-block "staircase" list with
    an inert tail, or something narrower?
11. **Missing instances.** The table in §3 lists five earlier lemmas as instances. From the shape of
    `F` alone, name further natural descents that *ought* to be instances at `s = 4` or `s ≥ 5`, and
    state them explicitly as `F_s(x,j;ν) ⟶ …`.

### Cross-cutting
12. **Do C1-N and C1-R compose?** `M(λ) = [λ₁]^{λ₁+1} ∪ λ` — is `M(λ)` an `F_s(x,j;ν)` for some
    `(s,j,x,ν)`? If yes, give them explicitly. If no, say precisely which structural feature of `F`
    `M(λ)` fails to have. **This is the single most valuable question in this brief.**
13. **A packaging judgment.** If these two lemmas were to be written up for use outside this effort,
    what is the smallest self-contained set of definitions they need, and what is the honest one-line
    claim for each? Be conservative: we have been burned by claims stated more generally than the
    proof buys.

---

## 5. Standing warnings

* **We are not asking whether the proofs are correct.** If you nonetheless believe you have found an
  error, state it separately at the end, with the exact line and a concrete instance where the step
  fails — and check that instance's arithmetic twice. Two prior reports on this effort claimed a
  refutation and both turned out to be the reporter's own arithmetic slip; a useful invariant for
  catching that is that **one Havel–Hakimi step drops the sum by exactly `2d` and the length by
  exactly `1`**, and **a list of odd sum can never terminate.**
* Do not report agreement with the census figures in §2 as a result. They are already in hand.
* Prefer "underdetermined by the brief" over a plausible guess. We can supply what is missing; we
  cannot cheaply detect a confident answer built on an assumption you did not flag.
