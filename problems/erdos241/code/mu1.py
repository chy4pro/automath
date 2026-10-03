import numpy as np, sys, time
from scipy.optimize import linprog
np.random.seed(0)
# minimize n*max(p*p*ptilde) over simplex (upper bound for mu1 = inf ||g*g*g~||_inf)
def q_of(p):
    pp = np.convolve(p,p)
    return np.convolve(pp, p[::-1])   # index t+(n-1), t=i+j-l in [-(n-1), 2(n-1)]
def jac(p):
    n=len(p)
    pp = np.convolve(p,p)            # (p*p)_s, s in [0,2n-2]
    ac = np.correlate(p,p,'full')     # (p*ptilde)_d = sum_j p_j p_{j-d}?  index d+(n-1)
    # q_t = sum_{i+j-l=t} p_i p_j p_l
    # dq_t/dp_m = 2 * sum_{j-l=t-m} p_j p_l + sum_{i+j=t+m} p_i p_j
    T = np.arange(-(n-1), 2*(n-1)+1)
    M = np.arange(n)
    J = np.zeros((len(T), n))
    # autocorr A_d = sum_j p_j p_{j-d}
    A = np.correlate(p,p,'full')[::-1]  # check below
    for k,t in enumerate(T):
        d = t - M
        s = t + M
        v = np.zeros(n)
        ok = (d>=-(n-1))&(d<=n-1)
        v[ok] += 2*Acorr(p)[d[ok]+(n-1)]
        ok2=(s>=0)&(s<=2*n-2)
        v[ok2] += pp[s[ok2]]
        J[k]=v
    return J
_cache={}
def Acorr(p):
    key=id(p)
    n=len(p)
    # A[d+(n-1)] = sum_j p_j p_{j-d}
    a = np.array([np.dot(p[max(0,d):n], p[max(0,-d)+0:n-max(0,d)] if d>=0 else p[0:n+d]) if True else 0 for d in range(-(n-1),n)])
    return a
def Acorr2(p):
    n=len(p)
    out=np.zeros(2*n-1)
    for d in range(-(n-1),n):
        if d>=0: out[d+n-1]=np.dot(p[d:],p[:n-d])
        else: out[d+n-1]=np.dot(p[:n+d],p[-d:])
    return out
def jac_fast(p):
    n=len(p)
    pp=np.convolve(p,p)
    A=Acorr2(p)
    T=np.arange(-(n-1),2*(n-1)+1)[:,None]; M=np.arange(n)[None,:]
    d=T-M; s=T+M
    J=np.where((d>=-(n-1))&(d<=n-1), 2*A[np.clip(d+n-1,0,2*n-2)],0.0)
    J+=np.where((s>=0)&(s<=2*n-2), pp[np.clip(s,0,2*n-2)],0.0)
    return J
def check():
    p=np.random.rand(7); p/=p.sum()
    J=jac_fast(p); eps=1e-7
    for m in range(7):
        e=np.zeros(7); e[m]=eps
        num=(q_of(p+e)-q_of(p-e))/(2*eps)
        assert np.allclose(num,J[:,m],atol=1e-6), (m,num,J[:,m])
    print('jac ok')
check()
def slp(n, p0=None, iters=200, tr=0.3):
    p = np.ones(n)/n if p0 is None else p0.copy()
    best=None
    for it in range(iters):
        q=q_of(p); J=jac_fast(p)
        cur=n*q.max()
        if best is None or cur<best[0]: best=(cur,p.copy())
        # variables delta (n), t
        nv=n+1
        c=np.zeros(nv); c[-1]=1
        A_ub=np.hstack([n*J, -np.ones((J.shape[0],1))]); b_ub=-n*q
        A_eq=np.zeros((1,nv)); A_eq[0,:n]=1; b_eq=[0]
        rad=tr*np.maximum(p,1.0/n)
        bounds=[(max(-p[i],-rad[i]), rad[i]) for i in range(n)]+[(None,None)]
        res=linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds,method='highs')
        if res.status!=0: tr*=0.5; continue
        dl=res.x[:n]
        pn=np.maximum(p+dl,0); pn/=pn.sum()
        new=n*q_of(pn).max()
        pred=res.x[-1]
        if new<cur: p=pn; tr=min(tr*1.2,1.0)
        else: tr*=0.5
        if tr<1e-6: break
    return best
if __name__=='__main__':
    for n in [20,40,80,160]:
        t0=time.time()
        b=slp(n,iters=400)
        print(n, b[0], time.time()-t0, flush=True)
        np.save(f'./mu1_p{n}.npy', b[1])
