#!/usr/bin/env node
// TCP relay to a Workbench local end's SSH bridge, for Paperclip.
//
// Workbench's documented path to a machine's sshd is an OpenSSH ProxyCommand that runs
// `node /opt/wb/kernel/local-shim.mjs <machine> ssh` (see /etc/ssh/ssh_config.d/wb.conf). That shim and the
// project's local-<machine>:ssh grant exist only in AI session containers. Paperclip runs in the project
// container, which has neither, so it cannot dial `<machine>.wb` itself. This relay runs in an AI session
// container and, for every accepted TCP connection, does exactly what that ProxyCommand does: spawn the shim
// and pipe bytes both ways. SSH authentication stays end to end between Paperclip and the machine's own sshd
// (public key only); the relay holds no SSH key and only ever sees ciphertext.
//
// Usage: node relay.mjs <machine> <listenHost> <listenPort> <allowedPeerIp[,ip...]>
import net from 'node:net';
import { spawn } from 'node:child_process';

const [machine, host, port, allow] = process.argv.slice(2);
if (!machine || !host || !port || !allow) { console.error('usage: relay.mjs <machine> <host> <port> <allowedPeerIps>'); process.exit(2); }
const allowed = new Set(allow.split(',').filter(Boolean));
const env = {
  PATH: process.env.PATH, HOME: process.env.HOME,
  WB_TOKEN_FILE: process.env.WB_TOKEN_FILE || '/wb/grant/token',
  WB_API: process.env.WB_API || 'http://host.docker.internal:8090',
};
const log = (...a) => console.log(new Date().toISOString(), ...a);

net.createServer((sock) => {
  const peer = (sock.remoteAddress || '').replace(/^::ffff:/, '');
  if (!allowed.has(peer)) { log('refused', peer); sock.destroy(); return; }
  const child = spawn(process.execPath, ['/opt/wb/kernel/local-shim.mjs', machine, 'ssh'], { env, stdio: ['pipe', 'pipe', 'pipe'] });
  log('open', peer, 'shim pid', child.pid);
  sock.pipe(child.stdin);
  child.stdout.pipe(sock);
  child.stderr.on('data', (d) => log('shim:', d.toString().trim()));
  child.stdin.on('error', () => {});
  sock.on('error', () => {});
  sock.on('close', () => {
    child.stdin.end();
    setTimeout(() => { if (child.exitCode === null && child.signalCode === null) child.kill('SIGTERM'); }, 10000).unref();
  });
  child.on('exit', (code, sig) => { log('close', peer, 'shim exit', code ?? sig); sock.end(); });
}).listen(Number(port), host, () => log(`relay ${host}:${port} -> ${machine} ssh; allowed peers ${[...allowed].join(',')}`));
