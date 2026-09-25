#!/usr/bin/env python3
"""
Round 5 (owner-w133).  Target: RES = empty.

(A) THE NAIL (planner's round-5 item 1): the two readings of (R3) in
    w133_res3_search.py's R3_holds() docstring are NOT equivalent.
      (R3a)  no pair at distance >= 3 whose a-values are (>=3, >=2)
      (R3b)  every vertex with a >= 3 has eccentricity <= 2
    (R3b) => (R3a) always.  The converse fails exactly on the low-a side
    (a = 1 vertices).  We exhibit explicit witnesses.
(B) Numerical backing for the round-5 lemmas G16 / G17 / G18 (all are general
    C4-free facts, so they are testable on real graphs, unlike RES itself).
(C) Structured hunt for a member of RES(b) (never exhaustive search).
"""
import sys, itertools, random
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, hoffman_singleton,
                                    greedy_long_induced_path)
from w133_res3_search import er_polarity, has_triangle

FAIL = 0


def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("  *** ASSERT FAILED: " + msg)
    return cond


def pack(name, n, E):
    adj = neighbours(E, n)
    if not connected(adj):
        return None
    D = alldist(adj)
    e, r = ecc_rad(D)
    a = avec(adj)
    return dict(name=name, n=n, adj=adj, D=D, ecc=e, rad=r, diam=max(e),
                a=a, S=sum(a), l=sum(a) / n, c4free=not has_c4(adj))


def R3a(f):
    """no pair at distance >= 3 with a-values (>=3, >=2)"""
    a, D, n = f['a'], f['D'], f['n']
    bad = [(u, v) for u in range(n) for v in range(n)
           if u != v and D[u][v] >= 3 and a[u] >= 3 and a[v] >= 2]
    return not bad, bad


def R3b(f):
    """every vertex with a >= 3 has ecc <= 2"""
    bad = [v for v in range(f['n']) if f['a'][v] >= 3 and f['ecc'][v] > 2]
    return not bad, bad


def RES(f, form):
    ok = (f['c4free'] and f['rad'] == 2 and f['diam'] == 3 and f['l'] > 3)
    return ok and (R3a(f)[0] if form == 'a' else R3b(f)[0])


# ---------------------------------------------------------------- constructions
def hs_plus_pendant():
    n, E = hoffman_singleton()
    return n + 1, list(E) + [(0, n)]          # leaf at vertex 0


def hs_plus_triangle_leaf():
    n, E = hoffman_singleton()
    adj = neighbours(E, n)
    t = min(adj[0])                            # 0 ~ t, HS is triangle-free
    return n + 1, list(E) + [(0, n), (t, n)]   # new vertex on the edge 0-t


def er_plus_pendant(q):
    n, E = er_polarity(q)
    return n + 1, list(E) + [(0, n)]


def rand_c4free(n, seed, tries=None):
    """greedy random maximal C4-free graph.  Adding uv is safe iff no pair
    acquires a second common neighbour, i.e. N(v) meets no N(w), w in N(u)\\{v}
    (and symmetrically)."""
    rng = random.Random(seed)
    adj = [set() for _ in range(n)]
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(pairs)
    E = []
    for u, v in pairs:
        if any(adj[v] & adj[w] for w in adj[u] if w != v):
            continue
        if any(adj[u] & adj[w] for w in adj[v] if w != u):
            continue
        adj[u].add(v); adj[v].add(u); E.append((u, v))
    return n, E


# ---------------------------------------------------------------- (A) the nail
print("=== (A) THE NAIL: (R3a) vs (R3b) are NOT equivalent ===")
witnesses = []
for name, (n, E) in [("HS + pendant leaf", hs_plus_pendant()),
                     ("HS + triangle-leaf", hs_plus_triangle_leaf()),
                     ("ER_5 + pendant leaf", er_plus_pendant(5)),
                     ("ER_7 + pendant leaf", er_plus_pendant(7))]:
    f = pack(name, n, E)
    oa, _ = R3a(f)
    ob, bb = R3b(f)
    print(f"  {f['name']:<20} n={f['n']:<3} C4free={f['c4free']} rad={f['rad']} "
          f"diam={f['diam']} l={f['l']:.3f} | (R3a)={oa} (R3b)={ob} | "
          f"in RES(a)={RES(f,'a')} in RES(b)={RES(f,'b')}")
    if RES(f, 'a') and not RES(f, 'b'):
        witnesses.append(f)
        # the offending high vertices sit at distance 3 from the a=1 vertex
        v = bb[0]
        far = [w for w in range(f['n']) if f['D'][v][w] == 3]
        print(f"      witness: a[{v}]={f['a'][v]}>=3, ecc={f['ecc'][v]}=3; "
              f"the {len(far)} vertices at distance 3 from it all have "
              f"a-value {sorted({f['a'][w] for w in far})} (so (R3a) is silent)")
check(len(witnesses) >= 1, "no (R3a)-but-not-(R3b) witness found")
print(f"  ==> RES(a) is INHABITED ({len(witnesses)} explicit members); "
      f"RES(b) members among them: 0")

# every witness must still satisfy the conjecture
for f in witnesses:
    P = greedy_long_induced_path(f['adj'])
    check(len(P) >= 6, f"{f['name']}: path certificate {len(P)} < 6")
print(f"  conjecture unharmed on the witnesses: path certificates "
      f"{[len(greedy_long_induced_path(f['adj'])) for f in witnesses]} (need >= 6)")

# --------------------------------------------- (B) general C4-free lemma checks
print()
print("=== (B) numerical backing for the round-5 lemmas ===")

pool = []
for nm, (n, E) in [("Petersen", (10, [(i, (i + 1) % 5) for i in range(5)] +
                                 [(i + 5, (i + 2) % 5 + 5) for i in range(5)] +
                                 [(i, i + 5) for i in range(5)])),
                   ("HS", hoffman_singleton()),
                   ("HS+pendant", hs_plus_pendant()),
                   ("HS+trileaf", hs_plus_triangle_leaf()),
                   ("ER_5", er_polarity(5)), ("ER_7", er_polarity(7)),
                   ("ER_11", er_polarity(11)), ("ER_5+pend", er_plus_pendant(5))]:
    f = pack(nm, n, E)
    if f:
        pool.append(f)
for s in range(40):
    n = 8 + (s % 18)
    f = pack(f"rand{n}_{s}", *rand_c4free(n, 1000 + s))
    if f:
        pool.append(f)
pool = [f for f in pool if f['c4free']]
print(f"  test pool: {len(pool)} connected C4-free graphs "
      f"(n from {min(f['n'] for f in pool)} to {max(f['n'] for f in pool)})")

# G18 identity: ecc(h) = 2  =>  n = 1 + sum_{x in N(h)} d(x) - 2 t(h)
cnt = 0
for f in pool:
    adj, a = f['adj'], f['a']
    for h in range(f['n']):
        if f['ecc'][h] != 2:
            continue
        t = sum(1 for x in adj[h] for y in adj[h] if x < y and y in adj[x])
        check(f['n'] == 1 + sum(len(adj[x]) for x in adj[h]) - 2 * t,
              f"G18 identity fails at {f['name']} vertex {h}")
        check(a[h] == len(adj[h]) - t, f"a = d - t fails at {f['name']} v{h}")
        cnt += 1
print(f"  G18  n = 1 + sum_{{x~h}} d(x) - 2t(h)  for ecc(h)=2 : {cnt} instances, "
      f"{'0 failures' if not FAIL else 'FAILURES'}")

# G16 confinement: d(u,z)=3  =>  |ball2(u) cap ball2(z)| <= d(u)d(z)+d(u)+d(z)
cnt = 0
for f in pool:
    adj, D = f['adj'], f['D']
    for u in range(f['n']):
        for z in range(u + 1, f['n']):
            if D[u][z] != 3:
                continue
            S = [v for v in range(f['n']) if D[u][v] <= 2 and D[z][v] <= 2]
            du, dz = len(adj[u]), len(adj[z])
            check(len(S) <= du * dz + du + dz,
                  f"G16 bound fails at {f['name']} pair {u},{z}: "
                  f"{len(S)} > {du*dz+du+dz}")
            cnt += 1
print(f"  G16  |ball2(u) cap ball2(z)| <= d(u)d(z)+d(u)+d(z) : {cnt} distance-3 "
      f"pairs, {'0 failures' if not FAIL else 'FAILURES'}")

# G17 Bonferroni: for every vertex subset S, sum_S a(h) <= |N(S)| + #pairs-with-cn
cnt = 0
for f in pool:
    adj, a, n = f['adj'], f['a'], f['n']
    rng = random.Random(7 * n)
    subsets = [[v for v in range(n) if a[v] >= 3]]
    for _ in range(6):
        k = rng.randint(2, min(8, n))
        subsets.append(rng.sample(range(n), k))
    for S in subsets:
        if len(S) < 2:
            continue
        NS = set().union(*[adj[h] for h in S])
        P = sum(1 for i in range(len(S)) for j in range(i + 1, len(S))
                if adj[S[i]] & adj[S[j]])
        check(sum(a[h] for h in S) <= len(NS) + P,
              f"G17 Bonferroni fails at {f['name']} on |S|={len(S)}")
        cnt += 1
print(f"  G17  sum_S a(h) <= |N(S)| + #(pairs with a common neighbour) : {cnt} "
      f"subsets, {'0 failures' if not FAIL else 'FAILURES'}")

# (*) fibre count at a centre:  l>3 and ecc(c)=2  =>  sum_{b in B}(a(b)-2) > 3+d(c)
cnt = 0
for f in pool:
    if f['l'] <= 3:
        continue
    adj, a, D = f['adj'], f['a'], f['D']
    for c in range(f['n']):
        if f['ecc'][c] != 2:
            continue
        B = [b for b in range(f['n']) if D[c][b] == 2]
        check(sum(a[b] - 2 for b in B) > 3 + len(adj[c]),
              f"(*) fails at {f['name']} centre {c}")
        cnt += 1
print(f"  (*)  sum_{{b in B(c)}}(a(b)-2) > 3 + d(c)  for l>3, ecc(c)=2 : {cnt} "
      f"centres, {'0 failures' if not FAIL else 'FAILURES'}")

# corollary actually used: a centre always has a HIGH vertex at distance exactly 2
cnt = 0
for f in pool:
    if f['l'] <= 3:
        continue
    for c in range(f['n']):
        if f['ecc'][c] != 2:
            continue
        check(any(f['a'][b] >= 3 for b in range(f['n']) if f['D'][c][b] == 2),
              f"G17b fails at {f['name']} centre {c}")
        cnt += 1
print(f"  G17b every centre of an l>3 C4-free graph has a high vertex at "
      f"distance exactly 2 : {cnt} centres, "
      f"{'0 failures' if not FAIL else 'FAILURES'}")

# ------------------------------------------------- (C) structured hunt for RES(b)
print()
print("=== (C) structured hunt for a member of RES(b) (no exhaustive search) ===")
cands = []
n0, E0 = hoffman_singleton()
adj0 = neighbours(E0, n0)


def hs_minus(drop):
    keep = [v for v in range(n0) if v not in drop]
    ix = {v: i for i, v in enumerate(keep)}
    return len(keep), [(ix[u], ix[v]) for u, v in E0 if u in ix and v in ix]


def subdivide(n, E, e):
    E = [x for x in E if x != e]
    return n + 1, E + [(e[0], n), (e[1], n)]


cands.append(("HS+pendant", hs_plus_pendant()))
cands.append(("HS+trileaf", hs_plus_triangle_leaf()))
cands.append(("HS subdiv edge", subdivide(n0, list(E0), tuple(sorted((0, min(adj0[0])))))))
cands.append(("HS-1", hs_minus({0})))
cands.append(("HS-1+pendant", (hs_minus({0})[0] + 1,
                               hs_minus({0})[1] + [(0, hs_minus({0})[0])])))
for k in (2, 3, 5, 8, 12):
    cands.append((f"HS-{k}", hs_minus(set(range(k)))))
for q in (5, 7, 11):
    n, E = er_polarity(q)
    cands.append((f"ER_{q}", (n, E)))
    cands.append((f"ER_{q}+pendant", er_plus_pendant(q)))
    cands.append((f"ER_{q}-1", (n - 1, [(u, v) for u, v in E if u < n - 1 and v < n - 1])))
    cands.append((f"ER_{q} subdiv", subdivide(n, list(E), E[0])))
for s in range(240):                                    # random maximal C4-free
    cands.append((f"rand{18+s%42}_{s}", rand_c4free(18 + s % 42, 5000 + s)))
# same families with one leaf / one triangle-leaf grafted on (pushes diam to 3)
for s in range(120):
    n, E = rand_c4free(18 + s % 42, 9000 + s)
    adjr = neighbours(E, n)
    cands.append((f"randL{n}_{s}", (n + 1, list(E) + [(0, n)])))
    if adjr[0]:
        t = min(adjr[0])
        cands.append((f"randT{n}_{s}", (n + 1, list(E) + [(0, n), (t, n)])))

hits_a, hits_b, live = [], [], 0
for nm, (n, E) in cands:
    f = pack(nm, n, E)
    if f is None or not f['c4free']:
        continue
    if f['rad'] == 2 and f['diam'] == 3 and f['l'] > 3:
        live += 1
        if RES(f, 'a'):
            hits_a.append(nm)
        if RES(f, 'b'):
            hits_b.append(nm)
            print(f"  *** RES(b) MEMBER: {nm} n={f['n']} l={f['l']:.3f}")
print(f"  candidates in the plain class (C4-free, rad 2, diam 3, l>3): {live}")
print(f"  of them in RES(a): {len(hits_a)}  -> {hits_a}")
print(f"  of them in RES(b): {len(hits_b)}")

print()
print(f"=== TOTAL ASSERT FAILURES: {FAIL} ===")
sys.exit(2 if FAIL else 0)
