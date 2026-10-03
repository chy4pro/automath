import numpy as np, sys
from scipy.optimize import minimize
from scipy.linalg import toeplitz, eigvalsh
P=3.0  # circle length
def ell(j):
    if j==0: return 1.0+0j
    t=j/P
    return (1-np.exp(-2j*np.pi*t))/(2j*np.pi*t)
def herm_toep(seq):  # seq[0..n], T[a,b]=seq[a-b], seq[-j]=conj
    n=len(seq)-1
    col=np.array(seq); row=np.conj(col)
    return toeplitz(col,row)
def mins(c,lam,n):
    seq=[1+0j]+list(c)
    T1=herm_toep(seq)
    rho=[1-lam]+[c[j-1]*abs(c[j-1])**2-lam*ell(j) for j in range(1,n+1)]
    T2=herm_toep(rho)
    # localizing g(x)=0.5 e^{-i pi/3} c_{j-1} + 0.5 e^{i pi/3} c_{j+1} - 0.5 c_j, j=0..n-1
    full={0:1+0j}
    for j in range(1,n+1): full[j]=c[j-1]; full[-j]=np.conj(c[j-1])
    loc=[0.5*np.exp(-1j*np.pi/3)*full[j-1]+0.5*np.exp(1j*np.pi/3)*full[j+1]-0.5*full[j] for j in range(0,n)]
    T3=herm_toep(loc)
    return eigvalsh(T1)[0], eigvalsh(T2)[0], eigvalsh(T3)[0]
def from_measure(xs,ws,n):
    return np.array([np.sum(ws*np.exp(-2j*np.pi*j*xs/P)) for j in range(1,n+1)])
if __name__=='__main__':
    n=int(sys.argv[1]); seeds=int(sys.argv[2])
    # check feasibility of numerical optimum
    p=np.load('best_p_120.npy'); M=len(p)-1; xs=np.arange(M+1)/M
    c=from_measure(xs,p,n)
    for lam in [0.70,0.715,0.72,0.75,0.8]:
        print('opt-measure lam',lam,mins(c,lam,n))
    rng=np.random.default_rng(0)
    best=0
    for s in range(seeds):
        # random start: random discrete measure on [0,1]
        k=rng.integers(1,6); xs0=rng.uniform(0,1,k); ws0=rng.dirichlet(np.ones(k))
        c0=from_measure(xs0,ws0,n)
        z0=np.concatenate([c0.real,c0.imag,[0.5]])
        def unpack(z): return z[:n]+1j*z[n:2*n], z[2*n]
        cons={'type':'ineq','fun':lambda z: np.array(mins(*unpack(z),n))}
        r=minimize(lambda z:-z[2*n],z0,constraints=[cons],method='SLSQP',options={'maxiter':500})
        c1,l1=unpack(r.x); m=mins(c1,l1,n)
        if min(m)>-1e-7 and l1>best: best=l1
    print('n',n,'relaxation max lambda (local search) approx',best)
