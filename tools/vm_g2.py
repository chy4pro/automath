#!/usr/bin/env python3
"""G2 duplicate check against the VibeMathed dataset (AI-solved problems record).

Usage:
  python3 tools/vm_g2.py 708 709 "sparse halves" "Ramsey"
  python3 tools/vm_g2.py --refresh 708

Numbers are matched against Erdős problem numbers (problemNumber field or a number in the
name); other arguments are case-insensitive keywords searched in name/statement/resultNote.
The dataset is cached at engine/cache/vm_dataset.json (refetched with --refresh or if older
than 24 h). Data license: see the 'license' field printed in the header; do not redistribute.
"""
import json, os, re, sys, time, urllib.request

URL = "https://vibemathed.com/api/dataset"
CACHE = os.path.join(os.path.dirname(__file__), "..", "engine", "cache", "vm_dataset.json")


def load(refresh=False):
    fresh = os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 86400
    if refresh or not fresh:
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 automath-g2"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(CACHE, "wb") as f:
            f.write(data)
    with open(CACHE, encoding="utf-8") as f:
        return json.load(f)


def s(x):
    return "" if x is None else str(x)


def is_erdos(it):
    blob = s(it.get("name")) + " " + s(it.get("sourceName")) + " " + s(it.get("shortName"))
    return re.search(r"erd", blob, re.I) is not None


def erdos_number(it):
    pn = it.get("problemNumber")
    if isinstance(pn, int):
        return pn
    m = re.search(r"#?(\d+)", s(pn) or s(it.get("name")))
    return int(m.group(1)) if m else None


def show(it):
    print("  - %s | %s | %s | model=%s | %s | sig=%s | %s" % (
        s(it.get("name"))[:80], s(it.get("resolution")), s(it.get("aiContribution")),
        s(it.get("model"))[:30], s(it.get("solveDate")), s(it.get("significance")),
        s(it.get("sourceUrl") or it.get("citationsUrl"))[:80]))


def main():
    args = [a for a in sys.argv[1:] if a != "--refresh"]
    d = load(refresh="--refresh" in sys.argv)
    items = d["problems"]
    print("VibeMathed dataset: %d problems, generated %s, license %s" % (
        len(items), s(d.get("generated")), s(d.get("license"))))
    for a in args:
        if a.isdigit():
            n = int(a)
            hits = [it for it in items if is_erdos(it) and erdos_number(it) == n]
            print("Erdős #%d: %d hit(s)" % (n, len(hits)))
        else:
            rx = re.compile(re.escape(a), re.I)
            hits = [it for it in items if rx.search(
                s(it.get("name")) + " " + s(it.get("statement")) + " " + s(it.get("resultNote")))]
            print("keyword %r: %d hit(s)" % (a, len(hits)))
        for it in hits[:10]:
            show(it)


if __name__ == "__main__":
    main()
