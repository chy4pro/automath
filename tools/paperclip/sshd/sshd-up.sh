#!/bin/sh
# Unprivileged OpenSSH sshd for a Workbench AI container, so Paperclip (project container) can use it as an
# `ssh` environment over the docker network. Binaries: /work/.tools/sshd/root (Debian bookworm arm64 packages,
# see /work/.tools/sshd/MANIFEST.txt). State per container: /work/.tools/sshd/state/<hostname>/.
# Usage: sh /work/tools/paperclip/sshd/sshd-up.sh [port]   (default 2222; pubkey only; AllowUsers = current user)
set -e
PORT="${1:-2222}"; R=/work/.tools/sshd/root; S=/work/.tools/sshd/state/$(hostname); U=$(id -un)
mkdir -p "$S"; chmod 700 "$S"
export LD_LIBRARY_PATH=$R/usr/lib/aarch64-linux-gnu:$R/lib/aarch64-linux-gnu
[ -f "$S/hostkey" ] || ssh-keygen -q -t ed25519 -N "" -f "$S/hostkey" -C "sshd@$(hostname)"
AK=/work/.paperclip/ssh/authorized_keys   # Paperclip's public key(s); shared on the project volume
[ -s "$AK" ] || { echo "no authorized keys at $AK"; exit 1; }
cat > "$S/sshd_config" <<CFG
Port $PORT
ListenAddress 0.0.0.0
HostKey $S/hostkey
PidFile $S/sshd.pid
AuthorizedKeysFile $AK
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
PermitRootLogin no
UsePAM no
StrictModes no
AllowUsers $U
LogLevel INFO
PrintMotd no
UseDNS no
Subsystem sftp internal-sftp
CFG
if [ -f "$S/sshd.pid" ] && kill -0 "$(cat "$S/sshd.pid")" 2>/dev/null; then echo "sshd already running (pid $(cat "$S/sshd.pid"))"; exit 0; fi
nohup "$R/usr/sbin/sshd" -D -f "$S/sshd_config" -E "$S/sshd.log" >/dev/null 2>&1 &
sleep 1
IP=$(hostname -I 2>/dev/null | awk '{print $1}')
echo "sshd up: $U@$IP:$PORT (host $(hostname)); host key fingerprint: $(ssh-keygen -lf "$S/hostkey.pub" | awk '{print $2}')"
