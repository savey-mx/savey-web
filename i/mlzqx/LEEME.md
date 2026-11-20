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

**La galería va en forma natural, no recortada a cuadro.** La selfie de espejo
es vertical de teléfono y la de la pareja es casi cuadrada; cada una se muestra
completa con su propia proporción. (Primero había recortado la vertical al
vientre; Mario pidió dejarla entera, y para que de verdad se vea entera hubo que
quitar el recorte cuadrado de la rejilla.)

**Oculté el contador de lugares.** En un círculo de siete, cada invitada
confirma por sí misma y un «¿cuántas vienen?» sobra. El motor registra 1 por
confirmación. Si quieres que puedan traer acompañante, en `index.html` cambia
`maxSinPase:1` por `maxSinPase:2` y borra la línea `[data-lugares]{display:none}`.

**A la frase de Ana solo le acomodé la puntuación.** Venía toda de corrido con
comas; la partí en dos oraciones para que respire. Las palabras son suyas.

**Los rótulos de la galería son míos:** «Esperando a Alana» y «Los que ya la
esperan». Cámbialos por lo que Ana prefiera; están marcados con un comentario
en la sección `<!-- Galería -->`.

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
