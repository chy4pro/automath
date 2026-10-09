# Paperclip playbook — session continuity by default (coordinator-owned)

Owner: the Paperclip `coordinator` agent. Adopted 2026-10-09 (AUT-55, owner instruction relayed by the chat session).
Authority: below AGENTS.md → OPERATIONS.md → OWNER_RULES.md; above strategy notes and the ledger. English; every
agent that touches Paperclip issues follows it. Changes to this file are made by the coordinator only, between rounds
(see §7), and recorded in the ledger.

## 0. The one rule

**Resumed sessions are the default. A fresh session is a deliberate act, taken only to open a NEW clean room, or when
Paperclip forces it.** Everything else — the coordinator's own work on a line, referee follow-ups, verifier re-checks,
scout updates, and follow-up questions to a clean-room attacker — continues in the existing session of the existing issue.

Facts this rests on (verified 2026-10-09 from run records): Paperclip keeps one saved session per (agent, issue). A wake
on the same issue resumes it (comments, child completions, status changes, reopen-via-comment). The session is RESET
when the wake reason is `issue_assigned`, `execution_approval_requested`, execution-review recovery or an unscoped timer
wake; when the agent's effective configuration changes (instructions bundle, model, adapter config, environment, env
bindings, secrets); or when a fresh session is forced. **Therefore the unit of continuity is the issue.**

## 1. Issue kinds and naming

| prefix | assignee | one issue per | lifetime | follow-ups |
|---|---|---|---|---|
| `LINE <id>: <title>` | coordinator (self) | research line or selection round (e.g. AUT-51) | open from selection to park/publish | children's closures wake it; the coordinator judges inside the same session |
| `OWNER <date>: <title>` | coordinator (self) | one owner instruction that needs work | open until executed and reported | same as LINE |
| `CR-<n> <target> (attacker-k)` | attacker-1 / attacker-2 | **one clean room** | done after the report; resumable | questions as comments (§4) |
| `REF <target> <file> (referee-k)` | referee-1 / referee-2 | one referee × one report under review | done after the report; resumable | repairs / re-review as comments |
| `VER <target>: <check>` | verifier | one target line's finite checks | done after the first check; resumable | further checks as comments |
| `SCOUT <topic>` | scout | one literature / G2 / catalogue topic | done after the first delivery; resumable | updates as comments |
| `LEAN <target>` | formalizer | one formalisation target | done per milestone; resumable | next lemma as comment |
| `Hourly coordinator tick`, `6-hour reflection` | coordinator | routine (timer wake, always fresh) | closed each run | none — real work moves to a LINE/OWNER issue |

`<n>` for clean rooms is a global counter continued from the probe numbering (PROBE_ASTRA_1–6 → CR-7 onwards). Every
child issue carries `parentId` = the LINE/OWNER issue and a blocker on the parent, so the parent's session is woken when
the child closes.

## 2. Close vs keep open

- **Worker issues (CR/REF/VER/SCOUT/LEAN): close with `done` as soon as the report is delivered.** A closed issue keeps
  its session; a follow-up is a comment with `resume: true` (the agent is woken, the saved session resumes). Keeping
  worker issues open would hide which reports are actually outstanding and would not add continuity.
- **Coordinator issues (LINE/OWNER): keep open for the life of the line.** Status `in_progress` while judging, `blocked`
  (with the child blockers) while reports are being produced, `done` only at park / publish / owner-instruction executed,
  with the closing summary in Chinese. This is what makes the coordinator's own session persist across child completions.
- **Successor issue instead of an endless session.** When a LINE issue's resumed runs become expensive (signal: input
  tokens of a resumed run exceed about twice those of a fresh coordinator run, read from the run record at the 6-hour
  reflection) or the line changes phase (probe → campaign → publication), close it with a written summary file and open
  `LINE <id> part 2` whose description names that file. The summary, not the transcript, is the memory.
- **Routine ticks and reflections** are timer wakes and always fresh; they do nothing unless something happened, and any
  real work found there is moved to a LINE/OWNER issue by one comment and one child issue.

## 3. Parent-issue mechanics for the coordinator

1. Create the LINE issue assigned to yourself (this first `issue_assigned` wake is the one fresh start of the line).
2. From inside that run create the children (`parentId` = LINE, assignee = the report, blocker on the parent), put the
   complete brief in each child's description, set the LINE issue to `blocked`.
3. Each child closure resumes the LINE session: read the report, judge, write the verdict, dispatch the next child or
   close. Approval requests (`request_board_approval`) are created from the LINE issue; whether the board's decision
   wake resumes or resets the session is **unverified** — the first occurrence is recorded here and in the ledger.
4. Never work on two lines inside one LINE issue; a second line gets its own LINE issue.

## 4. Follow-up questions to a clean-room attacker (literature-free)

A clean room is defined by what has entered the attacker's session, not by the session being fresh. Follow-ups keep the
room clean iff they obey this list.

Allowed in a follow-up comment:
- the attacker's own text quoted back, with an exact mathematical question ("in Lemma 3 the bound … fails for n = 17 —
  repair or retract");
- finite witnesses or counterexamples as data (tables, explicit sets, numbers), without saying where they came from;
- requests to make a quantifier, constant or onset explicit, or to write a missing case;
- a route seed stated purely as mathematics (a lemma to try, an object to look at), with no attribution;
- referee repair items **rewritten by the coordinator into mathematical statements**, never the referee file itself.

Forbidden (any one of these ends the clean room; record it and treat the session as contaminated):
- author names, paper titles, years, arXiv ids, "this is known/open", the status of the problem, "the literature";
- campaign files, verdict files, selection notes, or the other attacker's output (merging two rooms is a deliberate
  act: do it only to combine proofs, say so in the comment, and record the merge);
- referee reports verbatim (they may cite literature).

Format: the comment ends with the line `[CR-<n> follow-up <k>; literature-free: yes]`; the coordinator copies that line
into the verdict file. Follow-ups are capped at 3 per clean room per round; beyond that the session is either converged
(PROVED → referees) or at its method limit (OPEN → park).

When a NEW clean room is wanted (new `CR-` issue, deliberately fresh): a new target or lemma; a contaminated room; a
deliberately independent second attempt on the same target (the two attackers are two rooms by construction — use the
other attacker first); or Paperclip forced a reset (then the room is de facto fresh and is recorded as such, see §5).

## 5. Recording resumed vs fresh

Every report entry in a verdict file (`notes/selection/*.md`, `notes/review/*.md`) and the matching ledger line carries a
`session:` field with one of:
- `fresh (issue_assigned AUT-nn)` — first run on the issue;
- `resumed (comment on AUT-nn, follow-up k)` — continuation in the saved session;
- `reset (<reason>, AUT-nn)` — Paperclip reset the session (config change, approval wake, recovery); for a clean room
  this starts generation g+1: write `CR-n gen 2`, and judge its output as a fresh attempt, not a continuation.

Referee reports additionally state their own lineage in the status line's second sentence ("Resumed session of AUT-40,
follow-up 1") so cross-vendor independence stays auditable: referee-1 and referee-2 are independent because they are
different agents and vendors, not because their sessions are fresh.

## 6. Cost expectations and when to prefer fresh

- A fresh coordinator run pays the base context (≈70–100k input tokens per the 2026-10-09 measurements); worker runs
  less. A resumed run re-sends the saved transcript, so its cost grows with the length of the session; prompt caching
  makes a quick second turn cheap, a long-idle one not.
- Resume when the prior context is needed: follow-ups, repairs, judging a child's report against the brief you wrote,
  continuing a line. Start fresh when it is not: a new target, a new clean room, a line whose summary file already
  contains everything (then close and open the successor, §2).
- The 6-hour reflection reads the run records of the window and reports: runs per agent, fresh vs resumed count, input
  tokens of the longest resumed run, and whether any reset was unintended (config change while live).

## 7. Configuration freeze

Editing an agent's instructions bundle, model, adapter config, environment, env bindings or secrets resets every live
session of that agent. Therefore:
- no such edit while any CR/REF/VER/LINE issue of that agent still needs continuation; the chat session has stopped
  doing this (2026-10-09) and relays changes as comments;
- bundle changes are batched into a **maintenance window** between rounds: the coordinator announces it in the ledger
  ("CONFIG WINDOW: agents …, reason …"), the chat session applies them, the coordinator records the reset generation;
- owner instructions arriving mid-round are comments on the relevant issue or a new OWNER issue, never bundle edits.

## 8. Applied from 2026-10-09

- AUT-51 is the LINE issue of the lemma-gated selection round; its children (AUT-52 scout, the verifier tests, the
  step-2b probe) follow §1–§3. The step-2b probe will be `CR-7 … (attacker-1)` with follow-ups per §4.
- Round-4 issues (AUT-12/13/22–25 attackers, AUT-14–17/38–45 referees) are closed and resumable; if a parked line is
  reopened, its follow-ups go to those issues as comments, not to new rooms.
- Open verification items for this playbook: (a) does a board-decision wake on a `request_board_approval` resume or
  reset; (b) does a comment with `resume: true` on a `done` Codex issue resume the Codex session as reliably as the
  14:17 retries did. Both are recorded at first occurrence.
