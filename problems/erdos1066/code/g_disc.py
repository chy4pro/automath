from good import *
import numpy as np, sys
res=[]
rng=np.random.default_rng(0)
for trial in range(40):
    R=rng.uniform(3,7); c=rng.uniform(0,1,2)
    P=lattice_pts(lambda p,i,j: np.hypot(*(p-c))<=R, R=int(R)+3)
    adj=build(P); n=len(P)
    degs=[popcount(a) for a in adj]
    if min(degs)<3:
        res.append((R,n,'deg<3')); continue
    best=beam_search(adj,m=9,width=150)
    g=min([k for k in best if best[k][0]>=1],default=None)
    res.append((round(R,2),n,g,[best[k][0] for k in sorted(best)]))
    print(res[-1],flush=True)
