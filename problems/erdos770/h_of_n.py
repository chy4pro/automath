#!/usr/bin/env python3
# Erdos #770 (corrected reading): h(n) = minimal h such that gcd(2^n-1, 3^n-1, ..., h^n-1) = 1 ("mutually coprime" =
# collective gcd 1). Compare with P(n) = greatest prime p with (p-1) | n. Also record the collective gcd G(n) of
# 2^n-1..(h-1)^n-1 at the last step. Internal cap; std-lib.
import sys, math, time
N=int(sys.argv[1]) if len(sys.argv)>1 else 1000; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 900; T0=time.time()
def is_prime(p): return p>1 and all(p%q for q in range(2,int(p**0.5)+1))
def Pn(n): return max([d+1 for d in range(1,n+1) if n%d==0 and is_prime(d+1)], default=0)
out=open('problems/erdos770/h_table.txt','w'); out.write("# n h(n)=min h with gcd(2^n-1,...,h^n-1)=1 | P(n)=greatest prime p with p-1|n | h==P | gcd before last step\n")
agree=0; tot=0; mism=[]
for n in range(1,N+1):
    if time.time()-T0>CAP: out.write(f"# CAPPED at n={n}\n"); break
    g=0; h=1
    while True:
        h+=1; g=math.gcd(g, pow(h,n)-1) if g else pow(h,n)-1
        if g==1: break
        last=g
    P=Pn(n); tot+=1; agree+=(h==P)
    if h!=P: mism.append((n,h,P))
    out.write(f"{n} {h} {P} {h==P} {last if h>2 else '-'}\n")
out.write(f"# done N={N} h==P agreement {agree}/{tot}; mismatches (n,h,P): {mism[:80]}\n# elapsed={time.time()-T0:.1f}s\n"); out.close()
t=open('problems/erdos770/h_table.txt').read(); print(t[:700]); print('...'); print(t[-900:])
