#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""STANDALONE re-check of round 46's two load-bearing claims (doctrine 105).

This file shares NO CODE with w133_r46_hug.py.  Everything below is written from the
definitions, with deliberately different implementations:
  * distances by FLOYD-WARSHALL on a full matrix, not BFS;
  * neighbourhoods as BITMASKS (integers), not sets;
  * a(v) as a TRUE maximum independent set of G[N(v)] by recursive search, not by the
    deg - #edges matching bound -- so if the matching bound ever UNDERSTATED a(v) this file
    would report the lemma FIRING where the builder said it did not;
  * geodesics enumerated forward by DFS on the distance matrix, not backward.

It reads only:
  problems/wowii/w133_r44_W44a.txt      (the host, as an edge list)
  problems/wowii/w133_r46_nofire.txt    (the claimed non-firing frames)
and rebuilds Petersen / C7 / C8 from their own definitions.

CLAIM 1.  Petersen, C7 and C8 have F > 0 and N = 0: every step-3 frame of every vertex of
          maximum eccentricity exists, and (TAIL-3'') fires at NONE of them.
CLAIM 2.  Each of the 11 listed W44a frames is a genuine step-3 frame at a vertex with
          ecc = diam, and (TAIL-3'') does NOT fire at it.
"""
from __future__ import print_function
import sys
from itertools import combinations

CH = [0, 0]


def chk(cond, msg):
    CH[0] += 1
    if not cond:
        CH[1] += 1
        print("FAIL: " + msg)


# ------------------------------------------------------------- graph, as bitmasks


def build(n, edges):
    nb = [0] * n
    for (u, v) in edges:
        if u == v:
            continue
        nb[u] |= (1 << v)
        nb[v] |= (1 << u)
    return nb


def bits(m):
    out = []
    i = 0
    while m:
        if m & 1:
            out.append(i)
        m >>= 1
        i += 1
    return out


def floyd(nb):
    n = len(nb)
    INF = 10 ** 6
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
        for j in bits(nb[i]):
            D[i][j] = 1
    for k in range(n):
        Dk = D[k]
        for i in range(n):
            dik = D[i][k]
            if dik >= INF:
                continue
            Di = D[i]
            for j in range(n):
                t = dik + Dk[j]
                if t < Di[j]:
                    Di[j] = t
    return D


def alpha_nbhd(nb, v):
    """TRUE independence number of the subgraph induced on N(v), by recursive search."""
    S = bits(nb[v])
    idx = {u: i for i, u in enumerate(S)}
    m = len(S)
    adjm = [0] * m
    for a in range(m):
        for b in range(m):
            if a != b and (nb[S[a]] >> S[b]) & 1:
                adjm[a] |= (1 << b)
    best = [0]

    def rec(cand, size):
        if size + bin(cand).count("1") <= best[0]:
            return
        if cand == 0:
            if size > best[0]:
                best[0] = size
            return
        p = (cand & -cand).bit_length() - 1
        rec(cand & ~(1 << p) & ~adjm[p], size + 1)   # take p
        rec(cand & ~(1 << p), size)                  # drop p
    rec((1 << m) - 1, 0)
    return best[0]


def c4free(nb):
    n = len(nb)
    for u in range(n):
        for v in range(u + 1, n):
            if bin(nb[u] & nb[v]).count("1") >= 2:
                return False
    return True


def induced_path(nb, P):
    if len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if not ((nb[P[i]] >> P[i + 1]) & 1):
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if (nb[P[i]] >> P[j]) & 1:
                return False
    return True


def geos_forward(nb, D, s, t):
    """every s->t geodesic, built FORWARD from s using the distance matrix."""
    out = []
    d = D[s][t]

    def go(cur, acc):
        if cur == t:
            out.append(list(acc))
            return
        for w in bits(nb[cur]):
            if D[s][w] == D[s][cur] + 1 and D[w][t] == D[cur][t] - 1:
                acc.append(w)
                go(w, acc)
                acc.pop()
    go(s, [s])
    return [P for P in out if len(P) == d + 1]


def k3(nb, P, z):
    d = len(P) - 1
    k = 0
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0 and (nb[z] & nb[P[j]]):
            k += 1
    return k


def fires(nb, P, z):
    return max(alpha_nbhd(nb, z), bin(nb[z]).count("1") - 1) >= 2 + k3(nb, P, z)


def all_step3(nb, D, ecc, diam):
    """every step-3 frame of every vertex with ecc = diam.  Enumerated independently:
    y is taken as any neighbour of u_d whose closed neighbourhood misses the whole path,
    z as any neighbour of y with the same property."""
    n = len(nb)
    for v in range(n):
        if ecc[v] != diam:
            continue
        for x in range(n):
            if D[v][x] != ecc[v]:
                continue
            for P in geos_forward(nb, D, v, x):
                for y in bits(nb[P[-1]]):
                    if not induced_path(nb, P + [y]):
                        continue
                    for z in bits(nb[y]):
                        Q = P + [y, z]
                        if induced_path(nb, Q):
                            yield (P, y, z)


def load(path):
    n = None
    ed = []
    for ln in open(path):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        p = ln.split()
        if len(p) == 1:
            n = int(p[0])
        else:
            ed.append((int(p[0]), int(p[1])))
    return build(n, ed)


def main():
    print("STANDALONE re-check of round 46 -- shares no code with w133_r46_hug.py")

    # ---------------- CLAIM 1
    exhibits = []
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    exhibits.append(("Petersen", build(10, E)))
    for L in (7, 8):
        exhibits.append(("C%d" % L, build(L, [(i, (i + 1) % L) for i in range(L)])))
    for nm, nb in exhibits:
        n = len(nb)
        chk(c4free(nb), "%s is C4-free" % nm)
        D = floyd(nb)
        ecc = [max(D[v]) for v in range(n)]
        diam = max(ecc)
        chk(min(min(r) for r in D) >= 0 and max(max(r) for r in D) == diam,
            "%s distance matrix is finite (connected)" % nm)
        F = 0
        N = 0
        kmin = 99
        for (P, y, z) in all_step3(nb, D, ecc, diam):
            F += 1
            kk = k3(nb, P, z)
            kmin = min(kmin, kk)
            if fires(nb, P, z):
                N += 1
        mu = min(alpha_nbhd(nb, v) for v in range(n))
        print("  %-10s n=%-3d rad=%d diam=%d mu(true alpha)=%d  F=%-6d N=%-3d min k3=%s"
              % (nm, n, min(ecc), diam, mu, F, N, kmin if kmin < 99 else "-"))
        chk(F > 0, "%s has at least one step-3 frame (NOT vacuous)" % nm)
        chk(N == 0, "%s: (TAIL-3'') fires at NO step-3 frame" % nm)
        chk(kmin >= 1, "%s: no step-3 frame has k3 = 0" % nm)
        chk(kmin >= mu - 1, "%s: (ROW-K)'s k3 >= mu-1 holds at every step-3 frame" % nm)

    # ---------------- CLAIM 2
    nb = load("problems/wowii/w133_r44_W44a.txt")
    n = len(nb)
    chk(c4free(nb), "W44a is C4-free")
    tri = any((nb[u] & nb[v]) for u in range(n) for v in bits(nb[u]) if v > u)
    chk(not tri, "W44a is triangle-free (so alpha(N(v)) = deg(v) and the matching bound is "
                 "exact)")
    D = floyd(nb)
    ecc = [max(D[v]) for v in range(n)]
    diam = max(ecc)
    rad = min(ecc)
    print("  W44a  n=%d rad=%d diam=%d  (offset diam-rad = %+d)" % (n, rad, diam, diam - rad))
    nlines = 0
    for ln in open("problems/wowii/w133_r46_nofire.txt"):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        head, tail = ln.split("|")
        parts = head.split()
        tag = parts[0]
        v = int(parts[1])
        P = [int(t) for t in parts[2:]]
        y, z = [int(t) for t in tail.split()]
        nlines += 1
        chk(tag == "W44a", "certificate %d names the host it is verified against" % nlines)
        chk(ecc[v] == diam, "cert %d: the anchor v=%d has ecc = diam" % (nlines, v))
        chk(P[0] == v, "cert %d: the geodesic starts at the anchor" % nlines)
        chk(len(P) - 1 == ecc[v], "cert %d: P has ecc(v)+1 vertices" % nlines)
        chk(D[v][P[-1]] == ecc[v], "cert %d: P ends at a far end of v" % nlines)
        chk(all(D[v][P[i]] == i for i in range(len(P))), "cert %d: P is a geodesic" % nlines)
        chk(induced_path(nb, P + [y, z]),
            "cert %d: the frame u_0..u_d y z is an INDUCED path" % nlines)
        chk(not fires(nb, P, z),
            "cert %d: (TAIL-3'') does NOT fire (true alpha used, not the matching bound)"
            % nlines)
        chk(k3(nb, P, z) >= 1, "cert %d: k3 >= 1" % nlines)
        deg = bin(nb[z]).count("1")
        chk(deg == k3(nb, P, z) + 1,
            "cert %d: (HUG-EQ) deg(z) = k3(z)+1 exactly (deg=%d, k3=%d)"
            % (nlines, deg, k3(nb, P, z)))
    print("  W44a non-firing certificates re-checked: %d" % nlines)
    chk(nlines == 11, "all 11 claimed W44a non-firing frames are present")
    zs = set()
    for ln in open("problems/wowii/w133_r46_nofire.txt"):
        if ln.startswith("#") or not ln.strip():
            continue
        zs.add(int(ln.split("|")[1].split()[1]))
    print("  distinct step-3 vertices among them: %s (degree %s)"
          % (sorted(zs), [bin(nb[t]).count("1") for t in sorted(zs)]))

    print("CHECKS %d   FAILS %d" % (CH[0], CH[1]))
    return 1 if CH[1] else 0


if __name__ == "__main__":
    sys.exit(main())
