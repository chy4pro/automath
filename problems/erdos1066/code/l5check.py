import numpy as np, math, time
from good import build, lattice_pts
from mis import popcount, bits, alpha_from_edges
from exhaust import min_good
from dense_grow import grow
def outer_cycle(P,adj):
    n=len(P)
    # start at lowest (then leftmost) point; walk outer face keeping face on the right... use "most clockwise" rule
    s=min(range(n),key=lambda i:(P[i][1],P[i][0]))
    nb=lambda v:[u for u in bits(adj[v])]
    ang=lambda v,u: math.atan2(P[u][1]-P[v][1],P[u][0]-P[v][0])
    # first edge: from s, neighbour with smallest angle (all neighbours have angle in [0,pi))
    u=min(nb(s),key=lambda w: ang(s,w)%(2*math.pi))
    walk=[s]; prev,cur=s,u
    while True:
        walk.append(cur)
        # at cur, coming from prev: choose next neighbour turning most to the left? outer face on the right when going ccw
        a0=ang(cur,prev)
        best=None;bd=-1
        for w in nb(cur):
            d=(a0-ang(cur,w))%(2*math.pi)
            if d>2*math.pi-1e-12: d=0.0
            if d>bd: bd=d;best=w
        prev,cur=cur,best
        if prev==s and cur==u: break
        if len(walk)>4*n: return None
    walk=walk[:-1]
    return walk
def check(P):
    adj=build(P); n=len(P)
    if min(popcount(a) for a in adj)<3: return 'deg<3'
    W=outer_cycle(P,adj)
    if W is None or len(set(W))!=len(W): return 'nonsimple'
    area=sum(P[W[i-1]][0]*P[W[i]][1]-P[W[i]][0]*P[W[i-1]][1] for i in range(len(W)))
    if area<0: W=W[::-1]
    b=len(W); pos={v:i for i,v in enumerate(W)}
    # chordless?
    for i,v in enumerate(W):
        for u in bits(adj[v]):
            if u in pos and (pos[u]-i)%b not in (1,b-1): return 'chord'
    # interior angles and turning
    tau=[]
    for i,v in enumerate(W):
        p,q=W[i-1],W[(i+1)%b]
        a1=math.atan2(P[p][1]-P[v][1],P[p][0]-P[v][0]); a2=math.atan2(P[q][1]-P[v][1],P[q][0]-P[v][0])
        th=math.degrees((a1-a2)%(2*math.pi))  # interior angle (interior on the left of ccw walk)
        tau.append(180-th)
    tot=sum(tau)
    res=[]
    if b%2==0:
        for par in (0,1):
            I=W[par::2]; N=0
            for v in I: N|=adj[v]|(1<<v)
            s=4*len(I)-popcount(N); bound=sum(tau[par::2])/60
            res.append((s,round(bound,3)))
        return ('even',b,round(tot,6),res)
    else:
        best=None
        for j in range(b):
            I=[W[(j+2*t)%b] for t in range((b-1)//2)]
            N=0
            for v in I: N|=adj[v]|(1<<v)
            s=4*len(I)-popcount(N)
            bound=sum(tau[(j+2*t)%b] for t in range((b-1)//2))/60-1
            assert s>=bound-1e-9,(s,bound)
            best=max(best or -99,s)
        return ('odd',b,round(tot,6),best)
# lattice hexagons and random lattice blobs
for S in [3,4,5,8]:
    P=lattice_pts(lambda p,i,j: max(abs(i),abs(j),abs(i+j))<=S,R=S+1)
    print('hex',S,check(P))
rng=np.random.default_rng(5); cnt={}
for t in range(300):
    P=grow(int(rng.integers(15,60)),rng,12,float(rng.uniform(1,4)))
    # prune deg<3
    while True:
        adj=build(P); d=np.array([popcount(a) for a in adj])
        if len(P)<4 or d.min()>=3: break
        P=P[d>=3]
    if len(P)<4: continue
    r=check(P)
    key=r if isinstance(r,str) else r[0]
    cnt[key]=cnt.get(key,0)+1
    if not isinstance(r,str):
        if r[0]=='even': assert max(s for s,_ in r[3])>=3 and all(s>=bd-1e-9 for s,bd in r[3]), r
        else: assert r[3]>=2, r
        assert abs(r[2]-360)<1e-6, r
print('random clusters outcome counts',cnt)
