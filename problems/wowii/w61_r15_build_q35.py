#!/usr/bin/env python3
"""Build prompts/w61_S3_GFAN_r15.md — the Q35 brief (Part 2, family 1).

Q35 is specified in the campaign ledger's TOP RESUME POINTER. This script is a PATCH of
the AC1/AC1b-repaired regeneration `prompts/w61_S3_GFAN_r15_pending.md`; it does not
rebuild the mathematics and asserts the mathematics body is byte-identical to it.

Four things the spec requires and this patch implements:

 1. SCOPE = Part 2 (Theorem GFANnu, Corollary GFANnu-HC). Part 1 is closed and is
    re-labelled CONTEXT, not target. It is NOT deleted: the Part-1 lemmas FAN-4'/8'/6'
    and GFAN2 are exactly the imports Theorem GFANnu reaches for, and two rounds were
    already lost to GAP-on-imports. Byte economy is worth less than a checkable import.
 2. HELD-OUT HARNESS, mandatory, with a FRESH key (`w61_r15_heldout_key.txt`) — the
    round-14 key is burned, the ledger prints its values.
 3. The ROSTER CARVE-OUT. Theorem GFANnu is computer-assisted and its one obligation
    that a no-execution judge cannot discharge is the COMPLETENESS of the 72-survivor
    roster inside 1745 shapes. Per the spec's option (b), a no-execution judge is told
    not to attempt it and to mark it out of scope; everything else in Part 2 is
    hand-checkable from Appendix C.1 and IS scored.
 4. The report-format and version stamps move to r15.

ONE product: `prompts/w61_S3_GFAN_r15.md`.
"""
import pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
src = (ROOT / "prompts/w61_S3_GFAN_r15_pending.md").read_text()
out = src

# --------------------------------------------------------------- 1. target block
OLD_TARGET = """TARGET, in two parts:

* **Part 1 (seven statements):** Lemma FAN-4', Lemma FAN-8', Lemma FAN-6',
  Theorem GFAN2, Corollary RIG-1, Corollary GFAN2-HC, Corollary GFAN2-L3.
* **Part 2 (the computer-assisted one, two statements):** Theorem GFANnu
  (`1 <= nu <= 6`) and Corollary GFANnu-HC.

Lemma CAP, Corollary CAP1, Theorem RIG and Corollary RIG-2 are printed in Appendix B
as well. They are **context** for Part 1 rather than its target, but they are not
exempt: if you find a defect in them, report it."""
NEW_TARGET = """TARGET — **two statements, and only two**:

> **Theorem GFANnu (`1 <= nu <= 6`)** and **Corollary GFANnu-HC**, both in Appendix C.

Everything else in this file — Lemma CAP, Corollary CAP1, Theorem RIG, Corollary RIG-1,
Corollary RIG-2, Lemma FAN-4', Lemma FAN-8', Lemma FAN-6', Theorem GFAN2, Corollaries
GFAN2-HC and GFAN2-L3 in Appendix B, and every fact in Appendix A — is **CONTEXT**.
It is printed in full for one reason: Theorem GFANnu's proof reaches for those
statements, and you cannot check an import you cannot read. Earlier rounds of this
review were wasted precisely because imported statements were named and not printed.

**What "context" means here, exactly.** You are *not* asked to referee the context's own
proofs, and a verdict on them is not what this round counts. You *are* asked to check
every point where the target reaches into them (joint **J-IMPORT**). And if you happen
to see a defect in the context, **report it** — it will be read and acted on; it simply
will not decide this round's verdict."""
assert OLD_TARGET in out, "target block anchor missing"
out = out.replace(OLD_TARGET, NEW_TARGET, 1)

# ------------------------------------- 2. execution declaration + held-out harness
DECL = """
## BEFORE ANYTHING ELSE — declare your execution environment, in one line

**The first line of your report, above the `VERDICT:` line, must read exactly one of:**

* `EXECUTION ENVIRONMENT: I ran code. <name the language/runtime>.`
* `EXECUTION ENVIRONMENT: I did NOT run code. Everything below is hand-derived.`

There is no third option and no penalty for the second. A judge who hand-derives
honestly is useful; a judge who presents hand-derivation as machine output is worse
than useless, because its agreement looks like corroboration and is not. If you did not
execute anything, **do not print a block captioned as program output.** Write your
derivations as derivations.

## Section 0 — HELD-OUT CHECKS (mandatory; answer these FIRST, before the joints)

Five quantities below are fully determined by the specification in this brief and are
**deliberately not printed anywhere in it.** Compute them and put them in a table as
item 0 of your report, each with the derivation in at most two lines.

They are a calibration of *you*, not of the mathematics, and they are placed first on
purpose: a value copied out of this brief proves nothing about whether you can run the
process the brief describes. If you cannot compute one, **write `CANNOT COMPUTE` in
that row and say why** — that is an acceptable answer and it will be read as honest. A
wrong number here is recoverable. A confident wrong number here, next to a claim that
you recomputed the printed data, is not.

| # | held-out quantity |
|---|---|
| **G1** | The **number of head-deletions to reach all-zeros** — the *step count* `s`, not the residue — **and** the residue, for each of these four explicit lists: `La = [3,3,2,2,2]`, `Lb = [4,4,3,3,2,2]`, `Lc = [5,5,4,4,3,3,2,2]`, `Ld = [6,6,6,6,6,6,6]`. Eight numbers. Use the run of Appendix A.0 exactly; if a list is not a step sequence in the sense of Appendix C.1 (C-1)(4), say so instead of giving a number. |
| **G2** | `s0(lam)` for `lam = [9,5,2]`. Note `[9,5,2] |- 16 = 2*8`, two values of `nu` beyond every table printed here. Definition, Appendix C.1 (C-2): `s0(lam) := steps([lam_1]^{lam_1+1} + lam)`. |
| **G3** | The number of `E = 0` **boundary pairs** `(L, lam)` at **`nu = 8`** — boundary meaning `nu+1 <= L < lam_1 <= 2nu` with `lam |- 2nu`. Appendix C.1 (C-3) prints this count for `nu = 1..6`; it does not print it at `nu = 8`. |
| **G4** | `S(8)`, the count of `E >= 1` shapes at `nu = 8`. The closed form is printed in Appendix C.1 (C-4); its value at `nu = 8` is not. |
| **G5** | Does the `E = 0` boundary row `(L, lam) = (10, [12,4])` at `nu = 8` **clear in exactly `L = 10` steps**? Answer YES or NO **and give the actual step count.** |

**If your Section 0 rows disagree with the answer key, the rest of your report will be
read as unverified regardless of how it is captioned.** That is the whole point of the
section, and it is stated plainly so that nothing about the grading is hidden from you.

## What this round scores, and the ONE obligation it does not ask you for

Theorem GFANnu is a **computer-assisted** theorem and says so. Its case list is finite
because of Lemma FAN-4', Lemma FAN-8', Lemma TAIL and the theorem's own hypothesis
`L >= nu + 1`; inside that finite list, every step **except one** is checkable by hand
from Appendix C.1 alone. The exception is the **completeness of the `E >= 1` survivor
roster** — the claim that the `72` printed rows are *all* the rows clearing in exactly
`L` steps among the `1745` enumerated shapes.

* **If you ran code:** check it, and say how.
* **If you did NOT run code: do not attempt it, and do not certify it.** Write
  `NOT IN SCOPE (no execution)` on that row. Guessing it, or waving it through because
  the surrounding text looks careful, is the single worst thing you can do in this
  round. It is not a defect in the brief that you cannot discharge it; it is a property
  of the obligation.

**Everything else in Part 2 is in scope for you either way** and every piece of it is
hand-checkable: the finiteness argument and the disjointness/exhaustiveness of its
three-way split; the quantifier range `1 <= nu <= 6`; the `E = 0` criterion via Lemma
TAIL and the `159`-partition `s0` column; the `51` printed `E = 0` boundary rows; the
closed form `S(nu)` and the six values it produces; the application of Lemma FAN-6' to
every printed survivor; the five conventions of Appendix C.1 (C-1); Corollary
GFANnu-HC's arithmetic and its dependency on Theorem RIG; and **every import**.
"""
anchor = "## Who you are"
assert out.count(anchor) == 1, "who-you-are anchor not unique"
out = out.replace(anchor, DECL.strip() + "\n\n" + anchor, 1)

# ----------------------------------------------------------- 3. joint table scope
OLD_JOINTS = "## Named joints — give each an explicit verdict\n"
NEW_JOINTS = """## Named joints — give each an explicit verdict

**Scoring:** the joints marked **(TARGET)** decide this round. The joints marked
**(context)** are printed so that a defect you happen to find there gets reported; they
do not decide the verdict, and `NOT REVIEWED` is an acceptable answer on any of them.
**J-IMPORT is a TARGET joint even though it points at context statements** — a
mismatched import is a defect *of the target*, not of the thing imported.

"""
assert OLD_JOINTS in out
out = out.replace(OLD_JOINTS, NEW_JOINTS, 1)

for j in ("J-FAN4P", "J-FAN8P", "J-FAN6P", "J-GFAN2", "J-RIG1"):
    old = f"| **{j}** |"
    assert old in out, f"joint {j} missing"
    out = out.replace(old, f"| **{j}** *(context)* |", 1)
out = out.replace("| **J-CORHC** |",
                  "| **J-CORHC** *(TARGET for GFANnu-HC only; context for GFAN2-HC / "
                  "GFAN2-L3)* |", 1)
for j in ("J-FIN", "J-SPEC", "J-DATA", "J-KILL", "J-IMPORT", "J-SCOPE"):
    old = f"| **{j}** |"
    assert old in out, f"joint {j} missing"
    out = out.replace(old, f"| **{j}** *(TARGET)* |", 1)
out = out.replace("| **J-FIN** *(TARGET)* | (Part 2) ", "| **J-FIN** *(TARGET)* | ")
out = out.replace("| **J-SPEC** *(TARGET)* | (Part 2) ", "| **J-SPEC** *(TARGET)* | ")
out = out.replace("| **J-DATA** *(TARGET)* | (Part 2) ", "| **J-DATA** *(TARGET)* | ")
out = out.replace("| **J-KILL** *(TARGET)* | (Part 2) ", "| **J-KILL** *(TARGET)* | ")

# the roster row of J-DATA must carry the carve-out
OLD_DATA = ("regenerate the roster of `72` surviving `E >= 1` rows and ask whether it is "
            "**complete** — does your run produce a survivor that is not printed? Is any "
            "printed row not actually a survivor?")
NEW_DATA = ("and **if and only if you ran code**, regenerate the roster of `72` surviving "
            "`E >= 1` rows and ask whether it is **complete** — does your run produce a "
            "survivor that is not printed? Is any printed row not actually a survivor? "
            "**If you did not run code, write `NOT IN SCOPE (no execution)` for the "
            "completeness sub-claim** and answer the rest of this joint, which is "
            "hand-checkable.")
assert OLD_DATA in out, "J-DATA roster anchor missing"
out = out.replace(OLD_DATA, NEW_DATA, 1)

# J-SCOPE / J-IMPORT wording: keep, but restrict the scored surface to the target
OLD_SCOPE = "| **J-SCOPE** *(TARGET)* | Every statement in this file:"
NEW_SCOPE = "| **J-SCOPE** *(TARGET)* | For **Theorem GFANnu and Corollary GFANnu-HC**:"
assert OLD_SCOPE in out
out = out.replace(OLD_SCOPE, NEW_SCOPE, 1)

# ------------------------------------------------------------ 4. report format
OLD_FMT = """Open with a single `VERDICT:` line, then `TEXT VERSION REVIEWED: w61_S3_GFAN_r14`.
Then, in this order:

1. the joint table"""
NEW_FMT = """Open with the `EXECUTION ENVIRONMENT:` line, then a single `VERDICT:` line, then
`TEXT VERSION REVIEWED: w61_S3_GFAN_r15`. Then, in this order:

0. **the Section 0 held-out table** — five rows, G1...G5, each with its derivation in at
   most two lines. This comes before everything else;
1. the joint table"""
assert OLD_FMT in out, "report-format anchor missing"
out = out.replace(OLD_FMT, NEW_FMT, 1)

# the verdict line must say which of the two target statements it applies to
OLD_TAGS = "## Verdict tags — use exactly one\n"
NEW_TAGS = """## Verdict tags — use exactly one, PER TARGET STATEMENT

Give **two** verdict lines, one for Theorem GFANnu and one for Corollary GFANnu-HC, and
then the single overall `VERDICT:` line the report format asks for. A defect in one of
the two is not automatically a defect in the other, and a joint verdict that hides which
statement is affected cannot be scored.

"""
assert OLD_TAGS in out
out = out.replace(OLD_TAGS, NEW_TAGS, 1)

# ---------------------------------------------------- assertions before writing
def maths_body(t):
    i = t.index("## Appendix A — the standing setting")
    return t[i:]


assert maths_body(out) == maths_body(src), "MATHEMATICS BODY CHANGED — abort"

# the answer key must not have leaked into the brief
KEY_VALUES = ("8457", "= 11", "nu = 8 = 75", " 75 ", "3340", "0,1,3,7,14,26,45",
              "0, 1, 3, 7, 14, 26, 45", "397, 1211, 3340", "steps = ")
leaked = [k for k in KEY_VALUES if k in out]
# the MB1 mismatched-import defect must be gone from the reviewed text
mb1_sites = [ln for ln in out.splitlines()
             if "MB1" in ln and "Corollary MB1 (a floor on L)" not in ln]
# banned-provenance leak check, same list as the builder
BANNED = ("Q25", "Q30", "Q33", "Q34", "Q35", "Repair ", "Repairs ", "LANDED",
          "PROVED-S3", "§7.", "muse-spark", "ox-alpha", "owner-w61", "planner",
          "Qwen", "w61_r14", "w61_r15", "heldout", "held-out answer key")
probe = out.replace("held-out", "").replace("HELD-OUT", "")
leaks = [w for w in BANNED if w in probe]

print("  mathematics body byte-identical to r15_pending:", maths_body(out) == maths_body(src))
print("  answer-key leakage:", "clean" if not leaked else f"CHECK {leaked}")
print("  provenance leak check:", "clean" if not leaks else f"FAILED {leaks}")
print("  residual MB1 citations outside its own statement:", len(mb1_sites))
for ln in mb1_sites:
    print("      ", ln.strip()[:110])
for probe_s in ("G1", "G5", "EXECUTION ENVIRONMENT", "NOT IN SCOPE (no execution)",
                "TARGET —", "*(TARGET)*", "*(context)*"):
    print(f"  contains {probe_s!r}:", probe_s in out)

path = ROOT / "prompts/w61_S3_GFAN_r15.md"
path.write_text(out)
print(f"  wrote {path} ({len(out.encode()) / 1024:.1f} KB, "
      f"{len(out.splitlines())} lines)")
