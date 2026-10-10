#!/usr/bin/env python3
"""Pause the whole automath org in Paperclip: pause every agent (Paperclip cancels their queued/running runs)
and set every routine to paused. Resume with resume_all.py. Usage: pause_all.py [reason]"""
import sys, json
sys.path.insert(0, "/work/tools/paperclip"); import pc
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
for r in pc.call("GET", f"/companies/{C}/routines"):
    if r.get("status") != "paused":
        pc.call("PATCH", f"/routines/{r['id']}", {"status": "paused"}); print("routine paused:", r["title"])
for a in pc.call("GET", f"/companies/{C}/agents"):
    if a.get("status") != "paused":
        pc.call("POST", f"/agents/{a['id']}/pause", {}); print("agent paused:", a["name"])
runs = pc.call("GET", f"/companies/{C}/heartbeat-runs"); runs = runs if isinstance(runs, list) else runs.get("runs", runs)
print("still running/queued:", sum(1 for r in runs if r["status"] in ("running", "queued")))
