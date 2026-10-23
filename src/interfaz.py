"""Interfaz gráfica inicial de Agenda SENA usando Tkinter."""

import tkinter as tk

from config.config import APP_TITLE


def ejecutar() -> None:
    """Abre la ventana inicial de la aplicación."""

    ventana = tk.Tk()
    ventana.title(APP_TITLE)
    ventana.geometry("520x320")
    tk.Label(ventana, text=APP_TITLE, font=("Arial", 22, "bold")).pack(pady=(65, 15))
    tk.Label(
        ventana,
        text="La agenda se construirá paso a paso.",
        font=("Arial", 12),
    ).pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=20)
    ventana.mainloop()
