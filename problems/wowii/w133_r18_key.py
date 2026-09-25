#!/usr/bin/env python3
"""
w133 round 18 — KEY for the PART 6 held-out table of brief
`automath-sandbox/briefs/w133_r18_D3C6.md`.

Built BEFORE the brief was written and BEFORE dispatch, so that every number the
brief withholds exists on disk as a computed value, never as a remembered one.

Graphs, each rebuilt from an edge list stated in this file:
  R    = the 9-vertex equality instance of Theorem G50 (draft 28.3 S3)
  F3   = CE-2 with 3 pendant triangles at vertex 2 (the G49 family at k = 3)
  CE1, CE2 = the two certified controls, re-verified so the brief's PART 2 numbers
             are also computed here rather than copied.

HARD SELF-LIMIT: 240 s wall, enforced inside; exit(2) on overrun.
No SAT, no exhaustive enumeration of a large space: the biggest search is an induced-path
DFS over a 16-vertex graph with a depth cap.
"""
import sys, time, itertools
from fractions import Fraction
from collections import deque

T0 = time.time()
BUDGET = 240.0
def tick(where):
    if time.time() - T0 > BUDGET:
        print(f"HARD TIMEOUT at {where}"); sys.exit(2)

FAIL = []
def check(name, cond, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + name + (f"   [{detail}]" if detail else ""))
    if not cond: FAIL.append(name)

# ------------------------------------------------------------------ graph core
def mk(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v and 0 <= u < n and 0 <= v < n, (u, v)
        adj[u].add(v); adj[v].add(u)
    return adj

def c4free(adj):
    """strong form: no two distinct vertices with >= 2 common neighbours"""
    n = len(adj); bad = 0
    for u in range(n):
        for v in range(u+1, n):
            if len(adj[u] & adj[v]) >= 2: bad += 1
    return bad == 0, bad

def connected(adj):
    n = len(adj); seen = {0}; q = deque([0])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in seen: seen.add(w); q.append(w)
    return len(seen) == n

def alpha_nbhd(adj, v):
    """a(v) = independence number of G[N(v)].  In a C4-free graph G[N(v)] is a matching,
    but this routine does NOT assume that: it computes alpha by direct maximisation over
    the (small) neighbourhood, so it stays correct even if C4-freeness fails."""
    S = sorted(adj[v]); k = len(S)
    best = 0
    for r in range(k, -1, -1):
        if r <= best: break
        for comb in itertools.combinations(S, r):
            ok = True
            for i in range(r):
                for j in range(i+1, r):
                    if comb[j] in adj[comb[i]]: ok = False; break
                if not ok: break
            if ok: best = max(best, r); break
    return best

def avec(adj): return [alpha_nbhd(adj, v) for v in range(len(adj))]

def bfs(adj, s):
    n = len(adj); d = [-1]*n; d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if d[w] < 0: d[w] = d[u]+1; q.append(w)
    return d

def longest_induced_path(adj, cap=None):
    """exhaustive DFS over induced paths, returns max number of VERTICES and a witness.
    Exhaustive over the graph, which is why this is only run on n <= 16."""
    n = len(adj)
    best = [0, []]
    def ext(path, pathset):
        if len(path) > best[0]:
            best[0] = len(path); best[1] = list(path)
        if cap is not None and len(path) >= cap: return
        last = path[-1]
        for w in adj[last]:
            if w in pathset: continue
            # induced: w may touch only `last` among the path
            if len(adj[w] & pathset) != 1: continue
            path.append(w); pathset.add(w)
            ext(path, pathset)
            path.pop(); pathset.discard(w)
    for s in range(n):
        tick(f"induced-path DFS from {s}")
        ext([s], {s})
    return best[0], best[1]

def has_induced_c6(adj):
    n = len(adj)
    for comb in itertools.combinations(range(n), 6):
        sub = {v: adj[v] & set(comb) for v in comb}
        if any(len(sub[v]) != 2 for v in comb): continue
        # 2-regular on 6 vertices and connected  <=>  a 6-cycle
        start = comb[0]; seen = {start}; q = deque([start])
        while q:
            u = q.popleft()
            for w in sub[u]:
                if w not in seen: seen.add(w); q.append(w)
        if len(seen) == 6: return True, comb
    return False, None

def components_of_nbhd(adj, v):
    S = set(adj[v]); comps = []; seen = set()
    for u in sorted(S):
        if u in seen: continue
        comp = {u}; q = deque([u]); seen.add(u)
        while q:
            a = q.popleft()
            for w in adj[a] & S:
                if w not in seen: seen.add(w); comp.add(w); q.append(w)
        comps.append(comp)
    return comps

def frame_report(adj, u0, u1, u2, u3, x):
    """returns (is_geodesic, x_usable, usable_far_set, case2_forced)"""
    d0 = bfs(adj, u0); d3 = bfs(adj, u3)
    geo = (d0[u3] == 3 and u1 in adj[u0] and u2 in adj[u1] and u3 in adj[u2]
           and d0[u1] == 1 and d0[u2] == 2)
    comps0 = components_of_nbhd(adj, u0)
    c_of_u1 = next(c for c in comps0 if u1 in c)
    x_usable = (x in adj[u0]) and (x not in c_of_u1)
    comps3 = components_of_nbhd(adj, u3)
    c_of_u2 = next(c for c in comps3 if u2 in c)
    far = sorted({y for c in comps3 if c is not c_of_u2 for y in c})
    forced = len(far) > 0 and all(y in adj[x] for y in far)
    return geo, x_usable, far, forced

# ------------------------------------------------------------------ the graphs
R_EDGES = [(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,6),(4,7),(0,8)]
R = mk(9, R_EDGES)

CE1 = mk(10, [(0,9),(0,5),(1,5),(2,3),(2,5),(2,6),(2,8),(4,9),(4,6),(5,7),(5,8)])
CE2_EDGES = [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
CE2 = mk(10, CE2_EDGES)

# F3 = CE-2 + 3 pendant triangles at vertex 2  (G49 family, k = 3)
f3_edges = list(CE2_EDGES); nxt = 10
for _ in range(3):
    p, q = nxt, nxt+1; nxt += 2
    f3_edges += [(2,p),(2,q),(p,q)]
F3 = mk(nxt, f3_edges)

print("="*78); print("[A] the two certified controls re-verified from their edge lists"); print("="*78)
for nm, g, exp_n, exp_sum in (("CE-1", CE1, 10, 19), ("CE-2", CE2, 10, 25)):
    ok, bad = c4free(g)
    check(f"{nm} C4-free", ok, f"{bad} violating pairs")
    check(f"{nm} connected", connected(g))
    av = avec(g)
    check(f"{nm} n = {exp_n}", len(g) == exp_n, f"got {len(g)}")
    check(f"{nm} Sum a = {exp_sum}", sum(av) == exp_sum, f"got {sum(av)}, a = {av}")
    p, w = longest_induced_path(g)
    check(f"{nm} path = 6", p == 6, f"got {p}, witness {w}")
geo, xu, far, forced = frame_report(CE1, 2, 6, 4, 9, 5)
check("CE-1 frame (2,6,4,9;x=5) Case-2-forced", geo and xu and forced, f"far set {far}")
geo, xu, far, forced = frame_report(CE2, 2, 1, 0, 8, 3)
check("CE-2 frame (2,1,0,8;x=3) Case-2-forced", geo and xu and forced, f"far set {far}")

print(); print("="*78); print("[B] KEY — graph R (Theorem G50, 9 vertices)"); print("="*78)
tick("R")
okR, badR = c4free(R)
check("R C4-free", okR, f"{badR} violating pairs")
check("R connected", connected(R))
aR = avec(R)
dR = bfs(R, 0)
geoR, xuR, farR, forcedR = frame_report(R, 0, 1, 2, 3, 4)
geo, xu, far, forced = geoR, xuR, farR, forcedR
pR, wR = longest_induced_path(R)
c6R, c6witR = has_induced_c6(R)
print(f"  a-vector(R) = {aR}   Sum a = {sum(aR)}   n = {len(R)}")
print(f"  dist_R(0,3) = {dR[3]}   geodesic 0-1-2-3 = {geo}")
print(f"  x = 4 usable side-neighbour of 0 = {xu}   usable far set at u3=3 : {far}   Case-2-forced = {forced}")
print(f"  path(R) = {pR}   witness {wR}")
print(f"  induced C6 in R = {c6R}   witness {c6witR}")
check("R matches G50's recorded a-profile [3,2,2,2,4,2,1,1,1]", aR == [3,2,2,2,4,2,1,1,1], f"got {aR}")
check("R Sum a = 18, l = 2", sum(aR) == 18 and sum(aR) == 2*len(R), f"Sum a = {sum(aR)}")
check("R path = 6 (NOT 7 — the D3_C report's error)", pR == 6, f"got {pR}")
check("R has an induced C6 (G46 predicts one)", c6R, f"{c6witR}")

print(); print("="*78); print("[C] KEY — graph F3 = CE-2 + 3 pendant triangles at vertex 2 (G49 at k=3)"); print("="*78)
tick("F3")
okF, badF = c4free(F3)
check("F3 C4-free", okF, f"{badF} violating pairs")
check("F3 connected", connected(F3))
aF = avec(F3)
pF, wF = longest_induced_path(F3)
print(f"  n(F3) = {len(F3)}   a-vector = {aF}   Sum a = {sum(aF)}   l = {sum(aF)}/{len(F3)}")
print(f"  path(F3) = {pF}   witness {wF}")
check("F3 n = 16 = 10 + 2*3", len(F3) == 16, f"got {len(F3)}")
check("F3 Sum a = 34 = 25 + 3*3 (G49 identity)", sum(aF) == 34, f"got {sum(aF)}")
check("F3 l - 3/2 = 10/16 (G49 identity)",
      Fraction(sum(aF), len(F3)) - Fraction(3,2) == Fraction(10, 10+2*3),
      f"l = {sum(aF)}/{len(F3)} = {Fraction(sum(aF),len(F3))}, l-3/2 = {Fraction(sum(aF),len(F3))-Fraction(3,2)}")
check("F3 path = 6 (path >= 6 TRUE and path >= 7 FALSE, checked as two facts)",
      pF >= 6 and not (pF >= 7), f"got {pF}")
geo, xu, far, forced = frame_report(F3, 2, 1, 0, 8, 3)
check("F3 keeps CE-2's frame (2,1,0,8;x=3) Case-2-forced", geo and xu and forced, f"far {far}")

print(); print("="*78); print("[D] the PART 6 held-out key, as it will be graded"); print("="*78)
KEY = [
    ("T1", "H", "R is C4-free?",                       "YES" if okR else "NO"),
    ("T2", "H", "a_R(0)",                              str(aR[0])),
    ("T3", "H", "a_R(4)",                              str(aR[4])),
    ("T4", "H", "dist_R(0,3)",                         str(dR[3])),
    ("T5", "H", "frame (0,1,2,3), x=4 Case-2-forced?", "YES" if forcedR else "NO"),
    ("T6", "C", "path(R)",                             str(pR)),
    ("T7", "C", "R contains an induced C6?",           "YES" if c6R else "NO"),
    ("T8", "C", "Sum_v a(v) over F3",                  str(sum(aF))),
    ("T9", "C", "path(F3)",                            str(pF)),
]
for rid, tier, q, ans in KEY:
    print(f"  {rid}  tier {tier}   {q:<44s} = {ans}")

print()
print(f"FAILURES: {len(FAIL)}" + ("" if not FAIL else "  -> " + "; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
