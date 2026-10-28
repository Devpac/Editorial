<!-- Fábrica v3.0 — plantilla de GÉNERO (vale para cualquier saga de dark romance). Los valores de la obra viven en su preset: PRESET_<OBRA>.md (la obra activa la dice el LEEME). -->

# ROMANCE_BEAT_MAP.md — Fábrica v3.0

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

> La pareja es la trama A (`PAREJA_PRIMERO.md`, que manda en el peso de la pareja).

## PROPÓSITO

La pareja es la **trama A** de cada libro; la trama del libro (*Variante: dark romance policial:*
la investigación criminal) es la **trama B**. Este archivo fija los beats de la pareja con su
porcentaje de libro y su suelo, subordina a ellos los de la trama B y gradúa, libro a libro, la
escala de rendición. El calendario de calor vive aquí, en % del libro, y lo coloca la escaleta;
qué se muestra lo decide HEAT_DISCIPLINE.

JERARQUÍA: Capa 1, con prioridad sobre STORY_SPINE.md: la columna de cada libro es la de la
pareja, y STORY_SPINE trenza la trama B sobre ella. Si chocan la resolución de la trama B
(*Variante: dark romance policial:* el caso policial) y la relación, **gana la relación**. El peso
de la pareja (objetivo 80 %, suelo 70 %) y cómo se mide: GENRE_CONVENTIONS, regla 1, y
`PAREJA_PRIMERO.md` §2.

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Propósito en la obra.
> *Qué declara aquí la obra:* el nombre de la saga, su género secundario, su pareja y su peso de pareja.

---

## PRINCIPIO OPERATIVO DEL DARK ROMANCE

La trama del libro es el espejo del conflicto de pareja (GENRE_CONVENTIONS, regla 2): se elige
DESPUÉS de definir el tema emocional del libro. **La trama B entra por la pareja:** cada beat suyo
se convierte en choque, proximidad forzada, obstáculo o moneda entre ellos, y el dato que puede
llegar dentro de una escena de pareja llega ahí (`PAREJA_PRIMERO.md` §5). Rige la prohibición de la
«escena limpia» (GENRE_CONVENTIONS, regla 5): como mucho una de cada cuatro escenas mueve solo la
trama B sin ser página de pareja, y la que pasa de ese cupo no es escena (GENRE_CONVENTIONS, reglas
1, 2 y 5). *Variante: dark romance policial:* el crimen es el espejo, el caso se elige después y la
escena limpia prohibida es la de investigación.

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Principio operativo en la obra.
> *Qué declara aquí la obra:* quiénes son los dos protagonistas que la escena del género secundario pone en tensión.

---

## LOS BEATS DE LA PAREJA (trama A)

Posición por defecto en % del libro; la escaleta la fija capítulo a capítulo. Los suelos son los
de `PAREJA_PRIMERO.md` §3: la obra puede adelantarlos en su preset; retrasarlos es decisión del
autor, con su porqué en la biblia.

| Beat | Posición por defecto | Suelo (como tarde) |
|---|---|---|
| **Apertura con el protagonista peligroso (por defecto, él).** Él, o su presencia o su amenaza, antes que la trama B; el capítulo 1 promete la pareja (GENRE_CONVENTIONS, regla 3) | 0–5 % | Capítulo 1 |
| **Primer cara a cara.** Los dos en la misma escena (un prólogo que adelanta una escena de los dos cuenta) | 0–10 % | 10 % |
| **Contacto con carga.** El primer roce que pesa (el que tenga la obra: combate, cura, proximidad forzada…) | 10–20 % | 20 % |
| **Lo que los ata.** Una decisión de uno de los dos (no soltar al otro, vigilarlo, no delatarlo, aceptar un trato) los deja pegados; la trama B pone la excusa | 15–30 % | — |
| **Primer beso o equivalente** | 25–45 % | 45 % |
| **Punto de no retorno.** La pareja cruza una línea (ética, legal o entre ellos) y eso mueve la trama B | ≈ 50 % | — |
| **Primera escena explícita** | 40–60 % | 60 % |
| **Desde el contacto con carga: una escena con carga** (desde la primera escena explícita, de calor o *edging*) | cada 3–4 capítulos | nunca más de 4 capítulos seguidos sin ella |
| **La crisis de la pareja.** Lo que se rompe entre ellos (una verdad, una traición, una retirada); el clímax de la trama B sale de aquí | 75–90 % | — |
| **La entrega del libro.** Lo que entrega de sí en este libro quien se rinde (escala de rendición, abajo) | Donde la declare la obra | Una por libro |
| **El cierre**, según la forma de la saga (SERIES_GLUE, adenda de dark romance) | 95–100 % | — |

**El cierre en la saga con la misma pareja (formas A y B, salvo el último libro de la B, que cierra la pareja):** cliffhanger emocional. **No hay HEA (final feliz)
por libro.** El libro termina con una herida abierta en la relación, un secreto revelado a medias
o un avance crítico del reloj que cerca a la pareja, si la saga lo tiene, garantizando el salto al siguiente
volumen.

En los libros siguientes con la misma pareja, «primer» quiere decir el primero de ese libro (el
primer cara a cara es el reencuentro después del salto): el deseo, el contacto y el sexo vuelven
en cada libro con sus suelos (`PAREJA_PRIMERO.md` §4). Con parejas rotativas, cada libro es el del
encuentro de su pareja y cierra en su final feliz.

## LOS BEATS DE LA TRAMA B (subordinados)

Sin mínimo: lo que no es pareja (trama B, trama horizontal y elenco cuando su página no es de
pareja), como mucho el 30 % del libro (`PAREJA_PRIMERO.md` §3), y la trama B, con sus mecanismos
(pistas, señuelos, sospechosos, procedimiento), dimensionada para caber en ese techo (CLUE_LEDGER).
Ninguno tiene escena propia si puede ocurrir dentro de una escena de pareja.

- **EL DETONANTE ESPEJO (5–15 %).** Refleja de forma monstruosa la grieta entre ellos y los pone
  en la misma habitación. *Variante: dark romance policial:* el caso espejo, detonante policial.
- **LA ESCALADA (15–75 %).** Cada paso de la trama B es choque, proximidad forzada, obstáculo o
  moneda entre ellos, sin llegar jamás a la infidelidad emocional real (GENRE_CONVENTIONS,
  PELIGRO 1).
- **LA MIGA DE PAN HORIZONTAL (60–85 %)**, si la saga tiene trama horizontal: obligatoria por libro
  (GENRE_CONVENTIONS, regla 9); llega en una coyuntura crítica de la pareja y se cobra entre ellos.
- **LA RESOLUCIÓN DE LA TRAMA B (85–95 %).** Cae el antagonista del libro (justicia negociada u
  oscura, no institucional), y la desencadena una decisión de la pareja. La trama del libro se cierra en el volumen. *Variante: dark romance policial:*
  resolución del caso; cae el monstruo de la semana.

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Beats en la obra.
> *Qué declara aquí la obra:* cuántos libros tiene la saga; el porcentaje de cada beat de pareja en sus libros, si adelanta algún suelo (o el autor retrasa alguno, con la decisión de su biblia); y, si los tiene, sus paletas, de qué trata su trama horizontal, quién o qué cerca a la pareja y cómo usa la pareja la trama B en la escalada.

---

## LA ESCALERA DE RENDICIÓN MACRO (Arcos de la saga)

El sexo explícito en página es recurrente, no es la moneda escasa. La verdadera moneda es la
rendición del protagonista que declare la obra (por defecto, el hermetismo de él). **De un libro a otro se raciona la confesión, no el contacto**
(`PAREJA_PRIMERO.md` §4): la identidad, los secretos, las verdades que se dicen, los nombres. El
deseo, el contacto y el sexo tienen su suelo en todos los libros (tabla de beats). La escala mide
lo que se entregan, no lo que se tocan.

La obra declara cada peldaño con su libro o, si la escalera cabe en un libro, con su tramo:
- **Libro [N]:** [qué se entregan en ese libro: qué confiesa quien se rinde, qué sabe el otro de él].
- **Libro [N]:** […]
- **Libros posteriores:** [progresión hacia la entrega mayor, con su libro].

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Escalera de rendición de la obra.
> *Qué declara aquí la obra:* quién se rinde, en qué libro (o, si la escalera cabe en un libro, en qué tramo) cae cada peldaño de su rendición, hasta la entrega mayor, y el ritmo de consumación de cada libro dentro de los suelos (HEAT_DISCIPLINE).

---

## LOS PUNTOS DE CRUCE OBLIGATORIOS (El anudado de las dos tramas)

Una decisión de la pareja mueve la trama B; nunca al revés.

1. Lo que uno hace con el otro (acercarse, apartarse, protegerlo, vigilarlo, darle celos) abre o
   empuja la trama B, y lo que el otro hace con ello cambia el estado de esa trama.
2. Cada línea que la pareja cruza (ética, legal o entre ellos) produce la siguiente revelación o
   el siguiente obstáculo de la trama B.
3. Si la saga tiene trama horizontal, la miga de pan cae en una coyuntura crítica de la pareja y
   se cobra entre ellos: cambia lo que uno sabe del otro, lo que uno le calla, o algo entre ellos.

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Puntos de cruce en la obra.
> *Qué declara aquí la obra:* cómo cruza su pareja las dos tramas (qué hace uno con el otro que mueve la trama B, y qué líneas cruzan y qué destapa eso), de qué trata la miga de pan horizontal de su protagonista, si la saga tiene trama horizontal, y quién detona los instintos posesivos del protagonista posesivo, si lo hay.

---

## UMBRALES DE CONTROL

Se comprueban en la escaleta, antes de encargar cada bloque, y en OPERACIÓN D, después de
escribirlo (junto con TENSION_MECHANICS.md). Lo que falla en la escaleta se reescaleta antes de
encargar; lo que falla en lo escrito se corrige en el bloque siguiente (`PAREJA_PRIMERO.md` §2).

| Checkpoint | Elemento a auditar | Si no lo está |
|---|---|---|
| Primera pág. | Él o su perspectiva, presencia o amenaza; el capítulo 1 promete la pareja | Alerta: si abre con la trama del libro (*Variante: dark romance policial:* si hay cadáver, es procedimental). Revertir. |
| 10 · 20 · 45 · 60 % | Primer cara a cara, contacto con carga, primer beso, primera escena explícita: cada uno en su suelo o antes | **Alerta crítica:** la trama A va tarde. |
| Cada bloque de cuatro capítulos | Peso de pareja ≥ 70 % (o el suelo que declare el preset); ningún capítulo sin el otro; desde el primer cara a cara, nunca más de dos seguidos sin los dos en escena (salvo ausencia declarada con tope); desde el contacto con carga, nunca más de cuatro capítulos seguidos sin escena con carga (HEAT_DISCIPLINE) | **Alerta crítica:** se reescaleta el bloque siguiente. |
| Por capítulo | Escena limpia: cuenta en el cupo de una de cada cuatro escenas que mueven solo la trama B (GENRE_CONVENTIONS, regla 5) | Alerta: con el cupo lleno, la escena que avanza solo la trama del libro sin ser página de pareja es resumen. |
| 60-85 % | La Miga de Pan Horizontal (si la saga tiene trama horizontal), cobrada entre ellos | Alerta crítica: si no hay pista tangible de la trama horizontal, el libro se estanca. |
| 95-100 % | Cliffhanger emocional / Coda envenenada (saga con la misma pareja, formas A y B, salvo el último libro de la B, que cierra la pareja) | Alerta crítica: si hay sensación de HEA cerrado, se ha roto el contrato Dark Romance. |

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Umbrales en la obra.
> *Qué declara aquí la obra:* quién abre la primera página y, si la saga tiene trama horizontal, de qué trata la pista que se audita.

---

## TESTS DE FUNCIONAMIENTO

- **TEST 1 — SIN HEA (saga con la misma pareja, formas A y B, salvo el último libro de la B, que cierra la pareja):** ¿La trama del libro cerró pero la relación quedó en tensión con un cliffhanger emocional?
- **TEST 2 — ESCENA LIMPIA:** ¿Más de una de cada cuatro escenas de la trama del libro no es página de pareja (*Variante: dark romance policial:* reunión de comisaría o autopsia)? La que pasa del cupo va a resumen o se funde en una escena de pareja.
- **TEST 3 — LA MIGA (si la saga tiene trama horizontal):** ¿Se ha entregado información firme sobre la trama horizontal, y se ha cobrado entre ellos?
- **TEST 4 — RENDICIÓN MACRO:** ¿Se ha forzado una confesión emocional de quien se rinde que toca en un libro posterior (o en un tramo posterior del libro) según el canon? Si habla de más, recortar la confesión; nunca el contacto ni el deseo (`PAREJA_PRIMERO.md` §4).
- **TEST 5 — LA TRAMA A EN SU SITIO:** ¿Cada beat de pareja cae en su suelo o antes, y el libro llega al peso de pareja? Un beat que llega tarde es un fallo de escaleta.
- **TEST 6 — CRUCE INVERTIDO:** ¿Cada beat de la trama B lo dispara o lo resuelve una decisión de la pareja? El que se mueve solo va a resumen o se funde en una escena de pareja.

> **Valores de la obra →** `PRESET_<OBRA>.md` › ROMANCE_BEAT_MAP › Tests en la obra.
> *Qué declara aquí la obra:* sobre qué o quién es la información firme que exige la miga, si la saga tiene trama horizontal, y quién confiesa en la escala de rendición.

---

## RELACIÓN CON OTROS ARCHIVOS

ROMANCE_BEAT_MAP.md recibe de:
- `PAREJA_PRIMERO.md` (manda en el peso de la pareja y en los suelos de género).
- GENRE_CONVENTIONS.md (mandatos de Dark Romance, peso de pareja, prohibición de HEA por libro en la saga con la misma pareja, prohibición de escena limpia).
- CHARACTER_PHYSICS.md (la escala de rendición es el arco de defensa de quien se rinde).

ROMANCE_BEAT_MAP.md alimenta:
- STORY_SPINE.md (la trama A, sobre la que se trenza la trama del libro como espejo).
- La escaleta del libro (coloca los beats y el calendario de calor en % del libro; cada ficha empieza por «Entre ellos» y estima su peso de pareja: `PAREJA_PRIMERO.md` §5).
- TENSION_MECHANICS.md (tensión de posesión; la vigilancia, si la obra la tiene).
- HEAT_DISCIPLINE.md (los beats de calor y sus suelos; sexo explícito sin elipsis como campo de batalla).
- CLUE_LEDGER (la miga de pan horizontal, cobrada entre ellos; la trama B, dimensionada para caber en el techo de lo que no es pareja, el 30 %).
