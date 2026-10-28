# PLANTILLA_CUADERNO.md — el cuaderno del orquestador (MODELO_DarkRomance v2.0)

> Archivo de **modelo**. Cada obra tiene un `CUADERNO_<OBRA>.md` en la raíz de su repo, que solo
> escribe el orquestador (`ORQUESTADOR.md`, §9). Es lo primero que lee un relevo. Corto: una o dos
> pantallas. Lo que tiene su propio archivo no se copia aquí; se enlaza.

---

```
# CUADERNO_<OBRA>.md — <título de la saga>

## 1. Dónde estamos
- **Fase:** <0–5> · **Libro:** <N> · **Último encargo cerrado:** <código> (<qué>, commit <hash>)
- **Próximo encargo:** <código> — <qué>. Su NEXT está en `NEXT.md` (o: «por escribir»).
- **Pendiente de auditar:** <nada | código subido y sin leer>.

## 2. Decisiones permanentes del autor
Con sus palabras y la fecha. Ejemplos de lo que va aquí: su criterio de delegación; si manda la
lectora; permisos permanentes («mueve sin miedo»); el esfuerzo de las ventanas; prioridades
(«quiero ventas y lectoras»); líneas rojas.

## 3. Estado de la obra
- Biblia: versión <vX.Y>, última decisión <A-NN>.
- Preset: al día con la biblia <sí/no>.
- Forma de la saga: <A, la misma pareja en muchos libros · B, dúo o trilogía · C, parejas rotativas>.
- Libros cerrados: <lista, con su fila «Cierre del libro» del Anexo A>.
- Libro <N>: diseño <estado>, escaleta <estado>, ampliada <estado>, capítulos cerrados <lista o rango>.
- Numeración: <si la escaleta y el libro publicado difieren, cómo>.
- Códigos de ventana: <los del libro 1 (B1, E1, C01…); del libro 2 en adelante con el número del
  libro delante (L2-D1, L2-E1, L2-C01…); o la numeración propia de la obra, si la tenía>.

## 4. Pendientes abiertos
Lo que está decidido pero sin hacer, o preguntado y sin respuesta: <lista corta, con quién lo tiene>.

## 5. Notas del libro en curso
Lo que no cabe en el plan de la lectora ni en la continuidad y el relevo necesita saber (p. ej.,
«la lectora tipo puntúa un punto por debajo de las externas»; «el cap. X se fundió con el Y»).

## 6. Índice de archivos de la obra
- `<obra>_biblia.md` · `PRESET_<OBRA>.md` · `NEXT.md`
- `libro_NN/`: `diseño_libro.md` (del libro 2 en adelante), `escaleta.md`, `escaletaAmpliada.md`,
  `continuidad.md`, `plan_lectora.md`, `historial_lecturas.md` (forma: `PLANTILLA_LIBRO.md`),
  `capitulo_NN.md`, `capNN_brief.md`, `capNN_acta.md`, `capNN_lectura_editorial.md`
- Lo histórico: <carpeta de referencia, si la hay>
```
