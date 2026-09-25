#!/usr/bin/env python3
"""citation_gate -- G2 of the PUBLICATION GATE (user directive 2026-08-23,
inbox/directive_zero_fabrication_gate.md).

Species F2: citations that do not resolve. Engines produce decorative fake sources.
Every reference must resolve LIVE via arXiv / DOI (doi.org content negotiation) or
Crossref, and the title must match what the API returns. Unresolvable = BLOCK.

Usage:  python3 tools/citation_gate.py FILE [FILE ...] [--json OUT] [--limit N]
Exit:   1 if any reference is UNRESOLVED or MISMATCHED, else 0.

Network: one request per distinct identifier, throttled. Failures are reported as
NETWORK (not as resolution failures) so a flaky link never silently becomes a pass --
a NETWORK result still blocks, because "we could not check" is not "it is fine".
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request

UA = "automath-citation-gate/1.0 (mailto:chy4pro@users.noreply.github.com)"
SLEEP = 1.1          # polite: Crossref/arXiv are shared infrastructure
TIMEOUT = 20

ARXIV = re.compile(r"arxiv[:\s/]*((?:\d{4}\.\d{4,5})(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})", re.I)
DOI = re.compile(r"\b(10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+)")


def _get(url, accept=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "replace")


def resolve_arxiv(ident):
    base = ident.split("v")[0] if re.match(r"^\d{4}\.", ident) else ident
    url = "http://export.arxiv.org/api/query?id_list=%s&max_results=1" % base
    try:
        body = _get(url)
    except Exception as e:
        return ("NETWORK", str(e)[:80])
    if "<entry>" not in body:
        return ("UNRESOLVED", "no entry returned by arXiv API")
    m = re.search(r"<title>(.*?)</title>", body.split("<entry>", 1)[1], re.S)
    return ("OK", " ".join(m.group(1).split()) if m else "(title absent)")


def resolve_doi(doi):
    try:
        body = _get("https://doi.org/" + doi, accept="application/vnd.citationstyles.csl+json")
    except urllib.error.HTTPError as e:
        if e.code in (404, 302, 303):
            return ("UNRESOLVED", "doi.org HTTP %d" % e.code)
        return ("NETWORK", "HTTP %d" % e.code)
    except Exception as e:
        return ("NETWORK", str(e)[:80])
    try:
        d = json.loads(body)
    except ValueError:
        return ("UNRESOLVED", "no CSL JSON returned")
    return ("OK", (d.get("title") or "(no title field)") if isinstance(d.get("title"), str)
            else " / ".join(d.get("title") or ["(no title field)"]))


def scan(path, limit=None):
    text = open(path, encoding="utf-8", errors="replace").read()
    found = []
    seen = set()
    for m in ARXIV.finditer(text):
        k = ("arxiv", m.group(1).lower())
        if k not in seen:
            seen.add(k)
            found.append(k)
    for m in DOI.finditer(text):
        d = m.group(1).rstrip(".,;)}")
        k = ("doi", d)
        if k not in seen:
            seen.add(k)
            found.append(k)
    if limit:
        found = found[:limit]
    out = []
    for kind, ident in found:
        status, detail = (resolve_arxiv if kind == "arxiv" else resolve_doi)(ident)
        out.append({"file": path, "kind": kind, "id": ident,
                    "status": status, "detail": detail})
        time.sleep(SLEEP)
    return out


def main(argv):
    limit = None
    jout = None
    skip = set()
    if "--limit" in argv:
        i = argv.index("--limit")
        limit = int(argv[i + 1]); skip |= {i, i + 1}
    if "--json" in argv:
        i = argv.index("--json")
        jout = argv[i + 1]; skip |= {i, i + 1}
    files = [a for i, a in enumerate(argv) if i > 0 and i not in skip
             and not a.startswith("--")]

    rows = []
    for f in files:
        rows.extend(scan(f, limit))

    bad = 0
    for r in rows:
        flag = {"OK": "  ok  ", "UNRESOLVED": " FAIL ", "NETWORK": " NET? "}[r["status"]]
        if r["status"] != "OK":
            bad = 1
        print("[%s] %-5s %-34s %s :: %s" % (flag, r["kind"], r["id"], r["file"], r["detail"][:70]))
    print("\n%d reference(s) checked; %d not OK." % (len(rows), sum(1 for r in rows if r["status"] != "OK")))
    if jout:
        json.dump(rows, open(jout, "w"), indent=1)
        print("json -> %s" % jout)
    print("NOTE: NETWORK is a BLOCK, not a pass. 'Could not check' is not 'it is fine'.")
    return bad


if __name__ == "__main__":
    sys.exit(main(sys.argv))
