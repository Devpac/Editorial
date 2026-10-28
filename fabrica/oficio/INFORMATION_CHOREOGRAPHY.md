<!-- Fábrica v3.0 — INFORMATION_CHOREOGRAPHY: base de oficio + adenda de dark romance (v2.0) -->

# INFORMATION_CHOREOGRAPHY.md

## PROPÓSITO

Este archivo diseña cómo el lector accede a la fábula.
No es lo mismo que CONTINUITY_PHYSICS registro 6 (quién sabe qué):
aquél registra el estado actual; éste diseña la trayectoria.

Sin coreografía de información, la novela revela demasiado
pronto (mata la tensión), demasiado tarde (el lector no tiene
anclaje), o en orden equivocado (el efecto emocional se
desmonta). Los LLM fallan específicamente aquí: tienden a
explicar todo lo que saben en cuanto se menciona.

JERARQUÍA: Capa 1.5 (entre NARRATIVE_CHRONOLOGY y STORY_SPINE).
Es prospectiva: diseña antes de escribir.
CONTINUITY_PHYSICS registro 6 es retrospectiva: registra lo
que ya ocurrió.

---

## UNIDAD DE INFORMACIÓN

La unidad mínima es el HECHO: una afirmación que puede ser
verdadera o falsa en el mundo, y que modifica la comprensión
del lector si la conoce.

Ejemplos:
- "A mintió a B sobre X."
- "C es responsable del incidente Y."
- "D y E fueron amantes hace diez años."
- "El sistema Z funciona mediante el mecanismo W."

NO es hecho:
- "A se siente culpable" (estado interno, no hecho comunicable).
- "La escena transcurre al amanecer" (marco escénico).

Los hechos se identifican con ID y se trazan a lo largo de la
novela.

---

## TIPOS DE REVELACIÓN

La misma información puede entregarse de muchas formas. La
elección afecta el peso dramático.

### DIRECTA
Un personaje (o el narrador) afirma el hecho.
"Fue él quien firmó el documento."
Peso: bajo-medio. Útil para establecer plataforma.

### OBLICUA
El hecho se infiere de un gesto, omisión o detalle periférico.
El texto no lo afirma; el lector lo deduce.
Peso: medio-alto. El lector que deduce queda comprometido.

### POR CONTRADICCIÓN
Dos afirmaciones incompatibles, sin que el texto resuelva cuál
es cierta.
Peso: variable. Genera sospecha, funciona bien con
narradores no fiables.

### POR OMISIÓN SISTEMÁTICA
El hecho nunca se afirma, pero la sintaxis lo señala: el
personaje evita mencionar algo tantas veces que la evitación
se vuelve presencia.
Peso: muy alto cuando funciona.
Riesgo: el lector no percibe la omisión y el hecho queda mudo.

### RETROSPECTIVA
El hecho se afirma tarde, reconfigurando lo anterior.
Peso: alto pero sólo una vez por hecho. Irreversible.

### POR CONFIRMACIÓN
Lo que el lector sospechaba se confirma. No añade información:
cristaliza.
Peso: medio. Útil al cierre de arcos.

### POR DESMENTIDO
Lo que el lector creía cierto se demuestra falso.
Peso: alto. Riesgo: si se usa más de una vez, el lector deja
de creer en nada.

---

## CADENCIA DE REVELACIÓN

Un hecho importante rara vez se revela en un solo momento.
Suele tener trayectoria.

### TRAYECTORIA ESTÁNDAR DE UN HECHO PESADO
1. SIEMBRA: una mención periférica que el lector registra sin
   subrayar.
2. ECO: una segunda aparición que sugiere conexión con lo
   anterior.
3. SOSPECHA: el lector empieza a formular la hipótesis.
4. CONFIRMACIÓN O DESMENTIDO: el hecho se resuelve (o se
   reabre).
5. CONSECUENCIA: lo que cambia en el relato ahora que se sabe.

No todos los hechos requieren todas las fases. Los hechos
menores pueden ir directamente a confirmación. Los pesados
necesitan las cinco.

### ERRORES DE CADENCIA
- Siembra ausente: la revelación aparece sin preparación.
  Sensación de deus ex machina.
- Siembra sin eco: el lector olvida. La revelación no resuena.
- Demasiadas siembras sin confirmación: el lector se agota
  sospechando.
- Confirmación sin consecuencia: la revelación no cambia nada.
  Fue ornamental.

---

## ASIMETRÍAS DE INFORMACIÓN

En cada momento del relato, el sistema debe declarar, para cada
hecho activo:

- ¿Quiénes entre los personajes lo conocen?
- ¿Desde cuándo?
- ¿Con qué grado de certeza (saber / intuir / sospechar)?
- ¿Lo conoce el lector?
- ¿Con qué grado de certeza?

Las posibles configuraciones generan efectos dramáticos
distintos:

### LECTOR SABE — PERSONAJE NO SABE
Ironía dramática. El lector mira al personaje avanzar hacia lo
que el lector ya teme o prevé.

### PERSONAJE SABE — LECTOR NO SABE
Misterio. El lector acompaña al personaje que oculta algo.
Requiere narración externa o POV que permita ocultamiento.

### AMBOS SABEN — OTRO PERSONAJE NO SABE
Complicidad silenciosa entre narrador/POV y lector frente al
tercero. Ver DIALOGUE_MECHANICS: el subtexto opera sobre este
triángulo.

### NADIE SABE
El mundo guarda el secreto incluso del narrador. Raro, alto
impacto si se usa bien.

---

## CALENDARIO MAESTRO DE INFORMACIÓN

Tabla prospectiva que se elabora en diseño y se audita en
ejecución.

| Hecho | Siembra | Eco(s) | Sospecha formable | Confirmación / Desmentido | Consecuencia |
|-------|---------|--------|-------------------|---------------------------|--------------|
| H-01  | Cap. 2  | Cap. 6, 11 | Cap. 14         | Cap. 19 (confirmación)    | Cap. 20-22   |
| H-02  | Cap. 4  | —      | —                 | Cap. 32 (desmentido)     | Cap. 33      |

### DENSIDAD POR CAPÍTULO
Cuántos hechos están activos simultáneamente (en fase de
siembra, eco o sospecha) en un capítulo dado.

Rango sano variable por escala (cruzar con SCALE_CALIBRATION):
- Novela corta: 2-4 hechos activos simultáneos.
- Novela media: 4-8.
- Novela larga: 6-12.

Por encima: saturación informativa, el lector pierde el hilo.
Por debajo: vacío, el lector no tiene materia con la que
pensar.

---

## RELACIÓN CON LA PREGUNTA CENTRAL

No todos los hechos tienen igual rango. Los hechos que
presionan directamente la pregunta central (THEMATIC_ENGINE)
son de RANGO TEMÁTICO; los demás son de RANGO DE TRAMA.

Un hecho de rango temático mal coreografiado daña la novela en
su eje principal. Un hecho de trama mal coreografiado produce
molestias locales.

Priorizar el diseño de los hechos de rango temático.

---

## HECHOS DE RANGO DE MUNDO

Sección aplicable solo si WORLD_ARC.md está activo en el
proyecto.

Cuando el proyecto declara arco de mundo de serie, aparece un
tercer rango de hechos paralelo a los de rango temático y los
de rango de trama: los HECHOS DE RANGO DE MUNDO. Son hechos
cuyo contenido se inscribe en algún eje del arco de mundo
declarado en WORLD_ARC.md, y cuya revelación al lector forma
parte de la trayectoria del arco a lo largo de la saga.

### EJEMPLOS DE HECHOS DE RANGO DE MUNDO

- "La institución X ha cambiado de orientación entre libro 2 y
  libro 3."
- "El equilibrio político entre las facciones A y B se ha
  desplazado durante una elipsis larga."
- "El mercado del bien Z ha colapsado por causas sistémicas
  que ningún POV presenció directamente."
- "La cosmovisión dominante en la región se ha transformado
  como consecuencia acumulada de eventos previos."

Los hechos de rango de mundo no son hechos sobre personajes
individuales; son hechos sobre la trayectoria del mundo. Su
unidad operativa es la misma (afirmación que puede ser
verdadera o falsa, modifica la comprensión del lector si la
conoce) pero su rango pertenece al arco de mundo.

### CADENCIA ESPECÍFICA

Los hechos de rango de mundo siguen la trayectoria estándar
de cinco fases (siembra, eco, sospecha, confirmación o
desmentido, consecuencia) pero con tres particularidades:

**Distribución multilibro.** Mientras los hechos de rango
temático y de trama suelen completar trayectoria dentro de un
libro, los hechos de rango de mundo pueden distribuir las
cinco fases entre libros distintos. Una siembra en libro 1
puede tener su confirmación en libro 4. La distribución se
declara en el calendario maestro extendido (ver más abajo).

**Filtrado por POV.** Los hechos de rango de mundo solo
llegan al lector a través de POVs específicos. Si el cruce
POV × eje es marginal o ausente (ver tabla en WORLD_ARC.md),
ese POV no puede portar hechos de rango de mundo de ese eje.
La selección de POV portador es decisión de diseño que
condiciona la cadencia.

**Sometimiento a principios de neutralización.** Si
THEMATIC_ENGINE.md declara principios de neutralización
aplicables al arco de mundo (subordinación a la pregunta
central), los hechos de rango de mundo se diseñan con
respeto a esos principios. Un hecho que demostrara
empíricamente uno de los polos de la pregunta es hecho mal
diseñado y debe replantearse.

### CALENDARIO MAESTRO EXTENDIDO

Cuando WORLD_ARC está activo, la tabla del CALENDARIO
MAESTRO DE INFORMACIÓN incluye una columna adicional o
duplica filas para hechos de rango de mundo:

| Hecho | Rango | Eje (si mundo) | Siembra | Eco(s) | Sospecha | Confirmación | Consecuencia |
|-------|-------|----------------|---------|--------|----------|--------------|--------------|
| H-01  | temático | —          | L1c2    | L1c6   | L1c14    | L1c19        | L1c20        |
| H-15  | mundo    | institucional | L1c4   | L2c3   | L2c11    | L3c8         | L3c9-12      |

### DENSIDAD POR CAPÍTULO INCLUYENDO HECHOS DE MUNDO

Cuando el calendario incluye hechos de rango de mundo, la
densidad por capítulo se cuenta sumando hechos activos de
los tres rangos. Los rangos sanos declarados en CADENCIA DE
REVELACIÓN no se modifican por la presencia de hechos de
mundo: el lector tiene la misma capacidad de procesamiento.
Si la densidad combinada excede el rango sano, los hechos de
mundo de eje secundario o estructural-subterráneo pueden
desplazarse a libro siguiente sin daño estructural, pero los
de eje principal compiten en igualdad con hechos de rango
temático y de trama.

### PRIORIZACIÓN COMBINADA

Cuando el presupuesto de presencia narrativa por capítulo es
limitado (ver SCALE_CALIBRATION.md y WORLD_ARC.md sección
RIESGOS):

1. Hechos de rango temático: máxima prioridad.
2. Hechos de rango de mundo de eje principal o de cruce
   principal con el POV del capítulo: alta prioridad.
3. Hechos de rango de trama mayores: prioridad media-alta.
4. Hechos de rango de mundo de eje secundario o
   estructural-subterráneo: prioridad media.
5. Hechos de rango de trama menores: prioridad baja.

La regla operativa: si hay que sacrificar un hecho del
calendario por densidad, se sacrifica de los rangos
inferiores hacia arriba.

---

## INFORMACIÓN Y SUBTEXTO

Lo que el lector infiere (vía SUBTEXT_MECHANICS) cuenta como
información adquirida. Si la coreografía prevé que el lector
sospeche algo en cap. X, los mecanismos de subtexto deben
estar activados a partir de cap. X−1.

Cruce operativo: cada hecho en el calendario indica, si
procede, los mecanismos de subtexto que lo están construyendo.

---

## IRONÍA DRAMÁTICA

La sección ASIMETRÍAS DE INFORMACIÓN trata la ironía dramática
como una de las configuraciones posibles (lector sabe —
personaje no sabe). Esta sección formaliza el mecanismo: lo
que en aquella sección aparece como configuración de hecho
puntual, aquí se trata como decisión coreográfica que el
diseño puede activar conscientemente y que merece su propia
declaración en el calendario.

La distinción operativa: la asimetría de información es
estado registrado del sistema en un momento dado; la ironía
dramática es uso productivo de esa asimetría como mecanismo
de presión sobre el lector. No toda asimetría es ironía
dramática. Hay asimetría siempre que un personaje ignore lo
que otro o el lector saben; hay ironía dramática solo cuando
esa asimetría está dispuesta para que el lector experimente
tensión, simpatía, distancia crítica o anticipación específica
hacia el personaje desinformado.

### TRES MODOS DE IRONÍA DRAMÁTICA

**EMERGENTE.** La asimetría surge naturalmente del juego de
POVs y revelaciones declarado en el calendario maestro. El
lector accede a información a través de un POV que otros
personajes no tienen, y el efecto de ironía aparece como
subproducto de la coreografía general. No es decisión sobre
escena puntual; es consecuencia del diseño multi-POV.

Función dramática: sostiene tensión continua de fondo. Cada
escena con personaje desinformado puede leerse a través de la
asimetría sin que la escena tenga que orquestarla
explícitamente.

Criterio de uso: aplicable en cualquier proyecto multi-POV
con cadencia diferenciada de revelación. No requiere
declaración escena por escena; se declara una vez en el
diseño general.

Riesgo específico: la ironía emergente puede saturar el
manuscrito si el calendario produce demasiados hechos donde
el lector queda informado por delante de los personajes. El
lector cansado de saber-más-que-los-personajes deja de
implicarse.

**ACTIVA.** Decisión consciente de estructurar escena
específica para que el lector sepa algo que el personaje en
escena no sabe. Mecanismo: revelación previa al lector por
capítulo paralelo, por POV alterno, o por intervención
narratorial; seguida de escena del personaje no informado
cuyo comportamiento gana significación por la asimetría.

Función dramática: concentra el efecto en escena específica
con propósito declarado (tensión por espera de descubrimiento,
simpatía hacia el personaje vulnerable, distancia crítica
hacia el personaje que actúa con información incompleta).

Criterio de uso: aplicable cuando una escena necesita
cargarse con peso adicional que la propia escena no puede
generar internamente. Si la escena ya carga peso por su
materia interna, la ironía dramática activa puede ser
redundante.

Riesgo específico: la inscripción explícita en el calendario
es obligatoria. Una ironía dramática activa improvisada en
ejecución sin declaración previa produce escena que el lector
no termina de procesar (no llega a saber lo que tendría que
saber para que la asimetría funcione).

**INVERTIDA.** El lector está deliberadamente menos informado
que un personaje. La asimetría es a favor del personaje. El
lector descubre después que el personaje sabía algo que el
texto no le dijo. Recurso menos frecuente pero productivo en
novela negra, thriller con narrador no fiable, novela de
revelación tardía.

Función dramática: produce relectura retroactiva del
comportamiento del personaje. Pasajes que parecían transparentes
se revelan opacos; gestos que parecían inocuos se revelan
cargados.

Criterio de uso: aplicable cuando el efecto principal del
libro depende de relectura final. La ironía invertida tiene
costo: requiere que el texto sostenga ambigüedad sin marcarla
demasiado (se delataría) ni demasiado poco (la revelación
posterior caería sin resonancia).

Riesgo específico: si el personaje sabía algo que se omitió
sin justificación interna, el lector puede sentir manipulación
narratorial. La ocultación debe ser legítima desde el POV
escogido (un personaje puede no contarse a sí mismo lo que
sabe; un narrador omnisciente no puede omitir sin razón
declarada).

### COORDINACIÓN CON OTROS ARCHIVOS

**Cruce con CHARACTER_PHYSICS.** La asimetría de información
modula la presión sobre el personaje no informado. La sección
TIPOS DE ANTAGONISMO puede iluminar la lectura: el personaje
desinformado frente a antagonista circunstancial vive la
asimetría como vulnerabilidad estructural; frente a antagonista
individual la vive como desventaja táctica; frente a sociedad
como antagonista la vive como ceguera sistémica. Cada lectura
condiciona el efecto de la ironía dramática.

**Cruce con TENSION_MECHANICS.** El archivo declara la ironía
dramática como uno de los mecanismos del repertorio de tensión.
La declaración aquí no la duplica: la formaliza como decisión
de coreografía de información, mientras TENSION_MECHANICS la
trata como mecanismo de presión sobre la escena. Operativamente:
la ironía dramática se diseña aquí (calendario, modo, función)
y se ejecuta en escena con los recursos que TENSION_MECHANICS
documenta.

**Cruce con SCENE_NECESSITY.** La escena que opera por
ironía dramática puede tener doble criterio de necesidad. La
necesidad de la escena en sí (¿qué hace avanzar?) sigue siendo
condición primaria. La necesidad de que el lector acceda a la
información antes (¿por qué la escena previa que informa al
lector tiene que ocurrir antes que esta?) es condición
adicional. Si la información previa es prescindible para el
arco, la ironía dramática activa basada en ella es ornamental.

### TEST DE IRONÍA DRAMÁTICA

Para cada escena con asimetría declarada de información,
verificar:

- ¿La asimetría está declarada en el calendario maestro como
  parte de la trayectoria del hecho involucrado?
- ¿El modo (emergente, activa, invertida) está identificado
  en el diseño?
- ¿El efecto sobre el lector es el previsto (tensión, simpatía,
  distancia crítica, anticipación), no efecto accidental
  distinto?
- Si activa: ¿la escena previa que informa al lector está
  inscrita en el calendario con cadencia previsible, no
  improvisada?
- Si invertida: ¿la ocultación es legítima desde el POV
  escogido?

Una escena que falla cualquier verificación se ajusta: o bien
se declara la asimetría retroactivamente en el calendario, o
bien se elimina la asimetría improvisada que no funciona, o
bien se rediseña la cadencia para que la ironía dramática
opere como diseñada.

---

## PROTOCOLO DE DISEÑO

Antes de empezar el libro:

1. Listar todos los hechos pesados del proyecto (los que
   presionan la pregunta central y los pivotes de trama).
2. Asignar ID a cada uno.
3. Diseñar trayectoria de cinco fases (o menos, justificadas)
   para cada uno.
4. Distribuir en calendario por capítulos.
5. Verificar densidad por capítulo.
6. Cruzar con STORY_SPINE: los momentos estructurales mayores
   deben coincidir con consecuencias de hechos pesados.

Durante la escritura:

- En CHAPTER_BRIEF, declarar qué hechos están en qué fase.
- En OPERACIÓN C, actualizar el calendario (pueden aparecer
  ajustes).
- En OPERACIÓN D, auditar: ¿la cadencia real coincide con la
  diseñada? Si no, o se ajusta el diseño o se corrige la
  ejecución.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — TRAZABILIDAD DE SIEMBRA
Para cada hecho revelado, ¿hay siembra previa registrada?
Si un hecho aparece sin siembra, es agujero o deus ex machina.

TEST 2 — ECONOMÍA DE SIEMBRAS
¿Hay siembras que nunca se recogen? Son ruido informativo.
Eliminar o convertir en hecho real.

TEST 3 — CADENCIA POR HECHO PESADO
Cada hecho de rango temático: ¿tiene trayectoria de cinco
fases (o justificación para saltarse alguna)?

TEST 4 — DENSIDAD POR CAPÍTULO
¿Algún capítulo tiene demasiados hechos activos? ¿Alguno tiene
pocos? Revisar.

TEST 5 — ASIMETRÍAS CONSISTENTES
Un personaje no puede actuar usando información que aún no
tiene registrada. Verificar con CONTINUITY_PHYSICS registro 6.

---

## ERRORES COMUNES

ERROR 1 — REVELACIÓN ANTICIPADA
El LLM explica al lector lo que aún no debería saber porque
"tiene sentido narrativo explicarlo". Romper el hábito.

ERROR 2 — SIEMBRA INVISIBLE
Se siembra en una subordinada perdida en un párrafo de textura.
El lector no registra. La confirmación posterior cae sin eco.
Solución: la siembra debe tener peso suficiente para quedarse,
sin tanto peso que parezca anuncio.

ERROR 3 — EQUIVALENCIA FALSA
Tratar hechos de rango distinto como si pesaran igual.
Los hechos temáticos dominan el calendario.

ERROR 4 — HECHOS HUÉRFANOS
Hechos que se revelan pero no generan consecuencia.
Eliminar o rediseñar para que la consecuencia exista.

---

## RELACIÓN CON OTROS ARCHIVOS

INFORMATION_CHOREOGRAPHY.md recibe de:
- NARRATIVE_CHRONOLOGY.md (qué hechos existen en la fábula)
- THEMATIC_ENGINE.md (qué hechos son de rango temático)
- STORY_SPINE.md (dónde caen las consecuencias mayores)
- WORLD_ARC.md (cuando está activo, qué hechos son de rango
  de mundo, qué eje los aloja, qué cruce POV × eje los hace
  legibles, qué principios de neutralización los condicionan)

INFORMATION_CHOREOGRAPHY.md alimenta:
- CHAPTER_BRIEF.md (eje informativo: qué revela el capítulo)
- SCENE_NECESSITY.md (pregunta 3: qué deja sin resolver)
- SUBTEXT_MECHANICS.md (qué se prepara para inferencia)
- CONTINUITY_PHYSICS.md (registro 6, retrospectivo)
- WORLD_ARC.md (cuando está activo, devuelve el calendario
  de revelación de los hechos de rango de mundo, para que la
  auditoría conjunta verifique coherencia entre arco
  declarado y trayectoria de revelación al lector)

INFORMATION_CHOREOGRAPHY.md se revisa:
- OPERACIÓN 0 (diseño inicial completo).
- OPERACIÓN D (auditoría de cadencia real vs. diseñada).

La sección IRONÍA DRAMÁTICA de este archivo introduce
coordinaciones específicas con archivos del catálogo donde la
asimetría de información se vuelve mecanismo productivo:
- TENSION_MECHANICS.md: la ironía dramática (modos emergente,
  activa e invertida) es fuente sostenida de tensión sobre el
  lector; las escenas donde opera se diseñan respetando los
  marcadores de tensión declarados allí.
- VOICE_ARCHITECTURE.md: el POV escogido determina qué
  información ve el lector; la ironía dramática invertida
  exige que la ocultación sea legítima desde el POV declarado
  en este archivo.
- SCENE_NECESSITY.md: las escenas que activan ironía dramática
  (especialmente en modo activo) se justifican respondiendo a
  las preguntas declaradas allí, evitando que la ironía
  funcione como ornamento sin necesidad.
- CHAPTER_BRIEF.md: declaración por capítulo de qué asimetrías
  están activas y qué efecto sobre el lector se persigue,
  según el calendario maestro.
- SUBTEXT_MECHANICS.md: la asimetría que produce ironía
  dramática es una fuente característica de subtexto,
  especialmente cuando el personaje desinformado dice o hace
  algo cuyo significado real solo el lector capta.
- CHARACTER_PHYSICS.md: el efecto de la ironía dramática
  (tensión, simpatía, distancia crítica, anticipación) opera
  sobre el personaje desinformado y modula la lectura de su
  herida, mecanismo de defensa y arco.


---
---

