'use strict';
// Save the final large T1 point even if its allotted CPU budget is reached.
const fs=require('fs'),path=require('path');
const {Ops,power,cpu}=require('./run_n8.js');
const out=path.join(__dirname,'last_T1_1999993_N256_20260926.jsonl');
if(fs.existsSync(out))throw Error('output exists');
const O=new Ops(1999993),r=power(O.op('T1',256),O.n,100,987654321,600);
const data={p:1999993,kind:'T1',N:256,...r,free_T1_comparator:2*Math.sqrt(255)/256,cpu_seconds:cpu(),rss_bytes:process.memoryUsage().rss};
fs.writeFileSync(out,JSON.stringify(data)+'\n'+JSON.stringify({complete:true,cpu_seconds:cpu(),rss_bytes:process.memoryUsage().rss})+'\n');
console.log(JSON.stringify({...data,history:undefined}));
