import numpy as np, sys
from scipy.optimize import minimize, brentq
from scipy.linalg import toeplitz, eigvalsh
def ellf(t):
    if t==0: return 1.0+0j
    return (1-np.exp(-2j*np.pi*t))/(2j*np.pi*t)
def herm_toep(seq):
    col=np.array(seq); return toeplitz(col,np.conj(col))
def mins(c,lam,n,h,loc=True):
    seq=[1+0j]+list(c)
    out=[eigvalsh(herm_toep(seq))[0]]
    rho=[1-lam]+[c[j-1]*abs(c[j-1])**2-lam*ellf(j*h) for j in range(1,n+1)]
    out.append(eigvalsh(herm_toep(rho))[0])
    if loc:
        full={0:1+0j}
        for j in range(1,n+1): full[j]=c[j-1]; full[-j]=np.conj(c[j-1])
        e=np.exp(-1j*np.pi*h)
        locs=[0.5*e*full[j-1]+0.5*np.conj(e)*full[j+1]-np.cos(np.pi*h)*full[j] for j in range(0,n)]
        out.append(eigvalsh(herm_toep(locs))[0])
    return np.array(out)
def from_measure(xs,ws,n,h):
    return np.array([np.sum(ws*np.exp(-2j*np.pi*j*h*xs)) for j in range(1,n+1)])
def lam_for(c,n,h):
    f=lambda l: mins(c,l,n,h,loc=False)[1]
    if f(0)<0: return 0
    if f(1)>=0: return 1
    return brentq(f,0,1)
def relax(n,h,seeds,rng):
    best=0;bestc=None
    for s in range(seeds):
        k=rng.integers(1,8); xs0=rng.uniform(0,1,k); ws0=rng.dirichlet(np.ones(k))
        if s%3==0: xs0=np.concatenate([[0.5],rng.uniform(0,1,k)]); ws0=np.concatenate([[rng.uniform(0.3,0.6)],rng.dirichlet(np.ones(k))]); ws0/=ws0.sum()
        c0=from_measure(xs0,ws0,n,h); l0=lam_for(c0,n,h)*0.999
        z0=np.concatenate([c0.real,c0.imag,[l0]])
        un=lambda z:(z[:n]+1j*z[n:2*n],z[2*n])
        cons={'type':'ineq','fun':lambda z: mins(*un(z),n,h)}
        r=minimize(lambda z:-z[2*n],z0,constraints=[cons],method='SLSQP',options={'maxiter':300,'ftol':1e-10})
        c1,l1=un(r.x)
        if mins(c1,l1,n,h).min()>-1e-8 and l1>best: best=l1;bestc=c1
    return best,bestc
if __name__=='__main__':
    rng=np.random.default_rng(1)
    for n in [2,3,4]:
        for h in [0.2,0.25,0.3,1/3,0.4,0.5,0.6]:
            b,_=relax(n,h,25,rng)
            print(n,round(h,3),round(b,4),flush=True)
