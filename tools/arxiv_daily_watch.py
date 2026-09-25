#!/usr/bin/env python3
"""
Zero-quota daily arXiv watch for conjecture resolutions and AI-assisted mathematics.

WHY THIS EXISTS.  On 2026-08-19 the cscK Yau-Tian-Donaldson conjecture was disproved
(arXiv:2608.19301, AI-obtained, with a documented AI-usage appendix).  This project's
intel line did not surface it for four days.  The cause was structural, not cadence:
EVERY channel we had was PULL-BY-TARGET ("is conjecture X still open?") and pub-watch
looked only at our OWN artefacts.  Nothing asked "what closed today?".

This tool is the time-indexed, field-facing channel we did not have.

SELF-TEST.  Run with --selftest.  It replays the 2026-08-19 window and REQUIRES the
real historical miss to come back.  Per RULING CZ a positive control must inject the
hardest real instance, not a synthetic one -- so the control here IS the paper we missed.

Zero quota: arXiv export API only.  Polite: one request per arm, sleeps between.

DATE-WINDOW SEMANTICS (bug fixed 2026-08-24).  The export API only serves a submission
day's postings after they are ANNOUNCED (Sun-Thu 20:00 ET), so querying "yesterday"
returns population 0 for fresh days -- the old code then silently logged an empty day
and the watch was blind while looking alive.  Now: with no --date the tool walks the
last MAX_BACKLOG_DAYS submission days, skips days already in the ledger, defers days
younger than ANNOUNCE_LAG_DAYS that still show population 0 (announcement lag, retried
on the next run, never written to the ledger), and raises ALARM (exit 2) for any day
past the lag whose population is still 0 -- population 0 is never a silent no-op.

Usage:
    python3 tools/arxiv_daily_watch.py                # catch up all unlogged announced days
    python3 tools/arxiv_daily_watch.py --date 20260819
    python3 tools/arxiv_daily_watch.py --selftest
"""
import argparse, datetime, re, sys, time, urllib.request, os

BASE = "https://export.arxiv.org/api/query?"     # MUST be https: http returns 301 and curl-style
                                                 # clients see an EMPTY body (SCOUTING trap 1)
MATH_CATS = ["AG","DG","CV","NT","CO","GR","AC","AT","CT","GT","LO","RA","RT","OA",
             "FA","PR","ST","NA","OC","DS","GM","HO","IT","KT","MG","MP","QA","SG","SP"]
CATS = "%28" + "+OR+".join("cat:math." + c for c in MATH_CATS) + "%29"

ARM_RESOLUTION = ('%28ti:%22disproof%22+OR+ti:%22disprove%22+OR+ti:%22counterexample%22'
                  '+OR+abs:%22disproves%22+OR+abs:%22counterexample+to%22'
                  '+OR+ti:%22resolution+of%22+OR+ti:%22proof+of+the%22%29')
ARM_AI = ('%28abs:%22generative+AI%22+OR+abs:%22AI-assisted%22+OR+abs:%22large+language+model%22'
          '+OR+abs:%22language+models%22%29')
# Positive-resolution arm (added 2026-08-24, S^6 retrospective R6): the resolution arm
# carries only negative-resolution vocabulary plus "proof of the"/"resolution of", so a
# CONSTRUCTION that settles a famous problem (e.g. "A complex structure on the six-sphere")
# matched nothing.  Terms measured on the 20260820 window: ~14 extra flags/day total.
ARM_POSITIVE = ('%28abs:%22in+the+affirmative%22+OR+abs:%22long-standing%22'
                '+OR+abs:%22longstanding%22+OR+abs:%22answering+a+question%22'
                '+OR+abs:%22answers+a+question%22+OR+abs:%22open+problem%22'
                '+OR+abs:%22open+question%22+OR+abs:%22settles%22+OR+abs:%22settling%22%29')

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                      "notes", "case_intel", "arxiv_watch_ledger.md")

ANNOUNCE_LAG_DAYS = 3   # a submission day may be invisible to the API for up to ~3 days
MAX_BACKLOG_DAYS = 7    # how far back the no---date run looks for unlogged days


def fetch(search, max_results=200, timeout=90):
    url = ("%ssearch_query=%s&start=0&max_results=%d&sortBy=submittedDate&sortOrder=descending"
           % (BASE, search, max_results))
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def total(xml):
    m = re.search(r"<opensearch:totalResults>(\d+)", xml)
    return int(m.group(1)) if m else -1


def parse(xml):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        def g(tag):
            m = re.search(r"<%s>(.*?)</%s>" % (tag, tag), e, re.S)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
        out.append({"id": g("id").split("/abs/")[-1],
                    "title": g("title"),
                    "published": g("published"),
                    "authors": re.findall(r"<name>(.*?)</name>", e),
                    "cats": [c for c in re.findall(r'term="([^"]+)"', e)],
                    "abstract": g("summary")})
    return out


def window(day):
    nxt = (datetime.datetime.strptime(day, "%Y%m%d") + datetime.timedelta(days=1)).strftime("%Y%m%d")
    return "submittedDate:[%s0000+TO+%s0000]" % (day, nxt)


def run_day(day, verbose=True):
    win = window(day)
    # denominator first: population is printed before any verdict
    base = fetch(CATS + "+AND+" + win, 1)
    n_math = total(base)
    time.sleep(3)
    results = {}
    for name, arm in (("resolution", ARM_RESOLUTION), ("positive", ARM_POSITIVE),
                      ("ai-disclosure", ARM_AI)):
        xml = fetch(CATS + "+AND+" + win + "+AND+" + arm, 200)
        results[name] = parse(xml)
        if verbose:
            n = total(xml)
            print("  %-14s %3d of %3d math postings (%.1f%%)"
                  % (name, n, n_math, 100.0 * n / max(n_math, 1)))
        time.sleep(3)
    return n_math, results


def selftest():
    """The control IS the real miss.  A synthetic probe would certify nothing."""
    print("SELF-TEST: replaying 2026-08-19, the day the project missed arXiv:2608.19301")
    n_math, res = run_day("20260819")
    ids = {e["id"].split("v")[0] for arm in res.values() for e in arm}
    ok_hit = "2608.19301" in ids
    # binding control: the filter must actually reduce the population
    ok_bind = 0 < len(res["resolution"]) < n_math
    print("  population that day: %d math postings" % n_math)
    print("  target 2608.19301 recovered : %s" % ("YES" if ok_hit else "*** NO -- WATCH IS DEAD ***"))
    print("  filter binds (0 < hits < N)  : %s" % ("YES" if ok_bind else "*** NO -- FILTER NOT BINDING ***"))
    # negative control: a nonsense term must return nothing in the same window
    time.sleep(3)
    nonsense = fetch(CATS + "+AND+" + window("20260819") + "+AND+ti:%22zzzqqqxxnotaword%22", 1)
    ok_neg = total(nonsense) == 0
    print("  negative control (nonsense)  : %s" % ("returns 0, good" if ok_neg else "*** FIRES ON NOTHING ***"))
    return 0 if (ok_hit and ok_bind and ok_neg) else 2


def logged_days():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return set(re.findall(r"^## (\d{8}) --", f.read(), re.M))
    except OSError:
        return set()


def process_day(day):
    """Run one day; print + ledger-append only when the population is nonzero.
    Returns n_math (population 0 / parse failure -1 are the caller's ALARM cases)."""
    print("arXiv daily watch -- window %s (UTC)" % day)
    n_math, res = run_day(day)
    if n_math <= 0:
        return n_math
    seen, lines = set(), []
    for arm in res:
        for e in res[arm]:
            k = e["id"].split("v")[0]
            if k in seen:
                continue
            seen.add(k)
            lines.append("| %s | %s | %s | %s | %s |"
                         % (k, e["title"].replace("|", "/")[:95],
                            ", ".join(e["authors"][:3])[:48],
                            ",".join(c for c in e["cats"][:3]), arm))
    print("\n%s: %d distinct papers flagged from %d math postings\n" % (day, len(lines), n_math))
    if lines:
        print("| id | title | authors | cats | arm |")
        print("|---|---|---|---|---|")
        print("\n".join(lines))
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write("\n## %s -- %d flagged / %d math postings\n\n" % (day, len(lines), n_math))
        if lines:
            f.write("| id | title | authors | cats | arm |\n|---|---|---|---|---|\n")
            f.write("\n".join(lines) + "\n")
        else:
            f.write("_no flagged postings_\n")
    return n_math


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYYMMDD; default = catch up all unlogged announced days")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if a.date:
        if process_day(a.date) <= 0:
            print("ALARM: %s returned population<=0 -- window empty or API unparsable" % a.date)
            sys.exit(2)
        return
    now = datetime.datetime.utcnow()
    done, alarm, handled = logged_days(), False, 0
    for back in range(MAX_BACKLOG_DAYS, 0, -1):
        day = (now - datetime.timedelta(days=back)).strftime("%Y%m%d")
        if day in done:
            continue
        n = process_day(day)
        handled += 1
        if n <= 0:
            if back >= ANNOUNCE_LAG_DAYS:
                print("ALARM: population<=0 for %s (%d days back, past announcement lag) "
                      "-- watch may be blind" % (day, back))
                alarm = True
            else:
                print("%s: population 0, within announcement lag -- deferred to next run" % day)
        time.sleep(3)
    if handled == 0:
        print("ledger already covers the last %d days -- nothing to do" % MAX_BACKLOG_DAYS)
    if alarm:
        sys.exit(2)


if __name__ == "__main__":
    main()
