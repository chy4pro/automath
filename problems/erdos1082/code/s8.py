import numpy as np, math, itertools
from collections import Counter
s=math.sqrt(3)
P=np.array([(-0.5,1-s/2),(-0.5,-s/2),(-(1+s)/2,-(s-1)/2),(-s/2,0.5),((1-s)/2,(1-s)/2),(-s/2,-0.5),(-1,0),(0,0)])
n=len(P); D2=((P[:,None]-P[None])**2).sum(-1)
sL={}
for p,pp in itertools.combinations(range(n),2):
    c=0
    for q,r in itertools.combinations([x for x in range(n) if x not in(p,pp)],2):
        if abs(D2[p,q]-D2[p,r])<1e-9 and abs(D2[pp,q]-D2[pp,r])<1e-9: c+=1
    sL[(p,pp)]=c
print('s(L) distribution',Counter(sL.values()))
