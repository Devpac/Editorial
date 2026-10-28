REGISTRO 001 — 2026-04-27

Campo 1 — Identificador: 001 / Captura 2026-04-27.

Campo 2 — Síntoma observado: Proyecto creativo intentó redactar
capítulo 1 tras CHAPTER_BRIEF y descubrió que cinco archivos
(SEAMS_AND_HINGES, TENSION_MECHANICS, DIALOGUE_MECHANICS,
SUBTEXT_MECHANICS, SENSORY_HIERARCHY) seguían vacíos. La
ventana entrante notó que escribir sin esas decisiones
producía prosa errática por POV. La OP 0 había cerrado
formalmente con verificación pasada.

Campo 3 — Diagnóstico del modelo: SYSTEM_ORCHESTRATION OP 0
cierra VOICE_ARCHITECTURE como disciplina previa pero deja
emergentes archivos paralelos cuyo contenido cumple función
análoga (mecánica por POV, jerarquía sensorial dominante,
apertura del libro, mecanismos por acto). La VERIFICACIÓN
audita coherencia, no exhaustividad por tipo operativo. El
modelo no distingue archivos que requieren cierre previo de
archivos que pueden emerger en oficio.

Campo 4 — Patrón general implícito: Las plantillas v7 clasifican
archivos por granularidad estructural (capa 1, 2, 3) pero no
por momento operativo (disciplina previa de proyecto, proceso
emergente por capítulo o escena, oficio tardío de revisión).
Esa frontera capa 1/2/3 es porosa: hay archivos cuyo contenido
debería pre-decidirse en proyectos densos (multivolumen,
multi-POV, gran escala, registro muy específico) y emerger
en proyectos ligeros. El modelo no ofrece mecanismo de
elevación condicional, paralelo al condicional ya implementado
para BRIEFING en OP 0 paso 14.

Campo 5 — Implicación para v7: (a) Añadir a SEAMS_AND_HINGES,
TENSION_MECHANICS, DIALOGUE_MECHANICS, SUBTEXT_MECHANICS y
SENSORY_HIERARCHY sección "MOMENTO DE CIERRE" declarando
cuándo conviene elevar a disciplina previa. (b) Añadir a
SYSTEM_ORCHESTRATION OP 0 paso condicional 15 (después de
BRIEFING) sobre elevación de archivos a disciplina previa
según densidad declarada. (c) Enriquecer VERIFICACIÓN AL
FINALIZAR OP 0 con criterio de exhaustividad por tipo
operativo, no solo coherencia entre presentes.

Marca de procesamiento — MODELO_DarkRomance v2.0, 23-10-2026:
(a) y (b), DESCARTADAS (regla del fork). Piden elevar reglas a
disciplina previa, es decir, aplicarlas antes de escribir. En
este modelo DIALOGUE_MECHANICS, SUBTEXT_MECHANICS y
SENSORY_HIERARCHY se leen después del borrador (adenda de
SYSTEM_ORCHESTRATION, §2), y lo que se decide antes es diseño
—biblia, preset y escaleta—, donde ya viven las decisiones de
SEAMS_AND_HINGES y TENSION_MECHANICS (apertura, ganchos,
picos). Se conservan como traza; no se aplican. (c), sin
procesar.

---

REGISTRO 002 — 2026-04-27

Campo 1 — Identificador: 002 / Captura 2026-04-27.

Campo 2 — Síntoma observado: Proyecto creativo a escala saga
multivolumen, al cerrar OP 0.5 del primer capítulo y abrir
OP A, enfrentó decisión no contemplada por el modelo: cómo
instanciar físicamente CHAPTER_BRIEF, SCENE_NECESSITY y
SCENE_SHAPE en el espacio de trabajo. La ventana saliente
emitió NEXT ofreciendo dos opciones (un archivo por capítulo
para cada plantilla; un archivo por escena para SHAPE y
NECESSITY). El cálculo proyectado superaba las cinco centenas
de archivos para la saga completa, volviendo el espacio de
trabajo ingobernable. El autor detectó por sí mismo opciones
intermedias no contempladas (fusión de plantillas hermanas;
absorción en archivo de capa anterior). La elección quedó
como decisión autoral huérfana de marco.

Campo 3 — Diagnóstico del modelo: Las plantillas describen
función y contenido (qué responder, qué decidir) pero no se
pronuncian sobre nomenclatura física ni granularidad de
instanciación en el proyecto creativo. SYSTEM_ORCHESTRATION
OP A formula "completar SCENE_SHAPE.md" usando el nombre de
la plantilla, lo que es ambiguo entre dos lecturas: modificar
un archivo único reutilizado, o producir una instancia nueva
con nomenclatura derivada. Las plantillas individuales hablan
de "esta escena", "este capítulo" como unidades conceptuales
sin mapearlas a archivos concretos. La ausencia obliga al
proyecto a improvisar política, y la improvisación pasa
invisible al sistema porque ningún archivo audita coherencia
de instanciación.

Campo 4 — Patrón general implícito: Las plantillas de cardinalidad
alta (las que se aplicarían naturalmente una vez por capítulo o
una vez por escena) producen, bajo lectura archivo-por-unidad,
inflación que bloquea proyectos a escala saga o novela larga.
La cardinalidad alta concentrada en capa 2 (CHAPTER_BRIEF,
SCENE_NECESSITY, SCENE_SHAPE) es problema operativo distinto al
de plantillas de cardinalidad alta acotada (CHARACTER_PHYSICS,
RELATIONSHIP_PHYSICS, VOICE_ARCHITECTURE), donde el conteo está
naturalmente limitado por escala declarada. El modelo no
distingue cardinalidad acotada de cardinalidad multiplicativa, y
trata ambas como si la nomenclatura emergiera sola.

Campo 5 — Implicación para v7: (a) Declarar política de
instanciación por defecto para las tres plantillas de capa 2 con
cardinalidad multiplicativa (CHAPTER_BRIEF, SCENE_NECESSITY,
SCENE_SHAPE): instancia única por archivo con crecimiento
interno mediante anclas (## CAPÍTULO N para CHAPTER_BRIEF;
## CAPÍTULO N — ESCENA X para SCENE_NECESSITY y SCENE_SHAPE).
La trazabilidad de los pasos canónicos de OP A se preserva en
las anclas; la auditoría de OP D opera sobre archivo
consolidado. (b) Declarar criterio de granularidad según escala
declarada en SCALE_CALIBRATION: cuento y novela corta toleran
consolidación total; novela media puede consolidar; novela larga
y saga multivolumen consolidan por libro (un CHAPTER_BRIEF por
libro, un SCENE_NECESSITY por libro, un SCENE_SHAPE por libro)
para mantener archivos manejables. (c) Añadir nota breve en las
tres plantillas declarando que el nombre del .md refiere al
archivo teórico en estado puro, y que en el proyecto creativo
las unidades (capítulos, escenas) viven como secciones internas,
no como archivos separados. (d) Añadir a SYSTEM_ORCHESTRATION OP
0.5 y OP A precisión operativa: "completar CHAPTER_BRIEF /
SCENE_NECESSITY / SCENE_SHAPE" se entiende como "abrir el
archivo y añadir sección con ancla de la unidad correspondiente".
(e) Las plantillas restantes de cardinalidad N (CHARACTER_PHYSICS,
RELATIONSHIP_PHYSICS, VOICE_ARCHITECTURE) mantienen instanciación
archivo-por-entidad, dado que su conteo está acotado por escala
y no produce inflación. La distinción cardinalidad acotada vs
multiplicativa se documenta explícitamente en
MODELO_AGNOSTICO_v7_APERTURA sección de política de instanciación.

---

REGISTRO 003 — 2026-10-23

Campo 1 — Identificador: 003 / Captura 2026-10-23.

Campo 2 — Síntoma observado: La primera obra del modelo,
diseñada con la v1.3, se leía como «80 % novela negra y 20 %
romance». Diseño del libro 1: 39 % de pareja; los doce primeros
capítulos, 26 %; los dos protagonistas en escena en 9 de 47
capítulos. El único capítulo de ella con él puntuó por encima
de todos los suyos sin él, con las mismas reglas de prosa.

Campo 3 — Diagnóstico del modelo: Nacido de un modelo de
intriga, el modelo conservaba sus adendas (AGATHA_ROSA) en
muchas plantillas y daba a la pareja más de una docena de
techos y ningún suelo. Nueve lecturas sin contexto situaron la
causa en el diseño (biblia, preset, escaleta), no en la prosa.
Situación 5 del protocolo.

Campo 4 — Patrón general implícito: Un modelo derivado de otro
de género distinto hereda sus proporciones. Si la trama que
define el género nuevo solo tiene techos, el diseño la deja por
debajo de lo prometido y la prosa no lo compensa: necesita un
suelo medible por capítulo, por bloque y por libro, aplicado al
diseñar y comprobado tras el borrador, nunca como consigna de
escritura.

Campo 5 — Implicación para v7: (a) Al derivar un modelo,
retirar las adendas del modelo de origen en vez de apilarlas.
(b) Un archivo rector con la trama A del género, su medida y
sus suelos. (c) Que las lecturas digan qué parte del libro es
trama A.

Marca de procesamiento: procesado en la v2.0 del
MODELO_DarkRomance (22–23-10-2026); motivó PAREJA_PRIMERO.md.
