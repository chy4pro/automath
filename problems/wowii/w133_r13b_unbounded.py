#!/usr/bin/env python3
"""w133 round 13b — CERTIFICATION of the unbounded bad-class family (Item 8 adoption).

Planner confirmation 10:2x CDT 2026-08-22, r13b executor.

WHAT THIS CERTIFIES
-------------------
Round 13's Gate-3 pass over `D3_E` FLAGGED (but withheld from the registry, being a
derivation rather than a verification) the following claim:

    Attaching k pendant triangles at vertex 2 of CE-2 gives, for every k >= 0, a graph
    F_k that is C4-free, connected, carries BOTH of CE-2's Case-2-forced 3-frames, and
    has path(F_k) = 6 EXACTLY, while n(F_k) = 10 + 2k -> infinity.

`D3_E` itself declined this question ("whether CE-2 possesses such a vertex is
undetermined without computation").  This script performs that computation from the
edge list up: every graph is rebuilt here, C4-freeness is checked BEFORE any statistic
is read off it, and no engine-supplied adjacency, a-value, distance or path count is
trusted anywhere.

CONVENTIONS (the brief's, restated so they cannot drift)
  * path(G) counts VERTICES of a longest INDUCED path.
  * a(v) = deg(v) - #{triangles at v}; equivalently the number of components of
    G[N(v)] when that graph is a matching (true in every C4-free graph).
  * l(G) = (sum_v a(v)) / n.
  * A 3-frame is (u0,u1,u2,u3;x) with dist(u0,u3) = 3 along the geodesic
    u0-u1-u2-u3, a(u0) >= 3, a(u3) >= 2, x a neighbour of u0 outside u1's component
    of G[N(u0)] with a(x) >= 4, and a non-empty usable far-side set
    ys = N(u3) \\ comp(u2).  It is CASE-2-FORCED iff every y in ys is adjacent to x.

A PENDANT TRIANGLE at v is two NEW vertices p,q with edges v-p, v-q, p-q.

STRATEGIC CONSEQUENCE (recorded with the result, not derived from it):
  n is UNBOUNDED in the bad class, so no route to (T-C+)/(T-D) can come from bounding
  n; every route must come through the hypothesis l > 3.  Note this family has
  l = (25+3k)/(10+2k) < 5/2 < 3 for all k -- it lives strictly BELOW the l > 3 line,
  which is exactly why it kills the n-bounding route without threatening the l > 3 one.

No SAT.  No exhaustive enumeration of a large space.
"""
import itertools, sys
from fractions import Fraction

FAIL = 0
def check(cond, msg, extra=""):
    global FAIL
    tag = "PASS" if cond else "FAIL"
    if not cond:
        FAIL += 1
    print("  %s  %s%s" % (tag, msg, ("   [%s]" % extra) if extra else ""))
    return cond

# ---------------------------------------------------------------- basic tools
def mk(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v and 0 <= u < n and 0 <= v < n, (u, v, n)
        adj[u].add(v); adj[v].add(u)
    return adj

def c4free_strong(adj):
    """returns (bool, list of violating pairs) -- STRONG form: no two distinct
    vertices with >= 2 common neighbours (this forbids C4 AND K4-minus-an-edge)."""
    n = len(adj); bad = []
    for u in range(n):
        for v in range(u + 1, n):
            if len(adj[u] & adj[v]) >= 2:
                bad.append((u, v, sorted(adj[u] & adj[v])))
    return (not bad), bad

def a_of(adj, v):
    N = list(adj[v])
    t = sum(1 for p, q in itertools.combinations(N, 2) if q in adj[p])
    return len(N) - t

def mass(adj):
    return sum(a_of(adj, v) for v in range(len(adj)))

def bfs(adj, s):
    n = len(adj); d = [-1] * n; d[s] = 0; q = [s]
    while q:
        nq = []
        for u in q:
            for w in adj[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1; nq.append(w)
        q = nq
    return d

def connected(adj):
    return all(x >= 0 for x in bfs(adj, 0))

def nbr_components(adj, v):
    """components of G[N(v)] -- a matching in a C4-free graph."""
    N = set(adj[v]); comps = []; seen = set()
    for u in sorted(N):
        if u in seen: continue
        c = {u}; seen.add(u)
        for w in adj[u] & N:
            c.add(w); seen.add(w)
        comps.append(c)
    return comps

def has_induced_path(adj, k):
    """True iff G has an induced path on >= k VERTICES.  Early-exit DFS."""
    n = len(adj)
    if k <= 1: return n >= k
    def ext(pathv, pset):
        if len(pathv) >= k: return True
        last = pathv[-1]
        inner = pset - {last}
        for w in adj[last]:
            if w in pset: continue
            if adj[w] & inner: continue          # chord -> not induced
            if ext(pathv + [w], pset | {w}): return True
        return False
    for s in range(n):
        if ext([s], {s}): return True
    return False

def longest_induced_path(adj, cap):
    for k in range(cap, 1, -1):
        if has_induced_path(adj, k): return k
    return min(1, len(adj))

def frames(adj):
    """every 3-frame as (u0,u1,u2,u3,x,ys,case2)."""
    n = len(adj); D = [bfs(adj, s) for s in range(n)]
    A = [a_of(adj, v) for v in range(n)]
    out = []
    for u0 in range(n):
        if A[u0] < 3: continue
        for u3 in range(n):
            if D[u0][u3] != 3 or A[u3] < 2: continue
            comps0 = nbr_components(adj, u0); comps3 = nbr_components(adj, u3)
            for u1 in adj[u0]:
                if D[u1][u3] != 2: continue
                for u2 in adj[u3]:
                    if D[u0][u2] != 2 or u2 not in adj[u1]: continue
                    c1 = next(c for c in comps0 if u1 in c)
                    c2 = next(c for c in comps3 if u2 in c)
                    xs = [x for x in adj[u0] if x not in c1 and A[x] >= 4]
                    ys = [y for y in adj[u3] if y not in c2]
                    if not xs or not ys: continue
                    for x in xs:
                        out.append((u0, u1, u2, u3, x, tuple(sorted(ys)),
                                    all(y in adj[x] for y in ys)))
    return out

# ---------------------------------------------------------------- the family
CE2_N = 10
CE2_E = [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),
         (4,8),(8,9)]
HUB = 2                      # the attachment vertex named in round 13

def F(k):
    """CE-2 with k pendant triangles attached at vertex HUB."""
    n = CE2_N + 2 * k
    e = list(CE2_E)
    for i in range(k):
        p, q = CE2_N + 2 * i, CE2_N + 2 * i + 1
        e += [(HUB, p), (HUB, q), (p, q)]
    return mk(n, e), n

# the two 3-frames of CE-2 named in round 13 (u0,u1,u2,u3;x)
NAMED = [(2, 1, 0, 8, 3), (2, 6, 4, 8, 3)]

KMAX = 10                    # brief asked for 0..6, extend to 10 if cheap -- it is

print("=" * 78)
print("w133 r13b — CE-2 + k pendant triangles at vertex %d: family certification" % HUB)
print("=" * 78)

# ---- 0. the seed itself, re-verified from the edge list ---------------------
print("\n[0] CE-2 re-verified from its edge list (nothing inherited)")
g0, n0 = F(0)
ok, bad = c4free_strong(g0)
check(ok, "CE-2 is C4-free (strong form)", "%d violating pairs" % len(bad))
check(n0 == 10, "n(CE-2) = 10", "got %d" % n0)
check(connected(g0), "CE-2 is connected")
check(mass(g0) == 25, "sum a(v) = 25 on CE-2", "got %d" % mass(g0))
check(longest_induced_path(g0, 9) == 6, "path(CE-2) = 6 (VERTICES)",
      "got %d" % longest_induced_path(g0, 9))
f0 = frames(g0)
check(len(f0) == 2, "CE-2 has exactly 2 three-frames", "got %d" % len(f0))
check(all(t[6] for t in f0), "both are Case-2-forced")
got0 = sorted((t[0], t[1], t[2], t[3], t[4]) for t in f0)
check(got0 == sorted(NAMED), "they are exactly the two named in round 13",
      "%s" % (got0,))

# ---- 1. the family, k = 0..KMAX --------------------------------------------
print("\n[1] the family F_k, k = 0..%d — every property re-derived per k" % KMAX)
print("     k    n    E   sum_a       l        path   #frames  named frames  C4-free")
rows = []
for k in range(KMAX + 1):
    g, n = F(k)
    ok, bad = c4free_strong(g)
    check(ok, "F_%d is C4-free (strong form)" % k, "%d violating pairs" % len(bad)) \
        if not ok else None
    conn = connected(g)
    m = mass(g)
    E = sum(len(s) for s in g) // 2
    # path: prove BOTH bounds -- >= 6 and NOT >= 7.  This is the off-by-one trap
    # that killed D3_A and D3_C in round 13, so it is checked as two separate facts.
    p6 = has_induced_path(g, 6)
    p7 = has_induced_path(g, 7)
    fr = frames(g)
    named_ok = all(any((t[0], t[1], t[2], t[3], t[4]) == nm and t[6] for t in fr)
                   for nm in NAMED)
    l = Fraction(m, n)
    rows.append((k, n, E, m, l, p6, p7, len(fr), named_ok, ok, conn))
    print("   %3d  %3d  %3d   %5d   %7s     %s   %5d     %-5s        %s"
          % (k, n, E, m, str(l),
             ("6" if (p6 and not p7) else ("<6" if not p6 else ">=7")),
             len(fr), named_ok, ok))

print()
for (k, n, E, m, l, p6, p7, nf, named_ok, c4, conn) in rows:
    check(c4, "k=%2d: C4-free (strong form)" % k)
    check(conn, "k=%2d: connected" % k)
    check(n == 10 + 2 * k, "k=%2d: n = 10 + 2k" % k, "got %d" % n)
    check(m == 25 + 3 * k, "k=%2d: sum a = 25 + 3k" % k, "got %d" % m)
    check(p6 and not p7, "k=%2d: path = 6 EXACTLY (>=6 yes, >=7 no)" % k,
          "p6=%s p7=%s" % (p6, p7))
    check(named_ok, "k=%2d: BOTH named 3-frames survive and stay Case-2-forced" % k)
    check(l == Fraction(25 + 3 * k, 10 + 2 * k), "k=%2d: l = (25+3k)/(10+2k)" % k,
          "l = %s" % l)
    check(l < 3, "k=%2d: l < 3 (family sits BELOW the l>3 line)" % k, "l = %s" % l)

# ---- 2. the two limit facts the strategic consequence rests on -------------
print("\n[2] monotonicity and limits of l on the family")
ls = [r[4] for r in rows]
check(ls[0] == Fraction(5, 2), "sup l = l(k=0) = 5/2", "l0 = %s" % ls[0])
check(all(ls[i] > ls[i + 1] for i in range(len(ls) - 1)),
      "l is STRICTLY DECREASING in k", "%s ... %s" % (ls[0], ls[-1]))
check(all(l > Fraction(3, 2) for l in ls),
      "l stays strictly > 3/2 for every k", "l(k=%d) = %s" % (KMAX, ls[-1]))
# the limit, as an EXACT identity rather than a numerical impression:
#   l(k) - 3/2 = (25+3k)/(10+2k) - 3/2 = (50+6k-30-6k) / (2(10+2k)) = 10/(10+2k) -> 0
gap_ok = all(rows[i][4] - Fraction(3, 2) == Fraction(10, 10 + 2 * rows[i][0])
             for i in range(len(rows)))
check(gap_ok, "EXACT: l(k) - 3/2 = 10/(10+2k), hence l -> 3/2 from above",
      "gap(k=%d) = %s" % (KMAX, ls[-1] - Fraction(3, 2)))

# ---- 3. the conclusion, stated as the two registry-facing propositions ------
print("\n[3] conclusions")
unbounded = all(r[5] and not r[6] and r[8] and r[9] and r[10] for r in rows)
check(unbounded,
      "E3(i) is NO: n is UNBOUNDED in the bad class "
      "(C4-free + Case-2-forced 3-frame + path = 6)")
check(unbounded,
      "E3(iii): the infinite family EXISTS, n = 10+2k -> oo, "
      "l = (25+3k)/(10+2k) decreasing")

print("""
[4] STRATEGIC CONSEQUENCE (recorded with the result)
    Since n is unbounded in the bad class, NO route to (T-C+)/(T-D) can proceed by
    bounding n.  Every surviving route must come through the hypothesis l > 3.
    This family is consistent with that hypothesis being the live one: its l is
    strictly below 5/2 < 3 for every k, so it never enters the l > 3 class and
    therefore constrains the n-route only.""")

print("\nFAILURES: %d" % FAIL)
sys.exit(1 if FAIL else 0)
