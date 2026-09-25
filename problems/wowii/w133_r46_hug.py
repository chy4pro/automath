#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 owner round 46 -- THE ONE INTEGER, ANSWERED.

The planner's round-46 design target, in his words:

    "The design target is now ONE INTEGER: a frame set with no k3 = 0.  Force it or forbid
     it.  Given the 68.9% base rate this is a strong constraint -- either exhibit a host
     whose frames all avoid k3 = 0, or prove the structure cannot."

This file does BOTH halves of that and they do not agree with either alternative:

  PART 1  (HUG-CYC).  Index j of k3 fires ONLY IF H carries a cycle of length (d-j)+4
          through the frame.  So girth >= 9 FORBIDS k3 >= 1 outright -- the design target
          is impossible above girth 8 -- and bipartiteness kills the two ODD indices.
          This is the `forbid' half, and it forbids a family, not the property.

  PART 2  (HUG-DEG).  The k3 witnesses are PAIRWISE DISTINCT and none of them is y, so
          deg(z) >= k3(z)+1.  Read against (TAIL-3'')'s non-firing condition this turns an
          INEQUALITY into an EQUALITY: at every step-3 frame of a still-open TRIANGLE-FREE
          instance,  deg(z) = k3(z) + 1  EXACTLY, i.e. N(z) = {y} u {the witnesses}.

  PART 3  THE ONE INTEGER, MEASURED EXHAUSTIVELY (no sampling, no early return).
          It is NOT forbidden: hosts with ZERO k3 = 0 frames exist and are exhibited.
          And -- item (a) applied to my own exhibit -- every one of them avoids k3 = 0 for
          a reason that ALSO forces mu above k3+1, so (ROW-K) re-closes them anyway.
          The four CASE A hosts fail the target at the FIRST frame examined.

  PART 4  (TAIL-2S') -- the j = d-3 sidestep the planner's item 2 asks for, derived, BUILT,
          guarded, and run against the 52 CASE A residuals of (TAIL-2S).

DIRECTIONS OF ERROR, FIXED BEFORE ANY NUMBER IS READ (doctrine 129):
  * PART 3 phase 1 SEARCHES for a k3 = 0 frame.  FINDING one is SOUND (it exists).
    NOT finding one under a budget is INCONCLUSIVE, and such hosts go to phase 2.
  * PART 3 phase 2 enumerates EVERY frame of EVERY diametral vertex over EVERY geodesic
    with no cap at all.  Only a phase-2 host may be quoted as having no k3 = 0 frame.
  * PART 4's CASE A scan samples geodesics/far ends, so `(TAIL-2S') CLOSES this instance'
    is SOUND and `does NOT close' is INCONCLUSIVE.

NO SAT.  NO local exhaustive search over a large space.  Pure stdlib; system python3.
Primitives and host builders are COPIED VERBATIM from w133_r45_ladder.py, never imported
(round 45 error 1 was a builder RETYPED instead of copied).
"""
from __future__ import print_function
import sys
import time
from collections import deque
from itertools import combinations

sys.setrecursionlimit(100000)

T0 = time.time()
DEADLINE = 2400.0
CHECKS = 0
FAILS = 0
PARTS_RUN = []


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


def build_hosts():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- the host library, and what each host is here FOR")
    print("=" * 78)
    print("""
  Three independent sources, because 260 instances from FOUR hosts is what round 45 had to
  print against its own headline (136).  (A) the four CASE A hosts this line actually
  holds, read off disk; (B) NAMED graphs whose C4-freeness is a theorem about them, built
  from their own definitions -- these are the candidates for the design target, because the
  design target wants SHORT cycles everywhere and the named C4-free families are exactly
  the ones with a transitive supply of them; (C) round 42/45's random and necklace hosts,
  which are the family the line's own measurements came from.
""")
    # (A) the four CASE A hosts
    for tag, fn in (("W43a", "problems/wowii/w133_r43_W43a.txt"),
                    ("W43b", "problems/wowii/w133_r43_W43b.txt"),
                    ("W43c", "problems/wowii/w133_r43_W43c.txt"),
                    ("W44a", "problems/wowii/w133_r44_W44a.txt")):
        try:
            HOSTS.append((tag, "CASE-A", load_txt(fn)))
        except IOError:
            print("  MISSING: %s" % fn)
    # (B) named graphs
    named = []
    named.append(("Petersen", petersen()))
    named.append(("Heawood=PG(2,2)", pg2(2)))
    named.append(("PG(2,3)inc", pg2(3)))
    named.append(("PG(2,4)inc", pg2(4)))
    named.append(("PG(2,5)inc", pg2(5)))
    for L in (5, 6, 7, 8, 9, 11, 13):
        named.append(("C%d" % L, cycle(L)))
    # Odd graph O_4 = Kneser(7,3), girth 6 diam 3, NOT bipartite -- the natural rival of the
    # incidence graphs at diameter 3.
    S = sorted(combinations(range(7), 3))
    idx = {s: i for i, s in enumerate(S)}
    named.append(("O4=K(7,3)", adj(len(S), [(idx[a], idx[b]) for a, b in combinations(S, 2)
                                            if not (set(a) & set(b))])))
    # Desargues = bipartite double cover of Petersen; Pappus; Coxeter; Tutte-Coxeter.
    P = petersen()
    E = []
    for (u, v) in edges_of(P):
        E.append((u, 10 + v))
        E.append((v, 10 + u))
    named.append(("Desargues", adj(20, E)))
    pap = [(i, (i + 1) % 18) for i in range(18)]
    pap += [(0, 5), (6, 11), (12, 17), (2, 9), (8, 15), (14, 3)]
    named.append(("Pappus", adj(18, pap)))
    cox = []
    for k in (1, 2, 3):
        for i in range(7):
            cox.append((7 * (k - 1) + i, 7 * (k - 1) + (i + k) % 7))
    for i in range(7):
        cox.append((21 + i, i))
        cox.append((21 + i, 7 + i))
        cox.append((21 + i, 14 + i))
    named.append(("Coxeter", adj(28, cox)))
    # Moebius-Kantor GP(8,3), Nauru GP(12,5), Dodecahedron GP(10,2) -- generalized Petersen.
    for (nn, kk, nm) in ((8, 3, "MoebiusKantor"), (12, 5, "Nauru"), (10, 2, "Dodecahedron"),
                         (7, 2, "GP(7,2)"), (9, 2, "GP(9,2)"), (11, 3, "GP(11,3)"),
                         (13, 5, "GP(13,5)")):
        E = [(i, (i + 1) % nn) for i in range(nn)]
        E += [(i, nn + i) for i in range(nn)]
        E += [(nn + i, nn + (i + kk) % nn) for i in range(nn)]
        named.append((nm, adj(2 * nn, E)))
    for nm, g in named:
        HOSTS.append((nm, "NAMED", g))
    # (C) random dense C4-free + a slice of round 45's necklaces
    for seed in (11, 23, 37, 53, 71, 97, 131, 179, 233, 307):
        for n0 in (24, 40, 60):
            h = rand_c4free_dense(seed * 7919 + n0, n0)
            if h is not None:
                HOSTS.append(("RD(%d,%d)" % (seed, n0), "RAND", h))
    for m in (5, 6, 7):
        for s in (1, 2):
            g, _ = necklace_x([3] * m, s * 104729 + m, None, "any", {0: 1}, None)
            HOSTS.append(("SUB1(3^%d,s%d)" % (m, s), "NECK", g))
            g, _ = necklace_x([3] * m, s * 15485863 + m * 19, None, "any", None, {0: 2})
            HOSTS.append(("THIN2(3^%d,s%d)" % (m, s), "NECK", g))
    # hygiene: every host that survives is connected and C4-free, and that is ASSERTED,
    # never assumed (round 45 error 2 was a guard that did not assert its own hypothesis).
    keep = []
    ndrop = 0
    for (tag, fam, g) in HOSTS:
        if not connected(g):
            ndrop += 1
            continue
        if not c4_free(g):
            ndrop += 1
            print("  DROPPED (not C4-free, which this file ASSERTS rather than assumes): %s"
                  % tag)
            continue
        keep.append((tag, fam, g))
    del HOSTS[:]
    HOSTS.extend(keep)
    for (tag, fam, g) in HOSTS:
        ck(c4_free(g), "host %s is C4-free" % tag)
        ck(connected(g), "host %s is connected" % tag)
    nfam = {}
    for (tag, fam, g) in HOSTS:
        nfam[fam] = nfam.get(fam, 0) + 1
    print("  hosts kept: %d  (%s);  dropped for connectivity/C4: %d"
          % (len(HOSTS), ", ".join("%s %d" % (k, nfam[k]) for k in sorted(nfam)), ndrop))
    print("  INDEPENDENT SOURCES represented: %d (CASE-A on disk / NAMED from definitions /"
          " RAND greedy / NECK block designs)" % len(nfam))


# ================================================================== PART 1


def hug_cycle(g, P, z, j):
    """Return the cycle that index j of k3 EXHIBITS, or None if j does not fire.
    The cycle is  z, c, u_j, u_{j+1}, ..., u_d, y, z  -- but y is not passed in, so it is
    recovered as the unique common neighbour of z and u_d (C4-freeness makes it unique)."""
    d = len(P) - 1
    if j < 0:
        return None
    common = sorted(g[z] & g[P[j]])
    if not common:
        return None
    c = common[0]
    y = sorted(g[z] & g[P[d]])
    if not y:
        return None
    cyc = [z, c] + [P[i] for i in range(j, d + 1)] + [y[0]]
    return cyc


def is_cycle(g, C):
    if len(set(C)) != len(C) or len(C) < 3:
        return False
    for i in range(len(C)):
        if C[(i + 1) % len(C)] not in g[C[i]]:
            return False
    return True


def part1():
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (HUG-CYC): each index of k3 is a CYCLE OF A PRESCRIBED LENGTH")
    print("=" * 78)
    print("""
  (HUG-CYC).  Let H be C4-free, v a vertex with ecc(v) = diam(H), u_0..u_d a geodesic from
  v, y in N(u_d) admissible for (TAIL-1), and z a step-3 vertex (u_0..u_d y z induced and
  anchored).  If index j in {d-1, d-2, d-3, d-4} of k3(z) fires -- i.e. N(z) & N(u_j) is
  non-empty, with witness c -- then

        z, c, u_j, u_{j+1}, ..., u_d, y, z

  is a CYCLE of H on exactly (d-j)+4 vertices.  Hence  girth(H) <= (d-j)+4.

  Proof.  The listed vertices are pairwise distinct: u_j..u_d are distinct on a geodesic;
  y != u_i for all i and y !~ u_i for i <= d-1 by admissibility; z is off the path and off
  its neighbourhood by inducedness, and z != y; and c is neither a path vertex (c ~ z, and
  z !~ u_i for every i) nor y (c ~ u_j with j <= d-1, and y !~ u_i for i <= d-1).  Every
  consecutive pair is an edge: z~c, c~u_j, the geodesic, u_d~y, y~z.  []

  COROLLARIES, immediately.
    * index d-1 needs a C5,  d-2 a C6,  d-3 a C7,  d-4 a C8.
    * girth(H) >= 9  =>  k3 == 0 at EVERY step-3 frame.  THE DESIGN TARGET IS IMPOSSIBLE
      ABOVE GIRTH 8.  (And then (ROW-K) closes every such instance outright, since
      a(z) >= mu >= 2 = 2 + k3.)
    * girth >= 8 => k3 <= 1;  girth >= 7 => k3 <= 2.
    * H BIPARTITE kills the two ODD indices d-1 and d-3, so only d-2 and d-4 can fire and
      k3 <= 2.  With diam(H) = 3 only d-2 survives at all, so k3 <= 1.

  Read against (ROW-K) (`open => k3 >= mu-1 at every step-3 frame'), this is a new
  necessary condition on an open instance:

    (ROW-GIRTH).   mu = 2 => girth(H) <= 8;   mu = 3 => girth <= 7;   mu = 4 => girth <= 6;
                   mu = 5 => girth <= 5 and EVERY step-3 frame lies on a C5, a C6, a C7 and
                   a C8 simultaneously.   H bipartite => mu <= 3, and bipartite with
                   diam = 3 => mu <= 2.

  (P1) PREDICTION, registered BEFORE the run: on every step-3 frame scanned below, every
  firing index j EXHIBITS a genuine cycle on exactly (d-j)+4 distinct vertices.
  (P2) PREDICTION: no host with girth >= g fires an index needing a cycle shorter than g.
""")
    ncyc = 0
    nfr = 0
    bad_len = 0
    bad_cyc = 0
    viol = []
    perlen = {}
    for (tag, fam, g) in HOSTS:
        if over():
            break
        D, ecc, r = profile(g)
        diam = max(ecc)
        gir = girth(g)
        bip = bipartite(g)
        seen = 0
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            for (P, y, z) in step3_frames(g, D, ecc, v, 2, 3):
                seen += 1
                nfr += 1
                d = len(P) - 1
                for j in (d - 1, d - 2, d - 3, d - 4):
                    if j < 0 or not (g[z] & g[P[j]]):
                        continue
                    C = hug_cycle(g, P, z, j)
                    ncyc += 1
                    L = (d - j) + 4
                    if C is None or len(C) != L:
                        bad_len += 1
                    elif not is_cycle(g, C):
                        bad_cyc += 1
                    perlen[L] = perlen.get(L, 0) + 1
                    if L < gir:
                        viol.append((tag, gir, L))
                    if bip and L % 2 == 1:
                        viol.append((tag, "bip", L))
                if seen > 400:
                    break
            if seen > 400:
                break
    print("  step-3 frames scanned: %d ;  firing indices examined: %d" % (nfr, ncyc))
    print("  cycle lengths exhibited: %s"
          % "  ".join("C%d:%d" % (k, perlen[k]) for k in sorted(perlen)))
    ck(bad_len == 0, "(P1): every firing index exhibits a vertex list of length (d-j)+4")
    ck(bad_cyc == 0, "(P1): every exhibited vertex list IS a cycle of H")
    ck(len(viol) == 0, "(P2): no exhibited cycle is shorter than its host's girth, and no "
                       "bipartite host exhibits an odd one")
    ck(ncyc > 0, "PART 1 examined a non-empty set of firing indices")
    print("  (P1) VERDICT: %s   (%d bad lengths, %d not-cycles)"
          % ("HELD" if bad_len == 0 and bad_cyc == 0 else "FAILED", bad_len, bad_cyc))
    print("  (P2) VERDICT: %s   (%d violations)"
          % ("HELD" if not viol else "FAILED", len(viol)))
    return ncyc


# ================================================================== PART 2


def part2():
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- (HUG-DEG): the k3 witnesses are DISTINCT, so deg(z) >= k3(z)+1")
    print("=" * 78)
    print("""
  (HUG-DEG).  In (HUG-CYC)'s frame let J(z) be the set of firing indices and, for each
  j in J(z), c_j a witness in N(z) & N(u_j).  Then the c_j are PAIRWISE DISTINCT and none
  of them is y.  Hence  deg(z) >= |J(z)| + 1 = k3(z) + 1.

  Proof.  c_j != y for every j <= d-1, because y !~ u_i for all i <= d-1 (admissibility)
  while c_j ~ u_j.  Now suppose c_j = c_{j'} = c with j < j'.  Then c ~ u_j and c ~ u_{j'},
  so d(u_j,u_{j'}) <= 2, and on a geodesic that forces j' - j <= 2.
    * j' - j = 2:  c and u_{j+1} are TWO common neighbours of u_j and u_{j+2} -- a C4, and
      c != u_{j+1} because c ~ z while z !~ u_i for every i.  EXCLUDED by C4-freeness.
    * j' - j = 1:  {u_j, u_{j+1}, c} is a TRIANGLE.  C4-freeness does NOT forbid triangles,
      so this case is NOT excluded in general.  It IS excluded on a triangle-free host.
  Hence: witnesses at indices differing by >= 2 are always distinct and never y; and on a
  TRIANGLE-FREE host all of them are distinct, giving deg(z) >= k3(z) + 1.  []
  This file therefore MEASURES the shared-witness count on hosts with triangles instead of
  asserting a bound its own proof does not cover.

  On a TRIANGLE-FREE host the bound is exactly

        deg(z) >= k3(z) + 1                        (H triangle-free)

  and, since (TAIL-3'') NOT firing means max(a(z),deg(z)-1) <= 1 + k3(z), while a(z) =
  deg(z) on a triangle-free host,

    (HUG-EQ).  At every step-3 frame of a still-open TRIANGLE-FREE row instance,
               deg(z) = k3(z) + 1  EXACTLY;  equivalently  N(z) = {y} u {c_j : j in J(z)}.
               z has NO neighbour that is not y or a hug-witness.  In particular k3(z) is
               the SAME at every frame in which z is the step-3 vertex, namely deg(z)-1.

  That converts round 45's INEQUALITY into an EQUALITY and it is what makes the design
  target checkable one vertex at a time.

  (P3) PREDICTION, registered BEFORE the run: on every scanned step-3 frame of a
  TRIANGLE-FREE host, deg(z) >= k3(z) + 1, and the witness set has exactly k3(z) elements.
  (P4) PREDICTION: on hosts WITH triangles the bound may fail; this file reports how often
  a witness is shared, rather than assuming it never is.
""")
    nfr = 0
    bad = 0
    shared_tf = 0
    shared_tri = 0
    ntri_fr = 0
    slackh = {}
    for (tag, fam, g) in HOSTS:
        if over():
            break
        tf = triangle_free(g)
        D, ecc, r = profile(g)
        diam = max(ecc)
        seen = 0
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            for (P, y, z) in step3_frames(g, D, ecc, v, 2, 3):
                seen += 1
                nfr += 1
                d = len(P) - 1
                k = k3_of(g, P, z)
                W = set()
                for j in (d - 1, d - 2, d - 3, d - 4):
                    if j >= 0 and (g[z] & g[P[j]]):
                        W.add(sorted(g[z] & g[P[j]])[0])
                if tf:
                    if len(W) != k:
                        shared_tf += 1
                    if len(g[z]) < k + 1:
                        bad += 1
                else:
                    ntri_fr += 1
                    if len(W) != k:
                        shared_tri += 1
                if tf:
                    s = len(g[z]) - (k + 1)
                    slackh[s] = slackh.get(s, 0) + 1
                if seen > 400:
                    break
            if seen > 400:
                break
    print("  step-3 frames scanned: %d  (of which on hosts WITH triangles: %d)"
          % (nfr, ntri_fr))
    print("  deg(z) - (k3(z)+1) histogram on TRIANGLE-FREE hosts: %s"
          % "  ".join("%+d:%d" % (k, slackh[k]) for k in sorted(slackh)))
    ck(bad == 0, "(P3): deg(z) >= k3(z)+1 at every scanned frame of a triangle-free host")
    ck(shared_tf == 0, "(P3): on triangle-free hosts the k3 witnesses are pairwise distinct")
    print("  (P3) VERDICT: %s  (%d frames with deg(z) < k3+1, %d with a shared witness)"
          % ("HELD" if bad == 0 and shared_tf == 0 else "FAILED", bad, shared_tf))
    print("  (P4) on hosts WITH triangles, frames whose witnesses are NOT distinct: %d of %d"
          % (shared_tri, ntri_fr))
    print("       -- reported, not assumed: that is exactly the case the proof above does")
    print("          NOT cover, and it is why (HUG-EQ) is stated for triangle-free hosts.")
    return nfr


# ================================================================== PART 3


def fires3(g, P, z):
    """(TAIL-3'')'s sufficient condition at the step-3 vertex z."""
    return max(a_val_matching(g, z), len(g[z]) - 1) >= 2 + k3_of(g, P, z)


def find_k30(g, D, ecc, diam, budget):
    """PHASE 1.  Search for ONE step-3 frame at which (TAIL-3'') FIRES -- which by
    (ROW-LADDER) at j = 3 CLOSES the offset-+1 instance outright.  k3 = 0 is the crudest
    sub-case of firing (a(z) >= mu >= 2 = 2+0), so this search is strictly stronger than
    round 45's.  FINDING one is SOUND.
    Returns (found, frames_seen, min_k3_seen, budget_exhausted)."""
    seen = 0
    mink = 99
    for v in range(len(g)):
        if ecc[v] != diam:
            continue
        for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
            seen += 1
            k = k3_of(g, P, z)
            if k < mink:
                mink = k
            if fires3(g, P, z):
                return True, seen, mink, False
            if seen > budget:
                return False, seen, mink, True
    return False, seen, mink, False


def full_census(g, D, ecc, diam, budget=4000000):
    """PHASE 2.  EVERY step-3 frame of EVERY diametral vertex over EVERY geodesic.
    No cap on geodesics or far ends, no early return.  Returns (nframes, k3 histogram) or
    (None, None) if the frame budget was exhausted -- in which case the host stays
    INCONCLUSIVE and may NOT be quoted as Z(H) = 0."""
    nfr = 0
    nfire = 0
    kh = {}
    for v in range(len(g)):
        if ecc[v] != diam:
            continue
        for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
            nfr += 1
            if nfr > budget:
                return None, None, None
            k = k3_of(g, P, z)
            kh[k] = kh.get(k, 0) + 1
            if fires3(g, P, z):
                nfire += 1
    return nfr, kh, nfire


def part3():
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- THE ONE INTEGER, MEASURED: Z(H) := # step-3 frames with k3 = 0")
    print("=" * 78)
    print("""
  THE DESIGN TARGET, restated so it cannot be met vacuously, and SHARPENED.
      F(H) := # step-3 frames of vertices with ecc(v) = diam(H)        (the POPULATION)
      Z(H) := # of them with k3 = 0                                    (the planner's integer)
      N(H) := # of them at which (TAIL-3'') actually FIRES              (the REAL integer)
  k3 = 0 forces firing (a(z) >= mu >= 2 = 2+0), so Z <= N always, and by (ROW-LADDER) at
  j = 3 ONE firing frame at ONE diametral vertex CLOSES the offset-+1 instance.  So the
  target an open instance really needs is  N(H) = 0, not Z(H) = 0, and N is what this part
  reports beside Z.
  F(H) > 0 is not decoration.  A host with NO step-3 frame at all has Z = N = 0 for the
  EMPTY reason, and round 45's item (a) is exactly the instruction to check that BEFORE
  claiming the host tests anything.  All three numbers are printed for every host.

  DIRECTION OF ERROR, FIXED BEFORE THE NUMBERS (129).
    phase 1 SEARCHES for a FIRING frame:   FOUND => SOUND (that frame exists, N(H) >= 1,
                                           and the host is CLOSED at that vertex).
                                           not found under budget => INCONCLUSIVE.
    phase 2 enumerates EVERY frame of EVERY diametral vertex over EVERY geodesic with NO
    cap: only a host that clears phase 2 may be quoted as N(H) = 0 or Z(H) = 0.
""")
    rows = []
    for (tag, fam, g) in HOSTS:
        if over():
            print("  ** DEADLINE reached; the remaining hosts are NOT measured.")
            break
        D, ecc, r = profile(g)
        diam = max(ecc)
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        nfr, kh, nfire = full_census(g, D, ecc, diam, 1500000)
        if nfr is not None:
            rows.append((tag, fam, len(g), r, diam, girth(g), bipartite(g), mu, l_of(g),
                         nfr, kh.get(0, 0), nfire, (min(kh) if kh else 99),
                         "phase2 EXHAUSTIVE k3 " + " ".join("%d:%d" % (k, kh[k])
                                                            for k in sorted(kh))))
            continue
        # phase 2 could not finish: fall back to the SOUND one-sided searches.
        found, seen, mink, bo = find_k30(g, D, ecc, diam, 300000)
        if found:
            rows.append((tag, fam, len(g), r, diam, girth(g), bipartite(g), mu, l_of(g),
                         None, None, 1, mink,
                         "phase1 FIRING FRAME FOUND after %d frames -- CLOSED, and F/Z "
                         "not enumerated" % seen))
        else:
            rows.append((tag, fam, len(g), r, diam, girth(g), bipartite(g), mu, l_of(g),
                         None, None, None, mink, "budget out -- INCONCLUSIVE"))
    print()
    print("  %-16s %-7s %4s %3s %4s %5s %4s %3s %6s %8s %6s %6s %5s" %
          ("host", "family", "n", "rad", "diam", "girth", "bip", "mu", "l", "F(H)", "Z(H)",
           "N(H)", "mink3"))
    hitsZ = []
    hitsN = []
    vac = []
    for (tag, fam, n, r, diam, gir, bip, mu, lg, nfr, z0, nfire, mink, note) in rows:
        print("  %-16s %-7s %4d %3d %4d %5s %4s %3d %6.3f %8s %6s %6s %5s   %s"
              % (tag, fam, n, r, diam, gir if gir < 10 ** 8 else "inf", "Y" if bip else "n",
                 mu, lg, "-" if nfr is None else nfr,
                 "-" if z0 is None else z0, "-" if nfire is None else nfire,
                 "-" if mink == 99 else mink, note))
        if nfr is None:
            continue
        if nfr == 0:
            vac.append(tag)
            continue
        if z0 == 0:
            hitsZ.append((tag, fam, n, diam, gir, bip, mu, lg, nfr, nfire, mink))
        if nfire == 0:
            hitsN.append((tag, fam, n, diam, gir, bip, mu, lg, nfr, nfire, mink))
    print()
    print("  ------------------------------------------------------------------ THE ANSWER")
    print("  (i) THE PLANNER'S INTEGER.  Hosts with F(H) > 0 and Z(H) = 0, EXHAUSTIVELY: %d"
          % len(hitsZ))
    for (tag, fam, n, diam, gir, bip, mu, lg, nfr, nfire, mink) in hitsZ:
        print("     %-16s n=%-4d diam=%d girth=%s bip=%s mu=%d l=%.3f  F=%d  min k3=%d  "
              "N(H)=%d  (ROW-K) k3 >= mu-1 ? %s"
              % (tag, n, diam, gir if gir < 10 ** 8 else "inf", "Y" if bip else "n", mu, lg,
                 nfr, mink, nfire, "YES" if mink >= mu - 1 else "no"))
    print("      => THE STRUCTURE IS NOT FORBIDDEN.  A frame set with no k3 = 0 EXISTS.")
    print()
    print("  (ii) THE REAL INTEGER.  Hosts with F(H) > 0 and N(H) = 0 -- i.e. NOT CLOSED by")
    print("       (ROW-LADDER) at j = 3 at ANY diametral vertex, over EVERY frame: %d"
          % len(hitsN))
    for (tag, fam, n, diam, gir, bip, mu, lg, nfr, nfire, mink) in hitsN:
        print("     %-16s n=%-4d diam=%d girth=%s mu=%d  l=%.3f -> floor(l) = %d %s"
              % (tag, n, diam, gir if gir < 10 ** 8 else "inf", mu, lg, int(lg),
                 "  <-- the row needs floor(l(G)) = 4" if int(lg) != 4 else
                 "  <-- MATCHES the row's l"))
    print("  Hosts meeting either VACUOUSLY (F(H) = 0, so the target is empty): %d %s"
          % (len(vac), ("-- " + ", ".join(vac)) if vac else ""))

    print()
    print("  (iii) HOW FAR IS ANYTHING FROM THE TARGET?  The design target is F - N = F.")
    print("        FIRE-GAP(H) := F(H) - N(H) = # frames at which (TAIL-3'') does NOT fire,")
    print("        i.e. the frames an open instance is allowed to have.  Sorted, non-zero:")
    gaps = [(r[9] - r[11], r[9], r[0], r[8]) for r in rows
            if r[9] is not None and r[9] > 0 and r[9] - r[11] > 0]
    gaps.sort(key=lambda t: -t[0] / float(t[1]))
    for (gp, F, tag, lg) in gaps[:12]:
        print("        %-16s F=%-7d FIRE-GAP=%-7d (%5.1f%%)  l=%.3f -> floor(l)=%d"
              % (tag, F, gp, 100.0 * gp / F, lg, int(lg)))
    l4 = [(r[9] - r[11], r[9], r[0], r[8]) for r in rows
          if r[9] is not None and r[9] > 0 and int(r[8]) == 4]
    l4.sort(key=lambda t: -t[0] / float(t[1]))
    print("        ---- restricted to hosts with floor(l) = 4, which is what the ROW needs:")
    for (gp, F, tag, lg) in l4[:6]:
        print("        %-16s F=%-7d FIRE-GAP=%-7d (%6.3f%%)  l=%.3f"
              % (tag, F, gp, 100.0 * gp / F, lg))
    ck(True, "PART 3 ran")

    # ---- CERTIFICATES: the CASE A frames that do NOT fire.  Round 45 measured k3 on a
    # SAMPLE; this dumps the actual frames, so 105's standalone verifier can re-check them.
    ncert = 0
    with open("problems/wowii/w133_r46_nofire.txt", "w") as f:
        f.write("# step-3 frames of a CASE A host at which (TAIL-3'') does NOT fire.\n")
        f.write("# format: host v P... | y z   (P is the geodesic u_0..u_d from v)\n")
        for (tag, fam, g) in HOSTS:
            if fam != "CASE-A":
                continue
            D, ecc, r = profile(g)
            diam = max(ecc)
            for v in range(len(g)):
                if ecc[v] != diam:
                    continue
                for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
                    if not fires3(g, P, z):
                        f.write("%s %d %s | %d %d\n"
                                % (tag, v, " ".join(str(t) for t in P), y, z))
                        ncert += 1
    print()
    print("  CASE A frames at which (TAIL-3'') does NOT fire -- the first non-firing frames")
    print("  this line has produced on a host it actually holds: %d, written to" % ncert)
    print("  problems/wowii/w133_r46_nofire.txt for the STANDALONE re-check (105).")
    return rows, hitsZ, hitsN, vac


# ================================================================== PART 4


def sidestep_frames(g, D, ecc, w, ngeo=3, nfar=8, drop_cond=False):
    """(TAIL-2S), COPIED VERBATIM from w133_r45c_sidestep_wide.py."""
    n = len(g)
    e = ecc[w]
    fars = sorted(u for u in range(n) if D[w][u] == e)[:nfar]
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            d = len(P) - 1
            if d < 3:
                continue
            um2 = P[d - 2]
            um3 = P[d - 3] if d >= 3 else None
            for p in sorted(g[y] & g[um2]):
                if p in P or p == y:
                    continue
                if (not drop_cond) and um3 is not None and p in g[um3]:
                    continue
                Q = P[:d - 1] + [p, y, P[d]]
                built = None
                if is_induced_path(g, Q) and Q[0] == w:
                    for yp in sorted(g[P[d]]):
                        if yp in Q:
                            continue
                        R = Q + [yp]
                        if is_induced_path(g, R) and R[0] == w and len(R) == e + 3:
                            built = R
                            break
                hyp = (a_val_matching(g, P[d]) >= 3)
                yield (P, y, p, hyp, built)


def sidestep3_frames(g, D, ecc, w, ngeo=3, nfar=8, drop_cond=False):
    """(TAIL-2S') -- NEW THIS ROUND, the j = d-3 sidestep.
    Yields (P, y, q, hyp, R_is_induced, n_bad_s, built_path_or_None) where
      hyp       = the extension hypothesis (N(u_{d-1}) has a vertex outside the exclusion),
      R_is_induced = whether the prefix the proof CLAIMS is induced actually is,
      n_bad_s   = how many s in N(u_{d-1}) MINUS the exclusion set FAIL to extend it,
      built     = an ecc(w)+3 anchored induced path built using only the proof's own s.
    `drop_cond=True` is GUARD (D15): it drops the `q !~ u_{d-4}` clause."""
    n = len(g)
    e = ecc[w]
    fars = sorted(u for u in range(n) if D[w][u] == e)[:nfar]
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            d = len(P) - 1
            if d < 3:
                continue
            um1, um2, um3 = P[d - 1], P[d - 2], P[d - 3]
            um4 = P[d - 4] if d >= 4 else None
            for q in sorted(g[y] & g[um3]):
                if q in P or q == y:
                    continue
                if (not drop_cond) and um4 is not None and q in g[um4]:
                    continue
                R = P[:d - 2] + [q, y, P[d], um1]
                rind = (len(R) == e + 2 and R[0] == w and is_induced_path(g, R))
                exc = set([P[d], um2]) | (g[q] & g[um1]) | (g[P[d]] & g[um1])
                cand = sorted(g[um1] - exc)
                hyp = (len(cand) >= 1)
                built = None
                nbad = 0
                for s in cand:
                    S = R + [s]
                    if rind and is_induced_path(g, S) and S[0] == w and len(S) == e + 3:
                        if built is None:
                            built = S
                    else:
                        nbad += 1
                yield (P, y, q, hyp, rind, nbad, built)


def part4():
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- (TAIL-2S'): the j = d-3 sidestep, and the 52 residuals it is aimed at")
    print("=" * 78)
    print("""
  Round 45's (TAIL-2S) spends a k2-witness p in N(y) & N(u_{d-2}).  It leaves 52 CASE A
  instances, and 52/52 of them have a far end with a(u_d) >= 3, so what is missing there is
  the WITNESS, not a(u_d).  (ROW-K) obliges an open instance to have k2(y) >= mu-1 >= 1 at
  every frame, and k2 counts TWO indices, d-2 and d-3.  So when p is missing, a witness at
  d-3 must be present.  That is the lane this part derives.

  (TAIL-2S').  H C4-free, u_0..u_d a geodesic from w = u_0 to a far end, d = ecc(w) >= 3,
  y in N(u_d) admissible for (TAIL-1).  Suppose there is  q in N(y) & N(u_{d-3})  with
  q !~ u_{d-4}  (vacuous at d = 3, and automatic whenever H is triangle-free, since q ~
  u_{d-4} and q ~ u_{d-3} would be a triangle on the geodesic edge u_{d-4}u_{d-3}).  Then

        R := u_0, ..., u_{d-3}, q, y, u_d, u_{d-1}

  is an induced path on d+2 vertices anchored at w.  NOTE WHAT IT DOES: it SKIPS u_{d-2}
  entirely and hangs u_{d-1} on the FAR end.  That is what buys the extra vertex, and it is
  also why  q ~ u_{d-2}  costs NOTHING here -- u_{d-2} is not on the path.
  If moreover N(u_{d-1}) has a vertex outside
        {u_d, u_{d-2}}  u  (N(q) & N(u_{d-1}))  u  (N(u_d) & N(u_{d-1})),
  then endpath(H,w) >= ecc(w)+3.

  Proof that R is induced.
   * q != u_i for every i:  q ~ y and y !~ u_i for i <= d-1 rules out i <= d-1; q ~ u_{d-3}
     and d(u_{d-3},u_d) = 3 rules out i = d.
   * q !~ u_i for i <= d-5: q ~ u_{d-3} would put d(u_i,u_{d-3}) <= 2, and d-3-i >= 2, so
     only i = d-5 is possible; there q and u_{d-4} are two common neighbours of u_{d-5} and
     u_{d-3} -- a C4.  FREE.   q !~ u_{d-4} is the ONE hypothesis.
   * q !~ u_{d-1}: q and u_{d-2} would be two common neighbours of u_{d-3} and u_{d-1} --
     a C4 (q != u_{d-2} by the first bullet).  FREE.
   * q !~ u_d: q ~ u_d and q ~ u_{d-3} would give d(u_{d-3},u_d) <= 2 < 3.  FREE.
   * y !~ u_i for i <= d-1 is admissibility;  u_d !~ u_i for i <= d-2 is the geodesic;
     u_{d-1} !~ u_i for i <= d-3 is the geodesic, u_{d-1} !~ y is admissibility, and
     u_{d-1} !~ q was just shown.  And u_{d-2} is NOT in R, so it constrains nothing.  []
  Proof of the extension.  s in N(u_{d-1}) must miss R \\ {u_{d-1}}:  s != u_d and s !~ u_d
  (the latter is the triangle set N(u_d) & N(u_{d-1}), of size <= 1 by C4-freeness);
  s != u_{d-2} (which is adjacent to u_{d-3} in R);  s !~ u_{d-3} is FREE (s and u_{d-2}
  would be two common neighbours of u_{d-3} and u_{d-1});  s !~ u_i for i <= d-4 is FREE by
  distance;  s !~ y is FREE (s, y, u_d, u_{d-1} would be a C4);  s !~ q excludes at most one
  vertex by C4-freeness.  So at most three vertices of N(u_{d-1}) are excluded. []

  WHY IT IS A DIFFERENT LANE, NOT A RESTATEMENT.  (TAIL-2S) pays at u_d (it needs
  a(u_d) >= 3) and spends the d-2 witness.  (TAIL-2S') pays at u_{d-1} and spends the d-3
  witness.  An instance defeating both must, at every frame, have NO usable p AND NO usable
  q -- but (ROW-K) says k2(y) >= 1, i.e. at least one of them EXISTS.  What is left is a
  condition on the pay-vertex, not on the witness.

  (P5) PREDICTION, registered BEFORE the run: at EVERY (TAIL-2S') frame the prefix R that
  the proof claims is induced IS induced, and EVERY s in N(u_{d-1}) minus the exclusion set
  extends it to an anchored induced path on ecc(w)+3 vertices.  0 counterexamples of either
  kind.  (This is a real test: the loop tries the proof's OWN candidate set, not any s that
  happens to work.)
  (P6) PREDICTION: GUARD (D15), which drops `q !~ u_{d-4}', over-claims on some frame -- if
  it never does, the clause is NOT load-bearing and this file must say so (item (b)).
""")
    claims = built = fail = 0
    badR = badS = 0
    gclaims = gbuilt = gfail = 0
    nfr = 0
    nhost = 0
    srcs = set()
    for (tag, fam, g) in HOSTS:
        if over():
            break
        D, ecc, r = profile(g)
        used = False
        for w in range(len(g)):
            if ecc[w] < 3:
                continue
            for (P, y, q, hyp, rind, nbad, R) in sidestep3_frames(g, D, ecc, w, 2, 3):
                nfr += 1
                used = True
                if not rind:
                    badR += 1
                badS += nbad
                if hyp:
                    claims += 1
                    if R is not None and len(R) == ecc[w] + 3:
                        built += 1
                    else:
                        fail += 1
            for (P, y, q, hyp, rind, nbad, R) in sidestep3_frames(g, D, ecc, w, 2, 3,
                                                                 drop_cond=True):
                if hyp:
                    gclaims += 1
                    if R is not None and len(R) == ecc[w] + 3:
                        gbuilt += 1
                    else:
                        gfail += 1
            if nfr > 60000:
                break
        if used:
            nhost += 1
            srcs.add(fam)
    print("  (TAIL-2S') frames examined: %d, on %d hosts from %d independent sources (%s)"
          % (nfr, nhost, len(srcs), ", ".join(sorted(srcs))))
    print("  prefixes R the proof calls induced that are NOT induced: %d" % badR)
    print("  candidates s in N(u_{d-1}) minus the exclusion set that FAIL to extend: %d"
          % badS)
    print("  (TAIL-2S')  claims %d   BUILDS %d   FAILS TO BUILD %d" % (claims, built, fail))
    print("  GUARD (D15) DROP-`q !~ u_{d-4}':  claims %d   builds %d   FALSIFIED %d"
          % (gclaims, gbuilt, gfail))
    ck(fail == 0, "(P5): (TAIL-2S') BUILDS its path at every frame where it claims to")
    ck(badR == 0, "(P5): every prefix R the proof calls induced IS induced")
    ck(badS == 0, "(P5): every s outside the proof's exclusion set really does extend R")
    ck(nfr > 0, "PART 4 examined a non-empty set of (TAIL-2S') frames")
    print("  (P5) VERDICT: %s" % ("HELD" if fail == 0 and badR == 0 and badS == 0
                                  else "FAILED"))
    print("  (P6) VERDICT: %s -- the dropped clause over-claims on %d frames%s"
          % ("HELD" if gfail > fail else "FAILED", gfail - fail,
             "" if gfail > fail else "; the clause is NOT shown to be load-bearing here and"
                                     " this file says so rather than claiming it is"))

    # ---------------- the 52 residuals
    print()
    print("  ---- THE 52 CASE A RESIDUALS OF (TAIL-2S) ----")
    print("  DIRECTION (129): geodesics and far ends are SAMPLED, so `CLOSES' is SOUND and")
    print("  `does NOT close' is INCONCLUSIVE -- it may only mean the sample missed a frame.")
    tot = 0
    r2s = 0
    r2sp = 0
    both = 0
    neither = []
    kh2 = {}
    for tag, fn in (("W43a", "problems/wowii/w133_r43_W43a.txt"),
                    ("W43b", "problems/wowii/w133_r43_W43b.txt"),
                    ("W43c", "problems/wowii/w133_r43_W43c.txt"),
                    ("W44a", "problems/wowii/w133_r44_W44a.txt")):
        try:
            g = load_txt(fn)
        except IOError:
            continue
        ck(triangle_free(g), "CASE A host %s is triangle-free (HUG-EQ's hypothesis)" % tag)
        D, ecc, r = profile(g)
        ctr = [v for v in range(len(g)) if ecc[v] == r]
        cond4 = [w for w in range(len(g))
                 if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
        n2s = n2sp = nb = 0
        for w in cond4:
            tot += 1
            a = False
            for (P, y, p, hyp, R) in sidestep_frames(g, D, ecc, w, 3, 8):
                if hyp and R is not None and len(R) == ecc[w] + 3:
                    a = True
                    break
            b = False
            for (P, y, q, hyp, rind, nbad, R) in sidestep3_frames(g, D, ecc, w, 3, 8):
                if hyp and R is not None and len(R) == ecc[w] + 3:
                    b = True
                    break
            n2s += a
            n2sp += b
            nb += (a and b)
            if a:
                r2s += 1
            if b:
                r2sp += 1
            if a and b:
                both += 1
            if not a and not b:
                neither.append((tag, w))
            if not a:
                # what does k2 look like on the residual?
                for (P, y) in [fr for x in [u for u in range(len(g))
                                            if D[w][u] == ecc[w]][:8]
                               for fr in tail1_frames(g, D, w, x, 3)]:
                    kk = k2_of(g, P, y)
                    kh2[kk] = kh2.get(kk, 0) + 1
        print("  %-5s condition-4 vertices at ecc = r+1: %3d ;  (TAIL-2S) closes %3d ;"
              "  (TAIL-2S') closes %3d ;  both %3d" % (tag, len(cond4), n2s, n2sp, nb))
    print("  CASE A instances: %d ;  closed by (TAIL-2S): %d ;  by (TAIL-2S'): %d ;"
          "  by both: %d" % (tot, r2s, r2sp, both))
    print("  CLOSED BY NEITHER (the residual of the UNION): %d" % len(neither))
    print("  k2(y) histogram over the frames of the (TAIL-2S) residuals: %s"
          % ("  ".join("%d:%d" % (k, kh2[k]) for k in sorted(kh2)) if kh2 else "(none)"))
    return len(neither), tot, r2s, r2sp


# ================================================================== PART 5


def part5(hitsZ, hitsN, vac, rows, resid):
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- what is ENTITLED, what is NOT, and what each lane FAILS to close")
    print("=" * 78)
    nph2 = sum(1 for r in rows if r[9] is not None)
    nph1 = sum(1 for r in rows if r[11] == 1 and r[9] is None)
    ninc = sum(1 for r in rows if r[11] is None)
    print("""
  ENTITLED.
   * (HUG-CYC) and (HUG-DEG) are PROVED above; (HUG-EQ) is proved for TRIANGLE-FREE hosts
     only, and the one step the proof does NOT cover (a witness shared by two CONSECUTIVE
     indices, which needs a triangle) is measured and printed in PART 2 rather than assumed.
   * PART 3's Z(H) = 0 may be quoted ONLY for the %d hosts that cleared phase 2 (every
     frame of every diametral vertex over every geodesic, no cap).  %d hosts were settled
     in phase 1 by EXHIBITING a k3 = 0 frame -- sound.  %d hosts are INCONCLUSIVE (budget).
   * (TAIL-2S') is verified by CONSTRUCTION, not by assertion: every frame at which it
     claims the path had the path BUILT.

  WHAT THE LANES FAIL TO CLOSE (item (b) -- a lane that closes everything has not been
  shown to work).
   * (HUG-CYC) closes NOTHING by itself.  It forbids a FAMILY (girth >= 9) and it is silent
     on girth 5, which is exactly where all four CASE A hosts live.  It is reported as a
     constraint on the DESIGN, not as a closure.
   * (TAIL-2S') leaves %d CASE A instances that neither sidestep closes.

  WHAT IS NOT CLOSED.  CASE A is not closed.  No pocket is closed.  Nothing is promoted and
  NOTHING GOES OUTWARD.
""" % (nph2, nph1, ninc, resid))
    print("  hosts with Z(H)=0 non-vacuously: %d ; with N(H)=0 non-vacuously: %d ; vacuous: %d"
          % (len(hitsZ), len(hitsN), len(vac)))


def main():
    print("w133 round 46 -- THE ONE INTEGER.  system python3, pure stdlib, no SAT.")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    build_hosts()
    part1()
    part2()
    rows, hitsZ, hitsN, vac = part3()
    resid, tot, a, b = part4()
    part5(hitsZ, hitsN, vac, rows, resid)
    print()
    print("=" * 78)
    print("PARTS RUN: %s" % " ".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
