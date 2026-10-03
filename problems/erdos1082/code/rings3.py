import mpmath as mp, itertools, math
mp.mp.dps=60
def check(k,rho_float):
    phi=mp.pi/k
    # refine rho: find which coincidence holds; solve symbolic by mp.findroot on each candidate equation near rho_float
    def pts(rho):
        P=[(mp.cos(2*mp.pi*j/k),mp.sin(2*mp.pi*j/k)) for j in range(k)]
        P+=[(rho*mp.cos(phi+2*mp.pi*j/k),rho*mp.sin(phi+2*mp.pi*j/k)) for j in range(k)]
        return P
    # candidate equations: ring0 point0 distances vs ring1 distances
    best=None
    for a in range(1,k):
        for b in range(k):
            f=lambda r: (2-2*mp.cos(2*mp.pi*a/k))-(1+r**2-2*r*mp.cos(phi+2*mp.pi*b/k))
            try:
                r=mp.findroot(f,rho_float)
            except Exception: continue
            if abs(r-rho_float)<1e-6: best=r;break
        if best is not None: break
    rho=best
    P=pts(rho); n=len(P)
    d2=lambda p,q:(p[0]-q[0])**2+(p[1]-q[1])**2
    Ms=[]
    for i in range(n):
        vals=[]
        for j in range(n):
            if j==i: continue
            v=d2(P[i],P[j])
            if not any(abs(v-w)<mp.mpf(10)**-40 for w in vals): vals.append(v)
        Ms.append(len(vals))
    mincross=min(abs((P[j][0]-P[i][0])*(P[l][1]-P[i][1])-(P[l][0]-P[i][0])*(P[j][1]-P[i][1])) for i,j,l in itertools.combinations(range(n),3))
    return rho,max(Ms),Ms,mincross
for k,r in [(4,0.517638090205),(8,2.285332209101),(10,0.61803398875),(12,2.356254097559)]:
    rho,M,Ms,mc=check(k,r); print('k',k,'n',2*k,'rho',mp.nstr(rho,20),'M',M,'set(Ms)',set(Ms),'min|cross|',mp.nstr(mc,5))
