# CODEX TICKET (engineering; any tier incl. luna) — rebuild BreakID with a WORKING symmetry
# backend and re-break our CNFs. Repo: $HOME/workspace/claudecode/automath.
# Heavy processes ≤ 2. DONE marker: DONE-BREAKID.

## Defect (verified 2026-08-29)
tools/breakid/build/breakid (BreakID 37a72c5…) prints "Bliss graph group order 1 / Num
generators: 0 / total symmetry breaking clauses added: 0" on EVERY input, including the toy
`p cnf 4 2 / 1 2 0 / 3 4 0` whose swap symmetry (1↔3, 2↔4) is obvious. Output = input. So the
18 "BreakID'd" cells in problems/etp677/ext/in_bk/ are NOT symmetry-broken.

## Tasks
1. Diagnose: inspect tools/breakid (CMakeLists.txt, build_local.sh, flake.nix) — is bliss
   linked/vendored, was it built without the graph backend, is there a run-time flag? Fix the
   build (vendor bliss 0.73 or the version BreakID expects; self-contained under tools/, no
   system installs). Verify on the toy CNF (must report group order 2 and add breaking
   clauses) and on a 5×5 Latin-square CNF you generate (must find the row/column/symbol
   symmetries).
2. Re-break: problems/etp677/ext/in/*.cnf → ext/in_bk2/ (log generators, clause counts, time);
   problems/etp677/simple/window/in_gen/w14_idemfree.cnf (expect S_{n−7} on the free elements)
   and simple/mono/in/mono_n12.cnf; the (N)@q=3 instance under problems/etp677/cloud_r45/item3/
   (STEP-noted: 0 symmetries found earlier — recheck with the fixed tool; report whether the
   sequential-counter encoding really kills the symmetry).
3. Sanity: for two small cells with known verdicts (e.g. ext F31 m=2 UNSAT with DRAT in
   ext/out/drat/, and simple/mono n=8 UNSAT), run kissat on original vs broken CNF (≤ 600 s
   each), report times and that verdicts agree; for a known-SAT control (window n=7 plain or
   ext known-SAT control) confirm SAT is preserved and the decoded model still verifies with
   the cell's own decoder.

## Deliverables
Fixed tools/breakid build (+ a README note on how it was fixed), in_bk2/ files, logs, and
engine/out/codex/etp677_breakid_report.md ending with DONE-BREAKID.
