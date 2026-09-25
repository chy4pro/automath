#!/usr/bin/env python3
"""
w61 round 4: the A'-residual partition of the Fan(tau,L) high phase.

Owner-w61 proved (draft Sec 7.8 A, Lemma FAN-4) that IF no C-vertex escapes a
block during the high phase, then the A'-entries at the start of step p+1 sum to
EXACTLY 2 -- a pure counting identity, no structural input.  So the residual
partition is either [1,1] or [2].

That distinction is LOAD-BEARING for every L >= 2, not just L = 2:
  [L]^(L+1), 1, 1  ->  the process needs tau+1 steps  (Lemma FAN-3, proved)
  [L]^(L+1), 2     ->  the process finishes in exactly tau steps, i.e. it WOULD
                       be a hard-core survivor.
This script (a) demonstrates the second line by direct simulation, and (b) scans
the SUPERSET Fan box (no occurring-type requirement) to see whether the [2]
residual is ever realized by an actual Fan degree sequence.
"""
import sys
from collections import Counter


def hh_steps(mult):
    """number of HH steps to clear a value multiset (list)."""
    s = sorted(mult, reverse=True)
    n = 0
    while s and s[0] > 0:
        d = s[0]; s = s[1:]
        if d > len(s):
            return None
        for i in range(d):
            s[i] -= 1
            if s[i] < 0:
                return None
        s.sort(reverse=True)
        n += 1
    return n


def parts(R, k, lo, hi, cur=None, start=None):
    if cur is None:
        cur, start = [], hi
    if k == 0:
        if R == 0:
            yield list(cur)
        return
    if R < lo * k or R > hi * k:
        return
    top = min(start, R - lo * (k - 1))
    for val in range(top, lo - 1, -1):
        cur.append(val)
        yield from parts(R - val, k - 1, lo, hi, cur, val)
        cur.pop()


def gale_ryser(a, b):
    if sum(a) != sum(b):
        return False
    if any(x < 0 for x in a) or any(x < 0 for x in b):
        return False
    a = sorted(a, reverse=True)
    if any(x > len(b) for x in a) or any(x > len(a) for x in b):
        return False
    for k in range(1, len(a) + 1):
        if sum(a[:k]) > sum(min(x, k) for x in b):
            return False
    return True


def hh_snapshot(deg, upto):
    """value multiset at the START of step upto+1 (0-indexed steps)."""
    s = sorted(deg, reverse=True)
    for _ in range(upto):
        if not s or s[0] == 0:
            return None
        d = s[0]; s = s[1:]
        if d > len(s):
            return None
        for i in range(d):
            s[i] -= 1
            if s[i] < 0:
                return None
        s.sort(reverse=True)
    return s


print("[A] the two candidate suffixes, simulated directly")
print("    (L+1 entries of value L, plus the residual of A'-total 2)")
for L in range(2, 9):
    a = [L] * (L + 1) + [1, 1]
    b = [L] * (L + 1) + [2]
    print(f"    L={L}:  [L]^(L+1),1,1 clears in {hh_steps(a)} steps "
          f"(need {L});   [L]^(L+1),2 clears in {hh_steps(b)} steps "
          f"(need {L})")
print("    => the [2] residual WOULD terminate on time: Lemma 2's '1+1, not 2'")
print("       is load-bearing for EVERY L>=2.")
print()

print("[B] does the [2] residual ever occur?  SUPERSET Fan box, no type "
      "requirement, A'-residual partition at the start of step p+1")
TAU_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
R_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 18
K_MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 14
hist = Counter()
bad = []
tot = 0
for tau in range(4, TAU_MAX + 1):
    for L in range(2, tau - 1):
        p = tau - L
        nW = p - 2
        if nW < 0:
            continue
        wvecs = [()] if nW == 0 else [tuple(q) for t in range(nW, R_MAX + 1)
                                      for q in parts(t, nW, 1, R_MAX)]
        for d_u in range(2, R_MAX + 1):
            for d_v in range(2, d_u + 1):
                for wv in wvecs:
                    R = d_u + d_v + sum(wv)
                    if R > R_MAX:
                        continue
                    bside = [d_u, d_v] + list(wv)
                    for k in range(1, K_MAX + 1):
                        if k > R:
                            continue
                        for adeg in parts(R, k, 1, p):
                            if not gale_ryser(adeg, bside):
                                continue
                            deg = ([tau] * (L + 1)
                                   + [tau - 1 + d_u, tau - 1 + d_v]
                                   + [tau + x for x in wv] + adeg)
                            snap = hh_snapshot(deg, p)
                            if snap is None:
                                continue
                            tot += 1
                            pos = [x for x in snap if x > 0]
                            cpart = [x for x in pos if x == L]
                            apart = sorted([x for x in pos if x != L],
                                           reverse=True)
                            # C-part must be the L+1 entries of value L
                            key = (len(cpart) == L + 1, tuple(apart))
                            hist[key] += 1
                            if len(cpart) != L + 1 or sum(apart) != 2:
                                bad.append((tau, L, d_u, d_v, wv, tuple(adeg),
                                            pos))
print(f"    Fan degree sequences reaching step p+1 = {tot}")
print(f"    (C-part is exactly [L]^(L+1) ?, A'-residual partition) histogram:")
for kk, vv in sorted(hist.items(), key=lambda t: -t[1])[:10]:
    print(f"       {kk} : {vv}")
print(f"    instances violating 'C-part=[L]^(L+1) and A'-sum=2' = {len(bad)}")
if bad:
    print(f"    first 3: {bad[:3]}")
print("    => a (True,(2,)) row would be a hard-core SURVIVOR; a (True,(1,1)) "
      "row is killed by Lemma FAN-3.")
