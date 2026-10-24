"""Vista inicial de la aplicación integrada."""

import tkinter as tk

from src.state import AppState


def build(parent: tk.Frame, state: AppState) -> tk.Frame:
    """Construye la vista inicial dentro del área central."""

    frame = tk.Frame(parent, bg="#ffffff", padx=32, pady=32)
    tk.Label(
        frame,
        text="Agenda SENA",
        bg="#ffffff",
        fg="#172554",
        font=("Arial", 22, "bold"),
    ).pack(pady=(28, 8))
    tk.Label(
        frame,
        text="Mi agenda local para PC",
        bg="#ffffff",
        fg="#64748b",
        font=("Arial", 12),
    ).pack()
    return frame
