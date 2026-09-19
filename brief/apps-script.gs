/**
 * SAVEY · Receptor del cuestionario de diseño
 * ═══════════════════════════════════════════════════════════
 * Pégalo completo en Extensiones → Apps Script de tu hoja.
 * Crea solo la pestaña "Cuestionarios" si no existe.
 * No toca ninguna otra pestaña del archivo.
 * ═══════════════════════════════════════════════════════════
 */

var PESTANA = 'Cuestionarios';

// Orden de las columnas. Si algún día agregas una pregunta nueva
// al formulario, su columna se abre sola al final.
var ORDEN = [
  'enviado', 'folio', 'paquete', 'evento', 'evento_otro',
  'contacto', 'whatsapp', 'correo', 'relacion', 'comonos',
  'nombres', 'edad', 'empresa', 'fecha', 'hora', 'ciudad',
  'invitados_aprox', 'frase',
  'sede1_tipo', 'sede1_nombre', 'sede1_dir', 'sede1_hora',
  'sede2_nombre', 'sede2_dir', 'sede2_hora', 'itinerario',
  'secciones', 'padres', 'padrinos', 'dress', 'dress_nota',
  'regalos_texto', 'regalos_tiendas', 'regalos_cuenta',
  'hospedaje', 'transporte', 'hashtag', 'notas_papas',
  'actividades', 'programa', 'registro', 'extra',
  'plantilla', 'plantilla_ref', 'colores', 'ambiente', 'musica', 'fotos_cuantas',
  'lista', 'lista_tel', 'lista_despues', 'origen'
];


function doPost(e) {
  var candado = LockService.getScriptLock();
  candado.waitLock(20000);
  try {
    var datos = JSON.parse(e.postData.contents);
    var libro = SpreadsheetApp.getActiveSpreadsheet();

    // Si la pestaña no existe, la creamos con sus encabezados
    var hoja = libro.getSheetByName(PESTANA);
    if (!hoja) {
      hoja = libro.insertSheet(PESTANA);
      hoja.appendRow(ORDEN);
      hoja.getRange(1, 1, 1, ORDEN.length)
          .setFontWeight('bold')
          .setBackground('#F7F2EA');
      hoja.setFrozenRows(1);
      hoja.setColumnWidths(1, ORDEN.length, 160);
    }
    if (hoja.getLastRow() === 0) {
      hoja.appendRow(ORDEN);
      hoja.getRange(1, 1, 1, ORDEN.length)
          .setFontWeight('bold').setBackground('#F7F2EA');
      hoja.setFrozenRows(1);
    }

    // Si llegó una respuesta que no tiene columna, se la abrimos
    var cabeceras = hoja.getRange(1, 1, 1, hoja.getLastColumn())
                        .getValues()[0].map(String);
    Object.keys(datos).forEach(function (clave) {
      if (cabeceras.indexOf(clave) === -1) {
        cabeceras.push(clave);
        hoja.getRange(1, cabeceras.length).setValue(clave)
            .setFontWeight('bold').setBackground('#F7F2EA');
      }
    });

    hoja.appendRow(cabeceras.map(function (c) { return datos[c] || ''; }));

    // Aviso por correo para no vivir revisando la hoja
    var correo = Session.getEffectiveUser().getEmail();
    if (correo) {
      MailApp.sendEmail(
        correo,
        'Savey · cuestionario nuevo: ' + (datos.evento || '') + ' — ' + (datos.nombres || ''),
        [
          'Folio:        ' + (datos.folio || ''),
          'Paquete:      ' + (datos.paquete || ''),
          'Evento:       ' + (datos.evento || ''),
          'Fecha:        ' + (datos.fecha || ''),
          'Ciudad:       ' + (datos.ciudad || ''),
          'Invitados:    ' + (datos.invitados_aprox || ''),
          '',
          'Contacto:     ' + (datos.contacto || ''),
          'WhatsApp:     ' + (datos.whatsapp || ''),
          'Escribirle:   https://wa.me/' + String(datos.whatsapp || '').replace(/\D/g, ''),
          'Correo:       ' + (datos.correo || ''),
          '',
          'Abrir la hoja: ' + libro.getUrl()
        ].join('\n')
      );
    }

    return ContentService.createTextOutput('ok');

  } catch (error) {
    return ContentService.createTextOutput('error: ' + error);
  } finally {
    candado.releaseLock();
  }
}


// Sirve para comprobar desde el navegador que el endpoint está vivo
function doGet() {
  return ContentService.createTextOutput('Savey · endpoint activo');
}
