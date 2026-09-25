#!/usr/bin/env python3
"""Publish a NEW VERSION of an existing Zenodo record with a replaced PDF. Token from ~/.automath_engine_keys
(ZENODO_TOKEN=...), never printed. Usage: python3 zenodo_newversion.py RECORD_ID FILE.pdf [--publish] [--version 2] [--description FILE.html]"""
import sys, os, json, urllib.request
def token():
    for line in open(os.path.expanduser('~/.automath_engine_keys')):
        if line.startswith('ZENODO_TOKEN='): return line.split('=',1)[1].strip().strip('"').strip("'")
    raise SystemExit('no ZENODO_TOKEN')
def req(method, url, data=None, headers=None, raw=None):
    h = {'Authorization': 'Bearer ' + token()}
    if headers: h.update(headers)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    if body is not None and raw is None: h['Content-Type'] = 'application/json'
    r = urllib.request.Request(url, data=body, method=method, headers=h)
    with urllib.request.urlopen(r, timeout=180) as resp:
        t = resp.read(); return json.loads(t) if t else {}
def main():
    rec = sys.argv[1]; pdf = sys.argv[2]; publish = '--publish' in sys.argv
    version = sys.argv[sys.argv.index('--version') + 1] if '--version' in sys.argv else None
    nv = req('POST', f'https://zenodo.org/api/deposit/depositions/{rec}/actions/newversion')
    draft_url = nv['links']['latest_draft']
    draft = req('GET', draft_url); did = draft['id']
    # remove old files from the draft, upload the new one
    for f in draft.get('files', []):
        req('DELETE', f"https://zenodo.org/api/deposit/depositions/{did}/files/{f['id']}")
    bucket = draft['links']['bucket']
    with open(pdf, 'rb') as fh:
        req('PUT', bucket + '/' + os.path.basename(pdf), raw=fh.read(), headers={'Content-Type': 'application/octet-stream'})
    desc = open(sys.argv[sys.argv.index('--description') + 1], encoding='utf-8').read() if '--description' in sys.argv else None
    if version or desc:
        meta = draft['metadata']
        if version: meta['version'] = version
        if desc: meta['description'] = desc
        meta.pop('doi', None); meta.pop('prereserve_doi', None)
        req('PUT', f'https://zenodo.org/api/deposit/depositions/{did}', data={'metadata': meta})
    if publish:
        pub = req('POST', f'https://zenodo.org/api/deposit/depositions/{did}/actions/publish')
        print('PUBLISHED', pub.get('doi'), pub.get('links', {}).get('record_html'), 'concept', pub.get('conceptdoi'))
    else:
        print('DRAFT new version', did, '(not published)')
if __name__ == '__main__': main()
