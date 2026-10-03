from core import *
def reg(k,R=1,phase=0,c=(0,0)):
    return [(c[0]+R*math.cos(phase+2*math.pi*j/k), c[1]+R*math.sin(phase+2*math.pi*j/k)) for j in range(k)]
for k in [5,7,9,11,13,15]:
    P=reg(k)+[(0,0)]
    m,cl=Mvals(P); print('polygon+center k=',k,'n=',k+1,'M=',max(m),'collinear',collinear_triples(P),'apex hist',apex_stats(P), 'sum1/M', sum(1/x for x in m), 'bound 3n/(n-1)',3*(k+1)/k)
for n in [5,6,7,8,9,10]:
    P=reg(n); m,cl=Mvals(P); print('regular',n,'M',max(m),'coll',collinear_triples(P))
