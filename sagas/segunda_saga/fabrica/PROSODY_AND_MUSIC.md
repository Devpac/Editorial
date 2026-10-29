<!-- Fábrica — PROSODY_AND_MUSIC: base de oficio + adenda de dark romance (v2.0) -->

# PROSODY_AND_MUSIC.md

## PROPÓSITO

La prosa suena. Aunque se lea en silencio, el lector percibe
cadencia, acento, ritmo. Una frase técnicamente correcta puede
sonar mal; una frase poco ortodoxa puede sonar perfecta.

AESTHETIC_REGISTER fija longitudes medias y densidades. VOICE
define idiolecto. Este archivo se ocupa del nivel intermedio:
la música de la frase, del párrafo y del capítulo.

Sin archivo dedicado, la musicalidad se deja al instinto. En
escritura asistida por LLM, esto genera prosa métricamente
correcta pero inerte: cumple el régimen sin sonar.

JERARQUÍA: Capa 3.
Subordinada a AESTHETIC_REGISTER (define los parámetros
audibles del régimen) y a VOICE_ARCHITECTURE (la voz es la
musicalidad de base).

---

## PRINCIPIO BASE

La prosa tiene tres niveles de ritmo simultáneos:
1. Ritmo de frase: acentos, cláusulas, longitud.
2. Ritmo de párrafo: alternancia de frases.
3. Ritmo de capítulo: alternancia de párrafos, de escenas, de
   densidades.

Los tres deben coordinarse. Un párrafo bien escrito puede
romper el ritmo del capítulo. Un capítulo rítmicamente
correcto puede contener párrafos sordos.

---

## RITMO DE FRASE

### LONGITUD Y PESO
La longitud ya está regulada por AESTHETIC_REGISTER. Lo que
este archivo añade: el peso dentro de la longitud.

Una frase de 20 palabras puede:
- Tener peso uniforme (todas las palabras importan igual).
- Tener peso creciente (acumulación hacia el final).
- Tener peso concentrado (una o dos palabras dominan).
- Tener peso decreciente (empieza densa y se relaja).

Elegir no es cosmético: el peso determina dónde queda el lector
al terminar la frase.

### ACENTO Y CADENCIA
En español, la cadencia depende de:
- Número y posición de sílabas tónicas.
- Grupos acentuales (palabras ligadas sin pausa).
- Pausas internas (comas, dos puntos, guiones).

REGLA OPERATIVA:
Una frase debería poder pronunciarse sin tropezar. Si al leerla
en voz alta se tropieza, revisar. A veces el tropiezo es
deliberado (marca emoción, fractura); debe ser declarado.

### FINALES DE FRASE
La última palabra de una frase recibe énfasis natural. Elegirla
con cuidado: lo que quede al final es lo que resuena.

COMPARAR:
"Volvió a casa sin decir palabra, cansado."
"Cansado, volvió a casa sin decir palabra."

Las dos tienen el mismo contenido. La primera termina en
"cansado" (estado); la segunda en "palabra" (ausencia). Eligen
resonancias distintas.

### COMIENZOS DE FRASE
La primera palabra también pesa. Frases que empiezan con
conectores neutros ("Y", "Entonces", "Pero") a menudo se
benefician de reescritura.

Nota: este apartado describe el efecto prosódico de evitar
arranques con conectores neutros. La cuota cuantificada que cubre
las cuatro familias completas de aperturas (artículo definido,
artículo indefinido, sujeto pronominal, nombre propio,
estructura sintáctica, conector neutro) vive en REGLA 1 — INICIO
DE FRASE de PROSE_LINE_DISCIPLINE.md, con el techo operativo de
máximo dos frases consecutivas iniciadas con el mismo elemento.
Aquel archivo cuantifica lo que aquí se nombra como tendencia.

---

## RITMO DE PÁRRAFO

### ALTERNANCIA
Un párrafo con todas las frases de longitud similar suena
plano. La variación es el motor rítmico.

PATRÓN BASE RECOMENDADO (en régimen no declarado otro):
Frase media — frase corta — frase larga — frase corta.
Variante: frase larga — frases cortas (2-3) — frase media.

El patrón exacto depende del régimen y de la función del
párrafo. La regla es la alternancia, no una fórmula.

### EL PÁRRAFO DE UNA FRASE
Un párrafo que contiene una sola frase tiene peso especial.
Úsese como recurso cuando:
- Se quiere subrayar un cambio.
- El pensamiento cierra.
- Se introduce una imagen cargada.

Si se usa con frecuencia, pierde efecto.

### LA FRASE CORTA AISLADA
Dentro de un párrafo de frases largas, una frase corta
funciona como golpe. Colocarla con intención: suele quedar
bien después de una acumulación, no antes.

---

## RITMO DE CAPÍTULO

### ESCENA A ESCENA
Las escenas no deben tener todas la misma densidad ni
longitud. Cruzar con SCENE_SHAPE (mapa de densidad). La música
del capítulo depende de que escenas largas y cortas alternen,
densas y ligeras, dialogadas y narrativas.

### PÁRRAFO DE APERTURA / PÁRRAFO DE CIERRE
El primer y último párrafo de cada capítulo tienen peso
específico (ver SEAMS_AND_HINGES). Su musicalidad debe ser
deliberada.

Principio: el primer párrafo inicia la respiración del
capítulo; el último la cierra o la suspende. Ambos merecen
más atención rítmica que los párrafos del medio.

---

## FIGURAS DE SONIDO

Herramientas disponibles. No todas compatibles con todo
régimen.

### ALITERACIÓN
Repetición de consonantes o sonidos.
Permitida en régimen barroco, oral, algunos periódicos de alta
factura. Prohibida o muy dosificada en régimen minimalista
(suena como adorno).

Cuando se usa, debe ser inaudible deliberadamente: el lector
siente el efecto sin identificar la figura. Si la figura se
nota, es artificio.

### ASONANCIA
Repetición de vocales.
Más discreta que la aliteración. Tolerada más ampliamente.
Peligro en prosa: aparece por accidente y suena a verso
oculto.

### RIMA INTERNA
Rimas dentro o entre frases.
En prosa, casi siempre error. Detectar en revisión y eliminar
(sustituir una de las palabras por sinónimo o reordenar).

### REPETICIÓN DELIBERADA
Repetir una palabra o estructura para marcar ritmo. Legítima
en régimen oral, testimonial, algunas aperturas memorables.
Debe ser inequívocamente deliberada; si el lector puede dudar,
parece descuido.

---

## PATRONES BINARIOS Y TERNARIOS

### ENUMERACIONES DE TRES
"A, B y C" tiene cadencia natural en español.
Usar con moderación. Aparecen en exceso en prosa asistida por
LLM.

### PARALELISMOS
Estructuras gemelas: "Vino. Vio. Venció." (ternario simétrico).
"Vino, y no dijo nada." (binario asimétrico).

Funcionan bien cuando la simetría del contenido lo justifica.
Sin justificación, suenan a retórica vacía.

### CLIMAX GRADUAL
Orden ascendente en enumeración: la palabra más fuerte al
final. Clásico, eficaz.
"Perdió el rumbo, perdió la fe, perdió la vida."

### ANTICLÍMAX
Orden descendente o disruptivo para producir contraste
cómico o amargo.
"Perdió la casa, la fe y las llaves."

Son recursos. Los recursos se usan, no se aplican sistemáticamente.

---

## LA LECTURA EN VOZ ALTA

Es el test fundamental de prosodia. Operativo.

### CÓMO APLICARLO
- Leer un pasaje en voz alta (propio o asistido por TTS).
- Marcar dónde se tropieza, dónde falta aire, dónde suena mal.
- No corregir en el momento: anotar.
- Reescribir en sesión aparte.

### QUÉ DETECTA
- Frases que requieren respiración imposible.
- Grupos consonánticos difíciles.
- Rimas internas accidentales.
- Ambigüedades que la vista salva.
- Párrafos sin variación audible.

### QUÉ NO DETECTA
- Problemas de arco de personaje o estructura. Prosodia es
  nivel línea.

---

## PROSA "CALCULADA" vs "ORGÁNICA"

### PROSA CALCULADA
Todas las frases están pesadas. La musicalidad es deliberada
en cada punto. Es el modelo de cierta narrativa literaria
(Flaubert, Onetti, Cortázar en ciertos pasajes).
Riesgo: manierismo. La prosa se nota más que lo narrado.

### PROSA ORGÁNICA
La musicalidad emerge de la voz sin ser construida frase a
frase. Es el modelo de la voz oral y de cierta prosa
anglosajona de género.
Riesgo: irregularidad. Hay pasajes sordos que la voz no
cubre sola.

La mayoría de las novelas se sitúan entre los dos polos.
Declarar en qué zona opera el proyecto orienta las
revisiones de pasada 4.

---

## CONTAMINACIÓN DE REGISTRO

Cuando una frase introduce música ajena al régimen declarado.
Típico:
- Frase lírica en régimen periodístico.
- Frase seca en régimen expansivo.

Detectar en lectura: sensación de que "esa frase no es de
aquí". Reescribir hasta que se integre.

Excepción: cambio de voz declarado (en multi-POV, en pasajes
de libre indirecto donde la voz del personaje invade al
narrador). Estas contaminaciones son método, no error.

---

## PROSODIA Y SUBTEXTO

La musicalidad puede transportar subtexto.
Ejemplo: una frase que "suena a resignación" por su cadencia
descendente, sin que el contenido lo diga.

Cruce con SUBTEXT_MECHANICS: los mecanismos de subtexto
incluyen cadencia, no sólo elección léxica.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — VOZ ALTA
Un capítulo entero leído en voz alta: ¿hay zonas que se
tropiezan y no son deliberadas?

TEST 2 — VARIACIÓN EN PÁRRAFO
Tomar tres párrafos al azar. ¿Las longitudes de frase
alternan? ¿O son homogéneas?

TEST 3 — FINALES DE FRASE
Tomar diez frases al azar. ¿La última palabra de cada una
fue elegida con intención, o quedó donde el orden sintáctico
la puso?

TEST 4 — RIMAS ACCIDENTALES
Tomar una página al azar. ¿Hay rimas involuntarias que no se
habían detectado?

TEST 5 — PRIMEROS Y ÚLTIMOS PÁRRAFOS
Los primeros y últimos párrafos de cada capítulo: ¿tienen
cadencia trabajada o son funcionales?

---

## ERRORES FRECUENTES

### ERROR 1 — HOMOGENEIDAD
Todas las frases del mismo largo. El párrafo suena monótono.
Corrección: alternar por diseño.

### ERROR 2 — RITMO APRENDIDO
Patrón rítmico que se repite inconscientemente (típico:
frase larga + frase corta + frase larga, uniformemente).
Se detecta leyendo en voz alta páginas alternas.

### ERROR 3 — ABUSO DEL TERNARIO
Cada párrafo contiene una enumeración de tres. Tic
detectable, especialmente en prosa asistida por LLM.

Nota: este error nombra el patrón. La cuota numérica cuantificada
(máximo un ternario por página de 250-300 palabras, con
sustituciones operativas y excepciones por materia) vive en TIC 1
— TERNARIO OBSESIVO de PROSE_LINE_DISCIPLINE.md. Aquel archivo
cuantifica lo que aquí se nombra como hábito.

### ERROR 4 — FRASE FINAL PERDIDA
El final de la frase queda en palabra insignificante.
Reescribir para que el final lleve peso.

### ERROR 5 — SOLEMNIDAD POR CADENCIA
Uso de cadencias solemnes (ternarios ascendentes, cláusulas
paralelas) en contenido trivial. Produce tono pomposo.

---

## RELACIÓN CON OTROS ARCHIVOS

PROSODY_AND_MUSIC.md recibe de:
- AESTHETIC_REGISTER.md (parámetros audibles del régimen)
- VOICE_ARCHITECTURE.md (cadencia base de cada voz)
- SCENE_SHAPE.md (dónde dilatar, dónde comprimir, dónde
  concentrar)

PROSODY_AND_MUSIC.md alimenta:
- SUBTEXT_MECHANICS.md (cadencia como transporte de subtexto)
- DIALOGUE_MECHANICS.md (ritmo del intercambio)

PROSODY_AND_MUSIC.md opera en paralelo, sin precedencia mutua,
con:
- PROSE_LINE_DISCIPLINE.md (este archivo es música; aquel archivo
  es anatomía gramatical. Las dos disciplinas se solapan en los
  comienzos de frase y en el ternario: este archivo describe el
  efecto prosódico, PROSE_LINE_DISCIPLINE.md cuantifica las
  cuotas. Las correcciones de un archivo no deben romper las
  cuotas del otro; la coordinación opera en pasada 4 de
  REVISION_PROTOCOL.)

PROSODY_AND_MUSIC.md se invoca principalmente en:
- OPERACIÓN B (mientras se escribe, como oído de fondo).
- PASADA 4 de REVISION_PROTOCOL (trabajo de línea).

---

## NOTA

No todas las novelas requieren la misma atención prosódica.
Una novela de género con ritmo cinético puede ganar poco de
trabajo fino en cadencia; una novela literaria puede depender
de él.
Declarar el nivel de atención prosódica como parte de
AESTHETIC_REGISTER es opción.


---
---

## ADENDA DE ESPECIALIZACIÓN — Fábrica (género)

> Especializa la base de arriba, que sigue vigente. El nivel de atención prosódica lo declara
> `AESTHETIC_REGISTER.md` (DECLARACIÓN PRIMARIA, por defecto) o, si la obra declara otro, su
> preset (`PRESET_<OBRA>.md` › AESTHETIC_REGISTER › Declaración primaria).

### EL GANCHO

Este archivo no da criterio de gancho. El cierre de capítulo lo juzgan DIALOGUE_MECHANICS (EL
DIÁLOGO COMO GANCHO DE CAPÍTULO y TEST 11) y SEAMS_AND_HINGES, con el suelo de
`PAREJA_PRIMERO.md` (§3) o el del preset; su cadencia, el TEST 9 de AESTHETIC_REGISTER. El TEST 5 de la base
mira solo la cadencia de los primeros y últimos párrafos.
