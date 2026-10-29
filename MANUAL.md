# Manual de producción

Cómo se hace un libro con la fábrica, de la idea a Amazon, y **por qué sale bien**: qué piezas del proceso han dado la calidad que tiene hoy la primera obra, con qué pruebas, y cuáles no se tocan sin una prueba a ciegas.

Es para el autor y para cualquier orquestador nuevo. El detalle de cada paso está en la fábrica (`fabrica/metodo/ORQUESTADOR.md` y sus plantillas); aquí está el mapa y el porqué. Las evidencias salen de la primera obra hecha con el método (*Madera y Pólvora*, libro 1, octubre de 2026). El dossier completo, con cada nota y su fuente, está en `historia/dossier_por_que_funciona_2026-10-29.md`.

---

## 1. El proceso, de la idea a Amazon

### 1.1 Quién hace qué

| Quién | Qué hace | Qué no hace |
|---|---|---|
| **El autor** | Da la idea; decide lo cerrado (🔒): la premisa, el reparto entre pareja y trama, el calor, las líneas rojas, las muertes, los títulos; aprueba en las puertas; lanza cada ventana con el prompt que le da el orquestador | No escribe consignas de prosa |
| **El orquestador** (una ventana larga por obra, con relevos) | Diseña cada encargo (`NEXT.md`), lanza las lecturas, decide con lo que vuelve, corta, lleva la memoria (cuaderno, biblia, actas, plan de la lectora) e informa al autor | **No escribe la obra** |
| **Las ventanas de trabajo** (una por encargo, con el contexto limpio) | Escriben la biblia, el preset, las escaletas o un capítulo; hacen su cierre con acta; suben | No se auditan a sí mismas |
| **Las lectoras** (agentes nuevos, sin contexto) | Editora, lectora tipo, correctora, lectoras externas: leen solo lo que leería el público (la editora, además, la ficha) | No leen la biblia, el brief ni el acta |

### 1.2 Las fases

| Fase | Sale | Quién | Puerta del autor |
|---|---|---|---|
| **0. Arranque** | El repo de la saga (un comando: `ARRANQUE.md`), la ficha de premisa (`FICHA_PREMISA.md`) y el cuaderno | El orquestador, con una entrevista corta | Aprueba la ficha: la pareja y su pregunta, el reparto 🔒, el calor, las edades, las líneas rojas |
| **1. Biblia** | `<obra>_biblia.md` v1.0, en tres ventanas (B1 fundación, B2 arquitectura de la saga, B3 régimen) | Ventanas B1–B3 + auditoría (editora, lectora tipo, correctora) | Decide lo 🔒 |
| **1b. Preset** | `PRESET_<OBRA>.md`: los valores que leen las plantillas, sacados de la biblia | Ventana P1 + correctora | — |
| **2. Escaleta** | La escaleta del libro: cada ficha empieza por «Entre ellos» (qué cambia entre los dos) | Ventana E1 + lectura de plan de la lectora tipo + editora + correctora | Aprueba la escaleta |
| **3. Ampliada** | Las fichas detalladas, por tramos de unos doce capítulos | Ventanas A1, A2… + correctora + lectora (la muestra) | — |
| **4. Capítulos** | Cada capítulo con su brief, su texto y su acta | Una ventana por capítulo (C01, C02…) → lectura C.5 → cortes | Las preguntas que pida el plan de la lectora |
| **5. Cierre del libro** | El libro auditado, la pasada final y el paquete de publicación | OPERACIÓN D, lectura completa, externas, ventana F1 | Aprueba el libro y el paquete |
| **Publicación** | EPUB, interior PDF, cubiertas y ficha de KDP | El maquetador (`maquetador/`), con `publicacion/` de la saga | Sube a KDP |
| **Libro siguiente** | El puente, el diseño del libro (D1) y otra vez desde la fase 2 | El orquestador (`ORQUESTADOR.md` §2.7) | Aprueba el diseño |

### 1.3 El ciclo de un capítulo (el corazón del método)

1. **El encargo** (`NEXT.md`, del orquestador): qué cambia entre los dos en este capítulo, qué pone la otra trama, tiempo y lugar, qué no sabe cada uno, los vetos de canon, lo que pide la lectora, cómo cierra y lo que «se decide al escribir». **Qué, nunca cómo.**
2. **El autor lo lanza** con el prompt que le da el orquestador.
3. **La ventana escribe** con la obra entera leída (la voz que va a escribir, dos veces) y las reglas de prosa como oído de fondo, no como lista.
4. **El cierre obligatorio** (OPERACIÓN C): después del borrador, las comprobaciones (C-1 a C-10, los tests de calor, de voz, de continuidad, la edad) y el acta, una línea por comprobación. Sin acta, el capítulo no está escrito.
5. **La lectura** (C.5), por quien no lo escribió: una editora y una lectora tipo, agentes nuevos, a la vez, con paquetes distintos.
6. **Las correcciones** del orquestador: como mucho tres, cortando antes que añadiendo; si hace falta más, el capítulo vuelve a una ventana de reescritura.
7. **La memoria**: el canon nuevo a la biblia (Anexo A), lo que pide la lectora al plan con su destino (la ficha siguiente, el NEXT, la pasada final o el autor), las notas al historial.
8. **Cada unos siete capítulos**: una OPERACIÓN D corta y, si el autor las pasa, lecturas externas con otros modelos.

**Ritmo observado:** con el ciclo rodado, varios capítulos al día, cada uno con su lectura (*Madera y Pólvora*: seis el 28-10-2026).

---

## 2. Por qué funciona

La lectura honesta de los datos de la primera obra tiene dos partes.

**La prosa buena llegó con el cierre obligatorio y la lectura por otra (v1.1), y desde entonces no se mueve.** En la única prueba a ciegas que separa la prosa, el mismo capítulo escrito con el modelo anterior y con el cierre obligatorio, dos editoras sin contexto y con los textos en orden invertido dieron 6,5 y 7 al anterior y **8,3 y 8** al nuevo, con 6–6,5 frente a 8–7,5 en prosa. Desde entonces la editora puntúa entre 7,4 y 8,5 todo lo escrito, en todas las versiones.

**Lo que subió después fue el enganche de la lectora: lo hizo la pareja.** Con el diseño heredado de un modelo de intriga, los capítulos con un 40 % de pareja o más sacaban 8,25 de media de la lectora tipo, y los de un 15 % o menos, unos 6, con las mismas reglas de prosa. Las lecturas externas veían «80 % novela negra y 20 % romance». Con «la pareja primero» (v2.0), lo nuevo puntúa ≈ 8,0–8,3 frente a ≈ 6,4–6,8 de lo anterior en las mismas lecturas, y la lectora ve un 60–80 % de romance en los capítulos con cara a cara. Mientras tanto, la editora daba 8–8,8 a capítulos que la lectora puntuaba 4–7: **la editora mide la prosa, la lectora mide el libro.**

### 2.1 Las piezas, por la fuerza de su evidencia

- **A · Probado** (prueba a ciegas, o antes y después con el mismo instrumento)
- **B · Claro** (coincide en el tiempo con lo que dicen las lectoras)
- **C · Plausible** (no se puede atribuir)

| Pieza | Qué es | Evidencia | Qué pasó |
|---|---|---|---|
| **Cierre obligatorio + lectura por otra** | Un capítulo no está escrito hasta que tiene acta y lo ha leído quien no lo escribió | **A** | 8,3 y 8 frente a 6,5 y 7 a ciegas; menos de la mitad de comparaciones con «como» (3,3 frente a 7,6 por cada 1.000 palabras). Los borradores que se saltaron el cierre tenían ocho defectos que «casi todos ya tenían regla» |
| **Medir cuánto es romance en cada lectura** | Cada lectura estima el peso de la pareja y se compara con la cuenta de quien escribió | **A** como instrumento | Caza lo que el acta no ve: un capítulo con 94 % en el acta y 35 % para la lectora; el tic de los cierres de un narrador |
| **La lectora tipo, que manda** | Cada capítulo lo lee también una lectora del público, con todo lo anterior; si discrepa de la editora, gana ella | **B** | «Ahora sí sigo leyendo» (el primer cara a cara adelantado); «Por fin el dark romance que vine a buscar» (9) |
| **La pareja primero** | La pareja es la trama A de cada libro y cada capítulo, con objetivo y suelo medidos; la otra trama, con techo | **B** fuerte | ≈ 8,1 frente a ≈ 6,6; romance visto del 20 % al 60–80 %. Sin prueba a ciegas: no se separa del diseño nuevo |
| **Gancho en todos los cierres** | Ningún capítulo cierra plano; la mayoría, en la pareja | **B** | La excepción ensayada se retiró por la lectora; los cierres nuevos acompañan las subidas |
| **La muestra gratuita, leída como muestra** | Los primeros capítulos se leen con «¿lo comprarías?» | **B** | Lo que no vendía antes del primer encuentro se cortó o se fundió |
| **Tres lecturas = problema confirmado** | Lo que señalan tres lecturas o más se corrige también en lo escrito, y se vuelve una comprobación de cierre | **B** | Resolvió las escenas espejo, las muletillas y el rótulo del narrador |
| **Corregir lo que cae, como hecho de trama** | Lo que la lectora echa de menos va a la ficha siguiente como hecho, no como estilo | **B** | «Vuelve el miedo, y es lo mejor»; «Quiero oírselo» cumplió una petición de tres capítulos |
| **La regla del fork** (ninguna instrucción de prosa antes de escribir) | Las reglas de prosa se aplican después del borrador, para cortar | **C** con indicio fuerte | La prosa aguantó cuatro versiones del método que cambiaron mucho; el modelo que prescribía prosa escribía peor |
| **Lectura de plan antes de escribir** | Las decisiones grandes se dan a lectoras tipo como opciones | **C** | Las decisiones salen de la lectora; aún no hay capítulos que lo midan |
| **Esfuerzo máximo** | Ventanas y orquestador al máximo | Sin atribuir | El primer capítulo en máximo quedó en la misma banda |

---

## 3. Lo que no se toca sin una prueba a ciegas

Estas piezas son las que sostienen la calidad. Cambiarlas, o añadirles una excepción, pide una rama y una **prueba a ciegas**: el mismo capítulo escrito con el método actual y con el cambio, leído por dos editoras con el orden invertido y por la lectora tipo (`SYSTEM_ORCHESTRATION.md`, adenda §7). Si no hay prueba, no entra.

1. **La regla del fork.** Nada que diga cómo escribir antes de escribir. Las mejoras van al cierre, a la lectura o a los tests de diseño.
2. **El cierre obligatorio con acta** (OPERACIÓN C, C-1 a C-10). Un capítulo sin acta no existe.
3. **La lectura por quien no escribió**: agentes nuevos, a la vez, con el paquete del público (sin biblia, brief ni acta).
4. **Manda la lectora tipo**, y se mira el orden de sus notas, no una cifra suelta.
5. **El orquestador no escribe la obra**, y cada pieza la escribe una ventana limpia que solo lee lo que le manda su encargo.
6. **Cortar antes que añadir.** Como mucho tres correcciones; lo demás, a una reescritura.
7. **La pareja primero**: el peso de la pareja medido en el diseño y comprobado después, nunca como consigna de prosa; cada ficha empieza por «Entre ellos».
8. **La medida independiente**: la cuenta de quien escribe es registro, no veredicto.
9. **El gancho en todos los cierres** (la obra puede declarar cierres de descarga, con tope, por diseño; nunca por estilo).
10. **Tres lecturas = confirmado**, y una correctora de continuidad después de cualquier corte que toque más de un capítulo.

Y una que **no se prueba ni se discute: mayores de edad** (`PAREJA_PRIMERO.md` §8).

---

## 4. Lo que costó caro (no repetir)

| Error | Lo que costó | La regla que quedó |
|---|---|---|
| **Un método heredado de otro género** (intriga), con sus reglas apiladas | Cuatro días parados, escaleta nueva, cortes y fusiones de lo escrito, cuatro piezas nuevas; los primeros capítulos se quedan con un 40 % de romance | Al adaptar un método, se quitan las reglas del género de origen y se pone un suelo medible para lo que define el nuevo. Declararlo no basta |
| **Borradores que se saltaron el cierre** y entregas que «existían» solo en el informe | Una versión entera del método; el capítulo 2 sigue siendo el valle | El trabajo se comprueba por lo que existe en el repo (`Hecha si existe…`), nunca por lo que dice la ventana |
| **Tics y muletillas** («cuento hasta tres» siete veces en siete capítulos) | Cortes en cinco capítulos y una segunda pasada | Tics vigilados con techo por obra (C-9) |
| **Repetir lo que la lectora ya leyó** (escenas espejo, resúmenes) | Es el defecto que más vuelve, incluso pedido en el encargo | Un detalle compartido como mucho; se comprueba en el cierre y en la lectura, porque el encargo solo no lo evita |
| **Explicar lo que la escena ya muestra** | Cortes en casi cada lectura | El narrador no explica; el cierre corta y la lectura caza lo que se escapa |
| **Fusiones que rompen costuras** | Cinco costuras graves en una fusión | Correctora de continuidad sin contexto tras cada corte entre capítulos |
| **Demasiados frenazos de la tensión** | «Tres cortes los aguanto; un cuarto, no» | Las interrupciones se cuentan por libro, con tope bajo |
| **Fiarse de la medida de quien escribe** | Un 94 % que era un 35 % | Manda la medida independiente |
| **Rellenar para llegar a una extensión** | Fichas con cifras viejas | La ficha recalcula su extensión; nunca se rellena |
| **Operación**: doce agentes a la vez, compactar la conversación, auditar antes de que la ventana termine | Sesiones agotadas, auditorías de versiones viejas | Unos cuatro agentes a la vez; relevo antes que compactar; antes de auditar, comprobar que no hay commits posteriores |

---

## 5. Cómo trabaja un buen orquestador

- **Encarga qué, nunca cómo.** El NEXT fija qué pasa, qué cambia entre los dos, qué no se sabe todavía y cómo termina; deja a quien escribe las palabras («se decide al escribir»).
- **Hace leer entera la obra** a quien escribe, y dos veces la voz que va a escribir. Las reglas de oficio, al cerrar.
- **Exige un acta contrastable**: si el acta dice que se cortó algo, el texto lo tiene que haber cortado.
- **Lanza las lecturas a la vez**, con agentes nuevos y el paquete del público, y guarda las lecturas en bruto.
- **Apunta cada petición de la lectora con su destino** y comprueba en la lectura siguiente si se cumplió.
- **Pregunta al autor solo lo cerrado**, con las opciones, la recomendada primero y la que prefiere la lectora. Cuando la lectora pide dos veces algo que el diseño tiene cerrado, prepara ya la consulta al autor.
- **Lo guarda todo en el repo**: cuaderno, Anexo A, historial de notas, commits que resumen cada lectura. Un relevo retoma con solo leer el cuaderno.

---

## 6. Lo que no se sabe (y cómo se averiguaría)

| Pregunta | Por qué importa | Cómo se sabría |
|---|---|---|
| ¿La v2.0 escribe mejor o solo diseña mejor? | La prueba a ciegas se canceló; la subida coincide con más pareja por diseño | Un capítulo de la segunda saga escrito con y sin el cambio que se quiera medir |
| ¿Qué pieza del paquete v1.1 da la prosa: el cierre, la lectura, el brief o no prescribir? | Solo hay una prueba, del paquete entero | Pruebas a ciegas quitando una pieza cada vez |
| ¿Qué medida de pareja predice el enganche? | Acta, editora, auditoría y lectora dan cifras distintas | Cruzar las cuatro con la nota de la lectora en la segunda saga |
| ¿La lectora tipo predice a lectoras reales? | No hay ningún dato humano todavía | Lectoras beta o ARC del libro 1 y comparar con el orden de la lectora tipo |
| ¿Qué nota usar para el listón? | La primera nota de un capítulo nuevo es más baja que la de la relectura siguiente | Fijar la regla tras unas cuantas relecturas más |
| ¿El calor funciona en página? | Los suelos de calor de la v2.0 caen en capítulos aún sin escribir | Las lecturas de esos capítulos |
| ¿El método funciona en otra saga? | Solo se ha escrito una obra | La segunda saga: la prueba de fuego |
| ¿Importa el esfuerzo máximo? | Se decidió sin prueba | Una prueba a ciegas de un capítulo |

---

*El manual se pone al día cuando una pieza cambia de grado de evidencia o entra un error nuevo en la tabla del §4. Lo que cambia la fábrica va al `CHANGELOG.md`.*
