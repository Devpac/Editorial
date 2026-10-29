"""Ficha para copiar y pegar en KDP + informe de la maquetación."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import kdp
from .config import parrafos, pendientes
from .modelo import CambioPov, Capitulo

MAX_DESCRIPCION = 4000
MAX_PALABRAS_CLAVE = 7
MAX_LARGO_CLAVE = 50


def _avisos_ficha(cfg: Dict[str, Any]) -> List[str]:
    av = []
    desc = cfg["descripcion"] or ""
    if len(desc) > MAX_DESCRIPCION:
        av.append(f"la descripción tiene {len(desc)} caracteres (KDP admite {MAX_DESCRIPCION})")
    kws = cfg["palabras_clave"] or []
    if len(kws) > MAX_PALABRAS_CLAVE:
        av.append(f"hay {len(kws)} palabras clave (KDP admite {MAX_PALABRAS_CLAVE})")
    for k in kws:
        if len(str(k)) > MAX_LARGO_CLAVE:
            av.append(f"palabra clave de más de {MAX_LARGO_CLAVE} caracteres: «{k}»")
    if not kws:
        av.append("sin palabras clave")
    if not cfg["categorias"]:
        av.append("sin categorías")
    for campo in pendientes(cfg):
        av.append(f"campo pendiente: {campo}")
    return av


def escribir(cfg: Dict[str, Any], capitulos: List[Capitulo], paginas: Optional[int],
             medianil: Optional[float], errores: List[str], avisos: List[str],
             cubierta: Optional[Dict[str, Any]] = None) -> str:
    imp = cfg["impresion"]
    serie = cfg["serie"].get("nombre") or ""
    palabras = sum(c.palabras for c in capitulos)
    l: List[str] = []
    w = l.append

    w(f"# Ficha KDP — {cfg['titulo']}")
    w("")
    w("Generada por el maquetador. Los campos se copian tal cual en KDP.")
    w("")
    w("## Detalles del libro")
    w("")
    w(f"- **Idioma:** {cfg['idioma']}")
    w(f"- **Título:** {cfg['titulo']}")
    w(f"- **Subtítulo:** {cfg['subtitulo'] or '—'}")
    if serie:
        w(f"- **Serie:** {serie} · número {cfg['numero']}")
    w(f"- **Autor:** {cfg['autor']}")
    w(f"- **Sello:** {cfg['sello'] or '— (KDP pone «Independently published»)'}")
    w(f"- **Categorías:** " + ("; ".join(cfg["categorias"]) if cfg["categorias"] else "—"))
    w("")
    w("### Descripción")
    w("")
    w("```")
    w("\n\n".join(parrafos(cfg["descripcion"])))
    w("```")
    w(f"{len(cfg['descripcion'] or '')} / {MAX_DESCRIPCION} caracteres")
    w("")
    w("### Palabras clave")
    w("")
    for i in range(MAX_PALABRAS_CLAVE):
        kws = cfg["palabras_clave"] or []
        w(f"{i + 1}. {kws[i] if i < len(kws) else '—'}")
    w("")
    w("### Contenido generado por IA")
    w("")
    w("KDP pide declarar el contenido *generado* por IA (texto, imágenes, traducción). "
      "El contenido *asistido* (corregir, revisar, idear) no hay que declararlo.")
    w("")
    ia = cfg["ia"]
    w(f"- Texto: {ia.get('texto')}")
    w(f"- Imágenes: {ia.get('imagenes')}")
    w(f"- Traducción: {ia.get('traduccion')}")
    w("")
    w("## Ebook")
    w("")
    w(f"- **ISBN:** {cfg['isbn'].get('ebook') or '— (no hace falta: Amazon asigna ASIN)'}")
    w(f"- **Archivo:** `{cfg['_id']}.epub`")
    w(f"- **Portada:** `portada_ebook.jpg` (1600 × 2560 px), se sube aparte en KDP"
      + (" y también va dentro del EPUB" if cfg['portada'].get('ebook') else ""))
    w("")
    w("## Tapa blanda")
    w("")
    if paginas:
        cub = kdp.cubierta(imp["formato"], imp["papel"], paginas)
        ancho, alto = kdp.FORMATOS[imp["formato"]]
        px = cub.px()
        w(f"- **ISBN:** {cfg['isbn'].get('tapa_blanda') or '— (ISBN gratuito de KDP)'}")
        w(f"- **Formato:** {ancho} × {alto} in ({ancho * kdp.MM:.1f} × {alto * kdp.MM:.1f} mm), sin sangrado")
        w(f"- **Papel:** {imp['papel']} · tinta negra")
        w(f"- **Páginas:** {paginas}")
        w(f"- **Medianil aplicado:** {medianil:.3f} in (mínimo KDP para {paginas} págs.: {kdp.medianil_minimo(paginas)} in)")
        w(f"- **Archivo interior:** `{cfg['_id']}_interior.pdf`")
        w("")
        w("### Cubierta completa (contraportada + lomo + portada, con sangrado)")
        w("")
        w(f"- **Lomo:** {cub.lomo:.4f} in ({cub.lomo * kdp.MM:.2f} mm)")
        w(f"- **Tamaño total:** {cub.ancho:.3f} × {cub.alto:.3f} in "
          f"({cub.ancho * kdp.MM:.1f} × {cub.alto * kdp.MM:.1f} mm)")
        w(f"- **A 300 ppp:** {px[0]} × {px[1]} px")
        w(f"- **Texto en el lomo:** {'sí' if cub.texto_en_lomo else 'no (menos de 80 páginas)'}")
        w("")
        if cubierta and (cubierta.get("papel")):
            w("- **Archivo:** `cubierta_papel.pdf` (vista con guías: `control_cubierta_papel.png`)")
        w("")
        w("Comprobar siempre con la calculadora de cubiertas de KDP antes de subirla.")
        if not (kdp.PAGINAS_MIN <= paginas <= kdp.PAGINAS_MAX):
            w("")
            w(f"**Atención:** KDP exige entre {kdp.PAGINAS_MIN} y {kdp.PAGINAS_MAX} páginas.")
    else:
        w("No se ha generado el interior.")
    w("")
    w("## Informe de maquetación")
    w("")
    w(f"- **Capítulos:** {len(capitulos)}")
    w(f"- **Palabras:** {palabras:,}".replace(",", "."))
    pov: Dict[str, int] = {}
    for c in capitulos:
        pov[c.pov or "—"] = pov.get(c.pov or "—", 0) + 1
    w("- **Punto de vista:** " + ", ".join(f"{k.title()} {v}" for k, v in pov.items()))
    w("")
    av_ficha = _avisos_ficha(cfg) + [f"cubierta: {a}" for a in (cubierta or {}).get("avisos", [])]
    if errores:
        w("### Errores")
        w("")
        for e in errores:
            w(f"- {e}")
        w("")
    if av_ficha or avisos:
        w("### Avisos")
        w("")
        for a in av_ficha + avisos:
            w(f"- {a}")
        w("")
    w("### Capítulos")
    w("")
    w("| Nº | POV | Palabras | Archivo |")
    w("|---:|---|---:|---|")
    for c in capitulos:
        num = c.titulo or c.numero
        povs = [(c.pov or "—").title()] + [b.pov.title() for b in c.bloques if isinstance(b, CambioPov)]
        w(f"| {num} | {' → '.join(povs)} | {c.palabras} | {c.origen} |")
    w("")
    return "\n".join(l)
