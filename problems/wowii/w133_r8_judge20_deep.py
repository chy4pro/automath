#!/usr/bin/env python3
"""S3 audit of draft section 20 -- deep inspection of the surviving frames.

Question: outside RES(b) the frame Z + {P?,Q?} + W admits Sigma_H(a-2) = 6 even
with ONE slot and |W| = 4.  Which section-20 claim is the first to break there,
and is it legitimately blocked by a RES(b) hypothesis?
"""
import sys, itertools
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (alldist, ecc_rad, avec, has_c4, connected, alpha)

U, U1, U2, ZV, Y, X = 0, 1, 2, 3, 4, 5
ZE = [(i, (i+1) % 6) for i in range(6)]
SLOTZ = {'P': (U1, Y), 'Q': (U2, X)}
LBL = ['u', 'u1', 'u2', 'z', 'y', 'x']


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


def build(occ, Wn, m, prs):
    adj = [set() for _ in range(6 + len(occ) + Wn)]
    for a, b in ZE:
        adj[a].add(b); adj[b].add(a)
    for i, s in enumerate(occ):
        for t in SLOTZ[s]:
            adj[6+i].add(t); adj[t].add(6+i)
    for i, (a, b) in enumerate(prs):
        if m >> i & 1:
            adj[a].add(b); adj[b].add(a)
    return adj


print("=" * 78)
print("Frames C4-free + connected + P6-free with the G13 hexagon: full census")
print("(no RES(b) filter). Reporting rad/diam/l/(R3b)/a-values and G34 status.")
print("=" * 78)
rows = []
for sub in range(4):
    occ = [s for i, s in enumerate(['P', 'Q']) if sub >> i & 1]
    for Wn in range(0, 5):
        nodes = list(range(6, 6 + len(occ) + Wn))
        prs = [(a, b) for i, a in enumerate(nodes) for b in nodes[i+1:]]
        for m in range(1 << len(prs)):
            adj = build(occ, Wn, m, prs)
            if has_c4(adj) or not connected(adj) or has_induced_pk(adj, 6):
                continue
            n = len(adj)
            D = alldist(adj)
            e, r = ecc_rad(D)
            av = avec(adj)
            H = [v for v in range(n) if av[v] >= 3]
            mass = sum(av[v]-2 for v in H)
            R3b = all(e[h] <= 2 for h in H)
            Wid = list(range(6+len(occ), n))
            Pidx = 6 + occ.index('P') if 'P' in occ else None
            Qidx = 6 + occ.index('Q') if 'Q' in occ else None
            # section-20 sub-claims
            wa2 = all(av[w] == 2 for w in Wid)
            wdist3 = all(D[w][U] == 3 and D[w][ZV] == 3 for w in Wid)
            aP = av[Pidx] if Pidx is not None else None
            aQ = av[Qidx] if Qidx is not None else None
            WP = [w for w in Wid if Pidx is not None and Pidx in adj[w]]
            WQ = [w for w in Wid if Qidx is not None and Qidx in adj[w]]
            rows.append(dict(occ=tuple(occ), Wn=Wn, n=n, rad=r, diam=max(e),
                             l=sum(av)/n, R3b=R3b, mass=mass, aP=aP, aQ=aQ,
                             wa2=wa2, wdist3=wdist3, WP=len(WP), WQ=len(WQ),
                             adj=[sorted(s) for s in adj], av=av, ecc=e))
print(f"  total admissible frames (C4-free, connected, P6-free): {len(rows)}")
print()
print("  Every frame, one line:")
hdr = ("   occ        |W|  n rad diam    l    R3b  Sig  a(P) a(Q) |W_P| |W_Q| "
       "a(w)=2 d(w,u)=d(w,z)=3")
print(hdr)
for R in sorted(rows, key=lambda r: (r['occ'], r['Wn'], -r['mass'])):
    print(f"   {str(R['occ']):10s} {R['Wn']}  {R['n']:2d}  {R['rad']}   "
          f"{R['diam']}  {R['l']:5.2f}  {str(R['R3b']):5s} {R['mass']:3d}  "
          f"{str(R['aP']):4s} {str(R['aQ']):4s}  {R['WP']}     {R['WQ']}    "
          f"{str(R['wa2']):5s}  {R['wdist3']}")

print()
print("=" * 78)
print("Which frames violate a section-20 conclusion, and what blocks them?")
print("=" * 78)
for R in rows:
    bad = []
    if R['aP'] is not None and R['aP'] > 3: bad.append(f"a(P)={R['aP']}>3 (G34c)")
    if R['aQ'] is not None and R['aQ'] > 3: bad.append(f"a(Q)={R['aQ']}>3 (G34c)")
    if R['WP'] > 1: bad.append(f"|W_P|={R['WP']}>1 (G34c)")
    if R['WQ'] > 1: bad.append(f"|W_Q|={R['WQ']}>1 (G34c)")
    if R['mass'] > 6: bad.append(f"mass={R['mass']}>6 (G35)")
    if not bad: continue
    blockers = []
    if R['rad'] != 2: blockers.append(f"rad={R['rad']}")
    if R['diam'] != 3: blockers.append(f"diam={R['diam']}")
    if R['l'] <= 3: blockers.append(f"l={R['l']:.2f}<=3")
    if not R['R3b']: blockers.append("(R3b) fails")
    if not R['wa2']: blockers.append("some a(w)!=2 (G26/G33)")
    print(f"   occ={R['occ']} |W|={R['Wn']} n={R['n']}: VIOLATES {bad}")
    print(f"       blocked by RES(b) hypotheses: {blockers}")
    print(f"       adj={R['adj']}  a={R['av']}  ecc={R['ecc']}")

print()
print("=" * 78)
print("Independent shortcut: diam<=3 forces every W-vertex adjacent to P or Q")
print("(N(u)={u1,x}; a 3-path w-?-?-u must use a neighbour of u1 or x off Z)")
print("=" * 78)
viol = 0
for R in rows:
    if R['diam'] > 3: continue
    if not R['wdist3']:
        viol += 1
        print("   *** W-vertex not at distance 3 from u/z in a diam-3 frame:", R['adj'])
print(f"   frames with diam <= 3: {sum(1 for R in rows if R['diam']<=3)}; "
      f"violations of 'every w in W has d(w,u)=d(w,z)=3': {viol}")
mx = max((R['n'] for R in rows if R['diam'] == 3 and R['rad'] == 2), default=None)
print(f"   largest n among frames with rad=2 and diam=3: {mx}   "
      f"(section 15.5 requires n >= 14 for l > 3)")
