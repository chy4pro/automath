from mis import *
import itertools, random, time
def brute(n,E):
    adj=[0]*n
    for u,v in E: adj[u]|=1<<v; adj[v]|=1<<u
    best=0
    for m in range(1<<n):
        ok=all(not (adj[v]&m) for v in bits(m))
        if ok: best=max(best,popcount(m))
    return best
random.seed(1)
for t in range(200):
    n=random.randint(1,13); p=random.random()
    E=[(i,j) for i in range(n) for j in range(i+1,n) if random.random()<p]
    a=alpha_from_edges(n,E); b=brute(n,E)
    assert a==b,(n,E,a,b)
print("ok")
