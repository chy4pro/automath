# Zaremba E1 campaign probe (2026-09-26): empirical operator norm of the Lemma-14 averaging operator
# T f(x) = (1/N) sum_{j<=N} f(g_j x),  g_j x = 1/(x+2j) - 2j  on P^1(F_p)  (Shkredov 2603.14116 Lemma 14; MMS 2212.14646 eq.(15))
# restricted to mean-zero functions. Proven: ||T_0|| <= N^{-kappa}, kappa >= 2^-1656 (Shkredov appendix).
# Observed (p=100003 and p=1000003, N=2..64): ||T_0|| = 2 sqrt(N-1)/N to 3 decimals = Akemann-Ostrand free-group value,
# i.e. empirical kappa -> 1/2. Usage: python zaremba_kappa_numerics.py <prime> <Nmax>
import numpy as np, sys, math
def build(p,N):
    invtab=np.zeros(p,dtype=np.int64)
    # inverse table via powers of primitive root is overkill; use pow vectorized by modular exponent
    a=np.arange(1,p,dtype=object)
    invtab[1:]=np.array([pow(int(v),-1,p) for v in range(1,p)],dtype=np.int64)
    P=[]
    for j in range(1,N+1):
        y=np.empty(p+1,dtype=np.int64)
        s=(np.arange(p)+2*j)%p
        z=np.where(s==0,-1,(invtab[s]-2*j)%p)
        y[:p]=np.where(z<0,p,z)          # x=-2j -> infinity
        y[p]=(-2*j)%p                     # infinity -> -2j
        P.append(y)
    return P
def norm(P,iters=300,seed=0):
    n=len(P[0]); N=len(P); rng=np.random.default_rng(seed)
    Pinv=[np.argsort(y) for y in P]
    f=rng.standard_normal(n); f-=f.mean()
    lam=0
    for _ in range(iters):
        g=sum(f[y] for y in P)/N        # (T f)(x)=f(g x)
        h=sum(g[yi] for yi in Pinv)/N   # T^* g
        h-=h.mean(); nh=np.linalg.norm(h); lam=nh/np.linalg.norm(f); f=h/nh
    return math.sqrt(lam)
p=int(sys.argv[1])
P=build(p,int(sys.argv[2]) if len(sys.argv)>2 else 64)
for N in [2,4,8,16,32,64]:
    if N>len(P): break
    s=norm(P[:N]); print(p,N,round(s,4),'kappa_emp',round(-math.log(s)/math.log(N),3) if N>1 else None, 'ramanujan~', round(math.sqrt(2*N-1)/N,4),flush=True)
