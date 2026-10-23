"""Demostración aislada del guardado JSON."""

import tempfile
from pathlib import Path

from storage import cargar, guardar


with tempfile.TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "agenda.json"
    guardar([{"titulo": "Clase", "fecha": "2026-10-23", "hora": "18:00"}], ruta)
    print(cargar(ruta))
