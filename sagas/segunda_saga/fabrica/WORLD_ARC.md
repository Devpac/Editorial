<!-- Fábrica — WORLD_ARC: base de oficio + adenda de dark romance (v2.0) -->

# WORLD_ARC.md

## PROPÓSITO

Este archivo declara el arco del mundo de serie como dimensión narrativa propia. En sagas multivolumen donde el mundo evoluciona en paralelo a los personajes y esa evolución carga peso temático específico, el mundo no puede tratarse como decorado estable. Necesita arquitectura propia: ejes que se mueven, deudas que abren y cierran, promesas hechas al lector sobre cómo cambiará el universo, puntos de inflexión declarados o explícitamente ausentes, trayectoria por libro auditable.

Sin este archivo, las sagas con mundo evolutivo producen uno de dos síntomas patológicos. El mundo queda decorativo (no evoluciona porque no hay archivo que lo gestione, y los personajes cambian sobre fondo estático que el lector empieza a percibir como caricaturesco). O el mundo se gestiona ad hoc capítulo a capítulo (improvisado sin diseño multilibro, con riesgo de incoherencias entre volúmenes y pérdida de la inversión temática que el mundo evolutivo podría aportar).

Con este archivo, el mundo se trata como personaje colectivo con arco propio. No protagoniza la saga (esa función pertenece a los personajes, salvo que el proyecto declare otra orientación), pero tiene trayectoria diseñada que opera como fondo iluminador de los arcos personales y como portador de carga temática que los personajes solos no podrían sostener.

JERARQUÍA: Capa 0.5 (gobierno de serie). Archivo paralelo a SERIES_ARCHITECTURE.md, ambos coexisten cuando el proyecto es multivolumen.

---

## CONDICIONALIDAD DE APLICACIÓN

Este archivo no se aplica a todos los proyectos. Su uso es condicional a tres criterios que deben cumplirse simultáneamente:

**Criterio 1 — Multivolumen.** El proyecto declara serie de dos o más volúmenes. SERIES_ARCHITECTURE.md está activo.

**Criterio 2 — Mundo evolutivo.** El mundo del proyecto cambia sustantivamente entre el primer libro y el último. No basta con que pase tiempo; debe haber transformación del entorno (institucional, cultural, geopolítica, ecológica, tecnológica, según naturaleza del proyecto) que sea narrativamente legible.

**Criterio 3 — Carga temática del mundo.** La evolución del mundo aporta significado que excede al avance de los arcos personales. El mundo cambiando dice algo que los personajes solos no dicen.

Si los tres criterios se cumplen, este archivo se diseña en OPERACIÓN 0 del proyecto, después de SERIES_ARCHITECTURE.md y antes de los archivos de capa 1.

Si solo se cumplen uno o dos criterios, este archivo se omite. Saga con mundo estable (criterio 2 no cumple) se gestiona con SERIES_ARCHITECTURE solo. Obra única (criterio 1 no cumple) ni siquiera entra en capa 0.5.

La declaración de cumplimiento o incumplimiento de los criterios es decisión autoral consciente al inicio del proyecto, no asunción tácita. Se registra en BRIEFING.md como decisión inicial.

---

## DECLARACIÓN DE ESTRUCTURA DEL ARCO DE MUNDO

El archivo declara la forma dramática del arco de mundo, distinguiéndola de las formas dramáticas de los arcos personales.

**Forma dramática.** Cada proyecto declara la suya. Ejemplos posibles: escalada con clímax sistémico (el mundo cambia direccionalmente y culmina en transformación visible), ciclo con variación (el mundo se reorganiza pero la función subyacente se reproduce), expansión expositiva (el mundo revela sucesivamente capas que estaban presentes desde el inicio), colapso progresivo (el mundo se degrada en cascadas concatenadas), reconstrucción tras ruptura (el mundo se reordena después de evento traumático). La elección no es estética; condiciona qué deudas son posibles, qué promesas se le pueden hacer al lector, cómo se cruza con los arcos personales.

**Subordinación temática.** El arco de mundo se subordina a la pregunta central del proyecto declarada en THEMATIC_ENGINE.md. Esta subordinación es obligatoria: el arco de mundo no puede resolver la pregunta central por vía macro. Si la pregunta central pertenece a la agencia moral individual y el arco de mundo demuestra empíricamente uno de los polos, la pregunta queda respondida por el sistema y la novela pierde su irresolubilidad. La subordinación se ejecuta mediante principios de neutralización que cada proyecto declara según naturaleza de su pregunta central.

**Jerarquía de intensidad escénica.** Cada proyecto declara cómo se relacionan en escena los arcos personales y el arco de mundo. Posibilidades: personajes por encima de mundo (mundo como fondo iluminador), mundo por encima de personajes (personajes como agentes del mundo cambiante), simetría declarada (ambos compiten conscientemente por intensidad), alternancia rítmica (predominio variable según fase de la obra). La elección condiciona la regla operativa de cómo se diseñan los capítulos donde ambos comparezcan.

---

## INVENTARIO DE EJES DE MUNDO EN MOVIMIENTO

El arco de mundo se descompone en ejes. Un eje es dimensión específica del mundo cuya evolución se rastrea durante la saga. Los ejes pueden ser institucionales (sistemas políticos, organizaciones, estructuras de poder), corporativo-económicos (actores económicos, mercados, relaciones extractivas), territoriales (regiones, fronteras, periferias), culturales-generacionales (cosmovisiones, memorias colectivas, identidades), tecnológicos, ecológicos, geopolíticos, según naturaleza del proyecto.

**Cantidad de ejes.** Decisión autoral. Recomendación operativa: entre tres y seis ejes. Menos de tres produce arco de mundo monolítico que no permite asimetrías necesarias. Más de seis produce dispersión que excede el presupuesto de presencia narrativa.

**Dominancia de ejes.** No todos los ejes pesan igual. La declaración de dominancia distingue ejes dominantes (presencia central en la saga, cruce con varios POVs, evolución sustantiva en cada libro), ejes subordinados o sustrato (presencia atmosférica, alimentan a los dominantes sin competir con ellos), y ejes activables puntualmente (dormidos durante varios libros, se activan en momento específico para función concreta).

**Función sistémica por eje.** Para cada eje se declaran los componentes operativos de su función actual al inicio de la saga. Esta declaración es crítica porque permite auditar si el eje, al cambiar de forma a lo largo de la saga, preserva su función subyacente o la altera. La auditoría de función sistémica es el test operativo principal del archivo.

**Cruce con POVs.** Para cada eje se declara cómo se cruza con los personajes punto de vista de la saga. Tabla operativa con códigos de intensidad (principal, secundario, estructural-subterráneo, instrumental, marginal, ausente) por POV y por eje. Esta tabla es referencia constante en OPERACIÓN 0.5 de cada capítulo.

---

## ARCO DEL MUNDO POR LIBRO

Para cada libro de la saga, el archivo declara el estado del mundo al inicio, las manifestaciones del arco durante el libro, y el estado al cierre. La declaración cubre los ejes declarados (los que apliquen) en cada libro.

**Estado por libro.** Configuración del mundo al inicio del libro. Descripción concreta de cómo se presenta cada eje al lector que abre ese volumen. Para libros posteriores al primero, esta declaración debe coherer con el estado al cierre del libro anterior, asegurando continuidad multivolumen.

**Manifestaciones durante el libro.** Eventos concretos del arco de mundo que ocurren durante el libro. Cada manifestación se declara con eje al que pertenece, presencia narrativa estimada (cuántos capítulos, cuál es su distribución), y cruce con qué POVs.

**Movimientos centrales.** Algunos libros tienen puntos de inflexión propios del arco de mundo (escisiones, consolidaciones, rupturas, articulaciones, dispersiones). Cada movimiento se declara con su tipología (por ejemplo: doble movimiento acoplado, movimiento único direccional, movimiento triple distribuido) y su función dentro del arco global.

**Siembras y anclajes.** Las manifestaciones tempranas del arco de mundo en libros iniciales suelen ser siembras invisibles en primera lectura, legibles en relectura. Estas siembras se declaran explícitamente con su función (preparan qué deuda, anticipan qué movimiento), su ubicación (en qué fase del libro), y su forma (frase oída, nombre que aparece en archivo, mención marginal en texto).

---

## ARCO GLOBAL DE MUNDO EN LA SAGA COMPLETA

Sección integradora que declara la trayectoria del mundo a lo largo de toda la saga, vista como totalidad. Sintetiza los estados por libro en forma dramática unificada.

**Estado inicial y estado final.** Configuración del mundo al inicio del primer libro y al cierre del último. La diferencia entre ambos estados es la trayectoria del arco. La declaración explícita previene que la diferencia sea casual o se diluya durante la escritura.

**Forma de la trayectoria.** Cómo se llega del estado inicial al estado final. Si la forma dramática declarada es ciclo con variación, la trayectoria atraviesa estados intermedios donde la apariencia cambia pero la función se preserva. Si es escalada, la trayectoria es direccional con clímax. Si es colapso, la trayectoria es descendente con cascadas. La forma condiciona cómo se distribuyen los movimientos centrales entre los libros.

**Clausura o no-clausura final.** Decisión autoral sobre si el arco de mundo cierra limpiamente al final de la saga o queda inconcluso. La no-clausura es decisión legítima cuando el proyecto declara que el patrón continuará más allá del horizonte narrativo. La clausura es decisión legítima cuando el proyecto declara que el ciclo termina. Ambas opciones requieren ejecución consciente para no producir efecto contrario por descuido.

**Cierre argumentativo del arco.** Si la saga tiene un evento o estado final que opera como cierre argumentativo del arco de mundo (no necesariamente coincidente con el clímax narrativo del último libro), se declara explícitamente. Este cierre argumentativo es típicamente lateral al clímax personal del libro final.

---

## DEUDAS DE MUNDO

Análogas a las deudas de SERIES_ARCHITECTURE pero específicas de mundo. Una deuda de mundo es elemento del arco que se abre en algún libro y debe pagarse (cerrar, transformar, declarar como no-cierre consciente) en libro posterior. Sin gestión de deudas, el arco de mundo se dispersa y los lectores quedan con expectativas no atendidas.

**Inventario.** Cada deuda recibe identificador único, descripción concreta, libro de apertura, libro de pago previsto, tipo (mundo puro, mundo con resonancia temática, mundo con resonancia de personaje, mundo con resonancia cultural). Recomendación operativa: entre cuatro y ocho deudas. Menos produce arco de mundo poco articulado; más produce sobrecarga.

**Calendario de pagos.** Distribución de aperturas y cierres por libro. La distribución debe ser equilibrada: ningún libro carga sobreabundancia de cierres respecto a otros. La auditoría del calendario detecta libros con riesgo de saturación (típicamente el último de la saga, donde concurren cierres de personaje y cierres de mundo).

**Tipos de pago.** Cada deuda puede pagarse de cuatro maneras: cierre completo (la deuda se resuelve y la cuestión queda zanjada), cierre parcial (la deuda se resuelve incompletamente, dejando residuo que es funcional al efecto temático), declaración de no-cierre consciente (el proyecto explicita que esta deuda no se cierra y registra por qué), reedición (la deuda se cierra abriendo otra análoga, en proyectos donde el patrón se reproduce).

**Coherencia con deudas de SERIES_ARCHITECTURE.** Las deudas de mundo conviven con las deudas de personaje declaradas en SERIES_ARCHITECTURE. La nomenclatura debe permitir distinguirlas (prefijos diferenciados, numeración paralela). La auditoría de calendario consolidado revisa el conjunto.

---

## PROMESAS AL LECTOR SOBRE EL MUNDO

Análogas a las promesas de SERIES_ARCHITECTURE pero específicas del mundo. Cuando el lector empieza la saga, la presentación del mundo le hace promesas implícitas sobre cómo evolucionará. Algunas se cumplen, otras se subvierten conscientemente, otras se neutralizan deliberadamente.

**Cumplir.** Promesas que la saga entrega como el lector las espera. El mundo evolucionará visiblemente, las consecuencias institucionales del evento desencadenante se desplegarán, el conflicto político escalará. Las promesas a cumplir son la base contractual entre obra y lector.

**Subvertir.** Promesas que la saga entrega de forma inesperada pero satisfactoria. La subversión exige que el lector reciba algo distinto de lo que esperaba, pero más interesante. Una promesa subvertida mal ejecutada es promesa rota; bien ejecutada es promesa enriquecida.

**Neutralizar.** Promesas que el lector podría inferir y que la saga deliberadamente impide que arraiguen. La neutralización requiere herramientas específicas (por ejemplo: tratar cierto elemento como tópico secundario, evitar momentos donde la promesa cristalizaría, mantener silencio sobre cierto aspecto del mundo). La neutralización es la decisión más delicada de las tres porque opera por ausencia, no por presencia.

**Coherencia con promesas de SERIES_ARCHITECTURE.** Las promesas de mundo conviven con las promesas de personaje. Algunas pueden cruzarse (una promesa parece de personaje pero se entrega vía mundo, o viceversa). La auditoría declara los cruces explícitamente.

---

## PUNTOS DE NO RETORNO DE MUNDO

Decisión autoral fundamental sobre si el mundo cruza umbrales irreversibles durante la saga.

**Opción 1 — El mundo cruza puntos de no retorno formales.** En proyectos donde el mundo evoluciona direccionalmente con transformaciones irreversibles (tras evento X, el mundo nunca vuelve a ser como antes de X), los puntos de no retorno se declaran explícitamente. Para cada uno: en qué libro ocurre, cuál es el umbral cruzado, qué hace que sea irreversible, qué consecuencias produce.

**Opción 2 — El mundo no cruza puntos de no retorno formales.** En proyectos donde el mundo se reorganiza pero la función subyacente se preserva (forma cambia, sustancia se conserva), la declaración explícita es que el mundo no cruza umbrales irreversibles. Esta declaración es crítica porque sostiene asimetría con los personajes (que sí pueden cruzar puntos de no retorno propios). La asimetría es motor emocional específico de proyectos con esta orientación.

La elección entre opción 1 y opción 2 condiciona toda la auditoría operativa del arco. La declaración explícita en este archivo hace que OPERACIÓN D pueda verificar coherencia capítulo a capítulo.

---

## CRUCES CON LOS ARCOS POV

Sección integradora que declara cómo el arco de mundo se cruza con los arcos de los personajes punto de vista.

**Tabla de intensidad.** Para cada POV declarado en CHARACTER_PHYSICS.md y para cada eje del arco de mundo, se registra la intensidad del cruce con códigos consistentes. La tabla es referencia operativa para diseñar capítulos: dado un capítulo del POV X en libro N, los ejes de mundo que se manifestarán son los que la tabla declara cruce significativo.

**Función reveladora.** Para cada cruce significativo, se declara qué revela el eje sobre el POV. El arco de mundo no se cruza con personajes en abstracto; se cruza para iluminar dimensiones específicas del personaje que sus arcos personales solos no exhibirían. Esta función reveladora es la que justifica el cruce.

**Asimetría temporal.** El cruce de un POV con un eje no es uniforme a lo largo de la saga. Puede ser intenso en libros tempranos y atenuarse, o lo contrario, o tener pico en libro intermedio. La declaración de la asimetría temporal por cruce permite planificar cuándo cada POV se enfrenta a cada eje con qué intensidad.

---

## INTERACCIÓN CON LA PREGUNTA TEMÁTICA

Sección crítica para preservar la integridad temática del proyecto. Declara explícitamente cómo el arco de mundo se subordina a la pregunta central declarada en THEMATIC_ENGINE.md.

**Principios de neutralización.** El proyecto declara los principios mediante los cuales evita que el arco de mundo resuelva la pregunta central por vía macro. Cada principio es regla operativa que se audita en cada libro. Los principios pueden combinar filtros estructurales (que evitan resoluciones lógicas inadvertidas) y motores emocionales (que producen el efecto temático específico que el proyecto busca).

**Test operativo de subordinación.** Auditoría binaria que se aplica al cierre del último libro: ¿el lector razonable concluye que la pregunta central tiene respuesta porque el mundo demostró X o Y? Si la respuesta es sí, el arco de mundo ha fallado en subordinarse a la pregunta. La declaración del test en este archivo permite que OPERACIÓN D y PASADA 1 de REVISION_PROTOCOL lo verifiquen.

**Resonancias con motivos.** Si THEMATIC_ENGINE declara motivos recurrentes, el arco de mundo puede generar resonancias con ellos. Las resonancias se declaran explícitamente para evitar que sean accidentales (que producirían colisión temática) o se pierdan (lo cual desperdiciaría material temático aprovechable).

---

## RIESGOS ESPECÍFICOS DEL ARCO DE MUNDO

El arco de mundo introduce riesgos narrativos específicos que conviene declarar para auditarlos durante la ejecución. Cada proyecto puede declarar los suyos según naturaleza; los siguientes son los más comunes.

**Riesgo 1 — Mundo que resuelve la pregunta.** El arco de mundo demuestra empíricamente uno de los polos de la pregunta central, vaciándola de irresolubilidad. Prevención: principios de neutralización rigurosos, auditoría operativa.

**Riesgo 2 — Escalada cósmica.** El arco de mundo introduce fenómeno estructural nuevo que desplaza el centro narrativo del proyecto hacia el mundo. Prevención: limitar el arco a evolución sin novedad estructural, mantener jerarquía de intensidad escénica declarada.

**Riesgo 3 — Exposición narratorial.** Capítulos donde el narrador expone cambios macro del mundo, rompiendo el régimen estético del proyecto. Prevención: regla operativa de que ningún capítulo toma evento de mundo como materia central; evento de mundo entra como fricción sobre la rutina del POV.

**Riesgo 4 — Mundo episódico.** Eventos de mundo dispersos sin arco integrado, percibidos como sucesos sueltos. Prevención: forma dramática declarada en estructura del arco global, calendario de pagos coherente.

**Riesgo 5 — Mundo dominante.** El mundo come presencia narrativa a los personajes, invirtiendo la jerarquía de intensidad escénica. Prevención: presupuesto de presencia narrativa por libro, auditoría de cada capítulo donde concurran ambos.

---

## TESTS DE FUNCIONAMIENTO

Auditorías operativas que verifican el cumplimiento del archivo durante la ejecución. Se aplican en OPERACIÓN D y en PASADA 1 de REVISION_PROTOCOL.

**Test 1 — Subordinación temática.** ¿La pregunta central permanece irresuelta tras el cierre del último libro? Auditoría binaria. Si falla, el arco de mundo está resolviendo la pregunta por vía macro.

**Test 2 — Reproducción funcional.** Si la forma dramática es ciclo con variación, ¿la función sistémica de cada eje se preserva en estado final? Si falla, el ciclo se ha convertido en escalada por descuido.

**Test 3 — Asimetría intensidad escénica.** ¿La jerarquía declarada entre personajes y mundo se mantiene en muestra de capítulos? Si falla, algún capítulo ha invertido la jerarquía y conviene revisar.

**Test 4 — Coherencia de deudas y promesas.** ¿Las deudas abiertas se pagan en el calendario declarado? ¿Las promesas (cumplir/subvertir/neutralizar) se entregan según clasificación? Si falla, hay deuda en olvido o promesa traicionada.

**Test 5 — Articulación inadecuada.** Si el proyecto declara que ciertos patrones del arco de mundo no deben articularse por personajes ni narrador (efectos que dependen de no-articulación), ¿algún capítulo permite leer la articulación? Auditoría binaria. Si falla, el efecto colapsa.

Cada proyecto puede añadir tests específicos según orientación.

---

## INTEGRACIÓN OPERATIVA

**OPERACIÓN 0 (FUNDACIÓN).** Si los tres criterios de aplicación se cumplen, este archivo se diseña después de SERIES_ARCHITECTURE.md y antes de los archivos de capa 1. La declaración de no-aplicación, si los criterios no se cumplen, queda registrada en BRIEFING.md.

**OPERACIÓN 0.5 (BRIEF DE CAPÍTULO).** Si el capítulo toca manifestación de eje de mundo, se consulta este archivo para verificar fase del eje en libro N, deudas activas, jerarquía declarada con arcos personales. La consulta es obligatoria para capítulos con cruce; opcional para capítulos sin cruce.

**OPERACIÓN A (DISEÑO DE ESCENA).** Si la escena cruza arco de personaje y arco de mundo, se aplica jerarquía de intensidad escénica declarada en este archivo. La escena debe diseñarse de forma que respete la jerarquía.

**OPERACIÓN D (AUDITORÍA ESTRUCTURAL).** Cada auditoría revisa fase de eje de mundo según calendario, pagos de deudas según calendario, asimetría con arcos personales, tests de funcionamiento. La consulta es obligatoria si el arco de mundo está activo en el proyecto.

**REVISION_PROTOCOL (PASADA 1).** Auditoría completa del cumplimiento del archivo en el primer borrador. Detecta derivas que la ejecución no captó.

---

## RELACIÓN CON OTROS ARCHIVOS

**SERIES_ARCHITECTURE.md.** Archivo paralelo de capa 0.5. Coexisten ambos cuando el proyecto es multivolumen. SERIES_ARCHITECTURE rige arcos de personaje multivolumen; este archivo rige arco de mundo de serie. Las deudas y promesas de ambos se mantienen en inventarios diferenciados con nomenclatura distinguible.

**THEMATIC_ENGINE.md.** Archivo de capa 1 al que este archivo se subordina. La pregunta central declarada allí condiciona los principios de neutralización que este archivo aplica.

**WORLD_TEXTURE.md.** Archivo de capa 1 con función complementaria. WORLD_TEXTURE registra el mundo en estado (configuración estable, descripción del entorno); este archivo registra el mundo en proceso (trayectoria evolutiva multilibro). Ambos se consultan: WORLD_TEXTURE para textura material de cualquier escena, este archivo para fase del eje correspondiente al libro en curso.

**CHARACTER_PHYSICS.md.** Archivo de capa 1 al que este archivo se cruza. La tabla de intensidad de cruces POV × ejes registra la relación específica de cada personaje con cada eje del arco de mundo.

**NARRATIVE_CHRONOLOGY.md.** Archivo de capa 1 que registra los eventos del arco de mundo en sus capas correspondientes (eventos manifestados, eventos invisibles simultáneos, eventos proyectados post-narrativos).

**INFORMATION_CHOREOGRAPHY.md.** Archivo de capa 1 que registra los hechos del arco de mundo según calendario de revelación al lector. Hechos de rango de mundo paralelos a hechos de rango temático y de personaje.

**STORY_SPINE.md.** Archivo de capa 1 al que este archivo aporta material. Las siembras del arco de mundo en libros iniciales son anclajes para deudas que cierran en libros posteriores. STORY_SPINE de libros tempranos integra las siembras como retoques o inserciones específicas.

**CONTINUITY_PHYSICS.md.** Archivo de capa 2 transversal que registra estado durante la ejecución. Sus registros de información por POV, deudas narrativas, tensión y motivos contemplan los elementos del arco de mundo activos.

**SYSTEM_ORCHESTRATION.md.** Archivo de capa 0 que gobierna las operaciones. Su declaración de capa 0.5 incluye este archivo cuando los criterios de aplicación se cumplen.

**BRIEFING.md.** Archivo transversal que registra estado del proyecto y decisiones autorales acumuladas. La decisión sobre cumplimiento o incumplimiento de los criterios de aplicación de este archivo se registra allí.

Fin de la plantilla agnóstica WORLD_ARC.


---
---

## ADENDA DE ESPECIALIZACIÓN — Fábrica (género)

> Aplica `PAREJA_PRIMERO.md`, que manda donde choquen: la pareja es la trama A y el mundo, como
> mucho, el escenario de la trama B. La base agnóstica de arriba sigue vigente para la obra que
> active este archivo.

### 1. INACTIVO POR DEFECTO

En dark romance este archivo no se activa: el criterio 3 de la base se da por no cumplido (la carga
temática la lleva la pareja: THEMATIC_ENGINE, adenda) y la no aplicación se registra en BRIEFING,
como pide la base. Lo que cambia en el mundo de una saga (la trama horizontal y sus relojes, la
amenaza de fondo de las parejas rotativas) se lleva en CLUE_LEDGER (capas B y C) y en las deudas de
serie de SERIES_ARCHITECTURE. Activarlo es decisión del autor, con su porqué en la biblia.

### 2. SI SE ACTIVA

- **Jerarquía de intensidad escénica:** personajes por encima de mundo, sin las otras tres
  opciones, y los personajes son la pareja. El mundo entra como fricción entre ellos (choque,
  proximidad forzada, obstáculo o moneda: `PAREJA_PRIMERO.md` §5), nunca como materia central del
  capítulo (riesgos 3 y 5 de la base). Su página cuenta dentro de lo que no es pareja, salvo que
  cumpla `PAREJA_PRIMERO.md` §2 (SCALE_CALIBRATION, adenda).
- **Cifras:** los tres a seis ejes y las cuatro a ocho deudas de la base son techo, no mínimo.
- **Tabla de cruces POV × eje:** se consulta al escaletar el libro, no en el brief de cada capítulo
  (CHAPTER_BRIEF, adenda).
- El **Test 3** de la base se lee con la pareja como «personajes».
