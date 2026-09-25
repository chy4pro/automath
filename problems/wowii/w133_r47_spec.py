#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WOWII-133 owner round 47 -- (HUG-EQ) READ AS A SPECIFICATION, AND ROUND 46's OWN
(ROW-BUDGET) DEMOTED TO A COROLLARY.

The planner's round-47 dispatch, in his order:
  1. Build FROM (HUG-EQ) as a CONSTRUCTION SPEC, not a filter for it.
  2. The 15 residuals of the (TAIL-2S)/(TAIL-2S') pair.
  3. Sum (ROW-BUDGET) against (ROW-CT).

Item 3 is answered FIRST because the answer kills the lane, and it is my own lane:

  PART 1  (BUDGET-SUB).  On a TRIANGLE-FREE C4-free host -- which is the ONLY population on
          which (ROW-BUDGET)'s proof is valid, since it needs (HUG-DEG) -- the budget test
          FIRES ONLY WHERE (TAIL-3'') ALREADY FIRES.  Proof: a(z) = deg(z) when the host is
          triangle-free, so `some z has deg(z) >= 2+k3(z)' IS `(TAIL-3'') fires at z'.  So
          (ROW-BUDGET) closes a SUBSET of the frames (TAIL-3'') closes and there is nothing
          to sum it against.  Round 46 section 4's sentence -- "it closes a frame at which
          no single vertex looks closable" -- is FALSE, and its own (P2) (`every closed
          frame carries an explicitly firing z', 0 failures) was the PROOF of the
          subsumption, which I read as a soundness check.  RETRACTED HERE, not defended.
          And with it: r46's (P3) `fires on 0 frames of Petersen/C7/C8' was NOT an
          independent soundness test -- (TAIL-3'') fires on 0 frames there, so a subsumed
          test CANNOT fire.  A control that could not have failed.

  GENERAL PRINCIPLE, stated once and applied to my own ledger: ANY test derived from the
  contrapositive of `(TAIL-3'') fires nowhere' is a COROLLARY of (TAIL-3''), never a new
  lane -- it can only re-detect a firing frame more cheaply, and exhaustive (TAIL-3'')
  checking already costs seconds.  A genuinely NEW lane must build a DIFFERENT PATH
  ((TAIL-2S), (TAIL-2S')), not re-read the same non-firing condition.  By that test
  (ROW-BUDGET), (HUG-EQ)-as-filter and (HUG-VAR) are all corollaries; their ONLY value is
  as CONSTRUCTION CONSTRAINTS, which is exactly what the dispatch's item 1 asks for.

  PART 2  (SHELL) -- the spec, completed.  Round 46 pinned the step-3 shell only.  On a
          triangle-free C4-free host the ADMISSIBLE set is exactly N(u_d) \\ {u_{d-1}}, and
          at every frame   deg(y) = 1 + k2(y) + |Z(y)|   EXACTLY (an identity, not a bound),
          so an open instance ALSO pins the y-shell: Z(y) empty forces deg(y) <= 3.

  PART 3  (SPEC-CT) -- the spec summed against the l-budget, with the missing ingredient
          named rather than hidden: everything reduces to a LOWER bound on |T|/n, which
          this line does not have.  |T| measured EXHAUSTIVELY on the four CASE A hosts.

  PART 4  THE VACUOUS ROUTE, RECLASSIFIED.  Round 46 separated C5/C6 as `VACUOUS (F=0)' and
          set them aside.  For the design target that is BACKWARDS: F(H) = 0 means there is
          no step-3 frame at all, so (TAIL-3'') can never fire and (ROW-LADDER) j=3 does not
          close the instance.  F = 0 is not a vacuum, it is a WIN CONDITION -- a fourth
          integer, and the cheapest one to state.  Measured across the library, with the
          theorem that says what it costs.

  PART 5  THE 15 RESIDUALS, EXHAUSTIVELY.  Round 46's residual count SAMPLED geodesics (3)
          and far ends (8), so `does not close' was INCONCLUSIVE.  Here every geodesic and
          every far end of every condition-4 vertex is enumerated, so BOTH directions are
          sound and the number is entitled.

  PART 6  A CONSTRUCTION, BUILT FROM THE SPEC AND NOT SEARCHED FOR.  (HUG-EQ) says a
          non-firing step-3 vertex has deg(z) = k3(z)+1; the eleven non-firing CASE A frames
          all sit at ONE planted degree-2 vertex.  So PLANT MORE OF THEM.  Planting a
          degree-2 vertex on a pair at distance >= 3 preserves C4-freeness and
          triangle-freeness, and -- this is why the lane is worth taking -- it preserves
          floor(l) = 4 EXACTLY: it adds 2 to Sum a at the new vertex and 1 at each of two
          attachment points, i.e. +4 for +1 vertex, and (Sa+4k)/(n+k) stays inside [4,5)
          whenever it started there.  The l-budget is therefore NOT the obstruction to this
          construction, and PART 6 reports what is.

DIRECTIONS OF ERROR, FIXED BEFORE ANY NUMBER IS READ (doctrine 129, dispatch item (d)):
  * PART 1/2/3: frames enumerated EXHAUSTIVELY per host (every diametral vertex, every far
    end, every geodesic, no cap) -- both directions sound.  Where a host is skipped for the
    frame budget it is PRINTED and excluded from every quoted total.
  * PART 4: F(H) = 0 is a claim about a host, so it needs the EXHAUSTIVE census; a host
    whose census is truncated may NOT be quoted as F = 0.
  * PART 5: EXHAUSTIVE over geodesics and far ends, so `does NOT close' is SOUND here --
    that is the whole point of the part, and it is what round 46 could not say.
  * PART 6: `the construction reached FIRE-GAP x%' is SOUND (it is measured on the built
    host); `no construction can do better' would be INCONCLUSIVE and is not claimed.

PREDICTIONS REGISTERED BEFORE THE RUN (dispatch item (c): a diagnosis is a conjecture):
  (Q1) BUDGET-only frames -- closed by (ROW-BUDGET) and by no single z -- number ZERO on
       every triangle-free host.  If this FAILS the subsumption proof is wrong.
  (Q2) TAIL3-only frames are MANY, so the containment is STRICT and (ROW-BUDGET) is
       strictly weaker, not equivalent.
  (Q3) deg(y) = 1 + k2(y) + |Z(y)| at every frame of every triangle-free C4-free host:
       0 violations.  And the admissible set equals N(u_d) \\ {u_{d-1}}: 0 mismatches.
  (Q4) No host in the library with floor(l) >= 4 has F(H) = 0.  (If one does, the design
       target is ALREADY MET by a host on disk and this line has been looking past it.)
  (Q5) The exhaustive residual count is <= 15 -- exhaustiveness can only CLOSE more
       instances, never fewer, so a number ABOVE 15 would mean round 46's 15 was wrong.
  (Q6) Planting degree-2 vertices RAISES the non-firing frame count above 11 and keeps
       floor(l) = 4.  Registered because it is the construction's own claim; PART 6 reports
       the trajectory whatever it does.

NO SAT.  NO local exhaustive search over a large space (the frame enumerations are over the
frames of a FIXED host, which is the object under study, not a search space).  Pure stdlib,
system python3.  Primitives, frame machinery, host builders, fires3 and the two sidestep
generators are COPIED VERBATIM from w133_r46_hug.py / w133_r46b_budget.py, never imported
(round 45 error 1 was a builder RETYPED instead of copied).
"""
from __future__ import print_function
import sys
import time
from collections import deque
from itertools import combinations

sys.setrecursionlimit(100000)

T0 = time.time()
DEADLINE = 2100.0
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



# ---- (ROW-BUDGET) machinery, COPIED VERBATIM from w133_r46b_budget.py
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



# ---- (TAIL-3'') firing test, COPIED VERBATIM from w133_r46_hug.py
def fires3(g, P, z):
    """(TAIL-3'')'s sufficient condition at the step-3 vertex z."""
    return max(a_val_matching(g, z), len(g[z]) - 1) >= 2 + k3_of(g, P, z)



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



# ---- the two sidestep generators, COPIED VERBATIM from w133_r46_hug.py
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




# ================================================================== shared scanning

CASE_A_FILES = (("W43a", "problems/wowii/w133_r43_W43a.txt"),
                ("W43b", "problems/wowii/w133_r43_W43b.txt"),
                ("W43c", "problems/wowii/w133_r43_W43c.txt"),
                ("W44a", "problems/wowii/w133_r44_W44a.txt"))


def scan_host(g, budget=600000):
    """ONE exhaustive pass over every (TAIL-1) frame of every diametral vertex, over EVERY
    far end and EVERY geodesic.  Returns a dict of counters, or None if the frame budget was
    exhausted -- in which case the host may not be quoted in any total."""
    n = len(g)
    D, ecc, r = profile(g)
    diam = max(ecc)
    S = dict(nfr=0, nz=0, bud=0, t3=0, budonly=0, t3only=0, neither=0,
             p1bad=0, idbad=0, admbad=0, z0=0, z0deg_bad=0, kmaxz0=0)
    seen = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        e = ecc[v]
        for x in [u for u in range(n) if D[v][u] == e]:
            for P in geodesics(D, g, v, x, 10 ** 9):
                if len(P) != e + 1:
                    continue
                # --- (ADM) the admissible set on a triangle-free C4-free host
                adm = []
                for y in sorted(g[x]):
                    if y == P[-2] or y in g[P[-2]]:
                        continue
                    if any(y == P[i] or y in g[P[i]] for i in range(e)):
                        continue
                    adm.append(y)
                if set(adm) != (g[x] - set([P[-2]])):
                    S['admbad'] += 1
                for y in adm:
                    Q = P + [y]
                    if len(Q) != e + 2:
                        continue
                    seen += 1
                    if seen > budget:
                        return None
                    S['nfr'] += 1
                    Z = extend_once(g, Q, v)
                    k2 = k2_of(g, P, y)
                    # --- (SHELL) the identity
                    if len(g[y]) != 1 + k2 + len(Z):
                        S['idbad'] += 1
                    if not Z:
                        S['z0'] += 1
                        if len(g[y]) > 3 or len(g[y]) != 1 + k2:
                            S['z0deg_bad'] += 1
                        continue
                    S['nz'] += 1
                    B = budget_set(g, P)
                    sk = 0
                    allw = []
                    for z in Z:
                        sk += k3_of(g, P, z)
                        allw.extend(witnesses(g, P, z))
                    sd = sum(len(g[z]) - 1 for z in Z)
                    if sk > len(B) or len(allw) != len(set(allw)) or not set(allw) <= B:
                        S['p1bad'] += 1
                    bud = (sd > len(B))
                    t3 = any(fires3(g, P, z) for z in Z)
                    S['bud'] += bud
                    S['t3'] += t3
                    if bud and not t3:
                        S['budonly'] += 1
                    if t3 and not bud:
                        S['t3only'] += 1
                    if not t3 and not bud:
                        S['neither'] += 1
    return S


def part1and2():
    PARTS_RUN.append("PART1+2")
    print()
    print("=" * 78)
    print("PART 1 -- (BUDGET-SUB): round 46's own (ROW-BUDGET) is a COROLLARY, not a lane")
    print("PART 2 -- (SHELL): the y-shell is pinned by an IDENTITY, not a bound")
    print("=" * 78)
    print("""
  (BUDGET-SUB).  H C4-free and TRIANGLE-FREE -- the only population on which (ROW-BUDGET)'s
  proof is valid, because it needs (HUG-DEG), which needs triangle-freeness.  Then at every
  frame:  (ROW-BUDGET) FIRES  ==>  (TAIL-3'') FIRES AT SOME z IN Z(y).
  Proof.  In a C4-free graph N(z) induces a matching, so a(z) = deg(z) - t(z) with t(z) the
  number of edges inside N(z); triangle-free means t(z) = 0, so a(z) = deg(z) EXACTLY.
  (ROW-BUDGET) fires iff SUM_z (deg(z)-1) > |B| >= SUM_z k3(z), which forces some z with
  deg(z) - 1 > k3(z), i.e. deg(z) >= 2 + k3(z), i.e. a(z) >= 2 + k3(z) -- which IS
  (TAIL-3'')'s sufficient condition at z. []
  So the set of frames (ROW-BUDGET) closes is a SUBSET of the set (TAIL-3'') closes, and
  there is nothing to sum it against: it carries no information (TAIL-3'') does not already
  carry.  Round 46 section 4's "it closes a frame at which no single vertex looks closable"
  is FALSE -- its own proof exhibits the single vertex.  RETRACTED.

  AND THE CONTROL THAT COULD NOT HAVE FAILED.  Round 46's (P3) -- `the budget test fires on
  0 frames of Petersen / C7 / C8' -- was recorded as the check that could have shown the
  lane unsound.  Those are exactly the three hosts with N(H) = 0, i.e. (TAIL-3'') fires on
  none of their frames; by (BUDGET-SUB) a subsumed test then CANNOT fire.  (P3) was FORCED.
  That is dispatch item (a) firing on my own control, one round later.

  (SHELL) -- and this is the part that is worth keeping.  H C4-free TRIANGLE-FREE, P a
  geodesic from a diametral v to a far end x = u_d.
   (a) ADMISSIBILITY IS FREE: the (TAIL-1)-admissible y are EXACTLY N(x) \\ {u_{d-1}}.
       (y !~ u_{d-1} because N(x) is independent; y !~ u_{d-2} would give u_{d-2}, x the two
       common neighbours u_{d-1} and y; y !~ u_i for i <= d-3 by distance.)
   (b) THE IDENTITY:  deg(y) = 1 + k2(y) + |Z(y)|  EXACTLY.
       (N(y) splits into x; the vertices of N(y) meeting N(u_{d-2}) or N(u_{d-3}), at most
       one each by C4-freeness and never the same vertex by triangle-freeness, i.e. exactly
       k2(y) of them; and the rest, which is precisely Z(y).  Nothing else can be blocked:
       a neighbour of y adjacent to u_{d-1} would give a C4 with x, and one adjacent to
       u_{d-4} or earlier would contradict d(u_j, x) = d - j.)
   (c) CONSEQUENCE FOR AN OPEN INSTANCE: if Z(y) is EMPTY at a frame then deg(y) = 1+k2(y)
       <= 3.  So the open case pins the y-shell too, not only round 46's z-shell:
       AT EVERY FRAME, EITHER deg(y) <= 3, OR every z in Z(y) has deg(z) = k3(z)+1 <= 5.

  (Q1) BUDGET-only frames = 0 on every triangle-free host.   (Q2) TAIL3-only frames > 0.
  (Q3) identity violations = 0 and admissible-set mismatches = 0.
""")
    rows = []
    skipped = []
    ntri = 0
    for (tag, fam, g) in HOSTS:
        if over():
            skipped.append((tag, "deadline"))
            continue
        if not triangle_free(g):
            continue
        ntri += 1
        S = scan_host(g)
        if S is None:
            skipped.append((tag, "frame budget"))
            continue
        rows.append((tag, len(g), S))
    tot = dict(nfr=0, nz=0, bud=0, t3=0, budonly=0, t3only=0, neither=0,
               p1bad=0, idbad=0, admbad=0, z0=0, z0deg_bad=0)
    for (tag, n, S) in rows:
        for k in tot:
            tot[k] += S[k]
    print("  triangle-free hosts in the library: %d ; fully scanned: %d ; skipped: %d %s"
          % (ntri, len(rows), len(skipped),
             ("(" + ", ".join("%s:%s" % t for t in skipped) + ")") if skipped else ""))
    print()
    print("  %-16s %5s %9s %9s %9s %9s %9s %9s"
          % ("host", "n", "frames", "with Z", "BUDGET", "TAIL3", "BUD only", "T3 only"))
    for (tag, n, S) in rows:
        print("  %-16s %5d %9d %9d %9d %9d %9d %9d"
              % (tag, n, S['nfr'], S['nz'], S['bud'], S['t3'], S['budonly'], S['t3only']))
    print("  %-16s %5s %9d %9d %9d %9d %9d %9d"
          % ("TOTAL", "", tot['nfr'], tot['nz'], tot['bud'], tot['t3'],
             tot['budonly'], tot['t3only']))
    print()
    ck(tot['budonly'] == 0, "(Q1) BUDGET-SUB: 0 frames closed by (ROW-BUDGET) and by no z")
    ck(tot['t3only'] > 0, "(Q2) the containment is STRICT: (TAIL-3'') closes frames the "
                          "budget test does not")
    ck(tot['p1bad'] == 0, "r46 (P1) reproduced: SUM k3 <= |B|, witnesses distinct, inside B")
    ck(tot['idbad'] == 0, "(Q3) (SHELL) identity deg(y) = 1 + k2(y) + |Z(y)| at every frame")
    ck(tot['admbad'] == 0, "(Q3) (SHELL)(a) admissible set = N(u_d) minus {u_{d-1}}")
    ck(tot['z0deg_bad'] == 0, "(SHELL)(c): Z(y) empty ==> deg(y) = 1+k2(y) <= 3")
    print("  (Q1) VERDICT: %s -- BUDGET-only frames %d.  (ROW-BUDGET) IS SUBSUMED."
          % ("HELD" if tot['budonly'] == 0 else "FAILED", tot['budonly']))
    print("  (Q2) VERDICT: %s -- TAIL3-only frames %d of %d with Z (%.1f%%).  The "
          "containment is STRICT." % ("HELD" if tot['t3only'] > 0 else "FAILED",
                                      tot['t3only'], tot['nz'],
                                      100.0 * tot['t3only'] / tot['nz'] if tot['nz'] else 0))
    print("  (Q3) VERDICT: %s -- identity violations %d, admissible mismatches %d, "
          "empty-Z degree violations %d"
          % ("HELD" if tot['idbad'] == 0 and tot['admbad'] == 0 and tot['z0deg_bad'] == 0
             else "FAILED", tot['idbad'], tot['admbad'], tot['z0deg_bad']))
    print("  frames with Z(y) EMPTY (the vacuous route, PART 4): %d of %d (%.1f%%)"
          % (tot['z0'], tot['nfr'], 100.0 * tot['z0'] / tot['nfr'] if tot['nfr'] else 0))
    print("  frames closed by NEITHER test: %d" % tot['neither'])
    return rows


# ================================================================== PART 3


def part3():
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- (SPEC-CT): the spec summed against the l-budget, and what is MISSING")
    print("=" * 78)
    print("""
  (SPEC-CT).  H a TRIANGLE-FREE C4-free CASE A host that is NOT closed by (ROW-LADDER) at
  j = 3.  Let T := the set of vertices that occur as a step-3 vertex at SOME frame of SOME
  diametral vertex.  By (HUG-EQ), deg(z) = k3(z)+1 for every z in T, and by (ROW-CT)
  SUM_{v in V(H)} (deg(v) - 4) >= 2.  Splitting the sum at T:

        SUM_{v NOT in T} (deg(v) - 4)  >=  2 + SUM_{z in T} (3 - k3(z)).

  With Delta := max degree this needs  (n - |T|)(Delta - 4)  >=  2 + SUM_T (3 - k3(z)).
  Since k3 <= 4, every z with k3 <= 2 costs at least one unit; by (HUG-CYC) a BIPARTITE host
  has k3 <= 2 at every step-3 vertex, so for bipartite H the demand is at least 2 + |T|:

        BIPARTITE OPEN CASE A  ==>  |T| <= ( n (Delta-4) - 2 ) / (Delta - 3).

  WHAT IS MISSING, NAMED: a LOWER bound on |T|/n.  This line does not have one.  Everything
  else in the display is a theorem; |T| is measured, and a measurement on a CLOSED host is a
  coordinate, not evidence about an open one.  Printed anyway, because the size of the gap
  is the only honest way to say how far the construction has to travel.

  ALSO MEASURED HERE: (HUG-VAR).  deg(z) is one number, so if z occurs as a step-3 vertex at
  two frames with DIFFERENT k3, the equality fails at one of them.  Per (BUDGET-SUB)'s
  general principle this is a COROLLARY of (TAIL-3''), not a new lane -- it is printed as a
  CONSTRUCTION CONSTRAINT: the builder must make k3(z) frame-invariant.
""")
    for tag, fn in CASE_A_FILES:
        if over():
            print("  DEADLINE before %s" % tag)
            break
        try:
            g = load_txt(fn)
        except IOError:
            print("  MISSING %s" % fn)
            continue
        ck(c4_free(g), "PART3 host %s C4-free" % tag)
        ck(triangle_free(g), "PART3 host %s triangle-free" % tag)
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
                kset.setdefault(z, set()).add(k3_of(g, P, z))
        T = sorted(kset)
        deg = [len(g[v]) for v in range(n)]
        Delta = max(deg)
        sig = sum(d - 4 for d in deg)
        nvary = sum(1 for z in T if len(kset[z]) > 1)
        demand = 2 + sum(3 - max(kset[z]) for z in T)
        actual = sum(deg[v] - 4 for v in range(n) if v not in kset)
        cap = (n - len(T)) * (Delta - 4)
        khist = {}
        for z in T:
            k = max(kset[z])
            khist[k] = khist.get(k, 0) + 1
        print("  %-5s n=%d  diam=%d rad=%d  Delta=%d  SUM(deg-4)=%d  l=%.4f  step-3 frames=%d"
              % (tag, n, diam, r, Delta, sig, l_of(g), nfr))
        print("        |T|=%d (%.1f%% of n)   k3max-per-z histogram %s   z with VARYING k3: %d"
              % (len(T), 100.0 * len(T) / n,
                 " ".join("%d:%d" % (k, khist[k]) for k in sorted(khist)), nvary))
        print("        DEMAND 2+SUM_T(3-k3) = %d   vs   ACTUAL SUM_{v not in T}(deg-4) = %d"
              "   vs   CAPACITY (n-|T|)(Delta-4) = %d" % (demand, actual, cap))
        print("        => the spec is violated by %d units on this host, which is another "
              "way of saying it is CLOSED." % (demand - actual))
        ck(nfr > 0, "PART3 %s has step-3 frames" % tag)


# ================================================================== PART 4


def part4():
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE VACUOUS ROUTE, RECLASSIFIED: F(H) = 0 IS A WIN, NOT A VACUUM")
    print("=" * 78)
    print("""
  Round 46 measured F(H) := # step-3 frames and set C5, C6 aside as `VACUOUS (F = 0)',
  separating them from the exhibits.  For the question `can (TAIL-3'') fail to close a CASE
  A instance' that is BACKWARDS: if there is no step-3 frame at all then (TAIL-3'') has
  nothing to fire on and (ROW-LADDER) at j = 3 does not close the instance.  F = 0 is the
  cheapest possible way to meet the design target -- a FOURTH integer after Z, N and 11.

  WHAT IT COSTS, and it is (SHELL) read backwards.  F(H) = 0 means Z(y) is empty at EVERY
  frame, so by (SHELL)(c)

        deg(y) = 1 + k2(y) <= 3   for EVERY y in N(x) \\ {u_{d-1}}, at every far end x
        of every diametral vertex and every geodesic reaching it.

  i.e. ALL BUT AT MOST ONE NEIGHBOUR OF EVERY FAR END HAS DEGREE <= 3.  Against l >= 4 that
  is the real tension, and it is LOCAL -- no covering hypothesis needed, unlike (SPEC-CT).

  (Q4) PREDICTION: no host in the library with floor(l) >= 4 has F(H) = 0.
  DIRECTION (129): a host whose census is TRUNCATED may not be quoted as F = 0; truncated
  hosts are printed and excluded.
""")
    zero = []
    trunc = []
    pos = 0
    lo = []
    for (tag, fam, g) in HOSTS:
        if over():
            trunc.append((tag, "deadline"))
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        nfr = 0
        cut = False
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
                nfr += 1
                if nfr > 600000:
                    cut = True
                    break
            if cut:
                break
        lg = l_of(g)
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        if cut:
            trunc.append((tag, "frame budget"))
            continue
        if nfr == 0:
            zero.append((tag, fam, len(g), lg, mu, r, diam))
        else:
            pos += 1
            if lg >= 4.0:
                lo.append((tag, lg, nfr))
    print("  hosts with F(H) = 0, census EXHAUSTIVE (the design target, met vacuously):")
    if zero:
        for (tag, fam, n, lg, mu, r, diam) in zero:
            print("    %-16s n=%-4d l=%.4f  mu=%d  rad=%d diam=%d  offset=%+d  floor(l)=%d"
                  % (tag, n, lg, mu, r, diam, diam - r, int(lg)))
    else:
        print("    (none)")
    print("  hosts with F(H) > 0: %d ;  truncated (excluded from every total): %d %s"
          % (pos, len(trunc),
             ("(" + ", ".join("%s:%s" % t for t in trunc) + ")") if trunc else ""))
    bad = [z for z in zero if z[3] >= 4.0]
    ck(not bad, "(Q4) no host with l >= 4 has F(H) = 0")
    print("  (Q4) VERDICT: %s -- hosts with F = 0 AND l >= 4: %d %s"
          % ("HELD" if not bad else "FAILED", len(bad),
             ", ".join(b[0] for b in bad) if bad else ""))
    print("  max l among the F = 0 hosts: %s   (the target needs floor(l) = 4)"
          % ("%.4f" % max(z[3] for z in zero) if zero else "n/a"))
    # the local cost, measured on the four CASE A hosts
    print()
    print("  THE LOCAL COST OF F = 0, measured where the line actually works:")
    for tag, fn in CASE_A_FILES:
        if over():
            break
        try:
            g = load_txt(fn)
        except IOError:
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        nx = 0
        bad4 = 0
        tot4 = 0
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            for x in [u for u in range(len(g)) if D[v][u] == diam]:
                nx += 1
                for y in g[x]:
                    tot4 += 1
                    if len(g[y]) >= 4:
                        bad4 += 1
        print("    %-5s (diametral v, far end x) pairs %d ; neighbours y of a far end with "
              "deg(y) >= 4: %d of %d (%.1f%%) -- every one of them is a frame F = 0 would "
              "have to forbid" % (tag, nx, bad4, tot4, 100.0 * bad4 / tot4 if tot4 else 0))


# ================================================================== PART 5


def part5():
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- THE RESIDUALS OF THE (TAIL-2S)/(TAIL-2S') PAIR, EXHAUSTIVELY")
    print("=" * 78)
    print("""
  Round 46 ran both sidesteps over 3 geodesics and 8 far ends per condition-4 vertex, so
  `closes' was SOUND and `does not close' was INCONCLUSIVE, and the 15 was a number the file
  was NOT entitled to read as a residual.  Here EVERY far end and EVERY geodesic of EVERY
  condition-4 vertex is enumerated (the same enumeration round 46 used for its 1 775 390
  frame census), so BOTH directions are sound and the count is entitled.

  (Q5) PREDICTION: the exhaustive residual count is <= 15.  Exhaustiveness can only find
  MORE closing frames, never fewer, so a count ABOVE 15 would mean round 46's number was
  wrong rather than merely inconclusive.
""")
    tot = 0
    r2s = 0
    r2sp = 0
    both = 0
    neither = []
    for tag, fn in CASE_A_FILES:
        if over():
            print("  DEADLINE before %s -- PART 5 is INCOMPLETE and its total is not quoted"
                  % tag)
            return None
        try:
            g = load_txt(fn)
        except IOError:
            print("  MISSING %s" % fn)
            continue
        ck(c4_free(g), "PART5 host %s C4-free" % tag)
        D, ecc, r = profile(g)
        ctr = [v for v in range(len(g)) if ecc[v] == r]
        cond4 = [w for w in range(len(g))
                 if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
        n2s = n2sp = nb = 0
        for w in cond4:
            tot += 1
            a = False
            for (P, y, p, hyp, R) in sidestep_frames(g, D, ecc, w, 10 ** 9, 10 ** 9):
                if hyp and R is not None and len(R) == ecc[w] + 3:
                    a = True
                    break
            b = False
            for (P, y, q, hyp, rind, nbad, R) in sidestep3_frames(g, D, ecc, w,
                                                                  10 ** 9, 10 ** 9):
                if hyp and R is not None and len(R) == ecc[w] + 3:
                    b = True
                    break
            n2s += a
            n2sp += b
            nb += (a and b)
            r2s += a
            r2sp += b
            both += (a and b)
            if not a and not b:
                neither.append((tag, w))
        print("  %-5s condition-4 vertices %3d ;  (TAIL-2S) closes %3d ;  (TAIL-2S') closes"
              " %3d ;  both %3d ;  NEITHER %3d"
              % (tag, len(cond4), n2s, n2sp, nb, len(cond4) - n2s - n2sp + nb))
    print("  CASE A instances %d ; (TAIL-2S) %d ; (TAIL-2S') %d ; both %d ; UNION MISSES %d"
          % (tot, r2s, r2sp, both, len(neither)))
    ck(len(neither) <= 15, "(Q5) the exhaustive residual count is at most round 46's 15")
    print("  (Q5) VERDICT: %s -- exhaustive residual %d vs round 46's sampled 15"
          % ("HELD" if len(neither) <= 15 else "FAILED", len(neither)))
    try:
        with open("problems/wowii/w133_r47_resid.txt", "w") as f:
            f.write("# WOWII-133 r47 -- CASE A instances closed by NEITHER sidestep,\n")
            f.write("# EXHAUSTIVE over every far end and every geodesic.  host vertex\n")
            for (tag, w) in neither:
                f.write("%s %d\n" % (tag, w))
        print("  residual list dumped to problems/wowii/w133_r47_resid.txt (%d lines)"
              % len(neither))
    except IOError:
        print("  (could not dump residual list)")
    return neither


# ================================================================== PART 6


def plant_spec(g, D, ecc, budget):
    """BUILD TO (HUG-EQ).  Attach new degree-2 vertices z on a pair (y, c) where y is an
    admissible (TAIL-1) vertex at a far end x of a diametral vertex and c is a neighbour of
    u_{d-1} off the path with d(y,c) >= 3.  Then at that frame z is a step-3 vertex with
    deg(z) = 2 and k3(z) = 1 (c witnesses index d-1 and nothing else can), i.e. EXACTLY the
    (HUG-EQ) equality that the eleven non-firing frames of W44a sit at.
    d(y,c) >= 3 is what keeps the host C4-free and triangle-free -- ASSERTED afterwards, not
    assumed.  Deterministic: first candidate in sorted order, each vertex used at most once
    as an attachment point."""
    g0 = [set(s) for s in g]        # FROZEN: every candidate is read off the ORIGINAL host,
    g = [set(s) for s in g]         # so the stale distance matrix D is never used on a new
    n0 = len(g)                     # vertex.
    diam = max(ecc)
    used = set()
    added = 0
    for v in range(n0):
        if added >= budget:
            break
        if ecc[v] != diam:
            continue
        for x in sorted(u for u in range(n0) if D[v][u] == diam):
            if added >= budget:
                break
            for P in geodesics(D, g0, v, x, 3):
                if added >= budget:
                    break
                if len(P) != diam + 1:
                    continue
                um1 = P[-2]
                for y in sorted(g0[x] - set([um1])):
                    if y in used or added >= budget:
                        continue
                    for c in sorted(g0[um1] - set(P)):
                        if c in used:
                            continue
                        if D[y][c] < 3:
                            continue
                        z = len(g)
                        g.append(set([y, c]))
                        g[y].add(z)
                        g[c].add(z)
                        used.add(y)
                        used.add(c)
                        added += 1
                        break
    return g, added


def census(g):
    """F, N and the CASE A bookkeeping of a host, EXHAUSTIVE."""
    n = len(g)
    D, ecc, r = profile(g)
    diam = max(ecc)
    F = 0
    N = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        for (P, y, z) in step3_frames(g, D, ecc, v, 10 ** 9, 10 ** 9):
            F += 1
            if fires3(g, P, z):
                N += 1
    ctr = [v for v in range(n) if ecc[v] == r]
    cond4 = [w for w in range(n) if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
    return dict(n=n, r=r, diam=diam, off=diam - r, l=l_of(g), F=F, N=N,
                gap=F - N, cond4=len(cond4),
                mu=min(a_val_matching(g, v) for v in range(n)))


def part6():
    PARTS_RUN.append("PART6")
    print()
    print("=" * 78)
    print("PART 6 -- BUILT FROM THE SPEC: plant the (HUG-EQ) equality instead of filtering")
    print("=" * 78)
    print("""
  The eleven non-firing CASE A frames all sit at ONE vertex -- W44a's planted degree-2
  vertex 420, at k3 = 1, i.e. deg = 2 = k3+1.  (HUG-EQ) says that IS the shape a non-firing
  step-3 vertex must have.  So build more of them, to the spec, rather than sampling hosts
  and filtering.

  WHY THE l-BUDGET IS NOT THE OBSTRUCTION (this is the reason the lane is worth taking).
  Planting a degree-2 vertex on a triangle-free C4-free host adds a(z) = 2 at the new vertex
  and +1 at each of the two attachment points: SUM a goes up by 4 and n by 1.  So
  l -> (Sa + 4k)/(n + k), which stays in [4, 5) whenever it started there -- for W44a,
  4.988 -> 4.99..., never leaving floor(l) = 4.  ROUND 45's dead end (`a <= 5 everywhere is
  CONSISTENT with l < 5') is therefore not a barrier to THIS construction either.

  (Q6) PREDICTION, registered before the run: planting raises the non-firing frame count
  (FIRE-GAP) above eleven and keeps floor(l) = 4.  Whether it raises the RATIO -- which is
  what the design target actually needs, 100% -- is the question, and this part prints the
  ratio beside the count whichever way it goes.
  DIRECTION (129): every number below is measured on the BUILT host by the exhaustive
  census, so it is SOUND as a statement about that host; nothing here is a statement about
  what planting can achieve in general.
""")
    try:
        g0 = load_txt("problems/wowii/w133_r44_W44a.txt")
    except IOError:
        print("  MISSING W44a -- PART 6 not run")
        return
    ck(c4_free(g0), "PART6 base host W44a is C4-free")
    ck(triangle_free(g0), "PART6 base host W44a is triangle-free")
    base = census(g0)
    print("  %-14s n=%-4d rad=%-2d diam=%-2d offset=%+d  l=%.4f  mu=%d  cond4=%-4d "
          "F=%-7d N=%-7d FIRE-GAP=%d (%.4f%%)"
          % ("W44a (base)", base['n'], base['r'], base['diam'], base['off'], base['l'],
             base['mu'], base['cond4'], base['F'], base['N'], base['gap'],
             100.0 * base['gap'] / base['F'] if base['F'] else 0))
    for k in (1, 5, 20, 60):
        if over():
            print("  DEADLINE -- PART 6 stopped before k=%d" % k)
            break
        D, ecc, r = profile(g0)
        gk, added = plant_spec(g0, D, ecc, k)
        okc4 = c4_free(gk)
        oktf = triangle_free(gk)
        ck(okc4, "PART6 planted host k=%d is C4-free -- ASSERTED" % k)
        ck(oktf, "PART6 planted host k=%d is triangle-free -- ASSERTED" % k)
        if not (okc4 and oktf and connected(gk)):
            print("  k=%-3d planted %d -- REJECTED (C4-free %s, triangle-free %s)"
                  % (k, added, okc4, oktf))
            continue
        c = census(gk)
        print("  %-14s n=%-4d rad=%-2d diam=%-2d offset=%+d  l=%.4f  mu=%d  cond4=%-4d "
              "F=%-7d N=%-7d FIRE-GAP=%d (%.4f%%)"
              % ("+%d planted" % added, c['n'], c['r'], c['diam'], c['off'], c['l'],
                 c['mu'], c['cond4'], c['F'], c['N'], c['gap'],
                 100.0 * c['gap'] / c['F'] if c['F'] else 0))
        ck(int(c['l']) == 4, "PART6 k=%d keeps floor(l) = 4" % k)
        if c['off'] != 1 or c['cond4'] == 0:
            print("       ^ NOTE: this host is NO LONGER a CASE A instance "
                  "(offset %+d, condition-4 vertices %d) -- printed, not hidden."
                  % (c['off'], c['cond4']))


# ================================================================== main


def main():
    print("w133 round 47 -- (HUG-EQ) AS A SPEC; (ROW-BUDGET) RETRACTED.  system python3.")
    print("started %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print(__doc__)
    build_hosts()
    part1and2()
    part3()
    part4()
    part5()
    part6()
    print()
    print("PARTS RUN: %s" % ", ".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
