#!/usr/bin/env python3
"""Erdős #709: exact f(n) restricted to sets A with max(A) <= M, by brute force (Hall's condition via augmenting paths).
f_M(n) = max over n-subsets A of [2,M] of the least f such that every window of length f*max(A) admits distinct multiples.
Usage: python3 f_small.py n M"""
import sys, itertools, math
n=int(sys.argv[1]); M=int(sys.argv[2])
def matchable(A, x, L):
    # bipartite matching: elements of A -> multiples in (x, x+L]
    adj=[]
    for a in A:
        first=(x//a+1)*a; adj.append(list(range(first, x+L+1, a)))
    match={}
    def try_(i, seen):
        for v in adj[i]:
            if v in seen: continue
            seen.add(v)
            if v not in match or try_(match[v], seen):
                match[v]=i; return True
        return False
    return all(try_(i,set()) for i in range(len(A)))
def f_of(A):
    m=max(A); lcm=1
    for a in A: lcm=lcm*a//math.gcd(lcm,a)
    f=1
    while True:
        L=f*m
        if all(matchable(A,x,L) for x in range(lcm)): return f
        f+=1
worst=(0,None)
for A in itertools.combinations(range(2,M+1), n):
    v=f_of(A)
    if v>worst[0]: worst=(v,A); print("new max f =",v,"at A =",A, flush=True)
print(f"f_{M}({n}) = {worst[0]} attained at {worst[1]}")
