import numpy as np, random, time, sys
from mis import *
def grow(n, rng, ptri=0.5):
    P=[np.array([0.0,0.0])]
    # first second point
    P.append(np.array([1.0,0.0]))
    tries=0
    while len(P)<n and tries<20000:
        tries+=1
        A=np.array(P)
        i=rng.randrange(len(P))
        D=np.hypot(*(A-A[i]).T)
        cand=[j for j in range(len(P)) if j!=i and D[j]<=2-1e-9]
        if not cand: continue
        # prefer pairs at distance 1 with prob ptri
        c1=[j for j in cand if abs(D[j]-1)<1e-7]
        if c1 and rng.random()<ptri: j=rng.choice(c1)
        else: j=rng.choice(cand)
        p,q=A[i],A[j]; d=D[j]
        m=(p+q)/2; h=np.sqrt(max(0,1-(d/2)**2)); u=(q-p)/d; perp=np.array([-u[1],u[0]])
        opts=[m+h*perp,m-h*perp]; rng.shuffle(opts)
        for x in opts:
            if np.min(np.hypot(*(A-x).T))>=1-1e-9:
                P.append(x); break
    return np.array(P)
if __name__=="__main__":
    seed=int(sys.argv[1]); N=int(sys.argv[2]); reps=int(sys.argv[3])
    rng=random.Random(seed); best=1
    stats=[]
    for r in range(reps):
        P=grow(N,rng,ptri=rng.random())
        E,dm=penny_edges(P)
        assert dm>1-1e-6
        al=alpha_from_edges(len(P),E)
        ratio=al/len(P); stats.append(ratio)
        if ratio<best:
            best=ratio; np.save(f'best_{seed}_{N}.npy',P)
            print(r,len(P),len(E),al,ratio,flush=True)
    print('min',min(stats),'mean',np.mean(stats))
