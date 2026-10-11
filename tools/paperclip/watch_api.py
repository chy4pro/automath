#!/usr/bin/env python3
"""Watch the Claude API org: every INTERVAL seconds append one status line to /work/.paperclip/logs/api-watch.log
(API spend vs the budget, API runs, rate-limit signals in finished API runs, failures) and print ALERT lines to stdout
only when something needs attention: rate-limit errors or retries (HTTP 429 / api_retry / overloaded), API spend
crossing another $40, Paperclip unreachable, or 3+ failed runs in one interval. Disk rule (owner, 2026-10-11): below 20 GB
free on /work an ALERT asks for a cleanup agent (once per crossing); below 5 GB free it pauses the whole org with
pause_all.py and alerts. Usage: watch_api.py [interval_s] [hours]"""
import json, os, shutil, subprocess, sys, time, urllib.request, datetime
sys.path.insert(0, "/work/tools/paperclip"); import pc
C = "d0817321-3b6a-412d-8aaa-1e2b42e35cae"
API = ("coordinator-api", "referee-api-1", "referee-api-2", "verifier-api")
INTERVAL = int(sys.argv[1]) if len(sys.argv) > 1 else 300
HOURS = float(sys.argv[2]) if len(sys.argv) > 2 else 12
LOG = "/work/.paperclip/logs/api-watch.log"
# exact markers emitted by Claude Code / the API (plain words like "429" also appear in task text)
SIGNALS = ('"subtype":"api_retry"', "rate_limit_error", "API Error: 429", '"status":429', "overloaded_error", "API Error: 529")
seen, step, disk_low, disk_stopped = set(), None, False, False
def get(path):
    try: return pc.call("GET", path)
    except SystemExit: return None
end = time.time() + HOURS * 3600
while time.time() < end:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M")
    free_gb = shutil.disk_usage("/work").free / 1e9
    if free_gb < 5 and not disk_stopped:
        out = subprocess.run([sys.executable, "/work/tools/paperclip/pause_all.py"], capture_output=True, text=True)
        disk_stopped = True
        print(f"ALERT {now} /work has {free_gb:.1f} GB free (< 5 GB): paused the org (pause_all.py exit {out.returncode})", flush=True)
    if free_gb < 20 and not disk_low:
        disk_low = True
        print(f"ALERT {now} /work has {free_gb:.1f} GB free (< 20 GB): a cleanup agent should be dispatched", flush=True)
    if free_gb >= 22: disk_low = False
    try:
        urllib.request.urlopen("http://wb-proj-656d7af54e8b:3100/api/health", timeout=10)
    except Exception:
        print(f"ALERT {now} Paperclip unreachable", flush=True); time.sleep(INTERVAL); continue
    agents = {a["name"]: a for a in (get(f"/companies/{C}/agents") or [])}
    pol = ((get(f"/companies/{C}/budgets/overview") or {}).get("policies") or [{}])[0]
    spent = (pol.get("observedAmount") or 0) / 100
    new_runs, hits, failed, running = 0, [], 0, 0
    for n in API:
        if n not in agents: continue
        r = get(f"/companies/{C}/heartbeat-runs?agentId={agents[n]['id']}&limit=20") or []
        r = r if isinstance(r, list) else r.get("runs", [])
        running += sum(1 for x in r if x.get("status") == "running")
        for x in r:
            if x["id"] in seen or x.get("status") in ("running", "queued", "scheduled_retry"): continue
            seen.add(x["id"]); new_runs += 1
            if x.get("status") == "failed": failed += 1
            text = (x.get("error") or "")
            lg = get(f"/heartbeat-runs/{x['id']}/log")
            if isinstance(lg, dict): text += lg.get("content") or ""
            text = text.replace('\\"', '"')   # run logs store chunks as escaped JSON
            found = sorted({s for s in SIGNALS if s in text})
            if found: hits.append(f"{n}:{x['id'][:8]}:{','.join(found)}")
    line = f"{now} disk_free={free_gb:.1f}GB spent=${spent:.2f}/{(pol.get('amount') or 0)/100:.0f} running_api={running} finished_api={new_runs} failed={failed} ratelimit={hits or '-'}"
    open(LOG, "a").write(line + "\n")
    if step is None: step = int(spent // 40)
    if hits: print(f"ALERT {now} rate-limit signals: {hits}", flush=True)
    if failed >= 3: print(f"ALERT {now} {failed} API runs failed in the last interval", flush=True)
    if int(spent // 40) > step:
        step = int(spent // 40); print(f"ALERT {now} API spend passed ${step*40} (now ${spent:.2f} of $200)", flush=True)
    time.sleep(INTERVAL)
