# automath restart — strategy update (2026-09-25)

Written by the Fable 5.1 coordinator on restart. Sources checked today: Quanta (2026-08-03),
`ubmids/erdos-verification-gap` (251 proof claims 07-14→09-24, data pulled 09-25),
`jaredwilder/erdos-release-index` (peer operator, 09-11→09-18), erdosproblems.com pages
708/859/377, claude.ai usage page.

## 1. What the landscape looks like now (numbers, not vibes)

- erdosproblems.com: 1,217 problems, 565 solved / 652 open (Quanta, 08-03).
- **The acceptance funnel is nearly closed.** Of 224 claims on open problems: 108 got any comment,
  42 any verdict, 31 verified, **9 accepted by moderators (4%)**. 133/251 have zero comments.
  P(no verdict at 60 d) = 81.7%; median wait among still-waiting claims = 53.4 d.
- **By model family (verified %):** GPT-other 19.4, GPT-5.6 18.7, **GPT-6 Astra 4.2**,
  **Claude/Fable 0.0 (n=5)**. Our Astra-as-workhorse choice was wrong by this data.
- **Lean does not buy acceptance:** with Lean 11.3% verified vs without 16.1%.
- Number theory claims verified 12.6% (n=111); graph theory 20.0% (n=40).
- Most new results come from hobbyists/undergrads on public models, not labs (Bloom). The #1
  failure mode is missing existing literature (Barreto, #333, solved by Erdős 1977).
- Site rules now: AI use must be disclosed; every claim independently human-verified before posting.

## 2. Where we actually stand

- #708 claim = `claim_id 262`, kind=partial, verdict=`other`, accepted=False, **`lean_url` empty,
  `lean_discussed=n`.** Our kernel-verified `g(n) ≤ 12n` is invisible in the record. Fixable.
- #708 / #859 / #377: all three still have `Currently working on: None`. Lines are ours.
- Peer comparison: Wilder runs broad-shallow (30+ repos, 8 exact finite bounds, 79 Lean decls
  over 15 problems, no failure record). We run deep-narrow (one problem to 12n, full ledger
  including our own mistakes). Complementary, not competing.

## 3. Strategy changes

1. **Stop optimising for moderator acceptance.** It is a 4% lottery with 81.7% silence. Optimise
   for the *verifiable public record*: GitHub (now `chy4pro/automath`, public) + Zenodo + Lean.
   Submit one clean claim per problem and move on.
2. **Lean is our quality gate, not our sales pitch.** Keep kernel verification as the internal
   red line; do not expect it to move reviewers. **Amended 2026-09-25 (owner):** Lean comes
   last — formalise only a result that is big enough to be worth verifying, after referee and G2.
   No Lean infrastructure work (rebuilds, CI, import trimming) before such a result exists.
3. **Fix the concrete miss:** claim 262 must link the Lean (`lean/proofenv/Erdos708/`). Owner
   action (site login), text supplied below.
4. **Engines: Claude only, tiered.** Fable coordinates and judges (scarce: 75% of weekly pool
   used, resets Sat 00:00). Opus executes proofs/referees. Sonnet/Haiku for extraction and
   mechanical checks. Every dispatch names its tier.
5. **Keep the two-slot portfolio, add Wilder's lesson to slot 2:** small exact finite results
   (tables, bounds with certificates) are cheap, verifiable, and publishable — good filler for
   the deterministic slot when the deep slot is waiting on a gate.
6. **G2 discipline stays absolute.** It is the single failure mode the whole community keeps
   hitting; ours already caught four of my own briefing errors.

## 4. Immediate queue

- [ ] Independent Claude-side referee of the #859 effective chain (A4 explicit A, B′ θ=0.8896,
      Codex's qualitative partial summation). Dispatched to Opus 09-25. Gate before any write-up.
- [ ] Owner: edit claim 262 → add `lean_url`.
- [ ] After referee: decide #859 publication scope (a *new bound on a new problem* → Zenodo yes,
      X no — not kernel-verified). No "first proof" wording; G2 not done on the qualitative route.
- [ ] Slot 2: pick one small exact-result target from the thin-literature screen.

## 5. Owner text for claim 262 (copy-paste, no AI wording added)

> Update: the g(n) ≤ 12n bound is kernel-verified in Lean 4 (v4.34.0-rc1, Mathlib de5ce8a9).
> Source and FinalCheck (axioms frozen to propext/Classical.choice/Quot.sound):
> https://github.com/chy4pro/automath/tree/main/lean/proofenv/Erdos708
