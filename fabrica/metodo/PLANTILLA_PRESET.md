# PLANTILLA_PRESET.md — el preset de una obra (MODELO_DarkRomance v2.0)

> Archivo de **modelo**. Cada obra tiene un `PRESET_<OBRA>.md` en la raíz de su repo con **los
> valores que leen las plantillas de género**: fichas, voces, idiolectos y tics vigilados, paletas,
> contadores, ritmo de consumación, escala de rendición, trama horizontal y su calendario, escala del
> libro y los datos de los encargos de lectura. Lo escribe la ventana P1 en la fase 1b
> (`ORQUESTADOR.md`, §2.2) **a partir de la biblia**, que manda.

## Reglas

- **No inventa.** Cada valor sale de la biblia (cítala por sección o por decisión del Anexo A). Si
  una ranura no tiene respuesta en la biblia, se escribe la pregunta para el orquestador, que la lleva
  al autor o a la biblia antes de seguir.
- **Una sección `##` por plantilla y una `###` por ranura**, con los nombres exactos de abajo: las
  plantillas apuntan a ellos («`PRESET_<OBRA>.md` › <PLANTILLA> › <sección>»).
- **Se mantiene al día:** cuando la biblia cambia un valor, el orquestador cambia el preset en el mismo
  commit.
- **Es contrato de canon** para las ventanas de capítulo: el NEXT dice qué secciones leer.
- **Si una ranura no aplica** a la obra (por ejemplo, una sola voz narradora, o ningún apodo
  racionado), se escribe «no aplica» y por qué; no se deja vacía. Las descripciones de abajo salen
  de la primera obra del modelo: dicen qué decidir, no qué responder.
- **Ningún recurso es obligatorio por estar en una ranura.** Muchas nombran recursos que tuvo la
  primera obra (dos paletas y su mezcla racionada, una señal física de él que delata su deseo, un
  apodo o un nombre reservado, una ausencia larga, un investigador que persigue a la protagonista,
  relojes de saga, una miga por libro, una firma del antagonista). Si la biblia de la obra no lo
  tiene, la ranura dice «no aplica»: **no se inventa un equivalente para rellenarla**. Lo que la
  obra tenga y ninguna ranura prevea se apunta en la sección de la plantilla más cercana, con un
  `###` nuevo, y se avisa al orquestador.
- **Lo que vale para un solo libro se rotula con su libro** («Antagonista del libro 1», «libro 1:
  [N] capítulos»), para que la ventana del libro siguiente no lo lea como suyo. Al abrir cada libro,
  el orquestador añade las filas del libro nuevo (`ORQUESTADOR.md`, §2.7).

## Cabecera del preset

Obra y saga; subgénero declarado; forma de la saga (SERIES_GLUE, adenda de dark romance: la misma
pareja en muchos libros, dúo o trilogía, o parejas rotativas); narradores (cuántos, quién es cada
uno en una línea); número de libros previsto; versión de la biblia de la que sale; regla «manda la
biblia»; y la **correspondencia de roles**: una tabla que dice quién es en la obra cada rol que
nombran las plantillas (protagonista A, protagonista B, narrador hermético, narradora irónica,
antagonista del libro, antagonista de saga, la herida de cada uno, el espacio propio, los recursos
racionados), con «no aplica» en los que no tenga. Con parejas rotativas, la tabla lleva una
columna por libro (la pareja de cada uno) y las fichas de cada pareja entran al abrir su libro.

## SYSTEM_ORCHESTRATION

La adenda de género apunta aquí sin nombre de sección. Declara:

- **Extensión, persona y narradores:** palabras por libro y por capítulo; persona, tiempo y
  alternancia; dónde está el régimen estético de la biblia (sus medidas son siempre alarma de
  cierre: PROSE_LINE_DISCIPLINE, adenda).
- **Instancia y canon oculto:** el nombre del archivo de la biblia; qué partes guardan canon oculto;
  el criterio para la investigación sin informante; referencias heredadas de un modelo anterior.
- **Doble hélice:** el peso de la pareja (adenda §5, «La pareja es la trama A»; la ranura conserva
  su nombre de la v1.3): objetivo, suelo y unidad, de la biblia §14 🔒.
- **Narradores y cierre:** cuál es el narrador hermético y cuál el irónico (si los hay); las paletas
  de cada uno; los contadores de la obra y su techo; los datos de la trama horizontal que el calendario
  vigila.
- **Tics vigilados:** la muletilla de cada narrador y las imágenes de oficio que se racionan.
- **Lectora tipo:** el perfil de lectora (de la biblia).
- **Gancho y primer capítulo:** cómo abre cada libro.

## PROTOCOLO_LECTURA

- **Descripción para lectoras:** persona, tiempo y narradores, una línea cada uno.
- **Lectora tipo:** el perfil que se pega en los encargos (`PROTOCOLO_LECTURA.md` §5).
- **Lectura externa:** subgénero, título de la saga y preguntas propias de la obra.
- **Numeración:** si la escaleta y el libro publicado difieren, cómo.
- **La otra trama:** cómo se nombra la trama B en palabras de lectora («la investigación», «la
  mafia»…), lo que los encargos piden como [LA OTRA TRAMA] (`PROTOCOLO_LECTURA.md` §5, §6 bis y §8).

## Las demás plantillas

Las ranuras salen de las líneas «**Valores de la obra →**» de cada plantilla (abajo, una por línea,
con lo que la plantilla pide que se declare).

## GENRE_CONVENTIONS

- **Régimen de la saga.** Cuántas novelas forman la saga, con qué ambientación se declara su dark romance y qué voz y qué firma sensorial tiene su estética.
- **Declaración primaria de la obra.** Quiénes forman su pareja protagonista y cuál es su subgénero, con lo que aporta a cada libro.
- **Variante del subgénero.** Su subgénero y, si no es el policial, qué es en él cada regla con marca de variante (regla por regla), o «no aplica».
- **Declaración fundacional de la obra.** Su frase fundacional y a qué lectoras no hay que venderle el libro.
- **Posicionamiento de la obra.** Frente a qué vecino de género se posiciona y cómo encarna su pareja cada atributo de la tabla.
- **Pilares en la obra.** Su firma sensorial, si la tiene, cuántos libros señaliza, y quién cruza las líneas con quién.
- **Convenciones en la obra.** Su peso de pareja y sus suelos, si sube alguno (si el autor baja alguno, la decisión de la biblia que lo autoriza), el número y la longitud de sus capítulos, de qué trata su trama horizontal y qué sabe la lectora antes que la protagonista.
- **La inversión clave de la obra.** Cómo rompe su protagonista la convención, qué oficio concreto conserva y en qué libros se hace evidente la inversión.
- **Peligros en la obra.** Con qué formación seduce tácticamente su protagonista, en qué planos se activa su defecto y en qué libros descubre la vigilancia y la vuelve a su favor.
- **Pecados propios de la obra.** Qué nombre de él reserva y hasta qué libro, y qué recursos racionados tiene (mezcla de paletas, gesto de vulnerabilidad, apodo) con su techo por libro, si los tiene.
- **Expectativas en la obra.** Con qué destreza física gana sus batallas su protagonista.
- **Oscuridad propia de la obra.** De qué está hecha su oscuridad, qué tópicos de dark romance no repite (su anti-firma de género) y cómo actúa su antagonista de saga, si lo tiene.
- **Marca y clasificación de la obra.** El nombre de la saga, su fórmula de títulos y sus categorías.
- **Tests en la obra.** Su peso de pareja, su número de capítulos y el techo de sus recursos racionados, si los tiene.
- **Relación con otros archivos en la obra.** Su peso de pareja, su extensión y la horquilla de sus capítulos, y la voz de cada protagonista.

## CHARACTER_PHYSICS

- **Propósito.** Cuántos libros tiene la saga, quiénes forman su pareja fija (o sus parejas, si rotan) y qué personajes tienen ficha cerrada.
- **Tipos de personaje.** Quiénes son protagonista A y protagonista B, en cuántas capas se reparte el transversal, si lo tiene, cuántos forman el elenco fijo, qué personajes son bisagra y qué extensión y cuota de relación protege el máximo de tres fichas.
- **Tipos de antagonismo.** Cuántos tipos de antagonismo superpone la saga y quién o qué encarna cada uno.
- **Registro de mecanismos de presión.** Qué condicionantes estructurales presionan a la pareja, cómo se manifiestan sobre ella y quién los encarna en escena.
- **Caso híbrido.** Si la saga tiene un antagonista con cuerpo que opera como sociedad, durante qué libros, y qué obliga a resolver con la cabeza y no con la violencia.
- **Compatibilidad entre tipos.** Qué tipos ocupan el puesto secundario permanente y el terciario por arco.
- **Ficha A1 — protagonista A.** La ficha completa y cerrada de protagonista A, campo por campo, con sus cifras vinculantes y el libro de cada fase.
- **Ficha A2 — protagonista B.** La ficha completa y cerrada de protagonista B, campo por campo, con sus cifras vinculantes y el libro de cada peldaño.
- **Reglas duras del canon.** Cuáles de estas reglas tiene y con qué valores: la señal corporal de protagonista A y su estado de control; la señal física que delata el deseo de B; la asimetría verbal, con el idiolecto de cada uno; si a A la subestiman, su cuota de combate con carga sexual por libro y el contraste de envergadura, si lo hay; y cuántas mezclas de paletas caben en un volumen, si tiene paletas.
- **Plantilla B — antagonista.** Los mecanismos de la pareja que el antagonista invierte, las franjas entre las que rota el antagonista del libro y, si protagonista B lo vigila, por qué medio lo ve.
- **Antagonista transversal.** Cuántas capas tiene el antagonista transversal, con sus libros, quién o qué es cada una, su tipo y lo que obliga, y la ficha de quien lo encarna.
- **Elenco fijo.** Quiénes forman el elenco fijo, con su edad, su función dura, lo que ilumina de la pregunta central y su bomba.
- **Regla de oro de Asuntos Internos.** Si tiene un investigador que cerca a la pareja, qué miembro del elenco fijo es.
- **Personajes-bisagra.** Quiénes son los personajes-bisagra, con su edad, su frecuencia de aparición, su función dura y su estado.
- **Registro de coste acumulado.** Qué amenaza acumulativa suma una pieza en cada volumen, si la tiene, y sobre qué misterio de la trama horizontal cae la miga de pan; la columna de pareja sale de su escala de rendición (ROMANCE_BEAT_MAP).
- **Instrucción operativa.** El verbo que resume el mecanismo de cada protagonista y el ejemplo canónico de peldaño entregado antes de tiempo.
- **Síntomas verbales del colapso.** Con qué rasgos de idiolecto colapsa cada protagonista, qué nombra B en voz alta solo al colapsar, si lo tiene, y en qué libro cae la crisis.
- **Test de tres preguntas.** El libro de la crisis y la marca de idiolecto que identifica a cada protagonista.
- **Rango de la excepción.** El nombre del protagonista hermético al que se aplica la última frase.
- **Tests de funcionamiento.** Los tests con los nombres, los planos y las cifras de cada herida y, si los tiene, la señal corporal, la señal del deseo de B, las marcas y el contador de mezclas de la saga.
- **Cruces POV × ejes del arco de mundo.** Si WORLD_ARC está activo, los ejes de mundo y su intensidad para cada protagonista por tramos de libros, el cruce revelador canónico, el libro en que la crisis coincide con el pico de un eje y, si los tiene, los arcos de la saga y sus puertas de salida.
- **Relación con otros archivos.** Los mecanismos que chocan en la pareja, el peso de pareja, la extensión de la saga y, si las tiene, las columnas de serie que se actualizan en cada capítulo.

## RELATIONSHIP_PHYSICS

- **La relación central.** Su pareja, la clase y la reciprocidad de la relación, cómo se reparte entre los dos la asimetría, las dos heridas, el tercero que no forma triángulo, si lo tiene, las transgresiones no consentidas concretas y las decisiones de su biblia que lo ratifican.

## DIALOGUE_MECHANICS

- **Los dos narradores.** Quiénes son sus dos narradores: protagonista A, la voz que habla, y el narrador hermético (protagonista B).
- **Los tres campos.** Quién ocupa cada campo (la pareja del duelo, qué voces se interrogan entre sí y qué personajes del elenco fijo forman el roce).
- **La asimetría de la pareja.** La ficha rellena de los dos registros, la proporción del choque entre ambos y una muestra de calibración correcta.
- **Beats de rendición pactados.** En qué libro cae cada beat de rendición y qué sentimiento puede articular en él el narrador hermético.
- **Regla de nombre.** Si los tiene, qué apelativo sale de una sola boca y qué nombre se retiene hasta un beat de rendición (quién puede decirlo, desde cuándo y qué efecto tiene en la escena).
- **Cadencia.** Qué otras voces tienen derecho al turno largo y con qué función.
- **Cadencia.** Una muestra del silencio del narrador hermético acotado como turno.
- **Atribución.** Una muestra de atribución por gesto del narrador hermético, con un objeto de su mundo.
- **Atribución.** Los marcadores de atribución que bastan para la voz del narrador hermético.
- **Idiolecto.** La ficha rellena de cada voz y los anclajes de canon que fija entre voces concretas.
- **Asimetría dialógica.** De dónde saca su ventaja el narrador hermético y con qué voz se invierte la mesa y es protagonista A quien responde.
- **Asimetría dialógica.** Con cuántas palabras como máximo cierra el narrador hermético y quién cierra con cada voz del elenco que se enfrenta a protagonista A.
- **Interrupción y solapamiento.** Quién corta desde fuera (quién avisa, quién escribe en el peor momento), cuánto dura su *edging* y su muestra de corte por gesto.
- **Lo no dicho en el diálogo.** Una muestra de cambio de tema y, si la saga tiene trama horizontal, qué secreto de ella se administra así.
- **Lo no dicho en el diálogo.** Una muestra de gesto deslizado del narrador hermético.
- **Lo no dicho en el diálogo.** Qué gesto físico de protagonista A es su marca de vulnerabilidad, si la tiene.
- **Diálogo y registro.** Su régimen fijado y la longitud de capítulo, y la modulación de registro admitida en cada voz que no es el narrador hermético.
- **El interrogatorio como seducción táctica.** Si tiene esta escena (variante policial), el defecto de protagonista A y los planos en que sí se activa, y una muestra de la mecánica en su voz, con hueco de instancia.
- **Diálogo durante el sexo.** Cómo se le rompe en la cama el registro a protagonista A y, si los tiene, qué apelativo y qué nombre cambian la temperatura de la escena.
- **Gestión de información en diálogo.** Quién hace de tercero que no sabe, qué secreto de la trama horizontal se entrega por capas y en qué libros (si la saga la tiene), y quién informa por omisión.
- **Gestión de información en diálogo.** Un contraejemplo de diálogo «como sabes» con datos de su propio mundo.
- **Diálogo de grupo.** Qué alianzas se ven en sus escenas de grupo, en qué sala y delante de quién calla protagonista A, y si su narrador hermético entra en ellas.
- **Errores frecuentes.** Qué voces tienen la elocuencia, y ninguna más.
- **El diálogo como gancho de capítulo.** Cuántos capítulos tiene cada libro y, si la saga tiene trama horizontal, qué secreto de ella alimenta la miga.
- **Protocolo pre-escritura.** La pregunta 5 dicha con el nombre de su narrador hermético.
- **Tests de funcionamiento.** El umbral de palabras del TEST 1, los nombres del TEST 4, si los tiene, y qué voces cuentan con turno largo en el TEST 6.
- **Relación con otros archivos.** Las mismas dependencias dichas con los nombres de su pareja y, si lo tiene, de su nombre retenido.

## VOICE_ARCHITECTURE

- **Declaración de voz.** Su persona, su tiempo y sus narradores, la regla de su canon que fija la asimetría verbal y en qué sección de su biblia se dice cuánta explicación narratorial admite cada voz.
- **Test de asimetría: las voces de la obra.** El rasgo de cada narrador que el test busca en la narración, quién es el hermético, si lo tiene, un ejemplo de su manuscrito y el caso que dio origen al test.

## AESTHETIC_REGISTER

- **Propósito.** Cuántos libros tiene la saga y, si las tiene, qué paletas la sostienen.
- **Declaración primaria.** El alcance de la declaración en libros, los nombres de sus dos narradores, la ciudad de su ambientación, de dónde le viene a A la explicación moderada (su oficio, su historia o su carácter) y cuántos cierres de capítulo en gancho tiene cada libro.
- **Persona, tiempo y alternancia.** Su persona, su tiempo y sus narradores, el alcance de la regla en libros, el ejemplo canónico de lo que la lectora sabe antes que A y qué pasados de la pareja entran en la escena.
- **Voz de la protagonista A.** El tono de A y lo que tapa con él, si tapa algo, su frase y su cadencia, desde dónde analiza (su oficio, si le viene de ahí), cómo se comporta su tono en las escenas duras y su límite.
- **Voz del protagonista B.** Qué registra B antes de sentir y de dónde le viene la hipervigilancia, si la tiene; qué señal física delata su deseo, si la obra se la da; y qué nombres y apelativos reserva, si reserva alguno, con el libro en que aparece cada uno.
- **Medidas de la asimetría.** Las cifras de longitud de frase y de réplica de cada narrador.
- **Lectora implícita.** A qué escenas, cuentas e hilos de la saga vuelve la lectora al releer, y qué motivos recurrentes lo sostienen.
- **Regímenes no declarados.** Qué secundarios pueden hablar en registro oral y, si admite un préstamo local como el dato conductual, en qué escenas entra.
- **Efecto sobre Capa 3.** En qué espacio se curan las heridas y ante qué tercero habla la pareja en sus escenas de crisis.
- **Metáfora estructural.** La pregunta central que codifica su metáfora, el vehículo concreto que la lleva (un oficio, un objeto, un lugar) y su relación con el título de la saga, si la tiene.
- **Doble paleta.** Si la tiene, la paleta de cada narrador sentido por sentido y su significado, la fórmula con que se nombra la mezcla y su máximo de apariciones por libro.
- **Motivos fijos.** Sus motivos fijos —rasgos, objetos, marcas y lugares— y lo único que significa cada uno.
- **Estética de lo táctil y lo corporal.** Los lugares y objetos concretos en que ancla la violencia, el contacto y el registro corporal de A.
- **Longitud de frase por voz.** La referencia y el rango de longitud de frase de cada narrador.
- **Proporción de diálogo por voz.** La proporción global de diálogo, la de los capítulos de cada narrador con su porqué y la extensión de capítulo en palabras.
- **Patrón de A.** En qué consiste el patrón propio de A y qué personas y episodios lo encarnan.
- **Oficio de análisis de A.** De dónde le viene a A la licencia de interpretar (su oficio, su historia o su carácter).
- **Tests.** Los rangos con que mide TEST 3, la mezcla y el máximo que cuenta TEST 5, si tiene paletas, y el motivo fijo que audita.
- **Relación con otros archivos.** El máximo de mezclas que recibe SENSORY_HIERARCHY, si tiene paletas, los escenarios cuya densidad regula WORLD_TEXTURE, el peso de pareja de STORY_SPINE, el número de volúmenes y el adjetivo con que GENRE_CONVENTIONS sugiere la voz de A.
- **Error común.** Qué escenario suyo es el que más tienta a convertirse en personaje.

## PROSE_LINE_DISCIPLINE

- **Régimen estético.** En qué sección de su biblia vive el régimen estético que gobierna las cuotas 1–8.
- **Anti-firma.** De qué tradiciones o corpus huye su prosa y en qué sección de su biblia lo declara.
- **Medidas observadas.** Las medidas de sus capítulos de referencia, una columna por capítulo con su narrador, y la variación de un narrador que no es alarma.
- **Las dos voces.** Cuál de sus narradores es el hermético, si lo tiene, y cuándo habla, y qué explicación narratorial, qué manera de perfilar y qué metáfora ornamental admite cada voz.
- **TIC 4: glosa y remate.** Qué narrador es el irónico y cuál el hermético, si los tiene, la sección de su biblia con el idiolecto, y los ejemplos de su manuscrito de glosa cortada, de remate de idiolecto y de regla de trabajo.

## HEAT_DISCIPLINE

- **Propósito en la obra.** Cuántos libros tiene la saga sobre la que se dosifica el calor, quién es el hombre cuya rendición se raciona (su narrador hermético, si lo tiene) y de qué documento sale la regla de la moneda escasa.
- **Contacto en la obra.** Dónde ocurren las curas y qué gestos de contacto propios de su pareja cargan como el sexo.
- **Corte en la obra.** De qué sección de su biblia salen sus herramientas de *edging*, quién corta y cuánto dura su tramo de *edging*.
- **Ritmo de consumación y escala de rendición.** Qué pasa entre los dos, en lo físico y en lo emocional, en cada uno de sus primeros libros (o en cada tramo del libro, con parejas rotativas), si adelanta algún suelo de calor (o el autor retrasa alguno, con la decisión de su biblia), desde cuándo rige el refuerzo intermitente y dónde cae cada entrega de la escala de rendición.
- **Consentimiento en la obra.** Qué sección y qué decisión de su biblia fijan las familias de actos de su pareja.
- **Señales y contadores.** Cada señal de calor de su pareja, si las tiene, qué anuncia y su techo por libro.
- **Tests en la obra.** Qué señales y contadores vigila el TEST 5, si los tiene.
- **Relación con la biblia de la obra.** Qué secciones de su biblia alimentan este archivo.

## ROMANCE_BEAT_MAP

- **Propósito en la obra.** El nombre de la saga, su género secundario, su pareja y su peso de pareja.
- **Principio operativo en la obra.** Quiénes son los dos protagonistas que la escena del género secundario pone en tensión.
- **Beats en la obra.** Cuántos libros tiene la saga; el porcentaje de cada beat de pareja en sus libros, si adelanta algún suelo (o el autor retrasa alguno, con la decisión de su biblia); y, si los tiene, cuáles son sus dos paletas, de qué trata su trama horizontal y quién cerca a la pareja.
- **Escalera de rendición de la obra.** En qué libro (o, si la escalera cabe en un libro, en qué tramo) cae cada peldaño de la rendición de él, hasta la entrega mayor, y el ritmo de consumación de cada libro dentro de los suelos (HEAT_DISCIPLINE).
- **Puntos de cruce en la obra.** De qué trata la miga de pan horizontal de su protagonista, si la saga tiene trama horizontal, y quién detona en él los instintos posesivos.
- **Umbrales en la obra.** Quién abre la primera página y, si la saga tiene trama horizontal, de qué trata la pista que se audita.
- **Tests en la obra.** Sobre qué o quién es la información firme que exige la miga, si la saga tiene trama horizontal, y quién confiesa en la escala de rendición.

## ELLIPSIS_PROTOCOL

- **Propósito.** Quién investiga a la protagonista A y no puede probar lo que el texto no narra, si la obra lo tiene.
- **Lo que no se elide nunca.** Dónde está el punto más bajo de la saga porque su violencia se mira entera, si lo tiene, dónde caen los hitos de la escala de rendición, sobre qué trata el hallazgo horizontal, si la saga tiene trama horizontal, y qué decisiones concretas de la protagonista A no se eliden.
- **Uso A.** Los resultados concretos por los que la protagonista A deduce lo que hizo el protagonista B, quién la investiga, si alguien la investiga, y en qué libro y con qué escena se rompe el fuera de plano.
- **Uso B.** Si tiene una ausencia larga del protagonista B, cuánto dura (dentro del tope, o la decisión de su biblia que lo pasa) y dónde cae (después de la primera consumación), y desde dónde se sustituye por otras retiradas.
- **Uso C.** Adónde van los traslados que se saltan y qué escenarios de procedimiento se narran porque en ellos ocurre otra cosa.
- **Uso D.** Cuál es la memoria racionada del protagonista B, si la tiene, dónde se cuenta entera y con qué fragmentos asoma antes; cuál es la herida de fondo de la protagonista A y por qué astillas llega.
- **Tipos de elipsis.** Qué calla el protagonista B y desde cuándo, si calla algo, dónde suena ese reloj y, si los protagonistas tienen un duelo, cómo lo vive cada uno y cuándo nombra a su muerto.
- **Cuándo elidir.** En qué espacio transcurre la domesticidad de la pareja, clandestina o no.
- **Descrito seco.** La operación canónica del protagonista B que fija la temperatura de este modo.
- **Descrito poético.** Qué duelos concretos abren este modo y, si tiene paletas, la fórmula de su cruce y cuántas veces por libro se permite.
- **Asignación por tipo de contenido.** Qué duelos y qué memoria ocupan sus filas, si los tiene, dónde se cuenta entera esa memoria y, si hay secuestro, dónde cae.
- **Coherencia por tipo.** Cuántos libros abarca la consistencia y en qué libros cae típicamente la escena que rompe el régimen.
- **Elipsis mayores permanentes.** Cuántas y cuáles son sus elipsis mayores permanentes, si las tiene, y en qué libros se abren y se cierran.
- **Elipsis y subtexto.** Qué rastro deja el protagonista B en el espacio de la protagonista A (de su paleta, si la tiene) y, si ella lee esas marcas por oficio, de cuál le viene.
- **Elipsis y ritmo.** La extensión de sus capítulos en palabras.
- **Tests.** Quién investiga a la protagonista A en el test de asimetría, si alguien la investiga, y qué memoria audita el test de racionamiento, si la tiene.
- **Relación con otros archivos.** Cuántas elipsis mayores permanentes pasan de un libro a otro, quién completa la asimetría de INFORMATION_CHOREOGRAPHY y el techo de cruces de paleta por libro, si los tiene.

## CLUE_LEDGER

- **Cabecera: escala de la saga y trama horizontal.** Cuántos libros tiene la saga y, si tiene trama horizontal, qué hecho de ella tiene que moverse en cada libro.
- **Propósito: las capas y la firma en la obra.** Si los tiene, sobre qué hecho trata su trama horizontal, cuántos relojes lleva y a qué distancia suenan, y qué antagonista deja firma y con qué rastro.
- **La regla rectora en la obra.** Quién es su narrador hermético y cuánto calla, qué sabe de antes y qué reloj mueve esa ocultación, si lo mueve, la causa propia habitual de sus señuelos y, en la variante policial, dónde fija su biblia la arquitectura legal y por qué vías llega una pista sin petición.
- **Registro de pistas verdaderas: ficha, tabla y figura de la obra.** Qué vías de cobro tiene (en la variante policial, qué instituciones) y qué precio concreto tiene cada cobro, su tabla de pistas verdaderas y, si la tiene, su figura propia de pista con la frecuencia de uso.
- **Presupuesto de pistas a la escala de la obra.** La extensión y el número de capítulos de cada libro y su peso de pareja.
- **Pistas falsas: tabla y señuelo de la obra.** Sus señuelos de ejemplo (a quién incriminan, causa propia, siembra y desmentido) y cómo formula las reglas del señuelo que apunta a protagonista B.
- **Coartadas: tabla de la obra.** Las coartadas de ejemplo de sus sospechosos y cómo se rellena la fila fija de protagonista B.
- **Sospechosos: tabla, reparto y veto de la obra.** Sus sospechosos de ejemplo, su reparto de páginas y el defecto de protagonista A que no se activa con los sospechosos, con los planos en que sí.
- **La pista-espejo en la obra.** Dónde fija su biblia la regla del espejo, su ejemplo de pista-espejo y, si lo tiene, qué reloj recibe la pieza del coste.
- **La obligación de miga en la obra.** Si la saga tiene trama horizontal, sobre qué hecho de ella descubre protagonista A una pista en cada libro, y qué escena fija suya es también condición de entrega.
- **Test del objeto: ejemplos de la obra.** Sus ejemplos de lo que es miga y lo que no, y dónde guarda protagonista A los objetos.
- **Los canales de miga en la obra.** Qué guarda protagonista B y cómo lo obtuvo, si es canal; en la variante policial, qué deja ver el papel institucional de su antagonista; si lo tiene, qué personaje del elenco tiene acceso a los cuerpos o a los papeles (en la variante policial, su forense), cuándo ve y calla y qué migas técnicas aporta; y qué miembros del elenco pueden soltar datos.
- **Ficha de miga en la obra.** Los nombres de sus canales y, en la variante policial, los modos en que una miga le llega a protagonista A sin pedirla.
- **Registro acumulado de migas de la obra.** La miga de cada libro de la saga, con su canal y lo que abre, y en negrita lo que su biblia fija como canon.
- **Reparto de migas por arco en la obra.** Si los tiene, qué libros forman cada arco, en qué capa compone cada uno la trama horizontal y qué piezas concretas entrega.
- **Los relojes de la obra.** Si los tiene, cuántos relojes lleva la saga, qué cuenta cada uno, su ID y los libros en que empieza y suena.
- **Ficha de tic en la obra.** Cuál de sus relojes es el contable, si tiene uno, y qué piezas se cuentan en él.
- **Registro de tics y reglas de los relojes de la obra.** Los tics ya puestos en cada reloj y cuáles de sus relojes son el invisible y el contable, si los tiene, con sus libros y su ejemplo de cuenta en voz alta.
- **El antagonista de la firma en la obra.** Si lo tiene, quién es el antagonista de saga que deja firma, en qué libros actúa, en qué consiste su método y qué capacidad de la pareja hace falta contra él.
- **Ficha y reglas de firma en la obra.** Qué gesto compone la firma de su antagonista, en qué libro se revela, quién puede notarla y cuáles son sus dos primeros hechos firmados, con sus rasgos.
- **Calendario de datos horizontales en la obra.** De quién son los datos que protagonista A ya sabe y su ejemplo de dato aplazado a su capítulo, con la frase con que se alude antes.
- **Vetos de contabilidad en la obra.** Qué nombres e implicaciones tienen libro asignado y sus ejemplos de cada veto.
- **Errores comunes en la obra.** Los nombres, libros y cifras con que formula estos errores.
- **Tests en la obra.** Los nombres, libros y relojes con que formula estos tests.
- **Relación con otros archivos en la obra.** En qué libros revela su calendario largo y qué tipo propio de pista documental exige verificación.

## BRIEFING

- **Propósito en la obra.** Cuántos libros comparten su canon, cuál es el reloj que cerca a su pareja, si lo tiene, y qué canon suyo se redecide con más facilidad.
- **Condicionalidad en la obra.** La extensión de cada entrega y, si los tiene, cuántos relojes lleva su briefing de saga y cuál es el reloj que cerca a su pareja.
- **Canon heredado.** El valor fijo de cada fila de la tabla y la sección de su biblia de la que sale.
- **Reglas de actualización en la obra.** Cuántos volúmenes tiene la saga y, si lo tiene, cuál es el reloj que cerca a su pareja, que se vuelca al cerrar cada libro.
- **Declaración de instancia en la obra.** Sus arcos y, si las tiene, sus puertas de salida; un ejemplo canónico de tema y de trama derivada; los hitos de su escala de rendición; su lista de no negociables por libro y, si los tiene, de dónde salen sus migas y cuál es el reloj que cerca a su pareja.
- **Decisiones y pendientes en la obra.** Qué decisiones deja abiertas su canon, qué datos suyos rozan el canon y qué pendientes horizontales tiene, con su libro.
- **Bloques específicos de la obra.** Si los tiene, sus relojes con el libro en que arranca y suena cada uno, su techo de mezclas de paletas y de qué trata su inventario de migas; y los términos de su glosario.
- **Integración operativa en la obra.** Qué peso de pareja declara, cuáles son sus no negociables y, si los tiene, cuál es el reloj que cerca a su pareja y cuáles sus dos paletas.
- **Tests en la obra.** Quién entrega en su escala de rendición, qué no negociables vigila el TEST 7 y, si los tiene, sobre qué trata su miga y desde qué libro corre el reloj que cerca a su pareja.
- **Relación con otros archivos en la obra.** Cómo se llama su biblia, qué peso de pareja declara, cuántos volúmenes tiene y qué puertas de salida, si las tiene, y qué investigación lleva.

## SCALE_CALIBRATION

- **Declaración de escala.** La extensión por libro, el número y la banda de palabras de sus capítulos, su peso de pareja (objetivo y suelo, si sube alguno) y las cifras y excepciones del libro en curso.
- **Capítulo de una escena.** Si sus capítulos son de una escena, el techo y el suelo de su banda y la escaleta que fija el suelo.

## CHAPTER_BRIEF

- **Gancho de cierre.** La decisión de su biblia que fija el cierre en gancho sin excepción.

## CONTINUITY_PHYSICS

- **Casos del registro 13.** Los casos de su manuscrito que ilustran la comprobación de huecos sin narrar y el error de horas que dio origen al registro.

## SEAMS_AND_HINGES

- **Gancho sin excepción.** La sección de su biblia que ratifica el gancho en todos los capítulos.
- **Costura entre capítulos.** Quiénes son los narradores cuya alternancia hace de costura, si la tiene.

## TENSION_MECHANICS

- **La amenaza dentro de la pareja.** Cuál de los dos protagonistas es la fuente posesiva de peligro.
- **Catálogo de torturas.** En qué sección de su biblia está el catálogo de torturas al que pertenecen esas descargas falsas.

## SERIES_ARCHITECTURE

- **Declaración de la saga.** Su número de libros y de arcos, la pregunta central, la escala de rendición con el libro de cada peldaño (si la tiene), sus deudas de serie y relojes con su libro de pago, y dónde declara cada libro su arco de pareja y qué hace que el anterior no podía hacer.

## SERIES_GLUE

- **Forma de la saga.** Su forma (A, B o C), cuántos libros, qué cierra cada libro y qué deja abierto, dónde cae el final feliz y si cada libro es autónomo.
- **Puente entre libros.** Cómo pasa de un libro al siguiente (gancho de cierre, tiempo entre libros, epílogo-puente) y, si los tiene, los libros que cierran un arco con una puerta de salida limpia.
