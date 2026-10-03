import numpy as np, itertools, math, random, sys
def cyclo_pool(m, coeffs=(-1,0,1), deg=None, rmax=1.8):
    z=[complex(math.cos(2*math.pi*j/m), math.sin(2*math.pi*j/m)) for j in range(m)]
    deg=deg or {5:4,8:4,10:4,12:4,7:6,9:6}[m]
    pts=set()
    for c in itertools.product(coeffs, repeat=deg):
        w=sum(ci*z[j] for j,ci in enumerate(c))
        if abs(w)<=rmax+1e-9: pts.add((round(w.real,9),round(w.imag,9)))
    return sorted(pts)
def prep(pts):
    P=np.array(pts); N=len(P)
    D2=((P[:,None,:]-P[None,:,:])**2).sum(-1)
    # quantize distances
    keys=np.round(D2*1e7).astype(np.int64)
    return P,keys
def collinear_mask(P):
    N=len(P); X=P[:,0]; Y=P[:,1]
    return X,Y
def ncol(S,P):
    c=0
    for i,j,k in itertools.combinations(S,3):
        a=P[j]-P[i]; b=P[k]-P[i]
        if abs(a[0]*b[1]-a[1]*b[0])<1e-7: c+=1
    return c
def score(S,P,K):
    sub=K[np.ix_(S,S)]
    ms=[len(set(r.tolist()))-1 for r in sub]
    c=ncol(S,P)
    return max(ms)+0.02*sum(ms)/len(S)+3*c, ms, c
def sa(P,K,n,iters,seed):
    rnd=random.Random(seed); N=len(P)
    S=rnd.sample(range(N),n); sc,ms,c=score(S,P,K); best=(sc,list(S),ms,c)
    for it in range(iters):
        T=1.0*(1-it/iters)+0.02
        i=rnd.randrange(n); new=rnd.randrange(N)
        if new in S: continue
        S2=list(S); S2[i]=new
        sc2,ms2,c2=score(S2,P,K)
        if sc2<=sc or rnd.random()<math.exp((sc-sc2)/T):
            S,sc,ms,c=S2,sc2,ms2,c2
            if sc<best[0]: best=(sc,list(S),ms,c)
    return best
if __name__=='__main__':
    m=int(sys.argv[1]); rmax=float(sys.argv[2]); ns=[int(x) for x in sys.argv[3].split(',')]; restarts=int(sys.argv[4]); iters=int(sys.argv[5])
    pts=cyclo_pool(m,rmax=rmax); P,K=prep(pts); print('pool',m,len(pts),flush=True)
    for n in ns:
        bestall=None
        for r in range(restarts):
            b=sa(P,K,n,iters,r)
            if bestall is None or b[0]<bestall[0]: bestall=b
        sc,S,ms,c=bestall
        print('m',m,'n=',n,'M=',max(ms),'col',c,'Ms',sorted(ms),'pts',[tuple(P[i]) for i in S],flush=True)
