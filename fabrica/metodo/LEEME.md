# LÉEME — MODELO_DarkRomance v2.0

Este repo tiene dos cosas: **el modelo** (un método para escribir sagas de dark romance con
ventanas de IA) y **una obra** que se está escribiendo con él.

**Si llegas sin contexto:**

- **Te han lanzado con un código de ventana** (B1, E1, C05, DR-10…): eres una **ventana de
  trabajo**. Lee este archivo y `NEXT.md`, y ejecútalo tal cual; su lista de lecturas te dice
  todo lo demás. Si una parte del NEXT ya tiene sus archivos de salida, está hecha: salta a la
  siguiente.
- **Te han dicho que eres el orquestador:** lee `ORQUESTADOR.md` y el cuaderno de la obra activa
  (abajo).

---

## 1. La obra activa

- **Obra:** *Madera y Pólvora* (saga de dark romance policial). Libro 1 en escritura.
- **Cuaderno del orquestador:** `CUADERNO_MADERA_Y_POLVORA.md` (dónde estamos, decisiones del
  autor, índice de la obra).
- **Preset** (los valores de la obra que leen las plantillas): `PRESET_MADERA_Y_POLVORA.md`.
  Donde una plantilla diga `PRESET_<OBRA>.md`, es este archivo.
- **Biblia:** `madera_y_polvora_biblia.md` (versión en su cabecera).
- **Libro 1:** `libro_01/` (escaletas, capítulos, briefs, actas, lecturas, continuidad, plan de
  la lectora, historial de lecturas).
  **Escaleta vigente:** `libro_01/escaleta_v4.md` (A99), con su ampliada `escaletaAmpliada_v4.md`; `escaleta.md`
  y `escaletaAmpliada.md` son histórico, con la numeración vieja.
- **Encargo vivo:** `NEXT.md`.
- **Rama de trabajo:** `main` (desde el 28-10-2026; las ramas `modelo-v2` y `modelo-v1.3-final` son de archivo).
- **Histórico:** `Referencia_Dark Romance/` (borradores de agosto, biblias antiguas, el contrato
  de conversión de agosto y el LEEME anterior, con la historia del modelo con esta obra).

## 2. Qué es modelo y qué es obra

Para empezar **otra saga**, se copian a un repo nuevo **solo los archivos del modelo** y se
arranca un orquestador (`ORQUESTADOR.md`, §1a). Para **otro libro de esta saga**, se sigue en
este repo (`ORQUESTADOR.md`, §1b).

**Modelo** (se copia):

- *Dirección y servicio:* `PAREJA_PRIMERO.md` (el principio rector), `LEEME.md` (cambiando la
  §1), `ORQUESTADOR.md`, `SYSTEM_ORCHESTRATION.md`, `PROTOCOLO_LECTURA.md`, `PLANTILLA_NEXT.md`,
  `PLANTILLA_CUADERNO.md`, `PLANTILLA_BIBLIA.md`, `PLANTILLA_PRESET.md`,
  `PLANTILLA_ESCALETA.md`, `PLANTILLA_LIBRO.md`.
- *Plantillas de género (dark romance):* `GENRE_CONVENTIONS.md`, `HEAT_DISCIPLINE.md`,
  `ROMANCE_BEAT_MAP.md`, `CHARACTER_PHYSICS.md`, `DIALOGUE_MECHANICS.md`,
  `AESTHETIC_REGISTER.md`, `ELLIPSIS_PROTOCOL.md`, `CLUE_LEDGER.md`, `BRIEFING.md`,
  `SERIES_GLUE.md`.
- *Plantillas de base con adenda de dark romance:* `CHAPTER_BRIEF.md`, `CONTINUITY_PHYSICS.md`,
  `PROSE_LINE_DISCIPLINE.md`, `RELATIONSHIP_PHYSICS.md`, `SCALE_CALIBRATION.md`,
  `SEAMS_AND_HINGES.md`, `TENSION_MECHANICS.md`, `VOICE_ARCHITECTURE.md`, `SERIES_ARCHITECTURE.md`,
  `INFORMATION_CHOREOGRAPHY.md`, `NARRATIVE_CHRONOLOGY.md`,
  `PROSODY_AND_MUSIC.md`, `REVISION_PROTOCOL.md`, `SCENE_NECESSITY.md`, `SEMANTIC_OMISSION.md`,
  `SENSORY_HIERARCHY.md`, `STORY_SPINE.md`, `SUBPLOT_ARCHITECTURE.md`, `SUBTEXT_MECHANICS.md`,
  `THEMATIC_ENGINE.md`, `WORLD_ARC.md`, `WORLD_TEXTURE.md`, `RESEARCH_LEDGER.md`.
- *Plantillas de base* (oficio general): `SCENE_SHAPE.md`, `PROTOCOLO_CAPTURA_APRENDIZAJE.md`,
  `REGISTROS_APRENDIZAJE.md`.
- *Historia del modelo:* `Referencia_modelo/` (el modelo de Intriga del que salían las adendas que
  la v2.0 derogó; solo traza, nadie tiene que leerla).

**Obra** (no se copia): `<obra>_biblia.md`, `PRESET_<OBRA>.md`, `CUADERNO_<OBRA>.md`,
`NEXT.md`, `libro_NN/`, y cualquier carpeta de referencia de la obra.

**Regla:** ningún archivo del modelo lleva valores de una obra (nombres, paletas, contadores,
capítulos, decisiones de su biblia). Si una mejora nace de una obra, al modelo va la regla y a
la obra, su valor.

**Lo que cambia de una saga a otra y dónde se declara:** el **subgénero** (las reglas marcadas
«Variante: dark romance policial» solo valen para el policial; otro subgénero escribe su variante
en la biblia y en el preset: `GENRE_CONVENTIONS.md`, declaración primaria) y la **forma de la
saga** (la misma pareja en muchos libros, dúo o trilogía, o parejas rotativas: `SERIES_GLUE.md`,
adenda de dark romance). Todo lo demás de la obra vive en su biblia y en su preset.

## 3. El método en una línea

**La pareja primero** (`PAREJA_PRIMERO.md`: la pareja es la trama A de cada libro y de cada
capítulo, y su peso se mide después del borrador) → biblia → preset → escaleta (cada ficha empieza
por «Entre ellos») → escaleta ampliada → por cada capítulo: brief de una hoja →
escritura libre con las reglas de prosa como oído de fondo → **cierre obligatorio** (OPERACIÓN C,
con acta) → **lectura editorial y de lectora tipo** por quien no escribió (C.5) → correcciones
mínimas y canon a la biblia. Lo dirige un **orquestador** que no escribe la obra
(`ORQUESTADOR.md`). Las reglas viven **después** del borrador, nunca como prescripción previa.

## 4. Cómo se mejora el modelo

- **Regla del fork:** ninguna mejora añade instrucciones antes de escribir. Todo cambio va al
  cierre (OPERACIÓN C), a la lectura (C.5, `PROTOCOLO_LECTURA.md`) o a los tests de las
  plantillas de fase. Si una mejora necesita decirle a quien escribe cómo escribir, no entra.
- Las mejoras que solo cortan pueden ir directas a `main` y se vigilan en las lecturas
  siguientes; las demás, en una rama y con prueba a ciegas (`SYSTEM_ORCHESTRATION.md`, adenda
  §7).
- Cada versión se apunta en la adenda de `SYSTEM_ORCHESTRATION.md` (§8) y aquí.

## 5. Versiones

| Versión | Fecha | Qué trae |
|---|---|---|
| v1.0 | 08-08-2026 | Conversión del modelo de Intriga (base agnóstica v7) a dark romance, hecha para la primera obra |
| v1.1 | 21-10-2026 | Cierre obligatorio (OPERACIÓN C, con acta) y lectura editorial (C.5); reglas de género en las plantillas de cada capítulo |
| v1.2 | 21-10-2026 | Pruebas a ciegas; glosa frente a remate en la narradora irónica; huecos sin narrar |
| v1.2.1 | 21-10-2026 | Lectora tipo en cada capítulo (manda la lectora); gancho sin excepción |
| v1.2.2 | 21-10-2026 | C-9 (espejos entre POV, tics, motivos que vuelven) y C-10 (peso de la relación); lectura externa con otros modelos; correctora de continuidad tras cortes |
| v1.3 | 22-10-2026 | **Orquestador** (`ORQUESTADOR.md`) y plantillas de fase (biblia, preset, escaleta, cuaderno, archivos del libro); **separación de obra y modelo**: las plantillas son de género y los valores de cada obra viven en su preset; variante del subgénero y tres formas de saga; paso al libro siguiente y diseño de cada libro |
| **v2.0** | 22–23-10-2026 | **«La pareja primero»** (`PAREJA_PRIMERO.md`): la pareja es la trama A de cada libro y de cada capítulo; su peso se mide en palabras, con objetivo del 80 % y suelo del 70 % por bloque y por libro; suelos de presencia, contacto, calor, voces y ganchos; fuera las adendas de Intriga; la escena necesaria es la que cambia algo entre ellos; las lecturas miden cuánto es romance; sin instrucciones de prosa · **en `main` desde el 28-10-2026**, por decisión del autor y sin prueba a ciegas (la v1.3 queda en la rama `modelo-v1.3-final`) |
