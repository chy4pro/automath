#!/usr/bin/env python3
"""VER #377-D2 checks 2,3,4 (stdlib + numpy). Usage: ver377d2.py"""
import math, random, statistics
import numpy as np

# ---- check 2: exact v_2(C(2^(h+1),2^h)) = 1, h=1..300 (big-int, plus Kummer)
def v2(x): return (x & -x).bit_length()-1
bad=[]
def leg2(n):  # Legendre: v_2(n!) = sum floor(n/2^i), exact integers
    t=0;q=n>>1
    while q: t+=q;q>>=1
    return t
for h in range(1,301):
    v=leg2(2**(h+1))-2*leg2(2**h)
    kummer=2*bin(2**h).count('1')-bin(2**(h+1)).count('1')  # s(a)+s(b)-s(a+b), base 2
    if v!=1 or kummer!=1: bad.append(h)
for h in range(1,12):  # cross-check vs literal binomial
    assert v2(math.comb(2**(h+1),2**h))==1
print("CHECK2 (certificate, exact): h=1..300 v_2(C(2^(h+1),2^h))=1 failures:",bad)

# ---- check 3: A(alpha)
def w(t): return 2.0**(-math.floor(1/t))
def A_closed(s,alpha):
    return 2.0**(-s)*math.log((s+1)*alpha)+sum(2.0**(-r)*math.log1p(1/r) for r in range(s+1,200))
def A_num(alpha):
    # sum over bands [1/(r+1),1/r] intersect (0,alpha]; Gauss-Legendre per band (integrand w/t is smooth in band: 2^-r/t)
    x,wt=np.polynomial.legendre.leggauss(40)
    tot=0.0; s=math.floor(1/alpha+1e-12)
    for r in range(s,120):
        a=1/(r+1); b=min(1/r,alpha)
        if a>=b: continue
        t=(b-a)/2*x+(a+b)/2
        # w(t)=2^-r on open band (a,1/r)
        tot+=(b-a)/2*np.sum(wt*2.0**(-r)/t)
    return tot
print("CHECK3 (numerics): alpha, s, A_closed, A_quad, diff, bound 2^(1-s)/s, ok")
for s in (2,3,4,5):
    al=1/s; c=A_closed(s,al); q=A_num(al); b=2.0**(1-s)/s
    print(f" 1/{s} {s} {c:.15f} {q:.15f} {abs(c-q):.2e} {b:.15f} {c<=b}")
# independent crude check: adaptive-free midpoint in log t
for s in (2,3,4,5):
    al=1/s; u=np.linspace(-60,math.log(al),4_000_001); um=(u[1:]+u[:-1])/2
    t=np.exp(um); ww=2.0**(-np.floor(1/t)); val=np.sum(ww)*(u[1]-u[0])
    print(f" midpoint-in-log-t 1/{s}: {val:.9f}")

# ---- check 4
N=10**6
spf=np.zeros(N+1,dtype=np.int64)
primes=[]
for i in range(2,N+1):
    if spf[i]==0:
        primes.append(i); spf[i::i][spf[i::i]==0]=i
primes=np.array(primes)
def vp_central(n,p):
    # carries when adding n+n in base p
    c=0;carry=0
    while n or carry:
        d=n%p; t=2*d+carry
        carry=1 if t>=p else 0
        c+=carry; n//=p
    return c
def Nalpha(n,alpha):
    L=int(math.floor(n**alpha+1e-9))
    # exact floor of n**alpha for safety
    while (L+1)**round(1/alpha)<=n: L+=1
    while L**round(1/alpha)>n: L-=1
    vb={int(p):vp_central(n,int(p)) for p in primes[primes<=L]}
    bad=0
    for m in range(1,L+1):
        x=m; ok=True
        while x>1:
            p=int(spf[x]);e=0
            while x%p==0: x//=p;e+=1
            if e>vb[p]: ok=False;break
        if not ok: bad+=1
    return bad/L, L
mid={2:(0.160401041573+0.160401748642)/2,3:(0.059862571395+0.059862608229)/2}
SEED=377202610
rng=random.Random(SEED)
print("CHECK4 (numerics) seed",SEED,"n uniform integer in [1e9,1e10], 200 samples")
ns=[rng.randint(10**9,10**10) for _ in range(200)]
for s in (2,3):
    al=1/s; vals=[Nalpha(n,al)[0] for n in ns]
    q=np.percentile(vals,[25,50,75])
    fr=sum(abs(v-mid[s])<=0.02 for v in vals)/len(vals)
    print(f" alpha=1/{s} midpoint={mid[s]:.6f} mean={np.mean(vals):.5f} median={q[1]:.5f} Q1={q[0]:.5f} Q3={q[2]:.5f} min={min(vals):.5f} max={max(vals):.5f} frac_within_0.02={fr:.3f}")
    print(f" N_alpha(2^h), 1/4 floor-bound: ", end="")
    for h in range(30,34):
        v,L=Nalpha(2**h,al); print(f"h={h}: {v:.5f} (L={L}, lb={(L//4)/L:.5f})",end="; ")
    print()
