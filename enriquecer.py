"""Enriquece las cinco invitaciones de boda: iconografía, ornamentos y secciones nuevas.
Cada plantilla recibe un tratamiento distinto a propósito."""
import json, re, io

IC = json.load(open("/home/claude/iconos.json"))

def sprite(nombres):
    return "\n".join(f'<symbol id="i-{n}" viewBox="0 0 256 256">{IC[n]}</symbol>' for n in nombres)

def leer(p): return open(p, encoding="utf-8").read()
def escribir(p, s): open(p, "w", encoding="utf-8").write(s)

# ════════════════════════════════════════════════════════════
# AURORA — botánico. Medallones circulares, padres y padrinos,
#          mesa de regalos con tiendas, playlist.
# ════════════════════════════════════════════════════════════
p = "i/boda-aurora/index.html"; s = leer(p)

s = s.replace('<symbol id="foto" viewBox="0 0 24 24"><path d="M3 5h4l1.5-2h7L17 5h4v15H3V5zm9 3a5 5 0 105 5 5 5 0 00-5-5zm0 2a3 3 0 11-3 3 3 3 0 013-3z"/></symbol>',
 sprite(["church","champagne","map-pin","gift","coat-hanger","camera","users-three","music-notes","leaf","storefront","flower-tulip"]) +
 '\n  <symbol id="rombo" viewBox="0 0 22 22"><path d="M11 1l6 10-6 10-6-10z" fill="none" stroke="currentColor" stroke-width="1.1"/><circle cx="11" cy="11" r="2.2" fill="currentColor"/></symbol>')
s = s.replace('<use href="#foto"/>', '<use href="#i-camera"/>')

s = s.replace("""/* ─────────── Movimiento ─────────── */""", """
/* ─────────── Iconografía y ornamentos ─────────── */
.ico{width:26px;height:26px;fill:var(--champagne);margin:0 auto 14px;opacity:.9}
.ornato{display:flex;align-items:center;justify-content:center;gap:14px;padding:6px 0 2px;
  opacity:.5;color:var(--champagne)}
.ornato i{display:block;width:54px;height:1px;background:currentColor}
.ornato svg{width:20px;height:20px;color:currentColor}
.guirnalda{position:absolute;top:60px;left:50%;transform:translateX(-50%);width:min(76%,310px);
  stroke:var(--marfil);fill:none;stroke-width:1;opacity:.45;z-index:1}
.sede .et{display:flex;align-items:center;gap:9px}
.sede .et svg{width:17px;height:17px;fill:var(--champagne);flex:none}
.mini{display:inline-flex;align-items:center;gap:8px}
.mini svg{width:15px;height:15px;fill:var(--champagne)}
.etiquetita{display:inline-block;margin-top:18px;padding:7px 16px;border:1px solid rgba(184,154,99,.35);
  border-radius:999px;font-size:12.5px;letter-spacing:.16em;color:var(--champagne)}

/* Familia */
.familia{padding:76px 0;border-top:1px solid rgba(184,154,99,.22);text-align:center}
.grupo{margin-top:30px}
.grupo+.grupo{margin-top:32px;padding-top:28px;border-top:1px solid rgba(184,154,99,.14)}
.grupo .et{font-size:11.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--champagne)}
.grupo .par{font-family:var(--serif);font-size:23px;line-height:1.45;margin-top:10px}
.padrinos{display:grid;grid-template-columns:1fr 1fr;gap:20px 16px;margin-top:22px;text-align:left}
.padrinos .rol{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--salvia)}
.padrinos .qui{font-family:var(--serif);font-size:19px;line-height:1.25;margin-top:2px}

/* Medallones */
.medallones{display:flex;gap:14px;justify-content:center;margin-top:30px}
.medallon{width:30%;max-width:118px;aspect-ratio:1;border-radius:50%;overflow:hidden;position:relative;
  background:var(--verde2);box-shadow:0 0 0 1px rgba(184,154,99,.4),0 0 0 7px rgba(184,154,99,.09)}
.medallon:nth-child(2){transform:translateY(-16px)}
.arco-grande{width:min(66%,232px);margin:26px auto 0;aspect-ratio:3/4;position:relative;overflow:hidden;
  border-radius:999px 999px 6px 6px;background:var(--verde2);border:1px solid rgba(184,154,99,.3)}
.medallon img,.arco-grande img{width:100%;height:100%;object-fit:cover}

/* Mesa de regalos */
.opciones{display:grid;gap:10px;margin-top:26px;text-align:left}
.opcion{display:flex;align-items:center;gap:14px;padding:17px 18px;text-decoration:none;
  border:1px solid rgba(184,154,99,.26);transition:border-color .4s var(--curva),background .4s var(--curva)}
.opcion:hover{border-color:var(--champagne);background:rgba(184,154,99,.06)}
.opcion svg{width:22px;height:22px;fill:var(--champagne);flex:none}
.opcion b{display:block;font-family:var(--serif);font-weight:400;font-size:20px;line-height:1.2}
.opcion span{font-size:13px;color:var(--salvia)}
.opcion .fl{margin-left:auto;font-size:17px;color:var(--champagne)}

/* ─────────── Movimiento ─────────── */""")

# guirnalda en la portada
s = s.replace('<div class="velo"></div>', '''<div class="velo"></div>
  <svg class="guirnalda" viewBox="0 0 320 44" aria-hidden="true">
    <path d="M8 22q76-30 152 0t152 0"/>
    <path d="M60 14c-5-7-3-15 5-19 3 8 1 16-5 19z"/><path d="M60 14c7-4 15-1 19 7-8 2-16-1-19-7z"/>
    <path d="M160 8c-5-7-3-15 5-19 3 8 1 16-5 19z"/><path d="M160 8c7-4 15-1 19 7-8 2-16-1-19-7z"/>
    <path d="M260 14c-5-7-3-15 5-19 3 8 1 16-5 19z"/><path d="M260 14c7-4 15-1 19 7-8 2-16-1-19-7z"/>
  </svg>''')

ORN = '<div class="ornato" aria-hidden="true"><i></i><svg viewBox="0 0 22 22"><use href="#rombo"/></svg><i></i></div>\n'

# sección familia, antes del itinerario
s = s.replace('<section class="itin">', ORN + '''<section class="familia">
  <div class="env">
    <svg class="ico sube"><use href="#i-users-three"/></svg>
    <div class="sube"><div class="sobretitulo">Con la bendición de</div></div>
    <div class="grupo sube">
      <div class="et">Padres de la novia</div>
      <div class="par">Sr. Fernando Ríos Guzmán<br>Sra. Marisol Montes de Ríos</div>
    </div>
    <div class="grupo sube">
      <div class="et">Padres del novio</div>
      <div class="par">Sr. Antonio Lara Vega<br>Sra. Patricia Beltrán de Lara</div>
    </div>
    <div class="grupo sube">
      <div class="et">Nuestros padrinos</div>
      <div class="padrinos">
        <div><div class="rol">Velación</div><div class="qui">Sr. y Sra. Ríos Montes</div></div>
        <div><div class="rol">Anillos</div><div class="qui">Laura y Andrés</div></div>
        <div><div class="rol">Lazo</div><div class="qui">Familia Beltrán</div></div>
        <div><div class="rol">Arras</div><div class="qui">Marisol y Javier</div></div>
      </div>
    </div>
  </div>
</section>

<section class="itin">''')

# iconos en los encabezados
s = s.replace('<div class="sube"><div class="sobretitulo">El día</div>',
              '<svg class="ico sube"><use href="#i-champagne"/></svg>\n    <div class="sube"><div class="sobretitulo">El día</div>')
s = s.replace('<div class="sube"><div class="sobretitulo">Dónde</div>',
              '<svg class="ico sube"><use href="#i-map-pin"/></svg>\n    <div class="sube"><div class="sobretitulo">Dónde</div>')
s = s.replace('<div class="sube"><div class="sobretitulo">Nosotros</div>',
              '<svg class="ico sube"><use href="#i-camera"/></svg>\n    <div class="sube"><div class="sobretitulo">Nosotros</div>')
s = s.replace('<div class="et">Ceremonia religiosa · 5:00 pm</div>',
              '<div class="et"><svg><use href="#i-church"/></svg>Ceremonia religiosa · 5:00 pm</div>')
s = s.replace('<div class="et">Recepción · 7:00 pm</div>',
              '<div class="et"><svg><use href="#i-champagne"/></svg>Recepción · 7:00 pm</div>')
s = s.replace('>Cómo llegar</a>', '><svg><use href="#i-map-pin"/></svg>Cómo llegar</a>')
s = s.replace('<div class="sobretitulo">Código de vestimenta</div>',
              '<svg class="ico"><use href="#i-coat-hanger"/></svg>\n    <div class="sobretitulo">Código de vestimenta</div>')
s = s.replace('<p>Te pedimos evitar el blanco. El jardín es de pasto, así que considera tacón cómodo o zapato plano.</p>',
              '<p>Te pedimos evitar el blanco. El jardín es de pasto, así que considera tacón cómodo o zapato plano.</p>\n    <div class="etiquetita">Paleta sugerida · verdes y tierras</div>')

# galería en medallones
s = s.replace('''<div class="tira sube">
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto horizontal</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
    </div>''', '''<div class="medallones sube">
      <div class="medallon"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="medallon"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="medallon"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
    </div>
    <div class="arco-grande sube"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto principal</span></div></div>''')

# mesa de regalos con tiendas + playlist
s = s.replace('''<div class="sobretitulo">Regalos</div>
    <h2 style="margin-top:12px">Tu compañía basta</h2>
    <p>Si además quieres tener un detalle con nosotros, agradecemos la lluvia de sobres.</p>
    <div class="cuenta-clabe">0123 4567 8901 2345<small>BBVA · Valeria Ríos Montes</small></div>''',
'''<svg class="ico"><use href="#i-gift"/></svg>
    <div class="sobretitulo">Mesa de regalos</div>
    <h2 style="margin-top:12px">Tu compañía basta</h2>
    <p>Si además quieres tener un detalle con nosotros, aquí están todas las opciones.</p>
    <div class="opciones">
      <a class="opcion" href="#" target="_blank" rel="noopener"><svg><use href="#i-storefront"/></svg>
        <div><b>Liverpool</b><span>Evento 51234567</span></div><span class="fl">→</span></a>
      <a class="opcion" href="#" target="_blank" rel="noopener"><svg><use href="#i-gift"/></svg>
        <div><b>Amazon</b><span>Nuestra lista de deseos</span></div><span class="fl">→</span></a>
    </div>
    <div class="cuenta-clabe">0123 4567 8901 2345<small>Lluvia de sobres · BBVA · Valeria Ríos Montes</small></div>''')

s = s.replace('<section class="rsvp" id="confirmar">', ORN + '''<section class="bloque">
  <div class="env sube">
    <svg class="ico"><use href="#i-music-notes"/></svg>
    <div class="sobretitulo">Playlist</div>
    <h2 style="margin-top:12px">¿Qué canción no puede faltar?</h2>
    <p>Dinos cuál te hace bailar sí o sí y la sumamos a la lista de la noche.</p>
  </div>
</section>

<section class="rsvp" id="confirmar">''')
s = s.replace('<div class="sobretitulo">Confirmación</div>',
              '<svg class="ico"><use href="#i-leaf"/></svg>\n      <div class="sobretitulo">Confirmación</div>')
s = s.replace('<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>',
 '<div><label for="cancion">Tu canción para la fiesta</label><input id="cancion" placeholder="Artista y título"></div>\n      '
 '<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>')
s = s.replace("mensaje:$('mensaje').value,fecha:", "cancion:$('cancion').value,mensaje:$('mensaje').value,fecha:")

# ornamentos entre secciones
for antes in ['<section class="bloque-fecha"','<section class="sedes"','<section class="galeria"']:
    s = s.replace(antes, ORN + antes, 1)
escribir(p, s); print("aurora listo")

# ════════════════════════════════════════════════════════════
# SAL — destino. Hospedaje, transporte, carrusel horizontal,
#       actividades del fin de semana, iconografía marina.
# ════════════════════════════════════════════════════════════
p = "i/boda-sal/index.html"; s = leer(p)
s = s.replace('<symbol id="foto" viewBox="0 0 24 24"><path d="M3 5h4l1.5-2h7L17 5h4v15H3V5zm9 3a5 5 0 105 5 5 5 0 00-5-5zm0 2a3 3 0 11-3 3 3 3 0 013-3z"/></symbol>',
 sprite(["map-pin","bed","car-profile","camera","gift","coat-hanger","martini","sparkle","clock","path","champagne"]))
s = s.replace('<use href="#foto"/>', '<use href="#i-camera"/>')

s = s.replace("""/* ─────────── Pase y RSVP ─────────── */""", """
/* ─────────── Iconografía ─────────── */
.ico{width:25px;height:25px;fill:var(--terracota);margin-bottom:12px;opacity:.85}
.brujula{display:flex;align-items:center;gap:12px;justify-content:center;padding:4px 0;color:var(--azulgris);opacity:.45}
.brujula i{display:block;width:48px;height:1px;background:currentColor}
.brujula svg{width:15px;height:15px;fill:currentColor}
.dato .et{display:flex;align-items:center;gap:8px}
.dato .et svg{width:16px;height:16px;fill:var(--terracota);flex:none}

/* Hospedaje */
.hospedaje{padding:84px 0}
.hotel{display:flex;gap:14px;padding:20px 0;border-bottom:1px solid rgba(24,48,64,.12)}
.hotel:last-child{border-bottom:0}
.hotel .num{font-family:var(--serif);font-size:30px;line-height:1;color:var(--terracota);flex:none;width:34px}
.hotel h3{font-family:var(--serif);font-weight:400;font-size:23px;line-height:1.2}
.hotel .d{font-size:13.5px;color:var(--azulgris);margin-top:3px}
.hotel .tarifa{display:inline-block;margin-top:9px;font-size:12px;letter-spacing:.1em;
  padding:4px 11px;border:1px solid rgba(197,121,94,.45);color:var(--terracota);border-radius:999px}

/* Fin de semana */
.finde{padding:84px 0;background:var(--marfil)}
.dia{display:grid;grid-template-columns:88px 1fr;gap:16px;padding:18px 0;
  border-bottom:1px solid rgba(24,48,64,.1)}
.dia:last-child{border-bottom:0}
.dia .cuando{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--terracota);padding-top:5px}
.dia .que{font-family:var(--serif);font-size:21px;line-height:1.25}
.dia .nota{font-size:13.5px;color:var(--azulgris)}

/* Carrusel */
.carrusel{display:flex;gap:12px;overflow-x:auto;margin-top:26px;padding-bottom:10px;
  scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.carrusel::-webkit-scrollbar{display:none}
.carrusel .lamina{flex:none;width:70%;max-width:250px;aspect-ratio:3/4;background:var(--arena);
  position:relative;scroll-snap-align:center;border-radius:2px;overflow:hidden}
.carrusel .lamina img{width:100%;height:100%;object-fit:cover}
.pista{display:flex;gap:6px;justify-content:center;margin-top:14px}
.pista i{width:5px;height:5px;border-radius:50%;background:rgba(85,112,128,.35)}

/* ─────────── Pase y RSVP ─────────── */""")

BRJ = '<div class="brujula" aria-hidden="true"><i></i><svg><use href="#i-sparkle"/></svg><i></i></div>\n'

s = s.replace('<div class="sube"><div class="eyebrow">Dónde</div></div>',
              '<svg class="ico sube"><use href="#i-map-pin"/></svg>\n    <div class="sube"><div class="eyebrow">Dónde</div></div>')
s = s.replace('<div class="et">Ceremonia · 17:00</div>',
              '<div class="et"><svg><use href="#i-champagne"/></svg>Ceremonia · 17:00</div>')
s = s.replace('<div class="et">Cena y fiesta · 20:00</div>',
              '<div class="et"><svg><use href="#i-martini"/></svg>Cena y fiesta · 20:00</div>')
s = s.replace('<div class="eyebrow">Código de vestimenta</div>',
              '<svg class="ico" style="margin-inline:auto"><use href="#i-coat-hanger"/></svg>\n    <div class="eyebrow">Código de vestimenta</div>')

# hospedaje + fin de semana antes del dress code
s = s.replace('<section class="bloque">\n  <div class="env sube">\n    <svg class="ico" style="margin-inline:auto"><use href="#i-coat-hanger"/></svg>',
'''<section class="hospedaje">
  <div class="env">
    <svg class="ico sube"><use href="#i-bed"/></svg>
    <div class="sube"><div class="eyebrow">Dónde quedarte</div>
      <h2 style="font-family:var(--serif);font-weight:400;font-size:32px;margin-top:10px">Tres opciones cerca</h2>
      <p style="color:var(--azulgris);margin-top:10px;max-width:36ch">Apartamos bloque de habitaciones con tarifa especial. Menciona nuestros nombres al reservar.</p></div>
    <div class="hotel sube"><div class="num">01</div>
      <div><h3>Hotel Casa Xcalacoco</h3><div class="d">A 5 minutos caminando de la playa</div>
        <span class="tarifa">Tarifa boda · $2,400 la noche</span></div></div>
    <div class="hotel sube"><div class="num">02</div>
      <div><h3>Posada del Manglar</h3><div class="d">A 10 minutos en coche</div>
        <span class="tarifa">Tarifa boda · $1,600 la noche</span></div></div>
    <div class="hotel sube"><div class="num">03</div>
      <div><h3>Rincón Quinta Avenida</h3><div class="d">En el centro de Playa del Carmen</div>
        <span class="tarifa">Desde $1,100 la noche</span></div></div>
  </div>
</section>

<section class="finde">
  <div class="env">
    <svg class="ico sube"><use href="#i-path"/></svg>
    <div class="sube"><div class="eyebrow">Fin de semana</div>
      <h2 style="font-family:var(--serif);font-weight:400;font-size:32px;margin-top:10px">No solo es un día</h2></div>
    <div class="dia sube"><div class="cuando">Viernes</div>
      <div><div class="que">Cena de bienvenida</div><div class="nota">8:00 pm · Terraza del hotel. Informal.</div></div></div>
    <div class="dia sube"><div class="cuando">Sábado</div>
      <div><div class="que">La boda</div><div class="nota">5:00 pm · Playa Xcalacoco</div></div></div>
    <div class="dia sube"><div class="cuando">Domingo</div>
      <div><div class="que">Desayuno de despedida</div><div class="nota">11:00 am · Antes de que todos vuelen.</div></div></div>
  </div>
</section>

<section class="bloque">
  <div class="env sube">
    <svg class="ico" style="margin-inline:auto"><use href="#i-coat-hanger"/></svg>''')

# transporte
s = s.replace('<section class="galeria">', '''<section class="bloque">
  <div class="env sube">
    <svg class="ico" style="margin-inline:auto"><use href="#i-car-profile"/></svg>
    <div class="eyebrow">Transporte</div>
    <h2>Nosotros te llevamos</h2>
    <p>Sale una camioneta del hotel a las 4:15 pm y regresa a la 1:00 am. Avísanos al confirmar si la vas a usar.</p>
  </div>
</section>

<section class="galeria">''')

# galería como carrusel
s = s.replace('''<div class="celdas sube">
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto horizontal</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
    </div>''', '''<div class="carrusel sube">
      <div class="lamina"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto 1</span></div></div>
      <div class="lamina"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto 2</span></div></div>
      <div class="lamina"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto 3</span></div></div>
      <div class="lamina"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto 4</span></div></div>
    </div>
    <div class="pista" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <p class="eyebrow" style="margin-top:12px">Desliza para ver más</p>''')

s = s.replace('<div class="eyebrow">Regalos</div>',
              '<svg class="ico" style="margin-inline:auto"><use href="#i-gift"/></svg>\n    <div class="eyebrow">Regalos</div>')
s = s.replace('<div class="eyebrow">Confirmación</div>',
              '<svg class="ico" style="margin-inline:auto"><use href="#i-sparkle"/></svg>\n      <div class="eyebrow">Confirmación</div>')
s = s.replace('<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>',
 '<div><label for="transporte">¿Usarás la camioneta del hotel?</label>'
 '<select id="transporte"><option value="si">Sí, cuenten conmigo</option><option value="no">No, llego por mi cuenta</option></select></div>\n      '
 '<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>')
s = s.replace("mensaje:$('mensaje').value,fecha:", "transporte:$('transporte').value,mensaje:$('mensaje').value,fecha:")

for antes in ['<section class="itin"','<section class="datos"']:
    s = s.replace(antes, BRJ + antes, 1)
escribir(p, s); print("sal listo")

# ════════════════════════════════════════════════════════════
# BRUMA — mínimo. Muy poco ornamento a propósito: un solo
#         ícono fino, notas prácticas y preguntas en acordeón.
# ════════════════════════════════════════════════════════════
p = "i/boda-bruma/index.html"; s = leer(p)
s = s.replace('<symbol id="foto" viewBox="0 0 24 24"><path d="M3 5h4l1.5-2h7L17 5h4v15H3V5zm9 3a5 5 0 105 5 5 5 0 00-5-5zm0 2a3 3 0 11-3 3 3 3 0 013-3z"/></symbol>',
 sprite(["map-pin","camera","clock","coat-hanger","gift","lectern"]))
s = s.replace('<use href="#foto"/>', '<use href="#i-camera"/>')

s = s.replace("""/* Motion contenido""", """
/* Iconografía mínima: un solo trazo por sección */
.ico{width:19px;height:19px;fill:var(--greige);margin-bottom:16px}
.preguntas{margin-top:26px}
.preg{border-top:1px solid rgba(39,38,36,.14)}
.preg:last-of-type{border-bottom:1px solid rgba(39,38,36,.14)}
.preg summary{padding:18px 30px 18px 0;cursor:pointer;list-style:none;position:relative;
  font-family:var(--serif);font-size:19px;font-weight:400}
.preg summary::-webkit-details-marker{display:none}
.preg summary::after{content:"";position:absolute;right:2px;top:26px;width:12px;height:1px;background:var(--carbon)}
.preg summary::before{content:"";position:absolute;right:7px;top:21px;width:1px;height:11px;
  background:var(--carbon);transition:transform .5s var(--curva)}
.preg[open] summary::before{transform:scaleY(0)}
.preg p{padding:0 0 20px;color:var(--greige);max-width:40ch;font-size:14.5px}
.nota-seca{margin-top:26px;padding:22px 0;border-top:1px solid rgba(39,38,36,.14);
  border-bottom:1px solid rgba(39,38,36,.14)}
.nota-seca b{font-family:var(--serif);font-size:21px;font-weight:400;display:block}
.nota-seca span{color:var(--greige);font-size:14.5px}

/* Motion contenido""")

s = s.replace('<div class="et">Ceremonia</div>', '<svg class="ico"><use href="#i-clock"/></svg>\n    <div class="et">Ceremonia</div>')
s = s.replace('<div class="et">Lugar</div>', '<svg class="ico"><use href="#i-map-pin"/></svg>\n    <div class="et">Lugar</div>')
s = s.replace('<div class="et">Vestimenta</div>', '<svg class="ico"><use href="#i-coat-hanger"/></svg>\n    <div class="et">Vestimenta</div>')
s = s.replace('<div class="et">Regalos</div>', '<svg class="ico"><use href="#i-gift"/></svg>\n    <div class="et">Regalos</div>')

# nota sin niños + preguntas
s = s.replace('<section class="rsvp" id="confirmar">', '''<section class="texto">
  <div class="env fade">
    <svg class="ico"><use href="#i-lectern"/></svg>
    <div class="et">Buena información</div>
    <h2 style="margin-top:10px">Cosas que conviene saber</h2>
    <div class="nota-seca"><b>Solo adultos</b><span>Queremos que todos puedan relajarse. Gracias por entender.</span></div>
    <div class="nota-seca" style="border-top:0"><b>Estacionamiento</b><span>Valet en la puerta, sin costo.</span></div>
    <div class="preguntas">
      <details class="preg"><summary>¿Puedo llevar acompañante?</summary>
        <p>Tu pase indica los lugares apartados. Si necesitas uno más, escríbenos y vemos.</p></details>
      <details class="preg"><summary>¿Hay opción vegetariana?</summary>
        <p>Sí. Avísanos al confirmar y la cocina lo prepara.</p></details>
      <details class="preg"><summary>¿A qué hora termina?</summary>
        <p>Alrededor de las 8 de la noche. Es una comida, no una fiesta larga.</p></details>
    </div>
  </div>
</section>

<section class="rsvp" id="confirmar">''')
s = s.replace('<div class="et">Confirmación</div>', '<svg class="ico"><use href="#i-clock"/></svg>\n      <div class="et">Confirmación</div>')
escribir(p, s); print("bruma listo")

# ════════════════════════════════════════════════════════════
# GRANATE — gala. Art déco, padrinos, mesa asignada,
#           galería tipo tira de cine, tornaboda.
# ════════════════════════════════════════════════════════════
p = "i/boda-granate/index.html"; s = leer(p)
s = s.replace('<symbol id="foto" viewBox="0 0 24 24"><path d="M3 5h4l1.5-2h7L17 5h4v15H3V5zm9 3a5 5 0 105 5 5 5 0 00-5-5zm0 2a3 3 0 11-3 3 3 3 0 013-3z"/></symbol>',
 sprite(["church","champagne","map-pin","gift","coat-hanger","camera","users-three","armchair","wine","sparkle"]) +
 '''\n  <symbol id="abanico" viewBox="0 0 64 26">
    <g fill="none" stroke="currentColor" stroke-width="1">
      <path d="M32 25a25 25 0 010-24"/><path d="M32 25a17 17 0 010-16"/><path d="M32 25a9 9 0 010-8"/>
      <path d="M32 25a25 25 0 000-24"/><path d="M32 25a17 17 0 000-16"/><path d="M32 25a9 9 0 000-8"/>
      <path d="M0 25h20M44 25h20"/></g></symbol>''')
s = s.replace('<use href="#foto"/>', '<use href="#i-camera"/>')

s = s.replace("""/* Revelado con máscara vertical""", """
/* ─────────── Art déco e iconografía ─────────── */
.ico{width:25px;height:25px;fill:var(--champagne);margin:0 auto 14px;opacity:.9}
.deco{display:flex;justify-content:center;padding:8px 0;color:var(--champagne);opacity:.45}
.deco svg{width:64px;height:26px}
.sede .et svg{width:16px;height:16px;fill:var(--champagne);flex:none}
.sede .et{display:flex;align-items:center;gap:9px;justify-content:center}

/* Padrinos en columnas */
.corte{padding:80px 0;position:relative;z-index:1;border-top:1px solid rgba(198,164,109,.2);text-align:center}
.corte .grupo{margin-top:30px}
.corte .grupo+.grupo{margin-top:30px;padding-top:26px;border-top:1px solid rgba(198,164,109,.14)}
.corte .et2{font-size:11px;letter-spacing:.26em;text-transform:uppercase;color:var(--champagne)}
.corte .par{font-family:var(--display);font-size:23px;line-height:1.5;margin-top:10px}
.corte .rejilla{display:grid;grid-template-columns:1fr 1fr;gap:18px 16px;margin-top:20px;text-align:left}
.corte .rol{font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:rgba(244,233,220,.5)}
.corte .qui{font-family:var(--serif);font-size:19px;line-height:1.25}

/* Mesa asignada */
.mesa{margin:28px auto 0;max-width:330px;border:1px solid rgba(198,164,109,.4);padding:24px;
  position:relative}
.mesa::before,.mesa::after{content:"";position:absolute;width:13px;height:13px;border:1px solid var(--champagne)}
.mesa::before{top:-1px;left:-1px;border-right:0;border-bottom:0}
.mesa::after{bottom:-1px;right:-1px;border-left:0;border-top:0}
.mesa .n{font-family:var(--display);font-size:52px;line-height:1;color:var(--champagne)}
.mesa .l{font-size:11px;letter-spacing:.26em;text-transform:uppercase;margin-top:8px;color:rgba(244,233,220,.6)}

/* Tira de cine */
.cine{display:flex;gap:8px;overflow-x:auto;margin-top:26px;padding:12px 0;
  scroll-snap-type:x mandatory;scrollbar-width:none;
  border-top:1px dashed rgba(198,164,109,.3);border-bottom:1px dashed rgba(198,164,109,.3)}
.cine::-webkit-scrollbar{display:none}
.cine .fotograma{flex:none;width:42%;max-width:150px;aspect-ratio:3/4;background:var(--borgona);
  position:relative;scroll-snap-align:center}

/* Revelado con máscara vertical""")

DEC = '<div class="deco" aria-hidden="true"><svg viewBox="0 0 64 26"><use href="#abanico"/></svg></div>\n'

s = s.replace('<div class="sube"><div class="et">Sábado 28 de noviembre</div></div>',
              '<svg class="ico sube"><use href="#i-champagne"/></svg>\n    <div class="sube"><div class="et">Sábado 28 de noviembre</div></div>')
s = s.replace('<div class="sube"><div class="et">Dónde</div></div>',
              '<svg class="ico sube"><use href="#i-map-pin"/></svg>\n    <div class="sube"><div class="et">Dónde</div></div>')
s = s.replace('<div class="et" style="color:rgba(244,233,220,.5)">Misa · 19:00</div>',
              '<div class="et" style="color:rgba(244,233,220,.5)"><svg><use href="#i-church"/></svg>Misa · 19:00</div>')
s = s.replace('<div class="et" style="color:rgba(244,233,220,.5)">Recepción · 21:00</div>',
              '<div class="et" style="color:rgba(244,233,220,.5)"><svg><use href="#i-wine"/></svg>Recepción · 21:00</div>')
s = s.replace('<div class="sube"><div class="et">Nosotros</div></div>',
              '<svg class="ico sube"><use href="#i-camera"/></svg>\n    <div class="sube"><div class="et">Nosotros</div></div>')
s = s.replace('<div class="et">Código de vestimenta</div>',
              '<svg class="ico"><use href="#i-coat-hanger"/></svg>\n    <div class="et">Código de vestimenta</div>')
s = s.replace('<div class="et">Regalos</div>', '<svg class="ico"><use href="#i-gift"/></svg>\n    <div class="et">Regalos</div>')
s = s.replace('<div class="et">Confirmación</div>', '<svg class="ico"><use href="#i-sparkle"/></svg>\n      <div class="et">Confirmación</div>')

# corte de honor
s = s.replace('<section class="sedes" id="ubicacion">', DEC + '''<section class="corte">
  <div class="env">
    <svg class="ico sube"><use href="#i-users-three"/></svg>
    <div class="sube"><div class="et2">Con la bendición de</div></div>
    <div class="grupo sube">
      <div class="et2">Padres de la novia</div>
      <div class="par">Sr. Joaquín Ortega Lira<br>Sra. Elena Vidal de Ortega</div>
    </div>
    <div class="grupo sube">
      <div class="et2">Padres del novio</div>
      <div class="par">Sr. Alberto Fuentes Mora<br>Sra. Rosa María Serrano</div>
    </div>
    <div class="grupo sube">
      <div class="et2">Corte de honor</div>
      <div class="rejilla">
        <div><div class="rol">Velación</div><div class="qui">Sr. y Sra. Ortega Vidal</div></div>
        <div><div class="rol">Anillos</div><div class="qui">Ximena y Rodrigo</div></div>
        <div><div class="rol">Lazo</div><div class="qui">Familia Serrano</div></div>
        <div><div class="rol">Arras</div><div class="qui">Paulina y Óscar</div></div>
        <div><div class="rol">Cojines</div><div class="qui">Los pequeños Fuentes</div></div>
        <div><div class="rol">Brindis</div><div class="qui">Tío Ernesto</div></div>
      </div>
    </div>
  </div>
</section>

<section class="sedes" id="ubicacion">''')

# tira de cine
s = s.replace('''<div class="celdas sube">
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto horizontal</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
    </div>''', '''<div class="cine sube">
      <div class="fotograma"><div class="hueco"><svg><use href="#i-camera"/></svg><span>01</span></div></div>
      <div class="fotograma"><div class="hueco"><svg><use href="#i-camera"/></svg><span>02</span></div></div>
      <div class="fotograma"><div class="hueco"><svg><use href="#i-camera"/></svg><span>03</span></div></div>
      <div class="fotograma"><div class="hueco"><svg><use href="#i-camera"/></svg><span>04</span></div></div>
      <div class="fotograma"><div class="hueco"><svg><use href="#i-camera"/></svg><span>05</span></div></div>
    </div>
    <p class="et" style="margin-top:12px">Desliza para ver más</p>''')

# mesa asignada + tornaboda
s = s.replace('<section class="rsvp" id="confirmar">', DEC + '''<section class="bloque">
  <div class="env sube">
    <svg class="ico"><use href="#i-armchair"/></svg>
    <div class="et">Tu mesa</div>
    <h2>Ya te apartamos lugar</h2>
    <p>Al llegar, muestra tu pase en la entrada y te acompañamos a tu mesa.</p>
    <div class="mesa"><div class="n">14</div><div class="l">Mesa asignada</div></div>
  </div>
</section>

<section class="bloque">
  <div class="env sube">
    <svg class="ico"><use href="#i-wine"/></svg>
    <div class="et">Después de la fiesta</div>
    <h2>Tornaboda</h2>
    <p>A las dos de la mañana abrimos el salón chico con chilaquiles y café para los que aguanten.</p>
  </div>
</section>

<section class="rsvp" id="confirmar">''')
for antes in ['<section class="itin"','<section class="galeria"']:
    s = s.replace(antes, DEC + antes, 1)
escribir(p, s); print("granate listo")

# ════════════════════════════════════════════════════════════
# ALMENDRO — día. Padres, actividades, galería polaroid
#            desfasada, playlist colaborativa, hashtag.
# ════════════════════════════════════════════════════════════
p = "i/boda-almendro/index.html"; s = leer(p)
s = s.replace('<symbol id="foto" viewBox="0 0 24 24"><path d="M3 5h4l1.5-2h7L17 5h4v15H3V5zm9 3a5 5 0 105 5 5 5 0 00-5-5zm0 2a3 3 0 11-3 3 3 3 0 013-3z"/></symbol>',
 sprite(["map-pin","camera","gift","coat-hanger","users-three","music-notes","leaf","storefront","wine","flower-tulip"]))
s = s.replace('<use href="#foto"/>', '<use href="#i-camera"/>')

s = s.replace("""/* ─────────── RSVP ─────────── */""", """
/* ─────────── Iconografía y ornamento ─────────── */
.ico{width:25px;height:25px;fill:var(--champagne);margin-bottom:12px;opacity:.9}
.hojita{display:flex;align-items:center;gap:12px;padding:6px 0;color:var(--salvia);opacity:.5}
.hojita i{display:block;height:1px;background:currentColor;flex:1}
.hojita svg{width:17px;height:17px;fill:currentColor;flex:none}
.et svg{vertical-align:-2px}

/* Padres */
.padres{padding:80px 0;border-top:1px solid rgba(89,101,75,.15)}
.par-bloque{margin-top:26px}
.par-bloque+.par-bloque{margin-top:26px;padding-top:24px;border-top:1px solid rgba(89,101,75,.12)}
.par-bloque .rol{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--salvia)}
.par-bloque .nom{font-family:var(--serif);font-weight:600;font-size:22px;line-height:1.45;margin-top:8px}

/* Actividades */
.acts{display:grid;gap:10px;margin-top:24px}
.act{display:flex;gap:14px;align-items:flex-start;padding:17px 18px;background:var(--blanco);
  border:1px solid rgba(89,101,75,.14);border-radius:4px}
.act svg{width:21px;height:21px;fill:var(--champagne);flex:none;margin-top:3px}
.act b{display:block;font-family:var(--serif);font-weight:600;font-size:19px;line-height:1.2}
.act span{font-size:13.5px;color:var(--salvia)}

/* Galería polaroid desfasada */
.polaroids{margin-top:28px}
.polaroid{background:var(--blanco);padding:10px 10px 40px;border:1px solid rgba(89,101,75,.12);
  box-shadow:0 10px 30px -18px rgba(46,54,38,.4);position:relative}
.polaroid .marco{aspect-ratio:1;background:var(--arena);position:relative}
.polaroid .titulo{position:absolute;left:0;right:0;bottom:12px;text-align:center;
  font-family:var(--cursiva);font-style:italic;font-size:13px;color:var(--salvia)}
.polaroid:nth-child(1){width:62%;transform:rotate(-2.2deg)}
.polaroid:nth-child(2){width:58%;margin:-16px 0 0 auto;transform:rotate(2.6deg)}
.polaroid:nth-child(3){width:54%;margin:-10px auto 0;transform:rotate(-1.2deg)}
.polaroid+.polaroid{margin-top:18px}

/* Hashtag */
.hashtag{display:inline-block;margin-top:16px;font-family:var(--serif);font-weight:600;
  font-size:26px;color:var(--champagne);letter-spacing:.01em}

/* ─────────── RSVP ─────────── */""")

HOJ = '<div class="env"><div class="hojita" aria-hidden="true"><i></i><svg><use href="#i-leaf"/></svg><i></i></div></div>\n'

s = s.replace('<div class="sube"><div class="et">Sábado 4 de julio</div></div>',
              '<svg class="ico sube"><use href="#i-wine"/></svg>\n    <div class="sube"><div class="et">Sábado 4 de julio</div></div>')
s = s.replace('<div class="sube"><div class="et">Dónde</div>',
              '<svg class="ico sube"><use href="#i-map-pin"/></svg>\n    <div class="sube"><div class="et">Dónde</div>')
s = s.replace('<div class="et">Código de vestimenta</div>',
              '<svg class="ico"><use href="#i-coat-hanger"/></svg>\n    <div class="et">Código de vestimenta</div>')
s = s.replace('<div class="sube"><div class="et">Nosotros</div></div>',
              '<svg class="ico sube"><use href="#i-camera"/></svg>\n    <div class="sube"><div class="et">Nosotros</div></div>')
s = s.replace('<div class="et">Regalos</div>',
              '<svg class="ico"><use href="#i-gift"/></svg>\n    <div class="et">Regalos</div>')
s = s.replace('<div class="et">Confirmación</div>',
              '<svg class="ico"><use href="#i-flower-tulip"/></svg>\n      <div class="et">Confirmación</div>')

# padres antes del itinerario
s = s.replace('<section class="itin" id="detalles">', '''<section class="padres">
  <div class="env">
    <svg class="ico sube"><use href="#i-users-three"/></svg>
    <div class="sube"><div class="et">Con la bendición de</div>
      <h2 style="font-family:var(--serif);font-weight:600;font-size:30px;margin-top:8px">Nuestros papás</h2></div>
    <div class="par-bloque sube"><div class="rol">Padres de la novia</div>
      <div class="nom">Sr. Ignacio Aguilar Pardo<br>Sra. Teresa León de Aguilar</div></div>
    <div class="par-bloque sube"><div class="rol">Padres del novio</div>
      <div class="nom">Sr. Gerardo Campos Ruiz<br>Sra. Alicia Navarro de Campos</div></div>
  </div>
</section>

<section class="itin" id="detalles">''')

# actividades + galería polaroid
s = s.replace('<section class="galeria">', '''<section class="bloque">
  <div class="env">
    <svg class="ico sube"><use href="#i-flower-tulip"/></svg>
    <div class="sube"><div class="et">Durante la tarde</div>
      <h2 style="font-family:var(--serif);font-weight:600;font-size:30px;margin-top:8px">Qué va a haber</h2></div>
    <div class="acts sube">
      <div class="act"><svg><use href="#i-wine"/></svg>
        <div><b>Cata de vinos del valle</b><span>3:00 pm · En la terraza de piedra</span></div></div>
      <div class="act"><svg><use href="#i-flower-tulip"/></svg>
        <div><b>Taller de coronas</b><span>4:00 pm · Con flores del jardín</span></div></div>
      <div class="act"><svg><use href="#i-music-notes"/></svg>
        <div><b>Trío en vivo</b><span>6:00 pm · Hasta que se acabe la luz</span></div></div>
    </div>
  </div>
</section>

<section class="galeria">''')

s = s.replace('''<div class="celdas sube">
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto horizontal</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
      <div class="celda"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
    </div>''', '''<div class="polaroids sube">
      <div class="polaroid"><div class="marco"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
        <div class="titulo">el día que nos conocimos</div></div>
      <div class="polaroid"><div class="marco"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
        <div class="titulo">nuestro primer viaje</div></div>
      <div class="polaroid"><div class="marco"><div class="hueco"><svg><use href="#i-camera"/></svg><span>Foto</span></div></div>
        <div class="titulo">la propuesta</div></div>
    </div>''')

# mesa de regalos con tienda + hashtag
s = s.replace('<div class="clabe">9988 7766 5544 3322<small>BBVA · Sofía Aguilar León</small></div>',
'''<div class="acts" style="margin-top:20px">
      <a class="act" href="#" target="_blank" rel="noopener" style="text-decoration:none">
        <svg><use href="#i-storefront"/></svg>
        <div><b>Mesa en Liverpool</b><span>Evento 51239876 · Ver la lista →</span></div></a>
    </div>
    <div class="clabe">9988 7766 5544 3322<small>Lluvia de sobres · BBVA · Sofía Aguilar León</small></div>''')

s = s.replace('<section class="rsvp" id="confirmar">', '''<section class="bloque">
  <div class="env sube" style="text-align:center">
    <svg class="ico" style="margin-inline:auto"><use href="#i-camera"/></svg>
    <div class="et">Comparte tus fotos</div>
    <h2 style="font-family:var(--serif);font-weight:600;font-size:30px;margin-top:8px">Súbelas con nuestro hashtag</h2>
    <p style="margin-inline:auto">Todo lo que publiques ese día lo vamos a guardar en nuestro álbum.</p>
    <div class="hashtag">#SofíaYTomás2026</div>
  </div>
</section>

<section class="rsvp" id="confirmar">''')

s = s.replace('<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>',
 '<div><label for="cancion">Una canción para la tarde</label><input id="cancion" placeholder="Artista y título"></div>\n      '
 '<div><label for="mensaje">Un mensaje para nosotros</label><textarea id="mensaje" rows="3"></textarea></div>')
s = s.replace("mensaje:$('mensaje').value,fecha:", "cancion:$('cancion').value,mensaje:$('mensaje').value,fecha:")

for antes in ['<section class="lugares"','<section class="galeria"']:
    s = s.replace(antes, HOJ + antes, 1)
escribir(p, s); print("almendro listo")
