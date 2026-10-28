<!-- MODELO_DarkRomance v2.0 — CONTINUITY_PHYSICS: base agnóstica v7 (verbatim) + adenda de dark romance (v2.0) -->

# CONTINUITY_PHYSICS.md

## PROPÓSITO

Este archivo es la memoria operativa del sistema. Es donde se
registra, capítulo a capítulo, qué ha cambiado en cada uno de los
ejes del mundo narrativo. Sin este registro, el sistema reescribe
desde cero cada capítulo y pierde coherencia acumulada.

Es el archivo más largo en ejecución porque crece con la novela.
Su estructura es la de una base de datos ligera.

DISTINCIÓN OPERATIVA IMPORTANTE:
CONTINUITY_PHYSICS es RETROSPECTIVO: registra lo que ya ha
ocurrido en el relato escrito.
NARRATIVE_CHRONOLOGY es más amplio y contiene la fábula completa
(incluida pre-narrativa, invisible y proyectada).
INFORMATION_CHOREOGRAPHY es PROSPECTIVO: diseña el calendario
de revelación antes de que se cumpla.

Los tres archivos deben mantenerse coordinados. CONTINUITY es
el espejo de la ejecución.

Si WORLD_ARC.md está activo en el proyecto (sagas multivolumen
con mundo evolutivo de carga temática), CONTINUITY_PHYSICS
incorpora una dimensión adicional: registro retrospectivo de
manifestaciones del arco de mundo en los capítulos escritos. Esa
dimensión se cruza con NARRATIVE_CHRONOLOGY (que registra eventos
del arco en sus cuatro capas temporales, no solo en la capa
visible) y con WORLD_ARC.md (que declara la trayectoria diseñada
por libro). CONTINUITY es el registro de lo ejecutado en el
relato escrito; el cruce con WORLD_ARC permite auditar si la
ejecución sigue o se desvía de la trayectoria diseñada.

JERARQUÍA: Capa 2 transversal (memoria retrospectiva del sistema).
No tiene contenido dramático propio; sincroniza todos los demás
archivos.

---

## ESTRUCTURA GENERAL

El archivo contiene nueve registros base. Cada uno se actualiza en
OPERACIÓN C (al cerrar un capítulo).

1. REGISTRO DE TIEMPO (cronología)
2. REGISTRO DE LUGAR
3. REGISTRO DE ESTADO DE PERSONAJES (física interna)
4. REGISTRO DE COSTE ACUMULADO POR PERSONAJE
5. REGISTRO DE VECTORES DE RELACIÓN
6. REGISTRO DE INFORMACIÓN POR POV (quién sabe qué)
7. REGISTRO DE DEUDAS NARRATIVAS
8. REGISTRO DE TENSIÓN Y DESCARGAS
9. REGISTRO DE MOTIVOS RECURRENTES

Si WORLD_ARC.md activo, se añade un décimo registro:

10. REGISTRO DE MANIFESTACIONES DEL ARCO DE MUNDO (condicional)

Los registros 6, 7 y 9 incorporan también extensiones específicas
para el arco de mundo cuando WORLD_ARC.md está activo. Estas
extensiones se documentan dentro de la sección de cada registro,
no como registros separados.

---

## 1. REGISTRO DE TIEMPO

Cronología interna de la novela. Permite verificar que las
escenas son compatibles con los días transcurridos.

FORMATO:
CAPÍTULO [N]: [fecha/día dentro del mundo + duración
transcurrida desde el capítulo anterior].
CAMBIOS DE FECHA DENTRO DEL CAPÍTULO: [si hay saltos internos,
registrarlos].

Ejemplo:
CAP. 1: Día 1, mañana. (Apertura de la novela.)
CAP. 2: Día 1, tarde. (3 horas después.)
CAP. 3: Día 3, mañana. (Elipsis de 1 día.)

NOTA: si la novela usa tiempo no lineal, registrar tanto el
tiempo del relato como el tiempo del suceso.

### USO
Antes de escribir un capítulo: consultar fecha de entrada.
Después de escribir: actualizar fecha de salida.

### VERIFICACIÓN
Al llegar al final del acto II, revisar que el tiempo transcurrido
es coherente. Personajes que envejecen 20 años en dos capítulos,
eventos climáticos que duran demasiado, duelos físicos que
retroceden sin justificación.

---

## 2. REGISTRO DE LUGAR

Dónde está cada personaje al final de cada capítulo.

FORMATO:
CAPÍTULO [N] — Cierre:
- [Personaje A]: [lugar]
- [Personaje B]: [lugar]
...

Cambios de lugar dentro del capítulo: indicar brevemente
("cap. 5: A parte de Cádiz → llega a Gibraltar").

### USO
Evitar que un personaje "aparezca" en otra escena sin viaje
verosímil. Especialmente útil en novela con trayectos largos
(naval, carretera, de viaje).

---

## 3. REGISTRO DE ESTADO DE PERSONAJES

Estado interno de cada personaje con física completa.

FORMATO por personaje:
- FASE ACTUAL DEL ARCO DE DEFENSA: [1, 2, 3 o 4; ver
  CHARACTER_PHYSICS.md]
- MECANISMO DE DEFENSA: [activo / en fallo / en colapso /
  post-colapso]
- DESEO SUPERFICIAL ACTIVO: [formulación en este momento]
- SABE / NO SABE SU DESEO PROFUNDO: [sí / no / lo intuye]

ACTUALIZACIÓN:
Al terminar un capítulo, si la fase o el estado del mecanismo
cambia, registrar. En capítulos donde no cambia, registrar igual
para marcar continuidad.

### CRUCE
Este registro es el que permite, en OPERACIÓN D, decir
objetivamente si el arco está avanzando o estancado. Si el
personaje está en FASE 1 al capítulo 3 y al capítulo 18 sigue
en FASE 1, hay problema estructural.

---

## 4. REGISTRO DE COSTE ACUMULADO POR PERSONAJE

Qué ha perdido cada personaje con física completa, capítulo a
capítulo. Es el indicador real del arco (ver
CHARACTER_PHYSICS.md).

FORMATO:
PERSONAJE [A]:
- CAP. 1: [qué coste concreto se pagó. Ej.: "Primera mentira
  a B; coste: corrosión mínima de la relación."]
- CAP. 3: [...]
- CAP. 5: [...]

COSTE ACUMULADO TOTAL (actualizable):
Lista consolidada que resume qué ha perdido este personaje
desde el inicio.

### USO
En cada capítulo, preguntar: ¿qué paga hoy el protagonista?
Si "nada concreto", la escena probablemente no está haciendo
arco.

### VERIFICACIÓN
El coste debe crecer. Si dos capítulos seguidos no tienen
entrada en este registro para un protagonista, revisar.

---

## 5. REGISTRO DE VECTORES DE RELACIÓN

Por cada relación con ficha en RELATIONSHIP_PHYSICS.md:

FORMATO:
RELACIÓN [A × B]:
- ESTADO AL INICIO: [según ficha de RELATIONSHIP_PHYSICS.md]
- CAP. 2: [qué cambió en el vector. Ej.: "A gana ventaja
  informativa sobre B: ahora sabe de la carta."]
- CAP. 4: [...]
- ASIMETRÍA ACTUAL: [quién está arriba en este momento]
- FUERZAS ACTIVAS: [acercamiento / repulsión: intensidades
  aproximadas]

### USO
Antes de una escena compartida, consultar estado actual.
Después de la escena, registrar cambios.

### VERIFICACIÓN
Vectores que no se mueven en 5+ capítulos: o la relación está
dormida por diseño (aceptable), o la novela la está olvidando
(reabrir).

---

## 6. REGISTRO DE INFORMACIÓN POR POV

Quién sabe qué, cuándo. Crítico en multi-POV y en narraciones
con ironía dramática.

FORMATO:
HECHO [X]:
- OCURRIÓ EN CAP.[N]
- POV QUE LO CONOCE DESDE EL CAP.[N]: [lista de personajes]
- LECTOR LO CONOCE DESDE CAP.[N]: [sí / no / parcialmente]

Ejemplo:
HECHO: "A mintió a B sobre el paradero de C."
- Ocurrió en cap.4.
- A lo sabe (cap.4). C lo sabe (cap.7). B no lo sabe.
- Lector lo sabe desde cap.4.

### USO
- Permite que el narrador no "sepa" lo que el POV no debe saber.
- Permite explotar ironía dramática: el lector sabe lo que el
  POV ignora.
- Permite detectar filtraciones: un personaje no puede usar
  información que su POV no ha recibido.

### ERROR COMÚN QUE EVITA
A actúa en cap.9 como si supiera algo que solo supo en cap.10.
Sin este registro, es fácil cometer este error.

### EXTENSIÓN PARA HECHOS DE RANGO DE MUNDO (si WORLD_ARC.md activo)
Los hechos de rango de mundo (cambios institucionales, colapsos
sistémicos, transformaciones de cosmovisión declarados en
INFORMATION_CHOREOGRAPHY.md sección HECHOS DE RANGO DE MUNDO) se
registran aquí con campo adicional EJE DE MUNDO ASOCIADO. Su
filtrado por POV obedece a la tabla de cruces POV × ejes de
WORLD_ARC.md: solo los POV con cruce significativo
(principal, secundario, estructural-subterráneo) reciben el
hecho de mundo en su línea de información.

FORMATO EXTENDIDO:
HECHO DE MUNDO [X]:
- EJE DE MUNDO ASOCIADO: [identificador del eje]
- OCURRIÓ EN: [cap.N visible / capa 3 narrativa invisible
  simultánea, declarado en NARRATIVE_CHRONOLOGY.md / capa 1
  pre-narrativa, registrada como condición de inicio]
- POV QUE LO CONOCE DESDE EL CAP.[N]: [lista filtrada por
  cruce significativo]
- POV QUE NO LO CONOCEN: [lista, distinguiendo "no aplica
  por marginalidad de cruce" de "aún no han recibido la
  información"]
- LECTOR LO CONOCE DESDE CAP.[N]: [sí / no / parcialmente,
  según fase declarada en INFORMATION_CHOREOGRAPHY.md:
  siembra / eco / sospecha / confirmación / consecuencia]

Ejemplo:
HECHO DE MUNDO: "La cofradía de comerciantes pierde el
monopolio del puerto."
- Eje de mundo asociado: equilibrio económico-portuario.
- Ocurrió en: capa 3 narrativa invisible simultánea, durante
  elipsis entre cap.12 y cap.14 (registrado en
  NARRATIVE_CHRONOLOGY.md).
- POV que lo conoce: D (capitán mercante, cruce principal con
  eje) desde cap.14 por carta recibida; E (juez de cabildo,
  cruce secundario) desde cap.16 por escena directa.
- POV que no lo conoce: A, B, C (cruces marginales con el
  eje; el hecho no llega a su esfera de información).
- Lector lo sabe desde cap.14, fase ECO; confirmación
  programada para cap.20.

---

## 7. REGISTRO DE DEUDAS NARRATIVAS

Sincronizado con STORY_SPINE.md (deudas estructurales) + todas
las deudas locales abiertas durante la escritura.

FORMATO:
DEUDA [ID o descripción]:
- ABIERTA EN CAP.[N]: [cómo se planta el setup]
- ESTADO: [abierta / pagada en cap. X / reprogramada / cerrada
  por descarte]
- FECHA DE PAGO PREVISTA: [capítulo]
- TIPO: [de trama / emocional / relacional / temática /
  informativa]

### USO
Al cerrar cada capítulo, actualizar todas las deudas que se han
pagado o modificado.
Al diseñar un capítulo, consultar deudas próximas a vencer.

### VERIFICACIÓN CRUZADA CON SCALE_CALIBRATION.md
Número de deudas abiertas simultáneamente debe estar en el rango
de la escala declarada. Más: saturación. Menos: novela vacía.

### DEUDAS EN VÍAS DE OLVIDO
Deudas abiertas hace muchos capítulos y aún no pagadas:
riesgo de agujero. Alertar en OPERACIÓN D y decidir: pagar,
recontextualizar, o declarar explícitamente como final abierto.

### EXTENSIÓN PARA DEUDAS DE MUNDO (si WORLD_ARC.md activo)
Las deudas de mundo declaradas en WORLD_ARC.md sección DEUDAS
DE MUNDO se registran aquí con nomenclatura distinguible
(prefijo distinto de las deudas de personaje declaradas en
SERIES_ARCHITECTURE.md, según decisión autoral). Recomendación
operativa: prefijo SP- para deudas de serie de personaje, WA-
para deudas de arco de mundo, DL- o sin prefijo para deudas
locales del libro.

FORMATO EXTENDIDO:
DEUDA DE MUNDO [WA-N]:
- ABIERTA EN: [libro N, cap.M; cómo se planta el setup en
  capa visible o cómo aparece la siembra]
- EJE DE MUNDO: [identificador del eje al que pertenece]
- TIPO DE DEUDA DE MUNDO: [mundo puro / mundo con resonancia
  temática / mundo con resonancia de personaje / mundo con
  resonancia cultural; según WORLD_ARC.md sección DEUDAS DE
  MUNDO]
- LIBRO DE PAGO PREVISTO: [libro N+k]
- ESTADO: [abierta / pagada / reprogramada / declarada
  explícitamente como no-cierre consciente / reedición]
- TIPO DE PAGO APLICADO (si pagada): [cierre completo / cierre
  parcial / no-cierre consciente declarado / reedición]
- CRUCES CON DEUDAS DE PERSONAJE (si los hay): [referencia a
  ID de SERIES_ARCHITECTURE.md sección CRUCES ENTRE DEUDAS DE
  PERSONAJE Y DEUDAS DE MUNDO]

### DEUDAS DE MUNDO EN VÍAS DE OLVIDO
Deudas de mundo abiertas en libro N y cuyo libro de pago
previsto era N+1 o N+2 sin pago registrado son señal específica
distinta de las deudas locales. La auditoría debe distinguir si
la deuda quedó en silencio por diseño (neutralización por
ausencia, declarada en WORLD_ARC.md sección PROMESAS AL LECTOR
SOBRE EL MUNDO subsección NEUTRALIZAR) o por descuido. Si por
descuido, decidir: pagar tarde, declarar como no-cierre
consciente, o reabrir con consulta autoral.

---

## 8. REGISTRO DE TENSIÓN Y DESCARGAS

Estado emocional acumulado del lector, medido por proxy.

FORMATO:
CAPÍTULO [N]:
- TENSIÓN DE ENTRADA: [baja / media / alta / insostenible]
- MECANISMO ACTIVO: [ver TENSION_MECHANICS.md]
- DESCARGA INCLUIDA EN EL CAPÍTULO: [ninguna / parcial / falsa /
  escala / total]
- TENSIÓN DE SALIDA: [baja / media / alta / insostenible]

### USO
Detectar:
- Demasiados capítulos seguidos en "alta" sin descarga:
  fatiga lectora.
- Descarga total antes de clímax: pérdida de potencia.
- Ningún mecanismo activo: escena de transición sin función
  dramática.

### CRUCE CON OPERACIÓN D
Revisar patrones de 5 en 5 capítulos.

---

## 9. REGISTRO DE MOTIVOS RECURRENTES

Para cada motivo declarado en THEMATIC_ENGINE.md:

FORMATO:
MOTIVO [X]:
- APARICIÓN 1 (cap.[N]): [cómo aparece, qué función]
- APARICIÓN 2 (cap.[N]): [variación, eco]
- APARICIÓN 3 (cap.[N]): [cristalización]
- APARICIONES SIGUIENTES (si hay): [...]

### USO
Evitar sobreuso (motivo mencionado demasiadas veces se vuelve
didáctico) y subuso (motivo que aparece una vez y se olvida).

### VERIFICACIÓN
Todo motivo declarado debe tener al menos 3 apariciones
registradas al finalizar la novela. Si no: el motivo no se
construyó.

### EXTENSIÓN PARA RESONANCIAS MUNDO-MOTIVO (si WORLD_ARC.md activo)
THEMATIC_ENGINE.md sección MOTIVOS RECURRENTES subsección
RESONANCIAS ENTRE EVENTOS DE MUNDO Y MOTIVOS declara tres tipos
de resonancia: diseñada (anclaje deliberado), accidental
(coincidencia no diseñada que produce lectura sistémica no
querida), neutralizada (silencio diseñado para evitar
articulación). Cada aparición de motivo cuyo capítulo
también porta manifestación de eje de mundo se registra con
campo adicional RESONANCIA, aplicando una de las tres
declaraciones.

FORMATO EXTENDIDO POR APARICIÓN:
APARICIÓN k (cap.[N]):
- Forma: [cómo aparece el motivo]
- Función: [qué hace en el capítulo]
- RESONANCIA CON ARCO DE MUNDO (si aplica): [diseñada con eje
  X / accidental detectada con eje Y / neutralizada por silencio
  / sin coincidencia con manifestación de eje en este capítulo]

### AUDITORÍA DE RESONANCIAS ACCIDENTALES
Si una aparición de motivo cae sin coincidir con ninguna
declaración previa de THEMATIC_ENGINE.md y al mismo tiempo el
capítulo manifiesta eje de mundo, comprobar si la resonancia
emergente es funcional al efecto temático buscado o si produce
lectura sistémica no querida (típicamente: el motivo, al
coincidir con la manifestación, parece sugerir que el eje de
mundo demuestra empíricamente algo que la pregunta central
debería sostener irresuelto). Si funcional: declararla en
THEMATIC_ENGINE.md. Si no funcional: corregir mediante
modulación del motivo o de la manifestación en el capítulo.

---

## 10. REGISTRO DE MANIFESTACIONES DEL ARCO DE MUNDO (si WORLD_ARC.md activo)

Registro condicional. Solo aplicable si WORLD_ARC.md está activo
en el proyecto. Espejo retrospectivo de la trayectoria diseñada
en WORLD_ARC.md sección ARCO DEL MUNDO POR LIBRO.

Por eje declarado en WORLD_ARC.md sección INVENTARIO DE EJES DE
MUNDO EN MOVIMIENTO:

FORMATO:
EJE [identificador]:
- DOMINANCIA DECLARADA: [dominante / subordinado-sustrato /
  activable puntualmente]
- ESTADO REGISTRADO AL INICIO DEL LIBRO N: [configuración
  concreta tomada del estado declarado en WORLD_ARC.md]
- MANIFESTACIONES REGISTRADAS HASTA EL CAPÍTULO ACTUAL:
  - CAP.[M]: [forma de la manifestación, intensidad escénica
    aplicada (principal / secundario /
    estructural-subterráneo / instrumental / marginal),
    POVs implicados, función reveladora aplicada]
  - CAP.[M+k]: [...]
- ESTADO ACTUAL DEL EJE EN EL LIBRO EN CURSO: [configuración
  tras las manifestaciones registradas hasta el capítulo actual]
- DESVIACIÓN RESPECTO AL ESTADO PROGRAMADO PARA ESTE PUNTO DEL
  LIBRO (según WORLD_ARC.md): [coherente / desviación menor
  declarada / desviación mayor que requiere consulta autoral]
- DEUDAS DE MUNDO ASOCIADAS AL EJE: [cruce con REGISTRO 7
  extensión deudas de mundo]
- SIEMBRAS REGISTRADAS PORTADAS POR ESTE EJE (si libro inicial
  o intermedio): [cruce con WORLD_ARC.md sección SIEMBRAS Y
  ANCLAJES; lista de cap.[M], forma de la siembra, deuda de
  mundo que prepara]

### USO
- Antes de un capítulo cuyo brief declara manifestación de eje
  X, consultar este registro para verificar el estado actual
  del eje y la coherencia con la trayectoria diseñada.
- Después de un capítulo con manifestación, actualizar este
  registro con la entrada nueva.
- En OPERACIÓN D: auditar conjunto de ejes para detectar
  desviaciones acumuladas, ejes silenciados durante demasiados
  capítulos, ejes sobrerrepresentados respecto a otros.

### VERIFICACIÓN
- Cada manifestación declarada en WORLD_ARC.md sección ARCO DEL
  MUNDO POR LIBRO subsección MANIFESTACIONES DURANTE EL LIBRO
  tiene entrada aquí cuando se ha narrado.
- Cada movimiento central declarado en WORLD_ARC.md tiene
  entrada de capítulo donde ocurre.
- El estado actual de cada eje al cierre del libro debe
  coincidir con el estado declarado en WORLD_ARC.md como
  estado al cierre del libro N. Si discrepa, decidir: actualizar
  WORLD_ARC.md (decisión autoral), corregir el manuscrito, o
  documentar la desviación como cambio consciente respecto al
  diseño inicial.

---

## OPERATIVA DEL ARCHIVO

CONTINUITY_PHYSICS.md se actualiza en dos momentos:

### OPERACIÓN C (al cerrar cada capítulo)
Actualizar:
- Tiempo
- Lugar
- Estado de personajes (si hay cambio)
- Coste acumulado (si se pagó algo en este capítulo)
- Vectores de relación (si se movieron)
- Información por POV (nuevos hechos)
- Deudas (abiertas, pagadas, modificadas)
- Tensión y descargas
- Motivos (si aparecieron)

Si WORLD_ARC.md activo, además:
- Hechos de rango de mundo del capítulo (REGISTRO 6 extensión).
- Deudas de mundo abiertas, pagadas o modificadas (REGISTRO 7
  extensión).
- Resonancias mundo-motivo de las apariciones de motivo del
  capítulo (REGISTRO 9 extensión).
- Manifestaciones de eje del capítulo (REGISTRO 10).

### OPERACIÓN D (cada 3-5 capítulos)
Revisar el registro completo:
- ¿Algún arco se está estancando? (ver registros 3 y 4)
- ¿Alguna relación está dormida injustamente? (registro 5)
- ¿Alguna deuda está en vías de olvido? (registro 7)
- ¿El patrón de tensión es saludable? (registro 8)
- ¿Algún motivo está infrausado o sobreusado? (registro 9)

Si WORLD_ARC.md activo, además:
- ¿Algún eje está silenciado durante demasiados capítulos
  respecto al peso declarado en WORLD_ARC.md sección INVENTARIO
  DE EJES (registro 10)?
- ¿Algún eje está sobrerrepresentado respecto a su peso
  declarado, comiendo presencia narrativa de los arcos
  personales (riesgo 5 de WORLD_ARC.md)?
- ¿Alguna deuda de mundo está en vías de olvido o necesita
  declaración explícita de no-cierre consciente (registro 7
  extensión deudas de mundo)?
- ¿La jerarquía de intensidad escénica declarada en WORLD_ARC.md
  se respeta en muestra de capítulos recientes? Auditoría
  cruzada con REGISTRO 10 (intensidad aplicada a cada
  manifestación) y CHAPTER_BRIEF.md de cada capítulo (TEST 5).
- ¿Las resonancias mundo-motivo registradas en REGISTRO 9
  extensión incluyen alguna accidental no funcional al efecto
  temático buscado?

---

## INTEGRIDAD DEL REGISTRO

CONTINUITY_PHYSICS.md es la única fuente de verdad sobre el
estado del mundo. Otros archivos no deben tener sus propios
registros; deben remitirse a este.

Si hay discrepancia entre lo que el texto sugiere y lo que
CONTINUITY_PHYSICS.md registra:
- Si la discrepancia es error de escritura: corregir el texto.
- Si la discrepancia es cambio intencional: actualizar el
  registro y revisar las consecuencias.

No existe tercera opción: "dejarlo ambiguo" produce incoherencias
que se descubren capítulos más tarde.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — RECONSTRUCCIÓN
¿Un lector externo podría, a partir solo de este archivo,
entender en qué punto está la novela? Si no, el registro es
incompleto.

TEST 2 — COHERENCIA CRUZADA
El estado de un personaje en registro 3 debe ser coherente con
sus costes en registro 4 y sus relaciones en registro 5.
Si no: revisar.

TEST 3 — SINCRONIZACIÓN CON SPINE
Las deudas abiertas en registro 7 deben cuadrar con lo previsto
en STORY_SPINE.md. Si hay deudas no previstas acumulándose,
la estructura está desviándose.

TEST 4 — COHERENCIA CON ARCO DE MUNDO (si WORLD_ARC.md activo)
El registro 10 debe ser espejo retrospectivo coherente con la
trayectoria diseñada en WORLD_ARC.md sección ARCO DEL MUNDO POR
LIBRO. Cada manifestación declarada en WORLD_ARC.md tiene
entrada en registro 10 cuando se ha narrado; cada movimiento
central tiene entrada de capítulo donde ocurre; el estado actual
de cada eje al cierre del libro coincide con el estado declarado
en WORLD_ARC.md como estado al cierre de ese libro. Si discrepa,
hay tres salidas legítimas: actualizar WORLD_ARC.md (decisión
autoral declarada), corregir el manuscrito, documentar la
desviación como cambio consciente respecto al diseño inicial.
La cuarta opción ("dejarlo ambiguo") está prohibida también
aquí, como para los registros base.

---

## RELACIÓN CON OTROS ARCHIVOS

CONTINUITY_PHYSICS.md recibe de:
- CHARACTER_PHYSICS.md (estado y coste)
- RELATIONSHIP_PHYSICS.md (vectores)
- STORY_SPINE.md (deudas estructurales)
- THEMATIC_ENGINE.md (motivos, y resonancias mundo-motivo si
  WORLD_ARC.md activo)
- TENSION_MECHANICS.md (patrón de tensión)
- CHAPTER_BRIEF.md (qué cambia en este capítulo)
- INFORMATION_CHOREOGRAPHY.md (qué hechos deben estar en qué
  fase en cada capítulo, incluidos hechos de rango de mundo si
  WORLD_ARC.md activo)
- WORLD_ARC.md (si activo): trayectoria diseñada por libro,
  inventario de ejes, deudas y promesas de mundo, jerarquía de
  intensidad escénica, principios de neutralización. El
  REGISTRO 10 es espejo retrospectivo de esa trayectoria.
- SERIES_ARCHITECTURE.md (si proyecto multivolumen):
  nomenclatura distinguible para deudas de personaje vs deudas
  de mundo en REGISTRO 7; cruces declarados entre ambas en
  SERIES_ARCHITECTURE.md sección DEUDAS DE SERIE subsección
  CRUCES ENTRE DEUDAS DE PERSONAJE Y DEUDAS DE MUNDO.

CONTINUITY_PHYSICS.md alimenta:
- Todo capítulo nuevo (lee estado de entrada).
- OPERACIÓN D (auditoría estructural).
- NARRATIVE_CHRONOLOGY.md (los eventos de capa 2 registrados
  aquí también se anotan en la fábula; si WORLD_ARC.md activo,
  los eventos del arco de mundo que aparecen en capa visible
  se registran aquí y se cruzan con la capa 2 de
  NARRATIVE_CHRONOLOGY).
- WORLD_ARC.md (si activo): el REGISTRO 10 alimenta la
  auditoría conjunta de la trayectoria del arco; las
  desviaciones detectadas aquí son insumo para decisiones
  autorales sobre actualizar WORLD_ARC.md o corregir
  manuscrito.

CONTINUITY_PHYSICS.md se coordina con:
- NARRATIVE_CHRONOLOGY.md (memoria de mundo; más amplia,
  incluye pre-narrativa e invisible). CONTINUITY es el
  subconjunto visible. Si WORLD_ARC.md activo, eventos del
  arco de mundo en capa 3 (narrativa invisible simultánea)
  viven principalmente en NARRATIVE_CHRONOLOGY pero se
  reflejan aquí cuando algún POV los conoce (REGISTRO 6
  extensión).
- INFORMATION_CHOREOGRAPHY.md (prospectivo vs. retrospectivo
  del REGISTRO 6, incluyendo extensión hechos de mundo).

CONTINUITY_PHYSICS.md no tiene contenido propio: es espejo
sincronizado del estado real de la novela escrita.


---
---

