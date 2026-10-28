# Guía de la cirugía (paso 2) — de MODELO_DarkRomance v2.0 a Fábrica v3.0

**Qué se busca:** que la fábrica de `Editorial/fabrica/` sirva para cualquier saga de romance (dark romance de cualquier subgénero, romantasy, dark academia…), sin heredar nada de *Madera y Pólvora* (MyP), **y sin tocar lo que ha dado la buena prosa**.
**Qué se arregla:** los hallazgos de `auditorias/2026-10-28_separacion/` (el `INFORME.md` y las seis lecturas en `revisores/`).
**Punto de partida:** la v2.0 en capas, idéntica byte a byte al modelo con el que se escribe MyP (`historia/ORIGEN.md`). Copia de referencia montada (solo lectura): `/tmp/claude-0/-home-claude/b9398d74-6bbd-5b28-b56a-1d8c19f63593/scratchpad/montado/`. Los números de línea de las lecturas son los de esa copia montada.

## 1. Decisiones del autor (28-10-2026) que mandan sobre la auditoría

1. **«La pareja primero» es la identidad de la fábrica.** Se quedan como valores por defecto de la fábrica: objetivo 80 % / suelo 70 % de pareja, el caso con techo del 30 %, los suelos de `PAREJA_PRIMERO.md` §3, ganchos de pareja (dos de cada tres; objetivo, tres de cada cuatro) y gancho en todos los cierres. Donde un test los mide, debe remitir a «los de `PAREJA_PRIMERO.md` §3 o los que declare el preset»; el gancho sin excepción pasa a «por defecto; la obra puede declarar cierres de descarga con su tope». **No es de la fábrica** el «40 % por voz» (es el reparto de MyP): sale al preset.
2. **El criterio de delegación** («1.º el disfrute de la lectora, 2.º la coherencia de la saga, 3.º la calidad literaria»; «manda la lectora») es el valor por defecto del método; cada obra lo declara (o lo cambia) en `CUADERNO_<OBRA>.md` §2, y el método lo lee de allí.
3. **Mercado y lengua:** por defecto, español de España; Amazon KDP con Kindle Unlimited; lectora de dark romance (mujer de 20 a 40, KU, BookTok, Bookstagram); 3,99 €. Cada obra lo declara en `PRESET_<OBRA>.md` › Cabecera › Mercado y lengua. Las plantillas no repiten estos valores: remiten a esa ranura.
4. **Alcance:** cualquier pareja (no solo ella/él) y cualquier subgénero de romance. Lo propio del dark romance se queda en `generos/dark_romance/`; lo del subgénero policial, bajo la marca «*Variante: dark romance policial*»; lo de MyP, fuera de la fábrica.

## 2. Lo que NO se toca (lo que ha dado la buena prosa)

- **La regla del fork:** ninguna instrucción nueva antes de escribir. La cirugía solo **corta, condiciona o generaliza**; no añade reglas de prosa.
- **El método:** orquestador y ventanas, brief de una hoja → escritura libre → cierre obligatorio (OPERACIÓN C y sus comprobaciones C-1 a C-10) → lectura C.5 por quien no escribió → cortes. Se conservan todas las comprobaciones; solo cambia que los **valores** que traían de MyP los lean del preset.
- **Las bases de oficio** (la parte de cada plantilla de `oficio/` y la base de `metodo/SYSTEM_ORCHESTRATION.md`): no se tocan, salvo los restos de v7 que la auditoría marca como D (cola de cirugía v7.1 de PROSE_LINE, los cinco modos de VOICE, «cinco a seis ejes» de WORLD_ARC, el NEXT de seis secciones) y las cabeceras de historia.
- **Los encabezados (`##`, `###`)**: las plantillas y el preset se apuntan por nombre de sección. No se renombra ninguno salvo que el hallazgo lo pida (p. ej. «Regla de oro de Asuntos Internos» → «Regla de oro del perseguidor legítimo»); cada renombre va al registro de ranuras con nombre viejo → nuevo.
- **El tono y la forma de los archivos.** Arreglo mínimo: «cortar antes que añadir». Nada de reescribir párrafos que no tienen hallazgo.

## 3. Cómo se arregla cada tipo de hallazgo

- **B (trama de MyP disfrazada de regla) y A (valor de MyP):** se quita de la fábrica. Si debajo hay una convención de verdad del género o del subgénero, se deja **solo la convención**, en abstracto, con «si la obra lo declara» y el puntero a su ranura. El contenido concreto va al preset de la obra (ver §5). Un ejemplo útil se puede quedar si es **neutro** (no de MyP) y va marcado como ejemplo.
- **C (supuesto de forma sin salida):** se le pone la salida: «si la obra lo tiene», «con dos narradores», «quien declare la obra»… sin cambiar la regla para el caso por defecto.
- **D (historia, restos):** la regla se queda; la anécdota o la historia sale de la regla y se copia a tu registro de historia (§5) para el `CHANGELOG.md`. Un resto de v7/Intriga que **sigue mandando** se deroga o se reescribe (lo dice cada lectura).
- **Roles «ella/él».** No se reescriben todos. En la **cabecera de cada plantilla de género y de cada adenda** que use «ella/él» se añade, tal cual, esta línea (una sola vez por archivo, justo debajo del título o del encabezado de la adenda):

  > *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

  Y se arreglan, uno a uno, los sitios donde «él» o «ella» **fija un papel** sin salida: quién se rinde o raciona su confesión, quién es el hermético, quién vigila, quién es peligroso, quién está del lado de la ley, quién guarda el secreto horizontal. Ahí se escribe el rol («el protagonista que se rinde (lo declara la obra)», «protagonista B»…).
- **Cifras de MyP** (3–4 pistas, 70 %/88 %, seis personajes, cuarenta fichas…): fuera; la regla dice «a la escala que declare la obra» y apunta a su ranura.

## 4. Ranuras del preset

- **Ranuras comunes (nombres exactos):**
  - `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles — quién es cada rol, los géneros de la pareja, quién narra, quién es hermético o irónico (si alguno), quién raciona su rendición, quién vigila (si alguien), quién está del lado de la ley (variante policial).
  - `PRESET_<OBRA>.md` › Cabecera › Mercado y lengua — lengua y variedad, plataforma y canal, público, precio, comparables y tradición de referencia, perfil de lectora externa.
- **No edites a mano las secciones por plantilla de `PLANTILLA_PRESET.md`** («Las demás plantillas»): son copia literal de la línea «*Qué declara aquí la obra:*» de cada plantilla y se regeneran al final con un script. Para cambiar una ranura, cambia **el bloque «Valores de la obra →» de su plantilla**. Para crear una ranura nueva, añade el bloque en la plantilla con el mismo formato:

  ```
  > **Valores de la obra →** `PRESET_<OBRA>.md` › <PLANTILLA> › <Ranura>.
  > *Qué declara aquí la obra:* <qué decide la obra, en abstracto; «o "no aplica"» si puede no tenerlo>.
  ```
- Las lecturas de PLANTILLA_PRESET (`revisores/G2_plantillas_fase.md`) que hablan de ranuras de otra plantilla las arregla **el dueño de esa plantilla**, en su bloque.

## 5. Lo que deja cada cirujano (en `cirugia/`)

1. **`traslados/G<n>.md` — lo que sale de la fábrica y dónde vive en MyP.** Una fila por cosa que quitas de la fábrica que sea de MyP (B, A y los valores de C):

   | Archivo de la fábrica | Qué sale (≤ 15 palabras) | Dónde lo tiene MyP | Estado |
   |---|---|---|---|

   - «Dónde lo tiene MyP»: la sección del preset (`/home/claude/dark/PRESET_MADERA_Y_POLVORA.md`, rama `main`) o de la biblia (`/home/claude/dark/madera_y_polvora_biblia.md`), con una cita corta que lo pruebe (búscalo con `LC_ALL=C.UTF-8 grep`).
   - «Estado»: **«en el preset»**, **«en la biblia»** (cuando debería estar también en el preset para que una ventana lo lea, dilo), o **«FALTA»**: entonces escribe debajo de la tabla el texto exacto que habrá que añadir al preset de MyP al migrar, y en qué ranura. Esto es lo que garantiza que MyP no pierda nada.
2. **`ranuras/G<n>.md`** — ranuras nuevas, renombradas o eliminadas: `PLANTILLA › Ranura` — qué declara — nuevo / renombrada (antes «…») / eliminada.
3. **`historia/G<n>.md`** — las frases de historia que saques de las reglas, con su archivo, para el `CHANGELOG.md`.
4. **Tu informe final** (en tu respuesta): por archivo, qué hallazgos arreglaste, cuáles no y por qué (si discrepas de la lectura, dilo: no se arregla lo que no es fuga).

## 6. Reglas de trabajo

- **Edita solo tus archivos**, en sus capas de `/home/claude/editorial/fabrica/`. Cada plantilla puede estar partida: la base en `metodo/` u `oficio/` y su adenda en `generos/dark_romance/adendas/<mismo nombre>`; las plantillas enteras de género, en `generos/dark_romance/plantillas/`. No edites la copia montada ni nada en `/home/claude/dark` (solo lectura). No hagas commits.
- Al terminar, monta y comprueba:
  ```
  cd /home/claude/editorial && python3 -I herramientas/montar.py --destino /tmp/claude-0/-home-claude/b9398d74-6bbd-5b28-b56a-1d8c19f63593/scratchpad/montado_G<n>
  ```
  y busca en tus archivos montados que no quede nada de la huella de MyP (`scratchpad/huella_obra.md`): `LC_ALL=C.UTF-8 grep -n -E 'Mara|Cruz|Salvat|Bosch|Almenar|Quiroga|Notario|Sarasola|Valdefuentes|sándalo|SAC\b|UAI\b|Asuntos Internos|cámaras|forense' <archivos>` (con criterio: «cruzar» y lo que sea convención legítima del subgénero policial pueden quedarse).
- Un archivo empieza con la línea `# NOMBRE.md — MODELO_DarkRomance v2.0`: déjala (el cambio de nombre a Fábrica v3.0 se hace al final, de una vez).
