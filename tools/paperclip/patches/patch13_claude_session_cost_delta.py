#!/usr/bin/env python3
"""Patch 13 (PAPERCLIP_PATCH_SESSION_COST_DELTA): bill only the per-run increase of a resumed Claude Code session.
Claude Code restores a session's cost state on --resume, so a resumed run's result reports the SESSION's running totals
(total_cost_usd, modelUsage, duration_api_ms), not this invocation's. claude_local marks its usage "per_run", so the
server charged each resumed run the whole session total again. Observed 2026-10-11 on the Claude API org: a 10-second run
billed $6.31, Paperclip counted about 2-3x the spend the Anthropic Console shows. A resumed run that replays a stale
result (num_turns 0) after background tasks also reported an old total. Fix: for claude_local, bill
max(0, reported - highest total already reported by earlier runs of the same agent and session). The first run of a
session is billed in full. Token counters are left as reported. Usage: patch13_claude_session_cost_delta.py <@paperclipai dir>"""
import sys
p = f"{sys.argv[1]}/server/dist/services/heartbeat.js"; s = open(p).read()
M = "/* PAPERCLIP_PATCH_SESSION_COST_DELTA */"
if M in s: print("already: patch 13"); sys.exit(0)
old = "        const billedCostUsd = resolveCacheAdjustedCostUsd(result);\n"
assert s.count(old) == 1, "anchor"
new = (f"        let billedCostUsd = resolveCacheAdjustedCostUsd(result); {M}\n"
       "        if (agent.adapterType === \"claude_local\" && typeof billedCostUsd === \"number\" && typeof result.sessionId === \"string\" && result.sessionId) {\n"
       "            const prior = await db\n"
       "                .select({ maxCost: sql `max(nullif(${heartbeatRuns.usageJson} ->> 'costUsd', '')::double precision)` })\n"
       "                .from(heartbeatRuns)\n"
       "                .where(and(eq(heartbeatRuns.agentId, agent.id), eq(heartbeatRuns.sessionIdAfter, result.sessionId), ne(heartbeatRuns.id, run.id)))\n"
       "                .then((rows) => Number(rows[0]?.maxCost ?? 0));\n"
       "            if (Number.isFinite(prior) && prior > 0) billedCostUsd = Math.max(0, billedCostUsd - prior);\n"
       "        }\n")
s = s.replace(old, new, 1); open(p, "w").write(s); print("patched: 13 session cost delta for claude_local")
