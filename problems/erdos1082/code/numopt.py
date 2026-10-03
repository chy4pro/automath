import numpy as np, itertools, sys, math
from scipy.optimize import minimize
def kmeans1d_cost(v,k):
    # v sorted; optimal partition into <=k contiguous groups minimizing SSE (on squared distances, relative)
    m=len(v); pre=np.concatenate([[0],np.cumsum(v)]); pre2=np.concatenate([[0],np.cumsum(v*v)])
    def sse(i,j): # v[i:j]
        s=pre[j]-pre[i]; s2=pre2[j]-pre2[i]; return s2-s*s/(j-i)
    INF=1e18; dp=np.full((k+1,m+1),INF); dp[0,0]=0
    for g in range(1,k+1):
        for j in range(1,m+1):
            best=INF
            for i in range(g-1,j):
                c=dp[g-1,i]+sse(i,j)
                if c<best: best=c
            dp[g,j]=best
    return dp[k,m]
def obj(x,n,k,trip):
    P=x.reshape(n,2)
    D2=((P[:,None]-P[None])**2).sum(-1)
    tot=0.0
    for i in range(n):
        v=np.sort(np.delete(D2[i],i))
        tot+=kmeans1d_cost(v,k)
    # barriers
    dmin=D2[np.triu_indices(n,1)].min()
    pen=max(0,1-dmin)**2*100
    i,j,l=trip
    a=P[j]-P[i]; b=P[l]-P[i]
    cr=np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])/np.sqrt((a*a).sum(1)*(b*b).sum(1))
    pen+=100*(np.maximum(0,0.08-cr)**2).sum()
    scale=D2.max()
    return tot/scale**2*1e2+pen
def run(n,k,trials,seed=0):
    rng=np.random.default_rng(seed)
    trip=np.array(list(itertools.combinations(range(n),3))).T
    best=[]
    for t in range(trials):
        x0=rng.normal(size=2*n)*2
        r=minimize(obj,x0,args=(n,k,trip),method='L-BFGS-B',options={'maxiter':3000})
        r=minimize(obj,r.x,args=(n,k,trip),method='Nelder-Mead',options={'maxiter':20000,'xatol':1e-12,'fatol':1e-16})
        best.append((r.fun,r.x))
    best.sort(key=lambda z:z[0])
    return best
if __name__=='__main__':
    n=int(sys.argv[1]);k=int(sys.argv[2]);trials=int(sys.argv[3]); seed=int(sys.argv[4]) if len(sys.argv)>4 else 0
    b=run(n,k,trials,seed)
    for f,x in b[:5]:
        print(n,k,'obj',f)
    np.save(f'best_{n}_{k}_{seed}.npy',b[0][1])
