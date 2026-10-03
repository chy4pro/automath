import numpy as np, time
from good import build
from exhaust import min_good
from mis import popcount
from shell import shell
def prune(P):
    while True:
        adj=build(P); degs=np.array([popcount(a) for a in adj])
        if degs.min()>=3: return P,adj
        P=P[degs>=3]
for s in [6,8]:
    for rows in [1,2,3,4]:
        for ext in [0,1,2]:
            P=shell(s,rows,extend=ext); P,adj=prune(P); n=len(P)
            degs=[popcount(a) for a in adj]
            r=min_good(adj,7)
            print('s',s,'rows',rows,'ext',ext,'n',n,'deg',np.bincount(degs).tolist(),'min good',r[0] if r else '>7',flush=True)
