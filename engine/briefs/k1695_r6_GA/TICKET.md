# TICKET K6-GA — group-algebra families of regular permutation groups: a structured hunt for hard cases at n = 6, 8

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_GA/` (create): `scan.c`,
logs, `REPORT.md` ending with `DONE-K6GA`. Exact GF(q) tables (self-checked), no floating point;
reuse audited primitives from `engine/harvest/k1695_r6_T/search.c` if convenient. Cap 30 min per cell
(print progress; a capped cell is reported as a prefix).

## The family
For a finite group G of order n acting regularly on itself (points = group elements, P_h = the
permutation matrix of left translation x ↦ h·x) and f : G → F, put A_f := Σ_{h∈G} f(h) P_h, i.e.
A_f[x][y] = f(x y⁻¹). These are the matrices commuting with the right-regular action; for G = Z_n they
are the circulants; for G = S_n itself (not regular) the analogue is aI + bJ. Known: at n = 4 (G = V₄,
Z₄) no member defeats S₄ over GF(q ≤ 13); a V₄ member over GF(7) defeats all transpositions and all
(3,1)'s but is rescued by double transpositions and 4-cycles. Facts to use: for σ ∈ G (right
translation), A_f P_σ ∈ F[G]; for abelian G and char F ∤ |G| its eigenvalues are χ(σ)·f̂(χ) over the
characters χ of G, so A_f P_σ is cyclic iff χ ↦ χ(σ)f̂(χ) is injective; A_f is invertible iff all
f̂(χ) ≠ 0. For σ ∉ G there is no such formula — that is where the hunt is.

## Cells (exhaustive over f unless capped; for each invertible A_f test ALL σ ∈ S_n, stop at the first
## cyclic product; record the number of good σ for the hardest members)
1. n = 6, G = Z₆ and G = S₃ (regular action of S₃ on itself), over GF(2), GF(3), GF(5), GF(7): |F|⁶
   members, 720 permutations each.
2. n = 8, G = (Z/2)³ (elementary abelian — the prime candidate for a hard family in odd
   characteristic, by analogy with the char-2 / n ≡ 2 mod 4 obstruction of the aI+bJ family), G = Z₈,
   G = Z₄×Z₂, G = D₄, G = Q₈, over GF(3) (6 561 members, 40 320 permutations each — use symmetry: f and
   f∘(automorphism of G) and f∘(translation) give conjugate/equivalent A's; and stop at the first
   cyclic σ), then GF(5) and GF(7) if within cap.
3. For every member with NO cyclic product: that is a counterexample to Kourovka 16.95 — re-verify
   with a second independent cyclicity oracle (minimal-polynomial degree AND rank of the Krylov matrix
   for a random cyclic-vector search) before printing it, and print it in full with the field.
4. For the hardest members (fewest good σ), print f, f̂ (for abelian G), the cycle-type histogram of
   the good σ, and whether any good σ lies in G.

## Controls
- Monomial members f = v·δ_h: the good σ are exactly those with hσ an n-cycle (for the regular action
  this is a known count) — assert.
- Circulant f = all ones (A = J): singular for n > 1 — assert excluded. f with f̂ having a repeated
  value: assert A_f itself is non-cyclic.
- Cross-check cyclicity by two oracles on 10⁴ random (f, σ) per cell.

## Report
Per cell: population, all-fail count (expected 0 — if not, the matrix), minimum good-σ count and
its members, histograms. End with `DONE-K6GA`.
