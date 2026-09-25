#!/usr/bin/env python3
"""owner-w61 round 25, second landing: the RULING BB mint's own second-outing defect.

Found the way the first one was: by PRINTING THE ADDRESS SPACE BEFORE WRITING (RULING AS).
The listing said `R-24` was spent when no such registry row exists -- SS7.39 (g)'s own
self-test sentence and SS7.40's accounting line are prose MENTIONS, and `spent()` counts
any occurrence.  Fixed in `w61_mint.py` by splitting ROW from MENTION; recorded here.
"""
import hashlib, pathlib, sys
ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
D = ROOT / "notes/proofs/wowii61_draft.md"
src = D.read_text(); pre = hashlib.md5(src.encode()).hexdigest(); out = src

old_acct = ("| promotions | **none.** `w61_mint.py` re-run: `R`-family lowest free is "
            "**`R-24`**, and **no address was minted this round** |")
new_acct = ("| promotions | **none**, and **no address was minted this round**. "
            "`w61_mint.py` re-run before the write: `23` registry ROWS spent (`R-1`…`R-23`), "
            "lowest free row **`R-24`** — see 〔**BB2**〕 for what that listing caught |")
assert out.count(old_acct) == 1
out = out.replace(old_acct, new_acct)

bb2 = """〔**BB2 — the RULING BB mint, on ITS second outing, was mis-reporting its own address space,
and the same discipline caught it.** Printing the listing before writing anything showed
`R`-family addresses spent `[1 … 24]` — but **there is no registry row `R-24`.** `spent()` is a
plain regex over the whole draft, so it counts a sentence that merely *discusses* an address:
§7.39 (g)'s own self-test line (*"lowest free `R-24`"*) and this section's first draft of the
accounting line below. **The consequence is asymmetric, and that asymmetry is the whole point of
RULING BL.** `mint()` erring this way is **noisy-and-safe** — it can only refuse an address that
is free, never approve one that is taken. `next_free()` erring this way is **silent**: it would
have returned `R-25` for the next real promotion and left an unexplained hole at `R-24`, and
nobody would have seen a warning. **Fixed at the root rather than worked around:** `w61_mint.py`
now distinguishes a **ROW** (`| R-n |` opening a table line) from a **MENTION**, `mint_row` /
`next_free_row` key on rows, and **both print a loud WARNING naming the line numbers of any
mention they step over** rather than acting on it quietly. Self-test on the live draft: rows
`R-1…R-23`, mentioned-but-never-a-row `[24]`, lowest free row `R-24` **with the warning printed**.
**Third time on this line that the address layer has produced a defect, and the third time the
thing that caught it was printing the population before the verdict** (RULING AS).〕

"""
anchor = "### (i) **Round accounting**"
assert out.count(anchor) == 1
out = out.replace(anchor, bb2 + anchor)
D.write_text(out)
print(f"draft md5 {pre} -> {hashlib.md5(out.encode()).hexdigest()}")

t = D.read_text()
checks = [
 ("BB2 recorded exactly once", t.count("〔**BB2 —"), 1),
 ("stale R-24 'lowest free' accounting claim gone", t.count("lowest free is **`R-24`**"), 0),
 ("corrected accounting present", t.count("`23` registry ROWS spent (`R-1`…`R-23`)"), 1),
 ("noisy-vs-silent named at the defect", t.count("`mint()` erring this way is **noisy-and-safe**"), 1),
 ("SS7.40 still the last section", t.rfind("## §7.4") == t.rfind("## §7.40 owner-w61 round 25:"), True),
 ("three bounded weakenings still present", t.count("**BOUNDED WEAKENING recorded 2026-08-23"), 3),
]
ok = True
for n,g,w in checks:
    f = "OK " if g==w else "FAIL"; ok = ok and g==w
    print(f"  [{f}] {n}: {g} (want {w})")
print("ALL RECORD ASSERTIONS PASS" if ok else "RECORD ASSERTIONS FAILED")
sys.exit(0 if ok else 1)
