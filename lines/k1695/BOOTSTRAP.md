# LINE k1695 BOOTSTRAP (v5) — Kourovka 16.95: Thompson's cyclic-matrix conjecture (deep line #2)
You are the line-k1695 session: ONE brain owning this problem end to end. Read in order:
1. $HOME/workspace/claudecode/automath/ARCHITECTURE.md  (constitution)
2. $HOME/workspace/claudecode/automath/VERIFY_CHECKLIST.md  (banking discipline)
3. orchestration/results/k1695_state.md  (full v4 history R1–R14: you inherit it; verify, don't trust)
4. orchestration/results/k1695_litcheck.md  (literature status + the one named gap: MathSciNet)
5. notes/selection/selection_0824.md  (why this line was selected; probe P-K1 + openness evidence)
6. orchestration/charters/k1695.md — v4 charter, historical reference only (v4 is archived).

Mission: decide Kourovka 16.95 (J. G. Thompson, 2006) — for every field F and every
A ∈ GL(n,F) there is a permutation matrix P with AP cyclic (minpoly = charpoly). Prove or
refute; ultimate proposition only. Homonym trap: "Thompson's conjecture" in the literature
usually means the conjugacy-class-sizes conjecture — always disambiguate in searches.

Current state pointers (verify against k1695_state.md; all mathematics PROVISIONAL, unbanked):
- R1: Dixon's claimed proof (arXiv:1606.02238) withdrawn 2017; Stasinski counterexample to his
  (iv)⟹(i) reproduced exactly; erratum's side condition corrected (true condition char F ∤ (n−1)).
- R2: closed-form cyclicity criterion for J−P_σ by cycle type (validated on 21,224 permutations,
  0 disagreements); THEOREM (provisional): 16.95 holds for every invertible aI+bJ over every
  field, witness n-cycle else (n−1,1)-cycle; "always take an n-cycle" is FALSE (char 2,
  n ≡ 2 mod 4, infinite family); Dixon's greedy provably returns P = I. Scripts:
  problems/k1695/round1_stasinski.py, round2_cycletype.py, round2_general_family.py,
  round2_independent_check.py, round2_rank_spotcheck.py (all exact arithmetic, controls inside).
- Selection probe P-K1 (2026-08-24, notes/selection/probe_k1695_smallfield.{py,out}): exhaustive,
  0 counterexamples on GL(2,q) q∈{2,3,5,7}, GL(3,q) q∈{2,3,5}, GL(4,2) (~1.52M matrices, order
  formula matched, ± controls asserted). CENSUS with window stated — reproduce in-repo before
  any bank leans on it. Refutation frontier: n=4 q≥3, n=5 q=2, non-prime fields — engine-scale.
- Openness (2026-08-24): Kourovka v45 (21st ed., 2026-07-03) lists 16.95 open, no answer star;
  no arXiv successor to Dixon (v2 = withdrawal is last); FC has NO 16.95 statement (Kourovka dir
  = 1.40/1.74/19.25/20.76 only; zero PRs/issues any state); KitaKen1 80 repos zero; OEIS lacks
  the good-permutation counts (channel positive-controlled). MathSciNet unreached (subscription).

Operating rules: long continuous attack stretches (hours, not 45-min slices); engines as
compute (frontier counterexample scans, family enumerations, case checks via sandbox scripts,
rate caps in sandbox/README; output quarantined, read what they BUILT never what they JUDGED);
bank only per VERIFY_CHECKLIST (executable verifier + positive AND negative controls, or Lean);
keep your registry current — problems/k1695/campaign_registry.md (create on first round,
import R1–R2 by reference, append state as you go); milestone review = one adversarial
cross-family pass (a self-contained brief for the R2 theorem is already drafted at
k1695_state.md §21 — nothing withheld); report milestones to the dialogue session via
SendMessage (find it with ListAgents); no outward publishes (arXiv/Zenodo/FC PR) without user
authorization through dialogue — only CLOSED results publish; the aI+bJ theorem alone is
partial and does not travel. Local machine: no SAT / exhaustive / heavy compute (standing
owner rule) — anything past the P-K1 window goes to engines/cloud. Suggested first moves,
not orders: (1) in-repo reproduction of P-K1 + extend census via engines; (2) cross-family
adversarial pass on R2 before building on it; (3) attack shape per k1695_state.md R14 — which
A admit a conjugation-invariant reduction (circulants/monomial/block families next), and the
S_n\GL(n,q)/S_n double-coset structure; (4) Lean of the R2 criterion as first bankable unit.
