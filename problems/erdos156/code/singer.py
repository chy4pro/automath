"""Singer sets mod m=q^2+q+1 (q prime), experiments:
 (E1) lift S subset [0,m) to Z: which x in [lo,hi] are blocked?  maximal in which intervals?
 (E2) minimal subsets A of S (greedy cover) with A+A-A = Z_m  (A is Sidon mod m), size vs m^{1/3}
 (E3) arc test: can a unit multiple tA+u lie in an arc of length <= (m-1)/3 (=> lifted maximal Sidon set of an interval)?
"""
import numpy as np, sys, itertools
def is_prime(p): return p>1 and all(p%d for d in range(2,int(p**.5)+1))
def polymulmod(a,b,f,q):
    # a,b: lists len3 (coeffs of 1,x,x^2); f monic cubic x^3 + f2 x^2 + f1 x + f0 as [f0,f1,f2]
    r=[0]*5
    for i in range(3):
        for j in range(3): r[i+j]=(r[i+j]+a[i]*b[j])%q
    for d in (4,3):
        c=r[d]
        if c:
            r[d]=0
            for i in range(3): r[d-3+i]=(r[d-3+i]-c*f[i])%q
    return r[:3]
def singer(q):
    m=q*q+q+1
    # find irreducible cubic: no roots in F_q
    for f0 in range(1,q):
        for f1 in range(q):
            for f2 in range(q):
                if all((x**3+f2*x*x+f1*x+f0)%q for x in range(q)):
                    f=[f0,f1,f2]
                    # find primitive element: order q^3-1
                    order=q**3-1
                    fac=[p for p in range(2,order+1) if order%p==0 and is_prime(p)] if order<10**6 else None
                    for g0 in itertools.product(range(q),repeat=3):
                        g=list(g0)
                        if g==[0,0,0]: continue
                        def pw(e):
                            r=[1,0,0]; b=g[:]
                            while e:
                                if e&1: r=polymulmod(r,b,f,q)
                                b=polymulmod(b,b,f,q); e>>=1
                            return r
                        if all(pw(order//p)!=[1,0,0] for p in fac):
                            S=set(); e=[1,0,0]
                            for i in range(order):
                                if e[2]==0: S.add(i%m)
                                e=polymulmod(e,g,f,q)
                            return m,sorted(S)
    return None
def is_sidon_mod(A,m):
    s=set()
    for i,a in enumerate(A):
        for b in A[i:]:
            t=(a+b)%m
            if t in s: return False
            s.add(t)
    return True
def cover_mod(A,m):
    A=np.array(A); cov=np.zeros(m,bool)
    for a in A:
        for b in A:
            cov[(a+b-A)%m]=True
    return cov
def lift_blocked(A,lo,hi):
    # integer blocked set within [lo,hi] for integer set A
    A=sorted(A); S=set(); Sd=set()
    for i,a in enumerate(A):
        for b in A[i:]:
            S.add(a+b)
            if a!=b: Sd.add(a+b)
    bl=set(A)
    for s in S:
        for a in A: bl.add(s-a)
    for s in Sd:
        if s%2==0: bl.add(s//2)
    return [x for x in range(lo,hi+1) if x not in bl]
def greedy_subset(S,m,rng=None):
    # greedy: choose subset A of S maximizing coverage of A+A-A mod m
    S=list(S); A=[]
    cov=np.zeros(m,bool)
    Sarr=np.array(S)
    while not cov.all():
        best=-1;bs=None
        cand=S if rng is None else list(rng.permutation(S))
        for s in cand:
            if s in A: continue
            B=A+[s]; Barr=np.array(B)
            new=np.zeros(m,bool)
            # new triples involving s: s+b-a, b+c-s, b+s-s(=b), 2s-a
            for b in B:
                new[(s+b-Barr)%m]=True
                new[(b+Barr-s)%m]=True
            gain=int((new&~cov).sum())
            if gain>best: best=gain;bs=s
        A.append(bs)
        cov=cover_mod(A,m)
    return sorted(A)
if __name__=='__main__':
    for q in [int(v) for v in sys.argv[1].split(',')]:
        m,S=singer(q)
        assert len(S)==q+1 and is_sidon_mod(S,m)
        D=set((a-b)%m for a in S for b in S if a!=b); assert len(D)==m-1
        # E1: lift S to [0,m): unblocked integers in [0,m-1]
        un=lift_blocked(S,0,m-1)
        # longest interval containing S where S is maximal
        print(f'q={q} m={m} |S|={len(S)}  lifted S: #unblocked in [0,m-1] = {len(un)}  (first few {un[:6]})')
        A=greedy_subset(S,m)
        k=len(A)
        print(f'   greedy subset A of S with A+A-A=Z_m: |A|={k}  k^3/m={k**3/m:.2f}  k/m^(1/3)={k/m**(1/3):.3f}')
        # E3: arc test over multipliers t (units) : minimal arc length containing tA
        best=(m,None)
        for t in range(1,m):
            if np.gcd(t,m)!=1: continue
            pts=np.sort((t*np.array(A))%m)
            gaps=np.diff(np.concatenate([pts,[pts[0]+m]]))
            arc=m-gaps.max()   # length of smallest arc containing all points
            if arc<best[0]: best=(arc,t)
        print(f'   best multiplier t={best[1]}: tA fits in arc of length {best[0]}  (need <= (m-1)/3 = {(m-1)/3:.1f}); ratio arc/m={best[0]/m:.3f}')
