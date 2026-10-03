import numpy as np, itertools, math, random, sys
from collections import defaultdict
def pool_eisen(R):
    pts=[]
    for a in range(-R,R+1):
        for b in range(-R,R+1):
            if a*a+a*b+b*b<=R*R: pts.append((a,b))
    return pts
def pool_square(R):
    return [(a,b) for a in range(-R,R+1) for b in range(-R,R+1) if a*a+b*b<=R*R]
def build(pts, kind):
    n=len(pts)
    D=np.zeros((n,n),dtype=np.int64)
    for i in range(n):
        for j in range(n):
            a=pts[i][0]-pts[j][0]; b=pts[i][1]-pts[j][1]
            D[i,j]= a*a+a*b+b*b if kind=='e' else a*a+b*b
    # collinear: for each pair (i,j) set of k collinear
    col=defaultdict(set)
    for i,j in itertools.combinations(range(n),2):
        for k in range(n):
            if k==i or k==j: continue
            x1=pts[j][0]-pts[i][0]; y1=pts[j][1]-pts[i][1]; x2=pts[k][0]-pts[i][0]; y2=pts[k][1]-pts[i][1]
            if x1*y2-x2*y1==0: col[(i,j)].add(k)
    return D,col
def ncol(S,col):
    Sset=set(S); c=0
    for i,j in itertools.combinations(sorted(S),2):
        c+=len(col.get((i,j),set())&Sset)
    return c//3
def Mof(S,D):
    S=list(S); sub=D[np.ix_(S,S)]
    ms=[len(set(row))-1 for row in sub]  # minus zero
    return ms
def score(S,D,col):
    ms=Mof(S,D); c=ncol(S,col)
    return max(ms)+0.01*sum(ms)/len(S)+10*c, ms, c
def sa(pts,D,col,n,iters=20000,T0=1.0,seed=0):
    rnd=random.Random(seed); N=len(pts)
    S=rnd.sample(range(N),n); sc,ms,c=score(S,D,col); best=(sc,list(S),ms,c)
    for it in range(iters):
        T=T0*(1-it/iters)+1e-3
        i=rnd.randrange(n); new=rnd.randrange(N)
        if new in S: continue
        S2=list(S); S2[i]=new
        sc2,ms2,c2=score(S2,D,col)
        if sc2<=sc or rnd.random()<math.exp((sc-sc2)/T):
            S,sc,ms,c=S2,sc2,ms2,c2
            if sc<best[0]: best=(sc,list(S),ms,c)
    return best
if __name__=='__main__':
    kind=sys.argv[1]; R=int(sys.argv[2]); ns=[int(x) for x in sys.argv[3].split(',')]; restarts=int(sys.argv[4])
    pts=pool_eisen(R) if kind=='e' else pool_square(R)
    D,col=build(pts,kind)
    for n in ns:
        bestall=None
        for r in range(restarts):
            b=sa(pts,D,col,n,iters=6000,seed=r)
            if bestall is None or b[0]<bestall[0]: bestall=b
        sc,S,ms,c=bestall
        print(kind,R,'n=',n,'M=',max(ms),'collinear',c,'Ms',sorted(ms),'pts',[pts[i] for i in S],flush=True)
