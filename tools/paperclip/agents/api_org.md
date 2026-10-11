## Engines since 2026-10-11 (owner decision)
- The Claude agents (coordinator-api, referee-api-1, referee-api-2, formalizer-api, verifier-api) run Claude Code on the owner's Claude API key: metered and billed per token at list price (Opus 5.5 is $4 per million input tokens and $20 per million output tokens; Sonnet 5.5 is half that). The earlier subscription Claude agents are paused and not used.
- Formalization (Lean) goes to formalizer-api on the Claude API; the Codex formalizer is paused (owner, 2026-10-11).
- Codex work stays on Codex: scout, attacker-1, attacker-2 (and muse-codex on muse) run GPT-6 Astra on the Codex subscription and report to coordinator-api. Give Codex tasks to them, as before.
- Budget: Paperclip enforces a lifetime hard stop of $200 on API spend (warning at 80%). At the limit Paperclip pauses the agents and opens a budget incident; only the owner raises it. Each report to the owner states the API spend since the previous report.
- Cross-vendor review is still available: Claude referees for Astra work, Astra (Codex) referees for Claude work.
- Commit trailer for coordinator-api: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` (it replaces the trailer named in the role text).
