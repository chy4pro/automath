#!/usr/bin/env python3
"""Assemble prompts/w61_S3_TAIL_spark.md — SECOND-FAMILY brief on the REPAIRED Lemma TAIL.

Same construction as w61_r10_build_sol_brief.py: protocol + background appendix reused from the
round-9 Qwen brief, the text under review replaced by the current (repaired) draft §7.13 D, and
the round-10 repair provenance rewritten into the author's voice so the second-family judge is
not told what the first-family judge found.
"""
import re
import pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
qwen = (ROOT / "prompts/w61_S3_TAIL_qwen.md").read_text().splitlines(keepends=True)
draft = (ROOT / "notes/proofs/wowii61_draft.md").read_text().splitlines(keepends=True)


def slice_between(lines, start_pred, end_pred):
    i = next(k for k, l in enumerate(lines) if start_pred(l))
    j = next(k for k, l in enumerate(lines) if k > i and end_pred(l))
    return "".join(lines[i:j])


protocol = slice_between(qwen,
                         lambda l: l.startswith("## REFUTE FIRST"),
                         lambda l: l.startswith("## How the appendix is organised"))
tail_of_brief = slice_between(qwen,
                              lambda l: l.startswith("## How the appendix is organised"),
                              lambda l: l.startswith("### E. **THE TEXT UNDER REVIEW"))

# the round-9 J-TAIL-EQUIV / J-TAIL-BLOCK rows quote wording the current text no longer uses
reaim = [
    ("Line 2: `TEXT VERSION REVIEWED: w61_S3_TAIL_qwen (Q24)`.",
     "Line 2: `TEXT VERSION REVIEWED: w61_S3_TAIL_spark (Q27)`."),
    ("* Boundaries: `L = λ₁`",
     "* You have a filesystem and a Python interpreter — **use them**. Put your scripts in\n"
     "  `problems/wowii/w61_S3_TAIL_spark_check.py` and keep their output. This lemma is\n"
     "  directly falsifiable by simulation: a verdict that did not simulate is not a verdict.\n"
     "* Boundaries: `L = λ₁`"),
    ("**State plainly in your verdict line whether any MATHEMATICS defect was found.**",
     "**Write the report to `problems/wowii/w61_S3_TAIL_spark.md`** (create it; do not read any\n"
     "other file in that directory). Print the verdict line to the terminal as well.\n\n"
     "**State plainly in your verdict line whether any MATHEMATICS defect was found.**"),
]
for old, new in reaim:
    if old in protocol:
        protocol = protocol.replace(old, new)
    elif old in tail_of_brief:
        tail_of_brief = tail_of_brief.replace(old, new)
    else:
        print("  WARNING: anchor not found, skipped:", old[:60])

# --- the REPAIRED §7.13 D
secD = slice_between(draft,
                     lambda l: l.startswith("### D. **Lemma TAIL, and the elimination"),
                     lambda l: l.startswith("## §7.14 owner-w61 round 5"))

for pat, rep in [
    (re.compile(r"\s*〔\*\*Repair Y1 已落地\*\*.*?〕", re.S), ""),
    (re.compile(r"\s*〔\*\*Repair Y2 已落地\*\*.*?〕", re.S), ""),
    (re.compile(r"\s*〔\*\*Repair Y3 已落地\*\*.*?〕", re.S), ""),
]:
    secD = pat.sub(rep, secD)
secD = re.sub(r"\n>\s*([.,:;])", r"\1", secD)
secD = re.sub(r"[ \t]+\n", "\n", secD)
assert "Repair Y" not in secD and "Q24" not in secD, "annotation leak"

header = pathlib.Path(ROOT / "prompts/w61_S3_TAIL_spark_header.md").read_text()
out = [header, protocol, tail_of_brief,
       "### E. **THE TEXT UNDER REVIEW — draft §7.13 D in full (current text)**\n\n", secD]
target = ROOT / "prompts/w61_S3_TAIL_spark.md"
target.write_text("".join(out))
print("wrote", target, target.stat().st_size, "bytes")
body = target.read_text()
for probe in ("Repair Y", "Q24", "已落地"):
    print(f"  leak-probe {probe!r}: {body.count(probe)} occurrence(s)")
