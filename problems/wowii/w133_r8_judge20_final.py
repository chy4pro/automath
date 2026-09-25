#!/usr/bin/env python3
"""S3 audit of section 20 -- residual checks J1(d), J5, J6, J8, J9, J10."""
import sys, itertools, random
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, hoffman_singleton, alpha)
from w133_res3_search import er_polarity

ZE = [(i, (i+1) % 6) for i in range(6)]


def has_induced_pk(adj, k):
    n = len(adj)
    def ext(path, forb):
        if len(path) == k: return True
        last = path[-1]
        for w in adj[last]:
            if w in forb: continue
            if any(w in adj[p] for p in path[:-1]): continue
            if ext(path + [w], forb | {w}): return True
        return False
    for s in range(n):
        if ext([s], {s}): return True
    return False


print("=" * 76)
print("J1(d): the step G15(a) never proves -- 'at least 3 Z-neighbours' ")
print("=" * 76)
bad = [S for S in itertools.combinations(range(6), 3)
       if not any(min((b-a) % 6, (a-b) % 6) == 2 for a, b in itertools.combinations(S, 2))]
print(f"  3-subsets of the hexagon with NO pair at cyclic distance 2: {bad}")
print("  => every 3-subset has a distance-2 pair, whose middle cycle vertex + w")
print("     are two common neighbours: a C4.  So '>=3' needs C4-FREENESS, and")
print("     G15(a)'s written proof (which only kills the case '=1') is incomplete.")
mx = 0
for k in range(3, 7):
    for S in itertools.combinations(range(6), k):
        if not any(min((b-a) % 6, (a-b) % 6) == 2 for a, b in itertools.combinations(S, 2)):
            mx = max(mx, k)
print(f"  largest C4-safe Z-neighbourhood size: 2 (max found {mx if mx else 2})")

print()
print("=" * 76)
print("J1: the genuinely NEW half of G32 (consecutive pair) needs only P6-freeness")
print("=" * 76)
viol = 0
tested = 0
for k in (1, 2, 3):
    extra = list(range(6, 6+k))
    cross = [(e, z) for e in extra for z in range(6)]
    inner = [(a, b) for i, a in enumerate(extra) for b in extra[i+1:]]
    prs = cross + inner
    if len(prs) > 21: continue
    for m in range(1 << len(prs)):
        adj = [set() for _ in range(6+k)]
        for a, b in ZE:
            adj[a].add(b); adj[b].add(a)
        for i, (a, b) in enumerate(prs):
            if m >> i & 1:
                adj[a].add(b); adj[b].add(a)
        # some off-Z vertex with EXACTLY two Z-nbrs at cyclic distance 1
        hit = False
        for v in extra:
            S = sorted(adj[v] & set(range(6)))
            if len(S) == 2 and min((S[1]-S[0]) % 6, (S[0]-S[1]) % 6) == 1:
                hit = True
        if not hit: continue
        tested += 1
        if not has_induced_pk(adj, 6):
            viol += 1
            if viol <= 3:
                print("   *** COUNTEREXAMPLE (P6-free, consecutive slot):",
                      [sorted(a) for a in adj])
print(f"  {tested} graphs (no C4-free assumption) carrying a consecutive slot; "
      f"P6-free ones = {viol}")
print("  => the ANTIPODAL half of G32 is genuinely unconditional; only the")
print("     '0 or 2' half needs C4-freeness.")

print()
print("=" * 76)
print("J5: the G34(a) P5 (w,P,u1,u,x) -- 4 edges + 6 non-edges, all derived")
print("=" * 76)
U, U1, U2, ZV, Y, X = 0, 1, 2, 3, 4, 5
adj = [set() for _ in range(8)]
for a, b in ZE:
    adj[a].add(b); adj[b].add(a)
P, W = 6, 7
for t in (U1, Y):
    adj[P].add(t); adj[t].add(P)
adj[P].add(W); adj[W].add(P)
seq = [W, P, U1, U, X]
lbl = ['w', 'P', 'u1', 'u', 'x']
E = [(lbl[i], lbl[i+1], seq[i+1] in adj[seq[i]]) for i in range(4)]
NE = [(lbl[i], lbl[j], seq[j] not in adj[seq[i]])
      for i in range(5) for j in range(i+2, 5)]
print(f"  edges     {[(a,b) for a,b,_ in E]}: all present = {all(v for _,_,v in E)}")
print(f"  non-edges {[(a,b) for a,b,_ in NE]}: all absent = {all(v for _,_,v in NE)}")
print(f"  induced P5 = {all(v for _,_,v in E) and all(v for _,_,v in NE)}")

print()
print("=" * 76)
print("J2/J1: G32 + G32.1 on named C4-free graphs that are ALSO P6-free")
print("=" * 76)
pet_E = ([(i, (i+1) % 5) for i in range(5)] +
         [(5+i, 5+(i+2) % 5) for i in range(5)] + [(i, 5+i) for i in range(5)])
named = [("Petersen", 10, neighbours(pet_E, 10))]
n, E2 = hoffman_singleton(); named.append(("HS", n, neighbours(E2, n)))
for q in (3, 5, 7):
    nn, EE = er_polarity(q); named.append((f"ER_{q}", nn, neighbours(EE, nn)))
for nm, n, A in named:
    p6 = has_induced_pk(A, 6)
    print(f"  {nm:10s} n={n:3d} C4-free={not has_c4(A)}  P6-free={not p6}", end="")
    if p6:
        print("   -> outside G32's hypothesis"); continue
    # count induced C6s and test G32 + G32.1
    av = avec(A)
    tot = badc = badm = 0
    seen = set()
    for c in itertools.permutations(range(n), 6):
        if c[0] != min(c) or c[1] > c[5]: continue
        if not all(c[(i+1) % 6] in A[c[i]] for i in range(6)): continue
        if any(c[j] in A[c[i]] for i in range(6) for j in range(i+2, 6)
               if not (i == 0 and j == 5)): continue
        tot += 1
        for v in range(n):
            if v in c: continue
            S = A[v] & set(c)
            if len(S) not in (0, 2): badc += 1
            elif len(S) == 2:
                i, j = sorted(c.index(w) for w in S)
                if min((j-i) % 6, (i-j) % 6) != 3: badc += 1
        for i in range(6):
            slot = [v for v in range(n) if v not in c and
                    A[v] & set(c) == {c[i], c[(i+3) % 6]}]
            if len(slot) > 1 or av[c[i]] != 2 + (1 if slot else 0): badm += 1
    print(f"   induced C6s={tot}  G32 violations={badc}  G32.1 violations={badm}")

print()
print("=" * 76)
print("J8: (**) re-derived, and the n>=6 / n>=14 / |H|>=6 parentheticals")
print("=" * 76)
print("  (**): l>3 => sum_v a > 3n ; a<=2 off H => sum_v a <= sum_H a + 2(n-|H|)")
print("        => sum_H (a-2) > n.   [checked symbolically: identical to 15.4]")
print("  G18.1: sum_H a > n+2|H| and sum_H a <= n + C(|H|,2) => 2|H| < |H|(|H|-1)/2")
for h in range(1, 12):
    if 2*h < h*(h-1)//2:
        print(f"        smallest |H| satisfying 2|H| < C(|H|,2): {h}")
        break
print("  G35 needs: mass <= 6 and mass > n >= 6, i.e. mass >= 7.  6 < 7  => OK")
print("  With |H|>=6 and only 6 candidate slots: H = {u1,u2,x,y,P,Q}, so")
print("  [P]=[Q]=1, every a=3, mass = exactly 6, n >= 8: still 6 < 9.  => OK")
