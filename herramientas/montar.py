"""Monta la fábrica plana que leen las ventanas a partir de sus capas.

    python herramientas/montar.py --genero dark_romance --destino <carpeta>

Cada archivo de salida se compone, en este orden, con los trozos que existan con su nombre:

    fabrica/metodo/       fabrica/oficio/       fabrica/romance/
    fabrica/generos/<genero>/plantillas/        fabrica/generos/<genero>/adendas/

Lo que es común a todo romance va arriba; lo de cada subgénero, en su paquete. Un paquete
nuevo (romantasy, dark academia…) es una carpeta más en fabrica/generos/, con sus plantillas
y sus adendas, sin tocar las capas de arriba.

Con --destino, además de los archivos, escribe en la carpeta el sello `_FABRICA.txt` (versión,
género, commit de Editorial, fecha y la lista de archivos). Si la carpeta ya tenía un sello, es una
actualización: se borran los archivos de la fábrica anterior que ya no existen y no se toca nada
que no figure en el sello viejo. Así se monta y se pone al día la carpeta `fabrica/` de una saga:

    python herramientas/montar.py --genero dark_romance --destino <repo_de_la_saga>/fabrica

Con --comprobar <carpeta>, en vez de escribir, compara byte a byte el montaje con los archivos
de esa carpeta y dice si son idénticos.
"""
import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

EDITORIAL = Path(__file__).resolve().parent.parent
RAIZ = EDITORIAL / "fabrica"
CAPAS = ["metodo", "oficio", "romance"]
SELLO = "_FABRICA.txt"


def version() -> str:
    v = EDITORIAL / "VERSION"
    return v.read_text(encoding="utf-8").strip() if v.is_file() else "?"


def commit() -> str:
    try:
        r = subprocess.run(["git", "-C", str(EDITORIAL), "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, check=True)
        sucio = subprocess.run(["git", "-C", str(EDITORIAL), "status", "--porcelain", "fabrica"],
                               capture_output=True, text=True).stdout.strip()
        return r.stdout.strip() + (" (con cambios sin subir)" if sucio else "")
    except (OSError, subprocess.CalledProcessError):
        return "desconocido"


def leer_sello(carpeta: Path) -> list:
    """Archivos que la fábrica montada anteriormente dejó en la carpeta."""
    sello = carpeta / SELLO
    if not sello.is_file():
        return []
    lineas = sello.read_text(encoding="utf-8").splitlines()
    return [l[2:].strip() for l in lineas if l.startswith("- ") and l.strip().endswith(".md")]


def escribir(destino: Path, genero: str, archivos: dict) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    viejos = set(leer_sello(destino))
    sueltos = sorted(p.name for p in destino.glob("*.md") if p.name not in viejos and p.name not in archivos)
    if sueltos:
        sys.exit(f"{destino} tiene archivos que no son de la fábrica: {', '.join(sueltos)}. "
                 "La carpeta de la fábrica solo lleva la fábrica (la obra va en la raíz del repo).")
    quitados = sorted(viejos - set(archivos))
    for n in quitados:
        (destino / n).unlink(missing_ok=True)
    for n, datos in archivos.items():
        (destino / n).write_bytes(datos)
    hoy = dt.date.today().isoformat()
    (destino / SELLO).write_text(
        f"Fábrica v{version()} · género: {genero} · Editorial {commit()} · montada el {hoy}\n"
        "No se edita a mano: se monta desde Devpac/Editorial (herramientas/montar.py).\n"
        "Las mejoras se proponen a Editorial (PROTOCOLO_CAPTURA_APRENDIZAJE.md).\n\n"
        + "\n".join(f"- {n}" for n in sorted(archivos)) + "\n", encoding="utf-8")
    print(f"{len(archivos)} archivos montados en {destino} (Fábrica v{version()}, {genero})"
          + (f"; retirados: {', '.join(quitados)}" if quitados else ""))


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
        escribir(a.destino, a.genero, archivos)
        return

    distintos = [n for n, d in archivos.items()
                 if not (a.comprobar / n).is_file() or (a.comprobar / n).read_bytes() != d]
    if distintos:
        print(f"DISTINTOS ({len(distintos)}): " + ", ".join(distintos))
        sys.exit(1)
    print(f"Idénticos: los {len(archivos)} archivos montados coinciden byte a byte con {a.comprobar}")


if __name__ == "__main__":
    main()
