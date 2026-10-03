"""Branch and bound: prove infeasibility of Fourier/Toeplitz relaxation R_n(h) at lambda0.
Variables: c_j = x_j + i y_j, j=1..n (Fourier coefficients of mu at frequencies j*h).
Constraints: T1=Toep(1,c_1..c_n) PSD; T2=Toep(1-lam, rho_1..rho_n) PSD, rho_j=c_j|c_j|^2-lam*ell(jh);
T3 = localizing Toep(g_0..g_{n-1}) PSD, g_j = .5 e^{-i pi h} c_{j-1} + .5 e^{i pi h} c_{j+1} - cos(pi h) c_j.
A box is discarded if for some matrix and some test vector v the upper bound of v^*Tv over the box is < -margin.
"""
import numpy as np, sys, time
from scipy.linalg import toeplitz
def ellf(t):
    return (1-np.exp(-2j*np.pi*t))/(2j*np.pi*t)
def herm_toep(seq):
    col=np.array(seq,dtype=complex); return toeplitz(col,np.conj(col))
def Svec(v,n):
    # S_j = sum_{a-b=j} conj(v_a) v_b, j=0..n
    m=len(v); return np.array([np.sum(np.conj(v[j:])*v[:m-j]) for j in range(n+1)])
def iv_mul(a,b):
    p=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
    return (min(p),max(p))
def iv_sq(a):
    lo,hi=a
    if lo>=0: return (lo*lo,hi*hi)
    if hi<=0: return (hi*hi,lo*lo)
    return (0.0,max(lo*lo,hi*hi))
def iv_add(a,b): return (a[0]+b[0],a[1]+b[1])
def iv_scale(s,a): return (s*a[0],s*a[1]) if s>=0 else (s*a[1],s*a[0])
def ncube_bounds(xi,yi):
    r2=iv_add(iv_sq(xi),iv_sq(yi))
    return iv_mul(xi,r2), iv_mul(yi,r2)   # Re n, Im n
def max_affine(S0,S,box_re,box_im):
    # max over box of S0 + 2 Re(sum S_j z_j), z_j in box (re-interval, im-interval)
    tot=S0
    for j in range(len(S)):
        a=S[j].real; b=-S[j].imag   # Re(S z) = a*Re z + b*Im z
        tot+=2*(max(a*box_re[j][0],a*box_re[j][1])+max(b*box_im[j][0],b*box_im[j][1]))
    return tot
class Prob:
    def __init__(s,n,h,lam):
        s.n,s.h,s.lam=n,h,lam
        s.ell=np.array([ellf(j*h) for j in range(1,n+1)])
        s.e=np.exp(-1j*np.pi*h); s.ch=np.cos(np.pi*h)
    def mats(s,c):
        n=s.n
        T1=herm_toep(np.concatenate([[1],c]))
        rho=c*np.abs(c)**2-s.lam*s.ell
        T2=herm_toep(np.concatenate([[1-s.lam],rho]))
        full=lambda j: (1+0j) if j==0 else (c[j-1] if j>0 else np.conj(c[-j-1])) if abs(j)<=n else None
        g=[0.5*s.e*full(j-1)+0.5*np.conj(s.e)*full(j+1)-s.ch*full(j) for j in range(n)]
        T3=herm_toep(g)
        return T1,T2,T3
    def bound(s,which,v,box):
        # box: array shape (n,2,2): [j][0]=re interval, [j][1]=im interval
        n=s.n
        if which==0:
            S=Svec(v,n); return max_affine(S[0].real,S[1:],[box[j][0] for j in range(n)],[box[j][1] for j in range(n)])
        if which==1:
            S=Svec(v,n); tot=S[0].real*(1-s.lam)
            for j in range(n):
                rn,im_=ncube_bounds(tuple(box[j][0]),tuple(box[j][1]))
                # rho_j = n_j - lam ell_j
                rr=(rn[0]-s.lam*s.ell[j].real, rn[1]-s.lam*s.ell[j].real)
                ri=(im_[0]-s.lam*s.ell[j].imag, im_[1]-s.lam*s.ell[j].imag)
                a=S[j+1].real; b=-S[j+1].imag
                tot+=2*(max(a*rr[0],a*rr[1])+max(b*ri[0],b*ri[1]))
            return tot
        if which==2:
            # v^* T3 v = sum_j S'_j g_j (j=-(n-1)..n-1) = S'_0 g_0 + 2Re sum_{j>=1} S'_j g_j ; g affine in c
            m=len(v); Sp=Svec(v,m-1)
            # express as const + 2Re sum_k W_k c_k  (k=1..n) ; compute coefficients numerically by linearity
            # g_j = .5 e c_{j-1} + .5 conj(e) c_{j+1} - ch c_j ; with c_0=1, c_{-k}=conj(c_k)
            const=0.0; W=np.zeros(n,dtype=complex)
            # term j=0 (real): S'_0 * g_0, g_0 = .5 e conj(c_1) + .5 conj(e) c_1 - ch = Re(conj(e) c_1) - ch
            const+= Sp[0].real*(-s.ch); W[0]+= 0.5*Sp[0].real*np.conj(s.e)  # 2Re(W c) with W=.5 S0 conj(e) gives S0 Re(conj(e)c1)
            for j in range(1,m):
                # 2Re(S'_j g_j)
                # g_j contributions: .5 e c_{j-1}: if j-1==0 -> constant .5 e
                if j-1==0: const+=2*(Sp[j]*0.5*s.e).real
                else: W[j-2]+=Sp[j]*0.5*s.e
                if j+1<=n: W[j]+=Sp[j]*0.5*np.conj(s.e)
                W[j-1]+=-Sp[j]*s.ch
            return max_affine(const,W,[box[j][0] for j in range(n)],[box[j][1] for j in range(n)])
def run(n,h,lam,margin=1e-9,maxboxes=10**7,verbose=True):
    P=Prob(n,h,lam)
    root=np.array([[[-1.0,1.0],[-1.0,1.0]] for _ in range(n)])
    stack=[root]; leaves=[]; cnt=0; t0=time.time()
    while stack:
        box=stack.pop(); cnt+=1
        if cnt>maxboxes: return None,cnt,leaves
        # unit disk prune
        pruned=False
        for j in range(n):
            xr,yr=box[j]
            mx=0 if xr[0]<=0<=xr[1] else min(abs(xr[0]),abs(xr[1]))
            my=0 if yr[0]<=0<=yr[1] else min(abs(yr[0]),abs(yr[1]))
            if mx*mx+my*my>1+1e-12: pruned=True; leaves.append(('disk',box,j)); break
        if pruned: continue
        c=box[:,0,:].mean(1)+1j*box[:,1,:].mean(1)
        Ts=P.mats(c)
        ev=[np.linalg.eigh(T) for T in Ts]
        mins=[e[0][0] for e in ev]
        if min(mins)>=0:
            return ('FEASIBLE',c),cnt,leaves
        if (box[:,:,1]-box[:,:,0]).max()<1e-7 and min(mins)>-1e-6:
            return ('NEARFEASIBLE',c,min(mins)),cnt,leaves
        done=False
        for w in np.argsort(mins):
            if mins[w]>=0: break
            v=ev[w][1][:,0]
            if P.bound(w,v,box)< -margin:
                leaves.append(('vec',box,w,v)); done=True; break
        if done: continue
        # split widest coordinate
        widths=box[:,:,1]-box[:,:,0]
        j,k=np.unravel_index(np.argmax(widths),widths.shape)
        mid=box[j,k].mean()
        b1=box.copy(); b1[j,k,1]=mid; b2=box.copy(); b2[j,k,0]=mid
        stack.append(b1); stack.append(b2)
        if verbose and cnt%200000==0: print('boxes',cnt,'stack',len(stack),'t',round(time.time()-t0,1),flush=True)
    return 'INFEASIBLE',cnt,leaves
if __name__=='__main__':
    n=int(sys.argv[1]); h=float(sys.argv[2]); lam=float(sys.argv[3])
    t0=time.time()
    res,cnt,leaves=run(n,h,lam,maxboxes=int(sys.argv[4]) if len(sys.argv)>4 else 10**7)
    print(n,h,lam,res if not isinstance(res,tuple) else res,cnt,'leaves',len(leaves),'time',round(time.time()-t0,1))
