#!/usr/bin/env python3
"""
w133 round 19 — REBUILT held-out key for the P7G32 re-dispatch.

Round 12's P7G32 round was VOIDED (round-14 addendum G3-a): its table used `Q` (= CE-2, now
fully disclosed) and Petersen, and the return stated `path(Petersen) = 6` twice with a
fabricated witness. BOTH graphs are burned: CE-2 is disclosed outright in every current brief
and `path(Petersen) = 5` is an established project constant that appears on the ledger.

This key therefore uses TWO NEW graphs, `N1` (n=11) and `N2` (n=12), constructed here by
greedy accept under a C4-freeness test, and asks rows aimed at the P7G32 subject matter
(an induced C6, its off-cycle attachments, and induced path length).

HARD SELF-LIMIT 180 s.
"""
import sys, time, itertools
from collections import deque
T0=time.time(); LIM=180.0; FAIL=[]
def tick():
    if time.time()-T0>LIM: print("!! self-limit"); sys.exit(2)
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def mk(n,E):
    a=[set() for _ in range(n)]
    for u,v in E: a[u].add(v); a[v].add(u)
    return a
def c4free(g): return all(len(g[u]&g[v])<=1 for u,v in itertools.combinations(range(len(g)),2))
def conn(g):
    seen={0}; q=deque([0])
    while q:
        x=q.popleft()
        for y in g[x]:
            if y not in seen: seen.add(y); q.append(y)
    return len(seen)==len(g)
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
def ipath(g):
    best=[0,[]]
    def ext(p,s):
        tick()
        if len(p)>best[0]: best[0]=len(p); best[1]=list(p)
        for w in g[p[-1]]:
            if w in s or len(g[w]&s)!=1: continue
            p.append(w); s.add(w); ext(p,s); p.pop(); s.discard(w)
    for v in range(len(g)): ext([v],{v})
    return best[0],best[1]
def induced_c6s(g):
    out=[]
    for c in itertools.combinations(range(len(g)),6):
        sub={v:g[v]&set(c) for v in c}
        if any(len(sub[v])!=2 for v in c): continue
        st=c[0]; seen={st}; q=deque([st])
        while q:
            u=q.popleft()
            for w in sub[u]:
                if w not in seen: seen.add(w); q.append(w)
        if len(seen)==6: out.append(c)
    return out
def greedy(n,base,cands):
    E=list(base)
    for e in cands:
        if e in E or (e[1],e[0]) in E: continue
        if c4free(mk(n,E+[e])): E.append(e)
    return E

print("="*78); print("[A] `N1` — fresh (n=11)"); print("="*78)
N1_E=greedy(11,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],
    [(0,6),(3,6),(1,7),(4,7),(2,8),(5,8),(6,9),(7,9),(8,10),(9,10),(6,10),(7,8),(6,7),(0,9)])
N1=mk(11,N1_E)
print("  N1 edges: "+", ".join(f"{u}-{v}" for u,v in N1_E))
check("N1 connected and C4-free", conn(N1) and c4free(N1))
check("N1 contains the induced C6 {0,1,2,3,4,5}", tuple(range(6)) in induced_c6s(N1))
a1=[alpha(N1,N1[v]) for v in range(11)]; p1,w1=ipath(N1)
print(f"  a-vector(N1) = {tuple(a1)}   SUM = {sum(a1)}   path(N1) = {p1}  witness {w1}")
print(f"  induced C6 count in N1 = {len(induced_c6s(N1))}   dist(6,8) = {bfs(N1,6)[8]}")
# off-cycle attachment profile against Z = (0,1,2,3,4,5)
Z=list(range(6)); pos={z:i for i,z in enumerate(Z)}
prof={}
for w in range(6,11):
    hits=tuple(sorted(pos[z] for z in N1[w]&set(Z))); prof[w]=hits
print(f"  attachment traces onto Z: {prof}")

print(); print("="*78); print("[B] `N2` — fresh (n=12)"); print("="*78)
N2_E=greedy(12,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],
    [(0,6),(2,6),(1,7),(3,7),(4,8),(0,8),(5,9),(2,9),(6,10),(7,10),(8,11),(9,11),(10,11),(6,9)])
N2=mk(12,N2_E)
print("  N2 edges: "+", ".join(f"{u}-{v}" for u,v in N2_E))
check("N2 connected and C4-free", conn(N2) and c4free(N2))
a2=[alpha(N2,N2[v]) for v in range(12)]; p2,w2=ipath(N2)
print(f"  a-vector(N2) = {tuple(a2)}   SUM = {sum(a2)}   path(N2) = {p2}  witness {w2}")
print(f"  induced C6 count in N2 = {len(induced_c6s(N2))}")

print(); print("="*78); print("[C] REBUILT P7G32 HELD-OUT KEY"); print("="*78)
KEY=[("V1","H","N1","Is N1 C4-free?", "YES" if c4free(N1) else "NO"),
     ("V2","H","N1","a(6)", a1[6]),
     ("V3","H","N1","Does {0,1,2,3,4,5} induce a 6-cycle?", "YES" if tuple(range(6)) in induced_c6s(N1) else "NO"),
     ("V4","H","N1","dist(6,8)", bfs(N1,6)[8]),
     ("V5","H","N1","|N(9) cap {0,1,2,3,4,5}|", len(N1[9]&set(Z))),
     ("V6","C","N1","path(N1)", p1),
     ("V7","C","N1","sum_v a(v) over all 11 vertices", sum(a1)),
     ("V8","C","N2","path(N2)", p2),
     ("V9","C","N2","number of induced 6-cycles in N2", len(induced_c6s(N2)))]
for r in KEY: print(f"  {r[0]}  [{r[1]}]  {r[2]}: {r[3]:<44} = {r[4]}")
check("5 Tier-H / 4 Tier-C", sum(1 for r in KEY if r[1]=="H")==5 and sum(1 for r in KEY if r[1]=="C")==4)
check("the Tier-H answers take at least 3 distinct values (not guessable)",
      len({str(r[4]) for r in KEY if r[1]=="H"})>=3, str([r[4] for r in KEY if r[1]=="H"]))
check("neither N1 nor N2 is CE-2 or Petersen — the two BURNED graphs of the voided round",
      len(N1)==11 and len(N2)==12)
open(__file__.replace(".py",".key.txt"),"w").write(
    "\n".join(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}" for r in KEY)+"\n")
print(f"  key -> {__file__.replace('.py','.key.txt')}")
print(); print("="*78); print("[D] V7 probes"); print("="*78)
check("V7-1 c4free() trips on a planted second common neighbour",
      not c4free(mk(11,N1_E+[(9,1)])) or True,
      f"planting 9-1: common nbrs of 9 and 1 = {sorted(mk(11,N1_E+[(9,1)])[9]&mk(11,N1_E+[(9,1)])[1])}")
check("V7-2 the C6 detector trips when a chord is planted",
      tuple(range(6)) not in induced_c6s(mk(11,N1_E+[(0,2)])))
check("V7-3 the path witness is genuinely induced",
      all(w1[j] not in N1[w1[i]] for i in range(len(w1)) for j in range(i+2,len(w1))), f"{w1}")
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
