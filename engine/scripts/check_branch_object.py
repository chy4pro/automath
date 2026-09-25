#!/usr/bin/env python3
"""Independent quick check of a claimed branch object for ANY prime power q (n = q^2+q+1).
Usage: check_branch_object.py <json-file>. Second opinion only; line-677's verifier banks."""
import json, sys
from collections import Counter
obj = json.load(open(sys.argv[1]))
T, L, nu = obj["table"], obj["lines"], obj["nu"]
n = len(T); q = next(q for q in range(2, 20) if q*q+q+1 == n)
fail = []
for a,row in enumerate(T):
    if sorted(row) != list(range(n)): fail.append(f"B1 row {a}")
if sorted(nu) != list(range(n)): fail.append("B4")
D = {}
for t in range(n):
    col = [T[a][t] for a in range(n)]; c = Counter(col)
    ell = sorted(a for a in range(n) if T[a][t] == nu[t])
    if c[nu[t]] != q+1: fail.append(f"B2 col {t}: nu count {c[nu[t]]}")
    if ell != sorted(L[t]): fail.append(f"B2 col {t}: line mismatch")
    if any(v != nu[t] and k > 1 for v,k in c.items()): fail.append(f"B2 col {t}: repeated non-nu value")
    D[t] = sorted(set(range(n)) - set(col))
    if len(D[t]) != q: fail.append(f"B2 col {t}: |D|={len(D[t])}")
pairs = Counter()
for line in L:
    if len(line) != q+1: fail.append("B3 line size")
    for i in range(len(line)):
        for j in range(i+1, len(line)): pairs[frozenset((line[i], line[j]))] += 1
if len(pairs) != n*(n-1)//2 or any(k != 1 for k in pairs.values()): fail.append("B3 pair condition")
if fail:
    # F2 (CHECKADV 08-29): stop before left-division/Xi construction on a malformed table
    print(f"q={q} n={n} | FAILURES: {fail}")
    print("VERDICT: NOT A BRANCH OBJECT")
    sys.exit(1)
ldiv = [[None]*n for _ in range(n)]
for a in range(n):
    for w in range(n): ldiv[a][T[a][w]] = w
Xi = [[ldiv[x][ldiv[t][x]] for x in range(n)] for t in range(n)]
if any(T[x][Xi[t][x]] != ldiv[t][x] for t in range(n) for x in range(n)): fail.append("F-fusion")
E = [Counter(Xi[t]) for t in range(n)]; N = [Counter(T[a][t] for a in range(n)) for t in range(n)]
perfect = [r for r in range(n) if all(E[r][v] == N[r][v] for v in range(n))]
delta = [sum(E[t][v] for t in range(n)) - n for v in range(n)]
g = [ldiv[nu[c]][c] for c in range(n)]; b = Counter(g)
print(f"q={q} n={n} | FAILURES: {fail if fail else 'none'}")
print(f"perfect rows: {perfect} (|P|={len(perfect)}) | delta mass: {sum(abs(d) for d in delta)} | delta: {delta}")
print("D of perfect rows:", {r: D[r] for r in perfect}, "| b(v) values:", sorted(set(b[v] for v in range(n))))
# F1 (CHECKADV 08-29): branch validity and delta==0 are separate predicates
mass = sum(abs(d) for d in delta)
if fail:
    print("VERDICT: NOT A BRANCH OBJECT"); sys.exit(1)
print("VERDICT:", f"BRANCH OBJECT OK, |P|={len(perfect)}, " + ("delta==0" if mass == 0 else f"delta!=0 (mass {mass})"))
