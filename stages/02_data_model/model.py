"""Ejemplo aislado del modelo de datos."""

from dataclasses import asdict, dataclass


@dataclass
class Cita:
    titulo: str
    fecha: str
    hora: str
    descripcion: str = ""


if __name__ == "__main__":
    print(asdict(Cita("Clase", "2026-10-23", "18:00")))
