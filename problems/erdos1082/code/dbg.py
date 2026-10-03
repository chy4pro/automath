import numpy as np, itertools, math
from numopt2 import *
from scipy.optimize import least_squares
n=5;k=2
P=np.array([(2*math.cos(2*math.pi*j/5),2*math.sin(2*math.pi*j/5)) for j in range(5)])
x=P.flatten()+np.random.default_rng(0).normal(size=10)*0.05
trip=np.array(list(itertools.combinations(range(n),3))).T
for it in range(10):
    groups,c=assign(x.reshape(n,2),k); print(it,c,groups[:3])
    r=least_squares(resid,x,args=(n,groups,trip),method='trf',max_nfev=400); x=r.x; print(' ls cost',r.cost,r.status,r.nfev)
