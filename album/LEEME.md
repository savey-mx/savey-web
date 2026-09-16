# Álbum compartido de Savey

Tres piezas:

```
album/index.html   la página que ven los invitados
album/worker.js    el receptor en Cloudflare
album/tarjeta.html tarjeta imprimible con QR para las mesas
```

## Lo que hay que configurar

**En `worker.js`**, al desplegarlo en Cloudflare:
- binding de R2 llamado `ALBUM`
- variable `LLAVE` con tu contraseña para borrar
- variable `EVENTOS` con los slugs permitidos, separados por comas

**En `album/index.html`**, línea con `var API =` → la URL de tu Worker.

**El objeto `EVENTOS`** dentro de `index.html` define título y colores por evento.
Para agregar uno nuevo, una línea:

```js
"boda-lopez": { titulo:"La boda de Ana y Luis", acento:"#B0873F", fondo:"#F2EDE1", tinta:"#1B241B" }
```

Y agregar el mismo slug a la variable `EVENTOS` del Worker.

## Costos

R2 regala 10 GB de almacenamiento, 1 millón de escrituras y 10 millones de
lecturas al mes, y **no cobra por descarga**, que es donde los demás cobran caro.
Con la compresión que hace el celular antes de subir (máximo 1600 px, calidad 82),
cada foto pesa unos 300 kB. Un evento de 100 invitados con 30 fotos cada uno
son unos 900 MB: caben once eventos en el plan gratuito.

## Borrar una foto

```
https://TU-WORKER.workers.dev/f/EVENTO/ARCHIVO.jpg?k=TU_LLAVE
```
con método DELETE. Desde la consola del navegador:

```js
fetch('https://TU-WORKER.workers.dev/f/regina-5/abc123.jpg?k=TU_LLAVE',{method:'DELETE'})
```
