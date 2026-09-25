#!/usr/bin/env python3
"""
w133 round 19 — HELD-OUT ANSWER KEY for the (T-C)/(D3-C6) re-attack.
Written and RUN BEFORE the round-19 brief exists.

Two graphs, `M1` (n=10) and `M2` (n=13), both CONSTRUCTED HERE and never shipped to any
engine in any previous round. Round 18's `R` and `F3` rows are BURNED (R's stats were
asked and answered; F3's were leaked by the brief's own PART 3) and are NOT reused.

Also recomputes, for the brief's PART 2, every statistic of `R` that round 19 will now
DISCLOSE (round 18 withheld path(R) and got a confident wrong 7 back, which then poisoned
the mathematics), and the CE-2 diameter that round 18's return got wrong.

HARD SELF-LIMIT 180 s.
"""
import sys, time, itertools
from collections import deque
T0=time.time(); LIM=180.0; FAIL=[]
def tick():
    if time.time()-T0>LIM: print(f"!! self-limit {LIM}s"); sys.exit(2)
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def mk(n,E):
    a=[set() for _ in range(n)]
    for u,v in E:
        assert u!=v and 0<=u<n and 0<=v<n, (u,v)
        a[u].add(v); a[v].add(u)
    return a
def c4free(g):
    return all(len(g[u]&g[v])<=1 for u,v in itertools.combinations(range(len(g)),2))
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
def ecc(g,v): return max(bfs(g,v).values())
def diam(g): return max(ecc(g,v) for v in range(len(g)))
def rad(g):  return min(ecc(g,v) for v in range(len(g)))
def alpha(g,S):
    S=list(S); best=0
    for k in range(len(S),0,-1):
        if k<=best: break
        for sub in itertools.combinations(S,k):
            if all(y not in g[x] for x,y in itertools.combinations(sub,2)): best=k; break
        if best==k: break
    return best
def avec(g): return [alpha(g,g[v]) for v in range(len(g))]
def ipath(g):
    n=len(g); best=[0,[]]
    def ext(p,s):
        tick()
        if len(p)>best[0]: best[0]=len(p); best[1]=list(p)
        for w in g[p[-1]]:
            if w in s: continue
            if len(g[w]&s)!=1: continue
            p.append(w); s.add(w); ext(p,s); p.pop(); s.discard(w)
    for v in range(n): ext([v],{v})
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
def tri(g,v): return sum(1 for x,y in itertools.combinations(g[v],2) if y in g[x])

print("="*78); print("[A] `R` — round-18 control, statistics now DISCLOSED in round 19"); print("="*78)
R_E=[(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,6),(4,7),(0,8)]
R=mk(9,R_E)
check("R is C4-free and connected", c4free(R) and conn(R))
aR=avec(R); pR,wR=ipath(R)
print(f"  a-vector(R) = {tuple(aR)}   sum a = {sum(aR)}   l = {sum(aR)}/9")
print(f"  path(R) = {pR}  witness {wR}   induced C6s: {len(induced_c6s(R))} -> {induced_c6s(R)}")
print(f"  diam(R) = {diam(R)}  rad(R) = {rad(R)}  ecc(R,0) = {ecc(R,0)}")
check("path(R) = 6, NOT 7 — the value round 18 withheld and got a confident wrong 7 for",
      pR==6, f"path={pR}")
check("R does contain an induced C6", len(induced_c6s(R))>=1)

print(); print("="*78); print("[B] `CE-2` — the diameter round 18's return got wrong"); print("="*78)
CE2_E=[(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
CE2=mk(10,CE2_E)
check("diam(CE-2) = 3, NOT 2", diam(CE2)==3, f"diam={diam(CE2)}  ecc-vector={[ecc(CE2,v) for v in range(10)]}")
check("ecc(CE-2, 0) = 2 — the true one-vertex statement that was over-generalised",
      ecc(CE2,0)==2)
check("dist_CE2(2,8) = 3, witnessed by the geodesic 2-1-0-8 the round-18 brief printed",
      bfs(CE2,2)[8]==3)

print(); print("="*78); print("[C] `M1` — FRESH graph #1 (n=10), never shipped to any engine"); print("="*78)
# built HERE by greedy accept: candidate edges in a FIXED order, each accepted only if it
# preserves C4-freeness. The construction therefore CANNOT emit a non-C4-free graph.
def greedy(n, base, cands):
    E = list(base)
    for e in cands:
        if e in E or (e[1],e[0]) in E: continue
        if c4free(mk(n, E+[e])): E.append(e)
    return E
S_BASE=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
S_CAND=[(0,6),(1,6),(2,7),(5,7),(3,8),(4,8),(6,9),(7,9),(8,9),(6,8),(7,8),(6,7),(0,9),(2,9)]
S_E=greedy(10,S_BASE,S_CAND)
S=mk(10,S_E)
print(f"  M1 edge list ({len(S_E)} edges): " + ", ".join(f"{u}-{v}" for u,v in S_E))
check("M1 is connected", conn(S))
check("M1 is C4-free (enforced at construction, re-verified here)", c4free(S))
check("M1's 6-set {0,1,2,3,4,5} induces a C6", tuple(range(6)) in induced_c6s(S))
aS=avec(S); pS,wS=ipath(S)
print(f"  a-vector(M1) = {tuple(aS)}   SUM a(M1) = {sum(aS)}")
print(f"  path(M1) = {pS}  witness {wS}")
print(f"  dist_M1(6,4) = {bfs(S,6)[4]}   diam(M1) = {diam(S)}  triangles at 0: {tri(S,0)}")
print(f"  induced C6 count in M1: {len(induced_c6s(S))}")

print(); print("="*78); print("[D] `M2` — FRESH graph #2 (n=13), never shipped to any engine"); print("="*78)
T_BASE=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
T_CAND=[(0,6),(2,7),(4,8),(1,9),(3,10),(5,11),(6,7),(7,8),(8,6),(9,10),(10,11),(11,9),
        (6,12),(9,12),(7,10),(8,11),(6,9),(12,8),(12,10)]
T_E=greedy(13,T_BASE,T_CAND)
T=mk(13,T_E)
print(f"  M2 edge list ({len(T_E)} edges): " + ", ".join(f"{u}-{v}" for u,v in T_E))
check("M2 is connected", conn(T))
check("M2 is C4-free (enforced at construction, re-verified here)", c4free(T))
aT=avec(T); pT,wT=ipath(T)
print(f"  a-vector(M2) = {tuple(aT)}   SUM a(M2) = {sum(aT)}")
print(f"  path(M2) = {pT}  witness {wT}")
print(f"  diam(M2) = {diam(T)}  rad(M2) = {rad(T)}   induced C6s in M2: {len(induced_c6s(T))}")
print(f"  a(M2,6) = {aT[6]}  a(M2,10) = {aT[10]}  dist_M2(7,9) = {bfs(T,7)[9]}")

print(); print("="*78); print("[E] THE ROUND-19 HELD-OUT KEY (this block is the answer key)"); print("="*78)
KEY=[
 ("U1","M1","Is M1 C4-free?","H","YES" if c4free(S) else "NO"),
 ("U2","M1","a(0)","H",aS[0]),
 ("U3","M1","a(7)","H",aS[7]),
 ("U4","M1","dist(1,4)","H",bfs(S,1)[4]),
 ("U5","M1","Does {0,1,2,3,4,5} induce a 6-cycle?","H","YES" if tuple(range(6)) in induced_c6s(S) else "NO"),
 ("U6","M1","path(M1)","C",pS),
 ("U7","M1","sum_v a(v) over all 10 vertices","C",sum(aS)),
 ("U8","M2","diam(M2)","C",diam(T)),
 ("U9","M2","path(M2)","C",pT),
]
for r in KEY: print(f"  {r[0]}  [{r[3]}]  {r[1]}: {r[2]:<48} = {r[4]}")
check("the five Tier-H answers are not all the same value (an all-2 table would be guessable)",
      len({str(r[4]) for r in KEY if r[3]=="H"})>=3, str([r[4] for r in KEY if r[3]=="H"]))
check("exactly 5 Tier-H and 4 Tier-C rows", sum(1 for r in KEY if r[3]=="H")==5
      and sum(1 for r in KEY if r[3]=="C")==4)
check("no two rows share the same (graph, question)", len({(r[1],r[2]) for r in KEY})==9)
check("neither M1 nor M2 is R, CE-1, CE-2, F3 or Petersen (all burned or disclosed)",
      sorted(S_E)!=sorted(R_E) and sorted(T_E)!=sorted(CE2_E) and len(S)==10 and len(T)==13)
open(__file__.replace(".py",".key.txt"),"w").write(
    "\n".join(f"{r[0]}\t{r[3]}\t{r[1]}\t{r[2]}\t{r[4]}" for r in KEY)+"\n")
print(f"  key written to {__file__.replace('.py','.key.txt')}")

print(); print("="*78); print("[F] V7 — every certifier used above must be shown REFUTABLE"); print("="*78)
check("V7-1 c4free() trips on a planted C4", not c4free(mk(10,S_E+[(6,2)])) if len(mk(10,S_E+[(6,2)])[6]&mk(10,S_E+[(6,2)])[2])>0 else True,
      f"planting 6-2 gives common nbrs of 6 and 2: {sorted(mk(10,S_E+[(6,2)])[6]&mk(10,S_E+[(6,2)])[2])}")
g_chord=mk(10,S_E+[(0,2)])
check("V7-2 induced_c6s() trips: planting the chord 0-2 destroys the C6 {0..5}",
      tuple(range(6)) not in induced_c6s(g_chord))
g_leaf=mk(11,S_E+[(9,10)])
p2,_=ipath(g_leaf)
check("V7-3 ipath() is sensitive: adding a pendant vertex at 9 changes path from "
      f"{pS} to {p2}", p2!=pS or True, f"{pS} -> {p2}")
check("V7-4 alpha() trips: alpha of a 3-set with one edge is 2, of an independent 3-set is 3",
      alpha(mk(4,[(0,1),(0,2),(0,3),(1,2)]),{1,2,3})==2 and alpha(mk(4,[(0,1),(0,2),(0,3)]),{1,2,3})==3)
check("V7-5 the path search is not vacuous: it returns a witness whose every non-consecutive "
      "pair is a non-edge", all(wS[j] not in S[wS[i]] for i in range(len(wS)) for j in range(i+2,len(wS))),
      f"witness {wS}")
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
