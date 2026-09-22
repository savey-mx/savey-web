/* ═══════════════════════════════════════════════════════════
   SAVEY · Motor de las invitaciones de XV
   Pantalla de carga, apariciones al hacer scroll, parallax,
   cuenta regresiva, pases por familia y confirmación.
   Cada invitación define window.XV antes de cargar este archivo.
   Librerías (opcionales, si no cargan todo sigue funcionando):
   GSAP + ScrollTrigger (parallax) y Lenis (scroll suave).
   ═══════════════════════════════════════════════════════════ */
(function(){
"use strict";
var C = window.XV || {};
var d = document, B = d.body, H = d.documentElement;
var $ = function(s,c){ return (c||d).querySelector(s) };
var $$ = function(s,c){ return Array.prototype.slice.call((c||d).querySelectorAll(s)) };
var quieto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var fino = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
var esc = function(s){ return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]}) };
var G = window.gsap, ST = window.ScrollTrigger;
if(G && ST) G.registerPlugin(ST);

/* ── Letras separadas para animarlas una por una ── */
$$('[data-letras]').forEach(function(el){
  var n = 0;
  el.innerHTML = el.textContent.split(/(\s+)/).map(function(p){
    if(/^\s+$/.test(p)) return ' ';
    return '<span class="palabra">'+p.split('').map(function(ch){
      return '<span class="l" style="--i:'+(n++)+'">'+esc(ch)+'</span>';
    }).join('')+'</span>';
  }).join('');
  el.setAttribute('aria-label', el.textContent);
});

/* ══════════ Pantalla de carga ══════════ */
var carga = $('#carga'), progreso = 0;
function avanza(v){
  progreso = Math.max(progreso, v);
  if(carga) carga.style.setProperty('--progreso', progreso.toFixed(3));
}
function abrir(){
  if(B.classList.contains('abierto')) return;
  avanza(1);
  setTimeout(function(){
    B.classList.add('abierto');
    B.classList.remove('cargando');
    try{ sessionStorage.setItem('xv-visto-'+(C.slug||''),'1') }catch(e){}
    if(typeof C.alAbrir === 'function') C.alAbrir(G);
    setTimeout(function(){ if(carga) carga.remove(); if(ST) ST.refresh() }, 1800);
  }, quieto ? 0 : 380);
}
(function(){
  var yaVisto = false;
  try{ yaVisto = !!sessionStorage.getItem('xv-visto-'+(C.slug||'')) }catch(e){}
  var minimo = quieto ? 0 : (yaVisto ? 500 : (C.cargaMinima || 1700));
  var inicio = Date.now(), listos = 0, total = 2;
  var uno = function(){ listos++; avanza(.25 + .7*listos/total); if(listos>=total) termina() };
  var termina = function(){ setTimeout(abrir, Math.max(0, minimo-(Date.now()-inicio))) };
  // progreso de cortesía mientras llegan las piezas
  var t0 = setInterval(function(){ if(progreso<.85) avanza(progreso+.04); else clearInterval(t0) }, 140);
  var img = $('[data-portada] img');
  if(img && !img.complete){ img.addEventListener('load',uno); img.addEventListener('error',uno) } else uno();
  if(d.fonts && d.fonts.ready) d.fonts.ready.then(uno); else uno();
  setTimeout(abrir, 5000);   // nunca más de 5 segundos
})();

/* ══════════ Scroll suave ══════════ */
var lenis = null;
if(window.Lenis && !quieto && fino){
  lenis = new window.Lenis({ duration: 1.15, smoothWheel: true });
  if(G && ST){
    lenis.on('scroll', ST.update);
    G.ticker.add(function(t){ lenis.raf(t*1000) });
    G.ticker.lagSmoothing(0);
  } else {
    (function raf(t){ lenis.raf(t); requestAnimationFrame(raf) })(0);
  }
}
$$('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var id = a.getAttribute('href'); if(id.length<2) return;
    var destino = $(id); if(!destino) return;
    e.preventDefault();
    if(lenis) lenis.scrollTo(destino, {offset:-10});
    else destino.scrollIntoView({behavior: quieto?'auto':'smooth'});
  });
});

/* ══════════ Apariciones ══════════ */
function mostrar(el){ el.classList.add('visto') }
if('IntersectionObserver' in window && !quieto){
  // lo que empieza recortado (máscaras) no "se ve" para el observador:
  // lo vigilamos a través de su contenedor
  var destinos = new Map();
  var ojo = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      var el = destinos.get(e.target) || e.target;
      // hermanos dentro de un grupo entran en cascada
      var g = el.closest('[data-grupo]');
      if(g && !el.style.getPropertyValue('--d')){
        var hs = $$('[data-a]', g), paso = +(g.getAttribute('data-grupo')||110);
        el.style.setProperty('--d', (hs.indexOf(el)*paso)+'ms');
      }
      mostrar(el); ojo.unobserve(e.target);
    });
  }, {rootMargin:'0px 0px -10% 0px', threshold:0});
  $$('[data-a],[data-letras]').forEach(function(el){
    var recorte = /^(mascara|telon|barre|linea|lineav)$/.test(el.getAttribute('data-a')||'');
    var vigia = recorte ? el.parentElement : el;
    if(recorte){ if(destinos.has(vigia)){ mostrarJunto(vigia, el); return } destinos.set(vigia, el) }
    ojo.observe(vigia);
  });
  function mostrarJunto(vigia, el){
    // varios recortes en el mismo contenedor
    var otro = new IntersectionObserver(function(es,o){ if(es[0].isIntersecting){ mostrar(el); o.disconnect() } },{rootMargin:'0px 0px -10% 0px'});
    otro.observe(vigia);
  }
} else {
  $$('[data-a],[data-letras]').forEach(mostrar);
}

/* ══════════ Parallax con GSAP ══════════ */
if(G && ST && !quieto){
  $$('[data-px]').forEach(function(el){
    var v = parseFloat(el.getAttribute('data-px')) || .15;
    G.fromTo(el, {yPercent:-v*50}, {yPercent:v*50, ease:'none',
      scrollTrigger:{trigger: el.closest('section,header,figure') || el, start:'top bottom', end:'bottom top', scrub:true}});
  });
  $$('[data-acerca]').forEach(function(el){
    G.fromTo(el, {scale:1}, {scale:parseFloat(el.getAttribute('data-acerca'))||1.12, ease:'none',
      scrollTrigger:{trigger: el.closest('header,section') || el, start:'top top', end:'bottom top', scrub:true}});
  });
}

/* ══════════ Cuenta regresiva ══════════ */
$$('[data-cuenta]').forEach(function(caja){
  var meta = new Date(C.fechaISO).getTime();
  var et = caja.getAttribute('data-cuenta') === 'corta'
    ? ['días','hrs','min','seg'] : ['Días','Horas','Minutos','Segundos'];
  caja.innerHTML = et.map(function(t,i){
    return '<div class="cu"><span class="cu-n" data-u="'+i+'">00</span><span class="cu-t">'+t+'</span></div>';
  }).join('<i class="cu-sep" aria-hidden="true"></i>');
  var ns = $$('.cu-n', caja);
  var pinta = function(){
    var r = Math.max(0, meta - Date.now());
    var v = [Math.floor(r/864e5), Math.floor(r/36e5)%24, Math.floor(r/6e4)%60, Math.floor(r/1e3)%60];
    ns.forEach(function(n,i){ var t = (i===0 ? String(v[i]) : ('0'+v[i]).slice(-2)); if(n.textContent!==t) n.textContent = t });
  };
  pinta(); setInterval(pinta, 1000);
});

/* ══════════ Agregar al calendario ══════════ */
$$('[data-calendario]').forEach(function(a){
  var ini = new Date(C.fechaISO), fin = new Date(ini.getTime() + 6*36e5);
  var f = function(x){ return x.toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'') };
  a.href = 'https://calendar.google.com/calendar/render?action=TEMPLATE'+
    '&text='+encodeURIComponent(C.evento||'Mis XV años')+
    '&dates='+f(ini)+'/'+f(fin)+
    '&location='+encodeURIComponent(C.lugar||'');
  a.target = '_blank'; a.rel = 'noopener';
});

/* ══════════ Copiar datos bancarios ══════════ */
$$('[data-copiar]').forEach(function(b){
  b.addEventListener('click', function(){
    var txt = b.getAttribute('data-copiar'), antes = b.innerHTML;
    var listo = function(){ b.classList.add('copiado'); b.textContent = 'Copiado';
      setTimeout(function(){ b.classList.remove('copiado'); b.innerHTML = antes }, 1800) };
    if(navigator.clipboard) navigator.clipboard.writeText(txt).then(listo, listo); else listo();
  });
});

/* ══════════ Pase por familia ══════════ */
var codigo = (new URLSearchParams(location.search).get('c')||'').toUpperCase();
var pase = (C.pases||{})[codigo] || null;
var maximo = pase ? pase.l : (C.maxSinPase || 4);
$$('[data-pase]').forEach(function(p){
  if(!pase){ p.remove(); return }
  p.innerHTML = '<span class="pase-et">'+(C.textoPase||'Esta invitación es para')+'</span>'+
    '<span class="pase-qui">'+esc(pase.n)+'</span>'+
    '<span class="pase-lug">'+(pase.l===1?'1 lugar reservado':pase.l+' lugares reservados')+'</span>';
});

/* ══════════ Confirmación ══════════ */
var caja = $('[data-rsvp]');
if(caja){
  var guardado = null;
  try{ guardado = JSON.parse(localStorage.getItem('xv-rsvp-'+C.slug+'-'+codigo)||'null') }catch(e){}
  var lugares = maximo;
  caja.innerHTML =
    '<form class="rsvp-form" novalidate>'+
      '<label class="campo-l"><span>Nombre'+(pase?'':' completo')+'</span>'+
        '<input class="linea-in" name="nombre" autocomplete="name" required value="'+esc(pase?pase.n:'')+'"></label>'+
      '<div class="campo-l"><span>¿Asistirás?</span><div class="elige" role="radiogroup">'+
        '<label><input type="radio" name="asiste" value="si" checked><b>Sí, ahí estaré</b></label>'+
        '<label><input type="radio" name="asiste" value="no"><b>No podré ir</b></label></div></div>'+
      '<div class="campo-l" data-lugares><span>Lugares</span><div class="paso-lug">'+
        '<button type="button" data-l="-1" aria-label="Menos lugares">−</button>'+
        '<output aria-live="polite">'+lugares+'</output>'+
        '<button type="button" data-l="1" aria-label="Más lugares">+</button>'+
        '<small>'+(pase?'de '+maximo+' reservados':'')+'</small></div></div>'+
      '<label class="campo-l"><span>Un mensaje para '+esc(C.nombre||'la festejada')+' (opcional)</span>'+
        '<textarea class="linea-in" name="mensaje" rows="2"></textarea></label>'+
      '<button class="bt-p bt-lleno" type="submit">Confirmar asistencia</button>'+
      (C.fechaLimite?'<p class="rsvp-nota">Te agradecemos confirmar antes del '+C.fechaLimite+'.</p>':'')+
    '</form>'+
    '<div class="rsvp-gracias" hidden><div class="rg-sello" aria-hidden="true"></div>'+
      '<h3 class="rg-t"></h3><p class="rg-p"></p></div>';
  var form = $('form',caja), out = $('output',caja), bloque = $('[data-lugares]',caja);
  $$('[data-l]',caja).forEach(function(b){
    b.addEventListener('click',function(){
      lugares = Math.min(maximo, Math.max(1, lugares + (+b.getAttribute('data-l'))));
      out.textContent = lugares;
      out.classList.remove('late'); void out.offsetWidth; out.classList.add('late');
    });
  });
  $$('input[name=asiste]',caja).forEach(function(r){
    r.addEventListener('change',function(){ bloque.classList.toggle('apagado', r.value==='no' && r.checked) });
  });
  var gracias = function(asiste){
    form.hidden = true;
    var g = $('.rsvp-gracias',caja); g.hidden = false;
    $('.rg-t',g).textContent = asiste==='si' ? (C.graciasSi||'¡Gracias por confirmar!') : 'Gracias por avisarnos';
    $('.rg-p',g).textContent = asiste==='si' ? (C.graciasSiTexto||'Nos vemos pronto.') : (C.graciasNo||'Te vamos a extrañar.');
    requestAnimationFrame(function(){ g.classList.add('visto') });
  };
  if(guardado) gracias(guardado.asiste);
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var nombre = form.nombre.value.trim();
    if(!nombre){ form.nombre.focus(); form.nombre.closest('.campo-l').classList.add('falta'); return }
    var asiste = form.asiste.value;
    var b = $('.bt-p',form); b.disabled = true; b.textContent = 'Enviando…';
    var dato = {evento:C.evento, slug:C.slug, codigo:codigo, pase:pase?pase.n:'', nombre:nombre,
      asiste:asiste, lugares: asiste==='si'?lugares:0, mensaje:form.mensaje.value, fecha:new Date().toISOString()};
    var fin = function(){
      try{ localStorage.setItem('xv-rsvp-'+C.slug+'-'+codigo, JSON.stringify({asiste:asiste})) }catch(e){}
      gracias(asiste);
    };
    if(C.endpoint){
      fetch(C.endpoint,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain;charset=utf-8'},
        body:JSON.stringify(dato)}).then(fin)['catch'](fin);
    } else {
      window.open('https://wa.me/'+(C.wa||'')+'?text='+encodeURIComponent(
        'Confirmación '+C.evento+': '+nombre+' — '+(asiste==='si'?lugares+(lugares===1?' lugar':' lugares'):'no asistirá')),'_blank');
      fin();
    }
  });
}

/* ══════════ Botón flotante de confirmar ══════════ */
var flota = $('#flota'), portada = $('[data-portada]'), rsvp = $('#confirmar');
if(flota && portada && 'IntersectionObserver' in window){
  var enPortada = true, enRsvp = false;
  var ajusta = function(){ flota.classList.toggle('ve', !enPortada && !enRsvp) };
  new IntersectionObserver(function(es){ enPortada = es[0].isIntersecting; ajusta() },{threshold:.15}).observe(portada);
  if(rsvp) new IntersectionObserver(function(es){ enRsvp = es[0].isIntersecting; ajusta() },{threshold:.05}).observe(rsvp);
}

/* ══════════ Imágenes ampliables ══════════ */
var visor = null;
$$('[data-ampliar]').forEach(function(fig){
  fig.addEventListener('click', function(){
    var img = $('img',fig); if(!img) return;
    if(!visor){
      visor = d.createElement('div'); visor.className = 'visor';
      visor.innerHTML = '<img alt=""><button type="button" aria-label="Cerrar">×</button>';
      B.appendChild(visor);
      visor.addEventListener('click', function(){ visor.classList.remove('ve'); if(lenis) lenis.start() });
    }
    $('img',visor).src = img.currentSrc || img.src;
    requestAnimationFrame(function(){ visor.classList.add('ve') });
    if(lenis) lenis.stop();
  });
});
d.addEventListener('keydown', function(e){ if(e.key==='Escape' && visor){ visor.classList.remove('ve'); if(lenis) lenis.start() } });

/* ══════════ Brillo que sigue al cursor en botones ══════════ */
if(fino && !quieto){
  $$('.bt-p,.bt-s').forEach(function(b){
    b.addEventListener('pointermove', function(e){
      var r = b.getBoundingClientRect();
      b.style.setProperty('--bx', ((e.clientX-r.left)/r.width*100).toFixed(1)+'%');
      b.style.setProperty('--by', ((e.clientY-r.top)/r.height*100).toFixed(1)+'%');
    });
  });
}
})();
