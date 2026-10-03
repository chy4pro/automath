import itertools, sys, pickle, time
n=6
def partitions_of(others):
    res=[]
    others=list(others)
    res.append((frozenset(others),))
    for k in (1,2):
        for c in itertools.combinations(others,k):
            a=frozenset(c); b=frozenset(others)-a
            res.append((b,a))
    return res
opts=[partitions_of([q for q in range(n) if q!=p]) for p in range(n)]
pairs=list(itertools.combinations(range(n),2))
t0=time.time()
sols=[]
apex={pr:0 for pr in pairs}
triples={}
choice=[None]*n
def rec(p):
    if p==n:
        sols.append(tuple(choice)); return
    for part in opts[p]:
        ok=True; added=[]; addedt=[]
        for C in part:
            for pr in itertools.combinations(sorted(C),2):
                apex[pr]+=1; added.append(pr)
                if apex[pr]>2: ok=False
            for t in itertools.combinations(sorted(C),3):
                if t in triples: ok=False
                triples[t]=p; addedt.append(t)
        if ok:
            choice[p]=part; rec(p+1)
        for pr in added: apex[pr]-=1
        for t in addedt:
            if triples.get(t)==p: del triples[t]
rec(0)
print('raw structures',len(sols),time.time()-t0)
# canonicalize
def canon(sol):
    best=None
    for perm in itertools.permutations(range(n)):
        # relabel: new point perm[p] has classes {perm[q]}
        rel=[None]*n
        for p in range(n):
            rel[perm[p]]=tuple(sorted(tuple(sorted(perm[q] for q in C)) for C in sol[p]))
        key=tuple(rel)
        if best is None or key<best: best=key
    return best
can=set(canon(s) for s in sols)
print('canonical',len(can),time.time()-t0)
pickle.dump(sorted(can),open('struct6.pkl','wb'))
