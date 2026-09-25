#!/usr/bin/env python3
"""
w133 round 19 — SELF-CHECK OF THE OWNER'S OWN BRIEF.
Round 18's return died on a stated fact that was false; gate clause B6 makes that expensive.
The same standard applies to ME: every factual assertion the round-19 brief makes about a
control graph is re-derived here from the printed edge list.
"""
import sys, itertools
from collections import deque
FAIL=[]
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def mk(n,E):
    a=[set() for _ in range(n)]
    for u,v in E: a[u].add(v); a[v].add(u)
    return a
def bfs(g,s):
    d={s:0}; q=deque([s])
    while q:
        x=q.popleft()
        for y in g[x]:
            if y not in d: d[y]=d[x]+1; q.append(y)
    return d
def alpha(g,S):
    S=list(S); best=0
    for k in range(len(S),0,-1):
        if k<=best: break
        for sub in itertools.combinations(S,k):
            if all(y not in g[x] for x,y in itertools.combinations(sub,2)): best=k; break
        if best==k: break
    return best
def comps(g,S):
    S=set(S); out=[]; seen=set()
    for v in S:
        if v in seen: continue
        c={v}; q=[v]; seen.add(v)
        while q:
            x=q.pop()
            for y in g[x]&S:
                if y not in seen: seen.add(y); c.add(y); q.append(y)
        out.append(c)
    return out
def frame(g,u,x):
    """u = geodesic (u0..u3); returns (is_geodesic, x usable, a-conditions, far set, case2forced)"""
    d={i:bfs(g,u[i]) for i in range(4)}
    geo=all(d[i][u[j]]==abs(i-j) for i in range(4) for j in range(4))
    cN0=comps(g,g[u[0]]); comp_of=lambda v,C:[c for c in C if v in c][0]
    usable = x in g[u[0]] and comp_of(x,cN0)!=comp_of(u[1],cN0)
    cN3=comps(g,g[u[3]]); far=[y for y in g[u[3]] if comp_of(y,cN3)!=comp_of(u[2],cN3)]
    forced = bool(far) and all(y in g[x] for y in far)
    return geo, usable, far, forced

print("="*78); print("Every claim the round-19 brief makes about `R`, re-derived"); print("="*78)
R=mk(9,[(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,7),(4,6),(0,8)])
a=[alpha(R,R[v]) for v in range(9)]
check("brief: a-vector(R) = (3,2,2,2,4,2,1,1,1)", tuple(a)==(3,2,2,2,4,2,1,1,1), str(tuple(a)))
check("brief: sum a = 18 and l(R) = 2", sum(a)==18 and sum(a)==2*9, f"sum={sum(a)}")
check("brief: mu(R) = 1", min(a)==1)
ecc={v:max(bfs(R,v).values()) for v in range(9)}
check("brief: diam(R) = 4", max(ecc.values())==4, str(ecc))
check("brief: rad(R) = 3", min(ecc.values())==3)
check("brief: ecc(R,0) = 3", ecc[0]==3)
geo,usable,far,forced=frame(R,[0,1,2,3],4)
check("brief: 0-1-2-3 IS a geodesic of R", geo)
check("brief: x = 4 is a USABLE side-neighbour of u0 = 0", usable)
check("brief: a(0) >= 3, a(3) >= 2, a(4) >= 4 (the 3-frame's a-conditions)",
      a[0]>=3 and a[3]>=2 and a[4]>=4, f"a(0)={a[0]} a(3)={a[3]} a(4)={a[4]}")
check("brief: the frame IS Case-2-forced (every usable far-side y is adjacent to x=4)",
      forced, f"usable far-side set = {sorted(far)}")
P=[1,2,3,5,4,6]
check("brief: 1-2-3-5-4-6 IS an induced path on 6 vertices (the disclosed path(R) witness)",
      all(P[i+1] in R[P[i]] for i in range(5)) and
      all(P[j] not in R[P[i]] for i in range(6) for j in range(i+2,6)))
C=[0,1,2,3,5,4]
check("brief: (0,1,2,3,4,5) induces a 6-cycle in R",
      all(C[(i+1)%6] in R[C[i]] for i in range(6)) and
      all(C[(i+j)%6] not in R[C[i]] for i in range(6) for j in (2,3)))

print(); print("="*78); print("Every claim the round-19 brief makes about `CE-2`"); print("="*78)
CE2=mk(10,[(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)])
e2={v:max(bfs(CE2,v).values()) for v in range(10)}
check("brief: ecc-vector(CE-2) = (2,3,3,2,2,3,3,3,3,3)",
      tuple(e2[v] for v in range(10))==(2,3,3,2,2,3,3,3,3,3), str(tuple(e2[v] for v in range(10))))
check("brief: diam(CE-2) = 3, NOT 2", max(e2.values())==3)
check("brief: dist(2,8) = 3 along 2-1-0-8", bfs(CE2,2)[8]==3 and
      all(y in CE2[x] for x,y in zip([2,1,0],[1,0,8])))
g2,u2,f2,fo2=frame(CE2,[2,1,0,8],3)
check("brief: CE-2's frame on 2-1-0-8 with x=3 is a Case-2-forced 3-frame with far set {9}",
      g2 and u2 and sorted(f2)==[9] and fo2, f"far={sorted(f2)} forced={fo2}")
a2=[alpha(CE2,CE2[v]) for v in range(10)]
check("brief: a-vector(CE-2) = (3,2,3,4,3,2,2,2,2,2), sum 25, l = 2.5",
      tuple(a2)==(3,2,3,4,3,2,2,2,2,2) and sum(a2)==25, str(tuple(a2)))

print(); print("="*78); print("Every claim the round-19 brief makes about `CE-1`"); print("="*78)
CE1=mk(10,[(0,9),(0,5),(1,5),(2,3),(2,5),(2,6),(2,8),(4,9),(4,6),(5,7),(5,8)])
a1=[alpha(CE1,CE1[v]) for v in range(10)]
check("brief: a-vector(CE-1) = (2,1,3,1,2,4,2,1,1,2), sum 19, l = 1.9",
      tuple(a1)==(2,1,3,1,2,4,2,1,1,2) and sum(a1)==19, str(tuple(a1)))
g1,u1,f1,fo1=frame(CE1,[2,6,4,9],5)
check("brief: CE-1's frame on 2-6-4-9 with x=5 is Case-2-forced with far set {0}",
      g1 and u1 and sorted(f1)==[0] and fo1, f"far={sorted(f1)} forced={fo1}")
check("brief: all three controls have l < 3 (the brief's stated escape route)",
      sum(a1)/10 < 3 and sum(a2)/10 < 3 and sum(a)/9 < 3,
      f"l = {sum(a1)/10}, {sum(a2)/10}, {sum(a)/9}")
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
sys.exit(1 if FAIL else 0)
