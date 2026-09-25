#!/usr/bin/env python3
# Erdos #463 (Er92e form): F(n) = min_{m > n, m composite} (m - p(m)), p = least prime factor.
# Computes F(n) for n <= N, records of n - F(n), and the ratio (n - F(n))/sqrt(n). Internal time cap. std-lib only.
import sys, math, time
N=int(sys.argv[1]) if len(sys.argv)>1 else 10**6; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 1200
T0=time.time()
M=N+2*int(math.sqrt(N))*200+1000   # search window above N (heuristic; extended on demand)
lpf=list(range(M+1))
for p in range(2,int(M**0.5)+1):
    if lpf[p]==p:
        for q in range(p*p,M+1,p):
            if lpf[q]==q: lpf[q]=p
# For composite m: value m - lpf(m). F(n) = min over composite m>n. Sweep n downward with a suffix minimum.
sufmin=[10**18]*(M+2)
for m in range(M,1,-1):
    v = m-lpf[m] if lpf[m]!=m else 10**18
    sufmin[m]=min(v,sufmin[m+1])
out=open('problems/erdos463/F_records.txt','w'); out.write("# n F(n) n-F(n) (n-F(n))/sqrt(n)  [records of n-F(n)]\n")
best=-1; rec=0
for n in range(2,N+1):
    if time.time()-T0>CAP: out.write(f"# CAPPED at n={n}\n"); break
    F=sufmin[n+1]
    if F>=10**18: out.write(f"# window too small at n={n}\n"); break
    d=n-F
    if d>best: best=d; rec+=1; out.write(f"{n} {F} {d} {d/math.sqrt(n):.4f}\n")
out.write(f"# done N={N} records={rec} elapsed={time.time()-T0:.1f}s\n"); out.close()
print(open('problems/erdos463/F_records.txt').read()[-1500:])
