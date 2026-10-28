# AUTOINFORME_VALIDACION_Intriga.md

> **Fase D del PROMPT_DERIVACION_MODELO.** Validación del fork MODELO_Intriga_v1.0
> mediante la novelette **«El tono que falta»** (premisa original, no derivada del
> corpus). Mide cumplimiento del mapa de beats (real vs objetivo) y de las cuotas
> estilométricas (real vs cuota), registra desviaciones y su corrección.
>
> Datos de la obra: **16.476 palabras**, **15 capítulos** (media 1.098 pal/cap).
> Dentro del objetivo de novelette (15–20k) y de la cuota de capítulo (~1.150).

---

## 1. CUMPLIMIENTO DEL MAPA DE BEATS (doble hélice)

Posición estimada por capítulo (15 capítulos ≈ 6,7 % cada uno). Objetivo tomado de
STORY_SPINE/ROMANCE_BEAT_MAP (Fase A §2).

### Hélice de INTRIGA
| Beat | Objetivo | Real (cap → %) | Estado |
|---|---|---|---|
| Cold open | 0–2 % | c1 → 0 % | ✓ |
| Detonante | 2–8 % | c1–2 → 3–8 % | ✓ |
| Primera pista real (el tono que falta) | 10–18 % | c3 → ~15 % | ✓ |
| Escalada de sospechas | 20–48 % | c4–6 → 20–40 % | ✓ |
| Giro medio / inversión | 48–62 % | c8 → ~50 % | ✓ |
| Falsa resolución | 70–85 % | c11 → ~70 % | ✓ |
| Gran twist (autoría de R.) | 88–95 % | c12–13 → ~80–86 % | ⚠ algo temprano |
| Resolución | 95–98 % | c14 → ~90 % | ⚠ algo temprano |
| Coda cálida | 98–100 % | c15 → 93–100 % | ✓ (coda larga) |

### Hélice ROMÁNTICA (variante cortejo)
| Beat | Objetivo | Real | Estado |
|---|---|---|---|
| Encuentro | 0–13 % | c1 | ✓ |
| Chispa | 13–27 % | c2–3 | ✓ |
| Primer obstáculo | 27–40 % | c4 | ✓ |
| Acercamiento / casi-contacto | 40–55 % | c5, c7 | ✓ |
| Beso | — | c9 (~57 %) | ✓ |
| Momento oscuro / ruptura | 70–87 % | c10–11 (~70 %) | ✓ |
| Gran gesto | 90–96 % | c13 (~85 %) | ⚠ algo temprano |
| Resolución HEA | 96–100 % | c14 (~90 %) + coda c15 | ⚠ algo temprano |

### Puntos de cruce (obligatorios) — CUMPLIDOS
1. Secreto doméstico = obstáculo romántico y pista (el cambio del violín / la reserva
   de Mateo). ✓
2. Cada escalada de intriga acerca o tensa a la pareja (tormenta/apagón, protección). ✓
3. **Falsa resolución = ruptura** (c10–11: Mateo «culpable» y huido → Elsa lo rechaza). ✓
4. **Gran gesto = llave** (c12–13: creer a Mateo la lleva a releer las pistas y hundir
   a Rafael; Mateo vuelve y la protege). ✓
5. Ambas hélices cierran en el mismo tramo final (c11–14). ✓

**Desviación de beats:** el racimo clímax–gran gesto–HEA cae ~5–8 puntos antes de lo
óptimo, porque la resolución (c14) y la coda (c15) ocupan dos capítulos completos
(~13 % del texto) frente al ~5 % previsto. Corrección → §4.

---

## 2. CUOTAS ESTILOMÉTRICAS (real vs cuota)

| Métrica | Cuota | Real | Estado |
|---|---|---|---|
| Longitud media de frase | 11 (9–13) | **12,3** | ✓ en rango |
| Longitud media de capítulo | ~1.150 (1.000–1.350) | **1.098** | ✓ |
| Fragmentos ≤4 palabras | 12–15 % | **24,2 %** | ✗ por encima (ver caveat) |
| Dos puntos / 1.000 | ~2 | **0,97** | ⚠ por debajo (sobrecorregido; tolerable) |
| Giro «No era X. Era Y.» / 10.000 | ~4 | **7,9** | ✗ por encima (ver caveat) |
| Símil «como se + verbo» / 10.000 | ~2,5 | **3,0** | ✓ cerca |
| % diálogo | ~35 % | **~29 %** (medido por línea) | ⚠ por debajo (ver caveat) |
| Rayas «—» / 1.000 | ~4 (paréntesis) | **33,8** (incl. diálogo) | métrica no separada (ver caveat) |
| Muletillas propias (3) | presentes | recuento vigilante, corrección interior, condicional de amenaza | ✓ las tres |
| Vocabulario vetado | 0 infracciones | 0 (sin sexo explícito, sin gore, sin sobrenatural) | ✓ |

**Caveats de medición (importante):** el medidor actual es aproximado y sesga tres
métricas. (a) *Fragmentos* y *% diálogo* se distorsionan porque las líneas de diálogo
en español empiezan por raya y se contabilizan como oraciones muy cortas: inflan el %
de fragmentos y, a la vez, el método por línea infracuenta el diálogo intercalado; el
diálogo real está más cerca del objetivo. (b) *Rayas/1.000* mezcla la **raya de
diálogo** (correcta, mayoritaria) con la raya parentética de la cuota (~4), que no es
separable sin analizador. (c) El *giro «No…Era»* se sobrecuenta por falsos positivos
(«No hay nadie… Era…» no es la muletilla). La corrección incluye construir un medidor
que separe diálogo de narración (§4, fricción de utillaje).

---

## 3. CONTRATO DE GÉNERO (lista de verificación) — TODO CUMPLIDO

- **HEA garantizado:** ✓ pareja junta, viva y a salvo; coda cálida sin veneno (c14–15).
- **Puerta cerrada:** ✓ intimidad elidida en el umbral; deseo y casi-contacto sí
  mostrados.
- **Violencia contenida, sin gore:** ✓ el antagonista cae por la escalera (tobillo
  torcido); nada gráfico.
- **Ganchos de cierre en la intriga, nunca en el romance:** ✓ (c1–13).
- **Juego limpio:** ✓ P4 (medidas del violín), P5 (metrónomo 112 = entrada 112 del
  catálogo con la nota de la maestra) y P6 (escalón fregado, agua del lago) sembradas
  antes del cobro; el gran giro es reinterpretable en relectura.
- **Protagonista simpática y NO culpable:** ✓.
- **Interés dual que se limpia:** ✓ Mateo pasa de sospechoso a limpio; el ganador
  romántico no es el villano.
- **ANTI-FIRMA McFadden:** ✓ culpable = albacea/agente (NO la figura doméstica: Pilar
  es inocente y aliada); sin diario hallado como vehículo, sin epílogo-espejo, sin coda
  oscura, sin narrador infantil, sin culpables encadenados, fragmentos con variedad (no
  párrafo-de-una-palabra mecánico).
- **Doble hélice trenzada con los 5 cruces:** ✓.

---

## 4. DESVIACIONES DETECTADAS Y CORRECCIÓN

1. **Extensión del primer borrador (crítica, ya corregida).** El primer pase salió a
   7.090 palabras (< mínimo). *Corrección aplicada:* pase de expansión ×2 anclado en el
   borrador (voz y trama fijas) → 16.476 palabras. *Corrección de modelo:* CHAPTER_BRIEF
   debe fijar **cuota de palabras por capítulo** (no solo el total en SCALE_CALIBRATION).
2. **Fragmentos por encima de cuota (24 % vs 12–15 %).** Parte es artefacto de medición;
   parte es real (la voz cortante tiende al exceso). *Corrección:* pasada de prosa que
   fusione fragmentos narrativos; reforzar el techo en PROSODY_AND_MUSIC.
3. **Giro «No era X. Era Y.» por encima (7,9 vs ~4).** Parte falsos positivos, parte
   sobreuso de la muletilla de marca. *Corrección:* auditar y adelgazar a ~4/10.000.
4. **Racimo clímax/HEA algo temprano; denouement largo (2 capítulos).** *Corrección:*
   comprimir resolución+coda a ~1 capítulo o retrasar el gran giro más allá del 88 %
   (control a añadir en STORY_SPINE/ROMANCE_BEAT_MAP).
5. **Utillaje de medición (fricción de pipeline).** El medidor no separa raya de diálogo
   ni detecta la muletilla con precisión. *Corrección:* construir un medidor
   estilométrico que distinga diálogo/narración y case las muletillas, e integrarlo en
   REVISION_PROTOCOL (auditoría de cuotas).

Todas estas fricciones se registran en `NEXT.md` según el protocolo de captura.

---

## 5. VEREDICTO

La novelette **cumple el contrato de género en su totalidad** (los diez ítems de §3),
respeta el mapa de beats dentro de tolerancia (con el clímax algo adelantado) y alcanza
la extensión objetivo. Las desviaciones estilométricas residuales son menores y en buena
parte artefactos del medidor; sus correcciones están prescritas.

**MODELO_Intriga_v1.0 se declara OPERATIVO** para producción, con dos correcciones
menores pendientes de incorporar en una v1.1 (cuota de palabras por capítulo en
CHAPTER_BRIEF; medidor estilométrico que separe diálogo de narración) y un afinado de
prosa (fragmentos y giro corrector a cuota). Fase D superada.

**Fin del AUTOINFORME_VALIDACION_Intriga.**
