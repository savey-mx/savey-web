# MLZQX · Blessingway de Gaby

Paquete **Plata** · sábado 5 de diciembre de 2026, 11:00 am · Miraval I, Lomas Verdes

```
i/mlzqx/
  index.html        la invitación
  lista/index.html  el panel de confirmaciones
  fotos/            las tres fotos, ya procesadas
  musica/           la pista de fondo
```

## Las dos ligas

| | Liga |
|---|---|
| Invitación | `saveystudio.com/i/mlzqx/` |
| Panel | `saveystudio.com/i/mlzqx/lista/` |

Una sola liga para las siete invitadas. Plata no lleva pases por persona.

## Ya quedó conectado

El `.exec` de confirmaciones **ya está puesto** en los dos archivos. Es el
mismo Apps Script multi-evento de vtmus y 226zf, así que `mlzqx` va a aparecer
solo en la hoja en cuanto llegue la primera respuesta. No tienes que pegar nada.

## Lo que necesito de ti

### 1. El WhatsApp de Ana

En la hoja llegó como `#ERROR!`, así que no lo tengo. Lo necesitas para dos
cosas: mandarle la liga, y poner su número en la invitación como respaldo por
si la hoja no contesta. Mientras tanto dejé el de Savey. Está en `index.html`:

```js
wa:'5215618906790',   /* cámbialo por el de Ana */
```

### 2. Confirmar qué es el lugar

Ana cambió la sede a **Miraval I**, que en Google Maps aparece como complejo de
departamentos. El cuestionario original decía «Jardín», así que ya no sé si se
reúnen en un jardín, una terraza o adentro. No lo inventé: el renglón de Lugar
dice la zona y la dirección, y nada más. Si Ana quiere que diga dónde
exactamente, me pasas el dato y lo agrego.

### 3. La fecha límite para confirmar

No venía en el cuestionario. Puse **30 de noviembre**, que da cinco días de
margen. Se cambia en `fechaLimite` de `index.html`.

## Decisiones que tomé y puedes revertir

**La galería es un mosaico cuadrado.** La selfie de espejo va completa a la
izquierda y a la derecha dos chicas apiladas: la pareja arriba, las manos
abajo. La columna de la izquierda es de `1.4fr` justamente para que el conjunto
cierre en cuadro: la foto alta manda la altura y las dos chicas se reparten lo
que queda. Sin rótulos.

**La foto de las manos aparece dos veces**, en la portada y en el mosaico, pero
con encuadres distintos: la portada va abierta y en arco, y la del mosaico es un
recorte cerrado a las manos. Si prefieres que no se repita, dime y la cambio por
otra que tengan.

**Oculté el contador de lugares.** En un círculo de siete, cada invitada
confirma por sí misma y un «¿cuántas vienen?» sobra. El motor registra 1 por
confirmación. Si quieres que puedan traer acompañante, en `index.html` cambia
`maxSinPase:1` por `maxSinPase:2` y borra la línea `[data-lugares]{display:none}`.

**A la frase de Ana solo le acomodé la puntuación.** Venía toda de corrido con
comas; la partí en dos oraciones para que respire. Las palabras son suyas.

**El único texto de la galería** es el encabezado «El camino hasta aquí». Se
cambia en la sección `<!-- Galería -->` de `index.html`.

## El diseño

Blessingway, no baby shower. El adorno que se repite es un **círculo de siete
puntos**, uno por cada mujer de la tribu: aparece en la pantalla de carga
llenándose punto por punto, y luego junto a la frase y en el cierre. La foto de
portada va en **arco**, como un umbral. Paleta de blancos, beige y rosa como
pidió Ana, con tipografía Cormorant Garamond.

La invitación cierra con el nombre de **Alana**, no con el de Gaby. Ese es el
camino que se está honrando.

## La música

«Te Esperaba», de Carlos Rivera, la que pidió Ana. El botón va abajo a la
izquierda, para no pelearse con el de confirmar.

**No arranca sola, a propósito.** Los navegadores bloquean el audio automático
si nadie ha tocado la pantalla, y aunque se pudiera, una página que suena de
golpe se cierra más de lo que se escucha. En pausa el botón late despacio para
que se note que se puede tocar. Si de todos modos la quieres automática, dime y
son dos líneas.

Recodifiqué la pista de 4.8 MB a 2.4 MB. Para música de fondo no se nota la
diferencia y en datos móviles sí. Además va con `preload="none"`: solo se baja
si la invitada toca el botón.

**Un apunte de negocio, y lo digo una sola vez.** El archivo viene de un video
de letra y la grabación es de Carlos Rivera y su disquera. Alojarla completa en
tu dominio es distribuirla, que es el mismo terreno del aviso que ya tienes
publicado sobre personajes con derechos de autor. Para una página privada de
siete invitadas el riesgo práctico es mínimo y es lo que hace todo el mercado,
pero si Savey crece vale la pena resolverlo. Dos salidas limpias: licenciar
instrumentales en algún banco de música, o poner un botón que abra la canción
en Spotify en vez de alojarla tú. Tú decides; yo lo dejo armado como lo pidió
Ana.

## Dos cosas más

**Lo que Plata no incluye,** por si Ana pregunta: pases personalizados, álbum
compartido y save the date son de Oro. Las secciones que pidió —cuenta
regresiva, código de vestimenta y galería— están las tres.

**Si Ana quiere pedirles algo a las invitadas** (una cuenta para el collar, una
flor, un deseo escrito: son costumbres comunes en un blessingway), no inventé
nada porque no venía en el cuestionario. Me dices qué va y le agrego una
sección corta.
