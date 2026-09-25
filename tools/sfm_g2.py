#!/usr/bin/env python3
"""G2 check against starfleetmath.com (self-hosted AI claims with Lean bundles).

Usage: python3 tools/sfm_g2.py 709 708 1212
Fetches the dashboard page (one large HTML) and prints the Result line and bundle
links for each Erdős problem number given. Claims there are first-party, referee'd
by the project's own Fable harness; always re-verify the Lean bundle locally.
"""
import html, re, sys, urllib.request

URL = "https://www.starfleetmath.com/"


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 automath-g2"})
    with urllib.request.urlopen(req, timeout=60) as r:
        page = r.read().decode("utf-8", "replace")
    for arg in sys.argv[1:]:
        n = int(arg)
        i = page.find("Erdős Problem #%d" % n)
        if i < 0:
            print("Erdős #%d: not on starfleetmath.com" % n)
            continue
        seg = page[i:i + 40000]
        txt = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", seg)))
        m = re.search(r"Result (.*?) › Report", txt)
        links = sorted(set(re.findall(r'href="([^"]*erdos-%d[^"]*)"' % n, seg)))
        if not m:
            print("Erdős #%d: in the site's tracked catalog only (no claim / no Result line)" % n)
            continue
        print("Erdős #%d: CLAIM LISTED. Result: %s" % (n, m.group(1)[:300]))
        for l in links:
            print("   ", l)


if __name__ == "__main__":
    main()
