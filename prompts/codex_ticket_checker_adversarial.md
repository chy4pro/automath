# TICKET CHECKADV — adversarial cross-check of the three ETP-677 branch-object checkers

Self-contained. Do NOT modify any existing file. Put all new scripts under
`problems/etp677/checker_adv/` and the report at
`engine/out/codex/etp677_checker_adversarial_report.md`, ending with the literal line `DONE-CHECKADV`.
Time budget ~90 min. Never fabricate a number: every figure in the report must come from a command
you ran and whose output you captured under `problems/etp677/checker_adv/logs/`.

## Objects of study (three independent implementations of the same definitions)
1. `engine/scripts/check_branch_object.py` (dialogue's checker, any q)
2. `problems/etp677/R45_verify_any.py` and `problems/etp677/R45_grade_object.py` (line-677's bank checker/grader)
3. `lean/etp677_certs/ETP677Certs/Core.lean` (kernel-checked definitions of (B1)-(B4), `ldiv`, `Xi`, `E`, `N`,
   `delta`, perfect rows; build with `cd lean/etp677_certs && ~/.elan/bin/lake build`)
Prose definitions: `engine/briefs/etp677_L06_frontier_r45.md` and `engine/briefs/etp677_L02*.md` (read the
definitions section; the JSON format is whatever the banked files below use).

## Banked JSON objects (all under `problems/etp677/`)
delta==0 records: `R45_L02_q3_3perf_delta0.json`, `L03_q3_four_perfect_delta0.json`,
`L03_q4_three_perfect_delta0.json`, `L04/L04_q4_P4_delta0.json`, `L04/L04_q4_P5_delta0.json`,
`L05/L05_q4_P6_delta0.json`, `L05/L05_q5_P8_delta0.json`, `L06/L06_q7_P14_delta0_best.json`.
non-zero-delta controls: `L04/L04_q3_P5_mass18_diagnostic.json`, `L04/L04_q4_P6_mass2_diagnostic.json`,
`L06/L06_q3_N_total44_fail40.json`, `R44_q3_3perf_deltanz.json`.

## Tasks
T1 (agreement on the bank). Run checkers 1 and 2 on every object above; tabulate per object: (B1)-(B4) verdict,
perfect-row set, delta vector (or its mass), and any other metric both print (total_defect / failing_cells).
Any disagreement is a FINDING. For the four objects that have Lean modules (R45_L02, L03 q3, L05 q4 P6,
L06 q7 P14), also confirm the Lean theorem's claimed perfect-row set equals what 1 and 2 print.
T2 (perturbation fuzz). For every object generate >= 300 perturbations with a seeded RNG: single-cell swap
inside a row, two-cell swap across rows, whole-row permutation, changing one entry of `nu`, relabelling one
line, off-by-one shift of one column, and identity (control). Run checkers 1 and 2 on each; record for each
perturbation whether each checker (i) accepts as a branch object, (ii) reports the same perfect-row set,
(iii) reports the same delta. Any case where 1 and 2 differ is a FINDING; list it with the perturbation seed
and a reproducer command.
T3 (semantic diff by reading). Read the three implementations side by side and list every place where the
semantics could diverge: index conventions (0/1-based), how `nu` is applied (nu(c) vs nu^{-1}), which cells
are "fixed"/special, what exactly "perfect row" and "delta" mean, JSON field names and defaults, handling of
q not in {2,3,4,5,7}. For each, say whether T1/T2 exercised it and what happened.
T4 (verdict). One paragraph: are the three checkers provably (by the evidence above) computing the same
predicate on the banked objects? Which checker should be considered authoritative and why?

## Report format
Sections T1-T4 with tables; FINDINGS list (possibly empty, say so explicitly); commands run; then `DONE-CHECKADV`.
