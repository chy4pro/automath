# CODEX TICKET (writing; sol) — announcement drafts for Paper 1: X thread + Zenodo metadata +
# GitHub release notes. NOTHING is posted by you; the exact texts go to the owner for approval.
# Repo: $HOME/workspace/claudecode/automath. Inputs: problems/etp677/pub/PLAN_0830.md,
# the draft paper problems/etp677/pub/paper1/ (or its CLAIMS.md), the GitHub package
# problems/etp677/pub/github/README.md, and the previous papers' announcement/Zenodo metadata
# under problems/*/pub/ (copy the author/affiliation/license conventions and the AI-assistance
# disclosure exactly as used before). No owner e-mail. DONE marker: DONE-ANNOUNCE.

## Deliverables (problems/etp677/pub/announce/)
1. x_thread.md — a thread of ≤ 8 posts, each ≤ 280 characters, plain and precise:
   (1) the result: a minimal finite counterexample to the ETP implication 677 ⟹ 255 must be
   simple or have all congruence classes of size ≥ 5 — the implication itself remains OPEN;
   (2) what "677" and "255" are (the two equations, one line each); (3) how: pair-indexed
   quotient extensions + a gauge-free local core; fibre 2 by hand, fibre 3 by a finite
   classification, fibre 4 using the E255 failure; (4) verification: Lean 4 (clean for 2/3,
   one SAT certificate for 4), DRAT proofs checked independently, two encodings, three
   solver families; (5) sharpness: the local method stops at 5 (explicit witness) — an
   invitation to extend it or break it; (6) also closed: group-action row templates (A5 etc.)
   as counterexample sources; (7) links: paper (Zenodo DOI placeholder), GitHub repo
   (verify.sh), Lean sources; (8) the AI-assistance disclosure sentence used in the previous
   announcements. Provide an alternative 3-post short version.
2. zenodo.json — metadata in the exact schema used for the previous deposits (title, authors,
   description ≤ 2000 chars with the theorem and the verification status, keywords: equational
   theories project, magma, finite implication, SAT, DRAT, Lean 4; license CC-BY-4.0;
   related identifiers: the GitHub repo URL; version 1.0.0).
3. github_release.md — release notes for v1.0.0 (what is in the repo, how to verify in 30
   minutes, how to attempt falsification, checksums pointer).
4. arxiv_abstract.md — abstract + MSC classes + comments line, in case endorsement is
   available (say clearly it is optional).
All texts must match the paper's claims exactly; no "solved 677", no engine names; the
result is a structure theorem, the implication is open.
