#!/usr/bin/env python3
"""The automath Claude agents on the Claude API (owner decision 2026-10-11): coordinator, two referees and the verifier
run Claude Code in the Claude container over ssh, bound to the owner's Claude API connection (metered billing) instead
of the subscription. Codex work stays on Codex: scout, attacker-1/2, formalizer and muse-codex keep running GPT-6 Astra
and now report to coordinator-api. The subscription Claude agents are kept and stay paused. API spend is capped by a
company budget policy ($200 lifetime, hard stop). Idempotent by agent name; new agents are paused after creation and
`python3 resume_all.py` starts this org when the owner says so.

Needs patch 12 (tools/paperclip/patches): with an AI-connection binding on ssh, claude_local otherwise loses the session
between runs and runs with a throwaway HOME."""
import json, os, subprocess, sys
sys.path.insert(0, "/work/tools/paperclip"); from pc import call
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
AG = "/work/tools/paperclip/agents"
CLAUDE_BOX = {"host": "192.168.166.3", "port": 2222, "username": "agent"}
BINDING = {"mode": "responsible_user", "provider": "anthropic", "method": "api_key"}
ROLES = [
 # name, title, icon, role file, model, extra env
 ("coordinator-api", "Coordinator (Claude API, Opus 5.5) - single decision maker", "crown", "coordinator", "claude-opus-5-5", {}),
 ("referee-api-1", "Referee (Claude API, isolated, adversarial, same-vendor)", "shield", "referee", "claude-opus-5-5", {}),
 ("referee-api-2", "Referee (Claude API, isolated, adversarial, same-vendor)", "shield", "referee", "claude-opus-5-5", {}),
 ("verifier-api", "Verifier (Claude API, Sonnet 5.5) - finite checks and numerics", "microscope", "verifier", "claude-sonnet-5-5", {}),
]

def git_root(d):
    """Host-side workspace as its own tiny git repository, so Paperclip never ships the /work repository per run."""
    os.makedirs(d, exist_ok=True)
    if not os.path.isfile(f"{d}/.git/HEAD"):
        subprocess.run(["rm", "-rf", f"{d}/.git"], check=True)
        subprocess.run(["git", "-C", d, "init", "-q"], check=True)
        subprocess.run(["git", "-C", d, "-c", "user.name=paperclip", "-c", "user.email=paperclip@localhost", "commit", "-q",
                        "--allow-empty", "-m", "api org workspace root"], check=True)

def bundle(role):
    text = open(f"{AG}/{role}.md").read() + "\n" + open(f"{AG}/api_org.md").read() + "\n" + open(f"{AG}/_common.md").read()
    if role == "coordinator":
        text += "\n\n" + open("/work/notes/OWNER_RULES.md").read()
    return text

secs = call("GET", f"/companies/{C}/secrets"); secs = secs if isinstance(secs, list) else secs.get("secrets", [])
key = next(x for x in secs if x["name"] == "ssh-key-paperclip")
known = call("GET", f"/environments/{json.load(open('/work/.paperclip/env_ids.json'))['verifier']}")["config"]["knownHosts"]
envs = {e["name"]: e for e in call("GET", f"/companies/{C}/environments")}
agents = {a["name"]: a for a in call("GET", f"/companies/{C}/agents")}
ids = {}
for name, title, icon, rf, model, extra in ROLES:
    cfg = {**CLAUDE_BOX, "remoteWorkspacePath": f"/home/agent/pcws/{name}", "knownHosts": known, "strictHostKeyChecking": True,
           "privateKeySecretRef": {"type": "secret_ref", "secretId": key["id"], "version": "latest"}}
    ebody = {"name": f"ws-{name}", "driver": "ssh", "status": "active", "config": cfg, "description": f"Claude container, private workspace for {name}"}
    e = call("PATCH", f"/environments/{envs[ebody['name']]['id']}", ebody) if ebody["name"] in envs \
        else call("POST", f"/companies/{C}/environments", ebody)
    host_ws = f"/work/.paperclip/host-ws/{name}"; git_root(host_ws)
    body = {"name": name, "title": title, "icon": icon, "role": "ceo" if rf == "coordinator" else "researcher",
            "adapterType": "claude_local", "defaultEnvironmentId": e["id"], "capabilities": title,
            "adapterConfig": {"cwd": host_ws, "model": model, "engine": "cli", "timeoutSec": 3600, "maxTurnsPerRun": 200,
                              "env": {"PAPERCLIP_AGENT_NAME": name, **extra}},
            "runtimeConfig": {"heartbeat": {"enabled": False, "maxConcurrentRuns": 1}, "aiConnection": BINDING},
            "instructionsBundle": {"entryFile": "AGENTS.md", "files": {"AGENTS.md": bundle(rf)}},
            "permissions": {"canCreateAgents": rf == "coordinator", "canCreateSkills": False, "trustPreset": "standard"}}
    if rf != "coordinator":
        body["reportsTo"] = ids["coordinator-api"]
    if name in agents:
        a = call("PATCH", f"/agents/{agents[name]['id']}", {k: v for k, v in body.items() if k not in ("permissions", "instructionsBundle")})
        cur = call("GET", f"/agents/{a['id']}/instructions-bundle/file?path=AGENTS.md")
        new = body["instructionsBundle"]["files"]["AGENTS.md"]
        if cur.get("content") != new:
            call("PUT", f"/agents/{a['id']}/instructions-bundle/file", {"path": "AGENTS.md", "content": new,
                 "baseRevisionId": (cur.get("revision") or {}).get("id"), "baseHash": cur.get("contentHash")})
        verb = "updated"
    else:
        a = call("POST", f"/companies/{C}/agents", body); verb = "created"
        call("POST", f"/agents/{a['id']}/pause", {})
    ids[name] = a["id"]
    probe = call("POST", f"/environments/{e['id']}/probe", {}).get("ok")
    full = call("GET", f"/agents/{a['id']}")
    print(f"{verb:7s} {name:15s} {model:18s} status={full['status']:7s} env probe={probe} api-binding={bool((full.get('runtimeConfig') or {}).get('aiConnection'))}")
# Codex seats keep their engine and report to the API coordinator.
for n in ("scout", "attacker-1", "attacker-2", "formalizer", "muse-codex"):
    if n in agents:
        call("PATCH", f"/agents/{agents[n]['id']}", {"reportsTo": ids["coordinator-api"]}); print(f"codex   {n:15s} reports to coordinator-api")
json.dump(ids, open("/work/.paperclip/api_agent_ids.json", "w"), indent=1)
