import json,os,sympy as sp
HERE="$HOME/workspace/claudecode/automath/problems/zc1a7"
D=json.load(open(os.path.join(HERE,"a7_table.json")))
NAMES=D["names"];NC=len(NAMES);IDX={NAMES[k]:k for k in range(NC)}
TAB=[[sp.sympify(s) for s in row] for row in D["table"]];DEG=D["degrees"]
t=sp.Symbol("t")
PI={"7 pts":{"1a":7,"2a":3,"4a":1},"21 pairs":{"1a":21,"2a":5,"4a":1},
    "35 triples":{"1a":35,"2a":7,"4a":1},"15 cosets":{"1a":15,"2a":3,"4a":1}}
chars=[("ord deg %d"%DEG[i],DEG[i],TAB[i][IDX["2a"]],TAB[i][IDX["4a"]]) for i in range(NC)]
for lab,pi in PI.items():
    for p in (3,5,7):
        s=2 if pi["1a"]%p==0 else 1
        chars.append(("p=%d %s dim %d"%(p,lab,pi["1a"]-s),pi["1a"]-s,pi["2a"]-s,pi["4a"]-s))
print("%-24s %-8s %-8s %-10s %-10s"%("character","chi(2a)","chi(4a)","t >=","t <="))
for name,d,v2,v4 in chars:
    chu=t*v2+(1-t)*v4
    lo,hi=-sp.oo,sp.oo
    for ell in range(4):
        mu=sp.Rational(1,4)*(d+v2*(-1)**ell+chu*(sp.I**(-ell)+sp.I**ell))
        mu=sp.expand(sp.simplify(mu)); P=sp.Poly(mu,t)
        b=P.coeff_monomial(t); a=P.coeff_monomial(1)
        if b>0: lo=max(lo,sp.ceiling(-a/b))
        elif b<0: hi=min(hi,sp.floor(-a/b))
    print("%-24s %-8s %-8s %-10s %-10s"%(name,v2,v4,lo,hi))
