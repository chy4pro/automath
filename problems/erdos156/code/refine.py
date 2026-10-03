import numpy as np, lam_opt as L, sys
p0=np.load('best_p_120.npy'); M0=len(p0)-1
for M in [int(v) for v in sys.argv[1].split(',')]:
    # interpolate: keep central atom as atom, interpolate density part
    xs0=np.arange(M0+1)/M0; xs=np.arange(M+1)/M
    c0=M0//2; w=p0[c0]
    dens=p0.copy(); dens[c0]=(p0[c0-1]+p0[c0+1])/2
    d=np.interp(xs,xs0,dens)*(M0+1)/(M+1)
    d[M//2]+=w
    d/=d.sum()
    x=np.log(np.maximum(d,1e-12))
    lam,p=L._run(M,x,6000,200.0)
    np.save(f'best_p_{M}.npy',p)
    print(M,'lambda_M=%.6f'%lam,'atom weight=%.5f'%p[M//2],'mass outside target=%.5f'%(1-L.nu_of(p)[M:2*M+1].sum()),flush=True)
