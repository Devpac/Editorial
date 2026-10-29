<!-- Fábrica — SYSTEM_ORCHESTRATION: base de oficio + ADENDA DE GÉNERO (dark romance; los valores de la obra viven en PRESET_<OBRA>.md) al final. Decisión: ESPECIALIZA. Ver LEEME.md -->

# SYSTEM_ORCHESTRATION.md

## PROPÓSITO

Este archivo es el orquestador. Define el orden de operaciones,
la regla de precedencia entre archivos en conflicto, el bucle de
retroalimentación entre capas, y los puntos de auditoría
sistemática.

Sin orquestador, los archivos se ejecutan como voces simultáneas
y el sistema pierde coherencia. El orquestador es quien decide,
en cada momento, qué archivo habla y cuándo.

Este orquestador opera dentro del marco filosófico declarado en
MODELO_AGNOSTICO_v7_APERTURA.md. En particular, la SECCIÓN 11
del documento de apertura (SESGOS DECLARADOS DEL SISTEMA)
declara explícitamente tres sesgos del catálogo (sesgo
psicológico-literario, asunción de narración contemporánea por
defecto, sesgo de tradición literaria hispana y anglosajona).
La aplicación del orquestador en proyectos que se aparten de
estos sesgos puede requerir adaptación local de las operaciones
y decisiones declaradas aquí; tal adaptación es legítima cuando
está conscientemente formulada.

JERARQUÍA: Ninguna. Es la capa 0: gobierna las demás capas.

---

## ARQUITECTURA DE CAPAS

### CAPA 0 — GOBIERNO
- SYSTEM_ORCHESTRATION.md

### CAPA 0.5 — SERIE (si el proyecto es multivolumen)
- SERIES_ARCHITECTURE.md
- WORLD_ARC.md (condicional adicional)

Si el proyecto es un libro único, esta capa se omite.

Si es serie, los dos archivos coexisten o no según naturaleza
del proyecto. SERIES_ARCHITECTURE rige arcos de personaje
multivolumen, deudas y promesas de personaje, puntos de
convergencia. WORLD_ARC rige arco de mundo de serie con sus
ejes, deudas y promesas de mundo, trayectoria multilibro.

SERIES_ARCHITECTURE se aplica siempre que el proyecto sea
multivolumen. WORLD_ARC se aplica adicionalmente solo si se
cumplen tres criterios simultáneos: el mundo evoluciona
sustantivamente entre primer libro y último, la evolución
carga peso temático específico, y el proyecto declara
conscientemente esta orientación. Saga con mundo estable usa
solo SERIES_ARCHITECTURE; saga con mundo evolutivo usa ambos.

Si es serie, todos los archivos de Capa 1 de cada libro se
subordinan a los archivos activos de Capa 0.5 en lo que
concierne a arcos multivolumen y, si aplica, arco de mundo.

### CAPA 1 — DISEÑO (preguntas fundacionales)
- AESTHETIC_REGISTER.md
- GENRE_CONVENTIONS.md (paralelo a AESTHETIC_REGISTER:
  régimen estético declara cómo se escribe; convenciones de
  género declaran qué expectativas de lector el proyecto
  acepta, modula o desafía)
- THEMATIC_ENGINE.md
- CHARACTER_PHYSICS.md
- RELATIONSHIP_PHYSICS.md
- WORLD_TEXTURE.md
- VOICE_ARCHITECTURE.md
- NARRATIVE_CHRONOLOGY.md
- STORY_SPINE.md
- SUBPLOT_ARCHITECTURE.md (derivado de STORY_SPINE: declara
  el conjunto de subtramas con su forma, función, intersección
  con la línea principal y protocolo de salud)

Orden de precedencia interna aproximado: los primeros alimentan
a los siguientes. VOICE_ARCHITECTURE recibe de CHARACTER_PHYSICS
(la herida del narrador determina sus puntos ciegos) y de
AESTHETIC_REGISTER (qué tipo de voz es compatible con el
régimen). STORY_SPINE es terminal (no puede formularse sin los
anteriores). SUBPLOT_ARCHITECTURE se diseña después de
STORY_SPINE: la línea principal precede al inventario de
subtramas porque las subtramas se definen por su relación con
la línea principal.

### CAPA 1.5 — DISEÑO INTERMEDIO
- SCALE_CALIBRATION.md (entre THEMATIC_ENGINE y STORY_SPINE:
  traduce escala temática y de proyecto a presupuesto
  operativo de palabras, capítulos, escenas)
- INFORMATION_CHOREOGRAPHY.md (entre NARRATIVE_CHRONOLOGY y
  STORY_SPINE: traduce fábula completa a calendario
  prospectivo de revelación al lector)

La Capa 1.5 captura la función específica de archivos que no
son ni decisiones puramente fundacionales (Capa 1 propia) ni
arquitectura de capítulo y escena (Capa 2). Operan como
traductores entre archivos de Capa 1 y archivos de Capa 1
terminales (STORY_SPINE) o archivos de Capa 2 (CHAPTER_BRIEF,
SCENE_NECESSITY). La nomenclatura "Capa 1.5" es información
genuina sobre la posición funcional del archivo; simplificar
a "Capa 1" perdería el matiz operativo.

### CAPA 2 — ARQUITECTURA DE CAPÍTULO Y ESCENA
- CHAPTER_BRIEF.md
- SCENE_NECESSITY.md
- SCENE_SHAPE.md
- ELLIPSIS_PROTOCOL.md
- SEAMS_AND_HINGES.md
- CONTINUITY_PHYSICS.md (Capa 2 transversal, memoria
  retrospectiva)
- TENSION_MECHANICS.md (Capa 2 transversal, conecta con
  Capa 3)

La cualificación "Capa N transversal" se aplica a archivos cuya
función es servicio o memoria que cruza varias operaciones del
ciclo de trabajo, no decisión puntual de capítulo o escena.
CONTINUITY_PHYSICS sincroniza estado retrospectivo entre
archivos del catálogo capítulo a capítulo; TENSION_MECHANICS
opera como mecanismo activo en Capa 2 (diseño de escena) y
también modula ejecución en Capa 3 (escritura). La
cualificación captura esta naturaleza distribuida y la
distingue de archivos de Capa 2 con función puntual
(CHAPTER_BRIEF, SCENE_NECESSITY, SCENE_SHAPE, ELLIPSIS_PROTOCOL,
SEAMS_AND_HINGES). La nomenclatura "Capa N transversal" se
generaliza a otras capas si la función transversal aparece en
ellas (por ejemplo, AESTHETIC_REGISTER es Capa 1 con función
moduladora transversal sobre Capa 3, según declaración
explícita del archivo huésped).

### CAPA 3 — EJECUCIÓN DE PROSA
- DIALOGUE_MECHANICS.md
- SUBTEXT_MECHANICS.md
- SENSORY_HIERARCHY.md
- SEMANTIC_OMISSION.md
- PROSODY_AND_MUSIC.md
- PROSE_LINE_DISCIPLINE.md (disciplina de la línea: cuotas
  globales y tics anti-LLM; modulada por AESTHETIC_REGISTER
  según régimen declarado, sobreescribible localmente por
  VOICE_ARCHITECTURE en su sección IDIOLECTO Y SOBREESCRITURA
  DE CUOTAS GLOBALES)

### CAPA 4 — REVISIÓN (post-primer borrador)
- REVISION_PROTOCOL.md

### TRANSVERSAL
- RESEARCH_LEDGER.md (alimenta a WORLD_TEXTURE, VOICE,
  CHARACTER cuando el proyecto requiere investigación).
- BRIEFING.md (registra estado operativo del proyecto y
  decisiones autorales acumuladas; archivo de servicio que
  toda ventana consulta al arrancar y actualiza al cerrar
  trabajo significativo).

### ARCHIVO FUNCIONAL EFÍMERO
- NEXT.md (plantilla de transición entre ventanas; cada
  instancia vive entre dos ventanas concretas, la emite la
  saliente y la consume la entrante).

Total: archivos operativos del catálogo permanente, según
naturaleza del proyecto. SERIES_ARCHITECTURE solo en serie;
WORLD_ARC solo en serie con mundo evolutivo de carga temática;
BRIEFING solo en proyectos de cuatro o más ventanas. NEXT no
forma parte del catálogo permanente: sus instancias son
efímeras.

---

## OPERACIONES (el ciclo de trabajo)

### OPERACIÓN 0 — FUNDACIÓN (al inicio, una vez)

Secuencia:
1. Si es serie: declarar SERIES_ARCHITECTURE.md (forma de serie,
   nº de volúmenes, pregunta por libro). Si además se cumplen
   los tres criterios de WORLD_ARC (mundo evolutivo, carga
   temática del mundo, declaración consciente), declarar
   WORLD_ARC.md después de SERIES_ARCHITECTURE y antes de los
   archivos de capa 1: forma dramática del arco de mundo, ejes
   en movimiento, dominancia, cruces con POVs, deudas, promesas,
   puntos de no retorno de mundo (o ausencia consciente),
   subordinación temática.
2. Declarar AESTHETIC_REGISTER.md, incluyendo declaración de
   LECTOR IMPLÍCITO (sección de AESTHETIC_REGISTER que ofrece
   cinco perfiles con implicaciones operativas y reglas de
   compatibilidad con régimen). La declaración del lector
   implícito es decisión temprana paralela al régimen porque
   la combinación lector × régimen es la que rige las cuotas
   moduladas en Capa 3.
3. Declarar GENRE_CONVENTIONS.md (género primario, géneros
   secundarios si aplica, postura del proyecto frente a las
   convenciones: aceptación, modulación o desafío declarado).
   Decisión temprana paralela al régimen estético: el régimen
   declara cómo se escribe; el género declara qué expectativas
   de lector el proyecto acepta, modula o desafía.
4. Formular THEMATIC_ENGINE.md.
5. Declarar SCALE_CALIBRATION.md.
6. Crear fichas CHARACTER_PHYSICS.md para cada personaje con arco.
7. Crear fichas RELATIONSHIP_PHYSICS.md para cada relación
   significativa.
8. Configurar WORLD_TEXTURE.md (mundo disponible).
9. Si aplica, abrir RESEARCH_LEDGER.md (backlog inicial).
10. Construir NARRATIVE_CHRONOLOGY.md (al menos capa 1:
    pre-narrativa completa). Los eventos pre-narrativos que
    explican las heridas declaradas en CHARACTER_PHYSICS y los
    nudos declarados en RELATIONSHIP_PHYSICS deben estar
    registrados aquí. Si WORLD_ARC está activo, los eventos
    pre-narrativos del arco de mundo (estados iniciales de los
    ejes, antecedentes de las deudas que se abrirán) también
    se registran.
11. Diseñar INFORMATION_CHOREOGRAPHY.md (calendario prospectivo
    de revelación al lector de los hechos de la fábula). Si
    WORLD_ARC está activo, el calendario incluye hechos de
    rango de mundo paralelos a los hechos de rango temático y
    de personaje.
12. Diseñar STORY_SPINE.md según plantilla elegida. Si WORLD_ARC
    está activo, las siembras del arco de mundo en libros
    iniciales son anclajes para deudas que cierran en libros
    posteriores; STORY_SPINE las integra como retoques.
13. Diseñar SUBPLOT_ARCHITECTURE.md (inventario de subtramas
    con forma, función, intersección con la línea principal,
    protocolo de salud). La línea principal precede al
    inventario de subtramas: las subtramas se definen por su
    relación con la línea principal declarada en STORY_SPINE.
14. Configurar VOICE_ARCHITECTURE.md (ficha por voz),
    incluyendo declaración de TIEMPO VERBAL DOMINANTE (sección
    de VOICE_ARCHITECTURE que ofrece cinco modos calibrados:
    PRESENTE HISTÓRICO, PASADO SIMPLE / PRETÉRITO,
    PLUSCUAMPERFECTO COMO MARCO, CONDICIONAL COMO FLASHBACK,
    ALTERNANCIA DECLARADA). La declaración del tiempo verbal
    dominante es decisión temprana paralela al régimen
    estético y al género primario porque fija la matriz
    enunciativa de cada frase.
15. Inicializar CONTINUITY_PHYSICS.md vacío.
16. Si el proyecto se distribuirá en cuatro o más ventanas de
    trabajo: inicializar BRIEFING.md con catálogo declarado,
    decisiones fundacionales tomadas, ningún pendiente derivado
    todavía, próximo paso apuntando a la primera ventana de
    capa 1 o a donde corresponda según planificación.

VERIFICACIÓN AL FINALIZAR OPERACIÓN 0:
- AESTHETIC_REGISTER compatible con SCALE declarada.
- LECTOR IMPLÍCITO compatible con régimen declarado (TEST 6 de
  AESTHETIC_REGISTER).
- GENRE_CONVENTIONS coherente con régimen estético y postura
  declarada (aceptación, modulación o desafío).
- THEMATIC_ENGINE encarnado en CHARACTER_PHYSICS.
- CHARACTER_PHYSICS coherente con RELATIONSHIP_PHYSICS.
- Heridas de CHARACTER_PHYSICS ancladas en eventos de
  NARRATIVE_CHRONOLOGY.
- STORY_SPINE alimentado por THEMATIC + CHARACTER + SCALE +
  NARRATIVE_CHRONOLOGY + INFORMATION_CHOREOGRAPHY.
- SUBPLOT_ARCHITECTURE coherente con STORY_SPINE: cada
  subtrama declara intersección con la línea principal y
  función específica.
- VOICE_ARCHITECTURE con TIEMPO VERBAL DOMINANTE declarado y
  coherente con AESTHETIC_REGISTER y GENRE_CONVENTIONS.
- Si es serie, SERIES_ARCHITECTURE coherente con THEMATIC de
  libro 1.
- Si WORLD_ARC declarado: forma dramática, ejes, deudas y
  promesas coherentes con SERIES_ARCHITECTURE (deudas y
  promesas en inventarios diferenciados con nomenclatura
  distinguible) y con THEMATIC_ENGINE (subordinación temática
  declarada, principios de neutralización formulados). Tabla de
  cruces POV × ejes coherente con CHARACTER_PHYSICS.
- Si BRIEFING activo: estado inicial registrado, decisiones
  fundacionales documentadas, próximo paso apuntando a primera
  ventana operativa.

Si hay incompatibilidad, revisar antes de continuar.
Escribir capítulos sin completar Operación 0 produce novelas
que se derrumban a mitad.

---

### OPERACIÓN 0.5 — BRIEF DE CAPÍTULO (al inicio de cada capítulo)

Secuencia:
1. Si BRIEFING activo: consulta inicial al BRIEFING para
   reconstruir contexto operativo del proyecto entero (estado
   del catálogo, decisiones acumuladas, pendientes derivados,
   próximo paso). Esta consulta es paso primero de la operación,
   anterior a cualquier otro archivo, en toda ventana que abra.
2. Consultar CONTINUITY_PHYSICS.md (estado de entrada).
3. Consultar STORY_SPINE.md (posición estructural) y
   SCALE_CALIBRATION.md (posición porcentual).
4. Consultar INFORMATION_CHOREOGRAPHY.md (qué hechos están en
   fase de siembra, eco, sospecha o confirmación en este
   capítulo). Si WORLD_ARC activo, incluir hechos de rango de
   mundo en la consulta.
5. Si WORLD_ARC activo y el capítulo toca manifestación de eje
   de mundo: consultar WORLD_ARC.md para verificar fase del eje
   en el libro en curso, deudas activas del eje, jerarquía de
   intensidad escénica declarada con los arcos personales del
   POV en escena. La consulta es obligatoria si hay cruce;
   omisible si no lo hay.
6. Consultar GENRE_CONVENTIONS.md para verificar qué
   convenciones del género primario aplican al capítulo
   (apertura, escena tipo, cierre esperado, lectura del lector
   de género). La consulta es ergonómica: el capítulo no
   tiene por qué cumplir la convención literalmente, pero la
   postura declarada en OPERACIÓN 0 (aceptación, modulación,
   desafío) debe ser coherente con lo que el capítulo hará.
7. Consultar SUBPLOT_ARCHITECTURE.md para identificar qué
   subtramas avanzan en el capítulo, qué intersecciones con la
   línea principal están programadas, qué deudas de subtrama
   tocan tratarse. El capítulo donde ninguna subtrama avanza
   y ninguna línea de la principal se mueve es candidato a
   revisión.
8. Completar CHAPTER_BRIEF.md (función única, deltas en los
   tres ejes, escenas necesarias).
9. Consultar THEMATIC_ENGINE.md (subtexto del capítulo).
10. Consultar CHARACTER_PHYSICS.md (fase actual del arco).
11. Consultar RELATIONSHIP_PHYSICS.md (vectores activos).
12. Si el capítulo es el primero, el último, o incluye
    transición POV: consultar SEAMS_AND_HINGES.md.
13. Si el proyecto requiere investigación bloqueante para este
    capítulo: resolver en RESEARCH_LEDGER.md antes de seguir.

SALIDA DE OPERACIÓN 0.5:
Un CHAPTER_BRIEF.md completo. Sin brief completo, no se pasa
a la escritura.

---

### OPERACIÓN A — DISEÑO DE ESCENA (por cada escena)

Secuencia:
1. Decidir si la escena existe narrativamente o se elide:
   cruzar SCENE_NECESSITY.md (las tres preguntas) con
   ELLIPSIS_PROTOCOL.md. Una escena puede ser necesaria y aun
   así elidirse si el efecto dramático lo requiere.
2. Si existe: identificar tipo según tipología de
   SCENE_NECESSITY.md.
3. Si es elipsis mayor: declarar en ELLIPSIS_PROTOCOL.md y
   registrar evento en NARRATIVE_CHRONOLOGY.md aunque no se
   narre.
4. Si WORLD_ARC activo y la escena cruza arco de personaje y
   arco de mundo: aplicar la jerarquía de intensidad escénica
   declarada en WORLD_ARC (personajes por encima de mundo,
   mundo por encima de personajes, simetría declarada,
   alternancia rítmica). La escena se diseña respetando la
   jerarquía: el evento de mundo entra como fricción sobre la
   rutina del POV, no como materia central, salvo orientación
   contraria explícita del proyecto.
5. Consultar GENRE_CONVENTIONS.md para verificar qué
   convenciones de la escena tipo aplican: estructuras,
   ritmos, gestos genéricos esperados por el lector del
   género. La postura declarada en OPERACIÓN 0 (aceptación,
   modulación, desafío) orienta la decisión de cumplir,
   modular o subvertir la convención de escena.
6. Si la escena trata contenido cargado (sexo, violencia,
   trauma, muerte, espiritualidad, política íntima, dolor
   físico extremo, ruptura): consultar ELLIPSIS_PROTOCOL.md
   sección TRATAMIENTO DE CONTENIDO CARGADO para decidir
   modo entre los cuatro disponibles (MOSTRADO, ELIDIDO,
   DESCRITO SECO, DESCRITO POÉTICO), coordinando con régimen
   estético y con la modulación de prosa de línea declarada
   en PROSE_LINE_DISCIPLINE.
7. Si la escena admite asimetría informativa entre lector y
   personajes (lector sabe algo que el personaje ignora, o
   viceversa, o lector y personaje saben distinto): consultar
   INFORMATION_CHOREOGRAPHY.md sección IRONÍA DRAMÁTICA para
   diseño formal de la asimetría (tipo, mecanismo, tempo de
   resolución, función estructural).
8. Completar SCENE_SHAPE.md (cuatro momentos, mapa de
   densidad, gestión de tiempo interno).
9. Consultar TENSION_MECHANICS.md (mecanismo activo).
10. Consultar SENSORY_HIERARCHY.md (qué sentido dominará).
11. Si es escena de apertura o cierre de novela, o bisagra
    importante entre capítulos: consultar SEAMS_AND_HINGES.md.
12. Si la novela admite paratextos o el capítulo es candidato
    para alguno (epígrafe, dedicatoria, nota de autor,
    glosario, mapa, árbol genealógico, calendario, índice,
    apéndice, anexo, título de capítulo con función
    estructural): consultar SEAMS_AND_HINGES.md sección
    PARATEXTO. La consulta en OPERACIÓN A es ergonómica
    (decidir si el paratexto procede); el diseño detallado del
    paratexto puede ocurrir en operación dedicada o en
    REVISION_PROTOCOL.

SALIDA DE OPERACIÓN A:
Una escena especificada pero no escrita, o una elipsis
declarada. Un LLM entrenado con estos archivos escribiría
aquí la escena con bastante autonomía.

---

### OPERACIÓN B — ESCRITURA DE PROSA

Aquí se produce la prosa. Durante la escritura, los archivos
de CAPA 3 operan en paralelo, sostenidos sobre la voz declarada
en VOICE_ARCHITECTURE (capa 1) que se mantiene activa porque
fija la matriz perceptiva, narrativa y enunciativa de cada
frase:

- VOICE_ARCHITECTURE.md (capa 1, sostén): mantener la voz.
- DIALOGUE_MECHANICS.md: aplicar en diálogos.
- SENSORY_HIERARCHY.md: elección de detalle.
- SUBTEXT_MECHANICS.md: no declarar lo que debe inferirse.
- PROSODY_AND_MUSIC.md: cadencia como oído de fondo
  (no se "aplica" frase a frase; se escucha).
- PROSE_LINE_DISCIPLINE.md: guard-rail selectivo en modo
  oído de fondo de cuotas globales y de tics anti-LLM, con
  énfasis especial en TIC 4 (frase-resumen al cierre de
  párrafo) y TIC 7 (mitigación atemperada), que son los tics
  más detectables sobre la marcha. La aplicación rigurosa
  por conteo cuantitativo (test de cuotas por capítulo) es
  trabajo de PASADA 4 del REVISION_PROTOCOL en OPERACIÓN C
  o D, no de OPERACIÓN B.

Si la escena incluye antagonismo activo (individual,
colectivo, interno, circunstancial, sociedad como
antagonista): consultar CHARACTER_PHYSICS.md sección TIPOS
DE ANTAGONISMO para identificar el tipo en juego y aplicar la
mecánica propia de construcción de presión que el archivo
declara para ese tipo. La consulta orienta la escritura en
escenas de fricción dramática alta.

REGLA OPERATIVA DURANTE ESCRITURA:
No aplicar SEMANTIC_OMISSION.md durante el primer borrador.
El primer borrador puede tener excesos que se filtran después.
Aplicar el filtro mientras se escribe bloquea el flujo y produce
prosa sobreregulada.

Tampoco aplicar PROSODY_AND_MUSIC.md con rigor frase a frase.
El trabajo prosódico fino es de PASADA 4 (ver REVISION_PROTOCOL).
Durante la escritura sólo se mantiene el oído.

PROSE_LINE_DISCIPLINE opera en modo oído de fondo durante
OPERACIÓN B, no en modo conteo cuantitativo riguroso. El
modo riguroso (test por capítulo, conteo de cuotas por mil
palabras, calibración por régimen y por idiolecto declarado)
pertenece a PASADA 4 del REVISION_PROTOCOL. Aplicar las
cuotas con rigor cuantitativo durante el primer borrador
produce el mismo bloqueo de flujo que SEMANTIC_OMISSION
aplicado prematuramente.

---

### OPERACIÓN C — CIERRE DE CAPÍTULO (después de escribir)

Secuencia:
1. Relectura completa del capítulo.
2. Aplicar filtros de SEMANTIC_OMISSION.md, modulados por
   AESTHETIC_REGISTER.md.
3. Verificar DIALOGUE_MECHANICS.md en diálogos.
4. Verificar SUBTEXT_MECHANICS.md (no declaración, prohibición
   central, excepción de síntoma).
5. Verificar SENSORY_HIERARCHY.md (jerarquía respetada,
   detalles reveladores).
6. Aplicar TEST POR CAPÍTULO de PROSE_LINE_DISCIPLINE.md:
   conteo cuantitativo de cuotas globales por mil palabras
   modulado por régimen estético declarado y por idiolectos
   sobreescriben en VOICE_ARCHITECTURE; verificación de tics
   anti-LLM con énfasis en TIC 4 (frase-resumen al cierre de
   párrafo) y TIC 7 (mitigación atemperada). Las desviaciones
   detectadas se anotan; las correcciones de prosa fina
   pertenecen a PASADA 4 del REVISION_PROTOCOL pero el test
   por capítulo da medida temprana de salud de la línea.
7. Si hay transición de capítulo o bisagra POV: verificar
   SEAMS_AND_HINGES.md (última frase del capítulo, primera
   del siguiente).
8. Actualizar CONTINUITY_PHYSICS.md en sus nueve registros.
9. Actualizar NARRATIVE_CHRONOLOGY.md con eventos de capa 2
   (lo narrado) y de capa 3 (lo invisible pero ocurrido).
10. Actualizar INFORMATION_CHOREOGRAPHY.md: ¿qué hechos se
    movieron en el capítulo? (siembra / eco / sospecha /
    confirmación / desmentido / consecuencia).
11. Si se usaron elipsis significativas: verificar en
    ELLIPSIS_PROTOCOL.md que están declaradas.

TRAMPA FRECUENTE:
Saltarse pasos 7-9 por prisa. Perder dos capítulos de trabajo
después cuando se descubre incoherencia.

---

### OPERACIÓN D — AUDITORÍA ESTRUCTURAL (cada 3-5 capítulos)

Revisión sistémica. Se hace SIEMPRE, no cuando "parece que hace
falta".

Secuencia:
1. Si BRIEFING activo: consulta para revisar decisiones
   acumuladas y verificar coherencia de la auditoría con el
   estado registrado del proyecto.
2. Revisar REGISTROS 3 y 4 de CONTINUITY_PHYSICS.md.
   ¿Está avanzando el arco de cada personaje? ¿Hay coste
   acumulado registrado?
3. Revisar REGISTRO 5. ¿Están vivos los vectores de relación?
4. Revisar REGISTRO 7. ¿Hay deudas en vías de olvido?
5. Revisar REGISTRO 8. ¿El patrón de tensión/descarga es sano?
6. Revisar REGISTRO 9. ¿Los motivos están siendo usados
   adecuadamente?
7. Consultar THEMATIC_ENGINE.md. ¿La pregunta central está
   escalando o se ha diluido?
8. Auditar SISTEMA DE IMÁGENES de THEMATIC_ENGINE.md. ¿Los
   campos visuales sostenedores del sistema están presentes
   con la frecuencia declarada en el archivo? ¿El sistema es
   coherente con los motivos recurrentes registrados en
   CONTINUITY_PHYSICS REGISTRO 9? ¿El sistema cruza con
   SENSORY_HIERARCHY en el detalle revelador?
9. Consultar STORY_SPINE.md. ¿Las escaladas previstas están
   ocurriendo en su posición esperada?
10. Auditar coherencia con GENRE_CONVENTIONS.md. ¿El proyecto
    sigue cumpliendo, modulando o desafiando las convenciones
    de género según la postura declarada en OPERACIÓN 0? ¿Hay
    transgresiones accidentales (no declaradas) de convenciones
    centrales del género que el lector de género detectaría
    como ruptura?
11. Auditar salud de subtramas en SUBPLOT_ARCHITECTURE.md.
    ¿Todas las subtramas declaradas están avanzando según su
    forma y función declaradas? ¿Alguna subtrama ha quedado a
    la deriva (sin avance reciente)? ¿Las intersecciones con
    la línea principal están ocurriendo según el calendario
    diseñado? ¿Hay subtramas que merecerían cierre o
    redistribución de recursos?
12. Consultar INFORMATION_CHOREOGRAPHY.md. ¿La cadencia real
    de revelación coincide con la diseñada? ¿Hay hechos
    sembrados sin eco, o confirmados sin siembra? Si la
    novela usa ironía dramática, verificar coherencia con el
    diseño de IRONÍA DRAMÁTICA del archivo.
13. Consultar NARRATIVE_CHRONOLOGY.md. ¿Cada efecto narrativo
    visible tiene causa registrada? ¿Hay elipsis mayores sin
    declarar?
14. Si es serie, consultar SERIES_ARCHITECTURE.md. ¿Los
    compromisos de serie siguen en pie? ¿El calendario de
    cierre de deudas de serie está a tiempo?
15. Si WORLD_ARC activo: revisar fase del eje de mundo según
    calendario por libro, pagos de deudas de mundo según
    calendario, asimetría con arcos personales (puntos de no
    retorno cruzados o no según declaración del proyecto), tests
    de funcionamiento del archivo: subordinación temática,
    reproducción funcional de ejes, asimetría intensidad
    escénica, coherencia de deudas y promesas, articulación
    inadecuada de patrones de mundo si el proyecto declara
    restricción específica.
16. Si hay investigación pendiente en RESEARCH_LEDGER.md con
    urgencia alta: resolver antes de seguir.
17. Revisar memoria estética: leer (o hacer releer) dos o tres
    pasajes de capítulos distantes. ¿Podrían ser de la misma
    novela?
18. Si BRIEFING activo y la auditoría detectó decisiones
    autorales nuevas o pendientes nuevos: actualizar BRIEFING
    antes de cerrar la auditoría.

SI LA AUDITORÍA DETECTA PROBLEMAS:
Activar el BUCLE DE RETROALIMENTACIÓN.

---

### OPERACIÓN E — LECTURA HOLÍSTICA

OPERACIÓN D es fiscal: audita registros. OPERACIÓN E es
lectura: experimenta la novela como lector, no como fiscal.

Son complementarias, no sustituibles.

### FRECUENCIA DURANTE ESCRITURA
- Al 50% aproximado del borrador: primera lectura corrida de
  todo lo escrito hasta ese momento.
- Al completar el primer borrador (100%): segunda lectura
  corrida antes del reposo obligatorio de REVISION_PROTOCOL.

### FRECUENCIA DURANTE REVISIÓN
- Al menos dos veces durante el ciclo de pasadas
  (ver REVISION_PROTOCOL.md, operaciones E-1 y E-2).

### MODO
Lectura corrida. No se editan líneas; se anotan impresiones
generales: dónde aburre, dónde acelera, dónde se pierde, dónde
suena distinto al resto.

### SALIDA
Lista de zonas a trabajar en la pasada correspondiente.
Si la OPERACIÓN E detecta problema estructural mayor, activa
vuelta a OPERACIÓN D (o a Pasada 1 de revisión si se está ya
en fase post-borrador).

---

## CICLO DE REVISIÓN (post-primer borrador)

Cuando el primer borrador está completo (todos los capítulos
escritos, OPERACIÓN C ejecutada en cada uno, OPERACIÓN D
ejecutada en sus hitos), se entra en fase de revisión.
Gobernada por REVISION_PROTOCOL.md.

Ejecución obligatoriamente ordenada:

1. REPOSO (duración según escala, ver REVISION_PROTOCOL).
2. PASADA 1 — ESTRUCTURAL.
3. PASADA 2 — DE ARCO Y COHERENCIA (incluye verificación de
   NARRATIVE_CHRONOLOGY, INFORMATION_CHOREOGRAPHY,
   CHARACTER_PHYSICS, RELATIONSHIP_PHYSICS, motivos de
   THEMATIC_ENGINE).
4. OPERACIÓN E-1.
5. PASADA 3 — DE VOZ (unidad de VOICE_ARCHITECTURE,
   AESTHETIC_REGISTER).
6. PASADA 4 — DE LÍNEA (SEMANTIC_OMISSION, DIALOGUE, SUBTEXT,
   SENSORY, PROSODY, modulados por AESTHETIC_REGISTER).
7. OPERACIÓN E-2.
8. PASADA 5 — DE PROOFS (coherencia final con
   CONTINUITY_PHYSICS y NARRATIVE_CHRONOLOGY; ortografía,
   tipografía).

CRITERIO DE TERMINACIÓN: ver REVISION_PROTOCOL.md. Sin
criterio de parada aplicado, las pasadas se vuelven infinitas.

---

## BUCLE DE RETROALIMENTACIÓN (crítico)

La arquitectura no es de sentido único (Capa 1 ordena, Capa 3
obedece). La prosa a veces descubre cosas que la Capa 1 no
previó, y estos descubrimientos deben poder modificar la Capa 1.

### DÓNDE SE ACTIVA EL BUCLE

Durante OPERACIÓN B (escritura), pueden aparecer:
- Un personaje que quiere actuar de forma incompatible con su
  ficha de CHARACTER_PHYSICS.
- Una relación que se está moviendo más rápido o más lento
  de lo previsto.
- Un motivo que emerge sin haberse diseñado.
- Una escena que pide una plantilla estructural distinta.
- Un evento que no estaba en NARRATIVE_CHRONOLOGY y se vuelve
  necesario.
- Una revelación que el calendario de INFORMATION_CHOREOGRAPHY
  ubicaba más adelante pero que pide salir aquí.

### PROTOCOLO DEL BUCLE

Cuando la prosa propone una modificación a Capa 1:

1. NO ignorar el impulso. La resistencia del material es
   información.
2. NO obedecer ciegamente. A veces la prosa va en dirección
   equivocada porque un filtro falló.
3. Evaluar: ¿la propuesta fortalece o debilita la pregunta
   central?
4. Si la fortalece: anotar como propuesta, confirmar en
   próxima OPERACIÓN D, actualizar archivo correspondiente.
5. Si la debilita: revisar la prosa; posiblemente el filtro
   correcto falló.
6. Si es neutra: decidir según criterio estético y mantener
   coherencia.

### CUÁNDO SE CONFIRMA LA MODIFICACIÓN

Las modificaciones de Capa 1 se confirman en OPERACIÓN D,
no durante OPERACIÓN B. Durante la escritura se anota la
propuesta; en la auditoría se decide.

Modificaciones de NARRATIVE_CHRONOLOGY son frecuentes (el
mundo se enriquece durante la escritura). Modificaciones de
THEMATIC_ENGINE son raras; si se hacen con frecuencia, la
pregunta central estaba mal formulada.

---

## REGLA DE PRECEDENCIA (contextual, no absoluta)

En caso de conflicto entre archivos, la precedencia es:

### REGLA BASE
CAPA 0.5 > CAPA 1 > CAPA 2 > CAPA 3.
La serie manda sobre el libro, el diseño sobre la estructura,
la estructura sobre el filtro de prosa.

### PRECEDENCIAS ESPECÍFICAS

- NARRATIVE_CHRONOLOGY precede a STORY_SPINE: la fábula
  existe antes que la trama; la trama la usa.
- THEMATIC_ENGINE precede a CHARACTER_PHYSICS: la pregunta
  central determina qué arcos son legítimos.
- INFORMATION_CHOREOGRAPHY es prospectiva; CONTINUITY_PHYSICS
  registro 6 es retrospectiva. Si divergen, actualizar la
  prospectiva (el diseño cambió) o corregir la retrospectiva
  (la ejecución falló).
- SCENE_NECESSITY y ELLIPSIS_PROTOCOL son hermanas: la escena
  que no existe también es decisión. Ambas consultan antes de
  narrar.
- REVISION_PROTOCOL (Capa 4) no opera durante la escritura
  del primer borrador. Intentar aplicarlo antes de su tiempo
  bloquea el avance.
- SERIES_ARCHITECTURE y WORLD_ARC son archivos paralelos en
  capa 0.5, sin jerarquía entre ellos. Sus deudas y promesas
  conviven en inventarios diferenciados con nomenclatura
  distinguible. Cuando una promesa cruza arco de personaje y
  arco de mundo (entrega vía mundo de algo que parecía de
  personaje, o viceversa), el cruce se declara explícitamente
  y la auditoría de calendario consolidado revisa el conjunto.
- WORLD_ARC precede a STORY_SPINE en manifestación de ejes de
  mundo: la manifestación entra como fricción sobre la rutina
  del POV, no como materia central del capítulo. STORY_SPINE
  integra las siembras del arco de mundo como retoques o
  inserciones específicas, no como armazón estructural.
- THEMATIC_ENGINE precede a WORLD_ARC en subordinación
  temática: el arco de mundo no puede resolver la pregunta
  central por vía macro. La subordinación se ejecuta por los
  principios de neutralización declarados en WORLD_ARC.
- BRIEFING no precede ni se subordina a otros archivos: es
  servicio operativo transversal. Su consulta y actualización
  son operaciones del flujo, no decisiones de contenido. Las
  decisiones autorales que el briefing registra viven en los
  archivos del catálogo correspondientes; el briefing solo es
  índice operativo de acceso rápido.
- AESTHETIC_REGISTER y GENRE_CONVENTIONS son archivos
  paralelos en Capa 1, sin jerarquía absoluta entre ellos.
  AESTHETIC declara cómo se escribe (régimen, lector
  implícito); GENRE declara qué expectativas de lector el
  proyecto acepta, modula o desafía. Cuando se contradicen,
  la postura declarada en GENRE (aceptación, modulación,
  desafío) determina cómo se resuelve la tensión: en
  proyectos de aceptación, el régimen estético se acomoda a
  las convenciones del género; en proyectos de modulación,
  ambos archivos se equilibran caso a caso; en proyectos de
  desafío, la decisión estética puede dominar pero el
  desafío al género debe estar declarado, no accidental.
- STORY_SPINE precede a SUBPLOT_ARCHITECTURE: la línea
  principal existe antes que las subtramas; las subtramas
  se definen por su forma de intersección con la línea
  principal. Cualquier subtrama declarada en SUBPLOT_
  ARCHITECTURE hereda las decisiones estructurales de
  STORY_SPINE.
- PROSE_LINE_DISCIPLINE es Capa 3 modulada por
  AESTHETIC_REGISTER (que ajusta cuotas globales según
  régimen y según LECTOR IMPLÍCITO declarado) y
  sobreescribible localmente por VOICE_ARCHITECTURE en su
  sección IDIOLECTO Y SOBREESCRITURA DE CUOTAS GLOBALES
  (cuando un POV o narrador tiene idiolecto declarado, sus
  cuotas locales sobreescriben las globales). En conflicto:
  AESTHETIC > PROSE_LINE_DISCIPLINE, VOICE > PROSE_LINE_
  DISCIPLINE en su jurisdicción local.

### EXCEPCIONES DECLARADAS

#### EXCEPCIÓN 1 — SÍNTOMA DE PERSONAJE
Si un personaje está en FASE 3 o 4 de su arco de defensa
(ver CHARACTER_PHYSICS.md), sus acciones, diálogos o
pensamientos pueden violar filtros de Capa 3 como síntoma de
su descomposición defensiva.
En este caso: CHARACTER_PHYSICS > SEMANTIC_OMISSION,
CHARACTER_PHYSICS > DIALOGUE_MECHANICS,
CHARACTER_PHYSICS > SUBTEXT_MECHANICS,
CHARACTER_PHYSICS > PROSE_LINE_DISCIPLINE. La descomposición
defensiva del personaje en fase 3-4 puede manifestarse como
violación localizada de cuotas globales (frase-resumen
exagerada al cierre, mitigaciones acumuladas, sintaxis
sobrecargada) que CHARACTER_PHYSICS legitima como síntoma
del estado interno; el filtro de PROSE_LINE_DISCIPLINE no se
aplica con rigor cuantitativo en pasajes así marcados, y
PASADA 4 del REVISION_PROTOCOL respeta la excepción cuando
está declarada.

#### EXCEPCIÓN 2 — RÉGIMEN ESTÉTICO
AESTHETIC_REGISTER.md modula agresividad de filtros.
En régimen expansivo o barroco, SEMANTIC_OMISSION se suaviza.
En régimen oral, VOICE_ARCHITECTURE domina sobre cualquier
otro filtro de Capa 3.

#### EXCEPCIÓN 3 — INMERSIÓN DE MUNDO
En régimen naval, histórico o especializado (declarado en
AESTHETIC_REGISTER), WORLD_TEXTURE puede permitir detalle
técnico que SEMANTIC_OMISSION marcaría como exceso, porque la
inmersión es la función.

#### EXCEPCIÓN 4 — VOZ NO FIABLE
Si VOICE_ARCHITECTURE declara narrador no fiable, la
"incoherencia" entre lo narrado y lo inferible no es error:
es el método. Esto tiene precedencia sobre filtros de
continuidad en CONTINUITY_PHYSICS.md, que debe registrar ambas
versiones (la narrada y la real).
NARRATIVE_CHRONOLOGY mantiene siempre la versión real.

#### EXCEPCIÓN 5 — PLANTILLA KISHŌTENKETSU
Si STORY_SPINE declara kishōtenketsu, la prohibición de
SCENE_NECESSITY ("toda escena debe cambiar algo") se
reformula: el cambio puede ser de comprensión del lector, no
de estado manifiesto.

#### EXCEPCIÓN 6 — SERIE EN CURSO
Si el proyecto es multivolumen, SERIES_ARCHITECTURE puede
sostener deudas o estados de personaje que, en libro único,
CONTINUITY exigiría cerrar. Las deudas de serie tienen ventana
propia, declarada en SERIES_ARCHITECTURE.

#### EXCEPCIÓN 7 — ELIPSIS MAYOR DELIBERADA
Una elipsis mayor declarada en ELLIPSIS_PROTOCOL puede omitir
un evento que CHARACTER_PHYSICS o RELATIONSHIP_PHYSICS
considerarían central. El evento sigue existiendo en
NARRATIVE_CHRONOLOGY; su omisión es el método.

#### EXCEPCIÓN 8 — JERARQUÍA DE INTENSIDAD ESCÉNICA
Si WORLD_ARC declara orientación específica entre profundidad
de personajes y profundidad de mundo (personajes por encima
de mundo, mundo por encima de personajes, simetría declarada,
alternancia rítmica), esa orientación se aplica como excepción
contextual a la regla base de precedencia entre arcos de
personaje y arco de mundo. La declaración vive en WORLD_ARC.md
y opera en OPERACIÓN A para diseñar las escenas de cruce.

### PRINCIPIO GENERAL
Las excepciones deben estar DECLARADAS en el archivo
correspondiente. Un conflicto no declarado se resuelve por la
regla base. Un conflicto declarado en sus términos se resuelve
por la excepción.

---

## MEMORIA DEL SISTEMA

El sistema tiene cuatro capas de memoria:

### MEMORIA OPERATIVA
CONTINUITY_PHYSICS.md. Registra el estado del mundo narrado
capítulo a capítulo. Es retrospectiva.

### MEMORIA DE MUNDO
Compuesta. La memoria de mundo se descompone en tres archivos
con funciones distintas y complementarias.
- WORLD_TEXTURE.md registra el mundo en estado: configuración
  estable del entorno material, social y sensorial disponible
  para cualquier escena. Es referencia descriptiva.
- NARRATIVE_CHRONOLOGY.md registra la fábula completa del
  mundo, incluyendo eventos pre-narrativos, invisibles y
  proyectados. Es prospectiva y expansiva.
- WORLD_ARC.md (si activo) registra el mundo en proceso:
  trayectoria evolutiva multilibro con ejes, deudas, promesas y
  puntos de no retorno (o ausencia consciente). Es prospectiva
  y direccional.

Las tres se consultan para preguntas distintas: WORLD_TEXTURE
para textura material de cualquier escena, NARRATIVE_CHRONOLOGY
para causa/efecto y eventos por capa, WORLD_ARC para fase del
eje correspondiente al libro en curso.

### MEMORIA ESTÉTICA
Implícita. Se verifica en OPERACIÓN D relectura de pasajes
distantes. Si capítulos distantes no parecen de la misma
novela, la memoria estética se ha fracturado.

### MEMORIA OPERATIVA DE PROYECTO
BRIEFING.md (si activo). Registra estado del catálogo,
decisiones autorales acumuladas, pendientes derivados, próximo
paso. Es servicio operativo entre ventanas, no de capa
específica. Toda ventana lo consulta al arrancar y lo actualiza
al cerrar trabajo significativo.

Las cuatro memorias deben mantenerse coordinadas. Divergencia
entre ellas señala error concreto:
- CONTINUITY vs NARRATIVE_CHRONOLOGY: revisar qué se narró y
  qué no; actualizar la que refleje peor la realidad.
- WORLD_TEXTURE vs WORLD_ARC (si activo): la textura debe
  coherer con la fase del eje en el libro en curso. Si textura
  describe mundo en estado X pero el arco está en fase Y, hay
  desfase.
- Memoria estética fracturada: problema de VOICE o de
  AESTHETIC_REGISTER.
- BRIEFING desactualizado respecto a archivos del catálogo:
  ventana cerró sin actualizar; reconstruir antes de seguir.

---

## ERRORES DEL SISTEMA A EVITAR

### ERROR 1 — DOGMATISMO DE FILTROS
Aplicar SEMANTIC_OMISSION sin modular por régimen.
Prevención: primera consulta de cada filtro es a
AESTHETIC_REGISTER.

### ERROR 2 — IGNORAR EL BUCLE
Tratar Capa 1 como inmutable produce novelas ejecutadas pero
sin vida.
Prevención: OPERACIÓN D incluye revisión de propuestas
acumuladas.

### ERROR 3 — SALTARSE CONTINUITY O CHRONOLOGY
No actualizar CONTINUITY_PHYSICS y NARRATIVE_CHRONOLOGY
produce incoherencias acumulativas que sólo se descubren a
mitad.
Prevención: OPERACIÓN C no se considera completa sin ambas
actualizaciones.

### ERROR 4 — OPERACIÓN 0.5 LIGERA
Empezar a escribir capítulo sin brief completo produce
capítulos decorativos.
Prevención: sin brief no hay escritura.

### ERROR 5 — AUDITAR RARAMENTE
Posponer OPERACIÓN D produce desviaciones estructurales que
solo se detectan tarde.
Prevención: cada 3-5 capítulos, sin excepción.

### ERROR 6 — FILTROS DURANTE ESCRITURA
Aplicar filtros de Capa 3 mientras se escribe el borrador
produce prosa sobrefiltrada.
Prevención: borrador primero, filtros después.

### ERROR 7 — MÚLTIPLES VOCES SIN DIFERENCIACIÓN
Entrar en multi-POV sin fichas diferenciadas en
VOICE_ARCHITECTURE produce voces intercambiables.
Prevención: test de identificación sin atribución cada pocos
capítulos.

### ERROR 8 — REVELACIÓN ANTICIPADA
El sistema (o el LLM que lo ejecuta) explica al lector hechos
que INFORMATION_CHOREOGRAPHY programaba para más adelante.
Prevención: consultar calendario prospectivo en OPERACIÓN 0.5.

### ERROR 9 — SALTARSE EL REPOSO
Entrar en REVISION_PROTOCOL sin el reposo previo produce
pasada 1 contaminada por memoria de escritura.
Prevención: respetar tiempos de REVISION_PROTOCOL.

### ERROR 10 — REVISIÓN DESORDENADA
Ejecutar pasadas fuera de orden (pulir línea antes de cerrar
estructura). Resultado: trabajo perdido.
Prevención: orden 1→5 sin excepción salvo vuelta atrás por
detección de problema mayor.

### ERROR 11 — ELIPSIS SIN DECLARAR
Un evento importante se omite sin declararlo en
ELLIPSIS_PROTOCOL. Se comporta como agujero en lectura.
Prevención: toda omisión que afecte vectores o fase de arco
se declara.

### ERROR 12 — SERIE NO GESTIONADA
Escribir libro 1 sin SERIES_ARCHITECTURE cuando el proyecto
es multivolumen fuerza improvisación retroactiva en libros
posteriores.
Prevención: versión mínima de SERIES_ARCHITECTURE antes del
capítulo 1 si el proyecto es serie declarada.

### ERROR 13 — ARTICULACIÓN INADECUADA DE PATRONES DE MUNDO
Si WORLD_ARC declara que ciertos patrones del arco de mundo
no deben articularse por personajes ni narrador (efectos que
dependen de no-articulación), una articulación accidental
rompe el régimen estético del proyecto y el efecto colapsa.
Prevención: declarar explícitamente en WORLD_ARC qué patrones
operan por no-articulación, auditar en OPERACIÓN D la
articulación inadecuada.

### ERROR 14 — EVENTO DE MUNDO COMO MATERIA CENTRAL DE CAPÍTULO
Capítulo donde el evento de mundo desplaza la rutina del POV
y se convierte en sustancia central. El evento de mundo debe
entrar como fricción sobre la rutina, no como tema. Cuando se
invierte la jerarquía declarada en WORLD_ARC, el capítulo
deviene exposición narratorial.
Prevención: regla de OPERACIÓN A respetar jerarquía de
intensidad escénica, auditoría en OPERACIÓN D.

### ERROR 15 — EVENTO DE MUNDO COMO CLÍMAX DE LIBRO
El clímax del libro pertenece a los arcos personales (salvo
orientación contraria explícita del proyecto). Si el evento
de mundo opera como clímax, el centro narrativo del libro se
desplaza al sistema y los personajes pierden agencia.
Prevención: el cierre argumentativo del arco de mundo es
típicamente lateral al clímax personal del libro final, no
coincidente. Verificar en STORY_SPINE y en auditoría de
WORLD_ARC.

### ERROR 16 — BRIEFING DESACTUALIZADO
Una ventana cierra sin actualizar el BRIEFING habiendo
cerrado archivo del catálogo, tomado decisión autoral nueva
o identificado pendientes. La ventana siguiente arranca con
información obsoleta y reconstruye contexto erróneo o
duplica trabajo.
Prevención: la actualización del BRIEFING al cierre es paso
explícito, no implícito. Una ventana que cambió algo que la
siguiente ventana necesita saber actualiza el briefing antes
de cerrar.

### ERROR 17 — TRANSICIÓN ENTRE VENTANAS SIN NEXT
Una ventana cierra trabajo continuable sin emitir NEXT. La
ventana siguiente arranca sin tarea específica, reconstruye
desde BRIEFING qué hacer y arranca con fricción evitable.
Prevención: emisión de NEXT al cierre cuando el trabajo es
continuable, declarada como paso explícito de la operación
de cierre de ventana.

### ERROR 18 — INCUMPLIMIENTO DE CUOTAS DE PROSE_LINE
La prosa del primer borrador o de capítulo cerrado excede
las cuotas globales de PROSE_LINE_DISCIPLINE moduladas por
régimen estético declarado. Tics anti-LLM detectables en
oído de fondo (con énfasis en TIC 4 frase-resumen al cierre
de párrafo y TIC 7 mitigación atemperada) aparecen sin
justificación de idiolecto o de síntoma de personaje. La
prosa pierde tensión y suena a producto de modelo de
lenguaje sin disciplina.
Prevención: TEST POR CAPÍTULO de PROSE_LINE en OPERACIÓN C
y PASADA 4 del REVISION_PROTOCOL en revisión rigurosa.
Distinguir tic LLM de rasgo declarado de idiolecto o de
género: si el rasgo está declarado en VOICE_ARCHITECTURE
(IDIOLECTO Y SOBREESCRITURA DE CUOTAS GLOBALES) o en
GENRE_CONVENTIONS (rasgo de género específico), no es tic;
si no está declarado, es tic y se corrige.

### ERROR 19 — TRANSGRESIÓN ACCIDENTAL DE CONVENCIONES DE GÉNERO
El proyecto, sin haber declarado postura de desafío en
OPERACIÓN 0, transgrede convención central del género
primario y rompe la lectura del lector de género sin
intencionalidad. Resultado: el lector espera un movimiento
del género que no llega y el proyecto pierde la lectura
sin haber ganado nada.
Prevención: declaración explícita de postura en
GENRE_CONVENTIONS al inicio (aceptación, modulación,
desafío); auditoría de coherencia en OPERACIÓN D;
verificación en OPERACIÓN A de cada escena tipo.

### ERROR 20 — SUBTRAMA DEJADA A LA DERIVA
Una subtrama declarada en SUBPLOT_ARCHITECTURE deja de
avanzar durante varios capítulos sin que el archivo registre
cierre, suspensión declarada o redistribución. La subtrama
queda en estado fantasma: el lector la recuerda y espera
movimiento que no llega; el sistema no la trabaja pero
tampoco la cierra.
Prevención: auditoría de salud de subtramas en OPERACIÓN D
(cada 3-5 capítulos); decisión explícita en
SUBPLOT_ARCHITECTURE cuando se decide cerrar, suspender o
redistribuir; registro de la decisión.

### ERROR 21 — CONFUSIÓN ENTRE TIC LLM Y RASGO DECLARADO
Una corrección de PROSE_LINE_DISCIPLINE elimina rasgo que
estaba declarado en VOICE_ARCHITECTURE como idiolecto del
narrador o del POV, o rasgo declarado en GENRE_CONVENTIONS
como característica del género primario. Resultado: la voz
pierde diferenciación o el género pierde un marcador
esperado por el lector.
Prevención: antes de aplicar corrección de PROSE_LINE en
PASADA 4, cruzar el rasgo candidato con (a) IDIOLECTO Y
SOBREESCRITURA DE CUOTAS GLOBALES de VOICE_ARCHITECTURE,
(b) marcadores de género declarados en GENRE_CONVENTIONS.
Si el rasgo está declarado en alguno de los dos, es rasgo
legítimo, no tic. La sección RELACIÓN CON OTROS ARCHIVOS de
PROSE_LINE_DISCIPLINE documenta este protocolo de
distinción.

---

## AUTONOMÍA Y DECISIÓN

Este sistema está diseñado para que un modelo con arquitectura
suficiente pueda tomar decisiones locales sin consulta constante
al autor humano. Pero hay clases de decisión que el sistema no
debería tomar solo.

### DECISIONES QUE EL SISTEMA PUEDE TOMAR
- Elección de detalle sensorial concreto.
- Longitud específica de una escena.
- Orden de turnos en un diálogo.
- Detalle de textura de mundo.
- Cadencia de un párrafo.
- Elección de mecanismo de tensión entre los disponibles.
- Añadir evento de capa 3 (invisible) a NARRATIVE_CHRONOLOGY
  si coherencia lo exige.
- Reajustar cadencia menor de INFORMATION_CHOREOGRAPHY
  (desplazar un eco un capítulo, por ejemplo).
- Actualizar BRIEFING con cambios de estado del catálogo,
  pendientes resueltos, próximo paso ajustado.
- Emitir NEXT al cierre de ventana con las seis secciones
  formuladas según el trabajo de la ventana.

### DECISIONES QUE EL SISTEMA DEBE SEÑALAR
- Cambio de plantilla estructural a mitad de novela.
- Promoción de un secundario a protagonista.
- Alteración significativa del arco de un personaje.
- Revisión de la formulación de la pregunta central.
- Decisión de abandonar una deuda abierta.
- Revelación anticipada de hecho temático.
- Reformulación de elipsis mayor declarada.
- Si serie: redistribución de deudas entre libros.
- Si WORLD_ARC activo: alteración de forma dramática del arco
  de mundo, cambio de jerarquía de intensidad escénica
  declarada, decisión de abandonar deuda de mundo abierta,
  reformulación de principio de neutralización temática.
- Si BRIEFING activo: registro de decisión autoral nueva en
  el briefing.

Estas decisiones se registran como propuestas en OPERACIÓN D.

---

## SECUENCIA COMPLETA DE EJECUCIÓN

Vista sintética del ciclo completo:

1. OPERACIÓN 0 — una vez, al inicio. Declaraciones tempranas:
   AESTHETIC_REGISTER con LECTOR IMPLÍCITO; GENRE_CONVENTIONS
   con postura declarada (aceptación, modulación, desafío);
   THEMATIC_ENGINE con sus motivos y SISTEMA DE IMÁGENES si
   aplica; SCALE_CALIBRATION; CHARACTER_PHYSICS y
   RELATIONSHIP_PHYSICS; WORLD_TEXTURE; NARRATIVE_CHRONOLOGY;
   INFORMATION_CHOREOGRAPHY (con IRONÍA DRAMÁTICA si el
   proyecto la usa); STORY_SPINE; SUBPLOT_ARCHITECTURE;
   VOICE_ARCHITECTURE con TIEMPO VERBAL DOMINANTE declarado
   (presente histórico, pasado simple/pretérito,
   pluscuamperfecto como marco, condicional como flashback,
   alternancia declarada). Si serie con mundo evolutivo,
   declaración de WORLD_ARC. Si proyecto multiventana,
   inicialización de BRIEFING.
2. Por cada ventana de trabajo que abra:
   a. Si NEXT recibido de ventana anterior: lectura del NEXT
      antes que cualquier otro archivo (cabecera y tarea
      específica primero).
   b. Si BRIEFING activo: lectura del briefing para contexto
      general del proyecto, después del NEXT y antes de los
      archivos del catálogo.
3. Por cada capítulo:
   a. OPERACIÓN 0.5 — brief, con consultas a GENRE
      (convenciones del capítulo) y a SUBPLOT_ARCHITECTURE
      (qué subtramas avanzan).
   b. Por cada escena (o elipsis declarada):
      - OPERACIÓN A — diseño, con consultas a GENRE
        (convenciones de escena), a ELLIPSIS_PROTOCOL sección
        TRATAMIENTO DE CONTENIDO CARGADO si aplica, a SEAMS
        sección PARATEXTO si la escena admite paratextos, a
        INFORMATION_CHOREOGRAPHY sección IRONÍA DRAMÁTICA si
        la escena admite asimetría informativa.
      - OPERACIÓN B — escritura (si la escena se narra), con
        PROSE_LINE_DISCIPLINE como guard-rail en oído de
        fondo (énfasis en TIC 4 y TIC 7, no conteo riguroso)
        y consulta a CHARACTER_PHYSICS sección TIPOS DE
        ANTAGONISMO si la escena incluye antagonismo activo.
   c. OPERACIÓN C — cierre de capítulo, incluyendo TEST POR
      CAPÍTULO de PROSE_LINE_DISCIPLINE.
4. Cada 3-5 capítulos: OPERACIÓN D — auditoría, incluyendo
   coherencia con GENRE_CONVENTIONS, salud de subtramas en
   SUBPLOT_ARCHITECTURE, auditoría de SISTEMA DE IMÁGENES de
   THEMATIC_ENGINE. Si BRIEFING activo, consulta inicial y
   actualización al cierre.
5. Al 50% y al 100%: OPERACIÓN E — lectura holística.
6. En cualquier punto de OPERACIÓN B, propuesta que toca Capa
   1 o capa 0.5: anotar, llevar a próxima OPERACIÓN D.
7. Al cierre de cada ventana de trabajo:
   a. Si la ventana cerró archivo del catálogo, tomó decisión
      autoral, identificó pendientes o resolvió alguno: actualizar
      BRIEFING.
   b. Si la ventana cierra trabajo continuable que la siguiente
      ventana ejecutará: emitir NEXT con las seis secciones.
8. Al completar 100% y tras reposo: ciclo de
   REVISION_PROTOCOL (pasadas 1→5 con OPERACIÓN E-1 y E-2
   intercaladas, FEEDBACK EXTERNO en pasada o sub-pasada
   declarada del protocolo). Si WORLD_ARC activo, su
   auditoría es parte de PASADA 1. PASADA 4 aplica
   PROSE_LINE_DISCIPLINE en modo conteo cuantitativo
   riguroso, distinguiendo tic LLM de rasgo declarado de
   idiolecto (en VOICE_ARCHITECTURE) o de género (en
   GENRE_CONVENTIONS).
9. Criterio de terminación aplicado (ver REVISION_PROTOCOL).

---

## TESTS DE FUNCIONAMIENTO DEL SISTEMA

TEST 1 — EJECUCIÓN DE OPERACIÓN 0
¿El sistema puede completar OPERACIÓN 0 sin contradicciones
internas? Si no, los inputs iniciales son incompatibles y
deben revisarse antes de escribir.

TEST 2 — COHERENCIA DE BRIEF
¿Cada CHAPTER_BRIEF se puede completar con datos de la
arquitectura? Si el sistema tiene que inventar datos nuevos,
algo falta en las capas anteriores.

TEST 3 — TRAZABILIDAD DE FÁBULA
Para cualquier efecto narrativo en un capítulo: ¿hay causa
registrada en NARRATIVE_CHRONOLOGY? Si no, la cadena causal
tiene agujeros.

TEST 4 — CADENCIA DE INFORMACIÓN
¿La cadencia real de revelación (registrada en CONTINUITY
registro 6) coincide con la diseñada en INFORMATION_
CHOREOGRAPHY? Si diverge, revisar cuál es correcta.

TEST 5 — ESTABILIDAD EN AUDITORÍA
Después de 10 capítulos, ¿la arquitectura de Capa 1 ha
cambiado sustancialmente? Algún cambio es signo de
descubrimiento sano. Cambios grandes y frecuentes son signo
de arquitectura mal fundada.

TEST 6 — AUTONOMÍA OPERATIVA
¿El sistema puede producir un capítulo sin input externo
más allá de los archivos? Si sí, la arquitectura está
trabajando.

TEST 7 — COMPLETITUD DE REVISIÓN
¿Las cinco pasadas se ejecutaron en orden, con reposo previo,
con OPERACIÓN E-1 y E-2 intercaladas? Si no, la novela no
está terminada todavía.

TEST 8 — DISCIPLINA DE FLUJO DE VENTANAS
Si BRIEFING activo: ¿toda ventana que cerró trabajo
significativo actualizó el briefing antes de cerrar? Si toda
ventana que cerró trabajo continuable emitió NEXT a la
siguiente? Si la respuesta es no, hay fricción acumulada en
las transiciones que la próxima ventana absorberá como coste.

TEST 9 — INTEGRIDAD DEL ARCO DE MUNDO
Si WORLD_ARC activo: ¿la pregunta central permanece irresuelta
tras el cierre del último libro? ¿La función sistémica de cada
eje se preserva o se transforma según forma dramática
declarada? ¿La jerarquía de intensidad escénica se mantiene
en muestra de capítulos? Si alguno falla, el arco de mundo
está derivando.

TEST 10 — CONVENCIONES DE GÉNERO
¿Está declarado el género primario en GENRE_CONVENTIONS al
inicio del proyecto, con postura explícita (aceptación,
modulación, desafío)? ¿Las convenciones del género primario
están respetadas en escena, en capítulo, en libro, según la
postura declarada? Si la postura es desafío, ¿los desafíos
son intencionales y declarados, no accidentales? Si alguno
falla, el género opera mal y la lectura del lector de género
se rompe sin compensación.

TEST 11 — SALUD DE SUBTRAMAS
¿Todas las subtramas declaradas en SUBPLOT_ARCHITECTURE están
avanzando según su forma y función declaradas? ¿Alguna
subtrama ha quedado a la deriva (sin avance reciente sin
decisión explícita de cierre, suspensión o redistribución)?
¿Las intersecciones con la línea principal ocurren según el
calendario diseñado? Si alguna subtrama está fantasma, la
arquitectura está perdiendo recursos narrativos.

TEST 12 — DISCIPLINA DE LA LÍNEA
¿Las cuotas globales de PROSE_LINE_DISCIPLINE están dentro
del rango del régimen estético declarado y de los idiolectos
declarados en VOICE_ARCHITECTURE, por capítulo y por libro?
¿Los tics anti-LLM (con énfasis en TIC 4 y TIC 7) están
controlados o se manifiestan como rasgos legítimos de
idiolecto o de género declarado? Si las cuotas se incumplen
sin justificación, la prosa pierde tensión.

TEST 13 — SISTEMA DE IMÁGENES
Si THEMATIC_ENGINE declara SISTEMA DE IMÁGENES: ¿los campos
visuales sostenedores aparecen con la frecuencia declarada en
el archivo? ¿Los motivos recurrentes registrados en
CONTINUITY_PHYSICS REGISTRO 9 son coherentes con el sistema
declarado? ¿El sistema cruza con SENSORY_HIERARCHY en el
detalle revelador? Si el sistema se diluye, el motor temático
pierde anclaje sensorial.

TEST 14 — LECTOR IMPLÍCITO
¿La combinación lector implícito × régimen estético declarada
en AESTHETIC_REGISTER es productiva según TEST 6 del archivo
huésped? ¿La prosa real respeta las cuotas y mecanismos
asociados al lector implícito declarado? Si la combinación es
incompatible o la prosa se aparta del lector declarado, el
proyecto pierde a su lector previsto.

TEST 15 — TIEMPO VERBAL DOMINANTE
¿La voz mantiene el modo declarado en TIEMPO VERBAL DOMINANTE
de VOICE_ARCHITECTURE (presente histórico, pasado simple/
pretérito, pluscuamperfecto como marco, condicional como
flashback, alternancia declarada)? ¿Las alternancias declaradas
se respetan según las reglas declaradas y no por deriva? Si
el tiempo verbal deriva sin declaración, la matriz enunciativa
se vuelve inestable.

TEST 16 — TRATAMIENTO DE CONTENIDO CARGADO
Si la novela tiene escenas con contenido cargado (sexo,
violencia, trauma, muerte, espiritualidad, política íntima,
dolor extremo, ruptura): ¿el modo elegido por escena (entre
los cuatro de ELLIPSIS_PROTOCOL: MOSTRADO, ELIDIDO, DESCRITO
SECO, DESCRITO POÉTICO) se respeta en su ejecución? ¿La
coherencia entre escenas equivalentes se mantiene (escenas
del mismo tipo de contenido cargado se tratan con el mismo
modo o con declaración explícita de variación)? Si la
coherencia se rompe sin justificación, el régimen estético del
proyecto se quiebra en los pasajes más expuestos.

---

## TRANSICIÓN ENTRE VENTANAS

Sección que declara el protocolo formal de paso del testigo
entre ventanas de trabajo. La transición es operación
regular del sistema cuando el proyecto se distribuye en
múltiples ventanas, no improvisación al cierre.

### CIERRE DE VENTANA

Toda ventana que cierra trabajo continuable ejecuta el cierre
como operación explícita, no implícita. Pasos:

1. Verificar trabajo completado en la ventana: archivos
   cerrados o modificados, decisiones autorales tomadas,
   pendientes identificados, pendientes resueltos.
2. Si BRIEFING activo y la ventana cambió algo que la
   siguiente ventana necesita saber: actualizar BRIEFING en
   las secciones afectadas (estado del catálogo, decisiones
   autorales, pendientes derivados, próximo paso).
3. Si la ventana cierra trabajo continuable que ventana
   posterior ejecutará: emitir NEXT con las seis secciones
   declaradas en NEXT.md (cabecera, estado al cierre, tarea
   específica, insumos requeridos, voz del modelo saliente,
   verificación al cierre de la entrante).
4. Si la ventana cierra ciclo cerrado sin continuación
   inmediata planificada: la emisión de NEXT es opcional. En
   estos casos puede emitirse NEXT informativo registrando
   estado para futura ventana de retoma.

### ARRANQUE DE VENTANA

Toda ventana que arranca consume las transiciones recibidas
en este orden:

1. Lectura de NEXT recibido (si lo hay): cabecera y tarea
   específica primero para orientarse, después insumos
   requeridos, después voz del modelo saliente, finalmente
   verificación al cierre.
2. Lectura de BRIEFING (si activo): estado del catálogo y
   decisiones acumuladas para contexto general del proyecto.
3. Lectura de archivos del catálogo declarados como insumos
   en NEXT, en el orden que NEXT indique.
4. Ejecución de la tarea específica.

### REGLA DE NO SATURACIÓN

La emisión de NEXT y la actualización de BRIEFING son pasos
del cierre, no carga adicional. Si la ventana saliente está
al límite de capacidad, prioriza NEXT mínimo viable
(cabecera, tarea específica, insumos, voz del modelo) y
actualización mínima del BRIEFING (próximo paso reformulado)
sobre intentar emisión completa que sature. NEXT mínimo bien
formulado es preferible a NEXT extenso confuso por
saturación. La calidad del traspaso está sobre la
exhaustividad.

### CICLO DE VIDA DEL NEXT

NEXT es archivo funcional efímero. Cada instancia vive entre
dos ventanas concretas. Tras consumir el NEXT y completar la
tarea, la ventana entrante decide qué hacer con el archivo:
archivarlo en bitácora del proyecto si tiene valor histórico
(sospechas registradas que después resultaron correctas,
decisiones de transición que documentan el proceso) o
descartarlo si solo tenía valor instrumental para la
transición. La decisión es del proyecto, no del modelo.

### RELACIÓN CON PROTOCOLO DE CAPTURA DE APRENDIZAJE

Cuando la voz del modelo saliente en un NEXT registra
contenido que constituye fricción legítima del modelo
agnóstico (no solo del proyecto concreto), ese contenido
puede alimentar también al protocolo de captura del proyecto
agnóstico. La ventana entrante valora si trasladar el
contenido de la voz del modelo al registro formal del
protocolo, según las cinco situaciones declaradas en
PROTOCOLO_CAPTURA_APRENDIZAJE.md.

---

## NOTA FINAL SOBRE EL EXPERIMENTO

Este sistema no garantiza buena literatura. Garantiza
coherencia estructural, ausencia de errores elementales y una
plataforma desde la cual pueden emerger buenas decisiones.
El valor literario depende de:
- La calidad de la formulación inicial (pregunta central,
  personajes, régimen, fábula).
- La intuición en las decisiones locales que el sistema
  debe tomar.
- La disposición a escuchar lo que la prosa propone
  (bucle de retroalimentación).
- La disciplina en el ciclo de revisión (Capa 4).

Un sistema rígido produce novelas técnicamente correctas y
literariamente muertas. Un sistema sin estructura produce
caos. Un sistema con estructura y sin revisión produce
primeros borradores que nunca maduran. Este pretende ser un
sistema con estructura, poros y cierre.

---
---

