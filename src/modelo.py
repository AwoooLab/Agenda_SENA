"""Modelo de una cita o tarea de la agenda."""

from dataclasses import asdict, dataclass


@dataclass
class Cita:
    titulo: str
    fecha: str
    hora: str
    descripcion: str = ""

    def a_diccionario(self) -> dict:
        """Convierte la cita a un formato que se puede guardar en JSON."""

        return asdict(self)

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Cita":
        """Reconstruye una cita desde un diccionario."""

        return cls(
            titulo=datos["titulo"],
            fecha=datos["fecha"],
            hora=datos["hora"],
            descripcion=datos.get("descripcion", ""),
        )
