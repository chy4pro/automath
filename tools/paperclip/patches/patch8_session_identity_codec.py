#!/usr/bin/env python3
"""Patch 8 (PAPERCLIP_PATCH_SESSION_CODEC): backport of upstream PR #12930 (open) — the claude_local and
codex_local session codecs drop `remoteExecution` (and codex also `mcpServerIdentity`-free), so a saved
session never matches the next run's remote execution identity and `--resume` is never used on ssh/sandbox
targets. Keep the identity keys through the codec round trip (same key whitelist as the PR; never the
privateKey/knownHosts). Usage: patch8_session_identity_codec.py <@paperclipai dir>"""
import sys
NM = sys.argv[1]; M = '/* PAPERCLIP_PATCH_SESSION_CODEC */'
HELPER = f'''{M}
const REMOTE_EXECUTION_IDENTITY_KEYS = ["transport", "host", "port", "username", "remoteCwd", "providerKey", "environmentId", "leaseId"];
function readRemoteExecutionIdentity(value) {{
    if (typeof value !== "object" || value === null || Array.isArray(value)) return null;
    const identity = {{}};
    for (const key of REMOTE_EXECUTION_IDENTITY_KEYS) {{ if (value[key] !== undefined && value[key] !== null) identity[key] = value[key]; }}
    return Object.keys(identity).length > 0 ? identity : null;
}}
export const sessionCodec = {{'''
for a in ('claude', 'codex'):
    p = f'{NM}/adapter-{a}-local/dist/server/index.js'; s = open(p).read()
    if M in s: print('already:', a); continue
    assert s.count('export const sessionCodec = {') == 1
    s = s.replace('export const sessionCodec = {', HELPER, 1)
    # deserialize: after workspaceId line (record.*) add remoteExecution; serialize: after workspaceId line (params.*)
    for src in ('record', 'params'):
        old = f'''        const workspaceId = readNonEmptyString({src}.workspaceId) ?? readNonEmptyString({src}.workspace_id);'''
        new = old + f'''
        const remoteExecution = readRemoteExecutionIdentity({src}.remoteExecution) ?? readRemoteExecutionIdentity({src}.remote_execution);'''
        assert s.count(old) == 1, f'{a}:{src} workspaceId anchor'
        s = s.replace(old, new, 1)
    old = '''            ...(workspaceId ? { workspaceId } : {}),'''
    assert s.count(old) == 2, f'{a}: workspaceId spread count'
    s = s.replace(old, old + '''
            ...(remoteExecution ? { remoteExecution } : {}),''')
    open(p, 'w').write(s); print('patched:', a)
