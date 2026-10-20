# 226ZF · Mario cumple 22

Paquete **Oro** · sábado 7 de noviembre de 2026, 5:00 pm · Fiesta Equivocada

```
i/226zf/
  index.html        la invitación
  lista/index.html  el panel de confirmaciones
  fotos/            las ocho fotos, ya procesadas
```

## Las dos ligas

| | Liga |
|---|---|
| Invitación | `saveystudio.com/i/226zf/` |
| Panel | `saveystudio.com/i/226zf/lista/` |

Es **una sola liga para todos**: quitamos los pases personalizados. Cada quien
escribe su nombre y cuántos lugares aparta, hasta 6. Si algún día quieres
subir o bajar ese tope, en `index.html` está la línea `maxSinPase:6`.

## Lo que falta llenar

### 1. El `.exec` de la hoja

En `index.html`, dentro de `window.XV`:

```js
endpoint:'',   /* ←←← Pega aquí el .exec ←←← */
```

Y el mismo en `lista/index.html`, en la variable `ENDPOINT`.

Es la URL del Apps Script de **confirmaciones** (el multi-evento, no el de
cuestionarios). `226zf` va a aparecer solo en la hoja en cuanto llegue la
primera respuesta.

Si lo dejas vacío, la invitación sigue sirviendo: el recuadro final ofrece
avisar por WhatsApp a tu número.

### 2. El álbum compartido

Ya di de alta `226zf` en `album/index.html`. Falta una cosa en Cloudflare;
los pasos están abajo.

### 3. Los rótulos de la galería

Los que están son inventos míos: «Venía de una kermés», «Venía a cazar
fantasmas», «Venía de un safari, según él». Cámbialos por lo que de verdad
te haga reír; están marcados con un comentario en el HTML, en la sección
`<!-- Galería -->`.

## El álbum, paso a paso

El álbum ya existe y ya está desplegado desde la fiesta de Cami: el Worker
vive en `savey-album.savey-mx.workers.dev` y las fotos se guardan en R2. Lo
único que puede faltar es darle permiso a este evento.

**Paso 1 — sube los archivos.** `i/226zf/` y `album/index.html` (ese último
ya trae el renglón de `226zf` con tus colores). Haz el push como siempre.

**Paso 2 — pruébalo antes de tocar Cloudflare.** Abre en tu teléfono:

```
saveystudio.com/album/?e=226zf
```

Sube una foto cualquiera.

- Si aparece → **ya está, no hay paso 3.** Es lo más probable: el Worker
  solo filtra si le pusiste la variable `EVENTOS`, y si la dejaste vacía
  deja pasar todos los eventos.
- Si sale un error de que el evento no está permitido → sigue al paso 3.

**Paso 3 — solo si falló.** Entra a `dash.cloudflare.com` → *Workers &
Pages* → **savey-album** → pestaña *Settings* → *Variables and Secrets*.
Busca la variable `EVENTOS`. Edítala y agrega `,226zf` al final, sin
espacios. Te va a quedar algo así:

```
vtmus,226zf
```

Dale *Save and deploy* y espera unos segundos. Vuelve al paso 2.

**Para borrar una foto** (si alguien sube algo que no va), abre esta liga en
el navegador, cambiando el nombre del archivo y tu llave:

```
https://savey-album.savey-mx.workers.dev/f/226zf/ARCHIVO.jpg?k=TU_LLAVE
```

`TU_LLAVE` es la variable `LLAVE` del Worker, la misma que pusiste cuando lo
desplegaste.

**El espacio no es problema.** R2 te da 10 GB gratis, un millón de subidas y
diez millones de vistas al mes, y no cobra por descarga. Una fiesta normal no
llega ni al 1%.

## Lo que ya lleva

- Cuenta regresiva, código de vestimenta y galería: las tres secciones que
  pediste.
- **Álbum compartido**, que es de Oro.
- Visor de fotos a pantalla completa.
- Botón para agendar en el calendario y mapa a tu casa.
- Confirmación con contador de lugares y campo libre («¿de qué fiesta vas a
  venir?»), que te va a servir para saber qué esperar.

## El diseño

Minimalista, como pediste, con tu paleta exacta: los tres naranjas
(`#DF7117`, `#BB4E08`, `#FF992C`) y los tres verdes (`#6BC4A6`, `#005236`,
`#20686C`). Tipografía Space Grotesk, que es geométrica y no estorba.

El chiste visual está en tres lugares: la pantalla de carga va rotando
temáticas («¿Fiesta de disfraces?», «¿Pijamada?»…) como si no supiera cuál
es; la portada tacha tres temáticas antes de decir que vengas de la que
quieras; y la galería presenta tus fotos como pruebas de que esto ya te
pasaba.

## Save the date

Oro lo incluye y no lo pediste, pero si lo quieres es rápido: una versión
corta de la portada con la fecha y nada más, para mandar antes. Dime y la
armo.
