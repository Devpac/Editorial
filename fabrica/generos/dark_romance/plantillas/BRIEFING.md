<!-- Fábrica v3.0 — plantilla de GÉNERO (vale para cualquier saga de dark romance). Los valores de la obra viven en su preset: PRESET_<OBRA>.md (la obra activa la dice el LEEME). Historia: convertida desde el modelo agnóstico v7 el 08-08-2026; separada de la obra el 22-10-2026; v2.0, «la pareja primero» (PAREJA_PRIMERO.md), el 22-10-2026. -->

# BRIEFING.md — Fábrica v3.0

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

> **v2.0 · la pareja primero.** Rige `PAREJA_PRIMERO.md`: la pareja es la trama A de cada libro. La
> compuerta dura del bloque de libro es su arco de pareja (campo 2 bis); la miga, compuerta blanda.

## PROPÓSITO

Archivo de servicio: no diseña, no ejecuta, no revisa. Registra el estado operativo y las decisiones acumuladas, y sirve a todas las capas con la memoria que ningún archivo de capa cubre.

Su función principal aquí: **es la hoja de arranque de cada libro**. En la saga con la misma pareja (formas A y B; la forma de la saga la declara la obra: SERIES_GLUE, adenda de dark romance), las novelas comparten pareja, elenco, escenario y trama horizontal, así que ya no pregunta quién protagoniza, dónde ocurre ni hacia dónde va la trama horizontal: **eso se hereda de la biblia y no se vuelve a decidir**; con parejas rotativas se hereda el mundo y la pareja de cada libro se declara en su bloque. Lo que pide, libro a libro, es la capa de instancia: número y arco, tema emocional de la relación, el arco de pareja del libro, la trama del libro que se deriva de él (*Variante: dark romance policial:* el caso), la miga de pan sobre la trama horizontal (si la saga la tiene), la posición en la escala de rendición, el estado del reloj que cerca a la pareja (si la saga lo tiene: una amenaza que se acerca y suma una pieza en cada libro), el antagonista del libro (*Variante: dark romance policial:* el villano de la semana) y el gancho de cierre.

Sin él, una saga larga padece dos fricciones: la clásica —cada ventana arranca reconstruyendo qué se hizo antes— y una peor, propia de la saga: las ventanas **redeciden canon**. Reinventan cómo huele él, mueven la edad de ella, adelantan a un libro anterior el peldaño que la escala de rendición reserva (lo que revela quien raciona su confesión; el contacto y el calor no se reservan: tienen suelo en cada libro, `PAREJA_PRIMERO.md` §4).

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Propósito en la obra.
> *Qué declara aquí la obra:* cuántos libros comparten su canon, cuál es el reloj que cerca a su pareja, si lo tiene, y qué canon suyo se redecide con más facilidad.

JERARQUÍA: Transversal. Sirve a todas las capas como archivo operativo. No manda sobre GENRE_CONVENTIONS ni sobre CHARACTER_PHYSICS: los cita.

---

## CONDICIONALIDAD DE APLICACIÓN

Aquí **no es opcional**. Una entrega completa (su extensión la declara la obra) no cabe en tres ventanas, y ninguna es autónoma: todas mueven lo que dejaron las anteriores y, en la saga con la misma pareja, relojes que vienen de libros anteriores. Opera en dos niveles.

**Briefing de saga (uno, permanente; formas A y B, la saga con la misma pareja; en este modelo no es un archivo aparte, `ORQUESTADOR.md` §9).** Estado de los relojes de la saga, posición alcanzada en la escala de rendición, inventario de migas entregadas y, si lo tiene, peso acumulado del reloj que cerca a la pareja. Se actualiza al cerrar cada libro y **nunca se archiva**.

**Bloque de libro (uno por volumen).** Se abre con la declaración de instancia (Sección 1) y se cierra al entregar la novela, volcando sus consecuencias horizontales al briefing de saga.

Única omisión legítima: material de acompañamiento breve. Si toca canon horizontal, se anota igual.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Condicionalidad en la obra.
> *Qué declara aquí la obra:* la extensión de cada entrega y, si los tiene, cuántos relojes lleva su briefing de saga y cuál es el reloj que cerca a su pareja.

---

## LO QUE YA NO SE PREGUNTA: CANON HEREDADO

Esta tabla cierra preguntas, no las abre. Ningún briefing de libro declara nada de aquí.

| Se hereda | Valor fijo | Fuente |
|---|---|---|
| Pareja (saga con la misma pareja) | [los dos protagonistas: nombre, edad y oficio] | [sección de la biblia] |
| Elenco | [el elenco fijo y los recurrentes de fuera de él] | [sección de la biblia] |
| Escenario | [los escenarios recurrentes, como la obra los organice, y, si lo tiene, el espacio propio] | [sección de la biblia] |
| Trama horizontal (si la saga la tiene) | [los misterios y los antagonistas que atraviesan la saga] | [secciones de la biblia] |
| Género y arbitraje | Dark Romance con [la ambientación del subgénero que declara la obra]. Ganan la relación, la tensión, la oscuridad | GENRE_CONVENTIONS |
| Persona y POV | [la persona, el tiempo y la alternancia de POV que fija la biblia] | [sección de la biblia] |
| Extensión y reparto | [palabras por libro · capítulos y su horquilla · peso de pareja: objetivo y suelo, como poco los de `PAREJA_PRIMERO.md` §2 (y los suelos de su §3)] | [secciones de la biblia] |
| Apertura | [cómo abre cada libro, según la biblia §14: con la pareja (los dos, o uno mira al otro)]. Nunca con la trama del libro (*Variante: dark romance policial:* nunca con un cadáver) | [sección de la biblia] |
| Cierre | Trama del libro cerrada y pregunta de pareja del libro contestada (campo 2 bis). En las formas A y B (salvo el último libro de la B), relación abierta: **prohibido registrar un final feliz cerrado por libro** | SERIES_GLUE |

**Regla dura:** si una ventana cree que está "decidiendo" algo de esta lista, no decide: rompe canon. Se detiene y consulta la biblia.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Canon heredado.
> *Qué declara aquí la obra:* el valor fijo de cada fila de la tabla y la sección de su biblia de la que sale.

---

## ESTRUCTURA DEL ARCHIVO

Cinco secciones permanentes desde la apertura del bloque de libro —**1** declaración de instancia, **2** estado del catálogo, **3** decisiones autorales acumuladas, **4** pendientes derivados, **5** próximo paso— y una **variable** con los tableros que la saga necesita. Se detallan más abajo.

---

## REGLAS DE ACTUALIZACIÓN

Un briefing desactualizado es peor que su ausencia: genera falsa confianza, y en una saga larga eso se paga en continuidad rota que las lectoras detectan y reseñan.

**A — Cierre de ventana significativa.** Toda ventana que cierre archivo, tome decisión autoral o resuelva pendiente actualiza el briefing antes de cerrar. Paso obligatorio.

**B — Actualización mínima viable.** Si la ventana cambió algo que la siguiente necesita saber, se actualiza. Afinar un archivo ya cerrado puede no requerir nada.

**C — Ediciones limpias, no acumulativas.** Se reemplaza lo obsoleto. Esto es estado actual, no traza histórica: la traza vive en los archivos cerrados y en los registros de aprendizaje.

**D — "Próximo paso" siempre vigente.** Si queda obsoleta, la ventana siguiente arranca desorientada.

**E — Concisión.** Si engorda, pierde su función.

**F — Los relojes se vuelcan siempre.** Ninguna ventana cierra un libro sin anotar qué pasó con la escala de rendición y, si la saga los tiene, con la miga de pan y el reloj que cerca a la pareja. No admite la excepción de la Regla B.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Reglas de actualización en la obra.
> *Qué declara aquí la obra:* cuántos volúmenes tiene la saga y, si lo tiene, cuál es el reloj que cerca a su pareja, que se vuelca al cerrar cada libro.

---

## ANATOMÍA DETALLADA DE LAS SECCIONES

### Sección 1 — Declaración de instancia del libro

**El orden es vinculante** *(v2.0: el de `PLANTILLA_BIBLIA.md` §19 y `ORQUESTADOR.md` §2.8)*. Primero la pareja: su pregunta en este libro y lo que cambia entre ellos (campo 2 bis, que por eso va delante del 2); después, el tema emocional (2) y la trama del libro (3), que se deriva de los dos (regla del espejo: GENRE_CONVENTIONS, regla 2). Si el bloque se rellena empezando por la trama, el libro ya está escrito como novela del género secundario aunque nadie lo note hasta la revisión (*Variante: dark romance policial:* el caso se deriva del tema; si el bloque se rellena empezando por el crimen, el libro ya está escrito como novela negra).

1. **Número de libro, título y arco.** Con la ventana del arco y su foco (los arcos que declara la obra). Con parejas rotativas, también la pareja del libro. Se anota si el volumen es puerta de salida limpia, si la saga las tiene.

   **2 bis. ARCO DE PAREJA DEL LIBRO** *(v2.0)*. Va primero, antes que el tema emocional y que la trama del libro, que se elige para provocarlo. Cinco piezas, concretas y con su % del libro cuando lo tienen: **la pregunta de pareja** (la versión que el libro agota y contesta en página, y lo que cambia entre ellos para contestarla, de dónde a dónde; en las formas A y B (salvo el último libro de la B), sin final feliz: THEMATIC_ENGINE y SERIES_GLUE, adendas); **la transgresión** (la línea que uno cruza por el otro, o contra él, y que ya no se deshace); **el momento oscuro** (lo que se rompe entre ellos: la crisis de la pareja de ROMANCE_BEAT_MAP); **el pago de calor** (qué pasa entre los cuerpos en este libro y dónde, dentro de los suelos de HEAT_DISCIPLINE); **el cara a cara** (el primero, como tarde al 10 %, y el tope de la ausencia, si la obra declara una: ELLIPSIS_PROTOCOL, uso B). **Compuerta dura: sin este campo relleno, el libro no se abre.**
2. **TEMA EMOCIONAL DE LA RELACIÓN.** Una línea, sin adornos, en presente. Se rellena después del arco de pareja (2 bis), antes que la trama, y no se toca después.
3. **La trama del libro, derivada del tema** (*Variante: dark romance policial:* el caso). La versión monstruosa del punto 2. Se declara junto a la frase que explica el espejo. Si el espejo no se puede enunciar en una frase, la trama está mal elegida. Y se declara como motor de la pareja: qué choque, qué proximidad forzada y qué obstáculo pone entre ellos para mover el arco del 2 bis (`PAREJA_PRIMERO.md` §5). Si no los junta ni los enfrenta, está mal elegida aunque el espejo funcione.
4. **La miga de pan sobre la trama horizontal** (si la saga la tiene). Qué descubre aquí quien la persigue (la obra lo declara), concreto y tangible, y de dónde sale la pista. **Compuerta blanda:** si falta, el libro se abre igual, la miga pasa a la Sección 4 como pendiente con plazo (antes de escaletar el bloque en que cae) y el libro no se entrega sin ella (GENRE_CONVENTIONS, regla 9).
5. **Posición en la escala de rendición.** Qué entrega quien raciona su confesión (la obra lo declara) que no hubiera entregado antes. Hitos fijos: los que declara la obra, cada uno con su libro (o con su tramo, si la escalera cabe en un libro). Si la escalera se reparte en varios libros, en los volúmenes intermedios el peldaño es menor, pero existe y se especifica. Es lo único de la pareja que se reserva para otro libro: el choque, el deseo, el contacto y el calor no bajan en los intermedios (campo 2 bis; `PAREJA_PRIMERO.md` §4).
6. **Estado del reloj que cerca a la pareja** (si la saga lo tiene). Desde el libro en que arranca: qué pieza suma en este libro y si lo sabe quien está cercado (lo declara la obra). La lectora lleva la cuenta; el briefing también.
7. **El antagonista del libro, como attrezzo** (*Variante: dark romance policial:* el villano de la semana, como attrezzo táctico). Qué presión pone sobre la pareja. Ningún antagonista asciende a interés romántico; si la protagonista se le acerca, el acercamiento es instrumental y sin roce (GENRE_CONVENTIONS, PELIGRO 1), y qué celos activa en el otro y por qué medio lo sabe, si la obra lo declara.
8. **Gancho de cierre.** En las formas A y B (salvo el último libro de la B), cliffhanger emocional: una pregunta de la relación que el libro deja viva (una pista grande de la trama horizontal puede ir con ella, no en su lugar); en otra forma, el cierre que declare la obra (SERIES_GLUE). Se declara en el arranque; no se improvisa en el último capítulo.

**Comprobación de los no negociables de la obra.** Antes de cerrar la sección se marca dónde caen los que la obra declara obligatorios en cada libro.

Cierra la metadata: fase (diseño, escritura, revisión), versión del modelo y fecha.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Declaración de instancia en la obra.
> *Qué declara aquí la obra:* sus arcos y, si las tiene, sus puertas de salida; un ejemplo canónico de tema y de trama derivada; quién descubre la miga y quién entrega en la escala de rendición, con sus hitos; qué activa en la pareja el antagonista del libro además de su presión, si la obra lo declara; su lista de no negociables por libro y, si los tiene, de dónde salen sus migas y cuál es el reloj que cerca a su pareja.

### Sección 2 — Estado del catálogo

Estados: **heredado** (llega cerrado desde el modelo; por defecto, en la saga con la misma pareja, casi todo el catálogo desde el libro 2), **virgen**, **abierto**, **cerrado** y **congelado** (cerrado pero reabrible por archivos vecinos).

En esa forma, exigen trabajo real por volumen muy pocos: STORY_SPINE, ROMANCE_BEAT_MAP, CLUE_LEDGER, CHAPTER_BRIEF y SUBPLOT_ARCHITECTURE. La fracción cerrado/total sigue dando la métrica de avance.

### Sección 3 — Decisiones autorales acumuladas

Solo las decisiones que el canon deja abiertas. Tres campos: contexto, contenido, ventana.

Si una decisión se reabre, la entrada se sustituye. **Si roza el canon —cronología, edades, quién sabe qué de la trama horizontal, el peldaño que la escala de rendición reserva— no se registra: se consulta la biblia y se obedece.**

### Sección 4 — Pendientes derivados

Acciones específicas, distintas de las decisiones (ya tomadas) y del catálogo (archivos enteros). Cada una con descripción, ventana donde se identificó, ventana de ejecución, dependencias y prioridad.

Se marca aparte **el pendiente horizontal**: el que no se resuelve aquí sino en un volumen posterior fijado por la biblia. Ejecutado un pendiente, se elimina; si generó otros, se registran nuevos.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Decisiones y pendientes en la obra.
> *Qué declara aquí la obra:* qué decisiones deja abiertas su canon, qué datos suyos rozan el canon y qué pendientes horizontales tiene, con su libro.

### Sección 5 — Próximo paso

Una frase: "La ventana siguiente debe [acción concreta], consultando [archivos relevantes], y produciendo [resultado esperado]." Se reescribe entera cada vez; nunca acumula histórico.

### Sección variable — Bloques específicos

- **Tablero de los relojes de la saga** (saga con la misma pareja: formas A y B). El bloque más útil de la saga: cada reloj que declara la obra (libro en que arranca → libro en que suena), con su estado tras el libro en curso.
- **Contador de paleta** (si la obra raciona la mezcla de dos paletas). Cuántas veces se han mezclado. **Máximo: el que declara la obra por libro.** Se lleva aquí porque es una cuota de volumen entero que ninguna ventana de capítulo puede vigilar sola. Autoridad: SENSORY_HIERARCHY.
- **Inventario de migas entregadas** (si la saga tiene trama horizontal). Todo lo que sabe ya de la trama horizontal quien la persigue. Evita repetir descubrimiento y evita el estancamiento.
- **Glosario operativo.** Los términos técnicos de la obra.
- **Registro de fricciones.** Lo que rozó en producción; lo procesa después PROTOCOLO_CAPTURA_APRENDIZAJE.

Añadir y quitar bloques es decisión autoral. Los dos primeros, si la saga los tiene, no se quitan nunca.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Bloques específicos de la obra.
> *Qué declara aquí la obra:* si los tiene, sus relojes con el libro en que arranca y suena cada uno, su techo de mezclas de paletas y de qué trata su inventario de migas; y los términos de su glosario.

---

## INTEGRACIÓN OPERATIVA

**OPERACIÓN 0 (FUNDACIÓN).** En el libro 1 el briefing se inicializa al final. Desde el libro 2, en la saga con la misma pareja (formas A y B), la operación se reduce drásticamente —el catálogo llega heredado— y su trabajo real es **rellenar la Sección 1 en su orden vinculante**: arco de pareja (su pregunta y lo que cambia entre ellos), tema, trama del libro, miga, rendición, reloj que cerca a la pareja, antagonista del libro, gancho (la miga y el reloj, si la saga los tiene).

**OPERACIÓN 0.5 (BRIEF DE CAPÍTULO).** Se consulta en el primer paso a través del NEXT (adenda de SYSTEM_ORCHESTRATION, §0). CHAPTER_BRIEF diseña el capítulo; el briefing dice en qué punto del arco de pareja y del tema emocional, de la escala de rendición y, si lo tiene, del reloj que cerca a la pareja arranca ese capítulo.

**OPERACIONES A, B, C.** Rara vez lo consultan. El contador de paleta, si la obra lo lleva, se comprueba en el cierre (C-3), no antes de escribir una escena. Decisiones y pendientes nuevos se vuelcan al cerrar la ventana.

**OPERACIÓN D (AUDITORÍA).** Lo requiere siempre: contrasta el peso de pareja real (registro 12 de CONTINUITY_PHYSICS; D-21 de la adenda de SYSTEM_ORCHESTRATION) contra su objetivo y su suelo, revisa que el arco de pareja y la miga (si la hay) sigan en pie y verifica que los no negociables de la obra tengan sitio en el mapa.

**Cierre de libro** (formas A y B). Volcado al briefing de saga: relojes, rendición, migas y, si lo tiene, peso del reloj que cerca a la pareja. **Arranque de ventana:** lo que el NEXT nombre de él (adenda de SYSTEM_ORCHESTRATION, §0).

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Integración operativa en la obra.
> *Qué declara aquí la obra:* qué peso de pareja declara, cuáles son sus no negociables y, si los tiene, cuál es el reloj que cerca a su pareja y, si las tiene, sus paletas.

---

## TESTS DE FUNCIONAMIENTO

- **TEST 1 — ORDEN.** ¿El arco de pareja (2 bis) y el tema emocional están escritos antes que la trama del libro, y el espejo cabe en una frase? Si el bloque empieza por la trama (*Variante: dark romance policial:* por el crimen), se ha invertido la regla del espejo (GENRE_CONVENTIONS, regla 2).
- **TEST 2 — MIGA** (si la saga tiene trama horizontal). ¿El campo 4 trae un descubrimiento concreto y tangible sobre la trama horizontal, o una promesa vaga? Vago equivale a vacío: queda como pendiente con plazo (compuerta blanda) y el libro no se entrega sin ella.
- **TEST 3 — RENDICIÓN.** ¿El campo 5 nombra algo que quien raciona su confesión no había entregado antes? Si no, la moneda real de la saga no circula en este volumen.
- **TEST 4 — EL RELOJ QUE CERCA A LA PAREJA** (si la saga lo tiene). Desde el libro en que arranca, ¿hay pieza nueva, y cuadra con el peso acumulado del briefing de saga?
- **TEST 5 — CANON REDECIDIDO.** ¿Alguna entrada de la Sección 3 decide algo que la tabla de canon heredado da por cerrado? Se borra y se consulta la biblia.
- **TEST 6 — ATTREZZO.** ¿El antagonista del libro se declara por la presión que ejerce sobre la pareja, o se le ha escrito química propia? Lo segundo rompe el contrato.
- **TEST 7 — LOS NO NEGOCIABLES.** Los que la obra declara por libro: ¿tienen sitio en el mapa, o son intenciones?
- **TEST 8 — CIERRE ABIERTO** (formas A y B, salvo el último libro de la B). ¿El campo 8 registra una pregunta de la relación (con la pista grande al lado, si la hay), y no una coda cálida que desactive la tensión de saga?
- **TEST 9 — PESO Y VIGENCIA.** ¿Se lee entero en pocos minutos y su "Próximo paso" describe lo que toca ahora?
- **TEST 10 — ARCO DE PAREJA** (compuerta dura). ¿El campo 2 bis trae sus cinco piezas, concretas y con su sitio, dentro de los suelos de `PAREJA_PRIMERO.md` §3? Si falta una o es vaga, el libro no se abre.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Tests en la obra.
> *Qué declara aquí la obra:* quién entrega en su escala de rendición, qué no negociables vigila el TEST 7 y, si los tiene, sobre qué trata su miga y desde qué libro corre el reloj que cerca a su pareja.

---

## RELACIÓN CON OTROS ARCHIVOS

**La biblia de la obra.** Autoridad superior y fuente de todo lo heredado. El briefing no la resume ni la interpreta: la cita y la obedece. Sus datos son vinculantes al dígito.

**`PAREJA_PRIMERO.md`.** Manda en el peso de la pareja y en los suelos que aplica el campo 2 bis.

**SYSTEM_ORCHESTRATION.md.** Capa 0: declara cuándo se consulta y cuándo se actualiza el briefing. **GENRE_CONVENTIONS.md** fija el contrato que la Sección 1 aplica —apertura con la pareja, peso de pareja con sus suelos, escena limpia prohibida, gancho en todos los capítulos por defecto—.

**CLUE_LEDGER.md.** Lleva al detalle las pistas de la trama del libro y las migas horizontales; el briefing guarda solo el titular: qué se descubrió y en qué libro.

**SERIES_GLUE.md y SERIES_ARCHITECTURE.md.** Gobiernan la continuidad de la saga y declaran su forma; en la saga con la misma pareja, el briefing de saga es su cuadro de mandos: relojes, escala de rendición y puertas de salida limpias que declara la obra.

**RESEARCH_LEDGER.md.** Investigación pendiente y resuelta. Función complementaria, sin solape.

**NEXT.md.** Transición efímera entre ventanas: se lee NEXT primero (tarea puntual) y el briefing después (estado durable).

**Todos los archivos del catálogo.** Ellos registran su contenido; el briefing, la metadata: cuáles están cerrados o heredados, qué decisiones gobiernan el volumen y qué pendientes los relacionan.

> **Valores de la obra →** `PRESET_<OBRA>.md` › BRIEFING › Relación con otros archivos en la obra.
> *Qué declara aquí la obra:* cómo se llama su biblia, qué peso de pareja declara, cuántos volúmenes tiene y qué puertas de salida, si las tiene, y qué investigación lleva.

Fin de la plantilla BRIEFING — Fábrica v3.0.
