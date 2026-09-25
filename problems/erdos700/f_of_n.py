#!/usr/bin/env python3
# Erdos #700: f(n) = min_{1<k<=n/2} gcd(n, C(n,k)). Characterise composite n with f(n) = n/P(n) (P = largest prime factor);
# count composite n with f(n) > sqrt(n). Internal cap. std-lib.
import sys, math, time
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 900; T0=time.time()
def P(n):
    d=2; last=1
    while d*d<=n:
        while n%d==0: last=d; n//=d
        d+=1
    return max(last,n) if n>1 else last
out=open('problems/erdos700/f_table.txt','w'); out.write("# n f(n) n/P(n) f==n/P  f>sqrt(n)  [composite n only]\n")
eq=[]; big=[]
for n in range(4,N+1):
    if time.time()-T0>CAP: out.write(f"# CAPPED at n={n}\n"); break
    if all(n%q for q in range(2,int(n**0.5)+1)): continue
    f=n; c=1
    for k in range(1,n//2+1):
        c=c*(n-k+1)//k
        if k>1:
            g=math.gcd(n,c)
            if g<f: f=g
            if f==1: break
    q=n//P(n); e=(f==q); b=(f*f>n)
    if e: eq.append(n)
    if b: big.append((n,f))
    out.write(f"{n} {f} {q} {e} {b}\n")
out.write(f"# composite n with f(n)=n/P(n): {eq}\n# composite n with f(n)>sqrt(n): {big}\n# elapsed={time.time()-T0:.1f}s\n"); out.close()
print("f(n)=n/P(n) for composite n:", eq[:60]); print("f(n)>sqrt(n):", big[:40]); print("elapsed", round(time.time()-T0,1))
