#!/usr/bin/env node
'use strict';
// Exact finite audit for MANHATTAN.md. No package dependencies or floating-point
// inequality decisions. This supplements, and does not replace, the proof.
const assert = require('node:assert/strict');
const abs = n => n < 0n ? -n : n;
function gcd(a, b) { a = abs(a); b = abs(b); while (b) [a,b] = [b,a%b]; return a; }
class Q {
  constructor(n, d=1n) {
    n=BigInt(n); d=BigInt(d); assert(d!==0n);
    if(d<0n){n=-n;d=-d;} const g=gcd(n,d); this.n=n/g;this.d=d/g;
  }
  add(b){b=q(b);return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
  sub(b){b=q(b);return new Q(this.n*b.d-b.n*this.d,this.d*b.d);}
  mul(b){b=q(b);return new Q(this.n*b.n,this.d*b.d);}
  div(b){b=q(b);return new Q(this.n*b.d,this.d*b.n);}
  pow(n){let v=q(1);for(let i=0;i<n;i++)v=v.mul(this);return v;}
  cmp(b){b=q(b);const v=this.n*b.d-b.n*this.d;return v<0n?-1:v>0n?1:0;}
  abs(){return new Q(abs(this.n),this.d);}
  toString(){return `${this.n}/${this.d}`;}
}
const q=(n,d)=>n instanceof Q?n:new Q(n,d);
function eq(a,b,msg){assert.equal(q(a).cmp(b),0,msg);}
function le(a,b,msg){assert(q(a).cmp(b)<=0,msg);}
const a=q(4,3), b=q(2,3), c3=q(4,3);
function f(t){t=q(t).abs();return t.cmp(1)>0?q(0):a.sub(t.mul(2)).add(t.pow(3).mul(q(2,3)));}

// Uniform real-variable proof margins and optimized radical identities.
assert(32000n*32n < 2n**20n);
eq(b.add(a.pow(2).div(c3.mul(4))),1,'coefficient divided by c');
eq(q(27,16).mul(a.mul(b).pow(2)),c3,'cubed optimized coefficient');
eq(q(1).sub(a.pow(2).div(c3.mul(2)))
  .sub(a.pow(2).mul(b).div(c3)).sub(b.pow(2)),-1,'negative x^4 coefficient');
const remainder=q(1,24).add(q(16,9)).add(2).add(q(13,720)).add(q(128,27));
eq(remainder,q(18529,2160)); assert(remainder.cmp(9)<0);

function lattice(T){
  const lim=Number((T.n+T.d-1n)/T.d);
  let even=q(0),odd=q(0),direct=q(0);
  for(let j=-lim;j<=lim;j++) {
    const v=f(q(j).div(T));
    if(j%2===0) even=even.add(v); else odd=odd.add(v);
  }
  for(let u=-lim;u<=lim;u++)for(let v=-lim;v<=lim;v++)
    if((u-v)%2===0)direct=direct.add(f(q(u).div(T)).mul(f(q(v).div(T))));
  eq(direct,even.pow(2).add(odd.pow(2)),'index-2 lattice identity');
  le(even,T.div(2).add(a),'even sum');le(odd,T.div(2).add(a),'odd sum');
  le(direct.sub(a.pow(2)),T.pow(2).div(2).add(a.mul(T).mul(2)).add(a.pow(2)),
     'complete off-diagonal lattice bound');
  return {even,odd,direct};
}
let latticeChecks=0;
for(let den=1;den<=4;den++)for(let num=1;num<=18;num++){
  lattice(q(num,den));latticeChecks++;
}
const key=v=>v.join(',');
function sidonSums(P){
  const seen=new Set();
  for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
    const k=key(P[i].map((v,h)=>v+P[j][h]));
    if(seen.has(k))return false;seen.add(k);
  }return true;
}
function orderedDifferences(P){
  const seen=new Set();
  for(let i=0;i<P.length;i++)for(let j=0;j<P.length;j++)if(i!==j){
    const k=key(P[i].map((v,h)=>v-P[j][h]));
    if(seen.has(k))return false;seen.add(k);
  }return true;
}
const transform=([x,y])=>[x+y,x-y];
const grid=[];for(let x=0;x<4;x++)for(let y=0;y<3;y++)grid.push([x,y]);
for(const p of grid)for(const r of grid){
  const u=transform(p),v=transform(r);
  assert.equal(Math.abs(p[0]-r[0])+Math.abs(p[1]-r[1]),
    Math.max(Math.abs(u[0]-v[0]),Math.abs(u[1]-v[1])));
  assert(((u[0]-v[0])-(u[1]-v[1]))%2===0);
}
assert(!sidonSums([[0,0],[1,0],[2,0]]),'diagonal-sum negative control');
assert(!orderedDifferences([[0,0],[1,0],[2,0]]));
const scales=[q(1,2),q(1),q(3,2),q(2),q(3)];
const ls=scales.map(lattice);
let subsets=0,ddcs=0,energies=0;
for(let mask=0;mask<(1<<grid.length);mask++){
  const P=grid.filter((_,i)=>(mask&(1<<i))!==0);subsets++;
  const isS=sidonSums(P);assert.equal(isS,orderedDifferences(P));if(!isS)continue;
  ddcs++;const V=P.map(transform);assert(orderedDifferences(V));
  if(P.length){
    let diameter=0;for(const p of P)for(const r of P)
      diameter=Math.max(diameter,Math.abs(p[0]-r[0])+Math.abs(p[1]-r[1]));
    for(let h=0;h<2;h++)assert(Math.max(...V.map(v=>v[h]))-Math.min(...V.map(v=>v[h]))<=diameter);
  }
  for(let ti=0;ti<scales.length;ti++){
    const T=scales[ti];let E=q(0);
    for(const p of V)for(const r of V)
      E=E.add(f(q(p[0]-r[0]).div(T)).mul(f(q(p[1]-r[1]).div(T))));
    le(E,a.pow(2).mul(P.length).add(ls[ti].direct).sub(a.pow(2)),'DDC energy bound');
    le(E,a.pow(2).mul(P.length).add(T.pow(2).div(2)).add(a.mul(T).mul(2)).add(a.pow(2)),
       'scout (M) upper-energy factor');energies++;
  }
}
console.log(JSON.stringify({status:'PASS',arithmetic:'BigInt rational',latticeChecks,
  subsets,ddcs,energyChecks:energies,
  scope:'finite model/energy checks and exact proof margins; analytic capacity is proved in text'},null,2));
