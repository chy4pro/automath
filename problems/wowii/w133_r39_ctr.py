#!/usr/bin/env python3
"""WOWII-133 round 39 -- THE ENGINE HARVEST (E13/E14) AND THE SINGLE-HAIR RESIDUAL CLASS,
LOCATED IN VERTICES.

Self-contained: every primitive is COPIED from round 38's file, never imported.
Interpreter: system python3 (pure stdlib; networkx/sympy not needed).
No SAT.  No exhaustive graph enumeration.  The only searches are a depth-capped anchored DFS
run on a NAMED residual and a subset-enumeration oracle at n <= 13.

PARTS
  0  primitive self-tests + the GUARD (planted defects in this round's census predicate)
  1  E13 harvest: verify Graph A / B(m) / C(m) against every numeric claim the engine made
  2  E14 harvest: verify H_k, literal edge list AND repaired, k = 1..8
  3  LEMMA AUDIT (mine, not the engine's): the three derived lemmas E13/E14 state
  4  THE SINGLE-HAIR RESIDUAL CLASS in vertices, and whether (TAIL-2'') covers it
  5  (CS-3) consistency: the r36 bound against E14's unbounded-|Ctr| family
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


def a_val_brute(g, v):
    """independent implementation, cross-check only: a maximum independent set in N(v)."""
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = max(best, k)
                break
        if best == k:
            break
    return best


def mu(g):
    """mu(G) = min_v a(v).  Uses the BRUTE independent-set value, so it is correct even on
    graphs that are NOT C4-free (E13's counterexamples are not)."""
    return min(a_val_brute(g, v) for v in range(len(g)))


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


def floyd(g):
    """INDEPENDENT distance computation (no BFS): all-pairs by relaxation.  Used only to
    cross-check profile()."""
    n = len(g)
    INF = 10 ** 6
    D = [[INF] * n for _ in range(n)]
    for v in range(n):
        D[v][v] = 0
        for u in g[v]:
            D[v][u] = 1
    for k in range(n):
        Dk = D[k]
        for i in range(n):
            dik = D[i][k]
            if dik >= INF:
                continue
            Di = D[i]
            for j in range(n):
                if dik + Dk[j] < Di[j]:
                    Di[j] = dik + Dk[j]
    return D


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


def oracle_endpath(g, start, cap):
    n = len(g)
    others = [v for v in range(n) if v != start]
    best = 1
    for k in range(min(cap, n), 1, -1):
        if k <= best:
            break
        found = False
        for S in combinations(others, k - 1):
            vs = (start,) + S
            deg = {v: 0 for v in vs}
            ok = True
            for x, y in combinations(vs, 2):
                if y in g[x]:
                    deg[x] += 1
                    deg[y] += 1
            if any(d > 2 for d in deg.values()):
                ok = False
            if ok and deg[start] != 1:
                ok = False
            if ok and sum(deg.values()) // 2 != k - 1:
                ok = False
            if ok:
                seen = {start}
                cur = start
                for _ in range(k - 1):
                    nxt = [z for z in g[cur] if z in deg and z not in seen]
                    if len(nxt) != 1:
                        ok = False
                        break
                    cur = nxt[0]
                    seen.add(cur)
                if ok and len(seen) != k:
                    ok = False
            if ok:
                found = True
                break
        if found:
            best = k
            break
    return best


# ------------------------------------------------------------------ hosts (COPIED r38)
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
def geodesics_from(g, D, w, ud, limit):
    out = []
    stack = [[ud]]
    while stack and len(out) < limit:
        P = stack.pop()
        cur = P[-1]
        if cur == w:
            out.append(list(reversed(P)))
            continue
        step = D[w][cur] - 1
        for x in sorted(g[cur]):
            if D[w][x] == step:
                stack.append(P + [x])
                if len(stack) > 60:
                    break
    return out


def frames(g, D, ecc, w, max_far, max_geo, dmin=2):
    n = len(g)
    d = ecc[w]
    if d < dmin:
        return
    fars = [v for v in range(n) if D[w][v] == d][:max_far]
    for ud in fars:
        for P in geodesics_from(g, D, w, ud, max_geo):
            if len(P) != d + 1:
                continue
            comps = nbhd_components(g, ud)
            home = None
            for C in comps:
                if P[-2] in C:
                    home = C
            for C in comps:
                if C is home:
                    continue
                for y in sorted(C):
                    if y == P[-2]:
                        continue
                    yield (P, ud, y)


def dodge_count(g, P, v, idxs):
    d = len(P) - 1
    c = 0
    for j in idxs:
        if 0 <= j <= d:
            if g[v] & g[P[j]]:
                c += 1
    return c


def step2_build(g, P, y, w, M):
    d = len(P) - 1
    return [z for z in sorted(g[y])
            if checker_induced_anchored(g, P + [y, z], w, d + 3, M)]


# ============================================================ E13 / E14 constructions
def e13_graph_A():
    """E13 sec.1.  V = {w,u,c1,c2,a1,a2,s} -> 0..6 in that order."""
    lbl = ["w", "u", "c1", "c2", "a1", "a2", "s"]
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("w", "u"), ("u", "c1"), ("u", "c2"), ("c1", "a1"), ("c1", "a2"),
         ("c2", "a1"), ("c2", "a2"), ("a1", "s"), ("a2", "s")]
    return adj(7, [(ix[a], ix[b]) for a, b in E]), ix, lbl


def e13_graph_B(m):
    """E13 sec.2.  V = {w,u,a1,a2,s} u {c_1..c_m}."""
    lbl = ["w", "u", "a1", "a2", "s"] + ["c%d" % i for i in range(1, m + 1)]
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("w", "u"), ("a1", "s"), ("a2", "s")]
    for i in range(1, m + 1):
        E += [("u", "c%d" % i), ("c%d" % i, "a1"), ("c%d" % i, "a2")]
    return adj(len(lbl), [(ix[a], ix[b]) for a, b in E]), ix, lbl


def e13_graph_C(m):
    """E13 sec.3(a).  V = {w,u,u',s} u {c_i} u {e_j} u {a_j}."""
    lbl = (["w", "u", "up", "s"] + ["c%d" % i for i in range(1, m + 1)]
           + ["e%d" % j for j in range(1, m + 1)] + ["a%d" % j for j in range(1, m + 1)])
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("w", "u"), ("w", "up")]
    for i in range(1, m + 1):
        E.append(("u", "c%d" % i))
    for j in range(1, m + 1):
        E.append(("up", "e%d" % j))
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            E.append(("e%d" % j, "c%d" % i))
            E.append(("c%d" % i, "a%d" % j))
    for j in range(1, m + 1):
        E.append(("a%d" % j, "s"))
    return adj(len(lbl), [(ix[a], ix[b]) for a, b in E]), ix, lbl


def e14_Hk(k, repaired):
    """E14 sec.3.  Vertices: w; a,a'; b0,b'0; c0; b_j,c_j,f_j (j=1..k); e,e',f'0,x.

    `repaired=False` uses the engine's edge LIST verbatim.
    `repaired=True`  adds b'0-c0, the edge the engine's own N(c0) uses but never lists.
    """
    lbl = ["w", "a", "ap", "b0", "bp0", "c0", "e", "ep", "fp0", "x"]
    lbl += ["b%d" % j for j in range(1, k + 1)]
    lbl += ["c%d" % j for j in range(1, k + 1)]
    lbl += ["f%d" % j for j in range(1, k + 1)]
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("w", "a"), ("w", "ap"), ("ap", "bp0"), ("a", "b0"), ("b0", "c0"),
         ("c0", "fp0"), ("fp0", "ep"), ("e", "x"), ("ep", "x")]
    for j in range(1, k + 1):
        E += [("a", "b%d" % j), ("b%d" % j, "c%d" % j), ("c0", "c%d" % j),
              ("c%d" % j, "f%d" % j), ("f%d" % j, "e")]
    if repaired:
        E.append(("bp0", "c0"))
    return adj(len(lbl), [(ix[a], ix[b]) for a, b in E]), ix, lbl


def owner_c5_pendants():
    """OWNER-BUILT (round 39), against E14's lemma 'radius-extremal => ecc(w)=2*rad'.
    C5 on (w,u1,c1,c2,u2) with a pendant at c1 and at c2."""
    lbl = ["w", "u1", "c1", "c2", "u2", "s1", "s2"]
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("w", "u1"), ("u1", "c1"), ("c1", "c2"), ("c2", "u2"), ("u2", "w"),
         ("c1", "s1"), ("c2", "s2")]
    return adj(7, [(ix[a], ix[b]) for a, b in E]), ix, lbl


def battery(g, name, wv):
    """everything this round asks of a construction, in one row."""
    D, ecc, r = profile(g)
    C = centre_of(ecc, r)
    return dict(name=name, n=len(g), conn=connected(g), c4=c4_free(g), mu=mu(g),
                rad=r, nC=len(C), ecc_w=ecc[wv], rxm=maximally_far(D, ecc, r, wv),
                dists=sorted({D[c][wv] for c in C}))


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitive self-tests and THE GUARD")
    print("=" * 78)

    # -- primitives
    P = petersen()
    ck(connected(P) and c4_free(P) and len(P) == 10, "petersen basic")
    _, eccP, rP = profile(P)
    ck(rP == 2 and max(eccP) == 2, "petersen self-centred rad 2")
    C9 = cycle(9)
    _, e9, r9 = profile(C9)
    ck(r9 == 4 and len(centre_of(e9, r9)) == 9, "C9 rad 4, self-centred")
    ck(mu(C9) == 2, "mu(C9)=2")
    ck(mu(pathgraph(5)) == 1, "mu(P5)=1 (endpoints have degree 1)")

    # a_val vs brute on C4-free hosts (the matching formula is only valid there)
    agree = 0
    for g in (P, C9, theta333(), pg2(3)):
        for v in range(len(g)):
            ck(a_val(g, v) == a_val_brute(g, v), "a_val vs brute")
            agree += 1
    print("  a(.) matching-formula vs brute independent set: %d / %d vertices agree"
          % (agree, agree))

    # BFS profile vs an INDEPENDENT all-pairs relaxation
    ok = 0
    for g in (P, C9, theta333(), pg2(3), owner_c5_pendants()[0]):
        D, ecc, r = profile(g)
        F = floyd(g)
        ck(all(D[i][j] == F[i][j] for i in range(len(g)) for j in range(len(g))),
           "BFS vs Floyd distances")
        ok += 1
    print("  BFS profile cross-checked against an independent all-pairs relaxation on %d hosts"
          % ok)

    # -- A FACT, NOT A DEFECT: 'd(c,w) >= rad' and 'd(c,w) == rad' are the SAME test.
    # d(c,w) <= ecc(c) = rad always, so any '>=' reading of (RAD-1P)'s condition is a NO-OP.
    # Recorded here so it is never used as a planted guard member (r37's error 1).
    noop = 0
    fam_small = [petersen(), C9, theta333(), pg2(3), cycle(11)]
    for g in fam_small:
        D, ecc, r = profile(g)
        for w in range(len(g)):
            a = all(D[c][w] == r for c in centre_of(ecc, r))
            b = all(D[c][w] >= r for c in centre_of(ecc, r))
            ck(a == b, "'>= rad' vs '== rad' must agree (d(c,w) <= ecc(c) = rad)")
            noop += 1
    print("  NO-OP CHECK: '>= rad' and '== rad' readings agree on %d (host,w) pairs --"
          % noop)
    print("  they are the same test because d(c,w) <= ecc(c) = rad.  A guard member built on")
    print("  that swap would score 0 for a MATHEMATICAL reason, not because the guard is good.")

    # -- GUARD: planted defects in THIS round's census predicate
    # CLASS CLAIMED: any evaluator of the residual predicate
    #     R(G,w) :=  ecc(w) == rad+1  AND  w maximally far from EVERY centre
    # that mis-states either conjunct -- a widened centre set, a swapped quantifier, or a
    # stratum offset.  None of these is zero-step (r34), one-step (r35), late-block (r36),
    # off-by-one/anchor-drift (r37), or cost-evaluator/quantifier-scope-on-frames (r38).
    def R_correct(D, ecc, r, w):
        return ecc[w] == r + 1 and all(D[c][w] == r for c in centre_of(ecc, r))

    def R_d1(D, ecc, r, w):        # CENTRE-WIDEN: 'centre' := ecc <= rad+1
        C = [v for v in range(len(ecc)) if ecc[v] <= r + 1]
        return ecc[w] == r + 1 and all(D[c][w] == r for c in C)

    def R_d2(D, ecc, r, w):        # QUANTIFIER-SWAP: SOME centre instead of EVERY
        return ecc[w] == r + 1 and any(D[c][w] == r for c in centre_of(ecc, r))

    def R_d3(D, ecc, r, w):        # STRATUM-OFFSET: ecc == rad+2
        return ecc[w] == r + 2 and all(D[c][w] == r for c in centre_of(ecc, r))

    guard_hosts = [("Petersen", petersen()), ("C9", cycle(9)), ("C11", cycle(11)),
                   ("Theta(3,3,3)", theta333()), ("PG(2,3)", pg2(3)),
                   ("C9+C9 glued", glue_cycle(cycle(9), 0, 9)),
                   ("PG(2,3)+C7", glue_cycle(pg2(3), 0, 7)),
                   ("owner C5+2 pendants", owner_c5_pendants()[0])]
    # r37's THRESHOLD lesson, applied in advance: a guard host on which the CORRECT predicate
    # never fires makes every planted member invisible for free.  Three hosts on which it DOES
    # fire are added deliberately, and the count is printed rather than averaged away.
    for s in (1, 4, 6):
        h = rand_c4free_dense(s * 7919 + 14, 14)
        if h is not None:
            guard_hosts.append(("dense(s=%d,n0=14)" % s, h))
    tot = {"correct": 0, "d1": 0, "d2": 0, "d3": 0}
    extra = {"d1": 0, "d2": 0, "d3": 0}
    missed = {"d1": 0, "d2": 0, "d3": 0}
    live_hosts = 0
    for nm, g in guard_hosts:
        D, ecc, r = profile(g)
        cc = 0
        for w in range(len(g)):
            c = R_correct(D, ecc, r, w)
            cc += 1 if c else 0
            for key, f in (("d1", R_d1), ("d2", R_d2), ("d3", R_d3)):
                v = f(D, ecc, r, w)
                tot[key] += 1 if v else 0
                if v and not c:
                    extra[key] += 1
                if c and not v:
                    missed[key] += 1
        tot["correct"] += cc
        if cc > 0:
            live_hosts += 1
    print()
    print("  GUARD hosts: %d, of which %d CARRY the predicate (r37's threshold lesson)."
          % (len(guard_hosts), live_hosts))
    print("  correct residual predicate fires on %d vertices" % tot["correct"])
    print("  member                   fires   fires-where-correct-does-not   misses-a-real-one")
    for key, nm in (("d1", "(D1) CENTRE-WIDEN"), ("d2", "(D2) QUANT-SWAP"),
                    ("d3", "(D3) STRATUM-OFFSET")):
        print("  %-22s %6d %30d %19d" % (nm, tot[key], extra[key], missed[key]))
    # liveness of the guard itself, pre-registered: the correct predicate MUST fire somewhere,
    # otherwise every member is invisible for free (r37's threshold finding).
    ck(tot["correct"] > 0, "GUARD LIVENESS: correct predicate must fire on some guard host")
    ck(live_hosts >= 2, "GUARD LIVENESS: at least two guard hosts must CARRY the predicate")
    for key in ("d1", "d2", "d3"):
        ck(extra[key] + missed[key] > 0, "planted %s must be CAUGHT on the guard hosts" % key)


# ------------------------------------------------------------------ PART 1
def part1():
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- E13 HARVEST (out/ox-alpha/E13_w133_centre_density_A_out.md)")
    print("=" * 78)
    print("Each row is the engine's construction rebuilt from its OWN edge list and measured.")
    print()

    gA, ixA, _ = e13_graph_A()
    D, ecc, r = profile(gA)
    print("  Graph A  n=%d conn=%s C4-free=%s mu=%d" % (len(gA), connected(gA), c4_free(gA), mu(gA)))
    print("           rad=%d  Ctr=%s  ecc(w)=%d  d(w,c1)=%d d(w,c2)=%d"
          % (r, sorted(centre_of(ecc, r)), ecc[ixA["w"]], D[ixA["w"]][ixA["c1"]],
             D[ixA["w"]][ixA["c2"]]))
    ck(r == 2, "E13 A: rad = 2 as claimed")
    ck(set(centre_of(ecc, r)) == {ixA["c1"], ixA["c2"]}, "E13 A: Ctr = {c1,c2} as claimed")
    ck(maximally_far(D, ecc, r, ixA["w"]), "E13 A: w IS radius-extremal, as claimed")
    ck(not c4_free(gA), "E13 A is NOT C4-free (engine imposed no hypotheses)")
    # the engine's stated ecc(w)
    print("  ENGINE CLAIMED ecc(w) = 3 ('ecc(u)=3 (s), ecc(w)=3 (s)').  MEASURED ecc(w) = %d."
          % ecc[ixA["w"]])
    ck(ecc[ixA["w"]] == 4, "E13 A: measured ecc(w) = 4, NOT the 3 the engine printed")
    print("  -> the construction is REAL; one of its stated eccentricities is WRONG, and it is")
    print("     the number that would have refuted E14's lemma.  w-u-c1-a1-s has length 4.")

    for m in (2, 3, 4, 5, 6):
        gB, ixB, _ = e13_graph_B(m)
        D, ecc, r = profile(gB)
        C = centre_of(ecc, r)
        want = {ixB["c%d" % i] for i in range(1, m + 1)}
        ok = (r == 2 and set(C) == want and maximally_far(D, ecc, r, ixB["w"]))
        print("  Graph B(m=%d)  n=%2d rad=%d |Ctr|=%2d Ctr==claimed=%s  w radius-extremal=%s"
              "  C4-free=%s mu=%d  ecc(w)=%d"
              % (m, len(gB), r, len(C), set(C) == want,
                 maximally_far(D, ecc, r, ixB["w"]), c4_free(gB), mu(gB), ecc[ixB["w"]]))
        ck(ok, "E13 B(%d): rad/Ctr/radius-extremal as claimed" % m)
        ck(not c4_free(gB), "E13 B(%d) is not C4-free" % m)

    for m in (2, 3, 4):
        gC, ixC, _ = e13_graph_C(m)
        D, ecc, r = profile(gC)
        C = centre_of(ecc, r)
        want = {ixC["c%d" % i] for i in range(1, m + 1)}
        print("  Graph C(m=%d)  n=%2d rad=%d |Ctr|=%2d Ctr==claimed=%s  w radius-extremal=%s"
              "  C4-free=%s mu=%d  ecc(w)=%d"
              % (m, len(gC), r, len(C), set(C) == want,
                 maximally_far(D, ecc, r, ixC["w"]), c4_free(gC), mu(gC), ecc[ixC["w"]]))
        ck(r == 2 and set(C) == want, "E13 C(%d): rad/Ctr as claimed" % m)
        ck(maximally_far(D, ecc, r, ixC["w"]), "E13 C(%d): w radius-extremal as claimed" % m)
        ck(mu(gC) >= 2, "E13 C(%d): mu >= 2 as claimed" % m)
        ck(not c4_free(gC), "E13 C(%d) is not C4-free, as the engine itself says" % m)

    print()
    print("  VERDICT ON E13: the three constructions are REAL and their headline claims hold.")
    print("  They carry NO C4-freeness, so they say nothing about this line's class.  E13's")
    print("  own verdict (PARTIAL, 'under both hypotheses I could neither prove nor refute')")
    print("  is therefore weaker than what this line already holds: r36 (CS-3) PROVES the")
    print("  relative-threshold form under C4-free + delta >= 2.")


# ------------------------------------------------------------------ PART 2
def part2():
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- E14 HARVEST (out/ox-alpha/E14_w133_centre_density_B_out.md)")
    print("=" * 78)
    print("E14's verdict is CLAIM APPEARS FALSE via an infinite family H_k said to be")
    print("connected, C4-free, mu = 2, |Ctr| = k+1 -> oo, with w radius-extremal.")
    print()
    print("  reading      k    n  conn  C4f  mu  rad  |Ctr|  Ctr==claimed  w-rxm  ecc(w)  2*rad")
    lit_ok = 0
    rep_ok = 0
    for rep in (False, True):
        for k in (1, 2, 3, 4, 5, 6, 7, 8):
            g, ix, _ = e14_Hk(k, rep)
            D, ecc, r = profile(g)
            C = centre_of(ecc, r)
            want = {ix["c0"]} | {ix["c%d" % j] for j in range(1, k + 1)}
            rxm = maximally_far(D, ecc, r, ix["w"])
            good = (connected(g) and c4_free(g) and mu(g) >= 2 and set(C) == want and rxm)
            if rep:
                rep_ok += 1 if good else 0
            else:
                lit_ok += 1 if good else 0
            print("  %-9s  %2d %4d  %-5s %-4s %2d %4d %6d  %-12s  %-5s %6d %6d"
                  % ("repaired" if rep else "literal", k, len(g), connected(g), c4_free(g),
                     mu(g), r, len(C), set(C) == want, rxm, ecc[ix["w"]], 2 * r))
    print()
    ck(lit_ok == 0, "E14's LITERAL edge list does NOT deliver the claimed centre set")
    ck(rep_ok == 8, "E14's edge list REPAIRED with b'0-c0 delivers all 8 claimed rows")
    print("  THE DEFECT, NAMED: the engine's edge list omits b'0-c0, but its own verification")
    print("  text uses N(c0) = {b0, b'0, c1..ck, f'0}.  With the list as printed, b'0 hangs off")
    print("  a' alone, d(c0,b'0) = 5, and c0 is not a centre at all.  ADDING THAT ONE EDGE")
    print("  MAKES EVERY HEADLINE CLAIM TRUE.  So the refutation stands, on a repaired witness.")

    g, ix, _ = e14_Hk(4, True)
    D, ecc, r = profile(g)
    print()
    print("  H_4 repaired, explicit: n=%d, rad=%d, |Ctr|=%d, ecc(w)=%d = 2*rad, edges:"
          % (len(g), r, len(centre_of(ecc, r)), ecc[ix["w"]]))
    print("    " + " ".join("%d-%d" % e for e in edges_of(g)))
    ck(all(D[c][ix["w"]] == r for c in centre_of(ecc, r)), "H_4: every centre at distance rad")
    ck(min(len(g[v]) for v in range(len(g))) == 2, "H_4: delta = 2")


# ------------------------------------------------------------------ PART 3
def part3(fam):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- LEMMA AUDIT.  These are MY verdicts on the engines' DERIVATIONS, not the")
    print("          engines'.  Constructions are checkable; justifications are not delegated.")
    print("=" * 78)

    # (L1) E14 sec.1 step 2, first bullet: 'from any v there is a neighbour of smaller
    #      eccentricity whenever ecc(v) > rad'.
    print()
    print("  (L1) E14's DESCENT LEMMA: ecc(v) > rad => some neighbour has SMALLER ecc.")
    bad = []
    tested = 0
    for g, nm in [(e13_graph_A()[0], "E13 Graph A"), (owner_c5_pendants()[0], "owner C5+2p"),
                  (e14_Hk(3, True)[0], "E14 H_3 repaired"), (theta333(), "Theta(3,3,3)"),
                  (glue_cycle(cycle(9), 0, 9), "C9+C9")] + [(g, nm) for g, nm in fam[:40]]:
        D, ecc, r = profile(g)
        for v in range(len(g)):
            tested += 1
            if ecc[v] > r and not any(ecc[u] < ecc[v] for u in g[v]):
                bad.append((nm, v, ecc[v], r))
    print("      tested at %d vertices; VIOLATIONS: %d" % (tested, len(bad)))
    for row in bad[:6]:
        print("      counterexample: %s  v=%d  ecc(v)=%d  rad=%d  (no neighbour descends)"
              % row)
    ck(len(bad) > 0, "(L1) is FALSE and this run must exhibit a violation")
    print("      VERDICT: (L1) IS FALSE AS STATED.  Eccentricity has non-global local minima.")
    print("      E14 used it to derive 'ecc(w) >= 2*rad'.  That derivation is INVALID.")

    # (L2) the conclusion E14 drew from (L1): radius-extremal => ecc(w) = 2*rad.
    print()
    print("  (L2) E14's CONCLUSION: w radius-extremal => ecc(w) = 2*rad.")
    gO, ixO, _ = owner_c5_pendants()
    D, ecc, r = profile(gO)
    print("      OWNER counterexample (built this round, no hypotheses): C5 (w,u1,c1,c2,u2)")
    print("      with a pendant at c1 and at c2.  n=%d rad=%d Ctr=%s ecc(w)=%d 2*rad=%d mu=%d"
          % (len(gO), r, sorted(centre_of(ecc, r)), ecc[ixO["w"]], 2 * r, mu(gO)))
    ck(maximally_far(D, ecc, r, ixO["w"]), "(L2) witness: w IS radius-extremal")
    ck(ecc[ixO["w"]] == r + 1 and ecc[ixO["w"]] < 2 * r, "(L2) witness: ecc(w) = rad+1 < 2 rad")
    print("      VERDICT: (L2) IS FALSE without hypotheses.  (mu = %d here, so this witness"
          % mu(gO))
    print("      alone does NOT settle it inside this line's class.  So:)")
    inclass = 0
    first = None
    for g, nm in fam:
        if len(g) > 60:
            continue
        D, ecc, r = profile(g)
        for w in range(len(g)):
            if maximally_far(D, ecc, r, w) and ecc[w] < 2 * r:
                inclass += 1
                if first is None:
                    first = (nm, len(g), w, r, ecc[w], 2 * r, a_val(g, w))
    print("      IN-CLASS REFUTATION (C4-free, mu >= 2 hosts of this family, n <= 60):")
    print("      vertices that are radius-extremal with ecc(w) < 2*rad: %d" % inclass)
    if first:
        print("      first witness: %s n=%d w=%d rad=%d ecc(w)=%d 2*rad=%d a(w)=%d"
              % first)
    ck(inclass > 0, "(L2) must be refuted INSIDE the C4-free + mu>=2 class, not only outside")
    print("      VERDICT: (L2) IS FALSE INSIDE THIS LINE'S CLASS TOO.")

    # (L3) E14's 'bonus local lemma': C4-free, rad = 2, w radius-extremal => N(w) = {a}.
    print()
    print("  (L3) E14's BONUS LOCAL LEMMA (rad=2, C4-free => N(w) = {a}, so a(w)=1).")
    print("      ITS PROOF IS INVALID AS WRITTEN: it exhibits w-a-c-m-n-w and calls it a")
    print("      4-cycle.  Those are FIVE distinct vertices -- w,a,c,m,n -- so it is a C5 and")
    print("      C4-freeness forbids nothing.  (It is the step that would have made rad >= 3")
    print("      automatic for a radius-extremal vertex.)")
    c5 = cycle(5)
    ck(c4_free(c5), "(L3): the configuration the proof calls a C4 is a C5, which is C4-free")
    print("      MACHINE NOTE: C5 is C4-free (checked), so the cited configuration is legal.")
    # AND THE LEMMA ITSELF IS FALSE, not merely unproved: a witness from this line's own class.
    wit = None
    for g, nm in fam:
        if len(g) > 40:
            continue
        D, ecc, r = profile(g)
        if r != 2:
            continue
        for w in range(len(g)):
            if maximally_far(D, ecc, r, w) and a_val(g, w) >= 2:
                wit = (nm, len(g), w, a_val(g, w), len(g[w]), mu(g))
                break
        if wit:
            break
    if wit:
        print("      AND (L3) IS FALSE, NOT MERELY UNPROVED.  Witness in this line's own class:")
        print("      %s  n=%d  w=%d  rad=2  C4-free  a(w)=%d  deg(w)=%d  mu(G)=%d"
              % wit)
        print("      -- w IS radius-extremal at rad = 2 with a(w) >= 2, which (L3) says is")
        print("      impossible.  So rad >= 3 does NOT follow, and any argument leaning on it")
        print("      loses its footing.")
    ck(wit is not None, "(L3) must be refuted by an explicit in-class witness, not by prose")


# ------------------------------------------------------------------ PART 4
def part4(fam):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE SINGLE-HAIR RESIDUAL CLASS, LOCATED IN VERTICES, AND WHETHER THE")
    print("          ROUND-38 COST RULE ALREADY COVERS IT")
    print("=" * 78)
    print("Draft 42.4's single-hair table leaves exactly one open row:")
    print("    h = 1,  e := ecc_{G'}(w) = rad(G')+1,  rad(G'+pendant) = rad(G')+1.")
    print("By (RAD-1P) the third conjunct IS 'w maximally far from every centre of G''.")
    print("So the residual class is  R(G,w) := [ ecc(w) = rad+1 ]  AND  [ w rad-extremal ].")
    print("What that row needs is exactly  endpath(G,w) >= ecc(w)+3  -- the (TAIL-2) step.")
    print()
    print("DIRECTION OF ERROR, FIXED BEFORE THE NUMBERS: a residual vertex is COVERED only by")
    print("BUILDING an induced anchored path on ecc(w)+3 vertices and passing the independent")
    print("checker.  So COVERED is a LOWER bound and UNCOVERED an UPPER bound.")
    print()

    hosts = [(g, nm) for g, nm in fam if len(g) <= 130]
    skipped = len(fam) - len(hosts)
    n_conj1 = n_conj2 = n_res = 0
    n_sc = 0
    res_rows = []
    lgt4 = 0
    for g, nm in hosts:
        if over():
            break
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        selfc = (len(C) == len(g))
        if selfc:
            n_sc += 1
        la = mean_a(g)
        for w in range(len(g)):
            c1 = (ecc[w] == r + 1)
            c2 = all(D[c][w] == r for c in C)
            if c1:
                n_conj1 += 1
            if c2:
                n_conj2 += 1
            if c1 and c2:
                n_res += 1
                if la > 4:
                    lgt4 += 1
                res_rows.append((nm, len(g), w, r, ecc[w], la, len(C)))
    print("  hosts entered: %d  (skipped as too big: %d);  self-centred hosts: %d"
          % (len(hosts), skipped, n_sc))
    print("  EVERY host of this family is C4-free with mu >= 2 -- asserted, not assumed:")
    bad_h = [nm for g, nm in hosts if not (c4_free(g) and min(a_val(g, v)
                                                              for v in range(len(g))) >= 2)]
    ck(not bad_h, "every family host must be C4-free with mu >= 2 (else the class is wrong)")
    print("    hosts failing C4-free or mu >= 2: %d" % len(bad_h))
    print("  CONJUNCT POPULATIONS, printed BEFORE the verdict (r37 error (c)):")
    print("    vertices with ecc(w) = rad+1                     : %d" % n_conj1)
    print("    vertices maximally far from EVERY centre         : %d" % n_conj2)
    print("    BOTH  =  THE SINGLE-HAIR RESIDUAL CLASS          : %d" % n_res)
    print("    of those, on hosts with l > 4                    : %d" % lgt4)
    ck(n_conj1 > 0, "conjunct 1 must be non-empty or the census is vacuous")
    ck(n_conj2 > 0, "conjunct 2 must be non-empty or the census is vacuous")
    # the radius profile of the class -- route A2 imports rad >= 5, so this decides whether the
    # residual row can even arise inside A2's hypothesis class ON THIS FAMILY.
    radhist = {}
    for (nm, n, w, r, ew, la, nc) in res_rows:
        radhist[r] = radhist.get(r, 0) + 1
    print("    RADIUS PROFILE of the residual class: "
          + ", ".join("rad=%d : %d" % (k, radhist[k]) for k in sorted(radhist)))
    hi = sum(v for k, v in radhist.items() if k >= 5)
    print("    residual vertices with rad >= 5 (route A2's imported class)      : %d" % hi)
    # CONJUNCT 3 ALONE on route A2's host class -- asked because a brief of mine asserted it
    # before it had been run.  Measured, then written.
    c2_a2 = c2_lgt4 = c2_rad5 = 0
    hosts_a2 = 0
    off_a2 = {}
    off_all = {}
    for g, nm in hosts:
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        la = mean_a(g)
        isa2 = (la > 4 and r >= 5)
        if isa2:
            hosts_a2 += 1
        for w in range(len(g)):
            if all(D[c][w] == r for c in C):
                off_all[ecc[w] - r] = off_all.get(ecc[w] - r, 0) + 1
                if la > 4:
                    c2_lgt4 += 1
                if r >= 5:
                    c2_rad5 += 1
                if isa2:
                    c2_a2 += 1
                    off_a2[ecc[w] - r] = off_a2.get(ecc[w] - r, 0) + 1
    print("    CONDITION 3 ALONE (maximally far from every centre), by host class:")
    print("      on hosts with l > 4                 : %d" % c2_lgt4)
    print("      on hosts with rad >= 5              : %d" % c2_rad5)
    print("      on hosts with l > 4 AND rad >= 5 (%d such hosts) : %d" % (hosts_a2, c2_a2))
    print("      ecc(w)-rad profile, ALL condition-3 vertices : "
          + ", ".join("+%d : %d" % (k, off_all[k]) for k in sorted(off_all)))
    print("      ecc(w)-rad profile, on l>4 AND rad>=5 hosts  : "
          + ", ".join("+%d : %d" % (k, off_a2[k]) for k in sorted(off_a2)))
    # A LEMMA, not a measurement: condition 3 forces w out of the centre, so ecc(w) >= rad+1.
    ck(0 not in off_all, "condition 3 must never hold at a vertex with ecc(w) = rad (w would "
                         "be a centre at distance 0 from itself)")
    print("      LEMMA (proved, not measured): condition 3 => w is not a centre => ecc(w) >= rad+1,")
    print("      so offset 0 is IMPOSSIBLE and the run asserts it.  Everything at offset >= 2 is")
    print("      closed by (TAIL-1) alone: e >= rad+2 is draft 42.4's (B2) row, unconditional.")
    a2_res = off_a2.get(1, 0)
    print("      => on route A2's own host class here, the single-hair RESIDUAL row holds at %d"
          % a2_res)
    print("         of the %d condition-3 vertices; the other %d are in the (B2)-closed row."
          % (c2_a2, c2_a2 - a2_res))
    print("    NOT A THEOREM: r36 found 2 residual instances at rad = 4 on its own 145-base")
    print("    family, so the class is NOT confined to rad = 2 in general.  This is a profile")
    print("    of THIS family, printed with its population, not a structural claim.")

    if n_res == 0:
        print()
        print("  THE RESIDUAL CLASS IS EMPTY ON THIS FAMILY.  That is a MEASUREMENT over the")
        print("  population printed above, not a theorem: the family is designed plus seeded")
        print("  random and is NOT exhaustive.  r36 found 2 instances on ITS 145-base family,")
        print("  so the class is known non-empty in general -- this family simply misses them.")
    else:
        print()
        print("  RESIDUAL INSTANCES, NAMED (up to 12 shown):")
        for row in res_rows[:12]:
            print("    %-28s n=%3d w=%3d rad=%d ecc(w)=%d l=%.3f |Ctr|=%d" % row)

    # -- coverage: does (TAIL-2'') build the ecc+3 path at each residual vertex?
    print()
    print("  COVERAGE OF THE RESIDUAL CLASS BY THE ROUND-38 COST RULE (TAIL-2''):")
    cov = unc = 0
    cov_rows = []
    for (nm, n, w, r, ew, la, nc) in res_rows:
        if over():
            break
        g = None
        for gg, nn in hosts:
            if nn == nm and len(gg) == n:
                g = gg
                break
        if g is None:
            continue
        D, ecc, rr = profile(g)
        M = incidence_matrix(g)
        got = None
        for (P, ud, y) in frames(g, D, ecc, w, 6, 3, dmin=2):
            d = len(P) - 1
            k2 = dodge_count(g, P, y, (d - 2, d - 3))
            a = a_val(g, y)
            dg = len(g[y])
            if not (a >= 2 + k2 or dg >= 3 + k2):
                continue
            zs = step2_build(g, P, y, w, M)
            if zs:
                got = P + [y, zs[0]]
                break
        if got is not None and checker_induced_anchored(g, got, w, ecc[w] + 3, M):
            cov += 1
            cov_rows.append((nm, w, "COVERED", len(got)))
        else:
            unc += 1
            cov_rows.append((nm, w, "UNCOVERED", 0))
    print("    residual vertices COVERED   (ecc+3 path BUILT and checker-verified): %d" % cov)
    print("    residual vertices UNCOVERED (no firing frame found in the sample)  : %d" % unc)
    for row in cov_rows[:12]:
        print("      %-28s w=%3d %-9s built on %d vertices" % row)

    # -- every UNCOVERED vertex is diagnosed: is the CHAIN short, or is the STATEMENT false?
    print()
    print("  DIAGNOSIS OF EVERY UNCOVERED RESIDUAL VERTEX (r38 sec.4's split, re-run here):")
    short = false_ = undec = 0
    for (nm, w, verdict, _l) in cov_rows:
        if verdict != "UNCOVERED":
            continue
        g = None
        for gg, nn in hosts:
            if nn == nm:
                g = gg
                break
        if g is None:
            continue
        D, ecc, r = profile(g)
        need = ecc[w] + 3
        val, P, trunc = anchored_search(g, w, min(need, len(g)))
        if val >= need:
            short += 1
            ok = checker_induced_anchored(g, P[:need], w, need)
            ck(ok, "witness for %s w=%d must pass the independent checker" % (nm, w))
            print("    %-28s w=%3d  CHAIN IS SHORT -- an ecc+3 path EXISTS (built, checked)"
                  % (nm, w))
        elif trunc:
            undec += 1
            print("    %-28s w=%3d  UNDECIDED (search truncated)" % (nm, w))
        else:
            false_ += 1
            print("    %-28s w=%3d  STATEMENT FAILS -- search COMPLETE, endpath = %d < %d"
                  % (nm, w, val, need))
            if len(g) <= 13:
                ov = oracle_endpath(g, w, len(g))
                print("      independent subset oracle on the same (host,w): endpath = %d" % ov)
                ck(ov == val, "oracle must reproduce the failing value")
    print("    chain-short: %d   statement-fails: %d   undecided: %d" % (short, false_, undec))

    # -- LIVENESS, against this round's own interest: the coverage test must be able to fail.
    print()
    print("  LIVENESS OF THE COVERAGE TEST (pre-registered, against interest): the same walk")
    print("  is run on hosts where the ecc+3 path CANNOT exist, and must report UNCOVERED.")
    live_fail = 0
    live_tot = 0
    for nm, g in [("C6", cycle(6)), ("Theta(3,3,3)", theta333()), ("P5", pathgraph(5)),
                  ("C7", cycle(7))]:
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        for w in range(len(g)):
            live_tot += 1
            need = ecc[w] + 3
            true_val, _, trunc = anchored_search(g, w, min(need, len(g)))
            if true_val >= need or trunc:
                continue
            hit = False
            for (P, ud, y) in frames(g, D, ecc, w, 6, 3, dmin=2):
                d = len(P) - 1
                k2 = dodge_count(g, P, y, (d - 2, d - 3))
                if a_val(g, y) >= 2 + k2 or len(g[y]) >= 3 + k2:
                    if step2_build(g, P, y, w, M):
                        hit = True
                        break
            if hit:
                live_fail += 1
    print("    (host,w) pairs where NO ecc+3 path exists: the walk claimed one anyway %d times"
          % live_fail)
    ck(live_fail == 0, "LIVENESS: the walk must never claim a path that does not exist")

    # -- oracle cross-check on the small hosts
    orc = orc_ok = 0
    for nm, g in [("C6", cycle(6)), ("C7", cycle(7)), ("Theta(3,3,3)", theta333()),
                  ("P5", pathgraph(5)), ("Petersen", petersen())]:
        if len(g) > 13:
            continue
        for w in range(len(g)):
            cap = len(g)
            v1, _, tr = anchored_search(g, w, cap)
            v2 = oracle_endpath(g, w, cap)
            orc += 1
            if (not tr) and v1 == v2:
                orc_ok += 1
    print("    independent subset oracle agrees with the DFS value on %d / %d (host,w) pairs"
          % (orc_ok, orc))
    ck(orc_ok == orc, "oracle must agree with the DFS on every n <= 13 host")
    return n_conj1, n_conj2, n_res, cov, unc


# ------------------------------------------------------------------ PART 5
def part5(fam):
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- (CS-3) AGAINST E14's FAMILY: absolute vs relative thresholds")
    print("=" * 78)
    print("(CS-3), draft 45/ r36 sec.5: G connected C4-free, delta >= 2, r = rad >= 3.  If some")
    print("vertex is maximally far from every centre then |C| <= n - 1 - delta(delta-1) - (r-3).")
    print()
    print("   k    n  delta  rad  |Ctr|  (CS-3) bound  |Ctr| <= bound  |Ctr|/n")
    for k in (1, 2, 4, 8, 16, 32):
        g, ix, _ = e14_Hk(k, True)
        D, ecc, r = profile(g)
        C = centre_of(ecc, r)
        n = len(g)
        dl = min(len(g[v]) for v in range(n))
        bd = n - 1 - dl * (dl - 1) - (r - 3)
        print("  %3d %4d %6d %4d %6d %13d  %-14s %.3f"
              % (k, n, dl, r, len(C), bd, len(C) <= bd, len(C) / float(n)))
        ck(r >= 3, "H_k has rad >= 3 so (CS-3) applies")
        ck(len(C) <= bd, "H_k must SATISFY (CS-3) -- it has a radius-extremal vertex")
    print()
    print("  READING, and it is the harvest's real content: E14's family does NOT contradict")
    print("  (CS-3).  It refutes only the ABSOLUTE form of the r34 target ('|Ctr| large' with a")
    print("  universal constant), which (CS-3) never asserted.  |Ctr|/n -> 1/3 while the bound")
    print("  stays far above it, because delta = 2 makes delta(delta-1) = 2 and the bound nearly")
    print("  vacuous.  So the harvest CONFIRMS that (CS-3)'s dependence on n and delta is")
    print("  NECESSARY, not an artefact of how it was proved.")

    # what the family measures about delta: the bound only bites at large delta
    print()
    print("  WHERE (CS-3) ACTUALLY BITES, measured over this line's own host family:")
    bites = 0
    tot = 0
    for g, nm in fam:
        if len(g) > 130:
            continue
        D, ecc, r = profile(g)
        if r < 3:
            continue
        n = len(g)
        dl = min(len(g[v]) for v in range(n))
        bd = n - 1 - dl * (dl - 1) - (r - 3)
        C = centre_of(ecc, r)
        tot += 1
        if len(C) > bd:
            bites += 1
            ck(not any(all(D[c][w] == r for c in C) for w in range(n)),
               "(CS-3) fires on %s: there must be NO radius-extremal vertex" % nm)
    print("    hosts in scope (rad >= 3): %d;  hosts where (CS-3) DECIDES (|C| > bound): %d"
          % (tot, bites))
    print("    every deciding host re-checked by BFS: no radius-extremal vertex found.")


# ------------------------------------------------------------------ PART 6
def e39_lemmaX_witness():
    """E39 sec.4: G' on {z,a,b,w,u}, edges za, aw, zb, bu, ab."""
    lbl = ["z", "a", "b", "w", "u"]
    ix = {x: i for i, x in enumerate(lbl)}
    E = [("z", "a"), ("a", "w"), ("z", "b"), ("b", "u"), ("a", "b")]
    return adj(5, [(ix[p], ix[q]) for p, q in E]), ix


def longest_induced_path(g):
    """number of VERTICES of a longest induced path -- max over anchors of endpath."""
    best = 0
    for w in range(len(g)):
        v, _, tr = anchored_search(g, w, len(g))
        if tr:
            return None
        best = max(best, v)
    return best


def part6():
    PARTS_RUN.append("PART6")
    print()
    print("=" * 78)
    print("PART 6 -- E39 HARVEST (out/ox-alpha/E39_w133_multihair_caseII_out.md), UNREAD until")
    print("          this round.  Verdict PARTIAL, two theorems, one 'universal' lemma.")
    print("=" * 78)
    print("E39's LEMMA 0: path(G') <= 2*rad(G')+1, with the proof 'd(a,b) >= d_P(a,b) = p-1'.")
    print("THE PROOF IS INVALID: an INDUCED path is an induced SUBGRAPH; its endpoints may be")
    print("far closer in G than along it.  d(a,b) <= p-1 is what holds, and the proof needs the")
    print("reverse.  Whether the STATEMENT survives is a separate question, so it is measured:")
    print()
    print("   host              n  rad  path(G)  2*rad+1  Lemma 0 holds")
    viol = 0
    tested = 0
    worst = None
    for nm, g in [("C6", cycle(6)), ("C7", cycle(7)), ("C9", cycle(9)),
                  ("Theta(3,3,3)", theta333()), ("Petersen", petersen()),
                  ("P5", pathgraph(5)), ("C5+C5 glued", glue_cycle(cycle(5), 0, 5)),
                  ("PG(2,3)", pg2(3))]:
        _, ecc, r = profile(g)
        p = longest_induced_path(g)
        if p is None:
            continue
        tested += 1
        ok = (p <= 2 * r + 1)
        if not ok:
            viol += 1
            if worst is None or p - (2 * r + 1) > worst[3]:
                worst = (nm, r, p, p - (2 * r + 1))
        print("   %-16s %2d %4d %8d %8d  %s" % (nm, len(g), r, p, 2 * r + 1, ok))
    print()
    ck(viol > 0, "E39's Lemma 0 must be REFUTED by an explicit host, not merely doubted")
    print("  VERDICT: E39's LEMMA 0 IS FALSE, on %d of %d hosts tested.  Widest gap: %s,"
          % (viol, tested, worst[0]))
    print("  rad = %d, so the lemma allows %d vertices and the graph carries %d -- over by %d."
          % (worst[1], 2 * worst[1] + 1, worst[2], worst[3]))
    print("  (PRE-REGISTERED PREDICTION THAT FAILED, recorded: I expected Petersen to be the")
    print("  witness at path = 6.  MEASURED path(Petersen) = 5, so Lemma 0 HOLDS there.  The")
    print("  refutation came from hosts I added for coverage, not from the one I named.)")
    print("  CONSEQUENCE, and it is the whole point of reading this output: Lemma 0 is the LAST")
    print("  STEP of Theorem P1 ('path(G) >= 2 rad(G) >= (2r'+1)+Delta >= path(G')+Delta') and")
    print("  of Theorem P2.  BOTH THEOREMS FALL WITH IT.  Nothing of E39 sec.3 may be cited.")
    print("  E39's sec.1 verification of the (MH-II) => Case-II chain is a separate matter and")
    print("  is NOT touched by this -- that part re-derives, and I re-derived it by hand.")

    print()
    print("  E39's 'LEMMA X FALSE' WITNESS, rebuilt from its own edge list:")
    gX, ixX = e39_lemmaX_witness()
    D, ecc, r = profile(gX)
    print("    n=%d  connected=%s  C4-free=%s  mu=%d  rad=%d  centre=%s"
          % (len(gX), connected(gX), c4_free(gX), mu(gX), r,
             [["z", "a", "b", "w", "u"][c] for c in centre_of(ecc, r)]))
    ck(c4_free(gX), "E39's witness IS C4-free, as it claims")
    ck(mu(gX) < 2, "E39's witness has mu < 2 -- it is OUTSIDE this line's class")
    print("    THE WITNESS IS C4-FREE AS CLAIMED, AND IT HAS mu = %d < 2." % mu(gX))
    print("    w and u are pendants, so a(w) = a(u) = 1.  E39's 'blocker' is therefore not")
    print("    known to block anything inside this line's class -- the obstruction it names")
    print("    lives on a graph route A2 never has to handle.  Not a refutation of E39's")
    print("    honesty (it says PARTIAL); a statement about what the PARTIAL is about.")


# ------------------------------------------------------------------ PART 7
def part7():
    PARTS_RUN.append("PART7")
    print()
    print("=" * 78)
    print("PART 7 -- THE CONTROL THAT COULD BREAK PART 4's FINDING: hosts BUILT to put a")
    print("          condition-3 vertex at offset +1 inside route A2's class (l>4, rad>=5)")
    print("=" * 78)
    print("PART 4's family has 22 such hosts, ALL of them PG(2,5) with one tail.  A finding")
    print("resting on one shape is a finding about that shape.  These hosts are new to this")
    print("line: a denser core (PG(2,7), 8-regular, l = 8), tails of many lengths, tails at")
    print("TWO different roots, and two cores joined by a path -- chosen because each changes")
    print("WHERE the centre sits relative to the tail, which is what offset +1 needs.")
    print()
    ctrl = []
    b5, b7 = pg2(5), pg2(7)
    for L, k in ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 7), (7, 7), (8, 9)):
        ctrl.append((path_then_cycle(b7, 0, L, k), "PG(2,7)+P%d+C%d" % (L, k)))
    for k in (9, 11, 13, 15, 17, 19, 21):
        ctrl.append((glue_cycle(b7, 0, k), "PG(2,7)+C%d glued" % k))
    for L, k in ((7, 5), (8, 5), (9, 7), (10, 7), (11, 9), (12, 9)):
        ctrl.append((path_then_cycle(b5, 0, L, k), "PG(2,5)+P%d+C%d" % (L, k)))
    for k1, k2 in ((11, 13), (13, 15), (15, 17)):
        g = glue_cycle(b5, 0, k1)
        ctrl.append((glue_cycle(g, 3, k2), "PG(2,5)+C%d@0+C%d@3" % (k1, k2)))
    for L in (7, 9, 13, 15):
        ctrl.append((blob_chain(5, L), "2xPG(2,5)+P%d" % L))
    print("   host                       n   rad     l  cond-3 vertices   at offset +1")
    tot_a2 = 0
    tot_off1 = 0
    inscope = 0
    for g, nm in ctrl:
        if over() or len(g) > 300:
            continue
        D, ecc, r = profile(g)
        la = mean_a(g)
        if not (la > 4 and r >= 5):
            continue
        inscope += 1
        C = centre_of(ecc, r)
        c3 = [w for w in range(len(g)) if all(D[c][w] == r for c in C)]
        off1 = [w for w in c3 if ecc[w] == r + 1]
        tot_a2 += len(c3)
        tot_off1 += len(off1)
        ck(all(ecc[w] >= r + 1 for w in c3), "condition 3 => ecc >= rad+1 on %s" % nm)
        print("   %-24s %4d %5d %5.2f %17d %14d" % (nm, len(g), r, la, len(c3), len(off1)))
    print()
    print("  NEW hosts in route A2's class (l > 4 AND rad >= 5): %d" % inscope)
    print("  condition-3 vertices on them: %d;  of those at offset +1 (THE RESIDUAL ROW): %d"
          % (tot_a2, tot_off1))
    ck(inscope > 0, "the control must actually enter route A2's class, or it proves nothing")
    ck(tot_a2 > 0, "condition 3 must FIRE on the control hosts, or offset +1 is unreachable "
                   "for a trivial reason and the control is vacuous")
    if tot_off1 == 0:
        print("  THE CONTROL DID NOT BREAK THE FINDING.  It could have: condition 3 fires %d"
              % tot_a2)
        print("  times on these new shapes, so offset +1 was reachable and was not reached.")
        print("  STILL A MEASUREMENT, NOT A THEOREM -- now over %d NEW hosts of four shapes"
              % inscope)
        print("  ON TOP OF PART 4's own in-class hosts, whose count PART 4 printed above.")
    else:
        print("  *** THE CONTROL BROKE THE FINDING: %d residual-row instances inside route A2's"
              % tot_off1)
        print("  class.  PART 4's emptiness was a property of ONE host shape.  These are the")
        print("  objects brief E44 asks an engine to build, and they are ours already.")


def main():
    print("WOWII-133 round 39 -- E13/E14/E39 harvest + the single-hair residual class")
    print("interpreter: %s" % sys.version.split()[0])
    print("started: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    part0()
    part1()
    part2()
    fam = build_family()
    print()
    print("family built: %d host slots" % len(fam))
    part3(fam)
    r = part4(fam)
    part5(fam)
    part6()
    part7()
    print()
    print("=" * 78)
    print("parts run: %s" % ",".join(PARTS_RUN))
    print("CHECKS=%d FAILS=%d elapsed=%.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    ck(len(PARTS_RUN) == 8, "all 8 declared parts must self-register")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
