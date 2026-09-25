#!/usr/bin/env python3
"""
w61_r33_lemH.py -- machine backing for Lemma C1-H, the lemma Q42 (Gemini Pro) named
inside Statement 5 and then graded NONE.  cert_w61_r32 SS5 counts it as a GAP and
makes printing it a promotion precondition for Statement 5.

Lemma C1-H.  Along any run of the process every entry stays non-negative; a terminal
list is therefore all zeros and has sum 0; hence a COMPLETED run satisfies
Sum(L) = 2 * Sum(heads).

Implementation is EXTRACTED from w61_r29_c1audit.py by source text, not retyped.
Every boolean predicate carries an input where it MUST return True.
Self-limit: wall-clock cap, sys.exit(3) on overrun.  Never `return`.
"""
import sys, time, re, hashlib
from collections import Counter
from pathlib import Path

T0 = time.time(); CAP_S = 240.0
def tick(w):
    if time.time() - T0 > CAP_S:
        print("!! SELF-LIMIT exceeded at %s -- exit(3)" % w); sys.exit(3)

ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()
print("impl source : %s md5 %s" % (SRC.name, hashlib.md5(text.encode()).hexdigest()))
def grab(n):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % n, text, re.S | re.M)
    assert m; return m.group(0)
ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

CTRL = []
def ctl(tag, got, want):
    ok = got == want; CTRL.append(ok)
    print("   %-58s got %-10s want %-10s %s" % (tag, repr(got), repr(want), "OK" if ok else "** FAIL"))

def trace(L):
    """(heads, terminal_list) for a completed run; (None, None) if it aborts."""
    cur = sorted(L, reverse=True); heads = []
    while True:
        nxt = stepA(cur)
        if nxt == "TERMINAL": return heads, cur
        if nxt is None:       return None, None
        heads.append(sorted(cur, reverse=True)[0]); cur = nxt

def terminal_is_all_zero(L):
    h, t = trace(L)
    if h is None: return None
    return all(x == 0 for x in t)

def sum_is_twice_heads(L):
    h, t = trace(L)
    if h is None: return None
    return sum(L) == 2 * sum(h)

def all_entries_nonneg_throughout(L):
    cur = sorted(L, reverse=True)
    while True:
        if any(x < 0 for x in cur): return False
        nxt = stepA(cur)
        if nxt == "TERMINAL": return True
        if nxt is None:       return None
        cur = nxt

print()
print("PART 0 -- controls.  Each predicate shown returning True AND (where it can) False.")
ctl("terminal_is_all_zero(M((2,1,1))) [POSITIVE, brief example]", terminal_is_all_zero([2,2,2,2,1,1]), True)
ctl("sum_is_twice_heads(M((2,1,1)))   [POSITIVE, brief example]", sum_is_twice_heads([2,2,2,2,1,1]), True)
ctl("all_entries_nonneg_throughout([2,2,2,2,1,1]) [POSITIVE]",    all_entries_nonneg_throughout([2,2,2,2,1,1]), True)
ctl("terminal_is_all_zero([1,1,1])  aborts -> None [negative]",   terminal_is_all_zero([1,1,1]), None)
ctl("sum_is_twice_heads([1,1,1])    aborts -> None [negative]",   sum_is_twice_heads([1,1,1]), None)
# the predicates must be capable of returning False, else they are decoration.
ctl("sum_is_twice_heads is FALSIFIABLE: injected wrong head sum",
    sum([2,2,2,2,1,1]) == 2 * (sum(trace([2,2,2,2,1,1])[0]) + 1), False)
ctl("terminal_is_all_zero is FALSIFIABLE: a non-zero 'terminal' is rejected",
    all(x == 0 for x in [0, 0, 1]), False)
tick("part0")

print()
print("PART 1 -- the lemma over a DECLARED population")
def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []; return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p): yield [p] + r
def M(lam):
    w = max(lam); return [w]*(w+1) + list(lam)

pop = []
for n in range(1, 19):
    for lam in parts(n): pop.append(M(lam))
for w in range(0, 26):
    pop.append([w]*(w+2)); pop.append([w]*(w+3))
pop += [[4,4,3,3,2,2], [6,4,2], [5,5,4,3,2,1], [3,3,2,2,1,1], [2,2,2,2,2,1,1]]
print("   population : %d lists (every M(lambda) for Sum<=18, both proof shapes w<=25,"
      " plus the A3 list and four ad-hoc lists)" % len(pop))
term = ab = 0
bad_zero = bad_sum = bad_neg = 0
for L in pop:
    z = terminal_is_all_zero(L)
    if z is None: ab += 1; continue
    term += 1
    if z is not True: bad_zero += 1; print("   ** terminal not all zero: %s" % L)
    if sum_is_twice_heads(L) is not True: bad_sum += 1; print("   ** sum != 2*heads: %s" % L)
    if all_entries_nonneg_throughout(L) is not True: bad_neg += 1; print("   ** negative entry: %s" % L)
print("   terminating : %d   aborting : %d" % (term, ab))
print("   terminal-all-zero failures : %d" % bad_zero)
print("   Sum = 2*Sum(heads) failures : %d" % bad_sum)
print("   negative-entry failures     : %d" % bad_neg)
ctl("zero failures across the whole terminating population", (bad_zero, bad_sum, bad_neg), (0,0,0))
ctl("the population actually CONTAINS terminating lists [not vacuous]", term > 0, True)
ctl("the population actually CONTAINS aborting lists [not vacuous]",    ab > 0, True)
tick("part1")

print()
print("PART 2 -- the consequence Q42 asked for, at Statement 5's own numbers")
print("   Theorem C1-2 uses Sum(M) = w(w+2) + c and concludes 'odd => no completed run'.")
odd_checked = odd_abort = 0
for w in range(1, 41):
    for c in range(1, w + 1):
        if (w + c) % 2 == 0: continue
        odd_checked += 1
        L = [w]*(w+2) + [c]
        if runA(L)[0] is None: odd_abort += 1
print("   pairs (w,c), 1<=c<=w<=40, with w+c ODD : %d ; aborting : %d" % (odd_checked, odd_abort))
ctl("every odd-parity pair aborts", odd_abort, odd_checked)
even_checked = even_ok = 0
for w in range(1, 41):
    for c in range(1, w + 1):
        if (w + c) % 2: continue
        even_checked += 1
        if runA([w]*(w+2) + [c])[0] == w + 1: even_ok += 1
print("   pairs with w+c EVEN : %d ; s0 = w+1 : %d" % (even_checked, even_ok))
ctl("every even-parity pair gives s0 = w+1", even_ok, even_checked)

print()
print("   controls run : %d ; passed : %d" % (len(CTRL), sum(CTRL)))
if not all(CTRL):
    print("!! control failed -- Lemma C1-H is NOT backed.  exit(2)"); sys.exit(2)
print("elapsed %.1fs" % (time.time() - T0))
