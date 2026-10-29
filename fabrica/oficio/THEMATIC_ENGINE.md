<!-- Fábrica — THEMATIC_ENGINE: base de oficio + adenda de dark romance (v2.0) -->

# THEMATIC_ENGINE.md

## PROPÓSITO

Este archivo sostiene la tensión que hace que la novela sea
*esta* novela y no otra. Sin una pregunta central activa,
los capítulos son episodios y los arcos son trayectorias sin sentido
acumulativo.

JERARQUÍA: Capa 1. Tiene precedencia sobre toda la arquitectura
excepto sobre sí mismo (si la pregunta está mal formulada,
la novela no se arregla en capas inferiores) y sobre
SERIES_ARCHITECTURE (si el proyecto es multivolumen, la
pregunta del libro se inscribe en la pregunta de la serie).

---

## PREGUNTA CENTRAL

Formulación: ¿[pregunta que no admite respuesta simple]?

REQUISITOS DE UNA PREGUNTA CENTRAL VÁLIDA:
- No tiene una respuesta correcta evidente.
- Admite defensa razonada por ambos lados.
- No es un dilema moral de manual (bien vs. mal, libertad vs. seguridad
  tomado al pie de la letra): exige una formulación que enrede los
  dos lados en el mismo cuerpo.
- Es formulable sin mencionar al protagonista: es una pregunta sobre
  el mundo, que el protagonista encarna.

EJEMPLO NAVAL:
¿Puede un hombre servir con honor a una causa cuya justicia
le resulta cada vez más dudosa, y qué queda de él si decide
que el servicio es la justicia?

EJEMPLO CONTRA-EJEMPLO (mal formulado):
"¿Vale la pena ser leal?" → dilema abstracto, sin cuerpo.
La buena formulación enraíza la pregunta en la economía específica
del mundo y del personaje.

---

## POLARIDADES EN TENSIÓN

Polo A: [un valor legítimo, nombrado con precisión]
Polo B: [un valor legítimo opuesto, nombrado con precisión]

Ninguno de los dos polos puede ser evidentemente incorrecto.
Si el lector puede decidir cuál es el bueno en el primer capítulo,
la tensión no existe.

EJEMPLO:
Polo A: La lealtad como identidad (sin ella no hay yo).
Polo B: La supervivencia como precondición de toda lealtad
(un muerto no es leal a nada).

---

## ENCARNACIÓN POR PERSONAJE

La pregunta central no la encarna solo el protagonista. Cada personaje
principal representa una respuesta distinta a la misma pregunta,
o una mutación de ella. Sin esto, los secundarios son función de
trama, no tesis viva.

PROTAGONISTA: [qué respuesta encarna, con qué coste]

ANTAGONISTA: [la misma pregunta, resuelta con el mecanismo opuesto.
Ver RELATIONSHIP_PHYSICS.md para la física especular.]

PERSONAJE-ESPEJO: [alguien que encarna la respuesta que el protagonista
teme o envidia]

PERSONAJE-DESVIACIÓN: [alguien que muestra que la pregunta es mal
formulada, o que hay un tercer camino que el protagonista no ve]

---

## EVOLUCIÓN DE LA PREGUNTA

La pregunta central no es estática. Si la novela termina con la misma
formulación con la que empezó, no ha ocurrido nada.

FORMULACIÓN INICIAL (Acto I): [la forma ingenua de la pregunta,
la que el protagonista cree que está respondiendo]

FORMULACIÓN MEDIA (Acto II): [la pregunta se ha revelado más difícil,
los términos se han complicado]

FORMULACIÓN FINAL (Acto III): [la pregunta definitiva, que puede ser
distinta a la inicial: la novela ha enseñado al protagonista —y al
lector— cuál era la verdadera pregunta todo el tiempo]

SI EL PROYECTO ES MULTIVOLUMEN:
La evolución dentro del libro es un subconjunto de la evolución
de serie declarada en SERIES_ARCHITECTURE.md. Verificar que la
formulación final de este libro es la formulación inicial del
siguiente.

---

## SUBORDINACIÓN DEL ARCO DE MUNDO

Sección aplicable solo si WORLD_ARC.md está activo en el
proyecto (cumplimiento de los tres criterios declarados en
ese archivo).

El arco de mundo se subordina a la pregunta central declarada
en este archivo. La subordinación no es jerarquía nominal:
es regla operativa que evita que la evolución del mundo
resuelva la pregunta central por vía macro. La pregunta debe
permanecer irresoluble; el arco de mundo no puede demostrar
empíricamente uno de los polos.

### POR QUÉ LA SUBORDINACIÓN ES OBLIGATORIA

Si la pregunta central pertenece a la agencia moral
individual y el arco de mundo demuestra empíricamente que un
polo prevalece (por ejemplo: el sistema institucional
demuestra que la lealtad siempre traiciona, o que la
supervivencia siempre justifica), la pregunta queda
respondida por el sistema y la novela pierde su
irresolubilidad. El motor temático colapsa porque la
respuesta se ha construido fuera del cuerpo de los
personajes.

La subordinación se ejecuta mediante principios de
neutralización que cada proyecto declara según naturaleza de
su pregunta central. Los principios se registran en
WORLD_ARC.md (sección INTERACCIÓN CON LA PREGUNTA TEMÁTICA)
pero su raíz pertenece a este archivo.

### PRINCIPIOS DE NEUTRALIZACIÓN

Los principios son reglas operativas que filtran cómo el
arco de mundo puede entrar en escena sin resolver la
pregunta. Los siguientes son tipos posibles, no exhaustivos:

**Principio de no-articulación.** Ciertos patrones del arco
de mundo no se articulan jamás por personajes ni narrador.
El lector los percibe pero ningún cuerpo del proyecto los
nombra. La articulación los convertiría en tesis demostrada
y vaciaría la pregunta.

**Principio de evidencia ambigua.** El arco de mundo aporta
datos que pueden leerse en favor de cualquiera de los polos.
La ambigüedad es deliberada y se audita capítulo a capítulo
para que el sesgo no incline la balanza.

**Principio de asimetría temporal.** Los efectos del arco de
mundo sobre los personajes operan con desfase respecto a la
manifestación del eje, de modo que el lector no asocia causa
sistémica con consecuencia individual.

**Principio de filtro POV.** Los eventos de mundo se
presentan a través de un POV cuya posición respecto a la
pregunta central no permite extraer conclusión sistémica
limpia.

**Principio de neutralización por ciclo.** Si la forma
dramática del arco de mundo es ciclo con variación, la
reproducción funcional impide que la pregunta se resuelva
direccionalmente: el mundo cambia de forma sin cambiar de
sustancia, y la pregunta sigue abierta porque su contexto no
se ha movido.

Cada proyecto declara los principios que aplica. La
declaración es operativa: cada principio debe poder
auditarse capítulo a capítulo.

### TEST DE SUBORDINACIÓN

Auditoría binaria al cierre del último libro: ¿el lector
razonable concluye que la pregunta central tiene respuesta
porque el mundo demostró X o Y? Si la respuesta es sí, el
arco de mundo ha fallado en subordinarse a la pregunta.

Este test se ejecuta en OPERACIÓN D y en PASADA 1 de
REVISION_PROTOCOL. Su raíz está aquí porque la pregunta
central pertenece a este archivo; su mecánica operativa se
detalla en WORLD_ARC.md.

---

## MOTIVOS RECURRENTES

Objetos, imágenes, lugares o gestos que aparecen en puntos clave y
codifican la pregunta sin nombrarla. No son símbolos por decoración:
son el modo en que la pregunta se vuelve materia.

MOTIVO 1: [objeto/imagen/gesto] — qué codifica — reapariciones previstas
MOTIVO 2: ...
MOTIVO 3: ...

REGLA: Un motivo debe aparecer mínimo tres veces para funcionar.
La primera es establecimiento, la segunda es eco, la tercera es
cristalización. Menos es accidente, más es redundancia (salvo en
régimen barroco, ver AESTHETIC_REGISTER.md).

ANCLAJE EN FÁBULA:
Cada motivo debe tener un evento en NARRATIVE_CHRONOLOGY.md
donde aparece por primera vez. Un motivo sin anclaje cronológico
es adorno; con anclaje, opera.

EJEMPLO:
Motivo del reloj en una novela sobre lealtad:
1. Acto I: el protagonista recibe un reloj de su mentor.
2. Acto II: lo empeña en un momento de apuro, lo recupera mintiendo.
3. Acto III: lo destruye al descubrir que el mentor lo traicionó.
El reloj no se explica nunca: su trayectoria *es* la pregunta
sobre lealtad volviéndose materia.

### RESONANCIAS ENTRE EVENTOS DE MUNDO Y MOTIVOS

Subsección aplicable solo si WORLD_ARC.md está activo.

Cuando el proyecto tiene arco de mundo, los motivos pueden
resonar con eventos de mundo: la reaparición del motivo
coincide con manifestación del arco, o el motivo cambia de
significado en función de cómo ha evolucionado un eje del
mundo. Estas resonancias son material temático aprovechable
si se diseñan, peligro temático si quedan accidentales.

**Resonancia diseñada.** El motivo se ancla deliberadamente
en evento de mundo. Cada reaparición del motivo se vincula a
fase del arco de mundo en libro N. La resonancia carga al
motivo con contenido que excede al personaje portador y lo
conecta con la pregunta central por vía sistémica sin
resolverla (ver SUBORDINACIÓN DEL ARCO DE MUNDO más arriba).

**Resonancia accidental.** El motivo aparece en momento que
coincide con evento de mundo sin diseño previo. La
coincidencia produce lectura sistémica que el proyecto no ha
querido. Riesgo: el lector infiere que el mundo demuestra una
posición frente a la pregunta. Auditoría: cada reaparición
del motivo se verifica contra calendario del arco de mundo;
si la coincidencia produce lectura no querida, el motivo se
desplaza.

**Resonancia neutralizada.** El motivo aparece en momento
adyacente al evento de mundo pero el diseño aplica
principios de neutralización (ver SUBORDINACIÓN DEL ARCO DE
MUNDO) para que la coincidencia no produzca tesis. La
neutralización es decisión consciente cuando el motivo y el
arco de mundo no pueden separarse cronológicamente.

FORMATO DE DECLARACIÓN DE RESONANCIA:
MOTIVO [N] resuena con EJE DE MUNDO [eje]
- TIPO: diseñada / neutralizada
- LIBRO Y FASE DE RESONANCIA: [...]
- QUÉ APORTA LA RESONANCIA: contenido temático específico
  que excede al motivo solo y al eje solo
- AUDITORÍA: regla de verificación que confirma que la
  resonancia no resuelve la pregunta central por vía macro

La declaración explícita previene que las resonancias sean
accidentales (que producirían colisión temática con la
pregunta central) o se pierdan (lo cual desperdiciaría
material temático aprovechable).

---

## SISTEMA DE IMÁGENES

El motivo recurrente, declarado en la sección anterior, opera
por repetición codificando un valor temático: cada aparición
carga significación específica respecto a la pregunta central.
La función del motivo es semántica: el motivo dice algo. El
sistema de imágenes es operación distinta que también opera
por repetición pero con función propia: la repetición de un
campo visual o sensorial (agua, pájaros, luz, espejos,
ventanas, manos, frío, oxidación, vegetación, polvo, hierro,
piedra, cristal) sin que el campo codifique necesariamente
tema. La función es atmosférica y musical: el campo sostiene
un tono, una textura, una respiración del libro.

Esta distinción es importante porque ambas operaciones se
confunden con facilidad y producen problemas distintos cuando
se mezclan: un sistema de imágenes que pretende cargar tema
sin trabajar la cristalización del motivo queda como
insistencia decorativa; un motivo que se trata como sistema
de imágenes (sin tres apariciones cargadas) pierde su
capacidad codificadora. La novela puede sostener motivos y
sistema de imágenes en paralelo; debe declarar cada uno por
separado y respetar sus mecánicas respectivas.

### NATURALEZA DEL SISTEMA DE IMÁGENES

El sistema de imágenes es campo visual o sensorial que el
libro sostiene a lo largo de su extensión sin obligación
temática. Los referentes pueden cargar significación si
convergen con un motivo en clímax o cierre, pero la
significación no es la función primaria: la función primaria
es coherencia sensorial del mundo que la novela construye.

Una novela ambientada en archipiélago puede sostener sistema
de imágenes "agua" sin que el agua sea motivo: el agua está
porque la novela transcurre cerca del mar y la prosa registra
esa cercanía con repetición consciente. Una novela urbana
puede sostener sistema de imágenes "luz artificial" por
analogía: el campo construye atmósfera sin afirmar tesis. El
sistema de imágenes opera, en muchas novelas, por debajo del
nivel de conciencia explícita del lector: se siente como
unidad atmosférica del libro sin nombrarse.

### CAMPOS A DECLARAR

CAMPO 1: [nombre del campo] — densidad — distribución —
convergencia con motivo si la hay
CAMPO 2: ...
CAMPO 3: ...

REGLA: una novela puede sostener entre uno y cuatro campos de
imagen activos. Más de cuatro produce saturación sensorial
sin coherencia perceptible (los campos compiten entre sí y
ninguno se establece). Menos de uno significa que la novela
no trabaja el sistema sensorial de modo consciente; esto es
opción legítima en regímenes minimalistas o periodísticos
donde la concreción del detalle individual sustituye la
construcción de campo.

### DENSIDAD POR CAPÍTULO

Para cada campo de imagen activo, declarar densidad
operativa: cuántas apariciones del campo se esperan en rango
de capítulos. La densidad puede ser homogénea (el campo
aparece a frecuencia similar a lo largo del libro) o variable
(el campo se concentra en bloques específicos).

FORMATO:
CAMPO [nombre]
- Densidad media: [N apariciones por capítulo]
- Densidad mínima: [umbral por debajo del cual el campo se
  pierde como sistema y se vuelve aparición aislada]
- Densidad máxima: [techo por encima del cual el campo se
  vuelve insistencia perceptible y empieza a leerse como
  motivo declarado, contaminando su función atmosférica]

La densidad media depende del régimen estético: regímenes
expansivos y barrocos toleran densidad alta (cada capítulo
con varias apariciones por campo); regímenes minimalistas y
popular-eficientes operan con densidad baja (apariciones
distribuidas, no acumuladas). Cruce con AESTHETIC_REGISTER.md.

### DISTRIBUCIÓN

Declarar para cada campo si su presencia es:
- HOMOGÉNEA: aparece a lo largo de todo el libro con densidad
  similar.
- POR BLOQUES: aparece concentrado en secciones específicas
  (campo "frío" presente solo en bloque invernal, campo
  "agua" presente solo cerca del mar) y ausente en otras.
- ASCENDENTE: la densidad crece a medida que el libro avanza,
  cargando intensidad atmosférica hacia el clímax.
- DESCENDENTE: la densidad decrece, sugiriendo retirada del
  campo en favor de otro o en favor de aire seco.
- CICLO: el campo aparece y desaparece en patrón regular,
  generando ritmo perceptible.

La distribución por bloques es la más frecuente cuando los
campos están vinculados a localizaciones o épocas; la
homogénea es la más frecuente cuando el campo construye
atmósfera global del libro.

### CONVERGENCIA CON MOTIVO

Un sistema de imágenes puede o no terminar codificando tema.
Si en algún punto del libro un campo de imagen se carga
temáticamente (la primera aparición acumulada del campo en
escena con función dramática alta), el campo converge con
motivo: a partir de ese punto deja de operar solo
atmosféricamente y empieza a operar también semánticamente.

Casos posibles:
- CONVERGENCIA TEMPRANA. El campo se carga temáticamente en
  Acto I; el resto del libro lo trata como motivo declarado.
  Riesgo: la novela pierde el campo atmosférico y lo
  reemplaza por motivo, empobreciendo la respiración del
  libro.
- CONVERGENCIA TARDÍA. El campo opera atmosféricamente
  durante la mayor parte del libro y se carga semánticamente
  en clímax o cierre. Esta es la convergencia más
  productiva: la lectura final reorganiza retroactivamente el
  campo y descubre que llevaba significación latente.
- CONVERGENCIA NULA. El campo nunca se carga temáticamente.
  Opera siempre atmosféricamente. Es opción legítima si el
  libro tiene varios campos y la coherencia sensorial es
  valor en sí mismo.
- CONVERGENCIA ACCIDENTAL. El campo se carga temáticamente
  sin diseño previo, en una escena donde la prosa lo presenta
  con peso dramático que el resto del libro no sostiene.
  Riesgo: el lector infiere significación que la novela no ha
  construido. Auditoría: verificar densidad y distribución.

FORMATO DE DECLARACIÓN DE CONVERGENCIA:
CAMPO [nombre] converge con MOTIVO [N]
- TIPO: temprana / tardía / nula / accidental detectada
- PUNTO DE CONVERGENCIA: [capítulo, escena]
- QUÉ APORTA LA CONVERGENCIA: contenido temático que el
  campo solo y el motivo solo no aportarían

### COORDINACIÓN CON RESONANCIAS DE MUNDO

Subsección aplicable solo si WORLD_ARC.md está activo.

El sistema de imágenes puede entrar en resonancia con eventos
de mundo del mismo modo que el motivo (ver subsección
RESONANCIAS ENTRE EVENTOS DE MUNDO Y MOTIVOS, arriba). La
diferencia operativa: la resonancia del campo con eje de
mundo es más sutil que la del motivo, porque el campo no
afirma tesis. Aun así, una novela con arco de mundo puede
diseñar campos de imagen que evolucionen en paralelo a ejes
del mundo: campo "oxidación" que crece con eje sistémico de
deterioro, campo "luz fría" que se asocia con eje de
institucionalización, campo "vegetación" que se asocia con
eje de regeneración o pérdida según la dirección del eje.

La declaración de coordinación opera con el formato de
RESONANCIA pero sin tipo "diseñada / neutralizada" (el campo
de imagen no afirma; resuena de modo sostenido) sino con tipo
"asociado / contrapunto":
- ASOCIADO: el campo evoluciona en la misma dirección que el
  eje. El crecimiento del campo refuerza la lectura
  atmosférica del eje.
- CONTRAPUNTO: el campo evoluciona en dirección opuesta a la
  del eje. El campo entra en tensión con el eje y produce
  textura sensorial divergente del movimiento sistémico.

Cualquier coordinación campo × eje se audita contra la
SUBORDINACIÓN DEL ARCO DE MUNDO declarada arriba: el campo no
puede demostrar empíricamente uno de los polos de la pregunta
central. Si el campo asociado al eje produce sensación de
tesis sistémica, hay riesgo de resolución de la pregunta por
vía sensorial; aplicar principios de neutralización.

### COORDINACIÓN CON SENSORY_HIERARCHY.md

El sistema de imágenes opera sobre la dimensión sensorial del
libro y modula qué sentidos jerarquiza la novela. Una novela
con campo "luz" dominante jerarquiza la vista; una novela con
campo "frío" dominante jerarquiza la piel; una novela con
campo "voces" dominante jerarquiza el oído. La declaración
del campo aquí debe ser coherente con la jerarquía sensorial
declarada en SENSORY_HIERARCHY.md: si aquel archivo declara
que la novela jerarquiza tacto y este declara campo dominante
"luz", hay incoherencia que debe resolverse.

La autoridad sobre qué sentido jerarquiza la novela vive en
SENSORY_HIERARCHY.md; la autoridad sobre qué campos de imagen
sostienen esa jerarquía vive aquí. Los dos archivos se
auditan conjuntamente.

### COORDINACIÓN CON AESTHETIC_REGISTER.md

El régimen estético modula la tolerancia al sistema de
imágenes denso. Régimen minimalista: campo escaso, una o dos
apariciones por capítulo, distribución por bloques sin
convergencia explícita. Régimen expansivo: campo denso,
varias apariciones por capítulo, distribución variable,
convergencia tardía frecuente. Régimen barroco: campo
saturado, múltiples campos en paralelo, convergencia
ambigua. Régimen popular-eficiente: campo discreto, función
atmosférica subordinada al ritmo de trama, convergencia
preferentemente nula (la convergencia tardía exige relectura
y este régimen no la presupone).

La incoherencia entre régimen declarado en
AESTHETIC_REGISTER.md y densidad de sistema de imágenes
declarada aquí es error detectable en OPERACIÓN D.

### TESTS DE FUNCIONAMIENTO ESPECÍFICOS

Antes de cerrar capítulo o bloque, verificar:

- Que cada campo activo aparece dentro de su densidad
  declarada (ni por debajo del umbral mínimo ni por encima
  del techo que lo convertiría en motivo accidental).
- Que la distribución declarada se cumple en el bloque
  específico (un campo "homogéneo" que falta tres capítulos
  consecutivos no es homogéneo).
- Que los campos no compiten entre sí en el mismo párrafo o
  escena salvo que la competencia sea diseñada (escena de
  transición entre bloques con superposición de campos).
- Que la convergencia con motivo, si está declarada, ocurre
  donde se declaró y no antes (convergencia temprana
  accidental destruye convergencia tardía diseñada).

### RIESGO PRINCIPAL

El sistema de imágenes que el lector percibe como insistencia.
Si la repetición del campo se hace tan densa o tan poco
variada que el lector empieza a leerla como subraya, el campo
deja de operar atmosféricamente y se lee como autor que
insiste. La diferencia entre sistema de imágenes y subraya es
densidad calibrada, variación interna del campo (no las
mismas palabras cada vez: el campo "agua" puede aparecer como
mar, charco, lluvia, vapor, sed, sin repetir términos), y
ausencia de glosa narratorial sobre la presencia del campo.

Si el narrador comenta que "vuelve el agua", el campo se
quema: deja de ser sistema y se vuelve motivo accidentalmente
declarado, o peor, comentario autorial sobre la propia
escritura.

---

## INSTRUCCIÓN OPERATIVA

Antes de diseñar cualquier escena, preguntar:

1. ¿Esta escena añade presión a la tensión central o la ignora?
   Si la ignora, rediseñar o eliminar.

2. ¿Qué polaridad está activa en esta escena?
   A veces solo una. A veces ambas en colisión.
   Si ninguna, la escena es fuera de eje.

3. ¿Algún motivo recurrente reaparece aquí?
   Si sí, ¿en qué fase de su trayectoria?
   Si se está sobre-usando un motivo, redistribuir.

4. ¿Algún campo del sistema de imágenes opera en esta escena?
   Si sí, verificar que la densidad respeta lo declarado y
   que la variación interna del campo evita la insistencia.
   Si la escena debe ser punto de convergencia campo × motivo,
   verificar que el resto de la novela ha sostenido la
   atmósfera necesaria para que la convergencia funcione.

5. ¿El personaje está respondiendo a su formulación actual de la
   pregunta (inicial / media / final)?
   El desfase entre la formulación que él cree y la que la novela
   está construyendo es fuente dramática.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — RESUMEN INVERSO
¿Puedes resumir la novela sin mencionar la pregunta central?
Si sí, la pregunta no está funcionando como motor sino como adorno.

TEST 2 — ESCALABILIDAD
¿Cada acto aumenta la presión sobre la pregunta, o se repite
la misma intensidad?
Si se repite, la arquitectura está estancada.

TEST 3 — IRRESOLUBILIDAD
¿La respuesta que la novela propone cierra la pregunta o la
profundiza? Una pregunta central bien formulada no se resuelve:
se agota una versión de ella.

TEST 4 — COHERENCIA CON CADENCIA DE INFORMACIÓN
Los hechos de rango temático (los que presionan directamente la
pregunta central) deben tener cadencia prospectiva declarada en
INFORMATION_CHOREOGRAPHY.md. ¿La tienen? Si un hecho temático
no tiene calendario, su efecto será accidental.

---

## RELACIÓN CON OTROS ARCHIVOS

THEMATIC_ENGINE.md alimenta:
- STORY_SPINE.md (la estructura es la secuencia de presiones sobre esta pregunta)
- CHARACTER_PHYSICS.md (cada personaje encarna una respuesta)
- CHAPTER_BRIEF.md (el subtexto del capítulo conecta aquí)
- SCENE_NECESSITY.md (la primera pregunta de entrada es si la escena añade presión)
- INFORMATION_CHOREOGRAPHY.md (identifica hechos de rango temático)
- NARRATIVE_CHRONOLOGY.md (cada motivo se ancla en evento)
- SENSORY_HIERARCHY.md (el sistema de imágenes declarado aquí
  alimenta y se coordina con la jerarquía sensorial declarada
  allí; los dos archivos se auditan conjuntamente para verificar
  que el campo de imagen dominante coincide con el sentido
  jerarquizado por la novela)
- WORLD_ARC.md (cuando está activo, recibe la subordinación
  obligatoria a la pregunta central declarada aquí, los
  principios de neutralización aplicables, y las
  declaraciones de resonancia entre motivos y ejes de mundo
  más las coordinaciones campo de imagen × eje de mundo
  declaradas en SISTEMA DE IMÁGENES)

THEMATIC_ENGINE.md se subordina a:
- SERIES_ARCHITECTURE.md (si multivolumen, la pregunta del
  libro deriva de la pregunta de serie)

THEMATIC_ENGINE.md tiene precedencia sobre:
- WORLD_ARC.md (la subordinación del arco de mundo a la
  pregunta central es obligatoria; ningún arco de mundo
  puede resolver la pregunta por vía macro)

THEMATIC_ENGINE.md se revisa en:
- OPERACIÓN D (cada 3-5 capítulos), para verificar que la pregunta
  sigue escalando.
- PASADA 1 del REVISION_PROTOCOL (auditoría estructural).


---
---

