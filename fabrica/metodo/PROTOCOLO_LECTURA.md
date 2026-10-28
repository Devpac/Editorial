# PROTOCOLO_LECTURA.md — cómo se lee un capítulo antes de darlo por bueno

> Archivo de servicio del modelo (v2.0, 22-10-2026; genérico: los datos de la obra que usan
> los encargos están en su preset, `PRESET_<OBRA>.md` › PROTOCOLO_LECTURA). Desarrolla la OPERACIÓN C.5 de la
> adenda de `SYSTEM_ORCHESTRATION.md` (§4), las pruebas a ciegas (§7) y la lectura externa con
> otros modelos (§8 de este archivo). Contiene los
> **encargos literales** que se usaron en la primera obra del modelo, para que cualquier ventana
> los repita igual. Cada lectora es un agente nuevo, **sin contexto**: no ha escrito nada,
> no conoce el modelo ni la biblia, y solo lee los archivos que se le dan.

---

## 1. Quién lee y para qué

| Lectura | Quién | Cuándo | Qué decide |
|---|---|---|---|
| **Editora** | Editora de ficción comercial especializada en dark romance | Cada capítulo | Nota por criterios (también la pareja: qué parte del capítulo es suya), mejores y peores momentos, errores de coherencia, correcciones mínimas |
| **Lectora tipo** | Lectora intensiva de la plataforma y la red de la obra (perfil de lectora de la biblia) | Cada capítulo o tramo | Nota de **enganche**, cuánto es romance, dónde saltaría líneas, si seguiría leyendo |
| **Prueba a ciegas** | Dos editoras, en orden invertido | Cuando hay dos versiones del mismo capítulo (cambio de modelo, de rama, de enfoque) | Cuál gana |
| **Lectura de plan** | La lectora tipo | Antes de aplicar un cambio de escaleta | Si el plan arregla lo que le aburría |
| **Editora de desarrollo** *(v1.3)* | Editora de desarrollo del subgénero | Cada tramo de la biblia y cada escaleta | Promesa, pareja, arquitectura, riesgos, cambios por impacto (§6 bis) |
| **Correctora de coherencia** *(v1.3)* | Correctora sin contexto | Biblia, preset, escaletas; y tras cortes en varios capítulos | Contradicciones, quién sabe qué, huecos, techos y suelos (§6 bis y §7) |
| **Lectura externa** *(v1.2.2)* | Lectoras de otros modelos, que pasa el autor | Cada ~7 capítulos y el libro entero | Problemas confirmados por tres lecturas o más; cuánto es romance (§8) |

**Cuando editora y lectora discrepan, manda la lectora** (criterio 1.º del autor: el disfrute
de la lectora).

**Listón para dar un capítulo por bueno:** nota global de la editora ≥ 7,5 y comparaciones
con «como» (como si, como quien, como un…) por debajo de unas 5 por 1.000 palabras. La nota
de enganche de la lectora se registra siempre; si baja de 6, el capítulo se revisa aunque
la editora lo apruebe. **El peso de pareja** *(v2.0)* también se registra siempre: el que
estima la editora, junto al del acta (C-10), con la unidad de `PAREJA_PRIMERO.md` §2. Por
debajo del objetivo (80 %), alarma al plan de la lectora y a la escaleta del bloque siguiente;
si el bloque baja del suelo (70 %), se reescaleta el bloque siguiente, nunca la prosa, y el
capítulo va a reescritura solo si la lectura lo pide.

## 2. Cómo se prepara el paquete

Una carpeta nueva por lectura, en el scratchpad de la ventana, con **solo** esto:

- `referencia_capN.md`: los capítulos anteriores ya cerrados (como mínimo los dos últimos y
  el último del otro POV; mejor todos los del tramo), **numerados como se publican** (si la
  escaleta y el libro difieren —un capítulo fundido, por ejemplo—, el cuaderno de la obra dice cómo).
- `ficha_capN.md`: la ficha del capítulo en `escaletaAmpliada.md` (no para la lectora tipo).
- El texto o los textos a leer.
- **Cabeceras:** se quita el título del libro y el número de escaleta, pero **se deja la línea del
  narrador** (`### <NARRADOR>`), como en el libro publicado. Sin ella la lectora no sabe cómo se
  llama el narrador que nadie nombra: en la primera obra del modelo, la lectora tipo llevaba ocho
  capítulos sin saber el nombre del protagonista porque se le había quitado (v1.2.2).
- En pruebas a ciegas: `texto_A.md` y `texto_B.md`, y la segunda editora los recibe
  **intercambiados**.
- **Primeros capítulos de un libro 2 o siguiente:** la referencia son los tres o cuatro últimos
  capítulos publicados del libro anterior (y los ya escritos del nuevo). Si la obra declara cada
  libro autónomo, una segunda lectora tipo lee el capítulo **sin** esa referencia: ¿se entiende y
  engancha sin haber leído el libro anterior? (SERIES_GLUE, adenda de dark romance, TEST A4).

Nada de actas, briefs, biblia ni plantillas: la lectora lee como lectora, no como
verificadora de un plan.

Para medir las comparaciones con «como», en la carpeta del texto:

```python
import re; t=open('texto.md',encoding='utf-8').read()
w=len(t.split()); c=len(re.findall(r'\bcomo (si|quien|un|una|el|la|los|las|se)\b',t,re.I))
print(round(1000*c/w,1))
```

## 3. Encargo a la editora (un capítulo)

> Eres editora de ficción comercial en español, especializada en dark romance para lectoras
> de Kindle Unlimited y BookTok. Lee SOLO los archivos de `[CARPETA]` y nada más del sistema.
>
> - `referencia_cap1.md` a `referencia_cap[N-1].md`: capítulos ya publicados ([DESCRIPCIÓN
>   PARA LECTORAS: persona, tiempo y narradores, cada uno con una línea; está en
>   `PRESET_<OBRA>.md` › PROTOCOLO_LECTURA]).
> - `ficha_cap[N].md`: lo que el cap. [N] tiene que hacer.
> - `candidato_cap[N].md`: el capítulo propuesto, en la voz de [NARRADOR].
>
> Evalúa el candidato de 1 a 10 (decimales) en: disfrute de la lectora de dark romance (¿engancha?, ¿repone el anhelo?, ¿el cierre empuja a pasar página?); pareja (¿qué cambia entre los dos?; y estima qué parte del capítulo, en %, es de pareja: los dos en escena y algo pasa entre ellos (choque, deseo, miedo, control, lo que se callan) —si están juntos y esa parte solo mueve la trama B, cuenta como trama B—, uno con el otro en directo o quien narra ocupado con el otro; un recuerdo de pasada no cuenta); continuidad de voz con los capítulos anteriores del mismo POV; cumplimiento de la ficha y coherencia con los anteriores [en especial: lo que deba cuadrar en este capítulo —horas, quién sabe qué, la escena que el otro narrador ya contó—]; repeticiones: ¿cuenta otra vez cosas que la lectora ya leyó, o solo lo que el otro narrador no vio?; calidad de prosa (imágenes que salen del personaje frente a imágenes puestas para sonar literarias, frases que explican lo ya mostrado, tics de IA, ritmo); y nota global, comparada con el nivel de los publicados (dales también una nota de referencia).
>
> Después: los tres mejores momentos y los tres peores (con cita), errores de coherencia concretos, y como máximo tres correcciones mínimas para publicarlo (cortar antes que añadir; sin tocar la voz). Sé severa y concreta. Español, máximo 600 palabras.

## 4. Encargo a la editora (prueba a ciegas, dos versiones)

> Eres editora de ficción comercial en español, especializada en dark romance para lectoras
> de Kindle Unlimited y BookTok (mujeres de 20 a 40 años). Lee SOLO los archivos de
> `[CARPETA]` y nada más del sistema.
>
> - `referencia_cap*.md`: los capítulos ya publicados de la novela. Fijan la voz y el listón.
> - `ficha_cap[N].md`: lo que el capítulo [N] tiene que hacer según la escaleta.
> - `texto_A.md` y `texto_B.md`: dos versiones candidatas del capítulo [N], de autores
>   distintos. No sabes de dónde viene cada una.
>
> Lee primero las referencias y la ficha, luego A y B enteros.
>
> Evalúa cada candidato de 1 a 10 (decimales) en: 1. Disfrute de la lectora de dark romance; 2. Continuidad de voz con los capítulos anteriores del mismo POV; 3. Cumplimiento de la ficha y coherencia con los anteriores [añadir lo que deba cuadrar en especial]; 4. Calidad de prosa; 5. Nota global, comparada con el nivel de los publicados.
>
> Después: cuál prefieres y por qué (tres razones con citas cortas), dos mejores y dos peores momentos de cada texto (con cita), errores de coherencia concretos, y si alguno podría publicarse tal cual o qué le falta. Sé severa y concreta. Responde en español, máximo 750 palabras.

Se lanzan **dos** editoras a la vez, la segunda con A y B intercambiados. Gana el texto que
prefieran las dos; si discrepan, se miran las notas globales y la de la lectora tipo.

## 5. Encargo a la lectora tipo (capítulo o tramo)

El perfil sale del perfil de lectora de la biblia y se copia en `PRESET_<OBRA>.md` ›
PROTOCOLO_LECTURA. El de abajo es el de una saga de dark romance para Kindle Unlimited y BookTok;
se cambian las autoras y la plataforma si la obra apunta a otro sitio.

> Eres una lectora de 31 años que lee unos ocho libros de dark romance al mes en Kindle
> Unlimited (Penelope Douglas, Rina Kent, H.D. Carlton, Ana Huang) y comenta en BookTok. No
> eres crítica literaria: lees por placer y abandonas rápido. Lee SOLO los archivos de
> `[CARPETA]` y nada más del sistema: primero `referencia_cap1.md` a
> `referencia_cap[N-1].md` (los capítulos que ya has leído de esta novela; la
> primera línea de cada uno dice quién narra), luego `candidato_cap[N].md` (el siguiente).
> Ignora la ficha si la hay.
>
> Cuéntame con sinceridad, en español y en primera persona, en un máximo de 400 palabras:
> - Del 1 al 10, ¿cuánto te ha enganchado el cap. [N]? ¿Y los anteriores, cada uno?
> - ¿Sientes ya la química/obsesión que buscas en el género? ¿En qué frases exactas?
> - ¿En qué momento, si alguno, te has aburrido, has saltado líneas o has sentido que te
>   contaban otra vez algo que ya habías leído?
> - A ojo, ¿qué porcentaje del capítulo es romance y qué porcentaje es [LA OTRA TRAMA, en
>   palabras de lectora: «la investigación», «la mafia»…]?
> - [Siempre que [PROTAGONISTA B] no esté en escena en el capítulo:] ¿Has echado de menos a
>   [PROTAGONISTA B]?
> - [Una pregunta del capítulo, si la hay: «¿Te da miedo él?», «¿Te ha molestado algo de cómo
>   reacciona [PROTAGONISTA A]?».]
> - ¿Seguirías leyendo? ¿Lo recomendarías? ¿Qué le falta para que no puedas soltarlo?

Las dos lecturas (editora y lectora tipo) se lanzan **a la vez**, como agentes nuevos y
separados, sobre el mismo paquete.

## 6. Encargo a la lectora tipo (plan de cambios)

> [Misma persona que en §5.] Lee SOLO: los capítulos ya escritos, el plan de cambios
> (`[archivo del plan]`) y, para saber qué viene después, las fichas de la escaleta de los
> capítulos [X a Y].
>
> Cuéntame con sinceridad, en español y en primera persona, en un máximo de 400 palabras:
> 1. ¿El plan resuelve lo que te aburría y lo que echabas en falta? ¿Qué punto te convence más y cuál menos?
> 2. [La escena nueva más importante]: ¿es lo que querías? ¿Qué tendría que pasar en ella para que la subrayes?
> 3. ¿Hay algo en los capítulos que vienen que todavía te haría saltar páginas o abandonar? ¿Dónde?
> 4. Una sola cosa que añadirías o quitarías del plan.

## 6 bis. Encargos de las fases previas: biblia, preset y escaletas *(v1.3)*

Las lee el orquestador en paralelo con la lectura de plan de la lectora tipo (§6), como agentes
nuevos y sin contexto (`ORQUESTADOR.md`, §5).

**Editora de desarrollo** (biblia por tramos, escaleta):

> Eres editora de desarrollo de ficción comercial en español, especializada en [SUBGÉNERO] para
> [PLATAFORMA Y PÚBLICO]. Lee SOLO los archivos de `[CARPETA]` y nada más del sistema: [la ficha
> de premisa y la biblia hasta donde está escrita / la biblia y la escaleta del libro N]. Evalúa de
> 1 a 10 (decimales): promesa comercial (¿qué compraría la lectora y por qué?); fuerza de la pareja
> (deseo, peligro, asimetría, moneda escasa); arquitectura (¿la saga, o el libro, tienen motor,
> picos, cruces y ganchos?, ¿dónde se cae la tensión?); originalidad dentro del subgénero; y
> riesgos (lo que puede hacer abandonar, lo que choca con el género, lo que se gasta demasiado
> pronto). Después: las tres decisiones más fuertes y las tres más débiles (con cita), lo que
> falta para poder escribir el capítulo 1 sin preguntar, y como máximo cinco cambios concretos,
> ordenados por impacto en la lectora. Sé severa y concreta. Español, máximo 700 palabras.

**Correctora de coherencia** (biblia, preset, escaleta, escaleta ampliada):

> Eres correctora de coherencia de una editorial. Lee SOLO los archivos de `[CARPETA]` y nada más
> del sistema: [la biblia / el preset y la biblia / la escaleta y la biblia / el tramo de escaleta
> ampliada, la escaleta y el tramo anterior]. Busca, citando dónde: (1) contradicciones de fechas,
> edades, cifras, lugares, nombres y trato; (2) quién sabe qué y cuándo (nadie sabe algo antes de
> que se le cuente; el canon oculto no sale antes de su libro); (3) [en el preset: ranuras sin
> respuesta en la biblia o con un valor distinto del de la biblia] [en las escaletas: calendario
> imposible, narradores fuera del reparto declarado, contadores pasados de su techo o por debajo
> de su suelo (los que declara la escaleta: peso de pareja por bloque, capítulos seguidos sin los
> dos en escena, capítulos seguidos sin escena con carga, ganchos de pareja, voces), capítulos
> que no cumplen la función que les da la escaleta]; (4) lo que una ventana de escritura sin contexto
> no podría resolver sin preguntar. No valores la calidad. Lo ambiguo pero defendible, «leve».
> Español, máximo 700 palabras, de más grave a menos.

**Lectora tipo, lectura de plan de una escaleta:** el encargo de §6, con las fichas en lugar de los
capítulos, y además: «¿Hasta qué capítulo leerías la muestra gratuita (los tres o cuatro
primeros)? ¿Cuándo esperas el primer encuentro entre ellos y cuándo llega? ¿En qué tramo
abandonarías? A ojo, ¿qué porcentaje del libro sería romance y qué porcentaje [LA OTRA TRAMA]?».

**Lectora tipo, lectura de una biblia** (fase 1, cada tramo):

> [Misma persona que en §5.] Lee SOLO los archivos de `[CARPETA]` y nada más del sistema: [la
> ficha de premisa y la biblia hasta donde está escrita]. Léelos como si fueran la contraportada,
> la ficha de los protagonistas y el plan de una saga que te ofrecen antes de que exista.
>
> Cuéntame con sinceridad, en español y en primera persona, en un máximo de 400 palabras:
> 1. ¿Comprarías el libro 1 con esta promesa? ¿Por quién: por él, por ella, por la pareja, por la trama?
> 2. ¿Qué te engancha de él y qué te echa para atrás? ¿Y de ella?
> 3. ¿Qué esperas que pase entre ellos en el libro 1, y cuándo? Si la biblia lo dice, ¿te parece pronto, tarde o bien?
> 4. ¿Qué te sobra o te aburre, y qué echas de menos que esperarías en este subgénero?
> 5. Una sola cosa que cambiarías.

**Libro 2 y siguientes** (diseño del libro y escaleta; `ORQUESTADOR.md`, §2.7 y §2.8). Los mismos
encargos, con estos cambios:

- **Editora de desarrollo:** el paquete suma la escaleta del libro anterior, y una pregunta más:
  «¿Qué hace este libro que el anterior no podía hacer? Si la relación repite el motor del
  anterior, dilo» (riesgo del segundo libro flácido, `SERIES_ARCHITECTURE.md`, adenda).
- **Lectora tipo, lectura de plan:** el paquete son los tres o cuatro últimos capítulos
  publicados del libro anterior (con la línea del narrador) y el diseño o las fichas del nuevo. En
  lugar de «¿cuándo esperas el primer encuentro?»: «¿Te paga lo que te dejó el final del libro
  anterior? ¿Cuándo esperas volver a verlos juntos, y [lo que anuncia el diseño: un
  descubrimiento, una primera vez], y cuándo llega? ¿Te da miedo él?».
- **Correctora de coherencia:** el paquete suma el estado de cierre del libro anterior
  (`libro_<N-1>/continuidad.md`) y su escaleta; busca además que el libro arranque donde lo dejó
  el anterior (lo que sabe cada uno, el peldaño de la escala, objetos y aparatos en juego) y que
  ningún canon oculto salga antes de su libro.
- **Lectora tipo sin el libro anterior** (si la obra declara cada libro autónomo): lee solo las
  fichas de la muestra gratuita del nuevo (o sus primeros capítulos escritos): «¿Entiendes quiénes
  son y qué está en juego sin haber leído nada antes? ¿Qué te falta? ¿Seguirías?».

## 7. Qué se hace con las lecturas

1. Se escribe `libro_NN/capNN_lectura_editorial.md`: notas (tabla, con el peso de pareja de la
   editora, el porcentaje de romance de la lectora tipo y el del acta), lo que funciona y no se
   toca, **tres problemas como máximo** con su corrección mínima aplicada, lo que se queda
   aunque alguien pidiera cortarlo (y por qué), lo que sube a canon y los avisos para los
   capítulos siguientes.
2. Las correcciones las aplica la ventana principal: **cortar antes que añadir; añadir solo
   cuando falta un beat**. Nunca se reescribe el capítulo entero.
3. Lo que sube a canon se anota en la biblia (Anexo A). Lo que pide un cambio de escaleta
   pasa antes por la lectura de plan (§6), salvo que lo pidan ya tres lecturas o más.
4. **Correctora de continuidad** *(v1.2.2)*: si las correcciones tocan más de un capítulo (o
   cortan algo que otro capítulo cita), un agente nuevo relee el tramo entero con este encargo:

   > Eres correctora de continuidad de una editorial de ficción comercial en español. Lee SOLO
   > los archivos de `[CARPETA]` (los capítulos del tramo, en orden, con la línea del narrador)
   > y nada más del sistema. Varios capítulos acaban de recibir cortes: busca sobre todo costuras
   > rotas. Línea a línea: (1) referencias huérfanas —frases que remiten a algo que la lectora no
   > ha leído antes («otra vez», «como siempre», un chiste que se repite, una pregunta que «ya
   > hizo», un objeto o dato que se da por sabido)—, diciendo si lo que remite está establecido
   > antes (cita dónde) o no; (2) contradicciones de horas, días, lugares, quién sabe qué,
   > objetos, nombres; (3) repeticiones entre capítulos que una lectora notaría como copia,
   > también entre los dos narradores; (4) saltos que no se entienden. Cita la frase y el
   > capítulo. No valores la calidad. Si algo es ambiguo pero defendible, márcalo como «leve».
   > Español, máximo 700 palabras, de más grave a menos.

   Lo grave se arregla en una línea; lo leve se anota en `continuidad.md`.
5. Commit y push.

## 8. Lectura externa (otros modelos) *(v1.2.2)*

Cada tramo de unos siete capítulos, el autor pasa el tramo a dos o tres modelos distintos
(Gemini, GPT, Claude en otra ventana), cada uno en una conversación nueva, con un archivo que
junta los capítulos en orden de publicación y este encargo. No se les dice que el texto es de
una IA, ni que es una prueba, ni qué se espera.

> Quiero que hagas de lectora real, no de asistente ni de crítica literaria.
>
> **Quién eres:** Lucía, 31 años, de Valencia. Lees unos ocho libros al mes de dark romance en
> Kindle Unlimited y en papel. Tus favoritas son Penelope Douglas, Rina Kent, H.D. Carlton, Ana
> Huang, Sophie Lark y Mercedes Ron; también lees romántica española en Wattpad y Amazon. Tienes
> una cuenta de BookTok con unos 15.000 seguidores donde reseñas sin filtro. Abandonas un libro
> en cuanto te aburre y no te da pena decirlo. Te encantan el stalker con código, el *morally
> grey*, el *slow burn* que paga y las heroínas con carácter. Odias el relleno, las protagonistas
> tontas, los héroes que no dan miedo de verdad y la prosa que se escucha a sí misma.
>
> Te paso los [N] primeros capítulos de una novela en español de [SUBGÉNERO] que una amiga te ha
> recomendado: *[TÍTULO DE LA SAGA]*, libro [N] de una saga. Léelos enteros y en orden,
> como los leerías en el Kindle. Luego contesta como Lucía, en primera persona, en español y con
> tu forma de hablar. No me des la razón ni seas amable por compromiso: si algo te aburre o te
> saca de la historia, dilo con la frase exacta.
>
> 1. **Enganche capítulo a capítulo:** nota del 1 al 10 a cada uno y una línea de por qué.
> 2. **El momento exacto** (cita la frase) en que habrías dejado el libro, si lo hay. Y el
>    momento en que dijiste «vale, sigo».
> 3. **La pareja:** ¿hay química y obsesión de verdad? ¿Él da miedo? ¿Ella te cae bien o te
>    desespera? Cita las frases que subrayarías. A ojo, ¿qué porcentaje de lo que has leído es
>    romance y qué porcentaje es [LA OTRA TRAMA]?
> 4. **Lo que sobra y lo que falta:** qué te saltarías y qué estás deseando que pase.
> 5. **Comparado con lo que lees:** ¿a qué libro o autora se parece? ¿Está a la altura, por
>    encima o por debajo?
> 6. **Decisión:** ¿lo terminarías? ¿Lo comprarías a 3,99 € si no estuviera en KU? ¿Lo
>    recomendarías en BookTok? Si sí, escribe el texto del vídeo (unas 40 palabras); si no,
>    escribe la reseña de una o dos estrellas que dejarías en Goodreads.
> 7. **Una sola cosa** que le pedirías a la autora para que no pudieras soltarlo.
>
> Máximo 700 palabras.

(Lucía, sus autoras y sus gustos son los de una lectora de dark romance; si la obra es de otro
subgénero, se ajustan con el perfil de la biblia.)

**Qué se hace con ellas:** se ponen en una tabla junto a la última lectora tipo (numeración
publicada), con su porcentaje de romance junto al peso de las actas; con cada una va una
OPERACIÓN D corta del tramo (`ORQUESTADOR.md` §2.5). Lo que señalan tres lecturas o más es
problema confirmado: se corrige en los capítulos ya escritos (cortando) y, si es de oficio, va
al cierre del modelo. Lo que señala una sola se anota y no se toca. Después de cortar, una correctora de continuidad sin contexto lee el
tramo entero buscando referencias huérfanas: los cortes rompen callbacks.

**Calibración:** la lectora tipo puntúa más bajo que las externas (en el primer tramo, un punto
menos de media), pero coincide en el orden de los capítulos. Las dos sirven: la tipo encuentra
el valle; las externas dicen si se compra.

**OPERACIÓN D corta** *(v2.0)*: con cada lectura externa, o cada unos siete capítulos si no la
hay (`ORQUESTADOR.md` §2.5), un agente nuevo lee el tramo con este encargo. El paquete: el tramo
en orden de publicación, con la línea del narrador, y sus fichas de la escaleta, con el peso que
declara cada una.

> Eres editora de desarrollo de ficción comercial en español, especializada en dark romance. Lee
> SOLO los archivos de `[CARPETA]` y nada más del sistema: `tramo.md` (los capítulos [X] a [Y]) y
> `fichas_tramo.md` (lo que la escaleta pide a cada uno y el peso de pareja que estima). Mide, por
> capítulo y por bloque de cuatro capítulos ([BLOQUES DEL TRAMO]), qué parte es de pareja, en
> palabras: los dos en escena y algo pasa entre ellos (choque, deseo, miedo, control, lo que se
> callan) —si están juntos y esa parte solo mueve la trama B, cuenta como trama B—, uno con el otro
> en directo o quien narra ocupado con el otro; un recuerdo de pasada no cuenta. Ponla junto a la
> que estima la ficha. Después, citando el capítulo: (1) capítulos en que el otro no ocupa ni un
> tercio, y rachas de más de dos capítulos sin los dos en escena; (2) rachas de más de cuatro
> capítulos sin una escena con carga (contacto, *edging*, beso o sexo); (3) cuántos cierres dejan
> abierto algo entre ellos, por bloque; (4) qué parte del tramo ocupa lo que no es pareja, y si la
> trama B tiene agujeros (un dato que se cobra sin haberse sembrado, un paso que no se entiende);
> (5) si la relación se mueve de un bloque a otro o se repite. No valores la calidad. Español,
> máximo 600 palabras.

Su medida va al historial (§9) junto a la de las actas; si difieren, manda la suya (D-21 de la
adenda de `SYSTEM_ORCHESTRATION.md`).

## 9. Historial

Cada libro lleva el suyo: `libro_NN/historial_lecturas.md`, con una fila por lectura (qué se
leyó, quién, si están los dos, el peso de pareja, notas y qué se decidió). Lo escribe el
orquestador al cerrar cada auditoría.
