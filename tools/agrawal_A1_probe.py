#!/usr/bin/env python3
"""
A-1 probe for the Agrawal conjecture falsification route (planner v4 HOLD condition).

Measures the Lenstra-Pomerance (LP) counting inequality on REAL sieved data:

    max_{k odd} log C(N(B), k)   >=   log( Q_B * R_B )

where N(B) counts primes p <= X in the admissible congruence class whose
    (p-1)/2  is squarefree, B-smooth, all prime factors == 3 (mod 4)      [Carmichael side]
    (p+1)/4  is squarefree, B-smooth, all prime factors == 1 (mod 4)      [Lucas-Carmichael side]
and Q_B, R_B are the products of primes <= B in the classes 3 (mod 4), 1 (mod 4).

Rationale for the RHS: for p == 3 (mod 80) and k odd, n = prod p_i has 2||n-1 and 4||n+1,
so Lenstra (iii) (p_i-1)|(n-1) <=> n == 1 mod q for every q | (p_i-1)/2, and
   Lenstra (iv) (p_i+1)|(n+1) <=> n == -1 mod r for every r | (p_i+1)/4.
Requiring n == 1 (mod Q_B) and n == -1 (mod R_B) is sufficient; the heuristic count of
k-subsets landing in that class is C(N,k)/(Q_B R_B).

NEGATIVE CONTROL (V7): the SAME inequality is evaluated on the SAME sieved data for the
two single-sided routes:
  * CTRL-C  (Carmichael only, drop condition (iv))       -> RHS = log Q_B
  * CTRL-LC (Lucas-Carmichael only, drop condition (iii))-> RHS = log R_B
  * CTRL-E  (Erdos/AGP Carmichael construction, no class condition on the factors)
These correspond to constructions that demonstrably DO produce objects (Carmichael numbers
are known in abundance; Lucas-Carmichael numbers likewise). If the inequality cannot come
out PASS on any of them, the test is rigged and its FAIL is not evidence.

Staged: X = 1e7 then 1e8. Stage 3 (1e9) NOT authorised in this slice.
Hard wall-clock limit enforced inside the loop; JSON checkpoint written after each stage.
"""
import os, sys, json, time, math

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

T0 = time.time()
HARD_LIMIT_S = float(os.environ.get("A1_HARD_LIMIT_S", 2100))   # 35 minutes, hard
OUT = os.environ.get("A1_OUT", "$HOME/workspace/claudecode/automath/logs/agrawal_A1_state.json")
BLIST = [100, 1000, 10000, 100000]
BMAX = max(BLIST)


def elapsed():
    return time.time() - T0


def budget_left():
    return HARD_LIMIT_S - elapsed()


def log(*a):
    print("[%7.1fs]" % elapsed(), *a, flush=True)


# ---------------------------------------------------------------- sieve
def primes_upto(n):
    """Odd-only sieve of Eratosthenes -> np.int64 array of primes <= n."""
    if n < 2:
        return np.array([], dtype=np.int64)
    half = (n + 1) // 2                       # index i <-> 2i+1
    s = np.ones(half, dtype=bool)
    s[0] = False                              # 1 is not prime
    for i in range(1, int(n ** 0.5) // 2 + 1):
        if s[i]:
            p = 2 * i + 1
            s[(p * p) // 2:: p] = False
    out = np.empty(int(s.sum()) + 1, dtype=np.int64)
    out[0] = 2
    out[1:] = 2 * np.nonzero(s)[0] + 1
    return out


# ---------------------------------------------------------------- attribute pass
def attribute_pass(vals, small_primes, want_class, label):
    """
    Fully factor each entry of `vals` (all <= small_primes[-1]**2) by trial division over
    small_primes, recording per-entry:
        maxf  : largest prime factor
        sqf   : squarefree?
        cls   : all prime factors == want_class (mod 4)?
    Returns (maxf, sqf, cls) as arrays aligned with `vals`.
    Compaction: an entry is finalised as soon as its residual < q_next**2 (then the residual
    is 1 or a single prime), which is exact, not heuristic.
    """
    n = len(vals)
    maxf = np.zeros(n, dtype=np.int64)
    sqf = np.ones(n, dtype=bool)
    cls = np.ones(n, dtype=bool)

    ids = np.arange(n, dtype=np.int64)
    res = vals.astype(np.int64).copy()

    # entries equal to 1 are already finished
    keep = res > 1
    ids, res = ids[keep], res[keep]
    w_maxf = np.zeros(len(ids), dtype=np.int64)
    w_sqf = np.ones(len(ids), dtype=bool)
    w_cls = np.ones(len(ids), dtype=bool)

    np_ = len(small_primes)
    for pi in range(np_):
        if len(ids) == 0:
            break
        q = int(small_primes[pi])
        r = res % q
        m = (r == 0)
        if m.any():
            w_maxf[m] = q
            res = np.where(m, res // q, res)
            if (q % 4) != want_class:
                w_cls[m] = False
            # higher powers -> not squarefree
            m2 = m & (res % q == 0)
            while m2.any():
                w_sqf[m2] = False
                res = np.where(m2, res // q, res)
                m2 = m2 & (res % q == 0)
        qn = int(small_primes[pi + 1]) if pi + 1 < np_ else (int(q) + 1)
        # finalise everything whose residual is provably 1 or prime
        done = res < qn * qn
        if done.any() and (done.mean() > 0.02 or pi + 1 == np_):
            d_ids, d_res = ids[done], res[done]
            d_maxf, d_sqf, d_cls = w_maxf[done], w_sqf[done], w_cls[done]
            big = d_res > 1                       # residual is a prime > q
            d_maxf = np.where(big, np.maximum(d_maxf, d_res), d_maxf)
            d_cls = np.where(big & ((d_res % 4) != want_class), False, d_cls)
            maxf[d_ids] = d_maxf
            sqf[d_ids] = d_sqf
            cls[d_ids] = d_cls
            k = ~done
            ids, res = ids[k], res[k]
            w_maxf, w_sqf, w_cls = w_maxf[k], w_sqf[k], w_cls[k]
        if elapsed() > HARD_LIMIT_S:
            raise TimeoutError("hard limit hit inside attribute_pass(%s) at q=%d" % (label, q))
    if len(ids):
        raise RuntimeError("attribute_pass(%s): %d entries unresolved" % (label, len(ids)))
    return maxf, sqf, cls


# ---------------------------------------------------------------- inequality
def log_binom(n, k):
    if k < 0 or k > n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def best_odd_k(N):
    """max over ODD k of log C(N,k), returned as (k, value)."""
    if N < 1:
        return (0, float("-inf"))
    k0 = N // 2
    best = (None, float("-inf"))
    for k in (k0 - 1, k0, k0 + 1, 1, 3, N if N % 2 else N - 1):
        if k is None or k < 1 or k > N or k % 2 == 0:
            continue
        v = log_binom(N, k)
        if v > best[1]:
            best = (k, v)
    return best


def theta_class(primes, B, cls):
    """sum of log q over primes q <= B with q % 4 == cls  (cls=None -> all odd primes)."""
    s = 0.0
    for q in primes:
        q = int(q)
        if q > B:
            break
        if q == 2:
            continue
        if cls is None or (q % 4) == cls:
            s += math.log(q)
    return s


def evaluate(track, N, rhs_nats, rhs_label):
    k, lhs = best_odd_k(N)
    margin = lhs - rhs_nats
    return {
        "track": track, "N": int(N), "k_star": int(k or 0),
        "lhs_log_binom_nats": lhs if lhs != float("-inf") else None,
        "rhs_nats": rhs_nats, "rhs_label": rhs_label,
        "margin_nats": margin if lhs != float("-inf") else None,
        "margin_orders_of_magnitude": (margin / math.log(10)) if lhs != float("-inf") else None,
        "verdict": "PASS" if (lhs != float("-inf") and margin >= 0) else "FAIL",
        "N_required_approx": math.ceil(rhs_nats / math.log(2)),
    }


# ---------------------------------------------------------------- one stage
def run_stage(X, small_primes, all_primes_upto_BMAX):
    st = {"X": X}
    t = time.time()
    pr = primes_upto(X)
    st["t_sieve_s"] = round(time.time() - t, 2)
    st["pi_X"] = int(len(pr))
    log("stage X=%.0e: sieve done, pi(X)=%d, %.1fs" % (X, len(pr), st["t_sieve_s"]))

    # base pool: p == 3 (mod 4)  and  p mod 5 in {2,3}   (Popovych's mod-5 condition;
    # p == 3 mod 80 is a subset, so both tracks come out of one factorisation pass)
    t = time.time()
    m4 = (pr % 4) == 3
    r5 = pr % 5
    baseP = pr[m4 & ((r5 == 2) | (r5 == 3))]
    is80 = (baseP % 80) == 3
    st["n_baseP"] = int(len(baseP))
    st["n_base80"] = int(is80.sum())
    del pr, m4, r5
    log("  base pools: |p=3 mod 4 & p mod 5 in {2,3}| = %d ; |p = 3 mod 80| = %d (%.1fs)"
        % (st["n_baseP"], st["n_base80"], time.time() - t))

    A = (baseP - 1) // 2      # Carmichael side
    Bv = (baseP + 1) // 4     # Lucas-Carmichael side

    t = time.time()
    maxfA, sqfA, clsA = attribute_pass(A, small_primes, 3, "A")
    st["t_factor_A_s"] = round(time.time() - t, 2)
    log("  side A factored (%.1fs)" % st["t_factor_A_s"])
    t = time.time()
    maxfB, sqfB, clsB = attribute_pass(Bv, small_primes, 1, "B")
    st["t_factor_B_s"] = round(time.time() - t, 2)
    log("  side B factored (%.1fs)" % st["t_factor_B_s"])

    okA = sqfA & clsA          # squarefree + all factors == 3 (4)
    okB = sqfB & clsB          # squarefree + all factors == 1 (4)

    st["stages"] = {}
    for basename, basemask in (("mod80", is80), ("popovych_mod4_mod5", np.ones(len(baseP), bool))):
        res = {}
        for B in BLIST:
            smA = basemask & (maxfA <= B)
            smB = basemask & (maxfB <= B)
            logQ = theta_class(all_primes_upto_BMAX, B, 3)
            logR = theta_class(all_primes_upto_BMAX, B, 1)
            logAll = theta_class(all_primes_upto_BMAX, B, None)

            strict_both = smA & okA & smB & okB
            ub_both = smA & smB                       # upper bound: smoothness only
            ctrl_C = smA & okA                        # Carmichael side only  (drop (iv))
            ctrl_LC = smB & okB                       # Lucas-Carmichael side only (drop (iii))
            ctrl_E = smA                              # Erdos/AGP style: (p-1)/2 B-smooth, no class

            # "effective" moduli: only primes that actually occur in the qualifying pool
            def eff(mask, side_maxf, cls):
                idx = np.nonzero(mask)[0]
                if len(idx) == 0:
                    return 0.0, 0
                vals = (A if side_maxf is maxfA else Bv)[idx]
                occ = set()
                for q in all_primes_upto_BMAX:
                    q = int(q)
                    if q > B:
                        break
                    if q == 2:
                        continue
                    if cls is not None and (q % 4) != cls:
                        continue
                    if np.any(vals % q == 0):
                        occ.add(q)
                return sum(math.log(q) for q in occ), len(occ)

            row = {
                "B": B,
                "logQ_B": logQ, "logR_B": logR, "logAllOdd_B": logAll,
                "N_strict_both": int(strict_both.sum()),
                "N_ub_both_smoothonly": int(ub_both.sum()),
                "N_ctrl_carmichael_only": int(ctrl_C.sum()),
                "N_ctrl_lucascarm_only": int(ctrl_LC.sum()),
                "N_ctrl_erdos_noclass": int(ctrl_E.sum()),
            }
            row["MAIN_strict"] = evaluate("LENSTRA strict both sides", row["N_strict_both"],
                                          logQ + logR, "log(Q_B*R_B)")
            row["MAIN_upper_bound"] = evaluate("upper bound: B-smooth both sides, no sqfree/class",
                                               row["N_ub_both_smoothonly"], logQ + logR, "log(Q_B*R_B)")
            row["CTRL_carmichael_only"] = evaluate("CONTROL Carmichael side only",
                                                   row["N_ctrl_carmichael_only"], logQ, "log(Q_B)")
            row["CTRL_lucascarm_only"] = evaluate("CONTROL Lucas-Carmichael side only",
                                                  row["N_ctrl_lucascarm_only"], logR, "log(R_B)")
            row["CTRL_erdos_noclass"] = evaluate("CONTROL Erdos/AGP (p-1)/2 B-smooth, no class",
                                                 row["N_ctrl_erdos_noclass"], logAll, "log(prod odd p<=B)")
            # effective moduli only where it can matter (strict track)
            le_q, nq = eff(strict_both, maxfA, 3)
            le_r, nr = eff(strict_both, maxfB, 1)
            row["effective_logQ"] = le_q
            row["effective_logR"] = le_r
            row["effective_nprimes"] = [nq, nr]
            row["MAIN_strict_effective_modulus"] = evaluate(
                "LENSTRA strict, EFFECTIVE modulus (most generous)",
                row["N_strict_both"], le_q + le_r, "log(Q_eff*R_eff)")
            res["B=%d" % B] = row
            log("   [%s] B=%-6d  N_strict=%-6d N_ub=%-7d N_ctrlC=%-7d N_ctrlLC=%-7d N_ctrlE=%-7d"
                % (basename, B, row["N_strict_both"], row["N_ub_both_smoothonly"],
                   row["N_ctrl_carmichael_only"], row["N_ctrl_lucascarm_only"],
                   row["N_ctrl_erdos_noclass"]))
        st["stages"][basename] = res
    return st


def main():
    state = {"started": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "hard_limit_s": HARD_LIMIT_S,
             "stages": {}}
    log("sieving small primes to %d" % BMAX)
    small = primes_upto(BMAX)          # trial-division primes (>= sqrt of any value seen)
    log("  %d small primes" % len(small))

    for X in (10 ** 7, 10 ** 8):
        if budget_left() < 60:
            state["stages"]["X=%d" % X] = {"SKIPPED": "insufficient wall-clock budget"}
            break
        log("=== STAGE X=%.0e ===" % X)
        t = time.time()
        try:
            st = run_stage(X, small, small)
        except TimeoutError as e:
            state["stages"]["X=%d" % X] = {"ABORTED": str(e)}
            log("ABORT:", e)
            break
        st["t_stage_total_s"] = round(time.time() - t, 2)
        state["stages"]["X=%d" % X] = st
        with open(OUT, "w") as f:
            json.dump(state, f, indent=1, default=str)
        log("=== STAGE X=%.0e done in %.1fs; checkpoint written ===" % (X, st["t_stage_total_s"]))

    state["finished"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    state["total_wall_s"] = round(elapsed(), 2)
    with open(OUT, "w") as f:
        json.dump(state, f, indent=1, default=str)
    log("ALL DONE, total %.1fs" % elapsed())


if __name__ == "__main__":
    main()
