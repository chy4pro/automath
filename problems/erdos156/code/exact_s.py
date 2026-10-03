"""Exact s(N): minimum size of a maximal Sidon subset of {1..N}. Exhaustive DFS with bitsets.
x (not in A) is blocked iff A+{x} is not Sidon iff
   x in (A+^A) - A   (A+^A = sums b+c, b<=c, incl. 2b)   or   2x = b+c with b != c in A.
"""
import sys, time
def blocked_mask(A,N):
    full=(1<<(N+1))-2  # bits 1..N
    S=0; Sd=0
    for i,a in enumerate(A):
        for b in A[i:]:
            S|=1<<(a+b)
            if b!=a: Sd|=1<<(a+b)
    bl=0
    for a in A:
        bl|=S>>a
        bl|=1<<a
    # halving
    x=1
    sd=Sd
    while sd:
        low=sd&-sd; s=low.bit_length()-1
        if s%2==0: bl|=1<<(s//2)
        sd^=low
    return bl&full
def B(k): return (k*(k-1)//2)*(k-2)+k*(k-1)+k*(k-1)//2+k
def search(N,k,first_only=True):
    full=(1<<(N+1))-2
    found=[]
    cnt=[0]
    def rec(A,S,start):
        i=len(A)
        if i==k:
            cnt[0]+=1
            bl=blocked_mask(A,N)
            if bl==full:
                found.append(tuple(A)); return first_only
            return False
        # counting prune
        if i>=2:
            bl=blocked_mask(A,N)
            un=N-bin(bl).count('1')
            if un>B(k)-B(i): return False
        r=k-i
        for y in range(start,N-r+2):
            # Sidon check: new sums y+a for a in A and 2y
            new=0
            for a in A: new|=1<<(y+a)
            new|=1<<(2*y)
            if S&new: continue
            A.append(y)
            if rec(A,S|new,y+1): return True
            A.pop()
        return False
    rec([],0,1)
    return found,cnt[0]
if __name__=='__main__':
    N0,N1=int(sys.argv[1]),int(sys.argv[2])
    k=1
    for N in range(N0,N1+1):
        t0=time.time()
        k=1
        while B(k)<N: k+=1
        klb=k
        while True:
            f,c=search(N,k)
            if f: break
            k+=1
        print(N,k,'countLB',klb,f[0],round(time.time()-t0,2),flush=True)
