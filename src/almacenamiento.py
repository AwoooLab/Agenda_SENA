"""Lectura y escritura de la agenda en un archivo JSON local."""

import json
from pathlib import Path

from config.config import DATA_FILE
from src.modelo import Cita


def cargar_agenda(ruta: Path = DATA_FILE) -> list[Cita]:
    """Carga las citas guardadas o devuelve una lista vacía."""

    if not ruta.exists():
        return []
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return [Cita.desde_diccionario(item) for item in datos]


def guardar_agenda(citas: list[Cita], ruta: Path = DATA_FILE) -> None:
    """Guarda las citas en JSON con formato legible."""

    ruta.parent.mkdir(parents=True, exist_ok=True)
    datos = [cita.a_diccionario() for cita in citas]
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
