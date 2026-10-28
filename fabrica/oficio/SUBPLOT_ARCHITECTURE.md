<!-- Fábrica v3.0 — SUBPLOT_ARCHITECTURE: base de oficio + adenda de dark romance (v2.0) -->

# SUBPLOT_ARCHITECTURE.md

## PROPÓSITO

STORY_SPINE.md diseña la columna vertebral de la novela: la secuencia
de presiones sobre la pregunta central según la plantilla estructural
elegida. Este archivo diseña las ramas: las subtramas que corren en
paralelo a la principal con su propia función dramática, su propia
distribución temporal y sus propios puntos de cruce con la columna.

Sin archivo dedicado, las subtramas se improvisan capítulo a capítulo
y producen tres síntomas recurrentes: subtramas que no aportan (su
ausencia no se notaría); subtramas que compiten con la principal por
atención del lector y debilitan ambas; subtramas que se abandonan a
mitad sin que el autor lo registre, dejando promesas incumplidas que
el lector sí registra como hueco.

JERARQUÍA: Capa 1, derivado de STORY_SPINE. No puede completarse antes
de THEMATIC_ENGINE.md, CHARACTER_PHYSICS.md y STORY_SPINE.md. Si se
intenta, las subtramas serán decorativas (no encarnan la pregunta
central) o competitivas (toman materia de la principal).

CONDICIONALIDAD DE APLICACIÓN: archivo opcional según escala de
SCALE_CALIBRATION. Novela corta lo omite (no hay espacio para
subtrama significativa); novela media lo activa con una subtrama;
novela larga y extensa lo activan con varias.

---

## DECLARACIÓN DEL NÚMERO MANEJABLE DE SUBTRAMAS POR ESCALA

El número de subtramas que la novela puede sostener depende de la
escala declarada en SCALE_CALIBRATION.md. Sostener más subtramas de
las que la escala permite produce subtramas anémicas (sin presencia
suficiente para registrar) o expansión no declarada de la escala (la
novela crece más allá del rango previsto).

NOVELA CORTA (40-60k):
- Subtramas significativas: 0.
- Si el proyecto siente la necesidad de subtrama, suele indicar que
  la principal no carga suficiente densidad: revisar STORY_SPINE.

NOVELA MEDIA (70-110k):
- Subtramas significativas: 1.
- Una subtrama bien construida; nunca dos en este rango sin riesgo
  de anemia.

NOVELA LARGA (120-180k):
- Subtramas significativas: 2-4.
- Cada una con estructura interna propia, distribuida temporalmente
  con cuidado.

NOVELA EXTENSA (200k+):
- Subtramas significativas: 4 o más, según estructura modular.
- En estructura modular (partes, libros, secciones), cada bloque
  puede sostener su propio repertorio de subtramas; el archivo
  registra subtramas de novela completa y subtramas de bloque por
  separado.

ESTRUCTURA CORAL O MOSAICO (STORY_SPINE plantilla 4):
- En estructura coral, la distinción entre principal y subtrama se
  diluye: cada línea es una columna y la convergencia temática es lo
  que las une. Este archivo se reescribe como mapa de líneas más
  que como inventario de subtramas, pero la disciplina de función,
  distribución y cruce sigue aplicando línea por línea.

---

## DECLARACIÓN DE SUBTRAMAS ACTIVAS

Para cada subtrama del proyecto:

NOMBRE O TEMA: [identificador corto que el autor reconoce; puede
coincidir con el tema central de la subtrama o con el nombre del
personaje protagonista de ella]

FUNCIÓN RESPECTO A LA PRINCIPAL: [una de las funciones de la
TIPOLOGÍA, o combinación declarada]

PERSONAJE PRINCIPAL DE LA SUBTRAMA: [típicamente personaje secundario
o tritagonista con ficha en CHARACTER_PHYSICS.md plantilla C, en
algunos casos personaje-secundario que el proyecto promueve a
plantilla A para sostener subtrama]

PREGUNTA ENCARNADA: [la pregunta central de THEMATIC_ENGINE puede
manifestarse en la subtrama de modo distinto a como lo hace en la
principal; declararlo aquí permite verificar que la subtrama añade y
no resta al motor temático]

DISTRIBUCIÓN TEMPORAL EN EL ARCO: [cuándo abre, cuándo escala, cuándo
cierra, expresado en fases de la plantilla estructural elegida en
STORY_SPINE]

PUNTOS DE CRUCE CON LA PRINCIPAL: [al menos uno, idealmente dos o
tres; cada cruce modifica algo en al menos una de las dos líneas]

DEUDAS DE SUBTRAMA: [setups que la subtrama abre y debe pagar; estas
deudas se registran en CONTINUITY_PHYSICS.md con etiqueta de subtrama]

CIERRE: [cómo cierra la subtrama, en qué fase de la principal, con
qué efecto sobre el lector]

---

## TIPOLOGÍA FUNCIONAL DE SUBTRAMA

### SUBTRAMA DE CONTRASTE

Función: muestra lo opuesto a la principal para que la principal se
vea con relieve. Si el protagonista lucha con su herida, la subtrama
muestra a otro personaje que ha cedido ante la suya. Si el arco
principal sube, la subtrama baja; si la principal cierra abierta, la
subtrama cierra cerrada.

Riesgo específico: el contraste demasiado simétrico se siente
esquemático. La subtrama de contraste eficaz tiene su propia
verdad, no es solo espejo invertido.

### SUBTRAMA DE ESPEJO

Función: muestra el mismo dilema en escala distinta o en otra
encarnación. Si la pregunta central de THEMATIC_ENGINE pregunta sobre
lealtad y traición a través del protagonista, la subtrama la
pregunta sobre lealtad y traición a través de un secundario en
contexto distinto. La acumulación de manifestaciones de la pregunta
densifica el motor temático.

Riesgo específico: si la subtrama responde a la pregunta de modo
declarativo, redundancia; si la responde de modo distinto, la novela
gana una segunda voz. Verificar que la subtrama no resuelve la
pregunta antes que la principal.

### SUBTRAMA DE ESCALADA PARALELA

Función: tensa por su cuenta y se cruza con la principal en el clímax
o cerca de él. Tiene su propio detonante, sus propias escaladas, su
propia crisis. La convergencia con la principal en el momento alto
de la novela aumenta la presión sobre el clímax.

Riesgo específico: si la subtrama no llega al clímax con tensión
suficiente, la convergencia se siente como añadidura. Si llega con
demasiada tensión, compite con la principal y debilita el clímax.

### SUBTRAMA DE PROFUNDIZACIÓN TEMÁTICA

Función: explora una dimensión de la pregunta central que la
principal no toca. La principal puede no permitir que el
protagonista, dada su física, formule cierta posibilidad; la
subtrama deja que un secundario la encarne. La novela completa la
exploración temática sin forzar al protagonista.

Riesgo específico: la subtrama se siente como ensayo si su
encarnación es declarativa. La profundización temática eficaz pasa
por situación dramática, no por monólogo del personaje.

### SUBTRAMA DE ALIVIO

Función: respira al lector entre escaladas de la principal. En
novelas de alta densidad emocional o de tensión sostenida, la
subtrama de alivio permite que el lector regrese a la principal con
el aparato perceptivo descansado. El alivio puede ser cómico,
costumbrista, descriptivo, lírico.

Riesgo específico: si el alivio no comparte tono ni preocupación con
la principal, se siente como interrupción. El alivio bien
construido alivia sin desconectarse.

### SUBTRAMA DE CONTRAPUNTO MORAL

Función: encarna posición ética distinta a la del protagonista,
permitiendo que la pregunta central se examine desde otro vector
moral. El contrapunto moral no es antagonismo (ese vive en
CHARACTER_PHYSICS plantilla B): es legitimidad otra.

Riesgo específico: si la posición del contrapunto se presenta como
inferior a la del protagonista, deja de ser contrapunto y se vuelve
straw man; si se presenta como superior, la novela está confesando
que el protagonista es el equivocado y debería redeclararse.

---

## DISTRIBUCIÓN TEMPORAL Y RITMO

### REGLA DE PRESENCIA REGULAR

Una subtrama no puede abrir en el primer cuarto del libro y
desaparecer hasta el último capítulo: el lector la habrá olvidado y
su retorno se sentirá exógeno. Debe aparecer al menos una vez en
cada bloque mayor de la plantilla estructural (Acto I, II, III en
tres actos; KI, SHŌ, TEN, KETSU en kishōtenketsu; cada bloque del
arco cumulativo en episódica con arco; etc.).

### REGLA DE NO CONCENTRACIÓN

Una subtrama no puede concentrarse en un único bloque sin
manifestación previa ni posterior: se sentirá como cuerpo extraño,
no como subtrama. Si el proyecto necesita un bloque de un personaje
secundario sin distribución previa, está pidiendo otra cosa
(sección, capítulo de POV específico, intermezzo declarado), no
subtrama.

### PUNTOS DE GIRO INTERNOS

Cada subtrama significativa debe tener al menos un punto de giro
interno propio: un momento donde su propio arco cambia de
dirección. Sin punto de giro interno, la subtrama es presencia
pasiva del personaje secundario, no arco con tracción.

### CADENCIA DE APARICIÓN

La cadencia de aparición de cada subtrama se registra en
INFORMATION_CHOREOGRAPHY.md como hechos activos del registro de
revelación. La subtrama es activa cuando su línea avanza; está
latente cuando el lector la recuerda pero no avanza; está cerrada
cuando ha resuelto su arco. La cadencia mezcla los tres estados.

---

## PUNTOS DE CRUCE CON LA PRINCIPAL

### REGLA DE CRUCE OBLIGATORIO

Cada subtrama tiene al menos un punto donde cruza la línea de la
principal y modifica una de las dos. El cruce que solo informa al
protagonista de algo que pasa en la subtrama no es cruce: es
exposición. El cruce eficaz cambia la dirección de al menos una
línea.

### TIPOS DE CRUCE

CRUCE POR ACCIÓN: el personaje de la subtrama hace algo que cambia
el campo de juego del protagonista. Modifica la principal.

CRUCE POR INFORMACIÓN PESADA: la subtrama produce una información
que el protagonista recibe y que cambia su trayectoria. La
información debe ser pesada (cambia decisión, no solo conocimiento).

CRUCE POR PRESIÓN COMPARTIDA: ambas líneas se ven sometidas al mismo
evento exógeno (catástrofe, presión social, crisis política) que las
modifica simultáneamente. El cruce es indirecto pero modificador.

CRUCE POR ESPEJO REVELADO: el protagonista percibe (sin que se le
diga) que la subtrama encarna su propia pregunta. El cruce no
modifica trayectoria pero sí percepción: es cruce legítimo en
novelas literarias o contemplativas.

### DISTRIBUCIÓN DE LOS CRUCES

Una subtrama de escalada paralela típicamente cruza al menos tres
veces (apertura, mitad, clímax convergente). Una subtrama de
contraste o espejo puede cruzar solo dos veces (introducción del
contraste, manifestación final). Una subtrama de alivio puede
cruzar solo en su cierre. Cada subtrama declara aquí su mapa de
cruces.

---

## DEUDAS DE SUBTRAMA

Las subtramas abren deudas narrativas como la principal lo hace.
Estas deudas:

- SE REGISTRAN en CONTINUITY_PHYSICS.md con etiqueta explícita de
  subtrama (deuda de subtrama, no deuda principal).
- SE PAGAN antes del cierre de la subtrama, no del cierre de la
  novela: una subtrama que termina dejando deudas abiertas debe
  declararlas como deudas heredadas a la principal o como cierre
  abierto consciente.
- NO COMPITEN con las deudas de la principal en el inventario
  general: se contabilizan en su propio bloque del registro.

DISTINCIÓN OPERATIVA:
- DEUDAS ESTRUCTURALES (registradas en STORY_SPINE.md): de la
  columna principal.
- DEUDAS DE SUBTRAMA (registradas aquí, sincronizadas con
  CONTINUITY_PHYSICS): de las ramas.
- DEUDAS DE MUNDO (si WORLD_ARC.md activo): de la trayectoria
  multilibro del mundo.
- DEUDAS DE SERIE (si SERIES_ARCHITECTURE.md activo): del arco de
  personaje multilibro.

Cada categoría tiene sus criterios de payoff. La confusión entre
categorías es error frecuente: una deuda de subtrama que el autor
trata como deuda estructural fuerza a la principal a cerrarla; una
deuda estructural que el autor trata como deuda de subtrama queda
sin pagar al cierre de la novela.

---

## TESTS DE FUNCIONAMIENTO

### TEST 1 — FUNCIÓN DECLARADA

Para cada subtrama, articular en una frase: ¿qué aporta esta
subtrama que la novela perdería si no existiera? Si la respuesta es
vaga ("da contexto", "humaniza al protagonista"), la subtrama no
tiene función declarable y debería eliminarse o redeclararse.

### TEST 2 — DISTRIBUCIÓN

Trazar el mapa de apariciones de cada subtrama por bloques
estructurales. ¿Tiene presencia en cada bloque mayor? ¿Tiene puntos
de giro internos propios? Si está concentrada en un único bloque o
si carece de puntos de giro, redeclarar (puede ser un capítulo
sostenido, no una subtrama).

### TEST 3 — CRUCE EFECTIVO

Para cada subtrama, identificar sus puntos de cruce con la
principal. ¿Cada cruce modifica al menos una línea? Si algún cruce
solo informa, no modifica, redeclarar como exposición o construir el
cruce con tracción.

### TEST 4 — NÚMERO ADECUADO A LA ESCALA

Cruzar el número de subtramas declaradas con la escala declarada en
SCALE_CALIBRATION. Si el número excede la escala, evaluar: ¿una de
ellas es realmente subtrama o es secundario sin arco? ¿La novela
está creciendo más allá de su escala declarada y procede redeclarar
SCALE?

### TEST 5 — DEUDAS PAGADAS

Al cierre de la novela, cada subtrama tiene su inventario de deudas
abiertas. ¿Están pagadas o declaradas como cierre abierto consciente?
La deuda de subtrama abierta sin declaración produce el síntoma de
"falta algo en esa parte" que el lector percibe pero no localiza.

### TEST 6 — ENCARNACIÓN DE LA PREGUNTA CENTRAL

Cada subtrama declara cómo encarna la pregunta de THEMATIC_ENGINE.
Si una subtrama no encarna la pregunta, evaluar: ¿es subtrama de
alivio (admite manifestación temática lateral) o es subtrama anémica
(no aporta al motor)?

---

## INSTRUCCIÓN OPERATIVA

Antes de escribir un capítulo en CHAPTER_BRIEF, verificar:
- ¿Avanza este capítulo la principal, una subtrama o ambas?
- Si avanza una subtrama, ¿es de las declaradas en este archivo?
- ¿La subtrama está donde le toca según su distribución temporal?
- ¿Este capítulo es un punto de cruce? Si lo es, ¿el cruce modifica
  al menos una de las dos líneas?

CHAPTER_BRIEF debe declarar explícitamente, cuando un capítulo avanza
subtrama, qué subtrama avanza y en qué momento de su arco está.

---

## RELACIÓN CON OTROS ARCHIVOS

SUBPLOT_ARCHITECTURE.md recibe de:
- STORY_SPINE.md (la columna sobre la cual se inscriben las ramas;
  la plantilla estructural elegida determina qué bloques estructurales
  son fases para distribuir las subtramas).
- THEMATIC_ENGINE.md (la pregunta central que cada subtrama debe
  encarnar de algún modo, salvo subtrama de alivio declarada).
- CHARACTER_PHYSICS.md (cada subtrama tiene su personaje principal,
  cuya ficha existe en aquel archivo, típicamente plantilla C).
- SCALE_CALIBRATION.md (el número manejable de subtramas según
  escala declarada).

SUBPLOT_ARCHITECTURE.md alimenta:
- CHAPTER_BRIEF.md (qué subtrama avanza este capítulo, en qué
  momento de su arco está).
- CONTINUITY_PHYSICS.md (registro sincronizado de deudas de
  subtrama, distinguidas de deudas estructurales y deudas de mundo).
- INFORMATION_CHOREOGRAPHY.md (cadencia de aparición de cada
  subtrama como hecho activo en el registro de revelación al
  lector).
- SCENE_NECESSITY.md (las escenas de subtrama se justifican por su
  posición en el arco de la subtrama, no en el de la principal).

SUBPLOT_ARCHITECTURE.md está subordinado a:
- STORY_SPINE.md (las subtramas no pueden contradecir la columna;
  si una subtrama exige modificación de la principal, redeclarar
  STORY_SPINE).
- SERIES_ARCHITECTURE.md (si el proyecto es multivolumen, las
  subtramas pueden tener arco multilibro con su propia distribución
  por libros declarada en aquel archivo).
- GENRE_CONVENTIONS.md (algunos géneros tienen convenciones sobre
  número y tipo de subtrama: el thriller comercial tolera mal más
  de una subtrama; la novela negra suele tener subtrama personal
  del detective; el romance puede tener subtrama de personaje
  secundario que cierra antes de la principal).

SUBPLOT_ARCHITECTURE.md se revisa:
- En OPERACIÓN 0 (FUNDACIÓN), tras STORY_SPINE.
- En OPERACIÓN D (auditoría estructural) cada 3-5 capítulos:
  verificar que las subtramas avanzan según calendario, que sus
  puntos de cruce se están construyendo, que sus deudas se
  registran.
- En PASADA 1 del REVISION_PROTOCOL (auditoría estructural completa,
  verificar que todas las deudas de subtrama están pagadas o
  declaradas como cierre abierto consciente).

---

## ERROR COMÚN

Tratar como subtrama lo que es presencia de un personaje secundario
sin arco. Un personaje secundario con voz e idiolecto declarado en
CHARACTER_PHYSICS plantilla C no necesariamente sostiene subtrama:
puede simplemente acompañar al protagonista. La subtrama exige arco
con su propio detonante, sus propias escaladas, su propio cierre.

El segundo error común: confundir digresión con subtrama. Un
capítulo dedicado a un personaje secundario sin arco no es
subtrama; es bloque de POV o intermezzo. Se gestiona en
CHAPTER_BRIEF como capítulo especial, no en este archivo.

El tercer error común: forzar una subtrama porque la novela "pide
más". Si la principal no carga densidad suficiente, la subtrama no
la repondrá; añadirla diluye en lugar de reforzar. Antes de
declarar subtrama, verificar que la principal está bien construida
en STORY_SPINE.


---
---

