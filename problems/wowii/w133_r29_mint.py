#!/usr/bin/env python3
"""
WOWII-133 round 29 -- MINT GATE for `G61`, the IMPLICATION (D3-C6) => sec 27.4's consequent.

WHAT IS BEING CHECKED.  cert_w133_r28 section 5 ruled that the corollary may NOT be banked and
that the IMPLICATION may.  The two are different objects, and the whole value of the ruling is
that the ledger says which one we have.  So this gate asserts, on the draft's own text:

  (1) the antecedent lives INSIDE the statement block, in the same breath as the number;
  (2) the malformed-citation clause exists and is rejectable;
  (3) the statement is barred from S1 while the condition stands;
  (4) the condition names a STATE ("NOT ADOPTED", with the ledger address) and NOT a date;
  (5) the three NOTs are present and carry the right POLARITY: not the corollary, closes no
      pocket (residual OPEN), discharges no part -- in particular not part (2);
  (6) the registration line's GENUS is "Implication" and is NOT "Corollary" -- the carrier
      defect cert_w133_r28 section 5 says this line has hit FOUR times.

RULING CV.  Nothing here is addressed by a load-bearing line number.  The statement block is
located by ITS OWN ADDRESS -- the unique `G61` registration line.  PART 5 demonstrates the
difference: it inserts 60 lines ABOVE the block and asserts in the same run that the
anchor verdict is UNCHANGED while a line-number-addressed gate asking the same question is
DESTROYED.  The one pinned number in this file (the corpus boundary, RULING BX) is pinned
AFTER this round's in-place corrections and is load-bearing only for the historical question
"was G61 free before this round?", which has no anchor-addressed formulation.

RULING CG / CP.  Nothing probes for absence.  The FULL `G61` population in the whole draft is
enumerated, printed line by line, and classified REGISTRATION / FREE-ADDRESS-PROSE / CITATION /
UNCLASSIFIED, and `0 UNCLASSIFIED` is asserted.

RULING CZ (w61, standing on all lines).  A positive control that injects the CANONICAL form of a
species proves only that the gate sees the easy form.  Every corruption in PART 4 is the HARDEST
form of its species that still leaves the rest of the entry intact -- three of them are the real
historical instances this project has actually shipped.

RULING CY.  Every predicate is fired in PART 0 on an input where it MUST return True, and the
whole verdict is shown PASSING on the real draft -- a check that cannot pass is exactly as
uninformative as one that cannot fail.

Usage:  python3 problems/wowii/w133_r29_mint.py [pinned_boundary_line]
"""
import re
import sys
import collections
import unicodedata

DRAFT = "notes/proofs/wowii133_draft.md"
BOUND = int(sys.argv[1]) if len(sys.argv) > 1 else 5517

FAIL = []
N = [0]


def check(name, got, want):
    N[0] += 1
    ok = got == want
    print("  [%s] %-72s got=%s want=%s" % ("OK " if ok else "FAIL", name, got, want))
    if not ok:
        FAIL.append((name, got, want))
    return ok


# ---------------------------------------------------------------------------
# THE PREDICATES.  Pure functions of a draft's lines so that they can be re-run
# against corrupted copies inside this same process.
# ---------------------------------------------------------------------------
ANCHOR_RE = re.compile(r"\*\*`?G61`?\s*\(")

COND = "conditional on (d3-c6), which is not adopted"
MALFORMED = "is **malformed**, and a guard should reject it"
NO_S1 = "not an s1 candidate"
NOT_COROLLARY = "not §27.4's corollary"
RESIDUAL_OPEN = "case-2 residual remains **open**"
NO_DISCHARGE = "discharges no part"
NOT_PART2 = "in particular not part (2)"
LEDGER_ADDR = "w133_state.md:4463"
DATE_CARRIERS = [" as of r2", " as of r3", " as of 2026"]


def reflow(block_lines):
    """De-quote and reflow to ONE lower-cased line.  The clauses are 100+ chars and
    MUST be allowed to wrap; a gate that only matches on one physical line is a gate
    a future rewrap silently defeats -- RULING CV, one level down."""
    out = []
    for l in block_lines:
        s = l.lstrip()
        if s.startswith(">"):
            s = s[1:]
        out.append(s.strip())
    return re.sub(r"\s+", " ", " ".join(out)).lower()


def find_anchors(lines):
    return [i for i, l in enumerate(lines) if ANCHOR_RE.search(l)]


def statement_block(lines, idx):
    blk = []
    j = idx
    while j < len(lines) and lines[j].lstrip().startswith(">"):
        blk.append(lines[j])
        j += 1
    return blk


def verdict(lines):
    """The whole gate as a pure function.  Returns the list of REASON TAGS on which it
    fails; [] is a PASS.  Reason tags are asserted individually in PART 4, because a gate
    that fails for an unrelated reason is a gate that has not been tested."""
    bad = []
    anch = find_anchors(lines)
    if len(anch) != 1:
        bad.append("ANCHOR-NOT-UNIQUE(%d)" % len(anch))
        return bad
    reg_line = lines[anch[0]]
    blk = statement_block(lines, anch[0])
    if len(blk) < 5:
        bad.append("BLOCK-TOO-SHORT(%d)" % len(blk))
        return bad
    txt = reflow(blk)

    # (6) GENUS: the registration line must name it an IMPLICATION, never a corollary.
    low_reg = reg_line.lower()
    if "implication" not in low_reg:
        bad.append("GENUS-NOT-IMPLICATION")
    if re.search(r"`?g61`?\s*\(\s*corollary", low_reg):
        bad.append("GENUS-IS-COROLLARY")

    # (1) the antecedent INSIDE the block, twice: the opening and the malformed clause.
    n_cond = txt.count(COND)
    if n_cond < 2:
        bad.append("COND-NOT-IN-BLOCK(%d)" % n_cond)

    # (4) STATE, not date.
    if LEDGER_ADDR not in txt:
        bad.append("STATE-HAS-NO-LEDGER-ADDRESS")
    for d in DATE_CARRIERS:
        if d in txt:
            bad.append("DATE-CARRIER-IN-BLOCK(%s)" % d.strip())

    # (2) the malformed-citation clause.
    if MALFORMED not in txt:
        bad.append("MALFORMED-CLAUSE-MISSING")

    # (3) barred from S1.
    if NO_S1 not in txt:
        bad.append("S1-BAR-MISSING")

    # (5) the three NOTs, with POLARITY.
    if NOT_COROLLARY not in txt:
        bad.append("NOT-A-COROLLARY-MISSING")
    if RESIDUAL_OPEN not in txt:
        bad.append("RESIDUAL-NOT-DECLARED-OPEN")
    if "residual remains **closed**" in txt or "closes pocket 1" in txt:
        bad.append("POCKET-DECLARED-CLOSED")
    if NO_DISCHARGE not in txt:
        bad.append("DISCHARGE-DISCLAIMER-MISSING")
    if NOT_PART2 not in txt:
        bad.append("PART2-DISCLAIMER-MISSING")
    if re.search(r"discharges part \(2\)|discharges the second part", txt):
        bad.append("PART2-CLAIMED-DISCHARGED")
    return bad


raw = open(DRAFT, encoding="utf-8").read()
lines = raw.split("\n")
print("draft length now: %d lines; PINNED BOUNDARY = %d" % (len(lines), BOUND))
print()

# ---------------------------------------------------------------------------
# PART 0 -- LIVENESS.  Every predicate fired where it MUST return True (RULING CY).
# ---------------------------------------------------------------------------
print("PART 0 -- LIVENESS: every predicate fired on an input where it MUST return True")
PROBE = [
    "> **`G61` (Implication -- elementary; a conditional TRANSFER, not a closure).**",
    "> **Conditional on (D3-C6), which is NOT ADOPTED** -- `w133_state.md:4463` -- the",
    "> following holds. IF (D3-C6) THEN the residual closes. It is NOT §27.4's corollary.",
    "> pocket 1's `D = 3` Case-2 residual",
    "> remains **OPEN**. It discharges NO part of the condition, and",
    "> in particular not part (2). A citation of `G61` that does not carry",
    "> *\"conditional on (D3-C6), which is not adopted\"* is **MALFORMED**, and a guard",
    "> should reject it. **Not an S1 candidate.**",
]
pv = verdict(PROBE)
print("   probe verdict: %s" % (pv or "PASS",))
check("LIVENESS: the gate CAN PASS (fires clean on a minimal correct probe)", pv, [])
# and the reflow itself is positive-controlled: the clause is WRAPPED in the probe
# (it straddles lines 4-5) and must still be found.
check("LIVENESS: reflow finds a clause that WRAPS across two physical lines",
      RESIDUAL_OPEN in reflow(PROBE), True)
check("LIVENESS: WITHOUT the reflow the same wrapped clause is MISSED",
      any(RESIDUAL_OPEN in l.lower() for l in PROBE), False)
print()

# ---------------------------------------------------------------------------
# PART 1 -- THE ADDRESS POPULATION, enumerated, never probed (RULING CG/CP).
# ---------------------------------------------------------------------------
print("PART 1 -- ADDRESS POPULATION at or before the pinned boundary, enumerated in full")


def population(text_lines, upto):
    occ = collections.defaultdict(list)
    for i, l in enumerate(text_lines[:upto], 1):
        for m in re.finditer(r"\bG(\d{1,3})\b", l):
            occ[int(m.group(1))].append(i)
    return occ


occ_raw = population(lines, BOUND)
occ_nfkc = population(unicodedata.normalize("NFKC", raw).split("\n"), BOUND)
ks = sorted(occ_raw)
print("   raw  : %d distinct addresses, G%d .. G%d" % (len(ks), min(ks), max(ks)))
print("   NFKC : %d distinct addresses" % len(occ_nfkc))
holes = [k for k in range(0, max(ks) + 1) if k not in occ_raw]
print("   HOLES in G0..G%d: %s" % (max(ks), holes))
check("population is CONTIGUOUS G0..G61 (0 holes)", holes, [])
check("distinct addresses at the boundary", len(ks), 62)
check("raw and NFKC populations agree (no encoding-invisible address)",
      sorted(occ_raw) == sorted(occ_nfkc), True)
check("G62 is unoccupied at the boundary", 62 in occ_raw, False)
print()

print("PART 1b -- G61's PRE-BOUNDARY occurrences, printed line by line and classified")
reg_shaped = 0
for ln in occ_raw.get(61, []):
    txt = lines[ln - 1].strip()
    is_reg = bool(ANCHOR_RE.search(txt))
    print("   line %-5d [%s] %s" % (ln, "REGISTRATION" if is_reg else "prose", txt[:140]))
    if is_reg:
        reg_shaped += 1
check("G61 occurrences at or before the boundary", len(occ_raw.get(61, [])), 1)
check("of which REGISTRATION-SHAPED (the address was FREE)", reg_shaped, 0)
# LIVENESS of the registration classifier: fire it on G60's real registration line,
# where the answer MUST be REGISTRATION.
g60_reg = sum(1 for ln in occ_raw.get(60, [])
              if re.search(r"\*\*`?G60`?\s*\(", lines[ln - 1]))
check("classifier FIRES on G60's real registration (positive control)", g60_reg >= 1, True)
print()

# ---------------------------------------------------------------------------
# PART 2 -- THE WHOLE-DRAFT G61 CENSUS, classified, 0 UNCLASSIFIED.
# ---------------------------------------------------------------------------
print("PART 2 -- WHOLE-DRAFT `G61` CENSUS, every occurrence classified by SECTION")
# the mint section is located by its OWN HEADING, not by a line number.
mint_start = [i for i, l in enumerate(lines) if l.startswith("# \u00a740 ")]
check("the mint section heading is unique and locatable by anchor", len(mint_start), 1)
MS = mint_start[0] + 1 if mint_start else 10 ** 9
print("   mint section begins at draft line %s" % MS)


def classify(lines, ln):
    """REGISTRATION / FREE-ADDRESS-PROSE / CITATION-IN-MINT / CITATION-OUTSIDE / UNCLASSIFIED."""
    t = lines[ln - 1]
    if ANCHOR_RE.search(t):
        return "REGISTRATION"
    if ln < MS:
        return "FREE-ADDRESS-PROSE" if "unoccupied" in t.lower() else "UNCLASSIFIED"
    return "CITATION-IN-MINT"


whole = population(lines, len(lines))
cats = collections.Counter()
for ln in sorted(set(whole.get(61, []))):
    c = classify(lines, ln)
    cats[c] += 1
    print("   line %-5d [%-20s] %s" % (ln, c, lines[ln - 1].strip()[:110]))
print("   census: %s" % dict(cats))
check("whole-draft census has 0 UNCLASSIFIED", cats["UNCLASSIFIED"], 0)
check("exactly ONE registration in the whole draft", cats["REGISTRATION"], 1)

# CITATION HYGIENE, the check that will matter from the NEXT round on: every `G61`
# occurrence OUTSIDE the mint section must carry the antecedent token in the same line.
def bare_citations(lines, ms):
    out = []
    for ln in sorted(set(population(lines, len(lines)).get(61, []))):
        if ln < ms or ANCHOR_RE.search(lines[ln - 1]):
            continue
    return out


def bare_outside(lines, ms):
    """G61 cited OUTSIDE the mint section without the antecedent on the same line."""
    out = []
    for ln in sorted(set(population(lines, len(lines)).get(61, []))):
        t = lines[ln - 1]
        if ln >= ms or ANCHOR_RE.search(t):
            continue
        if "unoccupied" in t.lower():
            continue
        if "(D3-C6)" not in t:
            out.append(ln)
    return out


bo = bare_outside(lines, MS)
print("   bare G61 citations outside the mint section: %s" % bo)
check("0 bare `G61` citations outside the mint section", bo, [])
# POSITIVE CONTROL (RULING CY/CZ): the hygiene check MUST be able to say YES.  Inject the
# HARDEST form -- a citation that looks fully qualified because the antecedent appears on
# the PREVIOUS line, which is exactly how a real malformed citation gets written.
probe = list(lines)
probe.insert(10, "and (D3-C6) is discussed above, so")
probe.insert(11, "by `G61` the pocket-1 residual closes.")
bo2 = bare_outside(probe, MS + 2)
print("   positive control -- injected bare citation at line 12: %s" % bo2)
check("hygiene check FIRES on an injected bare citation (hardest form)", bo2, [12])
print()

# ---------------------------------------------------------------------------
# PART 3 -- THE STATEMENT BLOCK ITSELF.
# ---------------------------------------------------------------------------
print("PART 3 -- THE STATEMENT BLOCK, located by its OWN ADDRESS (no line number)")
anch = find_anchors(lines)
print("   anchors found at draft lines: %s" % [a + 1 for a in anch])
check("exactly one G61 registration anchor", len(anch), 1)
blk = statement_block(lines, anch[0])
print("   statement block: %d lines, %d chars reflowed" % (len(blk), len(reflow(blk))))
v = verdict(lines)
print("   verdict on the real draft: %s" % (v or "PASS",))
check("the real draft PASSES the whole gate", v, [])
print()

# ---------------------------------------------------------------------------
# PART 4 -- CORRUPTIONS.  RULING CZ: the HARDEST form of each species, and three of
# them are the real historical instances this project has shipped.
# ---------------------------------------------------------------------------
print("PART 4 -- CORRUPTIONS: hardest form of each species (RULING CZ), each asserted")
print("          to FIRE and to fire FOR THE RIGHT REASON")


def corrupt(fn, name, expect_tag, note):
    c = list(lines)
    c = fn(c)
    bad = verdict(c)
    print("   %-6s %s" % (name, note))
    print("          -> %s" % (bad or "PASS (!!)",))
    check("%s FIRES" % name, len(bad) > 0, True)
    check("%s fires for the RIGHT REASON (%s)" % (name, expect_tag),
          any(b.startswith(expect_tag) for b in bad), True)


def x1(c):
    """THE REAL HISTORICAL INSTANCE, four times over: the address carries the
    CONSEQUENT's genus.  Hardest form -- every disclaimer in the entry survives
    verbatim, so every prose-level and whole-document check still passes; only the
    genus of the registration line itself is wrong."""
    i = find_anchors(c)[0]
    c[i] = c[i].replace("(Implication —", "(Corollary —")
    return c


def x2(c):
    """r28's C2 in its hardest form: the condition SURVIVES and is true-looking, but
    it carries a DATE instead of the STATE.  A naive "is the condition present?"
    check passes -- 'Conditional on (D3-C6)' is right there."""
    i = find_anchors(c)[0]
    for j in range(i, min(i + 40, len(c))):
        if "which is NOT ADOPTED" in c[j]:
            c[j] = c[j].replace("which is NOT ADOPTED", "as of r29")
            c[j] = c[j].replace("`w133_state.md:4463`; its", "its")
            break
    return c


def x3(c):
    """r28's C3 in its hardest form: the antecedent is EVICTED from the block into the
    paragraph immediately above it.  A whole-document grep still finds the clause, in
    the right section, one line away.  Only the BLOCK-SCOPED check can fire."""
    i = find_anchors(c)[0]
    for j in range(i, min(i + 40, len(c))):
        if "Conditional on (D3-C6), which is NOT ADOPTED" in c[j]:
            c[j] = "> **Unconditionally**, the following implication holds:"
            break
    c.insert(i, "Conditional on (D3-C6), which is not adopted, we record:")
    return c


def x4(c):
    """A single NOT flipped in POLARITY while its headline token survives.  'closes NO
    pocket' stays on the page word for word; the residual is silently declared CLOSED.
    Hardest: locally token-identical, globally self-contradictory."""
    i = find_anchors(c)[0]
    for j in range(i, min(i + 40, len(c))):
        if "Case-2 residual remains **OPEN**" in c[j]:
            c[j] = c[j].replace("Case-2 residual remains **OPEN**",
                                "Case-2 residual remains **CLOSED**")
            break
    return c


def x5(c):
    """The planner's precisely forbidden claim: part (2) declared discharged, with the
    surrounding disclaimer sentence left standing so the paragraph still reads as a
    disclaimer."""
    i = find_anchors(c)[0]
    for j in range(i, min(i + 40, len(c))):
        if "discharges NO part" in c[j]:
            c[j] = c[j].replace("discharges NO part", "discharges part (2) and no other part")
            break
    return c


def x6(c):
    """A DUPLICATE registration -- and the duplicate is a CORRECT copy placed later, so
    every content check passes on it.  Only anchor UNIQUENESS can fire.  'The' statement
    block is then ambiguous and the gate is reading one of two."""
    i = find_anchors(c)[0]
    c = c + ["", "> **`G61` (Implication — elementary; a conditional TRANSFER, not a closure).**"] \
        + statement_block(c, i)[1:]
    return c


def x7(c):
    """The malformed-citation clause deleted while the condition itself stays -- the
    statement still LOOKS conditional, but nothing declares an unqualified citation
    rejectable, which is the only part of the pattern a citer ever hits."""
    i = find_anchors(c)[0]
    for j in range(i, min(i + 40, len(c))):
        if "is **MALFORMED**, and a guard should reject it" in c[j]:
            c[j] = c[j].replace("is **MALFORMED**, and a guard should reject it",
                                "is discouraged")
            break
    return c


corrupt(x1, "X1", "GENUS-IS-COROLLARY",
        "THE REAL HISTORICAL INSTANCE: genus flipped to Corollary, all disclaimers intact")
corrupt(x2, "X2", "DATE-CARRIER-IN-BLOCK",
        "r28's C2, hardest: condition survives but carries a DATE, state dropped")
corrupt(x3, "X3", "COND-NOT-IN-BLOCK",
        "r28's C3, hardest: antecedent evicted into the line immediately ABOVE the block")
corrupt(x4, "X4", "POCKET-DECLARED-CLOSED",
        "polarity flip: 'closes NO pocket' survives, residual silently CLOSED")
corrupt(x5, "X5", "PART2-CLAIMED-DISCHARGED",
        "the forbidden claim: part (2) declared discharged inside the disclaimer")
corrupt(x6, "X6", "ANCHOR-NOT-UNIQUE",
        "duplicate registration, and the duplicate is a CORRECT copy")
corrupt(x7, "X7", "MALFORMED-CLAUSE-MISSING",
        "malformed-citation clause deleted, condition left standing")
print()

# ---------------------------------------------------------------------------
# PART 5 -- RULING CV, DEMONSTRATED rather than obeyed.
# ---------------------------------------------------------------------------
print("PART 5 -- RULING CV DEMONSTRATED: 60 lines inserted ABOVE the statement block")
i = find_anchors(lines)[0]
shifted = lines[:i - 5] + ["<!-- CV probe line -->"] * 60 + lines[i - 5:]
print("   anchor moved: draft line %d -> %d" % (i + 1, find_anchors(shifted)[0] + 1))
check("ANCHOR-addressed verdict is UNCHANGED under a 60-line insertion above",
      verdict(shifted), verdict(lines))
# the line-number-addressed gate answering the SAME question, destroyed:
PIN = i  # 0-based index of the anchor in the UNCORRUPTED draft
before = len(statement_block(lines, PIN))
after = len(statement_block(shifted, PIN))
print("   line-number-addressed block length: %d -> %d" % (before, after))
check("the LINE-NUMBER-addressed gate is DESTROYED by the same insertion",
      after != before, True)
check("   ... and it is destroyed to ZERO, i.e. it would read an EMPTY statement",
      after, 0)
print()

print("checks: %d, failures: %d" % (N[0], len(FAIL)))
for f in FAIL:
    print("   FAIL %s got=%s want=%s" % f)
sys.exit(1 if FAIL else 0)
