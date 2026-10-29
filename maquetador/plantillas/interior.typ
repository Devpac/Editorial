// Interior de tapa blanda para KDP.
// No se edita a mano por libro: todo sale de datos.json, que genera maquetar.py.

#let d = json(sys.inputs.at("datos", default: "datos.json"))
#let pg = d.pagina

#set document(title: d.titulo, author: d.autor)
#set text(font: d.fuente, size: d.cuerpo * 1pt, lang: "es", region: "ES", hyphenate: true)
#set par(justify: true, leading: d.interlineado * 1em, spacing: d.interlineado * 1em,
         first-line-indent: (amount: 1.2em, all: false))

// ── Marcas para saber qué página es qué ────────────────────────────────
// <ini>: empieza una sección que abre en impar · <fin>: acaba una sección
// <cuerpo>: primera página numerada · <fin-cuerpo>: tras el último capítulo
#let marca(l) = [#metadata(none) #l]

#let pagina-en(etiqueta, p) = query(etiqueta).any(m => m.location().page() == p)

// Página en blanco insertada para abrir en impar: la anterior cierra una
// sección y la siguiente abre otra.
#let es-blanca(p) = pagina-en(<fin>, p - 1) and pagina-en(<ini>, p + 1) and not pagina-en(<ini>, p)

#let en-cuerpo(p) = {
  let c = query(<cuerpo>)
  let f = query(<fin-cuerpo>)
  c.len() > 0 and p >= c.first().location().page() and (f.len() == 0 or p <= f.first().location().page())
}

#let versalitas(t) = text(tracking: 0.12em, smallcaps(lower(t)))

#set page(
  width: pg.ancho * 1in,
  height: pg.alto * 1in,
  binding: left,
  margin: (inside: pg.interior * 1in, outside: pg.exterior * 1in,
           top: pg.superior * 1in, bottom: pg.inferior * 1in),
  header-ascent: 40%,
  footer-descent: 35%,
  header: context {
    let p = here().page()
    if not en-cuerpo(p) or es-blanca(p) or pagina-en(<cap>, p) { return }
    set text(size: 0.78em)
    if calc.even(p) { align(center, versalitas(d.autor)) } else { align(center, versalitas(d.titulo)) }
  },
  footer: context {
    let p = here().page()
    if not en-cuerpo(p) or es-blanca(p) { return }
    set text(size: 0.85em)
    align(center, counter(page).display("1"))
  },
)

#let abrir-impar() = {
  marca(<fin>)
  pagebreak(to: "odd", weak: true)
  marca(<ini>)
}

#let tramo(t) = {
  if t.at("br", default: false) { return linebreak() }
  let c = [#t.x]
  if t.at("i", default: false) { c = emph(c) }
  if t.at("b", default: false) { c = strong(c) }
  c
}

#let separador = block(width: 100%, above: 1.1em, below: 1.1em, align(center, d.separador))

#let parrafo(b) = {
  let contenido = b.r.map(tramo).join()
  if b.at("ini", default: false) and not d.sangrar_primero {
    par(first-line-indent: (amount: 0em, all: true), contenido)
  } else {
    par(contenido)
  }
}

#let capitulo(c, primero: false) = {
  if primero { } else if d.capitulo_en_impar { abrir-impar() } else { pagebreak(weak: true) }
  marca(<cap>)
  v(pg.alto * 0.16in)
  if c.at("titulo", default: none) != none {
    align(center, text(size: 1.6em, versalitas(c.titulo)))
  } else {
    align(center, text(size: 2.6em, str(c.numero)))
  }
  if c.pov != none {
    v(0.2em)
    align(center, text(size: 0.95em, versalitas(c.pov)))
  }
  v(2.6em)
  for b in c.bloques {
    if b.t == "sep" { separador }
    else if b.t == "pov" { block(width: 100%, below: 1.6em, align(center, text(size: 0.95em, versalitas(b.x)))) }
    else { parrafo(b) }
  }
}

// ── Preliminares ───────────────────────────────────────────────────────
// 1. Portadilla (impar)
#marca(<ini>)
#align(center + horizon)[
  #if d.serie != "" [
    #versalitas(d.serie + " · Libro " + str(d.numero))
    #v(2.5em)
  ]
  #text(size: 2.4em, d.titulo)
  #if d.subtitulo != "" [
    #v(0.6em)
    #emph(d.subtitulo)
  ]
  #v(4em)
  #text(size: 1.15em, versalitas(d.autor))
]
#if d.sello != "" {
  place(bottom + center, text(size: 0.85em, versalitas(d.sello)))
}

// 2. Créditos (par)
#pagebreak()
#align(bottom)[
  #set text(size: 0.78em)
  #set par(justify: false, first-line-indent: 0em, spacing: 0.9em)
  #d.titulo \
  #d.derechos

  #d.edicion, #d.anio
  #if d.sello != "" [ \ Publicado por #d.sello ]
  #if d.isbn != "" [ \ ISBN: #d.isbn ]

  #for l in d.creditos_extra [#l \ ]

  #for l in d.aviso_legal [#l

  ]
]

// 3. Dedicatoria y aviso de contenido (impares)
#if d.dedicatoria.len() > 0 {
  abrir-impar()
  v(pg.alto * 0.25in)
  align(right, {
    set par(justify: false, first-line-indent: 0em)
    for l in d.dedicatoria [#emph(l) \ ]
  })
}

#if d.aviso_contenido.len() > 0 {
  abrir-impar()
  v(pg.alto * 0.12in)
  align(center, text(size: 1.05em, versalitas("Aviso de contenido")))
  v(1.5em)
  set par(first-line-indent: 0em, spacing: 0.9em)
  for l in d.aviso_contenido [#l

  ]
}

// ── Cuerpo ─────────────────────────────────────────────────────────────
#abrir-impar()
#counter(page).update(1)
#marca(<cuerpo>)
#for (i, c) in d.capitulos.enumerate() { capitulo(c, primero: i == 0) }
#marca(<fin-cuerpo>)

// ── Páginas finales ────────────────────────────────────────────────────
#abrir-impar()
#{
  set par(justify: false, first-line-indent: 0em, spacing: 1em)
  v(pg.alto * 0.12in)
  align(center)[
    #if d.final.gracias != "" [#text(size: 1.4em, d.final.gracias) #v(2em)]
    #if d.siguiente.titulo != "" [
      La historia continúa en
      #v(0.3em)
      #text(size: 1.6em, d.siguiente.titulo)
      #v(0.2em)
      #if d.serie != "" [#versalitas(d.serie + " · Libro " + str(d.numero + 1))]
      #v(1.2em)
    ]
  ]
  if d.siguiente.gancho.len() > 0 {
    set par(justify: true)
    for l in d.siguiente.gancho [#emph(l)

    ]
    v(1.2em)
  }
  align(center)[
    #if d.final.resena != "" [#text(size: 0.9em, d.final.resena) #v(1.2em)]
    #if d.newsletter != "" [Para enterarte antes que nadie de cada nuevo libro: \ #d.newsletter #v(0.6em)]
    #if d.web != "" [#d.web]
  ]
}

#context [#metadata(here().page()) <paginas>]
