#!/usr/bin/env python3
"""One ssh environment per agent (same host, private remoteWorkspacePath) so agents sharing a
container never share a workspace. Reuses the per-host key secret. Idempotent by name."""
import json, os, urllib.request
API = "http://wb-proj-656d7af54e8b:3100/api"; COMPANY = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
TOK = open(os.environ.get("PAPERCLIP_BOARD_TOKEN_FILE", "/work/.paperclip/board.token")).read().strip()
KH = open("/work/.paperclip/ssh/known_hosts").read()
HOSTS = {"claude": ("192.168.166.3", "4e2622cb-dc03-4cc6-8f9e-793cb5412831"),
         "codex": ("192.168.166.4", "b71394f2-5c43-48f6-b281-c73e18785a75")}
AGENTS = {"coordinator": "claude", "referee-1": "claude", "referee-2": "claude", "verifier": "claude",
          "scout": "codex", "attacker-1": "codex", "attacker-2": "codex", "formalizer": "codex"}
def api(m, p, b=None):
    r = urllib.request.Request(API + p, method=m, data=json.dumps(b).encode() if b is not None else None,
        headers={"Authorization": "Bearer " + TOK, "Content-Type": "application/json", "Origin": "https://automath.mozone.io"})
    try:
        with urllib.request.urlopen(r) as x: return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e: print(m, p, e.code, e.read().decode()[:300]); raise
envs = {e["name"]: e for e in api("GET", f"/companies/{COMPANY}/environments")}
ids = json.load(open("/work/.paperclip/agent_ids.json")); out = {}
for name, box in AGENTS.items():
    host, sec = HOSTS[box]
    cfg = {"host": host, "port": 2222, "username": "agent", "remoteWorkspacePath": f"/home/agent/pcws/{name}",
           "privateKeySecretRef": {"type": "secret_ref", "secretId": sec, "version": "latest"},
           "knownHosts": KH, "strictHostKeyChecking": True}
    body = {"name": f"ws-{name}", "driver": "ssh", "status": "active", "config": cfg,
            "description": f"{box} container, private workspace for {name}"}
    e = api("PATCH", f"/environments/{envs[body['name']]['id']}", body) if body["name"] in envs \
        else api("POST", f"/companies/{COMPANY}/environments", body)
    probe = api("POST", f"/environments/{e['id']}/probe", {})
    ok = probe.get("ok", probe.get("status"))
    a = api("PATCH", f"/agents/{ids[name]}", {"defaultEnvironmentId": e["id"]})
    out[name] = e["id"]; print(f"{name:12s} env {e['id']} probe={ok} agent-env={a.get('defaultEnvironmentId')==e['id']}")
json.dump(out, open("/work/.paperclip/env_ids.json", "w"), indent=1)
