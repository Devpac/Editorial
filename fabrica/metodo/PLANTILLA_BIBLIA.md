# PLANTILLA_BIBLIA.md — la biblia de una saga (Fábrica v3.0)

> Archivo de **modelo**. Es la forma de la biblia que escriben las ventanas B1, B2 y B3 en la fase 1
> (`ORQUESTADOR.md`, §2.1). **No es una lista para rellenar a ciegas:** cada sección dice qué
> decide y por qué lo necesita el resto del modelo. Lo que lleva «si la obra lo tiene» se escribe
> «no aplica» cuando la saga no lo tiene: no se inventa para rellenarlo. Lo marcado 🔒 lo decide
> el autor (o lo aprueba); lo demás, la ventana por delegación, con su línea en el Anexo A. Desde
> la v2.0, la pareja es la trama A (`PAREJA_PRIMERO.md`): la biblia fija su peso (§14 🔒) y cada
> libro empieza por su pregunta (§19).
>
> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

---

## Cómo se escribe

- **Un archivo**, `<obra>_biblia.md`, con cabecera de estado (`v1.0 (fecha: qué)`, y cada versión
  nueva delante de la anterior) y un **Anexo A** de decisiones: una fila por decisión (`A-NN`,
  título, estado, qué se decide, origen y versión).
- **Se escribe en tres tramos** (B1, B2, B3), cada uno en una ventana, partiendo de la ficha de
  premisa (fase 0) y de lo ya aprobado. Cada tramo termina con un **informe** al orquestador: lo
  decidido por delegación, las preguntas 🔒 para el autor (con una opción recomendada) y las dudas.
- **Concreción antes que adjetivos:** nombres, edades, fechas, lugares, cifras. La biblia sirve para
  que una ventana sin contexto escriba un capítulo coherente; lo vago no le sirve.
- **Canon oculto:** lo que la lectora no debe saber hasta un libro concreto se escribe igual, con su
  libro de revelación al lado. Las ventanas de capítulo lo leen «solo para saber».
- **La forma de la saga cambia el reparto** (§18; `SERIES_GLUE.md`, adenda de dark romance). Con la
  misma pareja en todos los libros, §6–§8 son de esa pareja. **Con parejas rotativas**, §6–§8 se
  escriben para la pareja del libro 1, cada libro siguiente trae las fichas de la suya en su diseño
  (§19), y el elenco fijo (§9) es el mundo compartido (la familia, el clan, el club). En un dúo o
  trilogía, la escala de rendición y el ritmo de consumación (§16) se reparten entre sus dos o tres
  libros.

---

## PARTE I — FUNDACIÓN (ventana B1)

1. **La tesis** 🔒 — Qué promete la saga que no promete nadie más (el «océano azul»), en una
   frase, y su propuesta de valor. Validación de mercado si se puede comprobar (fecha de la
   comprobación).
2. **Los pilares del subgénero y su variante** — Qué hace que esto sea el subgénero declarado
   (policial, mafia, bully, romantasy oscura…) y no su vecino. Si no es el policial, **la
   variante**: regla por regla de las que llevan marca de variante en las plantillas de género
   (`GENRE_CONVENTIONS.md`, declaración primaria), qué es aquí la trama del libro, la escena del
   género secundario que no puede ir limpia, el antagonista del libro, la impunidad o su
   equivalente y la anti-firma; o «no aplica». Pasa al preset.
3. **Posicionamiento** 🔒 — Frente a los géneros vecinos (p. ej., romantic suspense): qué se hace
   aquí que allí no, y qué no se hace nunca.
4. **Público y comparables** — Lengua y variedad, canal de publicación y precio; comparables a los
   que se apunta y de los que se huye; **perfil de la lectora** (edad, plataforma, qué busca, qué
   la hace abandonar). De aquí sale la lectora tipo de `PROTOCOLO_LECTURA.md` §5. Pasa al preset
   (Cabecera › Mercado y lengua; si la obra no declara otro, valen los valores por defecto que da
   esa ranura).
5. **Marca** 🔒 — Nombre de la saga, fórmula de títulos, los datos de catálogo que pide el canal
   de publicación que declare la obra (título y subtítulo de tienda, palabras clave, categorías),
   dirección de portada, **advertencias de contenido**.
6. **Protagonista A** 🔒 — Datos duros; cronología verificada (y absoluta de la saga, año a año);
   descripción física; personalidad; su refugio sensorial (un oficio, un objeto, un lugar), si lo
   tiene; **el defecto** (el que la lectora le perdona y la saga explota); el trauma motor; el
   idiolecto.
7. **Protagonista B** 🔒 — Ficha técnica; perfil físico y estética; anclaje sensorial; personalidad y
   comportamiento; los tropos que activa (y por qué venden); **el pasado**; el idiolecto.
8. **El sistema de trauma** — Lo que cada uno carga y cómo se tocan las dos heridas (el nexo, si lo
   hay). Si la saga tiene trama horizontal que sale de ellas: el remate y la **regla de migas**
   (cuánto se revela y cuándo).
9. **Elenco fijo** — Pocos (el número lo fija la obra, con su porqué), cada uno con función, voz y
   destino. Notas de uso.
10. **El antagonista de la saga** 🔒 (si la obra lo tiene) — Su identidad y cuándo se revela; por
    capas o arcos, si los tiene.
11. **Lo que sostiene y lo que cerca a la protagonista** (o a la pareja) — Qué la sostiene y qué la
    amenaza en su mundo (la familia, el clan, la institución, la ley), y quién la persigue, si
    alguien la persigue.
12. **Escenario y logística** — Los escenarios recurrentes, como la obra los organice, y el
    **espacio propio** de la pareja o de un protagonista, si lo tiene (el que se carga de sentido a
    lo largo de la saga).
13. **Los relojes de la saga** (si los tiene) — Las cuentas atrás que corren por debajo de los
    libros, con el libro en que empieza y en el que suena cada una.
14. **Las reglas duras** 🔒 — Las que no se discuten. **El peso de la pareja** *(v2.0)*, con
    número, suelo y unidad: por defecto, los de `PAREJA_PRIMERO.md` (objetivo 80 % y suelo 70 %, por
    bloque de cuatro capítulos y por libro, en palabras medidas con su §2; lo que no es pareja, como
    mucho el 30 %, sin mínimo), y los suelos de género de su §3 que la obra sube; bajar cualquiera del suelo es
    decisión del autor, con su porqué aquí. Y quién es cada rol de la pareja (protagonista A y B,
    sus géneros, quién narra, quién raciona su confesión…: `PRESET_<OBRA>.md` › Cabecera ›
    Correspondencia de roles), persona y tiempo, cuántos narradores y su reparto (con más de uno,
    el que declare la obra), cómo se abre cada libro, qué espejo hay entre la trama del
    libro y la pareja. Pasan al preset.

## PARTE II — ARQUITECTURA DE LA SAGA (ventana B2)

15. **Tropos y peligros del género para esta obra** — Cómo se gestionan aquí los peligros conocidos
    (`GENRE_CONVENTIONS.md`), qué comportamientos oscuros son canónicos en quien da miedo
    (protagonista B por defecto), cómo
    funciona la tensión sin consumar, pecados capitales y tests de género.
16. **El refuerzo intermitente** 🔒 — Cómo evoluciona el conflicto a lo largo de la saga; **ritmo
    de consumación por libro** (qué pasa en el cuerpo y qué en lo emocional, libro a libro);
    **la escala de rendición** (lo que entrega quien raciona su confesión, y en qué libro: es la
    moneda escasa); los giros, y, si la obra los tiene, sus inversiones, su catálogo de torturas
    (las descargas falsas del anhelo) y su regla de mortalidad.
17. **Estructura interna de cada libro** — Los no negociables de cada volumen; si cada libro cambia
    de escenario o de tipo de conflicto, la malla y su rotación.
18. **La forma de la saga y sus arcos** 🔒 — La forma (`SERIES_GLUE.md`, adenda de dark romance:
    la misma pareja en muchos libros, dúo o trilogía, o parejas rotativas en un mundo compartido):
    qué cierra cada libro, qué deja abierto y dónde cae el final feliz. Los bloques de libros, con
    su pregunta.
19. **La tabla maestra de títulos** 🔒 — Un renglón por libro (título, qué pasa entre ellos, mundo,
    conflicto, qué se revela) y títulos de reserva. Y una subsección por libro, **«Libro N —
    <título>: decisiones de diseño»**: la del libro 1 la escribe B2; la de cada libro siguiente se
    escribe al abrirlo (fase 2a, `ORQUESTADOR.md`, §2.8) y se transcribe aquí cuando el autor la
    aprueba. Campos, en este orden *(v2.0)*: **la pregunta de la pareja** (cerrada: la que mueve el
    libro y que el libro contesta en página; abre el arco de pareja del libro, `BRIEFING.md`, campo
    2 bis) y **entre ellos** (qué cambia entre los dos, de dónde a dónde); el tema emocional y la
    trama del libro que es su espejo (*Variante: dark romance policial:* el caso), por lo que les
    hace: qué los junta, qué los enfrenta, qué los separa; el antagonista del libro, la elección
    costosa, el final y el gancho de cierre, las concreciones (personas, fechas, lugares), lo que
    entrega de la trama horizontal (si la hay), el peldaño de la escala de rendición, el calor del
    libro y dónde cae (dentro de los suelos de `PAREJA_PRIMERO.md` §3), el peso de la pareja si se
    aparta del de §14, las deudas que paga y las que abre, el tiempo desde el libro anterior y **qué
    hace este libro que el anterior no podía hacer**.
20. **Extensión, ritmo y puertas de salida** — Palabras por libro, capítulos, horquilla de capítulo;
    cuántos libros están comprometidos y dónde puede cerrarse la saga limpiamente si hace falta.

## PARTE III — RÉGIMEN (ventana B3)

21. **El régimen estético** — Qué prosa (popular-eficiente, literaria, mixta), qué permisos
    (metáfora, abstracción emocional, explicación narratorial) y sus medidas, que desde la v2.0 son
    siempre **alarma** de cierre, nunca cuota (las cuotas previas a la escritura matan la prosa:
    PROSE_LINE_DISCIPLINE, adenda).
22. **La forma de la extensión y el reparto** — Capítulos de una escena o de varias, y cómo se
    reparten las palabras entre narradores dentro de §14. El reparto entre la pareja y la trama no
    se decide aquí: es el peso de la pareja de §14 🔒.
23. **La columna** — Sujeto: la pareja, que es la trama A (`PAREJA_PRIMERO.md` §1). Motor: la
    pregunta de la pareja de cada libro (§19). Plantilla de cada libro (STORY_SPINE, adenda), con la
    trama del libro trenzada sobre ella como trama B.
24. **El régimen de líneas** — Las líneas de trama y su mapa.
25. **El calendario de fábula** — Cómo se mueve el tiempo (fechas en página o no, saltos, vueltas
    atrás permitidas).
26. **La pregunta central y el régimen temático** — Qué pregunta se hace la saga y cómo evoluciona
    (es de la pareja: THEMATIC_ENGINE, adenda).
27. **El arco de mundo** — Ejes del mundo y su evolución.
28. **Las capas del mundo y su jerarquía sensorial** — Qué se ve, se oye, se huele en cada capa, y
    las paletas de cada narrador, si las tiene (pasan al preset).
29. **El idiolecto** — Cómo habla cada narrador y cada personaje fijo; tics propios (pasan al preset
    como «tics vigilados»).
30. **El género declarado y las leyes del mundo** — El **contrato de género** con los campos que pide
    `GENRE_CONVENTIONS.md` (subgénero, calor, consentimiento, final de libro y de saga, lo que
    nunca pasa).
31. **Inertes declarados** · 32. **Reservas y materia amparada** · 33. **Carga de investigación**
    (qué hay que comprobar y qué capítulos bloquea) · 34. **El principio de serie** (la forma de §18
    aplicada: si cada libro se puede leer sin el anterior, cómo se pasa de uno a otro, cuánto tiempo
    pasa entre libros).

## ANEXOS

- **Anexo A — Registro de decisiones.** Toda decisión, desde la fase 0, con número.
- **Anexo B — Elenco completo, números canónicos y frases de referencia interna.**

---

## Tests de la biblia (los aplica la auditoría; la ventana no escribe contra ellos)

1. **¿Se puede escribir el capítulo 1 con esto?** Una ventana sin contexto, ¿sabría quiénes son,
   dónde están, cómo hablan y qué promete la pareja?
2. **¿La lectora tipo lo leería?** Lectura de una biblia (`PROTOCOLO_LECTURA.md` §6 bis):
   ¿compraría el libro 1 con esta promesa? ¿Qué le sobra y qué echa de menos?
3. **¿Hay moneda escasa?** El ritmo de consumación y la escala de rendición dan algo que esperar en
   cada libro sin gastar la saga.
4. **¿Se contradice?** Fechas, edades, quién sabe qué y cuándo (correctora de coherencia, §6 bis).
5. **¿Está todo lo que pide el preset?** Cada ranura de `PLANTILLA_PRESET.md` tiene su respuesta en
   la biblia, o una pregunta abierta para el autor.
6. **¿La pareja mueve la saga y cada libro?** *(v2.0)* La pregunta de cada libro (§19) y la columna
   (§23) son de ellos; el peso de la pareja (§14) tiene número, suelo y unidad, y si algo baja del
   suelo de género, la decisión del autor está escrita.
