import numpy as np, math
def config(k):
    c=math.cos(math.pi/k); rho=math.sqrt(1+c*c)-c
    a0=2*np.pi*np.arange(k)/k; a1=np.pi/k+a0
    return np.concatenate([np.c_[np.cos(a0),np.sin(a0)], rho*np.c_[np.cos(a1),np.sin(a1)]]),rho
def Mmax(P,tol=1e-10):
    D=((P[:,None]-P[None])**2).sum(-1); n=len(P); ms=[]
    for i in range(n):
        d=np.sort(np.delete(D[i],i)); ms.append(1+int((np.diff(d)>tol).sum()))
    return max(ms),min(ms)
def mincross(P):
    n=len(P); best=1e9
    for i in range(n):
        A=P-P[i]
        cr=np.abs(A[:,None,0]*A[None,:,1]-A[:,None,1]*A[None,:,0])
        cr[i,:]=1e9; cr[:,i]=1e9; np.fill_diagonal(cr,1e9)
        best=min(best,cr.min())
    return best
for k in range(4,101,4):
    P,rho=config(k); M,m=Mmax(P); print(k,2*k,'rho',round(rho,8),'M',M,'minM',m,'n/2-1',k-1,'mincross',f'{mincross(P):.2e}',flush=True)
