#!/usr/bin/env python3
"""ROUND 6-R: universal hitting sets (WIDE direction B1).  For every A in GL(n,q) compute the set
good(A) = {sigma : A P_sigma cyclic}; find the MINIMUM size of W_0 subset S_n with W_0 meeting every
good(A) (exact by branch-and-bound over the n! permutations; greedy as upper bound), and the minimum
over W_0 restricted to conjugation-closed unions of cycle types.  Cells: GL(3,q) q in {2,3,4,5},
GL(4,2), GL(4,3)-sample.  Light, exact tables."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']

def ctype(s):
    n = len(s); seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))

def min_hitting(sets, universe):
    """exact minimum hitting set by iterative deepening over subsets of the universe (small)."""
    sets = list({frozenset(s) for s in sets})
    # remove supersets (keep minimal sets only) — hitting the minimal ones hits all
    sets.sort(key=len)
    minimal = []
    for s in sets:
        if not any(m <= s for m in minimal): minimal.append(s)
    sets = minimal
    for k in range(1, len(universe)+1):
        for W in itertools.combinations(universe, k):
            Wset = set(W)
            if all(s & Wset for s in sets):
                return k, W
    return None, None

def run(n, q, sample=None):
    F = GF(q); perms = list(itertools.permutations(range(n)))
    goods = []; tot = 0; count_by_type_needed = {}
    rng = random.Random(1695)
    it = itertools.product(range(q), repeat=n*n) if sample is None else (tuple(rng.randrange(q) for _ in range(n*n)) for _ in range(sample))
    for entries in it:
        A = [list(entries[r*n:(r+1)*n]) for r in range(n)]
        if rank_rows(A, n, F) < n: continue
        tot += 1
        g = frozenset(s for s in perms if cyclic(tuple(A[i][s[j]] for i in range(n) for j in range(n)), n, F))
        assert g, "16.95 counterexample?! %s" % (A,)
        goods.append(g)
    distinct = {g for g in goods}
    k, W = min_hitting(list(distinct), perms)
    types = sorted({ctype(s) for s in W})
    # greedy for comparison
    remaining = set(distinct); greedy = []
    while remaining:
        best = max(perms, key=lambda s: sum(1 for g in remaining if s in g))
        greedy.append(best); remaining = {g for g in remaining if best not in g}
    print("GL(%d,%d)%s: matrices=%d distinct good-sets=%d  MIN hitting set size=%d  W0=%s (types %s)  greedy size=%d  [%.0fs]"
          % (n, q, "" if sample is None else " sample %d" % sample, tot, len(distinct), k, W, types, len(greedy), time.time()-T0))
    # also: min hitting set using only n-cycles?  only {n-cycles + (n-1,1)}?
    for name, allowed in [("n-cycles only", [s for s in perms if ctype(s) == (n,)]),
                          ("n-cycles + (n-1,1)", [s for s in perms if ctype(s) in ((n,), (n-1, 1))])]:
        ok = all(any(s in g for s in allowed) for g in distinct)
        if ok:
            k2, W2 = min_hitting(list(distinct), allowed)
            print("   restricted to %s: hits all, min size %d" % (name, k2))
        else:
            miss = sum(1 for g in distinct if not any(s in g for s in allowed))
            print("   restricted to %s: MISSES %d good-sets" % (name, miss))

print("ROUND 6-R: universal hitting sets")
for (n, q) in [(3, 2), (3, 3), (3, 4), (3, 5), (4, 2)]:
    run(n, q)
run(4, 3, sample=30000)
print("done %.0fs" % (time.time()-T0))
