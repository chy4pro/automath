import numpy as np
def verts(theta_deg, d, R=6):
    th=np.radians(theta_deg); r=1/np.sqrt(2); P=[]
    for i in range(-R,R+1):
        for j in range(-R,R+1):
            t = th*(1 if (i+j)%2==0 else -1)
            for k in range(4):
                a=t+np.pi/4+k*np.pi/2
                P.append((i*d+r*np.cos(a), j*d+r*np.sin(a)))
    P=np.array(P)
    # dedupe
    Q=[]
    for p in P:
        if not any(np.hypot(*(p-q))<1e-6 for q in Q): Q.append(p)
    return np.array(Q)
for th in [15]:
    for d in [np.sqrt(2)*np.cos(np.radians(45+th)), np.sqrt(2)*np.cos(np.radians(45-th))]:
        Q=verts(th,d,3)
        D=np.hypot(Q[:,None,0]-Q[None,:,0],Q[:,None,1]-Q[None,:,1]); np.fill_diagonal(D,9)
        print(th,d,len(Q),D.min(), np.bincount((abs(D-1)<1e-9).sum(1)))
