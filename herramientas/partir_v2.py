"""Parte los archivos de modelo de Dark (MODELO_DarkRomance v2.0) en las capas de Editorial.

Uso (una sola vez, queda como traza):  python -I herramientas/partir_v2.py <ruta_a_Dark> <ruta_a_Editorial>

No cambia ni un byte: cada archivo se copia entero a su capa o se corta por la línea donde
empieza su adenda de dark romance. montar.py vuelve a unirlos.
"""
import re
import sys
from pathlib import Path

METODO = ["LEEME.md", "ORQUESTADOR.md", "PROTOCOLO_LECTURA.md", "PLANTILLA_NEXT.md",
          "PLANTILLA_CUADERNO.md", "PLANTILLA_BIBLIA.md", "PLANTILLA_PRESET.md",
          "PLANTILLA_ESCALETA.md", "PLANTILLA_LIBRO.md", "PROTOCOLO_CAPTURA_APRENDIZAJE.md",
          "REGISTROS_APRENDIZAJE.md", "SYSTEM_ORCHESTRATION.md"]
ROMANCE = ["PAREJA_PRIMERO.md"]
GENERO = ["GENRE_CONVENTIONS.md", "HEAT_DISCIPLINE.md", "ROMANCE_BEAT_MAP.md",
          "CHARACTER_PHYSICS.md", "DIALOGUE_MECHANICS.md", "AESTHETIC_REGISTER.md",
          "ELLIPSIS_PROTOCOL.md", "CLUE_LEDGER.md", "BRIEFING.md", "SERIES_GLUE.md"]
OFICIO = ["CHAPTER_BRIEF.md", "CONTINUITY_PHYSICS.md", "PROSE_LINE_DISCIPLINE.md",
          "RELATIONSHIP_PHYSICS.md", "SCALE_CALIBRATION.md", "SEAMS_AND_HINGES.md",
          "TENSION_MECHANICS.md", "VOICE_ARCHITECTURE.md", "SERIES_ARCHITECTURE.md",
          "INFORMATION_CHOREOGRAPHY.md", "NARRATIVE_CHRONOLOGY.md", "PROSODY_AND_MUSIC.md",
          "REVISION_PROTOCOL.md", "SCENE_NECESSITY.md", "SEMANTIC_OMISSION.md",
          "SENSORY_HIERARCHY.md", "STORY_SPINE.md", "SUBPLOT_ARCHITECTURE.md",
          "SUBTEXT_MECHANICS.md", "THEMATIC_ENGINE.md", "WORLD_ARC.md", "WORLD_TEXTURE.md",
          "RESEARCH_LEDGER.md", "SCENE_SHAPE.md"]
COSTURA = re.compile(rb"^(#{1,2} .*ADENDA DE ESPECIALIZACI|# SYSTEM_ORCHESTRATION\.adenda)", re.M)


def partir(origen: Path, base: Path, adenda: Path) -> bool:
    datos = origen.read_bytes()
    m = COSTURA.search(datos)
    if not m:
        base.write_bytes(datos)
        return False
    base.write_bytes(datos[:m.start()])
    adenda.write_bytes(datos[m.start():])
    return True


def main(dark: Path, ed: Path) -> None:
    fab = ed / "fabrica"
    g = fab / "generos" / "dark_romance"
    for d in (fab / "metodo", fab / "oficio", fab / "romance", g / "plantillas", g / "adendas"):
        d.mkdir(parents=True, exist_ok=True)
    for n in METODO:
        partir(dark / n, fab / "metodo" / n, g / "adendas" / n)
    for n in ROMANCE:
        (fab / "romance" / n).write_bytes((dark / n).read_bytes())
    for n in GENERO:
        (g / "plantillas" / n).write_bytes((dark / n).read_bytes())
    for n in OFICIO:
        partir(dark / n, fab / "oficio" / n, g / "adendas" / n)
    total = len(METODO) + len(ROMANCE) + len(GENERO) + len(OFICIO)
    print(f"{total} archivos repartidos")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
