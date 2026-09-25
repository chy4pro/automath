# TICKET K6-T — PROVE the controllable-column statement (T_m), or break it

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_T/` (create): `REPORT.md`
ending with the literal line `DONE-K6T`, plus every script and log. Exact arithmetic only. You are
graded on what you BUILD: a proof is a chain of lemmas each with a proof valid over every field and,
where it has finite instances, a machine check against brute force with a control that can fail.
A counterexample is worth more than a proof, if it is real: re-verify it two independent ways.

## The statement
F a field, m ≥ 1. For an m×m matrix M and a vector b ∈ F^m, the pair (M, b) is CONTROLLABLE if
b, Mb, …, M^{m−1}b are linearly independent (⟺ no left eigenvector y of M over an algebraic closure
has yᵀb = 0 ⟺ rank[M − λI | b] = m for every λ ∈ F̄). P_τ is the permutation matrix with
P_τ e_l = e_{τ(l)}, so C P_τ has columns c_{τ(1)}, …, c_{τ(m)}.

**(T_m)** For every m×(m+1) matrix R of rank m over F there exist a column index j and a bijection τ
from {1..m} to the other columns such that (R[:,≠j]P_τ, R[:,j]) is controllable.

Equivalent forms (all proved, use freely):
- (T_m) ⟺ ∃ a partial permutation matrix E (m×(m+1), one 1 per row in distinct columns, one zero
  column) with `R − λE` of full row rank for every λ ∈ F̄.
- (T_m) ⟺ ∃ column permutation Q of R with `RQ − λ[I_m | 0]` of full row rank ∀λ.
- (T_{n−1}) ⟺ (S′): for every A ∈ GL(n,F) and every index i there is a permutation σ with e_i a
  cyclic vector of A P_σ. And (S′) ⟹ Kourovka 16.95 ("some AP_σ is cyclic").
- Failure in left-eigenvector form: (T_m) fails for (R, j, τ) iff ∃ y ≠ 0 (over F̄), λ, with
  `Rᵀy = λ·(y spread by τ, with 0 at column j)` — i.e. the vector Rᵀy ∈ F̄^{m+1} has a zero at
  column j and its other entries are λ times the entries of y, matched by τ.

## What is known (do not re-derive; you may use)
- (T_m) holds for: m ≤ 4 over GF(2) (ALL matrices: verified through GL(5,2)), m = 3 over GF(3)
  (ALL, through GL(4,3)), m = 3 over GF(4) and m = 2 over GF(2,3,4,5) (all matrices up to column
  order). No counterexample anywhere; the minimum witness count grows (12 at m = 4/GF(2)).
- **Deflation identity.** If R_{ij} ≠ 0, use column j to eliminate row i by column operations
  (subtract (R_{il}/R_{ij})·column j from each column l ≠ j; this preserves `R − λE` when column j is
  E's zero column), then delete row i and column j: the (m−1)×m result R̃ satisfies
  `rank(R − λE) = 1 + rank(R̃ − λE′)` for all λ, where E′ is the partial permutation Ẽ with its zero
  column (at φ(i)) refilled by −b̂/b_i (b = column j, b̂ = b without entry i). So (T_m)(R) at pivot
  (i,j) ⟺ the (m−1)×m pencil R̃ − λE′ is full rank ∀λ, with E′ NOT a partial permutation unless
  b̂ = 0. Consequently: **if some column of R has a single nonzero entry (row i, column j) then
  (T_m)(R) ⟸ (T_{m−1})(R[≠i, ≠j])** (b̂ = 0). The hard core is matrices whose every column has ≥ 2
  nonzero entries.
- **The "for all weights" generalisation is FALSE**: (W_m)(R, v) "∃ ordering τ̂ of all m+1 columns with
  (R[:,τ̂(1..m)], Σ_{l≤m} v_l c_{τ̂(l)} + c_{τ̂(m+1)}) controllable" fails for some (R, v ≠ 0), e.g.
  R = [e₁, e₁, e₂, e₃] over GF(2) with v = e_l. So an induction must control the weight vector
  produced by deflation (it is the pivot column's other entries divided by the pivot).
- Feedback invariance: (M, b) controllable ⟺ (M + b gᵀ, b) controllable for every g. Hence, for a
  chosen b, the other columns of R may be modified by adding any multiples of b.
- If R = [C | Cβ] with C invertible then (T_m) with j = m+1 ⟺ ∃τ: β is a cyclic vector of P_τ C
  (similarity by C). For C = I, β = (1,…,1) this particular j FAILS (β is fixed by every P_τ) while
  other j succeed — so the choice of j is essential.
- A usable column j does not require R[:,≠j] invertible (measured).

## What to do
1. Try to PROVE (T_m) by induction on m. Candidate strategies (pursue at least two, report all):
   (a) choose the pivot column b to be one with the fewest nonzero entries and the pivot row inside
       its support, and control the weight vector −b̂/b_i in the deflated pencil; find the right
       strengthened statement (W′_m)(R, v) restricted to the weights that actually arise, prove it
       is inductive, and machine-check it (all R, all arising v) over GF(2), GF(3) for m ≤ 4;
   (b) the left-eigenvector covering: each failing (y, λ) covers a coset of a Young subgroup of the
       (m+1)! injections; show the cosets cannot cover everything — e.g. bound the number of
       (y,λ)-classes with repeated coordinates via the rank of R, or use a "generic y" argument;
   (c) a direct construction of τ: order the columns so that the Krylov sequence b, Mb, M²b, …
       is triangular with respect to some flag, using rank m to guarantee a new direction at each
       step (a Hessenberg-type argument — careful: it only works if some permutation of R is
       Hessenberg, which is false in general; find the correct replacement).
2. If a strategy stalls, formulate the exact residual statement and machine-check whether it is
   true over GF(2), GF(3), GF(4) for m ≤ 4; if it is FALSE, print the smallest counterexample — that
   is a result.
3. Independent of 1–2: search for a counterexample to (T_m) itself at m = 5 over GF(2) and m = 4 over
   GF(3) if you can do it in exact C within ~20 min (state windows); and at m = 3 over GF(7), GF(8),
   GF(9) exhaustively.
4. Report: lemmas with proofs; the machine-check lines; every residual statement stated exactly;
   every window stated. End with `DONE-K6T`.
