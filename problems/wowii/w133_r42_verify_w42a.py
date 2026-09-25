#!/usr/bin/env python3
"""WOWII-133 round 42, THIRD script -- INDEPENDENT VERIFICATION OF WITNESS W42a.

This file shares NO code with the builder.  One thing came from the builder: the EDGE
LIST.  Everything else -- adjacency, distances, independence numbers, C4-freeness -- is
written here from scratch and deliberately in a different style: distances by repeated
matrix relaxation (no BFS queue), alpha by exhaustive subset enumeration over the
neighbourhood (no matching formula), C4-freeness by counting common neighbours in a
nested loop.

CLAIM UNDER TEST (draft 42.4's residual row, inside route A2's class):
  G connected, C4-free in this line's sense (no two vertices have two common neighbours),
  mu(G) = min_v alpha(G[N(v)]) >= 2, l(G) = mean_v alpha(G[N(v)]) > 4, rad(G) >= 5, and
  some vertex w has ecc(w) = rad+1 and is at distance exactly rad from EVERY centre.

Interpreter: system python3 (pure stdlib).
"""
import sys
from itertools import combinations

N = 96
EDGES = [(0, 14), (0, 17), (0, 20), (0, 23), (0, 28), (1, 13), (1, 17), (1, 18), (1, 19), (1, 26), (2, 32), (2, 16), (2, 17), (2, 22), (2, 24), (3, 37), (3, 15), (3, 17), (3, 21), (3, 87), (3, 25), (4, 13), (4, 14), (4, 15), (4, 16), (4, 27), (5, 33), (5, 14), (5, 19), (5, 22), (5, 25), (6, 36), (6, 14), (6, 18), (6, 21), (6, 24), (7, 35), (7, 13), (7, 23), (7, 24), (7, 25), (8, 16), (8, 82), (8, 19), (8, 21), (8, 23), (8, 30), (9, 34), (9, 15), (9, 18), (9, 22), (9, 23), (10, 13), (10, 20), (10, 21), (10, 22), (10, 84), (10, 29), (11, 38), (11, 15), (11, 19), (11, 20), (11, 24), (12, 16), (12, 18), (12, 20), (12, 25), (12, 31), (26, 34), (26, 36), (26, 38), (26, 51), (27, 33), (27, 36), (27, 37), (28, 35), (28, 36), (28, 39), (28, 49), (29, 33), (29, 34), (29, 35), (29, 47), (30, 34), (30, 37), (30, 39), (31, 33), (31, 38), (31, 39), (32, 35), (32, 37), (32, 38), (40, 48), (40, 50), (40, 52), (40, 60), (41, 50), (41, 51), (41, 54), (41, 47), (42, 49), (42, 50), (42, 53), (42, 62), (43, 48), (43, 49), (43, 64), (43, 47), (44, 48), (44, 65), (44, 51), (44, 53), (45, 56), (45, 52), (45, 53), (45, 47), (46, 49), (46, 66), (46, 51), (46, 52), (54, 64), (54, 66), (54, 62), (55, 64), (55, 65), (55, 61), (55, 71), (56, 64), (56, 67), (56, 70), (56, 63), (57, 61), (57, 62), (57, 63), (58, 80), (58, 65), (58, 67), (58, 62), (59, 66), (59, 67), (59, 61), (60, 65), (60, 66), (60, 63), (68, 80), (68, 90), (68, 76), (68, 78), (69, 75), (69, 92), (69, 78), (69, 79), (70, 77), (70, 78), (70, 81), (70, 82), (71, 75), (71, 76), (71, 77), (71, 87), (72, 88), (72, 81), (72, 76), (72, 79), (73, 80), (73, 81), (73, 75), (73, 84), (74, 80), (74, 77), (74, 94), (74, 79), (82, 90), (82, 92), (82, 94), (83, 89), (83, 92), (83, 93), (84, 91), (84, 92), (84, 95), (85, 89), (85, 90), (85, 91), (86, 90), (86, 93), (86, 95), (87, 89), (87, 94), (87, 95), (88, 91), (88, 93), (88, 94)]


def neighbours():
    g = [[] for _ in range(N)]
    for (u, v) in EDGES:
        assert 0 <= u < N and 0 <= v < N and u != v
        if v not in g[u]:
            g[u].append(v)
        if u not in g[v]:
            g[v].append(u)
    return [sorted(x) for x in g]


G = neighbours()
ADJ = [[False] * N for _ in range(N)]
for u in range(N):
    for v in G[u]:
        ADJ[u][v] = True

FAILS = 0
CHECKS = 0


def ck(cond, msg):
    global FAILS, CHECKS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg)


INF = 10 ** 9
D = [[0 if i == j else (1 if ADJ[i][j] else INF) for j in range(N)] for i in range(N)]
changed = True
while changed:
    changed = False
    for i in range(N):
        Di = D[i]
        for k in range(N):
            if Di[k] >= INF:
                continue
            dik = Di[k]
            for j in G[k]:
                if dik + 1 < Di[j]:
                    Di[j] = dik + 1
                    changed = True

ck(all(D[i][j] < INF for i in range(N) for j in range(N)), "G is connected")
ECC = [max(D[i]) for i in range(N)]
RAD = min(ECC)
DIAM = max(ECC)
CTR = [v for v in range(N) if ECC[v] == RAD]

bad = 0
for u in range(N):
    for v in range(u + 1, N):
        common = 0
        for x in G[u]:
            if ADJ[v][x]:
                common += 1
        if common >= 2:
            bad += 1
ck(bad == 0, "C4-free (this line's sense): " + str(bad) + " offending vertex pairs")


def alpha_nbhd(v):
    nb = G[v]
    for k in range(len(nb), 0, -1):
        for S in combinations(nb, k):
            ok = True
            for a, b in combinations(S, 2):
                if ADJ[a][b]:
                    ok = False
                    break
            if ok:
                return k
    return 0


A = [alpha_nbhd(v) for v in range(N)]
MU = min(A)
L = sum(A) / float(N)

print("n            = " + str(N))
print("|E|          = " + str(len(set(tuple(sorted(e)) for e in EDGES))))
print("mu           = " + str(MU))
print("l            = " + ("%.6f" % L))
print("rad          = " + str(RAD))
print("diam         = " + str(DIAM))
print("centre       = " + str(CTR))
ck(MU >= 2, "mu >= 2")
ck(L > 4, "l > 4")
ck(RAD >= 5, "rad >= 5")

W = [w for w in range(N) if ECC[w] == RAD + 1 and all(D[c][w] == RAD for c in CTR)]
print("witnesses w  = " + str(W) + "   (ecc(w) = rad+1 and d(c,w) = rad for EVERY centre)")
ck(len(W) > 0, "at least one w satisfies conditions 2 and 3")
for w in W:
    ck(ECC[w] == RAD + 1, "w=" + str(w) + ": ecc = rad+1")
    ck(all(D[c][w] == RAD for c in CTR), "w=" + str(w) + ": distance rad to every centre")
    ck(w not in CTR, "w=" + str(w) + " is not itself a centre")
print("CASE         = " + ("A" if DIAM == RAD + 1 else "B") + "   (A iff diam = rad+1)")
if DIAM > RAD + 1:
    for w in W:
        ck(ECC[w] < DIAM, "w=" + str(w) + " is condition-3 and NOT peripheral: a "
           "counterexample to (RXM-PERI) restricted to l > 4 and rad >= 5")
    print("Each w above has ecc(w) = " + str(RAD + 1) + " < " + str(DIAM) + " = diam, so each")
    print("is ALSO a counterexample to (RXM-PERI) restricted to l > 4 and rad >= 5.")

print("")
print("CHECKS: " + str(CHECKS) + "   FAILURES: " + str(FAILS))
sys.exit(1 if FAILS else 0)
