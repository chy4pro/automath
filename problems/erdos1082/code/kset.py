import numpy as np, itertools
rng=np.random.default_rng(5)
for n in (9,12,15):
  for trial in range(3):
    P=rng.normal(size=(n,2)) if trial<2 else np.c_[np.cos(np.linspace(0,6,n)),np.sin(np.linspace(0,6,n))]*rng.uniform(0.8,1.2,size=(n,1))
    E=np.zeros(n-2,int)
    for t in itertools.combinations(range(n),3):
        A=P[list(t)]; ax,ay=A[0];bx,by=A[1];cx,cy=A[2]
        d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
        r2=(ax-ux)**2+(ay-uy)**2
        inside=sum(1 for i in range(n) if i not in t and (P[i,0]-ux)**2+(P[i,1]-uy)**2<r2)
        E[inside]+=1
    ok=all(E[j]+E[n-3-j]==2*(j+1)*(n-j-2) for j in range(n-2))
    print(n,trial,'identity holds' if ok else 'FAILS',list(E))
