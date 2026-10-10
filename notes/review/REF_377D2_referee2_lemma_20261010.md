PASS

Session lineage: resumed referee-2 session of AUT-101 (third round, lemma confirmation only). My earlier reports are REF_377D2_referee2_20261010.md and REF_377D2_referee2_repairs_20261010.md. I read only `publish/automath-papers/erdos377/main.tex`, l. 166–179, 238–507 and 764–772, and not the other referee's reports.

# REF #377-D2 — third round: Lemma lem:nested and its use (referee-2)

**Verdict.** My second-round repair S1 is fully resolved, and I found no new defect.
- Lemma lem:nested is correctly stated and proved, with the explicit error 8mX/Q.
- Its hypotheses hold at both points of use.
- Lemma lem:local now depends only on eq:uniform1 and eq:uniform2, which the paper itself proves with explicit constants. It no longer depends on any unprinted uniformity or on EGRS statement (1).
- The program-scope wording is accurate.

## (1) Lemma lem:nested (l. 278–338)

**Statement.**
- **Hypotheses.** X and the w_i are positive integers, Q ≥ 2 is real, w_1 ≥ Q, w_{i+1}/w_i ≥ Q, and X/w_m ≥ Q.
- **Count.** C counts the integers 1 ≤ n ≤ X with n mod w_i < w_i/2 for every i.
- **Claim.** |C − 2^{−m}X| ≤ 8mX/Q.
- **No hidden assumptions.** The lemma needs neither coprimality nor primality of the moduli.

**Proof, checked line by line.**
- **One modulus.** The accepted residues mod w_i are 0, …, ⌈w_i/2⌉ − 1, so c_i·w_i = ⌈w_i/2⌉. A complete block contributes 0 to Σ(h_i − c_i), and the remainder contributes less than w_i in absolute value. This gives eq:perioderror.
- **Changes of h_j.** On {1, …, X}, h_j changes value only where n+1 ≡ 0 or n+1 ≡ ⌈w_j/2⌉ (mod w_j), so it changes at most 2X/w_j + 2 times.
- **Runs of ones.** A 0/1 sequence with c changes has at most c + 1 runs of ones. Hence R_i ≤ 1 + Σ_{j>i}(2X/w_j + 2).
- **Chain of inequalities.** I checked each step:
  - 2X/w_j + 2 ≤ 3X/w_j, because X/w_j ≥ X/w_m ≥ Q ≥ 2;
  - Σ_{j>i} 1/w_j ≤ 2/w_{i+1}, by the geometric series with ratio 1/Q ≤ 1/2;
  - 1 + 6X/w_{i+1} ≤ 7X/w_{i+1}, because X/w_{i+1} ≥ 1.
- **Terms i < m.** Applying eq:perioderror on each run gives ≤ R_i·w_i ≤ 7X·w_i/w_{i+1} ≤ 7X/Q.
- **Term i = m.** The sum is at most w_m ≤ X/Q.
- **Telescoping.** The identity Πh − Πc = Σ_i (Π_{j<i} c_j)(h_i − c_i)(Π_{j>i} h_j) is exact. Since 0 ≤ c_j ≤ 1 and the h_j are 0/1, it gives |C − XΠc_i| ≤ (7(m−1) + 1)X/Q ≤ 7mX/Q.
- **Replacing Πc_i by 2^{−m}.** c_i − 1/2 ∈ {0, 1/(2w_i)}, and w_i ≥ Q. Telescoping with all factors ≤ 1 gives 0 ≤ Πc_i − 2^{−m} ≤ m/(2Q).
- **Total.** 7 + 1/2 < 8. The case m = 1 is covered.
- **Uniformity.** The bound depends only on (m, X, Q), so it is uniform over all admissible moduli, as the lemma states.

**Numerical test (not a proof step).** I tried 400 random admissible instances, with Q ∈ {2, 2.5, 3, 5, 10}, m ≤ 4, and X up to about 3·Q·w_m. By brute-force counting, the largest observed value of |C − 2^{−m}X| / (8mX/Q) was 0.068, so the bound is never approached.

## (2) Hypotheses where the lemma is applied (l. 340–376)

- **Divisibility criterion (l. 343–349).** By Legendre's formula, p ∤ B_n ⟺ n mod p^i < p^i/2 for every i ≥ 1. The i-th summand ⌊2n/p^i⌋ − 2⌊n/p^i⌋ equals 1 exactly when 2(n mod p^i) ≥ p^i, and all summands are nonnegative.
  - I checked the equivalence by brute force for p ≤ 11 and n < 400, with no exceptions.
- **Single prime in a trimmed band, r ≤ L.**
  - **Q ≥ 2.** X ≥ 2^{1/ε} gives Q = X^ε ≥ 2.
  - **Higher conditions are automatic.** p > X^{1/(r+1)+ε} gives p^{r+1} > X·Q^{r+1} ≥ 4X. So for n ≤ X and i ≥ r+1, n mod p^i = n < p^i/2.
  - **Remaining moduli.** These are p, …, p^r:
    - the smallest is p > X^a > X^ε = Q (using ε < a/4);
    - successive ratios are p > Q;
    - p < X^{1/r−ε} gives X/p^r > X^{rε} ≥ Q.
  - **Deletion of n < p.** A_1 counts p ≤ n ≤ X, so deleting n < p costs fewer than p integers, i.e. ≤ p/X ≤ X^{b−1} after normalizing.
  - **Result.** eq:uniform1 holds: ≤ 8rX^{−ε} + p/X ≤ 8LX^{−ε} + X^{b−1}. r ≤ L holds because r ≤ 1/a < ⌈2/a⌉.
- **Pairs (p ≠ q) in trimmed bands r, t ≤ L, under (5) with x = X.**
  - **Distinct moduli.** The merged moduli are distinct by unique factorization, so m = r + t ≤ 2L.
  - **Smallest modulus.** It is at least min(p, q) > X^a > Q.
  - **Ratios.** (5) is stated with strict inequalities: consecutive ratios exceed X^ε = Q, and X/w_{r+t} > Q. This implies the lemma's non-strict hypotheses.
  - **Higher conditions.** Powers beyond p^r and q^t are automatic, as in the single-prime case.
  - **Deletion of n < max(p, q).** This costs < max(p, q)/X ≤ X^{b−1}.
  - **Result.** eq:uniform2 holds: ≤ 8(r+t)X^{−ε} + max(p,q)/X ≤ 16LX^{−ε} + X^{b−1}.
- **Onsets (l. 398–408).** For X > max{2^{1/ε}, (32L/z)^{1/ε}, (2/z)^{1/(1−b)}}, both 16LX^{−ε} < z/2 and X^{b−1} < z/2, so e_1 < z and e_2 < z. Correct.
- **Retained pairs satisfy (5).**
  - A retained prime p has |log p/log X − 1/j| > ε for every j ≤ L, so it lies strictly inside its trimmed band.
  - Same-prime ratios are p > X^a > X^ε.
  - p^r < X^{1−rε} gives X/w_{r+t} > X^ε.
  - Cross ratios outside [X^{−ε}, X^ε] are exactly the complement of eq:ratio. So every retained pair not excluded by eq:ratio satisfies the strict inequalities of (5).

## (3) Errors used in lem:local

- **Definitions.** e_1 and e_2 (l. 391–402) are the maxima of exactly the quantities that eq:uniform1 and eq:uniform2 bound. Their explicit bounds are 8LX^{−ε} + X^{b−1} and 16LX^{−ε} + X^{b−1}.
- **How lem:local uses them.**
  - In m_X (first moment, l. 457–464) and in eq:second (second moment, l. 499–505), the error appears as (e_i + X^{b−1}).
  - That extra X^{b−1} for passing from n ≥ p (or n ≥ max(p, q)) to n ≥ 1 is a harmless double allowance: e_i already contains the deletion term.
  - Apart from the change of label, lines 432–507 are as I confirmed in round two.
- **Imports.** eq:input1 and eq:input2 are now marked as quotations, and l. 273–276 says they are not used as uniform remainders. The only imported moment is EGRS Theorem 2, the printed full first moment (l. 378–389). It is used in subsec:G, not in lem:local.
- **Conclusion.** lem:local depends on no unprinted uniformity and not on EGRS statement (1).
- **Remaining references.** The mentions of "classes I and II" (l. 471) and of condition (5) are labels for the page-88 classification and are not used as inputs.

## (4) Program-scope wording

- **l. 172–174.** "This is a claim about the construction …; the supplied program implements α = 1/s for integers s ≥ 2."
- **l. 769–771.** "The program as shipped implements α = 1/s for integers s ≥ 2; the construction extends to any rational 0 < α ≤ 1/2 by clipping the top band at α."
- Both are accurate. The program's `--s` option takes integers and asserts min(s) ≥ 2.

## Optional (cosmetic, no action required)

- **Clash of the symbol Q.** Q denotes X^ε in lem:nested and §subsec:local, but 2^{56} in §sec:numerics. A different letter in the lemma, for example Λ, would avoid the clash.

## Not checked in this round, by instruction

- Everything outside the four items above, which I confirmed in round two and which this edit did not change.
- Whether main.pdf matches main.tex. No PDF tools are available here.
