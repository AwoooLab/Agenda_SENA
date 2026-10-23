"""Validaciones de los datos ingresados a la agenda."""

from datetime import datetime

from config.config import DATE_FORMAT, TIME_FORMAT
from src.modelo import Cita


def validar_cita(cita: Cita) -> list[str]:
    """Devuelve errores; una lista vacía significa que la cita es válida."""

    errores = []
    if not cita.titulo.strip():
        errores.append("El título es obligatorio.")
    try:
        datetime.strptime(cita.fecha, DATE_FORMAT)
    except ValueError:
        errores.append("La fecha debe tener el formato AAAA-MM-DD.")
    try:
        datetime.strptime(cita.hora, TIME_FORMAT)
    except ValueError:
        errores.append("La hora debe tener el formato HH:MM.")
    return errores
