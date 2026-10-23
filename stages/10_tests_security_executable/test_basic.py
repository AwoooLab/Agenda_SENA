"""Comprobación mínima de la estructura del proyecto."""

from pathlib import Path


raiz = Path(__file__).resolve().parents[2]
assert (raiz / "app.py").exists()
assert (raiz / "data" / "agenda.json").exists()
print("Estructura básica aprobada.")
