<!-- MODELO_DarkRomance v2.0 — PROSE_LINE_DISCIPLINE: base de oficio + adenda de dark romance (v2.0) -->

# PROSE_LINE_DISCIPLINE.md

## PROPÓSITO

Este archivo regula la **anatomía gramatical de la prosa a nivel de
línea**: distribución de partes del discurso, control de modificadores,
no-repetición estructural, eliminación de tics estadísticos heredados
del modelo de lenguaje, y tests cuantitativos que verifican la
disciplina antes de cerrar un capítulo.

Su existencia responde a un hecho empírico: los modelos de lenguaje no
escriben desde una intención, escriben desde una distribución
estadística. Su prosa por defecto gravita al centro de esa
distribución, que es prosa funcional, plausible, gramaticalmente
correcta y mediocre en el sentido literal del término: tiende al medio.
Las reglas cualitativas ("evita el adverbio cuando puedas", "el
detalle concreto antes que el abstracto") son insuficientes contra ese
prior, porque son interpretables y dejan al modelo libertad de regresar
al promedio bajo justificación estética. Las reglas cuantitativas duras
("máximo X adverbios -mente por mil palabras") no son interpretables: o
se cumplen o no. Y al obligar a no cumplirlas, fuerzan al modelo a
buscar soluciones que no están en su prior, que es donde vive la prosa
de calidad.

Sin este archivo, los demás filtros de Capa 3 cazan los excesos
semánticos (SEMANTIC_OMISSION), la música muerta (PROSODY_AND_MUSIC),
la enumeración sensorial plana (SENSORY_HIERARCHY) y la exposición
disfrazada en diálogo (DIALOGUE_MECHANICS), pero ninguno se ocupa de
la anatomía estadística de la frase. Quedan agujeros: la repetición de
artículos al inicio de frases consecutivas, el doblete adjetival
calcado del LLM, los adverbios -mente fuera del verbo dicendi, el
verbo débil compensado por adjetivo, las nominalizaciones
abstractas, los hedge-adverbs ("casi", "ligeramente",
"prácticamente"). Este archivo cierra esos agujeros.

JERARQUÍA: Capa 3. Subordinado a:
- AESTHETIC_REGISTER.md (modulador de cuotas por régimen).
- VOICE_ARCHITECTURE.md (cada voz puede sobrescribir cuotas
  localmente si su idiolecto lo justifica explícitamente).
- CHARACTER_PHYSICS.md (un personaje en crisis puede violar cuotas
  como síntoma; ver REGLA DE EXCEPCIÓN POR ESTADO al final).

Opera en paralelo, sin precedencia mutua, con:
- PROSODY_AND_MUSIC.md (música de la frase; este archivo es
  anatomía).
- SEMANTIC_OMISSION.md (qué se omite; este archivo es cómo se nombra
  lo que se conserva).
- SENSORY_HIERARCHY.md (qué se percibe; este archivo es con qué
  partes del discurso se nombra lo percibido).
- DIALOGUE_MECHANICS.md (extiende cuotas y anti-tics al diálogo).

Alimenta principalmente:
- OPERACIÓN B (escritura inicial: el modelo consulta cuotas como
  guard-rail antes y durante).
- OPERACIÓN C (relectura de capítulo: tests cuantitativos por
  página).
- PASADA 4 del REVISION_PROTOCOL (trabajo de línea).

---

## REGLA FUNDACIONAL: PRECEDENCIA Y MODULACIÓN

Este archivo NO impone una estética. La estética la impone
AESTHETIC_REGISTER. Lo que este archivo impone es:

1. **Una doctrina de jerarquía gramatical** que opera en todos los
   regímenes (sección DOCTRINA DE PRIMACÍA).
2. **Cuotas concretas** cuya magnitud es función del régimen
   declarado (sección CUOTAS POR RÉGIMEN). El régimen barroco tiene
   cuotas más altas que el minimalista, no las mismas.
3. **Anti-tics LLM** que operan en todos los regímenes sin
   excepción (sección TICS LLM ESPECÍFICOS). Un régimen barroco
   tiene mucha adjetivación, pero no se le permite el ternario
   obsesivo ni el doblete calcado del modelo. Los tics LLM no son
   rasgos de régimen, son sesgos de la herramienta; ningún régimen
   los tolera.
4. **Reglas de no-repetición estructural** que también operan en
   todos los regímenes, con cuotas levemente moduladas.

Si una regla de este archivo entra en conflicto con AESTHETIC_REGISTER
o con VOICE_ARCHITECTURE, manda el régimen o la voz. Pero la mayoría
de los conflictos son aparentes: las cuotas de este archivo están
diseñadas para servir al régimen declarado, no para imponerle una
estética ajena.

---

## DOCTRINA DE PRIMACÍA NOMINAL Y VERBAL

Antes de las cuotas, la doctrina. Las cuotas se siguen de aquí.

**El sustantivo concreto es el rey.** En la jerarquía de partes del
discurso de la prosa narrativa de calidad, el sustantivo concreto
ocupa la cima. No el sustantivo en general (los abstractos —"tristeza",
"esperanza", "soledad"— pertenecen a otra categoría sometida a
SEMANTIC_OMISSION), sino el sustantivo concreto: nombres de objetos,
lugares, partes del cuerpo, materiales, herramientas, plantas,
animales, fenómenos físicos. La materia del mundo nombrada con
exactitud. Hemingway dijo que las palabras "viejas, simples y
mejores" son las que usa, contra las "diez-dolares" de Faulkner: lo
que estaba describiendo es la primacía del sustantivo concreto.

**El verbo concreto es la reina.** Inmediatamente debajo del
sustantivo. No el verbo débil (ser, estar, haber, hacer, tener, dar,
poner) seguido de complemento adjetival, sino el verbo que internaliza
el atributo: "el agua estaba helada" es prosa débil; "el agua quemaba"
es prosa de calidad. La sustitución del verbo débil-más-adjetivo por
verbo concreto es uno de los movimientos que más eleva la prosa, y es
exactamente el movimiento que el LLM no hace por defecto, porque su
prior estadístico le ofrece primero "estar/ser + adjetivo".

**El adjetivo es siervo.** Tercero en la jerarquía. Su función es
especificar lo que el sustantivo no especifica por sí mismo. Un
adjetivo que el sustantivo ya implica es ruido. "Casa grande" puede
ser legítimo o ruido según el sustantivo posible: si la casa es
notable por algo, ese algo lo nombra el adjetivo; si la casa es
ordinaria, "casa" basta. La pregunta operativa antes de cada adjetivo
es: ¿qué información añade que el sustantivo no daba? Si la respuesta
es "intensidad emocional del narrador", el adjetivo sobra y el
trabajo es del verbo o del contexto.

**El adverbio es huésped raro.** Cuarto y último. No prohibido, sino
infrecuente. Hemingway, cuya prosa es la referencia minimalista
canónica, usa adverbios de modo (-mente en español, -ly en inglés) al
42% de la frecuencia del escritor medio. Eso significa que más de la
mitad de los adverbios de modo del escritor medio son innecesarios. La
regla operativa: cada adverbio -mente debe pasar el test "¿hay un
verbo más preciso que internalice este adverbio?". Si lo hay, se
sustituye. "Caminó lentamente" pierde frente a "se arrastró", "avanzó
a tientas", "midió cada paso". El adverbio queda solo cuando ningún
verbo del español lo absorbe sin pérdida semántica.

Los adverbios de tiempo, lugar y frecuencia (entonces, ahora, allí,
nunca, después, ya) están exentos de esta restricción. Son función,
no modificación cualitativa. Hemingway los usa con normalidad. El
problema es el adverbio de modo, no el adverbio en general.

**Corolario: la prosa de calidad es una prosa donde el peso semántico
está distribuido entre sustantivos y verbos concretos, con
modificación parsimoniosa.** Es exactamente lo contrario al equilibrio
por defecto del LLM, que reparte el peso entre sustantivos genéricos
("una sensación", "un momento"), verbos débiles ("era", "tenía",
"había") y modificación abundante (adjetivos descriptivos, adverbios
-mente intensificadores). La prosa de calidad es estadísticamente
desplazada respecto al promedio.

---

## CUOTAS POR RÉGIMEN

Esta sección declara cuotas numéricas concretas. Cada cuota es por
mil palabras de prosa narrativa (excluyendo diálogo, que tiene reglas
propias en DIALOGUE_MECHANICS modulado por este archivo). La unidad
"por mil palabras" se ha elegido sobre "por página" porque es
independiente del formato; mil palabras equivalen aproximadamente a
tres páginas estándar de novela (250-300 palabras por página).

Las cuotas distinguen tres regímenes calibrados directamente:
**MINIMALISTA**, **INTERMEDIO** y **EXPANSIVO**. Los demás regímenes
del catálogo de AESTHETIC_REGISTER se derivan de estos tres por la
regla de extrapolación al final de la sección.

Cada cuota tiene **techo**, **suelo** y **valor objetivo**. El techo
es la cuota máxima: pasar de aquí marca la prosa para reescritura. El
suelo es la cuota mínima: bajar de aquí en régimen no minimalista
indica prosa desnaturalizada (no es virtud llegar a cero adverbios en
régimen expansivo; es síntoma de aplicación robótica de la
disciplina). El valor objetivo es el centro óptimo del rango.

### CUOTA 1 — ADJETIVOS CALIFICATIVOS

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 5 | 12 | 20 |
| Intermedio | 15 | 25 | 40 |
| Expansivo | 25 | 45 | 80 |

Anclaje empírico: TEST 2 de AESTHETIC_REGISTER declara ≤3 adjetivos
calificativos por 150 palabras en minimalista, 5-15 en expansivo, sin
techo en barroco. Traduciendo a por-mil: minimalista ≤20, expansivo
33-100. Las cuotas de esta tabla son consistentes con esa horquilla,
afinadas con datos LitCharts (Hemingway usa adjetivos a frecuencia
inferior al promedio, no a frecuencia mínima).

Definición operativa: cuenta solo el adjetivo calificativo en función
atributiva o predicativa (mesa larga; el cielo es azul). Quedan
excluidos: artículos, posesivos, demostrativos, numerales,
indefinidos, relacionales (adjetivos del tipo "comercial", "nacional",
"legal" cuando funcionan como categoría más que como cualidad).

### CUOTA 2 — ADVERBIOS EN -MENTE

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 2 | 5 |
| Intermedio | 1 | 5 | 12 |
| Expansivo | 2 | 10 | 25 |

Anclaje empírico: Hemingway usa adverbios de modo al 42% de la
frecuencia del escritor medio. El escritor medio en inglés usa
aproximadamente 12-15 adverbios -ly por mil palabras según
estimaciones de corpus general. Hemingway-ratio (42%) sale en torno a
5-6 por mil. La cuota minimalista de techo 5 está calibrada a
Hemingway. Régimen intermedio tiende al promedio anglosajón (12).
Régimen expansivo permite hasta el doble del promedio en su techo, lo
que aún queda por debajo del LLM por defecto (que produce adverbios
-mente con frecuencia muy alta).

Excepción declarada: los adverbios de tiempo, lugar y frecuencia
(entonces, ahora, allí, después, nunca, siempre, ya, pronto, tarde,
arriba, abajo, dentro, fuera) NO computan en esta cuota. Solo computa
el adverbio de modo, típicamente terminado en -mente, ocasionalmente
en otras formas (despacio, deprisa, así).

### CUOTA 3 — HEDGE-ADVERBS Y MITIGADORES

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 1 | 3 |
| Intermedio | 0 | 3 | 7 |
| Expansivo | 1 | 5 | 12 |

Esta cuota es la que más impacto tiene contra el sesgo LLM, porque es
donde el modelo más pierde el control. Lista operativa de
hedge-adverbs en español (no exhaustiva, ampliable):

casi, ligeramente, prácticamente, simplemente, realmente,
ciertamente, evidentemente, probablemente, posiblemente, quizás, tal
vez, bastante, demasiado, suficientemente, levemente, suavemente,
apenas, escasamente, ligero, profundamente cuando funciona como
intensificador vacío, totalmente, completamente, absolutamente,
verdaderamente.

Estos adverbios suavizan, aproximan, mitigan o intensifican sin
añadir precisión. Son tics LLM por excelencia. La doctrina: o se
elimina la mitigación (un personaje "casi sonrió" se convierte en un
personaje que sonrió o que no sonrió; el "casi" suele ser pereza), o
se sustituye por una imagen concreta que muestre la mitigación (el
labio que se levanta apenas y vuelve a quedarse quieto). Régimen
minimalista tiende a eliminar; régimen expansivo puede tolerar
mitigación reflexiva si forma parte del movimiento del pensamiento del
narrador.

### CUOTA 4 — VERBOS DÉBILES + COMPLEMENTO ADJETIVAL

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 5 | 15 |
| Intermedio | 5 | 15 | 30 |
| Expansivo | 10 | 25 | 50 |

Verbos débiles relevantes para esta cuota: ser, estar, haber, tener,
hacer, dar, poner, quedar, parecer, resultar, encontrarse. Cuenta
cada construcción "verbo débil + adjetivo" (era alto, estaba cansado,
parecía nervioso, se encontraba solo, había mucho ruido) o "verbo
débil + sustantivo abstracto" (tenía miedo, hacía calor).

La cuota es alta incluso en minimalista (techo 15) porque estas
construcciones son inevitables en español. La regla operativa es: si
puede sustituirse por verbo concreto, sustituir; si no, mantener. "El
agua estaba helada" → "el agua quemaba" o "el agua mordía". "Tenía
miedo" → "temblaba", "se le erizó la nuca", "no quería ver". "Hacía
calor" → "el aire pesaba", "el sudor empapaba la camisa". No todas
las construcciones admiten sustitución; las que la admiten y se
mantienen sin sustituir son las que cuentan en esta cuota como exceso
corregible.

Diagnóstico complementario: si el techo se supera, la prosa está
construyéndose con adjetivos colgados de verbos vacíos en lugar de
verbos cargados. La corrección es siempre la misma: buscar el verbo
que internalice el adjetivo.

### CUOTA 5 — NOMINALIZACIONES ABSTRACTAS

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 3 | 8 |
| Intermedio | 2 | 8 | 18 |
| Expansivo | 5 | 15 | 35 |

Nominalización abstracta: sustantivo derivado de un verbo o adjetivo
que podría haberse expresado como acción. "La realización del
proyecto" en lugar de "realizar el proyecto"; "el pensamiento de que
mentía" en lugar de "pensó que mentía"; "la profundidad de su mirada"
en lugar de "miraba hondo". Sufijos típicos: -ción, -sión, -miento,
-mento, -dad, -tud, -encia, -ancia, -anza, -ura, -ismo.

Las nominalizaciones son legítimas cuando el referente es nominal
de raíz (la educación, la economía, la guerra). Son exceso cuando
son verbos disfrazados de nombre. La doctrina: si la
nominalización admite reescritura como verbo sin pérdida, suele
ganarse reescribiéndola. Régimen expansivo permite nominalizaciones
reflexivas legítimas (Marías, Saer, Sebald las usan con función
estilística clara). Régimen minimalista las suprime con
agresividad.

Anclaje: el español de calidad oscila más que el inglés en
nominalización; las traducciones técnicas inflan el contador
(burocrático, jurídico, académico). En narrativa, el contador alto es
síntoma de prosa que está pensando en abstracto cuando podría estar
mostrando en concreto.

### CUOTA 6 — COMODINES SEMÁNTICOS

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 2 | 6 |
| Intermedio | 1 | 5 | 12 |
| Expansivo | 2 | 8 | 20 |

Lista operativa de comodines en español: cosa, cosas, algo, alguien,
algún, alguna, gente, persona, personas, momento, momentos, lugar,
lugares, manera, maneras, forma, formas, modo, modos, tipo, tipos,
clase, parte, partes, asunto, problema, situación, hecho.

Estos sustantivos comodín son la antítesis de la primacía nominal: en
lugar de nombrar lo concreto, nombran su categoría más vacía. "Algo
brillaba en la mesa" reemplaza por nombrar el objeto que brilla; "un
momento incómodo" reemplaza por la imagen que muestra el momento.
Régimen minimalista los elimina con agresividad; régimen expansivo
puede tolerarlos cuando el narrador piensa explícitamente en
genéricos (en pasajes reflexivos sobre categorías), pero su techo
sigue siendo bajo respecto al uso natural del LLM.

### CUOTA 7 — POSESIVOS REDUNDANTES

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 1 | 3 |
| Intermedio | 0 | 2 | 5 |
| Expansivo | 0 | 3 | 8 |

El posesivo redundante en español es calco del inglés. El inglés
exige posesivo donde el español usa artículo: "He put his hand in his
pocket" → "metió la mano en el bolsillo", no "metió su mano en su
bolsillo". El LLM, entrenado masivamente en inglés, traslada el
patrón al español. Cada posesivo "su X" debe pasar el test: ¿hay
ambigüedad sobre de quién es la X? Si no hay ambigüedad, el posesivo
es ruido y se sustituye por artículo.

La cuota es baja en todos los regímenes porque este es un calco, no
un rasgo estético. Régimen expansivo no protege calcos; tolera
extensión sintáctica, no transferencia automática de inglés.

### CUOTA 8 — VOZ PASIVA PERIFRÁSTICA

Por mil palabras de prosa narrativa.

| Régimen | Suelo | Objetivo | Techo |
|---|---|---|---|
| Minimalista | 0 | 1 | 3 |
| Intermedio | 0 | 3 | 7 |
| Expansivo | 1 | 5 | 12 |

La voz pasiva perifrástica ("fue visto", "ha sido construido", "será
recordado") es estructuralmente menos natural en español que en
inglés y más rara aún en narrativa de calidad. La pasiva refleja
("se construyó", "se recordará") es más natural y no computa en esta
cuota.

Régimen minimalista la elimina casi por completo. Régimen expansivo
la admite cuando el agente es genuinamente desconocido o
deliberadamente ocultado (típico de narradores que quieren
desplazar responsabilidad o establecer distancia épica). La cuota es
baja en todos los regímenes porque la pasiva perifrástica narrativa
suele ser otro calco.

### REGLA DE EXTRAPOLACIÓN PARA REGÍMENES NO CALIBRADOS DIRECTAMENTE

AESTHETIC_REGISTER inventaría regímenes adicionales: NAVAL-DECIMONÓNICO,
BARROCO, ORAL, PERIODÍSTICO, MIXTO. Sus cuotas se derivan de los tres
calibrados:

- **NAVAL-DECIMONÓNICO**: cuotas del INTERMEDIO en general, con dos
  ajustes específicos: la CUOTA 1 (adjetivos) sube al techo del
  INTERMEDIO (40 por mil) por la inmersión técnica que la prosa naval
  exige; las CUOTAS 2 y 3 (adverbios -mente y hedge) bajan al
  MINIMALISTA por la autoridad de época y la concreción de objeto que
  caracteriza a O'Brian, Forester, Pérez-Reverte en Alatriste.

- **BARROCO**: cuotas del EXPANSIVO en general, con un ajuste
  específico: la CUOTA 1 (adjetivos) no tiene techo por consistencia
  con AESTHETIC_REGISTER. Pero las CUOTAS 3 (hedge), 6 (comodines),
  7 (posesivos calcados) y 8 (pasiva calcada) NO se relajan: la
  exuberancia barroca legítima (Lezama, Carpentier) no es
  hedge-adverbs ni calcos del inglés; es densidad léxica y
  sintáctica.

- **ORAL**: cuotas del INTERMEDIO en general, pero con la doctrina
  invertida: muletillas y repeticiones intencionales del habla
  oralizada NO computan en cuotas. Cruzar con DIALOGUE_MECHANICS y
  VOICE_ARCHITECTURE para identificar muletillas declaradas.

- **PERIODÍSTICO**: cuotas del MINIMALISTA en general, con un ajuste:
  la CUOTA 1 (adjetivos) sube al INTERMEDIO porque el periodismo de
  alta factura (Didion, Capote, Fresán reportero) usa adjetivos
  funcionales para caracterizar y contextualizar.

- **MIXTO**: cada sección computa por su régimen declarado. Si la
  novela tiene secciones en orales y secciones en distantes, cada
  bloque tiene su cuota.

Estas extrapolaciones son punto de partida, ajustables por el proyecto
concreto. El proyecto que instancie este archivo puede declarar
cuotas custom dentro de su instancia.

**Nota sobre POPULAR-EFICIENTE.** El régimen popular-eficiente
(thriller comercial moderno, novela negra contemporánea, suspense
doméstico, género popular eficiente en general) **no se extrapola
desde aquí**. Tiene calibración directa documentada en
AESTHETIC_REGISTER.md como entrada del INVENTARIO DE REGÍMENES, con
cuotas explícitas para las ocho cuotas de este archivo (CUOTAS 1 y 2
ajustadas al alza en rango INTERMEDIO; CUOTAS 3, 4, 6, 7, 8 en rango
MINIMALISTA; CUOTA 5 en rango INTERMEDIO): el tratamiento por
extrapolación subdotaba al régimen y producía cuotas inconsistentes
con su corpus de referencia (Lehane, Pelecanos, Flynn, thrillers
nórdicos en su rama eficiente).

---

## REGLAS DE NO-REPETICIÓN ESTRUCTURAL

Estas reglas operan en todos los regímenes con el mismo techo. La
repetición estructural es uno de los tics más detectables tanto del
mal escritor como del LLM. La razón es la misma: ambos siguen el
camino de menor resistencia gramatical. La regla rompe ese camino.

### REGLA 1 — INICIO DE FRASE

Máximo de **dos frases consecutivas** iniciadas con el mismo elemento
de las siguientes categorías:

- Mismo artículo definido (El / La / Los / Las).
- Mismo artículo indefinido (Un / Una / Unos / Unas).
- Mismo sujeto pronominal (Él / Ella / Ellos / Ellas / Yo / Tú).
- Mismo nombre propio.
- Misma estructura sintáctica (sujeto+verbo, gerundio inicial,
  complemento circunstancial inicial, oración subordinada inicial).
- Mismo conector neutro (Y, Pero, Entonces, Después, Sin embargo).

Tres frases consecutivas iniciadas con el mismo elemento es violación.
La tercera fuerza reescritura. Reescritura típica: trasladar un
complemento al inicio, invertir orden, fusionar dos frases, abrir con
un objeto en vez de con sujeto.

Esta regla complementa la sección "COMIENZOS DE FRASE" de
PROSODY_AND_MUSIC, que solo trata conectores neutros. Aquí se cubren
las cuatro familias completas que habían quedado fuera de PROSODY.

### REGLA 2 — INICIO DE PÁRRAFO

Máximo de **tres párrafos consecutivos** iniciados con la misma
familia de apertura (mismo tipo de elemento gramatical o misma
fórmula). Los párrafos cortos en escenas de acción rápida o diálogo
intercalado quedan exentos cuando la rapidez es la función.

### REGLA 3 — LÉXICO REPETIDO EN PÁRRAFO

Dentro de un párrafo, ningún sustantivo, verbo o adjetivo distintivo
debe aparecer más de **dos veces** salvo cuando la repetición sea
deliberada como recurso de PROSODY_AND_MUSIC (repetición declarada en
VOICE_ARCHITECTURE, motivo recurrente de THEMATIC_ENGINE) o cuando el
término sea funcionalmente insustituible (un nombre propio, una pieza
única del mundo).

Excepción: pronombres, artículos y conjunciones no computan. La regla
opera sobre palabras de contenido.

Tic LLM relacionado: "elegant variation" — el LLM, al detectar
repetición, sustituye el segundo nombre del personaje por sinónimo o
descripción ("el protagonista", "el joven", "el muchacho"). Esto está
prohibido por DIALOGUE_MECHANICS y VOICE_ARCHITECTURE, no es lo que
busca esta regla. La regla busca la repetición no deliberada de
verbos y sustantivos comunes (cuatro veces "mirar" en un párrafo,
tres veces "pensar"). Cuando se detecta, se reescribe sustituyendo o
reorganizando, no metiendo sinónimos.

### REGLA 4 — CIERRE DE FRASE

Cruzar con PROSODY_AND_MUSIC sección FINALES DE FRASE. La regla
adicional aquí: ninguna palabra de cierre de frase debe repetirse en
dos frases consecutivas. Si dos frases seguidas terminan en la misma
palabra, la segunda se reescribe.

---

## REGLAS DE ALTERNANCIA OBLIGATORIA

PROSODY_AND_MUSIC declara alternancia como recomendación. Este archivo
la declara como exigencia cuantitativa.

### LONGITUD DE FRASE EN PÁRRAFO

En cualquier párrafo de cinco o más frases, la dispersión de
longitudes debe cumplir:

- Diferencia entre frase más corta y frase más larga del párrafo: al
  menos un factor 2 (la más larga al menos doble que la más corta).
- No más de tres frases consecutivas dentro del mismo cuartil de
  longitud (corto, medio-corto, medio-largo, largo).

Régimen minimalista: cuartiles definidos sobre el rango 6-14 palabras
declarado en AESTHETIC_REGISTER. Régimen expansivo: cuartiles
definidos sobre 20-60 palabras. Los demás regímenes usan sus rangos
respectivos.

### LONGITUD DE PÁRRAFO EN CAPÍTULO

En cualquier capítulo de más de veinte párrafos, debe haber al menos:

- Un párrafo de una sola frase.
- Un párrafo largo (más del doble del párrafo medio del capítulo).
- Un párrafo medio.

La distribución no debe ser uniforme. Si todos los párrafos del
capítulo están entre el 80% y el 120% de la media, el capítulo suena
plano y hay que reescribir.

---

## TICS LLM ESPECÍFICOS — CATÁLOGO DE DETECCIÓN

Esta sección es el corazón anti-LLM del archivo. Los tics aquí
listados están documentados empíricamente (Wikipedia "Signs of AI
writing", estudio Gray 2024 sobre 14 millones de abstracts
post-2023, análisis de Stylometric-Semantic Pattern Learning
detectando aidiolectos). Operan en todos los regímenes sin excepción.
Régimen barroco no protege estos tics; los regímenes son rasgos del
proyecto, los tics son rasgos de la herramienta.

### TIC 1 — TERNARIO OBSESIVO

Patrón: "A, B y C" donde los tres elementos tienen función paralela
(tres adjetivos, tres sustantivos, tres frases cortas, tres
acciones).

Ejemplo defectuoso: "La habitación era oscura, fría y silenciosa."
Tres adjetivos en la misma función predicativa. El ternario tiene
cadencia en español, lo que lo hace tentador, y el LLM lo produce con
frecuencia anómala (ver Wikipedia "Signs of AI writing", "rule of
threes").

Cuota: máximo **un ternario por página** (250-300 palabras). Cuando
aparece, debe estar justificado por la materia (acumulación que la
escena pide) y no por hábito formal. Sustituciones: dos elementos en
lugar de tres ("oscura y fría", o "oscura, casi fría"), un elemento
solo si carga peso suficiente, una imagen concreta que sustituya la
enumeración ("la habitación era una nevera").

PROSODY_AND_MUSIC ya declara este tic en su ERROR 3. Este archivo lo
cuantifica.

### TIC 2 — DOBLETE ADJETIVAL

Patrón: dos adjetivos coordinados por "y" o por coma modificando al
mismo sustantivo.

Ejemplo defectuoso: "una sombra densa y oscura"; "el aire frío,
quieto"; "una mirada larga y dura".

El doblete adjetival es prima del ternario y aún más frecuente en
prosa LLM. Casi siempre uno de los dos adjetivos es redundante o
ambos son sustituibles por uno más preciso. "Sombra densa y oscura"
→ "tiniebla". "Mirada larga y dura" → "mirada de sentencia", o
simplemente "mirada larga" si la dureza ya está en el contexto.

Cuota: máximo **dos dobletes adjetivales por página**. Por encima,
reescribir.

### TIC 3 — PARALELISMO NEGATIVO ("NO X SINO Y")

Patrón: "No era X. Era Y." / "No solo X, sino también Y." /
"No tanto X, cuanto Y."

Ejemplo defectuoso: "No era miedo. Era anticipación." / "No era
solo cansancio, era resignación." Esta estructura retórica es uno de
los marcadores más fuertes del LLM (Wikipedia "Signs of AI writing",
"negative parallelisms"). El modelo la produce porque suena profunda
sin contenido.

Cuota: **máximo uno por capítulo**, y solo si la oposición carga
peso real. Cuando aparece como hábito, la
sustitución típica es: nombrar directamente el matiz sin la negación
previa. "Era anticipación" basta. "Resignación" basta. La negación
del primer término es retórica vacía.

### TIC 4 — FRASE-RESUMEN AL CIERRE DE PÁRRAFO

Patrón: el párrafo termina con una frase que glosa o resume lo que se
acaba de mostrar.

Ejemplo defectuoso: "Cerró la puerta sin mirarlo. Recogió las
llaves. Salió a la calle. Era una despedida sin palabras." La última
frase glosa lo mostrado. Es exposición disfrazada de cierre. El
lector ya entendió que era una despedida; nombrarlo lo cancela.

Cuota: máximo **una frase-resumen por capítulo**, idealmente cero.
Cuando aparece, se elimina o se reescribe transformándola en imagen
concreta que extienda lo mostrado en lugar de glosarlo. Cruzar con
SEMANTIC_OMISSION reglas 1 y 2 (no redundancia emocional, no
explicación simultánea de motivos): este tic es la versión a escala
de párrafo del mismo problema.

### TIC 5 — CIERRE SENTENCIOSO DE CAPÍTULO

Patrón: el capítulo cierra con una frase que pretende ser
aforística, profunda, memorable. "Y así fue como entendió que el
amor también era una forma de olvido." "Algunas heridas no se ven."

El LLM produce cierres sentenciosos por defecto porque su prior los
asocia a "cierre fuerte". El lector entrenado los lee como
manipulación. Los cierres efectivos son típicamente concretos
(imagen, gesto, fragmento de diálogo) o suspensos (no cerrar; dejar
abierto).

Cuota: ningún capítulo de la novela debe cerrar con frase
sentenciosa, salvo declaración explícita en VOICE_ARCHITECTURE de
narrador con autoridad sentenciosa de época (cierto naval
decimonónico, cierto siglo XIX). En esos casos, la sentencia debe
estar enraizada en la voz declarada, no aparecer como salida cómoda.

### TIC 6 — GERUNDIO DÉBIL

Patrón: gerundio de posterioridad o de causa, ambos incorrectos en
español formal aunque el LLM los produce.

Ejemplo defectuoso: "Salió de la habitación, cerrando la puerta tras
de sí." (gerundio de posterioridad: cerró después de salir, no
mientras salía). "Estaba cansado, habiendo trabajado todo el día"
(gerundio de causa, calco del inglés).

Cuota: cero gerundios de posterioridad o causa. Sustitución: "salió
y cerró la puerta"; "estaba cansado porque había trabajado todo el
día" (o reescritura completa para evitar la causa explícita). El
gerundio de simultaneidad ("salió mirando el reloj") es legítimo y no
computa.

### TIC 7 — MITIGACIÓN ATEMPERADA CONSTANTE

Patrón: prosa donde casi cada afirmación viene atenuada por
hedge-adverb (cubierto en CUOTA 3) o por mitigador sintáctico
("parecía", "como si", "casi se diría que", "uno podría pensar que").

El LLM mitiga por defecto porque su entrenamiento le penaliza
afirmar con confianza. La prosa narrativa no es discurso académico;
afirmar es función del narrador. La mitigación constante es síntoma
de modelo entrenado a hablar en condicional.

Cuota: máximo **tres mitigadores por mil palabras**. Sustitución
típica: eliminar la mitigación. Si el narrador es genuinamente no
fiable (declaración en VOICE_ARCHITECTURE), la no-fiabilidad se
construye con otros mecanismos (sesgo en interpretación, omisión,
contradicción), no con mitigación adverbial constante.

### TIC 8 — LÉXICO MARCADOR

Familia de palabras cuyo uso se ha disparado con la introducción de
modelos de lenguaje grandes. Inventario en español (no exhaustivo,
ampliable):

**Sustantivos marca**: tapiz, matiz, esencia, trasfondo, atisbo,
vestigio, destello, fulgor, halo, eco, susurro, latido, abismo,
crisol, prisma, tejido (como metáfora), urdimbre, danza (como
metáfora de cualquier cosa que se mueve coordinadamente).

**Adjetivos marca**: minucioso, intrincado, sutil cuando funciona
como elogio vacío, profundo cuando intensifica, vibrante, palpable,
inequívoco, inconfundible, indeleble, fugaz, etéreo.

**Adverbios marca**: profundamente, sutilmente, intrincadamente,
vibrantemente, palpablemente, inequívocamente, inconfundiblemente,
indeleblemente, fugazmente, etéreamente, ciertamente, evidentemente,
indudablemente.

**Verbos marca**: ahondar, indagar (cuando el contexto pide
"investigar"), urdir, tejer (como metáfora), iluminar (como
metáfora), bañar (de luz), envolver (de atmósfera), navegar (como
metáfora), surcar (como metáfora).

Cuota: cada palabra de esta lista que aparece en el texto exige
justificación. Si justifica, se mantiene. Si es elección por
inercia, se sustituye por término más concreto del campo semántico.
"Una sutil tristeza" → "tristeza" o imagen concreta que la porte.
"Tejido emocional" → la emoción sin metáfora textil.

Esta lista debe revisarse con periodicidad porque los aidiolectos de
los modelos cambian. El inventario se actualiza cuando los modelos
vigentes muden de tics (PROTOCOLO_CAPTURA_APRENDIZAJE).

### TIC 9 — EM-DASH / RAYA INTERCALADA OVERKILL

El em-dash inglés y la raya intercalada española como signo de
puntuación expresivo se ha convertido en marcador LLM (Wikipedia
"Signs of AI writing", "Em dash overkill"). El modelo abusa de la
raya para insertar incisos que en prosa de calidad humana suelen ir
con coma o paréntesis.

Cuota: máximo **una raya intercalada por mil palabras** en régimen
neutro. Régimen oral o expansivo puede subir a tres. Por encima,
sustituir la mayoría por coma o paréntesis o reescribir el inciso
como frase aparte. La raya queda para los incisos que de verdad
disrumpen (interrupción, salto de pensamiento, énfasis fuerte).

En diálogo, la raya tiene función propia (apertura y cierre de
intervención, atribución postpuesta) y no computa en esta cuota; ver
DIALOGUE_MECHANICS.

### TIC 10 — CADENCIA DE OPENING COMMERCIAL

Patrón típico de apertura de capítulo o escena: descripción
ambiental atemperada que no aporta información narrativa y se siente
como "preparar al lector".

Ejemplo defectuoso: "Era una mañana fría de noviembre. La luz
entraba oblicua por la ventana, dorada y quieta. Algo en el aire
tenía un peso distinto al de los otros días."

Tres frases que no hacen nada. El LLM las produce porque su prior de
"apertura" incluye este patrón ambiental. La prosa de calidad abre
con acción, con voz, con dato cargado, no con clima decorativo.

Cuota: ninguna apertura de capítulo construida sobre el patrón
clima-ambiental sin función. Cuando un capítulo necesita establecer
tiempo y lugar, se hace en una frase con dato concreto, no en tres
frases atmosféricas.

---

## ANCLAJES EMPÍRICOS

Las cuotas de este archivo están calibradas contra evidencia
estilométrica documentada. Esta sección lista las fuentes para que
revisiones futuras puedan verificar y ajustar.

**Fuente 1 — LitCharts Analitics, Justin Rice (2016).** Análisis
cuantitativo de Hemingway y comparativa con Bukowski, Carver,
Chandler, Fitzgerald, Proust, Stein, Steinbeck. Hallazgos relevantes:
Hemingway promedia ~10 palabras por frase (varía: más corto en
primeras novelas, más largo en El viejo y el mar tardío); usa
adverbios -ly al 42% de la frecuencia del escritor medio; tiene
menos sustantivos y más pronombres que el promedio; usa más verbos y
menos adjetivos que el promedio. Sus 20 adverbios más frecuentes son
casi todos de tiempo/lugar/frecuencia, no de modo. El 70% de sus
adverbios totales pertenece a esos 20.

**Fuente 2 — Densidad léxica narrativa.** Estimaciones de Halliday
(1985), Ure (1971) y derivaciones modernas. Ficción narrativa: 45-51%
de palabras de contenido sobre total. Por debajo de 45% prosa
genérica conversacional; por encima de 55% prosa académica densa. La
prosa narrativa de calidad tiende al alto del rango (cerca de 50%).

**Fuente 3 — Estudio Gray (2024) sobre marcadores LLM.** Análisis de
14 millones de abstracts en PubMed 2010-2024. Detecta surgimiento
abrupto post-2023 de "style words" — adjetivos y adverbios — frente
al patrón pre-LLM donde los excesos eran sustantivos por evento
(COVID). Inventario de palabras-marca: meticulous, intricate,
commendable, innovative, notable, versatile, noteworthy, invaluable,
pivotal, potent, fresh, ingenious; meticulously, reportedly,
lucidly, innovatively, aptly, methodically, excellently,
compellingly, impressively, undoubtedly, scholarly, strategically.

**Fuente 4 — Wikipedia "Signs of AI writing".** Catálogo
operacional de tics LLM mantenido por la comunidad de
WikiProject AI Cleanup, ~15.000 palabras. Recopilación de patrones
detectados en miles de envíos. Base del inventario de TIC 1 a TIC 10
de este archivo.

**Fuente 5 — Tradición hispana sobre primacía nominal.** Estudios
estilísticos de Crónica de una muerte anunciada (García Márquez)
documentan "predominio del sustantivo desnudo, acorde con el
dinamismo y la agilidad propios de la crónica". Réquiem por un
campesino español (Sender) documentado como "estilo directo,
sencillo, conciso y natural, con escasez de descripciones largas,
pero con unos adjetivos que sirven para crear una imagen con tan
solo una pincelada". La doctrina de primacía nominal tiene linaje
formal en la crítica hispana, no es trasplante anglosajón.

**Calibración pendiente:** las cuotas para regímenes específicos del
español (Marías expansivo, Saer expansivo intermedio, Onetti
oral-minimalista, Rulfo oral-minimalista, Pérez-Reverte
naval-decimonónico, Lezama barroco) requieren medición directa de
corpus que aún no se ha hecho. Las cuotas actuales son punto de
partida; los proyectos creativos que instancien este archivo y midan
sus referentes pueden afinar y devolver el aprendizaje al modelo a
través del PROTOCOLO_CAPTURA_APRENDIZAJE.

---

## TESTS CUANTITATIVOS

Tests operativos que verifican la disciplina. Se ejecutan con conteo,
no con impresión. Idealmente automatizados con un script externo (POS
tagger estándar como Stanza, spaCy o Freeling para español).

### TEST POR PÁGINA (~250-300 palabras)

Para cada página de prosa narrativa:

1. Contar adjetivos calificativos. Verificar que entran en el rango
   declarado para el régimen.
2. Contar adverbios -mente y otros adverbios de modo. Verificar
   rango.
3. Contar hedge-adverbs de la lista. Verificar rango.
4. Contar verbos débiles + complemento adjetival. Verificar rango.
5. Contar nominalizaciones abstractas. Verificar rango.
6. Contar comodines de la lista. Verificar rango.
7. Contar posesivos "su/sus" antes de partes del cuerpo, ropa,
   objetos personales. Aplicar test de ambigüedad.
8. Contar voces pasivas perifrásticas. Verificar rango.

Si una cuota se viola por más del 50% del techo, marcar la página
para reescritura intensiva. Si se viola dentro del 50%, marcar para
revisión específica de la cuota violada.

### TEST POR CAPÍTULO

Para cada capítulo:

1. Calcular dispersión de longitud de párrafo. ¿Hay al menos un
   párrafo corto, uno medio, uno largo? ¿La distribución es
   diversa?
2. Buscar inicio de capítulo: ¿es funcional/cargado o
   clima-ambiental decorativo? Aplicar TIC 10.
3. Buscar cierre de capítulo: ¿es sentencioso? Aplicar TIC 5.
4. Buscar frases-resumen al cierre de párrafos. Aplicar TIC 4.
5. Contar paralelismos negativos. Aplicar TIC 3 cuota por capítulo.
6. Verificar regla 1 de no-repetición (inicios de frase): ¿hay
   tríos o más con mismo elemento inicial?
7. Verificar regla 2 (inicios de párrafo): ¿hay cuartetos o más?

### TEST POR LIBRO

Para cada libro completo:

1. Contar palabras-marca de TIC 8 (léxico marcador). Si una palabra
   de la lista aparece más de cinco veces y ninguna está justificada
   por motivo recurrente declarado, eliminar al menos hasta dejar
   una o dos.
2. Verificar densidad léxica global. Debe entrar en 45-51% para
   narrativa de calidad. Por debajo: prosa con demasiados
   funcionales, probablemente conversacional o sin trabajo. Por
   encima: prosa académica, probablemente sobreescrita.
3. Verificar promedio de palabras por frase. Debe entrar en el rango
   declarado por AESTHETIC_REGISTER. Si se desvía, o el régimen está
   mal declarado o la prosa no respeta el régimen.
4. Verificar promedio de palabras por párrafo. Debe alternar dentro
   del libro, no quedar uniforme.

### TEST DE LECTURA EN VOZ ALTA EXTENDIDO

PROSODY_AND_MUSIC declara la lectura en voz alta como test prosódico.
Este archivo añade una dimensión: durante la lectura en voz alta,
detectar también los tics de TIC 1 a TIC 10 que el oído percibe como
"sonido a IA" sin saber por qué. Los lectores entrenados detectan
prosa LLM en pocos párrafos por la cadencia y los marcadores aunque
no puedan articular el motivo. La lectura en voz alta hecha con esta
sensibilidad es el test integrador.

---

## PROTOCOLO DE APLICACIÓN POR FASE

### FASE DE ESCRITURA (OPERACIÓN B)

Durante la escritura inicial, el sistema consulta este archivo como
guard-rail antes y durante cada escena. La consulta no es
exhaustiva: bloquearía el flujo. La consulta es **selectiva por
familia de tic activa**:

- Antes de empezar el capítulo, repaso de las cuotas del régimen
  declarado (tabla resumen mental).
- Durante la escritura, atención específica a TIC 4 (frase-resumen)
  y TIC 7 (mitigación) porque son los que más fácilmente se cuelan
  en el flujo.
- Al terminar la escena, antes de cerrarla, conteo rápido de
  adverbios -mente y dobletes adjetivales (TIC 2 y CUOTA 2).

### FASE DE RELECTURA DE CAPÍTULO (OPERACIÓN C)

Tras escribir el capítulo completo, ejecutar el TEST POR CAPÍTULO
de la sección anterior. Marcar violaciones y reescribir antes de
cerrar el capítulo y pasar al siguiente. Este es el momento crítico
de aplicación: si se deja para PASADA 4, el trabajo acumulado es
mucho mayor.

### FASE DE PASADA 4 (REVISION_PROTOCOL)

En la pasada 4 de revisión final, ejecutar TEST POR PÁGINA y TEST
POR LIBRO completos sobre todo el manuscrito. Las violaciones que
sobrevivieron a la fase de OPERACIÓN C aparecen aquí y se corrigen
con el manuscrito ya estable estructuralmente.

### FASE DE AUDITORÍA DE LIBRO (PASADA 1 + PASADA 4)

El TEST POR LIBRO se ejecuta una vez en pasada 1 (para verificar que
la prosa global respeta el régimen declarado, y si no, decidir
si corregir prosa o redeclarar régimen) y una vez en pasada 4 (para
verificar que las correcciones de línea no han desplazado la
prosa fuera del régimen).

---

## REGLA DE EXCEPCIÓN POR ESTADO DE PERSONAJE

(Cruza con CHARACTER_PHYSICS.md, fase 3 del arco defensivo, y con
SEMANTIC_OMISSION sección MODULACIÓN POR PERSONAJE EN CRISIS.)

Un personaje cuyo mecanismo de defensa ha colapsado puede empezar a
producir prosa que viola las cuotas: adjetivos en cascada, mitigación
constante, ternarios obsesivos, frases-resumen explicativas.

Cuando esto ocurre como síntoma del colapso del personaje en
indirecto libre o en su voz directa, las cuotas se relajan en esa
escena específica como mecanismo de caracterización.

Test para distinguir síntoma legítimo de aplicación robótica:

- ¿La violación de cuotas coincide con un punto declarado de crisis
  en el arco del personaje?
- ¿Tiene marcas del idiolecto del personaje declarado en
  VOICE_ARCHITECTURE?
- ¿Un lector atento la lee como descomposición del personaje, no como
  prosa floja del autor?

Si las tres respuestas son sí, mantener. Si alguna es no, el modelo
está justificándose a posteriori. La excepción no se aplica para
liberar al modelo de las cuotas; se aplica para preservar
caracterización ya diseñada.

---

## ERROR DEL SISTEMA A EVITAR

El error más probable de aplicación de este archivo es la
**sobreaplicación**: convertir cualquier prosa en minimalista por
inercia disciplinaria. Régimen barroco tiene adjetivos. Régimen
expansivo tiene oraciones largas con subordinación. Régimen oral
tiene repeticiones intencionales. Las cuotas existen para servir al
régimen declarado, no para imponerle una estética hemingwayana.

La regla operativa de prevención: antes de aplicar una cuota o un
filtro, consultar AESTHETIC_REGISTER y verificar el régimen vigente.
Si una corrección rompe el régimen para satisfacer la cuota, la
corrección está mal: o la cuota está mal calibrada para ese régimen
y debe ajustarse en la instancia del proyecto, o el filtro se aplica
con menos agresividad.

El segundo error frecuente es **declarar régimen y no respetarlo en
prosa**: el proyecto declara régimen expansivo en AESTHETIC_REGISTER
pero la prosa real entra en cuotas minimalistas. Esto significa o
que el régimen declarado está mal (la prosa real es minimalista y
debe redeclararse), o que el modelo está aplicando este archivo en
exceso. La pasada 1 detecta este desalineamiento y obliga a decidir.

El tercer error es **confundir tic LLM con rasgo de género**. Un
tic LLM es un patrón estadísticamente sobrerrepresentado en la
producción del modelo respecto a la producción humana de calidad
en cualquier régimen. Régimen oral tiene muletillas, pero las
muletillas declaradas en VOICE_ARCHITECTURE no son tic LLM: son
caracterización. Régimen barroco tiene profusión adjetival, pero la
profusión declarada en AESTHETIC_REGISTER no es tic LLM: es estética.
El tic LLM es lo que aparece sin haberse declarado, por inercia del
modelo.

---

## NOTA PARA VERSIONES FUTURAS DEL MODELO

Este archivo declara cuotas iniciales basadas en evidencia
empírica disponible al cierre de la sesión que lo produjo. Las
cuotas para regímenes específicos del español (Marías, Saer,
Onetti, Rulfo, Pérez-Reverte, Lezama y otros) requieren medición
directa de corpus.

Pasos recomendados para versiones futuras:

1. **Medición de corpus de referencia.** Tomar veinte páginas
   representativas de cada autor de referencia, pasarlas por POS
   tagger estándar, contar las ocho cuotas. Producir tabla
   detallada de cuotas-objetivo por autor. Refinar las cuotas de
   este archivo con esos datos.

2. **Actualización del inventario de TIC 8.** El léxico marcador
   evoluciona con los modelos. Cada año o cada cambio mayor de
   generación de modelo, revisar la lista contra estudios recientes
   y testimonios de detección.

3. **Ampliación a otros idiomas.** Las cuotas y los tics tienen
   componentes universales y componentes específicos del idioma.
   La ampliación a otros idiomas en proyectos creativos no
   castellanos requiere medición de corpus en esos idiomas y
   adaptación del inventario de hedge-adverbs y comodines.

4. **Calibración por época.** Una novela ambientada en el siglo
   XIX puede requerir cuotas distintas que una contemporánea, no
   solo por régimen, sino por convención de época. Las cuotas
   actuales asumen narrativa contemporánea o de época pero
   contada con voz contemporánea. Si la voz es declaradamente de
   época, las cuotas se modulan en consecuencia.

5. **Diálogo vs narración.** Las cuotas de este archivo se aplican
   a prosa narrativa. El diálogo tiene sus propias cuotas implícitas
   en DIALOGUE_MECHANICS. Una versión futura podría declarar cuotas
   explícitas para diálogo (densidad de adverbios en dicendi,
   muletillas por personaje, etc.).

---

## RELACIÓN CON OTROS ARCHIVOS

PROSE_LINE_DISCIPLINE.md dialoga con diecisiete archivos del catálogo,
organizados por nivel de criticidad de la coordinación, mediante notas
de redirección recíprocas en los archivos huéspedes.

### CRÍTICO

Archivos cuya autoridad o régimen modula cuotas, sobreescribe doctrinas
o introduce excepción legítima sobre las reglas de este archivo.

- **AESTHETIC_REGISTER.md** (modulador). Régimen estético declarado
  en el proyecto modula las ocho cuotas de este archivo. Los regímenes
  MINIMALISTA, INTERMEDIO y EXPANSIVO están calibrados directamente en
  CUOTAS POR RÉGIMEN. Los regímenes NAVAL-DECIMONÓNICO, BARROCO, ORAL,
  PERIODÍSTICO y MIXTO se derivan en REGLA DE EXTRAPOLACIÓN. El régimen
  POPULAR-EFICIENTE está calibrado directamente en AESTHETIC_REGISTER
  (entrada del INVENTARIO DE REGÍMENES con cuotas explícitas para las
  ocho cuotas), no se extrapola desde aquí. El campo LECTOR IMPLÍCITO
  puede modular tolerancia operativa a
  ciertas cuotas (lector culto admite cuotas más altas en hedge y
  nominalización si la voz es reflexiva; lector de lectura rápida exige
  disciplina más estricta en techo de adjetivación y de longitud). El
  TEST 2 de AESTHETIC_REGISTER sobre densidad de adjetivación tiene
  redirección a este archivo para la cuantificación detallada.

- **VOICE_ARCHITECTURE.md** (sobreescritura legítima). Cada voz
  narrativa puede sobreescribir cuotas globales localmente si su
  idiolecto declarado lo justifica. La sobreescritura es legítima
  cuando los componentes de la FICHA POR VOZ (registro léxico,
  sintaxis característica, fijaciones perceptivas, lo que la voz no
  nombra, musicalidad, tiempo verbal dominante) declaran explícitamente
  el rasgo y su función. La sección IDIOLECTO Y SOBREESCRITURA DE
  CUOTAS GLOBALES de aquel archivo es la sede formal de la
  sobreescritura. La sección TIEMPO VERBAL DOMINANTE modula cadencia y por tanto cuotas locales en ciertos
  casos (la voz en presente histórico tiende a cuotas más bajas de
  CUOTA 4; la voz en pluscuamperfecto como marco tiende a cuotas más
  altas de CUOTA 5). La distinción tic LLM versus rasgo de idiolecto
  declarado se ancla en la sección ERROR DEL SISTEMA A EVITAR de este
  archivo: el rasgo declarado es legítimo, el tic emergente sin
  declaración no.

- **CHARACTER_PHYSICS.md** (autoridad bidireccional sobre excepción).
  La REGLA DE EXCEPCIÓN POR ESTADO DE PERSONAJE de este archivo opera
  en coordinación bidireccional con la sección SÍNTOMAS VERBALES DEL
  COLAPSO de CHARACTER_PHYSICS. La autoridad sobre cuándo el personaje
  está en crisis reside allí (vinculada al ARCO DE DEFENSA y al
  MECANISMO DE DEFENSA del personaje, en cualquiera de los cinco tipos
  de antagonismo declarados); el tratamiento operativo de los síntomas
  verbales reside aquí (cuáles cuotas se relajan, en qué rango, con
  qué tests de verificación). La excepción no libera al modelo de las
  cuotas; preserva caracterización ya diseñada.

### IMPORTANTE

Archivos en paralelo operativo dentro de Capa 3 (coordinación de
jurisdicciones), o archivos de Capa 1 y Capa 2 que aportan densidad de
fondo, modulación local o consigna de capítulo, o archivos que invocan
las cuotas y los anti-tics en pasadas de revisión.

- **PROSODY_AND_MUSIC.md** (paralelo en Capa 3, sin precedencia mutua).
  Música de la frase contra anatomía gramatical. Reparto de
  jurisdicción explícito: PROSODY trabaja la cadencia, la longitud, los
  acentos, la respiración rítmica de la frase; este archivo trabaja la
  distribución de partes del discurso, las cuotas, los anti-tics. La
  sección COMIENZOS DE FRASE de PROSODY tiene redirección a la REGLA 1
  de este archivo, que cubre repetición de elementos al inicio más
  allá de los conectores neutros que cubre PROSODY.

- **SEMANTIC_OMISSION.md** (paralelo en Capa 3, sin precedencia mutua).
  Qué se omite contra cómo se nombra lo que se conserva. SEMANTIC
  trabaja la elisión de información ya inferible y la depuración de
  redundancia semántica; este archivo trabaja la anatomía gramatical
  de lo que sobrevive a esa elisión. El FILTRO 4 de SEMANTIC sobre
  adverbios en diálogo tiene redirección a la CUOTA 2 (adverbios
  -mente) de este archivo, que cubre la cuota global; aquel filtro
  cubre el caso específico del adverbio en dicendi.

- **DIALOGUE_MECHANICS.md** (paralelo en Capa 3, extiende al diálogo).
  Las cuotas y los anti-tics de este archivo se extienden al diálogo
  con dos modulaciones: las muletillas declaradas como idiolecto del
  personaje en la ficha de DIALOGUE_MECHANICS no computan en cuotas
  (paralelo a la sobreescritura por idiolecto de voz narrativa); los
  hedge-adverbs y comodines en boca de personaje sí computan salvo
  declaración explícita de rasgo de idiolecto. La sección ADVERBIOS EN
  ATRIBUCIÓN de DIALOGUE tiene redirección a TIC 7 (mitigación
  atemperada) y CUOTA 2 (adverbios -mente) de este archivo.

- **SENSORY_HIERARCHY.md** (paralelo en Capa 3, sin precedencia mutua).
  Qué se percibe contra con qué partes del discurso se nombra lo
  percibido. SENSORY trabaja la jerarquía sensorial, las sinestesias y
  el detalle revelador; este archivo trabaja la anatomía gramatical
  con que se construye la percepción nombrada. La sección SINESTESIAS
  Y CRUCES SENSORIALES de SENSORY tiene redirección a TIC 1 (ternario
  obsesivo) y TIC 2 (doblete adjetival) de este archivo. La sección EL
  DETALLE REVELADOR de SENSORY conecta con la DOCTRINA DE PRIMACÍA
  NOMINAL Y VERBAL: el detalle se construye con sustantivo concreto y
  verbo concreto, no con acumulación adjetival.

- **SUBTEXT_MECHANICS.md** (paralelo en Capa 3, sin precedencia mutua).
  Lo no dicho contra lo dicho con qué economía. SUBTEXT trabaja la
  presión semántica del silencio, la indirección, lo que el texto deja
  sin formular; este archivo trabaja la economía gramatical de lo que
  el texto sí formula. La coordinación entre los dos archivos es
  esencial en escenas de alta carga emocional, donde el subtexto es
  alto y la prosa de línea exige disciplina extra para no enturbiar el
  silencio con prosa floja.

- **ELLIPSIS_PROTOCOL.md** (paralelo en Capa 3, modula por modo
  elegido). La sección TRATAMIENTO DE CONTENIDO CARGADO declara cuatro modos (MOSTRADO, ELIDIDO, DESCRITO SECO,
  DESCRITO POÉTICO) con coordinación con régimen estético. El modo
  elegido modula la prosa: DESCRITO SECO impone cuotas estrictas de
  CUOTA 1, CUOTA 3 y TIC 1; DESCRITO POÉTICO admite cuotas más altas
  pero exige trabajo prosódico declarado en PROSODY. La cuota se
  respeta dentro del modo, no contra el modo.

- **SCALE_CALIBRATION.md** (aporta densidad de fondo). La densidad de
  suceso por unidad de palabra declarada por escala (corta, media,
  larga, extensa) es la densidad de fondo sobre la que se calibran las
  cuotas cuantitativas. La conexión opera en una sola dirección: SCALE
  declara densidad de fondo; este archivo aplica cuotas que respetan
  esa densidad. Si surge incompatibilidad entre cuotas exigentes de
  minimalista y escala extensa, o entre cuotas permisivas de expansivo
  y escala corta, el proyecto revisa la combinación antes de seguir.

- **WORLD_TEXTURE.md** (coordinación operativa). La materia del mundo
  se nombra siguiendo la DOCTRINA DE PRIMACÍA NOMINAL Y VERBAL de este
  archivo: sustantivos concretos, verbos concretos, modificación
  parsimoniosa. La profusión adjetival que el régimen permita o no se
  cuantifica con CUOTA 1 modulada por AESTHETIC_REGISTER. La sección
  DENSIDAD PERMITIDA de WORLD_TEXTURE tiene subsección COORDINACIÓN
  OPERATIVA CON PROSE_LINE_DISCIPLINE que declara explícitamente el
  reparto: WORLD_TEXTURE controla cuánta materia entra (Capa 1); este
  archivo controla con qué anatomía gramatical se nombra (Capa 3).

- **SCENE_SHAPE.md** (modulación local por momento). La densidad por
  momento de la escena (entrada, presión, giro, salida) modula cuotas
  locales dentro del techo del régimen. Asignación específica: entrada
  cuotas estándar, presión atención a TIC 7 (mitigación), giro cuota
  local elevada admisible para TIC 1 y TIC 2 si la materia lo pide,
  salida disciplina estricta de TIC 4 y TIC 5. La regla preexistente
  de SCENE sobre cierre sobre gesto, sobre no-dicho, sobre imagen,
  sobre tiempo, sobre frase es coherente con cuota cero de TIC 4 y
  TIC 5.

- **SEAMS_AND_HINGES.md** (zonas de alta exposición a tics). Las
  juntas del texto (primera página, primer capítulo, último capítulo,
  última página, bisagras entre capítulos, transiciones entre POVs,
  paratextos) son zonas de alta exposición a TIC 4 (frase-resumen al
  cierre de párrafo), TIC 5 (cierre sentencioso de capítulo) y TIC 10
  (cadencia de opening commercial). Coordinación: la diagnosis
  estructural de las juntas reside en SEAMS; la cuantificación de los
  tics que las juntas activan reside aquí. La sección PARATEXTO
  (títulos de capítulo, epígrafes,
  dedicatorias, notas de autor, glosarios, mapas, índices) declara
  función de cada paratexto sin tocar cuotas, que se aplican igualmente
  a la prosa paratextual con disciplina que la del cuerpo principal.

- **CHAPTER_BRIEF.md** (declara cuotas vigentes por capítulo). El
  brief de cada capítulo declara cuotas vigentes por defecto
  (cuotas globales moduladas por régimen) y formaliza la sobreescritura
  local cuando aplica. Cuatro casos formalizados: capítulo estándar
  (cuotas globales sin sobreescritura, modulación por momento conforme
  a SCENE_SHAPE); capítulo de crisis de personaje (invoca REGLA DE
  EXCEPCIÓN POR ESTADO con anclaje obligatorio en CHARACTER_PHYSICS
  sección SÍNTOMAS VERBALES); sobreescritura por idiolecto de voz
  narrativa (declarada en VOICE_ARCHITECTURE sin redeclaración por
  capítulo); otros casos experimentales o de ruptura formal
  (declaración explícita y verificación de coherencia con
  AESTHETIC_REGISTER y VOICE_ARCHITECTURE).

- **REVISION_PROTOCOL.md** (invoca cuotas y tests en pasadas).
  PASADA 4 (trabajo de línea) invoca este archivo con énfasis en los
  tests cuantitativos. PASADA 1 (revisión por libro) verifica
  coherencia con régimen declarado. La sección FEEDBACK EXTERNO
  declara que el procesamiento de
  comentarios externos no contamina el manuscrito directamente; la
  pasada de prosa que reciba comentarios cruza con este archivo en
  PASADA 4 con cuotas vigentes según AESTHETIC_REGISTER.

### CONVENIENTE

Archivos cuyas operaciones pueden sostener prosa con cuotas modificadas
si las decisiones del proyecto lo justifican, o archivos que sugieren
regímenes característicos por convención.

- **THEMATIC_ENGINE.md** (motivos recurrentes y sistema de imágenes).
  La REGLA 3 de no-repetición léxica en párrafo de este archivo admite
  excepción cuando la repetición sea declarada como motivo recurrente
  en THEMATIC_ENGINE (caso de palabras-clave que sostienen el motor
  temático). La sección SISTEMA DE IMÁGENES introduce campos visuales sostenedores que pueden incluir
  léxico repetido legítimo. La declaración explícita en
  THEMATIC_ENGINE legitima la repetición; la repetición no declarada
  computa como tic.

- **GENRE_CONVENTIONS.md** (sugiere regímenes característicos por
  género). Cada género literario tiene convenciones de régimen estético
  que activan calibración directa o REGLA DE EXTRAPOLACIÓN según el
  régimen sugerido. Thriller comercial activa POPULAR-EFICIENTE
  (calibración directa en AESTHETIC_REGISTER); novela negra
  contemporánea activa POPULAR-EFICIENTE o INTERMEDIO según
  declaración del proyecto; ficción literaria contemporánea activa
  INTERMEDIO o EXPANSIVO según declaración; novela histórica naval
  activa NAVAL-DECIMONÓNICO. La modulación opera vía AESTHETIC_REGISTER,
  no directamente sobre este archivo.

### FLUJO OPERATIVO

Este archivo recibe modulación de los archivos críticos
(AESTHETIC_REGISTER régimen, VOICE_ARCHITECTURE idiolecto y tiempo
verbal, CHARACTER_PHYSICS estado de excepción), recibe densidad de
fondo de SCALE_CALIBRATION, recibe consigna por capítulo de
CHAPTER_BRIEF, opera en paralelo con los seis archivos de Capa 3
restantes (PROSODY, SEMANTIC, DIALOGUE, SENSORY, SUBTEXT, ELLIPSIS) en
reparto de jurisdicción declarado, recibe coordinación operativa de
WORLD_TEXTURE y SCENE_SHAPE, alimenta a SEAMS_AND_HINGES en zonas de
alta exposición, alimenta a REVISION_PROTOCOL en PASADA 4 (trabajo de
línea) y PASADA 1 (coherencia con régimen).

---

## ORIGEN HISTÓRICO

Este archivo formaliza una pieza que existió en versión anterior del
modelo agnóstico (v3, perdida sin backup) y cuya pérdida produjo
degradación detectable de la prosa generada con el modelo. Aquella
pieza investigaba el uso estadístico de los modificadores en autores
de calidad y forzaba al sistema a respetar cuotas matemáticas
estrictas. La presente versión reconstruye esa pieza con evidencia
empírica actualizada al estado del arte estilométrico y del
conocimiento sobre tics LLM contemporáneos. La reconstrucción no es
literal; es una segunda redacción que aprovecha lo aprendido en
v4-v6 sobre arquitectura del modelo agnóstico (jerarquía de capas,
modulación por régimen, no contaminación de plantillas) para
integrar la disciplina de línea en el sistema sin romper la
disciplina operativa del proyecto.

Si la práctica revela mejoras necesarias, se hacen conforme a
`LEEME.md` §4 (regla del fork) y llegan por el
PROTOCOLO_CAPTURA_APRENDIZAJE. Los valores de cada obra (cuotas
propias, listas propias, anclajes a sus autores) no se escriben aquí:
van a su preset (`PRESET_<OBRA>.md` › PROSE_LINE_DISCIPLINE).

Fin de PROSE_LINE_DISCIPLINE.md.


---
---

