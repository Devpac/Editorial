# Arranque — cómo se usa la fábrica

Para el autor y para el orquestador. La fábrica vive aquí, en Editorial; cada saga vive en su
propio repo, con la fábrica montada en `fabrica/` y la obra en la raíz.

## 1. Empezar una saga

**Antes, el género.** La fábrica tiene un paquete por género (`fabrica/generos/`). Hoy hay uno:

- **`dark_romance`** — dark romance de cualquier subgénero: policial, mafia, *bully*, dark academia,
  romantasy oscura, *stalker*… El subgénero no es otro paquete: se declara en la biblia y en el
  preset de la obra (`GENRE_CONVENTIONS.md`, «Variante del subgénero»). La variante policial ya
  está escrita; las demás las escribe la obra.

Si la saga es de un género sin paquete (romantasy que no es oscura, romance contemporáneo…), primero se crea su paquete (§5).

**Pasos del autor:**

1. Crea en GitHub un repo **vacío** y privado para la saga (sin README).
2. Abre una ventana nueva, en esfuerzo máximo, y pega este prompt:

> Eres el orquestador de una obra nueva con la fábrica de Editorial. Autorizo conectar con acceso
> de escritura el repo de GitHub `Devpac/[repo-de-la-obra]` (vacío) y `Devpac/Editorial` (solo
> lectura). Lee `ARRANQUE.md` de Editorial y síguelo: prepara el repo de la obra con la fábrica y
> empieza por la fase 0. Mi idea, en bruto: [premisa, subgénero, lo que quiero]. Mi criterio de
> delegación: [el que trae la fábrica por defecto / el mío: …]. Todo en español.

3. Contesta la entrevista de la fase 0 (una pregunta cada vez) y aprueba la ficha de premisa. A
   partir de ahí, el orquestador te pide lo que es tuyo (`ORQUESTADOR.md` §7) y te da el prompt de
   cada ventana de trabajo.

**Pasos del orquestador** (con los dos repos clonados uno junto al otro):

1. Elige el paquete del género con el autor (arriba) y un **nombre de trabajo** en mayúsculas con
   guiones bajos (se cambia cuando haya título).
2. Prepara el repo:

   ```
   python3 -I Editorial/herramientas/nueva_saga.py --genero dark_romance --obra NOMBRE_DE_TRABAJO --destino <repo-de-la-obra>
   ```

   Deja `LEEME.md` (el de la obra), `.gitignore`, `fabrica/` (la fábrica montada, con su sello
   `_FABRICA.txt`) y `publicacion/` (la configuración del maquetador y la plantilla de
   instrucciones de portada). No crea el cuaderno, la biblia ni el preset: salen de sus plantillas
   en las fases 0, 1 y 1b.
3. Commit y push: «Fase 0: saga montada con la Fábrica vX.Y».
4. A partir de aquí, el repo de la obra es todo lo que hace falta: lee `fabrica/LEEME.md` y
   `fabrica/ORQUESTADOR.md`, y empieza la fase 0 (§2.0). Las ventanas de trabajo **no** necesitan
   acceso a Editorial.

## 2. Poner al día la fábrica de una saga

Cuando Editorial sube de versión (`VERSION`, `CHANGELOG.md`), una saga **no cambia sola**: se
pone al día cuando el autor lo decide, de preferencia entre libros (`ORQUESTADOR.md` §2.7 y §10):

```
python3 -I Editorial/herramientas/montar.py --genero dark_romance --destino <repo-de-la-obra>/fabrica
```

Vuelve a montar la carpeta, retira los archivos que la versión nueva ya no tiene y actualiza el
sello. Si en `fabrica/` hay algo que no es de la fábrica, se niega (la obra va en la raíz). Si el
`CHANGELOG.md` dice que cambian ranuras del preset, el orquestador rellena las de la obra antes de
lanzar ninguna ventana. Se apunta en el cuaderno de la obra.

## 3. Proponer una mejora

Una mejora que nace de una obra se registra en la obra: el orquestador deja el registro en
`informes/propuestas_fabrica.md` del repo de la obra (`PROTOCOLO_CAPTURA_APRENDIZAJE.md`; las
ventanas de una saga solo leen Editorial, no escriben en ella). Quien mantiene Editorial lo pasa a
`fabrica/metodo/REGISTROS_APRENDIZAJE.md` y lo procesa aquí: a la fábrica va la regla, escrita en abstracto y con su ranura; el valor se queda en la
obra. **Regla del fork:** nada que diga cómo escribir antes de escribir. Lo que solo corta va
directo; lo demás, con prueba a ciegas. Cada cambio se apunta en `CHANGELOG.md` y sube `VERSION`.

Al tocar la fábrica, en Editorial:

```
python3 -I herramientas/sincronizar_preset.py          # regenera las ranuras de PLANTILLA_PRESET
python3 -I herramientas/sincronizar_preset.py --comprobar
```

## 4. Publicar

El maquetador (`maquetador/`, con su `README.md`) convierte un libro en EPUB, interior PDF,
cubiertas y ficha de KDP. La configuración de cada libro está en `publicacion/` de la saga; el
orden de los capítulos publicados, en `orden:` de su `libro_NN.yaml`, igual que la tabla de su
escaleta.

```
cd Editorial/maquetador
python maquetar.py ../../<repo-de-la-obra>/publicacion/libro_01.yaml
```

## 5. Crear un paquete de género

Un género nuevo es una carpeta en `fabrica/generos/<género>/` con dos subcarpetas:

- `plantillas/` — sus plantillas de género, con **los mismos nombres de archivo** que las de
  `dark_romance` cuando cubren lo mismo (`GENRE_CONVENTIONS.md`, `HEAT_DISCIPLINE.md`,
  `ROMANCE_BEAT_MAP.md`…), para que el método las encuentre;
- `adendas/` — la adenda de su género para cada plantilla de oficio (`CHAPTER_BRIEF.md`,
  `CONTINUITY_PHYSICS.md`…), que se pega al final de la base al montar.

Lo común a todo romance (`fabrica/romance/`, la pareja primero) y el método no se tocan. Se hace
como se hizo la v3.0: una ventana de trabajo escribe el paquete a partir del de `dark_romance` y de
lo que el género tiene de distinto (sin valores de ninguna obra), una auditoría con lectoras sin
contexto lo revisa contra el de `dark_romance` y una saga de prueba arranca con él. Hasta que
exista, `nueva_saga.py` no deja montarlo.
