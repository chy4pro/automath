#!/usr/bin/env python3
"""owner-w61 round 22 -- BRIEF LINT.  Repair AD2's class fix, as a live check.

Q37 returned two BOOKKEEPING defects that read as two independent prose slips:
  * "the boundary rows are tabulated in the certified toolkit (C-3)" -- but (C-3) is a
    subsection of Appendix C.1, printed INSIDE the reviewed text; "the certified toolkit"
    strictly designates Appendix A.1.
  * "Theorem RIG (the certified toolkit)" in Corollary GFAN2-HC -- but Theorem RIG is
    proved locally, in Appendix B.
They are ONE defect.  `problems/wowii/w61_r14_build_gfan_brief.py` line 554 does

    out = re.sub(r"§7\\.(\\d+)( [A-G])?", "the certified toolkit", out)

-- a BLIND GLOBAL REWRITE of every "SS7.NN" cross-reference in the draft text into the
phrase "the certified toolkit", with no license over the references it was eating.  It ran
once and its product has been the base of every brief since (r14 -> r18 -> r20).
It also produced a THIRD site Q37 did not report: "the pre-declared failure mode L-d of
the the certified toolkit error prior" (draft: "of the SS7.6 error prior") -- a doubled
article and a reference to nothing.

This lint is the check that was missing.  Per RULING S (coverage != liveness) it is run
against the artifact that motivated it and MUST trip on it; a lint that cannot fail on the
r20 brief would be decoration.
"""
import re, sys, pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")

# The ONE legitimate occurrence: the hand-written header naming Appendix A.1.
ALLOWED_TOOLKIT_CONTEXT = "The certified toolkit. Theorem FAN says"

def lint(path):
    text = pathlib.Path(path).read_text()
    lines = text.splitlines()
    findings = []

    # Scope, exactly as the r20 builder scopes AC6: a brief may splice VERBATIM artifacts
    # inside ``` fences, and a quotation of someone else's lower-case (c-n) label is not a
    # defect in the brief's own prose.  Lint the prose only.
    infence, prose_idx = False, set()
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("```"):
            infence = not infence
            continue
        if not infence:
            prose_idx.add(i)

    # L1 -- "the certified toolkit" used as a cross-reference (i.e. anywhere but the header)
    for i, ln in enumerate(lines, 1):
        if i not in prose_idx: continue
        for m in re.finditer(r"the certified toolkit", ln, flags=re.I):
            if ALLOWED_TOOLKIT_CONTEXT in ln:
                continue
            findings.append(("L1 toolkit-as-xref", i, ln.strip()))

    # L2 -- doubled article, the fingerprint of a blind phrase substitution
    for i, ln in enumerate(lines, 1):
        if i not in prose_idx: continue
        if re.search(r"\bthe the\b", ln):
            findings.append(("L2 doubled-article", i, ln.strip()))

    # L3 -- lower-case (c-n) cross-references (the r20 AC6 defect, kept live)
    for i, ln in enumerate(lines, 1):
        if i not in prose_idx: continue
        for m in re.finditer(r"\(c-\d+\)", ln):
            findings.append(("L3 lowercase-cref", i, ln.strip()))

    # L4 -- duplicated bold appendix headings (the r20 AC5 defect, kept live)
    labels = re.findall(r"^\*\*\((C-\d+)\)", text, flags=re.M)
    for lab in sorted({l for l in labels if labels.count(l) > 1}):
        findings.append(("L4 duplicate-heading", 0, "**(%s) appears %d times" % (lab, labels.count(lab))))

    return findings

TARGETS = ["prompts/w61_S3_GFAN_r20.md", "prompts/w61_S3_GFAN_r18.md"]
trip = {}
for t in TARGETS:
    p = ROOT / t
    if not p.exists():
        print("== %s : ABSENT, skipped" % t); continue
    f = lint(p)
    trip[t] = f
    print("== %s : %d finding(s)" % (t, len(f)))
    for kind, i, ln in f:
        print("   [%s] line %s : %s" % (kind, i, (ln[:110] + "...") if len(ln) > 110 else ln))
    print()

# RULING S liveness: this lint MUST fire on the r20 brief, which is what motivated it.
r20 = trip.get("prompts/w61_S3_GFAN_r20.md", [])
kinds = {k for k, _, _ in r20}
print("LIVENESS (RULING S) -- the lint fires on the very artifact that motivated it:")
print("  r20 findings            : %d" % len(r20))
print("  toolkit-as-xref present : %s" % ("L1 toolkit-as-xref" in kinds))
print("  doubled-article present : %s" % ("L2 doubled-article" in kinds))
ok = len(r20) >= 3 and "L1 toolkit-as-xref" in kinds and "L2 doubled-article" in kinds
print("  LIVENESS: %s" % ("PASS -- the check can fail" if ok else "FAIL -- decoration, do not ship"))
sys.exit(0 if ok else 1)
