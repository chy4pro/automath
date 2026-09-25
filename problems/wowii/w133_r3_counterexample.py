#!/usr/bin/env python3
"""
WOWII-133 / pocket 1, r>=3.

Purpose: refute the "good pair" proposition
    (GP)  G connected C4-free, rad = r >= 2, l(G) >= 3
          ==> there exist u,z with dist(u,z) >= r and (a(u) >= 3, a(z) >= 2)
which Theorem G7/Theorem 4' establishes for r = 2, and which attack line (1)
(generalising the r=2 layer counting, i.e. proving 3n - Sigma > 0 from
(star) + r >= 3 + existence of a high vertex) would have to establish for r >= 3.

Witness family: Hoffman-Singleton with pendant leaves.
Everything below is computed, nothing is asserted from memory.

a(v) := alpha(G[N(v)]);  for C4-free G, a(v) = d(v) - t(v).
l(G) := (1/n) * sum_v a(v).
"""
import itertools
from collections import deque

# ---------------------------------------------------------------- graph utils

def neighbours(E, n):
    adj = [set() for _ in range(n)]
    for u, v in E:
        adj[u].add(v); adj[v].add(u)
    return adj

def bfs(adj, s):
    n = len(adj); d = [-1] * n; d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if d[w] < 0:
                d[w] = d[u] + 1; q.append(w)
    return d

def alldist(adj):
    return [bfs(adj, s) for s in range(len(adj))]

def connected(adj):
    return all(x >= 0 for x in bfs(adj, 0))

def has_c4(adj):
    """C4 as a subgraph on 4 distinct vertices == some two distinct vertices
       have >= 2 common neighbours."""
    n = len(adj)
    for u in range(n):
        for v in range(u + 1, n):
            if len(adj[u] & adj[v]) >= 2:
                return True
    return False

def girth(adj):
    n = len(adj); best = 10**9
    for s in range(n):
        d = [-1] * n; par = [-1] * n; d[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1; par[w] = u; q.append(w)
                elif w != par[u]:
                    best = min(best, d[u] + d[w] + 1)
    return best

def alpha(adj, S):
    """max independent set size of the induced subgraph on the vertex set S."""
    S = list(S)
    idx = {v: i for i, v in enumerate(S)}
    nb = [0] * len(S)
    for v in S:
        for w in adj[v]:
            if w in idx:
                nb[idx[v]] |= 1 << idx[w]
    best = 0
    def rec(cand, cur):
        nonlocal best
        if cur + bin(cand).count('1') <= best:
            return
        if cand == 0:
            best = max(best, cur); return
        v = (cand & -cand).bit_length() - 1
        rec(cand & ~(1 << v) & ~nb[v], cur + 1)   # take v
        rec(cand & ~(1 << v), cur)                # drop v
    rec((1 << len(S)) - 1, 0)
    return best

def avec(adj):
    return [alpha(adj, adj[v]) for v in range(len(adj))]

def ecc_rad(D):
    e = [max(row) for row in D]
    return e, min(e)

def is_induced_path(adj, P):
    if len(set(P)) != len(P):
        return False
    for i, u in enumerate(P):
        for j in range(i + 1, len(P)):
            v = P[j]
            adjacent = v in adj[u]
            if j == i + 1 and not adjacent:
                return False
            if j > i + 1 and adjacent:
                return False
    return True

def greedy_long_induced_path(adj, tries=4000, seed=12345):
    """Certificate generator: returns the longest induced path found.
       Only ever used to certify a LOWER bound on path(G)."""
    import random
    rng = random.Random(seed)
    n = len(adj); best = []
    for _ in range(tries):
        start = rng.randrange(n)
        P = [start]
        used = {start}      # vertices on the path
        forb = set()        # neighbours of *interior* path vertices
        while True:
            cand = [w for w in adj[P[-1]] if w not in used and w not in forb]
            if not cand:
                break
            w = rng.choice(cand)
            forb |= adj[P[-1]]      # the old endpoint is now interior
            P.append(w); used.add(w)
        if len(P) > len(best):
            best = P[:]
    assert is_induced_path(adj, best), "certificate is not an induced path"
    return best

# ---------------------------------------------------------------- H-S graph

def hoffman_singleton():
    """Robertson's pentagon/pentagram construction.
       P[h][j] ~ P[h][j+-1];  Q[i][k] ~ Q[i][k+-2];  P[h][j] ~ Q[i][k] iff k = h*i+j."""
    idP = lambda h, j: h * 5 + j
    idQ = lambda i, k: 25 + i * 5 + k
    E = set()
    for h in range(5):
        for j in range(5):
            E.add(tuple(sorted((idP(h, j), idP(h, (j + 1) % 5)))))
    for i in range(5):
        for k in range(5):
            E.add(tuple(sorted((idQ(i, k), idQ(i, (k + 2) % 5)))))
    for h in range(5):
        for i in range(5):
            for j in range(5):
                E.add(tuple(sorted((idP(h, j), idQ(i, (h * i + j) % 5)))))
    return 50, sorted(E)

def add_leaves(n, E, parents):
    """attach one pendant leaf to each entry of `parents` (repeats allowed)."""
    E = list(E); k = n
    for p in parents:
        E.append((p, k)); k += 1
    return k, E

# ---------------------------------------------------------------- the check

def report(name, n, E, expect_floor_l=None):
    adj = neighbours(E, n)
    D = alldist(adj)
    e, r = ecc_rad(D)
    a = avec(adj)
    S = sum(a)
    print(f"--- {name}")
    print(f"    n={n}  m={len(E)}  connected={connected(adj)}  C4-free={not has_c4(adj)}")
    print(f"    girth={girth(adj)}  rad={r}  diam={max(e)}")
    print(f"    Sigma a(v)={S}  l={S}/{n}={S/n:.4f}  floor(l)={S//n}")
    # the property that (GP) claims cannot happen
    bad = []
    for u in range(n):
        for v in range(n):
            if u != v and D[u][v] >= r and a[u] >= 3 and a[v] >= 2:
                bad.append((u, v, D[u][v], a[u], a[v]))
    print(f"    pairs at distance >= rad with a-values (>=3,>=2): {len(bad)}"
          + (f"   e.g. {bad[0]}" if bad else "   <-- NONE: (GP) FAILS"))
    # max distance realised by a pair both of whose a-values are >= 2
    best = max((D[u][v], u, v) for u in range(n) for v in range(n)
               if u != v and a[u] >= 2 and a[v] >= 2)
    print(f"    max distance over pairs with both a>=2: {best[0]}  (rad={r})")
    P = greedy_long_induced_path(adj)
    print(f"    induced-path certificate: {len(P)} vertices "
          f"(need path >= rad+3 = {r+3}, and >= rad+floor(l) = {r + S//n} for C133-b): "
          f"{'OK' if len(P) >= max(r + 3, r + S // n) else 'FAIL'}")
    if expect_floor_l is not None:
        assert S // n == expect_floor_l, (S // n, expect_floor_l)
    return dict(n=n, r=r, S=S, a=a, D=D, adj=adj, path_lb=len(P))

def induced_path_from(adj, s, target, allowed=None):
    """exact search: is there an induced path on >= `target` vertices starting at s?
       returns such a path or None.  `allowed` restricts the vertex set."""
    V = set(range(len(adj))) if allowed is None else set(allowed)
    best = [None]
    def rec(P, used, forb):
        if len(P) >= target:
            best[0] = P[:]; return True
        for w in adj[P[-1]]:
            if w in V and w not in used and w not in forb:
                if rec(P + [w], used | {w}, forb | adj[P[-1]]):
                    return True
        return False
    rec([s], {s}, set())
    return best[0]

def analyse_residual(name, n, E):
    """Classify G for the peeling induction of Theorem X and exercise (RP)."""
    adj = neighbours(E, n); D = alldist(adj); e, r = ecc_rad(D); a = avec(adj)
    Lam = [v for v in range(n) if a[v] == 1]
    core = [v for v in range(n) if a[v] >= 2]
    # radius-critical?  (does EVERY a=1 deletion drop the radius?)
    crit = True
    for v in Lam:
        keep = [u for u in range(n) if u != v]
        idx = {u: i for i, u in enumerate(keep)}
        E2 = [(idx[x], idx[y]) for x, y in E if x != v and y != v]
        a2 = neighbours(E2, n - 1)
        if min(max(row) for row in alldist(a2)) == r:
            crit = False; break
    # core C = G - Lambda, and the parent set P
    idx = {u: i for i, u in enumerate(core)}
    Ec = [(idx[x], idx[y]) for x, y in E if x in idx and y in idx]
    adjC = neighbours(Ec, len(core)); DC = alldist(adjC); eC, rC = ecc_rad(DC)
    P = sorted({idx[u] for u in core for w in adj[u] if w in set(Lam)})
    print(f"--- {name}: residual classification")
    print(f"    |Lambda|={len(Lam)}  mu={min(a)}  rad={r}  radius-critical={crit}"
          f"   (crit == the case the peeling induction cannot discharge)")
    print(f"    core C: n={len(core)} rad={rC} diam={max(eC)} self-centred={rC==max(eC)}"
          f"  |P|={len(P)}  rad(G)=rad(C)+1? {r == rC + 1}")
    cover = all(any(DC[u][p] == max(eC) for p in P) for u in range(len(core)))
    print(f"    covering condition (every core vertex has a parent at distance diam(C)): {cover}")
    # (RP): induced path in C on rad(C)+3 vertices with an endpoint in P  -> path(G) >= rad(G)+3
    tgt = rC + 3
    hit = next((p for p in P if induced_path_from(adjC, p, tgt)), None)
    print(f"    (RP) induced path in C on rad(C)+3={tgt} vertices ending in P: "
          f"{'YES at core vertex '+str(hit) if hit is not None else 'NO'}"
          f"  => path(G) >= {tgt+1} vs needed rad+3 = {r+3}")

if __name__ == "__main__":
    n0, E0 = hoffman_singleton()
    adj0 = neighbours(E0, n0)
    D0 = alldist(adj0)
    degs = sorted({len(adj0[v]) for v in range(n0)})
    print("Hoffman-Singleton sanity: n=%d m=%d degrees=%s girth=%d diam=%d"
          % (n0, len(E0), degs, girth(adj0), max(max(row) for row in D0)))
    assert degs == [7] and girth(adj0) == 5 and max(max(r) for r in D0) == 2

    print()
    # (A) pocket-1 shaped witness: floor(l) = 3 exactly, rad = 3
    nA, EA = add_leaves(n0, E0, [v for v in range(50) for _ in range(2)])
    report("A: Hoffman-Singleton + 2 pendant leaves at every vertex", nA, EA, 3)

    print()
    # (B) minimal-leaf variant: 3 leaves suffice to push rad from 2 to 3
    #     choose 3 parents pairwise at distance 2 with no common neighbour
    trip = None
    for u, v, w in itertools.combinations(range(50), 3):
        if D0[u][v] == 2 and D0[u][w] == 2 and D0[v][w] == 2 \
           and not (adj0[u] & adj0[v] & adj0[w]):
            trip = (u, v, w); break
    print("chosen leaf parents (pairwise distance 2, no common neighbour):", trip)
    nB, EB = add_leaves(n0, E0, list(trip))
    report("B: Hoffman-Singleton + 3 pendant leaves", nB, EB)
