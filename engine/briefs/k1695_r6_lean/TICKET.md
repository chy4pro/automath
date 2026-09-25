# TICKET K6-LEAN — Lean 4 / Mathlib: the transposition lemma for Kourovka 16.95 (kernel-checked)

Self-contained. Work in the existing Lean project under `lean/` in this repository (find the lake
project that builds against Mathlib — look for `lakefile` and an existing `lake build` that succeeds;
do NOT create a new Mathlib checkout, do NOT modify existing files; add ONE new file
`lean/<project>/K1695/TranspositionLemma.lean` and register it if the lakefile needs it). Deliver:
the file, the exact `lake build` output (0 errors, 0 sorry), `#print axioms` of every theorem
(must be only `propext`, `Classical.choice`, `Quot.sound`), and `engine/harvest/k1695_r6_lean/REPORT.md`
ending with the literal line `DONE-K6LEAN`. Time budget: ~2 h of work; if a statement resists, keep
the ones that compile and mark the rest clearly as NOT PROVED (never leave a `sorry` in a theorem you
list as proved).

## Mathematics (all over an arbitrary field K; n arbitrary)
Notation: `P_τ` for the transposition τ = (a b) is the permutation matrix with `P_τ e_a = e_b`,
`P_τ e_b = e_a`, `P_τ e_j = e_j` otherwise. `d := e_a − e_b`. Facts to formalise:

**L1 (matrix identity).** `P_τ = 1 − d dᵀ` (as matrices: `(P_τ)_{ij} = δ_{ij} − d_i d_j`). Hence
`P_τ * P_τ = 1` and `P_τ⁻¹ = P_τ`.
**L2 (rank identity).** For every `A : Matrix (Fin n) (Fin n) K` and `μ : K`:
`rank (A * P_τ − μ • 1) = rank ((A − μ • 1) + μ • (d dᵀ))`.
(Proof: `A * P_τ − μ•1 = (A − μ • P_τ) * P_τ` and `P_τ` is invertible; then substitute L1.)
**L3 (rank-one update bounds).** For `E : Matrix (Fin n) (Fin n) K`, `x y : Fin n → K`:
`rank E − 1 ≤ rank (E + x yᵀ) ≤ rank E + 1` (as natural numbers, with the obvious truncation).
**L4 (T0 — a transposition is derogatory only at an eigenvalue of A).** If `rank (A − μ • 1) = n`
(i.e. `A − μ•1` is invertible) then `rank (A * P_τ − μ • 1) ≥ n − 1`.
**L5 (T3).** If `rank (A − μ • 1) ≤ n − 3` then `rank (A * P_τ − μ • 1) ≤ n − 2`.
**L6 (T2, the direction used downstream).** If `rank (A − μ•1) = n − 2`, `d ∉ range (A − μ•1)` (column
space, i.e. `d` is not in the image of the linear map `mulVecLin (A − μ•1)`) and `dᵀ ∉ row space`
(i.e. `d ∉ range (mulVecLin (A − μ•1)ᵀ)`), then `rank (A * P_τ − μ • 1) = n − 1`.
(This is the general fact: `rank (E + x yᵀ) = rank E + 1` when `x ∉ range E` and `y ∉ range Eᵀ`.)
**L7 (T4, rationality).** Let `F ⊆ K` be fields (K an F-algebra, e.g. `[Algebra F K]`), `A` a matrix
over F, `μ : K` with `μ ∉ F` and `m : F[X]` its minimal polynomial over F (`m = minpoly F μ`). If
`w : Fin n → F` and `(A.map (algebraMap F K) − μ • 1).mulVec z = w.map (algebraMap F K)` for some
`z : Fin n → K`, then `w ∈ range (mulVecLin (aeval A m))` over F.
(Proof sketch you may follow: write `z = Σ_{t<k} μ^t z_t` with `z_t` over F using the power basis of
`F[μ]`; compare coefficients; conclude `w = m(A) z_{k−1}`. If the power-basis bookkeeping is too
heavy in Mathlib, prove the SEPARABLE special case or the case `k = 2` (quadratic m) explicitly —
that is the case needed for n = 4 — and say so.)

## Priorities
L1, L2, L3, L4, L5, L6 first (these are pure rank bookkeeping and should all go through with
`Matrix.rank`, `LinearMap.rank`, `rank_add_le`-style lemmas; look up the exact Mathlib names — do not
guess them, use `exact?`/`apply?` and grep the Mathlib source). L7 last. For each theorem, state it
EXACTLY as above (over an arbitrary field `K` with `[Field K]`, `n : ℕ`, `a b : Fin n`, `a ≠ b`), and
include one `example` instantiating it at n = 4 to show the statement is not vacuous.

## Report
List each of L1–L7 with: Lean theorem name, PROVED / NOT PROVED, the axioms printed, and the
`lake build` log. No prose beyond that. End with `DONE-K6LEAN`.
