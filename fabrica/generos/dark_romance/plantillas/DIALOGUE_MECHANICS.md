<!-- Fábrica v3.0 — plantilla de GÉNERO (vale para cualquier saga de dark romance). Los valores de la obra viven en su preset: PRESET_<OBRA>.md (la obra activa la dice el LEEME). Historia: convertida desde el modelo agnóstico v7 el 08-08-2026; separada de la obra el 22-10-2026; v2.0, la pareja primero (PAREJA_PRIMERO.md). -->

# DIALOGUE_MECHANICS.md — Fábrica v3.0

> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

## PROPÓSITO

El diálogo es donde la física de personaje, la física de relación
y el subtexto se vuelven performance. Es también donde los LLM
fallan más visiblemente: diálogos limpios pero inertes, ritmo
uniforme, personajes que suenan iguales, información en boca de
quien no hablaría así.

En el dark romance tiene además función de género: **la asimetría
entre los dos narradores es el motor de todos sus diálogos** (si la
obra tiene un solo narrador, la asimetría es la de la pareja en
diálogo). Mal calibrada, no es un defecto de línea: es una avería de
producto.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Los dos narradores.
> *Qué declara aquí la obra:* quiénes son sus narradores, si tiene dos: por defecto, protagonista A, la voz que habla, y el narrador hermético (protagonista B), si lo hay; o, con uno solo, quién narra.

Este archivo es el manual de operación para generar diálogo vivo.

JERARQUÍA: Capa 3 principalmente, con dependencias Capa 1-2.

---

## PRINCIPIO FUNDACIONAL

Los personajes no hablan para informar a la lectora. Hablan para
conseguir algo del otro, evitar decir algo, averiguar, defenderse,
imponerse o alterar el vector relacional.

Si alguien dice algo sobre todo porque la lectora necesita
saberlo, es exposición disfrazada, y se nota aunque no se nombre.

TEST INMEDIATO: para cada turno, ¿qué quiere el personaje al decir
esto? Si la respuesta es "informar", reescribir o eliminar.

### LOS TRES CAMPOS DEL GÉNERO

Todo turno relevante cae en uno de tres campos; el que no cae en
ninguno se corta.

**(a) Duelo de la pareja.** Ella habla para acercarse sin admitirlo,
provocarlo o arrancarle algo; él, para cerrar, ordenar o negarse.
**(b) Interrogatorio y evasión.** Uno pregunta para destapar, otro
responde para ocultar.
**(c) Roce de elenco.** Caracteriza, alivia o presiona; nunca
explica la trama del libro.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Los tres campos.
> *Qué declara aquí la obra:* quién ocupa cada campo (la pareja del duelo, qué voces se interrogan entre sí y qué personajes del elenco fijo forman el roce).

#### Variante: dark romance policial

**Prohibido el cuarto campo:** la exposición procedimental en boca
de personaje. Si el dato es imprescindible, entra por narración
breve o por INFORMATION_CHOREOGRAPHY, no por diálogo.

---

## LA ASIMETRÍA ENTRE LOS DOS NARRADORES (regla dura del género)

Es el eje que organiza todo lo demás de este archivo, que la da en
su forma por defecto: él, hermético. Si la obra no lo declara
hermético, declara aquí la asimetría de su pareja, y las reglas del
narrador hermético se leen con la que declare.

**Ella (protagonista A):** *[su registro: velocidad y tono, longitud
de turno, sintaxis, y qué función cumple su forma de hablar].*
**Él (el narrador hermético):** *[su economía: tipo de frase, tono y
longitud de turno].*
**El choque:** el registro de ella **rebota** contra él. Cuando él
por fin habla —o da una orden en voz baja— tiene el doble de
impacto porque ha callado antes.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › La asimetría de la pareja.
> *Qué declara aquí la obra:* la ficha rellena de los dos registros, la proporción del choque entre ambos y una muestra de calibración correcta.

**REGLA DE CUOTA IMPLÍCITA.** El narrador hermético no explica lo
que siente. Si articula un sentimiento, esa línea es **un beat de
rendición pactado**. Fuera de esos puntos, lo que siente se lee en
lo que hace, en lo que ordena y en lo que calla. Autoridad:
ROMANCE_BEAT_MAP.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Beats de rendición pactados.
> *Qué declara aquí la obra:* en qué libro cae cada beat de rendición y qué sentimiento puede articular en él el narrador hermético, si lo hay (o el protagonista que raciona su rendición, si la obra declara otro).

**REGLA DE NOMBRE** (si la obra reserva un apelativo o retiene un
nombre).

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Regla de nombre.
> *Qué declara aquí la obra:* si los tiene, qué apelativo sale de una sola boca y qué nombre se retiene hasta un beat de rendición (quién puede decirlo, desde cuándo y qué efecto tiene en la escena).

**Diagnóstico rápido:** si en una página el narrador hermético
habla tanto como protagonista A, o si sus turnos llevan
subordinadas, el diálogo está roto aunque suene bien.

---

## CADENCIA (ritmo del intercambio)

El diálogo tiene ritmo como la música. Alternar longitudes es
esencial.

### TURNOS LARGOS
Cuando alguien monopoliza, hay razón. Aquí el turno largo es de
**protagonista A** o de **quien se delata por exceso**
(*Variante: dark romance policial:* el sospechoso). Riesgo: que se
vuelva ensayo del autor o resumen de la trama del libro. Medida:
menos de lo que parece necesario.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Cadencia.
> *Qué declara aquí la obra:* qué otras voces tienen derecho al turno largo y con qué función.

### TURNOS CORTOS
La mayoría. Dos líneas, una línea, una palabra, un gesto como
respuesta. Registro base de **todo** lo que dice el narrador
hermético.

### MONOSÍLABOS Y SILENCIO
El "sí", el "no", el silencio declarado son turnos completos y
pueden ser los más cargados de la escena. **El silencio del
narrador hermético es una réplica, no una ausencia de réplica.** Se
acota como turno propio: lo que hace mientras no contesta es la
respuesta.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Cadencia.
> *Qué declara aquí la obra:* una muestra del silencio del narrador hermético acotado como turno, si lo hay.

### ALTERNANCIA
Tres o cuatro pulsos distintos por página: turno largo, respuesta
corta, intervención lateral, silencio. La monotonía es síntoma de
diálogo infraescrito. Patrón canónico del duelo: **largo /
cortísimo / silencio / orden en voz baja**.

---

## ATRIBUCIÓN (verbos dicendi)

### REGLA BASE
"Dice" es invisible y funciona casi siempre. Los sinónimos
("exclama", "musita", "espeta") llaman la atención sobre sí
mismos: solo cuando su precisión semántica sea necesaria.

### ATRIBUCIÓN POR GESTO
El gesto atribuye y añade información. **Opción por defecto del
género**: el narrador hermético tiene pocas palabras, así que su
turno se carga desde el cuerpo. Una sola cláusula. El gesto puede
valer además como pista y contabilizarse en CLUE_LEDGER.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Atribución.
> *Qué declara aquí la obra:* una muestra de atribución por gesto del narrador hermético, si lo hay (si no, de la voz más económica), con un objeto de su mundo.

### MECÁNICA ESPAÑOLA
Raya al inicio de línea; raya de cierre solo si sigue atribución
(ejemplo: "—Esta noche no —dice." / "—Esta noche no."). La
atribución va pospuesta: "—Esta noche no —dice, y le quita las
llaves"; la inversa suena desusual. Cuando dos personajes alternan con
claridad, se puede prescindir de atribución varios turnos: si se
pierde la cuenta, restablecer.

**Tiempo verbal:** el que fija la obra, sin excepción, también en
la acotación. Una acotación en otro tiempo es error de régimen, no
de estilo. Autoridad: VOICE_ARCHITECTURE.

### ADVERBIOS EN ATRIBUCIÓN
"Dice con tristeza", "responde alegremente": salvo excepciones,
indicio de que la emoción no está en el diálogo y se compensa
desde fuera. Reescribir para que se infiera, no que se declare.

**Endurecimiento del género (comprobación de cierre):** en la
atribución del narrador hermético y en la de cualquier
interrogatorio, el adverbio en -mente se busca en el cierre
(OPERACIÓN C) y se corta. En él el adverbio es doble redundancia:
rompe su economía y pone en el narrador la explicación que el
personaje se niega a dar.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Atribución.
> *Qué declara aquí la obra:* los marcadores de atribución que bastan para la voz del narrador hermético, si lo hay.

Este criterio se respalda en PROSE_LINE_DISCIPLINE.md con CUOTA 2
(-mente, donde computan los de atribución) y TIC 7 (dicendi con
mitigador: "dice, casi sin voz").

---

## IDIOLECTO

Cada voz diferenciada tiene marcadores verbales propios: es lo que
permite reconocer quién habla sin atribución.

**Componentes:** léxico preferido (técnico, regional, muletilla);
sintaxis característica (completa o elíptica, subordinación o
parataxis); **lo que nunca dice** —la veda genera más identidad
que el rasgo positivo—; muletillas (dos o tres como máximo) y
ritmo de habla (longitud media del turno).

### FICHAS DE IDIOLECTO DEL CANON

| Voz | Sintaxis y léxico | Lo que nunca dice |
|---|---|---|
| **Protagonista A** | | |
| **Narrador hermético** | | |
| **[Cada voz del elenco fijo]** | | |

*Una fila por voz diferenciada: las dos de la pareja y cada voz del
elenco fijo. «Sintaxis y léxico»: los componentes de arriba en una
línea. «Lo que nunca dice»: su veda.*

Anclajes que no son estilo, sino canon:

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Idiolecto.
> *Qué declara aquí la obra:* la ficha rellena de cada voz y los anclajes de canon que fija entre voces concretas (entre ellos, lo que uno nunca le pide al otro, si la obra lo declara).

### HOMOGENEIDAD SOSPECHOSA
Si todos hablan con el mismo léxico, sintaxis y longitud de frase,
es el autor hablando por ellos. TEST: quitar atribuciones en una
página de dos personajes. Con la pareja debe resolverse **a
ciegas y de inmediato**; si hace falta la acotación, la asimetría
se ha perdido.

### IDIOLECTO COMO SOBREESCRITURA DE CUOTAS GLOBALES
El idiolecto declarado aquí (o en VOICE_ARCHITECTURE.md cuando la
voz es narrativa) sobreescribe localmente las cuotas de
PROSE_LINE_DISCIPLINE.md. **Lo declarado no computa:** no entra en
CUOTA 2 (-mente), CUOTA 3 (hedge-adverbs) ni TIC 1 (ternario)
mientras viva en boca del personaje; sí entra si se filtra al
narrador fuera del indirecto libre. Sin declaración es tic del
modelo; con declaración, caracterización.

---

## ASIMETRÍA DIALÓGICA

En cualquier conversación uno tiene más información, deseo,
pérdida potencial o poder. Esto se codifica en cuatro palancas.

### DISTRIBUCIÓN DE TURNOS
Quien tiene más poder o información habla menos; quien pide o se
defiende habla más. El narrador hermético es el caso puro.
**Inversión en interrogatorio:** el interrogado que más tiene que
perder habla **más**, por nervio o despiste. Es la delación por
exceso.

### QUIÉN PREGUNTA / QUIÉN RESPONDE
Quien pregunta está arriba, aun desde posición aparente inferior.
Protagonista A pregunta casi siempre; con el narrador hermético
pregunta y no obtiene, y esa frustración es el combustible.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Asimetría dialógica.
> *Qué declara aquí la obra:* de dónde saca su ventaja el narrador hermético, si lo hay (o quién la tiene en la pareja), y con qué voz se invierte la mesa y es protagonista A quien responde.

### QUIÉN CIERRA
Quien dice la última palabra queda con el peso dramático. Con el
narrador hermético **cierra él**: ella se queda la réplica en la
boca, y esa réplica no dicha es la tensión.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Asimetría dialógica.
> *Qué declara aquí la obra:* con cuántas palabras como máximo cierra el narrador hermético, si lo hay, y quién cierra con cada voz del elenco que se enfrenta a protagonista A.

### QUIÉN IGNORA
Ignorar una pregunta es un movimiento de poder fuerte. El narrador
hermético lo hace de forma sistemática, con dos usos que no se
confunden: **por control** (no contesta y cambia de tarea) y **por
rendición** (no contesta porque contestar lo entregaría; se marca
desde el POV de ella, con el cambio de su mirada, nunca desde el
de él).

### LA ORDEN EN VOZ BAJA (recurso erótico)
Herramienta central del género. El narrador hermético baja el
volumen en vez de subirlo: la orden en voz baja **es caricia y
amenaza a la vez**, y su potencia depende de la economía previa
—solo pesa si lleva media escena callado—.

—Quieta.
—No estoy haciendo nada.
—Ya lo sé. Quieta.

Uso: peligro real, cura, cama y, si la pareja lo tiene, combate
cuerpo a cuerpo. Pocas por libro, nunca dos en la misma escena. La reacción se narra
desde el cuerpo de ella, no desde la intención de él.
Autoridades: HEAT_DISCIPLINE y RELATIONSHIP_PHYSICS, donde vive la
asimetría primaria del vector que aquí se pone en escena.

---

## INTERRUPCIÓN Y SOLAPAMIENTO

El habla real no respeta turnos puros: los diálogos donde cada uno
termina antes de que el otro empiece son artificiales.

### INTERRUPCIÓN LIMPIA
*Ejemplo:*
—Puedo arreglarlo yo, solo necesito una hora y que nadie—
—No.

La raya como marca de corte. Uso canónico del género: el
monosílabo del narrador hermético cortando el turno largo de
protagonista A. Variante por gesto (ejemplo): "—Puedo arreglarlo
yo, solo necesito una hora y— Él apaga la luz."

### SOLAPAMIENTO Y USO
No caben dos voces a la vez, pero puede indicarse ("hablan los dos
a la vez"). La interrupción es un recurso: usada cada página,
pierde. Reservar para donde la asimetría se activa o se quiebra.

### LA INTERRUPCIÓN COMO *EDGING*
El corte externo también es tensión: la llamada que interrumpe
(*Variante: dark romance policial:* la de la comisaría) cuando la
escena iba a consumarse, el aviso de un aliado, el mensaje de un
tercero en el peor momento. Se explota mientras dura el *edging*
que declara la obra y después solo cuando el corte cuesta algo.
Autoridad: HEAT_DISCIPLINE (CUÁNDO SE CORTA: el *edging* dura un
tramo, no un libro).

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Interrupción y solapamiento.
> *Qué declara aquí la obra:* quién corta desde fuera (quién avisa, quién escribe en el peor momento), cuánto dura su *edging* y su muestra de corte por gesto.

---

## LO NO DICHO EN EL DIÁLOGO (subtexto activo)

Lo más importante del diálogo es con frecuencia lo que no se dice.
SUBTEXT_MECHANICS.md lo cubre a fondo; aquí, los mecanismos.

### CAMBIO DE TEMA
No se responde a lo que se pregunta; se habla de otra cosa. Se
siente el salto y no se explica.

Sostiene los relojes de la saga, si los tiene: el secreto horizontal
que declare la obra se administra en buena parte por temas
esquivados de quien lo guarda.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Lo no dicho en el diálogo.
> *Qué declara aquí la obra:* una muestra de cambio de tema y, si la saga tiene trama horizontal, qué secreto de ella se administra así y quién lo guarda.

### EXCESO Y DEFECTO
Hablar mucho para no decir lo importante marca al interrogado
nervioso, y marca a protagonista A cuando la ponen contra la
cuerda. El monosílabo donde se esperaba explicación es delación
—salvo en el narrador hermético, que es su registro base: con él
la delación se invierte, y una palabra de más significa que ha
perdido pie—.

### EL GESTO DESLIZADO
Línea neutra, gesto significativo. La incongruencia es el
subtexto.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Lo no dicho en el diálogo.
> *Qué declara aquí la obra:* una muestra de gesto deslizado del narrador hermético, si lo hay (si no, de cada voz de la pareja).

En el duelo el gesto delata deseo o posesión; en interrogatorio,
culpa o miedo. No se mezclan en el mismo gesto: contamina
registros y desactiva la pista.

### LA MARCA DE VULNERABILIDAD
Si la obra le da una (un gesto reservado), la marca de protagonista
A **nunca es decorativa**: la armadura ha caído y su réplica va a
fallar en el turno siguiente. Si la escena no necesita esa caída,
la marca no aparece. Autoridad: CHARACTER_PHYSICS.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Lo no dicho en el diálogo.
> *Qué declara aquí la obra:* qué gesto físico de protagonista A es su marca de vulnerabilidad, si la tiene.

### PROHIBICIÓN
El subtexto no se nombra: se construye con síntomas. Refuerzo del
género: ni el deseo ni la sospecha se nombran dentro del diálogo,
y **el cambio de mirada del narrador hermético se describe siempre
desde el POV de protagonista A**, ni siquiera en capítulos de él.

---

## DIÁLOGO Y REGISTRO (por AESTHETIC_REGISTER.md)

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Diálogo y registro.
> *Qué declara aquí la obra:* su régimen y la longitud de capítulo, y la modulación de registro admitida en cada voz que no es el narrador hermético (en todas, si no lo hay).

Turnos breves, atribución escasa, tres o cuatro pulsos por página,
capítulos que no admiten diálogo moroso.

**Vetados** el barroco y el expansivo: en boca del narrador
hermético lo destruyen. Oral y periodístico, solo como color local
en secundarios de la trama del libro.

**Modulación admitida:** minimalista puro con el narrador
hermético.

---

## EL INTERROGATORIO COMO SEDUCCIÓN TÁCTICA

### Variante: dark romance policial

Escena opcional: si la obra la declara, es escena canónica del
subgénero, y la más fácil de estropear.

**Qué hace quien interroga** (protagonista A por defecto; lo
declara la obra). Con el oficio que le declare la obra, se mete en
la cabeza del interrogado: le ofrece un espejo, se muestra
vulnerable de forma calculada y le hace creer que tiene una
oportunidad. Se nota que es una técnica para todos menos para él.

**Reglas duras:**
- **Frío y calculado. Cero roce físico innecesario.** La seducción
  es psicológica o no es.
- **No siente nada por el interrogado.**
- El interrogado **no asciende jamás** a interés romántico.
- La vulnerabilidad exhibida es real en su material y falsa en su
  propósito. Esa mezcla es lo que funciona.
- **Nunca es escena limpia:** el otro de la pareja está en ella, en
  directo o ocupando a quien narra. Su reacción —celos, orden
  posterior en voz baja, desaparición— es la otra mitad de la
  escena (en el cierre, TEST 12).

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › El interrogatorio como seducción táctica.
> *Qué declara aquí la obra:* si tiene esta escena, quién interroga y con qué oficio, cómo está el otro de la pareja en ella y una muestra de la mecánica en su voz, con hueco de instancia; o «no aplica».

---

## DIÁLOGO DURANTE EL SEXO

Permitido y esperado. Sin elipsis por pudor, sin eufemismo
anatómico, sin metáfora floral. Autoridades: HEAT_DISCIPLINE y
ELLIPSIS_PROTOCOL.

- La asimetría se mantiene: **ella habla, él ordena.** El narrador
  hermético, imperativos cortos en voz baja; protagonista A,
  desafío en su registro, que se le va rompiendo, y después ya no.
- Vocabulario directo. Si una palabra suena a manual médico o a
  poema, está mal elegida.
- **El apelativo reservado**, si la obra lo tiene, cambia la
  temperatura de la escena entera. **El nombre retenido**, si lo
  tiene, no antes de su beat.
- **Prohibido el discurso sentimental.** El narrador hermético
  tampoco se explica en la cama: dice lo que quiere y lo que va a
  hacer.
- Se admite el conflicto durante el acto —reproches, la trama del
  libro metida en la cama—. Es campo de batalla, no tregua.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Diálogo durante el sexo.
> *Qué declara aquí la obra:* cómo se le rompe en la cama el registro a protagonista A y, si los tiene, qué apelativo y qué nombre cambian la temperatura de la escena.

---

## GESTIÓN DE INFORMACIÓN EN DIÁLOGO

El diálogo es mal canal para información neutra: dos personajes
diciéndose cosas que ambos ya saben.

### SOLUCIONES
- **Un tercero que no sabe.** Un recién llegado es el canal
  legítimo. Dos o tres veces por libro.
- **Conflicto sobre la información.** Los dos saben lo que uno de
  ellos ha hecho; el otro se lo echa en cara. El conflicto justifica
  la repetición y lo convierte en escena de pareja.
- **Por fragmentos.** Régimen obligatorio de la trama horizontal,
  si la saga la tiene: el secreto horizontal que declare la obra se
  entrega por capas a quien no lo sabe.
- **Por omisión.** Un personaje suelta un dato y calla el que
  importa.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Gestión de información en diálogo.
> *Qué declara aquí la obra:* quién hace de tercero que no sabe, qué secreto de la trama horizontal se entrega por capas, quién lo guarda y en qué libros (si la saga la tiene), y quién informa por omisión.

### LO QUE NO FUNCIONA

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Gestión de información en diálogo.
> *Qué declara aquí la obra:* un contraejemplo de diálogo «como sabes» con datos de su propio mundo.

### PROHIBICIÓN DE EXPOSICIÓN PROCEDIMENTAL

#### Variante: dark romance policial

Regla dura, no preferencia estilística. Fuera del diálogo: el
forense explicando dos páginas, la reunión de coordinación, la
balística detallada, la cadena de custodia, la jerga sin función
dramática.

Si el dato es imprescindible para la lectora, va en narración
breve desde el POV; si solo lo es para el autor, se corta. El que
sobreviva entra **cargado de tensión con el narrador hermético**,
o no entra.

---

## DIÁLOGO DE GRUPO (tres o más personajes)

No todos hablan en todos los turnos: quien calla existe, y se
registra qué hace. Las alianzas se ven. Si hay cinco personas, dos
o tres importan.

*Variante: dark romance policial.* **Advertencia de género.** Es la
puerta por la que se cuela la coralidad de comisaría, prohibida: el
equipo no es protagonista colectivo. Techo: tres voces activas. Si
alguno de la pareja tiene equipo institucional (lo declara la obra),
su sala es escenario de presión sobre él o ella —lo que no puede
decir delante de su equipo y de sus mandos—, nunca mesa de puesta
en común del caso.

**Si la obra lo declara, el narrador hermético no participa en
diálogos de grupo:** su registro es de dos personas; si hay una
tercera, calla. Esta regla no lo saca nunca de la escena.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Diálogo de grupo.
> *Qué declara aquí la obra:* qué alianzas se ven en sus escenas de grupo; si alguno de la pareja tiene equipo institucional, quién, en qué sala y delante de quién calla; y si su narrador hermético, si lo hay, entra en ellas.

---

## ERRORES FRECUENTES

### ERROR 1 — TODO EL MUNDO ES ELOCUENTE
Repartir elocuencia según carácter.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Errores frecuentes.
> *Qué declara aquí la obra:* qué voces tienen la elocuencia, y ninguna más.

### ERROR 2 — CERO RESISTENCIA
Error capital del género en interrogatorio: nadie contesta entero
a la primera pregunta relevante. Desvío, evasión parcial o mentira
por omisión.

### ERROR 3 — DIÁLOGO-EXPLICACIÓN
Un personaje explica al otro qué siente y por qué; si estuviera
ahí, no lo necesitaría. **En el narrador hermético es terminal**:
cada sentimiento verbalizado fuera de los beats pactados lo
blanquea y deja de ser el producto.

### ERROR 4 — NUNCA SE INTERRUMPEN
Todos terminan sus frases. Sospechoso.

### ERROR 5 — ATRIBUCIÓN EXCESIVA
"—...—dice él" en cada turno. Confiar en que la lectora sigue.

### ERROR 6 — PROTAGONISTA A PIDE
*Si la obra declara negación plausible (ELLIPSIS_PROTOCOL, USO A).*
Una petición explícita de quien la necesita a quien actúa por ella
rompe la negación plausible. Lo que se dice en su lugar, si algo,
lo declara la obra (DIALOGUE_MECHANICS › Idiolecto).

### ERROR 7 — SIMETRÍA DE VOLUMEN
El narrador hermético contesta con tantas palabras como recibe.
Fallo por defecto del modelo, invisible línea a línea: solo se ve
contando.

---

## EL DIÁLOGO COMO GANCHO DE CAPÍTULO

Los capítulos cierran en gancho **sin excepción**, y la última
línea de diálogo es la herramienta más eficaz. **El gancho
emocional vale más que el de trama:** una frase del narrador
hermético pesa más que un hallazgo de la trama, porque la lectora
ha venido por él.

Cierres canónicos: **la orden en voz baja** sin respuesta de ella;
**la pregunta que él no contesta**, con el silencio acotado como
turno; **la miga**, si la saga tiene trama horizontal: una frase
que revela que quien guarda el secreto horizontal que declare la
obra sabe algo de esa trama que el otro no sabe.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › El diálogo como gancho de capítulo.
> *Qué declara aquí la obra:* cuántos capítulos tiene cada libro y, si la saga tiene trama horizontal, qué secreto de ella alimenta la miga y quién lo guarda.

Prohibido cerrar en resolución cálida o en línea que desactive la
tensión. Autoridad: SEAMS_AND_HINGES.

---

## PROTOCOLO DE CIERRE DEL DIÁLOGO (el antiguo «pre-escritura»)

En el cierre (OPERACIÓN C), de cada escena con diálogo ya escrita:

1. ¿Qué quiere cada uno al entrar y qué no puede decir?
2. ¿Qué asimetría está activa? (RELATIONSHIP_PHYSICS)
3. ¿Qué tiene que haber cambiado al salir?
4. ¿Qué idiolecto aplica a cada voz?
5. Si está el narrador hermético: ¿cuántas palabras dirá, y cuál
   es la única que importa? Si no está: ¿dónde está su sombra?
6. ¿Con qué línea cierra el capítulo?

La que no tiene respuesta en la escena escrita delata diálogo
intercambiable: va al acta.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Protocolo pre-escritura.
> *Qué declara aquí la obra:* la pregunta 5 dicha con el nombre de su narrador hermético, si lo hay (si no, del protagonista B).

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — ASIMETRÍA (el principal)
Contar palabras de protagonista A y del narrador hermético en una
escena compartida. Si él llega al umbral que fija la obra, el motor
está roto. ¿Alguna frase del narrador hermético lleva subordinada?

TEST 2 — CUOTA IMPLÍCITA
Contar las veces que el narrador hermético nombra o explica un
sentimiento. ¿Coinciden con los beats de rendición pactados para
ese libro? Cualquier línea de más: revertir a acto, orden o
silencio.

TEST 3 — IDENTIFICACIÓN SIN ATRIBUCIÓN
Cubrir atribuciones. ¿Se identifica quién habla? Con la pareja,
instantáneo.

TEST 4 — NOMBRES (si la obra reserva un apelativo o retiene un nombre)
¿Ha dicho el apelativo reservado alguien que no sea su dueño?
¿Aparece el nombre retenido antes de su beat? Error de canon, no
de estilo.

TEST 5 — INTENCIÓN Y RITMO
Cinco turnos al azar: ¿qué quería cada uno? ¿Hay alternancia de
longitudes y patrón de duelo (largo / cortísimo / silencio / orden
en voz baja)?

TEST 6 — EXPOSICIÓN PROCEDIMENTAL
*Variante: dark romance policial.* El turno más largo del libro que
no sea de protagonista A, de otra voz con turno largo declarado o de
un sospechoso: si es el forense explicando una autopsia o alguien
coordinando una reunión, se ha escrito novela negra.

TEST 7 — RESISTENCIA Y TÁCTICA
¿Alguien contesta entero a la primera pregunta relevante?
*Variante: dark romance policial, si la obra tiene la seducción
táctica:* con el interrogado, ¿acercamiento frío y sin roce
innecesario? ¿Está el otro de la pareja en la escena?

TEST 8 — IMPUNIDAD
*Si la obra declara negación plausible (ELLIPSIS_PROTOCOL, USO A).*
Buscar peticiones explícitas de quien la necesita a quien actúa por
ella. Una sola la rompe.

TEST 9 — EXPLICITUD
En el sexo: ¿eufemismo, metáfora floral o corte por pudor? ¿Se
mantiene la asimetría —ella habla, él ordena—?

TEST 10 — SUBTEXTO Y MIRADA
¿Se percibe lo no dicho? ¿El cambio de mirada del narrador
hermético se lee siempre desde el POV de protagonista A?

TEST 11 — GANCHO DE PAREJA *(v2.0)*
Todos los cierres de capítulo, con línea de diálogo o sin ella:
¿cuántos son de pareja, por bloque de cuatro capítulos y por libro?
Cuenta también el gancho de la trama B que cae sobre la pareja
(sobre los dos, o sobre uno por el otro). Por libro, objetivo tres
de cada cuatro y suelo dos de cada tres; por bloque, objetivo tres
de cuatro y suelo dos de cuatro (`PAREJA_PRIMERO.md`, §3). Por
debajo del suelo, el libro se desliza hacia el género secundario:
alarma en el acta (C-7), que avisa a la escaleta del bloque
siguiente.

TEST 12 — SU SOMBRA EN LA PÁGINA DE ELLA *(v2.0)*
La pregunta 5 del protocolo, hecha en el cierre: en un capítulo de
protagonista A, en las escenas sin el narrador hermético, ¿dónde
está su sombra? ¿Queda en la página de ella algún rastro de él (lo
que ella piensa o teme de él, un mensaje, lo que se calla por él)?
*Si la obra tiene la seducción táctica:* ¿la reacción del otro de la
pareja deja rastro en la página de quien interroga o solo en el
capítulo del otro? Si no hay rastro, se anota en el acta como alarma
de C-10 (no obliga a añadir).

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Tests de funcionamiento.
> *Qué declara aquí la obra:* el umbral de palabras del TEST 1, los nombres del TEST 4, si los tiene, qué voces cuentan con turno largo en el TEST 6 y, si los tiene, qué rastro del otro (mensajes, vigilancia, lo que se calla) busca el TEST 12.

---

## RELACIÓN CON OTROS ARCHIVOS

Recibe de:
- GENRE_CONVENTIONS.md (contrato de género: escena limpia
  prohibida, gancho obligatorio, explicitud plena)
- CHARACTER_PHYSICS.md (canon de la pareja y del elenco fijo)
- RELATIONSHIP_PHYSICS.md (vector y asimetría del duelo)
- ROMANCE_BEAT_MAP.md (escala de rendición: qué puede decir el
  narrador hermético en cada libro y, si la obra retiene un nombre,
  cuándo se entrega)
- VOICE_ARCHITECTURE.md (POV, persona y tiempo que fija la obra)
- AESTHETIC_REGISTER.md (registro admisible)
- SUBTEXT_MECHANICS.md (lo no dicho)
- PROSODY_AND_MUSIC.md (cadencia del intercambio)
- PROSE_LINE_DISCIPLINE.md (cuotas globales sobre las que el
  idiolecto declarado aquí ejerce sobreescritura local)

Alimenta:
- El cierre (OPERACIÓN C) de toda escena con diálogo
- SCENE_SHAPE.md (escena principalmente dialogal)
- HEAT_DISCIPLINE.md (diálogo explícito y orden en voz baja)
- SEAMS_AND_HINGES.md (última línea como gancho, emocional
  preferente)
- CLUE_LEDGER.md (pistas en cambio de tema, monosílabo y gesto
  deslizado; migas en boca del narrador hermético)
- INFORMATION_CHOREOGRAPHY.md (dato de la trama del libro desviado
  del diálogo)

Se verifica en OPERACIÓN C y en la PASADA 4 de REVISION_PROTOCOL,
con los tests de asimetría y cuota implícita como auditoría de
género, no solo de estilo.

> **Valores de la obra →** `PRESET_<OBRA>.md` › DIALOGUE_MECHANICS › Relación con otros archivos.
> *Qué declara aquí la obra:* las mismas dependencias dichas con los nombres de su pareja y, si lo tiene, de su nombre retenido.
