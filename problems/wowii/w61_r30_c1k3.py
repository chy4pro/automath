#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61 round 30, item 2 -- Conjecture C1 for k >= 3.

sec7.44 (j)3 named the question:  for which lambda does M(lambda) = [w]^{w+1} u lambda
have a realization containing a k-clique cover?  Observation C1-E is the first "no".

This round sharpens the question by moving it to the COMPLEMENT, where both halves
become named graph properties, and then measures the two halves apart.

  N := (w+1) + k                      vertices of M
  complement degree sequence
  D(lambda) := [N-1-w]^{w+1} u (N-1-lambda_i)_i = [k]^{w+1} u (w+k-lambda_i)_i

  alpha(G) = omega(Gbar), so
    (A)  M has a realization with alpha <= k        <=>  D has a K_{k+1}-FREE realization
    (B)  M has a realization with a k-clique cover  <=>  D has a k-COLOURABLE realization

  (B) => (A) always, and (B) is what Corollary C1-C's construction actually builds.
  So the clique-cover attack is STRICTLY STRONGER than the thing C1-C needs, and the
  characterisation question is really TWO questions.  This script measures the gap.

Two implementations, diffed BEFORE any verdict (standing rule):
  IMPL A  brute force over every labelled graph on N vertices (exact, N <= 7)
  IMPL B  backtracking realizer of the degree sequence, early exit on first witness
"""
import sys, itertools
from functools import lru_cache

# ------------------------------------------------------------------ partitions
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

# ------------------------------------------------------------------ HH process
def steps_residue(lst):
    """Havel-Hakimi one-deletion-per-step process; returns (steps, residue) or None."""
    cur = sorted(lst, reverse=True)
    s = 0
    while cur and cur[0] > 0:
        d = cur[0]; rest = cur[1:]
        if d > len(rest): return None
        rest = sorted(rest, reverse=True)
        for i in range(d):
            if rest[i] == 0: return None
            rest[i] -= 1
        cur = sorted(rest, reverse=True); s += 1
    return s, len(cur)

def graphical(seq):
    return steps_residue(list(seq)) is not None

def M_of(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)

def Mplus_of(lam):          # the [w]^{w+2} u lambda variant is NOT used; kept out on purpose
    raise NotImplementedError

# ------------------------------------------------------------------ IMPL A
def implA(deg):
    """exact min clique number over all labelled graphs with this degree sequence.
       returns (min_omega, min_chi_over_realizations, n_realizations)"""
    n = len(deg)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    best_w, best_c, cnt = None, None, 0
    for mask in range(1 << len(pairs)):
        adj = [0] * n
        for b, (i, j) in enumerate(pairs):
            if mask >> b & 1:
                adj[i] |= 1 << j; adj[j] |= 1 << i
        if sorted((bin(a).count('1') for a in adj), reverse=True) != sorted(deg, reverse=True):
            continue
        cnt += 1
        w = clique_number(adj, n)
        c = chromatic_number(adj, n)
        best_w = w if best_w is None else min(best_w, w)
        best_c = c if best_c is None else min(best_c, c)
    return best_w, best_c, cnt

def clique_number(adj, n):
    best = 0
    def ext(cand, size):
        nonlocal best
        if size > best: best = size
        c = cand
        while c:
            v = (c & -c).bit_length() - 1
            c &= c - 1
            if size + bin(cand).count('1') <= best: return
            ext(cand & adj[v] & ~((1 << (v + 1)) - 1), size + 1)
    ext((1 << n) - 1, 0)
    return best

def chromatic_number(adj, n):
    for k in range(1, n + 1):
        if colourable(adj, n, k): return k
    return n

def colourable(adj, n, k):
    col = [-1] * n
    def go(v):
        if v == n: return True
        used = set()
        for c in range(min(k, max(col[:v], default=-1) + 2)):
            ok = True
            for u in range(v):
                if (adj[v] >> u & 1) and col[u] == c: ok = False; break
            if ok:
                col[v] = c
                if go(v + 1): return True
                col[v] = -1
        return False
    return go(0)

# ------------------------------------------------------------------ IMPL B
def implB(deg, want, prop):
    """backtracking realizer; returns True as soon as ONE realization with
       prop(adj,n) <= want is found.  prop in {clique_number, chromatic_number}."""
    n = len(deg)
    order = sorted(range(n), key=lambda i: -deg[i])
    rem = list(deg)
    adj = [0] * n
    found = [False]
    def rec(idx):
        if found[0]: return
        if idx == n:
            if prop(adj, n) <= want: found[0] = True
            return
        v = order[idx]
        need = rem[v]
        later = [u for u in order[idx + 1:] if rem[u] > 0]
        if need == 0:
            rec(idx + 1); return
        if need > len(later): return
        for comb in itertools.combinations(later, need):
            for u in comb:
                adj[v] |= 1 << u; adj[u] |= 1 << v; rem[u] -= 1
            rem[v] = 0
            rec(idx + 1)
            rem[v] = need
            for u in comb:
                adj[v] &= ~(1 << u); adj[u] &= ~(1 << v); rem[u] += 1
            if found[0]: return
    rec(0)
    return found[0]

# ------------------------------------------------------------------ PART 0
def part0():
    print('=' * 78)
    print('PART 0 -- two implementations, diffed BEFORE any verdict, and the')
    print('         hand result of Observation C1-E reproduced as a POSITIVE control.')
    print('=' * 78)
    rows, dis = 0, 0
    for n in range(2, 8):
        for lam in partitions(n):
            k = len(lam); w = lam[0]
            M = M_of(lam)
            if len(M) > 7: continue
            if steps_residue(M) is None: continue
            N = len(M)
            D = [N - 1 - d for d in M]
            if min(D) < 0: continue
            a_om, a_chi, nreal = implA(D)
            b_om = implB(D, k, clique_number)
            b_chi = implB(D, k, chromatic_number)
            rows += 1
            if (a_om is not None) and ((a_om <= k) != b_om or (a_chi <= k) != b_chi):
                dis += 1
                print(f'  DISAGREEMENT lam={lam} A=({a_om},{a_chi}) B=({b_om},{b_chi})')
    print(f'  rows diffed: {rows}   disagreements: {dis}')
    if dis:
        print('  STOP -- the diff sits before any verdict precisely so this stops the run.')
        sys.exit(2)
    # positive control: C1-E says lam=(3,1) has NO realization with alpha<=2
    lam = (3, 1); k = 2
    M = M_of(lam); N = len(M); D = [N - 1 - d for d in M]
    got = implB(D, k, clique_number)
    a_om, a_chi, nreal = implA(D)
    print(f'  [C1-E POSITIVE CONTROL] lam=(3,1): realizations={nreal}, min omega(Gbar)={a_om} '
          f'(= min alpha(G)), k={k} -> alpha<=k available: {got}  (hand proof says False)')
    assert got is False and a_om == 3, 'C1-E not reproduced -- stop'
    # false-positive probe: a lambda the hand argument does NOT exclude must come back True
    lam = (2, 2); k = 2
    M = M_of(lam); N = len(M); D = [N - 1 - d for d in M]
    print(f'  [FALSE-POSITIVE PROBE] lam=(2,2): alpha<=k available: '
          f'{implB(D, k, clique_number)}  (want True -- a detector that never says YES is silent)')
    assert implB(D, k, clique_number) is True
    print('  PART 0 PASS')

# ------------------------------------------------------------------ main
def main():
    part0()
    print()
    print('=' * 78)
    print('PART 1 -- the two halves measured apart, over every lambda with |M| <= 9')
    print('  ALPHA  = M has a realization with alpha <= k        (what C1-C needs)')
    print('  COVER  = M has a realization with a k-clique cover  (what C1-C builds)')
    print('  GRAPH  = lambda is itself graphical                 (sec7.44 (e)3: => both)')
    print('=' * 78)
    print(f"{'lambda':<16}{'k':>3}{'w':>4}{'|M|':>5}  {'GRAPH':>6}{'ALPHA':>7}{'COVER':>7}   note")
    tot = a_yes = c_yes = gap = 0
    fails = []
    for n in range(2, 15):
        for lam in partitions(n):
            k = len(lam); w = lam[0]
            M = M_of(lam)
            if len(M) > 9: continue
            if steps_residue(M) is None: continue
            N = len(M); D = [N - 1 - d for d in M]
            A = implB(D, k, clique_number)
            C = implB(D, k, chromatic_number)
            G = graphical(lam)
            tot += 1; a_yes += A; c_yes += C
            note = ''
            if G and not C: note = '*** GRAPHICAL BUT NO COVER -- contradicts sec7.44 (e)3'
            if A and not C: note = 'alpha yes, cover no -- (B) strictly stronger'; gap += 1
            if not A:
                note = (note + ' | C1-C UNAVAILABLE').strip(' |')
                fails.append((lam, k, w))
            print(f"{str(lam):<16}{k:>3}{w:>4}{len(M):>5}  {str(G):>6}{str(A):>7}{str(C):>7}   {note}")
    print()
    print(f'rows: {tot}   ALPHA available: {a_yes}   COVER available: {c_yes}   '
          f'ALPHA-but-not-COVER: {gap}')
    print()
    print('PART 2 -- where C1-C is UNAVAILABLE (the population Observation C1-E opened)')
    for lam, k, w in fails:
        print(f'   lambda={lam}  k={k}  w={w}   smallest part={min(lam)}   '
              f'sum-w={sum(lam)-w}   graphical={graphical(lam)}')
    print()
    print('PART 3 -- candidate criterion, tested on the population above, NOT proved')
    ok = True
    for n in range(2, 15):
        for lam in partitions(n):
            k = len(lam); w = lam[0]
            M = M_of(lam)
            if len(M) > 9 or steps_residue(M) is None: continue
            N = len(M); D = [N - 1 - d for d in M]
            A = implB(D, k, clique_number)
            pred = (sum(lam) - lam[0] >= 2) or graphical(lam)
            if A != pred:
                ok = False
                print(f'   criterion MISS at lambda={lam}: available={A} predicted={pred}')
    print(f'   criterion "sum(lambda) - lambda_1 >= 2  OR  lambda graphical"  '
          f'agrees on every row: {ok}')
    print('   THIS IS A MEASUREMENT OVER |M| <= 9.  More cases is not a proof and is')
    print('   not offered as one.')

if __name__ == '__main__':
    main()
