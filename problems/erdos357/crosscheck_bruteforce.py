#!/usr/bin/env python3
# Independent brute force for Erdos #357: enumerate ALL subsets of [1,n] (n <= 22) by increasing size from the top,
# check the all-block-sums-distinct property directly, report f(n). Also verifies the example sets in f_table*.txt.
import sys, itertools, time, ast
def ok(seq):
    seen=set()
    for u in range(len(seq)):
        s=0
        for v in range(u,len(seq)):
            s+=seq[v]
            if s in seen: return False
            seen.add(s)
    return True
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 22; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 1500; T0=time.time()
res={}
for n in range(1,NMAX+1):
    found=None
    for k in range(n,0,-1):
        for c in itertools.combinations(range(1,n+1),k):
            if ok(c): found=k; break
        if found or time.time()-T0>CAP: break
    if time.time()-T0>CAP: print("CAPPED at n",n); break
    res[n]=found; print(n,found,flush=True)
# verify examples from the DFS table
bad=0
for line in open('problems/erdos357/f_table_n34.txt'):
    if line.startswith('#') or not line.strip(): continue
    n,k,ex=line.split(' ',2); ex=ast.literal_eval(ex.strip())
    if not (ok(ex) and len(ex)==int(k) and max(ex)<=int(n)): bad+=1; print("BAD example", line.strip())
    if int(n) in res and res[int(n)]!=int(k): bad+=1; print("MISMATCH n=",n,"dfs",k,"brute",res[int(n)])
print("examples verified; mismatches/bad:",bad)
