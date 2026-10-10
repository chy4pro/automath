PASS

Resumed referee-1 session of AUT-100. This is the third round, by the same session that wrote `REF_377D2_referee1_20261010.md` and `REF_377D2_referee1_repairs_20261010.md`. In this round I read only the revised `main.tex` (and the PDF spot-checked earlier) and my own two earlier reports.

# REF #377-D2 third round — Lemma lem:nested and the repair of N1

## Verdict

Repair N1 is applied correctly and completely. Lemma lem:nested is correct as stated, including the explicit constant 8mX/Q. Its hypotheses hold at both points of application. Lemma lem:local now uses only the proved bounds eq:uniform1 and eq:uniform2. It assumes no unprinted uniformity and does not rely on EGRS statement (1). The program-scope wording has been fixed. I found no gap, so no further repairs are needed.

## (1) Lemma lem:nested (lines 278–338): statement, hypotheses, proof, constant

**Statement.** X and m are positive integers and Q >= 2 is real. The moduli satisfy w_1 >= Q, w_{i+1}/w_i >= Q and X/w_m >= Q. Then |C - 2^{-m}X| <= 8mX/Q. I re-derived each step.

**Steps.**
* **Residue count.** Each block of w_i consecutive integers contains exactly ceil(w_i/2) residues r with r < w_i/2. On any run of consecutive integers, the complete blocks contribute zero error and the remainder (length < w_i) contributes less than w_i. This gives eq:perioderror. Correct.
* **Change points.** h_j changes value only where n mod w_j is 0 or ceil(w_j/2). On {1..X} that happens at most 2X/w_j + 2 times. The 1-set of H_{i+1} = prod_{j>i} h_j therefore has at most 1 + (number of change points) runs. Correct.
* **The bound on R_i.**
  - 2X/w_j + 2 <= 3X/w_j holds because X/w_j >= X/w_m >= Q >= 2.
  - sum_{j>i} 1/w_j <= (1/w_{i+1}) sum_k Q^{-k} <= 2/w_{i+1}, using Q >= 2.
  - 1 + 6X/w_{i+1} <= 7X/w_{i+1}.

  Correct.
* **Per-index error.** R_i w_i <= 7X w_i/w_{i+1} <= 7X/Q for i < m, and w_m <= X/Q for i = m. Correct.
* **Telescoping.** The identity prod h - prod c = sum_i (prod_{j<i} c_j)(h_i - c_i)(prod_{j>i} h_j) holds; I checked that the sum telescopes. With 0 <= c_j <= 1 it gives |C - X prod c| <= (7(m-1)+1)X/Q <= 7mX/Q. Correct.
* **Last step.** 0 <= c_i - 1/2 <= 1/(2w_i) <= 1/(2Q), and with factors in [0,1] this gives 0 <= prod c - 2^{-m} <= m/(2Q). The total is (7 + 1/2)mX/Q <= 8mX/Q. Correct.

**Numerical test (not a proof step).** I brute-forced 2932 random instances with Q in {2, 2.5, 3, 4, 7, 10}, m <= 4, moduli generated to satisfy the hypotheses, and X up to about 3e6. The condition was implemented exactly as 2(n mod w) < w. The bound held in every case; the largest ratio of error to bound was 0.084.

## (2) The hypotheses where the lemma is applied (lines 340–376)

* **Kummer form.** The i-th Legendre summand floor(2n/p^i) - 2 floor(n/p^i) equals floor(2(n mod p^i)/p^i), which lies in {0,1} and is 1 exactly when n mod p^i >= p^i/2. So p ∤ B_n holds iff n mod p^i < p^i/2 for every i. Correct.
* **Single prime in a trimmed band.** Take X >= 2^{1/eps}, so Q = X^eps >= 2.
  - p > X^{1/(r+1)+eps} gives p^{r+1} > X Q^{r+1} >= 4X. For n <= X every condition with i >= r+1 then holds automatically, since n mod p^i = n < p^i/2.
  - The remaining moduli are p, ..., p^r. The smallest is p > X^a > X^eps = Q (because eps < a/4), consecutive ratios equal p > Q, and X/p^r > X^{r eps} >= Q (from p < X^{1/r-eps}).
  - Deleting the p-1 integers n < p costs p/X <= X^{b-1}.

  So eq:uniform1 holds with error 8rX^{-eps} + p/X <= 8LX^{-eps} + X^{b-1}. Correct.
* **Bands met.** Retained primes have exponent > a >= 2/L. So the bands met have r < 1/a <= L/2, and every band edge 1/(r+1) with r+1 <= L is among the removed points 1/j (j <= L). Retained means distance > eps from each 1/j, which matches the strict trimmed-band inequalities. Correct.
* **Pairs under (5).**
  - The merged moduli p^i, q^j are distinct by unique factorization, and the smallest exceeds Q.
  - With x = X, (5) gives w_{i+1}/w_i > Q and X/w_{r+t} > Q; this includes same-prime neighbours, whose ratio is p > Q.
  - The higher powers are automatic for both primes, and gcd(pq, B_n) = 1 iff both p ∤ B_n and q ∤ B_n.
  - m = r+t <= 2L, and deleting n < max(p,q) costs at most X^{b-1}.

  So eq:uniform2 holds with error <= 16LX^{-eps} + X^{b-1}. Correct.
* **Onset (lines 403–408).** If X > max{2^{1/eps}, (32L/z)^{1/eps}, (2/z)^{1/(1-b)}}, then 16LX^{-eps} < z/2 and X^{b-1} < z/2, so e_1, e_2 < z. Correct and explicit.

## (3) The error terms used in lem:local

* **Definitions.** e_1 and e_2 (lines 391–402) are defined as maxima over the trimmed bands and are bounded only by eq:uniform1 and eq:uniform2.
* **Where they enter.** The first moment (eq:meanerror) uses e_1 (line 459). The second moment (eq:second, eq:variance) uses e_2 for exactly "the retained pairs satisfying (5)" (line 499). Pairs violating (5) and pairs containing removed primes are handled by the reciprocal-mass bounds eq:badpairs and eq:removed, without any count estimate.
* **What remains of the quotations.** The quoted EGRS displays on p. 86 and p. 88 (lines 253–276) are now reproduced as printed. The text says explicitly that neither prints uniformity and that their o(x) terms are not used as uniform remainders. That matches the page images I checked in round 2.
* **What is still imported.** The only imported moment input left is the full first moment, EGRS Theorem 2 (eq:inputmean). It is used only in the small-prime section, and the text labels it the only qualitative remainder. Nothing depends on EGRS statement (1).
* **Harmless redundancy.** The term (e_1 + X^{b-1}) in m_X, and (e_2 + X^{b-1}) in eq:second, count the deletion of n < p twice: e_1 and e_2 already include p/X. This only makes the bound more conservative; no change is needed.

## (4) Program-scope wording

* Lines 172–174 (Remark rem:scope) read: "This is a claim about the construction in Section sec:numerics; the supplied program implements alpha=1/s for integers s>=2." Fixed.
* Lines 769–771 read: "The program as shipped implements alpha=1/s for integers s>=2; the construction extends to any rational 0<alpha<=1/2 by clipping the top band at alpha." Fixed.
* The abstract (line 40) now reads "We prove the uniform prime counts needed for the localized moment calculation", which matches the text.

## Not checked in this round

* Material outside the edit, which was confirmed in round 2 and not re-reviewed, as instructed.
* The compiled 17-page PDF was not compared with `main.tex` in this round.
* The `code/` directory, which is outside my permitted files.
