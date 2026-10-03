import numpy as np, time, sys
from good import build, lattice_pts
from exhaust import min_good
from dodec import dodec
def hexcond(S):
    return lambda p,i,j: max(abs(i),abs(j),abs(i+j))<=S
for S in [3,4,5,6,7]:
    P=lattice_pts(hexcond(S),R=S+1); adj=build(P)
    t=time.time(); r=min_good(adj,6)
    print('hexagon side',S,'n',len(P),'min good set',r[0] if r else '>6', 'example',[tuple(np.round(P[i],3)) for i in r[1]] if r else None, round(time.time()-t,1),'s',flush=True)
for R in [4,5]:
    P=dodec(R); adj=build(P); t=time.time(); r=min_good(adj,6)
    print('dodec R',R,'n',len(P),'min good',r[0] if r else '>6',round(time.time()-t,1),flush=True)
