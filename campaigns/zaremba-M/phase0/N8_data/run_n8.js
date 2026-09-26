'use strict';
// Dependency-free fallback, task007. Numerical estimates, not certified spectral upper bounds.
const fs=require('fs'),path=require('path');
const stop='/work/inbox/to_codex/STOP';
const started=process.cpuUsage(),wall0=Date.now();
const cpu=()=>{const t=process.cpuUsage(started);return(t.user+t.system)/1e6;};
function prime(p){if(p<3||p%2===0)return false;for(let d=3;d*d<=p;d+=2)if(p%d===0)return false;return true;}
function project(a){let s=0;for(const v of a)s+=v;s/=a.length;for(let i=0;i<a.length;i++)a[i]-=s;return a;}
function dot(a,b){let s=0;for(let i=0;i<a.length;i++)s+=a[i]*b[i];return s;}
function norm(a){return Math.sqrt(dot(a,a));}
function normalize(a){const n=norm(a);if(!n)return false;for(let i=0;i<a.length;i++)a[i]/=n;return true;}
function random(n,seed){let state=seed>>>0;const a=new Float64Array(n);for(let i=0;i<n;i++){state^=state<<13;state^=state>>>17;state^=state<<5;a[i]=(state>>>0)/4294967296-.5;}project(a);normalize(a);return a;}
class Ops{
 constructor(p){if(!prime(p)||p>2000000)throw Error('prime/cap');this.p=p;this.n=p+1;this.inv=new Int32Array(p);this.inv[1]=1;for(let a=2;a<p;a++)this.inv[a]=p-(Math.floor(p/a)*this.inv[p%a])%p;for(let a=1;a<p;a++)if((a*this.inv[a])%p!==1)throw Error('inverse');this.tmp=new Float64Array(p+1);this.tmp2=new Float64Array(p+1);this.perms=new Map();}
 shift(f,out,N,sgn){const p=this.p;let sum=0;for(let h=1;h<=N;h++)sum+=f[sgn===1?h%p:(p-h)%p];out[0]=sum/N;let err=0;for(let x=0;x<p-1;x++){let gone=sgn===1?(x+1)%p:(x+p-N)%p,added=sgn===1?(x+N+1)%p:x;let delta=f[added]-f[gone],y=delta-err,t=sum+y;err=(t-sum)-y;sum=t;out[x+1]=sum/N;}out[p]=f[p];}
 op(kind,N){if(N<1||N>Math.min(256,this.p))throw Error('N');const p=this.p,n=this.n;
  if(kind==='T1'&&N*n*4<=64*1024*1024&&!this.perms.has(N)){const perms=new Int32Array(N*n);for(let j=1;j<=N;j++){const s=2*j%p;for(let x=0;x<p;x++){let z=x+s;if(z>=p)z-=p;let y=z===0?p:this.inv[z]-s;if(y<0)y+=p;perms[(j-1)*n+x]=y;}perms[(j-1)*n+p]=(p-s)%p;}this.perms.clear();this.perms.set(N,perms);}
  return(f,out)=>{if(f.length!==n||out.length!==n)throw Error('operator dimension');if(kind==='T2'){this.shift(f,this.tmp,N,-1);this.tmp2[0]=this.tmp[p];this.tmp2[p]=this.tmp[0];for(let x=1;x<p;x++)this.tmp2[x]=this.tmp[this.inv[x]];this.shift(this.tmp2,out,N,1);}else if(kind==='T1'){out.fill(0);const pp=this.perms.get(N);for(let j=1;j<=N;j++){if(pp){let k=(j-1)*n;for(let x=0;x<n;x++)out[x]+=f[pp[k+x]];}else{let s=2*j%p;for(let x=0;x<p;x++){let z=x+s;if(z>=p)z-=p;let y=z===0?p:this.inv[z]-s;if(y<0)y+=p;out[x]+=f[y];}out[p]+=f[(p-s)%p];}}for(let x=0;x<n;x++)out[x]/=N;}else throw Error('kind');project(out);};
 }
}
function power(op,n,iters,seed,budget=3400){let f=random(n,seed),g=new Float64Array(n),h=new Float64Array(n),lam=0,res=0;const history=[];let it=0,completed=0,reason="iteration_limit";for(it=1;it<=iters;it++){if(fs.existsSync(stop))throw Error('STOP');if(cpu()>budget){reason='cpu_budget';break;}op(f,g);op(g,h);lam=dot(g,g);let rr=0;for(let i=0;i<n;i++){let d=h[i]-lam*f[i];rr+=d*d;}res=Math.sqrt(rr);completed=it;if(it%25===0||it===iters)history.push({iteration:it,sigma:Math.sqrt(lam),residual:res});if(res<1e-11*Math.max(1,lam)||!normalize(h)){reason="converged_or_zero";break;}[f,h]=[h,f];}if(!completed)throw Error("no completed power iteration");return{dimension:n,sigma_lower_estimate:Math.sqrt(lam),residual_tstar_t:res,iterations:completed,termination:reason,seed,history};}
// Independent dense construction uses Euclid inverses, not Ops' inverse recurrence.
function inverse(a,p){let r=p,s=a,u=0,v=1;while(s){let q=Math.floor(r/s);[r,s]=[s,r-q*s];[u,v]=[v,u-q*v];}return(u%p+p)%p;}
function dense(p,kind,N){let n=p+1,M=Array.from({length:n},()=>new Float64Array(n));const add=(x,a)=>x===p?p:((x+a)%p+p)%p,rec=x=>x===p?0:x===0?p:inverse(x,p);for(let x=0;x<n;x++)if(kind==='T1'){for(let j=1;j<=N;j++)M[x][add(rec(add(x,2*j)),-2*j)]+=1/N;}else{for(let a=1;a<=N;a++)for(let b=1;b<=N;b++)M[x][add(rec(add(x,a)),-b)]+=1/(N*N);}let symmetry=0,rowerr=0;for(let i=0;i<n;i++){rowerr=Math.max(rowerr,Math.abs(M[i].reduce((a,b)=>a+b,0)-1));for(let j=0;j<n;j++){symmetry=Math.max(symmetry,Math.abs(M[i][j]-M[j][i]));M[i][j]-=1/n;}}// Recompute symmetry on centered M (previous loop mixes centered and uncentered entries).
 symmetry=0;for(let i=0;i<n;i++)for(let j=0;j<n;j++)symmetry=Math.max(symmetry,Math.abs(M[i][j]-M[j][i]));
 const O=new Ops(p),apply=O.op(kind,N);let maxerr=0;const f=new Float64Array(n),o=new Float64Array(n);for(let j=0;j<n;j++){f.fill(0);f[j]=1;apply(f,o);for(let i=0;i<n;i++)maxerr=Math.max(maxerr,Math.abs(o[i]-M[i][j]));}
 // One-sided cyclic Jacobi SVD on dense centered columns; singular values are final column norms.
 let maxcorr=0,sweeps=0;for(sweeps=0;sweeps<80;sweeps++){maxcorr=0;let rotations=0;for(let a=0;a<n-1;a++)for(let b=a+1;b<n;b++){let aa=0,bb=0,ab=0;for(let i=0;i<n;i++){aa+=M[i][a]**2;bb+=M[i][b]**2;ab+=M[i][a]*M[i][b];}const scale=Math.sqrt(aa*bb);if(scale<1e-28)continue;maxcorr=Math.max(maxcorr,Math.abs(ab)/scale);if(Math.abs(ab)<=1e-13*scale)continue;let z=(bb-aa)/(2*ab),t=(z>=0?1:-1)/(Math.abs(z)+Math.sqrt(1+z*z)),cs=1/Math.sqrt(1+t*t),sn=cs*t;for(let i=0;i<n;i++){let x=M[i][a],y=M[i][b];M[i][a]=cs*x-sn*y;M[i][b]=sn*x+cs*y;}rotations++;}if(!rotations)break;}
 const sv=[];for(let j=0;j<n;j++){let ss=0;for(let i=0;i<n;i++)ss+=M[i][j]**2;sv.push(Math.sqrt(ss));}sv.sort((a,b)=>b-a);return{sigma_svd:sv[0],sigma2_svd:sv[1],dense_symmetry_error:symmetry,row_sum_error:rowerr,sparse_dense_entry_error:maxerr,jacobi_sweeps:sweeps,max_column_correlation:maxcorr};}
function run(){
const out=process.argv[2]||path.join(__dirname,'grid_20260926.jsonl');
function emit(rec){fs.appendFileSync(out,JSON.stringify(rec)+'\n');console.log(JSON.stringify(rec));}
if(fs.existsSync(out)&&fs.statSync(out).size)throw Error('output exists; use a fresh path');
emit({metadata:true,date:new Date().toISOString(),node:process.version,cpu_limit_seconds:3400,memory_limit_note:'run with --max-old-space-size=768; typed arrays monitored separately',status:'finite numerical estimates only'});
for(const p of[31,101])for(const kind of['T1','T2'])for(const N of[4,16]){let O=new Ops(p),a=O.op(kind,N),rec=power(a,p+1,400,12345),d=dense(p,kind,N);if(d.sparse_dense_entry_error>1e-10||d.dense_symmetry_error>1e-12||Math.abs(rec.sigma_lower_estimate-d.sigma_svd)>3e-4)throw Error('dense recheck');emit({p,kind,N,...rec,...d,free_T1_comparator:2*Math.sqrt(N-1)/N,cpu_total:cpu(),rss_bytes:process.memoryUsage().rss});}
const plan=[{p:1009,Ns:[4,16,64,256],kinds:['T1','T2'],iters:150},{p:10007,Ns:[4,16,64,256],kinds:['T1','T2'],iters:125},{p:100003,Ns:[4,16,64,256],kinds:['T1','T2'],iters:100},{p:1000003,Ns:[4,16,64,256],kinds:['T2'],iters:100},{p:1999993,Ns:[4,16,64,256],kinds:['T2'],iters:100}];
for(const item of plan){if(!prime(item.p))throw Error('grid prime');const O=new Ops(item.p);for(const kind of item.kinds)for(const N of item.Ns){let before=cpu(),rec=power(O.op(kind,N),item.p+1,item.iters,12345);emit({p:item.p,kind,N,...rec,free_T1_comparator:2*Math.sqrt(N-1)/N,free_T1_difference:rec.sigma_lower_estimate-2*Math.sqrt(N-1)/N,cpu_seconds:cpu()-before,cpu_total:cpu(),rss_bytes:process.memoryUsage().rss,upper_bound_status:'no certified spectral upper bound'});if(process.memoryUsage().rss>1500*1024**2)throw Error('memory guard');}}
emit({complete:true,cpu_seconds:cpu(),wall_seconds:(Date.now()-wall0)/1000,rss_bytes:process.memoryUsage().rss});
}
module.exports={Ops,power,dense,cpu};
if(require.main===module)run();
