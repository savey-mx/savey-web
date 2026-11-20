# MLZQX · Blessingway de Gaby

Paquete **Plata** · sábado 5 de diciembre de 2026, 1:00 pm · Centro Rena-Ser

```
i/mlzqx/
  index.html        la invitación
  lista/index.html  el panel de confirmaciones
  fotos/            las tres fotos, ya procesadas
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

### 2. Confirmar la dirección

Ana escribió «Avenida Lomas Verdes 48 / posible cambio». Puse la dirección tal
cual, sin el «posible cambio», porque eso no se le dice a la invitada. Si
cambia, se ajusta en dos lugares de `index.html`: el renglón de **Lugar** y la
liga del botón **Cómo llegar**.

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

## Dos cosas que vale la pena que sepas

**Música.** La landing promete música en los tres paquetes y el cuestionario
decía «Acepto propuestas», pero ninguna plantilla del catálogo tiene música
todavía. Si quieres cumplirlo aquí, dime y le pongo un reproductor discreto;
nada más necesito que elijas la pista, porque no puedo conseguirte una con
licencia desde acá.

**Lo que Plata no incluye,** por si Ana pregunta: pases personalizados, álbum
compartido y save the date son de Oro. Las secciones que pidió —cuenta
regresiva, código de vestimenta y galería— están las tres.

**Si Ana quiere pedirles algo a las invitadas** (una cuenta para el collar, una
flor, un deseo escrito: son costumbres comunes en un blessingway), no inventé
nada porque no venía en el cuestionario. Me dices qué va y le agrego una
sección corta.
