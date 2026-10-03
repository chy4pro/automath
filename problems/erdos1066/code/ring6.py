import numpy as np
from scipy.optimize import brentq
from mis import *
s3=np.sqrt(3)
def e(a): return np.array([np.cos(np.radians(a)),np.sin(np.radians(a))])
def build(ts):
    v=[np.zeros(2)]; d=0.0
    v.append(v[-1]+s3*e(d))
    for t in ts:
        d+=t; v.append(v[-1]+s3*e(d))
    return v
def pts(v,k):
    P=list(v)
    for i in range(k):
        a,b=v[i],v[i+1]; m=(a+b)/2; u=(b-a)/s3; nrm=np.array([-u[1],u[0]])
        P.append(m+nrm/2); P.append(m-nrm/2)
    return np.array(P)
k=6
res=[]
for t in np.linspace(40,60,201):
    # symmetric: turnings t at all 5 hinges -> closure distance
    v=build([t]*(k-1)); d=np.hypot(*(v[k]-v[0])); res.append((t,d))
f=lambda t: np.hypot(*(build([t]*(k-1))[k]-build([t]*(k-1))[0]))-1
t=brentq(f,40,59.999)
v=build([t]*(k-1)); P=pts(v,k); E,dm=penny_edges(P,1e-6)
print('turn',t,'n',len(P),'edges',len(E),'mindist',dm)
print('alpha',alpha_from_edges(len(P),E))
