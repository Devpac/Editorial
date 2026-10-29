# PROTOCOLO_CAPTURA_APRENDIZAJE.md — Plantilla operativa

## PROPÓSITO

Cómo aprende la fábrica de las obras que se escriben con ella: qué se aprende, dónde se registra y cómo pasa a la fábrica sin traerse la obra. Sin protocolo, las fricciones se quedan en las actas de una obra, con sus nombres y sus cifras, y no hay forma de pasárselas a la siguiente. Con protocolo, cada fricción deja un registro que se puede procesar en limpio.

---

## QUÉ SE APRENDE Y CUÁNDO

- **Al cerrar cada capítulo** (OPERACIÓN C): las **fricciones de catálogo** del acta, las reglas que no ayudaron o chocaron (adenda de `SYSTEM_ORCHESTRATION.md`, §4: la salida del cierre es el acta).
- **En cada lectura** (C.5, externa, de plan, a ciegas, OPERACIÓN D; `PROTOCOLO_LECTURA.md`): lo que las lectoras señalan y viene de una regla o de su falta (una repetición que vuelve en varios capítulos, un suelo que se cumple y no se nota, una comprobación que no vio lo que la lectora sí). El orquestador separa lo que es de la obra (va a su biblia, preset o escaleta) de lo que es del modelo.
- **Al cerrar un libro**: lo que dicen juntas las actas, las lecturas y el historial del libro.

Es del modelo cuando entra en una de estas cinco situaciones:

1. **Fricción operativa.** La plantilla no contempla algo que hace falta y hay que improvisar fuera de ella.
2. **Deriva.** La plantilla orientó mal: una decisión que, vista después, fue peor por seguirla.
3. **Hueco.** Falta una sección o un archivo, y la falta volverá en otras obras.
4. **Redundancia o contradicción.** Dos plantillas se solapan o se contradicen.
5. **Limitación de alcance.** Una plantilla supone un subgénero, una pareja, una forma de saga o un valor de una obra, y falla fuera de ese supuesto.

---

## DÓNDE SE REGISTRA

**Una mejora que nace de una obra se registra en la obra y se propone a la fábrica.** En la obra queda dónde se vio (el acta o la lectura, con su código). El orquestador lo propone a la fábrica, al cerrar el encargo en que lo vio, con un registro en `informes/propuestas_fabrica.md` de la obra (no en la copia montada en `fabrica/`, que no se edita). Quien mantiene Editorial lo pasa a su `REGISTROS_APRENDIZAJE.md` (el de `fabrica/metodo/`) y lo procesa allí. Cada registro tiene cinco campos y ocupa de 5 a 20 líneas:

- **Campo 1 — Identificador y fecha.** Número correlativo y fecha de captura.
- **Campo 2 — Síntoma observado.** Qué pasó, con la lengua de la obra si hace falta (nombres, capítulos, cifras) y el código del acta o la lectura de donde sale. Es testimonio: los datos de la obra son historia del registro, no regla.
- **Campo 3 — Diagnóstico del modelo.** Por qué pasó, en términos del modelo (archivo, sección, operación, comprobación).
- **Campo 4 — Patrón general implícito.** El defecto formulado sin nada de la obra. Prueba: una autora de otra saga, sin ver los campos 2 y 3, lo entendería como suyo.
- **Campo 5 — Implicación para el modelo.** Qué cambiar y dónde: propuesta, no decisión.

Al procesarlo se añade la **marca**: APLICADO (dónde y en qué versión), DESCARTADO (por qué), HISTÓRICO (de un modelo anterior, solo traza) o PENDIENTE. Ningún registro se borra.

Reglas de redacción: breve (si pide más de 20 líneas, son dos registros); fiel al síntoma, sin maquillarlo; al calor del momento, en el mismo encargo; sin filtrar al capturar: lo que entra o no se decide al procesar.

---

## CÓMO PASA A LA FÁBRICA

- **Regla del fork:** ninguna mejora añade instrucciones antes de escribir. Va al cierre (OPERACIÓN C), a la lectura (C.5, `PROTOCOLO_LECTURA.md`) o a los tests de las plantillas de fase. La que necesita decirle a quien escribe cómo escribir se descarta.
- **Si solo corta** (una comprobación de cierre, una pregunta de lectura, una regla que sobra), puede ir directa y se vigila en las lecturas siguientes. **Si no**, va en una rama y con prueba a ciegas (adenda de `SYSTEM_ORCHESTRATION.md`, §7).
- **A la fábrica va la regla; el valor se queda en la obra.** La regla se escribe en abstracto, con «si la obra lo declara» y su ranura del preset (bloque «Valores de la obra →»); el valor (la cifra, el nombre, la decisión) va al preset o a la biblia de la obra. Ningún archivo de la fábrica lleva valores de una obra.
- **Quién decide:** por delegación, el orquestador, las mejoras que solo añaden comprobaciones de cierre o de lectura; el autor, cualquier cambio que toque la escritura (`ORQUESTADOR.md`, §7).
- **Cuándo:** con 5 a 15 registros acumulados o al cerrar un libro. Cada cambio se apunta y llega a las obras como dice `ORQUESTADOR.md` §10, y su registro recibe la marca.

---

## QUÉ NO ES UN REGISTRO

- Una queja sin diagnóstico (falta el campo 3) o un archivo nuevo sin síntoma (falta el campo 2).
- Una especulación sobre obras hipotéticas: el protocolo se alimenta de práctica real.
- Una preferencia de gusto sin fricción que la sostenga.
- Un valor de la obra: va a su preset o a su biblia, no a la fábrica.
- Una instrucción de prosa previa: la regla del fork no la admite.
- Un duplicado: antes de capturar se mira la bitácora.

Fin de la plantilla del protocolo de captura de aprendizaje.
