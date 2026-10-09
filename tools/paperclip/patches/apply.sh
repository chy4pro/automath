#!/bin/sh
# Local patches to the installed Paperclip (npm prefix /work/.tools/npm). Idempotent; re-run after `npm install -g paperclipai`.
# Why: upstream `codex_local` allows a REMOTE's own ~/.codex/auth.json only for sandbox transports; ssh targets are forced
# to use the Paperclip host's login. We let ssh targets behave like sandboxes: (1) the credential gate probes the remote
# for ~/.codex/auth.json instead of refusing; (2) after the managed CODEX_HOME is uploaded over ssh, auth.json falls back
# to the remote's own login (same rule as codex-auth-merge-extract.sh uses for sandboxes).
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
/work/.tools/node/bin/node --check "$EX" && /work/.tools/node/bin/node --check "$RM" && echo "syntax ok"
