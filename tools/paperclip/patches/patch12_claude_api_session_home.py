#!/usr/bin/env python3
"""Patch 12 (PAPERCLIP_PATCH_CLAUDE_API_CONFIG_DIR): claude_local with an AI-connection binding (e.g. a Claude API key)
on an ssh target. Paperclip prepares a managed home on the *host* (mkdtemp /tmp/paperclip-ai-<company>-<grant>-XXXXXX)
and sets CLAUDE_CONFIG_DIR to its provider/ directory. Only sandbox targets remap that to a remote directory
(adapterExecutionTargetUsesManagedHome is sandbox-only), so on ssh the host path is passed to the remote process,
Claude Code creates it under the remote /tmp, writes the session there, and the next run gets a new random path:
"Claude resume session ... is unavailable; retrying with a fresh session", plus one stray /tmp directory per run
(observed 2026-10-11 on the API probe). This points CLAUDE_CONFIG_DIR, for managed-connection runs on non-sandbox
remote targets only, at a fixed directory in the environment's remote workspace (<remoteWorkspacePath>/.paperclip-runtime/
claude-api-config), and drops the host-only HOME / XDG_CONFIG_HOME / XDG_DATA_HOME that the managed home also sets: on the
remote they made `~` a throwaway /tmp path (no ~/.venv-automath, gh login or git config, one /tmp directory per run).
The run then uses the remote account's real home like subscription runs do. Authentication still comes only from the
injected ANTHROPIC_API_KEY (Claude Code reads credentials from CLAUDE_CONFIG_DIR, which holds none). Subscription runs
are unchanged.
Usage: patch12_claude_api_session_home.py <@paperclipai dir>"""
import sys
p = f"{sys.argv[1]}/adapter-claude-local/dist/server/execute.js"; s = open(p).read()
M = "/* PAPERCLIP_PATCH_CLAUDE_API_CONFIG_DIR */"
if M in s: print("already: patch 12"); sys.exit(0)
anchor = '''    const remoteClaudeConfigDir = useManagedRemoteClaudeConfig && remoteClaudeRuntimeRoot
        ? path.posix.join(remoteClaudeRuntimeRoot, "config")
        : null;
'''
assert s.count(anchor) == 1, "anchor"
add = (f'''    {M} if (executionTargetIsRemote && config.managedAiConnection && !useManagedRemoteClaudeConfig) {{
        const stableClaudeConfigDir = path.posix.join(adapterExecutionTargetRemoteCwd(executionTarget, cwd), ".paperclip-runtime", "claude-api-config");
        env.CLAUDE_CONFIG_DIR = stableClaudeConfigDir;
        loggedEnv.CLAUDE_CONFIG_DIR = stableClaudeConfigDir;
        for (const k of ["HOME", "XDG_CONFIG_HOME", "XDG_DATA_HOME"]) {{ delete env[k]; delete loggedEnv[k]; }}
        await onLog("stdout", `[paperclip] AI connection on a non-sandbox remote: CLAUDE_CONFIG_DIR -> ${{stableClaudeConfigDir}} (stable, so sessions resume); remote HOME kept.\\n`);
    }}
''')
s = s.replace(anchor, anchor + add, 1); open(p, "w").write(s); print("patched: 12 stable CLAUDE_CONFIG_DIR for AI-connection runs on ssh")
