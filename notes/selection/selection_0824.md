# SELECTION 0824 — deep-line slot #2 (v5, SELECTION.md gate v2)
Task: pick most valuable ~1-week-attackable problem; write lines/<line>/BOOTSTRAP.md.
Started 2026-08-24. Working notes, appended incrementally.

## Inputs digested so far
- ARCHITECTURE.md v5, SELECTION.md v2, VERIFY_CHECKLIST.md — read.
- TARGETS.md (669 lines, full): catalogue pool AUDITED OUT — six S0/S1 gates, zero GO.
  Final ranking: Agrawal 81 (HOLD) > Erdos307 ~79 > Kourovka20.76 72 (HOLD) > Erdos699 45
  (HOLD) > Kaplansky 37.5 (DROP) > Erdos982 31.5 (HOLD) > LonelyRunner 27 (DROP) >
  Erdos617 12 (DROP) > Erdos779 2.8 (DROP).
- orchestration/results/agrawal_A1_probe.md: A-1 probe RAN (08-22): FAIL decisively at 1e8;
  102/102 cells fail; X=1e9 excluded by ceiling arithmetic (needs x13.65 > pi(X) growth x8.67).
  Hegde-Devaraj kernel NOT bypassed. Verdict: DROP, not back to pool head. => Agrawal is DEAD.
- SOURCING FIX (user directive, applied 08-23): field arm mandatory. field_sweep_batch1.md:
  274 named conjectures, 12 areas. field_sweep_r1..r14 + gate_batch_fieldswept_r1.md exist.
- notes/case_intel/recalibration_ytd.md: cscK YTD disproof (arXiv:2608.19301) — AI-assisted
  counterexample construction reached top-tier named conjecture. Kind-1 construction targets:
  solvability prior RAISED. Kind-2: NOT raised (6 systems incl. Fable-5 failed even handed
  the counterexample). Disjunctive targeting = valuable pattern. certkind mandatory.

## Implications for this selection
- Do NOT re-audit the dead catalogue pool. The live input = field-sweep arm + mined staging.
- Prefer: named conjecture, Kind-1 certificate shape (finite witness / machine-checkable),
  construction-type, non-crowded, verifroute (a) or (b); disjunctive bonus.
- Avoid collision with line-677 (ETP finite implication).

## Next steps
1. Read gate_batch_fieldswept_r1.md + field_sweep_batch1 + skim r1-r14 heads.
2. Read notes/case_intel/cases.md + miss_analysis_ytd.md for class priors.
3. Shortlist ~5; probes first (cheap, minutes); structured openness checks on top picks.

## Landscape after full evidence pass (checkpoint 2)
Three v4 lines were orphaned by the v5 transition (ARCH_REVIEW_fresh.md: "k1695, zc1a7, tdn:
opened 08-22/23, early rounds, nothing external"). All three have REAL measured assets (S-5):

1. **tdn** (arXiv:2606.27961, transversal difference number delta((Z/p^2)^2,pG)=(2p-1)^2):
   - Assets: problems/tdn_2606_27961/* (12 scripts+outs). 4 rounds. R4 provisional THEOREM:
     one 2-direction anywhere forces the box; p=3 case FULLY proved by hand; trichotomy
     0/1/2 on 2-carrying lines with 1- and 2-branches closed. ONLY the 0-branch open
     (|A_w|>=3 for all w; shortfall 8 at p=5, 24 at p=7).
   - S1 duplication checks already run (tdn_S1_duplication.md, tdn_sands_szabo_check.md).
   - Weakness: 影响力 2.0 — 2-month-old paper's internal invariant, 0 citations.
2. **k1695** (Kourovka 16.95, J.G. Thompson 2006: for every A in GL(n,F) there is a
   permutation matrix P with AP cyclic):
   - Named: Thompson (Fields medalist), numbered Kourovka problem, 20 years old. Openness
     verified at PRIMARY source (Kourovka v45 = 21st ed 2026-07-03, no answer star; Dixon's
     only claimed proof arXiv:1606.02238 WITHDRAWN 2017 after Stasinski's counterexample
     to his Prop (iv)=>(i)).
   - Assets: problems/k1695/round1_stasinski.py + round2_*.py (4 scripts). R1: reproduced
     Stasinski counterexample, corrected the erratum's side condition (char不整除(n-1), not
     char!=2). R2: closed-form cyclicity criterion for J-P by cycle type (21,224 perms,
     0 disagreements), THEOREM: 16.95 true for ALL invertible aI+bJ over every field
     (410 exhaustive rows), obvious "take n-cycle" rule refuted (infinite family char 2,
     n=2 mod 4), Dixon's greedy provably returns P=I.
   - Gate batch 3 ranked it TOP GO of 145-candidate field-swept pool.
   - Both directions live; refutation = Kind-1 finite certificate (an A over small field
     where all n! products fail — seconds to verify).
3. **zc1a7** (ZC1 Zassenhaus for A7): named, single open HeLP case (2,-1) order 4;
   litcheck OPEN. But the sourcing paper's own lattice method already failed on it;
   proving non-existence is beyond-HeLP hard; refutation search space enormous.
   Lower P(week).

Gate batch 3 GO-2: 1903.02866 covering radius non-hollow simplices (<= d/2) — ranked below
16.95, evidence points TRUE. GO-3: 2412.03500/07 twisted derivations inner-ness. Gate batch 4
GO-2: 1604.06765 Balodi–Palcoux dual Euler totient (proved for A_n/S_n by Lucchini et al.
FoM Sigma 2020; residual open). Gate batch 2 HOLDs with unrun probes: Fici–Saarela abelian
squares (112.5, probe B-1 best 157.5), 2608.17771 F_q-points formula (105, probe I-1 best 140).

## Preliminary judgment (to be validated by probes + fresh openness checks)
Owner doctrine (08-16): named/famous first, ultimate proposition, believe AI capability.
Score = significance x P(week-solvable), judged.
- k1695 = the only candidate that is BOTH named/famous (Thompson, Kourovka) AND carries
  measured attack assets AND has a Kind-1 refutation certificate AND zero crowding
  (Aristotle's Kourovka sweep took 8 problems, skipped 16.95; Dixon unrepaired 9 years).
- tdn = highest P(progress) but lowest significance; keep as runner-up.
- zc1a7 = named but methods-exhausted; runner-up #2.
PLAN: (a) read k1695_litcheck.md; (b) fresh structured openness checks (arXiv API since 07-03,
gh FC PRs, KitaKen1); (c) cheap probe: exhaustive small-field scan n=3 (F2,F3,F5), n=4 (F2[,F3])
of ALL invertible A x all n! P — materially updates BOTH directions (counterexample found =>
16.95 REFUTED = major; none => census evidence + narrows structure). Light, single process,
time-capped ~10 min.

## Probe P-K1 (run 2026-08-24, this task) — Kourovka 16.95 small-case exhaustive scan
Script/output: notes/selection/probe_k1695_smallfield.{py,out} (copied from scratchpad).
47.2 s wall, single process, hard limit 600 s, pure stdlib.
Populations EXACT (enumerated |GL| == order formula in every cell):
  GL(2,2)=6, GL(2,3)=48, GL(2,5)=480, GL(2,7)=2016, GL(3,2)=168, GL(3,3)=11232,
  GL(4,2)=20160, GL(3,5)=1488000.
Controls: negative (identity judged non-cyclic) and positive (companion of x^n-1 finds
a cyclic AP) asserted per cell — a failure would have aborted the run.
RESULT: **0 counterexamples in ~1.52M invertible matrices.** 16.95 holds on ALL of
GL(2,q) q in {2,3,5,7}, GL(3,q) q in {2,3,5}, GL(4,2). CENSUS (window stated), not proof.
Update: refutation frontier starts at n=4 q>=3 / n=5 q=2 / non-prime fields — engine-scale,
never local. Proof side unaffected; the R2 structural machinery is the live route.

## Openness verification (fresh, this task, 2026-08-24) — all structured channels
1. arXiv API (export.arxiv.org, throttled): id_list=1606.02238 -> v2 only, last updated
   2017-11-14 (the withdrawal); NO v3/successor. all:"16.95"+all:"Kourovka" -> 1 hit =
   Dixon's own withdrawn paper. all:"cyclic matrix"+all:"Thompson" -> 0. all:"nonderogatory"
   +all:"permutation" -> only Borobia-Canogar 2020 (excluded by litcheck). Recent
   all:"Kourovka" (12 newest, Aug 2026): active AI/human wave on OTHER problems
   (21.88 solved 08-04, 17.102 counterexamples 08-01, factorizations) — 16.95 untouched.
2. gh formal-conjectures: Kourovka dir = {1_40, 1_74, 19_25, 20_76}.lean — NO 16_95 file;
   code search 16_95 total_count=0; PRs ALL STATES matching kourovka (14 rows listed) — none
   touches 16.95; "cyclic matrix" PRs = []; issues "thompson" = Guralnick-Thompson,
   Feit-Thompson, BMV only (different conjectures; homonym trap noted).
3. gh repo list KitaKen1 (80 repos, full): grep thompson|cyclic|kourovka|matrix|derog ->
   1 name hit "poisson-n-lie-scalar-matrix" = false positive (unrelated Poisson n-Lie repo).
4. OEIS: good-permutation counts 5,14,74,264,2484(,13488) and 1,2,5,14,74,264 -> "No results"
   (REAL zero: channel positive-controlled same session, Fibonacci -> 104 hits). The R2
   counting object is absent from OEIS — novelty corroboration.
5. Carried from line files (verified to exist): Kourovka Notebook v45 primary source
   (2026-07-03) lists 16.95 open, no answer star (k1695_state.md §0); Aristotle 8-problem
   Kourovka sweep skipped it; zbMATH litcheck ~35 queries with positive controls found no
   repair/successor; Dixon's own CV lists paper withdrawn, no successor (k1695_litcheck.md).
   Named residual gap: MathSciNet behind subscription wall (LibLynx), unreached.

## DECISION (selection authority delegated, owner ruling 08-22)
**PICK: Kourovka 16.95 — J. G. Thompson's cyclic-matrix conjecture (2006) — as deep line #2,
continuing the orphaned v4 k1695 line and absorbing its assets.**
Line dir: lines/k1695/BOOTSTRAP.md (written this task).

Why (one page in the final report; skeleton):
- Value doctrine: named (Thompson) + catalogued (Kourovka, 20 yrs) + ultimate proposition.
  Highest fame among all currently attackable candidates: catalogue pool is dead (6 gates,
  0 GO; Agrawal killed by A-1), field-swept GOs rank 16.95 top (gate_batch_3 GO-1).
- P(week): real measured assets (S-5): problems/k1695/round1_stasinski.py, round2_cycletype.py,
  round2_general_family.py, round2_independent_check.py, round2_rank_spotcheck.py — closed-form
  criterion (21,224 perms, 0 disagreements), aI+bJ theorem (410 exhaustive rows), erratum
  correction. Problem shape = finite-certificate/constructive linear algebra — the class the
  case library says AI cracks now (cases.md; recalibration_ytd.md: Kind-1 prior RAISED).
- Crowding: zero on every channel (above), while the Kourovka notebook as a whole is an
  active AI harvest zone — the fame is real and the seat is empty. Timing argues for now.
- Verification: refutation = seconds-verifiable Kind-1 certificate; proof side already has
  self-written verifiers with genuine negative controls; Lean route (c) later; FC statement
  absent (fine per SOURCING FIX §2 — verifroute (b) now, (d) only as authorized outward act).

RUNNERS-UP:
1. tdn (arXiv:2606.27961): highest P(progress) — R4 leaves only the 0-branch of a proved
   trichotomy — but 影响力 2.0 (a 2-month-old paper's own invariant, 0 citations) caps
   significance; loses on the owner's named/famous-first doctrine. Natural next line when
   a slot frees; its assets stay live in problems/tdn_2606_27961/.
2. zc1a7 (ZC1 for A7): named (Zassenhaus) and single open HeLP case (2,-1), but the sourcing
   paper's own lattice method already failed on exactly that case, and the residual attack
   needs beyond-HeLP machinery (2-adic double cosets / full modular data) — P(week) low.
Also considered: gate_batch_2 HOLDs with unrun probes (Fici-Saarela 112.5/B-1; 2608.17771
105/I-1) — below 16.95 on fame with no assets; gate_batch_3 GO-2/GO-3 and gate_batch_4 GO-2
(1604.06765 dual Euler totient) — external and open but no momentum and lower name value.
