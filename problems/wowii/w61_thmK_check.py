import sys, random
sys.path.insert(0,'$HOME/workspace/claudecode/automath/problems/wowii')
from w61_blockocc import adj_masks, is_connected, max_indep_sets, hh_labelled
import networkx as nx
from networkx.generators.atlas import graph_atlas_g

rng = random.Random(7)
hits = fails = tested = 0
wit = None
def test(n, edges):
    global hits, fails, tested, wit
    a = adj_masks(n, edges)
    if not is_connected(a, n): return
    degs = [bin(x).count('1') for x in a]
    al, isets = max_indep_sets(a, n)
    tau = n - al
    tested += 1
    heads,_,_,_ = hh_labelled(degs)
    if n - len(heads) != al: return          # need reductio residue = alpha
    for S in isets:
        B = [v for v in range(n) if not (S>>v & 1)]
        eB = sum(1 for u,v in edges if not (S>>u&1) and not (S>>v&1))
        if min(degs[b] for b in B) >= tau+1:
            hits += 1
            if eB != tau*(tau-1)//2:          # Theorem K: B must be a CLIQUE
                fails += 1
                if wit is None: wit=(n,edges,degs,tau,eB,tau*(tau-1)//2)

small=[]
for G in graph_atlas_g():
    if G.number_of_nodes()<2 or not nx.is_connected(G): continue
    small.append((G.number_of_nodes(), [(u,v) for u,v in G.edges()]))
for n,e in small: test(n,e)
print(f"[TheoremK n<=7] tested={tested} hits(all-B-high & residue=alpha)={hits} NOT-clique={fails}")
for n,edges in small:
    if n!=7: continue
    for mask in range(1,1<<7):
        test(8, list(edges)+[(7,v) for v in range(7) if mask>>v&1])
print(f"[TheoremK +n=8]  tested={tested} hits={hits} NOT-clique={fails}")
for n in range(9,13):
    for _ in range(1500):
        p = rng.choice([0.3,0.4,0.5,0.6,0.7,0.8])
        test(n, [(u,v) for u in range(n) for v in range(u+1,n) if rng.random()<p])
print(f"[TheoremK +rnd]  tested={tested} hits={hits} NOT-clique={fails}")
print("WITNESS", wit)
