# R5-A Brief: E255-violating extension over the exceptional F₃₁ base

GOAL (ultimate statement): construct a FINITE 677 magma violating E255, i.e. refute
proposition (P) "every element has a left unit" — this settles the last open finite
implication of the Equational Theories Project. Dual goal: if searches keep coming
back UNSAT, extract the forcing argument as a lemma toward proving (P) for extensions.

## Framework (blueprint ch. 13, verified in r5a_search.py selftest)

Base G: translation-invariant 677 model x⋄y = Ax+By+c on F_p, A+B=1.
Fiber M = Z_m, ops T[δ] for δ ∈ F_p (translation-invariant assignment ⋄_{x,y}=T[y−x]).
Big magma on G×M: (x,s)⋄(y,t) = (x⋄y, T[y−x][s][t]). 677 holds iff for every d ∈ F_p
and all s,t ∈ M:

    s = T[D1][t][ T[D2][s][ T[D4][ T[D3][t][s] ][t] ] ]        (eq 4, reduced)

    D1 = −(d+c)/B,  D2 = (A²+B)d+(A+1)c,  D3 = −d,  D4 = Bd−c   (mod p)

Every row T[δ][u][·] must be a permutation (left-invertibility). Columns free.
VERIFIED: with (A,B,c)=(3,−2,0), QR-class assignment and the F₁₆ ops ⋄⁰/⋄⁺/⋄⁻ this
reproduces the blueprint's 496 example exactly (0 violations, selftest PASS).

## Why the exceptional base (A,B,c)=(5,−4,1) on F₃₁ is forced

- E255 at (a,σ₀) ⟺ ∃τ: T[δ*][τ][σ₀] = σ₀, where δ* = a − b, b = unique base left
  unit of a. For idempotent bases (ALL other TI models: Type 1, and Φ₁₀-branch
  quandles) δ* = 0, and the d=0 instance forces T[0] itself to be an m-element 677
  magma while the violation clause demands T[0] violate 255 — CIRCULAR (need a small
  counterexample to build a big one). The exceptional models 5x−4y+c (c≠0) are the
  ONLY TI models with no idempotents: δ* = c/5 ≠ 0 escapes the circularity.
- wlog c=1 (scaling x↦λx maps c↦c/λ, permutes δ-classes; assignment is searched
  anyway). Then δ* = 1/5 = 25. Violation (wlog σ₀=0 by relabeling M):
  ∀τ: T[25][τ][0] ≠ 0.

## Lemma 13.4 barrier and its exact non-affine escape

Lemma 13.4: if ALL fiber ops are affine (α_{x,y}s + β_{x,y}t + c_{x,y}) over a base
satisfying 677+255, big magma satisfies 255. Our base satisfies 255 (linear ⟹ 255,
Lemma 13.3), so PURE AFFINE FIBERS ARE BLOCKED — record as (B4).
The proof's engine: non-injective α ⟹ two left-translations agree on an ENTIRE
fiber (uniform row collision in T[25]), then 677-alt + row-bijectivity of T[6]
(δ = −25 = 6 appears as ⋄_{y,x} slot) gives contradiction. This argument extends to
any op family: UNIFORM collision (two identical rows in T[25]) is impossible.
But violating 255 only needs a POINTWISE collision: column 0 of T[25] misses value 0
(hence collides somewhere) while rows stay pairwise distinct. Affine ops force
pointwise ⟹ uniform; general tables do not. m=2 provably impossible; m≥3 open —
this gap is exactly where a counterexample must live.

## Instance structure (c=1): d ↦ (D1,D2,D3,D4) = (8(d+1), 21d+6, −d, −4d−1)

Op 25 appears at: d=6 (D1 and D3): s = T25[t][ T8[s][ T6[T25[t][s]][t] ] ];
d=26 (D2 slot), d=9 (D4 slot). Functional view: each instance determines
T[D1] = Ψ(T[D2],T[D3],T[D4]) (needs s↦w3(s,t) injective); d↦D1 is a bijection, so
the system is 31 interlocking functional equations.

## Search status (kissat, r5a_search.py: gen/verify subcommands)

- m=3: UNSAT (0.14s). m=4: running. Escalation ladder: m=5..8; then DROP
  translation-invariance of the ASSIGNMENT (ops indexed by pairs (x,y) ∈ F₃₁²,
  961 ops; eq-4 instances per (x,y); same violation at the left-unit pair of a
  single fixed a, others free) — TI is a real restriction, non-TI is the full
  blueprint framework. Then base F₃₁×F₁₆ (496-order affine no-idempotent) if needed.
- Every SAT model must be verified by rebuilding the full 31m-order magma and
  checking E677 exhaustively + E255 failure list (verify subcommand does this).

## Task split

- codex (R5-A-impl, after R3-F): independent re-derivation check of the D-formulas;
  port search to C or improve SAT encoding (symmetry breaking: row 0 of T[0]
  lex-min under simultaneous M-relabeling fixing 0); run non-TI encoding for m=3,4.
- opus (R5-B): UNSAT-side theory — from m=3/4 UNSAT patterns, try to prove:
  "TI extension over the exceptional base always satisfies 255" (candidate lemma:
  chase instances d=6,26,9 to force a fixed point in column σ₀ of T[25]).
- GPT-5.6 Pro (web long-run): (P) both directions with this brief's algebra as
  ammunition; ask for structural obstructions or slicker constructions
  (e.g. non-abelian fiber symmetry, quasigroup-cocycle language).
