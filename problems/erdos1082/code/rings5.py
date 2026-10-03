import mpmath as mp, itertools
mp.mp.dps=50
def analyze(k,r0):
    phi=mp.pi/k
    # find exact rho by root of the coincidence equation nearest r0
    eqs=[]
    for a in range(1,k//2+1):
        s=4*mp.sin(mp.pi*a/k)**2
        for b in range(k):
            c=mp.cos(phi+2*mp.pi*b/k)
            eqs.append(('cross=ring0chord a=%d b=%d'%(a,b), lambda r,s=s,c=c: 1+r**2-2*r*c-s))
            eqs.append(('cross=ring1chord a=%d b=%d'%(a,b), lambda r,s=s,c=c: 1+r**2-2*r*c-s*r**2))
    rho=None
    for name,f in eqs:
        if abs(f(mp.mpf(r0)))<1e-8:
            rho=mp.findroot(f,mp.mpf(r0)); break
    hold=[name for name,f in eqs if abs(f(rho))<mp.mpf(10)**-35]
    P=[(mp.cos(2*mp.pi*j/k),mp.sin(2*mp.pi*j/k)) for j in range(k)]+[(rho*mp.cos(phi+2*mp.pi*j/k),rho*mp.sin(phi+2*mp.pi*j/k)) for j in range(k)]
    n=len(P); Ms=[]
    for i in range(n):
        vals=[]
        for j in range(n):
            if j==i: continue
            v=(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2
            if not any(abs(v-w)<mp.mpf(10)**-35 for w in vals): vals.append(v)
        Ms.append(len(vals))
    mc=min(abs((P[j][0]-P[i][0])*(P[l][1]-P[i][1])-(P[l][0]-P[i][0])*(P[j][1]-P[i][1])) for i,j,l in itertools.combinations(range(n),3))
    print('k',k,'rho',mp.nstr(rho,25),'M',max(Ms),set(Ms),'mincross',mp.nstr(mc,4),'eqs holding',hold[:6])
for k,r in [(4,0.517638090205),(8,0.437573144078),(12,0.424402444981),(16,0.419907321939),(20,0.417846524909),(24,0.416732298342),(28,0.416062224579),(21,0.445041867913),(10,0.61803398875),(30,0.61803398875)]:
    analyze(k,r)
