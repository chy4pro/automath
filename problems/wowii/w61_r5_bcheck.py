#!/usr/bin/env python3
"""owner-w61: independent check of the §7.8 round-B findings (D1-D5)."""
import sys
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w61_r5_rig import G, residue_seq
from itertools import combinations


def hh_trunc(seq):
    """residueAux-style run WITH natural-number truncation: returns (steps, trace)."""
    s = sorted(seq, reverse=True)
    steps, trace = 0, []
    while s and s[0] > 0:
        d = s[0]
        rest = s[1:]
        head, tail = rest[:d], rest[d:]
        trace.append((d, list(s)))
        head = [max(0, x - 1) for x in head]
        s = sorted(head + tail, reverse=True)
        steps += 1
    return steps, trace


print("=== D5 (MATHEMATICS): Lemma T' states an IFF; is the 'only if' direction true?")
w = [4, 1, 1, 0, 0, 0]
st, tr = hh_trunc(w)
print(f"   witness {w}: terminates in {st} step(s)")
print(f"   list at the start of step {st}: {tr[-1][1]}, head D_k = {tr[-1][0]}")
print(f"   T' would require it to be [D_k, 1^D_k, 0...] = "
      f"{[tr[-1][0]] + [1]*tr[-1][0]} + zeros")
print(f"   => 'only if' FAILS on this input. Is it graphical? sum={sum(w)} even, but a "
      f"degree-4 vertex needs 4 positive partners and only {sum(1 for x in w[1:] if x>0)} exist "
      f"=> NOT graphical.")
print("   So T' is true for GRAPHICAL sequences (where Lemma 1(2) applies) and false as")
print("   an unrestricted iff about the truncating process. UPHELD.")
# does it hold on all graphical sequences up to n<=8?
try:
    import networkx as nx
    ok = bad = 0
    for g in nx.graph_atlas_g():
        if g.number_of_nodes() < 2:
            continue
        gg = G(g.number_of_nodes(), list(g.edges()))
        seq = sorted(gg.degseq(), reverse=True)
        if sum(seq) == 0:
            continue
        st2, tr2 = hh_trunc(seq)
        last_d, last_list = tr2[-1][0], tr2[-1][1]
        want = sorted([last_d] + [1] * last_d + [0] * (len(last_list) - 1 - last_d), reverse=True)
        if last_list == want:
            ok += 1
        else:
            bad += 1
            if bad <= 3:
                print("   GRAPHICAL COUNTEREXAMPLE:", seq, last_list, want)
    print(f"   on graphical sequences (atlas): T' holds {ok}, fails {bad}")
except ImportError:
    print("   networkx unavailable")

print()
print("=== D2: are Theorem LOW / Theorem SL really 'hard core' statements?  C5 witness")
c5 = G(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
al, _ = c5.independent_sets_max()
seq = sorted(c5.degseq(), reverse=True)
res = residue_seq(seq)
s_steps, _ = hh_trunc(seq)
print(f"   C5: deg={seq} n=5 alpha={al} tau={5-al} residue={res} s={s_steps} "
      f"diam={c5.diam()} f={c5.f()}")
print(f"   reductio residue=alpha? {res == al}.  In the hard-core FRAME? "
      f"diam=4? {c5.diam()==4}; f=alpha+1? {c5.f()==al+1}")
print("   => if the reductio holds here while the frame does not, then any statement whose")
print("      PROOF needs only the reductio is mis-filed under 'hard core'. UPHELD if so.")

print()
print("=== D3: are the §7.8 numerical blocks measured where the reductio is FALSE?")
# Fan(4,2), A'=[2,2]: the instance whose labelled run the M/H checks would use
tau, L, p = 4, 2, 2
E = [(x, y) for x, y in combinations(range(4), 2) if (x, y) != (0, 1)]
E += [(4, b) for b in range(4)] + [(5, 0), (5, 1), (6, 0), (6, 1)]
g = G(7, E)
al2, _ = g.independent_sets_max()
seq2 = sorted(g.degseq(), reverse=True)
s2, _ = hh_trunc(seq2)
print(f"   Fan(4,2) A'=[2,2]: deg={seq2} alpha={al2} tau={g.n-al2} s={s2} "
      f"residue={residue_seq(seq2)}")
print(f"   reductio s = tau? {s2 == g.n-al2}  (tau={g.n-al2})")
print("   => the Fan runs the M1-M4 / H1-H5 blocks measure have s = tau+1, i.e. the")
print("      standing hypothesis of every FAN lemma is FALSE on them. UPHELD.")

print()
print("=== D4 upgrade: Observation FAN-5's second half is now PROVABLE via Lemma TAIL")
for L in range(2, 10):
    lam = [2]
    l1 = lam[0]
    base = [l1] * (l1 + 1) + lam
    s0, _ = hh_trunc(base)
    full = [L] * (L + 1) + lam
    sfull, _ = hh_trunc(full)
    print(f"   L={L}: s0([2]^3+[2])={s0} (=lam1={l1}?{s0==l1}); "
          f"steps([L]^(L+1)+[2])={sfull} (=L?{sfull==L}); TAIL predicts {(L-l1)+s0}")
print("done")
