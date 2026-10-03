# exhaustive search for minimal good sets: independent I, connected in distance-2 graph, s(I)=4|I|-|N[I]|>=1
from mis import bits, popcount
def dist2_graph(adj):
    n=len(adj); H=[0]*n
    for v in range(n):
        N=adj[v]; h=0
        for u in bits(N): h|=adj[u]
        H[v]=h & ~adj[v] & ~(1<<v)
    return H
def min_good(adj, kmax, need=1, roots=None, verbose=False):
    """return smallest k<=kmax with an independent H-connected I of size k and s(I)>=need (and an example)"""
    n=len(adj); H=dist2_graph(adj)
    closed=[adj[v]|(1<<v) for v in range(n)]
    best=[None]
    found={}
    # ESU: enumerate connected subsets containing root v with all other vertices > v
    roots=range(n) if roots is None else roots
    for k in range(1,kmax+1):
        for v in roots:
            # recursive
            def extend(Iset, Imask, ext, N, size, forb):
                if size==k:
                    s=4*k-popcount(N)
                    if s>=need: return Iset
                    return None
                while ext:
                    w=(ext&-ext).bit_length()-1
                    ext&=~(1<<w)
                    # new exclusive neighbours of w: H-neighbours > v not in Imask, not adjacent to I, not in current neighbourhood of I in H
                    nb=H[w] & ~((1<<(v+1))-1)
                    # exclude vertices adjacent to I or in I or already H-neighbours of I (ESU exclusive neighbourhood)
                    curH=0
                    for x in Iset: curH|=H[x]
                    newext=ext | (nb & ~curH & ~Imask)
                    # independence: remove vertices adjacent to w
                    newext&=~(forb|adj[w])
                    r=extend(Iset+[w], Imask|(1<<w), newext & ~(1<<w), N|closed[w], size+1, forb|adj[w])
                    if r: return r
                return None
            ext=H[v] & ~((1<<(v+1))-1)
            r=extend([v],1<<v,ext,closed[v],1,adj[v])
            if r:
                return k,r
        if verbose: print('no good set of size',k,flush=True)
    return None
