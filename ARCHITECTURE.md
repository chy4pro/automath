# AUTOMATH ARCHITECTURE v5 (2026-08-24)
Authorized by the owner after the fresh-eyes audit (orchestration/ARCH_REVIEW_fresh.md).
Supersedes orchestration/PROTOCOL.md v1–v4 entirely. The old orchestration layer is ARCHIVED.

## First principle (owner, verbatim intent)
AI is now powerful enough that many problems are in principle solvable by AI; this project
exists to solve them AT SCALE. Resources are limited; use them EFFICIENTLY.
Under v5: scale = pool breadth + serial closure rate; efficiency = scarce-model attention
concentrated where irreplaceable (deep attack, adjudication, target judgment).

## Topology: one session, one brain, per line
| session | model | role |
|---|---|---|
| `dialogue` (user's terminal) | Fable | User interface. Thin ops only: hosts pub-watch + arXiv-watch monitors, relays user directives, restart recovery, spawns selection tasks. NO planning layer, NO relay protocol. |
| `line-677` (screen) | Fable | Deep line #1: ETP 677→255 finite. Solver-orchestrator with FULL autonomy over its problem: attacks in long continuous stretches, uses engines as compute, banks via VERIFY_CHECKLIST, writes its own state. |
| `line-2` (screen, after selection) | Fable | Deep line #2, chosen by SELECTION.md gate. Same charter shape. |
| selection task (on demand) | Fable | Bounded task spawned by dialogue when a slot opens: answers "the most valuable problem we can attack for one week". |

Max 2 deep lines. A line closes (or is killed by the continuation gate) before a new one opens.

## The free wide layer (engines as COMPUTE, not authors)
ox-alpha (OpenRouter `stealth/ox-alpha`; failover `ox-alpha-free` on opencode go), muse-spark
(`muse-spark-1.2-contributor` on go), Qwen web, Gemini web. Used by line sessions and
selection tasks for: enumeration, case checks, candidate search, probes, cross-family review
votes at milestones.
**Role red line (owner, 08-24): Gemini (incl. Deep Research) is a SEARCH/LITERATURE channel
only — its intelligence is not sufficient for hard mathematics. Never dispatch it attack
rounds, proofs, or S3 judging (the one v4 precedent is voided). Math attack/review runs on
Qwen3.8-Max, codex sol, Claude, or qualification-tested API engines only. Corollary of the
model-tier discipline: capability is per-model; verify the model identity on screen before
any web dispatch; wrong-tier output is void.** Their output is DATA (machine-parseable where possible), never prose
that enters a paper or a bank decision unaudited. Engine workspace (2026-08-24, owner order:
former sandbox merged into the repo): `<repo>/engine/` — briefs/ out/ harvest/ logs/ scripts/;
old path `~/workspace/claudecode/automath-sandbox/` remains as a compatibility symlink.
Quarantine DISCIPLINE unchanged (engine output is data, audited before promotion); keys
`~/.automath_engine_keys`.

**Engine routing (amendment 2026-08-24, closes a v5 wiring gap).** API engines (ox-alpha,
muse-spark) and the codex TUI (screen `codex`, stuff/hardcopy protocol) are driven by LINE
sessions directly. Web engines (Qwen web, Gemini web, GPT-Pro web) are reachable ONLY through
the dialogue session's Chrome: a line that wants web-engine volume writes a brief file to
engine/briefs/ and SendMessages the dialogue session (name: automath-f1); dialogue drives the
browser (itself or via a spawned driver subagent) and returns the harvest path under
engine/harvest/. No-Goodhart rule stands: dispatch only real work — engine idleness with no
real dispatchable work is correct, not a violation; but real briefs sitting undispatched IS a
gap.

## Certification: milestones only, machine-checkable (replaces per-round certs)
- A claim BANKS when it has: a Lean proof, OR an executable verifier with negative controls
  (positive control + a control that must fail), run fresh. Route decisions: one paragraph
  in the line's registry.
- One adversarial cross-family review pass at MILESTONE/PUBLICATION time only.
- VERIFY_CHECKLIST.md (2 pages, frozen) is the operative discipline.
  notes/verification_doctrine.md is ARCHIVED as reference, no longer grows.
- 不可自宣 red line unchanged: solved = adversarial review clean + literature NEW + Lean
  (or machine-checkable certificate), all three, before any outward claim.

## Publication policy
Only CLOSED results are published. Preferred venue arXiv (endorsement permitting), else hold.
NO partial-result self-publishing. Existing Zenodo records: maintained (errata as needed),
no new partial records. Author: Haoyu Chen; git identity chy4pro; private email never public.

**Metadata-correction standing authorization (owner ruling 2026-08-24).** Correcting the
metadata of records WE ALREADY PUBLISHED is PRE-AUTHORIZED — no per-instance ask. Covered:
fixing a wrong number, a self-contradictory or over-stated sentence, a mis-scoped status
marker, a broken/incorrect citation or link, in the description/notes fields of an existing
Zenodo record or the equivalent on our own repos. Conditions: the correction only ever makes
the record MORE accurate; DOI, files and checksums are never touched; NEVER retract (absolute,
pre-existing rule); log every correction in the watch ledger and mention it in the next report
to the owner. NOT covered — still needs an explicit yes: publishing a new record or new
version carrying new content, uploading/replacing files, anything that changes what the work
CLAIMS rather than how accurately it states it, and any first-time outward publication.

**Certificate-first packaging (amendment 2026-08-24, owner-prompted, from the Alpoge S^6 case;
owner may veto).** Every closed result ships in this priority order:
1. a SHORT CERTIFICATE NOTE (few pages: exact statement, the witness/construction, the finite
   checks that carry the claim, and verbatim replication commands an expert can run);
2. the machine-verifiable artifact (Lean file or executable verifier + controls);
3. the long writeup.
Speed to a verifiable public timestamp beats polish; polish follows. The closed-results-only
red line is UNCHANGED. (Precision, owner correction 08-24: Alpoge-style announcements are
FIRST-PARTY-VERIFIED with certificates, not "unverified" — what they lack is independent/peer
verification. Our closed bar — adversarial review + literature NEW + machine certificate — is
stricter than a first-party bar, so announcing closed results is safe; what we do not do is
announce anything BELOW that bar.)

**X announcement channel (amendment 2026-08-24, owner-initiated).** Closed results, once the
user authorizes publication, also get an announcement thread on X from the user's logged-in
account **@HaoyuChn** (renamed from @roy_chn by the owner 08-24 to match the paper byline
Haoyu Chen; chy4pro stays for git; private email never appears). Mechanics: dialogue drafts
the thread (certificate-first: statement, witness, the finite checks, links to Zenodo/GitHub
artifact + replication commands), the user approves the draft, then it is posted via the
user's Chrome session. Per-post user approval is required — the channel is standing, the
authorization is not.
**Quality bar (owner ruling 08-24): post only what is WORTH posting — minor results are
skipped; post only when we honestly judge it will draw attention.** Negative-results papers
and partial/campaign artifacts do not clear the bar. The bar-clearing class: an actual
resolution of a named problem (e.g. closing the ETP finite implication either way, or
Kourovka 16.95 in full), independently verified per our red lines. The first post defines
the account — it waits for a genuine event. (First trial draft, 677 negative paper, was
prepared 08-24 and SHELVED under this bar; kept at engine/briefs/x_thread_draft_677neg.md
as a format template.)

## Quota policy
Spend flat across the week; no dark freezes (autoContinueAtUsageLimit is set). Claude goes
to: deep attack rounds (long, continuous), milestone adjudication, selection. Watch the
5h window only to schedule long stretches, not to hoard.

**Cloud compute (owner grant 2026-08-24): Google Cloud, one project with ~$90 credit.**
CLI: `~/.local/bin/gcloud` (self-contained SDK + standalone Python 3.12 in ~/.local).
HARD RULES (owner's grant conditions): (1) CONFIRM WITH THE OWNER BEFORE EACH SPEND —
every resource launch gets a written cost estimate (machine type, hours, $) and waits for
an explicit yes; (2) NEVER overspend — check remaining credit before and after each run,
size jobs so worst-case cost stays well under the remainder; (3) engineering discipline:
prefer spot/preemptible, every instance gets a hard TTL/auto-delete, jobs carry internal
timeouts and checkpoint to GCS/disk, delete resources immediately after harvest. This
unblocks the parked "677 cloud SAT" item: the line specs a costed proposal; dialogue
relays it for owner confirmation.

## Monitors (the only standing automation)
1. pub-watch (PR/Zenodo feedback; tools/pub_watch.sh) — in dialogue session.
2. arXiv daily watch (tools/arxiv_daily_watch.py — fix date-window bug before scheduling;
   population==0 must ALARM). — in dialogue session.
Everything else (lease ledgers, engine queues/backlogs as markdown-databases, engine meters,
heartbeat relays, channel-authentication protocol) is DELETED with the planner layer.

## File map (v5)
- `ARCHITECTURE.md` — this file. The constitution.
- `VERIFY_CHECKLIST.md` — frozen 2-page verification discipline.
- `SELECTION.md` — target selection gate v2 (flipped sign) + continuation gate.
- `lines/<line>/BOOTSTRAP.md` — per-line session bootstrap (identity, state pointers, rules).
- `problems/<line>/` — line workspace (registries, scripts, outputs) — unchanged.
- `notes/`, `papers/`, `prompts/` — unchanged roles.
- `orchestration/` — ARCHIVED (audit trail; see orchestration/ARCHIVED_README.md).
- Memory (auto-loaded by dialogue): mission / infra / methodology / pipeline-state.

## Restart recovery (any machine reboot)
Dialogue session: read memory + this file; `screen -ls`; relaunch missing line sessions with
`screen -dmS <line> ~/.local/bin/claude "Read <repo>/lines/<line>/BOOTSTRAP.md and resume."`;
re-arm the two monitors. Line state lives in files; sessions are disposable.
