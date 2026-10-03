import numpy as np, lam_opt as L, sys
M=int(sys.argv[1]); rng=np.random.default_rng(int(sys.argv[2]))
best=0
res=[]
for trial in range(int(sys.argv[3])):
    kind=trial%4
    x=rng.normal(size=M+1)*0.3
    na=rng.integers(1,5)
    pos=rng.integers(0,M+1,size=na)
    if kind==1: pos=np.round(np.linspace(0,M,na+2)[1:-1]).astype(int)
    if kind==2: pos=np.array([0,M//2,M]) if na>1 else np.array([M//2])
    for q in pos: x[q]+=rng.uniform(2,5)
    if kind==3: x=rng.normal(size=M+1)*2.0
    lam,p=L._run(M,x,4000,50.0)
    res.append((lam,trial,kind,na))
    if lam>best:
        best=lam; np.save(f'best2_{M}_{sys.argv[2]}.npy',p)
res.sort(reverse=True)
for r in res[:8]: print(r)
