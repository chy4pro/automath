import sys, time
from math import gcd
# Minimal M such that a B3 set mod M of size k exists. WLOG 0 in A (translation).
def L(k): return k*(k*k-k+2)//2
def isB3mod(A,M):
    s=set(); A=sorted(A)
    for i in range(len(A)):
        for j in range(i,len(A)):
            for l in range(j,len(A)):
                v=(A[i]+A[j]+A[l])%M
                if v in s: return False
                s.add(v)
    return True
def search(k,M,findall=False):
    mask=(1<<M)-1
    def rot(b,x):
        x%=M
        return ((b<<x)|(b>>(M-x)))&mask
    res=[]
    def dfs(A,P,T,Abits):
        if len(A)==k:
            res.append(list(A)); return not findall
        for x in range(A[-1]+1,M):
            newb=rot(P,x)|rot(Abits,2*x)|rot(1,3*x)
            if newb & T: continue
            if newb.bit_count()!=P.bit_count()+Abits.bit_count()+1: continue
            P2=P|rot(Abits,x)|rot(1,2*x)
            if dfs(A+[x],P2,T|newb,Abits|(1<<x)): return True
        return False
    # second element: by multiplier symmetry can't fix fully (only units); keep general but use 0 in A.
    dfs([0],1,1,1)
    return res
if __name__=='__main__':
    K=int(sys.argv[1])
    for k in range(3,K+1):
        M=L(k); t0=time.time()
        while True:
            r=search(k,M)
            if r:
                assert isB3mod(r[0],M)
                print(k,'L(k)=',L(k),'minM=',M,r[0],'fill L/M=%.3f'%(L(k)/M),'k^3/M=%.3f'%(k**3/M),'t=%.1f'%(time.time()-t0),flush=True)
                break
            M+=1
