#!/usr/bin/env python3
"""Undo pause_all.py: resume paused agents and set every routine back to active.
Usage: resume_all.py [api|old|all]   (default api: since 2026-10-11 the Claude agents run on the Claude API (*-api) and
Codex work stays on the Codex agents, so "api" = the *-api agents plus the Codex seats; "old" = the subscription Claude
agents coordinator, referee-1/2, verifier; "all" = everything). muse-claude / muse-agy / api-probe only with "all"."""
import sys
sys.path.insert(0, "/work/tools/paperclip"); import pc
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
which = sys.argv[1] if len(sys.argv) > 1 else "api"
CODEX = {"scout", "attacker-1", "attacker-2", "muse-codex", "muse-claude"}  # muse-claude: API-billed since 2026-10-12   # formalizer moved to formalizer-api (2026-10-11)
OLD_CLAUDE = {"coordinator", "referee-1", "referee-2", "verifier"}
def wanted(name):
    is_api = name.endswith("-api") or "-api-" in name
    return which == "all" or (which == "api" and (is_api or name in CODEX)) or (which == "old" and name in OLD_CLAUDE)
for a in pc.call("GET", f"/companies/{C}/agents"):
    if a.get("status") == "paused" and wanted(a["name"]):
        pc.call("POST", f"/agents/{a['id']}/resume", {}); print("agent resumed:", a["name"])
for r in pc.call("GET", f"/companies/{C}/routines"):
    if r.get("status") == "paused":
        pc.call("PATCH", f"/routines/{r['id']}", {"status": "active"}); print("routine active:", r["title"])
