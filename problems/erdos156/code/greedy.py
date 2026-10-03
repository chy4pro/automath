"""Greedy / random constructions of maximal Sidon sets in [1,N].
State: A; U = set of x in [1,N] not in A and not blocked (i.e. A+{x} Sidon).
Adding y requires y in U. Process ends when U is empty -> A maximal.
"""
import numpy as np, sys, time
from numpy.fft import rfft, irfft
def conv(a,b):
    n=len(a)+len(b)-1; L=1<<(n-1).bit_length()
    return np.rint(irfft(rfft(a,L)*rfft(b,L),L)[:n]).astype(np.int64)
def blocked(A,N):
    ind=np.zeros(N+1,dtype=np.float64); ind[A]=1
    s=conv(ind,ind)   # ordered pair counts, index a+b in 0..2N
    # sums b<=c present iff s>0 ; distinct-pair sums: s - [even and half in A] >0
    S=(s>0).astype(np.float64)
    dbl=np.zeros(2*N+1); dbl[2*np.array(A)]=1
    Sd=((s-dbl)>0)
    # S - A : x = t - a ; corr: x index = t - a
    rev=ind[::-1].copy()  # rev[j]=ind[N-j]
    c=conv(S,rev)  # index t + (N-a) -> x = idx - N
    bl=np.zeros(N+1,dtype=bool)
    xs=np.arange(N+1)
    bl|= c[N:2*N+1]>0
    bl[A]=True
    ev=np.nonzero(Sd)[0]; ev=ev[ev%2==0]//2; ev=ev[(ev>=1)&(ev<=N)]
    bl[ev]=True
    bl[0]=True
    return bl
def scores(A,U,N):
    # approximate number of currently-unblocked points that y would block, for all y
    ind=np.zeros(N+1); ind[A]=1
    u=U.astype(np.float64)
    s=conv(ind,ind); S=(s>0).astype(np.float64)
    # D = A - A nonzero: counts via corr
    d=conv(ind,ind[::-1].copy())  # index (a-b)+N
    D=(d>0).astype(np.float64); D[N]=0
    # (i) sum_d U(y+d): corr of U with D  -> score1[y] = sum_d D[d+N] U[y+d]
    c1=conv(u[::-1].copy(),D)  # index (N - (y+d)) + (d+N) = 2N - y
    sc=c1[2*N-np.arange(N+1)]
    # (ii) sum_s S[s] U(s-y): conv(S, U reversed?) U(s-y): index s - y = x -> y = s - x ; conv(S, u[::-1]) idx s + N - x = N + y
    c2=conv(S,u[::-1].copy()); sc=sc+c2[N+np.arange(N+1)]
    return sc
def run(N,mode,seed=0,topk=30):
    rng=np.random.default_rng(seed)
    A=[]
    U=np.ones(N+1,dtype=bool); U[0]=False
    while U.any():
        cand=np.nonzero(U)[0]
        if mode=='random':
            y=int(rng.choice(cand))
        else:
            if len(A)<2:
                y=int(cand[len(cand)//2]) if len(A)==0 else int(rng.choice(cand))
            else:
                sc=scores(A,U,N)[cand]
                order=np.argsort(-sc)[:topk]
                best=-1;y=None
                for j in order:
                    yy=int(cand[j]); nb=blocked(A+[yy],N)
                    val=int((U & nb).sum())
                    if val>best: best=val;y=yy
        A.append(y)
        U=~blocked(A,N); U[0]=False
    return sorted(A)
def check(A,N):
    A=sorted(A); s=set()
    for i,a in enumerate(A):
        for b in A[i:]:
            if a+b in s: return False
            s.add(a+b)
    return blocked(A,N)[1:].all()
if __name__=='__main__':
    mode=sys.argv[1]
    for N in [int(v) for v in sys.argv[2].split(',')]:
        t0=time.time(); A=run(N,mode,seed=1)
        k=len(A); ok=check(A,N)
        print(mode,N,k,'ok' if ok else 'BAD','k^3/N=%.3f'%(k**3/N),'k^3/(N lnN)=%.3f'%(k**3/(N*np.log(N))),'t=%.1f'%(time.time()-t0),flush=True)
