<!-- MODELO_DarkRomance v2.0 — NARRATIVE_CHRONOLOGY: base agnóstica v7 (verbatim) + adenda de dark romance (v2.0) -->

# NARRATIVE_CHRONOLOGY.md

## PROPÓSITO

Este archivo separa dos órdenes temporales que la prosa confunde
con facilidad:

- FÁBULA: la sucesión de hechos tal como ocurren en el mundo narrativo,
  en orden cronológico absoluto.
- SJUZHET (trama): el orden en que esos hechos se presentan al lector.

Sin un registro de la fábula, la novela improvisa retrospectivamente
qué ocurrió antes del primer capítulo y qué ocurrió fuera de cámara.
Los agujeros que eso produce aparecen, tarde, en capítulos avanzados
que ya no se pueden reescribir sin coste.

JERARQUÍA: Capa 1.
Debe completarse (al menos en su eje pre-narrativo) antes de
STORY_SPINE.md y antes de CHAPTER_BRIEF.md del capítulo 1.

---

## DISTINCIÓN OPERATIVA

FÁBULA es el mundo. SJUZHET es la novela.
La novela es siempre un subconjunto + reordenación del mundo.

Este archivo registra la fábula. STORY_SPINE.md diseña el sjuzhet.
INFORMATION_CHOREOGRAPHY.md diseña cómo el lector accede a la
fábula a través del sjuzhet.

---

## CATEGORÍAS TEMPORALES

La fábula se divide en cuatro capas por su relación con el relato.

### 1. PRE-NARRATIVA
Eventos anteriores al inicio del relato.
Todo lo que define el estado de entrada de los personajes,
el mundo y las relaciones.
Incluye: infancia de protagonistas, eventos fundacionales del
mundo, heridas originales, deudas previas, sistemas heredados.

### 2. NARRATIVA VISIBLE
Eventos que el relato muestra en escena.
Subconjunto del mundo que el lector ve ocurrir.

### 3. NARRATIVA INVISIBLE (simultánea o interpolada)
Eventos que ocurren dentro del tiempo del relato pero fuera
de las escenas visibles.
Un personaje viaja, otro negocia, un tercero muere: el relato
no lo muestra pero el mundo lo registra.
Crítico en multi-POV y en novela con elipsis largas.

ALCANCE EXTENDIDO A EVENTOS DE MUNDO:
La capa de narrativa invisible no se restringe a eventos de
personaje. Cuando el proyecto tiene mundo evolutivo (sea con
WORLD_ARC.md activo o sin él), los eventos sistémicos que
ocurren simultáneos al tiempo del relato pero fuera de las
escenas visibles también se registran aquí. Una decisión
institucional tomada en el centro del poder mientras los POVs
están en la periferia, una transformación de mercado que se
produce sin que ningún personaje la presencie, una guerra
distante cuyas consecuencias llegarán capítulos después: todo
ello pertenece a la capa 3 aunque no involucre directamente a
ningún personaje POV.

La distinción entre eventos de personaje y eventos de mundo
en capa 3 se registra en el campo TIPO de la unidad de
registro (ver más abajo). La auditoría de capa 3 verifica
ambos tipos: un evento de mundo que altera condiciones del
relato y no está registrado produce los mismos agujeros que
un evento de personaje no registrado.

### 4. POST-NARRATIVA (proyectada)
Eventos posteriores al último capítulo cuya sombra se proyecta
hacia atrás sobre el relato.
No se narran, pero condicionan el cierre.
En novelas con epílogo de vuelta, esta capa es visible al final.
En series, esta capa es la semilla del siguiente libro.

---

## UNIDAD DE REGISTRO

Cada evento en la fábula se registra con los campos mínimos:

### EVENTO [ID]
- FECHA / MOMENTO: [dentro del calendario del mundo]
- DESCRIPCIÓN: [una frase factual, sin interpretación]
- TIPO: [personaje / mundo / mixto]
- PARTICIPANTES: [quién estuvo presente, quién actuó, quién fue
  afectado]
- TESTIGOS: [quién lo vio ocurrir; distinto de participantes]
- CONSECUENCIAS DIRECTAS: [qué cambió en el mundo por este evento]
- CAPA TEMPORAL: [1 pre / 2 visible / 3 invisible / 4 proyectada]
- EJE DE MUNDO ASOCIADO (si aplica): [eje declarado en
  WORLD_ARC.md cuando el evento es de tipo mundo o mixto]
- EN QUÉ CAPÍTULO(S) SE ALUDE (si aplica): [...]
- GRADO DE REVELACIÓN AL LECTOR: [completo / parcial / oblicuo /
  oculto — cruzar con INFORMATION_CHOREOGRAPHY.md]

---

## CALENDARIO MAESTRO

Lista ordenada cronológicamente de todos los eventos de las
cuatro capas. Es el mapa completo del tiempo del mundo.

FORMATO:
- [Fecha/momento]: EVENTO [ID] — [descripción corta] — [capa]

Este calendario crece a lo largo del proyecto.
Al inicio contiene sobre todo eventos de capa 1 (pre-narrativa).
Durante la escritura se llena con eventos de capas 2 y 3.
Al cierre puede incluirse capa 4 si el epílogo la necesita.

---

## MAPA DE SUPERPOSICIÓN CON EL RELATO

Tabla que cruza fábula y sjuzhet:

| Evento ID | Ocurre en | Se narra/alude en | Lector lo sabe desde | Distancia |
|-----------|-----------|-------------------|---------------------|-----------|
| E-01      | Año X     | Cap. 17           | Cap. 17             | 15 años   |
| E-02      | Año X+3   | No se narra       | Inferible cap. 22   | —         |
| E-03      | Año X+5   | Cap. 1            | Cap. 1              | 0         |

USO:
- Detectar cuándo un evento clave se revela demasiado tarde
  (el lector no pudo anclar nada anterior).
- Detectar cuándo el sjuzhet reordena tanto que la fábula se
  vuelve ilegible.
- Cruzar con INFORMATION_CHOREOGRAPHY.md para verificar que el
  ritmo de revelación es el previsto.

---

## PRE-NARRATIVA EXPANDIDA

Esta sección exige especial cuidado. Es donde más agujeros se
generan.

### HISTORIA DEL MUNDO
Eventos sistémicos anteriores a los personajes.
Fundación de instituciones, guerras, cambios tecnológicos,
decisiones políticas, desastres.

### HISTORIA DE CADA PERSONAJE
Línea de vida. Al menos los hitos que condicionan su ficha
de CHARACTER_PHYSICS.md (herida, mecanismo, formación).

### HISTORIA DE CADA RELACIÓN
Cómo se conocieron, qué pasó entre ellos antes del capítulo 1.
Cruzar con RELATIONSHIP_PHYSICS.md (nudo central).

### EL EVENTO DETONANTE PRE-NARRATIVO (si existe)
Si la novela empieza después de un evento que la desencadena,
ese evento es el pivote de toda la fábula pre-narrativa.
Registrar con máximo detalle: qué ocurrió, quiénes estaban,
quién miró para otro lado, qué quedó sin decir.

---

## ELIPSIS MAYOR Y CAPA INVISIBLE

Cuando un evento importante ocurre dentro del tiempo del relato
pero fuera de escena, registrarlo en capa 3 y vincularlo con
ELLIPSIS_PROTOCOL.md.

REGLA: un evento que altera vectores de relación o sabe-no-sabe
de personajes no puede quedar sin registrar, aunque no se
narre. Sin registro, el personaje "sabe" cosas por intuición
autoral y el lector nota la falta.

La regla se aplica también a eventos de mundo que alteran
condiciones del relato (oferta y demanda en mercados, equilibrio
político, presencia de instituciones, accesibilidad de
territorios). Un evento de mundo que opera sobre la posibilidad
de la trama y no está registrado produce el mismo síntoma: el
sistema "sabe" cosas que el lector no puede anclar en causa.

---

## EVENTOS DEL ARCO DE MUNDO EN LAS CAPAS TEMPORALES

Sección aplicable solo si WORLD_ARC.md está activo en el
proyecto.

Cuando el proyecto declara arco de mundo de serie, los
eventos del arco se distribuyen entre las cuatro capas
temporales del calendario maestro. La distribución no es
opcional: cada evento del arco de mundo declarado en
WORLD_ARC.md (manifestaciones por libro, movimientos
centrales, siembras) debe tener entrada correspondiente aquí.

### CAPA 1 (PRE-NARRATIVA) — EVENTOS DE MUNDO PRE-NARRATIVOS

Eventos sistémicos anteriores al inicio del relato que
explican el estado inicial del arco de mundo en libro 1.
Fundación de instituciones, decisiones políticas que
configuran el equilibrio inicial, traumas colectivos que
preceden a la saga, transformaciones tecnológicas
recientes. Estos eventos pueden no aparecer narrados nunca,
pero sostienen la coherencia del estado inicial declarado en
WORLD_ARC.

### CAPA 2 (NARRATIVA VISIBLE) — MANIFESTACIONES DEL ARCO

Cada manifestación de eje declarada en WORLD_ARC para el
libro N tiene su entrada en capa 2 cuando se narra en
escena. La manifestación entra a través del POV (siguiendo
jerarquía de intensidad escénica declarada en WORLD_ARC) y
queda registrada con eje de mundo asociado. La auditoría
verifica que cada manifestación declarada en WORLD_ARC
encuentre su evento aquí.

### CAPA 3 (NARRATIVA INVISIBLE SIMULTÁNEA) — EVENTOS DE MUNDO FUERA DE ESCENA

Eventos del arco de mundo que ocurren simultáneos al tiempo
del relato pero fuera de las escenas visibles. Una decisión
institucional tomada cuando ningún POV está presente, una
escisión política que se resuelve en otro continente, una
transformación de mercado que se produce sin testigo POV.
Estos eventos pueden manifestarse para los personajes en
forma de consecuencia (carta que llega, rumor que circula,
cambio de orden recibido) sin que el evento mismo se haya
narrado. La capa 3 los registra con su fecha real, sus
participantes (aunque sean instituciones o colectivos), y su
eje de mundo asociado.

La auditoría de capa 3 con tipo "mundo" es crítica: en sagas
con arco de mundo, los eventos sistémicos invisibles que no
se registran producen incoherencias entre libros (un eje
parece no haber evolucionado entre libro N y libro N+1
porque el evento intermedio no se contabilizó en ningún
sitio).

### CAPA 4 (POST-NARRATIVA PROYECTADA) — CIERRE PARCIAL O CONTINUACIÓN

Cuando el arco de mundo declara clausura o no-clausura final
en WORLD_ARC, la capa 4 puede registrar eventos proyectados
del arco que la saga no narra pero cuya sombra se proyecta
sobre el cierre. En sagas con no-clausura consciente
declarada, esta capa registra qué continúa más allá del
horizonte narrativo. En sagas con clausura, esta capa puede
estar vacía o registrar consecuencias inmediatas que el
epílogo final usa.

### COHERENCIA ENTRE NARRATIVE_CHRONOLOGY Y WORLD_ARC

La auditoría conjunta de ambos archivos verifica:

- Cada manifestación declarada en WORLD_ARC tiene evento en
  capa 2 o capa 3 de aquí, según se narre o no.
- Cada movimiento central declarado en WORLD_ARC tiene
  evento aquí con fecha precisa.
- Cada siembra declarada en WORLD_ARC tiene evento aquí (la
  siembra es típicamente un evento de capa 2 marginal, pero
  registrado con su función prospectiva).
- El estado inicial de cada libro declarado en WORLD_ARC
  coincide con el calendario maestro al final del libro
  anterior.

La incoherencia entre ambos archivos en este punto es error
estructural detectado en OPERACIÓN D.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — TRAZABILIDAD
¿Cada efecto narrativo visible tiene causa registrada en fábula?
Si un personaje reacciona a algo, ¿ese algo está en el calendario?

TEST 2 — CAUSALIDAD INVERSA
Recorriendo la fábula hacia atrás desde el último evento,
¿la cadena causal se sostiene sin saltos inexplicables?

TEST 3 — COHERENCIA CON CHARACTER_PHYSICS
¿La herida declarada en la ficha del personaje tiene su evento
correspondiente en la fábula? Si no, la herida flota.

TEST 4 — COHERENCIA CON RELATIONSHIP_PHYSICS
¿El nudo central de cada relación tiene evento(s) fundacional(es)
en la fábula?

TEST 5 — ELIPSIS DECLARADAS
Todo evento de capa 3 (invisible) que afecte vectores o
información debe estar en la fábula, aunque no se narre.

---

## CUÁNDO ACTUALIZAR

- OPERACIÓN 0: completar capa 1 exhaustivamente.
- OPERACIÓN 0.5: si el capítulo va a revelar o usar información
  de capa 1 o 3, verificar que esté registrada con precisión.
- OPERACIÓN C: registrar eventos de capa 2 que ocurrieron en el
  capítulo y eventos de capa 3 que implican (personajes que
  hicieron cosas fuera de cámara).
- OPERACIÓN D: auditar coherencia de la fábula completa.

---

## RELACIÓN CON OTROS ARCHIVOS

NARRATIVE_CHRONOLOGY.md recibe de:
- CHARACTER_PHYSICS.md (heridas, formación)
- RELATIONSHIP_PHYSICS.md (historia de cada relación)
- WORLD_TEXTURE.md (historia del mundo)
- WORLD_ARC.md (cuando está activo, recibe los eventos del
  arco de mundo: pre-narrativos, manifestaciones por libro,
  movimientos centrales, siembras, eventos invisibles
  simultáneos de mundo, eventos proyectados post-narrativos)

NARRATIVE_CHRONOLOGY.md alimenta:
- INFORMATION_CHOREOGRAPHY.md (qué se puede revelar y cuándo)
- STORY_SPINE.md (la trama elige qué mostrar de la fábula)
- CONTINUITY_PHYSICS.md (registro de lo que ya se narró)
- ELLIPSIS_PROTOCOL.md (lo que se decide no narrar)
- WORLD_ARC.md (cuando está activo, devuelve los eventos
  registrados con sus fechas precisas y consecuencias, para
  que la auditoría conjunta verifique coherencia entre arco
  declarado y fábula registrada)

NARRATIVE_CHRONOLOGY.md no se reescribe con frecuencia pero
crece. Los eventos de capa 2 y 3 se añaden durante la escritura.

---

## ERROR COMÚN

Tratar la fábula como algo que "ya se sabe" sin registrarla.
La memoria autoral falla: en cap. 20 no se recuerda exactamente
qué se había decidido sobre un evento pre-narrativo mencionado
de pasada en cap. 4. El registro previene la deriva.

Otro error: confundir fábula con backstory. Backstory es el
marketing de la fábula (lo que se dice al lector o al editor
para situar). Fábula es el sistema completo de causalidad que
sostiene la novela, se diga o no se diga.


---
---

