"""Especificaciones de impresión de KDP (tapa blanda, sin sangrado en el interior).

Fuente: guía de formato de manuscrito y calculadora de cubierta de KDP.
Revisar si Amazon cambia los valores.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

# Formatos de corte habituales en ficción (pulgadas, ancho x alto)
FORMATOS = {
    "5x8": (5.0, 8.0),
    "5.06x7.81": (5.06, 7.81),
    "5.25x8": (5.25, 8.0),
    "5.5x8.5": (5.5, 8.5),
    "6x9": (6.0, 9.0),
}

# Grosor por página (pulgadas)
GROSOR_PAPEL = {
    "blanco": 0.002252,
    "crema": 0.0025,
}

# Medianil mínimo según número de páginas
MEDIANIL = [
    (24, 150, 0.375),
    (151, 300, 0.5),
    (301, 500, 0.625),
    (501, 700, 0.75),
    (701, 828, 0.875),
]

MARGEN_EXTERIOR_MIN = 0.25
SANGRADO_CUBIERTA = 0.125
PAGINAS_MIN = 24
PAGINAS_MAX = 828
PAGINAS_MIN_TEXTO_LOMO = 80  # por debajo de 80 páginas KDP no permite texto en el lomo

MM = 25.4


def medianil_minimo(paginas: int) -> float:
    for desde, hasta, valor in MEDIANIL:
        if paginas <= hasta:
            return valor
    return MEDIANIL[-1][2]


@dataclass
class Cubierta:
    paginas: int
    lomo: float
    ancho: float
    alto: float
    texto_en_lomo: bool

    def px(self, dpi: int = 300) -> Tuple[int, int]:
        return round(self.ancho * dpi), round(self.alto * dpi)


def cubierta(formato: str, papel: str, paginas: int) -> Cubierta:
    ancho, alto = FORMATOS[formato]
    lomo = paginas * GROSOR_PAPEL[papel]
    return Cubierta(
        paginas=paginas,
        lomo=lomo,
        ancho=SANGRADO_CUBIERTA + ancho + lomo + ancho + SANGRADO_CUBIERTA,
        alto=SANGRADO_CUBIERTA + alto + SANGRADO_CUBIERTA,
        texto_en_lomo=paginas >= PAGINAS_MIN_TEXTO_LOMO,
    )
