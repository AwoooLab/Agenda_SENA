"""Ejemplo aislado de la primera etapa."""

import tkinter as tk


ventana = tk.Tk()
ventana.title("Agenda SENA — Etapa 01")
ventana.geometry("420x240")
tk.Label(ventana, text="Agenda SENA", font=("Arial", 22, "bold")).pack(pady=65)
tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack()
ventana.mainloop()
