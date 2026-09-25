# TICKET K6-N4 — Kourovka 16.95 for n = 4 over EVERY field: verify one lemma, break or prove the rest

Self-contained. Work only from this file. Do not search the internet. Deliver MATHEMATICS WITH
MACHINE CHECKS, not an essay. Write everything to the directory
`engine/harvest/k1695_r6_n4/` (create it): a report `REPORT.md`, every script you run, every
log. End the report with the literal line `DONE-K6N4`. Exact arithmetic only (no floating
point anywhere). Every finite field GF(q) you use must be built in your own code with its axioms
self-checked (associativity/distributivity/inverses) before use. Time budget: as long as it takes,
but print progress; if a computation would exceed ~30 min, shrink the window and STATE the window.

## 0. The problem and the conventions
**Kourovka 16.95 (J. G. Thompson, 2006).** For every field F and every A ∈ GL(n,F) there is a
permutation matrix P with AP *cyclic*, i.e. nonderogatory: minimal polynomial = characteristic
polynomial ⟺ dim ker(AP − μI) ≤ 1 for every μ in an algebraic closure F̄ ⟺ rank(AP − μI) ≥ n−1
for every μ ∈ F̄.

Conventions: `P_σ e_j = e_{σ(j)}` (so `A P_σ` has columns `a_{σ(1)},…,a_{σ(n)}`). For a
transposition τ = (a b) write `d = e_a − e_b`; then `P_τ = I − d dᵀ` and `P_τ⁻¹ = P_τ`.
Everything below is over an arbitrary field F unless a finite field is named.

**Known (do not re-prove, may use):** 16.95 holds for n ≤ 3 over every field. Cyclicity is a
similarity invariant; `A P_σ` is similar to `P_σ A` and to `P_ρ A P_σ P_ρ⁻¹`. Rank of a rank-one
update: for X ∈ M_n(F̄), x,y ∈ F̄ⁿ, `rank(X + xyᵀ) ∈ {rank X − 1, rank X, rank X + 1}`, and
`= rank X + 1` iff `x ∉ col(X)` and `y ∉ row(X)`.

**The reduction to two strata for n = 4 (proved, may use).** If A ∈ GL(4,F) is derogatory at
μ ∈ F̄ (geometric multiplicity ≥ 2) and m is the minimal polynomial of μ over F, then m² divides
the characteristic polynomial, so deg m ∈ {1,2}.
- Stratum (a): μ ∈ F, hence `rank(A − μI) ≤ 2`, i.e. `A = μ(I + U Wᵀ)` with U, W ∈ F^{4×2}.
  Since cyclicity of AP is invariant under scaling A, WLOG μ = 1: `A = I + U Wᵀ`, and
  rank(UWᵀ) ∈ {1, 2}.
- Stratum (b): deg m = 2, charpoly = m², invariant factors (m, m): the minimal polynomial of A is
  m itself, an irreducible quadratic; over F̄, A is diagonalisable with eigenvalues μ, μ̄ (the two
  roots of m; equal only if m is inseparable), each of geometric multiplicity 2.
A counterexample to 16.95 at n = 4 would have to lie in (a) or (b).

## 1. LEMMA T (transposition lemma) — VERIFY IT, then USE IT
Let A ∈ M_n(F), τ = (a b), d = e_a − e_b, μ ∈ F̄, and E := A − μI, g := dim ker E.
Then `rank(A P_τ − μI) = rank(A − μ P_τ) = rank(E + μ d dᵀ)`, and therefore:
- (T0) if μ ∉ spec(A) (g = 0): `A P_τ` is NOT derogatory at μ.
- (T1) if g = 1, with ℓ spanning the left kernel of E and r the right kernel: `A P_τ` is derogatory
  at μ ⟺ `ℓ_a = ℓ_b` AND `r_a = r_b` AND `1 + dᵀz = 0` where z is any solution of `E z = μ d`
  (well defined because dᵀr = 0). [μ ≠ 0 here if A is invertible.]
- (T2) if g = 2: `A P_τ` is derogatory at μ ⟺ `d ∈ col(E)` OR `d ∈ row(E)`.
- (T3) if g ≥ 3: `A P_τ` is derogatory at μ for EVERY transposition τ.
In particular (T0): **a transposition can only be derogatory at an eigenvalue of A itself.**

**Rationality rider (T4).** If μ ∉ F with minimal polynomial m over F, then
`col(A − μI) ∩ Fⁿ = col_F(m(A))` and `row(A − μI) ∩ Fⁿ = row_F(m(A))` (col/row spaces over F of
the F-matrix m(A)). Prove this for separable m (Galois descent) and settle the inseparable case
(char 2, m = x² − s) separately — do not wave at it.

**Tasks for §1.**
1a. Give your own proof of T0–T4 (short; the rank-one-update facts above are the whole content).
    If any clause is FALSE, exhibit the (F, A, τ, μ) — that is the most valuable output of the
    ticket and everything else waits on it.
1b. MACHINE CHECK: for every A ∈ GL(n,q) with (n,q) ∈ {(3,2),(3,3),(3,4),(3,5),(4,2),(4,3)} and
    every transposition τ, compute the actual set of μ ∈ GF(q) at which AP_τ is derogatory
    (rank(AP_τ − μ) ≤ n−2; do it over GF(q) itself AND over GF(q²) for the (3,q),(4,2) cells so
    non-rational eigenvalues are exercised) and compare with the prediction of T0–T3 evaluated
    from A's own eigenstructure. Report: population per cell (must equal
    ∏(qⁿ − qⁱ)), number of (A,τ,μ) triples, disagreements (must be 0), AND the number of triples
    where each clause fired (T1-derogatory, T2-derogatory, T3) — a check in which no clause ever
    fires has checked nothing. Include a NEGATIVE CONTROL: deliberately delete the `1 + dᵀz = 0`
    clause from T1 and show the disagreement count becomes positive.

## 2. STRATUM (b) — a claimed PROOF; try to break it, then machine-check its prediction
Claim: **for A in stratum (b) (n = 4), A P_τ is cyclic for EVERY transposition τ.**
Argument: by (T0) a transposition can be derogatory only at μ ∈ {root of m}. There g = 2 and by
(T2) derogatory ⟺ d ∈ col(A − μI) or d ∈ row(A − μI). By (T4), since d ∈ F⁴ ∖ {0} and m(A) = 0,
`col(A − μI) ∩ F⁴ = col_F(m(A)) = 0`, so d ∉ col(A − μI); same for rows. Hence no μ works and
AP_τ is cyclic. ∎
2a. Attack the argument. The suspicious points: (i) the inseparable case (char 2, m = x² − s):
    is A still "diagonalisable with g = 2" — no: then A − μI is nilpotent of rank 2 over F(μ);
    does (T2) still apply and does (T4) still give col ∩ F⁴ = 0? (ii) any hidden use of μ ≠ μ̄.
2b. MACHINE CHECK of the prediction (it is falsifiable): enumerate ALL stratum-(b) matrices over
    GF(2) and GF(3) (union over irreducible monic quadratics m of the similarity class of
    C_m ⊕ C_m; the class has |GL(4,q)|/|GL(2,q²)| elements — assert your enumeration hits exactly
    that count, e.g. by orbit closure under GL(4,q) generators) and test EVERY transposition:
    report `#(A,τ) pairs`, `#cyclic`, `#non-cyclic` (prediction: 0). Also GF(4) and GF(5) if the
    class size (|GL(4,q)|/|GL(2,q²)|) is enumerable within the budget; otherwise sample ≥ 10⁵
    conjugates and say so.

## 3. STRATUM (a) — the open half at n = 4: PROVE IT over every field, or find the counterexample
`A = I + UWᵀ ∈ GL(4,F)`, rank(UWᵀ) ∈ {1,2}. Structure you should use:
- Eigenvalue 1 has geometric multiplicity `4 − rank(UWᵀ)` (= 3 or 2). By (T3), if rank = 1 every
  transposition fails at μ = 1, and more generally a permutation σ can only work if
  `rank(P_σ − I) = 4 − #cycles(σ) ≥ g − 1`: for rank-1 perturbations σ has ≤ 2 cycles (types
  (4), (3,1), (2,2)); for rank-2 perturbations σ has ≤ 3 cycles (transpositions allowed).
- The other eigenvalues of A are those of the k×k matrix `I_k + WᵀU` (k = rank), in F̄.
- For a general permutation σ: `A P_σ − μI = (P_σ − μI) + U (Wᵀ P_σ)`, a rank-k update of
  `P_σ − μI`; `dim ker(X + UVᵀ) = dim ker [[X, U],[Vᵀ, −I_k]]` (bordered matrix), and when
  X = P_σ − μI is invertible (μ not a root of any x^ℓ − 1, ℓ a cycle length) this equals
  `dim ker(I_k + Vᵀ X⁻¹ U)`; for σ an n-cycle, `(I − λP)⁻¹ = (1 − λⁿ)⁻¹ Σ_{j<n} λʲ Pʲ`.
3a. **Rank 2** (this is the piece nobody has touched): prove that some σ ∈ S₄ makes AP_σ cyclic,
    for every field F and all U, W ∈ F^{4×2} with rank(UWᵀ) = 2 and det(I + WᵀU) ≠ 0. Use Lemma T
    for the six transpositions first: when do ALL six fail? (Hint: for the eigenvalue 1 with g = 2,
    (T2) says τ = (ab) fails at 1 iff `e_a − e_b ∈ col(U)` or `e_a − e_b ∈ col(W)`; the graph of
    pairs {a,b} with `e_a − e_b` in a fixed 2-dimensional subspace of F⁴ is a disjoint union of
    ≥ 2 cliques — so two such subspaces cannot cover all six edges of K₄ unless … work it out.)
    Then handle the residual configurations with 3-cycles / double transpositions / 4-cycles.
    A proof that is a finite case analysis is fine PROVIDED each case is closed by an argument
    valid over every field (watch characteristic 2 and 3 separately where they matter) and the
    decision rule you extract is machine-checked as in 3c.
3b. **Rank 1**: `A = I + uvᵀ`, `1 + vᵀu ≠ 0`. Prove over every field that one of the types
    (4), (3,1), (2,2) works. Known partial facts you may use (they are proved): for an n-cycle
    arrangement, failure at μ = 1 ⟺ `Σu = 0 ∧ Σv = 0 ∧ e(σ) = 1` where `e(σ) = Σ_{t<k} u_{σ(t)}
    v_{σ(k)}` over the cyclic order; swapping two adjacent tokens changes e by the 2×2 determinant
    `u_b v_a − u_a v_b`. The hard sub-case is `v = ρu` (all tokens proportional) where e is
    constant; there a (3,1) split with the fixed point f having `u_f ≠ 0` fixes μ = 1 — and the
    remaining question is μ ≠ 1 (roots of x⁴−1, x³−1, x²−1 in F̄). Close it.
3c. MACHINE CHECK of whatever decision rule your proofs produce: over GF(q) for q ∈ {2,3,4,5,7},
    enumerate ALL invertible A with rank(A − I) ≤ 2 (for q ≤ 3 this is a subset of GL(4,q) you
    can filter exhaustively; for q ≥ 4 enumerate (U,W) up to the obvious GL₂ redundancy or state
    a window), apply your rule to name a permutation, and verify cyclicity with an INDEPENDENT
    oracle (minimal-polynomial degree or rank of the Krylov matrix — not the same code path as
    the rule). Report per cell: population, rule successes, rule failures (must be 0 if the proof
    is right), and how often each branch of the rule fired. Negative control: replace the rule by
    "always return P = I" and show it fails on every input.

## 4. Deliverables and grading (pre-registered on my side; you are graded on what you BUILT)
- `REPORT.md` with: §1 proof + check table; §2 verdict on the argument + check table;
  §3 the proofs (or the counterexample `(F, U, W)` with all 24 products shown non-cyclic by the
  oracle — that would refute a Kourovka problem, so re-verify it three ways before printing it);
  §3c tables. State every window explicitly. A cell you could not finish is UNRESOLVED, not 0.
- Every number in the report must come from a printed line of a log you include.
- If you find yourself writing "it is easy to see" in §3, replace it with the computation.
End with `DONE-K6N4`.
