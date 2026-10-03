import numpy as np, itertools, math
TOL=1e-9
def Mvals(P, tol=TOL):
    P=np.asarray(P,float); n=len(P)
    D=np.sqrt(((P[:,None,:]-P[None,:,:])**2).sum(-1))
    res=[]; classes=[]
    for i in range(n):
        d=np.sort(np.delete(D[i],i))
        sizes=[]; c=1
        for k in range(1,len(d)):
            if abs(d[k]-d[k-1])<tol*max(1,d[k]): c+=1
            else: sizes.append(c); c=1
        sizes.append(c)
        res.append(len(sizes)); classes.append(sorted(sizes,reverse=True))
    return res, classes
def collinear_triples(P, tol=1e-9):
    P=np.asarray(P,float); n=len(P); cnt=0
    for i,j,k in itertools.combinations(range(n),3):
        a=P[j]-P[i]; b=P[k]-P[i]
        if abs(a[0]*b[1]-a[1]*b[0])<tol*max(1,np.abs(a).max()*np.abs(b).max()): cnt+=1
    return cnt
def apex_stats(P,tol=TOL):
    P=np.asarray(P,float); n=len(P)
    D2=((P[:,None,:]-P[None,:,:])**2).sum(-1)
    hist={}
    for q,r in itertools.combinations(range(n),2):
        a=0
        for p in range(n):
            if p!=q and p!=r and abs(D2[p,q]-D2[p,r])<tol*max(1,D2[p,q]): a+=1
        hist[a]=hist.get(a,0)+1
    return hist
