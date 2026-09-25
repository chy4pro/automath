"""Exact MILP: for r moduli with max(A) = m exactly, k blocks (window [0, k*m)), minimise the covered set size.
A Hall failure (no matching) is implied when min |S| <= r-1.  Usage: python hall3.py r m k [--loops-only]
Model: choose r distinct moduli a in [2,m] (m forced), each with residue rho in [0,a); covered set = union of multiples.
"""
import sys, time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
def solve(r,m,k,loops_only=False,time_limit=600):
    W=k*m; amin=(m//2+1) if loops_only else 2
    cvars=[(a,rho) for a in range(amin,m+1) for rho in range(a)]
    nc=len(cvars); ns=W; n=nc+ns
    cost=np.zeros(n); cost[nc:]=1.0
    rows=[]; lo=[]; hi=[]
    A=lil_matrix((0,n))
    cons=[]
    # sum_rho c_{a,rho} <= 1 ; for a=m: == 1
    for a in range(amin,m+1):
        idx=[i for i,(aa,_) in enumerate(cvars) if aa==a]
        row=np.zeros(n); row[idx]=1
        cons.append((row,1 if a==m else 0,1))
    row=np.zeros(n); row[:nc]=1; cons.append((row,r,r))
    # coverage: s_p - c_{a,rho} >= 0 for p ≡ rho mod a
    for i,(a,rho) in enumerate(cvars):
        for p in range(rho,W,a):
            row=np.zeros(n); row[nc+p]=1; row[i]=-1; cons.append((row,0,np.inf))
    M=np.array([c[0] for c in cons]); L=np.array([c[1] for c in cons]); U=np.array([c[2] for c in cons])
    res=milp(cost,constraints=LinearConstraint(M,L,U),integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":time_limit})
    if res.x is None: return None,None,None,res
    x=np.round(res.x); chosen=[cvars[i] for i in range(nc) if x[i]>0.5]; S=[p for p in range(W) if x[nc+p]>0.5]
    return int(round(res.fun)),chosen,S,res
if __name__=="__main__":
    r=int(sys.argv[1]); m=int(sys.argv[2]); k=int(sys.argv[3]); lo="--loops-only" in sys.argv
    t=time.time(); val,ch,S,res=solve(r,m,k,lo)
    print(f"r={r} m={m} k={k} loops_only={lo}: min|S|={val} (failure iff <= {r-1}) status={res.status} {time.time()-t:.1f}s")
    if val is not None and val<=r-1: print(" moduli/residues:",ch); print(" covered:",S)
