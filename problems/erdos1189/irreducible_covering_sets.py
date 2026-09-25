#!/usr/bin/env python3
# Enumerate irreducible covering sets (Erdos problem 1189) of size k: distinct moduli 1<n_1<...<n_k such that
# some choice of residues covers Z, and no proper subset of the moduli is a covering set.
# Uses: Simpson bound n_k <= 2^(k-1); density necessity sum 1/n_i > 1; SAT (CaDiCaL via pysat) for coverability.
# Hard internal time cap (mem-6d09dbe9). Results appended incrementally to results_k<k>.txt.
import sys, math, time, itertools
from functools import reduce, lru_cache
from pysat.solvers import Cadical153
T0=time.time(); CAP=float(sys.argv[2]) if len(sys.argv)>2 else 1200.0
K=int(sys.argv[1]) if len(sys.argv)>1 else 6
def lcm(a,b): return a*b//math.gcd(a,b)
@lru_cache(maxsize=None)
def can_cover(mods):
    L=reduce(lcm,mods,1)
    var=lambda i,a: 1+sum(mods[:i])+a   # residue a of modulus i
    s=Cadical153()
    for i,n in enumerate(mods):
        s.add_clause([var(i,a) for a in range(n)])          # at least one residue
        for a in range(n):                                   # at most one residue per modulus (essential)
            for b in range(a+1,n): s.add_clause([-var(i,a),-var(i,b)])
    s.add_clause([var(0,0)])                                 # translation symmetry: first residue 0
    for t in range(L):
        s.add_clause([var(i, t%n) for i,n in enumerate(mods)])
    ok=s.solve(); s.delete(); return ok
def irreducible(mods):
    if not can_cover(mods): return False
    return not any(can_cover(mods[:i]+mods[i+1:]) for i in range(len(mods)))
bound=2**(K-1); out=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), f'results_k{K}.txt'),'a'); found=0; checked=0; capped=False
def rec(start, chosen, s):
    global found, checked, capped
    if capped: return
    if time.time()-T0>CAP: capped=True; return
    need=K-len(chosen)
    if need==0:
        if s>1+1e-12:
            checked+=1
            if irreducible(tuple(chosen)):
                found+=1; out.write(f"{chosen} sum={s:.6f} lcm={reduce(lcm,chosen,1)}\n"); out.flush()
        return
    for n in range(start, bound+1):
        opt=s+sum(1/(n+i) for i in range(need))
        if opt<=1: break
        rec(n+1, chosen+[n], s+1/n)
assert can_cover((2,3,4,6,12)) and not can_cover((2,3,4,12)) and not can_cover((2,3,4,6)), 'self-test failed'
rec(2,[],0.0)
out.write(f"# k={K} done={not capped} I(k)={found} candidates_checked={checked} elapsed={time.time()-T0:.1f}s\n"); out.close()
print(f"k={K} done={not capped} I(k)={found} checked={checked} elapsed={time.time()-T0:.1f}s")
