# {{TITULO}}

Saga hecha con la **Fábrica** (`Devpac/Editorial`). En este repo hay dos cosas, separadas:

- **`fabrica/`** — el método y las plantillas, montados desde Editorial (versión y género en
  `fabrica/_FABRICA.txt`). **No se editan aquí:** las mejoras se proponen a Editorial
  (`fabrica/PROTOCOLO_CAPTURA_APRENDIZAJE.md`) y la carpeta se vuelve a montar.
- **La obra**, en la raíz: `FICHA_PREMISA.md` (la de la fase 0), `CUADERNO_{{OBRA}}.md` (dónde estamos, decisiones del autor, índice),
  `PRESET_{{OBRA}}.md`, la biblia, `NEXT.md` (el encargo vivo), `libro_NN/`, `informes/` y
  `publicacion/` (la configuración del maquetador de Editorial).

**Si llegas sin contexto:**

- **Te han lanzado con un código de ventana** (B1, E1, C01…): eres una ventana de trabajo. Lee
  `fabrica/LEEME.md` y `NEXT.md`, y ejecuta el NEXT tal cual.
- **Te han dicho que eres el orquestador:** lee `fabrica/LEEME.md`, `fabrica/ORQUESTADOR.md` y
  `CUADERNO_{{OBRA}}.md` (si aún no existe, la saga está en la fase 0: `fabrica/ORQUESTADOR.md` §2.0).

Cuando el método nombra un archivo de la fábrica (`ORQUESTADOR.md`, `PLANTILLA_*.md`,
`GENRE_CONVENTIONS.md`, `PAREJA_PRIMERO.md`…), está en `fabrica/`. Los de la obra
(`CUADERNO_{{OBRA}}.md`, `PRESET_{{OBRA}}.md`, la biblia, `NEXT.md`, `libro_NN/`), en la raíz.

*Montada el {{FECHA}} con la Fábrica v{{VERSION}} (género: {{GENERO}}). Nombre de trabajo:
`{{OBRA}}` (se cambia cuando haya título: `fabrica/ORQUESTADOR.md` §2.0).*
