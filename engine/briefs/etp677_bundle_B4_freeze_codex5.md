# CODEX TICKET (sol, codex5 = owner of problems/etp677/pub/bundle/) — FOLLOW-UP after your CERTBUNDLE ticket (do it right after
# DONE-CERTBUNDLE; nobody else edits pub/bundle/). Source: G1 audit blocker B4 + FREEZE, see engine/briefs/etp677_paper1_fixes_G1_codex.md
# (read it; the PAPER changes B2/B3/M1/M2/N1 belong to another screen and are NOT yours — do not edit paper1/*.tex or CLAIMS.md).
B4-1 Add the regenerated small cells to the bundle: problems/etp677/pub/small_certs/ (core7nh_m4 DRAT regenerated locally by the owner
     line with a 600-s cap; the a4 cell is already there) — copy in, drat-trim each (record the VERIFIED line), per-cell SHA256SUMS.
B4-2 Add problems/etp677/pub/checkers/ outputs ({dropone_core7,parity_halves}.out + their SHA256SUMS) once they exist (poll; they are
     being produced in the background by the owner line — do NOT re-run them).
B4-3 certificates.json: one entry per cell/proof with sha256, bytes, verifier, verdict, and the public path; the eight big proofs
     take their rows verbatim from problems/etp677/pub/big_proof_hashes.txt.
B4-4 finalize_manifest.py must FAIL (non-zero) on any missing file, any cell not VERIFIED, or any sha mismatch; add a self-test.
B4-5 ONE isolated lake build of the public Lean package + a fresh axiom table (#print axioms) written next to it. Start the build
     only when `pgrep -fl "lake build" | grep -v pgrep | wc -l` is <= 1; never a second build of your own.
FREEZE (only after the paper screen reports DONE-PAPER1FIX-PAPER, poll for problems/etp677/pub/paper1/DONE-PAPER1FIX-PAPER):
     inventory of paper (PDF + sources) + bundle + github package with sha256 for every file -> problems/etp677/pub/FREEZE_INVENTORY.sha256
     and FREEZE.md (date, git-independent), then the DONE-PAPER1 marker in problems/etp677/pub/. Report: engine/out/codex/etp677_bundle_B4_freeze_report.md
Rules: any kissat/cadical/drat-trim run under `timeout 600` and `ulimit -v 8000000`; no push/upload; no owner e-mail or engine names.

# ADDENDUM (owner line, 07:5x) — B4-1 source of the core7nh_m4 proof: do NOT re-solve locally (the capped local run failed under load).
#  The owner line launched a cloud runner; the verified DRAT lands in gs://[gcp-project]/ext16/out/ within the hour:
#  core7nh_m4.drat.gz (+ dt.log with the sha256 line, proof.gz). Poll `gsutil ls gs://[gcp-project]/ext16/out/` every
#  2 min while doing B4-2..B4-5; when present: `gsutil cp` into problems/etp677/pub/small_certs/, verify sha256 against the .log line,
#  optionally re-run drat-trim under `timeout 600` / `ulimit -v 8000000`, record VERIFIED, then continue.
#  small_certs/ already holds core7nh_m4.cnf, a4_e677.cnf + a4_e677.drat (s VERIFIED) and SHA256SUMS; checkers/ outputs are complete
#  (dropone: all seven drops SAT; parity: 23,328 / 1,944 / 0 violations; PARITY_CONTRADICTION).

# ADDENDUM 3 (owner line, 08:1x) — GitHub package hygiene, part of B4/FREEZE:
#  (1) pub/github/lean/lakefile.toml was hand-edited by the owner line to use the …/mathlib4 URL exactly as lake-manifest.json (same rev).
#      Do not revert; include the file as-is in the inventory.
#  (2) problems/etp677/pub/github/lean/.lake (~1.6 GB build artifacts + Mathlib) must NOT be pushed: add problems/etp677/pub/github/.gitignore
#      containing `lean/.lake/` and `**/.lake/` (plus the usual *.olean/*.ilean, build/), confirm `git status` in pub/github shows no .lake
#      entries (if the package is not yet a git repo, `git init` + `git add -A` dry-run `git status --short | grep .lake` must print nothing),
#      and EXCLUDE every .lake/ path from FREEZE_INVENTORY.sha256. Record the .gitignore sha256 and the `git status` check in the report.

# CORRECTION to ADDENDUM 3 (08:1x): pub/github/.gitignore already exists (excludes .lake/, lean/.lake/, tools builds, verify-work, paper aux) — do not rewrite; only confirm git status shows no .lake entries and exclude .lake/ from the inventory.

# ADDENDUM 6 (owner line, 09:0x) — core7nh_m4 hashes: the ext16 runner emitted no raw/gzip sha256. A hash VM writes them to
#  gs://[gcp-project]/hashes/hashes_ext16.txt (separate file; the eight-row hashes.txt is untouched) within ~5 min.
#  Before the FREEZE inventory: poll that file (every 60 s, up to 20 min); fill the two null sha256 fields of core7nh_m4 in
#  certificates.json / proof-pointer.json from it verbatim, and append its row verbatim to problems/etp677/pub/big_proof_hashes.txt
#  (do not touch the eight existing rows); the dt.log sha you recorded stays. If the file has not appeared after 20 min, leave the
#  nulls, say so in the report, and do not freeze until the owner line decides.

# ADDENDUM 7 (owner line STEP 74, 09:2x) — MAJOR before FREEZE (bundle/):
#  bundle/scripts/check_m5_witness.py line 39 defaults to an internal path five levels above the bundle (engine/harvest/… — forbidden string
#  and unrunnable for a verifier). Fix: (1) copy problems/etp677/pub/github/witness/m5_witness.md -> problems/etp677/pub/bundle/witness/m5_witness.md
#  (same bytes, cmp); (2) default = Path(__file__).resolve().parents[1] / "witness" / "m5_witness.md"; (3) bundle/README.md line 22
#  "the harvested witness" -> "the witness file witness/m5_witness.md"; (4) re-run the checker from the bundle as shipped, regenerate
#  SHA256SUMS / MANIFEST. Whitelist for the freeze grep: github/scripts/check_manifest.py:29 (the leak checker's own pattern list) — the
#  only permitted match. Then FREEZE.
