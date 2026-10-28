"""Monta la fábrica plana que leen las ventanas a partir de sus capas.

    python herramientas/montar.py --genero dark_romance --destino <carpeta>

Cada archivo de salida se compone, en este orden, con los trozos que existan con su nombre:

    fabrica/metodo/       fabrica/oficio/       fabrica/romance/
    fabrica/generos/<genero>/plantillas/        fabrica/generos/<genero>/adendas/

Lo que es común a todo romance va arriba; lo de cada subgénero, en su paquete. Un paquete
nuevo (romantasy, dark academia…) es una carpeta más en fabrica/generos/, con sus plantillas
y sus adendas, sin tocar las capas de arriba.

Con --comprobar <carpeta>, en vez de escribir, compara byte a byte el montaje con los archivos
de esa carpeta y dice si son idénticos.
"""
import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / "fabrica"
CAPAS = ["metodo", "oficio", "romance"]


def montar(genero: str) -> dict:
    paquete = RAIZ / "generos" / genero
    if not paquete.is_dir():
        disponibles = ", ".join(p.name for p in (RAIZ / "generos").iterdir() if p.is_dir())
        sys.exit(f"No existe el género «{genero}». Hay: {disponibles}")
    carpetas = [RAIZ / c for c in CAPAS] + [paquete / "plantillas", paquete / "adendas"]
    nombres = sorted({p.name for c in carpetas if c.is_dir() for p in c.glob("*.md")})
    salida = {}
    for n in nombres:
        trozos = [c / n for c in carpetas if (c / n).is_file()]
        # Una adenda sin base no tiene a qué pegarse.
        if all(t.parent.name == "adendas" for t in trozos):
            sys.exit(f"{n}: hay adenda pero no base en ninguna capa")
        salida[n] = b"".join(t.read_bytes() for t in trozos)
    return salida


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--genero", default="dark_romance")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--destino", type=Path, help="carpeta donde escribir la fábrica plana")
    g.add_argument("--comprobar", type=Path, help="carpeta con la que comparar byte a byte")
    a = ap.parse_args()
    archivos = montar(a.genero)

    if a.destino:
        a.destino.mkdir(parents=True, exist_ok=True)
        for n, datos in archivos.items():
            (a.destino / n).write_bytes(datos)
        print(f"{len(archivos)} archivos montados en {a.destino}")
        return

    distintos = [n for n, d in archivos.items()
                 if not (a.comprobar / n).is_file() or (a.comprobar / n).read_bytes() != d]
    if distintos:
        print(f"DISTINTOS ({len(distintos)}): " + ", ".join(distintos))
        sys.exit(1)
    print(f"Idénticos: los {len(archivos)} archivos montados coinciden byte a byte con {a.comprobar}")


if __name__ == "__main__":
    main()
