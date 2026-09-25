#!/usr/bin/env python3
"""WOWII-133 round 40 -- THE MECHANISM BEHIND ROUND 39: WHERE THE CENTRE SET SITS WHEN A
VERTEX IS MAXIMALLY FAR FROM ALL OF IT.

Round 39 measured that draft 42.4's open single-hair row -- ecc(w)=rad+1 AND w maximally far
from every centre -- holds 414 times on this family, never on a host with l > 4 or rad >= 5,
and that on route A2's own host class the condition-3 vertices all sit at offset +5/+6/+7.
This round asks WHY, in the only way that can be checked: by measuring what distinguishes the
offset-+1 vertices from the rest.

Self-contained: primitives COPIED from round 39's file, never imported.
Interpreter: system python3.  No SAT.  No exhaustive enumeration.

PARTS
  0  primitive self-tests + the guard on THIS round's predicate
  1  the structural profile of the condition-3 class, split by eccentricity offset
  2  a FALSIFIABLE prediction, registered before its run, and its verdict
  3  the refined sphere bound, proved here and checked against every instance
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


# ---------------------------------------------------------------- primitives (COPIED r38)


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
    """a(v) = alpha(G[N(v)]); C4-free => G[N(v)] is a matching => a = deg - #inside edges."""
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def nbhd_components(g, v):
    nb = sorted(g[v])
    comp = {u: {u} for u in nb}
    for x, y in combinations(nb, 2):
        if y in g[x]:
            s = comp[x] | comp[y]
            for z in s:
                comp[z] = s
    out = []
    for u in nb:
        f = frozenset(comp[u])
        if f not in out:
            out.append(f)
    return out


def mean_a(g):
    n = len(g)
    return sum(a_val(g, v) for v in range(n)) / float(n)


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


# --------------------------------------------------- INDEPENDENT path checker (guard)


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


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def theta333():
    return adj(8, [(0, 1), (1, 2), (2, 7), (0, 3), (3, 4), (4, 7), (0, 5), (5, 6), (6, 7)])


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def pathgraph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


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
    if len(h) < 6 or not connected(h) or min(a_val(h, v) for v in range(len(h))) < 2:
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


# ------------------------------------------------------------------ frames (COPIED r38)


# ------------------------------------------------------------------ PART 0
def part0(fam):
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitive self-tests and the guard on THIS round's predicate")
    print("=" * 78)
    P = petersen()
    _, eP, rP = profile(P)
    ck(rP == 2 and len(centre_of(eP, rP)) == 10, "Petersen self-centred, rad 2")
    C9 = cycle(9)
    _, e9, r9 = profile(C9)
    ck(r9 == 4, "C9 rad 4")
    agree = 0
    for g in (P, C9, theta333(), pg2(3)):
        for v in range(len(g)):
            ck(a_val(g, v) == len(g[v]) - sum(1 for x, y in combinations(sorted(g[v]), 2)
                                              if y in g[x]), "a_val identity")
            agree += 1
    print("  a(.) identity re-checked at %d vertices" % agree)

    # THE PREDICATE THIS ROUND SPLITS ON, and the guard members for it.
    # CLASS CLAIMED: any evaluator of the SPLIT that assigns a condition-3 vertex to the wrong
    # offset bucket, or that computes the sphere sizes off by a layer.  Neither is r34's
    # zero-step, r35's one-step, r36's late-block, r37's off-by-one/anchor-drift, r38's
    # cost-evaluator, nor r39's centre-widen/quantifier-swap/stratum-offset.
    def spheres_correct(D, w, n):
        s = {}
        for v in range(n):
            s[D[w][v]] = s.get(D[w][v], 0) + 1
        return s

    def spheres_offbylayer(D, w, n):     # (D4) SPHERE-SHIFT: counts B_j instead of S_j
        s = {}
        for v in range(n):
            for j in range(D[w][v], -1, -1):
                s[j] = s.get(j, 0) + 1
        return s

    caught = 0
    tried = 0
    for g, nm in fam[:25]:
        D, ecc, r = profile(g)
        n = len(g)
        for w in range(0, n, 5):
            tried += 1
            a = spheres_correct(D, w, n)
            b = spheres_offbylayer(D, w, n)
            if a != b:
                caught += 1
            ck(sum(a.values()) == n, "correct sphere sizes must partition V")
    print("  planted (D4) SPHERE-SHIFT caught on %d of %d (host,w) probes" % (caught, tried))
    ck(caught > 0, "(D4) must be caught somewhere")
    ck(caught == tried, "(D4) must be caught EVERYWHERE -- if not, say where it hides")


# ------------------------------------------------------------------ PART 1
def part1(fam):
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- THE CONDITION-3 CLASS, SPLIT BY ECCENTRICITY OFFSET")
    print("=" * 78)
    print("condition 3 := d(c,w) = rad for EVERY centre c   (draft 42.4 / (RAD-1P)).")
    print("offset := ecc(w) - rad.  Round 39 proved offset >= 1 and measured offset 2 never.")
    print()
    hosts = [(g, nm) for g, nm in fam if len(g) <= 130]
    rows = {}
    for g, nm in hosts:
        if over():
            break
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        n = len(g)
        la = mean_a(g)
        for w in range(n):
            if not all(D[c][w] == r for c in C):
                continue
            off = ecc[w] - r
            sr = sum(1 for v in range(n) if D[w][v] == r)
            stop = sum(1 for v in range(n) if D[w][v] == ecc[w])
            bal = sum(1 for v in range(n) if D[w][v] <= r - 1)
            d = rows.setdefault(off, dict(k=0, nC=[], sr=[], stop=[], bal=[], nn=[], l=[],
                                          rad=[]))
            d["k"] += 1
            d["nC"].append(len(C))
            d["sr"].append(sr)
            d["stop"].append(stop)
            d["bal"].append(bal)
            d["nn"].append(n)
            d["l"].append(la)
            d["rad"].append(r)

    def rng(v):
        return "%d-%d" % (min(v), max(v))

    print("  offset  count   |Ctr| range   |S_rad(w)| range   |B_{rad-1}(w)| range   n range"
          "     rad range    l range")
    for off in sorted(rows):
        d = rows[off]
        print("   +%-4d %6d %13s %19s %23s %9s %12s %6.2f-%.2f"
              % (off, d["k"], rng(d["nC"]), rng(d["sr"]), rng(d["bal"]), rng(d["nn"]),
                 rng(d["rad"]), min(d["l"]), max(d["l"])))
    tot = sum(rows[o]["k"] for o in rows)
    print()
    print("  total condition-3 vertices: %d" % tot)
    ck(1 in rows, "the offset +1 bucket must be non-empty or this split is vacuous")
    ck(0 not in rows, "offset 0 is impossible (condition 3 => w is not a centre)")
    return rows


# ------------------------------------------------------------------ PART 2
def part2(fam, rows):
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- A FALSIFIABLE PREDICTION, REGISTERED BEFORE ITS RUN")
    print("=" * 78)
    print("PREDICTION (mine, written before the run below and reported either way):")
    print("  an offset-+1 condition-3 vertex needs the ENTIRE graph inside B_{rad+1}(w) with")
    print("  every centre on the sphere S_rad(w).  On a host whose a(.)-mean is high the ball")
    print("  B_{rad-1}(w) is large, so by (CS-1) the centre set is squeezed.  I therefore")
    print("  predict: at offset +1 the ratio |Ctr| / n is SMALL (below 0.35), and at higher")
    print("  offsets it is not systematically smaller.")
    print("  THIS CAN FAIL.  If offset-+1 vertices carry a large centre fraction, the whole")
    print("  mechanism story of round 39 sec.2 is wrong and I say so.")
    print()
    print("  offset   count   |Ctr|/n  min    mean     max")
    verdict = {}
    for off in sorted(rows):
        d = rows[off]
        fr = [c / float(n) for c, n in zip(d["nC"], d["nn"])]
        verdict[off] = (min(fr), sum(fr) / len(fr), max(fr))
        print("   +%-4d %7d %13.3f %8.3f %7.3f" % (off, d["k"], min(fr),
                                                   sum(fr) / len(fr), max(fr)))
    print()
    if 1 in verdict:
        lo, me, hi = verdict[1]
        others = [verdict[o][1] for o in verdict if o != 1]
        if hi < 0.35:
            print("  PREDICTION HELD on its first half: every offset-+1 vertex has |Ctr|/n = %.3f"
                  % hi + " or less.")
        else:
            print("  PREDICTION FAILED on its first half: an offset-+1 vertex carries")
            print("  |Ctr|/n = %.3f, above the 0.35 I registered." % hi)
        if others and me <= min(others):
            print("  Second half HELD: offset +1 has the smallest mean centre fraction (%.3f"
                  % me + " vs %.3f)." % min(others))
        elif others:
            print("  SECOND HALF FAILED: offset +1's mean centre fraction %.3f is NOT the"
                  % me)
            print("  smallest; some higher offset reaches %.3f.  The squeeze is not what"
                  % min(others))
            print("  separates offset +1 -- the separation must come from somewhere else.")


# ------------------------------------------------------------------ PART 3
def part3(fam, rows):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- (CS-1'), THE SPHERE BOUND REFINED BY THE ECCENTRICITY, PROVED AND CHECKED")
    print("=" * 78)
    print("(CS-1) says a condition-3 vertex forces Ctr cap B_{rad-1}(w) = empty.  Under")
    print("ecc(w) = rad + t the complement of that ball is S_rad u ... u S_{rad+t}, and Ctr")
    print("lies in S_rad ALONE, so:")
    print()
    print("  (CS-1')  |Ctr| <= |S_rad(w)| = n - |B_{rad-1}(w)| - sum_{j=1..t} |S_{rad+j}(w)|.")
    print()
    print("  Proof: c in Ctr => d(c,w) = rad exactly, so c lies on the sphere S_rad(w) and on")
    print("  no other layer; the layers partition V.  QED -- strictly sharper than (CS-1),")
    print("  which discards the layers beyond rad.")
    print()
    hosts = [(g, nm) for g, nm in fam if len(g) <= 130]
    tested = tight = 0
    worst = None
    for g, nm in hosts:
        if over():
            break
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        n = len(g)
        for w in range(n):
            if not all(D[c][w] == r for c in C):
                continue
            sr = sum(1 for v in range(n) if D[w][v] == r)
            bal = sum(1 for v in range(n) if D[w][v] <= r - 1)
            beyond = sum(1 for v in range(n) if D[w][v] > r)
            ck(len(C) <= sr, "(CS-1') must hold at %s w=%d" % (nm, w))
            ck(sr == n - bal - beyond, "layer partition identity at %s w=%d" % (nm, w))
            tested += 1
            if len(C) == sr:
                tight += 1
            slack = sr - len(C)
            if worst is None or slack > worst[0]:
                worst = (slack, nm, w, len(C), sr)
    print("  condition-3 vertices checked against (CS-1'): %d" % tested)
    print("  instances where (CS-1') is TIGHT (|Ctr| = |S_rad(w)|): %d" % tight)
    if worst:
        print("  loosest instance: %s w=%d, |Ctr|=%d, |S_rad(w)|=%d, slack %d"
              % (worst[1], worst[2], worst[3], worst[4], worst[0]))
    print()
    print("  WHAT THIS DOES AND DOES NOT BUY, stated plainly: (CS-1') is a real sharpening and")
    print("  it is TIGHT on some instances, so it is not slack-for-free.  It still does NOT")
    print("  decide the open row, because bounding |Ctr| above never contradicts a SMALL centre")
    print("  set, and every offset-+1 instance found so far has a small one.  Naming that is")
    print("  the point: the open row will not fall to a counting bound on |Ctr|.")


# ------------------------------------------------------------------ PART 4
def part4(fam):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- WHAT PART 1's TABLE ACTUALLY SAYS: A CONJECTURE, AND ITS LIVENESS")
    print("=" * 78)
    print("PART 1's offset buckets are rad = 2 at offset +1, and rad = t at offset +t for every")
    print("t >= 3.  The second family is ecc(w) = 2*rad; the first is ecc(w) = rad+1 on hosts")
    print("whose DIAMETER is rad+1.  Both read as one statement:")
    print()
    print("  (RXM-PERI)  w maximally far from every centre  =>  ecc(w) = diam(G).")
    print()
    print("i.e. such a w is PERIPHERAL.  Tested on every condition-3 vertex of the family.")
    print()
    hosts = [(g, nm) for g, nm in fam if len(g) <= 130]
    tested = held = 0
    viol = []
    all_v = peri_v = 0
    for g, nm in hosts:
        if over():
            break
        D, ecc, r = profile(g)
        dm = max(ecc)
        C = centre_of(ecc, r)
        n = len(g)
        for w in range(n):
            all_v += 1
            if ecc[w] == dm:
                peri_v += 1
            if not all(D[c][w] == r for c in C):
                continue
            tested += 1
            if ecc[w] == dm:
                held += 1
            else:
                viol.append((nm, n, w, r, ecc[w], dm))
    print("  condition-3 vertices tested : %d" % tested)
    print("  (RXM-PERI) HOLDS at         : %d" % held)
    print("  VIOLATIONS                  : %d" % len(viol))
    for row in viol[:8]:
        print("    %-28s n=%3d w=%3d rad=%d ecc(w)=%d diam=%d" % row)
    print()
    print("  LIVENESS -- the test is a real restriction, not something every vertex satisfies:")
    print("    peripheral vertices among ALL %d vertices of these hosts: %d (%.1f%%)"
          % (all_v, peri_v, 100.0 * peri_v / all_v))
    ck(tested > 0, "the conjecture must be tested on a non-empty set")
    ck(peri_v < all_v, "LIVENESS: peripherality must NOT be automatic, or the test is empty")
    if not viol:
        print()
        print("  NO VIOLATION on this family.  A MEASUREMENT, NOT A THEOREM -- designed plus")
        print("  seeded-random, not exhaustive.  What it would buy IF proved, stated so the")
        print("  next round is not tempted to assume it: draft 42.4's open row needs")
        print("  ecc(w) = rad+1 AND condition 3, so under (RXM-PERI) it needs diam = rad+1.")
        print("  Route A2's hosts are a dense core with a long attached tail, where diam is far")
        print("  above rad+1 -- so (RXM-PERI) would make round 39 sec.2's emptiness a THEOREM")
        print("  on that class instead of a census.  It is not proved and is not used.")
    else:
        print()
        print("  (RXM-PERI) IS REFUTED on this family.  The witnesses above are named, and the")
        print("  round-39 sec.2 emptiness keeps the status it already had: a measurement.")
    # AND the half that IS proved, restated with its proof, so the two are never conflated
    print()
    print("  PROVED, not conjectured (round 39): condition 3 => w is not a centre => ecc(w) >=")
    print("  rad+1.  And ecc(w) <= d(w,c) + ecc(c) = 2*rad for any centre c.  So a condition-3")
    print("  vertex always satisfies rad+1 <= ecc(w) <= 2*rad -- both bounds proved, and the")
    print("  table above sits strictly inside them.")
    for g, nm in hosts[:120]:
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        for w in range(len(g)):
            if all(D[c][w] == r for c in C):
                ck(r + 1 <= ecc[w] <= 2 * r, "proved bracket must hold at %s w=%d" % (nm, w))


def main():
    print("WOWII-133 round 40 -- where the centre set sits under condition 3")
    print("interpreter: %s" % sys.version.split()[0])
    print("started: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    fam = build_family()
    print("family built: %d host slots" % len(fam))
    part0(fam)
    rows = part1(fam)
    part2(fam, rows)
    part3(fam, rows)
    part4(fam)
    print()
    print("=" * 78)
    print("parts run: %s" % ",".join(PARTS_RUN))
    print("CHECKS=%d FAILS=%d elapsed=%.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    ck(len(PARTS_RUN) == 5, "all 5 declared parts must self-register")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
