# -*- coding: utf-8 -*-
"""Genera /catalogo/ y /catalogo/<id>/ a partir del CATALOGO del landing."""
import json, os, re, html

ROOT = "/home/claude/savey/savey-studio"
WA   = "5215618906790"
TEL  = "+52 1 56 1890 6790"

# ── leer CATALOGO del index.html ─────────────────────────────
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
i = src.index("var CATALOGO=[")
j = src.index("\n];", i) + 2
crudo = src[i + len("var CATALOGO="): j]
# claves sin comillas -> JSON
crudo = re.sub(r'([{,]\s*)([A-Za-z_]\w*)\s*:', r'\1"\2":', crudo)
CATALOGO = json.loads(crudo)

# ── copy por categoría ───────────────────────────────────────
COPY = {
 "bodas":      ("Invitaciones digitales de boda",
                "Desde una boda en el jardín hasta una en hacienda. Busca la que más se parezca a la de ustedes.",
                "boda"),
 "xv":         ("Invitaciones digitales de XV años",
                "Para su noche: desde algo sencillo y bonito hasta una fiesta de gala. Todo se ajusta a lo que ella quiera.",
                "XV años"),
 "bautizos":   ("Invitaciones digitales de bautizo",
                "Diseños tranquilos y con mucha luz, para la ceremonia y la comida con la familia.",
                "bautizo"),
 "ninos":      ("Invitaciones de cumpleaños infantil",
                "Dinosaurios, cohetes, ballet o carreras. Dinos qué le encanta y nosotros armamos su fiesta.",
                "cumpleaños infantil"),
 "teens":      ("Invitaciones digitales de cumpleaños",
                "Para cualquier edad: una comida en casa, una cena en la terraza o una fiesta con los amigos.",
                "cumpleaños"),
 "graduacion": ("Invitaciones digitales de graduación",
                "Para la ceremonia, la cena con la familia o la fiesta de toda la generación.",
                "graduación"),
 "empresa":    ("Invitaciones para eventos de empresa",
                "Conferencias, lanzamientos, aniversarios y cenas de premiación, con el tono que necesitas.",
                "evento de empresa"),
 "temporada":  ("Invitaciones para fiestas de temporada",
                "Posada, Día de Muertos, 15 de septiembre, Día de la Madre. Las fechas que celebras cada año.",
                "fiesta de temporada"),
 "otros":      ("Invitaciones para todo lo demás",
                "Kermés, concierto, obra de teatro, exposición, torneo o una ponencia. Si tu evento no entra en las otras listas, aquí hay algo.",
                "evento"),
}

NOTA = ("Estas son algunas ideas para inspirarte. Todo se adapta: tus colores, tus fotos "
        "y las secciones que quieras. Y si te gusta la portada de una con la estructura "
        "de otra, las combinamos.")

# Aviso de propiedad intelectual, solo en las dos de cumpleaños
IP = ("En Savey cuidamos los derechos de autor, así que no usamos personajes, logotipos "
      "ni ilustraciones con licencia dentro de las invitaciones. Lo que sí hacemos es "
      "trabajar el tema: dinos en qué personaje, película o serie quieres que nos "
      "inspiremos y armamos los colores, las texturas y el ambiente alrededor de esa "
      "idea, con dibujos originales hechos para tu fiesta.")

SIM = {  # símbolos svg compartidos
 "ch": '<symbol id="ch" viewBox="0 0 24 24"><path d="M12 0c0 6.2 5.8 12 12 12-6.2 0-12 5.8-12 12 0-6.2-5.8-12-12-12C6.2 12 12 6.2 12 0z"/></symbol>',
 "wa": '<symbol id="wa" viewBox="0 0 24 24"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 004.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96 0-2.66-1.04-5.16-2.92-7.04A9.88 9.88 0 0012.04 2zm0 1.87c2.16 0 4.19.84 5.72 2.37a8.04 8.04 0 012.37 5.72c0 4.46-3.63 8.09-8.09 8.09a8.06 8.06 0 01-4.11-1.13l-.3-.17-3.06.8.82-3-.19-.31a8.03 8.03 0 01-1.23-4.29c0-4.45 3.62-8.08 8.07-8.08zm-2.4 4.1c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32.98 2.48c.12.16 1.68 2.57 4.08 3.6.57.25 1.01.39 1.36.5.57.18 1.09.16 1.5.1.46-.07 1.41-.58 1.61-1.14.2-.56.2-1.04.14-1.14-.06-.1-.22-.16-.46-.28-.24-.12-1.41-.7-1.63-.78-.22-.08-.38-.12-.54.12-.16.24-.62.78-.76.94-.14.16-.28.18-.52.06-.24-.12-1.01-.37-1.92-1.19-.71-.63-1.19-1.41-1.33-1.65-.14-.24-.01-.37.11-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.54-1.3-.74-1.78-.19-.46-.39-.4-.54-.41h-.44z"/></symbol>',
 "fl": '<symbol id="fl" viewBox="0 0 20 20"><path d="M4 10h12M11 5l5 5-5 5"/></symbol>',
 "ig": '<symbol id="ig" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5.2"/><circle cx="12" cy="12" r="4.1"/><circle cx="17.4" cy="6.6" r="1.15" fill="currentColor" stroke="none"/></symbol>',
 "fb": '<symbol id="fb" viewBox="0 0 24 24"><path d="M14.6 21.5v-8h2.7l.5-3.2h-3.2V8.2c0-.9.3-1.6 1.6-1.6h1.7V3.7c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H8.3v3.2h2.9v8z"/></symbol>',
}
SVG_DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
            + SIM["ch"] + SIM["wa"] + SIM["fl"] + SIM["ig"] + SIM["fb"] + "</svg>")

REDES = ("https://www.instagram.com/savey.mx/",
         "https://www.facebook.com/profile.php?id=61594253131441")

E = lambda s: html.escape(s, quote=True)


def barra(activo_liga=True):
    return f'''<div class="hilo" id="hilo"><i></i></div>
<header class="barra" id="barra">
  <div class="barra-caja">
    <a class="logo" href="/"><svg width="12" height="12"><use href="#ch"/></svg>savey</a>
    <nav>
      <a class="liga" href="/catalogo/">Todas las categorías</a>
      <a class="liga" href="/#paquetes">Paquetes</a>
      <a class="btn btn-champ" href="/brief/">Cotiza tu evento</a>
      <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg width="17" height="17"><use href="#wa"/></svg></a>
    </nav>
  </div>
</header>'''


def pie():
    return f'''<footer>
  <div class="amplia">
    <svg class="chispa" width="14" height="14" aria-hidden="true"><use href="#ch"/></svg>
    <p>Savey. Estudio de invitaciones digitales. Estado de México, México.</p>
    <div class="redes">
      <a href="{REDES[0]}" target="_blank" rel="noopener" data-r="ig" aria-label="Savey en Instagram"><svg width="18" height="18"><use href="#ig"/></svg></a>
      <a href="{REDES[1]}" target="_blank" rel="noopener" data-r="fb" aria-label="Savey en Facebook"><svg width="18" height="18"><use href="#fb"/></svg></a>
    </div>
    <nav>
      <a href="/">Inicio</a>
      <a href="/catalogo/">Catálogo por categoría</a>
      <a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {TEL}</a>
      <a href="mailto:savey.mx@gmail.com">savey.mx@gmail.com</a>
      <a href="/aviso-de-privacidad.html">Aviso de privacidad</a>
      <a href="/terminos.html">Términos del servicio</a>
    </nav>
    <p class="legal">Precios en pesos mexicanos, vigentes en 2026.</p>
  </div>
</footer>'''


def cabeza(titulo, desc, url, og, extra=""):
    return f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" href="/favicon.ico?v=3" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=3">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3">
<link rel="manifest" href="/site.webmanifest">
<title>{E(titulo)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#F7F2EA">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(titulo)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="es_MX">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/catalogo/catalogo.css?v=3">
<script>document.documentElement.className+=' js';</script>
{extra}</head>
<body>
{SVG_DEFS}
'''


def mini(p, rotulo, clase="muestra"):
    """Miniatura de invitación, idéntica a la del landing."""
    foto = (f'<img class="m-foto" src="{p["im"]}" alt="" loading="lazy" draggable="false">'
            if p.get("im") else "")
    return (
      f'<a class="{clase} revelar" href="{p["ru"]}?c=A7K9" aria-label="Abrir el diseño {E(p["t"])}" draggable="false">'
      f'<div class="pantalla {p.get("k","")}{" con-foto" if p.get("im") else ""}" '
      f'style="--m-fondo:{p["c"][0]};--m-tinta:{p["c"][1]};--m-acento:{p["c"][2]}">'
      f'<div class="marco">{foto}</div>'
      f'<div class="capa"><span class="m-rotulo">{E(rotulo)}</span>'
      f'<span class="m-nombre">{E(p["n"])}</span>'
      f'<svg class="m-orn" width="10" height="10"><use href="#ch"/></svg>'
      f'<span class="m-fecha">{E(p["f"])}</span></div>'
      f'<span class="ver">Abrir</span></div>'
      f'<b>{E(p["t"])}</b><em>{E(p["d"])}</em></a>'
    )


def abanico(piezas, rotulo):
    orden = [piezas[1], piezas[0], piezas[2]] if len(piezas) > 2 else piezas
    hojas = []
    for p in orden:
        foto = (f'<img class="m-foto" src="{p["im"]}" alt="" loading="lazy">' if p.get("im") else "")
        hojas.append(
          f'<div class="hoja"><div class="pantalla {p.get("k","")}{" con-foto" if p.get("im") else ""}" '
          f'style="--m-fondo:{p["c"][0]};--m-tinta:{p["c"][1]};--m-acento:{p["c"][2]}">'
          f'<div class="marco">{foto}</div>'
          f'<div class="capa"><span class="m-rotulo">{E(rotulo)}</span>'
          f'<span class="m-nombre">{E(p["n"])}</span>'
          f'<svg class="m-orn" width="10" height="10"><use href="#ch"/></svg>'
          f'<span class="m-fecha">{E(p["f"])}</span></div></div></div>')
    return '<div class="abanico" aria-hidden="true">' + "".join(hojas) + '</div>'


def jsonld(cat, titulo, url):
    items = [{"@type": "ListItem", "position": n + 1, "name": p["t"],
              "url": "https://saveystudio.com" + p["ru"]}
             for n, p in enumerate(cat["piezas"])]
    d = {"@context": "https://schema.org", "@type": "CollectionPage",
         "name": titulo, "url": url,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": items}}
    return ('<script type="application/ld+json">'
            + json.dumps(d, ensure_ascii=False) + "</script>\n")


# ── páginas de categoría ─────────────────────────────────────
for n, cat in enumerate(CATALOGO):
    cid = cat["id"]
    titulo_largo, entrada, singular = COPY[cid]
    url = f"https://saveystudio.com/catalogo/{cid}/"
    og = f"https://saveystudio.com/catalogo/og/{cid}.jpg"
    acento = cat["piezas"][0]["c"][2]
    tinta = cat["piezas"][0]["c"][0]

    tarjetas = "\n      ".join(mini(p, cat["rotulo"]) for p in cat["piezas"])

    otras = [c for c in CATALOGO if c["id"] != cid]
    fichas = "\n      ".join(
        f'<a class="ficha revelar" href="/catalogo/{c["id"]}/" '
        f'style="--fa:{c["piezas"][0]["c"][2]};--fb:{c["piezas"][0]["c"][0]}">'
        f'<span class="fl"><svg width="15" height="15"><use href="#fl"/></svg></span>'
        f'<strong>{E(c["nombre"])}</strong><span>Ver ideas</span></a>'
        for c in otras)

    wa_txt = f"Hola Savey, vi el catálogo de {singular} y me interesa."

    aviso = ""
    if cid in ("ninos", "teens"):
        aviso = f'''<section class="aviso-pi">
  <div class="amplia">
    <div class="pi revelar">
      <b>Sobre los personajes con derechos de autor</b>
      <p>{E(IP)}</p>
    </div>
  </div>
</section>

'''


    doc = cabeza(
        f"{titulo_largo} · Savey",
        entrada,
        url, og,
        extra=jsonld(cat, titulo_largo, url)
    )
    doc += barra()
    doc += f'''
<main>

<section class="encabezado" style="--acento:{acento};--tinta-cat:{tinta}">
  <div class="amplia">
    <nav class="miga" aria-label="Ruta">
      <a href="/">Savey</a><i>/</i><a href="/catalogo/">Catálogo</a><i>/</i><b>{E(cat["nombre"])}</b>
    </nav>
    <h1 class="titulo">{E(cat["nombre"])}</h1>
    <p class="entrada">{E(entrada)}</p>
    <p class="nota">{E(NOTA)}</p>
    <div class="acciones">
      <a class="btn btn-champ" href="/brief/">Cotiza tu evento<svg class="flechita" width="16" height="16"><use href="#fl"/></svg></a>
      <a class="btn btn-wa" href="https://wa.me/{WA}?text={E(wa_txt).replace(" ", "%20").replace(",", "%2C")}" target="_blank" rel="noopener"><svg width="17" height="17"><use href="#wa"/></svg>Escríbenos</a>
    </div>
    {abanico(cat["piezas"], cat["rotulo"])}
  </div>
</section>

<section class="rejilla-sec">
  <div class="amplia">
    <div class="rejilla" id="rejilla">
      {tarjetas}
    </div>
  </div>
</section>

{aviso}<section class="otras">
  <div class="amplia">
    <h2 class="revelar">Otras categorías</h2>
    <p class="pie revelar">Cada una abre solo los diseños de ese tipo de evento.</p>
    <div class="fichas">
      {fichas}
    </div>
  </div>
</section>

<section class="cierre">
  <div class="amplia">
    <div class="panel revelar" style="--acento:{acento}">
      <h2>¿Te gustó alguno?</h2>
      <p>Cuéntanos de tu evento en unos minutos y te mandamos tu cotización por WhatsApp.</p>
      <div class="acciones">
        <a class="btn btn-champ" href="/brief/" style="background:var(--marfil);color:var(--espresso)">Cotiza tu evento<svg class="flechita" width="16" height="16"><use href="#fl"/></svg></a>
        <a class="btn btn-wa" href="https://wa.me/{WA}?text={E(wa_txt).replace(" ", "%20").replace(",", "%2C")}" target="_blank" rel="noopener"><svg width="17" height="17"><use href="#wa"/></svg>Escríbenos por WhatsApp</a>
      </div>
      <p class="tel">O márcanos directo al <a href="https://wa.me/{WA}" target="_blank" rel="noopener">{TEL}</a>.</p>
    </div>
  </div>
</section>

</main>

{pie()}
<script src="https://cdn.jsdelivr.net/npm/motion@11.15.0/dist/motion.min.js"></script>
<script src="/catalogo/catalogo.js?v=3"></script>
</body>
</html>
'''
    d = os.path.join(ROOT, "catalogo", cid)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(doc)

# ── índice del catálogo ──────────────────────────────────────
url = "https://saveystudio.com/catalogo/"
total = sum(len(c["piezas"]) for c in CATALOGO)
cartas = []
for c in CATALOGO:
    tira = "".join(
        f'<span style="--m-fondo:{p["c"][0]}"><img src="{p["im"]}" alt="" loading="lazy"></span>'
        for p in c["piezas"][:3])
    cartas.append(
      f'''<a class="carta revelar" href="/catalogo/{c["id"]}/" style="--fa:{c["piezas"][0]["c"][2]};--fb:{c["piezas"][0]["c"][0]}">
        <div class="cab"><h2>{E(c["nombre"])}</h2></div>
        <p>{E(COPY[c["id"]][1])}</p>
        <div class="tira">{tira}</div>
        <span class="mas">Ver la categoría<svg width="15" height="15"><use href="#fl"/></svg></span>
      </a>''')

desc_i = ("Los diseños de Savey ordenados por tipo de evento: bodas, XV años, "
          "bautizos, cumpleaños, graduación, corporativo, de temporada y más.")
doc = cabeza("Catálogo de invitaciones digitales por categoría · Savey",
             desc_i, url, "https://saveystudio.com/catalogo/og/catalogo.jpg")
doc += barra()
doc += f'''
<main>

<section class="indice-cab">
  <div class="amplia">
    <nav class="miga" aria-label="Ruta"><a href="/">Savey</a><i>/</i><b>Catálogo</b></nav>
    <h1 class="titulo">Catálogo</h1>
    <p class="entrada">Nuestros diseños, ordenados por tipo de evento. Cada categoría tiene su propia liga.</p>
    <div class="acciones">
      <a class="btn btn-champ" href="/brief/">Cotiza tu evento<svg class="flechita" width="16" height="16"><use href="#fl"/></svg></a>
      <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener"><svg width="17" height="17"><use href="#wa"/></svg>Escríbenos</a>
    </div>
  </div>
</section>

<section>
  <div class="amplia">
    <div class="indice">
      {"".join(cartas)}
    </div>
  </div>
</section>


<section class="cierre" style="padding-top:var(--aire)">
  <div class="amplia">
    <div class="panel revelar">
      <h2>¿Ya sabes cuál quieres?</h2>
      <p>Cuéntanos de tu evento en unos minutos y te mandamos tu cotización por WhatsApp.</p>
      <div class="acciones">
        <a class="btn btn-champ" href="/brief/" style="background:var(--marfil);color:var(--espresso)">Cotiza tu evento<svg class="flechita" width="16" height="16"><use href="#fl"/></svg></a>
        <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener"><svg width="17" height="17"><use href="#wa"/></svg>Escríbenos por WhatsApp</a>
      </div>
      <p class="tel">O márcanos directo al <a href="https://wa.me/{WA}" target="_blank" rel="noopener">{TEL}</a>.</p>
    </div>
  </div>
</section>

</main>

{pie()}
<script src="https://cdn.jsdelivr.net/npm/motion@11.15.0/dist/motion.min.js"></script>
<script src="/catalogo/catalogo.js?v=3"></script>
</body>
</html>
'''
open(os.path.join(ROOT, "catalogo", "index.html"), "w", encoding="utf-8").write(doc)

print("categorías:", [c["id"] for c in CATALOGO], "· total", total)
