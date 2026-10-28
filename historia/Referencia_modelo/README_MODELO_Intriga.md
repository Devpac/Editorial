# MODELO_Intriga_v1.0 — LÉEME

Fork de género del **MODELO_AGNÓSTICO_v7** para **suspense romántico de tensión
doméstica suavizada** (preset AGATHA_ROSA): intriga + historia de amor con final
feliz obligatorio, limpio / puerta cerrada, 70.000 palabras, contemporáneo.

## USO — CÓMO SE INSTANCIA POR NOVELA (disciplina de dos plantas)

Esta carpeta es el **modelo maestro de género en estado puro**: no contiene ninguna
novela, solo plantillas con las reglas del género listas para rellenar. Es el
«agnóstico de intriga romántica». Funciona con la misma disciplina de dos plantas que
el MODELO_AGNÓSTICO_v7:

1. **Para cada novela nueva se COPIA la carpeta entera** `MODELO_Intriga_v1.0/` y se
   renombra con el título de la novela (p. ej. `NOVELA_ElFaro/`). Esa copia es la
   **instancia**.
2. En la instancia se **rellenan las plantillas con los datos concretos** de esa novela
   (pregunta central, fichas de personaje, mapa de beats real, CLUE_LEDGER de sus pistas,
   voz, subtramas…). Se reescribe libremente: es la «planta de obra».
3. El maestro **queda virgen** para copiarlo otra vez en la siguiente novela. Nunca se
   escribe contenido de una novela dentro del maestro.
4. El arranque de cada instancia sigue **OPERACIÓN 0 — FUNDACIÓN** de
   `SYSTEM_ORCHESTRATION.md`, que declara qué archivos se activan y en qué orden.

**Carpeta correcta:** el maestro que se copia por novela es **este**
(`MODELO_Intriga_v1.0/`), no `MODELO_intriga/`. `MODELO_intriga/` es el agnóstico
general (el «abuelo»), que se conserva intacto y aparte para derivar los otros géneros
(Corín, Escocés). Copiar el abuelo por error daría una novela sin la especialización de
intriga romántica.

## Cómo leer estas plantillas

- **Plantillas ESPECIALIZA** (la mayoría): contienen la **base agnóstica v7
  verbatim** y, al final del archivo, tras un separador `---/---`, una **ADENDA DE
  ESPECIALIZACIÓN (AGATHA_ROSA)** que concreta o sustituye secciones para el género.
  Regla: *donde base y género chocan, gana el género*. Una nota HTML al inicio de
  cada archivo lo señala.
- **Plantillas HEREDA**: copia sin cambios del agnóstico (infraestructura válida
  tal cual).
- **Plantilla SUSTITUYE**: `GENRE_CONVENTIONS.md`, reescrita entera como contrato
  del género (archivo núcleo).
- **Plantillas AÑADE** (nuevas, no existen en el agnóstico): `ROMANCE_BEAT_MAP.md`,
  `HEAT_DISCIPLINE.md`, `CLUE_LEDGER.md`, `SERIES_GLUE.md`.

## Las dos inversiones del fork

1. **Pregunta resoluble** (no la irresoluble del agnóstico) + resolución contractual.
2. **Final feliz limpio garantizado** (frente al desenlace oscuro del corpus de
   referencia). El corpus enseñó la maquinaria de intriga; el final se invirtió.

## Orden de trabajo (herencia del agnóstico)

OPERACIÓN 0 (fundación) → capa 0.5 (serie, si aplica) → capa 1 (diseño) → capa 2
(capítulo/escena) → capa 3 (prosa) → capa 4 (revisión). Empezar por
`GENRE_CONVENTIONS`, `THEMATIC_ENGINE`, `STORY_SPINE` + `ROMANCE_BEAT_MAP`.

Documentación de la derivación: `INFORME_CONVENCIONES_Intriga.md` (Fase A),
`DIFF_DERIVACION_Intriga.md` (decisión por plantilla), `ESTILOMETRIA_Intriga.md`
(cuotas de la dama). No contamina el agnóstico original.
