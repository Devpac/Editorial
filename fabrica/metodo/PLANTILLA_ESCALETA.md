# PLANTILLA_ESCALETA.md — escaleta y escaleta ampliada de un libro (MODELO_DarkRomance v2.0)

> Archivo de **modelo**. La parte 1 es la escaleta del libro (ventana E1, fase 2); la parte 2, la
> escaleta ampliada (ventanas A1, A2…, fase 3). Los **tests** del final los aplica la auditoría,
> no quien escribe. Desde la v2.0, la escaleta es de la pareja (`PAREJA_PRIMERO.md`): cada ficha
> empieza por «Entre ellos» y estima su peso.
>
> *Roles:* «ella» y «él» son la protagonista A y el protagonista B por defecto; la obra declara su pareja en `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles (`PAREJA_PRIMERO.md`, «Roles»).

---

## PARTE 1 — `libro_NN/escaleta.md`

### Cabecera

- Título del libro y número en la saga.
- **Extensión**: palabras (horquilla), número de capítulos, capítulos de una escena o de varias,
  suelo y techo por capítulo y excepciones (el capítulo largo del pico, el más hablado).
- **Persona, tiempo y narradores**: reparto entre narradores (con más de uno, el que declare la
  obra: `PRESET_<OBRA>.md` › Cabecera › Correspondencia de roles);
  capítulos partidos (empieza uno y termina el otro).
- **Peso de la pareja**: el declarado (biblia §14 🔒 y preset; por defecto, objetivo 80 % y suelo
  70 % por bloque de cuatro capítulos y por libro, en palabras medidas con `PAREJA_PRIMERO.md` §2)
  y el que suman las fichas, por bloque y por libro.
- **Calendario**: de qué día a qué día (las fechas no tienen por qué salir en página).
- **De dónde arranca** (libro 2 y siguientes): el estado de cierre del libro anterior
  (`libro_<N-1>/continuidad.md`), cuánto tiempo ha pasado y qué ha cambiado en ese tiempo.
- **Cómo queda todo al cerrar**: dos o tres líneas: dónde está la pareja, qué sabe cada uno y qué
  sabe la lectora.

### 1. El libro en una página

Una frase-tema entre comillas, sobre los dos. **Entre ellos:** de dónde a dónde van en este
libro; qué no consigue clasificar ella de él (o al revés) y por qué; quién gana y qué le cuesta al
otro. Las heridas que corren por debajo. **La droga del libro**: la asimetría de información que hace que la
lectora mire con uno lo que el otro no sabe (con un solo narrador, lo que la lectora sabe y quien
narra no). Después, la trama del libro (*Variante: dark romance policial:* el caso) en una línea: qué los junta, qué los enfrenta y qué los separa.

### 2. La pregunta que tira del libro

**La pregunta de la pareja**, cerrada (la del diseño del libro, biblia §19), y cómo cambia la
ventaja entre ellos capítulo a capítulo hasta que se cierra. Por qué no se resuelve antes (las
razones que la lectora se preguntará). La pregunta de la trama del libro la refleja y no la
sustituye (THEMATIC_ENGINE, adenda): una línea.

### 3. Escaleta, por actos

Cada acto con su título y una línea de calendario. Cada capítulo:

```
**N · NARRADOR — día, hora si importa** *(partido / sin diálogo / el más largo…)* · los dos: sí/no · pareja ≈ NN %
*Entre ellos:* qué cambia entre los dos en este capítulo, en hechos (vacío: el capítulo se funde con otro).
Un párrafo: dónde, quién, qué pasa, cómo gira.
*La trama B* (si la hay): qué beat mueve y en qué se convierte entre ellos (choque, proximidad forzada, obstáculo o moneda).
*Cierra con:* el gancho.
```

*(v2.0)* «Los dos»: si comparten escena en algún momento del capítulo. «Pareja»: el peso estimado,
con la unidad de `PAREJA_PRIMERO.md` §2 (la sombra que no ocupa a quien narra no cuenta). Cada
bloque de cuatro capítulos (1–4, 5–8…) cierra con una línea: su peso estimado, ponderado por las
palabras previstas, y los capítulos sin los dos en escena.

Los saltos de tiempo largos entre capítulos se dicen en cursiva entre las fichas («Entre el N y el
N+1 pasan seis días; no ocurre nada que el libro vaya a necesitar»).

### 4. Lo que corre por debajo

Las líneas que atraviesan el libro, cada una con los capítulos donde asoma; primero, las de la
pareja: **las barreras que caen** (y en qué capítulo cede cada uno), **el trato** (tú/usted,
nombres, apodos, cuándo cambia), las marcas físicas que vuelven; después, la herida de cada uno, los
secundarios con su cadencia, los capítulos sin diálogo, quién pone el alivio y cuándo.

### 5. Reglas de este libro

Las que solo valen para este volumen: los contadores (cuántas veces aparece una señal), lo que no
pasa nunca en este libro, el calendario de calor del libro (cada beat con su % y su suelo:
HEAT_DISCIPLINE, calendario de calor), los suelos de pareja que el libro sube (o que el autor baja,
con su decisión de la biblia), qué palabras no salen, si hay fechas en página, si el libro vuelve
atrás en el tiempo.

### 6. Antes de escribir

Lo que ya está escrito y manda sobre la escaleta; **investigación que bloquea capítulos concretos**
(y cuáles) y la que conviene pero no para la escritura.

---

## PARTE 2 — `libro_NN/escaletaAmpliada.md`

Cabecera igual que la escaleta (extensión, narradores, calendario) y una línea: «Si alguna vez
choca con la escaleta, manda la escaleta».

Cada capítulo, en este orden:

```
**N · NARRADOR — día, hora** · los dos: sí/no · pareja ≈ NN %

*Entre ellos.* Qué cambia entre los dos, en hechos; si el otro no está en escena, dónde está (en
directo, o en qué ocupa a quien narra).

*Dónde y con quién.* El sitio con dos o tres detalles que se puedan usar y quién está.

*La escena.* Cómo avanza hasta su golpe: «Aquí aprieta: …» y «El capítulo gira cuando …».

*La trama B* (si la hay). Qué pone y en qué se convierte entre ellos.

*Lo que sabe la lectora.* Lo que sabe ella que los personajes no, y con qué sale.

*Trato.* Tú o usted, nombres y cómo se llaman en la cabeza de cada uno.

*No hace.* Lo que el capítulo no puede hacer (adelantar canon, resolver, explicar).

*Cierra con:* el gancho, concreto.

*Se decide al escribir:* lo que se deja a la ventana de capítulo (una o dos cosas).
```

Al final: «Reglas de este libro» y «Antes de escribir», como en la escaleta.

**Notas posteriores.** Cuando una lectura o el autor cambian un capítulo, se añade debajo de su
ficha, sin borrar nada: `*vN (A-NN, origen):* …`. La nota manda sobre lo anterior.

---

## TESTS DE ESCALETA (auditoría de las fases 2 y 3)

Los mira la editora de
desarrollo; la lectora tipo los confirma en su lectura de plan. Los suelos son los de
`PAREJA_PRIMERO.md` §3, o los que la obra suba en su preset; bajarlos es decisión del autor (biblia
§14 🔒). Lo que falla se reescaleta antes de encargar.

1. **El capítulo 1 promete la pareja**: los dos están, o uno mira al otro, o hay tensión entre
   ellos. Un capítulo 1 que solo promete trama es la muestra de un thriller.
2. **La muestra gratuita engancha** (la del canal que declare la obra, `PRESET_<OBRA>.md` ›
   Cabecera › Mercado y lengua; más o menos el primer 10 % del libro, unos tres o cuatro
   capítulos): dentro de ella están el primer cara a cara (test 3) y algún momento de pareja con
   cuerpo (una mirada que pesa, una distancia que se rompe), y su peso de pareja no baja del suelo
   (test 15). Dos capítulos seguidos de trámite (el trabajo, la casa, la familia) al principio
   hacen abandonar la muestra.
3. **Primer cara a cara pronto**: los dos protagonistas, en la misma escena y con diálogo, en el
   primer 10 % del libro (un prólogo en pleno pico cuenta).
4. **Presencia y cara a cara** *(v2.0)*: (a) ningún capítulo sin el otro, en escena, en directo o
   ocupando a quien narra al menos un tercio del capítulo, con la unidad de `PAREJA_PRIMERO.md` §2:
   la sombra que no ocupa a quien narra (lo que la lectora sabe que está ahí y ella no piensa) no
   cuenta; (b) desde el primer cara a cara, nunca más de dos capítulos seguidos sin los dos en
   escena, salvo una ausencia declarada con tope (ELLIPSIS_PROTOCOL, uso B).
5. **Calendario de calor con sus suelos** *(v2.0)*: contacto con carga como tarde al 20 % del
   libro, primer beso o equivalente al 45 %, primera escena explícita al 60 %; desde el contacto,
   nunca más de cuatro capítulos seguidos sin una escena con carga (ventana móvil, no bloques
   fijos) y, desde la primera escena explícita, de calor o *edging* (HEAT_DISCIPLINE, calendario
   de calor y TEST 6).
6. **Quien da miedo lo da en página** (protagonista B por defecto; lo declara la obra), no solo en
   la ficha: algún capítulo suyo muestra lo que podría hacer y lo que se contiene.
7. **Ganchos sin excepción, y de pareja**: cada «Cierra con» tira del siguiente (por defecto, sin
   excepción; la obra puede declarar cierres de descarga con su tope), y son de pareja
   (lo que dejan abierto es entre ellos, incluido el gancho de la trama B que cae sobre la pareja:
   SEAMS_AND_HINGES, adenda) al menos dos de cada tres por libro (objetivo, tres de cada cuatro) y
   al menos dos de cuatro por bloque de cuatro capítulos (objetivo, tres de cuatro), o los que
   declare el preset.
8. **Escenas espejo** (el mismo momento contado por los dos narradores): se planean como **un
   detalle compartido** y lo que el otro no vio; nunca como la misma escena contada dos veces.
9. **El género secundario cabe en una línea** (*Variante: dark romance policial:* el
   procedimiento), y la trama B en su techo *(v2.0)*: cada beat suyo entra por la pareja
   (STORY_SPINE, adenda, TEST 6); como mucho, una de cada cuatro escenas mueve solo la trama B
   (SCENE_NECESSITY, adenda) y un capítulo por bloque tiene en ella su tensión dominante
   (TENSION_MECHANICS, TEST 7); lo que no es pareja (trama B, trama horizontal y elenco cuando su
   página no es de pareja), como mucho el 30 % del libro, sin mínimo (SUBPLOT_ARCHITECTURE,
   TEST 7). Lo que pasa del techo se funde en una escena de pareja o va a resumen.
10. **Coherencia**: calendario, quién sabe qué en cada capítulo, trato, contadores y canon oculto
    contra la biblia (correctora).

**Del libro 2 en adelante** (`SERIES_GLUE.md` y `SERIES_ARCHITECTURE.md`, adendas de dark
romance). En el 1, el 3 y el 5, «la pareja», «el primer cara a cara» y cada «primer» del
calendario de calor son **los de este libro** (la primera escena juntos después del salto entre
libros). Y se suman:

11. **Arranca donde lo dejó el anterior**: el peldaño de la escala, lo que sabe cada uno y el
    gancho de cierre del libro anterior, cobrado en los primeros capítulos. Nadie vuelve a cero.
12. **Hace lo que el anterior no podía**: las reglas de la pareja cambian (algo que ella descubre,
    algo que él ya no puede negar); si el motor de la relación es el mismo, el libro es flácido.
13. **Se entiende sin el anterior** (si la obra declara cada libro autónomo): lo que hay que saber
    entra en acción, nunca en resumen; la muestra no exige haber leído el libro previo.
14. **Paga su libro**: su trama cierra, su pregunta de pareja tiene respuesta en página (el arco de
    pareja del libro: `BRIEFING.md`, campo 2 bis) y su promesa de calor se cumple en página; el
    gancho final es de la relación o de la trama horizontal, no de la trama del libro.

**En todos los libros** *(v2.0)*, además:

15. **Entre ellos y peso, ficha a ficha**: cada ficha trae su «Entre ellos» en hechos (vacío: se
    funde con otra), si están los dos y su peso estimado; cada bloque de cuatro capítulos y el libro
    apuntan al objetivo (80 %) y no bajan del suelo (70 %), o de lo que declare la obra (biblia §14
    🔒). Un bloque por debajo no se encarga.
16. **Voces**: con más de un narrador, el reparto que declare la obra (`PRESET_<OBRA>.md` ›
    Cabecera › Correspondencia de roles).
