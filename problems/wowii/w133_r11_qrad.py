#!/usr/bin/env python3
"""
w133 round 11 (owner-w133) — (Q-RAD) fork: does C4-free /\ l > 4 force rad <= 4?

Answer produced here: NO.  Explicit witnesses are built and verified from scratch:
  (A) PG(2,5) point/line incidence graph            (baseline blob: C4-free, l = 6, rad = 3)
  (B) two blobs joined by a path of L internal vertices  (l > 4 and rad >= 5)
  (C) a chain of k blobs joined by paths of L internal vertices each
      (radius grows linearly in k while l stays > 4  ==>  rad unbounded under l > 4)

Everything is verified directly on the constructed graph: simplicity, connectivity,
C4-freeness (no two distinct vertices with two common neighbours), a(v) = d(v) - t(v)
AND a(v) recomputed as the independence number of G[N(v)] by brute force (they must
agree -- this is the F1 identity, re-checked, not assumed), l = (1/n) sum a(v) as an
exact fraction, and rad/diam by all-pairs BFS.

NO SAT.  No search over a large space: every graph here is an explicit construction.
"""
from fractions import Fraction
from collections import deque
from itertools import combinations

FAIL = 0


def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("FAIL:", msg)
    return cond


# ---------------------------------------------------------------- graph helpers
def adj_from_edges(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v, "loop"
        g[u].add(v)
        g[v].add(u)
    return g


def is_connected(g):
    n = len(g)
    seen = [False] * n
    dq = deque([0])
    seen[0] = True
    c = 1
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if not seen[w]:
                seen[w] = True
                c += 1
                dq.append(w)
    return c == n


def c4_free(g):
    """no two distinct vertices have two common neighbours (4-cycle as SUBGRAPH)"""
    n = len(g)
    for u in range(n):
        for v in range(u + 1, n):
            if len(g[u] & g[v]) >= 2:
                return False, (u, v, sorted(g[u] & g[v]))
    return True, None


def a_value_bruteforce(g, v):
    """independence number of G[N(v)] by brute force over subsets (deg is small here)"""
    nb = sorted(g[v])
    best = 0
    m = len(nb)
    for size in range(m, 0, -1):
        if size <= best:
            break
        for S in combinations(nb, size):
            ok = True
            for a, b in combinations(S, 2):
                if b in g[a]:
                    ok = False
                    break
            if ok:
                best = size
                break
        if best == size:
            break
    return best


def a_value_f1(g, v):
    """a(v) = d(v) - t(v) in a C4-free graph"""
    nb = sorted(g[v])
    t = sum(1 for a, b in combinations(nb, 2) if b in g[a])
    return len(nb) - t


def ecc_all(g):
    n = len(g)
    ecc = []
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for w in g[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    dq.append(w)
        assert min(dist) >= 0
        ecc.append(max(dist))
    return ecc


def report(name, g, verbose=True):
    n = len(g)
    check(is_connected(g), name + ": connected")
    ok, wit = c4_free(g)
    check(ok, name + ": C4-free (witness %r)" % (wit,))
    avals = []
    for v in range(n):
        a1 = a_value_f1(g, v)
        a2 = a_value_bruteforce(g, v)
        check(a1 == a2, "%s: F1 identity a=d-t at vertex %d (%d vs %d)" % (name, v, a1, a2))
        avals.append(a2)
    sa = sum(avals)
    l = Fraction(sa, n)
    ecc = ecc_all(g)
    rad, diam = min(ecc), max(ecc)
    if verbose:
        print("%-34s n=%-6d sum_a=%-7d l=%-10s (%.4f)  rad=%-3d diam=%-3d  min_a=%d"
              % (name, n, sa, str(l), float(l), rad, diam, min(avals)))
    return dict(n=n, sum_a=sa, l=l, rad=rad, diam=diam, min_a=min(avals), avals=avals)


# ------------------------------------------------- PG(2,q) incidence graph, q prime
def pg2_incidence(q):
    """point/line incidence graph of the projective plane over GF(q), q prime."""
    def normalize(vec):
        for i in range(3):
            if vec[i] % q:
                inv = pow(vec[i], q - 2, q)
                return tuple((c * inv) % q for c in vec)
        return None

    pts = set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if (a, b, c) == (0, 0, 0):
                    continue
                pts.add(normalize((a, b, c)))
    pts = sorted(pts)
    npts = len(pts)
    idx = {p: i for i, p in enumerate(pts)}
    # lines are indexed by the same normalized triples (dual); incidence = dot product 0
    edges = []
    for j, L in enumerate(pts):
        for p in pts:
            if (p[0] * L[0] + p[1] * L[1] + p[2] * L[2]) % q == 0:
                edges.append((idx[p], npts + j))
    n = 2 * npts
    return n, edges, npts


def blob(q):
    n, edges, npts = pg2_incidence(q)
    return n, edges


def chain_of_blobs(q, k, L):
    """k disjoint copies of the PG(2,q) incidence graph, consecutive copies joined by a
    path with L internal (new, degree-2) vertices.  Attachment vertices are vertex 0 and
    vertex 1 of each copy (distinct vertices, chosen non-adjacent -- both are points)."""
    bn, bedges = blob(q)
    edges = []
    off = []
    for i in range(k):
        o = i * bn
        off.append(o)
        edges += [(u + o, v + o) for (u, v) in bedges]
    n = k * bn
    for i in range(k - 1):
        left = off[i] + 1      # exit port of copy i
        right = off[i + 1] + 0  # entry port of copy i+1
        prev = left
        for _ in range(L):
            edges.append((prev, n))
            prev = n
            n += 1
        edges.append((prev, right))
    return adj_from_edges(n, edges)


def main():
    print("=== (A) baseline blob: PG(2,q) incidence graphs ===")
    for q in (3, 5):
        n, edges = blob(q)
        g = adj_from_edges(n, edges)
        r = report("PG(2,%d) incidence" % q, g)
        if q == 5:
            check(r["l"] == 6, "PG(2,5): l = 6 exactly")
            check(r["rad"] == 3 and r["diam"] == 3, "PG(2,5): rad = diam = 3")
        if q == 3:
            check(r["l"] == 4, "PG(2,3): l = 4 exactly (the boundary control, NOT > 4)")

    print()
    print("=== (B) two blobs joined by a path: l > 4 AND rad >= 5 ===")
    for L in (5, 10, 15, 20, 30):
        g = chain_of_blobs(5, 2, L)
        r = report("2 x PG(2,5) + path(L=%d)" % L, g)
        check(r["l"] > 4, "L=%d: l > 4" % L)
        if L >= 5:
            check(r["rad"] >= 5, "L=%d: rad >= 5" % L)
        check(r["min_a"] >= 2, "L=%d: no a=1 vertex (F4 form holds)" % L)

    print()
    print("=== (C) chains: radius grows without bound while l stays > 4 ===")
    for k in (2, 3, 4, 6, 8):
        L = 10
        g = chain_of_blobs(5, k, L)
        r = report("%d x PG(2,5) chained, L=%d" % (k, L), g)
        check(r["l"] > 4, "k=%d: l > 4" % k)
        check(r["rad"] >= 5, "k=%d: rad >= 5" % k)

    print()
    print("=== (D) the smallest explicit witness we certify, with its exact data ===")
    g = chain_of_blobs(5, 2, 5)
    r = report("WITNESS W1 = 2 x PG(2,5) + path(L=5)", g)
    print("    exact l = %s = %.6f ;  rad = %d ;  diam = %d ; n = %d"
          % (r["l"], float(r["l"]), r["rad"], r["diam"], r["n"]))
    # a-value histogram
    hist = {}
    for a in r["avals"]:
        hist[a] = hist.get(a, 0) + 1
    print("    a-value histogram:", dict(sorted(hist.items())))

    print()
    print("=== (E) are these witnesses HARD instances of (G+k) k=2 (path >= rad+4)? ===")
    print("    A geodesic is an induced path, so path(G) >= diam(G)+1 ALWAYS.")
    print("    Hence path >= rad+4 is at risk ONLY when diam+1 < rad+4, i.e. diam <= rad+2.")
    for (k, L) in ((2, 5), (2, 30), (4, 10)):
        g = chain_of_blobs(5, k, L)
        n = len(g)
        ecc = ecc_all(g)
        rad, diam = min(ecc), max(ecc)
        # certify path >= diam+1 by exhibiting an actual diametral geodesic and checking
        # it is induced
        s = ecc.index(diam)
        dist = [-1] * n
        dist[s] = 0
        par = [-1] * n
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for w in g[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    dq.append(w)
        t = dist.index(diam)
        P = []
        cur = t
        while cur != -1:
            P.append(cur)
            cur = par[cur]
        induced = all((P[j] in g[P[i]]) == (abs(i - j) == 1)
                      for i in range(len(P)) for j in range(i + 1, len(P)))
        check(induced, "k=%d L=%d: diametral geodesic is induced" % (k, L))
        check(len(P) == diam + 1, "k=%d L=%d: geodesic length" % (k, L))
        hard = diam <= rad + 2
        print("    k=%d L=%d: rad=%d diam=%d  path >= %d  vs rad+4 = %d   -> %s"
              % (k, L, rad, diam, len(P), rad + 4,
                 "HARD instance" if hard else "trivially satisfied (diam > rad+2)"))
        check(not hard, "k=%d L=%d: witness is diameter-heavy, NOT a hard instance" % (k, L))

    print()
    print("    CONCLUSION (E): the (Q-RAD) witnesses settle NON-EMPTINESS of")
    print("    {C4-free, l>4, rad>=5} but every one of them has diam >> rad+2, so none is a")
    print("    hard instance of (G+k) k=2.  The refined open fork is (Q-RAD'):")
    print("    does there exist a C4-free graph with l>4, rad>=5 AND diam <= rad+2 ?")

    print()
    print("FAILURES:", FAIL)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
