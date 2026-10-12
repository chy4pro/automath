#!/usr/bin/env python3
"""Paperclip seats on the machine "muse" (Claude Code, Codex, Antigravity). Idempotent by name.

Path: Paperclip host -> Workbench host Mac's Tailscale -> muse userspace tailscaled -> muse sshd on 127.0.0.1:22
(/home/hatch/.local/share/paperclip-sshd, user root).
The CLIs on muse are the owner's keygate wrappers, launched through /home/hatch/pcbin/<cli> (sets HOME).
The SSH key lives only in Paperclip's secret store (secret "ssh-key-muse"); to recreate it pass MUSE_KEY_FILE.
"""
import json, os, subprocess, sys
sys.path.insert(0, "/work/tools/paperclip"); from pc import call
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
# Transport: muse's tailnet address, reached through the Workbench host Mac's Tailscale (containers route 100.64.0.0/10
# via the Mac) to muse's userspace tailscaled, which forwards inbound TCP to its loopback sshd.
MUSE_HOST, MUSE_PORT = "100.101.197.73", 22
MUSE_HOSTKEY = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKpt+vA3qyelu3exYrPtgfqS9rQ7auVqCoh0U3gtR5JF"
AG = "/work/tools/paperclip/agents"
SEATS = [
 # name, title, icon, adapter, command on muse, model, extra adapter config
 # muse-claude (owner, 2026-10-12): Claude Code with muse's own API login (ANTHROPIC_API_KEY in /home/hatch/.claude/settings.json,
 # which takes precedence over the process environment). The placeholder ANTHROPIC_API_KEY below never reaches the API; it
 # only makes Paperclip record these runs as API-billed, so they count against the $200 budget. Background tasks off.
 ("muse-claude", "Muse worker (Claude Code on the API, Opus 5.5) - long or heavy jobs on muse", "cpu", "claude_local", "/home/hatch/pcbin/claude-api", "claude-opus-5-5",
  {"env": {"ANTHROPIC_API_KEY": "placeholder-muse-settings-key-is-used", "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1"},
   "extraArgs": ["--disallowedTools=CronCreate,CronDelete,CronList,Monitor"]}),
 # OPENAI_API_KEY is a placeholder that only satisfies Paperclip's pre-run Codex credential gate; codex-keygate deletes
 # it from the environment before starting Codex, which then authenticates through the keygate provider.
 # Two clean-room attackers on muse (owner, 2026-10-12), Claude Code on muse's API login like muse-claude.
 ("muse-attacker-1", "Attacker on muse (Claude API, Opus 5.5, clean room)", "swords", "claude_local", "/home/hatch/pcbin/claude-api", "claude-opus-5-5",
  {"env": {"ANTHROPIC_API_KEY": "placeholder-muse-settings-key-is-used", "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1", "AUTOMATH_CLEAN_ROOM": "1"},
   "extraArgs": ["--disallowedTools=CronCreate,CronDelete,CronList,Monitor"]}),
 ("muse-attacker-2", "Attacker on muse (Claude API, Opus 5.5, clean room)", "swords", "claude_local", "/home/hatch/pcbin/claude-api", "claude-opus-5-5",
  {"env": {"ANTHROPIC_API_KEY": "placeholder-muse-settings-key-is-used", "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1", "AUTOMATH_CLEAN_ROOM": "1"},
   "extraArgs": ["--disallowedTools=CronCreate,CronDelete,CronList,Monitor"]}),
 ("muse-codex", "Muse worker (Codex, GPT-6 Astra)", "cpu", "codex_local", "/home/hatch/pcbin/codex", "gpt-6-astra",
  {"modelReasoningEffort": "xhigh", "env": {"OPENAI_API_KEY": "placeholder-stripped-by-codex-keygate"}}),
 ("muse-agy", "Muse worker (Antigravity, Gemini 3.1 Pro)", "cpu", "agy_local", "/home/hatch/pcbin/agy", "gemini-3.1-pro-high", {}),
]

secs = call("GET", f"/companies/{C}/secrets"); secs = secs if isinstance(secs, list) else secs.get("secrets", [])
sec = next((x for x in secs if x["name"] == "ssh-key-muse"), None)
if not sec:
    kf = os.environ.get("MUSE_KEY_FILE") or sys.exit("secret ssh-key-muse missing: set MUSE_KEY_FILE to the private key")
    sec = call("POST", f"/companies/{C}/secrets", {"name": "ssh-key-muse", "key": "SSH_KEY_MUSE", "provider": "local_encrypted",
        "managedMode": "paperclip_managed", "value": open(kf).read(),
        "description": "Paperclip's SSH key for muse (root, loopback sshd behind the Workbench SSH bridge)"})
envs = {e["name"]: e for e in call("GET", f"/companies/{C}/environments")}
agents = {a["name"]: a for a in call("GET", f"/companies/{C}/agents")}
coord = (agents.get("coordinator-api") or agents["coordinator"])["id"]   # the API coordinator since 2026-10-11
bundle_text = open(f"{AG}/muse.md").read() + "\n" + open(f"{AG}/_common.md").read()
bundle_api = open(f"{AG}/muse.md").read() + "\n" + open(f"{AG}/api_org.md").read() + "\n" + open(f"{AG}/_common.md").read()
bundle_attacker = open(f"{AG}/attacker.md").read() + "\n" + open(f"{AG}/muse_attacker.md").read() + "\n" + open(f"{AG}/api_org.md").read() + "\n" + open(f"{AG}/_common.md").read()
def bundle_for(name): return bundle_attacker if name.startswith("muse-attacker") else bundle_api if name == "muse-claude" else bundle_text
env_ids = json.load(open("/work/.paperclip/env_ids.json")); agent_ids = json.load(open("/work/.paperclip/agent_ids.json"))
ONLY = set(sys.argv[1:])
for name, title, icon, adapter, command, model, extra in SEATS:
    if ONLY and name not in ONLY: continue
    cfg = {"host": MUSE_HOST, "port": MUSE_PORT, "username": "root", "remoteWorkspacePath": f"/home/hatch/pcws/{name}",
           "privateKeySecretRef": {"type": "secret_ref", "secretId": sec["id"], "version": "latest"},
           "knownHosts": f"{MUSE_HOST} {MUSE_HOSTKEY}\n", "strictHostKeyChecking": True}
    body = {"name": f"ws-{name}", "driver": "ssh", "status": "active", "config": cfg, "description": f"muse, private workspace for {name}"}
    e = call("PATCH", f"/environments/{envs[body['name']]['id']}", body) if body["name"] in envs \
        else call("POST", f"/companies/{C}/environments", body)
    probe = call("POST", f"/environments/{e['id']}/probe", {})
    # The host-side workspace must be its own (tiny) git repository. Otherwise git discovery climbs into /work and
    # Paperclip ships the whole project repository (~260 MB) over the bridge on every run and copies it back.
    host_ws = f"/work/.paperclip/host-ws/{name}"
    for d in (host_ws, f"/work/.paperclip/instances/default/workspaces/{agents[name]['id']}" if name in agents else None):
        if d and not os.path.isfile(f"{d}/.git/HEAD"):
            os.makedirs(d, exist_ok=True); subprocess.run(["rm", "-rf", f"{d}/.git"], check=True)
            subprocess.run(["git", "-C", d, "init", "-q"], check=True)
            subprocess.run(["git", "-C", d, "-c", "user.name=paperclip", "-c", "user.email=paperclip@localhost", "commit", "-q",
                            "--allow-empty", "-m", "muse seat workspace root"], check=True)
    extra = dict(extra); env = {"PAPERCLIP_AGENT_NAME": name, **extra.pop("env", {})}
    acfg = {"cwd": host_ws, "command": command, "model": model, "timeoutSec": 3600, "env": env, **extra}
    if adapter in ("claude_local", "codex_local"): acfg.update({"engine": "cli", "maxTurnsPerRun": 200})
    a_body = {"name": name, "title": title, "icon": icon, "role": "researcher", "reportsTo": coord, "adapterType": adapter,
              "adapterConfig": acfg, "defaultEnvironmentId": e["id"], "capabilities": title,
              "instructionsBundle": {"entryFile": "AGENTS.md", "files": {"AGENTS.md": bundle_for(name)}},
              "permissions": {"canCreateAgents": False, "canCreateSkills": False, "trustPreset": "standard"}}
    if name in agents:
        a = call("PATCH", f"/agents/{agents[name]['id']}", {k: v for k, v in a_body.items() if k not in ("permissions", "instructionsBundle")})
        cur = call("GET", f"/agents/{a['id']}/instructions-bundle/file?path=AGENTS.md")
        want = bundle_for(name)
        if cur.get("content") != want:
            call("PUT", f"/agents/{a['id']}/instructions-bundle/file", {"path": "AGENTS.md", "content": want,
                 "baseRevisionId": (cur.get("revision") or {}).get("id"), "baseHash": cur.get("contentHash")})
        verb = "updated"
    else:
        a = call("POST", f"/companies/{C}/agents", a_body); verb = "created"
    env_ids[name], agent_ids[name] = e["id"], a["id"]
    print(f"{verb} {name:12s} agent {a['id']} env {e['id']} probe={probe.get('ok')}")
json.dump(env_ids, open("/work/.paperclip/env_ids.json", "w"), indent=1)
json.dump(agent_ids, open("/work/.paperclip/agent_ids.json", "w"), indent=1)
