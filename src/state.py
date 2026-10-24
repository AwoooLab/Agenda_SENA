"""Estado compartido mínimo de la aplicación integrada."""

from dataclasses import dataclass


@dataclass
class AppState:
    """Datos que pueden compartir las vistas integradas."""

    current_user: str | None = None
