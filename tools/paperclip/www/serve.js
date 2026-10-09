// Minimal static server for owner-facing reports at https://automath.mozone.io/reports/
// Serves /work/.www (git-ignored). Started by tools/paperclip/start.sh on port 3101.
// Access control is Cloudflare Access on the hostname; this server trusts the tunnel only.
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = process.env.REPORTS_ROOT || "/work/.www", PORT = Number(process.env.REPORTS_PORT || 3101);
const TYPES = { ".html": "text/html; charset=utf-8", ".md": "text/plain; charset=utf-8", ".txt": "text/plain; charset=utf-8",
  ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".png": "image/png", ".svg": "image/svg+xml", ".pdf": "application/pdf" };
http.createServer((req, res) => {
  const raw = (req.url || "/").split("?")[0];
  if (raw === "/reports") { res.writeHead(302, { Location: "/reports/" }); return res.end(); }
  let p = decodeURIComponent(raw).replace(/^\/reports\/?/, "/");
  if (p.endsWith("/")) p += "index.html";
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT + path.sep) && file !== ROOT) { res.writeHead(403); return res.end("forbidden"); }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) { res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" }); return res.end("not found"); }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream", "Cache-Control": "no-cache" });
    fs.createReadStream(file).pipe(res);
  });
}).listen(PORT, "0.0.0.0", () => console.log(`[reports] serving ${ROOT} on :${PORT} under /reports/`));
