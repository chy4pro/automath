#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61_r33_g2_adjudicate pass 2 -- the retraction rows pass 1 under-listed, plus the
quoted false forms inside round 33's OWN repair brackets.  Same positive control."""
import re, sys
from pathlib import Path
DRAFT = Path("$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md")
MARK = "<!-- RETRACTED-QUOTE -->"
G2 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                r"only thing (?:standing )?between|唯一残余|只差一个族轮", re.I)
RETRACTION = [
 '| 5 | §7.31 (g)3 | *"Family 2 for GFANν … closes the S3 surface of WOWII-61"*',
 '| 8 | §7.38 (g)1 | *"it is now **the only thing** between WOWII-61 and a closed S3 surface"* |',
 '| 9 | `HANDOVER.md` heading | *"WOWII-61 — **唯一残余** = GFAN 族第二族轮"* |',
 '| 11 | `orchestration/STATUS.md` banner | *"WOWII-61 的 S3 面**只差一个族轮**就全闭"* |',
 '| 12 | `orchestration/STATUS.md` item 1 | *"w61 的 S3 面**只差一个族轮**而族席已空"* |',
 'GFANν-HC, **because that is what closes the S3 surface**"*. **That reason is the dropped',
 'closed S3 surface"*. **AH3\'s sweep missed it because it says "only statement standing',
]
t = DRAFT.read_text(encoding="utf-8"); FAIL=[]
print("pass 2 -- CLASS A additions (quoted retraction, marker applied):")
for a in RETRACTION:
    n = t.count(a)
    if n != 1: FAIL.append("anchor %d hits: %r" % (n, a[:60])); continue
    if not G2.search(a): FAIL.append("anchor does not match G2: %r" % a[:60]); continue
    t = t.replace(a, a + " " + MARK, 1); print("   marked  %s" % a[:90])
print()
print("POSITIVE CONTROL: each string fires bare, is exempt marked")
ok = all(bool(G2.search(a)) and not any(G2.search(l) and MARK not in l
         for l in (a + " " + MARK).split("\n")) for a in RETRACTION)
print("   all pass: %s" % ok)
if not ok: FAIL.append("positive control failed")
if FAIL: print("!! NOTHING WRITTEN:", FAIL); sys.exit(2)
DRAFT.write_text(t, encoding="utf-8")
lines = t.split("\n")
u = [(i,l) for i,l in enumerate(lines,1) if G2.search(l) and MARK not in l]
print("\nFINAL unmarked G2 occurrences: %d  (each adjudicated B/C/D by reading)" % len(u))
for i,l in u: print("   %5d %s" % (i, l.strip()[:92]))
sys.exit(0)
