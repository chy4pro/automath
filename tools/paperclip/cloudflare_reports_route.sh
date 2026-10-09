#!/bin/sh
# Add the /reports path rule to the automath tunnel ingress (static report server on :3101), keep the
# Paperclip catch-all for the hostname and the http_status:404 fallback last. Idempotent.
set -e
API=https://api.cloudflare.com/client/v4
T=$(cat /wb/creds/cloudflare-api-token/value); A=$(cat /wb/creds/cloudflare-account-id/value)
HOST=${HOST:-automath.mozone.io}; TNAME=${TNAME:-automath}
cf(){ curl -s -H "Authorization: Bearer $T" -H "Content-Type: application/json" "$@"; }
jq_(){ python3 -c "import json,sys; d=json.load(sys.stdin); $1"; }
TID=$(cf "$API/accounts/$A/cfd_tunnel?name=$TNAME&is_deleted=false" | jq_ 'r=d["result"]; print(r[0]["id"] if r else "")')
[ -n "$TID" ] || { echo "tunnel $TNAME not found"; exit 1; }
cf "$API/accounts/$A/cfd_tunnel/$TID/configurations" > /tmp/tun_cfg.json
python3 - "$HOST" <<'PY' > /tmp/tun_new.json
import json,sys; host=sys.argv[1]; d=json.load(open('/tmp/tun_cfg.json'))
cfg=(d.get('result') or {}).get('config') or {}
ing=[r for r in cfg.get('ingress',[]) if r.get('hostname')!=host and r.get('service')!='http_status:404']
ing.append({'hostname':host,'path':'^/reports(/.*)?$','service':'http://localhost:3101'})
ing.append({'hostname':host,'service':'http://localhost:3100'})
ing.append({'service':'http_status:404'}); cfg['ingress']=ing
json.dump({'config':cfg}, sys.stdout)
PY
cf -X PUT "$API/accounts/$A/cfd_tunnel/$TID/configurations" --data @/tmp/tun_new.json | jq_ 'assert d["success"], d["errors"]; print("ingress:", [(r.get("hostname"), r.get("path"), r["service"]) for r in d["result"]["config"]["ingress"]])'
