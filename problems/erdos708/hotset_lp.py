"""Exact-ish experiments for the hot-set-excluded window LP (Erdos #708, round-15 T3 analogue).
Setting: primes P (weights 1 on p^1), threshold C (analogue of 64), window I of length m.
L_C = sum_{k<=m} (w(k)-C)^+, R = sum_{b in I} (w(b)-1)^+, w = number of primes of P dividing.
W_T = max sum_D c_D * #{b in I \\ T : D|b}  s.t. c>=0, sum_{D|b} c_D <= (w(b)-1)^+ for b in I \\ T.
T = {b in I : w(b) > C + t0}. Reports W_T/L for several t0 and several window types.
"""
import sys, time
from math import factorial, lcm, comb
import numpy as np
from scipy.optimize import linprog
T0=time.time(); LIMIT=float(sys.argv[1]) if len(sys.argv)>1 else 500.0
def w_of(b,P): return sum(1 for p in P if b%p==0)
def solve(P,m,x,C,t0s):
    I=list(range(x+1,x+m+1)); Ds=list(range(1,m+1))
    wI=[w_of(b,P) for b in I]
    L=sum(max(w_of(k,P)-C,0) for k in range(1,m+1)); R=sum(max(v-1,0) for v in wI)
    out={"L":L,"R":R}
    for t0 in t0s:
        keep=[i for i,v in enumerate(wI) if v<=C+t0]
        cnt=np.zeros(len(Ds))
        rows=[];rhs=[]
        for i in keep:
            b=I[i]; row=np.zeros(len(Ds))
            for j,D in enumerate(Ds):
                if b%D==0: row[j]=1.0; cnt[j]+=1
            rows.append(row); rhs.append(max(wI[i]-1,0))
        if not rows: out[t0]=None; continue
        res=linprog(-cnt,A_ub=np.array(rows),b_ub=np.array(rhs),bounds=[(0,None)]*len(Ds),method="highs")
        out[t0]=(-res.fun if res.status==0 else None, len(I)-len(keep))
    return out
cases=[]
# reflected windows around m!
for P,m,C in [([2,3,5,7],35,2),([2,3,5,7,11],40,2),([3,5,7,11,13],100,2),([2,3,5,7,11,13],60,3)]:
    cases.append(("reflect m!",P,m,factorial(m)-m,C))
# lcm windows: B = lcm(P-subset products up to m) -> B = lcm(1..m) also reflective; use B = product of P only
for P,m,C in [([2,3,5,7,11],40,2),([3,5,7,11,13],100,2)]:
    B=1
    for p in P: B*=p
    cases.append(("B=prod P",P,m,B-m,C)); cases.append(("B=prod P, shifted",P,m,B-m//2,C))
# congruence windows: x = 0 (initial segment itself), x = m
for P,m,C in [([2,3,5,7,11],40,2),([3,5,7,11,13],100,2)]:
    cases.append(("x=0",P,m,0,C)); cases.append(("x=m",P,m,m,C))
for name,P,m,x,C in cases:
    if time.time()-T0>LIMIT: print("TIME LIMIT"); break
    r=solve(P,m,x,C,[0,1,2,100])
    print(f"{name:20s} P={P} m={m} C={C}: L={r['L']} R={r['R']} W_T(t0=0)={r[0]} (t0=1)={r[1]} (t0=2)={r[2]} full-window W={r[100]}", flush=True)
print("done in %.1fs"%(time.time()-T0))
