#!/usr/bin/env python3
"""ROUND 6-AT: direct reduction of a characteristic-zero msolve terminal modulo a prime p.
Given <terminal.ms> (msolve format, line 1 variables, line 2 "0", then comma-separated integer polynomials) and
a prime p, rewrite every integer coefficient modulo p, run msolve over GF(p) and report whether the reduced
ideal is the unit ideal.  Rationale (registry R6.107/R6.108): the contraction generator d_S of the terminal
satisfies d_S | D_S for every lift denominator product D_S; a prime p | D_S is only a CANDIDATE exceptional
prime, and this direct check settles it for that terminal.  Exponents (after '^') and digits inside variable
names are left untouched.  Exit: prints "<name> p=<p> UNIT" / "NOTUNIT" / "NORESULT".
Usage: round6_terminal_modp.py <terminal.ms> <p> [<p> ...]  (outputs next to a scratch dir given by --scratch)"""
import sys, os, re, subprocess
sys.stdout.reconfigure(line_buffering=True)
MS = os.path.expanduser("~/.local/bin/msolve"); ENV = dict(os.environ, DYLD_LIBRARY_PATH=os.path.expanduser("~/.local/lib"))
argv = sys.argv[1:]
scratch = "/tmp"
if "--scratch" in argv:
    k = argv.index("--scratch"); scratch = argv[k + 1]; argv = argv[:k] + argv[k + 2:]
args = [a for a in argv if not a.startswith("--")]
ms = args[0]; primes = [int(a) for a in args[1:]]
name = os.path.basename(ms)[:-3]
lines = open(ms).read().splitlines()
assert lines[1].strip() == "0", "characteristic-zero input expected"
body = "\n".join(lines[2:])
NUM = re.compile(r"(?<![A-Za-z_0-9^])(-?\d+)")
def reduce_body(p):
    def rep(m):
        v = int(m.group(1)) % p
        return str(v)
    return NUM.sub(rep, body)
for p in primes:
    red = reduce_body(p)
    # drop generators that vanished entirely mod p (msolve rejects "0" generators only in some versions; keep it robust)
    gens = [g.strip() for g in red.split(",\n")]
    gens = [g for g in gens if g and re.search(r"[A-Za-z]", g) or (g.strip() not in ("", "0"))]
    gens = [g for g in gens if g.strip() != "0"]
    path = os.path.join(scratch, "%s_mod%d.ms" % (name, p)); out = path + ".gb"
    open(path, "w").write(lines[0].strip() + "\n" + str(p) + "\n" + ",\n".join(gens) + "\n")
    if os.path.exists(out): os.remove(out)
    try:
        r = subprocess.run([MS, "-g", "2", "-t", "1", "-f", path, "-o", out], env=ENV, capture_output=True, text=True, timeout=1800)
    except subprocess.TimeoutExpired:
        print("%s p=%d NORESULT timeout" % (name, p)); continue
    if r.returncode != 0 or not os.path.exists(out):
        print("%s p=%d NORESULT rc=%s %s" % (name, p, r.returncode, r.stderr.strip()[:100])); continue
    basis = "".join(l for l in open(out) if not l.startswith("#")).replace("\n", "").replace(" ", "")
    print("%s p=%d %s" % (name, p, "UNIT" if basis.startswith("[1]") else "NOTUNIT"))
