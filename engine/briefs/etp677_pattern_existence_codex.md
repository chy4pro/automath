# CODEX TICKET (sol tier, mathematics, MINIMUM 2 h) — from the seven-pair PATTERN to the
# general fibre-3 theorem: does every idempotent-free finite 677-magma contain it?
# Repo: $HOME/workspace/claudecode/automath. English. No internet. Pure Python only.
# Read first: problems/etp677/ext/fibre3/proof/proof.md (the human proof of the F31 seven-
# instance lemma and its SHAPE-ONLY generalization) and fibre3/notes.md.

## What is proved (R46 STEP 11–15)
Over any base B (finite E677 magma) containing an injective typed copy of the eight-vertex /
fourteen-operation / seven-instance pattern P* (the base pairs (3,12),(5,0),(7,30),(12,18),
(30,5),(30,12),(30,30) of F31 with their P1..P4 subscripts — see proof.md for the pattern's
abstract description: which base pairs coincide, which instances are {1,3}-collisions),
there is no pair-indexed extension with a 3-element fibre. Also: a congruence with all
classes of size 3 forces an idempotent-free quotient (Prop 0 / L6).

## The question
CONJECTURE F3 follows if every idempotent-free finite 677-magma B contains a typed copy of
P*. TASK: prove that, or find exactly what an idempotent-free base must contain.
 T1 Abstract P*: write the seven instances as constraints on base elements. In F31 the
    eight vertices are 0,3,5,7,12,18,20,30 and the coincidences come from base identities
    such as x_a<>a = a (left units), y\x, (y<>x)<>y, y<>x. Express every vertex as a base
    TERM in a few generators (e.g. start from one element a and its left unit u = x_a,
    and the elements a<>u, u<>a, a\u, u\a, …) so that P* becomes "for every a (or for
    some a), the following seven eq.(4) instances at the pairs (term_i(a), term_j(a))
    exist with the required coincidences and the required DISTINCTNESS of the 14 ops".
    Check on F31 that your term description reproduces exactly the seven pairs (script).
 T2 Which coincidences are automatic in ANY finite 677-magma (from E677/KEY: e.g. u\a = a
    when u<>a = a; (y<>x)<>y = x\(y\x) by KEY), which need "a is not idempotent", and which
    need more (e.g. some element being its own something)? For the ones needing more:
    can they be forced from idempotent-freeness (no x with x<>x = x)? Try: in an
    idempotent-free base the left-unit map a ↦ x_a has no fixed point; iterate it; the
    L_a-cycle through a has length ≥ 4 ((Cyc) toolkit: never 2 or 3; m = 1 iff idempotent).
 T3 If some coincidence cannot be forced, look for OTHER seven-instance (or k-instance)
    patterns that ARE forced in every idempotent-free base and still kill fibre 3 — you
    may generate candidate patterns from the F31 UNSAT core structure (other minimal
    cores: run kissat on the F31 m=3 no-defect CNF with different instance subsets,
    ≤ 120 s each, ≤ 30 calls) and test each candidate's shape-only proof by the
    existing checkers' method (a candidate pattern is "shape-only forbidden" if the
    CNF built from just those instances with abstract distinct ops is UNSAT).
 T4 Deliver either: THEOREM (F3) with a proof every step of which cites E677/KEY or a
    checked finite computation; or the precise statement "every idempotent-free finite
    677-magma containing X has no fibre-3 congruence" with X minimal, plus what is
    missing to show X is universal.

## Deliverables
`problems/etp677/ext/fibre3/pattern/{notes.md, scripts, outputs}` and
`engine/out/codex/etp677_pattern_existence_report.md` ending with DONE-PATTERN.
Labels PROVED / VERIFIED-ON-MODELS / CONJECTURED; do not stop before 2 h of work.
