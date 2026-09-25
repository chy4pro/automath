# CODEX TICKET (luna, engineering only) — github_pkg2 acceptance FAILED; fix in place. Repo: engine/harvest/k1695_github_pkg/repo
# Spec = engine/briefs/k1695_github_pkg2/TICKET.md (re-read it). Acceptance checks below are mandatory; print each as PASS/FAIL
# to engine/harvest/k1695_github_pkg/ACCEPT3.log and write DONE-github_pkg3 ONLY if all PASS. No push, no upload, no remote.
F1 Size: working tree is 291 MB (certificates/ 214 MB, MANIFEST.sha256 17 MB). Target <= 150 MB. Move the bulky certificate
   families (raw .ms inputs, per-cell msolve outputs) into a separate release bundle directory engine/harvest/k1695_github_pkg/bundle/
   (tar.zst per family + sha256), keep in the repo only: the certificate INDEX (family, cell id, sha256, size), the checkers,
   the Lean sources, SUMMARY.json, and small representative certificates (<= 1 MB each). MANIFEST.sha256 must list repo files only.
   CHECK: `du -sm repo` <= 150 and `du -sm repo/.git` <= 80.
F2 History: git log still shows TWO commits with the identical message "Kourovka 16.95, n <= 4: verification package v1"
   (647d8dd3, 446214ab). Produce exactly ONE commit: `git checkout --orphan fresh && git add -A && git commit -m ... && git branch -M main`,
   then `git reflog expire --expire=now --all && git gc --prune=now --aggressive`. CHECK: `git rev-list --count HEAD` == 1.
F3 Privacy: scripts/problems/round6_r2split_check.py and scripts/problems/round6_r2split_odd.py still contain "$HOME".
   Replace by repo-relative paths (argparse default = path relative to the script). CHECK: `grep -rIl '$HOME\|user\|chenhaoyu\|gmail' --exclude-dir=.git .` prints nothing.
F4 CLAIMS.md: currently a one-paragraph compression. It must contain the EXACT C1–C7 text from the TICKET (verbatim, one
   numbered section per claim, each followed by "Evidence:" pointing to repo paths / bundle sha256). CHECK: every claim string
   from the ticket appears verbatim (diff against the ticket block).
F5 Re-run `./verify.sh quick` after F1–F4; CHECK: exit 0.
Report file: engine/harvest/k1695_github_pkg/GITHUB_PKG3_REPORT.md (what moved where, sizes, sha256 of each bundle tarball).

# ADDENDUM (owner line, 07:2x) — exact F1 split, supersedes the generic wording above:
#  IN-REPO: every .gb basis (the tiny "[1]" outputs a reader checks), the DPLL trees/JSON, controls, scripts, Lean, docs.
#  BUNDLE (tar.zst + sha256, index in repo): the .ms inputs (regenerable by run_decomposition.py) and per-node logs.
#  MANIFEST.sha256 may list bundle members by sha256 without storing them in the repo.
