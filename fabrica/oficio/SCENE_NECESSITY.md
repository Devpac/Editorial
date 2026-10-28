<!-- Fábrica v3.0 — SCENE_NECESSITY: base de oficio + adenda de dark romance (v2.0) -->

# SCENE_NECESSITY.md

## PROPÓSITO

Este archivo decide si una escena existe. Sin un filtro de necesidad,
las novelas se llenan de escenas plausibles pero estructuralmente
vacías, que consumen espacio sin generar arco.

PREGUNTA HERMANA (en ELLIPSIS_PROTOCOL.md):
"¿Esta escena, aunque exista dramáticamente, se narra o se elide?"
Las dos preguntas son distintas. Una escena puede ser necesaria
y aun así elidirse deliberadamente. Consultar ambos archivos
antes de pasar a diseño.

JERARQUÍA: Capa 2. Opera después de CHAPTER_BRIEF.md.

Una escena puede ser buena prosa y aun así no deber existir.
La calidad de la prosa no sustituye a la necesidad dramática.

---

## PREGUNTAS DE ENTRADA (las tres mínimas)

### PREGUNTA 1 — ¿QUÉ CAMBIA?

No "qué ocurre": qué estado es distinto al final respecto al inicio.
Los estados son los tres ejes de CHAPTER_BRIEF.md:

- Relacional: ¿ha cambiado el vector de alguna relación?
- Emocional: ¿ha cambiado el estado interno de algún personaje?
- Informativo: ¿sabe alguien algo que no sabía? ¿Lo sabe el lector?

Si la respuesta a los tres es "no": la escena no existe.
Si solo uno: puede ser legítimo en escenas cortas de transición,
pero verificar la segunda pregunta con especial rigor.

### PREGUNTA 2 — ¿POR QUÉ AHORA?

La posición de la escena en la estructura no es arbitraria.
¿Por qué en este capítulo, en este momento, y no antes ni después?

Posibles respuestas válidas:
- "Porque la información necesaria para que funcione solo está
  disponible a partir del capítulo anterior."
- "Porque si ocurriera antes, el personaje aún no habría perdido
  lo suficiente como para responder así."
- "Porque si ocurriera después, el siguiente evento ya no tendría
  detonante."

Respuestas inválidas:
- "Porque toca." (No hay reloj dramático que lo justifique.)
- "Porque si no, no hay capítulo." (La escena compensa un diseño
  débil de capítulo, no responde a necesidad propia.)

### PREGUNTA 3 — ¿QUÉ DEJA SIN RESOLVER?

Toda escena debe generar una presión que la siguiente no pueda
ignorar. El gancho no es recurso de entretenimiento: es la deuda
que abre la escena hacia lo que viene.

Tipos de deuda:
- Pregunta explícita no respondida.
- Tensión emocional elevada que exige descarga o continuación.
- Amenaza proyectada hacia el futuro.
- Información parcialmente revelada.
- Relación alterada pero no reconsolidada.

Si la escena no deja nada abierto, la siguiente empieza desde cero.
Eso es puntuación, no continuidad.

---

## TIPOS DE ESCENA Y CRITERIOS ESPECÍFICOS

No todas las escenas cumplen las preguntas del mismo modo.
Identificar el tipo antes de evaluar.

### ESCENA DE CONFRONTACIÓN
Dos o más personajes en colisión.
CRITERIO AÑADIDO: al menos uno sale con algo distinto, aunque sea
una duda. Confrontaciones donde ambos se reafirman en su posición
original son ruido.

### ESCENA DE DECISIÓN
Un personaje frente a una opción significativa.
CRITERIO AÑADIDO: la decisión debe tener coste. Si la opción
elegida es gratis, no era decisión.

### ESCENA DE REVELACIÓN
Se descubre una información que altera el entendimiento.
CRITERIO AÑADIDO: la revelación debe cambiar cómo alguien
(personaje o lector) interpreta lo que ya ha visto, no solo añadir
dato nuevo.

### ESCENA DE SEDIMENTACIÓN
Aparentemente nada cambia: personajes descansan, viajan, esperan.
CRITERIO AÑADIDO (importante): la sedimentación es legítima si:
- Prepara un pico próximo y lo aumenta por contraste.
- Permite al lector asimilar cambios recientes.
- Deja visible una tensión subterránea que no se había podido
  mostrar en las escenas anteriores por densidad.
Una escena de sedimentación sin ninguna de estas funciones es
relleno.

### ESCENA DE ACCIÓN / SUSPENSE EXTERNO
Peligro físico o urgencia práctica.
CRITERIO AÑADIDO: los stakes deben estar construidos previamente
(ver TENSION_MECHANICS.md). Acción sin stakes es coreografía.

### ESCENA DE TRANSICIÓN
Breve, principalmente funcional.
CRITERIO AÑADIDO: si la transición no carga ningún detalle que
haga trabajo más adelante (atmósfera, información, estado
emocional), puede eliminarse y sustituirse por un salto de línea.

### ESCENA DE DIÁLOGO SOSTENIDO
Conversación extensa como materia principal.
CRITERIO AÑADIDO: el vector relacional debe moverse.
Ver RELATIONSHIP_PHYSICS.md. Un diálogo sin movimiento de vector
es información disfrazada de escena.

---

## DIAGNÓSTICO DE ESCENAS-PROBLEMA

Síntomas frecuentes y qué suelen indicar:

### SÍNTOMA — "ME GUSTA ESTA ESCENA PERO NO SÉ DÓNDE VA"
Diagnóstico: la escena tiene buena textura pero no tiene función.
Solución: o se le inyecta función (modificar para que uno de los
tres ejes cambie significativamente) o se guarda aparte para otro
proyecto.

### SÍNTOMA — "LA ESCENA ESTÁ EN EL LUGAR EQUIVOCADO"
Diagnóstico: la función es legítima pero la pregunta 2 falla.
Solución: mover. Frecuentemente una escena mal ubicada funciona
perfectamente dos capítulos antes o dos después.

### SÍNTOMA — "LA ESCENA NO SE CIERRA"
Diagnóstico: la pregunta 1 tiene respuesta pero no se está
ejecutando en la prosa. Los cambios están decididos pero no
dramatizados.
Solución: aumentar el peso de los gestos, acciones o palabras que
marcan el cambio. Bajar la explicación y subir el síntoma.

### SÍNTOMA — "LA ESCENA ES REDUNDANTE"
Diagnóstico: el mismo cambio ya ocurrió antes. Puede ser error
(escena duplicada) o indicio de estancamiento de arco (el personaje
no avanza porque el autor no ha dejado que avance).
Solución: eliminar o fundir con la escena original.

### SÍNTOMA — "LA ESCENA ES PERFECTA PERO ME ABURRE"
Diagnóstico: cumple todas las preguntas pero su mecanismo de
tensión está mal elegido. Incertidumbre cuando ya no hay
incertidumbre; cuenta atrás cuando el lector ya sabe que sobra
tiempo.
Solución: cambiar el mecanismo, no eliminar la escena.
Ver TENSION_MECHANICS.md.

---

## PROHIBICIÓN EXPLÍCITA

Una escena no puede terminar en el mismo estado emocional,
relacional e informativo en que empezó.
Si lo hace, es decoración, no dramaturgia.

EXCEPCIÓN DECLARADA:
En régimen kishōtenketsu (ver STORY_SPINE.md), una escena puede
no cambiar estado manifiesto pero cambiar el marco de comprensión
del lector. La prohibición sigue operando: lo que cambia es el
entendimiento, y ese es el tercer eje.

---

## ESCENAS DE RETORNO

Cuando la misma situación aparece dos o más veces (mismo lugar,
misma configuración), verificar:

¿Algo es distinto esta vez? Si no, la escena es repetición.

Si hay diferencia intencional, declararla:
- "Segunda cena, pero ahora A sabe lo que B mintió en la primera.
  La misma mesa es otra cosa."

Las escenas de retorno bien construidas son palancas dramáticas
poderosas. Las mal construidas producen sensación de déjà vu.

---

## PROTOCOLO DE VERIFICACIÓN (antes de escribir)

1. Responder las tres preguntas de entrada. Si alguna queda vacía,
   redesignar.
2. Identificar el tipo de escena y aplicar criterio específico.
3. Revisar si hay síntomas de escena-problema en el diseño previo.
4. Confirmar conexión con SCENE_SHAPE.md (forma interna) antes de
   pasar a escritura.

---

## TESTS DE FUNCIONAMIENTO

Las tres preguntas de entrada se reformulan aquí como tests
cuantificables que se aplican antes de aceptar la escena en el
diseño y después de escribirla en revisión.

TEST 1 — CAMBIO EFECTIVO ARTICULABLE
Al cierre del diseño de la escena (y, en revisión, al cierre del
texto), identificar cuál de los tres ejes cambió y articular el
cambio en una frase concreta:
- "El vector A→B pasó de aliados con reservas a aliados con
  ventaja informativa de A."
- "C pasó de creer que su padre era inocente a sospechar que
  miente."
- "El lector sabe ahora que la carta nunca llegó."
Si la articulación no sale en una frase, el cambio no está en la
prosa: está solo en la intención.

TEST 2 — POSICIÓN DEFENDIBLE
Formular por qué la escena va en este capítulo y no antes ni
después. La respuesta debe apelar a uno de los criterios válidos
declarados en PREGUNTA 2 (información disponible solo desde
capítulo previo, coste pagado solo a esa altura, detonante de
escena posterior). Respuestas inválidas: "porque toca", "porque
si no, no hay capítulo". Si la justificación cae en lo inválido,
mover la escena al capítulo correcto o eliminarla.

TEST 3 — DEUDA ABIERTA IDENTIFICABLE
Identificar la deuda concreta que la escena deja abierta hacia la
siguiente. Una de las cinco: pregunta explícita no respondida,
tensión emocional pendiente, amenaza proyectada, información
parcialmente revelada, relación alterada y no reconsolidada. Si no
puede identificarse ninguna, la siguiente escena empieza desde
cero y no hay continuidad dramática.

TEST 4 — CRITERIO DE TIPO CUMPLIDO
Identificar el tipo de escena (confrontación, decisión,
revelación, sedimentación, acción, transición, diálogo sostenido)
y verificar el criterio añadido específico declarado para ese
tipo. Si el criterio no se cumple, la escena pertenece al tipo
solo nominalmente. La sedimentación es el tipo más vulnerable a
fallar este test: sin ninguna de las tres funciones declaradas
(preparación de pico próximo, asimilación de cambios recientes,
visibilización de tensión subterránea), es relleno.

TEST 5 — PROHIBICIÓN DE INMOVILIDAD
Comparar el estado al inicio y al cierre de la escena en los tres
ejes (relacional, emocional, informativo). Si los tres son
idénticos, la escena es decoración, no dramaturgia. Excepción
única: régimen kishōtenketsu, donde el cambio puede ser solo del
marco de comprensión del lector (tercer eje informativo, aplicado
al lector y no al personaje). Cualquier otra justificación de
inmovilidad es ilegítima.

TEST 6 — REPETICIÓN DE RETORNO DECLARADA
Si la escena ocurre en lugar o configuración ya visitada, declarar
qué es distinto esta vez. Si no hay diferencia intencional
articulable, la escena es repetición y debe eliminarse o fundirse
con la original.

---

## RELACIÓN CON OTROS ARCHIVOS

SCENE_NECESSITY.md recibe de:
- CHAPTER_BRIEF.md (lista de escenas necesarias y posibles)
- STORY_SPINE.md (posición estructural global)
- RELATIONSHIP_PHYSICS.md (qué vector debe moverse)
- INFORMATION_CHOREOGRAPHY.md (qué hechos están en fase activa
  en este capítulo)

SCENE_NECESSITY.md opera en conjunto con:
- ELLIPSIS_PROTOCOL.md (archivo hermano: la escena necesaria
  puede aun así elidirse; ambos se consultan antes de escribir).

SCENE_NECESSITY.md alimenta:
- SCENE_SHAPE.md (la escena es necesaria; ahora darle forma)
- CONTINUITY_PHYSICS.md (registro de cambios tras escribir)

SCENE_NECESSITY.md se invoca en:
- OPERACIÓN A (diseño de escena, antes de escribir).
- OPERACIÓN C (revisión de capítulo).


---
---

