'use strict';
// Dependency-free exact finite checks for BOXES_ALL_N.md.
// Small Number indices are exact integers; all certificate arithmetic is BigInt.
const assert=(ok,label)=>{if(!ok)throw new Error(label);};
const key=v=>v[0]+','+v[1];
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const sub=(a,b)=>[a[0]-b[0],a[1]-b[1]];
function strongSidon(A){
  const sums=new Set();
  for(let i=0;i<A.length;i++)for(let j=i;j<A.length;j++){
    const s=key(add(A[i],A[j]));
    if(sums.has(s))return false;
    sums.add(s);
  }
  return true;
}
function uniqueDifferences(A){
  const seen=new Set();
  for(let i=0;i<A.length;i++)for(let j=0;j<A.length;j++)if(i!==j){
    const d=key(sub(A[i],A[j]));
    if(seen.has(d))return false;
    seen.add(d);
  }
  return true;
}
function weight(v,T){
  return BigInt(Math.max(T-Math.abs(v[0]),0))*BigInt(Math.max(T-Math.abs(v[1]),0));
}
function occupancy(A,T){
  const counts=new Map();
  for(const a of A)for(let u=0;u<T;u++)for(let v=0;v<T;v++){
    const z=key([a[0]+u,a[1]+v]);counts.set(z,(counts.get(z)||0n)+1n);
  }
  return counts;
}
function trim(a){
  while(a.length>1&&a[a.length-1]===0n)a.pop();return a;
}
function pa(a,b){
  const c=Array(Math.max(a.length,b.length)).fill(0n);
  for(let i=0;i<c.length;i++)c[i]=(a[i]||0n)+(b[i]||0n);return trim(c);
}
function pm(a,b){
  const c=Array(a.length+b.length-1).fill(0n);
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];
  return trim(c);
}
function peq(a,b,label){
  a=trim(a);b=trim(b);
  assert(a.length===b.length&&a.every((x,i)=>x===b[i]),label);
}
// Expansion of 8x^3 times the first line of (A7).
const xp1=[1n,1n],xp1sq=pm(xp1,xp1),xp1four=pm(xp1sq,xp1sq);
const expansion=pa(pa(pm([0n,0n,0n,8n],[0n,0n,1n,1n]),
                         pm([0n,0n,0n,4n],xp1sq)),xp1four);
peq(expansion,[1n,4n,6n,8n,9n,12n,8n],'A7 exact polynomial expansion');
peq(pm([-1n,1n],[1n,5n,11n,19n]),[-1n,-4n,-6n,-8n,19n],'A8 factorization');
assert(83n**3n===571787n,'83 cube');
assert(8n*60n**3n/3n===576000n,'comparison cube');
assert(3n*83n**3n<8n*60n**3n,'c>83/60');
assert(90n-83n===7n,'3/2-83/60=7/60');
assert(7n*120n===14n*60n,'splice coefficient 14');
assert(2n*14n+7n===35n&&35n<2n*18n,'35/2<18');
assert(3n*27n*64n===8n*8n*81n,'d=2 capacity coefficient has cube 8/3');
assert(8n<=18n,'large-parameter remainder fits');
assert(120n**3n===1728000n,'exact splice onset');
function ceilTwoThirds(N){
  assert(N>=1n,'positive N');
  let lo=0n,hi=N,target=N*N;
  while(hi-lo>1n){
    const mid=(lo+hi)/2n;
    if(mid**3n>=target)hi=mid;else lo=mid;
  }
  return hi;
}
let ceilingChecks=0;
const ceilingInputs=[];
for(let n=1n;n<=1000n;n++)ceilingInputs.push(n);
ceilingInputs.push(1727999n,1728000n,1728001n,1000000000000000000n);
for(const N of ceilingInputs){
  const T=ceilTwoThirds(N),M=N+T-1n;
  assert((T-1n)**3n<N*N&&N*N<=T**3n,'exact ceiling N^(2/3)');
  assert(M>=N,'M>=N');
  assert((M-N)**3n<=N*N,'M<=N+N^(2/3)');
  ceilingChecks++;
}
assert(!strongSidon([[0,0],[1,0],[2,0]]),'diagonal sum negative control');
assert(!uniqueDifferences([[0,0],[1,0],[2,0]]),'repeated vector negative control');
assert(strongSidon([[0,0],[0,1]]),'zero coordinate is permitted');
let subsets=0,sidonSubsets=0,energyIdentities=0,sidonEnergyBounds=0;
for(let T=1;T<=6;T++){
  let lattice=0n;
  for(let u=1-T;u<T;u++)for(let v=1-T;v<T;v++)lattice+=weight([u,v],T);
  assert(lattice===BigInt(T)**4n,'full vector budget T^4');
  assert(lattice-weight([0,0],T)===BigInt(T)**4n-BigInt(T)**2n,'nonzero budget T^4-T^2');
}
for(let N=1;N<=3;N++){
  const grid=[];
  for(let u=0;u<N;u++)for(let v=0;v<N;v++)grid.push([u,v]);
  for(let mask=0;mask<(1<<grid.length);mask++){
    const A=grid.filter((_,i)=>mask&(1<<i));subsets++;
    const sidon=strongSidon(A);
    assert(sidon===uniqueDifferences(A),'sum/difference equivalence');
    if(sidon)sidonSubsets++;
    for(let T=1;T<=6;T++){
      const counts=occupancy(A,T),M=N+T-1,K=BigInt(A.length),TT=BigInt(T);
      let mass=0n,E=0n;
      for(const[z,r]of counts){
        const uv=z.split(',').map(Number);
        assert(uv.every(t=>0<=t&&t<M),'support fits M by M');
        mass+=r;E+=r*r;
      }
      assert(mass===K*TT**2n,'occupancy mass k T^2');
      let pairEnergy=0n;
      for(const a of A)for(const b of A)pairEnergy+=weight(sub(a,b),T);
      assert(E===pairEnergy,'window intersection energy identity');
      assert(mass*mass<=BigInt(M)**2n*E,'finite occupancy Cauchy-Schwarz');
      energyIdentities++;
      if(sidon){
        assert(E<=TT**4n+(K-1n)*TT**2n,'Sidon energy budget with exact diagonal');
        assert(K*K*TT**2n<=BigInt(M)**2n*(TT**2n+K-1n),'A5 scalar inequality');
        sidonEnergyBounds++;
      }
    }
  }
}
console.log(JSON.stringify({status:'PASS',arithmetic:'exact BigInt and integer indices',
  gridSideMax:3,windowSideMax:6,subsets,sidonSubsets,energyIdentities,
  sidonEnergyBounds,ceilingChecks,polynomialIdentities:2,
  scope:'finite verification plus exact rational splice; analytic input remains BOXES.md'}));
