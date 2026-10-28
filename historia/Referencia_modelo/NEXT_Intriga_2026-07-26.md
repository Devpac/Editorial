# NEXT.md — Derivación MODELO_Intriga_v1.0 (AGATHA_ROSA)

> Archivo de transición entre ventanas del **proyecto de derivación** (no del
> agnóstico, que no se toca). Registra estado, fricciones capturadas y próximo paso.

---

## ESTADO AL CIERRE DE ESTA VENTANA

Derivación completa MODELO_AGNÓSTICO_v7 → **MODELO_Intriga_v1.0** (suspense romántico
de tensión doméstica suavizada, preset AGATHA_ROSA). Fases A, B, C y D **superadas**.

Entregables producidos (en la carpeta del proyecto):
- `INFORME_CONVENCIONES_Intriga.md` (Fase A).
- `MODELO_Intriga_v1.0/` — 39 archivos (34 plantillas agnósticas derivadas + 4 nuevas
  + README) · empaquetado en `MODELO_Intriga_v1.0.zip`.
- `DIFF_DERIVACION_Intriga.md` (Fase B): 1 SUSTITUYE + 4 AÑADE + 25 ESPECIALIZA + 8 HEREDA.
- `ESTILOMETRIA_Intriga.md` (Fase C).
- `El_tono_que_falta.md` (novelette de validación, 16.476 palabras) + su brief.
- `AUTOINFORME_VALIDACION_Intriga.md` (Fase D): contrato de género cumplido al 100 %;
  fork declarado OPERATIVO con correcciones menores para v1.1.

---

## FRICCIONES CAPTURADAS (protocolo: síntoma → diagnóstico → patrón general → implicación)

**F1 — Control de extensión por capítulo.**
- Síntoma: el primer borrador de la novelette salió a 7.090 palabras (< mínimo 15k);
  capítulos de ~470 palabras por defecto.
- Diagnóstico: SCALE_CALIBRATION fija el total del libro, pero la ejecución de prosa no
  tenía cuota de palabras por capítulo/escena, y la voz cortante empuja a capítulos muy
  breves.
- Patrón general: cualquier dama con voz breve tenderá a subproducir sin un presupuesto
  por unidad.
- Implicación (v1.1): añadir a `CHAPTER_BRIEF` un campo obligatorio de **cuota de
  palabras por capítulo** (derivada de SCALE_CALIBRATION / nº de capítulos).

**F2 — Utillaje de medición estilométrica.**
- Síntoma: las métricas de fragmentos, % diálogo, rayas y giro corrector salieron
  distorsionadas (la raya de diálogo se contó como fragmento y como raya de cuota; el
  giro «No…Era» acumuló falsos positivos).
- Diagnóstico: no existe un medidor que separe diálogo de narración ni que case la
  muletilla con precisión.
- Patrón general: toda validación de cuotas (Fase D de cualquier dama) necesita el mismo
  medidor fiable.
- Implicación (v1.1): construir un **medidor estilométrico** (script) que distinga
  diálogo/narración y detecte las muletillas, e integrarlo en la auditoría de cuotas de
  `REVISION_PROTOCOL` y `PROSE_LINE_DISCIPLINE`.

**F3 — Adelgazar la muletilla de marca.**
- Síntoma: el giro «No era X. Era Y.» apareció ~2× por encima de cuota; los fragmentos,
  por encima del techo (parte real, parte medición).
- Diagnóstico: los rasgos de marca de la dama se sobreusan cuando son cómodos.
- Patrón general: los marcadores de idiolecto tienden al exceso sin techo activo.
- Implicación: reforzar en `PROSODY_AND_MUSIC` / `PROSE_LINE_DISCIPLINE` el techo y la
  exigencia de variedad; pasada de prosa dedicada.

**F4 — Denouement largo / clímax adelantado.**
- Síntoma: gran twist ~80 % (objetivo 88–95 %); resolución + coda ocuparon 2 capítulos
  (~13 % vs ~5 %).
- Diagnóstico: la doble hélice resuelve pronto si el gran gesto no se retrasa y la coda
  no se acota.
- Patrón general: riesgo estructural recurrente del cierre doble (misterio + amor).
- Implicación: añadir en `STORY_SPINE`/`ROMANCE_BEAT_MAP` un control de que el gran gesto
  no caiga antes del 88 % y de que la coda no exceda ~1 capítulo.

---

## PRÓXIMO PASO

1. **v1.1 del fork:** aplicar F1 (cuota de palabras/capítulo en CHAPTER_BRIEF), F2
   (medidor estilométrico integrado), F4 (control de posición de clímax/coda); versionar.
2. **Afinado de la novelette (opcional):** pasada de prosa que baje fragmentos a 12–15 %
   y el giro corrector a ~4/10.000, y comprima la coda a un capítulo.
3. **Escalar el pipeline:** derivar las otras dos damas con el mismo PROMPT_DERIVACION
   (`MODELO_CORIN`, romance contemporáneo limpio; `MODELO_ESCOCES`, histórico), usando
   `ESTILOMETRIA_Intriga` como ancla de contraste para que las tres no se enlacen.
4. **Producción:** el fork está operativo para escribir la primera novela de 70k de la
   dama con el modelo ya derivado.

Recordatorio de disciplina: el modelo agnóstico original **no se ha modificado**; toda
la derivación vive en carpeta aparte.
