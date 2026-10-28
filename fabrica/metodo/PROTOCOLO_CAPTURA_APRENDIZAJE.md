# PROTOCOLO_CAPTURA_APRENDIZAJE.md — Plantilla operativa

## PROPÓSITO

Este archivo declara el protocolo formal por el cual los proyectos creativos que usan el modelo agnóstico v7 alimentan al modelo con aprendizaje empírico. Sin protocolo, las fricciones detectadas durante la práctica se capturan en formato fragmentario, con contexto específico de cada proyecto, y resultan difíciles de descontextualizar cuando el modelo intenta generalizarlas. Con protocolo, cada fricción produce registro estructurado que el modelo puede procesar limpiamente.

El protocolo cumple la regla 2 del proyecto agnóstico v7 (flujo unidireccional desde proyectos hacia v7) y la regla 3 (inputs aceptados). Los registros generados según este protocolo son el único input que v7 acepta de forma rutinaria. Cualquier otra forma de propuesta de modificación al modelo merece evaluación específica fuera del flujo regular.

---

## CUÁNDO ACTIVAR EL PROTOCOLO

El autor de un proyecto creativo activa el protocolo cuando detecta cualquiera de las cinco situaciones siguientes durante el trabajo con plantillas v7:

**Situación 1 — Fricción operativa.** El autor intenta usar una plantilla y descubre que no contempla algo que necesita. Tiene que improvisar fuera de la plantilla, parchear ad hoc, o rediseñar parcialmente el flujo de trabajo. La plantilla funciona pero no completamente.

**Situación 2 — Deriva del modelo.** El sistema produce decisión que en retrospectiva el autor reconoce como subóptima, y el análisis de por qué pasó revela que alguna plantilla orientó incorrectamente. La plantilla no falló por ausencia sino por dirección equivocada.

**Situación 3 — Hueco estructural.** El autor identifica que falta archivo entero del catálogo, o falta sección entera dentro de archivo existente. No es ausencia menor; es laguna que producirá fricción recurrente en proyectos futuros del mismo tipo.

**Situación 4 — Redundancia o contradicción.** El autor detecta que dos plantillas v7 se solapan en función, o se contradicen en directrices, o producen interpretaciones ambiguas cuando se aplican juntas. La acumulación de archivos ha generado tensión interna no resuelta.

**Situación 5 — Limitación de alcance agnóstico.** El autor detecta que una plantilla, supuestamente agnóstica, en realidad asume implícitamente cierto género o cierta escala o cierta voz, y falla cuando se aplica fuera de esos supuestos. La plantilla no es tan agnóstica como su declaración sugiere.

Las cinco situaciones se distinguen porque producen tipos distintos de modificación en v7. Fricción operativa típicamente produce ajuste menor en plantilla existente. Deriva del modelo produce reformulación de directriz. Hueco estructural produce archivo nuevo o sección nueva. Redundancia produce consolidación. Limitación de alcance produce ampliación o desdoblamiento. Cada tipo merece tratamiento distinto durante el procesamiento.

---

## ESTRUCTURA DEL REGISTRO

Cada activación del protocolo produce un registro con cinco campos. Los registros se acumulan en archivo de bitácora del proyecto v7 (REGISTROS_APRENDIZAJE.md o equivalente, decidido por v7). Cada registro es entre 5 y 20 líneas; suficientemente corto para ser fácil de generar al calor del momento, suficientemente largo para tener contexto cuando se procese.

**Campo 1 — Identificador y fecha.** Numeración secuencial del registro y fecha de captura. El identificador permite cruces y referencias cuando varios registros toquen tema similar.

**Campo 2 — Síntoma observado.** Descripción concreta de qué pasó en el proyecto vivo. Qué archivo se quedó corto, qué decisión tuvo que improvisarse, qué fricción se sintió. Lenguaje específico del proyecto (nombres de personajes, nombres de mundo, decisiones específicas) está permitido aquí porque ayuda a precisar el síntoma. Este campo es testimonio de la experiencia, no análisis.

**Campo 3 — Diagnóstico del modelo.** Análisis de por qué pasó el síntoma desde la perspectiva del modelo. Qué falta en v7, qué sobra, qué dirige mal. Este campo ya no es testimonio: es diagnóstico técnico. Lenguaje del modelo (capas, archivos, secciones, dependencias). El autor traduce el síntoma específico a hipótesis sobre el defecto del modelo.

**Campo 4 — Patrón general implícito.** Formulación agnóstica del defecto. El autor abstrae del proyecto concreto y formula el patrón en términos que sirven para cualquier proyecto futuro. Esta es la operación crítica del protocolo: si el campo 4 sigue mencionando elementos específicos del proyecto, el registro no está descontextualizado y v7 no podrá usarlo limpiamente. Lenguaje del modelo, sin nombres de obra.

**Campo 5 — Implicación para v7.** Acción concreta que v7 debería tomar. Qué archivo modificar, qué sección reformular, qué archivo nuevo crear, qué dependencia revisar. Este campo es propositivo, no decisivo: la decisión final se toma en sesión de procesamiento de aprendizaje en el proyecto v7, no en este registro. Pero el campo orienta al chat de procesamiento sobre la dirección esperada.

---

## REGLAS DE REDACCIÓN DEL REGISTRO

**Regla A — Brevedad.** Cada registro entre 5 y 20 líneas. Si un registro requiere más espacio, probablemente está mezclando varios aprendizajes en uno; conviene desdoblarlo en registros separados.

**Regla B — Disciplina del campo 4.** El campo de patrón general implícito debe estar limpio de referencias específicas al proyecto que generó el registro. Si menciona personajes, mundos o decisiones concretas, no está descontextualizado. La prueba operativa: si un autor de otro proyecto leyera el campo 4 sin haber visto los campos 2 y 3, ¿entendería el patrón como aplicable a su proyecto? Si la respuesta es sí, el campo está bien formulado.

**Regla C — Fidelidad al síntoma.** El campo 2 (síntoma observado) no debe maquillarse para hacer el aprendizaje más vendible o limpio. Si la fricción fue ambigua o difícil de describir, el campo lo refleja con honestidad. Los registros con síntomas inflados o disfrazados producen procesamiento de baja calidad en v7.

**Regla D — Captura al calor del momento.** El registro se genera lo antes posible después de detectar la fricción, idealmente dentro de la misma sesión de trabajo. La memoria del autor sobre por qué algo se sintió fricción se desvanece rápido. Capturar tres días después produce registros donde el campo 2 es vago.

**Regla E — Sin filtrado prematuro.** El autor no decide en el momento de captura si la fricción merece o no llegar a v7. Cualquier fricción legítima de las cinco situaciones produce registro. La decisión de qué se incorpora a v7 y qué se descarta se toma después, en sesión de procesamiento. Filtrar al capturar produce sesgo del autor sobre qué considera importante; el procesamiento posterior, con varios registros acumulados, identifica patrones que un solo registro aislado no revelaría.

---

## CICLO DE VIDA DEL REGISTRO

**Generación.** El autor del proyecto creativo genera el registro en su espacio de trabajo cuando detecta una de las cinco situaciones. Lo guarda en archivo local del proyecto creativo, en bitácora propia del autor, o directamente lo sube al proyecto v7. Recomendación operativa: subirlo al proyecto v7 al final de cada sesión de trabajo donde se haya generado al menos un registro, para que v7 acumule sin pérdida.

**Acumulación.** El proyecto v7 mantiene archivo REGISTROS_APRENDIZAJE.md (o equivalente, según convención que el primer chat de v7 establezca) donde los registros se acumulan en orden cronológico. No se procesan inmediatamente; se acumulan hasta que el autor decide que hay materia suficiente para sesión de procesamiento.

**Umbral de procesamiento.** El autor decide cuándo procesar. Heurística operativa: procesar cuando se acumulen entre 5 y 15 registros, o cuando un proyecto creativo principal cierre fase significativa (libro 1 terminado, primera novela completa, proyecto descartado). Procesar con menos de 5 registros produce sesiones de bajo rendimiento; procesar con más de 20 puede saturar capacidad de la sesión.

**Procesamiento.** Sesión de trabajo en el proyecto v7 donde se revisan los registros acumulados, se identifican patrones (varios registros que apuntan al mismo defecto), se decide qué cambios aplicar al modelo. Resultado: modificaciones de plantillas, archivos nuevos, secciones reformuladas, según corresponda. Las modificaciones siguen la regla 6 del proyecto v7 (versionado explícito): cada cambio produce nueva versión documentada.

**Archivo del registro.** Tras procesamiento, los registros que motivaron cambios quedan archivados en el proyecto v7 con marca de "procesado en sesión X, motivó cambio Y". Los registros que no motivaron cambios (descartados como específicos de un proyecto, no generalizables, o duplicados) quedan archivados con marca correspondiente. Ningún registro se borra. La traza completa permite auditar la evolución del modelo.

---

## QUÉ NO ES UN REGISTRO LEGÍTIMO

Para preservar la calidad del flujo, conviene declarar qué tipo de inputs no son registros legítimos y deben rechazarse:

- **Quejas estilísticas sin diagnóstico.** "Esta plantilla me molesta" sin análisis de por qué, dónde, cómo. Falta campo 3.
- **Propuestas de archivo nuevo sin síntoma asociado.** Querer un archivo nuevo porque "podría ser útil" sin haber detectado fricción real que lo justifique. Falta campo 2.
- **Especulación sobre proyectos hipotéticos.** "Si alguien escribiera tal proyecto, faltaría tal cosa." El protocolo se alimenta de práctica real, no de especulación.
- **Modificaciones de gusto.** "Prefiero que esta plantilla diga X en lugar de Y." Sin diagnóstico de por qué Y produce fricción operativa, es preferencia personal del autor, no aprendizaje del modelo.
- **Registros que duplican otro ya capturado.** El autor revisa la bitácora antes de capturar para evitar duplicados directos.

Estos inputs pueden ser conversación legítima sobre el modelo en otros contextos, pero no entran al protocolo de captura.

---

## RELACIÓN CON LAS REGLAS OPERATIVAS DE v7

El protocolo es la implementación práctica de la regla 2 (flujo unidireccional desde proyectos hacia v7) y la regla 3 (inputs aceptados). Su aplicación rigurosa es lo que diferencia un modelo que mejora con cada uso de un modelo que se contamina con cada uso. La regla 1 (no contaminación) se sostiene gracias a este protocolo: las plantillas en uso no se modifican; la captura genera registro que después produce modificación controlada en sesión dedicada.

---

## RELACIÓN CON OTROS ARCHIVOS

Este archivo es plantilla operativa del proyecto agnóstico v7, no plantilla del catálogo. Convive con:
- El documento de apertura del proyecto agnóstico v7 (que declara las reglas operativas que este protocolo implementa).
- Las treinta plantillas del catálogo v7.
- El archivo REGISTROS_APRENDIZAJE.md (o equivalente) que el primer chat de v7 establecerá para acumular los registros.
- Los reportes de sesiones de procesamiento que se vayan generando.

Cuando v7 evolucione hacia v8 (futuro hipotético), este protocolo puede revisarse según la experiencia acumulada. Cualquier modificación al protocolo sigue la regla 6 del proyecto (versionado explícito).

Fin de la plantilla del protocolo de captura de aprendizaje.
