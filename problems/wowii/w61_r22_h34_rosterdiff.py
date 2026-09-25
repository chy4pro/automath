#!/usr/bin/env python3
"""owner-w61 round 22 -- TWO-WAY roster diff of the two independent H3 implementations.

impl-1 = the round-17 key's primitives (`w61_r17_roster_recompute.py`: steps/partitions),
         re-driven here to EMIT the nu=11 E>=1 survivor roster it only ever counted.
impl-2 = `w61_r22_h34_second_impl.py`, written round 22 from the SPECIFICATION only, by a
         helper explicitly forbidden to read any existing file in this repo.

The diff is symmetric: rows in impl-1 not in impl-2 AND rows in impl-2 not in impl-1.
Comparing totals only would not distinguish two rosters of equal size and different content.
"""
import time, pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
src = (ROOT / "problems/wowii/w61_r17_roster_recompute.py").read_text()
rec = {}
exec(compile(src.replace('if __name__ == "__main__":', 'if False:'),
             "w61_r17_roster_recompute.py", "exec"), rec)
steps, partitions = rec["steps"], rec["partitions"]

NU, TWO, T0, LIMIT = 11, 22, time.time(), 600.0
rows1, per_E = [], {}
for E in range(1, NU):
    eparts, lparts = list(partitions(E)), list(partitions(TWO - E))
    c = 0
    for L in range(NU + 1, TWO - E + 1):
        for e in eparts:
            cpart = [L + x for x in e] + [L] * (L + 1 - len(e))
            for lam in lparts:
                if steps(cpart + list(lam)) == L:
                    c += 1
                    rows1.append("E=%d L=%d e=[%s] lam=[%s]" %
                                 (E, L, ",".join(map(str, e)), ",".join(map(str, lam))))
        if time.time() - T0 > LIMIT:
            raise SystemExit("HARD TIME LIMIT")
    per_E[E] = c

r2path = ROOT / "problems/wowii/w61_r22_h34_second_roster.txt"
rows2 = [l.strip() for l in r2path.read_text().splitlines() if l.strip()]

def norm(rs):
    return sorted(r.replace(", ", ",") for r in rs)

n1, n2 = norm(rows1), norm(rows2)
s1, s2 = set(n1), set(n2)

print("impl-1 (round-17 primitives, re-driven) : %d survivor rows, per-E %s" % (len(n1), per_E))
print("impl-2 (round-22 spec-only helper)      : %d survivor rows" % len(n2))
print("impl-1 duplicate rows : %d" % (len(n1) - len(s1)))
print("impl-2 duplicate rows : %d" % (len(n2) - len(s2)))
only1 = sorted(s1 - s2)
only2 = sorted(s2 - s1)
print("\nIN impl-1 NOT IN impl-2 : %d" % len(only1))
for r in only1[:25]: print("   %s" % r)
print("IN impl-2 NOT IN impl-1 : %d" % len(only2))
for r in only2[:25]: print("   %s" % r)
print("\nORDERED IDENTITY (sorted lists equal) : %s" % (n1 == n2))
print("TWO-WAY DIFF CLEAN : %s" % (not only1 and not only2 and len(n1) == len(n2) == 791))
print("elapsed %.2fs" % (time.time() - T0))
