# VTMUS · María Camila cumple 3

Paquete **Plata** · Estefanía Alemán (+52 444 384 3993) · domingo 15 de
noviembre de 2026, 2:30 p. m.

```
vtmus/
  index.html        ← la invitación
  lista/index.html  ← el panel de confirmaciones
  apps-script.gs    ← el código para la hoja de cálculo
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

**En dos archivos, la misma URL.** Búscala como `ENDPOINT`:

**1. `index.html`** — hasta abajo, en el bloque `DATOS DE ESTE EVENTO`:

```js
var WA       = '5214443843993';
var ENDPOINT = '';                /* ←←← PEGA AQUÍ EL .exec ←←← */
```

**2. `lista/index.html`** — arriba del `<script>`:

```js
var ENDPOINT = '';   /* ←←← PEGA AQUÍ EL .exec ←←← */
```

El archivo `apps-script.gs` trae el código de la hoja y las instrucciones
de instalación. Ya está escrito para estas columnas exactas:

```
recibido  evento  titulo  codigo  pase  nombre
asiste  personas  adultos  ninos  lugares  mensaje
```

`codigo`, `pase` y `lugares` van vacías a propósito: son de pases por
familia, que es Oro en adelante. Las dejé en la hoja para que todos tus
eventos usen el mismo formato.

Si dejas `ENDPOINT` vacío, la invitación sigue funcionando: el recuadro
final le ofrece al invitado avisar por WhatsApp. Pero entonces el panel
no tiene de dónde leer.

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
3. **El `.exec`** en los dos archivos.
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
