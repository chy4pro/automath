# Owner rules digest (standing instructions, 2026-08-23 → 2026-10-09)

Paraphrased in English from the owner's instructions over the life of the project, for the Paperclip coordinator
and every agent that needs the project's operating doctrine. The owner's own words are not reproduced here.
Authority order: AGENTS.md → OPERATIONS.md → this file → strategy notes → ledger. When a later instruction from the
owner arrives (via the chat session or a Paperclip comment), it overrides this digest; add it here afterwards.

## Mission and posture
- Mission: a fully autonomous pipeline that proves things about open problems; the objective is many × valuable ×
  efficient results. Decide and act; do not ask the owner routine questions. Reflect every ~6 hours and at every
  milestone or failure (what was decided, cost, outcome, what to change).
- Do not underestimate AI. "Hard for humans" is not a reason to skip a target; the only disqualifiers are: the target
  is already known (G2), the source was misread, or nobody cares (zero attention). Push attackers: assume a complete
  proof exists, no escape hatches in briefs, no "this is open" prior, no literature in the clean room.
- Metrics are diagnostics, never targets. Idle engines are a symptom: first ask whether real work is undispatched,
  whether the candidate pool is thin, or whether verification is the bottleneck. Never invent tasks to look busy.
  Idle free engines may try high-value long shots ("gacha"), but every claimed hit goes through the full gate.

## Selection
- Two slots: one hard, high-value target; one high-certainty, quickly closable target. Practical relevance raises
  priority. Attention (citations, named proposers, follow-up work) measures importance, not mere presence on a list.
- Selection v3 (2026-09-26): slot 1 = a famous problem × a quantitative frontier × at least two combinable machineries
  × verifiable output × a named untried lever. "Thin literature / elementary only" is not a filter. One target at a time.
- Order of checks before any engine hour: pin the exact statement from the primary source; importance bar; G2 novelty
  (arXiv, site comments and forum, open PRs, Zulip, OpenAI's 2026-10-06 catalogue); tool fit (partial results must be
  meaningful: explicit bounds, finite-range theorems, reductions); verifiability.
- Literature is read only to confirm the problem is open and to locate the frontier. Attacks are clean-room: fresh
  context, no web, no papers, no campaign files; the coordinator compares clean-room output with literature-aware
  route reports and never feeds the latter to the clean room.
- Lesson of round 4 (2026-10-09): probes launched without a concrete candidate lemma rediscover known saturated
  relaxations. Prefer targets with an identified omitted constraint or a lemma whose refutation by the known relaxations
  has been checked and does not apply.
- LLM reasoning is the main solver; SAT/ILP/Gröbner are verification aids, never the attack engine. Solvers run only on
  GitHub Actions and only for important results; none on the local containers.

## Engines and cost
- Subscriptions only; no API-key billing, no paid cloud (GCP retired), no new dependencies without approval.
- Dispatch at the calibrated model tier; a result from a lower tier is void. Astra (gpt-6-astra) takes only the hardest or
  most critical tasks, single agent per brief, no hard time limit in the brief (the real limit is the weekly pool).
- Quota is scarce: no exploratory fan-outs; one background run at a time unless a chain is in progress; routine ticks
  do nothing unless something happened.
- Never stop a web-model run that is still thinking; "stuck" means an error or an ended run with no output, never elapsed time.

- Full speed (2026-10-09 17:40Z, after the infrastructure repair — real session resumption, test residue cleaned,
  disk freed): the project runs at full speed again; the selection round continues under the coordinator's own
  procedure without pausing to save. Both Codex concurrency slots are to be kept busy wherever real work exists;
  verifier and referees run in parallel as needed. A surviving lemma goes to the probe and then to a campaign
  approval request; no survivor means the catalogue is widened and the next round opened. Standing rules and the
  approval gates are unchanged (so "full speed" never means inventing tasks, skipping gates or outward actions).

## Reporting
- Report facts, not model self-claims. Every result report states: what exactly closed and whether it is the easy end
  of the problem; the true size of the remaining gap; whether G2 was done (no "new"/"publishable" wording otherwise);
  cost and output ratio; blockers reported as blockers.
- Status words first: PROVED / HIT / PARTIAL / OPEN / PASS / PASS-WITH-REPAIRS / FAIL / DONE. Never claim a conjecture
  solved for a bound or a restricted case; an exponent with an unspecified constant is not an effective theorem.
- To the owner: concise Chinese. Internal notes, code and briefs: English. Grade every result when reporting:
  announce-worthy / important milestone / small result, with the reason.
- Everything that reaches the owner's Paperclip inbox is Chinese (2026-10-09): approval requests (title, grading,
  reason, proposed action), decision cards (questions and options), @-owner comments, and the titles and closing
  summaries of issues the owner must look at. Child-issue titles and briefs for other agents stay English.
  Procedure in notes/PAPERCLIP_PLAYBOOK.md §9.

## Publication gates
- Three gates before anything leaves the repository: two independent cross-vendor referees, G2 novelty, finite checks;
  Lean only when the result is worth it (then GitHub Actions, no local builds).
- Publish when a method reaches its limit: closed theorems go out, exploration moves on. Each milestone gets the full
  set (GitHub with everything needed to verify and refute, Zenodo paper, X post) — but only milestones: at most one
  Zenodo version per problem per day, X only for announce-worthy results, one erdosproblems.com proof claim per problem
  (concept DOI; no per-version comments). Small results: Zenodo + GitHub only, no X, no site claim.
- Outward actions (X, site claims, e-mails, moderator messages, community PRs) are proposed to the owner with the grading
  stated first; the owner decides. No Mathlib or other community-repo PRs from the pipeline. Posted X posts are never
  deleted or edited; one post per result, English, plain language, no provocation, written as a person proud of the work.
- After publishing, release what is no longer needed (regenerable inputs, raw certificates once the trimmed core is
  verified and uploaded, old bundles); no private archives; temporary backups are deleted once verified.
- Public repository privacy: no local paths, chat/session links, cloud ids, e-mail addresses or quoted owner chat;
  commits carry Co-Authored-By only; grep before every push.

## Orchestration (Paperclip, from 2026-10-09)
- The Paperclip coordinator agent is the coordinator. The chat-side session relays owner instructions, maintains the
  infrastructure and reports; it does not select, brief, judge or grade. Method prescriptions in a task description
  from the session side are suggestions.
- Delegate everything: literature → scout; proofs → attackers (clean room); review → referees (cross-vendor); finite
  checks → verifier; Lean → formalizer. Comments to the owner in Chinese, short; long content in files.
- Reports to the owner live at the reports site (Chinese pages); they compile the coordinator's own conclusions.
