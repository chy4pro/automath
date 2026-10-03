import numpy as np, time, sys
from good import build
from exhaust import min_good
from mis import popcount, alpha_from_edges
def e(a): return np.array([np.cos(np.radians(a)),np.sin(np.radians(a))])
def core_hex(s):
    P=[]
    for i in range(-s,s+1):
        for j in range(-s,s+1):
            if abs(i+j)<=s: P.append(i*e(0)+j*e(60))
    return P
def shell(s, rows, extend=3):
    P=core_hex(s)
    corners=[s*e(60*k) for k in range(6)]
    pts=list(P)
    def ok(x): return min(np.hypot(*(np.array(pts)-x).T))>=1-1e-7
    for k in range(6):
        c0=corners[k]; c1=corners[(k+1)%6]
        t=(c1-c0)/s; nrm=e(60*k+30)  # outward normal of side k
        for r in range(0,rows+1):
            base=c0+nrm*(1+r*np.sqrt(3)/2)+t*(r/2)
            for i in range(-extend, s+extend+1):
                x=base+i*t
                if ok(x): pts.append(x)
    return np.array(pts)
if __name__=="__main__":
    for s in [4,6,8]:
        for rows in [0,1,2,3]:
            P=shell(s,rows); adj=build(P); n=len(P)
            degs=[popcount(a) for a in adj]
            t=time.time(); r=min_good(adj,6)
            print('s',s,'rows',rows,'n',n,'deg hist',np.bincount(degs).tolist(),'min good',r[0] if r else '>6',round(time.time()-t,1),flush=True)
