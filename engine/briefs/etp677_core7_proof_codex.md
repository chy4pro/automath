# CODEX TICKET (sol tier, mathematics, MINIMUM 2 h) — a HUMAN-READABLE proof of the
# seven-pair F31 lemma, and its generalization if one appears.
# Repo: $HOME/workspace/claudecode/automath. English. No internet. Pure Python only
# (≤ 10 min CPU total). Read first: problems/etp677/ext/fibre3/notes.md and the core files
# fibre3/f31_min_core.cnf(.map), fibre3/analyze_core.py, fibre3/verify_partial_models.py.

## The lemma (DRAT-certified, R46 STEP 11)
Base B = F_31 with x<>y = 5x − 4y + 1 (no idempotents; translations x ↦ x+d are
automorphisms). Fibre M = {0,1,2}. Fourteen fibre operations <>_p (p among the pairs listed
below), each with permutation rows (rows ∈ S_3), CANNOT satisfy the seven instances of
eq.(4)   s = t <>_{P1} ( s <>_{P2} ( (t <>_{P3} s) <>_{P4} t ) )   at the base pairs
  (3,12): P = (12,30),(3,12),(12,3),(18,12)
  (5,0):  P = (0,30),(5,30),(0,5),(12,0)
  (7,30): P = (30,5),(7,0),(30,7),(30,30)
  (12,18):P = (18,12),(12,20),(18,12),(12,18)    [P1 = P3: a {1,3}-collision instance]
  (30,5): P = (5,30),(30,7),(5,30),(30,5)        [P1 = P3]
  (30,12):P = (12,0),(30,30),(12,30),(3,12)
  (30,30):P = (30,7),(30,5),(30,30),(0,30)
(the seven are inclusion-minimal: deleting any one makes the system satisfiable).

## Task
Produce a proof a human can follow: each row is one of the 6 permutations of {0,1,2};
use the {1,3}-collision instances first (they involve only 3 distinct ops each and are the
most constrained), derive what they force (fixed points, parity, the unique-witness formula
of R7-C: t(σ) = (L^G_σ)^{-1}((L^F_σ)^{-1}(σ)) etc.), then propagate through the remaining
five instances to a contradiction. Case splits are fine if each case is short; a proof that
is a disguised exhaustive enumeration is NOT acceptable (that is what the DRAT already is).
Check every intermediate claim with a small Python script against the actual constraint
system (the .map gives variable numbering) — e.g. enumerate the solutions of the two
collision instances alone (small: 3 ops × 6³ rows) and print the surviving row-sextuples.
THEN: does the proof use anything specific to F31 beyond the SHAPE of the seven instances
(which base pairs coincide)? If not, state the general theorem it proves (e.g. "no
fibre-3 extension over any base whose instance graph contains this 7-instance pattern",
or "over any idempotent-free translation-invariant base").

## Deliverables
`problems/etp677/ext/fibre3/proof/{proof.md, check_*.py, outputs}` and
`engine/out/codex/etp677_core7_proof_report.md` ending with DONE-CORE7PROOF: the proof,
the checks, and the generalization statement (labelled PROVED / CONJECTURED).
