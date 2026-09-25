#!/usr/bin/env python3
"""ROUND 6-W: numerical cross-check of the Qwen K6-PHI family A_Q = Q + J over GF(2), n even
(registry R6.62).  For every Q in S_n and every i: kd(A_Q, i) against the Lemma-2 formula
(L = length of the Q-cycle through i): L<n even -> L; L<n odd -> L+1; L=n -> n if n%4==0 else n-1.
Then, at every kd-local maximum below n (no transposition raises kd), check Lemma 3 (C odd, L<=n-3,
all other cycles fixed points), Lemma 4 (nu = C(m,2)+L*m, m=n-L) and Lemma 5 / (Mono) (every neutral
transposition lowers nu).  Own code; light (n = 4, 6, 8)."""
import sys, itertools, time
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows = G['GF'], G['rank_rows']
F = GF(2)

def run(n, sample=None):
    import random
    rng = random.Random(1695)
    trans = [(a, b) for a in range(n) for b in range(a+1, n)]
    def mat(s):  # A_Q = P_s + J, P_s e_j = e_{s(j)}
        return [[(1 if s[j] == i else 0) ^ 1 for j in range(n)] for i in range(n)]
    def matvec(B, v):
        return [sum(B[i][j] & v[j] for j in range(n)) & 1 for i in range(n)]
    def kd(B, i):
        v = [0]*n; v[i] = 1; kry = [v]
        for _ in range(n-1):
            v = matvec(B, v); kry.append(v)
        return rank_rows(kry, n, F)
    def swapcols(B, a, b):
        return [[row[b] if j == a else (row[a] if j == b else row[j]) for j in range(n)] for row in B]
    def cyc_len(s, i):
        L = 1; j = s[i]
        while j != i: j = s[j]; L += 1
        return L
    def cycles(s):
        seen = [False]*n; out = []
        for i in range(n):
            if not seen[i]:
                L = 0; j = i
                while not seen[j]: seen[j] = True; j = s[j]; L += 1
                out.append(L)
        return sorted(out)
    def formula(L):
        if L < n: return L if L % 2 == 0 else L + 1
        return n if n % 4 == 0 else n - 1
    bad2 = 0; locmax = 0; bad3 = 0; bad4 = 0; bad5 = 0; tot = 0
    perms = list(itertools.permutations(range(n)))
    if sample: perms = rng.sample(perms, sample)
    for s in perms:
        B = mat(s)
        for i in range(n):
            tot += 1
            k = kd(B, i)
            if k != formula(cyc_len(s, i)): bad2 += 1
            if k == n: continue
            nb = [kd(swapcols(B, a, b), i) for (a, b) in trans]
            if max(nb) > k: continue
            locmax += 1
            L = cyc_len(s, i); m = n - L
            others = [c for c in cycles(s)]; others.remove(L)
            if not (L % 2 == 1 and L <= n - 3 and all(c == 1 for c in others)): bad3 += 1
            nu = sum(1 for x in nb if x == k)
            if nu != m*(m-1)//2 + L*m: bad4 += 1
            for (a, b), x in zip(trans, nb):
                if x == k:
                    B2 = swapcols(B, a, b); k2 = kd(B2, i)
                    nu2 = sum(1 for (c, d) in trans if kd(swapcols(B2, c, d), i) == k2)
                    if nu2 >= nu: bad5 += 1
    print("n=%d%s: pairs (Q,i)=%d  Lemma2 mismatches=%d  local maxima below n=%d  Lemma3 violations=%d  Lemma4 violations=%d  Lemma5/(Mono) violations=%d  [%.0fs]"
          % (n, " (sample %d of %d perms)" % (sample, len(perms)) if sample else "", tot, bad2, locmax, bad3, bad4, bad5, time.time()-T0))

print("ROUND 6-W: Q + J family over GF(2) (Qwen K6-PHI section 2), own code")
run(4); run(6); run(8, sample=1500)
print("done %.0fs" % (time.time()-T0))
