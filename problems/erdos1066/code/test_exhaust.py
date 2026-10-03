import random, itertools
from exhaust import *
from mis import bits,popcount
# brute-force check on random small graphs
def brute(adj,kmax,need=1):
    n=len(adj)
    for k in range(1,kmax+1):
        for I in itertools.combinations(range(n),k):
            if any(adj[a]>>b&1 for a in I for b in I): continue
            N=0
            for v in I: N|=adj[v]|(1<<v)
            if 4*k-popcount(N)>=need: return k
    return None
random.seed(3)
for t in range(300):
    n=random.randint(4,11); p=random.uniform(0.15,0.5)
    adj=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if random.random()<p: adj[i]|=1<<j; adj[j]|=1<<i
    for need in (1,2):
        a=min_good(adj,4,need); b=brute(adj,4,need)
        assert (a[0] if a else None)==b,(adj,a,b,need)
print('exhaust ok')
