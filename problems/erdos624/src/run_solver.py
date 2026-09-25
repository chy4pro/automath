#!/usr/bin/env python3
"""Run a command under resource caps and append its CPU time to cpu_ledger.csv.

usage: run_solver.py --tag TAG [--cpu-sec S] [--mem-mb M] [--fsize-kb K] -- cmd args...
Caps: RLIMIT_AS = M MB (default 1953, i.e. `ulimit -v 2000000`), RLIMIT_CPU = S seconds
(default 1800), RLIMIT_FSIZE = K KB (default 3000000, i.e. `ulimit -f 3000000`, ~3 GB). The
fsize cap is what was missing before the checkpoint-2 crash (36 GB of unbounded DRAT output);
every solver invocation MUST go through this script or an equivalent explicit ulimit -f.
stdout of the child goes to runs/TAG.out ; the exit code is printed.
"""
import os, sys, time, resource, argparse, csv

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("--tag", required=True)
ap.add_argument("--cpu-sec", type=int, default=1800)
ap.add_argument("--mem-mb", type=int, default=1953)
ap.add_argument("--fsize-kb", type=int, default=3000000)
ap.add_argument("--stdout", default=None)
ap.add_argument("cmd", nargs=argparse.REMAINDER)
a = ap.parse_args()
cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
outp = a.stdout or os.path.join(HERE, "runs", a.tag + ".out")


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (a.mem_mb << 20, a.mem_mb << 20))
    resource.setrlimit(resource.RLIMIT_CPU, (a.cpu_sec, a.cpu_sec + 5))
    resource.setrlimit(resource.RLIMIT_FSIZE, (a.fsize_kb << 10, a.fsize_kb << 10))


t0 = time.time()
pid = os.fork()
if pid == 0:
    limits()
    fd = os.open(outp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    os.dup2(fd, 1)
    os.execvp(cmd[0], cmd)
_, status, ru = os.wait4(pid, 0)
wall = time.time() - t0
cpu = ru.ru_utime + ru.ru_stime
code = os.waitstatus_to_exitcode(status)
with open(os.path.join(HERE, "cpu_ledger.csv"), "a", newline="") as fh:
    csv.writer(fh).writerow([time.strftime("%Y-%m-%dT%H:%M:%S"), a.tag, "%.2f" % cpu, "%.2f" % wall,
                             code, ru.ru_maxrss // 1024, " ".join(cmd)])
print("%s exit=%s cpu=%.1fs wall=%.1fs maxrss=%dMB" % (a.tag, code, cpu, wall, ru.ru_maxrss // 1024))
