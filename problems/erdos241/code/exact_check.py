# Exact rational verification for the explicit step function g0 (n=640 bins).
import numpy as np
from fractions import Fraction
D='./'
p=np.load(D+'mu1_p640.npy'); n=len(p)
Q=10**12
P=[int(round(x*Q)) for x in p]
P[n//2]+= Q-sum(P)          # make sum exactly Q
assert sum(P)==Q and min(P)>=0
def conv(a,b):
    # exact integer convolution via Python ints (O(n^2))
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out
PP=conv(P,P)
q=conv(PP,P[::-1])      # p*p*p~ scaled by Q^3
q3=conv(PP,P)           # p*p*p scaled by Q^3
mq=max(q); mq3=max(q3)
sup_ggg_tilde=Fraction(n*mq,Q**3)
sup_ggg=Fraction(n*mq3,Q**3)
print('rigorous sup g*g*g~ <=',float(sup_ggg_tilde))
print('rigorous sup g*g*g  <=',float(sup_ggg))
# exact L2 norm of g*g for the step function: g*g piecewise linear with knot values y_m = n*(p*p)_{m-1}
y=[0]+[n*v for v in PP]+[0]     # knots m=0..2n, values scaled by Q^2
s=0
for m in range(len(y)-1):
    s+= y[m]*y[m]+y[m]*y[m+1]+y[m+1]*y[m+1]
L2=Fraction(s,3*n*Q**4)
print('exact int (g*g)^2 =',float(L2))
c_lim=(2/float(sup_ggg_tilde))**(1/3)
print('density-route barrier: c >= (2/sup)^(1/3) =',c_lim)
print('record constant check (2/0.574635)^(1/3)=',(2/0.574635)**(1/3))
# also check: g*g*g~ on [0,1] average etc
