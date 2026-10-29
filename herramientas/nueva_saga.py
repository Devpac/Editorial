"""Prepara el repo de una saga nueva con la fábrica.

    python herramientas/nueva_saga.py --genero dark_romance --obra NOMBRE_DE_TRABAJO --destino <repo>

Deja en <repo> (que tiene que estar vacío, salvo .git, README, LICENSE o .gitignore):

    LEEME.md            el de la obra: qué es fábrica y qué es obra, y por dónde empezar
    .gitignore
    fabrica/            la fábrica montada para el género, con su sello (_FABRICA.txt)
    publicacion/        serie.yaml y libro_01.yaml para el maquetador, y portadas/ con la
                        plantilla de instrucciones para el generador de imágenes

No crea el cuaderno, la biblia ni el preset: los hace el orquestador en las fases 0, 1 y 1b
(`fabrica/ORQUESTADOR.md`), con sus plantillas. Ver ARRANQUE.md.
"""
import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from montar import escribir, montar, version  # noqa: E402

EDITORIAL = Path(__file__).resolve().parent.parent
PLANTILLA = EDITORIAL / "plantilla_saga"
PORTADAS = EDITORIAL / "maquetador" / "portadas" / "INSTRUCCIONES_GPT_plantilla.md"
PERMITIDOS = {".git", "README.md", "LICENSE", ".gitignore", ".gitattributes"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--genero", required=True, help="paquete de fabrica/generos/ (p. ej. dark_romance)")
    ap.add_argument("--obra", required=True, help="nombre de trabajo en MAYÚSCULAS_CON_GUIONES_BAJOS")
    ap.add_argument("--titulo", help="título de trabajo para el LEEME (por defecto, el nombre de trabajo)")
    ap.add_argument("--destino", required=True, type=Path, help="carpeta del repo de la saga")
    a = ap.parse_args()

    if not re.fullmatch(r"[A-ZÁÉÍÓÚÑÜ0-9]+(_[A-ZÁÉÍÓÚÑÜ0-9]+)*", a.obra):
        sys.exit("--obra va en mayúsculas y con guiones bajos (p. ej. CORONA_DE_CENIZA): es el que "
                 "llevan los nombres de archivo (CUADERNO_<OBRA>.md, PRESET_<OBRA>.md).")
    archivos = montar(a.genero)  # sale con error si el género no existe
    destino = a.destino.resolve()
    destino.mkdir(parents=True, exist_ok=True)
    ocupado = sorted(p.name for p in destino.iterdir() if p.name not in PERMITIDOS)
    if ocupado:
        sys.exit(f"{destino} no está vacío ({', '.join(ocupado)}). Una saga nueva empieza en un repo vacío.")
    valores = {
        "{{OBRA}}": a.obra,
        "{{TITULO}}": a.titulo or a.obra.replace("_", " ").capitalize(),
        "{{GENERO}}": a.genero,
        "{{VERSION}}": version(),
        "{{FECHA}}": dt.date.today().strftime("%d-%m-%Y"),
    }
    for origen in sorted(PLANTILLA.rglob("*")):
        if origen.is_dir():
            continue
        rel = origen.relative_to(PLANTILLA)
        final = destino / rel
        final.parent.mkdir(parents=True, exist_ok=True)
        if rel.name == ".gitignore" and final.exists():
            final.write_text(final.read_text(encoding="utf-8").rstrip("\n") + "\n"
                             + origen.read_text(encoding="utf-8"), encoding="utf-8")
            continue
        texto = origen.read_text(encoding="utf-8")
        for k, v in valores.items():
            texto = texto.replace(k, v)
        final.write_text(texto, encoding="utf-8")
    portadas = destino / "publicacion" / "portadas"
    portadas.mkdir(parents=True, exist_ok=True)
    shutil.copy(PORTADAS, portadas / "INSTRUCCIONES_GPT.md")

    escribir(destino / "fabrica", a.genero, archivos)
    print(f"Saga {a.obra} preparada en {destino} (Fábrica v{version()}, {a.genero}).")
    print("Siguiente: commit «Fase 0: saga montada con la Fábrica» y la fase 0 "
          "(fabrica/ORQUESTADOR.md §2.0).")


if __name__ == "__main__":
    main()
