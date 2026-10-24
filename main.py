"""Punto de entrada de la aplicación integrada Agenda SENA.

El estudiante trabaja en stages/. La integración aprobada se conecta en src/
sin importar automáticamente los ejercicios de las etapas.
"""

from src.app_shell import AppShell


def main() -> None:
    """Construye y ejecuta una única ventana de Agenda SENA."""

    AppShell().run()


if __name__ == "__main__":
    main()
