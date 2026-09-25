#!/usr/bin/env python3
"""WOWII-133 round 45 -- (ROW-3) STOPPED ONE RUNG SHORT: THE ANCHOR-FREE LADDER REACHES
CASE A TOO, AND THE OPEN CASE IS NOW A CONJUNCTION OF TWO INDEPENDENT COLLAR CONDITIONS.

Round 44 proved (ROW-3): the residual row stratifies by `diam(H) - rad(H)` and closes
UNCONDITIONALLY at offset >= +3, by an EXISTENTIAL over the diametral set at offset +2, and
"needs the prescribed anchor" at offset +1 (= (SPLIT)'s CASE A).  That last line is what this
round attacks, and it turns out to be an artefact of where (ROW-3)'s ladder was truncated.

  (ROW-3) fed (TAIL-1) and (TAIL-2) into the anchor-free leg `path(G) >= path(H) >=
  endpath(H,v)`.  It never fed in (TAIL-3).  Draft 45.2's own (F11-STRAT) already uses
  (TAIL-3) one level down.  Reading the ladder as ONE statement:

      (ROW-LADDER).  offset sigma := diam(H) - rad(H), k := floor(l(G)).  If (TAIL-j) fires
      at ANY ONE vertex v with ecc(v) = diam(H), the row instance is CLOSED as soon as
      sigma + j >= k.  (j = 0 is a plain geodesic.)  NO ANCHOR AT ALL.

  At k = 4 this gives offset +1 a lane (ROW-3) does not have: j = 3, i.e. (TAIL-3'') at ANY
  non-central vertex.  The open case is therefore not "(TAIL-2'') fails at w" but the
  CONJUNCTION "(TAIL-2'') fails at w AND (TAIL-3'') fails at every non-central vertex".

PARTS
  0  primitives; the step-3 and step-4 builders with a POSITIVE and a NEGATIVE control; and
     THIS round's guard (D12) DROP-u_d -- the dodge list of the naive step-4 generalisation,
     which is exactly the off-by-one this round would be if its counting slipped.
  1  (ROW-LADDER) and the EXTENDED lane census over every residual-row instance this line
     holds, with L3 and the new L4 evaluated INDEPENDENTLY (not in fall-through order, which
     would hide L4 behind L3).
  2  (ROW-HARD') -- the strengthened necessary condition, and SLACK3 measured with the
     direction of the sampling error fixed BEFORE the number is read (129).
  3  THE FORCED-HYPOTHESIS AUDIT (90).  Which of these could have come out the other way?
     (F11-DEG'') already forces the whole step-3 chain when max(a,deg-1) >= 6 everywhere, and
     mu >= 6 forces it too; those instances are NOT evidence and are counted out.
  4  (TAIL-4'') -- proved here with the CORRECTED dodge list -- and the 30 BEYOND-k>=5 rows.
  5  (ROW-CT) -- summing (ROW-HARD')(ii) against floor(l(G)) = 4 turns the local collar
     condition into a GLOBAL budget: an open instance must hide every unit of its l-excess
     from the step-3 reach of every diametral vertex.  New sound closure test EXCESS <= 1.
  6  (ROW-K) as a closure test: which CASE A instances close by a THEOREM and which only
     by a built path.  This part exists because PART 3's audit found that PART 1's own
     260/260 headline was FORCED -- the same species of defect as (ROW-MU4)'s retraction.

Self-contained: primitives, family builders and the (TAIL-1)/(TAIL-2'') machinery COPIED
VERBATIM from round 44's `w133_r44_row.py` (lines 71-836, 927-939), never imported.
Interpreter: system python3 (pure stdlib).  No SAT.  No exhaustive graph enumeration; every
path is BUILT and then CHECKED, and a capped construction that returns nothing is recorded as
FAILURE TO BUILD, never as a shortfall.
"""
import sys
import time
from collections import deque
from itertools import combinations

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


def a_val(g, v):
    """a(v) = alpha(G[N(v)]) by BRUTE independent-set search."""
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = k
                break
        if best == k:
            break
    return best


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


def centre_of(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] == r]


def maximally_far(D, ecc, r, w):
    """draft 42.4 condition 4 / brief E46 condition 4: d(c,w) == rad for EVERY centre c."""
    C = centre_of(ecc, r)
    return all(D[c][w] == r for c in C)


def l_of(g):
    n = len(g)
    return sum(a_val_matching(g, v) for v in range(n)) / float(n)


def pathgraph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


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


# ------------------------------------------------------------------ builders


def necklace(qs, seed, src_frac=1.0, tgt_mode="any", fracs=None):
    """round 42's necklace, rebuilt EXACTLY (same call signature, same LCG order)."""
    m = len(qs)
    blocks = [pg2(q) for q in qs]
    off = []
    tot = 0
    for b in blocks:
        off.append(tot)
        tot += len(b)
    E = []
    for i, b in enumerate(blocks):
        for (u, v) in edges_of(b):
            E.append((off[i] + u, off[i] + v))
    rng = LCG(seed)
    for i in range(m):
        j = (i + 1) % m
        npts = len(blocks[i]) // 2
        srcs = rng.shuffled(range(npts))
        f = src_frac if fracs is None else fracs[i % len(fracs)]
        k = max(1, int(round(npts * f)))
        k = min(k, len(blocks[j]))
        srcs = srcs[:k]
        if tgt_mode == "points":
            pool = list(range(len(blocks[j]) // 2))
        else:
            pool = list(range(len(blocks[j])))
        tgts = rng.shuffled(pool)[:k]
        for s, t in zip(srcs, tgts):
            E.append((off[i] + s, off[j] + t))
    return adj(tot, E)


def necklace_x(qs, seed, fracs=None, tgt_mode="any", sub=None, widths=None):
    """ASYMMETRIC necklace, NEW THIS ROUND.

    Same skeleton as round 42's, plus two levers that break the cyclic symmetry ON PURPOSE:
      sub[i]    = s : the cross edges of junction i are each SUBDIVIDED s times (a chain of s
                      new degree-2 'bridge' vertices), so junction i costs s+1 instead of 1 and
                      the fibres it contributes have depth 0;
      widths[i] = k : junction i carries exactly k cross edges (k = 1 makes it a cut edge).
    Returns (g, bmap) with bmap[v] = block index of v, or -(i+1) for a bridge vertex of
    junction i.  C4-freeness is NOT certified by this docstring; every host is checked.
    """
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


def necklace_sym(q, m, seed, frac=1.0, tgt_mode="any"):
    """ROTATION-SYMMETRIC necklace: identical blocks, and the SAME injection at every junction.
    Returns (g, bmap, sigma) where sigma is the block rotation as a vertex permutation."""
    b = pg2(q)
    nb = len(b)
    npts = nb // 2
    E = []
    bmap = []
    for i in range(m):
        bmap.extend([i] * nb)
        for (u, v) in edges_of(b):
            E.append((i * nb + u, i * nb + v))
    rng = LCG(seed)
    k = max(1, int(round(npts * frac)))
    srcs = rng.shuffled(range(npts))[:k]
    pool = list(range(npts)) if tgt_mode == "points" else list(range(nb))
    tgts = rng.shuffled(pool)[:k]
    for i in range(m):
        j = (i + 1) % m
        for s, t in zip(srcs, tgts):
            E.append((i * nb + s, j * nb + t))
    g = adj(m * nb, E)
    sigma = [((v // nb + 1) % m) * nb + (v % nb) for v in range(m * nb)]
    return g, bmap, sigma


def rand_c4free_dense(seed, n):
    """round 42's greedy random C4-free host, COPIED: this is the family that produced round
    42's 414 condition-4 vertices at rad = 2, and it is used here ONLY as a POSITIVE CONTROL."""
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


def glue_cycle(g, at, k):
    """attach a cycle of length k through the vertex `at` -- round 42's lengthener, COPIED."""
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(k - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, at))
    return adj(n, E)


def theta(lens):
    """k >= 3 internally disjoint paths of the given lengths between two branch vertices.
    A CYCLE topology is what PART 4 says forces a spread centre; this is the smallest
    topology that is not a cycle."""
    E = []
    nxt = 2
    for L in lens:
        prev = 0
        for _ in range(L - 1):
            E.append((prev, nxt))
            prev = nxt
            nxt += 1
        E.append((prev, 1))
    return adj(nxt, E)


def blockgraph(qs, junctions, seed, tgt_mode="any"):
    """PG(2,q) blocks at the NODES of an arbitrary topology, NEW THIS ROUND.

    junctions: list of (i, j, width, sublen).  Junction (i,j,k,s) joins block i to block j by
    k internally disjoint paths of length s+1, whose sources are k distinct POINTS of block i
    (an independent set) and whose targets are k distinct vertices of block j.
    qs = [q_0, ...]; a q of 0 means the 'block' is a single vertex (a bare branch vertex).
    Returns (g, bmap).  C4-freeness is certified by the checker, never by this docstring.
    """
    blocks = []
    for q in qs:
        blocks.append(None if q == 0 else pg2(q))
    off = []
    tot = 0
    bmap = []
    for i, b in enumerate(blocks):
        off.append(tot)
        sz = 1 if b is None else len(b)
        tot += sz
        bmap.extend([i] * sz)
    E = []
    for i, b in enumerate(blocks):
        if b is None:
            continue
        for (u, v) in edges_of(b):
            E.append((off[i] + u, off[i] + v))
    rng = LCG(seed)
    for (i, j, k, slen) in junctions:
        bi, bj = blocks[i], blocks[j]
        npts = 1 if bi is None else len(bi) // 2
        srcs = rng.shuffled(range(npts))[:max(1, min(k, npts))]
        if bj is None:
            pool = [0]
        elif tgt_mode == "points":
            pool = list(range(len(bj) // 2))
        else:
            pool = list(range(len(bj)))
        tgts = rng.shuffled(pool)[:len(srcs)]
        for s, t in zip(srcs, tgts):
            if slen == 0:
                E.append((off[i] + s, off[j] + t))
            else:
                prev = off[i] + s
                for _ in range(slen):
                    nv = tot
                    tot += 1
                    bmap.append(-(1 + i * 37 + j))
                    E.append((prev, nv))
                    prev = nv
                E.append((prev, off[j] + t))
    return adj(tot, E), bmap


# ------------------------------------------------------------------ this round's predicates


def far_intersection(D, ecc, r):
    """(FAR): the set of vertices satisfying condition 4 = the intersection of the spheres
    S_rad(c) over all centres c.  Returned as a list."""
    n = len(ecc)
    C = centre_of(ecc, r)
    return [w for w in range(n) if all(D[c][w] == r for c in C)]


def defect(D, C, r, w):
    """how many centres are NOT at distance rad from w (0 <=> w satisfies condition 4)."""
    return sum(1 for c in C if D[c][w] != r)


def host_stats(g, bmap=None):
    n = len(g)
    D, ecc, r = profile(g)
    diam = max(ecc)
    C = centre_of(ecc, r)
    inter = far_intersection(D, ecc, r)
    best_def = None
    for w in range(n):
        if ecc[w] == r:
            continue
        dd = defect(D, C, r, w)
        if best_def is None or dd < best_def:
            best_def = dd
    spread = max((D[a][b] for a in C for b in C), default=0)
    nblk = len({bmap[c] for c in C}) if bmap is not None else None
    return dict(n=n, D=D, ecc=ecc, r=r, diam=diam, C=C, inter=inter,
                best_def=best_def, spread=spread, nblk=nblk)


def sweep_specs():
    """round 42's family (rebuilt) + THIS round's asymmetric designs."""
    specs = []
    # ---- round 42's own specs, rebuilt so the joint distribution below is over a population
    #      that includes everything this line has ever measured on this shape.
    for m in (5, 6, 7, 8, 9, 10, 12):
        for s in (1, 2, 3):
            specs.append(("R42", [3] * m, s * 104729 + m, None, "any", None, None,
                          "NL(3^%d,s%d)" % (m, s)))
    for m in (5, 6, 7, 8):
        for s in (1, 2):
            specs.append(("R42", [3] * m, s * 15485863 + m, (0.5,), "any", None, None,
                          "NLh(3^%d,s%d)" % (m, s)))
            specs.append(("R42", [3] * m, s * 32452843 + m, None, "points", None, None,
                          "NLp(3^%d,s%d)" % (m, s)))
    for m in (5, 6, 7):
        for s in (1, 2):
            specs.append(("R42", [5] * m, s * 49979687 + m, None, "any", None, None,
                          "NL(5^%d,s%d)" % (m, s)))
            specs.append(("R42", [5, 3] * (m // 2) + [5] * (m % 2), s * 67867967 + m, None,
                          "any", None, None, "NLmix(%d,s%d)" % (m, s)))
    for m in (5, 6, 7, 8):
        for s in (1, 2):
            specs.append(("R42", [3] * m, s * 86028121 + m, (0.34,), "any", None, None,
                          "NLt(3^%d,s%d)" % (m, s)))
    for m in (5, 6, 7, 8, 9):
        for s in (1, 2, 3):
            for fr, tag in (((1.0, 0.4), "a"), ((1.0, 0.6, 0.3), "b"),
                            ((0.9, 0.2, 0.7, 0.35), "c")):
                specs.append(("R42", [3] * m, s * 27644437 + m * 13, fr, "any", None, None,
                              "NLj%s(3^%d,s%d)" % (tag, m, s)))
    for m in (5, 6, 7, 8, 9, 10):
        for s in (1, 2, 3, 4, 5, 6):
            for fr, tag in (((1.0, 0.4), "a"), ((1.0, 0.6, 0.3), "b"),
                            ((0.9, 0.2, 0.7, 0.35), "c"), ((1.0,), "d")):
                qq = [3 if (i % 2 == 0) else 2 for i in range(m)]
                specs.append(("R42", qq, s * 6700417 + m * 31, fr, "any", None, None,
                              "NLs%s(%d,s%d)" % (tag, m, s)))
                specs.append(("R42", [3] * m, s * 2971215073 % (1 << 31) + m * 7, fr, "any",
                              None, None, "NLk%s(3^%d,s%d)" % (tag, m, s)))

    # ---- NEW THIS ROUND.  Every design below breaks the cyclic symmetry AT ONE PLACE, which
    #      is what PART 3 says a design must do to have any chance at all.
    # (A) ONE SUBDIVIDED JUNCTION: junction 0's cross edges each get s bridge vertices.
    for m in (5, 6, 7, 8, 9):
        for s in (1, 2, 3):
            for sl in (1, 2, 3):
                specs.append(("SUB", [3] * m, s * 104729 + m * 17, None, "any", {0: sl}, None,
                              "SUB%d(3^%d,s%d)" % (sl, m, s)))
                qq = [3 if (i % 2 == 0) else 2 for i in range(m)]
                specs.append(("SUB", qq, s * 6700417 + m * 31, None, "any", {0: sl}, None,
                              "SUBs%d(%d,s%d)" % (sl, m, s)))
    # (B) ONE THIN JUNCTION (k cross edges only) -- a near-cut through one seam.
    for m in (5, 6, 7, 8, 9):
        for s in (1, 2, 3):
            for k in (1, 2, 3):
                specs.append(("THIN", [3] * m, s * 15485863 + m * 19, None, "any", None,
                              {0: k}, "THIN%d(3^%d,s%d)" % (k, m, s)))
    # (C) THIN AND LONG at the same seam.
    for m in (5, 6, 7, 8):
        for s in (1, 2, 3):
            for k in (1, 2):
                for sl in (1, 2, 3, 4):
                    specs.append(("TL", [3] * m, s * 32452843 + m * 23, None, "any", {0: sl},
                                  {0: k}, "TL%d.%d(3^%d,s%d)" % (k, sl, m, s)))
    # (D) TWO seams treated differently (a 'dent' that is not a single seam).
    for m in (6, 7, 8, 9):
        for s in (1, 2):
            specs.append(("D2", [3] * m, s * 49979687 + m * 29, None, "any", {0: 1, 1: 1},
                          None, "D2(3^%d,s%d)" % (m, s)))
            specs.append(("D2", [3] * m, s * 67867967 + m * 31, None, "any", {0: 2},
                          {1: 2}, "D2b(3^%d,s%d)" % (m, s)))
    # (E) one ODD block among equals, plus one subdivided seam opposite it.
    for m in (6, 7, 8):
        for s in (1, 2):
            for sl in (1, 2):
                qq = [3] * m
                qq[m // 2] = 5
                specs.append(("ODD", qq, s * 86028121 + m * 37, None, "any", {0: sl}, None,
                              "ODD%d(%d,s%d)" % (sl, m, s)))
                qq2 = [3] * m
                qq2[m // 2] = 2
                specs.append(("ODD", qq2, s * 27644437 + m * 41, None, "any", {0: sl}, None,
                              "ODDs%d(%d,s%d)" % (sl, m, s)))
    return specs


def build_sweep():
    """QUIET pass: build and measure every host.  Nothing is printed here; PART 4 prints."""
    specs = sweep_specs()
    hosts = []
    n_built = n_disc = 0
    notc4 = []
    for sp in specs:
        if over():
            break
        fam, qs, seed, fracs, mode, sub, widths, nm = sp
        g, bmap = necklace_x(qs, seed, fracs, mode, sub, widths)
        if not connected(g):
            n_disc += 1
            continue
        if not c4_free(g):
            n_disc += 1
            notc4.append(nm)
            continue
        n_built += 1
        hosts.append((fam, nm, g, bmap))
    rows = []
    cond4_pairs = []
    for (fam, nm, g, bmap) in hosts:
        if over():
            break
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        if mu < 2:
            continue
        st = host_stats(g, bmap)
        lg = l_of(g)
        rows.append((fam, nm, g, bmap, mu, lg, st))
        if st["inter"]:
            cond4_pairs.append((nm, g, st["D"], st["ecc"], st["r"], st["inter"][0]))
    return rows, cond4_pairs, len(specs), n_built, n_disc, notc4



# ------------------------------------------------------------------ round 44 machinery


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


def is_anchored_induced_path(g, P, w):
    return bool(P) and P[0] == w and is_induced_path(g, P)


def build_anchored_path(g, w, cap, budget=200000):
    """capped DFS for an induced path with ENDPOINT w on >= cap vertices.  None means NOT
    BUILT WITHIN THE BUDGET -- never 'does not exist'."""
    nodes = [0]
    best = [1]
    dw = bfs(g, w)

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > budget:
            return None
        if len(path) > best[0]:
            best[0] = len(path)
        if len(path) >= cap:
            return list(path)
        u = path[-1]
        for x in sorted(g[u] - pset, key=lambda z: -dw[z]):
            bad = False
            for y in path[:-1]:
                if x in g[y]:
                    bad = True
                    break
            if bad:
                continue
            path.append(x)
            pset.add(x)
            r = dfs(path, pset)
            if r is not None:
                return r
            path.pop()
            pset.discard(x)
        return None
    r = dfs([w], {w})
    return r, best[0], nodes[0] > budget


def exact_endpath(g, w, cap=64):
    """LONGEST anchored induced path from w, by complete DFS.  Only for SMALL hosts: the
    return flag says whether the search was complete."""
    best = [1]
    nodes = [0]

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > 4000000:
            return False
        if len(path) > best[0]:
            best[0] = len(path)
        ok = True
        for x in g[path[-1]] - pset:
            if any(x in g[y] for y in path[:-1]):
                continue
            path.append(x)
            pset.add(x)
            if not dfs(path, pset):
                ok = False
            path.pop()
            pset.discard(x)
            if not ok:
                break
        return ok
    complete = dfs([w], {w})
    return best[0], complete


def exact_path(g):
    """LONGEST induced path, by complete DFS from every start.  SMALL hosts only."""
    best = 1
    comp = True
    for v in range(len(g)):
        b, c = exact_endpath(g, v)
        best = max(best, b)
        comp = comp and c
    return best, comp


def add_pendant(g, w):
    """G := H + one pendant vertex at w.  Returns the new graph; the pendant is vertex n."""
    n = len(g)
    E = edges_of(g) + [(w, n)]
    return adj(n + 1, E)


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


def k2_of(g, P, y):
    d = len(P) - 1
    k = 0
    for j in (d - 2, d - 3):
        if j >= 0 and (g[y] & g[P[j]]):
            k += 1
    return k


def tail2_at(g, D, ecc, w, ngeo=3, nfar=8):
    """Look for a frame from w at which (TAIL-2'') fires, and CERTIFY it by building z.
    Returns (fired, cert_path, best_slack, nframes).  best_slack = max over frames of
    max(a(y),deg(y)-1) - (2+k2), so >= 0 means (TAIL-2'') fires."""
    n = len(g)
    e = ecc[w]
    fars = [v for v in range(n) if D[w][v] == e]
    fars = sorted(fars)[:nfar]
    best = None
    nfr = 0
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            nfr += 1
            k2 = k2_of(g, P, y)
            slack = max(a_val_matching(g, y), len(g[y]) - 1) - (2 + k2)
            if best is None or slack > best:
                best = slack
            if slack >= 0:
                Q = P + [y]
                for z in sorted(g[y]):
                    if z in Q:
                        continue
                    if any(z in g[u] for u in Q[:-1]):
                        continue
                    R = Q + [z]
                    if is_anchored_induced_path(g, R, w) and len(R) == e + 3:
                        return True, R, best, nfr
    return False, None, (best if best is not None else -99), nfr


def frame_scan(g, D, ecc, w, ngeo=2, nfar=6):
    """EVERY admissible (TAIL-1) frame from w, with NO early return: returns (number of
    frames, max slack over them).  `tail2_at` stops at the first frame that fires, so its
    frame count is the index of that frame and NOT this number -- see PART 3's own-error
    note; this function exists because that distinction was got wrong once in this file."""
    n = len(g)
    e = ecc[w]
    fars = sorted(v for v in range(n) if D[w][v] == e)[:nfar]
    best = None
    nfr = 0
    amin = None
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            nfr += 1
            k2 = k2_of(g, P, y)
            sl = max(a_val_matching(g, y), len(g[y]) - 1) - (2 + k2)
            if best is None or sl > best:
                best = sl
            av = a_val_matching(g, y)
            if amin is None or av < amin:
                amin = av
    return nfr, (best if best is not None else -99), (amin if amin is not None else -1)


def tail1_path(g, D, ecc, v):
    """(TAIL-1)'s own construction at v: an anchored induced path on ecc(v)+2 vertices."""
    n = len(g)
    fars = [u for u in range(n) if D[v][u] == ecc[v]]
    for x in sorted(fars):
        for (P, y) in tail1_frames(g, D, v, x, 3):
            R = P + [y]
            if is_anchored_induced_path(g, R, v) and len(R) == ecc[v] + 2:
                return R
    return None


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


# ------------------------------------------------------------------ PART 0


def row_instances(hosts):
    """every residual-row instance carried by `hosts`: (name, g, D, ecc, r, diam, mu, l, w)
    with `w` satisfying condition 4 AND ecc(w) = r+1."""
    out = []
    for (nm, g, mu, lg, st) in hosts:
        r, diam, D, ecc = st["r"], st["diam"], st["D"], st["ecc"]
        for w in st["inter"]:
            if ecc[w] == r + 1:
                out.append((nm, g, D, ecc, r, diam, mu, lg, w))
    return out


# ================================================================== round 45 machinery
#
# (TAIL-3'') is draft 46.1.  (TAIL-4'') is NEW here; its proof is in PART 4 and the ONE
# place it differs from a naive generalisation of (TAIL-3'') is the index `d` itself, which
# is FREE at step 3 and is NOT free at step 4.  That difference is this round's guard.


def k3_of(g, P, z):
    """draft 46.1's k3 for the step-3 vertex z: indices d-1..d-4.  u_d is FREE at this step
    because N(z) & N(u_d) = {y} by C4-freeness and y is already paid for."""
    d = len(P) - 1
    k = 0
    for j in (d - 1, d - 2, d - 3, d - 4):
        if j >= 0 and (g[z] & g[P[j]]):
            k += 1
    return k


def k4_of(g, P, t, drop_ud=False):
    """(TAIL-4'')'s k4 for the step-4 vertex t: indices d..d-5.  `drop_ud=True` is the NAIVE
    generalisation that keeps u_d free -- guard (D12)."""
    d = len(P) - 1
    k = 0
    rng = (d - 1, d - 2, d - 3, d - 4, d - 5) if drop_ud else (d, d - 1, d - 2, d - 3,
                                                              d - 4, d - 5)
    for j in rng:
        if j >= 0 and (g[t] & g[P[j]]):
            k += 1
    return k


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


def tail3_at(g, D, ecc, v, ngeo=3, nfar=8):
    """(TAIL-1) -> (TAIL-2'') -> (TAIL-3''): BUILD an anchored induced path on ecc(v)+4
    vertices at v.  Returns (fired, cert, nframes3).  EARLY RETURN -- never read its frame
    count as a distribution (round 44's own error 1); use frame_scan3 for that."""
    n = len(g)
    e = ecc[v]
    fars = sorted(u for u in range(n) if D[v][u] == e)[:nfar]
    nfr = 0
    for x in fars:
        for (P, y) in tail1_frames(g, D, v, x, ngeo):
            Q = P + [y]
            if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                continue
            for z in extend_once(g, Q, v):
                R = Q + [z]
                if len(R) != e + 3:
                    continue
                nfr += 1
                for t in extend_once(g, R, v):
                    S = R + [t]
                    if is_anchored_induced_path(g, S, v) and len(S) == e + 4:
                        return True, S, nfr
    return False, None, nfr


def tail4_at(g, D, ecc, v, ngeo=3, nfar=8):
    """one rung further: BUILD an anchored induced path on ecc(v)+5 vertices at v."""
    n = len(g)
    e = ecc[v]
    fars = sorted(u for u in range(n) if D[v][u] == e)[:nfar]
    for x in fars:
        for (P, y) in tail1_frames(g, D, v, x, ngeo):
            Q = P + [y]
            if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                continue
            for z in extend_once(g, Q, v):
                R = Q + [z]
                if len(R) != e + 3:
                    continue
                for t in extend_once(g, R, v):
                    S = R + [t]
                    if len(S) != e + 4:
                        continue
                    for s in extend_once(g, S, v):
                        U = S + [s]
                        if is_anchored_induced_path(g, U, v) and len(U) == e + 5:
                            return True, U
    return False, None


def frame_scan3(g, D, ecc, v, ngeo=2, nfar=6):
    """EVERY step-3 frame from v, NO early return.  Returns
    (nframes, max slack3, n frames where the SUFFICIENT condition fires).
    slack3 := max(a(z), deg(z)-1) - (2 + k3(z)); >= 0 is (TAIL-3'')'s sufficient condition."""
    n = len(g)
    e = ecc[v]
    fars = sorted(u for u in range(n) if D[v][u] == e)[:nfar]
    best = None
    nfr = 0
    nfire = 0
    kh = {}
    for x in fars:
        for (P, y) in tail1_frames(g, D, v, x, ngeo):
            Q = P + [y]
            if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                continue
            for z in extend_once(g, Q, v):
                if len(Q) + 1 != e + 3:
                    continue
                nfr += 1
                k3 = k3_of(g, P, z)
                kh[k3] = kh.get(k3, 0) + 1
                sl = max(a_val_matching(g, z), len(g[z]) - 1) - (2 + k3)
                if sl >= 0:
                    nfire += 1
                if best is None or sl > best:
                    best = sl
    return nfr, (best if best is not None else -99), nfire, kh


def b4_of(g, D, ecc, diam, ncap=6, ngeo=2, nfar=4):
    """B4 := the vertices that occur as the step-3 vertex z of an admissible frame from some
    v with ecc(v) = diam, AT A FRAME WHERE k3(z) <= 3.  On such a z, (ROW-HARD')(ii) forces
    a(z) <= 1 + k3 <= 4.  SAMPLED, so the returned set is a SUBSET of the true B4."""
    n = len(g)
    B = set()
    tried = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        tried += 1
        if tried > ncap:
            break
        e = ecc[v]
        for x in sorted(u for u in range(n) if D[v][u] == e)[:nfar]:
            for (P, y) in tail1_frames(g, D, v, x, ngeo):
                Q = P + [y]
                if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                    continue
                for z in extend_once(g, Q, v):
                    if k3_of(g, P, z) <= 3:
                        B.add(z)
    return B, tried


def noncentral(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] > r]


# ------------------------------------------------------------------ PART 0


def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- the step-3 and step-4 builders, with a POSITIVE and a NEGATIVE control,")
    print("          and THIS round's guard (D12) DROP-u_d")
    print("=" * 78)

    # --- primitives, against hand computation
    c6 = cycle(6)
    ck(c4_free(c6) and connected(c6), "C6 is connected and C4-free")
    ck(a_val_matching(c6, 0) == 2 and a_val(c6, 0) == 2, "a(C6) = 2 by both routes")
    pet = petersen()
    ck(len(pet) == 10 and c4_free(pet), "Petersen built, C4-free")
    ck(min(a_val_matching(pet, v) for v in range(10)) == 3, "Petersen mu = 3")
    p5 = pg2(5)
    ck(c4_free(p5) and len(p5) == 62, "PG(2,5) built (n=62), C4-free")
    ck(min(a_val_matching(p5, v) for v in range(62)) == 6, "PG(2,5) has a(v) = 6 everywhere")

    # --- POSITIVE control: (F11-DEG) says the step-3 chain must fire at EVERY vertex of
    #     PG(2,5) (a >= 6 everywhere).  If it did not, the builder would be broken.
    D5, ecc5, r5 = profile(p5)
    fired = 0
    for v in range(len(p5)):
        ok, S, _ = tail3_at(p5, D5, ecc5, v, ngeo=2, nfar=3)
        if ok:
            fired += 1
            ck(is_anchored_induced_path(p5, S, v) and len(S) == ecc5[v] + 4,
               "PG(2,5) v=%d: built path is induced, anchored, ecc+4 long" % v)
    print("  POSITIVE control -- PG(2,5), a(v) = 6 everywhere, so (F11-DEG) FORCES the")
    print("    step-3 chain at every vertex:  fired at %d of %d vertices." % (fired, len(p5)))
    ck(fired == len(p5), "the step-3 builder fires at every vertex of PG(2,5) as (F11-DEG) forces")

    # --- NEGATIVE control: draft 45.4 records Petersen, C6 and Theta(3,3,3) as hosts on
    #     which (F11-ALL) is FALSE, i.e. endpath(w) < rad+4.  The step-3 chain must DECLINE
    #     there, or every `0` printed later would be a statement about the instrument.
    print("  NEGATIVE control -- hosts on which draft 45.4 records endpath(w) < rad+4:")
    for (nm, g) in (("C6", cycle(6)), ("Theta(3,3,3)", theta([3, 3, 3])), ("Petersen", pet),
                    ("C9", cycle(9))):
        Dg, eg, rg = profile(g)
        nf = sum(1 for v in range(len(g))
                 if tail3_at(g, Dg, eg, v, ngeo=3, nfar=4)[0])
        ex, comp = exact_path(g)
        print("    %-13s n=%2d rad=%d diam=%d  step-3 chain fires at %d of %d vertices; "
              "exact path(G) = %d%s"
              % (nm, len(g), rg, max(eg), nf, len(g), ex, "" if comp else " (TRUNCATED)"))
        if nm in ("C6", "Theta(3,3,3)", "Petersen"):
            ck(nf == 0, "%s: the step-3 chain DECLINES everywhere (it can report a negative)"
               % nm)

    # --- GUARD (D12) DROP-u_d.  (TAIL-3'') gets index d for free because
    #     N(z) & N(u_d) = {y}.  At step 4 that argument DIES: y is NOT a neighbour of t, so
    #     N(t) & N(u_d) can be an arbitrary (unique) vertex.  A naive generalisation that
    #     copies (TAIL-3'')'s index range {d-1..d-4} onto step 4 therefore UNDERCOUNTS the
    #     dodge list, and is one-sided: it can only over-claim.
    print()
    print("  GUARD (D12) DROP-u_d -- the step-4 dodge list with u_d wrongly kept free.")
    print("    ONE-SIDED BY THE PROOF: k4_naive <= k4_correct, so every frame the CORRECT")
    print("    form fires on the naive form fires on too => MISSES must be 0, and every")
    print("    disagreement is an OVER-CLAIM.  Each is settled by BUILDING the extension.")
    tot = ok_c = bad_c = ok_n = bad_n = miss = 0
    #     PG(2,q) is BIPARTITE, so d(t,u_d) is odd there and N(t) & N(u_d) is EMPTY at every
    #     step-4 frame: on incidence hosts alone the guard would be VACUOUS and would report
    #     a clean 0 that means nothing.  The seeded dense C4-free hosts are added precisely
    #     because the intersection is non-empty on about half their frames.
    hosts_g = [("PG(2,5)", p5), ("Petersen", pet), ("Theta(3,3,3)", theta([3, 3, 3])),
               ("PG(2,3)", pg2(3)), ("C9+glue", glue_cycle(cycle(9), 0, 9))]
    hosts_g += [("dense(s=%d,n=26)" % s, rand_c4free_dense(s, 26)) for s in (1, 2, 3, 5, 7)]
    nlive = 0
    for (nm, g) in hosts_g:
        # (TAIL-4'')'s proof uses C4-freeness in EVERY step, so a guard host that is not
        # C4-free would make both columns below meaningless.  ASSERTED, not assumed: slice 2
        # of this round lost 5 hosts to exactly this, from a builder that was retyped instead
        # of copied.
        ck(g is not None and c4_free(g), "guard host %s is C4-free" % nm)
        if g is None or not c4_free(g):
            continue
        Dg, eg, rg = profile(g)
        if min(a_val_matching(g, v) for v in range(len(g))) < 2:
            continue
        for v in range(0, len(g), max(1, len(g) // 8)):
            e = eg[v]
            for x in sorted(u for u in range(len(g)) if Dg[v][u] == e)[:2]:
                for (P, y) in tail1_frames(g, Dg, v, x, 2):
                    Q = P + [y]
                    if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                        continue
                    for z in extend_once(g, Q, v):
                        R = Q + [z]
                        for t in extend_once(g, R, v):
                            S = R + [t]
                            if len(S) != e + 4:
                                continue
                            tot += 1
                            m = max(a_val_matching(g, t), len(g[t]) - 1)
                            kc = k4_of(g, P, t, drop_ud=False)
                            kn = k4_of(g, P, t, drop_ud=True)
                            if kc != kn:
                                nlive += 1
                            fc = m >= 2 + kc
                            fn = m >= 2 + kn
                            has = len(extend_once(g, S, v)) > 0
                            if fc:
                                ok_c += has
                                bad_c += (not has)
                            if fn:
                                ok_n += has
                                bad_n += (not has)
                            if fc and not fn:
                                miss += 1
    print("    step-4 frames examined: %d" % tot)
    print("    frames where the two dodge lists actually DIFFER (k4_naive < k4_correct): %d"
          % nlive)
    ck(nlive > 0, "(D12) is LIVE on this sample -- the two forms differ somewhere")
    print("    (TAIL-4'') CORRECT form: claims %d, extension BUILT %d, FALSIFIED %d"
          % (ok_c + bad_c, ok_c, bad_c))
    print("    (D12) NAIVE   form:     claims %d, extension BUILT %d, FALSIFIED %d"
          % (ok_n + bad_n, ok_n, bad_n))
    print("    MISSES (correct fires, naive does not): %d   <-- must be 0" % miss)
    ck(miss == 0, "(D12) is one-sided: it cannot miss what the correct form catches")
    ck(bad_c == 0, "(TAIL-4'')'s CORRECT form is never falsified on the frames examined")
    if bad_n > 0:
        print("    ** THE NAIVE FORM IS FALSE, and %d frames exhibit it. **" % bad_n)
    else:
        print("    ** the naive form is not falsified on THIS sample -- the guard is live")
        print("       only where u_d actually has a private common neighbour with t. **")
    return tot


# ------------------------------------------------------------------ PART 1


def lanes_of(nm, g, D, ecc, r, diam, mu, lg, w, ngeo=3, nfar=8, ncap=12):
    """EVERY lane of (ROW-LADDER), each evaluated INDEPENDENTLY and each certified by
    BUILDING its path.  Fall-through order is reported separately -- evaluating L4 only
    after L3 has failed would hide it behind L3, which fires on all of CASE A already."""
    G = add_pendant(g, w)
    DG, eccG, rG = profile(G)
    k = int(l_of(G))
    need = rG + k
    n = len(g)
    res = dict(nm=nm, n=n, gref=g, r=r, diam=diam, off=diam - r, mu=mu, l=lg, w=w,
               rG=rG, lG=l_of(G), k=k, need=need, cert={}, fired={})

    # L0 -- a geodesic of H alone
    if diam + 1 >= need:
        v = ecc.index(diam)
        x = [u for u in range(n) if D[v][u] == diam][0]
        P = geodesics(D, g, v, x, 1)
        if P and is_induced_path(g, P[0]) and len(P[0]) == diam + 1:
            res["fired"]["L0"] = True
            res["cert"]["L0"] = P[0]
    # L1 -- (TAIL-1) at a diametral vertex
    if diam + 2 >= need:
        for v in range(n):
            if ecc[v] != diam:
                continue
            R = tail1_path(g, D, ecc, v)
            if R is not None and len(R) == diam + 2:
                res["fired"]["L1"] = True
                res["cert"]["L1"] = R
                break
    # L2 -- (TAIL-2'') at SOME diametral vertex
    if diam + 3 >= need:
        for v in range(n):
            if ecc[v] != diam:
                continue
            fired, R, slack, nfr = tail2_at(g, D, ecc, v, ngeo, nfar)
            if fired and len(R) == diam + 3:
                res["fired"]["L2"] = True
                res["cert"]["L2"] = R
                break
    # L3 -- the PRESCRIBED anchor: (TAIL-2'') at w, plus the hair
    if 1 + ecc[w] + 3 >= need:
        fired, R, slack, nfr = tail2_at(g, D, ecc, w, ngeo, nfar)
        res["slack_w"] = slack
        if fired:
            res["fired"]["L3"] = True
            res["cert"]["L3"] = R
    # L4 -- NEW: (TAIL-3'') at ANY ONE vertex with ecc = diam.  Anchor-free.
    if diam + 4 >= need:
        tried = 0
        for v in range(n):
            if ecc[v] != diam:
                continue
            tried += 1
            if tried > ncap:
                break
            fired, S, nfr = tail3_at(g, D, ecc, v, ngeo, nfar)
            if fired and len(S) == diam + 4:
                res["fired"]["L4"] = True
                res["cert"]["L4"] = S
                res["L4v"] = v
                break
        res["L4tried"] = tried
    res["lane"] = None
    for L in ("L0", "L1", "L2", "L3", "L4"):
        if res["fired"].get(L):
            res["lane"] = L
            break
    if res["lane"] is None:
        res["lane"] = "OPEN-k%d" % k if k <= 4 else "BEYOND-k%d" % k
    return res


def part1(inst):
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (ROW-LADDER): (ROW-3) STOPPED ONE RUNG SHORT")
    print("=" * 78)
    print("""
  (ROW-3) (round 44, draft 49.2) feeds (TAIL-1) and (TAIL-2) into the ANCHOR-FREE leg
  path(G) >= path(H) >= endpath(H,v) at a DIAMETRAL v, and stops.  Draft 45.2's own
  (F11-STRAT) already uses (TAIL-3) one level below.  Reading the whole ladder as one
  statement, with sigma := diam(H) - rad(H) and k := floor(l(G)):

    (ROW-LADDER).  Let (H,w) be a residual-row instance and G := H + one pendant at w, so
    the target is path(G) >= rad(G) + k = (r+1) + k.  If (TAIL-j) fires at ANY ONE vertex v
    with ecc_H(v) = diam(H), then the instance is CLOSED as soon as sigma + j >= k.
    Proof.  (IDENT) gives path(G) >= path(H) >= endpath(H,v); (TAIL-j) at v gives
    endpath(H,v) >= ecc(v) + 1 + j = diam(H) + 1 + j = r + sigma + 1 + j >= r + 1 + k. []
    NO ANCHOR, NO HAIR, NO F11, NO l > 4, NO rad >= 5 -- only C4-freeness and mu(H) >= 2.

  At k = 4:  sigma >= +4 needs j = 0 (a geodesic)     = (ROW-3)'s L0
             sigma  = +3 needs j = 1  (TAIL-1)        = (ROW-3)'s L1
             sigma  = +2 needs j = 2  (TAIL-2'')      = (ROW-3)'s L2
             sigma  = +1 needs j = 3  (TAIL-3'')      = *** NEW: L4 ***
  and offset +1 is exactly (SPLIT)'s CASE A.  So CASE A has an ANCHOR-FREE lane that
  (ROW-3) does not have, and round 44's sentence "offset +1 is the ONLY lane that still
  needs the prescribed anchor" is WRONG AS A STATEMENT ABOUT THE LADDER -- it is true only
  about the ladder truncated at j = 2.  This is MY error from last round and it is the
  first thing in this part.

  L3 (the prescribed anchor, (TAIL-2'') at w plus the hair) and L4 are INCOMPARABLE: L3 is
  a weaker local condition at a NAMED vertex, L4 a stronger local condition at ANY ONE of
  ~n vertices.  They are therefore evaluated INDEPENDENTLY below; a fall-through order
  would hide L4 behind L3, which already fires on all of CASE A.
""")
    if not inst:
        ck(False, "PART 1 had a non-empty row population to work on")
        return []
    out = []
    for it in inst:
        out.append(lanes_of(*it))
        if over():
            print("  ** DEADLINE reached after %d instances -- reported, not hidden **"
                  % len(out))
            break

    # fall-through table, for comparison with round 44's own numbers (a reproduction check)
    order = ["L0", "L1", "L2", "L3", "L4"]
    tally = {}
    for e in out:
        tally[e["lane"]] = tally.get(e["lane"], 0) + 1
    print("  FALL-THROUGH lanes over %d row instances (round 44's L0/L1/L2/L3 numbers are"
          % len(out))
    print("  reproduced here from an independently written classifier):")
    for L in order + sorted(k for k in tally if k not in order):
        print("    %-10s %5d" % (L, tally.get(L, 0)))

    # the offset table -- and, AGAINST THIS PART'S INTEREST, the number of DISTINCT HOSTS
    # behind each offset, because 260 instances carried by 2 hosts are not 260 tests.
    offs = {}
    ohost = {}
    for e in out:
        offs[e["off"]] = offs.get(e["off"], 0) + 1
        ohost.setdefault(e["off"], set()).add(e["nm"])
    print("  offsets diam-rad: %s" % ("  ".join("%+d:%d" % (o, offs[o])
                                                for o in sorted(offs))))
    print("  DISTINCT HOSTS behind each offset (printed because instances are NOT")
    print("  independent -- one host contributes one instance per condition-4 vertex):")
    print("    %s" % ("  ".join("%+d:%d hosts" % (o, len(ohost[o])) for o in sorted(ohost))))
    for o in sorted(ohost):
        if len(ohost[o]) <= 6:
            print("      offset %+d hosts: %s" % (o, sorted(ohost[o])))

    # THE NEW NUMBER: L3 x L4 on the offset +1 (CASE A) instances
    ca = [e for e in out if e["off"] == 1 and e["k"] == 4]
    joint = {}
    for e in ca:
        joint[(bool(e["fired"].get("L3")), bool(e["fired"].get("L4")))] = \
            joint.get((bool(e["fired"].get("L3")), bool(e["fired"].get("L4"))), 0) + 1
    print()
    print("  *** CASE A (offset +1, k = 4): %d instances, L3 and L4 evaluated INDEPENDENTLY"
          % len(ca))
    print("      L3 = (TAIL-2'') at the PRESCRIBED w + hair;  L4 = (TAIL-3'') at ANY ONE")
    print("      vertex with ecc = diam (anchor-free).  Both certified by BUILDING.")
    for key in ((True, True), (True, False), (False, True), (False, False)):
        print("        L3=%-5s L4=%-5s : %5d" % (key[0], key[1], joint.get(key, 0)))
    n_l4 = sum(1 for e in ca if e["fired"].get("L4"))
    n_l3 = sum(1 for e in ca if e["fired"].get("L3"))
    print("      L4 alone closes %d of %d CASE A instances WITHOUT the prescribed anchor."
          % (n_l4, len(ca)))
    print("      L3 closes %d of %d.  Closed by NEITHER: %d."
          % (n_l3, len(ca), joint.get((False, False), 0)))
    ck(len(ca) > 0, "the CASE A population this part reports on is non-empty")

    # every certificate re-checked from scratch, per lane, for the length ITS lane needs
    bad = short = ncert = 0
    for e in out:
        for L, P in e["cert"].items():
            ncert += 1
            if not is_induced_path(e["gref"], P):
                bad += 1
            have = len(P) + (1 if L == "L3" else 0)
            if have < e["need"]:
                short += 1
    ck(bad == 0, "every lane certificate re-checked and is an induced path of H")
    ck(short == 0, "every lane certificate is long enough for the target it discharges")
    print("  %d certificates re-checked from scratch: %d not induced, %d too short."
          % (ncert, bad, short))
    return out


# ------------------------------------------------------------------ PART 2


def part2(out):
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- (ROW-HARD'): the open case is a CONJUNCTION, not a single collar")
    print("=" * 78)
    print("""
  (ROW-HARD) (round 44) reads off (TAIL-2'') at w alone.  With L4 in the ladder an instance
  that is still open has to defeat BOTH lanes:

    (ROW-HARD').  Let (H,w) be a residual-row instance at offset +1 with k = 4 that is NOT
    closed.  Then
      (i)  at EVERY far end of w, EVERY geodesic and EVERY admissible y:
             max(a(y), deg(y)-1) <= 1 + k2(y) <= 3        [round 44's (ROW-HARD)]
      (ii) AND at EVERY vertex v with ecc(v) = diam(H) -- i.e. every NON-CENTRAL vertex,
           since diam = rad+1 here -- at every far end of v, every geodesic, every
           admissible y and every step-3 vertex z:
             max(a(z), deg(z)-1) <= 1 + k3(z) <= 5.
    Proof.  Contrapositive of (TAIL-2'')+(hair) and of (ROW-LADDER) at j = 3. []

  (ii) is a condition on the SECOND neighbourhood of BOTH ends of EVERY diametral pair --
  at offset +1 every non-central vertex is diametral, so (ii) constrains essentially the
  whole periphery in every direction, not just w's own far ends.

  SLACK3(H) := max over the sampled step-3 frames of [max(a(z),deg(z)-1) - (2 + k3(z))].
  DIRECTION OF THE SAMPLING ERROR, FIXED BEFORE ANY NUMBER IS READ (129): non-central
  vertices, far ends and geodesics are all SAMPLED, so the printed SLACK3 is a LOWER bound
  on the true maximum.  A printed SLACK3 >= 0 is therefore SOUND (the lane really does
  fire); a printed SLACK3 < 0 would be INCONCLUSIVE and could NOT be called an open
  instance without an exhaustive frame enumeration.
""")
    hist = {}
    histA = {}
    worst = None
    worstA = None
    kh_all = {}
    nfr_tot = 0
    done = 0
    for e in out:
        g = e["gref"]
        D, ecc, r = profile(g)
        nc = [v for v in range(len(g)) if ecc[v] == e["diam"]]
        best = None
        for v in nc[:4]:
            nfr, sl, nfire, kh = frame_scan3(g, D, ecc, v, ngeo=2, nfar=4)
            nfr_tot += nfr
            for kk, vv in kh.items():
                kh_all[kk] = kh_all.get(kk, 0) + vv
            if nfr and (best is None or sl > best):
                best = sl
        if best is None:
            continue
        done += 1
        hist[best] = hist.get(best, 0) + 1
        if worst is None or best < worst[0]:
            worst = (best, e)
        if e["off"] == 1 and e["k"] == 4:
            histA[best] = histA.get(best, 0) + 1
            if worstA is None or best < worstA[0]:
                worstA = (best, e)
        if over():
            print("  ** DEADLINE after %d instances -- reported **" % done)
            break
    print("  SLACK3 over %d instances (%d step-3 frames scanned, NO early return):"
          % (done, nfr_tot))
    print("    ALL:    %s" % ("  ".join("%+d:%d" % (s, hist[s]) for s in sorted(hist))))
    print("    CASE A: %s" % ("  ".join("%+d:%d" % (s, histA[s]) for s in sorted(histA))))
    for tag, wz in (("anywhere", worst), ("in CASE A", worstA)):
        if wz:
            s, e = wz
            print("    MINIMUM SLACK3 %-10s: %+d, at %s n=%d rad=%d diam=%d mu=%d l=%.4f w=%d"
                  % (tag, s, e["nm"], e["n"], e["r"], e["diam"], e["mu"], e["l"], e["w"]))
    neg = sum(v for s, v in hist.items() if s < 0)
    print("    instances with SLACK3 < 0 (the only ones (ii) could hold at): %d" % neg)
    print("  k3 histogram over every step-3 frame scanned: %s"
          % "  ".join("%d:%d" % (k, kh_all[k]) for k in sorted(kh_all)))
    print("    (draft 46.2's blanket worst case is k3 = 4; round 42's AMENDMENT exhibits it")
    print("     at n = 16, so `k3 = 4 never happens' is a property of the FAMILY, not a")
    print("     theorem -- and PART 5 is written so that it does not need one.)")
    ck(done > 0, "PART 2 measured a non-empty population")
    return hist, neg, kh_all


# ------------------------------------------------------------------ PART 3


def part3(out):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- THE FORCED-HYPOTHESIS AUDIT (90): WHICH OF THESE COULD HAVE COME OUT")
    print("          THE OTHER WAY?")
    print("=" * 78)
    print("""
  Round 43 banked a 129/129 census whose passes were FORCED by (ROW-MU4), and the planner
  certified it approvingly; round 44 caught it.  The same question has to be asked of PART
  1's L4 column BEFORE it is quoted, so it is asked here and answered against interest.

  TWO THEOREMS ALREADY FORCE L4, and both are this line's own:
    (F11-DEG'')  (draft 46.4).  max(a(v), deg(v)-1) >= 6 at EVERY v  =>  endpath(H,v) >=
                 ecc(v)+4 for every v.  So L4 fires by THEOREM, and such an instance is
                 NOT evidence that the lane is live.
    (ROW-MU6)    mu(H) >= 6  =>  a(z) >= 6 >= 2 + k3 (k3 <= 4)  =>  the same.  It is the
                 (F11-DEG'') hypothesis restricted to the a-half, hence subsumed by it.
  And for L3, round 44's (ROW-MU4): mu(H) >= 4 => (TAIL-2) at EVERY w.
""")
    forced4 = forced3 = 0
    tested4 = fired_tested4 = 0
    muh = {}
    mmh = {}
    for e in out:
        if e["off"] != 1 or e["k"] != 4:
            continue
        g = e["gref"]
        mm = min(max(a_val_matching(g, v), len(g[v]) - 1) for v in range(len(g)))
        muh[e["mu"]] = muh.get(e["mu"], 0) + 1
        mmh[mm] = mmh.get(mm, 0) + 1
        if mm >= 6:
            forced4 += 1
        else:
            tested4 += 1
            if e["fired"].get("L4"):
                fired_tested4 += 1
        if e["mu"] >= 4:
            forced3 += 1
    tot = forced4 + tested4
    print("  Over the %d CASE A (offset +1, k = 4) instances:" % tot)
    print("    mu(H) histogram:                    %s"
          % "  ".join("%d:%d" % (m, muh[m]) for m in sorted(muh)))
    print("    min_v max(a(v),deg(v)-1) histogram: %s"
          % "  ".join("%d:%d" % (m, mmh[m]) for m in sorted(mmh)))
    print("    L4 FORCED by (F11-DEG'') (min max(a,deg-1) >= 6): %d  <-- NOT evidence"
          % forced4)
    print("    L4 a GENUINE TEST (the hypothesis fails):         %d" % tested4)
    print("      ... of those, L4 fired:                         %d" % fired_tested4)
    print("    L3 FORCED by (ROW-MU4) (mu >= 4):                 %d  <-- NOT evidence"
          % forced3)
    # --- the SHARPER audit: at the frame L4 actually fired on, was it forced by mu alone?
    #     (TAIL-3'') fires as soon as max(a(z),deg(z)-1) >= 2 + k3(z).  mu(H) <= a(z), so
    #     mu >= 2 + k3 at that frame means the firing was FORCED by the host's own mu and
    #     the frame's own k3 -- the exact species of (ROW-MU4)'s 129/129.
    fmu = 0
    nfr_seen = 0
    azh = {}
    k3h = {}
    for e in out:
        if e["off"] != 1 or e["k"] != 4:
            continue
        S = e["cert"].get("L4")
        if S is None:
            continue
        g = e["gref"]
        dm = e["diam"]
        if len(S) != dm + 4:
            continue
        P, z = S[:dm + 1], S[dm + 2]
        k3 = k3_of(g, P, z)
        az = a_val_matching(g, z)
        nfr_seen += 1
        azh[az] = azh.get(az, 0) + 1
        k3h[k3] = k3h.get(k3, 0) + 1
        if e["mu"] >= 2 + k3:
            fmu += 1
    print()
    print("  SHARPER, AT THE FRAME L4 ACTUALLY FIRED ON (%d certificates re-read):"
          % nfr_seen)
    print("    k3 at the firing frame:  %s"
          % "  ".join("%d:%d" % (k, k3h[k]) for k in sorted(k3h)))
    print("    a(z) at the firing frame:%s"
          % "  ".join(" %d:%d" % (k, azh[k]) for k in sorted(azh)))
    print("    firings FORCED by mu alone (mu >= 2 + k3 at that frame): %d of %d"
          % (fmu, nfr_seen))
    print("    firings that needed the ACTUAL a(z)/deg(z), i.e. could have failed: %d"
          % (nfr_seen - fmu))
    ck(nfr_seen > 0, "PART 3 re-read a non-empty set of L4 certificates")
    if fmu == nfr_seen and nfr_seen > 0:
        print("""
  *** AGAINST THIS ROUND'S OWN HEADLINE, AND FIRST RATHER THAN BURIED. ***
  EVERY ONE of PART 1's L4 firings was forced: at the frame it fired on,
  mu(H) >= 2 + k3(z) already, so a(z) >= mu made (TAIL-3'')'s sufficient condition TRUE
  before a(z) was looked at.  THE 260/260 COULD NOT HAVE FAILED AT THOSE FRAMES.  This is
  the SAME SPECIES as (ROW-MU4)'s retraction of round 43's 129/129, one round later, in my
  own round -- and it is found here by asking the planner's own question of my own headline.

  WHAT SURVIVES, EXACTLY.  The certificates are BUILT paths and they are real: L4 does
  close all 260 CASE A instances anchor-free, and that claim STANDS.  What dies is any
  reading of `260/260' as evidence that the LANE discriminates.  What the census does test,
  and what is NOT forced, is the EXISTENCE of a frame with small k3 -- and that existence
  is now a named theorem rather than a measurement:

    (ROW-K).  H C4-free, mu := mu(H) >= 2, v with ecc(v) = D.  Since a(z) >= mu at every
    vertex, (TAIL-2'') fires at any frame with k2(y) <= mu-2 and (TAIL-3'') fires at any
    step-3 frame with k3(z) <= mu-2.  Hence an instance that is still open has
        k2(y) >= mu-1  at EVERY frame from w,   and   k3(z) >= mu-1  at EVERY step-3
        frame of EVERY vertex with ecc = D.
    Since k2 <= 2 and k3 <= 4 this forces mu(H) <= 3 (from the step-2 half; that is exactly
    round 44's (ROW-MU4) read backwards) and mu(H) <= 5 (from the step-3 half). []

  So the open case is NOT `a low-a collar' -- it is `EVERY step-3 vertex of EVERY frame of
  EVERY diametral vertex HUGS THE GEODESIC', in the precise sense that N(z) must meet
  N(u_j) for at least mu-1 of the four indices j in {d-1,..,d-4}.  PART 2's k3 histogram
  is the measurement of how rare that is.""")
    print()
    print("  ENTITLED READING.  The %d instances where (F11-DEG'')'s hypothesis fails are"
          % tested4)
    print("  the ONLY ones on which L4's firing is information; on the other %d it could not"
          % forced4)
    print("  have come out the other way.  PART 0's NEGATIVE control (C6, Theta(3,3,3),")
    print("  Petersen: 0 firings) is what makes a firing on the tested set information at")
    print("  all -- the detector demonstrably declines.")
    ck(tot > 0, "PART 3 audited a non-empty CASE A population")
    return forced4, tested4, fired_tested4


# ------------------------------------------------------------------ PART 4


def part4(out):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- (TAIL-4''), PROVED WITH THE CORRECTED DODGE LIST, AND THE 30")
    print("          BEYOND-k>=5 ROWS")
    print("=" * 78)
    print("""
  (TAIL-4'').  In (TAIL-3'')'s frame -- u_0..u_d a geodesic from v, d = ecc(v), y in N(u_d)
  off u_{d-1}'s matching component, z in N(y) and t in N(z) with u_0..u_d y z t induced --
  put  k4 := #{ j in {d, d-1, d-2, d-3, d-4, d-5} : N(t) & N(u_j) != {} }.  Then
  endpath(H,v) >= ecc(v) + 5 as soon as  max(a(t), deg(t)-1) >= 2 + k4.

  Proof.  Let s in N(t); u_0..u_d y z t s is induced and anchored iff s is not in the path,
  s !~ z, s !~ y and s !~ u_i for all i <= d.  Count the vertices of N(t) that forbids.
  (a) s = z: 1 vertex; s ~ z: N(t) & N(z) has at most ONE element by C4-freeness (t ~ z, and
      two common neighbours of t and z would be a C4) -- 2 vertices in all, and both lie in
      z's own matching component of G[N(t)] (that common neighbour is adjacent to z).
  (b) s ~ y: N(t) & N(y) has at most one element by C4-freeness; z is IN it (z ~ y, z ~ t),
      so it IS {z} and is already paid for -- FREE.  y itself is not in N(t) (t !~ y).
  (c) s ~ u_j: for each j, |N(t) & N(u_j)| <= 1 by C4-freeness -- k4 vertices; and u_j is
      never in N(t), since t !~ u_i for all i.  Which j can contribute?  s ~ u_j forces
      d(t,u_j) <= 2, and d(t,u_j) >= d(u_d,u_j) - d(u_d,t) >= (d-j) - 3, so j >= d-5.
  (d) i <= d-6 is free by distance.
  So at most 2 + k4 vertices of N(t) are excluded, and they meet at most 1 + k4 matching
  components; deg(t) >= 3 + k4 or a(t) >= 2 + k4 leaves one. []

  *** THE ONE PLACE THIS IS NOT A COPY OF (TAIL-3''). ***  (TAIL-3'') gets the index d for
  FREE, because N(z) & N(u_d) = {y} and y is already paid for.  At step 4 that argument
  DIES: y is NOT adjacent to t, so it is not a common neighbour of t and u_d, and N(t) &
  N(u_d) can be an arbitrary (unique) vertex.  A naive generalisation copying the range
  {d-1..d-4} onto step 4 UNDERCOUNTS the dodge list and can only OVER-CLAIM.  That is
  guard (D12) in PART 0, and it is stated here because it is exactly the kind of one-line
  slip this line has shipped before.

  BLANKET FORM: k4 <= 6, so a(t) >= 8 suffices -- and by the same reading as (ROW-MU6),
  mu(H) >= 8 gives endpath(H,v) >= ecc(v)+5 at EVERY v.

  (ROW-LADDER) AT j = 4 therefore closes offset sigma as soon as sigma + 4 >= k, i.e.
  offset +1 at k = 5 -- which is what the 30 BEYOND-k>=5 rows need.
""")
    bey = [e for e in out if e["k"] >= 5]
    print("  BEYOND-k>=5 rows in this population: %d" % len(bey))
    grid = {}
    for e in bey:
        grid[(e["off"], e["k"])] = grid.get((e["off"], e["k"]), 0) + 1
    for key in sorted(grid):
        print("    offset %+d, k = %d : %4d instances -> (ROW-LADDER) needs rung j = %d"
              % (key[0], key[1], grid[key], max(0, key[1] - key[0])))
    closed = {}
    nb = 0
    for e in bey:
        g = e["gref"]
        D, ecc, r = profile(g)
        j = max(0, e["k"] - e["off"])
        got = False
        if j <= 3:
            for v in range(len(g)):
                if ecc[v] != e["diam"]:
                    continue
                if j <= 2:
                    fired, R, sl, nf = tail2_at(g, D, ecc, v, 3, 6)
                    got = fired and len(R) >= e["need"]
                else:
                    fired, S, nf = tail3_at(g, D, ecc, v, 3, 6)
                    got = fired and len(S) >= e["need"]
                if got:
                    e["cert"]["Lbey"] = R if j <= 2 else S
                    break
        elif j == 4:
            for v in range(len(g)):
                if ecc[v] != e["diam"]:
                    continue
                fired, U = tail4_at(g, D, ecc, v, 3, 6)
                if fired and len(U) >= e["need"]:
                    got = True
                    e["cert"]["Lbey"] = U
                    break
        closed[(j, got)] = closed.get((j, got), 0) + 1
        nb += 1
        if over():
            break
    print("  rung needed vs CLOSED (certificate BUILT and re-checked), over %d rows:" % nb)
    for key in sorted(closed):
        print("    j = %d  closed = %-5s : %4d" % (key[0], key[1], closed[key]))
    bad = 0
    ncert = 0
    for e in bey:
        P = e["cert"].get("Lbey")
        if P is None:
            continue
        ncert += 1
        if not (is_induced_path(e["gref"], P) and len(P) >= e["need"]):
            bad += 1
    ck(bad == 0, "every BEYOND certificate is an induced path of H, long enough")
    print("  %d BEYOND certificates re-checked from scratch: %d bad." % (ncert, bad))
    nopen = sum(v for (j, gt), v in closed.items() if not gt)
    print("  BEYOND rows STILL NOT CLOSED by any rung of the ladder: %d" % nopen)
    return len(bey), nopen


# ------------------------------------------------------------------ PART 5


def part5(out):
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- (ROW-CT): THE OPEN CASE, MOVED OUT OF THE COLLAR AND INTO A GLOBAL")
    print("          BUDGET ON WHERE l's EXCESS IS ALLOWED TO LIVE")
    print("=" * 78)
    print("""
  (ROW-HARD')(ii) is a bound on a(z) at every step-3 vertex.  It becomes a GLOBAL statement
  the moment it is summed, because floor(l(G)) = 4 is itself a sum.

    (ROW-CT).  Let (H,w) be a residual-row instance at offset +1 with k = floor(l(G)) = 4,
    G := H + one pendant at w.  Put
      B4 := { z : z is the step-3 vertex of an admissible frame from some v with
                  ecc(v) = diam(H), at a frame where k3(z) <= 3 }.
    If the instance is NOT closed by (ROW-LADDER) at j = 3, then a_H(z) <= 1 + k3(z) <= 4
    for every z in B4, hence
        EXCESS(H) := SUM_{v not in B4} max(a_H(v) - 4, 0)  >=  2.
    Equivalently: EXCESS(H) <= 1  =>  the instance is CLOSED.

    Proof.  floor(l(G)) = 4 gives l(G) >= 4, i.e. SUM_{V(G)} (a_G - 4) >= 0.  The pendant p
    has a_G(p) = 1 and contributes -3; a_G(v) = a_H(v) for v != w and a_G(w) = a_H(w) + 1.
    So SUM_{V(H)} (a_H - 4) >= 2.  On B4, a_H - 4 <= 0, so dropping B4 can only increase the
    sum: SUM_{v not in B4} (a_H(v) - 4) >= 2, and replacing each term by its positive part
    only increases it again. []

  WHAT IT SAYS.  An instance that is still open has to carry the WHOLE of its l-budget --
  every unit by which a exceeds 4 -- on vertices that the step-3 chain from the periphery
  never reaches.  The obstruction stops being "a low collar" and becomes "a high core that
  is INVISIBLE from every diametral vertex at depth 3".

  DIRECTION OF THE SAMPLING ERROR, FIXED BEFORE THE NUMBER (129).  B4 is computed from
  SAMPLED frames, so the computed B4 is a SUBSET of the true B4, so the computed EXCESS is
  an UPPER bound on the true EXCESS.  Therefore `EXCESS <= 1 => CLOSED' is SOUND, and a
  computed EXCESS >= 2 is INCONCLUSIVE -- it can never be quoted as evidence of openness.
""")
    ca = [e for e in out if e["off"] == 1 and e["k"] == 4]
    seen = {}
    rows = []
    for e in ca:
        key = e["nm"]
        if key in seen:
            rows.append((e, seen[key]))
            continue
        g = e["gref"]
        D, ecc, r = profile(g)
        sa = sum(a_val_matching(g, v) for v in range(len(g)))
        B, tried = b4_of(g, D, ecc, e["diam"])
        exc = sum(max(a_val_matching(g, v) - 4, 0) for v in range(len(g)) if v not in B)
        seen[key] = (len(g), sa, len(B), exc, tried)
        rows.append((e, seen[key]))
        if over():
            break
    print("  Per HOST (the quantities are host quantities, not per-w quantities):")
    print("    %-24s %5s %7s %8s %8s %9s" % ("host", "n", "S(a-4)", "|B4|", "|B4|/n",
                                             "EXCESS"))
    for nm in sorted(seen):
        n, sa, nb, exc, tried = seen[nm]
        print("    %-24s %5d %7d %8d %7.1f%% %9d"
              % (nm, n, sa - 4 * n, nb, 100.0 * nb / n, exc))
        ck(sa - 4 * n >= 2,
           "%s: floor(l(G))=4 really does force SUM_H(a-4) >= 2 (it is %d)" % (nm, sa - 4 * n))
    nclosed = sum(1 for (e, s) in rows if s[3] <= 1)
    print("  CASE A instances CLOSED by (ROW-CT) (EXCESS <= 1): %d of %d"
          % (nclosed, len(rows)))
    print("  CASE A instances where (ROW-CT) is INCONCLUSIVE (EXCESS >= 2): %d"
          % (len(rows) - nclosed))
    print("""
  READ IT AGAINST THIS PART'S OWN INTEREST.  On this family (ROW-CT) closes nothing: these
  hosts are triangle-free or near it, so a = deg and the l-budget is enormous (hundreds of
  units), while B4 -- even sampled -- is a large fraction of n.  What (ROW-CT) buys is NOT
  a closure here; it is a REPLACEMENT of the open coordinate.  Round 44 left the question
  as `build a low-a collar'; slice 2 showed the only lever that lowers a on the collar also
  enlarges the collar.  (ROW-CT) says the same object must ALSO hide every unit of its
  l-excess from the step-3 reach of EVERY diametral vertex -- and the |B4|/n column is the
  measurement of how much room that leaves.
""")
    return seen, nclosed


# ------------------------------------------------------------------ PART 6


def k2min_at(g, D, ecc, w, ngeo=3, nfar=6):
    """min k2 over the sampled (TAIL-1) frames from w.  SAMPLED => an UPPER bound on the
    true minimum, so `k2min <= mu-2 => closed' is SOUND and the converse is not."""
    e = ecc[w]
    best = None
    for x in sorted(u for u in range(len(g)) if D[w][u] == e)[:nfar]:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            k = k2_of(g, P, y)
            if best is None or k < best:
                best = k
    return best


def k3min_at(g, D, ecc, diam, ncap=6, ngeo=2, nfar=4):
    n = len(g)
    best = None
    tried = 0
    for v in range(n):
        if ecc[v] != diam:
            continue
        tried += 1
        if tried > ncap:
            break
        e = ecc[v]
        for x in sorted(u for u in range(n) if D[v][u] == e)[:nfar]:
            for (P, y) in tail1_frames(g, D, v, x, ngeo):
                Q = P + [y]
                if len(Q) != e + 2 or not is_anchored_induced_path(g, Q, v):
                    continue
                for z in extend_once(g, Q, v):
                    k = k3_of(g, P, z)
                    if best is None or k < best:
                        best = k
                    if best == 0:
                        return 0, tried
    return best, tried


def part6(out):
    PARTS_RUN.append("PART6")
    print()
    print("=" * 78)
    print("PART 6 -- (ROW-K) AS A CLOSURE TEST: WHICH CASE A INSTANCES CLOSE BY A THEOREM,")
    print("          AND WHICH ONLY BY A BUILT PATH")
    print("=" * 78)
    print("""
  DIRECTION OF THE SAMPLING ERROR, FIXED BEFORE THE NUMBERS (129).  k2min and k3min are
  minima over SAMPLED frames, so each is an UPPER bound on the true minimum.  Therefore
  `k2min <= mu-2 => CLOSED' and `k3min <= mu-2 => CLOSED' are SOUND; a large k2min/k3min is
  INCONCLUSIVE and can never be quoted as evidence that an instance is open.
""")
    ca = [e for e in out if e["off"] == 1 and e["k"] == 4]
    cache = {}
    tally = {"(ROW-MU4) mu>=4": 0, "(ROW-K) step-2 k2min<=mu-2": 0,
             "(ROW-K) step-3 k3min<=mu-2": 0, "BUILT PATH ONLY": 0}
    h2 = {}
    h3 = {}
    for e in ca:
        g = e["gref"]
        if e["nm"] not in cache:
            D, ecc, r = profile(g)
            cache[e["nm"]] = (D, ecc, r, k3min_at(g, D, ecc, e["diam"]))
        D, ecc, r, (k3m, tried) = cache[e["nm"]]
        k2m = k2min_at(g, D, ecc, e["w"])
        h2[k2m] = h2.get(k2m, 0) + 1
        h3[k3m] = h3.get(k3m, 0) + 1
        mu = e["mu"]
        if mu >= 4:
            tally["(ROW-MU4) mu>=4"] += 1
        elif k2m is not None and k2m <= mu - 2:
            tally["(ROW-K) step-2 k2min<=mu-2"] += 1
        elif k3m is not None and k3m <= mu - 2:
            tally["(ROW-K) step-3 k3min<=mu-2"] += 1
        else:
            tally["BUILT PATH ONLY"] += 1
        if over():
            break
    print("  over %d CASE A instances:" % len(ca))
    print("    k2min at w   histogram: %s"
          % "  ".join("%s:%d" % (k, h2[k]) for k in sorted(h2, key=lambda z: (z is None, z))))
    print("    k3min at any diametral vertex histogram: %s"
          % "  ".join("%s:%d" % (k, h3[k]) for k in sorted(h3, key=lambda z: (z is None, z))))
    print("  CLOSED BY, in order of precedence (each instance counted ONCE):")
    for k in ("(ROW-MU4) mu>=4", "(ROW-K) step-2 k2min<=mu-2",
              "(ROW-K) step-3 k3min<=mu-2", "BUILT PATH ONLY"):
        print("    %-30s %5d" % (k, tally[k]))
    print("""
  THE ENTITLED SENTENCE.  Every CASE A instance this line holds is closed by a THEOREM
  whose hypothesis is checkable in O(frames) -- not by an unexplained successful search.
  That is what changed this round.  What did NOT change: there is still no theorem saying
  that a CASE A instance MUST satisfy one of these hypotheses, so CASE A is NOT closed.""")
    return tally


def main():
    print("WOWII-133 round 45 -- (ROW-3) STOPPED ONE RUNG SHORT: THE ANCHOR-FREE LADDER")
    print("                      REACHES CASE A TOO")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    part0()

    print()
    print("  building and measuring the host population (quiet pass) ...", flush=True)
    rows, cond4_pairs, nspecs, n_built, n_disc, notc4 = build_sweep()
    hosts = [(nm, g, mu, lg, st) for (fam, nm, g, bmap, mu, lg, st) in rows]
    print("  ... %d specs, %d built, %d discarded, %d hosts measured, %.1fs"
          % (nspecs, n_built, n_disc, len(hosts), time.time() - T0), flush=True)
    for tag in ("W43a", "W43b", "W43c"):
        try:
            g = load_txt("problems/wowii/w133_r43_%s.txt" % tag)
        except IOError:
            continue
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        hosts.append((tag, g, mu, l_of(g), host_stats(g)))
    try:
        g = load_txt("problems/wowii/w133_r44_W44a.txt")
        hosts.append(("W44a", g, min(a_val_matching(g, v) for v in range(len(g))),
                      l_of(g), host_stats(g)))
    except IOError:
        pass
    print("  population for the census: %d hosts (round 43's three witnesses + W44a)."
          % len(hosts), flush=True)

    inst = row_instances(hosts)
    print("  residual-row instances in it: %d." % len(inst), flush=True)

    out = part1(inst)
    part2(out)
    part3(out)
    part4(out)
    part5(out)
    part6(out)

    # --- the L4 certificates for the NAMED hosts, written out for the STANDALONE
    #     verifier (105).  One anchor-free path per host discharges EVERY CASE A instance
    #     that host carries, which is exactly what "anchor-free" buys.
    fn = "problems/wowii/w133_r45_L4certs.txt"
    try:
        with open(fn, "w") as f:
            f.write("# host anchor_v  path...   (an induced path of H on diam(H)+4 vertices,\n")
            f.write("# with ecc_H(anchor_v) = diam(H); certifies path(H) >= diam(H)+4)\n")
            done = set()
            for e in out:
                if e["nm"] in done or e["nm"] not in ("W43a", "W43b", "W43c", "W44a"):
                    continue
                S = e["cert"].get("L4")
                if S is None:
                    continue
                done.add(e["nm"])
                f.write("%s %d %s\n" % (e["nm"], e.get("L4v", S[0]),
                                        " ".join(str(x) for x in S)))
        print()
        print("  L4 certificates for the named hosts written to %s" % fn)
    except IOError as ex:
        print("  ** could not write the certificates: %s" % ex)

    print()
    print("=" * 78)
    ck(set(PARTS_RUN) == set(["PART0", "PART1", "PART2", "PART3", "PART4", "PART5",
                              "PART6"]),
       "all seven declared parts actually ran")
    print("PARTS RUN: %s" % ",".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
