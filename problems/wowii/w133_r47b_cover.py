#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 owner round 47, SLICE 2 -- (COVER): the step-3 shell is the WHOLE HOST, and
what that does to the spec.

Slice 1's PART 3 measured, exhaustively on all four CASE A hosts, that the set T of vertices
occurring as a step-3 vertex at SOME frame of SOME diametral vertex is ALL OF V(H) --
420/420, 420/420, 420/420, 421/421.  Slice 1 had written `what is missing is a LOWER bound
on |T|/n'.  On this family the bound is not merely large, it is 1, and that changes what
(SPEC-CT) says.  This slice does three things:

  PART A  (COVER) MEASURED ON THE WHOLE LIBRARY, not just the family that suggested it.
          A ratio measured on four hosts of one family is exactly the mixed-population
          mistake the planner's round-46 certificate opens with (143), in the other
          direction: four hosts of ONE family are not a population.  So |T|/n is measured
          on every host, exhaustively, and the conjecture is stated with the spread beside
          it -- including the hosts where it FAILS.

  PART B  (SPEC-COV) -- what (COVER) would buy, stated as a CONDITIONAL, because (COVER) is
          a CONJECTURE (dispatch item (c)) and not a theorem:
             T = V(H)  =>  SUM_v deg(v) = SUM_v (k3(v) + 1) = n + SUM_v k3(v),
             and (ROW-CT)'s SUM_v (deg(v)-4) >= 2 gives  SUM_v k3(v) >= 3n + 2.
          With k3 <= 4 that forces  #{v : k3(v) <= 2} <= (n-2)/2  and  #{v : k3(v) = 4} >= 2.
          By (HUG-CYC) a BIPARTITE host has k3 <= 2 everywhere, so #{k3<=2} = n > (n-2)/2:
             ** (COVER) + bipartite + CASE A + floor(l)=4  is CONTRADICTORY. **
          i.e. under (COVER) no BIPARTITE CASE A instance survives (ROW-LADDER) at j = 3.
          Measured beside it: what fraction of vertices actually have k3 <= 2.

  PART C  (VAC-CTR) -- the price of slice 1's PART 4 route, as a theorem:
             H triangle-free C4-free, offset +1, floor(l(G)) = 4, F(H) = 0, L := {deg >= 4},
             Delta := max degree (>= 5, since SUM(deg-4) >= 2 forbids Delta <= 4).
             Every x with ecc(x) = diam has |N(x) & L| <= 1, so
                SUM_{h in L} deg(h) - SUM_{c in Centre} |N(c) & L|  <=  n - |Centre|,
             while deg <= 3 off L forces SUM_{h in L} deg(h) >= n + 3|L| + 2.  Hence
                ** SUM_{c in Centre} (deg(c) - 1)  >=  3|L| + 2  >=  3(n+2)/(Delta-3) + 2 **
             and in particular |Centre| >= (3(n+2)/(Delta-3) + 2)/(Delta - 1).
          THE VACUOUS ROUTE COSTS A LARGE CENTRE.  The two counting steps are verified as
          IDENTITIES on every host (they are identities; only the `<= 1' is hypothetical),
          and max_x |N(x) & L| is measured as the distance from the route.

  WHY |N(x) & L| <= 1.  With F(H)=0 every admissible y has deg(y) = 1 + k2(y) <= 3 (slice 1
  PART 2(c)), and by (SHELL)(a) the admissible set at a geodesic P is N(x) minus its own
  penultimate vertex.  If x has two distinct penultimate vertices -- either two on one
  geodesic system from one diametral v, or two different ones coming from two different
  diametral v -- then each is admissible via the other's geodesic (N(x) is independent, and
  a neighbour of x adjacent to some u_{d-2} would give a C4), so ALL of N(x) is admissible.
  Otherwise exactly one vertex of N(x) is ever excluded.  Either way at most one neighbour
  of x escapes deg <= 3. []

DIRECTIONS OF ERROR, FIXED BEFORE THE NUMBERS (129):
  * PART A enumerates every step-3 frame of every diametral vertex with NO cap, so |T| is
    EXACT for a host that completes; a host that hits the frame budget is PRINTED and
    excluded from every quoted figure -- a truncated scan can only UNDER-count T.
  * PART B's inequality is a CONDITIONAL on (COVER); the measured k3 fractions are a
    statement about the hosts measured and about nothing else.
  * PART C's identities are verified on real hosts; the `<= 1' hypothesis is FALSE on them,
    which is why the theorem is about an object nobody has, and the measurement of
    max_x |N(x) & L| is printed as the distance, not as evidence.

Pure stdlib, system python3.  No SAT.  Primitives and host builders COPIED VERBATIM from
w133_r47_spec.py (which copied them from w133_r46_hug.py).
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




# ================================================================== PART A / B


def cover_of(g, budget=900000):
    """EXHAUSTIVE: T, per-vertex k3 range, and the step-3 frame count.  None if truncated."""
    n = len(g)
    D, ecc, r = profile(g)
    diam = max(ecc)
    kset = {}
    nfr = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
            nfr += 1
            if nfr > budget:
                return None
            kset.setdefault(z, set()).add(k3_of(g, P, z))
    return dict(n=n, rad=r, diam=diam, kset=kset, nfr=nfr, l=l_of(g),
                bip=bipartite(g), tf=triangle_free(g))


def partA():
    PARTS_RUN.append("PARTA")
    print()
    print("=" * 78)
    print("PART A -- (COVER): |T|/n on EVERY host, not on the four that suggested it")
    print("=" * 78)
    rows = []
    trunc = []
    for (tag, fam, g) in HOSTS:
        if over():
            trunc.append((tag, "deadline"))
            continue
        C = cover_of(g)
        if C is None:
            trunc.append((tag, "frame budget"))
            continue
        rows.append((tag, fam, C))
    print("  hosts scanned exhaustively: %d ; truncated and EXCLUDED: %d %s"
          % (len(rows), len(trunc),
             ("(" + ", ".join("%s:%s" % t for t in trunc) + ")") if trunc else ""))
    print()
    print("  %-16s %-7s %5s %6s %5s %5s %8s %7s %6s %s"
          % ("host", "family", "n", "l", "rad", "diam", "3-frames", "|T|", "|T|/n", "bip"))
    full = 0
    npos = 0
    for (tag, fam, C) in rows:
        T = len(C['kset'])
        if C['nfr'] == 0:
            frac = 0.0
        else:
            npos += 1
            frac = 100.0 * T / C['n']
            if T == C['n']:
                full += 1
        print("  %-16s %-7s %5d %6.3f %5d %5d %8d %7d %5.1f%% %s"
              % (tag, fam, C['n'], C['l'], C['rad'], C['diam'], C['nfr'], T, frac,
                 "yes" if C['bip'] else "no"))
    print()
    print("  hosts with at least one step-3 frame: %d ; of those, T = V(H) EXACTLY: %d "
          "(%.1f%%)" % (npos, full, 100.0 * full / npos if npos else 0))
    ck(len(rows) > 20, "PART A scanned a non-trivial slice of the library")
    return rows


def partB(rows):
    PARTS_RUN.append("PARTB")
    print()
    print("=" * 78)
    print("PART B -- (SPEC-COV): what (COVER) would buy, and how far the family is from it")
    print("=" * 78)
    print("""
  CONDITIONAL.  IF T = V(H) at an open CASE A instance, then (HUG-EQ) gives
  deg(v) = k3(v)+1 for EVERY vertex, so SUM deg = n + SUM k3, and (ROW-CT)'s
  SUM (deg - 4) >= 2 becomes  SUM_v k3(v) >= 3n + 2:  MEAN k3 >= 3 over the WHOLE host.
  With k3 <= 4 that forces  #{k3 <= 2} <= (n-2)/2  and  #{k3 = 4} >= 2.
  (HUG-CYC): k3 = 4 needs cycles of ALL FOUR lengths 5, 6, 7, 8 through the frame, and a
  BIPARTITE host has k3 <= 2 everywhere -- so under (COVER), bipartite + CASE A + floor(l)=4
  is CONTRADICTORY, i.e. every bipartite CASE A instance is CLOSED by (ROW-LADDER) at j = 3.
  (COVER) IS A CONJECTURE.  The row below is what the hosts actually do.
""")
    print("  %-16s %5s %7s %8s %8s %8s %10s"
          % ("host", "n", "|T|/n", "#k3<=2", "frac", "needed", "#k3=4 (need >=2)"))
    for (tag, fam, C) in rows:
        if C['nfr'] == 0:
            continue
        ks = C['kset']
        T = len(ks)
        le2 = sum(1 for z in ks if max(ks[z]) <= 2)
        k4 = sum(1 for z in ks if max(ks[z]) == 4)
        print("  %-16s %5d %6.1f%% %8d %7.1f%% %7s %10d"
              % (tag, C['n'], 100.0 * T / C['n'], le2, 100.0 * le2 / C['n'],
                 "<=50.0%", k4))
    nles = sum(1 for (t, f, C) in rows if C['nfr'] and
               sum(1 for z in C['kset'] if max(C['kset'][z]) <= 2) <= (C['n'] - 2) / 2.0)
    nk4 = sum(1 for (t, f, C) in rows if C['nfr'] and
              sum(1 for z in C['kset'] if max(C['kset'][z]) == 4) >= 2)
    npos = sum(1 for (t, f, C) in rows if C['nfr'])
    print()
    print("  OWNER ERROR, CAUGHT BY THIS TABLE AND CORRECTED BEFORE THE FIGURE WAS QUOTED.")
    print("  The first draft of this line read `nothing in the library is anywhere near")
    print("  either'.  THE TABLE ABOVE CONTRADICTS IT three rows down: the RAND hosts sit")
    print("  at #{k3<=2} = 0.0%%, which MEETS the <= 50%% half of the spec outright.  The")
    print("  narration was the r45-error-3 species -- a sentence contradicting the number")
    print("  below it -- and it is corrected by RUNNING the count, not by deleting it:")
    print("    hosts meeting  #{k3<=2} <= (n-2)/2 :  %d of %d" % (nles, npos))
    print("    hosts meeting  #{k3=4}  >= 2       :  %d of %d" % (nk4, npos))
    print("  SO THE BINDING HALF IS  #{k3 = 4} >= 2,  AND IT IS MET BY NOTHING.  k3 = 4 is")
    print("  draft 46.2's never-attained cell; under (COVER) an open CASE A instance is")
    print("  OBLIGED to attain it at >= 2 vertices, i.e. to carry cycles of ALL FOUR")
    print("  lengths 5, 6, 7, 8 through one step-3 frame, twice over.  Per-vertex k3 is")
    print("  read as the MAXIMUM over that vertex's frames, which is the reading most")
    print("  FAVOURABLE to the spec, so the zero above is not an artefact of the choice.")
    ck(nk4 == 0, "no host in the library attains k3 = 4 at two or more vertices")


# ================================================================== PART C


def partC():
    PARTS_RUN.append("PARTC")
    print()
    print("=" * 78)
    print("PART C -- (VAC-CTR): the F = 0 route costs a LARGE CENTRE")
    print("=" * 78)
    print("""
  The two counting steps are IDENTITIES and are checked as such on every host:
     (i)  SUM_{x : ecc(x)=diam} |N(x) & L|  =  SUM_{h in L} ( deg(h) - |N(h) & Centre| )
     (ii) SUM_{h in L} |N(h) & Centre|      =  SUM_{c in Centre} |N(c) & L|
  Only the hypothesis |N(x) & L| <= 1 is about the (non-existent) F = 0 host, and the
  measurement below is how far a real host is from it.  L := {v : deg(v) >= 4}.
""")
    bad = 0
    print("  %-16s %5s %6s %7s %7s %9s %9s"
          % ("host", "n", "|L|", "|Centre|", "offset", "max|N(x)&L|", "x with >=2"))
    for (tag, fam, g) in HOSTS:
        if over():
            break
        n = len(g)
        D, ecc, r = profile(g)
        diam = max(ecc)
        L = set(v for v in range(n) if len(g[v]) >= 4)
        ctr = set(v for v in range(n) if ecc[v] == r)
        X = [x for x in range(n) if ecc[x] == diam]
        lhs = sum(len(g[x] & L) for x in X)
        rhs = sum(len(g[h]) - len(g[h] & ctr) for h in L) if diam - r == 1 else None
        if rhs is not None and lhs != rhs:
            bad += 1
        i2 = sum(len(g[h] & ctr) for h in L)
        i2b = sum(len(g[c] & L) for c in ctr)
        if i2 != i2b:
            bad += 1
        mx = max([len(g[x] & L) for x in X]) if X else 0
        ge2 = sum(1 for x in X if len(g[x] & L) >= 2)
        print("  %-16s %5d %6d %7d %7s %9d %9d"
              % (tag, n, len(L), len(ctr), "%+d" % (diam - r), mx, ge2))
    ck(bad == 0, "(VAC-CTR)'s two counting steps are identities on every host (offset +1 "
                 "hosts for step (i), all hosts for step (ii))")
    print()
    print("  identity violations: %d" % bad)
    print("  EVERY host with a vertex x carrying two degree->=4 neighbours is a host the")
    print("  F = 0 route excludes.  The route survives only on hosts where NO far end has")
    print("  two neighbours of degree >= 4 -- and l >= 4 needs degree somewhere.")


def main():
    print("w133 round 47 slice 2 -- (COVER), (SPEC-COV), (VAC-CTR).  system python3.")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print(__doc__)
    build_hosts()
    rows = partA()
    partB(rows)
    partC()
    print()
    print("PARTS RUN: %s" % ", ".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
