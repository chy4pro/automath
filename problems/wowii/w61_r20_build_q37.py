#!/usr/bin/env python3
"""Build prompts/w61_S3_GFAN_r20.md -- the Q37 brief (Part 2, family-2 attempt #2).

PATCH, NOT REBUILD.  Base = prompts/w61_S3_GFAN_r18.md, md5 3a2c17cb1a3a45cd741ae63cad35de3f
(the text Qwen read in Q36 and GAP'd).  Every edit is an anchored replace with an assert;
the script refuses to write if any anchor is missing or a count is wrong.

Changes, per draft SS7.34 (g)/(f) and the r20 task book:
  AC5  de-duplicate the (C-8) HEADING (brief lines 993/1001) + assert heading uniqueness
       on the product AS A CLASS, not at those two lines.
  AC6  (c-3) -> (C-3) at line 755 + assert zero lower-case (c-n) refs on the product.
  STRUCT  make the completeness withdrawal STRUCTURAL: print the control figures and the
       round-17 diff artifact VERBATIM inline, and carry a binding rubric line forbidding
       a GAP whose sole ground is an explicitly withdrawn obligation -- while explicitly
       inviting the judge to attack the withdrawal's own evidence as a MATHEMATICS defect.
  STAMP  TEXT VERSION REVIEWED -> w61_S3_GFAN_r20.

RULING S (COVERAGE != LIVENESS) applied to this build: the two NEW asserts are run against
the BASE text as well as the product, and the script dies unless they FAIL on the base.
An assert that cannot fail on the very artifact that motivated it is not a check.
"""
import hashlib, pathlib, re, sys

ROOT   = pathlib.Path("$HOME/workspace/claudecode/automath")
BASE   = ROOT / "prompts/w61_S3_GFAN_r18.md"
DIFFA  = ROOT / "problems/wowii/w61_r17_roster_diff.out"
OUT    = ROOT / "prompts/w61_S3_GFAN_r20.md"

src = BASE.read_text()
assert hashlib.md5(src.encode()).hexdigest() == "3a2c17cb1a3a45cd741ae63cad35de3f", "base md5 moved"

out = src
patches = 0

def rep(old, new, n=1, tag=""):
    global out, patches
    c = out.count(old)
    assert c == n, f"[{tag}] expected {n} occurrence(s), found {c}"
    out = out.replace(old, new)
    patches += 1

# ---------------------------------------------------------------- the two NEW checks
def heading_dupes(text):
    """Return {label: count} for bold appendix headings appearing more than once."""
    labels = re.findall(r"^\*\*\((C-\d+)\)", text, flags=re.M)
    return {l: labels.count(l) for l in set(labels) if labels.count(l) > 1}

def lowercase_crefs(text):
    """Return the list of lower-case (c-n) cross-references."""
    return re.findall(r"\(c-\d+\)", text)

# ---- LIVENESS (RULING S): both new checks MUST fail on the base, or they are decoration
base_dupes = heading_dupes(src)
base_lc    = lowercase_crefs(src)
assert base_dupes == {"C-8": 2}, f"LIVENESS FAIL: heading check does not see the r18 defect ({base_dupes})"
assert base_lc == ["(c-3)"],     f"LIVENESS FAIL: c-ref check does not see the r18 defect ({base_lc})"
print(f"LIVENESS PROBE on the BASE text : heading-uniqueness TRIPS  ({base_dupes})")
print(f"LIVENESS PROBE on the BASE text : lower-case c-ref  TRIPS  ({base_lc})")

# ---------------------------------------------------------------- 1. version stamp
rep("`TEXT VERSION REVIEWED: w61_S3_GFAN_r18`",
    "`TEXT VERSION REVIEWED: w61_S3_GFAN_r20`", 1, "stamp")

# ---------------------------------------------------------------- 2. AC6
rep("tabulated in the certified toolkit (c-3), each with its",
    "tabulated in the certified toolkit (C-3), each with its", 1, "AC6")

# ---------------------------------------------------------------- 3. AC5
OLD_C8 = """**(C-8) The `ν = 7…10` rosters — the fold's own data, printed in full.** The
`ν ≤ 6` blocks above were produced by the original enumeration. The block below
was produced by an **independently written recomputation** whose `ν ≤ 6` output
was diffed both directions against the roster above with **zero** differences,
and whose Lemma TAIL control ran at full `ν ≤ 10` scope — `17 959` `(λ,L)`
pairs, `0` mismatches. Spot-check any row of it: rebuild the list from (C-1) and
run it.

**(C-8) The `ν = 7…10` rosters, printed in full.** Same specification as
(C-1), four steps outside the range (C-2)–(C-4) print. Produced by the
round-17 **independent recomputation** `w61_r17_roster_recompute.py` →
`.out`, whose `ν ≤ 6` output was diffed **both directions** against the
prior machine roster and against the printed roster of (C-2)–(C-4) with
**zero** differences (`w61_r17_roster_diff.out`)."""
NEW_C8 = """**(C-8) The `ν = 7…10` rosters — the fold's own data, printed in full.** The
`ν ≤ 6` blocks above were produced by the original enumeration; the block
below was produced by a separately written **independent recomputation**, to
the same specification as (C-1), four steps outside the range (C-2)–(C-4)
print. That recomputation's `ν ≤ 6` output was diffed **both directions**
against the prior machine roster *and* against the printed roster of
(C-2)–(C-4) with **zero** differences, and its Lemma TAIL control ran at full
`ν ≤ 10` scope — `17 959` `(λ,L)` pairs, `0` mismatches. **The diff itself is
printed verbatim in the scoring section above**, so you are not being asked to
take any of this on trust. Spot-check any row below: rebuild the list from
(C-1) and run it."""
rep(OLD_C8, NEW_C8, 1, "AC5")

# ---------------------------------------------------------------- 4. STRUCT
diff_art = DIFFA.read_text().rstrip("\n")
assert "DIFF_FAILURE_COUNT = 0" in diff_art, "diff artifact does not carry its own failure count"
assert len(diff_art) < 3000, "diff artifact unexpectedly large"

OLD_STRUCT = """**And here is the thing this round most needs from you, stated plainly.** The
completeness of these rosters — that the printed rows are *all* the rows, inside an
explicitly specified finite set — has been machine-checked independently of this text.
That is **not** a reason to wave anything through. It is a reason we are asking you for
something a machine cannot supply: **whether Appendix C.1 (C-1)'s five conventions
specify the RIGHT set.** Two implementations of a wrong specification agree perfectly.
If (C-1) enumerates a set that is not the set Lemma FAN-4' actually produces — too
small, wrongly reduced, wrongly bounded — then every count in this brief is a correct
answer to the wrong question, and no amount of recomputation will show it. That is
joint **J-SPEC**, and it is the highest-value thing you can do in this round."""

NEW_STRUCT = """### Roster completeness: DISCHARGED BEFORE THIS BRIEF, and here is the evidence, not the claim

The one obligation a reader without a machine cannot discharge is **completeness** of the
printed rosters — that the printed rows are *all* the rows inside the specified finite
set. A previous round of this review was told that this had been settled elsewhere and,
reasonably, declined to take a bare assertion. So it is not asserted here. **The
artifacts are printed inline and you are invited to attack them.**

**Control figures.** Each line below is a run that was performed, with the count it
covered and the number of disagreements it found:

| control | scope actually run | disagreements |
|---|---|---|
| Lemma TAIL formula `(L - lam_1) + s0(lam)` vs direct simulation, `nu <= 6` | `1 817` `(lam, L)` pairs | **`0`** |
| the same control re-run at the full scope of this appendix, `nu <= 10` | `17 959` `(lam, L)` pairs | **`0`** |
| padding-inertness of (C-1)(2) | `(964 + 1 745) x 7 = 18 963` `(list, padding)` pairs | **`0`** |
| independent recomputation vs the roster this text prints, **both directions** | `72`-in-`1 745` (`nu <= 6`) and `910`-in-`77 373` (`nu = 7...10`) | **`0`** |

**The diff artifact itself, verbatim** — this is the file, not a summary of it. `MINE` is
the independently written recomputation; `SOL` is the earlier machine roster it was
diffed against; `DRAFT` is the roster parsed straight out of the printed text you are
reading. It is pasted **unedited**, which is why the lower-case `(c-…)` labels inside it
are the *source draft's* own section numbering and not this brief's appendix labels — do
not read them as cross-references into Appendix C.1:

```
""" + diff_art + """
```

**What this does and does not buy.** It settles that two independently written programs
and the printed text agree. It settles **nothing** about whether the set they agree on is
the right set — two implementations of a wrong specification agree perfectly. That
residual is exactly joint **J-SPEC**: **do Appendix C.1 (C-1)'s five conventions specify
the set Lemma FAN-4' actually produces?** Too small, wrongly reduced, wrongly bounded, and
every count in this brief is a correct answer to the wrong question, with no amount of
recomputation showing it. **J-SPEC is the highest-value thing you can do in this round**,
and it is a reading obligation, not a computing one.

> **RUBRIC — binding on your verdict, and stated before you read the mathematics.**
> 1. Roster completeness is an **explicitly withdrawn** obligation in this round. Report
>    it under "What I could not check" if you did not run code — that is the honest
>    answer and it is the expected one.
> 2. **It may not be the sole ground of a `GAP`.** A `GAP` requires a proof obligation
>    *inside the reviewed text* that you could not settle and that is something other
>    than the completeness of the printed rosters. If completeness is your only
>    reservation, the verdict is `CLEAN` or `PARTIAL` **with the reservation stated in
>    full**.
> 3. **This does not lower the bar, and it is not an instruction to be agreeable.** Any
>    other unsettled obligation is a `GAP` and should be one; a counterexample is
>    `REFUTED`; a wrong printed row is a MATHEMATICS defect. Nothing here narrows what
>    you may find.
> 4. **The withdrawal itself is in scope and you may attack it.** If the diff printed
>    above does not diff what it claims, if the control does not control what it claims,
>    if "independently written" is not established by anything you can see, or if the
>    scope figures do not add up — **say so, and it is a defect, not a `GAP`.** That is a
>    live target and it is deliberately handed to you."""
rep(OLD_STRUCT, NEW_STRUCT, 1, "STRUCT")

# ---------------------------------------------------------------- 5. rubric echo at the verdict tags
rep("""`CLEAN` (no defect of either class) - `PARTIAL` (bookkeeping defects only, no
mathematics defect) - `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) - `REFUTED` (an explicit counterexample, printed in full).""",
    """`CLEAN` (no defect of either class) - `PARTIAL` (bookkeeping defects only, no
mathematics defect) - `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) - `REFUTED` (an explicit counterexample, printed in full).

**Reminder of the one rubric constraint, repeated here so it cannot be missed:** roster
completeness is an explicitly withdrawn obligation whose evidence is printed inline in
the scoring section, and it **may not be the sole ground of a `GAP`**. Every other
ground for a `GAP` stands untouched, and the withdrawal's own evidence is itself a live
target — attacking it is a defect report, not a `GAP`.""", 1, "verdict-rubric")

# ================================================================================
# STAGE 2 -- planner RULING Q: the pre-dispatch ADVERSARIAL BRIEF PASS, acted on.
# Source: automath-sandbox/out/ox-alpha/w61_r20_q37_brief_integrity.md (free engine,
# one question: "what would cause a competent reviewer to answer a DIFFERENT QUESTION
# than the one being asked?").  Every finding below was VERIFIED by grep on the stage-1
# product before it was acted on; the ones NOT acted on are recorded in draft SS7.35.
# ================================================================================

# ---- Q-1 (ox HIGH #1): Section 0 says "answer FIRST"; REFUTE FIRST step 1 says a number
#      reported before the calibration is printed does not count.  H1..H5 are numbers.
#      A reviewer must guess which rule wins.  Resolved explicitly, in favour of neither
#      being dropped: calibrate first, print both, Section 0 still leads the REPORT.
rep("""**A number you
   report before your calibration is printed does not count.** (If you cannot execute
   code, do these by hand and show the work.)""",
    """**A number you
   report before your calibration is printed does not count.** (If you cannot execute
   code, do these by hand and show the work.)
   **Precedence, so you do not have to guess:** this ordering governs the *work*;
   Section 0 governs the *report*. Do the calibration first, print it, then compute the
   Section 0 rows — and in the written report put the Section 0 table at item 0 with the
   calibration printed immediately under it. Section 0 rows backed by a printed
   calibration satisfy both rules, and nothing else is being asked of you.""",
    1, "Q-1 ordering")

# ---- Q-2 (ox HIGH #2): the completeness withdrawal contradicted itself in three places,
#      and -- the serious half -- left a code-running reviewer who REGENERATES and finds
#      the roster short with no verdict slot to put it in.  A rubric that can muzzle a
#      real finding is worse than the GAP it was written to prevent.
rep("""row in this brief and nothing you are told to skip.** The roster is data now, and data
can be spot-checked by hand, with or without a machine.""",
    """row in this brief and no row you are told to skip.** What is withdrawn is not a row and
not a check: it is the *obligation to certify the rosters COMPLETE without a machine*.
Every printed row is in scope, by hand, and so is every consequence of running code on
them. The roster is data now, and data can be spot-checked with or without a machine.""",
    1, "Q-2a no-carve-out wording")

rep("""> 2. **It may not be the sole ground of a `GAP`.** A `GAP` requires a proof obligation
>    *inside the reviewed text* that you could not settle and that is something other
>    than the completeness of the printed rosters. If completeness is your only
>    reservation, the verdict is `CLEAN` or `PARTIAL` **with the reservation stated in
>    full**.""",
    """> 2. **An *unverified* completeness claim may not be the sole ground of a `GAP`.** What
>    rule 2 forbids is one specific move: *"I could not check completeness, therefore
>    `GAP`."* If that is your only reservation, the verdict is `CLEAN` or `PARTIAL` for
>    that statement **with the reservation stated in full**. Rule 2 reaches nothing else.
> 2b. **And it explicitly does NOT reach a completeness finding you actually made.** If
>    you ran code and your run produces a shape that clears in exactly `L` steps, is not
>    killed by Lemma FAN-6', and is **not printed** — or shows that a printed row is not
>    a survivor — that is a **MATHEMATICS defect**, and if it breaks the statement it is
>    **`REFUTED`**. Print the shape. Nothing in this rubric touches that, and it is the
>    single most valuable thing a code-running reviewer could return.""",
    1, "Q-2b unclassifiable outcome")

# ---- Q-4 (ox MEDIUM-HIGH #4): the rubric told the reviewer in advance what the honest
#      answer "is".  That is verdict-steering and it is the exact species BIAS-2 exists
#      for.  Neutralised; the permission survives, the nudge does not.
rep("""> 1. Roster completeness is an **explicitly withdrawn** obligation in this round. Report
>    it under "What I could not check" if you did not run code — that is the honest
>    answer and it is the expected one.""",
    """> 1. Roster completeness is an **explicitly withdrawn** obligation in this round. If you
>    did not run code, record it under "What I could not check" and move on. No verdict
>    is being suggested to you here and none should be inferred.""",
    1, "Q-4 de-bias")

# ---- Q-3 (ox MEDIUM-HIGH #3): "a single VERDICT: line" vs "give TWO verdict lines".
rep("""Open with the `EXECUTION ENVIRONMENT:` line, then a single `VERDICT:` line, then""",
    """Open with the `EXECUTION ENVIRONMENT:` line, then the **two per-statement verdict
lines** described above (Theorem GFANnu, Corollary GFANnu-HC), then the single overall
`VERDICT:` line, then""", 1, "Q-3 verdict lines")

# ---- Q-5a (ox MEDIUM #5): the EXECUTION ENVIRONMENT section still named r14 artifacts
#      while the report format demands the r20 stamp.  A live stale-version defect that
#      rode from r14 through r15 and r18 untouched.
rep("`problems/wowii/w61_S3_GFAN_r14.md`, put your scripts in",
    "`problems/wowii/w61_S3_GFAN_r20.md`, put your scripts in", 1, "Q-5a env r14->r20 (1)")
rep("`problems/wowii/w61_S3_GFAN_r14_check.py` and keep their **raw stdout** (not a",
    "`problems/wowii/w61_S3_GFAN_r20_check.py` and keep their **raw stdout** (not a", 1, "Q-5a env r14->r20 (2)")
rep("hand-written summary) in `problems/wowii/w61_S3_GFAN_r14_check.out`. Also print the",
    "hand-written summary) in `problems/wowii/w61_S3_GFAN_r20_check.out`. Also print the", 1, "Q-5a env r14->r20 (3)")

# ---- Q-5b (ox MEDIUM #5): the reviewed text cites a `dispatch file` as evidence while
#      the restricted-files rule forbids reading any file named `dispatch`; and it cites
#      a "companion section (not supplied)" and named facts (Corollary FAN-HC, LEAD, the
#      unprimed FAN-n) that this brief does not print.  All three are the same hazard:
#      the reviewer is pointed at evidence they cannot reach.  Handled in ONE clause that
#      does not suppress anything -- an obligation that really rests on absent material
#      is a GAP and is wanted as one.
rep("""If a joint
cannot be settled without a restricted file, say so and mark that joint UNRESOLVED.""",
    """If a joint
cannot be settled without a restricted file, say so and mark that joint UNRESOLVED.

**Two consequences of that rule, spelled out so they do not cost you time.** (i) The
reviewed text below sometimes cites its own provenance — a `dispatch file` entry, a
timestamped log line. Those are exactly the files you are forbidden to open. **Treat any
such citation as unverified provenance, say so once, and do not go looking for the
file**; it is not evidence you are expected to check. (ii) The text also refers in places
to a **companion section "(not supplied)"** and names facts it does not print (for
instance `Corollary FAN-HC`, `LEAD`, and unprimed forms of the `FAN-n` lemmas where only
the primed forms are printed in Appendix A.1). Those are deliberately outside this brief
and you cannot check them. **If a TARGET obligation actually rests on one of them, say so
plainly — that is a real `GAP` and we want it.** If it only supports context, note it and
move on. Do not treat an absent name as a defect in itself.""", 1, "Q-5b unreachable citations")

# ---------------------------------------------------------------- checks on the PRODUCT
prod_dupes = heading_dupes(out)
assert prod_dupes == {}, f"AC5 FAIL: duplicate appendix headings survive: {prod_dupes}"

# AC6 is a check on the brief's OWN cross-references.  The verbatim diff artifact carries
# the SOURCE DRAFT's lower-case section labels and must not be normalised -- rewriting a
# quoted artifact to satisfy our own grep would destroy the only property that makes it
# evidence.  So the artifact block is excised for this check and then held to a STRICTER
# one: it must be byte-identical to the file on disk.  An exemption that is not itself
# checked is a hiding place; this one is checked harder than what it exempts.
FENCE = "```\n" + diff_art + "\n```"
assert out.count(FENCE) == 1, "AC6 scoping FAIL: the verbatim artifact block is not present exactly once"
prose = out.replace(FENCE, "")
prod_lc = lowercase_crefs(prose)
assert prod_lc == [],    f"AC6 FAIL: lower-case c-refs survive in the brief's own prose: {prod_lc}"
art_lc = lowercase_crefs(FENCE)
assert art_lc == ["(c-2)", "(c-3)", "(c-4)"], f"artifact content moved: {art_lc}"

# carried forward from the r18 builder -- these must not regress
assert "NOT IN SCOPE (no execution)" not in out, "carve-out reappeared"
for burnt in ["`1 <= nu <= 6`", "`1 ≤ ν ≤ 6`"]:
    assert burnt not in out, f"unfolded quantifier survives: {burnt}"
assert out.count("MB1") == 3, f"AC1b regression: MB1 site count moved ({out.count('MB1')})"
assert "Corollary MB1** (`L >= nu + 1`)" not in out, "AC1b regression: MB1 cited by GFANnu"
assert out.count("(C-8)") >= 4, "C-8 not referenced enough"
assert "w61_S3_GFAN_r18" not in out, "stale version stamp survives"
assert out.count("DIFF_FAILURE_COUNT = 0") == 1, "diff artifact not spliced exactly once"

# LEAK PROBE -- no held-out ANSWER may appear in the product.
hard = {r"98\s?384": "S(11)=98384", r"\b791\b": "H3 survivors",
        r"\b131\b": "H4 count", r"\b1\s?002\b": "H4 partition count"}
bad = [k for k in hard if re.search(k, out)]
assert not bad, f"HELD-OUT LEAK in product: {bad}"
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
print(f"delta vs r18    : +{b - len(src.encode())} bytes / +{c - len(src)} chars")
print(f"AC5 heading uniqueness on PRODUCT : PASS (dupes {prod_dupes})")
print(f"AC6 lower-case c-refs in PRODUCT PROSE : PASS (found {prod_lc})")
print(f"    verbatim diff artifact exempted, byte-identical to disk, carries {art_lc} = the SOURCE DRAFT's labels")
print("LEAK PROBE      : PASS (no held-out answer in product)")
