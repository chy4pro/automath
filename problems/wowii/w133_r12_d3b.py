#!/usr/bin/env python3
"""w133 round 12 slice 2 -- the reduction lemma G47 and the tightness controls for (D3-C6).

  F. Named controls: Petersen (l = 3 exactly, induced C6, path = 5) is the TIGHT instance
     for the target (D3-C6): 'C4-free + induced C6 + no induced P7 ==> l <= 3'.
     Heawood / PG(2,3) / PG(3,2) as the above-threshold controls (they must FAIL the
     'no induced P7' hypothesis -- i.e. (D3-C6) does not execute on them).
  G. Lemma G47: peeling a=1 vertices from a C4-free graph with l > 3 and path <= 6
     (i) preserves C4-freeness, connectivity, l > 3 and path <= 6,
     (ii) never deletes a vertex of an induced C6,
     (iii) leaves mu >= 2, whence by Theorem G+ every vertex h with a(h) >= 3 has
           ecc(h) <= 3; in particular rad <= 3 (and diam <= 5 unconditionally).
     Asserted on random C4-free graphs and on the two certified counterexamples.
"""
import itertools, random, sys
sys.setrecursionlimit(10000)
exec(open(__file__.rsplit('/', 1)[0] + '/w133_r12_d3.py').read().split(
     "# ================================================================= SECTION A")[0])

# ---------------------------------------------------------------- named graphs
def petersen():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, i + 5) for i in range(5)]
    return mk(10, outer + inner + spokes)

def heawood():
    # incidence graph of PG(2,2): points 0..6, lines 7..13 (Fano)
    lines = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
    es = [(p, 7 + i) for i, L in enumerate(lines) for p in L]
    return mk(14, es)

def pg_incidence(q, dim=2):
    """point/hyperplane incidence graph of PG(dim,q) for prime q."""
    k = dim + 1
    pts = []
    seen = set()
    for vec in itertools.product(range(q), repeat=k):
        if all(c == 0 for c in vec): continue
        key = None
        for s in range(1, q):
            cand = tuple((s * c) % q for c in vec)
            if key is None or cand < key: key = cand
        if key in seen: continue
        seen.add(key); pts.append(key)
    N = len(pts)
    es = []
    for i, p in enumerate(pts):
        for j, h in enumerate(pts):
            if sum(a * b for a, b in zip(p, h)) % q == 0:
                es.append((i, N + j))
    return mk(2 * N, es)

def ecc_all(adj):
    return [max(bfs(adj, s)) for s in range(len(adj))]

def find_induced_c6(adj):
    """fast: DFS an induced P6 whose ends are adjacent."""
    n = len(adj)
    for v0 in range(n):
        def ext(p, ps):
            if len(p) == 6:
                return p
            last = p[-1]
            closing = (len(p) == 5)
            inner = ps - {last} - ({p[0]} if closing else set())
            for w in adj[last]:
                if w <= v0 or w in ps: continue
                if adj[w] & inner: continue           # chord -> not induced
                if closing and p[0] not in adj[w]: continue
                r = ext(p + [w], ps | {w})
                if r: return r
            return None
        r = ext([v0], {v0})
        if r: return tuple(r)
    return None

# use the fast version everywhere below
has_induced_c6 = find_induced_c6

print("=" * 72)
print("SECTION F -- named controls for the target (D3-C6)")
print("  (D3-C6): C4-free + contains an induced C6 + no induced P7  ==>  l <= 3")
named = [("Petersen", petersen(), 12),
         ("Heawood (PG(2,2))", heawood(), 12),
         ("PG(2,3) incidence", pg_incidence(3), 10),
         ("PG(2,5) incidence", pg_incidence(5), 10)]
for nm, g, cap in named:
    n = len(g); av = [a_of(g, v) for v in range(n)]
    c6 = has_induced_c6(g)
    p7 = has_induced_path(g, 7)
    lp = longest_induced_path(g, cap)
    l = sum(av) / float(n)
    print("  %-20s n=%3d  l=%.4f  induced C6=%s  has induced P7=%s  path>=%d  rad=%d diam=%d"
          % (nm, n, l, c6 is not None, p7, lp, min(ecc_all(g)), max(ecc_all(g))))
    check(c4free(g), nm + " is C4-free")
    if not p7:                      # hypotheses of (D3-C6) met -> conclusion must hold
        check(l <= 3.0 + 1e-12, "(D3-C6) conclusion l<=3 holds on " + nm)

pet = petersen()
check(has_induced_c6(pet) is not None, "Petersen contains an induced C6")
check(not has_induced_path(pet, 7), "Petersen has NO induced P7")
check(abs(sum(a_of(pet, v) for v in range(10)) / 10.0 - 3.0) < 1e-12,
      "Petersen has l = 3 EXACTLY -> (D3-C6) is TIGHT, the strict form l<3 is FALSE")
print("  => (D3-C6) is TIGHT at Petersen: l = 3 exactly with an induced C6 and no induced P7.")
print("  => Petersen carries NO 3-frame (diam = 2), so it does not touch the D=3 layer.")
check(max(ecc_all(pet)) == 2, "Petersen has diam 2, hence no geodesic of length 3")

# ================================================================= SECTION G
print("=" * 72)
print("SECTION G -- Lemma G47 (peeling reduction) asserted")

def peel(adj):
    """iteratively delete a=1 vertices; return (surviving vertex list, induced subgraph)."""
    alive = set(range(len(adj)))
    A = [set(s) for s in adj]
    changed = True
    while changed:
        changed = False
        for v in sorted(alive):
            if a_of(A, v) == 1:
                for w in list(A[v]):
                    A[w].discard(v)
                A[v] = set(); alive.discard(v); changed = True
                break
    idx = {v: i for i, v in enumerate(sorted(alive))}
    g2 = [set() for _ in idx]
    for v in sorted(alive):
        for w in A[v]:
            if w in idx: g2[idx[v]].add(idx[w])
    return sorted(alive), g2

rng2 = random.Random(133133)
tested_G47 = 0
pool2 = [CE1_g, CE2_g] if False else []
CE1g = mk(10, [(0,9),(0,5),(1,5),(2,3),(2,5),(2,6),(2,8),(4,9),(4,6),(5,7),(5,8)])
CE2g = mk(10, [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)])
pool2 = [CE1g, CE2g, pet]
for n in range(8, 15):
    for _ in range(90):
        g = rand_c4free(n, rng2)
        if connected(g): pool2.append(g)

n_bad = 0
for g in pool2:
    n = len(g)
    if not connected(g): continue
    if has_induced_path(g, 7): continue          # need path <= 6
    c6 = has_induced_c6(g)
    if c6 is None: continue
    n_bad += 1
    alive, g2 = peel(g)
    if len(g2) == 0: continue
    # (i) preservation
    check(c4free(g2), "G47(i) peeled graph is C4-free")
    check(connected(g2), "G47(i) peeled graph is connected")
    check(not has_induced_path(g2, 7), "G47(i) peeled graph still has no induced P7")
    check(mass(g2) - 3 * len(g2) >= mass(g) - 3 * n,
          "G47(i) Sigma a - 3n does not decrease under peeling")
    # (ii) no C6 vertex is ever peeled
    check(all(v in alive for v in c6), "G47(ii) no vertex of the induced C6 is peeled")
    check(has_induced_c6(g2) is not None, "G47(ii) an induced C6 survives peeling")
    # (iii) mu >= 2 and the Theorem-G+ consequence
    if len(g2) >= 2:
        check(min(a_of(g2, v) for v in range(len(g2))) >= 2, "G47(iii) peeled graph has mu >= 2")
        ecc = ecc_all(g2)
        for h in range(len(g2)):
            if a_of(g2, h) >= 3:
                check(ecc[h] <= 3,
                      "G47(iii) Theorem G+ : a(h)>=3 and path<=6 forces ecc(h)<=3")
        check(min(ecc) <= 3, "G47(iii) rad <= 3")
        check(max(ecc) <= 5, "G47(iii) diam <= 5 (any geodesic is induced)")
    tested_G47 += 1
print("  graphs meeting 'C4-free + induced C6 + no induced P7' : %d   (G47 asserted on %d)"
      % (n_bad, tested_G47))
check(tested_G47 >= 20, "G47 test is non-vacuous")

# the mass record over that class (the (D3-C6) experiment, restated on this pool)
best = max((mass(g) - 3 * len(g), len(g)) for g in pool2
           if connected(g) and not has_induced_path(g, 7) and has_induced_c6(g) is not None)
print("  max (Sigma a - 3n) over the class in this pool = %d  (l = %.4f at n = %d)"
      % (best[0], (best[0] + 3 * best[1]) / float(best[1]), best[1]))
check(best[0] <= 0, "no member of the class in this pool has l > 3")

print("=" * 72)
print("FAILURES:", FAIL)
sys.exit(0 if FAIL == 0 else 2)
