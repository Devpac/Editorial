#!/usr/bin/env python3
"""Maquetador de la fábrica: de los capítulos de una saga a los archivos de KDP.

    python maquetar.py <saga>/publicacion/libro_01.yaml            # EPUB + interior PDF + cubiertas + ficha
    python maquetar.py <saga>/publicacion/libro_01.yaml --revisar  # solo comprobaciones
    python maquetar.py <saga>/publicacion/libro_01.yaml --solo epub

La configuración de cada libro vive en su saga (publicacion/); el código, aquí. La salida va a
salida/<libro>/ junto a la ficha (publicacion/salida/, que Git ignora), salvo --salida.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from maquetador import config, cubierta, epub, ficha, pdf
from maquetador.lector import (archivos_de_capitulo, archivos_en_orden, fuera_del_orden,
                               leer_capitulo)
from maquetador.revision import revisar

RAIZ = Path(__file__).resolve().parent


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Maqueta un libro de una saga para KDP.")
    ap.add_argument("libro", type=Path, help="ficha del libro, p. ej. ../MiSaga/publicacion/libro_01.yaml")
    ap.add_argument("--revisar", action="store_true", help="solo comprobar, sin generar archivos")
    ap.add_argument("--solo", choices=["epub", "pdf", "cubierta"], help="generar solo una parte")
    ap.add_argument("--forzar", action="store_true", help="generar aunque haya errores de andamiaje")
    ap.add_argument("--salida", type=Path, default=None,
                    help="carpeta de salida (por defecto, salida/ junto a la ficha del libro)")
    args = ap.parse_args()

    cfg = config.cargar(args.libro)
    carpeta = cfg["capitulos"]
    if not carpeta or not carpeta.is_dir():
        print(f"✗ No encuentro la carpeta de capítulos: {carpeta}")
        print("  Revisa «capitulos:» en la ficha del libro (ruta relativa a la ficha).")
        return 2

    orden = cfg.get("orden") or []
    errores_orden: list = []
    if orden:
        rutas, errores_orden = archivos_en_orden(carpeta, orden)
        capitulos = [leer_capitulo(p, por_orden=True) for p in rutas]
        n = 0
        for c in capitulos:  # el número publicado sale de la posición; prólogo y epílogo, sin número
            if c.titulo is None:
                n += 1
                c.numero = n
    else:
        rutas = archivos_de_capitulo(carpeta)
        capitulos = [leer_capitulo(p) for p in rutas]
    errores, avisos = revisar(capitulos, carpeta, por_orden=bool(orden))
    errores = errores_orden + errores
    if orden:
        for nombre in fuera_del_orden(carpeta, rutas):
            avisos.append(f"{nombre}: parece texto del libro y no está en «orden:»")
    palabras = sum(c.palabras for c in capitulos)

    numerados = sum(1 for c in capitulos if c.titulo is None)
    extra = [c.titulo for c in capitulos if c.titulo]
    resumen = f"{numerados} capítulos" + (f" + {', '.join(extra).lower()}" if extra else "")
    print(f"{cfg['titulo']} — {resumen}, {palabras:,} palabras".replace(",", "."))
    for e in errores:
        print(f"  ✗ {e}")
    if avisos:
        print(f"  {len(avisos)} avisos (detalle en la ficha)")
    pend = config.pendientes(cfg)
    if pend:
        print(f"  Pendiente en la ficha: {', '.join(pend)}")

    if args.revisar:
        for a in avisos:
            print(f"  · {a}")
        return 1 if errores else 0

    if errores and not args.forzar:
        print("✗ Hay restos de andamiaje: no se genera nada. Corrígelos o usa --forzar para una prueba.")
        return 1

    destino = (args.salida or cfg["_ruta_yaml"].parent / "salida") / cfg["_id"]
    destino.mkdir(parents=True, exist_ok=True)
    paginas = medianil = None

    if args.solo in (None, "pdf", "cubierta"):
        ruta, paginas, medianil = pdf.generar(cfg, capitulos, destino / f"{cfg['_id']}_interior.pdf")
        if args.solo == "cubierta":
            ruta.unlink()
        else:
            print(f"✓ Interior: {ruta} ({paginas} páginas, medianil {medianil:.3f} in)")

    inf_cub = None
    if args.solo in (None, "cubierta", "epub"):
        inf_cub = cubierta.generar(cfg, destino, paginas)
        for a in inf_cub["archivos"]:
            print(f"✓ Cubierta: {a}")
        for a in inf_cub["avisos"]:
            print(f"  ! {a}")
        generada = destino / "portada_ebook.jpg"
        if not cfg["portada"].get("ebook") and cfg["portada"].get("incluir_en_epub") and generada.exists():
            cfg["portada"]["ebook"] = generada

    if args.solo in (None, "epub"):
        ruta = epub.generar(cfg, capitulos, destino / f"{cfg['_id']}.epub")
        print(f"✓ EPUB: {ruta}")

    texto = ficha.escribir(cfg, capitulos, paginas, medianil, errores, avisos, inf_cub)
    (destino / "ficha_kdp.md").write_text(texto, encoding="utf-8")
    print(f"✓ Ficha: {destino / 'ficha_kdp.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
