import numpy as np, time
from scipy.optimize import linprog
import importlib.util, sys
sys.path.insert(0,'.')
from mu1 import q_of, jac_fast
D='./'
def slp(n, p0, iters=300, tr=0.3):
    p=p0.copy(); best=(n*q_of(p).max(),p.copy())
    for it in range(iters):
        q=q_of(p); J=jac_fast(p); cur=n*q.max()
        # only keep constraints near active to speed up
        act = np.where(n*q > cur - 0.05)[0]
        nv=n+1; c=np.zeros(nv); c[-1]=1
        A_ub=np.hstack([n*J[act], -np.ones((len(act),1))]); b_ub=-n*q[act]
        A_eq=np.zeros((1,nv)); A_eq[0,:n]=1
        rad=tr*np.maximum(p,0.2/n)
        bounds=[(max(-p[i],-rad[i]), rad[i]) for i in range(n)]+[(None,None)]
        res=linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=[0],bounds=bounds,method='highs')
        if res.status!=0: tr*=0.5; continue
        pn=np.maximum(p+res.x[:n],0); pn/=pn.sum()
        new=n*q_of(pn).max()
        if new<cur: p=pn; tr=min(tr*1.3,1.0)
        else: tr*=0.5
        if new<best[0]: best=(new,pn.copy())
        if tr<1e-7: break
    return best
def upsample(p):
    n=len(p); x=(np.arange(2*n)+0.5)/(2*n); xo=(np.arange(n)+0.5)/n
    g=np.interp(x,xo,p*n); g=np.maximum(g,1e-12); return g/g.sum()
if __name__=="__main__":
    p=np.load(D+"mu1_p160.npy")
    for n in [320,640]:
        p=upsample(p); t0=time.time()
        b=slp(n,p,iters=300)
        p=b[1]
        print(n,b[0],time.time()-t0,flush=True)
        np.save(D+f'mu1_p{n}.npy',p)
    # profile
    n=len(p); q=q_of(p)*n
    T=np.arange(-(n-1),2*(n-1)+1)/n
    for lo,hi in [(-1,0),(0,1),(1,2)]:
        m=(T>=lo)&(T<hi)
        print('region',lo,hi,'max',q[m].max(),'min',q[m].min())
    print('g near 0:',p[:8]*n)
    print('g near 1:',p[-8:]*n)
    print('g mid:',p[n//2-2:n//2+2]*n)
    # max of g*g*g (T constraint)
    pp=np.convolve(np.convolve(p,p),p)*n
    print('max g*g*g',pp.max(),' /3 =',pp.max()/3)
    