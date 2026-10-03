import numpy as np, random, sys, math, pickle
from mis import bits, popcount
from good import beam_search
def build_adj(P):
    P=np.asarray(P); n=len(P)
    D=np.hypot(P[:,None,0]-P[None,:,0],P[:,None,1]-P[None,:,1])
    adj=[0]*n
    I,J=np.where(abs(D-1)<1e-7)
    for i,j in zip(I,J):
        if i!=j: adj[i]|=1<<int(j)
    return adj
def gval(P,m=8,width=40):
    adj=build_adj(P)
    degs=[popcount(a) for a in adj]
    nlow=sum(1 for d in degs if d<3)
    if nlow: return 1-0.01*nlow,None
    best=beam_search(adj,m=m,width=width)
    for k in sorted(best):
        if best[k][0]>=1: return k,best
    return m+1,best
def run(seed,steps,K=12):
    rng=random.Random(seed)
    dirs=[np.array([np.cos(2*np.pi*k/K),np.sin(2*np.pi*k/K)]) for k in range(K)]
    # start: lattice hexagon side 3
    P=[np.array([i+j/2,j*np.sqrt(3)/2]) for i in range(-3,4) for j in range(-3,4) if abs(i+j)<=3]
    P=np.array(P)
    g,_=gval(P); best=(g,P.copy())
    for t in range(steps):
        r=rng.random()
        if r<0.45 and len(P)>20:
            i=rng.randrange(len(P)); Q=np.delete(P,i,axis=0)
        else:
            cands=[]
            for p in P:
                for d in dirs:
                    x=p+d; dd=np.hypot(*(P-x).T)
                    if dd.min()>=1-1e-7:
                        c=int((abs(dd-1)<1e-7).sum())
                        if c>=2: cands.append((c,x))
            if not cands: continue
            cs=np.array([c for c,_ in cands],float); w=np.exp(1.0*cs); w/=w.sum()
            x=cands[np.random.default_rng(rng.randrange(10**9)).choice(len(cands),p=w)][1]
            Q=np.vstack([P,x])
        if len(Q)>90: continue
        g2,_=gval(Q)
        if g2>=g or rng.random()<0.1:
            P,g=Q,g2
            if g>best[0]:
                best=(g,P.copy()); print(t,'g',g,'n',len(P),flush=True)
                pickle.dump(best,open(f'genbest_{seed}_{K}.pkl','wb'))
    return best
if __name__=="__main__":
    b=run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    print('best',b[0],len(b[1]))
