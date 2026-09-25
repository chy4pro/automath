# CODEX TICKET (sol, codex11 = GHPKG owner) — pre-freeze hygiene of problems/etp677/pub/github/. DONE marker: problems/etp677/pub/github/DONE-RENAME
# Report: engine/out/codex/etp677_github_rename_report.md. No push, no upload, no lake build, no solver runs. Do not touch pub/bundle/ (another screen owns it).
R1 Rename the internal-role-named checkers to *_independent.py and update EVERY reference:
     models/check_window217_dialogue.py -> models/check_window217_independent.py
     models/check_ucycle_dialogue.py    -> models/check_ucycle_independent.py
     sat/independent/check_fibre3_dialogue.py    -> sat/independent/check_fibre3_independent.py
     sat/independent/check_fibre4def_dialogue.py -> sat/independent/check_fibre4def_independent.py
   References to update: verify.sh, README.md, REPRODUCE.md, MANIFEST.json, SHA256SUMS (recompute the renamed rows), sat/small/certificates.json,
   any docstring/usage line inside the scripts themselves, and paper1 CLAIMS.md pointers if they name these files.
R2 Re-sync the package's paper copy from the revised sources: problems/etp677/pub/github/paper/ must equal problems/etp677/pub/paper1/
   (sections/*.tex, main.tex, refs.bib, CLAIMS.md, main.pdf, figures/) — the revised paper1 is already free of internal names; copy, do not edit.
R3 Acceptance: `grep -rn -i "dialogue\|codex\|luna\|chatgpt\|qwen\|registry R46\|engine/harvest\|$HOME\|gmail" problems/etp677/pub/github problems/etp677/pub/paper1 problems/etp677/pub/bundle --exclude-dir=.lake`
   must print NOTHING; paste the (empty) output in the report. Re-run `./verify.sh` quick mode (or the smallest mode) once to prove the renamed paths work.
R4 Keep the owner-edited lean/lakefile.toml and the existing .gitignore untouched.

# ADDENDUM (owner line, 08:2x): REPRODUCE.md (and README.md if it has a verify section) must state the cache variable explicitly —
#   ETP677_MATHLIB_CACHE=<path to an already-built Mathlib packages dir at the pinned rev> ./verify.sh
# — and WARN that a cold run without it downloads ≈7 GB of Mathlib and builds it (hours). Keep this in the DONE-RENAME acceptance.
