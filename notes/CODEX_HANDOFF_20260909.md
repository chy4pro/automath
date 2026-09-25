# automath — Codex handoff review

**Superseded operating state:** the owner subsequently transferred operation to Codex.
Use [OPERATIONS.md](OPERATIONS.md) and [the takeover review](CODEX_TAKEOVER_REVIEW_20260909.md)
for current ownership and verification. The text below is retained as the pre-transfer snapshot.

Review date: 2026-09-09, approximately 04:25 CDT / 09:25 UTC. The project is live; this is a dated knowledge handoff, not a transfer of operating control or a frozen proof release.

## Executive state

The active project is `$HOME/workspace/claudecode/automath`, not the parent workspace as a whole. The running Claude process was located by its working directory. The parent workspace and automath root are not Git repositories; the #708 publication checkout is a separate nested repository.

The project is an LLM-led mathematics research portfolio. Current work is on Erdős #859; #708 has a published partial bound and is idle; #377 is a secondary candidate with its main target still open. Historical ETP677 / k1695 infrastructure and cloud campaigns are not the current operating model.

**Operating ownership has NOT transferred.** The existing Claude coordinator explicitly retains both solver seats and its armed `ScheduleWakeup`. Codex did not create another loop, dispatch research, stop processes, publish, delete conversations, repair the watchdog, or change mathematical sources. The coordinator was told that read-only handoff checks do not suspend its pre-existing authorized workflow.

## Read these first

1. This review, including its verification limits and corrections below.
2. [Claude's handoff](CODEX_HANDOFF_20260909_FROM_CLAUDE.md), **especially Appendices A and B**. The initial sections contain statements superseded by those appendices and by outputs arriving during this review.
3. [Questions sent to Claude](CODEX_HANDOFF_QUESTIONS_20260909.md), which document the evidence and reasons for the corrections.
4. [Live ledger](../lines/DIALOGUE_STATE_0829.md). New entries are inserted **before** the `- 12:3x CHROME RESET` anchor, not simply appended at EOF. Its filename and opening date are misleading.
5. [Complete scoped documentation index](CODEX_DOCUMENT_INDEX_20260909.md): 2,272 files / 57,959,358 bytes in the input snapshot, including 35 Claude project-memory files. This is an inventory, not 2,272 full semantic reviews.

## Current mathematical state

| Line | Safely reportable state | What remains |
| --- | --- | --- |
| Erdős #708 | Local materials record `g(n) <= 12n` for all n as Lean kernel-verified; the cached `FinalCheck.lean` entry point was successfully rerun in this review. The `11n` result is recorded as refereed, not formalized. | The original `2n` conjecture is not solved. Formalizing `11n` would be a distinct milestone. No restart was requested here. |
| Erdős #859 upper bound | Local README and referee report give the logarithmic upper bound with Erdős–Ford exponent `delta = 0.08607133205593431`. The comparison constant has a confirmed typesetting error; see below. | Correct the written multiplication sign before reusing the formula. Claude repaired the numerical script during the handoff; Codex then reran it with exit 0. |
| Erdős #859 lower bound | The elementary chain is `d_t >= A(t)^2 / B(t)` and `B(t) <= S(t)`. A5 delivered an independent same-family review of the effective B bound; Claude subsequently reviewed the report. Codex reran its rational certificate successfully. | B has same-vendor verification, not cross-vendor clearance or a kernel proof. A4 has just produced a candidate effective fallback for A; it must not be promoted from solver output to an accepted theorem without review. |
| Erdős #377 | Round 1 did not close the requested explicit parameter triple. The local record identifies a limit/label correction in EGRS Theorem 4. | Primary target open; no active seat reported. Do not relabel the correction as a solution of #377. |

### #859: what changed during this handoff

Definitions and proofs live in [README](../problems/erdos859/README.md) and [LOWER_BOUND](../problems/erdos859/LOWER_BOUND.md). Keep the domains intact: A and B use practical integers in `(t,2t]`; B is an **ordered** pair sum including the diagonal. Density statements refer to the original integer parameter problem; intermediate estimates may hold for every real t.

**A5 delivered.** [The report](../engine/harvest/erdos859_verifyB_astra.md) marks all six requested checks CORRECT and gives

`B(t) <= S(t) <= 19,200,096,768 * (log t)^theta` for every real `t >= 2`,

where `theta = 1 + log(3349/4000)/log(5) = 0.8896306804161379...`. This is stronger than the stated coefficient 20,000,000,000. Codex read the report and executed its exact rational checker and a rejecting negative control. These reproduce the analytic numerical certificate; they do not by themselves certify every external theorem, derivation, or hypothesis in the proof. This is an independent Astra run, not a cross-vendor referee or a Lean kernel certificate. In Appendix A Claude had not yet read the report; in the later Appendix B it records reviewing the argument's scope and spot-checking the coefficient arithmetic. Its updated status is **verified within one vendor, cross-vendor mathematical review outstanding**, not fully cleared.

**A4 produced a new candidate while the review was closing.** Its [live report](../engine/harvest/erdos859_explicitA_astra.md) now claims the permitted fallback

`A(t) >= 2^(-4,000,000,000) / (log t)^(101/100)` for every real `t >= 1024`.

The exact exponent-1 target remains unresolved. Combining the candidate with the effective B bound would yield raw density exponent `2.9096306804161379...`; the report also claims `d_t > (log t)^(-73/25)` from the explicitly named but enormous onset `exp(2^(1,000,000,000,000))`. Treat all of this as **solver-claimed, pending mathematical acceptance**, not as a newly verified result of this handoff. Codex did not rerun A4's certificate: its entry point writes the weights JSON used by the active run, and the coordinator still owns that work. No need to touch or rerun an active producer's files for the purpose of a knowledge handoff.

**Existence versus effectivity versus priority.** Claude accepted that its earlier framing was wrong: the qualitative asymptotics `A(t) asymp 1/log(t)` and `S(t) asymp (log t)^delta_W`, together with the elementary reduction, suggest a qualitative density exponent `2 + delta_W`, approximately 2.7136, without the effective machinery. Its appendix also admits that the needed partial-summation transition to the dyadic S sum has not been fully written and checked. Thus:

- Do not treat “explicit exponent” as equivalent to “explicit coefficient and onset.”
- Do not claim the qualitative shortcut is newly certified by this review; its remaining link needs a proof check.
- Do not inherit “first proof.” Priority has not passed a targeted literature/G2 check, and an empty proof-claim page is not a novelty certificate.
- A4's justified objective is quantitative effectivity, with any loss in exponent stated explicitly.

## Defects and operational risks found

| Priority | Finding and evidence | Disposition |
| --- | --- | --- |
| High | Watchdog recovery is nonfunctional. `logs/heartbeat` contains `Sat Aug 29 13:26:30 CDT 2026`, while `tools/watchdog.sh` lines 19 and 35 require an epoch integer. Its launchd log repeatedly reports arithmetic errors. Claude confirmed no successful revival is recorded in the watchdog log. | **Not repaired.** Its revival prompt also points at the old ETP677 campaign. Repairing it in place could launch another coordinator; first design and record a single-owner transfer/recovery protocol. |
| High | `LOWER_BOUND.md` labels the effective theta theorem “verified,” but Claude admits it had only checked reductions, sampled values, and the producer's verifier, not the Section 4 proof. | A5's report has now arrived, but the old label's provenance was too strong. Distinguish producer claim, referee report, numerical certificate, coordinator acceptance, and kernel proof. |
| High | Earlier lower-bound sections continue to recommend a B target refuted by the later Section 4d. The original handoff also overstates novelty and conflates qualitative and effective bounds. | Preserve historical derivations, but add clear supersession markers before reusing them as briefs. No source changes made here. |
| Medium | Written `84^delta = 9.013845138057405` is false: `84^delta = 1.4642838801857625`. Claude confirmed the intended expression is `8 * 4^delta = 9.013845138057405`; its own range argument supplies that product. A literal upper bound with `84^delta` is not safe to quote. | Correct notation in the #859 README and referee report when a change is authorized. The intended derivation, not the erroneous literal formula, survives this check. |
| Resolved during handoff | The initial `python3 problems/erdos859/check859.py` run exited 1 because the later duplicated calculation called `math.exp(1000)` and overflowed. | Claude subsequently changed the two offending loops to use `L = log t` directly, disclosed in Appendix B. Codex inspected the revised source and independently reran the full script with exit 0. This was Claude's edit, not a Codex source change. |
| Medium | Dashboard source last updated 2026-09-08 14:40 local and omits the current #859/#377 developments. Dispatch registry has old headings, repeated identifiers and historical RUNNING rows despite Claude reporting no live web tasks. | Use dated ledger entries, outputs and live process checks. Never infer a currently running job from the registry alone. Dashboard was not republished. |
| Medium | #859 and #377 are local-only according to Claude; the published Git checkout contains #708. Historical publish directories/readmes are not a single synchronized release record. | Do not assume new work is backed up by the #708 remote. No remote fetch, push or publication was performed. |

## Processes, ownership and recovery

The observed interactive coordinator was Claude PID 1307, Terminal window 28, selected tab `/dev/ttys000`, cwd automath. These are observations, not permanent identifiers; re-resolve them before any future interaction.

| Seat | Screen session observed | Purpose | Handoff-time state |
| --- | --- | --- | --- |
| A4 | `2185.codex` | Effective A lower bound / permitted fallback | Report growing; fallback claimed near the review cutoff; acceptance pending. |
| A5 | `61406.codex_b` | Independent review of effective B bound | Report delivered, six CORRECT verdicts; Codex replayed rational checks. |

Use full screen IDs: bare `codex` is ambiguous. An additional Spark process was not identified as either of these tasks; neither it nor the existing memory-protection process was terminated. No inputs were sent to solver screens by Codex.

Claude says its `ScheduleWakeup` is armed for approximately 04:52 local and is rearmed once per tick. This is a coordinator-reported state, not independently verified through a scheduler API. If that session exits without rearming, there is currently no functioning automatic recovery behind it.

Any future operating transfer must be explicit in the ledger: outgoing Claude stops its wakeup and records the stop, then the incoming owner may establish one replacement loop. This review did **not** request or perform that transfer.

## Rules and authority to preserve

Current user instructions and task scope come first. The latest applicable owner-feedback files in [Claude project memory]($HOME/.claude/projects/-Users-user-workspace-claudecode-automath/memory/MEMORY.md) explain the historical operating rules; they are not permission to expand this read-only handoff into new research or publication.

- Chinese, concise and evidence-calibrated communication to the user; internal research documentation is English. Global-memory presets were recalled for automath/project handoff; four pending requirements were left unapplied and no memories were changed.
- Single-agent solver briefs; Astra for the hardest/critical tasks. Do not inherit old “fill all seats” or broad fan-out instructions. Quota/reset figures expire and must be checked live.
- Two-slot portfolio and methods-first proof work; no new heavy SAT/cloud campaign merely because the old infrastructure exists.
- G2 checks occupancy, exact original statements, adjacent problems/aliases, existing claims and literature before expensive research. Exact quantifiers and index sets belong in briefs. Never label a given PROVED without an auditable basis.
- Separate empirical tests, ordinary mathematical review, same-family independent review, cross-vendor review, and formal kernel verification. Partial results are not solved original conjectures.
- GCP retired on 2026-09-04. Old billing grants, launch plans and quota tables are historical, not current authorization.
- Zenodo versions only for a real headline bound/kernel milestone or necessary correction; no automatic per-version publishing. X only for kernel milestones, at most one thread/problem/day, not for constant changes or corrections. These record the established policy, not a publication action approved by this handoff.
- No Mathlib/community PRs; community/moderator communications are owner-controlled. Do not send historical cleanup queues or community drafts automatically.
- Preserve hot Lean/Mathlib caches and unrelated work. Do not print secrets, reuse retired infrastructure, or install dependencies merely to satisfy old instructions.
- Root `ARCHITECTURE.md` describes the old v5 per-line coordinators; that topology is not instantiated now. Vendored `problems/formal-conjectures/AGENTS.md` is upstream policy, not automath-wide policy.

## Verification performed by Codex

| Check | Observed result | Limitation |
| --- | --- | --- |
| `LEAN_PATH=. $HOME/.elan/bin/lake env lean Erdos708/FinalCheck.lean` from `lean/proofenv` | Exit 0, no output; the expected axiom guards passed. | Existing cached build, not a clean rebuild or second Lean implementation. |
| SHA-256 comparison of `Statement.lean` and `FinalCheck.lean` in `lean/proofenv/Erdos708` versus `problems/erdos708/repo/lean/Erdos708` | Both corresponding file pairs identical. | Only these two source entry points were hash-compared, not the entire dependency tree. |
| `git status --short --branch` in the #708 repo | Clean, `main...origin/main`; local HEAD recorded as `8b9c1c1`. | Remote-tracking state only; no network fetch or live release verification. |
| `python3 engine/harvest/erdos859_verifyB_astra_check.py` | Exit 0, `CERTIFIED q = 3349/4000`; coefficient 19,200,096,768. | Exact rational numerical/analytic certificate, not the complete surrounding theorem formalized. |
| Same checker with `--q 8372/10000` | Exit 1, explicitly REJECTED because the certified value at 47/20 exceeds q. | Expected negative-control failure, not a test-suite regression. |
| Direct calculation of `84**delta` and `8*4**delta` | Reproduced the notation discrepancy and the intended 9.013845138057405 value. | Does not independently referee the whole upper-bound argument. |
| `python3 problems/erdos859/check859.py` | Initially exit 1 / OverflowError. After Claude's repair, Codex's fresh rerun exited 0 and printed all three tables. | Floating-point sanity diagnostics, not a proof certificate for every real parameter. |
| Watchdog source, heartbeat, launchd configuration and logs | Human-readable heartbeat conflicts with integer arithmetic; repeated failures corroborate Claude's diagnosis. | No repair/restart or simulated recovery was attempted. |

## Documentation coverage and remaining reading

Focused reading covered the root architecture/selection/verification documents; current owner-feedback and project-memory entry points; recent ledger material; #859 README, LOWER_BOUND, active briefs and the A5 report; #377 current README; #708 statement/axiom-check entry points and publication overview; recent primary-source-selection notes; cleanup classification records; and Claude's complete handoff plus its corrective appendix. Selected long files, including historical pipeline state, the #708 README, verification-doctrine compilations and old line bootstraps, were read in relevant sections rather than exhaustively.

The index mechanically scanned the eligible files for metadata, headings and hashes. **Older dispatch/harvest reports, archived orchestration rounds, all PDF pages, and every historical proof were not read individually end to end.** They must not be treated as audited merely because they appear in the index. Upstream dependency/vendor documentation and sibling projects were deliberately excluded. If an archived line is restarted, its exact statement, latest accepted result, counterexamples and certificates need a fresh focused review first.

## Concrete next decisions, not actions already taken

1. Let the existing owner harvest and grade A4/A5; the handoff should not create a competing referee/dispatcher loop.
2. Before reusing #859 claims, reconcile the typo, obsolete/refuted target headings, acceptance labels and effectivity/priority framing. Write out the qualitative partial-summation link if that shortcut is pursued.
3. If operating control is to move, agree and record the transfer before repairing or replacing recovery. A watchdog with a stale dispatch prompt is not a safe fallback.
4. Refresh the dashboard from accepted ledger state and decide an explicit backup location for local-only research. Publication remains separately gated by the established milestone and permission rules.

Files added by Codex for this handoff: this review, the scoped index, and the questions file. Claude separately created its handoff, appended the exchange to its running ledger, and repaired `problems/erdos859/check859.py` after receiving the defect report. Existing research outputs continued to change under their original owner. The index predates these final live updates; its modification times and hashes intentionally describe its stated snapshot.
