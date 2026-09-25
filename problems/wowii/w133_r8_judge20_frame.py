#!/usr/bin/env python3
"""S3 adversarial audit of draft section 20, joints J3-J8.

Frame:  Z = (u,u1,u2,z,y,x) = positions 0..5 of an induced C6.
Slots:  u1'=(u,u1), A=(u1,u2), u2'=(u2,z), (z,y), B=(y,x), (x,u), (u,z),
        P=(u1,y), Q=(u2,x);  W = vertices with no Z-neighbour.
"""
import sys, itertools
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, alpha)

U, U1, U2, ZV, Y, X = 0, 1, 2, 3, 4, 5
NAME = {0: 'u', 1: 'u1', 2: 'u2', 3: 'z', 4: 'y', 5: 'x'}
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


def base(nextra):
    adj = [set() for _ in range(6 + nextra)]
    for a, b in ZE:
        adj[a].add(b); adj[b].add(a)
    return adj


print("=" * 74)
print("J3: the four G33 witness P6s -- explicit edge / non-edge audit")
print("=" * 74)
# slot vertex 6 attached to the two named Z-positions; the witness is checked
# ONLY from the induced-C6 relations + 'slot has exactly two Z-neighbours'.
WIT = {
    "u1' = (u,u1)": ((U, U1), ['u1p', 'u', 'x', 'y', 'z', 'u2'], [6, U, X, Y, ZV, U2]),
    "u2' = (u2,z)": ((U2, ZV), ['u2p', 'z', 'y', 'x', 'u', 'u1'], [6, ZV, Y, X, U, U1]),
    "A = (u1,u2)":  ((U1, U2), ['A', 'u1', 'u', 'x', 'y', 'z'], [6, U1, U, X, Y, ZV]),
    "B = (y,x)":    ((Y, X),   ['B', 'x', 'u', 'u1', 'u2', 'z'], [6, X, U, U1, U2, ZV]),
}
for tag, (zn, labels, seq) in WIT.items():
    adj = base(1)
    for t in zn:
        adj[6].add(t); adj[t].add(6)
    edges = [(labels[i], labels[i+1], seq[i+1] in adj[seq[i]]) for i in range(5)]
    nonedges = [(labels[i], labels[j], seq[j] not in adj[seq[i]])
                for i in range(6) for j in range(i+2, 6)]
    ok = all(e[2] for e in edges) and all(e[2] for e in nonedges)
    print(f"  {tag:14s} witness {'-'.join(labels)}")
    print(f"     5 edges    : {[(a,b) for a,b,v in edges]}   all present: "
          f"{all(v for _,_,v in edges)}")
    print(f"     10 nonedges: all absent: {all(v for _,_,v in nonedges)}"
          f"   [{len(nonedges)} checked]")
    print(f"     => induced P6 present: {ok};  frame P6-free? "
          f"{not has_induced_pk(adj,6)};  frame C4-free? {not has_c4(adj)}")

print()
print("=" * 74)
print("J3/J4: consecutive slot dies for EVERY edge pattern on the other slots")
print("=" * 74)
# all six consecutive slots + the three antipodal ones, arbitrary extra structure
SLOTS = {"u1'": (U, U1), "A": (U1, U2), "u2'": (U2, ZV), "(z,y)": (ZV, Y),
         "B": (Y, X), "(x,u)": (X, U), "P": (U1, Y), "Q": (U2, X)}
KEYS = list(SLOTS)
for tgt in ["u1'", "A", "u2'", "B", "(z,y)", "(x,u)"]:
    tot = c4free = withp6 = 0
    others = [k for k in KEYS if k != tgt]
    for sub in range(1 << len(others)):
        if bin(sub).count('1') > 3:      # cap: <= 4 slot vertices at a time
            continue
        occ = [tgt] + [others[i] for i in range(len(others)) if sub >> i & 1]
        prs = [(a, b) for i, a in enumerate(range(6, 6+len(occ)))
               for b in range(6+i+1, 6+len(occ))]
        for m in range(1 << len(prs)):
            adj = base(len(occ))
            for i, s in enumerate(occ):
                for t in SLOTS[s]:
                    adj[6+i].add(t); adj[t].add(6+i)
            for i, (a, b) in enumerate(prs):
                if m >> i & 1:
                    adj[a].add(b); adj[b].add(a)
            tot += 1
            if has_c4(adj): continue
            c4free += 1
            if has_induced_pk(adj, 6): withp6 += 1
    print(f"  slot {tgt:6s}: {tot} frames, {c4free} C4-free, "
          f"{withp6} of those contain an induced P6  "
          f"=> slot dies under (C6): {withp6 == c4free}")

print()
print("=" * 74)
print("J4-J8: FULL frame enumeration Z + {P?,Q?} + W (|W| <= 4), no filters")
print("=" * 74)
best = {}
report = []
for sub in range(4):
    occ = [s for i, s in enumerate(['P', 'Q']) if sub >> i & 1]
    for Wn in range(0, 5):
        nodes = list(range(6, 6 + len(occ) + Wn))
        prs = [(a, b) for i, a in enumerate(nodes) for b in nodes[i+1:]]
        kept = res = 0
        maxmass = -1
        maxn = 0
        bigW = 0
        for m in range(1 << len(prs)):
            adj = base(len(occ) + Wn)
            for i, s in enumerate(occ):
                for t in SLOTS[s]:
                    adj[6+i].add(t); adj[t].add(6+i)
            for i, (a, b) in enumerate(prs):
                if m >> i & 1:
                    adj[a].add(b); adj[b].add(a)
            if has_c4(adj) or not connected(adj): continue
            if has_induced_pk(adj, 6): continue
            kept += 1
            n = len(adj)
            D = alldist(adj)
            e, r = ecc_rad(D)
            av = avec(adj)
            H = [v for v in range(n) if av[v] >= 3]
            mass = sum(av[v] - 2 for v in H)
            maxmass = max(maxmass, mass)
            # RES(b) test
            R3b = all(e[h] <= 2 for h in H)
            if r == 2 and max(e) == 3 and sum(av) > 3*n and R3b:
                res += 1
            # sanity: is every W vertex adjacent to P or Q?
            Wid = list(range(6+len(occ), n))
            if max(e) == 3 and any(not (adj[w] & set(range(6, 6+len(occ)))) for w in Wid):
                bigW += 1
        report.append((tuple(occ), Wn, kept, maxmass, res, bigW))
print("  occ        |W| kept  maxSigma_H(a-2)  #in-RES(b)  #diam3-frames-with-"
      "a-W-vertex-missing-P/Q")
for occ, Wn, kept, mm, res, bigW in report:
    print(f"  {str(occ):11s} {Wn}  {kept:5d}   {mm:6d}          {res:4d}        {bigW}")

print()
print("=" * 74)
print("J8: the arithmetic recomputed independently")
print("=" * 74)
for P in (0, 1):
    for Q in (0, 1):
        caps = {'u1': 2 + P, 'u2': 2 + Q, 'x': 2 + Q, 'y': 2 + P}
        mass = sum(c - 2 for c in caps.values())
        if P: mass += 1      # a(P) <= 3
        if Q: mass += 1
        nmin = 6 + P + Q
        print(f"  [P]={P} [Q]={Q}:  Sigma_H(a-2) <= {mass};  n >= {nmin};  "
              f"(**) needs Sigma > n i.e. >= {nmin+1}: "
              f"{'CONTRADICTION' if mass <= nmin else 'NO CONTRADICTION'}")
print("  draft's claimed bound 3[P]+3[Q] <= 6 :",
      max(3*P + 3*Q for P in (0,1) for Q in (0,1)))
