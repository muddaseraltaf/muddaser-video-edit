/* Load after GSAP. Helpers only animate untimed visual wrappers. */
(function (scope) {
  function handoff(tl, out, incoming, t, width=1080) {
    tl.to(out, {scale:.84,borderRadius:28,duration:.38,ease:'power2.inOut'},t);
    tl.to(out, {x:-width*1.0926,duration:.76,ease:'power2.inOut'},t+.38);
    tl.set(out, {autoAlpha:0},t+1.14);
    tl.set(incoming, {x:-width*1.0926,scale:.84,borderRadius:28,autoAlpha:1},t+.18);
    tl.to(incoming, {x:0,duration:.9,ease:'power2.inOut'},t+.18);
    tl.to(incoming, {scale:1,borderRadius:0,duration:.5,ease:'power2.inOut'},t+1.08);
  }
  function phrase(tl, outer, ink, line, a, b) {
    if (b-a<1.3) throw new Error('Give the phrase at least 1.3s or use a shorter custom reveal');
    tl.set(outer,{autoAlpha:1},a);
    tl.fromTo(ink,{y:135,opacity:.4},{y:0,opacity:1,duration:.58,ease:'power2.inOut'},a);
    if(line)tl.fromTo(line,{scaleX:0},{scaleX:1,duration:.5,ease:'power2.inOut'},a+.35);
    tl.to(ink,{y:-135,duration:.45,ease:'power2.inOut'},b-.45);
    if(line)tl.to(line,{scaleX:0,duration:.35,ease:'power2.inOut'},b-.35);
    tl.set(outer,{autoAlpha:0},b);
  }
  function highlight(tl, target, t, duration=.4) {
    tl.fromTo(target,{scaleX:0},{scaleX:1,duration,ease:'power2.inOut'},t);
  }
  function arc(tl,target,t,from,control,to,duration=1.25) {
    const keys=[];
    for(let i=0;i<=24;i++){
      const u=i/24,p=u*u*(3-2*u),q=1-p;
      keys.push({x:q*q*from.x+2*q*p*control.x+p*p*to.x,y:q*q*from.y+2*q*p*control.y+p*p*to.y,duration:i===0?0:duration/24,ease:'none'});
    }
    tl.to(target,{keyframes:keys,ease:'none'},t);
  }
  scope.MuddaserMotion={handoff,phrase,highlight,arc};
})(typeof window!=='undefined'?window:globalThis);
