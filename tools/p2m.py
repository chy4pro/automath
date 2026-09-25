#!/usr/bin/env python3
"""Minimal Prove2Me API client for automath.

Reads P2M_KEY from ~/.automath_engine_keys, exchanges it for a 1-hour access token
(cached in ~/.automath_p2m_token.json, mode 600), and sends requests ONLY to
https://prove2.me/api/v1. Never prints the key or the token.

Usage:
  python3 tools/p2m.py get /missions
  python3 tools/p2m.py get "/theorems?q=Erdos%20709"
  python3 tools/p2m.py post /verify --form theorem_id=... --file solution.lean --form explanation=...
  python3 tools/p2m.py post /submit-problem --json '{"...": ...}'
  python3 tools/p2m.py patch /submissions/<id> --json '{"explanation": "..."}'
"""
import json, os, sys, time, urllib.request, urllib.parse, uuid

BASE = "https://prove2.me/api/v1"
KEYS = os.path.expanduser("~/.automath_engine_keys")
TOKEN_CACHE = os.path.expanduser("~/.automath_p2m_token.json")


def api_key():
    with open(KEYS) as f:
        for line in f:
            if line.startswith("P2M_KEY="):
                return line.strip().split("=", 1)[1]
    sys.exit("P2M_KEY missing in ~/.automath_engine_keys")


def access_token():
    try:
        with open(TOKEN_CACHE) as f:
            c = json.load(f)
        if c.get("expires_at", 0) - time.time() > 120:
            return c["access_token"]
    except Exception:
        pass
    req = urllib.request.Request(BASE + "/agent/refresh", data=json.dumps({"api_key": api_key()}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        c = json.loads(r.read())
    with open(TOKEN_CACHE, "w") as f:
        json.dump(c, f)
    os.chmod(TOKEN_CACHE, 0o600)
    sys.stderr.write("[p2m] new access token; platform version %s\n" % c.get("version"))
    return c["access_token"]


def request(method, path, json_body=None, form=None, file_field=None):
    url = BASE + path
    headers = {"Authorization": "Bearer " + access_token()}
    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode()
        headers["Content-Type"] = "application/json"
    elif form is not None:
        boundary = "----automath" + uuid.uuid4().hex
        parts = []
        for k, v in form.items():
            parts.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n" % (boundary, k, v)).encode())
        if file_field:
            name, fpath = file_field
            with open(fpath, "rb") as fh:
                content = fh.read()
            parts.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"; filename=\"%s\"\r\nContent-Type: text/plain\r\n\r\n" % (boundary, name, os.path.basename(fpath))).encode() + content + b"\r\n")
        parts.append(("--%s--\r\n" % boundary).encode())
        data = b"".join(parts)
        headers["Content-Type"] = "multipart/form-data; boundary=" + boundary
    req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
            return r.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        print(__doc__); return
    method, path = a[0], a[1]
    json_body = None; form = {}; file_field = None; out = None
    i = 2
    while i < len(a):
        if a[i] == "--json":
            json_body = json.loads(a[i + 1]); i += 2
        elif a[i] == "--form":
            k, v = a[i + 1].split("=", 1); form[k] = v; i += 2
        elif a[i] == "--file":
            file_field = ("file", a[i + 1]); i += 2
        elif a[i] == "--out":
            out = a[i + 1]; i += 2
        else:
            sys.exit("unknown arg " + a[i])
    status, body = request(method, path, json_body, form if (form or file_field) else None, file_field)
    print("HTTP", status)
    if out:
        with open(out, "wb") as f:
            f.write(body)
        print("saved", len(body), "bytes to", out)
        return
    try:
        print(json.dumps(json.loads(body), ensure_ascii=False, indent=1))
    except Exception:
        print(body.decode("utf-8", "replace"))


if __name__ == "__main__":
    main()
