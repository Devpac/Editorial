"""Comprobaciones antes de maquetar.

* ERRORES (bloquean salvo --forzar): restos del andamiaje del modelo que no
  pueden llegar a una lectora: marcas [INVENTADO]/[FALTA], claves CP-nnn,
  referencias a secciones de la biblia, comentarios HTML, TODO...
* AVISOS (no bloquean): tipografía española (comillas rectas, guiones en
  lugar de raya, tres puntos...), numeración de capítulos, POV ausente.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple

from .lector import RE_SEPARADOR
from .modelo import Capitulo

ANDAMIAJE = [
    (re.compile(r"\[(?:INVENTADO|FALTA|PENDIENTE|NOTA|TBD|TK)[^\]]*\]", re.I), "marca del modelo"),
    (re.compile(r"\b(?:CP|WT|EJ|SES)-\d{1,4}\b"), "clave de inventario"),
    # Decisiones y ventanas del modelo (A92, A110, DR-10, RL-LIC-03). No «A-6»: es una autovía.
    (re.compile(r"\b(?:A\d{2,3}|DR-\d{1,3}|RL-[A-Z]*-?\d{1,3})\b"), "clave del modelo"),
    (re.compile(r"§\s?\d+"), "referencia a sección de la biblia"),
    (re.compile(r"<!--|-->"), "comentario HTML"),
    (re.compile(r"\{\{|\}\}"), "variable sin sustituir"),
    (re.compile(r"\b(?:TODO|FIXME|XXX)\b"), "nota de trabajo"),
    (re.compile(r"\b(?:FRICCIONES DETECTADAS|biblia\.md|next\.md|faltas\.md)\b"), "referencia al catálogo"),
]

TIPOGRAFIA = [
    (re.compile(r'"'), "comillas rectas \" (en castellano: « » o “ ”)"),
    (re.compile(r"(?<![-—])--(?!-)"), "doble guion -- en lugar de raya —"),
    (re.compile(r"^\s*[-–]\s?\S", re.M), "diálogo con guion o semirraya en lugar de raya —"),
    (re.compile(r"\.\.\.(?!\.)"), "tres puntos ... (mejor el carácter …)"),
    (re.compile(r"\S  +\S"), "espacios dobles"),
    (re.compile(r"\s[,.;:!?)»]"), "espacio antes de signo de puntuación"),
    (re.compile(r"\t"), "tabulador"),
]


def revisar(capitulos: List[Capitulo], carpeta: Path,
            por_orden: bool = False) -> Tuple[List[str], List[str]]:
    errores: List[str] = []
    avisos: List[str] = []

    if not capitulos:
        errores.append(f"no hay capítulos en {carpeta} (capitulo_NN.md, o la lista «orden:» de la ficha)")
        return errores, avisos

    numeros = [c.numero for c in capitulos if c.titulo is None]
    esperados = list(range(1, len(numeros) + 1))
    if numeros != esperados:
        avisos.append(f"numeración de capítulos no consecutiva desde 1: {numeros}")
    if len(set(numeros)) != len(numeros):
        errores.append("hay números de capítulo repetidos")

    for c in capitulos:
        for a in c.avisos:
            avisos.append(f"{c.origen}: {a}")
        if c.pov is None:
            avisos.append(f"{c.origen}: sin punto de vista («### NOMBRE»)")
        if c.titulo and capitulos.index(c) not in (0, len(capitulos) - 1) and c.titulo.lower() != "interludio":
            avisos.append(f"{c.origen}: «{c.titulo}» en medio del libro")
        crudo = (carpeta / c.origen).read_text(encoding="utf-8-sig")
        for n, linea in enumerate(crudo.splitlines(), start=1):
            if linea.lstrip().startswith("#") or RE_SEPARADOR.match(linea):
                continue
            for patron, que in ANDAMIAJE:
                m = patron.search(linea)
                if m:
                    errores.append(f"{c.origen}:{n}: {que}: «{m.group(0)}»")
            for patron, que in TIPOGRAFIA:
                cuenta = len(patron.findall(linea))
                if cuenta:
                    avisos.append(f"{c.origen}:{n}: {que}" + (f" (×{cuenta})" if cuenta > 1 else ""))
    return errores, avisos
