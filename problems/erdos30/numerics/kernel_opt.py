"""Numerical search (not a proof): minimise a(h)*b(h) over nonnegative piecewise-constant kernels h on [0,S].
a = ||h||^2/(∫h)^2 ; b = 1/E_min - L, E_min = min energy of unit-mass signed measures on a grid of [0,L].
Compared against the ramp h = 2(1-t) evaluated with the SAME discretisation."""
import numpy as np, sys
from scipy.optimize import minimize
def ab(hc, S=1.0, L=4.0, sub=3):
    m=len(hc); n_per=int(m*sub/S); dx=1.0/n_per
    h=np.repeat(np.maximum(hc,0.0), sub); mass=h.sum()*dx
    if mass<=0: return 9.0,0,0
    h=h/mass
    fc=np.correlate(h,h,mode='full')*dx; mm=len(h)-1
    n=int(L*n_per)+1
    idx=np.abs(np.arange(n)[:,None]-np.arange(n)[None,:])
    F=np.where(idx<=mm, fc[mm+np.minimum(idx,mm)], 0.0)
    cap=np.ones(n)@np.linalg.solve(F+1e-11*np.eye(n),np.ones(n))
    a=fc[mm]; b=cap-L
    return a*b, a, b
m=int(sys.argv[1]) if len(sys.argv)>1 else 24
S=float(sys.argv[2]) if len(sys.argv)>2 else 1.0
t=(np.arange(m)+0.5)/m
ramp=1-t
v0,a0,b0=ab(ramp,S)
print(f"ramp (same discretisation): ab={v0:.6f} sqrt={np.sqrt(v0):.6f}  a={a0:.4f} b={b0:.4f}   exact 8/9={8/9:.6f}")
best=(v0,ramp)
rng=np.random.default_rng(1)
for start in range(4):
    x0=ramp*(1+0.25*rng.standard_normal(m)) if start else ramp.copy()
    x0=np.maximum(x0,0.0)
    res=minimize(lambda x: ab(x,S)[0], x0, method='L-BFGS-B', bounds=[(0,None)]*m, options={"maxiter":40,'ftol':1e-11})
    if res.fun<best[0]: best=(res.fun,res.x.copy())
    print(f" start {start}: ab={res.fun:.6f} sqrt={np.sqrt(res.fun):.6f}")
v,x=best; x=x/x.max()
print(f"best: ab={v:.6f} sqrt={np.sqrt(v):.6f}  gain vs ramp (same grid) = {np.sqrt(v0)-np.sqrt(v):.6f}")
print("best h (normalised to max 1):", np.round(x,3).tolist())
