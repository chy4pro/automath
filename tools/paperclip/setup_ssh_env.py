#!/usr/bin/env python3
"""Register an AI container as a Paperclip `ssh` environment and create one agent on it.
Needs a board API token (file path in PAPERCLIP_BOARD_TOKEN_FILE, default /wb/creds/paperclip-board-token/value).
Usage: setup_ssh_env.py --host 192.168.166.3 --name claude-box --agent coordinator-ssh --adapter claude_local
       [--port 2222] [--user agent] [--remote-path /work/.paperclip/ws/<name>] [--model claude-fable-5-1]
Never prints secrets. Idempotent on names (reuses existing secret/environment/agent with the same name)."""
import argparse, json, os, sys, urllib.request, urllib.error
BASE = os.environ.get("PAPERCLIP_API_URL", "http://wb-proj-656d7af54e8b:3100/api")
TOK = open(os.environ.get("PAPERCLIP_BOARD_TOKEN_FILE", "/wb/creds/paperclip-board-token/value")).read().strip()
def req(method, path, data=None):
    body = json.dumps(data).encode() if data is not None else None
    r = urllib.request.Request(BASE + path, data=body, method=method,
        headers={"Authorization": "Bearer " + TOK, "Content-Type": "application/json", "Origin": "https://automath.mozone.io"})
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            t = resp.read(); return json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} -> {e.code}: {e.read()[:400]}")
ap = argparse.ArgumentParser(); ap.add_argument("--host", required=True); ap.add_argument("--name", required=True)
ap.add_argument("--agent", required=True); ap.add_argument("--adapter", default="claude_local"); ap.add_argument("--port", type=int, default=2222)
ap.add_argument("--user", default="agent"); ap.add_argument("--remote-path"); ap.add_argument("--model", default=None)
ap.add_argument("--key", default="/work/.paperclip/ssh/paperclip_ed25519"); ap.add_argument("--known-hosts", default="/work/.paperclip/ssh/known_hosts")
ap.add_argument("--instructions", default=None, help="markdown file for the agent's instructions bundle / prompt")
ap.add_argument("--company", default=None, help="company id (default: the first company)")
a = ap.parse_args()
remote_path = a.remote_path or f"/work/.paperclip/ws/{a.name}"
cos = req("GET", "/companies"); cos = cos if isinstance(cos, list) else cos.get("companies") or cos.get("items") or []
cid = a.company or (cos[0]["id"] if cos else sys.exit("no company yet: create one in the UI first"))
print("company", cid)
# 1. private key as a company secret
secs = req("GET", f"/companies/{cid}/secrets"); secs = secs if isinstance(secs, list) else secs.get("secrets") or secs.get("items") or []
sname = f"ssh-key-{a.name}"
sec = next((s for s in secs if s.get("name") == sname), None)
if not sec:
    sec = req("POST", f"/companies/{cid}/secrets", {"name": sname, "key": f"SSH_KEY_{a.name.upper().replace('-','_')}",
           "provider": "local_encrypted", "managedMode": "paperclip_managed", "value": open(a.key).read(),
           "description": f"Paperclip's SSH private key for the {a.name} container"})
    print("secret created")
else: print("secret exists")
sid = sec["id"]
# 2. ssh environment
envs = req("GET", f"/companies/{cid}/environments"); envs = envs if isinstance(envs, list) else envs.get("environments") or envs.get("items") or []
env = next((e for e in envs if e.get("name") == a.name), None)
cfg = {"host": a.host, "port": a.port, "username": a.user, "remoteWorkspacePath": remote_path,
       "privateKeySecretRef": {"type": "secret_ref", "secretId": sid, "version": "latest"},
       "knownHosts": open(a.known_hosts).read() if os.path.exists(a.known_hosts) else None,
       "strictHostKeyChecking": bool(os.path.exists(a.known_hosts))}
if not env:
    env = req("POST", f"/companies/{cid}/environments", {"name": a.name, "driver": "ssh", "status": "active",
              "description": f"Workbench AI container {a.name} via unprivileged sshd", "config": cfg})
    print("environment created", env.get("id"))
else:
    env = req("PATCH", f"/environments/{env['id']}", {"config": cfg}); print("environment updated", env.get("id"))
eid = env["id"]
probe = req("POST", f"/environments/{eid}/probe", {})
print("probe:", json.dumps(probe)[:600])
# 3. agent bound to the environment
ags = req("GET", f"/companies/{cid}/agents"); ags = ags if isinstance(ags, list) else ags.get("agents") or ags.get("items") or []
ag = next((g for g in ags if g.get("name") == a.agent), None)
acfg = {"cwd": remote_path, "timeoutSec": 3600, "maxTurnsPerRun": 200}
if a.model: acfg["model"] = a.model
if a.instructions: acfg["promptTemplate"] = open(a.instructions).read()
if a.adapter == "codex_local": acfg["modelReasoningEffort"] = "xhigh"
if not ag:
    ag = req("POST", f"/companies/{cid}/agents", {"name": a.agent, "role": "researcher", "adapterType": a.adapter,
             "adapterConfig": acfg, "defaultEnvironmentId": eid})
    print("agent created", ag.get("id"))
else:
    ag = req("PATCH", f"/agents/{ag['id']}", {"adapterConfig": acfg, "defaultEnvironmentId": eid}); print("agent updated", ag.get("id"))
print("done:", a.agent, "→ environment", a.name, f"({a.user}@{a.host}:{a.port}, cwd {remote_path})")
