<!-- MODELO_DarkRomance v2.0 — REVISION_PROTOCOL: base agnóstica v7 (verbatim) + adenda de dark romance (v2.0) -->

# REVISION_PROTOCOL.md

## PROPÓSITO

Este archivo cubre el vacío más grande del sistema en su
primera formulación: la fase de reescritura posterior al
primer borrador completo.

OPERACIÓN C cierra cada capítulo y OPERACIÓN D audita cada
3-5 capítulos. Ambas son prospectivas: miran hacia adelante.
Ninguna releyó la novela entera como lector.

Una novela no se termina con la última palabra del último
capítulo. Se termina después de varias pasadas completas.
Este archivo las organiza.

Si WORLD_ARC.md está activo (sagas multivolumen con mundo
evolutivo de carga temática), la PASADA 1 incorpora auditoría
específica del arco de mundo en el libro auditado y, según
posición del libro en la saga, en la trayectoria multilibro
acumulada hasta ese punto. Esa auditoría se documenta dentro
de la PASADA 1 más abajo.

JERARQUÍA: Capa 4 (post-escritura).
Se activa cuando el primer borrador está completo.

---

## DEFINICIÓN DEL PRIMER BORRADOR

Se considera "primer borrador completo" cuando:
- Todos los capítulos previstos en STORY_SPINE están escritos.
- OPERACIÓN C se ha ejecutado sobre cada capítulo.
- OPERACIÓN D se ha ejecutado en sus hitos correspondientes.
- CONTINUITY_PHYSICS está actualizado hasta el final.
- Si WORLD_ARC.md activo: el REGISTRO 10 de CONTINUITY_PHYSICS
  está actualizado con todas las manifestaciones de eje del
  libro y el estado actual de cada eje al cierre del libro
  coincide con (o discrepa de forma documentada con) el estado
  declarado en WORLD_ARC.md como cierre de ese libro.

Antes de este punto, no se abren pasadas de revisión.
Aplicar revisión a un borrador incompleto bloquea el avance
y rara vez mejora.

Excepción única: si en cualquier momento se detecta que un
archivo de Capa 1 (la pregunta, el personaje, la escala)
está mal formulado y la novela entera requiere reconsideración,
se suspende la escritura, se corrige la Capa 1, y el reinicio
de escritura no cuenta como reescritura sino como refundación.

Si WORLD_ARC.md activo, la excepción se extiende: si durante la
escritura se detecta que el arco de mundo declarado tiene
forma dramática inadecuada para el efecto temático buscado, o
que los principios de neutralización elegidos no funcionan
operativamente, la corrección de WORLD_ARC.md también puede
disparar refundación parcial. La distinción entre refundación y
reescritura sigue siendo la misma: si la corrección obliga a
revisar capítulos ya escritos para que respeten el nuevo
diseño, es refundación parcial; si la corrección solo afecta a
capítulos no escritos todavía, es ajuste prospectivo y no
detiene la escritura.

---

## REPOSO OBLIGATORIO

Antes de la primera pasada de revisión: reposo.
El borrador debe estar guardado, sin abrir, durante un
período que permita al autor leerlo como lector.

Duración recomendada:
- Novela corta: 3-4 semanas.
- Novela media: 4-6 semanas.
- Novela larga: 6-8 semanas.

Sin reposo, la memoria de escritura contamina la lectura.
Se sigue "recordando lo que quisiste escribir" en vez de
"leer lo que escribiste".

El reposo puede ser trabajado (otro proyecto) o inactivo;
la exigencia es no abrir el manuscrito.

---

## TIPOS DE PASADA

Las pasadas se ejecutan en orden. Saltarse orden es el error
más común.

### PASADA 1 — ESTRUCTURAL
Eje: la novela entera como sistema.

Se verifica:
- ¿La pregunta central escala sin diluirse de principio a fin?
- ¿La plantilla estructural declarada en STORY_SPINE se
  cumple o se ha desviado? Si se desvió, ¿el resultado es
  mejor o peor?
- ¿Los arcos de CHARACTER_PHYSICS llegan a sus fases
  previstas en momentos estructurales coherentes?
- ¿Las deudas narrativas se abren y cierran en el calendario
  adecuado?
- ¿La escala real (longitud, densidad) coincide con la
  declarada en SCALE_CALIBRATION?

Si WORLD_ARC.md activo, la PASADA 1 incorpora auditoría
específica del arco de mundo. La auditoría reproduce los cinco
tests de funcionamiento declarados en WORLD_ARC.md sección
TESTS DE FUNCIONAMIENTO, aplicados sobre el primer borrador
completo del libro:

**Auditoría 1 — Subordinación temática (Test 1 de WORLD_ARC).**
¿La pregunta central permanece irresuelta tras el cierre del
libro auditado? Si el libro auditado es el último de la saga,
¿permanece irresuelta tras el cierre completo? Auditoría
binaria. Si falla (un lector razonable concluye que la
pregunta central tiene respuesta porque el mundo demostró X o
Y), el arco de mundo está resolviendo la pregunta por vía
macro y conviene revisar:
- Principios de neutralización declarados en WORLD_ARC.md
  sección INTERACCIÓN CON LA PREGUNTA TEMÁTICA: ¿se aplicaron
  efectivamente capítulo a capítulo o quedaron como
  declaración formal sin ejecución?
- Manifestaciones de eje en capítulos donde el cruce con la
  pregunta era denso: ¿alguna escena cristaliza respuesta sin
  que ningún principio de neutralización lo haya impedido?
- Ajuste correctivo: típicamente reescritura de las escenas
  donde la cristalización ocurre, no del arco entero.

**Auditoría 2 — Reproducción funcional (Test 2 de WORLD_ARC).**
Aplicable solo si la forma dramática declarada es ciclo con
variación. ¿La función sistémica de cada eje declarada en
WORLD_ARC.md sección INVENTARIO DE EJES se preserva en estado
final del libro auditado? Si el libro es el último, ¿la
función se preserva en estado final de la saga? Si falla, el
ciclo se ha convertido en escalada por descuido. Cruzar con
REGISTRO 10 de CONTINUITY_PHYSICS: el estado actual de cada
eje al cierre del libro debe coincidir con el estado
declarado en WORLD_ARC.md. Si discrepa, decidir si la
discrepancia es desviación intencional (actualizar
WORLD_ARC.md) o descuido a corregir (reescribir capítulos
donde la función se quebró).

**Auditoría 3 — Asimetría intensidad escénica (Test 3 de
WORLD_ARC).** ¿La jerarquía declarada entre arcos personales
y arco de mundo en WORLD_ARC.md sección DECLARACIÓN DE
ESTRUCTURA DEL ARCO DE MUNDO subsección JERARQUÍA DE
INTENSIDAD ESCÉNICA se mantiene en muestra de capítulos del
libro? Cruzar con TEST 5 de cada CHAPTER_BRIEF.md (que ya
auditó intensidad escena por escena) y con REGISTRO 10 de
CONTINUITY_PHYSICS (que registró la intensidad aplicada a
cada manifestación). Si algún capítulo invirtió la jerarquía
sin declarar excepción contextual, decidir: corregir la
escena o registrar la excepción retroactivamente como
patrón emergente que conviene declarar (decisión autoral).

**Auditoría 4 — Coherencia de deudas y promesas de mundo
(Test 4 de WORLD_ARC).** ¿Las deudas de mundo abiertas se
pagan en el calendario declarado en WORLD_ARC.md sección
DEUDAS DE MUNDO subsección CALENDARIO DE PAGOS? ¿Las promesas
sobre el mundo (cumplir, subvertir, neutralizar) se entregan
según clasificación declarada en WORLD_ARC.md sección
PROMESAS AL LECTOR SOBRE EL MUNDO? Si falla, hay deuda en
olvido o promesa traicionada. Cruzar con extensión deudas de
mundo del REGISTRO 7 de CONTINUITY_PHYSICS, que registró
estado actualizado capítulo a capítulo. Salidas legítimas:
pagar tarde la deuda olvidada, declarar como no-cierre
consciente, reabrir promesa con consulta autoral.

**Auditoría 5 — Articulación inadecuada (Test 5 de
WORLD_ARC).** Aplicable solo si el proyecto declara patrones
del arco de mundo que no deben articularse por personajes ni
narrador (por ejemplo: efectos que dependen de no-articulación
para sostener la pregunta central irresuelta). ¿Algún
capítulo permite leer la articulación? Auditoría binaria. Si
falla, el efecto colapsa y conviene reescribir el pasaje
donde la articulación se filtra.

**Auditoría 6 — Coherencia con archivos de capa 1 modificados
para WORLD_ARC.** Verificación de que el cumplimiento del
arco en el manuscrito coincide con lo registrado en las
plantillas que aterrizan WORLD_ARC en sus dimensiones
específicas:
- SERIES_ARCHITECTURE.md: paralelismo, deudas e inventarios
  diferenciados, asimetría puntos de no retorno.
- THEMATIC_ENGINE.md: subordinación, principios de
  neutralización, resonancias mundo-motivo.
- WORLD_TEXTURE.md: complementariedad estado vs proceso, no
  solapamiento de inventarios.
- CHARACTER_PHYSICS.md: tabla de cruces POV × ejes, función
  reveladora, asimetría temporal por POV.
- NARRATIVE_CHRONOLOGY.md: eventos del arco en las cuatro
  capas, campo TIPO en unidad de registro.
- INFORMATION_CHOREOGRAPHY.md: hechos de rango de mundo,
  cadencia multilibro, calendario maestro extendido.
- STORY_SPINE.md: siembras del arco de mundo como anclajes
  multilibro, regla de marginalidad.

Si alguna plantilla de capa 1 declara contenido relacionado
con WORLD_ARC pero el manuscrito no lo refleja (por ejemplo:
THEMATIC_ENGINE declara una resonancia diseñada que no se
produce en el texto), se documenta la incoherencia y se
decide: actualizar la plantilla (decisión autoral), corregir
el manuscrito, o registrar la desviación como cambio
consciente respecto al diseño inicial.

Salida de esta pasada:
- Lista de cambios estructurales necesarios: capítulos a
  reescribir, eliminar, añadir, fusionar, mover.
- Si WORLD_ARC.md activo, lista adicional de ajustes
  específicos del arco de mundo: deudas de mundo a pagar
  tarde o declarar como no-cierre, manifestaciones a corregir,
  resonancias mundo-motivo accidentales no funcionales a
  modular, principios de neutralización a aplicar
  retroactivamente en escenas detectadas con cristalización.
- No se reescriben párrafos todavía.

### PASADA 2 — DE ARCO Y COHERENCIA
Eje: personajes, relaciones, motivos.

Se verifica:
- Cada personaje con física completa: ¿su arco es legible de
  principio a fin sin saltos inexplicables?
- Cada relación con ficha: ¿sus inversiones de asimetría
  están marcadas?
- Los motivos recurrentes: ¿aparecen el número de veces
  previsto, distribuidos con cadencia?
- La cronología de la fábula es coherente (cruzar con
  NARRATIVE_CHRONOLOGY).
- La información al lector sigue la cadencia diseñada
  (cruzar con INFORMATION_CHOREOGRAPHY).

Si WORLD_ARC.md activo:
- Cada motivo recurrente con resonancia mundo-motivo
  declarada en THEMATIC_ENGINE.md sección RESONANCIAS ENTRE
  EVENTOS DE MUNDO Y MOTIVOS: ¿la resonancia se ejecuta en
  el texto donde se declaró, con la intensidad adecuada?
  ¿Alguna aparición de motivo coincide con manifestación de
  eje sin haber sido declarada como resonancia (riesgo de
  resonancia accidental)?
- La cadencia de hechos de rango de mundo declarada en
  INFORMATION_CHOREOGRAPHY.md sección HECHOS DE RANGO DE
  MUNDO se cumple capítulo a capítulo.
- La asimetría temporal por POV declarada en
  CHARACTER_PHYSICS.md sección CRUCES POV × EJES se ejecuta:
  los picos de intensidad de cruce coinciden con los
  capítulos donde el ARCO DE DEFENSA del personaje atraviesa
  fase 2 → fase 3.

Salida:
- Lista de capítulos o escenas que requieren ajuste de
  personaje/relación/motivo.
- Ajustes que pueden ser locales (una escena) o de escena
  añadida.
- Si WORLD_ARC.md activo, ajustes específicos en escenas
  donde resonancia mundo-motivo declarada no se ejecutó o
  resonancia accidental no funcional al efecto temático
  necesita modulación.

### PASADA 3 — DE VOZ
Eje: la voz narradora.

Se verifica:
- Unidad de voz: ¿la voz del cap. 3 y del cap. 30 son
  reconociblemente del mismo narrador?
- En multi-POV: ¿cada voz es estable en su idiolecto?
- Tonalidad según régimen declarado en AESTHETIC_REGISTER.
- Puntos ciegos del narrador respetados.
- No-fiabilidad (si declarada) funcionando consistentemente.

Salida:
- Pasajes donde la voz se "sale" y requieren reescritura de
  línea.
- Zonas donde la voz se empobrece (fatiga de escritura).

### PASADA 4 — DE LÍNEA
Eje: la frase. Trabajo fino.

Se verifica:
- Longitudes de frase dentro de rango declarado.
- Densidad de adjetivación dentro de rango.
- Aplicación de SEMANTIC_OMISSION (modulada por régimen).
- Verificación de DIALOGUE_MECHANICS.
- Música de la prosa (ver PROSODY_AND_MUSIC.md).
- Detalles sensoriales revisados (ver SENSORY_HIERARCHY).

Salida:
- Reescritura de línea en todo el manuscrito.
- Eliminación de exceso, precisión de detalle.

### PASADA 5 — DE PROOFS
Eje: corrección.

Se verifica:
- Ortografía, puntuación, tipografía.
- Nombres, fechas, datos de mundo.
- Coherencia cronológica final (cruce con NARRATIVE_CHRONOLOGY
  y CONTINUITY_PHYSICS).
- Unidad tipográfica (diálogos, cursivas, comillas).

Salida:
- Manuscrito limpio.

---

## ORDEN OBLIGATORIO DE PASADAS

1 → 2 → 3 → 4 → 5.

Entre cada pasada: reposo mínimo recomendado (días, no
semanas, excepto entre 1 y 2 que suele requerir más).

### POR QUÉ EL ORDEN IMPORTA
- Reescribir una frase (pasada 4) en una escena que luego se
  elimina (pasada 1) es trabajo perdido.
- Revisar voz (pasada 3) antes de fijar arco (pasada 2)
  confunde problemas de voz con problemas de personaje.
- Corrección (pasada 5) al final porque los cambios anteriores
  introducen errores nuevos.

### CUÁNDO ROMPER EL ORDEN
Sólo si en una pasada tardía se detecta un problema
estructural mayor. En ese caso, se retrocede: se vuelve a
la pasada pertinente, se ejecuta el ajuste, y las pasadas
posteriores se rehacen sobre el material modificado.

---

## OPERACIÓN E — LECTURA COMPLETA HOLÍSTICA

La OPERACIÓN D (auditoría cada 3-5 capítulos) es fiscal:
revisa registros. No es lectura.

La OPERACIÓN E es lectura, de principio a fin, en modo lector.
Se ejecuta al menos dos veces:

### OPERACIÓN E-1 (entre pasada 2 y pasada 3)
Propósito: experimentar la novela como lector tras las
correcciones estructurales y de arco.
Modo: lectura corrida en lo posible.
No se editan líneas; se anotan impresiones: dónde aburre,
dónde acelera, dónde se pierde, dónde resplandece.
Salida: lista de zonas que necesitan trabajo de línea con
prioridad en pasada 4.

### OPERACIÓN E-2 (tras pasada 4, antes de pasada 5)
Propósito: leer el manuscrito pulido como un todo.
Detectar: fatiga, desequilibrios de peso, pasajes que siguen
sin funcionar.
Si la E-2 descubre problema mayor, se retrocede.
Si no, se pasa a proofs.

### FRECUENCIA DE OPERACIÓN E DURANTE ESCRITURA
Una versión simplificada puede ejecutarse tras completar
aproximadamente el 50% del borrador (lectura completa de lo
escrito hasta ese momento) y aproximadamente el 100% (antes
del reposo y la pasada 1).

---

## CRITERIO DE TERMINACIÓN

Señales de que la novela está terminada (válido cualquiera,
idealmente varios):

- La pasada 4 produce muy pocos cambios respecto a la 3.
- La OPERACIÓN E-2 no detecta problemas mayores.
- El autor releé y ya no sabe qué cambiar (distinto de "estoy
  cansado y no veo más").
- Los tests de los archivos de Capa 1 (TESTS DE FUNCIONAMIENTO
  de THEMATIC_ENGINE, STORY_SPINE, etc.) pasan.

Señales de que NO está terminada, aunque parezca:
- Los últimos cambios son añadidos de "protección" (aclarar
  lo que ya se entendía, explicar lo que funcionaba).
- El autor siente que podría reescribirse de nuevo y sería
  distinto pero no mejor.
- Hay un capítulo o sección que el autor evita releer.

En caso de dudas: OPERACIÓN E extra.
En caso de parálisis: reposo extendido y decisión: terminar o
identificar el problema concreto.

---

## REESCRITURA CON CAPÍTULOS POSTERIORES YA ESCRITOS

Problema específico: reescribir el capítulo 4 cuando el 5-35
ya existen.

### PROTOCOLO
1. Identificar todos los elementos del cap. 4 que son usados
   en capítulos posteriores. Herramienta principal:
   CONTINUITY_PHYSICS.
2. Clasificar los cambios propuestos:
   - Cambios que no afectan elementos usados después:
     reescribir libremente.
   - Cambios que afectan elementos usados después: registrar
     el impacto y propagar.
3. Propagación: toda reescritura de cap. 4 que modifique un
   elemento activo en, por ejemplo, cap. 17, obliga a revisar
   cap. 17.
4. Si la propagación se extiende a muchos capítulos, la
   pasada se convierte en pasada estructural (vuelta a
   pasada 1 en esa zona).

### CASO PELIGROSO
El cambio propuesto parece local pero altera el estado
emocional de salida del capítulo, que es el de entrada del
siguiente. Pequeño cambio, gran propagación.
Verificar siempre temperatura de salida y bisagra.

---

## GESTIÓN DE VERSIONES

### PRINCIPIO
Cada pasada se guarda como versión numerada.
Cambios grandes en pasada 1: guardar versión previa completa.

### MATERIAL DESCARTADO
Capítulos o escenas eliminadas se guardan en un "archivo
muerto" con fecha y razón.
No se eliminan definitivamente hasta el cierre del proyecto.
A veces el material descartado vuelve a ser útil (en libro
siguiente de serie, por ejemplo) o en otra pasada se ve que
la eliminación fue error.

---

## FEEDBACK EXTERNO

Esta sección cubre la entrada de comentarios externos al
manuscrito (lectores beta, editores, miembros de taller,
agentes literarios) en el protocolo de revisión. El protocolo
de pasadas declarado arriba describe la operación interna del
autor sobre su propio texto; los comentarios externos son
input adicional que entra al protocolo sin alterarlo. La
disciplina central es procesar el feedback sin que la voz de
los comentaristas contamine el manuscrito.

### TIPOS DE FEEDBACK

Cuatro tipos de feedback externo, cada uno con función propia
y momento de aplicación recomendado.

**LECTORES BETA DE CONFIANZA.** Varios lectores (típicamente
dos a cinco) que leen una versión avanzada del manuscrito.
Función: detectar dónde la novela funciona y dónde falla
desde la posición del lector real, sin consideraciones
profesionales. Momento recomendado: entre PASADA 2 y PASADA
3, o entre PASADA 3 y PASADA 4. La elección de lectores beta
es decisión autoral: lectores ideales son los que leerían el
libro publicado, no los que el autor quisiera impresionar.

**EDITOR PROFESIONAL.** Un único lector con experiencia
editorial sobre una versión casi final. Función: detectar
problemas que el autor y los lectores beta no captan por
familiaridad o por falta de oficio. Momento recomendado:
tras PASADA 4, antes de PASADA 5. El editor profesional es
el feedback más caro y más concentrado; conviene aprovecharlo
sobre versión madura, no sobre borrador.

**TALLER LITERARIO.** Varios lectores en formato de discusión
colectiva, sobre versión intermedia (capítulos sueltos o
fragmento). Función: detectar problemas de prosa y voz por
contraste con otras prácticas. Riesgo: el taller tiende a
producir consenso que puede empujar el manuscrito hacia
medianía estética. Momento recomendado: durante el primer
borrador o entre PASADA 1 y PASADA 2; no en fases avanzadas
donde la convergencia con consenso de taller dañaría la
singularidad de la voz.

**AGENTE LITERARIO.** Un único lector con perspectiva de
mercado, sobre versión presentable. Función: detectar
problemas de viabilidad comercial, posicionamiento, expectativa
de género. Momento recomendado: tras PASADA 5, antes de
envío. El agente no opera dentro del protocolo de revisión
estética; opera sobre el manuscrito ya cerrado.

### ENTRADA DE COMENTARIOS

Procedimiento por el cual los comentarios se reciben y
procesan, sin aplicarlos al calor del momento.

**No aplicar al recibir.** El primer impulso al recibir
feedback (especialmente si contradice lo que el autor cree
sobre su libro) es aplicar inmediatamente o rechazar
inmediatamente. Ambas reacciones son sesgo del momento. El
procedimiento exige reposo entre recepción y aplicación:
mínimo veinticuatro horas para feedback ligero, mínimo una
semana para feedback estructural.

**Agrupar por tipo.** Los comentarios se clasifican antes de
procesarlos: estructurales (afectan diseño general),
de personaje (afectan arcos o coherencia psicológica), de
voz (afectan tonalidad o idiolecto), de prosa de línea
(afectan frase, ritmo, léxico), de sentido (afectan claridad
o ambigüedad de pasajes específicos). Un comentario puede
abarcar varios tipos; se desdobla.

**Descartar conscientemente.** No todo comentario merece
aplicación. La razón del descarte se documenta brevemente:
"problema percibido por el lector que el diseño exige
mantener", "preferencia personal del comentarista", "lectura
mal informada del fragmento", "diagnóstico correcto pero
solución propuesta equivocada". Documentar el descarte evita
que el comentario reaparezca en pasadas posteriores como
duda residual.

### ASIGNACIÓN A PASADA

Cada tipo de comentario se procesa en la pasada del protocolo
de revisión que le corresponde, no en pasada anterior ni
posterior. Aplicar comentario estructural en PASADA 4 produce
parche sobre estructura defectuosa; aplicar comentario de
prosa en PASADA 1 produce trabajo de línea sobre escena que
puede eliminarse.

- Comentarios estructurales → PASADA 1.
- Comentarios sobre personaje, relación o motivo → PASADA 2.
- Comentarios sobre voz narradora, idiolecto, tonalidad →
  PASADA 3.
- Comentarios sobre prosa de línea, ritmo, léxico → PASADA 4.
- Comentarios sobre coherencia final, datos, ortografía →
  PASADA 5.

Si la recepción del feedback ocurre tras una pasada que ya
debería haberlo procesado, se retrocede a esa pasada con
disciplina (ver sección ORDEN OBLIGATORIO DE PASADAS,
subsección CUÁNDO ROMPER EL ORDEN). No se aplica el comentario
en pasada posterior por ahorro de trabajo.

Comentarios que no encajan en ninguna pasada (sugerencias
sobre la pregunta central, sobre el régimen estético, sobre
la escala) se evalúan como decisiones autorales fuera del
protocolo de revisión. Pueden producir corrección de archivo
de Capa 1 (refundación según excepción declarada arriba) o
descarte por incompatibilidad con el diseño.

### RIESGO DE CONTAMINACIÓN DE VOZ

La voz de los comentaristas no debe entrar al manuscrito.
Aplicar literalmente sugerencias de comentaristas contamina
la voz del libro con voces ajenas; el manuscrito empieza a
sonar a compromiso entre voces externas en lugar de a su
propio narrador.

El procedimiento es: el autor procesa el comentario, decide
qué hacer, y escribe la modificación con su propia voz.
"Falta una escena de transición aquí" no se resuelve copiando
la transición que el comentarista propone; se resuelve
escribiendo la transición que el libro pide, en la voz del
libro.

Casos especialmente peligrosos: comentarios que proponen
diálogo concreto, comentarios que reescriben fragmentos para
ilustrar la sugerencia, comentarios que aportan léxico
específico ("esta palabra funciona mejor que aquella"). En
todos estos casos, la sugerencia se procesa como diagnóstico
("hay un problema en este pasaje") pero la solución la genera
el autor desde dentro de la voz del libro.

### REGLA DE LA MAYORÍA QUE NO ES MAYORÍA

Si varios comentaristas señalan el mismo problema, hay alta
probabilidad de problema real. Es señal fiable: la convergencia
de lectores no profesionales en un mismo punto rara vez es
casualidad.

Si un solo comentarista lo señala, evaluar si es percepción
legítima o gusto particular. La distinción operativa: la
percepción legítima describe efecto sobre el lector ("aquí
me perdí", "aquí dejé de creer al personaje"); el gusto
particular prescribe solución basada en preferencia
("preferiría que esta escena fuera más breve", "este
personaje debería ser más simpático").

Pero la mayoría puede equivocarse. Cuando varios comentaristas
señalan un problema cuya corrección destruiría algo esencial
del libro, la decisión final es del autor: documentar la
discrepancia, mantener el diseño, asumir el coste de que
algunos lectores reaccionarán como reaccionaron los
comentaristas.

### TEST DE FEEDBACK PROCESADO

Tras procesar todos los comentarios externos asignados a una
pasada, antes de cerrar la pasada, ejecutar verificación:

- ¿La voz del libro sigue siendo la del autor o se ha
  desplazado hacia un compromiso entre voces externas?
- ¿Las modificaciones aplicadas se integran con la voz
  preexistente o suenan como injertos?
- ¿Algún pasaje modificado a partir de feedback queda
  identificable como tal en relectura?

Si la voz se ha desplazado, retroceder a las modificaciones
aplicadas y reescribirlas desde la voz del libro. Si los
injertos persisten, el feedback fue mal procesado y conviene
revisar la asignación a pasada o la decisión de aplicación.

---

## TESTS DE FUNCIONAMIENTO DEL PROTOCOLO

TEST 1 — ORDEN
¿Se han ejecutado las pasadas en orden 1→5 sin saltar?
Si sí, pasadas posteriores heredan base estable.

TEST 2 — REPOSO CUMPLIDO
¿El reposo previo a la pasada 1 respetó el mínimo?

TEST 3 — OPERACIÓN E EJECUTADA
¿La novela se leyó entera al menos dos veces (E-1 y E-2)?

TEST 4 — COHERENCIA POST-REESCRITURA
Tras cada pasada: ¿CONTINUITY_PHYSICS se actualizó con los
cambios? Si no, la pasada introduce agujeros.

TEST 5 — AUDITORÍA DEL ARCO DE MUNDO COMPLETADA (si WORLD_ARC.md activo)
¿Las seis auditorías de la PASADA 1 (subordinación temática,
reproducción funcional, asimetría intensidad escénica,
coherencia de deudas y promesas, articulación inadecuada,
coherencia con archivos de capa 1 modificados) están
ejecutadas y documentadas? Si alguna quedó pendiente, la
PASADA 1 no está completa y las pasadas posteriores heredan
posibles desviaciones del arco no detectadas.

---

## ERRORES FRECUENTES

### ERROR 1 — EMPEZAR POR LA PASADA 4
"Sólo quiero corregir líneas." El resultado es prosa pulida
sobre estructura defectuosa. El lector detecta lo segundo,
no aprecia lo primero.

### ERROR 2 — INFINITAS PASADAS
La novela se reescribe indefinidamente sin criterio de cierre.
Aplicar criterio de terminación con disciplina.

### ERROR 3 — SALTAR EL REPOSO
"Conozco la novela, no necesito reposo." El reposo no es
para conocerla: es para poder olvidar lo que se quiso escribir
y leer lo que se escribió.

### ERROR 4 — NO PROPAGAR CAMBIOS
Se reescribe un capítulo y no se revisan los posteriores que
dependen de él. Incoherencias aparecen tarde.

### ERROR 5 — LECTURA FRAGMENTADA EN LUGAR DE OPERACIÓN E
Leer capítulo por capítulo con correcciones de línea no
sustituye a la lectura corrida. La experiencia del ritmo solo
emerge en lectura continua.

---

## RELACIÓN CON OTROS ARCHIVOS

REVISION_PROTOCOL.md consulta todos los demás archivos, pero
en distinto orden según pasada:

- Pasada 1: THEMATIC_ENGINE, STORY_SPINE, CHARACTER_PHYSICS,
  SCALE_CALIBRATION, SERIES_ARCHITECTURE (si aplica),
  WORLD_ARC (si aplica). Si WORLD_ARC activo, además
  WORLD_TEXTURE, NARRATIVE_CHRONOLOGY,
  INFORMATION_CHOREOGRAPHY y CONTINUITY_PHYSICS REGISTRO 10
  como insumos para las seis auditorías específicas del arco.
- Pasada 2: CHARACTER_PHYSICS, RELATIONSHIP_PHYSICS,
  CONTINUITY_PHYSICS, NARRATIVE_CHRONOLOGY,
  INFORMATION_CHOREOGRAPHY, THEMATIC_ENGINE (motivos y, si
  WORLD_ARC activo, resonancias mundo-motivo).
- Pasada 3: VOICE_ARCHITECTURE, AESTHETIC_REGISTER.
- Pasada 4: SEMANTIC_OMISSION, DIALOGUE_MECHANICS,
  SUBTEXT_MECHANICS, SENSORY_HIERARCHY, PROSODY_AND_MUSIC,
  AESTHETIC_REGISTER (moduladora).
- Pasada 5: CONTINUITY_PHYSICS, NARRATIVE_CHRONOLOGY (para
  coherencia final).

REVISION_PROTOCOL.md alimenta:
- Actualizaciones finales de CONTINUITY_PHYSICS y
  NARRATIVE_CHRONOLOGY tras cada pasada.
- Revisión final de SERIES_ARCHITECTURE si el libro pertenece
  a una serie.
- Si WORLD_ARC.md activo: actualizaciones de WORLD_ARC.md
  cuando la PASADA 1 detecta desviaciones cuya salida
  legítima es actualizar el archivo (decisiones autorales
  sobre forma dramática, principios de neutralización
  ejecutables, asimetría puntos de no retorno, no-cierre
  consciente de deudas de mundo).

La sección FEEDBACK EXTERNO de este archivo introduce
coordinaciones específicas con archivos del catálogo según
la asignación a pasada de los comentarios:
- VOICE_ARCHITECTURE.md: riesgo central de contaminación de
  voz por aplicación literal de sugerencias externas;
  comentarios sobre voz narradora, idiolecto y tonalidad se
  asignan a PASADA 3 sobre la voz declarada en este archivo.
- CHARACTER_PHYSICS.md y RELATIONSHIP_PHYSICS.md: comentarios
  sobre personaje, relación o motivo se asignan a PASADA 2
  sobre las fichas y dinámicas declaradas en estos archivos.
- PROSE_LINE_DISCIPLINE.md: comentarios sobre prosa de línea,
  ritmo o léxico se asignan a PASADA 4 sobre las cuotas
  globales y los siete tics anti-LLM declarados allí.
- DIALOGUE_MECHANICS.md: comentarios que proponen diálogo
  concreto se procesan como diagnóstico, con la solución
  generada por el autor desde dentro de la voz del libro.
- AESTHETIC_REGISTER.md y THEMATIC_ENGINE.md: comentarios
  sobre régimen estético o sobre pregunta central no encajan
  en pasada y se evalúan como decisiones autorales fuera del
  protocolo, pudiendo producir refundación de Capa 1 según
  la excepción declarada arriba.

---

## NOTA FINAL

Este protocolo es exigente. Aplicado con disciplina, transforma
un primer borrador sólido en una novela publicable. Aplicado
parcialmente, deja hoyos que el lector final detecta.

La resistencia al protocolo suele disfrazarse de intuición
("esta pasada no la necesito"). Es rara la novela que
realmente no la necesita. Si en duda, aplicar.


---
---

