#!/usr/bin/env python3
"""RULING BB, implemented rather than promised: ADDRESS UNIQUENESS ASSERTED AT MINT TIME.

Two lines of this project have now had independent address collisions (w61's `R-22`,
w133's `F6` carrying four meanings), and BOTH were found by an assertion that happened to
run at grep time, long after the collision was written.  An address space without a
uniqueness assertion is a defect generator.

Any script that mints an address into a ledger imports `mint` from here.  It refuses to
return the address if the draft already spends it.  `next_free` is the convenience form:
it returns the lowest unused number in a family, so the caller cannot pick a number at
all.

    from w61_mint import mint, next_free
    row = mint("R", 24)          # raises if R-24 is already spent
    row = next_free("R")         # returns e.g. "R-24", never a collision

WHY IT LIVES HERE AND NOT IN THE LANDING SCRIPT: a check that is re-typed per script is a
check that drifts.  The r23 collision survived because the only guard was a hand-written
grep in one script's closing block.
"""
import pathlib, re

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
DRAFT = ROOT / "notes/proofs/wowii61_draft.md"


def spent(family="R", draft=DRAFT):
    """Every address of `family` already written into the draft, with its line numbers."""
    out = {}
    for i, ln in enumerate(draft.read_text().splitlines(), 1):
        for m in re.finditer(rf"\b{re.escape(family)}-(\d+)\b", ln):
            out.setdefault(int(m.group(1)), []).append(i)
    return out


def mint(family, n, draft=DRAFT):
    """Return f'{family}-{n}', or raise if that address is already spent."""
    s = spent(family, draft)
    if n in s:
        raise AssertionError(
            f"ADDRESS COLLISION AT MINT TIME: {family}-{n} is already spent at "
            f"lines {s[n]}. Pick another; do NOT quietly renumber later.")
    return f"{family}-{n}"


def next_free(family, draft=DRAFT):
    """Lowest unused address in the family -- the caller does not choose a number."""
    s = spent(family, draft)
    n = 1
    while n in s:
        n += 1
    return f"{family}-{n}"


# ---------------------------------------------------------------------------
# owner-w61 round 25 (RULING BL, err noisy): `spent` counts ANY occurrence of the
# address, including a sentence that merely DISCUSSES it.  On this file's second
# outing that bit: SS7.39 (g)'s own self-test sentence -- "lowest free `R-24`" --
# and SS7.40's accounting line made `R-24` look spent, so `next_free` silently
# returned `R-25` and the next real promotion would have left an unexplained hole
# at `R-24`.  `mint()` erring on the noisy side is SAFE (it can only refuse a free
# address, never approve a spent one); `next_free()` skipping silently is NOT.
#
# Split the two notions.  A registry ROW is `| R-n |` at the start of a table line;
# anything else is a MENTION.  `mint`/`next_free` now key on ROWS, and both SHOUT
# about mentions instead of acting on them silently.
# ---------------------------------------------------------------------------

def rows(family="R", draft=DRAFT):
    """Addresses actually MINTED as registry rows (`| R-n |` opening a table line)."""
    out = {}
    for i, ln in enumerate(draft.read_text().splitlines(), 1):
        m = re.match(rf"\s*\|\s*{re.escape(family)}-(\d+)\s*\|", ln)
        if m:
            out.setdefault(int(m.group(1)), []).append(i)
    return out


def mentions_only(family="R", draft=DRAFT):
    """Addresses that appear in prose but were never minted as a row."""
    r, s = rows(family, draft), spent(family, draft)
    return {k: v for k, v in s.items() if k not in r}


def mint_row(family, n, draft=DRAFT):
    """Mint `family-n` as a registry ROW.  Refuses a spent row; SHOUTS on a mention."""
    r = rows(family, draft)
    if n in r:
        raise AssertionError(
            f"ADDRESS COLLISION AT MINT TIME: {family}-{n} is already a registry row at "
            f"lines {r[n]}. Pick another; do NOT quietly renumber later.")
    m = mentions_only(family, draft)
    if n in m:
        print(f"  MINT WARNING: {family}-{n} is not a row, but it is MENTIONED in prose at "
              f"lines {m[n]}. Read those lines before you mint it.")
    return f"{family}-{n}"


def next_free_row(family, draft=DRAFT):
    """Lowest address not yet minted as a ROW, with every mention it steps over named."""
    r = rows(family, draft)
    n = 1
    while n in r:
        n += 1
    m = mentions_only(family, draft)
    if n in m:
        print(f"  NEXT-FREE WARNING: {family}-{n} is free as a row but is MENTIONED at "
              f"lines {m[n]} (prose, not a row). Returning it anyway -- read those lines.")
    return f"{family}-{n}"


if __name__ == "__main__":
    s = spent("R")
    print(f"R-family addresses spent in the draft : {len(s)}")
    print(f"  lowest free : {next_free('R')}")
    dupes = {k: v for k, v in s.items() if len(set(v)) > 1}
    # a row number legitimately recurs (it is cited as well as minted); the mint-time
    # guard is about MINTING, so this listing is informational, not a gate.
    print(f"  R-22 line numbers (the r23 collision, kept visible) : {s.get(22)}")
    print(f"  R-23 line numbers                                   : {s.get(23)}")
    r = rows("R")
    print(f"  R addresses minted as REGISTRY ROWS  : {sorted(r)}")
    print(f"  mentioned in prose but never a row   : {sorted(mentions_only('R'))}")
    print(f"  lowest free ROW                      : {next_free_row('R')}")
    try:
        mint("R", 23)
        print("  SELF-TEST FAIL: minting a spent address was allowed")
    except AssertionError as e:
        print(f"  SELF-TEST PASS: {str(e).splitlines()[0][:90]}...")
