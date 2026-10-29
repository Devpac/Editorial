<!-- Fábrica — SERIES_ARCHITECTURE: base de oficio + adenda de dark romance (v2.0) -->

# SERIES_ARCHITECTURE.md

> **En dark romance rige la ADENDA DE DARK ROMANCE del final de este archivo** (v2.0), que aplica
> `PAREJA_PRIMERO.md`. La base agnóstica sigue vigente.

## PROPÓSITO

Este archivo gestiona la arquitectura de una serie (dilogía,
trilogía, tetralogía, ciclo abierto) como unidad superior al
libro individual. Sin este archivo, los libros posteriores
improvisan arcos que el libro 1 no preparó, o el libro 1
cierra prematuramente líneas que deberían durar toda la serie.

Aplicable sólo si el proyecto es multivolumen. En proyectos
de libro único, este archivo se omite o se marca como no
activo.

JERARQUÍA: Capa 0.5 (por encima de los libros individuales,
por debajo del orquestador general).

Si el proyecto cumple los tres criterios de aplicación de
WORLD_ARC.md (multivolumen, mundo evolutivo, carga temática
del mundo), WORLD_ARC.md coexiste en capa 0.5 como archivo
paralelo a éste. Ambos archivos se sitúan en el mismo nivel
sin jerarquía mutua: SERIES_ARCHITECTURE rige los arcos de
personaje multivolumen; WORLD_ARC rige el arco de mundo de
serie. Cuando los dos archivos están activos, sus inventarios
de deudas y promesas se mantienen diferenciados con
nomenclatura distinguible (ver secciones DEUDAS DE SERIE y
PROMESAS AL LECTOR), y sus calendarios consolidados se auditan
conjuntamente en OPERACIÓN D.

Los archivos de Capa 1 de cada libro (THEMATIC_ENGINE, STORY_SPINE,
CHARACTER_PHYSICS, etc.) se subordinan a éste en lo que
concierne a arcos de serie.

---

## DECLARACIÓN DE SERIE

FORMA DE LA SERIE:
[dilogía / trilogía / tetralogía / ciclo abierto sin número fijo]

FORMA DRAMÁTICA DE LA SERIE:
- ARCO ÚNICO DISTRIBUIDO: una sola pregunta y un solo arco
  cortados en volúmenes (ejemplo: Crónica del asesino de reyes).
- ARCOS PARALELOS CONVERGENTES: cada libro tiene arco propio;
  los arcos convergen al final (ejemplo: Canción de hielo y
  fuego en teoría).
- EPISÓDICA CON ACUMULACIÓN: cada libro tiene trama autónoma;
  los personajes y la pregunta evolucionan entre libros
  (ejemplo: serie Aubrey-Maturin).
- CASOS SEPARADOS CON HILO: cada libro es un caso/episodio;
  el hilo es el personaje o el mundo (detective clásico).

La forma dramática determina qué se cierra en cada libro y qué
queda abierto.

NÚMERO TOTAL DE VOLÚMENES:
[número; si ciclo abierto, declarar]

LONGITUD ESTIMADA DE SERIE:
[suma de palabras; cruzar con SCALE_CALIBRATION de cada libro]

---

## LA PREGUNTA CENTRAL A LO LARGO DE LA SERIE

La pregunta de THEMATIC_ENGINE.md puede:

### OPCIÓN A — EVOLUCIONAR POR FORMULACIÓN
Misma pregunta en forma reformulada por libro. Cada libro
agota una versión de la pregunta y abre la siguiente.

### OPCIÓN B — EXTENDERSE POR DIMENSIÓN
La pregunta se mantiene en forma, pero cada libro la explora
en una dimensión distinta (personal / política / histórica /
metafísica).

### OPCIÓN C — RAMIFICARSE
La pregunta del libro 1 genera subpreguntas que los libros
siguientes desarrollan.

### FORMULACIÓN POR LIBRO

LIBRO 1:
Pregunta en fase [inicial / establecida / desplegada].
Versión: [transcripción o paráfrasis]

LIBRO 2:
Pregunta en fase [...].
Versión: [...]

LIBRO 3:
...

LIBRO N / FINAL:
Pregunta en fase de agotamiento (no resolución).
Qué versión final queda planteada al lector.

Una serie no resuelve la pregunta más que un libro. Agota una
versión amplia de ella.

---

## ARCOS DE PERSONAJE MULTIVOLUMEN

Para cada personaje con física completa cuyo arco exceda un
libro:

### NOMBRE: [...]

FASE EN LIBRO 1: [cuál de las cuatro fases de
CHARACTER_PHYSICS.md alcanza al cierre del libro 1]

FASE EN LIBRO 2: [...]
FASE EN LIBRO 3: [...]
FASE EN LIBRO FINAL: [...]

COSTE ACUMULADO POR LIBRO:
- Al cierre de libro 1: [...]
- Al cierre de libro 2: [...]
- ...

PUNTO DE NO RETORNO:
En qué libro y a qué altura el personaje cruza la línea que
no puede deshacer.

### ARCOS SECUNDARIOS DE SERIE
Un personaje puede ser secundario en libro 1 y promocionar a
protagonista en libro 2 o 3. Si se prevé, declararlo aquí.
Esa promoción exige preparación: el personaje en libro 1 debe
tener densidad suficiente para sostener el ascenso.

---

## DEUDAS DE SERIE

Las deudas tienen dos horizontes:

### DEUDAS DE LIBRO
Se abren y se cierran dentro del mismo libro.
Gestionadas por STORY_SPINE de cada libro y CONTINUITY_PHYSICS.

### DEUDAS DE SERIE
Se abren en un libro, se cierran en otro.
Gestionadas aquí.

FORMATO:
DEUDA [ID]:
- ABRE EN: libro [N], cap. [X]
- CIERRA EN: libro [M], cap. [Y] (previsto)
- TIPO: [trama / personaje / temática / mundo]
- CONSECUENCIA DE NO CERRARLA: qué se rompe

### INVENTARIO DIFERENCIADO RESPECTO A WORLD_ARC

Si WORLD_ARC.md está activo, las deudas de serie gestionadas
en este archivo se circunscriben a las deudas de personaje y
trama de personaje (lo que el archivo cubre nativamente).
Las deudas de mundo puro o de mundo con resonancias propias
se gestionan en WORLD_ARC.md. La distinción no es estética:
permite auditar calendarios sin doble registro y mantener
trazabilidad de qué arco aporta qué deuda.

Para evitar colisión de identificadores cuando ambos archivos
operan, se recomienda nomenclatura distinguible (por ejemplo,
prefijo SP- para deudas de SERIES_ARCHITECTURE, prefijo WA-
para deudas de WORLD_ARC). La elección concreta es decisión
autoral, lo obligatorio es que un identificador permita
distinguir el archivo de origen sin consulta cruzada.

### CRUCES ENTRE DEUDAS DE PERSONAJE Y DEUDAS DE MUNDO

Algunas deudas pueden tener naturaleza híbrida: nacen como
deuda de personaje pero se pagan vía evento de mundo, o
inversamente. Estos cruces se declaran explícitamente para
que el archivo de origen mantenga la deuda como suya y el
otro archivo la registre como cruce.

FORMATO DE CRUCE:
DEUDA [ID origen] cruza con [ID del otro archivo]
- ARCHIVO PRINCIPAL: [SERIES_ARCHITECTURE / WORLD_ARC]
- TIPO DE CRUCE: pago vía mundo / pago vía personaje /
  resonancia simultánea
- LIBRO Y CAPÍTULO DE PAGO COMÚN: [...]

La declaración del cruce previene que la deuda quede
registrada dos veces sin coordinación, o que se pague una vez
en el calendario de un archivo y se considere abierta en el
otro.

### CALENDARIO DE PAGOS POR LIBRO

LIBRO 1 ABRE: [lista de deudas de serie abiertas]
LIBRO 1 CIERRA: [deudas que se pagan en este libro]

LIBRO 2 ABRE: [...]
LIBRO 2 CIERRA: [...]

...

LIBRO FINAL CIERRA: [todas las deudas pendientes deben pagarse
o declararse como final abierto]

---

## PROMESAS AL LECTOR

Distintas de las deudas: son expectativas implícitas que el
libro 1 crea sobre lo que la serie va a entregar.

EJEMPLO:
- Libro 1 presenta un conflicto político de fondo.
  Promesa: la serie lo explorará.
- Libro 1 muestra una relación no resuelta.
  Promesa: evolucionará.
- Libro 1 insinúa un secreto del mundo.
  Promesa: se develará.

Las promesas no declaradas son peligrosas: el lector las
registra igual, y siente traición si no se entregan.

Ejercicio obligatorio tras libro 1: listar las promesas
generadas y decidir cuáles se cumplirán, cuáles se
subvertirán conscientemente, y cuáles se han producido por
error y conviene neutralizar en cap. finales.

### CRUCES CON PROMESAS DE MUNDO

Si WORLD_ARC.md está activo, las promesas que este archivo
gestiona se circunscriben a expectativas sobre personajes,
relaciones y trama. Las promesas sobre evolución del mundo
(transformación institucional, cambio de mapa político,
develamiento de secreto sistémico) se gestionan en
WORLD_ARC.md.

Algunas promesas son ambiguas: el lector las puede leer como
de personaje o como de mundo. Estas promesas mixtas se
declaran como cruces, indicando archivo principal y archivo
secundario. La auditoría conjunta (ver OPERACIÓN D) verifica
que ambos archivos tienen registrado el cruce y que la
entrega prevista no produce contradicción.

---

## PUNTO DE NO RETORNO POR LIBRO

Cada libro de una serie debería tener su propio umbral:
el momento tras el cual el protagonista (y la pregunta
central) no pueden volver al estado anterior al libro.

Sin punto de no retorno, un libro se siente como un episodio
intercambiable dentro de la serie.

LIBRO 1:
Punto de no retorno: [descripción]
Qué se pierde tras cruzarlo: [...]

LIBRO 2:
Punto de no retorno: [...]
...

### ASIMETRÍA ENTRE ARCOS QUE CRUZAN UMBRALES Y ARCOS QUE NO

No todos los arcos de un proyecto multivolumen tienen la
misma relación con los puntos de no retorno. La declaración
explícita de la asimetría es decisión arquitectónica que
condiciona el motor emocional de la serie.

**Caso 1 — Todos los arcos cruzan umbrales.** Cada arco
declarado (de personaje y, si WORLD_ARC activo, también de
mundo) tiene puntos de no retorno propios. La saga es
direccional en todos los frentes; nada vuelve al estado
inicial. Motor emocional: avance irreversible compartido.

**Caso 2 — Solo los arcos de personaje cruzan umbrales; el
arco de mundo no.** Los personajes cambian sin retorno
mientras el mundo se reorganiza preservando su función
subyacente (en términos de WORLD_ARC.md, opción 2 de PUNTOS
DE NO RETORNO DE MUNDO). Esta asimetría es motor emocional
específico: el lector observa que los personajes pagan
precios irreversibles dentro de un mundo que absorbe los
golpes y se recompone, lo que carga la pregunta temática de
una tensión característica.

**Caso 3 — Algunos arcos de personaje cruzan umbrales y
otros no.** Distinción entre POVs cuyo arco implica
transformación irreversible y POVs cuyo arco es de
acumulación o de erosión sin umbral declarado. La asimetría
intra-personajes es típica de proyectos corales donde
algunos cargan el peso direccional y otros operan como
contraste estable.

**Caso 4 — Ningún arco cruza umbrales formales (ciclo
abierto puro).** Caso ya cubierto en NOTA SOBRE CICLO
ABIERTO.

La declaración del caso aplicable es obligatoria cuando el
proyecto es multivolumen. Si WORLD_ARC.md está activo, la
declaración debe ser coherente con la opción declarada en su
sección PUNTOS DE NO RETORNO DE MUNDO. La incoherencia entre
ambos archivos en este punto es error estructural detectado
en OPERACIÓN D.

---

## PUNTOS DE CONVERGENCIA

En series corales o con múltiples líneas, indicar los
momentos de convergencia previstos:

- Convergencia de libro 2: qué líneas se tocan, qué cambia.
- Convergencia de libro final: resolución coral.

---

## RIESGOS DE SERIE

### RIESGO 1 — SEGUNDO LIBRO FLÁCIDO
Un libro 2 que repite el motor del libro 1 sin escalar la
pregunta o transformar al personaje.
Prevención: declarar qué hace libro 2 que libro 1 no podía
hacer. Si la respuesta no existe, revisar el diseño.

### RIESGO 2 — SERIE QUE NO AVANZA
Libro tras libro el personaje "casi" cambia pero nunca cambia
del todo. El lector detecta el truco.
Prevención: verificar que el punto de no retorno de cada libro
cambia realmente el estado.

### RIESGO 3 — DEUDAS ACUMULADAS SIN CAPACIDAD DE PAGO
El libro final no tiene espacio para cerrar todas las deudas
abiertas. Cierres forzados, densidad insostenible.
Prevención: en cada libro, cerrar deudas de serie que
correspondan, no aplazarlas todas al final.

### RIESGO 4 — DESAPARICIÓN DE PERSONAJES
Personajes importantes en libro 1 se diluyen en libros
siguientes porque la arquitectura no los necesita.
El lector siente traición.
Prevención: declarar al inicio qué personajes son de serie
y cuáles son de libro.

### RIESGO 5 — REESCRITURA RETROACTIVA
En libro 3 se descubre que libro 1 debería haber dicho otra
cosa. No se puede corregir.
Prevención: cuanto más tarde se cierre SERIES_ARCHITECTURE,
más libertad queda, pero también más riesgo. Versión mínima
del archivo antes del cap. 1 del libro 1.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — NECESIDAD DE SERIE
¿La pregunta central requiere realmente varios volúmenes, o
se resolvería mejor en un libro más largo?
Si un volumen único bastaría, la serie es comercial, no
estructural.

TEST 2 — FUNCIÓN POR LIBRO
Cada libro: ¿hace algo que ningún otro libro de la serie puede
hacer? Si dos libros son intercambiables, sobra uno.

TEST 3 — ARCO DE PERSONAJE REAL
¿El personaje principal al final de la serie es demostrablemente
distinto del inicio? Si no, la serie es episódica pura (válido)
o fallida.

TEST 4 — CIERRE DE DEUDAS
¿El calendario de cierres es realista? Libro final: ¿tiene
espacio para cerrar lo que debe cerrarse?

---

## CUÁNDO SE REVISA

- Antes del cap. 1 del libro 1: versión mínima obligatoria
  (forma de serie, pregunta por libro, personajes de serie).
- Al cierre del libro 1: revisión completa. Qué se cumplió de
  lo previsto, qué se descubrió, qué hay que ajustar.
- Al inicio de cada libro siguiente: consulta obligatoria.
- OPERACIÓN D de cada libro: verificar que los compromisos de
  serie siguen en pie.

---

## RELACIÓN CON OTROS ARCHIVOS

SERIES_ARCHITECTURE.md es paralelo a:
- WORLD_ARC.md (cuando está activo). Ambos archivos coexisten
  en capa 0.5 sin jerarquía mutua. SERIES_ARCHITECTURE rige
  arcos de personaje multivolumen; WORLD_ARC rige arco de
  mundo de serie. Sus inventarios de deudas y promesas se
  mantienen diferenciados con nomenclatura distinguible.
  Cruces entre arcos de personaje y arcos de mundo se
  declaran explícitamente en ambos archivos.

SERIES_ARCHITECTURE.md es superior a:
- THEMATIC_ENGINE.md (de cada libro; la pregunta del libro se
  deriva de la pregunta de serie)
- STORY_SPINE.md (de cada libro)
- CHARACTER_PHYSICS.md (los arcos individuales de libro
  encajan en los arcos de serie)

SERIES_ARCHITECTURE.md recibe de:
- La decisión autoral inicial sobre forma de serie.
- Los descubrimientos de cada libro escrito.

SERIES_ARCHITECTURE.md alimenta:
- Todos los archivos de Capa 1 de cada libro.
- El CONTINUITY_PHYSICS de serie (si se mantiene uno
  transversal).
- WORLD_ARC.md, en lo que respecta a los cruces declarados de
  arcos de personaje con arcos de mundo (la coordinación es
  bidireccional cuando ambos archivos están activos).

---

## NOTA SOBRE CICLO ABIERTO

Si la serie no tiene número fijo de volúmenes (por ejemplo,
una serie de detective), muchas de las secciones anteriores
se reformulan:

- La pregunta central puede ser estable (no agotarse).
- Los arcos de personaje son graduales, acumulativos.
- Las deudas de serie son pocas; cada libro es
  mayoritariamente autónomo.
- El punto de no retorno puede faltar; lo que cambia es el
  mundo o las condiciones, no el personaje.

Un ciclo abierto bien concebido sigue siendo arquitectura,
no improvisación. Declarar qué es estable y qué acumula.


---
---

## ADENDA DE ESPECIALIZACIÓN — Fábrica (género)

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

> Aplica `PAREJA_PRIMERO.md`, que manda donde choquen y deroga la adenda de Intriga que traía este
> archivo: cada libro hace su arco de pareja entero (trama A) y su trama del libro (trama B), y entre
> libros solo se raciona lo que la pareja se revela (quién raciona, lo declara la obra). La base agnóstica de arriba sigue vigente. Es de género;
> la forma de la saga la declara la obra (SERIES_GLUE, adenda de dark romance: A, la misma pareja en
> muchos libros; B, dúo o trilogía; C, parejas rotativas).

### 1. Forma dramática (especializa DECLARACIÓN DE SERIE)
La forma **A** es, en la base, EPISÓDICA CON ACUMULACIÓN para la trama B de cada libro y ARCO ÚNICO
DISTRIBUIDO para la relación y la trama horizontal. Lo que se reparte entre libros es la confesión,
no el arco: **cada libro tiene su arco de pareja completo** (su pregunta, su transgresión, su momento
oscuro, su calor y su respuesta, que no es un final feliz: BRIEFING, campo 2 bis) además de su trama
B, y la relación sigue abierta en lo que la pareja todavía no se ha revelado. La **B** es ARCO ÚNICO
DISTRIBUIDO, con el mismo arco de pareja en cada libro. La **C** es CASOS SEPARADOS CON HILO: cada
libro, una pareja y su trama, autónomas y cerradas; el hilo es el mundo compartido (SERIES_GLUE).

### 2. La pregunta central (especializa LA PREGUNTA CENTRAL A LO LARGO DE LA SERIE)
En las formas A y B la pregunta que atraviesa la saga es de la pareja: qué serán el uno para el
otro y qué precio pagarán por serlo (y, si hay trama horizontal, la verdad que la persigue). Cada
libro la formula un paso más lejos (OPCIÓN A). En la C, la del mundo compartido (OPCIÓN B aplicada
al elenco: la misma pregunta de fondo en la vida de una pareja distinta en cada libro), con la
oscuridad del género.

### 3. Arcos multivolumen (especializa ARCOS DE PERSONAJE MULTIVOLUMEN)
**Se raciona el peldaño, no la intensidad** (`PAREJA_PRIMERO.md` §4). En la forma A el arco de quien
raciona su rendición (lo declara la obra) se mide en la **escala de rendición**: lo que revela que no
había revelado, con los peldaños y el libro de cada uno declarados en la biblia; el del otro, como lo
declare la obra. Al menos un peldaño por libro; ninguno antes
de su libro. El choque, el deseo, el contacto y el calor no se racionan: están en todos los libros,
con sus suelos (`PAREJA_PRIMERO.md` §3). En la B, la escala se reparte entre los dos o tres libros y
el último entrega el peldaño final. En la C, cada pareja hace su arco entero en su libro y lo cierra
en fase resuelta, que no retrocede en los siguientes; los ARCOS SECUNDARIOS DE SERIE son la rotación
de parejas: qué secundario del libro N protagoniza el N+1, con la densidad que la base exige para el
ascenso (SERIES_GLUE, ROTACIÓN DE PAREJAS).

### 4. Deudas de serie (especializa DEUDAS DE SERIE y CALENDARIO DE PAGOS POR LIBRO)
Admisibles en A y B: deudas de relación, que son de confesión (lo que uno calla, lo que el otro aún
no sabe de él, lo que se deben), y de trama horizontal (los relojes de la saga, si los hay, con el libro
en que empiezan y suenan). Ninguna deuda de intensidad pasa de un libro a otro, y está prohibido
aplazar una deuda de la trama del libro. Cada deuda tiene libro de pago en la biblia; OPERACIÓN D
comprueba al cerrar cada libro que ninguna se ha pasado de su libro sin decisión del autor. En la C,
solo deudas de mundo y de aparición o rotación de personajes; ninguna de trama del libro ni de final
feliz en suspenso.

### 5. Promesas al lector (especialización)
La forma A promete que la pareja sigue, que cada libro trae su choque, su deseo y su calor, y que la
confesión racionada llega peldaño a peldaño; la B, que el último libro cierra lo que abrió el primero; la
C, que el mundo sigue vivo y que cada personaje sembrado tendrá su libro y su final feliz. Ninguna
promete un final limpio: el género promete un final juntos.

### 6. Punto de no retorno por libro
Cada libro cruza al menos un umbral irreversible en la relación (un peldaño de la escala, una
transgresión que ya no se deshace, un descubrimiento) y, si hay trama horizontal, uno en ella. Un
libro que solo mueve su trama propia es un libro de relleno.

### 7. Riesgos propios del género (especializa RIESGOS DE SERIE)
- **RIESGO 1 agravado, el segundo libro flácido:** en dark romance se nota en que la relación
  repite el motor del primero. Prevención: el libro 2 cambia las reglas de la pareja (algo que
  uno descubre, algo que el otro ya no puede negar). Se pregunta en la lectura del plan del libro
  (`PROTOCOLO_LECTURA.md`, §6 bis).
- **RIESGO 2 agravado, la pareja que no avanza:** el *edging* sin fin. La lectora del canal que
  declare la obra abandona la saga si la consumación o la entrega se aplazan demasiado; el ritmo lo fija
  la biblia, dentro de los suelos de `PAREJA_PRIMERO.md` §3, y se audita por libro.
- **RIESGO 4 agravado en la forma C, la pareja que desaparece:** la lectora sigue parejas concretas;
  el registro del elenco de comunidad de SERIES_GLUE es obligatorio.
- **RIESGO NUEVO, la intensidad racionada:** guardar para el libro siguiente el contacto o el calor,
  como si fueran peldaños. Prevención: los suelos de `PAREJA_PRIMERO.md` §3 en cada libro (TEST A1
  de SERIES_GLUE).
- **RIESGO NUEVO, el reinicio del héroe:** quien raciona su rendición vuelve al punto cero en cada libro para que haya
  conflicto. Prevención: TEST A3 de SERIES_GLUE.
- **RIESGO NUEVO, el libro que solo existe para el siguiente:** un puente sin pago propio.
  Prevención: TEST A1 de SERIES_GLUE.

> **Valores de la obra →** `PRESET_<OBRA>.md` › SERIES_ARCHITECTURE › Declaración de la saga.
> *Qué declara aquí la obra:* su número de libros y de arcos, la pregunta central, quién raciona su rendición y la escala de rendición con sus peldaños y el libro de cada uno (si la tiene), cómo se mide el arco del otro, sus deudas de serie y relojes con su libro de pago, y dónde declara cada libro su arco de pareja y qué hace que el anterior no podía hacer.
