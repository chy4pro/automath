#!/usr/bin/env python3
"""owner-w61 round 29 - item 2: is Corollary C1-C's route to C1 for k >= 3 VIABLE?

C1-C proves C1 for lam as soon as M := [lam_1]^{lam_1+1} u lam has SOME realization G
with alpha(G) <= k.  Since residue(M) <= alpha(G) for every realization (FMS), the route
is available for lam exactly when

        minalpha(M) := min over realizations G of M of alpha(G)   <=   k.

This script computes minalpha(M) EXHAUSTIVELY (every labelled graph on N = |M| vertices,
degree-filtered) for every partition lam with k >= 2 and N <= 7, and compares it with k
and with residue(M).  A single lam with minalpha > k would kill the route outright.
Nothing here is taken from the draft: minalpha is recomputed from graphs, residue from
the process.
"""
import sys
from collections import Counter

def run(lst):
    cur = sorted(lst, reverse=True); n = 0
    while True:
        if not cur or cur[0] == 0: return n, len(cur)
        d = cur[0]; rest = cur[1:]
        if d > len(rest): return None, None
        blk, tail = rest[:d], rest[d:]
        if any(x == 0 for x in blk): return None, None
        cur = sorted([x - 1 for x in blk] + tail, reverse=True); n += 1

def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield []; return
    for p in range(min(n, mx), 0, -1):
        for t in parts(n - p, p): yield [p] + t

def alpha(nv, adj):
    best = 0
    for S in range(1 << nv):
        bits = [i for i in range(nv) if S >> i & 1]
        if len(bits) <= best: continue
        ok = True
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if adj[bits[i]] >> bits[j] & 1: ok = False; break
            if not ok: break
        if ok: best = len(bits)
    return best

CACHE = {}
def minalpha(M):
    key = tuple(sorted(M, reverse=True))
    if key in CACHE: return CACHE[key]
    nv = len(M)
    pairs = [(i, j) for i in range(nv) for j in range(i + 1, nv)]
    target = sorted(M, reverse=True)
    best = None; nreal = 0
    for mask in range(1 << len(pairs)):
        adj = [0] * nv
        m = mask; b = 0
        while m:
            if m & 1:
                i, j = pairs[b]; adj[i] |= 1 << j; adj[j] |= 1 << i
            m >>= 1; b += 1
        deg = sorted((bin(a).count("1") for a in adj), reverse=True)
        if deg != target: continue
        nreal += 1
        a = alpha(nv, adj)
        if best is None or a < best: best = a
    CACHE[key] = (best, nreal)
    return CACHE[key]

print("=" * 78)
print("ITEM 2 -- viability of Corollary C1-C's route, EXHAUSTIVE for |M| <= 7")
print("=" * 78)
print("  lam            k  w  |M|  residue  minalpha  #realizations  C1-C available?")
rows = 0; dead = 0; tight = 0
for n in range(2, 13):
    for lam in parts(n):
        k, w = len(lam), lam[0]
        if k < 2: continue
        M = [w] * (w + 1) + lam
        if len(M) > 7: continue
        st, res = run(M)
        if st is None: continue
        ma, nreal = minalpha(M)
        rows += 1
        avail = ma is not None and ma <= k
        if not avail: dead += 1
        if ma == k: tight += 1
        print("  %-14s %-2d %-2d %-4d %-8d %-9s %-14d %s"
              % ("+".join(map(str, lam)), k, w, len(M), res, ma, nreal,
                 "YES" if avail else "*** NO ***"))
print()
print("  rows: %d ; C1-C UNAVAILABLE: %d ; minalpha exactly k (tight): %d" % (rows, dead, tight))
print()
print("  Sanity, on the same rows: residue <= minalpha (FMS) and residue <= k (C1):")
bad1 = bad2 = 0
for n in range(2, 13):
    for lam in parts(n):
        k, w = len(lam), lam[0]
        if k < 2: continue
        M = [w] * (w + 1) + lam
        if len(M) > 7: continue
        st, res = run(M)
        if st is None: continue
        ma, _ = minalpha(M)
        if res > ma: bad1 += 1; print("   ** FMS VIOLATION lam=%s" % lam)
        if res > k: bad2 += 1; print("   ** C1 VIOLATION  lam=%s" % lam)
print("   residue > minalpha : %d ;  residue > k : %d" % (bad1, bad2))
print()
print("=" * 78)
print("  The disjoint-union special case, stated and checked:")
print("  if lam is GRAPHICAL then G := K_{w+1} (disjoint union) H realizes M, and")
print("  alpha(G) = 1 + alpha(H) <= 1 + (k-1) = k because H has an edge.")
print("=" * 78)
ok = 0
for n in range(2, 13):
    for lam in parts(n):
        k, w = len(lam), lam[0]
        if k < 2: continue
        M = [w] * (w + 1) + lam
        if len(M) > 7: continue
        if run(lam)[0] is None: continue
        ma, _ = minalpha(M)
        ok += 1
        assert ma is not None and ma <= k, lam
print("   graphical lam rows with |M| <= 7 : %d ; all have minalpha <= k" % ok)
print("done")
