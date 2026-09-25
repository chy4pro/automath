#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 owner round 46, SLICE 2 -- (ROW-BUDGET): the witnesses have to FIT.

(HUG-DEG) said the k3 witnesses of ONE step-3 vertex are pairwise distinct.  The same
C4-freeness says more: the witnesses of DIFFERENT step-3 vertices hanging off the SAME y are
distinct too, because two of them sharing a witness c would give c and y two common
neighbours.  So all the witnesses at a frame live in one small set and have to FIT in it.
That is a COUNTING closure test -- the first on this line that is not a per-vertex test.

  (ROW-BUDGET).  H C4-free and TRIANGLE-FREE, (v, P = u_0..u_d, y) a (TAIL-1) frame at a
  vertex v with ecc(v) = diam(H).  Let Z(y) be the admissible step-3 vertices and
        B := ( N(u_{d-1}) u N(u_{d-2}) u N(u_{d-3}) u N(u_{d-4}) ) \\ P      (the BUDGET).
  Then      SUM over z in Z(y) of k3(z)   <=   |B|.
  Consequently, if  SUM over z in Z(y) of (deg(z) - 1)  >  |B|,  then some z in Z(y) has
  deg(z) >= 2 + k3(z), so (TAIL-3'') FIRES there and -- by (ROW-LADDER) at j = 3 -- the
  offset-+1 instance is CLOSED.

DIRECTION OF ERROR, FIXED BEFORE THE NUMBERS (129).  Frames are enumerated EXHAUSTIVELY per
host (every diametral vertex, every geodesic, every admissible y), so `the budget test fires
at this frame' is SOUND and `it fires nowhere on this host' is also sound.  What is sampled
is the HOST LIST, so `no host escapes' would be inconclusive -- and this file's headline is
what the test FAILS to close, which is the sound direction.

Pure stdlib, system python3.  No SAT, no exhaustive search over a large space.
Primitives COPIED VERBATIM from w133_r46_hug.py.
"""
from __future__ import print_function
import sys
import time
from collections import deque
from itertools import combinations

sys.setrecursionlimit(100000)
T0 = time.time()
CHECKS = 0
FAILS = 0


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


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
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def triangle_free(g):
    for u in range(len(g)):
        for v in g[u]:
            if v > u and (g[u] & g[v]):
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
    return D, ecc, min(ecc)


def l_of(g):
    return sum(a_val_matching(g, v) for v in range(len(g))) / float(len(g))


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


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


def geodesics(D, g, w, x, cap):
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


def tail1_frames(g, D, w, x, ngeo):
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
    d = len(P) - 1
    k = 0
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0 and (g[z] & g[P[j]]):
            k += 1
    return k


def witnesses(g, P, z):
    """the actual witness set: one chosen c per firing index."""
    d = len(P) - 1
    W = []
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0 and (g[z] & g[P[j]]):
            W.append(sorted(g[z] & g[P[j]])[0])
    return W


def budget_set(g, P):
    d = len(P) - 1
    B = set()
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0:
            B |= g[P[j]]
    return B - set(P)


def hosts():
    H = []
    for tag, fn in (("W43a", "problems/wowii/w133_r43_W43a.txt"),
                    ("W43b", "problems/wowii/w133_r43_W43b.txt"),
                    ("W43c", "problems/wowii/w133_r43_W43c.txt"),
                    ("W44a", "problems/wowii/w133_r44_W44a.txt")):
        try:
            H.append((tag, load_txt(fn)))
        except IOError:
            pass
    H.append(("Petersen", petersen()))
    for L in (7, 8, 9, 11, 13):
        H.append(("C%d" % L, cycle(L)))
    for q in (2, 3, 5):
        H.append(("PG(2,%d)inc" % q, pg2(q)))
    S = sorted(combinations(range(7), 3))
    idx = {s: i for i, s in enumerate(S)}
    H.append(("O4=K(7,3)", adj(len(S), [(idx[a], idx[b]) for a, b in combinations(S, 2)
                                        if not (set(a) & set(b))])))
    P = petersen()
    E = []
    for (u, v) in edges_of(P):
        E.append((u, 10 + v))
        E.append((v, 10 + u))
    H.append(("Desargues", adj(20, E)))
    pap = [(i, (i + 1) % 18) for i in range(18)]
    pap += [(0, 5), (6, 11), (12, 17), (2, 9), (8, 15), (14, 3)]
    H.append(("Pappus", adj(18, pap)))
    cox = []
    for k in (1, 2, 3):
        for i in range(7):
            cox.append((7 * (k - 1) + i, 7 * (k - 1) + (i + k) % 7))
    for i in range(7):
        cox.append((21 + i, i))
        cox.append((21 + i, 7 + i))
        cox.append((21 + i, 14 + i))
    H.append(("Coxeter", adj(28, cox)))
    for (nn, kk, nm) in ((8, 3, "MoebiusKantor"), (12, 5, "Nauru"), (10, 2, "Dodecahedron"),
                         (11, 3, "GP(11,3)"), (13, 5, "GP(13,5)")):
        E = [(i, (i + 1) % nn) for i in range(nn)]
        E += [(i, nn + i) for i in range(nn)]
        E += [(nn + i, nn + (i + kk) % nn) for i in range(nn)]
        H.append((nm, adj(2 * nn, E)))
    out = []
    for (tag, g) in H:
        ck(connected(g), "host %s connected" % tag)
        ck(c4_free(g), "host %s C4-free -- ASSERTED, not assumed" % tag)
        ck(triangle_free(g), "host %s TRIANGLE-FREE -- (ROW-BUDGET)'s own hypothesis, "
                             "asserted before it is used" % tag)
        if connected(g) and c4_free(g) and triangle_free(g):
            out.append((tag, g))
    return out


def main():
    print("w133 round 46 slice 2 -- (ROW-BUDGET).  system python3, pure stdlib, no SAT.")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print(__doc__)
    print("""
  PROOF.  Let z, z' be distinct members of Z(y) and c a witness of both.  Then c and y have
  the two common neighbours z and z' -- a C4.  So witnesses of different z are distinct.
  Within one z they are distinct by (HUG-DEG) (H is triangle-free).  Every witness c is
  adjacent to some u_j with j in {d-1,..,d-4}, and c is not a path vertex, because c ~ z and
  z !~ u_i for every i.  So the whole collection injects into B, and |collection| =
  SUM_z k3(z) <= |B|.  For the consequence: if every z had deg(z) <= 1 + k3(z), then
  SUM_z (deg(z)-1) <= SUM_z k3(z) <= |B|, contradicting the hypothesis. []

  (P1) PREDICTION, registered BEFORE the run: SUM_z k3(z) <= |B| at EVERY frame of EVERY
       triangle-free host below.  0 violations.
  (P2) PREDICTION: at every frame where SUM_z (deg(z)-1) > |B|, an explicitly FIRING z is
       found.  0 failures to find one.
  (P3) PREDICTION, the one that can embarrass this lane: the budget test fires at NO frame
       of Petersen, C7 or C8 -- the three hosts round 46 slice 1 showed have N(H) = 0.  If
       it fired there it would be unsound.
""")
    HS = hosts()
    print("  hosts kept (connected, C4-free, TRIANGLE-FREE): %d" % len(HS))
    v1 = 0
    v2 = 0
    nfr = 0
    rows = []
    for (tag, g) in HS:
        D, ecc, r = profile(g)
        diam = max(ecc)
        nf = 0
        nclose = 0
        best = None
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            e = ecc[v]
            for x in [u for u in range(len(g)) if D[v][u] == e]:
                for (P, y) in tail1_frames(g, D, v, x, 10 ** 9):
                    Q = P + [y]
                    if len(Q) != e + 2:
                        continue
                    Z = [z for z in extend_once(g, Q, v) if len(Q) + 1 == e + 3]
                    if not Z:
                        continue
                    nf += 1
                    nfr += 1
                    B = budget_set(g, P)
                    sk = sum(k3_of(g, P, z) for z in Z)
                    sd = sum(len(g[z]) - 1 for z in Z)
                    # (P1): the counting bound itself
                    allw = []
                    for z in Z:
                        allw.extend(witnesses(g, P, z))
                    if len(allw) != len(set(allw)) or not set(allw) <= B:
                        v1 += 1
                    if sk > len(B):
                        v1 += 1
                    # (P2): the derived closure test
                    slack = len(B) - sd
                    if best is None or slack < best:
                        best = slack
                    if sd > len(B):
                        nclose += 1
                        if not any(max(a_val_matching(g, z), len(g[z]) - 1)
                                   >= 2 + k3_of(g, P, z) for z in Z):
                            v2 += 1
        rows.append((tag, len(g), diam, l_of(g), nf, nclose, best))
    print()
    print("  %-14s %5s %4s %6s %9s %9s %7s %s"
          % ("host", "n", "diam", "l", "frames", "BUDGET", "min", ""))
    print("  %-14s %5s %4s %6s %9s %9s %7s %s"
          % ("", "", "", "", "(with Z)", "closes", "slack", ""))
    for (tag, n, diam, lg, nf, nclose, best) in rows:
        print("  %-14s %5d %4d %6.3f %9d %9d %7s   %s"
              % (tag, n, diam, lg, nf, nclose, "-" if best is None else best,
                 "" if nf else "(no frame carries a step-3 vertex)"))
    ck(v1 == 0, "(P1): SUM_z k3(z) <= |B| at every frame, witnesses distinct and inside B")
    ck(v2 == 0, "(P2): every frame the budget test closes really does carry a firing z")
    tot = sum(r[4] for r in rows)
    clo = sum(r[5] for r in rows)
    print()
    print("  (P1) VERDICT: %s  (%d violations of the counting bound)"
          % ("HELD" if v1 == 0 else "FAILED", v1))
    print("  (P2) VERDICT: %s  (%d frames closed with no firing z found)"
          % ("HELD" if v2 == 0 else "FAILED", v2))
    bad3 = [r for r in rows if r[0] in ("Petersen", "C7", "C8") and r[5] > 0]
    ck(not bad3, "(P3): the budget test fires at NO frame of Petersen / C7 / C8")
    print("  (P3) VERDICT: %s  (%s)"
          % ("HELD" if not bad3 else "FAILED",
             "the three N(H)=0 hosts are untouched" if not bad3
             else ", ".join(r[0] for r in bad3)))
    print()
    print("  ---- WHAT (ROW-BUDGET) FAILS TO CLOSE (item (b)) ----")
    print("  frames carrying a step-3 vertex: %d ; closed by the budget test: %d (%.1f%%)"
          % (tot, clo, 100.0 * clo / tot if tot else 0.0))
    print("  frames it does NOT close: %d (%.1f%%).  It is a COUNTING test and it is far"
          % (tot - clo, 100.0 * (tot - clo) / tot if tot else 0.0))
    print("  from closing everything -- which is the point: it DISCRIMINATES.")
    nz = [r for r in rows if r[4] > 0 and r[5] == 0]
    print("  hosts it closes NOTHING on: %d -- %s"
          % (len(nz), ", ".join(r[0] for r in nz) if nz else "(none)"))
    print()
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
