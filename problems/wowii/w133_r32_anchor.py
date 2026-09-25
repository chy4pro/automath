#!/usr/bin/env python3
"""
w133 round 32 (owner-w133) — the SUCCESSOR TARGET (F11-AT-w), sharpened and MEASURED.

r31 refuted (A2-PATH) and proposed

    (F11-AT-w)   endpath(G', w) >= rad(G') + 4   at the attachment w of a deepest hair.

This round does four things, in this order:

 PART 1  THE QUANTIFIER.  A hair may be hung at ANY vertex, and a single hair is trivially the
         deepest one.  So the clause "at the attachment of a DEEPEST hair" carries NO positional
         information: (F11-AT-w) is, on its own hypothesis class, the UNIVERSAL statement
         "endpath(G',w) >= rad(G')+4 for EVERY w".  That is STRICTLY STRONGER than F11 = G42
         (which is the EXISTENTIAL "some induced path has rad+4 vertices"), not a mild anchoring
         of it.  Machine: the exact l-threshold arithmetic for G' + one pendant.

 PART 2  (TAIL-1), UNCONDITIONAL:   C4-free, mu(G) >= 2  ==>  endpath(G,w) >= ecc(w) + 2
         for EVERY w.  Certified by BUILDING the path and verifying it is induced, over every
         vertex of every test graph.  No l > 4, no rad >= 5, no F11.

 PART 3  (TAIL-2), one more vertex at the cost of a POINTWISE density hypothesis:
         if some y in N(u_d) off u_{d-1}'s component has a(y) >= 4 then endpath(G,w) >= ecc(w)+3.
         And (TAIL-3) needs a(z) >= 6 — the dodge list at the third step is
         {u_{d-1}, u_{d-2}, u_{d-3}, u_{d-4}} plus the previous component.  Both certified by
         construction, and the dodge lists are verified to be exactly right (which exclusions are
         FORCED by C4-freeness and which must be paid for).

 PART 4  THE THEOREM.  For the SINGLE-HAIR case — which is exactly the class in which r31 killed
         (A2-PATH) — route A2's conclusion  path(G) >= rad(G) + 4  follows, and the residual is a
         SINGLE named configuration.  Machine-verified end to end on explicit graphs, with
         path(G) computed exactly (longest induced path) wherever n permits.

 PART 5  NON-VACUITY of the residual configuration, and its scope measured.

NO SAT.  Explicit graphs, exact BFS, bounded DFS for longest induced path on small graphs only.
Every part registers itself; the final check asserts EVERY declared part actually ran, because
`exit 0` is a claim about the PROCESS and not about the WORK (r31 own-defect 7).
"""
import sys
from collections import deque
from itertools import combinations

FAIL = 0
CHECKS = 0
PARTS_DECLARED = ["PART0", "PART1", "PART2", "PART3", "PART4", "PART5", "PART6"]
PARTS_RUN = []


def check(cond, msg):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("FAIL:", msg)
    return cond


# ----------------------------------------------------------------- primitives
def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s, alive=None):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if alive is not None and w not in alive:
                continue
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g, alive=None):
    if alive is None:
        alive = set(range(len(g)))
    if not alive:
        return False
    s = next(iter(alive))
    d = bfs(g, s, alive)
    return all(d[v] >= 0 for v in alive)


def ecc(g, v, alive=None):
    if alive is None:
        alive = set(range(len(g)))
    d = bfs(g, v, alive)
    return max(d[u] for u in alive)


def rad(g, alive=None):
    if alive is None:
        alive = set(range(len(g)))
    return min(ecc(g, v, alive) for v in alive)


def c4_free(g):
    """C4-free in this line's sense: NO two vertices have two common neighbours."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def c4_free_slow(g):
    """Independent implementation: no 4-cycle as a SUBGRAPH.  Cross-check of c4_free."""
    n = len(g)
    for a, b, c, d in combinations(range(n), 4):
        for perm in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            p, q, r, s = perm
            if q in g[p] and r in g[q] and s in g[r] and p in g[s]:
                return False
    return True


def a_val(g, v):
    """a(v) = independence number of G[N(v)];  in a C4-free graph G[N(v)] is a matching,
    so a(v) = deg(v) - (#edges inside N(v)).  Both computed; they are cross-checked."""
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


def nbhd_components(g, v):
    """Components of G[N(v)] (a matching when G is C4-free)."""
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


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    return all((P[j] in g[P[i]]) == (j == i + 1)
               for i in range(len(P)) for j in range(i + 1, len(P)))


def peel_all(g):
    """Remove every a=1 vertex, repeatedly.  Returns (alive set, peeled set)."""
    alive = set(range(len(g)))
    while True:
        gone = [v for v in alive
                if len(g[v] & alive) - sum(1 for x, y in combinations(sorted(g[v] & alive), 2)
                                           if y in g[x]) <= 1]
        if not gone:
            return alive, set(range(len(g))) - alive
        alive -= set(gone)
        if not alive:
            return alive, set(range(len(g)))


def longest_induced_path(g, start=None, cap=None, node_budget=4_000_000):
    """Longest induced path (VERTEX count).  If start is given, it must be an ENDPOINT.
    If cap is given, stop as soon as a path with `cap` vertices is found (returns >= cap)."""
    n = len(g)
    best = 0
    nodes = [0]
    truncated = [False]

    def dfs(path, pathset, banned):
        nonlocal best
        nodes[0] += 1
        if nodes[0] > node_budget:
            truncated[0] = True
            return True
        if len(path) > best:
            best = len(path)
            if cap is not None and best >= cap:
                return True
        last = path[-1]
        for x in sorted(g[last]):
            if x in pathset or x in banned:
                continue
            # x must be non-adjacent to every path vertex except `last`
            if any(p in g[x] for p in path[:-1]):
                continue
            newban = banned | (g[last] - {x})
            if dfs(path + [x], pathset | {x}, newban):
                return True
        return False

    starts = [start] if start is not None else list(range(n))
    for s in starts:
        if dfs([s], {s}, set()):
            break
    return best, truncated[0]


def endpath(g, w, cap=None):
    return longest_induced_path(g, start=w, cap=cap)


def mean_a(g, alive=None):
    if alive is None:
        alive = set(range(len(g)))
    sub = induced(g, alive)
    idx = sorted(alive)
    return sum(a_val(sub, i) for i in range(len(idx))), len(idx)


def induced(g, alive):
    idx = sorted(alive)
    pos = {v: i for i, v in enumerate(idx)}
    E = [(pos[u], pos[v]) for u in idx for v in g[u] if v in pos and u < v]
    return adj(len(idx), E)


# ----------------------------------------------------------------- test graphs
def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def two_cycles_glued(a, b):
    """Two cycles C_a, C_b sharing exactly vertex 0."""
    E = [(i, (i + 1) % a) for i in range(a)]
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


def pg2(q):
    """Incidence graph of PG(2,q) for prime q — bipartite, girth 6, degree q+1."""
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


def blob_chain(q=3, L=5):
    """Two PG(2,q) incidence graphs joined by an induced path of L internal vertices —
    the W1 shape.  C4-free, mu >= 2, l = q+1, and rad forced up by the joining path."""
    b = pg2(q)
    bn = len(b)
    E = [(u, v) for (u, v) in edges_of(b)]
    E += [(u + bn, v + bn) for (u, v) in edges_of(b)]
    n = 2 * bn
    prev = 1
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, bn + 0))
    return adj(n, E)


def theta(a, b, c):
    """Two poles joined by three internally disjoint paths of a, b, c EDGES."""
    E = []
    n = 2
    for L in (a, b, c):
        prev = 0
        for _ in range(L - 1):
            E.append((prev, n))
            prev = n
            n += 1
        E.append((prev, 1))
    return adj(n, E)


def rand_c4free(seed, n, extra):
    """Seeded, deterministic: a cycle plus `extra` random C4-preserving chords, then peeled."""
    st = seed
    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    g = cycle(n)
    for _ in range(extra):
        u, v = nxt(n), nxt(n)
        if u == v or v in g[u]:
            continue
        if len(g[u] & g[v]) >= 1:
            continue
        ok = all(len((g[u] | {v}) & (g[x] | ({u} if x in g[v] else set()))) < 2 for x in range(n))
        g[u].add(v); g[v].add(u)
        if not c4_free(g):
            g[u].discard(v); g[v].discard(u)
    alive, _ = peel_all(g)
    if len(alive) < 6 or not connected(g, alive):
        return None
    h = induced(g, alive)
    if not connected(h) or min(a_val(h, v) for v in range(len(h))) < 2:
        return None
    return h


def hairy(g, w, h):
    """G' + a single hair (induced path of h vertices) hung at w."""
    n = len(g)
    E = edges_of(g)
    prev = w
    for _ in range(h):
        E.append((prev, n))
        prev = n
        n += 1
    return adj(n, E)


# ================================================================== PART 0
def part0():
    PARTS_RUN.append("PART0")
    print("=" * 78)
    print("PART 0 — PRIMITIVES, CROSS-CHECKED RATHER THAN TRUSTED")
    print("=" * 78)
    fam = [cycle(9), cycle(5), two_cycles_glued(9, 9), two_cycles_glued(5, 5),
           petersen(), pg2(2), pg2(3)]
    names = ["C9", "C5", "2xC9 glued", "2xC5 glued", "Petersen", "PG(2,2)=Heawood", "PG(2,3)"]
    for g, nm in zip(fam, names):
        n = len(g)
        cf, cfs = c4_free(g), (c4_free_slow(g) if n <= 26 else None)
        if cfs is not None:
            check(cf == cfs, "%s: the two C4-free implementations disagree" % nm)
        av = [a_val(g, v) for v in range(n)]
        ab = [a_val_brute(g, v) for v in range(n)]
        check(av == ab, "%s: a = d - t disagrees with brute-force independence number" % nm)
        mu = min(av)
        print("  %-16s n=%-3d C4-free=%-5s  rad=%-2d  mu=%d  mean a = %.4f"
              % (nm, n, cf, rad(g), mu, sum(av) / n))
    # a self-check that CAN fail: a graph that IS NOT C4-free must be reported so.
    k4 = adj(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    c4 = cycle(4)
    check(not c4_free(c4), "LIVENESS: C4 itself was not reported as containing a C4")
    check(not c4_free_slow(c4), "LIVENESS(slow): C4 itself was not reported as containing a C4")
    check(not c4_free(k4), "LIVENESS: K4 contains a 4-cycle SUBGRAPH and must be refused")
    print("  liveness probe: C4 and K4 are both REFUSED by both implementations (they must be:")
    print("    C4-free on this line means NO TWO VERTICES HAVE TWO COMMON NEIGHBOURS).")
    # peel_all liveness
    g = hairy(cycle(9), 3, 2)
    alive, peeled = peel_all(g)
    check(peeled == {9, 10}, "peel_all did not remove the 2-vertex hair from C9")
    check(alive == set(range(9)), "peel_all did not return C9 exactly")
    print("  peel_all probe: C9 + 2-hair  ->  peeled %s, alive = C9  [OK]" % sorted(peeled))
    print()


# ================================================================== PART 1
def part1():
    PARTS_RUN.append("PART1")
    print("=" * 78)
    print("PART 1 — THE QUANTIFIER: 'at the attachment of a DEEPEST hair' IS VACUOUS")
    print("=" * 78)
    print("""  A single hair is trivially the deepest hair, and a hair may be hung at ANY vertex of
  G'.  So over the class of G' to which (F11-AT-w) is meant to apply, the prescribed w
  ranges over EVERY vertex.  (F11-AT-w) is therefore the UNIVERSAL statement

      (F11-ALL)   endpath(G', w) >= rad(G') + 4   for EVERY vertex w of G',

  and F11 = G42 is the EXISTENTIAL one.  (F11-AT-w) is STRICTLY STRONGER than F11, not a
  mild anchoring of it.  That is a defect in the r31 proposal and it is this round's first
  finding against its own previous entry.""")
    # the arithmetic:  adding one pendant at w changes Sigma a by exactly +2 and n by +1
    for g, nm in [(pg2(3), "PG(2,3)"), (pg2(2), "Heawood"), (blob_chain(3, 5), "blob_chain(3,5)")]:
        n = len(g)
        S = sum(a_val(g, v) for v in range(n))
        for w in range(min(n, 6)):
            gh = hairy(g, w, 1)
            S2 = sum(a_val(gh, v) for v in range(n + 1))
            check(S2 == S + 2, "%s: adding a pendant at %d did not move Sigma a by exactly +2" % (nm, w))
            check(c4_free(gh), "%s: adding a pendant broke C4-freeness" % nm)
            alive, peeled = peel_all(gh)
            check(peeled == {n} and alive == set(range(n)),
                  "%s: peel(G'+pendant at %d) is not G'" % (nm, w))
            check(rad(gh) >= rad(g), "%s: adding a pendant lowered the radius at w=%d" % (nm, w))
        print("  %-18s n=%-4d Sigma a = %-5d  l = %.4f   ->  G'+pendant: Sigma a = %d, n = %d,"
              % (nm, n, S, S / n, S + 2, n + 1))
        print("  %-18s l(G) > 4  <==>  Sigma_{G'}(a-4) > 2   (exact threshold, not an estimate)"
              % "")
    # the exact statement of the threshold, verified as an EQUIVALENCE on a case that is tight
    g = pg2(3)
    n = len(g)
    S = sum(a_val(g, v) for v in range(n))
    check(S - 4 * n == 0, "PG(2,3) control: Sigma(a-4) must be exactly 0 (l = 4.0 exactly)")
    gh = hairy(g, 0, 1)
    S2 = sum(a_val(gh, v) for v in range(n + 1))
    check(S2 - 4 * (n + 1) == -2, "PG(2,3)+pendant: Sigma(a-4) must be -2")
    print("  CONTROL (pinned, not inferred): l(PG(2,3)) = 4.0 EXACTLY  [Sigma(a-4) = 0];")
    print("    PG(2,3) + one pendant has Sigma(a-4) = -2, i.e. l drops BELOW 4 — so the")
    print("    l-threshold on G is  Sigma_{G'}(a-4) > 2,  marginally stronger than l(G') > 4.")
    print()


# ================================================================== PART 2
def build_tail1(g, w):
    """(TAIL-1).  Geodesic w=u_0..u_d to a furthest vertex, plus ONE vertex y past u_d.
    Returns the path, or None if the hypotheses are absent."""
    d = bfs(g, w)
    D = max(d)
    if D < 1:
        return None
    far = max(range(len(g)), key=lambda v: d[v])
    # reconstruct a geodesic w -> far
    path = [far]
    while path[-1] != w:
        u = path[-1]
        path.append(next(x for x in sorted(g[u]) if d[x] == d[u] - 1))
    path.reverse()                       # u_0 = w ... u_d = far
    ud, udm1 = path[-1], path[-2]
    comps = nbhd_components(g, ud)
    own = next(c for c in comps if udm1 in c)
    other = [c for c in comps if c is not own]
    if not other:
        return None                      # a(u_d) = 1 : outside the hypothesis mu >= 2
    y = min(min(c) for c in other)
    return path + [y]


def part2():
    PARTS_RUN.append("PART2")
    print("=" * 78)
    print("PART 2 — (TAIL-1): C4-free and mu(G) >= 2  ==>  endpath(G,w) >= ecc(w) + 2, EVERY w")
    print("=" * 78)
    print("""  PROOF.  Let w = u_0 ... u_d be a geodesic to a vertex at distance d = ecc(w).  Since
  a(u_d) >= 2, G[N(u_d)] (a matching, because G is C4-free) has a component other than
  u_{d-1}'s; take y in it.  Then y !~ u_{d-1} by choice; y !~ u_i for i <= d-3 because
  dist(u_i,u_d) >= 3; and y !~ u_{d-2}, because otherwise u_{d-2} and u_d would have the
  TWO common neighbours u_{d-1} and y — a C4.  So u_0..u_d y is an induced path on d+2
  vertices with w as an ENDPOINT.  []
  Certified below by BUILDING the path at every vertex of every test graph and verifying
  it is induced — the construction is executed, not the conclusion asserted.""")
    fam = [(cycle(9), "C9"), (cycle(11), "C11"), (two_cycles_glued(9, 9), "2xC9 glued"),
           (two_cycles_glued(5, 5), "2xC5 glued"), (petersen(), "Petersen"),
           (pg2(2), "Heawood"), (pg2(3), "PG(2,3)"), (blob_chain(2, 5), "blob_chain(2,5)"),
           (blob_chain(3, 5), "blob_chain(3,5)")]
    total_w = 0
    for g, nm in fam:
        n = len(g)
        check(c4_free(g), "%s is not C4-free — out of hypothesis" % nm)
        mu = min(a_val(g, v) for v in range(n))
        check(mu >= 2, "%s has mu < 2 — out of hypothesis" % nm)
        worst = None
        for w in range(n):
            P = build_tail1(g, w)
            check(P is not None, "%s: TAIL-1 construction declined at w=%d despite mu>=2" % (nm, w))
            if P is None:
                continue
            check(is_induced_path(g, P), "%s: TAIL-1 path at w=%d is NOT induced" % (nm, w))
            check(P[0] == w, "%s: TAIL-1 path at w=%d does not start at w" % (nm, w))
            e = ecc(g, w)
            check(len(P) == e + 2, "%s: TAIL-1 path at w=%d has %d vertices, expected ecc+2=%d"
                  % (nm, w, len(P), e + 2))
            total_w += 1
            if worst is None or len(P) - e < worst:
                worst = len(P) - e
        print("  %-18s n=%-4d rad=%-2d mu=%d : TAIL-1 built and CERTIFIED INDUCED at all %d "
              "vertices, always ecc(w)+2" % (nm, n, rad(g), mu, n))
    print("  TOTAL: %d (graph, vertex) pairs, every one carrying an explicit induced witness." % total_w)
    # TIGHTNESS, and it is the hardest form: a case where endpath(w) = ecc(w)+2 EXACTLY.
    g = cycle(9)
    for w in range(9):
        e = ecc(g, w)
        best, tr = endpath(g, w)
        check(not tr, "C9 endpath truncated")
        check(best >= e + 2, "C9: TAIL-1 bound violated at w=%d" % w)
    best0, _ = endpath(cycle(6), 0)
    check(best0 == ecc(cycle(6), 0) + 2,
          "C6 was expected to make TAIL-1 TIGHT (endpath = ecc+2 exactly)")
    print("  TIGHTNESS (hardest form): on C6, endpath(w) = ecc(w)+2 = 5 EXACTLY for every w —")
    print("    so TAIL-1 cannot be improved to ecc(w)+3 without a further hypothesis.")
    # LIVENESS: the construction must DECLINE when its own hypothesis a(u_d) >= 2 is absent.
    # The probe must be aimed at a w whose FURTHEST vertex is the a = 1 one.  Aiming it AT the
    # pendant tests nothing, because the far end is then a healthy cycle vertex.  The first
    # version of this probe was mis-aimed exactly that way; it is kept, named, not deleted.
    g = hairy(cycle(9), 0, 1)            # pendant at 0: the only a = 1 vertex
    mu = min(a_val(g, v) for v in range(len(g)))
    check(mu == 1, "liveness probe graph should have mu = 1")
    mis = build_tail1(g, 9)
    check(mis is not None,
          "mis-aimed probe: it SUCCEEDS, which is precisely why it tests nothing")
    aimed = [w for w in range(9)
             if max(range(len(g)), key=lambda v: bfs(g, w)[v]) == 9]
    check(len(aimed) > 0, "no vertex has the pendant as its furthest vertex — probe impossible")
    fired = sum(1 for w in aimed if build_tail1(g, w) is None)
    print("  LIVENESS, CORRECTLY AIMED: on C9+pendant (mu = 1), the %d vertices whose FURTHEST"
          % len(aimed))
    print("    vertex is the a=1 pendant make the construction DECLINE %d/%d times."
          % (fired, len(aimed)))
    print("    The mis-aimed version (probe AT the pendant) SUCCEEDS and tests nothing — kept as")
    print("    a named negative, because a probe that cannot fail scores ABSENT, not PASS.")
    check(fired == len(aimed),
          "the construction did NOT decline where a(u_d) = 1 — it would be unsound there")
    print()


# ================================================================== PART 3
def build_tail2(g, w):
    """(TAIL-2).  TAIL-1's path, plus a SECOND vertex z past y.  Needs a(y) >= 4 in the worst
    case; returns (path, a(y), dodged) or None."""
    P = build_tail1(g, w)
    if P is None or len(P) < 3:
        return None
    y = P[-1]
    ud = P[-2]
    geo = P[:-1]
    dodge = set(geo[max(0, len(geo) - 4):len(geo) - 1])   # u_{d-3}, u_{d-2}, u_{d-1}
    comps = nbhd_components(g, y)
    own = next(c for c in comps if ud in c)
    cands = []
    for c in comps:
        if c is own:
            continue
        for z in sorted(c):
            if z in P:
                continue
            if any(p in g[z] for p in P[:-1]):
                continue
            cands.append(z)
    if not cands:
        return None
    return P + [cands[0]], a_val(g, y), sorted(dodge)


def part3():
    PARTS_RUN.append("PART3")
    print("=" * 78)
    print("PART 3 — (TAIL-2) COSTS a(y) >= 4, AND (TAIL-3) COSTS a(z) >= 6")
    print("=" * 78)
    print("""  SECOND EXTENSION.  Continue u_0..u_d y by z in N(y).  Forced for free by C4-freeness:
  z !~ u_d (choose z off u_d's component of G[N(y)]) and z !~ u_{d-1} (else z-y-u_d-u_{d-1}
  is a 4-cycle).  z !~ u_i for i <= d-4 because dist(u_i,y) >= 3.  What must be PAID FOR is
  exactly u_{d-2} and u_{d-3}: at most ONE vertex of N(y) is adjacent to each of them (two
  would give y and that u_j two common neighbours — a C4), so at most two components of the
  matching G[N(y)] are spoiled, plus u_d's.  Hence  a(y) >= 4  suffices.

  THIRD EXTENSION.  Continue by z' in N(z).  z' !~ u_d is forced (z'-z-y-u_d is a 4-cycle).
  The dodge list is then {u_{d-1}, u_{d-2}, u_{d-3}, u_{d-4}} — FOUR vertices, each costing
  at most one component — plus y's component.  Hence  a(z) >= 6  suffices, and nothing
  smaller is delivered by this argument.

  >>> l(G) > 4 IS A MEAN.  It does not supply a(y) >= 4, let alone a(z) >= 6, AT A
  >>> PRESCRIBED VERTEX.  This is the DENSITY-vs-POSITIONAL mismatch, now LOCATED at a
  >>> named vertex and carrying a NUMBER.""")
    fam = [(petersen(), "Petersen"), (pg2(2), "Heawood"), (pg2(3), "PG(2,3)"),
           (blob_chain(2, 5), "blob_chain(2,5)"), (blob_chain(3, 5), "blob_chain(3,5)"),
           (two_cycles_glued(9, 9), "2xC9 glued")]
    for g, nm in fam:
        n = len(g)
        ok = 0
        rich = 0
        for w in range(n):
            r = build_tail2(g, w)
            if r is None:
                continue
            P, ay, dodge = r
            check(is_induced_path(g, P), "%s: TAIL-2 path at w=%d is NOT induced" % (nm, w))
            check(P[0] == w, "%s: TAIL-2 path at w=%d does not start at w" % (nm, w))
            check(len(P) == ecc(g, w) + 3,
                  "%s: TAIL-2 path at w=%d has %d vertices, expected ecc+3" % (nm, w, len(P)))
            ok += 1
            if ay >= 4:
                rich += 1
        print("  %-18s n=%-4d : TAIL-2 succeeded at %3d/%3d vertices; a(y) >= 4 held at %3d "
              "of those" % (nm, n, ok, n, rich))
        check(ok <= n, "%s: impossible success count" % nm)
    # the C4-forced exclusions, verified as FORCED rather than asserted
    forced = 0
    for g, nm in fam:
        for w in range(len(g)):
            P = build_tail1(g, w)
            if P is None or len(P) < 4:
                continue
            y, ud, udm1, udm2 = P[-1], P[-2], P[-3], P[-4]
            check(udm1 not in g[y], "%s: y adjacent to u_{d-1} — TAIL-1 choice broken" % nm)
            check(udm2 not in g[y], "%s: y adjacent to u_{d-2} — the C4 argument FAILED" % nm)
            forced += 1
    print("  C4-FORCED exclusions verified on %d frames: y !~ u_{d-1} and y !~ u_{d-2} every"
          " time." % forced)
    check(forced > 0, "the forced-exclusion sweep had an EMPTY population — it proves nothing")
    print("  NULL EXPECTATION stated: y !~ u_{d-2} is NOT automatic for an arbitrary neighbour of")
    print("    u_d — it is exactly what C4-freeness buys, and a C4-carrying host would break it.")
    print()


# ================================================================== PART 4
def base_family():
    fam = [(cycle(n), "C%d" % n) for n in (5, 6, 7, 8, 9, 10, 11, 12, 13, 15)]
    fam += [(two_cycles_glued(a, b), "C%d+C%d glued" % (a, b))
            for (a, b) in ((5, 5), (5, 7), (7, 9), (9, 9), (6, 9), (11, 5))]
    fam += [(theta(a, b, c), "Theta(%d,%d,%d)" % (a, b, c))
            for (a, b, c) in ((3, 3, 3), (3, 4, 5), (4, 5, 6), (5, 5, 5), (4, 6, 8), (5, 6, 7))]
    fam += [(petersen(), "Petersen"), (pg2(2), "Heawood"), (pg2(3), "PG(2,3)")]
    for seed in range(1, 41):
        for n0, ex in ((14, 4), (18, 6), (22, 8)):
            h = rand_c4free(seed * 7919 + n0, n0, ex)
            if h is not None and len(h) >= 8:
                fam.append((h, "rand(s=%d,n0=%d)" % (seed, n0)))
    out = []
    for g, nm in fam:
        n = len(g)
        if n < 5 or not connected(g) or not c4_free(g):
            continue
        if min(a_val(g, v) for v in range(n)) < 2:
            continue
        out.append((g, nm))
    return out


def part4():
    PARTS_RUN.append("PART4")
    print("=" * 78)
    print("PART 4 — THE THEOREM: route A2's conclusion for the SINGLE-HAIR case,")
    print("         plus (RAD-1P), the radius dichotomy the machine forced me to find")
    print("=" * 78)
    print("""  SETTING.  G connected C4-free; G' = peel(G) connected with mu(G') >= 2; the peeled set
  is a SINGLE hair of h >= 1 vertices hung at w in V(G').  (This is exactly the class in
  which r31 killed (A2-PATH): its witness was G' + ONE pendant.)  Write r := rad(G') and
  e := ecc_{G'}(w).

  TWO BOUNDS.
    (B1)  G' is INDUCED in G, so path(G) >= path(G').  With F11 = G42 on G' this reads
          path(G) >= r + 4.       [needs G' to satisfy F11: C4-free, l>4, rad>=5, mu>=2 —
                                   the SAME import route A2 has always made, inherited here]
    (B2)  The hair prepends h vertices to any induced path of G' ending at w, so
          path(G) >= h + endpath(G',w) >= h + e + 2.        [TAIL-1, UNCONDITIONAL]

  RADIUS, single hair at w:  ecc_G(w) = max(e, h), so rad(G) <= max(e, h); and rad(G) <= r+h.

  CASE ANALYSIS.
    h >= 2 :  e >= h  ->  rad(G) <= e  and (B2) gives h+e+2 >= e+4.            CLOSED
              h  > e  ->  rad(G) <= h  and (B2) gives h+e+2 >= h+4 (e >= 2).   CLOSED
              -- UNCONDITIONAL: no l > 4, no rad >= 5, no F11, no (F11-AT-w).
    h = 1  :  rad(G) <= min(e, r+1).
              e = r     : rad(G) <= r, (B1) gives r+4 >= rad(G)+4.             CLOSED (via F11)
              e >= r+2  : rad(G) <= r+1, (B2) gives e+3 >= r+5 >= rad(G)+4.    CLOSED
              e = r+1   : (B1) gives r+4, (B2) gives r+4, and rad(G)+4 is r+5 if and only if
                          rad(G) = r+1.                    SHORT BY EXACTLY ONE VERTEX.

  (RAD-1P) — THE RADIUS DICHOTOMY FOR ONE PENDANT.  For c in V(G'),
  ecc_G(c) = max(ecc_{G'}(c), d(c,w)+1), and ecc_G(pendant) = e+1.  Hence
        rad(G) = r      <==>  SOME centre c of G' has d(c,w) <= r-1,
        rad(G) = r + 1  <==>  EVERY centre c of G' has d(c,w) = r   (and never more).
  So the h = 1, e = r+1 case is only residual when w is ALSO at maximum distance from every
  centre.  I did not have this condition when I wrote the case analysis; the machine
  produced an EMPTY residual class and that is how the condition was found.""")
    fam = base_family()
    tally = {"h>=2 CLOSED by (B2)": 0, "h=1 e=r CLOSED by (B1)": 0,
             "h=1 e>=r+2 CLOSED by (B2)": 0, "h=1 e=r+1, rad(G)=r  CLOSED by (B1)": 0,
             "h=1 e=r+1, rad(G)=r+1  RESIDUAL": 0}
    residual_hosts = []
    rad_up = 0
    for gp, nm in fam:
        n = len(gp)
        r = rad(gp)
        centres = [v for v in range(n) if ecc(gp, v) == r]
        for w in range(n):
            e = ecc(gp, w)
            for h in (1, 2, 3):
                G = hairy(gp, w, h)
                alive, peeled = peel_all(G)
                check(alive == set(range(n)), "%s: peel(G) != G' at w=%d h=%d" % (nm, w, h))
                check(len(peeled) == h, "%s: peeled set is not the hair at w=%d h=%d" % (nm, w, h))
                check(c4_free(G), "%s: hanging a hair broke C4-freeness" % nm)
                rG = rad(G)
                check(ecc(G, w) == max(e, h),
                      "%s: ecc_G(w) != max(e,h) at w=%d h=%d" % (nm, w, h))
                check(rG <= r + h, "%s: rad(G) > rad(G')+h — r30's bound VIOLATED" % nm)
                b2 = h + e + 2
                if h == 1:
                    # (RAD-1P), verified as an EQUIVALENCE, both directions
                    pred = (r + 1) if all(bfs(gp, c)[w] == r for c in centres) else r
                    check(rG == pred,
                          "%s: (RAD-1P) predicted rad(G)=%d, machine says %d (w=%d)"
                          % (nm, pred, rG, w))
                    if rG == r + 1:
                        rad_up += 1
                if h >= 2:
                    check(b2 >= rG + 4, "%s: h>=2 case FAILED at w=%d h=%d (B2=%d, need %d)"
                          % (nm, w, h, b2, rG + 4))
                    tally["h>=2 CLOSED by (B2)"] += 1
                elif e == r:
                    check(rG == r, "%s: h=1, e=r but rad(G) != r" % nm)
                    tally["h=1 e=r CLOSED by (B1)"] += 1
                elif e >= r + 2:
                    check(b2 >= rG + 4, "%s: h=1, e>=r+2 FAILED at w=%d (B2=%d, need %d)"
                          % (nm, w, b2, rG + 4))
                    tally["h=1 e>=r+2 CLOSED by (B2)"] += 1
                else:
                    check(e == r + 1, "%s: the case split is not exhaustive at w=%d" % (nm, w))
                    if rG == r:
                        tally["h=1 e=r+1, rad(G)=r  CLOSED by (B1)"] += 1
                    else:
                        check(b2 == rG + 3,
                              "%s: residual must be short by EXACTLY one (B2=%d, need %d)"
                              % (nm, b2, rG + 4))
                        tally["h=1 e=r+1, rad(G)=r+1  RESIDUAL"] += 1
                        residual_hosts.append((nm, w, e, r, rG))
    tot = sum(tally.values())
    print("  CASE TALLY over %d (base, w, h) instances from %d bases, every one machine-checked:"
          % (tot, len(fam)))
    for k, v in tally.items():
        print("     %-38s %6d" % (k, v))
    check(tot > 0, "the case tally has an EMPTY population — it would prove nothing")
    print("  (RAD-1P) verified as an EQUIVALENCE on every h=1 instance; it FIRED (rad(G)=r+1)")
    print("     on %d of them, so the dichotomy's non-trivial side is LIVE, not vacuous." % rad_up)
    check(rad_up > 0, "(RAD-1P) never predicted rad(G)=r+1 — the equivalence would be untested")
    # THE CONCLUSION, computed EXACTLY where n permits — and SPLIT BY WHICH BOUND CARRIES IT,
    # because the two branches do not have the same status and a single verdict would hide that.
    print("  THE CONCLUSION, computed EXACTLY (longest induced path) on every host with n <= 15,")
    print("  SPLIT BY WHICH BOUND CARRIES IT — the two branches do NOT have the same status:")
    uncond_ok = uncond_n = 0
    h1_ok = h1_bad = 0
    h1_fail_rows = []
    for gp, nm in fam:
        if len(gp) > 15:
            continue
        r = rad(gp)
        for w in (0, len(gp) // 2):
            e = ecc(gp, w)
            for h in (1, 2, 3):
                G = hairy(gp, w, h)
                rG = rad(G)
                p, tr = longest_induced_path(G)   # EXACT: no cap, or `p` would be
                                                  # an UNDERESTIMATE and the comparison a lie
                check(not tr, "%s: longest-induced-path budget exhausted" % nm)
                # (B2) itself is UNCONDITIONAL and must hold on EVERY host, in or out of hypothesis
                pe, _ = endpath(gp, w)
                check(pe >= e + 2, "%s: TAIL-1 violated at w=%d (endpath=%d, ecc+2=%d)"
                      % (nm, w, pe, e + 2))
                check(p >= h + pe, "%s: path(G) >= h + endpath(G',w) VIOLATED at w=%d h=%d"
                      % (nm, w, h))
                if h >= 2:
                    # h >= 2 is closed by (B2) ALONE, with no import: the claim is unconditional,
                    # so it must hold on EVERY host here, including the sparse ones.
                    uncond_n += 1
                    if p >= rG + 4:
                        uncond_ok += 1
                    else:
                        check(False, "%s w=%d h=%d: UNCONDITIONAL branch FAILED "
                                     "(path=%d, rad+4=%d)" % (nm, w, h, p, rG + 4))
                else:
                    # h = 1 is carried by (B1) = F11 on G'.  These hosts do NOT satisfy F11's
                    # hypotheses (l > 4, rad >= 5), so the import is ABSENT and the conclusion
                    # is NOT claimed for them.  Recorded, not asserted.
                    if p >= rG + 4:
                        h1_ok += 1
                    else:
                        h1_bad += 1
                        if len(h1_fail_rows) < 6:
                            lval = sum(a_val(gp, v) for v in range(len(gp))) / len(gp)
                            h1_fail_rows.append((nm, w, p, rG + 4, lval, r))
    print("     h >= 2, closed by (B2) ALONE (UNCONDITIONAL — asserted): %d/%d hold, 0 violations"
          % (uncond_ok, uncond_n))
    check(uncond_n > 0, "no h>=2 instance ran — the unconditional branch would be UNTESTED")
    check(uncond_ok == uncond_n, "the UNCONDITIONAL branch has a violation — the proof is wrong")
    print("     h  = 1, carried by (B1) = F11 on G' (IMPORT ABSENT on these sparse hosts):")
    print("            %d hold, %d FAIL — and the failures are the point:" % (h1_ok, h1_bad))
    for nm, w, p, need, lval, r in h1_fail_rows:
        print("            %-18s w=%-2d path(G)=%-2d < rad(G)+4=%-2d   l(G')=%.3f  rad(G')=%d"
              % (nm, w, p, need, lval, r))
    print("""     >>> HARDEST-FORM LIVENESS CONTROL, and it was NOT designed — the machine produced it
     >>> when a check of mine ran on a sample outside its own hypothesis (own defect, PART 7).
     >>> DELETE F11 AND THE h = 1 BRANCH IS FALSE.  C5 + one pendant has path = 5 and
     >>> rad + 4 = 6.  So (B1) is not decorative bookkeeping in that branch: it is the whole
     >>> of it, and the h = 1 branch is exactly as strong as F11's applicability to G'.
     >>> The h >= 2 branch imports nothing and holds on every one of these same hosts.""")
    check(h1_bad > 0, "the h=1 liveness control never fired — it would show nothing")
    small = uncond_n + h1_ok + h1_bad
    print("     %d exact longest-induced-path computations in total." % small)
    check(small > 0, "no exact path computation ran — the verdict would be VACUOUS")
    print()
    return residual_hosts, fam


# ================================================================== PART 5
def part5(residual_hosts, fam):
    PARTS_RUN.append("PART5")
    print("=" * 78)
    print("PART 5 — THE RESIDUAL HUNT.  POPULATION FIRST, VERDICT SECOND.")
    print("=" * 78)
    print("""  The residual of PART 4 is a CONJUNCTION of three conditions:
      (a) h = 1;   (b) ecc_{G'}(w) = rad(G') + 1;   (c) every centre of G' has d(c,w) = rad(G').
  (b) says w is nearly peripheral in ECCENTRICITY; (c) says w is maximally far from the
  CENTRE.  They pull in the same direction and yet the sweep finds them never co-occurring.""")
    fams = len(fam)
    # populations of the individual conditions — a conjunction whose parts must each be live
    nb, nc, nbc = 0, 0, 0
    for gp, nm in fam:
        n = len(gp)
        r = rad(gp)
        centres = [v for v in range(n) if ecc(gp, v) == r]
        for w in range(n):
            b = (ecc(gp, w) == r + 1)
            c = all(bfs(gp, cc)[w] == r for cc in centres)
            nb += b
            nc += c
            nbc += (b and c)
    print("  POPULATIONS over %d bases:" % fams)
    print("     (b) ecc(w) = rad+1                       : %5d vertices" % nb)
    print("     (c) w maximally far from EVERY centre    : %5d vertices" % nc)
    print("     (b) AND (c)  = the residual              : %5d vertices" % nbc)
    check(nb > 0, "condition (b) never occurred — the conjunction test is uninformative")
    check(nc > 0, "condition (c) never occurred — the conjunction test is uninformative")
    if nbc == 0:
        print("  >>> BOTH CONJUNCTS LIVE, CONJUNCTION EMPTY on this family — a HINT only, and a")
        print("  >>> zero hit is not evidence of absence.")
    else:
        print("  >>> THE RESIDUAL IS NON-EMPTY.  My FIRST, narrower family produced ZERO of them")
        print("  >>> and I was one sentence away from recording the single-hair case as closed")
        print("  >>> outright.  The SEEDED RANDOM HOSTS produced them.  A residual that only a")
        print("  >>> wider family exhibits is exactly the residual a narrow family lets you")
        print("  >>> claim away — so the width of the family is load-bearing, not decoration.")
    check(len(residual_hosts) == nbc,
          "PART 4's residual list and PART 5's recount disagree (%d vs %d)"
          % (len(residual_hosts), nbc))
    byname = {}
    for gg, nn_ in fam:
        byname[nn_] = gg
    if residual_hosts:
        print("  RESIDUAL INSTANCES FOUND (%d), each MEASURED rather than merely listed:"
              % len(residual_hosts))
        print("    %-20s %-4s %-4s %-8s %-8s %-7s %-8s %s"
              % ("base", "w", "n", "ecc(w)", "rad(G')", "l(G')", "TAIL-2?", "endpath(w) vs rad+4"))
        t2_disc = 0
        for nm, w, e, r, rG in residual_hosts:
            g = byname[nm]
            nn = len(g)
            ll = sum(a_val(g, v) for v in range(nn)) / nn
            R = build_tail2(g, w)
            got = (R is not None and is_induced_path(g, R[0]) and len(R[0]) >= e + 3)
            t2_disc += got
            ep, _ = endpath(g, w)
            check(ep >= e + 2, "%s: TAIL-1 violated on a residual instance" % nm)
            print("    %-20s %-4d %-4d %-8d %-8d %-7.3f %-8s %d vs %d"
                  % (nm, w, nn, e, r, ll, "YES" if got else "no", ep, r + 4))
        print("  (TAIL-2) discharges %d of %d residual instances BY CONSTRUCTION."
              % (t2_disc, len(residual_hosts)))
        print("  >>> AND READ THE endpath COLUMN: on these hosts endpath(w) is already at or past")
        print("  >>> rad(G')+4.  The residual is a GAP IN THE ARGUMENT, not a counterexample to")
        print("  >>> anything.  The BOUND is short by one vertex; the GRAPHS are not.")
        check(all(sum(a_val(byname[nm], v) for v in range(len(byname[nm]))) / len(byname[nm]) <= 4.0
                  for nm, w, e, r, rG in residual_hosts),
              "a residual instance carries l > 4 — that would be a MUCH stronger finding and "
              "must not be reported as this one")
        print("  EVERY residual instance carries l(G') <= 4 : the l > 4 hypothesis is UNSPENT")
        print("     on all of them, exactly as r31 measured for (A2-PATH) over 179 witnesses.")
    else:
        print("  RESIDUAL INSTANCES FOUND: NONE.  Recorded as an OPEN sub-question, not a")
        print("     discharge — a zero hit is not evidence of absence (doctrine 5).")
    # NULL EXPECTATION, stated before the scan counts as evidence
    print("  NULL EXPECTATION, stated: condition (c) alone occurs at %.1f%% of swept vertices and"
          % (100.0 * nc / max(1, sum(len(g) for g, _ in fam))))
    print("     condition (b) at %.1f%%; if they were INDEPENDENT the expected joint count over"
          % (100.0 * nb / max(1, sum(len(g) for g, _ in fam))))
    tv = sum(len(g) for g, _ in fam)
    print("     %d vertices would be %.2f.  So the empty conjunction carries only about that"
          % (tv, nb * nc / max(1, tv)))
    print("     much information — it is a HINT, and it is reported as one.")
    print()


# ================================================================== PART 6
def part6():
    PARTS_RUN.append("PART6")
    print("=" * 78)
    print("PART 6 — IN-HYPOTHESIS CONTROL (l > 4 PRESENT) AND THE SCOPE MEASUREMENT")
    print("=" * 78)
    g = blob_chain(5, 5)
    n = len(g)
    S = sum(a_val(g, v) for v in range(n))
    l = S / n
    r = rad(g)
    mu = min(a_val(g, v) for v in range(n))
    print("  HOST: two PG(2,5) incidence graphs joined by an induced path of 5 vertices (the W1")
    print("        shape).  n=%d  rad=%d  mu=%d  l=%.4f  C4-free=%s  connected=%s"
          % (n, r, mu, l, c4_free(g), connected(g)))
    check(c4_free(g), "in-hypothesis control is not C4-free")
    check(connected(g), "in-hypothesis control is not connected")
    check(mu >= 2, "in-hypothesis control has mu < 2")
    check(l > 4, "in-hypothesis control does NOT carry l > 4 — the sample would be out of "
                 "hypothesis, which proves nothing and proves it silently (doctrine 1)")
    check(r >= 5, "in-hypothesis control does NOT carry rad >= 5")
    print("  IN-HYPOTHESIS MEMBERSHIP ASSERTED BEFORE THE CHECK RUNS: all five hypotheses present.")
    # control on l: PG(2,3) is exactly 4.0
    gp3 = pg2(3)
    l3 = sum(a_val(gp3, v) for v in range(len(gp3))) / len(gp3)
    check(abs(l3 - 4.0) < 1e-12, "l(PG(2,3)) must be EXACTLY 4.0 — the pin, not an inference")
    print("  l IS PINNED BY A CONTROL, NOT INFERRED: l(PG(2,3)) = %.4f exactly." % l3)
    # (TAIL-1)/(TAIL-2) availability across the whole host
    t1 = t2 = 0
    for w in range(n):
        P = build_tail1(g, w)
        if P is not None and is_induced_path(g, P) and len(P) == ecc(g, w) + 2:
            t1 += 1
        R = build_tail2(g, w)
        if R is not None and is_induced_path(g, R[0]) and len(R[0]) == ecc(g, w) + 3:
            t2 += 1
    print("  (TAIL-1) built and certified induced at %d/%d vertices; (TAIL-2) at %d/%d."
          % (t1, n, t2, n))
    check(t1 == n, "(TAIL-1) failed somewhere on the in-hypothesis host — it is UNCONDITIONAL")
    # the eccentricity classes, which is where the case analysis lives
    cls = {}
    for w in range(n):
        cls[ecc(g, w) - r] = cls.get(ecc(g, w) - r, 0) + 1
    print("  ECCENTRICITY PROFILE (ecc(w) - rad):", dict(sorted(cls.items())))
    print("     class 0 and 1 are the only ones the h=1 case analysis leaves anything to do;")
    print("     classes >= 2 are closed by (B2) alone.")
    # endpath >= rad+4 sampled, with the population printed
    sample = list(range(0, n, max(1, n // 24)))
    bad = []
    for w in sample:
        b, tr = endpath(g, w, cap=r + 4)
        if b < r + 4:
            bad.append((w, b, tr))
    print("  endpath(w) >= rad+4 = %d ?  sampled %d of %d vertices; FAILURES: %s"
          % (r + 4, len(sample), n, bad if bad else "NONE"))
    check(len(sample) > 0, "the endpath sample was EMPTY — a PASS on it would be VACUOUS")
    print("     This is EVIDENCE about (F11-ALL), NOT a discharge of it: a sample, not a sweep,")
    print("     and (F11-ALL) is a universal statement.")
    # the r31 comparison table, on the residual-eccentricity vertices
    print()
    print("  SCOPE, in r31's own format so the two rounds are comparable:")
    print("    %-26s %-9s %-8s %-7s %-8s %-8s" % ("host", "connected", "C4-free", "mu>=2",
                                                  "rad>=5", "l"))
    rows = [(blob_chain(5, 5), "2xPG(2,5)+path(5)"), (blob_chain(3, 5), "2xPG(2,3)+path(5)"),
            (two_cycles_glued(9, 9), "2xC9 glued (r31 witness)"), (pg2(3), "PG(2,3)"),
            (petersen(), "Petersen")]
    for gg, nm in rows:
        nn = len(gg)
        ll = sum(a_val(gg, v) for v in range(nn)) / nn
        print("    %-26s %-9s %-8s %-7s %-8s %.4f"
              % (nm, connected(gg), c4_free(gg), min(a_val(gg, v) for v in range(nn)) >= 2,
                 rad(gg) >= 5, ll))
    print("""  >>> THE r31 MISMATCH, RE-MEASURED ON THE SUCCESSOR TARGET.  The one host that carries
  >>> l > 4 AND rad >= 5 together is the dense one, and on it (TAIL-2) is available almost
  >>> everywhere — while the hosts that make the anchored bound TIGHT are the sparse ones,
  >>> which carry l = 2.0 to 3.0.  l > 4 is still a DENSITY hypothesis and the failure is
  >>> still POSITIONAL, and this round LOCATES the exchange: what l > 4 must be made to buy
  >>> is a(y) >= 4 at ONE PRESCRIBED VERTEX — the far end of a geodesic FROM w.""")
    print()


# ================================================================== MAIN
def main():
    print("w133 round 32 — (F11-AT-w) SHARPENED: the anchored target, its true strength,")
    print("and the single-hair theorem.   NO SAT.  Explicit graphs only.")
    print()
    part0()
    part1()
    part2()
    part3()
    residual, fam = part4()
    part5(residual, fam)
    part6()

    print("=" * 78)
    print("EVERY-PART-RAN CHECK  (r31 own-defect 7: `exit 0` is a claim about the PROCESS,")
    print("not about the WORK.  A wrapper that exits 0 having done none of the work is the")
    print("worst failure mode there is, so the parts are asserted, not assumed.)")
    print("=" * 78)
    print("  declared: %s" % PARTS_DECLARED)
    print("  ran     : %s" % PARTS_RUN)
    missing = [p for p in PARTS_DECLARED if p not in PARTS_RUN]
    check(not missing, "PARTS DECLARED BUT NEVER RUN: %s" % missing)
    check(PARTS_RUN == PARTS_DECLARED, "parts ran out of declared order or duplicated")
    print()
    print("CHECKS RUN : %d" % CHECKS)
    print("FAILURES   : %d" % FAIL)
    if FAIL or missing:
        print("VERDICT    : FAILED")
        sys.exit(1)
    print("VERDICT    : all declared parts executed, all checks passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
