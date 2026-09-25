"""
modular_a7.py -- ROUND 2, line zc1a7.

Computes the COMPLETE set of irreducible p-modular Brauer characters of A_7
for p in {2,3,5,7}, on every RATIONAL p-regular class, from scratch:
  * A_7 built as a permutation group on 7 points, BFS'd (2520 elements, words);
  * F_p A_7-modules built as permutation / tensor modules;
  * chopped into irreducibles by a self-contained MeatAxe (meataxe.py) whose
    irreducibility certificate is NORTON's criterion (an iff, not a heuristic);
  * COMPLETENESS certified by Berman's count:
        #{irreducible F_p G-modules} = #{orbits of p-regular classes under g -> g^p}
    and #{absolutely irreducible} = #{p-regular classes} (Brauer);
  * absolutely irreducible Brauer values obtained from the F_p ones by dividing
    by k = dim_{F_p} End(S), which is legitimate on RATIONAL classes because
    S (x) Fbar_p is the sum of k Galois conjugates, all of which agree there.

EXACT arithmetic throughout: Python integers mod p.  No floating point.
Interpreter: .venv/bin/python3  (sympy 1.14.0) -- sympy used only for
polynomial factorisation mod p and cyclotomic polynomials.
"""
import json
import sys
from collections import deque
from sympy import cyclotomic_poly, Poly, symbols, divisors, totient, mobius

sys.setrecursionlimit(10000)
import meataxe as MA

X = symbols('x')

# ---------------------------------------------------------------- the group

N = 7
GENS_PERM = [
    tuple([1, 2, 0, 3, 4, 5, 6]),                  # a = (1 2 3)   0-based
    tuple([1, 2, 3, 4, 5, 6, 0]),                  # b = (1 2 3 4 5 6 7)
]


def pmul(x, y):
    """(x*y)(i) = x(y(i))"""
    return tuple(x[y[i]] for i in range(N))


def parity(perm):
    seen = [False] * N
    par = 0
    for i in range(N):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                L += 1
            par += L - 1
    return par % 2


def bfs_group():
    ident = tuple(range(N))
    words = {ident: []}
    q = deque([ident])
    while q:
        g = q.popleft()
        for gi, s in enumerate(GENS_PERM):
            h = pmul(s, g)
            if h not in words:
                words[h] = [gi] + words[g]
                q.append(h)
    return words


def cycle_type(perm):
    seen = [False] * N
    t = []
    for i in range(N):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))


def order_of(perm):
    from math import gcd
    o = 1
    for c in cycle_type(perm):
        o = o * c // gcd(o, c)
    return o


# rational class representatives, given directly by cycle type
def perm_from_cycles(cycles):
    p = list(range(N))
    for cyc in cycles:
        for i in range(len(cyc)):
            p[cyc[i] - 1] = cyc[(i + 1) % len(cyc)] - 1
    return tuple(p)


CLASS_REPS = {
    '1a': perm_from_cycles([]),
    '2a': perm_from_cycles([(1, 2), (3, 4)]),
    '3a': perm_from_cycles([(1, 2, 3)]),
    '3b': perm_from_cycles([(1, 2, 3), (4, 5, 6)]),
    '4a': perm_from_cycles([(1, 2, 3, 4), (5, 6)]),
    '5a': perm_from_cycles([(1, 2, 3, 4, 5)]),
    '6a': perm_from_cycles([(1, 2, 3), (4, 5), (6, 7)]),
    '7a': perm_from_cycles([(1, 2, 3, 4, 5, 6, 7)]),
}


def word_matrix(word, gens_mats, p):
    """word is a list of generator indices; the permutation was built as
    s_{i1} s_{i2} ... acting on the left, so apply the matrices in the same order."""
    d = len(gens_mats[0][0])
    M = MA.mat_id(d)
    for gi in word:
        M = MA.mat_mul(M, gens_mats[gi], p)
    return M


# ---------------------------------------------------------------- modules

def perm_module(points, act, p):
    """points: list of objects; act(g_perm, x) -> object.  Returns generator matrices."""
    idx = {x: i for i, x in enumerate(points)}
    d = len(points)
    out = []
    for s in GENS_PERM:
        M = [[0] * d for _ in range(d)]
        for x in points:
            M[idx[act(s, x)]][idx[x]] = 1
        out.append(M)
    return out


def act_point(s, x):
    return s[x]


def act_set(s, x):
    return tuple(sorted(s[i] for i in x))


# ---------------------------------------------------------------- Brauer values

def nullity(M, p):
    d = len(M)
    return d - MA.rank(M, p)


def brauer_value(Mg, m, p):
    """Brauer character value of a module element of order m on a RATIONAL class.
    Returns (value_as_Fraction-free integer or Fraction, diagnostics).
    Raises AssertionError if the rationality structure fails (a real control)."""
    d = len(Mg)
    total = 0
    val_num = 0            # value = sum_d mult_d * mobius(d)
    detail = {}
    for dd in divisors(m):
        Phi = Poly(cyclotomic_poly(dd, X), X, modulus=p)
        facs = Phi.factor_list()[1]
        mults = []
        ndd = 0
        for f, e in facs:
            assert e == 1, "cyclotomic poly not squarefree mod p (p | m?)"
            cs = [int(c) % p for c in reversed(f.all_coeffs())]
            deg = len(cs) - 1
            nul = nullity(MA.poly_eval_mat(cs, Mg, p), p)
            assert nul % deg == 0, "nullity not divisible by factor degree"
            mults.append(nul // deg)
            ndd += nul
        # RATIONALITY CONTROL: every primitive dd-th root must occur equally often
        assert len(set(mults)) == 1, (
            "class not rational on order-%d part: multiplicities %s" % (dd, mults))
        total += ndd
        detail[dd] = mults[0]
        val_num += mults[0] * int(mobius(dd))
    assert total == d, "eigenvalue multiplicities do not sum to the dimension"
    return val_num, detail


# ---------------------------------------------------------------- main

def p_regular_classes(p):
    return [c for c, g in CLASS_REPS.items() if order_of(g) % p != 0]


def find_all_irreducibles(p, target_fp, log=print):
    """All irreducible F_p A_7-modules, up to isomorphism.  Stops when the
    Berman count target_fp is reached."""
    irrs = []

    def add(m):
        d = len(m[0])
        for r in irrs:
            if r['dim'] == d and MA.hom_dim(m, r['gens'], p)[0] > 0:
                return False
        irrs.append({'gens': m, 'dim': d})
        log("      new irreducible F_%d-module of dimension %d  (total %d/%d)"
            % (p, d, len(irrs), target_fp))
        return True

    nat7 = perm_module(list(range(N)), act_point, p)
    sources = [('perm 7 points', nat7),
               ('perm 21 pairs', perm_module(
                   [t for t in __import__('itertools').combinations(range(N), 2)], act_set, p)),
               ('perm 35 triples', perm_module(
                   [t for t in __import__('itertools').combinations(range(N), 3)], act_set, p))]
    queue = list(sources)
    tensored = set()
    while len(irrs) < target_fp:
        if not queue:
            # tensor the smallest not-yet-tensored irreducible with the natural module
            cand = [r for i, r in enumerate(irrs) if i not in tensored]
            if not cand:
                raise RuntimeError("ran out of module sources for p=%d" % p)
            i = min(range(len(irrs)), key=lambda j: (j in tensored, irrs[j]['dim']))
            tensored.add(i)
            queue.append(('(%d-dim) (x) nat7' % irrs[i]['dim'],
                          MA.tensor(irrs[i]['gens'], nat7, p)))
        name, mod = queue.pop(0)
        log("   chopping %s  (dim %d) over F_%d" % (name, len(mod[0]), p))
        facs = MA.chop(mod, p)
        log("      composition factor dimensions: %s"
            % sorted(len(f[0]) for f in facs))
        for f in facs:
            add(f)
            if len(irrs) >= target_fp:
                break
    return irrs


def compute_tables(words, class_words, meta, log=print):
    out = {}
    for p in (2, 3, 5, 7):
        log("=" * 72)
        log("p = %d" % p)
        target = meta[p]['n_fp_irr']
        irrs = find_all_irreducibles(p, target, log=log)
        reg = [c for c in meta[p]['regular'] if c not in ('7a', '7b')]
        rows = []
        ksum = 0
        for r in irrs:
            k, _ = MA.hom_dim(r['gens'], r['gens'], p)
            ksum += k
            vals = {}
            for c in reg:
                Mg = word_matrix(class_words[c], r['gens'], p)
                v, _det = brauer_value(Mg, order_of(CLASS_REPS[c]), p)
                assert v % k == 0, ("Galois division failed: %s value %d not divisible "
                                    "by k=%d" % (c, v, k))
                vals[c] = v // k
            rows.append(dict(dim_fp=r['dim'], k=k, deg=r['dim'] // k, vals=vals,
                             gens=r['gens']))
            log("   F_%d-irreducible dim %-3d  k=dim End=%d  ->  absolutely irreducible "
                "Brauer character of degree %-3d  %s"
                % (p, r['dim'], k, r['dim'] // k,
                   " ".join("%s=%-3d" % (c, vals[c]) for c in reg)))
        assert ksum == meta[p]['n_regular'], (
            "sum of k over F_%d-irreducibles = %d, but there are %d p-regular classes"
            % (p, ksum, meta[p]['n_regular']))
        log("   COMPLETENESS: %d irreducible F_%d-modules (Berman target %d); "
            "sum of dim End = %d = #p-regular classes %d  [OK]"
            % (len(irrs), p, target, ksum, meta[p]['n_regular']))
        out[p] = dict(classes=reg, rows=rows)
    return out


def main():
    words = bfs_group()
    assert len(words) == 2520, "group order %d" % len(words)
    print("A_7 built by BFS: |G| = %d, all elements even = %s"
          % (len(words), all(parity(g) == 0 for g in words)))

    class_words = {}
    for c, g in CLASS_REPS.items():
        assert g in words, "class rep %s not in the group" % c
        class_words[c] = words[g]
    print("class reps as words in <a,b>: "
          + ", ".join("%s:len%d" % (c, len(w)) for c, w in sorted(class_words.items())))

    # p-regular class counts and p-power orbit counts (7a/7b handled separately)
    # 7a, 7b are the ONLY classes of A_7 that are not rational; they are the two
    # halves of the S_7 class of 7-cycles, distinguished by quadratic residues.
    QR7 = {1, 2, 4}
    def seven_class(k):     # class of g0^k where g0 = (1..7)
        return '7a' if (k % 7) in QR7 else '7b'

    results = {}
    for p in (2, 3, 5, 7):
        reg = [c for c in ['1a', '2a', '3a', '3b', '4a', '5a', '6a'] if order_of(CLASS_REPS[c]) % p]
        reg7 = [] if p == 7 else ['7a', '7b']
        nreg = len(reg) + len(reg7)
        # orbits under g -> g^p
        orbits = set()
        for c in reg:
            # rational class: g^p is conjugate to g, so each is its own orbit
            orbits.add(frozenset([c]))
        if reg7:
            o = frozenset([ '7a', seven_class(p) ]) if seven_class(p) == '7b' else frozenset(['7a'])
            if seven_class(p) == '7b':
                orbits.add(frozenset(['7a', '7b']))
            else:
                orbits.add(frozenset(['7a']))
                orbits.add(frozenset(['7b']))
        n_fp_irr = len(orbits)
        results[p] = dict(n_regular=nreg, n_fp_irr=n_fp_irr, regular=reg + reg7)
        print("p=%d: %d p-regular classes -> %d absolutely irreducible Brauer characters; "
              "%d irreducible F_%d-modules" % (p, nreg, nreg, n_fp_irr, p))

    tables = compute_tables(words, class_words, results)
    with open('brauer_tables.json', 'w') as fh:
        json.dump({str(p): tables[p] for p in tables}, fh, indent=1, sort_keys=True)
    print("\nwrote brauer_tables.json")
    return words, class_words, results, tables


if __name__ == '__main__':
    main()
