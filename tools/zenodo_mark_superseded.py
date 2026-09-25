#!/usr/bin/env python3
"""Mark older Zenodo versions as superseded by editing their metadata in place (no new version).
Prefixes the description with a notice pointing to the concept DOI. Token from ~/.automath_engine_keys, never printed.
Usage: python3 zenodo_mark_superseded.py CONCEPT_DOI RECORD_ID [RECORD_ID ...]"""
import sys, os, json, urllib.request, urllib.error
def token():
    for line in open(os.path.expanduser('~/.automath_engine_keys')):
        if line.startswith('ZENODO_TOKEN='): return line.split('=',1)[1].strip().strip('"').strip("'")
    raise SystemExit('no ZENODO_TOKEN')
def req(method, url, data=None):
    h = {'Authorization': 'Bearer ' + token()}
    body = json.dumps(data).encode() if data is not None else None
    if body is not None: h['Content-Type'] = 'application/json'
    r = urllib.request.Request(url, data=body, method=method, headers=h)
    with urllib.request.urlopen(r, timeout=180) as resp:
        t = resp.read(); return json.loads(t) if t else {}
concept = sys.argv[1]
notice = ('<p><b>Superseded version.</b> This record is an earlier version of the paper; the current version is always available at the '
          f'concept DOI <a href="https://doi.org/{concept}">https://doi.org/{concept}</a>. Please cite and read the latest version.</p>\n')
for rid in sys.argv[2:]:
    try:
        req('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/edit')
        dep = req('GET', f'https://zenodo.org/api/deposit/depositions/{rid}')
        meta = dep['metadata']
        if 'Superseded version.' in meta.get('description', ''):
            print(rid, 'already marked'); req('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/publish'); continue
        meta['description'] = notice + meta.get('description', '')
        meta.pop('doi', None); meta.pop('prereserve_doi', None)
        req('PUT', f'https://zenodo.org/api/deposit/depositions/{rid}', data={'metadata': meta})
        req('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/publish')
        print(rid, 'marked superseded')
    except urllib.error.HTTPError as e:
        print(rid, 'HTTP error', e.code, e.read()[:200])
