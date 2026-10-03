"""Rigorous re-verification (mpmath interval arithmetic) of B&B leaf certificates for relaxation R_n(h) at lambda0.
Usage: verify.py n h lambda0_decimal_string
"""
import sys, time, numpy as np
from fractions import Fraction as F
from mpmath import iv, mpf
import bnb
iv.prec=90
def I(x): return iv.mpf(x)
def run_and_verify(n,h,lam_str,maxboxes=10**8,delta=0.0):
    lam_f=float(lam_str)
    t0=time.time()
    res,cnt,leaves=bnb.run(n,h,lam_f,margin=max(1e-7,1.05*delta),maxboxes=maxboxes,verbose=False)
    print('float B&B:',res,'boxes',cnt,'leaves',len(leaves),'t',round(time.time()-t0,1),flush=True)
    if res!='INFEASIBLE': return False
    lam=iv.mpf(lam_str)          # encloses the decimal number exactly
    H=I(h)                       # h is the exact binary float value
    pi=iv.pi
    ell=[]
    for j in range(1,n+1):
        th=j*H
        ell.append((iv.sin(2*pi*th)/(2*pi*th), -(1-iv.cos(2*pi*th))/(2*pi*th)))
    eR,eI=iv.cos(pi*H),-iv.sin(pi*H)   # e = exp(-i pi h)
    ch=iv.cos(pi*H)
    def cmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    def cadd(a,b): return (a[0]+b[0],a[1]+b[1])
    def cscale(s,a): return (s*a[0],s*a[1])
    def conj(a): return (a[0],-a[1])
    def Svec(v,m):
        vv=[(I(float(z.real)),I(float(z.imag))) for z in v]
        out=[]
        for j in range(m+1):
            s=(I(0),I(0))
            for a in range(j,len(vv)):
                s=cadd(s,cmul(conj(vv[a]),vv[a-j]))
            out.append(s)
        return out
    def ub_affine(const,W,box):
        # upper bound of const + 2 Re sum W_j z_j over box ; Re(W z)= W_R x - W_I y
        tot=const
        for j in range(len(W)):
            xr=iv.mpf([box[j][0][0],box[j][0][1]]); yr=iv.mpf([box[j][1][0],box[j][1][1]])
            tot=tot+2*(W[j][0]*xr-W[j][1]*yr)
        return tot.b
    bad=0; vol=F(0); minmarg=[1e9]
    for lf in leaves:
        box=lf[1]
        v_=F(1)
        for j in range(n):
            for k in range(2): v_*=F(box[j][k][1])-F(box[j][k][0])
        vol+=v_
        if lf[0]=='disk':
            j=lf[2]; xr,yr=box[j]
            mx=F(0) if xr[0]<=0<=xr[1] else min(abs(F(xr[0])),abs(F(xr[1])))
            my=F(0) if yr[0]<=0<=yr[1] else min(abs(F(yr[0])),abs(F(yr[1])))
            if not (mx*mx+my*my>1): bad+=1
            continue
        _,box,w,v=lf
        if w==0:
            S=Svec(v,n)
            ub=ub_affine(S[0][0],S[1:],box)
        elif w==1:
            S=Svec(v,n)
            tot=S[0][0]*(1-lam)
            for j in range(n):
                x=iv.mpf([box[j][0][0],box[j][0][1]]); y=iv.mpf([box[j][1][0],box[j][1][1]])
                r2=x**2+y**2
                nR=x*r2-lam*ell[j][0]; nI=y*r2-lam*ell[j][1]
                tot=tot+2*(S[j+1][0]*nR-S[j+1][1]*nI)
            ub=tot.b
            minmarg[0]=min(minmarg[0],-float(ub))
            if not (ub< -delta): bad+=1
            continue
        else:
            m=len(v); Sp=Svec(v,m-1)
            e=(eR,eI); ce=conj(e)
            const=Sp[0][0]*(-ch); W=[(I(0),I(0)) for _ in range(n)]
            W[0]=cadd(W[0],cscale(Sp[0][0]*mpf(0.5),ce))
            for j in range(1,m):
                if j-1==0:
                    const=const+2*cmul(Sp[j],cscale(I(0.5),e))[0]
                else:
                    W[j-2]=cadd(W[j-2],cmul(Sp[j],cscale(I(0.5),e)))
                if j+1<=n: W[j]=cadd(W[j],cmul(Sp[j],cscale(I(0.5),ce)))
                W[j-1]=cadd(W[j-1],cscale(-ch,Sp[j]))
            ub=ub_affine(const,W,box)
        if not (ub<0): bad+=1
    print('verified leaves:',len(leaves),'failed:',bad,'min T2 margin',minmarg[0],'covered volume:',vol,'root volume:',F(4)**n,'t',round(time.time()-t0,1),flush=True)
    return bad==0 and vol==F(4)**n
if __name__=='__main__':
    ok=run_and_verify(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3],delta=float(sys.argv[4]) if len(sys.argv)>4 else 0.0)
    print('RIGOROUS_INFEASIBLE' if ok else 'NOT_VERIFIED')
