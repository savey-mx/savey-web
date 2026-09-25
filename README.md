# Savey Studio

Sitio público de Savey. Vive en **saveystudio.com**, alojado en Hostinger
y publicado desde este repositorio.

```
/                      Landing con el catálogo de 54 diseños
/catalogo/             Índice de las nueve categorías
/catalogo/<cat>/       Subpágina con los 6 diseños de esa categoría (liga para compartir)
/i/?e=SLUG             Motor de invitaciones (25 eventos de muestra)
/i/boda-*/             6 bodas hechas a la medida
/i/xv-*/               6 XV años hechos a la medida (motor en /i/motor/)
/i/bautizo-*/          6 bautizos hechos a la medida
/i/cumple-*/           6 cumpleaños infantiles (ci-) y 6 de adulto (cg-)
/i/grad-*/             6 graduaciones
/i/corp-*/             6 eventos de empresa
/i/temporada-*/        6 fiestas de temporada
/i/otros-*/            6 de todo lo demás (kermés, concierto, ponencia, teatro, galería, torneo)
/brief/                Cuestionario para cotizar (enlazado desde la landing)
/album/                Álbum compartido de fotos del evento
/generador.html        Herramienta interna para dar de alta eventos
/aviso-de-privacidad.html, /terminos.html
```

## Las invitaciones vendidas no viven aquí

Regina y Tamara están en un repositorio aparte, publicado en **savey.pro**
(Netlify), porque sus ligas ya se repartieron y no pueden cambiar. Cuando
pasen sus eventos, ese dominio se puede apagar.

| Dominio | Aloja | Sirve |
|---|---|---|
| saveystudio.com | Hostinger | Este repositorio |
| savey.pro | Netlify | Solo Regina y Tamara |

## Alojamiento

Son archivos estáticos: no hay compilación ni servidor. El `.htaccess`
fuerza HTTPS, quita el `www`, comprime, define la caché y marca como
`noindex` las rutas `/brief/`, `/album/` e `/i/`.

En Hostinger la carpeta de publicación es `public_html`.

## Dar de alta un evento nuevo

1. Abrir `generador.html` con doble clic.
2. Llenar los datos y la lista de invitados.
3. **Generar** → **Descargar JSON**.
4. Guardar en `i/eventos/` y la foto en `i/fotos/`.
5. `git add -A && git commit && git push`.

La liga de cada familia queda `https://saveystudio.com/i/?e=SLUG&c=CODIGO`.

## Servicios conectados

| Qué | Dónde | Cómo se configura |
|---|---|---|
| Cuestionario | Google Apps Script | `ENDPOINT` en `brief/index.html` |
| Confirmaciones | Google Apps Script | `rsvpEndpoint` en cada JSON de `i/eventos/` |
| Álbum de fotos | Cloudflare Worker + R2 | `API` en `album/index.html` |

El código del Worker está en `album/worker.js`, junto con su `LEEME.md`.

## Catálogo por categoría

Cada categoría tiene su propia liga para mandarla al mercado que le toca:

| Categoría | Liga |
|---|---|
| Bodas | saveystudio.com/catalogo/bodas/ |
| XV Años | saveystudio.com/catalogo/xv/ |
| Bautizos | saveystudio.com/catalogo/bautizos/ |
| Cumpleaños infantil | saveystudio.com/catalogo/ninos/ |
| Cumpleaños | saveystudio.com/catalogo/teens/ |
| Graduación | saveystudio.com/catalogo/graduacion/ |
| Corporativo | saveystudio.com/catalogo/empresa/ |
| De Temporada | saveystudio.com/catalogo/temporada/ |
| Otros | saveystudio.com/catalogo/otros/ |

Las nueve comparten `/catalogo/catalogo.css` y `/catalogo/catalogo.js`, y cada
una lleva su propia tarjeta de vista previa en `/catalogo/og/<cat>.jpg` para
que la liga se vea bien al mandarla por WhatsApp.

El contenido sale del mismo arreglo `CATALOGO` que usa la landing: si se
agrega un diseño ahí, hay que volver a generar las subpáginas para que
aparezca también en ellas.

Para regenerarlas, desde la raíz del repositorio:

```
python3 herramientas/generar-catalogo.py      # las diez páginas
python3 herramientas/generar-og-catalogo.py   # las tarjetas de vista previa
```
