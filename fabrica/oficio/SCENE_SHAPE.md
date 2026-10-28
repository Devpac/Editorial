# SCENE_SHAPE.md

## PROPÓSITO

SCENE_NECESSITY.md decide si una escena existe. Este archivo decide
qué forma tiene. Entre el contrato (CHAPTER_BRIEF + SCENE_NECESSITY)
y la prosa generada (OPERACIÓN B) falta un nivel: la arquitectura
interna de la escena.

Sin forma de escena, la prosa entra sin saber cuándo acelerar, dónde
poner el peso, qué dejar fuera de la página. Resultado: escenas
que se estiran o se atropellan sin motivo interno.

JERARQUÍA: Capa 2.

---

## LOS CUATRO MOMENTOS DE UNA ESCENA

Toda escena tiene al menos cuatro momentos internos. Pueden estar
más o menos marcados, pero declarados o no, existen. Declararlos
mejora la ejecución.

### MOMENTO 1 — ENTRADA
El lector es introducido en la situación. Orientación mínima
necesaria: quién, dónde, en qué estado.

CRITERIO OPERATIVO:
La entrada debe dar al lector las coordenadas sin demorarse.
Frecuentemente: en primer párrafo, quién está presente y qué
está haciendo. El resto se revela en el curso de la escena.

ERROR FRECUENTE:
Descripción estática del entorno antes de la acción.
Corrección: entrada in medias res (en medio de la acción)
siempre que el lector pueda orientarse rápidamente.

### MOMENTO 2 — PRESIÓN
La fuerza dramática se establece. Esto es distinto a la entrada:
aquí el lector entiende qué está en juego.

CRITERIO OPERATIVO:
Si un lector tuviera que abandonar la escena, ¿a partir de qué
punto querría saber cómo sigue? Ese es el momento 2.

CONECTAR CON:
TENSION_MECHANICS.md — qué mecanismo sostiene la presión.
RELATIONSHIP_PHYSICS.md — qué asimetría se activa si hay dos
personajes.

### MOMENTO 3 — GIRO
El estado interno de la escena cambia. No tiene que ser un
"giro de trama" mayor: puede ser una inflexión emocional, una
palabra que cambia el tono, un gesto pequeño pero irreversible.

CRITERIO OPERATIVO:
Identificar el momento antes del cual la escena iba en una
dirección y después del cual va en otra. Si no existe,
la escena es monolineal y probablemente plana.

Este es con frecuencia el momento más importante de ejecutar bien:
la prosa aquí debe ralentizar y aumentar densidad. Ver abajo
(GESTIÓN DE TIEMPO INTERNO).

### MOMENTO 4 — SALIDA
La escena cierra dejando un estado nuevo y, habitualmente,
una deuda abierta (la pregunta 3 de SCENE_NECESSITY).

CRITERIO OPERATIVO:
La última frase de la escena debería ser difícil de mover sin
perder algo. Si la última frase es intercambiable por otra,
no se ha construido salida.

TIPOS DE SALIDA:
- Cierre sobre gesto: la escena termina en una acción pequeña que
  sintetiza.
- Cierre sobre no-dicho: el personaje calla algo que la escena ha
  hecho evidente.
- Cierre sobre imagen: detalle sensorial que carga significado.
- Cierre sobre tiempo: un salto temporal directo que opera por
  yuxtaposición con lo siguiente.
- Cierre sobre frase: diálogo que suspende.

Evitar: cierre sobre explicación. El narrador explicando lo
que acaba de ocurrir rompe el efecto de salida.

---

## ESTRUCTURA POR TIPO DE ESCENA

Los cuatro momentos se modulan según tipo (ver SCENE_NECESSITY.md).

### CONFRONTACIÓN
Entrada: rápida. Los personajes ya están en colisión.
Presión: inmediata. Stakes declarados en primera página.
Giro: el momento en que la confrontación cambia de eje. Con
frecuencia ocurre a los dos tercios de la escena.
Salida: asimetría alterada. Alguien ha perdido algo.

### DECISIÓN
Entrada: establecer la opción.
Presión: dramatizar el coste de cada alternativa.
Giro: suele ser interno. El personaje ve algo que no veía. A veces
ocurre en silencio.
Salida: la decisión ya tomada pero sus consecuencias abiertas.
Rara vez la escena termina cuando la decisión se verbaliza:
termina cuando la decisión se ejecuta o cuando se deja ver su
coste.

### REVELACIÓN
Entrada: situación aparentemente normal.
Presión: un elemento empieza a no cuadrar.
Giro: la revelación. Momento más importante de toda la escena,
ejecutar con máxima densidad.
Salida: ajuste inmediato. Nadie queda como estaba.

### SEDIMENTACIÓN
Entrada: más lenta permitida.
Presión: implícita. No declarada.
Giro: emocional interno, no necesariamente compartido entre
personajes.
Salida: preparación de lo que viene, a veces por imagen.

### ACCIÓN / SUSPENSE
Entrada: debe bajar la temperatura un momento antes de subirla
(contraste).
Presión: escalada.
Giro: cambio de vector (la acción va en una dirección, algo la
desvía).
Salida: consecuencia irreversible.

---

## GESTIÓN DE TIEMPO INTERNO

La relación entre tiempo del suceso y espacio narrativo
(palabras dedicadas) es ajustable y significativa.

### TIEMPO COMPRIMIDO
Mucho suceso, pocas palabras.
Usar en: transiciones, aceleraciones intencionales, información
de soporte.
Indicador: "Durante las siguientes semanas..."

### TIEMPO PROPORCIONAL
El suceso y la escena son aproximadamente equivalentes.
Estado de base.

### TIEMPO DILATADO
Poco suceso, muchas palabras.
Usar en: picos de tensión, giros, momentos emocionales densos.
Indicador: describir tres segundos en dos páginas.

REGLA OPERATIVA:
La tensión escala dilatando. Cuanto más importa el momento, más
lento avanza. La inversa es el error más común:
acelerar en los picos porque "ahí está la acción".
La acción en los picos se dilata; son los pasajes
de bajo interés los que se comprimen.

CRUCE CON TENSION_MECHANICS.md: la gestión de pacing de escena.

---

## MAPA DE DENSIDAD DE LA ESCENA

Antes de escribir, distribuir la densidad sensorial, de textura y
de diálogo según los cuatro momentos.

ENTRADA: densidad media (orientación).
PRESIÓN: densidad variable (depende del tipo).
GIRO: densidad máxima. Aquí es donde el detalle, el gesto pequeño,
el pensamiento filtrado tienen que operar al límite. Ver
SENSORY_HIERARCHY.md para la elección sensorial.
SALIDA: densidad alta pero concentrada. Pocos elementos bien
elegidos.

Una escena con densidad uniforme de principio a fin es plana
independientemente de su contenido.

MODULACIÓN DE CUOTAS LOCALES DE PROSA. La densidad por momento
modula cuotas locales de PROSE_LINE_DISCIPLINE.md dentro del
techo del régimen declarado en AESTHETIC_REGISTER. La regla
operativa: el techo del régimen es el techo del capítulo
agregado (la suma de las cuatro escenas no puede desbordarlo);
dentro del capítulo, los momentos de la escena modulan
localmente.

ENTRADA: cuotas estándar del régimen. La orientación al lector
no licencia profusión adjetival ni mitigación.

PRESIÓN: cuotas estándar, con atención específica a TIC 7
(mitigación atemperada constante): la presión dramática se
construye por concreción nominal y verbal, no por hedge-adverbs
ni mitigadores sintácticos que diluyen la apuesta.

GIRO: cuota local elevada admisible si la materia lo pide. El
giro puede sostener un ternario obsesivo (TIC 1) o un doblete
adjetival (TIC 2) cuando la acumulación es la forma del
desplazamiento emocional, siempre que la cuota global del
capítulo no se desborde y la acumulación no sea hábito formal
sino exigencia de la materia. La dilatación de tiempo interno
declarada arriba se traduce en densidad nominal y verbal
concentrada, no en multiplicación de modificadores.

SALIDA: densidad alta pero disciplinada. Aplicar TIC 4
(frase-resumen al cierre de párrafo, máximo una por capítulo) y
TIC 5 (cierre sentencioso de capítulo, ideal cero) con
estrictitud, ya que la salida es donde más fácilmente se cuelan
ambos tics. La regla de "cierre sobre gesto, sobre no-dicho,
sobre imagen, sobre tiempo, sobre frase" declarada arriba en
TIPOS DE SALIDA es coherente con esos tics: ninguno de los
cinco tipos legítimos exige glosa explicativa ni sentencia
aforística.

---

## ENTRADAS Y SALIDAS EN MEDIAS RES

Un principio operativo: las escenas tienden a empezar más tarde
y terminar antes de lo que el instinto sugiere.

PRINCIPIO DE ENTRADA TARDÍA:
Empezar la escena lo más cerca posible del momento 2 (presión).
Lo que el lector necesita saber para orientarse puede distribuirse
en pequeñas pinceladas a lo largo del momento 1 y el principio
del 2, sin escena previa de preparación.

PRINCIPIO DE SALIDA TEMPRANA:
Cortar la escena justo después del momento 4, no alargarla hasta
ver a los personajes despedirse. La despedida raramente añade
algo; la suspensión sí.

EJEMPLO NAVAL:
Entrada tardía: no empezar cuando el protagonista sube al barco
y pasa lista, empezar cuando la orden que lo pondrá en apuro
ya se ha dado y él lleva diez minutos sabiéndola.
Salida temprana: no terminar con todos volviendo a sus puestos,
terminar con el mando asintiendo y girándose.

---

## EL DIALOGO COMO VECTOR DE FORMA

Cuando la escena es principalmente diálogo, los cuatro momentos
se expresan a través del diálogo mismo (ver DIALOGUE_MECHANICS.md):

- Entrada: primer intercambio establece la situación.
- Presión: turno que introduce el desacuerdo, la asimetría, la
  tensión.
- Giro: frase o silencio que desplaza el eje de la conversación.
- Salida: última palabra (o último silencio declarado).

Un diálogo bien construido tiene estos momentos sin necesidad de
narración entre medias. Si requieren mucha narración para
funcionar, el diálogo está sobrecargado.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — IDENTIFICACIÓN DE MOMENTOS
Tras escribir la escena, ¿puedes señalar con claridad los cuatro
momentos? Si alguno falta o se solapa confusamente, la escena no
tiene estructura interna.

TEST 2 — DENSIDAD VARIABLE
¿La densidad cambia entre momentos? Si la página entera tiene
ritmo uniforme, falta modulación.

TEST 3 — ENTRADA Y SALIDA
¿Podrías empezar la escena más tarde y terminarla antes?
Con frecuencia la respuesta es sí, y aplicarla mejora la escena.

TEST 4 — LA ÚLTIMA FRASE
¿La última frase es intercambiable? Si sí, no hay salida.

---

## RELACIÓN CON OTROS ARCHIVOS

SCENE_SHAPE.md recibe de:
- SCENE_NECESSITY.md (la escena está justificada, tiene tipo)
- CHAPTER_BRIEF.md (posición y función en el capítulo)
- TENSION_MECHANICS.md (mecanismo activo)
- SEAMS_AND_HINGES.md (si la escena es apertura o cierre de
  novela, o bisagra importante)

SCENE_SHAPE.md alimenta:
- OPERACIÓN B (escritura informada: dónde dilatar, dónde comprimir)
- SENSORY_HIERARCHY.md (dónde concentrar densidad sensorial)
- DIALOGUE_MECHANICS.md (ritmo del diálogo)
- PROSODY_AND_MUSIC.md (mapa de densidad se traduce en ritmo
  de párrafo)
- PROSE_LINE_DISCIPLINE.md (la densidad por momento de la escena
  modula cuotas locales dentro del techo del régimen; el giro
  puede sostener TIC 1 o TIC 2 si la materia lo pide y la cuota
  global del capítulo no se desborda; la salida disciplina
  TIC 4 y TIC 5; ver sección MAPA DE DENSIDAD DE LA ESCENA
  más arriba)

SCENE_SHAPE.md se invoca en:
- OPERACIÓN A (diseño final de escena, después de necesidad).
