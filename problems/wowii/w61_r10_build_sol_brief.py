#!/usr/bin/env python3
"""Assemble prompts/w61_S3_76_sol.md — the SECOND-FAMILY brief on the REPAIRED §7.6 chain.

Sources
  * prompts/w61_S3_76_qwen.md   — the round-9 brief: protocol block + appendix A-F (background,
                                  unchanged text) are reused verbatim; header and appendix G/H/T
                                  are replaced.
  * notes/proofs/wowii61_draft.md — the REPAIRED §7.6 and the REPAIRED three-tier scope text.

Independence rule enforced here: the appendix carries the *operative* repaired text with the
repair-provenance annotations (Repair X1-X4, which name the previous judge's findings) rewritten
into the author's own voice, so the second-family judge reads corrected mathematics without being
told what the first-family judge found. The draft keeps every annotation as the audit trail.
"""
import re
import pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
qwen = (ROOT / "prompts/w61_S3_76_qwen.md").read_text().splitlines(keepends=True)
draft = (ROOT / "notes/proofs/wowii61_draft.md").read_text().splitlines(keepends=True)


def slice_between(lines, start_pred, end_pred):
    i = next(k for k, l in enumerate(lines) if start_pred(l))
    j = next(k for k, l in enumerate(lines) if k > i and end_pred(l))
    return "".join(lines[i:j])


# --- protocol block of the round-9 brief: "REFUTE FIRST" .. end of "Deliverable format"
protocol = slice_between(qwen,
                         lambda l: l.startswith("## REFUTE FIRST"),
                         lambda l: l.startswith("## How the appendix is organised"))

# the J-MB and J-L2 rows of the round-9 brief quote wording that the current text no longer
# uses; re-aim them at the text as it now stands (and thereby avoid signposting the edits)
old_jmb = ("Then the claim \"**every `b ∈ T₁ ∪ T₂` lies in `B_lo⁺`**\" — it needs the other "
           "type to be non-empty and disjoint from `b`'s B-neighbourhood; is that exactly what "
           "(F-b) supplies, for the *occurring* types, and is the quantifier over types or over "
           "the specific pair?")
new_jmb = ("Then the inclusion `B_lo ∩ (T₁ ∪ T₂) ⊆ B_lo⁺` and the `c ≤ |B_lo⁺|` drawn from it: "
           "it needs the other type to be non-empty and disjoint from `b`'s B-neighbourhood; is "
           "that exactly what (F-b) supplies, for the *occurring* types, and is the quantifier "
           "over types or over the specific pair? Is the inclusion stated over the set the count "
           "actually ranges over, and does any vertex of `T₁ ∪ T₂` outside that set enter the "
           "sum by mistake?")
assert old_jmb in protocol
protocol = protocol.replace(old_jmb, new_jmb)

old_jl2 = ("(c) is a **tightness** argument — \"Theorem MB is now tight, and re-running its "
           "degree count forces `Σ deg_A = 2`\". Tightness requires **every** link of the chain "
           "(MB's degree count, SL's (LOW3) form, and the LOW-to-SL `−1`) to be tight "
           "simultaneously; verify that is spelled out, and if it is not, say so and say whether "
           "the conclusion survives.")
new_jl2 = ("(c) is a **tightness** argument: a lower bound and an upper bound are claimed to "
           "meet at `Σ_{b∈B_lo} deg_A(b) = 2`. Check each bound separately at the stated values, "
           "check they really coincide, and check that **every** link the tightness rides on "
           "(MB's degree count, SL's (LOW3) form, and the LOW-to-SL `−1`) can hold with equality "
           "simultaneously — a squeeze whose two sides come from incompatible equality cases "
           "proves nothing. If a link is not addressed, say so and say whether the conclusion "
           "survives.")
assert old_jl2 in protocol
protocol = protocol.replace(old_jl2, new_jl2)

protocol = protocol.replace(
    "Line 2: `TEXT VERSION REVIEWED: w61_S3_76_qwen (Q23)`.",
    "Line 2: `TEXT VERSION REVIEWED: w61_S3_76_sol (Q26)`.")
protocol = protocol.replace(
    "* Boundaries to hit explicitly:",
    "* You have a filesystem and a Python interpreter — **use them**. Put your scripts in\n"
    "  `problems/wowii/w61_S3_76_sol_check.py` (one file, or several with that prefix) and\n"
    "  keep their output; a joint certified by proof-reading alone must say so.\n"
    "* Boundaries to hit explicitly:")
protocol = protocol.replace(
    "**State plainly in your verdict line whether any MATHEMATICS defect was found.**",
    "**Write the report to `problems/wowii/w61_S3_76_sol.md`** (create it; do not read any\n"
    "other file in that directory). Print the verdict line to the terminal as well.\n\n"
    "**State plainly in your verdict line whether any MATHEMATICS defect was found.**")

# --- appendix A-F (background: statement, Lemma 1/4/5, toolkit, types, C*, K-chain) verbatim
appendix_af = slice_between(qwen,
                            lambda l: l.startswith("### A. Exact statement"),
                            lambda l: l.startswith("### G. **THE TEXT UNDER REVIEW"))

# --- REPAIRED draft §7.6 (whole section) and the §7.6 G numerical backing block
sec76 = slice_between(draft,
                      lambda l: l.startswith("## §7.6 owner-w61 round 4 (2026-08-18"),
                      lambda l: l.startswith("## §7.7 owner-w61 round 4"))
sec76g = slice_between(draft,
                       lambda l: l.startswith("### §7.6 G — numerical backing"),
                       lambda l: l.startswith("## §7.8 owner-w61 round 4"))

# --- REPAIRED three-tier scope text (§7.10 Repair F3 as amended by V2 / W1 / X3)
tier = slice_between(draft,
                     lambda l: l.startswith("### Repair F3 —"),
                     lambda l: l.startswith("### Repair F4 —"))


def tidy(text):
    """Repair the line-break artifacts an excised parenthetical leaves behind."""
    text = re.sub(r"\n>\s*([.,:;])", r"\1", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text


def neutralise(text):
    """Rewrite round-10 repair provenance into the author's voice (independence firewall)."""
    subs = [
        # X1 — Theorem MB quantifier
        (re.compile(r"\s*〔\*\*Repair X1 已落地\*\*.*?〕", re.S), ""),
        # X2 — Proposition L2(c) squeeze
        (re.compile(r"\s*〔\*\*Repair X2 已落地\*\*.*?〕", re.S), ""),
        # X4 — Fan slack one-liner
        (re.compile(r"— 〔\*\*Repair X4\n已落地\*\*.*?〕", re.S), "—"),
        (re.compile(r"\s*〔\*\*Repair X4\s*\n?已落地\*\*.*?〕", re.S), ""),
    ]
    for pat, rep in subs:
        text = pat.sub(rep, text)
    return tidy(text)


sec76 = neutralise(sec76)

# X3 — the tier list: keep the corrected list and the filed-vs-needed note, drop the provenance
tier = re.sub(r"〔\*\*Repair X3 已落地\*\*.*?〕",
              """〔**Scope note (author).** The tier of a statement records **where it is used**,
not the weakest hypotheses its proof needs. Several hard-core entries are therefore
*over-hypothesised*: **Theorem MB**, **Corollary L1-short**, **Corollary MB1**,
**Proposition L1**, **Corollary L1′** and **Proposition L2** use only *frame +
reductio* (Lemma 4, Lemma C\\*, R1, (F-b), and Theorem SL, which needs `τ ≥ 2`); the
`τ ≥ 4` of the hard-core tier is inherited from Theorem T3 and is not consumed by any
of their proofs. Every call site of these six is inside the hard core, so this is
recorded, not re-tiered.〕""",
              tier, flags=re.S)
tier = tidy(tier)
tier = re.sub(r"~~With that reading every statement in §7\.6/§7\.8 is correctly scoped\.~~\s*\n〔\*\*Withdrawn by Repair X3\*\*.*?〕",
              """With the list as it stands, every statement of §7.6/§7.8 is assigned a tier at
which it is valid, and the six statements named in the scope note are valid one tier
lower than they are filed.""",
              tier, flags=re.S)

assert "Repair X" not in sec76 and "Repair X" not in tier and "Q23" not in tier, "annotation leak"

header = pathlib.Path(ROOT / "prompts/w61_S3_76_sol_header.md").read_text()

out = [
    header,
    protocol,
    """## How the appendix is organised

Appendix sections **A–F** are background: the exact conjecture and the `residueAux`
spec, the reduction and Lemmas 4/5, the τ-uniform toolkit (Lemma S, Lemma T′, Lemma
F3′, Lemma DICH, Lemma Z⁺), the type notation and (F-a)/(F-b)/(F-c), Lemma C\\* and the
block-occupancy material, and the K-chain. They are quoted so that every hypothesis
the chain leans on is present in this file; **they are not under review** except where
§7.6 uses them.

Appendix section **G** is **the text under review**: draft §7.6 in full. Appendix **H**
is its later numerical addendum. Appendix **T** is the three-tier scope assignment,
also under review.

The excerpts keep the original document's own sub-section letters ("### A.", "### B.",
…), which are **not** the appendix letters. When you cite a location, quote the line;
do not cite a letter alone.

=== APPENDIX — the text under review (authoritative) ===

""",
    appendix_af,
    "### G. **THE TEXT UNDER REVIEW — draft §7.6 in full (current text)**\n\n",
    sec76,
    "\n\n### H. **UNDER REVIEW — §7.6 G numerical backing (added later)**\n\n",
    sec76g,
    "\n\n### T. **UNDER REVIEW — the three-tier scope assignment (draft §7.10, Repair F3 as amended)**\n\n",
    tier,
]
target = ROOT / "prompts/w61_S3_76_sol.md"
target.write_text("".join(out))
print("wrote", target, target.stat().st_size, "bytes")
for probe in ("Repair X", "Q23", "Qwen", "已落地"):
    body = target.read_text()
    print(f"  leak-probe {probe!r}: {body.count(probe)} occurrence(s)")
