import json, os, unicodedata

OUT = "i/eventos"
os.makedirs(OUT, exist_ok=True)

def mapa(d): 
    from urllib.parse import quote
    return "https://maps.google.com/?q=" + quote(d)

MESES = ["enero","febrero","marzo","abril","mayo","junio","julio",
         "agosto","septiembre","octubre","noviembre","diciembre"]
DIAS = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

def fechas(iso, dia_semana):
    y, m, d = iso.split("T")[0].split("-")
    largo = f"{dia_semana} {int(d)} de {MESES[int(m)-1]} de {y}"
    corto = f"{d} · {m} · {y[2:]}"
    return largo, corto

PASES = {
  "A7K9": {"nombre": "Familia González", "lugares": 4},
  "B2M5": {"nombre": "Daniel y Andrea",  "lugares": 2},
  "C8T1": {"nombre": "Familia Ramírez",  "lugares": 5},
  "D4X6": {"nombre": "Familia Herrera",  "lugares": 3},
}

WA = "5215500000000"

E = []

# Las 5 bodas son plantillas hechas a la medida en i/boda-*/ y no se generan aquí.

# ═══════════════════════ XV AÑOS ═══════════════════════
E += [
 dict(slug="xv-encanto", plantilla="encanto", tipo="Mis XV años", nombre="Valentina",
   fecha="2026-11-14T19:00:00-06:00", dia="Sábado",
   colores=dict(fondo="#1B241B", papel="#F2EDE1", acento="#D9BB80", suave="#8C9B7E"),
   frase="Hay días que se sueñan durante años. Este es el mío, y quiero vivirlo contigo.",
   ceremonia=dict(titulo="Misa de acción de gracias", lugar="Parroquia de San Juan Bautista", direccion="Av. Hidalgo 210, Centro, Metepec, Edo. Méx.", hora="7:00 PM"),
   recepcion=dict(titulo="Recepción", lugar="Jardín Los Encinos", direccion="Carretera Toluca–Tenango km 4.5, Edo. Méx.", hora="9:00 PM"),
   itinerario=[("7:00 PM","Misa"),("9:00 PM","Recepción y cóctel"),("10:00 PM","Vals"),("10:30 PM","Cena"),("12:00 AM","Baile")],
   dress="Formal", dressNota="Te pedimos reservar el verde olivo para la festejada.",
   regalos="Tu presencia es el regalo. Si deseas tener un detalle, agradecemos la lluvia de sobres.",
   banco="BBVA 0123 4567 8901 2345", titular="María Fernanda Ríos", limite="20 de octubre"),

 dict(slug="xv-aura", plantilla="aura", tipo="Mis XV años", nombre="Regina",
   fecha="2027-02-07T18:00:00-06:00", dia="Domingo",
   colores=dict(fondo="#6B4A4A", papel="#F7EDE9", acento="#E6C3AE", suave="#B08B84"),
   frase="Quince años se cumplen una sola vez. Quiero que estés ahí cuando pase.",
   ceremonia=dict(titulo="Misa", lugar="Santuario de Guadalupe", direccion="Calle Morelos 45, Centro, Querétaro, Qro.", hora="6:00 PM"),
   recepcion=dict(titulo="Recepción", lugar="Quinta Las Rosas", direccion="Camino a Jurica km 2, Querétaro, Qro.", hora="8:00 PM"),
   itinerario=[("6:00 PM","Misa"),("8:00 PM","Recepción"),("8:45 PM","Vals"),("9:30 PM","Cena"),("11:00 PM","Baile"),("1:00 AM","Última canción")],
   dress="Formal", dressNota="Rosa palo reservado para la festejada y sus chambelanes.",
   regalos="Lo que quieras regalar lo recibo con mucho cariño. También hay lluvia de sobres.",
   banco="Santander 4455 6677 8899 0011", titular="Regina Salas Mora", limite="15 de enero"),

 dict(slug="xv-medianoche", plantilla="medianoche", tipo="XV", nombre="Ximena",
   fecha="2026-08-30T20:00:00-05:00", dia="Domingo",
   colores=dict(fondo="#111111", papel="#F5F5F5", acento="#C9C9C9", suave="#8A8A8A"),
   frase="Sin misa, sin protocolo. Música fuerte y la gente que quiero.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Terraza Noir", direccion="Av. Chapultepec 480, Americana, Guadalajara, Jal.", hora="8:00 PM"),
   itinerario=[("8:00 PM","Bienvenida"),("9:00 PM","Cena ligera"),("10:00 PM","DJ"),("12:00 AM","Pastel"),("2:00 AM","Cierre")],
   dress="Negro", dressNota="Código estricto: todo negro. Es parte de la fiesta.",
   regalos="Sin regalos, en serio. Solo vengan.",
   banco="", titular="", limite="15 de agosto"),

 dict(slug="xv-jacaranda", plantilla="jacaranda", tipo="Mis XV años", nombre="Fernanda",
   fecha="2027-04-18T18:30:00-06:00", dia="Domingo",
   colores=dict(fondo="#2E2140", papel="#F2EDF7", acento="#C9A227", suave="#8E7BA8"),
   frase="En la temporada en que florecen las jacarandas, cumplo quince.",
   ceremonia=dict(titulo="Misa de acción de gracias", lugar="Parroquia del Carmen", direccion="Av. Revolución 4, San Ángel, Ciudad de México", hora="6:30 PM"),
   recepcion=dict(titulo="Recepción", lugar="Salón Jacarandas", direccion="Calle Frontera 22, San Ángel, Ciudad de México", hora="8:30 PM"),
   itinerario=[("6:30 PM","Misa"),("8:30 PM","Recepción"),("9:15 PM","Vals"),("10:00 PM","Cena"),("11:30 PM","Baile")],
   dress="Formal", dressNota="Morado y dorado reservados para la corte de honor.",
   regalos="Tu presencia es lo más importante. Si quieres tener un detalle, hay lluvia de sobres.",
   banco="Banamex 3344 5566 7788 9900", titular="Fernanda Vega Cruz", limite="25 de marzo"),

 dict(slug="xv-marfil", plantilla="marfil", tipo="Mis XV años", nombre="Isabella",
   fecha="2026-11-02T19:00:00-06:00", dia="Lunes",
   colores=dict(fondo="#F7F2EA", papel="#332B27", acento="#C7A77A", suave="#8A7B6C"),
   frase="Quiero que este día se sienta como se ve: sencillo, luminoso y muy mío.",
   ceremonia=dict(titulo="Misa", lugar="Capilla de la Purísima", direccion="Calle Allende 12, Centro, San Miguel de Allende, Gto.", hora="7:00 PM"),
   recepcion=dict(titulo="Recepción", lugar="Patio Casa Marfil", direccion="Calle Recreo 30, Centro, San Miguel de Allende, Gto.", hora="8:30 PM"),
   itinerario=[("7:00 PM","Misa"),("8:30 PM","Recepción"),("9:15 PM","Vals"),("10:00 PM","Cena"),("11:30 PM","Baile")],
   dress="Cóctel", dressNota="Tonos neutros. El marfil es de la festejada.",
   regalos="Tu presencia es el regalo. Si deseas tener un detalle, agradecemos la lluvia de sobres.",
   banco="BBVA 7788 9900 1122 3344", titular="Isabella Navarro Ruiz", limite="10 de octubre"),
]

# ═══════════════════════ BAUTIZOS ═══════════════════════
E += [
 dict(slug="bautizo-cielo", plantilla="cielo", tipo="Mi bautizo", nombre="Emiliano",
   fecha="2026-09-20T12:00:00-05:00", dia="Domingo",
   colores=dict(fondo="#2E4859", papel="#EFF4F5", acento="#BFD3D6", suave="#7E9BA6"),
   frase="Hoy recibo mi primer sacramento y quiero que estés conmigo.",
   ceremonia=dict(titulo="Ceremonia de bautizo", lugar="Parroquia del Espíritu Santo", direccion="Av. Constituyentes 88, Centro, Querétaro, Qro.", hora="12:00 PM"),
   recepcion=dict(titulo="Comida", lugar="Salón El Roble", direccion="Calle Pino 14, Jurica, Querétaro, Qro.", hora="1:30 PM"),
   itinerario=[("12:00 PM","Bautizo"),("1:30 PM","Comida"),("3:00 PM","Pastel"),("4:00 PM","Convivencia")],
   dress="Casual elegante", dressNota="Colores claros, por favor.",
   regalos="Tu presencia es el mejor regalo.",
   banco="", titular="", limite="5 de septiembre"),

 dict(slug="bautizo-nube", plantilla="nube", tipo="Mi bautizo", nombre="Julieta",
   fecha="2026-10-11T11:00:00-06:00", dia="Domingo",
   colores=dict(fondo="#E9E9EC", papel="#33333A", acento="#8E97A8", suave="#6E7684"),
   frase="Un domingo tranquilo, en familia, para empezar bien.",
   ceremonia=dict(titulo="Bautizo", lugar="Templo de San José", direccion="Calle Zaragoza 5, Centro, Toluca, Edo. Méx.", hora="11:00 AM"),
   recepcion=dict(titulo="Desayuno", lugar="Casa de los abuelos", direccion="Calle Nogal 22, Santa Ana, Toluca, Edo. Méx.", hora="12:30 PM"),
   itinerario=[("11:00 AM","Bautizo"),("12:30 PM","Desayuno"),("2:00 PM","Brindis")],
   dress="Casual", dressNota="",
   regalos="Sin regalos. Con que vengan basta.",
   banco="", titular="", limite="1 de octubre"),

 dict(slug="bautizo-oliva", plantilla="oliva", tipo="Bautizo", nombre="Mateo",
   fecha="2026-12-05T13:00:00-06:00", dia="Sábado",
   colores=dict(fondo="#5A6B4F", papel="#F4F2E8", acento="#C8CBB0", suave="#8C9A80"),
   frase="Mis papás y mis padrinos te quieren ahí este día.",
   ceremonia=dict(titulo="Bautizo", lugar="Parroquia de San Mateo", direccion="Calle Reforma 40, Centro, León, Gto.", hora="1:00 PM"),
   recepcion=dict(titulo="Comida", lugar="Jardín La Huerta", direccion="Blvd. Campestre 900, León, Gto.", hora="2:30 PM"),
   itinerario=[("1:00 PM","Bautizo"),("2:30 PM","Comida"),("4:00 PM","Pastel"),("5:00 PM","Despedida")],
   dress="Casual elegante", dressNota="Verde y beige van perfecto con la decoración.",
   regalos="Si quieres tener un detalle, agradecemos pañales etapa 3.",
   banco="", titular="", limite="20 de noviembre"),

 dict(slug="bautizo-azahar", plantilla="azahar", tipo="Mi bautizo", nombre="Renata",
   fecha="2027-01-23T12:30:00-06:00", dia="Sábado",
   colores=dict(fondo="#FBF8F3", papel="#3B332C", acento="#C4A878", suave="#8C7D69"),
   frase="Un día blanco, con flores de azahar y toda la familia junta.",
   ceremonia=dict(titulo="Bautizo", lugar="Catedral de Morelia", direccion="Av. Madero Poniente s/n, Centro, Morelia, Mich.", hora="12:30 PM"),
   recepcion=dict(titulo="Comida", lugar="Hacienda San Rafael", direccion="Carretera Morelia–Pátzcuaro km 6, Mich.", hora="2:00 PM"),
   itinerario=[("12:30 PM","Bautizo"),("2:00 PM","Comida"),("3:30 PM","Brindis de los padrinos"),("5:00 PM","Pastel")],
   dress="Formal claro", dressNota="Blanco y marfil reservados para la festejada.",
   regalos="Tu presencia es el mejor regalo. Si quieres tener un detalle, hay lluvia de sobres.",
   banco="BBVA 2233 4455 6677 8899", titular="Paulina Cárdenas Ruiz", limite="8 de enero"),

 dict(slug="bautizo-trigo", plantilla="trigo", tipo="Bautizo", nombre="Santiago",
   fecha="2027-03-08T11:30:00-06:00", dia="Lunes",
   colores=dict(fondo="#7A6244", papel="#F8F2E7", acento="#E0C79B", suave="#A89272"),
   frase="Empiezo el camino y quiero que estés en la primera foto.",
   ceremonia=dict(titulo="Bautizo", lugar="Parroquia de Santiago Apóstol", direccion="Plaza Principal s/n, Centro, San Luis Potosí, S.L.P.", hora="11:30 AM"),
   recepcion=dict(titulo="Comida", lugar="Quinta El Trigal", direccion="Camino a la Presa km 3, San Luis Potosí, S.L.P.", hora="1:00 PM"),
   itinerario=[("11:30 AM","Bautizo"),("1:00 PM","Comida"),("2:30 PM","Pastel"),("4:00 PM","Convivencia")],
   dress="Casual elegante", dressNota="Tonos tierra y beige.",
   regalos="Agradecemos pañales etapa 2 o 3.",
   banco="", titular="", limite="20 de febrero"),
]

# ═══════════════════════ INFANTIL ═══════════════════════
E += [
 dict(slug="nino-confeti", plantilla="confeti", tipo="Mi fiesta", nombre="Mía cumple 5",
   fecha="2026-05-12T16:00:00-06:00", dia="Martes",
   colores=dict(fondo="#E0684F", papel="#FFF6EC", acento="#FFD79A", suave="#F2A98E"),
   frase="¡Cumplo cinco! Ven a brincar, comer pastel y hacer mucho ruido.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Salón Brinca Brinca", direccion="Av. Las Torres 300, Metepec, Edo. Méx.", hora="4:00 PM"),
   itinerario=[("4:00 PM","Llegada y juegos"),("5:00 PM","Show"),("5:45 PM","Merienda"),("6:15 PM","Pastel"),("7:00 PM","Piñata")],
   dress="Cómodo para jugar", dressNota="Habrá brincolín, así que tenis y ropa que se pueda ensuciar.",
   regalos="Si quieres traer algo, a Mía le encantan los libros ilustrados.",
   banco="", titular="", limite="5 de mayo"),

 dict(slug="nino-safari", plantilla="safari", tipo="Mi cumpleaños", nombre="Leo cumple 3",
   fecha="2026-06-26T12:00:00-06:00", dia="Viernes",
   colores=dict(fondo="#3E5641", papel="#F6F1E2", acento="#D9A441", suave="#7F9470"),
   frase="Rugimos de gusto: Leo cumple tres y quiere a toda su manada.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta safari", lugar="Jardín Kikapú", direccion="Calle Ceiba 18, Cuernavaca, Mor.", hora="12:00 PM"),
   itinerario=[("12:00 PM","Bienvenida exploradores"),("1:00 PM","Comida"),("2:00 PM","Animales en vivo"),("3:00 PM","Pastel"),("3:45 PM","Piñata")],
   dress="De safari", dressNota="Colores tierra, gorra y muchas ganas de correr.",
   regalos="Nada indispensable. Si insisten, juguetes de madera.",
   banco="", titular="", limite="18 de junio"),

 dict(slug="nino-oceano", plantilla="oceano", tipo="Mi fiesta", nombre="Emma cumple 6",
   fecha="2026-08-03T15:00:00-05:00", dia="Lunes",
   colores=dict(fondo="#1F6E7A", papel="#EFF9F8", acento="#F0A08C", suave="#5E9AA2"),
   frase="Nos vamos al fondo del mar. Trae traje de baño.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta de alberca", lugar="Club Azul", direccion="Av. Costera 210, Veracruz, Ver.", hora="3:00 PM"),
   itinerario=[("3:00 PM","Alberca"),("4:30 PM","Merienda"),("5:15 PM","Pastel"),("6:00 PM","Piñata")],
   dress="Traje de baño", dressNota="Trae toalla y cambio de ropa. Habrá bloqueador.",
   regalos="Emma está juntando para su bici. Cualquier aportación se agradece.",
   banco="", titular="", limite="25 de julio"),

 dict(slug="nino-globos", plantilla="globos", tipo="Mi cumpleaños", nombre="Tadeo cumple 4",
   fecha="2026-09-17T16:30:00-06:00", dia="Jueves",
   colores=dict(fondo="#2F4A80", papel="#F4F7FC", acento="#EE8A7C", suave="#6C84B5"),
   frase="Cuatro años, mil globos y un pastel enorme.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Casa de Tadeo", direccion="Calle Girasol 9, Lomas Verdes, Naucalpan, Edo. Méx.", hora="4:30 PM"),
   itinerario=[("4:30 PM","Llegada"),("5:15 PM","Show de magia"),("6:00 PM","Merienda"),("6:30 PM","Pastel"),("7:00 PM","Piñata")],
   dress="Cómodo", dressNota="",
   regalos="Sin regalos, de verdad. Vengan y ya.",
   banco="", titular="", limite="10 de septiembre"),

 dict(slug="nino-jardin", plantilla="jardin", tipo="Mi fiesta", nombre="Luna cumple 7",
   fecha="2026-10-29T15:00:00-06:00", dia="Jueves",
   colores=dict(fondo="#C96C89", papel="#FFF3F6", acento="#A8C48C", suave="#D79AAE"),
   frase="Un jardín, muchas flores y siete velitas.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Jardín La Pérgola", direccion="Calle Camelia 55, Coyoacán, Ciudad de México", hora="3:00 PM"),
   itinerario=[("3:00 PM","Bienvenida"),("3:45 PM","Taller de coronas de flores"),("5:00 PM","Merienda"),("5:30 PM","Pastel"),("6:15 PM","Piñata")],
   dress="Floreado", dressNota="Si traes algo con flores, mejor. Habrá pasto y tierra.",
   regalos="A Luna le encantan las plantas de maceta.",
   banco="", titular="", limite="20 de octubre"),
]

# ═══════════════════════ ADOLESCENTE ═══════════════════════
E += [
 dict(slug="teen-neon", plantilla="neon", tipo="Mi cumpleaños", nombre="Dani cumple 16",
   fecha="2026-04-22T20:00:00-06:00", dia="Miércoles",
   colores=dict(fondo="#15171A", papel="#EDEFF0", acento="#B6E04A", suave="#8A9179"),
   frase="Luces bajas, música alta. Nos vemos ahí.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Estudio 33", direccion="Calle Córdoba 33, Roma Norte, Ciudad de México", hora="8:00 PM"),
   itinerario=[("8:00 PM","Entrada"),("9:00 PM","Pizza"),("10:00 PM","DJ"),("11:30 PM","Pastel"),("1:00 AM","Cierre")],
   dress="Lo que quieras, pero que brille", dressNota="Habrá luz negra: el blanco y el neón se ven increíbles.",
   regalos="Nada de regalos. Traigan energía.",
   banco="", titular="", limite="15 de abril"),

 dict(slug="teen-cassette", plantilla="cassette", tipo="Mi fiesta", nombre="Iker cumple 15",
   fecha="2026-07-10T19:00:00-05:00", dia="Viernes",
   colores=dict(fondo="#241639", papel="#F2ECFA", acento="#E5559B", suave="#8B6FB0"),
   frase="Una fiesta con la playlist que llevo armando todo el año.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Roof Garden Vértigo", direccion="Av. Vallarta 1200, Guadalajara, Jal.", hora="7:00 PM"),
   itinerario=[("7:00 PM","Llegada"),("8:00 PM","Cena"),("9:00 PM","Karaoke"),("10:30 PM","Pastel"),("12:00 AM","Cierre")],
   dress="Casual", dressNota="",
   regalos="Si quieres regalar algo, tarjetas de música o videojuegos.",
   banco="", titular="", limite="1 de julio"),

 dict(slug="teen-polaroid", plantilla="polaroid", tipo="Mis 18", nombre="Ale cumple 18",
   fecha="2027-02-15T19:30:00-06:00", dia="Lunes",
   colores=dict(fondo="#F1EDE6", papel="#1C1C1C", acento="#7E7E7E", suave="#5C5C5C"),
   frase="Dieciocho. Quiero la foto con toda la gente que me trajo hasta aquí.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Cena y fiesta", lugar="Casa Blanco", direccion="Calle Amsterdam 210, Condesa, Ciudad de México", hora="7:30 PM"),
   itinerario=[("7:30 PM","Bienvenida"),("8:30 PM","Cena"),("10:00 PM","Brindis"),("10:30 PM","Baile"),("1:00 AM","Cierre")],
   dress="Blanco y negro", dressNota="Código estricto de blanco y negro. Habrá cabina de fotos.",
   regalos="Estoy juntando para mi viaje de graduación.",
   banco="Santander 6677 8899 0011 2233", titular="Alejandra Mena Soto", limite="1 de febrero"),

 dict(slug="teen-prisma", plantilla="prisma", tipo="Mi cumpleaños", nombre="Sam cumple 17",
   fecha="2026-09-06T18:00:00-05:00", dia="Domingo",
   colores=dict(fondo="#101B33", papel="#E9F4FB", acento="#4FC8E8", suave="#5C7BA8"),
   frase="Diecisiete. Torneo, pizza y pastel. Nada más.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Arena Gamer Norte", direccion="Av. Universidad 800, Monterrey, N.L.", hora="6:00 PM"),
   itinerario=[("6:00 PM","Registro"),("6:30 PM","Torneo"),("8:30 PM","Pizza"),("9:15 PM","Pastel y premiación")],
   dress="Cómodo", dressNota="",
   regalos="Sin regalos.",
   banco="", titular="", limite="30 de agosto"),

 dict(slug="teen-vinilo", plantilla="vinilo", tipo="Mi fiesta", nombre="Nico cumple 16",
   fecha="2026-11-19T19:00:00-06:00", dia="Jueves",
   colores=dict(fondo="#22201E", papel="#F3F0EC", acento="#E08A3C", suave="#9A8D7E"),
   frase="Música en vivo, tacos y la banda completa.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Fiesta", lugar="Foro Tinta", direccion="Calle 5 de Mayo 18, Centro, Puebla, Pue.", hora="7:00 PM"),
   itinerario=[("7:00 PM","Apertura"),("8:00 PM","Banda en vivo"),("9:30 PM","Tacos"),("10:15 PM","Pastel"),("12:00 AM","Cierre")],
   dress="Casual", dressNota="",
   regalos="Si quieres regalar algo, vinilos o playeras de banda.",
   banco="", titular="", limite="10 de noviembre"),
]

# ═══════════════════════ CORPORATIVO ═══════════════════════
E += [
 dict(slug="corp-consejo", plantilla="consejo", tipo="Te esperamos", nombre="Cena Anual 2026",
   fecha="2026-12-04T20:00:00-06:00", dia="Viernes",
   colores=dict(fondo="#132033", papel="#EDF1F6", acento="#9BA9BE", suave="#6B7D96"),
   frase="Cerramos el año agradeciendo a quienes lo hicieron posible.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Cena de gala", lugar="Salón Diamante, Hotel Presidente", direccion="Campos Elíseos 218, Polanco, Ciudad de México", hora="8:00 PM"),
   itinerario=[("8:00 PM","Registro y cóctel"),("9:00 PM","Palabras de bienvenida"),("9:30 PM","Cena"),("10:30 PM","Reconocimientos"),("11:30 PM","Música")],
   dress="Etiqueta", dressNota="Traje oscuro o vestido largo.",
   regalos="", banco="", titular="", limite="25 de noviembre", rsvpTitulo="Confirma tu asistencia"),

 dict(slug="corp-cumbre", plantilla="cumbre", tipo="Invitación", nombre="Congreso Nacional",
   fecha="2026-05-18T09:00:00-05:00", dia="Lunes",
   colores=dict(fondo="#2B2B2E", papel="#F4F4F5", acento="#B9B9BC", suave="#86868A"),
   frase="Dos días de conferencias, mesas de trabajo y networking.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Sede", lugar="Centro de Convenciones Expo", direccion="Blvd. Manuel Ávila Camacho 5, Monterrey, N.L.", hora="9:00 AM"),
   itinerario=[("9:00 AM","Registro"),("10:00 AM","Conferencia magistral"),("12:00 PM","Mesas de trabajo"),("2:00 PM","Comida"),("4:00 PM","Panel de cierre")],
   dress="Ejecutivo", dressNota="",
   regalos="", banco="", titular="", limite="5 de mayo", rsvpTitulo="Reserva tu lugar"),

 dict(slug="corp-brindis", plantilla="brindis", tipo="Te invitamos", nombre="Posada Savey",
   fecha="2026-12-12T19:00:00-06:00", dia="Sábado",
   colores=dict(fondo="#1F3330", papel="#F1F5F2", acento="#C8A860", suave="#7C9A92"),
   frase="Un brindis por el año que termina y por el equipo que lo sacó adelante.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Posada", lugar="Terraza Verde", direccion="Av. Insurgentes Sur 1200, Del Valle, Ciudad de México", hora="7:00 PM"),
   itinerario=[("7:00 PM","Bienvenida"),("8:00 PM","Cena"),("9:00 PM","Intercambio"),("10:00 PM","Música y baile")],
   dress="Casual elegante", dressNota="Si te animas, algo verde o dorado.",
   regalos="Intercambio con tope de $500. Trae tu regalo envuelto.",
   banco="", titular="", limite="1 de diciembre", rsvpTitulo="Confirma tu asistencia"),

 dict(slug="corp-enlace", plantilla="enlace", tipo="Inauguración", nombre="Nuevas Oficinas",
   fecha="2026-08-27T18:00:00-05:00", dia="Jueves",
   colores=dict(fondo="#F5F6F8", papel="#1C2A3A", acento="#3D6EA8", suave="#5F7691"),
   frase="Abrimos las puertas de nuestra nueva casa y queremos enseñártela.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Coctel de inauguración", lugar="Torre Norte, piso 12", direccion="Av. Ricardo Margáin 440, San Pedro Garza García, N.L.", hora="6:00 PM"),
   itinerario=[("6:00 PM","Recepción"),("6:30 PM","Corte de listón"),("7:00 PM","Recorrido"),("8:00 PM","Cóctel")],
   dress="Ejecutivo", dressNota="",
   regalos="", banco="", titular="", limite="18 de agosto", rsvpTitulo="Confirma tu asistencia"),

 dict(slug="corp-distincion", plantilla="distincion", tipo="Entrega de premios", nombre="Premios 2026",
   fecha="2026-10-21T19:30:00-05:00", dia="Miércoles",
   colores=dict(fondo="#131313", papel="#F6F4F0", acento="#CBA85C", suave="#8C8375"),
   frase="Una noche para reconocer el trabajo que marcó el año.",
   ceremonia=dict(titulo="", lugar="", direccion="", hora=""),
   recepcion=dict(titulo="Ceremonia y cena", lugar="Teatro Diana", direccion="Av. 16 de Septiembre 710, Guadalajara, Jal.", hora="7:30 PM"),
   itinerario=[("7:30 PM","Alfombra y registro"),("8:15 PM","Ceremonia"),("9:45 PM","Cena"),("11:00 PM","Brindis final")],
   dress="Etiqueta rigurosa", dressNota="Smoking y vestido largo.",
   regalos="", banco="", titular="", limite="10 de octubre", rsvpTitulo="Confirma tu asistencia"),
]

# ═══════════ Secciones extra por temática ═══════════
PADRINOS_BODA = [
  {"rol":"Padrinos de velación","nombre":"Sr. y Sra. Ríos Montes"},
  {"rol":"Padrinos de anillos","nombre":"Laura y Andrés"},
  {"rol":"Padrinos de lazo","nombre":"Familia Beltrán"},
  {"rol":"Padrinos de arras","nombre":"Marisol y Javier"},
]
PADRINOS_XV = [
  {"rol":"Madrina de vals","nombre":"Tía Guadalupe"},
  {"rol":"Padrino de brindis","nombre":"Tío Ricardo"},
  {"rol":"Madrina de ramo","nombre":"Abuela Carmen"},
  {"rol":"Chambelán de honor","nombre":"Emilio Ruiz"},
]
PADRINOS_BAUTIZO = [
  {"rol":"Padrino","nombre":"Rodrigo Salas"},
  {"rol":"Madrina","nombre":"Ana Paula Salas"},
]
NOTAS_NINOS = [
  {"titulo":"Papás bienvenidos","texto":"Hay café y mesa para adultos. Nadie tiene que quedarse parado."},
  {"titulo":"Alergias","texto":"Avísanos al confirmar si tu peque tiene alguna alergia alimentaria."},
  {"titulo":"Salida","texto":"La fiesta termina puntual. Pasa por tu peque a la hora indicada."},
]
NOTAS_TEEN = [
  {"titulo":"Entrada","texto":"Solo pasan quienes están en la lista. Trae tu pase a la mano."},
  {"titulo":"Sin alcohol","texto":"Evento para menores. Habrá bebidas sin alcohol toda la noche."},
]
NOTAS_CORP = [
  {"titulo":"Estacionamiento","texto":"Cortesía en el nivel B2. Presenta tu boleto en el registro."},
  {"titulo":"Gafete","texto":"Tu gafete se entrega en la mesa de registro con tu nombre confirmado."},
  {"titulo":"Cupo","texto":"El registro cierra cuando se agota el aforo. Confirma cuanto antes."},
]

EXTRAS = {
  "boda":    dict(galeria=5, padrinos=PADRINOS_BODA, notas=[], galeriaTitulo="Nuestra historia en fotos"),
  "xv":      dict(galeria=5, padrinos=PADRINOS_XV, notas=[], galeriaTitulo="Mi sesión de fotos"),
  "bautizo": dict(galeria=3, padrinos=PADRINOS_BAUTIZO, notas=[], galeriaTitulo="Mis primeras fotos"),
  "nino":    dict(galeria=3, padrinos=[], notas=NOTAS_NINOS, galeriaTitulo="Así celebramos"),
  "teen":    dict(galeria=3, padrinos=[], notas=NOTAS_TEEN, galeriaTitulo="Fotos"),
  "corp":    dict(galeria=0, padrinos=[], notas=NOTAS_CORP, galeriaTitulo=""),
}

# ═══════════════════════ Escritura ═══════════════════════
for ev in E:
    largo, corto = fechas(ev["fecha"], ev["dia"])
    cer, rec = ev["ceremonia"], ev["recepcion"]
    extra = EXTRAS[ev["slug"].split("-")[0]]
    d = {
        "plantilla": ev["plantilla"],
        "colores": ev["colores"],
        "tipo": ev["tipo"],
        "nombre": ev["nombre"],
        "fecha": ev["fecha"],
        "fechaTexto": largo,
        "fechaCorta": corto,
        "frase": ev["frase"],
        "fotoPortada": "",
        "musica": "",
        "ceremonia": {**cer, "mapa": mapa(cer["direccion"]) if cer["direccion"] else ""},
        "recepcion": {**rec, "mapa": mapa(rec["direccion"]) if rec["direccion"] else ""},
        "itinerario": [{"hora": h, "evento": e} for h, e in ev["itinerario"]],
        "dressCode": ev["dress"],
        "dressNota": ev["dressNota"],
        "regalos": {"texto": ev["regalos"], "banco": ev["banco"], "titular": ev["titular"]},
        "limiteRsvp": ev["limite"],
        "rsvpEndpoint": "",
        "whatsappAnfitrion": WA,
        "pases": PASES,
        "marca": "Hecho por Savey · savey.pro",
        "galeria": extra["galeria"],
        "fotos": [],
        "padrinos": extra["padrinos"],
        "notas": extra["notas"],
    }
    if extra["galeriaTitulo"]:
        d["galeriaTitulo"] = extra["galeriaTitulo"]
    if ev.get("rsvpTitulo"):
        d["rsvpTitulo"] = ev["rsvpTitulo"]
    with open(f"{OUT}/{ev['slug']}.json", "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

print(f"{len(E)} invitaciones generadas")
for ev in E:
    print(" ", ev["slug"], "→", ev["plantilla"])
