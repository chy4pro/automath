# CODEX TICKET (engineering; any tier; heavy <= 1 kissat run at a time, <= 600 s each, no CP-SAT) — package the
# dialogue's OUTSIDE-FAMILY fibre checkers for public release. Repo: $HOME/workspace/claudecode/automath.
# DONE marker: DONE-DLGPKG. Report: engine/out/codex/dialogue_fibre_checkers_pkg_report.md.

## What these files are
problems/etp677/fibre_core_dialogue/check_fibre3_dialogue.py   — independent encoding of the fibre-3 exclusion
  (Core-7 pattern, 14 pairs, 7 instances; m=2,3 UNSAT with DRAT; m=4 SAT; m=5 direct-product positive control).
problems/etp677/fibre_core_dialogue/check_fibre4def_dialogue.py — independent encoding of the fibre-4 exclusion
  with the E255 defect (21 pairs, 10 instances; controls: m=3+defect UNSAT, m=4 no-defect SAT, m=5 product+defect
  UNSAT, m=4 defect-only SAT, m=5 product no-defect SAT; main m=4+defect UNSAT — local kissat/CaDiCaL verdicts,
  cloud drat-trim VERIFIED on the identical CNF sha256 8d04dd3ddc2d87857a1a6b93da05798d5d279f6631ccb865966de3617ae3827d,
  proof 5,723,472,267 bytes, gs://[gcp-project]/ext13/out/ (dlgdef_m4_def.drat.gz, .dt.log)).
problems/etp677/fibre_core_dialogue/replay_m5_witness.py       — replays the Pro m=5 SAT witness
  (engine/harvest/etp677_fibre4_m5witness_pro.md) against the dialogue's own tables: 250/250 chains, defect at s in {0,1,3,4}.
Logs: run_m2_m3.log, run_m4.log, run_def_controls.log, run_def_cadical_m4.log, replay_m5_witness.log; CNFs dlg*.cnf, dlgdef_*.cnf.

## Deliverables (create under problems/etp677/fibre_core_dialogue/release/, nothing outside it except the report)
1. README.md: what each checker proves, the exact theorem statements it supports (fibre 2/3/4 exclusion, sharpness at
   m=5), how it is INDEPENDENT of line-677's encoders (own PROD/INST tables written from the algebra), and the
   falsification hooks: (a) find a valid m=4 assignment for the defect system (the script prints one if SAT),
   (b) extend the m=5 witness to a full E677 extension, (c) exhibit a smaller instance set.
2. REPRODUCE.md: exact commands with pinned versions (python3 + python-sat from the project .venv — record versions;
   kissat + drat-trim from ./tools with their git commits/version strings), expected outputs verbatim from the logs,
   run times, and the memory warning (m=4+defect DRAT ~5.7 GB; drat-trim needs ~15 GB RAM — recommend verdict-only
   locally and point to the cloud-verified proof + sha256).
3. verify.sh: re-runs check_fibre3_dialogue.py 2 3 (with DRAT + drat-trim), the five controls of
   check_fibre4def_dialogue.py, and replay_m5_witness.py; prints PASS/FAIL per claim; must finish < 10 min; must NOT
   run the m=4+defect main solve by default (flag --full to enable, verdict-only).
4. MANIFEST.sha256 of every file in the release dir plus the CNFs, logs and the witness file it references.
5. requirements/pins: a small pins.txt (python version, python-sat version, kissat version string, drat-trim commit).
Constraints: do not modify the three checker scripts (byte-identical; if a fix is truly needed, add a wrapper and say so);
no CP-SAT; keep memory small; delete any DRAT you generate after drat-trim verification (keep logs + sha256).
End the report with the verify.sh output and DONE-DLGPKG.
