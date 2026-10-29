# PLANTILLA_NEXT.md — cómo se escribe el NEXT de una ventana de trabajo

> Archivo de la fábrica. Lo usa el orquestador (`ORQUESTADOR.md`, §3) para
> encargar cualquier trabajo: un tramo de biblia, el preset, una escaleta, un capítulo, una
> reescritura o la pasada final. Una ventana sin contexto que recibe el repo con «continúa con lo
> que toque» tiene que encontrar sola la tarea (LEEME → NEXT) y poder hacerla sin preguntar. Todo
> NEXT se escribe con estas secciones, en este orden; la §8 dice qué cambia en cada fase.

## 1. Cabecera

- Ventana saliente y qué dejó hecho (con commits).
- Ventana entrante: código (fase + número: B1, P1, E1, A1, C01, R01, F1…; del libro 2 en
  adelante, con el número del libro delante: L2-D1, L2-E1, L2-C01…) y tarea en una línea.
- Rama de trabajo, cómo se conecta el repo y cuándo se hace commit y push.
- Quién hace la lectura editorial después (siempre otra ventana; `PROTOCOLO_LECTURA.md`).

## 2. Estado de cada parte

Si la ventana tiene varias partes, una tabla con **cómo saber si ya está hecha**:

| Parte | Hecha si existe… | Commit |
|---|---|---|
| 1 | `libro_01/[archivo de salida]` | `[mensaje]` |

Una ventana que llega a mitad de trabajo salta las partes hechas.

## 3. Lecturas, en dos tiempos

Lo de abajo es lo de un capítulo; en las demás fases, lo que se lee antes sale de la columna «Lee
antes» de la §8, y lo de después, de su «Verificación propia».


- **Antes de escribir** (obra y contrato): `LEEME.md`; la adenda Dark Romance de
  `SYSTEM_ORCHESTRATION.md`; los capítulos anteriores (siempre el último de cada narrador);
  `continuidad.md`; la ficha del capítulo en las dos escaletas; las secciones de la biblia que
  toca (con número); las plantillas de género que toca **y su sección del preset**
  (`PRESET_<OBRA>.md` › <PLANTILLA>), **como contrato de canon**. La ventana de trabajo no lee el
  cuaderno: el NEXT le nombra el preset, la biblia y las escaletas vigentes.
- **Después del borrador** (cierre): los filtros de CAPA 3 y los tests (adenda de
  VOICE_ARCHITECTURE, TIC 4 de PROSE_LINE_DISCIPLINE, registro 13 de CONTINUITY_PHYSICS,
  HEAT_DISCIPLINE, SEMANTIC_OMISSION, SUBTEXT_MECHANICS, SENSORY_HIERARCHY), el protocolo
  de cierre de DIALOGUE_MECHANICS y C-9 y C-10 de la adenda de SYSTEM_ORCHESTRATION (espejos
  entre POV si hay dos narradores, tics, peso de la pareja).
- Una línea siempre: «Las cifras y listas de las plantillas son comprobación de cierre, no
  objetivo; las reglas de prosa son oído de fondo» (desde la v2.0, las medidas de prosa son
  siempre alarma de cierre, nunca cuota: PROSE_LINE_DISCIPLINE, adenda).

## 4. Lo que el encargo tiene que cumplir

Lo de abajo es lo de un capítulo; en las demás fases, la columna «Tiene que cumplir» de la §8.


- **Entre ellos** *(v2.0)*, de la escaleta: qué cambia entre los dos en este capítulo (el paso
  que da la pregunta de la pareja del libro) y si están los dos en escena; después, **qué pone
  la trama B** (*Variante: dark romance policial:* el caso), si pone algo: qué los junta, los
  enfrenta o los separa. Qué, nunca cómo; el peso de pareja se mide después del borrador (C-10).
- **Tiempo y lugar**, con la hora de entrada y cómo se enlaza con el capítulo anterior (si
  hay espera o hueco, cuánto, y que no se dice en página si no hace falta).
- **Lo que no sabe cada protagonista y no puede intuir (empezando por el narrador del capítulo).**
- **Vetos de canon oculto** que el capítulo tienta especialmente: los dos o tres datos que la
  biblia guarda para un capítulo o un libro posterior y que esta escena pone al alcance de la
  mano (un nombre, una causa, una fecha).
- **Investigación**: si la escaleta lo bloquea, licencia que se declara (la siguiente del
  registro de investigación de la obra: RESEARCH_LEDGER) y qué se escribe sin detalle.
- **Plan de la lectora** que toca a ese capítulo (`libro_NN/plan_lectora.md` y notas «vN» de
  las escaletas).
- **Cierre** que pide la escaleta (gancho; por defecto, en todos los cierres, salvo los de
  descarga que declare la obra en `PRESET_<OBRA>.md` › SEAMS_AND_HINGES › Gancho en todos los
  cierres).
- **Comprobaciones extra** del cierre (fechas, contadores, datos horizontales; y los de pareja:
  capítulos seguidos sin cara a cara, peso acumulado del bloque).

## 5. Prohibido

Otras ramas, otros repos, conversaciones pasadas; la lectura editorial; el capítulo
siguiente; tocar plantillas, biblia o escaleta.

## 6. Criterio

El criterio de delegación de la obra, copiado tal cual de `CUADERNO_<OBRA>.md` §2 (o el de por
defecto, `ORQUESTADOR.md` §1). Ante una sección 🔒: no se para, elige lo que no altere canon y lo
anota en el acta.

## 7. Verificación al cierre

Archivos que deben existir, extensión, POV y persona, cierre, commits pusheados, sección 5
respetada.

## 8. Variantes por fase *(v1.3)*

Las secciones 1–7 tienen la misma forma en todas las fases; la §3 y la §4 de arriba están escritas
para un capítulo, y en las demás fases se rellenan con esta tabla:

| Fase | Lee antes | Tiene que cumplir | Entrega | Verificación propia |
|---|---|---|---|---|
| **B1–B3 · Biblia** | Ficha de premisa (`FICHA_PREMISA.md`, con sus supuestos F0-NN si el autor no la ha confirmado); `PAREJA_PRIMERO.md`; la biblia hasta donde esté; `PLANTILLA_BIBLIA.md` (su parte); `GENRE_CONVENTIONS.md`; en B2, `SERIES_GLUE.md` y `SERIES_ARCHITECTURE.md` (adendas de dark romance) | Las secciones de su parte, concretas; canon oculto con su libro de revelación; Anexo A al día; en B1, el peso de la pareja 🔒 (§14: número, suelo y unidad) | `<obra>_biblia.md` + informe (decisiones por delegación, preguntas 🔒 con opción recomendada, dudas) | Que cada decisión tiene su fila en el Anexo A y cada pregunta 🔒 su opción recomendada (los tests de la biblia los aplica la auditoría) |
| **P1 · Preset** | La biblia entera; `PAREJA_PRIMERO.md`; `PLANTILLA_PRESET.md`; las plantillas de género que apunta | Cada ranura con su valor **de la biblia**; lo que la biblia no responde, como pregunta | `PRESET_<OBRA>.md` + lista de preguntas | Ninguna ranura vacía sin su pregunta |
| **D1 · Diseño del libro** (libro 2 y siguientes) | Biblia (la tabla de títulos y el diseño del libro anterior); preset; el estado de cierre del libro anterior (`libro_<N-1>/continuidad.md`) y su plan de la lectora («Para el libro N»); los últimos capítulos del libro anterior; `PAREJA_PRIMERO.md`; `PLANTILLA_BIBLIA.md` §19; `BRIEFING.md` (declaración de instancia) | Los campos del diseño de cada libro, empezando por la pregunta de la pareja y qué cambia entre ellos, dentro de la tabla de títulos | `libro_NN/diseño_libro.md` + informe (decisiones, preguntas para el autor con opción recomendada) | Que el libro arranca donde lo dejó el anterior y dice qué hace que el anterior no podía |
| **E1 · Escaleta** | Biblia (la tabla de títulos y el diseño del libro: §19) y lo que cite; preset; `PAREJA_PRIMERO.md`; `PLANTILLA_ESCALETA.md` parte 1; del libro 2 en adelante, el estado de cierre del libro anterior | La escaleta completa del libro, cada ficha con su «Entre ellos», si están los dos y su peso estimado | `libro_NN/escaleta.md` + informe | Calendario, reparto de narradores, peso de pareja por bloque, capítulos seguidos sin cara a cara y contadores |
| **A1… · Ampliada** | Escaleta; biblia; preset; `PAREJA_PRIMERO.md`; el tramo anterior; `PLANTILLA_ESCALETA.md` parte 2 | Las fichas de su tramo (unos doce capítulos) | `libro_NN/escaletaAmpliada.md` (su tramo) | Que cada ficha cumpla su línea de la escaleta y lleve su «Entre ellos», si están los dos y su peso estimado |
| **C01… · Capítulo** | Lo de las §3–§4 de arriba | Lo de la §4 | Brief, capítulo, acta, `continuidad.md` | OPERACIÓN C completa (C-1 a C-10) |
| **R01… · Reescritura** | Lo del capítulo + su lectura editorial | Lo que pidieron las lecturas, sin perder lo que funcionaba (lista de «se queda») | El capítulo nuevo + acta | OPERACIÓN C |
| **F1 · Pasada final** | El libro entero; la lista de pendientes de prosa de `continuidad.md`; `REVISION_PROTOCOL.md` (pasadas 2 a 5; la 1 fue con la OPERACIÓN D) | Esos pendientes, lo que pidan las pasadas 2 a 5 y la numeración publicada | Capítulos retocados + informe | Que no cambia nada fuera de la lista y de las pasadas |

En todas: **no se prescribe prosa** (la regla del fork vale también para la biblia y las
escaletas: se dice qué decidir, no cómo escribir) y lo que la ventana no puede decidir va al
informe como pregunta para el orquestador. El informe de una ventana de fase se escribe en
`informes/<CÓDIGO>.md` (el de un capítulo es su acta).
