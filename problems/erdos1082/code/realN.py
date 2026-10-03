import pickle, numpy as np, itertools, sys
from scipy.optimize import least_squares
n=int(sys.argv[2]); S=pickle.load(open('struct%d.pkl'%n,'rb'))
trip=np.array(list(itertools.combinations(range(n),3))).T
def eqs(st):
    E=[]
    for p in range(n):
        for C in st[p]:
            C=list(C)
            for c in C[1:]: E.append((p,C[0],c))
    return np.array(E)
def make(E):
    def f(x):
        P=np.concatenate([[0,0,1,0],x]).reshape(n,2)
        d=lambda a,b:((P[a]-P[b])**2).sum(-1)
        r=d(E[:,0],E[:,1])-d(E[:,0],E[:,2])
        return r
    return f
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
summary=[]
for si,st in enumerate(S):
    E=eqs(st); f=make(E); found=None; bestdeg=None
    types=sorted(tuple(sorted(len(C) for C in st[p])) for p in range(n))
    for t in range(400):
        x0=rng.normal(size=2*n-4)*1.5
        r=least_squares(f,x0,method='lm',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=2000)
        if np.abs(r.fun).max()<1e-11:
            P=np.concatenate([[0,0,1,0],r.x]).reshape(n,2)
            D=np.sqrt(((P[:,None]-P[None])**2).sum(-1)); sc=D.max()
            dmin=(D+np.eye(n)*1e9).min()/sc
            i,j,l=trip; a=P[j]-P[i]; b=P[l]-P[i]
            cr=(np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])).min()/sc**2
            deg=min(dmin,cr)
            if bestdeg is None or deg>bestdeg: bestdeg=deg
            if dmin>1e-5 and cr>1e-6:
                found=P; break
    summary.append((si,types,found is not None,bestdeg))
    print(si,types,'REALIZED' if found is not None else 'not found','best nondegeneracy among exact solutions',bestdeg,flush=True)
    if found is not None: np.save(f'realN_{si}.npy',found)
