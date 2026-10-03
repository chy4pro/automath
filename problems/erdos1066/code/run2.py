import numpy as np, time
from good import build, lattice_pts
from exhaust import min_good
for S in [8,9,10]:
    P=lattice_pts(lambda p,i,j: max(abs(i),abs(j),abs(i+j))<=S,R=S+1); adj=build(P)
    t=time.time(); r=min_good(adj,6)
    print('hexagon side',S,'n',len(P),'min savings-1 set size',r[0] if r else '>6',round(time.time()-t,1),'s',flush=True)
S=7
P=lattice_pts(lambda p,i,j: max(abs(i),abs(j),abs(i+j))<=S,R=S+1); adj=build(P)
for need in (2,3):
    t=time.time(); r=min_good(adj,8,need=need)
    print('hexagon side 7: min size with savings >=',need,':',r[0] if r else '>8',round(time.time()-t,1),'s',flush=True)
