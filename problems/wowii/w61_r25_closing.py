#!/usr/bin/env python3
"""owner-w61 round 25 CLOSING GREP -- run AFTER SS7.40 and the three weakenings landed.
RULING S (coverage != liveness): every assertion below is stated with WHAT IT CANNOT SEE.
RULING AS: the population is printed before each verdict.
"""
import pathlib, re, collections, sys
D = pathlib.Path("$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md")
t = D.read_text(); L = t.splitlines()
# line-wrapped prose broke two naive counts on the first run (recorded, not hidden):
# normalise whitespace before counting any multi-word record claim.
flat = re.sub(r"\s+", " ", t)

print("=== POPULATION ===")
heads = [l for l in L if l.startswith("## §7.")]
print(f"  §7.x sections : {len(heads)}   last = {heads[-1][:70]}…")
dupes = [h for h,c in collections.Counter(x.split(":")[0] for x in heads).items() if c > 1]
print(f"  duplicate §7.x addresses : {dupes or 'none'}")
rows = sorted({int(m.group(1)) for l in L for m in [re.match(r"\s*\|\s*R-(\d+)\s*\|", l)] if m})
print(f"  registry ROWS (distinct) : R-{rows[0]}…R-{rows[-1]}, {len(rows)} addresses, gaps={[n for n in range(1,rows[-1]+1) if n not in rows] or 'none'}")
weak = [i+1 for i,l in enumerate(L) if l.startswith("〔**BOUNDED WEAKENING recorded 2026-08-23")]
print(f"  bounded-weakening notes at lines : {weak}")

# the three notes, isolated, so a phrase check reports about THEM and not about
# SS7.40's prose (an unscoped count wanted 4 and said nothing about the notes)
_pre = "\u3014**BOUNDED WEAKENING recorded 2026-08-23"
notes = []
_i = 0
while True:
    _i = t.find(_pre, _i)
    if _i < 0: break
    _j = t.index("\u3015", _i)
    notes.append(re.sub(r"\s+", " ", t[_i:_j]))
    _i = _j

print("\n=== CHECKS (verdicts computed only now) ===")
C = [
 ("§7.40 present exactly once", t.count("## §7.40 owner-w61 round 25:"), 1),
 ("§7.40 is the last section", heads[-1].startswith("## §7.40 owner-w61 round 25:"), True),
 ("no duplicate §7.x address", dupes, []),
 ("registry rows contiguous R-1…R-23", (rows[0], rows[-1], len(rows)), (1, 23, 23)),
 ("three weakening notes, all before §7.40", len(weak) == 3 and max(weak) < t[:].count("\n", 0, t.find("## §7.40"))+1, True),
 ("each weakening names what is NOT weakened", flat.count("**What is NOT weakened:**"), 3),
 # scoped: the phrase also occurs once in SS7.40 (f) quoting RULING BK, so an
 # unscoped count wants 4 and says nothing about the NOTES.  Count inside them.
 ("each weakening note itself says 'not a re-run and not a retraction'",
  sum("not a re-run and not a retraction" in n for n in notes), 3),
 ("R-23's PROVED-S3 status word still present exactly once in its row",
  len([l for l in L if re.match(r"\s*\|\s*R-23\s*\|", l) and "PROVED-S3" in l]), 1),
 ("no promotion language for GFANν-HC", t.count("Corollary GFANν-HC → PROVED-S3"), 0),
 ("the withdrawal outcome is never called a pass",
  bool(re.search(r"withdrawal[^.]{0,80}\bpass(ed)?\b", t.split("## §7.40")[1])), False),
 ("BB2 recorded", t.count("〔**BB2 —"), 1),
 ("BK1..BK7 all present", [t.count(f"**BK{i} ") + t.count(f"**BK{i} —") for i in range(1,8)].count(0), 0),
]
ok = True
for n,g,w in C:
    f = "OK " if g == w else "FAIL"; ok = ok and g == w
    print(f"  [{f}] {n}: {g!r} (want {w!r})")
print("\nWHAT THIS GREP CANNOT SEE (RULING S): it checks structure and record claims only.")
print("  It does not read a single line of mathematics, it cannot tell a true weakening from")
print("  a well-formed false one, and it has no view of the six BRIEF files at all -- the")
print("  audit's findings live there and were adjudicated by hand, not by this script.")
print("\nCLOSING GREP PASS" if ok else "\nCLOSING GREP FAILED")
sys.exit(0 if ok else 1)
