import re
from math import gcd, lcm, prod
raw=open("$HOME/workspace/claudecode/automath/engine/harvest/erdos709_s1_raw.md").read()
def block_after(marker, ntuple):
    i=raw.find(marker); assert i>=0, marker
    seg=raw[i:]; j=seg.find("```text"); seg=seg[j:]; k=seg.find("```",7); seg=seg[:k]
    pat=r"\("+",".join([r"(-?\d+)"]*ntuple)+r"\)"
    return [tuple(map(int,m)) for m in re.findall(pat,seg)]
def check_layers(lines,t):
    layers=[set() for _ in range(t)]
    for L in lines:
        pts=L[:t]; d=L[t]
        assert all(pts[j+1]-pts[j]==d for j in range(t-1)), L
        assert d>=1
        for j in range(t): layers[j].add(pts[j])
    ds=[L[t] for L in lines]; assert len(set(ds))==len(ds), "duplicate slopes"
    return layers, sum(len(l) for l in layers)
def embed_and_verify(lines,t):
    # P30 Lemma 7 embedding; verify directly by counting multiples in the window
    ds=[L[t] for L in lines]; K=max(ds); D=K-min(ds)
    X=[[L[j] for L in lines] for j in range(t)]
    Xp=[[x-j*K for x in X[j]] for j in range(t)]
    R=max(abs(z) for layer in Xp for z in layer)
    Q=1
    for i in range(1,max(1,D)+1): Q=lcm(Q,i)
    C=R+D+1; N=C+R+D+1; m=N*Q+1
    mods=[]; u0=[]
    for L in lines:
        d=L[t]; dp=d-K; a=m+Q*dp; b=L[0]  # b = first-layer point
        us=[j*m+Q*(C+b+j*dp) for j in range(t)]
        assert all(us[j+1]-us[j]==a for j in range(t-1))
        mods.append(a); u0.append(us[0])
    assert max(mods)==m
    assert all(gcd(mods[i],mods[j])==1 for i in range(len(mods)) for j in range(i))
    P=prod(mods)
    x=sum(((-u)%a)*(P//a)*pow(P//a,-1,a) for a,u in zip(mods,u0))%P
    W=t*m; union=set()
    for a in mods:
        first=(x//a+1)*a; ms=[]
        z=first
        while z<=x+W: ms.append(z-x); z+=a
        assert len(ms)==t, (a,len(ms))
        union|=set(ms)
    return len(mods), len(union), m
L17=block_after("### r = 17",4); lay,pts=check_layers(L17,3); print("3-layer 17-system: lines",len(L17),"points",pts,"layers",[len(l) for l in lay])
r,u,m=embed_and_verify(L17,3); print("  CRT-embedded: moduli",r,"union in window of 3*max(A):",u,"-> f(%d) >= 4"%r if u<r else "FAIL", " max(A) digits",len(str(m)))
L62=block_after("全部 62 条",5); lay,pts=check_layers(L62,4); print("4-layer 62-system: lines",len(L62),"points",pts,"layers",[len(l) for l in lay])
r,u,m=embed_and_verify(L62,4); print("  CRT-embedded: moduli",r,"union in window of 4*max(A):",u,"-> f(%d) >= 5"%r if u<r else "FAIL", " max(A) digits",len(str(m)))
L79=block_after("79 条线",5); lay,pts=check_layers(L79,4); print("4-layer 79-system: lines",len(L79),"points",pts,"layers",[len(l) for l in lay])
r,u,m=embed_and_verify(L79,4); print("  CRT-embedded: moduli",r,"union:",u,"excess",r-u)
# also the r=12..16 exhaustive-optimum systems: just check the data consistency
for rr in (12,13,14,15,16):
    Ls=block_after("### r = %d"%rr,4); lay,pts=check_layers(Ls,3); print("3-layer r=%d system: lines %d points %d"%(rr,len(Ls),pts))
print("ALL CHECKS DONE")
