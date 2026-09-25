#!/usr/bin/env python3
"""
WOWII-61: numerical stress test of the new head-decay lemmas (owner-w61, 08-18).

Claims under test (all assume residue(G) = alpha(G), i.e. the Havel-Hakimi
process on d(G) takes exactly s = tau = n - alpha steps):

 S  (survivor bound)   every entry of value >= tau+1 must be removed as a head;
                       hence #{v : deg v >= tau+1} <= tau.
 F3 (decay bound)      at the START of step j (1-indexed) every survivor entry
                       has value <= tau - j + 1.
 H  (head decay)       write h_i = g_i - D_i for the number of decrements the
                       i-th head absorbs before removal (g_i its degree, D_i
                       its value on removal).  Then for every i >= 2 with
                       h_i <= i-2:      D_i <= tau - i + 2 + h_i.
 N  (theorem)          if B is a minimum vertex cover with e_B edges inside,
                       every b in B has deg(b) >= tau+1, and e_B <= tau-2,
                       then  min_{b in B} deg(b) <= 2 e_B + 2.
                       (=> if additionally min deg(b) >= 2 e_B + 3 the graph
                        cannot have residue = alpha.)

Run:  python3 w61_lemH.py [MAXN]        (default: exhaustive n<=8 + random 9..12)
"""
import sys, random, itertools

# ------------------------------------------------------------------ Havel-Hakimi with labels
def hh_labelled(degs):
    """Returns (steps, heads) where heads = [(label, g, D, h)] in removal order,
       and survivors = labels never removed.  Also returns, for each step j,
       the list of (label, value) at the START of step j."""
    ent = [[d, i] for i, d in enumerate(degs)]          # [value, label]
    g0 = {i: d for i, d in enumerate(degs)}
    dec = {i: 0 for i in range(len(degs))}              # decrements absorbed
    heads = []
    snapshots = []
    while True:
        ent.sort(key=lambda t: -t[0])
        if not ent:
            return heads, [], snapshots
        if ent[0][0] == 0:
            return heads, [lab for _, lab in ent], snapshots
        snapshots.append([(lab, v) for v, lab in ent])
        d = ent[0][0]
        hl = ent[0][1]
        heads.append((hl, g0[hl], d, dec[hl]))
        rest = ent[1:]
        for k in range(min(d, len(rest))):
            rest[k][0] = max(rest[k][0] - 1, 0)
            dec[rest[k][1]] += 1
        ent = rest


def residue_of(degs):
    h, surv, _ = hh_labelled(degs)
    return len(degs) - len(h)


# ------------------------------------------------------------------ graph tools
def adj_masks(n, edges):
    a = [0] * n
    for (u, v) in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def is_connected(a, n):
    seen, stack = 1, [0]
    while stack:
        v = stack.pop()
        m = a[v] & ~seen
        while m:
            b = m & -m
            m ^= b
            w = b.bit_length() - 1
            seen |= b
            stack.append(w)
    return seen == (1 << n) - 1


def alpha_and_covers(a, n):
    """exact independence number + ALL maximum independent sets (as masks)."""
    best, sets = 0, []
    for S in range(1 << n):
        ok = True
        m = S
        while m:
            b = m & -m
            m ^= b
            v = b.bit_length() - 1
            if a[v] & S:
                ok = False
                break
        if not ok:
            continue
        c = bin(S).count('1')
        if c > best:
            best, sets = c, [S]
        elif c == best:
            sets.append(S)
    return best, sets


# ------------------------------------------------------------------ the tests
class Res:
    def __init__(self):
        self.n_tested = 0
        self.n_resalpha = 0
        self.failS = self.failF3 = self.failH = self.failN = 0
        self.hitN = 0
        self.hitNp = self.failNp = 0
        self.wit = {}

    def note(self, key, payload):
        self.wit.setdefault(key, payload)


def test_graph(n, edges, R):
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    degs = [bin(x).count('1') for x in a]
    al, isets = alpha_and_covers(a, n)
    tau = n - al
    R.n_tested += 1
    heads, surv, snaps = hh_labelled(degs)
    s = len(heads)

    # --- Theorem N, tested on EVERY graph (this is the real, non-vacuous test):
    #     hypothesis  => conclusion residue <= alpha - 1
    for S in isets:
        B = [v for v in range(n) if not (S >> v & 1)]
        eB = sum(1 for u, v in edges if (not (S >> u & 1)) and (not (S >> v & 1)))
        if eB <= tau - 2 and min(degs[b] for b in B) >= max(tau + 1, 2 * eB + 3):
            R.hitN += 1
            if n - s >= al:                       # residue >= alpha : N is FALSE
                R.failN += 1
                R.note("N", (n, edges, degs, tau, eB, sorted(degs[b] for b in B)))

    if n - s != al:
        return                                   # residue < alpha: nothing to check
    R.n_resalpha += 1
    assert s == tau

    # --- S
    if sum(1 for d in degs if d >= tau + 1) > tau:
        R.failS += 1
        R.note("S", (n, edges, degs, tau))
    headlabels = {h[0] for h in heads}
    for d_i, lab in [(degs[i], i) for i in range(n)]:
        if d_i >= tau + 1 and lab not in headlabels:
            R.failS += 1
            R.note("S2", (n, edges, degs, tau, lab))

    # --- F3 : survivors at start of step j have value <= tau - j + 1
    for j, snap in enumerate(snaps, start=1):
        for lab, v in snap:
            if lab in headlabels:
                continue
            if v > tau - j + 1:
                R.failF3 += 1
                R.note("F3", (n, edges, degs, tau, j, lab, v))

    # --- H : D_i <= tau - i + 2 + h_i whenever h_i <= i-2
    for i, (lab, g, D, h) in enumerate(heads, start=1):
        if i >= 2 and h <= i - 2:
            if D > tau - i + 2 + h:
                R.failH += 1
                R.note("H", (n, edges, degs, tau, i, g, D, h))

    # --- N' : the raw conclusion  min_B deg <= 2 e_B + 2  under K = B
    for S in isets:
        B = [v for v in range(n) if not (S >> v & 1)]
        eB = sum(1 for u, v in edges if (not (S >> u & 1)) and (not (S >> v & 1)))
        if min(degs[b] for b in B) >= tau + 1 and eB <= tau - 2:
            R.hitNp += 1
            if min(degs[b] for b in B) > 2 * eB + 2:
                R.failNp += 1
                R.note("Np", (n, edges, degs, tau, eB, sorted(degs[b] for b in B)))


def gen_upto7():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    out = []
    for G in graph_atlas_g():
        n = G.number_of_nodes()
        if n < 2:
            continue
        if not nx.is_connected(G):
            continue
        out.append((n, [(u, v) for u, v in G.edges()]))
    return out


def main():
    R = Res()
    small = gen_upto7()
    for n, e in small:
        test_graph(n, e, R)
    print(f"[stage A n<=7 exhaustive] tested={R.n_tested} residue=alpha:{R.n_resalpha} "
          f"failS={R.failS} failF3={R.failF3} failH={R.failH} "
          f"hitN={R.hitN} failN={R.failN} hitNp={R.hitNp} failNp={R.failNp}")

    conn7 = [e for n, e in small if n == 7]
    for edges in conn7:
        for mask in range(1, 1 << 7):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            test_graph(8, e2, R)
    print(f"[+stage B n=8 exhaustive cover] tested={R.n_tested} residue=alpha:{R.n_resalpha} "
          f"failS={R.failS} failF3={R.failF3} failH={R.failH} "
          f"hitN={R.hitN} failN={R.failN} hitNp={R.hitNp} failNp={R.failNp}")

    rnd = random.Random(20260818)
    for n in range(9, 13):
        for _ in range(3000):
            p = rnd.choice([0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6])
            edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rnd.random() < p]
            test_graph(n, edges, R)
    print(f"[+random n=9..12] tested={R.n_tested} residue=alpha:{R.n_resalpha} "
          f"failS={R.failS} failF3={R.failF3} failH={R.failH} "
          f"hitN={R.hitN} failN={R.failN} hitNp={R.hitNp} failNp={R.failNp}")

    # structured stress: complete multipartite / split graphs / near-regular,
    # the natural residue = alpha zoo
    fam = []
    for k in range(2, 7):
        fam.append((k, [(i, j) for i in range(k) for j in range(i + 1, k)]))   # K_k
    for a_ in range(1, 6):
        for b_ in range(1, 6):
            n = a_ + b_
            fam.append((n, [(i, a_ + j) for i in range(a_) for j in range(b_)]))  # K_{a,b}
    for c in range(2, 6):
        for lv in range(1, 5):
            n = c + lv
            e = [(i, j) for i in range(c) for j in range(i + 1, c)]
            e += [(c + t, t % c) for t in range(lv)]
            fam.append((n, e))                                                  # clique+pendants
    for n, e in fam:
        test_graph(n, e, R)
    print(f"[+structured] tested={R.n_tested} residue=alpha:{R.n_resalpha} "
          f"failS={R.failS} failF3={R.failF3} failH={R.failH} "
          f"hitN={R.hitN} failN={R.failN} hitNp={R.hitNp} failNp={R.failNp}")
    for k, v in R.wit.items():
        print("  WITNESS", k, v)


if __name__ == "__main__":
    main()
