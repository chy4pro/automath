PASS-WITH-REPAIRS

# Referee report (referee-2): Erdős #86, PROBE_ASTRA_4_20261009.md, round 4

Reviewed file: `problems/erdos86/PROBE_ASTRA_4_20261009.md` (Astra clean-room probe, 390 lines). I read only that file and the task brief. I used no web or literature.

**Bottom line.** Every statement the report labels as proved is correct. I re-derived each one by hand. All finite claims reproduce exactly under my own, independent Python code, and also when I run the report's Appendix A/B/C scripts verbatim. The mathematics needs no repair.

One repair is mandatory, and it concerns the STATUS label. The report proves π₄ ≤ 4^(−1/3) ≈ 0.62996 and π₄ ≤ r ≈ 0.62582. Both are weaker than both bounds quoted in the brief (0.6068 and 0.60318). Nothing is proved toward c < 0.60318. The honest status is therefore **OPEN**, with an exact relaxation obstruction, not PARTIAL. The body of the report is candid about this. The label and the first sentence of the status line are not.

A side finding sharpens the report's own negative result. The 5/8 mixture is correct, but it understates the obstruction. I give an exact rational witness showing that the Q₄-degree-histogram relaxation cannot rule out p = 0.6258168. So r itself is, to within 2·10⁻⁹, the exact optimum of that relaxation (§3.6 below).

---

## 1. Claim-by-claim verdicts

| Report location | Claim | Verdict | How checked |
|---|---|---|---|
| Preamble | Spanning subgraphs; isolated vertices counted; e(Q_n)=n2^(n−1); p=e(G)/(n2^(n−1)) | Consistent throughout | All expectations are over all 2^n vertices, and n₀ is included in (3) and (8). No silent change of convention found. |
| §1 face averaging | 2^(n−k)·C(n,k) k-faces; each edge lies in C(n−1,k−1) of them; mean face density = p; a_n is nonincreasing; π₄ exists | Correct | Re-derived: e·C(n−1,k−1)/(2^(n−k)C(n,k)·k2^(k−1)) = p. |
| §1 full vertices in Q₃ | At most one full vertex per parity class, so at most 2 | Correct | Two full vertices at distance 2 span a C₄ through their two common neighbours. Exhaustive Q₃ check: max #deg-3 vertices = 2. |
| §1 count | Σ_v C(d,3) ≤ 2·2^(n−3)C(n,3) ⇒ E(d)₃ ≤ (n)₃/4 (n ≥ 3) | Correct | Re-derived the constant: 6·2·2^(n−3)C(n,3)/2^n = (n)₃/4. Random-graph tests below. |
| §1 Jensen | (d)₃ ≥ ((d−2)₊)³; the function is convex; ((np−2)₊)³ ≤ (n)₃/4 ⇒ p ≤ 2/n + 4^(−1/3) | Correct | The convexity is that of t³ (nondecreasing, convex on [0,∞)) composed with (x−2)₊. Mean degree = np. Checked (d)₃ ≥ ((d−2)₊)³ for d < 10⁴. 4^(−1/3) = 0.629960524947… confirmed. |
| §2 (1)⇔(2)⇔(3) | n₁+n₂ ≥ 3n₄ ⇔ T₂+T₄ ≤ 2e ⇔ T₃+n₀ ≤ 16 | Correct | C(i,2)+C(i,4)−i = 0,−1,−1,0,3 for i=0..4. T₃ = n₃+4n₄. |
| §2 full vertices in Q₄ | At most 2 per parity class (must be antipodal), so at most 4 | Correct | Exhaustive: max n₄ over all C₄-free Q₄ = 4. |
| §2 certificate partition | With 0000 full: 3⁶·2¹⁶ = 47,775,744 candidates. Each C₄-free graph with 0000 full occurs exactly once. f = 0 is trivial. Translation reduces f ≥ 1 to this case. | Correct and complete | Re-derived: 4 root edges, 12 level-1/2 edges (pairs at each weight-2 vertex, at most one per pair), and 12+4 = 16 free edges. Translation is an automorphism that preserves degrees and C₄-freeness. |
| §2 "every 4-cycle is a coordinate square" | Standard | Correct | — |
| §2 table | f = 1,2,3,4 → 19,975,328 / 4,877,691 / 147,744 / 1,296 valid; min n₁+n₂ = 4/6/9/12; total 25,002,059; 0 violations | **Exactly reproduced** by two independent methods | §3.2–3.3 below |
| §3 identity | E_F Σ_{v∈F} C(d_F(v),k) = 16·C(4,k)·q_k | Correct | Re-derived via Σ_D C(\|S∩D\|,k) = C(d,k)C(n−k,4−k) and C(n−k,4−k)/C(n,4) = C(4,k)/C(n,k). Checked with exact rationals over all 4-faces of random C₄-free graphs, n = 4..7, k = 0..4. |
| §3 (4) | 6q₂+q₄ ≤ 4p | Correct | 96q₂+16q₄ ≤ 2·32p. |
| §3 (5) | (d)_k/(n)_k ≥ (d/n)^k − C(k,2)/n | Correct | Mixture/union-bound argument re-derived. Exhaustive exact check for 2 ≤ k ≤ 5, k ≤ n ≤ 60, 0 ≤ d ≤ n: no failure. |
| §3 (6) | p⁴+6p²−4p ≤ 12/n | Correct | Error terms 6·(1/n)+6/n = 12/n. Jensen for t² and t⁴. |
| §3 (7) | p ≤ r+3/n for every n ≥ 4; π₄ ≤ r | Correct | g′(r) = 4r³+12r−4 = 12(1−r) (using r³ = 4−6r), which is > 4 since r < 2/3. g is convex, so g(p) ≥ 4(p−r) for p ≥ r. Onset n ≥ 4 is the right one (4-faces exist). |
| §3 cubic and bracket | r = 0.625816818958…; numerators −3348659416260042279926088 and +3826280656413965615148079; (5/8)³+6(5/8)−4 = −3/512 | **Exactly reproduced** | Python big integers. mpmath (40 digits): r = 0.6258168189584667160118889… |
| §4.1 | T₃ < 16 is false; all 8 extremal 24-edge graphs are cubic; max T₃ = 16 for f ∈ {0,2,3,4} and 15 for f = 1 | Correct | Exhaustive: the 24-edge histogram is (0,0,0,16,0) with multiplicity 8. Max T₃ per f = 16,15,16,16,16. |
| §4.2 mixture | Five (a,b,V) graphs are C₄-free with the stated histograms/profiles; weights 132,30,43,157,150 sum to 512; weighted histogram = 16·Bin(4,5/8) | **Exactly reproduced** | Decoded with the stated edge order (which matches the code's order) and checked against all 24 squares. E(e,T₂,T₃,T₄) = (20, 75/2, 125/8, 625/256) confirmed. |
| §4.2 conclusion | The degree-histogram + one-vertex-moment relaxation cannot rule out 5/8 | Correct, but **not sharp** and only stated in limit form | See §2 R2 and §3.6. The true optimum of that relaxation is r (to 2·10⁻⁹). |
| §4.3 (8) | 2T₃+5n₀+n₁ ≤ 160 for C₄-free Q₅ | Correct | Each triple lies in 2 of the 10 4-faces. Isolation multiplicities 5/1/0 re-derived, as is d·C(d−1,3)+(5−d)·C(d,3) = 2C(d,3). Tested on 30 random maximal C₄-free Q₅ graphs. |
| §4.3 substitution | Binomial substitution of (8) gives p⁴+6p²−4p ≤ 0 | Correct (heuristic, presented as such) | Algebra re-done. |
| §4.3 Q₅ full vertices | At most 4; q₅ ≤ 1/8; p⁵ ≤ 1/8+10/n | Correct | (1/8)^(1/5) = 0.65975 > 4^(−1/3), as stated. |
| §4.4 two-path count | Σ C(d,2) ≤ 2^(n−1)C(n,2), q₂ ≤ 1/2, p² ≤ 1/2+1/n | Correct | Random tests. |
| §4.4 neighbour-degree count | Σ_{y∼x} d(y) ≤ nd − C(d,2); 3Σd² ≤ (2n+1)Σd; p ≤ 2/3+1/(3n) | Correct | Re-derived. Random tests. |
| §4.4 failed hand proof | Explicitly not claimed | Honest | — |
| §5.1 compression | The example becomes a square under OR/AND compression | Correct | I implemented the OR/AND rule myself. Result: (0,1),(0,2),(1,3),(2,3), one square. |
| §5.2 entropy | Shearer with multiplicity n−1; Gibbs bound with P(λ) = 1+4λ+6λ²+4λ³; result p ≤ 3/4 (trivial); H(Z) ≤ n+log₂ n! | Correct; the conclusion is trivial, and the report says so | — |
| §5.3 | Symmetrised root bits of the 5/8 mixture are exactly i.i.d. Bernoulli(5/8) | **Exactly reproduced** | Exact rational law over 5 graphs × 16 roots × 24 permutations. |
| §6 items 1–2 | Q₃: 2902 graphs, edge counts 1,12,66,220,489,744,756,468,138,8; 35 histograms; ex = 9. Q₄: 1,226,436,381 graphs, 828 profiles, the stated edge-count vector; ex = 24 | **Exactly reproduced** | §3.1 below |

## 2. Errors, gaps and required repairs

There are no mathematical errors, no circularity, and no hypothesis used before it is available. The repairs:

- **R1 (mandatory, STATUS line, line 1).** Replace `PARTIAL` with `OPEN`. Then add to the status line, verbatim or equivalent: "both bounds (4^(−1/3) ≈ 0.62996 and r ≈ 0.62582) are weaker than the known 0.6068 and 0.60318; nothing is proved toward c < 0.60318." Reason: under the pipeline's definitions, a bound weaker than the brief's known bounds is not progress toward the target. The surviving content is a relaxation-specific obstruction, which is exactly the "honest OPEN with the exact obstruction" case. As written, "strengthens this to π₄ ≤ r" reads like progress unless the reader already knows the brief's bounds. The body itself is not misleading: the Scope section says the report "does not improve either numerical bound", and §3 says "The target was therefore not reached".

- **R2 (recommended, §4.2 and §5.3 conclusion).**
  - (a) State that the obstruction concerns the *limiting* relaxation: the vertex-degree law μ on [0,1], and the averaged 4-face histogram E_μ[16·Bin(4,T)] lying in conv{C₄-free Q₄ histograms}. At finite n the averaged histogram is a hypergeometric mixture, so the statement there is asymptotic.
  - (b) Sharpen "cannot rule out 5/8" to "cannot rule out any p ≤ 0.6258168; hence r is (to within 2·10⁻⁹) the exact optimum of this relaxation, and inequality (1) is its only binding constraint". An exact witness is given in §3.6. The report's sentence is true as written; it just undersells the result, and the sharp form is the more useful negative statement. The same applies to §5.3: the i.i.d. root law is realisable by an exact mixture at p = 0.6258168, not only at 5/8.

- **R3 (cosmetic, Appendix C).** The compression check computes `after = before.map(([a,b])=>[a&3,b&3])`, which projects every edge to the lower layer. That is not the OR/AND rule stated in §5.1. It gives the same result here only because no corresponding lower/upper pair has both edges present. My own OR/AND implementation confirms the §5.1 conclusion.

- **R4 (cosmetic, §5.2).** "The resulting optimized bound is exactly p ≤ 3/4" means the infimum over λ > 1, which is approached as λ → ∞ and not attained. The conclusion p ≤ 3/4 is still correct.

## 3. Independent re-checks actually run

All of these ran in Python (numpy/mpmath, exact `fractions`/big integers where stated) in my own scratch space. Total CPU was about 40 s, plus about 19 s for the report's own JavaScript. No SAT/ILP solver was used. One plain LP (scipy `linprog`, no integrality) was used only to locate the support in §3.6; the conclusion there is then verified in exact rational arithmetic.

1. **Q₃ exhaustive (own code).** 4096 edge subsets → 2902 C₄-free. Edge-count vector [1,12,66,220,489,744,756,468,138,8,0,0,0]. 35 degree histograms. Max #deg-3 vertices = 2. ex(Q₃,C₄) = 9. *Exact agreement.*

2. **Q₄ exhaustive, all ordered layer pairs (own code, a different decomposition from the report's).** For every ordered pair (a,b) of the 2902 C₄-free Q₃ layers (no a ≤ b symmetry trick), and every V ⊆ {0..7} independent in the graph a∧b, I encoded the full degree histogram as Σ_v 17^{deg v} and accumulated counts. Results:
   - 1,226,436,381 graphs; 828 distinct histograms.
   - Edge-count vector identical to §6 item 2 (…, 7552, 192, 8, then zeros from 25 to 32).
   - (1) holds for all 828 histograms, with 0 violations. max(T₃+n₀) = 16 and max(T₂+T₄−2e) = 0, so (1)–(3) hold for every C₄-free Q₄ graph, not only for those with a full vertex.
   - 14 histograms with n₄ > 0 attain equality in (1).
   - Sanity checks: 4-edge count 35936 = C(32,4) − 24.

3. **Cross-check of the §2 table by vertex-transitivity (independent of any rooted enumeration).** Let N_f be the number of C₄-free Q₄ graphs with exactly f full vertices. Then the number with 0000 full and f full vertices in total is f·N_f/16. From item 2: N_1..N_4 = 319,605,248 / 39,021,528 / 787,968 / 5,184, which gives 19,975,328 / 4,877,691 / 147,744 / 1,296. Min n₁+n₂ per f = 4/6/9/12. *Exact agreement with the table.*

4. **Direct rooted enumeration (own vectorised code).** Over all 2¹² level-1/2 patterns, the 729 square-free ones (as expected) × 2¹⁶ free edges give exactly 47,775,744 candidates. Of these, 25,002,059 are valid, with the per-f counts above, min n₁+n₂ = 4/6/9/12, and 0 violations. *Exact agreement.*

5. **The report's own scripts, verbatim (node, single-threaded).**
   - Appendix A reproduces its JSON: 47,775,744 attempts, 25,002,059 valid, 0 violations, about 3.85 s CPU.
   - Appendix B reproduces the counts and the 828 profiles. Its profile set equals mine exactly as a set of (e,T₂,T₃,T₄). About 14.6 s CPU.
   - Appendix C reproduces the witness, bracket and compression outputs.

6. **Relaxation optimum (new; sharpens §4.2).**
   - The limiting relaxation is: maximise E_μT subject to E_μ[16·Bin(4,T)] ∈ conv(H₈₂₈). The LP on a 4001-point grid gives 0.6258167962, with μ supported on the two grid points adjacent to r.
   - **Exact rational witness.** For p\* = 782271/1250000 = 0.6258168, the vector 16·Bin(4,p\*) equals, exactly, the convex combination of the histograms below. All weights are positive and all five coordinates match in exact arithmetic.

     | Histogram (n₀,…,n₄) | Weight |
     |---|---|
     | (0,2,4,8,2) | 2735855342520231975626709/3814697265625000000000000 |
     | (0,2,10,0,4) | 846629975337811444258101/3814697265625000000000000 |
     | (1,5,4,3,3) | 41980879946792739261519/953674316406250000000000 |
     | (11,4,0,0,1) | 207830248048011519/152587890625000000000000 |
     | (16,0,0,0,0) | 64283232223584422781139/3814697265625000000000000 |

   - Exact witnesses also exist at p = 0.6258, 0.62581 and 0.625816. A second exact 5/8 mixture, different from the report's, uses weights 25/768, 133/192, 7/32, 23/768, 5/192 on histograms (0,1,6,7,2), (0,2,4,8,2), (0,2,10,0,4), (1,5,4,3,3), (11,4,0,0,1).
   - The report's own §3 argument applies inside this relaxation, giving an upper bound of r. So the relaxation optimum lies in [0.6258168, 0.6258168190]. The certificate (1) already extracts everything that Q₄ degree histograms plus one-vertex degree laws can give.

7. **Random C₄-free graphs.** I tested random greedy maximal C₄-free subgraphs of Q_n, half with a level-biased edge order, for n = 4..8 (30 each for n ≤ 7, 8 for n = 8). Each was checked to be C₄-free. In exact arithmetic I tested:
   - the §1 count;
   - the two-path count;
   - 3Σd² ≤ (2n+1)Σd;
   - the §3 face identity for k = 0..4 (summing over every 4-face, n ≤ 7);
   - (1) on every 4-face;
   - (4), (6a) and (6);
   - (7);
   - (8) and "at most 4 full vertices" for n = 5.

   All held. I also checked (5) exhaustively as described in §1 of this report.

8. **Mixture and §5.3.** The five witnesses have 0 squares and the stated histograms and profiles. The weights sum to 512, and the weighted histogram is (162,1080,2700,3000,1250) = 512·16·Bin(4,5/8). The symmetrised root law is exactly (5/8)^|S|(3/8)^(4−|S|).

9. **Cubic.** The bracket numerators match to the digit. (5/8)³+6(5/8)−4 = −3/512. (2/3)³+6(2/3)−4 = 8/27 > 0. g′(r) = 12(1−r) = 4.4902 > 4.

## 4. Honest status

The honest status is **OPEN**.

- Both proved bounds (0.62996 and 0.62582) lie above both bounds in the brief (0.6068 and 0.60318), so nothing is proved toward c < 0.60318.
- The Section 1 argument is a standard full-vertex/Jensen count.
- The new ingredient is an exhaustively certified Q₄ degree inequality, and §3.6 shows that it saturates its own relaxation.
- The negative result is a genuine but relaxation-specific obstruction: Q₄ histograms plus one-vertex degree law. The report correctly says it is not a general obstruction, and nothing conditional is presented as unconditional.
- HIT is not justified.

The only dressing-up is the word PARTIAL, together with the status line not saying that r is weaker than the known bounds (R1).

## 5. Value

**Usable.** The cleanly certified lemma "every C₄-free H ⊆ Q₄ satisfies n₁+n₂ ≥ 3n₄ (equivalently T₃+n₀ ≤ 16)", with the explicit, onset-exact averaging to π₄ ≤ r + 3/n for n ≥ 4. Also usable is the sharpened negative result: no inequality on Q₄ degree histograms, combined with any one-vertex degree distribution, can prove anything below r ≈ 0.62582. That rules out this route even to the brief's elementary 0.6068.

**Remaining obstruction.** Any proof below r, and a fortiori below 0.60318, must use correlations between different roots or overlapping faces (for example, joint constraints on adjacent vertices' incident-direction patterns, or coloured/rooted Q₄–Q₅ configurations of flag-algebra type). The report has none, and §5.1–5.2 confirm that its compression and entropy attempts do not provide them.

## 6. What I could not check

- The CPU-time table and the "interrupted-run" provenance. My timings for Appendices A and B (3.85 s and 14.6 s) are consistent with the reported ones.
- The exploratory floating-point weight search (§6 item 6). Not needed: the final weights were verified exactly.
- ex(Q₅,C₄) = 56. Neither the report nor I verified it. It is used only in non-claimed remarks (§4.3 first paragraph and the end of §5.2).
- The literature attribution of 0.6068 in the brief, which does not affect this review. From memory (not checked), Chung's 1992 elementary bound was about 0.623 and 0.6068 is due to Thomason–Wagner. Either way, both of the report's bounds lie above the brief's numbers.
