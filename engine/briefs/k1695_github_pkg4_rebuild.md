# CODEX TICKET (sol high) — REBUILD the Kourovka 16.95 public verification package from sources.
# Background: the previously assembled repo at engine/harvest/k1695_github_pkg/repo was destroyed by an engineering
# screen during a history rewrite (orphan checkout + gc before commit); the wreck is kept at
# engine/harvest/k1695_github_pkg/repo_wrecked_0723 (do NOT use it, do NOT delete it). All sources still exist in the tree.
# Specs, in order of precedence: (1) engine/briefs/k1695_github_pkg2/TICKET.md (CLAIMS C1–C7 verbatim text, fix list, size,
# one commit); (2) engine/briefs/k1695_github_pkg/TICKET.md (original assembly spec: contents, verify.sh, docs);
# (3) engine/briefs/k1695_github_pkg3_fixup.md incl. its ADDENDUM (exact in-repo/bundle split, acceptance checks F1–F5).
# Output: engine/harvest/k1695_github_pkg/repo (fresh), engine/harvest/k1695_github_pkg/bundle/ (tar.zst + SHA256SUMS),
# engine/harvest/k1695_github_pkg/ACCEPT4.log (F1..F5 PASS/FAIL, one line each, with the measured numbers),
# engine/harvest/k1695_github_pkg/GITHUB_PKG4_REPORT.md, and DONE-github_pkg4 ONLY if all five PASS.
# HARD RULES: build the tree first, `git init && git add -A && git commit` ONCE — never checkout --orphan, never
# reflog expire / gc --prune / filter-branch / rm -rf inside the repo; if a rebuild is needed, delete and re-create
# the whole repo directory from sources instead. Copy sources (cp), never mv them out of engine/harvest or lean/.
# No push, no remote, no upload, no network. Memory: no lake build (Lean sources are copied, `lake build` is documented
# in BUILD.md but NOT run here); verify.sh quick may run msolve on the tiny [1] bases only (≤ 2 processes).
# Privacy: grep-zero for $HOME, user, chenhaoyu, gmail, codex, luna, dialogue, "line-k1695", engine/harvest.
