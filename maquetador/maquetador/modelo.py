"""Estructuras de datos compartidas por el lector y los generadores."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Tramo:
    """Trozo de texto con un mismo estilo dentro de un párrafo."""
    texto: str
    cursiva: bool = False
    negrita: bool = False
    salto: bool = False  # salto de línea forzado (dos espacios o «\» al final de línea)


@dataclass
class Parrafo:
    tramos: List[Tramo]


@dataclass
class Separador:
    """Cambio de escena."""


@dataclass
class CambioPov:
    """Rótulo de narrador a mitad de capítulo («### ÉL» tras un cambio de escena)."""
    pov: str


Bloque = Union[Parrafo, Separador, CambioPov]


@dataclass
class Capitulo:
    numero: Optional[int]          # número publicado; None en prólogo, epílogo…
    pov: Optional[str]
    bloques: List[Bloque]
    origen: str
    palabras: int = 0
    avisos: List[str] = field(default_factory=list)
    titulo: Optional[str] = None   # «Prólogo», «Epílogo»… (sin número)
    numero_archivo: Optional[int] = None  # el número que trae el encabezado del archivo

    @property
    def rotulo(self) -> str:
        """Cómo se nombra en índices y fichas: «Prólogo» o «Capítulo 7»."""
        return self.titulo or f"Capítulo {self.numero}"
