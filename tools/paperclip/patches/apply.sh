#!/bin/sh
# Local patches to the installed Paperclip (npm prefix /work/.tools/npm). Idempotent; re-run after `npm install -g paperclipai`.
# Why: upstream `codex_local` allows a REMOTE's own ~/.codex/auth.json only for sandbox transports; ssh targets are forced
# to use the Paperclip host's login. We let ssh targets behave like sandboxes: (1) the credential gate probes the remote
# for ~/.codex/auth.json instead of refusing; (2) after the managed CODEX_HOME is uploaded over ssh, auth.json falls back
# to the remote's own login (same rule as codex-auth-merge-extract.sh uses for sandboxes); (3) the server's pre-dispatch
# credential gate (run-preparation) exempts ssh environments like it exempts sandbox ones; (4) agent deletion removes the
# agent's cost_events first (upstream FK bug: cost_events -> heartbeat_runs/agents blocks DELETE /api/agents/:id).
set -e
PY=$(command -v python3 || echo /work/.tools/node/bin/node)   # python3 exists in the Claude container; fall back handled below
NM=/work/.tools/npm/lib/node_modules/paperclipai/node_modules/@paperclipai
EX=$NM/adapter-codex-local/dist/server/execute.js
RM=$NM/adapter-utils/dist/remote-managed-runtime.js
VER=$(sed -n 's/.*"version": "\([^"]*\)".*/\1/p' /work/.tools/npm/lib/node_modules/paperclipai/package.json | head -1)
echo "paperclipai $VER"
for f in "$EX" "$RM"; do [ -f "$f.orig" ] || cp "$f" "$f.orig"; done
python3 - "$EX" "$RM" <<'PYEOF'
import sys
ex, rm = sys.argv[1:3]
s = open(ex).read()
if 'PAPERCLIP_PATCH_SSH_AUTH' not in s:
    a = 'async function probeSandboxCodexAuthJson(input) {\n    if (!input.target || input.target.kind !== "remote" || input.target.transport !== "sandbox") {'
    b = 'async function probeSandboxCodexAuthJson(input) {\n    // PAPERCLIP_PATCH_SSH_AUTH: ssh targets are probed like sandboxes (automath local patch)\n    if (!input.target || input.target.kind !== "remote" || (input.target.transport !== "sandbox" && input.target.transport !== "ssh")) {'
    assert a in s, 'probe anchor missing'; s = s.replace(a, b, 1)
    a2 = '    const targetIsSandbox = input.target?.kind === "remote" && input.target.transport === "sandbox";\n    if (targetIsSandbox) {\n        const sandboxAuthJson = await probeSandboxCodexAuthJson({'
    b2 = '    const targetIsSandbox = input.target?.kind === "remote" && (input.target.transport === "sandbox" || input.target.transport === "ssh"); // PAPERCLIP_PATCH_SSH_AUTH\n    if (targetIsSandbox) {\n        const sandboxAuthJson = await probeSandboxCodexAuthJson({'
    assert a2 in s, 'gate anchor missing'; s = s.replace(a2, b2, 1)
    open(ex, 'w').write(s); print('patched execute.js')
else: print('execute.js already patched')
r = open(rm).read()
if 'PAPERCLIP_PATCH_SSH_AUTH' not in r:
    a = '''            await syncDirectoryToSsh({
                spec: input.spec,
                localDir: asset.localDir,
                remoteDir,
                followSymlinks: asset.followSymlinks,
                exclude: asset.exclude,
                onProgress: input.onProgress,
                progressLabel: asset.key,
            });
'''
    b = a + '''            // PAPERCLIP_PATCH_SSH_AUTH (automath local patch): mirror codex-auth-merge-extract.sh's fallback —
            // when the shipped home carries no auth.json, use the remote's own ~/.codex/auth.json.
            if (asset.key === "home") {
                const q = (v) => "'" + String(v).replace(/'/g, "'\\\\''") + "'";
                await runSshCommand(input.spec, `[ -f ${q(remoteDir)}/auth.json ] || { [ -f "$HOME/.codex/auth.json" ] && umask 077 && cp "$HOME/.codex/auth.json" ${q(remoteDir)}/auth.json && echo "[paperclip-patch] using the remote host's own Codex login"; true; }`, { timeoutMs: 20000 });
            }
'''
    assert r.count(a) >= 1, 'sync anchor missing'; r = r.replace(a, b, 1)
    open(rm, 'w').write(r); print('patched remote-managed-runtime.js')
else: print('remote-managed-runtime.js already patched')
PYEOF
HB=$NM/server/dist/services/heartbeat.js
[ -f "$HB.orig" ] || cp "$HB" "$HB.orig"
python3 - "$HB" <<'PYEOF'
import sys
hb = sys.argv[1]; s = open(hb).read()
if 'PAPERCLIP_PATCH_SSH_AUTH' not in s:
    a = '(input.environmentDriver ?? null) !== "sandbox") {\n        const resolvedEnv = parseObject(resolvedConfig.env);\n        const readiness = await evaluateCodexCredentialReadiness({'
    b = '(input.environmentDriver ?? null) !== "sandbox" && (input.environmentDriver ?? null) !== "ssh" /* PAPERCLIP_PATCH_SSH_AUTH: ssh environments are probed by the adapter like sandboxes */) {\n        const resolvedEnv = parseObject(resolvedConfig.env);\n        const readiness = await evaluateCodexCredentialReadiness({'
    assert a in s, 'heartbeat anchor missing'; s = s.replace(a, b, 1); open(hb, 'w').write(s); print('patched heartbeat.js')
else: print('heartbeat.js already patched')
PYEOF
AG=$NM/server/dist/services/agents.js
[ -f "$AG.orig" ] || cp "$AG" "$AG.orig"
python3 - "$AG" <<'PYEOF'
import sys, re
ag = sys.argv[1]; s = open(ag).read()
if 'PAPERCLIP_PATCH_AGENT_DELETE' not in s:
    # (4) upstream bug: agent removal deletes heartbeat_runs while cost_events still reference them (and the agent) -> FK violation
    a = '                await tx.delete(heartbeatRuns).where(eq(heartbeatRuns.agentId, id));'
    b = '                await tx.delete(costEvents).where(eq(costEvents.agentId, id)); // PAPERCLIP_PATCH_AGENT_DELETE (automath local patch)\n' + a
    assert s.count(a) == 1, 'agents remove anchor missing'
    s = s.replace(a, b, 1)
    if not re.search(r'\bcostEvents\b.*from "@paperclipai/db"', s) and 'costEvents,' not in s.split('from "@paperclipai/db"')[0][-4000:]:
        m = re.search(r'import \{([^}]*)\} from "@paperclipai/db";', s)
        assert m, 'db import missing'
        s = s.replace(m.group(0), 'import {' + m.group(1).rstrip() + (', ' if m.group(1).strip() else '') + 'costEvents } from "@paperclipai/db";', 1)
    open(ag, 'w').write(s); print('patched agents.js')
else: print('agents.js already patched')
PYEOF
/work/.tools/node/bin/node --check "$EX" && /work/.tools/node/bin/node --check "$RM" && /work/.tools/node/bin/node --check "$HB" && /work/.tools/node/bin/node --check "$AG" && echo "syntax ok"

# ---- patch 5: run pools (PAPERCLIP_PATCH_RUN_POOLS) ------------------------------------------------
# Paperclip only caps concurrency per agent. PAPERCLIP_RUN_POOLS="codex:2:scout,attacker-1,attacker-2,formalizer"
# caps the number of simultaneously RUNNING runs across the named agents (one pool per ';'); queued runs
# wait and are promoted when a pool-mate finishes.
HB=$NM/server/dist/services/heartbeat.js
if ! grep -q PAPERCLIP_PATCH_RUN_POOLS "$HB"; then
  cp -n "$HB" "$HB.orig5" 2>/dev/null || true
  python3 - "$HB" <<'PY'
import sys,re
p=sys.argv[1]; s=open(p).read()
helpers='''
    // PAPERCLIP_PATCH_RUN_POOLS: cross-agent concurrency caps from PAPERCLIP_RUN_POOLS ("name:max:a,b,c;...").
    const RUN_POOLS = (process.env.PAPERCLIP_RUN_POOLS || "").split(";").map((s) => s.trim()).filter(Boolean).map((spec) => {
        const [name, max, members] = spec.split(":");
        return { name, max: Number(max), members: new Set((members || "").split(",").map((m) => m.trim()).filter(Boolean)) };
    }).filter((p) => p.max > 0 && p.members.size > 0);
    function runPoolForAgent(agent) { return RUN_POOLS.find((p) => p.members.has(agent.name)) ?? null; }
    async function countRunningRunsForPool(companyId, pool) {
        const [{ count }] = await db.select({ count: sql `count(*)` }).from(heartbeatRuns)
            .innerJoin(agents, eq(agents.id, heartbeatRuns.agentId))
            .where(and(eq(heartbeatRuns.companyId, companyId), eq(heartbeatRuns.status, "running"), inArray(agents.name, [...pool.members])));
        return Number(count ?? 0);
    }
    async function startNextQueuedRunForAgent(agentId) {
        const started = await startNextQueuedRunForAgentCore(agentId);
        if (RUN_POOLS.length === 0) return started;
        const agent = await getAgent(agentId); const pool = agent ? runPoolForAgent(agent) : null;
        if (!pool) return started;
        const mates = await db.select({ id: agents.id }).from(agents)
            .where(and(eq(agents.companyId, agent.companyId), inArray(agents.name, [...pool.members])));
        for (const m of mates) { if (m.id !== agentId) await startNextQueuedRunForAgentCore(m.id); }
        return started;
    }
    async function startNextQueuedRunForAgentCore(agentId) {'''
s=s.replace('    async function startNextQueuedRunForAgent(agentId) {', helpers, 1)
old='''            const policy = parseHeartbeatPolicy(agent);
            const runningCount = await countRunningRunsForAgent(agentId);
            const availableSlots = Math.max(0, policy.maxConcurrentRuns - runningCount);
            if (availableSlots <= 0)
                return [];'''
new='''            const policy = parseHeartbeatPolicy(agent);
            const runningCount = await countRunningRunsForAgent(agentId);
            let availableSlots = Math.max(0, policy.maxConcurrentRuns - runningCount);
            const runPool = runPoolForAgent(agent);
            if (runPool) availableSlots = Math.min(availableSlots, Math.max(0, runPool.max - (await countRunningRunsForPool(agent.companyId, runPool))));
            if (availableSlots <= 0)
                return [];'''
assert old in s, 'slot block not found'
s=s.replace(old,new,1)
open(p,'w').write(s)
PY
  node --check "$HB" && echo "patch 5 applied: run pools"
else echo "patch 5 already applied"; fi
