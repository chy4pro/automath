PASS-WITH-REPAIRS

# Referee report (referee-2): Erdős #241, probe PROBE_ASTRA_5 (round 4)

Reviewed file: `problems/erdos241/PROBE_ASTRA_5_20261009.md` (522 lines). Nothing else under the repository was read. No web, no papers. Line numbers below refer to the reviewed file.

**Verdict in one paragraph.** Every statement the report labels as proved is correct. I re-derived each step by hand, with exact quantifiers, constants and onsets. All reported finite checks reproduce exactly. I found no circularity and no hypothesis used before it is available. The conditional statement in §6 is correctly quantified and clearly labelled as conditional. The repairs are about status and framing, not mathematics:
- The STATUS keyword should be **OPEN**, not PARTIAL. Nothing proved moves toward the target. The only unconditional bound is the classical-type (4N)^{1/3} bound, which is weaker than the brief's known 1.5154.
- §6 needs two clarifications. First, by the report's own identity (11), the "hole-fraction" hypothesis is, up to an explicit ±5N^{-1/6}, the same thing as an upper bound on the smoothed pair-sum energy. It is therefore a reparametrisation of the Cauchy–Schwarz/autoconvolution input, not a new kind of realizability information. Second, the instance θ_0 = 13/100 beats 1.5154 only at the level of the brief's rounding.

## 1. Claim-by-claim verdicts (re-derived on paper)

| Report item | Verdict | How checked |
|---|---|---|
| §2.1: B_3 ⇒ B_2; d(0)=m, d(h)∈{0,1} for h≠0 (lines 77–79) | Correct | Append a fixed element and cancel it. Equal nonzero differences give a+e=c+b, and the swapped alternative forces a=b, i.e. difference 0. |
| §2.1: uniqueness of noncancelling representations; values in A only cancel; r=2m−1 on A | Correct | {a,b,c'}={a',b',c} with c∉{a,b} forces c=c'. For x∈A, B_2 gives {a,b}={c,x}. The count is 2(m−1)+1. |
| T∩A=∅, \|T\|=m(m−1), (3) \|S\|=m+m²(m−1)/2 | Correct | Case count: C(m,2)(m−2) + m(m−1) + m. This also holds for m=0,1,2. |
| (4) pointwise formula for r | Correct | Four disjoint cases give 2m−1, 1, 2, 0. Also checked at m=0,1. |
| (5), (6) one-point moments | Correct | Re-summed. k=1 gives m³ and k=2 gives 6m³−9m²+4m. |
| (1) C(h)=2m−2H+(2m−3)d−B | Correct | C(h)=Σ_{a∈A} r(a+h), then sum (4) over a∈A. Here Σ_a 1_A(a+h)=d(h). |
| (7) C(0)=2m²−m; H=0 on D | Correct | Ordered B_2 count. Also consistent with (1), since B(0)=\|T∩A\|=0. |
| (8) C(h)=4m−4 on D\{0}; B(h)=1 there | Correct | {a,b,v}={c,e,u} with u≠v gives {a,b}={u,z}, {c,e}={v,z}. Multiplicities: 4 per z∉{u,v}, 2 each for z=u and z=v. Direct check: only a=u puts a+h=2u−v into T. |
| (9) C(h)≤2m off D | Correct | From (1) with d=0. |
| §3 matching constraint (lines 167–175) | Correct, but not new | For h∉D, a positive pair {a,b} with negative pair Q is the noncancelling representation sum(Q)−b of a−h. "Two positive pairs share a" is therefore exactly the uniqueness of §2.1 evaluated at a−h. It is a restatement of (4), not an additional constraint. Suggested relabel (minor). |
| (10) Cauchy–Schwarz on q_L, support [2,2N+L−1], size 2N+L−2 | Correct | Re-derived. |
| (11) Σq_L² = Σ_h w_L(h)C(h) = 2mL²−2W_L+(2m−3)V_L−U_L | Correct | Σ_n p(n)p(n+h)=C(h) holds directly by relabelling. The phrase "since C is symmetric" (line 191) is harmless but unnecessary. #{(j,k): j−k=h}=w_L(h) and Σ_h w_L(h)=L². |
| (12), (13) | Correct | V_L≤L·Σd=Lm² needs 2m−3≥0, i.e. m≥2, which is stated. (2m−3)m≤2m². θ_L∈[0,1] because H≤m. |
| (14), (15) | Correct | S⊂[2−N,2N−1]. For m≥3, m³−m²≥(2/3)m³ gives m³<9N, and 9^{2/3}=81^{1/3}<5. For m≤2, m²≤4≤5N^{2/3}. |
| (16), (17), (2), (18) | Correct, all N≥1 | With L=⌈N^{5/6}⌉: 2N+L−2≤2N+N^{5/6}−1 and 2m²/L≤10N^{−1/6}. Both factors are ≥0. Expanding gives 4(1−θ)N + (2(1−θ)+20)N^{5/6} + 10N^{2/3} ≤ 4(1−θ)N + 32N^{5/6}. The constant 32 is exact as stated. m=0,1 are trivial. |
| (19)–(21) global holes | Correct, trivial | G_N=3N−2−\|S\|. Using (18) and m²/2−m≥−1/2. Note: the limiting fraction 1/3 is weaker than what the brief's own known bound already gives, (3−1.74)/3≈0.42. |
| §5.1 artificial-set relaxation (line 294) | Correct as stated, and labelled as a relaxation only | See the framing remark R3 below. The relaxation drops the report's own identity (1), so it is looser than the real constraint. |
| (22) first-moment balance | Correct | Σ over quadruples of first-positive minus first-negative coordinate; symmetry in each pair gives 2(Σu−Σs)=hC(h). |
| (23), (24) | Correct | h∉D ⇒ −h∉D and r(a±h)∈{0,1,2}. Σe_+=Σe_−=2m−C(h)=2H+B. Then 1≤a≤N gives hC/2≤(N−1)Δ_h. Rearrangement re-done. |
| (25), (26), (27) | Correct | Σ_h B(h)=m\|T\|. The H/m lower bound from (24) is ≤\|h\|/(2(N−1)+\|h\|)≤(L−1)/(2(N−1)). U_L/(mL²)≤m²/L≤5N^{−1/6}. |
| §6 (28) arithmetic | Correct | 1.5154³=3.480020872264 and θ_*=64997390967/500000000000. |
| §6 conditional (lines 374–398) | Correct and clearly labelled conditional | Under the assertion of line 69, (17) gives m³/N≤87/25+32N^{−1/6}. For N≥3200000^6, 32N^{−1/6}≤10^{−5}. Sets below the regime satisfy m³<27N/8<3.48001N. So limsup≤3.48001^{1/3}=1.5153984…<1.5154. The general version (line 374) is also right: limsup≤max(3/2,(4(1−θ_0))^{1/3})<1.5154 for θ_0>θ_*. |
| §7 route 2 (C–S on r) | Correct | (Σr)²≤\|S\|Σr². |
| §7 route 6 (E_4 bounds) | Correct | I re-expanded 2m⁵+(2m²−m)(2m²−3m)+m(m−1)(4m−4)(2m−4)=2m⁵+12m⁴−40m³+43m²−16m. The support of C is in [2−2N,2N−2] (4N−3 points). Leading coefficient 8. |

No error was found in any proved statement. Conventions are used consistently throughout:
- ordered tuples with repetition for p, r, d, C;
- multisets for B_3;
- w_L(h)=max(0,L−|h|) with Σw_L=L².

## 2. Repairs required

**R1 (status, line 1 and line 522).** Change the keyword PARTIAL to **OPEN** and keep the list of auxiliary facts. Reason: nothing proved is progress toward c<1.5154.
- (18) has limiting constant 4^{1/3}=1.587401… This is, to my recollection, the classical Cilleruelo-type (4N)^{1/3}+O(N^{1/6}) bound for B_3 sets, and it is weaker than the brief's known 1.5154.
- (1), (3)–(9) and the matching constraint are elementary restatements of the B_3 property.
- (22)/(24) is a correct new-looking identity, but the report itself shows (26) that it yields only an O(N^{−1/6}) hole fraction at the relevant scale.
- §6 is conditional.

The report is candid in its body (line 7, line 258, line 398). It does not present the 4^{1/3} bound as progress, and it does not present the conditional as unconditional. Only the keyword overstates.

**R2 (status line, line 1).** Add to the status line that the unconditional constant is 4^{1/3}≈1.5874>1.5154. A reader of the status line alone currently sees "|A|^3 <= 4N + 32N^(5/6)" listed as a proved result without that qualification.

**R3 (framing of the §1/§6 hypothesis; lines 67–71, 294, 412–414).** Add the following observation. It follows in two lines from the report's own (11), (12), (15), (16), (27).

From (11), θ_L = 1 − E_L/(2mL²) + ε_L, where E_L := Σ_n q_L(n)² = Σ_h w_L(h)C(h) and ε_L = ((2m−3)V_L − U_L)/(2mL²).
- For m≥2 we have V_L ≥ Lm ≥ 0, so (27) gives ε_L ≥ −(5/2)N^{−1/6}.
- By (12), (15), (16), ε_L ≤ m²/L ≤ 5N^{−1/6}.

So |θ_L − (1 − E_L/(2mL²))| ≤ 5N^{−1/6}. The "weighted hole fraction ≥ 13/100" assertion is therefore equivalent, up to an explicit O(N^{−1/6}), to the smoothed pair-sum energy bound E_L ≤ (87/50)·mL². That is an L²-bound for the representation function of A+A smoothed at scale N^{5/6}, the discrete analogue of c³‖f∗f‖₂² ≤ 1.74. It is the same quantity to which Cauchy–Schwarz (10) is applied, and the same kind of autoconvolution-norm input as in the known approach.

Consequences:
- The §6 reduction is a reparametrisation, not a reduction to a different kind of information.
- The §5.1 / route-4 sentence "proving that B_3 realizability excludes this behavior is the unresolved part" should say that the missing input is this energy bound. Identity (1) already fixes Σ_a 1_S(a+h) in terms of C(h), d(h), B(h), so "S arbitrary" is not the relevant relaxation.

I verified the identity and the bound |ε_L|≤5N^{−1/6} exactly, in rational arithmetic, on all 49,544 B_3 subsets of {1..37} with m≥2 (see §3 below).

**R4 (margin of the 13/100 instance; lines 69, 376–396).** State the conditional primarily in parametric form: θ_L≥θ_0 eventually ⇒ limsup ≤ max(3/2, (4(1−θ_0))^{1/3}). Also say explicitly how small the 13/100 margin is:
- 13/100 exceeds θ_* only by 5.2×10^{−6}.
- The resulting constant 1.5153984… is below 1.5154 only by 1.6×10^{−6}, which is at the level of the brief's 5-significant-digit rounding. If the unrounded known constant is ≤1.51539 (cube 3.47995), the instance gives no improvement at all. I cannot check this without literature.
- 1.5153984 lies above the brief's density-only barrier 1.5152. A conditional that targets a genuine beyond-density improvement needs θ_0 > 1 − 1.5152³/4 = 0.130339202048.

This is a precision and labelling repair. The statement as written is formally correct relative to the literal brief.

**Minor (optional).**
- (a) Line 191: drop "since C is symmetric"; the equality is a relabelling.
- (b) Lines 167–175: say that the matching constraint is §2.1 uniqueness evaluated at a∓h.
- (c) Line 414 "substantial global hole fraction": note that it is a direct consequence of (18) and weaker than what the known 1.5154 bound implies.

## 3. Independent re-checks (my own code; Python 3, exact integer/rational arithmetic, no solvers; total CPU ≈ 5 s)

**Check 1. Exhaustive enumeration of the B_3 subsets of {1..20}.** I used a DFS over increasing elements; B_3 is hereditary.
- 2,089 sets including the empty set. By size: 1, 20, 190, 936, 942 for m=0..4; none of size ≥5. Exact agreement with §8.1.
- Cumulative counts for N=1..20: 2, 4, 7, 11, 18, 30, 45, 67, 96, 132, 177, 237, 314, 420, 559, 737, 968, 1270, 1631, 2089. Exact agreement.
- The first size-4 set in increasing-bitmask order is {1,2,8,12}, in agreement. In lexicographic order it is {1,2,5,14}, so the report's phrase "first encountered" is order-dependent but consistent with bitmask order.
- With N=max A (N=1 for the empty set), I checked (3), |T|=m(m−1), T∩A=∅ and (4) on [1−2N,3N+1]: no failures.
- (5) for k=1..6 and (6): 12,534 comparisons, in agreement.
- Shifts h∈[−2N−2,2N+2]: 150,665 shift points, in agreement (= Σ(4N+5)). At each I checked (1), C=Σ_a r(a+h), C=Σ_n p(n)p(n+h), (7), H=0 on D, (8), B=1 on D\{0}, (9), r(a±h)≤2 off D, (22), and (23)–(24) cross-multiplied for N>1 (131,260 off-D shift points).
- Matching: 51,176 (P,Q) representations at shifts outside D, in agreement. I checked disjointness of P and Q and the matching property on each side.
- Smoothing with L∈{1,2,⌈N/2⌉,N,2N+1} (distinct values): 10,427 comparisons for m≥1. Adding the 3 lengths of the empty set gives the reported 10,430, in agreement. I checked Σq_L=Lm², the support, (10), both forms of (11), (12), and U_L≤Lm²(m−1). The cleared form of (13) was checked for m≥2: 10,333 comparisons, in agreement with §8.4.
- E_4 lower and upper bounds and the polynomial identity of route 6: 2,088 comparisons, in agreement. Also (14), (15), and Σ_h B(h)=m|T|.
- Failures: 0.

**Check 2. The 36 explicit sets of §8.2.** These are P_m={4^j}, Q_m=5P_m+3, and their reflections, for m=1..12. I used N=max A and the exact ceiling ⌈N^{5/6}⌉, computed as the least L with L⁶≥N⁵.
- B_3 verified directly.
- (5) for k=1..10: 360 comparisons, in agreement.
- (1), (7)–(9), (22), (24) on supp(C)∪{±(2N+1)}: 39,576 shift points, in agreement.
- (11), (10) and cleared (13) with W_L=mL²−Σ_{a,s}w_L(s−a): 177 comparisons, in agreement.
- Largest endpoint 20,971,523, in agreement.
- Failures: 0.

**Check 3. §6 arithmetic in exact rationals.** 1.5154³ = 3.480020872264; θ_* = 64997390967/500000000000; 4·(87/100)=87/25; 32/3200000=1/100000; 3200000⁶ equals the displayed 40-digit integer; 348001/100000 < 1.5154³ (gap 1359033/125000000000); 27/8 < 348001/100000. All agree.

At 30 digits: 3.48001^{1/3} = 1.515398421863…, 3.48^{1/3} = 1.515396970335…, and 1.5152³ = 3.478643191808, so the corresponding threshold is θ = 0.130339202048.

**Check 4 (new diagnostic, for R3/R4).**
- The identity θ_L = 1 − E_L/(2mL²) + ε_L and the bound |ε_L|≤5N^{−1/6} (checked as ε_L⁶≤5⁶/N in rationals) hold on all B_3 subsets of {1..37} with m≥2, at L=⌈N^{5/6}⌉, N=max A.
- In the density regime m≥1.5N^{1/3} with m∈{4,5} (N≤37), 162 sets have θ_L<0.13:
  - m=4: 40 of 444, minimum 0.1016 at {1,2,8,12};
  - m=5: 122 of 9,662, minimum 0.0853 at {1,2,5,16,25}.

  This does not contradict the assertion of line 69, which only covers N≥N_*. It shows that no small onset is available, which is consistent with the report's "No value of N_* has been obtained".

## 4. What I could not check

- Novelty and attribution. I had no literature access. My statement that (18) is a classical-type bound is from memory and is not needed for the verdict, since the report itself says it is weaker than 1.5154.
- Whether the brief's 1.5154 is a rounded value of the known constant. This matters only for the value of the 13/100 instance (R4).
- The report's process claims (Node version, CPU timings, files read).
- The author's numerical choice of ⌈N^{5/6}⌉ in §8.2. I used the exact ceiling and obtained the same comparison count, 177.

## 5. Honest status

**OPEN.**
- No statement toward c<1.5154 is proved.
- The unconditional bound has constant 4^{1/3}>1.5154 and is presented honestly as not reaching the target.
- The proved identities are correct but elementary.
- The §6 conditional is correctly quantified and explicitly labelled conditional, but its hypothesis is, by (11), equivalent up to ±5N^{−1/6} to the smoothed-energy bound that the target itself requires.
- Nothing is dressed up as unconditional, and the one relaxation obstruction (§5.1) is labelled as a relaxation. Only the PARTIAL keyword overstates.

## 6. Value

Usable pieces:
- The exact, fully effective coupling (1)/(11). It makes the classical (4N)^{1/3} argument explicit with onset N≥1, and shows that the local hole fraction θ_L near A is (up to ±5N^{−1/6}) the slack 1 − E_L/(2mL²) in the smoothed pair-sum energy.
- Three negative results: the one-point moments of r are rigid (5), so seed (b) cannot work through moment defects of unshifted r; the first-moment endpoint balance (22)/(24) gives only an O(N^{−1/6}) hole fraction at scale N^{5/6}; and the unsmoothed E_4 route gives constant 8.

The exact remaining obstruction is an upper bound E_L = Σ_h w_L(h)C(h) ≤ 2(1−θ_0)mL² with θ_0 > 0.129995 (θ_0 > 0.130339 for a beyond-density improvement) for B_3 sets with m ≥ 1.5N^{1/3}. That is the smoothed autoconvolution L²-norm problem itself, so the "hole" seed (a), as formalised here, does not supply a new handle.
