import numpy as np, time
from snub2 import verts
from mis import *
a=np.sqrt(2+np.sqrt(3))
Q=verts(15,a,R=6)
for Rad in [2,2.5,3,3.5,4,4.5,5]:
    P=Q[np.hypot(Q[:,0],Q[:,1])<=Rad]
    E,dm=penny_edges(P)
    t=time.time()
    al=alpha_from_edges(len(P),E)
    print(Rad,len(P),len(E),round(dm,6),al, al/len(P), round(time.time()-t,2))
