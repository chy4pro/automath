#!/usr/bin/env python3
# k=8: SAT irreducibility check on lemma survivors of one prefix file. Internal cap. Output per file.
import sys, math, time
from functools import reduce, lru_cache
from pysat.solvers import Cadical153
fn=sys.argv[1]; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 3000; LMAX=int(sys.argv[3]) if len(sys.argv)>3 else 2000000
def lcm(a,b): return a*b//math.gcd(a,b)
@lru_cache(maxsize=None)
def can_cover(mods):
    L=reduce(lcm,mods,1)
    off=[0]
    for n in mods: off.append(off[-1]+n)
    var=lambda i,a: 1+off[i]+a
    s=Cadical153()
    for i,n in enumerate(mods):
        s.add_clause([var(i,a) for a in range(n)])
        for a in range(n):
            for b in range(a+1,n): s.add_clause([-var(i,a),-var(i,b)])
    s.add_clause([var(0,0)])
    for t in range(L): s.add_clause([var(i,t%n) for i,n in enumerate(mods)])
    ok=s.solve(); s.delete(); return ok
T0=time.time(); found=[]; n=0; skipped=0; capped=False
for line in open(fn):
    if time.time()-T0>CAP: capped=True; break
    parts=list(map(int,line.split())); mods=tuple(parts[:-1]); L=parts[-1]; n+=1
    if L>LMAX: skipped+=1; continue
    if can_cover(mods) and not any(can_cover(mods[:i]+mods[i+1:]) for i in range(len(mods))): found.append(mods)
out=open(fn.replace('k8_surv_','k8_irr_'),'w')
for f in found: out.write(f"{list(f)} sum={sum(1/x for x in f):.6f} lcm={reduce(lcm,f,1)}\n")
out.write(f"# file={fn} checked={n} skipped_L>{LMAX}={skipped} irreducible={len(found)} complete={not capped} t={time.time()-T0:.0f}s\n"); out.close()
print(f"{fn}: checked={n} skipped={skipped} irreducible={len(found)} complete={not capped} t={time.time()-T0:.0f}s")
