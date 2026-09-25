#!/usr/bin/env python3
"""owner-w61 round 29 - Corollary C1-C's sufficient condition FAILS on an infinite family.

Witness family:  lam = (w, 1) with w ODD, w >= 3.  Then k = 2, |lam| = w+1 is even, so
M := [w]^{w+1} u lam = [w]^{w+2} u [1] IS a step sequence, and C1 holds there by
Theorem C1-2 (s0 = w+1).  But NO realization of M has alpha <= k = 2.

Hand argument (three lines, machine-confirmed below):
  alpha(G) <= 2  <=>  complement(G) is triangle-free.  M has N = w+3 vertices, so
  complement degrees are (N-1) - w = 2  for the w+2 entries of value w, and
  (N-1) - 1 = w+1  for the single entry of value 1.  In a triangle-free complement the
  degree-(w+1) vertex u has w+1 independent neighbours, each of complement-degree 2, so
  each needs its second edge at the ONE remaining vertex z; then deg(z) = w+1, but
  deg(z) = 2.  Contradiction unless w = 1.

This script re-derives minalpha by a SECOND, structurally different route from
w61_r29_c1lead.py: a backtracking realization enumerator (choose each vertex's forward
neighbourhood) instead of a mask sweep, with early exit as soon as alpha <= k is found.
"""
import sys
from itertools import combinations

def run(lst):
    cur = sorted(lst, reverse=True); n = 0
    while True:
        if not cur or cur[0] == 0: return n, len(cur)
        d = cur[0]; rest = cur[1:]
        if d > len(rest): return None, None
        blk, tail = rest[:d], rest[d:]
        if any(x == 0 for x in blk): return None, None
        cur = sorted([x - 1 for x in blk] + tail, reverse=True); n += 1

def alpha_le(nv, adj, bound):
    """True iff alpha(G) <= bound."""
    best = 0
    for S in range(1 << nv):
        bits = [i for i in range(nv) if S >> i & 1]
        if len(bits) <= bound: continue
        ok = True
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if adj[bits[i]] >> bits[j] & 1: ok = False; break
            if not ok: break
        if ok: return False
    return True

def exists_realization_with_alpha_le(M, bound, cap=8_000_000):
    """Backtracking over labelled realizations; early exit on the first witness."""
    nv = len(M)
    deg = list(M)
    adj = [0] * nv
    nodes = [0]
    found = [False]
    def rec(v, rem):
        if nodes[0] > cap: raise RuntimeError("cap")
        nodes[0] += 1
        if found[0]: return
        if v == nv:
            if all(x == 0 for x in rem):
                if alpha_le(nv, adj, bound): found[0] = True
            return
        need = rem[v]
        later = [u for u in range(v + 1, nv)]
        if need > len(later): return
        for combo in combinations(later, need):
            if any(rem[u] == 0 for u in combo): continue
            for u in combo:
                adj[v] |= 1 << u; adj[u] |= 1 << v; rem[u] -= 1
            rem[v] = 0
            rec(v + 1, rem)
            for u in combo:
                adj[v] &= ~(1 << u); adj[u] &= ~(1 << v); rem[u] += 1
            rem[v] = need
            if found[0]: return
    rec(0, deg)
    return found[0], nodes[0]

print("=" * 78)
print("COROLLARY C1-C's HYPOTHESIS ON lam = (w,1), w ODD  --  second implementation")
print("=" * 78)
print("  w   lam     |M|  k  residue  s0   C1 true?  exists G with alpha<=k ?  nodes")
for w in (3, 5, 7, 9):
    lam = [w, 1]; k = 2
    M = sorted([w] * (w + 1) + lam, reverse=True)
    st, res = run(M)
    if st is None:
        print("  %-3d %-7s not a step sequence" % (w, lam)); continue
    try:
        ok, nodes = exists_realization_with_alpha_le(M, k)
    except RuntimeError:
        print("  %-3d %-7s %-4d %-2d %-8d %-4d %-9s CAP REACHED" % (w, lam, len(M), k, res, st, st != w)); continue
    print("  %-3d %-7s %-4d %-2d %-8d %-4d %-9s %-24s %d"
          % (w, lam, len(M), k, res, st, "YES" if st != w else "NO",
             "YES" if ok else "*** NO ***", nodes))

print()
print("  control -- the same enumerator on rows the mask sweep called AVAILABLE:")
for lam in ([1, 1], [2, 2], [2, 1, 1], [3, 3], [3, 2, 1], [2, 2, 2], [3, 3, 2]):
    w, k = lam[0], len(lam)
    M = sorted([w] * (w + 1) + lam, reverse=True)
    if run(M)[0] is None: continue
    ok, nodes = exists_realization_with_alpha_le(M, k)
    print("   lam=%-10s k=%d  alpha<=k realizable: %-5s  (mask sweep said YES)"
          % ("+".join(map(str, lam)), k, ok))

print()
print("  control -- alpha<=k-1 vs residue.  FMS forbids alpha<=k-1 exactly when residue=k;")
print("  rows with residue=k-1 are NOT forbidden, and the enumerator must say so:")
for lam in ([2, 1, 1], [1, 1, 1, 1], [3, 2, 1], [2, 2, 1, 1], [2, 2, 2, 2]):
    w, k = lam[0], len(lam)
    M = sorted([w] * (w + 1) + lam, reverse=True)
    if run(M)[0] is None: continue
    ok, _ = exists_realization_with_alpha_le(M, k - 1)
    r = run(M)[1]
    print("   lam=%-10s k=%d  residue=%d %s  alpha<=k-1 realizable: %-5s  (FMS predicts %s)"
          % ("+".join(map(str, lam)), k, r,
             "(= k)  " if r == k else "(= k-1)", ok, "False" if r == k else "possible"))
print("done")
