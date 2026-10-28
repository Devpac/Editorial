<!-- Fábrica v3.0 — VOICE_ARCHITECTURE: base de oficio + adenda de dark romance (v2.0) -->

# VOICE_ARCHITECTURE.md

## PROPÓSITO

Este archivo define la(s) voz(ces) narradora(s). La voz es el filtro
a través del cual el lector accede al mundo; no es "estilo" en
sentido ornamental, es epistemología del texto.

Una voz mal definida produce prosa plausible pero impersonal.
Una voz múltiple mal orquestada produce novela fragmentada.

JERARQUÍA: Capa 1. Condicionado por:
- CHARACTER_PHYSICS.md (la herida del narrador determina sus
  puntos ciegos)
- AESTHETIC_REGISTER.md (qué tipo de voz es compatible con el
  régimen)

---

## DECLARACIÓN GLOBAL

TIPO DE NARRADOR PRINCIPAL:
[primera persona / tercera limitada / tercera omnisciente /
segunda persona / coral / narrador-testigo / narrador-protagonista
diferido]

NÚMERO DE POVs: [uno / dos / tres o más, en qué distribución]

RELACIÓN DEL NARRADOR CON LA HISTORIA:
[participa / observa / narra desde el futuro / narra desde el
presente del suceso / indeterminada]

POSICIÓN TEMPORAL:
[contemporánea al suceso / retrospectiva / anacrónica /
dislocada]

GRADO DE FIABILIDAD:
[fiable / levemente no fiable / abiertamente no fiable / fiable
con zonas ciegas]

---

## FICHA POR VOZ

Si hay múltiples POVs, completar una ficha por cada una.
Si hay una sola voz, completar una.

### NOMBRE DE LA VOZ / PERSONAJE POV
[...]

### REGISTRO LÉXICO
El rango de vocabulario que esta voz usa naturalmente.
- Cultismos permitidos: sí / no / en qué condiciones.
- Vulgarismos permitidos: sí / no / en qué condiciones.
- Léxico técnico: ¿conoce el de qué oficios?

### SINTAXIS CARACTERÍSTICA
- Longitud media de frase (ver AESTHETIC_REGISTER.md)
- Preferencia por parataxis (frases cortas yuxtapuestas)
  o hipotaxis (subordinación)
- Uso de puntuación: normal, expresiva, disruptiva

### PUNTO CIEGO PRINCIPAL
Derivado directamente de la herida del personaje (si es narrador
protagonista) o de su posición epistemológica (si es testigo).

NO es rasgo de estilo: es lo que el narrador genuinamente no
puede ver porque verlo desmoronaría su mecanismo de defensa
o excedería su acceso.

Ejemplo 1 (narrador protagonista):
"Narrador cuyo mecanismo de defensa es el control:
no puede percibir la generosidad espontánea de otros
sin reinterpretarla como cálculo."

Ejemplo 2 (narrador testigo):
"Narrador que nunca fue marino: no puede nombrar correctamente
las maniobras; las describe por su efecto en los cuerpos.
Esta limitación es la ventaja: da cuenta de lo que los marinos
ya no ven por costumbre."

### FIJACIONES PERCEPTIVAS
3 elementos que el narrador observa de forma desproporcionada.
Estas fijaciones no son decorativas: revelan deseo profundo o
herida.

Ejemplo:
Fijación 1: el estado de la ropa ajena (codifica ansiedad de clase)
Fijación 2: la forma en que otros comen (codifica ansiedad de
control)
Fijación 3: las manos de quien le habla (codifica deseo no
permitido)

### LO QUE ESTA VOZ NO NOMBRA
Ciertas cosas están ausentes por estructura, no por omisión
accidental.

Ejemplo:
"El narrador nunca nombra a su madre. Esto se sostiene durante
toda la novela. El lector lo notará hacia la mitad."

### MUSICALIDAD
Algunas voces tienen rasgos auditivos específicos:
- Aliteración recurrente
- Cadencia de cierre de párrafo
- Repetición estructural de palabras-ancla

No imponer si no aplica. Pero si aplica, declararlo: si no se
declara, se pierde entre capítulos.

### IDIOLECTO Y SOBREESCRITURA DE CUOTAS GLOBALES
El conjunto de los campos de esta ficha (registro léxico,
sintaxis característica, fijaciones perceptivas, lo que la voz
no nombra, musicalidad) constituye el idiolecto de la voz
narrativa. Este idiolecto es sobreescritura legítima local de
las cuotas globales declaradas en PROSE_LINE_DISCIPLINE.md.

Lo declarado en esta ficha no computa contra aquellas cuotas
cuando funciona como rasgo de voz: una voz narrativa con
muletillas sostenidas, abuso declarado de adverbios, ternarios
obsesivos como cadencia de cierre, hedge-adverbs como tic
verbal, dobletes adjetivales sistemáticos o cualquier otro
patrón que en prosa neutra sería tic LLM no transgrede aquel
archivo si está aquí declarado como rasgo de la voz.

La distinción entre tic LLM y rasgo de voz se ancla en la
sección ERROR DEL SISTEMA A EVITAR de PROSE_LINE_DISCIPLINE: el
tic LLM es lo que aparece sin haberse declarado, por inercia
del modelo; el rasgo de voz es lo que aparece porque está
declarado aquí, y opera como caracterización epistemológica
del narrador. Lo no declarado se cuenta y se corrige; lo
declarado se respeta y se sostiene.

Declaración paralela: DIALOGUE_MECHANICS.md aplica la misma
sobreescritura para idiolecto de personaje en diálogo. Esta
ficha cubre la voz narrativa; aquella, las voces de personajes.

Para que la sobreescritura sea legítima debe ser explícita:
declaración en esta ficha del rasgo concreto, su función en la
caracterización epistemológica de la voz, y la magnitud
aproximada del desplazamiento respecto a la cuota global. Sin
declaración explícita, el rasgo se trata como tic LLM y se
corrige.

---

## TIEMPO VERBAL DOMINANTE

La elección del tiempo verbal de la prosa narrativa es decisión
arquitectónica de la voz, paralela a la persona narrativa y al
grado de fiabilidad. No es decoración; configura la
epistemología del texto: distancia narratorial, gestión de
retrospección, cadencia, integración natural o forzada del
salto temporal.

La distinción entre esta sección y el IDIOLECTO declarado
arriba es precisa: el idiolecto opera dentro de la elección de
tiempo verbal (cómo habla esta voz dentro del marco temporal
elegido); la elección de tiempo verbal es decisión de capa
arquitectónica que precede al idiolecto y lo enmarca. El
idiolecto puede modular pero no contradice el marco temporal
declarado aquí.

Se declara el modo dominante de la prosa narrativa. Si la
novela usa varios tiempos en distintas secciones, se declara
la alternancia (ver ALTERNANCIA DECLARADA al final de esta
sección).

### PRESENTE HISTÓRICO

La narración ocurre en presente del indicativo. El narrador
relata como si los hechos sucedieran en el momento de la
lectura.

Implicaciones operativas:
- Inmediatez perceptiva: el lector está dentro del momento; la
  distancia narratorial se reduce al mínimo.
- Ausencia de retrospección integrada: no hay narrador desde
  el futuro que sepa cómo termina; la epistemología del texto
  es la del personaje en el instante.
- Dificultad de saltos temporales controlados: las elipsis
  largas y los flashbacks resultan más rígidos en presente
  histórico que en pretérito; cada salto exige declaración
  explícita.
- Riesgo de monotonía: sin modulación de cadencia (ver
  PROSODY_AND_MUSIC), el presente sostenido produce sensación
  de uniformidad; el régimen estético debe trabajar con la
  cadencia como contrapunto.

Compatibilidad con regímenes estéticos (ver
AESTHETIC_REGISTER): natural en MINIMALISTA tardío, en cierta
novela de plano interior intensificado, en POPULAR-EFICIENTE
de tensión sostenida. Tenso en NAVAL-DECIMONÓNICO y en
EXPANSIVO de conciencia mediada (donde el pretérito sostiene
mejor la digresión).

### PASADO SIMPLE / PRETÉRITO

La narración ocurre en pretérito perfecto simple (o indefinido
en sus variantes regionales) como tiempo dominante.

Implicaciones operativas:
- Distancia narratorial moderada: el narrador relata desde
  algún momento posterior al evento; el lector reconoce que lo
  narrado ya ocurrió.
- Gestión natural de la secuencia temporal: la línea del
  tiempo se construye sin fricción, los saltos se integran sin
  declaración pesada.
- Integración natural de retrospectiva: el pluscuamperfecto
  marca pasado anterior al pasado principal sin disonancia.
- Registro de tradición narrativa: el lector reconoce el
  contrato narrativo clásico.

Tiempo por defecto de la novela en español. La elección no
necesita justificación específica; lo que requiere
justificación es apartarse de él.

Compatibilidad con regímenes estéticos: natural en todos los
regímenes del inventario, salvo cuando el régimen exige
explícitamente otra elección (presente histórico en cierto
MINIMALISTA tardío, oralidad evocativa en ciertos modos del
régimen ORAL / TESTIMONIAL).

### PLUSCUAMPERFECTO COMO MARCO

El pluscuamperfecto no es tiempo dominante; es marco
gramatical para registrar pasado anterior al pasado principal
cuando la narración corre en pretérito. Algunas escenas o
pasajes enteros pueden iniciarse en pluscuamperfecto y
deslizarse a pretérito cuando la retrospectiva se hace
sostenida.

Implicaciones operativas:
- Función primaria: marcar nivel temporal anterior al de la
  narración principal sin declaración explícita del tipo
  "años antes".
- Función secundaria: instalar pasaje retrospectivo extenso.
  El primer párrafo en pluscuamperfecto, los siguientes
  deslizándose a pretérito; al cierre del pasaje, retorno al
  marco principal por pluscuamperfecto o por anclaje temporal
  explícito.
- Riesgo: el uso sostenido del pluscuamperfecto pesa
  sintácticamente (perífrasis verbal continua) y produce
  sensación de prosa apresada en estado anterior; conviene
  tratarlo como marco que abre y cierra, no como tiempo
  dominante.

### CONDICIONAL COMO FLASHBACK

Uso del condicional para evocar pasado distante o evento
puntual con tinte retrospectivo, frecuente en español
literario para introducir eventos cuya consecuencia se muestra
después (estructura del tipo "años más tarde recordaría
aquella tarde").

Implicaciones operativas:
- Recurso expresivo, no tiempo dominante. Su función es marcar
  un punto de evocación desde un futuro respecto al evento
  principal, frecuentemente proyectando consecuencias.
- Uso medido: convertido en recurso recurrente se vuelve tic
  prosódico identificable. La cuota razonable es escasa: dos o
  tres apariciones por novela media, no por capítulo.
- Compatible con régimen EXPANSIVO de conciencia mediada
  (donde la voz se permite estos saltos evocativos como parte
  del tejido). Tenso en MINIMALISTA y en POPULAR-EFICIENTE.

### ALTERNANCIA DECLARADA

Una novela puede combinar tiempos verbales por sección con
función dramática: pasado en capítulos de protagonista,
presente en capítulos de antagonista; pretérito en marco
general, presente en escenas culminantes; presente en
flashbacks, pretérito en línea principal (inversión deliberada
del esquema natural).

Cada cambio de régimen temporal debe estar declarado en esta
ficha. La declaración explicita: qué secciones usan qué
tiempo, por qué función dramática, qué contraste produce. El
cambio sin declaración es inconsistencia, no virtuosismo, y se
trata como error en revisión (cruzar con REVISION_PROTOCOL,
pasada de voz).

Reglas operativas para la alternancia:
- Si la alternancia distingue POVs en multi-POV (ver
  COORDINACIÓN MULTI-POV más abajo), se declara la asignación
  voz × tiempo y se mantiene en toda la novela.
- Si la alternancia distingue niveles temporales (línea
  principal vs flashback), se declara el criterio y se respeta
  consistentemente.
- Si la alternancia distingue intensidad dramática (presente
  para escenas culminantes), se declara el umbral; sin umbral
  declarado, la decisión queda al arbitrio de cada capítulo y
  produce inconsistencia detectable.

### COMPATIBILIDAD CON IDIOLECTO

La elección de tiempo verbal dominante precede al idiolecto y
lo enmarca. Un idiolecto declarado opera dentro del tiempo
elegido; sus rasgos (registro léxico, sintaxis característica,
fijaciones perceptivas, lo que la voz no nombra) modulan la
prosa pero no transgreden el marco temporal. Si un rasgo de
idiolecto exige fricción con el marco temporal (narrador que
salta a presente histórico en momentos de crisis perceptiva,
por ejemplo), esa fricción pertenece a ALTERNANCIA DECLARADA
y se documenta allí, no como rasgo silencioso del idiolecto.

---

## INDIRECTO LIBRE

El estilo indirecto libre es el mecanismo por el cual el narrador
filtra el mundo a través del léxico y las categorías de un
personaje sin necesidad de verbos de percepción ("pensó",
"sintió"). Es uno de los recursos más potentes de la narración
literaria y uno de los más mal usados.

### CÓMO FUNCIONA
Se usa tercera persona gramatical pero léxico, ritmo, giros y
juicios son del personaje.

Ejemplo sin indirecto libre:
"Pensó que el oficial era un idiota."

Con indirecto libre:
"El oficial: un idiota acabado, de esos que respiran por el
reglamento y mueren por él."

El narrador no ha dicho que el oficial sea idiota. Ha filtrado
el mundo por el juicio del personaje.

### REGLAS DE USO
- Mantener coherencia: si se decide filtrar un pasaje por el
  personaje X, no mezclar juicios del personaje Y en el mismo
  pasaje sin marcar la transición.
- El indirecto libre permite que la voz narradora "hable como"
  el personaje sin perder la tercera. Esto da acceso psicológico
  sin sacrificar distancia.
- En régimen minimalista (ver AESTHETIC_REGISTER.md), el
  indirecto libre es escaso y preciso. En régimen expansivo,
  es el tejido principal.

### ERROR COMÚN
Mezclar sin aviso: tres párrafos en indirecto libre del
personaje X, seguidos de un párrafo de juicio del narrador
externo, sin transición marcada. El lector pierde orientación
epistemológica.

### TRANSICIONES
Para marcar el paso entre voces, hay varios mecanismos:
- Cambio de párrafo (el más sutil)
- Frase puente con verbo de percepción que recentra
- Espacio en blanco mayor
- Capítulo o sección nueva

---

## NARRADOR NO FIABLE

Un narrador no fiable miente al lector, voluntaria o
involuntariamente. Esto es distinto a tener puntos ciegos.

### TIPOS DE NO FIABILIDAD
- El narrador miente consciente para el lector (rara vez
  funciona; el lector siente manipulación).
- El narrador miente para sí mismo (el caso más poderoso:
  el lector entiende gradualmente que lo que se le cuenta
  no es lo que pasó).
- El narrador no sabe lo que ignora (niño, testigo limitado,
  herida cognitiva).
- El narrador omite por pudor o por culpa (omisión que
  el lector detecta como tal).

### GESTIÓN
Si se elige narrador no fiable:
- Decidir qué tipo.
- Decidir qué grado de acceso tiene el lector a la verdad.
- Proveer pistas: la no-fiabilidad debe ser detectable,
  aunque sea en relectura.
- No abusar: la no-fiabilidad total destruye la inversión
  del lector.

### DETALLES OPERATIVOS
Un narrador que miente para sí mismo no contradice
visiblemente la realidad: sesga la interpretación. Lo que miente
es el cómo lee el mundo, no el qué ocurrió. Los hechos duros
deben ser verificables por el lector a partir de cómo los otros
personajes reaccionan.

---

## COORDINACIÓN MULTI-POV

Si la novela tiene múltiples POVs, hay decisiones de arquitectura.

### DISTRIBUCIÓN
Por capítulo: cada capítulo una voz. Cómodo para el lector.
Por sección: varias secciones por capítulo, cada una una voz.
Flexible pero exige más del lector.
Por escena: transiciones más frecuentes. Arriesgado; con
frecuencia mejor no hacerlo.

DECLARAR LA REGLA Y MANTENERLA. Cambios de régimen a mitad
son posibles pero deben tener función.

### DISTINCIÓN ENTRE VOCES
Si dos POVs suenan igual, una de las dos es innecesaria.
Cada voz debe tener:
- Registro léxico distinto.
- Sintaxis distinta.
- Fijaciones distintas.
- Puntos ciegos distintos.

Ejercicio de verificación: cubrir el nombre del POV al principio
de una escena. ¿Se identifica por la prosa? Si no, las voces
no están diferenciadas.

### INFORMACIÓN DESIGUAL
Los distintos POVs saben cosas distintas. Esto genera ironía
dramática si se gestiona bien, y confusión si se gestiona mal.

Registrar, en CONTINUITY_PHYSICS.md, qué sabe cada POV en cada
momento. Los cambios de POV explotan estas asimetrías.

### FRECUENCIA DE REPETICIÓN
Un POV que no vuelve durante muchos capítulos se olvida. Si al
reaparecer necesita "ponerse al día", algo está fallando
estructuralmente.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — IDENTIFICACIÓN DE VOZ
Una página al azar, sin contexto: ¿se identifica la voz?

TEST 2 — PUNTO CIEGO COHERENTE
¿Los puntos ciegos declarados se mantienen en toda la novela
o hay escenas en que el narrador "ve lo que no podría ver"?

TEST 3 — FIJACIONES ACTIVAS
¿Las fijaciones perceptivas aparecen con frecuencia suficiente
como para ser reconocibles? Si una fijación solo aparece una
vez, no es fijación: es detalle.

TEST 4 — INDIRECTO LIBRE CONSISTENTE
Cuando se usa indirecto libre, ¿se mantiene puro o se mezcla
sin aviso con juicio externo?

---

## RELACIÓN CON OTROS ARCHIVOS

VOICE_ARCHITECTURE.md recibe de:
- CHARACTER_PHYSICS.md (herida → punto ciego)
- AESTHETIC_REGISTER.md (compatibilidad de voces con régimen)
- SCALE_CALIBRATION.md (número manejable de voces)

VOICE_ARCHITECTURE.md alimenta:
- Toda escritura en OPERACIÓN B
- SEMANTIC_OMISSION.md (lo que el narrador no puede ver no se nombra)
- SUBTEXT_MECHANICS.md (el narrador puede no entender lo que muestra)
- PROSODY_AND_MUSIC.md (la voz es la musicalidad de base;
  cada voz tiene cadencia propia)
- SEAMS_AND_HINGES.md (en multi-POV, las transiciones de voz
  entre capítulos son bisagras que requieren mecánica propia)
- PROSE_LINE_DISCIPLINE.md (cada voz puede sobrescribir
  localmente las cuotas globales declaradas allí mediante el
  idiolecto declarado en su ficha; la declaración explícita es
  condición de legitimidad de la sobreescritura)

VOICE_ARCHITECTURE.md se revisa:
- OPERACIÓN D, especialmente para verificar que voces múltiples
  no se han contagiado entre sí.
- PASADA 3 del REVISION_PROTOCOL (pasada de voz).

La sección TIEMPO VERBAL DOMINANTE de este archivo introduce
coordinaciones específicas con archivos del catálogo donde el
marco temporal de la voz tiene consecuencias operativas:
- AESTHETIC_REGISTER.md: cada tiempo de la sección TIEMPO
  VERBAL DOMINANTE tiene compatibilidades declaradas con los
  regímenes del inventario; la elección de tiempo y la
  elección de régimen se cruzan en la declaración global.
- PROSODY_AND_MUSIC.md: el tiempo verbal dominante condiciona
  la cadencia (el presente histórico tiende a uniformidad sin
  modulación; el pretérito integra digresión sin disonancia);
  la prosodia debe coordinarse con el marco temporal elegido.
- REVISION_PROTOCOL.md (PASADA 3): la verificación de
  consistencia del tiempo verbal y de las alternancias
  declaradas se ejecuta en la pasada de voz; cualquier cambio
  de tiempo no declarado se trata como error, no como
  virtuosismo.
- En multi-POV, la asignación voz × tiempo declarada en
  ALTERNANCIA DECLARADA es punto de control de
  COORDINACIÓN MULTI-POV de este mismo archivo: cada voz
  conserva su tiempo dominante asignado a lo largo de la
  novela.


---
---

