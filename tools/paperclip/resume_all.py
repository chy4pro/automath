#!/usr/bin/env python3
"""Undo pause_all.py: resume every agent and set every routine back to active."""
import sys
sys.path.insert(0, "/work/tools/paperclip"); import pc
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
for a in pc.call("GET", f"/companies/{C}/agents"):
    if a.get("status") == "paused":
        pc.call("POST", f"/agents/{a['id']}/resume", {}); print("agent resumed:", a["name"])
for r in pc.call("GET", f"/companies/{C}/routines"):
    if r.get("status") == "paused":
        pc.call("PATCH", f"/routines/{r['id']}", {"status": "active"}); print("routine active:", r["title"])
