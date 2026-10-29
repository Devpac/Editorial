# Dossier de evidencias: por qué funciona

*Madera y Pólvora*, libro 1. Repo `Devpac/Dark`, rama `main`, al commit `62cb0c6` (29-10-2026, «C17: brief»). Hecho en
solo lectura el 29-10-2026 para el capítulo «por qué funciona» del manual de producción.

**Cómo leer este dossier**

- Cada afirmación lleva su fuente: la decisión (A-NN, en el Anexo A de `madera_y_polvora_biblia.md`), el archivo o el commit.
- Abreviaturas de archivos:
  - `HIST`: `libro_01/historial_lecturas.md`;
  - `PLAN`: `libro_01/plan_lectora.md`;
  - `CUAD`: `CUADERNO_MADERA_Y_POLVORA.md`;
  - `LEEME-h`: `Referencia_Dark Romance/LEEME_historia_MyP_hasta_v1.2.2.md`;
  - `SO §8`: el registro de la adenda de `SYSTEM_ORCHESTRATION.md`;
  - `DIAG/`: `informes/diagnostico_v2/`.
- **Límites de las fuentes:**
  - El `git log` está injertado en `f693014` (23-10-2026). Lo anterior solo consta en los archivos.
  - De los borradores de agosto no hay ninguna nota numérica escrita en el repo.
  - Las lecturas externas del tramo 8–14 no han llegado: `informes/lectura_externa_T2/` solo tiene el encargo, el manuscrito y la OPERACIÓN D corta.
  - El 17 solo tiene el brief.
- **Las notas son relativas.** La lectora tipo «oscila alrededor de un punto entre lecturas: se mira su **orden**, no un número suelto»
  (`ORQUESTADOR.md` §5). También «puntúa alrededor de un punto por debajo de las lectoras externas, pero ordena los capítulos igual»
  (`CUAD` §5). Cada lectora es un agente nuevo y sin contexto. Una subida de un punto en un capítulo suelto no prueba nada.

---

## 0. En una página

1. **La prosa ya era buena desde el 21-10 (v1.1).** Desde entonces la editora no se mueve: entre 7,4 y 8,5 en todos los capítulos escritos
   desde el 3, antes y después de la v2.0. El 2, que viene de agosto, se queda en 6,8–7,0.
   - Lo que más subió la calidad de la prosa fue salir de la v9Beta. En la prueba a ciegas del cap. 3, la v9Beta sacó 6,5 y 7, con prosa
     de 6 y 6,5. El modelo con cierre obligatorio y lectura por otra sacó 8,3 y 8, con prosa de 8 y 7,5.
2. **Lo que subió después fue el enganche de la lectora y la parte del libro que es romance.** Ahí está la diferencia entre «buena prosa»
   y «el libro que la lectora vino a buscar».
   - Con el diseño heredado de intriga, los capítulos sin la pareja sacaban unos 6 de enganche y los que la tenían, unos 8.
   - En las mismas lecturas, lo escrito con la v2.0 saca ≈ 8,1–8,3 y lo escrito antes, ≈ 6,8.
3. **Funcionan:** escritura sin consignas de prosa, cierre obligatorio con acta, lectura por quien no escribió, lectora tipo que manda,
   cortar antes que añadir, la regla de las tres lecturas y medir el peso de la pareja. Hay que poner cada pieza con la fuerza de evidencia
   que tiene (§2): solo la primera tiene prueba a ciegas.
4. **Lo que más costó:**
   - el modelo heredado de un modelo de intriga: hubo que parar cuatro días, rediseñar, cortar lo escrito y escribir cuatro piezas nuevas;
   - los borradores que se saltaron el cierre;
   - los tics y los espejos entre POV, que siguen saliendo en casi cada lectura.

---

## 1. La curva de calidad

### 1.1 Tabla cronológica, pieza a pieza

Las versiones del método están en `SO §8` y `LEEME-h`.

- La numeración es la del momento.
- Desde A99, la v4 (la publicada): 3 = `capitulo_05.md`, 5 = `capitulo_07.md` (el bar), 7 = `capitulo_09.md`, 8 = `capitulo_10.md`,
  9 = `capitulo_12.md`.

Columnas de la tabla:

- **Editora:** nota global; entre paréntesis, la que estima con sus cortes.
- **Lectora:** enganche de la lectora tipo.
- **% romance:** lo que ve la lectora tipo.
- **% pareja:** el de la editora y el del acta (C-10), en ese orden.
- «—»: el dato no consta.

| Fecha | Método | Pieza (ventana) | Editora | Lectora | % romance | % pareja | Otros datos | Fuente |
|---|---|---|---|---|---|---|---|---|
| 08-08 | Modelo DR del 08-08, derivado de MODELO_Intriga v1.0 | Borradores de los caps. 1 y 2 (Opus 5.5) | — (sin nota en el repo; la «lectura editorial del chat» halló 8 defectos) | — | — | — | El cap. 1, «corregido tras la lectura editorial del chat» | `LEEME-h` §1, §5 |
| ≤ 21-10 | v9Beta (`Agnostico9`) | Cap. 3 (V-10) | 6,5 y 7 (a ciegas; prosa 6 y 6,5) | — | — | — | «como»: 7,6 por cada 1.000 palabras | `libro_01/cap03_lectura_editorial.md` |
| 21-10 | **DR v1.1** (cierre C y C.5 obligatorios) | Cap. 3 (DR-01) | **8,3 y 8** (a ciegas; prosa 8 y 7,5) | — | — | — | «como»: 3,3; gana DR-01 | ídem; A80 |
| 21-10 | v1.1 frente a v1.2 | Cap. 4 (DR-02A / DR-02B) | 7,5 y 7,8 / **8,5 y 8** | — | — | — | «la v1.2 **no empeora**»; parte de la diferencia es variación | `cap04_lectura_editorial.md`; A81 |
| 21-10 | v1.2 | Cap. 5, Cruz (DR-03) | 8,4 | **8**; los caps. 1–4, 7 · 4 · 5 · 6 | — | — | La editora puntúa los caps. 1–4 con 8,6 · 8,5 · 8,0 · 8,8 | `cap05_lectura_editorial.md` |
| 21-10 | v1.2.1 (plan de la lectora, A82) | Pasada a los caps. 2 y 3; cap. 6 (DR-04) | 6,8 · 8,0 · 7,8 | Caps. 1–6: 8 · 5 · 5 · 6 · 9 · 7 | — | — | «la parte de ella me parece de las mejores que he leído en español» | `cap06_lectura_editorial.md` |
| 21-10 | v1.2.1 | Cap. 7, el bar (DR-05) | 7,8 (≈ 8,3) | **8**; caps. 1–7: 6 · 4 · 5 · 6 · 8 · 7 · 8 | — | — | «Ahora sí sigo leyendo» | `cap07_…`; `PLAN` §D |
| 21-10 | A84: el cap. 2 funde el 2 y el 3 | Cap. 2 fundido | 7,0 (los antiguos, 6,0 y 5,8) | Muestra vieja: 8 · 6 · 5. Publicados 1–4: 8 · 5 · 7 · 9 | — | — | — | `cap02_lectura_editorial_A84.md` |
| 21-10 | v1.2.1 | Cap. 8, Dani (DR-06) | 8,0 (≈ 8,3) | **6** («él no sale»); publicados 1–7: 7 · 5 · 6 · 8 · 6 · 9 · 6 | — | — | — | `cap08_…`; `PLAN` §G |
| 21-10 | **v1.2.2** (C-9, C-10 y lectura externa) | Externas de los publicados 1–7 (Gemini, GPT y Opus) | — | Medias con la lectora: 7,9 · 5,5 · 7,0 · 8,4 · 6,9 · 9,0 · 7,6 | «80 % novela negra y 20 % romance» | — | Las tres lo comprarían a 3,99 €; prosa «muy por encima de la media de KU» | `PLAN` §H; A86 |
| 21-10 | v1.2.2 | Relectura de los publicados 1–7 tras los cortes | — | 8 · 6 · 7 · 9 · 7 · 9 · 7 (antes 7 · 5 · 6 · 8 · 6 · 9 · 6; +1 de media) | — | — | — | `PLAN` §H bis |
| 21-10 | v1.2.2 (escrito con el NEXT anterior a A86) | Cap. 9, Cruz (DR-07) | 7,4 (≈ 8,1) | **8** (la segunda mitad, 10): «¿Miedo? Por fin, sí» | — | — | — | `cap09_…` |
| 22-10 | v1.2.2, **esfuerzo máximo** | Cap. 10, Salvat (DR-08) | 7,9 (≈ 8,6) | 7; publicados 1–8: 8 · 6 · 7 · 9 · 7 · 9 · 8 · **10** | — | — | — | `cap10_…` |
| 22-10 | v1.2.2 | Cap. 11 (DR-09) | 7,4 (≈ 8) | **6** («con el dedo cerca de devolver»; «lo íntimo se lo lleva el malo») | — | — | — | `cap11_…`; `PLAN` §J |
| 22-10 | **v1.3** | Cap. 12, Cruz en el piso (DR-10) | 7,8 (≈ 8,1) | **9**: «Por fin el dark romance que vine a buscar» (publicados 1–10: 7 · 4 · 6 · 8 · 7 · 8 · 6 · 9 · 6 · 5) | — | — | — | `cap12_…`; `PLAN` §K |
| 22-10 | Diagnóstico (A92) | El diseño del libro 1 (48 caps.) | — | — | — | Diseño: **39 %**; caps. 1–12, **26 %**; juntos en 9 de 47 | Nueve lecturas sin contexto | `DIAG/G1_escaletas.md`; `PAREJA_PRIMERO.md` |
| 24-10 | **v2.0** («la pareja primero») | Escaleta v4 (E2), lectura de plan | Promesa 7,6 · pareja 7,8 · arquitectura 6,6 · originalidad 7,5 · riesgos 6,0 | Compraría la muestra; no abandona | **60 %** («el mínimo») | ≈ 73 % medido (78,6 % declarado) | Fallan los tests de calor y de peso | A98; `PLAN` §L |
| 24-10 | v2.0 | Ampliada, tramo 1 (A1) | — | Compraría la muestra | **55 %** | Bloques 82 · 88 · 84 % (correctora) | «aguanta tres cortes y no un cuarto» | A100; `PLAN` §M |
| 26-10 | v2.0 | Ampliada, tramo 2 (A2) | — | «él ya me tiene» | **65 %** («con un 75/25 iría más contenta») | 84 · 94 · 74 · 95 % | — | A101; `PLAN` §N |
| 26-10 | v2.0 | Ampliada, tramo 3 (A3): el libro entero | — | Compraría el 2 «esa misma noche» | **60 %**; del 33 al 40, mitad y mitad | 77 · 79 %; el libro, 78 % | — | A102; `PLAN` §O |
| 26-10 | v2.0 | Prólogo (C00) | **8,3** (≈ 8,5) | **8,5** (el 1, 7: «bajón») | **80 %** | 85 / 92 | «me lo bajo ya en KU» | A104; `prologo_lectura_editorial.md` |
| 27-10 | v2.0 | El 5 con el bar ampliado (C05b) | **8,3** (≈ 8,7) | **8** (el bar, 9; la pecera, 5) | **80 %** | 70 / 72 | — | A105 |
| 27-10 | v2.0 | Mitades de Cruz del 4 y del 8 (C04b y C08b) | 7,8 y 7,8 | 6 y 7; del prólogo al 9: 9 · 7 · 5 · 6 · 6 · 9 · 6 · 8 · 7 · 9 | **40 %** del prólogo al 9 | 30–33 / 31; 25 / 24 | — | A106 |
| 27-10 | v2.0 | El 10 (C10) | 7,9 (≈ 8,3) | 7 (la cámara, 9) | **40 %** | 60 / 62 | — | A108 |
| 28-10 | v2.0 | El 11 (C11) | 7,9 (≈ 8,3) | 7,5 («Pídemelo», «Aquí no») | **60 %** | 63–65 / 70 | — | A109 |
| 28-10 | v2.0 pasa a `main` (A110) | El 12 (C12) | 7,7 (≈ 8,3) | 8 («vuelve el miedo») | **80 %** | 70 / 91 | — | A111 |
| 28-10 | v2.0 | El 13 (C13), el primer beso | **8,1** (≈ 8,5) | **8,5** («casi todo lo que quería») | **60 %** | 80 / 98 | — | A112 |
| 28-10 | v2.0 | El 14 (C14) | 7,7 (≈ 8,1) | 7 («el mejor giro») | **35 %** (alarma) | 75 / 94 | — | A113; `PLAN` §W |
| 28-10 | v2.0 | OPERACIÓN D corta del tramo 8–14 | — | — | — | Medido: 8, 23 · 9, 97 · 10, 55 · 11, 69 · 12, 90 · 13, 98 · 14, 82. Bloque 3, **77 %**; bloque 4 (13–14), 91 %; tramo, 69 % | Todos los cierres de Cruz, él mirándola | A114; `informes/lectura_externa_T2/OPD_8_14.md` |
| 28-10 | v2.0 | El 15 (C15) | 8,0 | **6** | **65 %** | 60 / 70 | — | A115; `PLAN` §X |
| 28-10 | v2.0 | El 16 (C16) | **8,4** (voz, 8,8) | 7 («Quiero oírselo», «ahí grité») | **65 %** | 70 / 85 | Bloque 4 (13–16), ≈ 79 % | A117; `PLAN` §Y |
| 28-10 | v2.0 | Las cámaras, lectura de plan con dos lectoras tipo | — | Las dos: **B > A > C** | — | — | C: «me siento estafada» | A118; `informes/plan_camaras/` |
| 29-10 | v2.0 | C17 | — | — | — | — | Solo el brief (`62cb0c6`); las externas del 8–14, sin llegar | `CUAD` §1 |

Otras pruebas del método, que no puntúan prosa (`HIST`; `CUAD` §5):

- Una ventana ciega con «continúa con lo que toque» saca un 8/10 de autosuficiencia.
- La v1.3 hizo tres pruebas a ciegas:
  - seguir esta obra, 8/10;
  - una saga nueva de otro subgénero, 7/10;
  - el paso al libro 2, 6/10 (6/10 también al repetirla).

### 1.2 Lo que dice la tabla

1. **La editora es plana desde el 21-10.** En lo escrito con la v1.x desde el 3 saca entre 7,4 y 8,5 (8,1–8,6 con cortes); el 2, de agosto, 6,8–7,0. En la v2.0, entre 7,7 y 8,4 (8,1–8,7 con
   cortes). La curva no está en la editora: está en la lectora tipo y en el porcentaje de romance.
2. **Antes de la v2.0, la editora no veía el problema de género.**
   - En la lectura del cap. 5, la editora puntúa los caps. 1–4 con 8,6 · 8,5 · 8,0 · 8,8. La lectora tipo les da 7 · 4 · 5 · 6
     (`cap05_lectura_editorial.md` §1).
   - La lectora del 6 lo dice claro: el problema «ya no es la prosa […] sino que **aún no se han visto la cara**» (`cap06_…` §1).
3. **El enganche sigue a la pareja, ya con el diseño viejo.** Se cruza el peso de pareja que daban las fichas viejas (`DIAG/G1_escaletas.md`)
   con la primera nota de la lectora a cada capítulo:

   | Cap. (escaleta vieja) | Pareja (ficha) | Lectora, primera nota |
   |---|---|---|
   | 1 (C) | 15 % | 7 |
   | 2 (M) | 0 % | 4 |
   | 4 (M) | 5 % | 6 |
   | 5 (C) | 80 % | 8 |
   | 6 (M) | 0 % | 7 |
   | 7 (M, el bar) | 40 % | 8 |
   | 8 (M) | 5 % | 6 |
   | 9 (C) | 55 % | 8 (la mitad con ella, 10) |
   | 10 (M) | 0 % | 7 |
   | 11 (M) | 5 % | 6 |
   | 12 (C) | 85 % | 9 |

   - Con un 40 % de pareja o más, la media es **8,25**. Con un 15 % o menos, **≈ 6**.
   - El diagnóstico lo dice así: «el único capítulo de ella con él saca un 8 con las mismas reglas de prosa que los suyos sin él (4–7):
     enfría la ausencia de él, que se decide al diseñar» (`DIAG/E1_prosa_revision.md`).
4. **Lo escrito con la v2.0 puntúa más que lo de antes, en las mismas lecturas.** La lectora tipo relee del prólogo al último en cada C.5.
   Separando las piezas por versión:

   | Lectura | Del 1 al 9 (v1.x, cortado) | Prólogo y del 10 en adelante (v2.0) |
   |---|---|---|
   | C14 | 6,4 | 8,0 |
   | C15 | 6,8 | 8,3 |
   | C16 | 6,8 | 8,1 |

   Lo de la v2.0 son además los capítulos con más pareja por diseño y los más recientes. La comparación no separa el modelo del diseño ni de
   la posición en el libro (ver §5).
5. **La nota del capítulo nuevo sube casi siempre en la relectura siguiente:**
   - el 10, de 7 a 9;
   - el 11, de 7,5 a 8;
   - el 12, de 8 a 9;
   - el 13, de 8,5 a 9 y a 10;
   - el 14, de 7 a 8;
   - el 15, de 6 a 7.

   El listón (lectora ≥ 6) se aplica a la primera nota.
6. **El romance que ve la lectora sube del 20 % que veían las externas a un 60–80 % en las piezas con cara a cara.** Pero no se estabiliza:
   el 14 cae al 35 %, el 15 y el 16 se quedan en el 65 %. La lectora «solo cuenta como romance el deseo y el contacto» (A114).
7. **Tres medidas del peso de pareja que no coinciden:**

   | Pieza | Acta | Editora | Lectora | OPD |
   |---|---|---|---|---|
   | Prólogo | 92 | 85 | 80 | — |
   | 10 | 62 | 60 | 40 | 55 |
   | 12 | 91 | 70 | 80 | 90 |
   | 13 | 98 | 80 | 60 | 98 |
   | 14 | 94 | 75 | 35 | 82 |
   | 15 | 70 | 60 | 65 | — |
   | 16 | 85 | 70 | 65 | — |

   Quien escribe se mide más alto que quien lee.

---

## 2. Los cambios que movieron la curva

Grados de evidencia:

- **A:** prueba a ciegas, o antes y después con el mismo instrumento.
- **B:** coincidencia clara en el tiempo, con lo que dicen las lectoras.
- **C:** plausible; no se puede atribuir.

### 2.1 Cierre obligatorio con acta y lectura por quien no escribió (v1.1, 21-10; A80)

- **Qué:** se deja la v9Beta y se vuelve al modelo Dark Romance con la OPERACIÓN C obligatoria («un capítulo no está escrito hasta que tiene
  su acta») y la C.5, la lectura editorial por otra ventana (`SO §8`, v1.1; adenda §4).
- **Qué arreglaba:** los borradores del 08-08 tenían ocho defectos «que el modelo no cazó porque se saltó el cierre; los cazó la lectura
  editorial del chat. Casi todas las reglas ya existían» (`LEEME-h` §5). Por ejemplo:
  - «Cruz se explica con remates-resumen»;
  - «Mara narra sin ironía y suena a Cruz»;
  - el «cap. 1 sin señal de dark romance».
- **Qué pasó:** en la prueba a ciegas del cap. 3, dos editoras sin contexto con los textos en orden invertido:

  | | DR-01 | v9Beta |
  |---|---|---|
  | Global | 8,3 y 8 | 6,5 y 7 |
  | Prosa | 8 y 7,5 | 6 y 6,5 |
  | Comparaciones con «como» (por 1.000 palabras) | 3,3 | 7,6 |

  A la v9Beta le señalan «frases-resumen y aforismos», «imágenes puestas para sonar literarias y un cierre plano que copia la ficha»
  (`cap03_lectura_editorial.md` §1).
- **Evidencia: A** para «el paquete DR v1.1 escribe mejor que la v9Beta». Lo que no aísla es qué pieza del paquete lo consigue: el cierre,
  la lectura, la ausencia de consignas o el brief de una hoja (ver 2.2).
- **En general:** un capítulo no está terminado hasta que pasa un cierre obligatorio con acta y lo lee alguien que no lo escribió.

### 2.2 La regla del fork: ninguna instrucción de prosa antes de escribir

- **Qué:** «ninguna mejora añade instrucciones antes de escribir. Todo cambio va al cierre (OPERACIÓN C) o a la lectura editorial (C.5). Si una
  mejora necesita decirle a quien escribe cómo escribir, no entra. (Es lo que hundió la prosa de la v9.)» (`LEEME-h` §6). Hoy está en
  `ORQUESTADOR.md` §10, en la adenda §4 (REGLA DE NO PRESCRIPCIÓN) y en `PAREJA_PRIMERO.md` §6.
- **Cuándo:** v1.1 y v1.2 (21-10). Después se ratifica en cada versión:
  - la v1.2.2 «va directa a `main` porque solo añade comprobaciones de cierre que cortan»;
  - de la v2.0: «Cambia el diseño, no la escritura: no añade instrucciones antes de escribir» (`SO §8`).
- **Cómo se aplica:**
  - el registro de aprendizaje 001 pedía elevar SEAMS, TENSION, DIALOGUE, SUBTEXT y SENSORY «a disciplina previa»: se marcó «DESCARTADAS (regla
    del fork)» (`REGISTROS_APRENDIZAJE.md`, 001);
  - el NEXT pone los filtros «Después del borrador» y dice: «Las reglas de prosa son oído de fondo: no se escribe contra una lista» (`NEXT.md`
    §3);
  - C04b y C08b escribieron los dos borradores y solo después leyeron las reglas de cierre (`libro_01/C04b_acta.md`, cabecera).
- **Qué pasó:** la prosa se mantiene a lo largo de cuatro versiones del método que sí cambiaron cosas. La editora da 7,5–8,4 de prosa y la voz
  de Cruz sube a 8,8 en el 16. Ninguna mejora posterior la bajó.
- **Evidencia: C**, con un indicio fuerte. La afirmación de que la v9 se hundió por prescribir prosa es del propio repo y no tiene una prueba
  aislada. La prueba a ciegas del 2.1 encaja con ella, pero no la separa.
- **En general:** quien escribe lo hace con la obra y el encargo delante, y las reglas de prosa solo se aplican después del borrador, para
  cortar. Un cambio del método que diga cómo escribir no entra.

### 2.3 La lectora tipo, que manda (v1.2.1, 21-10; A82)

- **Qué:** además de la editora, cada capítulo lo lee una lectora tipo (31 años, KU/BookTok), sin contexto y con todo lo anterior. Su enganche
  manda: «hay que hacerle caso sí o sí» (el autor, A82; `CUAD` §2). Lo que pide se apunta en `PLAN`.
- **Qué arreglaba:** el enganche de los caps. 1–5 era 7 · 4 · 5 · 6 · 8, y pedía:
  - «grieta interior en Cruz»;
  - un «encuentro cara a cara pronto», «en el 6 o el 7»;
  - «menos taller y oficina»;
  - «peligro real» (A82; `PLAN`, cabecera).

  Mientras tanto, la editora daba a esos capítulos entre 8,0 y 8,8 (2.1 arriba).
- **Qué pasó** (evidencia B, por lo que dicen las lectoras):
  - el bar pasa al cap. 7: enganche 8, «Ahora sí sigo leyendo» (`PLAN` §D);
  - la grieta y el miedo, en el 9: «¿Miedo? Por fin, sí»;
  - el piso de ella, en el 12: 9, «Por fin el dark romance que vine a buscar» (`PLAN` §K);
  - la pasada de lectora al cap. 2 lo sube de 4 a 5 y el 3 se queda en 5 (`cap06_…`). En los capítulos de oficina, la pasada sola no basta.
- **En general:** cada capítulo lo lee también un lector del público objetivo, sin contexto y con todo lo anterior delante. Da una nota de
  enganche y dice dónde salta y qué le falta. Si discrepa del editor, gana el lector del público. Se mira el orden de sus notas, no un número
  suelto.

### 2.4 Gancho sin excepción (v1.2.1; A82)

- **Qué:** se retira la excepción de «cierre estático» que se había ensayado en la v1.1; el cap. 2 «se reescribe para cerrar en gancho» (`LEEME-h`
  §5, defecto 8; adenda §5).
- **Qué pasó:**
  - la lectora: «Cerrar los capítulos en ellos, no en el caso […] un "Robles" engancha más que un nombre de médico». El cierre del 7 pasa a los
    nudillos (`PLAN` §D.5; `cap07_…` §2.3);
  - en el 9, el cierre nuevo («A la policía no la voy a esperar. / A ella, sí.») acompaña a la subida a 10 tras los cortes (`PLAN` §I).
- **Evidencia: B.**
- **En general:** todos los capítulos cierran empujando a pasar página, y la mayoría de los cierres son de la trama principal del género.

### 2.5 La muestra gratuita, leída como muestra (A84, 21-10)

- **Qué:** la lectora leyó los caps. 1–3 como la muestra de Amazon (8 · 6 · 5: «lo pediría en KU porque es gratis, pero no lo compraría»), y se
  funden el 2 y el 3.
- **Qué pasó:**
  - la editora sube el 2 de 6,0 y 5,8 a 7,0;
  - la lectora, con los publicados 1–4: 8 · 5 · 7 · 9 (`cap02_lectura_editorial_A84.md`).
- **Evidencia: B.** El 2 sigue siendo el valle: 5,5 de media en las externas (`PLAN` §H). Se recortó otra vez a la mitad en A93 y A103.
- **En general:** los primeros capítulos se leen también como muestra gratuita («¿lo comprarías?»), y lo que no vende antes del primer
  encuentro se corta o se funde.

### 2.6 Lecturas externas, la regla de las tres lecturas y las comprobaciones C-9 y C-10 (v1.2.2, 21-10; A86)

- **Qué:** el autor pasa los publicados 1–7 a Gemini, GPT y Opus en otra ventana. Lo que señalan tres lecturas o más «es un problema confirmado
  y se corrige en los capítulos escritos». El cierre suma:
  - C-9: espejos entre POV, tics y motivos que vuelven;
  - C-10: peso de la relación (`SO §8`, v1.2.2).
- **Qué arreglaba** (`PLAN` §H):
  - «80 % novela negra y 20 % romance»; «*Haunting Adeline* con el freno de mano puesto»;
  - escenas espejo (el tablón del 5 y el 6, «casi palabra por palabra»);
  - «cuento hasta tres» siete veces en siete capítulos;
  - «no necesito que cada persona, cadáver y emoción venga con su comparación de restauración»;
  - «Cruz no da miedo todavía».
- **Qué pasó:** la relectura con los cortes da 8 · 6 · 7 · 9 · 7 · 9 · 7, frente a 7 · 5 · 6 · 8 · 6 · 9 · 6: +1 de media (`PLAN` §H bis).
  - Ojo: también suben capítulos que los cortes de A86 no tocaban (el publicado 1, de 7 a 8; el 4, de 8 a 9), así que parte de esa subida es
    variación entre lectoras.
  - Después, la regla de las tres lecturas resuelve dos cosas:
    - el rótulo `### CRUZ` en los capítulos partidos (A108): «En el 4 y en el 8 pone MARA, pero a mitad pasa a narrar él sin avisar», tercera
      lectura;
    - las cámaras (A117 → A118).
- **Evidencia: B** para los problemas, que se confirmaron y se corrigieron. **C** para el +1.
- **En general:** cada tramo de unos siete capítulos lo leen lectores de otros modelos. Lo que señalan tres lecturas o más es un problema
  confirmado y se corrige también en lo ya escrito. Y se convierte en una comprobación de cierre que solo corta.

### 2.7 La pareja primero (v2.0, 22–23-10; A92 a A97; lo escrito, A103; entra en `main` en A110)

- **Qué:** la pareja es la trama A de cada libro y de cada capítulo, y el caso es la trama B, con techo.
  - Su peso tiene número, suelo y unidad: objetivo 80 %, suelo 70 %, por bloque de cuatro capítulos, medido en palabras (`PAREJA_PRIMERO.md`
    §1–§3).
  - Hay suelos de presencia, cara a cara, contacto, calor, voces y ganchos.
  - Se derogan las adendas de Intriga en todo el catálogo.
  - Cada ficha empieza por «Entre ellos».
  - El orden del trabajo: escaleta nueva (E2), ampliada (A1–A3), cortes y fusiones de lo escrito (A103) y piezas nuevas (C00, C05b, C04b y C08b).
  - Las palabras del autor: «Quieren dark romance, no quieren policial […] no queremos un 80/20, queremos un 20/80, mínimo 30/70» (A92).
- **Qué arreglaba:**
  - el diseño del libro 1 daba un 39 % de pareja, los caps. 1–12 un 26 % y los dos protagonistas estaban juntos en escena en 9 de 47 capítulos
    (`DIAG/G1_escaletas.md`);
  - «Doce capítulos con un solo cara a cara no rompen el modelo: **lo cumplen**. Más de una docena de techos para la pareja y **ningún suelo**»
    (`DIAG/D_genero.md`);
  - «Siete de nueve archivos siguen con la cabecera "MODELO_Intriga_v1.0" […] rige la Intriga» (`DIAG/B_estructura_trama.md`);
  - las externas: «80 % novela negra y 20 % romance».
- **Qué pasó:**
  - El romance que ve la lectora en los planes pasa a 55–65 % (A98 a A102).
  - En lo escrito, 80 % en el prólogo, el bar ampliado y el 12; 60 % en el 11 y el 13; 35 % en el 14.
  - Las piezas de la v2.0 puntúan ≈ 8,0–8,3 frente a ≈ 6,4–6,8 de lo anterior en las mismas lecturas (§1.2.4).
  - Lo que dicen las lectoras:
    - «me lo bajo ya en KU» (prólogo, 8,5);
    - «por fin de frente» (el 11);
    - «casi todo lo que quería» (el 13, que sube a 10 en las relecturas).
  - La OPD mide 77 % en el bloque 3 y 91 % en el 13–14 (A114).
  - La editora no cambia (7,7–8,4). Su nueva sub-nota de «pareja» va de 6,5 a 8,8.
  - El autor: «el modelo v2.0 va mejor de calle» (A110).
- **Evidencia: B**, fuerte en lo que dicen las lectoras y en la tabla de §1.2.3. **No hay prueba a ciegas:** estaba prevista y se canceló en A110.
  No se puede separar el efecto del modelo del de la escaleta nueva ni del avance del libro.
- **En general:** en un género cuya promesa es una relación, la relación es la trama A de cada libro y de cada capítulo, con un peso medido
  (objetivo y suelo) por bloque y por libro. La otra trama tiene techo. Ese peso se fija en el diseño y se comprueba después del borrador. Nunca
  es una consigna de prosa.

### 2.8 Que todas las lecturas digan cuánto es romance (v2.0)

- **Qué:** cada lectura dice qué parte es romance y qué parte es la otra trama. El acta lo mide con C-10 y el registro 12, con alarma y salida
  («se reescaleta el bloque siguiente, nunca la prosa»). Cada ~7 capítulos hay una OPERACIÓN D corta (`PROTOCOLO_LECTURA.md` §3, §5, §8; adenda
  §4, D-21).
- **Qué arreglaba:** «las lecturas preguntan si hay química, no cuánta» (`DIAG/A_direccion_fases.md`).
- **Qué pasó:** el 35 % de la lectora en el 14, frente al 94 % del acta, dispara la alarma (`PLAN` §W.5). Con ella llega la OPD corta, que encuentra
  el tic estructural de los cierres de Cruz (A114). El cierre nuevo del 16 funciona («El cierre nuevo funciona», `C16_lectura_editorial.md`).
- **Evidencia: A** como instrumento: detecta cosas que el acta no ve. Sobre la nota, B.
- **En general:** todas las lecturas estiman a ojo el peso de la trama principal del género y se comparan con la cuenta de quien escribió. Si un
  bloque baja del suelo, se rediseña el bloque siguiente, no la prosa.

### 2.9 Lectura de plan por la lectora tipo antes de escribir (desde A82; A90, A98 a A102, A118)

- **Qué:** las decisiones grandes se dan a lectoras tipo sin contexto como opciones o como escaleta, antes de escribir. El orquestador convierte en
  nota de la escaleta lo que pide la lectora y la editora no contradice (`ORQUESTADOR.md` §2.3).
- **Ejemplos:**
  - el monitor de la piscina, «en dos tiempos» (A90);
  - «tres cortes los aguanto; un cuarto, no», que llevó al *edging* sin cortes (A100, A101);
  - la mirada a la cámara como última línea del libro (A102);
  - las cámaras: B > A > C en las dos lectoras (A118).
- **Qué pasó:** de lo que ya está escrito, el cobro del monitor («se fue el sábado», en el 11; «El de la piscina está bien. Lejos.», en el 16) llega
  sin quejas. Lo demás está en capítulos que no se han escrito.
- **Evidencia: C** sobre las notas (no hay todavía capítulos que lo midan). Lo que sí está claro es que las decisiones vienen de la lectora.
- **En general:** antes de escribir, las decisiones grandes de trama se dan a lectores del público como opciones, y se elige con su orden de
  preferencia.

### 2.10 Esfuerzo máximo (22-10)

- **Qué:** las ventanas de trabajo y el orquestador, en esfuerzo máximo («usaremos máx», `CUAD` §2), «sin pruebas a ciegas para decidirlo».
- **Qué pasó:** el primer capítulo en máximo es el 10 (DR-08): editora 7,9 (≈ 8,6) y lectora 7, en la misma banda que antes.
- **Evidencia: no atribuible.**
- **En general:** el nivel de esfuerzo se fija y se apunta, pero no se puede citar como causa de la calidad sin una prueba.

### 2.11 Correcciones que siguen a una caída

Dos casos en que la nota cae, se cambia algo y después se recupera:

- **Los cierres de Cruz.** La OPD descubre que todos los cierres de Cruz (8, 9, 10, 12, 14) son él mirándola a través de algo (A114). El NEXT del 16
  pide otro cierre. La editora del 16 lo confirma («El cierre nuevo funciona»), con la nota más alta de la v2.0: 8,4, y voz 8,8 (A117).
  - **Evidencia: B.**
  - **En general:** una auditoría periódica busca patrones de estructura repetidos (cierres, aperturas), además de las frases repetidas.
- **El miedo.**
  - La lectora pide que él dé miedo «con ella delante» (`PLAN` §M.7); en el 11 lo ve «contenido, casi tierno».
  - El NEXT del 12 lo apunta, y el 12 trae «vuelve el miedo, y es lo mejor»: 8, y 9 en la relectura (`PLAN` §T.3, §U.1).
  - **Evidencia: B.**
  - **En general:** lo que el lector echa de menos se apunta como hecho de trama en la ficha del capítulo siguiente, nunca como consigna de estilo.

---

## 3. Los errores que costaron caro

### 3.1 Un modelo heredado de otro género

- **Qué pasó:** el modelo nació del MODELO_Intriga v1.0 (`LEEME-h` §1). Sus adendas siguieron mandando en muchas plantillas.
  - El documento de derivación de agosto ya declaraba «Esto NO es una novela policíaca con romance» (`Referencia_Dark Romance/DIFF_DERIVACION_DarkRomance.md`).
  - El NEXT del 08-08 ya avisaba de «evitar el deslizamiento al procedimental».
  - Sin un suelo medible, la declaración no aguantó: diseño al 39 %, lectoras al 20 % (§2.7).
- **Coste:**
  - la escritura se para del 22-10 al 26-10 (A92 → C00);
  - nueve diagnósticos;
  - la biblia v4.0;
  - una escaleta nueva (E2) y su ampliada (A1–A3);
  - cortes y fusiones de lo escrito (A103), con cinco costuras graves;
  - cuatro piezas nuevas.
- **Lo que no se pudo arreglar:**
  - lo escrito sigue bajo una excepción declarada (A96);
  - «del 6 al 10, cinco capítulos sin carga (lo escrito; consta, no se reescribe)»;
  - el tramo 8–14 se queda en un 69 % «por el 8» (A114);
  - del prólogo al 9, la lectora sigue viendo un 40 % de romance (A106).
- **No repetir:** «Al derivar un modelo, retirar las adendas del modelo de origen en vez de apilarlas», y poner un archivo rector con la trama A,
  su medida y sus suelos (`REGISTROS_APRENDIZAJE.md`, 003).
- **En general:** al adaptar un método de un género a otro, se quitan las reglas del género de origen y se pone un suelo medible para lo que
  define el género nuevo. Declararlo no basta.

### 3.2 Los borradores que se saltaron el cierre y las entregas que no existían (08-08)

- **Qué pasó:** los ocho defectos de los caps. 1–2 (`LEEME-h` §5): sin señal de género, horas que no cuadran, erratas, remates-resumen, la paleta
  que falta, el volcado de datos, las dos voces que suenan igual, el cierre estático. Además, el NEXT y el DIFF de aquel día «declaran entregas que
  no existen (39 plantillas, un zip, una novela de validación, estilometría y autoinforme)» (`LEEME-h` §1).
- **Coste:**
  - la v1.1 entera;
  - el cap. 2 sigue siendo el valle de todas las lecturas: 4–5 de la lectora, 5,5 de las externas;
  - se recortó tres veces (A82, A84, A103).
- **No repetir:** se da por hecho lo que existe en el repo («Hecha si existe…», en `NEXT.md` §2), no lo que dice el informe de la ventana.
- **En general:** el trabajo de una ventana se comprueba por lo que existe en el repositorio, nunca por lo que la ventana dice haber hecho.

### 3.3 Las excepciones a una regla de enganche

- **Qué pasó:** la v1.1 ensayó una excepción de cierre estático, y la primera obra la retiró «por criterio de la lectora» (adenda §5; A82).
- **En general:** las reglas que sostienen el enganche no llevan excepciones de estilo.

### 3.4 Los tics de la narradora y las muletillas

- **Qué pasó:**
  - «cuento hasta tres», siete veces en siete capítulos; la nuca erizada; demasiada madera (A86; `PLAN` §H.2–3);
  - la lectora los tiene «pillados» (`PLAN` §K.2);
  - en el 11, «el bar como muleta: nueve veces en mil palabras» (`C11_lectura_editorial.md` §2);
  - en el 13, tres sentencias seguidas, «un tic» (`C13_…` §2);
  - en Cruz, «No pienso en eso» y las aperturas con cifra («cada capítulo empieza con una cifra, ya lo veo venir», `PLAN` §S.3);
  - en la estructura: todos los cierres de Cruz, él mirándola (A114).
- **Coste:** cortes en cinco capítulos (A86) y una segunda pasada (`PLAN` §H bis). Desde entonces, C-9 y un contador por obra en el preset.
- **En general:** cada narrador tiene una lista de tics vigilados y un contador. Una muletilla sale como mucho una vez por capítulo, y un motivo que
  vuelve tiene que cambiar algo.

### 3.5 Los espejos y los resúmenes de lo que la lectora ya ha leído

Es el defecto que más se repite y no se ha curado:

| Dónde | Qué se repetía |
|---|---|
| Caps. 5 y 6 | El tablón, «casi palabra por palabra» (`PLAN` §H) |
| El 9 | El bar desde él, calcado del 7 |
| El 12 viejo | El viernes, que ya contaba el 11 |
| El 10 | «Salvat no hace noches» («me lo acababa de decir el enfermero») |
| El 12 nuevo | La pelea del prólogo («ya me la sé») |
| El 15 | El perfil que «repasa el libro» |
| El 16 | «el folio del 15 contado otra vez» |

- Desde el 14, el NEXT lo pide: «nada del caso que la lectora ya haya leído» (`PLAN` §W.3). Aun así vuelve en el 15 y el 16, y el NEXT del 17 lo repite.
- **En general:** si un capítulo pasa por algo que el lector ya leyó, comparte con eso un detalle como mucho y da solo lo nuevo. Hay que comprobarlo
  en el cierre y en la lectura, porque el encargo solo no lo evita.

### 3.6 Explicar lo que ya se ve (glosas, frases-resumen, aforismos)

- **Qué pasó:**
  - en la v9Beta, «frases-resumen y aforismos»;
  - en agosto, «Cruz se explica con remates-resumen»;
  - en la v2.0 se sigue cortando en casi cada C.5: «tres frases que explicaban» en el 4 (A106), lo del 10 (A108), dos en el 11 (A109), tres
    sentencias en el 13 (A112), una réplica en el 14 (A113);
  - la ventana del 16 anotó en su acta el corte de C-2 («Para otro.») y no lo aplicó. Lo arregló en otro commit (`8c343be`).
- **En general:** el narrador no explica lo que la escena ya muestra. El cierre lo corta y la lectura de otro caza lo que se le escapa al cierre.

### 3.7 Fusiones y cortes que rompen costuras

- **Qué pasó:**
  - la fusión A84 rompió dos remisiones («¿Y quién firma…? / —Mara.» y «los pago yo, el primero de cada mes…») que «nadie había visto», hasta la
    revisión de las externas (`PLAN` §H);
  - A103 dejó cuatro costuras graves en la fusión del 8 y una en el 4 (`informes/cortes_A103/`);
  - después de cortar, la lectora se lió con «—Mara» y creyó que firmaba ella (`PLAN` §H bis).
- **Qué se cambió:** «después de cortar, siempre una correctora de continuidad sin contexto» (`PLAN` §H bis; `ORQUESTADOR.md` §6).
- **En general:** cada corte o fusión que toca más de un capítulo lo relee un corrector de continuidad sin contexto, porque los cortes rompen las
  remisiones.

### 3.8 Los frenazos

- **Qué pasó:**
  - el plan tenía cuatro interrupciones (prólogo, 13, 18, 23). La lectora: «tres cortes los aguanto; un cuarto, no» y «a la tercera ya no es tensión:
    me torean» (`PLAN` §L.2, §M.6, §N.2);
  - en el 13, el corte del móvil: «lo he visto mil veces y me ha dado rabia» (`PLAN` §V.3).
- **Qué se cambió:** el autor decidió que el *edging* de la abstinencia es deseo sostenido, sin cortes (A101).
- **En general:** las interrupciones de la tensión principal se cuentan por libro, con un tope bajo. El deseo sostenido no necesita un corte para
  serlo.

### 3.9 Defender un 🔒 contra la lectora hasta la tercera vez (las cámaras)

- **Qué pasó:**
  - la lectora pide que ella descubra las cámaras en el 11, el 15 y el 16;
  - después de la segunda, el orquestador lo mantuvo por delegación (A116, «el 18 hace creíble que ella no las vea»);
  - a la tercera, el autor eligió la B (A118).
- **Coste:** una reescaleta (A4) y su correctora, con cuatro graves (A119).
- **Evidencia:** la regla funcionó como estaba escrita. Si es un error es discutible: lo que costó fue una ronda más.
- **En general:** cuando el lector pide dos veces algo que el diseño tiene cerrado, se prepara ya la consulta al autor con opciones, en vez de
  justificar el diseño en el texto.

### 3.10 Fiarse de la medida de quien escribe

- **Qué pasó:** el acta da sistemáticamente más pareja que la editora y la lectora (§1.2.7). El caso extremo es el 14: acta 94 %, editora 75 %,
  lectora 35 %.
- **En general:** la cuenta de quien escribió sirve de registro, no de veredicto. Manda una medida independiente.

### 3.11 Las fichas con extensiones viejas

- **Qué pasó:** tres actas seguidas (14, 15, 16) avisan de que la ficha no recalcula la extensión cuando las notas recortan materia. El bloque 4 da
  ≈ 4.755 de las ≈ 6.350 declaradas.
- **Qué se cambió:** el autor fija el libro en ≈ 52.000 y dice «no se rellena» (A119).
- **En general:** cuando una nota quita materia a una ficha, la ficha anota su extensión nueva. Nunca se rellena para llegar a una cifra.

### 3.12 Fallos de operación (`CUAD` §6)

- Doce agentes a la vez agotaron el límite de la sesión (22-10). Con la biblia entera en el paquete, cuatro bastaron (23-10).
- Al compactar la conversación, «el consumo se va de madre».
- Ventanas que suben ajustes después de su informe: E2 a los 42 minutos, A3 a los 26. La auditoría de A1 «leyó la versión anterior».
- Paquetes de lectura con los rótulos de la numeración vieja (A111).
- Cifras de un informe sin sumar: la primera vez «hacia el 50 %» no cabía con las extensiones (A97).
- En la prueba a ciegas, una búsqueda en la biblia enseñó a DR-01 canon de la versión descartada (`cap03_…` §1), y desde ahí se aísla (adenda §7).
- **En general:**
  - como mucho unos cuatro agentes a la vez;
  - un relevo antes que compactar;
  - antes de auditar, comprobar que no hay commits posteriores al informe;
  - las cifras de un informe se suman antes de darlas por buenas;
  - en una prueba a ciegas, el material de la versión descartada queda fuera del alcance de quien escribe.

---

## 4. Las prácticas del orquestador que sostienen la calidad

### 4.1 No escribe, y deja una ventana limpia por encargo

- **La práctica:** el orquestador acumula la memoria y no redacta capítulos. Cada ventana de trabajo empieza con el contexto limpio, «que es lo que
  mejor escribe» (`ORQUESTADOR.md` §0).
- **Ejemplo:** el NEXT del 17 prohíbe «la lectura editorial, y lanzar lectoras o correctoras propias: el capítulo lo lee quien no lo ha escrito», y
  también «otras ramas, el repo `Devpac/Agnostico9` y las conversaciones pasadas» (`NEXT.md` §5).
- **En general:** quien acumula la memoria del proyecto no escribe. Cada pieza la escribe una sesión nueva, que solo lee lo que le manda el encargo.

### 4.2 Cómo se encarga un capítulo

El encargo es un `NEXT.md` (`PLANTILLA_NEXT.md`). Contiene:

- el estado de cada parte, con lo que tiene que existir en el repo;
- lo que se lee antes y después del borrador;
- **«Entre ellos»** primero, y la escena;
- lo que pide la lectora, con su sección de `PLAN`;
- el calor, la voz, el trato y los contadores;
- lo que el narrador no sabe y lo que no hace;
- el peso de pareja y la extensión como techo;
- el cierre;
- **«Se decide al escribir»**;
- lo prohibido y la verificación.

No hay ninguna consigna de prosa.

- **Ejemplo:** el NEXT del 17 da el «Cierra con» (ella abre el coche y él está en el copiloto) y deja a la ventana «las palabras exactas sobre el padre,
  qué la hace reír, qué le da a Salvat». Para el peso: «Que la parte de pareja la ocupe ella con él, no el caso» (`NEXT.md` §4).
- **En general:** el encargo fija qué pasa, qué cambia entre los protagonistas, qué no se sabe todavía y cómo termina. Deja el cómo a quien escribe.

### 4.3 Lo que lee cada ventana

- **Antes de escribir:**
  - toda la obra escrita, en orden, y la del narrador del capítulo dos veces;
  - las dos fichas con sus notas vN («lo tachado no vale»);
  - las secciones de `PLAN` que tocan;
  - las secciones de la biblia y las filas A-NN concretas;
  - el preset como contrato de canon.
- **Después del borrador:** los filtros (`NEXT.md` §3; `CUAD` §6, «Lo que lee cada NEXT de capítulo»).
- **Ejemplo:** en el 17, «Lo de Mara, dos veces: el prólogo, el 2, el 4…»; «El 15 y el 16, otra vez»; «Del 16, ella no sabe nada de lo que pensó u oyó
  él». Lo que se cobra después se lee «solo para saber qué se cobra después (no se escriben ni se adelantan)».
- **En general:** quien escribe lee entero lo ya escrito y las decisiones que le tocan. Lee dos veces la voz que tiene que escribir. Las reglas de
  oficio las lee al cerrar.

### 4.4 El cierre deja una prueba que se puede comprobar

- **La práctica:** el acta lleva una línea por comprobación (pasos 1–7 de la base, C-1 a C-10), las palabras, las fricciones del catálogo y las
  propuestas de canon (adenda §4).
- **Ejemplos:**
  - el acta del 16 dice «C-2: Para otro.», y el capítulo se corrige en `8c343be` para que coincida;
  - las fricciones del 14, el 15 y el 16 (la extensión de las fichas, C-10 con un tercero, el hecho visible en el narrador hermético) suben a
    «mejoras del modelo para llevar al autor» (`CUAD` §1, séptimo relevo).
- **En general:** el cierre deja un acta que se puede contrastar con el texto. Lo que un capítulo descubre de las reglas se apunta para mejorar el
  método, no para el capítulo siguiente.

### 4.5 La lectura: dos agentes nuevos, a la vez, con paquetes distintos

- **La práctica** (`ORQUESTADOR.md` §5; `PROTOCOLO_LECTURA.md` §2–§5):
  - una editora con la ficha y lo publicado antes;
  - una lectora tipo con todo, del prólogo al capítulo, numerado como se publica y con la línea del narrador;
  - ninguna lee la biblia, el brief ni el acta;
  - las lecturas en bruto se guardan en `informes/lecturas_C5/`.
- **Ejemplos:**
  - sin la línea del narrador, la lectora «no sabía que él se llama Cruz» (`PLAN` §H bis);
  - la editora del 5 tardó trece minutos con la indicación «de leer como editora y no hacer recuentos con scripts», frente a más de dos horas de la del
    prólogo (`CUAD` §6).
- **En general:** cada lectura la hace un agente nuevo que solo recibe lo que leería el público (y el editor, la ficha). No lee notas de diseño.

### 4.6 Cortar antes que añadir

- **La práctica:** como mucho tres problemas, cada uno con una corrección mínima. Si hay que añadir, solo el beat que falta, en una o dos líneas. Nunca
  se reescribe desde el orquestador. Los cortes se aplican con un script que comprueba que cada cadena aparece una sola vez (`ORQUESTADOR.md` §6;
  `CUAD` §6).
- **Ejemplos:**
  - el prólogo pasa de 1.307 a 1.225 palabras; el 10, de 1.397 a 1.330; el 15, de 1.145 a 1.065, «sin añadir nada»;
  - los pocos añadidos son un beat que faltaba: «A la policía no la voy a esperar. / A ella, sí.» (el 9); la línea de consentimiento antes del beso (el
    13); «La quiero ahí otra vez.» (el 14, lo pide la lectora).
- **En general:** se corrige cortando. Solo se añade el beat que falta, en una o dos líneas, y si hace falta más, el capítulo vuelve a una sesión de
  reescritura con lo que dijeron las lecturas.

### 4.7 Qué hace con lo que dice la lectora

- **La práctica:** cada lectura tiene su sección en `PLAN`, con una flecha a dónde va cada cosa: una nota v4 en la ficha siguiente, el NEXT, la pasada
  final o el autor si es 🔒. Hay tres reglas:
  - **manda la lectora** sobre la editora;
  - **tres lecturas = problema confirmado**;
  - se mira el **orden** de sus notas, no la cifra.
- **Ejemplos:**
  - «Se queda, aunque la editora proponía cortarlo»: «tarda en hacer lo siguiente» (A105), «No me lo sacudo» (A106), el remolino (A108), «Me sobra uno»
    (A111);
  - la cadena del 13 al 16: la lectora pide «que él hable: una frase suya que me destroce» y «algo posesivo dicho a ella» (§V.5). Entra «La quiero ahí
    otra vez.» (A113). Sigue pidiéndolo, va al NEXT del 16 y sale «Quiero oírselo»: «§W.4, cumplido» (`PLAN` §Y.1).
- **En general:** cada petición del lector queda apuntada con su destino, y se comprueba en la lectura siguiente si se cumplió.

### 4.8 Una auditoría periódica independiente y lecturas externas

- **La práctica:** cada ~7 capítulos, una OPERACIÓN D corta, con lectoras externas si el autor las pasa (`ORQUESTADOR.md` §2.5).
- **Ejemplo:** la del 8–14 encuentra el tic de los cierres de Cruz y dos costuras del 14 (A114).
- **En general:** cada tramo lo mide un agente sin contexto contra lo declarado, y busca patrones que una lectura de capítulo no ve.

### 4.9 Las puertas del autor, solo para lo cerrado, y con la opción recomendada

- **La práctica:** el orquestador decide por delegación los cortes, la coherencia y el canon menor. Al autor le pregunta lo 🔒, las muertes, el reparto
  y el calor, con «la opción recomendada primero y por qué (si la lectora tipo la prefiere, se dice)» (`ORQUESTADOR.md` §7).
- **Ejemplos:**
  - las cámaras: las dos lectoras, B > A > C. El autor: «Sí, apruebo B» (A118);
  - las seis preguntas de A4: «Vale así» (A119).
- **En general:** el autor solo decide lo irreversible o lo que está cerrado, y recibe la pregunta con las opciones y la que prefiere el lector.

### 4.10 La memoria en el repo y los relevos

- **La práctica:**
  - el cuaderno se lee primero en cada relevo;
  - el Anexo A guarda cada decisión con fecha y origen;
  - `HIST` guarda todas las notas;
  - los commits llevan el resumen de cada lectura;
  - la regla es «relevo antes que compactar»;
  - el orquestador espera a que el autor avise, sin vigilancia en segundo plano;
  - no lee la biblia entera: usa `grep` y `sed`, y el agente lee el paquete (`CUAD` §6).
- **Ejemplo:** ocho relevos del 22-10 al 29-10, cada uno con «todo subido […] y nada a medias» (`CUAD` §1).
- **En general:** todo lo que hace falta para continuar vive en el repositorio, y un relevo puede retomar el trabajo con solo leer el cuaderno.

---

## 5. Lo que no se sabe

1. **Si la v2.0 escribe mejor o solo diseña mejor.**
   - La prueba a ciegas «antes de fusionar» se canceló (A110).
   - La editora no distingue las versiones (7,7–8,4 frente a 7,4–8,5 desde el 3).
   - La subida de la lectora coincide con más pareja por diseño y con capítulos más avanzados en la historia.
2. **Qué parte de la prosa se debe a cada pieza del paquete v1.1:** el cierre, la lectura por otra, el brief de una hoja o la ausencia de consignas. Solo
   hay una prueba a ciegas, y es del paquete entero. La de v1.2 contra v1.1 da una diferencia «pequeña» que el propio repo atribuye en parte a la
   variación.
3. **Si el esfuerzo máximo importa:** se decidió «sin pruebas a ciegas».
4. **Cuál es la medida de pareja que predice el enganche.** Acta, editora, OPD y lectora dan cifras distintas (§1.2.7). Un 65 % de romance da un 6 en el 15
   y un 7 en el 16, y un 60 % da un 8,5 en el 13. Parece que pesan más el cara a cara en escena y lo que no se repite, pero no se ha probado.
5. **Si la lectora tipo predice a lectoras reales.** No hay ningún dato de mercado ni de lectoras humanas en el repo. Las únicas externas (1–7) son otros
   modelos y ordenan igual que ella. Las del 8–14 no han llegado.
6. **La deriva de la escala.** El mismo capítulo baja cuando el libro mejora: el 9 viejo (hoy el 7) pasa de 10 a 7–8, y el 3 de 8 a 6. La primera nota de
   cada capítulo nuevo es más baja que la de la relectura siguiente (§1.2.5). No se sabe qué nota usar para el listón.
7. **Si las estimaciones «con cortes» de la editora se cumplen.** Casi nunca se vuelven a medir. La única relectura completa tras cortes da +1, pero también
   suben capítulos sin tocar (`PLAN` §H bis).
8. **Si «manda la lectora» mejora la calidad o solo el enganche.** Hay líneas que la editora cortaba y se quedaron. Nadie ha medido si el texto final es mejor
   para una editora.
9. **Si las notas del encargo («nada que la lectora ya haya leído») evitan los recaps.** Hasta ahora no: vuelven en el 15 y el 16 (§3.5). Tampoco está claro
   si una nota así respeta la regla del fork.
10. **El calor está sin probar en página.** Los suelos de la v2.0 (la primera vez hacia el 50 %, *edging* sin cortes, el pinar) caen del 21 en adelante,
    todavía sin escribir. Lo mismo la opción B de las cámaras (19, 20, 24, 40).
11. **La extensión.** El libro baja de ≈ 62.000 a ≈ 52.000 porque los capítulos que cumplen las notas salen cortos (A119). No se sabe si la lectora lo nota.
12. **El arranque.** El 1 sigue con «bajón» al pasar del prólogo (7). Lo que pide la lectora para el 1 espera a la lectura de la muestra gratuita y a la
    pasada final (A104, A110).
13. **Si el método se lleva a otra saga.** La v1.3 sacó 7/10 en una saga nueva de otro subgénero y 6/10 en el paso al libro 2, pero eso mide autosuficiencia,
    no calidad. Ninguna otra obra se ha escrito todavía con la v2.0.
