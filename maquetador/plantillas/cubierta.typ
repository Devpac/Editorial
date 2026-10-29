// Cubierta: portada del ebook o cubierta completa de papel.
// No se edita a mano: todo sale de cubierta.json, que genera maquetador/cubierta.py.
// Unidades en pulgadas salvo que se diga otra cosa.

#let d = json(sys.inputs.at("datos", default: "cubierta.json"))
#let u = 1in
#let tinta = rgb(d.color_texto)

#set page(width: d.pagina.ancho * u, height: d.pagina.alto * u, margin: 0pt, fill: black)
#set text(font: d.fuente, fill: tinta, lang: "es", hyphenate: false)
#set par(justify: false, first-line-indent: 0pt)

#let espaciado(t, tracking, size) = text(size: size, tracking: tracking, upper(t))

// Título: cada línea llena el ancho disponible (condensada en horizontal), con
// un tope de proporción entre líneas y un tope de altura total.
#let titulo(lineas, ancho, alto-max) = context {
  let c = d.condensar
  let base = 100pt
  let caja(l, s) = text(size: s, weight: d.peso_titulo, top-edge: "cap-height", bottom-edge: "baseline", l)
  let medidas = lineas.map(l => measure(caja(l, base)))
  let tam = medidas.map(m => base * (ancho / (m.width * c)))
  let menor = calc.min(..tam.map(t => t / 1pt)) * 1pt
  tam = tam.map(t => calc.min(t / 1pt, menor / 1pt * d.proporcion_max_lineas) * 1pt)
  let hueco = 0.14
  let alto = (range(lineas.len()).map(i => medidas.at(i).height * (tam.at(i) / base)).sum()
              + tam.slice(1).map(t => t * hueco).sum(default: 0pt))
  let k = calc.min(1.0, alto-max / alto)
  stack(dir: ttb, spacing: 0pt, ..range(lineas.len()).map(i => {
    let s = tam.at(i) * k
    let bloque = align(center, scale(x: c * 100%, reflow: true, caja(lineas.at(i), s)))
    if i == 0 { bloque } else { v(s * hueco) + bloque }
  }))
}

// Línea de serie con filetes a los lados: ── NOMBRE DE LA SERIE · 1 ──
#let linea-serie(t, ancho, size) = {
  let filete = box(width: 1fr, inset: (bottom: size * 0.32), line(length: 100%, stroke: 0.5pt + tinta))
  box(width: ancho, grid(columns: (1fr, auto, 1fr), column-gutter: size * 1.2, align: horizon,
    filete, espaciado(t, 0.28em, size), filete))
}

// Panel delantero. (x, y) = esquina superior izquierda del área de corte.
#let frente(f, x, y) = {
  let W = f.ancho * u
  let H = f.alto * u
  let m = f.seguro * u
  // Imagen: geometría calculada en Python (encuadre automático del objeto)
  place(top + left, dx: x - f.sangrado_izq * u, dy: y - f.sangrado * u,
    box(width: W + (f.sangrado_izq + f.sangrado_der) * u, height: H + 2 * f.sangrado * u, clip: true,
      place(top + left, dx: (f.img_x + f.sangrado_izq) * u, dy: (f.img_y + f.sangrado) * u,
        image(d.imagen, width: f.img_ancho * u, height: f.img_alto * u, fit: "stretch"))))
  // Título
  let tw = calc.min(W - 2 * m, W * d.ancho_titulo)
  place(top + left, dx: x + (W - tw) / 2, dy: y + f.titulo_arriba * H,
    box(width: tw, titulo(d.titulo_lineas, tw, (f.titulo_abajo - f.titulo_arriba) * H)))
  // Lema (opcional)
  if d.lema != "" {
    place(top + left, dx: x + m, dy: y + f.lema_y * H,
      box(width: W - 2 * m, align(center, espaciado(d.lema, 0.3em, W * 0.024))))
  }
  // Autora
  place(top + left, dx: x + m, dy: y + f.autor_y * H,
    box(width: W - 2 * m, align(center, text(weight: 500, espaciado(d.autor, 0.22em, W * f.autor_tam)))))
  // Serie
  if d.serie != "" {
    place(top + left, dx: x + W * 0.1, dy: y + f.serie_y * H,
      linea-serie(d.serie, W * 0.8, W * 0.026))
  }
}

#if d.modo == "ebook" {
  frente(d.frente, 0pt, 0pt)
} else {
  let b = d.sangrado * u
  let W = d.corte.ancho * u
  let H = d.corte.alto * u
  let L = d.lomo * u
  // Contraportada
  let mc = 0.55 * u
  place(top + left, dx: b + mc, dy: b + 0.85 * u, box(width: W - 2 * mc, {
    set text(size: d.contra_tam * 1pt)
    set par(leading: 0.62em, spacing: 1.05em, justify: false)
    if d.contra_gancho != "" {
      align(center, text(size: 1.35em, style: "italic", d.contra_gancho))
      v(1.4em)
    }
    for p in d.contra_texto { align(center, p); parbreak() }
  }))
  place(top + left, dx: b + mc, dy: b + H - 0.62 * u - 0.24 * u, box(width: W - 2 * mc - 2.1 * u,
    align(left, espaciado(d.autor, 0.22em, 9pt))))
  // Lomo
  if d.texto_en_lomo {
    let s = d.lomo_tam * 1pt
    place(top + left, dx: b + W, dy: b, box(width: L, height: H, align(center + horizon,
      rotate(d.lomo_giro * 1deg, reflow: true, box(width: H - 1.2 * u,
        grid(columns: (auto, 1fr, auto), align: horizon,
          text(size: s, tracking: 0.12em, upper(d.titulo)),
          [],
          text(size: s * 0.8, tracking: 0.2em, upper(d.autor))))))))
  }
  // Portada
  frente(d.frente, b + W + L, b)
  // Guías (solo en la vista previa)
  if d.guias {
    let g = 0.6pt + rgb("#00c8ff")
    let r = 0.6pt + rgb("#ff3b6b")
    let corte(x, y, w, h, s) = place(top + left, dx: x, dy: y, rect(width: w, height: h, stroke: s))
    corte(b, b, 2 * W + L, H, g)                       // corte
    corte(b + W, b, L, H, g)                           // lomo
    let sg = 0.25 * u
    corte(b + sg, b + sg, W - 2 * sg, H - 2 * sg, r)   // zona segura trasera
    corte(b + W + L + sg, b + sg, W - 2 * sg, H - 2 * sg, r)
    corte(b + W - 0.25 * u - 2 * u, b + H - 0.25 * u - 1.2 * u, 2 * u, 1.2 * u,
          (paint: rgb("#ffd400"), thickness: 0.8pt, dash: "dashed"))  // código de barras
  }
}
