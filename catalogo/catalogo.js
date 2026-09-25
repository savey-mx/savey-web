/* Savey · Catálogo por categoría
   Sin dependencias obligatorias: si Motion carga, las entradas
   son más finas; si no, todo se revela igual con CSS. */
(function(){
"use strict";
var $=function(s,c){return (c||document).querySelector(s)};
var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var M=window.Motion&&window.Motion.animate?window.Motion:null;
var quieto=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var fino=window.matchMedia("(hover: hover) and (pointer: fine)").matches;
var SUAVE=[.2,.7,.3,1];

/* ── Barra que se marca al bajar ── */
var barra=$("#barra");
function pegar(){ if(barra) barra.classList.toggle("pegada", window.scrollY>6) }
pegar(); window.addEventListener("scroll",pegar,{passive:true});

/* ── Hilo de progreso ── */
var hilo=$("#hilo i");
function progreso(){
  if(!hilo) return;
  var h=document.documentElement.scrollHeight-window.innerHeight;
  hilo.style.width=(h>0?Math.min(100,(window.scrollY/h)*100):0)+"%";
}
progreso();
window.addEventListener("scroll",progreso,{passive:true});
window.addEventListener("resize",progreso);

/* ── Revelado al entrar en pantalla ── */
var porRevelar=$$(".revelar");
if("IntersectionObserver" in window && porRevelar.length){
  var ob=new IntersectionObserver(function(ent){
    ent.forEach(function(e){
      if(!e.isIntersecting) return;
      e.target.classList.add("visto");
      ob.unobserve(e.target);
    });
  },{rootMargin:"0px 0px -8% 0px",threshold:.08});
  porRevelar.forEach(function(el){ob.observe(el)});
}else{
  porRevelar.forEach(function(el){el.classList.add("visto")});
}

/* ── Entrada en cascada de la rejilla ── */
var rejilla=$("#rejilla");
if(rejilla && M && !quieto && "IntersectionObserver" in window){
  var tarjetas=$$(".muestra",rejilla);
  tarjetas.forEach(function(t){t.style.opacity=0});
  var ob2=new IntersectionObserver(function(ent,o){
    if(!ent[0].isIntersecting) return;
    o.disconnect();
    M.animate(tarjetas,{opacity:[0,1],y:[26,0]},
      {duration:.7,delay:M.stagger(.055),ease:[.16,1,.3,1]});
  },{threshold:.06});
  ob2.observe(rejilla);
}

/* ── Inclinación y reflejo que siguen al cursor ── */
function inclinar(caja,plano,grados){
  if(!plano) return;
  var dentro=false;
  caja.addEventListener("pointermove",function(e){
    if(e.pointerType!=="mouse") return;
    var r=caja.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width, y=(e.clientY-r.top)/r.height;
    plano.style.setProperty("--ry",((x-.5)*grados).toFixed(2)+"deg");
    plano.style.setProperty("--rx",((.5-y)*grados).toFixed(2)+"deg");
    plano.style.setProperty("--gx",(x*100).toFixed(1)+"%");
    plano.style.setProperty("--gy",(y*100).toFixed(1)+"%");
    dentro=true;
  });
  caja.addEventListener("pointerleave",function(){
    if(!dentro) return;
    plano.style.setProperty("--ry","0deg");
    plano.style.setProperty("--rx","0deg");
    dentro=false;
  });
}
if(fino&&!quieto){
  $$(".muestra").forEach(function(m){ inclinar(m,$(".pantalla",m),8) });
}

/* ── Entrada del encabezado ── */
if(M&&!quieto){
  var cab=[$(".miga"),$(".titulo"),$(".entrada"),$(".marcas"),$(".encabezado .acciones")].filter(Boolean);
  if(cab.length){
    M.animate(cab,{opacity:[0,1],y:[16,0]},
      {duration:.85,delay:M.stagger(.075,{startDelay:.06}),ease:[.16,1,.3,1]});
  }
}
})();
