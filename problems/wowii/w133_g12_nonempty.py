#!/usr/bin/env python3
"""
Round 3, planner requirement (1):
  non-emptiness evidence for the class  { C4-free,  diam = 2,  l > 3 }
  which is the hypothesis class of Theorem G12 (draft s13.1).

Also: structured-family probe for conjecture (G+k) and Lemma G14 (pocket 2).
Everything is computed; nothing is asserted from memory.
"""
import sys, itertools
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    girth, connected, hoffman_singleton,
                                    greedy_long_induced_path, is_induced_path)

def facts(name, n, E):
    adj = neighbours(E, n); D = alldist(adj); e, r = ecc_rad(D); a = avec(adj)
    S = sum(a)
    return dict(name=name, n=n, m=len(E), adj=adj, D=D, rad=r, diam=max(e),
                a=a, S=S, l=S / n, mu=min(a), amax=max(a),
                c4free=not has_c4(adj), girth=girth(adj), conn=connected(adj))

def show_g12(f):
    ok = f['c4free'] and f['diam'] == 2 and f['l'] > 3
    P = greedy_long_induced_path(f['adj'])
    print(f"  {f['name']:<34} n={f['n']:<4} C4-free={f['c4free']} diam={f['diam']} "
          f"l={f['l']:.3f} -> in G12 class: {ok}")
    if ok:
        print(f"      => G12 predicts path >= 6;  induced-path certificate = {len(P)}  "
              f"{'OK' if len(P) >= 6 else 'FAIL'}")
    return ok

# ---- circulant helper for the pocket-2 probe -------------------------------
def circulant(n, conns):
    E = set()
    for v in range(n):
        for c in conns:
            E.add(tuple(sorted((v, (v + c) % n))))
    return n, sorted(E)

if __name__ == "__main__":
    print("=== (1) NON-EMPTINESS of the G12 class {C4-free, diam=2, l>3} ===")
    n0, E0 = hoffman_singleton()
    witnesses = 0
    witnesses += show_g12(facts("Hoffman-Singleton", n0, E0))
    # comparison points that just miss the class
    from w133_r3_counterexample import neighbours as _nb
    pet_E = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
             (0,5),(1,6),(2,7),(3,8),(4,9)]
    show_g12(facts("Petersen (l=3 exactly -> excluded)", 10, pet_E))
    show_g12(facts("C5", 5, [(0,1),(1,2),(2,3),(3,4),(4,0)]))
    print(f"  ==> witnesses found: {witnesses}  "
          f"({'CLASS NON-EMPTY, G12 is NOT vacuous' if witnesses else 'class empty so far'})")

    print()
    print("=== (2) pocket-2 probe: (G+k) and Lemma G14 on structured families ===")
    fams = [("Hoffman-Singleton", n0, E0), ("Petersen", 10, pet_E)]
    # 4-regular circulants that are C4-free, searched for large radius
    for n in range(17, 46):
        for k in range(3, n // 2):
            nn, EE = circulant(n, [1, k])
            f = facts(f"C_{n}(1,{k})", nn, EE)
            if f['c4free'] and f['mu'] >= 4 and f['rad'] >= 5:
                fams.append((f"C_{n}(1,{k})", nn, EE)); break
        if len(fams) > 6:
            break
    for name, n, E in fams:
        f = facts(name, n, E)
        P = greedy_long_induced_path(f['adj'])
        gk = [k for k in range(3, 8) if f['mu'] >= k - 1 and f['amax'] >= k
              and f['rad'] >= 2]
        need = {k: f['rad'] + k for k in gk}
        bad = [k for k in gk if len(P) < need[k]]
        g14 = (f['mu'] >= 4 and f['rad'] >= 5)
        print(f"  {name:<20} n={f['n']:<4} rad={f['rad']} mu={f['mu']} amax={f['amax']} "
              f"path>={len(P):<3} | (G+k) applies k={gk} need={list(need.values())} "
              f"violations={bad} | G14 applies={g14}"
              + (f" need path>={f['rad']+4} -> {'OK' if len(P) >= f['rad']+4 else 'FAIL'}" if g14 else ""))

# ---------------------------------------------------------------------------
def random_reg_girth5(n, deg, seed, tries=400):
    """greedy: add edges only between vertices at distance >= 4 (=> girth >= 5)."""
    import random
    rng = random.Random(seed)
    for _ in range(tries):
        adj = [set() for _ in range(n)]
        pool = [v for v in range(n) for _ in range(deg)]
        rng.shuffle(pool)
        stuck = 0
        while stuck < 3000:
            cand = [v for v in range(n) if len(adj[v]) < deg]
            if not cand:
                break
            u = rng.choice(cand)
            # BFS distance from u
            import collections
            dist = {u: 0}; q = collections.deque([u])
            while q:
                a = q.popleft()
                if dist[a] >= 3: continue
                for b in adj[a]:
                    if b not in dist:
                        dist[b] = dist[a] + 1; q.append(b)
            ok = [v for v in cand if v != u and dist.get(v, 99) >= 4]
            if not ok:
                stuck += 1; continue
            v = rng.choice(ok)
            adj[u].add(v); adj[v].add(u)
        if all(len(adj[v]) == deg for v in range(n)):
            E = sorted({tuple(sorted((u, v))) for u in range(n) for v in adj[u]})
            return n, E
    return None

def circulant_note():
    print("  NOTE: every circulant C_n(a,b) of degree 4 contains a C4, because")
    print("        0 = a+(-a) = b+(-b) gives two representations => 4-cycle.")
    print("        So NO circulant of degree >= 4 is C4-free; that family cannot")
    print("        supply G14 test graphs at all.")

if __name__ == "__main__" and "--g14" in sys.argv:
    print()
    print("=== (3) Lemma G14 test graphs: mu>=4 and rad>=5, C4-free ===")
    circulant_note()
    for n in (90, 120, 150, 180):
        got = random_reg_girth5(n, 4, seed=n)
        if not got: 
            print(f"  n={n}: construction failed"); continue
        f = facts(f"rand 4-reg girth5 n={n}", *got)
        P = greedy_long_induced_path(f['adj'], tries=1500)
        applies = f['c4free'] and f['mu'] >= 4 and f['rad'] >= 5
        print(f"  n={f['n']:<4} girth={f['girth']} C4-free={f['c4free']} rad={f['rad']} "
              f"mu={f['mu']} l={f['l']:.2f} path>={len(P)} | G14 applies={applies}"
              + (f" need >= rad+4 = {f['rad']+4} -> {'OK' if len(P)>=f['rad']+4 else 'FAIL'}"
                 if applies else ""))
