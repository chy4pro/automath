from fractions import Fraction as F
import itertools, math
# numbers a+b*sqrt3 as (a,b) Fractions
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def iszero(x): return x[0]==0 and x[1]==0
def val(x): return float(x[0])+float(x[1])*math.sqrt(3)
def d2(p,q):
    dx=sub(p[0],q[0]); dy=sub(p[1],q[1]); return add(mul(dx,dx),mul(dy,dy))
def cross(p,q,r):
    a=(sub(q[0],p[0]),sub(q[1],p[1])); b=(sub(r[0],p[0]),sub(r[1],p[1]))
    return sub(mul(a[0],b[1]),mul(a[1],b[0]))
def analyze(P,name=''):
    n=len(P)
    col=[t for t in itertools.combinations(range(n),3) if iszero(cross(P[t[0]],P[t[1]],P[t[2]]))]
    Ms=[];cls=[]
    for i in range(n):
        ds={}
        for j in range(n):
            if j!=i: ds.setdefault(d2(P[i],P[j]),[]).append(j)
        Ms.append(len(ds)); cls.append(sorted([v for v in ds.values()],key=len,reverse=True))
    apex={}
    for q,r in itertools.combinations(range(n),2):
        a=[p for p in range(n) if p not in(q,r) and d2(P[p],P[q])==d2(P[p],P[r])]
        apex[(q,r)]=a
    hist={}
    for v in apex.values(): hist[len(v)]=hist.get(len(v),0)+1
    print(name,'n',n,'collinear triples',len(col),'M',max(Ms),'Ms',Ms,'apex hist',hist)
    for i in range(n): print('  p',i,[len(c) for c in cls[i]],cls[i])
    return Ms,cls,apex
h=F(1,2)
def S(a,b=0): return (F(a),F(b))
# n=8 example, coordinates: x,y in Q(sqrt3)
P8=[ (S(-h),S(1,-h)), (S(-h),S(0,-h)), (S(-h,-h),S(h,-h)), (S(0,-h),S(h)), (S(h,-h),S(h,-h)), (S(0,-h),S(-h)), (S(-1),S(0)), (S(0),S(0)) ]
for p in P8: print((val(p[0]),val(p[1])))
analyze(P8,'n8')
