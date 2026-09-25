#!/usr/bin/env python3
"""
WOWII-133 round 28 -- AMENDMENT GATE on `G60`'s carried qualifier.

WHAT IS BEING CHECKED.  cert_w133_r27 section 5 ruled the "single-source as of r26"
qualifier amendable, and amendable ONLY to a form that carries the STATE rather than a
newer date:

    modulo the sections 35-37 enumerations -- two independent implementations agreeing
    as of r27, still single-author and single-specification

This gate asserts that the AMENDED form is what the statement block carries, that the
r26 form is not carried anywhere in that block, and that the malformed-citation clause
survived the amendment.

RULING CV (bought by this line's own round-27 defect #4): a gate addressed by LINE
NUMBER is silently invalidated by any edit above it.  Round 27's mint gate pinned 5210
and the pin moved when a correction was entered above it -- and the gate kept reporting
PASS over a subtly wrong population.  So NOTHING here is addressed by line number.  The
statement block is located by ITS OWN ADDRESS -- the `G60` registration line -- and
PART 5 demonstrates the difference by inserting lines above the block and showing that
this gate's verdict is unchanged while a line-number-addressed gate's is destroyed.

RULING CG / CP: nothing here probes for absence.  The FULL population of qualifier-shaped
occurrences in the whole draft is enumerated, printed line by line, and classified; the
absence of the r26 form inside the block is then a CONSEQUENCE of a complete census, not
of a probe's silence.

STANDING: a gate returning 0 has said nothing until it has been shown returning 1, in the
same run, on a corrupted copy.  PART 4 corrupts four ways and every one must FIRE.

Usage:  python3 problems/wowii/w133_r28_amend.py
"""
import re
import sys
import unicodedata

DRAFT = "notes/proofs/wowii133_draft.md"

FAIL = []
N = [0]


def check(name, got, want):
    N[0] += 1
    ok = got == want
    print("  [%s] %-70s got=%s want=%s" % ("OK " if ok else "FAIL", name, got, want))
    if not ok:
        FAIL.append((name, got, want))
    return ok


# ---------------------------------------------------------------------------
# The predicates.  Every one of them is fired in PART 0 on an input where it
# MUST return True, because a predicate whose only observed output is False is
# indistinguishable from a predicate that is broken shut.
# ---------------------------------------------------------------------------
ANCHOR_RE = re.compile(r"\*\*`?G60`?\s*\(")          # the statement's OWN address
QUAL_RE = re.compile(r"modulo the §35[–-]§37 enumerations", re.I)

OLD_FORM = "single-source as of r26"
NEW_FRAGS = [
    "modulo the §35–§37 enumerations",
    "two independent implementations agreeing as of r27",
    "still single-author and single-specification",
]


def normalise_block(block_lines):
    """Strip the blockquote markers and reflow to ONE line.

    The qualifier is 130+ characters and must be allowed to wrap; a gate that
    only matches it on a single physical line is a gate that a future rewrap
    silently defeats.  Same species of defect as RULING CV, one level down.
    """
    out = []
    for l in block_lines:
        s = l.lstrip()
        if s.startswith(">"):
            s = s[1:]
        out.append(s.strip())
    return re.sub(r"\s+", " ", " ".join(out))


def find_anchor(lines):
    """Return every line index (0-based) carrying the G60 registration anchor."""
    return [i for i, l in enumerate(lines) if ANCHOR_RE.search(l)]


def statement_block(lines, idx):
    """The blockquote run the registration line opens."""
    blk = []
    j = idx
    while j < len(lines) and lines[j].lstrip().startswith(">"):
        blk.append(lines[j])
        j += 1
    return blk


def has_old_form(text):
    return OLD_FORM in text


def has_all_new_frags(text):
    return all(f in text for f in NEW_FRAGS)


def verdict(lines):
    """The whole gate, as a pure function of a draft's lines, so that it can be
    re-run against corrupted copies inside this same process.  Returns a list of
    the reasons it FAILS; an empty list is a PASS."""
    bad = []
    anch = find_anchor(lines)
    if len(anch) != 1:
        bad.append("anchor count %d != 1" % len(anch))
        return bad
    blk = statement_block(lines, anch[0])
    if len(blk) < 3:
        bad.append("statement block only %d lines" % len(blk))
        return bad
    txt = normalise_block(blk)
    if has_old_form(txt):
        bad.append("SUPERSEDED r26 form is carried INSIDE the statement block")
    if not has_all_new_frags(txt):
        bad.append("amended qualifier fragments missing from the statement block: %s"
                   % [f for f in NEW_FRAGS if f not in txt])
    if txt.count(NEW_FRAGS[1]) < 2:
        bad.append("amended qualifier appears %d time(s) inside the block; the opening "
                   "qualifier AND the malformed-citation clause must both carry it"
                   % txt.count(NEW_FRAGS[1]))
    if "MALFORMED" not in txt:
        bad.append("the malformed-citation clause did not survive the amendment")
    return bad


raw = open(DRAFT, encoding="utf-8").read()
lines = raw.split("\n")
print("draft: %s, %d lines" % (DRAFT, len(lines)))
print("gate is ANCHOR-addressed (RULING CV): no line number is load-bearing anywhere below.")

# ---------------------------------------------------------------------------
print()
print("PART 0. POSITIVE CONTROLS -- every predicate fired where it MUST return True")
# ---------------------------------------------------------------------------
check("ANCHOR_RE fires on a real registration line",
      bool(ANCHOR_RE.search("> **`G60` (Theorem — elementary).**")), True)
check("ANCHOR_RE does NOT fire on prose about the address",
      bool(ANCHOR_RE.search("`G61` is unoccupied.")), False)
check("QUAL_RE fires on the r26 form",
      bool(QUAL_RE.search("modulo the §35–§37 enumerations, single-source as of r26")), True)
check("QUAL_RE fires on the r27 form",
      bool(QUAL_RE.search("modulo the §35–§37 enumerations — two independent implementations")), True)
check("has_old_form fires on the r26 string (MUST be True)",
      has_old_form('*"modulo the §35–§37 enumerations, single-source as of r26"*'), True)
check("has_all_new_frags fires on the r27 string (MUST be True)",
      has_all_new_frags("modulo the §35–§37 enumerations — two independent implementations "
                        "agreeing as of r27, still single-author and single-specification"), True)
check("has_all_new_frags is False on the r26 string (discrimination)",
      has_all_new_frags("modulo the §35–§37 enumerations, single-source as of r26"), False)
_probe = ["> **`G60` (Theorem).**", "> modulo the §35–§37 enumerations — two independent",
          "> implementations agreeing as of r27, still single-author and single-specification."]
check("normalise_block REJOINS a wrapped qualifier (MUST be True)",
      has_all_new_frags(normalise_block(_probe)), True)
check("normalise_block WITHOUT reflow would MISS it (the defect it defends against)",
      has_all_new_frags("\n".join(_probe)), False)

# ---------------------------------------------------------------------------
print()
print("PART 1. THE ANCHOR -- the statement's own address, enumerated not probed")
# ---------------------------------------------------------------------------
anch = find_anchor(lines)
for i in anch:
    print("   G60 registration anchor at line %d: %s" % (i + 1, lines[i].strip()[:110]))
check("exactly one G60 registration anchor in the whole draft", len(anch), 1)
blk = statement_block(lines, anch[0])
print("   statement block = the blockquote run it opens: %d lines, %d chars"
      % (len(blk), len("\n".join(blk))))
check("statement block is a blockquote run of >= 3 lines", len(blk) >= 3, True)
blk_txt = normalise_block(blk)

# ---------------------------------------------------------------------------
print()
print("PART 2. FULL CENSUS of qualifier-shaped occurrences in the WHOLE draft")
print("        (RULING CG/CP -- absence is read off a complete census, never probed)")
# ---------------------------------------------------------------------------
blk_lo, blk_hi = anch[0], anch[0] + len(blk) - 1     # 0-based, inclusive
census = {"r26-OLD/in-block": 0, "r26-OLD/outside": 0,
          "r27-NEW/in-block": 0, "r27-NEW/outside": 0, "UNCLASSIFIED": 0}
# the qualifier wraps, so classify on a 2-line window ending at each hit
for i, l in enumerate(lines):
    if not QUAL_RE.search(l):
        continue
    window = normalise_block([l] + lines[i + 1:i + 3])
    inblk = blk_lo <= i <= blk_hi
    if OLD_FORM in window:
        form = "r26-OLD"
    elif NEW_FRAGS[1] in window:
        form = "r27-NEW"
    else:
        form = "UNCLASSIFIED"
    key = "UNCLASSIFIED" if form == "UNCLASSIFIED" else "%s/%s" % (form, "in-block" if inblk else "outside")
    census[key] += 1
    print("   line %-5d %-8s %-9s %s" % (i + 1, form, "IN-BLOCK" if inblk else "outside",
                                         l.strip()[:96]))
print("   census: %s" % census)
check("r26-OLD occurrences INSIDE the statement block", census["r26-OLD/in-block"], 0)
check("r27-NEW occurrences INSIDE the statement block", census["r27-NEW/in-block"], 2)
check("no qualifier-shaped occurrence is UNCLASSIFIED", census["UNCLASSIFIED"], 0)
print("   (r26-OLD occurrences OUTSIDE the block are HISTORICAL RECORD -- §39 quotes the")
print("    superseded form in order to record what was superseded, which is not a carrier.)")

# ---------------------------------------------------------------------------
print()
print("PART 3. THE AMENDED QUALIFIER IS INSIDE THE STATEMENT, fragment by fragment")
# ---------------------------------------------------------------------------
for f in NEW_FRAGS:
    check("fragment %r inside the statement block" % f[:46], f in blk_txt, True)
check("malformed-citation clause survived the amendment", "MALFORMED" in blk_txt, True)
check("the amended qualifier is carried TWICE (opening + citation clause)",
      blk_txt.count(NEW_FRAGS[1]), 2)
check("NFKC normalisation does not change the verdict (no encoding-invisible text)",
      has_all_new_frags(unicodedata.normalize("NFKC", blk_txt)), True)
print()
print("   THE VERDICT ON THE LIVE DRAFT:")
live = verdict(lines)
print("   verdict(live) = %s" % (live if live else "PASS (no reasons to fail)"))
check("live draft PASSES the amendment gate", live, [])

# ---------------------------------------------------------------------------
print()
print("PART 4. THE GATE MUST FIRE -- four corrupted copies, in this same run")
print("        A gate returning 0 has said nothing until it has been shown returning 1.")
# ---------------------------------------------------------------------------


def corrupt_revert(ls):
    """C1 -- put the SUPERSEDED r26 form back inside the statement block.
    This is the exact defect the round was told not to ship."""
    out = list(ls)
    for i in range(blk_lo, blk_hi + 1):
        if QUAL_RE.search(out[i]):
            out[i] = "> **Modulo the §35–§37 enumerations, single-source as of r26**, the following holds."
            out[i + 1] = ">"
            break
    return out


def corrupt_halfqual(ls):
    """C2 -- a DATE BUMP with the state dropped: 'as of r27' but no
    'still single-author and single-specification'.  cert section 5 calls this
    exact shape a carrier defect: the number looks stronger with no new evidence."""
    out = list(ls)
    for i in range(blk_lo, blk_hi + 1):
        if "still single-author and single-specification" in out[i]:
            out[i] = out[i].replace("still single-author and single-specification", "")
    return out


def corrupt_evict(ls):
    """C3 -- the qualifier is TRUE but has been moved OUT of the statement into
    surrounding prose, which is precisely what cert_w133_r26 section 5 forbade."""
    out = list(ls)
    for i in range(blk_lo, blk_hi + 1):
        if QUAL_RE.search(out[i]):
            out[i] = ">"
    out.insert(blk_hi + 2, "Modulo the §35–§37 enumerations — two independent implementations "
                           "agreeing as of r27, still single-author and single-specification.")
    return out


def corrupt_dupanchor(ls):
    """C4 -- a second G60 registration appears, so 'the' statement block is
    ambiguous and the gate no longer knows which population it is judging."""
    out = list(ls)
    out.insert(blk_lo, "> **`G60` (Theorem — a second, contradictory registration).**")
    return out


def corrupt_stripmalformed(ls):
    """C5 -- the malformed-citation clause is deleted while the qualifier stays.
    The condition would then travel only by convention."""
    out = list(ls)
    for i in range(blk_lo, blk_hi + 1):
        out[i] = out[i].replace("**MALFORMED**", "**fine**")
    return out


for nm, fn, expect_sub in [
    ("C1 r26 form reverted into the block", corrupt_revert, "SUPERSEDED r26 form"),
    ("C2 date bumped, STATE dropped", corrupt_halfqual, "fragments missing"),
    ("C3 qualifier evicted to prose", corrupt_evict, "fragments missing"),
    ("C4 duplicate G60 registration", corrupt_dupanchor, "anchor count"),
    ("C5 malformed-citation clause deleted", corrupt_stripmalformed, "malformed-citation clause"),
]:
    v = verdict(fn(lines))
    print("   %-38s -> %s" % (nm, v if v else "PASS  <-- GATE FAILED TO FIRE"))
    check("gate FIRES on %s" % nm, len(v) > 0, True)
    check("   ...and fires for the RIGHT reason (%r)" % expect_sub,
          any(expect_sub in r for r in v), True)

# ---------------------------------------------------------------------------
print()
print("PART 5. RULING CV DEMONSTRATED -- the anchor survives insertion; a line number does not")
# ---------------------------------------------------------------------------
SHIFT = 40
shifted = ["<inserted line %d>" % k for k in range(SHIFT)] + list(lines)
sh_anch = find_anchor(shifted)
print("   inserted %d lines ABOVE the statement block (round 27's defect, reproduced)" % SHIFT)
print("   anchor line before insertion: %d ; after insertion: %d"
      % (anch[0] + 1, sh_anch[0] + 1 if sh_anch else -1))
check("the anchor MOVED (so the insertion really happened)", sh_anch[0], anch[0] + SHIFT)
check("ANCHOR-addressed verdict is UNCHANGED by the insertion", verdict(shifted), live)

# the same question asked the round-27 way: a hard-pinned line number.
PINNED = anch[0]          # correct before the insertion, silently wrong after
pinned_blk_before = statement_block(lines, PINNED) if ANCHOR_RE.search(lines[PINNED]) else []
pinned_blk_after = statement_block(shifted, PINNED) if ANCHOR_RE.search(shifted[PINNED]) else []
print("   line-number-addressed gate: block found BEFORE insertion = %d lines; AFTER = %d lines"
      % (len(pinned_blk_before), len(pinned_blk_after)))
check("line-number gate WAS correct before the insertion", len(pinned_blk_before) >= 3, True)
check("line-number gate is DESTROYED by the insertion (RULING CV, made visible)",
      len(pinned_blk_after) >= 3, False)
print("   ^ that pair IS ruling CV: same question, same draft, one addressing scheme survives.")

# ---------------------------------------------------------------------------
print()
print("PART 6. What this gate does NOT check -- stated against the round's interest")
print("   * it does NOT check that the amended qualifier is TRUE.  That is cert_w133_r27 §1")
print("     and §5, which certified the agreement and ruled the amendment; this gate checks")
print("     only that the carrier says what the ruling said it may say.")
print("   * it does NOT re-verify the §35–§37 enumerations.  w133_r27_reimpl.out did that.")
print("   * it does NOT bank §27.4's corollary.  Parts (2) and (3) of the corrected")
print("     three-part discharge condition (cert_w133_r27 §4) are both open: (D3-C6) is")
print("     unadopted, and the links are still ONE family until Q41 lands.")

print()
print("checks: %d, failures: %d" % (N[0], len(FAIL)))
for f in FAIL:
    print("   FAIL %s got=%s want=%s" % f)
sys.exit(1 if FAIL else 0)
