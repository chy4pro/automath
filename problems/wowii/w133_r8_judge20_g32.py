#!/usr/bin/env python3
"""S3 adversarial audit of draft section 20, joint J1/J2: Lemma G32 + Cor G32.1.

G32 as literally stated in the draft:
  "Let Z=(v0..v5) be an induced C6 in a graph with NO INDUCED P6.  Then every
   vertex outside Z has 0 or 2 neighbours on Z, and if 2, they are antipodal."
No C4-freeness is stated.  We hunt for counterexamples.
"""
import sys, itertools, random
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, hoffman_singleton, alpha)

def has_induced_pk(adj, k):
    n = len(adj)
    def ext(path, forb):
        if len(path) == k:
            return True
        last = path[-1]
        for w in adj[last]:
            if w in forb: continue
            if any(w in adj[p] for p in path[:-1]): continue
            if ext(path + [w], forb | {w}): return True
        return False
    for s in range(n):
        if ext([s], {s}): return True
    return False

ZE = [(i, (i+1) % 6) for i in range(6)]

def frames(k):
    """ALL graphs on 6+k vertices containing the fixed induced C6 on 0..5.
       (every graph on <=6+k vertices with an induced C6 is isomorphic to one)"""
    extra = list(range(6, 6+k))
    cross = [(e, z) for e in extra for z in range(6)]
    inner = [(a, b) for i, a in enumerate(extra) for b in extra[i+1:]]
    pairs = cross + inner
    for m in range(1 << len(pairs)):
        adj = [set() for _ in range(6+k)]
        for a, b in ZE:
            adj[a].add(b); adj[b].add(a)
        for i, (a, b) in enumerate(pairs):
            if m >> i & 1:
                adj[a].add(b); adj[b].add(a)
        yield adj

def g32_violation(adj, c4free_required):
    """returns list of (v, sorted Z-neighbour positions) violating G32"""
    bad = []
    for v in range(6, len(adj)):
        S = sorted(adj[v] & set(range(6)))
        if len(S) not in (0, 2):
            bad.append((v, S, 'count'))
        elif len(S) == 2:
            i, j = S
            cd = min((j-i) % 6, (i-j) % 6)
            if cd != 3:
                bad.append((v, S, f'cycdist{cd}'))
    return bad

print("="*74)
print("J1: G32 WITHOUT C4-freeness -- exhaustive hunt, |V| = 7 and 8")
print("="*74)
for k in (1, 2):
    tot = p6free = viol_cnt = 0
    first = {}
    for adj in frames(k):
        tot += 1
        if has_induced_pk(adj, 6):
            continue
        p6free += 1
        bad = g32_violation(adj, False)
        if bad:
            viol_cnt += 1
            for (v, S, why) in bad:
                key = (why, tuple(S))
                if key not in first:
                    first[key] = ([sorted(x) for x in
                                   [list(a) for a in adj]], v, S)
    print(f"  n={6+k}: {tot} labelled graphs w/ the fixed induced C6, "
          f"{p6free} of them P6-free, {viol_cnt} violate G32-as-stated")
    for key, (A, v, S) in sorted(first.items())[:8]:
        print(f"    violation type {key}: vertex {v}, Z-nbrs {S}, adj={A}")

print()
print("="*74)
print("J1(e): G32 WITH C4-freeness -- exhaustive, up to 3 off-cycle vertices")
print("="*74)
for k in (1, 2, 3):
    tot = kept = viol = 0
    for adj in frames(k):
        tot += 1
        if has_c4(adj): continue
        if has_induced_pk(adj, 6): continue
        kept += 1
        bad = g32_violation(adj, True)
        if bad:
            viol += 1
            print("   *** COUNTEREXAMPLE", bad, [sorted(a) for a in adj])
    print(f"  n={6+k}: {tot} frames, {kept} C4-free & P6-free, G32 violations = {viol}")

print()
print("="*74)
print("J1: does the '0 or 2' part alone need C4-freeness?  explicit witnesses")
print("="*74)
for name, S in [("w ~ v0,v2 (cyclic distance 2)", [0, 2]),
                ("w ~ v0,v2,v4 (three nbrs)", [0, 2, 4]),
                ("w ~ v0,v1,v3 ", [0, 1, 3]),
                ("w ~ v0,v1,v2,v3,v4,v5 (dominating)", [0,1,2,3,4,5]),
                ("w ~ v0 only (one nbr)", [0])]:
    adj = [set() for _ in range(7)]
    for a, b in ZE:
        adj[a].add(b); adj[b].add(a)
    for z in S:
        adj[6].add(z); adj[z].add(6)
    print(f"  {name:42s} P6-free={not has_induced_pk(adj,6):5}  "
          f"C4-free={not has_c4(adj):5}  G32-holds={not g32_violation(adj,False)}")

print()
print("="*74)
print("J2: Corollary G32.1 on real C4-free P6-free graphs with an induced C6")
print("="*74)
# exhaustive over C4-free P6-free frames with <=3 extra vertices: check
#   a(v_i) = 2 + [antipodal slot occupied],  and slot has <= 1 vertex
bad_mass = bad_slot = 0
inst = 0
occ_inst = 0
for k in (1, 2, 3):
    for adj in frames(k):
        if has_c4(adj) or has_induced_pk(adj, 6): continue
        av = avec(adj)
        for i in range(6):
            slot = [v for v in range(6, len(adj))
                    if adj[v] & set(range(6)) == {i, (i+3) % 6}]
            if len(slot) > 1: bad_slot += 1
            inst += 1
            if slot: occ_inst += 1
            if av[i] != 2 + (1 if slot else 0):
                bad_mass += 1
                print("   *** MASS IDENTITY FAILS", i, av, [sorted(a) for a in adj])
print(f"  {inst} mass-identity instances ({occ_inst} with occupied slot); "
      f"failures: mass {bad_mass}, slot-multiplicity {bad_slot}")

print()
print("="*74)
print("J2: is C4-freeness needed for G32.1?  (P6-free only)")
print("="*74)
cnt = 0
for k in (1, 2):
    for adj in frames(k):
        if has_induced_pk(adj, 6): continue
        av = avec(adj)
        for i in range(6):
            slot = [v for v in range(6, len(adj))
                    if adj[v] & set(range(6)) == {i, (i+3) % 6}]
            if av[i] != 2 + (1 if slot else 0):
                cnt += 1
                if cnt <= 3:
                    print(f"    G32.1 fails w/o C4-freeness: v{i}, a={av[i]}, "
                          f"slot={slot}, adj={[sorted(a) for a in adj]}")
print(f"  total G32.1 failures among P6-free (not nec. C4-free) frames: {cnt}")
