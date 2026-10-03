import numpy as np, itertools, sys, math
from scipy.optimize import least_squares
def dp_groups(v,k):
    m=len(v); pre=np.concatenate([[0],np.cumsum(v)]); pre2=np.concatenate([[0],np.cumsum(v*v)])
    INF=1e300; dp=[[INF]*(m+1) for _ in range(k+1)]; arg=[[0]*(m+1) for _ in range(k+1)]; dp[0][0]=0
    for g in range(1,k+1):
        for j in range(1,m+1):
            best=INF;bi=0
            for i in range(g-1,j):
                s=pre[j]-pre[i]; s2=pre2[j]-pre2[i]; c=dp[g-1][i]+s2-s*s/(j-i)
                if c<best: best=c;bi=i
            dp[g][j]=best;arg[g][j]=bi
    cuts=[];j=m
    for g in range(k,0,-1):
        i=arg[g][j]; cuts.append((i,j)); j=i
    return dp[k][m],cuts[::-1]
def assign(P,k):
    n=len(P); D2=((P[:,None]-P[None])**2).sum(-1); groups=[];tot=0
    for p in range(n):
        idx=[q for q in range(n) if q!=p]; v=D2[p,idx]; o=np.argsort(v); vs=v[o]
        c,cuts=dp_groups(vs,k); tot+=c
        for (i,j) in cuts:
            g=[idx[o[t]] for t in range(i,j)]
            if len(g)>1: groups.append((p,g))
    return groups,tot/D2.max()**2
def resid(x,n,groups,trip):
    P=x.reshape(n,2); D2=((P[:,None]-P[None])**2).sum(-1); sc=D2.max()
    r=[]
    for p,g in groups:
        for q in g[1:]: r.append((D2[p,q]-D2[p,g[0]])/sc)
    i,j,l=trip; a=P[j]-P[i]; b=P[l]-P[i]
    cr=np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])/np.sqrt((a*a).sum(1)*(b*b).sum(1))
    r.extend(list(3*np.maximum(0,0.05-cr)))
    r.append(10*max(0,1-math.sqrt(D2[np.triu_indices(n,1)].min())))
    r.append(0.01*(math.sqrt(sc)-4))
    return np.array(r)
def solve(n,k,trials,seed):
    rng=np.random.default_rng(seed); trip=np.array(list(itertools.combinations(range(n),3))).T
    out=[]
    for t in range(trials):
        x=rng.normal(size=2*n)*2
        prev=None
        for it in range(30):
            groups,c=assign(x.reshape(n,2),k)
            key=sorted((p,tuple(sorted(g))) for p,g in groups)
            if key==prev: break
            prev=key
            x=least_squares(resid,x,args=(n,groups,trip),method='trf',max_nfev=400).x
        groups,c=assign(x.reshape(n,2),k)
        P=x.reshape(n,2); i,j,l=trip; a=P[j]-P[i]; b=P[l]-P[i]
        cr=(np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])/np.sqrt((a*a).sum(1)*(b*b).sum(1))).min()
        out.append((c,cr,x))
    out.sort(key=lambda z:z[0])
    return out
if __name__=='__main__':
    n=int(sys.argv[1]);k=int(sys.argv[2]);trials=int(sys.argv[3]);seed=int(sys.argv[4])
    out=solve(n,k,trials,seed)
    good=[o for o in out if o[0]<1e-14 and o[1]>1e-3]
    print('n',n,'k',k,'trials',trials,'best costs',[f'{o[0]:.1e}/{o[1]:.2e}' for o in out[:6]],'num good',len(good),flush=True)
    if good: np.save(f'good_{n}_{k}_{seed}.npy',np.array([g[2] for g in good]))
