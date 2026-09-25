#!/usr/bin/env python3
"""ROUND 6-AT (registry R6.108/R6.110): prime content of the ZLIFT denominators.
Each <terminal>.result line "NAME LIFT D=<integer>" records D_S = product of the coefficient denominators of a
Nullstellensatz certificate sum c_i g_i = 1 over Q, so d_S | D_S where (d_S) = I_S cap Z (contraction lemma).
A prime p that does not divide D_S is certified: I_S reduces to the unit ideal mod p.  The D_S can have
up to ~10^6 decimal digits (products over thousands of coefficients), so we never factor them: we strip every
prime <= BOUND with one big gcd against the primorial-type product and report the residual cofactor size.
Output per terminal: NAME digits=<n> small={p:e,...} cofactor_digits=<m>   (cofactor 1 => fully explained).
Usage: round6_zlift_primes.py <results_dir> [--bound 10000] [--out summary.tsv]"""
import sys, os, re, glob, time, json, math
from functools import reduce
sys.stdout.reconfigure(line_buffering=True)
if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(0)
d = sys.argv[1]; bound = 10000; out = None
if "--bound" in sys.argv: bound = int(sys.argv[sys.argv.index("--bound") + 1])
if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
sieve = bytearray([1]) * (bound + 1); sieve[0] = sieve[1] = 0
for i in range(2, int(bound ** 0.5) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
PR = [i for i in range(bound + 1) if sieve[i]]
PRIMORIAL = reduce(lambda a, b: a * b, PR, 1)
files = sorted(glob.glob(os.path.join(d, "*.result")), key=os.path.getsize)
T0 = time.time(); rows = []; allprimes = {}; unexplained = 0; fails = 0
for f in files:
    line = open(f).read().strip()
    m = re.match(r"(\S+) LIFT D=(\d+)", line)
    if not m:
        m2 = re.match(r"(\S+) ZSTD d=(\d+)", line)
        if m2: m = m2
        else:
            fails += 1; print(os.path.basename(f), "NOLIFT:", line[:80]); continue
    name, ds = m.group(1), m.group(2)
    D = int(ds); digits = len(ds)
    g = math.gcd(D, PRIMORIAL)
    small = {}
    for p in PR:
        if g % p == 0:
            e = 0
            while D % p == 0: D //= p; e += 1
            small[p] = e; allprimes[p] = allprimes.get(p, 0) + 1
    cof_digits = len(str(D)) if D > 1 else 0
    if D > 1: unexplained += 1
    rows.append((name, digits, small, cof_digits))
    print("%s digits=%d small=%s cofactor_digits=%d  [%.0fs]" % (name, digits, json.dumps(small), cof_digits, time.time() - T0))
print("SUMMARY terminals=%d nolift=%d bound=%d primes_seen=%s terminals_with_cofactor>1=%d" % (len(rows), fails, bound, json.dumps(dict(sorted(allprimes.items()))), unexplained))
if out:
    with open(out, "w") as fh:
        for r in rows: fh.write("%s\t%d\t%s\t%d\n" % (r[0], r[1], json.dumps(r[2]), r[3]))
