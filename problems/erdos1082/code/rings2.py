import numpy as np, math, itertools
from core import Mvals, collinear_triples
def config(k,phi,rho,center):
    P=[(math.cos(2*math.pi*j/k),math.sin(2*math.pi*j/k)) for j in range(k)]
    P+=[(rho*math.cos(phi+2*math.pi*j/k),rho*math.sin(phi+2*math.pi*j/k)) for j in range(k)]
    if center: P.append((0.0,0.0))
    return P
best={}
for k in range(3,13):
  for phi_num in range(0,2*k):  # phi = pi*phi_num/(2k)... in [0, 2pi/k)
    phi=math.pi*phi_num/(2*k) if phi_num<4 else None
    if phi is None: continue
    # candidate rho from coincidences: d^2(p,q)=d^2(p,q'), p on ring0 or ring1
    # ring0 point at angle 0 radius1; ring1 point at angle phi radius rho
    angs0=[2*math.pi*j/k for j in range(k)]; angs1=[phi+2*math.pi*j/k for j in range(k)]
    cands=set()
    # p ring0 (1,0): d2 to ring0 j: 2-2cos a ; to ring1: 1+rho^2-2rho cos b ; to center: 1
    for a in angs0[1:]:
        for b in angs1:
            # 2-2cos a = 1+rho^2-2rho cos b
            c=-(1-2*math.cos(a)); # rho^2 -2cos b rho + (1-2+2cos a)=0
            disc=math.cos(b)**2-(2*math.cos(a)-1)
            if disc>=0:
                for r in [math.cos(b)+math.sqrt(disc), math.cos(b)-math.sqrt(disc)]:
                    if r>1e-6: cands.add(round(r,12))
    for b in angs1: # ring0 p to center (1) = ring1 dist
        disc=math.cos(b)**2
        r=2*math.cos(b)
        if r>1e-6: cands.add(round(r,12))
    for b1,b2 in itertools.combinations(angs1,2):
        pass
    # p on ring1 at angle phi: d2 to ring1: rho^2(2-2cos a); to ring0: 1+rho^2-2rho cos(b) with b=angle diff
    for a in angs0[1:]:
        for b in angs0:
            bb=b-phi
            # rho^2(2-2cos a) = 1+rho^2-2 rho cos bb -> rho^2(1-2cos a)+2rho cos bb -1=0
            A=1-2*math.cos(a); B=2*math.cos(bb); C=-1
            if abs(A)<1e-12:
                if abs(B)>1e-12: cands.add(round(-C/B,12))
                continue
            disc=B*B-4*A*C
            if disc>=0:
                for r in [(-B+math.sqrt(disc))/(2*A),(-B-math.sqrt(disc))/(2*A)]:
                    if r>1e-6: cands.add(round(r,12))
        # ring1 to center: rho = ring1 to ring1 or ring0 distance
        for b in angs0:
            bb=b-phi; # rho^2 = 1+rho^2-2rho cos bb -> rho=1/(2cos bb)
            if math.cos(bb)>1e-9: cands.add(round(1/(2*math.cos(bb)),12))
    for rho in cands:
        if abs(rho-1)<1e-9 and phi==0: continue
        for center in (False,True):
            P=config(k,phi,rho,center)
            Pa=np.array(P)
            dmin=np.sqrt(((Pa[:,None]-Pa[None])**2).sum(-1)+np.eye(len(P))).min()
            if dmin<1e-6: continue
            if collinear_triples(P,1e-9)>0: continue
            m,_=Mvals(P,1e-9); n=len(P)
            key=n
            if key not in best or max(m)<best[key][0]:
                best[key]=(max(m),k,phi,rho,center)
for n in sorted(best): print(n,'M=',best[n][0],'floor(n/2)=',n//2,'k,phi,rho,center=',best[n][1:])
