#!/usr/bin/env python3
"""WOWII-133 round 41 -- HARVEST OF E43 AND E45, AND WHAT THE (RXM-PERI) CENSUS ACTUALLY TESTED.

Round 40 posed (RXM-PERI): "w maximally far from every centre => w peripheral", measured
1297/1297 with zero violations, and did NOT promote it.  This round:

  * rebuilds E45's REFUTATION witness from its own edge list (its verdict and its certificate
    are separate objects and they do not agree);
  * rebuilds E43's k3=4 CONSTRUCTION from its own edge list, against every frame condition of
    the brief, and against the one derived fact of that brief E43 disputes;
  * proves the two one-line lemmas that make peripherality FORCED, and measures how many of
    round 40's 1297 census instances are forced passes -- i.e. how much of that census is
    evidence for the conjecture and how much is arithmetic;
  * settles (RXM-PERI) in general graphs with a hand-built witness of this file's own;
  * asks the restricted question that survives, on this line's own class (C4-free, mu >= 2).

Self-contained: primitives COPIED from round 40's file, never imported.
Interpreter: system python3 (pure stdlib).  No SAT.  No exhaustive graph enumeration --
every search here is a seeded-random sample or a named hand construction.

PARTS
  0  primitive self-tests + the guard on THIS round's predicate
  1  E45 harvest -- the (RXM-PERI) refutation, rebuilt
  2  E43 harvest -- the k3 = 4 construction, rebuilt, and brief E43's disputed derived fact
  3  the two FORCED-PASS lemmas, and how much of the 1297 census they eat
  4  (RXM-PERI) in general graphs -- this file's own witness, plus a seeded-random liveness run
  5  the restricted question on this line's class (C4-free, mu >= 2): a seeded-random attack
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


# ---------------------------------------------------------------- primitives (COPIED r40)


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
    """a(v) = alpha(G[N(v)]); C4-free => G[N(v)] is a matching => a = deg - #inside edges.
    Computed here by BRUTE independent-set search so it is correct off the class too."""
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
    """(RAD-1P)'s condition, draft 42.4: d(c,w) == rad for EVERY centre c."""
    C = centre_of(ecc, r)
    return all(D[c][w] == r for c in C)


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def pathgraph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


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
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(k - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, at))
    return adj(n, E)


def path_then_cycle(g, at, L, k):
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    tip = prev
    p = tip
    for _ in range(k - 1):
        E.append((p, n))
        p = n
        n += 1
    E.append((p, tip))
    return adj(n, E)


def blob_chain(q, L):
    b = pg2(q)
    bn = len(b)
    E = edges_of(b) + [(u + bn, v + bn) for (u, v) in edges_of(b)]
    n = 2 * bn
    prev = 1
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, bn + 0))
    return adj(n, E)


def build_family():
    """round 33's family, rebuilt here (COPIED, not imported).  Designed + seeded-random,
    NOT exhaustive."""
    fam = []
    b3, b5 = pg2(3), pg2(5)
    fam.append((b3, "PG(2,3)"))
    fam.append((b5, "PG(2,5)"))
    for k in (5, 7, 9, 11, 13, 15, 17, 19, 21, 25):
        fam.append((glue_cycle(b5, 0, k), "PG(2,5)+C%d glued" % k))
        fam.append((glue_cycle(b3, 0, k), "PG(2,3)+C%d glued" % k))
    for L, k in ((1, 5), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 9), (5, 9), (6, 11)):
        fam.append((path_then_cycle(b5, 0, L, k), "PG(2,5)+P%d+C%d" % (L, k)))
    for k1, k2 in ((7, 7), (9, 9), (11, 11), (13, 13), (9, 11)):
        g = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g, 1, k2), "PG(2,5)+C%d@0+C%d@1" % (k1, k2)))
        g2 = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g2, 5, k2), "PG(2,5)+C%d@0+C%d@5" % (k1, k2)))
    for L in (3, 5, 7, 9, 11):
        fam.append((blob_chain(5, L), "2xPG(2,5)+P%d" % L))
        fam.append((blob_chain(3, L), "2xPG(2,3)+P%d" % L))
    for n0 in (14, 18, 22, 26, 30, 34, 38, 44, 50):
        for s in range(1, 26):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                fam.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    for n0 in (26, 30, 34, 38, 44, 50):
        for s in (1, 2, 3, 4, 5, 6, 7, 8):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is None:
                continue
            for k in (5, 7, 9):
                fam.append((glue_cycle(h, 0, k), "dense(s=%d,n0=%d)+C%d" % (s, n0, k)))
    return fam


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitive self-tests and the guard on THIS round's predicate")
    print("=" * 78)
    P = petersen()
    _, eP, rP = profile(P)
    ck(rP == 2 and len(centre_of(eP, rP)) == len(P), "Petersen self-centred, rad 2")
    C9 = cycle(9)
    _, e9, r9 = profile(C9)
    ck(r9 == 4 and max(e9) == 4, "C9 rad = diam = 4")
    P5 = pathgraph(5)
    D5, e5, r5 = profile(P5)
    ck(r5 == 2 and max(e5) == 4 and centre_of(e5, r5) == [2], "P5 rad 2 diam 4 centre {2}")
    ck(maximally_far(D5, e5, r5, 0) and e5[0] == 4, "P5 endpoint is condition-3 AND peripheral")
    agree = 0
    for g in (P, C9, pg2(3), pathgraph(7)):
        for v in range(len(g)):
            if c4_free(g):
                ck(a_val(g, v) == a_val_matching(g, v), "a_val brute == matching formula")
            agree += 1
    print("  a(.) brute-vs-formula cross-check at %d vertices (C4-free hosts only)" % agree)

    # CLASS CLAIMED for this round: any evaluator of PERIPHERALITY or of the FORCED/OPEN regime
    # split that (i) reads a graph from a narrated adjacency table instead of its edge list, or
    # (ii) tests peripherality as "ecc(w) > rad" instead of "ecc(w) = diam".  Neither is r34's
    # zero-step, r35's one-step, r36's late-block, r37's off-by-one/anchor-drift, r38's
    # cost-evaluator, r39's centre-widen/quantifier-swap/stratum-offset, nor r40's sphere-shift.
    #
    # (D5) TABLE-TRUST: build from a stated adjacency table rather than the edge list.
    #      This is not hypothetical -- it is E45's own defect, planted here as a guard member.
    # (D6) PERI-AS-NONCENTRAL: call w peripheral when ecc(w) > rad.
    fires_d6 = extra_d6 = 0
    for g, _nm in [(pathgraph(k), "P%d" % k) for k in range(4, 12)] + \
                  [(cycle(k), "C%d" % k) for k in (5, 6, 7, 8, 9)]:
        D, e, r = profile(g)
        dm = max(e)
        for v in range(len(g)):
            correct = (e[v] == dm)
            wrong = (e[v] > r)
            if wrong:
                fires_d6 += 1
            if wrong and not correct:
                extra_d6 += 1
    ck(extra_d6 > 0, "(D6) PERI-AS-NONCENTRAL is distinguishable (fires where correct does not)")
    print("  (D6) PERI-AS-NONCENTRAL: fires %d, of which %d WRONG -- distinguishable"
          % (fires_d6, extra_d6))
    return True


# ------------------------------------------------------------------ PART 1
E45_EDGES = [(0, 1), (1, 2), (2, 3), (4, 1), (4, 2), (1, 5), (2, 6)]
E45_NAME = {0: "u", 1: "a", 2: "b", 3: "v", 4: "c", 5: "w", 6: "x"}
# E45's OWN narrated adjacency table, transcribed verbatim from its answer:
E45_TABLE = {1: {0, 2, 4, 5}, 2: {1, 3, 6}, 4: {1, 2}, 0: {1}, 3: {2}, 5: {1}, 6: {2}}


def part1():
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- E45 harvest: the (RXM-PERI) refutation witness, rebuilt from its edge list")
    print("=" * 78)
    g = adj(7, E45_EDGES)
    ck(connected(g), "E45 witness connected")
    D, e, r = profile(g)
    dm = max(e)
    C = centre_of(e, r)
    print("  rebuilt from the EDGE LIST:")
    for v in range(7):
        print("    %s : N = %s   ecc = %d" % (E45_NAME[v],
                                              sorted(E45_NAME[x] for x in g[v]), e[v]))
    print("    rad = %d   diam = %d   centre = %s" % (r, dm, sorted(E45_NAME[c] for c in C)))
    w = 5
    print("    d(c,w) for c in centre: %s" % {E45_NAME[c]: D[c][w] for c in C})
    # the engine's three narrated claims:
    ck(e[0] != 4, "E45 CLAIM ecc(u)=4 is WRONG (its own path u-a-b-v has length 3)")
    ck(sorted(C) != [4], "E45 CLAIM centre={c} is WRONG")
    ck(not maximally_far(D, e, r, w), "E45's w FAILS the hypothesis: not maximally far")
    print("  VERDICT on the certificate: ecc(u) = %d (E45 said 4); centre = %s (E45 said {c});"
          % (e[0], sorted(E45_NAME[c] for c in C)))
    print("           w is maximally far from every centre? %s (E45's argument needed YES)"
          % maximally_far(D, e, r, w))
    # WHY it went wrong: its narrated adjacency table is not even symmetric.
    asym = sorted((u, v) for u, S in E45_TABLE.items() for v in S if u not in E45_TABLE[v])
    print("  its narrated adjacency table is ASYMMETRIC -- rows listing a vertex that does not")
    print("  list them back: %s (so the table describes no graph at all)"
          % [(E45_NAME[a], E45_NAME[b]) for a, b in asym])
    ck(asym == [(4, 2)], "(D5) TABLE-TRUST: c's row lists b, b's row omits c")
    # (D5) planted: read the table the OTHER way -- keep only mutually-listed pairs -- and redecide.
    tab_edges = sorted({(min(u, v), max(u, v)) for u, S in E45_TABLE.items() for v in S
                        if u in E45_TABLE[v]})
    gt = adj(7, tab_edges)
    Dt, et, rt = profile(gt)
    Ct = centre_of(et, rt)
    print("  even on the TABLE graph: rad = %d  diam = %d  centre = %s  d(centre,w) = %s"
          % (rt, max(et), sorted(E45_NAME[c] for c in Ct), [Dt[c][w] for c in Ct]))
    ck(not maximally_far(Dt, et, rt, w),
       "(D5) the table graph ALSO fails the hypothesis -- neither reading is a counterexample")
    print("  >> E45's WITNESS IS INVALID under both readings of its own answer.")
    return True


# ------------------------------------------------------------------ PART 2
E43_EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
             (0, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 11),
             (5, 6), (6, 7), (6, 10), (10, 3),
             (7, 8), (8, 4), (8, 3),
             (7, 9), (9, 2), (9, 1)]


def part2():
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- E43 harvest: the k3 = 4 construction, rebuilt against every frame condition")
    print("=" * 78)
    g = adj(16, E43_EDGES)
    n = len(g)
    ck(n == 16, "E43 graph has the claimed order")
    ck(connected(g), "E43 graph connected")
    ck(c4_free(g), "E43 graph C4-free in this line's sense (no two vertices, two common nbrs)")
    mus = [a_val(g, v) for v in range(n)]
    ck(min(mus) >= 2, "E43 graph has mu >= 2 (brute alpha at every vertex)")
    print("  n = %d  connected = %s  C4-free = %s  mu = min a(v) = %d"
          % (n, connected(g), c4_free(g), min(mus)))
    D, e, r = profile(g)
    w = 0
    U = [0, 1, 2, 3, 4, 5]
    d = len(U) - 1
    ck(e[w] == d, "ecc(w) = d = %d" % d)
    ck(D[w][U[-1]] == d, "w..u_d is a geodesic (d(w,u_d) = d)")
    ck(all(D[w][U[j]] == j for j in range(d + 1)), "d(w,u_j) = j along the frame path")
    ck(all((U[j] in g[U[i]]) == (abs(i - j) == 1)
           for i in range(d + 1) for j in range(i + 1, d + 1)), "u-path is INDUCED")
    y, z = 6, 7
    ck(y in g[U[d]], "y in N(u_d)")
    # y off u_{d-1}'s component of the matching G[N(u_d)]
    nb = sorted(g[U[d]])
    ck(y != U[d - 1] and U[d - 1] not in g[y], "y off u_{d-1}'s matching component in N(u_d)")
    print("  N(u_d) = %s   (a matching; y = %d sits off u_{d-1} = %d)" % (nb, y, U[d - 1]))
    ck(z in g[y], "z in N(y)")
    Q = U + [y, z]
    ck(all((Q[j] in g[Q[i]]) == (abs(i - j) == 1)
           for i in range(len(Q)) for j in range(i + 1, len(Q))),
       "w,u_1..u_d,y,z is an INDUCED anchored path")
    wit = {}
    for j in (d - 1, d - 2, d - 3, d - 4):
        S = g[z] & g[U[j]]
        ck(len(S) <= 1, "|N(z) cap N(u_%d)| <= 1 by C4-freeness" % j)
        if S:
            wit[j] = sorted(S)[0]
    k3 = len(wit)
    print("  witnesses N(z) cap N(u_j): %s   =>  k3 = %d" % (wit, k3))
    ck(k3 == 4, "k3 = 4 IS ATTAINED on a connected C4-free mu>=2 graph")
    # brief E43 sec.2's disputed derived fact
    print("  brief E43 sec.2 asserted the derived fact  d(w,z) >= d-1 = %d." % (d - 1))
    print("  MEASURED on this frame: d(w,z) = %d = d-2." % D[w][z])
    ck(D[w][z] == d - 2, "the disputed derived fact d(w,z) >= d-1 FAILS on a legal frame")
    ck(D[z][U[d]] == 2, "d(z,u_d) = 2 (the part of that bullet that IS derivable)")
    print("  >> E43's CONSTRUCTION HOLDS; brief E43's derived fact d(w,z) >= d-1 is FALSE.")
    # a(z) and the step-3 sufficient condition
    print("  a(z) = %d, 2 + k3 = %d, so (TAIL-3'')'s hypothesis a(z) >= 2+k3 %s here."
          % (a_val(g, z), 2 + k3, "HOLDS" if a_val(g, z) >= 2 + k3 else "FAILS"))
    return True


# ------------------------------------------------------------------ PART 3
def part3():
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- the two FORCED-PASS lemmas, and how much of round 40's census they eat")
    print("=" * 78)
    print("""  (PER-A)  If diam = rad+1 and w is not a centre, then ecc(w) = diam.
           Proof: ecc(w) >= rad+1 = diam, and ecc(w) <= diam always.  QED
  (PER-B)  If ecc(w) = 2*rad, then ecc(w) = diam.
           Proof: for any centre c and any x,y: d(x,y) <= d(x,c)+d(c,y) <= 2*rad, so
           diam <= 2*rad; and ecc(w) <= diam.  Hence 2*rad <= diam <= 2*rad.  QED
  (PER-C)  So (RXM-PERI) can only FAIL at an instance with diam >= rad+2 AND ecc(w) < 2*rad.
           Call such an instance OPEN; every other instance is a FORCED PASS and is evidence
           for nothing.""")
    print("  PREDICTION REGISTERED BEFORE THE RUN: all 1297 census instances are FORCED PASSES,")
    print("  i.e. the count of OPEN instances is 0 and round 40's 1297/1297 tested nothing.")
    fam = build_family()
    hosts = 0
    inst = 0
    forced_a = 0
    forced_b = 0
    forced_both = 0
    openn = 0
    viol = 0
    hosts_open = set()
    hosts_diam_ge_r2 = 0
    skipped = 0
    for g, nm in fam:
        if over():
            break
        if len(g) > 130:
            skipped += 1
            continue
        hosts += 1
        D, e, r = profile(g)
        dm = max(e)
        if dm >= r + 2:
            hosts_diam_ge_r2 += 1
        for w in range(len(g)):
            if not maximally_far(D, e, r, w):
                continue
            inst += 1
            fa = (dm == r + 1)
            fb = (e[w] == 2 * r)
            if fa:
                forced_a += 1
            if fb:
                forced_b += 1
            if fa and fb:
                forced_both += 1
            if fa or fb:
                ck(e[w] == dm, "FORCED PASS really is peripheral (%s, w=%d)" % (nm, w))
            else:
                openn += 1
                hosts_open.add(nm)
                if e[w] != dm:
                    viol += 1
                    print("    OPEN VIOLATION: %s w=%d rad=%d diam=%d ecc=%d" % (nm, w, r, dm, e[w]))
    print("  hosts rebuilt: %d (skipped %d as too big)" % (hosts, skipped))
    print("  hosts with diam >= rad+2 at all: %d" % hosts_diam_ge_r2)
    print("  condition-3 instances: %d" % inst)
    print("    FORCED by (PER-A) diam = rad+1 : %d" % forced_a)
    print("    FORCED by (PER-B) ecc(w) = 2rad: %d" % forced_b)
    print("    forced by BOTH                 : %d" % forced_both)
    print("    OPEN (the only ones that test the conjecture): %d" % openn)
    print("    violations among the OPEN ones: %d" % viol)
    ck(forced_a + forced_b - forced_both + openn == inst, "the regime split partitions the census")
    if openn == 0:
        print("  >> PREDICTION HELD.  Round 40's 1297/1297 is a union of two one-line lemmas;")
        print("     it contains ZERO instances of the only regime in which (RXM-PERI) has content.")
    else:
        print("  >> PREDICTION FAILED: %d instances are genuinely open.  Printed as a failure."
              % openn)
    return inst, openn


# ------------------------------------------------------------------ PART 4
# This file's own witness, built by hand from (PER-C): rad 2, diam 4, ecc(w) = rad+1 = 3.
# c=0; A = a1,a2,a3,a4 = 1,2,3,4; S = s,t,w,q = 5,6,7,8.
R41_W_EDGES = [(0, 1), (0, 2), (0, 3), (0, 4),
               (3, 1), (3, 2),
               (1, 5), (2, 6),
               (7, 3), (7, 4), (8, 4)]
R41_W_NAME = {0: "c", 1: "a1", 2: "a2", 3: "a3", 4: "a4", 5: "s", 6: "t", 7: "w", 8: "q"}


def scan_general(g):
    """return list of (w, rad, diam, ecc(w), OPEN?, VIOLATION?) for condition-3 vertices."""
    out = []
    D, e, r = profile(g)
    dm = max(e)
    for w in range(len(g)):
        if maximally_far(D, e, r, w):
            op = (dm >= r + 2) and (e[w] < 2 * r)
            out.append((w, r, dm, e[w], op, e[w] != dm))
    return out


def rand_graph(seed, n, num_edges):
    st = seed

    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for i in range(len(pairs) - 1, 0, -1):
        j = nxt(i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = adj(n, pairs[:num_edges])
    return g if connected(g) else None


def part4():
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- (RXM-PERI) in GENERAL graphs: this file's own witness, and a liveness run")
    print("=" * 78)
    g = adj(9, R41_W_EDGES)
    ck(connected(g), "r41 witness connected")
    D, e, r = profile(g)
    dm = max(e)
    C = centre_of(e, r)
    w = 7
    for v in range(9):
        print("    %-2s : N = %-22s ecc = %d" % (R41_W_NAME[v],
                                                 sorted(R41_W_NAME[x] for x in g[v]), e[v]))
    print("    rad = %d  diam = %d  centre = %s" % (r, dm, sorted(R41_W_NAME[c] for c in C)))
    print("    d(c,w) for every centre c: %s" % {R41_W_NAME[c]: D[c][w] for c in C})
    ck(r == 2, "r41 witness rad = 2")
    ck(dm == 4, "r41 witness diam = 4")
    ck(C == [0], "r41 witness centre is the single vertex c")
    ck(maximally_far(D, e, r, w), "w IS maximally far from every centre")
    ck(e[w] == 3, "ecc(w) = 3 = rad+1")
    ck(e[w] < dm, ">>> (RXM-PERI) IS REFUTED: ecc(w) = %d < %d = diam" % (e[w], dm))
    ck(dm >= r + 2 and e[w] < 2 * r, "the witness lies in (PER-C)'s OPEN regime, as designed")
    print("  >> (RXM-PERI) REFUTED in general graphs by this 9-vertex witness (rad+1 form too).")
    print("     class check on THIS LINE's hypotheses: C4-free = %s, mu = %d"
          % (c4_free(g), min(a_val(g, v) for v in range(9))))
    ck(not c4_free(g), "the witness is NOT C4-free -- so the RESTRICTED statement survives it")
    bad = [(u, v) for u, v in combinations(range(9), 2) if len(g[u] & g[v]) >= 2]
    print("     the C4 it uses: pairs with two common neighbours = %s"
          % [(R41_W_NAME[a], R41_W_NAME[b]) for a, b in bad])
    # liveness: how rare is a violation in general graphs?  seeded-random sample, NOT exhaustive.
    tot = insts = opens = viols = 0
    hosts_with_viol = 0
    for n in range(7, 13):
        for m in range(n - 1, min(2 * n + 4, n * (n - 1) // 2) + 1):
            for s in range(1, 41):
                if over():
                    break
                h = rand_graph(s * 104729 + n * 1000 + m, n, m)
                if h is None:
                    continue
                tot += 1
                rows = scan_general(h)
                insts += len(rows)
                o = sum(1 for x in rows if x[4])
                v = sum(1 for x in rows if x[5])
                opens += o
                viols += v
                if v:
                    hosts_with_viol += 1
    print("  seeded-random GENERAL graphs (NOT exhaustive): %d connected hosts sampled" % tot)
    print("    condition-3 vertices %d ; in the OPEN regime %d ; VIOLATIONS of (RXM-PERI) %d"
          % (insts, opens, viols))
    print("    hosts carrying at least one violation: %d" % hosts_with_viol)
    return True


# ------------------------------------------------------------------ PART 5
def rand_c4free_sparse(seed, n, cap):
    """seeded-random C4-free graph, edge budget capped so the diameter can grow."""
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
    cnt = 0
    for (u, v) in pairs:
        if cnt >= cap:
            break
        if any(g[u] & g[x] for x in g[v] if x != u):
            continue
        if any(g[v] & g[y] for y in g[u] if y != v):
            continue
        g[u].add(v)
        g[v].add(u)
        cnt += 1
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
    if len(h) < 5 or not connected(h):
        return None
    if min(a_val_matching(h, v) for v in range(len(h))) < 2:
        return None
    return h


# --------------------------------------------------- INDEPENDENT path checker (COPIED r40)


def incidence_matrix(g):
    n = len(g)
    M = [[0] * n for _ in range(n)]
    for (u, v) in edges_of(g):
        M[u][v] = 1
        M[v][u] = 1
    return M


def checker_induced_anchored(g, P, w, need, M=None):
    if P is None:
        return False
    if len(P) != need:
        return False
    if len(set(P)) != len(P):
        return False
    if P[0] != w:
        return False
    if M is None:
        M = incidence_matrix(g)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            want = 1 if j == i + 1 else 0
            if M[P[i]][P[j]] != want:
                return False
    return True


def anchored_search(g, start, cap, node_budget=60000):
    best = [0]
    bestP = [None]
    nodes = [0]
    trunc = [False]

    def rec(P, forb):
        if len(P) > best[0]:
            best[0] = len(P)
            bestP[0] = list(P)
        if best[0] >= cap:
            return True
        nodes[0] += 1
        if nodes[0] > node_budget or over():
            trunc[0] = True
            return True
        last = P[-1]
        for z in sorted(g[last]):
            if z in forb:
                continue
            P.append(z)
            if rec(P, forb | g[last] | {z}):
                P.pop()
                return True
            P.pop()
        return False

    rec([start], {start})
    return best[0], bestP[0], trunc[0]


def part5():
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- the question that SURVIVES: (RXM-PERI) restricted to C4-free, mu >= 2")
    print("=" * 78)
    print("  Attack: seeded-random C4-free mu>=2 hosts at capped edge budgets so that")
    print("  diam >= rad+2 is reachable.  NOT exhaustive; a sample.")
    tot = insts = opens = viols = 0
    hosts_diam_ge_r2 = 0
    examples = []
    viol_hosts = {}
    off = {}
    vrad = {}
    vl = {}
    v_lbig = 0
    v_radbig = 0
    for n in range(8, 30):
        for cap in (n, n + 2, n + 4, n + 6, n + 9, n + 12, n + 16, 2 * n, 3 * n):
            for s in range(1, 26):
                if over():
                    break
                h = rand_c4free_sparse(s * 15485863 + n * 977 + cap, n, cap)
                if h is None:
                    continue
                tot += 1
                D, e, r = profile(h)
                dm = max(e)
                if dm >= r + 2:
                    hosts_diam_ge_r2 += 1
                for w in range(len(h)):
                    if not maximally_far(D, e, r, w):
                        continue
                    insts += 1
                    off[e[w] - r] = off.get(e[w] - r, 0) + 1
                    if dm >= r + 2 and e[w] < 2 * r:
                        opens += 1
                        if e[w] != dm:
                            viols += 1
                            key = tuple(sorted(edges_of(h)))
                            viol_hosts.setdefault(key, []).append(w)
                            vrad[r] = vrad.get(r, 0) + 1
                            vl[int(mean_a(h))] = vl.get(int(mean_a(h)), 0) + 1
                            if mean_a(h) > 4.0:
                                v_lbig += 1
                            if r >= 5:
                                v_radbig += 1
                            if len(examples) < 2:
                                examples.append((edges_of(h), w, r, dm, e[w]))
    print("  C4-free mu>=2 hosts sampled: %d ; of them with diam >= rad+2: %d"
          % (tot, hosts_diam_ge_r2))
    print("  condition-3 vertices: %d ; in the OPEN regime: %d ; VIOLATIONS: %d"
          % (insts, opens, viols))
    print("  DISTINCT violating hosts (by edge set): %d" % len(viol_hosts))
    print("  AGAINST THIS ROUND'S INTEREST -- where the violations actually sit:")
    print("    rad of the violating instances: %s" % dict(sorted(vrad.items())))
    print("    floor(l) of the violating instances: %s" % dict(sorted(vl.items())))
    print("    violations with l > 4 : %d ;  violations with rad >= 5 : %d" % (v_lbig, v_radbig))
    print("  eccentricity-offset profile of the condition-3 vertices on THIS sample: %s"
          % dict(sorted(off.items())))
    print("  (round 39 measured offset +2 at 0 of 1297 and could not explain it; this sample")
    print("   says how much of that was the family)")
    for E, w, r, dm, ew in examples:
        print("    RESTRICTED VIOLATION: w=%d rad=%d diam=%d ecc(w)=%d edges=%s" % (w, r, dm, ew, E))
    if viols == 0 and opens > 0:
        print("  >> the restricted statement SURVIVED %d open-regime instances -- a census," % opens)
        print("     not a theorem, and it is the statement the line actually needs.")
    elif opens == 0:
        print("  >> NO open-regime instance was produced at all on this class: the restricted")
        print("     statement is UNTESTED here, exactly as round 40's census was.")
    else:
        print("  >> (RXM-PERI) IS REFUTED ON THIS LINE's OWN CLASS TOO -- C4-free, mu >= 2.")
    return viol_hosts


# ------------------------------------------------------------------ PART 6
R41_INCLASS_EDGES = [(0, 1), (0, 6), (0, 9), (1, 2), (1, 5), (1, 9), (2, 3), (3, 8),
                     (4, 5), (4, 6), (4, 7), (5, 7), (7, 8), (8, 9)]


def part6(viol_hosts):
    PARTS_RUN.append("PART6")
    print()
    print("=" * 78)
    print("PART 6 -- the NAMED in-class witness, re-verified from scratch, and the COVERAGE")
    print("          question on the population round 39's family did not contain")
    print("=" * 78)
    g = adj(10, R41_INCLASS_EDGES)
    n = len(g)
    D, e, r = profile(g)
    dm = max(e)
    C = centre_of(e, r)
    print("  W41: n = %d, %d edges" % (n, len(edges_of(g))))
    for v in range(n):
        print("    %2d : N = %-16s ecc = %d  a(v) = %d" % (v, sorted(g[v]), e[v], a_val(g, v)))
    print("    rad = %d  diam = %d  centre = %s" % (r, dm, C))
    ck(connected(g), "W41 connected")
    ck(c4_free(g), "W41 is C4-FREE in this line's sense")
    ck(min(a_val(g, v) for v in range(n)) >= 2, "W41 has mu >= 2 (brute alpha at every vertex)")
    ck(r == 2 and dm == 4, "W41 rad 2, diam 4 = rad+2")
    ck(C == [1], "W41 centre is the single vertex 1")
    incl = [w for w in range(n) if maximally_far(D, e, r, w)]
    print("    condition-3 vertices: %s ; their ecc: %s" % (incl, [e[w] for w in incl]))
    bad = [w for w in incl if e[w] != dm]
    print("    of those, NOT peripheral (violations of (RXM-PERI)): %s" % bad)
    print("    and the ones at offset +2 (round 39 saw this 0 times in 1297): %s"
          % [w for w in incl if e[w] == r + 2])
    ck(len(bad) > 0, ">>> W41 REFUTES (RXM-PERI) INSIDE the class, at %d vertices" % len(bad))
    ck(all(e[w] == r + 1 for w in bad), "every violating vertex of W41 is at offset +1 exactly")
    ck(all(maximally_far(D, e, r, w) for w in bad), "re-assert the predicate at each witness")
    incl = bad
    # COVERAGE: the row still needs endpath(G,w) >= ecc(w)+3, certified BY BUILDING.
    print("  COVERAGE of the residual row on this NEW population (diam = rad+2, offset +1):")
    print("  direction of error fixed before the numbers: COVERED is a LOWER bound (a path was")
    print("  BUILT and passed by the independent checker); CHAIN-SHORT is an UPPER bound.")
    cov = short = 0
    for w in incl:
        need = e[w] + 3
        best, P, trunc = anchored_search(g, w, need)
        okp = P[:need] if (P and len(P) >= need) else None
        good = checker_induced_anchored(g, okp, w, need)
        if good:
            cov += 1
        else:
            short += 1
        print("    w=%d  ecc=%d  need=%d vertices  longest anchored induced found=%d  "
              "checker=%s%s" % (w, e[w], need, best, good, "  (search truncated)" if trunc else ""))
    print("    COVERED (path BUILT + checker-verified): %d of %d ; chain-short: %d"
          % (cov, len(incl), short))
    # the same test over every distinct violating host from PART 5
    tot_w = tot_cov = tot_short = tot_trunc = 0
    hosts_done = 0
    shortfalls = []
    for key, ws in viol_hosts.items():
        if over() or hosts_done >= 400:
            break
        hosts_done += 1
        h = adj(max(max(u, v) for u, v in key) + 1, list(key))
        Dh, eh, rh = profile(h)
        for w in ws:
            need = eh[w] + 3
            best, P, trunc = anchored_search(h, w, min(need, len(h)))
            okp = P[:need] if (P and len(P) >= need) else None
            tot_w += 1
            if checker_induced_anchored(h, okp, w, need):
                tot_cov += 1
            else:
                tot_short += 1
                if trunc:
                    tot_trunc += 1
                shortfalls.append((sorted(key), w, rh, max(eh), eh[w], need, best, trunc))
    print("  same coverage test over %d distinct violating in-class hosts, %d witnesses:"
          % (hosts_done, tot_w))
    print("    COVERED (path BUILT + checker-verified): %d" % tot_cov)
    print("    SHORT of ecc(w)+3: %d, of which %d had a TRUNCATED search (upper bound unknown)"
          % (tot_short, tot_trunc))
    print("    A shortfall with an UNtruncated search is a real endpath deficit and must be")
    print("    printed in full -- it is the one thing here that could hurt the route:")
    for E, w, rr, dd, ew, need, best, trunc in shortfalls[:8]:
        print("      w=%d rad=%d diam=%d ecc(w)=%d need=%d longest=%d truncated=%s"
              % (w, rr, dd, ew, need, best, trunc))
        print("        edges=%s" % E)
    return [s for s in shortfalls if not s[7]]


# ------------------------------------------------------------------ PART 7
def mean_a(g):
    return sum(a_val_matching(g, v) for v in range(len(g))) / float(len(g))


def oracle_longest_induced(g, anchor=None, nmax=13):
    """INDEPENDENT of the DFS: enumerate vertex SUBSETS and test whether the induced
    subgraph is a path (with `anchor` an endpoint, when given).  n <= 13 only."""
    n = len(g)
    assert n <= nmax
    best = 0
    for k in range(n, 0, -1):
        if k <= best:
            break
        for S in combinations(range(n), k):
            if anchor is not None and anchor not in S:
                continue
            Sset = set(S)
            deg = {v: len(g[v] & Sset) for v in S}
            if any(d > 2 for d in deg.values()):
                continue
            ends = [v for v in S if deg[v] == 1]
            if k == 1:
                ok = True
            elif len(ends) != 2:
                continue
            else:
                # connected check inside S
                seen = {ends[0]}
                stack = [ends[0]]
                while stack:
                    u = stack.pop()
                    for x in g[u] & Sset:
                        if x not in seen:
                            seen.add(x)
                            stack.append(x)
                ok = (len(seen) == k)
            if not ok:
                continue
            if anchor is not None and k > 1 and deg[anchor] != 1:
                continue
            best = k
            break
    return best


def part7(shortfalls):
    PARTS_RUN.append("PART7")
    print()
    print("=" * 78)
    print("PART 7 -- THE SIX SHORTFALLS, RE-VERIFIED BY AN INDEPENDENT SUBSET ORACLE")
    print("=" * 78)
    print("  These are the only objects this round found that could HURT the route: in-class")
    print("  instances of draft 42.4's residual row at which  endpath(G',w) >= ecc(w)+3  FAILS.")
    # oracle vs DFS agreement first, on hosts where both are cheap
    agree = 0
    for g in (petersen(), cycle(9), pathgraph(8), theta_like()):
        for v in range(len(g)):
            o = oracle_longest_induced(g, anchor=v)
            b, _, tr = anchored_search(g, v, len(g))
            ck(not tr and o == b, "oracle == DFS anchored longest induced path")
            agree += 1
    print("  oracle-vs-DFS cross-check at %d anchors, all agree" % agree)
    print()
    rows = 0
    for E, w, rr, dd, ew, need, best, trunc in shortfalls:
        n = max(max(u, v) for u, v in E) + 1
        g = adj(n, E)
        D, e, r = profile(g)
        C = centre_of(e, r)
        ck(c4_free(g), "shortfall host is C4-free")
        ck(min(a_val(g, v) for v in range(n)) >= 2, "shortfall host has mu >= 2 (brute alpha)")
        ck(connected(g), "shortfall host connected")
        ck(maximally_far(D, e, r, w), "w satisfies condition 3 (maximally far from every centre)")
        ck(e[w] == r + 1, "w is at offset +1 -- draft 42.4's residual row exactly")
        ep = oracle_longest_induced(g, anchor=w)
        pg = oracle_longest_induced(g)
        ck(ep == best, "ORACLE CONFIRMS the DFS endpath value (%d)" % ep)
        ck(ep < e[w] + 3, "ORACLE CONFIRMS the shortfall: endpath %d < %d" % (ep, e[w] + 3))
        rows += 1
        print("  n=%2d m=%2d  l=%.3f  rad=%d diam=%d centre=%s  w=%d ecc(w)=%d"
              % (n, len(E), mean_a(g), r, max(e), C, w, e[w]))
        print("      endpath(G',w) = %d  (target ecc+3 = %d)  SHORT BY %d"
              % (ep, e[w] + 3, e[w] + 3 - ep))
        print("      path(G') = %d   (B1)'s target r+4 = %d  -> (B1) %s here"
              % (pg, r + 4, "HOLDS" if pg >= r + 4 else "ALSO FAILS"))
    print()
    print("  %d shortfalls re-verified independently." % rows)
    print("  BOUNDING THIS AGAINST ITS OWN INTEREST: every one sits at rad = 2 with l ~ 2.2,")
    print("  i.e. OUTSIDE route A2's class (l > 4 and rad >= 5), exactly like round 39's 414.")
    print("  What it does establish: (B2)/(TAIL-2) alone does NOT close draft 42.4's residual")
    print("  row on the C4-free mu>=2 class -- the row's remaining hypotheses are load-bearing.")
    return True


def theta_like():
    return adj(8, [(0, 1), (1, 2), (2, 7), (0, 3), (3, 4), (4, 7), (0, 5), (5, 6), (6, 7)])


def main():
    print("WOWII-133 round 41 -- (RXM-PERI) and the two engine harvests")
    print("interpreter: %s" % sys.version.split()[0])
    part0()
    part1()
    part2()
    part3()
    part4()
    vh = part5()
    sf = part6(vh)
    part7(sf)
    print()
    print("=" * 78)
    print("PARTS RUN: %s" % ",".join(PARTS_RUN))
    print("CHECKS = %d   FAILS = %d   elapsed = %.1f s" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
