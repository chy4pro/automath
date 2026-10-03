import numpy as np, itertools, heapq
from mis import bits, popcount
def build(P,tol=1e-7):
    P=np.asarray(P); n=len(P)
    D=np.hypot(P[:,None,0]-P[None,:,0],P[:,None,1]-P[None,:,1])
    adj=[0]*n
    for i in range(n):
        for j in range(n):
            if i!=j and abs(D[i,j]-1)<tol: adj[i]|=1<<j
    assert D[np.triu_indices(n,1)].min()>1-1e-6
    return adj
def closed(adj,v): return adj[v]|(1<<v)
def savings(adj,I):
    N=0
    for v in I: N|=closed(adj,v)
    return 4*len(I)-popcount(N)
def beam_search(adj, m=8, width=200, starts=None, allowed=None):
    n=len(adj)
    if allowed is None: allowed=(1<<n)-1
    if starts is None: starts=[v for v in range(n) if allowed>>v&1]
    best={}  # size -> (s, I)
    beam=[]
    for v in starts:
        N=closed(adj,v); beam.append((4-popcount(N),(v,),N))
    seen=set()
    for k in range(1,m+1):
        for s,I,N in beam:
            if k not in best or s>best[k][0]: best[k]=(s,I)
        if k==m: break
        cand={}
        for s,I,N in beam:
            # neighbours at distance exactly 2 of I (in N(N[I]) \ N[I])
            ext=0
            for u in bits(N): ext|=adj[u]
            ext&=~N & allowed
            for x in bits(ext):
                I2=tuple(sorted(I+(x,)))
                if I2 in cand: continue
                N2=N|closed(adj,x)
                cand[I2]=(4*(k+1)-popcount(N2),I2,N2)
        beam=heapq.nlargest(width,cand.values(),key=lambda t:t[0])
    return best
def lattice_pts(cond,R=12):
    pts=[]
    for i in range(-R,R+1):
        for j in range(-R,R+1):
            p=np.array([i+j/2,j*np.sqrt(3)/2])
            if cond(p,i,j): pts.append(p)
    return np.array(pts)
