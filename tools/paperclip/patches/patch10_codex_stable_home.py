#!/usr/bin/env python3
"""Patch 10 v2 (PAPERCLIP_PATCH_ASSET_STATE): on ssh targets keep the adapter's runtime *assets* (for codex_local the
CODEX_HOME: config, skills, auth and the session rollouts) in a per-task directory, so `codex ... resume <id>` finds
the previous run's rollout. Verified 2026-10-09: with patches 8/9/9b Codex attempted the resume and answered
"no rollout found for thread id" because each run got a brand-new home. The runtime root itself (bridge, referenced
project staging) stays per run, so concurrent runs never share those. Asset sync overlays with tar (no clear), so
sessions/ persists. Opt out: PAPERCLIP_STABLE_ASSET_STATE=0. Reverts v1 (whole runtime root stable) if present.
Usage: patch10_codex_stable_home.py <@paperclipai dir>"""
import sys, os
NM = sys.argv[1]; M = "/* PAPERCLIP_PATCH_ASSET_STATE */"; V1 = "/* PAPERCLIP_PATCH_STABLE_RUNTIME_ROOT */"
RMR = f"{NM}/adapter-utils/dist/remote-managed-runtime.js"; ET = f"{NM}/adapter-utils/dist/execution-target.js"; CX = f"{NM}/adapter-codex-local/dist/server/execute.js"
V1_RMR_NEW = (f'    const runtimeRootDir = {V1} (typeof input.runtimeRootKey === "string" && input.runtimeRootKey.length > 0)\n'
              '        ? path.posix.join(baseWorkspaceRemoteDir, ".paperclip-runtime", "runtime", input.runtimeRootKey, input.adapterKey)\n'
              '        : path.posix.join(workspaceRemoteDir, ".paperclip-runtime", input.adapterKey);')
ORIG_RMR = '    const runtimeRootDir = path.posix.join(workspaceRemoteDir, ".paperclip-runtime", input.adapterKey);'
V1_ET = f'            runtimeRootKey: input.runtimeRootKey, {V1}\n'
V1_CX_HELPER_START = f'                {V1} const stableRuntimeRootKey'
def rw(path, fn):
    s = open(path).read(); t = fn(s)
    if t != s: open(path, "w").write(t); print("changed:", os.path.relpath(path, NM))
# --- revert v1
rw(RMR, lambda s: s.replace(V1_RMR_NEW, ORIG_RMR))
rw(ET, lambda s: s.replace(V1_ET, ""))
def revert_cx(s):
    i = s.find(V1_CX_HELPER_START)
    if i < 0: return s
    j = s.index("return await prepareAdapterExecutionTargetRuntime({", i)
    s = s[:i] + "                " + s[j:]
    return s.replace("                    runId,\n                    runtimeRootKey: stableRuntimeRootKey,\n", "                    runId,\n", 1)
rw(CX, revert_cx)
# --- apply v2
def v2_rmr(s):
    if M in s: return s
    assert s.count(ORIG_RMR) == 1, "rmr anchor"
    s = s.replace(ORIG_RMR, ORIG_RMR + f'''
    {M} const assetRootDir = (typeof input.assetStateKey === "string" && input.assetStateKey.length > 0)
        ? path.posix.join(baseWorkspaceRemoteDir, ".paperclip-runtime", "state", input.assetStateKey, input.adapterKey)
        : runtimeRootDir;''', 1)
    assert s.count("path.posix.join(runtimeRootDir, asset.key)") == 2, "asset uses"
    return s.replace("path.posix.join(runtimeRootDir, asset.key)", "path.posix.join(assetRootDir, asset.key)")
rw(RMR, v2_rmr)
def v2_et(s):
    if M in s: return s
    old = "        const prepared = await prepareRemoteManagedRuntime({\n            spec: target.spec,\n            runId: input.runId,\n"
    assert s.count(old) == 1, "et anchor"
    return s.replace(old, old + f"            assetStateKey: input.assetStateKey, {M}\n", 1)
rw(ET, v2_et)
def v2_cx(s):
    if M in s: return s
    old = '''                return await prepareAdapterExecutionTargetRuntime({
                    runId,
                    target: executionTarget,
                    adapterKey: "codex",'''
    assert s.count(old) == 1, "cx anchor"
    new = (f'''                {M} const assetStateKey = (process.env.PAPERCLIP_STABLE_ASSET_STATE === "0") ? undefined
                    : ("task-" + (((typeof context.taskKey === "string" && context.taskKey.trim()) || (typeof context.issueId === "string" && context.issueId.trim()) || runId).replace(/[^A-Za-z0-9_.-]/g, "_")));
                return await prepareAdapterExecutionTargetRuntime({{
                    runId,
                    assetStateKey,
                    target: executionTarget,
                    adapterKey: "codex",''')
    return s.replace(old, new, 1)
rw(CX, v2_cx)
print("patch 10 v2 in place")

# --- v3: replace host-owned entries in the retained home before upload (Greptile P1 on upstream PR #15724)
M3 = "/* PAPERCLIP_PATCH_ASSET_REPLACE */"
def v3_rmr(s):
    if M3 in s: return s
    old = "            const remoteDir = path.posix.join(assetRootDir, asset.key);\n            assetDirs[asset.key] = remoteDir;\n"
    assert s.count(old) == 1, "rmr v3 anchor"
    add = (f"            {M3} const replaceEntries = (asset.replaceEntries ?? []).filter((e) => e && e !== \".\" && e !== \"..\" && !e.includes(\"/\"));\n"
           "            if (assetRootDir !== runtimeRootDir && replaceEntries.length > 0) {\n"
           "                const q = (v) => \"'\" + String(v).replace(/'/g, \"'\\\\''\") + \"'\";\n"
           "                await runSshCommand(input.spec, `mkdir -p ${q(remoteDir)} && cd ${q(remoteDir)} && rm -rf -- ${replaceEntries.map(q).join(\" \")}`, { timeoutMs: 30000 });\n"
           "            }\n")
    return s.replace(old, old + add, 1)
rw(RMR, v3_rmr)
def v3_cx(s):
    if M3 in s: return s
    old = '                                key: "home",\n'
    if s.count(old) != 1:
        import re
        m = re.search(r'\n(\s*)key: "home",\n', s); assert m, "cx v3 anchor"; old = m.group(0)[1:]
    ind = old[:len(old) - len(old.lstrip())]
    return s.replace(old, old + f"{ind}replaceEntries: [\"config.json\", \"config.toml\", \"instructions.md\", \"auth.json\", \"skills\"], {M3}\n", 1)
rw(CX, v3_cx)
print("patch 10 v3 (replace host-owned entries) in place")
