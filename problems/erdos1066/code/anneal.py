import numpy as np, random, sys, time, math
from mis import *
from dense_grow import grow, contacts
def alpha_of(P):
    E,dm=penny_edges(P)
    return alpha_from_edges(len(P),E)
def run(seed,n0,K,steps,T):
    rng=np.random.default_rng(seed)
    dirs=[np.array([np.cos(2*np.pi*k/K),np.sin(2*np.pi*k/K)]) for k in range(K)]
    P=grow(n0,rng,K,3.0)
    a=alpha_of(P); f=a-len(P)/3
    best=(f,P.copy(),a)
    for s in range(steps):
        if rng.random()<0.5 and len(P)>8:
            i=rng.integers(len(P)); Q=np.delete(P,i,axis=0)
        else:
            cands=[]
            for p in P:
                for d in dirs:
                    x=p+d; c=contacts(P,x)
                    if c>=2: cands.append((c,x))
            if not cands: continue
            cs=np.array([c for c,_ in cands],float); w=np.exp(1.5*cs); w/=w.sum()
            x=cands[rng.choice(len(cands),p=w)][1]
            Q=np.vstack([P,x])
        a2=alpha_of(Q); f2=a2-len(Q)/3
        if len(Q)>60: f2+=0.05*(len(Q)-60)
        if f2<=f or rng.random()<math.exp(-(f2-f)/T):
            P,f,a=Q,f2,a2
            if f<best[0]-1e-9:
                best=(f,P.copy(),a)
    return best
if __name__=="__main__":
    seed=int(sys.argv[1]); K=int(sys.argv[2]); steps=int(sys.argv[3])
    for r in range(int(sys.argv[4])):
        f,P,a=run(seed*100+r,30,K,steps,0.3)
        print(seed*100+r,'best f',round(f,3),'n',len(P),'alpha',a,a/len(P),flush=True)
        np.save(f'ann_{seed*100+r}_{K}.npy',P)
