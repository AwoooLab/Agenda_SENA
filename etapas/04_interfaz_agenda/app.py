"""Prototipo de formulario para la etapa 04."""

import tkinter as tk
from tkinter import messagebox


def agregar():
    titulo = entrada.get().strip()
    if not titulo:
        messagebox.showerror("Validación", "El título es obligatorio.")
        return
    lista.insert(tk.END, titulo)
    entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Agenda SENA — Etapa 04")
ventana.geometry("520x360")
tk.Label(ventana, text="Título de la cita").pack(pady=(25, 5))
entrada = tk.Entry(ventana, width=45)
entrada.pack()
tk.Button(ventana, text="Agregar cita", command=agregar).pack(pady=15)
lista = tk.Listbox(ventana, width=55, height=10)
lista.pack()
ventana.mainloop()
