#!/usr/bin/env python3
"""w133 round-9 slice-2, DEFECT 6: §20.8 item 8 asserts "every admissible frame has
n <= 11 and l <= 2.67" but w133_r8_q61.py section (D) NEVER computes l.  This script
re-runs exactly that enumeration and computes l = (1/n) sum_v a(v) on every admissible
frame.  If l <= 3 on all of them, Remark G35.2's second, (**)-free kill is REINSTATED
(as a finite-frame check, which is what the Q19 pass asked for).  NO SAT."""
import sys
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import avec, has_c4, connected

def has_induced_pk(adj, k):
    def ext(path, forb):
        if len(path) == k: return True
        last = path[-1]
        for w in adj[last]:
            if w in forb: continue
            if any(w in adj[p] for p in path[:-1]): continue
            if ext(path + [w], forb | {w}): return True
        return False
    return any(ext([s], {s}) for s in range(len(adj)))

U, U1, U2, ZV, Y, X = 0, 1, 2, 3, 4, 5
P_, Q_ = 10, 11
Zc = (U, U1, U2, ZV, Y, X)
ZEDGES = [(U, U1), (U1, U2), (U2, ZV), (ZV, Y), (Y, X), (X, U)]
SLOTZ = {P_: (U1, Y), Q_: (U2, X)}

def build(occ, Wn, edgemask, extra_pairs):
    verts = list(Zc) + occ + list(range(100, 100 + Wn))
    idx = {v: i for i, v in enumerate(verts)}
    adj = [set() for _ in verts]
    for a, b in ZEDGES:
        adj[idx[a]].add(idx[b]); adj[idx[b]].add(idx[a])
    for s in occ:
        for t in SLOTZ[s]:
            adj[idx[s]].add(idx[t]); adj[idx[t]].add(idx[s])
    for i, (a, b) in enumerate(extra_pairs):
        if edgemask >> i & 1:
            adj[idx[a]].add(idx[b]); adj[idx[b]].add(idx[a])
    return adj, idx, verts

print("=== (D') admissible frames of §20.4/G35.2, with l computed ===")
rows, maxl, kept = [], -1.0, 0
for sub in range(1 << 2):
    occ = [s for i, s in enumerate([P_, Q_]) if sub >> i & 1]
    for Wn in (0, 1, 2, 3):
        nodes = occ + list(range(100, 100 + Wn))
        free = [(a, b) for i, a in enumerate(nodes) for b in nodes[i + 1:]]
        for m in range(1 << len(free)):
            adj, idx, verts = build(occ, Wn, m, free)
            if has_c4(adj) or not connected(adj): continue
            if has_induced_pk(adj, 6): continue
            av = avec(adj)
            Wid = [idx[v] for v in range(100, 100 + Wn)]
            if any(av[w] != 2 for w in Wid): continue
            kept += 1
            n = len(adj); S = sum(av); l = S / n
            maxl = max(maxl, l)
            rows.append((sorted('PQ'[s == Q_] for s in occ), Wn, n, S, round(l, 4)))
print(f"  admissible frames kept: {kept}   (round-8 log says 5)")
for r in sorted(set(map(str, rows))):
    print("   ", r)
print(f"  MAX l over all admissible frames: {maxl}")
ok = kept == 5 and maxl <= 3.0
print(f"  l > 3 required by RES(b);  max realised l = {maxl}  ==> "
      f"{'NO admissible frame satisfies l > 3: G35.2 kill REINSTATED' if ok else 'INCONCLUSIVE'}")
print(f"=== TOTAL FAILURES: {0 if ok else 1} ===")
sys.exit(0 if ok else 2)
