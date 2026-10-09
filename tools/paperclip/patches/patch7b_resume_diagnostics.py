#!/usr/bin/env python3
"""Patch 7b: resume diagnostics from upstream #15437. Without it the claude_local adapter prints
"does not match the current remote execution identity and will not be resumed" on every ssh run — the old
else-if branch fired whenever the host-side session cwd differed from the remote run directory, which is
always the case on ssh — even when the session WAS resumed (verified 2026-10-09: same session id and one
conversation file spanning three runs). Usage: patch7b_resume_diagnostics.py <@paperclipai dir>"""
import sys
NM = sys.argv[1]; p = f"{NM}/adapter-claude-local/dist/server/execute.js"; s = open(p).read()
M = "/* PAPERCLIP_PATCH_RESUME_DIAG */"
if M in s: print("already: patch 7b"); sys.exit(0)
OLD = (
"    if (executionTargetIsRemote &&\n"
"        runtimeSessionId &&\n"
"        isValidUuid &&\n"
"        !canResumeSession) {\n"
"        await onLog(\"stdout\", `[paperclip] Claude session \"${runtimeSessionId}\" does not match the current remote execution identity and will not be resumed in \"${effectiveExecutionCwd}\". Starting a fresh remote session.\\n`);\n"
"    }\n"
"    else if (runtimeSessionId &&\n"
"        isValidUuid &&\n"
"        runtimeSessionCwd.length > 0 &&\n"
"        path.resolve(runtimeSessionCwd) !== path.resolve(effectiveExecutionCwd)) {\n"
"        await onLog(\"stdout\", `[paperclip] Claude session \"${runtimeSessionId}\" does not match the current remote execution identity and will not be resumed in \"${effectiveExecutionCwd}\". Starting a fresh remote session.\\n`);\n"
"    }\n"
"    else if (runtimeSessionId && isValidUuid && !canResumeSession) {\n"
"        await onLog(\"stdout\", `[paperclip] Claude session \"${runtimeSessionId}\" was saved for cwd \"${runtimeSessionCwd}\" and will not be resumed in \"${effectiveExecutionCwd}\".\\n`);\n"
"    }\n")
NEW = (
f"    {M}\n"
"    const hasMatchingExecutionTargetPC = adapterExecutionTargetSessionMatches(runtimeRemoteExecution, runtimeExecutionTarget);\n"
"    const hasMatchingSessionCwdPC = claudeSessionCwdMatchesExecutionTarget({ runtimeSessionCwd, effectiveExecutionCwd, executionTargetIsRemote });\n"
"    if (runtimeSessionId && isValidUuid && !hasMatchingExecutionTargetPC) {\n"
"        await onLog(\"stdout\", `[paperclip] Claude session \"${runtimeSessionId}\" does not match the current execution target and will not be resumed in \"${effectiveExecutionCwd}\". Starting a fresh session.\\n`);\n"
"    }\n"
"    else if (runtimeSessionId && isValidUuid && runtimeSessionCwd.length > 0 && !hasMatchingSessionCwdPC) {\n"
"        await onLog(\"stdout\", `[paperclip] Claude session \"${runtimeSessionId}\" was saved for cwd \"${runtimeSessionCwd}\" and will not be resumed in \"${effectiveExecutionCwd}\".\\n`);\n"
"    }\n"
"    else if (runtimeSessionId && isValidUuid && canResumeSession) {\n"
"        await onLog(\"stdout\", `[paperclip] Resuming Claude session \"${runtimeSessionId}\" (prompt bundle, MCP set and execution target unchanged).\\n`);\n"
"    }\n")
assert s.count(OLD) == 1, "anchor"
open(p, "w").write(s.replace(OLD, NEW, 1)); print("patch 7b applied: resume diagnostics")
