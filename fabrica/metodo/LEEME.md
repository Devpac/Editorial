# LÉEME — la Fábrica

La **fábrica** es un método para escribir sagas de romance con ventanas de IA: un **orquestador**
que no escribe la obra la diseña, la encarga a **ventanas de trabajo** con el contexto limpio, la
hace leer por **lectoras** que no la han escrito y la corrige con cortes. Lo que llevas en esta
carpeta es la fábrica **montada** para un género (versión y género en `_FABRICA.txt`). Se monta
desde `Devpac/Editorial`; no se edita en la saga.

**Si llegas sin contexto:**

- **Te han lanzado con un código de ventana** (B1, E1, C01, C05…): eres una **ventana de
  trabajo**. Lee este archivo y `NEXT.md`, y ejecútalo tal cual; su lista de lecturas te dice
  todo lo demás. A la ventana de trabajo, el NEXT le nombra el preset, la biblia y las escaletas
  vigentes. Si una parte del NEXT ya tiene sus archivos de salida, está hecha: salta a la
  siguiente.
- **Te han dicho que eres el orquestador:** lee `ORQUESTADOR.md` y el cuaderno de la obra (§1).

---

## 1. Dónde está cada cosa

En el repo de una saga hay dos cosas, separadas:

- **La fábrica**, en `fabrica/`: este archivo y todos los que el método nombra en mayúsculas
  (`ORQUESTADOR.md`, `PAREJA_PRIMERO.md`, `PLANTILLA_*.md`, `GENRE_CONVENTIONS.md`…). Cuando una
  plantilla cita uno de ellos, está aquí.
- **La obra**, en la raíz del repo: `FICHA_PREMISA.md` (la de la fase 0), `CUADERNO_<OBRA>.md` (dónde estamos, rama de trabajo,
  decisiones del autor, versión de la fábrica e índice de los archivos de la obra), la biblia,
  `PRESET_<OBRA>.md` (los valores de la obra que leen las plantillas: donde una plantilla diga
  `PRESET_<OBRA>.md`, es el de la raíz), `NEXT.md` (el encargo vivo), `libro_NN/`, `informes/` y
  `publicacion/` (la configuración del maquetador de Editorial).

## 2. Qué es fábrica y qué es obra

**Fábrica** (en `fabrica/`, la monta `montar.py` de Editorial):

- *Dirección y servicio:* `PAREJA_PRIMERO.md` (el principio rector), `LEEME.md`, `ORQUESTADOR.md`,
  `SYSTEM_ORCHESTRATION.md`, `PROTOCOLO_LECTURA.md`, `PLANTILLA_NEXT.md`,
  `PLANTILLA_CUADERNO.md`, `PLANTILLA_BIBLIA.md`, `PLANTILLA_PRESET.md`,
  `PLANTILLA_ESCALETA.md`, `PLANTILLA_LIBRO.md`, `PROTOCOLO_CAPTURA_APRENDIZAJE.md`,
  `REGISTROS_APRENDIZAJE.md`.
- *Plantillas de género* (en el paquete de dark romance): `GENRE_CONVENTIONS.md`,
  `HEAT_DISCIPLINE.md`, `ROMANCE_BEAT_MAP.md`, `CHARACTER_PHYSICS.md`, `DIALOGUE_MECHANICS.md`,
  `AESTHETIC_REGISTER.md`, `ELLIPSIS_PROTOCOL.md`, `CLUE_LEDGER.md`, `BRIEFING.md`, `SERIES_GLUE.md`.
- *Plantillas de oficio, con la adenda de su género al final:* `CHAPTER_BRIEF.md`,
  `CONTINUITY_PHYSICS.md`, `PROSE_LINE_DISCIPLINE.md`, `RELATIONSHIP_PHYSICS.md`,
  `SCALE_CALIBRATION.md`, `SEAMS_AND_HINGES.md`, `TENSION_MECHANICS.md`, `VOICE_ARCHITECTURE.md`,
  `SERIES_ARCHITECTURE.md`, `INFORMATION_CHOREOGRAPHY.md`, `NARRATIVE_CHRONOLOGY.md`,
  `PROSODY_AND_MUSIC.md`, `REVISION_PROTOCOL.md`, `SCENE_NECESSITY.md`, `SEMANTIC_OMISSION.md`,
  `SENSORY_HIERARCHY.md`, `STORY_SPINE.md`, `SUBPLOT_ARCHITECTURE.md`, `SUBTEXT_MECHANICS.md`,
  `THEMATIC_ENGINE.md`, `WORLD_ARC.md`, `WORLD_TEXTURE.md`, `RESEARCH_LEDGER.md`; y, sin adenda,
  `SCENE_SHAPE.md`.

**Obra** (en la raíz): `FICHA_PREMISA.md`, `<obra>_biblia.md`, `PRESET_<OBRA>.md`, `CUADERNO_<OBRA>.md`, `NEXT.md`,
`libro_NN/`, `informes/`, `publicacion/` y cualquier carpeta de referencia de la obra.

**Regla:** ningún archivo de la fábrica lleva valores de una obra (nombres, paletas, contadores,
capítulos, decisiones de su biblia, su mercado). Si una mejora nace de una obra, a la fábrica va la
regla y a la obra, su valor.

**Lo que cambia de una saga a otra y dónde se declara:** el **género** (el paquete que se monta),
el **subgénero** (las reglas marcadas «Variante: dark romance policial» solo valen para el
policial; otro subgénero escribe su variante en la biblia y en el preset: `GENRE_CONVENTIONS.md`,
declaración primaria), la **pareja** (`PAREJA_PRIMERO.md`, «Roles»), el **mercado y la lengua**
(`PRESET_<OBRA>.md` › Cabecera › Mercado y lengua), el **criterio de delegación** (el cuaderno,
§2) y la **forma de la saga** (la misma pareja en muchos libros, dúo o trilogía, o parejas
rotativas: `SERIES_GLUE.md`). Todo lo demás de la obra vive en su biblia y en su preset.

## 3. El método en una línea

**La pareja primero** (`PAREJA_PRIMERO.md`: la pareja es la trama A de cada libro y de cada
capítulo, y su peso se mide después del borrador) → biblia → preset → escaleta (cada ficha empieza
por «Entre ellos») → escaleta ampliada → por cada capítulo: brief de una hoja →
escritura libre con las reglas de prosa como oído de fondo → **cierre obligatorio** (OPERACIÓN C,
con acta) → **lectura editorial y de lectora tipo** por quien no escribió (C.5) → correcciones
mínimas y canon a la biblia. Lo dirige un **orquestador** que no escribe la obra
(`ORQUESTADOR.md`). Las reglas viven **después** del borrador, nunca como prescripción previa.

## 4. Cómo se mejora la fábrica

- **Regla del fork:** ninguna mejora añade instrucciones antes de escribir. Todo cambio va al
  cierre (OPERACIÓN C), a la lectura (C.5, `PROTOCOLO_LECTURA.md`) o a los tests de las
  plantillas de fase. Si una mejora necesita decirle a quien escribe cómo escribir, no entra.
- **No se edita en la saga.** La mejora se registra en la obra y se propone a Editorial
  (`PROTOCOLO_CAPTURA_APRENDIZAJE.md`); allí se escribe en abstracto, se prueba y se versiona.
  Las que solo cortan pueden ir directas y se vigilan en las lecturas siguientes; las demás, con
  prueba a ciegas (`SYSTEM_ORCHESTRATION.md`, adenda §7).
- **La saga se pone al día cuando el autor lo decide**, de preferencia entre libros
  (`ORQUESTADOR.md` §2.7 y §10): se vuelve a montar `fabrica/` y se apunta en el cuaderno.

## 5. Versiones

| Versión | Fecha | Qué trae |
|---|---|---|
| v1.0 | 08-08-2026 | Conversión a dark romance desde un modelo de intriga |
| v1.1–v1.2.2 | 21-10-2026 | Cierre obligatorio (OPERACIÓN C, con acta) y lectura editorial (C.5); lectora tipo en cada capítulo; pruebas a ciegas; C-9 y C-10 |
| v1.3 | 22-10-2026 | Orquestador y plantillas de fase; los valores de cada obra, en su preset; variante del subgénero y tres formas de saga |
| v2.0 | 22–23-10-2026 | **«La pareja primero»** (`PAREJA_PRIMERO.md`): objetivo del 80 % y suelo del 70 % de pareja; suelos de presencia, contacto, calor, voces y ganchos |
| v3.0 | 28-10-2026 | **La fábrica se separa de su primera obra**: repo propio (Editorial), por capas y paquetes de género; sin valores de ninguna obra; pareja en roles A/B; mercado, lengua y criterio, de cada obra; se monta en `fabrica/` de cada saga |
| **v3.1** | 29-10-2026 | Arranque de saga con un comando; **mayores de edad, regla dura** (`PAREJA_PRIMERO.md` §8); un solo narrador y parejas de cualquier género, sin fricción; la fase 0 sin el autor |

La historia completa, con el porqué de cada cambio, está en el `CHANGELOG.md` de Editorial.
