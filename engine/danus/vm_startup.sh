#!/bin/bash
# Danus evaluation host — first-boot provisioning for a disposable GCP VM (Debian 12).
# Committed repo file; referenced by path at launch. Installs only what Danus's
# getting-started lists as host prerequisites, then clones the codex branch.
# Secrets are NOT here: config/codex.env is copied in over ssh after boot.
set -x
exec > /var/log/danus-provision.log 2>&1
apt-get update -qq
apt-get install -y -qq git python3 python3-venv python3-pip curl tar tmux xz-utils jq >/dev/null
mkdir -p /opt/danus && chown "$(id -un 1000 2>/dev/null || echo root)" /opt/danus
cd /opt && git clone -q --branch codex --depth 1 https://github.com/frenzymath/Danus danus
chown -R 1000:1000 /opt/danus 2>/dev/null || true
touch /opt/danus/.provisioned
