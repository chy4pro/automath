# CODEX TICKET (engineering + exact search) — smallest IDEMPOTENT-FREE finite 677-magma.
# Repo: $HOME/workspace/claudecode/automath. English. Extend (a COPY of)
# problems/etp677/simple/simple_cnf.py under problems/etp677/simple/noidem/ — do not edit the
# original. Tools: tools/kissat/build/kissat, tools/drat-trim/drat-trim, tools/breakid/.
# Local compute: kissat runs ≤ 600 s each, one at a time, total ≤ 90 min. No cloud action.

## Why
Congruences with all classes of size 2 or 3 force an idempotent-free quotient (R46 STEP 10 /
Prop 0), and the only idempotent-free finite 677-magmas we know are the F_31 (5x−4y+c,
c≠0) family (affine census over fields q ≤ 169 and over F_2², F_3²: none other; eq677 db
orders ≤ 13: none). The question "what is the smallest idempotent-free finite 677-magma?"
is open and is decidable order by order.

## Tasks
1. Add mode `noidem` to the copied encoder: the plain E677 CNF plus, for every x, the unit
   clause ¬X[x,x,x] (x*x ≠ x). Keep BreakID preprocessing (as in the original; it fixes
   nothing unproved).
2. Positive control: order 31 with the F_31 table (5x−4y+1, generate it in code) fixed by
   unit clauses → must be SAT by propagation (encoding accepts a known idempotent-free
   model); and a negative control: order 5 with the F_5 (2x−y) table fixed + noidem → UNSAT.
3. Run `noidem` at orders 5, 7, 9, 11, 13, 15, 16, 17, 19, 20, 21, 23, 25 with a 600 s cap
   each (stop the ladder when three consecutive orders time out). Expected: UNSAT at
   5, 7, 9, 11, 13 if the eq677 database is complete there (all its models have an
   idempotent) — a DRAT-verified UNSAT is then a THEOREM independent of the database.
   SAT at any order: decode, verify E677 with problems/etp677/simple/simple_check.py, confirm
   no idempotent, report the table verbatim (a new idempotent-free model — also check
   whether it is affine/translation-invariant and whether it satisfies E255).
4. Also run `noidem` at order 31 FREE (no table fixed), 600 s cap: SAT expected (F_31
   exists) — report whether the solver finds it and whether the decoded model is
   isomorphic to F_31 (invariants: x ↦ x*x cycle type, left-unit map, |Aut| if cheap).

## Deliverables
`problems/etp677/simple/noidem/{noidem_cnf.py, run.sh, calibration.out, in/*.cnf for the
timed-out orders}` and `engine/out/codex/etp677_noidem_report.md` with the verdict table
(order, vars/clauses, BreakID, verdict, time, certificate), ending with DONE-NOIDEM.
