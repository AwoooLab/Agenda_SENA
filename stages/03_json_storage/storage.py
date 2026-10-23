"""Ejemplo de persistencia local para la etapa 03."""

import json
from pathlib import Path


def guardar(datos: list[dict], ruta: Path) -> None:
    ruta.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")


def cargar(ruta: Path) -> list[dict]:
    return json.loads(ruta.read_text(encoding="utf-8"))
