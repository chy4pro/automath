import numpy as np
from scipy.optimize import brentq
from mis import *
s3=np.sqrt(3)
def e(a): return np.array([np.cos(np.radians(a)),np.sin(np.radians(a))])
def build(t1,t2):
    ts=[t1,t2,t2,t1]  # turnings at hinges v1..v4
    v=[np.zeros(2)]; d=0.0
    v.append(v[-1]+s3*e(d))
    for t in ts:
        d+=t; v.append(v[-1]+s3*e(d))
    return v
def pts(v):
    P=list(v)
    for i in range(5):
        a,b=v[i],v[i+1]; m=(a+b)/2; u=(b-a)/s3; nrm=np.array([-u[1],u[0]])
        P.append(m+nrm/2); P.append(m-nrm/2)
    return np.array(P)
sols=[]
for t1 in np.linspace(30,60,61):
    f=lambda t2: np.hypot(*(build(t1,t2)[5]-build(t1,t2)[0]))-1
    xs=np.linspace(0.01,60,600); vals=[f(x) for x in xs]
    for k in range(len(xs)-1):
        if vals[k]*vals[k+1]<0:
            t2=brentq(f,xs[k],xs[k+1]); v=build(t1,t2); P=pts(v)
            E,dm=penny_edges(P,1e-6)
            sols.append((t1,t2,dm,len(E)))
good=[s for s in sols if s[2]>1-1e-9]
print(len(sols),len(good))
for s in good[:10]: print(s)
if good:
    t1,t2,_,_=good[len(good)//2]; v=build(t1,t2); P=pts(v); E,dm=penny_edges(P,1e-6)
    print('chosen',t1,t2,'n',len(P),'edges',len(E),'mindist',dm,'alpha',alpha_from_edges(len(P),E))
    np.save('ring5.npy',P)
    # angle checks at v0
    print('angle at v0 between axis0 and v5:', np.degrees(np.arccos(np.dot((v[1]-v[0])/s3,(v[5]-v[0])))))
