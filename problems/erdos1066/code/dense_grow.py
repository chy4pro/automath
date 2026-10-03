import numpy as np, random, sys, time
from mis import *
def contacts(P,x):
    d=np.hypot(*(P-x).T)
    if d.min()<1-1e-7: return -1
    return int((abs(d-1)<1e-7).sum())
def grow(n,rng,K=12,temp=1.0):
    dirs=[np.array([np.cos(2*np.pi*k/K),np.sin(2*np.pi*k/K)]) for k in range(K)]
    P=np.array([[0.0,0.0]])
    while len(P)<n:
        cands=[];scores=[]
        for p in P:
            for d in dirs:
                x=p+d
                c=contacts(P,x)
                if c>0:
                    cands.append(x);scores.append(c)
        scores=np.array(scores,float)
        w=np.exp(temp*scores); w/=w.sum()
        i=rng.choice(len(cands),p=w)
        P=np.vstack([P,cands[i]])
    return P
if __name__=="__main__":
    seed=int(sys.argv[1]); n=int(sys.argv[2]); reps=int(sys.argv[3]); K=int(sys.argv[4]); temp=float(sys.argv[5])
    rng=np.random.default_rng(seed); best=1; t0=time.time()
    for r in range(reps):
        P=grow(n,rng,K,temp)
        E,dm=penny_edges(P); assert dm>1-1e-6
        al=alpha_from_edges(len(P),E)
        if al/len(P)<best or al*3<len(P):
            best=min(best,al/len(P)); np.save(f'dg_{seed}_{n}_{K}_{r}.npy',P)
            print(r,len(P),len(E),al,al/len(P),flush=True)
    print('done',time.time()-t0)
