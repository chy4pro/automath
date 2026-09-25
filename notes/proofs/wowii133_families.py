#!/usr/bin/env python3
"""WOWII Conjecture 133 : structural-family verification.

    path(G) >= rad(G) + floor(l(G))^{cC4(G)},   cC4 = 1 iff G is C4-free (subgraph sense)

path(G) = #vertices of a largest induced path, rad = min eccentricity,
l(G) = (1/n) sum_v alpha(G[N(v)]).
"""
import sys, random, itertools, time
from collections import deque

sys.setrecursionlimit(100000)

# ---------------- graph helpers (adjacency = list of bitmasks) ----------------

def from_edges(n, edges):
    adj = [0]*n
    for u, v in edges:
        assert u != v
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj

def is_connected(adj):
    n = len(adj)
    seen, fr = 1, 1
    while fr:
        nf = 0
        for v in range(n):
            if fr >> v & 1: nf |= adj[v]
        nf &= ~seen
        seen |= nf
        fr = nf
    return seen == (1 << n) - 1

def has_c4(adj):
    n = len(adj)
    for u in range(n):
        for v in range(u+1, n):
            if bin(adj[u] & adj[v]).count('1') >= 2:
                return True
    return False

def radius(adj):
    n = len(adj)
    best = 10**9
    for s in range(n):
        seen, fr, d = 1 << s, 1 << s, 0
        while True:
            nf = 0
            for v in range(n):
                if fr >> v & 1: nf |= adj[v]
            nf &= ~seen
            if not nf: break
            seen |= nf; fr = nf; d += 1
        best = min(best, d)
    return best

def diameter(adj):
    n = len(adj)
    best = 0
    for s in range(n):
        seen, fr, d = 1 << s, 1 << s, 0
        while True:
            nf = 0
            for v in range(n):
                if fr >> v & 1: nf |= adj[v]
            nf &= ~seen
            if not nf: break
            seen |= nf; fr = nf; d += 1
        best = max(best, d)
    return best

def alpha(adj, mask):
    """maximum independent set of the subgraph induced on `mask`"""
    if not mask: return 0
    # pick max-degree vertex inside mask
    bd, bv = -1, -1
    m = mask
    while m:
        b = m & -m; m ^= b
        v = b.bit_length()-1
        d = bin(adj[v] & mask).count('1')
        if d > bd: bd, bv = d, v
    if bd == 0:
        return bin(mask).count('1')
    return max(alpha(adj, mask & ~(1 << bv)),
               1 + alpha(adj, mask & ~((1 << bv) | adj[bv])))

def sum_local_indep(adj):
    return sum(alpha(adj, adj[v]) for v in range(len(adj)))

def longest_induced_path(adj, cap=None):
    """exact largest induced path (#vertices); cap = stop as soon as cap reached"""
    n = len(adj)
    full = (1 << n) - 1
    best = 0
    order = list(range(n))
    def dfs(last, pmask, forbid, ln):
        nonlocal best
        if ln > best: best = ln
        if cap is not None and best >= cap: return True
        avail = full & ~pmask & ~forbid
        if ln + bin(avail).count('1') <= best: return False
        cands = adj[last] & avail
        nf = forbid | adj[last]
        while cands:
            b = cands & -cands; cands ^= b
            if dfs(b.bit_length()-1, pmask | b, nf, ln+1): return True
        return False
    for s in order:
        if dfs(s, 1 << s, 0, 1): break
    return best

def induced_path_at_least(adj, target, tries=400, seed=0):
    """randomised search for an induced path on >= target vertices (True/False + witness len)"""
    n = len(adj)
    full = (1 << n) - 1
    rng = random.Random(seed)
    found = [0]
    def dfs(last, pmask, forbid, ln, budget):
        if ln > found[0]: found[0] = ln
        if ln >= target: return True
        if budget[0] <= 0: return False
        budget[0] -= 1
        avail = full & ~pmask & ~forbid
        if ln + bin(avail).count('1') < target: return False
        cands = []
        c = adj[last] & avail
        while c:
            b = c & -c; c ^= b
            cands.append(b)
        rng.shuffle(cands)
        nf = forbid | adj[last]
        for b in cands:
            if dfs(b.bit_length()-1, pmask | b, nf, ln+1, budget): return True
        return False
    for t in range(tries):
        s = rng.randrange(n)
        if dfs(s, 1 << s, 0, 1, [200000]):
            return True, found[0]
    return False, found[0]

# ---------------- the test ----------------

RESULTS = []
def check(name, adj, exact=True, verbose=True):
    n = len(adj)
    assert is_connected(adj), name + " not connected"
    r = radius(adj)
    c4 = has_c4(adj)
    S = sum_local_indep(adj)
    fl = S // n
    rhs = r + (1 if c4 else fl)
    if exact:
        p = longest_induced_path(adj)
        ok = p >= rhs
        pstr = str(p)
    else:
        ok, p = induced_path_at_least(adj, rhs)
        pstr = ">=%d" % rhs if ok else "<%d (best found %d)" % (rhs, p)
    slack = (p - rhs) if exact else None
    RESULTS.append((name, n, r, c4, S/n, fl, rhs, pstr, ok, slack))
    if verbose:
        print("%-34s n=%-4d rad=%-2d C4=%-5s l=%7.4f floor=%d  RHS=%-3d path=%-4s %s%s" %
              (name, n, r, str(not c4)+"free" if not c4 else "yes", S/n, fl, rhs, pstr,
               "OK" if ok else "*** VIOLATION ***",
               "  TIGHT" if (exact and p == rhs) else ""))
    if not ok:
        print("!!! COUNTEREXAMPLE:", name, [(u, v) for u in range(n) for v in range(u+1, n) if adj[u] >> v & 1])
    return ok

# ---------------- families ----------------

def cycle(n):
    return from_edges(n, [(i, (i+1) % n) for i in range(n)])

def path_graph(n):
    return from_edges(n, [(i, i+1) for i in range(n-1)])

def star(m):
    return from_edges(m+1, [(0, i) for i in range(1, m+1)])

def friendship(k):
    e = []
    for i in range(k):
        e += [(0, 2*i+1), (0, 2*i+2), (2*i+1, 2*i+2)]
    return from_edges(2*k+1, e)

def petersen():
    e = [(i, (i+1) % 5) for i in range(5)]
    e += [(i, i+5) for i in range(5)]
    e += [(5+i, 5+(i+2) % 5) for i in range(5)]
    return from_edges(10, e)

def kneser(nn, kk):
    sets = list(itertools.combinations(range(nn), kk))
    idx = {s: i for i, s in enumerate(sets)}
    e = []
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            if not (set(sets[i]) & set(sets[j])):
                e.append((i, j))
    return from_edges(len(sets), e)

def heawood():
    # incidence graph of Fano plane
    return incidence_pg(2)

# --- finite fields (prime and prime power via polynomial rep) ---
class GF:
    """GF(p^k) with p prime; elements are tuples of length k over F_p."""
    def __init__(self, p, k, modpoly=None):
        self.p, self.k = p, k
        if k == 1:
            self.elts = [(i,) for i in range(p)]
            self.modpoly = None
        else:
            self.modpoly = modpoly  # list of k coeffs c0..c_{k-1} with x^k = -(c0+c1x+...)
            self.elts = [tuple(t) for t in itertools.product(range(p), repeat=k)]
        self.zero = tuple([0]*k)
        self.one = tuple([1]+[0]*(k-1))
    def add(self, a, b): return tuple((x+y) % self.p for x, y in zip(a, b))
    def neg(self, a): return tuple((-x) % self.p for x in a)
    def mul(self, a, b):
        p, k = self.p, self.k
        if k == 1: return ((a[0]*b[0]) % p,)
        res = [0]*(2*k-1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    res[i+j] = (res[i+j] + x*y) % p
        # reduce
        for d in range(2*k-2, k-1, -1):
            c = res[d]
            if c:
                res[d] = 0
                for i in range(k):
                    res[d-k+i] = (res[d-k+i] + c*self.modpoly[i]) % p
        return tuple(res[:k])

FIELDS = {
    2: GF(2, 1), 3: GF(3, 1), 5: GF(5, 1), 7: GF(7, 1), 11: GF(11, 1), 13: GF(13, 1),
    4: GF(2, 2, [1, 1]),      # x^2 = x + 1  over F2
    8: GF(2, 3, [1, 1, 0]),   # x^3 = x + 1
    9: GF(3, 2, [1, 0]),      # x^2 = 1 ... will fix below
}
FIELDS[9] = GF(3, 2, [1, 0])   # x^2 = 1? not irreducible -> replace
FIELDS[9] = GF(3, 2, [1, 0])
# x^2 + 1 irreducible over F3  =>  x^2 = -1 = 2  => modpoly coeffs (c0,c1) with x^2 = c0 + c1 x
FIELDS[9] = GF(3, 2, [2, 0])

def pg2_points(q):
    F = FIELDS[q]
    pts = []
    seen = set()
    for v in itertools.product(F.elts, repeat=3):
        if all(x == F.zero for x in v): continue
        # normalise: first nonzero coordinate = 1
        # find scalar to multiply
        key = None
        for lam in F.elts:
            if lam == F.zero: continue
            w = tuple(F.mul(lam, x) for x in v)
            if key is None or w < key: key = w
        if key not in seen:
            seen.add(key); pts.append(key)
    return F, pts

def dot(F, a, b):
    s = F.zero
    for x, y in zip(a, b): s = F.add(s, F.mul(x, y))
    return s

def incidence_pg(q):
    """bipartite incidence graph of PG(2,q): girth 6, (q+1)-regular, 2(q^2+q+1) vertices"""
    F, pts = pg2_points(q)
    npt = len(pts)
    e = []
    for i, P in enumerate(pts):
        for j, L in enumerate(pts):
            if dot(F, P, L) == F.zero:
                e.append((i, npt + j))
    return from_edges(2*npt, e)

def polarity_graph(q):
    """Erdos-Renyi orthogonal polarity graph ER_q: C4-free, n=q^2+q+1, ~ (1/2)q(q+1)^2 edges,
       diameter 2 -> radius 2.  The extremal C4-free graphs."""
    F, pts = pg2_points(q)
    n = len(pts)
    e = []
    for i in range(n):
        for j in range(i+1, n):
            if dot(F, pts[i], pts[j]) == F.zero:
                e.append((i, j))
    return from_edges(n, e)

def hoffman_singleton():
    """standard construction: 5 pentagons P_h, 5 pentagrams Q_i, P_h[j] ~ Q_i[i*h+j mod 5]"""
    n = 50
    def P(h, j): return h*5 + j
    def Q(i, j): return 25 + i*5 + j
    e = []
    for h in range(5):
        for j in range(5):
            e.append((P(h, j), P(h, (j+1) % 5)))
            e.append((Q(h, j), Q(h, (j+2) % 5)))
    for h in range(5):
        for i in range(5):
            for j in range(5):
                e.append((P(h, j), Q(i, (h*i + j) % 5)))
    e = sorted(set(tuple(sorted(x)) for x in e))
    return from_edges(n, e)

def mcgee():
    # (3,7)-cage, 24 vertices: LCF-like construction
    e = [(i, (i+1) % 24) for i in range(24)]
    chords = {0: 12, 1: 8, 2: 16, 3: 15, 4: 20, 5: 9, 6: 18, 7: 11, 10: 22, 13: 21, 14: 19, 17: 23}
    for a, b in chords.items():
        e.append((a, b))
    return from_edges(24, e)

def lcf(n, shifts, repeats):
    e = [(i, (i+1) % n) for i in range(n)]
    s = shifts * repeats
    for i in range(n):
        j = (i + s[i]) % n
        if i < j: e.append((i, j))
        else: e.append((j, i))
    e = sorted(set(tuple(sorted(x)) for x in e))
    return from_edges(n, e)

def robertson():
    """(4,5)-cage, 19 vertices"""
    e = [(i, (i+1) % 19) for i in range(19)]
    for i in range(0, 19):
        pass
    # Robertson graph: 19-cycle + chords of length 4 and 9 in a pattern
    # standard: chords {i, i+4} for i in 0,4,8,12,16? use known edge list via LCF-ish pattern
    chords = [(0, 4), (4, 9), (9, 13), (13, 17), (17, 2), (2, 6), (6, 10), (10, 15), (15, 0),
              (1, 8), (8, 16), (16, 5), (5, 12), (12, 1), (3, 11), (11, 18), (18, 7), (7, 14), (14, 3)]
    for a, b in chords:
        e.append((a, b))
    e = sorted(set(tuple(sorted(x)) for x in e))
    return from_edges(19, e)

def random_c4free(n, seed, tries=None):
    """greedy maximal C4-free graph on n vertices"""
    rng = random.Random(seed)
    adj = [0]*n
    pairs = [(u, v) for u in range(n) for v in range(u+1, n)]
    rng.shuffle(pairs)
    for u, v in pairs:
        # adding uv creates C4 iff u,v have a common neighbour already, or
        # exists w in N(u), x in N(v) with w~x ... no: C4 = u-v-x-w-u  => w in N(u), x in N(v), w~x
        bad = False
        w = adj[u]
        while w and not bad:
            b = w & -w; w ^= b
            wi = b.bit_length()-1
            if wi == v: continue
            if adj[wi] & adj[v] & ~(1 << u):
                bad = True
        if bad: continue
        adj[u] |= 1 << v; adj[v] |= 1 << u
    return adj

# ---------------- more families ----------------

def disjoint_union_chain(blocks, links):
    """blocks: list of adjacency lists; links: [(bi,vi,bj,vj)]"""
    off, adj = [], []
    o = 0
    for b in blocks:
        off.append(o); o += len(b)
    n = o
    adj = [0]*n
    for bi, b in enumerate(blocks):
        for v in range(len(b)):
            m = b[v]
            while m:
                x = m & -m; m ^= x
                adj[off[bi]+v] |= 1 << (off[bi] + x.bit_length()-1)
    for (bi, vi, bj, vj) in links:
        a, c = off[bi]+vi, off[bj]+vj
        adj[a] |= 1 << c; adj[c] |= 1 << a
    return adj

def petersen_chain(t):
    blocks = [petersen() for _ in range(t)]
    links = [(i, 0, i+1, 5) for i in range(t-1)]
    return disjoint_union_chain(blocks, links)

def petersen_path_tail(k):
    """Petersen with a pendant path of length k attached to vertex 0"""
    g = petersen()
    n = 10 + k
    adj = [0]*n
    for v in range(10): adj[v] = g[v]
    prev = 0
    for i in range(k):
        w = 10+i
        adj[prev] |= 1 << w; adj[w] |= 1 << prev
        prev = w
    return adj

def random_regular_girth5(n, k, seed, maxit=200000):
    """random k-regular graph on n vertices with girth >= 5 via edge swaps"""
    rng = random.Random(seed)
    if n*k % 2: return None
    for attempt in range(60):
        stubs = [v for v in range(n) for _ in range(k)]
        rng.shuffle(stubs)
        adj = [0]*n
        edges = []
        ok = True
        for i in range(0, len(stubs), 2):
            u, v = stubs[i], stubs[i+1]
            if u == v or (adj[u] >> v & 1): ok = False; break
            adj[u] |= 1 << v; adj[v] |= 1 << u; edges.append((u, v))
        if not ok: continue
        def bad(adj):
            c = 0
            for u in range(n):
                for v in range(u+1, n):
                    cm = bin(adj[u] & adj[v]).count('1')
                    if adj[u] >> v & 1:
                        c += cm            # triangles
                    if cm >= 2: c += cm-1  # C4
            return c
        cur = bad(adj)
        it = 0
        while cur > 0 and it < maxit:
            it += 1
            i, j = rng.randrange(len(edges)), rng.randrange(len(edges))
            (a, b), (c, d) = edges[i], edges[j]
            if len({a, b, c, d}) < 4: continue
            if rng.random() < .5: c, d = d, c
            if (adj[a] >> c & 1) or (adj[b] >> d & 1): continue
            adj[a] ^= (1 << b); adj[b] ^= (1 << a)
            adj[c] ^= (1 << d); adj[d] ^= (1 << c)
            adj[a] |= 1 << c; adj[c] |= 1 << a
            adj[b] |= 1 << d; adj[d] |= 1 << b
            nb = bad(adj)
            if nb <= cur:
                cur = nb; edges[i] = (a, c); edges[j] = (b, d)
            else:
                adj[a] ^= (1 << c); adj[c] ^= (1 << a)
                adj[b] ^= (1 << d); adj[d] ^= (1 << b)
                adj[a] |= 1 << b; adj[b] |= 1 << a
                adj[c] |= 1 << d; adj[d] |= 1 << c
        if cur == 0 and is_connected(adj):
            return adj
    return None


# ================= drivers (python3 wowii133_families.py) =================

def main():
    # field sanity
    for q,F in FIELDS.items():
        nz=[e for e in F.elts if e!=F.zero]
        assert len(F.elts)==q, (q,len(F.elts))
        for a in nz:
            assert any(F.mul(a,b)==F.one for b in nz), ("no inverse",q,a)
    print("fields OK")
    print("=== small / classic ===")
    for n in range(3,16): check("C_%d"%n, cycle(n))
    for n in range(2,12): check("P_%d"%n, path_graph(n))
    for m in range(1,10): check("star K_1,%d"%m, star(m))
    for k in range(1,8): check("friendship F_%d"%k, friendship(k))
    check("Petersen", petersen())
    check("Kneser(5,2)=Petersen", kneser(5,2))
    print("=== incidence graphs of PG(2,q) (girth 6, bipartite, (q+1)-regular) ===")
    for q in [2,3,4,5,7,8,9]:
        t=time.time(); g=incidence_pg(q)
        assert not has_c4(g), q
        check("IncidencePG(2,%d)"%q, g, exact=(len(g)<=30))
        print("   (%.1fs, n=%d, deg=%d)"%(time.time()-t,len(g),bin(g[0]).count('1')))
    print("=== Erdos-Renyi orthogonal polarity graphs ER_q (extremal C4-free, rad 2) ===")
    for q in [2,3,4,5,7,8,9,11,13]:
        t=time.time(); g=polarity_graph(q)
        assert not has_c4(g), q
        assert is_connected(g)
        check("ER_%d"%q, g, exact=(len(g)<=32))
        print("   (%.1fs, n=%d, m=%d, maxdeg=%d)"%(time.time()-t,len(g),sum(bin(a).count('1') for a in g)//2,max(bin(a).count('1') for a in g)))
    g=hoffman_singleton()
    n=len(g)
    degs=set(bin(a).count('1') for a in g)
    print("HoSi n=%d degs=%s connected=%s C4free=%s diam=%d rad=%d"%(n,degs,is_connected(g),not has_c4(g),diameter(g),radius(g)))
    # girth check: no triangles (C4-free already checked)
    tri=sum(1 for u in range(n) for v in range(n) if u<v and (g[u]>>v&1) and (g[u]&g[v]))
    print("triangles containing an edge:",tri)
    S=sum_local_indep(g); print("sum alpha(N(v))=",S," l=",S/n," floor=",S//n)
    t=time.time()
    ok,best=induced_path_at_least(g, S//n+2, tries=50, seed=1)
    print("induced path >= %d ?"%(S//n+2), ok, "best seen",best, "%.1fs"%(time.time()-t))
    # how long can we push?  greedy exact-ish lower bound
    t=time.time()
    for tgt in range(S//n+2, 40):
        ok,_=induced_path_at_least(g,tgt,tries=60,seed=7)
        if not ok:
            print("randomised search fails at target",tgt,"(%.1fs)"%(time.time()-t)); break
        print("  found induced path with >=",tgt,"vertices")
    print("=== chains / attachments built on Petersen ===")
    for t in [2,3,4]: check("Petersen-chain x%d"%t, petersen_chain(t), exact=(t<=3))
    for k in [1,2,3,5,8]: check("Petersen+tail%d"%k, petersen_path_tail(k))
    print("=== random k-regular girth>=5 graphs ===")
    bad=0; tot=0
    for (n,k) in [(20,4),(24,4),(26,4),(19,4),(30,5),(32,5),(40,5),(30,6),(36,6),(42,6),(50,7),(40,4),(50,5),(60,6)]:
        for seed in range(1,4):
            g=random_regular_girth5(n,k,seed)
            if g is None: print("  (%d,%d) seed%d: construction failed"%(n,k,seed)); continue
            tot+=1
            ok=check("rand %d-reg girth5 n=%d s=%d"%(k,n,seed), g, exact=(n<=26))
            if not ok: bad+=1
    print("random regular tested=%d violations=%d"%(tot,bad))
    import random, itertools
    # --- verify structural lemma: C4-free => alpha(N(v)) = d(v) - t(v), l = (2m-3T)/n
    rng=random.Random(5); bad=0; tot=0
    for trial in range(3000):
        n=rng.randint(3,11); g=random_c4free(n,trial)
        if not is_connected(g): continue
        assert not has_c4(g)
        tot+=1
        m=sum(bin(a).count('1') for a in g)//2
        T=sum(1 for a,b,c in itertools.combinations(range(n),3) if (g[a]>>b&1) and (g[b]>>c&1) and (g[a]>>c&1))
        S=sum_local_indep(g)
        for v in range(n):
            t=sum(1 for x,y in itertools.combinations([i for i in range(n) if g[v]>>i&1],2) if g[x]>>y&1)
            if alpha(g,g[v]) != bin(g[v]).count('1')-t: bad+=1
            # neighbourhood induces a matching
            for x in range(n):
                if g[v]>>x&1: assert bin(g[x]&g[v]).count('1')<=1
        assert S==2*m-3*T, (S,m,T)
    print("structural lemma checked on %d random connected C4-free graphs, mismatches=%d"%(tot,bad))
    # --- obstacle witness: local surgery destroys min-degree bounds but not l
    g=hoffman_singleton(); n=50
    # subdivide edge (0, first neighbour)
    u=0; v=(g[0]&-g[0]).bit_length()-1
    adj=[x for x in g]+[0]
    adj[u]&=~(1<<v); adj[v]&=~(1<<u)
    w=50
    adj[u]|=1<<w; adj[w]|=1<<u; adj[v]|=1<<w; adj[w]|=1<<v
    print("HoSi with one subdivided edge:")
    check("HoSi/subdiv", adj, exact=False)
    delta=min(bin(a).count('1') for a in adj)
    S=sum_local_indep(adj)
    print("   delta=%d  floor(l)=%d  rad=%d  -> proven bounds give max(rad+2, delta+2)=%d, need %d"%(
       delta, S//len(adj), radius(adj), max(radius(adj)+2, delta+2), radius(adj)+S//len(adj)))

if __name__ == '__main__':
    import time as _t
    _s=_t.time()
    main()
    n_ok=sum(1 for r in RESULTS if r[8]); n_bad=len(RESULTS)-n_ok
    print('\nTOTAL structural-family graphs tested: %d   violations: %d   (%.1fs)'%(len(RESULTS), n_bad, _t.time()-_s))
