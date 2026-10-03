import numpy as np, random, sys, math
from mis import bits, popcount
from good import beam_search
NB=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def graph(S):
    S=sorted(S); idx={p:i for i,p in enumerate(S)}
    adj=[0]*len(S)
    for p,i in idx.items():
        for d in NB:
            q=(p[0]+d[0],p[1]+d[1])
            if q in idx: adj[i]|=1<<idx[q]
    return S,adj
def gval(S,m=8,width=60):
    S,adj=graph(S)
    if min(popcount(a) for a in adj)<3: return 1,None
    best=beam_search(adj,m=m,width=width)
    for k in sorted(best):
        if best[k][0]>=1: return k,best
    return m+1,best
def hexagon(s):
    return {(i,j) for i in range(-s,s+1) for j in range(-s,s+1) if abs(i+j)<=s}
def run(seed,steps):
    rng=random.Random(seed)
    S=hexagon(5)
    g,_=gval(S); best=(g,set(S))
    for t in range(steps):
        S2=set(S)
        # boundary cells
        bd=[p for p in S2 if any((p[0]+d[0],p[1]+d[1]) not in S2 for d in NB)]
        out=list({(p[0]+d[0],p[1]+d[1]) for p in S2 for d in NB}-S2)
        r=rng.random()
        if r<0.5 and len(S2)>40: S2.discard(rng.choice(bd))
        else: S2.add(rng.choice(out))
        if len(S2)>110: continue
        g2,_=gval(S2)
        if g2>=g or rng.random()<0.15:
            S,g=S2,g2
            if g>best[0]:
                best=(g,set(S)); print(t,'g',g,'n',len(S),flush=True)
    return best
if __name__=="__main__":
    b=run(int(sys.argv[1]),int(sys.argv[2]))
    print('best',b[0],len(b[1]))
    import pickle; pickle.dump(b,open(f'latbest_{sys.argv[1]}.pkl','wb'))
