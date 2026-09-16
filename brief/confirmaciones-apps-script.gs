/**
 * SAVEY · Receptor de confirmaciones
 * ═══════════════════════════════════════════════════════════════
 * Un solo endpoint para TODAS las invitaciones del sitio.
 * Cada invitación manda su "slug" y el script lo separa solo.
 *
 * Pégalo en Extensiones → Apps Script de una hoja NUEVA,
 * distinta a la de los cuestionarios.
 * ═══════════════════════════════════════════════════════════════
 */

var HOJA = 'Confirmaciones';

// Columnas fijas, en este orden. Cualquier campo que llegue y no esté
// aquí se agrega solo como columna nueva al final.
var BASE = [
  'recibido',    // cuándo entró la confirmación
  'evento',      // slug de la invitación: regina-5, boda-aurora…
  'titulo',      // nombre legible del evento
  'codigo',      // el ?c= de la liga
  'pase',        // familia a la que se le mandó
  'nombre',      // lo que escribió el invitado
  'asiste',      // si / no
  'personas',    // total, calculado
  'adultos',
  'ninos',
  'lugares',
  'mensaje',
  'alergias'
];


function doPost(e) {
  var candado = LockService.getScriptLock();
  candado.waitLock(20000);
  try {
    var d = JSON.parse(e.postData.contents);
    var libro = SpreadsheetApp.getActiveSpreadsheet();
    var hoja = libro.getSheetByName(HOJA);

    if (!hoja) {
      hoja = libro.insertSheet(HOJA);
      hoja.appendRow(BASE);
      hoja.getRange(1, 1, 1, BASE.length)
          .setFontWeight('bold').setBackground('#F7F2EA');
      hoja.setFrozenRows(1);
      hoja.setColumnWidth(1, 150);
      hoja.setColumnWidth(12, 320);
    }
    if (hoja.getLastRow() === 0) {
      hoja.appendRow(BASE);
      hoja.getRange(1, 1, 1, BASE.length)
          .setFontWeight('bold').setBackground('#F7F2EA');
      hoja.setFrozenRows(1);
    }

    // Normalizamos lo que llega de cualquier tipo de invitación
    var fila = {
      recibido: new Date(),
      evento:   d.slug || '',
      titulo:   d.evento || '',
      codigo:   d.codigo || '',
      pase:     d.pase || '',
      nombre:   d.nombre || '',
      asiste:   d.asiste || '',
      adultos:  d.adultos || '',
      ninos:    d.ninos || '',
      lugares:  d.lugares || '',
      mensaje:  d.mensaje || '',
      alergias: d.alergias || ''
    };

    // Total de personas: infantiles mandan adultos+niños, el resto lugares
    if (String(d.asiste).toLowerCase() === 'no') {
      fila.personas = 0;
    } else if (d.adultos !== undefined || d.ninos !== undefined) {
      fila.personas = (parseInt(d.adultos, 10) || 0) + (parseInt(d.ninos, 10) || 0);
    } else {
      fila.personas = parseInt(d.lugares, 10) || 0;
    }

    // Campos que no estaban previstos (canción, transporte, lo que sea)
    Object.keys(d).forEach(function (k) {
      if (['slug', 'evento', 'fecha'].indexOf(k) >= 0) return;
      if (fila[k] === undefined) fila[k] = d[k];
    });

    var cab = hoja.getRange(1, 1, 1, hoja.getLastColumn()).getValues()[0].map(String);
    Object.keys(fila).forEach(function (k) {
      if (cab.indexOf(k) === -1) {
        cab.push(k);
        hoja.getRange(1, cab.length).setValue(k)
            .setFontWeight('bold').setBackground('#F7F2EA');
      }
    });

    hoja.appendRow(cab.map(function (k) {
      return fila[k] !== undefined ? fila[k] : '';
    }));

    return ContentService.createTextOutput('ok');

  } catch (err) {
    return ContentService.createTextOutput('error: ' + err);
  } finally {
    candado.releaseLock();
  }
}


function doGet() {
  return ContentService.createTextOutput('Savey · confirmaciones activo');
}


/* ═══════════════════════════════════════════════════════════════
   MENÚ SAVEY
   Aparece en la barra de la hoja al abrirla.
   ═══════════════════════════════════════════════════════════════ */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Savey')
    .addItem('Generar corte de un evento', 'generarCorte')
    .addItem('Ver resumen de todos los eventos', 'generarResumen')
    .addToUi();
}


/**
 * Crea una pestaña limpia con el estado final de cada familia
 * de un evento. Si alguien confirmó dos veces, gana la última.
 * Esto es lo que se le manda al salón.
 */
function generarCorte() {
  var ui = SpreadsheetApp.getUi();
  var libro = SpreadsheetApp.getActiveSpreadsheet();
  var datos = libro.getSheetByName(HOJA).getDataRange().getValues();
  var cab = datos.shift().map(String);

  var iEvento = cab.indexOf('evento');
  var eventos = {};
  datos.forEach(function (f) { if (f[iEvento]) eventos[f[iEvento]] = true; });
  var lista = Object.keys(eventos).sort();

  if (!lista.length) { ui.alert('Todavía no hay confirmaciones.'); return; }

  var r = ui.prompt('Corte por evento',
    'Escribe el identificador del evento:\n\n' + lista.join('\n'),
    ui.ButtonSet.OK_CANCEL);
  if (r.getSelectedButton() !== ui.Button.OK) return;
  var slug = r.getResponseText().trim();
  if (lista.indexOf(slug) === -1) { ui.alert('No encontré "' + slug + '".'); return; }

  var i = {
    recibido: cab.indexOf('recibido'), codigo: cab.indexOf('codigo'),
    pase: cab.indexOf('pase'), nombre: cab.indexOf('nombre'),
    asiste: cab.indexOf('asiste'), personas: cab.indexOf('personas'),
    adultos: cab.indexOf('adultos'), ninos: cab.indexOf('ninos'),
    mensaje: cab.indexOf('mensaje'), alergias: cab.indexOf('alergias')
  };

  // última respuesta por código; si no trae código, por nombre
  var ultima = {};
  datos.forEach(function (f) {
    if (f[iEvento] !== slug) return;
    var clave = f[i.codigo] || f[i.nombre];
    if (!ultima[clave] || f[i.recibido] > ultima[clave][i.recibido]) ultima[clave] = f;
  });

  var filas = Object.keys(ultima).map(function (k) { return ultima[k]; })
    .sort(function (a, b) { return String(a[i.pase]).localeCompare(String(b[i.pase])); });

  var nombreHoja = 'Corte · ' + slug;
  var h = libro.getSheetByName(nombreHoja);
  if (h) h.clear(); else h = libro.insertSheet(nombreHoja);

  h.appendRow(['Familia', 'Quién contestó', 'Asiste', 'Personas',
               'Adultos', 'Niños', 'Alergias', 'Mensaje', 'Cuándo']);
  h.getRange(1, 1, 1, 9).setFontWeight('bold').setBackground('#F7F2EA');
  h.setFrozenRows(1);

  var si = 0, no = 0, personas = 0;
  filas.forEach(function (f) {
    var asiste = String(f[i.asiste]).toLowerCase() === 'si';
    if (asiste) { si++; personas += Number(f[i.personas]) || 0; } else { no++; }
    h.appendRow([
      f[i.pase], f[i.nombre], asiste ? 'Sí' : 'No', f[i.personas],
      f[i.adultos], f[i.ninos], f[i.alergias], f[i.mensaje], f[i.recibido]
    ]);
  });

  h.appendRow([]);
  h.appendRow(['TOTALES', '', 'Confirmadas: ' + si, personas + ' personas',
               '', '', '', 'No asisten: ' + no, new Date()]);
  h.getRange(h.getLastRow(), 1, 1, 9).setFontWeight('bold').setBackground('#EDE3D2');
  h.autoResizeColumns(1, 9);

  libro.setActiveSheet(h);
  SpreadsheetApp.getUi().alert(
    'Corte de ' + slug + '\n\n' +
    si + ' familias confirmadas · ' + personas + ' personas\n' +
    no + ' avisaron que no pueden');
}


/** Tabla con el estado de todos los eventos vivos a la vez. */
function generarResumen() {
  var libro = SpreadsheetApp.getActiveSpreadsheet();
  var datos = libro.getSheetByName(HOJA).getDataRange().getValues();
  var cab = datos.shift().map(String);
  var iE = cab.indexOf('evento'), iT = cab.indexOf('titulo'),
      iA = cab.indexOf('asiste'), iP = cab.indexOf('personas'),
      iC = cab.indexOf('codigo'), iR = cab.indexOf('recibido'),
      iN = cab.indexOf('nombre');

  var ev = {};
  datos.forEach(function (f) {
    var s = f[iE]; if (!s) return;
    if (!ev[s]) ev[s] = { titulo: f[iT], vistos: {}, ultima: f[iR] };
    var clave = f[iC] || f[iN];
    if (!ev[s].vistos[clave] || f[iR] > ev[s].vistos[clave][iR]) ev[s].vistos[clave] = f;
    if (f[iR] > ev[s].ultima) ev[s].ultima = f[iR];
  });

  var h = libro.getSheetByName('Resumen');
  if (h) h.clear(); else h = libro.insertSheet('Resumen', 0);
  h.appendRow(['Evento', 'Nombre', 'Familias que contestaron',
               'Confirmadas', 'No asisten', 'Personas', 'Última respuesta']);
  h.getRange(1, 1, 1, 7).setFontWeight('bold').setBackground('#F7F2EA');
  h.setFrozenRows(1);

  Object.keys(ev).sort().forEach(function (s) {
    var si = 0, no = 0, per = 0, n = 0;
    Object.keys(ev[s].vistos).forEach(function (k) {
      var f = ev[s].vistos[k]; n++;
      if (String(f[iA]).toLowerCase() === 'si') { si++; per += Number(f[iP]) || 0; }
      else no++;
    });
    h.appendRow([s, ev[s].titulo, n, si, no, per, ev[s].ultima]);
  });
  h.autoResizeColumns(1, 7);
  libro.setActiveSheet(h);
}
