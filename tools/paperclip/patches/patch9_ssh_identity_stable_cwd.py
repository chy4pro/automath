#!/usr/bin/env python3
"""Patch 9 (PAPERCLIP_PATCH_SSH_IDENTITY): the ssh remote execution identity used for session resume must not
include the per-run workspace directory. Every ssh run executes in <remoteWorkspacePath>/.paperclip-runtime/runs/<runId>/workspace,
so an identity keyed on that path never matches the next run of the same task and `--resume` is never used
(verified 2026-10-09 after backporting #12930: the saved identity carried the per-run path). Key it on the
environment's remoteWorkspacePath instead; Claude CLI resumes a session id from any cwd (verified locally) and
Codex sessions are stored globally. Usage: patch9_ssh_identity_stable_cwd.py <@paperclipai dir>"""
import sys
NM = sys.argv[1]; p = f'{NM}/adapter-utils/dist/remote-managed-runtime.js'; s = open(p).read()
M = '/* PAPERCLIP_PATCH_SSH_IDENTITY */'
if M in s: print('already: patch 9'); sys.exit(0)
old = '''        username: spec.username,
        remoteCwd: spec.remoteCwd,
    };
}'''
new = f'''        username: spec.username,
        remoteCwd: {M} (typeof spec.remoteWorkspacePath === "string" && spec.remoteWorkspacePath.trim().length > 0) ? spec.remoteWorkspacePath.trim() : spec.remoteCwd,
    }};
}}'''
assert s.count(old) == 1, 'anchor'
open(p, 'w').write(s.replace(old, new, 1)); print('patch 9 applied: ssh identity keyed on remoteWorkspacePath')
