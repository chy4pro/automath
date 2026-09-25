#!/usr/bin/env python3
"""w133 round-9 slice-2 adjudication: verify the two Qwen control instances.
NO SAT. Pure explicit-graph checks on two named constructions (Petersen, STS(15)
incidence graph) + a bounded induced-path search. Q15 claims Petersen path=5;
Q16 claims STS(15): C4-free, a(P)=7, a(B)=3, l=4.2, rad=3, diam=4, path>=9.
Also: does the (D)-frame census of round 8 pin l on admissible frames? (separate)
"""
from itertools import combinations
import sys

fail = 0
def check(name, got, want):
    global fail
    ok = (got == want)
    if not ok:
        fail += 1
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}: got {got!r}, expected {want!r}")

def nbrs(adj, v): return adj[v]

def is_c4_free(V, adj):
    for u, v in combinations(V, 2):
        if len(adj[u] & adj[v]) >= 2:
            return False
    return True

def has_triangle(V, adj):
    for u in V:
        for a, b in combinations(adj[u], 2):
            if b in adj[a]:
                return True
    return False

def alpha(S, adj):
    S = list(S)
    best = 0
    def rec(rem, cur):
        nonlocal best
        if not rem:
            best = max(best, cur); return
        if cur + len(rem) <= best: return
        v = rem[0]
        # take v
        rec([u for u in rem[1:] if u not in adj[v]], cur + 1)
        # skip v
        rec(rem[1:], cur)
    rec(S, 0)
    return best

def bfs(adj, s, V):
    dist = {s: 0}; q = [s]
    while q:
        nq = []
        for u in q:
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1; nq.append(w)
        q = nq
    return dist

def ecc_rad_diam(V, adj):
    ecc = {}
    for v in V:
        d = bfs(adj, v, V)
        if len(d) != len(V): return None
        ecc[v] = max(d.values())
    return ecc, min(ecc.values()), max(ecc.values())

def longest_induced_path(V, adj, cap=None):
    """number of VERTICES of a longest induced path; exact DFS, prune at cap."""
    best = 1
    Vl = list(V)
    def extend(path, pset, forb):
        nonlocal best
        best = max(best, len(path))
        if cap and best >= cap: return
        last = path[-1]
        for w in adj[last]:
            if w in pset or w in forb: continue
            # w must have no neighbour in path except last
            if len(adj[w] & pset) != 1: continue
            extend(path + [w], pset | {w}, forb)
    for v in Vl:
        extend([v], {v}, set())
    return best

print("=== CONTROL A: Petersen (Kneser K(5,2)) — Q15's control ===")
pts = list(combinations(range(1, 6), 2))
Vp = list(range(10))
idx = {p: i for i, p in enumerate(pts)}
adjp = {i: set() for i in Vp}
for a, b in combinations(pts, 2):
    if not (set(a) & set(b)):
        adjp[idx[a]].add(idx[b]); adjp[idx[b]].add(idx[a])
check("Petersen edges", sum(len(adjp[v]) for v in Vp) // 2, 15)
check("Petersen C4-free", is_c4_free(Vp, adjp), True)
check("Petersen triangle-free", has_triangle(Vp, adjp), False)
ep, rp, dp = ecc_rad_diam(Vp, adjp)
check("Petersen rad", rp, 2); check("Petersen diam", dp, 2)
lp = sum(alpha(adjp[v], adjp) for v in Vp) / 10
check("Petersen l = mean a(v)", lp, 3.0)
pathp = longest_induced_path(Vp, adjp)
check("Petersen path (vertices) [Q15 claims 5]", pathp, 5)

print("=== CONTROL B: STS(15)=PG(3,2) point-line incidence graph — Q16's control ===")
# lines of PG(3,2): {x,y,x^y} over nonzero vectors of F_2^4
P = list(range(1, 16))
lines = set()
for x, y in combinations(P, 2):
    lines.add(frozenset((x, y, x ^ y)))
lines = sorted(lines, key=lambda s: sorted(s))
check("STS(15) block count", len(lines), 35)
Vs = [('p', p) for p in P] + [('b', i) for i in range(len(lines))]
adjs = {v: set() for v in Vs}
for i, L in enumerate(lines):
    for p in L:
        adjs[('p', p)].add(('b', i)); adjs[('b', i)].add(('p', p))
check("STS incidence n", len(Vs), 50)
check("STS incidence C4-free", is_c4_free(Vs, adjs), True)
check("STS incidence triangle-free (bipartite)", has_triangle(Vs, adjs), False)
aP = {alpha(adjs[('p', p)], adjs) for p in P}
aB = {alpha(adjs[('b', i)], adjs) for i in range(len(lines))}
check("a(point) set [Q16 claims 7]", aP, {7})
check("a(block) set [Q16 claims 3]", aB, {3})
S = sum(alpha(adjs[v], adjs) for v in Vs)
check("Sum a(v) [Q16 claims 210]", S, 210)
check("l = S/n [Q16 claims 4.2]", S / len(Vs), 4.2)
es, rs, ds = ecc_rad_diam(Vs, adjs)
check("STS rad [Q16 claims 3]", rs, 3)
check("STS diam [Q16 claims 4]", ds, 4)
check("point eccentricities", {es[('p', p)] for p in P}, {3})
check("block eccentricities", {es[('b', i)] for i in range(35)}, {4})
mu = min(alpha(adjs[v], adjs) for v in Vs)
check("mu = min a [Q16 claims 3]", mu, 3)
# path: exact search is heavy; cap at 12 to confirm >= 9 comfortably
pth = longest_induced_path(Vs, adjs, cap=12)
print(f"  [INFO] STS(15) induced path >= {pth} (search capped at 12); "
      f"Q16 claims >= 9 > rad+4 = 7")
check("STS path >= 9 (Q16's claim)", pth >= 9, True)
print(f"=== TOTAL FAILURES (controls A+B): {fail} ===")

# --- appended round-9 slice-2: non-vacuity witness for Q15's partial theorem ---
# Q15 proves: C4-free + triangle-free + delta>=4 + diam D>=3 ==> path >= D+4.
# Its OWN control (Petersen) has delta=3 and diam=2 -> does NOT satisfy the
# hypotheses, so the theorem was delivered untested.  PG(2,3) incidence graph
# (26 vertices, 4-regular, girth 6, diam 3) is the smallest natural witness.
print("=== NON-VACUITY WITNESS for Q15's theorem: PG(2,3) incidence graph ===")
q = 3
pts3 = []
for a in range(q):
    for b in range(q):
        pts3.append((1, a, b))
for a in range(q):
    pts3.append((0, 1, a))
pts3.append((0, 0, 1))
def dot(u, v): return sum(x * y for x, y in zip(u, v)) % q
Vg = [('P', i) for i in range(13)] + [('L', j) for j in range(13)]
adjg = {v: set() for v in Vg}
for i, p in enumerate(pts3):
    for j, L in enumerate(pts3):
        if dot(p, L) == 0:
            adjg[('P', i)].add(('L', j)); adjg[('L', j)].add(('P', i))
check("PG(2,3) n", len(Vg), 26)
check("PG(2,3) 4-regular", {len(adjg[v]) for v in Vg}, {4})
check("PG(2,3) C4-free", is_c4_free(Vg, adjg), True)
check("PG(2,3) triangle-free", has_triangle(Vg, adjg), False)
eg, rg, dg = ecc_rad_diam(Vg, adjg)
check("PG(2,3) rad", rg, 3); check("PG(2,3) diam D", dg, 3)
lg = sum(alpha(adjg[v], adjg) for v in Vg) / 26
check("PG(2,3) l = 4 > 3", lg, 4.0)
pg = longest_induced_path(Vg, adjg, cap=9)
print(f"  [INFO] PG(2,3) induced path >= {pg}; Q15's theorem demands >= D+4 = 7")
check("Q15 theorem conclusion holds on witness", pg >= dg + 4, True)
print(f"=== TOTAL FAILURES (incl. appendix): {fail} ===")
sys.exit(0 if fail == 0 else 2)
