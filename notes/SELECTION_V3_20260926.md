# Selection strategy v3 — "famous problem, quantitative frontier, combine the machinery" (2026-09-26)

Owner, 2026-09-26: "你不能太保守，你要相信 AI 的能力，重新设计选题策略。" Reference cases: Anthropic's
critical-line proportion 41.6% → 67.2% (60 subagents, 31M output tokens, 54 h; two literature
machineries combined; isolated adversarial referees; notes/case_intel/cases.md 2026-08-10) and
GPT-6 Astra's prime-gap constant 246 → 186 (Maynard–Tao sieve re-optimised). Both are the same
recipe. v3 replaces the "thin literature, elementary frontier, small partial result" filter of
2026-09-25 for slot 1.

## 1. What a slot-1 target must look like
1. **Famous.** A named problem with real community attention (Erdős prize problems, classical
   constants, problems with active expert work). Attention is the point, not a risk.
2. **A quantitative sub-statement with a frontier number** — a bound, exponent, proportion or
   constant whose current record is known and dated (12n for #708; 67.2%; 186; Λ ≤ 0.2; …).
   Progress = the number moves. "Solve the conjecture" is never the campaign target.
3. **Rich literature with ≥ 2 machineries that can be combined** (explicit formula + operator
   theory; sieve weights + zero-density; LP duality + arithmetic certificates; …). Rich literature
   is an asset: G2's job becomes "map the machinery", not "check thinness".
4. **Verifiable output**: numerical optimisation with certified constants, explicit inequalities
   checked by exact/interval arithmetic, LP/SDP certificates, or a proof a referee can walk.
5. **A lever nobody has pulled**: a specific combination or re-optimisation that the literature has
   not tried (the campaign brief must name it; the skeptic must fail to find it in print).
Excluded only: pure compute races with no mathematical lever, and targets already under a
large-lab campaign in the same month (collision at 100× our budget).

## 2. Capability assumption
Opus/Fable operate research-level machinery (analytic number theory, sieve theory, additive
combinatorics, operator inequalities, LP/SDP). Analytic or heavy frontiers are allowed. The
09-25 "non-edge" list (flag algebras/SDP/analytic) is withdrawn as a filter; it survives only as
a cost estimate.

## 3. Campaign shape (one target at a time)
- Budget 20–30M tokens, 1–3 days, dozens of agents; Fable judges every claim and attacks directly
  when a route needs it.
- Phase 0 warm-up: parallel route explorers produce a **negative list** (what does not work and
  why) and a machinery map with the exact theorems to combine.
- Phase 1 routes: 3–6 route groups, each with a gap indicator ("the single inequality that would
  finish it"); budgets per route; routes die on evidence.
- Phase 2 verification: every claim gets 2–4 isolated adversarial referees with distinct attack
  briefs; numerics re-derived independently; constants certified.
- Phase 3 publication only if the movement is announce-worthy (owner rule); otherwise the
  negative list and partial machinery stay in the repo.

## 4. Slot 2
Constructions reachable by mathematical reasoning + light checking (no solvers), or nothing.

## 5. Immediate: candidate pass v3
One workflow: scouts over (a) Erdős prize/famous problems with numerical records, (b) classical
analytic constants with explicit optimisation frontiers (de Bruijn–Newman Λ, Linnik, Brun–Titchmarsh,
prime-gap constants, least nonresidue, zero proportions for other L-functions), (c) additive/extremal
combinatorics exponents and constants with LP/SDP/entropy machinery, (d) our own #708 gap
12n → 2n (window-adaptive LP + arithmetic route untried); rater + skeptic; output top 3 with a
campaign design each. Then commit to one.
