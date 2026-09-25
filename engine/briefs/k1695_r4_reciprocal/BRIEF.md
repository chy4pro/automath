# TASK K4-REC — a self-contained combinatorial problem about roots of unity

Pure mathematics + computation. No context outside this file is needed. Build tables and
constructions; do NOT write an essay. Every claimed witness must be machine-verified by your
own code, and the script must be included.

## The problem
Let `p` be a prime, `F` an algebraic closure of `GF(p)`, and `n ≥ 2`. Write `n = m·p^e` with
`gcd(m,p) = 1`; then the `n`-th roots of unity in `F` are exactly the `m`-th roots of unity,
`μ_m`, and there are `m` of them.

Given a multiset of NONZERO coefficients `u_1,…,u_k ∈ GF(p)` (or `GF(q)`), place them at
`k` DISTINCT positions `s_1,…,s_k ∈ Z_n = {0,1,…,n−1}` and form

        F(x) = u_1 x^{s_1} + u_2 x^{s_2} + … + u_k x^{s_k}.

Call the placement **CLEAN** if there is **no** `λ ∈ μ_m \ {1}` such that `F(λ) = 0` **and**
`F(λ^{-1}) = 0`. (Note `λ = −1` is its own inverse, so if `−1 ∈ μ_m` then `F(−1) = 0` alone
already makes the placement dirty.) Equivalently: `gcd(F, F*, (x^m−1)/(x−1))` is a constant,
where `F*` is the reversal of `F`.

**QUESTION: for which `(p, n, k)` and coefficient multisets does a clean placement exist,
and is there a construction that produces one?**

## What is already known (do not re-derive; use as controls)
- `p = 2`, all coefficients `= 1` (so the data is just a `k`-subset `S ⊆ Z_n`): the placement
  is clean iff no `λ ∈ μ_m\{1}` has both `λ` and `λ^{-1}` as roots of `Σ_{s∈S} x^s`.
- **CONSECUTIVE positions `{0,1,…,k−1}` give `F = (x^k−1)/(x−1)`, whose roots are the `k`-th
  roots of unity other than 1.** So consecutive is clean whenever the part of `k` coprime to
  `p` equals 1, i.e. **whenever `k` is a power of `p`** — verified for `p=2, k=4`, every
  `n = 5..29`.
- **Consecutive FAILS for `k = 6`, `p = 2`**: `(x^6−1)/(x−1)` has roots of order 3, and a bad
  pair appears at `n = 9, 12, 15, 18, 21`. Your code MUST reproduce this — it is the control
  that shows your checker discriminates. A checker that calls everything clean is worthless.
- `k = 2` is fully solved: with gap `g = s_2 − s_1`, a bad `λ` exists iff `−u_1/u_2` equals
  `−u_2/u_1` (i.e. `u_1² = u_2²`) and `ord(−u_1/u_2)` divides `m/gcd(m,g)`; choosing `g` with
  `gcd(m,g) = 1` when that ratio is 1, or `gcd(m,g)` not dividing `m/ord`, settles it except
  when `m = n` is a prime power `ℓ^a` and the ratio has order exactly `ℓ`.

## Deliverables
1. **A TABLE for `p = 2`, all coefficients 1.** For every `n = 4…64` and every EVEN
   `k` with `4 ≤ k ≤ n` (odd `k` is excluded for a reason outside this problem — just skip it),
   report: does a clean `k`-subset of `Z_n` exist? If yes, print one explicit witness `S`.
   If no, print `NONE` — those cells are the interesting ones and I want them all.
   (Search smartly: you may restrict to subsets containing 0, and you may stop at the first
   clean witness. State your search strategy and whether it was exhaustive per cell.)
2. **A CONSTRUCTION.** From the table, find a rule `S = S(n,k)` that is clean wherever a clean
   set exists, and PROVE it clean (a proof about roots of unity, not a table). Ideas worth
   testing: consecutive blocks; a consecutive block of size `p^j` plus a shifted block; sets
   whose `F` factors as `(x^{p^j}−1)/(x−1)` times something with no reciprocal pair; sets
   contained in an arithmetic progression whose common difference is coprime to `m`.
3. **The obstruction.** Characterise exactly the `(n,k)` with NO clean subset. Give the proof
   of impossibility for at least one infinite family if one exists.
4. **General coefficients / general `q`.** Repeat item 1 for `q = 3` and `q = 4` with
   coefficients ranging over the nonzero elements, for `n ≤ 24` and `k ≤ 6`. Report whether
   allowing unequal coefficients ever rescues an `(n,k)` that is `NONE` in the all-ones case.
5. **A SELF-CONTAINED python3 script** (stdlib only, EXACT arithmetic over finite fields —
   build `GF(4)`/`GF(8)`/`GF(9)` yourself, no floating point anywhere) that regenerates every
   table and re-verifies every witness it prints. It must print, as controls:
   (a) the `k=6`, `p=2` consecutive failures at `n = 9,12,15,18,21` (must FAIL — if your code
       says these are clean, your checker is broken and everything else you report is void);
   (b) the `k=4`, `p=2` consecutive successes (must be clean);
   (c) the population it searched per cell, so a silently truncated search is visible.

## Rules
- Exact arithmetic only. Work in `GF(p^d)` where needed, or reason with cyclotomic polynomials
  over `GF(p)` — never numerically.
- Every witness you print must be re-verified by your own checker in the same run.
- "No clean set exists for `(n,k)`" is only acceptable if your search for that cell was
  EXHAUSTIVE; say so per cell, and say the size of the space you enumerated.
- Do not speculate about what the problem is for. Answer the question as stated.
