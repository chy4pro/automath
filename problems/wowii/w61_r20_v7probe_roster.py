#!/usr/bin/env python3
"""owner-w61 round 20 -- RULING L SELF-SATISFIED-INVARIANT SWEEP over the round-17
roster recomputation (`w61_r17_roster_recompute.py`).

WHY: that recomputation is now the evidentiary basis of a DISCHARGED obligation --
draft SS7.32 discharged roster completeness on it, cert_w61_r17.md certified the
discharge, and the r20 brief PRINTS its diff artifact inline as the reason a judge
should not GAP on completeness.  An assertion carrying that much weight should be
shown LIVE by execution, not assumed live by reading its source.

METHOD (RULING L, and RULING S's amendment): inject a fault at each guarded site and
run the whole thing.  A guard that TRIPS is live.  A guard that does NOT trip is
recorded, not dropped -- it is either a tautology or a fact about the object, and
either way we want to know which.  Nothing is graded by whether the answer is
comfortable.

HARD LIMIT: 300 s wall clock for the whole sweep (the clean run is ~2.4 s).
"""
import pathlib, re, subprocess, sys, tempfile, time, os

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
SRC  = ROOT / "problems/wowii/w61_r17_roster_recompute.py"
OUTF = ROOT / "problems/wowii/w61_r20_v7probe_roster.out"
BUDGET = 300.0
T0 = time.time()

src = SRC.read_text()
lines = []
def rep(s):
    print(s); lines.append(s)

# Each probe: (tag, description, old, new, what a LIVE guard should do)
PROBES = [
 ("F1", "steps_list: drop the negative-value guard so implementation #2 diverges from #1",
  "        if any(x < 0 for x in blk):\n            return None",
  "        if False:\n            return None",
  "the two-implementation cross-check should DIE with IMPLEMENTATION DISAGREEMENT"),
 ("F1b", "steps_list: perturb the DELETION COUNTER so implementation #2 genuinely\n"
         "      diverges from #1 (F1 turned out to perturb UNREACHABLE code -- see the note)",
  "        cur = sorted([x for x in blk + rest[d:] if x > 0], reverse=True)\n        n += 1",
  "        cur = sorted([x for x in blk + rest[d:] if x > 0], reverse=True)\n        n += 2",
  "the two-implementation cross-check should DIE with IMPLEMENTATION DISAGREEMENT"),
 ("F2", "p_euler: off-by-one, so the partition generator no longer matches p(n)",
  "def p_euler(n, _memo={0: 1}):",
  "def p_euler(n, _memo={0: 2}):",
  "the partition-count guard should DIE"),
 ("F3a", "fan6_kills: always FALSE -- nothing is killed",
  "    return w > second and second <= w - 2",
  "    return False",
  "FAN-6' miss counts should go POSITIVE and FAILURE_COUNT with them"),
 ("F3b", "fan6_kills: always TRUE -- everything is killed.  THIS IS THE SELF-SATISFIED\n"
         "      DIRECTION: a kill test that never rejects cannot report a miss",
  "    return w > second and second <= w - 2",
  "    return True",
  "if FAILURE_COUNT stays 0, 'FAN-6' misses = 0' carries NO information about the\n"
  "      kill test being right -- that is exactly the invariant the bulletin names"),
 ("F4", "tail_control: corrupt the Lemma TAIL formula by +1",
  "                if direct != (L - lam[0]) + base:",
  "                if direct != (L - lam[0]) + base + 1:",
  "TAIL-formula mismatches should go POSITIVE and FAILURE_COUNT with them"),
 ("F5", "the E>=1 closed form: perturb it so it disagrees with the enumeration loop",
  "        if r[\"S_closed\"] != r[\"e1_tested\"]:",
  "        if r[\"S_closed\"] + 1 != r[\"e1_tested\"]:",
  "the closed-form-vs-loop guard should raise FAILURE_COUNT"),
]

def run(text, tag):
    d = tempfile.mkdtemp()
    outp = os.path.join(d, "probe.out")
    t = text.replace('OUT = "problems/wowii/w61_r17_roster_recompute.out"',
                     'OUT = %r' % outp)
    assert outp in t, "OUT redirect failed"
    f = os.path.join(d, "probe_%s.py" % tag)
    pathlib.Path(f).write_text(t)
    try:
        p = subprocess.run([sys.executable, f], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return ("TIMEOUT", "", "")
    body = pathlib.Path(outp).read_text() if os.path.exists(outp) else ""
    return (p.returncode, (p.stdout + p.stderr).strip()[:300], body)

def failure_count(body):
    m = re.search(r"FAILURE_COUNT = (\d+)", body)
    return int(m.group(1)) if m else None

def misses_positive(body):
    return sum(1 for m in re.finditer(r"misses over ALL survivors\] : (\d+)", body)
               if int(m.group(1)) > 0)

rep("=== owner-w61 ROUND 20 -- RULING L SELF-SATISFIED-INVARIANT SWEEP ===")
rep("target: problems/wowii/w61_r17_roster_recompute.py")
rep(time.strftime("%a %b %d %H:%M:%S %Z %Y"))
rep("")

rc, msg, body = run(src, "CLEAN")
base_fc = failure_count(body)
rep("BASELINE (unmodified): rc=%s  FAILURE_COUNT=%s  DIFF-relevant counts intact=%s"
    % (rc, base_fc, "E>=1 shapes, nu <= 6      : 1745   survivors 72" in body))
assert rc == 0 and base_fc == 0, "baseline is not clean -- sweep aborted"
rep("")

live = 0; dead = 0
for tag, desc, old, new, expect in PROBES:
    if time.time() - T0 > BUDGET:
        rep("BUDGET EXHAUSTED -- remaining probes not run"); break
    n = src.count(old)
    if n != 1:
        rep("[%s] ANCHOR MISS (%d occurrences) -- probe not run, recorded as NOT RUN" % (tag, n))
        continue
    rc, msg, body = run(src.replace(old, new), tag)
    fc = failure_count(body)
    mp = misses_positive(body)
    tripped = (rc != 0) or (fc not in (0, None)) or mp > 0
    rep("[%s] %s" % (tag, desc))
    rep("     expected of a LIVE guard: %s" % expect)
    rep("     rc=%s  FAILURE_COUNT=%s  nu-blocks with positive FAN-6' misses=%d" % (rc, fc, mp))
    if msg and rc != 0:
        rep("     died with: %s" % msg.splitlines()[-1][:160])
    rep("     VERDICT: %s" % ("LIVE -- the guard trips" if tripped
                              else "DOES NOT TRIP -- recorded, not dropped"))
    rep("")
    live += 1 if tripped else 0
    dead += 0 if tripped else 1

rep("SWEEP RESULT: %d/%d injected faults trip a guard; %d do not." % (live, live + dead, dead))
rep("elapsed %.1fs (budget %.0fs)" % (time.time() - T0, BUDGET))
OUTF.write_text("\n".join(lines) + "\n")
print("wrote %s" % OUTF)
