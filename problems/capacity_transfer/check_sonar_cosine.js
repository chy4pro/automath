'use strict';
// Exact BigInt rational checks for SONAR_COSINE.md and KERNEL_FUNCTIONAL.md.
// No solver, dependency, or floating-point transcendental evaluation.
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
  add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
  neg(){return new Q(-this.n,this.d);}
  sub(b){return this.add(b.neg());}
  mul(b){return new Q(this.n*b.n,this.d*b.d);}
  div(b){return new Q(this.n*b.d,this.d*b.n);}
  pow(n){return new Q(this.n**BigInt(n),this.d**BigInt(n));}
  cmp(b){const v=this.n*b.d-b.n*this.d;return v<0n?-1:v>0n?1:0;}
  str(){return this.n+'/'+this.d;}
}
const q=(n,d=1)=>new Q(n,d), Z=q(0), ONE=q(1);
let count=0;
function check(test,label){count++;if(!test)throw Error(label);}
function atanInverseBounds(d,terms){let s=Z;for(let j=0;j<terms;j++){const t=q(1,BigInt(2*j+1)*BigInt(d)**BigInt(2*j+1));s=j%2?s.sub(t):s.add(t);}const r=q(1,BigInt(2*terms+1)*BigInt(d)**BigInt(2*terms+1));return terms%2?[s.sub(r),s]:[s,s.add(r)];}
// Machin's identity: pi=16 atan(1/5)-4 atan(1/239).
const [l5,u5]=atanInverseBounds(5,24),[l239,u239]=atanInverseBounds(239,8);
const piLo=q(16).mul(l5).sub(q(4).mul(u239));
const piHi=q(16).mul(u5).sub(q(4).mul(l239));
check(piLo.cmp(q(3))>0,'pi lower bracket');
check(piHi.cmp(q(22,7))<0,'pi upper bracket');
check(piHi.pow(2).cmp(q(32,3))<0,'cosine coefficient strictly below 2');
check(q(3,5).pow(3).cmp(piLo.pow(2).div(q(36)))<0,'v>3/5');
check(piHi.pow(2).div(q(36)).cmp(q(2,3).pow(3))<0,'v<2/3');
const x=q(160), vHi=q(2,3), vLo=q(3,5), dHi=q(17,8).mul(vHi.pow(2));
check(dHi.cmp(q(17,18))===0,'d upper bound');
const margin=q(4).sub(q(41,8).mul(vHi.pow(2))).sub(q(8).div(q(9).mul(vLo)));
check(margin.cmp(q(13,54))===0,'coefficient margin');
check(q(4).mul(vHi).add(q(3).mul(vHi).mul(dHi)).add(q(26,9)).cmp(q(67,9))===0,'constant bound');
check(q(4).mul(dHi).div(x).cmp(ONE)<0,'inverse-x constant');
const eps=q(1).div(x.pow(4));
const uHi=vHi.div(x).add(dHi.add(q(2,3).mul(eps)).div(x.pow(2)));
check(uHi.cmp(q(1,2))<0,'positive denominator for x>=160');
const epsLoss=q(1).div(x.pow(2)).add(q(2,3).div(x.pow(3))).add(q(8,3).div(x.pow(4))).add(q(8,3).div(x.pow(5)));
check(epsLoss.cmp(ONE)<0,'tail loss for x>=160');
check(q(13,54).mul(x).sub(q(85,9)).cmp(Z)>0,'uniform final margin');
check(200n*160n**4n<2n**40n,'uniform exponential endpoint');
const e=q(-1,5), halfLag=q(1,2).add(q(2).mul(e)).sub(q(4).mul(e.pow(2)));
check(halfLag.cmp(q(-3,50))===0,'signed-factor negative autocorrelation');
const J=q(1).sub(q(2).mul(e)).add(q(10).mul(e.pow(2))).mul(q(1).add(q(2).mul(e)).sub(q(2).mul(e.pow(2))));
check(J.cmp(q(117,125))===0,'inadmissible candidate functional');
check(q(1,4).add(q(1,18).div(piLo.pow(2))).cmp(piLo.pow(2).div(q(32)))<0,'full-class bounds do not close');
console.log(JSON.stringify({result:'PASS',exactRationalChecks:count,scope:'Certified coefficient envelopes, uniform endpoint inequalities, and rejected signed-factor candidate. Analytic identities and positivity proofs are in the notes.'},null,2));
