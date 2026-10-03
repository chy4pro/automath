from good import *
import numpy as np
# big hexagon side S
def hexcond(S):
    def c(p,i,j):
        k=-i-j
        return max(abs(i),abs(j),abs(k))<=S
    return c
S=7
P=lattice_pts(hexcond(S),R=S+1)
adj=build(P)
n=len(P)
# interior: restrict I to vertices with distance >=4 from boundary (hex distance <= S-4)
def hexd(i,j): return max(abs(i),abs(j),abs(i+j))
ij=[]
for i in range(-S-1,S+2):
    for j in range(-S-1,S+2):
        if hexd(i,j)<=S: ij.append((i,j))
allowed=0
for t,(i,j) in enumerate(ij):
    if hexd(i,j)<=S-4: allowed|=1<<t
center=[t for t,(i,j) in enumerate(ij) if (i,j)==(0,0)]
best=beam_search(adj,m=12,width=400,starts=center,allowed=allowed)
print('interior lattice:',[(k,best[k][0]) for k in sorted(best)])
# corner of hexagon: start at corner
corner=[t for t,(i,j) in enumerate(ij) if (i,j)==(S,0)]
print('deg corner',popcount(adj[corner[0]]))
best=beam_search(adj,m=10,width=400,starts=corner)
print('corner start:',[(k,best[k][0]) for k in sorted(best)])
best=beam_search(adj,m=8,width=300)
print('all starts:',[(k,best[k][0]) for k in sorted(best)])
