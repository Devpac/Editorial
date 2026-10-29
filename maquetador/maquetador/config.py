"""Carga obra/<libro>.yaml y la ficha de serie que referencia, con valores por defecto."""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Dict, List

import yaml

PENDIENTE = "POR DEFINIR"

POR_DEFECTO: Dict[str, Any] = {
    "autor": PENDIENTE,
    "sello": "",
    "idioma": "es-ES",
    "anio": 2026,
    "edicion": "Primera edición",
    "derechos": "© {anio} {autor}. Todos los derechos reservados.",
    "aviso_legal": (
        "Esta es una obra de ficción. Los nombres, personajes, lugares e incidentes son producto "
        "de la imaginación de la autora o se usan de manera ficticia. Cualquier parecido con "
        "personas reales, vivas o muertas, o con hechos reales es pura coincidencia.\n"
        "Queda prohibida la reproducción total o parcial de esta obra por cualquier medio sin "
        "autorización escrita del titular de los derechos."
    ),
    "creditos_extra": [],
    "newsletter": "",
    "web": "",
    "serie": {"nombre": "", "total_previsto": None},
    "numero": 1,
    "titulo": PENDIENTE,
    "subtitulo": "",
    "capitulos": "",
    "orden": [],                 # archivos en orden de publicación (admite comodines)
    "isbn": {"ebook": "", "tapa_blanda": ""},
    "dedicatoria": "",
    "aviso_contenido": "",
    "descripcion": PENDIENTE,
    "palabras_clave": [],
    "categorias": [],
    "otros_libros": [],
    "siguiente": {"titulo": "", "gancho": "", "enlace": ""},
    "final": {
        "gracias": "Gracias por leer.",
        "resena": "Si te ha gustado, una reseña en Amazon ayuda más de lo que imaginas a que otras lectoras encuentren la serie.",
        "boton_siguiente": "Léelo ya en Kindle",
    },
    "portada": {
        "imagen": "",            # objeto sobre negro (ChatGPT)
        "ebook": "",             # portada terminada que sustituye a la generada (opcional)
        "titulo_lineas": [],     # cómo partir el título; vacío = automático
        "lema": "",
        "gancho_contraportada": "",
        "contraportada": "",     # vacío = la descripción
        "zoom": 1.0,
        "desplazar_x": 0.0,
        "desplazar_y": 0.0,
        "incluir_en_epub": True,
    },
    "cubierta": {
        "fuente": "Bodoni Moda",
        "peso_titulo": 400,
        "color_texto": "#ECE5D8",
        "condensar": 0.8,
        "proporcion_max_lineas": 1.5,
        "ancho_titulo": 0.84,
        "autor_tam": 0.052,
        "contra_tam": 10.5,
        "lomo": "descendente",
    },
    "ia": {"texto": PENDIENTE, "imagenes": PENDIENTE, "traduccion": "no"},
    "impresion": {
        "formato": "5.5x8.5",
        "papel": "crema",
        "fuente": "Libertinus Serif",
        "cuerpo": 11,
        "interlineado": 0.62,
        "capitulo_en_impar": False,
        "sangrar_primero": False,
        "separador": "⁂",
        "exterior": 0.6,
        "superior": 0.75,
        "inferior": 0.7,
    },
    "ebook": {"separador": "⁂"},
}


def _fusionar(base: Dict[str, Any], encima: Dict[str, Any]) -> Dict[str, Any]:
    r = copy.deepcopy(base)
    for k, v in (encima or {}).items():
        if isinstance(v, dict) and isinstance(r.get(k), dict):
            r[k] = _fusionar(r[k], v)
        else:
            r[k] = v
    return r


def cargar(ruta_libro: Path) -> Dict[str, Any]:
    ruta_libro = ruta_libro.resolve()
    libro = yaml.safe_load(ruta_libro.read_text(encoding="utf-8")) or {}
    cfg = copy.deepcopy(POR_DEFECTO)
    ficha_serie = libro.pop("serie_config", None)
    if ficha_serie:
        ruta_serie = (ruta_libro.parent / ficha_serie).resolve()
        cfg = _fusionar(cfg, yaml.safe_load(ruta_serie.read_text(encoding="utf-8")) or {})
    cfg = _fusionar(cfg, libro)

    base = ruta_libro.parent
    cfg["_ruta_yaml"] = ruta_libro
    cfg["_id"] = ruta_libro.stem
    cfg["capitulos"] = (base / cfg["capitulos"]).resolve() if cfg["capitulos"] else None
    for clave in ("ebook", "imagen"):
        if cfg["portada"].get(clave):
            cfg["portada"][clave] = (base / cfg["portada"][clave]).resolve()
    for clave in ("derechos",):
        cfg[clave] = cfg[clave].format(anio=cfg["anio"], autor=cfg["autor"])
    return cfg


def pendientes(cfg: Dict[str, Any], prefijo: str = "") -> List[str]:
    """Campos que siguen en POR DEFINIR."""
    fuera = []
    for k, v in cfg.items():
        if k.startswith("_"):
            continue
        clave = f"{prefijo}{k}"
        if isinstance(v, dict):
            fuera += pendientes(v, clave + ".")
        elif isinstance(v, str) and PENDIENTE in v:
            fuera.append(clave)
        elif isinstance(v, list) and any(isinstance(x, str) and PENDIENTE in x for x in v):
            fuera.append(clave)
    return fuera


def parrafos(texto: str) -> List[str]:
    """Divide un bloque de texto del YAML en párrafos (línea en blanco o salto simple)."""
    if not texto:
        return []
    return [p.strip() for p in texto.strip().split("\n") if p.strip()]
