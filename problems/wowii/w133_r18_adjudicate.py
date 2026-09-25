#!/usr/bin/env python3
"""
w133 round 18 — ADJUDICATION of the ox-alpha return
`automath-sandbox/out/ox-alpha/w133_r18_D3C6_out.md` against the gate pre-registered
blind at `orchestration/results/w133_state.md` section "Round 18" 1.

Every claim checked here is checked from an edge list rebuilt in this file.
HARD SELF-LIMIT 120 s.
"""
import sys, time, itertools
from collections import deque
from fractions import Fraction
T0=time.time()
FAIL=[]
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def mk(n,E):
    a=[set() for _ in range(n)]
    for u,v in E: a[u].add(v); a[v].add(u)
    return a
def bfs(a,s):
    d={s:0}; q=deque([s])
    while q:
        x=q.popleft()
        for y in a[x]:
            if y not in d: d[y]=d[x]+1; q.append(y)
    return d
def alpha(a,S):
    S=list(S); best=0
    for k in range(len(S),0,-1):
        if k<=best: break
        for sub in itertools.combinations(S,k):
            if all(y not in a[x] for x,y in itertools.combinations(sub,2)): best=k; break
        if best==k: break
    return best

R_E=[(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,6),(4,7),(0,8)]
R=mk(9,R_E)
CE2_E=[(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
CE2=mk(10,CE2_E)
PET_E=[(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),(0,5),(1,6),(2,7),(3,8),(4,9)]
PET=mk(10,PET_E)

print("="*76); print("[1] T6 — the engine answered path(R) = 7 and exhibited 6-4-0-1-2-3-5"); print("="*76)
P=[6,4,0,1,2,3,5]
cons=all(P[i+1] in R[P[i]] for i in range(len(P)-1))
ch=[(P[i],P[j]) for i in range(len(P)) for j in range(i+2,len(P)) if P[j] in R[P[i]]]
check("the exhibited 7-sequence IS a path (consecutive vertices adjacent)", cons)
check("but it is NOT induced: it carries a chord", len(ch)>0, f"chords {ch}")
check("the chord is the edge 4-5, the FIFTH edge of R's printed edge list",
      ch==[(4,5)] and (4,5) in R_E, f"R's edge list position {R_E.index((4,5))+1}")
# exhaustive
best=[0,[]]
def ext(p,s):
    if len(p)>best[0]: best[0]=len(p); best[1]=list(p)
    for w in R[p[-1]]:
        if w in s or len(R[w]&s)!=1: continue
        p.append(w); s.add(w); ext(p,s); p.pop(); s.discard(w)
for v in range(9): ext([v],{v})
check("exhaustive induced-path search over R gives path(R) = 6, NOT 7", best[0]==6,
      f"path(R) = {best[0]}, witness {best[1]}")

print(); print("="*76); print("[2] the load-bearing factual claim of Angle 2: 'diam(CE-2) = 2'"); print("="*76)
ecc={v:max(bfs(CE2,v).values()) for v in range(10)}
check("diam(CE-2) = 3, NOT 2", max(ecc.values())==3, f"ecc = {ecc}, diam = {max(ecc.values())}")
check("dist_CE2(2,8) = 3 — the very geodesic 2-1-0-8 the brief printed",
      bfs(CE2,2)[8]==3, f"dist(2,8) = {bfs(CE2,2)[8]}")
check("ecc_CE2(0) = 2 — the true statement the engine generalised from",
      ecc[0]==2, f"ecc(0) = {ecc[0]}")

print(); print("="*76); print("[3] Byproduct 3 — the diam-2 counting identity, checked as MATHEMATICS"); print("="*76)
def stats(g):
    n=len(g); m=sum(len(g[v]) for v in range(n))//2
    T=sum(1 for t in itertools.combinations(range(n),3)
          if t[1] in g[t[0]] and t[2] in g[t[0]] and t[2] in g[t[1]])
    sa=sum(alpha(g,g[v]) for v in range(n))
    sc=sum(len(g[v])*(len(g[v])-1)//2 for v in range(n))
    return n,m,T,sa,sc
for nm,g,is_d2 in (("Petersen",PET,True),("CE-2",CE2,False)):
    n,m,T,sa,sc=stats(g)
    d2 = max(max(bfs(g,v).values()) for v in range(n))==2
    lhs = sc; rhs = n*(n-1)//2 - m + 3*T
    idn = (sa == m - sc + n*(n-1)//2)
    print(f"  {nm}: n={n} m={m} T={T} Sum a={sa} Sum C(d,2)={sc} diam2={d2}")
    check(f"{nm}: the path-count identity Sum C(d,2) = C(n,2)-m+3T holds iff diam = 2 "
          f"(here diam2={d2})", (lhs==rhs)==d2, f"{lhs} vs {rhs}")
    check(f"{nm}: the derived identity Sum a = m - Sum C(d,2) + C(n,2) holds iff diam = 2",
          idn==d2, f"Sum a = {sa}, formula gives {m-sc+n*(n-1)//2}")
n,m,T,sa,sc = stats(CE2)
check("the engine's arithmetic for Sum C(d,2) on CE-2 is WRONG (it wrote 26)", sc==29, f"true value {sc}")
check("CE-2 is therefore NOT a valid instance of Byproduct 3 (it fails the diam = 2 hypothesis)",
      max(max(bfs(CE2,v).values()) for v in range(10))!=2)
n,m,T,sa,sc = stats(PET)
check("Petersen IS a valid instance of Byproduct 3, and it was printed in the brief",
      sa == m - sc + n*(n-1)//2 and sa==30, f"Sum a = {sa} = {m} - {sc} + {n*(n-1)//2}")

print(); print("="*76); print("[4] Lemma 1 and Lemma 2 — the two survivors"); print("="*76)
# Lemma 1 on every induced C6 of every control graph
def induced_c6s(g):
    n=len(g); out=[]
    for c in itertools.combinations(range(n),6):
        sub={v:g[v]&set(c) for v in c}
        if any(len(sub[v])!=2 for v in c): continue
        st=c[0]; seen={st}; q=deque([st])
        while q:
            u=q.popleft()
            for w in sub[u]:
                if w not in seen: seen.add(w); q.append(w)
        if len(seen)==6:
            cyc=[c[0]]; prev=None
            while len(cyc)<6:
                nxt=[w for w in sub[cyc[-1]] if w!=prev][0]; prev=cyc[-1]; cyc.append(nxt)
            out.append(cyc)
    return out
viol1=[]; viol2=[]
for nm,g in (("R",R),("CE-2",CE2),("Petersen",PET)):
    for cyc in induced_c6s(g):
        Zs=set(cyc); pos={z:i for i,z in enumerate(cyc)}
        for w in range(len(g)):
            if w in Zs: continue
            hits=sorted(pos[z] for z in g[w]&Zs)
            if len(hits)>2: viol1.append((nm,w,hits))
            if len(hits)==2:
                dd=min((hits[1]-hits[0])%6,(hits[0]-hits[1])%6)
                if dd not in (1,3): viol1.append((nm,w,hits,dd))
        # Lemma 2
        av=[alpha(g,g[v]) for v in range(len(g))]
        Wp=set()
        lhs=0
        for z in cyc:
            Wz=g[z]-Zs; Wp|=Wz
            t=sum(1 for x,y in itertools.combinations(g[z],2) if y in g[x])
            if av[z]-2 != len(Wz)-t: viol2.append((nm,z,av[z],len(Wz),t))
            lhs+=av[z]-2
        if lhs > 2*len(Wp): viol2.append((nm,"bound",lhs,2*len(Wp)))
check("Lemma 1 holds on EVERY induced C6 of R, CE-2 and Petersen (non-empty scan)",
      not viol1 and len(induced_c6s(R))+len(induced_c6s(CE2))+len(induced_c6s(PET))>0,
      f"{len(induced_c6s(R))+len(induced_c6s(CE2))+len(induced_c6s(PET))} induced C6s scanned, "
      f"{len(viol1)} violations")
check("Lemma 2's identity a(z) = 2 + |W_z| - t(z) and the bound <= 2|W'| hold on the same scan",
      not viol2, f"{len(viol2)} violations")
# the brief's own PART 5 hint said |N(w) cap Z| = 3 pairwise opposite was possible
tri_opp=[t for t in itertools.combinations(range(6),3)
         if all(min((b-a)%6,(a-b)%6)==3 for a,b in itertools.combinations(t,2))]
check("the BRIEF's PART 5 hint was WRONG: three pairwise-opposite vertices on a C6 do not exist",
      len(tri_opp)==0, f"{len(tri_opp)} such triples")
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
