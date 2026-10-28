# ¿Está la fábrica separada del producto?

**Auditoría de separación entre el MODELO_DarkRomance v2.0 (la fábrica) y *Madera y Pólvora* (el producto)**
Repo auditado: `Devpac/Dark`, rama `main`, commit `5d2bd13` (A110, biblia v4.14), 28-10-2026. También el repo `Devpac/maquetador` (`817ddb0`).
Método: un control mecánico (nombres, archivos citados, ranuras del preset) y seis lectoras sin contexto que leyeron enteros, línea a línea, los 47 archivos que el `LEEME.md` declara de modelo. Cada una tenía delante la huella de la obra (la tabla de roles del preset, los nombres y los rasgos). Sus lecturas están en `revisores/`.

---

## Veredicto

**Todavía no.** La fábrica está limpia en la superficie y contaminada por dentro.

- **En la superficie, sí.** En los 47 archivos de fábrica casi no aparecen nombres de la obra: ni Mara, ni Cruz, ni Salvat, ni Valdefuentes. El mecanismo del preset funciona: hay 172 punteros «Valores de la obra →» y todos llevan a una ranura que existe en `PLANTILLA_PRESET.md` y en el preset de la obra. Las bases de oficio (la parte v7 de cada plantilla) están limpias. Archivos que valen tal cual: `PLANTILLA_LIBRO`, `SCENE_SHAPE`, `VOICE_ARCHITECTURE` y casi todo `PLANTILLA_ESCALETA`.
- **Por dentro, no.** Las lectoras encontraron unos **250 hallazgos**. Casi ninguno es un nombre. Son **decisiones de diseño de *Madera y Pólvora* escritas como reglas del género o del subgénero**: se les quitó el nombre y se dejó el rol. Una saga nueva que clone el repo heredaría, sin saberlo, la trama de esta.
- **En el repo, no.** Fábrica y obra conviven en la misma raíz, sin carpetas. Para empezar otra saga hay que borrar a mano lo que diga la lista del `LEEME.md`, y esa lista ya se queda corta (no menciona `informes/`). El maquetador tiene el mismo problema.

## 1. Las tres capas del problema

### 1.1 Repo: fábrica y obra mezcladas

| | Fábrica | Obra |
|---|---|---|
| Dónde | Raíz de `Dark` (47 archivos) | Raíz de `Dark` (biblia, preset, cuaderno, NEXT) + `libro_01/`, `informes/`, `Referencia_Dark Romance/` |
| Separación | Solo una lista en `LEEME.md` §2 | Ídem |

- **`LEEME.md` es de la fábrica, pero su §1 guarda el estado de la obra:** la escaleta vigente, A99, las ramas archivadas. Cada mejora del modelo obliga a fusionarlo a mano.
- **`Referencia_modelo/`** (los restos de Intriga) está en la lista «se copia», así que cada saga nueva heredaría basura.
- **No hay versión de la fábrica independiente de la obra.** Las mejoras del modelo nacen y se registran dentro del repo de la obra (en las actas, en el cuaderno, en el §8 de la adenda). Si mañana hay dos sagas, no hay forma de pasarle a la segunda las mejoras de la primera.
- **Maquetador:** el código está limpio (*Madera y Pólvora* solo sale en comentarios), pero `obra/`, `portadas/` e `INSTRUCCIONES_GPT.md` son de la obra y viven en el mismo repo. Además no lee lo que produce el modelo v2: solo reconoce `capitulo_NN.md`, así que se salta `prologo.md` y `C10_capitulo.md`… También numera por el nombre del archivo, no por la numeración publicada, y apunta todavía a `MODELO_AGNOSTICO_v9Beta/Producto/libro_01`.

### 1.2 Superficie: limpia

- **Nombres:** cero fugas reales. Las coincidencias son el verbo «cruzar» y códigos de ejemplo (C01).
- **Archivos de la obra citados por la fábrica:** solo en `LEEME.md` §1, y por diseño.
- **Ranuras del preset:** las 172 existen.
- **Adendas de Intriga:** derogadas. Quedan menciones históricas en casi todas las adendas («deroga la adenda de Intriga», «AGATHA_ROSA»). No mandan, pero una ventana nueva las lee.

### 1.3 Por dentro: la obra codificada como regla

Por orden de gravedad.

**B · Trama de la obra disfrazada de regla de subgénero.** Es lo más grave porque no se ve: lleva la marca «*Variante: dark romance policial*» y parece legítimo. Pero otra saga policial no tendría por qué compartirlo. Es el diseño de esta.

| Lo que es de *Madera y Pólvora* | Dónde está escrito como regla |
|---|---|
| Las **cámaras** en el piso de ella y el móvil intervenido; ella lo descubre, le gusta, habla sola en voz alta para que él la oiga (*weaponized stalking*) | GENRE_CONVENTIONS (PELIGRO 2), HEAT_DISCIPLINE, RELATIONSHIP_PHYSICS, ROMANCE_BEAT_MAP, DIALOGUE_MECHANICS, BRIEFING, PLANTILLA_PRESET |
| La **arquitectura legal de Mara**: ella nunca pide, la negación plausible, «diseña su impunidad», le pasa los casos a él | ELLIPSIS_PROTOCOL (USO A, «el uso que define el archivo»), CLUE_LEDGER, DIALOGUE_MECHANICS, GENRE_CONVENTIONS (TEST 10), ROMANCE_BEAT_MAP, PLANTILLA_BIBLIA §11 |
| **Mara perfiladora**: seducción táctica de los sospechosos, el defecto que no se activa con ellos, los tres planos del Síndrome de la Restauradora | GENRE_CONVENTIONS (PELIGRO 1, TEST 9), CHARACTER_PHYSICS, DIALOGUE_MECHANICS, HEAT_DISCIPLINE, PLANTILLA_PRESET |
| **Bosch**, el investigador de Asuntos Internos | CHARACTER_PHYSICS («Regla de oro de Asuntos Internos», TEST 10 sin salida), PLANTILLA_PRESET |
| **Cruz**: sospechoso fijo de cada caso (un señuelo apunta siempre a él; no tiene coartada), operativo profesional («fría, táctica, sin huellas»), guarda el secreto horizontal | CLUE_LEDGER, ELLIPSIS_PROTOCOL, DIALOGUE_MECHANICS, INFORMATION_CHOREOGRAPHY, PLANTILLA_PRESET |
| **El Notario**: su firma, el expediente del padre como primer FN e Irene como segundo, los relojes «invisible» y «contable» (Quiroga y Bosch) | CLUE_LEDGER, PLANTILLA_PRESET |
| **Almenar**, la forense | CLUE_LEDGER («(la forense)», los cuatro canales de miga) |
| **El idiolecto de Cruz** como regla de todo narrador hermético: «la frase que enuncia una regla de trabajo» | PROSE_LINE_DISCIPLINE (TIC 4), SYSTEM_ORCHESTRATION (C-2) |
| **El remate de Mara** («giro irónico seco, en párrafo propio») | PROSE_LINE_DISCIPLINE |
| La **paleta olfativa por narrador** (sándalo y pólvora) comprobada siempre | SYSTEM_ORCHESTRATION (C-3) |
| La **evolución de la pregunta del libro 1** («sobre el otro» → «sobre uno mismo con el otro») como regla de todos los libros | THEMATIC_ENGINE |
| La **lectora externa «Lucía»** con los gustos de esta biblia (y la misma ciudad y el mismo nombre que un personaje, Lucía Ferrándiz) | PROTOCOLO_LECTURA §8 |

**A · Valores de la obra sin nombre.** Cifras y episodios: las 3–4 pistas, el 70 % y el 88 % de CLUE_LEDGER; «seis personajes como mucho» (A17); «caro en cuarenta fichas»; «si hay secuestro, dónde cae» (el secuestro del libro 21); el cajón del taller; «comisaría, taller» como trámites; Carmen Mola y Gómez-Jurado como comparables; «no contiene la palabra inspectora»; «el monstruo de los buenos»; ejemplos de diálogo sacados del manuscrito («—No vas a ir sola»); el diagnóstico 39 % / 9 de 47 / «80 % novela negra» en la cabecera de `PAREJA_PRIMERO`; la calibración de la lectora tipo («un punto por debajo») en el protocolo y en la plantilla del cuaderno.

**C · La forma de esta obra como arquitectura fija, sin salida.**
- **La pareja es ella y él**, él el hermético que se rinde y ella la que analiza. Está en todos los archivos y no deja hueco para M/M, F/F ni roles invertidos. Algunos textos sí tienen salida («si la obra no declara a B hermético»), pero el «ella/él» no la tiene en ninguno.
- **Dos narradores** en DIALOGUE_MECHANICS, AESTHETIC_REGISTER (el régimen «MIXTO por POV» como «declaración fijada, no hueco de instancia»), CHARACTER_PHYSICS, CLUE_LEDGER y la adenda de SYSTEM_ORCHESTRATION.
- **La vigilancia como motor:** «él, o su vigilancia» en la primera página, «aparatos en juego» en el volcado de saga.
- **La trama B es un caso que se cierra en cada libro** y es obligatoria (STORY_SPINE, SUBPLOT_ARCHITECTURE, THEMATIC_ENGINE). No vale para un dúo de mafia ni para un bully.
- **El mercado:** español de España, Amazon/KDP/KU, BookTok, «mujer de 20 a 40», 3,99 €, H.D. Carlton y J.T. Geissinger como tradición, la anti-firma de «dark romance importado» (que veta una saga de mafia ambientada en España). Está en AESTHETIC_REGISTER, PROTOCOLO_LECTURA, GENRE_CONVENTIONS y PLANTILLA_BIBLIA.
- **El criterio del autor de esta obra** («1.º el disfrute de la lectora…», «manda la lectora») está escrito en el modelo, en vez de leerse del cuaderno.
- **Recursos de la obra hechos obligatorios:** catálogo de torturas, regla de mortalidad, malla de mundos que rota cada libro, paletas por narrador, refugio sensorial, antagonista de saga por capas, relojes.

**D · Restos de modelos anteriores que siguen mandando.**
- `PROTOCOLO_CAPTURA_APRENDIZAJE.md` entero habla en términos de la v7 (sus reglas, su «documento de apertura», «cuando v7 evolucione hacia v8»).
- La base de `SYSTEM_ORCHESTRATION` sigue diciendo que el NEXT tiene seis secciones y que lo emite la ventana saliente. `PLANTILLA_NEXT` tiene ocho y lo escribe el orquestador, y la adenda no lo deroga.
- La base de `SYSTEM_ORCHESTRATION` también cita `MODELO_AGNOSTICO_v7_APERTURA.md`, que no está en el repo.
- `PROSE_LINE_DISCIPLINE` arrastra la cola de la cirugía v7.1: «este archivo no se modifica», `CIRUGIA_v7_REPORTE.md` (que no existe) y pendientes «diferidos» de ventanas 9 y 10.
- `REGISTROS_APRENDIZAJE` tiene el registro 002 sin procesar y con «implicación para v7».
- Historia de la obra y de las versiones en las cabeceras («nace del cap. 3 de la primera obra», «v1.1, 21-10-2026: un borrador de capítulo 1…», ramas `modelo-v1.3-final`).

## 2. Lo que decide el autor antes de arreglar nada

Hay cuatro preguntas que solo puedes contestar tú, porque dicen qué es la fábrica:

1. **¿El «pareja primero» con sus cifras (objetivo 80 %, suelo 70 %; cada voz al 40 %; ganchos de pareja dos de cada tres; gancho sin excepción) es la identidad de la fábrica o un valor de *Madera y Pólvora*?**
   *Recomendación:* que sea de la fábrica, como valor por defecto declarado y con la salida de `PAREJA_PRIMERO` §3 visible en cada test que lo mide. Es lo que hace que la v2 vaya «mejor de calle», y otra saga de dark romance lo querría igual. Lo que no es de la fábrica es el «40 % por voz»: eso es el reparto de esta obra y va a su preset.
2. **¿El criterio de delegación («1.º la lectora, 2.º la coherencia, 3.º la calidad; manda la lectora») es del método o tuyo para esta obra?**
   *Recomendación:* valor por defecto de la fábrica, que se lee del cuaderno de cada obra, así otra obra puede cambiarlo.
3. **¿Hasta dónde llega la fábrica?** ¿Solo dark romance en español para KU, o también otras lenguas, otros canales y parejas que no sean ella/él?
   *Recomendación:* dark romance de cualquier subgénero y pareja, con la lengua, el canal y el público como ranuras del preset (con los valores de hoy por defecto). Cuesta poco, porque es sobre todo cambiar «ella/él» por roles y mover el mercado al preset, y abre mucho.
4. **¿Cómo se separan físicamente?** Tres opciones:
   - (a) **Dos repos:** la fábrica en uno propio, limpio y con su versión, que se clona para cada saga; `Dark` se queda como el repo de *Madera y Pólvora*.
   - (b) **Un solo repo con dos carpetas** (`modelo/` y `obra/`).
   - (c) **Dejarlo como está**, arreglando solo el contenido.
   *Recomendación:* la (a). Es la única que cumple «clonar y empezar de cero» sin borrar nada a mano, y deja que las mejoras del modelo pasen de una saga a otra. Hay que hacerlo con el orquestador, porque cambia las rutas que leen sus ventanas.

## 3. Cuánto trabajo es

Con lo que ya hay, no hace falta reescribir ninguna base de oficio. El trabajo está en las adendas de dark romance y en las plantillas de fase.

| Zona | Qué hay que hacer | Tamaño |
|---|---|---|
| GENRE_CONVENTIONS (los dos peligros, TEST 9–10, la inversión clave), CLUE_LEDGER (impunidad, señuelo y coartada de B, canales, firma, relojes, cifras), CHARACTER_PHYSICS (Asuntos Internos, TEST 10, tres planos, R1–R5, colapso), ELLIPSIS_PROTOCOL (USO A, tipo 6), DIALOGUE_MECHANICS (pedir/enunciar, seducción táctica, la sala de la unidad) | Separar la convención del subgénero (se queda en la fábrica) del diseño de esta saga (va a su preset) | Grande: es reescribir las variantes |
| PLANTILLA_PRESET y PLANTILLA_BIBLIA | Reformular unas 30 ranuras y secciones en abstracto, con «si la tiene» | Medio |
| AESTHETIC_REGISTER, PROTOCOLO_LECTURA §3, §4 y §8 | Pasar el régimen, la lectora, los referentes, la lengua y el mercado a «por defecto, si la obra no declara otro» | Medio |
| Todas las adendas | Pasar «ella/él» a roles A/B (una línea de cabecera más los casos sin salida); trama B «si la tiene / donde la obra la cierre» | Medio, mecánico |
| SYSTEM_ORCHESTRATION (adenda, C-2, C-3, C-6, C-9b), PROSE_LINE (TIC 4) | Que lean del preset los valores de esta obra | Pequeño |
| Restos v7/Intriga | Reescribir PROTOCOLO_CAPTURA_APRENDIZAJE; derogar en la adenda el NEXT de seis secciones y BRIEFING como archivo; borrar la cola v7.1 de PROSE_LINE; mover la historia a un changelog | Pequeño |
| LEEME §1 | Dejarlo en un puntero al cuaderno | Pequeño |
| Maquetador | Separar `obra/` y `portadas/`; leer `prologo.md` y `C<NN>_capitulo.md`; numerar por la tabla de correspondencia de la escaleta | Pequeño–medio |

**Condición para no romper la obra:** cada valor que salga de la fábrica tiene que estar ya en `PRESET_MADERA_Y_POLVORA.md` o en la biblia. Las lectoras comprobaron que casi todos lo están, porque la plantilla lo copió de ahí. Los que no, se añaden al preset antes de cortar la plantilla. Así las ventanas de *Madera y Pólvora* siguen leyendo lo mismo.

**Cómo comprobar el resultado:** cuando esté hecho, la prueba es la misma que ya usó la v1.3 («saga nueva de otro subgénero», 7/10). Se clona solo la fábrica y una ventana sin contexto arranca la fase 0 con una premisa distinta, por ejemplo un dúo de mafia M/M en tercera persona. Una lectora busca en lo que produce rastros de *Madera y Pólvora*.

---

*Lecturas completas, con archivo, línea y arreglo propuesto para cada hallazgo:* `revisores/G1_orquestacion.md` a `revisores/G6_oficio_base.md`.
