#!/usr/bin/env python3
"""ROUND 6-AT: exact integer content of EVERY characteristic-zero unit terminal (registry R6.110), locally.
For each <terminal>.ms in the input directory run round6_zstd_one.py (Singular strong Groebner basis over Z,
self-capped: SIGKILL at --rss-mb or --wall) STRICTLY ONE AT A TIME and record "<name>\t<status>\t<d>\t<seconds>"
in the results table (resumable: names already in the table are skipped; pass --retry-fail to redo FAIL rows).
Machine guard (registry R6.110 incident): before each terminal the driver reads `sysctl vm.swapusage` and waits
while swap in use exceeds --swap-guard-mb (default 6000).  Never run two drivers.
(d_S) = I_S cap Z, so the primes dividing d_S are EXACTLY the characteristics in which terminal S is not the unit
ideal; d_S = 1 means unit in every characteristic.
Usage: round6_zstd_batch.py <terminals_dir> <results.tsv> [--order order.txt] [--wall 30] [--rss-mb 2000]
       [--swap-guard-mb 6000] [--retry-fail]"""
import sys, os, re, subprocess, time
sys.stdout.reconfigure(line_buffering=True)
HERE = os.path.dirname(os.path.abspath(__file__))
argv = sys.argv[1:]; order = None; wall = 30; rss_mb = 2000; swap_guard = 6000; retry = False
if "--retry-fail" in argv: retry = True; argv.remove("--retry-fail")
for flag in ("--order", "--wall", "--rss-mb", "--swap-guard-mb"):
    if flag in argv:
        k = argv.index(flag); val = argv[k + 1]; argv = argv[:k] + argv[k + 2:]
        if flag == "--order": order = val
        elif flag == "--wall": wall = int(val)
        elif flag == "--rss-mb": rss_mb = int(val)
        else: swap_guard = int(val)
tdir, table = argv[0], argv[1]
scratch = os.path.join(os.path.dirname(table), "scratch"); os.makedirs(scratch, exist_ok=True)
done = {}
if os.path.exists(table):
    for line in open(table):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 2: done[f[0]] = f[1]
if order and os.path.exists(order): names = [l.strip() for l in open(order) if l.strip()]
else: names = sorted(f for f in os.listdir(tdir) if f.endswith(".ms"))
todo = [n for n in names if n[:-3] not in done or (retry and done[n[:-3]] == "FAIL")]
print("terminals %d, in table %d, todo %d, wall %ds, rss cap %d MB, swap guard %d MB" % (len(names), len(done), len(todo), wall, rss_mb, swap_guard))
def swap_used_mb():
    try:
        m = re.search(r"used = ([\d.]+)M", subprocess.run(["sysctl", "vm.swapusage"], capture_output=True, text=True).stdout)
        return float(m.group(1)) if m else 0.0
    except Exception:
        return 0.0
T0 = time.time(); counts = {"ZSTD": 0, "FAIL": 0}; nontrivial = 0
for i, n in enumerate(todo):
    name = n[:-3]
    waited = 0
    while swap_used_mb() > swap_guard and waited < 3600:
        if waited == 0: print("  swap guard: %.0f MB in use > %d MB, waiting" % (swap_used_mb(), swap_guard))
        time.sleep(30); waited += 30
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(HERE, "round6_zstd_one.py"), os.path.join(tdir, n), "--scratch", scratch,
                        "--wall", str(wall), "--rss-mb", str(rss_mb)], capture_output=True, text=True, timeout=wall + 120)
    out = r.stdout
    m = re.search(r"%s ZSTD d=(\d+) size=(\d+)" % re.escape(name), out)
    if m:
        status, d = "ZSTD", m.group(1); counts["ZSTD"] += 1
        if d != "1": nontrivial += 1
        if d not in ("1", "2", "3"): print("  UNUSUAL %s d=%s" % (name, d))
    else:
        status, d = "FAIL", "0"; counts["FAIL"] += 1
        reason = re.search(r"%s FAIL ([^\n]*)" % re.escape(name), out)
        print("  FAIL %s %s" % (name, reason.group(1)[:120] if reason else "(no output)"))
    with open(table, "a") as fh: fh.write("%s\t%s\t%s\t%.1f\n" % (name, status, d, time.time() - t0))
    try: os.remove(os.path.join(scratch, name + ".zstd.sing"))
    except OSError: pass
    if (i + 1) % 100 == 0 or i + 1 == len(todo):
        print("progress %d/%d  ZSTD %d  FAIL %d  nontrivial %d  [%.0fs]" % (i + 1, len(todo), counts["ZSTD"], counts["FAIL"], nontrivial, time.time() - T0))
print("DONE zstd batch: ZSTD %d FAIL %d nontrivial %d [%.0fs]" % (counts["ZSTD"], counts["FAIL"], nontrivial, time.time() - T0))
