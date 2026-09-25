# TASK K5-GFQ — the same reciprocal-root problem over a GENERAL finite field

Self-contained; no context outside this file is needed. Deliver a CONSTRUCTION WITH PROOF plus
a machine-verified table. Do not write an essay. Every witness must be re-verified by your own
code in the same run, and the script must be embedded.

## The problem
Let `q = p^d`, `F = GF(q)`, `n ≥ 2`. Write `n = m·p^e` with `gcd(m,p) = 1`; the `n`-th roots of
unity in the algebraic closure are exactly the `m`-th roots of unity, `μ_m`, and there are `m`.

**You are GIVEN a multiset of nonzero coefficients `u_1,…,u_k ∈ F^×` — you do not get to choose
them.** You choose only the `k` DISTINCT positions `s_1,…,s_k ∈ Z_n` at which to place them,
forming `F_S(x) = Σ_i u_i x^{s_i}`.

Call the placement **CLEAN** if there is **no** `λ ∈ μ_m \ {1}` with `F_S(λ) = 0` **and**
`F_S(λ^{-1}) = 0`. (Note `λ = −1` is its own inverse, so if `−1 ∈ μ_m` then `F_S(−1) = 0` alone
makes the placement dirty.)

**GOAL: a construction that, given `(q, n, k)` and the coefficient multiset, outputs a clean
placement — with a PROOF that it is clean — together with an exact characterisation of the
`(q, n, k, multiset)` for which no clean placement exists.**

## What is already PROVED — scaffold; do not re-derive, and do not contradict without a witness
**The `q = 2` case is completely solved** (all coefficients are then forced to be 1, so the data
is just a `k`-subset `S ⊆ Z_n`). Both constructions below are verified out of sample on
`n = 65…150`, 4 473 cells:
- **Odd `n`.** With `d = n−1`, take `S₀ = {d, d/2} ∪ ⋃_{r=1}^{(k−2)/2} {r, d−r}`. `S₀` is
  symmetric under `s ↦ d−s` except that `d ∈ S₀` while `0 ∉ S₀`, so in characteristic 2
  `F_{S₀}(x) + x^d F_{S₀}(x^{-1}) = 1 + x^d`. A common reciprocal root kills the left side, so
  `λ^d = 1`; with `λ^n = 1` and `gcd(n, n−1) = 1` that forces `λ = 1`, excluded. ∎
- **Even `n = m·2^e`, `m > 1`.** Place so that residues `0` and `1 mod m` carry an ODD number of
  positions and every other residue an EVEN number. Then on `μ_m` the pairs cancel and
  `F_S(λ) = 1 + λ`, which vanishes only at `λ = 1`. Capacity `2 + 2(h−2) + (m−2)h = n−2`. ∎
- **Obstruction.** `k = n` forces `S = Z_n`; every residue mod `m` then occurs `2^e` times, an
  even number, so `F_S ≡ 0` on all of `μ_m` and the placement is dirty whenever `m > 1`.

## ⚠️ WHY THIS DOES NOT TRANSFER, AND WHAT THE REAL DIFFICULTY IS
**BOTH `q = 2` arguments run on characteristic-2 pairwise cancellation** (`x + x = 0`). Over any
`q` with `p > 2` that mechanism is simply unavailable, and over `q = 2^d` with `d > 1` the
coefficients are no longer forced to be 1, so "count the positions in each residue class" is
replaced by "SUM the coefficients in each residue class". Concretely, the reduction you should
start from — this much is elementary and is handed to you so you do not spend a pull on it — is:

> for `λ ∈ μ_m`, `F_S(λ)` depends only on the **residue-class sums**
> `T_r = Σ{ u_i : s_i ≡ r (mod m) }`, via `F_S(λ) = Σ_{r=0}^{m−1} T_r λ^r`.

So the problem splits into two halves, and I want both answered:
1. **Which profiles `(T_0,…,T_{m−1})` are clean?** (A question about polynomials of degree `< m`
   and their reversals over `GF(q)`.)
2. **Which profiles are REALISABLE** by distributing the GIVEN coefficient multiset into residue
   classes of prescribed sizes (each class has exactly `n/m = p^e` positions available)? This is
   the genuinely hard half over general `q` — it is a subset-sum-flavoured constraint that is
   trivial when all coefficients are equal and is not trivial otherwise.

## Empirical facts you must reproduce or refute (they are verified; disagreeing means you are wrong)
- **Unequal coefficients RESCUE cells that all-ones cannot.** Verified examples, each confirmed
  twice independently: `q=3, n=6, k=6, positions [0,1,2,3,4,5], coefficients [1,1,1,1,1,2]` is
  CLEAN, while the all-ones placement on the same positions is DIRTY. Likewise
  `q=3, n=4, k=4, coeffs [1,1,1,2]`; `q=3, n=5, k=5, coeffs [1,1,1,1,2]`;
  `q=4, n=3, k=3, coeffs [1,1,2]`; `q=4, n=6, k=6, coeffs [1,1,1,1,1,2]`.
  In particular **the `k = n` obstruction above is a `q = 2` artefact** of having no coefficients
  to vary. Your characterisation must reflect that.
- **`k = 2` is fully solved**, any `q`: with gap `g = s_2 − s_1`, a bad `λ` exists iff
  `u_1² = u_2²` and `ord(−u_1/u_2)` divides `m/gcd(m,g)`. Reproduce this as a check.
- Across `q ∈ {3,4}`, `n ≤ 24`, `k ≤ 6`, a clean placement was found in EVERY cell once unequal
  coefficients were allowed. **No cell is known to be unrescuable for `p > 2`.** Either prove
  that (a construction covering all cells), or exhibit the first counterexample.

## Deliverables
1. **CONSTRUCTION + PROOF** for general `q`, covering odd `n` and even `n`, for an arbitrary
   given coefficient multiset. State precisely the cells it does not cover.
2. **The exact obstruction** for `p > 2`: characterise `(q,n,k,multiset)` with no clean
   placement, or prove there are none, or give the first explicit example.
3. **A TABLE** for `q ∈ {3,4,5,7,8,9}`, `n ≤ 30`, `2 ≤ k ≤ n`, over a stated family of
   coefficient multisets (at minimum: all-ones; all-ones-with-one-entry-changed; and a
   multiset with all entries distinct where `k ≤ q−1`). Per cell: clean placement found or not,
   an explicit witness, the population searched, and whether the search was exhaustive.
4. **A SELF-CONTAINED python3 script** (stdlib only, EXACT finite-field arithmetic you build
   yourself, NO floating point) regenerating everything and re-verifying every printed witness.

## MANDATORY CONTROLS — a submission missing any of these is void, not partially credited
- **(V-a)** `q=2, k=6`, consecutive positions `{0,…,5}` must come out **DIRTY** at
  `n = 9, 12, 15, 18, 21`. A checker that calls these clean is broken and everything else you
  report is void.
- **(V-b)** `q=2, k=4`, consecutive positions `{0,1,2,3}` must come out **CLEAN** for
  `n = 5…29`.
- **(V-c)** the five rescue examples listed above must come out CLEAN, and their all-ones
  counterparts on the same positions must come out DIRTY. Print both verdicts side by side.
- **(V-d)** your field arithmetic must self-check (associativity/distributivity/inverses) for
  every `GF(q)` you build, and you must build `GF(4)`, `GF(8)`, `GF(9)` yourself.
- **(V-e)** print the population searched per cell. A cell reported as having NO clean placement
  is only acceptable if that cell's search was EXHAUSTIVE; say so per cell. (Stopping early
  after FINDING a witness is fine — a witness is a witness.)

## Rules
- Exact arithmetic only; work in `GF(q^j)` or with cyclotomic factorisations over `GF(q)`.
- A construction validated only on the cells it was read off from is a PATTERN, not a
  construction. Prove it, or say plainly that it is a conjecture supported by a table.
- Do not speculate about what this problem is for. Answer it as stated.
