# PRO BRIEF v2 (GPT-5.6 Sol + Pro; code sandbox mandatory; no internet) — R46: what could kill the m = 5 local witness?
# Scope is deliberately narrow. Do NOT attempt a full m = 5 exclusion. Label every statement PROVED / COMPUTED / CONJECTURED / REFUTED.
Context. The relaxed local system for a minimal finite counterexample to the finite implication E677 ⟹ E255 (E677: x = y*(x*((y*x)*y));
E255: (((x*x)*x)*x) = x) uses ten universal E677 instances ("Core-10") plus the E255 defect; an explicit m = 5 witness satisfies
Core-10 + defect (250 chain equations checked). Hence m = 5 can die LOCALLY only if E677 forces an ADDITIONAL universal instance,
or a term coincidence, that the witness violates.
Tasks. (a) Enumerate the instances derivable from the twelve universal products with at most ONE new term (state the derivation
rule precisely and print the enumeration as a table). (b) For EACH enumerated instance, check whether the existing witness
violates it — the check must be executed in the sandbox and printed (witness tables and chain equations are given below).
(c) Report the enumeration even if nothing kills the witness; if something does, print the violated equation and the witness
values involved. No other work.

## DATA (appended by line-677; everything below is COMPUTED and machine-checked; parse it, do not retype it)
### D1. Base terms, base products, instances
Base symbols (elements of the quotient magma, distinct unless a coincidence is PROVED):
a, w, u, p, b, d, v, c, s0, p2, f2, g2. The 21 known base products are the dict PRODUCTS below
(key (x,y) means x*y; value the base symbol of the product). They arise from a with
w = a\a (so a*w = a), u = (a*a)*a via s0 = a*a, u*a = a (fixed point), p with a*p = u, b = p*a,
d = a*b ... and the second family p2, f2, g2 around b. E677 holds on the base at the ten pairs
INSTANCES, in the chain form of the function chain(x,y) (it asserts the base identity
y*(x*((y*x)*y)) = x from the products). Nothing else about the base is assumed.
### D2. Fibre semantics (the extension over a fibre of size m = 5)
Each base product x*y = z carries a table sigma[x,y]: for fibre coordinates s (of x) and t (of y),
sigma[x,y][s][t] is the fibre coordinate of (x,s)*(y,t); every row sigma[x,y][s] is a
permutation of {0,...,4} (left translations are bijections). E677 at the base pair (x,y) with
chain (y,x),(yx,y),(x,yxy),(y,inner) means, for all s,t in {0..4}:
    r1 = sigma[y,x][t][s]; r2 = sigma[yx,y][r1][t]; r3 = sigma[x,yxy][s][r2]; sigma[y,inner][t][r3] == s.
Ten instances × 25 (s,t) = 250 chain equations. The E255 defect at a: with s0 = a*a, u = s0*a,
u*a = a on the base, at fibre coordinate s: r1 = sigma[a,a][s][s]; r2 = sigma[s0,a][r1][s];
E255 fails at (a,s) iff sigma[u,a][r2][s] != s. The witness fails at s in {0,1,3,4}.
### D3. What "derivable with at most one new term" must mean (state your rule; this is the intended one)
An E677 instance at a base pair (x,y) is available iff its four chain products (y,x), (y*x,y),
(x, (y*x)*y), (y, inner) are all in PRODUCTS, possibly after adjoining ONE new base symbol z as
the value of one so-far-unknown product (then the instance's last product is forced to equal x by
E677 on the base, and any product of the form x'*z or z*x' that the chain needs must be in
PRODUCTS or be that same single new symbol). Also list the base COINCIDENCES forced by
left-cancellation (x*y1 = x*y2 implies y1 = y2 in a finite E677 magma) and by the chain
assertion — a forced coincidence identifies two symbols and may create new instances; treat each
as a candidate and check the witness under it (identified symbols must share sigma tables, which
is itself a check).
### D4. Parser + checker (verbatim from the shipped replay script; run it first, it must print PASS)
```python
PRODUCTS = {
    ("u", "a"): "a", ("a", "w"): "a", ("a", "u"): "w", ("a", "p"): "u",
    ("a", "b"): "p", ("a", "d"): "b", ("p", "a"): "b", ("v", "b"): "b",
    ("b", "c"): "b", ("b", "v"): "c", ("d", "v"): "a", ("c", "d"): "v",
    ("b", "b"): "d", ("d", "b"): "v", ("a", "a"): "s0", ("s0", "a"): "u",
    ("b", "p2"): "v", ("b", "f2"): "p2", ("p2", "b"): "f2",
    ("b", "g2"): "f2", ("f2", "f2"): "g2",
}
INSTANCES = [
    ("p", "a"), ("v", "d"), ("c", "b"), ("a", "u"), ("b", "v"),
    ("b", "a"), ("b", "b"), ("a", "a"), ("p2", "b"), ("f2", "b"),
]
ROW = re.compile(
    r"^sigma\[([A-Za-z0-9]+),([A-Za-z0-9]+)\]\[(\d+)\] = \[([0-9 ]+)\]$",
    re.MULTILINE,
)


def chain(x: str, y: str) -> tuple[tuple[str, str], ...]:
    yx = PRODUCTS[(y, x)]
    yxy = PRODUCTS[(yx, y)]
    inner = PRODUCTS[(x, yxy)]
    assert PRODUCTS[(y, inner)] == x
    return (y, x), (yx, y), (x, yxy), (y, inner)
def load(text):
    sigma = {}
    for m in ROW.finditer(text):
        pair = (m.group(1), m.group(2)); row = int(m.group(3)); vals = [int(v) for v in m.group(4).split()]
        assert row in range(5) and sorted(vals) == list(range(5))
        sigma.setdefault(pair, [None]*5)[row] = vals
    assert len(sigma) == 21 and sum(r is not None for t in sigma.values() for r in t) == 105
    return sigma
def check(sigma):
    checked = 0
    for x, y in INSTANCES:
        p1, p2, p3, p4 = chain(x, y)
        for s in range(5):
            for t in range(5):
                r1 = sigma[p1][t][s]; r2 = sigma[p2][r1][t]; r3 = sigma[p3][s][r2]
                assert sigma[p4][t][r3] == s; checked += 1
    defect = [s for s in range(5) if sigma[("u","a")][sigma[("s0","a")][sigma[("a","a")][s][s]][s]][s] != s]
    assert checked == 250 and defect == [0, 1, 3, 4]
    print("PASS m=5 local witness; defect coordinates", defect)
```
### D5. The witness (105 rows; feed this block to load())
```text
sigma[u,a][0] = [1 4 3 2 0]
sigma[u,a][1] = [3 2 4 0 1]
sigma[u,a][2] = [4 0 2 1 3]
sigma[u,a][3] = [3 2 1 4 0]
sigma[u,a][4] = [3 4 0 1 2]
sigma[a,w][0] = [1 3 0 4 2]
sigma[a,w][1] = [1 0 4 3 2]
sigma[a,w][2] = [3 4 0 2 1]
sigma[a,w][3] = [4 2 0 1 3]
sigma[a,w][4] = [1 2 0 4 3]
sigma[a,u][0] = [0 2 3 4 1]
sigma[a,u][1] = [3 1 0 4 2]
sigma[a,u][2] = [1 2 3 4 0]
sigma[a,u][3] = [0 1 2 3 4]
sigma[a,u][4] = [1 4 0 2 3]
sigma[a,p][0] = [0 4 1 3 2]
sigma[a,p][1] = [3 1 4 2 0]
sigma[a,p][2] = [1 4 3 2 0]
sigma[a,p][3] = [4 3 0 1 2]
sigma[a,p][4] = [0 4 2 1 3]
sigma[a,b][0] = [0 1 4 2 3]
sigma[a,b][1] = [1 2 4 3 0]
sigma[a,b][2] = [4 3 1 0 2]
sigma[a,b][3] = [0 4 2 3 1]
sigma[a,b][4] = [1 0 3 2 4]
sigma[a,d][0] = [4 0 2 1 3]
sigma[a,d][1] = [0 2 1 3 4]
sigma[a,d][2] = [0 1 3 4 2]
sigma[a,d][3] = [2 4 3 0 1]
sigma[a,d][4] = [1 3 0 4 2]
sigma[p,a][0] = [1 0 4 2 3]
sigma[p,a][1] = [2 3 0 1 4]
sigma[p,a][2] = [0 4 2 3 1]
sigma[p,a][3] = [3 2 1 4 0]
sigma[p,a][4] = [4 1 3 0 2]
sigma[v,b][0] = [1 4 0 2 3]
sigma[v,b][1] = [4 3 1 0 2]
sigma[v,b][2] = [2 0 3 4 1]
sigma[v,b][3] = [3 1 0 4 2]
sigma[v,b][4] = [3 2 4 1 0]
sigma[b,c][0] = [3 1 2 4 0]
sigma[b,c][1] = [1 2 4 0 3]
sigma[b,c][2] = [0 3 1 2 4]
sigma[b,c][3] = [4 0 3 1 2]
sigma[b,c][4] = [2 4 0 3 1]
sigma[b,v][0] = [1 3 2 4 0]
sigma[b,v][1] = [2 4 3 0 1]
sigma[b,v][2] = [0 2 1 3 4]
sigma[b,v][3] = [4 1 0 2 3]
sigma[b,v][4] = [3 0 4 1 2]
sigma[d,v][0] = [1 0 4 2 3]
sigma[d,v][1] = [4 0 1 2 3]
sigma[d,v][2] = [0 1 4 2 3]
sigma[d,v][3] = [0 1 4 2 3]
sigma[d,v][4] = [1 4 0 2 3]
sigma[c,d][0] = [2 3 1 0 4]
sigma[c,d][1] = [1 4 3 2 0]
sigma[c,d][2] = [3 0 4 1 2]
sigma[c,d][3] = [4 2 0 3 1]
sigma[c,d][4] = [0 1 2 4 3]
sigma[b,b][0] = [4 1 3 0 2]
sigma[b,b][1] = [4 1 3 0 2]
sigma[b,b][2] = [4 1 3 0 2]
sigma[b,b][3] = [4 1 3 0 2]
sigma[b,b][4] = [4 1 3 0 2]
sigma[d,b][0] = [2 0 1 3 4]
sigma[d,b][1] = [4 3 0 2 1]
sigma[d,b][2] = [0 4 2 1 3]
sigma[d,b][3] = [1 2 3 4 0]
sigma[d,b][4] = [3 1 4 0 2]
sigma[a,a][0] = [0 4 1 3 2]
sigma[a,a][1] = [0 1 3 4 2]
sigma[a,a][2] = [4 0 3 1 2]
sigma[a,a][3] = [1 4 0 3 2]
sigma[a,a][4] = [2 0 3 4 1]
sigma[s0,a][0] = [1 4 3 0 2]
sigma[s0,a][1] = [3 2 0 1 4]
sigma[s0,a][2] = [4 3 0 2 1]
sigma[s0,a][3] = [1 3 2 4 0]
sigma[s0,a][4] = [2 3 1 0 4]
sigma[b,p2][0] = [3 2 4 1 0]
sigma[b,p2][1] = [1 4 3 0 2]
sigma[b,p2][2] = [0 4 3 1 2]
sigma[b,p2][3] = [3 1 4 0 2]
sigma[b,p2][4] = [0 2 1 4 3]
sigma[b,f2][0] = [2 4 1 0 3]
sigma[b,f2][1] = [4 2 1 0 3]
sigma[b,f2][2] = [3 1 0 4 2]
sigma[b,f2][3] = [0 2 4 3 1]
sigma[b,f2][4] = [1 3 2 0 4]
sigma[p2,b][0] = [2 4 1 3 0]
sigma[p2,b][1] = [4 0 2 3 1]
sigma[p2,b][2] = [4 1 2 0 3]
sigma[p2,b][3] = [1 0 3 2 4]
sigma[p2,b][4] = [0 1 4 3 2]
sigma[b,g2][0] = [0 1 2 4 3]
sigma[b,g2][1] = [4 0 3 2 1]
sigma[b,g2][2] = [1 2 3 0 4]
sigma[b,g2][3] = [2 1 4 0 3]
sigma[b,g2][4] = [2 0 1 3 4]
sigma[f2,f2][0] = [2 1 4 3 0]
sigma[f2,f2][1] = [1 4 0 3 2]
sigma[f2,f2][2] = [3 1 4 0 2]
sigma[f2,f2][3] = [3 1 4 0 2]
sigma[f2,f2][4] = [0 3 4 2 1]
```
Defect trace at s* = 0: r1 = sigma[a,a][0](0) = 0; r2 = sigma[s0,a][0](0) = 1; sigma[u,a][1](0) = 3 != 0.
Chains of the ten instances (pairs in order p1..p4):
(a,u): (u,a),(a,u),(a,w),(u,a)
(b,a): (a,b),(p,a),(b,b),(a,d)
(b,b): (b,b),(d,b),(b,v),(b,c)
(b,v): (v,b),(b,v),(b,c),(v,b)
(p,a): (a,p),(u,a),(p,a),(a,b)
(v,d): (d,v),(a,d),(v,b),(d,b)
(c,b): (b,c),(b,b),(c,d),(b,v)
(a,a): (a,a),(s0,a),(a,u),(a,w)
(p2,b): (b,p2),(v,b),(p2,b),(b,f2)
(f2,b): (b,f2),(p2,b),(f2,f2),(b,g2)
chain equations checked = 250; passed = 250; failed = 0
