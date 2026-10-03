import numpy as np, random, time, sys
from math import gcd
random.seed(1)
# ---------- B3 checks ----------
def isB3_int(A):
    A=sorted(A); s=set()
    for i in range(len(A)):
        for j in range(i,len(A)):
            for l in range(j,len(A)):
                v=A[i]+A[j]+A[l]
                if v in s: return False
                s.add(v)
    return True
def isB3_mod(A,M):
    A=sorted(A); s=set()
    for i in range(len(A)):
        for j in range(i,len(A)):
            for l in range(j,len(A)):
                v=(A[i]+A[j]+A[l])%M
                if v in s: return False
                s.add(v)
    return True
# ---------- Bose-Chowla for prime q ----------
def bose_chowla(q):
    # find monic irreducible cubic x^3+a2 x^2+a1 x+a0 over F_q and primitive element
    def mul(u,v,c):
        a0,a1,a2=c
        prod=[0]*5
        for i in range(3):
            for j in range(3):
                prod[i+j]=(prod[i+j]+u[i]*v[j])%q
        for d in (4,3):
            co=prod[d]
            if co:
                prod[d]=0
                # x^d = x^{d-3} * x^3 = x^{d-3} * (-(a0+a1x+a2x^2))
                prod[d-3]=(prod[d-3]-co*a0)%q
                prod[d-2]=(prod[d-2]-co*a1)%q
                prod[d-1]=(prod[d-1]-co*a2)%q
        return tuple(prod[:3])
    M=q**3-1
    for a0 in range(1,q):
        for a1 in range(q):
            for a2 in range(q):
                if any((x**3+a2*x*x+a1*x+a0)%q==0 for x in range(q)): continue
                c=(a0,a1,a2)
                for th in [(0,1,0),(1,1,0),(2,1,0),(0,1,1),(1,0,1)]:
                    logs={}; e=(1,0,0)
                    ok=True
                    for i in range(M):
                        if e in logs: ok=False;break
                        logs[e]=i; e=mul(e,th,c)
                    if not ok or e!=(1,0,0): continue
                    A=sorted(logs[((u+th[0])%q,th[1],th[2])] for u in range(q))
                    return A,M
    return None
def best_dilate(A,M,tries=None):
    best=None
    units=[u for u in range(1,M) if gcd(u,M)==1]
    if tries and len(units)>tries: units=random.sample(units,tries)
    for u in units:
        B=sorted((u*a)%M for a in A)
        # best rotation: largest cyclic gap
        gaps=[(B[(i+1)%len(B)]-B[i])%M for i in range(len(B))]
        i=max(range(len(B)),key=lambda j:gaps[j])
        start=B[(i+1)%len(B)]
        C=sorted((b-start)%M for b in B)
        span=C[-1]
        if best is None or span<best[0]: best=(span,C)
    return best
# ---------- greedy ----------
def greedy_B3(N, order=None):
    A=[]; P=0; T=0; Ab=0
    cand = range(N+1) if order is None else order
    for x in cand:
        newb=(P<<x)|(Ab<<(2*x))|(1<<(3*x))
        if newb & T: continue
        if newb.bit_count()!=P.bit_count()+Ab.bit_count()+1: continue
        # P must use pairs including x: we need P for the set A sorted? shifts assume x>all? No: sums are symmetric, fine.
        P=P|(Ab<<x)|(1<<(2*x)); T|=newb; Ab|=(1<<x); A.append(x)
    return sorted(A)
# ---------- diagnostics ----------
def diagnostics(A,label):
    A=sorted(A); a0=A[0]; A=[a-a0 for a in A]; N=A[-1]; k=len(A)
    f=np.zeros(N+1,dtype=np.int64); f[A]=1
    ff=np.convolve(f,f)
    r=np.convolve(ff,f[::-1])          # index n+N for n in [-N,2N]
    r3=np.convolve(ff,f)
    idx=np.arange(-N,2*N+1)
    fA=np.zeros(len(idx),dtype=np.int64); fA[np.array(A)+N]=1
    rp=r-(2*k-1)*fA
    assert rp.min()>=0 and rp.max()<=2 and rp[fA==1].max()==0, 'r prime check failed'
    E3=int((r3*r3).sum()); E3pred=6*k**3-9*k**2+4*k
    assert E3==E3pred,(E3,E3pred)
    # R4(t) = sum_d r(t+d)
    R4=np.convolve(r, f[::-1])  # index t + 2N ... compute directly instead
    # direct: R4 = ff conv ff~
    R4=np.convolve(ff,ff[::-1]); c0=len(ff)-1
    AmA=set(a-b for a in A for b in A if a!=b)
    viol=0
    for t in range(-2*N,2*N+1):
        if t==0: continue
        bound=2*k+(2*k-1)*(1 if t in AmA else 0)
        if R4[t+c0]>bound: viol+=1
    assert viol==0
    assert R4[c0]==2*k*k-k
    inside=(idx>=0)&(idx<=N)
    cover=((rp>0)|(fA==1))[inside].mean()
    nD2=int((rp==2).sum()); nD1=int((rp==1).sum())
    ratio=k/(N+1)**(1/3)
    # deficiency in record argument over window |t|<=H, H=N//8 (excluding t in A-A)
    H=max(1,N//8)
    rsum=0; cnt=0
    for t in range(-H,H+1):
        if t==0 or t in AmA: continue
        rsum+=R4[t+c0]; cnt+=1
    sat=rsum/cnt/(2*k) if cnt else float('nan')
    print(f'{label:28s} k={k:3d} N={N+1:7d} k/N^(1/3)={ratio:.4f} |D2|={nD2} |D1|={nD1} '
          f'D-cover[0,N]={cover:.3f} avg R4(t)/2k (|t|<=N/8)={sat:.3f} checks:OK',flush=True)
    return ratio
if __name__=='__main__':
    t0=time.time()
    # exhaustive optima from search
    for A in [[0,1,4],[0,1,7,11],[0,1,15,18,23],[0,2,11,26,42,45],[0,1,7,50,59,78,82]]:
        assert isB3_int(A); diagnostics(A,'exhaustive optimum')
    for q in [3,5,7,11,13,17,19,23]:
        A,M=bose_chowla(q)
        assert isB3_mod(A,M)
        span,C=best_dilate(A,M,tries=400)
        assert isB3_int(C)
        diagnostics(C,f'Bose-Chowla q={q} (M={M})')
    for N in [1000,10000,100000]:
        A=greedy_B3(N); assert isB3_int(A); diagnostics(A,f'greedy [0,{N}]')
    for N in [1000,10000]:
        best=None
        for trial in range(20):
            order=list(range(N+1)); random.shuffle(order)
            A=greedy_B3(N,order)
            if best is None or len(A)>len(best): best=A
        assert isB3_int(best); diagnostics(best,f'random greedy best/20 [0,{N}]')
    print('time',time.time()-t0)
