#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61_r33_g2_adjudicate.py -- item 4: adjudicate every unmarked G2 occurrence BY READING,
then apply <!-- RETRACTED-QUOTE --> only where the occurrence is genuinely a retraction.

"A phrase-hunting detector cannot close a class."  Every line below was READ; the
classification is a human judgement recorded here, and the script only EXECUTES it.

POSITIVE CONTROL (RULING CW + CZ): after marking, the same G2 pattern must STILL FIRE
on each marked string with the marker stripped -- otherwise the marker, not the repair,
is doing the work.  Self-limits with sys.exit, never `return`.
"""
import re, sys
from pathlib import Path

DRAFT = Path("$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md")
MARK = "<!-- RETRACTED-QUOTE -->"
G2 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                r"only thing (?:standing )?between|唯一残余|只差一个族轮", re.I)

# ---- the adjudication, by reading.  key = anchor substring, unique in the draft. ----
RETRACTION = [   # the false form QUOTED inside a repair/ruling record
 '(RULING CT, *"that is the round that closes the S3 surface"*). Every site is repaired',
 '> entire S3 surface of WOWII-61 closes"*.〕',
 'round 30 — this line read *"closes the S3 surface of WOWII-61"*, contradicted by the',
 'between WOWII-61 and a closed S3 surface"* — was **missed by D-CLOSE** because the claim',
 '*"**the entire S3 surface of WOWII-61 closes**"*. **The hedge and its contradiction sit',
 '| 2 | §7.28 (c) heading | *"the one re-round that closes WOWII-61\'s S3 surface"* |',
 '| 3 | §7.28 (c) gate | *"the entire S3 surface of WOWII-61 closes"* |',
 '| 4 | §7.30 (o) heading | *"the one round that closes WOWII-61\'s S3 surface"* |',
 '| 6 | §7.31 (h) | *"This is the round that closes WOWII-61\'s S3 surface"* |',
 '| 7 | §7.32 (j) | *"The round that closes WOWII-61\'s S3 surface"* |',
]
NEGATION_FP = [  # detector fires; the sentence asserts the OPPOSITE.  No marker: the
 '**So the S3 surface does NOT close this cycle.**',   # claim is TRUE as written.
 '> S3 surface does NOT close**: the five §7.25 statements stand at `0` S3 rounds and',
 '1. **Neither candidate closes WOWII-61\'s S3 surface.** Under (b)\'s corrected arithmetic,',
]
CORRECT_SCOPED = [  # says "the GFAN family's surface", which is TRUE.  No marker.
 "### (c) **TOP RESUME POINTER — the one re-round that closes the GFAN family's S3 surface**",
 "> family's S3 surface closes down to one round**",
 "### (o) **TOP RESUME POINTER — the one round that closes the GFAN family's S3 surface**",
 "family 2. This is the round that closes the GFAN family's S3 surface**",
 "1. **Corollary GFANν-HC needs family 2, and it is the only thing between the GFAN family",
]
DETECTOR_SPEC = [  # the line DESCRIBES the pattern; it makes no claim.  No marker.
 '| **G2** | the AH3 closure over-claim, EN **and** ZH',
]
# ---- LIVE CARRIERS found by READING that the AH3 12-site sweep and AK1 both MISSED ----
REPAIR = [
 ("ox-alpha never counts. If all land clean the entire S3 surface of WOWII-61 closes.",
  "ox-alpha never counts. If all land clean the **GFAN family's** S3 surface closes 〔**AH3\n"
  "class, LANDED round 33 — site 13.** This read *\"the entire S3 surface of WOWII-61\n"
  "closes\"*; the §7.25 family was never in this gate arithmetic and stood at `0` rounds\n"
  "throughout. Found by READING the G2 suspect list, not by the detector, which scores\n"
  "this line the same as a correctly-scoped one〕."),
 ("### (a) **What this round is, and what it is the only thing between**",
  "### (a) **What this round is, and what it is the only thing between** 〔**AH3 class,\n"
  "LANDED round 33 — site 14**: the object of *\"between\"* is supplied below and was\n"
  "WOWII-61's whole surface; it is the **GFAN family's**〕"),
 ("and it is now the only statement standing between WOWII-61 and a closed S3 surface.",
  "and it is now the only statement standing between the **GFAN family** and a closed S3\n"
  "surface 〔**AH3 class, LANDED round 33 — site 15.** This read *\"between WOWII-61 and a\n"
  "closed S3 surface\"*. **AH3's sweep missed it because it says \"only statement standing\n"
  "between\", not \"only thing between\"** — the interposition species of RULING CZ, one\n"
  "scale down, inside the very class AH3 exists to close〕."),
]

t = DRAFT.read_text(encoding="utf-8")
orig = t
print("=" * 84)
print("ITEM 4 -- G2 suspects adjudicated BY READING (population before verdict)")
print("=" * 84)
lines = t.split("\n")
suspects = [(i, l) for i, l in enumerate(lines, 1) if G2.search(l)]
unmarked = [(i, l) for i, l in suspects if MARK not in l]
print("  draft lines matching G2 : %d   already marked : %d   to adjudicate : %d"
      % (len(suspects), len(suspects) - len(unmarked), len(unmarked)))

FAIL = []
def find_one(anchor):
    n = t.count(anchor)
    if n != 1:
        FAIL.append("anchor not unique (%d): %r" % (n, anchor[:70])); return False
    return True

print()
print("  CLASS A -- QUOTED RETRACTION (marker applied):")
for a in RETRACTION:
    if not find_one(a): continue
    assert G2.search(a), "anchor does not even match G2: %r" % a[:60]
    t = t.replace(a, a + " " + MARK, 1)
    print("     marked  %s" % a[:88])
print()
print("  CLASS B -- NEGATION FALSE POSITIVE (no marker; the sentence is TRUE):")
for a in NEGATION_FP:
    find_one(a); print("     kept    %s" % a[:88])
print()
print("  CLASS C -- CORRECTLY SCOPED to the GFAN family (no marker; the claim is TRUE):")
for a in CORRECT_SCOPED:
    find_one(a); print("     kept    %s" % a[:88])
print()
print("  CLASS D -- DETECTOR SPEC, makes no claim (no marker):")
for a in DETECTOR_SPEC:
    find_one(a); print("     kept    %s" % a[:88])
print()
print("  CLASS E -- LIVE CARRIER, REPAIRED (the detector could not tell these from C):")
for a, b in REPAIR:
    if not find_one(a): continue
    t = t.replace(a, b, 1)
    print("     REPAIRED %s" % a[:87])

print()
print("=" * 84)
print("POSITIVE CONTROL -- the marker must not be doing the detector's work")
print("=" * 84)
ok = True
for a in RETRACTION:
    fires_bare = bool(G2.search(a))
    fires_marked = any(G2.search(l) and MARK not in l for l in (a + " " + MARK).split("\n"))
    print("     %-70s bare=%s  suppressed-by-marker=%s"
          % (a[:70], fires_bare, not fires_marked))
    ok = ok and fires_bare and not fires_marked
print("     ALL retraction strings fire WITHOUT the marker and are exempted WITH it: %s" % ok)
if not ok: FAIL.append("marker positive control failed")

if FAIL:
    print("\n!! %d failure(s), NOTHING WRITTEN: %s" % (len(FAIL), FAIL)); sys.exit(2)
DRAFT.write_text(t, encoding="utf-8")
print("\n  draft rewritten: %d -> %d chars" % (len(orig), len(t)))

lines2 = t.split("\n")
s2 = [(i, l) for i, l in enumerate(lines2, 1) if G2.search(l)]
u2 = [(i, l) for i, l in s2 if MARK not in l]
print("  AFTER: G2 matches %d ; unmarked %d" % (len(s2), len(u2)))
print("  remaining unmarked, each adjudicated above as B / C / D:")
for i, l in u2:
    print("     %5d  %s" % (i, l.strip()[:96]))
sys.exit(0)
