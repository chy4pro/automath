#!/usr/bin/env python3
"""w133 round 12 — owner-w133's own attack on pocket 1's D = 3 layer.

Sections
  A. Re-verify the two certified counterexamples CE-1 (bare) and CE-2 (= H, Thm G45).
  B. Lemma G46 (NEW, unconditional): in any Case-2-forced 3-frame the six vertices
     u0,u1,u2,u3,y,x induce a C6.  Asserted over a structured/random sweep.
  C. The kill table: which candidate new hypothesis kills which counterexample.
  D. The decisive experiment for family (T-A)/(T-D): search for a connected C4-free
     graph with an induced C6, NO induced P7, and sum_v a(v) > 3n.
     (equivalently l > 3 with path <= 6).  Randomised local search, NO SAT,
     NO exhaustive enumeration of a large space.
  E. Same search restricted to graphs that actually carry a Case-2-forced 3-frame.

Every claim written into the draft is asserted here first.
"""
import itertools, random, sys

FAIL = 0
def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("FAIL:", msg)
    return cond

# ---------------------------------------------------------------- basic tools
def mk(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    return adj

def c4free(adj):
    n = len(adj)
    for u in range(n):
        for v in range(u + 1, n):
            if len(adj[u] & adj[v]) >= 2:
                return False
    return True

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
    """True iff G has an induced path on >= k vertices.  Early-exit DFS."""
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

def longest_induced_path(adj, cap=12):
    for k in range(cap, 1, -1):
        if has_induced_path(adj, k): return k
    return min(1, len(adj))

# ---------------------------------------------------------------- frames
def frames(adj, need_avals=True):
    """yield (u0,u1,u2,u3,x,ys,case2) for every 3-frame."""
    n = len(adj); D = [bfs(adj, s) for s in range(n)]
    out = []
    for u0 in range(n):
        for u3 in range(n):
            if D[u0][u3] != 3: continue
            if need_avals and (a_of(adj, u0) < 3 or a_of(adj, u3) < 2): continue
            comps0 = nbr_components(adj, u0); comps3 = nbr_components(adj, u3)
            for u1 in adj[u0]:
                if D[u1][u3] != 2: continue
                for u2 in adj[u3]:
                    if D[u0][u2] != 2 or u2 not in adj[u1]: continue
                    c1 = next(c for c in comps0 if u1 in c)
                    c2 = next(c for c in comps3 if u2 in c)
                    xs = [x for x in adj[u0] if x not in c1 and (not need_avals or a_of(adj, x) >= 4)]
                    ys = [y for y in adj[u3] if y not in c2]
                    if not xs or not ys: continue
                    for x in xs:
                        case2 = all(y in adj[x] for y in ys)
                        out.append((u0, u1, u2, u3, x, tuple(ys), case2))
    return out

def induces_c6(adj, cyc):
    """cyc = 6 vertices in cyclic order; check distinct, cycle edges present, no chords."""
    if len(set(cyc)) != 6: return False
    for i in range(6):
        if cyc[(i + 1) % 6] not in adj[cyc[i]]: return False
    for i, j in itertools.combinations(range(6), 2):
        if (j - i) % 6 in (1, 5): continue
        if cyc[j] in adj[cyc[i]]: return False
    return True

def has_induced_c6(adj):
    n = len(adj)
    for c in itertools.permutations(range(n), 6):
        if c[0] != min(c) or c[1] > c[5]: continue
        if induces_c6(adj, c): return c
    return None

# ---------------------------------------------------------------- generators
def rand_c4free(n, rng, tries=None):
    """greedy random maximal C4-free graph on n vertices."""
    adj = [set() for _ in range(n)]
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(pairs)
    for u, v in pairs:
        if len(adj[u] & adj[v]) >= 1:      # adding uv would create a C4? no: C4 needs
            pass                            # two common nbrs AFTER adding; check properly
        ok = True
        # adding uv creates a C4 iff some w != u,v has ... check all pairs touched
        adj[u].add(v); adj[v].add(u)
        for w in list(adj[u]):
            if w != v and len(adj[v] & adj[w]) >= 2: ok = False; break
        if ok:
            for w in list(adj[v]):
                if w != u and len(adj[u] & adj[w]) >= 2: ok = False; break
        if ok and len(adj[u] & adj[v]) >= 2: ok = False
        if not ok:
            adj[u].discard(v); adj[v].discard(u)
    return adj

def add_ok(adj, u, v):
    if v in adj[u]: return False
    if len(adj[u] & adj[v]) >= 1: return False   # would give 2 common nbrs? no
    return True

def edge_addable(adj, u, v):
    """adding uv keeps C4-freeness?"""
    if v in adj[u] or u == v: return False
    if len(adj[u] & adj[v]) >= 2: return False
    adj[u].add(v); adj[v].add(u)
    ok = c4free_local(adj, u, v)
    adj[u].discard(v); adj[v].discard(u)
    return ok

def c4free_local(adj, u, v):
    n = len(adj)
    for w in range(n):
        if w != u and len(adj[u] & adj[w]) >= 2: return False
        if w != v and len(adj[v] & adj[w]) >= 2: return False
    return True

# ================================================================= SECTION A
print("=" * 72)
print("SECTION A -- the two certified counterexamples")
CE1 = mk(10, [(0,9),(0,5),(1,5),(2,3),(2,5),(2,6),(2,8),(4,9),(4,6),(5,7),(5,8)])
CE2 = mk(10, [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)])
for nm, g, exp_mass in (("CE-1", CE1, 19), ("CE-2 (=H, G45)", CE2, 25)):
    av = [a_of(g, v) for v in range(10)]
    check(c4free(g), nm + " C4-free")
    check(connected(g), nm + " connected")
    check(sum(av) == exp_mass, nm + " mass")
    p = longest_induced_path(g)
    check(p == 6, nm + " path == 6")
    fr = [f for f in frames(g) if f[6]]
    check(len(fr) > 0, nm + " has a Case-2-forced 3-frame")
    print("  %-16s n=10 a=%s  sum a=%d  l=%.3f  mu=%d  path=%d  case2-frames=%d"
          % (nm, av, sum(av), sum(av)/10.0, min(av), p, len(fr)))
    for f in fr[:3]:
        print("      frame u=%s,%s,%s,%s x=%s ys=%s  a(u0)=%d a(u3)=%d a(x)=%d a(y)=%d"
              % (f[0], f[1], f[2], f[3], f[4], f[5],
                 a_of(g, f[0]), a_of(g, f[3]), a_of(g, f[4]), a_of(g, f[5][0])))

# ================================================================= SECTION B
print("=" * 72)
print("SECTION B -- Lemma G46: Case-2-forced 3-frame  ==>  u0,u1,u2,u3,y,x induce a C6")
rng = random.Random(20260822)
tested = 0; graphs_with = 0
pool = [CE1, CE2]
for n in range(8, 17):
    for _ in range(140):
        g = rand_c4free(n, rng)
        if connected(g): pool.append(g)
for g in pool:
    fs = frames(g, need_avals=False)
    hit = False
    for (u0, u1, u2, u3, x, ys, case2) in fs:
        if not case2: continue
        hit = True
        check(len(ys) == 1, "F5: usable-far set is a singleton in a Case-2-forced frame")
        y = ys[0]
        check(induces_c6(g, (u0, u1, u2, u3, y, x)), "G46 C6 on frame %s" % ((u0,u1,u2,u3,y,x),))
        tested += 1
    if hit: graphs_with += 1
print("  Case-2-forced frames tested: %d  (in %d of %d graphs)" % (tested, graphs_with, len(pool)))
check(tested >= 200, "G46 test is non-vacuous (>=200 frames)")

# also: the a-value-free version -- G46 needs no a-value hypothesis at all
tested_av = 0
for g in pool:
    for (u0, u1, u2, u3, x, ys, case2) in frames(g, need_avals=True):
        if case2:
            tested_av += 1
print("  of which frames also meeting a(u0)>=3,a(u3)>=2,a(x)>=4 : %d" % tested_av)

# ================================================================= SECTION C
print("=" * 72)
print("SECTION C -- kill table: candidate hypotheses vs the two counterexamples")
cands = [
    ("l(G) > 3            (IMPLIED by the live class)", lambda g, f: mass(g) > 3 * len(g)),
    ("mu(G) >= 2          (peeling; F4)", lambda g, f: min(a_of(g, v) for v in range(len(g))) >= 2),
    ("mu(G) >= 3", lambda g, f: min(a_of(g, v) for v in range(len(g))) >= 3),
    ("a(x) >= 5           (surcharge B1)", lambda g, f: a_of(g, f[4]) >= 5),
    ("a(u0) >= 4          (surcharge B2)", lambda g, f: a_of(g, f[0]) >= 4),
    ("a(u3) >= 3          (surcharge B3)", lambda g, f: a_of(g, f[3]) >= 3),
    ("a(y)  >= 3          (surcharge B4)", lambda g, f: a_of(g, f[5][0]) >= 3),
    ("triangle-free", lambda g, f: not any(q in g[p] for v in range(len(g))
                                           for p, q in itertools.combinations(g[v], 2))),
    ("delta(G) >= 3", lambda g, f: min(len(g[v]) for v in range(len(g))) >= 3),
]
print("  hypothesis                                    CE-1 holds?  CE-2 holds?   kills both?")
kills = []
for nm, fn in cands:
    r = []
    for g in (CE1, CE2):
        f = [f for f in frames(g) if f[6]][0]
        r.append(fn(g, f))
    print("  %-45s %-12s %-12s %s" % (nm, r[0], r[1], (not r[0]) and (not r[1])))
    if (not r[0]) and (not r[1]): kills.append(nm)
check(any(nm.startswith("l(G) > 3") for nm in kills), "l > 3 kills both counterexamples")

# ================================================================= SECTION D
print("=" * 72)
print("SECTION D -- decisive experiment: C4-free + induced C6 + no induced P7, maximise l")
print("  (randomised local search on Sigma a - 3n; NO SAT, NO exhaustive enumeration)")

def score(g):
    return mass(g) - 3 * len(g)

def local_search(n, rng, iters, seed_adj=None, require_frame=False):
    if seed_adj is None:
        g = rand_c4free(n, rng)
    else:
        g = [set(s) for s in seed_adj]
    def feasible(gg):
        if not c4free(gg): return False
        if not connected(gg): return False
        if has_induced_path(gg, 7): return False
        if require_frame:
            if not any(f[6] for f in frames(gg)): return False
        else:
            if has_induced_c6(gg) is None: return False
        return True
    # repair the seed down to feasibility by deleting edges
    guard = 0
    while not feasible(g) and guard < 400:
        guard += 1
        es = [(u, v) for u in range(n) for v in g[u] if u < v]
        if not es: break
        u, v = rng.choice(es); g[u].discard(v); g[v].discard(u)
    if not feasible(g): return None
    best = score(g); bestg = [set(s) for s in g]
    for _ in range(iters):
        u, v = rng.sample(range(n), 2)
        if v in g[u]:
            g[u].discard(v); g[v].discard(u); undo = ("add", u, v)
        else:
            g[u].add(v); g[v].add(u); undo = ("del", u, v)
        if feasible(g) and score(g) >= best:
            if score(g) > best:
                best = score(g); bestg = [set(s) for s in g]
        else:
            if undo[0] == "add": g[u].add(v); g[v].add(u)
            else: g[u].discard(v); g[v].discard(u)
    return best, bestg

rec = (-10 ** 9, None, 0)
for n in (8, 10, 12, 14, 16):
    for trial in range(14):
        r = local_search(n, rng, 900)
        if r is None: continue
        s, gg = r
        if s > rec[0]: rec = (s, gg, n)
    print("  n=%2d  best Sigma a - 3n so far = %d   (l = %.3f at n=%d)"
          % (n, rec[0], (rec[0] + 3 * rec[2]) / float(rec[2]), rec[2]))
best_s, best_g, best_n = rec
print("  RESULT: over the whole search, max (Sigma a - 3n) = %d, i.e. max l = %.4f"
      % (best_s, (best_s + 3 * best_n) / float(best_n)))
check(best_s <= 0, "SEARCH FOUND NO C4-free graph with an induced C6, no induced P7 and l > 3")

# ================================================================= SECTION E
print("=" * 72)
print("SECTION E -- same search, restricted to graphs carrying a Case-2-forced 3-frame")
rec2 = (-10 ** 9, None, 0)
seeds = [CE1, CE2]
for n in (10, 11, 12, 13, 14):
    for trial in range(12):
        seed = None
        if n == 10 and trial < 2: seed = seeds[trial]
        r = local_search(n, rng, 900, seed_adj=seed, require_frame=True)
        if r is None: continue
        s, gg = r
        if s > rec2[0]: rec2 = (s, gg, n)
    print("  n=%2d  best Sigma a - 3n so far = %d   (l = %.3f at n=%d)"
          % (n, rec2[0], (rec2[0] + 3 * rec2[2]) / float(rec2[2]), rec2[2]))
print("  RESULT: max (Sigma a - 3n) over Case-2-forced bad graphs = %d, max l = %.4f"
      % (rec2[0], (rec2[0] + 3 * rec2[2]) / float(rec2[2])))
if rec2[1] is not None:
    es = sorted((u, v) for u in range(rec2[2]) for v in rec2[1][u] if u < v)
    print("  best witness edges:", es)
check(rec2[0] <= 0, "SEARCH FOUND NO Case-2-forced bad graph with l > 3")

print("=" * 72)
print("FAILURES:", FAIL)
sys.exit(0 if FAIL == 0 else 2)
