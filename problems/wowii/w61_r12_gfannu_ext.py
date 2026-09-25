from itertools import combinations_with_replacement
import sys
def hh(m):
    s=sorted(m,reverse=True); st=0
    while s and s[0]>0:
        d=s[0]; rest=s[1:]
        if d>len(rest): return None
        h,t=rest[:d],rest[d:]
        if any(x<=0 for x in h): return None
        s=sorted([x-1 for x in h]+t,reverse=True); st+=1
    return st
def parts(n,mx=None):
    if mx is None: mx=n
    if n==0: yield []; return
    for k in range(min(n,mx),0,-1):
        for r in parts(n-k,k): yield [k]+r
def esc(E,slots):
    o=set()
    for c in combinations_with_replacement(range(E+1),slots):
        if sum(c)==E: o.add(tuple(sorted(c,reverse=True)))
    return sorted(o)
def f6(l):
    s=sorted(l,reverse=True); w=s[0]; sec=s[1] if len(s)>1 else 0
    return w>=1 and s.count(w)==1 and sec<=w-2
NU=int(sys.argv[1]) if len(sys.argv)>1 else 10
print("nu | E0 surv | E0 miss | bnd pairs | bnd surv | bnd miss | E>=1 tested | E>=1 surv | E>=1 miss | verdict")
for nu in range(1,NU+1):
    e0=[tuple(l) for l in parts(2*nu) if hh([l[0]]*(l[0]+1)+l+[0,0,0])==l[0]]
    m0=[l for l in e0 if not f6(list(l))]
    bp=0; bs=[]
    for L in range(nu+1,2*nu+1):
        for l in parts(2*nu):
            if L>=l[0]: continue
            bp+=1
            if hh([L]*(L+1)+l+[0,0,0])==L: bs.append((L,tuple(l)))
    mb=[r for r in bs if not f6(list(r[1]))]
    tested=0; sv=[]
    for E in range(1,2*nu+1):
        for L in range(nu+1,2*nu-E+1):
            for ev in esc(E,L+1):
                C=[L+e for e in ev]
                for l in parts(2*nu-E):
                    tested+=1
                    if hh(C+l+[0,0,0])==L: sv.append((L,E,tuple(ev),tuple(l)))
    m1=[r for r in sv if not f6(list(r[3]))]
    ok = not m0 and not mb and not m1
    print(f"{nu:>2} | {str(e0):<9}| {str(m0 or 'none'):<8}| {bp:>9} | {len(bs):>8} | {str(mb or 'none'):<8} | "
          f"{tested:>11} | {len(sv):>9} | {str(m1 or 'none'):<9} | {'ELIMINATED' if ok else 'OPEN'}")
