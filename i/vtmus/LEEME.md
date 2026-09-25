# VTMUS · María Camila cumple 3

Paquete **Plata** · Estefanía Alemán (+52 444 384 3993) · domingo 15 de
noviembre de 2026, 2:30 p. m.

```
vtmus/
  index.html        ← la invitación
  lista/index.html  ← el panel de confirmaciones
  arte/             ← los adornos ilustrados (ya vienen)
  fotos/            ← aquí van las fotos (vacía)
```

## Las dos ligas

| | Liga | Para quién |
|---|---|---|
| Invitación | `saveystudio.com/i/vtmus/` | Los invitados |
| Panel | `saveystudio.com/i/vtmus/lista/` | Estefanía y tú |

Las dos cuelgan del folio, y `/i/` ya está bloqueado en el `robots.txt`,
así que Google no las indexa. Tampoco están enlazadas desde ningún lado
del sitio: solo llega quien tenga la liga.

## Dónde va el `.exec` de la hoja

**No necesitas hoja ni script nuevos.** Tu Apps Script de confirmaciones
ya es multi-evento: separa por `slug`, y `cami-3` va a aparecer solo en
cuanto llegue la primera respuesta. El de cuestionarios es otro archivo
aparte y no se toca.

Lo único que hay que hacer es pegar la URL `/exec` de **la hoja de
confirmaciones** en dos lugares:

**1. `index.html`** — hasta abajo, en el bloque `DATOS DE ESTE EVENTO`:

```js
var ENDPOINT = '';                /* ←←← PEGA AQUÍ EL .exec ←←← */
```

**2. `lista/index.html`** — arriba del `<script>`:

```js
var ENDPOINT = '';   /* ←←← PEGA AQUÍ EL .exec ←←← */
```

### Lo que manda esta invitación

Va con los nombres que espera tu script, no con otros:

| Se manda | Cae en la columna |
|---|---|
| `slug: 'cami-3'` | `evento` |
| `evento: 'María Camila cumple 3 años'` | `titulo` |
| `nombre`, `asiste`, `adultos`, `ninos`, `mensaje` | iguales |
| `codigo`, `pase`, `lugares` | vacías (son de Oro en adelante) |

`personas` lo calcula tu script solo. También manda `folio: 'VTMUS'`,
que se abre como columna nueva la primera vez.

### Si quieres proteger el panel con clave

Tu script ya lo soporta. En Apps Script → Configuración → Propiedades
del script, agrega `CLAVES` con el valor `cami-3:loquesea`. Luego en
`lista/index.html` pon esa misma clave:

```js
var CLAVE = 'loquesea';
```

Los eventos que no estén listados en `CLAVES` siguen abriendo directo.

## Las fotos

Súbelas a `fotos/` con estos nombres:

| Archivo | Dónde sale |
|---|---|
| `boton.png` | El medallón de la pantalla de apertura |
| `cami.webp` | Dentro del marco dorado |
| `g1.webp` … `g4.webp` | Las cuatro polaroids |

No hace falta ponerlas todas: cada hueco detecta si falta su archivo y
deja un marcador discreto. Si falta `boton.png`, el medallón muestra la
estrella de sheriff.

## Lo que falta

1. **Las fotos** (arriba).
2. **El pin de Google Maps.** En `index.html`, busca `maps.google.com` y
   cambia el enlace por el pin exacto del salón.
3. **El `.exec`** de la hoja de confirmaciones en los dos archivos.
4. **Las actividades.** La sección está puesta pero con una pizarra que
   dice «muy pronto», tal como pediste. Cuando Estefanía confirme el
   programa: borra el `<div class="pizarra">` y quita los comentarios de
   la lista `<ol class="programa">` que está justo abajo. Ya tiene estilos.
5. **La fecha límite para confirmar.** Puse el 1 de noviembre. Si no es
   esa, búscala en `index.html` y en la sección de confirmación.

## El panel

Muestra personas confirmadas, adultos, niños y cuántas familias no van;
una tabla con el mensajito de cada quien; buscador que ignora acentos;
filtros de sí/no; y un botón para descargar todo en CSV. Se actualiza
solo cada dos minutos mientras la pestaña esté abierta.

**No tiene contraseña.** Cualquiera con la liga ve los nombres de los
invitados. Para un cumpleaños suele estar bien, pero si te preocupa, lo
más rápido es cambiarle el nombre a la carpeta por algo que nadie
adivine (por ejemplo `lista-9k3m/` en vez de `lista/`).

## Lo que no lleva, y por qué

- **Sin álbum compartido ni código QR**: eso es Oro en adelante.
- **Sin pases por familia ni control de entrada**: también es Oro.
- **Sin música**: no venía en el paquete y además arranca sola en el
  celular, que molesta más de lo que suma.

## Sobre el arte

Los adornos de `arte/` son los que mandaste: el marco, la guirnalda, la
cuerda con moños, la estrella de sheriff y la herradura. Los demás
detalles —botita, pañuelo, corazones, el moño del número 3 y los íconos—
son dibujos originales hechos para Savey.

El archivo del sombrero con orejas de ratón no se usó: esa silueta es de
Disney. Si quieres ponerlo en el medallón, súbelo tú a `fotos/boton.png`.
