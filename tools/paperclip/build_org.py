#!/usr/bin/env python3
"""Create (or update) the automath org in Paperclip. Idempotent by agent name.
Env: PAPERCLIP_BOARD_TOKEN_FILE (default /work/.paperclip/board.token)."""
import json, os, sys, urllib.request
API = "http://wb-proj-656d7af54e8b:3100/api"
COMPANY = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
CLAUDE_ENV = "b49d66b2-6453-4ac8-b186-c6404e9c2fe7"   # agent@192.168.166.3:2222
CODEX_ENV = "7d206964-8783-45d0-b6e4-f87a073d1e8e"    # agent@192.168.166.4:2222
TOK = open(os.environ.get("PAPERCLIP_BOARD_TOKEN_FILE", "/work/.paperclip/board.token")).read().strip()
AG = "/work/tools/paperclip/agents"

def api(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + TOK, "Content-Type": "application/json", "Origin": "https://automath.mozone.io"})
    try:
        with urllib.request.urlopen(req) as r: return json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        print(method, path, e.code, e.read().decode()[:400]); raise

def bundle(role):
    files = {"AGENTS.md": open(f"{AG}/{role}.md").read() + "\n" + open(f"{AG}/_common.md").read()}
    return {"entryFile": "AGENTS.md", "files": files}

def adapter(kind, name, model, env_extra=None):
    cwd = f"/work/.paperclip/host-ws/{name}"
    cfg = {"cwd": cwd, "timeoutSec": 3600, "maxTurnsPerRun": 200, "model": model, "engine": "cli",
           "env": {"PAPERCLIP_AGENT_NAME": name, **(env_extra or {})}}
    if kind == "codex_local": cfg["modelReasoningEffort"] = "xhigh"
    return cfg

ROLES = [
 # name, title, icon, role file, adapter, env, model, budget USD, extra env
 ("coordinator", "Coordinator (Fable) — single decision maker", "crown", "coordinator", "claude_local", CLAUDE_ENV, "claude-fable-5-1", 0, {}),
 ("scout", "Scout — literature status, G2, selection dossiers", "telescope", "scout", "codex_local", CODEX_ENV, "gpt-6-astra", 0, {}),
 ("attacker-1", "Attacker (Astra, clean room)", "swords", "attacker", "codex_local", CODEX_ENV, "gpt-6-astra", 0, {"AUTOMATH_CLEAN_ROOM": "1"}),
 ("attacker-2", "Attacker (Astra, clean room)", "swords", "attacker", "codex_local", CODEX_ENV, "gpt-6-astra", 0, {"AUTOMATH_CLEAN_ROOM": "1"}),
 ("referee-1", "Referee (Claude, isolated, adversarial)", "shield", "referee", "claude_local", CLAUDE_ENV, "claude-fable-5-1", 0, {}),
 ("referee-2", "Referee (Claude, isolated, adversarial)", "shield", "referee", "claude_local", CLAUDE_ENV, "claude-opus-5-5", 0, {}),
 ("formalizer", "Formalizer (Astra, Lean 4 via GitHub Actions)", "atom", "formalizer", "codex_local", CODEX_ENV, "gpt-6-astra", 0, {}),
 ("verifier", "Verifier (Claude, finite checks and numerics)", "microscope", "verifier", "claude_local", CLAUDE_ENV, "claude-sonnet-5-5", 0, {}),
]

existing = {a["name"]: a for a in api("GET", f"/companies/{COMPANY}/agents")}
ids = {}
for name, title, icon, rf, ad, env, model, budget, extra in ROLES:
    body = {"name": name, "title": title, "icon": icon, "role": "ceo" if name == "coordinator" else "researcher",
            "adapterType": ad, "adapterConfig": adapter(ad, name, model, extra), "defaultEnvironmentId": env,
            "instructionsBundle": bundle(rf), **({} if budget == 0 else {"budgetMonthlyCents": budget * 100}),
            "permissions": {"canCreateAgents": name == "coordinator", "canCreateSkills": False,
                            "trustPreset": "standard"},
            "capabilities": title}
    if name != "coordinator": body["reportsTo"] = ids["coordinator"]
    if name in existing:
        patch = {k: v for k, v in body.items() if k not in ("permissions", "instructionsBundle")}  # create-only on PATCH
        a = api("PATCH", f"/agents/{existing[name]['id']}", patch)
        cur = api("GET", f"/agents/{a['id']}/instructions-bundle/file?path=AGENTS.md")
        new = body["instructionsBundle"]["files"]["AGENTS.md"]
        if cur.get("content") != new:
            api("PUT", f"/agents/{a['id']}/instructions-bundle/file",
                {"path": "AGENTS.md", "content": new, "baseRevisionId": (cur.get("revision") or {}).get("id"), "baseHash": cur.get("contentHash")})
        print("updated", name, a["id"])
    else:
        a = api("POST", f"/companies/{COMPANY}/agents", body); print("created", name, a["id"])
    ids[name] = a["id"]
json.dump(ids, open("/work/.paperclip/agent_ids.json", "w"), indent=1)
print(json.dumps(ids, indent=1))
