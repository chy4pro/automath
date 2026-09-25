# TICKET V4REPRO — independent own-seed reproduction of the branch_anneal v4 frontier (ETP 677)

Self-contained. Do NOT modify existing files. New files only under `problems/etp677/v4_repro/`; report at
`engine/out/codex/etp677_v4_repro_report.md` ending with the literal line `DONE-V4REPRO`. Every number in
the report must come from a command you ran; keep all logs under `problems/etp677/v4_repro/logs/`.
Wall-clock budget: 100 minutes of compute total (use `timeout`; run up to 6 processes in parallel).

## Context
`problems/etp677/L07/branch_anneal_v4.c` (SHA-256 88009e88…) is a simulated-annealing instrument written by an
external engine. It claims (engine/harvest/etp677_L06_frontier_r45_pro.md, etp677_L07_freenu_r45_pro.md): with
ν = id and the built-in cyclic designs, the maximum number of "perfect rows" with δ ≡ 0 it ever reached is
q=3: 4, q=4: 6, q=5: 9, q=7: 14, and at q=3 the minimum (total_defect, failing_cells) toward (N) is (44, 40).
The banked objects are under `problems/etp677/` (L03_q3_four_perfect_delta0.json, L05/L05_q4_P6_delta0.json,
L05/L05_q5_P8_delta0.json, L06/L06_q7_P14_delta0_best.json, L06/L06_q3_N_total44_fail40.json). Checkers:
`engine/scripts/check_branch_object.py` (note: its final verdict folds delta==0 in) and
`problems/etp677/R45_grade_object.py` (bank grader — authoritative for JSON banking).

## Tasks
T0. Compile with `cc -O3 -std=c11 -Wall -Wextra -pedantic branch_anneal_v4.c -lm -o v4`; record `./v4 --help`
(or read the source) to learn the flags: --q, --seed, --iters, --target-P, --lock-rows, --dump-json, --nu, --asg,
--restart-every, --t-hi/--t-lo, --compound. Record the exact flag semantics you rely on.
T1 (own seeds, from scratch). Using seeds YOU choose (not the ones in the harvests), run from-scratch searches:
q=3 target |P|=4 δ=0; q=4 target |P|=6 δ=0; q=5 target |P|=8 then 9 δ=0. Report per run: seed, iterations,
wall time, best |P| at δ=0 reached, and whether the dump passes the bank grader. Success = reaching the same
frontier level from independent seeds (the objects need not coincide).
T2 (try to beat the frontier). With the remaining budget, run q=3 target |P|=5 δ=0 and q=4 target |P|=7 δ=0
(≥3 seeds each, ≥10^8 iterations each). Report the best states (|P|, δ-mass). Any object with q=3 |P|≥5 δ=0 or
q=4 |P|≥7 δ=0 that passes the bank grader is a NEW RECORD: dump it, print its SHA-256, and say so loudly.
T3 (q=3 toward (N)). ≥2 seeds free search minimising total_defect; report the best (total_defect, failing_cells)
you reach in the budget vs the claimed 44/40.
T4. Verdict paragraph: is the claimed frontier reproducible from independent seeds within this budget? Which
levels were reached, which were not (and say "not reached within budget", never "impossible").

## Report format
T0–T4 with tables; exact commands; SHA-256 of every dumped JSON; then `DONE-V4REPRO`.
