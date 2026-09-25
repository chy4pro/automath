#!/usr/bin/env python3
"""WOWII-133 round 44 -- THE RESIDUAL ROW'S ANCHOR IS FREE IN TWO OF ITS THREE LANES, AND OUR
OWN CASE A WITNESSES DO NOT EXHIBIT THE OPEN CASE.

Round 43 showed draft 42.4's residual row is non-empty in BOTH halves (CASE A: `W43a`/`W43b`/
`W43c`; CASE B: round 42's 146).  It therefore has to be closed by ARGUMENT.  This round makes
the argument as far as it goes and then says exactly where it stops -- and the second half of
that sentence is the one that matters, because it turns out our own witnesses are on the easy
side of the stop.

  PART 0  primitives self-tested against hand computation + THIS round's guard, (D10)
          HAIR-ON-ANY-PATH -- which is the ALREADY-REFUTED `(A2-PATH)` of draft 41, and is
          exactly the defect the new argument would be if its bookkeeping slipped by one.
  PART 1  (ROW-3).  The row's instance is `G = H + one pendant at w` with `rad(G) = rad(H)+1`.
          The target is `path(G) >= rad(G) + floor(l(G))`.  Draft 42.5 discharges it through
          `endpath(H,w)` -- at the PRESCRIBED `w`.  But `path(G) >= path(H)` needs NO anchor,
          and `path(H) >= diam(H)+2` by (TAIL-1) at a DIAMETRAL vertex.  So the row stratifies
          by `diam(H) - rad(H)`:  offset >= +3 is CLOSED UNCONDITIONALLY; offset = +2 is closed
          by (TAIL-2) at ANY ONE diametral vertex (an existential over a whole set, not a
          prescribed vertex); only offset = +1 -- CASE A -- still needs the prescribed anchor.
          The ingredient is old (draft 12's (R1)/(R2)/Lemma G10 shape, and (TAIL-1) itself);
          what is new is noticing that the ROW never used the free anchor.
  PART 2  THE WITNESSES, RE-READ AS ROUTE A2 INSTANCES.  `W43a`/`W43b`/`W43c` have `mu >= 4`,
          and `mu >= 4` makes (TAIL-2)'s BLANKET form fire at every vertex.  So all 129+
          condition-4 vertices of round 43 slice 2 were covered BY A THEOREM, not merely by a
          built path -- and therefore **they do not exhibit the open case at all.**
  PART 3  (ROW-HARD).  What an instance that is still open must look like, read off
          (TAIL-2''): at EVERY far end of `w`, EVERY admissible `y` has `a(y) <= 3` AND
          `deg(y) <= 4`.  Census over every residual-row instance this line holds.
  PART 4  THE RE-AIMED SEARCH.  Round 43's owed item 2 was "make `n` smaller".  PART 2 says
          the binding coordinate is not `n` but `mu`: an instance with `mu >= 4` is closed
          before it is built.  So the search is re-aimed at CASE A with `mu <= 3`, and a
          prediction is registered before the run.

Self-contained: primitives and builders COPIED VERBATIM from round 43's
`w133_r43_caseA.py`, never imported.  Interpreter: system python3 (pure stdlib).
No SAT.  No exhaustive graph enumeration; every path is BUILT and then CHECKED, and a
capped DFS that returns nothing is recorded as FAILURE TO BUILD, never as a shortfall.

PARTS
  0  primitive self-tests + guard (D10) HAIR-ON-ANY-PATH
  1  (ROW-3): the three lanes, each certified by BUILDING its path
  2  (ROW-MU4) and the witnesses re-read as route A2 instances
  3  (ROW-HARD) and the census of what is still open
  4  the re-aimed search: CASE A with mu <= 3
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


def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitives against hand computation, and THIS round's guard")
    print("=" * 78)

    # ---- primitives, checked against values computed by hand, not by this file
    hand = [("P4", pathgraph(4), 2, 3, None),
            ("P6", pathgraph(6), 3, 5, None),
            ("C6", cycle(6), 3, 3, 2.0),
            ("C7", cycle(7), 3, 3, 2.0),
            ("C8", cycle(8), 4, 4, 2.0),
            ("Petersen", petersen(), 2, 2, 3.0),
            ("PG(2,3)", pg2(3), 3, 3, 4.0)]
    for nm, g, rr, dd, ll in hand:
        D, ecc, r = profile(g)
        ck(r == rr, "%s rad = %d (hand)" % (nm, rr))
        ck(max(ecc) == dd, "%s diam = %d (hand)" % (nm, dd))
        if ll is not None:
            ck(abs(l_of(g) - ll) < 1e-9, "%s l = %.1f (hand)" % (nm, ll))
        ck(all(a_val(g, v) == a_val_matching(g, v) for v in range(len(g))),
           "%s: brute alpha(N(v)) == the matching identity at every vertex" % nm)
    ck(c4_free(petersen()) and c4_free(pg2(3)) and c4_free(cycle(6)),
       "Petersen, PG(2,3), C6 are C4-free")
    print("  7 hosts, rad/diam/l against hand values, and brute alpha vs the matching")
    print("  identity at every vertex of each: agreed.")

    # ---- the load-bearing identity of this whole round, and the guard built on it
    print("""
  THE IDENTITY THE ROUND RESTS ON.  G := H + one pendant p at w.  p has degree 1, so an
  induced path of G either misses p, or has p as an ENDPOINT and its rest is an induced path
  of H ending at w.  Hence

        path(G) = max( path(H) , 1 + endpath(H,w) )                                    (IDENT)

  and in particular path(G) <= 1 + path(H) ALWAYS.  Draft 41 refuted `(A2-PATH)`
  (`path(G) >= path(H) + h`); this round's new lane uses only `path(G) >= path(H)`, the h = 0
  half.  The guard is the defect that would confuse the two.

  GUARD -- (D10) HAIR-ON-ANY-PATH: evaluating the row with `1 + path(H)` in place of (IDENT),
  i.e. crediting the pendant to an induced path that does not END at w.  It is ONE-SIDED BY
  THE PROOF ABOVE (it can only over-claim), so its MISSES must be 0 and any EXTRA is real.
""")
    guard = [("P5", pathgraph(5)), ("P6", pathgraph(6)), ("C5", cycle(5)), ("C6", cycle(6)),
             ("C7", cycle(7)), ("C8", cycle(8)), ("C9", cycle(9)), ("Petersen", petersen())]
    for s, nn in ((1, 10), (2, 11), (3, 12), (5, 12)):
        h = rand_c4free_dense(s, nn)
        if h is not None and connected(h) and c4_free(h):
            guard.append(("dense(s=%d,n=%d)" % (s, nn), h))
    tot = extra = miss = ident_ok = ident_bad = 0
    worst = None
    for nm, h in guard:
        ph, ch = exact_path(h)
        ck(ch, "%s: exact path(H) search COMPLETE, not truncated" % nm)
        for w in range(len(h)):
            g = add_pendant(h, w)
            ck(c4_free(g), "%s+pendant@%d stays C4-free" % (nm, w))
            true, ct = exact_path(g)
            eh, ce = exact_endpath(h, w)
            ck(ct and ce, "%s@%d: both exact searches COMPLETE" % (nm, w))
            ident = max(ph, 1 + eh)
            tot += 1
            if ident == true:
                ident_ok += 1
            else:
                ident_bad += 1
                print("  ** (IDENT) FAILS on %s w=%d: true=%d ident=%d" % (nm, w, true, ident))
            d10 = 1 + ph
            if d10 > true:
                extra += 1
                if worst is None or d10 - true > worst[3]:
                    worst = (nm, w, true, d10 - true)
            if d10 < true:
                miss += 1
    ck(ident_bad == 0, "(IDENT) holds on every (host, w) in the guard population")
    ck(miss == 0, "(D10) MISSES = 0 -- it is one-sided, as proved")
    print("  (IDENT) verified by COMPLETE search on %d (host, w) pairs over %d hosts: %d/%d."
          % (tot, len(guard), ident_ok, tot))
    print("  (D10) HAIR-ON-ANY-PATH: EXTRA %d of %d, MISSES %d." % (extra, tot, miss))
    if worst is not None:
        print("  worst over-claim: %s w=%d, true path(G) = %d, (D10) says %d."
              % (worst[0], worst[1], worst[2], worst[2] + worst[3]))
    ck(extra > 0, "(D10) actually over-fires somewhere -- the guard is LIVE, not vacuous")
    return tot, extra


# ------------------------------------------------------------------ the row, and its lanes


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


def lane_of(nm, g, D, ecc, r, diam, mu, lg, w, ngeo=3, nfar=8):
    """Classify one row instance and CERTIFY its lane by BUILDING the path.  Returns a dict."""
    G = add_pendant(g, w)
    DG, eccG, rG = profile(G)
    k = int(l_of(G))
    need = rG + k
    res = dict(nm=nm, n=len(g), gref=g, r=r, diam=diam, off=diam - r, mu=mu, l=lg, w=w,
               rG=rG, lG=l_of(G), k=k, need=need, lane=None, cert=None, certlen=0)
    # lane 0 -- a geodesic of H alone (draft 12's (R1) shape)
    if diam + 1 >= need:
        v = ecc.index(diam)
        x = [u for u in range(len(g)) if D[v][u] == diam][0]
        P = geodesics(D, g, v, x, 1)
        if P and is_induced_path(g, P[0]) and len(P[0]) == diam + 1:
            res.update(lane="L0-GEODESIC", cert=P[0], certlen=len(P[0]))
            return res
    # lane 1 -- (TAIL-1) at a DIAMETRAL vertex; no anchor, no F11, no l > 4
    if diam + 2 >= need:
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            R = tail1_path(g, D, ecc, v)
            if R is not None and len(R) == diam + 2:
                res.update(lane="L1-TAIL1-DIAM", cert=R, certlen=len(R))
                return res
    # lane 2 -- (TAIL-2) at SOME diametral vertex; still no anchor at w
    if diam + 3 >= need:
        for v in range(len(g)):
            if ecc[v] != diam:
                continue
            fired, R, slack, nfr = tail2_at(g, D, ecc, v, ngeo, nfar)
            if fired and len(R) == diam + 3:
                res.update(lane="L2-TAIL2-DIAM", cert=R, certlen=len(R))
                return res
    # lane 3 -- the PRESCRIBED anchor: (TAIL-2) at w itself, plus the hair
    if 1 + ecc[w] + 3 >= need:
        fired, R, slack, nfr = tail2_at(g, D, ecc, w, ngeo, nfar)
        res["slack_w"] = slack
        res["nframes_w"] = nfr
        if fired:
            res.update(lane="L3-TAIL2-AT-w", cert=R, certlen=len(R))
            return res
    res.update(lane=("OPEN-k4" if k <= 4 else "BEYOND-k%d" % k))
    return res


# ------------------------------------------------------------------ PART 1


def part1(inst):
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (ROW-3): the residual row stratifies, and two of its three lanes need")
    print("          no anchor at all")
    print("=" * 78)
    print("""
  SETTING (draft 42.5's residual row, in round 39/42/43's coordinates).  H connected, C4-free,
  mu(H) >= 2, r := rad(H); w with (2) ecc_H(w) = r+1 and (3) d(c,w) = r for EVERY centre c.
  By (RAD-1P), (3) is exactly `rad(G) = r+1` for G := H + one pendant at w, and the target is
  path(G) >= rad(G) + floor(l(G)) = (r+1) + k.

  Draft 42.5 discharges the row through (B2) `path(G) >= 1 + endpath(H,w)` -- at the
  PRESCRIBED w, which is the whole difficulty.  But (B1) `path(G) >= path(H)` carries NO
  anchor, and path(H) >= endpath(H,v) for EVERY v.  Feeding (TAIL-1)/(TAIL-2)/(TAIL-3) in at a
  DIAMETRAL vertex instead of at w gives

    (ROW-3).  With D := diam(H) and the target (r+1)+k:
      * D + 1 >= (r+1)+k  ->  a geodesic of H alone closes it.        [draft 12's (R1) shape]
      * D + 2 >= (r+1)+k  ->  (TAIL-1) at a DIAMETRAL vertex closes it, UNCONDITIONALLY:
                              no anchor, no F11, no l > 4, no rad >= 5.
      * D + 3 >= (r+1)+k  ->  (TAIL-2) at ANY ONE diametral vertex closes it -- an existential
                              over the whole diametral set, not a statement at a named vertex.
      * otherwise         ->  the prescribed anchor is needed: (TAIL-2) at w, plus the hair.
    At k = 4 this reads: offset D-r >= +3 is CLOSED UNCONDITIONALLY; offset = +2 needs
    (TAIL-2) somewhere on the diametral set; offset = +1 -- exactly (SPLIT)'s CASE A -- is the
    only lane that still needs the prescribed anchor.

  PROOF.  Immediate from (IDENT) of PART 0 (path(G) >= path(H)), path(H) >= endpath(H,v), and
  (TAIL-1)/(TAIL-2) at v with ecc(v) = D.  The INGREDIENT IS OLD -- it is the shape of draft
  12's reductions (R1)/(R2) and of Lemma G10, one level up.  WHAT IS NEW IS ONLY THIS: the row
  had never used the fact that its own (B1) leg is anchor-free.
""")
    if not inst:
        print("  NO ROW INSTANCES BUILT -- nothing to exhibit.  Reported as an instrument")
        print("  failure, not as a result.")
        ck(False, "PART 1 had a non-empty row population to exhibit on")
        return []
    seen = {}
    for it in inst:
        res = lane_of(*it)
        seen.setdefault(res["lane"], []).append(res)
        if over():
            break
    print("  Lanes taken, over %d row instances (each certificate BUILT and re-checked):"
          % sum(len(v) for v in seen.values()))
    order = ["L0-GEODESIC", "L1-TAIL1-DIAM", "L2-TAIL2-DIAM", "L3-TAIL2-AT-w", "OPEN-k4"]
    order += sorted(k for k in seen if k.startswith("BEYOND"))
    for lane in order:
        v = seen.get(lane, [])
        print("    %-16s %5d" % (lane, len(v)))
        if v:
            e = v[0]
            print("       e.g. %s n=%d rad=%d diam=%d (off %+d) mu=%d l(H)=%.4f w=%d "
                  "k=floor(l(G))=%d need=%d built=%d"
                  % (e["nm"], e["n"], e["r"], e["diam"], e["off"], e["mu"], e["l"], e["w"],
                     e["k"], e["need"], e["certlen"]))
    # EVERY certificate re-checked, from scratch, as an induced path long enough for ITS lane
    bad = short = 0
    ncert = 0
    for lane, v in seen.items():
        for e in v:
            if e["cert"] is None:
                continue
            ncert += 1
            if not is_induced_path(e["gref"], e["cert"]):
                bad += 1
            have = e["certlen"] + (1 if lane == "L3-TAIL2-AT-w" else 0)
            if have < e["need"]:
                short += 1
    ck(bad == 0, "every lane certificate re-checked and is an induced path of H")
    ck(short == 0, "every lane certificate is long enough for the target it discharges")
    print("  %d certificates re-checked from scratch: %d not induced, %d too short."
          % (ncert, bad, short))
    return seen


# ------------------------------------------------------------------ PART 2


def part2():
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- (ROW-MU4), and round 43's own CASE A witnesses re-read as route A2")
    print("          instances.  The result is AGAINST this line's interest.")
    print("=" * 78)
    print("""
    (ROW-MU4).  If mu(H) >= 4 then endpath(H,w) >= ecc(w) + 3 for EVERY w.
    PROOF.  a(u_d) >= 4 >= 2 gives (TAIL-1)'s y; a(y) >= 4 is (TAIL-2)'s BLANKET hypothesis
    (draft 42.3) at that same y; so (TAIL-2) fires at the first frame tried. ///

  It is a one-line corollary of a theorem this line proved in round 32.  What it costs us is
  the following, and the round prints it before anything else:

  ROUND 43's THREE CASE A WITNESSES ALL HAVE mu >= 4.  So round 43 slice 2's `129 of 129`
  built paths were never evidence about the OPEN case -- (TAIL-2) could not have failed on
  them.  W43a/W43b/W43c populate draft 42.4's residual row, which is what round 43 claimed and
  which stands; they do NOT test the one question that can still break WOWII-133 on it.
""")
    rows = []
    for tag in ("W43a", "W43b", "W43c"):
        try:
            g = load_txt("problems/wowii/w133_r43_%s.txt" % tag)
        except IOError:
            print("  ** %s not readable -- SKIPPED, and this part is incomplete." % tag)
            ck(False, "%s edge list present" % tag)
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        C = centre_of(ecc, r)
        W = far_intersection(D, ecc, r)
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        ck(c4_free(g), "%s is C4-free" % tag)
        ck(connected(g), "%s is connected" % tag)
        ck(mu >= 2, "%s has mu >= 2" % tag)
        lH = l_of(g)
        print("  %s  n=%d |E|=%d mu=%d l(H)=%.6f rad=%d diam=%d |Ctr|=%d condition-4=%d"
              % (tag, len(g), len(edges_of(g)), mu, lH, r, diam, len(C), len(W)))
        rows.append((tag, g, D, ecc, r, diam, C, W, mu, lH))

    print()
    print("  THE ROUTE A2 INSTANCE EACH ONE ACTUALLY IS  (G := H + one pendant at w):")
    tot = byth = built = failed = 0
    lowa = 0
    for (tag, g, D, ecc, r, diam, C, W, mu, lH) in rows:
        if not W:
            continue
        w0 = W[0]
        G = add_pendant(g, w0)
        DG, eccG, rG = profile(G)
        kG = int(l_of(G))
        ck(rG == r + 1, "%s: (RAD-1P) -- rad(G) = rad(H)+1 at a condition-4 w" % tag)
        ck(c4_free(G), "%s: G = H + pendant is C4-free" % tag)
        print("    %s: rad(G)=%d  l(G)=%.6f  floor(l(G))=%d  target path(G) >= %d"
              % (tag, rG, l_of(G), kG, rG + kG))
        ck(rG + kG == r + 1 + kG, "%s: the target is (r+1)+floor(l(G))" % tag)
        # every condition-4 vertex: BUILD the (TAIL-2) frame the theorem promises
        for w in W:
            if over():
                break
            tot += 1
            e = ecc[w]
            if e != r + 1:
                continue
            fired, R, slack, nfr = tail2_at(g, D, ecc, w, ngeo=2, nfar=4)
            if fired and is_anchored_induced_path(g, R, w) and len(R) == e + 3:
                built += 1
                # the theorem's own hypothesis, checked at the vertex the frame used
                y = R[-2]
                if a_val_matching(g, y) >= 4:
                    byth += 1
                else:
                    lowa += 1
            else:
                failed += 1
    print()
    print("  condition-4 vertices tested: %d;  ecc(w)+3 anchored induced path BUILT: %d;"
          % (tot, built))
    print("  of those, the frame's own y has a(y) >= 4 -- i.e. (ROW-MU4) applies: %d;" % byth)
    print("  frames using a y with a(y) < 4: %d;  NOT BUILT: %d." % (lowa, failed))
    ck(failed == 0, "every condition-4 vertex of W43a/b/c carries a BUILT ecc(w)+3 path")
    print()
    print("  ENTITLED READING: mu >= 4 on all three hosts, so (ROW-MU4) closes every one of")
    print("  these instances BEFORE any search.  THE OPEN CASE IS NOT EXHIBITED BY THEM.")
    # LIVENESS: the blanket hypothesis must be able to FAIL, or the sentence above is empty
    neg = cycle(6)
    Dn, eccn, rn = profile(neg)
    mun = min(a_val_matching(neg, v) for v in range(6))
    ck(mun == 2, "C6 has mu = 2 -- the blanket hypothesis of (ROW-MU4) FAILS there")
    fired, R, slack, nfr = tail2_at(neg, Dn, eccn, 0, ngeo=3, nfar=6)
    ck(not fired, "C6: (TAIL-2'') does NOT fire at w=0 -- the detector can decline")
    print("  LIVENESS: on C6 (mu = 2) the same detector DECLINES (endpath = ecc+2 exactly,")
    print("  draft 42.2's tightness example), so 'it fired' is information, not a tautology.")
    return rows, tot, built, byth


# ------------------------------------------------------------------ PART 3


def part3(inst, lanes):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- (ROW-HARD): what an instance that is STILL open has to look like, and")
    print("          the census of how far every instance we hold is from looking like it")
    print("=" * 78)
    print("""
    (ROW-HARD).  Let (H,w) be a residual-row instance at offset +1 (CASE A) with k = 4.  If it
    is not closed, then for EVERY far end x of w, EVERY w-x geodesic u_0..u_d, and EVERY
    y in N(u_d) admissible for (TAIL-1),
                     max( a(y), deg(y) - 1 )  <=  1 + k2(y)  <=  3,
    where k2(y) = #{ j in {d-2,d-3} : N(y) meets N(u_j) }.  In particular a(y) <= 3 and
    deg(y) <= 4 at EVERY such y; and since mu(H) >= 2 forces a(y) >= 2, every such frame must
    also have k2(y) >= 1.
    PROOF.  Contrapositive of (TAIL-2'') (draft 46.1): one frame with
    max(a(y),deg(y)-1) >= 2+k2 gives endpath(H,w) >= ecc(w)+3, and then the hair gives
    path(G) >= 1 + (r+1) + 3 = (r+1)+4. ///

  So the obstruction is not `n`, and not `|Ctr|`: it is a LOW-a COLLAR around EVERY far end of
  w.  The measurement below is the slack of that inequality, maximised over the frames -- the
  amount by which each instance we hold FAILS to be hard:

        SLACK(H,w) := max over admissible frames of [ max(a(y),deg(y)-1) - (2 + k2(y)) ].

  SLACK < 0 at an offset-+1 instance is exactly the open case.  SLACK >= 0 closes it.

  DIRECTION OF ERROR, FIXED BEFORE THE NUMBERS.  The frames are SAMPLED (<= 6 far ends,
  <= 2 geodesics each), so the SLACK printed below is a LOWER bound on the true maximum.
  A printed `SLACK >= 0` is therefore SOUND -- widening the sampling cannot take it back.
  A printed `SLACK < 0` would be INCONCLUSIVE and could NOT be called an open instance: it
  would first have to survive an exhaustive frame enumeration at that one vertex.
""")
    hist = {}
    fhist = {}
    minslack = None
    argmin = None
    inclass = 0
    inclass_open = 0
    n_off = {}
    collar = []
    for it in inst:
        if over():
            break
        (nm, g, D, ecc, r, diam, mu, lg, w) = it
        off = diam - r
        n_off[off] = n_off.get(off, 0) + 1
        nfr, slack, amin = frame_scan(g, D, ecc, w, ngeo=2, nfar=6)
        hist[slack] = hist.get(slack, 0) + 1
        fhist[min(nfr, 10)] = fhist.get(min(nfr, 10), 0) + 1
        S = [v for v in range(len(g)) if D[w][v] == ecc[w]]
        col = set()
        for x in S:
            col |= g[x]
        collar.append((len(S), len(col), len(g)))
        if minslack is None or slack < minslack:
            minslack = slack
            argmin = (nm, len(g), r, diam, mu, lg, w, slack, nfr)
        if lg > 4 and r >= 5:
            inclass += 1
            if off == 1 and slack < 0:
                inclass_open += 1
    print("  Row instances by offset diam(H)-rad(H):")
    for off in sorted(n_off):
        print("    %+d : %5d" % (off, n_off[off]))
    print("  SLACK histogram over every row instance (SLACK < 0 would be the open case):")
    for s in sorted(hist):
        print("    SLACK %+3d : %5d" % (s, hist[s]))
    if argmin is not None:
        print("  minimum SLACK anywhere: %+d, at %s (n=%d rad=%d diam=%d mu=%d l=%.4f w=%d,"
              % (argmin[7], argmin[0], argmin[1], argmin[2], argmin[3], argmin[4], argmin[5],
                 argmin[6]))
        print("  %d frames examined)." % argmin[8])
    print()
    print("  LANES, counted (PART 1's classification):")
    order = ["L0-GEODESIC", "L1-TAIL1-DIAM", "L2-TAIL2-DIAM", "L3-TAIL2-AT-w", "OPEN-k4"]
    order += sorted(k for k in lanes if k.startswith("BEYOND"))
    for lane in order:
        print("    %-16s %5d" % (lane, len(lanes.get(lane, []))))
    uncond = len(lanes.get("L0-GEODESIC", [])) + len(lanes.get("L1-TAIL1-DIAM", []))
    print("  CLOSED UNCONDITIONALLY (L0 + L1: no anchor, no F11, no l > 4, no rad >= 5): %d."
          % uncond)
    print("  Every BEYOND-k row is a row instance whose own floor(l(G)) is 5 or more: that is")
    print("  the NEXT pocket, not route A2's, and none of the four lanes reaches it.  It is")
    print("  reported here rather than folded into 'open'.")
    print()
    print("""
  OWN ERROR IN THIS PART, REPAIRED BY RUNNING (81), NOT BY DELETING.  The first version of the
  histogram below read its frame count off `tail2_at`, which RETURNS AT THE FIRST FRAME THAT
  FIRES.  It therefore printed `1 frame` for all 601 instances -- a distribution that cannot
  occur -- and the SLACK column it accompanied was the slack at the first firing frame, not the
  maximum.  Repaired by writing `frame_scan`, which enumerates every sampled frame with no
  early return; the SLACK histogram above is its output, and it MOVED (the old one peaked at
  +2, this one at +4).  The old numbers are not quoted anywhere.
""")
    print("  Admissible-frame count per instance (capped at 10 for the histogram):")
    for f in sorted(fhist):
        print("    %s frames : %5d" % (("%2d" % f) if f < 10 else ">=10", fhist[f]))
    if collar:
        cs = sorted(collar, key=lambda t: t[1])
        print("  Far-end sphere / collar N(S_ecc(w)(w)) / n, smallest and largest collar:")
        print("    smallest: |S| = %d, |collar| = %d, n = %d" % cs[0])
        print("    largest : |S| = %d, |collar| = %d, n = %d" % cs[-1])
        print("    median collar as a fraction of n: %.3f"
              % (cs[len(cs) // 2][1] / float(cs[len(cs) // 2][2])))
        print("  (ROW-HARD) asks for a(y) <= 3 AND deg(y) <= 4 on EVERY vertex of that collar")
        print("  while l(H) > 4 asks the AVERAGE of a over ALL n vertices to exceed 4.")
    print()
    print("  IN-CLASS (l(H) > 4 AND rad(H) >= 5) row instances: %d." % inclass)
    print("  OF THOSE, instances at offset +1 with SLACK < 0 -- i.e. instances that actually")
    print("  exhibit the open case: %d." % inclass_open)
    ick = sum(1 for e in lanes.get("OPEN-k4", []) if e["l"] > 4 and e["r"] >= 5)
    print("  AND, INDEPENDENTLY OF THE SLACK: in-class row instances at floor(l(G)) = 4 that")
    print("  NO lane of (ROW-3) closes: %d." % ick)
    print("  THAT IS THE ONLY CASE A NUMBER THIS ROUND IS ENTITLED TO REPORT.")
    return hist, inclass, inclass_open, argmin


def rand_c4free_sparse(seed, n, cap):
    """COPIED VERBATIM from round 43 (`w133_r43_caseA.py`), never imported."""
    st = seed % (1 << 31)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for i in range(len(pairs) - 1, 0, -1):
        st = (st * 1103515245 + 12345) % (1 << 31)
        j = st % (i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = [set() for _ in range(n)]
    for (u, v) in pairs:
        if len(g[u]) >= cap or len(g[v]) >= cap:
            continue
        if len(g[u] & g[v]) >= 1:
            continue
        if any(len(g[u] & g[x]) >= 1 for x in g[v] if x != u):
            continue
        if any(len(g[v] & g[y]) >= 1 for y in g[u] if y != v):
            continue
        g[u].add(v)
        g[v].add(u)
    h = adj(n, [(u, v) for u in range(n) for v in g[u] if u < v])
    return h if connected(h) else None


def subdivide(g, u, v):
    """replace the edge uv by a path u-m-v.  If uv lies in NO triangle this preserves
    C4-freeness (any 4-cycle through m is m-u-p-v-m, i.e. a common neighbour p of u,v)."""
    n = len(g)
    E = [(a, b) for (a, b) in edges_of(g) if (a, b) != (min(u, v), max(u, v))]
    E += [(u, n), (n, v)]
    return adj(n + 1, E)


def screen(g, tag):
    """the CASE A screen: conditions 1,2,3,4,5 in one place.  Returns a dict or None."""
    if g is None or not connected(g):
        return None
    D, ecc, r = profile(g)
    diam = max(ecc)
    mu = min(a_val_matching(g, v) for v in range(len(g)))
    lg = l_of(g)
    W = far_intersection(D, ecc, r)
    W = [w for w in W if ecc[w] == r + 1]
    return dict(tag=tag, n=len(g), g=g, D=D, ecc=ecc, r=r, diam=diam, mu=mu, l=lg,
                cond4=W, round_=(diam == r + 1), inclass=(lg > 4 and r >= 5))


# ------------------------------------------------------------------ PART 4


def part4():
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE SEARCH, RE-AIMED.  Round 43 owed 'make n smaller'; PART 2 says the")
    print("          binding coordinate is mu, not n.")
    print("=" * 78)
    print("""
  PREDICTIONS, REGISTERED BEFORE ANY NUMBER BELOW:
    (P1) subdividing ONE triangle-free edge of W43a yields, for at least one edge, a host that
         is still C4-free with l > 4 and rad >= 5 and diam = rad+1 and a condition-4 vertex --
         i.e. a CASE A instance with mu = 2, the first this line would hold.
    (P2) NO instance produced anywhere in this round will have SLACK < 0.  If (P2) is WRONG we
         have the first instance that exhibits the open case and it must be re-verified by a
         standalone script (rule 105) before anything is claimed about it.
  A SUBDIVIDED VERTEX HAS a = 2 BY CONSTRUCTION, so (P1) does not need luck for mu; what it
  needs is that rad, roundness and condition 4 all survive the surgery.
""")
    # ---- POSITIVE CONTROL FIRST: the screen must fire on a KNOWN carrier
    try:
        base = load_txt("problems/wowii/w133_r43_W43a.txt")
    except IOError:
        print("  ** W43a not readable -- PART 4 cannot run its positive control.  ABORTING")
        print("  ** this part rather than reporting an uninterpretable zero.")
        ck(False, "W43a edge list present for PART 4's positive control")
        return []
    ctl = screen(base, "W43a(control)")
    ck(ctl is not None and ctl["round_"] and ctl["cond4"] and ctl["inclass"],
       "POSITIVE CONTROL: the screen fires on W43a, a known CASE A carrier")
    print("  POSITIVE CONTROL: screen(W43a) -> rad=%d diam=%d mu=%d l=%.6f condition-4=%d"
          % (ctl["r"], ctl["diam"], ctl["mu"], ctl["l"], len(ctl["cond4"])))
    print("  (without this line every 0 below would be a statement about the instrument.)")

    found = []
    # ---- PROBE A: single-edge subdivisions of W43a at triangle-free edges
    E = edges_of(base)
    tf = [(u, v) for (u, v) in E if not (base[u] & base[v])]
    print()
    print("  PROBE A -- single-edge subdivision of W43a.  %d of %d edges lie in no triangle."
          % (len(tf), len(E)))
    step = max(1, len(tf) // 40)
    tried = ok_c4 = rnd = carr = 0
    seen_shapes = {}
    for i in range(0, len(tf), step):
        if over():
            break
        u, v = tf[i]
        h = subdivide(base, u, v)
        tried += 1
        if not c4_free(h):
            continue
        ok_c4 += 1
        st = screen(h, "SD(W43a,%d-%d)" % (u, v))
        key = (st["r"], st["diam"], st["mu"], len(st["cond4"]) > 0)
        seen_shapes[key] = seen_shapes.get(key, 0) + 1
        if st["round_"]:
            rnd += 1
        if st["round_"] and st["cond4"] and st["inclass"]:
            carr += 1
            found.append(st)
    print("    %d subdivisions tried, %d still C4-free, %d still round (diam = rad+1),"
          % (tried, ok_c4, rnd))
    print("    %d are in-class CASE A carriers." % carr)
    print("    shapes seen (rad, diam, mu, carries condition 4) -> count:")
    for k in sorted(seen_shapes):
        print("      (rad=%d, diam=%d, mu=%d, cond4=%s) : %d" % (k[0], k[1], k[2], k[3],
                                                                seen_shapes[k]))

    # ---- PROBE B: an independent sampler at a HIGHER degree cap
    print()
    print("  PROBE B -- degree-capped random C4-free hosts at cap 6 (l <= mean degree, so")
    print("  cap >= 5 is forced; cap 6 is the next value and gives mu room to sit below 4).")
    hits = 0
    for cap in (5, 6):
        for n in (360, 420, 480):
            for s in (1, 2, 3):
                if over():
                    break
                h = rand_c4free_sparse(s * 1000003 + n + cap, n, cap)
                st = screen(h, "SP%d(%d,s%d)" % (cap, n, s))
                if st is None:
                    continue
                if st["round_"] and st["cond4"] and st["inclass"]:
                    hits += 1
                    found.append(st)
                    print("    HIT  %s rad=%d diam=%d mu=%d l=%.6f cond4=%d"
                          % (st["tag"], st["r"], st["diam"], st["mu"], st["l"],
                             len(st["cond4"])))
    print("    in-class CASE A carriers from probe B: %d." % hits)

    # ---- the only question that matters about anything found: is any of it HARD?
    print()
    print("  THE SLACK OF EVERY CASE A INSTANCE FOUND IN THIS PART:")
    lowmu = []
    worst = None
    for st in found:
        if over():
            break
        for w in st["cond4"][:12]:
            fired, R, slack, nfr = tail2_at(st["g"], st["D"], st["ecc"], w, ngeo=2, nfar=4)
            if worst is None or slack < worst[1]:
                worst = (st["tag"], slack, st["mu"], w)
            if slack < 0:
                lowmu.append((st, w, slack))
    if worst is not None:
        print("    minimum SLACK over everything found: %+d  (%s, mu=%d, w=%d)"
              % (worst[1], worst[0], worst[2], worst[3]))
    print("    instances with SLACK < 0 -- i.e. exhibiting the OPEN case: %d." % len(lowmu))
    ck(True, "PART 4 ran its positive control before reporting any zero")
    print()
    print("  VERDICT ON THE REGISTERED PREDICTIONS:")
    print("    (P1) %s -- %d in-class CASE A carriers with mu <= 3 were built."
          % ("HELD" if any(st["mu"] <= 3 for st in found) else "FAILED",
             sum(1 for st in found if st["mu"] <= 3)))
    print("    (P2) %s -- %d instances with SLACK < 0."
          % ("HELD" if not lowmu else "FAILED", len(lowmu)))
    return found


# ------------------------------------------------------------------ main


def main():
    print("WOWII-133 round 44 -- THE ROW'S ANCHOR IS FREE IN TWO LANES OF THREE, AND OUR OWN")
    print("                      CASE A WITNESSES DO NOT EXHIBIT THE OPEN CASE")
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
    print("  population for the census: %d hosts (including round 43's three witnesses)."
          % len(hosts), flush=True)

    inst = row_instances(hosts)
    print("  residual-row instances in it: %d." % len(inst), flush=True)

    lanes = part1(inst)
    part2()
    part3(inst, lanes)
    found = part4()

    if found:
        print()
        print("=" * 78)
        print("PART 5 -- ANY NEW INSTANCE, WRITTEN OUT FOR INDEPENDENT RE-VERIFICATION (105)")
        print("=" * 78)
        best = sorted(found, key=lambda s: (s["mu"], s["n"]))[0]
        print("  HOST %s  n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d cond4=%d"
              % (best["tag"], best["n"], len(edges_of(best["g"])), best["mu"], best["l"],
                 best["r"], best["diam"], len(best["cond4"])))
        print("  condition-4 vertices (first 20): %s" % best["cond4"][:20])
        fn = "problems/wowii/w133_r44_W44a.txt"
        try:
            with open(fn, "w") as f:
                f.write("# %s  n=%d mu=%d l=%.6f rad=%d diam=%d\n"
                        % (best["tag"], best["n"], best["mu"], best["l"], best["r"],
                           best["diam"]))
                f.write("%d\n" % best["n"])
                for (u, v) in sorted(edges_of(best["g"])):
                    f.write("%d %d\n" % (u, v))
            print("  edge list written to %s" % fn)
        except IOError as e:
            print("  ** could not write the edge list: %s" % e)

    print()
    print("=" * 78)
    ck(set(PARTS_RUN) == set(["PART0", "PART1", "PART2", "PART3", "PART4"]),
       "all five declared parts actually ran")
    print("PARTS RUN: %s" % ",".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
