"""Regenera las ranuras por plantilla de fabrica/metodo/PLANTILLA_PRESET.md a partir de las plantillas.

    python herramientas/sincronizar_preset.py [--genero dark_romance] [--comprobar]

Cada plantilla declara sus ranuras con un bloque:

    > **Valores de la obra →** `PRESET_<OBRA>.md` › <PLANTILLA> › <Ranura>.
    > *Qué declara aquí la obra:* <texto>

PLANTILLA_PRESET.md copia esos bloques, una viñeta por ranura, en las secciones que siguen a
«## Las demás plantillas». Este script las reescribe en el orden en que aparecen en cada
plantilla montada, para que el preset y las plantillas no puedan desalinearse. Lo que hay antes
de «## Las demás plantillas» (reglas, cabecera, SYSTEM_ORCHESTRATION, PROTOCOLO_LECTURA) no lo toca.

Con --comprobar no escribe: dice qué cambiaría y sale con error si algo difiere.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from montar import montar  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent / "fabrica"
PRESET = RAIZ / "metodo" / "PLANTILLA_PRESET.md"
MARCA = "## Las demás plantillas"
RE_PUNTERO = re.compile(r"^>\s*\*\*Valores de la obra →\*\*\s*`PRESET_<OBRA>\.md` › (\w+) › (.+?)\.?\s*$")
RE_QUE = re.compile(r"^>\s*\*Qué declara aquí la obra:\*\s*(.*)$")


def ranuras(archivos: dict) -> dict:
    """{PLANTILLA: [(ranura, qué declara), ...]} en orden de aparición."""
    salida: dict = {}
    for nombre, datos in archivos.items():
        lineas = datos.decode("utf-8").split("\n")
        for i, linea in enumerate(lineas):
            m = RE_PUNTERO.match(linea)
            if not m:
                continue
            plantilla, ranura = m.group(1), m.group(2).strip()
            texto = ""
            j = i + 1
            if j < len(lineas) and RE_QUE.match(lineas[j]):
                partes = [RE_QUE.match(lineas[j]).group(1).strip()]
                j += 1
                while j < len(lineas) and lineas[j].startswith(">") and not RE_PUNTERO.match(lineas[j]) \
                        and lineas[j].strip() != ">":
                    partes.append(lineas[j].lstrip("> ").strip())
                    j += 1
                texto = " ".join(p for p in partes if p)
            if not texto:
                print(f"! {nombre}:{i + 1}: la ranura «{plantilla} › {ranura}» no dice qué declara la obra")
            lista = salida.setdefault(plantilla, [])
            # Una ranura puede citarse varias veces pidiendo partes distintas: una viñeta por cita.
            if (ranura, texto) not in lista:
                lista.append((ranura, texto))
    return salida


def componer(actual: str, por_plantilla: dict) -> str:
    if MARCA not in actual:
        sys.exit(f"No encuentro «{MARCA}» en {PRESET}")
    cabeza, cola = actual.split(MARCA, 1)
    # El párrafo que sigue a la marca se conserva; las secciones «## X» se regeneran.
    m = re.search(r"^## ", cola, re.M)
    intro = cola[:m.start()] if m else cola
    orden_actual = re.findall(r"^## (\w+)\s*$", cola, re.M)
    orden = [p for p in orden_actual if p in por_plantilla] + \
            [p for p in por_plantilla if p not in orden_actual]
    secciones = []
    for p in orden:
        vinetas = []
        for ranura, texto in por_plantilla[p]:
            texto = texto[:1].upper() + texto[1:] if texto else "(la plantilla no lo dice)"
            vinetas.append(f"- **{ranura}.** {texto}")
        secciones.append(f"## {p}\n\n" + "\n".join(vinetas) + "\n")
    return cabeza + MARCA + intro + "\n".join(secciones)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genero", default="dark_romance")
    ap.add_argument("--comprobar", action="store_true")
    a = ap.parse_args()
    archivos = montar(a.genero)
    archivos.pop("PLANTILLA_PRESET.md", None)
    por_plantilla = ranuras(archivos)
    actual = PRESET.read_text(encoding="utf-8")
    # La Cabecera, SYSTEM_ORCHESTRATION y PROTOCOLO_LECTURA viven antes de la marca, escritas a
    # mano. De la Cabecera se comprueba que existe cada ranura citada («### <Ranura>»).
    faltan = []
    for ranura, _ in por_plantilla.pop("Cabecera", []):
        if not re.search(rf"^###\s+{re.escape(ranura)}\s*$", actual, re.M):
            faltan.append(f"Cabecera › {ranura}")
    for propia in ("SYSTEM_ORCHESTRATION", "PROTOCOLO_LECTURA"):
        por_plantilla.pop(propia, None)
    if faltan:
        print("! Ranuras citadas que no existen en la Cabecera de PLANTILLA_PRESET: " + "; ".join(faltan))
    nuevo = componer(actual, por_plantilla)
    total = sum(len(v) for v in por_plantilla.values())
    if a.comprobar:
        if nuevo == actual and not faltan:
            print(f"Al día: {total} ranuras de {len(por_plantilla)} plantillas")
            return
        print("PLANTILLA_PRESET.md no coincide con las plantillas (ejecuta sin --comprobar)")
        sys.exit(1)
    PRESET.write_text(nuevo, encoding="utf-8")
    print(f"PLANTILLA_PRESET.md: {total} ranuras de {len(por_plantilla)} plantillas")


if __name__ == "__main__":
    main()
