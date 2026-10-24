"""Navegación entre vistas dentro de una única ventana Tkinter."""

from collections.abc import Callable
import tkinter as tk


ViewFactory = Callable[[tk.Frame], tk.Widget]


class Router:
    """Registra vistas y muestra una sola en el área central."""

    def __init__(self, container: tk.Frame) -> None:
        self.container = container
        self.routes: dict[str, ViewFactory] = {}

    def register(self, name: str, view_factory: ViewFactory) -> None:
        """Asocia un nombre de navegación con una fábrica de vista."""

        self.routes[name] = view_factory

    def show(self, name: str) -> None:
        """Reemplaza el contenido central sin crear otra ventana."""

        for child in self.container.winfo_children():
            child.destroy()

        view = self.routes[name](self.container)
        view.pack(fill="both", expand=True)
