# CODEX TICKET (sol tier, ATP + finite model search) — are the commutation identities
# FIRST-ORDER consequences of E677 + E255 (+ left division), or do they need finiteness?
# Repo: $HOME/workspace/claudecode/automath. English. Tools (self-contained, already
# built): tools/ladr_build/LADR-2009-11A/bin/{prover9,mace4}, tools/E/PROVER/eprover.
# Local compute: each ATP run ≤ 300 s wall, ≤ 3 GB; mace4 runs ≤ 300 s each; total ≤ 90 min.
# Read first: engine/out/codex/etp677_commutation_report.md (its PROVED reductions and the
# exact conjectures) and engine/out/codex/etp677_X6_existence2_report.md.

## Language
Binary * and left division \ with axioms  x*(x\y) = y,  x\(x*y) = y  (left quasigroup);
E677: x = y*(x*((y*x)*y)); E255: ((x*x)*x)*x = x. Define by equations:
 U(x) = (x*x)*x, W(x) = x*U(x), P(x) = x\U(x), F(x) = x\P(x), H(x) = (x*x)*((x*x)*x).

## Goals (each a separate prover9 run with the standard settings + a 300 s cap; ALSO eprover)
 G1 F(U(x)) = U(F(x))          G2 F(W(x)) = W(F(x))          G3 F(P(x)) = P(F(x))
 G4 F(H(x)) = x                (KNOWN PROVED in Lean under FINITENESS — the point: does the
    first-order theory already prove it? If G4 is not first-order derivable while it is
    true in every finite model, that calibrates what "needs finiteness" means here.)
 G5 H(F(x)) = x                 G6 (positive control) U(x)*x = x from E255 (trivial);
 G7 (negative control) x*y = y*x (must NOT be provable; expect saturation/timeout).
 G8 Pair Conservation in a first-order form is not expressible (counting) — skip; instead
    the pointwise "collision-value lift" style statements from the S-attack reports if any
    is equational; otherwise skip and say so.
Report for each: PROVED (with the proof length / used axioms, and save the proof file) /
SATURATED (sos empty — a genuine "not first-order entailed by these axioms" result for
prover9's complete strategy; state the strategy) / TIMEOUT.

## Finite counter-model search (mace4; the ATP's complement)
For G1, G2, G3, G5: mace4 with domain sizes 2..9 (and 10, 11 if time allows), the axioms
above, the negation of the goal — a counter-model would be a finite left quasigroup
satisfying E677 + E255 with the identity failing (a REFUTATION of the commutation
conjecture; decode and verify it with pure Python: E677 on all pairs, E255, left
division consistent, the identity's failure point). Expected: none (the campaign's models
all satisfy the identities), but mace4 is exhaustive per order — report "no model at
orders ≤ N" with the exact N and the time per order.

## Deliverables
`problems/etp677/ext/fibre3/pattern/atp/{inputs/*.in, outputs/*.out, notes.md}` and
`engine/out/codex/etp677_atp_commutation_report.md` ending with DONE-ATPCOMM, with the
G1–G7 table (prover9 / eprover verdicts) and the mace4 table (order → verdict, time).
