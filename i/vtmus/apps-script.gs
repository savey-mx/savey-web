/**
 * Savey · hoja de confirmaciones
 * ───────────────────────────────────────────────────────────────
 * Cómo se instala:
 *
 *  1. Abre la hoja de cálculo de Google donde quieras las
 *     confirmaciones. La primera fila debe tener exactamente
 *     estos encabezados, en este orden:
 *
 *     recibido | evento | titulo | codigo | pase | nombre |
 *     asiste | personas | adultos | ninos | lugares | mensaje
 *
 *  2. Extensiones → Apps Script. Borra lo que haya y pega todo
 *     este archivo.
 *
 *  3. Implementar → Nueva implementación → Aplicación web
 *       · Ejecutar como:   Yo
 *       · Quién tiene acceso:  Cualquier persona
 *     (Tiene que ser «cualquier persona»: los invitados no
 *      inician sesión con Google para confirmar.)
 *
 *  4. Copia la URL que te da, la que termina en /exec, y pégala
 *     en DOS lugares:
 *       · index.html          → variable ENDPOINT
 *       · lista/index.html    → variable ENDPOINT
 *     Es la misma URL en los dos.
 *
 *  Cada vez que cambies este código tienes que volver a
 *  «Implementar → Administrar implementaciones → Editar → Nueva
 *  versión», si no, sigue corriendo el código viejo.
 */

var COLUMNAS = ['recibido','evento','titulo','codigo','pase','nombre',
                'asiste','personas','adultos','ninos','lugares','mensaje'];

function hoja_() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
}

/* ── Guardar una confirmación ── */
function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var fila = COLUMNAS.map(function (c) {
      if (c === 'recibido') return new Date();
      return d[c] != null ? d[c] : '';
    });
    hoja_().appendRow(fila);
    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

/* ── Leer la lista para el panel ── */
function doGet(e) {
  try {
    var h = hoja_();
    var datos = h.getDataRange().getValues();
    if (datos.length < 2) return json_([]);

    var enc = datos[0].map(function (x) { return String(x).trim().toLowerCase(); });
    var filtro = (e && e.parameter && e.parameter.evento) || '';
    var salida = [];

    for (var i = 1; i < datos.length; i++) {
      var fila = {};
      for (var j = 0; j < enc.length; j++) {
        var v = datos[i][j];
        fila[enc[j]] = (v instanceof Date) ? v.toISOString() : v;
      }
      if (!fila.nombre) continue;                       // filas vacías, fuera
      if (filtro && fila.evento && fila.evento !== filtro) continue;
      salida.push(fila);
    }
    return json_(salida);
  } catch (err) {
    return json_({ error: String(err) });
  }
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

/* ── Opcional: pon los encabezados de un jalón ──
   Corre esta función una sola vez desde el editor si la hoja
   está en blanco. */
function ponerEncabezados() {
  var h = hoja_();
  h.getRange(1, 1, 1, COLUMNAS.length).setValues([COLUMNAS]);
  h.getRange(1, 1, 1, COLUMNAS.length).setFontWeight('bold');
  h.setFrozenRows(1);
}
