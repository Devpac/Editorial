<!-- MODELO_DarkRomance v2.0 — plantilla de GÉNERO (vale para cualquier saga de dark romance). Los valores de la obra viven en su preset: PRESET_<OBRA>.md (la obra activa la dice el LEEME). Historia: convertida desde el modelo agnóstico v7 el 08-08-2026; separada de la obra el 22-10-2026; v2.0, «la pareja primero» (PAREJA_PRIMERO.md), el 22-10-2026. -->

# CHARACTER_PHYSICS.md — MODELO_DarkRomance v2.0

## PROPÓSITO

Este archivo define la física interna de cada personaje con arco: no es
backstory ni caracterización, es el sistema de fuerzas que gobierna qué puede y
qué no puede hacer en cualquier escena de la saga. Un personaje sin física
reacciona a la trama pero no la tensiona; uno sin coste acumulado es el mismo al
final que al principio. En una saga con **la misma pareja** (la forma de la saga
la declara la obra: SERIES_GLUE, adenda de dark romance) el riesgo se multiplica:
si la física de protagonista A y de protagonista B no está declarada al dígito, la
lectora obtiene la misma escena una vez por libro.

**Este archivo, con el preset de la obra, es donde vive el canon de personajes
de la saga.** No es una plantilla hueca: los dos protagonistas tienen ficha
completa y cerrada; el elenco fijo y los personajes-bisagra, ficha de función
cerrada. Lo único que se rellena por instancia es **el antagonista de ese libro**
(*Variante: dark romance policial:* el villano de la semana) y **el estado
evolutivo de la pareja en ese volumen** (posición en la escala de rendición, fase
del arco de defensa, coste ya pagado); con parejas rotativas, también las dos
fichas de la pareja de cada libro. Lo demás es vinculante.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Propósito.
> *Qué declara aquí la obra:* cuántos libros tiene la saga, quiénes forman su pareja fija (o sus parejas, si rotan) y qué personajes tienen ficha cerrada.

JERARQUÍA: Capa 1. GENRE_CONVENTIONS no tiene precedencia sobre este archivo.
Los datos duros proceden de la biblia y son vinculantes al dígito —edades,
alturas, años, número de libro—: no se ajustan por conveniencia de escena.

---

## TIPOS DE PERSONAJE

Cuatro tipos, y no todos necesitan la misma ficha.

- **PROTAGONISTA (física completa, Plantilla A).** Deseo doble, herida,
  mecanismo, coste, arco de defensa. Hay **dos**: protagonista A y protagonista
  B, los dos POV. En una saga con la misma pareja son **fijos y para siempre**:
  ninguno se sustituye ni rota.
- **ANTAGONISTA (física especular, Plantilla B).** Comparte pregunta con los
  protagonistas y la resuelve con el mecanismo opuesto. Se instancia **por
  libro** (el antagonista del libro; *Variante: dark romance policial:* el villano
  de la semana) y, si la saga lo tiene, **por arco** (el transversal, por capas).
- **SECUNDARIO (función, no física; Plantilla C).** Sin arco propio: función
  dramática y voz. Darles física completa diluye a la pareja. El elenco fijo es
  **cerrado: ni uno más** de los que declara la obra; en saga larga el elenco se
  paga en páginas.
- **BISAGRA (función dura con herida declarada).** Categoría nueva que exige el
  género: un secundario cuya función depende de una herida propia que la lectora
  intuye sin que se desarrolle en arco. Casos: […]. Ni se promocionan a
  protagonistas ni se abaratan a atrezo.

REGLA: máximo de físicas completas vivas en un volumen, **tres** —protagonista A,
protagonista B y el antagonista de ese libro—. Una cuarta satura la extensión del
volumen y roba páginas a la cuota de relación.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Tipos de personaje.
> *Qué declara aquí la obra:* quiénes son protagonista A y protagonista B, en cuántas capas se reparte el transversal, si lo tiene, cuántos forman el elenco fijo, qué personajes son bisagra y qué extensión y cuota de relación protege el máximo de tres fichas.

---

## TIPOS DE ANTAGONISMO

Cinco tipos según la fuerza antagónica: cada uno con mecánica propia de presión
y relación distinta con el arco. Esta saga usa **[…] de los cinco a la vez**, en
capas, y esa superposición es su arquitectura.

| Tipo | Ficha que exige | Mecánica de presión | Uso canónico en la saga |
|---|---|---|---|
| **INDIVIDUAL** | Plantilla B completa | Decisión consciente: lee al protagonista, anticipa, contrarresta. Cada escena registra un movimiento suyo | El antagonista de cada volumen (*Variante: dark romance policial:* el villano de la semana); […] |
| **COLECTIVO** | Ficha de grupo: cohesión, modo de decisión, gradiente de hostilidad, evolución | Emerge de la dinámica, no del acto individual | […] |
| **INTERNO** | Ninguna adicional: vive en HERIDA y MECANISMO de la Plantilla A | Acumulación de coste hasta la crisis, por las cuatro fases del ARCO DE DEFENSA | **Dominante y permanente:** […] |
| **CIRCUNSTANCIAL** | PROTOCOLO DE LA CIRCUNSTANCIA: qué impone, qué recursos activa, trayectoria, umbral letal | La circunstancia no negocia; el protagonista solo responde | **Motor permanente de la pareja:** curas en […] (*care taking*), encierro o proximidad forzada en […] (*forced proximity*): la circunstancia los pone juntos. Escenario del interno, nunca su sustituto |
| **SOCIEDAD** | REGISTRO DE MECANISMOS DE PRESIÓN (ver abajo) | Condicionamiento estructural: las opciones están reducidas antes de elegir | […] |

Los otros cuatro tipos son escenarios donde se manifiesta el interno.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Tipos de antagonismo.
> *Qué declara aquí la obra:* cuántos tipos de antagonismo superpone la saga y quién o qué encarna cada uno.

**REGISTRO DE MECANISMOS DE PRESIÓN.** Tres campos por entrada: qué
condicionante opera, cómo se manifiesta sobre el protagonista, quién lo encarna
en escena. Vinculante:

| Mecanismo | Cómo se manifiesta | Quién lo encarna |
|---|---|---|
| […] | […] | […] |

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Registro de mecanismos de presión.
> *Qué declara aquí la obra:* qué condicionantes estructurales presionan a la pareja, cómo se manifiestan sobre ella y quién los encarna en escena.

**EL CASO HÍBRIDO** (si la saga lo tiene). […] *Un antagonista con cuerpo que
opera como sociedad: cómo actúa, durante qué libros y qué herramienta de la
pareja deja inútil.*

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Caso híbrido.
> *Qué declara aquí la obra:* si la saga tiene un antagonista con cuerpo que opera como sociedad, durante qué libros, y qué obliga a resolver con la cabeza y no con la violencia.

### COMPATIBILIDAD ENTRE TIPOS — DECLARACIÓN CANÓNICA

Combinación fijada para toda la saga, no negociable por libro: **dominante,
interno** (el obstáculo real vive dentro de protagonista A y dentro de
protagonista B; la lectora viene por eso) · **secundario permanente, […]** ·
**secundario rotativo, individual** (el antagonista del libro, con cara y ficha,
para que la trama del libro tenga rostro dentro del volumen; *Variante: dark
romance policial:* el villano de la semana, alguien a quien atrapar) ·
**terciario por arco, […]**.

Lo que esta combinación **prohíbe**: que el antagonista del libro sea el
antagonista dominante. Se comprueba **al cerrar cada capítulo** (TEST 13), con
la unidad de `PAREJA_PRIMERO.md` §2: la parte del capítulo que solo mueve la
trama del libro, aunque estén los dos en escena, si nada pasa entre ellos,
cuenta como trama B en el peso de pareja, que se mide en palabras, y un bloque
que así baja del suelo es género secundario. *Variante: dark romance policial:*
lo que manda entonces es "quién lo hizo", y se ha escrito novela negra.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Compatibilidad entre tipos.
> *Qué declara aquí la obra:* qué tipos ocupan el puesto secundario permanente y el terciario por arco.

### COORDINACIÓN CON GENRE_CONVENTIONS.md Y THEMATIC_ENGINE.md

La convención del Romance es antagonismo interno dominante; la del género
secundario, individual o colectivo (*Variante: dark romance policial:* la de la
novela negra). Esta saga **no transgrede**: adopta la del Romance y le enchufa el
aparato del género secundario como escenario. Si el tipo dominante se desplaza al
individual, se corrige aquí, no allí.

El interno concentra la pregunta moral en dos cuerpos y exige polaridad
interior: ambos protagonistas contienen las dos respuestas, no una cada uno. El
de sociedad obliga a que la pregunta **no se resuelva empíricamente**: el
sistema no se derrota, se sobrevive. Por eso no hay absolución al cerrar el
volumen y la coda va envenenada por diseño.

---

## PLANTILLA A — PROTAGONISTAS (fichas cerradas)

La maquinaria —deseo superficial, deseo profundo, herida anclada en fábula,
mecanismo, coste, arco de defensa en cuatro fases— se aplica de una vez y para
siempre a los dos protagonistas (con parejas rotativas, a la pareja de cada libro). Toda herida declarada tiene evento registrado
en NARRATIVE_CHRONOLOGY, capa pre-narrativa: sin evento concreto, la herida
flota.

### FICHA A1 — PROTAGONISTA A (cerrada)

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Ficha A1 — protagonista A.
> *Qué declara aquí la obra:* la ficha completa y cerrada de protagonista A, campo por campo, con sus cifras vinculantes y el libro de cada fase.

**Datos duros.** […] *Edad al inicio del libro 1, oficio y antigüedad,
formación, entrenamiento físico, secretos, referencia visual.*

**Física visible (vinculante).** […] *Rasgos, lo que la delata cuando la tensión
la sobrepasa, complexión frente a apariencia, manos, estilo.*

**DESEO SUPERFICIAL.** […] Visible desde fuera, con objeto distinto en cada
libro.

**DESEO PROFUNDO.** […] No puede nombrarlo. Lo que dice en voz alta es […].

**HERIDA (anclada en fábula).** […] *Evento concreto con sus cifras canónicas,
registrado en NARRATIVE_CHRONOLOGY.*

**MECANISMO DE DEFENSA — "[…]".** […] *Cómo opera, en qué terreno es impecable y
en cuál se le desajusta la brújula, qué lo dispara.*

**Los tres planos obligatorios (regla dura).** El defecto **no puede activarse
solo con protagonista B**: si solo se activa con uno, no es un patrón
psicológico. Se manifiesta en tres, y **los planos 1 y 2 entran como eco**: dentro
de una escena de pareja (a menudo, interrumpiéndola), en lo que él ve de ella en
directo o en lo que ella le calla. No tienen capítulos propios sin el otro
(`PAREJA_PRIMERO.md` §3, suelo de presencia).

1. **Plano 1 — […].** *Fuera de la pareja y con menos en juego.*
2. **Plano 2 — […].** *Otro terreno, también con menos en juego.*
3. **Plano 3 — PROTAGONISTA B.** La versión sin diluir. Funciona porque la
   lectora ya ha visto asomar el patrón en los otros dos planos, con menos en
   juego.

**Variante: dark romance policial.** **Prohibición asociada (regla dura). El
defecto de protagonista A no se activa con los sospechosos semanales.** Con ellos
opera en modo táctico: seducción fría y calculada, acercamiento puramente
psicológico, cero roce innecesario y ni un gramo de deseo real. Un villano que
despierte su defecto rompe el contrato con la lectora —infidelidad emocional— y
hunde el libro.

**COSTE DEL MECANISMO.** […] *Qué capa de la persona que juró ser le cuesta
cada activación, en qué libro, y qué papel lo demuestra.*

**ARCO DE DEFENSA (vinculante; distribución multivolumen en saga con la misma
pareja; con parejas rotativas, las cuatro fases caben en el libro de la pareja).**
- **FASE 1 — Libros […].** Mecanismo vigente, costes invisibles para ella. Cree
  que puede controlarlo. […]
- **FASE 2 — Libros […].** Los costes son visibles para la lectora y para […];
  ella todavía no. […]
- **FASE 3 — Crisis, libro […].** […] y pierde la herramienta con la que evitaba
  mirarse.
- **FASE 4 — Libros […].** Primera acción desde el deseo profundo, […]. Puede
  salir bien o mal; lo importante es que ya no es defensiva. […]

**ESCENAS DE PRUEBA.** Si al llegar a ellas protagonista A opera idéntica al
inicio, el arco está estancado: […] *Escenas numeradas, cada una con su libro.*

**Refugio y paleta (si la obra los tiene).** […] *Qué hace para pensar, en qué espacio y con qué techo
de escenas por libro (techo, no cuota: el refugio no pide escenas propias, entra en las de pareja o
bajo la mirada de él); paleta por sentidos: olfato; tacto; sonido; color.*

### FICHA A2 — PROTAGONISTA B (cerrada)

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Ficha A2 — protagonista B.
> *Qué declara aquí la obra:* la ficha completa y cerrada de protagonista B, campo por campo, con sus cifras vinculantes y el libro de cada peldaño.

**Datos duros.** […] *Edad y diferencia con protagonista A, de dónde viene y cómo
salió, oficio actual, código, nombre por el que se le conoce.*

**Física visible (vinculante).** […] **Si la obra declara un contraste de
envergadura con protagonista A**, es contraste de poder: parece que podría
destruirla, y ella es la única que lo pone de rodillas. […]

**Las marcas (si la obra se las da).** […] *Marcas del cuerpo que cargan su
herida, y qué hacen con el defecto de protagonista A.*

> **El momento que esas marcas compran, y que es canon:** […]

Si las tiene, son punto de contacto físico y emocional de la pareja, nunca
descripción inerte (TEST 12).

**DESEO SUPERFICIAL.** […]

**DESEO PROFUNDO.** […] No puede nombrarlo; si es narrador hermético, su economía
del lenguaje le impide intentarlo: por eso se mide en actos, no en frases.

**HERIDA (anclada en fábula).** […] *Evento concreto con sus cifras canónicas,
registrado en NARRATIVE_CHRONOLOGY.*

**MECANISMO DE DEFENSA.** […] *Cómo opera y en qué se convierte cuando
protagonista A entra en su radar.*

**COSTE DEL MECANISMO.** […] *Qué le cuesta cada acto del mecanismo, fuera y en
lo íntimo.*

**ARCO DE DEFENSA = ESCALA DE RENDICIÓN (vinculante; multivolumen en saga con la
misma pareja, dentro del libro con parejas rotativas).** En esta saga el sexo no
es la moneda escasa: la rendición de él sí. Cada peldaño se paga una sola vez y no
se repite. La escala raciona la confesión (lo que él dice y entrega de sí), no el
contacto: el deseo, el contacto y el sexo tienen su suelo en cada libro
(`PAREJA_PRIMERO.md` §4).
- **FASE 1 — Libros […].** El mecanismo funciona a la perfección. […]
- **FASE 2 — Libros […].** Costes visibles: […].
- **FASE 3 — Crisis, libro […].** […] Colapso.
- **FASE 4 — Libros […].** Actúa por primera vez sin su mecanismo: […].

Un libro en el que protagonista B entrega algo fuera de escala le ha robado
material a otro volumen (con parejas rotativas, a otro tramo del libro).
Autoridad de trazado: ROMANCE_BEAT_MAP.

**Paleta (si la obra la tiene).** […] *Olfato; tacto; sonido; color.*

---

## REGLAS DURAS DE ESCRITURA DEL CANON

Cinco reglas que no dependen del libro ni del beat. Se auditan en PASADA 2 de
REVISION_PROTOCOL.

**R1 — LA SEÑAL CORPORAL DE PROTAGONISTA A MARCA SIEMPRE VULNERABILIDAD (si la obra la declara).**
En el trabajo y en su refugio, si lo tiene, su estado es el de control: […]. **Cuando la señal
aparece, la escena está declarando que está expuesta.** No se usa gratis ni como
bordado descriptivo. Si en revisión aparece en una escena donde ella tiene el
control, se retira la señal o se reescribe la escena.

**R2 — LA SEÑAL FÍSICA DEL DESEO DE PROTAGONISTA B SE DESCRIBE DESDE EL POV DE ELLA.**
Ningún narrador ve su propia cara ni su propia mirada: eso es oficio y vale
siempre. Si la obra declara una señal física de protagonista B que delata su
deseo —en la mirada, en la voz, en las manos—, se describe desde el POV de A; él
no la ve ni la nombra. Él tiene capítulos —son la droga de la saga—, pero en ellos
esa señal no existe: se le nota en lo que hace, en lo que deja de hacer y en lo
que ve protagonista A cuando le toca. Si es narrador hermético, autodescribir el
deseo desde dentro de protagonista B = personaje blandido.

**R3 — ASIMETRÍA VERBAL (si la obra la declara).**
Ella […] *su idiolecto y lo que tapa con él*. Él […] *el suyo*. Si la obra
declara a protagonista B narrador hermético, **lo que dice ella rebota contra él,
y cuando él por fin habla tiene el doble de impacto.** Esa asimetría es el motor
de todos sus diálogos, no un adorno: si protagonista B iguala el volumen de
palabras de protagonista A, la escena está rota. Prohibido que explique lo que
siente: eso se paga en la escala de rendición.

**R4 — LA FALSA FRAGILIDAD SE USA, NO SE COMENTA (si la obra la declara).**
Si la obra declara que a protagonista A la subestiman, eso es una ventaja
operativa suya, y el texto **no la defiende**: ninguna narración aclara que es
más fuerte de lo que parece. Lo demuestra la acción —el cuerpo a cuerpo, si la
obra lo tiene, con la cuota de escenas de combate con carga sexual por libro que
declare—, no el narrador. Si la obra declara un contraste de envergadura con
protagonista B, se juega en bloqueo, altura de la mirada y espacio ocupado,
nunca en adjetivos.

**R5 — LA MEZCLA DE LAS DOS PALETAS, RACIONADA POR LIBRO (si la obra las tiene).**
Si la obra declara una paleta por narrador, mezclar las dos en un mismo párrafo
señala que la tensión va a estallar. Es una bala de calibre grande y solo hay […]
por volumen. Recuento: SENSORY_HIERARCHY.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Reglas duras del canon.
> *Qué declara aquí la obra:* cuáles de estas reglas tiene y con qué valores: la señal corporal de protagonista A y su estado de control; la señal física que delata el deseo de B; la asimetría verbal, con el idiolecto de cada uno; si a A la subestiman, su cuota de combate con carga sexual por libro y el contraste de envergadura, si lo hay; y cuántas mezclas de paletas caben en un volumen, si tiene paletas.

---

## PLANTILLA B — ANTAGONISTA (física especular)

NOMBRE: […] · LIBRO: […]

El antagonista no es el opuesto moral: es **otra respuesta a la misma pregunta
central** (THEMATIC_ENGINE). El que no comparte pregunta es obstáculo, no
antagonista.

- **PREGUNTA COMPARTIDA.** Deriva del **tema emocional de la relación** de ese
  volumen: la trama del libro es su versión monstruosa, nunca al revés
  (*Variante: dark romance policial:* el caso). […]
- **RESPUESTA QUE ENCARNA.** Defendible: si la lectora la descarta sin esfuerzo,
  no hay tensión. Motivo comprensible sin justificar. […]
- **HERIDA ANÁLOGA.** Misma familia que la de protagonista A o la de
  protagonista B, procesada al revés. Anclar en NARRATIVE_CHRONOLOGY. […]
- **MECANISMO OPUESTO.** Oposición estructural: el mecanismo de protagonista A o
  el de protagonista B, invertido. […]
- **QUÉ SABE DE ELLOS.** Los ve mejor que ellos mismos. Cruzar con
  INFORMATION_CHOREOGRAPHY: la asimetría tiene cadencia propia. […]
- **COSTE PROPIO.** Que la lectora lo intuya aunque el libro no lo resuelva. […]
- **VIOLENCIA.** Mostrada: tortura, ejecución, cuerpos. Se elide por ritmo o por
  subtexto, nunca por decoro. Autoridad: ELLIPSIS_PROTOCOL.

**REGLA DE VARIACIÓN OBLIGATORIA.** La franja del villano rota entre libros
consecutivos: […]. Dos volúmenes seguidos con la misma franja abaratan la serie.

**PROHIBICIÓN DURA.** El antagonista del libro **no asciende nunca a interés
romántico real**. *Variante: dark romance policial:* el villano de la semana es
atrezo táctico y catalizador de celos: protagonista A lo trabaja en frío,
protagonista B lo ve y pierde la cabeza. El efecto se obtiene sin que ella cruce
la línea.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Plantilla B — antagonista.
> *Qué declara aquí la obra:* los mecanismos de la pareja que el antagonista invierte, las franjas entre las que rota el antagonista del libro y, si protagonista B lo vigila, por qué medio lo ve.

### ANTAGONISTA TRANSVERSAL — por capas (canon cerrado)

| Capa | Libros | Quién | Tipo de antagonismo | Qué obliga |
|---|---|---|---|---|
| […] | […] | […] | […] | […] |

Si quien lo encarna tiene cuerpo oculto: ficha B completa desde el libro en que
se revela; antes, presencia sin cara.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Antagonista transversal.
> *Qué declara aquí la obra:* cuántas capas tiene el antagonista transversal, con sus libros, quién o qué es cada una, su tipo y lo que obliga, y la ficha de quien lo encarna.

---

## PLANTILLA C — SECUNDARIOS (función + voz). ELENCO FIJO CERRADO

Un secundario tiene **función dura** —algo que ningún otro puede hacer—,
relación con la pregunta central e **idiolecto** (muletilla, sintaxis, léxico).
**No se les da arco:** un secundario con arco compite con la pareja.

| Personaje | Edad | Función dura | Qué ilumina de la pregunta | La bomba |
|---|---|---|---|---|
| […] | […] | […] | […] | […] |

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Elenco fijo.
> *Qué declara aquí la obra:* quiénes forman el elenco fijo, con su edad, su función dura, lo que ilumina de la pregunta central y su bomba.

**Variante: dark romance policial, si la obra tiene un investigador que cerca a la
pareja** (por ejemplo, de Asuntos Internos; si no lo tiene, no se inventa:
ningún recurso es obligatorio, `PLANTILLA_PRESET.md`, reglas). **REGLA DE ORO:
ESE INVESTIGADOR TIENE RAZÓN.** Ni burócrata mezquino ni corrupto ni obstáculo
administrativo: **es un buen policía persiguiendo a una delincuente real**, y esa
delincuente es la protagonista. Es la conciencia de la lectora encarnada y el
único hombre que desarma a protagonista A **intelectualmente**, lo que pone a
protagonista B igual de nervioso que un rival. **Nunca es interés romántico: eso
lo abarataría** y rompería la prohibición de infidelidad emocional. Escribirlo
torpe, ridículo o venal destruye la arquitectura moral de la saga.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Regla de oro de Asuntos Internos.
> *Qué declara aquí la obra:* si tiene un investigador que cerca a la pareja, qué miembro del elenco fijo es.

### PERSONAJES-BISAGRA

- **[…]** ([edad]). […] *Quién es y qué herida propia intuye la lectora,
  apariciones por libro y en qué momento, función dura y estado, sin arco.*
- **[…]** ([edad]). […] *Si además es antagonista (Plantilla B): cómo opera como
  función hasta que se revela y desde qué libro tiene ficha completa.*

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Personajes-bisagra.
> *Qué declara aquí la obra:* quiénes son los personajes-bisagra, con su edad, su frecuencia de aparición, su función dura y su estado.

---

## REGISTRO DE COSTE ACUMULADO

[Se actualiza en CONTINUITY_PHYSICS.md por cada personaje con física completa.]

FORMATO — PERSONAJE: [nombre] · LIBRO: [n] · CAPÍTULO X: [qué coste pagó, qué
se perdió, qué documento existe ahora].

El coste acumulado es el vector real del arco: sin registro, un personaje puede
perder tres cosas en cinco capítulos y seguir igual. El registro lleva siempre una
**columna de pareja**: qué se han entregado los dos en este volumen (el peldaño de
la escala de rendición, la confesión, lo que ya no pueden deshacer). Un libro que
no la mueve no se entrega. En saga larga con la misma pareja el registro es además
**de serie**, con dos columnas más por volumen: la **pieza que suma […]**, si la
obra tiene esa amenaza, y la **miga de pan tangible sobre la trama horizontal**. Un
libro que no mueve ninguna de las dos tampoco se entrega.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Registro de coste acumulado.
> *Qué declara aquí la obra:* qué amenaza acumulativa suma una pieza en cada volumen, si la tiene, y sobre qué misterio de la trama horizontal cae la miga de pan; la columna de pareja sale de su escala de rendición (ROMANCE_BEAT_MAP).

---

## INSTRUCCIÓN OPERATIVA

En cada escena, un personaje con física completa actúa **desde su mecanismo de
defensa**, no desde su deseo profundo.

EXCEPCIÓN (SYSTEM_ORCHESTRATION, precedencia contextual): tras la crisis
(FASE 3 → FASE 4) puede actuar desde el deseo profundo. Antes de la crisis es
ruptura de personaje: **protagonista B entregando en un libro lo que le toca
entregar en otro posterior no es un regalo a la lectora, es un robo a ese otro
libro** (saga con la misma pareja; con parejas rotativas, el robo es a otro tramo
del libro).

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Instrucción operativa.
> *Qué declara aquí la obra:* el verbo que resume el mecanismo de cada protagonista y el ejemplo canónico de peldaño entregado antes de tiempo.

Un personaje que ha perdido su mecanismo puede volverse inesperadamente directo,
vulnerable o cruel. Ahí CHARACTER_PHYSICS tiene precedencia sobre
SEMANTIC_OMISSION, SUBTEXT_MECHANICS y PROSE_LINE_DISCIPLINE: lo que sería
exceso puede ser el síntoma preciso del colapso defensivo. Las cuotas se relajan
en esa escena concreta como caracterización, no como permiso para prosa floja.

---

## SÍNTOMAS VERBALES DEL COLAPSO

Sección bidireccional con PROSE_LINE_DISCIPLINE, sección REGLA DE EXCEPCIÓN POR
ESTADO DE PERSONAJE.

En FASE 3, la voz directa o el indirecto libre pueden manifestar síntomas que en
prosa neutra serían tics corregibles: adjetivos en cascada, mitigación adverbial
constante, ternarios obsesivos, frases-resumen que glosan lo que el personaje no
acaba de aceptar. **El colapso no suena igual en los dos protagonistas, y
confundirlos es el error más caro del modelo.** Cada uno colapsa desde su
idiolecto; si la obra declara la asimetría verbal de R3, en direcciones
contrarias:

- **PROTAGONISTA A colapsa hacia arriba.** Su idiolecto se descontrola: habla más
  rápido, más larga, y lo que tapaba con él deja de taparse. Aquí sí aplican los
  síntomas clásicos.
- **PROTAGONISTA B colapsa hacia abajo, y una sola frase de más ya es el
  colapso.** Su economía es tan cerrada que la excepción se mide en unidades
  mínimas: una frase larga donde siempre hubo tres palabras, una primera persona
  del plural, algo que nunca nombra dicho en voz alta. **Un párrafo explicativo
  en boca de protagonista B no es colapso: es un fallo de escritura.** Y está
  tasado: solo cabe en los peldaños de la escala de rendición o en el libro de la
  crisis.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Síntomas verbales del colapso.
> *Qué declara aquí la obra:* con qué rasgos de idiolecto colapsa cada protagonista, qué nombra B en voz alta solo al colapsar, si lo tiene, y en qué libro cae la crisis.

### TEST DE TRES PREGUNTAS

Antes de mantener una violación de cuotas en escena de presunto colapso:
¿coincide con un punto de crisis declarado aquí —fase del arco, peldaño de la
escala de rendición, libro de la crisis—? ¿Tiene marcas del idiolecto declarado
en VOICE_ARCHITECTURE o en su ficha? ¿Una lectora atenta lo lee como
descomposición del personaje y no como prosa floja de quien escribe? Tres síes:
se mantiene. Un no: es aplicación robótica justificada a posteriori y se corrige.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Test de tres preguntas.
> *Qué declara aquí la obra:* el libro de la crisis y la marca de idiolecto que identifica a cada protagonista.

### RANGO DE LA EXCEPCIÓN

Opera **por escena**, no por capítulo ni por bloque. En cuanto el personaje
vuelve al mecanismo o adopta su primer movimiento de FASE 4, la prosa regresa a
las cuotas estándar. Una excepción que se prolonga se vuelve rasgo permanente y
debe declararse en VOICE_ARCHITECTURE como idiolecto. En protagonista B, una
excepción sostenida equivale a haberlo blanqueado.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Rango de la excepción.
> *Qué declara aquí la obra:* el nombre del protagonista hermético al que se aplica la última frase.

---

## TESTS DE FUNCIONAMIENTO

**TEST 1 — EL DEFECTO EN SUS TRES PLANOS.** ¿El patrón de protagonista A asoma en
los planos 1 y 2, como eco dentro de las escenas de pareja o bajo la mirada de él,
y llega sin diluir con protagonista B? Sin eco de los otros dos planos, el defecto
no es un patrón; con capítulos propios de los planos 1 y 2 sin el otro, se han
comido páginas de la pareja.

**TEST 2 — CONTAMINACIÓN CON EL ANTAGONISTA DEL LIBRO.** Con el antagonista del
libro (*Variante: dark romance policial:* el villano de la semana, el sospechoso),
¿protagonista A siente algo real, se enternece o se le activa el defecto? Si sí,
se ha roto la prohibición y con ella el contrato con la lectora.

**TEST 3 — ASIMETRÍA VERBAL** (si la obra la declara, R3). Contar palabras por
réplica en cada escena de pareja: ¿lo que dice protagonista A rebota contra la
economía de protagonista B, o él habla de más? Más explicaciones de sentimientos
que las pactadas en la escala: revertir.

**TEST 4 — LA SEÑAL CORPORAL** (si la obra la declara). Cada aparición de la
señal corporal de protagonista A, ¿marca vulnerabilidad? Si alguna es
decorativa, se retira o se reescribe.

**TEST 5 — LA SEÑAL DEL DESEO DE B.** ¿Algún capítulo de protagonista B describe
su propia cara o su propia mirada, o la señal física que la obra le declara para
el deseo, si la tiene? Reescribir desde el POV de ella. Si es narrador hermético,
¿glosa su deseo desde dentro? También se reescribe.

**TEST 6 — COSTE LEGIBLE.** Cada 3–5 capítulos: ¿qué ha perdido cada uno y qué
papel lo demuestra? "Nada concreto" = mecanismo en vacío.

**TEST 7 — DISTANCIA DESEO-DEFENSA.** ¿Están separados el deseo superficial y
el profundo? Si coinciden, no hay arco; si son infinitamente distantes, hay
abstracción.

**TEST 8 — FASE CORRECTA.** ¿La fase declarada para este libro coincide con lo
que hacen? Un peldaño fuera de escala, o protagonista A actuando desde el deseo
profundo antes del libro de la crisis, es ruptura.

**TEST 9 — ANCLAJE DE HERIDA.** ¿Cada herida invocada tiene evento en
NARRATIVE_CHRONOLOGY con sus cifras canónicas, las de su ficha?

**TEST 10 — EL INVESTIGADOR DE ASUNTOS INTERNOS.** **Variante: dark romance
policial.** ¿Tiene razón en este libro, escrito competente, íntegro y sin
resquicio romántico? Un investigador ridiculizado es una protagonista sin
adversario moral.

**TEST 11 — ECONOMÍA DE FICHAS.** ¿Más de tres físicas completas vivas? ¿Algún
secundario del elenco fijo ha empezado a desarrollar arco?

**TEST 12 — MARCAS Y PALETA** (si la obra las tiene). ¿Las marcas de
protagonista B funcionan como punto de contacto y no como descripción inerte?
¿La mezcla de las dos paletas se queda en los usos declarados?

**TEST 13 — NOSOTROS DOS.** Al cerrar cada capítulo (acta, C-10), con la unidad
de `PAREJA_PRIMERO.md` §2: ¿qué parte del capítulo es de pareja? Los dos en
escena y algo pasa entre ellos (choque, deseo, miedo, control, lo que se
callan); si están juntos y esa parte solo mueve la trama B, cuenta como trama B
en el peso de pareja, que se mide en palabras.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Tests de funcionamiento.
> *Qué declara aquí la obra:* los tests con los nombres, los planos y las cifras de cada herida y, si los tiene, la señal corporal, la señal del deseo de B, las marcas y el contador de mezclas de la saga.

---

## CRUCES POV × EJES DEL ARCO DE MUNDO

Sección activa si WORLD_ARC está activo (su adenda lo deja inactivo por defecto;
activarlo es decisión del autor). La tabla operativa vive en WORLD_ARC; su
alimentación nace aquí. HERIDA y MECANISMO
determinan qué ejes agravan la física de cada POV; los DESEOS, qué ejes son
materia de su trayectoria; el COSTE, qué ejes producen daño. **Códigos:**
PRINCIPAL (atraviesa su columna vertebral) · SECUNDARIO ·
ESTRUCTURAL-SUBTERRÁNEO (opera bajo su conciencia) · INSTRUMENTAL · MARGINAL ·
AUSENTE.

| Eje de mundo | PROTAGONISTA A | PROTAGONISTA B |
|---|---|---|
| […] | […] | […] |

**FUNCIÓN REVELADORA.** Cada cruce declara qué revela el eje que el arco
personal no revelaría solo. […] Cruce que no revela nada: decorativo, baja de
intensidad.

**ASIMETRÍA TEMPORAL.** Si el paso de FASE 2 a FASE 3 coincide en ambos con el
pico de un eje de mundo, es por concurrencia de coste acumulado y presión
sistémica: es diseño, no casualidad. Los cruces deben ser compatibles con la
posición del libro en los arcos de la saga y con sus puertas de salida limpias
(saga con la misma pareja). Autoridad: SERIES_GLUE.

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Cruces POV × ejes del arco de mundo.
> *Qué declara aquí la obra:* si WORLD_ARC está activo, los ejes de mundo y su intensidad para cada protagonista por tramos de libros, el cruce revelador canónico, el libro en que la crisis coincide con el pico de un eje y, si los tiene, los arcos de la saga y sus puertas de salida.

---

## RELACIÓN CON OTROS ARCHIVOS

**ALIMENTA:** RELATIONSHIP_PHYSICS (la relación de la pareja es función de dos
físicas en colisión) · ROMANCE_BEAT_MAP (la escala de rendición es el arco de
defensa de protagonista B: aquí se declara, allí se traza por libro) ·
VOICE_ARCHITECTURE (el punto ciego de cada narrador deriva de su herida) ·
STORY_SPINE (los dos arcos, dentro del peso de pareja: `PAREJA_PRIMERO.md` §2) ·
SCENE_NECESSITY (toda escena modifica el estado de al menos uno) ·
NARRATIVE_CHRONOLOGY (heridas como eventos de fábula con cifras vinculantes) ·
CLUE_LEDGER (la miga de pan sobre la trama horizontal es coste, no solo
información) · SENSORY_HIERARCHY (las dos paletas y la regla de su mezcla, si
la obra las tiene) ·
WORLD_ARC (justificación física de cada intensidad de cruce) ·
PROSE_LINE_DISCIPLINE (autoridad bidireccional sobre el colapso: aquí se declara
la FASE 3 y se autoriza la excepción, allí se cuantifica).

**SE SUBORDINA A:** SERIES_GLUE (en saga con la misma pareja, el arco de cada
libro es subconjunto del de la saga: ninguna ficha gasta aquí lo pactado para más
adelante) · `PAREJA_PRIMERO.md` (el peso de la pareja frente a la trama del libro).

**NO SE SUBORDINA A** GENRE_CONVENTIONS, que modula la estructura pero no manda
sobre el canon de personajes. Donde choquen, gana esta ficha, salvo en lo que
aquel archivo declara contrato de género irrenunciable: **el peso de la pareja y
sus suelos** (regla 1), la persona, el tiempo y los narradores que declara la obra
(el POV alterno, por defecto: regla 4), explicitud y, en saga con la misma
pareja, ausencia de cierre romántico por libro.

**SE ACTUALIZA EN:** OPERACIÓN C (cada capítulo: coste, el peso de pareja
—TEST 13— y las columnas del registro de coste) · OPERACIÓN D (la de cierre del
libro: el arco progresa y no se gasta un peldaño fuera de escala) · PASADA 2 del
REVISION_PROTOCOL (arcos, reglas R1–R5, tests 1–13).

> **Valores de la obra →** `PRESET_<OBRA>.md` › CHARACTER_PHYSICS › Relación con otros archivos.
> *Qué declara aquí la obra:* los mecanismos que chocan en la pareja, el peso de pareja, la extensión de la saga y, si las tiene, las columnas de serie que se actualizan en cada capítulo.
