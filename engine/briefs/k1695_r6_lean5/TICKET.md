# TICKET K6-LEAN5 — Lean: "Krylov-cyclic vector ⟹ minpoly = charpoly" (closes the n = 3 caveat) and the general-n deflation

Continue in `lean/proofenv` (Mathlib; the K1695 modules must stay green). Add ONE new file
`K1695/CyclicToMinpoly.lean`. Deliver: file, `lake env lean` output with `#print axioms` for every
theorem (no axiom beyond [propext, Classical.choice, Quot.sound]), `lake build` green,
`engine/harvest/k1695_r6_lean5/REPORT.md` ending with `DONE-K6LEAN5`. No `sorry` in anything listed
as proved. Budget ~3 h; keep what compiles.

**C1 (the equivalence used by Kourovka's wording).** For a field K, n ≥ 1, M : Matrix (Fin n) (Fin n) K
and v : Fin n → K: if `LinearIndependent K (fun k : Fin n => (M ^ (k : ℕ)) *ᵥ v)` then
`minpoly K M = M.charpoly` (Mathlib: `Matrix.charpoly`, `minpoly`, `Matrix.minpoly_dvd_charpoly`,
`Matrix.aeval_self_charpoly` / Cayley–Hamilton, `minpoly.monic`, `Polynomial.eq_of_monic_of_dvd_of_natDegree_le`
or the degree argument). Proof: if p = minpoly has natDegree d < n then `aeval M p = 0` gives
`Σ_{k≤d} p_k (M^k *ᵥ v) = 0`, a nontrivial linear relation among the first d+1 ≤ n Krylov vectors
(the leading coefficient is 1), contradicting independence; so natDegree (minpoly) ≥ n; minpoly ∣
charpoly, both monic, natDegree charpoly = n (`Matrix.charpoly_natDegree_eq_dim`) ⟹ equal.
Also the converse is NOT required.
**C2 (apply to n = 3).** Using `K1695.kourovka_16_95_n3_cyclic_vector` (file CyclicVectorThree.lean;
its Krylov form is `![v, M*ᵥv, M*ᵥ(M*ᵥv)]` — bridge it to the `fun k : Fin 3 => (M^k) *ᵥ v` form),
state and prove
`theorem kourovka_16_95_n3 (A : Matrix (Fin 3) (Fin 3) K) (hA : IsUnit A.det) :
  ∃ σ : Equiv.Perm (Fin 3), minpoly K (A * σ.permMatrix K) = (A * σ.permMatrix K).charpoly`
— this is the notebook's statement for n = 3 verbatim (minimal polynomial = characteristic polynomial
of A·P), with P = σ.permMatrix K a permutation matrix.
**C3 (general-n deflation, the (S′) ⟸ (T_{n−1}) bridge).** For n ≥ 2, A : Matrix (Fin n) (Fin n) K,
i : Fin n, and a permutation σ: let R := A with row i deleted (`Matrix (…) (Fin n) K` over `{k // k ≠ i}`
or via `Fin.succAbove`), M′ := the (n−1)×(n−1) matrix `fun r s => (A * σ.permMatrix K) (i.succAbove r) (i.succAbove s)`
(rows and columns ≠ i of A·P_σ) and b′ := `fun r => (A * σ.permMatrix K) (i.succAbove r) i`. Prove:
if `LinearIndependent K (fun k : Fin (n−1) => (M′ ^ (k:ℕ)) *ᵥ b′)` then
`LinearIndependent K (fun k : Fin n => ((A * σ.permMatrix K) ^ (k:ℕ)) *ᵥ Pi.single i 1)`.
(The n = 3 instance is `ctrl3_e0_of_ctrl2_lowerBlock`; generalise its proof: the Krylov vectors of e_i,
projected off coordinate i, are b′, M′b′ + (scalar)·b′, … — a unitriangular change of the Krylov basis —
and e_i itself supplies the i-th coordinate.) If the index bookkeeping with `succAbove` is too heavy,
prove it for i = 0 with `Fin.succ` and derive the general i by conjugating with `Equiv.swap 0 i`
(as CyclicVectorThree.lean does).
Add `example`s at n = 4 for C1 and C3.

## Report
Theorem names, PROVED / NOT PROVED, axioms, build log. End with `DONE-K6LEAN5`.
