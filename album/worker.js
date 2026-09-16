/**
 * SAVEY · Álbum compartido
 * ═══════════════════════════════════════════════════════════════
 * Worker de Cloudflare con R2 pegado directo.
 * Recibe fotos de los invitados, las lista y las sirve.
 *
 * Rutas:
 *   POST   /u/:evento          sube una foto  (cuerpo = bytes de la imagen)
 *   GET    /l/:evento          lista las fotos en JSON
 *   GET    /f/:evento/:archivo entrega una foto
 *   DELETE /f/:evento/:archivo?k=LLAVE   borra (solo tú)
 *
 * Variables que hay que configurar en el panel del Worker:
 *   ALBUM      → binding al bucket de R2
 *   LLAVE      → tu contraseña para borrar fotos
 *   EVENTOS    → lista separada por comas de los slugs permitidos
 * ═══════════════════════════════════════════════════════════════
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, X-Quien',
  'Access-Control-Max-Age': '86400'
};

const MAX_BYTES = 8 * 1024 * 1024;   // 8 MB por foto, de sobra tras comprimir

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...CORS }
  });
}

function permitido(evento, env) {
  const lista = (env.EVENTOS || '').split(',').map(s => s.trim()).filter(Boolean);
  if (!lista.length) return true;              // sin lista, todo pasa
  return lista.includes(evento);
}

function nombreArchivo() {
  const t = Date.now().toString(36);
  const r = Math.random().toString(36).slice(2, 8);
  return `${t}-${r}`;
}

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') return new Response(null, { headers: CORS });

    const url = new URL(request.url);
    const partes = url.pathname.split('/').filter(Boolean);
    const accion = partes[0];
    const evento = partes[1];

    if (!accion || !evento) return json({ error: 'ruta incompleta' }, 400);
    if (!/^[a-z0-9\-]{2,40}$/.test(evento)) return json({ error: 'evento inválido' }, 400);

    /* ─────────── Subir ─────────── */
    if (accion === 'u' && request.method === 'POST') {
      if (!permitido(evento, env)) return json({ error: 'evento no habilitado' }, 403);

      const tipo = request.headers.get('content-type') || '';
      if (!tipo.startsWith('image/')) return json({ error: 'solo imágenes' }, 415);

      const bytes = await request.arrayBuffer();
      if (!bytes.byteLength) return json({ error: 'archivo vacío' }, 400);
      if (bytes.byteLength > MAX_BYTES) return json({ error: 'la foto pesa demasiado' }, 413);

      const ext = tipo.includes('png') ? 'png' : tipo.includes('webp') ? 'webp' : 'jpg';
      const clave = `${evento}/${nombreArchivo()}.${ext}`;
      const quien = (request.headers.get('X-Quien') || '').slice(0, 60);

      await env.ALBUM.put(clave, bytes, {
        httpMetadata: { contentType: tipo, cacheControl: 'public, max-age=31536000' },
        customMetadata: { quien, cuando: new Date().toISOString() }
      });

      return json({ ok: true, archivo: clave.split('/')[1] });
    }

    /* ─────────── Listar ─────────── */
    if (accion === 'l' && request.method === 'GET') {
      const salida = [];
      let cursor;
      do {
        const r = await env.ALBUM.list({ prefix: `${evento}/`, limit: 1000, cursor, include: ['customMetadata'] });
        for (const o of r.objects) {
          salida.push({
            archivo: o.key.split('/')[1],
            quien: (o.customMetadata && o.customMetadata.quien) || '',
            cuando: (o.customMetadata && o.customMetadata.cuando) || o.uploaded,
            peso: o.size
          });
        }
        cursor = r.truncated ? r.cursor : undefined;
      } while (cursor);

      salida.sort((a, b) => (a.cuando < b.cuando ? 1 : -1));   // lo más nuevo arriba
      return json({ total: salida.length, fotos: salida });
    }

    /* ─────────── Entregar una foto ─────────── */
    if (accion === 'f' && request.method === 'GET') {
      const archivo = partes[2];
      if (!archivo) return json({ error: 'falta el archivo' }, 400);

      const obj = await env.ALBUM.get(`${evento}/${archivo}`);
      if (!obj) return json({ error: 'no existe' }, 404);

      const h = new Headers(CORS);
      obj.writeHttpMetadata(h);
      h.set('etag', obj.httpEtag);
      h.set('Cache-Control', 'public, max-age=31536000, immutable');
      return new Response(obj.body, { headers: h });
    }

    /* ─────────── Borrar (solo tú) ─────────── */
    if (accion === 'f' && request.method === 'DELETE') {
      if (url.searchParams.get('k') !== env.LLAVE) return json({ error: 'no autorizado' }, 401);
      const archivo = partes[2];
      await env.ALBUM.delete(`${evento}/${archivo}`);
      return json({ ok: true });
    }

    return json({ error: 'ruta desconocida' }, 404);
  }
};
