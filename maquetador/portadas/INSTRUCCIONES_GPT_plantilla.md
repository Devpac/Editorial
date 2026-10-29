# Portadas · instrucciones para el generador de imágenes — PLANTILLA

> Plantilla de la fábrica. Cada saga la copia a `publicacion/portadas/INSTRUCCIONES_GPT.md` y
> rellena lo que va entre corchetes. **Lo que no va entre corchetes no se toca:** son las
> condiciones que necesita el maquetador para poner el texto y alargar el lienzo (fondo negro
> puro, sin texto, zonas vacías arriba y abajo). Lo que va entre corchetes es el sistema visual de
> la saga (el objeto, sus materiales, su único color), y se decide una vez con el autor.

Sistema de cubiertas de *[TÍTULO DE LA SAGA]*, una saga de [N] libros de [SUBGÉNERO] escrita por [AUTORA].

**Reparto del trabajo:** el generador pinta solo el objeto sobre fondo negro, sin texto. El maquetador añade el título, la autora y la línea de serie con una plantilla común, para que la tipografía sea idéntica en todos los tomos y no haya erratas ni tildes mal puestas. Como el fondo es negro puro, el lienzo se puede alargar al tamaño del ebook y a la cubierta completa de papel (contraportada + lomo + portada) sin que se note el añadido.

---

## 1. Instrucciones fijas

Pégalas al empezar el chat, o ponlas como instrucciones de un proyecto para no repetirlas.

```
Vas a generar las ilustraciones de cubierta de una saga de [N] novelas de [SUBGÉNERO]. Todas siguen el mismo sistema visual. Cumple estas reglas en cada imagen, sin excepciones:

FORMATO
- Vertical, proporción 2:3, a la máxima resolución que puedas.

FONDO
- Negro puro y uniforme (#000000) en toda la imagen.
- Sin degradados, viñeteado, textura, superficie, mesa, sombra proyectada ni reflejos en el suelo. El objeto flota sobre el negro.

OBJETO
- Un único objeto por cubierta, fotografiado como un bodegón de producto: [ESTILO: por ejemplo, hiperrealista, nítido de punta a punta, con detalle de material].
- [LUZ: por ejemplo, una sola luz suave lateral, desde arriba a la izquierda, que lo recorta del negro].
- [POSICIÓN: por ejemplo, en diagonal, a tres cuartos].

COMPOSICIÓN (imprescindible: el texto se añade después)
- El objeto es GRANDE y protagonista: ocupa entre el 55 % y el 65 % del ancho y llena la franja central, desde el 40 % hasta el 84 % de la altura.
- El 35 % superior queda completamente negro y vacío (ahí irá el título).
- El 12 % inferior queda completamente negro y vacío (ahí irán la autora y la serie).
- Ninguna parte del objeto a menos de un 8 % de cualquier borde.

COLOR
- [PALETA DE LA SAGA: por ejemplo, casi monocroma, con los materiales del mundo de la saga].
- [ACENTO: si la saga tiene un único color saturado, cuál, dónde y de qué tamaño; tiene que verse incluso con la imagen del tamaño de un sello].

PROHIBIDO
- Cualquier letra, número, palabra, logotipo, firma o marca de agua.
- [LO QUE LA SAGA VETA EN SUS CUBIERTAS: por ejemplo, personas, manos, caras o siluetas; armas visibles; gore explícito].

Cuando te pida una cubierta solo te daré el objeto [y el detalle de acento]. Todo lo demás es fijo.
```

## 2. Pedido por libro

```
Cubierta del libro [N]: [OBJETO, con su estado y su material]. [Detalle de acento: DÓNDE ESTÁ].
```

## 3. Antes de darla por buena

- [ ] El fondo es negro puro, sin superficie, sin degradado y sin sombra en el suelo.
- [ ] No hay ninguna letra, número ni marca.
- [ ] El tercio superior y la franja inferior están vacíos.
- [ ] El objeto no se acerca a los bordes.
- [ ] El objeto es grande: llena la franja central y ocupa más de la mitad del ancho.
- [ ] [El acento, si lo hay, se ve en miniatura.]
- [ ] Al verla del tamaño de un sello, el objeto se reconoce.

Si falla algo, **pide otra en lugar de retocarla**: el sistema depende de que todas salgan iguales.

Fallos habituales y cómo pedir la corrección en el mismo chat:

- **Objeto pequeño:** «Repítela con el objeto mucho más grande, entre el 55 % y el 65 % del ancho, desde el 40 % hasta el 84 % de la altura. Todo lo demás igual.»
- **Acento invisible:** «El detalle de [color] tiene que verse con claridad con la imagen del tamaño de un sello. Todo lo demás igual.»
- **Aparece texto:** «Sin ninguna letra ni número. Todo lo demás igual.»

## 4. Guardar

1. Si la imagen sale a 1024 × 1536 px o menos, amplíala ×2 con [Upscayl](https://upscayl.org) (gratuito, funciona en Windows): para imprimir hace falta más.
2. Guárdala en esta carpeta como `libro_NN_objeto.png`, por ejemplo `libro_01_objeto.png`, y pon esa ruta en `portada.imagen` de `publicacion/libro_NN.yaml`. El maquetador detecta el objeto y lo encuadra solo; si hace falta afinar, usa `zoom`, `desplazar_x` y `desplazar_y`.
3. Anota el objeto en la tabla de abajo para que no se repita en otro tomo.
4. En KDP, en la declaración de IA, marca las imágenes como **generadas** (en `publicacion/serie.yaml`: `ia.imagenes`).

## 5. Registro de objetos

Ningún objeto se repite. [Criterio de la saga para elegirlos: por ejemplo, alternar entre los mundos de los dos protagonistas.]

| Libro | Título | Objeto | Acento | Estado |
|---:|---|---|---|---|
| 1 | | | | |
