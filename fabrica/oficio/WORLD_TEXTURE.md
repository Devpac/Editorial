<!-- Fábrica v3.0 — WORLD_TEXTURE: base de oficio + adenda de dark romance (v2.0) -->

# WORLD_TEXTURE.md

## PROPÓSITO

Este archivo regula cómo el mundo físico, histórico o técnico entra
en la prosa: qué detalle en qué escena, cuándo el léxico especializado
inmersa y cuándo expulsa, cómo distribuir la información de mundo
sin romper el punto de vista.

El riesgo en novela histórica, naval, colonial, científica o fantástica
no es la falta de datos: es el infodump y la erudición como estorbo.
Este archivo es el filtro anti-infodump y el motor de inmersión.

JERARQUÍA: Capa 1 (decisión de diseño que condiciona ejecución de
prosa en Capa 3).
Subordinado a AESTHETIC_REGISTER.md (que define densidad permitida)
y a VOICE_ARCHITECTURE.md (que define qué puede saber el narrador).

---

## CATÁLOGO DE TEXTURA

El mundo se compone de capas. Cada una tiene su propia economía.

### CAPA 1 — MATERIAL
Objetos, sustancias, texturas, herramientas. Lo que se toca.
Ejemplo naval: cabo alquitranado, cabilla de cornamusa, mascarón,
brea, salitre en la madera.

### CAPA 2 — GESTUAL
Acciones especializadas, protocolos, secuencias. Lo que se hace
y cómo.
Ejemplo naval: el orden de las órdenes en una maniobra de viraje,
el protocolo de recibir a un oficial superior, cómo se amarra
un cabo frente a otro.

### CAPA 3 — LÉXICA
Vocabulario especializado. Lo que se nombra con nombres propios
del oficio o el período.
Ejemplo naval: estribor, portalón, obenques, driza, singladura.

### CAPA 4 — INSTITUCIONAL
Jerarquías, leyes, costumbres, economía del mundo.
Ejemplo naval: el Articles of War, los grados de oficial,
el sistema de botín, la economía del puerto.

### CAPA 5 — CULTURAL / MENTAL
Cosmovisión, supersticiones, expectativas morales, horizonte de
lo pensable en ese mundo.
Ejemplo naval: la idea del honor como capital simbólico,
el lugar de Dios en la cubierta, la actitud hacia la muerte
en combate.

---

## PRINCIPIO DE ANCLAJE

Toda textura entra por ANCLAJE: se ancla en lo que el personaje
está haciendo, viendo o necesitando en este momento.

PROHIBIDO: "En aquella época los barcos tenían...". Esto es
narrador-erudito hablando por encima del personaje, rompiendo
el punto de vista y anunciando que el autor ha investigado.

PERMITIDO: "La driza se le resbaló de las manos; llevaba dos días
sin brea y el cáñamo seco no aguantaba el tirón." Aquí la textura
sirve a la acción; la información llega por necesidad, no por
demostración.

TEST DE ANCLAJE:
¿Por qué este detalle, aquí? Si la respuesta es "para que el lector
sepa cómo era", reescribir. Si la respuesta es "porque el personaje
necesita hacer X y este detalle es la fricción de X", permitido.

---

## DENSIDAD PERMITIDA (según AESTHETIC_REGISTER.md)

### RÉGIMEN MINIMALISTA
Textura muy escasa. Preferencia por el detalle único revelador.
Un objeto bien elegido hace el trabajo de diez.

### RÉGIMEN EXPANSIVO
Textura abundante, pero filtrada por la conciencia del narrador.
Lo que se describe revela tanto de quien mira como de lo mirado.

### RÉGIMEN NAVAL-DECIMONÓNICO
Textura alta. Inmersión por saturación controlada. El lector debe
sentir que el narrador habita el mundo. Protocolo y léxico forman
parte del texto, no son paratexto. La ignorancia del lector es
confianza en el autor: el detalle no se explica, se practica.

### RÉGIMEN BARROCO
Textura máxima, con licencia para el detalle sin función aparente
inmediata. La saturación es el método.

### RÉGIMEN PERIODÍSTICO
Textura selecta y precisa. Cada detalle debe ser el detalle,
no un detalle.

### COORDINACIÓN OPERATIVA CON PROSE_LINE_DISCIPLINE

La densidad permitida declarada en cada régimen es la decisión
de Capa 1: cuánta materia del mundo entra en escena. La forma
gramatical concreta con que esa materia se nombra está regulada
por PROSE_LINE_DISCIPLINE.md desde Capa 3.

La materia del mundo se nombra con sustantivo concreto (driza,
brea, cabilla, salitre) y verbo concreto (resbaló, mordía,
empapaba), siguiendo la DOCTRINA DE PRIMACÍA NOMINAL Y VERBAL
de aquel archivo. La profusión adjetival que el régimen permita
o no se cuantifica con la CUOTA 1 — ADJETIVOS CALIFICATIVOS
modulada por el régimen declarado en AESTHETIC_REGISTER:
minimalista admite techo bajo de adjetivos sobre la textura,
expansivo y barroco admiten techos altos, naval-decimonónico se
beneficia de adjetivación funcional sobre la materia técnica.

La coordinación opera en una dirección: WORLD_TEXTURE declara
qué materia entra y con qué densidad de fondo; PROSE_LINE_DISCIPLINE
disciplina cómo se nombra esa materia en la línea concreta, con
qué cuotas de adjetivos, qué primacía nominal-verbal y qué tics
LLM se evitan. Si el detalle revelador se construye con
acumulación adjetival ("una luz suave, dorada, casi quieta") en
lugar de con sustantivo y verbo concretos ("el sol entraba
oblicuo entre las persianas"), la prosa cumple WORLD_TEXTURE en
densidad pero falla PROSE_LINE_DISCIPLINE en anatomía: el
detalle es decorativo aunque la cuota de detalles esté
respetada. La coordinación entre ambos archivos cierra ese
hueco.

---

## GLOSARIO TÉCNICO (tres estrategias)

Cuando el mundo requiere léxico especializado denso, tres
estrategias posibles. Declarar cuál se adopta.

### ESTRATEGIA 1 — INMERSIÓN SIN CONCESIONES
No se glosa nada. El léxico se usa como si el lector lo supiera.
El lector aprende por contexto y repetición.
Efecto: confianza y exigencia.
Riesgo: expulsión del lector casual.
Referentes: Cormac McCarthy en Blood Meridian con el léxico
árido del suroeste.

### ESTRATEGIA 2 — GLOSA INTRADIEGÉTICA
Un personaje explica a otro, o el propio personaje reflexiona.
La glosa nunca viene del narrador omnisciente.
Efecto: naturalidad, riesgo bajo de expulsión.
Riesgo: acartonamiento si se abusa (los personajes explican lo
que ya saben).
Referentes: O'Brian con Stephen Maturin como novato a bordo.

### ESTRATEGIA 3 — GLOSARIO EXTERNO
Apéndice al final. El texto no concede nada; el lector consulta
si quiere.
Efecto: máxima integridad del texto.
Riesgo: fricción de lectura.
Referentes: varios clásicos de ciencia ficción, Tolkien.

ELEGIR UNA Y MANTENER. La mezcla no declarada produce
inconsistencia.

---

## DETALLE REVELADOR vs. DETALLE DECORATIVO

Un detalle revelador hace un trabajo dramático: caracteriza a un
personaje, avanza una relación, carga un objeto con significado
futuro, comprime un estado emocional.

Un detalle decorativo existe para probar que el autor investigó.

TEST DE DETALLE:
Eliminar el detalle. ¿La escena pierde algo específico?
- Si no: decorativo, eliminar.
- Si sí, ¿qué pierde?: esa es la función del detalle.

CUOTA IMPLÍCITA:
En régimen minimalista, cada detalle debe pasar el test.
En régimen naval-decimonónico, se permite que algunos detalles
creen atmósfera sin carga dramática directa, siempre que estén
bien anclados (principio de anclaje).

---

## REGISTRO DE INVESTIGACIÓN

[Opcional pero muy recomendable. Este registro no entra en la
novela: alimenta al autor.]

FUENTES PRIMARIAS: [qué documentos, diarios, manuales, cartas,
mapas, testimonios se usan]

FUENTES SECUNDARIAS: [qué ensayos, historiografía]

ANACRONISMOS DETECTADOS Y DECIDIDOS:
Un anacronismo es consciente o es error. Registrar los conscientes
con su justificación dramática. Los no registrados son error.

VACÍOS DE INVESTIGACIÓN:
Qué aún no se sabe y qué escenas dependen de ello. Esto evita
escribir escenas falsas por falta de material.

---

## EL ERROR MÁS FRECUENTE — LA ESCENA-RESUMEN HISTÓRICO

Síntoma: un capítulo o escena entera dedicada a situar al lector
en la época, el oficio o el sistema político. Un personaje
"reflexiona" sobre el estado del mundo.

Diagnóstico: el autor sintió que el lector necesitaba saber esto
pero no encontró cómo distribuirlo escenificado.

Corrección: identificar lo estrictamente necesario, distribuirlo
en tres o cuatro escenas anteriores como fricción de acciones
concretas, eliminar el resumen.

Regla: no hay capítulo cuya función dramática sea "situar
históricamente". Si aparece, es un agujero dramático disfrazado.

---

## PROTOCOLO DE DISTRIBUCIÓN

Antes de entregar una escena, verificar:

1. ¿Qué textura entra en esta escena?
2. ¿Cuál es el anclaje de cada elemento? (acción, personaje,
   necesidad dramática)
3. ¿Hay algún elemento sin anclaje? Reubicarlo o eliminarlo.
4. ¿La densidad respeta AESTHETIC_REGISTER.md?
5. ¿La estrategia de glosario declarada se mantiene?
6. ¿Algún detalle es decorativo? Aplicar test de detalle.
7. ¿El narrador está sobrehablando su conocimiento? Filtrar.

---

## TESTS DE FUNCIONAMIENTO

TEST 1 — PÁGINA AL AZAR
Tomar una página. Contar elementos de textura. ¿Entran en la
densidad declarada? ¿Todos están anclados?

TEST 2 — ERUDICIÓN SILENCIOSA
¿El lector siente que el narrador sabe más de lo que muestra?
Ese es el efecto deseado. Si siente que el narrador muestra todo
lo que sabe, hay sobrexplicación.

TEST 3 — DETALLE MEMORABLE
Al cerrar el capítulo, ¿qué detalle recordará el lector? Si
ninguno específicamente, la textura no está cumpliendo su función
emotiva: es paisaje.

---

## FUNCIÓN COMPLEMENTARIA CON WORLD_ARC

Sección aplicable solo si WORLD_ARC.md está activo en el
proyecto.

Cuando el proyecto declara arco de mundo de serie, los dos
archivos de mundo se reparten función con regla operativa
clara: estado versus proceso.

**WORLD_TEXTURE registra el mundo en estado.** Configuración
material, gestual, léxica, institucional y mental disponible
para cualquier escena. Es la fotografía del mundo en un
momento concreto, accesible cuando una escena necesita
textura específica. WORLD_TEXTURE no rastrea evolución
multilibro; rastrea cómo el mundo se manifiesta en lo
sensible y lo nombrable.

**WORLD_ARC registra el mundo en proceso.** Trayectoria de
ejes en movimiento durante la saga, deudas y promesas
multilibro, fases del arco por libro, cruces con POVs. Es la
película del mundo, accesible cuando el diseño escénico
necesita saber qué fase del eje está activa en libro N.

**Regla operativa de consulta.** Toda escena se diseña con
ambos archivos disponibles, pero la pregunta operativa
determina cuál se consulta primero.

Pregunta de textura material o gestual ("¿cómo se manifiesta
el mundo en esta escena?"): WORLD_TEXTURE primero. Si la
escena toca eje del arco de mundo activo, consulta posterior
a WORLD_ARC para verificar fase del eje en libro N y ajustar
la textura a la fase.

Pregunta de fase de arco ("¿en qué punto del eje estamos en
este libro?"): WORLD_ARC primero. Si la fase del arco
requiere manifestarse en textura concreta, consulta
posterior a WORLD_TEXTURE para que la manifestación se
ancle en lo sensible siguiendo principio de anclaje.

**Coordinación de evolución.** Si el arco de mundo declara
que un eje cambia de fase entre libros, la textura del eje
en WORLD_TEXTURE debe coevolucionar coherentemente. La
descripción material del eje en libro N+1 no puede
contradecir la fase declarada en WORLD_ARC para libro N+1.
La auditoría de coherencia entre ambos archivos se ejecuta
en OPERACIÓN D.

**No solapamiento de inventarios.** WORLD_TEXTURE no
gestiona deudas, promesas, puntos de no retorno ni cruces
con POVs (eso pertenece a WORLD_ARC). WORLD_ARC no gestiona
densidad permitida, glosario técnico, estrategia de
inmersión léxica, ni catálogo de capas (eso pertenece a
WORLD_TEXTURE). El reparto evita que un mismo elemento se
registre dos veces sin coordinación.

---

## RELACIÓN CON OTROS ARCHIVOS

WORLD_TEXTURE.md recibe de:
- AESTHETIC_REGISTER.md (densidad permitida)
- VOICE_ARCHITECTURE.md (qué puede conocer/mencionar el narrador)
- SCALE_CALIBRATION.md (densidad soportable según longitud)
- RESEARCH_LEDGER.md (qué material del mundo está disponible
  por investigación y con qué fiabilidad)
- WORLD_ARC.md (cuando está activo, recibe la fase del eje
  correspondiente al libro en curso, para que la textura
  material coevolucione con la trayectoria multilibro
  declarada allí)

WORLD_TEXTURE.md alimenta:
- SENSORY_HIERARCHY.md (textura material)
- DIALOGUE_MECHANICS.md (léxico y registro de época)
- CHAPTER_BRIEF.md (distribución de información)
- CONTINUITY_PHYSICS.md (coherencia de mundo)
- NARRATIVE_CHRONOLOGY.md (historia del mundo, eventos
  sistémicos pre-narrativos)
- WORLD_ARC.md (cuando está activo, aporta el sustrato
  material y léxico del que las manifestaciones del eje
  toman cuerpo en escena: el arco se manifiesta a través de
  la textura, no en abstracto)
- PROSE_LINE_DISCIPLINE.md (la materia del mundo se nombra
  con sustantivo concreto y verbo concreto siguiendo la
  DOCTRINA DE PRIMACÍA NOMINAL Y VERBAL; la adjetivación
  sobre esa materia se regula por CUOTA 1 — ADJETIVOS
  CALIFICATIVOS modulada por el régimen declarado en
  AESTHETIC_REGISTER; ver sección COORDINACIÓN OPERATIVA
  CON PROSE_LINE_DISCIPLINE más arriba)

WORLD_TEXTURE.md es complementario funcional de:
- WORLD_ARC.md (cuando está activo). WORLD_TEXTURE registra
  el mundo en estado disponible para cualquier escena;
  WORLD_ARC registra el mundo en proceso multilibro. Ambos
  se consultan según pregunta operativa (ver sección FUNCIÓN
  COMPLEMENTARIA CON WORLD_ARC). Sus inventarios no se
  solapan: cada archivo gestiona dimensiones que el otro no
  cubre.


---
---

