import numpy as np
from periodic import *
a=np.sqrt(2+np.sqrt(3)); r=1/np.sqrt(2)
cell=[]
for (cx,cy,t) in [(0,0,15),(.5*a,.5*a,-15)]:
    for k in range(4):
        ang=np.radians(t+45+90*k); cell.append((cx+r*np.cos(ang),cy+r*np.sin(ang)))
cell=np.array(cell)
# reduce mod lattice and dedupe
cell=np.mod(cell, a); cell=np.round(cell,9)%np.round(a,9)
u=[]
for p in cell:
    if not any(np.hypot(*(p-q))<1e-6 or np.hypot(*((p-q+a/2)%a-a/2))<1e-6 for q in u): u.append(p)
print(len(u))
for k1,k2 in [(2,2),(2,4),(4,4),(3,3),(4,6),(6,6),(5,5)]:
    print(k1,k2,ratio(u,(a,0),(0,a),k1,k2),flush=True)
