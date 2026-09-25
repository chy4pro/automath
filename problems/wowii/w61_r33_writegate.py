#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r33 WRITE-TIME gate on §7.48.  Gates carry the RULING CZ repairs:
  L1  private local-part, CONSTRUCTED from parts, tolerant of interposed emphasis.
  G2  no UNRETRACTED AH3 closure carrier (r32's AK1-repaired pattern).
  G4' key shape, REPAIRED this round to match sk-ant-… and sk-or-… .
Each shown firing on a corrupted copy in the same run, with the corruption being the
REAL instance (CZ), not a canonical one.  Population printed before verdict."""
import re, sys
D = '$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md'
LOCAL = "chen" + "haoyu" + "1995"
LOOSE = re.compile(r"chen[\W_]{0,4}haoyu[\W_]{0,4}1995", re.I)   # CZ: emphasis-tolerant
MARK = "<!-- RETRACTED-QUOTE -->"
G2 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                r"only thing (?:standing )?between|唯一残余|只差一个族轮", re.I)
G4 = re.compile(r"sk-(?:[A-Za-z0-9]+-){0,3}[A-Za-z0-9]{8,}")     # CZ-REPAIRED
sec = open(D, encoding='utf-8').read()
sec = sec[sec.index('## §7.48'):]
print("=== w61 r33 write gate on §7.48 (population BEFORE verdict) ===")
print("  §7.48 chars %d, lines %d" % (len(sec), sec.count("\n")))
bad = 0
n1 = len(LOOSE.findall(sec)); print("  L1 private local-part (loose)   %d" % n1); bad += n1
raw = [(i, l) for i, l in enumerate(sec.split("\n"), 1) if G2.search(l)]
car = [h for h in raw if MARK not in h[1]]
print("  G2 raw=%d marked=%d CARRIERS=%d" % (len(raw), len(raw) - len(car), len(car)))
for i, l in car: print("      +%-4d CARRIER %r" % (i, l.strip()[:90]))
bad += len(car)
n4 = len(G4.findall(sec)); print("  G4' key shape                   %d" % n4); bad += n4
print("  POSITIVE CONTROLS, corrupted copy, SAME RUN -- REAL instances (RULING CZ):")
c1 = "chen" + "**" + "haoyu" + "**" + "1995"                      # emphasis interposed
c2 = "this is the round that closes WOWII-61's S3 surface"        # AK1's real instance
c3 = "sk-ant-api03-" + "X" * 12                                   # real vendor prefix
c4 = "sk-or-v1-" + "X" * 16                                       # this line's channel
f = [bool(LOOSE.search(sec + c1)) and not bool(LOOSE.search(sec)),
     bool(G2.search(c2)) and MARK not in c2,   # pure control: the REAL instance fires bare
     bool(G4.search(sec + " " + c3)), bool(G4.search(sec + " " + c4))]
print("      L1(emphasis)=%s  G2(possessive)=%s  G4'(sk-ant)=%s  G4'(sk-or)=%s" % tuple(f))
if not all(f):
    print("A GATE COULD NOT BE SHOWN FIRING ON ITS REAL INSTANCE -- refusing to certify"); sys.exit(2)
print("  NOTE, declared not hidden: §7.48 PRINTS the held-out key values. That is")
print("  correct here -- the key file is repo-internal and the null cannot be reported")
print("  without them -- but it means §7.48 MUST NEVER be pasted into a brief.")
print("VERDICT:", "CLEAN" if bad == 0 else "DIRTY bad=%d" % bad)
sys.exit(0 if bad == 0 else 2)
