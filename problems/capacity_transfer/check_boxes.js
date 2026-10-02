#!/usr/bin/env node
'use strict';
// Exact finite audit for BOXES.md. No package dependencies or floating-point
// inequality decisions. The all-N theorem is the written proof, not a scan.
const assert=require('node:assert/strict');
const abs=n=>n<0n?-n:n;
function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a;}
class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n);if(d<0n){n=-n;d=-d;}
    const g=gcd(n,d);this.n=n/g;this.d=d/g;}
  add(b){b=q(b);return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
  sub(b){b=q(b);return new Q(this.n*b.d-b.n*this.d,this.d*b.d);}
  mul(b){b=q(b);return new Q(this.n*b.n,this.d*b.d);}
  div(b){b=q(b);return new Q(this.n*b.d,this.d*b.n);}
  pow(n){let v=q(1);for(let i=0;i<n;i++)v=v.mul(this);return v;}
  cmp(b){b=q(b);const v=this.n*b.d-b.n*this.d;return v<0n?-1:v>0n?1:0;}
  abs(){return new Q(abs(this.n),this.d);}
}
const q=(n,d)=>n instanceof Q?n:new Q(n,d);
function eq(a,b,msg){assert.equal(q(a).cmp(b),0,msg);}
function le(a,b,msg){assert(q(a).cmp(b)<=0,msg);}
const a=q(4,3);
function f(t){t=q(t).abs();return t.cmp(1)>0?q(0):a.sub(t.mul(2)).add(t.pow(3).mul(q(2,3)));}

// Integer bivariate polynomial arithmetic: variables T and theta.
const constant=n=>new Map(n===0n?[]:[['0,0',n]]);
const varT=new Map([['1,0',1n]]),varH=new Map([['0,1',1n]]);
function add(A,B){const C=new Map(A);for(const[k,v]of B){const w=(C.get(k)||0n)+v;if(w)C.set(k,w);else C.delete(k);}return C;}
function scale(A,c){return new Map([...A].map(([k,v])=>[k,v*c]).filter(([,v])=>v));}
function sub(A,B){return add(A,scale(B,-1n));}
function mul(A,B){let C=constant(0n);for(const[ka,va]of A)for(const[kb,vb]of B){
  const ia=ka.split(',').map(Number),ib=kb.split(',').map(Number);
  C=add(C,new Map([[`${ia[0]+ib[0]},${ia[1]+ib[1]}`,va*vb]]));}return C;}
function pow(A,n){let C=constant(1n);for(let i=0;i<n;i++)C=mul(C,A);return C;}
const one=constant(1n),npoly=sub(varT,varH),nn=mul(npoly,add(npoly,one));
const lhs=add(add(scale(pow(varT,3),4n),scale(mul(npoly,pow(varT,3)),8n)),
  add(scale(mul(nn,pow(varT,2)),-6n),pow(nn,2)));
const hh=mul(varH,sub(one,varH));
const rhs=add(add(scale(pow(varT,4),3n),pow(varT,2)),
  add(scale(mul(mul(hh,sub(one,scale(varH,2n))),varT),-2n),pow(hh,2)));
assert.equal(sub(lhs,rhs).size,0,'symbolic identity (B3), multiplied by 3T^3');

function lattice(T){
  const n=T.n/T.d,theta=T.sub(q(n));let S=a;
  for(let j=1n;j<=n;j++)S=S.add(f(q(j).div(T)).mul(2));
  const formula=T.add(q(1).div(T.mul(3)))
    .sub(theta.mul(q(1).sub(theta)).mul(q(1).sub(theta.mul(2))).mul(2).div(T.pow(2).mul(3)))
    .add(theta.pow(2).mul(q(1).sub(theta).pow(2)).div(T.pow(3).mul(3)));
  eq(S,formula,'rational lattice formula');
  le(S,T.add(q(1).div(T.mul(2))),'sharp lattice bound');
  return S;
}
let latticeChecks=0;
for(let den=1;den<=8;den++)for(let num=den;num<=40;num++){lattice(q(num,den));latticeChecks++;}
assert(24000n*32n<2n**20n);
eq(q(1,3).add(q(1,12)).add(q(1,48)),q(7,16));
le(q(7,16),q(1,2));
eq(q(3,64).add(q(1,2)).add(q(5,32)),q(45,64));
le(q(5,16),q(1,3));
// 2d^2 minus the accumulated remainder is (40d^2-48d-9)/32.
assert.equal(40n*2n**2n-48n*2n-9n,55n);
// Its numerator increment from d to d+1 is 80d-8, positive for d>=2.
assert(80n*2n-8n>0n);
let marginChecks=0;
for(const d of [...Array.from({length:19},(_,i)=>i+2),50,100]){
  const Qmax=q(1,Math.max(120,4*d));
  const w=Qmax.add(Qmax.pow(2).mul(q(3,64))),z=Qmax.pow(2).div(2);
  const v=w.add(z).add(w.mul(z));
  le(v,Qmax.add(Qmax.pow(2)));le(w.mul(d),q(1,3));le(v.mul(d),q(1,3));
  le(q(1).add(w).pow(d),q(3,2));
  le(q(1).add(w).pow(d).sub(1),Qmax.mul(2*d));
  le(q(3,4).mul(d*d).add(q(3,2).mul(d)).add(q(9,32)),q(2*d*d));
  marginChecks++;
}
const key=v=>v.join(',');
function sidonSums(P){const seen=new Set();for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
  const k=key(P[i].map((v,h)=>v+P[j][h]));if(seen.has(k))return false;seen.add(k);}return true;}
function orderedDifferences(P){const seen=new Set();for(let i=0;i<P.length;i++)for(let j=0;j<P.length;j++)if(i!==j){
  const k=key(P[i].map((v,h)=>v-P[j][h]));if(seen.has(k))return false;seen.add(k);}return true;}
function grid(N,d){if(!d)return[[]];return grid(N,d-1).flatMap(p=>Array.from({length:N},(_,i)=>[...p,i]));}
const scales=[q(1),q(3,2),q(2),q(5,2),q(4)],sums=scales.map(lattice);
let subsets=0,sidonSets=0,energyChecks=0;
const dimensions=[];
for(const [N,d]of [[3,2],[2,3]]){
  const P=grid(N,d);let local=0;
  const ap=[Array(d).fill(0),[1,...Array(d-1).fill(0)],[2,...Array(d-1).fill(0)]];
  assert(!sidonSums(ap));assert(!orderedDifferences(ap));
  for(let mask=0;mask<(1<<P.length);mask++){
    const A=P.filter((_,i)=>(mask&(1<<i))!==0);subsets++;
    const ok=sidonSums(A);assert.equal(ok,orderedDifferences(A));if(!ok)continue;
    sidonSets++;local++;
    for(let ti=0;ti<scales.length;ti++){
      const T=scales[ti];let E=q(0);
      for(const p of A)for(const r of A){let term=q(1);
        for(let h=0;h<d;h++)term=term.mul(f(q(p[h]-r[h]).div(T)));E=E.add(term);}
      le(E,a.pow(d).mul(A.length).add(sums[ti].pow(d)).sub(a.pow(d)),'product-lattice energy bound');
      le(E,a.pow(d).mul(A.length).add(T.add(q(1).div(T.mul(2))).pow(d)).sub(a.pow(d)),
         'sharpened product-energy upper bound');energyChecks++;
    }
  }dimensions.push({N,d,sidonSets:local});
}
console.log(JSON.stringify({status:'PASS',arithmetic:'BigInt rational and exact integer polynomials',
  symbolicLatticeIdentity:true,latticeChecks,marginChecks,subsets,sidonSets,energyChecks,dimensions,
  scope:'finite model/energy checks and exact proof margins; analytic capacity is proved in text'},null,2));
