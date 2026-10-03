import numpy as np, math, itertools
from core import Mvals
def check(P,name,tol=1e-9):
    P=np.asarray(P,float); n=len(P)
    D2=((P[:,None]-P[None])**2).sum(-1)
    ms,cls=Mvals(P,tol)
    V=sum(sum((a-3)**2 for a in c) for c in cls)
    Z=[0,0,0]
    for q,r in itertools.combinations(range(n),2):
        a=sum(1 for p in range(n) if p not in(q,r) and abs(D2[p,q]-D2[p,r])<tol*max(1,D2[p,q]))
        Z[a]+=1
    lhs=9*sum(ms)-3*n*(n-1); rhs=V+2*Z[1]+4*Z[0]
    F=[c for c in cls]  # farthest class size:
    far=[]
    for i in range(n):
        d=np.delete(D2[i],i); far.append(int((np.abs(d-d.max())<tol*d.max()).sum()))
    print(name,'n',n,'lhs',lhs,'rhs',rhs,'Z',Z,'#|F|>=3',sum(1 for f in far if f>=3))
s=math.sqrt(3)
check([(-0.5,1-s/2),(-0.5,-s/2),(-(1+s)/2,-(s-1)/2),(-s/2,0.5),((1-s)/2,(1-s)/2),(-s/2,-0.5),(-1,0),(0,0)],'two squares n=8')
for k in (5,7,9): check([(math.cos(2*math.pi*j/k),math.sin(2*math.pi*j/k)) for j in range(k)]+[(0,0)],f'{k}-gon+center')
check([(math.cos(2*math.pi*j/7),math.sin(2*math.pi*j/7)) for j in range(7)],'heptagon')
rng=np.random.default_rng(1); check(rng.normal(size=(12,2)),'random12')
