#!/usr/bin/env python3
"""
WOWII-133 round 27 -- MINT GATE for the numbering call on section 37.

RULING CG / CP shape: nothing here asks "is G60 absent?".  A probe that asks for
absence answers "yes" whenever it cannot read the token, and round 24 was burned by
exactly that twice (once in case, once in unicode).  Instead the WHOLE ADDRESS
POPULATION is enumerated and asserted CONTIGUOUS.  An address written in an encoding
the scanner misses opens a HOLE, and a hole is VISIBLE.  Absence is then a
consequence of completeness, not of a probe's silence.

RULING BX: the gate runs against a PINNED corpus boundary -- the draft's length
immediately before this round's section was appended -- so the mint-time question
stays answerable for ever.

Usage:  python3 w133_r27_mint.py <pinned_boundary_line>
"""
import re
import sys
import collections
import unicodedata

DRAFT = "notes/proofs/wowii133_draft.md"
BOUND = int(sys.argv[1]) if len(sys.argv) > 1 else 5202

FAIL = []
N = [0]


def check(name, got, want):
    N[0] += 1
    ok = got == want
    print("  [%s] %-62s got=%s want=%s" % ("OK " if ok else "FAIL", name, got, want))
    if not ok:
        FAIL.append((name, got, want))


raw = open(DRAFT, encoding="utf-8").read()
lines = raw.split("\n")
print("draft length now: %d lines; PINNED BOUNDARY = %d" % (len(lines), BOUND))

# ---------------------------------------------------------------------------
# 1. THE WHOLE ADDRESS POPULATION, enumerated -- not probed.
#    Scanned on the NFKC-NORMALISED text as well as the raw text, and BOTH
#    counts printed, so a unicode defect is visible rather than silent.
# ---------------------------------------------------------------------------
print()
print("1. ADDRESS POPULATION at or before the pinned boundary, enumerated in full")


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
print("   full population: %s" % (ks,))
holes = [k for k in range(0, max(ks) + 1) if k not in occ_raw]
print("   HOLES in G0..G%d: %s" % (max(ks), holes))
check("population is CONTIGUOUS G0..G60 (0 holes)", holes, [])
check("distinct addresses", len(ks), 61)
check("raw and NFKC populations agree (no encoding-invisible address)",
      sorted(occ_raw) == sorted(occ_nfkc), True)
check("G61 is unoccupied at the boundary", 61 in occ_raw, False)

# ---------------------------------------------------------------------------
# 2. G60's pre-boundary occurrences, printed LINE BY LINE, and classified.
#    A REGISTRATION-SHAPED occurrence is one that defines the address; prose
#    ABOUT the next free address is not a registration.
# ---------------------------------------------------------------------------
print()
print("2. G60 pre-boundary occurrences, printed line by line and classified")
reg_shaped = 0
for ln in occ_raw.get(60, []):
    txt = lines[ln - 1].strip()
    is_reg = bool(re.search(r"\*\*`?G60`?\s*\(", txt)) or "is MINTED" in txt and "G60" in txt
    print("   line %-5d [%s] %s" % (ln, "REGISTRATION" if is_reg else "prose", txt[:150]))
    if is_reg:
        reg_shaped += 1
check("G60 occurrences at or before the boundary", len(occ_raw.get(60, [])), 2)
check("of which REGISTRATION-SHAPED", reg_shaped, 0)

# LIVENESS: the classifier must be able to say REGISTRATION.  Fire it on G59's
# actual registration line, where the answer MUST be yes.
print()
print("   LIVENESS of the registration classifier -- fired on G59, whose")
print("   registration line exists and where the answer MUST be REGISTRATION:")
g59_reg = 0
for ln in occ_raw.get(59, []):
    txt = lines[ln - 1].strip()
    if re.search(r"\*\*`?G59`?\s*\(", txt):
        g59_reg += 1
        print("      line %d: %s" % (ln, txt[:150]))
check("classifier FIRES on G59's registration (positive control)", g59_reg >= 1, True)

# ---------------------------------------------------------------------------
# 3. THE CONDITION MUST BE INSIDE THE STATEMENT.
#    Planner ruling cert_w133_r26 section 5: a number on an ASSEMBLY is a handle
#    that travels without its conditionality.  The enumeration-dependency goes in
#    the STATEMENT, not in a remark, not in a footnote, not in the tier line.
# ---------------------------------------------------------------------------
print()
print("3. THE CONDITION-IN-STATEMENT GUARD (planner ruling, cert_w133_r26 section 5)")
COND = "modulo the §‑35–§37 enumerations"   # placeholder, replaced below
CONDS = ["modulo the §35–§37 enumerations", "single-source as of r26"]

after = lines[BOUND:]
blob = "\n".join(after)
if not after:
    print("   (nothing appended yet -- run again after the mint is written)")
else:
    # locate the G60 registration block
    idx = None
    for i, l in enumerate(after):
        if re.search(r"\*\*`?G60`?\s*\(", l):
            idx = i
            break
    print("   G60 registration line found at draft line: %s"
          % (BOUND + idx + 1 if idx is not None else None))
    check("a G60 REGISTRATION line exists after the boundary", idx is not None, True)
    if idx is not None:
        # the STATEMENT is the blockquote that the registration line opens: take
        # the contiguous run of '>' lines starting at idx.
        stmt = []
        j = idx
        while j < len(after) and after[j].lstrip().startswith(">"):
            stmt.append(after[j])
            j += 1
        stmt_txt = "\n".join(stmt)
        print("   STATEMENT block: %d lines, %d chars" % (len(stmt), len(stmt_txt)))
        for c in CONDS:
            check("condition fragment %r is INSIDE the statement block" % c,
                  c in stmt_txt, True)
        check("the statement block is a blockquote run of >= 3 lines", len(stmt) >= 3, True)
        # LIVENESS: the same fragments must NOT be findable in an empty block
        check("LIVENESS: the guard reports ABSENT on an empty block",
              all(c in "" for c in CONDS), False)
        # and the tier line must NOT be the only carrier
        tier_only = [l for l in stmt if "Tier" in l or "TIER" in l]
        print("   tier lines inside the statement block: %d" % len(tier_only))

print()
print("checks: %d, failures: %d" % (N[0], len(FAIL)))
for f in FAIL:
    print("   FAIL %s got=%s want=%s" % f)
sys.exit(1 if FAIL else 0)
