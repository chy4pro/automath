#!/usr/bin/env python3
"""
owner-w61 round 13 -- Repair AB7's evidence: extend the zero-padding-inertness
control of SS7.22 (c-1) convention 2 from its original scope (E=0 lists, nu<=4)
to the WHOLE enumerated class: every E=0 list AND every E>=1 list of the nu<=6
enumeration.  Q30 Defect 4 observed, correctly, that the cited 480-list control
did not literally cover the class it is invoked on.
"""
import itertools


def hh_step(m):
    s = sorted(m, reverse=True)
    d, rest = s[0], s[1:]
    if d > len(rest):
        return None
    out = [rest[i] - 1 if i < d else rest[i] for i in range(len(rest))]
    return None if any(v < 0 for v in out) else out


def steps(m):
    cur, n = list(m), 0
    while cur and max(cur) > 0:
        cur = hh_step(cur)
        if cur is None:
            return None
        n += 1
    return n


def partitions(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


PADS = (0, 1, 2, 3, 4, 8, 13)
tested = dis = 0
e0 = eplus = 0

for nu in range(1, 7):
    # --- E = 0 lists: [L]^{L+1} u lam, over the full range the proof uses
    for lam in partitions(2 * nu):
        for L in range(nu + 1, 2 * nu + 2):
            base = [L] * (L + 1) + list(lam)
            b = steps(base)
            e0 += 1
            for z in PADS:
                tested += 1
                if steps(base + [0] * z) != b:
                    dis += 1
    # --- E >= 1 lists: the exact S(nu) enumerated shapes
    for E in range(1, nu):
        for L in range(nu + 1, 2 * nu - E + 1):
            for e in partitions(E):
                if len(e) > L + 1:
                    continue
                for lam in partitions(2 * nu - E):
                    base = [L + x for x in e] + [L] * (L + 1 - len(e)) + list(lam)
                    b = steps(base)
                    eplus += 1
                    for z in PADS:
                        tested += 1
                        if steps(base + [0] * z) != b:
                            dis += 1

print("=== AB7: zero-padding inertness over the WHOLE nu<=6 enumerated class ===")
print(f"  E=0   base lists tested : {e0}")
print(f"  E>=1  base lists tested : {eplus}   (= S(1..6) = 0+3+24+110+397+1211 = "
      f"{0+3+24+110+397+1211})")
print(f"  paddings per list       : {PADS}")
print(f"  (list, padding) pairs   : {tested}")
print(f"  PADDING-DEPENDENT STEP COUNTS : {dis}")
print()
print("  Reason (unchanged, and this is what carries the general case): at each step")
print("  the block is the d LARGEST non-head entries, so a zero can enter the block")
print("  only when fewer than d positive entries remain -- and in that case the run")
print("  aborts whether or not the zeros were written down.")
print(f"\nFAILURE_COUNT = {dis}")
