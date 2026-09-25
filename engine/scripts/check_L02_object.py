#!/usr/bin/env python3
"""Independent quick check of a claimed branch object (677 L02 harvest).
Checks (B1)-(B4), computes Xi_t(x) = x \\ (t \\ x), perfect rows, delta, and the
(F-fusion) coupling identity. Second opinion only; line-677's verifier banks."""
import json, sys, re
from collections import Counter
src = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"```json\s*(\{.*?\})\s*```", src, re.S)
obj = json.loads(m.group(1))
T, L, nu = obj["table"], obj["lines"], obj["nu"]
n = len(T); q = 3; assert n == q*q+q+1
fail = []
# B1 rows are permutations
for a,row in enumerate(T):
    if sorted(row) != list(range(n)): fail.append(f"B1 row {a}")
# B4 nu bijection
if sorted(nu) != list(range(n)): fail.append("B4")
# B2 columns: nu(t) attained exactly q+1 times on line ell_t; others <=1; exactly q absent
D = {}
for t in range(n):
    col = [T[a][t] for a in range(n)]
    c = Counter(col)
    ell = sorted(a for a in range(n) if T[a][t] == nu[t])
    if c[nu[t]] != q+1: fail.append(f"B2 col {t}: nu count {c[nu[t]]}")
    if ell != sorted(L[t]): fail.append(f"B2 col {t}: line mismatch {ell} vs {sorted(L[t])}")
    if any(v != nu[t] and k > 1 for v,k in c.items()): fail.append(f"B2 col {t}: repeated non-nu value")
    D[t] = sorted(set(range(n)) - set(col))
    if len(D[t]) != q: fail.append(f"B2 col {t}: |D|={len(D[t])}")
# B3 projective plane: every pair of points on exactly one line
pairs = Counter()
for line in L:
    if len(line) != q+1: fail.append("B3 line size")
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            pairs[frozenset((line[i], line[j]))] += 1
if len(pairs) != n*(n-1)//2 or any(k != 1 for k in pairs.values()): fail.append("B3 pair condition")
# left division a\v
ldiv = [[None]*n for _ in range(n)]
for a in range(n):
    for w in range(n): ldiv[a][T[a][w]] = w
Xi = [[ldiv[x][ldiv[t][x]] for x in range(n)] for t in range(n)]
# (F-fusion): x * Xi_t(x) == t \ x
if any(T[x][Xi[t][x]] != ldiv[t][x] for t in range(n) for x in range(n)): fail.append("F-fusion")
# perfect rows and delta
E = [Counter(Xi[t]) for t in range(n)]
N = [Counter(T[a][t] for a in range(n)) for t in range(n)]
perfect = [r for r in range(n) if all(E[r][v] == N[r][v] for v in range(n))]
delta = [sum(E[t][v] for t in range(n)) - n for v in range(n)]
print("FAILURES:", fail if fail else "none")
print("perfect rows:", perfect, "| count:", len(perfect))
print("delta:", delta, "| mass:", sum(abs(d) for d in delta))
print("D_4, D_6, D_10:", D.get(4), D.get(6), D.get(10))
g = [ldiv[nu[c]][c] for c in range(n)]; b = Counter(g)
print("b(v) all 1?", all(b[v] == 1 for v in range(n)))
print("VERDICT:", "CLAIM REPRODUCED (3 perfect rows, delta==0, all axioms pass)" if not fail and len(perfect)==3 and sum(abs(d) for d in delta)==0 else "CLAIM NOT REPRODUCED")
