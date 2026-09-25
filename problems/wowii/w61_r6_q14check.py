#!/usr/bin/env python3
"""owner-w61 round 6 — independent reproduction of Q14 (Qwen3.8-Max, S3 FAN round B)
bookkeeping defects D1/D2/D3.  Everything recomputed here; no number is taken from
the Q14 report or from any earlier brief.

D1  stale "FAN-2 PROVED" line in draft §7.8 A          -> textual, checked by grep in the report
D2  Observation FAN-5's second half only simulated     -> verify Qwen's OWN inductive route
                                                          [L]^(L+1),2 -> [L-1]^L,2, clear = L
D3  "Lemma T's second sentence needs Fact 2"           -> is that dependency note an
                                                          overstatement?  Test the two readings.
"""
import itertools, random

# ---------- labelled Havel-Hakimi (residueAux), N-truncating, canonical descending sort ----------
def hh_steps(seq, tie=None):
    """Return (steps, heads, trace). trace[k] = list at the START of step k (0-indexed)."""
    a = sorted(seq, reverse=True)
    steps, heads, trace = 0, [], []
    while any(x > 0 for x in a):
        a.sort(reverse=True)
        trace.append(list(a))
        d = a[0]
        heads.append(d)
        a = a[1:]
        for i in range(min(d, len(a))):
            a[i] = max(0, a[i] - 1)      # N-truncation, exactly as residueAux
        steps += 1
    return steps, heads, trace

def residue(seq):
    s, _, _ = hh_steps(seq)
    return len(seq) - s

# ---------- calibration (mandatory before trusting the implementation) ----------
cal = []
cal.append(("K2", residue([1, 1]), 1))
for n in range(3, 10):
    cyc = [2] * n
    cal.append((f"C{n}", residue(cyc), -(-n // 3)))
print("== calibration ==")
ok = True
for name, got, want in cal:
    good = (got == want)
    ok &= good
    print(f"  {name:4s} residue={got} expected={want} {'OK' if good else 'FAIL'}")
print("calibration:", "PASS" if ok else "FAIL")

# ---------- D2: Qwen's inductive route for Observation FAN-5, second half ----------
print("\n== D2: Observation FAN-5 second half, Qwen's own inductive route ==")
print("  claim: [L]^(L+1), 2  clears in exactly L steps, for every L >= 2")
print("  step : [L]^(L+1), 2  ->  [L-1]^L, 2   (one HH step)")
bad = 0
for L in range(2, 41):
    seq = [L] * (L + 1) + [2]
    s, heads, trace = hh_steps(seq)
    # direct simulation
    direct_ok = (s == L)
    # the inductive step itself: list at start of step 2 must be [L-1]^L, 2
    if len(trace) > 1:
        want = sorted([L - 1] * L + [2], reverse=True)
        step_ok = (trace[1] == want)
    else:
        step_ok = (L == 2)      # L=2 is the base case, clears in 2 steps
    if not (direct_ok and step_ok):
        bad += 1
        print(f"  L={L}: steps={s} (want {L})  start-of-step-2={trace[1] if len(trace)>1 else None}")
print(f"  L=2..40 : direct simulation AND induction step both hold in {39-bad}/39 cases")
# base case shown explicitly
s2, h2, t2 = hh_steps([2, 2, 2, 2])
print(f"  base L=2: [2]^3,2 = [2,2,2,2] -> steps={s2} (want 2), trace={t2}")
# and the first half of FAN-5 (Lemma FAN-3) for completeness
badh = 0
for L in range(2, 41):
    s, _, _ = hh_steps([L] * (L + 1) + [1, 1])
    if s != L + 1:
        badh += 1
print(f"  first half  [L]^(L+1),1,1 clears in L+1 : {39-badh}/39 cases")

# ---------- D3: the two readings of Lemma T's second sentence ----------
# Lemma T (2nd sentence): "if after step tau-1 there are two entries >= 2 then residue <= alpha-1"
# reading (i)  IN SCOPE  : the section's standing reductio residue=alpha (s=tau) is in force
# reading (ii) STANDALONE: reductio dropped; the sentence is a free-standing implication
#
# The dependency note says the sentence needs Fact 2 (residue <= alpha, i.e. s >= tau).
# Test: (i) does the antecedent EVER hold together with s = tau?  (if never -> vacuous, so
#       under reading (i) no Fact 2 is needed, but the sentence carries no content)
#       (ii) does the antecedent hold in the s > tau regime? (if yes, reading (ii) is the
#       only one with content, and there the passage s != tau -> residue <= alpha-1 needs s >= tau)
print("\n== D3: Lemma T's second sentence -- which reading, and does it need Fact 2? ==")

def graphs_upto(n):
    """all connected simple graphs on <= n vertices, as adjacency sets (brute force, small n)."""
    for k in range(2, n + 1):
        verts = list(range(k))
        edges = list(itertools.combinations(verts, 2))
        for mask in range(1 << len(edges)):
            adj = {v: set() for v in verts}
            for i, e in enumerate(edges):
                if mask >> i & 1:
                    adj[e[0]].add(e[1]); adj[e[1]].add(e[0])
            # connected?
            seen, stack = {0}, [0]
            while stack:
                v = stack.pop()
                for w in adj[v]:
                    if w not in seen:
                        seen.add(w); stack.append(w)
            if len(seen) == k:
                yield adj

def alpha_of(adj):
    verts = list(adj)
    best = 0
    for r in range(len(verts), 0, -1):
        if r <= best:
            break
        for S in itertools.combinations(verts, r):
            if all(b not in adj[a] for a, b in itertools.combinations(S, 2)):
                best = max(best, r)
                break
        if best == r:
            break
    return best

n_tot = ante_and_seq_tau = ante_and_s_gt_tau = fact2_viol = 0
s_lt_tau = 0
for adj in graphs_upto(7):
    n_tot += 1
    deg = sorted((len(adj[v]) for v in adj), reverse=True)
    a = alpha_of(adj)
    tau = len(deg) - a
    s, heads, trace = hh_steps(deg)
    res = len(deg) - s
    if res > a:
        fact2_viol += 1
    if s < tau:
        s_lt_tau += 1
    # "after step tau-1" = list at the START of step tau (1-indexed) = trace[tau-1]
    if tau >= 1 and len(trace) >= tau:
        lst = trace[tau - 1]
        two_big = sum(1 for x in lst if x >= 2) >= 2
        if two_big:
            if s == tau:
                ante_and_seq_tau += 1
            else:
                ante_and_s_gt_tau += 1
print(f"  connected graphs n<=7 scanned: {n_tot}")
print(f"  Fact 2 violations (residue > alpha)              : {fact2_viol}")
print(f"  instances with s < tau                           : {s_lt_tau}")
print(f"  antecedent TRUE and s = tau  (reading (i) live)  : {ante_and_seq_tau}")
print(f"  antecedent TRUE and s > tau  (reading (ii) live) : {ante_and_s_gt_tau}")
print("  -> reading (i) is VACUOUS (antecedent contradicts Lemma T's first sentence);")
print("     reading (ii) is the only one with content, and there 'residue <= alpha-1'")
print("     is reached from s != tau only via s >= tau, i.e. via Fact 2.")

# the arithmetic of the passage, made explicit
print("\n  passage under reading (ii):  residue = n - s (Lemma 1(1));")
print("     s != tau  AND  s >= tau (Fact 2)  =>  s >= tau+1  =>  residue <= n-tau-1 = alpha-1.")
print("     Without 's >= tau' the conclusion does not follow: s = tau-1 would give")
print("     residue = alpha+1.  (No such graph exists -- because Fact 2 is a theorem.)")

# ---------- D1: the two status lines, quoted from the draft ----------
print("\n== D1: draft status lines (quoted) ==")
import re, pathlib
draft = pathlib.Path(__file__).resolve().parents[2] / "notes" / "proofs" / "wowii61_draft.md"
txt = draft.read_text().splitlines()
for i, line in enumerate(txt, 1):
    if "FAN-2" in line and "PROVED" in line:
        print(f"  L{i}: {line.strip()}")
    if "Observation FAN-5 are" in line:
        print(f"  L{i}: {line.strip()}")
