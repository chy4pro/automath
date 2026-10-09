PASS-WITH-REPAIRS

# Referee report: PROBE_ASTRA_5_20261009.md (Erdős #241, T4, round 4)

Reviewer: referee-1 (independent, clean room). Files read: the probe report only, plus the task brief. No web, no papers, no other files under the project tree.

Verdict in one line: every statement the report labels as proved is correct and I re-derived each one by hand and by exhaustive/explicit computation (zero discrepancies); but nothing proved is progress toward the target, so the honest STATUS label is OPEN, not PARTIAL. The repairs are to the status line and to two presentational points; no mathematical repair is needed.

## 1. Claim-by-claim verdicts

Notation as in the report (ordered-tuple counts p, r, d, C with repetition; S = A+A-A; T = {2a-b : a != b}; D = A-A; H, B, w_L, W_L, V_L, U_L, theta_L).

| Item | Statement | Verdict | How re-derived |
|---|---|---|---|
| §2.1 | B_3 => B_2 (m>0); d(0)=m, d(h) in {0,1} for h != 0 | correct | multiset cancellation of an appended element; {a,e}={c,b} has only the two listed resolutions |
| §2.1 | noncancelling representations (unordered positive pair, c not in {a,b}) are unique | correct | a+b+c' = a'+b'+c, c lies in the left multiset, c != a,b forces c=c', then cancel |
| §2.1 | r(x) = 2m-1 on A; every representation of x in A cancels | correct | B_2 gives {a,b}={c,x}; count 2(m-1)+1 |
| §2.1 | T disjoint from A, |T| = m(m-1), r=1 on T, r=2 on S \ (A u T) | correct | uniqueness above; 2a-b in A would be a cancelling representation of an element of A with c not in {a,b} |
| (3) | |S| = m + m^2(m-1)/2, valid for all m >= 0 | correct | binom(m,2)(m-2) + m(m-1) = m^2(m-1)/2; checked m=0,1,2 by hand, all 2089 sets by code |
| (4) | r = 2·1_S + (2m-3)·1_A - 1_T pointwise | correct | the four cases give 2m-1, 1, 2, 0; m=0,1 checked separately |
| (5),(6) | sum r^k = m(2m-1)^k + 2^k m(m-1)(m-2)/2 + m(m-1); k=2 gives 6m^3-9m^2+4m | correct | sum of powers over the four value classes; expansion for k=2 verified |
| (1) | C(h) = 2m - 2H(h) + (2m-3)d(h) - B(h) for every h | correct | C(h) = sum_a r(a+h) (sum (4) over x = a+h); #{a: a+h in A} = d(h); B(0)=0 since T∩A = ∅ |
| (7) | C(0) = 2m^2 - m | correct | ordered pairs with equal sum, B_2; also (1) at h=0 |
| (8) | C(h) = 4m-4 on D \ {0}; hence H=0, B=1 there | correct | {a,b,v}={c,e,u} with u != v forces {a,b}={u,z}, {c,e}={v,z}; count 4(m-2)+2+2 |
| (9) | C(h) = 2m - 2H - B <= 2m off D | correct | (1) with d(h)=0 |
| §3 matching | off D the positive pairs (and separately the negative pairs) of the representations sum P - sum Q = h form matchings on their supports; P, Q disjoint | correct | {b} ⊎ Q' = {b'} ⊎ Q by B_3 (3-element multisets, so B_3 suffices), b not in Q; disjointness since a shared element would put h in D. The report correctly notes this does not forbid a positive endpoint of one representation being a negative endpoint of another |
| (10) | sum q_L^2 >= m^4 L^2/(2N+L-2) | correct | supp q_L ⊆ [2, 2N+L-1]; Cauchy–Schwarz |
| (11) | sum q_L^2 = sum_h w_L(h) C(h) = 2mL^2 - 2W_L + (2m-3)V_L - U_L | correct | #{(j,k) in [0,L)^2: j-k=h} = w_L(h); sum_n p(n)p(n+h) = C(-h) = C(h); substitute (1) |
| (12),(13) | V_L <= L m^2, U_L >= 0; (13) for m >= 2 | correct | 2m-3 >= 0 is exactly what is needed to drop V_L upward; the m >= 2 restriction is stated |
| (14),(15) | m^3 - m^2 + 2m <= 6N-4; m^2 <= 5N^{2/3} for all N >= 1 | correct | m >= 3: m-1 >= 2m/3; 9^{2/3} = 4.327 < 5; m <= 2 trivial |
| (16),(17),(18),(2) | L = ceil(N^{5/6}); m^3 <= 4(1-theta_L)N + 32N^{5/6} for m >= 2; m^3 <= 4N + 32N^{5/6} for all m, all N >= 1 | correct, constants exact | (2N+N^{5/6})(2(1-θ)+10N^{-1/6}) = 4(1-θ)N + (2(1-θ)+20)N^{5/6} + 10N^{2/3} <= 4(1-θ)N + 32N^{5/6}; both factors nonnegative as stated |
| (19)–(21) | G_N = 3N-2-m-m^2(m-1)/2 >= N - 16N^{5/6} - 3; liminf of global hole fraction >= 1/3 | correct but weak (see R2) | m^2/2 - m >= -1/2; substitution of (18) |
| §5.1 example | an arbitrary set S̃ ⊇ [1,N] of any cardinality in [N,3N-2] gives weighted hole fraction 0 | correct as stated, clearly flagged as a relaxation | trivial |
| (22) | sum_a a (r(a-h) - r(a+h)) = h C(h)/2 for every h | correct | sum over quadruples of the first positive coordinate is sum_u u r(u-h); of the first negative coordinate is sum_s s r(s+h); symmetrize |
| (23),(24) | off D: r(a±h) in {0,1,2}; Δ_h = 2m - C(h) = 2H + B; C(h) <= 4m(N-1)/(2(N-1)+|h|) | correct | a±h not in A off D; 1 <= a <= N gives h C/2 <= (N-1)Δ |
| (25)–(27) | sum_h B(h) = m|T|; U_L <= L m^2(m-1); U_L/(mL^2) <= 5N^{-1/6}; the lower bound from (24) for |h| < L is at most (L-1)/(2(N-1)) | correct | direct |
| §6 (28),(29) | 1.5154^3 = 3.480020872264; θ_* = 64997390967/500000000000; onset (3200000)^6 = 1.073741824·10^39; conditional constant^3 = 3.48001 < 1.5154^3 | arithmetic exact; conditional statement correctly quantified and labelled | exact rational arithmetic (below) |
| §7 route 6 | E_4 >= m^8/(4N-3); E_4 <= 2m^5 + 12m^4 - 40m^3 + 43m^2 - 16m | correct | upper bound is 2m·sum_h C(h) + sum_{h in D} C(h)(C(h)-2m); expansion verified |
| §8 counts | 2089 sets; sizes 1/20/190/936/942; cumulative list; 150,665 / 12,534 / 10,430 / 51,176 / 10,333 / 2,088 comparisons | all reproduced exactly | independent Python enumeration |

Quantifiers, onsets, conventions: consistent throughout. Ordered tuples with repetition are used everywhere for p, r, d, C, and the "unordered positive pair" convention in §2.1 is used only for the uniqueness argument and then converted back to ordered counts correctly (factor 2 vs 1). The B_3 definition is the multiset one and matches the brief. The m >= 2 restriction for (2)/(13) and the m = 0,1 separate treatment for (18) are both explicit. No circularity: the dependency order stated in §9 is the actual one. No lemma is silently assumed; the only external input is nothing (the 1.5154 value is used only as a numerical threshold in §6).

Errors found: none in any proved statement.

## 2. Repairs (presentation and status; no proof step changes)

R1 (status line, line 1). Replace PARTIAL by OPEN. Reason: every proved statement is either a standard elementary consequence of B_3 (the exact representation counts, |A+A-A|, (1), (7)–(9), (22)) or the bound m^3 <= 4N + 32N^{5/6}, whose constant 4^{1/3} = 1.5874 is strictly weaker than the brief's known 1.5154. The only target-directed content is the conditional reduction in §6, which rests on an unproved hypothesis. Nothing is dressed up: the report itself says the improvement remains OPEN and the bound is weaker. But by the pipeline's own convention (an honest OPEN with the exact obstruction is a valid outcome) the label should be OPEN. Suggested wording: "OPEN — exact B_3 representation identities and a smoothing bound |A|^3 <= 4N + 32N^{5/6} (constant 4^{1/3}, weaker than the known 1.5154); strict improvement reduced to an unproved uniform weighted-hole hypothesis theta_L >= 13/100."

R2 (§5.1, lines 276–290). State that the global hole bound (20)–(21) is dominated by what the brief's known bound already gives: inserting m^3 <= 3.4801N into the exact (19) yields G_N/(3N-2) >= 1 - 1.74005/3 - o(1) = 0.42 - o(1), versus the report's 1/3. So (21) is not a result on seed (a) beyond known facts, and the report should say so instead of "a substantial global hole fraction".

R3 (§1 and §6, the unproved assertion). Add that the hypothesis theta_L >= 13/100 is not provable by any density-type argument, and that none of the tools in the report (cardinalities, one-point moments, the first-moment balance (22)–(24), the relaxation-insensitive parts of §3) can therefore establish it. Referee's reasoning (my own, not in the report): in the continuous relaxation behind the known bound, the pointwise cap C(h) <= 2m becomes a sup-norm cap on the autocorrelation of f*f; an autocorrelation attains its sup at h = 0, so for the relaxed extremal the cap binds at h = 0 and the smoothed quantity at scale L = o(N) sits at the cap, i.e. theta_L -> 0. Thus the hypothesis is genuinely a realizability statement (which is what the brief asks for), and the §5.1 artificial-set example understates the obstruction: it is not merely "scalar information is insufficient" but "all density information is insufficient". The report should also say that the small-N instances do fail (see §3 below), so N_* cannot be small.

R4 (§6, threshold). Note that the threshold 13/100 is an artifact of using plain Cauchy–Schwarz in (10). If (10) is replaced by the known L^2 autoconvolution inequality underlying the brief's bound (constant 4/1.5154^3 = 1.1494 relative to Cauchy–Schwarz), then any uniform theta_0 > 0 at a scale N^{2/3} << L << N (for the corresponding kernel) would already give constant (3.4801(1-theta_0))^{1/3} < 1.5154. The reduction is therefore stronger than stated, and the honest open problem is "any fixed positive weighted hole fraction near A", not "at least 13%". (Referee's observation; it relies on the brief's known bound, which the clean-room report did not use.)

## 3. Independent re-checks actually run

All with python3 (numpy/scipy not needed), integer arithmetic throughout, total under 5 CPU-seconds, no SAT/ILP.

Exhaustive run over all 2^20 subsets of {1,...,20} (B_3 tested on multiset triple sums i <= j <= k):
- 2089 B_3 sets incl. empty; by size 1, 20, 190, 936, 942; no set of size 5; first size-4 set in lexicographic mask order {1,2,8,12}. Cumulative counts for N = 1..20: 2, 4, 7, 11, 18, 30, 45, 67, 96, 132, 177, 237, 314, 420, 559, 737, 968, 1270, 1631, 2089. All identical to §8.1.
- For every set with N = max(A) (N = 1 for the empty set): (3), |T| = m(m-1), T ∩ A = ∅, (4) on [2-N-3, 2N+3], (5) for k = 1..6, (6), (19); for every h in [-2N-2, 2N+2]: (1), C(h) = sum_a r(a+h), (7), (8) with H = 0, B = 1, d = 1 on D\{0}, (9) off D, (22), and the cross-multiplied forms of both inequalities in (24) off D (N > 1), and r(a±h) in {0,1,2} off D; sum_h B(h) = m|T|. Counts: 150,665 shift comparisons, 150,665 first-moment checks, 12,534 moment comparisons — identical to §8.1.
- Matching claim of §3: for every h off D, all pairs (P,Q) of unordered 2-multisets with sum P - sum Q = h were listed (51,176 representations in total, identical to §8.1); P ∩ Q = ∅ always, and no two representations share a positive endpoint or share a negative endpoint. Zero violations.
- Smoothing for L in {1, 2, ceil(N/2), N, 2N+1}: direct q_L, sum q_L = Lm^2, support inside [2, 2N+L-1], (11) both equalities, (10), (12), and the cleared form m^4L^2 <= (2N+L-2)(2mL^2 - 2W_L + (2m-3)m^2L) for m >= 2. Counts 10,430 and 10,333 — identical to §8.1/8.4.
- (14), (15) (as m^6 <= 125N^2), (18) (as (m^3-4N)^6 <= 32^6 N^5 when m^3 > 4N), and both E_4 bounds of route 6 on all 2,088 nonempty sets. Zero failures.

Explicit sets of §8.2 (P_m, Q_m = 5P_m+3, reflected Q_m, m = 1..12, largest N = 20,971,523): B_3 verified directly; (3), |T|, (4) on S and two outside points, (5) for k = 1..10, (1), (7)–(9), (22), (24) on supp C ∪ {±(2N+1)}, and the smoothing identities/inequalities at L in {1, 2, ceil(N^{5/6}) (exact integer ceiling via L^6 >= N^5), N, 2N+1}, with W_L computed as mL^2 - sum_{a,s} w_L(s-a). All pass. Sample values of theta_L at L = ceil(N^{5/6}): P_4 (N=64, m=4): 0.7915; P_12 (N=4,194,304): 0.9992; Q_12: 0.9998 (these sets are extremely sparse, so theta near 1 is expected and uninformative).

§6 arithmetic in exact rationals: 1.5154^3 = 435002609033/125000000000 = 3.480020872264 (numerator over 10^12 is 3,480,020,872,264); θ_* = 64997390967/500000000000 = 0.129994781934; 4(1-13/100) = 87/25; (3200000)^6 = 1073741824000000000000000000000000000000; 32·N^{-1/6} = 1/100000 exactly at that N; 348001/100000 < 1.5154^3 and 27/8 < 348001/100000; (3.48001)^{1/3} = 1.515398...; 4^{1/3} = 1.587401...; 9^{2/3} = 4.3267 < 5. All as reported.

Additional diagnostics (not in the report; not evidence for or against the hypothesis at large N):
- Bose–Chowla B_3 sets mod q^3-1 for q = 7, 11, 13, 17, 19, 23, 29, 31, shifted into {1,...,q^3-1} (B_3 verified directly): m^3/N between 1.005 and 1.17; theta_L at L = ceil(N^{5/6}) between 0.66 and 0.75; global hole fraction 0.82–0.84. These are at density 1, far below the (3/2)N^{1/3} regime, where holes are abundant, so they say nothing about the hypothesis.
- Among the 475 B_3 subsets of {1,...,20} with m >= (3/2)N^{1/3}, theta_L ranges from 0 ({1,2}, N=2) and 0.04 ({2,3,6}, N=6) up to 0.4537 ({1,7,8}). So the hypothesis of §1 is false without an onset; it is stated with an onset N_*, so this is not a counterexample, but any future proof must have N_* > 20 at least.

## 4. Honest status

The proof content passes. The status label should be OPEN. Nothing is a HIT: no statement in the report improves on, or even reaches, the known constant, and the §6 conclusion is explicitly conditional with the condition unproved. Nothing is presented as unconditional that is conditional; the §5.1 obstruction is correctly labelled as a relaxation. The one mild dressing-up is the description of (21) as "a substantial global hole fraction" when it is weaker than what the known bound already implies (R2).

## 5. Value

Usable lemmas: the exact identities (1), (4), (5), (7)–(8), (22) and the exact |A+A-A| formula (3) are correct, clean, and fully general; the matching structure in §3 is a correct (though so far unquantified) realizability constraint; the reduction "uniform weighted hole fraction near A at scale N^{5/6} => constant below 1.5154" is correct and, with the known autoconvolution inequality in place of Cauchy–Schwarz, becomes "any fixed positive theta_0 suffices" (R4). Usable negative results: all one-point moments of r are rigid (5), so no unshifted moment carries extra information; the first-moment balance (22)–(24) yields only an O(L/N) hole fraction and cannot give a constant one; the E_4 route gives constant 8. The exact remaining obstruction is to prove that a B_3 set with m >= (3/2)N^{1/3} has a positive proportion of holes of A+A-A within distance o(N) (but >> N^{2/3}) of its own elements; this fails in the density relaxation (the cap binds at h = 0 there), so it requires an argument using the integrality of r and the matching/realizability structure, none of which the report has made quantitative.

## 6. Not checked

Process claims (Node.js timings, which files were read, that no sub-agent was used) cannot be verified from the file. The hypothesis of §1 was not tested on any set in the density regime at large N, because no such set is available; its truth is open.
