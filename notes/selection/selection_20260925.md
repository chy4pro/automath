# Selection Report — 2026-09-25

## 1. Method

Offline pool of 329 open problems with Lean statements (formal-conjectures repository).
Excluded past-work problem numbers: 700, 770, 1212, 708, 859, 377, 693, 1189, 1188, 463,
357, 128, 709, 375, 167, 23, 324, 68, 595, 1159, 138, 390, 394, 450, 522, 942, 959, 996,
1201, 32, 70.

Pipeline stages, in order:
1. **Opus shortlist** — 15 candidate problems selected across two slots (slot 1: deep
   attack line, slot 2: deterministic/certificate line), each with a rationale ("why").
2. **Literature-first G2** — for each shortlisted problem, a dedicated pass reads the
   erdosproblems.com page, the pinned Lean statement, the primary and adjacent literature,
   AI-tracker/claim sites, and formal-conjectures PR/issue history, producing a verdict
   (CLEAR / OVERLAP / SUBSUMED / HOT), a thinness rating, and a reasoning note. Problems
   verdicted SUBSUMED or otherwise judged not worth a plan were dropped at this stage
   (#883, #65, #1074, #91, #340) and did not proceed to plan/skeptic.
3. **Plan** — for problems that passed G2, a detailed research plan: target partial
   result, method sketch, verification path, first steps, kill criteria, budget, value
   estimate, and risks.
4. **Adversarial skeptic** — an independent pass attempting to refute the plan's premises,
   novelty claims, math, budget, and collision-risk assessment, producing a refuted
   (true/false) verdict, findings list, adjusted value, and confidence.

All statements, numbers, and quotations below are copied verbatim from the source G2/plan/
skeptic records. No editorial opinion is added.

## 2. Summary Table

| n | slot | G2 verdict | thinness | frontier method | plan value | skeptic refuted? | adjusted value | confidence |
|---|------|-----------|----------|------------------|------------|-------------------|-----------------|------------|
| 757 | 1 | OVERLAP | moderate | mixed | medium | true | low | medium |
| 883 | 1 | SUBSUMED | active | mixed | — (dropped before plan) | — | — | — |
| 889 | 1 | OVERLAP | thin | elementary-number-theory | high | false | medium | medium |
| 727 | 1 | HOT | active | analytic/sieve | medium | true | low | high |
| 624 | 1 | OVERLAP | moderate | combinatorial | medium | true | low | medium |
| 65 | 1 | SUBSUMED | active | combinatorial | — (dropped before plan) | — | — | — |
| 243 | 1 | HOT | active | elementary-number-theory | low | true | none | high |
| 930 | 1 | HOT | moderate | analytic/sieve | low | true | none | high |
| 203 | 2 | HOT | active | computational | medium | true | low | high |
| 1056 | 2 | HOT | thin | computational | low | true | none | high |
| 624 | 2 | CLEAR | moderate | combinatorial | medium | false | low | medium |
| 389 | 2 | HOT | active | computational | medium | true | none | high |
| 1074 | 2 | SUBSUMED | moderate | elementary-number-theory | — (dropped before plan) | — | — | — |
| 91 | 2 | SUBSUMED | moderate | mixed | — (dropped before plan) | — | — | — |
| 340 | 2 | SUBSUMED | thin | combinatorial | — (dropped before plan) | — | — | — |

## 3. Per-Candidate Sections

### #757 (slot 1)

**Pinned statement.** Call c admissible if every finite A ⊂ ℝ in which every 4-element
subset B has at least 5 distinct positive differences (equivalently |B−B| ≥ 11) contains a
Sidon subset S with |S| ≥ c|A|. Determine sup{c : c admissible}. Known: 1/2 < sup < 3/5
(Gyárfás–Lehel 1995). Lean: FormalConjectures/ErdosProblems/757.lean, erdos_757 plus
variants lowerBound and upperBound; both variants are still `sorry`.

Pinned from /work/problems/formal-conjectures/FormalConjectures/ErdosProblems/757.lean,
current version after merged FC PR #5244 (2026-09-01), which changed `= 11` to `11 ≤`.
IsAdmissible c :⇔ for every finite A ⊆ ℝ such that every B ⊆ A with |B| = 4 has
11 ≤ |B − B|, there is some S ⊆ A with IsSidon S and c·|A| ≤ |S|. The condition means at
least 5 distinct positive differences among the 6 pairs. erdos_757 asks for the value of
sSup {c | IsAdmissible c}, left as answer(sorry). The variant lowerBound, 1/2 < sSup, and
the variant upperBound, sSup < 3/5, are both tagged "research solved" and both still have
`sorry` proofs. Their docstrings cite only Gyárfás–Lehel 1995 and are out of date: the page
and the literature now give 9/17 ≤ c* ≤ 4/7. Ma–Tang define c* = lim f(n)/n and prove it
equals inf_{n≥1} f(n)/n, where f(n) is the minimum, over n-element (4,5)-sets, of the
largest Sidon subset. So one finite (4,5)-set whose largest Sidon subset has ratio below
4/7 would directly improve the upper bound.

**Known state (with sources).**
- c ≥ 1/2 (every (4,5)-set of size n contains a Sidon subset of size ≥ n/2). Source: Erdős–Sós (as cited on erdosproblems.com/757 and in Ma–Tang).
- 1/2 + 1/(141·76) ≤ c* ≤ 3/5. The upper bound comes from the first n Fibonacci numbers; the lower bound from a Turán-type problem on sparse 3-uniform hypergraphs. Source: Gyárfás & Lehel, "Linear sets with five distinct differences among any four elements," J. Combin. Theory Ser. B (1995) 108–118 (1995).
- 9/17 ≤ c* ≤ 4/7 (Theorem 1.6), with c* = lim f(n)/n = inf_n f(n)/n (Theorem 1.5). Lower bound via Henning–Yeo's transversal bound on linear F7-free 3-uniform hypergraphs. Upper bound via an explicit 14-point set with largest Sidon subset 8, found with AI assistance. Source: Jie Ma & Quanyu Tang, arXiv:2602.23282 (2026).
- erdosproblems.com/757 (last edited 10 Apr 2026): OPEN, "cannot be resolved with a finite computation." Thanks to Yongxi Lin and Quanyu Tang.
- Sorry-free Lean proof that Admissible c → c ≤ 4/7, built on the Ma–Tang 14-point certificate; submitted to Justin Sun Prize (JSP-000621), closed as "not a complete solution." Source: TheJustinSunPrize/awards PR #74 (2026-09-16 to 09-24).
- AI research agent issue refuting an auxiliary inequality with 12-point sets (ratio above 4/7); no new bound claimed. Source: the-omega-institute/trureturing issue #9804, opened 2026-09-24, open.

**Site/AI-claim status.** Site: Comments (7); proof claims (0); working on: None. No site claim anywhere and no tracker listing a solution. Two active 2026 AI/bounty lines target this exact constant: trureturing #9804 (sharp constant, opened 09-24, still open) and JSP-000621 (Lean formalizations of c ≤ 4/7, closed 09-24). formal-conjectures PRs #2696/#3218 (loophole "formally solved" attempts) closed unmerged.

**Plan.**
- Target: T1 (upper side) — explicit integer set A with n ≤ 40 beating 4/7; T2 (secondary, finite exact statement) f(16)=10 or similar for n ≤ 22.
- Method: harmonic/rigid parametrization of saturated (4,5)-sets, mod-ℓ primality/square tests, tabu/annealing search seeded from Ma–Tang's A_base.
- Verification path: exact-integer double implementation, Lean lemma sSup ≤ s/n from one explicit A, kernel `decide` on Finset ℤ encoding, same-vendor then cross-vendor review.
- First steps: G2 refresh (≤30 min); build exact verifier/certificate emitter; calibration gate against A_base (h=8, n=14); production search on 8 cores; checkpoint report.
- Kill criteria: (a) anyone posts ratio below 4/7 or proves c*=4/7; (b) calibration gate fails after 2 agent-hours; (c) 10 agent-hours (~80 CPU-hours) search leaves best h one above target at every n; (d) T2 dropped unless pilot extrapolates to ≤24 CPU-hours; (e) hard cap 25 agent-hours.
- Budget: ~5 Opus-agent-hours to first checkpoint; hard cap 25 agent-hours; local CPUs only.
- Value: medium.
- Risks: true value may be c*=4/7 (Henning–Yeo bound attained at n=12,14); Ma–Tang may have tried n≥16 silently; naive probe exactly one above target at n=14,16,18; Python-only tooling caps throughput; floating-point solves can mislead; T2 depends on unverified Henning–Yeo hypotheses; moderate collision risk with trureturing.

**Skeptic's findings.**
- G2 missed teorth/optimizationproblems constants/5b.md (Tao's database), which lists this exact constant (C_5b) since 2026-02-27 with no improvement in 7 months — a watched, construction-friendly venue with zero progress.
- Forum contents (now fetched): Tang announces 9/17≤c≤4/7 with exploratory ChatGPT-5.2 Pro use; Tao lists the constant; no constructions below 4/7 and no working-on claims.
- Calibration gate already failing on the plan's own tool: 6 independent 120-second runs at n=14 all ended at h=9, none reaching Ma–Tang's h=8.
- The feasible region for T1 is very narrow (lo(n) rules out n≤15,17,19,21; saturated middle-map constraints for n=18,20,22); Ma–Tang (with GPT-5.2 Pro) stopped at n=14; trureturing only reaches 7/12.
- Upside is real but unlikely: an explicit set below 4/7 would be genuinely certificate-checkable and Lean-checkable, but without it nothing publishable remains.
- Statement pinning confirmed correct (IsAdmissible, IsSidon convention, csSup_le route sound); docstrings stale.
- Tooling claims wrong (a C compiler exists via leanc; nproc is 10 not 8), which cuts in the plan's favor but doesn't rescue the probability argument.
- Active work: trureturing #9804 open (updated today, 0 comments, aimed at proving 4/7 — opposite direction). JSP #74 closed. Collision risk mainly from C_5b database watchers, omitted from the plan's monitoring list.
- Verdict: do not launch as the slot-1 campaign; salvage option is at most a 2–3 agent-hour opportunistic spike with a must-hit gate of h=8 at n=14, no T2, no slot allocation.

---

### #889 (slot 1)

**Pinned statement.** Let v(n,k) be the number of prime factors of n+k that divide none of
n, n+1, …, n+k−1, and let v₀(n) = sup_k v(n,k). Does v₀(n) → ∞? Erdős–Selfridge 1967 proved
v₀(n) > 1 for every n outside {0,1,2,3,4,7,8,16}. Open variants: v_l(n) → ∞ for each fixed
l, and finiteness of {n : v₁(n) = 1} and of {n : V₁(n) = 1}.

v(n,k) = #{p prime : p | n+k and p ∤ n+i for every 0 ≤ i < k}, equal to #{p | n+k : p > k}.
erdos_889 says Tendsto v₀ atTop (𝓝 ⊤) in ℕ∞. Solved variant v0_gt_1: ∀ n ∉
{0,1,2,3,4,7,8,16}, 1 < v₀ n (still `sorry` upstream, tagged research solved). Open
variants: general (∀ l, v_l(n) → ⊤), v1_eq_1_finite, V1_eq_1_finite (V uses full
prime-power components).

**Known state (with sources).**
- v₀(n) > 1 for all n except n = 1,2,3,4,7,8,16, via reduction to Catalan-type equations. Erdős–Selfridge also conjecture v_l(n)→∞ for every l, largest exceptions 330 (v₁) and 80 (V₁). Source: Erdős–Selfridge, Illinois J. Math. 11 (1967) 428–430.
- A different 1971 paper with the same title (Grimm-type functions) is not relevant except by name.
- Guy, UPINT 3rd ed. (2004), problem B27.
- Capital-V₁ variant SOLVED (not effectively): Kenta Kitamura posted a Lean 4 proof (kernel-checked, only propext/Classical.choice/Quot.sound), method elementary (least non-divisor + u³+1 factorization), no explicit n0 bound. FC PR #6453 open. Source: github.com/KitaKen1/erdos-889-capital-v1-finite (2026-09-22).
- Tao–Teräväinen infinitely-many-n bound (arXiv:2512.01739) and Lau's infinitely-often ω(n+k)≪log k bound (arXiv:2604.15042) are adjacent but do not address #889 directly.
- Own finite check confirms exception lists match the 1967 paper exactly up to 3·10^6 (evidence only).

**Site/AI-claim status.** Comments (2, unread under one-page rule but fetched in plan stage). Status OPEN, "cannot be resolved with finite computation." 0 proof claims as of 2026-09-25. Working on: None. GPT-5.2 Pro / Astra llm-hunter attempt got only trivial lemmas, verdict UNRESOLVED.

**Plan.**
- Target: Theorem A — explicit N0 such that for n≥N0 there is k≤10 log n with v(n,k)≥2, giving Corollary A1: {n : v_l 1 n = 1} finite (settles erdos_889.variants.v1_eq_1_finite). Theorem A_l generalizes to every l. Not claimed: main conjecture v₀→∞, v₀≥3 eventually, or the exact largest-exception conjectures (330, 80).
- Method: Baker/Diophantine route — injection lemma (R1), Legendre–Erdős assignment (R2), pigeonhole to smooth terms (R5), three-log Matveev bound (R6) giving log n ≤ K(log log n)^5.
- Verification path: finite witness certificates for 331≤n≤10^9 (checked independently), exact rational-arithmetic computation of constants, same-vendor adversarial review, then conditional Lean with Matveev as a named hypothesis (never claimed "kernel-verified" outright).
- First steps: G2 novelty gate (~1.5h, needs fresh search budget) reading Guy B27, Shorey–Tijdeman, Laishram–Shorey/Saradha, Ramachandra–Shorey 1973, the forum thread and FC PR #6453; write full proof; build witness-certificate generator; referee pass; collision watch.
- Kill criteria: G2 finds Theorem A or lowercase v₁ finiteness already in the literature; someone posts a lowercase proof covering all l; referee finds an unrepaired gap; 10 agent-hours without a referee-clean write-up.
- Budget: ~8 Opus-agent-hours to first checkpoint; 15–30h more for conditional Lean.
- Value: high.
- Risks: novelty uncertain (may be folklore/Shorey–Tijdeman-style); Kitamura is active and named lowercase v₁ as the open next step; effectiveness is only nominal (N0 ≈ 10^20, conjectured exceptions unreachable); Lean can only be conditional (Matveev not in Mathlib); evidence so far thin (unreviewed scripts); nothing here moves the main conjecture.

**Skeptic's findings.**
- Statement pinning correct; Theorem A_l correctly gives only the M=2 level of `general`.
- Math survives attack; re-derived R1–R6 by hand; crude numerical run closes at log n ≈ 1.1×10^20, matching "≈10^20" more than "≲10^20."
- Novelty is the one live refutation risk and could not be closed: web search budget exhausted. G2's list is missing dangerous prior art — Ramachandra–Shorey–Tijdeman (J. reine angew. Math. 273, 1975) and its 1976 sequel run exactly this machinery (Legendre–Erdős assignment + near-prime-power terms + Baker) and may contain Theorem A nearly verbatim. Also flagged: Langevin (1975–77), Tijdeman (Compositio 1974), Erdős Eureka 1975/76.
- If novel, result settles an open FC variant Erdős–Selfridge themselves said they "could not even prove"; if not novel, an expert may call it a routine RST/Tijdeman corollary.
- Kitamura is high-throughput but has not pushed to the 889 repo since 2026-09-22; FC PR #6453 still open, 0 comments. Named lowercase v₁ as open, so collision risk remains but is lowered by his elementary (non-Baker) style.
- Budget realistic for the paper proof (re-derived in minutes), but the G2 gate (RST 1975/76, Langevin, Tijdeman 1974, Erdős Eureka 1975) MUST run before any proof write-up; witness-certificate range should be trimmed (e.g., to 10^8) to avoid quota-burning.
- Lean phase should be downgraded: conditional-on-Matveev proof would not be merged by FC and adds little credibility; formalize only R1–R5 unconditionally if the result survives.
- Net: not refuted on math, pinning, or edge-fit. Legitimate only with the expanded G2 kill gate run first.
- Adjusted value: medium (high if novel, times unknown chance it's a known RST/Tijdeman corollary).

---

### #727 (slot 1)

**Pinned statement.** Let k ≥ 2. Does ((n+k)!)² ∣ (2n)! hold for infinitely many n? The
problem is open even for k = 2. Known: k = 1 holds (Balakran). Erdős–Graham–Ruzsa–Straus
give infinitely many n with (n+k)!(n+1)! ∣ (2n)!.

erdos_727: answer(sorry) ↔ ∀ k ≥ 2, Set.Infinite {n : ℕ | ((n+k)!)^2 ∣ (2n)!}. Variant k_2
(open): the k=2 case. Variant k_1 (solved, Balakran 1929). Variant k_1_2 (solved, EGRS
1975): for every k≥2, infinitely many n with (n+k)!(n+1)! | (2n)!.

**Known state.**
- k=1 case: Balakran 1929, J. Indian Math. Soc. 18, 97–100.
- EGRS posed k≥2 conjecture; proved (n+k)!(n+1)! | (2n)! infinitely often for k < c log n. Source: Erdős, Graham, Ruzsa, Straus, Math. Comp. 29 (1975) 83–92.
- a!b! | n! ⟹ a+b ≤ n + O(log n). Source: Erdős [Er68c] (1968).
- Pomerance 2015 and Ford–Konyagin 2021: adjacent density results on n+k | C(2n,n) and n^l | C(2n,n), not #727 directly.
- Sothanaphan resolved neighboring #728 with Aristotle Lean proof (arXiv:2601.07421, 2026), same Kummer-carry toolkit.
- Unreviewed ChatGPT-assisted candidate for k=2 (Rexyysilent/erdos-727-k2-candidate, 2026-09).
- **G2 correction in plan stage**: the actual site proof claim (1) belongs to Johan Land (2026-09-07), an unconditional proof of k=3 (hence k=2) with a sorry-free Lean development (github.com/beetree/math_erdos_727). Review and independent build reproduction pending.

**Site/AI-claim status.** 7 comments; 1 proof claim (Land's k=3); "Currently working on: ryin, boolean_matrix." Our standing rule excludes problems with an existing proof claim or working-on marker — this problem has both.

**Plan.**
- Target: Theorem A — S(k,3) (k≥3: (n+k)!(n+3)! | (2n)! infinitely often), Theorem B (stretch, S(4,4), i.e. ((n+4)!)² | (2n)! infinitely often — barrier-blocked per own search).
- Method: extends Land's k=3 proof; local Hensel lemma for primes ≤ max(1000,2k); union-bound audit of Q-dependence.
- Verification path: finite Kummer-valuation checks to 60000; local-lemma certificates; Lean reproduction of Land's build then generic parametrized Lean theorem; same-vendor review.
- Kill criteria: Land's build fails to reproduce or an unpatchable gap found; someone posts a general-k extension first; union-bound margin consumed; Lean cost >30h beyond checkpoint or license permission refused.
- Budget: ~10 Opus-agent-hours to first checkpoint; 20–35h more conditional.
- Value: medium.
- Risks: low novelty (referee may call it a remark); dependency on Land's unrefereed claim; medium collision risk; no license on Land's repo (derivative work needs permission, contact is owner-gated); stretch B very likely out of reach (quadratic-family barrier proven, cubic/quartic searches empty).

**Skeptic's findings.**
- (f) Problem fails entry gate: 1 proof claim + working-on markers (ryin, boolean_matrix) present on the page as of 2026-09-25.
- (c) Theorem A (S(k,3)) is a footnote to Land's work, not a new citable result; the identity shows all real difficulty is in the squared triple Land already solved; not a formal-conjectures target; EGRS already proved a stronger growing-range form.
- (c) The actual open core, ((n+4)!)² | (2n)!, is untouched; plan's own analysis shows the quadratic-family route cannot reach it (four squares in AP impossible per Fermat/Euler); cubic/quartic searches empty; only remaining route is analytic (non-edge).
- (b) Frontier is analytic; plan's contribution would be local digit bookkeeping atop someone else's unrefereed analytic proof; "should carry over" is unverified and is the whole theorem.
- (e) Budget unrealistic: ~7.9k lines of Lean to parametrize, no license on Land's repo, contacting him is owner-gated; Land's n ≈ 10^900 so finite checks can't touch real family members.
- (f) High collision and dependency risk: Land is the natural person to post the trivial extension; targets of ryin/boolean_matrix undisclosed; whole campaign rests on an unrefereed, not-yet-independently-reproduced claim.
- (d) Statement pinning correct; finite checks reproduced (with one correction: first k=4 solution is 8174, and 8175 is also a solution; plan omitted k=7, count 5).
- (a) No missed paper found on S(k,3), but second web search was blocked (session search budget exhausted) so a Land follow-up in the last few days could not be ruled out.
- Salvage: reproducing Land's Lean build offline with an axiom audit (owner-gated disclosure), ~1–2h, as a watchlist item only.
- Adjusted value: low; confidence: high.

---

### #624 (slot 1)

**Pinned statement.** For |X| = n, let H(n) be the least m for which some f : 2^X → X has
{f(A) : A ⊆ Y} = X whenever |Y| ≥ m. Prove that H(n) − log₂ n → ∞. The trivial bound is
H(n) ≥ log₂ n, since 2^m ≥ n is needed.

ExistsEventuallySurjective n m := ∃ f : Finset (Fin n) → Fin n, ∀ Y, #Y ≥ m → Y.powerset.
image f = univ. H n := sInf of the set of valid m (0 if n=0). erdos_624: Tendsto (H n −
logb 2 n) atTop atTop, category research open.

**Known state.**
- log₂ n ≤ H(n) < log₂ n + (3+o(1)) log₂ log₂ n. Source: Erdős–Hajnal, "Egy kombinatorikus problémáról," Mat. Lapok 19 (1968) 345–348.
- Erdős said even H(2^k) ≥ k+1 was open; Alon gave a simple pigeonhole proof of it, plus a stronger (1−c)2^k theorem for n=2^k and a ¼·2^k construction (source and exact paper not located).
- Erdős–Gyárfás conjecture on the H(2^k) step, per erdosproblems.com/624 (fetched 2026-09-25); status OPEN, "cannot be resolved with a finite computation," last edited 27 Oct 2025.
- Public AI write-ups (llm-hunter, GPT-6 Astra Ultra continuation dated 23 Sep 2026) give an unreviewed upper bound H(n) ≤ ⌈log₂ n + 2 log₂ log₂ n + 2⌉ and an LP/first-moment barrier; self-rated COMPLETION 5%.

**Site/AI-claim status.** 2 comments (unread, one-page rule); 0 proof claims; working on: None. Active: the-omega-institute/trureturing issue #9861 (opened 2026-09-25, 0 comments as of check); Justin Sun Prize PR #635 (H(2^k)≥k+1, closed 2026-09-24 as partial progress only); llm-hunter three rounds.

**Plan.**
- Target: Theorem A — explicit uniform bound N(k) ≤ ((5+√5)/8)2^k + 2, giving liminf(H(n)−log₂n) ≥ 0.14487 for all n≥n0 (explicit n0). Theorem A' — explicit constant in Alon's theorem (c=1/12). Theorem B (conditional, depth-3 LP) — β3≈0.8121, liminf≥0.300.
- Method: block decomposition (Lemma 1) + Cauchy–Schwarz degree-sum bound (Lemma 2) + depth-3 colour-type LP (Lemma 3, unverified float-grid dual value).
- Verification path: exact-Fraction threshold scan (already run k=3..30); Lean glue lemmas + Cauchy–Schwarz over Finset + rational threshold; same-vendor then cross-vendor review.
- Kill criteria: Alon/[Er99]/herong/omega/llm-hunter already has explicit uniform bound ≤0.9045 or ≤0.81; someone publishes Lemma 2 first; finite-m analysis can't stay uniformly bounded; Lean exceeds 8 agent-hours; certified depth-3 value >0.85; a proof claim or working-on marker appears; any step needs Turán densities of K_4^(3)+ or SDP.
- Budget: ~6–8 Opus-agent-hours to checkpoint 1; conditional 4–6h more for checkpoint 2.
- Value: medium.
- Risks: Alon's unlocated (1−c)2^k argument may already give general-n β<1; omega #9861 publicly states Lemma 1 already; modest value (constant-size gain on a divergence conjecture); Theorem B's β3 only from an unverified float grid; Lean cost for irrational-to-rational constant handling could overrun budget.

**Skeptic's findings.**
- (d) Math checks out: re-derived Lemma 2 by hand; exact-Fraction scan (k=3..15) confirms threshold safety; glue lemmas correct.
- (a) G2 missed that [Er99] is identified and citable: Gyárfás "Problems and memories" (arXiv:1307.1768, 2013) cites it as Erdős, CPC 8 (1999) 1–6 — a findable paper nobody has read, the #859 failure pattern; kill criterion 1 cannot be decided until it or Alon's own note is read.
- (c) Novelty doubtful: the plan's own Theorem A' shows the block+Cauchy–Schwarz method reproduces Alon's (1−c)2^k theorem — very plausibly Alon's own argument or a close relative, which usually carries over to general n almost verbatim; if so Theorem A is at best "Alon's argument made explicit," a footnote.
- (c) Value sits below the named Erdős–Gyárfás milestone (β<1/2, our non-edge); Theorem A (β=0.9045) and conditional B (β≈0.81, uncertified) are far from it; gain is a constant 0.145 (or 0.30) on a divergence conjecture.
- (f) Field is crowded and active this week: omega#9861 (updated today, states block lemma + fractional barriers + random-kernel obstruction, explicitly rejects partial-result PRs); herong's forum comment (09-18) gives exact small values and a proof for n=2^m; JSP PR #635 (sorry-free H(2^k)≥k+1) closed 09-24 as "only partial progress," inviting resubmission — direct incentive for that Lean-active actor to strengthen exactly this bound; llm-hunter three rounds including Astra on 09-23.
- (b) Checkpoint 1 within edge (elementary, no SDP); checkpoint 2 drifts into Turán/flag-algebra territory, evidence is only a float grid.
- (e) Budget optimistic: 4–5h Lean estimate likely needs 8–12h; source-closure step has no remaining WebSearch budget, so kill test 1 may stay unresolved while Lean hours are spent.
- Verdict: refuted as a slot-1 campaign — correct and cheap, but (i) novelty depends on an identified-but-unread source whose known theorem the same method reproduces, (ii) result is a constant-size footnote below the named step, (iii) crowded by active Lean and AI actors this week. Salvage at most a ≤2h side note gated on first reading Erdős CPC 8 (1999).
- Adjusted value: low; confidence: medium.

---

### #243 (slot 1)

**Pinned statement.** If integers a₁ < a₂ < … satisfy a_n / a_{n−1}² → 1 and Σ 1/a_n ∈ ℚ,
then a_n = a_{n−1}² − a_{n−1} + 1 for all sufficiently large n. This is a characterisation
of Sylvester's sequence. In Lean, erdos_243 expresses rationality as Summable in ℚ.

erdos_243 (research open): StrictMono a; Tendsto (a n / a(n-1)^2) → 1; Summable
((1:ℚ)/a·); conclusion ∀ᶠ n, a n = a(n-1)^2 − a(n-1) + 1.

**Known state.**
- Erdős–Straus [ErSt64] Theorem 3: limsup condition settling the "recurrence fails eventually" case.
- Duverney [Du01] Corollary 3.2: conditional stronger-hypothesis version.
- Koizumi, arXiv:2504.05933 (2025): states #243 verbatim as Question 5; proves rigidity theorems and gives heuristics; no proof of #243.
- Will Cook, "Cubic-Rate Irrationality and Reciprocal-Tail Rigidity" (GitHub, Sept 2026, wcook04/plectis-erdos): Theorem 7.2 and Corollary 1.1 handle a restricted rate 1+3/n+o(n^{-3}); bounded-negative-part and bounded-P_n/a_n-increment criteria; Lean proofs reportedly sorry-free; AI-assisted (Claude Code, Codex); unrestricted problem remains open.
- Jared Wilder's findings ledger: an exact "defect telescoping identity" and a retracted false counterexample.
- Related but distinct: Kovač–Tao arXiv:2406.17593; Barreto–Kang–Kim–Kovač–Zhang arXiv:2601.21442; Crmarić–Kovač arXiv:2504.18712.

**Site/AI-claim status.** 8 comments (forum covers formalisation and Koizumi's paper); 0 proof claims on page; working on: None (site markers empty; off-site activity is heavy). formal-conjectures: only erdos_243 open; multiple closed PRs (#2860 loophole; #5059/#5058 Koizumi corollaries closed 09-22; #5292/#5291 Cook's variant closed 09-22); PR #6523 OPEN since 2026-09-23 (Cook, cubic-rate variant, external sorry-free Lean).

**Plan.**
- Target: Theorem R(d) — complete regular-rate family for every integer degree d≥2, d≠3 (Cook covers only d=3). Corollary combining with Cook's exclusions.
- Method: generalizes Cook's d=3 proof structure (gcd/primitive shape, rational-factor exclusion, level-1 square condition, exceptional-m classification, level-2 mod-ℓ automaton) to general d.
- Kill criteria: Cook/Bado posts integer-rate exclusion first; d=2 exceptional family has no uniform argument after 8h; certificate engine finds unkillable survivor; automaton unsound; 40-hour budget spent without R(2) closed.
- Budget: ~20 Opus-agent-hours to checkpoint 1; +20h for general d and Lean.
- Value: low (plan's own rating).
- Risks: collision high (Cook's extraction is already general-d); value low (artificial rate family, disjoint from core difficulty); math risk medium-high (ES75 counting may lack slack); Lean needs licence/owner sign-off to reuse Cook's code.

**Skeptic's findings.**
- (f) ACTIVE COLLISION, decisive: wcook04/plectis-erdos pushed today (12:46Z); OPEN PR #247 created 2026-09-25 02:27Z, "Prove irrationality at nonintegral regular rates for Erdős 243" — Cook's pipeline moving through the λ-rate family this very day; integer d≠3 is the obvious next PR. A second OPEN PR #241 (2026-09-24) extends the square-specialisation machinery to general algebraic integers; Cook's own files already scope the general-d classification as "pending" work.
- Forum (fetched): 8 comments; Cook posts the bounded-increment/cubic-rate results; Tao says "I see no plausible way to rigorously prove the claim"; no one discusses general-d rates or claims a full solution.
- (a) Literature not thin: Koizumi, Erdős–Straus, Duverney, Cook's 65KB paper + 200KB companion with 100+ Lean files, Wilder's ledger, three llm-hunter write-ups.
- (b) Work is outside our edge for the part that matters: closing R(2) needs a new level-2 Chebotarev/Galois specialisation lemma (L6), which the plan admits is open; R(4..6) needs algebraic-number-theory classification.
- (c) Result is a footnote even if it lands: plan's own value rating is "low"; the headline corollary depends on Cook's unreviewed, pending-review Lean; Cook himself writes "the claim of historical novelty is not made" for his λ extensions.
- (d) Statement pinned correctly; independently verified the plan's closed-form Q(α±1) formula and the d=2 exceptional classification.
- (e) Budget unrealistic: Cook needed revisions R7–R21, dozens of Lean files, and weeks of pipeline time for the single case d=3, m=12; plan budgets 20h for R(2) alone including an open lemma.
- Verdict: HOT, low-value, inside someone else's active programme, same-day PR on the adjacent case makes collision near-certain, method outside edge for the parts that matter, budget underestimated. Do not run even as a time-boxed side campaign.
- Adjusted value: none; confidence: high.

---

### #930 (slot 1)

**Pinned statement.** Is it true that for every r there is k such that, if I₁,…,I_r are
disjoint intervals of consecutive integers each of length ≥ k, then ∏ᵢ ∏_{m∈Iᵢ} m is not a
perfect power? The case r = 1 is Erdős–Selfridge 1975: a product of consecutive integers is
never a power.

`answer(sorry) ↔ ∀ r > 0, ∃ k, ∀ I₁ I₂ : Fin r → ℕ, (lengths ≥ k, disjoint, positive) →
¬ IsPower (∏ products)`.

**Known state.**
- r=1: product of k≥2 consecutive positive integers never a perfect power. Source: Erdős & Selfridge, Illinois J. Math. 19 (1975) 292–301.
- Erdős–Graham (1976/1980) ask a related but different finiteness question for fixed lengths.
- Skałba 2003/2019, Ulas 2005, Bauer–Bennett 2007, Luca–Walsh 2007, Bennett–van Luijk 2012, Yıldız–Gürel 2020, Tengely–Ulas 2016: a 50-year line building square counterexamples for FIXED block length with many blocks — different regime from #930 (fixed r, growing k).
- Decisive: Tao, arXiv:2603.27990 (Mar/Apr 2026) — r=2 square case with first block [1,a] ("type F3" intervals) is bounded by Vinogradov exponential sums; states the Erdős–Graham question "is there an F3 interval of length > 3?" is STILL OPEN.
- Jared Wilder (github, 2026-09-11..18): k(2) ≥ 5 via explicit length-4 square pair; unrefereed.

**Site/AI-claim status.** 1 comment; 0 proof claims; "Currently working on: Svyable, satsun93" — puts problem out under our standing rule. llm-hunter attack logged 2026-09-25.

**Plan.**
- Target: T930-R(b) — near-regime theorem: if the window is far from 0 relative to its length (A+1 > L²), then g ≥ c0·S/log S for S≥S0 (explicit constants), i.e. #930 holds on the near regime. Part (a): folklore prime-in-top-block obstruction. Part (c) optional: finite square search for r=2, both lengths ≥5, up to X=10^8.
- Kill criteria: omitted-terms literature (Saradha–Shorey etc.) already implies near-regime statement; ES75 counting can't absorb the required loss; collision from named working-on users or Wilder; budget 20h cap.
- Budget: ~8 Opus-agent-hours to checkpoint; hard cap 20h.
- Value: low (plan's own rating).

**Skeptic's findings.**
- (f) Hard exclusion rule triggered independent of math: page shows "Currently working on: Svyable, satsun93"; Wilder already holds the cheap deterministic item (k(2)≥5); llm-hunter attack 2026-09-25.
- (a) G2 missed the whole "products of integers from a block of consecutive integers with terms omitted" literature: Shorey (Acta Arith. 1987), Balasubramanian–Shorey (1993), Shorey–Nesterenko (1996), Mukhopadhyay–Shorey (2004), Hanrot–Saradha–Shorey (2001), Saradha–Shorey (2008); traces back to Erdős 1955 ("On the product of consecutive integers III").
- (c) Target T930-R(b) is a known special case: the plan's own hypothesis (A+1>L², i.e. n>k²) is exactly the literature's regime; conclusion is weaker than Erdős 1955's omitted-term count. Kill criterion 1 is met, though full texts (IMPAN/matwbn 403'd) could not be read to confirm exact constants.
- (c) Remaining parts (a) and (c) have no value: (a) is trivial folklore; (c) extends Wilder's ground without proving anything about k(2); far regime (the real difficulty, including the open Erdős–Graham F3 question) is explicitly excluded.
- (b) Method outside edge: the far regime needs prime-gap/Vinogradov exponential sums (Tao 2026) or Diophantine curve methods (Luca–Walsh, Bennett–van Luijk), both declared non-edges.
- (d) Statement pinned correctly; note the answer to r=2 may be NO per a forum comment, which would make "partial result toward YES" moot.
- (e) Budget unrealistic: rebuilding ES75's fine counting step with fully explicit constants won't fit in 3 hours, and the 2h G2 step alone would already end the campaign.
- Adjusted value: none; confidence: high.

---

### #203 (slot 2)

**Pinned statement.** Is there an integer m with gcd(m, 6) = 1 such that 2^k·3^l·m + 1 is
composite for all k, l ≥ 0?

erdos_203 : answer(sorry) ↔ ∃ m, m.Coprime 6 ∧ ∀ k l, ¬ (2^k * 3^l * m + 1).Prime.

**Known state.**
- Posed in Erdős–Graham, Old and New Problems (1980), p.27.
- Related single-base Sierpinski/Riesel-multi-base literature (Filaseta–Finch–Kozek 2008; Chen 2010) does not address the mixed two-base form.
- Cremona–Koymans, arXiv:2601.03212 (2026): adjacent lattice-covering theory for ℤ², does not mention #203.
- Multiple 2026 computational campaigns: veljjanoski (71.7–76.0% coverage, "no strip covering exists" claim); Neo7672/JSP-000190 (Claude-assisted, best partial cover 79–83%); Jared Wilder corpus (125 Lean files, ~17-19 unrefereed papers, exact finite obstructions e.g. union density ≤823/840 at N=5040); the-omega-institute/trureturing #9414 (Codex-driven, 5 merged PRs of obstructions, suspended, "Whole-solution KPI: 0"); own earlier Qwen campaign (m=7279 refuted, 51.4% uncovered).

**Site/AI-claim status.** 15 comments; 0 proof claims; "Currently working on: uona, AnimishSharma" — excludes under standing rule. JSP-000190 bounty drawing invalid AI submissions.

**Plan.**
- Target: StripL0 — finite-strip (bounded-l) existence theorem: ∃ m coprime to 6 such that 2^k 3^l m+1 composite for all k and all l≤L0. Checkpoint L0=1 (kernel-checked); headline aiming L0≥3.
- Method: fibre lemma per prime, SAT/kissat encoding, DRAT certification.
- Pilot evidence (unverified): L=1 covered at N=5040 with 70 primes; L=2 failed (409/15120 cells uncovered).
- Kill criteria: G2 finds StripL already published; L0=2 uncertified after 12h; collision from active campaigns; general StripL-for-all-L argument found (pivot); Lean kernel check exceeds budget.
- Budget: ~10 Opus-agent-hours to checkpoint 1; hard cap 20h.
- Value: medium (plan's own rating).

**Skeptic's findings.**
- (f) HARD-GATE VIOLATION, decisive by itself: page shows working-on markers; forum (fetched) shows uona actively working with sieve methods since 2025-12-31 and AnimishSharma posting density-obstruction theory 2026-06-21; selection note already records #203 as "Dropped; not pursued to plan/skeptic."
- (c) Target is a footnote, not progress on #203: plan itself admits StripL implies nothing about the 2D question; forum shows Filaseta–Finch–Kozek-style finite-family constructions are already part of the page's context (Woett citation); veljjanoski already analyses "strip Z_N × Z_d" configurations (the l-periodic version).
- (a) Residual G2 step ("kill if StripL already published") could NOT run — WebSearch budget exhausted; the #859 failure mode risk stands unresolved.
- (e) Companion quantity L*(N,P_N) infeasible: complete factorization of 2^d−1 for d|N up to N=55440 needs factoring numbers with thousands of digits — not achievable, and not our edge.
- (e) Budget rests on weak pilot evidence: one heuristic implementation, incomplete pool; L=2 failed at N=5040.
- (b) Core method is within edge (CRT/SAT/DRAT/kernel decide), but the "L* locates where difficulty starts" framing is weak given known obstructions concern the l-periodic case.
- (d) Statement pinning correct.
- Net assessment: exclusion rule applies; fallback target is low-value, non-edge (infeasible factoring), high collision risk.
- Adjusted value: low; confidence: high.

---

### #1056 (slot 2)

**Pinned statement.** For k ≥ 2, is there a prime p and consecutive intervals of integers
such that the product over each of the k intervals is ≡ 1 (mod p)? Known examples: k = 2
with p = 11 (3·4 ≡ 5·6·7 ≡ 1) and k = 3 with p = 17 (Makowski 1983). The Noll–Simmons
variant asks for k equal factorials q₁! ≡ … ≡ q_k! (mod p).

Main statement and Noll–Simmons variant are equivalent (main(k) ⟺ NS(k+1), derived and
numerically checked in G2).

**Known state.**
- k=2 example (Erdős letter 1979); recorded as Guy A15.
- k=3 example, Makowski 1983; primepuzzles.net credits Makowski/Narkiewicz with K=3,4 and K=7,8,9.
- OEIS A060427: smallest prime for n contiguous strings, computed to n=14 (p=10428007), unchanged since Andersen 2007.
- No theorem gives any lower bound on M(p) (max multiplicity of n! mod p) beyond small fixed values; adjacent literature (Klurman–Munsch, Garaev–Luca–Shparlinski, Hu 2026 arXiv:2608.01781) bounds distinct values, wrong direction.
- Abramov arXiv:2604.26429 (2026, unrefereed, 7 revisions): claims M(p)≥2 for all p>5.

**Site/AI-claim status.** 9 comments; 0 proof claims; "Currently working on: jeffhino" — excludes under standing rule. JSP-000876 bounty (mislabeled "Erdős #876") drawing multiple invalid submissions; two open PRs (#2279, #3526) still invalid.

**Plan.**
- Target: T1 — determine a(15) exactly (OEIS A060427 extension) via O(p) sweep; T2 — Lean-convention L(k) table for k=1..15; T3 — M(p) distribution vs Poisson prediction (data only).
- Method: segmented sieve, Barrett/Montgomery multiply-mod, bucketed counting.
- Kill criteria: priority already posted; throughput >8ns/element/core; validation disagreement; sweep reaches 8e7 with no hit; resource conflict with owner's memory-protection process.
- Budget: ~6–10 agent-hours; 6–60h background CPU wall time.
- Value: low (plan's own rating).

**Skeptic's findings.**
- (f) HARD RULE VIOLATION, decisive: page shows "Currently working on: jeffhino"; forum (fetched) shows jeffhino has posted nothing, so collision cannot be checked from outside — a pure brute-force computation is exactly the kind of task that could silently collide.
- (f) Crowded venue: octavioalberto/Woett (3 Jun 2026) already posted an infinite "4 equal factorials" family with Lean; KentaKitamura restated k≤14 witnesses; JSP bounty traffic including 2 open invalid PRs.
- (c) Not new in method: Rivera Prime Puzzles #27 quotes Andersen (2007) describing exactly this per-prime table computation; the sweep adds only 19 years of hardware.
- (b) Plan openly abandons stated edge: no certificate design, no LLM proof search, only brute-force CPU sweeping (explicitly a non-edge); minimality has no short certificate.
- (b/e) Anyone with a consumer GPU can do this faster; the resulting record is fragile.
- (e) Budget optimistic on this box: machine shows ~3GB available RAM with swap already in use; realistic thread count is 3-4, giving 15-45h at median and 50-150h at 90th percentile — breaches kill criterion (b).
- (e) Poisson calibration rests on 2 data points and ignores Wilson-pairing correlation structure, likely pushing the true tail beyond the 8e7 kill ceiling more often than the stated 3%.
- (d) Statement pin essentially correct (main(k) ⟺ NS(k+1) confirmed, L(2)=5 confirmed).
- (a) Literature on the multiplicity itself genuinely thin (not a #859-type loss), but priority risk is from private/unposted computation, which no check can rule out; Trudgian 2014 (missed by G2) is a large related computation.
- Bottom line: excluded by rule; fallback target is a non-edge, memory-constrained, high-collision brute-force job.
- Adjusted value: none; confidence: high.

---

### #624 (slot 2, facet of the same problem)

**Pinned statement.** Compute exact values of H(n), the least m for which some f : 2^[n] →
[n] has f(2^Y) = [n] for every |Y| ≥ m, for n as large as SAT allows.

Two variants distinguished: H_L (Lean/erdosproblems convention, f on ALL subsets, no
f(A)∉A condition) versus H_EH (original Erdős–Hajnal convention, f on proper subsets with
f(A) ∈ [n]∖A).

**Known state.** Same primary sources as slot-1 #624 (Erdős–Hajnal 1968; Gyárfás 2013
survey; erdosproblems.com/624 Alon results; recent AI rounds all UNRESOLVED with no
computed values). No paper, preprint, OEIS entry, or repository computes exact values of
H(n) — OEIS lists it as "possible" (no sequence exists).

**Site/AI-claim status.** 2 comments (unread); 0 proof claims; no working-on marker for
this facet as of the G2 check (though the slot-1 facet later surfaced trureturing #9861 and
JSP PR #635 activity on the same underlying problem).

**Plan.**
- Target: T1 — certified table: H_L(n) for n=1..11, H_L(16)=H_L(17)=5 (so H_L(2^k)=k+1 for k=1..4); H_EH(n) for n=2..12 (so H_EH(2^k)=k+1 for k=1,2,3). T2 (checkpoint 2) — decide (16,5)_EH and (12,4)_L. T3 (stretch) — structured witness for (32,6)_L.
- Method: SAT (bundled CaDiCaL) with monotonicity/top-set-elimination/symmetry-breaking lemmas; LRAT certification for UNSAT cells.
- Pilot evidence (unverified, single session): (11,4)_L SAT; (16,5)_L, (17,5)_L SAT; (7,3)_L, (5,2)_L UNSAT; various EH-variant cells.
- Kill criteria: checker disagreement; public posting of n=11 witness before release; 150 CPU-hours without deciding C1/C2; LRAT proofs uncheckable within 48h; C3 memory/time overrun; primary-source EH-definition mismatch.
- Budget: ~3–4 agent-hours + 10–20 CPU-hours for checkpoint 1; +3 agent-hours + ≤150 CPU-hours for checkpoint 2.
- Value: medium.

**Skeptic's findings.**
- (d) Statement pinned correctly; H(0)=0, H(1)=0 confirmed by convention analysis.
- Core pilot claims survive independent check: skeptic wrote own bitmask checker (no shared code), confirmed 0 failures on (11,4)_L, (16,5)_L, (10,4)_L, (6,3)_L, (8,4)_EH, (4,3)_EH.
- (c) Novelty thinner than implied: forum thread (fetched) shows herong already published H(2..8)=1,2,3,3,3,4,4 and N(1..3)=2,3,6 plus an explicit 10-point witness for N(4)≥10 and a short proof of H(2^m)≥m+1 (18 Sep 2026) — with monotonicity this already gives H_L(9)=H_L(10)=4. Only genuinely new Lean-variant cell in T1(a) is H_L(11)=4; T1(b) new part is one (16,5)/(17,5) witness.
- (d/c) T1(c) overclaims: pilot never established (11,5)_EH or (12,5)_EH as SAT; local search on (12,5)_EH ended in failure — plan's own step 4 lists it as still to do.
- Framing of decisive cell C2 is wrong: N_EH(5) itself is unknown (could be 10 or 11); should bisect n=11..16 before spending 100 CPU-h on n=16 directly; same logic applies to C1.
- (e) Budget for UNSAT outcomes unrealistic: these are pigeonhole-like problems, exponentially hard for CDCL; pilot's (7,3)_L already produced 500MB of LRAT in 178s with weak symmetry breaking; box has ~4GB available RAM and the owner's memory-protection process running; certified UNSAT for C1/C2 realistically ~25-35% likely; recommends cutting 150 CPU-h to ~30 CPU-h gated on bisection.
- Soundness risk flagged in symmetry-breaking (L5) combination of colour precedence + point cubes, needs a written composability proof; plan budgets no review for this.
- (c) Value ceiling: site says finite computation cannot resolve #624; Problem-7 remark only contradicts a literal (likely non-intended) small-k reading.
- (a) Literature-gap check inconclusive (WebSearch budget exhausted); no evidence of a missed paper found.
- (f) Active work: herong (7 days ago, explicitly targeting n=11), possible JSP PR #635 resubmission, trureturing #9861 opened today, llm-hunter rounds 09-23 — but no proof claim or working-on marker for this specific facet.
- Verdict: do not refute the cheap checkpoint 1 (~3–4 agent-h, ≤20 CPU-h) — sound, within edge, gives a small new certifiable table; required re-scope: fix T1(c) claims, replace C2 target with an N_EH(5) bisection, cap checkpoint 2 at ~30 CPU-h, credit herong up front, drop "Problem-7 false" framing, drop C3.
- Adjusted value: low; confidence: medium.

---

### #389 (slot 2)

**Pinned statement.** Is it true that for every n ≥ 1 there is k ≥ 1 with
n(n+1)⋯(n+k−1) ∣ (n+k)(n+k+1)⋯(n+2k−1)? Mehta computed the minimal k for 1 ≤ n ≤ 18 (for
example, k = 207 at n = 4, checked in-file with native_decide IsLeast).

`erdos_389 : answer(sorry) ↔ ∀ n ≥ 1, ∃ k ≥ 1, ∏_{i<k}(n+i) ∣ ∏_{i<k}(n+k+i)`. Variant
`mehta_four`: IsLeast {k | ...} 207, proved via native_decide + interval_cases.

**Known state.**
- Erdős–Straus 1977 raised the boundary case, settled n=1, called n=2 "much more difficult."
- Ulas 2013 (appendix Schinzel): positive answer for each n≤20 (companion Erdős–Graham question settled for n≤9).
- OEIS A375071: exact minimal k known for Lean n=1..27 (Mehta Aug 2024 through n=18; Sharvil Kesarwani extended a(19)-a(26) March 2026).
- FAR (arXiv:2608.16977, Aug 2026): relaxed density-1 result, explicitly states it says nothing about #389's boundary case.
- llm-hunter GPT-6 Astra (23 Sep 2026): easy obstruction (each n≥2 has infinitely many bad k); marks UNRESOLVED, ~10% complete.

**Site/AI-claim status.** 11 comments; 0 proof claims on page (unsupported off-site "solved" PR #3882 with no reference, closed 2026-09-23); "Currently working on: SharkyKesa" (Sharvil Kesarwani) — excludes under standing rule.

**Plan.**
- Target: T0 — Kummer-digit criterion (reusable); T1 — kernel-checked existence proof for n=1..27 (no native_decide), citing but not claiming minimality except optional T1b; T2 (stretch) — new existence witnesses for Lean n=28,29 (and beyond).
- Kill criteria: G2 finds Lean existence proof for n≥5 already merged/open; T0 formalization not closed after 8h; a(27)+ appears on OEIS/page (drop T2); benchmark extrapolates to >3 CPU-days per n; no T2 witness by C≤2e14.
- Budget: ~8–12 Opus-agent-hours to first checkpoint.
- Value: medium.

**Skeptic's findings.**
- (f)+(a) DECISIVE, both T1 and T2 already superseded: fetched the forum thread directly — existence witnesses already posted for Lean n=28..35 (Leandre Jack, 04 Sep 2026), with least-k proven exact for n=28,29 via exhaustive scan (code at github.com/leandrejack-afk/erdos-computations); skeptic independently re-checked witnesses for n=28,29,30,32,34,35 with own Legendre/Kummer certificate test — all pass.
- (f) Hard-rule exclusion stands: page still shows "Currently working on: SharkyKesa" and "Working on formalising: Etalides741," which collides directly with T1.
- (c) T1 is not new mathematics: existence for n≤20 (Ulas–Schinzel), exact least-k through n=27 (OEIS), existence through n=35 (forum) all already public; Kummer-digit criterion is textbook and already implicit in existing solvers per forum comments (Zeraoulia Rafik, Leandre Jack); Tao (31 Mar 2026) already posted the structural change-of-variables link to #396/A375077.
- (b) Only path to new content beyond n=35 is a large-scale sieve race (our non-edge); growth ~10× per pair of n; competitors with dedicated solvers already posting there; plan's own risk 4 concedes the method dies past n≈31, already passed by others.
- (d) Statement pin correct; digit-formula and corollaries independently verified.
- (e) Budget technically plausible for T1 but spent on a result with no external value now.
- Net: every component superseded, non-novel, or excluded by working-on/formalising markers. No residual publishable deliverable. Recommends always reading /forum/thread/N comments, not just page counts — same failure class as #859.
- Adjusted value: none; confidence: high.

---

### #1074 (slot 2) — dropped at G2, no plan/skeptic

**Pinned statement.** EHS numbers: m ≥ 1 for which some prime p ∣ m!+1 has p ≢ 1 (mod m).
Pillai primes: primes p ∣ m!+1 with p ≢ 1 (mod m) for some m ≥ 1. The density questions are
open. The stated initial segments (EHSNumbers_init: S begins 8, 9, 13, 14, 15, 16, 17, …,
and the Pillai-primes analogue) are left as `sorry`.

**Known state.** Pillai (1930s) asked; Chowla answered (14!+1≡18!+1≡0 mod 23). Hardy–
Subbarao 2002 prove both S and P infinite and suggest density heuristics (~0.5 for EHS,
0.5–0.6 for Pillai, "no reason not to tend to 1" — neither proved). Luca–Shparlinski 2005 /
Li Lai 2021 cover the largest-prime-factor question, not this. OEIS A064164/A064295/A063980
give exact finite data (a(20)≥140 for the complement sequence). Two public kernel-checked
Lean proofs of EHSNumbers_init already exist (williamjblair/lean-proofs, 2026-08-22;
conjectures-io contribution, 2026-09-01).

**Site/AI-claim status.** 5 comments (unread); 0 proof claims; working on: None. An
unsupported "solved" PR (#3882, Gemini 3 Flash, no proof) was closed 2026-09-23.

**G2 verdict: SUBSUMED.** The proposed slot-2 deliverable (kernel-checked EHSNumbers_init
and PillaiPrimes_init) already exists publicly and is part of the DeepMind FC100SolvedSet1
benchmark, attracting many AI pipelines. The density questions need analytic control of
factorial-distribution heuristics (Cobeli–Zaharescu Poisson conjecture), outside the stated
edge, with no certificate target. Other leftovers (formalizing PillaiPrimes_infinite;
resolving whether 140 is an EHS number, which needs factoring a 242-digit number; extending
the Pillai-prime table) are low value, already attempted, or large-scale compute. Dropped
before plan/skeptic stages.

---

### #91 (slot 2) — dropped at G2, no plan/skeptic

**Pinned statement.** For each n, is an n-point planar set that minimises the number of
distinct distances unique up to similarity? The file tags the small cases as solved but
leaves them as `sorry`: unique for n = 3 and n = 5 (Kovács 2024), non-unique for n = 4, 6,
7, 8, 9.

**Known state.** Underlying quantity f(n) (OEIS A186704) known for n=1..13; Guth–Katz /
Erdős lattice bound asymptotically. Erdős–Fishburn 1996 give g(k) and all k-optimal
configurations for k≤4, settling n=3,5,7,9. Shinohara 2008 proves the maximum planar
5-distance set (12 points) is unique, giving UniqueMinimizer 12 by combination — a fact
missing from the erdosproblems.com page remarks. Wei 2012 proves g(6)=13 with ≥3 optima.
Balaji et al. arXiv:1911.11688 (2019/2023) restates/corrects the Erdős–Fishburn tables.
Kovács arXiv:2412.05190 (2024) settles n=5 uniqueness by Gröbner/elimination computer
algebra (not a Lean proof).

**Site/AI-claim status.** 7 comments (unread); 0 proof claims; no working-on marker.
Contributors listed: Neel Somani, Terence Tao, Desmond Weisenberg. Four llm-hunter attempts
all UNRESOLVED and trivial.

**G2 verdict: SUBSUMED.** Every small n for which f(n) is known (n≤13, except g(7)
undetermined) is already settled in the literature by combining Erdős–Fishburn, Shinohara,
Wei, Kelly, and Kovács. For n≥14 even f(n) is unknown because g(7) is open — a hard
classification problem, not a finite certificate job. The only remaining work is Lean
formalization of already-known results (no open PR exists), which is formalization rather
than new mathematics, and is limited further by the no-community-PR rule. Dropped before
plan/skeptic stages.

---

### #340 (slot 2) — dropped at G2, no plan/skeptic

**Pinned statement.** Greedy Sidon sequence A = (1, 2, 4, 8, 13, 21, …). The main question
is whether |A ∩ [1, N]| ≫ N^{1/2−ε}. The file states greedySidon 2 = 4, 3 = 8, 4 = 13, 5 =
21 and 10 = 97 as bare `sorry`; their earlier native_decide proofs were removed.

**Known state.** Mian–Chowla 1944 define the sequence. Stöhr 1955 gives a_k ≤
(k−1)^3+1, i.e. |A∩[1,N]| ≥ N^{1/3}-type lower bound; general Sidon upper bound √N+O(N^{1/4})
(Erdős–Turán 1941, Lindström 1969). O'Bryant's 2004 survey (DS11): growth of the Mian–
Chowla sequence "not well understood." Cheng, J. Number Theory 266 (2025): generalizes to
linear forms but per zbMATH review has no new result for the x1+x2 (Mian–Chowla) case.
erdosproblems.com states only the trivial ≫N^{1/3} bound. 33 ∈ A−A remains undetermined;
absent from the first 100,000 Mian–Chowla terms (OEIS A080200, May 2026).

**Site/AI-claim status.** 0 comments on the fetched page; 0 proof claims; no working-on
marker. llm-hunter attempts (GPT-6 Astra Ultra, GPT-5.2 Pro, both committed 2026-09-25)
reach only the trivial (2N)^{1/3}−1 bound; both UNRESOLVED.

**G2 verdict: SUBSUMED** (for the proposed slot-2 target specifically). The bare-`sorry`
value lemmas (greedySidon 2=4, 3=8, 4=13, 5=21, 10=97, and _22_mem_sub) are already the
subject of an OPEN maintainer PR: google-deepmind/formal-conjectures PR #6156 (mo271,
2026-09-18), "Restore native_decide proofs dropped during modulization," which restores
exactly these proofs. The main asymptotic question (N^{1/2-ε}) is CLEAR on priority (0
comments, 0 claims, no working-on marker, thin/stalled literature since 1955) but is not a
finishable deterministic slot-2 target — no known method controls the greedy dynamics'
exponent, and the only finite side-question (33 ∈ A−A) can only be settled positively by
further large-scale search, which is a non-edge. Dropped before plan/skeptic stages.

## 4. Ranker's Dropped Summary

Sources checked: the Lean files; problems/erdosproblems/data/problems.yaml (all 75 still
'open' in the local snapshot); problems/ai_contributions.md (the AI wiki, frozen at
2026-06-30); and our notes/selection/thin_screen_0908.md, which records proof claims and
'working on' markers. No web.

**Hard gate: an existing claim or people working on it.** #1063 (2 claims, rickyc
working), #817 (1 claim, SamKorsky), #872 (1 claim, 36 comments, and 3 AI-wiki partials),
#361 and #400 (two people working each, per our dashboard), #538 (claimed full solution by
Star Fleet Math). #535 and #100 were already rejected on 09-08 because their frontiers are
sunflowers and Guth–Katz.

**AI-wiki partials, very likely with claims, so collision risk:** #11 (incorrect claim;
also a 2^50 compute race), #36 (AlphaEvolve and GPT-5.5; Haugland literature), #51, #124
(Aristotle partial), #188 (GPT-5 partial; the frontier is Tsaturian 2017, not the file's
10^7), #396, #503, #513, #602, #686 (Tao, van Doorn and others), #931, #1054, #1084, #1209.
Also #1062: Damek Davis posted a partial in April 2026. On shape it was a top slot-1 fit
(Lebensold's bracket 0.6725–0.6736), so re-admit it only if G2 shows no claim.

**Famous or hard-frontier, or the #859/Grimm trap:** #10 (sieve), #41, #155, #156 (Sidon
asymptotics), #195/#196/#197 (monotone-AP permutations; now ≤4 by Adenwalla, and the
infinite constructions are not finite-certifiable), #406 (powers of 2 in base 3), #701
(Chvátal's conjecture), #849 (Singmaster), #850 (Erdős–Woods), #1052 (sixth unitary perfect
number), #141 (CPAP-11 compute), #213 (integer-distance n = 8 compute), #1142 (2^44
compute), #552/#567/#569 (active Ramsey literature), #65 was kept but #80 dropped
(extremal graphs), #98 (not formalisable), #257 (the main question is deep; Erdős 1948
base case already formalised externally), #291 (Shiu, Wu–Yan; p-adic analytic), #373
(Surányi; well-searched literature), #452, #479 (many OEIS sequences, literature not
thin), #680/#681/#683/#887/#1060/#1106 (analytic or sieve frontiers), #509/#513 (complex
analysis), #33 (van Doorn active, recent upper bound), #170 (sparse rulers; thick
computational literature and a 2019 lower-bound improvement).

**Weak partial-result value:** #1055, #1059, #1108, #452.

**#885 (k = 5):** a certificate would be finite, but it needs 4N_i + d_j² to be a square
for every entry of a 5×5 grid. That is a high-genus Diophantine problem (Bremner needed
elliptic curves for k = 4), so the frontier is algebraic geometry.

**Caveats:** #624 appears twice on purpose (slot-1 bound and slot-2 SAT table), so there
are 15 distinct problems. #930, #243 and #727 each carry an explicit G2 precondition in
their entries. Every pick still needs a fresh G2 on the live erdosproblems page (claims,
'currently working on', forum) before dispatch, because the local AI-wiki snapshot is three
months old.

## 5. Unreachable Sources

Collected across all G2/plan/skeptic passes (deduplicated by cause):

- **erdosproblems.com forum/comment threads.** The one-page-per-problem rule meant the
  problem page itself was fetched, but the separate `/forum/discuss/N` or
  `/forum/thread/N` pages were generally NOT fetched during G2, leaving comment text
  unread for #757 (7), #883 (3), #889 (2, later fetched in plan stage), #727 (7), #624
  slot 1 (2) and slot 2 (2), #243 (8, later partly surfaced via search snippet and later
  fully fetched by the skeptic on #243), #930 (1), #203 (15), #1056 (9, later fetched by
  the skeptic — revealing the decisive jeffhino/octavioalberto activity), #389 (11, later
  fetched by the skeptic — revealing the decisive n=28-35 witnesses), #1074 (5), #91 (7),
  #340 (0 on fetched page). This gap directly caused missed decisive information at least
  twice (#1056, #389), confirmed by the plan/skeptic stage re-fetching those threads.
- **WebSearch session budget (200/200) exhausted** partway through the G2/plan passes for
  #203, #930 (partially), #243, #340, #1074, and others, cutting off residual literature
  gates that several plans explicitly required before proceeding (e.g., #203's "Residual
  G2" first step, #889's RST/Tijdeman/Langevin check).
- **Primary paywalled/inaccessible papers:** Erdős–Hajnal 1968 scan (no OCR tool
  installed); Gyárfás–Lehel 1995 (ScienceDirect paywall); Duverney 2001 (venue unverified);
  Erdős–Straus 1977 (not fetched, known via FAR quotation); Balakran 1929; Makowski 1983;
  Guy UPINT B27 and A15 full text; Skałba 2003/2019 (academia.edu/ResearchGate/
  worldscientific 403s); Pomerance 2026 (Integers); Shinohara 2008 and Wei 2012 (EJC, not
  fetched, known via Balaji et al. secondary citation); Erdős–Fishburn 1996 (Elsevier DOI
  redirect not followed); Cheng 2025 J. Number Theory (ScienceDirect 403, zbMATH review
  used instead); Jia 1988 (Chinese journal, MathSciNet inaccessible); Ramachandra–Shorey–
  Tijdeman 1975/76 and related omitted-terms papers (IMPAN/matwbn 403s, exact constants
  unverified).
- **arXiv export API** returned HTTP 406/429/empty from this sandbox repeatedly across
  multiple problems, degrading systematic recent-preprint coverage; web search and direct
  WebFetch of abs pages were used as fallbacks.
- **Dynamic/JS-rendered trackers:** the Erdosproblems-llm-hunter live site (loads via JS,
  did not render "Loading..."); checked via GitHub repo/code search instead, which was
  itself rate-limited (HTTP 403) for several repos (erdos-release-index, vibemathed) at
  various points.
- **MathSciNet, Google Scholar citation graphs, Zulip/Mathlib chat search:** not accessed
  in any pass (no credentials / not queried).
- **mathoverflow.net and some Springer/Wiley author pages:** blocked by fetch-tool domain
  restrictions or auth redirects (e.g., MO question on Erdős distance n=12; Springer
  Gyárfás–Prömel–Szemerédi–Voigt 1985).
- **global-memory `recall_presets`:** the tool was not available in these subagent
  sessions and so was not called, contrary to the AGENTS.md instruction to call it before
  a task.
