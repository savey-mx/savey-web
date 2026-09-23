# Savey Studio

Sitio público de Savey. Vive en **saveystudio.com**, alojado en Hostinger
y publicado desde este repositorio.

```
/                      Landing con el catálogo de 35 diseños
/i/?e=SLUG             Motor de invitaciones (25 eventos de muestra)
/i/boda-*/             6 bodas hechas a la medida
/i/xv-*/               6 XV años hechos a la medida (motor en /i/motor/)
/i/bautizo-*/          6 bautizos hechos a la medida
/i/cumple-*/           6 cumpleaños infantiles hechos a la medida
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
