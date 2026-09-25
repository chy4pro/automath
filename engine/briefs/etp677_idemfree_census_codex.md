# CODEX TICKET (engineering + finite classification) — census of IDEMPOTENT-FREE finite
# 677-magmas of small order, and fibre-size-3/4 extension existence over each of them.
# Repo: $HOME/workspace/claudecode/automath. English. Write under
# problems/etp677/ext/idemfree/ (copy, do not edit, problems/etp677/ext/ext_cnf.py).
# Local compute: pure Python; kissat (tools/kissat/build/kissat) runs ≤ 120 s each, at most
# 60 solver calls, one at a time; total ≤ 2 h.

## Why
Conjecture F3 ("no finite 677-magma has a congruence with all classes of size 3") reduces
(Prop 0, engine/out/codex/etp677_fibre3_report.md) to IDEMPOTENT-FREE quotient bases. Among
prime-field affine models only F_31 (5x−4y+c, c≠0) is idempotent-free, and it admits no
fibre-3 extension (DRAT-verified). We need the census beyond prime fields.

## Tasks
1. AFFINE MODELS OVER FIELDS F_q, q ∈ {4, 8, 9, 16, 25, 27, 32, 49, 64, 81, 121, 125, 169}:
   x<>y = αx + βy + c satisfies E677 iff (registry (Mods)/R6B Thm 3): αβ(1+β²) = 1,
   α + α²β² + β³ = 0, c(αβ² + β² + β + 1) = 0. Implement the fields (irreducible polynomial
   arithmetic; verify field axioms on a sample), enumerate all (α,β,c), CHECK E677 directly
   on the table for every solution (do not trust the equations alone), and list the
   idempotent-free ones (x<>x = x has no solution). Report counts per q.
2. AFFINE MODELS OVER NON-CYCLIC ABELIAN GROUPS of order ≤ 49 that are not fields, e.g.
   Z_3^2 with x<>y = Fx + Gy + c for endomorphisms F,G ∈ M_2(Z_3): enumerate (F,G,c),
   direct E677 check, idempotent-free list. (M9 = x + Gy is idempotent at 0 only; we want
   models with NO idempotent.)
3. NON-AFFINE: consult the eq677 database (problems/etp677/ext/db/ has orders 5,7,9,11,13;
   fetch more with `gh api repos/memoryleak47/eq677/contents/db/<n>` for n ≤ 49 if useful)
   and list any model with no idempotent; verify E677 on each table you use.
4. For EVERY idempotent-free base found (up to isomorphism — use invariants: order, cycle
   type of x ↦ x<>x, number of left units per element, …), build the fibre-3 no-defect
   extension CNF with the copied encoder and solve (120 s cap): record UNSAT (+ DRAT if
   < 60 s) / SAT (decode + verify with ext_decode_verify.py: this would REFUTE F3 — report
   verbatim) / TIMEOUT. Then the same for fibre size 4 (existence; 120 s cap).
5. Also record, for the F_31 base, fibre sizes 6, 7, 8 existence (120 s cap each).

## Deliverables
`problems/etp677/ext/idemfree/{fields.py, census.py, census.out, results.out, …}` and
`engine/out/codex/etp677_idemfree_census_report.md`: per-q counts, the idempotent-free list
with tables (or generators), the extension verdict table, ending with DONE-IDEMFREE.
Print populations with every count; a 0 must say what was enumerated.
