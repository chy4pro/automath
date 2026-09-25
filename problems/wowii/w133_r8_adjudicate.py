#!/usr/bin/env python3
"""w133 round 8 adjudication of the non-Qwen judge A report (S3 on 18/19).
Machine record for the three findings ADOPTED into the draft as 20.7."""
import sys
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import neighbours, avec, has_c4, alldist, ecc_rad

FAIL = 0
def check(c, m):
    global FAIL
    if not c:
        FAIL += 1; print("  *** ASSERT FAILED: " + m)

U, U1, U2, ZV, Y, X = range(6)
A, B, P, Q = 6, 7, 8, 9
ZE = [(U,U1),(U1,U2),(U2,ZV),(ZV,Y),(Y,X),(X,U)]
SZ = {A:(U1,U2), B:(Y,X), P:(U1,Y), Q:(U2,X)}
NM = {U:'u',U1:'u1',U2:'u2',ZV:'z',Y:'y',X:'x',A:'A',B:'B',P:'P',Q:'Q'}

def frame(occ, extra):
    adj = [set() for _ in range(10)]
    for a,b in ZE: adj[a].add(b); adj[b].add(a)
    for s in occ:
        for t in SZ[s]: adj[s].add(t); adj[t].add(s)
    for a,b in extra: adj[a].add(b); adj[b].add(a)
    return adj

def c4(adj, V):
    return [(NM[i],NM[j],[NM[k] for k in sorted(adj[i]&adj[j])])
            for i in V for j in V if i < j and len(adj[i]&adj[j]) >= 2]

print("=== judge-A finding 1: P~A, P~B, P~Q, Q~A, Q~B each force a C4 ===")
for tag, occ, ex in [("P~A",[A,P],[(P,A)]), ("P~B",[B,P],[(P,B)]), ("P~Q",[P,Q],[(P,Q)]),
                     ("Q~A",[A,Q],[(Q,A)]), ("Q~B",[B,Q],[(Q,B)])]:
    w = c4(frame(occ, ex), list(range(6))+occ)
    check(bool(w), f"{tag} does NOT force a C4")
    print(f"  {tag:5s} -> C4 witness {w[0]}")
print("  baseline (P,Q both present, no P-Q edge):",
      c4(frame([P,Q],[]), list(range(6))+[P,Q]) or "C4-free  => P !~ Q is the ONLY obstruction")
check(not c4(frame([P,Q],[]), list(range(6))+[P,Q]), "baseline P,Q frame is not C4-free")

print()
print("=== judge-A finding 2: A~B is NOT a C4 (the round-8 induced-P6 route is needed) ===")
w = c4(frame([A,B],[(A,B)]), list(range(6))+[A,B])
check(not w, "A~B unexpectedly forces a C4")
print(f"  A~B -> C4 witness {w or 'NONE'}  => (u,x,B,A,u2,z) induced-P6 route stands (draft 20.2)")

print()
print("=== consequence: with P !~ Q, N(P) = {u1,y} + W_P is EDGE-FREE, a(P) = d(P) ===")
adj = frame([P,Q],[])
check(Y not in adj[U1], "u1 ~ y on an induced C6")
check(Q not in adj[P], "P ~ Q survives")
print("  u1 !~ y (antipodal on an induced C6), u1,y !~ W (no Z-neighbour), P !~ Q")
print("  => a(P) = 2 + |W_P| <= 3 with |W_P| <= 1  (unchanged cap, simpler proof)")

print()
print("=== judge-A finding 3: G25(d) is NOT unconditional (label fix, no math change) ===")
print("  its proof consumes (R3b) for ecc(h)=2 and G24(b) for beta_q >= 1;")
print("  G24(b) is RES(b)-internal (it consumes (**) and l>3).  Recorded in draft 20.7.")
print("  G26 step (1) needs beta_p,beta_q >= 1 (G24(b)) for a(p)-2, a(q)-2 >= 0:")
for bp in range(1, 9):
    ep = bp // 2                      # e_p <= floor(beta_p/2) since N(p) is a matching
    check(bp - 1 - ep >= 0, f"a(p)-2 = beta_p-1-e_p < 0 at beta_p={bp}")
print("  verified beta_p - 1 - floor(beta_p/2) >= 0 for beta_p = 1..8   => the clause holds")

print()
print(f"TOTAL ASSERT FAILURES: {FAIL}")
sys.exit(1 if FAIL else 0)
