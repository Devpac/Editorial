# Historia de la fábrica

Las reglas no llevan historia: lo que pasó y por qué está aquí. El detalle de cada frase de historia que salió de las reglas en la v3.0, archivo por archivo, está en `cirugia/historia/`.

## v3.0 · 28-10-2026 · Editorial

**La fábrica se separa de su primera obra.** Mismo método, mismas plantillas de oficio, mismas comprobaciones: ninguna regla de prosa nueva (regla del fork). Lo que cambia es dónde vive cada cosa.

- **Repo propio, en capas:** `metodo/`, `oficio/`, `romance/` y `generos/<género>/` (plantillas y adendas), que `herramientas/montar.py` compone en los archivos planos que leen las ventanas. El punto de partida (paso 1) es idéntico byte a byte a la v2.0 con la que se escribe *Madera y Pólvora* (`historia/ORIGEN.md`).
- **Sin valores de ninguna obra** (auditoría de 28-10-2026, `auditorias/2026-10-28_separacion/`; cirugía en `cirugia/`):
  - La trama de la primera obra que vivía disfrazada de regla del subgénero (vigilancia con cámaras, impunidad y negación plausible, seducción táctica de una perfiladora, investigador de asuntos internos, B como sospechoso fijo, la forense, la firma del antagonista de saga, los relojes, los tres planos del defecto, R1–R5, el idiolecto del hermético, la evolución de la pregunta del libro 1, la lectora externa) sale al preset de la obra. En la fábrica queda la convención, condicional y con su ranura.
  - **Roles:** la pareja es protagonista A y protagonista B; «ella/él» son el valor por defecto (`PAREJA_PRIMERO.md` §7). Caben parejas de cualquier género y la asimetría invertida.
  - **Forma:** un solo narrador, sagas sin trama B propia o con trama B que cruza libros, sin vigilancia, sin trama horizontal: todo tiene salida declarada.
  - **Mercado y lengua:** ranura común del preset (`Cabecera › Mercado y lengua`), con los valores de siempre como valor por defecto (español de España; Amazon KDP con Kindle Unlimited; lectora de dark romance de 20 a 40, KU, BookTok, Bookstagram; 3,99 €).
  - **Criterio de delegación** («1.º el disfrute de la lectora, 2.º la coherencia de la saga, 3.º la calidad literaria»; manda la lectora): valor por defecto del método; cada obra lo declara en su cuaderno §2.
- **Se quedan como identidad de la fábrica (decisión del autor):** la pareja primero (objetivo 80 %, suelo 70 %, el caso con techo del 30 %, los suelos de `PAREJA_PRIMERO.md` §3), los ganchos de pareja (dos de cada tres) y el gancho en todos los cierres, ahora con la salida de declarar cierres de descarga con su tope.
- **Fuera los restos de modelos anteriores que seguían mandando:** el NEXT de seis secciones y el BRIEFING como archivo (derogados en la adenda de SYSTEM_ORCHESTRATION, §0); la cola de la cirugía v7.1 de PROSE_LINE_DISCIPLINE; `PROTOCOLO_CAPTURA_APRENDIZAJE.md`, reescrito para este método (la mejora que nace de una obra se registra en la obra y se propone a la fábrica: a la fábrica va la regla, a la obra su valor); las menciones a la adenda de Intriga.
- **`PLANTILLA_PRESET.md`** regenera sus ranuras por plantilla desde los bloques «Valores de la obra →» (`herramientas/sincronizar_preset.py`): ya no pueden desalinearse. Ranuras nuevas: Cabecera › Correspondencia de roles y › Mercado y lengua; SYSTEM_ORCHESTRATION › Peso de la pareja (antes «Doble hélice»); PROTOCOLO_LECTURA › Listón de comparaciones; THEMATIC_ENGINE › Evolución de la pregunta; SUBPLOT_ARCHITECTURE › Trama B; WORLD_TEXTURE › Léxico y glosario; CHARACTER_PHYSICS › Regla de oro del perseguidor legítimo (antes «de Asuntos Internos»); SEAMS_AND_HINGES › Gancho en todos los cierres (antes «Gancho sin excepción»); PROSE_LINE_DISCIPLINE › Las voces (antes «Las dos voces»).
- **Auditada después de operar** (seis lectoras sin contexto, `auditorias/2026-10-28_v3/`): sin fugas graves de la obra, sin pérdidas para ella salvo tres que se añadieron a la migración, y una docena de reglas del género que la cirugía había ablandado sin ser de la obra, que recuperan su fuerza (`cirugia/CORRECCIONES_v3.md`): la trama B se cierra en el libro; una escena de cada cuatro, como mucho, solo de la trama B; el veto a redimir al peligroso, en cualquier forma de saga; el filo del tropo de la vigilancia; el refuerzo intermitente; el juego limpio para todo narrador; el subtexto por escena de crisis; el fuera de plano de B (solo la negación plausible es condicional); el acercamiento instrumental y sin roce; la arquitectura legal de la variante policial. Y una sola ranura por decisión (cierres de descarga, reparto de voces, hermético e irónico, listón de comparaciones).
- **Para *Madera y Pólvora*:** termina el libro 1 con la v2.0 de `Devpac/Dark` y migra al abrir el libro 2. Lo que su preset tiene que recibir para leer exactamente lo mismo está en `cirugia/MIGRACION_MyP.md`.

## v2.0 · 22–23-10-2026 · `Devpac/Dark`

«La pareja primero»: `PAREJA_PRIMERO.md` al frente; fuera las adendas de Intriga de todo el catálogo; la columna de cada libro, de la pareja; suelos de presencia, cara a cara, contacto, calor, voces y ganchos; la escena necesaria es la que cambia algo entre ellos; el caso, con techo; el peso de la pareja se mide en la escaleta, en el cierre (registro 12) y en las lecturas. Origen: el libro 1 de la primera obra, diseñado con la v1.3, se leía como novela negra con romance (39 % de pareja; los protagonistas coincidían en 9 de 47 capítulos), y nueve lecturas sin contexto hallaron la causa en el modelo, no en la prosa. Paso a `main` el 28-10-2026, por decisión del autor y sin prueba a ciegas («va mejor de calle»).

## v1.3 · 22-10-2026

El orquestador (`ORQUESTADOR.md`) y las plantillas de fase (biblia, preset, escaleta, cuaderno, archivos del libro); primera separación de obra y modelo dentro del mismo repo (los valores de la obra, a su preset); variante del subgénero y tres formas de saga; paso al libro siguiente y diseño de cada libro. Tres pruebas a ciegas: seguir la primera obra (8/10), saga nueva de otro subgénero (7/10), paso al libro 2 (6/10).

## v1.2 – v1.2.2 · 21-10-2026

Pruebas a ciegas; glosa frente a remate en la narradora irónica; huecos sin narrar; lectora tipo en cada capítulo («manda la lectora»); gancho sin excepción (del plan de la lectora de la primera obra); C-9 (espejos entre POV, tics, motivos que vuelven) y C-10 (peso de la relación); lecturas externas con otros modelos; correctora de continuidad tras cortes. Origen: las fricciones del acta del primer capítulo escrito con el modelo y tres lecturas externas de los siete primeros capítulos de la primera obra.

## v1.1 · 21-10-2026

Cierre obligatorio (OPERACIÓN C, con acta) y lectura editorial (C.5); reglas de género en las plantillas de cada capítulo. Origen: los errores de los dos primeros borradores de la primera obra (08-08-2026), que el modelo cometió por saltarse el cierre y que solo cazó una lectura editorial externa.

## v1.0 · 08-08-2026

Conversión a dark romance del modelo agnóstico v7 (base de oficio) y de su especialización de Intriga (adendas AGATHA_ROSA, derogadas en la v2.0). Traza en `historia/Referencia_modelo/`.
