#!/usr/bin/env python3
"""Undo pause_all.py: resume paused agents and set every routine back to active.
Usage: resume_all.py [api|old|all]   (default api: since 2026-10-11 the project runs on the Claude API org, agents named
*-api; "old" = the subscription/Codex org, "all" = everything)."""
import sys
sys.path.insert(0, "/work/tools/paperclip"); import pc
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
which = sys.argv[1] if len(sys.argv) > 1 else "api"
def wanted(name):
    is_api = name.endswith("-api") or "-api-" in name
    return which == "all" or (which == "api" and is_api) or (which == "old" and not is_api and not name.startswith(("muse-", "api-probe")))
for a in pc.call("GET", f"/companies/{C}/agents"):
    if a.get("status") == "paused" and wanted(a["name"]):
        pc.call("POST", f"/agents/{a['id']}/resume", {}); print("agent resumed:", a["name"])
for r in pc.call("GET", f"/companies/{C}/routines"):
    if r.get("status") == "paused":
        pc.call("PATCH", f"/routines/{r['id']}", {"status": "active"}); print("routine active:", r["title"])
