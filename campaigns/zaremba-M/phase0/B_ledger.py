#!/usr/bin/env python3
"""
Zaremba campaign, Phase 0, Agent B: exact constant ledger for Shkredov arXiv:2603.14116v2
(Theorem 8 / Corollary 1 for large primes q = p; Appendix eq. (158) claims M = 2^2000).

Every step below cites the equation / statement it comes from.  Exact rationals (fractions.Fraction)
are carried until the very last log2, which is evaluated with mpmath at 50 digits.

Chain (Appendix, pp. 38-39, + Sec. 5.4, p. 37):
  c      >= min{1/3, (8 C2)^-1, tau (4 C2)^-1, 0.5 c_H (C1+C2)^-1}          [App., line after Lemma 40]
  k      = ceil(1/c) + 1                                                    [App.]
  delta  = c / 2^(k+4)                                                      [App.]
  kappa  = delta / 6   (from  log N * kappa = (6m)^-1 tau delta log p,  m = tau log_N p)   [App.]
           -- this is the kappa of Lemma 14/15 ("compute the constant kappa from Lemmas 14, 15")
  kappa_C = kappa / 2                                                       [Cor. 16 proof, p.10: error sqrt(|A||B|) N^(-kappa/2)]
  Sec 5.4 condition  M^-1 q^{w_M} N_*^{kappa_C} >> q^{1+o(1)},  N_* = N^{1/10}, N = q^{2 eps}
           <=>  1 - w_M < 2 eps kappa_C / 10                                 [p.37, display before (156)]
           (Shkredov drops the factor N^{w_{M*}-w_M+(1-w_{M*})/10} >= 1; option exact_exponent keeps it)
  Thm 38 (Kurzweil): for M >= 1000,  1 - 0.99/M <= w_M <= 1 - 1/(4M)
           => sufficient: 0.99/M <= eps kappa_C / 5,  i.e.  M_thr = 0.99 * 5 / (eps kappa_C)
  eps < 1/18 - o(1)                                                         [(119)->(151)->(156): N <= q^{1/9}/(2^30 M M* M~)]
  M* >= 40 M  (needs 1-w_M >= 10(1-w_M*); with Thm 38: M* >= 10*4*0.99 M = 39.6 M)      [App. after Thm 38]
  final partial-quotient bound: Lemma 10 turns x|y| >= q/(4 M*) into c_j <= 4 M*;  (157) writes O(M*)
  M~ = 200 in the appendix (second term of (157) negligible).
Readings of "the M of Corollary 1":
  A  = (157) literal:            10 / (kappa eps)           [kappa as in appendix, no Cor-16 halving, no 0.99*5, no 4]
  B  = visible rigorous chain:   4 * 39.6 * M_thr,  M_thr = 0.99*5/(eps kappa_C)
  C  = Theorem 8 wording (22):   100 * M_thr  (c_j <= 100 M for M >= M_thr)
"""
from fractions import Fraction as Fr
import math, mpmath
mpmath.mp.dps = 50

def log2(x):
    x = Fr(x)
    return float(mpmath.log(mpmath.mpf(x.numerator), 2) - mpmath.log(mpmath.mpf(x.denominator), 2))

def ceil_fr(x):
    x = Fr(x); return -((-x.numerator) // x.denominator)

BASE = dict(
    c_H=Fr(1, 20), C1=Fr(9), C2=Fr(32), tau=Fr(1, 4),
    terms=("third", "8C2", "tau4C2", "cH"),      # which terms of the min{...} are present
    k_offset=1,            # k = ceil(k_mult/c) + k_offset
    k_mult=Fr(1),          # appendix: k = ceil(1/c)+1 ; see structural question at the end
    bsg=True,              # False: replace 0.5 c_H/(C1+C2) by 0.5 c_H (other C2-terms kept)
    delta_shift=4,         # delta = c / 2^(k + delta_shift)
    delta_has_c=True,      # the factor c in delta = c/2^(k+4)
    kappa_div=Fr(6),       # kappa = delta / 6
    cor16_div=Fr(2),       # kappa_C = kappa / 2 (Cor 16)
    nstar_div=Fr(10),      # N_* = N^(1/10)  (H = N^(9/20))
    eps=Fr(1, 18),         # eps -> 1/18 from (156)
    w_up=Fr(99, 100),      # 1 - w_M <= w_up / M   (Thm 38, upper side of 1-w_M)
    w_lo=Fr(1, 4),         # 1 - w_M >= w_lo / M   (Thm 38, lower side)
    ratio10=Fr(10),        # need 1 - w_M >= 10 (1 - w_M*)   (Sec 5.4 / (155))
    lemma10=Fr(4),         # Lemma 10: 4M  (Remark 11: M+2 -> ~1)
    exact_exponent=False,  # keep (1-2eps) gain and the 9/5 eps (1-w_M*) cost instead of Shkredov's drop
    Mtilde=Fr(200),
)

def chain(**over):
    P = dict(BASE); P.update(over)
    cH, C1, C2, tau = P["c_H"], P["C1"], P["C2"], P["tau"]
    T = {"third": Fr(1, 3), "8C2": 1 / (8 * C2), "tau4C2": tau / (4 * C2), "cH": Fr(1, 2) * cH / ((C1 + C2) if P["bsg"] else 1)}
    T = {k: v for k, v in T.items() if k in P["terms"]}
    c = min(T.values()); binding = [k for k, v in T.items() if v == c]
    k = ceil_fr(P["k_mult"] / c) + P["k_offset"]
    delta = (c if P["delta_has_c"] else 1) / Fr(2) ** (k + P["delta_shift"])
    kappa = delta / P["kappa_div"]
    kappaC = kappa / P["cor16_div"]
    eps, nd = P["eps"], P["nstar_div"]
    Mstar_ratio = P["ratio10"] * P["w_up"] / P["w_lo"]          # 10*0.99/(1/4) = 39.6
    if not P["exact_exponent"]:
        # w_up/M <= 2 eps kappaC / nd
        Mthr = P["w_up"] * nd / (2 * eps * kappaC)
    else:
        # (1-w_M)(1-2eps) + 2eps*(9/10)(1-w_M*) < 2 eps kappaC / nd, with 1-w_M* <= w_up/(Mstar_ratio M)
        g = Fr(9, 10) if nd == 10 else (1 - 1 / nd)
        Mthr = P["w_up"] * ((1 - 2 * eps) + 2 * eps * g / Mstar_ratio) * nd / (2 * eps * kappaC)
    Mthr = max(Mthr, Fr(1000))                                     # Thm 38 needs M >= 1000
    MA = Fr(10) / (kappa * eps)                                    # (157) literal
    MB = P["lemma10"] * max(Mstar_ratio * Mthr, P["Mtilde"])       # rigorous visible chain
    MC = 100 * Mthr                                                # Theorem 8 wording
    return dict(c=c, binding=binding, k=k, delta=delta, kappa=kappa, kappaC=kappaC, Mthr=Mthr,
                Mstar_ratio=Mstar_ratio, A=log2(MA), B=log2(MB), C=log2(MC),
                l2c=log2(1 / c), l2delta=log2(delta), l2kappa=log2(kappa), l2kappaC=log2(kappaC),
                l2Mthr=log2(Mthr), C0=log2(MB * kappa))

def row(label, r):
    return (f"| {label} | 1/{float(1/r['c']):.1f} | {','.join(r['binding'])} | {r['k']} | {r['l2kappa']:.2f} | "
            f"{r['A']:.1f} | {r['B']:.1f} | {r['C']:.1f} |")

HDR = "| scenario | c | binding term | k | log2 kappa(L14) | log2 M [A: (157) literal] | log2 M [B: full visible chain] | log2 M [C: 100*M_thr] |\n|---|---|---|---|---|---|---|---|"

if __name__ == "__main__":
    b = chain()
    print("== Baseline (Shkredov's inputs) ==")
    print(f"c = {b['c']}  (binding: {b['binding']})")
    print(f"k = ceil(1/c)+1 = {b['k']}")
    print(f"delta = c/2^(k+4) = 1/({1/b['c']} * 2^{b['k']+4});  log2 delta = {b['l2delta']:.4f}")
    print(f"kappa = delta/6;  log2 kappa = {b['l2kappa']:.4f}   (appendix states kappa >= 2^-1656)")
    print(f"kappa/2^-1656 = 2^{b['l2kappa']+1656:.4f} = {2**(b['l2kappa']+1656):.4f}")
    print(f"kappa_C = kappa/2;  log2 kappa_C = {b['l2kappaC']:.4f}")
    print(f"M* ratio = {b['Mstar_ratio']} ; log2 M_thr = {b['l2Mthr']:.4f}")
    print(f"log2 M: A (157 literal, true kappa) = {b['A']:.4f};  B (full chain) = {b['B']:.4f};  C (100 M_thr) = {b['C']:.4f}")
    print(f"A with Shkredov's stated kappa=2^-1656: {1656 + log2(Fr(10)/Fr(1,18)):.4f}")
    print(f"kappa-independent overhead C0 = M_B * kappa(L14): log2 C0 = {b['C0']:.4f}; with kappa=1/2 -> log2 M_B = {b['C0']+1:.2f}")
    print(f"exact-exponent variant: B = {chain(exact_exponent=True)['B']:.4f}")
    print()
    print("== Sensitivity table ==")
    print(HDR)
    print(row("baseline (c_H=1/20, C1=9, C2=32, tau=1/4)", b))
    for d in [20, 15, 12, 10, 8, 6, 5, 4, 3, 2]:
        print(row(f"c_H = 1/{d}", chain(c_H=Fr(1, d))))
    print(row("C1 halved (4.5)", chain(C1=Fr(9, 2))))
    print(row("C2 halved (16)", chain(C2=Fr(16))))
    print(row("C1, C2 both halved", chain(C1=Fr(9, 2), C2=Fr(16))))
    print(row("tau = 1/5 (MMS 2212.14646 girth)", chain(tau=Fr(1, 5))))
    print(row("tau = 1/8 (MMS 1808.05845: m <= d/2)", chain(tau=Fr(1, 8))))
    print(row("tau = 1/20 (MMS22 m-coefficient tau/4)", chain(tau=Fr(1, 20))))
    for d in [2, 4, 8]:
        print(row(f"c_H=1/{d}, tau=1/5", chain(c_H=Fr(1, d), tau=Fr(1, 5))))
    print(row("c_H=1/2, C2 halved", chain(c_H=Fr(1, 2), C2=Fr(16))))
    print(row("BSG loss removed in c_H term only: min{1/3,1/(8C2),tau/(4C2),c_H/2}", chain(bsg=False)))
    print(row("R2 claim: all C2-terms gone, min{1/3, c_H/2}", chain(bsg=False, terms=("third", "cH"))))
    print()
    print("== Overhead factors removed one at a time (baseline inputs) ==")
    print("| factor removed | source | log2 M [B] | saving (bits) |\n|---|---|---|---|")
    OV = [("Lemma 10: 4 -> 1 (Remark 11, M+2)", "Lemma 10 / Rem. 11", dict(lemma10=Fr(1))),
          ("Thm 38 slack: M* ratio 39.6 -> 10 (needs 1-w_M ~ 6/(pi^2 M) both sides)", "Thm 38 / Hensley Thm 12", dict(w_up=Fr(1), w_lo=Fr(1))),
          ("M* ratio 39.6 -> 1 (no second Cantor level)", "Sec 5.4 (155)", dict(ratio10=Fr(1), w_up=Fr(1), w_lo=Fr(1))),
          ("Cor 16 halving kappa/2 -> kappa", "Cor 16 proof", dict(cor16_div=Fr(1))),
          ("N_* = N^(1/10) -> N (H=1)", "Sec 5.4, H=N^(9/20)", dict(nstar_div=Fr(1))),
          ("eps 1/18 -> 1/4 (interval length q^(1/2))", "(119),(151),(156)", dict(eps=Fr(1, 4))),
          ("0.99 -> 6/pi^2 ~ 0.6079 (Hensley asymptotic)", "Thm 38 vs Thm 12", dict(w_up=Fr(6079, 10000))),
          ("kappa = delta/6 -> delta", "App. [43,p.9]", dict(kappa_div=Fr(1))),
          ("delta = c/2^(k+4) -> c/2^k", "App.", dict(delta_shift=0)),
          ("factor c in delta -> 1", "App.", dict(delta_has_c=False)),
          ("k = ceil(1/c)+1 -> ceil(1/c)", "App.", dict(k_offset=0)),
          ]
    for lab, src, o in OV:
        r = chain(**o); print(f"| {lab} | {src} | {r['B']:.2f} | {b['B']-r['B']:.2f} |")
    comb = dict(lemma10=Fr(1), w_up=Fr(6079, 10000), w_lo=Fr(6079, 10000), cor16_div=Fr(1), kappa_div=Fr(1),
                delta_shift=0, k_offset=0)
    r = chain(**comb)
    print(f"| all pure bookkeeping at once (Lemma10->1, M* ratio->10 with 6/pi^2, Cor16 halving, /6, 2^4, +1) | | {r['B']:.2f} | {b['B']-r['B']:.2f} |")
    r = chain(**comb, nstar_div=Fr(1), eps=Fr(1, 4), delta_has_c=False)
    print(f"| ... plus N_*->N, eps->1/4, c-prefactor in delta | | {r['B']:.2f} | {b['B']-r['B']:.2f} |")
    print()
    print("== c needed for targets (reading B, all other inputs Shkredov's) ==")
    for target in [500, 150]:
        best = None
        for inv in range(2, 5000):
            r = chain(terms=("cH",), c_H=Fr(2 * 41, inv))   # forces c = 1/inv
            if r['B'] <= target: best = (inv, r['B'])
        print(f"log2 M <= {target}: need 1/c <= {best[0]} (log2 M = {best[1]:.2f} at c = 1/{best[0]})")
    print()
    print("== Structural question for RB1 (not a sensitivity input): doubling count k = ceil(k_mult/c)+1 ==")
    print("| reading of k | tau | c | k | log2 M [B] |\n|---|---|---|---|---|")
    for tau in [Fr(1, 4), Fr(1, 5)]:
        for mult, lab in [(Fr(1), "appendix: k = ceil(1/c)+1"),
                          (12 / tau, "k = ceil((log(|G|/d)/log K)/c)+1, K=p^(tau/6): 12/tau"),
                          (18 / tau, "k = ceil((log|G|/log K)/c)+1 (survey Thm 49 error<main): 18/tau")]:
            r = chain(tau=tau, k_mult=mult)
            print(f"| {lab} | {tau} | 1/{float(1/r['c']):.0f} | {r['k']} | {r['B']:.1f} |")
