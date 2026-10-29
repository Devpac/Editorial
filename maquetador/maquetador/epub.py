"""Genera un EPUB 3 listo para subir a KDP (y válido para cualquier tienda)."""
from __future__ import annotations

import datetime as dt
import mimetypes
import uuid
import zipfile
from html import escape
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .config import parrafos
from .modelo import CambioPov, Capitulo, Parrafo, Separador

CSS = (Path(__file__).parent.parent / "plantillas" / "epub.css")

XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<title>{titulo}</title>
<link rel="stylesheet" type="text/css" href="estilo.css"/>
</head>
<body{clase}>
{cuerpo}
</body>
</html>
"""


def _identificador(cfg: Dict[str, Any]) -> str:
    isbn = (cfg["isbn"] or {}).get("ebook")
    if isbn:
        return "urn:isbn:" + isbn.replace("-", "").replace(" ", "")
    semilla = f"{cfg['serie'].get('nombre')}|{cfg['numero']}|{cfg['titulo']}|{cfg['autor']}"
    return "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, semilla))


def _tramos_html(p: Parrafo) -> str:
    partes = []
    for t in p.tramos:
        if t.salto:
            partes.append("<br/>")
            continue
        h = escape(t.texto, quote=False)
        if t.cursiva:
            h = f"<i>{h}</i>"
        if t.negrita:
            h = f"<b>{h}</b>"
        partes.append(h)
    return "".join(partes)


def _capitulo_html(c: Capitulo, separador: str) -> str:
    if c.titulo:
        tipo = {"prólogo": "prologue", "epílogo": "epilogue"}.get(c.titulo.lower(), "chapter")
        out = [f'<section epub:type="{tipo}" role="doc-{tipo}">',
               f'<h1 class="num titulo">{escape(c.titulo)}</h1>']
    else:
        out = ['<section epub:type="chapter" role="doc-chapter">',
               f'<h1 class="num">{c.numero}</h1>']
    if c.pov:
        out.append(f'<p class="pov">{escape(c.pov.title())}</p>')
    inicial = True
    for b in c.bloques:
        if isinstance(b, Separador):
            out.append(f'<p class="sep" role="separator">{escape(separador)}</p>')
            inicial = True
        elif isinstance(b, CambioPov):
            out.append(f'<p class="pov pov-dentro">{escape(b.pov.title())}</p>')
            inicial = True
        else:
            clase = ' class="inicial"' if inicial else ""
            out.append(f"<p{clase}>{_tramos_html(b)}</p>")
            inicial = False
    out.append("</section>")
    return "\n".join(out)


def _p(texto: str, clase: str = "") -> str:
    c = f' class="{clase}"' if clase else ""
    return f"<p{c}>{escape(texto, quote=False)}</p>"


def _enlace(texto: str, url: str, clase: str = "") -> str:
    c = f' class="{clase}"' if clase else ""
    return f'<p{c}><a href="{escape(url)}">{escape(texto, quote=False)}</a></p>'


def generar(cfg: Dict[str, Any], capitulos: List[Capitulo], destino: Path) -> Path:
    lang = cfg["idioma"].split("-")[0]
    titulo = cfg["titulo"]
    serie = cfg["serie"].get("nombre") or ""
    sep = cfg["ebook"].get("separador", "⁂")
    paginas: List[Tuple[str, str, str, str]] = []  # (id, archivo, titulo_nav, xhtml)

    def pagina(id_, cuerpo, titulo_nav="", clase=""):
        archivo = f"{id_}.xhtml"
        html = XHTML.format(lang=lang, titulo=escape(titulo_nav or titulo),
                            clase=f' class="{clase}"' if clase else "", cuerpo=cuerpo)
        paginas.append((id_, archivo, titulo_nav, html))

    portada = cfg["portada"].get("ebook")
    if portada:
        portada = Path(portada)
        pagina("portada",
               f'<section epub:type="cover" class="portada"><img src="imagenes/portada{portada.suffix.lower()}" alt="{escape(titulo)}"/></section>',
               "", "portada")

    # Portadilla
    cuerpo = ['<section epub:type="titlepage" class="portadilla">']
    if serie:
        cuerpo.append(_p(f"{serie} · Libro {cfg['numero']}", "serie"))
    cuerpo.append(f'<h1 class="titulo">{escape(titulo)}</h1>')
    if cfg["subtitulo"]:
        cuerpo.append(_p(cfg["subtitulo"], "subtitulo"))
    cuerpo.append(_p(cfg["autor"], "autor"))
    cuerpo.append("</section>")
    pagina("portadilla", "\n".join(cuerpo), "Portadilla")

    # Créditos
    cuerpo = ['<section epub:type="copyright-page" class="creditos">', _p(f"{titulo}"),
              _p(cfg["derechos"]), _p(cfg["edicion"] + f", {cfg['anio']}")]
    if cfg["sello"]:
        cuerpo.append(_p(f"Publicado por {cfg['sello']}"))
    if (cfg["isbn"] or {}).get("ebook"):
        cuerpo.append(_p(f"ISBN: {cfg['isbn']['ebook']}"))
    for linea in cfg["creditos_extra"]:
        cuerpo.append(_p(linea))
    for linea in parrafos(cfg["aviso_legal"]):
        cuerpo.append(_p(linea, "legal"))
    cuerpo.append("</section>")
    pagina("creditos", "\n".join(cuerpo), "Créditos")

    if cfg["dedicatoria"]:
        cuerpo = '<section epub:type="dedication" class="dedicatoria">' + \
                 "".join(_p(x) for x in parrafos(cfg["dedicatoria"])) + "</section>"
        pagina("dedicatoria", cuerpo, "Dedicatoria")

    if cfg["aviso_contenido"]:
        cuerpo = ['<section epub:type="preface" class="aviso">', "<h2>Aviso de contenido</h2>"]
        cuerpo += [_p(x) for x in parrafos(cfg["aviso_contenido"])]
        cuerpo.append("</section>")
        pagina("aviso", "\n".join(cuerpo), "Aviso de contenido")

    primer_capitulo = None
    for i, c in enumerate(capitulos):
        id_ = f"cap{i:03d}"
        primer_capitulo = primer_capitulo or f"{id_}.xhtml"
        pagina(id_, _capitulo_html(c, sep), c.rotulo, "capitulo")

    # Páginas finales: lo que mueve el read-through en KU
    fin = cfg["final"]
    sig = cfg["siguiente"] or {}
    cuerpo = ['<section epub:type="afterword" class="final">']
    if fin.get("gracias"):
        cuerpo.append(f'<h2>{escape(fin["gracias"])}</h2>')
    if sig.get("titulo"):
        cuerpo.append(_p(f"La historia continúa en", "continua"))
        cuerpo.append(f'<p class="siguiente">{escape(sig["titulo"])}</p>')
        if serie:
            cuerpo.append(_p(f"{serie} · Libro {cfg['numero'] + 1}", "serie"))
        for x in parrafos(sig.get("gancho", "")):
            cuerpo.append(_p(x, "gancho"))
        if sig.get("enlace"):
            cuerpo.append(_enlace(fin.get("boton_siguiente") or "Léelo ya", sig["enlace"], "boton"))
    if fin.get("resena"):
        cuerpo.append(_p(fin["resena"], "resena"))
    if cfg["newsletter"]:
        cuerpo.append(_p("Para enterarte antes que nadie de cada nuevo libro:", "centro"))
        cuerpo.append(_enlace("Apúntate a la lista de correo", cfg["newsletter"], "boton"))
    if cfg["web"]:
        cuerpo.append(_enlace(cfg["web"].replace("https://", "").rstrip("/"), cfg["web"], "centro"))
    cuerpo.append("</section>")
    pagina("final", "\n".join(cuerpo), "Antes de irte")

    if cfg["otros_libros"]:
        cuerpo = ['<section epub:type="appendix" class="otros">', f"<h2>{escape(serie or 'De la misma autora')}</h2>"]
        for i, l in enumerate(cfg["otros_libros"], start=1):
            if isinstance(l, dict):
                t = l.get("titulo", "")
                cuerpo.append(_enlace(t, l["enlace"]) if l.get("enlace") else _p(t))
            else:
                cuerpo.append(_p(str(l)))
        cuerpo.append("</section>")
        pagina("otros", "\n".join(cuerpo), "Otros libros")

    # Índice (nav)
    entradas = "\n".join(f'<li><a href="{a}">{escape(t)}</a></li>'
                         for _, a, t, _ in paginas if t and t not in ("Portadilla", "Créditos"))
    hitos = ['<li><a epub:type="toc" href="indice.xhtml">Índice</a></li>']
    if portada:
        hitos.insert(0, '<li><a epub:type="cover" href="portada.xhtml">Cubierta</a></li>')
    if primer_capitulo:
        hitos.append(f'<li><a epub:type="bodymatter" href="{primer_capitulo}">Comienzo</a></li>')
    nav = (f'<nav epub:type="toc" id="toc" role="doc-toc"><h2>Índice</h2><ol>\n{entradas}\n</ol></nav>\n'
           f'<nav epub:type="landmarks" hidden=""><ol>{"".join(hitos)}</ol></nav>')
    nav_html = XHTML.format(lang=lang, titulo="Índice", clase=' class="indice"', cuerpo=nav)

    ident = _identificador(cfg)
    ahora = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    # Orden de lectura: el índice va tras los preliminares
    orden = [p for p in paginas]
    pos_indice = next((i for i, p in enumerate(orden) if p[0].startswith("cap")), len(orden))

    manifest = ['<item id="nav" href="indice.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="css" href="estilo.css" media-type="text/css"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>']
    if portada:
        mime = mimetypes.guess_type(portada.name)[0] or "image/jpeg"
        manifest.append(f'<item id="img-portada" href="imagenes/portada{portada.suffix.lower()}" '
                        f'media-type="{mime}" properties="cover-image"/>')
    for id_, archivo, _, _ in orden:
        manifest.append(f'<item id="{id_}" href="{archivo}" media-type="application/xhtml+xml"/>')
    spine = [f'<itemref idref="{p[0]}"/>' for p in orden[:pos_indice]] + \
            ['<itemref idref="nav"/>'] + [f'<itemref idref="{p[0]}"/>' for p in orden[pos_indice:]]

    meta = [f'<dc:identifier id="bookid">{escape(ident)}</dc:identifier>',
            f"<dc:title>{escape(titulo)}</dc:title>",
            f'<dc:creator id="autor">{escape(cfg["autor"])}</dc:creator>',
            '<meta refines="#autor" property="role" scheme="marc:relators">aut</meta>',
            f"<dc:language>{escape(cfg['idioma'])}</dc:language>",
            f"<dc:date>{cfg['anio']}</dc:date>",
            f'<meta property="dcterms:modified">{ahora}</meta>',
            f"<dc:rights>{escape(cfg['derechos'])}</dc:rights>"]
    if cfg["sello"]:
        meta.append(f"<dc:publisher>{escape(cfg['sello'])}</dc:publisher>")
    descripcion = cfg["descripcion"] if "POR DEFINIR" not in cfg["descripcion"] else ""
    if descripcion:
        meta.append(f"<dc:description>{escape(' '.join(parrafos(descripcion)))}</dc:description>")
    for kw in cfg["palabras_clave"]:
        meta.append(f"<dc:subject>{escape(str(kw))}</dc:subject>")
    if serie:
        meta += [f'<meta property="belongs-to-collection" id="serie">{escape(serie)}</meta>',
                 '<meta refines="#serie" property="collection-type">series</meta>',
                 f'<meta refines="#serie" property="group-position">{cfg["numero"]}</meta>']
    if portada:
        meta.append('<meta name="cover" content="img-portada"/>')

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
{chr(10).join(meta)}
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
</package>
"""

    puntos = []
    n = 0
    for id_, archivo, t, _ in orden:
        if not t or t in ("Portadilla", "Créditos"):
            continue
        n += 1
        puntos.append(f'<navPoint id="np{n}" playOrder="{n}"><navLabel><text>{escape(t)}</text></navLabel>'
                      f'<content src="{archivo}"/></navPoint>')
    ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="{lang}">
<head><meta name="dtb:uid" content="{escape(ident)}"/><meta name="dtb:depth" content="1"/>
<meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head>
<docTitle><text>{escape(titulo)}</text></docTitle>
<navMap>
{chr(10).join(puntos)}
</navMap>
</ncx>
"""

    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""

    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        def w(nombre, contenido):
            z.writestr(nombre, contenido, compress_type=zipfile.ZIP_DEFLATED)
        w("META-INF/container.xml", container)
        w("OEBPS/content.opf", opf)
        w("OEBPS/toc.ncx", ncx)
        w("OEBPS/indice.xhtml", nav_html)
        w("OEBPS/estilo.css", CSS.read_text(encoding="utf-8"))
        for _, archivo, _, html in orden:
            w(f"OEBPS/{archivo}", html)
        if portada:
            z.write(portada, f"OEBPS/imagenes/portada{portada.suffix.lower()}", compress_type=zipfile.ZIP_STORED)
    return destino
