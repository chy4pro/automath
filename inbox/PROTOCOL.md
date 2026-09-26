# automath inbox protocol (Claude coordinator ⇄ Codex/Astra worker)

Both sides share this project volume (/work). This directory is the only channel.

## For Codex (the worker)
1. Tasks live in `inbox/to_codex/NNN_<slug>.md`. Process them by number unless a task says `priority: high`.
   Tasks marked `parallel: yes` may run concurrently — use your sub-agents / parallel slots as fully as
   your environment allows; the owner wants Astra's agent and parallel capacity used to the full.
2. Before starting a task, append a line to `inbox/STATUS.md`: `<UTC time> START NNN <slug>`.
   When done: `<UTC time> DONE NNN <slug> → <report path>` (or `FAILED NNN <reason>`).
3. Write the report to the path named in the task (under `inbox/from_codex/` or the campaign dir).
   Reports are Markdown: status line first (PROVED / CONDITIONAL / OPEN / DEAD / DONE), then the work,
   every number traced to a source or a derivation, no "first"/priority wording, no hype.
4. Questions for the coordinator go to `inbox/from_codex/QUESTIONS.md` (append; one dated line per question).
   Do not wait for an answer unless the task says so — state your assumption and continue.
5. Never edit files outside the report paths and `inbox/STATUS.md`; never `git commit`/`push`;
   never post anywhere; no SAT solvers; numerics with python3 (numpy/mpmath) are fine, ≤ 2 processes, ≤ 2 GB each.
6. Poll: after finishing all tasks, check `inbox/to_codex/` again every 5 minutes for new ones; stop only
   when `inbox/to_codex/STOP` exists.

## Standing instruction from the owner (2026-09-26)
You are allowed — expected — to push back on the coordinator. If a task, a route, a target, a budget
or a claimed "known result" is wrong, wasteful, or not the most valuable thing to do, say so in
`inbox/from_codex/QUESTIONS.md` (or at the top of your report) with your reasons and your proposed
alternative, and act on your own judgement when the task leaves room. The only goal is the most
valuable correct mathematics; nobody's plan is sacred, including this protocol. Disagreements are
resolved by evidence (a proof, a counterexample, a source), not by rank.

## Clean-room rule (owner, 2026-09-26)
Literature search has one job: confirm nobody has finished the target and locate the exact frontier.
Once that is confirmed, the attack itself is done by CLEAN-ROOM agents: fresh context, no web search,
no papers, no campaign files — only the problem statement, the definitions and the precise target
(the inequality or theorem to prove), plus the standard mathematics the agent already knows. The
point is to avoid being trapped in the framing of existing human proofs. Tasks marked `clean-room: yes`
must be run that way; the route reports (which do cite literature) are then compared with the
clean-room output by the coordinator, never fed to the clean-room agents.

## For Claude (the coordinator)
- Writes tasks, reads STATUS.md and reports, moves finished tasks to `inbox/archive/`, answers QUESTIONS.md
  by appending under the question. Commits/pushes are Claude's job.

Kickoff prompt for the Codex session (owner types it once):
"Read /work/inbox/PROTOCOL.md and then process /work/inbox/to_codex/ as described, using your parallel capacity fully. Keep going until /work/inbox/to_codex/STOP exists."
