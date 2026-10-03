import sys
sys.setrecursionlimit(100000)
def popcount(x): return bin(x).count('1')
def bits(x):
    while x:
        b = x & -x
        yield b.bit_length()-1
        x ^= b

class MIS:
    def __init__(self, n, adj):
        # adj: list of bitmasks
        self.n=n; self.adj=adj
        self.memo={}
    def components(self,S):
        comps=[]
        while S:
            b=S&-S; comp=b; frontier=b
            while frontier:
                nf=0
                for v in bits(frontier): nf|=self.adj[v]
                nf&=S&~comp
                comp|=nf; frontier=nf
            comps.append(comp); S&=~comp
        return comps
    def ub(self,S):
        # greedy clique cover: triangles then edges then singles
        adj=self.adj; cnt=0; R=S
        while R:
            b=R&-R; v=b.bit_length()-1
            N=adj[v]&R
            if N:
                # try find triangle
                best=None
                for u in bits(N):
                    T=adj[u]&N
                    if T:
                        w=(T&-T); best=(1<<u)|w; break
                if best is None:
                    u=N&-N; best=u
                R&=~(b|best)
            else:
                R&=~b
            cnt+=1
        return cnt
    def solve(self,S,lb=0):
        # returns alpha of G[S]
        if S==0: return 0
        adj=self.adj
        # reductions
        taken=0
        changed=True
        while changed and S:
            changed=False
            for v in bits(S):
                N=adj[v]&S
                d=popcount(N)
                if d<=1:
                    taken+=1; S&=~(N|(1<<v)); changed=True; break
                if d==2:
                    a=N&-N; bb=N^a
                    if adj[a.bit_length()-1]&bb:
                        taken+=1; S&=~(N|(1<<v)); changed=True; break
        if S==0: return taken
        comps=self.components(S)
        if len(comps)>1:
            tot=taken
            for C in comps: tot+=self.solve(C)
            return tot
        # branch
        best=self.greedy(S)
        res=self.bb(S,0,best)
        out=res+taken
        return out
    def greedy(self,S):
        adj=self.adj; c=0
        while S:
            # min degree vertex
            mv=None;md=99
            for v in bits(S):
                d=popcount(adj[v]&S)
                if d<md: md=d;mv=v
            c+=1; S&=~(adj[mv]|(1<<mv))
        return c
    def bb(self,S,cur,best):
        # returns best total found (>= best), cur=already chosen
        adj=self.adj
        if S==0: return max(best,cur)
        if cur+self.ub(S)<=best: return best
        # reductions inside
        for v in bits(S):
            N=adj[v]&S; d=popcount(N)
            if d<=1:
                return self.bb(S&~(N|(1<<v)),cur+1,best)
            if d==2:
                a=N&-N; bb_=N^a
                if adj[a.bit_length()-1]&bb_:
                    return self.bb(S&~(N|(1<<v)),cur+1,best)
        comps=self.components(S)
        if len(comps)>1:
            tot=cur+sum(self.solve(C) for C in comps)
            return max(best,tot)
        # pick max degree vertex
        mv=max(bits(S),key=lambda v: popcount(adj[v]&S))
        best=self.bb(S&~(adj[mv]|(1<<mv)),cur+1,best)
        best=self.bb(S&~(1<<mv),cur,best)
        return best

def alpha_from_edges(n,edges):
    adj=[0]*n
    for u,v in edges: adj[u]|=1<<v; adj[v]|=1<<u
    M=MIS(n,adj)
    return M.solve((1<<n)-1)

def penny_edges(P,tol=1e-7):
    import numpy as np
    P=np.asarray(P)
    D=np.hypot(P[:,None,0]-P[None,:,0],P[:,None,1]-P[None,:,1])
    n=len(P)
    E=[(i,j) for i in range(n) for j in range(i+1,n) if abs(D[i,j]-1)<tol]
    dm=D[np.triu_indices(n,1)].min() if n>1 else 9
    return E,dm
