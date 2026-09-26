'use strict';
const fs=require('fs'),path=require('path');
const {Ops,power,cpu}=require('./run_n8.js');
const large=process.argv[2]==='large';
const ps=large?[Number(process.argv[3])]:[1009,10007,100003,1000003,1999993];
const out=path.join(__dirname,large?'large_T1_'+ps[0]+'_20260926.jsonl':'refinement_20260926.jsonl');
if(fs.existsSync(out))throw Error('output exists; move aside explicitly before rerunning');
function emit(r){fs.appendFileSync(out,JSON.stringify(r)+'\n');console.log(JSON.stringify({p:r.p,kind:r.kind,N:r.N,sigma:r.sigma_lower_estimate,residual:r.residual_tstar_t,cpu:r.cpu_total||r.cpu_seconds,complete:r.complete}));}
for(const p of ps){const O=new Ops(p);for(const kind of(large?['T1']:p<=100003?['T1','T2']:['T2']))for(const N of[4,16,64,256]){const t=cpu(),d=power(O.op(kind,N),p+1,large?200:p<=10007?1600:800,987654321,large?1250:3000);emit({p,kind,N,...d,free_T1_comparator:2*Math.sqrt(N-1)/N,cpu_seconds:cpu()-t,cpu_total:cpu(),rss_bytes:process.memoryUsage().rss});}}
emit({complete:true,cpu_seconds:cpu(),rss_bytes:process.memoryUsage().rss});
