import numpy as np, itertools
from scipy.optimize import minimize
from mis import *
from ring6 import build, pts
s3=np.sqrt(3)
# 1) minimal endpoint distance of a 5-rhombus chain with turnings in [-60,60]
def dist5(ts): v=build(list(ts)); return np.hypot(*(v[5]-v[0]))
best=9
for start in itertools.product([-60,0,30,60],repeat=4):
    r=minimize(lambda x: dist5(np.clip(x,-60,60)), np.array(start,float), method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-12,'maxiter':4000})
    best=min(best,dist5(np.clip(r.x,-60,60)))
print('min endpoint distance 5-chain:',best,'sqrt3=',s3)
# 2) ring6 variants: turnings (t1..t5) with closure |v6-v0|=1; allow some = 60 exactly
from scipy.optimize import brentq
def ring_with(fixed60):
    # hinges in fixed60 have turning 60, the others common value t
    def f(t):
        ts=[60 if i in fixed60 else t for i in range(5)]
        v=build(ts); return np.hypot(*(v[6]-v[0]))-1
    xs=np.linspace(0,60,601); sols=[]
    for a,b in zip(xs[:-1],xs[1:]):
        if f(a)*f(b)<0: sols.append(brentq(f,a,b))
    return sols
for k in range(0,4):
    for fixed in itertools.combinations(range(5),k):
        for t in ring_with(set(fixed)):
            ts=[60 if i in fixed else t for i in range(5)]
            v=build(ts); P=pts(v,6); E,dm=penny_edges(P,1e-6)
            if dm<1-1e-6: continue
            al=alpha_from_edges(len(P),E)
            # try deletions of up to 3 vertices to get alpha*16 <= 5*n ... record best ratio
            n=len(P); best=(al/n,())
            adj=[0]*n
            for a,b in E: adj[a]|=1<<b; adj[b]|=1<<a
            for r in (1,2,3):
                for S in itertools.combinations(range(n),r):
                    keep=[i for i in range(n) if i not in S]
                    mp={o:i for i,o in enumerate(keep)}
                    E2=[(mp[a],mp[b]) for a,b in E if a in mp and b in mp]
                    a2=alpha_from_edges(len(keep),E2)
                    if a2/len(keep)<best[0]-1e-12: best=(a2/len(keep),S,a2,len(keep))
            print(fixed,round(t,3),'n',n,'E',len(E),'alpha',al,'best sub',best)
