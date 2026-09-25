#!/usr/bin/env python3
"""
w133 round 15 — KEY for the PART 6 held-out table of the SECOND cross-family S3 round on
section 24 (brief `prompts/w133_S3_R24_v6_qwen.md`, judge = Qwen web), plus two owner
verification items this slice owes.

Nothing here is read off any engine report.  Every graph is rebuilt from a recipe or from
an edge list constructed IN THIS FILE, and C4-freeness is asserted BEFORE any statistic is
read off it.  The builders (pg2, chain, add_leaf, psl2, induced_path_exists,
longest_induced_path) are the ones this owner wrote and ran to exit 0 in round 14
(`w133_r14_heldout.py`); they are reproduced verbatim so this script stands alone.

Sections
  [A] PG(2,5) and W1 rebuilt and re-verified (the base of rows K1, K2).
  [B] K1 — the L = 9 chain: n, sum a, l.
  [C] K2 — W1 + three leaves: n, sum a, l, and site-independence over ALL sites.
  [D] K3 — W2 = Cay(PSL(2,11),S): distance distribution from a vertex (vertex-transitive,
      so this is a graph invariant).  NON-hand-derivable.
  [E] K4 — the bespoke 13-vertex C4-free graph Y: a-vector, l, mu, rad, diam and the EXACT
      longest induced path with a witness.  NON-hand-derivable (exact, by subset
      enumeration on n = 13 = 8192 subsets, which is not a large space).
  [F] K5 — PG(2,3) incidence: largest k for which an induced P_k is certified to EXIST and
      the smallest k for which non-existence is certified, both node-capped and two-sided.
      NON-hand-derivable.
  [G] Owner item — the D3_B S2 survivor's "a(u3) >= 3 is EQUIVALENT to escaping Case 2":
      the forward direction is proved by hand in the ledger; the CONVERSE is refuted here
      by an explicit C4-free instance.  This is why S2 enters the draft one-directional.

No SAT.  No exhaustive search of a large space.  Hard node caps on every DFS.
"""

import sys, time
from itertools import combinations
from collections import deque

FAILS = []
NCHECK = 0
T0 = time.time()

FAILS = []
NCHECK = 0


def check(cond, label, extra=""):
    global NCHECK
    NCHECK += 1
    if cond:
        print("  PASS  %s%s" % (label, ("   [%s]" % extra) if extra else ""))
    else:
        print("  FAIL  %s%s" % (label, ("   [%s]" % extra) if extra else ""))
        FAILS.append(label)


# ----------------------------------------------------------------- graph core
def mk(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v, "loop"
        assert 0 <= u < n and 0 <= v < n, "vertex out of range"
        adj[u].add(v)
        adj[v].add(u)
    return adj


def c4_violations(adj, cap=10):
    """C4-free (project convention): no two distinct vertices with >= 2 common
    neighbours.  Returns up to `cap` violating pairs."""
    n = len(adj)
    bad = []
    for u in range(n):
        for v in range(u + 1, n):
            if len(adj[u] & adj[v]) >= 2:
                bad.append((u, v))
                if len(bad) >= cap:
                    return bad
    return bad


def connected(adj):
    n = len(adj)
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return len(seen) == n


def indep_number(adj, S):
    """Brute-force independence number of the induced subgraph on S.  Only ever
    called with |S| <= 8 here, so this is 2^8 work at worst."""
    S = list(S)
    assert len(S) <= 12, "indep_number called on a big set"   # r15: raised from 8;
    # round-14's cap of 8 fired on W1 + three leaves at the SAME attachment vertex
    # (degree 7 + 3 = 10).  2^12 with early break is still not a large space.
    best = 0
    for r in range(len(S), -1, -1):
        if r <= best:
            break
        for T in combinations(S, r):
            if all(b not in adj[a] for a, b in combinations(T, 2)):
                best = max(best, r)
                break
    return best


def a_value(adj, v):
    """a(v) = alpha(G[N(v)]).  Computed two independent ways and cross-checked:
    (1) brute force independence number; (2) component count, valid because
    C4-freeness makes G[N(v)] a matching plus isolated vertices."""
    S = sorted(adj[v])
    brute = indep_number(adj, S)
    # component count of the matching G[N(v)]
    Sset = set(S)
    seen = set()
    comps = 0
    maxdeg = 0
    for s in S:
        deg_in = len(adj[s] & Sset)
        maxdeg = max(maxdeg, deg_in)
        if s not in seen:
            comps += 1
            stack = [s]
            seen.add(s)
            while stack:
                t = stack.pop()
                for w in adj[t] & Sset:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
    assert maxdeg <= 1, "G[N(%d)] is not a matching -- graph is not C4-free" % v
    assert brute == comps, "a(%d): brute %d != comps %d" % (v, brute, comps)
    return brute


def mass(adj):
    return sum(a_value(adj, v) for v in range(len(adj)))


def a_hist(adj):
    h = {}
    for v in range(len(adj)):
        h[a_value(adj, v)] = h.get(a_value(adj, v), 0) + 1
    return dict(sorted(h.items()))


def ecc_all(adj):
    n = len(adj)
    ecc = []
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    q.append(w)
        assert min(dist) >= 0, "disconnected"
        ecc.append(max(dist))
    return ecc


def frac(p, q):
    from math import gcd
    g = gcd(p, q)
    return "%d/%d" % (p // g, q // g)


# --------------------------------------------------- projective plane PG(2,q)
def pg2(q):
    """Point/line incidence graph of PG(2,q) over GF(q), q PRIME.
    Points 0..N-1, lines N..2N-1 with N = q^2+q+1.  Incidence a*x+b*y+c*z = 0.
    Every axiom is verified here, not assumed."""
    assert q in (2, 3, 5, 7, 11), "prime q only"
    pts = []
    seen = set()
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if (x, y, z) == (0, 0, 0):
                    continue
                # normalise: first non-zero coordinate scaled to 1
                v = (x, y, z)
                lead = next(c for c in v if c % q != 0)
                inv = pow(lead, q - 2, q)
                nv = tuple((c * inv) % q for c in v)
                if nv not in seen:
                    seen.add(nv)
                    pts.append(nv)
    N = q * q + q + 1
    assert len(pts) == N, "point count %d != %d" % (len(pts), N)
    idx = {p: i for i, p in enumerate(pts)}
    edges = []
    for i, P in enumerate(pts):
        for j, L in enumerate(pts):
            if sum(P[k] * L[k] for k in range(3)) % q == 0:
                edges.append((i, N + j))
    g = mk(2 * N, edges)
    # axioms, verified
    assert all(len(g[v]) == q + 1 for v in range(2 * N)), "not (q+1)-regular"
    for i in range(N):
        for j in range(i + 1, N):
            assert len(g[i] & g[j]) == 1, "two points not on exactly one line"
            assert len(g[N + i] & g[N + j]) == 1, "two lines not meeting once"
    return g, N, pts, idx


# ---------------------------------------------------------------- W1 family
def chain(base, nbase, L, attach_a, attach_b):
    """Two disjoint copies of `base` joined by a path with L NEW internal vertices,
    attached at vertex attach_a of copy A and attach_b of copy B."""
    edges = []
    for u in range(nbase):
        for v in base[u]:
            if u < v:
                edges.append((u, v))
                edges.append((u + nbase, v + nbase))
    off = 2 * nbase
    seq = [attach_a] + [off + i for i in range(L)] + [nbase + attach_b]
    for i in range(len(seq) - 1):
        edges.append((seq[i], seq[i + 1]))
    return mk(2 * nbase + L, edges)


def add_leaf(adj, p):
    n = len(adj)
    edges = [(u, v) for u in range(n) for v in adj[u] if u < v]
    edges.append((p, n))
    return mk(n + 1, edges)


def add_triangle_leaf(adj, u, v):
    n = len(adj)
    edges = [(a, b) for a in range(n) for b in adj[a] if a < b]
    edges += [(u, n), (v, n)]
    return mk(n + 1, edges)


# ----------------------------------------------- W2 = Cay(PSL(2,11), S)
def psl2(p, gens):
    """PSL(2,p) as SL(2,p)/{+-I}; Cayley graph on the generating set gens u gens^-1.
    The group is enumerated by brute force over the 2x2 matrices of determinant 1,
    which is p^4 = 14641 candidates for p = 11 -- cheap and fully explicit."""
    els = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        els.append((a, b, c, d))
    assert len(els) == p * (p * p - 1), "SL(2,%d) order %d" % (p, len(els))

    def norm(m):
        a, b, c, d = m
        neg = tuple((-x) % p for x in m)
        return min(m, neg)

    classes = sorted({norm(m) for m in els})
    assert len(classes) == p * (p * p - 1) // 2, "PSL order %d" % len(classes)
    ci = {m: i for i, m in enumerate(classes)}

    def mul(m, k):
        a, b, c, d = m
        e, f, g, h = k
        return ((a * e + b * g) % p, (a * f + b * h) % p,
                (c * e + d * g) % p, (c * f + d * h) % p)

    def inv(m):
        a, b, c, d = m
        return (d % p, (-b) % p, (-c) % p, a % p)

    S = set()
    for g in gens:
        a, b, c, d = g
        assert (a * d - b * c) % p == 1, "generator not in SL(2,%d)" % p
        S.add(norm(g))
        S.add(norm(inv(g)))
    ident = norm((1, 0, 0, 1))
    assert ident not in S, "identity in connection set"
    edges = set()
    for m in classes:
        i = ci[m]
        for s in S:
            j = ci[norm(mul(m, s))]
            if i != j:
                edges.add((min(i, j), max(i, j)))
    return mk(len(classes), sorted(edges)), len(classes), len(S)


# ------------------------------------------ capped DFS for an induced P_k
def induced_path_exists(adj, k, cap=400000):
    """Node-capped DFS for an induced path on exactly k vertices.
    Returns (True, witness) / (False, None) / ('CAP', None)."""
    n = len(adj)
    nodes = [0]

    def ext(path, used):
        if len(path) == k:
            return list(path)
        if nodes[0] > cap:
            return 'CAP'
        last = path[-1]
        capped = False
        for w in sorted(adj[last]):
            if w in used:
                continue
            # induced: w adjacent to nothing on the path except `last`
            if any(w in adj[u] for u in path[:-1]):
                continue
            nodes[0] += 1
            path.append(w)
            used.add(w)
            r = ext(path, used)
            path.pop()
            used.discard(w)
            if r == 'CAP':
                capped = True
            elif r:
                return r
        return 'CAP' if capped else None

    for s in range(n):
        r = ext([s], {s})
        if r == 'CAP':
            return ('CAP', None)
        if r:
            return (True, r)
    return (False, None)
def longest_induced_path(adj, cap_n=12):
    """Exact longest induced path by subset enumeration.  n <= 12 only: 2^12 = 4096
    subsets, which is not a large space."""
    n = len(adj)
    assert n <= cap_n, "refusing to enumerate subsets of a big graph"
    best = 0
    for r in range(n, 0, -1):
        if r <= best:
            break
        for S in combinations(range(n), r):
            Ss = set(S)
            deg = [len(adj[v] & Ss) for v in S]
            if max(deg) > 2 or deg.count(1) != 2 or deg.count(2) != r - 2:
                continue
            # connected check on the induced subgraph
            start = S[deg.index(1)]
            seen, stack = {start}, [start]
            while stack:
                t = stack.pop()
                for w in adj[t] & Ss:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
            if len(seen) == r:
                best = r
                break
    return best



def dist_from(adj, s):
    n = len(adj)
    d = [-1] * n
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                q.append(w)
    return d


# =============================================================== RUN
print("=" * 78)
print("w133 r15 -- held-out KEY for the second cross-family S3 round on section 24")
print("=" * 78)

# ---- [A] PG(2,5) and W1 ----------------------------------------------------
print("\n[A] PG(2,5) incidence and W1, rebuilt from GF(5) upward")
PG5, N5, _, _ = pg2(5)
check(len(PG5) == 62 and all(len(PG5[v]) == 6 for v in range(62)),
      "PG(2,5) incidence: n = 62, 6-regular")
check(c4_violations(PG5) == [], "PG(2,5) incidence is C4-free (asserted BEFORE any statistic)")
W1 = chain(PG5, 62, 5, 0, 0)
check(c4_violations(W1) == [], "W1 is C4-free (asserted BEFORE any statistic)")
check(connected(W1), "W1 connected")
h1 = a_hist(W1)
check(len(W1) == 129 and mass(W1) == 756 and h1 == {2: 5, 6: 122, 7: 2},
      "W1 reproduces round-14's verified profile",
      "n=%d sum_a=%d hist=%s" % (len(W1), mass(W1), h1))
tri = sum(1 for u in range(len(W1)) for v in W1[u] for w in W1[u]
          if u < v < w and w in W1[v])
check(tri == 0, "W1 has 0 triangles")

# ---- [B] K1 : the L = 9 chain ---------------------------------------------
print("\n[B] K1 -- the two-copy chain with L = 9 internal path vertices")
C9 = chain(PG5, 62, 9, 0, 0)
check(c4_violations(C9) == [], "L=9 chain is C4-free (asserted BEFORE any statistic)")
check(connected(C9), "L=9 chain connected")
n9, m9, hh9 = len(C9), mass(C9), a_hist(C9)
check(n9 == 133, "K1 n = 133", "got %d" % n9)
check(m9 == 764, "K1 sum_v a(v) = 764", "got %d" % m9)
check(hh9 == {2: 9, 6: 122, 7: 2}, "K1 a-histogram {2:9, 6:122, 7:2}", str(hh9))
print("      KEY K1 :  n = %d   sum_a = %d   l = %s = %.4f"
      % (n9, m9, frac(m9, n9), m9 / n9))

# ---- [C] K2 : W1 + three leaves -------------------------------------------
print("\n[C] K2 -- W1 with three leaves attached")
L3 = add_leaf(add_leaf(add_leaf(W1, 0), 1), 7)
check(c4_violations(L3) == [], "W1+3 leaves is C4-free (asserted BEFORE any statistic)")
n2, m2 = len(L3), mass(L3)
check(n2 == 132, "K2 n = 132", "got %d" % n2)
check(m2 == 762, "K2 sum_v a(v) = 762", "got %d" % m2)
print("      KEY K2 :  n = %d   sum_a = %d   l = %s = %.4f"
      % (n2, m2, frac(m2, n2), m2 / n2))
# site-independence, checked over EVERY single-leaf site and a spread of triples
masses = set()
for p in range(129):
    g = add_leaf(W1, p)
    assert c4_violations(g) == [], "leaf at %d broke C4-freeness" % p
    masses.add(mass(g))
check(masses == {758}, "one leaf: sum_a = 758 at ALL 129 sites (site-independent)", str(masses))
tri_masses = set()
for (p, q, r) in [(0, 1, 2), (0, 0, 0), (0, 62, 124), (5, 5, 9), (63, 64, 65)]:
    g = add_leaf(add_leaf(add_leaf(W1, p), q), r)
    assert c4_violations(g) == [], "triple %s broke C4-freeness" % str((p, q, r))
    tri_masses.add((len(g), mass(g)))
check(tri_masses == {(132, 762)},
      "three leaves: (n, sum_a) = (132, 762) for every tested site multiset, "
      "INCLUDING all three at the same vertex and two at adjacent vertices",
      str(tri_masses))

# ---- [D] K3 : W2 distance distribution ------------------------------------
print("\n[D] K3 -- W2 = Cay(PSL(2,11), S): distance distribution (NON-hand-derivable)")
GENS = [(5, 0, 2, 9), (1, 5, 0, 1), (1, 6, 10, 6)]
W2, n_w2, s_w2 = psl2(11, GENS)
check(n_w2 == 660 and s_w2 == 6, "W2: |PSL(2,11)| = 660, |S| = 6", "n=%d |S|=%d" % (n_w2, s_w2))
check(all(len(W2[v]) == 6 for v in range(660)), "W2 6-regular")
check(connected(W2), "W2 connected")
check(c4_violations(W2) == [], "W2 is C4-free (asserted BEFORE any statistic)")
tri2 = sum(1 for u in range(660) for v in W2[u] for w in W2[u]
           if u < v < w and w in W2[v])
check(tri2 == 0, "W2 triangle-free", "triangles=%d" % tri2)
e_w2 = sum(len(W2[v]) for v in range(660)) // 2
check(e_w2 == 1980, "|E(W2)| = 1980", "got %d" % e_w2)
dd = dist_from(W2, 0)
prof = {}
for v in range(660):
    prof[dd[v]] = prof.get(dd[v], 0) + 1
check(max(dd) == 5, "ecc = 5 from vertex 0", "got %d" % max(dd))
# vertex-transitivity spot-check: same profile from three more vertices
same = all({k: sum(1 for v in range(660) if dist_from(W2, s)[v] == k) for k in prof} == prof
           for s in (1, 17, 400))
check(same, "distance profile identical from vertices 1, 17, 400 (vertex-transitive)")
check(sum(prof.values()) == 660, "profile sums to 660")
print("      KEY K3 :  " + "  ".join("n%d=%d" % (k, prof[k]) for k in sorted(prof)))

# ---- [E] K4 : the bespoke 13-vertex graph Y --------------------------------
print("\n[E] K4 -- bespoke deterministic C4-free graph Y (greedy C4-free closure of C13)")
# Bespoke and fully deterministic: start from the 13-cycle and greedily add every pair
# in lexicographic order that keeps the graph C4-free.  No literature graph, nothing an
# engine could recall.  (Two-step circulants C13(1,k) were tried first and are NEVER
# C4-free -- i and i+k+1 always share the two neighbours i+1 and i+k -- so the assertion
# that guarded that attempt fired and the construction was replaced; recorded, not hidden.)
EY = [(i, (i + 1) % 13) for i in range(13)]
EY = sorted({(min(a, b), max(a, b)) for a, b in EY})
for i in range(13):
    for j in range(i + 1, 13):
        if (i, j) in EY:
            continue
        trial = mk(13, EY + [(i, j)])
        if c4_violations(trial) == []:
            EY = sorted(EY + [(i, j)])
Y = mk(13, EY)
check(c4_violations(Y) == [], "Y is C4-free (asserted BEFORE any statistic)")
check(connected(Y), "Y connected")
degs = sorted(len(Y[v]) for v in range(13))
avec = [a_value(Y, v) for v in range(13)]
ec = ecc_all(Y)
pathY = longest_induced_path(Y, cap_n=13)
print("      Y edge list (%d edges): %s" % (len(EY), " ".join("%d-%d" % e for e in EY)))
print("      KEY K4 :  degrees = %s" % degs)
print("      KEY K4 :  a-vector = %s   sum_a = %d   l = %s   mu = %d   rad = %d   diam = %d"
      % (avec, sum(avec), frac(sum(avec), 13), min(avec), min(ec), max(ec)))
print("      KEY K4 :  path(Y) = %d vertices (EXACT, subset enumeration over 2^13)" % pathY)
ok, wit = induced_path_exists(Y, pathY, cap=2000000)
check(ok is True, "a longest induced path of Y is exhibited", "witness %s" % (wit,))
no, _ = induced_path_exists(Y, pathY + 1, cap=2000000)
check(no is False, "and Y has NO induced path on %d vertices (two-sided)" % (pathY + 1))
print("      KEY K4 :  witness = %s" % (wit,))

# ---- [F] K5 : PG(2,3) incidence, longest induced path ----------------------
print("\n[F] K5 -- PG(2,3) incidence: two-sided induced-path certification")
PG3, N3, _, _ = pg2(3)
check(len(PG3) == 26 and all(len(PG3[v]) == 4 for v in range(26)),
      "PG(2,3) incidence: n = 26, 4-regular")
check(c4_violations(PG3) == [], "PG(2,3) incidence is C4-free (asserted BEFORE any statistic)")
CAP = 4000000
lo, hi_wit = 0, None
for k in range(7, 15):
    r, wit = induced_path_exists(PG3, k, cap=CAP)
    if r is True:
        lo, hi_wit = k, wit
        print("      induced P%-2d : EXISTS   witness %s" % (k, wit))
    elif r is False:
        print("      induced P%-2d : DOES NOT EXIST (search completed, no cap hit)" % k)
        check(lo == k - 1, "K5 two-sided: path(PG(2,3) incidence) = %d vertices" % lo)
        break
    else:
        print("      induced P%-2d : CAP HIT at %d nodes -- INCONCLUSIVE" % (k, CAP))
        check(False, "K5 inconclusive at k = %d -- row must be reworded" % k)
        break
print("      KEY K5 :  path(PG(2,3) incidence) = %d vertices, witness %s" % (lo, hi_wit))

# ---- [G] owner item: the S2 survivor's converse is FALSE -------------------
print("\n[G] owner item -- 'a(u3) >= 3 <=> escapes Case 2': the CONVERSE is refuted")
# u0=0 u1=1 u2=2 u3=3 y=4 x=5 z=6 p1=7 p2=8 p3=9
EZ = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (0, 6), (5, 7), (5, 8), (5, 9)]
Z = mk(10, EZ)
check(c4_violations(Z) == [], "Z is C4-free (asserted BEFORE any statistic)")
check(connected(Z), "Z connected")
dz = dist_from(Z, 0)
check(dz[3] == 3, "0-1-2-3 is a geodesic of length 3")
check(a_value(Z, 0) == 3, "a(u0) = 3", "got %d" % a_value(Z, 0))
check(a_value(Z, 5) == 4, "a(x) = 4 -- x = 5 is a usable side-neighbour of u0",
      "got %d" % a_value(Z, 5))
check(1 not in Z[5], "x is outside u1's component of G[N(u0)] (x !~ u1): x IS usable")
check(a_value(Z, 3) == 2, "a(u3) = 2 EXACTLY", "got %d" % a_value(Z, 3))
check(4 in Z[3] and 2 not in Z[4], "y = 4 is a usable side-neighbour of u3")
check(4 not in Z[5], "y !~ x -- the frame ESCAPES Case 2 while a(u3) = 2 < 3")
pz = longest_induced_path(Z, cap_n=10)
check(pz >= 7, "and path(Z) = %d >= 7, so no conflict with G37" % pz)

# =============================================================== SUMMARY
print("\n" + "=" * 78)
print("checks: %d   failures: %d   wall %.1fs" % (NCHECK, len(FAILS), time.time() - T0))
for f in FAILS:
    print("  FAILED: %s" % f)
print("=" * 78)
sys.exit(1 if FAILS else 0)
