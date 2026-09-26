# Phase 0 / Agent B: exact constant ledger for Shkredov's M = 2^2000

Written 2026-09-26T04:32Z. Script: `phase0/B_ledger.py` (exact `Fraction` arithmetic; log2 via mpmath at 50 digits). Full output: `phase0/B_ledger.out`. To reproduce: `python3 B_ledger.py`.

## 0. Bottom line

* Using Shkredov's own formulas and inputs, the chain gives **log2 M = 1665.8 / 1673.0 / 1672.4** under three readings of "the M of Corollary 1" (§3). So 2^2000 is a round-up with about 327 bits of slack. The DESIGN figure "≈1680" is 3–7 bits high: reading B is 1/c + log2(1/c) + 22.4, not + 25. This is bookkeeping only. It is not announce-worthy.
* **N2(κ):** "κ ≥ 2^-1656" is **false** under the appendix's own definitions. κ = δ/6 = 1/(9840·2^1645) = **2^-1658.264**, which is 0.208 × 2^-1656. The value 2^-1656 is δ rounded: δ = 2^-1655.68 ≥ 2^-1656. Correct statement: δ ≥ 2^-1656 and κ ≥ 2^-1659. The number that enters Sec. 5.4 is the Corollary-16 exponent κ/2 = 2^-1659.26. Neither error moves the result anywhere near 2000.
* **N2(τ):** the numerical result is **independent of τ ∈ {1/4, 1/5, 1/8}**. In the appendix κ = δ/6 the τ cancels. τ enters only through the min-term τ/(4C2), which does not bind whenever τ ≥ 128/1640 ≈ 0.078. τ = 1/4 is the sourced value in Shkredov's convention (m = τ log_N p, K = p^{τ/6}). It comes from MMS 1808.05845 Thm 25: d(Cay(PSL2(F_p),T)) ≥ (1/4) log_N p. The τ = 1/5 of MMS 2212.14646 is a different, weaker normalisation: girth ≥ (1/5) log_N p with m = (τ/4) log_N p. Details and one open caveat are in §5.
* **New structural finding for R1/R2 (sensitivity):** improving c_H alone **saturates at c = τ/(4C2) = 1/512**, which gives log2 M ≈ 543 (reading B) for every c_H ≥ 0.16. **The 500 target cannot be reached by c_H alone** while C2 = 32 and τ = 1/4. The target needs 1/c ≤ 468, which also requires τ/(4C2) ≥ 1/468, i.e. C2 ≤ 29.25 at τ = 1/4. The 150 target needs 1/c ≤ 120, i.e. C2 ≤ 7.5 (τ = 1/4) and c_H/(2(C1+C2)) ≥ 1/120.
* **Open structural question, flagged for RB1 / Agent A (unverified, potentially large):** the appendix takes the doubling count as k = ⌈1/c⌉+1. In the sourced statements the count scales with log|G| / log K: MMS18 Thm 9 has k = 3 log p/(c* log K), MMS22 eq. (19) has k ≪ log p / log K(f), and the error term in survey Thm 49 is |A|^{2k}/K_*^{ck}. With K = p^{τ/6} that is 18/τ = 72 times larger at τ = 1/4 and would give log2 M ≈ 1.2×10^5. I could not locate where the appendix's c absorbs this factor. The appendix cites "[43, Page 9]" for the κ formula, and that is the IMRN version, which I could not obtain (arXiv v1 of 2212.14646 differs). I am **not** claiming the appendix is wrong. The point is that the ledger's 1673 is conditional on the appendix's k-formula being correct as written.

## 1. Sources read (by me, full text extracted with pymupdf)

| source | what I used |
|---|---|
| Shkredov arXiv:2603.14116v2 (41 pp.) | Cor 1; Thm 8 (21)–(22); Lemma 10, Rem 11; Lemma 13; Lemma 14 (32); Lemma 15 (33); Cor 16 (34) and proof (35)–(36); Prop 35 (119)–(120); Sec 5.1 (130)–(136); 5.2 (140)–(152); 5.4 (155)–(157); Appendix (158), Thm 38, eq (159), Thm 39, Lemma 40, min{…} |
| MMS arXiv:2212.14646v1 | Lemma 4 sketch, eqs (15)–(19): girth τ = 1/5, m = (τ/4) log_N p, K(G) = p^{τ/6}, δ = 1/2^{k+2} with k ≪ log p / log K(f); (20)–(24) |
| MMS arXiv:1808.05845v2 | Thm 9 (δ = 2^-(k+2), k = 3 log p/(c* log K)); Thm 15 (flattening, K^{-c* k}); Thm 24 (m ≤ γ/2, τ ≤ τ0/2); Thm 25 (d ≥ (1/4) log_N p for T = {(1,−2j;2j,1−4j²)}); Thm 29 (Margulis girth) |
| Rudnev–Shkredov arXiv:1812.01671v3 | Thm 2: **symmetric** generating set, \|A\| > abs. const., A³ = SL2 or K ≫ \|A\|^{1/20}; footnote: 1/15 under an SL2 Szőnyi analogue, "as if 1/12" only for the diameter |
| Murphy arXiv:1907.13569 | Lemma 12 (BSG, "C an absolute constant"; **no 9/32 in this text**) |
| Shkredov, Russian Math. Surveys 76:6 (2021) 1065–1122 (mathnet, English and Russian PDFs) | Thm 10 (Murphy BSG, constant C unspecified); Thm 49 (error O(\|A\|^{2k}/K_*^{ck}), 0 < c < 1/4 in (60)), proof sketch (60)–(64); Cor 50 (ε(δ) ≪ exp(−O(1/δ))) |
| Zhang arXiv:2605.02518 | Remark 1.3: M "effectively computable"; no number |

**Unread:** the IMRN version of MMS [43] (the appendix's "[43, Page 7]" and "[43, Page 9]"); Tao–Vu Thm 2.29 / Lemma 2.13 and Tao 2008 Prop 4.5, which are the claimed source of C1 = 9, C2 = 32; Kurzweil 1951 Thm VIII (= Thm 38); Hensley 1989/1992; Helfgott 2008; Bourgain–Gamburd 2008. C1 = 9 and C2 = 32 are taken on Shkredov's word. Neither Murphy's arXiv text nor the survey states them.

## 2. The chain, step by step (exact statements, every constant)

1. **c** (App. p.39, "following the argument of the proof of [53, Theorem 49] in the case of SL2(F_p)"):
   c ≥ min{1/3, (8C2)^-1, τ(4C2)^-1, 0.5 c_H (C1+C2)^-1} = min{1/3, 1/256, 1/512, 1/1640} = **1/1640**. Here C1 = 9, C2 = 32 (Thm 39), c_H = 1/20 (Lemma 40), τ = 1/4 (App. after (159)). Binding term: 0.5 c_H/(C1+C2). The survey's Thm 49 gives no explicit c. The min{…} is Shkredov's own unpublished derivation (N1 is Agent A's task).
2. **k = ⌈1/c⌉ + 1 = 1641** (App.).
3. **δ = c/2^{k+4} = 1/(1640·2^1645)**, log2 δ = −1655.6795 (App.).
4. **κ (Lemmas 14/15) = δ/6.** Source: App. "log N·κ = (6m)^-1 τ δ log p = 6^-1 δ log N" with m = τ log_N p. So κ = 1/(9840·2^1645), **log2 κ = −1658.2644**.
5. **Cor 16 halves it:** the proof of Cor 16 ends with "≪ √(|A||B|) N^{-κ/2}", so κ_C = κ/2, log2 κ_C = −1659.2644. Shkredov writes "κ may vary from line to line" and the appendix never re-halves. The ledger keeps the halving because Sec. 5.4 applies Cor 16.
6. **Sec 5.4 condition** (p.37): |A| ≫ M_*^-1 q^{w_M} N^{1−w_M} H^{2(w_{M*}−1)} and |A ∩ A^-1| ≥ |A|²φ(q)/(2q²) provided M^-1 q^{w_M} N_*^{κ} ≫ q^{1+o(1)}. Here N_* = N/H² = N^{1/10}, H = N^{9/20}, N = q^{2ε}. For fixed M and q → ∞ this is exactly
   **1 − w_M < 2ε κ_C/10 = ε κ_C/5.**
   Shkredov drops the factor N^{w_{M*}−w_M+(1−w_{M*})/10} ≥ 1. Keeping it (option `exact_exponent`) gives the exact condition (1−w_M)(1−2ε) + (9/5)ε(1−w_{M*}) < εκ_C/5. That saves only 0.17 bits.
7. **Thm 38** (Kurzweil, M ≥ 1000): 1 − 0.99/M ≤ w_M ≤ 1 − 1/(4M). Sufficient condition: 0.99/M ≤ εκ_C/5, i.e. **M_thr = 0.99·5/(ε κ_C) = 89.1/κ_C at ε = 1/18.** log2 M_thr = 1665.7418.
8. **ε → 1/18:** (119) requires N ≤ q^{1/9}/(2^30 M M* M~) and N = q^{2ε}, which gives (151) ε < 1/18 and (156) ε < 1/18 − o_M(1). For fixed M the loss is o(1) as q → ∞, and M_thr decreases in ε, so the infimum is at ε = 1/18.
9. **M\* ≥ 40M:** Sec 5.4/(155) needs 1 − w_M ≥ 10(1 − w_{M*}). With Thm 38: 1/(4M) ≥ 10·0.99/M\* ⇐ M\* ≥ 39.6M (Shkredov: 40M).
10. **Final partial-quotient bound:** (157) says "max{O(M\*), M~} ∼ max{10(κε)^-1, 100δ^-60}", where this δ ∈ [1/2,1] is the δ-Assumption parameter, not step 3. The App. sets M~ = 200 and drops the δ-Assumption. The O(·) is Lemma 10's factor 4: x|y| ≥ q/(4M\*) ⇒ c_j ≤ 4M\*. Remark 11 says it could be M\*+2.

## 3. Three readings of "the M of Corollary 1" (baseline inputs)

| reading | formula | log2 M |
|---|---|---|
| A: (157) literal, with the true κ | 10/(κ ε) | **1665.76** |
| A with Shkredov's stated κ = 2^-1656 | 10·18·2^1656 | 1663.49 |
| B: full visible chain (steps 5–10) | 4 · 39.6 · 89.1/κ_C | **1673.05** |
| B, exact exponent (step 6 variant) | | 1672.88 |
| C: Thm 8 wording (22), c_j ≤ 100 M for M ≥ M_thr | 100 · M_thr | **1672.39** |

κ-independent overhead: M_B = C0/κ_{L14} with C0 = 4·39.6·89.1·2 = 28226.9, log2 C0 = 14.78. With κ = 1/2 this gives log2 M_B = 15.8. The DESIGN's "~2^21" also counts the ×100 of (22).

Note: (22)'s "100M" is below the rigorous 4·40M = 160M. It matches the heuristic M\* ≈ 10M (4·10M = 40M ≤ 100M). That is a cosmetic inconsistency and is immaterial to the final number.

## 4. Sensitivity table (from `B_ledger.out`; all other inputs at baseline)

| scenario | c | binding term | k | log2 kappa(L14) | log2 M [A: (157) literal] | log2 M [B: full visible chain] | log2 M [C: 100*M_thr] |
|---|---|---|---|---|---|---|---|
| baseline (c_H=1/20, C1=9, C2=32, tau=1/4) | 1/1640.0 | cH | 1641 | -1658.26 | 1665.8 | 1673.0 | 1672.4 |
| c_H = 1/20 | 1/1640.0 | cH | 1641 | -1658.26 | 1665.8 | 1673.0 | 1672.4 |
| c_H = 1/15 | 1/1230.0 | cH | 1231 | -1247.85 | 1255.3 | 1262.6 | 1262.0 |
| c_H = 1/12 | 1/984.0 | cH | 985 | -1001.53 | 1009.0 | 1016.3 | 1015.6 |
| c_H = 1/10 | 1/820.0 | cH | 821 | -837.26 | 844.8 | 852.0 | 851.4 |
| c_H = 1/8 | 1/656.0 | cH | 657 | -672.94 | 680.4 | 687.7 | 687.1 |
| c_H = 1/6 | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| c_H = 1/5 | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| c_H = 1/4 | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| c_H = 1/3 | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| c_H = 1/2 | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| C1 halved (4.5) | 1/1460.0 | cH | 1461 | -1478.10 | 1485.6 | 1492.9 | 1492.2 |
| C2 halved (16) | 1/1000.0 | cH | 1001 | -1017.55 | 1025.0 | 1032.3 | 1031.7 |
| C1, C2 both halved | 1/820.0 | cH | 821 | -837.26 | 844.8 | 852.0 | 851.4 |
| tau = 1/5 (MMS 2212.14646 girth) | 1/1640.0 | cH | 1641 | -1658.26 | 1665.8 | 1673.0 | 1672.4 |
| tau = 1/8 (MMS 1808.05845: m <= d/2) | 1/1640.0 | cH | 1641 | -1658.26 | 1665.8 | 1673.0 | 1672.4 |
| tau = 1/20 (MMS22 m-coefficient tau/4) | 1/2560.0 | tau4C2 | 2561 | -2578.91 | 2586.4 | 2593.7 | 2593.0 |
| c_H=1/2, tau=1/5 | 1/640.0 | tau4C2 | 641 | -656.91 | 664.4 | 671.7 | 671.0 |
| c_H=1/4, tau=1/5 | 1/640.0 | tau4C2 | 641 | -656.91 | 664.4 | 671.7 | 671.0 |
| c_H=1/8, tau=1/5 | 1/656.0 | cH | 657 | -672.94 | 680.4 | 687.7 | 687.1 |
| c_H=1/2, C2 halved | 1/256.0 | tau4C2 | 257 | -271.58 | 279.1 | 286.4 | 285.7 |
| BSG loss removed in c_H term only: min{1/3,1/(8C2),tau/(4C2),c_H/2} | 1/512.0 | tau4C2 | 513 | -528.58 | 536.1 | 543.4 | 542.7 |
| R2 claim: all C2-terms gone, min{1/3, c_H/2} | 1/40.0 | cH | 41 | -52.91 | 60.4 | 67.7 | 67.0 |


Reading the table:
* c_H saturates at c_H = 0.16 (τ = 1/4) or 0.128 (τ = 1/5), because the τ/(4C2) term takes over. With C2 = 32 the floor is **log2 M ≈ 543** (τ = 1/4) or **≈ 672** (τ = 1/5). The design's "minimal 500" is therefore unreachable without also improving C2 or the τ-term.
* Halving C2 is worth more than halving C1: 1032 vs 1493. With c_H = 1/2 and C2 = 16 the floor becomes 1/(8C2) = τ/(4C2) = 1/256, i.e. about 286.
* "BSG loss removed from the c_H term only" still stops at 1/512 (543). **The R2 figure "log2 M ≈ 70" assumes all three C2-terms disappear** (min{1/3, c_H/2} = 1/40 → 67.7). Whether the (8C2)^-1 and τ(4C2)^-1 terms also come from BSG is exactly the N1 question (Agent A). If they are BSG-independent, R2's ceiling is 543, not 70.

### Overhead factors removed one at a time (reading B, baseline 1673.05)

| factor removed | source | log2 M [B] | saving (bits) |
|---|---|---|---|
| Lemma 10: 4 -> 1 (Remark 11, M+2) | Lemma 10 / Rem. 11 | 1671.05 | 2.00 |
| Thm 38 slack: M* ratio 39.6 -> 10 (needs 1-w_M ~ 6/(pi^2 M) both sides) | Thm 38 / Hensley Thm 12 | 1671.08 | 1.97 |
| M* ratio 39.6 -> 1 (no second Cantor level) | Sec 5.4 (155) | 1667.76 | 5.29 |
| Cor 16 halving kappa/2 -> kappa | Cor 16 proof | 1672.05 | 1.00 |
| N_* = N^(1/10) -> N (H=1) | Sec 5.4, H=N^(9/20) | 1669.73 | 3.32 |
| eps 1/18 -> 1/4 (interval length q^(1/2)) | (119),(151),(156) | 1670.88 | 2.17 |
| 0.99 -> 6/pi^2 ~ 0.6079 (Hensley asymptotic) | Thm 38 vs Thm 12 | 1671.64 | 1.41 |
| kappa = delta/6 -> delta | App. [43,p.9] | 1670.46 | 2.58 |
| delta = c/2^(k+4) -> c/2^k | App. | 1669.05 | 4.00 |
| factor c in delta -> 1 | App. | 1662.37 | 10.68 |
| k = ceil(1/c)+1 -> ceil(1/c) | App. | 1672.05 | 1.00 |
| all pure bookkeeping at once (Lemma10->1, M* ratio->10 with 6/pi^2, Cor16 halving, /6, 2^4, +1) | | 1659.78 | 13.27 |
| ... plus N_*->N, eps->1/4, c-prefactor in delta | | 1643.60 | 29.45 |


All the κ-independent overheads together are worth about 30 bits out of 1673. The remaining ~1640 bits are 2^{1/c}. Only c (and the k-formula) matter. R5 is worth at most ~30 bits.

### Targets (reading B, Shkredov's overheads kept)
log2 M <= 500: need 1/c <= 468 (log2 M = 499.24 at c = 1/468)
log2 M <= 150: need 1/c <= 120 (log2 M = 149.28 at c = 1/120)

Every other min-term must then also be ≥ this c. At τ = 1/4: C2 ≤ 29.25 for the 500 target, and C2 ≤ 7.5 for the 150 target.

## 5. N2 settled

**(a) 2^-1656 vs 2^-1658.** From the appendix's formulas: δ = c/2^{k+4} = 2^-1655.68 and κ = δ/6 = 2^-1658.26. The claim "κ ≥ 2^-1656" is off by a factor 2^2.26 ≈ 4.8 in the wrong direction. The most likely cause is that the /6 was dropped, since 2^-1656 is δ rounded down. Correct: **κ_{L14} = 2^-1658.264 > 2^-1659**. The Cor 16 exponent used in Sec 5.4 is 2^-1659.264. Effect on M: +2.26 bits (plus 1 bit for the Cor 16 halving). Effect on the 2^2000 claim: none.

**(b) τ = 1/4 vs 1/5.** Three different normalisations share the letter τ:
1. MMS 1808.05845 Thm 25: d(Cay(PSL2(F_p), T)) ≥ (1/4) log_N p, for T = {(1,−2j; 2j,1−4j²)}, 1 ≤ j ≤ N, p ≫ 1. Here d is the max radius with distinct paths, and girth ∈ {2d−1, 2d}. Their Thm 24 then uses m ≤ γ/2 (so τ ≤ τ0/2 = 1/8) and K = |S|^{m/4}.
2. MMS 2212.14646v1 p.5–6: "girth … at least τ log_N p, τ = 1/5", m = (τ/4) log_N p, K(G) = p^{τ/6}.
3. Shkredov App.: τ = 1/4, m = τ log_N p, K(G^m) = p^{τ/6}, citing [42, Lemmas 12, 21] and the IMRN [43, p.7].

Verdict: **τ = 1/4 is correct as the sourced constant**. It is exactly τ0 of MMS18 Thm 25 in Shkredov's normalisation. MMS22's 1/5 is a weaker but also valid girth statement in a different normalisation (m = τ/4·log_N p). **For the ledger it does not matter.** In κ = δ/6 the τ cancels, and τ/(4C2) does not bind for τ ≥ 0.078: τ = 1/4, 1/5 and 1/8 all give the identical 1673.05.

Caveat for RB1: Shkredov's m = τ log_N p = (1/4) log_N p equals the full d-bound, whereas MMS18's proof takes m ≤ d/2 and MMS22 takes m = d/5. If the correct constraint forces the τ entering the min{…} to be the m-coefficient in MMS22's sense (1/20), then τ/(4C2) = 1/2560 binds and log2 M = 2593.7, which **exceeds 2000**. I found no text saying which τ enters [53, Thm 49]'s derivation, so this reading is listed only as a table row, not as a claim.

**(c) Structural question (not N2 proper, but found while settling it): the doubling count.**
| reading of k | tau | c | k | log2 M [B] |
|---|---|---|---|---|
| appendix: k = ceil(1/c)+1 | 1/4 | 1/1640 | 1641 | 1673.0 |
| k = ceil((log(|G|/d)/log K)/c)+1, K=p^(tau/6): 12/tau | 1/4 | 1/1640 | 78721 | 78753.0 |
| k = ceil((log|G|/log K)/c)+1 (survey Thm 49 error<main): 18/tau | 1/4 | 1/1640 | 118081 | 118113.0 |
| appendix: k = ceil(1/c)+1 | 1/5 | 1/1640 | 1641 | 1673.0 |
| k = ceil((log(|G|/d)/log K)/c)+1, K=p^(tau/6): 12/tau | 1/5 | 1/1640 | 98401 | 98433.0 |
| k = ceil((log|G|/log K)/c)+1 (survey Thm 49 error<main): 18/tau | 1/5 | 1/1640 | 147601 | 147633.0 |

In MMS18 Thm 15 / Thm 9 each flattening doubling gains K^{c*}, and the Hölder step gives δ = 2^-(k+2) with k = 3 log p/(c* log K). In survey Thm 49 the saving is K_*^{-ck} for 2k-fold products. In both, the number of steps needed to reach the |G|^-1 or |G|/d scale is ∝ (log p / log K)/c. With K = p^{τ/6}, log p/log K = 6/τ = 24. The appendix writes k = ⌈1/c⌉+1 with no log p/log K factor, and "log N·κ = (6m)^-1 τ δ log p" means a saving K^{-δ/m}. So either (i) Shkredov's c is normalised so that the factor is absorbed, or (ii) the saving only needs to beat K rather than |G|. Neither is visible in the text I could read. **This must be resolved from the IMRN [43, p.9] before any campaign number is quoted as "Shkredov's chain gives X".** If the pessimistic reading held, 2^2000 would not follow from the appendix as written. That would be a finding about the literature, to be reported only after RB1 and an author-level check, never as a headline.

## 6. Other items for referees (from reading, not computation)

* **Lemma 40 vs RS Thm 2:** RS assumes a *symmetric* generating set with |A| above an absolute constant. The appendix states it for "a generating set". Thm 39's output A_* ⊆ a^-1 A is not symmetric in general. It is probably harmless (e.g. symmetrise with a constant loss) but unaccounted in c.
* **Lemma 15 vs Lemma 14 κ:** Cor 16 uses Lemma 15 (2-parameter family S = [N]², δ = 1), whose κ(δ) comes from the girth-free machine [55]. The appendix computes "the constant κ from Lemmas 14, 15" with the single Lemma-14 formula. The two constants are not shown to be the same.
* **ε ∼ 1/M vs ε < 1/18:** consistent. For fixed M the o(1) losses are q-dependent only, so q0 is not explicit, as stated.
* **Thm 38 range M ≥ 1000:** satisfied trivially.

## 7. What this means for the campaign

* R1 (substitution) cannot reach 500. Its floor with c_H → ∞ is 543 (τ = 1/4, C2 = 32). Any announce-worthy claim needs C2 (BSG) improved **and** c_H improved, or a route that bypasses the min{…}.
* R2's "≈70" is conditional on all C2-terms disappearing. Agent A's N1 must say which terms are BSG-born.
* R5 is worth ≤ 30 bits. Irrelevant unless R2–R4 succeed.
* The k-formula question (§5c) is an RB1 priority. It could move Shkredov's own number by a factor of ~50–70 in the exponent.
