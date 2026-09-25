# CODEX TICKET (sol tier, ADVERSARIAL) — audit of the R46 claims of line-677 before any of
# them is written up. Repo: $HOME/workspace/claudecode/automath. English.
# Local compute: reading + pure Python + kissat/lake runs ≤ 120 s each, total ≤ 45 min.

## What to audit
`problems/etp677/campaign_registry.md`, the section "# ROUND 46 …" (STEP 0 through the last
STEP present when you start; grep for "## R46 STEP"). Every claim there is a candidate for
the line's next paper section. Your job is to find OVERSTATEMENTS — this campaign's
historical failure species is "statement stronger than its source" (three papers, first pass
INVALID, every defect of that species). Also audit the toolkit-style summaries inside those
STEPs against the artifacts they cite.

## Method (pre-registered)
For EVERY sentence in R46 that asserts a fact, produce a row: claim | evidence artifact
(path) | evidence actually shows | verdict ∈ {EXACT, OVERSTATED, UNDERSTATED, UNSUPPORTED,
UNVERIFIABLE}. Specific checks you must run yourself (not read):
 A1 The four DRAT-verified F31 proofs (ext/out/drat/*.drat): re-run drat-trim on each
    against its CNF (paths in STEP 6); confirm `s VERIFIED`.
 A2 The wiring controls (STEP 4): regenerate one gauge-twisted CNF with
    `ext/ext_cnf.py --fix-product f5 --fix-gauge 1 --no-defect --base f7a --m 5`, solve
    (seconds), decode with `ext/ext_decode_verify.py`; and the `--gauge-bad` twin → UNSAT.
 A3 The Lean claims (STEP 8, 9 and the decide upgrade): `lake build` in lean/etp677_certs
    and lean/etp677_ext; run `#print axioms` yourself on every theorem named in the registry
    and compare with the axiom lists WRITTEN in the registry; flag any mismatch in either
    direction.
 A4 STEP 1's "STRUCTURED NOVELTY CHECK" of memoryleak47/eq677: fetch the file
    (`gh api repos/memoryleak47/eq677/contents/color-extensions.py`) and state exactly
    what it searches (fibre op family, defect or not, which bases) — does the registry's
    description match?
 A5 STEP 1's logical chain "(R7-C) minimal counterexample is simple OR an extension with a
    defect over a non-idempotent level; fibre size in the 677 spectrum; defect level WLOG
    a = 1": check each link against R7A_report.md (R7-C section) and lean/etp677_ext/
    Ext677.lean; name any link that is asserted but not certified anywhere.
 A6 The outcome map wording: "UNSAT ⟹ NTS closed for (B,m)" — is "NTS closed" the right
    scope? (NTS as defined in REGISTER_A.md is the whole extension escape; an UNSAT at one
    (B,m) closes only that cell.) Propose exact replacement wording.
 A7 Cost/number hygiene: every dollar figure and every variable/clause count in R46 — is
    it reproducible from a printed artifact (generator output, `ls`, cloud console)? Mark
    those typed from memory.

## Deliverables
`engine/out/codex/etp677_r46_audit_report.md`: the claim table, the A1–A7 results with
command outputs quoted, a ranked list of the overstatements found (most consequential
first) with proposed replacement wording, ending with DONE-R46AUDIT. If you find nothing
overstated, say so and show the table anyway — an empty defect list must be earned, not
declared.
