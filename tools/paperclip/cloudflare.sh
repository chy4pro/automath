#!/bin/bash
# One-shot Cloudflare setup for automath.mozone.io → Paperclip (host port 3100). Idempotent where possible.
# Needs a VALID token at /wb/creds/cloudflare-api-token/value with: Zone DNS:Edit (mozone.io),
# Account Cloudflare Tunnel:Edit, Access: Apps and Policies:Edit. Never prints secrets.
# Usage: bash tools/paperclip/cloudflare.sh <owner-email> [tunnel-name]
set -euo pipefail
EMAIL="${1:?owner e-mail for the Access policy}"; TNAME="${2:-automath}"
HOST="automath.mozone.io"; ZONE_NAME="mozone.io"; ORIGIN="http://localhost:3100"
T=$(cat /wb/creds/cloudflare-api-token/value); A=$(cat /wb/creds/cloudflare-account-id/value)
cf(){ curl -s -H "Authorization: Bearer $T" -H "Content-Type: application/json" "$@"; }
jq_(){ python3 -c "import sys,json; d=json.load(sys.stdin); $1"; }
API=https://api.cloudflare.com/client/v4
cf $API/user/tokens/verify | jq_ 'assert d["success"] and d["result"]["status"]=="active", d'
ZID=$(cf "$API/zones?name=$ZONE_NAME" | jq_ 'print(d["result"][0]["id"])')
echo "zone $ZONE_NAME = $ZID"
# 1. tunnel (remote-managed config)
TID=$(cf "$API/accounts/$A/cfd_tunnel?name=$TNAME&is_deleted=false" | jq_ 'r=d["result"]; print(r[0]["id"] if r else "")')
if [ -z "$TID" ]; then
  SECRET=$(head -c 32 /dev/urandom | base64 | tr -d '\n')
  TID=$(cf -X POST "$API/accounts/$A/cfd_tunnel" --data "{\"name\":\"$TNAME\",\"config_src\":\"cloudflare\",\"tunnel_secret\":\"$SECRET\"}" | jq_ 'print(d["result"]["id"])')
  echo "created tunnel $TNAME = $TID"
else echo "tunnel $TNAME = $TID (existing)"; fi
# 2. ingress: GET existing, merge our hostname, keep catch-all last
cf "$API/accounts/$A/cfd_tunnel/$TID/configurations" > /tmp/tun_cfg.json
python3 - "$HOST" "$ORIGIN" <<'PY'
import json,sys
host,origin=sys.argv[1:3]; d=json.load(open('/tmp/tun_cfg.json'))
cfg=(d.get('result') or {}).get('config') or {}; ing=[r for r in cfg.get('ingress',[]) if r.get('hostname')!=host and r.get('service')!='http_status:404']
ing.append({'hostname':host,'service':origin}); ing.append({'service':'http_status:404'}); cfg['ingress']=ing
json.dump({'config':cfg},open('/tmp/tun_new.json','w'))
PY
cf -X PUT "$API/accounts/$A/cfd_tunnel/$TID/configurations" --data @/tmp/tun_new.json | jq_ 'assert d["success"], d["errors"]; print("ingress updated:", [r.get("hostname") for r in d["result"]["config"]["ingress"]])'
# 3. DNS CNAME automath → <tunnel>.cfargotunnel.com (proxied)
RID=$(cf "$API/zones/$ZID/dns_records?type=CNAME&name=$HOST" | jq_ 'r=d["result"]; print(r[0]["id"] if r else "")')
BODY="{\"type\":\"CNAME\",\"name\":\"$HOST\",\"content\":\"$TID.cfargotunnel.com\",\"proxied\":true,\"ttl\":1}"
if [ -z "$RID" ]; then cf -X POST "$API/zones/$ZID/dns_records" --data "$BODY" | jq_ 'assert d["success"], d["errors"]; print("dns created")'
else cf -X PUT "$API/zones/$ZID/dns_records/$RID" --data "$BODY" | jq_ 'assert d["success"], d["errors"]; print("dns updated")'; fi
# 4. Access application + allow policy (owner e-mail only)
AID=$(cf "$API/accounts/$A/access/apps" | jq_ 'r=[a for a in d["result"] if a.get("domain")=="'"$HOST"'"]; print(r[0]["id"] if r else "")')
if [ -z "$AID" ]; then
  AID=$(cf -X POST "$API/accounts/$A/access/apps" --data "{\"name\":\"automath paperclip\",\"domain\":\"$HOST\",\"type\":\"self_hosted\",\"session_duration\":\"24h\",\"app_launcher_visible\":false,\"allowed_idps\":[],\"auto_redirect_to_identity\":false}" | jq_ 'assert d["success"], d["errors"]; print(d["result"]["id"])')
  echo "access app $AID"
  cf -X POST "$API/accounts/$A/access/apps/$AID/policies" --data "{\"name\":\"owner only\",\"decision\":\"allow\",\"include\":[{\"email\":{\"email\":\"$EMAIL\"}}],\"precedence\":1}" | jq_ 'assert d["success"], d["errors"]; print("policy created")'
else echo "access app exists: $AID (policies untouched)"; fi
# 5. connector token for the Workbench tunnel project (printed to a file, never to stdout)
cf "$API/accounts/$A/cfd_tunnel/$TID/token" | jq_ 'open("/work/.paperclip/tunnel.token","w").write(d["result"]); print("tunnel token written to /work/.paperclip/tunnel.token (keep out of git)")'
echo "DONE: $HOST → tunnel $TNAME → $ORIGIN; Access allow $EMAIL"
