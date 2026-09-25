#!/usr/bin/env python3
"""WOWII-133 round 43 -- E46 IS HARVESTED AND AUDITED, AND CASE A IS RE-COORDINATED.

Round 42 proved (SPLIT) and built 146 CASE B instances.  CASE A (diam = rad+1) survived, and
brief E46 was sent for it.  E46 came back **UNSETTLED**: no construction, no emptiness proof,
three claimed side results, a stated break point and a repair program.  This file HARVESTS it,
which on this line means: re-derive every claim it makes, keep what survives, name what does
not, and then re-choose the coordinates.

  * PART 1  E46's three side results, audited line by line.  (R1) self-destructs inside its own
            proof (E46 says so).  (R2) is the triangle inequality and is correct.  (R3) -- its
            only real claim, "a strict strengthening of (CS-3) by 2" -- has an INVALID proof: it
            asserts `Ctr` is disjoint from `B_r(w)` while simultaneously assuming `Ctr` is a
            subset of `S_r(w)`, and its count uses the sphere `S_r(w)` twice.  The repaired and
            GENERALISED form (R3'') is proved here and asserted on live data.
  * PART 2  THE COORDINATE CHANGE.  Condition 4 says `d(c,w) = rad` for every centre; since
            `d(c,w) <= ecc(c) = rad` always, condition 4 says exactly that `w` realises the
            eccentricity of EVERY centre at once:  w is in the intersection of the spheres
            S_rad(c), c in Ctr.  So on a ROUND host the whole class of brief E46 is a property
            of the HOST alone -- (CA-EQ) -- and a host with a UNIQUE centre carries it for free.
            The search over (host, w) pairs collapses to a search for round hosts with a
            CLUSTERED centre.  E46's break point is stated in the wrong variable: it asks for a
            "dominant centre subset" of one sphere, i.e. a BIG centre; what is needed is a small
            and above all a LOCALISED one.
  * PART 3  (SYM-BAR): a symmetry obstruction.  If a group of automorphisms permutes a partition
            of V transitively and one part has diameter < rad, NO vertex of G satisfies
            condition 4.  Rotation-symmetric necklaces are built, their rotation is verified to
            be an automorphism by machine, and the lemma is exhibited on them.
  * PART 4  THE SWEEP.  Round 42's family rebuilt, plus new ASYMMETRIC designs (subdivided
            junctions, thin junctions, thin-and-long junctions, one odd block) built to localise
            the centre.  Predictions registered BEFORE the numbers.  The decisive test of
            PART 2 run on every in-class round host; the localisation diagnostic E46 asked for
            (its section 5.1) run in the coordinates of PART 2.

Self-contained: primitives COPIED from round 42's file, never imported.
Interpreter: system python3 (pure stdlib).  No SAT.  No exhaustive graph enumeration --
every host is a designed construction with seeded-random matchings.

PARTS
  0  primitive self-tests + THIS round's guard (D9 COUNT-FOR-PLACEMENT)
  1  E46 AUDIT: (R1)/(R2)/(R3), and the repaired (R3'')
  2  (FAR) / (CA-EQ): the coordinate change, proved and asserted as an equivalence
  3  (SYM-BAR): the symmetry obstruction, proved and exhibited
  4  THE SWEEP: round 42's family + the new asymmetric designs, and the decisive test
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 900.0
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


# ------------------------------------------------------------------ PART 0


def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitive self-tests and THIS round's guard")
    print("=" * 78)

    P3 = pathgraph(3)
    D, ecc, r = profile(P3)
    ck(r == 1 and max(ecc) == 2, "P3 rad 1 diam 2")
    ck(centre_of(ecc, 1) == [1], "P3 unique centre")
    ck(sorted(far_intersection(D, ecc, r)) == [0, 2], "P3: both ends satisfy condition 4")

    P4 = pathgraph(4)
    D, ecc, r = profile(P4)
    ck(r == 2 and max(ecc) == 3, "P4 rad 2 diam 3 (a ROUND graph)")
    ck(centre_of(ecc, 2) == [1, 2], "P4 centre = 2 vertices")
    ck(far_intersection(D, ecc, r) == [], "P4: NO vertex satisfies condition 4")

    P6 = pathgraph(6)
    D, ecc, r = profile(P6)
    ck(r == 3 and far_intersection(D, ecc, r) == [], "P6: no condition-4 vertex")

    for gg, nm in ((cycle(7), "C7"), (cycle(8), "C8"), (petersen(), "Petersen")):
        D, ecc, r = profile(gg)
        ck(max(ecc) == r, "%s is self-centred" % nm)
        ck(far_intersection(D, ecc, r) == [], "%s self-centred => no condition-4 vertex" % nm)
    print("  primitives + (FAR) evaluator agree with hand computation on P3/P4/P6/C7/C8/Petersen")

    g = pg2(3)
    ck(len(g) == 26 and c4_free(g), "PG(2,3) incidence graph: 26 vertices, C4-free")
    D, ecc, r = profile(g)
    ck(r == 3 and max(ecc) == 3, "PG(2,3) incidence graph is self-centred with rad 3")
    for v in (0, 5, 13, 20):
        ck(a_val(g, v) == a_val_matching(g, v) == 4, "PG(2,3): brute a(.) == matching a(.) == 4")

    # ---- THE GUARD ON THIS ROUND'S PREDICATE
    print()
    print("  GUARD.  CLASS CLAIMED: any evaluator that decides whether a host CAN carry a")
    print("  condition-4 vertex from the SIZE of its centre instead of from the PLACEMENT of")
    print("  its centre.  This is not r34's zero-step, r35's one-step, r36's late-block,")
    print("  r37's off-by-one/anchor-drift, r38's cost-evaluator, r39's centre-widen/quantifier-")
    print("  swap/stratum-offset, r40's sphere-shift, r41's table-trust/peri-as-noncentral, nor")
    print("  r42's diam-for-ecc/mean-deg-for-l.  It is the defect brief E46's own section 3")
    print("  fell into, and this round's whole method is the distinction it erases.")
    print()
    print("  (D9) COUNT-FOR-PLACEMENT: decide 'host may carry condition 4' by (CS-1'), i.e. by")
    print("       |Ctr| <= max_{w not in Ctr} |S_rad(w)|, instead of by the correct test")
    print("       'the intersection of the spheres S_rad(c) over c in Ctr is non-empty'.")
    print("  ONE-SIDED BY A THEOREM: if some w satisfies condition 4 then Ctr is contained in")
    print("  S_rad(w), so |Ctr| <= |S_rad(w)| <= max_w |S_rad(w)|.  So (D9) can only OVER-fire,")
    print("  never miss -- and a guard that can only over-fire is worthless unless it actually")
    print("  DOES over-fire on live data.  Measured below.")
    guard_hosts = []
    guard_hosts.append((pathgraph(3), "P3"))
    guard_hosts.append((pathgraph(4), "P4"))
    guard_hosts.append((pathgraph(6), "P6"))
    guard_hosts.append((cycle(9), "C9"))
    guard_hosts.append((petersen(), "Petersen"))
    for spec in (([3] * 5, 104729 + 5, 1.0, "any", None, "NL(3^5,s1)"),
                 ([3] * 6, 104729 + 6, 1.0, "any", None, "NL(3^6,s1)"),
                 ([3, 2] * 3, 6700417 + 6 * 31, 1.0, "any", (1.0, 0.4), "NLsa(6,s1)"),
                 ([3, 2] * 3, 3 * 6700417 + 6 * 31, 1.0, "any", (1.0,), "NLsd(6,s3)"),
                 ([3, 2] * 3, 4 * 6700417 + 6 * 31, 1.0, "any", (1.0,), "NLsd(6,s4)"),
                 ([3] * 6, 3 * 2971215073 % (1 << 31) + 6 * 7, 1.0, "any", (1.0,),
                  "NLkd(3^6,s3)"),
                 ([3, 2, 3, 2, 3, 2], 5 * 6700417 + 6 * 31, 1.0, "any", (1.0,),
                  "NLsd(6,s5)"),
                 ([3, 2, 3, 2, 3], 3 * 6700417 + 5 * 31, 1.0, "any", (1.0,), "NLsd(5,s3)"),
                 ([3, 2, 3, 2, 3], 4 * 6700417 + 5 * 31, 1.0, "any", (1.0,), "NLsd(5,s4)")):
        qs, sd, fr, md, frs, nm = spec
        gg = necklace(qs, sd, fr, md, frs)
        if connected(gg):
            guard_hosts.append((gg, nm))
    fires_d9 = fires_ok = extra = miss = 0
    carriers = []
    print()
    print("    %-14s %5s %5s %6s %8s %10s %8s" %
          ("guard host", "n", "rad", "diam", "|Ctr|", "max|S_r(w)|", "cond-4"))
    for gg, nm in guard_hosts:
        n = len(gg)
        D, ecc, r = profile(gg)
        C = centre_of(ecc, r)
        best = 0
        for w in range(n):
            if ecc[w] == r:
                continue
            sz = sum(1 for v in range(n) if D[w][v] == r)
            best = max(best, sz)
        d9 = (len(C) <= best)
        inter = far_intersection(D, ecc, r)
        ok = (len(inter) > 0)
        fires_d9 += 1 if d9 else 0
        fires_ok += 1 if ok else 0
        if d9 and not ok:
            extra += 1
        if ok and not d9:
            miss += 1
        if ok:
            carriers.append(nm)
        print("    %-14s %5d %5d %6d %8d %10d %8s" %
              (nm, n, r, max(ecc), len(C), best, "YES(%d)" % len(inter) if ok else "no"))
        ck(not (ok and not d9), "(D9) must never miss: %s" % nm)
    print()
    print("    guard hosts %d ; correct predicate FIRES on %d ; (D9) fires on %d"
          % (len(guard_hosts), fires_ok, fires_d9))
    print("    (D9) EXTRA (fires where the correct test does not): %d ; MISSES: %d"
          % (extra, miss))
    print("    hosts CARRYING the correct predicate: %s" % (", ".join(carriers) or "NONE"))
    ck(extra > 0, "the guard must be DISTINGUISHABLE on live data")
    ck(fires_ok > 0, "the guard host set must contain a CARRIER of the correct predicate")
    ck(miss == 0, "(D9) is one-sided by the theorem above")


# ------------------------------------------------------------------ PART 1


def part1(pairs):
    """pairs: list of (name, g, D, ecc, r, w) with w satisfying condition 4."""
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- E46 AUDITED: what came back, and what of it survives")
    print("=" * 78)
    print("""
  E46 returned UNSETTLED and said so in its first line.  It offered: a re-derivation of our
  section 4 (agrees), three 'small new results' (R1)(R2)(R3), a break point, and a repair
  programme.  Audited one by one.

  (R1)  WITHDRAWN BY ITS OWN AUTHOR, INSIDE ITS OWN PROOF.  The reply writes the proof, marks
        two of its own steps '**this step is vacuous**' and 'also vacuous', and retreats to
        (R1'): every vertex of S_{r+1}(w) is peripheral, Ctr is inside S_r(w), ecc <= diam
        everywhere.  That is (PER-A) plus condition 4 restated.  NOTHING NEW.  Recorded as
        an honest self-correction, not as a result.

  (R2)  CORRECT and it is the triangle inequality: if d(u,y) = r+1 and d(u,w) = j then
        d(w,y) >= r+1-j, so a diametral witness for u lies at distance >= r+1-j from w.
        Asserted on live data below.  NOTHING NEW, but nothing wrong.

  (R3)  ITS ONLY REAL CLAIM -- '|Ctr| <= n - delta(delta-1) - r, tighter than (CS-3) by 2'.
        THE PROOF IS INVALID.  Two independent faults in one sentence:
          (i)  it says 'the sets Ctr and S_{r+1}(w) are disjoint from each other AND FROM
               B_r(w)' while its own hypothesis is Ctr contained in S_r(w) -- and
               S_r(w) is contained in B_r(w).  The step contradicts the hypothesis;
          (ii) the count adds '(r-2) vertices for the spheres S_3..S_r' and THEN adds |Ctr|
               again.  S_r is counted twice.
        Removing the double count leaves a gain of exactly ONE, not two.  We are NOT entitled
        to call the STATEMENT false: no instance with r >= 3 satisfying conditions 1,3,4 is
        known to this line, so there is nothing to test it on.  It is UNPROVED.
""")
    # (R2) asserted on live data
    r2_pairs = 0
    for (nm, g, D, ecc, r, w) in pairs:
        n = len(g)
        diam = max(ecc)
        for u in range(n):
            if ecc[u] != diam:
                continue
            j = D[w][u]
            wit = [y for y in range(n) if D[u][y] == diam]
            for y in wit[:3]:
                ck(D[w][y] >= diam - j, "(R2) on %s: witness at distance >= diam-d(w,u)" % nm)
                r2_pairs += 1
        if r2_pairs > 400:
            break
    print("  (R2) asserted on %d (vertex, witness) pairs of live condition-4 hosts." % r2_pairs)

    print("""
  (R3'') THE REPAIR, PROVED HERE, AND IT IS STRICTLY MORE GENERAL THAN WHAT E46 ASKED FOR.

    Let G be connected, C4-free, delta >= 2, r = rad(G) >= 3, and let w satisfy condition 4
    (d(c,w) = rad for every centre c).  Write ecc(w) = r + t.  Then t >= 1 by (BRACKET), and

            |Ctr(G)|  <=  n - delta(delta-1) - r + 2 - t.

    Proof.  The spheres S_0(w),...,S_{ecc(w)}(w) are all non-empty and partition V.
    (CS-2) gives |S_0|+|S_1|+|S_2| >= 1 + delta(delta-1).  The spheres S_3,...,S_{r-1} are
    r-3 further non-empty sets.  Condition 4 puts Ctr inside S_r(w) and the spheres
    S_{r+1},...,S_{r+t} are t further non-empty sets disjoint from all of those.  Hence
    n >= (1 + delta(delta-1)) + (r-3) + |Ctr| + t.  []

    Compare: (CS-3) is n - delta(delta-1) - r + 2, i.e. (R3'') at t = 0.  So the gain is
    exactly t, and E46 claimed a gain of 2 at t = 1.  (R3'') ALSO NEEDS NO ROUNDNESS -- it
    holds for every condition-4 vertex, CASE A or CASE B, which is what makes it assertable
    at all: our 146 CASE B instances have t = 1 and the rest of round 42's 1 095 condition-4
    vertices have t >= 1, and every one of them is a test of it.  E46's version could only
    ever have been tested on objects nobody has.
""")
    n_as = 0
    tmin = None
    worst = None
    for (nm, g, D, ecc, r, w) in pairs:
        n = len(g)
        delta = min(len(g[v]) for v in range(n))
        C = centre_of(ecc, r)
        t = ecc[w] - r
        ck(t >= 1, "(BRACKET): ecc(w) >= rad+1 on %s" % nm)
        if r < 3 or delta < 2:
            continue
        bound = n - delta * (delta - 1) - r + 2 - t
        e46 = n - delta * (delta - 1) - r
        ck(len(C) <= bound, "(R3'') on %s: |Ctr|=%d <= %d" % (nm, len(C), bound))
        n_as += 1
        slack = bound - len(C)
        if worst is None or slack < worst[0]:
            worst = (slack, nm, len(C), bound, e46, n, delta, r, t)
        tmin = t if tmin is None else min(tmin, t)
    print("  (R3'') asserted on %d live condition-4 (host, w) pairs, minimum t = %s."
          % (n_as, tmin))
    if worst is not None:
        print("  tightest case: %s  n=%d delta=%d r=%d t=%d  |Ctr|=%d  (R3'')<=%d  slack %d"
              % (worst[1], worst[5], worst[6], worst[7], worst[8], worst[2], worst[3],
                 worst[0]))
        print("                 E46's (R3) would have said <= %d: NUMERICALLY TIGHTER BY %d,"
              % (worst[4], worst[3] - worst[4]))
        print("                 and UNPROVED -- the extra 1 is exactly the sphere S_r(w) its")
        print("                 proof counts twice.  Both bounds are VACUOUS on this family")
        print("                 (delta = 3 or 4), exactly as E46 itself says of its own (R3).")
    print()
    print("  VERDICT ON E46, stated as the number we are entitled to: of three claimed new")
    print("  results, ONE was withdrawn by its author mid-proof, ONE is the triangle")
    print("  inequality, and ONE has an invalid proof.  NEW USABLE THEOREMS FROM E46: 0.")
    print("  What E46 IS worth is its section 3 -- the break point -- and section 5.1's ask")
    print("  for a localisation diagnostic.  PART 2 shows the break point is stated in the")
    print("  wrong variable, and PART 4 runs the diagnostic in the right one.")


# ------------------------------------------------------------------ PART 2


def part2(hosts):
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- (FAR) and (CA-EQ): CASE A is a property of the HOST, not of a pair")
    print("=" * 78)
    print("""
  (FAR).  For any G and any w:  w satisfies condition 4  <=>  w lies in the intersection of
  the spheres S_rad(c) taken over ALL centres c.
  Proof.  d(c,w) <= ecc(c) = rad for every centre, so 'd(c,w) = rad' says w realises the
  eccentricity of c.  Condition 4 asks that of every centre at once.  []

  (CA-EQ).  Let G be ROUND (diam = rad+1) with rad >= 1.  Then G carries an instance of brief
  E46's class 1-4 if and only if  INTERSECTION_{c in Ctr} S_rad(c)  is NON-EMPTY; and any w in
  that intersection is an instance, with ecc(w) = rad+1 automatic by (PER-A).
  Proof.  (FAR), plus (PER-A) for the free conjunct: w in the intersection has d(c,w) = rad
  >= 1 for every centre, so w is not itself a centre, so ecc(w) = diam = rad+1.  []

  (CA-1).  If |Ctr(G)| = 1 then the intersection is S_rad(c) for the unique centre c, which is
  non-empty by definition of eccentricity.  SO EVERY ROUND HOST WITH A UNIQUE CENTRE CARRIES
  AN INSTANCE, and no search is needed on it.
  More generally the obstruction is not that Ctr is BIG, it is that Ctr is SPREAD: a set of
  centres with no common eccentricity-witness.

  WHAT THIS COSTS E46's BREAK POINT.  E46 section 3 item 1 asks for a 'dominant centre subset:
  |Ctr| between roughly half and two-thirds of |S_r(w)|'.  That is not a requirement of the
  problem, it is a readback of our four live hosts -- and it does not even describe them
  (12/44 is 27%, not 'half to two-thirds').  Condition 4 imposes NO lower bound on |Ctr|;
  |Ctr| = 1 is the EASIEST case, not an excluded one.  A search steered by E46's section 3
  would have hunted the hardest corner of the class and skipped the free one.  We keep E46's
  section 3 items 2-4; item 1 is struck.
""")
    eq_ok = 0
    uniq = 0
    uniq_carry = 0
    for (nm, g, st) in hosts:
        n = st["n"]
        D, ecc, r = st["D"], st["ecc"], st["r"]
        brute = [w for w in range(n) if maximally_far(D, ecc, r, w)]
        ck(sorted(brute) == sorted(st["inter"]), "(FAR) equivalence on %s" % nm)
        eq_ok += 1
        if len(st["C"]) == 1:
            uniq += 1
            if len(st["inter"]) > 0:
                uniq_carry += 1
            ck(len(st["inter"]) > 0, "(CA-1): unique centre => condition-4 vertex on %s" % nm)
    print("  (FAR) asserted as an EQUIVALENCE against the brute condition-4 test on %d hosts."
          % eq_ok)
    print("  hosts with |Ctr| = 1 in this round's whole population: %d ; every one of them"
          % uniq)
    print("  carries a condition-4 vertex: %d/%d  ((CA-1), asserted not assumed)."
          % (uniq_carry, uniq))


# ------------------------------------------------------------------ PART 3


def part3():
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- (SYM-BAR): symmetry alone can forbid condition 4")
    print("=" * 78)
    print("""
  (SYM-BAR).  Let G be connected, let P be a partition of V(G), and let GAMMA be a group of
  automorphisms of G that permutes the parts of P TRANSITIVELY.  If some part P0 satisfies
  max{ d_G(u,v) : u,v in P0 } < rad(G), then NO vertex of G satisfies condition 4.

  Proof.  Ctr(G) is invariant under every automorphism, hence a union of GAMMA-orbits.  Let
  c be a centre and let w be any vertex, lying in the part P(w).  By transitivity there is
  gamma in GAMMA with gamma(P(c)) = P(w), so gamma(c) lies in P(w), and gamma(c) is a centre.
  All parts are isomorphic images of P0 under distance-preserving maps, so
  d(w, gamma(c)) <= max{d(u,v) : u,v in P(w)} = max{d(u,v) : u,v in P0} < rad.  Condition 4
  demands d(c',w) = rad for EVERY centre c'; the centre gamma(c) violates it.  []

  Corollaries.  (a) A vertex-transitive graph (parts = singletons, part diameter 0 < rad) has
  no condition-4 vertex -- which also follows from self-centredness, but (SYM-BAR) does not
  need it.  (b) A necklace of m blocks whose block rotation is an automorphism has no
  condition-4 vertex as soon as the block diameter is < rad -- and for our blocks the block
  diameter is 3 while we need rad >= 5.  SO EVERY ROTATION-SYMMETRIC NECKLACE IS BARREN, FOR
  A REASON, AND NO SEARCH ON ONE MEASURES ANYTHING.

  This is the mechanism behind round 42's four live hosts and it is why the sweep in PART 4
  is built out of ASYMMETRIC designs.  The necklaces of round 42 use a fresh random injection
  at each junction, so they are NOT exactly symmetric and (SYM-BAR) does not apply to them as
  a theorem -- what PART 4 measures is whether they behave as if it did.
""")
    rows = []
    for (q, m, seed, frac) in ((3, 5, 11, 1.0), (3, 6, 12, 1.0), (3, 7, 13, 1.0),
                               (3, 6, 14, 0.5), (5, 5, 15, 1.0), (3, 8, 16, 1.0),
                               (2, 7, 17, 1.0), (2, 9, 18, 1.0)):
        if over():
            break
        g, bmap, sigma = necklace_sym(q, m, seed, frac)
        if not connected(g):
            continue
        ck(c4_free(g), "rotation-symmetric necklace PG(2,%d)^%d is C4-free" % (q, m))
        # sigma is an automorphism -- by machine, not by the construction argument
        okaut = all(sigma[v] in g[sigma[u]] for (u, v) in edges_of(g))
        ck(okaut, "the block rotation IS an automorphism of PG(2,%d)^%d" % (q, m))
        st = host_stats(g, bmap)
        blocks_hit = {bmap[c] for c in st["C"]}
        ck(len(blocks_hit) == m, "(SYM-BAR): Ctr meets EVERY block of the symmetric necklace")
        ck(st["inter"] == [], "(SYM-BAR): no condition-4 vertex on a symmetric necklace")
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        rows.append((q, m, len(g), mu, l_of(g), st["r"], st["diam"], len(st["C"]),
                     len(blocks_hit), len(st["inter"]), okaut))
    print("  %-12s %5s %4s %7s %5s %6s %7s %8s %8s" %
          ("host", "n", "mu", "l", "rad", "diam", "|Ctr|", "blocks", "cond-4"))
    for (q, m, n, mu, lg, r, diam, nc, nb, ni, ok) in rows:
        print("  PG(2,%d)^%-5d %5d %4d %7.3f %5d %6d %7d %8d %8d"
              % (q, m, n, mu, lg, r, diam, nc, nb, ni))
    print("  rotation verified an automorphism by machine on all %d ; Ctr meets every block on"
          % len(rows))
    print("  all %d ; condition-4 vertices on all %d: 0.  (SYM-BAR) exhibited, not asserted."
          % (len(rows), len(rows)))


# ------------------------------------------------------------------ PART 4


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


def part4(rows, nspecs, n_built, n_disc, notc4):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE SWEEP, IN PART 2's COORDINATES")
    print("=" * 78)
    print("""
  PREDICTIONS, REGISTERED BEFORE THE RUN (rule 81: no number and no load-bearing sentence
  written before its run; these are written as predictions and are judged below whatever
  they turn out to be).

   P1  On round 42's four LIVE CASE A hosts the failure is NOT a near miss: the best defect
       min_{w not in Ctr} #{c in Ctr : d(c,w) != rad} is >= 3 on every one of them.
   P2  On those four hosts Ctr touches >= 3 distinct blocks.  (The failure is SPREAD, not
       COUNT -- which is the whole point of PART 2 and the thing E46 could not see.)
   P3  Across the whole sweep, LOCALISATION and ROUNDNESS are ANTI-correlated: hosts whose
       centre touches at most 2 blocks have diam >= rad+2.  If this holds it is a measured
       mechanism, NOT a theorem, and will be reported as such.
   P4  The new asymmetric designs DO produce localised centres (some host with Ctr touching
       exactly 1 block) -- otherwise the sweep has not even tested P3.
   P5  Whether any host is a CASE A instance: NO PREDICTION REGISTERED.  That is the open
       question and we decline to guess it.
""")
    print("  specs written: %d ; built, connected and CERTIFIED C4-FREE BY MACHINE: %d ;"
          % (nspecs, n_built))
    print("  discarded (disconnected or NOT C4-free): %d ; of those, NOT C4-free: %d %s"
          % (n_disc, len(notc4), notc4[:6]))
    print("  hosts with mu >= 2 and fully measured: %d" % len(rows))

    inclass = [r for r in rows if r[5] > 4 and r[6]["r"] >= 5]
    roundh = [r for r in inclass if r[6]["diam"] == r[6]["r"] + 1]
    print()
    print("  THE POPULATION EACH NUMBER BELOW IS ABOUT (rule 90, stated before the verdicts):")
    print("    hosts C4-free with mu >= 2                       : %d" % len(rows))
    print("    ... IN CLASS (l > 4 AND rad >= 5)                : %d" % len(inclass))
    print("    ... of those ROUND (diam = rad+1) = CASE A hosts : %d" % len(roundh))

    # ---- P4 / P3: localisation vs roundness, over the in-class population
    print()
    print("  LOCALISATION x OFFSET over the IN-CLASS population (%d hosts).  'blocks' counts"
          % len(inclass))
    print("  the distinct blocks met by Ctr (a bridge chain counts as its own block).")
    tab = {}
    for (fam, nm, g, bmap, mu, lg, st) in inclass:
        nb = len({bmap[c] for c in st["C"]})
        key = (min(nb, 4), min(st["diam"] - st["r"], 4))
        tab[key] = tab.get(key, 0) + 1
    print("    %-10s %6s %6s %6s %6s %6s" % ("blocks\\off", "+0", "+1", "+2", "+3", ">=+4"))
    for b in (1, 2, 3, 4):
        lab = "%d" % b if b < 4 else ">=4"
        print("    %-10s %6d %6d %6d %6d %6d"
              % (lab, tab.get((b, 0), 0), tab.get((b, 1), 0), tab.get((b, 2), 0),
                 tab.get((b, 3), 0), tab.get((b, 4), 0)))
    loc12 = [r for r in inclass if len({r[3][c] for c in r[6]["C"]}) <= 2]
    loc12_round = [r for r in loc12 if r[6]["diam"] == r[6]["r"] + 1]
    loc1 = [r for r in inclass if len({r[3][c] for c in r[6]["C"]}) == 1]
    print()
    print("  P4: in-class hosts whose Ctr touches exactly ONE block: %d" % len(loc1))
    print("      ... at most TWO blocks: %d" % len(loc12))
    print("  P3: of those <=2-block hosts, how many are ROUND (offset +1)? %d"
          % len(loc12_round))
    if len(loc12) == 0:
        print("      P3 IS UNTESTED: the sweep produced no localised in-class host at all,")
        print("      so this round measured NOTHING about the anti-correlation.  Stated as a")
        print("      failure of the instrument, not as evidence for the mechanism.")
    else:
        print("      population in which P3 COULD have failed: %d hosts." % len(loc12))

    # ---- |Ctr| x offset, the count coordinate, for contrast with the localisation one
    print()
    print("  For contrast, the SAME population in the COUNT coordinate (|Ctr| x offset) --")
    print("  this is the table (D9) reads, and PART 2 says it is the wrong one:")
    tab2 = {}
    for (fam, nm, g, bmap, mu, lg, st) in inclass:
        c = len(st["C"])
        b = 0 if c == 1 else (1 if c == 2 else (2 if c <= 5 else (3 if c <= 25 else 4)))
        key = (b, min(st["diam"] - st["r"], 4))
        tab2[key] = tab2.get(key, 0) + 1
    print("    %-10s %6s %6s %6s %6s %6s" % ("|Ctr|\\off", "+0", "+1", "+2", "+3", ">=+4"))
    for b, lab in ((0, "1"), (1, "2"), (2, "3-5"), (3, "6-25"), (4, ">=26")):
        print("    %-10s %6d %6d %6d %6d %6d"
              % (lab, tab2.get((b, 0), 0), tab2.get((b, 1), 0), tab2.get((b, 2), 0),
                 tab2.get((b, 3), 0), tab2.get((b, 4), 0)))

    # ---- THE DECISIVE TEST on every in-class ROUND host
    print()
    print("  THE DECISIVE TEST (CA-EQ) ON EVERY IN-CLASS ROUND HOST -- %d of them." %
          len(roundh))
    print("  %-18s %5s %7s %5s %6s %7s %7s %8s %7s" %
          ("host", "n", "l", "rad", "diam", "|Ctr|", "blocks", "spread", "defect"))
    found = []
    for (fam, nm, g, bmap, mu, lg, st) in roundh:
        nb = len({bmap[c] for c in st["C"]})
        print("  %-18s %5d %7.3f %5d %6d %7d %7d %8d %7s"
              % (nm, st["n"], lg, st["r"], st["diam"], len(st["C"]), nb, st["spread"],
                 ("INSTANCE" if st["inter"] else str(st["best_def"]))))
        if st["inter"]:
            found.append((fam, nm, g, bmap, mu, lg, st))
    print()
    if found:
        print("  *** CASE A INSTANCES FOUND: %d hosts. ***" % len(found))
    else:
        print("  CASE A INSTANCES FOUND: 0.")
        print("  THE NUMBER WE ARE ENTITLED TO (rule 90/104): the in-class ROUND hosts on")
        print("  which (CS-1') does not already decide the answer are the only ones on which")
        print("  a search could have failed.  Everything else is arithmetic, not evidence.")
    dec = live = 0
    live_rows = []
    for (fam, nm, g, bmap, mu, lg, st) in roundh:
        n = st["n"]
        D, ecc, r = st["D"], st["ecc"], st["r"]
        best = 0
        for w in range(n):
            if ecc[w] == r:
                continue
            sz = sum(1 for v in range(n) if D[w][v] == r)
            best = max(best, sz)
        if len(st["C"]) > best:
            dec += 1
        else:
            live += 1
            live_rows.append((nm, st, bmap, lg, mu))
    print("    in-class CASE A hosts                                      : %d" % len(roundh))
    print("    ... DECIDED EMPTY BY (CS-1') alone (|Ctr| > max_w |S_r(w)|) : %d" % dec)
    print("    ... LIVE (counting does not decide; the search tested them) : %d" % live)
    contentful_v = sum(st["n"] for (nm, st, bmap, lg, mu) in live_rows)
    contentful_nc = sum(st["n"] - len(st["C"]) for (nm, st, bmap, lg, mu) in live_rows)
    print("    THE CONTENTFUL CASE A POPULATION: %d hosts / %d vertices / %d non-central"
          % (live, contentful_v, contentful_nc))
    print("    ... of which satisfy condition 4: %d." % len(found))

    # ---- P1 / P2: the localisation diagnostic E46 section 5.1 asked for
    print()
    print("  THE DIAGNOSTIC E46 SECTION 5.1 ASKED FOR, RUN IN PART 2's COORDINATES.")
    print("  For each LIVE round host: the best w, how many centres it misses, and WHERE the")
    print("  centres sit relative to it (distance profile of Ctr from that w).")
    p1_ok = p2_ok = 0
    for (nm, st, bmap, lg, mu) in live_rows:
        n, D, ecc, r, C = st["n"], st["D"], st["ecc"], st["r"], st["C"]
        bw, bd = None, None
        for w in range(n):
            if ecc[w] == r:
                continue
            dd = defect(D, C, r, w)
            if bd is None or dd < bd:
                bw, bd = w, dd
        prof = {}
        for c in C:
            prof[D[c][bw]] = prof.get(D[c][bw], 0) + 1
        nb = len({bmap[c] for c in C})
        print("    %-18s n=%3d rad=%d |Ctr|=%2d blocks=%d  best w=%3d misses %2d of %2d"
              % (nm, n, r, len(C), nb, bw, bd, len(C)))
        print("        distances of the centres from that w: %s   (condition 4 wants ALL = %d)"
              % (", ".join("%d:%d" % (k, prof[k]) for k in sorted(prof)), r))
        if bd >= 3:
            p1_ok += 1
        if nb >= 3:
            p2_ok += 1
    print()
    print("  P1 (best defect >= 3 on every live round host): %d of %d live hosts"
          % (p1_ok, len(live_rows)))
    print("  P2 (Ctr touches >= 3 blocks on every live round host): %d of %d"
          % (p2_ok, len(live_rows)))
    return found


# ------------------------------------------------------------------ PART 5


def part5():
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- OFF THE CYCLE: is it condition 5 that is doing the work?")
    print("=" * 78)
    print("""
  PART 4 measured a mechanism: on a CYCLE of blocks the centre is spread and roundness only
  ever occurs with a spread centre.  A cycle is the only topology this line has ever used at
  rad >= 5.  Two questions follow, and only one of them is about density:

    Q-A  Are conditions 1,2,3,4 (C4-free, mu >= 2, rad >= 5, diam = rad+1, a vertex maximally
         far from every centre) satisfiable AT ALL above rad = 2?  Every instance this line
         holds above rad 2 is CASE B; every CASE A instance it holds is at rad = 2.  If the
         answer is yes with l <= 4, then any emptiness proof for brief E46's class MUST use
         condition 5, and we would know that before spending another engine round on it.
    Q-B  How large can l be on such an object?  That is the frontier, and 4 is the number
         the brief asks us to cross.

  PROBE.  (i) THETA graphs: k >= 3 internally disjoint paths between two branch vertices --
  the smallest topology that is not a cycle, l about 2.  (ii) BLOCK GRAPHS on non-cycle
  topologies (theta of blocks, K4 of blocks, cycle-plus-chord), which interpolate: as the
  connecting paths shorten and the blocks dominate, l climbs from 2 towards 5.

  PREDICTIONS, REGISTERED BEFORE THIS PROBE RAN:
    P6  Conditions 1,2,3,4 ARE satisfiable above rad = 2 on a non-cycle topology -- some
        theta graph will carry them.  (If false, the obstruction is not about density at all
        and this line has been looking at the wrong condition for two rounds.)
    P7  The maximum l over every instance this probe finds will be < 4, i.e. the probe will
        NOT settle brief E46's class.  It will locate the frontier, not cross it.
    P8  (added before the second table below ran, after P6 came back NEGATIVE.)  Conditions
        1,3,4 ARE satisfiable at rad = 2 -- round 42 found 414 such vertices -- so the
        barrenness at rad >= 5 is a THRESHOLD in rad, not a blanket impossibility.  The
        table below reports, for every rad, how many ROUND hosts this probe built and how
        many of them carry condition 4.  PREDICTION: the largest rad carrying condition 4
        in this probe is 2 or 3.  If instead carriers appear at every rad up to some large
        value, the whole diagnosis of PART 4 is wrong and this line should say so.
""")
    hosts = []
    for a in range(2, 13):
        for b in range(a, 15):
            for c in range(b, 22):
                if a + b < 5:
                    continue
                hosts.append((theta([a, b, c]), None, "TH(%d,%d,%d)" % (a, b, c), "THETA"))
    for a in range(2, 9):
        for b in range(a, 11):
            for c in range(b, 13):
                for d in range(c, 15):
                    if a + b < 5:
                        continue
                    hosts.append((theta([a, b, c, d]), None,
                                  "TH4(%d,%d,%d,%d)" % (a, b, c, d), "THETA"))
    print("  theta hosts written: %d" % len(hosts))
    nb = len(hosts)
    # ---- block graphs on NON-CYCLE topologies
    for q in (2, 3):
        for s1 in (1, 2, 3, 4, 5, 6):
            for s2 in (1, 2, 3, 4, 5, 6, 7, 8):
                for k in (1, 2, 3):
                    if s2 < s1:
                        continue
                    J = [(0, 1, k, s1), (0, 1, k, s2), (0, 1, k, s1 + s2)]
                    hosts.append((None, ([q, q], J, 7 * (s1 * 31 + s2 * 7 + k), "any"),
                                  "THB%d(%d,%d,%d)" % (q, s1, s2, k), "BLOCK"))
    for q in (2, 3):
        for s in (1, 2, 3, 4, 5):
            for k in (1, 2, 3):
                J = [(0, 1, k, s), (1, 2, k, s), (2, 3, k, s), (3, 0, k, s),
                     (0, 2, k, s + 1), (1, 3, k, s + 2)]
                hosts.append((None, ([q] * 4, J, 11 * (s * 17 + k), "any"),
                              "K4B%d(%d,%d)" % (q, s, k), "BLOCK"))
    for q in (2, 3):
        for m in (5, 6, 7):
            for s in (0, 1, 2, 3):
                for ch in (2, 3):
                    J = [(i, (i + 1) % m, 3, s) for i in range(m)]
                    J.append((0, ch, 3, s + 1))
                    hosts.append((None, ([q] * m, J, 13 * (m * 23 + s * 5 + ch), "any"),
                                  "CCB%d(%d,%d,%d)" % (q, m, s, ch), "BLOCK"))
    print("  block-graph hosts on NON-CYCLE topologies written: %d" % (len(hosts) - nb))
    nb2 = len(hosts)
    # ---- THE POSITIVE CONTROL, without which a 0 in the table below means nothing.
    # Round 42's own greedy random C4-free family is where its 414 condition-4 vertices at
    # rad = 2 live.  If the instrument cannot find condition 4 THERE, its 0 elsewhere is a
    # statement about the instrument.  Lengthened copies (a cycle glued through one vertex)
    # carry the SAME family up through the radii.
    for sd in range(1, 90):
        for n0 in (12, 16, 20, 24):
            h = rand_c4free_dense(sd * 7919 + n0, n0)
            if h is None:
                continue
            hosts.append((h, None, "RC(%d,%d)" % (sd, n0), "CTRL"))
            for k in (5, 7, 9, 11, 13):
                hosts.append((glue_cycle(h, 0, k), None, "RCg(%d,%d,%d)" % (sd, n0, k),
                              "CTRLg"))
    print("  POSITIVE-CONTROL hosts (round 42's rad-2 family, plus lengthened copies): %d"
          % (len(hosts) - nb2))

    inst = []
    n_ok = n_bad = 0
    seen = 0
    t_round = {}
    t_carry = {}
    t_live = {}
    fr = {}
    fc = {}
    carriers = []
    for (g, spec, nm, fam) in hosts:
        if over():
            break
        if g is None:
            qs, J, sd, md = spec
            g, _bm = blockgraph(qs, J, sd, md)
        if not connected(g):
            n_bad += 1
            continue
        if not c4_free(g):
            n_bad += 1
            continue
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        if mu < 2:
            n_bad += 1
            continue
        n_ok += 1
        D, ecc, r = profile(g)
        diam = max(ecc)
        if diam != r + 1:
            continue
        t_round[r] = t_round.get(r, 0) + 1
        fr[(fam, r)] = fr.get((fam, r), 0) + 1
        best = 0
        for wv in range(len(g)):
            if ecc[wv] == r:
                continue
            sz = sum(1 for v in range(len(g)) if D[wv][v] == r)
            if sz > best:
                best = sz
        if len(centre_of(ecc, r)) <= best:
            t_live[r] = t_live.get(r, 0) + 1
        it = far_intersection(D, ecc, r)
        if it:
            t_carry[r] = t_carry.get(r, 0) + 1
            fc[(fam, r)] = fc.get((fam, r), 0) + 1
            carriers.append((r, nm, g, diam, len(centre_of(ecc, r)), it[0], mu, l_of(g)))
        if r < 5:
            continue
        seen += 1
        if it:
            lg = l_of(g)
            C = centre_of(ecc, r)
            inst.append((lg, nm, g, r, diam, len(C), it[0], mu))
    print()
    print("  THE POPULATION (rule 90): probe hosts C4-free with mu >= 2 and connected: %d ;"
          % n_ok)
    print("  ... of those satisfying conditions 2 AND 3 (rad >= 5 AND diam = rad+1): %d --"
          % seen)
    print("  that is the ONLY sub-population in which condition 4 could have been found.")
    inst.sort()
    print("  ... of those, carrying condition 4 as well (INSTANCES of conditions 1-4): %d"
          % len(inst))
    if inst:
        print()
        print("  *** CONDITIONS 1,2,3,4 ARE SATISFIABLE ABOVE rad = 2.  P6 HOLDS. ***")
        print("  %-18s %5s %8s %5s %6s %7s %5s %5s" %
              ("instance", "n", "l", "rad", "diam", "|Ctr|", "w", "mu"))
        for (lg, nm, g, r, diam, nc, w, mu) in inst[-6:]:
            print("  %-18s %5d %8.4f %5d %6d %7d %5d %5d"
                  % (nm, len(g), lg, r, diam, nc, w, mu))
        best = inst[-1]
        print()
        print("  MAXIMUM l OVER EVERY INSTANCE THIS PROBE FOUND: %.4f  (host %s)"
              % (best[0], best[1]))
        print("  Condition 5 asks for l > 4.  Gap to the frontier: %.4f" % (4.0 - best[0]))
        print("  SMALLEST instance, written out for independent re-verification:")
        sm = min(inst, key=lambda x: len(x[2]))
        (lg, nm, g, r, diam, nc, w, mu) = sm
        D, ecc, rr = profile(g)
        print("    %s  n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d Ctr=%s w=%d"
              % (nm, len(g), len(edges_of(g)), mu, lg, r, diam,
                 sorted(centre_of(ecc, rr)), w))
        print("    EDGES = %s" % (sorted(edges_of(g)),))
        ck(all(D[c][w] == r for c in centre_of(ecc, rr)), "the printed instance IS one")
        ck(c4_free(g) and diam == r + 1 and r >= 5, "the printed instance meets 1,2,3")
    else:
        print("  *** NO INSTANCE.  P6 FAILS -- and that is the more interesting outcome:")
        print("  it says the obstruction survives without condition 5 on every topology")
        print("  probed here, which is a statement about ROUNDNESS, not about density. ***")

    # ---- P8: the rad threshold, over EVERY round host this probe built
    print()
    print("  P8 -- THE rad TABLE OVER EVERY ROUND HOST OF THIS PROBE (no rad filter).")
    print("  Each row is a population in which condition 4 COULD have been found and was")
    print("  looked for; the right column is the only evidence the row carries.")
    print("  The LIVE column applies (CS-1') host by host FIRST: a round host with")
    print("  |Ctr| > max_w |S_rad(w)| is proved barren by counting and is NOT evidence.")
    print("  Only the LIVE column is a population in which the search could have failed.")
    fams = ["THETA", "BLOCK", "CTRL", "CTRLg"]
    print("    %5s %8s %8s %8s   %s" % ("rad", "ROUND", "LIVE", "carry",
                                        " ".join("%s r/c" % f for f in fams)))
    rmax = None
    for r in sorted(t_round):
        cells = " ".join("%d/%d" % (fr.get((f, r), 0), fc.get((f, r), 0)) for f in fams)
        print("    %5d %8d %8d %8d   %s"
              % (r, t_round[r], t_live.get(r, 0), t_carry.get(r, 0), cells))
        if t_carry.get(r, 0):
            rmax = r
    print("    %5s %8d %8d %8d" % ("all", sum(t_round.values()), sum(t_live.values()),
                                   sum(t_carry.values())))
    live3 = sum(v for k, v in t_live.items() if k >= 3)
    car3 = sum(v for k, v in t_carry.items() if k >= 3)
    print("    THE NUMBER THIS PROBE IS ENTITLED TO: at rad >= 3 it built %d LIVE round"
          % live3)
    print("    hosts -- hosts on which counting does NOT already decide the answer -- and")
    print("    found %d condition-4 vertices on them." % car3)
    ctrl_car = sum(v for (f, r), v in fc.items() if f.startswith("CTRL"))
    ctrl_rnd = sum(v for (f, r), v in fr.items() if f.startswith("CTRL"))
    print("    POSITIVE CONTROL: %d round hosts, %d of them carry condition 4."
          % (ctrl_rnd, ctrl_car))
    ck(ctrl_car > 0, "THE PROBE MUST HAVE A POSITIVE CONTROL or its zeros mean nothing")
    if ctrl_car == 0:
        print("    THE CONTROL IS DEAD: every zero in this table is a statement about the")
        print("    instrument and NOT about the mathematics.  Reported as such.")
    if rmax is None:
        print("  NO round host of this probe carries condition 4 AT ANY rad -- including")
        print("  rad = 2, where round 42 has 414 instances on OTHER families.  So this probe")
        print("  says nothing about a threshold; it says these two topologies are barren.")
        print("  P8 IS NOT CONFIRMED BY THIS PROBE, and the honest reading is that the probe")
        print("  never contained a positive control.  Recorded as an instrument failure.")
    else:
        print("  LARGEST rad carrying condition 4 in this probe: %d   (P8 predicted 2 or 3)"
              % rmax)
        ex = [c for c in carriers if c[0] == rmax][0]
        (r, nm, g, diam, nc, w, mu, lg) = ex
        print("  witness at that rad: %s  n=%d |E|=%d mu=%d l=%.4f rad=%d diam=%d |Ctr|=%d w=%d"
              % (nm, len(g), len(edges_of(g)), mu, lg, r, diam, nc, w))
        print("    EDGES = %s" % (sorted(edges_of(g)),))
        D2, e2, r2 = profile(g)
        ck(all(D2[c][w] == r2 for c in centre_of(e2, r2)), "printed rad-%d witness IS one" % r)
    return inst


# ------------------------------------------------------------------ PART 6


def rand_graph(seed, n, num):
    st = seed % (1 << 31)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    out = []
    for i in range(len(pairs) - 1, 0, -1):
        st = (st * 1103515245 + 12345) % (1 << 31)
        j = st % (i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    return adj(n, pairs[:num])


def rand_c4free_sparse(seed, n, cap):
    """random C4-free graph with a DEGREE CAP -- sparse, so it can be long.  The dense greedy
    of round 42 always lands at rad 2; capping the degree is what lets rad grow."""
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
    if not connected(h):
        return None
    return h


def part6():
    PARTS_RUN.append("PART6")
    print()
    print("=" * 78)
    print("PART 6 -- WHERE DOES THE OBSTRUCTION LIVE: roundness, or C4-freeness?")
    print("=" * 78)
    print("""
  PART 5 found conditions 3+4 together at rad = 2 (166 of 207 live control hosts) and NEVER
  above it.  Two very different explanations fit that, and they point at different next
  rounds:
     (E1) roundness plus 'maximally far from every centre' is impossible above rad = 2 for
          ANY graph -- a statement with no C4 or mu in it at all;
     (E2) it is possible in general and the obstruction is C4-freeness / mu >= 2 / density.
  This part separates them by dropping the class hypotheses.

  PREDICTIONS, REGISTERED BEFORE THIS PROBE RAN:
    P9   Random GENERAL graphs (no C4-freeness, no mu) WILL produce round hosts at rad >= 3
         carrying condition 4, i.e. (E2).  If they do not, the target of this whole front
         changes: the thing to prove would be a statement about round graphs in general.
    P10  Sparse C4-free hosts with a degree cap (l about 3, so condition 5 FAILS): NO
         PREDICTION REGISTERED.  This is the sub-question the round cannot guess.
""")
    fams = []
    for sd in range(1, 260):
        for n in (8, 10, 12, 14, 16):
            for dens in (0.18, 0.25, 0.33):
                num = max(n, int(round(dens * n * (n - 1) / 2)))
                fams.append(("GEN", rand_graph(sd * 7717 + n * 13 + int(dens * 100), n, num),
                             "G(%d,%d,%.2f)" % (sd, n, dens)))
    for sd in range(1, 260):
        for n in (14, 18, 22, 26, 30, 36, 44):
            for cap in (3, 4, 5):
                h = rand_c4free_sparse(sd * 6329 + n * 17 + cap, n, cap)
                if h is not None:
                    fams.append(("SPC", h, "S(%d,%d,%d)" % (sd, n, cap)))
    print("  hosts written: GEN %d ; SPC %d"
          % (sum(1 for f in fams if f[0] == "GEN"), sum(1 for f in fams if f[0] == "SPC")))
    tab = {}
    hits = []
    for (fam, g, nm) in fams:
        if over():
            break
        if g is None or not connected(g):
            continue
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        if fam == "SPC" and (mu < 2 or not c4_free(g)):
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        if diam != r + 1:
            continue
        it = far_intersection(D, ecc, r)
        key = (fam, r)
        a, b = tab.get(key, (0, 0))
        tab[key] = (a + 1, b + (1 if it else 0))
        if it and r >= 3:
            hits.append((fam, nm, g, r, diam, len(centre_of(ecc, r)), it[0], mu, l_of(g)))
    print()
    print("    %5s %10s %10s %10s %10s" % ("rad", "GEN round", "GEN carry", "SPC round",
                                           "SPC carry"))
    for r in sorted({k[1] for k in tab}):
        ga, gb = tab.get(("GEN", r), (0, 0))
        sa, sb = tab.get(("SPC", r), (0, 0))
        print("    %5d %10d %10d %10d %10d" % (r, ga, gb, sa, sb))
    g3 = sum(b for (f, r), (a, b) in tab.items() if f == "GEN" and r >= 3)
    s3 = sum(b for (f, r), (a, b) in tab.items() if f == "SPC" and r >= 3)
    g2 = sum(b for (f, r), (a, b) in tab.items() if f == "GEN" and r == 2)
    s2 = sum(b for (f, r), (a, b) in tab.items() if f == "SPC" and r == 2)
    print()
    print("  POSITIVE CONTROLS (rad = 2): GEN %d carriers, SPC %d carriers." % (g2, s2))
    ck(g2 + s2 > 0, "PART 6 needs its own positive control at rad = 2")
    print("  AT rad >= 3: GEN carriers %d ; SPC carriers %d" % (g3, s3))
    if g3:
        print("  *** P9 HOLDS: dropping C4-freeness and mu PRODUCES the configuration above")
        print("  rad 2.  So (E2): roundness alone does NOT forbid it, and any emptiness proof")
        print("  for brief E46's class MUST use C4-freeness or mu >= 2. ***")
        h = sorted(hits, key=lambda x: (-x[3], len(x[2])))[0]
        (fam, nm, g, r, diam, nc, w, mu, lg) = h
        print("  LARGEST-rad witness: %s  n=%d |E|=%d mu=%d l=%.4f rad=%d diam=%d |Ctr|=%d w=%d"
              % (nm, len(g), len(edges_of(g)), mu, lg, r, diam, nc, w))
        print("    EDGES = %s" % (sorted(edges_of(g)),))
        D2, e2, r2 = profile(g)
        ck(all(D2[c][w] == r2 for c in centre_of(e2, r2)) and max(e2) == r2 + 1,
           "the printed PART 6 witness IS round and IS a condition-4 pair")
    else:
        gr3 = sum(a for (f, r), (a, b) in tab.items() if f == "GEN" and r >= 3)
        print("  *** P9 FAILS AS PREDICTED-EVENT, AND ITS FAILURE IS AN ARTEFACT OF THE")
        print("  SAMPLER, NOT EVIDENCE FOR (E1).  The GEN sampler produced %d round hosts at"
              % gr3)
        print("  rad >= 3 at all -- dense random graphs are short, so the population that")
        print("  could have carried it is thin and skewed to rad exactly 3.  The question")
        print("  (E1) vs (E2) is NOT settled by the GEN column; it is settled by the SPC")
        print("  column of the same table, which is read next. ***")
    if s3:
        print("  *** AND IT SURVIVES C4-FREENESS + mu >= 2 AT l <= 4: %d carriers." % s3)
        h = sorted([x for x in hits if x[0] == "SPC"], key=lambda x: (-x[3], len(x[2])))[0]
        (fam, nm, g, r, diam, nc, w, mu, lg) = h
        print("  LARGEST-rad C4-free witness: %s n=%d |E|=%d mu=%d l=%.4f rad=%d diam=%d "
              "|Ctr|=%d w=%d" % (nm, len(g), len(edges_of(g)), mu, lg, r, diam, nc, w))
        print("    EDGES = %s" % (sorted(edges_of(g)),))
        D2, e2, r2 = profile(g)
        ck(all(D2[c][w] == r2 for c in centre_of(e2, r2)) and max(e2) == r2 + 1
           and c4_free(g) and mu >= 2, "the printed SPC witness IS one, C4-free, mu >= 2")
        print("  THIS IS THE FIRST OBJECT ON THIS LINE MEETING CONDITIONS 1,3,4 ABOVE rad 2.")
        print("  It fails condition 5 (l = %.4f <= 4) and condition 2 if rad < 5 -- say so."
              % lg)
    else:
        print("  C4-free + mu >= 2 at rad >= 3: 0 carriers in this probe.")
    if s3:
        print("  (E1) IS REFUTED: roundness plus 'maximally far from every centre' at rad >= 3")
        print("  is NOT impossible -- it happens %d times here, under C4-freeness and mu >= 2."
              % s3)
        print("  Any emptiness proof for brief E46's class must therefore use condition 5,")
        print("  and PART 7 asks how far condition 5 can be pushed.")
    return hits


# ------------------------------------------------------------------ PART 7


def part7():
    PARTS_RUN.append("PART7")
    print()
    print("=" * 78)
    print("PART 7 -- THE l-FRONTIER: how dense can conditions 1,2,3,4 be made?")
    print("=" * 78)
    print("""
  PART 6 produced an object meeting conditions 1,2,3,4 at rad = 5 with l about 3.  Only
  condition 5 (l > 4) is missing, and the sampler that produced it had its DEGREE CAPPED AT
  3, which caps l at 3.  Raising the cap raises l and shortens the graph; keeping rad >= 5
  then needs many more vertices.  This part sweeps that trade-off directly.

  PREDICTIONS, REGISTERED BEFORE THIS PROBE RAN:
    P11  The sweep WILL produce hosts in class (C4-free, mu >= 2, l > 4, rad >= 5) that are
         also ROUND -- i.e. CASE A hosts from a family that is not a necklace.
    P12  Whether any of them carries condition 4: NO PREDICTION.  That is brief E46's
         question and this round will not guess it.
""")
    rows = []
    allc = []
    best = None
    inclass = 0
    live = 0
    carriers = 0
    for cap in (4, 5, 6):
        for n in (120, 200, 300, 420, 560):
            for sd in (1, 2, 3):
                if over():
                    break
                g = rand_c4free_sparse(sd * 104729 + n * 31 + cap, n, cap)
                if g is None or not connected(g):
                    continue
                if not c4_free(g):
                    continue
                mu = min(a_val_matching(g, v) for v in range(len(g)))
                if mu < 2:
                    continue
                D, ecc, r = profile(g)
                diam = max(ecc)
                lg = l_of(g)
                C = centre_of(ecc, r)
                it = far_intersection(D, ecc, r)
                rows.append((cap, n, sd, len(g), lg, mu, r, diam, len(C), len(it)))
                if lg > 4 and r >= 5:
                    inclass += 1
                    if diam == r + 1:
                        bst = 0
                        for wv in range(len(g)):
                            if ecc[wv] == r:
                                continue
                            sz = sum(1 for v in range(len(g)) if D[wv][v] == r)
                            if sz > bst:
                                bst = sz
                        if len(C) <= bst:
                            live += 1
                        if it:
                            carriers += 1
                            allc.append((lg, "SP(%d,%d,%d)" % (cap, n, sd), g, r, diam,
                                         len(C), it[0], mu, len(it)))
                            if best is None or lg > best[0]:
                                best = (lg, "SP(%d,%d,%d)" % (cap, n, sd), g, r, diam,
                                        len(C), it[0], mu)
    print("  %5s %6s %4s %6s %8s %4s %5s %6s %7s %7s" %
          ("cap", "n_ask", "sd", "n", "l", "mu", "rad", "diam", "|Ctr|", "cond4"))
    for (cap, n, sd, nn, lg, mu, r, diam, nc, ni) in rows:
        print("  %5d %6d %4d %6d %8.4f %4d %5d %6d %7d %7d"
              % (cap, n, sd, nn, lg, mu, r, diam, nc, ni))
    print()
    print("  THE POPULATION (rule 90): hosts built, C4-free, mu >= 2: %d" % len(rows))
    print("  ... IN CLASS (l > 4 AND rad >= 5): %d ; of those ROUND and LIVE under (CS-1'): %d"
          % (inclass, live))
    print("  ... carrying condition 4 (INSTANCES OF BRIEF E46's CLASS 1-5): %d" % carriers)
    if best:
        (lg, nm, g, r, diam, nc, w, mu) = best
        print()
        print("  *** BRIEF E46's CLASS IS NON-EMPTY. ***")
        print("  %s n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d |Ctr|=%d w=%d"
              % (nm, len(g), len(edges_of(g)), mu, lg, r, diam, nc, w))
        D2, e2, r2 = profile(g)
        ck(c4_free(g) and mu >= 2, "witness: condition 1")
        ck(r2 >= 5, "witness: condition 2")
        ck(max(e2) == r2 + 1, "witness: condition 3")
        ck(all(D2[c][w] == r2 for c in centre_of(e2, r2)), "witness: condition 4")
        ck(l_of(g) > 4, "witness: condition 5")
        for tag, c in zip(("W43a", "W43b"), sorted(allc, key=lambda x: -x[8])):
            (lg2, nm2, g2, r2b, dm2, nc2, w2, mu2, ni2) = c
            print("  %-5s %-14s n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d |Ctr|=%d "
                  "condition-4 vertices=%d  (w=%d)"
                  % (tag, nm2, len(g2), len(edges_of(g2)), mu2, lg2, r2b, dm2, nc2, ni2, w2))
            with open("problems/wowii/w133_r43_%s.txt" % tag, "w") as fh:
                fh.write("# %s = %s  n=%d rad=%d diam=%d |Ctr|=%d l=%.6f\n"
                         % (tag, nm2, len(g2), r2b, dm2, nc2, lg2))
                fh.write("%d\n" % len(g2))
                for (u, v) in sorted(edges_of(g2)):
                    fh.write("%d %d\n" % (u, v))
        print("  edge lists written to problems/wowii/w133_r43_W43a.txt and _W43b.txt for")
        print("  INDEPENDENT re-verification by a script sharing no code with this one")
        print("  (rule 105).  NOTHING BELOW OR ABOVE CERTIFIES THEM; that script does.")
    else:
        print("  NO instance of brief E46's class in this sweep.  What the sweep DID reach")
        print("  is printed above; the entitled number is the LIVE count, not the built one.")
    return best


# ------------------------------------------------------------------ main


def main():
    print("WOWII-133 round 43 -- E46 HARVESTED AND AUDITED; CASE A RE-COORDINATED")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    part0()
    print()
    print("  building and measuring the PART 4 sweep (quiet pass) ...", flush=True)
    rows, cond4_pairs, nspecs, n_built, n_disc, notc4 = build_sweep()
    print("  ... done, %.1fs" % (time.time() - T0), flush=True)
    part1(cond4_pairs[:40])
    part2([(nm, g, st) for (fam, nm, g, bmap, mu, lg, st) in rows])
    part3()
    found = part4(rows, nspecs, n_built, n_disc, notc4)
    part5()
    part6()
    part7()

    if found:
        print()
        print("=" * 78)
        print("PART 5 -- THE INSTANCE(S), WRITTEN OUT FOR INDEPENDENT RE-VERIFICATION")
        print("=" * 78)
        for (fam, nm, g, bmap, mu, lg, st) in found[:2]:
            print("  HOST %s  n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d |Ctr|=%d w=%s"
                  % (nm, len(g), len(edges_of(g)), mu, lg, st["r"], st["diam"],
                     len(st["C"]), st["inter"][:5]))
            print("  Ctr = %s" % sorted(st["C"]))
            print("  EDGES = %s" % (sorted(edges_of(g)),))

    print()
    print("=" * 78)
    print("PARTS RUN: %s" % ",".join(PARTS_RUN))
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
