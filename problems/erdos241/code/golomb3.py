import sys, time
# Minimal N such that a B3 set {0=a0<...<a_{k-1}=N} exists (integers).
def isB3(A):
    s=set()
    A=sorted(A)
    for i in range(len(A)):
        for j in range(i,len(A)):
            for l in range(j,len(A)):
                v=A[i]+A[j]+A[l]
                if v in s: return False
                s.add(v)
    return True

G={1:0,2:1}
sols={1:[0],2:[0,1]}
nodes=0
def search(k,N):
    global nodes
    # place 0 and N; elements in between, increasing
    # state: A list, P pairs bitset, T triples bitset
    res=[]
    def add(A,P,T,Abits,x):
        newb=(P<<x)|(Abits<<(2*x))|(1<<(3*x))
        if newb & T: return None
        if newb.bit_count()!=P.bit_count()+Abits.bit_count()+1: return None
        P2=P|(Abits<<x)|(1<<(2*x))
        if (Abits<<x)&P or (1<<(2*x))&P or ((Abits<<x)&(1<<(2*x))): pass  # pair-distinctness implied by triple-distinctness
        return (P2,T|newb,Abits|(1<<x))
    def dfs(A,P,T,Abits):
        global nodes
        nodes+=1
        i=len(A)
        r=k-i  # remaining incl. N
        if r==1:
            st=add(A,P,T,Abits,N)
            if st is not None:
                res.append(A+[N]); return True
            return False
        lo=A[-1]+1
        hi=N-G[r]  # remaining r elements need length >= G[r]
        # also prefix with i+1 elements needs x >= G[i+1]
        lo=max(lo,G[i+1])
        if i==1:
            # symmetry: first gap <= last gap is hard to enforce early; enforce a1 <= N/2 roughly
            hi=min(hi,N//2)
        for x in range(lo,hi+1):
            st=add(A,P,T,Abits,x)
            if st is None: continue
            if dfs(A+[x],*st): return True
        return False
    A=[0]; P=1; T=1; Abits=1
    dfs(A,P,T,Abits)
    return res
if __name__=='__main__':
    K=int(sys.argv[1])
    for k in range(3,K+1):
        N=G[k-1]+1
        t0=time.time()
        while True:
            r=search(k,N)
            if r:
                G[k]=N; sols[k]=r[0]
                assert isB3(r[0])
                print(k,N,r[0],'ratio k/N^(1/3)=%.4f'%(k/N**(1/3)),'(k-1)/N^(1/3)=%.4f'%((k-1)/N**(1/3)),'t=%.1f'%(time.time()-t0),'nodes',nodes,flush=True)
                break
            N+=1
