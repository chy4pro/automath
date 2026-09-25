#!/usr/bin/env python3
"""
w133 round 11 slice 2 (owner-w133) — adjudication of the §23 S3 judge report
(problems/wowii/w133_S3_R23_opus.md).  Three things are checked here, all from primary data:

 (A) the judge's counterexample H, from its edge list alone -- every claimed property;
 (B) whether H also touches G36 (d=4) or G37 (d=3 Case 1) -- the judge says no, owner checks;
 (C) defect B10: the peeling slack arithmetic, leaf vs triangle-leaf, on CE-1.

NO SAT.  Explicit graphs; exhaustive induced-path DFS on n=10.
"""
from itertools import combinations
from collections import deque

FAIL = 0
def check(c, m):
    global FAIL
    if not c: FAIL += 1; print("FAIL:", m)
    else: print("  ok:", m)

def build(E, n):
    g = [set() for _ in range(n)]
    for u, v in E: g[u].add(v); g[v].add(u)
    return g
def c4_free(g):
    return not [(u, v) for u, v in combinations(range(len(g)), 2) if len(g[u] & g[v]) >= 2]
def bfs(g, s):
    d = [-1]*len(g); d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for w in g[u]:
            if d[w] < 0: d[w] = d[u]+1; q.append(w)
    return d
def a_val(g, v):
    nb = sorted(g[v]); return len(nb) - sum(1 for x, y in combinations(nb, 2) if y in g[x])
def comps(g, v):
    nb = sorted(g[v]); c = {u: {u} for u in nb}
    for x, y in combinations(nb, 2):
        if y in g[x]:
            s = c[x] | c[y]
            for z in s: c[z] = s
    out = []
    for u in nb:
        f = frozenset(c[u])
        if f not in out: out.append(f)
    return out
def longest_induced_path(g):
    best = [0, None]
    def dfs(P, inP, blocked):
        if len(P) > best[0]: best[0] = len(P); best[1] = list(P)
        for w in g[P[-1]]:
            if w in inP or w in blocked: continue
            dfs(P+[w], inP | {w}, blocked | set(g[P[-1]]))
    for s in range(len(g)): dfs([s], {s}, set())
    return best

print("=== (A) judge's counterexample H, re-verified from the edge list ===")
EH = [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
H = build(EH, 10); n = 10
A = {v: a_val(H, v) for v in range(n)}
check(c4_free(H), "H is C4-free")
check(all(x >= 0 for x in bfs(H, 0)), "H is connected")
check(min(A.values()) == 2, "mu(H) = 2  (F4 form holds; NO peeling possible)  a=%r" % (A,))
dH = [bfs(H, s) for s in range(n)]
check(dH[2][8] == 3 and dH[2][1] == 1 and dH[2][0] == 2, "2-1-0-8 is a geodesic of length 3")
check(A[2] == 3, "a(u0)=a(2)=3 >= 3"); check(A[8] == 2, "a(u3)=a(8)=2 >= 2")
c2 = comps(H, 2); C1 = next(c for c in c2 if 1 in c)
usable_near = [x for c in c2 if c is not C1 for x in c]
check(3 in usable_near and A[3] == 4, "x=3 is a usable side-neighbour of u0 with a(x)=4")
c8 = comps(H, 8); C0 = next(c for c in c8 if 0 in c)
usable_far = [y for c in c8 if c is not C0 for y in c]
check(usable_far == [9], "usable-far set is exactly {9}")
check(all(3 in H[y] for y in usable_far), "Case-2-forced: every usable far y is adjacent to x")
lp = longest_induced_path(H)
check(lp[0] == 6, "path(H) = 6 exactly < 7 = d+4   witness %r" % (lp[1],))
sa = sum(A.values())
print("  NOTE (owner scope guard): Sigma a = %d, n = %d, l(H) = %s = %.2f  -> l < 3, so H lies"
      % (sa, n, "%d/%d" % (sa, n), sa/n))
print("       OUTSIDE pocket 1's live class (l > 3): it kills the local d=3 route, not (RP-D).")

print()
print("=== (B) does H also touch G36 (d=4) or G37 (d=3 Case 1)?  judge says no ===")
maxd = max(max(r) for r in dH)
check(maxd == 3, "diam(H) = %d, so H carries NO geodesic of length >= 4 -> G36 untouched" % maxd)
# NOTE: the owner's first pass omitted the `u1 ~ u2` edge test and therefore admitted
# non-paths as "frames", producing a spurious Case-1 hit.  The geodesic must be a PATH.
frames, case1 = [], []
for u0 in range(n):
    if A[u0] < 3: continue
    for u3 in range(n):
        if dH[u0][u3] != 3 or A[u3] < 2: continue
        cs = comps(H, u0); cy = comps(H, u3)
        for u1 in H[u0]:
            if dH[u1][u3] != 2: continue
            for u2 in H[u3]:
                if dH[u0][u2] != 2 or u2 not in H[u1]: continue      # <-- the edge test
                C = next(c for c in cs if u1 in c)
                xs = [x for c in cs if c is not C for x in c if A[x] >= 4]
                Cf = next(c for c in cy if u2 in c)
                ys = [y for c in cy if c is not Cf for y in c]
                for x in xs:
                    frames.append((u0, u1, u2, u3, x, tuple(ys)))
                    if any(y not in H[x] for y in ys): case1.append((u0, u1, u2, u3, x))
print("  qualifying frames in H:", frames)
check(len(frames) > 0, "H carries qualifying frames at all (the test is not vacuous)")
check(not case1, "H carries NO Case-1 frame (all %d qualifying frames are Case-2-forced)"
      " -> G37 untouched" % len(frames))

print()
print("=== (C) defect B10: peeling slack arithmetic on CE-1, leaf vs triangle-leaf ===")
ECE = [(0,9),(0,5),(1,5),(2,3),(2,5),(2,6),(2,8),(4,9),(4,6),(5,7),(5,8)]
CE = build(ECE, 10)
A0 = {v: a_val(CE, v) for v in range(10)}; S0 = sum(A0.values()); n0 = 10
print("  CE-1: a =", A0, " Sigma a =", S0, " slack Sigma a - 3n =", S0 - 3*n0)
for v, kind, expect in ((1, "leaf", 1), (8, "triangle-leaf", 2)):
    keep = [u for u in range(10) if u != v]; idx = {u: i for i, u in enumerate(keep)}
    g2 = build([(idx[x], idx[y]) for x, y in ECE if v not in (x, y)], 9)
    S2 = sum(a_val(g2, u) for u in range(9))
    rise = (S2 - 3*9) - (S0 - 3*n0)
    check(rise == expect, "deleting %d (%s): slack rises by %+d (project text says exactly +1)"
          % (v, kind, rise))
print("  => the '+1 exactly' phrasing is FALSE for triangle-leaves (+2); '>= +1' is what every")
print("     downstream use needs, so no conclusion moves.  B10 CONFIRMED.")

print()
print("FAILURES:", FAIL)
raise SystemExit(0 if FAIL == 0 else 1)
