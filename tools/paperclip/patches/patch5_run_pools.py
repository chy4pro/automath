#!/usr/bin/env python3
"""Patch 5 (PAPERCLIP_PATCH_RUN_POOLS v2): cross-agent concurrency caps in heartbeat.js.
Mirrors upstream PR #14333's admission mechanism (count + claim under pg_advisory_xact_lock at the single
admission point) with the bucket key generalised:
  PAPERCLIP_ADAPTER_CONCURRENCY_LIMITS='{"codex_local":2}'                 per adapter type, instance-wide
  PAPERCLIP_RUN_POOLS="codex:2:scout,attacker-1,attacker-2,formalizer"      explicit named agent groups (per company)
Usage: patch5_run_pools.py <path to server/dist/services/heartbeat.js>"""
import sys
p = sys.argv[1]; s = open(p).read()
if 'PAPERCLIP_PATCH_RUN_POOLS' in s:
    print('patch 5 already applied'); sys.exit(0)
HELPERS = '''
    // PAPERCLIP_PATCH_RUN_POOLS v2 — cross-agent concurrency caps (tools/paperclip/patches/patch5_run_pools.py).
    const RUN_POOL_GROUPS = (process.env.PAPERCLIP_RUN_POOLS || "").split(";").map((x) => x.trim()).filter(Boolean).map((spec) => {
        const [name, max, members] = spec.split(":");
        return { key: "group:" + name, max: Math.floor(Number(max)), members: new Set((members || "").split(",").map((m) => m.trim()).filter(Boolean)) };
    }).filter((g) => Number.isFinite(g.max) && g.max >= 1 && g.members.size > 0);
    const RUN_POOL_ADAPTER_LIMITS = (() => {
        const raw = process.env.PAPERCLIP_ADAPTER_CONCURRENCY_LIMITS; if (!raw || !raw.trim()) return {};
        let parsed; try { parsed = JSON.parse(raw); } catch { return {}; }
        if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) return {};
        const out = {}; for (const [k, v] of Object.entries(parsed)) { const n = typeof v === "number" ? v : Number(v); if (Number.isFinite(n) && n >= 1) out[k] = Math.floor(n); }
        return out;
    })();
    function resolveRunPool(agent) {
        const g = RUN_POOL_GROUPS.find((x) => x.members.has(agent.name));
        if (g) return { kind: "group", key: g.key, max: g.max, members: g.members, companyId: agent.companyId };
        const lim = RUN_POOL_ADAPTER_LIMITS[agent.adapterType];
        if (lim !== undefined) return { kind: "adapter", key: "adapter:" + agent.adapterType, max: lim, adapterType: agent.adapterType };
        return null;
    }
    async function countRunningRunsForPool(pool, executor = db) {
        if (pool.kind === "group") {
            const [{ count }] = await executor.select({ count: sql `count(*)` }).from(heartbeatRuns)
                .innerJoin(agents, eq(agents.id, heartbeatRuns.agentId))
                .where(and(eq(heartbeatRuns.companyId, pool.companyId), eq(heartbeatRuns.status, "running"), inArray(agents.name, [...pool.members])));
            return Number(count ?? 0);
        }
        const dispatched = sql `${heartbeatRuns.runnerProfileJson}->'adapterDispatch'->>'adapterType'`;
        const [{ count }] = await executor.select({ count: sql `count(*)` }).from(heartbeatRuns)
            .innerJoin(agents, eq(agents.id, heartbeatRuns.agentId))
            .where(and(eq(heartbeatRuns.status, "running"), eq(sql `coalesce(${dispatched}, ${agents.adapterType})`, pool.adapterType)));
        return Number(count ?? 0);
    }
    async function claimQueuedRunOrRecordRejection(queuedRun, companyAgents, rejectedClaims) {
        try { return await claimQueuedRun(queuedRun, companyAgents); }
        catch (err) {
            if (isPermanentClaimRejection(err)) { rejectedClaims.push({ run: queuedRun, err }); return null; }
            if (!isDeferrableClaimRejection(err)) throw err;
            logger.warn({ err, runId: queuedRun.id, agentId: queuedRun.agentId, companyId: queuedRun.companyId }, "queued heartbeat run claim was rejected; leaving it queued for the next recovery pass");
            return null;
        }
    }
    // Claims up to maxClaims runs; with a pool, the count and the claims happen under pg_advisory_xact_lock(hashtext(pool.key)).
    async function claimRunsWithPoolGuard(agent, prioritizedRuns, maxClaims, companyAgents, rejectedClaims) {
        const claimedRuns = []; const pool = resolveRunPool(agent);
        if (!pool) {
            for (const queuedRun of prioritizedRuns) { if (claimedRuns.length >= maxClaims) break; const c = await claimQueuedRunOrRecordRejection(queuedRun, companyAgents, rejectedClaims); if (c) claimedRuns.push(c); }
            return claimedRuns;
        }
        await db.transaction(async (tx) => {
            await tx.execute(sql `select pg_advisory_xact_lock(hashtext(${pool.key}))`);
            const running = await countRunningRunsForPool(pool, tx);
            const allowed = Math.max(0, Math.min(maxClaims, pool.max - running));
            for (const queuedRun of prioritizedRuns) { if (claimedRuns.length >= allowed) break; const c = await claimQueuedRunOrRecordRejection(queuedRun, companyAgents, rejectedClaims); if (c) claimedRuns.push(c); }
        });
        return claimedRuns;
    }
    async function startNextQueuedRunForAgent(agentId) {
        const started = await startNextQueuedRunForAgentCore(agentId);
        const agent = await getAgent(agentId); const pool = agent ? resolveRunPool(agent) : null;
        if (!pool) return started;
        const mates = pool.kind === "group"
            ? await db.select({ id: agents.id }).from(agents).where(and(eq(agents.companyId, agent.companyId), inArray(agents.name, [...pool.members])))
            : await db.select({ id: agents.id }).from(agents).where(and(eq(agents.companyId, agent.companyId), eq(agents.adapterType, pool.adapterType)));
        for (const m of mates) { if (m.id !== agentId) await startNextQueuedRunForAgentCore(m.id); }
        return started;
    }
    async function startNextQueuedRunForAgentCore(agentId) {'''
anchor = '    async function startNextQueuedRunForAgent(agentId) {'
assert s.count(anchor) == 1, 'anchor not found once'
s = s.replace(anchor, HELPERS, 1)
OLD = '''            const claimedRuns = [];
            for (const queuedRun of prioritizedRuns) {
                if (claimedRuns.length >= availableSlots)
                    break;
                let claimed;
                try {
                    claimed = await claimQueuedRun(queuedRun, companyAgents);
                }
                catch (err) {
                    if (isPermanentClaimRejection(err)) {
                        rejectedClaims.push({ run: queuedRun, err });
                        continue;
                    }
                    if (!isDeferrableClaimRejection(err))
                        throw err;
                    logger.warn({ err, runId: queuedRun.id, agentId: queuedRun.agentId, companyId: queuedRun.companyId }, "queued heartbeat run claim was rejected; leaving it queued for the next recovery pass");
                    continue;
                }
                if (claimed)
                    claimedRuns.push(claimed);
            }
'''
assert s.count(OLD) == 1, 'claim loop not found exactly once'
s = s.replace(OLD, '            const claimedRuns = await claimRunsWithPoolGuard(agent, prioritizedRuns, availableSlots, companyAgents, rejectedClaims);\n', 1)
open(p, 'w').write(s); print('patch 5 v2 applied: run pools with advisory lock')
