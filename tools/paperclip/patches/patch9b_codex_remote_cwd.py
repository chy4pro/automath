#!/usr/bin/env python3
"""Patch 9b: codex_local never resumes on remote targets because canResumeSession also requires the saved
(host-side) cwd to equal the remote per-run execution cwd. Skip that comparison for remote targets, as the
claude_local adapter already does (claudeSessionCwdMatchesExecutionTarget returns true when remote); the
remote execution identity check still guards host/user/workspace. Usage: patch9b_codex_remote_cwd.py <@paperclipai dir>"""
import sys
NM = sys.argv[1]; p = f"{NM}/adapter-codex-local/dist/server/execute.js"; s = open(p).read()
M = "/* PAPERCLIP_PATCH_CODEX_REMOTE_CWD */"
if M in s: print("already: patch 9b"); sys.exit(0)
old = """        const canResumeSession = runtimeSessionId.length > 0 &&
            (runtimeSessionCwd.length === 0 || path.resolve(runtimeSessionCwd) === path.resolve(effectiveExecutionCwd)) &&
            adapterExecutionTargetSessionMatches(runtimeRemoteExecution, runtimeExecutionTarget);"""
new = f"""        const canResumeSession = runtimeSessionId.length > 0 &&
            (runtimeSessionCwd.length === 0 || executionTargetIsRemote {M} || path.resolve(runtimeSessionCwd) === path.resolve(effectiveExecutionCwd)) &&
            adapterExecutionTargetSessionMatches(runtimeRemoteExecution, runtimeExecutionTarget);"""
assert s.count(old) == 1, "anchor"
open(p, "w").write(s.replace(old, new, 1)); print("patch 9b applied: codex remote cwd check")
