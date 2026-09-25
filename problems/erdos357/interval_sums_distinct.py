#!/usr/bin/env python3
# Erdos #357 (Erdos-Harzheim): f(n) = max k such that there are 1 <= a_1 < ... < a_k <= n with all sums of
# consecutive blocks a_u + ... + a_v (u <= v) pairwise distinct. Exact branch-and-bound DFS. Internal time cap.
import sys, time
N_MAX=int(sys.argv[1]) if len(sys.argv)>1 else 30; CAP=float(sys.argv[2]) if len(sys.argv)>2 else 3000
T0=time.time()
def f(n, lower):
    # returns (best_k, example) ; prune if cannot beat 'lower'
    best=[lower, None]
    seq=[]; sums=set(); suffix=[]   # suffix[i] = sum of seq[i:] (block sums ending at last element)
    def dfs(start):
        if time.time()-T0>CAP: return
        k=len(seq)
        # upper bound: remaining numbers available start..n
        if k+(n-start+1)<=best[0]: return
        for a in range(start,n+1):
            if k+(n-a+1)<=best[0]: break
            # new block sums: a + each suffix sum, and a itself
            new=[a]+[s+a for s in suffix]
            if len(set(new))!=len(new) or any(s in sums for s in new): continue
            seq.append(a); suffix_old=suffix[:]; 
            for s in new: sums.add(s)
            suffix[:]=new  # suffix sums now end at a: [a, seq[-2]+a, ...]
            if len(seq)>best[0]: best[0]=len(seq); best[1]=seq[:]
            dfs(a+1)
            suffix[:]=suffix_old
            for s in new: sums.discard(s)
            seq.pop()
    dfs(1)
    return best
out=open('problems/erdos357/f_table.txt','w'); out.write("# n f(n) example\n"); prev=0
for n in range(1,N_MAX+1):
    k,ex=f(n, prev-1 if prev>0 else 0)
    if time.time()-T0>CAP: out.write(f"# CAPPED before completing n={n}\n"); break
    prev=k; out.write(f"{n} {k} {ex}\n"); out.flush()
out.write(f"# elapsed={time.time()-T0:.0f}s\n"); out.close(); print(open('problems/erdos357/f_table.txt').read())
