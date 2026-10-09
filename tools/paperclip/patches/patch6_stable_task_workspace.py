#!/usr/bin/env python3
"""Patch 6 (PAPERCLIP_PATCH_STABLE_TASK_WS): stable per-task remote workspace so sessions can resume over ssh.
Upstream puts every ssh run in <remoteWorkspacePath>/.paperclip-runtime/runs/<runId>/workspace. The saved
session identity includes that remoteCwd, so two runs of the same task never match and `--resume` is never
used (verified 2026-10-09: every "resumed" run actually started fresh). With this patch the directory is
runs/task-<taskKey|issueId>/workspace, identical across runs of one task; Claude/Codex then find the saved
session in the same cwd. Opt out with PAPERCLIP_STABLE_TASK_WORKSPACES=0.
Usage: patch6_stable_task_workspace.py <node_modules/@paperclipai dir>"""
import sys, os
NM = sys.argv[1]
def patch(path, old, new, marker):
    s = open(path).read()
    if marker in s: print('already:', os.path.basename(path)); return
    assert s.count(old) == 1, f'anchor not found once in {path}'
    open(path, 'w').write(s.replace(old, new, 1)); print('patched:', os.path.basename(path))
M = '/* PAPERCLIP_PATCH_STABLE_TASK_WS */'
patch(f'{NM}/adapter-utils/dist/remote-managed-runtime.js',
      '? path.posix.join(baseWorkspaceRemoteDir, ".paperclip-runtime", "runs", input.runId, "workspace")',
      f'? path.posix.join(baseWorkspaceRemoteDir, ".paperclip-runtime", "runs", {M} (input.runDirKey ?? input.runId), "workspace")', M)
patch(f'{NM}/adapter-utils/dist/execution-target.js',
      '''        const prepared = await prepareRemoteManagedRuntime({
            spec: target.spec,
            runId: input.runId,''',
      f'''        const prepared = await prepareRemoteManagedRuntime({{
            spec: target.spec,
            runId: input.runId,
            runDirKey: input.runDirKey, {M}''', M)
helper = f'''{M} const stableRunDirKey = (process.env.PAPERCLIP_STABLE_TASK_WORKSPACES === "0") ? runId
                : ("task-" + (((typeof context.taskKey === "string" && context.taskKey.trim()) || (typeof context.issueId === "string" && context.issueId.trim()) || runId).replace(/[^A-Za-z0-9_.-]/g, "_")));
'''
patch(f'{NM}/adapter-claude-local/dist/server/execute.js',
      '''            return await prepareAdapterExecutionTargetRuntime({
                runId,
                target: executionTarget,
                adapterKey: "claude",''',
      helper + '''            return await prepareAdapterExecutionTargetRuntime({
                runId,
                runDirKey: stableRunDirKey,
                target: executionTarget,
                adapterKey: "claude",''', M)
patch(f'{NM}/adapter-codex-local/dist/server/execute.js',
      '''                return await prepareAdapterExecutionTargetRuntime({
                    runId,
                    target: executionTarget,
                    adapterKey: "codex",''',
      helper + '''                return await prepareAdapterExecutionTargetRuntime({
                    runId,
                    runDirKey: stableRunDirKey,
                    target: executionTarget,
                    adapterKey: "codex",''', M)
