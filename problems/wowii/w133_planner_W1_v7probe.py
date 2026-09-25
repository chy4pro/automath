# V7 execution probe on the planner's own artifact w133_planner_W1_recompute.py.
# Method per RULING L: settle LIVE vs TAUTOLOGICAL by EXECUTION, not by reading assert lines.
# For each assertion, inject a fault that SHOULD trip it. An assertion that survives every
# injected fault is not evidence.
from itertools import combinations
q = 5

def build(norm_ok=True, inc_ok=True, extra_edge=False):
    def norm(v):
        for c in v:
            if c % q:
                inv = pow(c, q-2, q)
                return tuple((x*inv) % q for x in v)
        return None
    def norm_bad(v):                     # fault A: normalisation collapses too much
        return tuple(x % 2 for x in v) if any(v) else None
    N = norm if norm_ok else norm_bad
    pts = sorted({N(v) for v in ((a,b,c) for a in range(q) for b in range(q) for c in range(q)) if N(v)})
    lines = pts[:]
    def inc(p,l): return sum(p[i]*l[i] for i in range(3)) % q == 0
    def inc_bad(p,l): return sum(p[i]*l[i] for i in range(3)) % q in (0,1)   # fault B
    I = inc if inc_ok else inc_bad
    V = [('P',p) for p in pts] + [('L',l) for l in lines]
    adj = {v:set() for v in V}
    for p in pts:
        for l in lines:
            if I(p,l):
                adj[('P',p)].add(('L',l)); adj[('L',l)].add(('P',p))
    if extra_edge:                        # fault C: one spurious edge creating a C4
        a,b = V[0], V[1]
        adj[a].add(b); adj[b].add(a)
    return pts, V, adj

def c4_free(a):
    return all(len(a[x]&a[y])<2 for x,y in combinations(list(a),2))

CHECKS = {
 "len(pts)==31"        : lambda pts,V,adj: len(pts)==31,
 "deg set == {6}"      : lambda pts,V,adj: set(len(adj[v]) for v in V)=={6},
 "len(V)==62"          : lambda pts,V,adj: len(V)==62,
 "c4_free(adj)"        : lambda pts,V,adj: c4_free(adj),
}
FAULTS = {
 "none (baseline)"        : dict(),
 "A: broken normalisation": dict(norm_ok=False),
 "B: broken incidence"    : dict(inc_ok=False),
 "C: spurious edge"       : dict(extra_edge=True),
}
print(f"{'check':<22}" + "".join(f"{k:<26}" for k in FAULTS))
verdict = {}
for name, fn in CHECKS.items():
    row, tripped = [], 0
    for fname, kw in FAULTS.items():
        try:
            ok = fn(*build(**kw))
        except Exception:
            ok = False
        if fname.startswith("none"):
            row.append("PASS" if ok else "!! baseline broken")
        else:
            row.append("TRIPPED ✓" if not ok else "survived ✗")
            tripped += (not ok)
    verdict[name] = tripped
    print(f"{name:<22}" + "".join(f"{c:<26}" for c in row))
print()
for name, t in verdict.items():
    print(f"  {name:<22} tripped by {t}/3 injected faults -> {'LIVE' if t else 'TAUTOLOGICAL'}")
print()
print("VERDICT:", "all assertions LIVE" if all(verdict.values()) else "at least one assertion cannot fail")
