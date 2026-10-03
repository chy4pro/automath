import numpy as np, math
s=math.sqrt(3)
P=np.array([(-0.5,1-s/2),(-0.5,-s/2),(-(1+s)/2,-(s-1)/2),(-s/2,0.5),((1-s)/2,(1-s)/2),(-s/2,-0.5),(-1,0),(0,0)])
c=P.mean(0); Q=P-c
for q in Q: print(round(np.hypot(*q),6), round(math.degrees(math.atan2(q[1],q[0]))%360,4))
D=np.sqrt(((P[:,None]-P[None])**2).sum(-1)); print(sorted(set(np.round(D.flatten(),6))))
