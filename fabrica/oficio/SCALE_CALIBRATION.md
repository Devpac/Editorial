<!-- MODELO_DarkRomance v2.0 — SCALE_CALIBRATION: base agnóstica v7 (verbatim) + adenda de dark romance (v2.0) -->

# SCALE_CALIBRATION.md

## PROPÓSITO

La arquitectura operativa de una novela depende de su escala.
Una novela de 80.000 palabras y una de 250.000 no admiten las
mismas decisiones estructurales, aunque se llamen igual.

Sin calibración de escala, el sistema tiende por defecto
a la novela media occidental (90-120k palabras) y falla
tanto en la brevedad como en la longitud.

JERARQUÍA: Capa 1.5 (entre THEMATIC_ENGINE y STORY_SPINE).
STORY_SPINE no puede construirse sin escala declarada.

---

## DECLARACIÓN DE ESCALA

LONGITUD OBJETIVO: [palabras totales, rango aceptable]

Referencias de escala:
- Novela corta: 40.000 – 60.000 palabras
- Novela media: 70.000 – 110.000 palabras
- Novela larga: 120.000 – 180.000 palabras
- Novela extensa: 200.000+ palabras

CAPÍTULOS PREVISTOS: [número o rango]

LONGITUD MEDIA DE CAPÍTULO: [palabras]

PROPORCIÓN DE DIÁLOGO vs NARRACIÓN: [aproximada]

SI EL PROYECTO ES MULTIVOLUMEN:
Declarar longitud total de serie (suma de libros previstos)
y verificar en SERIES_ARCHITECTURE.md la compatibilidad entre
escala de libro y escala de serie. Un libro de 200k dentro
de una tetralogía de 800k tiene economía estructural
distinta a un libro único de 200k.

RELACIÓN CON AESTHETIC_REGISTER.md:
Régimen minimalista → tiende a novela corta o media.
Régimen expansivo → tiende a novela larga o extensa.
Régimen naval-decimonónico → tiende a episódica larga.
Si hay incompatibilidad entre el régimen declarado y la escala
declarada, revisar uno u otro antes de seguir.

---

## CÓMO LA ESCALA MODIFICA LA ARQUITECTURA

### NOVELA CORTA (40-60k)

STORY_SPINE:
- Plantilla preferida: tres actos comprimidos, kishōtenketsu,
  o circular.
- Punto de giro 1: entre 15-25% (antes que en novela media).
- Crisis: entre 65-75%.
- No hay espacio para subtramas significativas; toda subtrama
  compite con el arco principal.

CHARACTER_PHYSICS:
- 1-2 personajes con física completa.
- Antagonista puede ser interno (la propia herida del protagonista
  encarnada en situaciones) sin antagonista externo.
- Secundarios: máximo 3-4 con voz individualizada.

CHAPTER_BRIEF:
- Capítulos cortos: 1.500-3.500 palabras.
- Cada capítulo debe hacer al menos dos cosas (establecer + escalar).

DEUDAS NARRATIVAS:
- Número bajo: 3-5 deudas abiertas como máximo simultáneo.
- Ventana entre setup y payoff: 5-15 capítulos.

INFORMATION_CHOREOGRAPHY:
- 2-4 hechos activos simultáneos como máximo.
- Cadencia rápida; pocas siembras, ecos próximos.

RIESGO PRINCIPAL:
Falta de respiración. Todo está apretado y el lector no tiene
momentos de sedimentación.

### NOVELA MEDIA (70-110k)

STORY_SPINE:
- Plantilla estándar: cualquiera, con ajustes.
- Tres actos con punto de giro 1 alrededor del 25% y crisis
  alrededor del 75%.
- Cabe una subtrama significativa además del arco principal.

CHARACTER_PHYSICS:
- 2-3 personajes con física completa.
- Antagonista externo con ficha propia.
- Secundarios con voz: 4-6.

CHAPTER_BRIEF:
- Capítulos de 3.000-6.000 palabras.
- Cada capítulo tiene función declarable; algunos pueden ser
  de sedimentación.

DEUDAS NARRATIVAS:
- 5-8 deudas abiertas simultáneas.
- Ventana setup-payoff: 8-25 capítulos.

INFORMATION_CHOREOGRAPHY:
- 4-8 hechos activos simultáneos.
- Cadencia moderada; siembras y ecos bien espaciados.

RIESGO PRINCIPAL:
Flacidez en el Acto II. Es donde el sistema necesita más
vigilancia.

### NOVELA LARGA (120-180k)

STORY_SPINE:
- Plantilla flexible; admite episódica con arco, coral, o tres
  actos con subestructuras.
- Los puntos de giro pueden ser múltiples.
- Cabe más de una subtrama, cada una con su propia estructura
  interna.

CHARACTER_PHYSICS:
- 3-5 personajes con física completa.
- Sistema de relaciones significativo (varias fichas de
  RELATIONSHIP_PHYSICS).
- Secundarios con voz: 6-10.

CHAPTER_BRIEF:
- Capítulos variables: de 2.000 (bisagras) a 10.000 (sostenidos).
- Función más rica: a veces dos funciones por capítulo, a veces
  un capítulo se dedica a una sola función sostenida.

DEUDAS NARRATIVAS:
- 8-15 deudas abiertas simultáneas.
- Ventana setup-payoff: muy amplia, hasta 40-50 capítulos.

INFORMATION_CHOREOGRAPHY:
- 6-12 hechos activos simultáneos.
- Cadencia amplia; trayectorias largas de cinco fases.

RIESGO PRINCIPAL:
Pérdida de foco temático. A esta escala es fácil que la pregunta
central se diluya. OPERACIÓN D debe ser estricta.

### NOVELA EXTENSA (200k+)

STORY_SPINE:
- Suele requerir estructura modular: partes, libros, secciones
  con sus propios arcos internos y un metaarco que las integra.
- Plantilla típica: episódica con arco (sagas navales, fantasía
  épica) o coral expandida.

CHARACTER_PHYSICS:
- 5-8 personajes con física completa si es coral.
- Sistema de relaciones complejo.
- Secundarios con voz: 10-15.
- Se acepta promover secundarios a protagonistas en secciones
  propias.

CHAPTER_BRIEF:
- Capítulos muy variables; la unidad operativa puede ser
  "la sección" más que el capítulo.

DEUDAS NARRATIVAS:
- Se necesitan registros jerárquicos: deudas de sección
  vs. deudas de novela completa.
- Ventana setup-payoff puede cubrir toda la novela.

INFORMATION_CHOREOGRAPHY:
- 10+ hechos activos simultáneos.
- Cadencias solapadas; coreografía compleja.

RIESGO PRINCIPAL:
Deriva. La novela puede cambiar de tema a mitad sin que el autor
lo note. OPERACIÓN D debe ejecutarse más frecuentemente (cada
2-3 capítulos).

---

## MAPA DE PRESIÓN POR ESCALA

Posición aproximada de los eventos estructurales según longitud.
Los porcentajes son orientativos; la plantilla elegida los modifica.

| Evento estructural | Novela corta | Media | Larga | Extensa |
|---|---|---|---|---|
| Detonante | 5-10% | 8-15% | 10-15% | 10-18% |
| Punto de giro 1 | 15-25% | 20-28% | 22-30% | 25-33% |
| Punto medio | 45-55% | 48-55% | 48-55% | 48-55% |
| Crisis | 65-75% | 72-80% | 75-82% | 78-85% |
| Punto de giro 2 | 75-85% | 80-88% | 82-90% | 85-92% |
| Clímax | 85-95% | 88-95% | 90-95% | 92-97% |

Estos valores se incluyen en CHAPTER_BRIEF.md
(posición estructural) para orientar cuándo escribir qué.

---

## PACING POR ESCALA

La densidad de suceso por unidad de palabra no es constante.

NOVELA CORTA: alta densidad. Cada escena carga mucho.
Pocas escenas de sedimentación.

NOVELA MEDIA: densidad variable. Se permite respirar entre
picos; se requieren 2-3 escenas de sedimentación por cada
escena de alta intensidad.

NOVELA LARGA: densidad moderada por defecto, con picos.
Mucha sedimentación legítima. El arco emerge por acumulación
tanto como por eventos.

NOVELA EXTENSA: densidad baja por defecto. El mundo, los
personajes y las relaciones tienen tiempo propio. Los picos
son más espaciados y más intensos.

TENSION_MECHANICS.md modula su operación según la densidad
declarada aquí.

CALIBRACIÓN DE CUOTAS DE PROSA SOBRE LA DENSIDAD DE FONDO.
La densidad de suceso por unidad de palabra declarada en esta
sección es la densidad de fondo sobre la que se calibran las
cuotas cuantitativas de PROSE_LINE_DISCIPLINE.md. La escala
declarada (corta, media, larga, extensa) determina cuánto
cambio puede sostener la prosa sin sobrecargarse: una novela
extensa con densidad baja admite trayectorias largas de
modificación adjetival y nominal porque tiene espacio para
sostenerlas; una novela corta con densidad alta exige
disciplina más estricta porque cada página carga mucho
suceso. Las cuotas concretas (CUOTA 1 a CUOTA 8 por mil
palabras) viven en aquel archivo y se modulan por el régimen
estético declarado en AESTHETIC_REGISTER. La conexión opera
en una sola dirección: SCALE_CALIBRATION declara densidad de
fondo; PROSE_LINE_DISCIPLINE aplica cuotas que respetan esa
densidad. Si una incompatibilidad aparece (cuotas exigentes
de minimalista combinadas con escala extensa, o cuotas
permisivas de expansivo combinadas con escala corta), el
proyecto revisa la combinación antes de seguir.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — RATIO DE DEUDAS
Contar deudas abiertas en un momento dado. ¿Entra en el rango
recomendado para la escala? Si no, revisar STORY_SPINE.

TEST 2 — VENTANA SETUP-PAYOFF
Para cada deuda, ¿la ventana es coherente con la escala?
Ventana demasiado corta en novela extensa: el pago se siente
atropellado. Ventana demasiado larga en novela corta: el lector
ya no recuerda el setup.

TEST 3 — DENSIDAD DE SUCESO
Leer tres capítulos seguidos al azar. ¿La densidad de suceso
coincide con la declarada? Si un capítulo aparentemente de
sedimentación ocurre en novela corta donde no hay espacio para
sedimentar, redistribuir o eliminar.

TEST 4 — COMPATIBILIDAD CON SERIE
Si aplica: ¿la escala declarada del libro es compatible con
la longitud total de serie? Un libro de escala extensa en una
serie corta puede desequilibrar; un libro corto en serie
extensa puede sentirse como interludio.

---

## ERROR COMÚN

Escribir una novela corta como si fuera media, o viceversa,
produce síntomas distintos:

Novela corta tratada como media: el lector se aburre al comienzo,
el final se acelera y no funciona.

Novela media tratada como corta: la segunda mitad se queda sin
material y se repite.

Novela larga tratada como media: faltan arcos menores, la novela
se siente esquelética.

Novela media tratada como larga: subtramas que no aportan,
personajes secundarios sobredimensionados.

Diagnosticar el síntoma y recalibrar.

---

## RELACIÓN CON OTROS ARCHIVOS

SCALE_CALIBRATION.md alimenta:
- STORY_SPINE.md (plantilla y ritmo)
- CHAPTER_BRIEF.md (longitud y función de capítulos)
- CHARACTER_PHYSICS.md (número de personajes con física completa)
- WORLD_TEXTURE.md (densidad de textura admisible)
- TENSION_MECHANICS.md (pacing)
- INFORMATION_CHOREOGRAPHY.md (número de hechos activos
  simultáneos admisibles)
- PROSE_LINE_DISCIPLINE.md (densidad de fondo sobre la que se
  calibran las cuotas cuantitativas de prosa de línea; la
  escala determina cuánto cambio puede sostener la prosa sin
  sobrecargarse)

SCALE_CALIBRATION.md se coordina con:
- SERIES_ARCHITECTURE.md (si multivolumen, cruzar escala de
  libro con escala de serie)

SCALE_CALIBRATION.md se revisa:
- Al inicio.
- Si a mitad el sistema detecta que la escala real se desvía
  significativamente (>20%) de la declarada.


---
---

