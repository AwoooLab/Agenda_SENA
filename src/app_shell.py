"""Carcasa de integración de Agenda SENA para una sola ventana."""

import tkinter as tk

from src.router import Router
from src.state import AppState
from src.views.home_view import build as build_home


class AppShell:
    """Ventana principal y punto de conexión de los módulos aprobados."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Agenda SENA")
        self.root.geometry("900x600")
        self.root.minsize(720, 480)

        self.state = AppState()
        self.content = tk.Frame(self.root, bg="#f8fafc")
        self.content.pack(fill="both", expand=True)

        self.router = Router(self.content)
        self.router.register("inicio", lambda parent: build_home(parent, self.state))
        self.router.show("inicio")

    def run(self) -> None:
        """Inicia el bucle de la única ventana de la aplicación."""

        self.root.mainloop()
