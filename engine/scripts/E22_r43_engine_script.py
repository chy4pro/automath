import itertools

def build_pg2(q):
    """Points/lines of PG(2,q) as sorted tuples of field elements."""
    if q == 2:
        add = lambda a,b: a^b
        mul = lambda a,b: a&b
    elif q == 3:
        add = lambda a,b: (a+b)%3
        mul = lambda a,b: (a*b)%3
    elif q == 4:
        # GF(4) = F2[t]/(t^2+t+1); encode 0,1,t,t+1 as 0,1,2,3
        def add(a,b): return a^b
        MUL = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
        mul = lambda a,b: MUL[a][b]
    else:
        raise ValueError("q must be 2,3,4")
    els = list(range(q))
    vecs = [(a,b,c) for a in els for b in els for c in els]
    pts, rep = [], set()
    for v in vecs:
        if v != (0,0,0):
            norm = tuple(sorted(
                tuple(mul(lam,x) for x in v) for lam in els))
            if norm[0] not in rep:
                rep.add(norm[0]); pts.append(v)
    lines = []
    for (a,b,c) in vecs:
        if (a,b,c) != (0,0,0):
            L = frozenset(p for p in pts
                          if add(add(mul(a,p[0]),mul(b,p[1])),mul(c,p[2]))==0)
            if L not in lines: lines.append(L)
    return pts, lines

def moments(pts, lines, S):
    ks = [len(S & L) for L in lines]
    s1 = sum(ks)
    s2 = sum(k*(k-1)//2 for k in ks)
    s3 = sum(k*(k-1)*(k-2)//6 for k in ks)
    return s1, s2, s3

def report(q, sizes):
    pts, lines = build_pg2(q)
    print(f"=== PG(2,{q}): {len(pts)} points, {len(lines)} lines ===")
    for m in sizes:
        print(f"-- all subsets of size {m}: "
              f"{len(list(itertools.combinations(pts,m)))} enumerated --")
        seen = {}
        for combo in itertools.combinations(pts, m):
            S = frozenset(combo)
            s1,s2,s3 = moments(pts, lines, S)
            assert s1 == (q+1)*m, "I1 failed"
            assert s2 == m*(m-1)//2, "I2 failed"
            seen.setdefault(s3, []).append(S)
        print(f"   I1, I2 verified for all subsets. "
              f"Distinct third-moment values: {sorted(seen)}")
        for v in sorted(seen):
            ex = seen[v][0]
            print(f"     value {v}: example {sorted(ex)}")
    print()

report(2, [3,4])
report(3, [4])
report(4, [5])
