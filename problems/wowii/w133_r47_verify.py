#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 round 47 -- STANDALONE re-verification (doctrine 105).

Shares NO code with w133_r47_spec.py.  Everything here is written from scratch and
deliberately differently:
  * adjacency as BITMASKS (ints), not sets of ints;
  * distances by bitmask frontier expansion from every vertex, not by deque BFS;
  * geodesics enumerated FORWARD from w (push u_{i+1} with d(w,u)=i+1 and d(u,x)=d-i-1),
    not by backward parent-walk from x;
  * inducedness by a bitmask sweep, not by a double loop over index pairs;
  * k2/k3 by popcount on bitmask intersections;
  * the two sidestep shapes re-derived from the STATEMENTS in the draft, not copied.

It reads only the four host edge lists and problems/wowii/w133_r47_resid.txt, and re-decides,
for every condition-4 vertex of every CASE A host, whether (TAIL-2S) and (TAIL-2S') close it
-- EXHAUSTIVELY over every far end and every geodesic -- then compares the residual set with
the one the builder dumped.  It also re-checks, independently, the two statements this round
puts weight on: the (SHELL) identity deg(y) = 1 + k2(y) + |Z(y)|, and (BUDGET-SUB)
(no frame closed by the budget test without a firing z).

system python3, pure stdlib.  No SAT.
"""
from __future__ import print_function
import sys
import time

T0 = time.time()
CHECKS = 0
FAILS = 0


def ck(c, m):
    global CHECKS, FAILS
    CHECKS += 1
    if not c:
        FAILS += 1
        print("FAIL: " + m, flush=True)


def read_host(path):
    """own parser: first int is n, then pairs."""
    toks = []
    for line in open(path):
        line = line.split("#")[0].strip()
        if line:
            toks.extend(line.split())
    nums = [int(t) for t in toks]
    n = nums[0]
    A = [0] * n
    it = iter(nums[1:])
    for u in it:
        v = next(it)
        A[u] |= 1 << v
        A[v] |= 1 << u
    return n, A


def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


def bits(x):
    out = []
    i = 0
    while x:
        if x & 1:
            out.append(i)
        x >>= 1
        i += 1
    return out


def dists(n, A):
    """bitmask frontier expansion."""
    D = []
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        seen = 1 << s
        front = 1 << s
        k = 0
        while front:
            k += 1
            nxt = 0
            for u in bits(front):
                nxt |= A[u]
            nxt &= ~seen
            for u in bits(nxt):
                d[u] = k
            seen |= nxt
            front = nxt
        D.append(d)
    return D


def induced(A, P):
    """bitmask sweep: P induced path?"""
    if len(set(P)) != len(P):
        return False
    m = 0
    for v in P:
        m |= 1 << v
    for i, v in enumerate(P):
        nb = A[v] & m
        want = 0
        if i > 0:
            want |= 1 << P[i - 1]
        if i + 1 < len(P):
            want |= 1 << P[i + 1]
        if nb != want:
            return False
    return True


def geos(n, A, D, w, x):
    """EVERY w->x geodesic, enumerated FORWARD."""
    d = D[w][x]
    out = []
    stack = [[w]]
    while stack:
        P = stack.pop()
        i = len(P) - 1
        if P[-1] == x:
            if i == d:
                out.append(P)
            continue
        for u in bits(A[P[-1]]):
            if D[w][u] == i + 1 and D[u][x] == d - i - 1:
                stack.append(P + [u])
    return out


def kcount(A, P, v, idxs):
    c = 0
    d = len(P) - 1
    for j in idxs:
        j = d + j
        if j >= 0 and (A[v] & A[P[j]]):
            c += 1
    return c


def alocal(n, A, v):
    """a(v) = independence number of N(v); in a C4-free graph N(v) induces a matching, but
    this function does NOT assume that -- it computes a TRUE maximum independent set by
    branching, so it is valid whatever the host looks like."""
    nb = bits(A[v])
    best = [0]

    def rec(rem, cur):
        if not rem:
            best[0] = max(best[0], cur)
            return
        if cur + len(rem) <= best[0]:
            return
        u = rem[0]
        rec([x for x in rem[1:] if not (A[u] >> x) & 1], cur + 1)
        rec(rem[1:], cur)
    rec(nb, 0)
    return best[0]


def close_2s(n, A, D, ecc, w):
    """(TAIL-2S), re-derived from draft 50.6: Q = u_0..u_{d-2}, p, y, u_d with
    p in N(y)&N(u_{d-2}), p !~ u_{d-3}, a(u_d) >= 3; extend by y' in N(u_d).
    EXHAUSTIVE over far ends and geodesics.  Returns True if an anchored induced path on
    ecc(w)+3 vertices is actually BUILT."""
    e = ecc[w]
    if e < 3:
        return False
    for x in range(n):
        if D[w][x] != e:
            continue
        for P in geos(n, A, D, w, x):
            d = len(P) - 1
            if d < 3:
                continue
            ud, um1, um2, um3 = P[d], P[d - 1], P[d - 2], P[d - 3]
            for y in bits(A[ud]):
                if y == um1 or ((A[um1] >> y) & 1):
                    continue
                if any(y == P[i] or ((A[P[i]] >> y) & 1) for i in range(d)):
                    continue
                if alocal(n, A, ud) < 3:
                    continue
                for p in bits(A[y] & A[um2]):
                    if p in P or p == y:
                        continue
                    if (A[um3] >> p) & 1:
                        continue
                    Q = P[:d - 1] + [p, y, ud]
                    if not (induced(A, Q) and Q[0] == w):
                        continue
                    for yp in bits(A[ud]):
                        if yp in Q:
                            continue
                        R = Q + [yp]
                        if len(R) == e + 3 and R[0] == w and induced(A, R):
                            return True
    return False


def close_2sp(n, A, D, ecc, w):
    """(TAIL-2S'), re-derived from draft 51.5: R = u_0..u_{d-3}, q, y, u_d, u_{d-1} with
    q in N(y)&N(u_{d-3}), q !~ u_{d-4}; extend by s in N(u_{d-1}) off the exclusion set."""
    e = ecc[w]
    if e < 3:
        return False
    for x in range(n):
        if D[w][x] != e:
            continue
        for P in geos(n, A, D, w, x):
            d = len(P) - 1
            if d < 3:
                continue
            ud, um1, um2, um3 = P[d], P[d - 1], P[d - 2], P[d - 3]
            um4 = P[d - 4] if d >= 4 else None
            for y in bits(A[ud]):
                if y == um1 or ((A[um1] >> y) & 1):
                    continue
                if any(y == P[i] or ((A[P[i]] >> y) & 1) for i in range(d)):
                    continue
                for q in bits(A[y] & A[um3]):
                    if q in P or q == y:
                        continue
                    if um4 is not None and ((A[um4] >> q) & 1):
                        continue
                    R = P[:d - 2] + [q, y, ud, um1]
                    if not (len(R) == e + 2 and R[0] == w and induced(A, R)):
                        continue
                    exc = (1 << ud) | (1 << um2) | (A[q] & A[um1]) | (A[ud] & A[um1])
                    for s in bits(A[um1] & ~exc):
                        S = R + [s]
                        if len(S) == e + 3 and S[0] == w and induced(A, S):
                            return True
    return False


HOSTS = (("W43a", "problems/wowii/w133_r43_W43a.txt"),
         ("W43b", "problems/wowii/w133_r43_W43b.txt"),
         ("W43c", "problems/wowii/w133_r43_W43c.txt"),
         ("W44a", "problems/wowii/w133_r44_W44a.txt"))


def main():
    print("w133 r47 STANDALONE verifier -- shares no code with the builder.  system python3")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print(__doc__)
    claimed = set()
    try:
        for line in open("problems/wowii/w133_r47_resid.txt"):
            line = line.split("#")[0].strip()
            if line:
                t, v = line.split()
                claimed.add((t, int(v)))
    except IOError:
        print("  residual file missing -- cannot compare")
    mine = set()
    tot = n2s = n2sp = 0
    for tag, path in HOSTS:
        n, A = read_host(path)
        # C4-freeness and triangle-freeness, re-asserted here from the bitmasks
        c4 = True
        tf = True
        for u in range(n):
            for v in range(u + 1, n):
                if popcount(A[u] & A[v]) >= 2:
                    c4 = False
            if A[u] & sum(1 << x for x in bits(A[u]) if A[u] & A[x]):
                pass
        for u in range(n):
            for v in bits(A[u]):
                if v > u and (A[u] & A[v]):
                    tf = False
        ck(c4, "%s C4-free (re-asserted from bitmasks)" % tag)
        ck(tf, "%s triangle-free (re-asserted from bitmasks)" % tag)
        D = dists(n, A)
        ecc = [max(D[v]) for v in range(n)]
        r = min(ecc)
        ctr = [v for v in range(n) if ecc[v] == r]
        cond4 = [w for w in range(n) if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
        a = b = 0
        for w in cond4:
            tot += 1
            x1 = close_2s(n, A, D, ecc, w)
            x2 = close_2sp(n, A, D, ecc, w)
            a += x1
            b += x2
            if not x1 and not x2:
                mine.add((tag, w))
        n2s += a
        n2sp += b
        print("  %-5s n=%d rad=%d diam=%d  condition-4 vertices %3d ;  (TAIL-2S) %3d ;"
              "  (TAIL-2S') %3d ;  NEITHER %3d"
              % (tag, n, r, max(ecc), len(cond4), a, b,
                 len([1 for w in cond4 if (tag, w) in mine])))
    print("  TOTAL condition-4 vertices %d ; (TAIL-2S) %d ; (TAIL-2S') %d ; NEITHER %d"
          % (tot, n2s, n2sp, len(mine)))
    print("  builder's residual set: %s" % sorted(claimed))
    print("  this verifier's residual set: %s" % sorted(mine))
    ck(mine == claimed, "the residual set agrees with the builder's, vertex for vertex")
    ck(tot == 260, "260 condition-4 vertices, independently recomputed")
    print()
    print("  ---- independent re-check of (SHELL) and (BUDGET-SUB) on W44a ----")
    n, A = read_host("problems/wowii/w133_r44_W44a.txt")
    D = dists(n, A)
    ecc = [max(D[v]) for v in range(n)]
    diam = max(ecc)
    idbad = admbad = budonly = nfr = 0
    p1bad = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        for x in range(n):
            if D[v][x] != diam:
                continue
            for P in geos(n, A, D, v, x):
                d = len(P) - 1
                adm = []
                for y in bits(A[x]):
                    if y == P[d - 1] or ((A[P[d - 1]] >> y) & 1):
                        continue
                    if any(y == P[i] or ((A[P[i]] >> y) & 1) for i in range(d)):
                        continue
                    adm.append(y)
                if set(adm) != set(bits(A[x])) - set([P[d - 1]]):
                    admbad += 1
                for y in adm:
                    nfr += 1
                    Zm = A[y]
                    Zm &= ~(1 << x)
                    for i in range(d + 1):
                        Zm &= ~(1 << P[i])
                        Zm &= ~A[P[i]]
                    Z = bits(Zm)
                    k2 = kcount(A, P, y, (-2, -3))
                    if popcount(A[y]) != 1 + k2 + len(Z):
                        idbad += 1
                    if not Z:
                        continue
                    B = 0
                    for j in (d - 1, d - 2, d - 3, d - 4):
                        if j >= 0:
                            B |= A[P[j]]
                    for i in range(d + 1):
                        B &= ~(1 << P[i])
                    sk = sum(kcount(A, P, z, (-1, -2, -3, -4)) for z in Z)
                    if sk > popcount(B):
                        p1bad += 1
                    sd = sum(popcount(A[z]) - 1 for z in Z)
                    if sd > popcount(B):
                        if not any(max(alocal(n, A, z), popcount(A[z]) - 1)
                                   >= 2 + kcount(A, P, z, (-1, -2, -3, -4)) for z in Z):
                            budonly += 1
    print("  W44a frames re-enumerated independently: %d" % nfr)
    ck(admbad == 0, "(SHELL)(a) admissible set = N(u_d) minus {u_{d-1}} -- independently")
    ck(idbad == 0, "(SHELL)(b) deg(y) = 1 + k2(y) + |Z(y)| -- independently, with a TRUE "
                   "independence number where a(.) is used")
    ck(p1bad == 0, "SUM_z k3(z) <= |B| -- independently")
    ck(budonly == 0, "(BUDGET-SUB): 0 frames closed by the budget test with no firing z")
    print("  admissible mismatches %d ; identity violations %d ; budget bound violations %d ;"
          " BUDGET-only frames %d" % (admbad, idbad, p1bad, budonly))

    print()
    print("  ---- W47a: the round's CONSTRUCTED CASE A instance, re-verified STANDALONE ----")
    try:
        n, A = read_host("problems/wowii/w133_r47_W47a.txt")
    except IOError:
        print("  W47a missing -- not verified")
        print()
        print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
        return 1 if FAILS else 0
    c4 = True
    tf = True
    for u in range(n):
        for v in range(u + 1, n):
            if popcount(A[u] & A[v]) >= 2:
                c4 = False
    for u in range(n):
        for v in bits(A[u]):
            if v > u and (A[u] & A[v]):
                tf = False
    ck(c4, "W47a C4-free")
    ck(tf, "W47a triangle-free")
    D = dists(n, A)
    ck(all(min(d for d in D[v]) >= 0 for v in range(n)), "W47a connected")
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    diam = max(ecc)
    ctr = [v for v in range(n) if ecc[v] == r]
    cond4 = [w for w in range(n) if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
    lv = sum(alocal(n, A, v) for v in range(n)) / float(n)
    print("  W47a n=%d rad=%d diam=%d offset=%+d l=%.6f (TRUE alpha) centre=%d cond4=%d"
          % (n, r, diam, diam - r, lv, len(ctr), len(cond4)))
    ck(n == 428, "W47a has 428 vertices")
    ck(diam - r == 1, "W47a is offset +1 -- the CASE A hypothesis")
    ck(int(lv) == 4, "W47a has floor(l) = 4")
    ck(len(cond4) == 126, "W47a has 126 condition-4 vertices")
    F = N = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        for x in range(n):
            if D[v][x] != diam:
                continue
            for P in geos(n, A, D, v, x):
                d = len(P) - 1
                for y in bits(A[x]):
                    if y == P[d - 1] or ((A[P[d - 1]] >> y) & 1):
                        continue
                    if any(y == P[i] or ((A[P[i]] >> y) & 1) for i in range(d)):
                        continue
                    Zm = A[y] & ~(1 << x)
                    for i in range(d + 1):
                        Zm &= ~(1 << P[i])
                        Zm &= ~A[P[i]]
                    for z in bits(Zm):
                        F += 1
                        k3 = kcount(A, P, z, (-1, -2, -3, -4))
                        if max(alocal(n, A, z), popcount(A[z]) - 1) >= 2 + k3:
                            N += 1
    print("  W47a step-3 frames F=%d ; (TAIL-3'') fires N=%d ; FIRE-GAP=%d (%.4f%%)"
          % (F, N, F - N, 100.0 * (F - N) / F if F else 0.0))
    ck(F == 531759, "W47a F = 531759, independently recounted")
    ck(N == 531598, "W47a N = 531598, independently recounted with a TRUE alpha(N(z))")
    ck(F - N == 161, "W47a FIRE-GAP = 161")
    print()
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
