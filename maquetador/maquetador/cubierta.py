"""Cubiertas: portada del ebook (JPG), cubierta completa de papel (PDF) y controles.

La imagen de partida es el objeto sobre negro puro que genera ChatGPT
(ver portadas/INSTRUCCIONES_GPT.md). El objeto se detecta automáticamente y se
encuadra en la franja central: no hace falta que GPT lo clave de tamaño.
"""
from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import typst
from PIL import Image, ImageDraw

from . import kdp
from .config import PENDIENTE, parrafos

PLANTILLA = Path(__file__).parent.parent / "plantillas" / "cubierta.typ"
FUENTES = Path(__file__).parent.parent / "fuentes"

EBOOK_PX = (1600, 2560)
EBOOK_IN = (5.0, 8.0)        # 320 ppp
UMBRAL_NEGRO = 40            # suma R+G+B por encima de la cual un píxel es «objeto»

# Maqueta del panel delantero, en fracciones del alto
TITULO_ARRIBA = 0.045
TITULO_ABAJO = 0.33
FRANJA_OBJETO = (0.37, 0.81)
ANCHO_OBJETO = 0.70          # ancho máximo del objeto respecto al panel
LEMA_Y = 0.355
AUTOR_Y = 0.855
SERIE_Y = 0.925


def _caja_objeto(img: Image.Image) -> Tuple[int, int, int, int]:
    gris = img.convert("RGB").point(lambda v: 255 if v > UMBRAL_NEGRO // 3 else 0).convert("L")
    gris = gris.point(lambda v: 255 if v > 0 else 0)
    caja = gris.getbbox()
    return caja or (0, 0, img.width, img.height)


def _geometria(img: Image.Image, ancho: float, alto: float, ajuste: Dict[str, Any]) -> Dict[str, float]:
    """Escala y posición de la imagen para que el objeto llene la franja central."""
    x0, y0, x1, y1 = _caja_objeto(img)
    ow, oh = (x1 - x0), (y1 - y0)
    fy0, fy1 = FRANJA_OBJETO
    escala = min(ANCHO_OBJETO * ancho / ow, (fy1 - fy0) * alto / oh)   # pulgadas por píxel
    escala *= float(ajuste.get("zoom", 1.0))
    cx_obj = (x0 + x1) / 2 * escala
    cy_obj = (y0 + y1) / 2 * escala
    cx = ancho / 2 + float(ajuste.get("desplazar_x", 0)) * ancho
    cy = (fy0 + fy1) / 2 * alto + float(ajuste.get("desplazar_y", 0)) * alto
    return {"img_ancho": img.width * escala, "img_alto": img.height * escala, "img_x": cx - cx_obj, "img_y": cy - cy_obj,
            "ppp": 1 / escala}


def _frente(img, ancho, alto, seguro, sangrado, sangrado_izq, sangrado_der, ajuste, autor_tam):
    g = _geometria(img, ancho, alto, ajuste)
    return {"ancho": ancho, "alto": alto, "seguro": seguro, "sangrado": sangrado,
            "sangrado_izq": sangrado_izq, "sangrado_der": sangrado_der,
            "titulo_arriba": TITULO_ARRIBA, "titulo_abajo": TITULO_ABAJO,
            "lema_y": LEMA_Y, "autor_y": AUTOR_Y, "serie_y": SERIE_Y, "autor_tam": autor_tam,
            **g}


def _lineas_titulo(cfg: Dict[str, Any]) -> List[str]:
    lineas = cfg["portada"].get("titulo_lineas")
    if lineas:
        return [str(l) for l in lineas]
    palabras = cfg["titulo"].split()
    if len(palabras) <= 1:
        return palabras
    if len(palabras) == 2:
        return palabras
    # Reparto equilibrado en dos líneas
    mejor = min(range(1, len(palabras)),
                key=lambda i: abs(len(" ".join(palabras[:i])) - len(" ".join(palabras[i:]))))
    return [" ".join(palabras[:mejor]), " ".join(palabras[mejor:])]


def _comunes(cfg: Dict[str, Any], imagen: str) -> Dict[str, Any]:
    cub = cfg["cubierta"]
    serie = cfg["serie"].get("nombre") or ""
    return {
        "imagen": imagen,
        "titulo": cfg["titulo"],
        "titulo_lineas": [l.upper() for l in _lineas_titulo(cfg)],
        "autor": cfg["autor"],
        "serie": f"{serie} · {cfg['numero']}" if serie else "",
        "lema": cfg["portada"].get("lema") or "",
        "fuente": cub["fuente"],
        "peso_titulo": cub["peso_titulo"],
        "color_texto": cub["color_texto"],
        "condensar": cub["condensar"],
        "proporcion_max_lineas": cub["proporcion_max_lineas"],
        "ancho_titulo": cub["ancho_titulo"],
    }


def _fuentes(cfg: Dict[str, Any]) -> list:
    """Las fuentes del maquetador y, si las tiene, las de la saga (publicacion/fuentes/)."""
    return [str(d) for d in (FUENTES, cfg["_ruta_yaml"].parent / "fuentes") if d.is_dir()]


def _compilar(datos: Dict[str, Any], imagen: Path, destino: Path, formato: str, ppp: Optional[int] = None,
              fuentes: Optional[list] = None) -> None:
    fuentes = fuentes or ([str(FUENTES)] if FUENTES.exists() else [])
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        shutil.copy(PLANTILLA, tmp / "cubierta.typ")
        shutil.copy(imagen, tmp / ("objeto" + imagen.suffix.lower()))
        (tmp / "cubierta.json").write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")
        kwargs = {"root": str(tmp), "font_paths": fuentes}
        if formato == "png":
            kwargs.update(format="png", ppi=ppp)
        typst.compile(str(tmp / "cubierta.typ"), output=str(destino), **kwargs)


def generar(cfg: Dict[str, Any], destino: Path, paginas: Optional[int]) -> Dict[str, Any]:
    """Devuelve un informe con rutas, resoluciones y avisos."""
    informe: Dict[str, Any] = {"avisos": [], "archivos": []}
    ruta_img = cfg["portada"].get("imagen")
    if not ruta_img:
        informe["avisos"].append("sin imagen de cubierta (portada.imagen)")
        return informe
    ruta_img = Path(ruta_img)
    if not ruta_img.exists():
        informe["avisos"].append(f"no existe la imagen de cubierta: {ruta_img}")
        return informe
    img = Image.open(ruta_img)
    if PENDIENTE in cfg["autor"]:
        informe["avisos"].append("la cubierta lleva «POR DEFINIR» como autora")
    nombre_img = "objeto" + ruta_img.suffix.lower()
    ajuste = cfg["portada"]
    comunes = _comunes(cfg, nombre_img)
    cub = cfg["cubierta"]

    # ── Ebook ──────────────────────────────────────────────────────────
    w, h = EBOOK_IN
    frente = _frente(img, w, h, seguro=w * 0.06, sangrado=0, sangrado_izq=0, sangrado_der=0,
                     ajuste=ajuste, autor_tam=cub["autor_tam"])
    datos = {**comunes, "modo": "ebook", "pagina": {"ancho": w, "alto": h}, "frente": frente}
    png = destino / "portada_ebook.png"
    _compilar(datos, ruta_img, png, "png", ppp=EBOOK_PX[0] / w, fuentes=_fuentes(cfg))
    jpg = destino / "portada_ebook.jpg"
    Image.open(png).convert("RGB").save(jpg, quality=92, dpi=(EBOOK_PX[0] / w,) * 2)
    png.unlink()
    informe["archivos"].append(jpg)
    informe["ebook_ppp_objeto"] = frente["ppp"]
    if frente["ppp"] < EBOOK_PX[0] / w * 0.8:
        informe["avisos"].append(
            f"la imagen se amplía en el ebook (sale a {frente['ppp']:.0f} ppp; ideal 320): conviene ampliarla con Upscayl")

    # Miniatura de control, al tamaño de los resultados de búsqueda de Amazon
    mini = Image.open(jpg)
    tira = Image.new("RGB", (40 + 160 + 20 + 80 + 20 + 50 + 20, 300), "white")
    x = 20
    for ancho in (160, 80, 50):
        m = mini.resize((ancho, round(ancho * mini.height / mini.width)), Image.LANCZOS)
        tira.paste(m, (x, 20))
        x += ancho + 20
    ruta_mini = destino / "control_miniaturas.png"
    tira.save(ruta_mini)
    informe["archivos"].append(ruta_mini)

    # ── Papel ──────────────────────────────────────────────────────────
    if not paginas:
        informe["avisos"].append("sin interior PDF: no se genera la cubierta de papel")
        return informe
    imp = cfg["impresion"]
    medidas = kdp.cubierta(imp["formato"], imp["papel"], paginas)
    W, H = kdp.FORMATOS[imp["formato"]]
    b = kdp.SANGRADO_CUBIERTA
    frente = _frente(img, W, H, seguro=0.25 + 0.05, sangrado=b, sangrado_izq=0, sangrado_der=b,
                     ajuste=ajuste, autor_tam=cub["autor_tam"])
    texto_contra = cfg["portada"].get("contraportada") or cfg["descripcion"]
    lomo_tam = min(13.0, medidas.lomo * 72 * 0.42)
    datos = {**comunes, "modo": "papel",
             "pagina": {"ancho": medidas.ancho, "alto": medidas.alto},
             "corte": {"ancho": W, "alto": H}, "sangrado": b, "lomo": medidas.lomo,
             "texto_en_lomo": medidas.texto_en_lomo and medidas.lomo >= 0.2,
             "lomo_tam": lomo_tam,
             "lomo_giro": 90 if cub["lomo"] == "descendente" else -90,
             "contra_gancho": cfg["portada"].get("gancho_contraportada") or "",
             "contra_texto": parrafos(texto_contra),
             "contra_tam": cub["contra_tam"],
             "frente": frente, "guias": False}
    pdf = destino / "cubierta_papel.pdf"
    _compilar(datos, ruta_img, pdf, "pdf", fuentes=_fuentes(cfg))
    informe["archivos"].append(pdf)
    guias = destino / "control_cubierta_papel.png"
    _compilar({**datos, "guias": True}, ruta_img, guias, "png", ppp=60, fuentes=_fuentes(cfg))
    informe["archivos"].append(guias)
    informe["papel_ppp_objeto"] = frente["ppp"]
    informe["papel"] = medidas
    if frente["ppp"] < 300:
        informe["avisos"].append(
            f"la imagen sale a {frente['ppp']:.0f} ppp en papel (KDP pide 300): amplíala ×2 con Upscayl")
    if not datos["texto_en_lomo"]:
        informe["avisos"].append("lomo sin texto (menos de 80 páginas o lomo demasiado estrecho)")
    return informe
