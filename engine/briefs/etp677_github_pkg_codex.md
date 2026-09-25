# CODEX TICKET (engineering + packaging; sol or luna) — PUBLIC GITHUB PACKAGE for Paper 1 (owner
# directive 2026-08-30: "GitHub 要有 … 要提供让其他人验证和证伪的全部条件"). Repo:
# $HOME/workspace/claudecode/automath. Inputs: problems/etp677/pub/PLAN_0830.md,
# problems/etp677/pub/paper1/ (draft, CLAIMS.md) and problems/etp677/pub/bundle/ (from the
# PAPER1 / CERTBUNDLE tickets — if not finished yet, build the package from the sources directly
# and let the paper/bundle tickets fill in), lean/etp677_ext, problems/etp677/simple/fibre_core,
# problems/etp677/diag, problems/etp677/ext (encoders only), engine/harvest/etp677_fibre4_m5witness_pro.md,
# problems/etp677/fibre_core_dialogue/ (independent encoders). Do NOT push: prepare the repo
# content under problems/etp677/pub/github/ and a push script; the dialogue pushes after G1–G3
# (gh auth as chy4pro). NO owner e-mail anywhere; git author "chy4pro". DONE marker: DONE-GHPKG.

## Target repository
New public repo `chy4pro/etp677-structure-theorem` (self-contained; the paper is also mirrored
into chy4pro/automath-papers by the dialogue). Licenses: code MIT, paper/text CC BY 4.0.

## Layout
README.md — the theorem in two sentences, what is verified by whom (Lean clean / Lean labelled /
DRAT), the falsification hooks, one-command verification, citation (Zenodo DOI placeholder).
REPRODUCE.md — exact commands, expected outputs, run times, hardware used; sections:
  1. Lean: toolchain (lean-toolchain), lake-manifest.json, `lake exe cache get` (Mathlib cache),
     `lake build`, `lake env lean scripts/PrintAxioms.lean` → expected AXIOMS_TABLE.md.
  2. SAT certificates: pinned kissat (version + commit + build), drat-trim (commit), CaDiCaL/
     Glucose via python-sat versions (the dialogue's encoder); generation scripts with exact
     arguments; per certificate: CNF sha256, proof sha256, size, solve time, check time.
  3. Big certificates (jdef_m4 1.95 GB, dlgdef_m4_def 5.7 GB, c8def_m4 2.1 GB, A5 cubes 0.67–2.39
     GB, MONO3 cubes): public download URLs (the gs:// objects must be made publicly readable
     or mirrored to a Zenodo dataset — write the exact gsutil commands for the dialogue) +
     sha256 + `verify_big.sh` that downloads, checks sha256, runs drat-trim (hours).
  4. Falsification hooks: (a) the m = 5 local witness + replay script — "extend this to a real
     magma with a class of size 5 over a base and you have a counterexample"; (b) the
     generators for any m (core_joint.py, fibre_core_dialogue encoder) — "find a SAT instance
     at m = 4 and the theorem is false"; (c) the A5 orbit cover script + cube generator.
lean/ — a copy of lean/etp677_ext (all modules, AXIOMS.txt, lean-toolchain, lakefile,
lake-manifest) building with one command.
sat/ — encoders (core7_free.py, core_joint.py, core_nh.py, diag_cnf.py + a5.py + check.py,
the dialogue's check_fibre3_dialogue.py / check_fibre4def_dialogue.py / replay scripts),
small CNF+DRAT pairs (< 50 MB each) with SHA256SUMS, drat-trim logs for all certificates.
witness/ — the m = 5 witness (verbatim) + replay_witness.py (standalone).
models/ — explicit models used in the paper (F31, T7, 4x+3y, M49ε, M217ε, R217, J1519 as
generators + a checker), the switching construction generator.
paper/ — main.tex + PDF (from the PAPER1 ticket) + CLAIMS.md (claim → certificate map).
MANIFEST.json + SHA256SUMS — every file with sha256; scripts/make_manifest.sh.
verify.sh — CI-style: within ~30 minutes on a laptop re-checks everything small: builds kissat
+ drat-trim from pinned sources (or uses provided binaries), regenerates + solves + drat-trims
the small certificates (core7 m=2/3, joint+defect m=3, Core-7+NH m=4 (minutes), A4 section,
c8 controls), replays the witness, recomputes the A5 orbit cover, checks all sha256s, runs
`lake build` if Lean is present (skips with WARN otherwise), and prints PASS/FAIL per claim
(C1–C9 of PLAN §G2 numbering). A GitHub Actions workflow file (.github/workflows/verify.yml)
running verify.sh on ubuntu-latest (Lean step optional via cache).
push.sh — creates the repo with gh (public), adds LICENSE files, commits with author chy4pro,
pushes; NOT executed by you.

## Rules
Everything a stranger needs, nothing internal: no registry, no engine/cost data, no owner
e-mail. Pin every version. Test verify.sh yourself end to end (report its wall time and the
PASS/FAIL table). Where an artifact is not yet produced (paper PDF), leave a clearly marked
placeholder and list it in the report.
## Deliverables
problems/etp677/pub/github/ (complete repo content), verify.sh run log, and
engine/out/codex/etp677_github_pkg_report.md ending with DONE-GHPKG.
