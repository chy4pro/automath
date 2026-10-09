// Owner-facing pages at https://automath.mozone.io/reports/ (static files from /work/.www, git-ignored)
// plus a live Chinese progress page at /reports/status rendered from the Paperclip API.
// Started by tools/paperclip/start.sh on port 3101; access control is Cloudflare Access on the hostname.
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = process.env.REPORTS_ROOT || "/work/.www", PORT = Number(process.env.REPORTS_PORT || 3101);
const API = process.env.PAPERCLIP_API_URL || "http://localhost:3100/api";
const COMPANY = process.env.PAPERCLIP_COMPANY_ID || "d0817321-3b6a-412d-8aaa-1e2b42e35cae";
const TOKEN_FILE = process.env.PAPERCLIP_BOARD_TOKEN_FILE || "/work/.paperclip/board.token";
const TYPES = { ".html": "text/html; charset=utf-8", ".md": "text/plain; charset=utf-8", ".txt": "text/plain; charset=utf-8",
  ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".png": "image/png", ".svg": "image/svg+xml", ".pdf": "application/pdf" };
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const STATUS = { todo: "待办", in_progress: "进行中", blocked: "等待子任务", in_review: "待审", done: "完成", backlog: "积压", cancelled: "取消" };
const RUN = { running: "运行中", queued: "排队", succeeded: "成功", failed: "失败", timed_out: "超时", cancelled: "取消", setup_failed: "启动失败" };
const sh = (iso) => iso ? new Date(iso).toLocaleString("zh-CN", { timeZone: "Asia/Shanghai", hour12: false }) : "—";
const mins = (a, b) => a && b ? Math.round((new Date(b) - new Date(a)) / 60000) + " 分" : "—";
async function api(p) {
  const tok = fs.readFileSync(TOKEN_FILE, "utf8").trim();
  const r = await fetch(API + p, { headers: { Authorization: "Bearer " + tok, Origin: "https://automath.mozone.io" } });
  if (!r.ok) throw new Error(`${p} -> ${r.status}`);
  return r.json();
}
async function statusPage() {
  const [agentsRaw, issuesRaw, runsRaw, activityRaw] = await Promise.all([
    api(`/companies/${COMPANY}/agents`), api(`/companies/${COMPANY}/issues`),
    api(`/companies/${COMPANY}/heartbeat-runs`), api(`/companies/${COMPANY}/activity?limit=40`)]);
  const agents = Array.isArray(agentsRaw) ? agentsRaw : agentsRaw.agents ?? [];
  const issues = (Array.isArray(issuesRaw) ? issuesRaw : issuesRaw.issues ?? []).filter((i) => !i.routineId && !i.conversationAgentId);
  const runs = Array.isArray(runsRaw) ? runsRaw : runsRaw.runs ?? [];
  const activity = Array.isArray(activityRaw) ? activityRaw : activityRaw.activity ?? activityRaw.items ?? [];
  const name = Object.fromEntries(agents.map((a) => [a.id, a.name]));
  const byId = Object.fromEntries(issues.map((i) => [i.id, i]));
  const live = runs.filter((r) => r.status === "running" || r.status === "queued");
  const open = issues.filter((i) => !["done", "cancelled"].includes(i.status)).sort((a, b) => (b.updatedAt || "").localeCompare(a.updatedAt || ""));
  const recentDone = issues.filter((i) => i.status === "done").sort((a, b) => (b.updatedAt || "").localeCompare(a.updatedAt || "")).slice(0, 12);
  const lastComment = {};
  await Promise.all(open.slice(0, 12).concat(recentDone.slice(0, 6)).map(async (i) => {
    try { const cs = await api(`/issues/${i.id}/comments`); const c = (Array.isArray(cs) ? cs : cs.comments ?? []).at(-1);
      if (c) lastComment[i.id] = { who: name[c.authorAgentId] || (c.authorUserId ? "业主" : "系统"), at: c.createdAt, body: c.body || "" }; } catch {}
  }));
  const today = new Date(); today.setUTCHours(0, 0, 0, 0);
  const tot = { in: 0, cached: 0, out: 0, n: 0, running: 0 }; const perAgent = {};
  for (const r of runs) { let u = r.usageJson || r.usage || {}; if (new Date(r.createdAt) < today) continue;
    if (r.status === "running") { tot.running++; continue; }
    if (!u.inputTokens && !u.outputTokens) continue;
    // Codex reports inputTokens inclusive of cached reads; Claude reports them separately. Normalise to "new input".
    if ((u.model || "").startsWith("gpt")) u = { ...u, inputTokens: Math.max(0, (u.inputTokens || 0) - (u.cachedInputTokens || 0)) };
    tot.in += u.inputTokens || 0; tot.cached += u.cachedInputTokens || 0; tot.out += u.outputTokens || 0; tot.n++;
    const k = name[r.agentId] || r.agentId; const a = perAgent[k] ||= { n: 0, in: 0, cached: 0, out: 0, usd: 0, model: u.model || "" };
    a.n++; a.in += u.inputTokens || 0; a.cached += u.cachedInputTokens || 0; a.out += u.outputTokens || 0; a.usd += u.costUsd || 0; }
  const issueRow = (i) => { const c = lastComment[i.id]; const parent = i.parentId && byId[i.parentId] ? ` ← ${byId[i.parentId].identifier}` : "";
    return `<tr><td><a href="/AUT/issues/${esc(i.identifier)}">${esc(i.identifier)}</a>${esc(parent)}</td><td>${esc(i.title)}</td><td>${esc(STATUS[i.status] || i.status)}</td><td>${esc(name[i.assigneeAgentId] || "—")}</td><td>${sh(i.updatedAt)}</td></tr>` +
      (c ? `<tr class="c"><td colspan="5"><b>${esc(c.who)}</b> <span class="meta">${sh(c.at)}</span><br>${esc(c.body.slice(0, 600))}${c.body.length > 600 ? " …" : ""}</td></tr>` : ""); };
  const runRow = (r) => { const u = r.usageJson || r.usage || {}; const iid = (r.contextSnapshot || {}).issueId; const iss = iid && byId[iid];
    return `<tr><td>${esc(name[r.agentId] || r.agentId)}</td><td>${iss ? `<a href="/AUT/issues/${esc(iss.identifier)}">${esc(iss.identifier)}</a> ${esc(iss.title.slice(0, 50))}` : "—"}</td><td>${esc(RUN[r.status] || r.status)}</td><td>${sh(r.createdAt)}</td><td>${mins(r.startedAt, r.finishedAt || (r.status === "running" ? new Date().toISOString() : null))}</td><td>${u.inputTokens || u.outputTokens ? `${((u.inputTokens || 0) / 1000).toFixed(0)}k+${((u.cachedInputTokens || 0) / 1e6).toFixed(1)}M缓存 / ${((u.outputTokens || 0) / 1000).toFixed(1)}k` : r.status === "running" ? "结束后统计" : "无记录"}</td><td>${esc((r.error || "").slice(0, 80))}</td></tr>`; };
  const actRow = (a) => `<tr><td>${sh(a.createdAt)}</td><td>${esc(a.actorType === "user" ? "业主" : name[a.agentId] || a.actorType)}</td><td>${esc(a.action)}</td><td>${esc(a.entityType === "issue" && byId[a.entityId] ? byId[a.entityId].identifier : "")}</td></tr>`;
  const recentRuns = [...runs].sort((a, b) => (b.createdAt || "").localeCompare(a.createdAt || "")).slice(0, 40);
  return `<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="120"><title>automath 实时进度</title><link rel="stylesheet" href="/reports/style.css"><style>.c td{background:#f3f3f3;font-size:.9rem;white-space:pre-wrap}table{width:100%;font-size:.92rem}</style></head><body>
<p class="meta"><a href="/reports/">← 战报目录</a> · <a href="/">Paperclip 看板</a> · 生成于 ${sh(new Date().toISOString())}（每 2 分钟自动刷新）</p>
<h1>automath 实时进度</h1>
<h2>正在运行（${live.length}）</h2>${live.length ? `<table><tr><th>代理</th><th>任务</th><th>状态</th><th>开始</th><th>已用</th><th>token 入/出</th><th></th></tr>${live.map(runRow).join("")}</table>` : "<p>没有代理在运行。</p>"}
<h2>未完成任务（${open.length}）</h2><p class="meta">每个任务下方是最新一条评论，即协调者/代理最近说的话。</p><table><tr><th>编号</th><th>标题</th><th>状态</th><th>负责</th><th>更新</th></tr>${open.map(issueRow).join("")}</table>
<h2>最近完成</h2><table><tr><th>编号</th><th>标题</th><th>状态</th><th>负责</th><th>更新</th></tr>${recentDone.map(issueRow).join("")}</table>
<h2>最近 40 次运行</h2><table><tr><th>代理</th><th>任务</th><th>状态</th><th>开始</th><th>时长</th><th>token 新输入+缓存读 / 输出</th><th>错误</th></tr>${recentRuns.map(runRow).join("")}</table>
<h2>今日用量（UTC 日，只统计已结束的 run）</h2><p>${tot.n} 次已结束运行${tot.running ? `，另有 ${tot.running} 次运行中（结束后才有 token 数）` : ""}：新输入 ${(tot.in / 1e6).toFixed(2)}M，缓存读 ${(tot.cached / 1e6).toFixed(2)}M，输出 ${(tot.out / 1000).toFixed(0)}k token。全部订阅内，不计现金；"参考价"是 Claude 按列表价折算，Codex 无参考价。</p>
<table><tr><th>代理</th><th>模型</th><th>次数</th><th>新输入</th><th>缓存读</th><th>输出</th><th>参考价</th></tr>${Object.entries(perAgent).sort((a, b) => b[1].out - a[1].out).map(([k, a]) => `<tr><td>${esc(k)}</td><td>${esc(a.model)}</td><td>${a.n}</td><td>${(a.in / 1000).toFixed(0)}k</td><td>${(a.cached / 1e6).toFixed(2)}M</td><td>${(a.out / 1000).toFixed(0)}k</td><td>${a.usd ? "$" + a.usd.toFixed(2) : "—"}</td></tr>`).join("")}</table>
<h2>代理</h2><table><tr><th>代理</th><th>状态</th><th>角色</th></tr>${agents.map((a) => `<tr><td>${esc(a.name)}</td><td>${esc(a.status)}</td><td>${esc(a.title || a.role)}</td></tr>`).join("")}</table>
<h2>最近活动</h2><table><tr><th>时间</th><th>谁</th><th>动作</th><th>任务</th></tr>${activity.slice(0, 40).map(actRow).join("")}</table>
</body></html>`;
}
http.createServer(async (req, res) => {
  const raw = (req.url || "/").split("?")[0];
  if (raw === "/reports") { res.writeHead(302, { Location: "/reports/" }); return res.end(); }
  if (raw === "/reports/status" || raw === "/reports/status.html") {
    try { const html = await statusPage(); res.writeHead(200, { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" }); return res.end(html); }
    catch (e) { res.writeHead(502, { "Content-Type": "text/plain; charset=utf-8" }); return res.end("status page error: " + e.message); }
  }
  let p = decodeURIComponent(raw).replace(/^\/reports\/?/, "/");
  if (p.endsWith("/")) p += "index.html";
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT + path.sep) && file !== ROOT) { res.writeHead(403); return res.end("forbidden"); }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) { res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" }); return res.end("not found"); }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream", "Cache-Control": "no-cache" });
    fs.createReadStream(file).pipe(res);
  });
}).listen(PORT, "0.0.0.0", () => console.log(`[reports] serving ${ROOT} on :${PORT} under /reports/ (+ /reports/status)`));
