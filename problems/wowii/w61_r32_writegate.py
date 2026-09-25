#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 round 32 — WRITE-TIME gate on the new draft section §7.47.

Three gates, each shown FIRING on a corrupted copy in the same run:
  L1  the private email must not appear.  The local-part is CONSTRUCTED FROM PARTS
      and never written down in this file -- round 31's own defect was a leak gate
      whose regex contained the secret it was written to catch.
  L2  no held-out answer may stand beside its own row's object.
  G2  no unretracted AH3 closure carrier (RULING CW: the marker exempts ONE line).
Population is printed before the verdict.  Self-limits with sys.exit, never return.
"""
import re, sys

DRAFT = '$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md'
KEYF = '$HOME/workspace/claudecode/automath/problems/wowii/w61_r31_heldout_key.txt'
LOCAL = "chen" + "haoyu" + "1995"          # never written whole, in this file or any artifact
DOM = "gmail" + "." + "com"
MARK = "<!-- RETRACTED-QUOTE -->"
G2 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                r"only thing (?:standing )?between|唯一残余|只差一个族轮", re.I)

sec = open(DRAFT, encoding='utf-8').read()
sec = sec[sec.index('## §7.47'):]
vals = {m.group(1): m.group(2)
        for m in re.finditer(r'([AB][123])\s*=\s*(-?\d+)', open(KEYF, encoding='utf-8').read())}

print("=== w61 r32 write gate on §7.47 (population BEFORE verdict) ===")
print("§7.47 chars", len(sec))
bad = 0
for name, s in (("private local-part", LOCAL), ("private email", LOCAL + "@" + DOM)):
    n = sec.count(s); print("  L1 %-22s %d" % (name, n)); bad += (n > 0)
for row, v in sorted(vals.items()):
    h = re.findall(r'`?%s`?[^\n]{0,40}\b%s\b' % (row, v), sec)
    print("  L2 key-beside-row %-3s %d" % (row, len(h))); bad += len(h)
raw = [(i, m.group(0), MARK in l)
       for i, l in enumerate(sec.split("\n"), 1) for m in G2.finditer(l)]
car = [h for h in raw if not h[2]]
print("  G2 raw=%d  marked-retraction=%d  CARRIERS=%d" % (len(raw), len(raw) - len(car), len(car)))
for i, t, r in raw:
    print("      +%-4d %-11s %r" % (i, "RETRACTION" if r else "CARRIER", t))
bad += len(car)

cor = sec + "\nmail " + LOCAL + "@" + DOM + "\n| `A1` value " + vals["A1"] + \
      " |\nthis closes WOWII-61's S3 surface\n"
f1 = cor.count(LOCAL) > 0
f2 = bool(re.search(r'`?A1`?[^\n]{0,40}\b%s\b' % vals["A1"], cor))
f3 = any(G2.search(l) and MARK not in l for l in cor.split("\n"))
print("  POSITIVE CONTROLS, corrupted copy, SAME RUN: L1=%s L2=%s G2=%s" % (f1, f2, f3))
if not (f1 and f2 and f3):
    print("A GATE COULD NOT BE SHOWN FIRING -- refusing to certify"); sys.exit(2)
print("VERDICT:", "CLEAN" if bad == 0 else "DIRTY bad=%d" % bad)
sys.exit(0 if bad == 0 else 2)
