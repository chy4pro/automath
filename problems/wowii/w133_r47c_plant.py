#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 owner round 47, SLICE 3 -- THE CONSTRUCTION, SCREENED.

Slice 1's PART 6 planted degree-2 vertices to the (HUG-EQ) shape and the built host stopped
being a CASE A instance at the FIRST plant: rad 5 -> 6, diam 6 -> 7, condition-4 vertices
129 -> 0.  That is a defect in MY RULE, not a verdict on the construction, and saying so is
the point of this slice.  A new vertex z attached to {y, c} has

        d(z, u) = 1 + min( d(y,u), d(c,u) )     for every old u,
        ecc(z)  = 1 + max_u min( d(y,u), d(c,u) ),

so diam is preserved exactly when the pair {y, c} JOINTLY 2-covers the host at radius
diam-1: max_u min(d(y,u), d(c,u)) <= diam - 1.  Slice 1's rule never screened for that, and
its y (a neighbour of a far end) and c (a neighbour of u_{d-1}) are both peripheral, so
ecc(z) = diam+1 every time.  This slice SCREENS, and reports the screen's own yield first --
because if no spec-shaped pair survives it, THAT is the obstruction, and it is a statement
about the host, not about my rule.

  PART A   the screen's yield: how many pairs {y, c} at distance >= 3 (C4- and
           triangle-freeness) jointly 2-cover at radius diam-1 (diameter preserved), split
           by whether the pair has the (HUG-EQ) SPEC SHAPE -- y admissible at a far end of a
           diametral vertex, c a neighbour of u_{d-1} off the path, which is what makes the
           planted z a step-3 vertex with deg = 2 and k3 = 1.
  PART B   plant the survivors and re-measure everything: C4-freeness and triangle-freeness
           ASSERTED on the built host, then n, rad, diam, offset, l, mu, condition-4 count,
           F, N and FIRE-GAP by the exhaustive census.

DIRECTION OF ERROR (129): every number is measured on the BUILT host, so `this host reaches
FIRE-GAP x%' is SOUND.  `No construction can do better' is NOT claimed and would be
inconclusive.  A screen yield of zero is SOUND (the screen is exhaustive over pairs).

Pure stdlib, system python3.  No SAT, no search over a large space -- the pair screen is a
pass over the O(n^2) pairs of ONE fixed host.  Primitives COPIED VERBATIM from
w133_r47_spec.py.
"""
from __future__ import print_function
import sys
import time
from collections import deque
from itertools import combinations

sys.setrecursionlimit(100000)

T0 = time.time()
DEADLINE = 1500.0
CHECKS = 0
FAILS = 0


def over():
    return (time.time() - T0) > DEADLINE


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)

# ------------------------------------------------------------------ primitives (COPIED)


def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    """this line's sense: NO two vertices have two common neighbours."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val_matching(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    return D, ecc, r


def l_of(g):
    n = len(g)
    return sum(a_val_matching(g, v) for v in range(n)) / float(n)


def girth(g):
    """shortest cycle length; 10**9 if acyclic.  BFS from every vertex."""
    n = len(g)
    best = 10 ** 9
    for s in range(n):
        d = [-1] * n
        par = [-1] * n
        d[s] = 0
        dq = deque([s])
        while dq:
            u = dq.popleft()
            if 2 * d[u] >= best:
                break
            for w in g[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1
                    par[w] = u
                    dq.append(w)
                elif w != par[u]:
                    c = d[u] + d[w] + 1
                    if c < best:
                        best = c
        if best == 3:
            break
    return best


def bipartite(g):
    n = len(g)
    col = [-1] * n
    for s in range(n):
        if col[s] >= 0:
            continue
        col[s] = 0
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for w in g[u]:
                if col[w] < 0:
                    col[w] = 1 - col[u]
                    dq.append(w)
                elif col[w] == col[u]:
                    return False
    return True


def triangle_free(g):
    for u in range(len(g)):
        for v in g[u]:
            if v > u and (g[u] & g[v]):
                return False
    return True


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


class LCG(object):
    def __init__(self, seed):
        self.s = seed % (1 << 31)

    def nxt(self, k):
        self.s = (self.s * 1103515245 + 12345) % (1 << 31)
        return self.s % k

    def shuffled(self, xs):
        xs = list(xs)
        for i in range(len(xs) - 1, 0, -1):
            j = self.nxt(i + 1)
            xs[i], xs[j] = xs[j], xs[i]
        return xs


def pg2(q):
    def norm(v):
        for i in range(3):
            if v[i] % q:
                inv = pow(v[i], q - 2, q)
                return tuple((c * inv) % q for c in v)
    pts = sorted({norm((a, b, c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a, b, c) != (0, 0, 0)})
    idx = {p: i for i, p in enumerate(pts)}
    m = len(pts)
    E = []
    for j, L in enumerate(pts):
        for p in pts:
            if sum(p[t] * L[t] for t in range(3)) % q == 0:
                E.append((idx[p], m + j))
    return adj(2 * m, E)


def rand_c4free_dense(seed, n):
    """round 42's greedy random C4-free host, COPIED VERBATIM from w133_r45_ladder.py.
    (Round 45's error 1 was this builder RETYPED from memory; it is copied here.)"""
    st = seed

    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for i in range(len(pairs) - 1, 0, -1):
        j = nxt(i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = [set() for _ in range(n)]
    for (u, v) in pairs:
        if any(g[u] & g[x] for x in g[v] if x != u):
            continue
        if any(g[v] & g[y] for y in g[u] if y != v):
            continue
        g[u].add(v)
        g[v].add(u)
    alive = set(range(n))
    while True:
        gone = [v for v in alive
                if len(g[v] & alive) - sum(1 for x, y in combinations(sorted(g[v] & alive), 2)
                                           if y in g[x]) <= 1]
        if not gone:
            break
        alive -= set(gone)
        if not alive:
            return None
    idx = sorted(alive)
    pos = {v: i for i, v in enumerate(idx)}
    h = adj(len(idx), [(pos[u], pos[v]) for u in idx for v in g[u] if v in pos and u < v])
    if len(h) < 6 or not connected(h) or min(a_val_matching(h, v) for v in range(len(h))) < 2:
        return None
    return h


def necklace_x(qs, seed, fracs=None, tgt_mode="any", sub=None, widths=None):
    """round 45's asymmetric necklace, COPIED VERBATIM."""
    m = len(qs)
    blocks = [pg2(q) for q in qs]
    off = []
    tot = 0
    bmap = []
    for i, b in enumerate(blocks):
        off.append(tot)
        tot += len(b)
        bmap.extend([i] * len(b))
    E = []
    for i, b in enumerate(blocks):
        for (u, v) in edges_of(b):
            E.append((off[i] + u, off[i] + v))
    rng = LCG(seed)
    for i in range(m):
        j = (i + 1) % m
        npts = len(blocks[i]) // 2
        srcs = rng.shuffled(range(npts))
        if widths is not None and i in widths:
            k = widths[i]
        else:
            f = 1.0 if fracs is None else fracs[i % len(fracs)]
            k = max(1, int(round(npts * f)))
        k = max(1, min(k, len(blocks[j]), npts))
        srcs = srcs[:k]
        if tgt_mode == "points":
            pool = list(range(len(blocks[j]) // 2))
        else:
            pool = list(range(len(blocks[j])))
        tgts = rng.shuffled(pool)[:k]
        slen = 0 if sub is None else sub.get(i, 0)
        for s, t in zip(srcs, tgts):
            if slen == 0:
                E.append((off[i] + s, off[j] + t))
            else:
                prev = off[i] + s
                for _ in range(slen):
                    nv = tot
                    tot += 1
                    bmap.append(-(i + 1))
                    E.append((prev, nv))
                    prev = nv
                E.append((prev, off[j] + t))
    return adj(tot, E), bmap


def load_txt(path):
    nn = None
    ed = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) == 1:
            nn = int(p[0])
        else:
            ed.append((int(p[0]), int(p[1])))
    return adj(nn, ed)


def dump_txt(g, path, header):
    with open(path, "w") as f:
        f.write("# %s\n" % header)
        f.write("%d\n" % len(g))
        for (u, v) in edges_of(g):
            f.write("%d %d\n" % (u, v))



# ---------------------------------------------------- frame machinery (COPIED from r45)


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if P[i + 1] not in g[P[i]]:
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if P[j] in g[P[i]]:
                return False
    return True


def geodesics(D, g, w, x, cap):
    """up to `cap` DISTINCT w->x geodesics, deterministic order, as vertex lists w..x."""
    d = D[w][x]
    out = []

    def back(cur, acc):
        if len(out) >= cap:
            return
        if cur == w:
            out.append(list(reversed(acc)))
            return
        for p in sorted(g[cur]):
            if D[w][p] == D[w][cur] - 1:
                acc.append(p)
                back(p, acc)
                acc.pop()
                if len(out) >= cap:
                    return
    back(x, [x])
    return [P for P in out if len(P) == d + 1]


def tail1_frames(g, D, w, x, ngeo=3):
    """every (P, y) frame of (TAIL-1) from w to the far end x, over up to ngeo geodesics."""
    fr = []
    for P in geodesics(D, g, w, x, ngeo):
        d = len(P) - 1
        ud, um1 = P[-1], P[-2]
        for y in sorted(g[ud]):
            if y == um1 or y in g[um1]:
                continue
            if any(y == P[i] or y in g[P[i]] for i in range(d)):
                continue
            fr.append((P, y))
    return fr


def extend_once(g, R, v):
    """every u in N(R[-1]) that keeps R+[u] an induced path anchored at v, in sorted order."""
    out = []
    last = R[-1]
    head = R[:-1]
    for u in sorted(g[last]):
        if u in R:
            continue
        if any(u in g[x] for x in head):
            continue
        out.append(u)
    return out


def k3_of(g, P, z):
    """draft 46.1's k3 for the step-3 vertex z: indices d-1..d-4."""
    d = len(P) - 1
    k = 0
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0 and (g[z] & g[P[j]]):
            k += 1
    return k


def k2_of(g, P, y):
    d = len(P) - 1
    k = 0
    for j in (d - 2, d - 3):
        if j >= 0 and (g[y] & g[P[j]]):
            k += 1
    return k


def step3_frames(g, D, ecc, v, ngeo, nfar):
    """EVERY step-3 frame from v: yields (P, y, z).  ngeo/nfar = 10**9 means EXHAUSTIVE."""
    n = len(g)
    e = ecc[v]
    fars = sorted(u for u in range(n) if D[v][u] == e)[:nfar]
    for x in fars:
        for (P, y) in tail1_frames(g, D, v, x, ngeo):
            Q = P + [y]
            if len(Q) != e + 2:
                continue
            for z in extend_once(g, Q, v):
                yield (P, y, z)


# ================================================================== PART 0


HOSTS = []          # (tag, family, g)




def fires3(g, P, z):
    """(TAIL-3'')'s sufficient condition at the step-3 vertex z.  COPIED VERBATIM."""
    return max(a_val_matching(g, z), len(g[z]) - 1) >= 2 + k3_of(g, P, z)


def census(g):
    n = len(g)
    D, ecc, r = profile(g)
    diam = max(ecc)
    F = N = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
            F += 1
            if fires3(g, P, z):
                N += 1
    ctr = [v for v in range(n) if ecc[v] == r]
    cond4 = [w for w in range(n) if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
    return dict(n=n, r=r, diam=diam, off=diam - r, l=l_of(g), F=F, N=N, gap=F - N,
                cond4=len(cond4), mu=min(a_val_matching(g, v) for v in range(n)))


def spec_sites(g, D, ecc):
    """every pair {y, c} of the (HUG-EQ) SPEC SHAPE: y admissible at a far end x of a
    diametral vertex v on a geodesic P, c in N(u_{d-1}) off P.  Returned as a set of pairs
    so that the screen can be applied to it."""
    n = len(g)
    diam = max(ecc)
    out = set()
    for v in range(n):
        if ecc[v] != diam:
            continue
        for x in [u for u in range(n) if D[v][u] == diam]:
            for P in geodesics(D, g, v, x, 3):
                if len(P) != diam + 1:
                    continue
                um1 = P[-2]
                for y in sorted(g[x] - set([um1])):
                    for c in sorted(g[um1] - set(P)):
                        if y != c:
                            out.add((min(y, c), max(y, c)))
    return out


def main():
    print("w133 round 47 slice 3 -- the construction, SCREENED.  system python3.")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print(__doc__)
    g0 = load_txt("problems/wowii/w133_r44_W44a.txt")
    ck(connected(g0), "W44a connected")
    ck(c4_free(g0), "W44a C4-free -- ASSERTED")
    ck(triangle_free(g0), "W44a triangle-free -- ASSERTED")
    n = len(g0)
    D, ecc, r = profile(g0)
    diam = max(ecc)
    print("  base host W44a: n=%d rad=%d diam=%d offset=%+d l=%.4f centre=%d"
          % (n, r, diam, diam - r, l_of(g0), sum(1 for v in range(n) if ecc[v] == r)))
    print()
    print("=" * 78)
    print("PART A -- the screen, and its yield")
    print("=" * 78)
    ok = []
    npair = 0
    for y in range(n):
        for c in range(y + 1, n):
            if D[y][c] < 3:
                continue
            npair += 1
            m = 0
            for u in range(n):
                dy = D[y][u]
                dc = D[c][u]
                t = dy if dy < dc else dc
                if t > m:
                    m = t
                    if m > diam - 1:
                        break
            if m <= diam - 1:
                ok.append((y, c))
    print("  pairs at distance >= 3 (C4-/triangle-free plantable): %d" % npair)
    print("  of those, pairs that JOINTLY 2-COVER at radius diam-1 = %d, i.e. keep diam: %d"
          % (diam - 1, len(ok)))
    S = spec_sites(g0, D, ecc)
    print("  pairs of the (HUG-EQ) SPEC SHAPE (y admissible at a far end, c a neighbour of "
          "u_{d-1} off the path): %d" % len(S))
    good = [p for p in S if p in set(ok)]
    print("  SPEC-SHAPED pairs that ALSO survive the diameter screen: %d" % len(good))
    if not good:
        print()
        print("  ** THE SCREEN'S YIELD ON THE SPEC SHAPE IS ZERO, AND THAT IS THE FINDING. **")
        print("  Every site where planting produces the (HUG-EQ) equality is peripheral, and")
        print("  every peripheral site raises the diameter, which destroys the condition-4")
        print("  set the CASE A hypothesis is about.  On this host the (HUG-EQ) SHAPE and the")
        print("  CASE A ECCENTRICITY PROFILE are incompatible at EVERY candidate site -- the")
        print("  obstruction is the eccentricity bookkeeping, not the l-budget, which slice 1")
        print("  showed is neutral under planting.")
    print()
    print("=" * 78)
    print("PART B -- plant what survived, and re-measure")
    print("=" * 78)
    BEST = [0.0, None, None]
    base = census(g0)
    print("  %-18s n=%-4d rad=%-2d diam=%-2d offset=%+d l=%.4f mu=%d cond4=%-4d F=%-7d "
          "N=%-7d FIRE-GAP=%d (%.4f%%)"
          % ("W44a (base)", base['n'], base['r'], base['diam'], base['off'], base['l'],
             base['mu'], base['cond4'], base['F'], base['N'], base['gap'],
             100.0 * base['gap'] / base['F']))
    # Plant, in two flavours, so the comparison is not against one rule only:
    #   (1) SPEC-SHAPED and screened, if any survived;
    #   (2) SCREENED ONLY -- keeps the diameter but has no reason to make the planted vertex
    #       hug, so it is the CONTROL that says whether the shape mattered at all.
    for name, pool in (("spec+screen", good), ("screen only (control)", ok)):
        if not pool:
            print("  %-22s: pool EMPTY, nothing planted" % name)
            continue
        for K in range(1, 11):
            if over():
                print("  DEADLINE inside %s at K=%d" % (name, K))
                break
            g = [set(s) for s in g0]
            used = set()
            added = 0
            for (y, c) in pool:
                if added >= K:
                    break
                if y in used or c in used:
                    continue
                z = len(g)
                g.append(set([y, c]))
                g[y].add(z)
                g[c].add(z)
                used.add(y)
                used.add(c)
                added += 1
            okc4 = c4_free(g)
            oktf = triangle_free(g)
            ck(okc4, "%s K=%d built host is C4-free -- ASSERTED" % (name, K))
            ck(oktf, "%s K=%d built host is triangle-free -- ASSERTED" % (name, K))
            if not (okc4 and oktf and connected(g)):
                print("  %-22s K=%-3d REJECTED (C4-free %s, triangle-free %s)"
                      % (name, K, okc4, oktf))
                continue
            c1 = census(g)
            print("  %-22s +%-3d n=%-4d rad=%-2d diam=%-2d offset=%+d l=%.4f mu=%d "
                  "cond4=%-4d F=%-7d N=%-7d FIRE-GAP=%d (%.4f%%)%s"
                  % (name, added, c1['n'], c1['r'], c1['diam'], c1['off'], c1['l'],
                     c1['mu'], c1['cond4'], c1['F'], c1['N'], c1['gap'],
                     100.0 * c1['gap'] / c1['F'] if c1['F'] else 0.0,
                     "" if (c1['off'] == 1 and c1['cond4'] > 0)
                     else "   <-- NO LONGER A CASE A INSTANCE"))
            ck(int(c1['l']) == 4, "%s K=%d keeps floor(l) = 4" % (name, K))
            if c1['off'] == 1 and c1['cond4'] > 0 and int(c1['l']) == 4:
                gr = c1['gap'] / float(c1['F']) if c1['F'] else 0.0
                if gr > BEST[0]:
                    BEST[0] = gr
                    BEST[1] = (name, added, dict(c1))
                    BEST[2] = [set(t) for t in g]
            if added < K:
                break
    print()
    print("  BEST CASE-A-PRESERVING BUILD: %s" % (str(BEST[1][:2]) if BEST[1] else "none"))
    if BEST[2] is not None:
        c1 = BEST[1][2]
        print("    n=%d rad=%d diam=%d offset=%+d l=%.4f cond4=%d F=%d N=%d FIRE-GAP=%d "
              "(%.4f%%)  -- base was 11 (0.0022%%), a %.1fx gain, and the target is 100%%"
              % (c1['n'], c1['r'], c1['diam'], c1['off'], c1['l'], c1['cond4'], c1['F'],
                 c1['N'], c1['gap'], 100.0 * c1['gap'] / c1['F'],
                 (c1['gap'] / float(c1['F'])) / (11.0 / 490540.0)))
        dump_txt(BEST[2], "problems/wowii/w133_r47_W47a.txt",
                 "W47a = W44a + %d degree-2 vertices planted to the (HUG-EQ) shape, "
                 "round 47 slice 3.  n=%d l=%.6f rad=%d diam=%d cond4=%d FIRE-GAP=%d/%d"
                 % (BEST[1][1], c1['n'], c1['l'], c1['r'], c1['diam'], c1['cond4'],
                    c1['gap'], c1['F']))
        print("    dumped to problems/wowii/w133_r47_W47a.txt")
    print()
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
