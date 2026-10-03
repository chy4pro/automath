import numpy as np, itertools, math, random, sys
from search2 import prep, sa
def ring_pool(radii, N):
    pts=[]
    for r in radii:
        for j in range(N):
            a=2*math.pi*j/N; pts.append((round(r*math.cos(a),12),round(r*math.sin(a),12)))
    return pts
s3=math.sqrt(3); s2=math.sqrt(2)
radii=[(s3-1)/2, 1/s2, 1.0, (s3+1)/2/s2*1.0, s3/2, 0.5, (s3+1)/2]
radii=sorted(set(round(r,12) for r in radii))
pts=ring_pool(radii,24)
P,K=prep(pts); print('pool',len(pts),flush=True)
ns=[int(x) for x in sys.argv[1].split(',')]; restarts=int(sys.argv[2]); iters=int(sys.argv[3])
for n in ns:
    bestall=None
    for r in range(restarts):
        b=sa(P,K,n,iters,r)
        if bestall is None or b[0]<bestall[0]: bestall=b
    sc,S,ms,c=bestall
    print('n=',n,'M=',max(ms),'col',c,'Ms',sorted(ms),flush=True)
    np.save(f'ring_{n}.npy',P[S])
