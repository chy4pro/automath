# CR-16 (Erdős #542): lcm-separated sets, new leading constant — v2 (repaired)

**STATUS: PROVED** (target and stretch both met). v2 replaces the floating-point finite check with an exact integer check (REF-1 and REF-2 repairs, see the change log at the end). The theorem, its constants and its onsets are **unchanged**.

**Theorem.** For every integer n ≥ 1,

  rho(n) ≤ V_1 + E_1/n ≤ 1.0087578638 + 87.5686331624/n,

where V_1 ∈ [1.008757863713504319, 1.008757863713504320] and E_1 = 564156623381/6442450944 ∈ [87.568633162261297305, 87.568633162261297306]. Both enclosures are outward and exact (§3).

Consequences: rho(n) ≤ 1.0170 for all n ≥ 10625, and rho(n) ≤ 1.01 for all n ≥ 70499 (stretch target). These are the least onsets that follow from the displayed constants 1.0087578638 and 87.5686331624, checked in exact arithmetic. So rho(n) ≤ 1.00876 + r(n) with the explicit r(n) = 87.5686331624/n → 0, against the old leading constant 1.0170166.

The benchmark in the exact form "rho(n) ≤ 1.0170 + 15/(n−58) for all n ≥ 59" follows by combining this with the given baseline:
- for 59 ≤ n ≤ 47648 the baseline gives rho(n) ≤ 1.0170166 + 14.21/(n−58) ≤ 1.0170 + 15/(n−58), because 0.79/(n−58) ≥ 0.79/47590 = 0.0000166 + 3/23795000000 there;
- for n ≥ 10625 the theorem gives rho(n) ≤ 1.0170.

Our own additive term alone does not reach the form 15/(n−58) for 71 ≤ n ≲ 8800. That does not matter for the target, which is about the leading constant.

(Side remarks, not needed for the proof. Exact brute force gives rho(5) = 31/30, rho(11) = 4699/4620, and rho(n) = 1 for every other n ≤ 29; both referees confirmed this independently. A floating-point LP relaxation gives value 1.0 at every n tested in [12, 5000]. This suggests, but does not prove, that rho(n) = 1 for all n ≥ 12, in which case 1.00876 is not sharp. See §5.)

---

## 1. The duality principle

**Lemma 1 (weak duality).** Let z_1, …, z_n ≥ 0 satisfy Σ_{k ≤ n/a} z_{ka} ≥ 1/a for every a ≤ n. Then rho(n) ≤ Σ_{m=1}^n z_m.

*Proof.* Let A be lcm-separated. The sets M(a) = {ka ≤ n}, a ∈ A, are pairwise disjoint: a common element would be a multiple of lcm(a,b) that is ≤ n. So
Σ_{a∈A} 1/a ≤ Σ_{a∈A} Σ_{m∈M(a)} z_m ≤ Σ_{m≤n} z_m, using z ≥ 0. ∎

Experimental motivation (not part of the proof; floating-point LPs on specific grids only): with weights that depend only on m/n, the tested discretisations stayed at about 1.0172–1.0175. The greedy dual gave 1.01727 at n = 10⁵, and the step LP on the bins (1/(j+1), 1/j] gave 1.01726 for J = 80 and J = 150. These numbers do not prove any lower limit for that family, and they say nothing definite about how the classical constant was obtained. **The new ingredient is to let the weight also depend on the arithmetic of m, through gcd(m, 6).** Weight then moves onto integers with more small divisors, and the LP value drops.

## 2. The dual family

Fix L = 6 (squarefree), P = 4 and δ = 1/10. Let

  G = { p/j : 1 ≤ p ≤ 4, p ≤ j ≤ 10p } = {g_0 = 1/10 < g_1 < … < g_54 = 1}

(duplicates removed). This gives 54 bins I_b = (g_b, g_{b+1}], indexed **b = 0, …, 53**. For each η | 6 and each bin b, a coefficient c_{η,b} = C_{η,b}/2³⁰ is fixed, where C_{η,b} is a nonnegative integer.

**Certificate format.** `cert_main.txt` (sha256 `361c296fad7662dadc53699aead4f2eb33fdbff7e0d18efd3971535acec8534e`) has the header `6 4 1/10 1/10000` (L, P, δ, x_1), followed by lines `η b C_{η,b}`. Bin indices are 0-based. Every pair (η, b) that is not listed has C_{η,b} = 0. The file lists 67 distinct pairs, all positive integers below 2³²; the verifier rejects duplicate pairs. The largest coefficient is C_{6,53}/2³⁰ ≈ 2.459.

Define c_η(t) = c_{η,b} for t ∈ I_b, and c_η(t) = 0 for 0 < t ≤ 1/10. For a given n put

  z_m := c_{gcd(m,6)}(m/n) / m  (1 ≤ m ≤ n).

**Reduction of the dual constraint.** Let a ≤ n, x = a/n and γ = gcd(a,6). Since 6 is squarefree, gcd(ka,6) = lcm(γ, gcd(k,6)) =: γ∨k (a prime p ∈ {2,3} divides ka iff it divides a or k). Hence

  a·Σ_{k≤n/a} z_{ka} = Σ_{k ≤ 1/x} c_{γ∨k}(kx)/k =: F_γ(x).

So Lemma 1 applies as soon as **F_γ(x) ≥ 1 for all real x ∈ (0,1] and all γ | 6**. This condition does not depend on n, so one certificate covers every n.

**Notation.** V_γ := Σ_{r=0}^{5} (1/6) Σ_b c_{γ∨r,b} log(g_{b+1}/g_b) and E_γ := Σ_{r=0}^{5} Σ_b c_{γ∨r,b}/g_b, where γ∨r = lcm(γ, gcd(r,6)) and gcd(0,6) = 6.

## 3. The three estimates

**Lemma 2 (AP harmonic bounds).** Let L ≥ 1, r be an integer and 0 < A < B.
- (lower) Σ_{A<k≤B, k≡r (L)} 1/k ≥ (1/L) log(B/(A+L)).
- (upper) Σ_{A<k≤B, k≡r (L)} 1/k ≤ 1/A + (1/L) log(B/A).

*Proof.* Lower: if A+L ≥ B the right-hand side is ≤ 0 and the sum is ≥ 0. Otherwise, let k_0 be the least AP member > A and k_1 the largest ≤ B. Then k_0 ≤ A+L and k_1+L > B, so the intervals [k, k+L], k_0 ≤ k ≤ k_1 in the AP, have disjoint interiors and cover [A+L, B]. Also 1/k ≥ (1/L)∫_k^{k+L} dt/t. Upper: an empty sum is trivial. The first term is < 1/A, and every later term satisfies 1/k ≤ (1/L)∫_{k−L}^{k} dt/t; these intervals have disjoint interiors and lie in [A, B]. ∎

**Lemma 3 (piecewise constancy).** Let S = {p/N : 1 ≤ p ≤ 4, N ≥ 1}. If v' < v are consecutive elements of S, then F_γ is constant on (v', v].

*Proof.* Take x ∈ (v', v]. The condition k ≤ 1/x can change only at x = 1/k ∈ S. The bin containing kx can change only when kx crosses some g = p'/j ∈ G, i.e. at x = p'/(jk) ∈ S. No element of S lies strictly between v' and v. Because the bins are right-closed (and c = 0 on (0, 1/10], and the cutoff k ≤ 1/x is inclusive), the value at x = v equals the value on (v', v). ∎

Hence F_γ(x) = F_γ(v) where v = min{s ∈ S : s ≥ x}.

**Step A: finite range x ∈ [x_1, 1], x_1 = 1/10000 — exact integer check.** Since x_1 ∈ S, Lemma 3 reduces this range to F_γ(v) ≥ 1 for the points v ∈ S ∩ [x_1, 1] and the 4 values of γ. In reduced form these are the p/N with 1 ≤ p ≤ 4, p ≤ N ≤ 10000p and gcd(p,N) = 1: 10000 + 9999 + 19998 + 19998 = 59 995 points, so 239 980 constraints. For every point, ⌊N/p⌋ ≤ 10000.

Put Q = 2⁴⁸ and, for 1 ≤ k ≤ 10000,

  h_{γ,b}(k) = ⌊C_{γ∨k,b} · 2¹⁸ / k⌋,  Pre_{γ,b}(K) = Σ_{k=1}^K h_{γ,b}(k).

Then h_{γ,b}(k)/Q ≤ c_{γ∨k,b}/k < h_{γ,b}(k)/Q + 1/Q. For v = p/N let K_i = ⌊g_i N/p⌋ (exact integer division), which is the number of k ≥ 1 with kv ≤ g_i. The k with g_b < kv ≤ g_{b+1} are exactly K_b < k ≤ K_{b+1}, and the k ≤ K_0 have coefficient 0. Also K_54 = ⌊N/p⌋ is the cutoff k ≤ 1/v. So

  T_γ(v) := Σ_{b=0}^{53} [Pre_{γ,b}(K_{b+1}) − Pre_{γ,b}(K_b)]  satisfies  T_γ(v)/Q ≤ F_γ(v) < T_γ(v)/Q + 10000/Q.

**Arithmetic model.** `verify.py` uses only Python's arbitrary-precision integers and `fractions.Fraction`; it contains no floating-point operation. Prefix sums are stored in `array('q')` (signed 64-bit). Prefix sums are stored up to Kmax = 40000, and every stored value is ≤ 2.65·10⁹ · 2¹⁸ · H_{40000} ≤ 2.65·10⁹ · 2¹⁸ · 16 = 11114905600000000 < 2⁶³ (H_{40000} < 12), and any out-of-range store raises `OverflowError` rather than wrapping. So every quantity is exact.

**Result.** min over all 239 980 constraints of T_γ(v)/Q = 281475258209621/281474976710656 ≥ 1.000001000085223523 > 1, attained at (v, γ) = (4/15, 1). So F_γ ≥ 1 on [x_1, 1].

**Exact minimum (extra information).** All (v, γ) with T_γ(v)/Q ≤ F_1(4/15) are re-evaluated as exact rationals. There is only one, namely (4/15, 1) itself. Every other pair has F ≥ T/Q > F_1(4/15). Hence

  min F_γ(v) = F_1(4/15) = 0 + C_{2,48}/(2·2³⁰) + C_{3,52}/(3·2³⁰) = 6442457387/6442450944 = 1.0000010000852247… .

This equals REF-1's integer bound and exact minimum.

**Step B: tail x ∈ (0, x_1).** Split k by bin b and by residue r mod 6, and apply the Lemma 2 lower bound with A = g_b/x and B = g_{b+1}/x:

  F_γ(x) ≥ Σ_r Σ_b c_{γ∨r,b}[(1/6)log(g_{b+1}/g_b) − (1/6)log(1 + 6x/g_b)] ≥ V_γ − x·E_γ ≥ V_γ − x_1·E_γ,

using log(1+y) ≤ y for y ≥ 0, c ≥ 0 and E_γ ≥ 0.

*Rational log enclosures.* For rational y > 1 put s = (y−1)/(y+1) ∈ (0,1) and ℓ(y) = 2 Σ_{j=0}^{29} s^{2j+1}/(2j+1). Then log y − ℓ(y) = 2∫_0^s t^{60}/(1−t²) dt ∈ [0, 2s^{61}/(61(1−s²))]. Replacing every log by these exact rational bounds, with c ≥ 0, gives exact rational V_{γ,lo} ≤ V_γ ≤ V_{γ,hi}. The verifier proves V_{γ,lo} − x_1·E_γ − 1 > 0 for each γ, in exact rational arithmetic. Decimals below are rounded outward by integer division:

| γ | V_γ enclosure | E_γ (exact) | V_{γ,lo} − x_1E_γ − 1 ≥ |
|---|---|---|---|
| 1 | [1.008757863713504319, 1.008757863713504320] | 564156623381/6442450944 | 0.000001000397278190 |
| 2 | [1.221116740952808711, 1.221116740952808712] | 318232260905/3221225472 | 0.211237511334417068 |
| 3 | [1.128746579478093456, 1.128746579478093457] | 107202918283/1073741824 | 0.118762529691931825 |
| 6 | [1.260428018694485595, 1.260428018694485596] | 99593551913/1073741824 | 0.251152646376214048 |

Steps A and B give F_γ ≥ 1 on (0, 1] for every γ | 6, so z is dual-feasible for every n.

**Step C: total mass.** By the Lemma 2 upper bound with A = n·g_b and B = n·g_{b+1}, which holds for every n ≥ 1 even when a progression interval is empty, and since c = 0 at and below 1/10:

  Σ_{m≤n} z_m = Σ_r Σ_b c_{gcd(r,6),b} Σ_{m≡r (6), ng_b<m≤ng_{b+1}} 1/m ≤ V_1 + E_1/n.

The verifier checks the exact rational inequalities V_{1,hi} ≤ 10087578638/10¹⁰ and E_1 ≤ 875686331624/10¹⁰. With Lemma 1 this proves the Theorem. ∎

**Onsets.** For B ∈ {1.0170, 1.01} the verifier computes the least integer n with 1.0087578638 + 87.5686331624/n ≤ B as ⌈87.5686331624/(B − 1.0087578638)⌉ in exact rationals. It gets 10625 and 70499, and the bound is decreasing in n.

## 4. Reproduction

```
python3 verify.py cert_main.txt        # standard library only, ~2 CPU-s, ~72 MiB; ends with "RESULT OK"
python3 crosscheck.py cert_main.txt 1 2 5 11 100 997 1000 5040 20011    # ~0.5 s, ends with "CROSSCHECK OK"
```

Saved outputs: `verify_output.txt`, `crosscheck_output.txt`. **`verify.py` alone carries the proof.** It checks Step A (all 239 980 constraints and the exact minimum), Step B (four exact tail inequalities), the theorem constants, both onsets and the benchmark overlap arithmetic. Negative control: lowering the single entry C_{2,48} by 10⁴ makes the verifier print `FAIL finite range` / `RESULT FAIL`, with min F = 0.99999634….

`crosscheck.py` is an independent code path. It builds z_m for a concrete n by exact rational bin lookup and tests a·Σ_k z_{ka} ≥ 1 for every a ≤ n. Each term is enclosed by integer floor/ceil with denominator 2⁴⁸. It also checks that the upper enclosure of Σ z_m is at most the theorem's bound 1.0087578638 + 87.5686331624/n. Results:

| n | min_a a·Σ_k z_{ka} ≥ | Σ z_m ≤ |
|---|---|---|
| 1 | 1.000001000240445 | 1.000001000240446 |
| 2 | 1.054504025727510 | 1.054504025727511 |
| 5 | 1.000001000240445 | 1.064258680849652 |
| 11 | 1.000001000240445 | 1.031375302518033 |
| 100 | 1.000001000240445 | 1.000001000367039 |
| 997 | 1.000001000085223 | 1.009992335549399 |
| 1000 | 1.000001000085223 | 1.009017157250768 |
| 5040 | 1.000001000085223 | 1.008592039315766 |
| 20011 | 1.000001000085223 | 1.008750262227068 |

These agree with REF-1's independent Node computation. For n = 5 and n = 11 the totals are ≥ rho(5) = 1.0333… and rho(11) = 1.01710…, as they must be.

How the certificate was found (not part of the proof):
- `cont.py 6 4 1/10 1/10000` (scipy HiGHS, plain floating-point LP, no ILP) minimises V_1 subject to the Step-A constraints and the linear tail constraint.
- `mkcert.py` scales the solution by (1 + 10⁻⁶) and rounds each entry up to a multiple of 2⁻³⁰. It then drops entries whose scaled value is below 10⁻¹². That cutoff is applied after the ceiling, so the output is not literally an upward rounding of every entry. Nothing depends on this, because the final certificate is checked exactly.
- `brute.py` gives exact rho(n) for n < 30. `lp.py` gives the discrete LP value in floating point.

## 5. Routes tried, obstructions, remarks

All numerical values in this section come from floating-point LP experiments on the grids named. They are experimental observations, not theorems.

1. **Continuum dual z_m = c(m/n)/m with c a step function on the bins (1/(j+1), 1/j].** F is then constant on (1/(N+1), 1/N] with value Σ_k c_{⌊N/k⌋}/k, which is clean. But on the tested grids (J = 80 and J = 150, M up to 10⁴) the LP optimum was **1.017263**, and the greedy top-down dual gave 1.01727 at n = 10⁵. Observed obstruction: on these grids, weights depending only on m/n did not get below about 1.0172. This is not a proof for the whole family, and any link to the classical constant is a guess.
2. **Adding residue classes mod 2, 6 or 12 on the same coarse 1/j grid** reached only 1.017358 in the tested runs. The grid appears too coarse near t ∈ (1/3, 1].
3. **What worked:** arithmetic classes gcd(m,6) together with the finer grid {p/j : p ≤ 4}. A discrete floating-point probe at n = 4999, with L = 30 and 1/48 bins, suggests that V ≈ 1.000 may be reachable.
4. **Limit of this method.** The tail term x·E_γ costs about x_1·E ≈ 0.0088, which is the whole gap V − 1. Pushing V toward 1 needs a smaller x_1, with verification cost about P²/(4x_1²) terms, or a sharper tail lemma that uses cancellation between adjacent bins (smooth c). Not pursued.
5. **Conjecture (unproved): rho(n) = 1 for all n ≥ 12.** The LP relaxation max Σ y_a/a subject to Σ_{a|m} y_a ≤ 1, 0 ≤ y ≤ 1, has floating-point value 1.0 at n = 12..30, 60, 100, 200, 400, 1000, 2000 and 5000. Its optimal dual puts all mass on m > n/3 and weights integers with many divisors. Exact brute force confirms rho(n) = 1 for 12 ≤ n ≤ 29. Proving this for all n would need a dual that is exactly tight (total 1) uniformly in n. The certificate above is only within 0.0088 of that.

## Change log v1 → v2 (2026-10-12)

Old files are kept as `report_v1.md`, `verify_v1.py`, `crosscheck_v1.py` and `mkcert_v1.py`. `cert_main.txt` is unchanged (same sha256).

| # | Referee point | Change |
|---|---|---|
| 1 | REF-1 §1, REF-2 §1 (repairable): the Step-A justification assumed `math.fsum` is correctly rounded, and the final `s − 2Us·1.0000001` was not directed-rounded (REF-2 countermodel s = 5/4). | `verify.py` rewritten in pure integer/Fraction arithmetic with no floats and no numpy: integer-prefix lower enclosure with Q = 2⁴⁸, plus exact re-evaluation of every candidate for the minimum. Step A of the report rewritten with the arithmetic model and an overflow argument. New min lower bound 281475258209621/2⁴⁸ (> 1); exact min 6442457387/6442450944 at (4/15, 1). Both equal REF-1's values. |
| 2 | REF-1 §2, REF-2 §2 (repairable): the printed "V_1 ≤ 1.0087578637135" is false (rounded down). `verify.py` printed V_1 with `%.10f` (nearest), and `crosscheck.py` used 1.0087578637. | The report now states V_1 ∈ [1.008757863713504319, 1.008757863713504320], and all decimals are printed outward by integer floor/ceil. `verify.py` asserts V_{1,hi} ≤ 10087578638/10¹⁰ and E_1 ≤ 875686331624/10¹⁰ exactly. `crosscheck.py` compares against the theorem constants and now uses exact integer enclosures. |
| 3 | REF-1 §3, REF-2 §3 (repairable, expository): LP plateaus were stated as a barrier for every m/n-only weight and as the origin of the classical constant. | §1 and §5 reworded: the values are experimental, on the tested grids only, with no claimed limit for the family and no historical claim. The rho(n) = 1 statement is labelled unproved. |
| 4 | REF-1 §4 (cosmetic): certificate conventions; `mkcert.py` cutoff. | §2 states that bins are 0-indexed, omitted pairs are zero, there are 67 entries and duplicates are rejected. §4 and a header comment in `mkcert.py` describe the 10⁻¹² cutoff applied after the ceiling. |
| 5 | REF-2 §4 (cosmetic): strict "<" in the use of the baseline. | Changed to "≤", and the overlap margin 3/23795000000 is given exactly. |
| 6 | (REF-1 §8 / §13, minor) | Small-case side remark corrected to the complete list: rho(5) = 31/30, rho(11) = 4699/4620, otherwise rho(n) = 1 for n ≤ 29. The Lemma 2 and Lemma 3 boundary cases are spelled out. Onsets are stated as least onsets for the displayed constants. |

**Constants:** none changed. V = 1.0087578638, E = 87.5686331624, and the onsets 10625 and 70499 are all identical to v1.

Cost of v2: local compute < 10 CPU-seconds in total (verifier ~2 CPU-s, 72 MiB peak RSS, single thread); no solver. API spend for this repair task is roughly $3 (estimate).
