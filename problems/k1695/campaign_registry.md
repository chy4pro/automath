# k1695 CAMPAIGN REGISTRY — Kourovka 16.95 (Thompson's cyclic-matrix conjecture)
Line owner: `line-k1695` session (v5 architecture). Created 2026-08-24 at line resume.
Discipline: VERIFY_CHECKLIST.md. Everything is PROVISIONAL until it meets §A (executable
verifier + positive AND negative controls, run fresh, OR Lean). 不可自宣.

## Statement
For every field `F` and every `A ∈ GL(n,F)` there is a permutation matrix `P` with `AP`
cyclic (minpoly = charpoly, i.e. nonderogatory). — J. G. Thompson, Kourovka 16.95 (2006).
Homonym trap: "Thompson's conjecture" in the literature usually = the conjugacy-class-sizes
conjecture for finite simple groups. Always disambiguate.

## Inherited state (v4, imported BY REFERENCE — not re-derived here)
| id | content | where | status |
|---|---|---|---|
| R1 | Stasinski counterexample reproduced exactly; erratum's side condition corrected to `char F ∤ (n−1)`; break point inside Dixon's proof reproduced; J−I does NOT refute 16.95 | `orchestration/results/k1695_state.md` §0–§8; `problems/k1695/round1_stasinski.py`; `logs/k1695/round1.log` | provisional, verifier+controls present |
| R2 | closed-form cyclicity criterion for `J − P_σ` by cycle type (21 224 perms, 0 disagreements); THEOREM: 16.95 true for every invertible `aI+bJ` over every field (410 exhaustive rows); "always take an n-cycle" FALSE (char 2, n≡2 mod 4); Dixon's greedy provably returns `P=I` | `k1695_state.md` §R1–R14; `round2_*.py`; `logs/k1695/round2*.log` | provisional, verifier+controls+independent recheck present |
| LIT | zbMATH ~35 queries + Crossref/OpenAlex/author CV: no journal successor to arXiv:1606.02238, no prior appearance of the `aI+bJ` criterion found. Named gap: MathSciNet (subscription wall) | `orchestration/results/k1695_litcheck.md` | searched-and-absent; gap named |
| P-K1 | exhaustive census, 0 counterexamples in ~1.52M invertible matrices: GL(2,q) q∈{2,3,5,7}, GL(3,q) q∈{2,3,5}, GL(4,2) | `notes/selection/probe_k1695_smallfield.{py,out}` | CENSUS, window stated; in-repo reproduction pending (R3) |

## Rounds run by this line (v5)
(appended as they complete — see §R3 below)

---

# ROUND 3 (v5, 2026-08-24) — the rank-one-over-monomial stratum
Interpreter for every number below: `.venv/bin/python3` (3.9.6). Exact table arithmetic over
GF(q) built in-script (add/mul/inv tables, field axioms asserted); **no floating point is
constructed anywhere in either script**. Everything PROVISIONAL (不可自宣); nothing outward.

| script | log | what it is |
|---|---|---|
| `problems/k1695/round3_census.py` | `logs/k1695/round3_census.log` (28.9 s, cap 1500 s) | in-repo reproduction + extension of selection probe P-K1 |
| `problems/k1695/round3_family.py` | `logs/k1695/round3_family.log` (cap 2400 s) | criterion C1 + the family census |

## R3.1 · P-K1 reproduced IN-REPO and extended — and one hypothesis killed
`round3_census.py` re-runs the selection probe's question over a **wider** window and adds the
cycle-type structure P-K1 never recorded.

**Controls, all asserted before any census row (a failure aborts the run):**
NEG-1 identity judged NOT cyclic; NEG-2 `2I` judged NOT cyclic; POS-1 companion of `x^n-1`
judged cyclic — each for q ∈ {2,3,4,5,7,8,9} × n ∈ {2,3,4}. POS-2 enumerated `|GL(n,q)|` equals
`∏(q^n−q^i)` in every cell. **KAT-1/2 (known-answer, reproducing an INDEPENDENT prior result):**
over GF(2), `A=J−I`, n=6 — no n-cycle works but `(5,1)` does; n=4 — an n-cycle does work.
Both matched `k1695_state.md` §R8 exactly. **KAT-3:** the good-permutation counts for `A=J−I`
came out **14** at (q=2,n=4), **5** at (q=3,n=3), **8** at (q=5,n=4), **144** at (q=2,n=6) —
the four numbers §R4 of round 2 reports, recomputed from scratch by different code.

**Census result: 1 713 018 invertible matrices over 12 cells, 0 counterexamples to 16.95.**
Cells: GL(2,q) for q ∈ {2,3,4,5,7,8,9}, GL(3,q) for q ∈ {2,3,4,5}, GL(4,2).
⭐ **`q = 4, 8, 9` are NON-PRIME fields — P-K1's own stated frontier ("non-prime fields") is
now partly closed**, at n = 2,3.

**Two structural hypotheses, both refutable by one matrix:**
- **H1 — some P with AT MOST TWO CYCLES always works: 0 violations in all 1 713 018.**
- **H2 — some P of type `(n)` or `(n−1,1)` always works: FALSE.** 6 matrices in GL(4,2) need
  type `(2,2)`; first one printed in the log is
  `A = [[0,0,0,1],[1,0,1,1],[1,1,0,1],[1,0,0,0]]`. **H2 is dead for general A** — worth knowing,
  because §R3.3 shows it is nevertheless TRUE on the whole rank-one-over-monomial family.
- first-success histogram: the n-cycle wins on all but 194 of the 1 713 018 (e.g. 96 of the
  1 488 000 in GL(3,5) need `(2,1)`).

## R3.2 · ⭐ CRITERION C1 — cyclicity of `D P_π + u wᵀ` for π an n-cycle, any field
**Why this family.** For **n = 3 every counterexample to 16.95 must lie in it**: if `A ∈ GL(3,F)`
is not cyclic then `P = I` already fails, so `A` is derogatory, so some eigenvalue has geometric
multiplicity ≥ 2, i.e. `rank(A − λI) ≤ 1`; and λ ∈ F by the invariant-factor argument of
§R3.6 Step 2 (geometric multiplicity ≥ 2 forces `m_λ²` | charpoly, so `2·deg m_λ ≤ 3`; no
separability is used). So `A = λI + u vᵀ`.
More generally `A = N + uvᵀ` (N monomial) is the **maximally derogatory** stratum and the
natural home of round 2's `aI+bJ` theorem (`N = aI`, `u = b·1`, `v = 1`).

**The reduction (proved, and it is what makes the scan reach n = 12).** With `N = D P_τ`,
`A P_σ = D P_π + u wᵀ` where `π = τσ` and `w_i = ṽ_{π(i)}`, `ṽ_j := v_{τ^{-1}(j)}`. As σ runs
over `S_n` so does π. Conjugating by `P_ρ` permutes the **triples** `(d_j, u_j, ṽ_j)`
simultaneously and conjugates π — so the answer depends only on the **multiset of triples**.

**The criterion.** Put the tokens in a cyclic order, `Dp_j = d_0⋯d_j`, `δ = Dp_{n−1}`,
`w_i = ṽ_{i+1 mod n}`. Then `M = D P_c + u wᵀ` is **cyclic ⟺ gcd(χ, Pu, Pw, Pα − δ) = 1` in F[x]**,
where `χ = x^n − δ` and
`Pu = Σ_j (u_j/Dp_j) x^{j+1}`, `Pw = Σ_j w_j Dp_j x^{n−1−j}`,
`Pα = Σ_{t≤j} w_j u_t (Dp_j/Dp_t) x^{n−1+t−j}`.
Derivation: `nullity(X + uwᵀ) = dim(ker X ∩ wᵀ⊥) + ε`, `ε = 1` iff `∃x: Xx = −u, wᵀx = 1`;
at `X = D P_c − λ` the kernel is `z_j = λ^{-j}Dp_j`, the left kernel `y_j = λ^{j}/Dp_j`, and the
three clauses are `wᵀz = 0`, `yᵀu = 0`, `α = 1` — the three polynomials above.

**Validated against brute force: 312 888 rows, 0 disagreements** (17 grids, q ∈ {2,3,4,5},
n ∈ {2,3,4,5}, exhaustive over tokens where the grid is small enough, deterministic spread
otherwise; brute force = independent minimal-polynomial-degree computation, no shared code path).
⚠️ §90 vacuity control asserted per grid: the criterion must say "cyclic" on some rows and
"not cyclic" on others — e.g. 228/256 at (q=2,n=4), 101 136/104 976 at (q=3,n=4). A predicate
that always answered yes would have failed the assert.
**KAT before coding:** hand-computed on §R8's two known answers — (q=2,n=6,A=J−I) gcd = `x+1`
(not cyclic ✓) and (q=2,n=4) gcd = `1` (cyclic ✓). Both matched.

## R3.3 · ⭐ FAMILY CENSUS — the refutation frontier, pushed from n = 4 to n = 12
The multiset reduction makes this stratum searchable far past the GL(n,q) wall. Every "this
permutation works" reported by C1 is **re-verified by the brute-force oracle** before it counts
(a rejected witness aborts the run); "no permutation works" is only reported after an exhaustive
search, otherwise the case is printed as UNRESOLVED.

**811 517 token multisets over 24 completed cells: 0 counterexamples, 0 unresolved.**
Cells: q=2 (n=3..11), q=3 (n=3..8), q=4 (n=3,4,5), q=5 (n=3,4,5), q=7,8,9 (n=3);
`D` ranged over all invertible diagonals in the smaller cells (`D=var`), `D=I` in the larger.
⚠️ **The q=2, n=12 cell did NOT complete and is not counted.** Its numbers are absent, not
zero. Cause, recorded because it is a process defect and not a mathematical one: the script's
hard wall cap was polled only every 2000 multisets, and the n=12 cell has 455, so the cap could
not fire inside it (n=11 alone took 1 250.9 s). The cell was killed at 48 min. The gate is now
polled per item — the fix is in `round3_family.py`, not in a note (VERIFY_CHECKLIST D.14).

⭐ **The headline: 397 multisets admit NO n-cycle at all — and type `(n−1,1)` works for
every single one of them. 397/397. No other fallback type was ever needed**, across 7 fields,
n = 3…11, and general monomial `D`.
⟹ **CONJECTURE T1 (provisional, census-backed):** for every `A = N + uvᵀ ∈ GL(n,F)` with `N`
monomial, a permutation of cycle type `(n)` or `(n−1,1)` makes `AP` cyclic — i.e. round 2's
two-branch witness for `aI+bJ` survives verbatim on a vastly larger family.
Note the contrast with §R3.1: `(n)`-or-`(n−1,1)` is FALSE for general `A` (H2, 6 counterexamples
in GL(4,2)) but holds on all 811 153 rows of this family.

**The hard multisets are structured, and the criterion explains them.** Every fallback case has
`u` and `ṽ` supported on the same token set with proportional values. For `u = a·1_S`,
`ṽ = b·1_S`, `|S| = k`, the λ=1 clause computes in closed form to `α = ab·k(k+1)/2`, so the
n-cycle fails at λ=1 exactly when `p | k` and `ab·k(k+1)/2 = 1` — in characteristic 2 that is
`ab = 1` and `k ≡ 2 (mod 4)`. At `k = n` this is **exactly §R8's infinite family** (char 2,
n ≡ 2 mod 4); the census's q=2 fallback rows are `k = 2, 6, 10` — every one `≡ 2 mod 4` ✓.
So R8 was the `k = n` slice of a `k`-parameter phenomenon.

## R3.4 · What is proved outright (no census, all n, all F)
1. **`u = 0` or `v = 0`** ⟹ `A` is monomial and an n-cycle makes `AP` the companion matrix of
   `x^n − δ` ⟹ cyclic. ∎
2. **`u` or `ṽ` has exactly ONE nonzero coordinate** ⟹ `Pu` (resp. `Pw`) is a single monomial,
   never zero at a root of `χ` (δ ≠ 0) ⟹ clause (ii) (resp. (i)) fails at every λ ⟹ **every**
   n-cycle works. ∎
3. **At most two cycles.** For `A = aI + uvᵀ` (`a ≠ 0`), any π with `r ≥ 3` cycles gives
   `nullity(aP_π − λ) ≥ r` at `λ = a`, and a rank-one perturbation lowers nullity by at most 1,
   so `AP_π` is derogatory. **The search space for this family is provably `≤ 2` cycles.** ∎
4. **Fixed-point lemma.** For type `(n−1,1)` with fixed point `f`, the eigenvalue contributed by
   `f` is harmless as soon as `u_f ≠ 0` and `ṽ_f ≠ 0` (clauses (i),(ii) there read `w_f = ṽ_f`
   and `y ᵀu = u_f`); the remaining eigenvalues reduce to the `(n−1)`-cycle problem on the
   sub-multiset. This is the mechanism behind the 397/397. ∎
5. **n = 3 reduction** (stated in R3.2): every n = 3 counterexample is `λI + uvᵀ`, λ ∈ F. ∎

## R3.5 · Limitations, printed beside the results
- **16.95 in general is exactly as open as before.** T1 is a conjecture about a stratum; the
  proved items in §R3.4 are lemmas, not the theorem. No claim otherwise is made anywhere.
- The family census is a CENSUS with its window stated (7 fields, n ≤ 10 completed at the time
  of writing, `D=I` in the larger cells). It is not a proof for the family.
- C1 is proved only for π an **n-cycle**. The `(n−1,1)` outcomes in the census come from brute
  force, not from a criterion — the two-cycle criterion is not derived yet.
- Fields computed: GF(q) for q ∈ {2,3,4,5,7,8,9}. **No infinite field was computed this round**
  (round 2 did ℚ). The criterion is characteristic-uniform in form, but that is an argument,
  not an enumeration, and the distinction is on the record.
- Novelty of C1 and T1: **UNCHECKED this round.** `k1695_litcheck.md` searched the `aI+bJ`
  criterion and found nothing; C1 is strictly more general and has NOT been searched. Nothing
  travels outward.

## R3.6 · ⭐ THEOREM — Kourovka 16.95 holds for n ≤ 3, over EVERY field
This is a **closed case of the conjecture**, not a family result: it settles the statement for
all `A ∈ GL(n,F)`, `n ≤ 3`, `F` arbitrary (finite or infinite, any characteristic).

**Notation.** `P_π` is the permutation matrix with `P_π e_j = e_{π(j)}`; `A P_π` permutes columns.
`S_u = u_1+u_2+u_3`. "Cyclic" = nonderogatory = minpoly equals charpoly ⟺ `dim ker(M−λI) ≤ 1`
for every `λ ∈ F̄`.

**Lemma 0 (nullity of a rank-one update).** For `X ∈ M_n(F̄)`, `u,w ∈ F̄^n`, `K = ker X`:
`nullity(X + uwᵀ) = dim(K ∩ wᵀ⊥) + ε`, where `ε = 1` iff there is `x` with `Xx = −u` and
`wᵀx = 1`, else `ε = 0`.
*Proof.* `ker(X+uwᵀ) = {x : Xx = −(wᵀx)u}`; the functional `x ↦ wᵀx` on it has kernel
`K ∩ wᵀ⊥` and image `0` or `F̄`, the latter exactly under the stated condition. ∎

**Step 1.** If `A` is cyclic take `P = I`. So assume `A` derogatory: some `λ ∈ F̄` has
`dim ker(A−λ) ≥ 2`.

**Step 2 (reduction).** `λ ∈ F`. Let `m ∈ F[x]` be the minimal polynomial of `λ` over `F` and
let `F³ ≅ ⊕_i F[x]/(f_i)`, `f_1 | … | f_r`, be the invariant-factor decomposition of the
`F[x]`-module. Over `F̄` each summand with `m | f_i` contributes exactly 1 to `dim ker(A−λI)`
and each other summand contributes 0, so `dim ker(A−λI) = #{i : m | f_i} ≥ 2`; hence `m² `
divides `f_{r−1}f_r`, which divides the characteristic polynomial, so `2·deg m ≤ 3` and
`deg m = 1`, i.e. `λ ∈ F`. Then `rank(A − λI) ≤ 1`, and `λ ≠ 0` since `A` is invertible, so
`A = λ(I + uvᵀ)` for some `u,v ∈ F³`.
⚠️ **Repair, 2026-08-24, found by the codex adversarial pass (§R3.10) and re-derived
independently before adoption.** The first draft of this step argued by counting the DISTINCT
Galois conjugates of `λ`. That count is wrong over an imperfect field: an inseparable `λ` of
degree `d` has fewer than `d` distinct conjugates, so `2d ≤ 3` did not follow. The
invariant-factor argument above needs no separability and holds in every characteristic; the
conclusion is unchanged. This is exactly what the adversarial pass was dispatched to find. Cyclicity of `AP` is invariant under
nonzero scaling, so **WLOG `A = I + uvᵀ`**, invertible ⟺ `1 + vᵀu ≠ 0`. If `u = 0` or `v = 0`
then `A = I` and any 3-cycle `P` gives `AP = P`, the companion matrix of `x³−1`: cyclic. So
assume `u,v ≠ 0`.
*(Machine-checked exhaustively, `RED-1`: over GL(3,q), q ≤ 5, all 15 710 non-cyclic invertible
matrices are of this form.)*

**Step 3 (exact criterion for a transposition).** Let `π = (i j)` with fixed point `k`, and
`M = A P_π = P_π + u wᵀ`, `w_t = v_{π(t)}`. `spec(P_π) ⊆ {1,−1}`, so by Lemma 0 only `λ = ±1`
can make `M` derogatory. Computing `ker(P_π − 1) = ⟨e_i+e_j, e_k⟩` and (char ≠ 2)
`ker(P_π + 1) = ⟨e_i − e_j⟩`, Lemma 0 gives: **`M` is NOT cyclic ⟺ (T1) or (T2)**, where
- **(T1)** `[S_v = 0 and v_k = 0]` or `[S_u = 0 and u_k = 0]`  — the `λ=1` failure;
- **(T2)** `char F ≠ 2`, `u_i = u_j`, `v_i = v_j`, and `u_i v_i + u_k v_k/2 = −1` — the `λ=−1`
  failure (the free parameter in `x` cancels, so `α` is well defined).

**Step 4 (the case analysis).** Suppose, for contradiction, that all six permutations fail.
Note `u ≠ 0, S_u = 0` forces at most one `u_t = 0` (two zeros would force the third).
- **`S_u ≠ 0` and `S_v ≠ 0`.** (T1) is impossible, so every transposition fails by (T2); running
  it for `k=1,2,3` gives `u_1=u_2=u_3=a`, `v_1=v_2=v_3=b` (`a,b ≠ 0`) and `3ab/2 = −1`, so
  `char ∉ {2,3}` and `ab = −2/3`. Now take a 3-cycle: `A P = P_c + abJ`. At `λ=1`,
  clause (ii) reads `3a ≠ 0` ✓, so `λ=1` is not a failure. At a primitive cube root `ω`,
  `Σ_i ω^i = 0` kills clauses (i) and (ii), and the third clause computes to
  `α = ab(3ω²+2ω+1) = −ab(2+ω)`; `α = 1` would give `(−2/3)(2+ω) = −1`, i.e. `ω = −1/2`,
  whence `ω³ = 1` forces `9 = 0`, i.e. `char = 3` — excluded. So `α ≠ 1` and **the 3-cycle
  works**. Contradiction.
- **`S_u = 0`, `S_v ≠ 0`.** A transposition can fail by (T1) only via `u_k = 0`, which happens
  for at most one `k`; so at least two transpositions fail by (T2), which as above forces
  `u = a1` and `v = b1` with `a ≠ 0`. Then `S_u = 3a = 0` gives `char = 3`, hence `S_v = 3b = 0`
  — contradicting `S_v ≠ 0`.
- **`S_u ≠ 0`, `S_v = 0`.** Symmetric: two (T2) failures force `u = a1, v = b1`; `S_u = 3a ≠ 0`
  gives `char ≠ 3`, so `S_v = 3b = 0` forces `b = 0`, i.e. `v = 0` — excluded.
- **`S_u = S_v = 0`.** (T1) for `k` reduces to `u_k = 0 or v_k = 0`; at most one `u_t` and at
  most one `v_t` vanish, so some `k` escapes (T1). If two such `k` exist, (T2) at both forces
  `u = a1, v = b1`, so `3a = 0` with `a ≠ 0`, i.e. `char = 3`, and then (T2)'s equation reads
  `3ab/2 = 0 = −1` — false, so that transposition works. If exactly one such `k` exists, the
  other two indices each have `u_t = 0` or `v_t = 0`; since `u` and `v` each have at most one
  zero coordinate, one of the two indices kills `u` and the other kills `v`; the transposition
  fixing `k` then moves a pair `{i,j}` with `u_i ≠ u_j` (one of them is 0, the other is not, as
  `u` has a single zero), so (T2) fails and **that transposition works**. Contradiction. ∎

**Corollary.** With the trivial `n ≤ 2` case (for `n = 2` a derogatory invertible `A` is scalar
`λI`, and `λ·(swap)` has minimal polynomial `x²−λ²` of degree 2 in every characteristic),
**Kourovka 16.95 holds for every field and every `n ≤ 3`.**

### Machine verification of R3.6 — `problems/k1695/round3_n3_theorem.py`, `logs/k1695/round3_n3.log`
The proof is CONSTRUCTIVE, so its decision rule was implemented and its named witness checked
by a minimal-polynomial oracle sharing no logic with the rule.
| check | result |
|---|---|
| POS-1 oracle controls (`I` non-cyclic, companion cyclic), q ∈ {2,3,4,5,7,8,9} | pass |
| RED-1 Step-2 reduction, exhaustive over GL(3,q), q ≤ 5 | 15 710 non-cyclic matrices, **all** of the form `λ(I+uvᵀ)` |
| **PROOF RULE** on every invertible `I+uvᵀ` over GF(q), q ∈ {2,3,4,5,7,8,9} | **818 948 / 818 948 witnesses correct, 0 failures** |
| NEG-1 "always return `P=I`" | **0 / 818 948** — fails on every single input, so the test is not vacuous |
| NEG-2 clause (T2) deleted | fails in char ≠ 2 (24 at q=3, 120 at q=5, 336 at q=7, 720 at q=9) and **provably cannot** fail in char 2 (T2 is vacuous there) — matching the proof's own characteristic split |
| NEG-3 clause (T1) deleted | fails at every q (5 at q=2 … 10 296 at q=9) |
⚠️ §90: the entitled numbers are the **negative** ones. A rule that named a witness at random
would fail NEG-1's pattern; both clauses are demonstrably load-bearing, and NEG-2's char-2
vacuity is a prediction of the proof that the run confirms rather than a gap in the test.

## R3.7 · ⭐ THE NAMED REFUTATION FRONTIER IS CLOSED — `round3_frontier.c`
`notes/selection/selection_0824.md` recorded the frontier as *"n=4 q≥3 / n=5 q=2 / non-prime
fields — engine-scale, never local"*. Reimplemented in C (exact table arithmetic, no floating
point), it took **90.8 s** in one single-threaded process. Same control battery as the Python
census (NEG-1/NEG-2/POS-1 over 7 fields × 3 sizes; POS-2 population identity; the R8
known-answer test), all passing in this independent implementation.

| cell | invertible matrices | POS-2 | needed fallback | H2 violations | H1 violations | **counterexamples** |
|---|---|---|---|---|---|---|
| GL(3,7) | 33 784 128 | ✓ | 900 | 0 | 0 | **0** |
| GL(3,8) | 115 379 712 | ✓ | 441 | 0 | 0 | **0** |
| GL(3,9) | 339 655 680 | ✓ | 648 | 0 | 0 | **0** |
| **GL(4,3)** | 24 261 120 | ✓ | 552 | 24 | 0 | **0** |
| **GL(5,2)** | 9 999 360 | ✓ | 150 | 30 | 0 | **0** |

**523 080 000 invertible matrices, 0 counterexamples.** Together with §R3.1 the census now
stands at **≈ 524.8 million** invertible matrices over 17 cells with zero counterexamples and
**zero H1 violations** — every one of them has a good permutation with at most two cycles.
The frontier moves to n=4 q≥4, n=5 q≥3, n=6 q=2.
⚠️ This is a CENSUS with its window stated. It is not evidence about large n, and §R3.1's H2
counterexamples (now 6+24+30 = 60 of them) show that "small-case pattern ⟹ theorem" is exactly
the inference that already failed once this round.

## R3.8 · The λ=1 layer of the family problem — lemmas toward T1
`problems/k1695/round3_lambda1.py`, `logs/k1695/round3_lambda1.log`. For `A = I + uvᵀ`
(`D = I`, so `λ=1` is a resonance of EVERY cycle) the clauses (i),(ii) at `λ=1` are the plain
cycle sums, hence **arrangement-independent**; only the third clause moves. Write
`e(σ) := Σ_{t<k} u_{σ(t)} v_{σ(k)}` for the cyclic arrangement σ.

| lemma | statement | check |
|---|---|---|
| **L1** | an n-cycle fails **at λ=1** ⟺ `S_u = 0` ∧ `S_v = 0` ∧ `e(σ) = 1` | 210 763 arrangements vs criterion C1's `(x−1) | gcd`, **0 disagreements**; both sides of the equivalence occur (2 914 fail / 207 849 ok) so it is not vacuous |
| **L2** | `e` is rotation-invariant when `S_u = S_v = 0` (it must be — rotation is conjugation by a power of the cycle) | 34 839 rotations, 0 violations |
| **L3** | ⭐ **SWAP LEMMA**: swapping two adjacent tokens `a,b` changes `e` by exactly `u_b v_a − u_a v_b`, the 2×2 determinant of the two tokens | 555 229 adjacent swaps, 0 violations |
| **L4** | ⭐ **DICHOTOMY** (corollary of L3): if two tokens are non-proportional, `e` takes ≥ 2 values, so **some arrangement has `e ≠ 1` and λ=1 is never the obstruction**; if all tokens are pairwise proportional then `e` is constant — and that happens exactly when `v` is a scalar multiple of `u` | 1 169 all-proportional multisets (e constant ✓), 23 988 with a non-proportional pair (e takes ≥2 values ✓); of the latter 15 885 have `e = 1` for SOME arrangement, and every one of them has another arrangement that escapes |
| **L5** | for a 2-cycle type `(C₁,C₂)`, failure at λ=1 ⟺ `[Σ_{C₁}v = 0 ∧ Σ_{C₂}v = 0]` or `[Σ_{C₁}u = 0 ∧ Σ_{C₂}u = 0]` | 4 564 predicted failures, every one confirmed non-cyclic by brute force |

**What this buys.** L4 collapses the λ=1 layer to a single residual case — `v = ρu` — and L5
says that in that case a split with `Σ_{C₁}u ≠ 0` fixes λ=1, which always exists (`C₁ = {f}`,
`u_f ≠ 0`). **So the λ=1 layer of T1 is finished; what remains is the λ ≠ 1 layer**, i.e. the
arrangement problem for the non-trivial roots of `x^ℓ − δ`. Two facts already pin its shape:
(a) if `n` is a power of `char F` then λ=1 is the ONLY resonance and T1 follows for such `n`
except in the residual `v = ρu` case; (b) the λ≠1 obstruction is real, not an artifact — the
census's `q=7, n=3` fallbacks obstruct at `λ = 4 ≠ 1` (gcd `x+3`, and `4³ = 1` in 𝔽₇).

## R3.9 · ⚠️ NOVELTY POSTURE — criterion C1 is expected to be KNOWN, and is not claimed
Recorded before the check comes back, so the check cannot be graded against how it feels.
A monomial cyclic matrix is diagonalisable over a splitting field; in that basis C1 becomes
the standard eigenstructure of a **diagonal-plus-rank-one (DPR1)** matrix, where "λ = d_i is
a multiple eigenvalue iff the two eigenvector clauses hold plus a secular condition" is
textbook (Golub 1973; Bunch–Nielsen–Sorensen 1978 — but see §R4.3: that paper is the REAL
SYMMETRIC eigenproblem, so it cannot serve as the arbitrary-field citation), and in
control-theoretic dress it is the
Popov–Belevitch–Hautus test — which `k1695_litcheck.md` §Q2.1 already flagged (Ferrante–Wimmer,
ELA 20 (2010) 95–102) as the nearest classical framework to round 2's derivation.
**C1's value here is as a TOOL** — it reproduces round 2's `aI+bJ` criterion from a strictly
more general starting point and is what made the n = 12 family scan possible — **not as a
novel theorem, and it is not claimed as one.** The open citation question (a statement valid
over an arbitrary field, and whether the third/secular clause appears explicitly) is dispatched
as `engine/briefs/k1695_r3_novelty/BRIEF.md`. Per VERIFY_CHECKLIST C.11, "no name found" for a
self-invented object is a WEAK negative: cite, don't claim.

## R3.10 · Adversarial pass on the n≤3 theorem — PRE-REGISTERED acceptance conditions
Dispatched to codex (`gpt-5.6-sol`) as `engine/briefs/k1695_r3_adv/TASK.md`, held-out design:
it receives the proof text and the criterion but **not** the verifier's witness tables, its
818 948-row output, or the negative-control results, so agreement is reconstruction rather
than parroting (VERIFY_CHECKLIST B.8/B.9). Written down BEFORE the answer arrives
(VERIFY_CHECKLIST D.15):
1. The pass counts as CLEAN only if the engine's own independent exhaustive search over
   GF(q), q ∈ {2,3,4,5,7,8,9} (non-prime fields included), finds **no** `A = I+uvᵀ` for which
   all six permutations fail, **and** its independent re-derivation of Step 3 returns (T1),(T2)
   or names a specific discrepancy.
2. A DEFECT counts only if it names a concrete `(F,u,v)` I can re-run, or a specific inference
   step with a stated reason. Prose of the form "this looks right/wrong" counts for nothing —
   measured engine profile is checklist-completeness ~10/10, derivation validity ~2/15.
3. If the engine reports zero disagreements without printing a negative control that FAILED,
   the run is VOID, not clean.
4. This is ONE family. A clean pass banks as "same-family found nothing", never as "verified".

### RESULT of the adversarial pass, graded against the pre-registration above
Report: `engine/out/codex/k1695_n3_adversarial.md` (19 763 bytes, ends `DONE-K3-ADV`, 13m15s,
`gpt-5.6-sol high`). Channel = OpenAI, a genuinely different family from this line's own
reasoning, so this is a cross-family pass, not a same-family one.

| pre-registered condition | outcome |
|---|---|
| independent exhaustive search, 7 fields incl. non-prime, no `A = I+uvᵀ` with all six permutations failing | **met** — its own script, its own oracle: 818 948 valid `(u,v)` pairs / 112 514 distinct invertible matrices, **0 counterexamples**. Its population figure 818 948 reproduces this line's independently, from different code |
| independent re-derivation of Step 3 returns (T1),(T2) or names a discrepancy | **met** — re-derived; **0 Step-3 IFF disagreements** across all seven fields |
| a DEFECT must name a concrete case or a specific inference with a reason | **met — and it found one**, see below |
| a negative control that FAILED must be printed, else VOID | **met** — `negative-control-identity-cyclic: False` printed for every field |

⭐ **DEFECT FOUND (real, and now repaired).** Step 2's original justification counted the
DISTINCT Galois conjugates of λ. Over an imperfect field that count is wrong, with an explicit
witness: `F = 𝔽₂(s)`, λ a root of `x²−s`, has `[F(λ):F] = 2` but `x²−s = (x−λ)²` over `F̄`, so
λ has ONE distinct conjugate and `2d ≤ 3` does not follow. **The theorem's conclusion is
untouched** — §R3.6 Step 2 now carries an invariant-factor argument that uses no separability
and generalises to every n (`2·deg m_λ ≤ n`), derived independently here before the engine's
own repair was read. The engine additionally supplied a **second, independent repair**: all
2×2 minors of `A − λI` vanish, so picking `A_{ij} ≠ 0` off-diagonal and the third index `k`
gives `λ = A_{kk} − A_{ik}A_{kj}/A_{ij} ∈ F` outright (and if `A` is diagonal, λ is a diagonal
entry). Two independent routes to the same conclusion — convergent reconstruction, which
VERIFY_CHECKLIST B.8 counts as strong support, not proof.

**Other findings:** the engine worked all four Step-4 bullets and found no escape, and it
supplied a cleaner justification for the one step this line had flagged as weakest — bullet 4's
"one index kills `u`, the other kills `v`" — namely that if the two zero positions coincided,
**two** indices rather than one would escape (T1), contradicting that branch's hypothesis.
That phrasing is adopted.
**Engine limits, as stated by it:** n = 3 only, seven finite fields only, no infinite field.

## R3.11 · n = 4: the two strata identified, and the second one probed
`problems/k1695/round3_n4_stratumB.py`. For n = 4 the same invariant-factor count that made n = 3
collapse (§R3.6 Step 2: geometric multiplicity ≥ 2 forces `m_λ²` | charpoly, so
`2·deg m_λ ≤ 4`) leaves **exactly two** strata for a counterexample:
- **(a)** `λ ∈ F` ⟹ `rank(A − λI) ≤ 2`, i.e. `A = λ(I + U Wᵀ)` with `U,W ∈ F^{4×2}` — a
  rank-≤2 perturbation of a scalar. This is where the H2 violators live: the first GL(4,2)
  violator, `A = [[0,0,0,1],[1,0,1,1],[1,1,0,1],[1,0,0,0]]`, has `rank(A+I) = 2` exactly.
- **(b)** `λ` of degree 2 ⟹ charpoly `= f²`, geometric multiplicity 2 at each root, invariant
  factors `(f,f)`, i.e. **`minpoly(A) = f`, an irreducible quadratic**. Not reachable by any
  rank-one/rank-two-over-a-scalar argument: over F, A is not near a scalar at all.

**Stratum (b), probed exhaustively (orbit BFS from `C_f ⊕ C_f`, conjugation by GL(4,q)
generators).** Population control: each orbit's size must equal `|GL(4,q)|/|GL(2,q²)|` — a BFS
that closed early would be caught, and none was.
| q | irreducible quadratics | class size | stratum-(b) matrices | counterexamples | some 4-cycle works | ALL six 4-cycles work | #good permutations (of 24) |
|---|---|---|---|---|---|---|---|
| 2 | 1 | 112 | 112 | **0** | **112/112** | 28 (25%) | 19–23 |
| 3 | 3 | 4 212 | 12 636 | **0** | **12 636/12 636** | 10 584 (83.8%) | 10–23 |
⭐ **In stratum (b) a 4-cycle always works** (12 748/12 748), and these matrices are far from
tight — the worst has 10 good permutations out of 24, versus the rank-one family where the
good fraction is `Θ(log n/n)`. A partial obstruction is already visible for the proof: if
`AP` (P a 4-cycle, an ODD permutation) were itself of stratum-(b) shape with minpoly
`x²+b₁x+b₀`, then `det(AP) = b₀²` while `det(AP) = det(A)·sgn(P) = −c₀²`, forcing `−1` to be a
square in F. So over fields where `−1` is a non-square, a 4-cycle's failure would have to come
from an eigenvalue **in F** — a real constraint, not yet a proof.
⚠️ Limits: q ∈ {2,3} only (the orbit BFS is exhaustive there; larger q needs the C route);
stratum (a) is NOT probed here beyond the full GL(4,2)/GL(4,3) census of §R3.1/§R3.7.

## R3.12 · Round-3 summary and the state of the attack
**Closed:** 16.95 for n ≤ 3 over every field (§R3.6, machine-checked with load-bearing
negative controls). **Frontier:** ≈524.8M invertible matrices over 17 cells, 0 counterexamples;
the frontier named at selection time is fully closed and now sits at n=4 q≥4, n=5 q≥3, n=6 q=2.
**Tools:** criterion C1 (all n, monomial-cycle + rank one; expected classical, novelty check in
flight); the multiset reduction that made an n = 12 family scan possible.
**Conjectures with evidence:** T1 (family, two-branch witness, 397/397); H1 (≤2 cycles,
0 violations in ≈524.8M). **Killed:** H2.
**Where the general proof stands.** For `A = aI + uvᵀ` the λ=1 layer is FINISHED (§R3.8: the
swap lemma reduces it to the single case `v = ρu`, which L5 then handles by a cycle split).
The open piece is the **λ ≠ 1 layer** — the arrangement problem for the non-trivial roots of
`x^ℓ − δ` — where the obstruction is genuinely present (the q=7,n=3 fallbacks obstruct at
λ = 4). Next round: (1) the λ≠1 layer, using the swap identity `ΔÛ(λ) = (u_b−u_a)λ^s(1−λ)`,
which is nonzero at EVERY λ ≠ 1 simultaneously — the tool that makes joint control plausible;
(2) n = 4 = stratum (a) rank-2 Woodbury + stratum (b) via the determinant/sgn obstruction;
(3) Lean, once one of these is stable enough to be worth formalising.

## R3.13 · ⭐ SLACK MEASUREMENT — how close is the family to an actual counterexample?
`problems/k1695/round3_slack.py`. "No counterexample found" is the wrong statistic for a
refutation frontier; the right one is how many witnesses the HARDEST inputs still have. Round 2
already lost one bet of this shape ("most permutations work" was a small-n illusion; the true
density is `Θ(log n/n)`), so this is measured, not extrapolated.

For every token multiset with **no** good n-cycle, count (i) how many fixed points `f` give a
good `(n−1,1)`, and (ii) how many `(n−1,1)` permutations are good in total.

| n | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| min # good fixed points (q=2) | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| min # good `(n−1,1)` perms (q=2) | 2 | 4 | 12 | 48 | 240 | 1440 | 10080 |
(q=3, n = 3…7: identical minima, 2 and 2·(n−2)!.)

Two exact regularities, both meaningful:
1. **min #good f = 2, never 1**, at every n and both fields — and the tightest multisets are
   always the same shape: `n−2` zero tokens plus two nonzero ones (q=2: `(1,1)` twice; q=3:
   `(1,2)` and `(2,1)`). The 2 is not a coincidence: §R3.4's fixed-point lemma says `f` is
   harmless when `u_f ≠ 0` and `ṽ_f ≠ 0`, and in these multisets **exactly two tokens qualify**.
   The lemma is therefore TIGHT, not merely sufficient.
2. **min #good `(n−1,1)` = 2·(n−2)!** exactly — i.e. once `f` is one of the two good fixed
   points, EVERY cyclic arrangement of the remaining `n−1` tokens works. The witness set grows
   factorially; it is not thinning.

⭐ **This turns the refutation question into a precise recipe.** By the fixed-point lemma the
`λ=1` clause for type `(n−1,1)` fails only when `[ṽ_f = 0 ∧ S_v = 0]` or `[u_f = 0 ∧ S_u = 0]`.
So a counterexample built this way needs **`S_u = S_v = 0` AND no token with both coordinates
nonzero** (disjoint supports) — then `λ=1` kills every `(n−1,1)` at once. But then the two
token types `(a,0)` and `(0,b)` are non-proportional, so by the dichotomy L4 the `λ=1` clause
of the **n-cycle** can always be escaped, and by L5 a split with `Σ_{C₁}u ≠ 0 ≠ Σ_{C₁}v` also
escapes it. Every road out of `λ=1` therefore exists; **the whole remaining question for this
family is the `λ ≠ 1` layer.** That is now the single named gap, and it is where round 4 goes.

## R3.14 · ⭐ THE OBSTRUCTION IS (ALMOST ENTIRELY) SEPARABLE — round 4's proof shape
`problems/k1695/round3_joint.py`. Before attacking the λ≠1 layer it matters whether the two
layers can be handled independently. For every multiset with no good n-cycle, ask whether some
arrangement is clean at λ=1, and whether some (possibly different) arrangement is clean away
from λ=1. Criterion C1 supplies the bad set as the roots of one gcd `g`: λ=1 is bad iff
`(x−1) | g`; some λ≠1 is bad iff `g` still has a nonconstant part after every factor `(x−1)`
is divided out.

| q | n | multisets | no n-cycle | λ≠1 layer unfixable | λ=1 layer unfixable | **JOINT-only** |
|---|---|---|---|---|---|---|
| 2 | 3–7 | 189 | 7 | 0 | 7 | 0 |
| 3 | 3–6 | 3 339 | 15 | 4 | 11 | 0 |
| 4 | 3–5 | 15 252 | 29 | 9 | 12 | **2** |

⭐ **The two layers partition the failures almost perfectly.** Of 51 multisets with no good
n-cycle, 49 fail because ONE layer is unfixable on its own; only **2** (both q=4, n=3, e.g.
tokens `(1,1,2),(1,2,1),(1,3,3)`) are joint-only — an arrangement exists that is clean at λ=1,
another that is clean away from λ=1, and none that is clean at both.
⟹ **Round 4's proof of T1 can be modular**: prove the λ≠1 layer separately (the λ=1 layer is
already done, §R3.8), then treat the joint cases as a small, explicitly characterised residue.
⚠️ Window: q ∈ {2,3,4}, n ≤ 7, D = I. The joint cases only appeared at q=4, so their density
at larger q is unmeasured — do not assume 2 is the whole story.

---

# ROUND 4 (v5, 2026-08-24) — the λ ≠ 1 layer
Everything PROVISIONAL. Interpreter `.venv/bin/python3`; exact table arithmetic; no floating point.

## R4.1 · ⭐ THE TIGHTEST CASE IS SOLVED IN CLOSED FORM — `problems/k1695/round4_k2.py`
§R3.13 identified where the family bottoms out: multisets with exactly TWO tokens carrying
nonzero coordinates and `n−2` null tokens `(0,0)`. For those the λ≠1 layer is now settled.

**Setup.** Put the two live tokens `(u₁,v₁)`, `(u₂,v₂)` at cyclic distance `g ∈ {1,…,n−1}` —
`g` is ours to choose, since the null tokens go anywhere. For `λ^n = 1`:
`Û(λ) = 0 ⟺ λ^g = c₁ := −u₁/u₂`, and `V̂(λ) = 0 ⟺ λ^g = c₂ := −v₂/v₁`.

**Closed form.** Let `m = n/p^e` be the number of distinct n-th roots of unity.
1. **`c₁ ≠ c₂` ⟹ no λ is ever a bad candidate**, for any gap: the two eigenvector clauses can
   never hold at the same λ. The n-cycle wins outright.
2. **`c₁ = c₂ = c`**: since `λ^g` ranges over the subgroup of `μ_m` of index `gcd(m,g)`, a bad
   candidate exists ⟺ `ord(c) | m/gcd(m,g)`.
   - `ord(c) = 1` (i.e. `u₁ = −u₂` and `v₂ = −v₁`): unavoidable for every gap — but taking
     `gcd(g,m) = 1` leaves **λ = 1 as the only bad candidate**, and the λ=1 layer is already
     solved (§R3.8).
   - `ord(c) = ε > 1`: choose `g` with `gcd(m,g) ∤ m/ε`. Such a `g` exists unless `m` is a prime
     power `ℓ^a` **and** `m = n` **and** `ε = ℓ`. (If `m < n`, the gap `g = m` gives
     `gcd(m,g) = m` and `ε ∤ 1`, done.)
⟹ **the ONLY residual obstruction in this case is `n = m = ℓ^a` with `ord(c) = ℓ`**, where every
gap leaves a candidate and the third (secular) clause decides.

**Verification.** The closed form was checked against criterion C1 over q ∈ {2,3,4,5,7},
n = 3…8, every live-token pair and every gap: **~50 000 rows, 0 disagreements.** Every row the
closed form calls "no candidate" is a row where C1's obstruction is empty or sits only at λ=1;
no row escaped. ⚠️ §90 — both outcomes are exercised, so this is not a constant answer: of the
rows where a candidate DOES exist, C1 calls some cyclic anyway (the secular clause failing) and
others non-cyclic; e.g. at q=7, n=6: 480 cyclic-with-candidate vs 120 non-cyclic-with-candidate.
A predicate that always said "no candidate" would have failed on those 120.

**Where this leaves T1.** For the two-live-token family the λ≠1 layer is closed except for the
named prime-power residue, and §R3.8 closed the λ=1 layer. The general family still needs the
λ≠1 layer for ≥3 live tokens — that is the next target, and the same three ingredients apply:
the gap/exponent freedom, `ΔÛ(λ) = (u_b−u_a)λ^s(1−λ)` (nonzero at every λ≠1 at once), and the
secular clause as the last resort.

## R4.2 · Artifact index for rounds 3–4 (every claim above names its script and its output)
| script | log | what it certifies |
|---|---|---|
| `round3_census.py` | `logs/k1695/round3_census.log` | §R3.1 census, 1 713 018 matrices, H1/H2, 4 known-answer tests reproducing R8/R4 |
| `round3_family.py` | `logs/k1695/round3_family.log` | §R3.2 criterion C1 (312 888 validation rows) + §R3.3 family census (811 517 multisets, 397/397) |
| `round3_frontier.c` | `logs/k1695/round3_frontier.log` | §R3.7 frontier closure, 523 080 000 matrices in 90.8 s |
| `round3_n3_theorem.py` | `logs/k1695/round3_n3.log` | §R3.6 the n≤3 theorem's constructive rule, 818 948 witnesses + 3 negative controls + RED-1 |
| `round3_lambda1.py` | `logs/k1695/round3_lambda1.log` | §R3.8 lemmas L1–L5 (swap lemma, dichotomy) |
| `round3_n4_stratumB.py` | `logs/k1695/round3_n4_stratumB.log` | §R3.11 n=4 stratum (b), 12 748 matrices, orbit-size control |
| `round3_slack.py` | `logs/k1695/round3_slack.log` | §R3.13 witness slack (min 2 fixed points, 2·(n−2)! permutations) |
| `round3_joint.py` | `logs/k1695/round3_joint.log` | §R3.14 separability of the two layers |
| `round4_k2.py` | `logs/k1695/round4_k2.log` | §R4.1 closed form for the two-live-token case |
| `engine/briefs/k1695_r3_adv/TASK.md` | `engine/out/codex/k1695_n3_adversarial.md` | §R3.10 cross-family adversarial pass (codex `gpt-5.6-sol`) |
| `engine/briefs/k1695_r3_novelty/BRIEF.md` | pending | novelty/citation check for C1 and the n≤3 theorem — **outstanding** |

**Standing red lines for this line, unchanged:** nothing here is banked as SOLVED; 16.95 in
general is exactly as open as at round 1; no outward publication of any kind without user
authorization through dialogue, and only for CLOSED results — the n≤3 theorem is a PARTIAL
result and therefore does not travel, certificate-first policy notwithstanding.

## R4.3 · NOVELTY/CITATION CHECK — result, and what I verified MYSELF
Engine harvest: `engine/harvest/k1695_r3_novelty.md` (371 lines, Gemini search arm — a
compliant search-only dispatch). **A search model's citation is a lead, not a source**
(VERIFY_CHECKLIST C.12), so every load-bearing item below was re-resolved here through
Crossref by this session before being written down.

### Citations I opened and confirmed (Crossref, this session)
| DOI | resolves to | verdict |
|---|---|---|
| `10.13001/1081-3810.1360` | **Ferrante & Wimmer, "Reachability matrices and cyclic matrices", Electron. J. Linear Algebra 20 (2010)** | ✓ exactly as claimed. This is the arbitrary-field PBH/cyclic-matrix citation; `k1695_litcheck.md` §Q2.1 had already flagged it independently in round 2 — two separate sweeps converged on it |
| `10.4153/CJM-1980-018-9` | **R. C. Thompson, "Invariant Factors Under Rank One Perturbations", Canad. J. Math. 32 (1980) 240–245** | ✓ exactly as claimed — the rank-one interlacing theorem. ⚠️ It is **related work, not a dependency**: C1 is derived from Lemma 0 (nullity of a rank-one update), not from interlacing, which entered this line's notes only as a heuristic aside |
| `10.1007/BF01396012` | **Bunch, Nielsen, Sorensen, "Rank-one modification of the SYMMETRIC eigenproblem", Numer. Math. 31 (1978) 31–48** | ✓ resolves — **but its title itself limits it**: real symmetric. It cannot be the arbitrary-field citation, which is precisely the gap. §R3.9's wording is corrected accordingly |

**One harvest claim corrected.** It reported "Baragaña–Roca 2017, ResearchGate only, WEAK".
Crossref gives the real records: **Baragaña & Roca, "Rank-one perturbations of matrix pencils",
LAA (2020), `10.1016/j.laa.2020.07.030`**, and **"Fixed rank perturbations of regular matrix
pencils", LAA (2020), `10.1016/j.laa.2019.12.022`** — better sourced than reported, and the
year and venue in the harvest were both wrong. Also surfaced and relevant to round 4's rank-2
stratum: **Dodig & Stošić, "Bounded rank perturbations of matrix pencils without nontrivial
invariant factor", Linear Multilinear Algebra (2023), `10.1080/03081087.2023.2277210`**.

### The absence, re-checked through my own channel with a live positive control
arXiv REST API, this session: `all:"Kourovka"` → **100 results** (channel demonstrably alive);
`all:"Kourovka" AND all:"16.95"` → **exactly 1 hit, `1606.02238v2`, Dixon's withdrawn paper.**
Independently reproduces the harvest's Q2 finding on that channel. (An empty population would
have been an ALARM, not a quiet day — checklist A.4.)

### Verdict, stated as weakly as the evidence permits
- **Q1 (criterion C1):** the machinery is classical and now properly citable — Ferrante–Wimmer
  for the arbitrary-field PBH/cyclic frame, R. C. Thompson 1980 for rank-one interlacing, the
  DPR1 tradition for the secular clause over ℝ. The **monomial/permutation specialisation and
  the third clause in gcd form over an arbitrary field were not found in print.** Per checklist
  C.11 that is a WEAK negative: **C1 is cited as assembled from known machinery and is NOT
  claimed as new.** §R3.9's posture, written before the check, stands unrevised.
- **Q2 (16.95 partial results):** no partial result, no small-case statement, no Lean/Isabelle
  trace of 16.95 since the 2017 withdrawal. The engine's differential positive control is the
  strongest part of the harvest — it detected 2026 solutions of *other* Kourovka problems and
  Aristotle's eight, and 16.95 was absent from that list, so the instrument demonstrably
  distinguishes. **Still a WEAK negative: "not found" ≠ "absent".**

### Degradations, kept separate from the negatives
The engine's four REST channels (zbMATH, Crossref, OpenAlex, arXiv) **all failed on DNS name
resolution** and it pivoted to manual web frontends. So its API-channel results are not
machine-verified; only its web-channel results are, and those carried positive controls. The
DOI verification and the arXiv absence check above were run by THIS session precisely because
of that. **MathSciNet remains walled** (unchanged since round 2) and **non-English literature
is unchecked** — both named, both real, neither closed.

**Operational consequence: none.** The n≤3 theorem is a partial result and does not travel
regardless of novelty; C1 is a tool and is claimed as one.

### R4.3b · Q1 re-checked on a SECOND axis: forward citations (an axis the round-2 litcheck never used)
`k1695_litcheck.md` and the K3-NOV harvest are both **keyword** sweeps. The citation graph is an
independent axis (VERIFY_CHECKLIST C.11 asks for both). Run here via OpenAlex (`tools/cite_lookup.py`
supplied the entry point; its three controls pass — 1980 paper 39 cites positive, days-old
preprint resolves with a true 0, nonsense DOI resolves nowhere):

| parent | citers | titles touching permutation / monomial / cyclic-matrix / nonderogatory |
|---|---|---|
| Ferrante–Wimmer 2010 (the arbitrary-field PBH/cyclic frame) | **6, all read individually** | **0** — Hankel-via-Krylov, companion-matrix bilinear characterisations (×2 dup records), reachability/observability pairs (×2 dup), and one CV record |
| R. C. Thompson 1980 (rank-one invariant-factor interlacing) | **39, all titles read** | **0** |

The entire citing literature of both parents is the generic/structured low-rank-perturbation
tradition for matrices and pencils. **Nobody specialises it to permutation or monomial
matrices, and 16.95 appears nowhere in it.** This is a materially stronger negative for Q1 than
keyword search alone, on an axis where a repo-merge-style invisible resolution would have shown
up. It remains a WEAK negative — cite, don't claim — but it is now weak on two axes, not one.

**Closest related work, resolved and worth reading before round 4's rank-2 stratum** (all
verified by DOI here, none of them stating our specialisation):
- Bru, Cantó, Urbano, **"Eigenstructure of rank one updated matrices"**, LAA (2015),
  `10.1016/j.laa.2015.07.036` — the nearest thing to Lemma 0; check its field hypotheses first.
- Baragaña, Dodig, Roca, Stošić, **"Bounded rank perturbations of regular pencils over
  arbitrary fields"**, LAA (2020), `10.1016/j.laa.2020.05.015` — arbitrary fields, bounded rank:
  exactly the setting of the n=4 stratum (a).
- Dodig, Stošić, **"Bounded Rank Perturbations of Quasi-Regular Pencils Over Arbitrary Fields"**,
  SIMAX (2023), `10.1137/22m1504068`.
⚠️ These are RESOLVED, not yet READ. Nothing may lean on them until opened (checklist C.12).

## R4.2 · The residual λ≠1 layer, restated — plus TWO of my own errors, both caught by anomalies
`problems/k1695/round4_reciprocal.py`.

**Reformulation (verified).** L4 collapsed the λ=1 layer to the residual case `v = ρu`. There,
with live tokens `u_i` at cyclic positions `s_i` and `F(x) = Σ_i u_i x^{s_i}`:
`Û(λ) = F(λ)` and `V̂(λ) = ρ·F(λ^{-1})`, so **λ is a bad candidate ⟺ both `λ` and `λ^{-1}` are
roots of `F`** — i.e. `gcd(F, F*)` has a root in `μ_m\{1}`, `F*` the reversal. The remaining
question is therefore purely combinatorial: *place the tokens so that the root set of `F` in
`μ_m` contains no inverse-closed pair* (in particular `F(−1) ≠ 0` when `−1 ∈ μ_m`, since `−1`
is its own inverse).
**V1: 91 822 rows** over q ∈ {2,3,4,5}, n = 3…8, k ≤ 4 — **0 rows had a λ≠1 obstruction that
the reformulation did not predict**; both sides occur (12 506 predicted-candidate / 79 316
predicted-none), so it is not vacuous. ⚠️ Those two figures are the post-fix ones: the
pre-fix run reported 16 334 / 75 488, and the difference is exactly the false positives
Error 2 was producing. Re-extracted from `logs/k1695/round4_reciprocal.log` at bank time. The test is deliberately ONE-SIDED: a predicted
candidate need not produce an obstruction, because the secular clause can still save it.

### ⚠️ ERROR 1 (mine): the worked case I first wrote down does not exist
I drafted the three-live-token case over GF(2) as the worked instance and derived a clean rule
for it. **There are no instances.** Over GF(2) the only nonzero value is 1, so `u = v = 1_S`
and `c₀ = |S| mod 2`; `A = I + uvᵀ` is invertible iff `1 + c₀ ≠ 0`, i.e. **iff `|S|` is even**.
`|S| = 3` is always singular, so 16.95 says nothing about it and my "theorem" quantified over
an empty set. Caught only because the verification loop printed `0 values` — an assertion
inside it would have "passed" without ever executing. This is checklist A.3 exactly: *every
delivered theorem must include one worked instance satisfying its own hypotheses.* The census
had been telling me this all along and I did not read it: §R3.3/§R3.13's hard sizes were
`|S| = 2, 6, 10` — **all even**.

### ⚠️ ERROR 2 (mine): a false positive that the one-sided test could not see
`pair_candidate` reported "a bad candidate exists" for **every** position set whenever
`n` is a power of the characteristic. Wrong: there `m = 1`, so `μ_m = {1}` and there is no
`λ ≠ 1` to be a candidate at all. The code fell through to its "F ≡ 0 mod x^m−1" branch.
V1 could not catch it because V1 only tests one direction. Caught by an anomaly instead —
n = 8 and n = 16 reported **0 clean position sets out of 35 and 455**, which is not a shape a
true statement takes. Fixed in the script, with the reason recorded at the fix site.

### The real worked case, and where the difficulty actually sits
Smallest existing case over GF(2) is `|S| = 4`. **Consecutive positions `{0,1,2,3}` are clean
for every n = 5…29** — 25 values, each cross-checked against C1 (no λ≠1 obstruction), and the
script now asserts the loop body actually executed, so the Error-1 shape cannot recur silently. The reason is structural,
not numerical: consecutive positions give `F = (x^4−1)/(x−1) = (x+1)³` over GF(2), whose only
root is 1 — and a set whose `F` has no root ≠ 1 is trivially free of inverse-closed pairs.
That argument works whenever `k` is a power of the characteristic.
**It fails at the census's own hard size.** For `|S| = 6`, `F = (x^6−1)/(x−1)` has roots of
order 3, and consecutive positions carry a bad candidate at every n tested (9, 12, 15, 18, 21).
⟹ **the open problem is now sharp**: for `k` not a power of `p`, find a position set whose `F`
has no inverse-closed root pair in `μ_m`. That is the whole of what remains for this stratum.

## R4.4 · K4-REC — PRE-REGISTERED grading criteria (written before the harvest exists)
Dispatched to codex `gpt-5.6-sol high` via dialogue: `engine/briefs/k1695_r4_reciprocal/BRIEF.md`
→ `engine/harvest/k1695_r4_reciprocal_codex.md`, terminator `DONE-K4REC`. Written down now, per
VERIFY_CHECKLIST D.15, so the answer is graded against this and not against how it reads.

**VOID conditions — any one of these and the submission is discarded, not partially credited:**
1. The `k = 6`, `p = 2` consecutive control at `n = 9,12,15,18,21` is reported CLEAN. Those are
   dirty; a checker that calls them clean is broken and every other number it prints is void.
2. Printed witnesses are not re-verified by its own checker in the same run.
3. No per-cell population figure, so a silently truncated search is indistinguishable from an
   exhaustive one (§R3.3's own `UNRESOLVED` discipline applies to them too).
4. Floating point anywhere in the root computation.

**Downgrades (not void, but the claim is weakened to what survives):**
- A cell reported `NONE` without an explicit exhaustive-search declaration banks as
  **UNRESOLVED**, never as "no clean set exists".
- A construction validated only on the cells it was read off from banks as a **pattern**, not a
  construction. To count as a construction it must be checked on cells OUTSIDE the fitting
  range, and I will pick those cells myself.

**What each outcome buys, decided in advance:**
| outcome | what it settles |
|---|---|
| verified witness table only | evidence; the λ≠1 layer stays open |
| table + construction + a proof I can check | closes the λ≠1 layer for the proportional case, i.e. **completes T1's remaining piece for `v = ρu`** — but the proof must be re-derived by me before it enters the registry as anything but a citation |
| an infinite family with NO clean set | more valuable than a construction: it says the secular clause is *load-bearing*, and points at where a counterexample to T1 (hence to 16.95) would have to live |

**Grading doctrine, unchanged:** measured engine profile is checklist-completeness ~10/10,
derivation validity ~2/15. I grade what it BUILT — tables, witnesses, the script — never what
it JUDGED. Any proof it supplies is a lead to re-derive, not a result to adopt. A clean pass
banks as "one channel found no obstruction", never as "verified".

## R4.5 · ⭐ K4-REC GRADED — the λ≠1 layer CLOSES over GF(2); T1's residual case is finished there
Harvest `engine/harvest/k1695_r4_reciprocal_codex.md` (143 KB, codex `gpt-5.6-sol high`, 37m53s),
graded strictly against §R4.4's pre-registration. **Nothing below is taken on the engine's word:
I ran its script myself, re-verified every witness with MY checker, re-derived its proof, and
tested its construction out of sample on cells I chose.**

### Void checks (§R4.4) — all pass
| condition | outcome |
|---|---|
| `k=6`, p=2 consecutive at n=9,12,15,18,21 must be DIRTY | its script prints `clean=FALSE` on all five ✓ (and `clean=TRUE` on the k=4 controls) |
| witnesses re-verified in-run | yes, and re-verified again here by independent code |
| per-cell population | present: columns `tested / canonical-population / exhaustive` on every row |
| no floating point | none found in the script |
| field construction | its own GF(4)/GF(8)/GF(9) axioms self-checked |

### The grading that actually decides it — MY checker, not theirs
- **935 claimed clean witnesses, ALL confirmed by `round4_reciprocal.py`'s independent
  `pair_candidate`, 0 rejected.** 26 `NONE` cells, none contradicted.
- **11 claimed "rescues" (unequal coefficients making a cell clean that is dirty with all
  ones): 11/11 confirmed**, each checked both ways (all-ones dirty AND general clean).

### The construction, re-derived and tested OUT OF SAMPLE on cells I picked
**Odd n.** With `d = n−1`, `S₀ = {d, d/2} ∪ ⋃_{r=1}^{(k−2)/2}{r, d−r}`. Re-derived here: `S₀` is
symmetric under `s ↦ d−s` except that `d ∈ S₀` while `0 ∉ S₀`, so in characteristic 2
`F_{S₀}(x) + x^d F_{S₀}(x^{-1}) = 1 + x^d`. A common reciprocal root would kill the left side,
forcing `λ^d = 1`; with `λ^n = 1` and `gcd(n, n−1) = 1` that gives `λ = 1`, excluded. ∎ Correct.
**Even n = m·2^e, m > 1.** Choose the placement so residues 0 and 1 mod m carry an ODD number of
positions and every other residue an even number; then on `μ_m` the pairs cancel and
`F_S(λ) = 1 + λ`, which vanishes only at `λ = 1`. Capacity `2 + 2(h−2) + (m−2)h = n−2` ✓ (I
recomputed it). ∎ Correct.
**Obstruction.** `k = n` forces `S = Z_n`; every residue mod m then occurs `h = 2^e` times, even,
so `F_S ≡ 0` on all of `μ_m` and the set is dirty whenever `m > 1`. ∎ Correct.

⭐ **Out-of-sample test, the condition §R4.4 made binding:** I re-implemented the construction
from the PROOF TEXT (not from their code) and ran it on **n = 65…150 — entirely outside their
n ≤ 64 table — over 4 473 (n,k) cells: every one CLEAN by my checker, 0 dirty, 0 malformed.**
The claimed obstruction was checked on the same out-of-sample range: dirty in all 42 cases,
0 unexpectedly clean. This is the pre-registered top outcome, "table + construction + a proof
I can check", and it is the first time this line has taken a *proof* from the free layer.

### What this settles, stated no more widely than it holds
**Over GF(2) the λ≠1 layer of T1's residual case is CLOSED.** Over GF(2) the only nonzero scalar
is 1, so `v = ρu` forces `u = v = 1_S`: the proportional residual case IS the all-ones case, and
a clean placement exists for every even `k` with `4 ≤ k ≤ n` except `k = n` with `n` even and not
a power of 2. Combined with §R3.8 (λ=1 layer) this finishes **T1's remaining piece over GF(2)**.
⚠️ **It does NOT settle T1.** Still open: (i) all other fields — the general-coefficient table
covers only q ∈ {3,4}, n ≤ 24, k ≤ 6. ⚠️ **Correction to this entry, made while writing the
follow-up brief:** I first wrote that several of those rows bank as UNRESOLVED. That was
over-cautious to the point of being wrong. 209 of 212 rows are non-exhaustive, but every one of
them STOPS EARLY HAVING FOUND A WITNESS (`tested/pop` = 1/4, 2/6, …), and a witness is a witness
— non-exhaustiveness only invalidates a NEGATIVE claim. **There is no `NO` row anywhere in the
general-coefficient table**: with unequal coefficients allowed, a clean placement was found in
every cell tested. So nothing there is UNRESOLVED; the real gap is coverage plus the total
absence of a general-q construction or proof; (ii) the non-proportional case, which
§R3.8 L4 handles at λ=1 but not at λ≠1; (iii) the excluded `k = n` cells, where the secular
clause must decide — that is exactly the `aI+bJ` family, already proved by R7, so the two
results meet there rather than conflict.
⭐ **A finding worth keeping in its own right:** unequal coefficients rescue cells that all-ones
cannot (verified 11/11), including full-support `k = n` at q=3. So the `k = n` obstruction is a
**GF(2) artefact of having no coefficients to vary** — which is precisely why round 2's `aI+bJ`
(constant `u,v`) was the hard family, and why §R3.8's non-proportionality dichotomy is the right
lever. Three independently-derived results agreeing on the same structural point.

## R4.6 · K5-GFQ — PRE-REGISTERED grading criteria (written before the harvest exists)
Running on ChatGPT GPT-5.6 Sol + Pro effort (math tier, model verified on screen by dialogue);
brief `engine/briefs/k1695_r5_gfq/BRIEF.md` → harvest `engine/harvest/k1695_r5_gfq_pro.md`.
Written now, per VERIFY_CHECKLIST D.15. Sharpened by three things learned grading K4-REC.

**My grading instrument is already general-q.** `round4_reciprocal.py`'s `pair_candidate`
takes an arbitrary coefficient map over an arbitrary `GF(q)`. It exists BEFORE the answer does,
so grading cannot be shaped by what arrives — I will not write a new checker after reading the
harvest.

**VOID — any one and the submission is discarded, not partially credited:**
V-a `q=2, k=6` consecutive reported CLEAN at any of n = 9,12,15,18,21 (they are dirty).
V-b `q=2, k=4` consecutive reported DIRTY at any n = 5…29.
V-c any of the five coefficient-rescue examples reported dirty, or its all-ones counterpart on
    the same positions reported clean. This is the sharpest control: it is the fact any correct
    general-`q` construction most needs to respect.
V-d field arithmetic not self-checked, or `GF(4)/GF(8)/GF(9)` not built in-submission.
V-e floating point anywhere in a root computation.

**The distinction I got wrong myself in §R4.5, now binding:** a NON-EXHAUSTIVE cell that
reports a WITNESS is a valid positive — a witness is a witness. Only a cell claiming NO clean
placement needs exhaustiveness; without it that cell banks as **UNRESOLVED**.

**Out-of-sample test, with the cells fixed in advance so the choice cannot be made to flatter
the answer:** their table stops at `n ≤ 30`. I will re-implement their construction **from the
proof text, not from their code** (as with K4-REC) and run it through my checker on
`n = 31…80` for `q ∈ {3,4,5,7,8,9}`, over the same three coefficient families the brief names.
A construction that fails there is a pattern, not a construction, regardless of its table.

**⚠️ The specific failure mode I am watching for, named in advance.** The brief warns that both
halves of the `q=2` proof run on characteristic-2 pairwise cancellation. The likely partial
answer ports that parity argument and silently assumes `2 = 0`. I will test for it directly:
run their construction at `p = 2` and at `p` odd and check whether the odd-`p` branch is doing
real work or is the even branch in disguise.

**⚠️ The half I must not be impressed by.** The problem splits into (1) which residue-sum
profiles `(T_0,…,T_{m−1})` are clean, and (2) which profiles are REALISABLE from the GIVEN
coefficient multiset. Half (1) is a short exercise about polynomials and their reversals; half
(2) is the genuinely hard, subset-sum-flavoured half, and it is trivial exactly when all
coefficients are equal — which is why `q = 2` fell. **A submission answering only half (1)
banks as INCOMPLETE even if half (1) is flawless and beautifully written.** Deciding this now
is the whole point of pre-registering.

**What each outcome buys:**
| outcome | what it settles |
|---|---|
| table + witnesses only | evidence; T1 stays open off `GF(2)` |
| half (1) only | INCOMPLETE — the easy half |
| construction covering both halves, proof I can re-derive, surviving n = 31…80 | closes the λ≠1 layer of T1's proportional case **over all tested `q`** — the first result of this line to hold off `GF(2)` |
| an explicit `(q,n,k,multiset)` with NO clean placement for `p > 2` | more valuable than a construction: it says the secular clause is load-bearing off `GF(2)` and localises where a T1 counterexample must live |

**Doctrine unchanged:** I grade what it BUILT — tables, witnesses, scripts — never what it
JUDGED. Any proof is a lead to re-derive before it enters the registry as more than a citation.
A clean pass banks as "one channel found no obstruction", never as "verified".

## R4.7 · K5-GFQ — PARTIAL grade (mathematics only; the artifacts are not yet downloadable)
Harvest `engine/harvest/k1695_r5_gfq_pro.md` (GPT-5.6 Pro, 43 min). Its script/CSVs are ChatGPT
attachments awaiting the owner's per-file OK, so **the V-a…V-e controls CANNOT be re-run yet and
nothing that depends on them is graded.** Two of its claims are checkable by hand with the
grading instrument that already existed (§R4.6), and both were checked here.

### ⭐ CLAIM 2 — CONFIRMED, and the defect is MINE
It reports that the `k = 2` criterion **as stated in my brief** is wrong, with the witness
`GF(3), n = 5, coefficients (1,2) at positions (0,1)`: there `P(x) = 1 + 2x = 1 − x`, whose only
root is `x = 1`. My checker agrees: **CLEAN**. The brief's restatement —
*"a bad λ exists iff `u₁² = u₂²` and `ord(−u₁/u₂) | m/gcd(m,g)`"* — omits the exclusion of
`λ = 1`, so it calls this dirty. With `c = −u₁/u₂ = 1` and `ord(c) = 1`, the criterion fires on
a bad set whose only member is `λ = 1`, which the definition of *clean* excludes.
⚠️ **Provenance of the error, stated exactly: §R4.1's registry text was RIGHT** — it says
"`ord(c) = 1`: unavoidable for every gap — but taking `gcd(g,m) = 1` leaves **λ = 1 as the only
bad candidate**". **I introduced the defect when compressing R4.1 into the brief**, by dropping
that clause. So this is a briefing error of mine that an engine caught, not an error in the
banked mathematics — and it is a reminder that a compressed restatement is a new claim needing
its own check, not a citation.

### ⭐ CLAIM 3 — CONFIRMED, and it is the outcome §R4.6 priced HIGHEST
It exhibits a `p > 2` obstruction: `n = m = 4`, `k = 4`, multiset `{a,a,b,b}` is dirty for
**every** placement. Verified here independently, all 6 distinct arrangements, over four fields:
| field | multiset | arrangements dirty |
|---|---|---|
| GF(3) | {1,1,2,2} | 6/6 |
| GF(5) | {1,1,2,2} | 6/6 |
| GF(5) | {1,1,4,4} | 6/6 |
| GF(7) | {2,2,5,5} | 6/6 |
| GF(9) | {1,1,2,2} | 6/6 |
**This is convergence with this line's own round-3 analysis**, which had already derived by hand
that "`u = (a,a,b,b)`, `n = 4`, char ≠ 2: no arrangement makes `U` root-free on `μ₄\{1}`". Two
independent derivations, months of reasoning apart, landing on the same family.

⭐ **It also exposes an equivocation in my own brief.** The brief asserted "no cell is known to
be unrescuable for `p > 2`" — a statement about **cells** `(q,n,k)`, where the multiset may be
chosen. The new obstruction is about a **fixed multiset**. Both are true and they are not the
same statement: cell `(q=3,n=4,k=4)` does have a clean placement with multiset `[1,1,1,2]`
(one of the 11 rescues verified in §R4.5), but `{1,1,2,2}` has none.
**For 16.95 the multiset-level statement is the one that matters** — in T1 the coefficients ARE
the given vector `u`; nothing lets us choose them. So the obstruction is real for this line's
purposes and the "rescues" framing was misleading. Naming the level of quantification is now a
standing requirement for any cell/multiset claim in this campaign.

**What Claim 3 settles.** §R4.6 priced "an explicit `(q,n,k,multiset)` with no clean placement
for `p > 2`" ABOVE a construction, because it says the secular clause is load-bearing off
`GF(2)`. That is now established: **the λ≠1 layer of T1 cannot be closed by placement alone
once `p > 2`** — the third clause, or the `(n−1,1)` fallback, is doing real work there. Which is
exactly what §R3.13/§R3.14 predicted from the census, and is consistent rather than in tension
with it.

**Still ungraded, pending the files:** the general-`q` construction and its realisability half,
the 5 866-cell table, the 177 `NONE` cells, and every one of V-a…V-e. Per §R4.6 the construction
also owes the out-of-sample test at `n = 31…80`, which I will run from the PROOF TEXT once the
submission is in hand. **No part of the construction is banked.**

## R4.8 · K5-GFQ — FULL GRADE: controls pass, out-of-sample passes, but it answers a DIFFERENT question
Artifacts `engine/harvest/k1695_r5_gfq/{k5_gfq.py, K5-GFQ_submission.md}`. Graded against §R4.6.

**Provenance and hygiene.** `shasum -a 256` of the script reproduces the stated
`d04f15c0…3592` **byte-exact**; 701 lines; no floating point anywhere in the root computation.

**Controls, re-run by me under an external 900 s cap** (their realisability enumeration is
exponential worst case, so I capped rather than trusted): the run finished in **2.3 s**, cap
untouched. **V-a** k=6 consecutive DIRTY at n = 9,12,15,18,21 ✓. **V-b** k=4 consecutive CLEAN
for n = 5…29 ✓. **V-c** all five rescues CLEAN with their all-ones counterparts DIRTY, printed
side by side ✓. **V-d** GF(2,3,4,5,7,8,9) built in-submission, axioms self-checked ✓.
**V-e** per-cell `population_searched` / `exhaustive` columns present on all 5 866 rows; all 177
`NONE` cells flagged exhaustive ✓. **No void condition fired.**

⭐ **Out-of-sample, on the cells §R4.6 fixed BEFORE the answer existed.** Their table stops at
`n ≤ 30`; I re-ran their procedure to `n = 80` (28.3 s) and verified the result with MY checker,
which predates the submission: **33 900 rows at n = 31…80 → 33 589 witnesses, ALL confirmed
clean by `pair_candidate`, 0 rejected; 311 `NONE` cells, 0 contradicted.**

### Half (1) — CORRECT, and it converges with what this line already had
Their profile criterion: `T` clean ⟺ `gcd(P_T, P_T^∨, C_m) = 1`, where `P_T^∨(λ) = P_T(λ^{-1})`
on `μ_m` and `C_m = (x^m−1)/(x−1)`. **This is the same test `round4_reciprocal.py` already
computes** — independent arrival at the same criterion. What they add is genuine: since `p ∤ m`
makes `x^m−1` squarefree, factoring `C_m` into monic irreducibles gives the clean characterisation
*"no self-reciprocal factor divides `P_T`, and no reciprocal pair `{f, f^#}` both divide it"*.
That is a real sharpening of the half I handed them.

### Half (2) — ⚠️ NOT the deliverable that was asked for
The brief asked for a **construction with proof**. What arrived is an **exact decision
procedure**: bounded multiway subset-sum enumeration over residue classes with capacity `h`,
placement `s = r + j·m`, exponential in the worst case by their own statement. It is correct as
far as I can check it, but **it is a search, not a closed-form rule**, and that distinction is
the whole point of §R4.6's pricing.
⟹ **This does NOT buy the outcome §R4.6 priced as "closes the λ≠1 layer over all tested q".**
A procedure verified to `n ≤ 80` is evidence, not a theorem for all `n`. The GF(2) case
(§R4.5) remains the only place where the λ≠1 layer is genuinely CLOSED, because there we have a
closed-form placement plus a proof I re-derived. Off `GF(2)` the layer is now **decidable per
instance and empirically always solvable outside a characterised family — but not proved**.

### The `NONE` family, which is the mathematically interesting output
All 177 in-table (and 311 out-of-sample) `NONE` cells lie in the **all-ones** family: `k = n`
with `m > 1`, plus, in odd characteristic, `n ∈ {4,8,16}` with `k ∈ {2, n−2}`. Combined with
§R4.7's confirmed `{a,a,b,b}` obstruction this says the same thing from two directions:
**off `GF(2)`, placement alone cannot always win, so the secular clause and the `(n−1,1)`
fallback are load-bearing** — exactly what §R3.13/§R3.14 predicted from the census.

**VERDICT: strong partial.** All controls pass, both corrections (§R4.7) confirmed, half (1)
correct and sharpened, half (2) answered algorithmically rather than constructively. Banked as
**evidence plus a decision procedure**, NOT as a closure of the λ≠1 layer off `GF(2)`. Per
doctrine this counts as "one channel found no obstruction", never as "verified".

---

# ROUND 6 (v5, 2026-08-29, post quota-reset resume) — n = 4 via the transposition lemma
Interpreter `.venv/bin/python3`; exact table arithmetic; no floating point. Everything PROVISIONAL.
Resume context: `lines/RESUME_NOTE_0829.md` (pacing lifted; codex quota expires 08-30 so codex
is the engine of choice today; screen `codex3` reserved for this line by dialogue `automath-b6`).

## R6.1 · LEMMA T (transposition lemma) — derived at resume, before any dispatch
For A ∈ M_n(F), τ = (a b), d = e_a − e_b: `P_τ = I − ddᵀ = P_τ⁻¹`, hence
`rank(AP_τ − μI) = rank(A − μP_τ) = rank((A − μI) + μ ddᵀ)` — a RANK-ONE update of E = A − μI.
With g = dim ker E: (T0) g = 0 ⟹ not derogatory at μ (a transposition is derogatory only at an
eigenvalue of A ITSELF); (T1) g = 1 ⟹ derogatory iff ℓ_a = ℓ_b ∧ r_a = r_b ∧ 1 + dᵀz = 0 (Ez = μd);
(T2) g = 2 ⟹ derogatory iff d ∈ col(E) or d ∈ row(E); (T3) g ≥ 3 ⟹ always derogatory.
(T4, rationality) for μ ∉ F with minimal polynomial m: `col(A − μI) ∩ Fⁿ = col_F(m(A))` (Galois
descent; inseparable case to be settled separately).
**Consequence claimed for n = 4 stratum (b)** (minpoly(A) = m irreducible quadratic, §R3.11):
m(A) = 0 ⟹ col(A − μI) ∩ F⁴ = 0 ∌ d, so by (T0)+(T2)+(T4) EVERY transposition makes AP_τ cyclic.
This is a PROOF SKETCH, not banked: §R3.11 only probed 4-cycles, so the prediction "all six
transpositions work on all 112 (q=2) + 12 636 (q=3) stratum-(b) matrices" is a fresh falsifiable
test — run in `round6_transp.py` (below) and independently by codex (K6-N4).

## R6.2 · K6-N4 — PRE-REGISTERED grading (written before the harvest exists; VERIFY_CHECKLIST D.15)
Ticket `engine/briefs/k1695_r6_n4/TICKET.md` → harvest `engine/harvest/k1695_r6_n4/REPORT.md`,
terminator `DONE-K6N4`, codex `gpt-5.6-sol high` on screen `codex3` (--approve-for-me).
Asks: §1 prove + machine-check Lemma T (with a negative control that must FAIL when the T1 scalar
clause is deleted); §2 attack + machine-check the stratum-(b) argument (inseparable case named as
the weak point); §3 PROVE stratum (a) at n = 4 over every field (rank 2 — untouched so far — and
rank 1) with a machine-checked decision rule.
**VOID (discard entirely):** (V-a) any Lemma-T check cell without the per-clause firing counts, or
with the negative control reported as still agreeing; (V-b) stratum-(b) enumeration whose count
≠ |GL(4,q)|/|GL(2,q²)| (112 at q=2, 12 636 at q=3); (V-c) a §3c rule check with no "always P = I"
negative control or with that control not failing on every input; (V-d) floating point.
**Downgrades:** a §3 "proof" whose decision rule is only checked on q ∈ {2,3} banks as a PATTERN
until I re-run it on q ∈ {4,5,7} myself; any case closed by "clearly"/"easy to see" is OPEN.
**What each outcome buys:** Lemma T + (b) confirmed ⟹ R6.1 promoted from sketch to THEOREM
(stratum (b) closed over every field) after my own re-derivation; §3 proofs surviving my re-run ⟹
**16.95 closed for n ≤ 4 over every field** (milestone; then cross-family pass + Lean candidate);
a §3 counterexample ⟹ re-verified three ways here before anything is said to anyone.
Doctrine unchanged: grade what it BUILT; proofs are leads to re-derive; a clean pass = "one channel
found no obstruction".

## R6.3 · ⭐ THEOREM (provisional, machine-checked prediction): n = 4, stratum (b) is CLOSED over every field — every transposition is a witness
`problems/k1695/round6_transp.py`, `logs/k1695/round6_transp.log` (27.5 s).

**Lemma T (proof).** `P_τ = I − ddᵀ` (check on e_a, e_b, others), so `AP_τ − μI = (A − μP_τ⁻¹)P_τ` and
`P_τ⁻¹ = P_τ`, whence `rank(AP_τ − μI) = rank(E + μddᵀ)`, `E = A − μI`. Rank-one-update facts:
`rank(E + xyᵀ) = rank E + 1` iff `x ∉ col E ∧ y ∉ row E`; `= rank E − 1` iff `x ∈ col E`, `y ∈ row E`
and `1 + yᵀz = 0` for any z with `Ez = x` (well defined since y ⊥ ker E). With x = μd, y = d
(μ ≠ 0 for invertible A): T0/T1/T2/T3 as stated in §R6.1. ∎
**T4 (rationality, NO separability needed).** μ ∉ F, m = minpoly of μ over F, K = F(μ), k = deg m.
`m(A) = (A − μ)h(A)` gives `col_F(m(A)) ⊆ col_K(A − μ) ∩ Fⁿ`. Conversely if `w = (A − μ)z`, w ∈ Fⁿ,
z ∈ Kⁿ, write `z = Σ_{t<k} μᵗ z_t` (z_t ∈ Fⁿ) and reduce `μᵏ` by m: comparing coefficients in the
F-basis 1,μ,…,μ^{k−1} gives `z_{t−1} = A z_t + m_t z_{k−1}` (t = 1..k−1) and `w = A z_0 + m_0 z_{k−1}`,
so `w = m(A) z_{k−1} ∈ col_F(m(A))`. Solvability of a K-linear system does not change under F̄ ⊇ K,
so the same holds with col over F̄. Rows: transpose. ∎
**Stratum (b).** A ∈ GL(4,F), invariant factors (m, m), m irreducible quadratic. If AP_τ is
derogatory at μ then μ ∈ spec A by T0 — which holds for EVERY μ, including μ = 0, since it is only
the rank-one-update bound rank(E + μddᵀ) ≥ rank E − 1 (Lean `l4_t0` carries no μ ≠ 0 hypothesis);
so m(μ) = 0, and then μ ≠ 0 because m is irreducible and m ≠ X (A invertible) — this is where T2's
hypothesis μ ≠ 0 is discharged (ordering made explicit after the K6-QREV review, §R6.32). Invariant factors are stable under field
extension, so over K the number of invariant factors divisible by (x − μ) is 2: g = nullity(A − μ) = 2
(this covers the inseparable case μ = μ̄ with no case split). By T2, `d ∈ col(A − μ)` or
`d ∈ row(A − μ)`; by T4 both intersect F⁴ in `col_F(m(A)) = 0`, but d ≠ 0. Contradiction. ∎
**General n (written out after K6-QREV asked for it):** let A ∈ GL(n,F), n = 2k, with invariant
factors (m, m), m irreducible of degree k. If AP_τ is derogatory at μ ∈ F̄ then μ ∈ spec A (T0, any μ),
so m(μ) = 0, μ ∉ F (k ≥ 2; for k = 1 the invariant factors (m,m) with m = X − λ mean A = λI, and then
A P_τ = λ P_τ is cyclic iff n = 2 — the degree-one case is the n = 2 scalar case, handled directly),
and μ ≠ 0. Over F̄ the invariant factors are still (m, m), so nullity(A − μ) = #{invariant factors
divisible by X − μ} = 2. T2 (μ ≠ 0, g = 2): d ∈ col(A − μ) or d ∈ row(A − μ). T4 (any degree, no
separability): col(A − μ) ∩ Fⁿ = col_F(m(A)) = 0 as m(A) = 0; rows likewise; d ≠ 0 rational —
contradiction. So every transposition works, for every even n and every irreducible m of degree n/2. (And T4 makes EVERY Lemma-T clause an F-rational condition — for a
non-rational μ with g = 2 the transposition (ab) fails iff `e_a − e_b ∈ col_F(m_μ(A)) ∪ row_F(m_μ(A))`.)

**Machine check (fresh, both directions exercised).** Lemma T evaluated from A's eigenstructure vs the
actual rank, all A ∈ GL(n,q), all transpositions, all μ ∈ GF(q²):
| cell | |GL| (formula ok) | (A,τ,μ) triples | disagreements | neg. control (T1 scalar clause deleted) | clause fired T0/T1/T2/T3 | derogatory by clause | derogatory at non-rational μ |
|---|---|---|---|---|---|---|---|
| n=3 q=2 /GF(4) | 168 | 2 016 | **0** | 6 | 1320/630/63/3 | 0/48/15/3 | 0 |
| n=3 q=3 /GF(9) | 11 232 | 303 264 | **0** | 1 752 | 248346/53586/1326/6 | 0/1128/198/6 | 0 |
| n=4 q=2 /GF(4) | 20 160 | 483 840 | **0** | 7 248 | 322560/143760/16884/636 | 0/11328/5556/636 | 1 344 |
Oracle controls (identity derogatory, companion of xⁿ−1 never, minpoly-oracle vs rank-oracle on all
permutation matrices) pass. ⚠️ §90: every clause fired and each of T1/T2/T3 produced derogatory
verdicts; the negative control shows the scalar clause of T1 is load-bearing in every cell.
**Stratum-(b) prediction:** q=2: 112 matrices (class size ok) × 6 transpositions = **672/672 cyclic**;
q=3: 12 636 × 6 = **75 816/75 816 cyclic**; P = I non-cyclic on every representative (control).
§R3.11 had only recorded that some 4-cycle works — the transposition statement is new and sharper.
Status: THEOREM pending the codex cross-family pass (K6-N4 §1–§2); not banked as SOLVED-anything —
it closes one of the two n = 4 strata. Stratum (a) (rank ≤ 2 over a scalar) remains open at n = 4.

## R6.4 · ⭐ A STRONGER, INDUCTION-SHAPED CONJECTURE: the controllable-row-block certificate
`problems/k1695/round6_controllable.py`, `logs/k1695/round6_controllable.log` (32.8 s).
**Derivation.** `rank(AP_σ − μI) ≥ n−1 ∀μ` ⟸ some (n−1)-row submatrix of `AP_σ − μI` has full row
rank ∀μ. Deleting row i that submatrix is `[C P_τ − μ I_{n−1} | b]` with `C = A[≠i,≠j]`, `b = A[≠i,j]`,
`j = σ(i)` — i.e. the pair `(C P_τ, b)` is CONTROLLABLE (PBH) ⟺ b is a cyclic vector of `C P_τ`.
Equivalently (dual/left-eigenvector form): **e_i is a cyclic vector of AP_σ** (no left eigenvector of
AP_σ vanishes at coordinate i). Hence two statements, each implying 16.95(n):
- **(S)** for every A ∈ GL(n,F) there are σ and i with **e_i a cyclic vector of AP_σ** (the cyclic vector
  can be taken to be a STANDARD BASIS VECTOR).
- **(T_m)** for every m×(m+1) matrix R of rank m there are a column b and an ordering τ of the other
  columns with b a cyclic vector of `R[:,≠b] P_τ`; i.e. ∃ partial permutation E (one 1 per row,
  distinct columns) with `R − λE` of full row rank for every λ. (T_{n−1}) ⟹ (S) ⟹ 16.95(n).
**Data (all cells exhaustive up to column order; rank-m column multisets):** (T_2) over GF(2,3,4,5):
0 failures; (T_3) over GF(2), GF(3), GF(4) [687 960 multisets]: 0 failures; (T_4) over GF(2): 0 failures
(counts in the log). **(S)** on ALL of GL(3,2), GL(3,3), GL(4,2), GL(3,4), GL(3,5) [1 488 000]: 0 failures.
**Deflation identity (derived, not yet used).** Pivoting on an entry (i,j) of R with column operations
(column j eliminates row i), then deleting row i and column j, sends the pencil `R − λE` to an
(m−1)×m pencil `R̃ − λE'` of the same rank profile, where `E' = Ẽ − (b̂/b_i)e_{φ(i)}ᵀ` is the partial
permutation Ẽ with its zero column refilled by the pivot column. So (T_m) recurses into pencils whose
E has an arbitrary kernel vector — the natural general object; the recursion is NOT self-similar, which
is exactly why (T_m) is not trivially true. Left-eigenvector form of failure: `Rᵀy = λ E_φᵀ y`, i.e.
`Rᵀy` is λ × (y spread by φ, with a 0 at the missed column) — each failing (y,λ) covers a coset of a
Young subgroup of the injections φ, so a (T_m)-counterexample needs those cosets to cover all (m+1)!
injections. Over GF(2) with λ = 1 this reads `wt(Rᵀy) = wt(y)`.
Next probes (dispatched to the spark quota, K6-S): (S) on GL(5,2), GL(4,3), GL(4,4); (T_4) over GF(3),
(T_5) over GF(2). A counterexample to (S) or (T) that is not a counterexample to 16.95 would show the
certificate is too strong; none found so far.

## R6.5 · NEGATIVE: the weighted form (W_m) that deflation lands in is FALSE for general weights
`problems/k1695/round6_weighted.py`, `logs/k1695/round6_weighted.log` (14.7 s).
(W_m)(R, v): ∃ ordering τ̂ of all m+1 columns with `(R[:,τ̂(1..m)], Σ_{l≤m} v_l c_{τ̂(l)} + c_{τ̂(m+1)})`
controllable; v = 0 is (T_m); the deflation of (T_m) at a pivot (i, j) produces (W_{m−1}) with
`v = b̂/b_i` (the pivot column's other entries). Result: **fails for v ≠ 0** — (W_2)/GF(2): 5 of 40
(R,v) pairs; (W_3)/GF(3): 6 678 of 581 256; (W_4)/GF(2): 2 408 of 110 208; v = 0 never fails. The
failing R are degenerate (repeated columns, e.g. columns e₁,e₁,e₂,e₃ with v = e_l: the input
`c_a + c_b` collapses onto a kernel direction). ⟹ a "for all v" induction is dead; an inductive proof
of (T_m) must choose the pivot to control v. One clean reduction survives: **if R has a column with a
single nonzero entry (row i, column j), then (T_m)(R) ⟸ (T_{m−1})(R[≠i, ≠j])** (b ∝ e_i makes the
deflation delete row i and column j with v = 0). So the hard core of (T_m) is matrices whose every
column has ≥ 2 nonzero entries.
Also derived: (T_m) ⟺ ∃ column permutation Q with `(RQ⁻¹ − λ[I_m | 0])` of full row rank ∀λ — the
fixed pencil structure `[I | 0]` is the analogue of `I` in 16.95's `rank(AQ − λI) ≥ n−1`; the
advantage of (T)/(S) over 16.95 is that controllability is ONE polynomial condition
(`det[u, Mu, …, M^{m−1}u] ≠ 0`) where cyclicity is not.

## R6.6 · K6-N4 GRADED against §R6.2 — Lemma T repaired and cross-family confirmed; stratum (b) THEOREM; stratum (a) stays OPEN
Harvest `engine/harvest/k1695_r6_n4/{REPORT.md, checks.c, section1-3.log, build.log}` (codex
`gpt-5.6-sol high`, 21m56s, channel = OpenAI, cross-family). sha256 prefixes: checks.c 363bb9eb…,
REPORT.md c1b9b709…. Void checks: V-a per-clause counts present, negative control positive in all
11 cells ✓; V-b stratum-(b) counts 112 / 12 636 with per-class assertions ✓; V-c "always P = I"
control fails on every input in every §3c row ✓; V-d `grep -E '\b(float|double)\b' checks.c` → 0,
built with -Wall -Wextra -Werror ✓. **No void condition fired.**

⭐ **DEFECT FOUND IN MY STATEMENT (real, adopted).** T2 as written in §R6.1 omits μ = 0: when μ = 0
the update `μ ddᵀ` vanishes and `AP_τ` is derogatory at 0 iff A is (witness: F = GF(2), n = 2,
A = 0, τ = (12): g = 2, d ∉ col E ∪ row E, yet rank(AP_τ) = 0 = n−2). Repair (REPLACES §R6.1's
clause): **T1/T2 hold for μ ≠ 0**; for invertible A every eigenvalue is nonzero, so nothing
downstream (§R6.3, stratum (b)) is touched. The engine's own T4 proof (primary decomposition in a
splitting field for separable m; explicit `x = x₀ + μx₁` computation for the inseparable quadratic)
is a second, independent route to §R6.3's coefficient-comparison proof — convergent reconstruction.

**Lemma T cross-check (its code, its fields).** 11 cells, 0 disagreements, every clause fired,
negative control positive everywhere. Cells beyond my reach: GL(3,4)/GF(16) 8.7M triples;
GL(3,5)/GF(25) **111.6M** triples; GL(4,3)/GF(3) **436.7M** triples (population 24 261 120 = formula).
On the three cells both of us ran, every count is IDENTICAL (2016 / 48 / 15 / 3 / neg 6;
303 264 / 1128 / 198 / 6 / neg 1752; 483 840 / 11 328 / 5 556 / 636 / neg 7 248) — independent code.
**Stratum (b).** Argument survives attacks (i) and (ii); its note that irreducibility forces μ ≠ 0 is
exactly why the T2 repair is harmless here. Counts identical to mine (672/672, 75 816/75 816) plus
sampled windows GF(4), GF(5): 600 000 + 600 000 transposition products, 0 non-cyclic.
⟹ **§R6.3 is promoted: THEOREM (provisional, cross-family pass clean), same status class as the
n ≤ 3 theorem §R3.6.** 16.95 at n = 4 now reduces to stratum (a): `A = I + UWᵀ`, rank(UWᵀ) ∈ {1,2}.
**Stratum (a).** UNRESOLVED by the engine (it proved only the μ = 1 graph-covering lemma — the same
one I derived in §R6.4's margin — and declined to dress the search rule as a proof; correct
behaviour). Evidence: exhaustive over all distinct A with rank(A − I) ≤ 2: GF(2) 2 696, GF(3)
479 871, 0 failures, independent Krylov oracle 0 mismatches; 100 000-presentation windows over
GF(4), GF(5), GF(7), 0 failures. First-success histogram (lex order of S₄): transpositions carry
90–99 %, 3-cycles next, double transpositions and 4-cycles rare but present (7 / 59 / 14 / 3 / 0
4-cycle firsts by field) — rank-1 members need ≤ 2 cycles, so those rows are where they sit.
Banked as: Lemma T (repaired) + stratum-(b) theorem = cross-family CLEAN; stratum (a) = CENSUS.

## R6.7 · K6-N4b — PRE-REGISTERED grading (written before the harvest exists)
Ticket `engine/briefs/k1695_r6_n4b/TICKET.md` → harvest `engine/harvest/k1695_r6_n4b/REPORT.md`,
terminator `DONE-K6N4B`. It carries MY case skeleton for stratum (a): rank 2 by the eigenstructure of
S = I₂ + WᵀU — (α) S scalar [closed here: transposition works iff d ∉ X∪Y∪X⊥∪Y⊥ and the graph lemma
G_S ∪ G_{S⊥} ⊆ triangle-or-matching makes a cover of K₄ impossible], (β) distinct eigenvalues, (γ)
Jordan, (δ) 1 ∈ spec S, (ε) spec S = {1,1} [closed here: only eigenvalue 1, g = 2, graph lemma]; rank 1
by proportionality and characteristic with resonance clauses as cyclic Fourier coefficients.
**VOID:** (V-a) any lemma used in the proof without a machine-check line (population, failures,
controls) — the whole §1 or §2 that leans on it is void; (V-b) the "always P = I" control absent or
not failing on every input; (V-c) floating point; (V-d) a case closed by "clearly"/"easy to see".
**Downgrades:** a rule checked only on q ∈ {2,3} banks as PATTERN until I re-run it on q ∈ {4,5,7};
any case reported UNRESOLVED keeps stratum (a) OPEN — partial credit is per closed case, and each
closed case must be re-derived by me before it enters the registry as more than a citation.
**What each outcome buys:** all cases closed and re-derived ⟹ **16.95 for n ≤ 4 over every field**
(milestone: cross-family pass on the whole n = 4 proof next, then a Lean candidate); a named
UNRESOLVED configuration ⟹ that is the next target, by hand; a counterexample ⟹ re-verified three
independent ways here before anything is said.
Doctrine unchanged: grade what it BUILT; a clean pass = "one channel found no obstruction".

## R6.8 · K6-S (spark) first cells + (S)-slack: the certificate is UNIFORM in the index — (S′) ⟺ (T_{n−1})
Harvest (in flight) `engine/harvest/k1695_r6_S/logs/cell1.log, cell2.log` (codex `gpt-5.3-codex-spark`,
C, exact GF tables). **(S) on ALL of GL(5,2): 9 999 360 matrices (= formula), 0 (S)-failures,
0 16.95-failures. (S) on ALL of GL(4,3): 24 261 120 (= formula), 0 / 0.** First-success histogram of
the index: **i = 0 succeeds for EVERY matrix** in both cells. Since P_ρ A P_ρ⁻¹ runs over GL(n,q) as A
does, "i = 0 always works" ⟺ **(S′): for every A ∈ GL(n,F) and EVERY index i there is σ with e_i a
cyclic vector of A P_σ** — and (S′)_n ⟺ (T_{n−1}) exactly (every full-row-rank (n−1)×n matrix is
A[≠i,:] for an invertible A). So (T_4) over GF(2) and (T_3) over GF(3) hold for ALL matrices (not just
up to column order), by an independent channel. First-success σ types on GL(5,2): id 5 160 960,
one transposition 3 618 224, 3+1+1 1 081 824, 4+1 78 736, 3+2 52 640, 5-cycle 6 976 — half of GL(5,2)
has e₀ cyclic for A itself; a single transposition repairs most of the rest.
**(S)-slack (`round6_slack_S.py`, `logs/k1695/round6_slack_S.log`).** Fewest (i,σ) witnesses:
GL(3,q), q ∈ {2,3,4}: min 6, attained exactly by the monomial 3-cycles (2 good σ × 3 indices);
GL(4,2): min 20 (e.g. rows (0001),(0010),(0111),(1011), 6 cyclic σ), the H2-violator class.
The certificate is never tight in the sense of a unique witness.
Grading note for K6-S (pre-registered §R6.4 margin): cells 3–5 (GL(4,4), (T_4)/GF(3), (T_5)/GF(2))
pending; a (S)-failure that is not a 16.95-failure would show the certificate is too strong — none
in 34.3M matrices so far.

## R6.9 · Tightest (T_m) instances (`round6_T_slack.py`, `logs/k1695/round6_T_slack.log`)
Witness count = #(j, τ) with column j a cyclic vector of R[:,≠j]P_τ. Minima: (T_2) 2 (e.g. columns
0, e₁, e₂ — a zero column leaves only 2 usable pivots); (T_3)/GF(2) 4, attained only by
[e₁, e₂, e₁+e₂, 1]-type matrices (3 of 147); (T_3)/GF(3) 6; (T_4)/GF(2) 12, attained by exactly the
4 matrices [e_l, e_l, e_l+e_a, e_l+e_b, e_l+e_c] (a repeated column with every other column containing
it). A usable pivot column j does NOT require its complement R[:,≠j] to be invertible (κ_j ≠ 0):
e.g. (T_4)/GF(2) has 16 816 (j,R) pairs usable with κ_j = 0 vs 15 496 with κ_j ≠ 0 — so the kernel
vector of R is not the deciding invariant, and a proof cannot restrict to invertible complements.

## R6.10 · NEGATIVE (two polynomial-method probes) — `round6_krylov_sum.py`, `round6_cn.py`, logs in `logs/k1695/`
D_i(σ) := det[e_i, Me_i, …, M^{n−1}e_i], M = AP_σ (the (S′) certificate is "some D_i(σ) ≠ 0").
(1) Neither Σ_σ D_i(σ) nor Σ_σ sgn(σ) D_i(σ) is a multiple of det A: at n = 3 the signed sum factors as
`(a₃+a₄+a₅ − a₆−a₇−a₈)·(sum of the three 2×2 minors of rows 2,3)` (neither factor is det A), and at
n = 4, 5 the ratios to det A take 12/12 and 5/5 distinct values on random integer A. Dead.
(2) Combinatorial Nullstellensatz on the factorial-base grid σ = c_{n−1}^{a_{n−1}}⋯c_1^{a_1}
(0 ≤ a_k ≤ k, verified bijective): the top coefficient Δ(A) = Σ_a ∏_k (−1)^{k−a_k}/(a_k!(k−a_k)!) D_i(σ_a)
is NOT a det-multiple (n = 3 symbolic; n = 4: 10 distinct ratios) but was nonzero on all 10 random
A at n = 4. So **Δ(A) ≠ 0 ⟹ (S′)(A,i)** (valid where (n−1)! is invertible) — a generic certificate
off a hypersurface, useless exactly on the structured A that matter. Filed, not pursued.
**Standing picture after round 6 (for the next turns):** the proof-shaped target is (T_m) ⟺ (S′);
its deflation is not self-similar ((W) fails), the naive symmetrisations fail, transpositions are
exactly understood (Lemma T). Open moves: (i) grade K6-LEAN / K6-N4b / K6-T / K6-S as they land;
(ii) a "descent with potential" argument for (S′): from any σ, some transposition improves a
potential built from the left-eigenvector coordinates at i; (iii) characterise (S′)-tight matrices
(the [e_l, e_l, e_l+e_a, …] family) and prove (T_m) for the class "every column has weight ≥ 2" by
a second deflation that tracks the weight vector explicitly.

## R6.11 · Three harvests graded (03:1x CDT)
**K6-LEAN (codex5, sol high) — `engine/harvest/k1695_r6_lean/REPORT.md`, file `lean/proofenv/K1695/TranspositionLemma.lean` (209 lines, 0 sorry).**
Re-run HERE: `lake env lean K1695/TranspositionLemma.lean` → exit 0, and `#print axioms` for every
theorem is exactly [propext, Classical.choice, Quot.sound] (log `logs/k1695/round6_lean_recheck.log`,
2m24s wall incl. Mathlib load). **KERNEL-CHECKED (BANKED per VERIFY_CHECKLIST A.1):** L1 (P_τ = I − ddᵀ,
P_τ² = I, inverse), L2 (rank(AP_τ − μI) = rank((A − μI) + μ ddᵀ)), L3 (rank-one update bounds),
L4 = T0 (μ ∉ spec A ⟹ rank ≥ n−1), L5′ = T3 with the hypothesis 3 ≤ n (the ticket's L5 as literally
stated is false at n = 2 by truncated subtraction — engine's counterexample n=2, A=I, μ=1, correct).
NOT proved: L6 (T2) — the ticket carried the PRE-repair statement without μ ≠ 0; the engine found the
same μ = 0 hole (K = ℚ, A = diag(1,1,0,0), a=2, b=3) — consistent with §R6.6; L7 (T4) not attempted.
Statement fidelity check (mine): the Lean statements match §R6.1/§R6.3 for L1–L4; L5′ = T3 for n ≥ 3.
Follow-up ticket K6-LEAN2 (L6 with μ ≠ 0; L7 quadratic case) written.
**K6-N4b (codex7, sol high) — `engine/harvest/k1695_r6_n4b/REPORT.md`, `verify.c`, logs.**
Graded against §R6.7: no void condition (graph lemmas machine-checked on all 2-subspaces over
GF(2,3,5): 0 failures; P = I control fails on every input; no floating point). **Rank-2 cases (α)
[S = νI] and (ε) [spec S = {1,1}] PROVED over every field** — the proofs coincide with my §R6.4/§R6.7
derivations (graph lemma + Lemma T with ν ≠ 0 noted explicitly); exhaustive checks: (α) 10 530 /
182 784 / 1 511 250 distinct A over GF(3)/GF(4)/GF(5), 0 failures; (ε) 1 470 / 81 120 over GF(2)/GF(3).
Cases (β),(γ),(δ) and rank 1: UNRESOLVED (honest; no counterexample; every rank-2 input in
15 540 + 2 590 + 477 750 + 3×100 000 rescued by a transposition; rank-1 exhaustive over GF(2..5):
105 / 4 240 / 48 705 / 311 376 with 0 failures, 3-cycle needed in 6/32/36/184). Its smallest sharp
rank-2 diagnostic: GF(2), S with charpoly t²+t+1, exactly ONE working transposition (34). It also
corrected a parenthetical of mine: over GF(2), A = I + uvᵀ is invertible iff vᵀu = 0 (my "|supp u|
even" was the u = v = 1_S special case of §R4.2, over-generalised in the ticket). Adopted.
⟹ stratum (a) status: (α),(ε) closed; (β),(γ),(δ), rank 1 OPEN. n = 4 remains half-closed.
**K6-S (codex6, spark) — `engine/harvest/k1695_r6_S/logs/cell1-5.log`, `scan.c`.**
Cell 3 (GL(4,4)): the ticket's population "62 894 592" was MY arithmetic error; the true
|GL(4,4)| = 255·252·240·192 = **2 961 100 800 = exactly the checked count** (dialogue caught it, I
recomputed). So cell 3 is VALID: (S) on ALL of GL(4,4), 0 failures, i = 0 first-success everywhere
(734 s). **(S′) now verified on all of GL(5,2), GL(4,3), GL(4,4).**
Cells 4–5 ((T_4)/GF(3), (T_5)/GF(2)) are **VOID**: cell 4 printed 10 511 FAIL_T matrices; I re-tested
the first 200 with my independent `T_test` (`round6_T4_gf3_check.py`, log
`logs/k1695/round6_T4_gf3_check.log`): **200/200 refuted — every one HAS a witness** (the dialogue
independently found 24 witnesses for the first). The scan's (T) routine is buggy (the FAIL_T matrices
all have a repeated column — likely a bijection/duplicate-column bug), so its cell-5 "fail=0" is
unreliable too. Status of (T_4)/GF(3) and (T_5)/GF(2): UNKNOWN pending a fixed scan (K6-S2 ticket).

## R6.12 · ⭐ n = 4 rank 2, case (β) CONJUGATE sub-case CLOSED by hand (provisional)
Setting §R6.7: A = I + UWᵀ (rank 2), X = col U, Y = col W, S = I₂ + WᵀU with eigenvalues ν₁ ≠ ν₂,
both ≠ 1; r_j = Uc_j, ℓ_j = Wf_j (right/left eigenvectors of A at ν_j; c_j, f_j those of S).
**Lemma (β-conj).** If ν₁ ∉ F (so ν₂ = ν̄₁), some transposition makes AP_τ cyclic.
Proof. A transposition (ab), d = e_a − e_b, fails only at μ ∈ {1, ν₁, ν₂} (T0). At 1 (g = 2, T2):
d ∈ X ∪ Y. At ν_j (g = 1, T1): d ⊥ r_j and d ⊥ ℓ_j (and a scalar clause we do not need). Since the
eigenvectors of S at conjugate eigenvalues are Galois conjugate and U, W are F-rational, r₂ = r̄₁,
ℓ₂ = ℓ̄₁, so "d ⊥ r₁" ⟺ "d ⊥ r₂" (d rational) and the ν₁- and ν₂-failure sets coincide and require
d ⊥ r₁, r₂ and d ⊥ ℓ₁, ℓ₂. As r₁, r₂ span X ⊗ F̄ (they are independent: a rational-up-to-scale r₁
would force c₁ rational, impossible for a non-rational eigenvalue), d ⊥ X, i.e. d ∈ X⊥; likewise
d ∈ Y⊥. Hence every failing edge lies in G_X ∪ G_Y ∪ (G_{X⊥} ∩ G_{Y⊥}) ⊆ (G_X ∪ G_{X⊥}) ∪ (G_Y ∪ G_{Y⊥}),
each of which is contained in a triangle or a perfect matching (graph lemma, §R6.7 / K6-N4b Lemma 2),
and two such sets never cover K₄. ∎
Machine support: K6-N4b's exhaustive rank-2 tables (all distinct A over GF(2) and GF(3), 2 590 +
477 750, every input rescued at the transposition stage) contain every conjugate-(β) instance; its
sharpest diagnostic (GF(2), charpoly(S) = t²+t+1, exactly one working transposition) is this
sub-case and confirms the bound is tight, not slack.
**Still open at n = 4:** (β) with ν₁, ν₂ ∈ F distinct, (γ) Jordan, (δ) 1 ∈ spec S, and rank 1.
For the rational simple-eigenvalue cases the scalar clause reads `1 + ν dᵀ(A − ν)^# d = 0` with
(A − ν)^# = Σ_{λ≠ν} Π_λ/(λ − ν) (spectral projectors) — an explicit quadratic condition on the pair
{a,b}; the remaining work is showing that G_X ∪ G_Y ∪ (L₁∩R₁∩scalar₁) ∪ (L₂∩R₂∩scalar₂) ≠ K₄, where
L_j, R_j are the level-set graphs of ℓ_j, r_j (complete graphs when the eigenvector is constant,
i.e. when A has constant column/row sums ν_j).

## R6.13 · K6-T — PRE-REGISTERED grading (written before reading the report)
Ticket `engine/briefs/k1695_r6_T/TICKET.md` (prove (T_m) or break it). **VOID:** a "proof" step
without a machine check where it has finite instances; a residual statement not stated exactly;
floating point. **Grading:** a counterexample to (T_m) counts only after `round6_controllable.py:T_test`
confirms it (the spark FAIL_T lesson); a proof of (T_m) for a FIXED m over every field banks as a
theorem for that m after my re-derivation; "residual statement X is false, witness Y" banks as a
negative result after I re-run Y; prose strategies bank as nothing. Expected: (T_1), (T_2) trivial;
anything at m ≥ 3 over all fields is progress.

### R6.13 result · K6-T GRADED (codex8, sol high, 45 min) — `engine/harvest/k1695_r6_T/{REPORT.md, search.c, residuals.py, covering.py, logs/}`
No void condition. **Banked (after my re-derivation of the 2×2 identity `det[b, [c_k c_l]b] =
x_j det(c_j,c_k) + y_j det(c_j,c_l)` and the case chain):** (T_1), (T_2) hold over every field.
(T_2) ⟺ (S′)_3: for every A ∈ GL(3,F) and every i some AP_σ has e_i as cyclic vector — a sharper form
of the n ≤ 3 theorem.
**Negative results (witnesses re-checked by me):** (a) the minimum-support deflation residual
C_r ⟹ H_r is FALSE — GF(3), r = 1, A = [1 1], v = [1] (arising from columns b = (1,2)ᵀ, c = c = (2,2)ᵀ);
(b) "every bad injection has a base-field witness" is FALSE — GF(2), R = [0, e₁, e₁+e₂], the choice
b = 0 with order [e₁+e₂, e₁] fails only through the extension eigenvalues of x²+x+1; (c) the union
bound on left-eigenvector covers cannot close: R = [0, e₁, e₂] has cover-size sum 6 = |Ω| but union 4.
Cover-size formula (4): a witness (y, λ) covers (t+1)·∏ m_a! injections (t = #zeros of y, m_a the
coordinate multiplicities) — machine-checked on all multisets through m = 3 over GF(2), GF(3).
**Census (its search.c, independent Leibniz cross-check, exact fields):** (T_5)/GF(2) exhaustive
1 083 264 rank-5 multisets, 0 failures; **(T_4)/GF(3) exhaustive 26 485 056, 0 failures** (this REPLACES
the void spark cell 4 — the engine identified the spark bug: `run_cell_T` allocated six permutation
slots for 24/120 permutations); (T_3)/GF(7) exhaustive 571 514 832, 0; (T_3)/GF(8) exhaustive
2 841 225 408, 0; (T_3)/GF(9) 77.36 % prefix (9 043 459 139 rank-3), 0; three 10⁷-matrix LCG windows,
0. ⟹ (T_3) has no counterexample over GF(q), q ≤ 8, exhaustively, and (T_4)/GF(3), (T_5)/GF(2) are
clean. Verdict: (T_m) survives every attack so far; the two naive induction routes are provably dead.

## R6.14 · K6-LEAN2 GRADED — selected components of Lemma T are kernel-checked: T0, T3 (n ≥ 3), the nonderogatory direction of corrected T2 (μ ≠ 0), and the hard quadratic-descent inclusion of T4 under an explicit decomposition hypothesis (wording replaced after the K6-AUDIT, §R6.20)
`lean/proofenv/K1695/TranspositionLemma.lean` (429 lines, 0 sorry). Re-run HERE (`lake env lean`,
log `logs/k1695/round6_lean2_recheck.log`): all 16 theorems; no theorem uses an axiom beyond
[propext, Classical.choice, Quot.sound] (fifteen print exactly that list; `smul_vecMulVec` prints
[propext, Quot.sound]). Statement fidelity checked by reading the source: `l6a_rank_one_update_eq_add_one`
(x ∉ col E, y ∉ row E ⟹ rank(E + xyᵀ) = rank E + 1), `l6prime_t2_corrected` (μ ≠ 0, 2 ≤ n,
rank(A − μ) = n − 2, d ∉ col, d ∉ row ⟹ rank(AP_τ − μ) = n − 1 — exactly the T2 direction used by the
stratum-(b) proof), `l7_quadratic_descent_with_decomposition` (with the power-basis decomposition
z = z₀ + μz₁ as an explicit hypothesis, as permitted; conclusion w = (A² − tA − s)z₁ ∈ col_F(m(A))),
plus `one_mu_coefficients_eq_zero`. **BANKED per VERIFY_CHECKLIST A.1 (Lean, 0 sorry, axioms clean).**
What is still NOT in Lean: T1 (the g = 1 scalar clause), T4 for general degree, and the stratum-(b)
theorem itself (needs invariant factors / eigenvalue theory over an extension) — candidates for later.
Next tickets written: K6-T2 (`engine/briefs/k1695_r6_T2/`, prove (T_3) over every field ⟹ n = 4 in
full) and K6-N4c (`engine/briefs/k1695_r6_n4c/`, remaining stratum-(a) cases with §R6.12 as model).

## R6.15 · PRE-REGISTRATION for K6-T2 and K6-N4c (written before reading either report)
K6-T2 ((T_3) over every field): VOID if a lemma lacks a machine check where it has finite instances,
or a residual is not stated exactly. A full proof banks only after my case-by-case re-derivation;
a proof restricted to a characteristic or to a sub-case banks as that sub-case; an exact residual +
its finite-field verification banks as "the remaining statement"; prose does not count.
K6-N4c (stratum (a), four cases): same void rules plus the "always P = I" control; each closed case
must be re-derived by me; an input family where all six transpositions fail is a RESULT (it bounds
what any transposition-only argument can do) if the family is printed and re-verifiable by my
oracle; UNRESOLVED cases stay open.
K5-OOS (dialogue's ticket, K5-GFQ out-of-sample): graded against §R4.6/§R4.8 — CSV hashes must
reproduce byte-exactly; independent checker must agree on all NONE cells and on ≥ 500 witnesses;
out-of-sample cells must pass my `round4_reciprocal.py:pair_candidate` on a sample I pick.

## R6.16 · K6-T2 and K6-N4c GRADED (04:1x) — no proof either side; two structural facts banked
**K6-T2 (codex8, 23 min) `engine/harvest/k1695_r6_T2/`.** No void. Not a proof of (T_3). Banked after
my check: identity (1) `det[b,Mb,M²b] = Σ_{i<k} det(b,c_i,c_k)(b_i h_k − b_k h_i)` (h = Mb; pure
multilinearity) and the alternating six-order identity (3)
`Σ_{π∈S₃} sgn(π) K_π(b) = −(𝟙ᵀb)·det(b, 𝟙, u+v+w)·det(b, u−v, v−w)` (symbolic expansion over ℤ,
396 terms, plus 43M finite checks) — a sufficient criterion (three nonzero factors for one column ⟹
some ordering works) that is NOT complete (hard core over GF(2): R = [[1,1,1,1],[1,1,0,1],[0,0,1,1]]).
Exact residual for Case B (all κ_j ≠ 0, R = C[e₁ e₂ e₃ β], β ∈ (F^×)³): "one of the 24 cubics
det(C)·det[v_j, BCv_j, BCBCv_j] is nonzero" — the statement K6-T3 now attacks by Gröbner/saturation.
Negative: the fixed-column weighted-(T_2) deflation is false over every field (b = (0,1,−1)ᵀ with
columns (0,1,0)ᵀ,(0,1,0)ᵀ,(1,0,0)ᵀ). Census: (T_3) exhaustive over GF(2,3,4,5), 0 failures.
**K6-N4c (codex5, 9 min) `engine/harvest/k1695_r6_n4c/`.** No void. All four cases UNRESOLVED
field-uniformly; failure-set lemmas (β-rat)/(γ)/(δ) proved (they coincide with §R6.12's structure);
permutation-update lemma for arbitrary σ proved; rank-1 exhaustive over GF(2..9) (up to 4.78M
matrices), 0 failures. ⭐ **Structural fact, RE-VERIFIED here (`round6_n4c_verify.py`,
`logs/k1695/round6_n4c_verify.log`):** over GF(4) there are stratum-(a) rank-2 matrices — one in
(β-rat) [A = ((3,2,0,1),(0,1,0,0),(2,2,1,2),(0,0,0,2)), 2 = α, 3 = α+1], one in (γ)
[A = ((1,0,0,0),(3,0,2,0),(3,2,0,0),(0,3,3,1))] — for which **ALL SIX transpositions fail**; in both,
all three double transpositions work (3/3) and most 4-cycles (6/6, 4/6) and (3,1)s (6/8, 4/8). So a
transposition-only theorem is FALSE for stratum (a); the two examples have witnesses of types (2,2),
(3,1) and (4) — they force no particular cycle type (wording replaced after the K6-AUDIT, §R6.20).
(§R6.12's conjugate sub-case is unaffected — those examples have rational spec S.) Consequence for
the attack: the (T_3)-route (no stratification) is now the main line for n = 4; the stratum route
needs the rank-two update criterion (K6-N4d).
**K5-OOS (codex4, dialogue's ticket, 9 min) `engine/out/codex/k1695_k5_oos_report.md`, artifacts
`problems/k1695/k5_oos/`.** CSV hashes reproduce byte-exactly (full b9e4bde9…, NONE bc94363f…);
independent from-scratch checker: 0 disagreements on all 177 in-sample NONE cells (populations
match), 1 000 seeded witnesses, and all 7 794 out-of-sample cells (n = 31..40 on the original fields;
q ∈ {11,13,16}, n ≤ 30); every NONE cell is in the all-ones family. FINDING: the literal
"n ∈ {4,8,16}" clause does not extend — at n = 32 the all-ones family has NONE cells k ∈ {2, 30}
for q ∈ {3,5,7,9}; in the tested odd-characteristic range the extra NONE cells occur exactly at
n ∈ {4, 8, 16, 32}, k ∈ {2, n−2}, which SUPPORTS the conjectural replacement "n a power of 2" (claimed
only on the tested range). §R4.1 explains why these cells are candidates — two live tokens (1,1) give
c = −1 of order ℓ = 2 and n = m = 2^a, so every gap leaves a candidate — but §R4.1 leaves the secular
clause to decide, so it does not prove that the whole infinite residue is NONE (wording replaced after
the K6-AUDIT, §R6.20).
My spot-check of the new-field witnesses with `pair_candidate` (§R6.15 condition): see
`logs/k1695/round6_k5oos_spot.log` (recorded below in §R6.17 once run).

## R6.17 · K5-OOS spot-check with MY instrument — PASS
`problems/k1695/round6_k5oos_spot.py`, `logs/k1695/round6_k5oos_spot.log`: all 2 163 FOUND witnesses
over q ∈ {11, 13} (n ≤ 30) are CLEAN under `round4_reciprocal.py:pair_candidate` (0 dirty); control:
in all 56 NONE cells with k = n the all-ones placement is DIRTY (56/56) — the instrument can fail and
did not. (GF(16) skipped: my GF builder lacks the degree-4 modulus; the engine's own checker covered
it.) ⟹ K5-GFQ's construction + criterion now stand on three independent implementations
(theirs, codex's from-scratch checker, mine); the R4.8 verdict "decision procedure, not closure" is
unchanged, and every observed NONE cell lies in §R4.1's candidate residue (wording per §R6.20).

## R6.18 · ⭐ MILESTONE — K6-LEAN3 GRADED: Kourovka 16.95 for n = 3 is KERNEL-CHECKED (cyclic-vector form), plus (S′)₃
`lean/proofenv/K1695/CyclicVectorThree.lean` (530 lines, 0 sorry, 19 theorems). Re-run HERE:
`lake env lean K1695/CyclicVectorThree.lean` → exit 0, every `#print axioms` ⊆ [propext,
Classical.choice, Quot.sound] (log `logs/k1695/round6_lean3_recheck.log`). Statement fidelity, read in
source: `t2_rank_two_matrix` — for every 2×3 matrix of rank 2 there are distinct j,k,l with
`LinearIndependent K ![c_j, [c_k c_l]·c_j]` = (T_2) exactly; `kourovka_16_95_n3_every_coordinate` —
for every A with `IsUnit A.det` and every i there is σ : Perm (Fin 3) with e_i, Me_i, M²e_i linearly
independent, M = A * σ.permMatrix K (columns permuted: `(A*P_σ) i j = A i (σ⁻¹ j)`) = (S′)₃ exactly;
`kourovka_16_95_n3_cyclic_vector` — ∃ σ ∃ v with v, Mv, M²v linearly independent = "A P_σ has a
cyclic vector". **This is Kourovka 16.95 at n = 3 over every field in the cyclic-vector formulation.**
What is NOT formalised: the classical equivalence "has a cyclic vector ⟺ minimal polynomial =
characteristic polynomial" (the notebook's wording); it is standard, and stated here as the only
gap between the Lean theorem and the notebook's sentence. Also formalised: the six-choice scalar
core `t2_six_choices_scalar` (division-free, every field) and the deflation
`ctrl3_e0_of_ctrl2_lowerBlock`. **BANKED per VERIFY_CHECKLIST A.1 (Lean, 0 sorry, axioms clean,
statement checked).** First closed case of this campaign in Lean; the n ≤ 3 theorem §R3.6 (hand proof
+ 818 948-witness verifier) now has a second, kernel-checked proof by an entirely different route
((T_2) ⟹ (S′)₃ ⟹ 16.95(3)). Nothing outward; n ≥ 4 unchanged.
**Independent third check (dialogue's ticket, codex4, `engine/out/codex/k1695_lean3_fidelity_report.md`):
verdict YES-WITH-CAVEATS** — rebuild reproduces all 19 theorems with the claimed axioms; vacuity
examples over ℚ, ZMod 2, ZMod 3 pass; a non-invertible input is correctly not covered. The two
caveats, recorded verbatim as formalisation boundaries (not counterexamples): (i) "lines 23–25/499–508
prove the Krylov formulation directly — no theorem identifies it with minpoly = charpoly / Mathlib's
cyclic notion"; (ii) "lines 42–49: Mathlib's `σ.permMatrix` convention makes column j of A·P_σ equal
column σ.symm j of A, whereas the registry labels P_π e_j = e_{π(j)} — reconcile by π = σ.symm."
So, in this registry's convention, what is formalised is: for every A ∈ GL(3,K) there is π (= σ⁻¹ in
Mathlib's convention) with A P_π having a Krylov cyclic vector — the same set of six products, so
the mathematical content is unchanged; the sentence above now says so.
**Caveat (i) CLOSED in §R6.29 (K6-LEAN5): `kourovka_16_95_n3` states minpoly = charpoly directly.**

## R6.19 · K6-N4d GRADED (codex9, sol high) — rank-two update criterion banked; my ticket's (3,1) "iff" corrected
`engine/harvest/k1695_r6_n4d/`. No void. **Banked (re-derived by me):** the border-reduction
formula `nullity(E + XYᵀ) = (g − rank D) + dim T` (D = Yᵀ|_{ker E}, C = X mod im E, Q = I₂ + YᵀGX,
T = {z ∈ ker C : Qz ∈ im D}) and its explicit g = 0..3 clauses, checked on all GL(4,2)/GF(4) and all
GL(4,3)/GF(9) (436.7M cells) with a negative control that fires; the eleven factorisations of
μ(I − P_σ⁻¹) for two-cycle σ; the exact characterisation (6) of "all six transpositions fail" in
(β-rat)/(γ)/(δ); clause diagnoses of the two GF(4) inputs (β: edges 01,02,03,23 fail at 1 by T2,
12 at ν=2 and 13 at ν=3 by T1; γ: 01,02,13,23 at 1, 03 at 2, 12 at both). **Correction adopted:** my
K6-N4d ticket wrote "type (3,1) with fixed point f is clean at 1 iff u_f ≠ 0 ∧ v_f ≠ 0" — FALSE as an
iff (only sufficient); the exact statement, which I re-derived from Lemma 0 (nullity(M − I) =
dim(K₁ ∩ w⊥) + ε, K₁ = ⟨e_f, 𝟙_C⟩): for types (3,1) and (2,2), `nullity(AP_σ − I) ≥ 2 ⟺ u ∈ Z_σ or
v ∈ Z_σ` (all cycle sums of u, or of v, vanish); for (3,1): [u_f = 0 ∧ Σ_{i≠f} u_i = 0] or the same
for v. §R3.13 already had this form; the ticket compressed it wrongly (same lesson as §R4.7: a
compressed restatement is a new claim). Exhaustive check over GF(2..9): 0 disagreements, the wrong
"iff" as negative control fires (304 … 7 091 712). Rank-2 rescue selection and rank 1: UNRESOLVED.

## R6.20 · K6-AUDIT (dialogue's adversarial audit of §R6.*) — LOGGED and APPLIED
`engine/out/codex/k1695_r6_audit_report.md` (codex4). 44 claim rows: central result SURVIVES
(invariant factors (m,m), m irreducible ⟹ every transposition cyclic; stratum (b) supported);
every artifact re-run by the auditor reproduced (all round6_*.py, five C sources rebuilt with
-Werror, hashes, populations). Verdicts other than EXACT: T2 (R6.1 without μ ≠ 0) WRONG — already
repaired in §R6.6; L1 ("axioms exactly …") WRONG — `smul_vecMulVec` uses [propext, Quot.sound];
L3 (R6.14 "FULLY kernel-checked") OVERSTATED; C6 (R6.16 "must sometimes be (2,2) or (3,1)") WRONG —
the examples also have 4-cycle witnesses; O2 (R6.16–17 "the correct statement is n a power of 2")
OVERSTATED — the OOS report claims only the tested range and R4.1 gives the candidate residue only.
**Applied:** §R6.14, §R6.16, §R6.17 wording REPLACED in place with the auditor's replacement text
(no annotation), §R6.11's "exactly" superseded by "no axiom beyond". Lesson (recurring, §R4.7 and
§R6.19 too): my compressions and summaries are the error source, not the mathematics — every
summary sentence is a claim and gets the same scrutiny as a theorem.

## R6.21 · K6-N4e GRADED (codex9, 13 min) — the double-transposition rescue is a robust CENSUS fact; three lemmas banked; theorem open
`engine/harvest/k1695_r6_n4e/`. No void (two independent cyclicity oracles, P = I and fixed-transposition
controls fire, populations exact). **Census:** ALL 22 940 820 distinct rank-two updates B = A − I over
GF(4) (357 column spaces × 64 260 coordinate maps, each B once; 16 109 268 invertible A; 7 996 800 in
(β-rat)/(γ)/(δ)): exactly **216 all-six-transpositions-fail inputs (192 β-rat, 24 γ, 0 δ), and for every
one of them ALL THREE double transpositions are cyclic** (648/648 products, both oracles). Five 10⁶-
presentation windows over GF(5), GF(7), GF(8), GF(9): no all-six-fail input in THOSE samples (GF(4):
25 in 10⁶) — they do exist in odd characteristic, e.g. the GF(7) Klein-four example of §R6.37, where
only 2 of the 3 double transpositions work.
**Banked after my re-derivation:** Lemma 1 — at a simple eigenvalue ν (g = 1), a matching M = {ab, cd}
is clean whenever its two edges are not both in L_ν = {e : d_e ∈ im(A−ν)} and not both in
R_ν = {e : d_e ∈ row(A−ν)} (C: Z_M → coker E and D = Zᵀ|_{ker E} are then both nonzero, and N4d's g = 1
clause says clean — no scalar clause needed); Lemma 2 — at μ = 1 with rank C = rank D = 1 the matching
is clean iff the compatibility scalar κ_M = ηᵀQξ ≠ 0 (ξ spans ker C, η spans ker Dᵀ, Q = I₂ + ZᵀGZ), with
rank C = 2 − dim(Z_M ∩ X), rank D = 2 − dim(Z_M ∩ Y); Lemma 3 — at a non-eigenvalue μ, nullity 2 iff
Q_M(μ) = I₂ + μ Zᵀ(A−μ)⁻¹Z = 0. **Cover patterns realised over GF(4) (machine census, not an all-field
classification):** β-rat: G_X one edge, G_Y a triangle, L_j a matching and R_j a triangle at each ν_j;
γ: G_X, G_Y triangles sharing an edge, L_ν = R_ν = C_ν = one matching. In both, Lemma 1 already makes
the matching M₀ clean at every simple eigenvalue; the whole residual is κ_{M₀} ≠ 0 at 1 and
Q_{M₀}(μ) ≠ 0 off the spectrum — plus proving these two patterns are the only ones over every field.
Status: rank-2 stratum (a) is reduced to two explicit scalar non-vanishings + a pattern classification;
UNRESOLVED. Next ticket K6-N4f attacks exactly that with the transposition-failure equations as
hypotheses (they are what should force κ ≠ 0).

## R6.22 · PRE-REGISTRATION (before reading) for K6-T3, K6-LEAN4, K6-N4f, K6-N4g
K6-T3: a Gröbner basis [1] banks as "(T_3) holds on that stratum in that characteristic" only after I
re-run the printed ideal with sympy myself (at least one stratum × one characteristic); strata not
finished = UNRESOLVED; msolve not built = a tooling gap, not evidence. K6-LEAN4: rebuild myself,
read every new statement; "Lemma T fully kernel-checked" may be written only for the exact list of
clauses proved, with general-degree T4 named as the exception if only the cubic fallback exists.
K6-N4f: a pattern "proved over every field" banks only after I re-derive the char-2 forcing and the
normal form and re-run its symbolic certificate; the classification stays open unless proved.
K6-N4g: any corrected clause of my ticket is adopted only after my re-derivation; Gröbner
certificates bank per branch only after a spot re-run; unresolved assignments are counted, not hidden.

## R6.23 · K6-LEAN4 GRADED — Lemma T kernel-checked: T0, T1 (iff), T2 (iff), T3 (n ≥ 3); T4: easy inclusion in general degree, hard inclusion in degrees 2 and 3 under an explicit power-basis decomposition hypothesis
`lean/proofenv/K1695/TranspositionLemmaFull.lean` (595 lines, 0 sorry, 16 theorems). Re-run HERE:
exit 0, every `#print axioms` exactly [propext, Classical.choice, Quot.sound] (log
`logs/k1695/round6_lean4_recheck.log`). Statements read in source: `t2_rank_eq_iff_both_sides_not_mem`
(μ ≠ 0, rank(A − μ) = n − 2: rank(AP_τ − μ) = n − 1 ⟺ d ∉ col ∧ d ∉ row) = T2 as an iff;
`t1_rank_drop_iff` (μ ≠ 0, rank(A − μ) = n − 1: rank(AP_τ − μ) = n − 2 ⟺ d ∈ row(A − μ) ∧ μd ∈ col(A − μ)
∧ ∃ z, (A − μ)z = μd ∧ 1 + d·z = 0) = T1 exactly, with the preimage-scalar well-definedness proved
separately; the rank-one-update trichotomy (`rank_one_update_eq_sub_one`, `…_eq_of_preimage_scalar_ne_zero`,
`…_le_of_one_side_mem`); `t4_minpoly_mulVec_mem_range` (general degree, easy inclusion);
`t4_cubic_minpoly_descent_with_decomposition` (degree 3, hard inclusion, coordinates assumed).
**Exact status sentence (audit-proof):** every clause of Lemma T that the n = 4 stratum-(b) proof uses is
kernel-checked; what is not is the hard inclusion of T4 in degree ≥ 4 and without the decomposition
hypothesis, and the stratum-(b) theorem itself. BANKED per VERIFY_CHECKLIST A.1.

## R6.24 · K6-N4f GRADED — the two realised rank-2 cover patterns are CLOSED over every field (provisional); classification open
`engine/harvest/k1695_r6_n4f/`. No void. **Re-derived by me:** (β) a left eigenvector ℓ₁ ∈ Y = ⟨d₀₂, d₀₃⟩
whose level graph is the matching {03, 12}: ℓ₁ = u d₀₂ + v d₀₃ = (u+v, 0, −u, −v); ℓ(1) = ℓ(2) ⟹ u = 0;
ℓ(0) = ℓ(3) ⟹ u + 2v = 0 ⟹ 2v = 0 with v ≠ 0 ⟹ **char 2**; (γ) r ∈ X = ⟨d₀₁, d₀₂⟩ with level graph
{01, 23}: r = (u+v, −u, −v, 0), 23 ⟹ v = 0, 01 ⟹ 2u = 0 ⟹ char 2. So both realised patterns live only in
characteristic 2 (216 over GF(4)); other all-six-fail patterns exist in odd characteristic (§R6.37,
GF(7) Klein-four family) — these two are NOT the only ones. Normal forms A_β(a,c) (a² + a + 1 = 0) and A_γ(λ) (λ ≠ 0,1); κ_{M₀} = 1 (β) and
(λ+1)/λ² (γ); off-spectrum Q(μ) certified via D(μ)·Q(μ) with D = det(A − μ); Krylov determinants
show EVERY double transposition works in both families. **Symbolic certificate re-run by me**
(`logs/k1695/round6_n4f_symbolic_rerun.log`: SYMBOLIC_COMPLETE … PASS, 0.9 s). Census: all 216
all-six-fail inputs over GF(4) fall into the two normal forms (4 symmetry orbits), κ ≠ 0 and off-spectrum
Q ≠ 0 on all of them; 10⁵ constrained samples per field over GF(4), GF(8), GF(16), 0 zeros; bad-double
control fires (κ = 0 predicted and observed). **UNRESOLVED:** that these two are the only all-field
covers in (β-rat)/(γ)/(δ) — one formal δ configuration (two triangles + a scalar matching) is not
excluded, and the constant-eigenvector branches are not enumerated.

## R6.25 · K6-T3 GRADED — Gröbner certificates for the two smallest Case-A strata of (T_3); the rest untouched
`engine/harvest/k1695_r6_T3/` (ideals/, certificates/, logs/). No void. Exact split by cofactor support
of κ (after column permutation): Case A support 1 (β = 0; 9 vars + t; 18 nonzero generators), support 2,
support 3, Case B (support 4). Also a real correction to my ticket: β₁ = 1 is NOT a legitimate
normalisation for the j ≠ 4 choices (integer witness printed) — adopted. **Certified [1] (sympy grevlex,
Rabinowitsch 1 − t·det C·∏β):** support 1 and support 2, over ℚ and over GF(p), p ∈ {2,3,5,7,11,13,17,19,23,29,31}
(19–150 s each) ⟹ on those two strata (T_3) holds in characteristic 0 and in those eleven characteristics
(each certificate covers every field of that characteristic). Support 3 hit the 1200 s cap over GF(2);
Case B not attempted (msolve could not be built: `autoreconf` missing, GMP/MPFR/FLINT absent, ticket
forbade fetching them). My independent spot re-run (own parser, `round6_t3_spot.py`,
`logs/k1695/round6_t3_spot.log`): PENDING at the time of writing — result recorded in §R6.27.
Status: (T_3) proved on two strata for 12 characteristics; not proved in general.

## R6.26 · K6-N4g GRADED — rank-1 stratum (a): one branch closed by 896 certificates; my (2,2) clause corrected; the case tree is too large
`engine/harvest/k1695_r6_n4g/`. No void. **Correction adopted after my re-derivation:** for σ = (ab)(cd)
at μ = −1 (char ≠ 2) the resonance has nullity 2 (both 2-cycles resonate), so by the T2-type clause the
failure is `(u_a = u_b ∧ u_c = u_d) ∨ (v_a = v_b ∧ v_c = v_d)` — NO secular clause; my ticket's
"candidate then secular" was the nullity-1 shape, wrong here (third compression error of the day). All
clauses machine-checked vs brute force over GF(2..5)×quadratic extensions, 0 disagreements, controls
fire. **Closed branch:** "all 17 permutations blocked at μ = 1" is inconsistent — 128 leaves × 7 fields
= 896 unit-ideal certificates (ℚ, GF(2,3,5,7,11,13)) with a negative control, plus exhaustive searches
over GF(7), GF(9), GF(13) with 0 survivors. **Everything else UNRESOLVED:** 214 990 847 split-generic
resonance assignments (6 560 in char 2, 32 767 in char 3) — the case tree is the wrong tool for rank 1.
Exhaustive decision searches over GF(2..9) (7 796 579 updates): 0 failures.
⟹ New plan for stratum (a): attack it through (T_3) restricted to R = A[≠i,:] = (partial identity) +
(rank ≤ 2) — a structured family where, e.g., for b ∝ u′ the Krylov space of M = (I + u′v′ᵀ)P_τ from u′
equals that of P_τ (tickets K6-N4h, K6-N4i).

## R6.27 · K6-T3 certificates INDEPENDENTLY REPRODUCED (resolves the PENDING in §R6.25)
`problems/k1695/round6_t3_spot.py` (own parser of the printed `.ms` ideals, sympy grevlex),
`logs/k1695/round6_t3_spot.log`: Case A support-1 over GF(2): basis [1] (17.1 s); support-1 over GF(3):
[1] (18.2 s); support-2 over GF(2): [1] (72.1 s). **Control that can fail:** dropping the Rabinowitsch
generator 1 − t·det C from the support-1/GF(2) ideal gives a NON-unit basis (152 elements) — so the
unit ideal is carried by the invertibility hypothesis, not by a degenerate generator set. ⟹ BANKED:
(T_3) holds on the Case-A strata "cofactor support 1" and "cofactor support 2" in characteristic 0 and
in characteristics 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 (the engine's 24 certificates, three of them
reproduced here from the printed ideals). Not banked: other characteristics on these strata (no
certificate coefficients were extracted), support 3, Case B.

## R6.28 · K6-LIT (Gemini 3.1 Pro, search-grounded, dialogue's seat) — recorded, NOT a novelty claim
`engine/harvest/k1695_r6_lit.md`. (1) column-ordering / standard-basis cyclic-vector statement
((T_m)/(S′)): NOT-FOUND (5 queries incl. "controllability under permutation", Krylov / controllable
pair / column permutation); (2) transposition lemma: NOT-FOUND as a statement; the engine alludes to
"general discussions on rank-one updates for transposition matrices" without URLs (dialogue chasing
them); (3) the invariant-factor (m,m) statement: NOT-FOUND exact; FOUND-RELATED only Dixon
arXiv:1606.02238 (withdrawn) quoting the conjecture; 2025–2026 openness re-check: NOT-FOUND (recent hits
are the Lie-type Thompson conjecture — the known homonym). Per VERIFY_CHECKLIST C.11 these are WEAK
negatives from a single search engine with citations unopened: they license "not found", never "new".
The transposition lemma is elementary rank-one-update algebra and is expected to be folklore in pieces
(cf. §R4.3: Bunch–Nielsen–Sorensen, Ferrante–Wimmer); a zbMATH pass + second engine is required before
any wording stronger than "not found in this sweep".

## R6.29 · ⭐ MILESTONE UPGRADED — K6-LEAN5 GRADED: Kourovka 16.95 for n = 3 is kernel-checked in the NOTEBOOK'S OWN FORMULATION
`lean/proofenv/K1695/CyclicToMinpoly.lean` (270 lines, 0 sorry, 5 theorems). Re-run HERE: exit 0,
every `#print axioms` exactly [propext, Classical.choice, Quot.sound] (log
`logs/k1695/round6_lean5_recheck.log`). Statements read in source:
- `minpoly_eq_charpoly_of_krylov_linearIndependent` (any n): `LinearIndependent K (fun k : Fin n ↦
  (M^k) *ᵥ v) → minpoly K M = M.charpoly` — the classical "cyclic vector ⟹ nonderogatory", via
  `minpoly.eq_of_linearIndependent` and Cayley–Hamilton.
- `kourovka_16_95_n3 (A : Matrix (Fin 3) (Fin 3) K) (hA : IsUnit A.det) : ∃ σ : Equiv.Perm (Fin 3),
  minpoly K (A * σ.permMatrix K) = (A * σ.permMatrix K).charpoly` — **verbatim the notebook's
  sentence for n = 3: for every invertible 3×3 matrix over every field there is a permutation matrix P
  with the minimal polynomial of AP equal to its characteristic polynomial.** (Convention note from
  §R6.18 caveat (ii) still applies harmlessly: Mathlib's `permMatrix` labels the permutation by its
  inverse relative to this registry; the set of six products is the same.)
- `cyclic_standardBasis_of_principalBlock` (any n = m+1): if the principal block of A·P_σ with row and
  column i deleted, together with the deleted pivot column, is a controllable pair, then e_i is a
  Krylov-cyclic vector of A·P_σ — the LOCAL deflation implication that the general-n argument
  (T_{n−1}) ⟹ (S′)_n uses; the theorem does not itself quantify over the global predicates (T), (S′)
  (scope wording per LEAN5FID, §R6.33); plus
  `krylov_feedback_linearIndependent` and `deleteCoordinate_mulVec`.
⟹ **§R6.18 caveat (i) is CLOSED.** BANKED per VERIFY_CHECKLIST A.1 (Lean, 0 sorry, axioms clean,
statement checked against the original wording). First kernel-checked closed case of Kourovka 16.95
in the problem's own words. Nothing outward; n ≥ 4 unchanged.

## R6.30 · LEAN4FID (dialogue's audit of K6-LEAN4) — LOGGED
`engine/out/codex/k1695_lean4_fidelity_report.md`: verdict on the dialogue's summary sentence "Lemma T
is fully kernel-checked except general-degree T4" = OVERSTATED; exact: T0, T3 (3 ≤ n), and the full
corrected T1/T2 criteria for μ ≠ 0 are kernel-checked over every field (hypothesis table all "exact");
T4 is NOT kernel-checked as the registry equality — Lean has the easy inclusion in general degree and
the reverse inclusion only in degrees 2–3 under an explicit decomposition hypothesis. This is exactly
§R6.23's heading; the auditor's replacement sentence is adopted verbatim as the canonical wording:
**"Selected components of Lemma T are kernel-checked: T0, T3 (n ≥ 3), the full T1 and T2 criteria for
μ ≠ 0; of T4 only the easy inclusion in general degree and the hard inclusion in degrees 2 and 3 under
an explicit power-basis decomposition hypothesis."**
Next: K6-LEAN6 (stratum-(b) theorem in Lean, with the nullity lemma as the hard step), K6-H (is the
Krylov dimension a hill-climbing potential? exact scan), K6-QREV (held-out cross-family review of
Lemma T / rationality / stratum (b) on Qwen3.8-Max, via dialogue).

## R6.31 · K6-N4h and K6-N4i GRADED — structured (T_3): the rank-1 residual is now a 6-variable system; rank 2 a 14-variable one
**K6-N4h (codex10, 26 min) `engine/harvest/k1695_r6_n4h/`.** No void. Banked after my re-derivation:
Lemma 1 (deflation: e_i cyclic for AP_p ⟺ det[b, Mb, M²b] ≠ 0 with b = A[≠i, j], M = A[≠i, τ]) — the
same statement as Lean's `cyclic_standardBasis_of_principalBlock`; Lemma 2 (F1): for the fixed-row
family R = [x, e₁ + y₁x, e₂ + y₂x, e₃ + y₃x] (x = (a,b,c), obtained by scaling so the deleted row has
v_i = 1), the exceptional column x works iff τ is a 3-cycle and det[x, Px, P²x] = ±S·Q ≠ 0 with
S = a+b+c, Q = a²+b²+c²−ab−bc−ca = (a+ωb+ω²c)(a+ω²b+ωc) — I checked the circulant determinant:
[[a,c,b],[b,a,c],[c,b,a]] has determinant S·Q ✓ (Q = S² in characteristic 3). Lemma 3: the 96
determinants D_{i,j,τ}(u,v) printed as integer polynomials (68 nonzero). Exhaustive decision audit
over GF(2,3,4,5,7) (919 104 updates): 0 failures, independent 4×4 Krylov oracle, P = I control.
Strong finite observation (not promoted): the LEAST i with v_i ≠ 0 always suffices (F1 first, then
the F2 columns). **The exact residual for a proof of that observation (hence of rank 1):** the two
6-variable systems (10) 𝒰_S = {S₀ = 0, D = 0 ∀D ∈ 𝒟} and (11) 𝒰_Q = {Q₀ = 0, D = 0 ∀D ∈ 𝒟}, 𝒟 = the 18 F2
determinants of the fixed row (variables a,b,c,y₁,y₂,y₃), plus the invertibility inequation. sympy
timed out at 120 s on (10) — a tooling limit; with msolve now built (K6-T4) this is the next run.
**K6-N4i (codex9, 49 min) `engine/harvest/k1695_r6_n4i/`.** No void. Banked: Lemma 1 (deflation, same);
Lemma 2 (exact G1 criterion: with φ the functional cutting out X′ = col U′, s = φ(Pb), t = φ(P²b + Px):
if s = 0 then b, Mb independent in X′ and t ≠ 0; if s ≠ 0 then b and h = sM²b − tMb independent in
X′ — plausible, machine-checked on 16M cells with a control that fires). Exhaustive GF(2)/GF(3)
(2 590 / 477 750 distinct A) + 3×10⁵ presentations: 0 failures. Residual: three 14-variable
Rabinowitsch charts (U normalised to [I₂; (a b); (c d)], W's pivot pair in 01/02/23), 92 distinct
determinants; sympy timed out (600 s) on the full system and on a 12-determinant subideal.
⟹ Both strata now reduce to explicit polynomial systems; the blocker is the Gröbner engine, not the
mathematics. Tickets: K6-N4k (msolve on the rank-1 systems (10),(11) — 6 variables — then the rank-2
charts; plus an integer Nullstellensatz certificate for all characteristics if [1]), K6-N4j (the
abstract cover-pattern classification for rank 2 as the parallel route).

## R6.32 · K6-QREV (Qwen3.8-Max, Thinking, cross-family, held-out) — LOGGED and APPLIED
`engine/harvest/k1695_r6_qrev.md` (model verified on screen by dialogue). Proof 1 (transposition
lemma) VALID; Proof 2 (rationality, any degree, no separability) VALID; Proof 3 (stratum (b)) GAP —
"the proof invokes T0 before excluding μ = 0, while the brief stated T0–T3 under μ ≠ 0", and "the
generalisation is asserted, the proof stays 4×4". No WRONG, no counterexample. **Assessment:** the
GAP is real as a reading of the BRIEF (my brief put μ ≠ 0 as a blanket hypothesis on T0–T3); it is
not a mathematical gap: T0 holds for every μ (rank-one-update bound; Lean `l4_t0` has no μ ≠ 0),
and μ ≠ 0 is only needed for T2, where it follows from m ≠ X. **Applied:** §R6.3's proof now states the
ordering explicitly, and the general-n statement (invariant factors (m,m), deg m = n/2, degree-one
case named) is written out as a paragraph instead of a parenthetical. Per VERIFY_CHECKLIST B.7/B.9:
this is a genuine cross-family channel (Qwen ≠ OpenAI ≠ Anthropic), held-out (no verifier tables),
and it found a presentation defect — banks as "cross-family found no mathematical defect, one
presentation defect repaired".

## R6.33 · LEAN5FID (dialogue's audit of K6-LEAN5) — YES; one scope wording fixed
`engine/out/codex/k1695_lean5_fidelity_report.md`: `K1695.kourovka_16_95_n3` kernel-checks 16.95 for
n = 3 in the notebook's minimal-polynomial formulation over every field; the only hypothesis is
`IsUnit A.det`; the witness ranges over all permutation matrices; the conclusion is the literal
`minpoly K (A*P) = (A*P).charpoly`; vacuity examples over ℚ, ZMod 2, ZMod 3 pass. Ancillary
correction adopted: `cyclic_standardBasis_of_principalBlock` is the LOCAL deflation implication
(controllable principal block + pivot column ⟹ e_i Krylov-cyclic) used inside (T_{n−1}) ⟹ (S′)_n; it
does not itself state the global predicates (T) and (S′). §R6.29's wording amended accordingly.

## R6.34 · K6-LEAN6 GRADED — partial: stratum (b) rank statement at a quadratic root, with the nullity as a hypothesis
`engine/harvest/k1695_r6_lean6/REPORT.md`. Proved (per report; my rebuild of the file pending the
next Lean re-run — recorded as PENDING until then): T4 quadratic descent WITHOUT the decomposition
hypothesis (constructed from a degree-2 `PowerBasis`), μ ∉ F, the quadratic annihilator of A and Aᵀ,
both T2 transversality conditions, and `stratumB_rank_at_root_of_simple_extension_and_nullity`:
for L = F(μ) generated by an integral quadratic μ, μ a root of m, and `hnull : rank(A_L − μ) = 2`,
`rank(A_L · swap(a,b) − μ) = 3`. NOT proved: the nonroot case / global spectral reduction (every
possibly-derogatory eigenvalue of AP is a root of m), the nullity lemma (invariant factors (m,m) ⟹
nullity 2), and the bridge to minpoly = charpoly. Status: the stratum-(b) THEOREM remains a hand
theorem (§R6.3, cross-family clean); its Lean version is ~60 % assembled with the nullity lemma as
the named gap.

## R6.36 · K6-N4j GRADED — formal cover enumeration complete; too coarse to close rank 2 by itself
`engine/harvest/k1695_r6_n4j/`. Complete enumeration under the stated structural constraints: 116 γ,
116 δ, 5 131 β-rat orbits (`pattern_verdicts.tsv`); the two N4f patterns are in the list with their
proved char-2 normal forms; the other 5 361 orbits have neither a realisation nor an exclusion
certificate. The GF(4) census proves the finite statement there (216 all-six-fail inputs = 192 β + 24
γ); 5×10⁵ presentations over GF(3,5,7,8,9): no all-six-fail input. Verdict: the graph-pattern route is
too coarse (the scalar-clause graphs C_ν are formally free); the algebraic charts (K6-N4k, msolve) are
the live route for rank 2. No counterexample.

## R6.35 · ⭐ K6-H GRADED — the Krylov dimension is NOT a strict hill-climbing potential, but "one equal step, then ascent" never fails on any scanned cell
`engine/harvest/k1695_r6_H/` (codex11, C, exact; each B = AP_σ enumerated once × n! with a
quotient-graph control; populations = ∏(qⁿ − qⁱ)). Cells: GL(3,q) q ∈ {2,3,4,5,7}, GL(4,2), GL(4,3),
GL(5,2) — up to 6.0×10⁹ (A,σ,i) triples. **Strict ascent: NO** — local maxima (kd < n, no neighbour
larger) exist: none in GL(3,2), GL(3,3); 5 184 in GL(3,4); 14 400 in GL(3,5); 254 016 in GL(3,7);
768 in GL(4,2); 445 824 in GL(4,3); 1 804 800 in GL(5,2) (kd values 2..n−1). **Strict peaks (all
neighbours smaller): 0 everywhere. Two-step traps (no neutral step followed by an ascent): 0
everywhere** — for kd, for kd_max, and for the defect δ. **RE-VERIFIED HERE** (`round6_H_verify.py`,
`logs/k1695/round6_H_verify.log`): the smallest local maximum A = ((1,2,1),(2,1,1),(1,0,0)) over
GF(4), σ = id, i = 2: kd = 2, all three transposition neighbours kd = 2, and (0 1) then (0 2) reaches
kd = 3 — exact match. Controls: A = I gives kd = cycle length through i; a wrong kd changes every
count; 80 000 independent-rank cross-checks, 0 mismatches.
⟹ **Conjecture (H2)**: from any (A, σ, i) with kd < n there is a two-step path (neutral transposition,
then ascending transposition) — (H2) ⟹ (S′) ⟹ 16.95 by iteration. This is the first candidate for a
GENERAL-n proof mechanism with exhaustive support (ticket K6-H2: mechanism, refined potentials
without local maxima, proof attempt).

## R6.37 · ⭐ K6-N4m GRADED — the "all-six-fail ⟹ characteristic 2" reading is FALSE; a Klein-four group-algebra family
`engine/harvest/k1695_r6_n4m/` (codex10, 20 min). Shape reduction valid (16 shape orbits of (G_X, G_Y),
92 spectral conjuncts, 22 with verdicts, 70 open). **Counterexample to the char-2 reading, RE-VERIFIED
HERE** (`round6_n4m_verify.py`, `logs/k1695/round6_n4m_verify.log`): over GF(7),
A = ((2,3,4,6),(3,2,6,4),(4,6,2,3),(6,4,3,2)): rank(A) = 4, rank(A − I) = 2, row/column sums ≡ 1,
nullities at μ = 1, 2, 4: 2, 1, 1 (spectrum {1,1,2,4}, case (β-rat) with 𝟙 a right AND left eigenvector
— the constant-eigenvector sub-case the graph arguments excluded); **all 6 transpositions and all 8
(3,1)-permutations non-cyclic; 2 of the 3 double transpositions and all 6 four-cycles cyclic.**
Structure: A_{ij} = f(i ⊕ j) for the Klein four-group V₄ acting regularly on {0,1,2,3}, i.e.
A = Σ_{g∈V₄} f(g)·P_g with f = (2,3,4,6) — a group-algebra family, the V₄-analogue of aI + bJ.
**Corrections applied in place:** §R6.21's "no all-six-fail input at all" (true only of those 4×10⁶
samples) and §R6.24's "consistent with the census" now carry the pointer here; §R6.21's "ALL THREE
double transpositions" is a GF(4) fact only — in the GF(7) example one double transposition fails, so
the surviving conjecture is "some (2,2) or (4) works", not "every (2,2)". K6-N4e's Lemmas 1–3 are
unaffected (they are exact criteria). Lesson (again): a pattern read off one field is a census.
Next: K6-N4n — normal form of the odd-characteristic family (V₄ group algebra?), its rescue proof,
and the 70 remaining conjuncts by msolve.

## R6.38 · Group-algebra families at n = 4 (census, light, `round6_v4_family.py`, `logs/k1695/round6_v4_family.log`)
V₄ family A_f = Σ_{g∈V₄} f(g)P_g (A[i][j] = f(i ⊕ j)) and the circulant Z₄ family, ALL invertible members
over GF(q), q ∈ {2,3,4,5,7,9,11,13} (up to 20 736 members each): **no member defeats S₄**; the minimum
number of cyclic products is 6 in every cell, attained exactly by the monomial members A = v·P_g
(whose good σ are those with gσ a 4-cycle, resp. the (3,1)-type rescues for Z₄'s shift). The GF(7)
example of §R6.37 (f = (2,3,4,6), f̂ = (1,2,4,1)) has 8 good σ. Character computation (V₄, char ≠ 2):
for σ ∈ V₄ the eigenvalues of A_f P_σ are χ(σ)·f̂(χ), so a double transposition works iff χ ↦ χ(σ)f̂(χ)
is injective — this reproduces exactly which two of the three double transpositions rescue the GF(7)
example ((03)(12) recreates the coincidence 1 = χ_c(σ)·1). The family that could be genuinely hard is
the elementary-abelian one at n = 8 ((Z/2)³, char ≠ 2) — ticket K6-GA.

## R6.39 · K6-H2 GRADED — the two-step mechanism is exact and universal on the cells; no independent potential; the residual lemma is isolated
`engine/harvest/k1695_r6_H2/` (codex11, 28 min; eight exhaustive cells, counts identical to K6-H,
`verify.py` re-checks the logs). No void. **Banked after my re-derivation:** for τ = (ab), d = e_a − e_b,
u = Md, N = M P_τ = M − u dᵀ, the Krylov vectors of v under N satisfy x₀ = v, x_{j+1} = M x_j − u·dᵀx_j,
so kd(N, v) = rank[x₀ … x_{n−1}] (exact single-step algorithm); K = Krylov(M, v) is M-invariant; if
dᵀK = 0 then N = M on K (kd unchanged, K_N = K); if d ∈ K then N K ⊆ K (kd ≤ k); otherwise ("generic")
the new Krylov space leaves K at the first index ℓ with dᵀM^ℓ v ≠ 0. Jump range per step is
[1 − k, n − k], sharp (permutation matrices attain ±(n−1)). **Census facts (all eight cells):** at
every local maximum (i) some generic step is NEUTRAL, (ii) every generic neutral step gives
dim(K ∩ K_N) = k − 1, (iii) every generic neutral step is escapable (an ascending second step exists)
— whereas 1 881 600 same-K neutral edges in GL(5,2) are not escapable, so the mechanism is
specifically the generic one. Also: K is NOT always a sum of complete primary components (e.g.
384/768 in GL(4,2)). **Refined potentials:** (kd, c), (kd, s), (kd, r) all leave traps; the only
trap-free one, (kd, h) with h = one-step lookahead, is H2 itself. **Exact residual lemma (unproved):**
if k < n and no transposition ascends, then some d = e_a − e_b has d ∉ K, dᵀK ≠ 0, kd(M − Mddᵀ, v) = k,
and a further transposition ascends. Status: (H2) is an empirically universal mechanism with an
isolated obstruction; not a proof. Next: mine the STRUCTURE of local maxima for an invariant
(normal forms under the symmetries) — ticket K6-H3.

## R6.40 · K6-LEAN7 GRADED — the stratum-(b) nullity lemma is kernel-checked; LEAN6's gap closed; rank form nearly assembled
`lean/proofenv/K1695/RankCriterion.lean` (285 lines, 0 sorry, 11 theorems). Re-run HERE: exit 0,
every `#print axioms` exactly [propext, Classical.choice, Quot.sound]
(`logs/k1695/round6_lean7_recheck.log`); K6-LEAN6's `StratumB.lean` also re-run here: clean
(`round6_lean6_recheck.log`) — §R6.34's PENDING resolved. Statements read in source:
- `stratumB_root_shift_rank_eq_two`: A over F (4×4), `minpoly F A = m`, m irreducible of natDegree 2,
  L ANY field extension, μ ∈ L a root of m ⟹ `rank(A_L − μ•1) = 2`. **No separability, nullity or
  non-base-field hypothesis** — the uniform 2×2-minor argument of §R6.40's ticket
  (`rank_two_le_map_sub_quadratic_scalar` gives ≥ 2 for any non-base-field μ satisfying a quadratic
  relation; `quadratic_conjugate_shift_mul_eq_zero` + `rank_add_rank_le_card_of_mul_eq_zero` give ≤ 2).
- `quadratic_nonroot_shift_rank_eq_four` and `quadratic_nonroot_transposition_rank_ge_three`: for μ
  NOT a root of the quadratic annihilator, `rank(A_L − μ) = 4` and `rank(A_L·swap(a,b) − μ) ≥ 3`
  (the nonroot case, via (A − μ)(A − (t − μ)) = c·1, c ≠ 0, and `l4_t0`).
- `stratumB_rank_at_root_of_simple_extension`: LEAN6's root theorem with the nullity hypothesis
  DISCHARGED — `rank(A_L·swap(a,b) − μ) = 3` at every root μ, still under LEAN6's simple-extension
  hypotheses (μ integral, `Algebra.adjoin F {μ} = ⊤`, natDegree (minpoly F μ) = 2).
- `minpoly_eq_charpoly_of_natDegree_eq` (natDegree minpoly = n ⟹ minpoly = charpoly); the bridge R1
  ("∀ μ in an algebraic closure rank(M_L − μ) ≥ n − 1 ⟹ minpoly = charpoly") NOT proved.
⟹ In Lean, for L = F(μ) (μ a root of m): `rank(A_L·P_τ − μ) ≥ 3` for EVERY μ ∈ L (roots: = 3;
nonroots: ≥ 3) — i.e. the rank form of the stratum-(b) theorem over the quadratic extension, modulo the
one-line assembly (ticket K6-LEAN8) and the open bridge R1 to the minpoly statement. BANKED as listed.

## R6.41 · PRE-REGISTRATION (before reading) — K6-N4k (msolve on the rank-1 systems), K6-N4n, K6-GA, K6-H3, K6-LEAN8, K6-T4
K6-N4k: a basis [1] for BOTH systems 𝒰_S, 𝒰_Q (with the stated Rabinowitsch generators) in a
characteristic banks "rank-1 stratum (a) at n = 4 holds in that characteristic" only after (i) my own
re-run of at least one printed ideal with an independent parser (msolve and/or sympy), and (ii) a check
that the ideals encode exactly the N4h fixed-row family with v_i normalised and c ≠ 0; an integer
Nullstellensatz certificate banks "all characteristics not dividing N" only after I expand
Σ g_k f_k = N exactly myself. A non-[1] basis is a candidate family, not a counterexample, until a
concrete (u, v) is produced and fails T_test / all 24 permutations. Others: as in §R6.22/§R6.15
(Lean rebuild + statement read; GA counterexample protocol; N4n/H3 normal forms re-verified).

## R6.42 · ⭐ K6-N4k GRADED — RANK-1 STRATUM (a) AT n = 4 IS PROVED in characteristic 0 and in characteristics 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 (certificates reproduced here)
`engine/harvest/k1695_r6_n4k/` (codex9, msolve 0.10.1 built into ~/.local by K6-T4). Ideals: variables
a,b,c,y₁,y₂,y₃,z,t,r; generators = the 15 nonzero F2 determinants D_{0,j,τ} of the fixed-row family
R = [x, e₁+y₁x, e₂+y₂x, e₃+y₃x] (x = (a,b,c), the deleted row i normalised to v_i = 1), the split
generator S = a+b+c (resp. Q), the invertibility generator 1 − t(1 + z + ay₁ + by₂ + cy₃) (z = v_i u_i,
a free variable since R does not determine it), and a chart generator (1 − ra; or a, 1 − rb; or a, b,
1 − rc) covering x ≠ 0; x = 0 handled by hand (R = [0|I₃]: j = 1, order (2,3,0) gives det = 1).
**Engine result:** all 72 = 2 systems × 3 charts × 12 characteristics are the unit ideal, 0.26–0.30 s each.
**My verification (all logged under logs/k1695/round6_n4k_*):** (i) msolve re-run by me on six printed
ideals (S/a p2, S/c p3, Q/a p0, Q/b p7, Q/c p31, S/b p11): `[1]` each; (ii) the ideal contents: I
regenerated the 18 determinants from the definition with sympy — 15 nonzero, and all 15 appear in the
file up to sign; the only other generators are S, the invertibility and chart generators
(`round6_n4k_check.py`); (iii) second engine: sympy grevlex on S/a over GF(2) → `[1]` (273 s);
(iv) controls that can fail: a 3-determinant sub-ideal → 194-element non-unit basis; the toy
non-unit ideal → not `[1]`. **Bonus, found here:** the PURE 15-determinant ideal — no S, no
invertibility, no chart — is already `[1]` over ℚ, GF(2) and GF(3). So the theorem is simpler and
stronger than N4k stated: *for every field of those characteristics and every x, y ∈ F³ (x = 0
included), one of the 15 F2 determinants is nonzero* — the F1 column and the S/Q split are never
needed, and the "least i with v_i ≠ 0" rule is proved.
**Certified statement (per characteristic 0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):** for every field F
of that characteristic and every invertible A = I + uvᵀ ∈ GL(4,F), for any i with v_i ≠ 0 some σ ∈ S₄
makes e_i a Krylov-cyclic vector of A P_σ; hence A P_σ is cyclic; hence **Kourovka 16.95 holds for
every rank-one A at n = 4 in those characteristics** (deflation = Lean `cyclic_standardBasis_of_principalBlock`;
Krylov-cyclic ⟹ minpoly = charpoly = Lean `minpoly_eq_charpoly_of_krylov_linearIndependent`).
**NOT yet:** the remaining characteristics (p ≥ 37): needs an integer Nullstellensatz certificate
(N4k's Macaulay search reached degree 9 without one) — or a hand proof of the 15-determinant statement,
which the pure-ideal finding makes more plausible. Blind re-verification ticket K6-N4x dispatched.
n = 4 status: stratum (b) closed (all fields); stratum (a) rank 1 closed in 12 characteristics;
stratum (a) rank 2 open (msolve capped on the 14-variable charts).

## R6.43 · ⚠ codex quota EXHAUSTED (08:3x, "try again Sep 3") — engine layer closed; consequences
Screens 3 (N4z), 4 (LEAN8), 8 (T4), 9 (N4x blind cross-check), 10 (N4n) stopped mid-ticket. So:
the blind cross-check of the rank-1 certificates did NOT run; N4z (ℤ-Gröbner) did not run; LEAN8 no
harvest; N4n and T4 left partial outputs (read below). From here the line runs on its own compute
(light, local) and on web engines via dialogue. The rank-1 result's cross-check is therefore done by
ME with an independent re-encoding (§R6.47) — same family as the original grader, which VERIFY_CHECKLIST
B.7 counts as "same-family found nothing", not "verified"; recorded as such.

## R6.44 · K6-GA GRADED — group-algebra families at n = 6, 8: benign in every exhaustively completed cell
`engine/harvest/k1695_r6_GA/` (codex5, C, exact, two oracles, 230 000 cross-checks 0 mismatches).
20 exhaustive cells: n = 6 (Z₆, S₃) over GF(2,3,5,7); n = 8 ((Z/2)³ over GF(3,5,7); Z₈, Z₄×Z₂, D₄ over
GF(3,5); Q₈ over GF(3,5,7)) — up to 5.76M members, translation-by-automorphism orbits — **all-fail
count 0 everywhere**; the minimising members are exactly the monomial ones f = c·δ_h (good σ = (n−1)!
= 120 / 5 040), no other member ties. Three GF(7) order-8 cells (Z₈, Z₄×Z₂, D₄) UNRESOLVED-due-to-load
(their observed 0 failures withheld as non-evidence, per the rule). Fourier data f̂(χ) = c·χ(h) for
the hard members; a good σ lies in the regular copy of G iff G has an element of order n. ⟹ the
elementary-abelian family is NOT a hard family at n = 8 in odd characteristic (my analogy with the
aI+bJ char-2 obstruction does not transfer); no counterexample candidate from this hunt.

## R6.45 · ⭐ K6-H3 GRADED — a NON-tautological potential with no local maxima on every cell: Φ′ = (kd, −ν)
`engine/harvest/k1695_r6_H3/` (codex11; verify.py; counts identical to H2). Part A: symmetry orbits of
local maxima (90 / 360 / 16 / 1 592 / 760 in GL(3,4), GL(3,5), GL(4,2), GL(4,3), GL(5,2)); support
normal forms are NOT uniform ((axes, supp) = (1,3), (1,4), (2,5), (1,5), (4,4) occur); K may or may
not be a full primary summand. Exact neutral predicates: same-K neutral ⟺ kd unchanged ∧ (d ∈ K ∨
dᵀK = 0); generic neutral ⟺ kd unchanged ∧ d ∉ K ∧ dᵀK ≠ 0; no "one endpoint in a coordinate set"
rule survives GL(4,3)/GL(5,2). Part B (banked after my re-derivation of the left-eigenvector
equation yᵀ((M − μ) + μddᵀ) = 0 and PBH): in the layer kd = n − 1, K = ker ψ (ψᵀM = λψᵀ, ψ_i = 0), and
the transposition (ab) ascends ⟺ Res(χ_N^out, p_ab) ≠ 0 with p_ab(μ) = dᵀadj(M − μ)e_i (roots outside
spec M) AND gcd(b_{N,i}, χ_M) = 1 with b_{N,i} = gcd(χ_N, components of adj(xI − N)e_i) (roots inside
spec M); checked on 15.5×10⁹ directed pairs in GL(4,2)/GL(4,3)/GL(5,2), 0 disagreements, both
negative controls fire; χ_N = χ_M + dᵀadj(xI − M)Md (rank-one identity). Top-layer residual lemma
NOT proved (a generic pair can DROP kd — GL(4,3) has such pairs — so "some b avoids a drop" cannot be
argued pair-by-pair). **Part C, the finding:** Φ = (kd, #distinct neighbouring Krylov spaces) fails,
but **Φ′ = (kd, −ν), ν = number of neutral transpositions, has ZERO suboptimal local maxima in all
eight cells** (GL(3,q≤7), GL(4,2), GL(4,3), GL(5,2)). Unlike H2's lookahead this is a genuine,
computable, non-tautological potential: the conjecture **"every kd-local maximum has a neutral
neighbour with strictly fewer neutral transpositions"** would make Φ′ a bounded strict potential and
PROVE (S′), hence 16.95, for all n and all fields. This is now the sharpest general-n target of the
campaign. Status: conjecture with exhaustive support; the monotonicity theorem is open.

## R6.46 · K6-T4 (partial, quota cut) — (T_3) Case A COMPLETE in characteristic 0, 2, 3, 5, 7; Case B capped
`engine/harvest/k1695_r6_T4/{ideals, logs}` (no REPORT). Toolchain built into ~/.local (m4, autoconf,
automake, libtool, GMP, MPFR, FLINT, msolve 0.10.1 — build logs retained). Case A, cofactor support 3,
split into three sub-charts w1/w2/w3: msolve basis `[1]` over ℚ, GF(2) (retry), GF(3), GF(5), GF(7)
(15 logs; times 0.27 s … 624 s / 4 GB). **My re-run:** caseA3_w1_p3 → `[1]` in 0.02 s (caseA3_w3_p7
aborted at my 10-min tool timeout — not evidence either way). Together with K6-T3 (supports 1, 2):
**(T_3) Case A (some κ_j = 0) holds over every field of characteristic 0, 2, 3, 5, 7** (supports 1–2
also for the primes up to 31). Case B (all κ_j ≠ 0): the six-cubic sub-family (j = 4), the 12- and
18-cubic families and all 24 — capped at 2400 s / 7.4 GB over GF(2) — OPEN. Note Case B is exactly
"the four columns are in general position"; the hard core.

## R6.47 · ⭐ RANK 1 AT n = 4: certified in characteristic 0 and in EVERY prime characteristic p < 10 000, by my own encoding
`problems/k1695/round6_rank1_certify.py`, `logs/k1695/round6_rank1_certify.log` (143 s). Independent
of N4k's files: the 24 determinants D_{j,τ} (j = 0..3) generated from the definition (17 nonzero;
j = 0 gives ±S·Q), variable order (y₃,y₂,y₁,c,b,a), no invertibility/chart/split generators. msolve:
`[1]` over ℚ; `[1]` over GF(p) for ALL 1 229 primes p < 10⁴ (coefficients reduced mod p here). Controls:
a 3-determinant sub-ideal → non-unit (6 003-char basis); the toy ⟨xy, 1 − tx⟩ → non-unit; (the
"wrong family" R′ = [x, e₁+y₁x, e₂+y₂x, e₃] also turned out to be unit — a true statement about a
different family, so not a failing control; the other two are). Second engine: sympy (§R6.42).
**Certified statement:** for every field F of characteristic 0 or p < 10 000 and all x, y ∈ F³, one of
the 17 determinants is nonzero; hence for every A = I + uvᵀ ∈ GL(4,F) and every i with v_i ≠ 0 some
σ makes e_i Krylov-cyclic for A P_σ (deflation, Lean-checked), hence A P_σ is cyclic (Lean-checked):
**Kourovka 16.95 for every rank-one A at n = 4 in those characteristics.** Same-family self-check
(VERIFY_CHECKLIST B.7: "same family found nothing"); the blind codex cross-check never ran (quota).
Remaining for all fields: an integer certificate (ℤ-Gröbner via Singular, or modular Macaulay).
**K6-N4n (partial, quota cut):** shape-0 conjunct systems (392): unit in char 2 for all 392; in
characteristics 0, 5, 7, 11, 13: 373 unit / 19 non-unit; char 3: 389 / 3 — the non-unit ones are the
odd-characteristic all-six-fail families (cf. §R6.37); their rescue is unproved. Rank 2 at n = 4: OPEN.

## R6.48 · Toward EVERY characteristic for rank 1 at n = 4 — Singular jobs (in flight)
Found at 08:4x: codex3 had built Singular into ~/.local before the quota cut and launched
`std(I)` over `integer` for the 15-determinant ideal (`engine/harvest/k1695_r6_n4z/inputs/ideal_Z.sing`,
watchdog cap 2400 s / 8 GB; toy control ⟨x² − 2, x − 3⟩ → constant 7 ✓). If it finishes, the constant
of the strong ℤ-basis is N with I_ℤ ∩ ℤ = (N): the bad primes are exactly the primes dividing N.
My parallel route (`engine/harvest/k1695_r6_n4z/lift/lift_Q.sing`, same caps): over ℚ, `lift(I, 1)`
gives cofactors g_k with 1 = Σ g_k f_k; D := lcm of their denominators satisfies D ∈ I_ℤ, so every bad
prime divides D; msolve over GF(p) for each p | D then certifies every remaining characteristic. Either
result, once re-verified by me (expand Σ (D g_k) f_k = D exactly in sympy; msolve per prime factor),
upgrades §R6.47 to "every field". Status: both running (2 heavy processes; load ≈ 4.5).
Free-tier brief K6-PHI written (`engine/briefs/k1695_r6_phi/BRIEF.md`): prove/break (Mono) for Φ′.

## R6.49 · OWNER DIRECTIVE (09:1x, via dialogue): widen the search — brief K6-WIDE written
The owner suspects our briefs constrain the search space (the three refutations of 08-29 — F1
transposition-only, F2 char-2 forcing, F4 (Z/2)³ hard family — were all narrow-hypothesis failures).
`engine/briefs/k1695_r6_wide/BRIEF.md`: the full problem, proved facts P1–P11, refuted hypotheses
F1–F8 with their refuting objects, methods used, and an open question (assumptions to drop; outside
machinery; three orthogonal directions with a first lemma each; literature with exact citations).
To run on Pro (depth) and Qwen3.8-Max (speed) via dialogue. Acceptance: literature resolved by me
(Crossref/arXiv) before registry entry; directions tested on n = 4, 5 small-field data first.
(Memory: feedback-widen-search-space.md now records the principle: widen the GENERATION side —
wide briefs + control tickets — while the acceptance red lines stay fixed.)

## R6.50 · Φ′ = (kd, −ν) monotonicity (Mono) — INDEPENDENTLY CONFIRMED on GL(3,4), GL(4,2) with my own code; Singular status
`problems/k1695/round6_phi_probe.py`, `logs/k1695/round6_phi_probe.log` (own kd/ν code, scanning
every B ∈ GL(n,q) — every (A,σ) pair is some B): GL(3,4): 864 kd-local maxima (B,i), all with
ν = 3 (all three transpositions neutral) and a neutral neighbour with ν′ = 1 (the only neutral move
from there is the way back; the other two transpositions ascend) — 0 violations; GL(4,2): 32 local
maxima, all ν = 6 → some neutral neighbour with ν′ = 2 — 0 violations. Counts coincide with K6-H3's
quotient tables (864 / 32). GL(3,5) running (20-min cap). Observation: in these cells every local
maximum is "totally flat" (every transposition neutral), and the successful neutral step lands on a
state where almost every transposition ascends. At n = 3 this is forced by (T_2): at a local
maximum the identity and the three transpositions fail, so the two 3-cycles (distance 2) must work.
Singular: the ℤ-`std` died at the 2400 s cap (UNRESOLVED-by-cap, `logs/ideal_Z.log`); RELAUNCHED at
09:2x with a 3 h wall cap and the same 8 GB memory cap (`relaunch/ideal_Z_3h.log`,
`scripts/run_capped_3h.py` = the watchdog with WALL_SECONDS = 10800). The ℚ-`lift` run hits its
2400 s cap at ~09:27; next attempt `liftstd` (std + cofactors in one pass), 20-min cap.
**Addendum to §R6.50 (09:4x):** GL(3,5) also confirmed with my code — 2 400 kd-local maxima, all ν = 3 with
a neutral neighbour of ν′ = 1, 0 violations of (Mono) (151 s). So (Mono) stands independently verified
on GL(3,4), GL(3,5), GL(4,2) (my code) and on GL(3,2..7), GL(4,2), GL(4,3), GL(5,2) (K6-H3). In GL(4,3)
and GL(5,2) local maxima are NOT totally flat (ν ∈ {3..6}, {5..9}), so the "all transpositions neutral"
picture is a small-cell artefact; the drop of ν is the robust fact. `liftstd` over ℚ launched
(20-min cap) as the second route to the integer N.

## R6.51 · K6-WIDE (Qwen3.8-Max) GRADED — honest, useful; direction B1 tested and NOT small; B2 launched
`engine/harvest/k1695_r6_wide_qwen.md` (24 KB; declares no web use for solving; claims no result decides
16.95). **Assumptions it says to drop:** one-transposition-at-a-time (our F1 already forced this);
stratification by nullity/conjugacy type (true symmetry = simultaneous permutation conjugation only —
correct, and it is why (S′)/(T_m), which are unstratified, are our live targets); "cyclic vector = a
standard basis vector" (it suggests small finite test sets instead — note (S′) with e_i has held on
every scanned cell, so we keep it but the remark is fair); "P modifies A" → base change between two
ordered bases (Bruhat/flag/matroid language); finite fields only as search (use Lang–Weil / Ax-type
transfer as proof tools); union bounds (agreed, F6e). **Machinery:** regular elements of algebraic
groups (cyclic = regular; the problem is "GL_n = GL_n^reg · S_n"), determinantal varieties and
intersection theory, non-abelian Fourier analysis on S_n, control/matroid circuits, Birkhoff
polytope/Hall, finite-field counting, pencils. **Directions:** A (Fourier/SOS: Φ(A) = Σ_{i,σ}K_{i,σ}(A)²
> 0 over ℝ; the (3,1)-coefficient conjecture A2), B (global: hitting sets B1; the (S′)-ideal saturated
by det being unit, B2), C (circuit/tropical reformulation of (T_m); C1 = the Case-B unit-ideal
statement we already have as the open piece of (T_3); C2 a tropical matching lemma).
**Tested here (`round6_hitting.py`, `logs/k1695/round6_hitting.log`):** exact minimum universal
hitting sets W₀ ⊂ S_n: GL(3,q), q ∈ {2,3,4,5}: min |W₀| = 4 of 6 in every cell (the good sets of the
monomial 3-cycles have size 2 and vary), n-cycles alone never suffice; GL(4,2): min |W₀| = 8 of 24 and
W₀ must contain all five cycle types; a 30 000-sample of GL(4,3) gives 3 but is not exhaustive (the
sample misses the rare hard members). ⟹ **B1 in its "small witness set" form is refuted**: the needed
fraction of S_n is large (2/3 at n = 3, 1/3 at n = 4 over GF(2)); hitting sets do not simplify the
problem. **B2 launched** (`round6_sprime4_ideal.py`): the ideal of all 96 Krylov determinants
K_{i,σ}(A) in the 16 entries of A plus 1 − t·det A, over GF(2) first, msolve, 30-min cap — a unit ideal
would prove (S′)₄, hence 16.95 at n = 4, in that characteristic with NO stratification.
**Citations:** Steinberg 1965 (IHES 25) resolved via OpenAlex; Lang–Weil 1954, Ax 1968, Alon 1999,
Gerstenhaber 1961, Fulton 1984, Kalman 1963, Birkhoff 1946 are canonical (OpenAlex title search was
noisy for two of them; none is load-bearing). No literature claim about 16.95 itself was made.

## R6.52 · ℤ-std relaunch KILLED EXTERNALLY at 38.7 min (3.5 GB) — machine memory, not the watchdog; local Gröbner ceiling reached
`engine/harvest/k1695_r6_n4z/relaunch/ideal_Z_3h.log`: `EXIT code=-9 seconds=2324.86 peak_rss_kib=3476336`.
The watchdog (`scripts/run_capped_3h.py`, WALL 10800 s, MEMORY 8 000 000 KiB) is exonerated by its own
code path: it writes `UNRESOLVED cap=…` when *it* kills; `EXIT code=-9` is the branch where the child
died on its own — a SIGKILL from outside. System state at 10:1x: swap 11.4 GB of 12.3 GB used, free
pages ≈ 64 MB, a 1-GB resident `~/.balloon/bin/balloon daemon` (not ours), the B2 msolve at 3.3 GB and
climbing. The kill is consistent with macOS memory exhaustion (largest process killed when swap runs
out); the 8-GB ticket cap is above what this machine can actually supply right now. **Consequences:**
(i) the ℤ-std (all-characteristic certificate for rank 1 at n = 4, §R6.47) needs > 3.5 GB and > 40 min
— UNRESOLVED-due-to-load, not evidence; not relaunched while B2 runs (load rule); (ii) the (S′)₄ ideal
over GF(2) (§R6.51 B2) is at the same wall — if it is killed or capped, that too is load, not evidence;
(iii) these Gröbner jobs are the first genuinely resource-bound items on the line; the right venue is
the GCP budget (`automath-gcp`: owner confirmation required before any use) or a lighter encoding
(exploit permutation-conjugation symmetry / scaling to cut variables before any relaunch).

## R6.53 · GCP run PRE-REGISTERED (in-budget, self-confirmed per the 08-29 rule; dialogue concurs): ℤ-std + (S′)₄ ideals
**Why cloud:** §R6.52 — the local box (swap 11.4/12.3 GB) SIGKILLs any process above ≈3.5 GB; the B2
msolve was stopped by me at 25 min (its log line "NOT unit (0 chars)" is the parse of an empty output
file after the kill — UNRESOLVED, not a verdict). **Machine:** one on-demand `e2-highmem-4` (4 vCPU,
32 GB) `k1695-r6-groebner`, us-central1-a, Ubuntu 24.04, project [gcp-project]. **Worst-case
cost:** ≈$0.18/h × 3 h 05 min ≈ $0.56 + 20-GB disk ≈ $0.01 + bucket ≈ $0 → **< $1**, far under the $20
alarm and the ≈$90 credit. **Caps inside the runner** (`engine/gcp/k1695_r6_groebner_startup.sh`):
3-h wall for everything with per-job trimming, absolute TTL poweroff at 3 h 05, per-job systemd
MemoryMax 13 GiB (≤ 26 GiB < 28 GiB), outputs synced to gs://[gcp-project]/k1695_r6/out/
after every job, poweroff at DONE, instance deleted at harvest. **Jobs:** A = Singular `std` over ℤ of
the rank-1 ideal (`engine/harvest/k1695_r6_n4z/inputs/ideal_Z.sing`, single-threaded, cap 10 200 s);
B = msolve `-g 2 -t 3` of the (S′)₄ ideal (97 generators, 17 variables) over GF(2), GF(3), GF(5), GF(7)
sequentially (cap 5 400 s each, trimmed). **Pre-registered readings:** A: `K6N4Z_CONSTANT_BEGIN N` →
I factor N and re-certify each p | N with msolve locally (light) before upgrading §R6.47 to "every
field"; no constant → the ideal over ℤ is not unit (rank 1 fails in some characteristic — then find the
prime and the point); B: `[1]` over GF(p) → (S′)₄ over every field of characteristic p → **16.95 at n = 4
in characteristic p**, to be re-run once by me from the same .ms file before entry; non-unit → extract a
point and test all 24 permutations by hand (a genuine 16.95 counterexample would have to pass the
disclosure protocol); killed/capped → UNRESOLVED-due-to-load. Launch command path:
`engine/gcp/k1695_r6_launch.sh` (uploads inputs, creates the VM). Launched by me; harvest at the next
wake-ups; the runner's own log lands at .../out/runner.log.

## R6.54 · REDUCTION LEMMA: (S′) ⟺ (S′₀) (start vector e₀ only), and a₀₀ = 1 WLOG — quarter-size (S′)₄ ideal; local capped probe pre-registered
**Lemma.** For π, σ ∈ S_n: P_π A P_σ = P_π (A P_{σπ}) P_π⁻¹ (check: P_π A P_{σπ} P_π⁻¹ = P_π A P_σ P_π P_π⁻¹).
Hence e_i is Krylov-cyclic for P_π A P_σ ⟺ P_π⁻¹e_i = e_{π⁻¹(i)} is Krylov-cyclic for A P_{σπ}
(conjugation carries Krylov spaces to Krylov spaces). So "(S′) at every index for every invertible A"
⟺ "(S′₀): for every invertible A some σ makes e₀ Krylov-cyclic for AP_σ" (apply (S′₀) to P_πA with
π⁻¹(0) = i). Further, cyclicity is invariant under A ↦ λA (Krylov determinants scale by λ^{n(n−1)/2}) and
the family {AP_σ} under A ↦ AP_ρ; since some a_{0j} ≠ 0, a₀₀ = 1 WLOG. **Consequence:** the (S′)₄ ideal
of §R6.51 (96 sextics, 16 variables + t) is equivalent, as a theorem, to the ideal of the 24
determinants K_{0,σ}|_{a₀₀=1} in 15 variables + t (`round6_sprime4_reduced.py`, files sprime4r_p{p}.ms).
Unit over GF(p) ⟺ 16.95 at n = 4 in characteristic p. **Pre-registered local probe** (box swap now
47 %): msolve `-g 2`, GF(2), own watchdog `run_capped.py` wall 900 s / resident 2.5 GB
(log `logs/k1695/round6_sprime4r_p2.log`). Readings: `[1]` → re-run once, then §R6.55 banks
characteristic 2 at n = 4 (the first unstratified n = 4 result); non-unit → a point, tested by hand
against all 24 permutations; capped → UNRESOLVED-due-to-load, the file goes to the VM runner.
**§R6.54 probe result (10:24):** msolve F4 on the reduced ideal over GF(2) hit the 2.5-GB resident cap
after 89 s (`logs/k1695/round6_sprime4r_p2.log`: `UNRESOLVED cap=resident-memory-2500000KiB`) —
UNRESOLVED-due-to-load; F4's dense matrices in 16 variables at degree ≥ 6 exceed what this box may
use. Second pre-registered probe, same caps: Singular Buchberger (`std`, redSB, dp) on the same
generators (`sprime4r_p2.sing`, converted verbatim from the .ms file), which is slower but far
more memory-frugal; readings identical to §R6.54. Both files go to the VM runner if the owner
approves the launch.
**§R6.54 second probe (10:29):** Singular `std` on the same reduced GF(2) ideal also hit the 2.5-GB
resident cap, after 261 s (`logs/k1695/round6_sprime4r_p2_sing.log`) — UNRESOLVED-due-to-load. Both
encodings of (S′)₄ therefore exceed the local box; owner clarification relayed by dialogue (§R6.52
addendum): `~/.balloon/bin/balloon daemon` is the owner's deliberate memory balloon that keeps math
jobs from freezing the machine — never to be killed; the realistic local ceiling is ≈2.5 GB per heavy
job (RAM − balloon − system), anything bigger goes to GCP.

## R6.55 · GCP run LAUNCHED (owner-approved, by dialogue): k1695-r6-groebner RUNNING since 2026-08-29T15:27:10Z (10:27 CDT)
My session's classifier denied both the create and the upload (§R6.53); dialogue refused to run them
on my behalf (permission-boundary rule), put a one-line decision to the owner, and launched after the
owner's approval via `engine/gcp/k1695_r6_launch.sh`. Inputs in the bucket are the ORIGINAL
96-determinant files (sprime4_p{2,3,5,7}.ms) plus ideal_Z.sing; the reduced files
(sprime4r_p{p}.ms/.sing, §R6.54) stay local as the input of a possible second run if job B caps at
13 GiB. Hard TTL poweroff ≈18:32 UTC (13:32 CDT). Harvest = read gs://[gcp-project]/
k1695_r6/out/ (runner.log, zstd.out/.status, sprime4_p*.gb/.status); delete at harvest (dialogue if my
classifier blocks the delete). Readings as pre-registered in §R6.53.
**§R6.55 status 10:42 CDT (serial console):** RUNNER START 15:27:26Z; TOOLS Singular 4.3.2 (distribution)
+ msolve built from the 0.10.1 source at /usr/local/bin; MEMORY-SCOPE systemd-run available (13 GiB
scopes active); both jobs started 15:29:56Z (zstd cap 10 200 s → ends by 18:20Z = 13:20 CDT;
sprime4_p2 cap 5 400 s → by 17:00Z = 12:00 CDT). The bucket receives outputs only when a job ends.

## R6.57 · Owner pre-clearance (10:5x, via dialogue) + RUN-2 contingency PREPARED (not launched)
Owner: "预先授权你直接同意" — GCP launches that my session's classifier blocks are run by dialogue
without further asking, provided in-budget and under the standard caps (hard TTL, memory cap, runner
by path, poweroff at DONE, delete at harvest); same for deletes. **Prepared now, by path, launched only
if job B of run 1 caps at 13 GiB:** `engine/gcp/k1695_r6_groebner2_startup.sh` (reduced inputs
sprime4r_p{2,3,5,7}.ms of §R6.54, sequential, msolve -t 4 with a 26 GiB scope, or 13 GiB + the ℤ-std
again when metadata run_zstd=1; same 3-h/TTL/sync/poweroff terms) and `engine/gcp/k1695_r6_launch2.sh`
(uploads to gs://…/k1695_r6b/inputs/, creates on-demand e2-highmem-4 `k1695-r6-groebner2`).
Worst case < $1 again. Trigger and readings: §R6.53.

## R6.58 · RUN 1 RESULT: both jobs OOM-killed at the 13 GiB scope — UNRESOLVED-due-to-load; contingency LAUNCH2 triggered
Harvest in `engine/harvest/k1695_r6_gcp/` (bucket outputs + `serial.log`). Kernel memcg log: msolve
(96-determinant (S′)₄ ideal, GF(2), `-t 3`) killed at 1528 s with anon-rss 13.60 GB; Singular ℤ-std of
the rank-1 ideal killed at 2071 s with anon-rss 13.60 GB; systemd's OOMPolicy=stop then SIGTERMed the
scopes (rc=143, "Terminated"). Both are load verdicts, not mathematics. VM 1 continued into sprime4_p3
with the same encoding and cap (doomed); VM 1 is harvested and deleted (below). **Run 2 (§R6.57
scripts, revised):** (B′) msolve on the REDUCED ideal (§R6.54: 24 determinants, 16 variables) over
GF(2), then 3, 5, 7, `-t 3 -m 3000 -u 5` (bounded pairs per matrix, periodic hash-table reset — memory
knobs, no effect on correctness), 18 GiB scope; (A′) instead of the ℤ-std, Singular `lift(I, ideal(1))`
over ℚ on the rank-1 ideal (`engine/harvest/k1695_r6_n4z/lift/lift_Q_vm.sing`, output path moved to
the VM), 8 GiB scope, cap 9 000 s: a cofactor certificate 1 = Σ hᵢgᵢ with rational hᵢ proves the unit
ideal in every characteristic not dividing the common denominator D, and the primes p | D are then
checked one by one with msolve over GF(p) (finite list) — cleaner than the ℤ-std. Readings: cofactors
→ I recompute D, verify Σ hᵢgᵢ = 1 myself with sympy (light), check p | D with msolve, then §R6.59
upgrades §R6.47 to every field; msolve `[1]` → 16.95 at n = 4 in characteristic p (VM certificate,
not locally reproducible — stated as such); OOM/cap again → UNRESOLVED, and the (S′)₄ ideal is
declared out of reach for msolve at this size (next: theory, not bigger machines).
**§R6.58 run 2 LAUNCHED** by dialogue (owner pre-authorised, scripts re-read): `k1695-r6-groebner2`
RUNNING since 2026-08-29T16:05:38Z (11:05 CDT); inputs gs://…/k1695_r6b/inputs/ (lift_Q_vm.sing,
sprime4r_p{2,3,5,7}.ms, ideal_Z.sing unused with run_zstd=0); outputs gs://…/k1695_r6b/out/; TTL
poweroff ≈19:10Z (14:10 CDT). Harvest + delete by me at the wake-ups.
**§R6.58 run-2 status 11:25 CDT:** RUNNER2 START 16:06:04Z; tools as in run 1; both jobs started
16:08:05Z (liftQ 8 GiB cap 9 000 s; sprime4r_p2 18 GiB `-t 3 -m 3000 -u 5` cap 9 000 s); no OOM and no
END marker at 17 min. Verifier for the lift certificate written meanwhile
(`problems/k1695/round6_verify_cofactors.py`: parses the Singular generators and the written
cofactor matrix, checks Σ hᵢgᵢ = 1 exactly in sympy, reports D and its prime factors); positive and
negative controls below.
**§R6.58 control finding (11:3x CDT):** the verifier's positive control exposed a defect in the lift
scripts: Singular's `write(":w f", T)` on a matrix writes only T[1,1], so `lift_Q_vm.sing` on the VM
will deliver "lift succeeded" plus timing but NO usable certificate (my copy error from the older
lift_Q.sing; the msolve job is unaffected). Fixed script `lift_Q_fix.sing` writes every entry
(`string(T[i,1]) + ","`); controls on a toy unit ideal: VERIFIED with D = 3 (and the toy ideal is
indeed non-unit mod 3 — the D-primes are genuinely the ones to check), tampered file FAILED.
**Corrected lift launched LOCALLY** (time-bound, ~1.2 GB at 40 min earlier; within the 2.5 GB ceiling):
`run_capped.py --wall 10800 --mem 2500000`, log `logs/k1695/round6_liftQ_fix.log`, output
`engine/harvest/k1695_r6_n4z/lift/cofactors.txt`. Readings: `K6N4Z_LIFT_DONE` → run
`round6_verify_cofactors.py lift_Q_fix.sing cofactors.txt`; VERIFIED with D → check each p | D by
msolve over GF(p) (the rank-1 ideal, light) → §R6.59 "rank 1 at n = 4 over every field"; capped →
UNRESOLVED (the VM's K6N4Z_LIFT_SECONDS then tells whether a longer local wall would suffice).

## R6.61 · OWNER RULE (11:1x, via dialogue): cloud solver jobs get NO wall/TTL caps — daily go/no-go review; RUN 3 written by path
Owner's intent verbatim (relayed): "3 hours is far too short — check once every 24 hours; no forced
hard caps; the only limit is the GCP credit + free tier." Standing rule from now: no wall caps, no
per-job timeouts on cloud solver jobs; orphan backstop only (auto-poweroff after a few days + a
staleness alert), daily review by the line (continue if progressing or likely close), memory scope =
the machine. **Run 3 (`engine/gcp/k1695_r6_groebner3_startup.sh`, `engine/gcp/k1695_r6_launch3.sh`):**
same jobs as run 2 — (B) msolve on the REDUCED (S′)₄ ideal over GF(2), 3, 5, 7 sequentially, `-v 2`
(per-round progress in the .err files), all vCPUs, scope = MemTotal − 8 GiB; (A) Singular `lift`
over ℚ with the FIXED entry-by-entry write (`lift_Q_vm2.sing`), 6 GiB, then optionally the ℤ-std —
no `timeout`, no WALL; heartbeat every 10 min (elapsed, per-job RSS, memory, disk) synced to the
bucket with all outputs; poweroff at DONE; orphan backstop poweroff after 5 days (metadata
`backstop_days`; chosen below 7 so that the worst case stays inside the credit). **Machine:** preferred
e2-highmem-8 (8 vCPU, 64 GB, ≈$0.36/h → ≈$8.6/day, 5-day worst case ≈$43); fallback e2-highmem-4
(32 GB, ≈$4.3/day, ≈$22 worst case) if the CPU quota (32/32 now) cannot free 8 vCPUs. **Run 2:** to be
deleted at run-3 launch — its msolve job is subsumed (same input, bigger scope, no cap); its serial
log is snapshotted in `engine/harvest/k1695_r6_gcp2/serial.log` (at 40 min: both jobs alive, no OOM).
**Daily review protocol:** at ≈11:00 CDT each day read heartbeat.txt + *.err progress (msolve round
count/degree, RSS trend): continue if rounds still advance or memory is stable; stop (harvest, delete)
if a scope OOM or a stall; every review and cost (≈$0.36/h) logged here.
**§R6.61 run 3 LAUNCHED** by dialogue: `k1695-r6-groebner3` (e2-highmem-4, 32 GB — quota 32/32 kept
highmem-8 out until 677's instances end ≈18:40–19:00Z; msolve scope = 24 GiB, `-m 3000 -u 5`)
RUNNING since 2026-08-29T16:31:21Z (11:31 CDT); run 2 deleted. Bucket prefix k1695_r6c; heartbeat
every 10 min; staleness Monitor armed by dialogue; backstop 5 days; ≈$0.18/h ≈ $4.3/day. If the 24 GiB
scope OOMs → relaunch on e2-highmem-8 when a slot opens (dialogue). Daily go/no-go ≈11:00 CDT.

## R6.62 · K6-PHI (Qwen3.8-Max) GRADED: no proof, no counterexample; one misstatement; §2 family VERIFIED (hand + own code) — a new infinite family of local maxima where (Mono) holds
`engine/harvest/k1695_r6_phi_qwen.md`. **§1 Lemma 1** (τ neutral for (M,i) ⟹ τ neutral for (MP_τ,i),
since P_τ² = I) — correct. **Corollary 1 is misstated**: "a counterexample must have ν ≥ 2" is the
inverse of what its own argument shows; the correct reading is "(Mono) can hold at a kd-local maximum
only if ν ≥ 2, so a local maximum with ν ∈ {0, 1} would be an immediate counterexample". The test it
proposes is already answered by my Φ′ data (`round6_phi_probe.log`): every kd-local maximum has ν = 3
(GL(3,4), 864 maxima; GL(3,5), 2400) or ν = 6 (GL(4,2), 32), never ν ≤ 1 — consistent with (Mono), and
a small structural fact worth keeping: **at every scanned local maximum ν ≥ 2** (n = 3: ν = 3 always;
n = 4 over GF(2): ν = 6 always). **§2 family A_Q = Q + J over F₂, n even**: closed under right
multiplication by transpositions (JP_τ = J), invertible ((I+J)² = I); Lemma 2 (kd(A_Q, i) determined
by the length L of the Q-cycle through i: L even < n → L; L odd < n → L+1; L = n → n or n−1 as n ≡ 0,
2 mod 4) — re-derived (v_{2m} = Q^{2m}e_i, v_{2m+1} = Q^{2m+1}e_i + 𝟙, parity-class argument);
Lemma 3 (local maxima below n: C odd, L ≤ n−3, all other cycles fixed points) — re-derived for all
parities of L and S; Lemma 4 (ν = C(m,2) + Lm, m = n−L) and Lemma 5 (type A merge-with-fixed-point:
ν − ν′ = (L+1)(m−1); type B merge-two-fixed-points: ν − ν′ = 2L) — re-derived, including the count
E−1 of adjacent transpositions that split off a singleton ≠ i. **Own-code cross-check**
(`round6_qj_family.py`, `logs/k1695/round6_qj_family.log`): Lemma 2 exact on all (Q, i) for n = 4, 6
and on 1500 random Q at n = 8; all 4 / 126 / 267 local maxima have the Lemma-3 shape, the Lemma-4 ν,
and satisfy (Mono) — 0 violations. **Value:** the first proved infinite family of kd-local maxima
(characteristic 2, every even n) on which (Mono) holds with an explicit ν-descent — a genuine, if
narrow, piece of evidence; it also identifies the general obstacle precisely (**§3**: the
"generic neutral" case ψ_a ≠ ψ_b, ψ ∦ d in the kd = n−1 layer, where the Krylov hyperplane moves and ν
may be compensated) — the same layer as our open (Top-Mono). Not a proof of (Mono); nothing banked
beyond the family theorem (Lean-able later if wanted). Pro pass of K6-PHI still queued.
**§R6.61 run-3 progress 11:53 CDT (heartbeat 16:51:57Z, elapsed 20 min):** msolve F4 on the reduced
(S′)₄ ideal over GF(2): rounds at degree 7 → 11 done (largest matrix so far 117 218 × 1 201 006 at 0.48 %
density, 365 s real / 614 s cpu), ≈33 k pairs still queued at degree 11 with the 3000-pair cap per
matrix; RSS 6.4 GB of the 23 GiB scope; Singular lift 131 MB. Local corrected lift: 26 min, 1.06 GB
(cap 2.5 GB / 3 h). No decision due; next look at the heartbeat in 30 min, daily go/no-go ≈11:00 CDT.
**§R6.61 run-3 progress 12:24 CDT (heartbeat 17:22Z, elapsed 50 min):** msolve still in the degree-11
layer: rounds of 3000 pairs, matrices ≈60–80 k × 380–455 k (3.5–3.8 % density), 700–870 s real each,
queue grown to ≈49.7 k pairs, recent rounds mostly reductions to zero (455 new / 2545 zero); RSS 9.97 GB
(+3.6 GB in 30 min) of the 23 GiB scope. Local lift 57 min, 1.19 GB. No decision due (no-cap regime);
memory trend to be judged at the daily review — if the scope OOMs, relaunch on e2-highmem-8.
**§R6.61 run-3 progress 12:55 CDT (heartbeat 17:52Z, elapsed 80 min):** still degree 11; queue 71.9 k
pairs; last full round 85 766 × 463 830 (4.3 %), 1485 s real; RSS 13.9 GB (+4 GB per 30 min) of the
23 GiB scope — at this slope the scope is exhausted in ≈1–1.5 h unless the periodic hash-table reset
(`-u 5`) releases memory. No-cap rule: continue; OOM → relaunch on e2-highmem-8 (64 GB) when 677's
instances expire (≈13:40–14:00 CDT). Local lift 88 min, 1.16 GB.
**§R6.61 run-3 progress 13:26 CDT (heartbeat 18:22Z, elapsed 111 min):** the degree-11 layer is
finishing — last round selected only its 1 379 remaining pairs (61 new / 1 318 zero; 94 372 × 492 271,
1203 s); queue 72.4 k pairs at degree ≥ 12 next. Memory growth flattened: RSS 14.3 GB (+0.4 GB in 30
min; the `-u 5` hash-table reset evidently released memory) — the earlier OOM forecast is withdrawn
for now; degree 12 will set the new slope. Local lift 119 min, 1.0 GB (cap 14:27).

## R6.63 · K6-WIDE (GPT-5.6 Pro) GRADED: §I reductions correct (re-derived); both finite-evidence claims REPRODUCED; three directions triaged
`engine/harvest/k1695_r6_wide_pro.md` (35 KB). **§I, all re-derived:** (1) two-sided permutations
free: ∃Q,P: QAP cyclic ⟺ ∃P′: AP′ cyclic (Q⁻¹(QAP)Q = A(PQ)) — same mechanism as my §R6.54;
(2) B cyclic ⟺ Ω(B) = I∧B∧…∧B^{n−1} ≠ 0 (linear independence of the powers ⟺ deg minpoly = n);
(3) any fixed-n counterexample specialises to a finite field (f.g. ring ℤ[a_ij, det⁻¹] or F_p[…], maximal
ideal → finite residue field, closed conditions Ω(AP_σ) = 0 survive) and the large-field principle
(non-cyclicity is stable under scalar extension, so "true for all q ≥ Q(n)" ⟹ all finite fields ⟹ all
fields); (4) the non-cyclic locus D_n is irreducible of codimension 3 (image of {rank(B−λI) ≤ n−2} ≅
{rank ≤ n−2} × A¹, dim n²−4+1, finite projection); (5) the fixed-n conjecture over all fields ⟺ the ideal
of all Ω-coordinates of all XP_σ is unit in ℤ[x, det⁻¹] ⟺ det^N ∈ J_n (unit over ℚ and every F_p ⟹ unit
over ℤ by stripping the primes of N ∈ J_n ∩ ℤ) — all correct. **§II** matches our refutations.
**D1 (Coxeter–Hessenberg charts):** cyclic ⟺ conjugate into the unreduced-Hessenberg cell BcB —
correct; S = Q·u·b exists for every S (partial-pivoting LU) so the two-sided reformulation is exact;
(OC_n) "∀A ∃P, u ∈ U⁻: u⁻¹APu ∈ BcB" is a genuine strengthening with n(n−1)/2 flag variables.
**REPRODUCED** (`round6_pro_tests.py`, `logs/k1695/round6_pro_tests.log`): over GF(2), |U⁻| = 64,
512 invertible unreduced Hessenberg matrices, 24 permutations, and the union {uHu⁻¹P⁻¹} has exactly
20 160 elements = GL(4,2) — (OC₄) holds over F₂. **D2 (conormal capture CC_n):** the tangent/conormal
description of the smooth stratum is right and the cone argument (⟨d det_A, A⟩ = n det A ≠ 0 in char
∤ n) is a clean idea, but its "n = 4 test" is NOT a small-field test: an all-bad A does not exist where
16.95 is verified, so (CC₄) can only be tested by proving a polynomial system inconsistent — the same
Gröbner class as the (S′)₄ ideal, with more variables; parked. **D3 (good-count conjecture (GC_n):
g(A) := #{σ : AP_σ cyclic} ≥ (n−1)! for every A ∈ GL_n(F), every F):** sharp at aI (n-cycles only);
every monomial DQ has ≥ (n−1)! good σ (whenever QP is an n-cycle) — correct. **REPRODUCED and
extended** (same script): min g over GL(4,2) = 6 = 3!, attained by exactly 168 matrices (Pro's
number); NEW: the 168 form exactly TWO orbits under A ↦ QAP — the 24 permutation matrices and 144
NON-monomial matrices (orbit representative rows 0001 / 0010 / 0111 / 1011), so "a minimizer is
always monomial" is already false over F₂; min g over GL(3,q) = 2 = 2! for q = 2, 3, 4, 5 (6/12/18/48
minimizers — far fewer than the monomial matrices: DQ with non-scalar D usually has more good σ); a
30 000-sample of GL(4,3) has min 8 (sample misses the rare minimizers). g is invariant under
A ↦ QAP, A ↦ aA, A ↦ Aᵀ. The hook-only Hecke compression (χ_q^λ(T_c) = 0 unless λ is a hook,
= (−1)^r q^{n−1−r}) is consistent with the q = 1 specialisation χ^λ(n-cycle) and is the
representation-theoretic reason the (3,1)-coefficient kept appearing in our group-algebra work; not
re-derived here. **Citations:** 10 of 11 DOIs resolved exactly via Crossref (Steinberg 1965; De
Mari–Procesi–Shayman 1992; Ram 1991; Neumann–Praeger 1995; Wimmer 1974; Thompson 1980; Zaballa 1987;
Rado 1942; Lovász 1980; Alon 1999); Green 1955 (JSTOR DOI, canonical) not in Crossref; Gohberg–
Lancaster–Rodman is a book. "No direct literature theorem" — consistent with our own searches.
**Verdict:** the strongest wide answer so far; (GC_n) and (OC_n) are the two concrete strengthenings
worth pursuing — both have passed every small-field test I could run; nothing is banked beyond the
reproduced finite facts.

## R6.64 · The 144 non-monomial g-minimizers over GL(4,2) are all "permutation + rank one"
`logs/k1695/round6_min144.log` (own code). Every one of the 144 non-monomial matrices with
g(A) = 6 = 3! is of the form A = P_w + (rank-1 matrix) over F₂ (min over permutations of rank(A − P_w)
is 1 for all 144); e.g. R = rows 0001/0010/0111/1011 = P_anti + vvᵀ with v = e₃ + e₄. Their six good
permutations are NOT the n-cycles: for R they have cycle types (1⁴), (2,1,1)×2, (2,2), (4)×2 — only
two of the six 4-cycles work — and the multiset of good cycle types takes several values across the
144 (12 each per pattern, several patterns; full list in the log). So the sharpness cases of (GC₄) over
F₂ are exactly the monomial matrices and the rank-one perturbations of permutation matrices, and the
mechanism of the bound is not "n-cycles always work". (Time stamps: the §R6.63 grade and its dialogue
message were written at 13:3x CDT, not 14:0x as the message said.) K6-GC is running on Qwen.
**§R6.61 run-3 progress 13:59 CDT (heartbeat 18:52Z, elapsed 141 min):** degree-12 layer begun — first
round 129 868 × 1 350 651 (0.64 %), 1 606 new / 1 395 zero, 1 234 s; queue ≈71.6 k; RSS 15.7 GB (+1.3 GB
in 30 min). Local lift 152 min, 1.2 GB (cap at 14:27). No decision due.
**§R6.58 local corrected lift: UNRESOLVED at the 3-h wall** (`logs/k1695/round6_liftQ_fix.log`:
`UNRESOLVED cap=wall-10800s peak_rss_kib=1302544`) — time-bound, not memory-bound (peak 1.3 GB); not
relaunched locally; the VM copy (run 3, no cap) continues (2 h 49 min at 14:29, 596 MB).
**§R6.61 run-3 progress 14:29 CDT (heartbeat 19:23Z, elapsed 171 min):** degree 12, second round in
progress with a 197 879 × 2 028 855 matrix (0.44 %); queue 86.3 k; RSS 17.0 GB (+1.4 GB per 30 min) of
23 GiB. At this slope the scope lasts ≈2 h more; continue under the no-cap rule; OOM → highmem-8.

## R6.65 · K6-GC (Qwen3.8-Max) GRADED — (GC₃) PROVED for every field (re-derived by me, exhaustively checked for q ≤ 5): BANKED as a lemma
`engine/harvest/k1695_r6_gc_qwen.md`. **Theorem (GC₃, strong form).** For every field F and every
A ∈ GL(3,F) there are at least two σ ∈ S₃ such that e₁ is a Krylov-cyclic vector of AP_σ; in
particular g(A) ≥ 2 = 2!. **Proof (Qwen; every step re-derived here).** With x_i ∈ F² the projection
of column a_i to coordinates 2,3, and σ = (i,j,k) in one-line notation, det(e₁, AP_σe₁, (AP_σ)²e₁) =
x_{i,1}[x_i,x_j] + x_{i,2}[x_i,x_k] =: Δ(i;j,k) (expand (AP_σ)²e₁ = a_{i,1}a_i + a_{i,2}a_j + a_{i,3}a_k and
the determinant along e₁). Rows 2,3 of A are independent, so x₁,x₂,x₃ span F². **Lemma:** at least two
of the six Δ(i;j,k) are nonzero. If some x_i = 0 the other two are independent and each gives a nonzero
Δ. Otherwise call i silent if Δ(i;j,k) = Δ(i;k,j) = 0; with x_i = (p,q), silence is pA + qB = qA + pB = 0
for A = [x_i,x_j], B = [x_i,x_k], so p² ≠ q² would force A = B = 0 and all three collinear — hence
silent vectors have p² = q², and two silent vectors are independent (else [x₁,x₃] = 0 and again
collinear). In characteristic 2, p² = q² means p = q, one line, so two silent indices cannot exist —
**characteristic 2 is handled, not dropped** (the "char ≠ 2" clause belongs to the branch where two
silent indices exist, which is impossible there). In characteristic ≠ 2 two silent vectors are
x₁ = a(1,1), x₂ = b(1,−1); silence gives x₃ = (a−b, a+b) and then Δ(3;1,2) = Δ(3;2,1) = −4a²b ≠ 0 —
so index 3 supplies two nonzero Δ. ∎ **Own-code checks** (`round6_gc3_check.py`,
`logs/k1695/round6_gc3_check.log`): exhaustive on GL(3,q), q = 2,3,4,5 — the minimum of
#{σ : e₁ Krylov-cyclic for AP_σ} is exactly 2 in every cell (histograms recorded). **Status:** the
first result on this line that is strictly stronger than the n = 3 theorem (§R6.18: one σ; now two,
both with e₁), proved for all fields by hand across two families (engine wrote, I re-derived) and
verified on every finite cell ≤ 5; Lean formalisation queued (elementary: a 2-variable polynomial
identity plus case analysis). **§2 (the F₂ minimizer):** normalisation rank(I + R + μS) with
S = P₀⁻¹P_σ⁻¹, R = (e₁+e₂)(e₃+e₄)ᵀ — correct; its six good σ = {id, (12)(34), (13), (24), (1243),
(1342)} coincide exactly with my computed list (§R6.64); the 18 failures explained by rank ≤ 2 at
μ = 1 — consistent. **§2.6 (non-monomial minimizers over q ≥ 3) — PROVED, re-derived and checked:**
A_γ = I + γJ with char ∤ n; A_γP = P + γJ splits over H = {Σx = 0} ⊕ F𝟙 with minpoly
lcm(m_{P|H}, x − (1+nγ)); n = 3, λ = −1 (char ≠ 2,3): only the two 3-cycles are cyclic ⟹ g = 2;
n = 4, λ = ω a primitive cube root (char ≠ 2,3): only the six 4-cycles ⟹ g = 6. Checked: F₅, n = 3,
A = I + J: g = 2 ✓ (and the 48 minimizers of GL(3,5) = 24 scalar×permutation + 24 = {QP + J}×F₅^×
exactly); F₇, n = 4, A = I + 2J: g = 6 ✓ (control I + J: g = 14). So "minimizers are monomial for
q ≥ 3" is FALSE (as Qwen says) and the sharpness locus of (GC_n) contains permutation + rank-one
matrices in every characteristic tested. Open (as stated): n ≥ 5 families, injections, characters.
**§R6.65 addendum — the e₁-strong form does NOT extend to n = 4:** over GL(4,2) the minimum of
#{σ : e₁ Krylov-cyclic for AP_σ} is 4 < 6 = 3! (576 matrices attain 4; `logs/k1695/round6_gc4_e1.log`),
while min g = 6 with an arbitrary cyclic vector (§R6.63). So the n = 3 mechanism (both good
permutations share the cyclic vector e₁) is special to n = 3; (GC₄) needs a vector-free argument.
**§R6.61 run-3 progress 15:01 CDT (heartbeat 19:53Z, elapsed 201 min):** degree 12, third round in
progress (196 115 × 1 740 188, 0.69 %); queue 95.2 k; RSS jumped to 20.9 GB (+3.9 GB in 30 min) of the
23 GiB scope — OOM likely within the hour. VM lift 3 h 19 min, 685 MB. Preparing the pre-cleared
highmem-8 run (64 GB) as run 4 with its own name/prefix so it can start before run 3 dies (msolve has
no checkpoint; nothing is lost by overlap except ≈$0.18/h).
**Decision 15:0x CDT:** CPU quota is 32/32 again (677 launched r46g, r46j), so the 8-vCPU highmem-8
cannot start now anyway. Plan: let run 3 continue (its msolve to the OOM — the memory-vs-degree curve
is itself the evidence; its lift uncapped); no relaunch request now; at the daily review (≈11:00 CDT
08-30, or earlier if 677 frees 8 vCPUs) decide between e2-highmem-8 (64 GB), n2-highmem-16 (128 GB,
≈$23/day) or stopping F4 on this ideal ("next: theory") from the curve: degree 12 already needs
≈21 GB with 3000-pair rounds and 1.7–2.0 M-column matrices; degrees 13+ will be larger.
`k1695_r6_launch3.sh` now takes NAME/PREFIX from the environment (run 4 = k1695-r6-groebner4 /
k1695_r6d) so a bigger machine can start while run 3 still holds the lift.
**Run 4 pre-registered (15:1x CDT):** 677 releases 8 vCPUs at ≈15:45 CDT (ext-r46e cap exit); dialogue
launches by path `MACHINE=e2-highmem-8 NAME=k1695-r6-groebner4 PREFIX=k1695_r6d bash
engine/gcp/k1695_r6_launch3.sh` on my "LAUNCH3" reply (pre-authorised, no caps, 5-day backstop,
run 3 untouched). Terms: e2-highmem-8 (8 vCPU, 64 GB, ≈$0.36/h ≈ $8.6/day; msolve scope = 56 GiB,
`-m 3000 -u 5` kept — memory is the binding constraint — 8 threads; lift 6 GiB in parallel; heartbeat
10 min; outputs gs://…/k1695_r6d/out/). Decision rationale: 64 GB is the largest machine the quota
allows; run 3 shows 32 GB is insufficient already at degree 12; cost is inside the owner's rule; the
daily review (08-30 ≈11:00 CDT) judges from run 4's curve whether F4 on this ideal is feasible at all.
**§R6.61 run-3 progress 15:28 CDT (heartbeat 20:23Z, elapsed 232 min):** degree-12 third round still
running (> 50 min; 196 115 × 1 740 188); RSS 21.5 GB (+0.6 GB in 30 min — the growth slowed again
inside the round). VM lift 3 h 49 min, 580 MB. GC2 / GC-LEAN harvests not yet in.

## R6.66 · CORRECTION of my K6-GC2 brief line, and grade of the K6-GC2 (Qwen) answer
**Correction (my error, caught by Qwen):** the brief said "over F₂ the 168 minimizers all have good
sets with ≥ 2 cycle types". That was read off the 144 NON-monomial minimizers (§R6.64) and
overgeneralised: for the 24 permutation matrices A = P_w over F₂ the good set is {σ : wσ a 4-cycle}
— one cycle type. Correct statement: the 144 non-monomial minimizers have ≥ 2 good cycle types; the
24 monomial ones have exactly one. Qwen's Q3 verdict FAILED is right (also for aI and I + γJ over
larger fields). Lesson re-recorded: a summary line about a dataset must be computed on that dataset.
**K6-GC2 (Qwen) grade.** `engine/harvest/k1695_r6_gc2_qwen.md`: honest (no proof of (GC₄)). **§1
Lemma 1.1 — correct** (a bad τ exists, B = AP_τ has an eigenvalue λ ≠ 0 of geometric multiplicity ≥ 2,
A₀ = λ⁻¹B = I + R with rank R ≤ 2, g unchanged by extension/right permutation/scaling) — but it is
exactly the stratum-(a) normalisation of §R6.42 (rank ≤ 2 perturbations of I, codimension 4 in
M₄), so a modest reduction, not "a 2-parameter family". **§3 derangement conjecture — REFUTED by my
tests** (`round6_gc4_lowrank.py`, `logs/k1695/round6_gc4_lowrank.log`): among rank ≤ 2 perturbations
of I over F₃ some members have all 9 derangements bad; explicit witness A = I + uuᵀ, u = (1,1,2,2)
over F₃ (A = rows 2122/1222/2221/2212): g = 8 and the good set is eight permutations of cycle type
(3,1) — no derangement is good. Over F₅ the maximum is 7 bad derangements. **Low-rank form of (GC₄)
— consistent:** min g = 6 over 11 939 invertible samples I + UWᵀ over F₃ (58 attain 6) and over
15 366 samples over F₅ (1 attains 6); rank-1 over F₃: min 6 (720 of 13 360). **§4 partial cases** —
correct (scalar, diagonal via weighted 4-cycles, monomial, I + γJ; verified: I + 2J over F₇ has g = 6
with bad derangements exactly the three double transpositions). **§5 kill-a-4-cycle family —
verified:** over F₅ with i = 2, E = 4(I + 2P + 4P² + 3P³) is an idempotent of rank 1 and A = I + E has
g = 14 with the identity and P among the bad ones (as claimed; g not below 6). **Q2** — nothing found,
consistent with all data. **Verdict:** no new theorem; one correct-but-known reduction; one
conjecture refuted; the sharp locus (g = 6) sits inside rank ≤ 1 perturbations of I in every test
so far — the natural next target is (GC₄) restricted to A = I + uwᵀ (brief K6-GC3).

## R6.67 · K6-GC-LEAN (Qwen) draft: 45 compile errors — repair round ticketed (engine as compute)
`engine/harvest/k1695_r6_gclean_GoodCount3.lean` (16 KB, 14 declarations, no sorry) copied to
`lean/proofenv/K1695/GoodCount3.lean`; `lake env lean` → 45 errors (`logs/k1695/round6_gclean_compile.log`):
two trivial (`.1` on an `Or` at line 26; a name clash with Mathlib's `eq_neg_of_add_eq_zero_left` at
41), the rest failing `simp`/`rewrite` steps and unsolved goals inside the Δ-lemma case analysis and
the 3×3 determinant/permMatrix reduction. Not "trivially repairable" → not repaired by hand; the full
compiler output plus repair hints goes back to the engine as `engine/briefs/k1695_r6_gclean2/BRIEF.md`
(K6-GC-LEAN-2). Nothing kernel-checked yet; (GC₃) remains banked on the hand proof (§R6.65).
**§R6.61 run 4 LAUNCHED** by dialogue at 2026-08-29T20:52:32Z (15:52 CDT) after 677 released 8 vCPUs:
`k1695-r6-groebner4` (e2-highmem-8, 64 GB, ≈$0.36/h), prefix k1695_r6d, no caps, 5-day backstop,
`-m 3000 -u 5`, 8 threads, msolve scope expected 56 GiB, lift 6 GiB in parallel. Run 3 untouched
(22.0 GB at 15:45, still the third degree-12 round). Fleet 32/32.
Run-4 setup verified (serial, 15:56 CDT): RUNNER3 START 20:53:32Z, memtotal 65 841 336 KiB → msolve
scope 54G, nproc 8, ms_opts '-m 3000 -u 5'; tools as before; liftQ (6G) and sprime4r_p2 (54G) started
20:55:55Z. Outputs gs://…/k1695_r6d/out/.

## R6.68 · RUN 3 msolve verdict: UNRESOLVED-due-to-load at the 23 GiB scope (OOM 15:59 CDT, 4 h 25 min); full memory-vs-degree curve
Harvest `engine/harvest/k1695_r6_gcp3/` (sprime4r_p2.err/.status, runner.log). Kernel: msolve killed
at anon-rss 24.07 GB in the FOURTH degree-12 round (115 996 rows started). F4 table (degree, pairs
selected, matrix, new/zero, real s): d7 129×5 376 (26/0, 0.2 s); d8 1 325×32 637 (121/3); d9
7 867×119 831 (478/165, 3 s); d10 36 582×415 894 (1960/1040, 135 s) + 27 931×221 143 (107/235, 75 s);
d11 117 218×1 201 006 (1876/1126, 365 s), 59 583×378 311 (2061/939, 704 s), 71 181×412 352 (455/2545,
871 s), 79 647×454 944 (2697/303, 1485 s), 85 766×463 830 (363/2637, 1659 s), 94 372×492 271 (61/1318,
1203 s); d12 129 868×1 350 651 (1606/1395, 1234 s), 197 879×2 028 855 (1066/1934, 2945 s), 196 115×
1 740 188 (2146/854, 4426 s), 4th round died. RSS: ≈14 GB through degree 11, 15.7 → 17.0 → 21.5 → 24 GB
across the degree-12 rounds; round times 20 → 49 → 74 min. Basis not reached; nothing about (S′)₄
follows. The runner moved on to sprime4r_p3 (same fate expected, harmless); the VM stays up for its
lift (uncapped, 0.75 GB). **Run 4** (54 GiB scope, 8 threads) will pass degree 12 (≈2.3× the memory)
and then meets degree 13 with unknown size; if degree 13 also outruns 54 GiB, F4 on this ideal is
declared out of reach (no larger machine fits the quota) — decision at the 08-30 review.
**§R6.61 progress 16:23 CDT:** run 4 (54 GiB, 8 threads) at 20 min is already in degree 11 (first
d11 round 406 s; RSS 6.2 GB); run 3's runner is on sprime4r_p3 (5.9 GB, doomed, harmless) and its lift
is at 4 h 40 min (0.70 GB). GC3 / LEAN-2 harvests not yet in.

## R6.69 · K6-GC3 (Qwen) GRADED: the rank-one bound g(I + uwᵀ) ≥ 6 SURVIVES every test, but its PROOF IS INVALID (face lemma false) and Theorem 2 is FALSE
`engine/harvest/k1695_r6_gc3_qwen.md`. Tests `round6_gc3_rank1.py` (`logs/k1695/round6_gc3_rank1.log`,
own code): exhaustive over all (u, w) for F₂ (136 invertible A), F₃ (4 401), F₄ (49 216); 30 000-samples
over F₅ (23 956) and F₇ (25 751). **Correct:** Lemma 1 (rank-one update, T1 in our language — standard);
Proposition 2 (identity and all six transpositions are bad for every rank-one A — 0 violations);
the equality family I + γJ, 1 + 4γ = ω. **Conclusion of Theorem 1 consistent:** min g = 6 in every
cell. **Proof of Theorem 1 INVALID:** the "face-matching lemma" b_T + b_F ≤ 8 is FALSE — max b_T + b_F
= 10 over F₂, F₃, F₄, F₅; the local claim "every bad 4-cycle has ≥ 2 good faces" fails (6/72/354/49
matrices) and Hall/SDR fails (12/36/36/10). Witness in every characteristic: the transposition matrix
A = P_(24) = I + uwᵀ with u = (0,1,0,−1), w = (0,−1,0,1): all six 4-cycles and four 3-cycles are bad
(b_T + b_F = 10), one double transposition bad, g = 6 with good types {(2,2)², (3,1)⁴}. The bound holds
there because the double transpositions compensate — the true accounting is the trivial identity
b_(2,2) + b_T + b_F ≤ 11 (⟺ g ≥ 6), and any real proof must handle the trade-off between the (2,2)
class and the (3,1)+(4) classes; Cases B/C of the sketch were never carried out. **Theorem 2 FALSE**
(char ≠ 2,3 equality classification): besides A = I and I + γJ, (a) the transposition matrices
(rank-one, monomial) have g = 6; (b) a non-monomial, non-constant witness over F₅: u = (4,0,1,0),
w = (1,1,4,4), A = rows 0411/0100/1104/0001 (8 nonzero entries), g = 6, good types {(3,1)⁴, (4)²}.
**Char-2 conjecture incomplete:** u = e₃+e₄, w = 𝟙 over F₂ has g = 6 and is not a complementary pair
(F₂ nontrivial minimizers form 4 orbits under simultaneous permutation + reciprocal scaling:
(e₃+e₄, e₃+e₄) [= P_(34)], (e₃+e₄, e₁+e₂), (e₃+e₄, 𝟙), (𝟙, e₃+e₄); F₃: 4 orbits, three non-monomial;
F₄: the same 4 patterns as F₂). **Status:** (GC₄) on the rank-one stratum = CONJECTURED with strong
exhaustive evidence (q ≤ 4) — not banked; corrected brief K6-GC4 written with the true counts.
**§R6.67 round 2 (16:47 CDT):** `k1695_r6_gclean2_GoodCount3.lean` (10 declarations, restructured)
compiles with 33 errors (was 45): systematic `let`-abbreviation opacity (`p q r s : K := ⋯` invisible to
`simpa`/`ring`/`linear_combination`), Finset/DecidablePred elaboration in the count lemma, a missing
binder at line 503, and the 3×3 determinant reduction. Not mathematical errors as far as visible. Round 3
brief with the full log and targeted fixes: `engine/briefs/k1695_r6_gclean3/BRIEF.md`. Still nothing
kernel-checked; (GC₃) stays banked on the hand proof.
**§R6.61 progress 16:54 CDT:** run 4 (54 GiB, 8 threads) at 58 min: degree-11 rounds 4 of 6 done,
round times ≈ run 3's (1255 s vs 1485 s — the F4 linear algebra is not scaling with threads), RSS
10.2 GB; expected to enter degree 12 at ≈17:50 and reach the round that killed run 3 at ≈20:00 CDT.
Run 3: p = 3 msolve 8.8 GB (45 min, doomed), lift 5 h 10 min (0.73 GB). No harvests yet (GC4, LEAN-3).

## R6.70 · K6-GC4 (Qwen) GRADED: honest, no proof; §1–§6 correct; §8 gives a valid COMPUTED-proof scheme — adopted as my next light deliverable
`engine/harvest/k1695_r6_gc4_qwen.md`. Re-derived: §1 corank-2 / corank-1 badness criteria (our Lemma T
T2/T1); §2 identity + six transpositions always bad; §3 g ≥ 6 ⟺ b_(2,2)+b_(3,1)+b_(4) ≤ 11; §4 explicit
conditions (double transposition bad at μ = ±1 ⟺ pair-sums or pair-differences of u or of w vanish;
3-cycle fixing l bad at μ = 1 ⟺ u_l = 0 = u_i+u_j+u_k or the same for w); §5 permutation matrices and
I + γJ (char ≠ 2,3) are equality families; §6 Lemma 3 (if all three double transpositions are bad,
one of u, w is a sign vector up to scaling/permutation — pigeonhole over the three partitions) and §6.1
(u of sign type (3,1) ⟹ no 4-cycle is bad in char ≠ 2: Σu = 2, alternating sums ±2, and the ±i
conditions force an even number of minus signs) — all correct. §9's terminology remark is fair: my brief's
"A monomial" as an equality family was sloppy (diag(λ,1,1,1) is monomial with g ≫ 6); the proved
monomial equality family is the permutation matrices (times scalars). **§8 scheme (valid):** for each
12-subset S of the 17 non-trivially-bad permutations, the ideal I_S = ⟨cz − 1, χ_{P_σ}(t_σ), all 3×3
minors of P_σ + u w_σᵀ − t_σ I : σ ∈ S⟩ in ℤ[u, w, z, t_σ] is unit iff no rank-one A has all of S bad;
1 ∈ I_S for every S (up to S₄-conjugation and σ ↦ σ⁻¹) proves the rank-one (GC₄) in that
characteristic. Systems are tiny (21 variables, ≈200 generators of degree ≤ 9 but sparse), so this is a
LIGHT local computation. **Pre-registration (§R6.71 to follow):** script `round6_gc4_cert.py`; controls:
the 11-element bad sets of I + γJ (3 (2,2) + 8 (3,1)) and of P_(24) (1 (2,2) + 4 (3,1) + 6 (4)) must be
CONSISTENT (non-unit); single-σ ideals non-unit; then all 12-subset orbits over GF(7) first, then
GF(2), 3, 5, 11, 13 and ℚ; a unit ideal for every orbit in characteristic p banks "(GC₄) on the rank-one
stratum in characteristic p" as COMPUTED (own verifier + controls); all characteristics would need
ℤ-certificates (later). Any non-unit 12-subset = a candidate counterexample: extract the point and
test with round6_gc3_rank1.py-style code.

## R6.71 · Rank-one (GC₄) certificate run LAUNCHED (own encoder `round6_gc4_cert.py`; controls passed)
Controls over GF(7) (`logs/k1695/round6_gc4_cert_controls.log`): a single-σ ideal, the 11-element bad
set of I + γJ ({(2,2)³, (3,1)⁸}) and the 11-element bad set of P_(24) ({(2,2)¹, (3,1)⁴, (4)⁶}) are all
NON-unit (as they must be: those patterns are realised), 1–7 s each. Full run: every 12-subset of the
17 permutations up to S₄-conjugation × inversion (48 symmetries), GF(7) first
(`logs/k1695/round6_gc4_cert_p7.log`); reading: all orbits unit ⟹ "(GC₄) on the rank-one stratum,
every field of characteristic 7" COMPUTED; any non-unit orbit ⟹ candidate counterexample to extract.
Then p = 2, 3, 5, 11, 13 and ℚ.
**§R6.61 progress 17:25 CDT:** run 4 finished degree 11 (six rounds, last 707 s) at 88 min and enters
degree 12 with RSS 13.9 GB of 54 GiB; run 3: p = 3 msolve 13.2 GB (doomed), lift 5 h 50 min.
Certificate run (§R6.71, GF(7)): 126/195 orbits, 0 non-unit so far.

## R6.72 · COMPUTED: (GC₄) on the rank-one stratum holds over every field of characteristic 7 — BANKED (own verifier + controls); other characteristics running
`logs/k1695/round6_gc4_cert_p7.log`: all 195 orbits of 12-subsets (of the 17 permutations of types
(2,2), (3,1), (4), under S₄-conjugation × inversion) give the UNIT ideal over GF(7) — 0 non-unit —
in 1395 s (msolve 0.10.1, ≈7 s per system). Together with the identity and the six transpositions
being always bad (§R6.70 §2, proved), and the Nullstellensatz over F̄₇: **for every field F of
characteristic 7 and all u, w ∈ F⁴ with 1 + wᵀu ≠ 0, at most 11 of the 17 permutations are bad, i.e.
g(I + uwᵀ) ≥ 6.** Verifier: `round6_gc4_cert.py` (encoder written by me from the criterion "AP_σ
non-cyclic ⟺ ∃ eigenvalue t of P_σ with rank(P_σ + u w_σᵀ − tI) ≤ 2", implemented as χ_{P_σ}(t_σ) = 0
plus all sixteen 3×3 minors; Rabinowitsch cz − 1); positive/negative controls in §R6.71 (the two
realised 11-element bad sets and a single-σ ideal are non-unit). Same-family caveat: encoder and
verifier are both mine; the statement is independent of the (falsified) face lemma. Exhaustive
finite-field data (§R6.69) agree. **Launched sequentially** (same script): p = 2, 3, 5, 11, 13 and
characteristic 0 (`logs/k1695/round6_gc4_cert_p{2,3,5,11,13,0}.log`); each ≈ 25 min. Reading: unit
everywhere ⟹ the rank-one half of (GC₄) in those characteristics; all characteristics at once would
need ℤ-certificates (later, via lift on the tiny systems).
**§R6.72 update (17:5x CDT):** characteristic 2 also COMPUTED — all 195 orbits unit over GF(2) (569 s,
`logs/k1695/round6_gc4_cert_p2.log`); p = 3, 5, 11, 13, 0 running.
**§R6.67 round 3 (17:52 CDT):** `k1695_r6_gclean3_GoodCount3.lean` (15 declarations, no let-abbreviations)
compiles with 23 errors (45 → 33 → 23): two Mathlib-name mismatches (`Finset.card_insert_of_not_mem` →
`…_of_notMem`, `Matrix.dotProduct` → `dotProduct`; renamed by me, trivial), six "no goals" (tactics
after the goal closed), five `rewrite` pattern failures, four `simp` failures, one unsolved goal, one
type mismatch. One more engine round (round 4) with the post-rename log; firm stop rule: park unless
round 4 reaches ≤ 5 errors.
**§R6.72 update (17:57 CDT):** characteristic 3 COMPUTED — 195/195 unit over GF(3) (866 s); p = 5, 11,
13, 0 running. **§R6.61 progress:** run 4 in degree 12 — round 1 done in 799 s (run 3: 1234 s), round 2
(197 879 × 2 028 855) running, RSS 17.1 GB of 54 GiB at 118 min; run 3's p = 3 msolve at 18.6 GB
(will OOM), lift 6 h 20 min. K6-PHI is now on the Pro seat; LEAN-4 on Qwen.
**§R6.67 round 4 (18:2x CDT) — Lean target PARKED.** The round-4 harvest is an incomplete file
(204 lines, 11 helper declarations; the Δ-lemma, `deltaSix_count_ge_two` and `goodCount3` are absent —
output truncated or partial). Stop rule applied: no further blind rounds. (GC₃) stays banked on the
hand proof (§R6.65: engine proof + my full re-derivation + exhaustive q ≤ 5 checks). Best artefact if
resumed by a Lean-capable engine (codex, after Sep 3): `engine/harvest/k1695_r6_gclean3_GoodCount3.lean`
(531 lines, 22 mechanical errors after two renames; log `logs/k1695/round6_gclean3b_compile.log`).
**§R6.72 update (18:24 CDT):** characteristic 5 COMPUTED — 195/195 unit over GF(5) (987 s); p = 11
running, then 13 and 0. **§R6.61 progress:** run 4 degree-12 round 2 done in 1286 s (run 3: 2945 s —
the 8 threads pay off in the big rounds), round 3 running, RSS 21.2 GB of 54 GiB at 138 min; run 3's
p = 3 at 18.6 GB, lift 6 h 41 min.

## R6.73 · (Mono) REFUTED at n = 6 over F₂ — cross-family (GPT-5.6 Pro found it; my own kd/ν code confirms); the Φ′ = (kd, −ν) hill-climbing route is dead as stated; the two-step phenomenon survives
`engine/harvest/k1695_r6_phi_pro.md` (K6-PHI on Pro, 45 min); my check `logs/k1695/round6_phi_pro_check.log`
(round6_controllable conventions: column swap = right multiplication by P_τ, index i ↦ e_i, kd = rank of
the Krylov matrix). M ∈ GL(6,2) with rows 000100 / 100000 / 111101 / 001000 / 101110 / 000001, i = 1:
kd(M, e₁) = 5; no transposition raises it (profile 3,4,4,5,4,4,4,5,4,2,5,4,3,4,3 over the 15
transpositions in lexicographic order) — a kd-local maximum; ν = 3 with neutral moves (1,5), (2,5), (3,5);
after them ν = 8, 4, 4 — every neutral move INCREASES ν. So Φ′ = (kd, −ν) has a strict local maximum
below kd = n: **(Mono) is false** (§R6.45's conjecture; also fails at i = 4 for the same M). The
two-step ascent exists: kd(M P_(15) P_(16), e₁) = 6 — consistent with "one neutral step then ascent"
observed on every scanned cell (n ≤ 5, §R6.35/§R6.39) and here. **Status changes:** (Mono) → REFUTED
(smallest known counterexample n = 6, q = 2; the eight exhaustive cells with no Φ′-local maxima were
all n ≤ 5); the Q + J family theorem (§R6.62) is unaffected (a family where (Mono) holds); 16.95
untouched (M has good permutations). **Surviving conjecture (2Step):** for every (B, i) with kd < n
that is a kd-local maximum there are transpositions τ (neutral) and τ′ with kd(BP_τP_τ′, i) > kd(B, i)
— it implies (S′), hence 16.95, by repeated ≤ 2-step ascents; no potential-function proof is known.
Lesson: the potential was fitted to n ≤ 5 data — "no local maxima on 8 cells" was evidence, not a law.

## R6.75 · CONSOLIDATED (18:52 CDT): (GC₄) on the rank-one stratum COMPUTED for characteristics 2, 3, 5, 7, 11, 13 (ℚ running)
All six finite characteristics: every one of the 195 orbits of 12-subsets gives the unit ideal
(`logs/k1695/round6_gc4_cert_p{2,3,5,7,11,13}.log`: 569 / 866 / 987 / 1395 / 1150 / 1096 s; 0 non-unit).
Hence, for every field F with char F ∈ {2, 3, 5, 7, 11, 13} and all u, w ∈ F⁴ with 1 + wᵀu ≠ 0:
g(I + uwᵀ) ≥ 6 (at most 11 of the 17 permutations of types (2,2), (3,1), (4) are bad; the identity and
the six transpositions are always bad). Verifier: `round6_gc4_cert.py` (own encoder; controls §R6.71).
Characteristic 0 running (`round6_gc4_cert_p0.log`). All characteristics at once would need
ℤ-certificates — a later item. **(2Step) probe** (`round6_twostep_probe.py`, GF(2)): n = 6 — 5 871 random
invertible B, exactly one kd-local maximum (B, i) below n found, and it is a (Mono) failure while
(2Step) holds; n = 7 — 1 781 samples, no local maximum at all. So kd-local maxima are rare at n ≥ 6
in random samples (the Pro counterexample was not a random find), and (2Step) has no failure yet.
**Run 4 (§R6.61) 18:52:** degree-12 round 3 done in 2093 s (run 3: 4426 s); round 4 — the round that
killed run 3 at 24 GB — running with RSS 26.7 GB of 54 GiB at 169 min.
**K6-2STEP brief (19:0x CDT)** `engine/briefs/k1695_r6_2step/BRIEF.md` for the Pro seat: break (2Step) by
construction with an exact verifier (n ≤ 7, F₂/F₃/F₄, structured families, the neighbourhood of M) or
prove it in the top layer / isolate the obstruction; also asks for any radius-≤2 potential with
evidence. Harvest → `k1695_r6_2step_pro.md`. Pre-registered readings: a verified counterexample →
(2Step) REFUTED, the hill-climbing paradigm closed, and the S′-route must be re-based on a global
argument (OC_n / GC_n / Ω-ideal); a top-layer proof → re-derived step by step before entry.
**Structured (2Step)/(Mono) probe, n = 6 over GF(2)** (`round6_twostep_struct.py`,
`logs/k1695/round6_twostep_struct.log`): rank-one perturbations P_w + uvᵀ and rank-two perturbations of
permutation matrices — see the log lines (local maxima are far more common here than in random
matrices: 77 among 11 528 invertible rank-two samples); (Mono) fails at several of them (6), (2Step)
fails at NONE. (2Step) remains unbroken on every cell probed.
**§R6.75 FINAL (19:13 CDT): characteristic 0 also COMPUTED** — 195/195 unit over ℚ (1030 s,
`logs/k1695/round6_gc4_cert_p0.log`). **Banked statement:** for every field F of characteristic
0, 2, 3, 5, 7, 11 or 13 and all u, w ∈ F⁴ with 1 + wᵀu ≠ 0, g(I + uwᵀ) ≥ 6 — the rank-one stratum of the
good-count conjecture (GC₄) — COMPUTED by my own encoder/verifier (`round6_gc4_cert.py`, msolve
Gröbner bases of the 195 orbit ideals; positive/negative controls §R6.71; exhaustive finite-field
agreement §R6.69). Not yet all characteristics (would need ℤ-certificates; each system is tiny, so
`lift` is a plausible later item). **Run 4 (§R6.61) 19:13:** degree-12 round 4 (202 755 × 1 762 422,
0.88 %) running with RSS 28.2 GB of 54 GiB at 189 min — past the 24 GB at which run 3 died; run 3's
p = 3 at 22.7 GB (about to OOM), lift 7 h 31 min.
**§R6.61 progress 19:39 CDT:** run 4 survived the round that killed run 3 (degree-12 round 4: 804 new /
2196 zero, 2654 s) and is in round 5 (262 126 × 2 471 029, 0.56 %), queue 121.6 k, RSS 31.9 GB of
54 GiB at 219 min; still degree 12 (the layer has many rounds at 3000 pairs each). Run 3: p = 3 at
22.6 GB, lift 8 h 02 min. K6-2STEP (Pro) not yet harvested.

## R6.76 · (2Step) REFUTED at n = 5 over F₄ — cross-family (GPT-5.6 Pro constructed; my own GF(4) code confirms); the neutral-prefix hill-climbing programme is closed
`engine/harvest/k1695_r6_2step_pro.md`; my check `logs/k1695/round6_2step_pro_check.log` (GF(4) with
α² = α + 1, entries 0,1,2,3 = 0,1,α,α+1 — the encoding of round6_controllable agrees: 2·2 = 3, 2·3 = 1).
**C** = rows 00001 / 01000 / 10000 / 21310 / 33302 ∈ GL(5,4), i = 1: kd = 4 = n − 1, profile
12:3 13:3 14:4 15:4 23:3 24:3 25:3 34:2 35:2 45:2 — a kd-local maximum with exactly two neutral moves
(14), (15); after each, the maximum second-step kd is 4 — both dead. So (2Step) is FALSE, in the top
layer (the Krylov hyperplane is even a coordinate hyperplane x₂ = 0). **T** = rows 00010 / 33223 /
00100 / 10120 / 22231 ∈ GL(5,4), i = 1: kd = 4 and EVERY transposition lowers it (profile 3,3,2,3,3,2,2,
3,3,2) — a strict local maximum with no neutral move, so every neutral-prefix (kStep) variant fails;
T = S + uwᵀ with S a permutation-like matrix, u = (0,1,0,2,3), w = (2,3,2,2,3) — a rank-one structured
neighbourhood, not a random point. Both C and T reach kd = 5 within two unrestricted swaps (first step
descending); C also has a neutral-neutral-ascent path. **Status changes:** (2Step) → REFUTED (n = 5,
q = 4; all-F₂ cells up to n = 5 and our 8 cells had none — again "evidence, not law"); (2Step′) → refuted
(Pro: 1984 failures in GL(5,2), consistent with our data that (2Step) held there); the surviving
radius-2 statement is Pro's **U2**: every non-cyclic (B, i) has a larger kd within swap-distance 2 (first
step may descend); with the valid lexicographic potential Ψ₂ = (R₂, −δ₂) (nearest radius-2 maximum),
U2 ⟹ (S′) ⟹ 16.95 — the lemma is a routine BFS-distance argument and is correct. Pro's searches
(≈8.8·10⁸ state visits: exhaustive GL(n,2) n ≤ 5, GL(n,3) n ≤ 4, GL(n,4) n ≤ 3, structured families to
n = 8) found no U2 failure. **Assessment:** the hill-climbing programme has retreated twice today (radius-1
potential Φ′ → (2Step) → radius-2 U2); each refinement is empirically true and structurally empty — a
radius-r ascent for r ≈ n!/2 is the theorem itself. U2 is recorded as a conjecture, not pursued as a
route; the live routes are the global ones: (GC_n) (rank-one half COMPUTED for seven characteristics,
§R6.75), (OC_n) (single opposite chart, §R6.63), and the (S′)₄ Ω-ideal (run 4). Nothing about 16.95
itself changes: C and T have good permutations.
**§R6.61 progress 20:10 CDT:** run 4 degree-12 round 5 done (679 new / 2321 zero, 2423 s), round 6
running, RSS 31.7 GB of 54 GiB — flat for 30 min — at 249 min; degree 12 looks like it is saturating
(new elements per round 1606 → 1066 → 2146 → 804 → 679). Run 3: p = 3 OOM-killed at 00:53Z after 14 057 s
(as expected), runner on p = 5, lift 8 h 32 min.
**§R6.61 progress 20:41 CDT:** run 4 degree-12 round 6 is the biggest matrix so far — 412 072 × 3 363 868
(0.46 %) — and RSS jumped to 43.9 GB of 54 GiB at 279 min (+12 GB in 30 min); OOM in this or the next
round is likely. Curve so far (degree 12, 3000-pair rounds): rows 130 k → 198 k → 196 k → 203 k → 262 k
→ 412 k; RSS 14 → 17 → 21 → 27 → 32 → 44 GB. Run 3: p = 5 at 10.1 GB (doomed), lift 9 h 02 min.
**ℤ-certificate probe for the rank-one (GC₄) systems (20:57 CDT):** Singular `lift(I_S, ideal(1))` over ℚ
on one orbit system (21 variables, 205 generators) exceeded the 2.5 GB local cap in 100 s
(`logs/k1695/round6_gc4_lift_orb000.log`) — cofactor certificates for the 195 systems are NOT a light
local job; they would need a VM (memory unknown, possibly tens of GB per system). Deferred to the
08-30 review as an optional item (upgrade "seven characteristics" → "all characteristics" for a
modest lemma). Tonight's free 8 vCPUs: HOLD — a parallel p = 3 run would meet the same degree-12 wall
as run 4, and the lift job's value does not justify a blind launch.
**§R6.61 progress 21:02 CDT:** run 4 degree-12 round 6 done — 1849 new / 1152 zero (NOT saturating),
3167 s; round 7 running; RSS 43.9 GB of 54 GiB, flat over the last 20 min; 299 min elapsed. Run 3: p = 5
at 14.5 GB, lift 9 h 22 min.
**§R6.61 progress 21:33 CDT:** run 4 degree-12 round 7 done — 2928 new / 74 zero (almost every pair
yields a new basis element: the degree-12 layer is expanding, not saturating), 1906 s; round 8 running;
queue 141.5 k pairs; RSS 45.1 GB of 54 GiB at 330 min. Run 3: p = 5 at 15.8 GB, lift 9 h 53 min.
Review recommendation forming: STOP F4 on this ideal — the basis is growing by ≈3000 elements per
3000-pair round with a six-figure queue; neither 128 GB nor days of wall would predictably finish it.

## R6.77 · OWNER DIRECTIVE 21:3x CDT: codex quota recovered for ONE day — six tickets written; the rank-two 16.95 ideal becomes the main computational target
Tickets (engine/briefs/k1695_r6_*/TICKET.md; DONE markers under engine/harvest/): **K6-R2CERT** (highest):
the rank-two ideal for 16.95 at n = 4 — every all-bad A normalises to I + UWᵀ, U, W ∈ F^{4×2} (§R6.42
stratum (a)); for each of the 23 non-identity σ a FREE variable t_σ (a rank-two update can lower the
rank of the invertible P_σ − tI to 2, so t need not be an eigenvalue of P_σ — unlike rank one, §R6.71)
and the 16 minors of AP_σ − t_σI; plus cz − 1 with c = det(I₂ + WᵀU). Unit over GF(p) ⟺ 16.95 at n = 4
over every field of characteristic p. 40 variables, ≈369 generators — a far better-shaped target than
the (S′)₄ Ω-ideal (16 variables but 24 unstructured sextics whose degree-12 layer alone exceeds
54 GiB). **K6-LEAN-GC3** (compile the parked Lean file), **K6-GC4R2** (rank-two (GC₄) counterexample
hunt, exhaustive over F₃), **K6-OC3** (prove (OC₃); exhaustive (OC₄) over GF(3), GF(4)),
**K6-U2CENSUS** (radius-2 local maxima census), **K6-GC4R2CERT** ((GC₄) rank-two certificates,
19-subsets). Load rule restated in every ticket (run_capped.py, 2.5 GB, ≤ 2 heavy processes overall).
My own R2 encoder is being written in parallel (cross-family verification of the top item).
**§R6.77 own encoder `round6_r2_ideal.py` — controls PASSED (21:4x CDT, GF(2)):** rank-one specialisation
on the bad set of P_(24) → NON-unit (as realised); rank-one all-23 ideal → UNIT in 31 s (reproduces the
§R6.42 rank-one certificate for 16.95 in a new encoding: free t_σ, 16 minors per σ, cz − 1). Main
rank-two ideal over GF(2) (40 variables, 369 generators) launched under run_capped (2.5 GB, 3 h):
`logs/k1695/round6_r2_main_p2.log`. Reading: UNIT → 16.95 at n = 4 in characteristic 2 (cross-family
confirmation expected from the codex K6-R2CERT run); NOT unit → candidate all-bad A: solve and test
all 24 permutations by hand (disclosure protocol); capped → send the .ms file to the VM (8 vCPUs are
free: a run 5 on e2-highmem-8 for this ideal is the right use of them, not the Ω-ideal).

## R6.78 · K6-N4X (codex, clean-room rerun) CONFIRMS rank one at n = 4 — §R6.42/§R6.47 upgraded from PROVISIONAL to cross-family; PROAUDIT third-family checks of M, C, T
`engine/harvest/k1695_r6_n4x/REPORT.md` (11 KB): an independent encoder from the definition (24 deflation
determinants, three x ≠ 0 charts) with msolve: 48/48 reduced bases equal [1] over ℚ and GF(p) for
p ∈ {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47}; 6/6 reruns with the natural variable order also unit;
exhaustive finite audits with zero failures; the load-bearing negative control is a proper determinant
subset over GF(7) (non-unit, 0.29 s) — controls (i) and (iii) turned out not to be negative and are
documented as such (honest). Independence: a clean-room rerun by the same agent that ran N4k, results
frozen before comparison — "not memoryless", as the report says. Together with (a) my encoder
(§R6.42, all p < 10⁴) and (b) today's new-encoding control (round6_r2_ideal.py: the rank-one all-23
ideal with free t_σ and 16 minors per σ is UNIT over GF(2) in 31 s, §R6.77), the rank-one stratum of
16.95 at n = 4 now rests on THREE encodings by two families: **status → cross-family confirmed** for
characteristic 0 and every prime < 10⁴ (all characteristics still needs a ℤ-certificate — the lift
job on runs 3/4). **PROAUDIT** (`engine/out/codex/pro_constructions_audit.md`, codex11, third family):
M (F₂, n = 6: rank 6, kd 5 local max, ν = 3, neighbours 8/4/4), C (F₄, n = 5: kd 4, neutrals (1,4),(1,5)
both dead) and T (strict local maximum) all VERIFIED with negative controls — consistent with my own
checks (§R6.73, §R6.76); the refutations of (Mono) and (2Step) are now three-family.

## R6.79 · Local box thrashing (22:04 CDT: swap 18.2 GB, my msolve swapped out to 156 MB RSS) — local rank-two run KILLED; run 5 (VM) pre-registered for the rank-two ideal
The local rank-two msolve stalled under memory pressure (resident set swapped out, so the RSS cap
cannot trigger; the run is not evidence either way) — killed by me at 22:0x. Inputs written for p = 2,
3, 5, 7 (`engine/harvest/k1695_r6_r2ideal/r2_main_p{2,3,5,7}.ms`, 40 variables, 369 generators).
**Run 5 (pre-registered):** `engine/gcp/k1695_r6_launch5.sh` → e2-highmem-8 `k1695-r6-r2`, prefix
k1695_r6e, ms_jobs = r2_main_p2, p3, p5, p7 sequentially, `-m 6000 -u 5`, no lift, no caps, 5-day
backstop, ≈$8.6/day — the right use of the 8 free vCPUs. Readings: [1] over GF(p) → 16.95 at n = 4 in
characteristic p (VM certificate; local re-run when the box is quiet; codex K6-R2CERT as the
cross-family replicate); non-unit → a candidate all-bad A: solve (-P 1), test all 24 permutations by
hand, disclosure protocol; OOM/stall → UNRESOLVED-due-to-load. **Run 4 (§R6.61) 22:04:** degree-12
round 8 done (149 610 × 697 264), round 9 running, queue 169 k, RSS 45.3 GB of 54 GiB.
**§R6.79 note:** `logs/k1695/round6_r2_main_p2.log` ends with "main: NOT unit (0 chars) … RESULT char 2:
NOT UNIT" — this is the script parsing an EMPTY .gb (0 bytes) after my kill; it is NOT a verdict and
must not be read as a candidate counterexample. Swap fell to 7.3 GB after the kill (22:08 CDT).
**§R6.79 run 5 LAUNCHED** by dialogue at 2026-08-30T03:07:05Z (22:07 CDT): `k1695-r6-r2` (e2-highmem-8),
prefix k1695_r6e, ms_jobs r2_main_p2 → p3 → p5 → p7, no lift, no caps, 5-day backstop. Fleet 32/32.
Run-5 setup verified 22:10 CDT (serial): RUNNER3 START 03:07:35Z, msolve scope 54G, nproc 8, `-m 6000 -u 5`;
r2_main_p2 started 03:09:27Z. Note: the run-3 runner starts its liftQ job unconditionally (the
run_lift flag belongs to runner 2), so a third uncapped lift (6 GiB) also runs here — harmless.

## R6.80 · K6-LEAN8 (codex) reports the assembled stratum-(b) rank theorem in Lean — my own kernel check DEFERRED (memory); T4 interrupted (no verdict)
`engine/harvest/k1695_r6_lean8/REPORT.md`; new file `lean/proofenv/K1695/StratumBAssembly.lean`
(registered in lakefile): `rank_map_eq_of_field_hom`, `stratumB_rank_at_root` (LEAN6's root theorem
upgraded to every ambient extension L/F), `stratumB_rank_at_nonroot`, and the assembled
`stratumB_rank_form` splitting on aeval μ m = 0; report's #print axioms: [propext, Classical.choice,
Quot.sound], no sorry/admit/axiom/native_decide. **My own check:** `lake env lean` on the file hit my
2.5 GB local cap after 19 s (Mathlib import alone needs ≈3 GB resident) — kernel check deferred until
the box is quiet (a single Lean compile at ≈3.5 GB is fine when no other heavy job runs; codex's
lean_objects build is running now). Status: engine-reported clean, not yet line-verified; R1 (rank form
⟹ minimal-polynomial form) still open in Lean (the notebook proof exists, §R6.29). **T4 (codex8):**
interrupted by dialogue at swap 15 GB / load 36 per my pre-approval; the cell caseB_all24_w3_p2 has NO
verdict; resume when quiet.
**§R6.79 run-5 early profile (22:26 CDT):** F4 on the rank-two ideal explodes early — degree 5–7 rounds
already carry a 582 k-pair queue, matrices 60 452 × 620 019 at degree 7, thousands of new basis elements
per round, RSS 15.3 GB at 8 min (scope 54 GiB). It keeps its uncapped chance. **Fallback prepared:**
chart-reduced encoding (`round6_r2_ideal.py --chart`): WLOG rank W = 2 (rank ≤ 1 is the certified rank-one
stratum), an invertible 2×2 minor of W moved to rows 1,2 by conjugation (rows of U and W permute
together, the family {AP_σ} is preserved), and R = UWᵀ = (UG)(WG⁻ᵀ)ᵀ makes that block I₂ — 36 variables,
files `r2_main_chart_p{2,3,5,7}.ms`. If run 5 dies, run 6 = the chart files (same launch script with
ms_jobs override).
**§R6.79 progress 22:32 CDT:** run 5 at 18 min: degree 7, pair queue 888 k, matrix 94 101 × 1 045 364,
RSS 28.4 GB of 54 GiB — the naive rank-two ideal is exploding (OOM expected within the hour). Run 6
prepared: `k1695_r6_launch5.sh` now takes MS_JOBS/NAME/PREFIX from the environment (run 6 =
`MS_JOBS=r2_main_chart_p2,r2_main_chart_p3,r2_main_chart_p5,r2_main_chart_p7 NAME=k1695-r6-r2c
PREFIX=k1695_r6f bash engine/gcp/k1695_r6_launch5.sh`) — to be requested when run 5 dies (quota).
**§R6.61 run 4 22:32:** degree-12 round 9 done (2998 new / 3 zero), round 10 running, queue 197 k,
RSS 46.5 GB; run 3: p = 5 at 22.5 GB, lift 10 h 53 min.

## R6.81 · (GC₃) KERNEL-CHECKED (Lean 4 / Mathlib, my own compile) — the parked target closed by codex10 in 25 min; codex5 exhaustive rank-two (GC₄) over GF(3): min g = 6
`lean/proofenv/K1695/GoodCount3.lean` (codex10 repair of the Qwen round-3 draft; report
`engine/out/codex/k1695_gc3_lean_report.md`). **My check** (`logs/k1695/round6_gc3lean_check.log`,
22:52 CDT): `lake env lean` on the file plus appended `#print axioms` — 0 errors in 12.5 s (peak RSS
6.1 GB: a Lean compile on this box needs ≈6 GB, hence the earlier cap failures); `goodCount3`,
`deltaSix_count_ge_two`, `exists_two_deltaSix_ne_zero` all depend only on [propext, Classical.choice,
Quot.sound]; no sorry/admit/native_decide in the file. **Statement verified:** `theorem goodCount3
(K) [Field K] (A : Matrix (Fin 3) (Fin 3) K) (hA : IsUnit A.det) : 2 ≤ #{σ : Perm (Fin 3) |
det ![e1Vec, colPerm A σ *ᵥ e1Vec, (colPerm A σ * colPerm A σ) *ᵥ e1Vec] ≠ 0}` with `colPerm A σ i j =
A i (σ j)` (= AP_σ in our convention) and `e1Vec = ![1,0,0]` — exactly the strong form of (GC₃)
(§R6.65). Status: **BANKED, kernel-checked** (three families: Qwen proof → my re-derivation →
codex Lean; exhaustive q ≤ 5 data). **K6-GC4R2 (codex5)** `engine/harvest/k1695_r6_gc4r2/`: exhaustive
over GF(3) of all 814 401 rank-≤2 perturbations of I (479 871 invertible): min g = 6, 237 minimizers
(rank(A − I) = 0: 1, 1: 42, 2: 194) in 4 orbit classes under A ↦ QAP; 10⁶ random rank-two samples over
GF(4) (min 6), GF(5) (min 6), GF(7) (min 9), GF(9) (min 12); controls aI / I + 2J / I + J / I + uuᵀ =
6 / 6 / 14 / 8 in two implementations (match my §R6.66/§R6.69 numbers); audit passed. Reading: **(GC₄)
holds on the whole rank ≤ 2 stratum over GF(3) exhaustively** (and hence, by the normalisation
§R6.66, min g over GL(4,3) = 6 — no F₃ counterexample to (GC₄)); no counterexample anywhere. Engine
computation with controls; not independently re-run by me (light to replicate later).

## R6.82 · K6-OC3 (codex4) GRADED: (OC₃) PROVED for every field (re-derived; it is equivalent to "some AP has a cyclic vector with first coordinate ≠ 0", hence also a corollary of (S′)₃/(GC₃)); (OC₄) COMPUTED exhaustively over GL(4,3) and GL(4,4)
`engine/harvest/k1695_r6_oc3/PROOF.md`, `REPORT.md`, logs, `oc_flag_solver.py`, `oc4_exhaustive.c`.
**Proof (re-derived):** for M = AP and v = (1, x, y): u₁ = v, u₂ = (Mv − w₁v)/β with β = w₂ − xw₁,
u₃ = e₃ is lower unitriangular; Mu₁ = w₁u₁ + βu₂ (so H₃₁ = 0, H₂₁ = β) and, writing γ = H₃₂,
multilinearity gives det[v, Mv, M²v] = β²γ — so v is a cyclic vector of M with v₁ = 1 iff β ≠ 0 and
γ ≠ 0 iff u⁻¹Mu is unreduced Hessenberg (their extra factor β in f = K·β is redundant since K = β²γ).
Nonvanishing: M cyclic (our n = 3 theorem) ⟹ K_M ≢ 0 as a homogeneous cubic ⟹ its dehomogenisation
K_M(1, x, y) ≢ 0 ⟹ a nonzero value exists over infinite fields and over GF(q) with q > 3 (partial
degrees < q; they argue with degree 5 and q > 5 — also fine); GF(2), GF(3) (and 4, 5) by exhaustive
enumeration (168 / 11 232 / 181 440 / 1 488 000 matrices, all pass). ∎ **Assessment:** correct and
clean; but at n = 3 the opposite-chart condition is automatic for any cyclic vector with v₁ ≠ 0, so
(OC₃) also follows at once from (S′)₃ (e₁ cyclic) — a corollary, not a new mechanism; for n ≥ 4 the
chart imposes genuine extra conditions (H₃₁ = H₄₁ = H₄₂ = 0), which is where (OC_n) differs from (S′).
**(OC₄) COMPUTED (codex C verifier):** all 24 261 120 matrices of GL(4,3) (505 440 orbit representatives
under right permutation × scaling, matching |GL|/(24(q−1))) and all 2 961 100 800 of GL(4,4)
(41 126 400 representatives) admit (P, u); Python screens of 2×200 000 random matrices agree; controls
in `controls.log`. Not replicated by me (GL(4,4) is out of local reach; GL(4,3) replicable later in C).
Status: (OC₃) PROVED (engine + my re-derivation); (OC₄) over GF(3), GF(4): engine-COMPUTED.

## R6.83 · RUN 5 (naive rank-two ideal, GF(2)) OOM at 54.9 GB after 49 min — UNRESOLVED-due-to-load; RUN 6 (chart-reduced) launched 23:03 CDT
Harvest `engine/harvest/k1695_r6_gcp5/` (r2_main_p2.err/.out/.status, runner.log): `rc=143 seconds=2966
mem=54G`; the F4 table (degrees 5–7, 6000-pair rounds, pair queue > 1.1 M, matrices to 165 689 ×
1 768 580) is in the .err. Verdict: nothing about 16.95 follows. Dialogue deleted k1695-r6-r2 at
04:03:24Z and launched **run 6** `k1695-r6-r2c` (e2-highmem-8, prefix k1695_r6f) at 04:03:40Z with the
chart-reduced inputs (36 variables; §R6.79) — same terms (no caps, 5-day backstop). Readings §R6.79.

## R6.84 · K6-U2CENSUS (codex7) GRADED: 13.46 M structured/random state visits at n = 6, 7 — 10 633 kd-local maxima, 25 (2Step) failures, 12 strict local maxima, ZERO U2 failures
`engine/harvest/k1695_r6_u2census/` (DONE-u2census, REPORT.md, summary.json, census_table.tsv,
aggregate.log, independent_all.log). Controls reproduce M (kd 5, neutral (1,5),(2,5),(3,5), ν 8/4/4),
C and T exactly (controls.log); cells: rank-one perturbations of permutation matrices at n = 6 over
GF(2) EXHAUSTIVE (63² bases × 720 permutations, 1 406 160 invertible visits), seven more rank-one/two
cells over GF(2)/GF(3)/GF(4) at n = 6, 7 with 10⁶ samples each, four random-GL cells (10⁶ each), and
the full right-permutation orbits plus single-column changes of M, C, T. Result: no radius-2 local
maximum anywhere (U2 witness streams empty; re-verified by independent_check.py). Consistent with
Pro's ≈8.8·10⁸ visits (§R6.76). Grade: engine-COMPUTED evidence for U2; (2Step)/strict failures are
now common (25 / 12 in this census) while U2 has none. Per §R6.76 U2 stays a recorded conjecture,
not a route.
**Ticket K6-LEAN9 (23:0x CDT)** `engine/briefs/k1695_r6_lean9/TICKET.md`: close R1 in Lean (rank ≥ n − 1 at
every μ of an algebraic closure ⟹ minpoly = charpoly) and assemble `stratumB_minpoly` — the
kernel-checked 16.95 for stratum (b) at n = 4 — on a free sol screen (one ≈6 GB lake process).
#6 gc4r2cert: WAIT (naive rank-two systems need > 54 GB; re-issue in chart form if run 6 fits).
**Tickets 23:07 CDT:** K6-R2HAND (`engine/briefs/k1695_r6_r2hand/TICKET.md`) — 16.95 on the rank-two
stratum at n = 4 by hand (Lemma T + Woodbury rank-drop criterion for non-eigenvalue t; partial credit
characteristic 2 / W = U); K6-GC4EQ (`engine/briefs/k1695_r6_gc4eq/TICKET.md`) — classification of the
(GC₄) minimizers on the low-rank stratum from codex5's GF(3) scan, tested over GF(7)/GF(9). Both light.
**§R6.83 run-6 early profile (23:16 CDT, 10 min):** the chart-reduced rank-two ideal shows the same
explosive pattern — degree 6 rounds with 3 000–4 400 new basis elements each, pair queue 470 k, matrix
67 990 × 360 570, RSS 12.7 GB of 54 GiB at 8 min (run 5 at the same stage: ≈275 k pairs / 28 GB at 18 min —
so somewhat slower growth, but the same shape). **Run 4:** degree-12 round 11 running, RSS 47.7 GB.
Run 3's lift: 11 h 33 min, 0.94 GB.

## R6.85 · K6-R2HAND (codex7) GRADED: honest partial — correct rank-two rank-drop lemmas, a proved sub-stratum, and decisive NEGATIVE data (no cycle-type-uniform witness on the rank-two stratum)
`engine/harvest/k1695_r6_r2hand/PROOF.md` + scripts/logs. **PROVED (re-derived):** Lemma 1 — for
invertible M and n×r U, V: rank(M + UVᵀ) = n − r + rank(I_r + VᵀM⁻¹U) (bordered-matrix argument; for
n = 4, r = 2: rank ≤ 2 ⟺ I₂ + VᵀM⁻¹U = 0, and then the rank is exactly 2); Lemma 2 — corank-one M:
rank(M + UVᵀ) = n − 3 + rank K with K = [[0, qᵀU], [−Vᵀp, I₂ + VᵀM⁺U]] (a 3×3 bordered block) — the
correct rank-two replacement of Lemma T's corank-one criterion; the 4-cycle non-eigenvalue equations
E_P(t) = (1 − t⁴)I₂ + Wᵀ(I + tP³ + t²P² + t³P)U = 0 (from (P − tI)⁻¹ = (P³ + tP² + t²P + t³)/(1 − t⁴));
the **support-pair theorem**: if A ≅ diag(B, I₂) after simultaneous permutation (rows of U and W
supported on the same pair) then some AP_σ is cyclic over every field — via the block matrices
T_C = [[0, C], [I₂, 0]], cyclic whenever C is non-scalar (Krylov vectors (0,v),(Cv,0),(0,Cv),(C²v,0)),
using C = B or C = BJ. **COMPUTED (exhaustive GF(3), rank exactly 2, 477 750 matrices):** 192 have all
six 4-cycles bad, 128 all eight 3-cycles bad, 12 both (witness (8): rows 0211/0010/0100/1120, rescued
by four transpositions and two double transpositions); 0 all-bad. So the natural intermediate lemmas
"some 4-cycle works" / "some 3-cycle works" are FALSE on the rank-two stratum — together with the
N4n odd-characteristic all-transpositions-fail families, a proof must select the witness type
adaptively. **UNRESOLVED:** the arbitrary-field rank-two theorem, char 2, W = U, one-zero-row.
Grade: correct and useful; no new banked theorem beyond the sub-stratum; the negative data are the
valuable part and are recorded as constraints on any future proof.

## R6.86 · MILESTONE — Kourovka 16.95 on stratum (b) at n = 4 is KERNEL-CHECKED (Lean 4 / Mathlib, my own recompilation): `K1695.stratumB_minpoly`
Files `lean/proofenv/K1695/StratumBAssembly.lean` (codex LEAN8, §R6.80), `RankToMinpoly.lean` and
`StratumBMinpoly.lean` (codex LEAN9). **My checks** (23:27–23:28 CDT, `logs/k1695/round6_lean9_*`): each
source file recompiled from scratch with `lake env lean` — 0 errors (12 / 7 / 5 s, peak ≈6.2 GB); an
importing check file reports `K1695.stratumB_minpoly`, `K1695.minpoly_eq_charpoly_of_rank_ge_four`
(R1) and `K1695.stratumB_rank_form` depend only on [propext, Classical.choice, Quot.sound]; no
sorry/admit/native_decide in the files. **Statement (verified):** `theorem stratumB_minpoly {F} [Field F]
(A : Matrix (Fin 4) (Fin 4) F) (hA : IsUnit A.det) (m : F[X]) (hm : Irreducible m) (hdeg : m.natDegree = 2)
(hmin : minpoly F A = m) (a b : Fin 4) (hab : a ≠ b) : minpoly F (A * Matrix.swap F a b) = (A * Matrix.swap
F a b).charpoly` — for every field, every invertible 4×4 matrix whose minimal polynomial is an
irreducible quadratic, EVERY transposition makes A·P_τ cyclic; i.e. 16.95 holds on stratum (b) at n = 4,
with the stronger "every transposition" conclusion (§R6.3). R1 is proved via the algebraic closure
(`minpoly_eq_charpoly_of_rank_ge_four_algClosed`: rank(B − μ) ≥ 3 for all μ ∈ L algebraically closed ⟹
one Jordan block per eigenvalue ⟹ minpoly = charpoly; then descent to K). **Status: BANKED, kernel-
checked** — the first kernel-checked n = 4 statement on the line (previously: hand + notebook + cross-
family). Lean assets now: n ≤ 3 (16.95 + (GC₃)), Lemma T, stratum (b) at n = 4.
**Ticket K6-R2CHAR2 (23:30 CDT)** `engine/briefs/k1695_r6_r2char2/TICKET.md`: rank-two stratum at n = 4 in
characteristic 2 by hand (single eigenvalue 1 for 2-/4-cycles; R2HAND lemmas L1–L4; reduce to a finite
check if possible) — would give 16.95 at n = 4 over every field of characteristic 2. Dispatched to a
free sol screen.
**§R6.83/§R6.61 progress 23:47 CDT:** run 6 (chart) at 38 min: degree 6, pair queue 1.05 M, matrix
130 923 × 711 557, RSS 48.4 GB of 54 GiB — OOM imminent; run 4: degree-12 round 12 (165 850 × 724 812),
RSS 51.8 GB of 54 GiB — also near its scope; run 3's lift 12 h 04 min.

## R6.87 · K6-R2CHAR2 (codex) GRADED: honest partial — all-coranks rank formula, unbounded finite-field descent, an explicit obstruction to "parameter descent", and GF(2)-exhaustive negative data on the exact rank-two stratum
`engine/harvest/k1695_r6_r2char2/PROOF.md` + scans/audits. **PROVED (re-derived):** Lemma 1 — for M of
rank g and n×2 U, V, with bases making M = diag(I_g, 0): rank(M + UVᵀ) = g − 2 + rank K_c, K_c =
[[0_c, U₁], [−V₁ᵀ, I₂ + V₀ᵀU₀]] (bordered matrix; c = n − g) — R2HAND's Lemmas 1–2 are c = 0, 1; for
n = 4 "rank ≤ 2 ⟺ rank K_c ≤ 4 − g", with the characteristic-2 table at the sole eigenvalue t = 1
(corank 4/3/2/2/1 for identity / transposition / double transposition / 3-cycle / 4-cycle). Descent: an
all-bad presentation over any characteristic-2 field yields one over some GF(2^m) (Nullstellensatz;
no bound on m) — correct, not performable. **Obstruction to the GF(2)/GF(4) reduction:** over F₂(s),
U = (e₀, e₁), Wᵀ = [[1, s, 0, 0], [s³, 1, 0, 0]] gives A = diag([[0, s], [s³, 0]], I₂) with AP bad at the
transcendental t = s for the 4-cycle P — so bad parameters need not lie in a small field (this A is in
the support-pair stratum and has other good permutations). **COMPUTED (GF(2), all 65 536 (U, W); 15 540
invertible exact-rank-two presentations; two independent oracles agree):** all 4-cycles bad: 108; all
3-cycles bad: 102; both: 36 (witness rows 0111/1011/0001/0010, rescued by four transpositions and two
double transpositions); all double transpositions bad: 444; **all six transpositions bad: 0**; no all-bad;
min g = 6 in every rank class. GF(4) 10⁶ sample: no all-bad; 15 presentations with all transpositions
bad (so "some transposition works" is NOT a characteristic-2 lemma either), none with all 3- and
4-cycles bad (sampled only). **UNRESOLVED:** the theorem in characteristic 2; one-zero-row; W = U.
Grade: correct, no new theorem; the transcendental example is a genuinely useful "why not" — it kills
the hope that inseparability alone confines the bad parameter.

## R6.88 · K6-GC4EQ (codex10) GRADED: equality cases of (GC₄) on the low-rank stratum — two classes in characteristics 2, 3, three otherwise (conjecture, consistent with every dataset)
`engine/harvest/k1695_r6_gc4eq/REPORT.md` + TSV/JSON lists + audit PASS. Symmetry used (PROVED, correct):
A ↦ aQAP and A ↦ aQAᵀP preserve g. Under it the exhaustive GF(3) minimizers (237) and GF(2) minimizers
(168) each fall into exactly TWO classes: **scalar-permutation** (aP; good types 4×(2,1,1) + 2×(4) for
the canonical P₀) and **two-support** (orbit of T = P₀ + zzᵀ, z = e₃ − e₄: permutation plus a rank-one
term with both factors supported on the same two coordinates, opposite values there (equal in
characteristic 2); good types (1⁴) + 2×(2,1,1) + (2,2) + 2×(4)); over GF(7) (rank 0/1 exhaustive) a
third **dense** class I + γJ with 1 + 4γ a primitive cube root (two representatives, distinct under the
symmetry); GF(4)/GF(5)/GF(9) sample hits and my F₅ witness u = (4,0,1,0), w = (1,1,4,4) all lie in these
classes; GF(7) exact-rank-two sample (2.18 M): min g = 10, no equality. **Conjecture (recorded):** over
an algebraically closed field the g = 6 cases up to the symmetry are scalar-permutation and
two-support in characteristics 2 and 3, plus the dense class in every other characteristic. Controls
match my numbers. Grade: engine-COMPUTED classification + conjecture; consistent with §R6.64/§R6.69.
**Ticket K6-LEAN10 (23:5x CDT)** `engine/briefs/k1695_r6_lean10/TICKET.md`: generalise the kernel-checked
stratum-(b) theorem (§R6.86) and R1 from Fin 4 to every even n (invariant factors (m, m), m irreducible
of degree n/2 — the hand theorem of §R6.3); partial credit n = 6.

## R6.89 · RUN 6 (chart-reduced rank-two ideal, GF(2)) OOM at the 54 GiB scope after 54 min, in the DEGREE-6 layer — UNRESOLVED-due-to-load; VM harvested and deleted; F4 verdict for the review
Harvest `engine/harvest/k1695_r6_gcp6/` (r2_main_chart_p2.err/.out/.status, runner.log, serial.log):
`rc=143 seconds=3249 mem=54G` (04:06:26Z → 05:00:37Z); last round degree 6, 130 923 × 711 557 (0.41 %),
4 822 new / 1 179 zero, pair queue ≈1.05 M. The chart normalisation (36 variables) removed four variables
but not the combinatorial explosion: the ideal generates thousands of new degree-6 elements per round.
VM `k1695-r6-r2c` deleted by me at 00:0x CDT (8 vCPUs free; its lift was redundant with runs 3/4).
Run 3: p = 5 also OOM at 23 GiB after 4 h (dialogue's monitor; p = 7 next, same fate; lift continues).
**F4 verdict (for the 08-30 review):** the Gröbner route to 16.95 at n = 4 is memory-dead on 64 GB in
all three formulations — the (S′)₄ Ω-ideal (16 vars: degree 12 exceeds 54 GB with a 200 k-pair queue
still growing, runs 3/4), the naive rank-two ideal (40 vars: degree 7, run 5) and the chart rank-two
ideal (36 vars: degree 6, run 6). A 128 GB machine (n2-highmem-16, 16 vCPUs = the whole free quota)
would buy ≈2.3× on curves that grow ≥ 3× per layer — not a predictable finish; recommendation: STOP
F4 on these ideals, delete run 4 after its lift is harvested or judged hopeless, keep only the lifts
if they are near completion. The productive computational form this week was the CERTIFICATE
scheme on small subsystems (§R6.75); the rank-two stratum needs a hand argument (R2HAND/R2CHAR2
data) or a smarter decomposition (case split on which permutations are bad at eigenvalues vs.
non-eigenvalues, each sub-ideal small), not a bigger machine.

## R6.91 · K6-LEAN10 (codex) GRADED: general R1 KERNEL-CHECKED (my own recompilation); the general stratum-(b) theorem reduced to one root-rank premise (honest partial); a wrong formula in my ticket corrected by the engine
`engine/harvest/k1695_r6_lean10/REPORT.md`; files `RankToMinpoly.lean` (refactored: `K1695.minpoly_eq_
charpoly_of_rank_ge (n) (B : Matrix (Fin n) (Fin n) K) (h : ∀ L [Field L] [Algebra K L] (μ : L), n − 1 ≤
rank(B.map − μ•1)) : minpoly K B = B.charpoly`, plus `rank_map_sub_scalar_eq_of_not_isRoot_map_minpoly`)
and `StratumBMinpolyGeneral.lean` (assembly for arbitrary n from the all-scalar rank form; even n;
"suffices at roots"; `stratumB_minpoly_general_of_root_rank`). **My checks** (00:14–00:27 CDT, box under
load 18): the three sources recompile with 0 errors (258 / 181 / 125 s); `#print axioms` for
`K1695.minpoly_eq_charpoly_of_rank_ge`, `K1695.stratumB_minpoly` (regression after the refactor) and
`K1695.stratumB_minpoly_general_of_root_rank` = [propext, Classical.choice, Quot.sound]; no
sorry/admit/native_decide. **Status:** R1 for every n is BANKED (kernel-checked); the general stratum-(b)
minpoly theorem is conditional on the root-rank lemma (rank(A·P_τ − μ) ≥ n − 1 at roots μ of m), which
the engine did NOT prove — the Fin 4 proof used quadratic power-basis identities that do not
generalise by index change. **Correction of my own ticket:** I wrote "A − μ has rank n − k" for the root
case; the correct value for n = 2k with invariant factors (m, m) is 2k − 2 (geometric multiplicity 2 at
every root), which coincides with n − k only at k = 2 — the engine's remark is right and my phrase was
wrong (the hand proof of §R6.3 uses multiplicity 2, not n − k).

## R6.90 · DAILY REVIEW 2026-08-30 (drafted 00:3x CDT for the ≈11:00 go/no-go) — cloud F4 routes STOP; codex-day summary
**Cloud (owner rule §R6.61: no caps, daily go/no-go):** (1) Ω-ideal (S′)₄, runs 3/4: run 3 OOM at 23 GiB
for p = 2, 3, 5 (degree 12 each; p = 7 in progress, same fate); run 4 at 51.8 GB of 54 GiB after 8.2 h,
degree-12 rounds 1–12 with the basis still growing ≈2 700/round and a 227 k pair queue — **NO-GO:
stop**; the layer-to-layer growth (≥ 3×) outruns any machine the quota allows. (2) Rank-two ideals,
runs 5/6: OOM at 54 GB in degree 7 (naive, 40 variables) and degree 6 (chart, 36 variables) — **stopped
and deleted** (§R6.83, §R6.89). (3) Lifts (rank-one cofactor certificate for all characteristics): run 3's
lift 12 h 34 min, run 4's ≈8 h, both uncapped at ≈1 GB; the local capped attempts and the earlier VM
attempts never finished — **keep run 3's lift alone** (cheapest: 4 vCPU, $0.18/h) and delete run 4
after harvesting its .err curve (its lift duplicates run 3's); re-review the lift at the next daily
review; if still running on 08-31, stop it — the all-characteristic upgrade of a rank-one lemma is not
worth an open-ended $4/day. **VM actions at the review:** harvest run 4 → engine/harvest/k1695_r6_gcp4/,
delete `k1695-r6-groebner4`; keep `k1695-r6-groebner3` (lift) until 08-31. Cost so far (list price):
run 1 ≈$0.6, run 2 ≈$0.2, run 3 ≈$0.18/h × ≈24 h ≈ $4.3, run 4 ≈$0.36/h × ≈16 h ≈ $5.8, run 5 ≈$0.3,
run 6 ≈$0.3 — total ≈$11.5 of the ≈$90 credit.
**Codex day (08-29 21:3x → 08-30, owner directive §R6.77) — banked:** (GC₃) kernel-checked
(§R6.81); 16.95 on stratum (b) at n = 4 kernel-checked (§R6.86); R1 for every n kernel-checked (§R6.91);
N4x independent confirmation of rank one at n = 4 (§R6.78); (OC₃) proved + (OC₄) exhaustive over GL(4,3),
GL(4,4) (§R6.82); rank-one (GC₄) certificates in characteristics 0, 2, 3, 5, 7, 11, 13 (§R6.75, my own
encoder). **Refuted today:** (Mono) (§R6.73), (2Step) and (2Step′) (§R6.76), the face-matching lemma
(§R6.69), the derangement conjecture (§R6.66), Theorem 2 of K6-GC3 (§R6.69), cycle-type-uniform witness
lemmas on the rank-two stratum (§R6.85, §R6.87). **Open:** the rank-two stratum of 16.95 at n = 4 (the
whole residual of n = 4), (GC₄) beyond rank one (conjecture, strong evidence, classification conjecture
§R6.88), U2 (evidence only, not a route), (OC_n) for n ≥ 4 over arbitrary fields, the general
stratum-(b) root-rank lemma in Lean. **Next moves (in order):** (a) rank-two stratum by hand with the
R2HAND/R2CHAR2 toolkit and a case decomposition into SMALL sub-ideals (which permutations are bad at
eigenvalues vs non-eigenvalues), certified per case like §R6.75 — the productive computational form;
(b) Lean: the root-rank lemma for general even n; (c) (GC₄) rank-two certificates only in the
decomposed form. Nothing is SOLVED; nothing published.
**§R6.61 progress 00:59 CDT:** run 4 degree-12 round 13 done (183 135 × 776 771, 2866 new / 134 zero,
3591 s), round 14 running, RSS 55.7 GB (≈51.8 GiB of the 54 GiB scope) at 9.0 h — at the edge; run 3:
lift 13 h 24 min, runner on p = 7 (15 GB, doomed). No new harvests for this line.

## R6.92 · RUN 4 (Ω-ideal, 54 GiB, 8 threads) OOM after 9.26 h in degree-12 round 14 — UNRESOLVED-due-to-load; VM harvested and deleted; the F4 route is closed (review item executed early)
Harvest `engine/harvest/k1695_r6_gcp4/` (sprime4r_p2.err/.out/.status, runner.log, liftQ.*, serial.log):
`rc=143 seconds=33333 mem=54G`. Degree-12 table on 54 GiB (rounds of 3000 pairs): rows 130 k → 198 k →
196 k → 203 k → 262 k → 412 k → 141 k → 150 k → 155 k → 166 k → 183 k → … with 1 600–3 000 new basis
elements per round and 100–2 900 reductions to zero, pair queue 72 k → 254 k, RSS 14 → 56 GB over
9 h; the degree-12 layer was nowhere near saturation when the scope ran out. Run 3 had died at 24 GB in
round 4 of the same layer (§R6.68). Conclusion (already drafted in §R6.90): the (S′)₄ Ω-ideal is out of
reach for F4 on any machine the quota allows; nothing about (S′)₄ or 16.95 follows. VM
`k1695-r6-groebner4` DELETED by me at 01:3x CDT (its lift, ≈9.5 h, duplicated run 3's, now 13.9 h).
Remaining cloud footprint: `k1695-r6-groebner3` only (4 vCPU, ≈$0.18/h) for its lift, until the 08-31
review at the latest.
**Ticket K6-R2SPLIT (01:3x CDT)** `engine/briefs/k1695_r6_r2split/TICKET.md`: the rank-two stratum by case
decomposition — per permutation the cases "bad at eigenvalue t" (t-free polynomial conditions via the
bordered rank formula) and "bad at a non-eigenvalue" (Woodbury 2×2 = 0 with t a variable), a DPLL-like
branch search with one small msolve certificate per closed branch (≤ 2.5 GB, seconds each), controls =
the actual case pattern of a concrete rank-two A must be consistent; characteristic 2 first. Dispatch
when the box is quiet (next move (a) of §R6.90).

## R6.93 · K6-R2SPLIT (codex2) CLAIMS the exact-rank-two stratum in characteristic 2 by 255 small certificates — my independent re-check LAUNCHED (own encoder, full enumeration, no symmetry reduction)
`engine/harvest/k1695_r6_r2split/REPORT.md` + certificates/ + verify_certificates.py. Claim: over every
field of characteristic 2, every A = I + UWᵀ with rank UWᵀ = 2 has a cyclic AP_σ among the six
transpositions and (12)(34); proof = for every U-chart (which two rows of U are independent) and every
assignment of a badness case (E₁: bad at the eigenvalue 1 — all 3×3 minors of AP_σ + I vanish; N: bad
at a non-eigenvalue t — Woodbury χ(t)I₂ + W_σᵀ adj(P_σ − tI)U = 0 with χ(t) ≠ 0) to those seven
permutations, the ideal (with det(I₂ + WᵀU)·za − 1 and the U-minor saturation) is unit over GF(2); DPLL
on three symmetry-representative U-charts, 255 msolve runs, 222 unit terminals, replay verifier,
negative control = the realised pattern of a concrete matrix (non-unit). **Logic audited by me:** in
characteristic 2 the only eigenvalue of a transposition or double transposition matrix is 1, so
"bad ⟺ E₁ ∨ N" is exhaustive; rank R = 2 ⟹ rank U = rank W = 2, so the W-chart + six U-charts cover
the exact-rank-two stratum; rank ≤ 1 is the certified rank-one stratum (§R6.42/§R6.78, p = 2 included);
every all-bad A normalises to I + (rank ≤ 2) (§R6.66). Hence, IF the certificates hold, **Kourovka
16.95 is true for n = 4 over every field of characteristic 2**. **My re-check** (`round6_r2split_check.py`,
own encoder written from the criteria, not from their code): controls pass (all-transposition-E₁
conjunction unit; the realised pattern of A₀ = rows 0111/0001/1101/0100 — bad (13), (24) both E₁ — non-
unit); full enumeration running: all six U-charts × all 128 case assignments = 768 ideals, each must be
unit (`logs/k1695/round6_r2split_check_full.log`, summary.json). Readings: 768/768 unit → §R6.94 BANKS
"16.95 at n = 4 in characteristic 2" as COMPUTED, two families (codex DPLL certificates + my full
enumeration) — not SOLVED (n = 4 other characteristics and all n ≥ 5 remain); any non-unit assignment
→ a candidate all-bad configuration: solve and test by hand before anything is said.

## R6.94 · BANKED (COMPUTED, two independent encoders): KOUROVKA 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 2
**Statement.** For every field F with char F = 2 and every A ∈ GL(4,F) there is a permutation matrix P
with AP cyclic (minpoly = charpoly). **Proof structure.** (1) If all 24 AP_σ were non-cyclic, A itself
would have an eigenvalue λ ≠ 0 of geometric multiplicity ≥ 2, so λ⁻¹A = I + R with rank R ≤ 2 (§R6.66;
scaling and the family {AP_σ} commute). (2) rank R ≤ 1: the rank-one stratum has a good permutation
in every characteristic < 10⁴, in particular 2 — three encodings, two families (§R6.42, §R6.78, §R6.77
control). (3) rank R = 2: write R = UWᵀ with rank U = rank W = 2; conjugating by a coordinate permutation
(which conjugates the family {AP_σ}) and re-gauging the factorisation puts W = [I₂; w] (W-chart); the
six U-charts det U[{i,j},:] ≠ 0 cover rank U = 2. For each of the seven permutations {(12), (13), (14),
(23), (24), (34), (12)(34)} the only eigenvalue of P_σ in characteristic 2 is 1, so "AP_σ non-cyclic" is
exactly (E₁) all 3×3 minors of AP_σ + I vanish, OR (N) ∃t: χ_σ(t) ≠ 0 and χ_σ(t)I₂ + W_σᵀ adj(P_σ − tI)U = 0
(Woodbury: for invertible M, rank(M + UVᵀ) ≤ 2 ⟺ I₂ + VᵀM⁻¹U = 0). For every U-chart and every one of
the 2⁷ assignments of cases to the seven permutations, the ideal ⟨det(I₂ + WᵀU)·za − 1, det U[{i,j}]·zu
− 1, case generators⟩ over GF(2) is the UNIT ideal — so no point over F̄₂ (hence over any field of
characteristic 2, by the Nullstellensatz and extension) makes all seven bad; some AP_σ is cyclic. ∎
**Certificates.** codex2 (K6-R2SPLIT, §R6.93): DPLL over three symmetry-representative U-charts, 255
msolve runs, 222 unit terminals, independent replay. **Mine** (`problems/k1695/round6_r2split_check.py`,
encoder written from the criteria; `engine/harvest/k1695_r6_r2split_check/`, 770 .gb files;
`logs/k1695/round6_r2split_check_full.log`): all six U-charts × all 128 assignments = 768 ideals, every
basis = [1] (verified file by file), 295 s, peak 1.1 GB; controls: all-transposition-E₁ core unit; the
realised pattern of A₀ = rows 0111/0001/1101/0100 non-unit. Solver shared (msolve 0.10.1 −g 2 over
GF(2)); encoders independent; finite-field agreement: GL(4,2), GL(4,4) exhaustive (§R6.20 era). **Status:**
BANKED as COMPUTED — not a Lean theorem, not "SOLVED" (16.95 is for all n and all fields; n = 4 in odd
characteristic and characteristic 0 remains open, as does every n ≥ 5). Interesting corollary: in
characteristic 2 the witness can always be taken among the six transpositions and (12)(34) when
rank(A − λI) = 2 — the "transposition-only" idea (refuted in general, §R6.42 N4n odd-characteristic
families) survives in characteristic 2 on the rank-two stratum. Next: characteristics 3, 5, 7 by the
same decomposition (their case inventories exist; more cases per permutation: E_{±1}, E_{±i}, E_ω…).
**Progress 02:26 CDT:** run 3's lift 14 h 45 min (1.05 GB), its p = 7 msolve at 23.5 GB (about to OOM,
harmless); K6-R2SPLIT-357 running on codex2 (control files for p = 3, 5, 7 written; trees in progress).

## R6.95 · Own odd-characteristic decomposition encoder (`round6_r2split_odd.py`) — controls pass; DPLL for p = 3 launched in parallel with codex2's K6-R2SPLIT-357
Cases: E_r for every eigenvalue r of P_σ over F̄_p (2-cycles/double transpositions {1, −1}; 3-cycles
{1, ω, ω²} with ω adjoined via ω² + ω + 1 = 0 when p ≢ 1 mod 3 and ω = 1 for p = 3; 4-cycles {1, −1, ±i}
with i adjoined via i² + 1 = 0 when p ≢ 1 mod 4) and N (Woodbury with χ ≠ 0); DPLL over the permutations
in the order transpositions → double transpositions → 3-cycles → 4-cycles; msolve per node under the
2.5 GB cap. Controls over GF(3), U-chart {1,2}: the realised pattern of A₀ = rows 0001/1212/0010/0221
(eight bad non-4-cycles, all at eigenvalue 1) is NON-unit ✓; the all-transposition-E₁ conjunction is
UNIT — consistent (the odd-characteristic all-transposition-fail families of N4n are bad at mixed
eigenvalues/non-eigenvalues, not all at 1); my in-script "expected False" label for that probe was
over-strong. Running: p = 3, chart 0 (`logs/k1695/round6_r2split_odd_p3_chart0.log`).
**§R6.95 update (02:5x CDT):** my p = 3 DPLL hit the 2.5 GB cap at a SHALLOW node (`d_N_E1`: only two
transpositions assigned, 16 variables, 23 generators, yet > 2.5 GB) — UNRESOLVED-due-to-load, no
evidence. Lesson: partial assignments leave a large positive-dimensional ideal whose full Gröbner basis
is expensive; the characteristic-2 enumeration was fast only because every ideal was a FULL leaf (all
seven permutations assigned, unit). codex2's char-2 DPLL started at depth 6 for the same reason.
Re-check strategy for odd p: replicate the engine's closed tree node by node (full leaves) rather than
run my own DPLL from the root; wait for K6-R2SPLIT-357's report.
**Progress 03:29 CDT:** K6-R2SPLIT-357 in progress on codex2 (p = 3 states for charts 0, 1, 5 being
written; no DONE); run 3: msolve sequence finished (p = 7 OOM after 11 843 s; all four primes died at
degree 12 under 23 GiB) — the VM now carries only the uncapped lift (15 h 46 min, 1.48 GB).

## R6.96 · K6-R2SPLIT-357 (codex2) CLAIMS characteristics 3, 5, 7 closed (7 117 certificates) — my full independent replication (own encoder, own DPLL, all six U-charts) LAUNCHED; first tree matches
`engine/harvest/k1695_r6_r2split357/REPORT.md` + certificates/ + verify. Claim: for p ∈ {3, 5, 7}, every
exact-rank-two A = I + UWᵀ over any field of characteristic p has a cyclic AP_σ; trees start after all
six transpositions are assigned (3 cases each: E₁, E₋₁, N), extend by the three double transpositions
and, where needed, one to three 3-cycles ((234), (243), (123)); max depth 10–12; 757/752/763 (p = 3),
824/807/785 (p = 5), 826/806/797 (p = 7) runs on the three symmetry-representative U-charts; max 11.5 s
and 1.2 GB per run; replay verifier passes; controls: realised patterns (incl. the §R6.85 GF(3) witness
and the N4n GF(7) Klein-four matrix, with four N cases) NON-unit. **Control judgement (dialogue's
question):** the ticket's expectation that "all six transpositions bad at E₁" is non-unit in odd
characteristic was MY error (§R6.95): the N4n all-transposition-fail families are bad at MIXED cases
(E₋₁ / N), and the simultaneous all-E₁ subcase is indeed empty on the exact-rank-two chart; the E₁
generators are exactly "rank(AP_σ − I) ≤ 2" (all 3×3 minors) — not stronger than intended — and the
realised-pattern controls (which contain many E₁ cases) are non-unit, so E₁ is satisfiable by real
points. Case exhaustiveness (bad ⟺ ∨_r E_r ∨ N over the eigenvalue set of P_σ) is correct for every
cycle type and p. **My replication** (`round6_r2split_odd.py --start-depth 6`, §R6.95 encoder; all SIX
U-charts, no symmetry argument; logs `logs/k1695/round6_r2split_odd_p{3,5,7}_chart{0..5}.log`): p = 3
chart 0 finished — 759 runs, 747 closed, 0 OPEN leaves, 0 capped, 116 s — matching codex's 757/747.
The remaining 17 trees run sequentially (≈1–2 h). Readings: all 18 trees with 0 OPEN and 0 capped →
§R6.97 BANKS "16.95 at n = 4 over every field of characteristic 3, 5, 7" (COMPUTED, two families);
any OPEN leaf → candidate all-bad configuration (solve, test the point over an extension with own
code, disclosure protocol); capped → UNRESOLVED for that tree.

## R6.97 · BANKED (COMPUTED, two independent encoders + two independent searches): KOUROVKA 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 3 AND OF CHARACTERISTIC 5 (characteristic 7 replication in progress)
Same proof structure as §R6.94 (normalisation to I + R, rank ≤ 1 certified in every characteristic
< 10⁴, rank 2 covered by the W-chart and the six U-charts), with the odd-characteristic case
inventory of §R6.95 (E_r for every eigenvalue r of P_σ over F̄_p, with ω/i adjoined as variables where
absent from GF(p), plus N). **My replication** (`round6_r2split_odd.py --start-depth 6`, all SIX
U-charts, own DPLL over the order transpositions → double transpositions → 3-cycles → 4-cycles):
p = 3 — charts {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}: 759/754/754/754/754/765 msolve runs, 747/744/744/
744/744/751 closed branches, 0 OPEN leaves, 0 capped, 95–116 s each; p = 5 — 826/809/809/793/793/787
runs, 795/783/783/771/771/767 closed, 0 OPEN, 0 capped, 132–182 s each. In every tree the assigned
permutations never went beyond the nine (2,1,1)/(2,2) permutations plus a few 3-cycles (max depth
≤ 12), so in characteristics 3 and 5 a witness for exact-rank-two A always exists among
transpositions, double transpositions and 3-cycles. codex2's trees (§R6.96) agree on the
representative charts (757/747, 752/744, 763/751 for p = 3; 824/795, 807/783, 785/767 for p = 5).
**Status:** BANKED as COMPUTED — not Lean, not SOLVED. p = 7: chart {1,2} replicated (828 runs / 795
closed / 0 open / 0 capped); charts {1,3}…{3,4} running (§R6.98 when complete).

## R6.98 · BANKED: 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 7 — hence n = 4 is COMPUTATIONALLY CLOSED in characteristics 2, 3, 5, 7 (§R6.94, §R6.97, §R6.98)
p = 7 replication (own encoder + own DPLL, all six U-charts): charts {1,2}, {1,3}, {1,4}, {2,3}, {2,4},
{3,4}: 828/808/808/808/808/799 msolve runs, 795/781/781/781/781/775 closed branches, 0 OPEN leaves,
0 capped, 138–195 s each; codex2's representative charts: 826/795, 806/781, 797/775 — agreement. Grand
total of my odd-characteristic replication: 18 trees, ≈14 200 msolve runs, every terminal basis [1],
no cap. **Consolidated statement (n = 4):** for every field F of characteristic 2, 3, 5 or 7 and every
A ∈ GL(4,F) some AP_σ is cyclic. Proof = normalisation (§R6.66) + rank ≤ 1 certificates (§R6.42/§R6.78,
three encodings) + exact-rank-two case-decomposition certificates (this section; two encoders, two
searches, full chart cover on my side). In all four characteristics the witness for exact-rank-two A
lies among transpositions, double transpositions and 3-cycles; 4-cycles were never needed to close a
branch. **Not covered:** characteristic 0 and characteristics ≥ 11 at n = 4 — the same decomposition
over ℚ (msolve char 0) would settle characteristic 0; "all characteristics" needs ℤ-content of the
certificates or a uniform argument. NOT SOLVED (n ≥ 5 entirely open); not Lean; not published.

## R6.99 · CHARACTERISTIC 0 at n = 4 — my decomposition encoder adapted to ℚ (msolve char 0); controls pass; six-chart DPLL LAUNCHED
Changes for p = 0: −1 literal; ω and i adjoined as variables (ω² + ω + 1 = 0, i² + 1 = 0) — the
eigenvalue set of a 3-cycle is {1, ω, ω²} and of a 4-cycle {1, −1, ±i} over ℚ̄; no coefficient
reduction; msolve header characteristic 0. A unit ideal over ℚ means no point over ℚ̄ (Nullstellensatz),
hence none over any field of characteristic 0 (extension invariance). Controls (chart {1,2}): the
realised pattern of the integer matrix A₀ = rows (−1,0,−4,0)/(−1,−1,2,2)/(2,0,5,0)/(1,2,−2,−1) (exact rank
two; three bad non-4-cycles, all E₁, decided exactly over ℚ via rank[vec I, vec B, vec B², vec B³]) is
NON-unit ✓; the all-transposition-E₁ conjunction is unit (as in every characteristic). Running: p = 0,
charts 0…5 sequentially, `--start-depth 6`, run_capped 2.5 GB / 3 h per chart
(`logs/k1695/round6_r2split_odd_p0_chart{0..5}.log`). Readings: all six charts 0 OPEN / 0 capped →
§R6.100 banks "16.95 at n = 4 over every field of characteristic 0" (COMPUTED; one family until a codex
replicate); OPEN leaf → solve over ℚ̄ (msolve −P), test with exact sympy over the needed extension,
disclosure protocol; capped → UNRESOLVED (a VM runner with sympy + msolve if needed).

## R6.100 · BANKED (COMPUTED, one family so far): KOUROVKA 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 0 — hence n = 4 is closed in characteristics 0, 2, 3, 5, 7
My encoder over ℚ (§R6.99), all six U-charts, `--start-depth 6`: 828/808/808/808/808/799 msolve runs,
795/781/781/781/781/775 closed branches, 0 OPEN leaves, 0 capped, 113–168 s per chart (the tree shapes
coincide with p = 7, where i is likewise adjoined). Every unit terminal basis is [1]; non-unit
prefixes were extended and closed. With the normalisation (§R6.66), the rank ≤ 1 certificates in
characteristic 0 (§R6.42: msolve over ℚ; §R6.78 N4x over ℚ) and the exact-rank-two decomposition here:
**for every field of characteristic 0 (ℚ, ℝ, ℂ, all number fields, …) and every A ∈ GL(4,F) some AP_σ is
cyclic.** Second family: ticket K6-R2SPLIT-Q (`engine/briefs/k1695_r6_r2splitq/TICKET.md`) asks codex2
to replicate over ℚ with its own encoder. **n = 4 summary:** closed in characteristics 0, 2, 3, 5, 7;
open in characteristics ≥ 11 (finitely many primes — the ℤ-content of the certificates would settle all
at once; or run p = 11, 13, … one by one, ≈10 min each locally). NOT SOLVED (n ≥ 5); not Lean; not
published.
**§R6.100 file-level recount (05:13 CDT):** 4 859 .gb files for p = 0 = 12 control runs + 4 694 unit
terminals ([1] verified file by file) + 153 non-unit prefixes (each extended and closed; the script's
"runs − closed = 165" includes the 12 control runs). Launched p = 11 and p = 13 (six charts each,
sequential, same caps).

## R6.101 · BANKED (COMPUTED, one family): 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 11 (six charts closed:        6/6) AND CHARACTERISTIC 13 (six charts closed:        6/6)
Same decomposition (§R6.95 encoder; ω adjoined for p = 11 (11 ≡ 2 mod 3), i adjoined for p = 11 (≡ 3 mod 4);
p = 13: ω ∈ GF(13) (13 ≡ 1 mod 3), i ∈ GF(13) (≡ 1 mod 4)), `--start-depth 6`, all six U-charts:
p = 11 — 827/807/807/807/807/798 runs, 795/781/781/781/781/775 closed, 0 OPEN, 0 capped, 147–192 s per
chart; p = 13 — 827/807/807/807/807/(chart {3,4}) runs, 795/781/781/781/781/… closed, 0 OPEN, 0 capped.
The tree shapes are IDENTICAL for p = 0, 7, 11, 13 (and nearly so for 3, 5): the branch structure of the
decomposition is characteristic-independent for p ≥ 5 — strong evidence that the ℤ-content of the
certificates would close every characteristic at once (the only remaining n = 4 gap: p ≥ 17). Rank ≤ 1 in
these characteristics: §R6.42 (p < 10⁴) and §R6.78 (N4x, p ≤ 47). n = 4 now closed in characteristics
0, 2, 3, 5, 7, 11, 13 (one family for 0, 11, 13 so far; two families for 2, 3, 5, 7). NOT SOLVED; not Lean.
**§R6.101 completion:** p = 13 chart {3,4}: 798 runs, 775 closed, 0 OPEN, 0 capped (149 s) — p = 13 fully
closed (six charts). Launched p = 17 and 19 (same loop, one msolve at a time).

## R6.102 · §R6.100 UPGRADED TO TWO FAMILIES: characteristic 0 at n = 4 — codex2's independent ℚ encoder agrees (K6-R2SPLIT-Q)
`engine/harvest/k1695_r6_r2splitq/REPORT.md`: its own encoder extended to characteristic 0 (field line 0,
integer coefficients; "the line's characteristic-zero script was neither read nor reused"); three
symmetry-representative U-charts, 2 429 msolve runs, 2 351 unit prunes, 78 non-unit prefixes extended,
0 open leaves, 0 capped; realised-pattern control (integer exact-rank-two matrix, exact rational
classification) NON-unit on each chart; replay verifier. My six-chart run (§R6.100): 828/808/799 on the
same representatives (2 435) — agreement within the expected ±6 (case ordering). **n = 4 status:** closed
in characteristics 0, 2, 3, 5, 7 with TWO independent families each; 11 and 13 with one (mine); 17, 19
running. Next ticket for codex2: replicate p = 11, 13 (K6-R2SPLIT-1113) — light. NOT SOLVED (n ≥ 5); not
Lean; not published.

## R6.103 · BANKED (COMPUTED, one family): 16.95 HOLDS FOR n = 4 OVER EVERY FIELD OF CHARACTERISTIC 17 (6/6 charts) AND 19 (6/6 charts) — the same tree again
p = 17 (ω ∈ GF(17)? 17 ≡ 2 mod 3 → ω adjoined; i ∈ GF(17) since 17 ≡ 1 mod 4) and p = 19 (19 ≡ 1 mod 3 → ω ∈
GF(19); 19 ≡ 3 mod 4 → i adjoined): 827/807/807/807/807/798 runs, 795/781/781/781/781/775 closed, 0 OPEN,
0 capped per chart — the identical tree shape of p = 0, 7, 11, 13 for the fifth and sixth time. n = 4 is
now closed in characteristics 0, 2, 3, 5, 7 (two families), 11, 13, 17, 19 (one family). Remaining gap
at n = 4: primes ≥ 23 — each ≈15 min locally, but "all characteristics" needs the ℤ-content of the
certificates (a lift per unit terminal — ≈4 700 lifts, heavy) or a uniform argument explaining the
characteristic-independent tree (a real mathematical target now: the same 795/781/775 branch counts
suggest the decomposition's inconsistency proofs are characteristic-free polynomial identities).
**Tickets/launches 06:18 CDT:** p = 23, 29, 31 six-chart decompositions running locally (one msolve);
K6-R2UNIFORM (`engine/briefs/k1695_r6_r2uniform/TICKET.md`) offered to a sol screen: explain or prove the
characteristic-free tree (ℤ[1/N] certificates with explicit N, hand proofs of terminal
inconsistencies, or a bound P₀) — the route from "closed in nine characteristics" to "all fields" at
n = 4.

## R6.104 · OWNER DIRECTIVE (06:3x CDT, verbatim via dialogue): "当当前方法达到极限就先发布成果然后继续探索新方法" — PUBLICATION PLAN for the n ≤ 4 results and the n ≥ 5 exploration
**Reading:** the case-decomposition/certificate method has reached its ceiling at n = 4; once n = 4 is
closed for ALL fields, publish (three gates: adversarial audit, literature novelty, machine
certificates; Zenodo; git author chy4pro; no owner email; X posts only with the owner's per-post
approval), then explore new methods for n ≥ 5. **What is closed now:** n ≤ 3 (Lean); n = 4 stratum (b)
(Lean); n = 4 in characteristics 0, 2, 3, 5, 7 (two certificate families each), 11, 13, 17, 19 (one
family; codex replicates in progress); rank ≤ 1 at n = 4 in characteristic 0 and every prime < 10⁴.
**What "every field" at n = 4 still needs:** (a) the rank-two stratum in characteristics ≥ 23
(K6-R2UNIFORM: ℤ[1/N] certificates with explicit N, or a hand proof of the terminal inconsistencies, or
a prime bound); (b) the rank-one stratum in characteristics ≥ 10⁴ (the run-3 lift = ℤ-content, 19 h and
counting; or K6-R1HAND, a hand proof). **Decision:** the publishable claim is "n = 4 over every field"
— WAIT for (a) and (b); do not publish a characteristic list. Meanwhile run the three gates and build
the package so publication follows within a day of closure. **Draft title/scope:** "Kourovka 16.95
(Thompson) for n ≤ 4: kernel-checked proofs for n ≤ 3 and a computer-certified proof for n = 4 over
every field" — Theorem A (n ≤ 3, Lean, with the two-permutation strengthening (GC₃)); Theorem B (n = 4,
every field: normalisation lemma (hand), rank ≤ 1 (hand proof if K6-R1HAND succeeds, else certificates +
ℤ-content), rank 2 (case decomposition, two independent certificate families, characteristic-free
argument if R2UNIFORM succeeds)); Theorem C (stratum (b), every even n if LEAN10's root lemma is
finished, else n = 4, Lean); Lemma T (Lean); §Negative results and data: refutations of the
transposition-only rule, of (Mono) and (2Step) with explicit matrices, of the face lemma; the
good-count conjecture (GC_n) with its rank-one certificates in seven characteristics and the
minimizer classification as data; §Methods: the F4 memory-death of the monolithic ideals vs the
small-certificate decomposition; the identical-tree phenomenon. **Stays internal:** engine transcripts,
briefs, the hill-climbing programme beyond its refutations, cost/infra notes. **Dispatch list (sent to
dialogue):** K6-R1HAND (sol) — hand proof of the rank-one stratum at n = 4 (+ all-n stretch);
K6-AUDIT4 (sol) — adversarial audit of the whole n = 4 chain; K6-LIT4 (Pro, web) — literature
novelty check; K6-PUBPKG (luna/engineering) — certificate package + manifest + README; **n ≥ 5
exploration:** K6-R1ALLN (Pro) — the rank-one stratum for every n by hand (Fourier-coefficient
counting over n-cycles; a genuinely new, uniform method target); K6-N5R1 (sol, one msolve) —
feasibility of the eigenvalue-case decomposition for the rank-one stratum at n = 5 (first n = 5
computational foothold). Publication itself happens only after the owner's explicit go on the final
package (through dialogue) and only for closed results.

## R6.105 · OWNER DECISION (06:5x CDT, via dialogue; owner replied "好"): PORTFOLIO — finish the publications; deep lines get 48 h per new method with rotation; spare capacity goes to small-scale-decidable, publicly listed, 1–3-day-closable open problems
Consequences for this line: the n ≤ 4 publication track (§R6.104) is unchanged and highest-value;
the n ≥ 5 exploration (K6-R1ALLN, K6-N5R1) is budgeted at 48 h per method — rotate if nothing
banks. Immediate request fulfilled: `engine/briefs/kourovka_candidates_k1695.md` — my from-memory
list of candidate problems fitting the toolkit (matrix Waring tables over F_q; products of two
cyclic matrices over F₂/F₃ for n ≤ 4; GAP-decidable "does there exist a finite group…" Kourovka
entries; Cayley-graph Hamiltonicity bounds), every number/status flagged for verification by the
internet scan (engine/briefs/gacha_scan_0830.md). Pro order now: 677 fibre-5 → SCAN → my LIT4 →
677 novelty → 677 affine → my R1ALLN.

## R6.106 · OWNER DIRECTIVE (07:1x CDT, verbatim via dialogue): "当前codex额度还没用完，可以多考虑使用它，之前的成果做好了直接对外，GitHub要有哈，论文也要发，x也要发，要全面，如果有要发布的代码发GitHub上，要提供让其他人验证和证伪的全部条件"
Reading and actions: (1) use the remaining codex day for publication engineering; (2) completed
results go OUT on all three channels — GitHub (a dedicated repository with everything needed to
verify AND falsify: both encoders, every certificate or its regeneration script + sha256, pinned
solver/Lean versions, one-command builds, AXIOMS.txt, REPRODUCE.md, verify.sh with PASS/FAIL per claim,
control matrices, a falsification hook to try new characteristics), a paper (Zenodo DOI; arXiv if
endorsed), and an X thread (text to the owner via dialogue before posting); (3) still only CLOSED
results and after the owner's final go: "n = 4 over every field" (needs §R6.104 (a)+(b)) + n ≤ 3 +
stratum (b) + the negative results. Ticket `engine/briefs/k1695_github_pkg/TICKET.md` written
(repo `kourovka-16-95` built locally, not pushed; author chy4pro; privacy grep). Git identity:
chy4pro / [email] — never the owner's private email.

## R6.107 · K6-R2UNIFORM and K6-R1HAND GRADED (both honest FAILED for their full goals) — what IS proved: "all but finitely many characteristics" by transfer; the explicit exceptional set needs the terminals' ℤ-content
**R2UNIFORM** (`engine/harvest/k1695_r6_r2uniform/PROOF.md`): (i) the line-side DPLL path sets are literally
identical for p = 0, 7, 11, 13, 17, 19 on all six charts (COMPUTED); (ii) 243 of the 2 351 ℚ unit
terminals contain −d (d = the U-chart minor) as a generator, so 1 = −zu·g − s is an identity over ℤ —
those close in EVERY characteristic (PROVED); (iii) five small terminals (14–16 variables) have exact
integral Singular lift certificates (denominator product 1); an 18-variable lift failed at a 180-s
wall; (iv) the **contraction lemma** (PROVED, re-derived): for a terminal ideal I ⊂ ℤ[x] with Iℚ[x] = (1),
I ∩ ℤ = (d_S) with d_S ≥ 1, and the reduction I_p is unit iff p ∤ d_S — so N = ∏ d_S is the exact
exceptional integer and every prime not dividing N closes the whole ℚ-tree; (v) corrections to my
ticket: the terminals have up to 28 variables (not ≤ 20) and 32–119 generators; node counts 826/806/797
per representative chart (+ control invocations). No global N obtained; the "every characteristic"
rank-two claim is NOT banked from this ticket. **R1HAND** (`…/k1695_r6_r1hand/PROOF.md`): Lemma T
re-proved; fixed-row normalisation and the 24 deflation determinants; the feedback lemma
det[b, (N + bfᵀ)b, …] = det[b, Nb, …]; the generic branch S·Q ≠ 0 (S = a+b+c, Q = a²+b²+c²−ab−ac−bc, the
Fourier factorisation Q = (a+ωb+ω²c)(a+ω²b+ωc)) closed by the 3-cycle orderings over every field; the
x = 0 branch closed; the residual branches S = 0 and Q = 0 (Fourier planes) NOT closed by hand — exactly
where the Gröbner certificates carry the proof; all-n stretch: a sufficient condition (13) only.
**What is now PROVED for n = 4 (precise statement for the paper):** 16.95 holds over every field of
characteristic 0, over every field of characteristic p for p ∈ {2, 3, 5, 7, 11, 13, 17, 19} (and 23 pending
the last charts), and — by the transfer principle for the universal first-order sentence "∀A (det A ≠ 0 →
∨_σ Ω(AP_σ) ≠ 0)" from ACF₀ to ACF_p — for all but finitely many primes p (non-effective: the exceptional
set is contained in the primes dividing N = ∏ d_S over the rank-two terminals times the analogous integer
for the rank-one certificates). **Routes to "every field":** (a) K6-ZLIFT — a VM campaign computing d_S
(Singular lift or ℤ-std) for every ℚ-terminal of the rank-two tree (2 351 on the representative charts;
small ones seconds, 22–28-variable ones possibly hours) and for the rank-one certificate ideals (the
run-3 lift is the rank-one piece, 19 h so far) — then run msolve for every prime dividing N;
(b) a structural classifier proving integrality for whole classes of terminals (243 done, 2 108 left).
**Publication scope (proposal to the owner via dialogue):** publish the precise statement above now
(it is a closed theorem: characteristic 0, the explicit primes, and all but finitely many characteristics),
with the exceptional-set computation as stated follow-up; upgrade to "every field" if ZLIFT finishes
before the paper is final.

## R6.108 · K6-ZLIFT pre-registered (run 7): integer content of all 4 694 characteristic-0 unit terminals (my six-chart tree) on a VM
Files: `engine/gcp/k1695_r6_zlift_startup.sh` (runner), `engine/gcp/zlift_one.py` (worker: Singular
`lift(I, ideal(1))` → D_S = product of coefficient denominators, verified Σ c_i g_i = 1; fallback
`std` over ℤ → constant generator d_S), `engine/gcp/k1695_r6_launch7.sh` (e2-highmem-8, 4 parallel
lifts in 12 GiB scopes, per-terminal wall 2 h internal, no campaign cap, 5-day backstop, ≈$8.6/day),
inputs `engine/harvest/k1695_r6_zlift/inputs/terminals.tar.gz` (4 694 .ms files by chart; sizes 14–28
variables: 384/1169/1457/966/446/16/191/42/12/11 for 14/16/18/20/22/23/24/26/27/28). Readings: every
terminal LIFT with D_S = 1 (or ZSTD d_S = 1) → the rank-two tree is characteristic-free → with the
rank-one ℤ-content (run-3 lift or its own campaign) "n = 4 over every field"; terminals with D_S > 1 →
run msolve over GF(p) for each p | D_S (those p are the only possible exceptions); FAIL terminals →
their primes stay unknown (the theorem stays "all but finitely many p" for those). Launch by dialogue
(pre-authorised; 8 vCPUs free).
**§R6.108 run 7 LAUNCHED by me** (the classifier allowed the committed script this time): `k1695-r6-zlift`
(e2-highmem-8) RUNNING since 2026-08-30T11:53:15Z (06:53 CDT); inputs gs://…/k1695_r6g/inputs/
(terminals.tar.gz 3.0 MB, zlift_one.py); outputs gs://…/k1695_r6g/out/ (heartbeat, results/, ALL_RESULTS).
**Dialogue's decision (07:2x, applying the owner's standing directives):** proceed NOW with the honest
closed statement (characteristic 0; p = 2, 3, 5, 7, 11, 13, 17, 19, 23 pending; all but finitely many
characteristics by transfer, exceptional set ⊆ primes dividing an N under computation); gates G1–G3
and the package run on that statement; upgrade to "every field" if ZLIFT delivers first; the owner can
override via dialogue's status line.
**§R6.103 addendum (07:12 CDT):** p = 23 fully closed (six charts: 827/807/807/807/807/798 runs, 795/781/
781/781/781/775 closed, 0 OPEN, 0 capped — the identical tree). My p ≥ 29 loop stopped to free the msolve
slot for AUDIT4 (gate 1). **GITHUB_PKG (luna) inspected:** local repo 941 MB (raw .ms inputs must move
to a release/Zenodo bundle), two overlapping "Initial public verification package" commits (squash
before push), two line scripts still contain absolute machine paths (privacy grep hit — must be
fixed), CLAIMS.md a placeholder — follow-up ticket K1695-GITHUB-PKG-2 with the precise claims text.
**§R6.108 ZLIFT first look (07:14 CDT, 20 min in):** 4 694 terminals loaded; the first four lifts (24-variable
terminals with five N cases — the smallest FILES, not the smallest systems) are still running after
20 min; no result yet. Expect a slow campaign; per-terminal wall 2 h, then fallback ℤ-std 2 h. (Worker
writes its temporary .sing into results/ — harmless noise in the sync.) Messages to dialogue failed
twice at 07:1x (session busy); content queued for resend.
**Dispatch confirmed (07:2x CDT, dialogue):** AUDIT4 → codex3 (sol high), GITHUB-PKG-2 → luna (no push),
PAPER → codex10; my three earlier sends had arrived. ZLIFT readings are mine.
**GITHUB-PKG-2 (luna) FAILED dialogue's acceptance (07:2x CDT):** 291 MB, still two same-titled commits,
the two line scripts still contain the machine path, CLAIMS.md compressed instead of verbatim.
Re-issued as k1695_github_pkg3_fixup with mandatory PASS/FAIL checks (size ≤ 150 MB with .ms inputs
and logs in a tar.zst bundle + sha256 + in-repo index; orphan-branch single commit; privacy grep zero;
CLAIMS.md verbatim diff; verify.sh quick exit 0). My decision: keep every .gb basis, the trees,
controls, scripts, Lean and docs in-repo; bundle the regenerable .ms inputs and logs.
**§R6.103 addendum (07:2x CDT):** the p ≥ 29 loop had survived my first kill; p = 29 charts {1,2} and {1,3}
finished (0 OPEN, 0 capped) before I stopped it for good (chart {1,4} interrupted — no verdict). p = 29
is therefore PARTIAL (two charts); resumed only if a slot is idle. AUDIT4 has priority for msolve.
**INCIDENT (07:3x CDT, dialogue):** the pkg3 fix-up on luna ran a history rewrite in the wrong order and
emptied the local package repo (engine/harvest/k1695_github_pkg/repo: unborn branch, dangling refs;
quarantined as repo_wrecked_0723 / bundle_wrecked_0723). SOURCES UNTOUCHED (verified: certificates,
Lean files, scripts all present). Root cause (dialogue's own assessment): a destructive git sequence in a
low-tier ticket. Rebuild ticket k1695_github_pkg4_rebuild → codex4 (sol): build tree by copy, single
init/add/commit, no orphan/gc/filter-branch/rm -rf, verbatim CLAIMS, ACCEPT4 PASS required. Rule
recorded: history-rewriting/rm operations never go to luna; verbatim/spec tasks go to sol. Wreck kept
for forensics until pkg4 passes; then delete.

## R6.109 · GATE 1 (K6-AUDIT4, codex3): PASS with publication-hygiene findings — no mathematical defect in the n = 4 chain
`engine/harvest/k1695_r6_audit4/AUDIT.md` + artifact_audit.json, encoder_comparison.json, rank1_audit.json,
random_extension_search.json. Verified links: normalisation + scalar extension (A); rank ≤ 1 branch and
N4x cover (B); conjugation direction, GL₂ gauge, six U-charts (C); exhaustiveness of E_r ∨ N with the
correct eigenvalue inventories per characteristic and correct adjunction of ω, i (D); the Woodbury
branch with χ ≠ 0 exactly (E); independent re-derivation of two permutations' generators matching BOTH
families up to scalars (F); full DPLL structure replay (729 roots, complete children, open = [] and
capped = 0 in every tree; 180 sampled unit bases hashed; one fresh capped msolve rerun byte-identical)
(G); random exact-rank-two search over GF(2,4,8,3,9,27,5,25,125): no all-bad matrix (H);
Nullstellensatz + extension (I); Lean statements audited, standard axioms (J). Findings: F1 MEDIUM —
my runner ignored msolve's return code and could classify a stale output (evidence hardening; FIXED
now in round6_r2split_odd.py and round6_r2split_check.py: stale .gb removed before each run, nonzero
exit ⟹ no verdict); F2 LOW (ticket resource inconsistency; honoured the cap); F3 LOW — codex2's
p = 13 chart 5 state is incomplete (must not be cited; the line's six-chart p = 13 trees are complete);
F4 LOW (RSS not observable in the sandbox); F5 LOW — wording: "n = 3 kernel-checked; n ≤ 2 elementary"
unless the small cases are wrapped in Lean. Gate 1: PASSED for characteristics 0, 2, 3, 5, 7, 11, 13, 17,
19 (23 was closed after the audit's snapshot; its trees are structurally identical — include in the
replay before publication).
**K6-PAPER (codex10) first draft graded (07:3x CDT):** `engine/harvest/k1695_paper/main.tex` (952 lines):
Theorems A/B/C match CLAIMS C1/C6/C2 exactly, the scope remark is honest ("not an every-field theorem",
\upgradeflag markers), sections cover Lemma T, normalisation, Δ-lemma, stratum (b), rank ≤ 1, rank 2
(chart normalisation, bordered-rank and Woodbury lemmas, contraction lemma), negative results, data,
open problems. Fix-ups (K6-PAPER-2, `engine/briefs/k1695_paper2/TICKET.md`): F5 wording (n ≤ 2
elementary, n = 3 Lean), per-characteristic family counts (codex2's 1113: p = 11 complete on the three
representative charts → two families; p = 13 chart 5 incomplete → one complete family), the audit
paragraph, a precise citation for the transfer principle. **K6-R2SPLIT-1113 (codex2):** p = 11 three
representative charts 826/806/797 runs, 795/781/775 unit, 0 open, 0 capped → §R6.101 p = 11 upgraded to
TWO families; p = 13: charts 0, 1 complete, chart 5 incomplete (AUDIT4 F3) → stays one complete family.
**§R6.108 ZLIFT RELAUNCHED (07:4x CDT):** the first campaign spent 50 min on four 24-variable terminals
with five N cases each (the file-size order picked the HARDEST systems first: N-case terminals have few
but long generators; one Singular process reached its 12 GiB scope) — deleted and relaunched with an
easiest-first `order.txt` (by number of N cases, then variables, then size; distribution of N cases:
0: 384, 1: 1169, 2: 1457, 3: 966, 4: 462, 5: 191, 6: 54, 7: 11). Same VM name `k1695-r6-zlift`, same
prefix k1695_r6g (old results dir empty). Run 3's heartbeat confirmed fresh (its lift continues).
**Ticket K6-R2SPLIT-1723 (07:44 CDT)** → codex2: second families for p = 17, 19, 23 + completion of codex2's
p = 13 chart 5 (F3). codex2's 1113 finished (DONE) without the optional primes.
**K6-PAPER-2 (codex10) spot-checked (07:53 CDT):** F5 wording applied ("n = 3 kernel-checked; n ≤ 2
elementary"), family counts per characteristic stated (incl. "one family, not two" where true), the
Robinson–Lefschetz transfer cited (Marker, Cor. 2.2.10) with a K6-LIT4 bibliographic placeholder box,
prepublication placeholders kept. Full read at the 11:00 review. LIT4 moved ahead of the SCAN on Pro.

## R6.110 · GATE 3 PASS (pkg4) · ZLIFT first reading · the lift denominators are the WRONG number — exact ℤ-content by Singular `std` over ℤ is fast (08:4x CDT, 08-30)
**Gate 3 (K6-GITHUB-PKG4, codex4) PASS — my own inspection agrees with dialogue's:** `engine/harvest/k1695_github_pkg/repo`:
1 commit bb1c1108 (author chy4pro <chy4pro@users.noreply.github.com>, "Kourovka 16.95, n ≤ 4: verification package v1"),
121 MB (.git 17 MB), privacy grep 0 hits, all 8 claim lines C1–C7 VERBATIM from `engine/briefs/k1695_github_pkg2/TICKET.md`,
`VERIFY_QUICK.log` ends PASS (5.8 s), `lean/AXIOMS.txt` = propext/Classical.choice/Quot.sound only for goodCount3,
stratumB_minpoly, minpoly_eq_charpoly_of_rank_ge; `falsify/` (find_counterexample.py, try_new_characteristic.md);
VERSIONS pins msolve 1e3af01f / Lean v4.34.0-rc1 / Mathlib de5ce8a9; README line 5 disclaims "every field" and n ≥ 5
and states nothing is published. Gate board: G1 PASS, G3 PASS, G2 = K6-LIT4 (Pro, after FIBRE5). Wrecked copies deleted by
dialogue. NO push/publication until the owner's final go through dialogue.
**ZLIFT (run 7) first reading:** 1 565 of 4 694 terminals lifted in the first 10 min (all LIFT, 0 FAIL/ZSTD), then only
10 more in the next 40 min (the N-case terminals are slow). Prime content of the denominator products D_S
(`problems/k1695/round6_zlift_primes.py`, strip all primes ≤ 10⁴ by one gcd against their product; log
`logs/k1695/round6_zlift_primes.log`, table `engine/harvest/k1695_r6_zlift/primes_summary.tsv`): D_S has up to
1 168 399 decimal digits (r0072, three charts); primes seen {2,3,5,7,11,13,17,19,29,37,43,47,647,2477}; SEVEN
terminals keep an unfactorable cofactor (> 10⁴-rough, 6 104 to 867 757 digits: r0408 charts 0,2,3,4 and r0072
charts 1,2,5). So the product of certificate denominators is far too redundant to identify the exceptional set.
**Direct checks of every (terminal, prime > 23) pair (`problems/k1695/round6_terminal_modp.py`: reduce the ℚ terminal's
integer coefficients mod p, msolve over GF(p)):** r0139 charts 1–4 mod 43, r0409 charts 0,2,3,4 mod 37, r0514 charts
1,3,5 mod 47, r0330 charts 0,1,2 mod 2477, r0486_E1 chart 4 mod 647, chart 3 mod 29 — ALL 16 UNIT. Controls: positive
(r0139 chart 1 mod 101, a prime not dividing D) UNIT; negative (`ctrl_realised.ms`, the realised bad pattern, non-unit
over ℚ, mod 29) NOTUNIT. Every candidate prime so far is a spurious pivot denominator.
**THE RIGHT TOOL — Singular strong Gröbner basis over ℤ (`ring r = integer`; `problems/k1695/round6_zstd_one.py`):**
on p0_chart0__r0408 (lift D 8 757 digits, cofactor 6 104 digits) it returns G = {1}, i.e. d_S = 1, in 0.5 s at 4 MB
(`logs/k1695/round6_zstd_r0408.log`). Controls: (2x−1, 15, y−3) → d = 15 (expected 15, unit over ℚ, non-unit mod 3, 5);
`ctrl_realised.ms` → no constant (expected: non-unit over ℚ). (d_S) = I_S ∩ ℤ exactly, so the primes of d_S are EXACTLY
the characteristics in which terminal S fails; d_S = 1 ⟹ unit in every characteristic. **Launched (08:4x CDT) the
local batch `problems/k1695/round6_zstd_batch.py` over all 4 694 terminals** (easiest-first order.txt, per terminal
wall 120 s + 2.5 GB cap via run_capped, one process; table `engine/harvest/k1695_r6_zstd/results.tsv`, log
`logs/k1695/round6_zstd_batch.log`). If every terminal returns d_S with all prime factors ≤ 23 (or FAILs are closed by
the lifts/direct checks), the rank-two case of 16.95 at n = 4 is closed in EVERY characteristic (p ≤ 23 by the direct
campaigns §R6.94–§R6.103, p > 23 by contraction); the remaining piece for "every field" is the rank ≤ 1 stratum's
ℤ-content (run 3's lift, or the same ℤ-std on the 195 rank-one certificate ideals — next). ZLIFT VM kept running as an
independent second method until the batch is graded (decide at the 11:00 review).
**§R6.110 addendum (09:2x CDT) — INCIDENT and fix.** At 09:05–09:15 dialogue killed three Singular processes of mine
(6.9 GB footprint / 5 min; 2.9 GB; 2.0 GB / 5 min) as swap went 4.9 → 10 GB: I had TWO ℤ-std drivers running (rank-two
terminals + the 198 GC4 orbit ideals) PLUS foreground Singular runs (an uncapped debug run of the rank-one ideal J,
an N4x loop with a 600 s wall) — three concurrent Singulars, and run_capped's RSS cap is blind to macOS compressed
memory (a 6.9 GB footprint reads < 2.5 GB RSS). 09:16: both drivers and every Singular of mine killed (pgrep clean).
Fix (in the tree): `round6_zstd_one.py` now runs Singular as a direct child under a 1-second watchdog that SIGKILLs at
--rss-mb (2000) or --wall (30 s for the local sweep); `round6_zstd_batch.py` is strictly sequential with a swap guard
(waits while `vm.swapusage` used > 9 000 MB; the box's baseline is ≈7 GB); rule: ONE driver, NO foreground Singular.
Watchdog verified: r0504 chart 0 killed at 2 027 MB after 10 s; with --rss-mb 50 killed at 2 s; no orphan. Ring renamed
R_ in every script (the N4x ideals have a variable r that shadowed Singular's ring name → "`poly` * `ring` failed").
Local sweep relaunched 09:19 (single process): median 0.6 s per terminal; hard terminals (N-case) fail fast at 2 GB
(r0299, r0504, r0060 …) and are left to the cloud. New d_S values seen: 3 (r0486_N charts 0–2) besides 1 and 2 — all
≤ 23. Rank-one ideal J (6 variables, 24 determinants) is HARD over ℤ (6.9 GB in 5 min); GC4 orbit 004 gave d = 1 in
94 s, the others exceeded the caps; the N4x chart ideals reach 1.5 GB in 11 s.
**RUN 8 = ZSTD v2 prepared** (`engine/gcp/zlift_one_v2.py`: ℤ-std first → exact d_S, lift fallback; `engine/gcp/
k1695_r6_zstd_startup.sh`: PAR workers in systemd scopes with MemoryMax — a real limit — skip list of locally resolved
terminals, extra ideals appended last, heartbeat/results every 10 min, poweroff at DONE, 5-day backstop, no campaign
cap; `engine/gcp/k1695_r6_launch8.sh`: e2-highmem-4, PAR 2 × 14G, walls 2 h + 1 h, prefix k1695_r6h, extras =
`engine/harvest/k1695_r6_zstd/extra_inputs/` (209 files: J_p0, 10 N4x charts, 195 GC4 orbits + 2 controls)). Launch
handed to dialogue (pre-authorised): delete k1695-r6-zlift first (its 1 575 lift results stay in gs://…/k1695_r6g/,
superseded), then `bash engine/gcp/k1695_r6_launch8.sh`. Run 3 kept until run 8 returns d for J.

## R6.111 · K6-R2SPLIT-1723 (codex2) GRADED PASS — p = 17, 19, 23 now TWO families; p = 13 chart-5 audit closes codex's p = 13 family (09:4x CDT, 08-30)
`engine/harvest/k1695_r6_r2split1723/REPORT.md` (6.4 KB, 181 MB of certificates): nine representative-chart trees
(charts 0, 1, 5 — orbits {0}, {1,2,3,4}, {5} as in 1113) for p = 17, 19, 23: 826/806/797 runs per chart with 795/781/775
UNIT prunes and 31/25/22 extended NONUNIT prefixes — the SAME tree shapes as my p = 0, 7, 11, 13, 17, 19, 23 trees
(§R6.94–§R6.103); 7 287 msolve runs, 0 capped (max 49.9 s, 1.2 GB), zero open leaves, `exhaustive=true` in all nine
states; nine realised-pattern controls (reversal matrix, exact 17-bad conjunction) NONUNIT; the saved p = 13 chart-5
tree audited complete (797 runs, 775/22, zero candidate leaves) → codex's p = 13 family complete. Independent replay
(`r2split1723_verify.py`, 1113's replay core) `verified: true`. Eigenvalue tables per p correct (p = 17: ω ∈ GF(17) via
ω²+ω+1 = 0 adjoined, 4-cycles E_4/E_13 (4² = 16 = −1); p = 19: 3-cycle roots 7, 11 in GF(19), i adjoined; p = 23: ω
and i adjoined). **My spot check (09:4x CDT): 15 random nodes (4 UNIT + 1 NONUNIT per prime) rerun with my own msolve
from their .ms files → 15/15 agree.** Swap gate honoured (max 10 197 MiB at launch; two launches refused and resumed).
Grade: PASS, COMPUTED. Consequence: n = 4, rank two, characteristics 13, 17, 19, 23 each rest on TWO families
(mine + codex2), as 0, 2, 3, 5, 7, 11 already did. CLAIMS C5 wording ("one family, not two" for 13–23) can be upgraded
in the package/paper at the next revision — a wording change only, not a scope change. No DONE marker file yet (the
report ends with DONE-r2split1723).

## R6.112a · K6-N5R1 (codex2) GRADED PASS as an honest feasibility screen — the per-permutation DPLL is DEAD at n = 5 (combinatorial breadth, not big ideals); next method = the deflation (Krylov-determinant) ideal J₅ (10:4x CDT, 08-30)
`engine/harvest/k1695_r6_n5r1/REPORT.md` (8.4 KB) + replay `verified: true`. Encoder: A = I + u wᵀ, w₁ = 1, z(1 + wᵀu) = 1
(10 variables); E_r cases = all 4×4 minors of P_σ + u w_σᵀ − rI; controls: diag(2,1,1,1,1) over GF(3) (63 bad / 56 cyclic,
63-case conjunction NONUNIT). GF(3) DPLL stopped after 2 866 nodes (1 753 UNIT, 1 113 NONUNIT, 78 pending, depth 96)
having finished only 1 of 1 024 transposition prefixes; p = 0 probe 60 nodes all NONUNIT to depth 69. Max node time
0.59 s, max ideal 792 generators in 11 variables, nothing capped — the explosion is the NUMBER of consistent prefixes
from the (3,2) block on. **Structural fact worth keeping (their §3):** a permutation with ≥ 3 cycles has
rank(P_σ − I) = 5 − #cycles ≤ 2, so rank(P_σ + u w_σᵀ − I) ≤ 3 < 4: every transposition, double transposition and
3-cycle is AUTOMATICALLY bad for every rank-one A at n = 5 (in general: only permutations with ≤ 2 cycles can be good
for I + uwᵀ). The all-E₁ spine of depth 45 is forced, and the DPLL over the remaining 74 permutations (2–5 cases each)
has too many consistent prefixes. Grade: PASS (COMPUTED negative feasibility result; memory rules honoured: swap gate
5.1–5.5 GiB, no Singular). Decision under the 48-h budget (§R6.105): the DPLL method is abandoned for n = 5; the
next method is the one that closed the rank-one stratum at n = 4 WITHOUT case splits — the deflation criterion
(Lean `cyclic_standardBasis_of_principalBlock` + `minpoly_eq_charpoly_of_rank_ge`): with v_i = 1 and R = A with row i
deleted, D_{j,τ} = det[c_j, M c_j, …, M^{n−2} c_j] ≠ 0 ⟹ e_i is cyclic for A P_σ; the ideal J_n of ALL these determinants
(n = 5: 5 × 24 = 120 determinants of 4×4 Krylov matrices in 8 variables) being the unit ideal over GF(p) closes the
rank-one stratum at n = 5 in characteristic p. My own light computation first (one msolve, capped).

## R6.112b · PRIOR ART FOUND (my own web check, 10:5x CDT, 08-30): Dixon, "Recognizing cyclic matrices and a conjecture of J.G. Thompson", arXiv:1606.02238 — a claimed proof of 16.95, WITHDRAWN in v2 (14 Nov 2017); attribution of 16.95 is J. G. Thompson (2006), not R. C. Thompson
Source: the arXiv abstract page (fetched 10:5x CDT). Abstract (v1, 7 Jun 2016): "In 2006 J.G. Thompson conjectured: 'If F is
a field and A is in GL(n,F), then there is a permutation matrix P such that AP is cyclic, that is, the minimal polynomial
of AP is also its characteristic polynomial' (open problem 16.95 in the Kourovka Notebook). The present note provides a
simple criterion for a matrix to be cyclic and uses this to prove Thompson's conjecture." Comments of v2 (14 Nov 2017,
withdrawn): "I am withdrawing this paper since the implication (iv) => (i) in the Proposition is false for n > 2. As a
consequence the conjecture of J.G. Thompson remains open." MSC 15A21; no journal reference. Consequences: (1) 16.95 is
NOT subsumed — it remains open (consistent with Pro's interim LIT4 note "only n = 3 apparently new within n ≤ 3; strong
two-factor cyclic results do not imply 16.95"); our n = 4 chain stands as new. (2) ATTRIBUTION ERROR in our package and
paper: 16.95 was proposed by J. G. Thompson (2006), not R. C. Thompson — must be corrected in CLAIMS.md:1, README.md:3,
main.tex:77 (and any "R. C." elsewhere) before ANY publication; `\cite{Thompson1980}` at main.tex:255 to be checked
against the bib entry (if it is R. C. Thompson's own 1980 work on cyclic matrices it is a separate legitimate reference).
(3) Dixon's withdrawn note must be cited in the paper's related work as an attempted proof (with the withdrawal
reason quoted), and the Kourovka Notebook edition/entry cited exactly. Gate 2 status: OPEN pending the LIT4 harvest
and my own resolution of every reference; the package/paper get a revision ticket (pkg5/paper3) bundling: attribution
fix, Dixon citation, 1723 two-family wording (§R6.111), exact-d_S results (§R6.110/§R6.112) — after run 8.
**§R6.112b addendum (10:5x CDT) — the Kourovka entry itself, read from the Notebook PDF (arXiv:1401.0300v40 = No. 21,
Novosibirsk 2026, 18 Jan 2026, editors E. I. Khukhro and V. D. Mazurov; extracted with pypdf, 299 pages):** 16th Issue
(2006), p. 102: "16.95. Conjecture: If F is a field and A is in GL(n, F), then there is a permutation matrix P such that
AP is cyclic, that is, the minimal polynomial of AP is also its characteristic polynomial. J. G. Thompson". No editorial
comment, no archive mark — still listed as open in the 2026 edition. This is the verified citation for the K6-LIT4
placeholder in main.tex (replace \cite{Kourovka1695} data: Khukhro–Mazurov (eds.), Unsolved Problems in Group Theory.
The Kourovka Notebook, No. 21, Novosibirsk 2026, arXiv:1401.0300v40, Problem 16.95, p. 102, proposer J. G. Thompson).

## R6.112 · DAILY REVIEW (§R6.90) — 10:5x CDT, 08-30
**Cloud jobs (both e2-highmem-4, $0.18/h each, no caps per the owner's rule):** run 3 `k1695-r6-groebner3` (created 08-29
11:31 CDT; 23.2 h; the rank-one monolithic lift still running, ≈ $4.2 so far) — keep until J's exact d arrives from run 8
(extras) or its own lift ends; run 8 `k1695-r6-zstd` (created 09:22 CDT; 1.5 h; ≈ $0.3): 5 results — 3 ZSTD d = 2
(r0060 ch1 349 s, r0504 ch3 1 105 s, +1), 2 FAIL scope-killed (r0504 ch0, ch1: > 14 GiB over ℤ; v2 loses the lift
fallback on a scope kill → run 9 with the v3 worker `engine/gcp/k1695_r6_launch9.sh` on the FAIL set after run 8);
two Singulars at 8.7 GB, 26 min (r0299/r0060 ch2). ZLIFT VM deleted 09:21 (1 584 lift results kept, superseded).
Cumulative GCP spend estimate ≈ $17 of the $90.22 credit (earlier runs ≈ $12, run 3 ≈ $4.2, ZLIFT ≈ $0.6, run 8 ≈ $0.3).
**Codex day (quota until ≈21:3x):** 1113 ✓, 1723 ✓ PASS (§R6.111), AUDIT4 ✓ (G1 PASS), PAPER2 ✓, PKG4 ✓ (G3 PASS), N5R1 ✓
PASS-negative (§R6.112a); codex2 idle — next ticket only after my J₅ experiment (rank-one n = 5 via the deflation ideal)
says whether a second family is worth it; then the revision ticket pkg5 + paper3 (attribution J. G. Thompson, Dixon
withdrawal prose, Kourovka No. 21 citation, 1723 two-family wording, exact-d_S results). **Pro seat:** FIBRE5 (677) →
LIT4 (chat stuck on one search line since 10:27; dialogue re-issues at 10:55 with the mandatory Dixon/attribution block
and the verified Notebook quote).
**Publication gates:** G1 PASS, G3 PASS, G2 OPEN — my own web/PDF checks (§R6.112b) settled the two decisive facts
(Dixon 1606.02238 withdrawn Nov 2017 ⟹ 16.95 open; proposer J. G. Thompson, Kourovka No. 21 p. 102); remaining for G2:
the LIT4 list of any other partial results, each resolved via Crossref/OpenAlex/arXiv by me.
**Scope statement (unchanged):** n ≤ 3 every field (Lean); n = 4: characteristic 0, p ∈ {2,3,5,7,11,13,17,19,23} (two
families each), and all but finitely many characteristics (transfer). Exact exceptional set so far: 2 090 of 4 694
terminals have d_S ∈ {1, 2, 3} (§R6.110/§R6.112) — every exceptional prime seen is directly closed; "every characteristic
at n = 4" is claimed ONLY when all 4 694 terminals AND the rank-one ideal J have exact d with all primes ≤ 23.
**n ≥ 5:** N5R1 negative (DPLL breadth); next: J₅ deflation ideal (mine, one capped msolve) — result in the next entry.
**Local box:** 0 Singular, ≤ 1 msolve, swap ≈ 5–6 GB. **Nothing published; nothing SOLVED.**

## R6.113 · ⭐ n = 5, RANK-ONE STRATUM, characteristic 3: COMPUTED (my family) by the deflation ideal J₅ — unit ideal in 15 s, no case split (10:5x CDT, 08-30)
Method (§R6.112a decision): `problems/k1695/round6_rank1_n5.py` (general n; sympy `Poly` arithmetic, Laplace determinants).
A = I + u vᵀ, v_i = 1 after scaling; R = A with row i deleted = [x, e₁ + y₁x, …, e₄ + y₄x] (4 × 5, 8 variables); for each
column j and each ordering τ of the other four, D_{j,τ} = det[c_j, M c_j, M² c_j, M³ c_j] (M = the other columns in
order τ). With B = A P_σ, σ(i) = j and τ = the order of σ on the other indices, c_j = column i of B without entry i
and M = the principal block of B without row/column i, so the Lean lemma `cyclic_standardBasis_of_principalBlock`
(CyclicToMinpoly.lean:190, general m + 1 = n, standard axioms) gives: D_{j,τ} ≠ 0 ⟹ e_i is a cyclic vector of A P_σ ⟹
A P_σ cyclic (`minpoly_eq_charpoly_of_rank_ge`). Hence J_n = (all n·(n−1)! determinants) unit over GF(p) ⟹ the rank-one
stratum of 16.95 at n holds in characteristic p. **Sanity n = 4:** 24 determinants (17 nonzero, degree ≤ 6): UNIT over
GF(3), GF(2), ℚ; control (3 determinants) NOT unit — reproduces §R6.42. **n = 5:** 120 determinants, 74 nonzero, ≤ 155
terms, degree ≤ 8, built in 50 s; **msolve over GF(3): UNIT [1] in 15 s** (control 3 determinants NOT unit). Files
`engine/harvest/k1695_r6_rank1_n5/J5_p3.ms(.gb)`. Status: COMPUTED, one family (mine) — banking needs a second family
(codex ticket K6-N5J) and, for "every characteristic", the ℤ-content of J₅ (cloud only: Singular over ℤ is banned on
this box). Contrast: N5R1's per-permutation DPLL could not finish one transposition prefix in 2 866 nodes; the deflation
ideal needs ONE Gröbner basis. Other characteristics: next lines.
**§R6.113 addendum (10:5x CDT):** J₅ is the UNIT ideal also over ℚ (46 s) and over GF(2) 18 s, GF(5) 31 s, GF(7) 32 s,
GF(11) 25 s, GF(13) 36 s, GF(17) 37 s, GF(19) 38 s, GF(23) 38 s — control (3 determinants) NOT unit in every run
(`engine/harvest/k1695_r6_rank1_n5/J5_p{0,2,3,5,7,11,13,17,19,23}.ms(.gb)`). So (one family, COMPUTED): **the rank-one
stratum of 16.95 at n = 5 holds in characteristic 0 and in characteristics 2, 3, 5, 7, 11, 13, 17, 19, 23** (GF(2)
agrees with the exhaustive GF(2) check of n = 5). Ticket K6-N5J (`engine/briefs/k1695_r6_n5j/TICKET.md`, codex2): second
family + finite audits + all p < 2000. Next: J₆ (720 determinants, 10 variables) feasibility, and J₅ for p < 10⁴.

## R6.114 · GATE 2 PASS — K6-LIT4 v2 (Pro) graded; every citation resolved by me (12:0x CDT, 08-30)
`engine/harvest/k1695_r6_lit4_pro.md` (33.9 KB): verdicts — proposer J. G. Thompson (PROVED); no valid general proof
(Dixon withdrawn); no prior n = 3 all-fields proof, no prior n = 4 irreducible-quadratic or characteristic-list theorem
(NOT FOUND); closest permutation-only theorem Cigler–Jerman 2014 (over ℂ, 3×3: some PA has ≥ 2 distinct eigenvalues —
weaker than cyclic); diagonal/monomial-scaling (Choi–Huang–Li–Sze 2012, Feng–Li–Huang 2012, Cigler–Jerman LAA 2014),
two-cyclic-factor (Vaserstein–Wheland 1990, Sourour 1986, Botha 2010), centralizer cosets (Đoković 1995), completions
(Rodman–Shalom 1992) — none subsumes; n ≤ 2 elementary (present as preliminary); monomial inputs elementary (n-cycle).
**My resolutions (11:5x–12:0x CDT):** all 13 DOIs resolved via api.crossref.org with matching title/authors/journal/
volume/pages/year (Fulman BAMS 39 (2002) 51–85 [online 2001]; Cigler–Jerman Special Matrices 2 (2014); Stuart–Weaver
LAA 212/213 (1994) 397–411; Choi–Huang–Li–Sze LAA 436 (2012) 3773–3776; Feng–Li–Huang LAA 436 (2012) 120–125;
Cigler–Jerman LAA 440 (2014) 213–217; Vaserstein–Wheland LAA 142 (1990) 263–277; Sourour LMA 19 (1986) 141–147; Botha
LAA 433 (2010) 1–11; Đoković LAA 220 (1995) 111–121; Rodman–Shalom LAA 168 (1992) 221–249; J. G. Thompson J. Algebra 191
(1997) 265–278; Holden–Piene, The Abel Prize 2008–2012, Springer, pp. 101–107 [Crossref 2013]). **Fulman verified from
the arXiv PDF (math/0003195v2, 27 Mar 2001; first version 28 Mar 2000), §1:** "John Thompson has asked if every matrix
is the product of a cyclic matrix and a permutation matrix, suggesting that the answer could have applications to
finite projective planes." — so the question predates the 2006 Notebook issue (asked by 2000). **Kourovka v45 (3 Jul
2026) verified from its PDF:** entry 16.95 unchanged, uncommented, "J. G. Thompson" (the v45 update note says some new
solutions "obtained using AI" were added elsewhere — not 16.95). **Aristotle paper (arXiv:2607.17477, van Doorn–Judin–
Monticone–Morrison, Jul 2026: eight Kourovka problems solved and Lean-verified by the Aristotle agent):** does not
mention 16.95. **Gate 2: PASS.** Corrections carried into the revision ticket K6-PUBREV: proposer J. G. Thompson;
"asked by Thompson before 2000 (Fulman), recorded in the 16th issue (2006)"; Dixon = withdrawn attempted proof; n ≤ 2
elementary; exact Notebook citation (No. 21, arXiv:1401.0300v45, 3 Jul 2026, 16th Issue (2006), p. 102); related-work
paragraph with the verified references; 1723 two-family wording; exact-d_S status (SUMMARY.md); C8 (n = 5 rank-one)
only when N5J is graded PASS.
**§R6.113 addendum 2 (12:2x CDT):** second builder `problems/k1695/round6_rank1_jn_singular.py` (determinants built by
Singular polynomial arithmetic over GF(p), fed on stdin under the 1-s watchdog; msolve decides): n = 5, p = 3 → 74 nonzero
determinants, max degree 8 (same as the sympy builder), UNIT in 17 s (peak 604 MB). The sympy builder needs > 70 min
for n = 6 (killed); the Singular builder does n = 5 in 1 s — J₆ over GF(3) (720 determinants, 10 variables) now building
in the detached chain, followed by the J₅ sweep over 29 ≤ p < 1000. Note for the record: `Singular -q <file>` stayed
interactive after the script and hung until the wall (that was the 12:1x "timeout"); stdin mode exits cleanly.

## R6.115 · Run 8 status and the cost of exact ℤ-content; run 9 (v3) work list; PUBREV nearly accepted (12:5x CDT, 08-30)
**Exact d_S status:** 2 401 of 4 694 terminals resolved (local sweep + run 8) — every resolved terminal has N ≤ 2 cases
(N = 0: 384, N = 1: 1 169, N = 2: 848); values d_S ∈ {1, 2, 3} only. Remaining 2 293 by N-case count: N = 2: 609, 3: 966,
4: 462, 5: 191, 6: 54, 7: 11. Run 8 (v2, 2 workers, walls 2 h + 1 h) resolved 378 N = 2 terminals with median 0 s, p90 1 s,
max 1 523 s, and 8 FAIL scope-killed (> 14 GiB over ℤ: r0504 ch0/1, r0299 ch1/3, r0384 ch1/2/4, +1) — the hard tail costs
up to 3 h of a worker each, so run 8 will take days through N ≥ 3 unless walls are shortened and workers added (decision
at the evening review; the FAIL set goes to the refinement fallback: split one permutation deeper, ℤ-std the children).
**Run 9 (v3 worker, per-Singular scopes) work list written** `engine/harvest/k1695_r6_zstd/run9_work.txt` (19 names):
J_p0 FIRST (the rank-one ideal's exact d — decides the rank-one stratum in every characteristic and makes run 3
redundant), the 10 N4x charts (second rank-one family), then the 8 run-8 FAILs. The 195 GC4 orbit ideals are dropped from
the cloud queue (GC₄ is not needed for 16.95). Launch handed to dialogue (quota has one e2-highmem-4 slot).
**PUBREV (codex10) in progress — ACCEPT5.log so far:** F1 PASS (repo 137.8 MiB incl. .git 22 MiB; 54 739 .gb; raw .ms in
repo 12 = self-tests + control inputs; bundle 19 507 files with REGENERABLE_MS.sha256), F2 PASS (2 commits: base bb1c1108 +
new 81a52ff4), F3 PASS (0 forbidden hits in repo5 + main3.tex), F4 PASS (C1–C7 + C7′ "2394/4694 as of 12:0x, d_S = 1: 1383,
2: 1006, 3: 5, exceptional primes ⊂ {2,3}"; C5 two families for all listed characteristics; no n = 4 every-field claim; n = 5
claim absent — N5J not graded yet), F5 PASS (verify quick 5.7 s, stored log identical, one sequential regeneration + capped
msolve sample per p = 17, 19, 23), F6 items 1–3 PASS (attribution, origin with Fulman, Kourovka21, refs3.bib byte-identical
to VERIFIED_REFS.bib) — remaining F6 items and DONE-pubrev pending; my final grade after DONE.
**J chain:** the n = 6 Singular build hung 26 min at 0 % CPU — my stdout PIPE filled with Singular warnings (deadlock);
fixed (stdout to file; single `int rr`), chain relaunched 12:5x (J₆ p = 3 → J₅ sweep 29 ≤ p < 1000).
**§R6.115 addendum (12:5x CDT):** (i) J₆ over GF(3) locally: 394 nonzero determinants (of 720), max degree 10, built in
2 s; msolve exceeded the 1.5 GB local cap after 47 s (≈3 GB) → NORESULT; J₆ goes to the cloud (needs a GF(p) Gröbner
worker: Singular `std` over GF(3) or msolve on the VM) — stretch goal, not blocking. (ii) GCP: run 9 launch refused —
the binding quota is GLOBAL `CPUS-ALL-REGIONS-per-project = 32` (us-central1 28 + us-east1 4 in use; also
IN_USE_ADDRESSES 8/8 in us-central1); zone switching does not help. **Decision: delete run 3 (`k1695-r6-groebner3`)** —
its lift ran 28 h with no END marker and no partial output (final heartbeat 17:43Z, elapsed 90 677 s, ≈ $5 sunk); run 9
attacks the same rank-one ideal (J_p0 = J₄, 6 variables) first under a 14 GiB scope (ℤ-std 2 h, lift 1 h) and supersedes
it. Run 3 recorded as: NO RESULT (lift did not finish). Run 9 launch re-issued after the deletion.

## R6.116 · K6-PUBREV (codex10) GRADED PASS — package pkg5 (repo5, commit 81a52ff4 on bb1c1108) and paper3 (main3.tex + refs3.bib) ready for the owner's decision; one owed item: the PDF build (12:5x CDT, 08-30)
My own inspection of `engine/harvest/k1695_github_pkg/repo5` and `engine/harvest/k1695_paper/main3.tex`: 2 commits (base
bb1c1108 + 81a52ff4 "Publication revision: provenance, certificates, and compact release", author chy4pro), working tree
clean, 138 MB (.git 22 MB); privacy grep 0 hits; README line 3 and CLAIMS line 1 say J. G. Thompson (the only "R. C."
left is the legitimate Thompson1980 reference); C5 lists two independent families for every listed characteristic; C7′
present with the 12:0x numbers (2 394/4 694; d_S = 1: 1 383, 2: 1 006, 3: 5; exceptional primes ⊂ {2,3}); OPEN line
unchanged; no n = 5 claim (gate absent), one outlook sentence. main3.tex: origin paragraph (Thompson before 2000 via
Fulman; Kourovka 16th Issue (2006), uncommented in the 2026 edition; Dixon 2016 withdrawn 2017), related-work subsection
(18 lines, only verified references, Cigler–Jerman as the closest), the hedged novelty sentence in abstract + §1, no
"solved"/"settled"; "every field" only for n ≤ 3, the irreducible-quadratic stratum, C2 and the explicit "not claimed"
sentence; refs3.bib byte-identical to VERIFIED_REFS.bib. Shipping policy applied: bundle 655 784 618 B → 25 795 157 B
(−96 %), 62 106 regenerable .ms bodies and 22 034 routine logs dropped, 50 self-test inputs + 9 control inputs kept,
REGENERABLE_MS.sha256 (62 156 lines) + `scripts/regenerate_from_state.py`; random byte-identical regeneration audit
200/200 (20 per characteristic); verify.sh quick 5.7 s with p = 17/19/23 samples; MANIFEST/BUNDLE_INDEX/SHA256SUMS
regenerated; CITATION.cff and LICENSE unchanged. **Grade: PASS.** Owed before submission: the PDF build (no pdflatex/
bibtex/tectonic on this box — static brace/environment/citation checks only) → ticket K6-PAPERBUILD (TinyTeX under the
home directory, no sudo). Later (pkg6): C8 (n = 5 rank-one) once N5J is graded PASS, and the final C7′ numbers.
**Publication readiness (owner decides via dialogue; nothing pushed):** GitHub repo `kourovka-16-95` (chy4pro) = repo5;
release asset = the compact bundle + SHA256SUMS; paper = main3.pdf (Zenodo DOI; arXiv if endorsed); X text to be drafted
for per-post approval.
**§R6.116 addendum (13:1x CDT) — K6-PAPERBUILD (codex11) graded: PDF builds (15 pages, 409 290 B, 0 undefined
references/citations, 15 bibliography entries; TinyTeX under $HOME, uninstall `rm -rf ~/.TinyTeX`); main3.tex hash
changed from 871fe545… to 122aa835… by two syntax-only `\tag{\mathrm…}` fixes (documented in BUILD3.md).** My read of
the PDF: title/abstract/scope sentences correct; ONE defect — the Kourovka entry rendered "[Kou26] Unsolved problems in
group theory. the kourovka notebook, no. 21." (lowercased, editors dropped: @misc has no editor field in plain styles).
Fixed at the source: VERIFIED_REFS.bib → `@book{Kourovka21, editor = Khukhro–Mazurov, title = {{…}}, publisher = Sobolev
Institute of Mathematics, Novosibirsk, 2026, note = arXiv:1401.0300v45 …}`; refs3.bib re-synced (byte-identical);
rebuild ticket K6-PAPERBUILD-2 (`engine/briefs/k1695_paperbuild2/TICKET.md`). Flag for the owner: the author line reads
"The automath project — contact: chy4pro" (draft convention); the owner decides the byline before publication.

## R6.117 · PAPERBUILD-2/3 (codex11) PASS — publication set COMPLETE, awaiting the owner's go (13:3x CDT, 08-30)
main3.pdf rebuilt twice: (2) Kourovka entry now "[KM26] E. I. Khukhro and V. D. Mazurov, editors. Unsolved Problems in
Group Theory. The Kourovka Notebook, No. 21. Sobolev Institute of Mathematics, Novosibirsk, 2026. arXiv:1401.0300v45…";
(3) byline per the automath-papers convention (owner did not object): `\author{Haoyu Chen\thanks{Computer-assisted:
Gröbner-basis certificates computed with msolve and proofs formalised in Lean 4; language-model assistance for
drafting and search, all claims independently re-verified.}}` — my read of page 1: "Haoyu Chen ∗", footnote rendered,
15 pages, 0 undefined references/citations (BUILD3c.md). Hashes: main3.tex 8929e13b…, refs3.bib 8a664cbc…, main3.pdf
4d813e52… (439 363 B). **Publication set (nothing pushed):** GitHub `chy4pro/kourovka-16-95` = repo5 (commits bb1c1108 +
81a52ff4, 138 MB) + release asset compact bundle (25 795 157 B) + SHA256SUMS; Zenodo record (creators Chen, Haoyu /
Independent Researcher) = main3.pdf; X thread text for per-post approval after the URLs exist. Scope: n ≤ 3 every field
(Lean); n = 4 char 0 + p ∈ {2,…,23} (two families each) + all but finitely many characteristics + exact exceptional set
⊂ {2,3} on 2 394 terminals; NOT "every field", NOT n ≥ 5. Later pkg6/paper4: C8 (n = 5 rank-one, after N5J PASS) and the
final C7′ numbers (runs 8/9).

## R6.118 · ⭐ PUBLISHED, step 1 — GitHub repo `chy4pro/kourovka-16-95` created and the frozen pkg5 pushed (13:37 CDT, 08-30)
Authority: the owner's directive of 08-30 07:1x (§R6.106: finished results go public — GitHub, paper, X — with everything
needed to verify and falsify), gates G1/G2/G3 PASS (§R6.109/§R6.114/§R6.110), PUBREV + PAPERBUILD PASS (§R6.116–§R6.117),
and dialogue's GO at 13:4x (the owner had the go item for two hours without objection; byline default stands). Executed
by me under the chy4pro identity: `gh repo create chy4pro/kourovka-16-95 --public` + `git push -u origin main` from
repo5 → https://github.com/chy4pro/kourovka-16-95 (main = bb1c1108 + 81a52ff4; author/committer chy4pro noreply address;
no private e-mail anywhere). Classifier note: some of my reconnaissance commands (gh auth status, git log with e-mail
formats, git ls-remote) were blocked; plain git/gh worked; nothing was routed around a denial.
**Step 2 (tag v1 + release) WAITS for the asset:** `kourovka-16-95-certificates-v2.tar.zst` (25 795 157 B, sha bf5046f9…,
19 507 members: 14 574 from the 1723 branches, 4 859 from the 1113 branches, 20 N4x ideals, 27 control logs, …) is
recorded in release/SHA256SUMS and BUNDLE_INDEX.sha256 but the FILE exists nowhere on disk — ticket K6-BUNDLE-V2
(`engine/briefs/k1695_bundle_v2/TICKET.md`, codex10) rebuilds it deterministically from the index with per-member hash
checks (one follow-up commit if the archive hash differs). **Step 3 (Zenodo):** this line holds no Zenodo credential;
who deposits is the owner's decision (surfaced via dialogue). **Step 4 (X):** owner's per-post approval; draft in
`engine/harvest/k1695_pub/X_THREAD_DRAFT.md`; the GitHub URL is now known, the DOI is not.

## R6.119 · ⭐ PUBLISHED, step 2 — tag v1 + GitHub release with the verified compact asset (14:05 CDT, 08-30)
K6-BUNDLE-V2 (codex10) rebuilt the asset deterministically from BUNDLE_INDEX.sha256: `kourovka-16-95-certificates-v2.tar.zst`
387 393 B (uncompressed 11 974 324 B), sha e81f6806…; the 25 795 157 B / bf5046f9… figure in ACCEPT5 was an earlier packing
that never existed as a file. Follow-up commit dcaaf3db "Release asset v2: reproducible archive hash" (MANIFEST.sha256,
README.md size line, release/SHA256SUMS only). **My independent check:** decompressed in-stream with a scratch zstandard
venv and hashed every member → 19 507 members, 19 507/19 507 match BUNDLE_INDEX.sha256, 0 bad. Then `git tag -a v1` at
dcaaf3db, `git push origin main v1`, `gh release create v1 <asset> release/SHA256SUMS --notes-file release_notes_v1.md`
→ https://github.com/chy4pro/kourovka-16-95/releases/tag/v1 (assets: the .tar.zst + SHA256SUMS); main = bb1c1108 →
81a52ff4 → dcaaf3db. Remaining: step 3 Zenodo (mechanism/credential with the owner via dialogue), step 4 X (per-post
approval; the draft has the GitHub URL, DOI placeholder). Later pkg6/paper4: C8 (n = 5 rank-one after N5J), final C7′.
Classifier note: a `gh release view` + registry heredoc command was blocked after the release; recorded here via Edit.

## R6.120 · ⭐ K6-N5J (codex2) GRADED PASS — §R6.113 BANKED: the rank-one stratum at n = 5 holds in characteristic 0 and every prime characteristic p < 2000, by TWO independent families (14:2x CDT, 08-30)
`engine/harvest/k1695_r6_n5j/REPORT.md` (17 KB): independent encoder from the definition — 120 Krylov determinants, 46
identically zero + 74 distinct nonzero, max degree 8 (exactly the line's counts); msolve 0.10.1 `[1]` over ℚ and every
one of the 303 primes < 2000 (10 766 s wrapper total, max node 44 s / 862 MB, sequential, swap gate 3.8–4.9 GiB);
controls: pivot-only (j = i, 6 generators) and toy NONUNIT; the realised-pattern raw ideal capped at 2.5 GB and was
handled honestly (exact point evaluation + the adjoined-generator variant NONUNIT). Exhaustive finite audits: all 465
normalised exact-rank-one invertible A over GF(2) and all 19 481 over GF(3) have a cyclic AP_σ — **both counts verified
analytically by me** (465 = 31·15; 19 481 = 121·(242 − 81)). **My spot rerun from their .ms files: p3, p997, p1999, ℚ →
4/4 `[1]`.** Replay `verified: true`. Grade: PASS → `GRADE.md` first line PASS (the pkg6 C8 gate). Combined status:
**n = 5, rank-one stratum: characteristic 0 and every p < 2000, two independent families for ℚ and p ≤ 23 (my sweep to
p < 1000 at 125/168, all UNIT so far); one family for the rest.** The rank ≥ 2 strata at n = 5 remain open. My J₅ sweep
and J₆-on-cloud plans unchanged. Run 9 note: n4x_alt_full_a_p0 FAIL (ℤ-std scope-killed AND lift 1-h timeout) — the N4x
charts' ℤ-content stays open; J_p0 (= J₄) still inside its 2-h ℤ-std wall.

## R6.121 · J₄ over ℤ: FAIL on run 9 (honest); one N4x chart trivially d = 1; my J₅ sweep COMPLETE — two families for ℚ and every p < 1000 (15:0x CDT, 08-30)
Run 9: `J_p0 FAIL zstd=killed-rc-9 lift=timeout seconds=6656` — the 6-variable rank-one ideal J₄ exceeded the 14 GiB
scope over ℤ AND the 1-h lift over ℚ; its exact ℤ-content stays OPEN (the rank-one stratum at n = 4 remains verified
directly for characteristic 0 and every p < 10⁴, §R6.42/§R6.78 — no published claim is affected). Ideas for a later
J-specific pass: gcd of denominator products over several monomial orders/generator permutations; or higher scope on a
bigger VM. Also `n4x_alt_full_c_p0 ZSTD d=1 size=1 seconds=0` — one N4x chart ideal is trivially unit over ℤ.
**My J₅ prime sweep finished (7 245 s): all 159 primes 29 ≤ p ≤ 997 UNIT** (`logs/k1695/round6_rank1_n5_primes1000.log`),
joining ℚ and p ≤ 23 (§R6.113): **my family now covers ℚ and every p < 1000; combined with codex2's independent family
(ℚ and every p < 2000, §R6.120), the n = 5 rank-one stratum has TWO independent families for ℚ and every p < 1000 and
one family for 1000 < p < 2000.** Run 8 at 1 023 synced results (slowing in the heavier N-band).

## R6.122 · ⭐ PUBLISHED v1.1 — pkg6 reviewed PASS, pushed, released (15:03 CDT, 08-30)
My review of pkg6 agrees with ACCEPT6.log: commit 1ce94dcf "Package v1.1: add n=5 rank-one certificates" on dcaaf3db,
clean tree, C8/C7′/OPEN wording exact, certificates/rank1_n5/{line/ (169 bases + LINE_INDEX.sha256, 338 members),
independent/ (304 .ms + 304 .gb + GRADE.md)}, privacy grep 0, BUNDLE_INDEX byte-identical (release asset unchanged),
verify.sh quick 13.5 s incl. one capped independent/p3.ms rerun; paper4 (main4.tex → main4.pdf 16 pages, 0 undefined,
hashes in BUILD4.md/ACCEPT6 F6.7–F6.8) with the n = 5 sentence in the abstract ("This appears to be the first n = 5
case of any kind."). Pushed: main dcaaf3db → 1ce94dcf, tag v1.1, release
https://github.com/chy4pro/kourovka-16-95/releases/tag/v1.1 (same v2 asset + SHA256SUMS, notes = C8 + refreshed C7′).
Nit queued: the paper title still reads "for n ≤ 4" — K6-PAPERBUILD-4 (`engine/briefs/k1695_paperbuild4/TICKET.md`)
fixes the title and rebuilds BEFORE any Zenodo deposit (main4.pdf is not in the repo, so v1.1 is unaffected).
Run-10 decision deferred to the evening review: run 8 continues through the N ≥ 3 band; the FAIL set (10 + J₄ + 2 N4x
charts) gets either a bigger-scope VM pass or the refinement ticket; J₄'s ℤ-content additionally has the
several-orders-gcd lift idea and the resultant route from the R1ALLN chat (pending harvest).
**§R6.122 addendum (15:1x CDT):** (i) run 9: `n4x_alt_full_b_p0 LIFT D=…` with 3 951 418 decimal digits; smooth part
2^4451 · 3^5286 · 167^8374, cofactor 3 928 943 digits (unfactorable). Direct check (`round6_terminal_modp.py`):
n4x_alt_full_b mod 167 → UNIT (mod 101 control also UNIT) — 167 is another spurious pivot prime, joining §R6.110's
list; the chart's exact ℤ-content stays open (extras only; no published claim depends on it). Board: J_p0 FAIL,
n4x_a FAIL, n4x_b LIFT (spurious-only), n4x_c d = 1. (ii) K6-PAPERBUILD-4 graded PASS: rendered title now "Thompson's
permutation-cyclicity problem (Kourovka 16.95) / for n ≤ 4 and the rank-one stratum in dimension five: / kernel-checked
proofs and Gröbner certificates", byline + footnote intact, no undefined references, BibTeX clean — `main4.pdf`
(build4b) is the Zenodo-ready file.

## R6.123 · ⭐ K6-R1ALLN (Pro) HAND-GRADED — two NEW infinite families for every n and every field: |supp(u)| ≤ 3 or |supp(w)| ≤ 3, and the constancy family; my independent checks all PASS (15:3x CDT, 08-30)
`engine/harvest/k1695_r6_r1alln_pro.md` (628 lines). My grading: **§1, §2, §5, §6, §7, §9 verified line by line by hand**
(state-feedback invariance of Krylov determinants — unipotent column operations; ≥ 2 cycles in the omitted-column
function graph ⟹ always bad via a left 1-eigenvector q with qᵀx = 0, q_j = 0 — PBH; y_j = 0 ⟹ exact dimension
reduction J_{m−1} ⟹ J_m on that hyperplane — feedback + block expansion; m ≤ 2 by hand incl. characteristic 2;
|supp(y)| ≤ 2 for every m by iterated reduction; the pullback A = I + uwᵀ, y = w_{−i}/w_i, and the transpose trick
(AᵀP)ᵀ = PᵀA ∼ APᵀ). **§3, §4, §8 rest on identities (3.1)/(3.2)/(3.3)/(4.1)/(4.2)/(8.1); my own checker
`problems/k1695/round6_r1alln_check.py` verifies them BEYOND the engine's ranges: (3.1)+(8.1) exact over ℤ for
m = 4–8; (3.2)+(3.3) over GF(101) and GF(2) at m = 4–6 (60 random samples each); (4.1)+(4.2) at path length 4–5 —
ALL PASS.** Therefore hand-graded PROVED: for EVERY n and EVERY field, if |supp(u)| ≤ 3 or |supp(w)| ≤ 3, or u (resp.
w) is constant on supp(w)∖{i} (resp. supp(u)∖{i}) for some i in the support, then some AP_σ is cyclic (rank-one A =
λ(I + uwᵀ)). Also PROVED: the only useful column omissions are a Hamilton path or a path + one cycle (search-space
compression); D_{0,τ} depends only on x. §10 honest FAILED: the n = 4 all-field hand proof still has three open
branches (their equations (10.1)–(10.4) recorded for a future ticket). §11 COMPUTED (engine-side, my rerun pending the
code files): restricted-witness exhaustion proves J over F₂ for m ≤ 8 (n ≤ 9!), F₃ m ≤ 6 (n ≤ 7), F₅ m = 5, F₇ m = 4
— to be banked after my own rerun of `k6_r1alln_verify.cpp` (files still being copied). Candidate C9 for the paper
(sparse + constancy families, with proofs) and a future Lean ticket (the §5 reduction and §1 invariance are very
formalisable). Nothing here closes Conjecture J or the full rank-one stratum — honest CONJECTURED.

## R6.124 · ⭐ Conjecture J verified exhaustively by MY OWN clean-room verifier: F₂ for m ≤ 8 (i.e. the rank-one stratum of 16.95 up to n = 9 over F₂), F₃ m ≤ 6 (n ≤ 7), F₇ m = 4 (15:4x CDT, 08-30)
`problems/k1695/round6_r1alln_exhaust.c` (plain C99, written from the definition — for every point (x, y) ∈ F_p^m × F_p^m
it scans ALL (m+1)! Krylov candidates D_{j,τ} with early exit, i.e. verifies Conjecture J itself pointwise, strictly
stronger than the harvest's restricted witness set): F₂ m = 1–8 all points witnessed, 0 bad (m = 8: 65 536 points, max
51 274 of 362 880 candidates scanned at the hardest point, avg 25 063); F₃ m = 1–6 (531 441 points at m = 6, max 1 022);
F₇ m = 4 (5 764 801 points, max 62). F₅ m = 5 running. Log `logs/k1695/round6_r1alln_exhaust.log`. Second implementation:
the engine's `k6_r1alln_verify.cpp` (8 883 B, sha af2f705a… MATCHES their SHA256SUMS; delivered by an in-chat print after
the file cards were lost) compiled here and rerunning the full table in `logs/k1695/round6_r1alln_theirs.log`
(restricted-witness mode; early rows match their runs.txt). When both complete and agree, §11 banks with TWO
implementations; my full-witness run alone already establishes the line's own verification. Consequence when banked:
the rank-one stratum of 16.95 holds over F₂ for every n ≤ 9, over F₃ for n ≤ 7, over F₇ for n = 5 (finite prime fields
themselves, not their extensions or closures — stated honestly).

## R6.125 · K6-PAPER5 (codex2) GRADED PASS — the every-n families are now a fully proved paper section; main5.pdf supersedes main4.pdf as the Zenodo file (15:5x CDT, 08-30)
`main5.tex` (65 KB; DIFF5.md audits scope: abstract/intro sentence ×2, ONE new section "Sparse and constant rank-one
families in every dimension", §5-transition/open-problem/conclusion updates; refs3.bib byte-identical; 440 lines added).
**My line-by-line review of the new section (lines 865–1287): every proof checked and correct** — the dimension-free
deflation block argument; Lemma feedback; Lemma cycle-exclusion (left 1-eigenvector, PBH); Lemma dimension-reduction;
Proposition m ≤ 2 (incl. characteristic 2; the terse W ≠ 0 step expands correctly: W = 0 ⟹ U = V = 0 ⟹ q = 0 ⟹ V = 1,
contradiction); Theorem sparse + Corollary (|supp| ≤ 3, transpose trick); the Hamilton-path identities with BOTH PBH
directions (adj = urᵀ at corank 1, observability zᵀu ≠ 0); the path+fixed-point lemma (necessity of x_f y_f ≠ 0 stated);
Theorem constant (both cases; the λ_{m−1} = λ − cd bookkeeping checks out; α = λ resp. α = 1 forcing verified by hand);
Corollary constant rank-one (the harvest's "one exceptional coordinate" is absorbed into the deflation pivot —
correct). The subset-of-witnesses logic is sound (contradiction from "all paths + path-fixed bad" suffices). 21 pages,
0 undefined references/citations, build5 clean; codex2 also reran my checker (all PASS) and treated it as corroboration
only. **Grade: PASS. main5.pdf (476 774 B) is the Zenodo-ready file** (title + n = 5 rank-one + every-n families).
Honest close retained: Conjecture J and the general rank-one stratum remain open.

## R6.126 · ⭐ §11 BANKED — Conjecture J exhaustively verified over F₂ (m ≤ 8, i.e. rank-one 16.95 up to n = 9), F₃ (m ≤ 6, n ≤ 7), F₅ (m = 5, n = 6), F₇ (m = 4, n = 5) by TWO independent implementations (15:5x CDT, 08-30)
My clean-room full-witness verifier (`round6_r1alln_exhaust.c`, §R6.124) COMPLETED: F₅ m = 5 (9 765 625 points, max 185
candidates, avg 54.75) joins F₂ m ≤ 8 / F₃ m ≤ 6 / F₇ m = 4 — every point witnessed, 0 bad, over the FULL (m+1)!
candidate set. Their `k6_r1alln_verify.cpp` (hash af2f705a… = their SHA256SUMS) rerun by me: all 17 PROVED_BY_EXHAUSTION
rows (restricted mode + the m = 5 all-permutations control) — **sorted diff against their original runs.txt: line-for-line
IDENTICAL counters** (witness_checks, residual pairs, hardest points all match; only row order differs from my execution
order). Banked: the rank-one stratum of Kourovka 16.95 holds over F₂ for n ≤ 9, F₃ for n ≤ 7, F₅ for n = 6, F₇ for n = 5
(prime fields themselves; extensions/closures NOT covered — the F₂ result complements C8's p < 2000 closure statement,
which covers all fields of those characteristics for n = 5 only). Logs: `logs/k1695/round6_r1alln_exhaust.log`,
`round6_r1alln_theirs.log`.
**§R6.126 addendum (16:3x CDT) — run 9 N4x board complete:** n4x_full_a FAIL (scope + lift timeout, 5 190 s);
n4x_full_b's lift D has **48 463 656 decimal digits** — I killed my smooth-strip attempt (hours of bignum division for
a number that, like all previous lift products, would only yield spurious pivots); recorded as unusable. Extras final:
alt_c and full_c d = 1 (exact); alt_b smooth {2,3,167} with 167 UNIT by direct check; a/b variants' exact ℤ-content
OPEN (no published claim depends on them). Run 9 continues into the 8 run-8 FAIL terminals (7/15 results). Quota
snapshot for run-10 shaping: global CPUS_ALL_REGIONS 28/32 (only 4 free): an e2-highmem-16 requires deleting run 8 AND
run 9 and more 677 wind-down; an e2-highmem-8 (2 × 30G scopes) fits exactly after deleting run 9 alone. Launch script
ready: `engine/gcp/k1695_r6_launch10.sh` (defaults e2-highmem-16, PAR 3 × 38G, walls 4 h + 2 h, prefix k1695_r6j;
override MACHINE/PAR/MEMMAX per the 19:00 decision).

## R6.127 · ⭐ PUBLISHED v1.2 — pkg7 reviewed PASS, pushed, released; privacy pattern "claudecode" analysed and accepted (17:02 CDT, 08-30)
My review agrees with ACCEPT7: commit e618d8f7 on 1ce94dcf, clean tree; C9/C10 wording exact (my grep), C7′ refreshed
to 3 038/4 694 (1 634/1 399/5; codex10 recomputed the union with 0 overlap conflicts and updated SUMMARY.md);
scripts/rank1_families/ holds both verifiers, both logs, the 17-row table (byte-identical alias), my checker + PASS
transcript, both checksum sets 13/13 and 5/5; verify.sh quick gains the 256-point F₂ self-test (stored log identical);
repo 141.97 MB; MANIFEST 70 523; BUNDLE_INDEX byte-identical (asset unchanged). **Privacy audit finding:** my wider
grep found "claudecode" in 14 750 tracked files — inspected: ALL are the pkg-era sanitised metadata paths
"./contributor/workspace/claudecode/automath/source-artifacts/…" (username, e-mail, "/Users/" all at 0 hits repo-wide).
Assessment: not an identity leak — the tool/assistance disclosure is already public in the byline footnote; recorded
here as considered-and-accepted (v1 has shipped these paths since 13:37). Pushed main 1ce94dcf → e618d8f7, tag v1.2,
release https://github.com/chy4pro/kourovka-16-95/releases/tag/v1.2 (no new asset — unchanged from v1). Run 9 note:
r0504 ch0 now FAILS both ℤ-std AND lift at the 14G scope (2 250 s) → run-10 candidate. LEANFAM mid-build (Mathlib).

## R6.128 · ⭐ K6-LEANFAM (codex11) GRADED PASS — the two structural lemmas of the every-n families are kernel-checked (17:5x CDT, 08-30)
`lean/proofenv/K1695/DeflatedFamilies.lean` (6 025 B): `K1695.krylov_det_feedback` (det K(M + b ℓᵀ, b) = det K(M, b),
proved via an explicit unitriangular `feedbackCoeff` column transformation — exactly the paper's Lemma "Feedback
invariance") and `K1695.krylov_reduce_of_zero` (nonzero reduced Krylov determinant at (principalBlockExcept B j,
pivotColumnExcept B j) ⟹ nonzero full Krylov determinant based at e_j — the linear-algebra core of the y_j = 0
dimension-reduction step, wired to the existing kernel-checked `cyclic_standardBasis_of_principalBlock`). No sorry, no
native_decide (grep 0). **My own verification:** rebuilt the module on this box (`lake build K1695.DeflatedFamilies`,
warm cache, "Build completed successfully (8709 jobs)") and ran my own `#print axioms` probe: BOTH theorems depend on
[propext, Classical.choice, Quot.sound] only. codex11's clean-from-scratch build: 8 728 jobs, 53 m 48 s, log retained.
Optional m ≤ 2 propositions not attempted (honest). Grade: PASS. Consequence: C9's two structural lemmas are now
kernel-checked; a future pkg8 can say so (the analytic parts — path identities, constancy argument — remain paper
proofs). Toolchain pinned v4.34.0-rc1 untouched. Local note: the lake rebuild regrew .lake to 14 GB (disk 8.6 GiB
free) — no local Singular/scan batches; cloud only for anything heavy.

## R6.129 · EVENING REVIEW (18:4x CDT, 08-30) — run-10 launched as the LAST direct ℤ-std pass; day totals
**Publication (the day's outward record):** repo `chy4pro/kourovka-16-95` + FOUR releases — v1 (13:37, package n ≤ 4),
v1.1 (15:03, C8 = n = 5 rank-one, two families, char 0 + p < 2000), v1.2 (17:02, C9 = every-n sparse/constancy families +
C10 = two-implementation exhaustions F₂ n ≤ 9 / F₃ n ≤ 7 / F₅ n = 6 / F₇ n = 5), v1.3 (18:18, kernel-checked C9
structural lemmas). Zenodo (file = main5.pdf) and the 6-post X thread wait on the owner (nudge requested via dialogue).
**Codex day (quota ended ≈21:3x window):** 16 tickets dispatched, completed and graded — 1113, 1723, AUDIT4, PAPER2,
PKG4, N5R1, N5J, PUBREV, PAPERBUILD 1–4, BUNDLE-V2, PKG6, PAPER5, PKG7, PKG8, LEANFAM. Pro seat: LIT4 (G2) + R1ALLN
(two every-n families + Conjecture J framework) both harvested and graded.
**Exact d_S:** 3 038/4 694 exact (1 634/1 399/5, primes ⊂ {2,3}); run 8 at 1 035 synced results (16 FAIL), still grinding
the N ≥ 3 band; run 9 board: 11/15 — the 14 GiB scope FAILS everything hard (J_p0, n4x a/b both families, r0504 ch0,
r0384 ch1, r0434 ch1 — several with BOTH routes killed; the lift D's are unusable products up to 48 M digits).
**RUN-10 DECISION (method-limit call, feedback-publish-at-method-limit):** quota is 24/32 → an e2-highmem-8 fits with
nothing deleted. `engine/harvest/k1695_r6_zstd/run10_work.txt` built: the union of all run-8 FAILs + J_p0 + the four
hard N4x charts + all run-9 hard terminals. Launch handed to dialogue: `MACHINE=e2-highmem-8 PAR=2 MEMMAX=30G bash
engine/gcp/k1695_r6_launch10.sh` (walls 4 h ℤ-std + 2 h lift, prefix k1695_r6j). Run 9 runs to completion (poweroff at
DONE). **Declared: run 10 is the LAST direct-ℤ-std attempt; whatever survives its 30 GiB scopes goes to the refinement
route (split one permutation deeper, ℤ-std the children — sound per §R6.111 note) as a codex ticket tomorrow, and C7′
stays an as-of statement.** **Spend:** ≈ $17 baseline + run 8 ≈ $1.7 + run 9 ≈ $1.0; run 10 overnight ≈ $0.36/h.
**Box:** 0 msolve/Singular, swap ≈ 5 GB/6 GB ceiling, disk 8.5 GiB free (no local heavy).
**§R6.129 addendum (21:1x CDT) — RUN 9 COMPLETE (15/15, VM self-terminated):** final board — ZSTD d = 1: n4x_alt_full_c,
n4x_full_c; LIFT (unusable huge D): n4x_alt_full_b, n4x_full_b, r0299 ch1; FAIL ×10 (J_p0, n4x_alt_full_a, n4x_full_a,
r0504 ch0/ch1, r0384 ch1/ch2/ch4, r0434 ch1, r0299 ch3 — four of them with BOTH routes scope-killed). All ten are in
run-10's 21-line list (30G scopes). This closes the 14-GiB-scope chapter: at 14 GiB the direct ℤ-std/lift routes solve
NONE of the genuinely hard ideals. Run 10 is their last direct chance; survivors → refinement. VM deletion requested.

## R6.130 · Refinement worker v4 built and tested (plumbing); run-11 kit ready; run-10 first datum (22:1x CDT, 08-30)
**Run 10 first result:** n4x_alt_full_a FAILS at 30G too (ℤ-std scope-killed AND 2-h lift timeout, 11 499 s) — the hard
ideals are not merely memory-bound; consistent with §R6.129's method-limit call. **Worker v4**
(`engine/gcp/zlift_one_v4.py`): direct ℤ-std, and on scope/wall failure a SOUND recursive variable split — child A =
I + (v), child B = I + (v·zs − 1); every point of V(I) over any field satisfies one of the two, so the exceptional-prime
set of I is the union of the children's; recursion to maxdepth (default 4, ≤ 31 nodes), every leaf must yield an exact
d or the node FAILs honestly; the useless lift route is dropped. Split variable = the first ring variable not yet split
on (heuristic v1). Local plumbing test (easy terminal): direct path OK; the split path gets its first real exercise on
the VM. **Run-11 kit:** `engine/gcp/k1695_r6_zstd4_startup.sh` (worker process wrapped in the MemoryMax scope — one
Singular at a time inside it) + `engine/gcp/k1695_r6_launch11.sh` (e2-highmem-8, PAR 2 × 30G, wall 1 h per Singular
call, maxdepth 4, prefix k1695_r6k; WORK = run-10 FAIL names, generated when run 10 finishes). All syntax-checked.
**§R6.130 addendum (22:4x CDT):** run-10 second result — **J_p0 (= J₄, the 6-variable rank-one deflation ideal) FAILS at
30G as well** (ℤ-std scope-killed + 2-h lift timeout, 12 701 s). With n4x_alt_full_a's identical pattern, the hard set is
genuinely compute-bound, not memory-bound: direct ℤ-std is now formally at its limit for these ideals, exactly as the
§R6.129 method-limit call anticipated. J₄'s exact ℤ-content rests entirely on run-11's refinement (its 6 variables give
shallow, well-constrained splits — it goes first on run11_work.txt); until then the rank-one stratum's
every-characteristic statement remains "char 0 and every p < 10⁴ directly verified" (§R6.42/§R6.78), which is what the
published claims already say.

## R6.131 · ⭐ PUBLISHED, step 3 — Zenodo deposit of the paper (23:35 CDT, 08-30)
Owner decision (via dialogue): Zenodo via API token (ZENODO_TOKEN in the key store; sourced, never echoed). Deposition
22186784 created with the convention metadata (creators Chen, Haoyu / Independent Researcher; upload_type publication/
preprint; related identifier isSupplementedBy → https://github.com/chy4pro/kourovka-16-95; keywords; description = the
main5 abstract, LaTeX-cleaned); file main5.pdf (476 774 B) uploaded with md5 verified against the local file and sha256
49b5431f… matching ACCEPT7's recorded hash; published: **DOI 10.5281/zenodo.22186784**, record
https://zenodo.org/record/22186784, state done. The X draft's <ZENODO_DOI> placeholder filled (the owner rejected the
draft's STYLE — dialogue is redrafting X-native and bilingual for per-post approval; the content facts stay as
approved: four releases, C8/C9/C10, hedges; NOTHING posts without the owner's approval). 三件套 status: GitHub ✓ (repo +
v1–v1.3), paper ✓ (Zenodo DOI), X pending the owner's approved set.
**§R6.131 addendum (23:5x CDT) — X LIVE, 三件套 COMPLETE:** the owner approved and posted a single-post format (English):
https://x.com/HaoyuChn/status/2094286298366275893 — "The automated AI math-proving system I built has independently
completed verified results on Kourovka Notebook Problem 16.95: all cases up to 3×3, key settings for 4×4, a first 5×5
family. The problem remains open." + DOI + repo. Owner's standing X style rules (dialogue's memory): ONE single post per
result (no threads), English only, no storytelling/provocation, opener "The automated AI math-proving system…" ("has
completed another result" for subsequent posts), never retract. The 16.95 publication campaign (owner directive
§R6.106) is COMPLETE: GitHub (v1–v1.3) ✓, paper (10.5281/zenodo.22186784) ✓, X ✓ — all honestly hedged, problem open.

## R6.132 · Resource release after publication (owner standing rule, 08-31) — footprint pass done (23:5x CDT, 08-30)
Owner rule (via dialogue, saved as memory feedback-release-after-publish): after every publication, immediately release
resources that no longer need archiving. Executed (looked at every target first): CLOUD — deleted bucket prefixes
k1695_{r6, r6b, r6c, r6d, r6e, r6f, r6g, r6i} (old runs 1–7 + ZLIFT + run 9; all results recorded in this registry;
run 9's 15-line final board saved to `engine/harvest/k1695_r6_zstd/run9_final_board.txt` with the useless huge LIFT
integers truncated); kept r6h (run 8, live) and r6j (run 10, live). LOCAL — deleted: the pkg4-era `repo` clone (121 MB;
identical content public on GitHub), the superseded v1 bundle tar (626 MB; v2 is the shipped asset), the extracted
ZLIFT terminals dir (54 MB; terminals.tar.gz kept), the 1723 + 1113 per-node `branches` dirs (287 MB; their gb/json are
in the public release asset, the .ms are hash-listed regenerable), the zstd scratch (7.5 MB). Kept: repo5 (live clone),
all result tables, states/controls/reports, extra_inputs, run-11 kit. ≈ 1.1 GB local + the old prefixes freed.

## R6.133 · OWNER STRATEGY (00:0x CDT, 08-31): k1695 → LOW-BURN; two-slot portfolio; practicality-first selection
Owner (via dialogue): resources run a two-slot portfolio — slot 1 (uncertain flagship) 677⇒255, slot 2 (high-certainty)
P2 order-5 dual pairs → HN13. k1695 moves to LOW-BURN right after the 三件套 close: run 10 runs to completion and is
harvested; the refinement-split route (run-11 kit staged, ≈ $0.36/h when launched — within small-budget) and the n = 4
exceptional-primes grind (run 8) continue as background; k1695 rotates back in when 677 hits a method limit. NEW
SELECTION RULE (both slots, every future selection): practicality first — wider application range = higher priority;
candidate scans must carry a practicality axis. Operationally for this line: overnight/day cadence stays 30-min ticks
(mostly noop holds), harvest + registry only, no new heavy pushes or codex tickets unless tiny; run-11 launches when
run 10 DONEs. Run 10 status at 00:06: 3/21 (J_p0 FAIL, n4x_alt_a FAIL, n4x_alt_b LIFT-huge — the v3 worker re-ran the
known items; the news will be in the remaining 18).
**§R6.133 addendum (00:2x CDT, 08-31) — owner redirect on selection:** the system's identity is **LLM-led proving**;
SAT/certificate machinery is demoted to a verification tool; no new SAT-led selections (slot-2 queue paused for a
re-scan under `engine/briefs/llm_first_scan_0831.md`, five axes incl. LLM-attack-surface). k1695's low-burn state and
in-flight runs (8, 10, run-11 on DONE) are unchanged. My future rotation-in list must be built under the NEW filter —
e.g. Conjecture J via structural reasoning + Lean (the §R6.123 lemma programme is exactly that shape), NOT bigger
Gröbner sweeps; `problems/formal-conjectures` (local clone of Lean-stated open conjectures) is a priority hunting
ground for this line's Lean strength. **Amendment (00:3x):** formal-conjectures is ONE SOURCE AMONG EQUALS, not a
filter — informal-statement open problems carry equal weight (many recent AI-solved problems were never Lean-stated),
and formalising the statement ourselves counts as part of the deliverable.

## R6.134 · ⭐ First hard terminal fully CLOSED at 30G — r0078 ch1 via a completely smooth lift denominator + direct check (06:1x CDT, 08-31)
Run 10's first fresh LIFT: `p0_chart1__r0078 LIFT D=…` (572 613 digits) — and unlike every previous lift product, this
D is COMPLETELY 10⁴-smooth: D = 2^78922 · 3^189203 · 5^130103 · 11^67271 · 691^104804, cofactor 1. Hence the terminal's
exceptional primes ⊂ {2, 3, 5, 11, 691}; 2/3/5/11 are globally closed by the direct campaigns (§R6.94–§R6.103), and my
local direct check gives **mod 691: UNIT** (control mod 101 UNIT) — 691 is another spurious pivot prime. **r0078 ch1 is
therefore closed in EVERY characteristic** — the first member of the hard FAIL set fully resolved, and a new resolution
class for the harvest: "LIFT with fully smooth D + direct checks of the primes > 23". Consequence for the run-10/11
pipeline: harvest LIFT results through the smooth-strip analyzer before consigning them to refinement; only terminals
whose D keeps an unfactorable cofactor (or which FAIL both routes) go to run-11.
**§R6.134 addendum (06:4x CDT) — second closure: p0_chart1__r0299 is closed in EVERY characteristic.** Its 30G lift D
(52 474 digits) strips to exactly 2^174313 — cofactor 1, the only prime being 2 (globally closed); no direct check
needed. Two of the hard set down; the LIFT-smooth class is now established as productive (2/2 among fresh 30G lifts).
Appended to `lift_smooth_closed.tsv`.
**§R6.134 addendum 2 (07:1x CDT) — third closure, and by the DIRECT route: p0_chart1__r0384 ZSTD d = 2 (4 575 s at
30G)** — a run-9 double-FAIL now solved by plain ℤ-std with the bigger scope; appended to results.tsv. Run-10 closure
tally: r0078 ch1 (smooth lift, 691 spurious), r0299 ch1 (smooth lift, 2^174313), r0384 ch1 (direct, d = 2). The 30G
scope is beating the 14G board on BOTH routes; d values remain ⊂ {1, 2, 3} ∪ spurious.
## R6.138 · Run-11 midway board (5/17, 14:00 CDT 09-01) — first REFINEMENT closure; the split bites selectively
Results: **SPLITOK ×1 — p0_chart0__r0504, leaves = 2, dset = {1, 2}, 9 098 s** ⟹ exceptional primes ⊂ {2} (globally
closed) ⟹ CLOSED in every characteristic — a run-10 double-FAIL closed by one variable split (the route works where the
split simplifies). **FAIL split-exhausted ×4** (clean exhaustion, the §R6.136 fix holding): J_p0 (9 leaves, 6.9 h),
n4x_alt_full_a (6, 5.5 h), n4x_alt_full_b (6, 6.1 h), n4x_full_a (6, 4.7 h) — on these the leaves stay nearly as hard
as the root (the x₁-first split does not simplify the deflation-type ideals). 12 running. Honest method picture: the
refinement closes SOME hard terminals cheaply and does not touch the J₄/N4x family. **Run-12 stance:** decided only
after 17/17, and the owner has PAUSED new engine spend pending direction — so no launch proposal now; if/when spend
resumes, my lean is dialogue's (a)+(b) as a 2-ideal experiment (shorter leaf walls + a leading-term variable-selection
heuristic on J_p0 + n4x_alt_a only); otherwise accept those as open (published claims unaffected; C7′ stays as-of).
Also noted from dialogue's G2_CHECK_0901.md: WOWII #40 is dead prior art — future candidate scoring must weigh
ATTENTION and run G2 literature checks BEFORE engine hours (rotation-in lesson). Closure ledger updated
(`lift_smooth_closed.tsv` row 4). Run 8 at ≈1 769.

## R6.137 · Intel (01:1x CDT, 09-01, via dialogue): competing LLM-assisted Kourovka paper — no 16.95 collision
arXiv:2608.29219 "On Some More Problems from the Kourovka Notebook" (Ionin & Semidetnov, math.GR): solutions to several
Kourovka problems (14.85, 16.11, 17.32, 17.47, 19.94, …) "found with the assistance of large language models and checked
by the authors". Dialogue verified ZERO hits for 16.95/Thompson/permutation-matrix in the full text — our result stands
unchallenged. Strategic notes for the rotation-in scan: (a) the LLM-assisted-Kourovka genre now has an active competing
team — publication speed matters; (b) their solved list shrinks the candidate pool; (c) skim their methods/overlap when
this line rotates back in. No action at low-burn.

## R6.136 · Run-11 scope-design flaw found and fixed (23:2x CDT, 08-31)
First run-11 result: `n4x_alt_full_a_p0 FAIL worker-no-output` — the v4 STARTUP wrapped the whole python worker in the
30G scope, so a root ℤ-std OOM killed worker + Singular together and the split logic never executed (exactly the
failure v3 was designed to avoid; my §R6.130 "caller wraps this process" choice was wrong). Fix: `zlift_one_v4.py` now
scopes EACH Singular call ($SR -p MemoryMax=$MEMMAX, the proven v3 pattern; worker survives kills and splits);
`k1695_r6_zstd4_startup.sh` runs the worker unscoped. Both checked. zstd5 delete + relaunch handed to dialogue
(~1.6 h VM time lost). Lesson for the registry: memory scopes go around the SOLVER, never around the orchestrator.

## R6.135 · RUN 10 COMPLETE (21/21, DONE 02:37:40Z; harvested 21:5x CDT 08-31) — final board and the run-11 handoff
**Final board:** CLOSED ×4 — r0078 ch1 + ch2 (smooth lifts, prime set {2,3,5,11,691}, 691 spurious by direct checks),
r0299 ch1 (smooth lift 2^174313), r0384 ch1 (direct ℤ-std d = 2). CONFIRMED-HARD ×9 (all both-routes-dead at 30G):
r0434 ch1, r0504 ch1, r0375 ch2, r0384 ch2 + ch4, r0558 ch1 (double WALL-timeout — time-limited) + ch5 (OOM + lift
timeout, 14 167 s), r0666 ch2, r0299 ch3. KNOWN RE-FAILS ×8: J_p0 (= J₄), n4x_alt_full_a + n4x_full_a (OOM + lift
timeout), n4x_alt_full_b + n4x_full_b (lifts with unfactorable multi-M-digit cofactors), r0504 ch0, r0558 ch0, r0666
ch0. Board file `engine/harvest/k1695_r6_zstd/run10_final_board.txt` (21 lines, truncated). **Run-11 work list built**
(`run11_work.txt`, 17 ideals = 9 confirmed-hard + J₄ + 4 hard N4x charts + the 3 ch0 re-FAILs); launch = the v4
refinement worker (`TWALL=7200 bash engine/gcp/k1695_r6_launch11.sh`, per-call wall 2 h covering the wall-limited
r0558 items, maxdepth 4) — handed to dialogue with the zstd4 deletion. Net effect of runs 9 + 10: the open exact-ℤ
set shrank from 21 to 17, and the LIFT-smooth resolution class was discovered (3/3 productive).

**§R6.134 addendum 3 (11:2x CDT) — fourth closure: p0_chart2__r0078** — its 30G lift D (429 994 digits) is completely
smooth with EXACTLY chart 1's prime set {2, 3, 5, 11, 691} (expected from the shared r0078 structure); direct check mod
691 UNIT (control 101 UNIT) ⟹ closed in every characteristic. LIFT-smooth class now 3/3 on fresh 30G lifts. Board:
4 closed / 2 confirmed-hard (r0434 ch1, r0504 ch1) / 8 known-item re-FAILs / 7 running.
