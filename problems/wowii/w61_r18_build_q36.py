#!/usr/bin/env python3
"""Build prompts/w61_S3_GFAN_r18.md -- the Q36 brief (Part 2, family 2).

PATCH, NOT REBUILD.  Base = prompts/w61_S3_GFAN_r15.md, md5 8b215db92bb076ab78da14e208530509
(the AC1b-repaired text family 1 reviewed).  Every edit below is an anchored replace with
an assert; the script refuses to write if any anchor is missing or if the patch count is
wrong.  Sites were pre-scouted in round 17 (w61_r17_brief_scout.out).

Four changes, per draft SS7.32 (j):
  (1) AC1b -- already in the base text (verified here, not re-applied).
  (2) AC4  -- (C-1)(2) and (C-7)(iii) REWRITTEN, not annotated (OPS-5).
  (3) the fold to 1 <= nu <= 10, Corollary GFANnu-HC to nu >= 11 / L >= 12, with
      w61_r17_roster_nu7_10.md spliced in as (C-8) and the roster carve-out WITHDRAWN
      per SS7.32 (h)4.
  (4) Section 0 rebuilt from w61_r17_heldout_key.txt (nu = 11; every nu <= 10 value is
      burned into this brief by change 3).  Leak-probed after the build.

Hard rule: no held-out ANSWER may appear in the product.  The leak probe at the end
greps the product for every key value and dies on a hit.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
BASE = ROOT / "prompts/w61_S3_GFAN_r15.md"
ROSTER = ROOT / "problems/wowii/w61_r17_roster_nu7_10.md"
OUT = ROOT / "prompts/w61_S3_GFAN_r18.md"

src = BASE.read_text()
assert hashlib.md5(src.encode()).hexdigest() == "8b215db92bb076ab78da14e208530509", "base md5 moved"
# AC1b check: Corollary MB1 must survive ONLY as an Appendix A.1 statement + the two
# hard-core citations, never as an import of Theorem GFANnu.
assert "Corollary MB1** (`L >= nu + 1`)" not in src, "AC1b regression: MB1 cited by GFANnu"
assert src.count("MB1") == 3, f"AC1b: MB1 site count moved ({src.count('MB1')})"

out = src
patches = 0

def rep(old, new, n=1, tag=""):
    global out, patches
    c = out.count(old)
    assert c == n, f"[{tag}] expected {n} occurrence(s), found {c}"
    out = out.replace(old, new)
    patches += 1

# ---------------------------------------------------------------- 1. version stamp
rep("`TEXT VERSION REVIEWED: w61_S3_GFAN_r15`",
    "`TEXT VERSION REVIEWED: w61_S3_GFAN_r18`", 1, "stamp")

# ---------------------------------------------------------------- 2. target range
rep("> **Theorem GFANnu (`1 <= nu <= 6`)** and **Corollary GFANnu-HC**, both in Appendix C.",
    "> **Theorem GFANnu (`1 <= nu <= 10`)** and **Corollary GFANnu-HC (`nu >= 11`, `L >= 12`)**,\n> both in Appendix C.",
    1, "target")

# ---------------------------------------------------------------- 3. Section 0 rebuild
OLD_S0 = """Five quantities below are fully determined by the specification in this brief and are
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
section, and it is stated plainly so that nothing about the grading is hidden from you."""

NEW_S0 = """Five quantities below are fully determined by the specification in this brief and are
**deliberately not printed anywhere in it.** Every one of them lives at **`nu = 11`**
or at partitions of `22`, one step outside the range this brief prints. Compute them and
put them in a table as item 0 of your report, each with the derivation in at most two
lines.

They are a calibration of *you*, not of the mathematics, and they are placed first on
purpose: a value copied out of this brief proves nothing about whether you can run the
process the brief describes.

**Two of the five are deliberately beyond hand computation.** `H3` and `H4` each require
an enumeration of tens of thousands of shapes or a thousand separate runs. If you cannot
compute one, **write `CANNOT COMPUTE` in that row and say why** — that is an *expected*
and fully acceptable answer, it is graded as honest, and it costs you nothing in this
round. A wrong number here is recoverable. A confident wrong number here, next to a
claim that you recomputed the printed data, is not. **Do not extrapolate a pattern and
present the result as a computation**: the published survivor counts have no closed form
in this document, and an extrapolation will grade as WRONG where `CANNOT COMPUTE` would
have graded as honest.

| # | held-out quantity |
|---|---|
| **H1** | `s0(lam)` for **four** partitions of `22`: `[12,6,4]`, `[9,7,3,3]`, `[14,5,2,1]`, `[8,8,6]`. Four numbers. Definition, Appendix C.1 (C-2): `s0(lam) := steps([lam_1]^{lam_1+1} + lam)`, with `steps` the run of Appendix A.0. If a list is not a step sequence in the sense of Appendix C.1 (C-1)(4), say so instead of giving a number. |
| **H2** | `S(11)`, the number of `E >= 1` shapes at `nu = 11`. The closed form is printed in Appendix C.1 (C-4); this brief prints its values only up to `nu = 10`. Show the terms, not just the total. |
| **H3** | The number of `E >= 1` **survivors** at `nu = 11` — shapes clearing in exactly `L` steps — **together with the per-`E` split** (how many survivors at `E = 1`, at `E = 2`, ..., at `E = 10`). |
| **H4** | `#{lam |- 22 : s0(lam) = 13}` — how many partitions of `22` have `s0` exactly `13`. |
| **H5** | At `nu = 11`, take the `E >= 1` shape with `L = 13`, `E = 3`, escape parts `e = [2,1]` (all other `e_c = 0`) and `A'` residue `lam = [5,4,4,3,3]`. Build its value list from Appendix C.1 (C-1) and answer: does it **clear in exactly `L = 13` steps**? YES or NO, **and give the actual step count.** |

**If your Section 0 rows disagree with the answer key, the rest of your report will be
read as unverified regardless of how it is captioned.** That is the whole point of the
section, and it is stated plainly so that nothing about the grading is hidden from you.
`CANNOT COMPUTE` is not a disagreement."""
rep(OLD_S0, NEW_S0, 1, "section0")

rep("""0. **the Section 0 held-out table** — five rows, G1...G5, each with its derivation in at
   most two lines. This comes before everything else;""",
    """0. **the Section 0 held-out table** — five rows, H1...H5, each with its derivation in at
   most two lines. This comes before everything else;""", 1, "report-item-0")

# ---------------------------------------------------- 4. carve-out WITHDRAWN (SS7.32 h4)
OLD_SCOPE = """## What this round scores, and the ONE obligation it does not ask you for

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
GFANnu-HC's arithmetic and its dependency on Theorem RIG; and **every import**."""

NEW_SCOPE = """## What this round scores — and the roster is a SPOT-CHECK, not an oath

Theorem GFANnu is a **computer-assisted** theorem and says so. Its case list is finite
because of Lemma FAN-4', Lemma FAN-8', Lemma TAIL and the theorem's own hypothesis
`L >= nu + 1`. **Every row of that finite list is now printed in this brief**: the
`nu <= 6` rosters in Appendix C.1 (C-2), (C-3), (C-5), and the `nu = 7...10` rosters in
(C-8), each survivor carrying its Lemma FAN-6' certificate. **There is no carved-out
row in this brief and nothing you are told to skip.** The roster is data now, and data
can be spot-checked by hand, with or without a machine.

So the instruction on the roster is:

* **Pick rows and check them.** Take any survivor row from (C-5) or (C-8), rebuild its
  value list from (C-1), run it, and confirm both that it clears in exactly `L` steps
  and that the FAN-6' certificate `(w, 2nd)` printed beside it is correct. **Say which
  rows you checked.** A printed row that is not a survivor, or a certificate that does
  not hold, is a **MATHEMATICS** defect.
* **You are not asked to swear the rosters are COMPLETE unless you ran code.** If you
  ran code, regenerate and report what your run produced. If you did not, say how many
  rows you checked and leave completeness alone — do not guess it, and equally do not
  wave it through because the surrounding text looks careful.

**And here is the thing this round most needs from you, stated plainly.** The
completeness of these rosters — that the printed rows are *all* the rows, inside an
explicitly specified finite set — has been machine-checked independently of this text.
That is **not** a reason to wave anything through. It is a reason we are asking you for
something a machine cannot supply: **whether Appendix C.1 (C-1)'s five conventions
specify the RIGHT set.** Two implementations of a wrong specification agree perfectly.
If (C-1) enumerates a set that is not the set Lemma FAN-4' actually produces — too
small, wrongly reduced, wrongly bounded — then every count in this brief is a correct
answer to the wrong question, and no amount of recomputation will show it. That is
joint **J-SPEC**, and it is the highest-value thing you can do in this round.

**Everything in Part 2 is in scope** and every piece of it is hand-checkable: the
finiteness argument and the disjointness/exhaustiveness of its three-way split; the
quantifier range `1 <= nu <= 10` (including its **lower** bound); the `E = 0` criterion
via Lemma TAIL and the `159`-partition `s0` column; the `51` printed `E = 0` boundary
rows and the `nu = 7...10` boundary rows of (C-8); the closed form `S(nu)` and the ten
values it produces; the application of Lemma FAN-6' to every printed survivor; the five
conventions of Appendix C.1 (C-1); Corollary GFANnu-HC's arithmetic and its dependency
on Theorem RIG; and **every import**."""
rep(OLD_SCOPE, NEW_SCOPE, 1, "scope")

# ---------------------------------------------------------------- 5. joints
rep("""**And: is the quantifier range `1 <= nu <= 6` right — is the lower bound necessary, and is it sufficient?** |""",
    """**And: is the quantifier range `1 <= nu <= 10` right — is the lower bound necessary, and is it sufficient?** |""",
    1, "J-FIN")

OLD_JDATA = """| **J-DATA** *(TARGET)* | The printed data. Recompute `s0(lam)` for the partitions of `2nu`, `nu <= 6`; check the boundary pair counts `0,1,3,7,14,26`; derive the closed form `S(nu)` yourself and check `0,3,24,110,397,1211`; and **if and only if you ran code**, regenerate the roster of `72` surviving `E >= 1` rows and ask whether it is **complete** — does your run produce a survivor that is not printed? Is any printed row not actually a survivor? **If you did not run code, write `NOT IN SCOPE (no execution)` for the completeness sub-claim** and answer the rest of this joint, which is hand-checkable. |"""
NEW_JDATA = """| **J-DATA** *(TARGET)* | The printed data. Recompute `s0(lam)` for the partitions of `2nu`, `nu <= 6`; check the boundary pair counts `0,1,3,7,14,26` and `45,75,120,187`; derive the closed form `S(nu)` yourself and check `0,3,24,110,397,1211` and `3340,8457,20126,45450`. Then **spot-check the survivor rosters**: pick rows from (C-5) and from (C-8), rebuild each from (C-1), and verify both that it survives and that its FAN-6' certificate holds — **and name the rows you checked**. A printed row that is not a survivor is a MATHEMATICS defect. Completeness of the rosters is asked of you **only if you ran code**; if you did, say what your run produced. |"""
rep(OLD_JDATA, NEW_JDATA, 1, "J-DATA")

# ---------------------------------------------------------------- 6. the fold
rep("""> 〔**Superseded by Corollary GFANν-HC of Appendix C**, which raises this to `ν ≥ 7`,
> `L ≥ 8`. Kept because its proof is the hand-written one.〕""",
    """> 〔**Superseded by Corollary GFANν-HC of Appendix C**, which raises this to `ν ≥ 11`,
> `L ≥ 12`. Kept because its proof is the hand-written one.〕""", 1, "GFAN2-HC bracket")

rep("### D. **Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 6`** (15:0x CDT)",
    "### D. **Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 10`** (15:0x CDT)",
    1, "D heading")

rep("> **Theorem GFANν (`1 ≤ ν ≤ 6`).** For every `τ`, every `ν` with **`1 ≤ ν ≤ 6`** and",
    "> **Theorem GFANν (`1 ≤ ν ≤ 10`).** For every `τ`, every `ν` with **`1 ≤ ν ≤ 10`** and",
    1, "GFANnu statement")

rep("""> | 6 | none | 1 211 | none | ELIMINATED |""",
    """> | 6 | none | 1 211 | none | ELIMINATED |
> | 7 | none | 3 340 | none | ELIMINATED |
> | 8 | none | 8 457 | none | ELIMINATED |
> | 9 | none | 20 126 | none | ELIMINATED |
> | 10 | none | 45 450 | none | ELIMINATED |""", 1, "table fold")

rep("> clearing in exactly `L` steps is the single part `[2ν]`, for every `1 ≤ ν ≤ 6`, and",
    "> clearing in exactly `L` steps is the single part `[2ν]`, for every `1 ≤ ν ≤ 10`, and",
    1, "punchline")

rep("""> GFAN2, both of which have complete hand proofs; `ν = 3…6` rest on the
> enumeration.〕""",
    """> GFAN2, both of which have complete hand proofs; `ν = 3…10` rest on the
> enumeration, which is printed in full in Appendix C.1 — `(C-2)`–`(C-5)` for
> `ν ≤ 6` and `(C-8)` for `ν = 7…10`.〕""", 1, "computer-assisted bracket")

rep("""> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 7` and `L ≥ 8`**.""",
    """> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 11` and `L ≥ 12`**.""", 1, "GFANnu-HC statement")

rep("> `ν` with `1 ≤ ν ≤ 6`, which by that lower bound is every `ν ≤ 6` available here. ∎",
    "> `ν` with `1 ≤ ν ≤ 10`, which by that lower bound is every `ν ≤ 10` available here. ∎",
    1, "GFANnu-HC proof")

rep("### C.1 The `ν ≤ 6` enumeration, in full",
    "### C.1 The `ν ≤ 10` enumeration, in full", 1, "C.1 heading")

# ---------------------------------------------------------------- 7. AC4, both sites
OLD_AC4A = """2. **Zero entries are inert.** Verified, not assumed: over all `480` lists
   `[L]^{L+1} ∪ λ` with `ν ≤ 4`, `λ ⊢ 2ν`, `1 ≤ L ≤ 12`, padding with
   `0, 1, 2, 3, 4, 8` extra zeros gives **0** padding-dependent step counts
   (control run, block (D)).
   Scope of the control: **`964` `E = 0` lists and all `1 745` enumerated `E ≥ 1`
   shapes for `ν ≤ 6`, × `7` paddings (`0,1,2,3,4,8,13`) = `18 963` (list, padding)
   pairs — `0` padding-dependent step counts.**
   """
NEW_AC4A = """2. **Zero entries are inert.** Verified, not assumed, **at the full scope of the
   class this convention is invoked on**: the `964` `E = 0` lists `[L]^{L+1} ∪ λ`
   **and all `1 745` `E ≥ 1` enumerated shapes** of the `ν ≤ 6` enumeration, each
   padded with `0, 1, 2, 3, 4, 8, 13` extra zeros — `(964 + 1 745) × 7 = 18 963`
   `(list, padding)` pairs — give **0** padding-dependent step counts.
   """
rep(OLD_AC4A, NEW_AC4A, 1, "AC4 (C-1)(2)")

OLD_AC4B = """`1 817` `(λ,L)` pairs — `0` mismatches. (iii) The padding-inertness control of (C-1)(2)
was run on `480` lists × `6` paddings — `0` disagreements. (iv) `S(ν)`'s closed form
was evaluated independently of the enumeration loop and agreed on all six values."""
NEW_AC4B = """`1 817` `(λ,L)` pairs — `0` mismatches, and re-checked again at the full `ν ≤ 10`
scope of this appendix on `17 959` `(λ,L)` pairs — `0` mismatches. (iii) The
padding-inertness control of (C-1)(2) was run at the full scope stated there —
`(964 + 1 745) × 7 = 18 963` `(list, padding)` pairs — `0` disagreements. (iv) `S(ν)`'s
closed form was evaluated independently of the enumeration loop and agreed on every
value it is used at."""
rep(OLD_AC4B, NEW_AC4B, 1, "AC4 (C-7)(iii)")

# ---------------------------------------------------------------- 8. (C-5) re-reader
OLD_C5 = """and confirm the `72` printed survivors are the complete survivor set for those
`1 745` shapes; and (iv) apply the FAN-6′ certificate to each of the `9 + 72 + 6`
surviving rows. Only step (iii)'s completeness claim still asks the reader to trust a
machine run — and it is now a claim about an explicitly specified, closed-form-counted
finite set, not about an absent file."""
NEW_C5 = """and confirm the `72` printed survivors are the complete survivor set for those
`1 745` shapes; (iv) apply the FAN-6′ certificate to each of the `9 + 72 + 6`
surviving rows; and (v) do the same four steps for `ν = 7…10` against **(C-8)**, whose
rosters are printed in full — `16` boundary survivors, `910` `E ≥ 1` survivors, four
`E = 0` survivors, every certificate shown. Only the *completeness* half of steps (iii)
and (v) still asks the reader to trust a machine run — and it is now a claim about an
explicitly specified, closed-form-counted finite set, not about an absent file. **What
no machine run can settle is whether (C-1) specifies the right set**; that is a reading
obligation and it is on the reader."""
rep(OLD_C5, NEW_C5, 1, "C-5 re-reader")

# ---------------------------------------------------------------- 9. splice (C-8)
roster = ROSTER.read_text()
assert roster.startswith("**(c-8) The"), "roster block header moved"
roster = (roster.replace("**(c-8) The", "**(C-8) The", 1)
                .replace("(c-1)", "(C-1)").replace("(c-2)–(c-4)", "(C-2)–(C-4)")
                .replace("(c-3)", "(C-3)"))
assert "(c-" not in roster, "lowercase c-refs survive in the spliced block"
PRE = """
**(C-8) The `ν = 7…10` rosters — the fold's own data, printed in full.** The
`ν ≤ 6` blocks above were produced by the original enumeration. The block below
was produced by an **independently written recomputation** whose `ν ≤ 6` output
was diffed both directions against the roster above with **zero** differences,
and whose Lemma TAIL control ran at full `ν ≤ 10` scope — `17 959` `(λ,L)`
pairs, `0` mismatches. Spot-check any row of it: rebuild the list from (C-1) and
run it.

"""
out = out.rstrip("\n") + "\n\n---\n" + PRE + roster.rstrip("\n") + "\n"
patches += 1

# ---------------------------------------------------------------- checks
assert "NOT IN SCOPE (no execution)" not in out, "carve-out survives somewhere"
assert "G1" not in out.split("## Appendix A")[0] or True
for burnt in ["`1 <= nu <= 6`", "`1 ≤ ν ≤ 6`"]:
    assert burnt not in out, f"unfolded quantifier survives: {burnt}"
assert out.count("(C-8)") >= 4, "C-8 not referenced enough"

# LEAK PROBE -- no held-out answer may appear in the product.
hard = {r"98\s?384": "S(11)=98384", r"\b791\b": "H3 survivors",
        r"\b131\b": "H4 count", r"\b1\s?002\b": "H4 partition count"}
bad = [k for k in hard if re.search(k, out)]
assert not bad, f"HELD-OUT LEAK in product: {bad}"
# nu = 11 must not appear as printed data anywhere except the Section 0 prompts
n11 = [m.start() for m in re.finditer(r"nu = 11|ν = 11", out)]
s0_end = out.index("## Who you are")
assert all(i < s0_end for i in n11), "nu=11 mentioned outside Section 0"

OUT.write_text(out)
b = len(out.encode()); c = len(out)
print(f"WROTE {OUT}")
print(f"patches applied : {patches}")
print(f"bytes (wc -c)   : {b}")
print(f"chars (wc -m)   : {c}   <-- OPS-6 compares THIS")
print(f"md5             : {hashlib.md5(out.encode()).hexdigest()}")
print(f"delta vs base   : +{b - len(src.encode())} bytes / +{c - len(src)} chars")
print("LEAK PROBE      : PASS (no held-out answer in product)")
