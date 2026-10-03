import numpy as np
from mis import *
from good import build, beam_search, savings
def e(a): return np.array([np.cos(np.radians(a)),np.sin(np.radians(a))])
def dodec(R):
    P=[np.zeros(2)]
    h=[e(60*k) for k in range(6)]
    P+=h
    for k in range(6):
        u=e(60*k+30)
        for j in range(1,R+1):
            P.append(h[k]+j*u); P.append(h[(k+1)%6]+j*u)
    for k in range(6):
        a=e(60*k-30); b=e(60*k+30)
        for i in range(1,R+1):
            for j in range(1,R+1):
                if i+j<=R: P.append(h[k]+i*a+j*b)
    P=np.array(P)
    P=np.unique(np.round(P,9),axis=0)
    return P
if __name__=="__main__":
    for R in [3,4,5,6]:
        P=dodec(R); adj=build(P); n=len(P)
        degs=[popcount(a) for a in adj]
        E=[(i,j) for i in range(n) for j in range(i+1,n) if adj[i]>>j&1]
        al=alpha_from_edges(n,E) if n<=200 else None
        best=beam_search(adj,m=10,width=150)
        print('R',R,'n',n,'deg hist',np.bincount(degs),'alpha',al, al/n if al else None)
        print('   beam savings by size',[(k,best[k][0]) for k in sorted(best)])
