# Maquetador

Convierte los capítulos de un libro de la fábrica en los archivos para publicar en Amazon KDP. El **código** vive aquí, en Editorial, y vale para cualquier saga. La **configuración de cada libro** (títulos, textos, cubierta, orden de los capítulos) vive en la saga, en su carpeta `publicacion/`.

| Sale | Para qué |
|---|---|
| `libro_NN.epub` | Ebook (KDP / Kindle Unlimited). EPUB 3 válido en epubcheck, con metadatos de serie. |
| `libro_NN_interior.pdf` | Interior de tapa blanda, con el medianil de KDP calculado según el número de páginas. |
| `portada_ebook.jpg` | Portada del ebook, 1600 × 2560 px. |
| `cubierta_papel.pdf` | Cubierta completa de tapa blanda (contraportada + lomo + portada), con el lomo calculado según las páginas reales. |
| `control_*.png` | Para revisar a ojo: miniaturas al tamaño de Amazon y cubierta de papel con guías de corte, zona segura y hueco del código de barras. |
| `ficha_kdp.md` | Lo que se copia en KDP: descripción, palabras clave, serie, declaración de IA, medidas de lomo y cubierta, e informe del libro. |

Antes de generar nada revisa los capítulos. Si queda andamiaje del método (`[INVENTADO]`, `[FALTA]`, claves `CP-nnn`, decisiones `A92`, ventanas `DR-10`, `§27`, `TODO`…), **se niega a maquetar**. Las carreteras (`la A-6`) no cuentan. Las faltas tipográficas (comillas rectas, guion en lugar de raya, `...`, espacios dobles) las avisa, pero no las corrige: el texto es del autor.

## Instalación (Windows)

1. Python 3.9 o superior: <https://www.python.org/downloads/>. En el instalador, marca *Add python.exe to PATH*.
2. En una terminal, dentro de esta carpeta (`Editorial/maquetador`):

   ```
   pip install -r requirements.txt
   ```

No hace falta LaTeX, Pandoc ni Vellum: el PDF lo compone [Typst](https://typst.app), que se instala con `pip`.

Para comprobar la instalación:

```
python maquetar.py ejemplo/libro_01.yaml
```

## Uso

Los repos, uno junto al otro:

```
Documents/GitHub/
├── Editorial/          ← la fábrica y este maquetador
└── MiSaga/             ← la saga
    ├── libro_01/       ← los capítulos (solo se leen)
    └── publicacion/    ← serie.yaml, libro_NN.yaml, portadas/ (y fuentes/, si la saga trae las suyas)
```

Desde `Editorial/maquetador`:

```
python maquetar.py ../../MiSaga/publicacion/libro_01.yaml              # todo
python maquetar.py ../../MiSaga/publicacion/libro_01.yaml --revisar    # solo comprobar los capítulos
python maquetar.py ../../MiSaga/publicacion/libro_01.yaml --solo epub  # o --solo pdf, o --solo cubierta
python maquetar.py ../../MiSaga/publicacion/libro_01.yaml --forzar     # maquetar aunque haya andamiaje (solo pruebas)
```

Los archivos se escriben en `MiSaga/publicacion/salida/libro_01/`, que Git ignora (o donde diga `--salida`).

Una saga nueva trae `publicacion/` ya preparada (`herramientas/nueva_saga.py`, ver `ARRANQUE.md` de Editorial), con todo en `POR DEFINIR`.

## Configuración

- **`publicacion/serie.yaml`**: lo común a toda la serie (seudónimo, sello, newsletter, formato de impresión, fuente, diseño de cubierta, textos de la página final…).
- **`publicacion/libro_NN.yaml`**: lo de cada libro (título, carpeta de capítulos, orden, ISBN, descripción, palabras clave, aviso de contenido, siguiente libro…). Cualquier campo de la serie se puede sobrescribir aquí.

Para un libro nuevo, copia `libro_01.yaml` a `libro_02.yaml` y cambia número, título, carpeta, orden y textos.

Lo que siga en `POR DEFINIR` sale avisado en la terminal y en la ficha.

### Qué archivos y en qué orden

`orden:` en la ficha del libro dice de qué archivo sale cada capítulo publicado, en orden. El número publicado lo pone el maquetador por posición; los `## N` de los archivos se ignoran, así que da igual que un archivo conserve el número de su escaleta. Una entrada con comodines (`"C*_capitulo.md"`) trae todos los que encajen, ordenados por su número, y así los capítulos nuevos entran solos a medida que se escriben. Si en la carpeta queda un archivo que parece texto del libro y no está en el orden, lo avisa.

```yaml
orden:
  - prologo.md          # «## Prólogo»: sale sin número
  - capitulo_01.md      # 1
  - capitulo_05.md      # 2, aunque el archivo diga «## 5»
  - "C*_capitulo.md"    # el resto, por su número
```

Sin `orden:`, se usan los `capitulo_NN.md` de la carpeta por su número.

### Formato de los capítulos

Es el que produce el método:

```markdown
# TÍTULO DEL LIBRO                    ← cabecera repetida: se ignora
## Nombre de la serie — Libro 1
---
## 7                                  ← número de capítulo (o «## Prólogo», «## Epílogo»)
### ELLA                              ← punto de vista (el nombre del narrador)

Texto con *cursiva* y **negrita**.

---                                   ← cambio de escena (sale como ⁂)
### ÉL                                ← cambio de narrador a mitad de capítulo (sale rotulado)
```

### Impresión

| Campo | Por defecto | Notas |
|---|---|---|
| `formato` | `5.5x8.5` | También `5x8`, `5.06x7.81`, `5.25x8` y `6x9`. |
| `papel` | `crema` | O `blanco`. Cambia el grosor del lomo. |
| `fuente` | Libertinus Serif | Para otra fuente, ponla en `publicacion/fuentes/` de la saga (.ttf/.otf) o instálala. |
| `cuerpo` | 11 | Puntos. |
| `capitulo_en_impar` | `false` | `true` abre cada capítulo en página impar (más páginas). |
| `sangrar_primero` | `false` | Sangría en el primer párrafo tras un título o un cambio de escena. |

El **medianil** no se configura. KDP exige un mínimo según el número de páginas (0,375 in hasta 150, 0,5 hasta 300, 0,625 hasta 500…). El maquetador compila, cuenta las páginas, aplica el mínimo más 1/8 in de holgura y vuelve a compilar si cambia de tramo.

## Cubiertas

El sistema es el mismo para toda la serie: un generador de imágenes pinta **solo el objeto** sobre negro puro, sin texto; el maquetador pone el título, la autora y la línea de serie con una plantilla común, para que la tipografía sea idéntica en todos los tomos y no haya erratas. Las instrucciones para el generador se escriben una vez por saga, a partir de `portadas/INSTRUCCIONES_GPT_plantilla.md`, en la carpeta `publicacion/portadas/` de la saga.

- **Título** arriba, en Bodoni Moda condensada (o la fuente de `cubierta.fuente`). Cada línea llena el ancho, y el reparto se decide con `portada.titulo_lineas`.
- **Encuadre del objeto:** se detecta solo en la imagen y se centra en la franja central, así que da igual si salió grande o pequeño. Se puede retocar con `zoom`, `desplazar_x` y `desplazar_y`.
- **La autora** y la línea de serie **NOMBRE DE LA SERIE · N**, abajo.
- **Contraportada** con la descripción del libro (o con `portada.contraportada`), y el hueco del código de barras libre.
- **Lomo** con título y autora, solo si el libro supera las 79 páginas.

Lo común a toda la serie (fuente, color, condensación, sentido del lomo) está en `cubierta:` dentro de `serie.yaml`.

Si la imagen sale a menos de 300 ppp en papel, el maquetador lo avisa. Las imágenes de 1024 × 1536 hay que ampliarlas ×2 con [Upscayl](https://upscayl.org) antes de imprimir.

## Qué lleva cada libro

**Ebook:** portadilla con la serie y el número, créditos, dedicatoria (si la hay), aviso de contenido, índice, capítulos y una página final con «La historia continúa en…», el gancho del siguiente libro, el enlace (botón `final.boton_siguiente`, por defecto «Léelo ya en Kindle»), la petición de reseña y la newsletter. Esa página es la que tira del read-through en Kindle Unlimited.

**Tapa blanda:** las mismas partes. La portadilla va en impar y los créditos en par. El cuerpo empieza en impar con el folio 1, con cabeceras en versalitas (autora en las pares, título en las impares). Los arranques de capítulo y las páginas en blanco van sin cabecera.

## Estructura

```
maquetar.py            ← punto de entrada
maquetador/
  lector.py            ← lee los capítulos (orden, prólogo, cambio de narrador)
  revision.py          ← andamiaje y tipografía
  epub.py              ← EPUB 3
  pdf.py               ← interior con Typst (medianil automático)
  kdp.py               ← medidas de KDP: formatos, medianil, lomo, cubierta
  cubierta.py          ← portada del ebook, cubierta de papel y controles
  ficha.py             ← ficha_kdp.md
  config.py            ← carga y valores por defecto
plantillas/            ← interior.typ, epub.css, cubierta.typ (comunes a todas las sagas)
portadas/              ← plantilla de instrucciones para el generador de imágenes
fuentes/               ← Bodoni Moda (licencia OFL) para las cubiertas
ejemplo/               ← una serie y un libro de prueba
```

*Origen:* el maquetador nació en `Devpac/maquetador` para *Madera y Pólvora*; esta copia es la misma herramienta sin la configuración de esa obra (comprobado: con su ficha produce el mismo EPUB, el mismo interior, la misma portada y la misma ficha).
