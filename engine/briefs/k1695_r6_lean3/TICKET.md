# TICKET K6-LEAN3 — Lean 4 / Mathlib: (T_2) over every field, and Kourovka 16.95 for n = 3 as a corollary

Continue in the project `lean/proofenv` (Mathlib present; existing file `K1695/TranspositionLemma.lean`
must stay green). Add ONE new file `K1695/CyclicVectorThree.lean`. Deliver: the file, the
`lake env lean K1695/CyclicVectorThree.lean` output with `#print axioms` for every theorem (must be
exactly [propext, Classical.choice, Quot.sound]), `lake build` green, and
`engine/harvest/k1695_r6_lean3/REPORT.md` ending with the literal line `DONE-K6LEAN3`. No `sorry` in
anything listed as proved. Time budget ~3 h; keep what compiles, mark the rest NOT PROVED.

## Mathematics (K any field)
Controllability: for M : Matrix (Fin m) (Fin m) K and b : Fin m → K, `Ctrl M b :=
LinearIndependent K ![b, M *ᵥ b, …, M^(m−1) *ᵥ b]` (for m = 2: `![b, M *ᵥ b]`; for m = 3:
`![b, M *ᵥ b, M *ᵥ (M *ᵥ b)]`).
**(T_2).** For every 2×3 matrix R over K of rank 2 (i.e. its three columns c₀,c₁,c₂ span K²) there
exist j and an ordering (k, l) of the other two indices such that `Ctrl (Matrix.of ![c_k, c_l]ᵀ…)` —
concretely: `Ctrl M b` with `b = c_j` and M the 2×2 matrix with columns c_k, c_l (in that order).
Proof to formalise (all fields, no division): with b = (x, y)ᵀ,
`det[b, [c_k c_l] b] = x·det(b, c_k) + y·det(b, c_l)` (∗). Suppose all six choices fail. Pick two
independent columns u, v (exist by rank 2), write the third w = αu + βv. From b = u with both
orders: x_u + β y_u = 0 and β x_u + y_u = 0 (using det(u,u) = 0, det(u,w) = β det(u,v)); since u ≠ 0
this forces β² = 1, y_u ≠ 0, x_u = −β y_u. Symmetrically from b = v: α² = 1, y_v ≠ 0, x_v = −α y_v.
Then D := det(u,v) = (α − β) y_u y_v; α, β ∈ {1, −1} and D ≠ 0 forces α = −β and char K ≠ 2
(else α − β = 0). From b = w with both orders one gets x_w + y_w = 0 (after cancelling a nonzero
sign), which reads 2y_u = 0 (if α = 1) or 2y_v = 0 (if α = −1) — impossible as char ≠ 2 and the
y's are nonzero. Contradiction. (This is the K6-T proof; re-derive it as you formalise; if a step is
wrong, fix it and say so.) It is fine to first prove the determinant form: `Ctrl M b ↔ det ![b, M*ᵥb] ≠ 0`
for m = 2 (Mathlib: linear independence of two vectors in K² ↔ det ≠ 0).
**Corollary (16.95 at n = 3, cyclic-vector form).** For every A ∈ GL(3,K) and every i : Fin 3 there is
a permutation σ of Fin 3 such that e_i is a cyclic vector of `A * P_σ`, i.e.
`LinearIndependent K ![e_i, (A*P_σ) *ᵥ e_i, (A*P_σ) *ᵥ ((A*P_σ) *ᵥ e_i)]`.
Proof: let R := A with row i deleted (2×3, rank 2 since A is invertible). (T_2) gives j and (k,l).
Define σ by σ(i) = j and the other two indices mapped to k, l in order (so that `A*P_σ` has column
i equal to A's column j, etc.). Then the Krylov vectors of e_i under M := A*P_σ are e_i, Me_i,
M²e_i; project away coordinate i: the projections of Me_i and M²e_i are b and M'b where
M' = R[:, k,l] (2×2) and b = R[:,j]; feedback/deflation: since row i of M is irrelevant to the
Krylov independence modulo e_i … — formalise the cleanest version you can: e.g. prove directly that
if `![b, M' *ᵥ b]` is independent in K² then `![e_i, M e_i, M² e_i]` is independent in K³ by looking
at the 2×3 block of coordinates ≠ i of the last two vectors plus the e_i-coordinate of the first.
(Hint: `(M *ᵥ e_i)` restricted to coordinates ≠ i is b; `(M *ᵥ (M *ᵥ e_i))` restricted is
M' b + (M e_i)_i · b — the extra multiple of b does not affect independence with b.)
Finally state `theorem kourovka_16_95_n3_cyclic_vector (A : Matrix (Fin 3) (Fin 3) K) (hA : IsUnit A.det) :
∃ σ : Equiv.Perm (Fin 3), ∃ v : Fin 3 → K, LinearIndependent K ![v, (A * σ.permMatrix K) *ᵥ v, …]`
— and, if Mathlib has the notion, also derive `minpoly = charpoly` (or `IsCyclic`-style) from the
cyclic vector; if not, say so and leave the cyclic-vector form (it is the classical equivalent and
is honest).

## Report
Theorems with names, PROVED/NOT PROVED, axioms, build log. End with `DONE-K6LEAN3`.
