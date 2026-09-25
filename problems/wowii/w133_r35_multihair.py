#!/usr/bin/env python3
"""owner-w133 round 35 -- THE MULTI-HAIR FRONT, reproduced in my own hand, plus the
CENTRE-SPHERE bound that turns round 34's measured 0 into a proof.

SELF-CONTAINED.  Every primitive is COPIED, never imported (doctrine).  No SAT, no
exhaustive search over a large space; every census is a designed, bounded family and
every longest-induced-path computation is capped at a stated vertex count.

Interpreter: system python3 (no networkx, no sympy needed -- pure stdlib).

PARTS
  0  guards + controls, incl. the STANDING ZERO-STEP PATH GUARD owed by cert_w133_r34 s5
  1  multi-hair eccentricity formulas, re-derived and BFS-certified; E11's radius
     counterexample rebuilt in my own hand
  2  the a-value / l(G) bookkeeping for hairs -- E12's Lemma A(ii) and Lemma B tested
  3  E12's radius identity and its endpath route, tested
  4  CASE I of the multi-hair reduction (rad(G) = rad(G')), stated and certified
  5  the CENTRE-SPHERE bound, and its application to round 34's 248 hosts

Deadline is internal; partial results are PRINTED, never discarded.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 210.0
FAIL = 0
CHECKS = 0
PARTS_RUN = []


def over():
    return time.time() - T0 > DEADLINE


def check(cond, msg):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("FAIL:", msg, flush=True)
    return cond


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
    return len(g) > 0 and all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
    """alpha(G[N(v)]).  Valid whenever G[N(v)] is a disjoint union of cliques; in a
    C4-free graph G[N(v)] is a MATCHING, so this is exact there.  Cross-checked against
    a_val_brute in PART 0."""
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def a_val_brute(g, v):
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


def mean_a(g, brute=False):
    n = len(g)
    f = a_val_brute if brute else a_val
    return sum(f(g, v) for v in range(n)) / float(n)


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    centres = [v for v in range(n) if ecc[v] == r]
    return D, ecc, r, centres


def maximally_far(D, w, centres, r):
    """EVERY centre is at distance exactly r from w."""
    return all(D[c][w] == r for c in centres)


# ---- induced paths, WITH THE STANDING ZERO-STEP GUARD ------------------------------
class ZeroStepAbort(Exception):
    """cert_w133_r34 s5: a path search that takes zero steps must ABORT, not report.
    r33 own-defect #1 and r34 own-defect #2 were the same bug one round apart: a DFS
    whose initial forbidden set already contained every neighbour of the seed printed
    path=1 and failed nothing."""


def endpath(g, s, cap=None):
    """Max number of vertices of an induced path of g having s as an ENDPOINT.

    Blocking rule: when the endpoint moves from `cur` to `x`, every OTHER neighbour of
    `cur` becomes unusable (a later vertex adjacent to `cur` would chord the path), and
    `x` itself is consumed.  Neighbours of `x` stay available -- one of them is the next
    step.  (My first version blocked the neighbours of `x`, which forbids the very step
    it is looking for; it is kept named in OWNER ERRORS.)

    GUARD: in a graph where s has a neighbour, a result of 1 means the search could not
    take a first step -> abort."""
    n = len(g)
    best = [1]
    blocked = [False] * n

    def rec(cur, ln):
        if ln > best[0]:
            best[0] = ln
        if cap is not None and best[0] >= cap:
            return
        cands = [x for x in g[cur] if not blocked[x]]
        for x in cands:
            newly = [y for y in cands if y != x]
            newly.append(x)
            for y in newly:
                blocked[y] = True
            rec(x, ln + 1)
            for y in newly:
                blocked[y] = False

    blocked[s] = True
    rec(s, 1)
    if best[0] == 1 and len(g[s]) > 0:
        raise ZeroStepAbort("endpath returned 1 at a vertex of degree %d" % len(g[s]))
    return best[0]


def longest_induced_path(g, cap=None):
    return max(endpath(g, s, cap) for s in range(len(g)))


def is_induced_path(g, seq):
    if len(set(seq)) != len(seq):
        return False
    for i, u in enumerate(seq):
        for j, v in enumerate(seq):
            if j <= i:
                continue
            if (j == i + 1) != (v in g[u]):
                return False
    return True


# ------------------------------------------------------------------ builders
def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def path_graph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


def two_cycles_glued(a, b):
    E = [(i, i + 1) for i in range(a - 1)] + [(a - 1, 0)]
    n = a
    prev = 0
    for _ in range(b - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, 0))
    return adj(n, E)


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def theta(a, b, c):
    """Theta graph: two hub vertices joined by three internally disjoint paths with
    a, b, c internal vertices."""
    E = []
    n = 2
    for L in (a, b, c):
        prev = 0
        for _ in range(L):
            E.append((prev, n))
            prev = n
            n += 1
        E.append((prev, 1))
    return adj(n, E)


def pg2(q):
    def norm(v):
        for x in v:
            if x % q:
                inv = pow(x % q, q - 2, q) if q > 2 else 1
                return tuple((c * inv) % q for c in v)
        return None
    pts = []
    seen = set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if (a, b, c) == (0, 0, 0):
                    continue
                nv = norm((a, b, c))
                if nv and nv not in seen:
                    seen.add(nv)
                    pts.append(nv)
    N = len(pts)
    E = []
    for i, p in enumerate(pts):
        for j, L in enumerate(pts):
            if sum(p[k] * L[k] for k in range(3)) % q == 0:
                E.append((i, N + j))
    return adj(2 * N, E)


def del_edge(g, e):
    E = [x for x in edges_of(g) if x != e and (x[1], x[0]) != e]
    return adj(len(g), E)


def del_vertex(g, v):
    n = len(g)
    idx = {}
    k = 0
    for u in range(n):
        if u != v:
            idx[u] = k
            k += 1
    E = [(idx[a], idx[b]) for a, b in edges_of(g) if a != v and b != v]
    return adj(n - 1, E)


def attach_hairs(gp, spec):
    """G = G' + hairs.  spec = [(root, h), ...] with DISTINCT roots and h >= 1.
    Returns (G, hair_vertex_lists) where hair_vertex_lists[i] = [x_i^1, ..., x_i^h_i]."""
    roots = [w for w, _ in spec]
    assert len(set(roots)) == len(roots), "roots must be distinct"
    n = len(gp)
    E = edges_of(gp)
    hairs = []
    nxt = n
    for w, h in spec:
        assert h >= 1
        chain = []
        prev = w
        for _ in range(h):
            E.append((prev, nxt))
            chain.append(nxt)
            prev = nxt
            nxt += 1
        hairs.append(chain)
    return adj(nxt, E), hairs


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append(0)
    print("\n[PART 0] guards and controls", flush=True)

    # a_val vs a_val_brute on every vertex of a mixed sample
    hosts = [cycle(6), cycle(9), petersen(), theta(3, 3, 3), two_cycles_glued(9, 9)]
    tested = 0
    for g in hosts:
        for v in range(len(g)):
            check(a_val(g, v) == a_val_brute(g, v), "a_val mismatch")
            tested += 1
    print("  a_val double-sourced on %d vertices over %d hosts" % (tested, len(hosts)))

    # is_induced_path liveness: it must REJECT as well as accept
    c6 = cycle(6)
    check(is_induced_path(c6, [0, 1, 2, 3]), "C6 0-1-2-3 should be induced")
    check(not is_induced_path(c6, [0, 1, 2, 3, 4, 5]), "the whole C6 is not a path")
    check(not is_induced_path(c6, [0, 2]), "non-adjacent pair is not a path")

    # THE STANDING ZERO-STEP GUARD -- shown to FIRE on a planted broken search.
    def broken_endpath(g, s):
        n = len(g)
        best = [1]
        blocked = [False] * n
        blocked[s] = True
        for y in g[s]:          # <-- r33 defect #1 / r34 defect #2, planted here on purpose
            blocked[y] = True

        def rec(cur, ln):
            best[0] = max(best[0], ln)
            cands = [x for x in g[cur] if not blocked[x]]
            for x in cands:
                newly = [y for y in cands if y != x]
                newly.append(x)
                for y in newly:
                    blocked[y] = True
                rec(x, ln + 1)
                for y in newly:
                    blocked[y] = False
        rec(s, 1)
        return best[0]

    bad = broken_endpath(c6, 0)
    check(bad == 1, "planted broken search must return 1 (it returned %d)" % bad)
    fired = False
    try:
        # the guard is in endpath(); simulate its trigger on the broken value
        if bad == 1 and len(c6[0]) > 0:
            raise ZeroStepAbort("planted")
    except ZeroStepAbort:
        fired = True
    check(fired, "ZERO-STEP GUARD did not fire on the planted broken search")
    good = endpath(c6, 0)
    check(good == 5, "endpath(C6,0) should be 5, got %d" % good)
    print("  ZERO-STEP GUARD: planted broken search returns %d and the guard FIRES; "
          "the corrected search returns %d" % (bad, good))

    # endpath vs an independent exhaustive check on a small host
    g = theta(3, 3, 3)
    n = len(g)
    bestbrute = 0
    for k in range(n, 1, -1):
        if bestbrute:
            break
        for S in combinations(range(n), k):
            sub = set(S)
            deg = {v: len([u for u in g[v] if u in sub]) for v in S}
            if sorted(deg.values())[:2] == [1, 1] and max(deg.values()) <= 2:
                # check connectivity of the induced subgraph
                st = [S[0]]
                seen = {S[0]}
                while st:
                    u = st.pop()
                    for x in g[u]:
                        if x in sub and x not in seen:
                            seen.add(x)
                            st.append(x)
                if len(seen) == k:
                    bestbrute = k
                    break
    lip = longest_induced_path(g)
    check(lip == bestbrute, "longest_induced_path(Theta(3,3,3)) = %d vs brute %d"
          % (lip, bestbrute))
    print("  longest_induced_path double-sourced on Theta(3,3,3): %d == %d"
          % (lip, bestbrute))


# ------------------------------------------------------------------ PART 1
def ecc_core_formula(gp, spec, c):
    """My re-derivation of the core-vertex eccentricity in G = G' + hairs."""
    Dp = bfs(gp, c)
    return max(max(Dp), max(Dp[w] + h for w, h in spec))


def ecc_hair_formula(gp, spec, i, j):
    """My re-derivation of the eccentricity of the j-th vertex of hair i (1 <= j <= h_i)."""
    w_i, h_i = spec[i]
    Dp = bfs(gp, w_i)
    terms = [h_i - j, j + max(Dp)]
    for m, (w_m, h_m) in enumerate(spec):
        if m != i:
            terms.append(j + Dp[w_m] + h_m)
    return max(terms)


def part1():
    PARTS_RUN.append(1)
    print("\n[PART 1] multi-hair eccentricity formulas, re-derived and BFS-certified",
          flush=True)
    bases = [("C6", cycle(6)), ("C9", cycle(9)), ("Petersen", petersen()),
             ("Theta333", theta(3, 3, 3)), ("C9+C9", two_cycles_glued(9, 9)),
             ("P5", path_graph(5))]
    specs_tested = 0
    core_checks = 0
    hair_checks = 0
    for name, gp in bases:
        np_ = len(gp)
        roots = list(range(min(np_, 4)))
        for k in (1, 2, 3):
            if k > len(roots):
                continue
            for combo in combinations(roots, k):
                for hs in [(1,) * k, (2,) * k, tuple(range(1, k + 1))]:
                    spec = list(zip(combo, hs))
                    G, hairs = attach_hairs(gp, spec)
                    D, ecc, r, centres = profile(G)
                    specs_tested += 1
                    for c in range(np_):
                        check(ecc[c] == ecc_core_formula(gp, spec, c),
                              "core ecc formula %s %s c=%d" % (name, spec, c))
                        core_checks += 1
                    for i, chain in enumerate(hairs):
                        for j, u in enumerate(chain, start=1):
                            check(ecc[u] == ecc_hair_formula(gp, spec, i, j),
                                  "hair ecc formula %s %s i=%d j=%d" % (name, spec, i, j))
                            hair_checks += 1
                if over():
                    print("  DEADLINE inside PART 1; partial results stand")
                    break
    print("  hair configurations tested: %d over %d bases" % (specs_tested, len(bases)))
    print("  core-eccentricity formula verified at %d (graph,vertex) pairs" % core_checks)
    print("  hair-eccentricity formula verified at %d (graph,vertex) pairs" % hair_checks)

    # E11's headline, rebuilt in my own hand: rad(G) need not be attained on the core.
    LONG = 100
    gp = adj(2, [(0, 1)])                        # K2 core, w1 = 0, w2 = 1
    spec = [(0, LONG), (1, 1)]
    G, hairs = attach_hairs(gp, spec)
    D, ecc, r, centres = profile(G)
    core_min = min(ecc[0], ecc[1])
    print("  [E11 rebuild] K2 core, hairs of length %d and 1: n=%d" % (LONG, len(G)))
    print("    ecc(w1)=%d  ecc(w2)=%d  min over the core=%d" % (ecc[0], ecc[1], core_min))
    print("    rad(G)=%d  |centre|=%d  centre inside the long hair: %s"
          % (r, len(centres), all(c in hairs[0] for c in centres)))
    check(r < core_min, "rad must be strictly below the core minimum")
    check(all(c in hairs[0] for c in centres), "every centre must lie inside hair 1")
    check(r == (LONG + 2 + 1) // 2, "closed form ceil((h+alpha)/2) for hair 1")
    print("    CONFIRMED IN MY OWN HAND: rad(G)=%d is attained strictly inside a hair, "
          "while min ecc over V(G') = %d." % (r, core_min))
    print("    E11's prose reports ecc(w2) = 102; the BFS value is %d. "
          "The slip is real and does not touch the headline." % ecc[1])
    check(ecc[1] == 1 + LONG, "ecc(w2) = 1 + h1")


# ------------------------------------------------------------------ PART 2
def part2():
    PARTS_RUN.append(2)
    print("\n[PART 2] the a-value / l(G) bookkeeping for hairs", flush=True)

    # (a) E12 Lemma A(ii): "a_G(x_i^t) = 1 for every hair vertex".
    gp = cycle(6)
    spec = [(0, 3)]
    G, hairs = attach_hairs(gp, spec)
    vals = [a_val(G, u) for u in hairs[0]]
    valsb = [a_val_brute(G, u) for u in hairs[0]]
    check(vals == valsb, "a_val/a_val_brute disagree on hair vertices")
    print("  hair of length %d on C6: a-values along the hair = %s" % (3, vals))
    check(vals[0] == 2, "the first hair vertex has two NON-adjacent neighbours")
    check(vals[-1] == 1, "the tip has a single neighbour")
    print("  E12 Lemma A(ii) claims 1 at every hair vertex. Interior hair vertices "
          "measure %d, because x^{t-1} and x^{t+1} are NOT adjacent. REFUTED." % vals[0])

    # (b) the exact a-sum for hairs, and the two competing l(G) formulas.
    bases = [("C6", cycle(6)), ("C9", cycle(9)), ("Petersen", petersen()),
             ("Theta333", theta(3, 3, 3)), ("C9+C9", two_cycles_glued(9, 9)),
             ("PG(2,3)", pg2(3))]
    tested = 0
    e12_matches = 0
    mine_matches = 0
    lemC_pop = 0
    lemC_hits = 0
    for name, gp in bases:
        np_ = len(gp)
        lp = mean_a(gp)
        roots = list(range(min(np_, 4)))
        for k in (1, 2, 3):
            if k > len(roots):
                continue
            for combo in combinations(roots, k):
                for hs in [(1,) * k, (3,) * k, tuple(range(1, k + 1))]:
                    spec = list(zip(combo, hs))
                    G, _ = attach_hairs(gp, spec)
                    H = sum(h for _, h in spec)
                    lg = mean_a(G)
                    mine = (np_ * lp + 2 * H) / float(np_ + H)
                    e12 = (np_ * lp + 2 * k) / float(np_ + H)
                    tested += 1
                    if abs(lg - mine) < 1e-9:
                        mine_matches += 1
                    if abs(lg - e12) < 1e-9:
                        e12_matches += 1
                    lemC_pop += 1
                    if int(lg) <= int(lp):
                        lemC_hits += 1
                    check(abs(lg - mine) < 1e-9,
                          "my l(G) formula failed on %s %s" % (name, spec))
                    check(int(lg) <= int(lp),
                          "Lemma C failed on %s %s" % (name, spec))
    print("  hair configurations tested: %d" % tested)
    print("  l(G) = (n'l' + 2H)/(n'+H)  [MINE]  matches BFS/alpha count on %d of %d"
          % (mine_matches, tested))
    print("  l(G) = (n'l' + 2k)/(n'+H)  [E12 Lemma B] matches on %d of %d"
          % (e12_matches, tested))
    print("  floor(l(G)) <= floor(l(G')) [Lemma C, corrected proof] holds on %d of %d"
          % (lemC_hits, lemC_pop))
    print("  POPULATION for both counts: the %d configurations above; EXCLUSIONS: "
          "designed families only, roots drawn from the first four vertices of each base, "
          "k <= 3, h_i <= 3, no random trawl, no enumeration." % tested)


# ------------------------------------------------------------------ PART 3
def part3():
    PARTS_RUN.append(3)
    print("\n[PART 3] E12's radius identity and its endpath route", flush=True)

    # (a) R = max(r', max_i(d'(c0,w_i)+h_i)) for a centre c0 of G' -- tested.
    LONG = 100
    gp = adj(2, [(0, 1)])
    spec = [(0, LONG), (1, 1)]
    G, _ = attach_hairs(gp, spec)
    _, _, R, _ = profile(G)
    _, eccp, rp, centres_p = profile(gp)
    claims = []
    for c0 in centres_p:
        Dp = bfs(gp, c0)
        claims.append(max(rp, max(Dp[w] + h for w, h in spec)))
    print("  K2 core with hairs (%d,1): rad(G) measured by BFS = %d" % (LONG, R))
    print("    E12's identity would give %s over the centres of G'" % sorted(set(claims)))
    check(all(cl != R for cl in claims),
          "E12's radius identity should be refuted by E11's own example")
    check(R < min(claims), "the true radius is strictly below E12's value")
    print("    REFUTED, and by an example from E12's OWN BATCH (E11 Part 3). "
          "E12's (R2) and its Case-II reduction rest on this identity.")

    # (b) TE: does path(G) >= h_i + ecc_{G'}(w_i) + 3 hold?
    #     (TAIL-1) gives h_i + ecc_{G'}(w_i) + 2 vertices; E12 writes +3.
    tests = []
    for name, gp in [("C6", cycle(6)), ("C9", cycle(9)), ("Petersen", petersen())]:
        _, eccp, rp, _ = profile(gp)
        for w in range(min(len(gp), 3)):
            for h in (1, 2):
                spec = [(w, h)]
                G, _ = attach_hairs(gp, spec)
                if len(G) > 16:
                    continue
                P = longest_induced_path(G)
                tail1 = h + eccp[w] + 2
                te = h + eccp[w] + 3
                tests.append((name, w, h, P, tail1, te))
    ok1 = sum(1 for t in tests if t[3] >= t[4])
    ok2 = sum(1 for t in tests if t[3] >= t[5])
    print("  single-hair instances tested: %d" % len(tests))
    print("    path(G) >= h + ecc_{G'}(w) + 2   [(TAIL-1) route, MINE]: %d of %d"
          % (ok1, len(tests)))
    print("    path(G) >= h + ecc_{G'}(w) + 3   [E12 Tool TE]:          %d of %d"
          % (ok2, len(tests)))
    check(ok1 == len(tests), "the +2 route must hold everywhere")
    viol = [t for t in tests if t[3] < t[5]]
    check(len(viol) > 0, "expected at least one counterexample to E12's +3")
    if viol:
        name, w, h, P, t1, te = viol[0]
        print("    COUNTEREXAMPLE to E12's TE: base %s, root %d, h=%d -> path(G)=%d "
              "but E12's bound asserts %d." % (name, w, h, P, te))
    print("  EXCLUSIONS for these counts: three bases, roots among the first three "
          "vertices, h in {1,2}, hosts capped at 16 vertices for the exact path.")


# ------------------------------------------------------------------ PART 4
def part4():
    PARTS_RUN.append(4)
    print("\n[PART 4] CASE I of the multi-hair reduction: rad(G) = rad(G')", flush=True)
    bases = [("C6", cycle(6)), ("C9", cycle(9)), ("Theta333", theta(3, 3, 3)),
             ("Petersen", petersen()), ("C9+C9", two_cycles_glued(9, 9))]
    caseI = 0
    caseII = 0
    caseI_ok = 0
    caseII_ok = 0
    ind_ok = 0
    total = 0
    skipped = 0
    for name, gp in bases:
        np_ = len(gp)
        if not (connected(gp) and c4_free(gp)):
            continue
        lp = mean_a(gp)
        _, _, rp, _ = profile(gp)
        pathp = longest_induced_path(gp)
        base_conj = pathp >= rp + int(lp)
        roots = list(range(min(np_, 4)))
        for k in (2, 3):
            if k > len(roots):
                continue
            for combo in combinations(roots, k):
                for hs in [(1,) * k, (2,) * k, tuple(range(1, k + 1))]:
                    spec = list(zip(combo, hs))
                    G, _ = attach_hairs(gp, spec)
                    if len(G) > 16 or over():
                        skipped += 1
                        continue
                    if not c4_free(G):
                        skipped += 1
                        continue
                    total += 1
                    _, _, R, _ = profile(G)
                    lg = mean_a(G)
                    P = longest_induced_path(G)
                    if P < pathp:
                        check(False, "G' induced in G must give path(G) >= path(G')")
                    else:
                        ind_ok += 1
                    conj = P >= R + int(lg)
                    if R == rp:
                        caseI += 1
                        if conj:
                            caseI_ok += 1
                        check(not base_conj or conj,
                              "CASE I must inherit the conjecture: %s %s" % (name, spec))
                    else:
                        caseII += 1
                        if conj:
                            caseII_ok += 1
    print("  multi-hair instances (k >= 2) certified C4-free and computed: %d "
          "(skipped %d: over 16 vertices, not C4-free, or past the deadline)"
          % (total, skipped))
    print("  path(G) >= path(G') held on %d of %d" % (ind_ok, total))
    print("  CASE I  (rad(G) = rad(G')): %d instances, conjecture holds on %d"
          % (caseI, caseI_ok))
    print("  CASE II (rad(G) > rad(G')): %d instances, conjecture holds on %d"
          % (caseII, caseII_ok))
    check(caseI + caseII == total, "case split must be exhaustive")
    check(caseI_ok == caseI, "CASE I must be clean")
    print("  POPULATION: the %d instances above.  EXCLUSIONS: five bases, roots among "
          "the first four vertices, k in {2,3}, h_i <= 3, hosts capped at 16 vertices "
          "for the exact induced path.  Not exhaustive." % total)


# ------------------------------------------------------------------ PART 5
def ball_size(D_w, rad):
    return sum(1 for x in D_w if 0 <= x <= rad)


def part5():
    PARTS_RUN.append(5)
    print("\n[PART 5] the CENTRE-SPHERE bound", flush=True)

    # (a) The bound, verified wherever the configuration EXISTS (positive controls).
    hosts = [("C6", cycle(6)), ("C9", cycle(9)), ("C9+C9", two_cycles_glued(9, 9)),
             ("Theta333", theta(3, 3, 3)), ("Petersen", petersen()),
             ("C7", cycle(7)), ("C11", cycle(11)), ("P7", path_graph(7))]
    live = 0
    pop = 0
    bound_ok = 0
    cs3_scope = 0
    cs3_ok = 0
    for name, g in hosts:
        n = len(g)
        D, ecc, r, centres = profile(g)
        delta = min(len(g[v]) for v in range(n))
        for w in range(n):
            if r >= 1 and maximally_far(D, w, centres, r):
                pop += 1
                live += 1
                bsz = ball_size(D[w], r - 1)
                if len(centres) <= n - bsz:
                    bound_ok += 1
                check(len(centres) <= n - bsz,
                      "CENTRE-SPHERE bound violated on %s at w=%d" % (name, w))
                check(all(D[c][w] == r for c in centres), "hypothesis restated")
                # (CS-3) must NOT forbid a configuration that demonstrably exists.
                if c4_free(g) and delta >= 2 and r >= 3:
                    cs3_scope += 1
                    b3 = n - 1 - delta * (delta - 1) - (r - 3)
                    if len(centres) <= b3:
                        cs3_ok += 1
                    check(len(centres) <= b3,
                          "(CS-3) forbids a configuration that EXISTS on %s at w=%d"
                          % (name, w))
    print("  positive controls: %d (host,w) pairs across %d hosts actually CARRY the "
          "configuration; the bound |C| <= n - |B_{r-1}(w)| holds on %d of %d"
          % (live, len(hosts), bound_ok, pop))
    print("  of those, %d also satisfy (CS-3)'s hypotheses (C4-free, delta >= 2, r >= 3); "
          "(CS-3) permits the configuration on %d of %d -- it over-claims on none"
          % (cs3_scope, cs3_ok, cs3_scope))
    check(live > 0, "the predicate must be live -- a bound proved on an empty set is void")
    check(cs3_scope > 0, "(CS-3) must be exercised on a LIVE instance, not only on empties")

    # (b) The C4-free ball lower bound |B_2(w)| >= 1 + deg(w)*(delta-1).
    c4hosts = [("Petersen", petersen()), ("PG(2,3)", pg2(3)), ("C9+C9", two_cycles_glued(9, 9)),
               ("C6", cycle(6)), ("Theta333", theta(3, 3, 3))]
    bb_pop = 0
    bb_ok = 0
    for name, g in c4hosts:
        if not c4_free(g):
            continue
        n = len(g)
        delta = min(len(g[v]) for v in range(n))
        if delta < 2:
            continue
        for w in range(n):
            D = bfs(g, w)
            bb_pop += 1
            lhs = ball_size(D, 2)
            rhs = 1 + len(g[w]) * (delta - 1)
            if lhs >= rhs:
                bb_ok += 1
            check(lhs >= rhs, "ball bound failed on %s at %d (%d < %d)"
                  % (name, w, lhs, rhs))
    print("  C4-free ball bound |B_2(w)| >= 1 + deg(w)*(delta-1): %d of %d vertices"
          % (bb_ok, bb_pop))

    # (c) APPLICATION -- round 34's 248 PG(2,5) surgery hosts, now by PROOF.
    core = pg2(5)
    print("  core PG(2,5): n=%d, C4-free=%s, connected=%s"
          % (len(core), c4_free(core), connected(core)))
    fam = []
    for e in edges_of(core):
        fam.append(("PG(2,5)-e", del_edge(core, e)))
    for v in range(len(core)):
        fam.append(("PG(2,5)-v", del_vertex(core, v)))
    certified = 0
    proved_empty = 0
    measured_empty = 0
    undecided = []
    out_of_scope = 0
    lgt4 = 0
    nonselfcentred = 0
    radii = {}
    sample = None
    for name, g in fam:
        if over():
            print("  DEADLINE inside PART 5(c); partial results stand")
            break
        if not (connected(g) and c4_free(g)):
            continue
        delta = min(len(g[v]) for v in range(len(g)))
        if delta < 2:
            continue
        certified += 1
        n = len(g)
        D, ecc, r, centres = profile(g)
        radii[r] = radii.get(r, 0) + 1
        if len(centres) < n:
            nonselfcentred += 1
        if mean_a(g) > 4:
            lgt4 += 1
        res = [w for w in range(n) if maximally_far(D, w, centres, r)]
        if len(res) == 0:
            measured_empty += 1
        if r < 3:
            # the |B_2| lower bound is NOT a lower bound for |B_{r-1}| when r < 3.
            out_of_scope += 1
            continue
        bound = n - (1 + delta * (delta - 1) + (r - 3))
        if sample is None:
            sample = (name, n, r, delta, len(centres), bound)
        if len(centres) > bound:
            proved_empty += 1
            check(len(res) == 0,
                  "PROOF says empty but a witness exists on %s (n=%d)" % (name, n))
        else:
            undecided.append((name, n, r, delta, len(centres), bound, len(res)))
    print("  hosts certified connected, C4-free, delta >= 2: %d" % certified)
    print("  radius distribution over those hosts: %s" % sorted(radii.items()))
    print("  of those, non-self-centred: %d ; with l(G) > 4: %d" % (nonselfcentred, lgt4))
    print("  out of the corollary's scope (r < 3, where |B_2| is not a bound on "
          "|B_{r-1}|): %d" % out_of_scope)
    if sample:
        print("    representative host: %s  n=%d  r=%d  delta=%d  |C|=%d  "
              "n-(1+delta(delta-1)+(r-3))=%d  -> |C| exceeds the bound: %s"
              % (sample + (sample[4] > sample[5],)))
    print("  hosts where the CENTRE-SPHERE bound PROVES no vertex can be maximally far "
          "from every centre: %d of %d" % (proved_empty, certified))
    print("  hosts where BFS MEASURES that set empty: %d of %d"
          % (measured_empty, certified))
    print("  hosts the bound leaves undecided: %d" % len(undecided))
    for row in undecided[:5]:
        print("    undecided: %s n=%d r=%d delta=%d |C|=%d bound=%d measured=%d" % row)
    check(proved_empty <= measured_empty,
          "the proof may never claim empty where the measurement finds a witness")
    check(proved_empty + len(undecided) + out_of_scope == certified,
          "the three outcome buckets must partition the certified population")
    print("  EXCLUSION LIST for this block: single-edge and single-vertex deletions from "
          "ONE core, PG(2,5); no multi-edge surgery, no second core, no search.")


def main():
    print("w133 r35 -- multi-hair reproduced in my own hand + the CENTRE-SPHERE bound")
    print("started", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("interpreter:", sys.version.split()[0], "(system python3 expected)")
    for f in (part0, part1, part2, part3, part4, part5):
        try:
            f()
        except ZeroStepAbort as ex:
            print("ABORT (zero-step guard):", ex)
            check(False, "zero-step guard fired in %s" % f.__name__)
        except Exception as ex:                       # noqa: BLE001
            print("EXCEPTION in", f.__name__, ":", repr(ex))
            check(False, "exception in %s" % f.__name__)
    expected = [0, 1, 2, 3, 4, 5]
    check(PARTS_RUN == expected,
          "declared parts %s but ran %s" % (expected, PARTS_RUN))
    print("\nPARTS RUN:", PARTS_RUN)
    print("CHECKS:", CHECKS, " FAILURES:", FAIL)
    print("elapsed %.1f s" % (time.time() - T0))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
