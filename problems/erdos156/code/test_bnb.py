import numpy as np, bnb
rng=np.random.default_rng(0)
worst=1e9
for n in [2,3]:
  for trial in range(3000):
    h=rng.uniform(0.2,0.9); lam=rng.uniform(0.5,1)
    P=bnb.Prob(n,h,lam)
    lo=rng.uniform(-1,0.8,size=(n,2)); w=rng.uniform(0,0.3,size=(n,2))
    box=np.stack([lo,lo+w],axis=-1)
    w_=rng.integers(0,3); m=[n+1,n+1,n][w_]
    v=rng.normal(size=m)+1j*rng.normal(size=m)
    ub=P.bound(w_,v,box)
    for s in range(20):
        c=rng.uniform(box[:,0,0],box[:,0,1])+1j*rng.uniform(box[:,1,0],box[:,1,1])
        T=P.mats(c)[w_]
        val=np.real(np.conj(v)@T@v)
        worst=min(worst,ub-val)
print('min(ub - actual) over tests (must be >=0):',worst)
