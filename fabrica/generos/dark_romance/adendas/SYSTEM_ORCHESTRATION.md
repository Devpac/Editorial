# SYSTEM_ORCHESTRATION.adenda.md

## ADENDA DE ESPECIALIZACIÓN — MODELO_DarkRomance v2.0 (género)

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

> Especializa la plantilla agnóstica de arriba, que se conserva **verbatim** (base v7) salvo
> en lo que deroga §0. Donde base y género choquen, gana el género. En el peso de la
> pareja manda `PAREJA_PRIMERO.md` (v2.0).
> DECISIÓN: ESPECIALIZA. **Es de género:** vale para cualquier saga de dark romance; los valores
> de la obra (nombres, paletas, contadores, extensión) viven en su preset, `PRESET_<OBRA>.md`
> (la obra activa la dice su cuaderno: `LEEME.md` §1).

### 0. QUIÉN HACE QUÉ *(v1.3)*

La obra la dirige una ventana **orquestador** (`ORQUESTADOR.md`): encarga cada trabajo con un
`NEXT.md`, lo audita con lectoras sin contexto (C.5), corrige con cortes y lleva la memoria.
Esta adenda rige el trabajo de las **ventanas de trabajo** que escriben los capítulos; las fases
previas (biblia, preset, escaletas) tienen sus plantillas (`PLANTILLA_BIBLIA.md`,
`PLANTILLA_PRESET.md`, `PLANTILLA_ESCALETA.md`) y se encargan igual, con `PLANTILLA_NEXT.md`.

**Lo que la base dice de los traspasos entre ventanas y aquí no rige:**
- **El NEXT** tiene las ocho secciones de `PLANTILLA_NEXT.md`, no las seis de la base, y **lo
  escribe el orquestador**, no la ventana saliente (`ORQUESTADOR.md` §3). `NEXT.md` es el encargo
  vivo de la obra; la plantilla es `PLANTILLA_NEXT.md`. Donde la base manda «emitir NEXT» al
  cerrar una ventana (ARQUITECTURA DE CAPAS, AUTONOMÍA Y DECISIÓN, SECUENCIA COMPLETA,
  TRANSICIÓN ENTRE VENTANAS), la
  ventana de trabajo deja su acta o su informe y el orquestador escribe el NEXT siguiente.
- **BRIEFING** no es un archivo aparte que cada ventana lea al arrancar y actualice al cerrar: el
  briefing de saga lo forman el cuaderno, el estado de cierre de cada `continuidad.md` y las
  ranuras de saga del preset (`ORQUESTADOR.md` §9), y `BRIEFING.md` es la plantilla de género de
  la declaración de cada libro. Una ventana de trabajo arranca con el LEEME y el NEXT; lo demás
  que lee, se lo dice el NEXT.
- **`MODELO_AGNOSTICO_v7_APERTURA.md`** no forma parte de la fábrica: la referencia de la base a
  su SECCIÓN 11 queda sin efecto. Los tres sesgos que la base nombra se leen como aviso, y su
  adaptación local es legítima cuando está formulada.

### 1. PRECEDENCIA SOBRE LAS ADENDAS HEREDADAS *(v2.0)*

**De cada plantilla rigen su cuerpo de oficio y su adenda de género; nada más**
(`PAREJA_PRIMERO.md` §5). No rige ninguna capa heredada de otro modelo. Caen, por si asoman:

- el final feliz cerrado por libro (HEA/HFN) y la coda cálida, salvo en la forma de saga
  de parejas rotativas (SERIES_GLUE, adenda de dark romance; la forma la declara la obra);
- la puerta cerrada y cualquier techo de proximidad física: rige la explicitud plena
  (`GENRE_CONVENTIONS`, regla 7);
- el gancho solo de intriga y la prohibición de cerrar capítulos en la pareja;
- las parejas rotativas y la serie de standalones como forma obligatoria: son una de las
  tres formas de saga de dark romance, y solo rigen si la obra la declara;
- la extensión de 70.000 palabras y la cuota de ~1.150 palabras por capítulo: rige la
  extensión que declara la biblia de la obra (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION);
- la «voz de la dama» y la tercera persona: rigen la persona, el tiempo y la alternancia que
  declara la biblia (en dark romance, lo habitual es primera persona, presente y dos
  narradores).

**`PAREJA_PRIMERO.md` manda sobre cualquier plantilla en el peso de la pareja**; la biblia
solo baja sus suelos por decisión del autor (B1, 🔒).
**La biblia manda sobre cualquier plantilla en las cifras y parámetros de prosa** (su régimen
estético: régimen, estado, tolerancias, metáfora, frases por párrafo). **Las cuotas de
prosa son siempre alarma de cierre**, con el ESTADO del régimen en `PROVISIONAL` o fuera de
él (PROSE_LINE_DISCIPLINE, adenda): los números de AESTHETIC_REGISTER y
PROSE_LINE_DISCIPLINE son referencia y alarma en el cierre, nunca objetivo.

### 2. LA OPERACIÓN 0 VIVE EN LA BIBLIA

En una saga de dark romance la fundación no se rellena plantilla a plantilla en cada libro. La
cumplen tres documentos de instancia, que produce la obra en sus fases 1–3 (`ORQUESTADOR.md`):

- **la biblia de la saga** (`<obra>_biblia.md`): registro, género, tema, personajes,
  relaciones, mundo, cronología, trama horizontal, idiolectos;
- **el preset de la obra** (`PRESET_<OBRA>.md`): los valores que leen las plantillas de género
  (fichas, voces, paletas, contadores, ritmo de consumación, escala, calendario de datos);
- **la escaleta del libro** (y su ampliada): la columna de la pareja, capítulo a capítulo,
  cada ficha con «Entre ellos», si están los dos y su peso de pareja estimado, POV y cierre;
  la trama B, trenzada sobre ella.

Las plantillas se **consultan** para decidir; no se vuelven a rellenar desde cero. La
VERIFICACIÓN AL FINALIZAR OPERACIÓN 0 se hace contra la biblia y la escaleta.

**Las plantillas no se rellenan nunca durante la escritura.** Todo lo que la base manda
«actualizar» en una plantilla (CONTINUITY_PHYSICS, NARRATIVE_CHRONOLOGY,
INFORMATION_CHOREOGRAPHY, CLUE_LEDGER) se lleva en la instancia del libro:
`libro_NN/continuidad.md`. Lo que una plantilla debería cambiar va al acta como fricción.

**Antes y después de escribir.** Antes de escribir se lee la obra (biblia, escaleta,
capítulos anteriores, `continuidad.md`) y las plantillas de género con su sección del preset
**como contrato de canon**. Los protocolos previos de las plantillas (por ejemplo, el protocolo
de cierre de DIALOGUE_MECHANICS) y los filtros de CAPA 3 (SEMANTIC_OMISSION,
SUBTEXT_MECHANICS, SENSORY_HIERARCHY, PROSE_LINE_DISCIPLINE, VOICE_ARCHITECTURE) **se leen
después del borrador**, en el cierre.

**Canon oculto.** La biblia guarda canon que no sale todavía en página (el pasado que se
revela en libros posteriores, los datos del calendario de datos horizontales). Regla: **lo que la escaleta no pone
en página en ese capítulo, no sale**, aunque esté en la biblia. El NEXT nombra los vetos
más tentadores del capítulo.

**Investigación sin informante.** Si la escaleta marca un capítulo como bloqueado por una
pregunta de investigación y no hay informante, **no se para**: se declara la licencia
siguiente libre (RL-LIC-NN) en el acta, se escribe sin detalle de procedimiento y la
pregunta sigue abierta (criterio por defecto; el autor puede cambiarlo en el cuaderno de la
obra).

**Referencias heredadas.** Si la biblia cita archivos de un modelo anterior, el preset de la
obra dice a qué archivo de este corresponden (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION).

**Pasos de la base que se aplican en una saga:**
- OPERACIÓN 0.5: solo el brief de una hoja (adenda de CHAPTER_BRIEF), consultando la
  escaleta, `continuidad.md`, ROMANCE_BEAT_MAP y CLUE_LEDGER. Los demás pasos de consulta
  de la base ya los cubren la biblia y la escaleta.
- OPERACIÓN A: se piensa la escena (existe o se elide, forma, tensión, sentido dominante);
  no se rellena SCENE_SHAPE ni otro archivo.
- OPERACIÓN C: pasos 1–7 de la base y C-1 a C-10 de esta adenda; los pasos 8–11 de la base
  se hacen en `continuidad.md`.
- OPERACIÓN D *(v2.0)*: la secuencia de la base con 19–21 de esta adenda, entera al cerrar el
  libro y corta con cada lectura externa (§4).

### 3. CATÁLOGO DE GÉNERO

- **`PAREJA_PRIMERO.md`** *(v2.0)* — al frente del catálogo: la pareja es la trama A de cada
  libro y de cada capítulo. Manda sobre cualquier plantilla en el peso de la pareja (cómo se
  mide, §2; por defecto, objetivo 80 % y suelo 70 %) y en los suelos de género (§3). No es
  instrucción de prosa: se aplica en el diseño y en las comprobaciones de cierre y de lectura (§6).
- **ROMANCE_BEAT_MAP.md** — CAPA 1, con prioridad sobre STORY_SPINE *(v2.0)*: la columna de
  cada libro (los beats de la pareja, con su % y su suelo), el calendario de calor y la escala
  de rendición a lo largo de la saga; STORY_SPINE trenza sobre ella la trama B.
- **CLUE_LEDGER.md** — CAPA 2 transversal: pistas de la trama del libro
  (*Variante: dark romance policial:* del caso), dimensionadas para caber en el techo de lo que
  no es pareja (por defecto, el 30 %), migas de pan de la trama horizontal (si la hay), la firma del
  antagonista de saga (si la hay) y **calendario de datos horizontales**.
- **HEAT_DISCIPLINE.md** — CAPA 3: explicitud plena, cortes dramáticos y no de pudor,
  ritmo de consumación y consentimiento por familia de actos (reescrita en la v1.1); en la
  v2.0, el calendario de calor con sus suelos, que es estructura (escaleta y OPERACIÓN D).
- **SERIES_GLUE.md** y **SERIES_ARCHITECTURE.md** — CAPA 0.5: sus adendas de dark romance
  *(v1.3)* declaran las tres formas de saga del género (la misma pareja en muchos libros con
  trama horizontal; el dúo o trilogía de una pareja; las parejas rotativas en un mundo
  compartido) y qué cierra cada libro y qué queda abierto. La obra declara su forma en el
  preset.

### 4. LUGAR EN LAS OPERACIONES

- **OPERACIÓN 0.5 — Brief.** *(v2.0)* El brief **empieza por qué cambia entre ellos**: el
  «Entre ellos» de la ficha, si están los dos y el beat de la pareja en curso
  (ROMANCE_BEAT_MAP, con la posición en la escala de rendición). Después, lo que pone la
  trama B (CLUE_LEDGER: miga, pistas y datos horizontales con fecha de entrada, si los hay).
  El brief es corto: qué cambia entre ellos, función única, deltas, escenas y gancho.
  **No prescribe prosa.**
- **OPERACIÓN A — Escena.** Contenido cargado: modo MOSTRADO por defecto (violencia y
  sexo); la elipsis solo por ritmo o subtexto, nunca por decoro.
- **OPERACIÓN B — Escritura. REGLA DE NO PRESCRIPCIÓN.** Se confirma y endurece la base:
  ningún test, cuota, lista de prohibiciones ni filtro de CAPA 3 se convierte en
  instrucción previa a la escritura. Se escribe con delante: la biblia, la escaleta, el
  brief, el capítulo anterior y las fichas de voz. Las reglas de prosa son oído de fondo.
  Lo que se escape se caza en C y en C.5, no antes.
- **OPERACIÓN C — Cierre. OBLIGATORIA.** Un capítulo no está escrito hasta que tiene su
  acta de cierre. A los pasos de la base se añaden diez comprobaciones de género:
  - **C-1 Relectura de superficie.** Erratas, concordancias, persona verbal («cuando
    trabajo bien», no «cuando trabaja bien» en primera persona).
  - **C-2 Frase-resumen.** TIC 4 de PROSE_LINE_DISCIPLINE. En el POV del narrador hermético
    (si la obra lo tiene: `PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION), todo párrafo o remate que
    explique lo que significa algo **se corta**: observa y decide, no interpreta. Se quedan
    las excepciones que declara su idiolecto (`PRESET_<OBRA>.md` › PROSE_LINE_DISCIPLINE ›
    TIC 4: glosa y remate; PROSE_LINE_DISCIPLINE, adenda, TIC 4). En el del narrador irónico
    (si la obra lo tiene), la glosa se corta y el remate de idiolecto se queda.
  - **C-3 Paleta del POV.** Si la obra declara paletas por narrador
    (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION › Narradores y cierre), el narrador del capítulo trae la suya (lo que
    pone el entorno no cuenta como paleta). Los contadores de la obra
    (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION), dentro de su techo.
  - **C-4 Horas y cifras.** Registro 13 de CONTINUITY_PHYSICS: la aritmética de horas,
    duraciones y cifras cuadra con el propio capítulo y con los anteriores.
  - **C-5 Datos horizontales.** Calendario de datos horizontales (CLUE_LEDGER, llevado en
    `continuidad.md`): ningún dato de la trama horizontal (la herida de cada protagonista,
    el antagonista de saga) aparece en página antes de su capítulo asignado. Antes de su fecha, se alude
    sin dato.
  - **C-6 Asimetría de voces.** Test de VOICE_ARCHITECTURE (adenda Dark Romance): cada
    narrador lleva su rasgo también en la narración, no solo en el diálogo (el que la obra le
    declara en `PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION); si hay dos narradores, las voces se
    distinguen con el nombre tapado.
  - **C-7 Gancho.** El capítulo cierra empujando a pasar página (§5: por defecto, todos los
    cierres; la obra puede declarar cierres de descarga con su tope). *(v2.0)*
    Y se anota si es de pareja (lo que deja abierto es entre ellos, o el gancho de la trama B
    que cae sobre los dos o sobre uno por el otro: SEAMS_AND_HINGES, adenda), con la cuenta en
    `continuidad.md`, contra los suelos de `PAREJA_PRIMERO.md` §3 o los que declare el preset
    (por defecto: por libro, objetivo tres de cada cuatro y suelo dos de cada tres; por
    bloque de cuatro capítulos, objetivo tres de cuatro y suelo dos de cuatro). Por debajo del
    suelo, alarma en el acta, que avisa a la escaleta del bloque siguiente.
  - **C-8 Pudor y calendario de calor.** Tests 1, 3 y 6 de HEAT_DISCIPLINE *(v2.0: el 6,
    calor tardío)*: ¿algún beat de calor pasa de su suelo, o, desde el contacto con carga, van
    más de cuatro capítulos seguidos sin escena con carga (ventana móvil, no bloques fijos)? El
    calor que llega tarde no se arregla en la prosa: alarma en el acta y se reescaleta el
    bloque siguiente.
  - **C-9 Lo que la lectora ya ha leído** *(v1.2.2)*. (a) **Espejos entre POV** (si hay dos
    narradores): si el capítulo pasa por un lugar o un momento ya narrado desde el otro POV,
    comparte con él **un detalle como mucho** (el que hace la ironía); lo demás es lo que el
    otro no vio. Lo que la lectora ya ha leído no se vuelve a describir. (b) **Tics de
    idiolecto:** los tics vigilados de la obra (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION › Tics
    vigilados), cada uno dentro del techo que declara la obra y solo donde pesa (régimen
    estético de la biblia). (c) **Motivos que vuelven** (un chiste, un objeto, una frase
    hecha de un secundario): la segunda vez tiene que cambiar algo; si no, se corta. Se
    corrige cortando.
  - **C-10 Peso de la pareja** *(v1.2.2; v2.0)*. Con la unidad de `PAREJA_PRIMERO.md` §2
    (la sombra que no ocupa a quien narra no cuenta): qué parte del capítulo, en palabras, es
    de pareja, si están los dos en escena y qué cambia entre ellos, en una frase, frente al
    «Entre ellos» de la ficha. Va a `continuidad.md` (registro 12 de CONTINUITY_PHYSICS), con
    el acumulado del bloque y del libro. **El registro 12 bloquea el cierre**, como el 13: sin
    la fila contada y, si un suelo se rompe, sin su salida anotada en el acta, el capítulo no
    se cierra. Por debajo del objetivo (el de `PAREJA_PRIMERO.md` §2 o el que declare el
    preset; por defecto, 80 %), del capítulo o del bloque, **alarma**; si el bloque cerrado baja
    del suelo (por defecto, 70 %), **se reescaleta el bloque siguiente, nunca la prosa**. En la
    misma línea del acta (✔, o la que da alarma), las comprobaciones de pareja que otras
    plantillas mandan aquí: la tensión dominante (TENSION_MECHANICS, TEST 7), «nosotros dos»
    (CHARACTER_PHYSICS, TEST 13), el vector (RELATIONSHIP_PHYSICS, TEST 6), el hecho de
    pareja (INFORMATION_CHOREOGRAPHY, TEST 6), qué cambia entre ellos y la copresencia
    (SCENE_NECESSITY, TESTS 7 y 8) y, en un capítulo de la protagonista A, el protagonista B en
    su voz, en sus sentidos, en su análisis y en su página (adendas de VOICE_ARCHITECTURE y
    SENSORY_HIERARCHY; AESTHETIC_REGISTER, TEST 13; DIALOGUE_MECHANICS, TEST 12) y el deseo
    que acaba en la trama del libro (SUBTEXT_MECHANICS, adenda). No obliga a añadir: lo que se
    anota es la cuenta y la salida, que es reescaletar el bloque siguiente, nunca tocar la
    prosa; avisa a la lectura editorial y al NEXT siguiente.
  - **Salida: el acta** (`libro_NN/capNN_acta.md`), con este formato fijo: una línea por
    paso 1–7 de la base y por C-1 a C-10 (qué se miró y qué se corrigió); palabras finales;
    **fricciones de catálogo** (reglas que no ayudaron o chocaron); **propuestas de canon**
    (lo que el capítulo inventó y la biblia no tiene). Además se actualiza `continuidad.md`
    (estado, saber, registro 13, datos horizontales gastados y contadores, también los de
    pareja: `PLANTILLA_LIBRO.md`, contadores del libro).
- **OPERACIÓN C.5 — Lectura editorial. NUEVA Y OBLIGATORIA.** Encargos literales, paquete y
  listón en `PROTOCOLO_LECTURA.md`. Tras el cierre, lee el
  capítulo alguien que **no lo ha escrito** (un agente nuevo o una ventana nueva).
  - **Carga** (paquete de `PROTOCOLO_LECTURA.md` §2): el capítulo y los publicados
    anteriores, numerados como se publican y con la línea del narrador; la editora, además,
    la ficha de la escaleta. **No carga** biblia, brief, acta ni plantillas: lee como lectora
    y editora, no como verificadora de un plan.
  - **Quién lee, a la vez y por separado:** una **editora** (encargo literal en
    `PROTOCOLO_LECTURA.md` §3: notas de disfrute, pareja —qué parte del capítulo es suya—,
    voz, ficha y coherencia, repeticiones y prosa; tres mejores y tres peores momentos;
    errores de coherencia; tres correcciones mínimas como mucho) y una **lectora tipo** (§5:
    enganche, cuánto es romance, dónde salta o siente que le repiten algo, qué le falta).
  - **Formato del resultado** (`libro_NN/capNN_lectura_editorial.md`, §7 del protocolo):
    1. **Notas** de las dos (con el peso de pareja de la lectura junto al del acta) y **lo
       que funciona y no se toca**, con citas.
    2. **Tres problemas como máximo**, ordenados por daño a la lectora de dark romance:
       promesa de género y peso de pareja, voz, información gastada antes de tiempo,
       repetición, gancho, continuidad.
    3. **Corrección mínima** para cada uno, preservando la voz: cortar antes que añadir;
       añadir solo cuando falta un beat.
    4. **Lo que se queda aunque alguien lo pidiera cortar**, y por qué.
    5. **Lo que sube a canon**: hallazgos del capítulo mejores que la escaleta.
    6. **Avisos** para los capítulos siguientes (al plan de la lectora y al NEXT).
  - **Correctora de continuidad** *(v1.2.2)*: si las correcciones tocan más de un capítulo,
    relee el tramo un agente sin contexto (§7 del protocolo).
  - **Criterio:** el criterio de delegación de la obra (`CUADERNO_<OBRA>.md` §2; por defecto,
    el de `ORQUESTADOR.md` §1).
  - **Prohibido:** reescribir el capítulo entero; convertir la crítica en prescripciones
    para el capítulo siguiente (va como fricción al NEXT y, si es de catálogo, a la
    plantilla que corresponda).
  - **Lectora tipo** *(v1.2.1)*: además de la editora, lee el capítulo una lectora tipo de
    la saga (el perfil de lectora de la biblia), sin contexto,
    con los capítulos anteriores. Da una nota de **enganche**, dice dónde saltaría líneas y
    qué parte del capítulo es romance.
    Cuando editora y lectora discrepan, decide lo que declare `CUADERNO_<OBRA>.md` §2 (o el
    valor por defecto, `ORQUESTADOR.md` §1).
  - **Lectura externa** *(v1.2.2)*: cada tramo de unos siete capítulos, el autor puede
    pasarlo a lectoras de otros modelos con el encargo de `PROTOCOLO_LECTURA.md` §8. Lo que
    señalan tres lecturas o más (externas y propias) es un problema confirmado y se corrige
    en los capítulos escritos, no solo en los siguientes. Con cada una, una OPERACIÓN D
    corta del tramo (abajo) *(v2.0)*.
  - La ventana principal aplica las correcciones y anota en la biblia lo que sube a
    canon. Hasta entonces el capítulo no se da por cerrado.
- **OPERACIÓN D — Auditoría.** Se conserva la secuencia de la base y se añaden 19–21. Se
  hace entera al cerrar el libro y, **corta**, con cada lectura externa *(v2.0)*: el paso 3
  de la base y el 21, sobre el tramo, y el estado de pistas y migas (CLUE_LEDGER) al día en
  `continuidad.md` (`ORQUESTADOR.md` §2.5).
  19. **LA TRAMA B NO SE RESUELVE POR AZAR** *(v2.0)* (*Variante: dark romance policial:*
      el caso). ¿Su resolución sale de lo que ya estaba en página y de una decisión de la
      pareja, no de la casualidad ni del sistema (CLUE_LEDGER, TEST 4)?
  20. **PROMESA DE SAGA** (sustituye a la «garantía de HEA»), según la forma de la saga
      (SERIES_GLUE, adenda de dark romance). En las tres, ¿el libro contesta en página su
      pregunta de pareja (el arco de pareja del libro: `BRIEFING.md`, campo 2 bis)? *Misma
      pareja en muchos libros:* ¿la relación
      avanza en la escala de rendición sin cerrarse? ¿El libro llega a su final con su
      trama cerrada, la relación abierta y la miga entregada? Un cierre cálido y redondo es
      un fallo. *Dúo o trilogía:* ¿el libro que no es el último deja la relación en su
      punto más alto de daño o de deseo, y el último la cierra? *Parejas rotativas:* ¿la
      pareja del libro cierra su final feliz y el puente siembra la siguiente sin poner en
      duda a la que cierra?
  21. **PESO DE PAREJA REAL CONTRA EL DECLARADO** *(v2.0)*. Medido sobre lo escrito con la
      unidad de `PAREJA_PRIMERO.md` §2, por bloque de cuatro capítulos y por libro, contra el
      declarado (biblia B1 🔒, preset y escaleta) y el de las actas (C-10); si difieren,
      manda esta medida. Con él, los suelos de §3 de aquel archivo en lo escrito (presencia,
      cara a cara, calor —capítulos seguidos sin escena con carga—, voces, ganchos y el techo
      de lo que no es pareja, por defecto el 30 %), o los que declare el preset. Bloque por
      debajo del suelo: se reescaleta el siguiente. Libro por debajo: no se entrega
      (GENRE_CONVENTIONS, regla 1).

### 5. LA PAREJA ES LA TRAMA A *(v2.0)*

Sustituye a la doble hélice con reparto libre. La pareja es la **trama A** de cada libro y de
cada capítulo; la trama del libro, la **trama B** (`PAREJA_PRIMERO.md` §1). ROMANCE_BEAT_MAP
traza la columna y STORY_SPINE trenza la trama B sobre ella. El peso de la pareja tiene
número, suelo y unidad: por defecto, objetivo 80 % y suelo 70 %, por bloque de cuatro
capítulos y por libro, en palabras medidas con `PAREJA_PRIMERO.md` §2; lo que no es pareja
(trama B, trama horizontal y elenco cuando su página no es de pareja), como mucho el 30 %, sin
mínimo; la trama horizontal y el elenco no tienen cuota propia (GENRE_CONVENTIONS, regla 1).
La obra lo declara en la biblia (B1, 🔒) y en el preset (`PRESET_<OBRA>.md` ›
SYSTEM_ORCHESTRATION › Peso de la pareja): puede subirlo; bajarlo del suelo es decisión del
autor. De los ganchos, por defecto al menos dos de cada tres son de pareja (C-7); el emocional
es el más valioso.

**Por defecto, sin excepción:** ningún capítulo cierra en imagen estática de personaje. La obra
puede declarar cierres de descarga, con su tope (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION ›
Gancho y primer capítulo).

### 6. EL PRIMER CAPÍTULO DE CADA LIBRO

Además de abrir como manden las reglas duras que declare la obra, el capítulo 1 **contiene la
promesa de la pareja**: el otro protagonista visto, presente
o en tensión con el narrador. Un capítulo 1 que solo promete la trama del libro es una muestra
gratuita de thriller (GENRE_CONVENTIONS, TEST 1). Del libro 2 en adelante, además, cobra el gancho
con que cerró el libro anterior y arranca en su estado (SERIES_GLUE, adenda, TEST A3).

### 7. PRUEBAS A CIEGAS *(v1.2)*

Cuando un capítulo se escribe para compararlo con otra versión:
- la ventana que escribe trabaja en su rama y no mira otras ramas ni otras versiones del
  capítulo;
- el material de canon que nació de una versión descartada se marca en la biblia como «sin
  uso en página» y el NEXT dice qué decisiones del Anexo A se leen y cuáles no;
- la comparación la hacen al menos dos lectoras sin contexto, con los textos anonimizados y
  en orden invertido entre ellas, contra los capítulos anteriores como referencia de voz.

### 8. REGISTRO DE LA ADENDA

v2.0 · 22-10-2026: **«la pareja primero»** (`PAREJA_PRIMERO.md`, al frente del catálogo, §3).
La pareja es la trama A y sale la doble hélice con reparto libre (§5); fuera las adendas de
otro modelo (§1); el brief empieza por qué cambia entre ellos (§4); C-7 cuenta los ganchos de
pareja, C-8 suma el calor tardío y C-10 mide el peso de pareja con la unidad de
`PAREJA_PRIMERO.md` §2 y recoge en una línea las comprobaciones de pareja de las demás
plantillas; D-19 se degrada, entra D-21 y una OPERACIÓN D corta acompaña cada lectura externa.
En las plantillas de fase: el reparto 🔒 desde la ficha de premisa y la biblia (B1), la pregunta
de la pareja y «Entre ellos» al frente del diseño, la escaleta y el NEXT, suelos en los tests de
escaleta y lecturas que dicen cuánto es romance. Cambia el diseño, no la escritura: no añade
instrucciones antes de escribir.

v1.3 · 22-10-2026: §0 (orquestador y ventanas de trabajo, con `ORQUESTADOR.md` y las
plantillas de fase); **separación de obra y modelo**: la adenda y las plantillas de género ya
no llevan valores de ninguna obra, que pasan a su preset (`PRESET_<OBRA>.md`); la variante del
subgénero (GENRE_CONVENTIONS); las tres formas de saga (adendas de dark romance de SERIES_GLUE y
SERIES_ARCHITECTURE; §1 y D-20 condicionados a la forma); el libro siguiente (`ORQUESTADOR.md`
§2.7 y §2.8, diseño de cada libro en la biblia, tests y encargos de lectura de libro siguiente,
`PLANTILLA_LIBRO.md`). Solo añade comprobaciones y formas de declarar; no añade instrucciones
antes de escribir.

v1.2.2 · 21-10-2026: C-9 (espejos entre POV, tics y motivos que vuelven) y C-10 (peso de la
relación) en el cierre; lectura externa en C.5. Solo añade comprobaciones de cierre que cortan.

v1.2.1 · 21-10-2026: gancho en todos los cierres.

v1.2 · 21-10-2026: §7 (pruebas a ciegas); TIC 4 de la narradora irónica en
PROSE_LINE_DISCIPLINE; huecos sin narrar en el registro 13 de CONTINUITY_PHYSICS.

v1.1 · 21-10-2026: cierre obligatorio (OPERACIÓN C, con acta) y lectura editorial (C.5).
