"""Lee los capítulos que produce el modelo y los convierte en bloques.

Formato esperado:

    # TÍTULO DEL LIBRO              <- cabecera repetida: se ignora
    ## Serie — Libro 1
    ---
    ## 7                            <- número de capítulo (o «## Prólogo», «## Epílogo»)
    ### ELLA                        <- punto de vista (opcional)

    Texto...

    ---                             <- cambio de escena
    ### ÉL                          <- cambio de narrador a mitad de capítulo (opcional)

Qué archivos y en qué orden: la lista «orden:» de la ficha del libro (ver
archivos_en_orden). Sin ella, los capitulo_NN.md por su número.

Solo se admite la sintaxis que usa la prosa: párrafos, *cursiva*, **negrita**,
saltos de escena y saltos de línea forzados. Cualquier otra cosa se avisa.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

from .modelo import CambioPov, Capitulo, Parrafo, Separador, Tramo

RE_NUMERO = re.compile(r"^#{1,3}\s+(?:cap[ií]tulo\s+)?(\d+)\s*$", re.IGNORECASE)
RE_TITULO = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
RE_SEPARADOR = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,}|(?:\*\s*){3,}|⁂|#)\s*$")
RE_ARCHIVO = re.compile(r"cap[ií]tulo_?(\d+)\.md$", re.IGNORECASE)
RE_ESPECIAL = re.compile(r"^#{1,3}\s+(pr[oó]logo|ep[ií]logo|interludio)\s*$", re.IGNORECASE)
RE_POV_DENTRO = re.compile(r"^###\s+(\S.*?)\s*#*\s*$")
# Archivos que parecen texto de libro (para avisar de los que se quedan fuera del orden).
RE_PARECE_TEXTO = re.compile(r"(cap[ií]tulo|pr[oó]logo|ep[ií]logo|interludio)", re.IGNORECASE)
RE_NO_ES_TEXTO = re.compile(r"(brief|acta|lectura|pasada|ficha|nota|resumen)", re.IGNORECASE)
RE_SINTAXIS_RARA = re.compile(r"^\s*(?:[-+]\s|\d+\.\s|>|\||```|<)")


def archivos_de_capitulo(carpeta: Path) -> List[Path]:
    """Sin lista de orden: los capitulo_NN.md, por su número."""
    encontrados = []
    for p in carpeta.iterdir():
        m = RE_ARCHIVO.search(p.name)
        if p.is_file() and m:
            encontrados.append((int(m.group(1)), p))
    encontrados.sort()
    return [p for _, p in encontrados]


def _primer_numero(nombre: str) -> Tuple[int, str]:
    m = re.search(r"\d+", nombre)
    return (int(m.group(0)) if m else 0, nombre)


def archivos_en_orden(carpeta: Path, orden: Sequence[str]) -> Tuple[List[Path], List[str]]:
    """Resuelve la lista «orden:» de la ficha: nombres de archivo en orden de publicación.

    Una entrada con comodines («C*_capitulo.md») trae todos los que encajen, ordenados por el
    primer número de su nombre, salvo los que ya estén en la lista. Devuelve los archivos y
    los errores (entradas que no existen).
    """
    rutas: List[Path] = []
    errores: List[str] = []
    explicitos = {e for e in orden if not any(c in e for c in "*?[")}
    for entrada in orden:
        if any(c in entrada for c in "*?["):
            encontrados = sorted((p for p in carpeta.glob(entrada)
                                  if p.is_file() and p.name not in explicitos),
                                 key=lambda p: _primer_numero(p.name))
            if not encontrados:
                errores.append(f"«{entrada}» no encaja con ningún archivo de {carpeta}")
            rutas.extend(p for p in encontrados if p not in rutas)
        else:
            p = carpeta / entrada
            if not p.is_file():
                errores.append(f"no existe {entrada} en {carpeta}")
            elif p in rutas:
                errores.append(f"{entrada} aparece dos veces en «orden:»")
            else:
                rutas.append(p)
    return rutas, errores


def fuera_del_orden(carpeta: Path, usados: Sequence[Path]) -> List[str]:
    """Archivos de la carpeta que parecen texto del libro y no están en el orden."""
    usados_n = {p.name for p in usados}
    return sorted(p.name for p in carpeta.glob("*.md")
                  if p.name not in usados_n and RE_PARECE_TEXTO.search(p.name)
                  and not RE_NO_ES_TEXTO.search(p.name))


def leer_capitulo(ruta: Path, por_orden: bool = False) -> Capitulo:
    """Lee un capítulo. Con por_orden, el número publicado lo pone quien llama (por posición)
    y el número del encabezado solo se guarda como numero_archivo."""
    texto = ruta.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    lineas = texto.split("\n")
    avisos: List[str] = []

    # 1. Localizar el encabezado del capítulo («## 7» o «## Prólogo»); lo anterior es
    #    cabecera repetida.
    inicio = None
    numero: Optional[int] = None
    titulo: Optional[str] = None
    for i, linea in enumerate(lineas):
        m = RE_NUMERO.match(linea)
        if m:
            inicio, numero = i, int(m.group(1))
            break
        m = RE_ESPECIAL.match(linea)
        if m:
            inicio, titulo = i, m.group(1).strip().capitalize()
            break
    numero_archivo = numero
    if inicio is None:
        m = RE_ARCHIVO.search(ruta.name)
        numero = int(m.group(1)) if m else 0
        inicio = -1
        avisos.append("no hay encabezado «## N» ni «## Prólogo»; se toma el principio del archivo")
    elif not por_orden and numero is not None:
        m = RE_ARCHIVO.search(ruta.name)
        if m and int(m.group(1)) != numero:
            avisos.append(f"el encabezado dice {numero} pero el archivo es {m.group(1)}")
    if titulo:
        numero = None

    cuerpo = lineas[inicio + 1:]

    # 2. Punto de vista: primer encabezado no vacío tras el número.
    pov = None
    while cuerpo and not cuerpo[0].strip():
        cuerpo.pop(0)
    if cuerpo:
        m = RE_TITULO.match(cuerpo[0])
        if m and not RE_SEPARADOR.match(cuerpo[0]):
            pov = m.group(1).strip()
            cuerpo.pop(0)

    # 3. Bloques.
    bloques = []
    actual: List[str] = []

    def cerrar():
        if actual:
            bloques.append(_parrafo(actual, avisos))
            actual.clear()

    for n, linea in enumerate(cuerpo, start=inicio + 2):
        if not linea.strip():
            cerrar()
        elif RE_SEPARADOR.match(linea):
            cerrar()
            bloques.append(Separador())
        elif RE_POV_DENTRO.match(linea):
            cerrar()
            bloques.append(CambioPov(RE_POV_DENTRO.match(linea).group(1).strip()))
        elif linea.lstrip().startswith("#"):
            cerrar()
            avisos.append(f"línea {n}: encabezado dentro del capítulo, se ignora: {linea.strip()[:60]}")
        else:
            if RE_SINTAXIS_RARA.match(linea) and not actual:
                avisos.append(f"línea {n}: sintaxis no prevista (lista, cita, tabla…), se trata como texto")
            actual.append(linea)
    cerrar()

    # Limpiar separadores al principio, al final o repetidos.
    limpios = []
    for b in bloques:
        if isinstance(b, Separador) and (not limpios or isinstance(limpios[-1], Separador)):
            continue
        limpios.append(b)
    while limpios and isinstance(limpios[-1], Separador):
        limpios.pop()

    palabras = sum(len(t.texto.split()) for b in limpios if isinstance(b, Parrafo) for t in b.tramos)
    return Capitulo(numero=numero, pov=pov, bloques=limpios, origen=ruta.name,
                    palabras=palabras, avisos=avisos, titulo=titulo,
                    numero_archivo=numero_archivo)


def _parrafo(lineas: List[str], avisos: List[str]) -> Parrafo:
    """Une las líneas de un párrafo y resuelve el formato en línea."""
    tramos: List[Tramo] = []
    cursiva = negrita = False
    buf: List[str] = []

    def volcar():
        if buf:
            tramos.append(Tramo("".join(buf), cursiva, negrita))
            buf.clear()

    for k, linea in enumerate(lineas):
        ultima = k == len(lineas) - 1
        salto = not ultima and (linea.endswith("  ") or linea.endswith("\\"))
        linea = linea.rstrip()
        if linea.endswith("\\") and salto:
            linea = linea[:-1]
        linea = linea.strip()
        i = 0
        while i < len(linea):
            c = linea[i]
            if c == "\\" and i + 1 < len(linea):
                buf.append(linea[i + 1])
                i += 2
                continue
            if linea.startswith("**", i) or linea.startswith("__", i):
                volcar()
                negrita = not negrita
                i += 2
                continue
            if c == "*" or (c == "_" and _guion_bajo_es_marca(linea, i)):
                volcar()
                cursiva = not cursiva
                i += 1
                continue
            buf.append(c)
            i += 1
        if not ultima:
            if salto:
                volcar()
                tramos.append(Tramo("", salto=True))
            else:
                buf.append(" ")
    volcar()
    if cursiva or negrita:
        inicio = "".join(t.texto for t in tramos)[:50]
        avisos.append(f"cursiva o negrita sin cerrar en el párrafo «{inicio}…»")
    # Fusionar tramos contiguos del mismo estilo
    fusion: List[Tramo] = []
    for t in tramos:
        if fusion and not t.salto and not fusion[-1].salto and \
                (t.cursiva, t.negrita) == (fusion[-1].cursiva, fusion[-1].negrita):
            fusion[-1].texto += t.texto
        elif t.texto or t.salto:
            fusion.append(t)
    return Parrafo(fusion)


def _guion_bajo_es_marca(linea: str, i: int) -> bool:
    antes = linea[i - 1] if i > 0 else " "
    despues = linea[i + 1] if i + 1 < len(linea) else " "
    return not (antes.isalnum() and despues.isalnum())
