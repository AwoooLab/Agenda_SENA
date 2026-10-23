"""Ventana inicial de Agenda SENA para la etapa 01."""

import tkinter as tk


def main() -> None:
    """Construye y muestra la ventana inicial de la agenda."""

    ventana = tk.Tk()
    ventana.title("Agenda SENA — Etapa 01")
    ventana.geometry("520x320")
    ventana.resizable(False, False)
    ventana.configure(bg="#ffffff")

    titulo = tk.Label(
        ventana,
        text="Agenda SENA",
        bg="#ffffff",
        font=("Arial", 22, "bold"),
    )
    titulo.pack(pady=(68, 14))

    subtitulo = tk.Label(
        ventana,
        text="Mi agenda local para PC",
        bg="#ffffff",
        font=("Arial", 12),
    )
    subtitulo.pack(pady=8)

    boton_cerrar = tk.Button(
        ventana,
        text="Cerrar",
        command=ventana.destroy,
        font=("Arial", 11),
    )
    boton_cerrar.pack(pady=22)

    ventana.mainloop()


if __name__ == "__main__":
    main()
