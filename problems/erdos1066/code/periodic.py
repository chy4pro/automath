import numpy as np, itertools
from mis import *
def torus_graph(cell_pts, L1, L2, k1, k2, tol=1e-7):
    cell_pts=np.asarray(cell_pts); L1=np.asarray(L1); L2=np.asarray(L2)
    m=len(cell_pts)
    idx={}
    pts=[]
    for i in range(k1):
        for j in range(k2):
            for t in range(m):
                idx[(i,j,t)]=len(pts); pts.append(cell_pts[t]+i*L1+j*L2)
    n=len(pts); E=set()
    for i in range(k1):
        for j in range(k2):
            for t in range(m):
                p=cell_pts[t]+i*L1+j*L2
                for di in range(-2,3):
                    for dj in range(-2,3):
                        for s in range(m):
                            q=cell_pts[s]+(i+di)*L1+(j+dj)*L2
                            d=np.hypot(*(p-q))
                            if d<1-1e-6 and d>1e-9: raise ValueError('too close %g'%d)
                            if abs(d-1)<tol:
                                a=idx[(i,j,t)]; b=idx[((i+di)%k1,(j+dj)%k2,s)]
                                if a!=b: E.add((min(a,b),max(a,b)))
    return n,sorted(E)
def ratio(cell_pts,L1,L2,k1,k2):
    n,E=torus_graph(cell_pts,L1,L2,k1,k2)
    al=alpha_from_edges(n,E)
    return n,len(E),al,al/n
