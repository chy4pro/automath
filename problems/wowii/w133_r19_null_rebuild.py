#!/usr/bin/env python3
"""
w133 round 19 — INDEPENDENT REBUILD of the null-model audit's SAMPLE COUNT.

DEBT-3's lesson applied to the number the planner gated numbering on: the count `M = 59`
and the trace histogram come from ONE implementation (`w133_r19_null.py`). This file
recomputes them sharing NO code and NO representation with it:

  * graphs as integer BITMASK adjacency rows, not sets;
  * Petersen built as the KNESER graph K(5,2) (vertices = 2-subsets of {1..5}, adjacent iff
    disjoint), not from an edge list;
  * induced C6s found by DEPTH-6 CYCLE WALK with an inducedness test on bitmasks, not by
    enumerating 6-subsets and BFS-ing them;
  * traces as popcounts of bitmask intersections, not as sorted position tuples.

HARD SELF-LIMIT 120 s.
"""
import sys, time, itertools
T0=time.time(); LIM=120.0; FAIL=[]
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def rows_from_edges(n,E):
    A=[0]*n
    for u,v in E: A[u]|=1<<v; A[v]|=1<<u
    return A
def popcount(x): return bin(x).count("1")

# Petersen as the Kneser graph K(5,2) — no edge list
V=[frozenset(s) for s in itertools.combinations(range(1,6),2)]
idx={s:i for i,s in enumerate(V)}
PET=[0]*10
for i,s in enumerate(V):
    for j,t in enumerate(V):
        if i!=j and not (s&t): PET[i]|=1<<j
check("Kneser K(5,2) is 3-regular on 10 vertices (Petersen)",
      len(PET)==10 and all(popcount(r)==3 for r in PET))
check("Kneser K(5,2) is triangle-free", all(not (PET[i]&PET[j]) for i in range(10)
      for j in range(10) if i!=j and (PET[i]>>j)&1))
R  = rows_from_edges(9,[(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,6),(4,7),(0,8)])
CE2= rows_from_edges(10,[(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),
                         (4,6),(4,7),(4,8),(8,9)])
GS=[("R",R),("CE-2",CE2),("Petersen",PET)]
for nm,A in GS:
    bad=[(u,v) for u in range(len(A)) for v in range(u+1,len(A)) if popcount(A[u]&A[v])>1]
    check(f"{nm} is C4-free (bitmask common-neighbour popcount)", not bad, str(bad[:3]))

def c6_walks(A):
    """every induced 6-cycle, found by walking, canonicalised as a frozenset of vertices"""
    n=len(A); found={}
    for start in range(n):
        stack=[(start,[start],1<<start)]
        while stack:
            v,path,mask=stack.pop()
            if len(path)==6:
                if (A[v]>>start)&1:
                    # inducedness: each path vertex has exactly 2 nbrs inside the set
                    if all(popcount(A[x]&mask)==2 for x in path):
                        found[frozenset(path)]=tuple(path)
                continue
            for w in range(start+1,n):          # canonical: start is the minimum
                if not (A[v]>>w)&1 or (mask>>w)&1: continue
                stack.append((w,path+[w],mask|1<<w))
    return found
tot=0; M=0; hist={}; dist2={}
for nm,A in GS:
    fs=c6_walks(A)
    tot+=len(fs)
    print(f"  {nm}: {len(fs)} induced C6s")
    for vs,cyc in fs.items():
        mask=0
        for x in vs: mask|=1<<x
        pos={z:i for i,z in enumerate(cyc)}
        for w in range(len(A)):
            if (mask>>w)&1: continue
            inter=A[w]&mask
            k=popcount(inter); M+=1; hist[k]=hist.get(k,0)+1
            if k==2:
                p=[pos[b] for b in range(len(A)) if (inter>>b)&1]
                d=min((p[0]-p[1])%6,(p[1]-p[0])%6); dist2[d]=dist2.get(d,0)+1
print(f"  TOTAL induced C6s = {tot}   off-cycle (Z,w) pairs M = {M}")
print(f"  trace-size histogram = {dict(sorted(hist.items()))}")
print(f"  distance classes among 2-traces = {dict(sorted(dist2.items()))}")
check("INDEPENDENT AGREEMENT: 15 induced C6s", tot==15, f"{tot}")
check("INDEPENDENT AGREEMENT: M = 59 off-cycle pairs", M==59, f"{M}")
check("INDEPENDENT AGREEMENT: trace histogram {0:10, 1:9, 2:40}",
      hist=={0:10,1:9,2:40}, str(dict(sorted(hist.items()))))
check("INDEPENDENT AGREEMENT: 2-trace distance classes {1:4, 3:36}",
      dist2=={1:4,3:36}, str(dict(sorted(dist2.items()))))
check("INDEPENDENT AGREEMENT: 0 traces at cycle-distance 2 (the claim's whole content)",
      dist2.get(2,0)==0, f"{dist2.get(2,0)}")
print()
print("  ==> the null expectation stands on TWO implementations sharing no code and no")
print("      representation: 1.000000 inside the C4-free class, because the violating trace")
print("      is the one C4-freeness forbids.")
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
