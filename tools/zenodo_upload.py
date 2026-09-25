#!/usr/bin/env python3
"""Upload a PDF to Zenodo as a new deposition and publish it. Token read from ~/.automath_engine_keys (ZENODO_TOKEN=...),
never printed. Usage: python3 zenodo_upload.py FILE.pdf TITLE 'AUTHOR NAME' DESCRIPTION_FILE [--publish]"""
import sys, os, json, urllib.request, urllib.parse, mimetypes
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
    with urllib.request.urlopen(r, timeout=120) as resp:
        t = resp.read()
        return json.loads(t) if t else {}
def main():
    pdf, title, author, descfile = sys.argv[1:5]; publish = '--publish' in sys.argv
    desc = open(descfile).read()
    dep = req('POST', 'https://zenodo.org/api/deposit/depositions', data={})
    dep_id = dep['id']; bucket = dep['links']['bucket']
    with open(pdf, 'rb') as f:
        req('PUT', bucket + '/' + os.path.basename(pdf), raw=f.read(), headers={'Content-Type': 'application/octet-stream'})
    meta = {'metadata': {'title': title, 'upload_type': 'publication', 'publication_type': 'preprint',
            'description': desc, 'creators': [{'name': author}], 'access_right': 'open', 'license': 'cc-zero',
            'keywords': ['Erdős problems', 'number theory', 'divisibility', 'Erdős–Surányi', 'automated theorem proving']}}
    req('PUT', f'https://zenodo.org/api/deposit/depositions/{dep_id}', data=meta)
    if publish:
        pub = req('POST', f'https://zenodo.org/api/deposit/depositions/{dep_id}/actions/publish')
        print('PUBLISHED', pub.get('doi'), pub.get('links', {}).get('record_html'))
    else:
        print('DRAFT deposition', dep_id, '(not published)')
if __name__ == '__main__': main()
