# -*- coding: utf-8 -*-
"""Tarjetas 1200x630 para la vista previa al compartir cada categoría."""
import json, os, re
from PIL import Image, ImageDraw, ImageFont

ROOT = "/home/claude/savey/savey-studio"
OUT  = os.path.join(ROOT, "catalogo", "og")
os.makedirs(OUT, exist_ok=True)

SERIF = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
SANS  = "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"
SANSB = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"

MARFIL = (247, 242, 234)
ESPRESSO = (51, 43, 39)
SUAVE = (110, 98, 91)
CHAMP = (199, 167, 122)

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
i = src.index("var CATALOGO=["); j = src.index("\n];", i) + 2
crudo = re.sub(r'([{,]\s*)([A-Za-z_]\w*)\s*:', r'\1"\2":', src[i + len("var CATALOGO="): j])
CATALOGO = json.loads(crudo)

SUB = {
 "bodas": "Invitaciones digitales de boda",
 "xv": "Invitaciones digitales de XV años",
 "bautizos": "Invitaciones digitales de bautizo",
 "ninos": "Invitaciones de cumpleaños infantil",
 "teens": "Invitaciones digitales de cumpleaños",
 "graduacion": "Invitaciones digitales de graduación",
 "empresa": "Invitaciones para eventos de empresa",
 "temporada": "Invitaciones para fiestas de temporada",
 "otros": "Invitaciones para todo lo demás",
}

W, H = 1200, 630
S = 3  # supersampling


def hx(c):
    c = c.lstrip("#")
    return tuple(int(c[k:k + 2], 16) for k in (0, 2, 4))


def chispa(d, cx, cy, r, color):
    """Los cuatro pétalos del logo, en curvas."""
    pts = []
    n = 160
    import math
    for k in range(n + 1):
        t = 2 * math.pi * k / n
        # estrella de cuatro puntas suave
        rr = r * (abs(math.cos(2 * t)) ** 0.5)
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
    d.polygon(pts, fill=color)


def tarjeta(cid, nombre, piezas, destino):
    im = Image.new("RGB", (W * S, H * S), MARFIL)
    d = ImageDraw.Draw(im, "RGBA")
    ac = hx(piezas[0]["c"][2])
    fo = hx(piezas[0]["c"][0])

    # lavado de color, dos radiales suaves
    lav = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    dl = ImageDraw.Draw(lav)
    dl.ellipse([int(W * .42) * S, int(-H * .55) * S, int(W * 1.35) * S, int(H * 1.05) * S],
               fill=ac + (56,))
    dl.ellipse([int(-W * .2) * S, int(H * .42) * S, int(W * .5) * S, int(H * 1.6) * S],
               fill=fo + (26,))
    from PIL import ImageFilter
    lav = lav.filter(ImageFilter.GaussianBlur(radius=110 * S))
    im = Image.alpha_composite(im.convert("RGBA"), lav).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")

    # ── tres miniaturas, abanico a la derecha ──
    mw, mh = 228, 380
    base_x, base_y = int(W * .665), int(H * .5)
    orden = [(-1, -7.5), (1, 7.5), (0, 0)]  # el central al final, encima
    for k, (lado, giro) in enumerate(orden):
        p = piezas[[0, 2, 1][k]] if len(piezas) > 2 else piezas[0]
        idx = [0, 2, 1][k]
        p = piezas[idx % len(piezas)]
        ruta = os.path.join(ROOT, p["im"].split("?")[0].lstrip("/"))
        card = Image.new("RGB", (mw * S, mh * S), hx(p["c"][0]))
        if os.path.exists(ruta):
            foto = Image.open(ruta).convert("RGB")
            fw, fh = foto.size
            esc = max(mw * S / fw, mh * S / fh)
            foto = foto.resize((int(fw * esc), int(fh * esc)), Image.LANCZOS)
            ox = (foto.width - mw * S) // 2
            oy = (foto.height - mh * S) // 2
            card.paste(foto.crop((ox, oy, ox + mw * S, oy + mh * S)), (0, 0))
        # velo inferior + nombre
        dc = ImageDraw.Draw(card, "RGBA")
        velo = Image.new("RGBA", (mw * S, mh * S), (0, 0, 0, 0))
        dv = ImageDraw.Draw(velo)
        alto = int(mh * S * .42)
        for y in range(alto):
            a = int(215 * (y / alto) ** 1.5)
            dv.line([(0, mh * S - alto + y), (mw * S, mh * S - alto + y)], fill=hx(p["c"][0]) + (a,))
        card = Image.alpha_composite(card.convert("RGBA"), velo).convert("RGB")
        dc = ImageDraw.Draw(card)
        if lado == 0:   # solo la del centro lleva nombre: las laterales se ven tapadas
            f_n = ImageFont.truetype(SERIF, 30 * S)
            tn = p["n"]
            while dc.textlength(tn, font=f_n) > (mw - 26) * S and len(tn) > 4:
                tn = tn[:-2]
            dc.text((mw * S / 2, mh * S - 46 * S), tn, font=f_n, fill=hx(p["c"][1]), anchor="ms")
        # borde interior
        dc.rounded_rectangle([7 * S, 7 * S, (mw - 7) * S, (mh - 7) * S], radius=9 * S,
                             outline=hx(p["c"][2]), width=max(1, int(S * .8)))

        # esquinas redondeadas + rotación
        mask = Image.new("L", (mw * S, mh * S), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, mw * S, mh * S], radius=18 * S, fill=255)
        card.putalpha(mask)
        card = card.rotate(-giro, resample=Image.BICUBIC, expand=True)
        px = base_x * S + int(lado * 198 * S) - card.width // 2
        py = base_y * S + (18 * S if lado else 0) - card.height // 2
        # sombra
        som = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sm = card.split()[-1].point(lambda v: int(v * .34))
        som.paste((30, 24, 21, 255), (px, py + 16 * S), sm)
        som = som.filter(ImageFilter.GaussianBlur(radius=16 * S))
        im = Image.alpha_composite(im.convert("RGBA"), som).convert("RGB")
        im.paste(card.convert("RGB"), (px, py), card.split()[-1])

    d = ImageDraw.Draw(im, "RGBA")

    # ── texto a la izquierda ──
    x = 78 * S
    f_marca = ImageFont.truetype(SERIF, 34 * S)
    f_tit = ImageFont.truetype(SERIF, 88 * S)
    f_sub = ImageFont.truetype(SANS, 29 * S)
    f_pie = ImageFont.truetype(SANSB, 22 * S)

    chispa(d, x + 12 * S, 96 * S, 13 * S, CHAMP)
    d.text((x + 36 * S, 96 * S), "savey", font=f_marca, fill=ESPRESSO, anchor="lm")

    # título, hasta dos líneas
    palabras = nombre.split()
    lineas, act = [], ""
    for p_ in palabras:
        t = (act + " " + p_).strip()
        if d.textlength(t, font=f_tit) > 560 * S and act:
            lineas.append(act); act = p_
        else:
            act = t
    lineas.append(act)
    y = 232 * S if len(lineas) == 1 else 196 * S
    for ln in lineas:
        d.text((x, y), ln, font=f_tit, fill=ESPRESSO, anchor="ls")
        y += 92 * S

    d.text((x, y + 16 * S), SUB[cid], font=f_sub, fill=SUAVE, anchor="ls")

    # sello inferior
    yb = H * S - 84 * S
    d.rounded_rectangle([x, yb, x + 268 * S, yb + 52 * S], radius=26 * S,
                        fill=(255, 253, 252, 235), outline=(51, 43, 39, 28), width=int(S))
    chispa(d, x + 28 * S, yb + 26 * S, 7 * S, hx(piezas[0]["c"][2]))
    d.text((x + 46 * S, yb + 27 * S), f"{len(piezas)} diseños · saveystudio.com",
           font=f_pie, fill=ESPRESSO, anchor="lm")

    im = im.resize((W, H), Image.LANCZOS)
    im.save(destino, "JPEG", quality=88, optimize=True, progressive=True)
    return os.path.getsize(destino) // 1024


from PIL import ImageFilter  # noqa: E402

for c in CATALOGO:
    k = tarjeta(c["id"], c["nombre"], c["piezas"], os.path.join(OUT, c["id"] + ".jpg"))
    print(c["id"], k, "KB")

# portada del índice: mezcla de categorías
mix = [c["piezas"][0] for c in CATALOGO[:3]]
k = tarjeta("bodas", "Catálogo", mix, os.path.join(OUT, "catalogo.jpg"))
print("catalogo", k, "KB")
