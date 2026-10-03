import numpy as np
def verts(th_deg,a,R=4):
    r=1/np.sqrt(2); P=[]
    for i in range(-R,R+1):
        for j in range(-R,R+1):
            for (cx,cy,t) in [(i*a,j*a,th_deg),((i+.5)*a,(j+.5)*a,-th_deg)]:
                for k in range(4):
                    ang=np.radians(t+45+90*k)
                    P.append((cx+r*np.cos(ang),cy+r*np.sin(ang)))
    P=np.round(np.array(P),9)
    Q=np.unique(P,axis=0)
    return Q
