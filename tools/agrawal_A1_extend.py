#!/usr/bin/env python3
"""
A-1 extension, entirely INSIDE the authorised envelope (nothing above X = 1e8).

(a) Growth curve: one factorisation pass at X = 1e8, then N(B; X) read off for
    X in {1e6, 3e6, 1e7, 3e7, 1e8} by masking p <= X, and B on a denser grid.
    Gives a measured per-decade growth exponent for each B, hence an honest
    extrapolation of the X at which the LP counting inequality would first clear.
(b) SATURATION: for small B the pool is FINITE and independent of X, because
    (p-1)/2 must divide Q_B exactly. Enumerating the squarefree divisors of Q_B
    gives the EXACT pool size over ALL X, i.e. an unconditional result at that B.
"""
import os, sys, json, math, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
sys.path.insert(0, "$HOME/workspace/claudecode/automath/tools")
from agrawal_A1_probe import primes_upto, attribute_pass

T0 = time.time()
HARD = float(os.environ.get("A1X_HARD_LIMIT_S", 900))
OUT = "$HOME/workspace/claudecode/automath/logs/agrawal_A1_extend.json"


def log(*a):
    print("[%6.1fs]" % (time.time() - T0), *a, flush=True)


BGRID = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]
XGRID = [10 ** 6, 3 * 10 ** 6, 10 ** 7, 3 * 10 ** 7, 10 ** 8]
XMAX = 10 ** 8


def theta_odd(primes, B, cls=None):
    s = 0.0
    for q in primes:
        q = int(q)
        if q > B:
            break
        if q == 2:
            continue
        if cls is None or q % 4 == cls:
            s += math.log(q)
    return s


# ---------------- Miller-Rabin (deterministic for n < 3.3e24) ----------------
def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def saturated_pool(B, small):
    """EXACT, X-independent count of the Lenstra pool at smoothness bound B.

    p is admissible  <=>  (p-1)/2 is a squarefree divisor of Q_B (all prime factors
    == 3 mod 4, <= B) and (p+1)/4 is a squarefree divisor of R_B. Since (p-1)/2 | Q_B,
    p <= 2*Q_B+1: the pool is FINITE and enumerating divisors of Q_B settles it for
    every search depth at once.
    """
    q3 = [int(q) for q in small if q <= B and q % 4 == 3 and q != 2]
    r1 = [int(q) for q in small if q <= B and q % 4 == 1]
    R = 1
    for r in r1:
        R *= r
    Q = 1
    for q in q3:
        Q *= q
    divs = [1]
    for q in q3:
        divs += [d * q for d in divs]
    hits80, hitsAny = [], []
    for m in divs:
        if (time.time() - T0) > HARD:
            return {"B": B, "ABORTED": "hard limit"}
        l = (m + 1) // 2                 # = (p+1)/4 with p = 2m+1
        if l == 0 or R % l != 0:
            continue
        p = 2 * m + 1
        if not is_prime(p):
            continue
        hitsAny.append(p)
        if p % 80 == 3:
            hits80.append(p)
    return {"B": B, "n_q3_primes": len(q3), "n_r1_primes": len(r1),
            "n_divisors_enumerated": len(divs),
            "logQ": math.log(Q), "logR": math.log(R),
            "N_saturated_any_p3mod4": len(hitsAny),
            "N_saturated_p3mod80": len(hits80),
            "max_p_any": max(hitsAny) if hitsAny else 0,
            "sample_p3mod80": sorted(hits80)[:40],
            "N_required": math.ceil((math.log(Q) + math.log(R)) / math.log(2))}


def main():
    out = {"started": time.strftime("%Y-%m-%d %H:%M:%S %Z")}
    small = primes_upto(100000)

    log("sieving to 1e8 (single pass, reused for every X in the grid)")
    pr = primes_upto(XMAX)
    m4 = (pr % 4) == 3
    r5 = pr % 5
    baseP = pr[m4 & ((r5 == 2) | (r5 == 3))]
    del pr, m4, r5
    is80 = (baseP % 80) == 3
    A = (baseP - 1) // 2
    Bv = (baseP + 1) // 4
    log("factorising both sides for %d candidates" % len(baseP))
    maxfA, sqfA, clsA = attribute_pass(A, small, 3, "A")
    maxfB, sqfB, clsB = attribute_pass(Bv, small, 1, "B")
    okA = sqfA & clsA
    okB = sqfB & clsB
    log("factorisation done")

    req = {}
    for B in BGRID:
        lq, lr = theta_odd(small, B, 3), theta_odd(small, B, 1)
        req["B=%d" % B] = {"logQ": lq, "logR": lr, "logQR": lq + lr,
                           "N_required_strict": math.ceil((lq + lr) / math.log(2)),
                           "N_required_carmichael_only": math.ceil(lq / math.log(2)),
                           "N_required_lucascarm_only": math.ceil(lr / math.log(2)),
                           "N_required_erdos_noclass": math.ceil(theta_odd(small, B) / math.log(2))}
    out["requirements"] = req

    curve = {}
    for base_name, bm in (("mod80", is80), ("popovych", np.ones(len(baseP), bool))):
        rows = {}
        for B in BGRID:
            smA = maxfA <= B
            smB = maxfB <= B
            strict = bm & smA & okA & smB & okB
            ub = bm & smA & smB
            cC = bm & smA & okA
            cL = bm & smB & okB
            cE = bm & smA
            per_X = {}
            for X in XGRID:
                le = baseP <= X
                per_X["%.0e" % X] = {
                    "N_strict": int((strict & le).sum()),
                    "N_ub": int((ub & le).sum()),
                    "N_ctrl_carm": int((cC & le).sum()),
                    "N_ctrl_lucascarm": int((cL & le).sum()),
                    "N_ctrl_erdos": int((cE & le).sum()),
                }
            rows["B=%d" % B] = per_X
        curve[base_name] = rows
    out["growth_curve"] = curve
    log("growth curve done")

    # decade growth + crossover extrapolation for the strict track
    extrap = {}
    for base_name in ("mod80", "popovych"):
        e = {}
        for B in BGRID:
            n7 = curve[base_name]["B=%d" % B]["1e+07"]["N_strict"]
            n8 = curve[base_name]["B=%d" % B]["1e+08"]["N_strict"]
            need = req["B=%d" % B]["N_required_strict"]
            if n7 > 0 and n8 > 0:
                g = n8 / n7
                dec = (math.log(need / n8) / math.log(g)) if (g > 1 and n8 < need) else 0.0
                e["B=%d" % B] = {"N_1e7": n7, "N_1e8": n8, "N_required": need,
                                 "shortfall_factor": need / n8 if n8 else None,
                                 "growth_per_decade_measured": g,
                                 "decades_needed_naive": dec,
                                 "X_needed_naive": "1e%.1f" % (8 + dec) if dec else None,
                                 "N_at_1e9_naive": n8 * g,
                                 "still_short_at_1e9_by": (need / (n8 * g)) if n8 else None}
            else:
                e["B=%d" % B] = {"N_1e7": n7, "N_1e8": n8, "N_required": need,
                                 "note": "pool empty or too small to fit a rate"}
        extrap[base_name] = e
    out["extrapolation_strict"] = extrap

    log("saturation enumeration (exact, X-independent) for small B")
    out["saturation"] = {}
    for B in (30, 50, 100, 150):
        t = time.time()
        s = saturated_pool(B, small)
        s["t_s"] = round(time.time() - t, 2)
        out["saturation"]["B=%d" % B] = s
        log("  B=%-4d divisors=%-8d N_sat(p=3 mod 4)=%-5d N_sat(p=3 mod 80)=%-5d required=%-5d (%.1fs)"
            % (B, s.get("n_divisors_enumerated", -1), s.get("N_saturated_any_p3mod4", -1),
               s.get("N_saturated_p3mod80", -1), s.get("N_required", -1), s["t_s"]))

    out["finished"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    out["total_wall_s"] = round(time.time() - T0, 2)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1, default=str)
    log("wrote %s (total %.1fs)" % (OUT, time.time() - T0))


if __name__ == "__main__":
    main()
