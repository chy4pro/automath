import numpy as np, math, itertools
from core import Mvals
def config(k,phi,rho):
    P=[(math.cos(2*math.pi*j/k),math.sin(2*math.pi*j/k)) for j in range(k)]
    P+=[(rho*math.cos(phi+2*math.pi*j/k),rho*math.sin(phi+2*math.pi*j/k)) for j in range(k)]
    return np.array(P)
def coll(P):
    n=len(P); best=1e9
    for i,j in itertools.combinations(range(n),2):
        a=P[j]-P[i]; b=P-P[i]; cr=np.abs(a[0]*b[:,1]-a[1]*b[:,0]); cr[[i,j]]=1e9; best=min(best,cr.min())
    return best
for k in range(4,31):
    phi=math.pi/k
    chords0=[4*math.sin(math.pi*a/k)**2 for a in range(1,k//2+1)]
    cands=set()
    for a in range(1,k//2+1):
        for b in range(k):
            c=math.cos(phi+2*math.pi*b/k); s=4*math.sin(math.pi*a/k)**2
            # 1+r^2-2rc = s  (ring0 chord)
            disc=c*c-(1-s)
            if disc>=0:
                for r in (c+math.sqrt(disc),c-math.sqrt(disc)):
                    if r>1e-6: cands.add(round(r,12))
            # 1+r^2-2rc = s r^2 (ring1 chord)
            A=1-s;B=-2*c;C=1
            if abs(A)>1e-12:
                disc=B*B-4*A*C
                if disc>=0:
                    for r in ((-B+math.sqrt(disc))/(2*A),(-B-math.sqrt(disc))/(2*A)):
                        if r>1e-6: cands.add(round(r,12))
    res=[]
    for r in cands:
        if abs(r-1)<1e-9: continue
        P=config(k,phi,r)
        if coll(P)<1e-9: continue
        m,_=Mvals(P,1e-9); res.append((max(m),r))
    res.sort()
    print('k',k,'n',2*k,'best M',res[0] if res else None,'n/2',k, flush=True)
