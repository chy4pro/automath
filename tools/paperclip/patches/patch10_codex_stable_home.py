#!/usr/bin/env python3
"""Patch 10 (PAPERCLIP_PATCH_STABLE_RUNTIME_ROOT): on ssh targets keep the adapter runtime root (which holds
CODEX_HOME for codex_local: config, skills, auth and the session rollouts) in a per-task directory instead of
the per-run one, so `codex resume <id>` finds the previous run's rollout. Verified 2026-10-09: with patches 8/9/9b
Codex attempted the resume but answered "no rollout found for thread id" because the per-run home was new.
The home asset sync overlays with tar (no clear), so sessions/ persists. Workspace dirs stay per run.
Usage: patch10_codex_stable_home.py <@paperclipai dir>"""
import sys, os
NM = sys.argv[1]; M = "/* PAPERCLIP_PATCH_STABLE_RUNTIME_ROOT */"
def patch(path, old, new):
    s = open(path).read()
    if M in s: print("already:", os.path.basename(path)); return
    assert s.count(old) == 1, f"anchor not found once in {path}"
    open(path, "w").write(s.replace(old, new, 1)); print("patched:", os.path.basename(path))
patch(f"{NM}/adapter-utils/dist/remote-managed-runtime.js",
      '    const runtimeRootDir = path.posix.join(workspaceRemoteDir, ".paperclip-runtime", input.adapterKey);',
      f'    const runtimeRootDir = {M} (typeof input.runtimeRootKey === "string" && input.runtimeRootKey.length > 0)\n'
      '        ? path.posix.join(baseWorkspaceRemoteDir, ".paperclip-runtime", "runtime", input.runtimeRootKey, input.adapterKey)\n'
      '        : path.posix.join(workspaceRemoteDir, ".paperclip-runtime", input.adapterKey);')
patch(f"{NM}/adapter-utils/dist/execution-target.js",
      '''        const prepared = await prepareRemoteManagedRuntime({
            spec: target.spec,
            runId: input.runId,''',
      f'''        const prepared = await prepareRemoteManagedRuntime({{
            spec: target.spec,
            runId: input.runId,
            runtimeRootKey: input.runtimeRootKey, {M}''')
patch(f"{NM}/adapter-codex-local/dist/server/execute.js",
      '''                return await prepareAdapterExecutionTargetRuntime({
                    runId,
                    target: executionTarget,
                    adapterKey: "codex",''',
      f'''                {M} const stableRuntimeRootKey = (process.env.PAPERCLIP_STABLE_RUNTIME_ROOT === "0") ? undefined
                    : ("task-" + (((typeof context.taskKey === "string" && context.taskKey.trim()) || (typeof context.issueId === "string" && context.issueId.trim()) || runId).replace(/[^A-Za-z0-9_.-]/g, "_")));
                return await prepareAdapterExecutionTargetRuntime({{
                    runId,
                    runtimeRootKey: stableRuntimeRootKey,
                    target: executionTarget,
                    adapterKey: "codex",''')
