#!/usr/bin/env python3
"""
WOWII Graffiti.pc Conjecture 61 verification.

Claim:  for every connected simple graph G,
            f(G) >= residue(G) + ceil(diam(G)/3)
where f(G) = largestInducedForestSize (max # vertices inducing a forest),
residue(G) = Havel-Hakimi residue of the degree sequence (Lean: residueAux),
diam(G) = graph diameter.

All definitions mirror the Lean statements in
  FormalConjectures/WrittenOnTheWallII/GraphConjecture61.lean
  FormalConjecturesForMathlib/Combinatorics/SimpleGraph/Residue.lean
  FormalConjecturesForMathlib/Combinatorics/SimpleGraph/Induced.lean

Stages:
  A  all connected graphs on 2..7 vertices (networkx graph atlas, exhaustive)
  B  all connected graphs on 8 vertices (exhaustive cover, no iso-dedup:
     every connected 8-vertex graph = connected 7-vertex graph + one vertex
     with nonempty neighbourhood, because every connected graph has a
     non-cut vertex)
  C  structured families (paths/cycles/powers/lexicographic blow-ups/
     clique chains/theta graphs/trees ...) up to ~40 vertices
  D  randomised + simulated-annealing search minimising the slack
       slack(G) = f(G) - residue(G) - ceil(diam(G)/3)
     on n = 9..13
Run:  python3 wowii61_verify.py
"""
import sys, random, math, itertools
from math import ceil

# ---------------------------------------------------------------- primitives

def residue_seq(degs):
    """Havel-Hakimi residue, mirroring Lean `residueAux` exactly.
       [] -> 0 ; 0::s -> 1+len(s) ; d::rest -> residueAux(HHstep)."""
    s = sorted(degs, reverse=True)
    while True:
        if not s:
            return 0
        if s[0] == 0:
            return len(s)
        d = s[0]
        rest = s[1:]
        head = rest[:d]           # List.splitAt d  (takes min(d,len) elements)
        tail = rest[d:]
        s = sorted([max(x - 1, 0) for x in head] + tail, reverse=True)


def adj_masks(n, edges):
    a = [0] * n
    for (u, v) in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def bfs_ecc(a, n, s):
    dist = [-1] * n
    dist[s] = 0
    frontier = [s]
    seen = 1 << s
    d = 0
    cnt = 1
    while frontier:
        d += 1
        nxt = []
        for u in frontier:
            m = a[u] & ~seen
            while m:
                b = m & -m
                v = b.bit_length() - 1
                m ^= b
                seen |= b
                dist[v] = d
                cnt += 1
                nxt.append(v)
        frontier = nxt
    return (d - 1 if cnt > 1 else 0), cnt


def diameter(a, n):
    """0 if not connected (matches Mathlib SimpleGraph.diam convention)."""
    best = 0
    for s in range(n):
        e, cnt = bfs_ecc(a, n, s)
        if cnt != n:
            return None            # disconnected
        best = max(best, e)
    return best


def is_acyclic(a, sub, verts):
    """induced subgraph on bitmask `sub` is a forest?  |E| == |V| - #components"""
    ecount = 0
    for v in verts:
        ecount += bin(a[v] & sub).count('1')
    ecount //= 2
    # components
    comps = 0
    unseen = sub
    while unseen:
        b = unseen & -unseen
        comps += 1
        stack = [b.bit_length() - 1]
        unseen ^= b
        while stack:
            u = stack.pop()
            m = a[u] & unseen
            while m:
                c = m & -m
                m ^= c
                unseen ^= c
                stack.append(c.bit_length() - 1)
    return ecount == len(verts) - comps


def largest_induced_forest_bruteforce(a, n):
    """exact, exponential; only used as a cross-check for n <= 12"""
    for k in range(n, -1, -1):
        for verts in itertools.combinations(range(n), k):
            sub = 0
            for v in verts:
                sub |= 1 << v
            if is_acyclic(a, sub, verts):
                return k
    return 0


def _acyclic_mask(a, sub):
    verts = []
    m = sub
    while m:
        b = m & -m
        m ^= b
        verts.append(b.bit_length() - 1)
    return is_acyclic(a, sub, verts)


def _greedy_forest(a, n, order):
    S = 0
    for v in order:
        T = S | (1 << v)
        if _acyclic_mask(a, T):
            S = T
    return bin(S).count('1')


def largest_induced_forest(a, n, rnd=None):
    """exact maximum induced forest, branch & bound seeded by randomised greedy."""
    rnd = rnd or random.Random(12345)
    best = 0
    order0 = sorted(range(n), key=lambda v: bin(a[v]).count('1'))
    best = max(best, _greedy_forest(a, n, order0))
    for _ in range(12):
        o = list(range(n)); rnd.shuffle(o)
        best = max(best, _greedy_forest(a, n, o))
    # branch & bound: vertices in decreasing-degree order
    order = sorted(range(n), key=lambda v: -bin(a[v]).count('1'))
    bestbox = [best]

    def rec(i, S, size):
        if size + (n - i) <= bestbox[0]:
            return
        if i == n:
            if size > bestbox[0]:
                bestbox[0] = size
            return
        v = order[i]
        T = S | (1 << v)
        if _acyclic_mask(a, T):
            rec(i + 1, T, size + 1)
        rec(i + 1, S, size)

    rec(0, 0, 0)
    return bestbox[0]


def stats(n, edges):
    a = adj_masks(n, edges)
    d = diameter(a, n)
    if d is None:
        return None
    degs = [bin(x).count('1') for x in a]
    r = residue_seq(degs)
    f = largest_induced_forest(a, n)
    rhs = r + -((-d) // 3)          # ceil(d/3)
    return dict(n=n, edges=edges, diam=d, residue=r, f=f, rhs=rhs, slack=f - rhs)


# ------------------------------------------------------------------- reports

class Tracker:
    def __init__(self):
        self.count = 0
        self.viol = []
        self.best = None          # minimal slack witness
        self.tight = 0
    def add(self, st, tag):
        if st is None:
            return
        self.count += 1
        if st['slack'] < 0:
            self.viol.append((tag, st))
        if st['slack'] == 0:
            self.tight += 1
        if self.best is None or st['slack'] < self.best[1]['slack']:
            self.best = (tag, st)
    def report(self, name):
        print(f"[{name}] tested={self.count}  violations={len(self.viol)}  tight(slack=0)={self.tight}")
        if self.best:
            t, s = self.best
            print(f"    min slack = {s['slack']}  at {t}: n={s['n']} diam={s['diam']} "
                  f"residue={s['residue']} f={s['f']}")
        for t, s in self.viol[:10]:
            print("    !!! COUNTEREXAMPLE", t, s)


# ------------------------------------------------------------------ stage A/B

def stage_AB():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    T = Tracker()
    conn7 = []
    for G in graph_atlas_g():
        n = G.number_of_nodes()
        if n < 2:
            continue
        if not nx.is_connected(G):
            continue
        edges = [(u, v) for u, v in G.edges()]
        st = stats(n, edges)
        T.add(st, f"atlas n={n} E={edges}")
        if n == 7:
            conn7.append(edges)
    T.report("A: exhaustive n=2..7 (all connected graphs, atlas)")

    T2 = Tracker()
    for edges in conn7:
        for mask in range(1, 1 << 7):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            st = stats(8, e2)
            T2.add(st, f"n=8 E={e2}")
    T2.report("B: exhaustive n=8 (cover of all connected 8-vertex graphs)")
    return T, T2


# -------------------------------------------------------------------- stage C

def fam_path(n):      return [(i, i + 1) for i in range(n - 1)]
def fam_cycle(n):     return [(i, (i + 1) % n) for i in range(n)]

def fam_power(n, k, cyc=False):
    E = []
    for i in range(n):
        for j in range(i + 1, n):
            d = j - i
            if cyc:
                d = min(d, n - d)
            if d <= k:
                E.append((i, j))
    return E

def fam_lex_clique(m, r, cyc=False):
    """P_m (or C_m) blown up: each of m groups is a clique K_r,
       consecutive groups completely joined."""
    E = []
    for i in range(m):
        for x in range(r):
            for y in range(x + 1, r):
                E.append((i * r + x, i * r + y))
    lim = m if cyc else m - 1
    for i in range(lim):
        j = (i + 1) % m
        for x in range(r):
            for y in range(r):
                E.append((i * r + x, j * r + y))
    return E

def fam_lex_empty(m, r, cyc=False):
    """P_m (or C_m) blown up by independent sets of size r."""
    E = []
    lim = m if cyc else m - 1
    for i in range(lim):
        j = (i + 1) % m
        for x in range(r):
            for y in range(r):
                E.append((i * r + x, j * r + y))
    return E

def fam_clique_chain(m, r):
    """m cliques K_r in a row, consecutive ones sharing exactly one vertex."""
    E = []
    base = 0
    verts = []
    idx = 0
    groups = []
    for i in range(m):
        g = []
        if i > 0:
            g.append(groups[-1][-1])
        while len(g) < r:
            g.append(idx); idx += 1
        groups.append(g)
    for g in groups:
        for x in range(len(g)):
            for y in range(x + 1, len(g)):
                E.append((g[x], g[y]))
    return E, idx

def fam_theta(a, b):
    """two vertices joined by two internally disjoint paths of lengths a,b."""
    E = []
    idx = 2
    for L in (a, b):
        prev = 0
        for _ in range(L - 1):
            E.append((prev, idx)); prev = idx; idx += 1
        E.append((prev, 1))
    return E, idx

def fam_caterpillar(m, legs):
    E = [(i, i + 1) for i in range(m - 1)]
    idx = m
    for i in range(m):
        for _ in range(legs):
            E.append((i, idx)); idx += 1
    return E, idx

def stage_C(maxn=26):
    T = Tracker()
    for n in range(2, maxn + 1):
        T.add(stats(n, fam_path(n)), f"P_{n}")
        if n >= 3:
            T.add(stats(n, fam_cycle(n)), f"C_{n}")
        for k in (2, 3, 4):
            if n > k + 1:
                T.add(stats(n, fam_power(n, k)), f"P_{n}^{k}")
                T.add(stats(n, fam_power(n, k, True)), f"C_{n}^{k}")
    for m in range(2, 15):
        for r in range(1, 6):
            if m * r <= maxn:
                T.add(stats(m * r, fam_lex_clique(m, r)), f"P_{m}[K_{r}]")
                T.add(stats(m * r, fam_lex_clique(m, r, True)), f"C_{m}[K_{r}]")
                T.add(stats(m * r, fam_lex_empty(m, r)), f"P_{m}[E_{r}]")
                if m >= 3:
                    T.add(stats(m * r, fam_lex_empty(m, r, True)), f"C_{m}[E_{r}]")
    for m in range(2, 12):
        for r in range(3, 7):
            E, n = fam_clique_chain(m, r)
            if n <= maxn:
                T.add(stats(n, E), f"chain {m}xK_{r}")
    for a in range(2, 16):
        for b in range(a, 16):
            E, n = fam_theta(a, b)
            if n <= maxn and n >= 3:
                T.add(stats(n, E), f"theta({a},{b})")
    for m in range(2, 16):
        for legs in range(1, 4):
            E, n = fam_caterpillar(m, legs)
            if n <= maxn:
                T.add(stats(n, E), f"caterpillar({m},{legs})")
    # random trees
    rnd = random.Random(7)
    for n in range(3, maxn + 1):
        for _ in range(30):
            E = [(rnd.randrange(i), i) for i in range(1, n)]
            T.add(stats(n, E), f"randtree n={n}")
    T.report("C: structured families")
    return T


# -------------------------------------------------------------------- stage D

def rand_conn(n, p, rnd):
    while True:
        E = [(i, j) for i in range(n) for j in range(i + 1, n) if rnd.random() < p]
        a = adj_masks(n, E)
        if diameter(a, n) is not None:
            return E


def stage_D(seed=1, samples_per=4000):
    T = Tracker()
    rnd = random.Random(seed)
    for n in (9, 10):
        for p in (0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6):
            for _ in range(samples_per // 7):
                T.add(stats(n, rand_conn(n, p, rnd)), f"G({n},{p})")
    T.report("D1: uniform random connected graphs n=9,10")

    # simulated annealing on slack
    T2 = Tracker()
    for n in (9, 10, 11, 12, 13):
        best_overall = None
        for restart in range(6):
            E = set(map(tuple, rand_conn(n, 0.3, rnd)))
            cur = stats(n, sorted(E))
            temp = 1.0
            for step in range(1200):
                i = rnd.randrange(n); j = rnd.randrange(n)
                if i == j:
                    continue
                e = (min(i, j), max(i, j))
                if e in E:
                    E.discard(e)
                else:
                    E.add(e)
                st = stats(n, sorted(E))
                if st is None:
                    # revert (disconnected)
                    if e in E: E.discard(e)
                    else: E.add(e)
                    continue
                T2.add(st, f"anneal n={n}")
                d = st['slack'] - cur['slack']
                if d <= 0 or rnd.random() < math.exp(-d / max(temp, 1e-6)):
                    cur = st
                else:
                    if e in E: E.discard(e)
                    else: E.add(e)
                temp *= 0.997
    T2.report("D2: simulated annealing minimising slack, n=9..13")
    return T, T2


# -------------------------------------------------------------------- stage E
# Certificates / candidate strengthenings.  alpha = independence number,
# mu = maximum matching, nabla = n - f = decycling number,
# rho*(G) = max over MAXIMUM independent sets A of the largest 2-packing in V\A.

def alpha_num(a, n):
    for k in range(n, -1, -1):
        for verts in itertools.combinations(range(n), k):
            ok = True
            for i in range(k):
                if a[verts[i]] & sum(1 << verts[j] for j in range(i + 1, k)):
                    ok = False; break
            if ok:
                return k
    return 0


def all_dists(a, n):
    D = []
    for s in range(n):
        dist = [-1] * n; dist[s] = 0; fr = [s]; d = 0
        while fr:
            d += 1; nx = []
            for u in fr:
                m = a[u]
                while m:
                    b = m & -m; v = b.bit_length() - 1; m ^= b
                    if dist[v] < 0:
                        dist[v] = d; nx.append(v)
            fr = nx
        D.append(dist)
    return D


def matching_num(a, n):
    edges = [(u, v) for u in range(n) for v in range(u + 1, n) if a[u] >> v & 1]
    best = 0
    def rec(i, used, k):
        nonlocal best
        if k + (len(edges) - i) <= best: return
        if i == len(edges):
            best = max(best, k); return
        u, v = edges[i]
        if not (used >> u & 1) and not (used >> v & 1):
            rec(i + 1, used | (1 << u) | (1 << v), k + 1)
        rec(i + 1, used, k)
    rec(0, 0, 0)
    return best


def rho_star(a, n, D, al):
    best = 0
    for A in itertools.combinations(range(n), al):
        ok = True
        for i in range(al):
            if a[A[i]] & sum(1 << A[j] for j in range(i + 1, al)):
                ok = False; break
        if not ok: continue
        cand = [v for v in range(n) if v not in A]
        cur = [0]
        def rec(i, S):
            if len(S) + (len(cand) - i) <= cur[0]: return
            if i == len(cand):
                cur[0] = max(cur[0], len(S)); return
            v = cand[i]
            if all(D[v][u] >= 3 for u in S): rec(i + 1, S + [v])
            rec(i + 1, S)
        rec(0, [])
        best = max(best, cur[0])
    return best


def stage_E(limit8=30000):
    """Coverage of the PROVED sufficient conditions (see wowii61_draft.md)."""
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g

    def gens():
        for G in graph_atlas_g():
            n = G.number_of_nodes()
            if 2 <= n <= 7 and nx.is_connected(G):
                yield "n<=7", n, [(u, v) for u, v in G.edges()]
        c7 = [[(u, v) for u, v in G.edges()] for G in graph_atlas_g()
              if G.number_of_nodes() == 7 and nx.is_connected(G)]
        k = 0
        for edges in c7:
            for mask in range(1, 1 << 7):
                if k >= limit8: return
                k += 1
                yield "n=8", 8, list(edges) + [(7, v) for v in range(7) if mask >> v & 1]

    print("[E] Corollary B2: d with floor((d-1)/4)+1 >= ceil(d/3):  "
          f"{[d for d in range(1, 500) if (d - 1) // 4 + 1 >= -((-d) // 3)]}")
    print("[E] Corollary C1: d with ceil(d/2) < ceil(d/3) (must be empty):  "
          f"{[d for d in range(0, 500) if -((-d)//2) < -((-d)//3)]}")
    import collections
    tot = collections.Counter(); cov = collections.Counter(); unc = []
    for tag, n, edges in gens():
        a = adj_masks(n, edges)
        D = all_dists(a, n)
        if any(D[i][j] < 0 for i in range(n) for j in range(n)): continue
        d = max(max(r) for r in D); cd = -((-d) // 3)
        al = alpha_num(a, n); f = largest_induced_forest(a, n)
        res = residue_seq([bin(x).count('1') for x in a])
        mu = matching_num(a, n); nab = n - f
        assert res <= al, ("FMS residue<=alpha violated", n, edges)
        assert f >= al + 1, ("f>=alpha+1 violated", n, edges)
        assert f >= al + (d - 1) // 4 + 1, ("Thm 3 corollary violated", n, edges)
        assert f >= res + cd, ("CONJECTURE 61 VIOLATED", n, edges)
        tot[tag] += 1
        p1 = d <= 3
        p2 = mu >= nab + cd
        p3 = rho_star(a, n, D, al) >= cd
        if p1: cov[(tag, 'P1 diam<=3')] += 1
        if p2: cov[(tag, 'P2 mu>=nabla+ceil(d/3)')] += 1
        if p3: cov[(tag, 'P3 rho*>=ceil(d/3)')] += 1
        if p1 or p2 or p3: cov[(tag, 'ANY')] += 1
        else: unc.append((n, d, al, f, res, mu, nab, edges))
    for tag in tot:
        print(f"[E] {tag}: {tot[tag]} graphs")
        for key in ('P1 diam<=3', 'P2 mu>=nabla+ceil(d/3)', 'P3 rho*>=ceil(d/3)', 'ANY'):
            c = cov[(tag, key)]
            print(f"     {key:26s} {c:6d} ({100.0*c/tot[tag]:5.1f}%)")
    print(f"[E] uncovered total: {len(unc)}; diameters present: "
          f"{sorted(set(u[1] for u in unc))}")
    for u in unc[:4]:
        print(f"     n={u[0]} d={u[1]} alpha={u[2]} f={u[3]} res={u[4]} mu={u[5]} nabla={u[6]} E={u[7]}")


# -------------------------------------------------------------------- stage W
# Every numerical assertion made in wowii61_draft.md is re-checked here.

def _pack_num(a, n, D, avoid=()):
    cand = [v for v in range(n) if v not in avoid]
    cur = [0]
    def rec(i, S):
        if len(S) + (len(cand) - i) <= cur[0]: return
        if i == len(cand):
            cur[0] = max(cur[0], len(S)); return
        v = cand[i]
        if all(D[v][u] >= 3 for u in S): rec(i + 1, S + [v])
        rec(i + 1, S)
    rec(0, [])
    return cur[0]


def _full(n, edges):
    a = adj_masks(n, edges)
    D = all_dists(a, n)
    d = max(max(r) for r in D)
    al = alpha_num(a, n)
    return dict(n=n, d=d, cd=-((-d) // 3), alpha=al,
                f=largest_induced_forest(a, n),
                res=residue_seq([bin(x).count('1') for x in a]),
                mu=matching_num(a, n), rho=_pack_num(a, n, D),
                rho_star=rho_star(a, n, D, al))


def _sub(n, edges, removed):
    keep = [v for v in range(n) if v not in removed]
    idx = {u: i for i, u in enumerate(keep)}
    a = adj_masks(n, edges)
    e2 = [(idx[u], idx[w]) for u in keep for w in keep if u < w and (a[u] >> w & 1)]
    a2 = adj_masks(len(keep), e2)
    return residue_seq([bin(x).count('1') for x in a2]) if keep else 0


def stage_W():
    W = {
      'W1 (Route R2 "f>=alpha+ceil(d/3)" is FALSE)':
          (8, [(0,1),(1,2),(1,3),(1,4),(2,5),(5,6),(7,1),(7,5)]),
      'W2 (Route R1 "alpha+1>=res+ceil(d/3)" is FALSE)':
          (8, [(0,1),(1,2),(2,3),(2,4),(2,5),(2,6),(7,3)]),
      'W3 (Route R3 "f>=alpha+rho" is FALSE)':
          (7, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,6),(2,3),(3,5)]),
      'W4 (smallest uncovered tight graph, d=4)':
          (6, [(0,2),(1,3),(2,4),(2,5),(3,4),(3,5)]),
    }
    for name, (n, e) in W.items():
        s = _full(n, e)
        print(f"  {name}\n     n={s['n']} E={e}\n     diam={s['d']} ceil(d/3)={s['cd']} "
              f"alpha={s['alpha']} f={s['f']} residue={s['res']} mu={s['mu']} "
              f"rho={s['rho']} rho*={s['rho_star']}  slack={s['f']-s['res']-s['cd']}")
    # W5: residue(G) <= 1 + residue(G-N[v]) fails for v of minimum degree
    n, e = 6, [(0,2),(0,5),(1,3),(1,4),(2,3),(3,4),(3,5)]
    a = adj_masks(n, e); degs = [bin(x).count('1') for x in a]
    v = min(range(n), key=lambda u: degs[u])
    rem = {v} | {u for u in range(n) if a[v] >> u & 1}
    print(f"  W5 (min-degree residue recursion is FALSE): n={n} E={e}")
    print(f"     degrees={degs}  v={v} (min degree)  N[v]={sorted(rem)}")
    print(f"     residue(G)={residue_seq(degs)}  residue(G-N[v])={_sub(n,e,rem)}")
    # W6: diametral-endpoint peeling fails: broom B_k = star K_{1,k} + path of length 3
    print("  W6 (brooms: the R6 peeling inequality happens to hold with EQUALITY here,\n       so brooms are NOT a counterexample to R6 - see stage F for the real 36.4% rate)")
    for k in (2, 3, 5, 8):
        n = k + 4
        e = [(0, i) for i in range(1, k + 1)] + [(0, k+1), (k+1, k+2), (k+2, k+3)]
        a = adj_masks(n, e)
        D = all_dists(a, n)
        v0 = 1                                   # a leaf of the star: ecc = 4 = diam
        rem = {v0} | {u for u in range(n) if a[v0] >> u & 1}
        s = _full(n, e)
        print(f"     k={k}: n={n} diam={s['d']} residue={s['res']} f={s['f']} "
              f"residue(G-N[v0])={_sub(n,e,rem)}  (1+that = {1+_sub(n,e,rem)})")
    # W7: residue of cycles = ceil(n/3); residue of K_2 = 1 (Lean sanity check)
    print("  W7 (definition sanity):  residue(K2)=%d  residue(C_n) for n=3..9: %s"
          % (residue_seq([1,1]), [residue_seq([2]*i) for i in range(3, 10)]))
    print("     expected ceil(n/3) for C_n:            %s"
          % [-((-i)//3) for i in range(3, 10)])


# -------------------------------------------------------------------- stage F
# Sub-conjectures SC1 / SC2 (which together imply Conjecture 61), and the
# measured failure rates of the dead attack routes R4 and R6.

def stage_F(limit8=40000):
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g

    def gens():
        for G in graph_atlas_g():
            n = G.number_of_nodes()
            if 2 <= n <= 7 and nx.is_connected(G):
                yield n, [(u, v) for u, v in G.edges()]
        c7 = [[(u, v) for u, v in G.edges()] for G in graph_atlas_g()
              if G.number_of_nodes() == 7 and nx.is_connected(G)]
        k = 0
        for edges in c7:
            for mask in range(1, 1 << 7):
                if k >= limit8: break
                k += 1
                yield 8, list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            if k >= limit8: break
        rnd = random.Random(4242)                     # random n = 9..14 top-up
        for _ in range(6000):
            nn = rnd.choice((9, 10, 11, 12, 13, 14))
            yield nn, rand_conn(nn, rnd.choice((0.15, 0.2, 0.25, 0.3, 0.4, 0.5)), rnd)

    n1 = sc2n = bad1 = bad2 = 0
    r4n = r4bad = r6n = r6bad = 0
    for n, edges in gens():
        a = adj_masks(n, edges); D = all_dists(a, n)
        if any(D[i][j] < 0 for i in range(n) for j in range(n)): continue
        d = max(max(r) for r in D); cd = -((-d) // 3)
        al = alpha_num(a, n); f = largest_induced_forest(a, n)
        res = residue_seq([bin(x).count('1') for x in a])
        k = max(1, -((-(d - 1)) // 3))
        n1 += 1
        if f < al + k: bad1 += 1; print("  SC1 FAILS", n, edges)
        if d >= 4 and d % 3 == 1 and f == al + k:
            sc2n += 1
            if res > al - 1: bad2 += 1; print("  SC2 FAILS", n, edges)
        if n > 8:                       # R4/R6 statistics: n<=8 part only
            continue
        # R4: ball-peeling certificate  Phi = max over 2-packings B of |B|+alpha(G-N[B])
        best = 0
        def rec(i, B):
            nonlocal best
            if i == n:
                rem = 0
                for b in B: rem |= (1 << b) | a[b]
                keep = [v for v in range(n) if not (rem >> v & 1)]
                idx = {u: j for j, u in enumerate(keep)}
                e2 = [(idx[u], idx[w]) for u in keep for w in keep
                      if u < w and (a[u] >> w & 1)]
                a2 = adj_masks(len(keep), e2)
                best = max(best, len(B) + (alpha_num(a2, len(keep)) if keep else 0))
                return
            if all(D[i][u] >= 3 for u in B): rec(i + 1, B + [i])
            rec(i + 1, B)
        rec(0, [])
        r4n += 1
        if best < res + cd: r4bad += 1
        # R6: exists diametral endpoint v with residue(G) <= residue(G-N[v]) ?
        if d >= 4:
            r6n += 1
            ok = False
            for v in [u for u in range(n) if max(D[u]) == d]:
                rem = {v} | {u for u in range(n) if a[v] >> u & 1}
                keep = [u for u in range(n) if u not in rem]
                idx = {u: j for j, u in enumerate(keep)}
                e2 = [(idx[u], idx[w]) for u in keep for w in keep
                      if u < w and (a[u] >> w & 1)]
                a2 = adj_masks(len(keep), e2)
                r2 = residue_seq([bin(x).count('1') for x in a2]) if keep else 0
                if res <= r2: ok = True; break
            if not ok: r6bad += 1
    print(f"[F] SC1 (f >= alpha + max(1,ceil((d-1)/3))):  tested={n1}  failures={bad1}")
    print(f"[F] SC2 (d=1 mod 3, d>=4, f = alpha+ceil((d-1)/3) => residue<alpha): "
          f"hypothesis met on {sc2n} graphs, failures={bad2}")
    print(f"[F] DEAD route R4 (ball-peeling certificate Phi >= residue+ceil(d/3)): "
          f"tested={r4n}  failures={r4bad} ({100.0*r4bad/max(r4n,1):.1f}%)")
    print(f"[F] DEAD route R6 (some diametral endpoint v with residue(G)<=residue(G-N[v])): "
          f"tested={r6n} (diam>=4)  failures={r6bad} ({100.0*r6bad/max(r6n,1):.1f}%)")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "w"):
        stage_W()
    if which in ("all", "f"):
        stage_F()
    if which in ("all", "ab"):
        stage_AB()
    if which in ("all", "c"):
        stage_C()
    if which in ("all", "d"):
        stage_D()
    if which in ("all", "e"):
        stage_E()
