"""Interior PDF de tapa blanda con Typst (se instala con pip, sin LaTeX)."""
from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

import typst

from . import kdp
from .config import parrafos
from .modelo import CambioPov, Capitulo, Separador

PLANTILLA = Path(__file__).parent.parent / "plantillas" / "interior.typ"
FUENTES = Path(__file__).parent.parent / "fuentes"


def _datos(cfg: Dict[str, Any], capitulos: List[Capitulo], interior: float) -> Dict[str, Any]:
    imp = cfg["impresion"]
    ancho, alto = kdp.FORMATOS[imp["formato"]]
    sig = cfg["siguiente"] or {}
    return {
        "titulo": cfg["titulo"],
        "subtitulo": cfg["subtitulo"] or "",
        "autor": cfg["autor"],
        "serie": cfg["serie"].get("nombre") or "",
        "numero": cfg["numero"],
        "sello": cfg["sello"] or "",
        "anio": str(cfg["anio"]),
        "edicion": cfg["edicion"],
        "derechos": cfg["derechos"],
        "isbn": (cfg["isbn"] or {}).get("tapa_blanda") or "",
        "creditos_extra": list(cfg["creditos_extra"]),
        "aviso_legal": parrafos(cfg["aviso_legal"]),
        "dedicatoria": parrafos(cfg["dedicatoria"]),
        "aviso_contenido": parrafos(cfg["aviso_contenido"]),
        "newsletter": cfg["newsletter"] or "",
        "web": cfg["web"] or "",
        "final": {"gracias": cfg["final"].get("gracias") or "", "resena": cfg["final"].get("resena") or ""},
        "siguiente": {"titulo": sig.get("titulo") or "", "gancho": parrafos(sig.get("gancho") or "")},
        "fuente": imp["fuente"],
        "cuerpo": imp["cuerpo"],
        "interlineado": imp["interlineado"],
        "separador": imp["separador"],
        "capitulo_en_impar": bool(imp["capitulo_en_impar"]),
        "sangrar_primero": bool(imp.get("sangrar_primero", False)),
        "pagina": {"ancho": ancho, "alto": alto, "interior": interior,
                   "exterior": imp["exterior"], "superior": imp["superior"], "inferior": imp["inferior"]},
        "capitulos": [
            {"numero": c.numero,
             "titulo": c.titulo,
             "pov": c.pov.title() if c.pov else None,
             "bloques": _bloques(c)}
            for c in capitulos
        ],
    }


def _bloques(c: Capitulo) -> List[Dict[str, Any]]:
    salida = []
    inicial = True
    for b in c.bloques:
        if isinstance(b, Separador):
            salida.append({"t": "sep"})
            inicial = True
        elif isinstance(b, CambioPov):
            salida.append({"t": "pov", "x": b.pov.title()})
            inicial = True
        else:
            salida.append({"t": "p", "ini": inicial,
                           "r": [{"x": t.texto, "i": t.cursiva, "b": t.negrita, "br": t.salto} for t in b.tramos]})
            inicial = False
    return salida


def generar(cfg: Dict[str, Any], capitulos: List[Capitulo], destino: Path) -> Tuple[Path, int, float]:
    """Compila el interior. Devuelve (ruta, páginas, medianil usado).

    El medianil mínimo de KDP depende del número de páginas, y el número de
    páginas depende del medianil: se compila, se cuenta y se recompila si
    cambia de tramo.
    """
    holgura = 0.125  # por encima del mínimo, para que el texto no se hunda en el lomo
    interior = kdp.medianil_minimo(250) + holgura
    fuentes = [str(d) for d in (FUENTES, cfg["_ruta_yaml"].parent / "fuentes") if d.is_dir()]  # las de la saga, en publicacion/fuentes/

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        shutil.copy(PLANTILLA, tmp / "interior.typ")
        paginas = 0
        for _ in range(4):
            (tmp / "datos.json").write_text(json.dumps(_datos(cfg, capitulos, interior), ensure_ascii=False),
                                            encoding="utf-8")
            entrada = str(tmp / "interior.typ")
            resultado = typst.query(entrada, "<paginas>", field="value", root=str(tmp), font_paths=fuentes)
            paginas = json.loads(resultado)[0]
            necesario = kdp.medianil_minimo(paginas) + holgura
            if abs(necesario - interior) < 1e-9:
                break
            interior = necesario
        destino.parent.mkdir(parents=True, exist_ok=True)
        typst.compile(entrada, output=str(destino), root=str(tmp), font_paths=fuentes)
        if cfg.get("_guardar_typst"):
            shutil.copy(tmp / "datos.json", destino.with_suffix(".json"))
    return destino, paginas, interior
