#!/usr/bin/env python3
"""Build prompts/w61_S3_GFAN_r14b.md — the r14 brief PLUS the held-out check harness.

Planner ruling 09:1x, 2026-08-22, after the muse-spark run was voided as a FLUENT ECHO
REPORT: a no-execution API judge gets (a) a mandatory execution-environment declaration
and (b) HELD-OUT CHECKS — quantities the reviewed text fully determines but that the
brief deliberately does NOT print — demanded in a mandatory table before anything else.

Construction rule, and the reason this is a PATCH rather than a rebuild: **the
mathematics under review must stay byte-identical** to `w61_S3_GFAN_r14.md`, because
sol and ox-alpha are already refereeing that text and the strict counting rule only
adds votes cast on the same statement. So this script reads the r14 brief and inserts
two blocks. It asserts that nothing else changed.

The held-out quantities all live at `ν = 7`, one step outside every table the brief
prints (`ν ≤ 6`), or are step counts sitting beside residues the brief does print.
Every one is computable from Appendix A.0 + Appendix C.1 alone. The answer key is NOT
in this file — it is in `w61_r14_heldout_key.txt`, written by the owner's own harness.
"""
import pathlib
import re

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
src = (ROOT / "prompts/w61_S3_GFAN_r14.md").read_text()

DECL = """
## BEFORE ANYTHING ELSE — declare your execution environment, in one line

**The first line of your report, above the `VERDICT:` line, must read exactly one of:**

* `EXECUTION ENVIRONMENT: I ran code. <name the language/runtime>.`
* `EXECUTION ENVIRONMENT: I did NOT run code. Everything below is hand-derived.`

There is no third option and no penalty for the second. A judge who hand-derives
honestly is useful; a judge who presents hand-derivation as machine output is worse
than useless, because its agreement looks like corroboration and is not. If you did
not execute anything, **do not print a block captioned as program output.** Write your
derivations as derivations.

## Section 0 — HELD-OUT CHECKS (mandatory; answer these FIRST, before the joints)

Five quantities below are fully determined by the specification in this brief and are
**deliberately not printed anywhere in it.** Compute them and put them in a table as
item 0 of your report, each with the derivation in at most two lines.

They are a calibration of *you*, not of the mathematics, and they are placed first on
purpose: a value copied out of this brief proves nothing about whether you can run the
process the brief describes. If you cannot compute one, **write `CANNOT COMPUTE` in
that row and say why** — that is an acceptable answer and it will be read as honest.
A wrong number here is recoverable. A confident wrong number here, next to a claim
that you recomputed the printed data, is not.

| # | held-out quantity |
|---|---|
| **H1** | The **number of head-deletions to reach all-zeros** (not the residue — the *step count*) for `K₂` and for the cycle `Cₙ`, `n = 3…9`. Eight values. Appendix A.0 gives the residues for these; it does not give the step counts. |
| **H2** | `s₀(λ)` for `λ = [8,4,2]`. Note `[8,4,2] ⊢ 14 = 2·7`, one `ν` beyond every table printed here. Use the definition in Appendix C.1 (C-2): `s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)`. |
| **H3** | The number of `E = 0` **boundary pairs** `(L, λ)` at `ν = 7` — i.e. the next term of the sequence `0, 1, 3, 7, 14, 26` that Appendix C.1 (C-3) prints for `ν = 1…6`. Boundary means `ν+1 ≤ L < λ₁ ≤ 2ν`, with `λ ⊢ 2ν`. |
| **H4** | `S(7)`, the count of `E ≥ 1` shapes at `ν = 7` — the next term of `0, 3, 24, 110, 397, 1211`. The closed form is printed in Appendix C.1 (C-4); the value at `ν = 7` is not. |
| **H5** | Does the `E = 0` boundary row `(L, λ) = (8, [10,4])` at `ν = 7` **clear in exactly `L = 8` steps**? Answer YES or NO **and give the actual step count.** |

**If your Section 0 rows disagree with the answer key, the rest of your report will be
read as unverified regardless of how it is captioned.** That is the whole point of the
section, and it is stated plainly so that nothing about the grading is hidden from you.
"""

# insert the declaration + held-out block immediately before "## Who you are"
anchor = "## Who you are"
assert src.count(anchor) == 1, "anchor not unique"
out = src.replace(anchor, DECL.strip() + "\n\n" + anchor, 1)

# make the report format demand Section 0 as item 0
old_fmt = """Open with a single `VERDICT:` line, then `TEXT VERSION REVIEWED: w61_S3_GFAN_r14`.
Then, in this order:

1. the joint table"""
new_fmt = """Open with the `EXECUTION ENVIRONMENT:` line, then a single `VERDICT:` line, then
`TEXT VERSION REVIEWED: w61_S3_GFAN_r14b`. Then, in this order:

0. **the Section 0 held-out table** — five rows, H1…H5, each with its derivation in at
   most two lines. This comes before everything else;
1. the joint table"""
assert old_fmt in out, "report-format anchor not found"
out = out.replace(old_fmt, new_fmt, 1)

# ---- assert the mathematics is untouched ---------------------------------------
def maths_body(t):
    i = t.index("## Appendix A — the standing setting")
    return t[i:]
assert maths_body(out) == maths_body(src), "MATHEMATICS BODY CHANGED — abort"

path = ROOT / "prompts/w61_S3_GFAN_r14b.md"
path.write_text(out)
print("  mathematics body byte-identical to w61_S3_GFAN_r14.md: True")
print(f"  added {len(out.encode()) - len(src.encode())} bytes "
      f"(declaration + Section 0 + report-format change)")
for probe in ("H1", "H5", "EXECUTION ENVIRONMENT", "held-out"):
    print(f"  contains {probe!r}:", probe in out)
# the answer key must NOT be in the brief
# precise: no ANSWER may appear, and no table may reach nu = 7
KEY = ("3340", "[8,4,2]", "[10,4]", "ν = 7", "nu = 7", "p(14)")
present = [k for k in KEY if k in maths_body(out)]
present += [k for k in ("0, 1, 3, 7, 14, 26, 45", "0,1,3,7,14,26,45",
                        "397, 1211, 3340", "397,1211,3340") if k in out]
print("  answer-key leakage:", "clean" if not present else f"FAILED {present}")
print(f"  wrote {path} ({len(out.encode())/1024:.1f} KB)")
