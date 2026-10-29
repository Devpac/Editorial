# Migración de *Madera y Pólvora* a la Fábrica v3.0

**Cuándo:** al abrir el libro 2 (paso al libro siguiente, `ORQUESTADOR.md` §2.7). El libro 1 se termina con la v2.0 de `Devpac/Dark`.
**Objetivo:** que las ventanas de MyP lean con la v3.0 **exactamente lo mismo** que leían con la v2.0. Todo lo que la cirugía sacó de la fábrica por ser de MyP tiene que estar en el preset de MyP (o en su biblia o su cuaderno, donde la fábrica lo busca ahora).
**De dónde sale:** los registros de traslado de los seis cirujanos (`traslados/G1.md` a `G6.md`): unas doscientas filas, de las que la gran mayoría ya estaba en el preset de MyP (la plantilla lo había copiado de allí cambiando nombres por roles). Lo que sigue es lo que **no** estaba, o lo que cambia de nombre. Números de línea del preset y la biblia de `Devpac/Dark` a 28-10-2026.

## 1. Cabecera del preset (estructura nueva)

- El párrafo de cabecera actual (l. 27–32, «**Obra:** *Madera y Pólvora* · …») pasa bajo `## Cabecera`.
- La `## Correspondencia de roles` actual (l. 42) baja a `### Correspondencia de roles` dentro de `## Cabecera` (las plantillas la citan como «Cabecera › Correspondencia de roles»), con estas filas nuevas al final de su tabla:

  | En las plantillas | En *Madera y Pólvora* |
  |---|---|
  | Géneros de la pareja | ella (Mara) y él (Cruz): «ella» y «él» de las plantillas valen tal cual |
  | Quién narra | los dos, en primera persona y presente, alternos (el reparto, «Cruz cerca de la mitad; ninguna voz por debajo del 40 %», ya está en › SYSTEM_ORCHESTRATION › Extensión, persona y narradores, que es la ranura que lo declara) |
  | Quien raciona su rendición o su confesión (la escala de rendición) | Cruz (biblia §16.3; CHARACTER_PHYSICS › Ficha A2) |
  | Quién da miedo | Cruz (biblia §2, pilar 5, y §3: «la intensidad de Cruz») |
  | Quién vigila | Cruz: las cámaras y el micrófono del piso de Mara, y el móvil (biblia §15.2 y §12.4; desde el cap. 12 del libro 1) |
  | Quién guarda el secreto de la trama horizontal | Cruz: lo que sabe del padre de Mara (RELOJ-C, biblia §13; §8.1.1 y §8.5) |
  | Negación plausible (ELLIPSIS_PROTOCOL, USO A) | sí: Cruz actúa fuera del plano de Mara, y ella no pide nunca (biblia §11.3) |
  | Quién está del lado de la ley (variante policial) | Mara, inspectora de la SAC |
  | Quién de la pareja tiene equipo institucional | Mara: la SAC |
  | Quién descubre la miga | Mara (biblia §8.5) |

- Ranura nueva `### Mercado y lengua`:

  > - **Lengua y variedad:** español de España (biblia §21; cabecera: «Mercado objetivo: España e Hispanoamérica»).
  > - **Plataforma y canal:** Amazon KDP con Kindle Unlimited; la muestra gratuita es la de Amazon (A84). Título y subtítulo de tienda, siete palabras clave y categorías: biblia §5.3–§5.5 (nunca Novela negra / Policíaca / Misterio).
  > - **Público lector:** mujer de 20 a 40 años, lectora intensiva de KU, consumidora de BookTok y Bookstagram, que lee en el móvil, de noche, a velocidad alta (biblia §4.3).
  > - **Precio:** 3,99 € fuera de KU (el de las lecturas externas, A86; la biblia no fija precio: **confirmar con el autor**).
  > - **Comparables y tradición de referencia:** H.D. Carlton, J.T. Geissinger y J.D. Robb (*In Death*, por la serialidad, no por el reparto entre pareja y caso); se huye de Gómez-Jurado, Carmen Mola, Lorenzo Silva, Alicia Giménez Bartlett y Dolores Redondo (biblia §4.1, §4.2 y §21).
  > - **Perfil de lectora externa** (`[PERFIL DE LECTORA EXTERNA]`, `[NOMBRE]`, `[SU RED]` de `PROTOCOLO_LECTURA.md` §8), literal, el que salió de la fábrica: «Lucía, 31 años, de Valencia. Lees unos ocho libros al mes de dark romance en Kindle Unlimited y en papel. Tus favoritas son Penelope Douglas, Rina Kent, H.D. Carlton, Ana Huang, Sophie Lark y Mercedes Ron; también lees romántica española en Wattpad y Amazon. Tienes una cuenta de BookTok con unos 15.000 seguidores donde reseñas sin filtro. Abandonas un libro en cuanto te aburre y no te da pena decirlo. Te encantan el stalker con código, el *morally grey*, el *slow burn* que paga y las heroínas con carácter. Odias el relleno, las protagonistas tontas, los héroes que no dan miedo de verdad y la prosa que se escucha a sí misma.» `[NOMBRE]`: Lucía. `[SU RED]`: BookTok; la reseña negativa, en Goodreads; lee «en el Kindle».

## 2. Ranuras que cambian de nombre

| Sección del preset de MyP | Antes | Ahora |
|---|---|---|
| SYSTEM_ORCHESTRATION (l. 98) | `### Doble hélice (§5)` (y se borra la nota «la ranura conserva su nombre de la v1.3», l. 100) | `### Peso de la pareja (§5)` |
| CHARACTER_PHYSICS (l. 816) | `### Regla de oro de Asuntos Internos` | `### Regla de oro del perseguidor legítimo` |
| SEAMS_AND_HINGES | `### Gancho sin excepción` | `### Gancho en todos los cierres` (MyP no declara cierres de descarga: todos en gancho, A82; biblia §20.1) |
| PROSE_LINE_DISCIPLINE (l. 1729) | `### Las dos voces` | `### Las voces` |

## 3. Lo que hay que añadir a ranuras que ya existen

1. **PROSE_LINE_DISCIPLINE › TIC 4: glosa y remate**, al final del párrafo «En Cruz: …» (l. 1748–1751):
   > *(v2.0)* Se conserva también la que enuncia **una regla que se impone respecto a ella** («Lo que pidan de ella, a mí.», acta del C10; «Si alguien la sigue, no llega a la autovía», acta del C12): es su forma de pensar, no una glosa. Fuera de estas dos, en su POV se corta toda frase que explique.
2. **CLUE_LEDGER › Presupuesto de pistas a la escala de la obra** (l. 2232–2238), al final:
   > **Trazabilidad del cobro (TEST 4):** cada pista cobrada después del 88 % del manuscrito tiene siembra registrada antes del 70 %. Si no, deus ex machina.
3. **ELLIPSIS_PROTOCOL › Propósito**, al principio:
   > Lo que Cruz hace en página: mata, tortura y manipula en página, también pruebas (biblia §15.3).
4. **DIALOGUE_MECHANICS › Tests de funcionamiento**:
   > TEST 12 — SU SOMBRA EN LA PÁGINA DE ELLA. El rastro de Cruz en la página de Mara: lo que ella sabe o teme que él ve u oye (las cámaras, el micrófono), un mensaje, lo que se calla por él; en la seducción táctica, su reacción, en la página de ella y no solo en el capítulo de él.
5. **SERIES_ARCHITECTURE › Declaración de la saga**, en la línea de la escala de rendición:
   > El arco de Mara, en la forma A, se mide en lo que se descubre dispuesta a ser o a hacer.
6. **PROTOCOLO_LECTURA › Lectura externa**: «Lucía, tal cual.» pasa a «El perfil, en Cabecera › Mercado y lengua.»; a las preguntas se suma la de §8, punto 3: «¿Él da miedo? ¿Ella te cae bien o te desespera?», y la del libro siguiente en la lectura de plan (§6 bis): «¿Te da miedo él?» (en la v2.0 la traía fija el protocolo; la v3.0 la lee de aquí).
7. **Los cierres de descarga, en una sola ranura.** En la v3.0 solo los declara › SEAMS_AND_HINGES › Gancho en todos los cierres (renombrada, §2), que en MyP dice «ninguno: todos los cierres en gancho (A82; biblia §20.1)». Las otras dos secciones de MyP que hoy lo repiten dejan de declararlo:
   - **SYSTEM_ORCHESTRATION › Gancho y primer capítulo:** la línea «Gancho sin excepción: biblia §20.1 y A82…» pasa a «Los cierres: › SEAMS_AND_HINGES › Gancho en todos los cierres». La cuota de ganchos de pareja («al menos dos de cada tres; objetivo, tres de cada cuatro…») se mueve a › SYSTEM_ORCHESTRATION › Peso de la pareja. El primer capítulo se queda donde está.
   - **CHAPTER_BRIEF › Gancho de cierre:** «no aplica: los cierres, en › SEAMS_AND_HINGES › Gancho en todos los cierres; la cuota de ganchos de pareja, en › SYSTEM_ORCHESTRATION › Peso de la pareja».
8. **SYSTEM_ORCHESTRATION › Instancia y canon oculto**: añadir «Las preguntas de procedimiento no bloquean la escritura (criterio del autor desde V-10)», que ahora es la ranura donde la fábrica lo busca (RESEARCH_LEDGER, adenda).

## 4. Secciones nuevas del preset (añadirlas también al índice)

1. **`## PROTOCOLO_LECTURA` › `### Listón de comparaciones`**
   > Español: comparaciones con «como» (como si, como quien, como un…) por debajo de unas 5 por 1.000 palabras, medidas con la expresión de `PROTOCOLO_LECTURA.md` §2 (el valor por defecto).
2. **`## THEMATIC_ENGINE` › `### Evolución de la pregunta`** (después de `## TENSION_MECHANICS`)
   > - **Libro 1** (biblia §26, A93 y A94): Acto I, sobre el otro (quién es, qué quiere, hasta dónde dejarle llegar): «¿Qué es él para ella: testigo, sospechoso, aliado, amenaza o las cuatro cosas?» → Acto II, sobre ella con él (qué está dispuesta a ser o a hacer por él, o contra él): «¿Qué está dispuesta a callar por él?» → Acto III: «¿Puede Mara quererlo sin convertirse en su coartada?». Ninguna de las tres es sobre el caso («qué está pasando aquí»).
   > - **En serie:** la formulación final de cada libro abre el siguiente (A61). Cada libro declara la suya al diseñarse (biblia §26; BRIEFING, arco de pareja del libro).
   > - **Forma por defecto de cada libro** (la que la v2.0 daba a todos): Acto I sobre el otro (quién es, qué quiere, hasta dónde dejarle llegar) → Acto II sobre ella con él (qué está dispuesta a ser o a hacer por él, o contra él), salvo que el diseño del libro declare otra.
3. **`## SUBPLOT_ARCHITECTURE` › `### Trama B`**
   > - **Cada libro tiene trama B propia:** el caso del libro, autoconclusivo; se abre y se cierra dentro del volumen (biblia §17, punto 1; v4.0: es la trama B, cabe en el techo del 30 % y lo resuelve una decisión de la pareja). Ningún libro va «sin trama B propia».
   > - **Dónde se cierra:** en el libro (forma A: › SERIES_GLUE › Forma de la saga, «Cada libro cierra su caso»). Lo que cruza libros es la trama horizontal, no la trama B.
4. **`## WORLD_TEXTURE` › `### Léxico y glosario`**
   > - **Época y oficios del léxico:** España actual (biblia §25); el oficio de la trama B es el policial (SAC), el forense y el judicial.
   > - **Tecnicismo:** llano, sin tecnicismo forense, legal o clínico denso; el tecnicismo denso es alarma de cierre (› PROSE_LINE_DISCIPLINE › Anti-firma; biblia §15.5).
   > - **Densidad de los escenarios:** la de Madrid, el taller-dojo, la SAC y el corredor mediterráneo, bajo el umbral del paisaje lírico.
   > - **Glosario:** `ESTRATEGIA 0` dominante (el término se entiende por contexto, sin glosa del narrador), con un tramo de despliegue único: cada sigla del Anexo D se despliega una vez, en boca de quien la usa; sin glosario ni paratexto en los libros (biblia §28, A63; Anexo D, A64).

## 5. Cuaderno de MyP

- **§2:** el criterio de delegación y «manda la lectora» ya están entre las decisiones permanentes del autor; con la v3.0, el método los lee de ahí (`PLANTILLA_CUADERNO.md` §2): comprobar que están con las dos líneas que pide la plantilla.
- **§5 (notas del libro en curso):** añadir «La lectora tipo es exigente y oscila alrededor de un punto entre lecturas: se mira su orden, no un número suelto» (estaba en `ORQUESTADOR.md`; la v3.0 lo deja como regla general, «se mira su orden», sin la cifra).
- **§7 (índice):** `Referencia_modelo/` deja de ser parte del modelo; si se queda en Dark, va al índice como histórico («el modelo de Intriga del que salían las adendas que la v2.0 derogó; solo traza»).

## 6. Lo que MyP leerá distinto (a propósito)

- **REVISION_PROTOCOL (a):** la alarma «capítulo sin el otro en escena ni en directo» ahora es simétrica: también salta con un capítulo de Cruz sin Mara (antes solo con uno de Mara sin Cruz). Es más estricta, no peor; los capítulos de Cruz que la miran en directo (las cámaras) no la disparan.
- **El glosario:** con la v2.0, MyP leía la ESTRATEGIA 2 de la fábrica; con la v3.0 lee la `ESTRATEGIA 0` que declara su biblia (§4.4 y pregunta 1 de §7).

## 7. Preguntas para el autor (no bloquean la migración)

1. **Glosario:** la biblia de MyP declara `ESTRATEGIA 0`, que la plantilla WORLD_TEXTURE no define (tiene 1, 2 y 3; la adenda de la v2.0 decía 2). Con la v3.0 manda lo que declare la obra, así que MyP sigue con la suya; ¿se añade una ESTRATEGIA 0 a la fábrica, o MyP declara la más cercana?
2. **Lucía:** el nombre y la ciudad de la lectora externa coinciden con Lucía Ferrándiz, de la Consignataria del puerto de Valencia (biblia l. 2041). La fábrica ya no la lleva; en MyP, ¿se queda o se cambia?
3. **Precio** de las lecturas externas: 3,99 € (no lo fija la biblia).

## 8. La estructura del repo y la publicación

Con la v3.0, la fábrica de una saga vive en `fabrica/` y la obra en la raíz (`ARRANQUE.md`). En `Devpac/Dark`, al migrar:

1. **La fábrica a `fabrica/`:** se borran de la raíz los 47 archivos de modelo (la lista de `historia/ORIGEN.md`) y se monta `python3 -I Editorial/herramientas/montar.py --genero dark_romance --destino Dark/fabrica`. Quedan en la raíz solo los de la obra.
2. **El `LEEME.md` de la raíz** pasa a ser el de la obra (el de `plantilla_saga/LEEME.md`, con `{{OBRA}}` = `MADERA_Y_POLVORA`), en lugar del de la fábrica.
3. **`Referencia_modelo/`** sale de la raíz de Dark o se queda como histórico de la obra (§5); la traza ya está en Editorial (`historia/Referencia_modelo/`).
4. **La publicación:** `Dark/publicacion/` recibe de `Devpac/maquetador` `obra/serie.yaml` y `obra/libro_NN.yaml` (con `capitulos: ../libro_01` y su `orden:`), `portadas/` (las instrucciones de la saga y las imágenes) y, si hay, fuentes propias en `publicacion/fuentes/`. El código pasa a ser el de `Editorial/maquetador` (mismo resultado, comprobado el 29-10-2026), y `Devpac/maquetador` queda como archivo.
5. **El cuaderno** apunta la versión montada (`fabrica/_FABRICA.txt`) y la fecha.

La publicación del libro 1 no tiene que esperar a la migración: `Devpac/maquetador` sigue funcionando tal cual.

## 9. Cómo se comprueba la migración

Una correctora sin contexto monta la v2.0 (`Devpac/Dark`, `fcd6839`, o `herramientas/montar.py` sobre el commit del paso 1 de Editorial) y la v3.0, cada una con su preset de MyP, y comprueba, plantilla por plantilla, que lo que una ventana de capítulo de MyP lee es lo mismo. Lo que falte, al preset antes de lanzar ninguna ventana del libro 2.
