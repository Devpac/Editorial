<!-- Fábrica v3.0 — plantilla de GÉNERO (vale para cualquier saga de dark romance). Los valores de la obra viven en su preset: PRESET_<OBRA>.md (la obra activa la dice el LEEME). -->

# GENRE_CONVENTIONS.md — Fábrica v3.0

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

> **ARCHIVO NÚCLEO.** Declara el régimen de género de las novelas de la saga y
> gobierna, desde él, a STORY_SPINE, ROMANCE_BEAT_MAP, TENSION_MECHANICS, CLUE_LEDGER,
> CHAPTER_BRIEF, HEAT_DISCIPLINE, SEAMS_AND_HINGES y SERIES_GLUE. Sin esta declaración,
> esos archivos derivan por defecto hacia el **género secundario con romance encima**
> (*Variante: dark romance policial:* la **novela negra con romance encima**),
> que es exactamente el producto que hunde el proyecto.

## PROPÓSITO

Fijar por escrito, y de una vez, qué se está escribiendo. La saga vive en la intersección
de dos mercados que casi nunca se tocan y la tentación permanente —capítulo a capítulo— es
deslizarse hacia el que se escribe con más facilidad: el del género secundario
(*Variante: dark romance policial:* el procedimiento policial). Este archivo existe para
hacer ese deslizamiento visible y corregible.

JERARQUÍA: Capa 1, paralela a AESTHETIC_REGISTER. Modula la estructura; no manda sobre
THEMATIC_ENGINE ni sobre CHARACTER_PHYSICS, pero fija el contrato de lectura que ningún
archivo inferior puede contradecir. En el peso de la pareja frente a la trama del libro manda
`PAREJA_PRIMERO.md`, por encima de este archivo y de cualquier plantilla.

REGLA FUNDACIONAL heredada: género y estética son dimensiones distintas. El género aquí es
**Dark Romance con la ambientación del subgénero que declara la obra**; la estética (la
voz de cada narrador, su firma sensorial, la persona y el tiempo) vive en
AESTHETIC_REGISTER.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Régimen de la saga.
> *Qué declara aquí la obra:* cuántas novelas forman la saga, con qué ambientación se declara su dark romance y qué voz y qué firma sensorial tiene su estética.

---

## DECLARACIÓN PRIMARIA (fijada, inmutable)

- **GÉNERO PRIMARIO:** **Dark Romance.** La relación entre la protagonista A y el
  protagonista B (por defecto, ella y él; si uno es hermético, cuál, lo declara la obra) es el producto. Todo lo demás es ambientación,
  motor o excusa.
- **GÉNERO SECUNDARIO:** el subgénero que declara cada obra. Aporta la trama de cada
  libro, que es la **trama B** (`PAREJA_PRIMERO.md` §1: el escenario, el obstáculo, la
  excusa para que choquen y la causa de la proximidad forzada), la credibilidad de mundo y
  el motor de escenarios. Las reglas marcadas
  «Variante: dark romance policial» rigen solo cuando la obra declara ese subgénero.
  **Otro subgénero escribe su variante:** la biblia (fase 1, `PLANTILLA_BIBLIA.md` §2)
  recorre, regla por regla, las que llevan marca de variante y
  dice qué es en su subgénero la trama del libro, la escena limpia, el antagonista del
  libro, la impunidad, la anti-firma…; el preset la copia
  (`PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Variante del subgénero). Una regla con marca
  policial que no tenga equivalente se declara «no aplica»; ninguna se aplica a otro
  subgénero por inercia.
  *Variante: dark romance policial:* investigación criminal / procedimental.
  Aporta el caso autoconclusivo (la trama B), la credibilidad de mundo y el motor
  inagotable de escenarios.
- **FIDELIDAD AL GÉNERO:** estricta en las convenciones de Dark Romance (posesión,
  toxicidad consentida, morally grey, POV del obseso, explicitud); deliberadamente
  **infiel** al género secundario (*Variante: dark romance policial:* al procedimiento
  policial), que se sacrifica sin nostalgia cada vez que compite con la relación.
- **LECTORA ESPERADA:** la que declara la obra (`PRESET_<OBRA>.md` › Cabecera › Mercado y
  lengua). Busca hombre posesivo con código, protagonista
  femenina competente que no sea damisela, tensión sostenida, escenas explícitas y, si la
  obra es una saga, una en la que instalarse. **Tolera mal:** el procedimiento extenso
  (*Variante: dark romance policial*), el héroe blando, la protagonista pasiva, el libro
  que no avanza la trama horizontal (si la saga la tiene) y la contención pudorosa.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Declaración primaria de la obra.
> *Qué declara aquí la obra:* quiénes forman su pareja protagonista y cuál es su subgénero, con lo que aporta a cada libro.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Variante del subgénero.
> *Qué declara aquí la obra:* su subgénero y, si no es el policial, qué es en él cada regla con marca de variante (regla por regla), o «no aplica».

### DECLARACIÓN FUNDACIONAL

> **Esto NO es una novela [del género secundario] con romance. Esto es Dark Romance con
> ambientación [del género secundario].**

Si el libro se vende a las lectoras del género secundario, **odiarán al protagonista
peligroso por lo que hace y al otro por permitírselo.** Es el público equivocado y el error
es irreversible en la tienda: la categoría mal elegida arrastra reseñas de una estrella
durante toda la vida del título.

**Variante: dark romance policial.** *Esto NO es una novela policíaca con romance. Esto es
Dark Romance con ambientación policial.* Las lectoras del género secundario son las de
la novela policíaca (sus autores, los comparables de los que huye la obra).

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Declaración fundacional de la obra.
> *Qué declara aquí la obra:* su frase fundacional y a qué lectoras no hay que venderle el libro.

### REGLA DE ARBITRAJE

| Cuando chocan | Gana |
|---|---|
| Género secundario y relación (*Variante: dark romance policial:* procedimiento policial y relación) | **La relación** |
| Verosimilitud y tensión | **La tensión**, siempre que la verosimilitud se sostenga con una frase |
| Decoro y oscuridad | **La oscuridad** |
| Justicia y deseo | **El deseo.** Nadie sale limpio |
| Cierre satisfactorio de la trama del libro (*Variante: dark romance policial:* del caso) y cliffhanger emocional | **El cliffhanger** |

---

## POSICIONAMIENTO: DARK ROMANCE POLICIAL vs. ROMANTIC SUSPENSE

**Variante: dark romance policial.** La distinción no es académica: decide las palabras
clave, la categoría de la tienda y el tono de cada escena. El Romantic Suspense es el vecino
más peligroso, porque se parece por fuera y es lo contrario por dentro.

| Atributo | Romantic Suspense (lo que NO somos) | **Dark Romance Policial (lo que somos)** |
|---|---|---|
| El peligro | Viene de fuera: el asesino del caso | Viene del asesino, **pero también de la intensidad de él** |
| La moralidad | Los buenos atrapan a los malos | Líneas difusas. Él mata al asesino para protegerla |
| La protección | Él la protege porque la ama y la respeta | **Él la aísla y manipula su entorno porque es "suya"** |
| Reacción de ella | Agradece la ayuda, trabajan en equipo | Lucha contra él, se enfada, **pero la atracción la domina** |
| El sexo | Recompensa del acto tercero | Moneda de cambio recurrente y campo de batalla |
| El final | Justicia restaurada | Justicia negociada. **Nadie sale limpio** |

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Posicionamiento de la obra.
> *Qué declara aquí la obra:* frente a qué vecino de género se posiciona y cómo encarna su pareja cada atributo de la tabla.

---

## LOS CINCO PILARES DEL SUBGÉNERO

1. **La Protagonista Ancla.** Una protagonista joven, atractiva y brillante que genera
   comunidad y fidelidad, pero con una vida afectiva y sexual visceral y magnética.
   *Variante: dark romance policial:* uno de los dos está del lado de la ley; quién, lo
   declara la obra.
2. **Estructura Dual (romance + adrenalina), con jerarquía.** La catarsis y el calor del
   Dark Romance, con la trama B como fuente de peligro y de proximidad
   (*Variante: dark romance policial:* el caso pone a la pareja en peligro y la obliga a
   estar cerca).
3. **El Chico Malo con Código.** Hombres moralmente grises
   (*Variante: dark romance policial:* el que está fuera de la ley o se la salta) que despiertan el deseo
   de la protagonista y desdibujan la línea entre el deber y el instinto.
4. **El Espejo Sensorial** *(si la obra lo declara)*. Una firma sensorial de la pareja
   —la que declara la obra: dos paletas opuestas, un olor, un sonido, un tacto— que
   funciona como sistema de señalización emocional a lo largo de la saga. Autoridad:
   SENSORY_HIERARCHY.
5. **La Toxicidad Consentida.** No basta con que el peligro venga de fuera. **El
   protagonista peligroso (por defecto, él) cruza líneas morales no solo con los malos,
   sino con el otro.** Ese es el núcleo puro del Dark
   Romance y lo que separa la saga del Romantic Suspense.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Pilares en la obra.
> *Qué declara aquí la obra:* su firma sensorial, si la tiene, cuántos libros señaliza, y quién cruza las líneas con quién.

---

## CONVENCIONES OPERATIVAS DEL GÉNERO (el contrato)

1. **La pareja es la trama A** (`PAREJA_PRIMERO.md`, que manda en esto). Relación y trama
   del libro (*Variante: dark romance policial:* relación e investigación) avanzan
   trenzadas, pero **no pesan lo mismo**: la trama del libro es la trama B.
   - **Página de pareja:** los dos en escena y algo pasa entre ellos (choque, deseo, miedo,
     control, lo que se callan); uno con el otro en directo, a distancia (vigilancia en tiempo
     real, una llamada, un mensaje); o el otro ocupando a quien narra (lo desea, lo teme, lo
     busca, lo perfila o se lo calla). Si están juntos y esa parte solo mueve la trama B,
     cuenta como trama B. Un recuerdo de pasada, o una sombra que no ocupa a quien narra, no
     cuenta.
   - **Peso de pareja:** objetivo 80 %, **suelo 70 %**, en palabras, por bloque de cuatro
     capítulos y por libro. Lo que no es pareja (trama B, trama horizontal y elenco cuando su
     página no es de pareja), como mucho el 30 % del libro, sin mínimo. La trama horizontal y
     el elenco no tienen cuota propia: cuentan como pareja si cumplen lo de arriba. Lo estima
     la escaleta y lo miden el acta y la lectura, después del borrador.
   - **Puerta de entrega:** un libro por debajo del suelo no se entrega. Un bloque por
     debajo no se arregla en la prosa: se reescaleta el siguiente y, si la lectura lo pide,
     un capítulo va a reescritura.
   - **Suelos de género** (presencia, primer cara a cara, contacto, beso, primera escena
     explícita, calor, voces, ganchos): `PAREJA_PRIMERO.md` §3. La obra puede subirlos en su
     preset; bajarlos es decisión del autor, con su porqué en la biblia.

   Autoridad de trazado: ROMANCE_BEAT_MAP (la trama A); STORY_SPINE trenza la B sobre ella.
2. **La trama del libro es el espejo del conflicto de pareja**
   (*Variante: dark romance policial:* el crimen es el espejo del conflicto de pareja).
   Cada libro fija primero su tema emocional; **la trama del libro**
   (*Variante: dark romance policial:* el caso) **se elige después** y es su versión
   monstruosa. Nunca al revés.
3. **Apertura con el protagonista peligroso (por defecto, él), no con la trama del libro**
   (*Variante: dark romance policial:* no con el cadáver). La lectora debe verlo —o sentirlo
   observando— antes de entrar en
   la trama del libro (*Variante: dark romance policial:* antes de saber que hay un
   muerto; el cuerpo puede llegar en la página tres). Y el capítulo 1 **contiene la
   promesa de la pareja**: el otro protagonista visto, presente o en tensión con el
   narrador. Abrir con él solo, sin el otro, promete thriller.
4. **Primera persona y POV alterno ella / él, por defecto.** Es la señal de género más
   potente que existe y no cuesta nada: la lectora sabe qué está leyendo en el primer
   párrafo, antes de la sinopsis y antes de la portada. Los capítulos de él dan acceso
   directo a la obsesión desde dentro; la lectora sabe lo que él ha hecho mucho antes que
   ella. La persona, el tiempo (presente o pasado) y si hay uno o dos narradores los fija
   la biblia (🔒, decisión del autor); lo que fije rige siempre. Con dos narradores,
   el reparto entre las voces lo declara la obra (`PRESET_<OBRA>.md` › SYSTEM_ORCHESTRATION ›
   Extensión, persona y narradores).
5. **Prohibición de la escena limpia.** Una escena que solo avanza la trama del libro
   (*Variante: dark romance policial:* una escena de investigación que solo avanza el caso),
   sin ser página de pareja (regla 1; con una sombra que no ocupa a quien narra no basta, y
   con los dos delante tampoco, si nada pasa entre ellos), entra en un cupo: **como mucho una
   de cada cuatro escenas** (`PAREJA_PRIMERO.md` §5). Más de una de cada cuatro rompe el
   contrato: con el cupo lleno, o si cabe en una línea, no es una escena, es un párrafo de
   resumen, o se funde en una escena de pareja.
6. **Gancho en todos los capítulos, por defecto.** Capítulos en el número y la
   horquilla de palabras que declara la obra, cada uno cerrado en gancho, salvo los cierres
   de descarga que declare la obra en › SEAMS_AND_HINGES › Gancho en todos los cierres,
   con su tope. **Al menos dos
   de cada tres ganchos son de pareja**, los más valiosos (`PAREJA_PRIMERO.md` §3, o la
   proporción que declare el preset); los demás pueden ser de la trama B. Autoridad:
   SEAMS_AND_HINGES.
7. **Explicitud plena.** El sexo se muestra en página, con vocabulario directo. No hay
   umbral de puerta ni elipsis por pudor. Autoridad: HEAT_DISCIPLINE.
8. **Violencia mostrada.** Ejecuciones, tortura, cuerpos. La elipsis se usa por ritmo o
   por efecto de subtexto, nunca por decoro. Autoridad: ELLIPSIS_PROTOCOL.
9. **Migas de pan obligatorias** *(si la saga tiene trama horizontal)*. En cada libro,
   la protagonista descubre **una pista real y tangible** sobre la trama horizontal. Un
   libro sin miga no se entrega. Autoridad: CLUE_LEDGER.
10. **Cierre de la trama del libro, no cierre de saga**
    (*Variante: dark romance policial:* cierre de caso). La trama del libro se resuelve
    dentro del volumen. Lo que queda abierto depende de la forma de la saga, que declara
    la obra (SERIES_GLUE, adenda de dark romance): con la misma pareja en muchos libros, la
    relación **no** se cierra y cada libro termina en cliffhanger emocional o en pista
    grande de la trama horizontal; en un dúo, el primer libro deja la relación en vilo y
    el último la cierra; con parejas rotativas, cada pareja cierra su final feliz y lo
    abierto es el mundo y la pareja siguiente.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Convenciones en la obra.
> *Qué declara aquí la obra:* su peso de pareja y sus suelos, si sube alguno (si el autor baja alguno, la decisión de la biblia que lo autoriza), el número y la longitud de sus capítulos, de qué trata su trama horizontal y qué sabe la lectora antes que la protagonista.

---

## LA INVERSIÓN CLAVE

El corpus de referencia de ambientación —el del género secundario— resuelve con su propia
política moral. La saga importa su solvencia y su textura, y **transgrede deliberadamente
su política moral y su gramática narrativa.**

- **Convención del género secundario que se rompe:** [cuál, y cómo la rompe la obra].
- **Razón autoral:** el contrato de Dark Romance promete que la lectora se ponga del lado
  del monstruo. Viene por él, no por la trama del libro.
- **Verosimilitud, no compensación:** [qué se conserva de él]: solo lo que hace
  creíble el mundo. No hay nada que compensar a la lectora del género secundario, que no es
  la del libro (declaración fundacional).
- **Punto donde se hace evidente:** [en qué libro y en qué página, por decisión de
  diseño; y en qué libro se vuelve irreversible].

**Variante: dark romance policial.** El corpus de referencia de ambientación —la novela
negra— resuelve en **restauración de la justicia institucional**: el equipo
funciona, el culpable cae, el sistema encaja las piezas y quien investiga vuelve a casa. La
saga importa su solvencia procedimental y su textura.
- Convención de la novela negra que se rompe: la justicia restaurada y la integridad de
  quien está del lado de la ley (quién es, lo declara la obra).
- Razón autoral: viene por el protagonista peligroso, no por el atestado.
- Verosimilitud: ambientación verificada (la del lugar y la época que declare la obra),
  jerga correcta y una unidad policial creíble, en lo que el caso necesite para sostenerse
  (con una frase: regla de arbitraje).

Esta inversión es paralela y solidaria a la de THEMATIC_ENGINE (pregunta moral sin
absolución en lugar de pregunta resoluble).

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › La inversión clave de la obra.
> *Qué declara aquí la obra:* qué convención del género secundario rompe y cómo, qué conserva de él para que el mundo sea creíble y dónde se hace evidente la inversión (en saga, en qué libro, y en cuál se vuelve irreversible).

---

## LA GESTIÓN DE LOS DOS PELIGROS DEL GÉNERO

### PELIGRO 1 — El flirteo con terceros

A las lectoras de Dark Romance les encantan los celos pero **odian la infidelidad
emocional**. Si la protagonista parece genuinamente atraída por un tercero en cada libro,
pierde la simpatía del público y la saga se cae.

**Convención:**
- Si ella se acerca a un tercero (el antagonista del libro; *Variante: dark romance
  policial:* el villano de la semana o un sospechoso) para sacarle algo, el acercamiento es
  **instrumental**: **ella no siente nada por él** y no hay roce físico innecesario.
- Los celos del otro protagonista se logran sin que ella cruce la línea: él lo sabe, lo ve o
  lo teme (cómo, lo declara la obra).
- Si la obra pone condiciones al defecto de la protagonista (en qué terrenos se activa), no
  se activa con esos terceros.

Si la obra lo tiene, declara la forma de ese acercamiento y por qué medio lo ve o lo sabe él.

### PELIGRO 2 — Incompetencia vs. tropo stalker (si uno de los dos vigila al otro)

Si un protagonista vigila al otro «para protegerlo» y el vigilado es competente en su
terreno (*Variante: dark romance policial:* si es quien investiga), no puede pasar mucho
tiempo sin darse cuenta: parecería incompetente.

**Convención:** el vigilado lo descubre en el momento que declara la obra, y lo *dark* es lo
que hace al descubrirlo: no lo detiene ni huye; **decide**, y la obsesión del otro lo atrae
en vez de espantarlo (consentirlo, volverlo a su favor). La vigilancia es una transgresión no consentida y no sexual
(HEAT_DISCIPLINE, consentimiento). Qué medios usa, cuándo lo descubre y qué hace con ello,
lo declara la obra.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Peligros en la obra.
> *Qué declara aquí la obra:* cómo gestiona los dos peligros: si la protagonista se acerca a terceros, con quién y de qué forma (y con qué oficio o formación, si lo usa) y por qué medio lo ve o lo sabe el otro; si su defecto tiene condiciones, en qué terrenos se activa; y, si uno de los dos vigila al otro, con qué medios, cuándo lo descubre el vigilado y qué hace con ello (en saga, en qué libros), o «no aplica».

---

## PECADOS CAPITALES (lista negra que rompe el contrato)

- *Variante: dark romance policial.* **Abrir el libro con un cadáver o una escena del
  crimen.** Novela negra a la primera página, público perdido en la muestra gratuita.
- *Variante: dark romance policial.* **Escenas de investigación limpias por encima del
  cupo:** más de una de cada cuatro escenas sin página de pareja (regla 5).
- **Capítulo sin el otro:** ni en escena, ni en directo, ni ocupando a quien narra al
  menos un tercio del capítulo; o, desde el primer cara a cara, tres capítulos seguidos sin
  los dos en escena, fuera de una ausencia declarada con tope (`PAREJA_PRIMERO.md` §3;
  ELLIPSIS_PROTOCOL, uso B).
- **Libro por debajo del suelo de pareja** (regla 1).
- Persona, tiempo o POV distintos de los que fija la biblia (por defecto: primera
  persona; ningún POV que no sea el de uno de los protagonistas).
- Capítulo sin gancho de cierre (salvo los cierres de descarga que declare la obra, dentro de su tope).
- Elipsis del acto sexual por pudor. Eufemismo anatómico. Metáfora floral.
- *Saga con la misma pareja (formas A y B, salvo el último libro de la B, que cierra la pareja):* **HEA cerrado por libro** o coda cálida que desactive la
  tensión de saga.
- La protagonista como damisela en apuros, o rescatada de forma que anule su agencia.
- **La protagonista genuinamente atraída por un tercero.** Infidelidad emocional: vetada.
- **El protagonista peligroso redimido, blanqueado o convertido en buen chico.** Vetado en
  cualquier forma de saga: el final feliz no lo blanquea; sigue siendo peligroso, ahora para
  los demás.
- El protagonista hermético, si la obra lo declara, explicando sus sentimientos con
  verborrea. Rompe su economía del lenguaje.
- Describir desde el POV de un narrador lo que solo se ve desde fuera (su mirada, su
  cara, el cambio que el otro nota en él).
- *Variante: dark romance policial.* Procedimiento como espectáculo: autopsia de tres
  páginas, reunión de coordinación, balística detallada, rueda de prensa, jerga sin
  función dramática.
- *Si la saga tiene trama horizontal:* **libro sin miga de pan tangible** sobre ella.
- Deus ex machina institucional: que el sistema resuelva lo que debe resolver la pareja
  (con las herramientas que la obra le da a cada uno).
- El antagonista del libro (*Variante: dark romance policial:* el villano de la semana)
  ascendido a interés romántico real.
- Si la obra reserva un nombre de uno de los dos para un libro posterior: decirlo antes,
  en boca de nadie.
- Si la obra declara recursos racionados (los que declare: por ejemplo, una señal
  sensorial, un gesto reservado, un apodo): usarlos más veces de las que declara, o sin que
  signifiquen lo que la obra les asigna.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Pecados propios de la obra.
> *Qué declara aquí la obra:* qué nombre de un protagonista reserva y hasta qué libro, si reserva alguno; qué recursos racionados tiene, si los tiene, con lo que significa cada uno y su techo por libro.

---

## EXPECTATIVAS ESTRUCTURALES DE LA LECTORA

Capítulos cortos con gancho y ritmo creciente, diseñados para lectura compulsiva;
el otro protagonista en todos los capítulos, contacto con carga antes del 20 % y beso antes
de la mitad (los suelos que lo aseguran: `PAREJA_PRIMERO.md` §3); tensión sexual que no baja
de intensidad aunque la pareja ya se haya consumado; un hombre
hermético (si la obra lo declara) que entrega algo suyo al ritmo de la escala de rendición;
una protagonista que gana sus batallas por sí misma, no por rescate; una trama del
libro que cierra y, si la saga la tiene, una trama horizontal que no (*Variante: dark
romance policial:* un caso que cierra y una conspiración que no); y, en saga, la certeza de
que la próxima entrega existe.

Tolera mal: la digresión sin función, el procedimiento sin tensión
(*Variante: dark romance policial*), el capítulo sin el otro, el anhelo sin obstáculo, la escena de pareja
decorativa que no cambia nada, y —sobre todo— el libro que no mueve ni la relación ni la
trama horizontal.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Expectativas en la obra.
> *Qué declara aquí la obra:* cómo gana sus batallas la protagonista (inteligencia, físico, poder social…) y cada cuánto entrega algo suyo el hermético, si lo hay.

---

## ANTI-DETECCIÓN

Se conserva la **gramática de género** (secciones anteriores) y se descartan las **huellas
de autor** de los dos corpus vecinos. Prohibido reproducir:

**a) Firma del corpus del género secundario.** *Variante: dark romance policial:* firma
de la novela negra. La persona y el tiempo de su corpus, cuando no son los que fija la
biblia (en la novela negra, a menudo tercera persona y pasado); coralidad de comisaría; el equipo
como protagonista colectivo; el procedimiento como espectáculo; el forense explicando
durante dos páginas; la rueda de prensa; el POV del asesino intercalado en cursiva; el
paisaje como personaje lírico; el final que restaura la justicia institucional.
*Uso permitido del corpus:* referencia de ambientación (la textura del lugar que declare la
obra), nunca de prosa. *Uso prohibido:* venderle el libro a su público o clasificarlo en sus
categorías de la tienda.

**b) Tópicos del dark romance que la obra no quiere repetir.** Cada obra declara su
anti-firma de género: los tópicos de dark romance que no usa porque no son de su mundo o
porque su subgénero ya los ha gastado. Un subgénero que vive de
alguno de los tropos del género (mafia, *bully*) no los veta: declara qué versión gastada de ellos
evita. De qué está hecha la oscuridad de la saga lo declara la obra.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Oscuridad propia de la obra.
> *Qué declara aquí la obra:* de qué está hecha su oscuridad, qué tópicos de dark romance no repite (su anti-firma de género) y cómo actúa su antagonista de saga, si lo tiene.

---

## MARCA Y CLASIFICACIÓN (vinculante para paratextos)

- **Saga:** [el nombre que declara la obra]. No encasilla la serie en el género
  secundario (*Variante: dark romance policial:* no nombra el oficio policial: no
  encasilla la serie en novela negra).
- **Fórmula de títulos:** [la declara la obra: de dónde sale cada título y qué nombra a
  la vez].
- **Subtítulo en la tienda, siempre en este orden** (si el canal lo admite): (1) género declarado
  (*Variante: dark romance policial:* "dark romance policial"), (2) arquetipo masculino,
  (3) conflicto en una línea. El subtítulo no es literatura: es el escaparate y el campo
  de keywords visible.
- **Categorías:** las de romance, nunca las del género secundario.
  *Variante: dark romance policial* (en una tienda con árbol de categorías): ✅ Romance >
  Suspense · ✅ Romance > Contemporáneo · ❌ **NUNCA** Novela negra / Policíaca / Misterio.
- **Advertencias de contenido:** página propia antes del capítulo 1, tono directo, sin
  disculpas. En dark romance no son un trámite legal: **son una señal de pertenencia.**

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Marca y clasificación de la obra.
> *Qué declara aquí la obra:* el nombre de la saga, su fórmula de títulos y sus categorías en el canal que declara (`PRESET_<OBRA>.md` › Cabecera › Mercado y lengua).

---

## TESTS DE FUNCIONAMIENTO

- **TEST 1 — PRIMERA PÁGINA Y PRIMER CAPÍTULO.** ¿Aparece el protagonista peligroso (por defecto, él), o su presencia o su amenaza, antes que
  la trama del libro? (*Variante: dark romance policial:* ¿antes que el muerto? Si el
  libro abre en escena del crimen, se ha escrito novela negra.) Y al cerrar el capítulo 1:
  ¿hay ya promesa de la pareja (el otro visto, presente o en tensión)? Si el capítulo 1
  solo promete la trama del libro, la muestra gratuita vende un thriller.
- **TEST 2 — ESCENA LIMPIA.** Recorrer las escenas del género secundario
  (*Variante: dark romance policial:* las de investigación): ¿más de una de cada cuatro
  escenas no es página de pareja y mueve solo la trama B? La que pasa del cupo, y la que
  cabe en una línea: convertirla en párrafo de resumen o fundirla en una escena de pareja.
- **TEST 3 — REPARTO (peso de pareja).** Contando palabras reales, no intenciones: ¿cada
  bloque de cuatro capítulos y el libro llegan al suelo de pareja (regla 1: 70 %; objetivo
  80 %; o los que declare el preset), con lo que no es pareja (trama B, trama horizontal y
  elenco cuando su página no es de pareja) en el 30 % como mucho? Con dos narradores, ¿se
  cumple el reparto entre voces que declara la obra?
  Bloque por debajo: se reescaleta el siguiente. Libro por debajo: no se entrega.
- **TEST 4 — DOBLE FILO DEL CASO.** ¿La trama de este libro
  (*Variante: dark romance policial:* el caso) es la versión monstruosa de su tema
  emocional? Si se eligió primero, se ha invertido la regla 2 (el espejo).
- **TEST 5 — MIGA DE PAN** *(si hay trama horizontal)*. ¿Qué descubre ella en este libro
  sobre la trama horizontal? Si no hay respuesta concreta y tangible, el libro no se
  entrega.
- **TEST 6 — RENDICIÓN.** ¿Qué entrega quien se rinde (por defecto, él; lo declara la obra) en este libro que no había entregado antes? Si
  nada, la moneda real de la saga no ha circulado. (En un libro único o en el último de
  un dúo, la entrega es la que cierra la relación.)
- **TEST 7 — GANCHOS.** ¿Todos los capítulos cierran en gancho (salvo los cierres de
  descarga que declare la obra, dentro de su tope)? ¿Al menos dos de cada tres son de
  pareja (`PAREJA_PRIMERO.md` §3, o lo que declare el preset)? Ninguno cierra en imagen estática.
- **TEST 8 — FIDELIDAD DEL HERMÉTICO** *(si la obra declara hermético a uno de los dos)*. ¿Se
  ha blandido? Contar cuántas veces explica lo que siente. Más de las pactadas para ese
  libro en la escala de rendición: revertir.
- **TEST 9 — SIN ATRACCIÓN POR TERCEROS.** En cada escena de ella con el antagonista del
  libro u otro tercero al que se acerca, ¿hay atracción real o roce innecesario? Si sí, se
  ha roto el PELIGRO 1. (La forma de acercamiento que declare la obra se audita con ella.)
- **TEST 10 — IMPUNIDAD** *(si la obra declara una regla que la sostiene; en la variante
  policial, la del protagonista que se salta la ley)*. ¿Se ha roto esa
  regla en este libro?
- **TEST 11 — ANTI-FIRMA.** ¿Reaparece algún tic del corpus del género secundario
  (*Variante: dark romance policial:* de novela negra) o de los tópicos de dark romance
  que la obra declara no repetir?
- **TEST 12 — RECURSOS RACIONADOS** *(si la obra los declara)*. ¿Cada recurso racionado
  que declara la obra aparece como máximo las veces que declara?
- **TEST 13 — PRESENCIA.** ¿Algún capítulo sin el otro (pecados capitales), o, desde el
  primer cara a cara, más de dos seguidos sin los dos en escena fuera de una ausencia
  declarada con tope? ¿El primer cara a cara cae en el primer 10 % del libro (o donde lo adelante el preset)? Si falla la escaleta, no se encarga; si falla lo
  escrito, se reescaleta el bloque siguiente.

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Tests en la obra.
> *Qué declara aquí la obra:* su peso de pareja, su número de capítulos, el techo de sus recursos racionados, si los tiene, la forma de acercamiento a terceros que audita el TEST 9 y la regla de impunidad que audita el TEST 10, si la tiene, con lo que la sostiene y lo que la rompe.

---

## RELACIÓN CON OTROS ARCHIVOS

GENRE_CONVENTIONS modula a: STORY_SPINE (la trama B trenzada sobre la A, con el peso de
pareja de la regla 1, y apertura con él), ROMANCE_BEAT_MAP (la pareja como trama A: beats
con sus suelos y escala de rendición),
TENSION_MECHANICS (peligro, anhelo y **amenaza que viene de dentro de la pareja**),
CLUE_LEDGER (pistas de la trama del libro + migas de pan horizontales), SEAMS_AND_HINGES
(gancho obligatorio en todos los capítulos; dos de cada tres, de pareja), HEAT_DISCIPLINE
(explicitud plena y suelos de calor),
ELLIPSIS_PROTOCOL (violencia mostrada), SERIES_GLUE (la forma de la saga: pareja fija
sin HEA por libro, dúo o parejas rotativas),
CHAPTER_BRIEF (cuota de palabras por capítulo que declara la obra, y un brief que empieza por
la pareja: qué cambia entre ellos y, después, qué pone la trama B),
SCALE_CALIBRATION (extensión y número de capítulos que declara la obra).

Sugiere a AESTHETIC_REGISTER el régimen de persona y tiempo que fija la biblia (por
defecto, primera persona), la voz de ella y la de él; y a PROSE_LINE_DISCIPLINE las cuotas de frase corta y el léxico
corporal disponible.

NO tiene precedencia sobre THEMATIC_ENGINE (con el que comparte la inversión) ni sobre
CHARACTER_PHYSICS (donde vive el canon de la pareja), salvo en el contrato irrenunciable que
aquel declara, que incluye el peso de la pareja y sus suelos.

Se revisa en OPERACIÓN 0 (tras THEMATIC_ENGINE, antes de STORY_SPINE), en OPERACIÓN D y en
PASADA 1 de REVISION_PROTOCOL (auditorías de peso de pareja y presencia, escena limpia,
migas, ganchos, explicitud y anti-firma).

> **Valores de la obra →** `PRESET_<OBRA>.md` › GENRE_CONVENTIONS › Relación con otros archivos en la obra.
> *Qué declara aquí la obra:* su peso de pareja, su extensión y la horquilla de sus capítulos, y la voz de cada protagonista.
