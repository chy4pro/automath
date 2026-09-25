#!/usr/bin/env python3
"""
Zero-quota citation / metadata channel for the selection gate's impact axis.

WHY THIS EXISTS.  Gate batch 2 (2026-08-22) reported "Semantic Scholar returned 429 on all
twelve candidates; we have no working citation channel for DOI-less 2026 preprints" and
recommended acquiring an S2 API key.  Re-measured 2026-08-24:

  * S2 without a key is genuinely dead (429 on every call, not transient -- the anonymous
    pool is shared across all unauthenticated users worldwide), AND the key form does not
    accept a public email address.  So S2 is unavailable to us, full stop.
  * BUT the premise was wrong: arXiv has auto-assigned every submission a DOI of the form
    10.48550/arXiv.NNNN.NNNNN since 2022.  There are no DOI-less arXiv preprints.
    OpenAlex indexes them and serves cited_by_count with no key and no rate pain.
  * Crossref (polite pool) covers published works.

SECOND FINDING, recorded so the gate stops chasing it: for a preprint days old the true
citation count is 0.  That is a MEASUREMENT, not a channel failure.  The impact axis must
not read 0-because-new as 0-because-unimportant; for fresh preprints score impact from the
problem's standing, not from citations.

Polite-pool identity uses the project's public address (chy4pro@), never the owner's
private mail.

Usage:
    python3 tools/cite_lookup.py arXiv:2608.19301
    python3 tools/cite_lookup.py 10.1016/j.laa.2020.07.030
    python3 tools/cite_lookup.py --selftest
"""
import json, re, sys, urllib.parse, urllib.request

MAILTO = "[email]"          # project-public identity, not the owner's private mail
UA = "automath/1.0 (mailto:%s)" % MAILTO
TIMEOUT = 30


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def normalize(token):
    """arXiv:2608.19301 / 2608.19301 / a bare DOI -> a DOI string."""
    t = token.strip()
    m = re.match(r"^(?:arxiv:)?(\d{4}\.\d{4,5})(v\d+)?$", t, re.I)
    if m:
        return "10.48550/arXiv.%s" % m.group(1), "arxiv"
    t = re.sub(r"^https?://(dx\.)?doi\.org/", "", t, flags=re.I)
    return t, "doi"


def openalex(doi):
    url = "https://api.openalex.org/works/doi:%s" % urllib.parse.quote(doi, safe="")
    d = _get(url)
    loc = d.get("primary_location") or {}
    src = loc.get("source") or {}
    return {
        "channel": "openalex",
        "title": d.get("title"),
        "year": d.get("publication_year"),
        "citations": d.get("cited_by_count"),
        "venue": src.get("display_name"),
        "authors": [a["author"]["display_name"] for a in (d.get("authorships") or [])[:5]],
        "id": d.get("id"),
    }


def crossref(doi):
    url = "https://api.crossref.org/works/%s?mailto=%s" % (urllib.parse.quote(doi, safe=""), MAILTO)
    m = _get(url)["message"]
    return {
        "channel": "crossref",
        "title": (m.get("title") or [None])[0],
        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "citations": m.get("is-referenced-by-count"),
        "venue": m.get("container-title", [None])[0],
        # parens matter: without them .strip() binds to the TUPLE, not the formatted string,
        # and every Crossref call dies with "'tuple' object has no attribute 'strip'"
        # (found by line-k1695 2026-08-24 -- the selftest could not see it, see below)
        "authors": [("%s %s" % (a.get("given", ""), a.get("family", ""))).strip()
                    for a in (m.get("author") or [])[:5]],
        "id": m.get("DOI"),
    }


def lookup(token):
    doi, kind = normalize(token)
    out, errors = [], []
    for fn in (openalex, crossref):
        try:
            out.append(fn(doi))
        except Exception as e:                       # channel-level failure, reported not hidden
            errors.append("%s: %s" % (fn.__name__, e))
    return doi, kind, out, errors


def selftest():
    """Controls: a known-old published work MUST show citations > 0; a days-old preprint
    MUST resolve and legitimately show 0; a nonsense DOI MUST fail on both channels.

    PER-ARM control added 2026-08-24 after line-k1695 found the Crossref arm 100% dead
    while this selftest still printed PASS: all three original controls happen to resolve
    through OpenAlex, so nothing here could ever fail on Crossref's behalf.  A control that
    cannot fail for the channel it covers is not a control.  Now each arm must report
    separately, and a silent one-arm run is a DEGRADATION, not a pass."""
    ok = True

    doi, _, rows, errs = lookup("10.4153/CJM-1980-018-9")   # R.C. Thompson 1980, long-cited
    hit = [r for r in rows if r.get("citations")]
    print("positive control (1980 paper, must have citations>0): %s"
          % ("PASS %s" % [r["citations"] for r in hit] if hit else "*** FAIL ***"))
    ok &= bool(hit)

    arms = {r["channel"] for r in rows}
    for want in ("openalex", "crossref"):
        alive = want in arms
        print("  arm control [%s] must answer on a DOI it indexes: %s"
              % (want, "PASS" if alive else "*** DEGRADED -- %s ***"
                 % ("; ".join(errs) or "no rows, no error")))
        ok &= alive

    doi, _, rows, _ = lookup("arXiv:2608.19301")          # YTD disproof, days old
    res = [r for r in rows if r.get("title")]
    print("preprint control (must RESOLVE; 0 citations is the true value): %s"
          % ("PASS %r cites=%s" % (res[0]["title"][:40], res[0]["citations"]) if res
             else "*** FAIL -- no channel resolves arXiv DOIs ***"))
    ok &= bool(res)

    _, _, rows, errs = lookup("10.9999/nonexistent.zzzqqq")
    print("negative control (nonsense DOI, must resolve NOWHERE): %s"
          % ("PASS" if not rows else "*** FAIL -- returned %s ***" % rows))
    ok &= not rows

    return 0 if ok else 2


def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--selftest":
        sys.exit(selftest())
    doi, kind, rows, errors = lookup(sys.argv[1])
    print("query -> DOI %s (%s)" % (doi, kind))
    for r in rows:
        print("  [%s] %s (%s) cites=%s venue=%s"
              % (r["channel"], (r["title"] or "?")[:70], r["year"], r["citations"], r["venue"]))
    for e in errors:
        print("  MISS %s" % e)
    if not rows:
        print("  NOT FOUND on any channel -- absence of a record, not a citation count of 0")


if __name__ == "__main__":
    main()
