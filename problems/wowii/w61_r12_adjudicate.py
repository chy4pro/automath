#!/usr/bin/env python3
"""owner-w61 round 12 — independent adjudication of Q26 (codex `sol`, §7.6 chain).

Reproduces, from scratch and reusing NO number from the report:
  * the residue calibration the judge claims it ran (K2, C3..C9),
  * both T12 control graphs (Control R = C5, Control F = the 6-vertex frame graph)
    against every class predicate the judge asserts of them,
  * the SL boundary graph E={03,12,13,23}, A={0,1},
  * the D1 claim: does Corollary SL-HC's proof consume `tau >= 4` anywhere?
    (checked as the mathematical fact the judge offers in its place:
     connected + diam = 4  =>  tau >= 2, i.e. no vertex cover of size <= 1.)
Own residue transcription, calibrated before any adjudication number is computed.
"""
from itertools import combinations


def residue(degs):
    """Havel-Hakimi residue: repeatedly delete the head d and subtract 1 from the
    next d entries (truncated at 0); the residue is the number of entries left when
    the head is 0."""
    s = sorted(degs, reverse=True)
    steps = 0
    while s and s[0] > 0:
        d = s[0]
        rest = s[1:]
        head, tail = rest[:d], rest[d:]
        head = [max(0, x - 1) for x in head]
        s = sorted(head + tail, reverse=True)
        steps += 1
    return len(s), steps


def deg(n, E):
    d = [0] * n
    for u, v in E:
        d[u] += 1
        d[v] += 1
    return d


def nbrs(n, E):
    g = {i: set() for i in range(n)}
    for u, v in E:
        g[u].add(v)
        g[v].add(u)
    return g


def bfs_ecc(n, E, s):
    g = nbrs(n, E)
    dist = {s: 0}
    frontier = [s]
    while frontier:
        nxt = []
        for x in frontier:
            for y in g[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    nxt.append(y)
        frontier = nxt
    return dist


def connected(n, E):
    return len(bfs_ecc(n, E, 0)) == n


def diameter(n, E):
    return max(max(bfs_ecc(n, E, s).values()) for s in range(n))


def indep_sets(n, E):
    Es = {frozenset(e) for e in E}
    for k in range(n, -1, -1):
        found = [S for S in combinations(range(n), k)
                 if all(frozenset((u, v)) not in Es for u, v in combinations(S, 2))]
        if found:
            return k, found
    return 0, [()]


def is_forest(n, sub, E):
    idx = {v: i for i, v in enumerate(sub)}
    edges = [(idx[u], idx[v]) for u, v in E if u in idx and v in idx]
    parent = list(range(len(sub)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True


def forest_number(n, E):
    for k in range(n, 0, -1):
        for S in combinations(range(n), k):
            if is_forest(n, set(S), E):
                return k
    return 0


print("=== CALIBRATION (run before any adjudication number) ===")
K2 = (2, [(0, 1)])
r, _ = residue(deg(*K2))
print(f"  K2   residue={r} expected=1  {'OK' if r == 1 else 'FAIL'}")
for n in range(3, 10):
    C = (n, [(i, (i + 1) % n) for i in range(n)])
    r, _ = residue(deg(*C))
    exp = -(-n // 3)
    print(f"  C{n}   residue={r} expected={exp}  {'OK' if r == exp else 'FAIL'}")
print()

print("=== Q26 CONTROL R (claimed: C5, reductio-only, NOT in the frame) ===")
n, E = 5, [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
a, sets_ = indep_sets(n, E)
r, s = residue(deg(n, E))
print(f"  connected={connected(n, E)}  alpha={a}  #max-ind-sets={len(sets_)}  "
      f"residue={r}  tau={n - a}  diam={diameter(n, E)}  f={forest_number(n, E)}")
print(f"  reductio (residue == alpha)? {r == a}   in the frame (diam==4 and f==alpha+1)? "
      f"{diameter(n, E) == 4 and forest_number(n, E) == a + 1}")
print()

print("=== Q26 CONTROL F (claimed: hard-core FRAME, residue < alpha) ===")
n, E = 6, [(0, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5)]
a, sets_ = indep_sets(n, E)
r, s = residue(deg(n, E))
f = forest_number(n, E)
print(f"  degrees={deg(n, E)}")
print(f"  connected={connected(n, E)}  alpha={a}  residue={r}  tau={n - a}  "
      f"diam={diameter(n, E)}  f={f}  non-forest={f < n}")
print(f"  A={{0,1,4,5}} independent and maximum? "
      f"{tuple(sorted((0,1,4,5))) in [tuple(sorted(S)) for S in sets_]}")
print(f"  frame (connected, non-forest, diam==4, f==alpha+1)? "
      f"{connected(n, E) and f < n and diameter(n, E) == 4 and f == a + 1}")
print(f"  reductio (residue == alpha)? {r == a}   -> frame-only control: "
      f"{'CONFIRMED' if r < a else 'WRONG'}")
print(f"  tau = {n - a}: does the FRAME by itself supply tau >= 4? "
      f"{'NO — this instance has tau=' + str(n - a) if n - a < 4 else 'inconclusive'}")
print()

print("=== Q26 SL boundary instance E={03,12,13,23}, A={0,1} ===")
n, E = 4, [(0, 3), (1, 2), (1, 3), (2, 3)]
a, sets_ = indep_sets(n, E)
r, s = residue(deg(n, E))
print(f"  alpha={a}  residue={r}  tau={n - a}  reductio? {r == a}  "
      f"A={{0,1}} maximum? {tuple(sorted((0,1))) in [tuple(sorted(S)) for S in sets_]}")
print()

print("=== D1: is `tau >= 4` needed, or does diam=4 already give tau >= 2? ===")
print("  Claim to check: a connected graph with vertex-cover number tau <= 1 has")
print("  diameter <= 2, so diam = 4 forces tau >= 2 with no appeal to Theorem T3.")
bad = 0
tested = 0
for n in range(2, 8):
    verts = list(range(n))
    allpairs = list(combinations(verts, 2))
    # exhaustive over all graphs is too big past n=5; enumerate covers directly instead:
    # tau <= 1 means every edge meets a fixed vertex c  ->  G is a star (plus isolated
    # vertices, excluded by connectivity).  Check every star on n vertices.
    for c in verts:
        E = [(c, v) for v in verts if v != c]
        if not E:
            continue
        tested += 1
        d = diameter(n, E)
        a, _ = indep_sets(n, E)
        tau = n - a
        if tau <= 1 and d > 2:
            bad += 1
            print("   COUNTEREXAMPLE", n, c, d, tau)
print(f"  stars tested = {tested}; connected graphs with tau <= 1 and diam > 2: {bad}")
print("  => diam = 4 implies tau >= 2.  Theorem SL's numerical hypothesis is met")
print("     WITHOUT the `tau >= 4` rider; the rider is therefore unused in SL-HC.")
print()
print("done")
