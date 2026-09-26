# automath — current operating record

Updated 2026-09-25 by the Fable 5.1 coordinator on restart (previous: 2026-09-09 Codex). This file is the current entry point;
dated handoff documents and old ledger sections retain their historical meaning.

## Ownership

- Coordinator: **Claude Fable 5.1 session `457116fb-0921-45cf-974f-013eece5c1dc`** (restart 2026-09-25, owner instruction). The 09-09 Codex coordinator ran one day; no Codex CLI exists in the container.
- Working root: `/work` (container). Public main repo: https://github.com/chy4pro/automath (per-problem repos as submodules).
- Transfer authority: the owner's direct instruction to take over the remaining work, plus
  outgoing Claude's explicit stop/transfer in [handoff Appendix C](CODEX_HANDOFF_20260909_FROM_CLAUDE.md).
- Outgoing Claude session `457116fb-0921-45cf-974f-013eece5c1dc` is handoff-only. Its final reply
  at 04:56 CDT reconfirmed no wakeups, dispatches, research edits or publication.
- No second coordinator may be started by repairing the legacy Claude watchdog.

## Current portfolio and work

| Line | State | Next useful gate |
| --- | --- | --- |
| Erdős #859 | **Closed 2026-09-25 (subsumed).** Referee found no error; G2 then found the upper bound in Hughes arXiv:2609.25446 (2026-09-21) and an exponent-1 lower bound in Pollack–Thompson 2013 / Weingartner 2015, stronger than ours. See problems/erdos859/CLOSURE_20260925.md. | None. No publication, no priority claim. Slot 1 is empty pending the 09-25 selection pass. |
| Erdős #708 | Published partial result, idle. Cached FinalCheck rerun passed during handoff; 12n kernel-checked in the recorded setup, 11n not formalized. | A real new bound or kernel milestone, not another supporting-section version. |
| Erdős #377 | Parked (see STATUS_SWEEP_20260925.md): D2 Theorem 4 correction, D3 barrier uncertified, D1 empty. | Referee D2 or supply the missing prime estimate; no campaign planned. |
| **Slot 1: Zaremba explicit M** (campaigns/zaremba-M/, started 2026-09-26 ~03:5x UTC under selection v3) — Shkredov 2026: Zaremba for all large primes with M = 2^2000; numerics show the true spectral gap is 2^-1 vs proven 2^-1658; target log2 M ≤ 500 by a new lemma (announce-worthy), ≤ 150 strong; 27.5M-token campaign, Phase 0 (negative list + machinery map + K0 collision) running as a workflow; K1 checkpoint at ~h18. | Phase 0 → SUMMARY.md → Fable K0/K1 decision → Phase 1 routes R2/R3/R4 with isolated referees. |
| Erdős #889 (former slot 1) | Selected 2026-09-25 (selection_20260925.md): effective finiteness of {n : v₁(n)=1} via an elementary reduction + Matveev; skeptic re-derived the maths; novelty vs Ramachandra–Shorey–Tijdeman 1975/76, Tijdeman 1974, Langevin unresolved. Kitamura (KitaKen1) proved the capital-V₁ variant in Lean on 09-22 and named lowercase v₁ as open — collision risk accepted (owner 09-25: active work is not a disqualifier). | Level 2 DONE and published as a small result (Zenodo 10.5281/zenodo.22962744; no X, no site claim — owner rule). **Level 3 PARKED 2026-09-25** (round 1: OPEN; the level-2 counting method provably fails on property-(P) integers; needs a new idea — see level3/ROUND1.md). Slot 1 empty pending a new selection pass. Previously: **Line continues: level 3** (some k ≤ C log n with v(n,k) ≥ 3 for all large n = first step past Erdős–Selfridge 1967 on the main conjecture v₀ → ∞). Gate: G2_LEVEL3_20260925.md (Opus, dispatched). CLEAR → Opus attack campaign (extend Lemma R to two large primes per term + multi-log Matveev; fallback RST block-product counting), kill after ~6 agent-hours without a reduction lemma. |
| **Slot 2: Erdős #624** | Selected 2026-09-25: certified small-value table H_L(n), H_EH(n) by SAT with independent checkers, re-scoped per the skeptic (credit herong; only certified cells; cap 20 CPU-h). Value low, cost low. | Checkpoint 1 DONE (certified table, forum reply posted). Checkpoint 2 CANCELLED 09-25 (owner: no local solvers; solvers only on GitHub Actions and only for important results). Line parked with the table as its result. |

### Worker seats

At the approximately 04:55 CDT takeover sweep, both screens showed completed jobs and idle prompts:

- `2185.codex`: A4 completed in 20m05s, `engine/harvest/erdos859_explicitA_astra.md`.
- `61406.codex_b`: A5 completed in 11m53s, `engine/harvest/erdos859_verifyB_astra.md`.

Use full `pid.name` IDs; bare `codex` is ambiguous. Neither was redispatched by the initial
takeover pass. No web research task was reported still running. Recheck before future input.

### Work already taken up by Codex

See [the takeover review](CODEX_TAKEOVER_REVIEW_20260909.md).

1. Accepted ownership and independently established the two worker completion states.
2. Read the final A4 report and its independent verifier; reran all 401 rational matrix rows,
   negative controls, six A(t) values and finite arithmetic checks with exit 0.
3. Reran A5's rational contraction certificate with exit 0.
4. Corrected the upper-bound transcription to `8*4^delta`, with an editorial provenance note.
5. Marked refuted lower-bound targets historical, qualified the review labels, and removed
   unsupported first-proof/exact-unit-coefficient inferences from the active problem notes.
6. Wrote [the missing qualitative partial-summation argument](../problems/erdos859/QUALITATIVE_LOWER_BOUND.md).
   It also corrects the theorem's `<<` hypothesis and the missing dyadic `log 2` coefficient.

## Verification queue

- Effective B proof: independent Astra review delivered; full cross-vendor review remains pending.
- A4 fallback and density consequence: exact checks reproduced, local review recorded; external
  mathematical review remains pending. The exact exponent-1 A target is still open.
- Qualitative derivation: written from two checked primary-source theorems; independent review
  pending, no numerical onset or novelty claim.
- A question has been sent to the owner about one independent Claude referee session. Do not
  treat the pending question as permission. The outgoing handoff conversation is not the referee.
- **Engines on restart: Claude only** (Fable coordinates; Opus executes; Sonnet/Haiku mechanical). No Codex/Astra/ChatGPT seats. Strategy: notes/STRATEGY_RESTART_20260925.md. Historical note — genuine non-OpenAI alternatives included Anthropic or Qwen, but a current login/model check is
  required. ChatGPT Pro, Astra and Spark are all OpenAI and do not diversify the vendor.

Do not keep improving an arbitrary constant solely because a seat is idle. First finish the
verification and source/priority gates, then select the most useful next proof objective.

## Continuation and recovery

**Current state (2026-09-25): continuation mechanism = `CronCreate` inside the Fable coordinator session, TESTED.** A one-shot job scheduled 11:28Z fired at 11:33Z (ledger entry "TICK-TEST fired"). Properties: session-only (dies with the session, not on disk), fires only while the REPL is idle, recurring jobs auto-expire after 7 days and must be re-armed; the coordinator records each armed job here. Lean policy (owner 2026-09-25): Lean only for a result worth verifying; the #708 FinalCheck container rebuild is dropped from the queue. **2026-09-26 02:4x: ALL scheduled jobs cancelled by the owner; no tick armed; continuation only on the owner's instruction.** Previously: tick f43f4e60 (with disk check). **Resource caps (crash lesson 09-25):** ≤ 2 solver processes and ≤ 3 background agents at any time; every solver under `ulimit -v 2000000 -f 3000000` + `timeout`; no DRAT logging on exploratory runs; delete uncertified proof files immediately; stop all runs if free disk < 20 GB. Previous: Production tick RE-ARMED 2026-09-25 ~17:00Z: CronCreate job 04afc142 (replaces d1edc358), hourly at :07, 7-day expiry (re-arm by 2026-10-02); prompt = read notifications, check in-flight agents, act per gates, **战报 check (dashboard notes/automath-dashboard-src.html → Artifact b3511490…, every milestone and at most 2 h between publishes when anything changed)**, one ledger line if changed. Task notifications (subagents, workflows, background commands) are the primary wake signal; the tick is the fallback.
The old Claude `ScheduleWakeup` was explicitly stopped. The legacy launchd watchdog was
disabled and unloaded at 05:11:40 CDT, with both states verified; its script and plist were
retained. It contained a broken heartbeat parser and obsolete `claude --continue` / ETP677
revival prompt. See [the reversible retirement record](LEGACY_WATCHDOG_RETIREMENT_20260909.md).

Do not silently recreate a background agent, self-message a second coordinator, or write an
old heartbeat into a working format that could accidentally activate the legacy launcher.
Record and test any replacement continuation mechanism before claiming unattended operation.
Routine research sweeps should be quota-efficient (normally around 60 minutes, or on meaningful
task completion), not a high-frequency screenshot/polling loop.

## Standing publication and privacy gates

- New research is not automatically a paper/version. While a line is iterating, accumulate notes.
- Zenodo: only a changed proved-and-refereed headline bound, a kernel milestone, or correction of
  a published claim. No new version merely for a referee report or supporting section.
- X: kernel milestones only, at most one thread/problem/day; no constants/corrections spam.
- GitHub is the continuous research record, but do not push private/internal material or mix
  unrelated problem lines into the #708 repository. #859 and #377 are currently local-only;
  their destination and privacy-safe export scope must be established before any new remote write.
- No new Mathlib/community PRs and no AI-authored moderator/community communications.
  Exception, one-time, owner-authorized 2026-09-25 in the coordinator chat ("[owner message redacted]"): a single DM
  reply to the erdosproblems.com moderator in the existing 04 Sep thread, asking to update the #708
  claim summary to the 12n result and add the Lean link. Text fixed by the coordinator (Fable 5.1);
  a Sonnet browser subagent may send it verbatim. This does not create a standing permission.
  Second one-time exception, owner-authorized 2026-09-25 ("你来发吧", after the coordinator independently re-verified the witnesses): one forum comment on erdosproblems.com/624 replying in the existing thread with the certified small values; text fixed in notes/forum_624_comment_20260925.txt; a Sonnet browser subagent may post it verbatim.
- Do not put the owner's private email, keys, login tokens, internal session dumps or unrelated
  personal conversations into a publication. **2026-09-25 scrub (owner: rewrite, it is not project content):** the public repo was rewritten from a single root; never commit local paths (`/Users/...`), chat/session links (chatgpt.com/c/…, claude.ai/…session…), GCP ids, e-mail addresses, quoted owner chat, arXiv text extracts, or GCP scripts. Commit trailers carry `Co-Authored-By` only, no session link. Pre-push grep: `roychen|chatgpt\.com/c/|claude\.ai/.*session|gmail|chenhaoyu1995`. Do not read/print engine-key files to prove access.
- Owner-only pending items from handoff: account data export/deletion choice, Prove2Me key rotation,
  and whether to obtain additional Lean checker implementations. None authorizes automatic cleanup.

## Reference map

- [Original Codex document review](CODEX_HANDOFF_20260909.md): dated pre-transfer snapshot.
- [Claude handoff and corrections](CODEX_HANDOFF_20260909_FROM_CLAUDE.md): Appendices A–C supersede its opening sections.
- [Documentation index](CODEX_DOCUMENT_INDEX_20260909.md): 2,272 files indexed at its stated snapshot;
  indexed does not mean fully read or mathematically audited.
- [Historical ledger](../lines/DIALOGUE_STATE_0829.md): newest entries are before `- 12:3x CHROME RESET`.
- [Dashboard source](automath-dashboard-src.html): still stale; update only with explicitly qualified results.
- Existing owner-feedback sources remain under
  `$HOME/.claude/projects/-Users-user-workspace-claudecode-automath/memory/`.
  Latest feedback supersedes old full-speed fan-out/cloud/publishing directives.

## Known access limitations

Global-memory recall for the takeover timed out and yielded no new terminal notice; no preset
was changed. The web lookup tool later returned a revoked-token error; public paper downloads
still worked. Do not conflate a failed connector with authorization to use credentials elsewhere.
