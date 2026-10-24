"""Base visual de Agenda SENA para la etapa 01.

La etapa usa una sola ventana de Tkinter. Primero muestra una bienvenida con un
botón ``Siguiente`` y después reemplaza su contenido por la agenda. Todavía no
hay usuarios, contraseñas, archivos ni base de datos.
"""

import tkinter as tk


NAVY = "#111d4a"
BLUE = "#2563eb"
LIGHT_BLUE = "#e8f0ff"
PAGE = "#eef2f7"
CONTENT = "#f7f9fc"
WHITE = "#ffffff"
MUTED = "#64748b"
LINE = "#e2e8f0"
GREEN = "#16a34a"
ORANGE = "#f97316"
PURPLE = "#7c3aed"


def clear_window(window: tk.Tk) -> None:
    """Elimina la vista actual sin crear otra ventana."""

    for child in window.winfo_children():
        child.destroy()


def build_login(window: tk.Tk, go_to_agenda) -> None:
    """Construye la bienvenida inicial con la única acción de la etapa."""

    window.title("Agenda SENA")
    window.geometry("1180x760")
    window.minsize(980, 640)
    window.configure(bg=PAGE)

    top = tk.Frame(window, bg=NAVY, height=58)
    top.pack(fill="x")
    top.pack_propagate(False)
    tk.Label(top, text="Agenda SENA", bg=NAVY, fg=WHITE,
             font=("Arial", 19, "bold")).pack(side="left", padx=28)
    tk.Label(top, text="Aplicación local para PC", bg=NAVY, fg="#c9d7f5",
             font=("Arial", 11)).pack(side="right", padx=28)

    body = tk.Frame(window, bg=PAGE)
    body.pack(fill="both", expand=True, padx=34, pady=34)
    body.grid_columnconfigure(0, weight=1)
    body.grid_columnconfigure(1, weight=1)
    body.grid_rowconfigure(0, weight=1)

    brand = tk.Frame(body, bg=NAVY, padx=42, pady=42)
    brand.grid(row=0, column=0, sticky="nsew")
    tk.Label(brand, text="◉", bg=NAVY, fg="#7dd3fc",
             font=("Arial", 42, "bold")).pack(anchor="w", pady=(24, 34))
    tk.Label(brand, text="Agenda SENA", bg=NAVY, fg=WHITE,
             font=("Arial", 32, "bold")).pack(anchor="w")
    tk.Label(brand, text="Organiza tu tiempo.\nCumple tus objetivos.",
             bg=NAVY, fg="#dbeafe", justify="left",
             font=("Arial", 17)).pack(anchor="w", pady=(16, 34))
    for text in ("Información organizada", "Seguimiento de actividades",
                 "Todo en una sola ventana"):
        row = tk.Frame(brand, bg=NAVY)
        row.pack(anchor="w", pady=7)
        tk.Label(row, text="✓", bg=NAVY, fg="#60a5fa",
                 font=("Arial", 15, "bold")).pack(side="left", padx=(0, 12))
        tk.Label(row, text=text, bg=NAVY, fg="#e0ebff",
                 font=("Arial", 12)).pack(side="left")

    card = tk.Frame(body, bg=WHITE, highlightbackground=LINE,
                    highlightthickness=1, padx=48, pady=48)
    card.grid(row=0, column=1, sticky="nsew")
    tk.Label(card, text="▣", bg=WHITE, fg=BLUE,
             font=("Segoe UI Symbol", 28)).pack(anchor="w")
    tk.Label(card, text="Bienvenido a Agenda SENA", bg=WHITE, fg=NAVY,
             font=("Arial", 24, "bold"), wraplength=420,
             justify="left").pack(anchor="w", pady=(28, 12))
    tk.Label(card,
             text="Esta primera etapa prepara la ventana y su estructura de trabajo.",
             bg=WHITE, fg=MUTED, font=("Arial", 13), wraplength=420,
             justify="left").pack(anchor="w")

    features = tk.Frame(card, bg=WHITE)
    features.pack(fill="x", pady=(34, 32))
    for symbol, text in (("▦", "Menú y resumen"), ("◷", "Calendario y citas"),
                         ("◌", "Actividades y categorías")):
        row = tk.Frame(features, bg=WHITE)
        row.pack(anchor="w", pady=7)
        tk.Label(row, text=symbol, bg=WHITE, fg=BLUE,
                 font=("Segoe UI Symbol", 16)).pack(side="left", padx=(0, 14))
        tk.Label(row, text=text, bg=WHITE, fg=NAVY,
                 font=("Arial", 12)).pack(side="left")

    tk.Button(card, text="Siguiente", command=go_to_agenda,
              bg=BLUE, fg=WHITE, activebackground="#1d4ed8",
              activeforeground=WHITE, relief="flat", cursor="hand2",
              font=("Arial", 12, "bold"), padx=18, pady=11).pack(fill="x")


def make_card(parent: tk.Frame, title: str, value: str, detail: str,
              symbol: str, color: str) -> tk.Frame:
    """Crea una tarjeta de resumen con datos demostrativos."""

    card = tk.Frame(parent, bg=WHITE, highlightbackground=LINE,
                    highlightthickness=1, padx=16, pady=14, height=112)
    card.grid_propagate(False)
    head = tk.Frame(card, bg=WHITE)
    head.pack(fill="x")
    tk.Label(head, text=title, bg=WHITE, fg=MUTED,
             font=("Arial", 10)).pack(side="left")
    tk.Label(head, text=symbol, bg=WHITE, fg=color,
             font=("Segoe UI Symbol", 17)).pack(side="right")
    tk.Label(card, text=value, bg=WHITE, fg=NAVY,
             font=("Arial", 24, "bold")).pack(anchor="w", pady=(8, 0))
    tk.Label(card, text=detail, bg=WHITE, fg=color,
             font=("Arial", 9)).pack(anchor="w")
    return card


def build_agenda(window: tk.Tk) -> None:
    """Construye la agenda base dentro de la ventana existente."""

    clear_window(window)
    window.title("Agenda SENA")
    window.configure(bg=PAGE)

    top = tk.Frame(window, bg=NAVY, height=66)
    top.pack(fill="x")
    top.pack_propagate(False)
    tk.Label(top, text="Agenda SENA", bg=NAVY, fg=WHITE,
             font=("Arial", 18, "bold")).pack(side="left", padx=24)
    tk.Label(top, text="⌕  Buscar citas, actividades o usuarios", bg=NAVY,
             fg="#c9d7f5", font=("Arial", 11)).pack(side="left", padx=70)
    tk.Label(top, text="AS  Alejandro", bg=NAVY, fg=WHITE,
             font=("Arial", 11, "bold")).pack(side="right", padx=24)

    body = tk.Frame(window, bg=CONTENT)
    body.pack(fill="both", expand=True)
    body.grid_columnconfigure(1, weight=1)
    body.grid_rowconfigure(0, weight=1)

    sidebar = tk.Frame(body, bg=NAVY, width=220, padx=18, pady=24)
    sidebar.grid(row=0, column=0, sticky="nsew")
    sidebar.grid_propagate(False)
    tk.Label(sidebar, text="MENÚ PRINCIPAL", bg=NAVY, fg="#a9bce3",
             font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 18))
    items = (("⌂", "Inicio"), ("＋", "Nueva cita"), ("▣", "Citas"),
             ("♙", "Usuarios"), ("▦", "Calendario"), ("◷", "Actividades"))
    for index, (symbol, label) in enumerate(items):
        row = tk.Frame(sidebar, bg=BLUE if index == 0 else NAVY,
                       padx=10, pady=9)
        row.pack(fill="x", pady=2)
        tk.Label(row, text=symbol, bg=row.cget("bg"),
                 fg=WHITE if index == 0 else "#8fa7d6",
                 font=("Segoe UI Symbol", 13)).pack(side="left", padx=(0, 10))
        tk.Label(row, text=label, bg=row.cget("bg"),
                 fg=WHITE if index == 0 else "#d5e1f7",
                 font=("Arial", 10, "bold" if index == 0 else "normal")).pack(side="left")
    tk.Frame(sidebar, bg="#34477b", height=1).pack(fill="x", pady=24)
    tk.Label(sidebar, text="CUENTA", bg=NAVY, fg="#a9bce3",
             font=("Arial", 9, "bold")).pack(anchor="w")
    tk.Label(sidebar, text="AS  Alejandro S.", bg=NAVY, fg=WHITE,
             font=("Arial", 10, "bold")).pack(anchor="w", pady=(16, 4))
    tk.Label(sidebar, text="Sesión de demostración", bg=NAVY, fg="#a9bce3",
             font=("Arial", 9)).pack(anchor="w")
    tk.Label(sidebar, text="↪  Cerrar sesión", bg=NAVY, fg="#d5e1f7",
             font=("Arial", 10)).pack(anchor="w", side="bottom", pady=10)

    content = tk.Frame(body, bg=CONTENT, padx=28, pady=24)
    content.grid(row=0, column=1, sticky="nsew")
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(3, weight=1)
    tk.Label(content, text="Buenos días, Alejandro", bg=CONTENT, fg=NAVY,
             font=("Arial", 22, "bold")).grid(row=0, column=0, sticky="w")
    tk.Label(content, text="Aquí tienes el resumen de tu agenda para hoy.",
             bg=CONTENT, fg=MUTED, font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=(4, 18))

    summaries = tk.Frame(content, bg=CONTENT)
    summaries.grid(row=2, column=0, sticky="ew", pady=(0, 18))
    for column in range(4):
        summaries.grid_columnconfigure(column, weight=1)
    cards = (("Citas de hoy", "04", "+2 esta semana", "▦", BLUE),
             ("Pendientes", "08", "3 importantes", "✓", ORANGE),
             ("Próxima cita", "10:00", "Reunión", "◷", GREEN),
             ("Actividades", "12", "En progreso", "◌", PURPLE))
    for column, data in enumerate(cards):
        make_card(summaries, *data).grid(row=0, column=column, sticky="ew", padx=(0 if column == 0 else 8, 0))

    middle = tk.Frame(content, bg=CONTENT)
    middle.grid(row=3, column=0, sticky="nsew", pady=(0, 18))
    middle.grid_columnconfigure(0, weight=3)
    middle.grid_columnconfigure(1, weight=2)
    middle.grid_rowconfigure(0, weight=1)

    calendar = tk.Frame(middle, bg=WHITE, highlightbackground=LINE,
                        highlightthickness=1, padx=16, pady=14)
    calendar.grid(row=0, column=0, sticky="nsew", padx=(0, 9))
    tk.Label(calendar, text="▦  Calendario mensual", bg=WHITE, fg=NAVY,
             font=("Arial", 13, "bold")).pack(anchor="w")
    tk.Label(calendar, text="Octubre 2026     ‹   ›", bg=WHITE, fg=MUTED,
             font=("Arial", 10)).pack(anchor="w", pady=(5, 10))
    grid = tk.Frame(calendar, bg=WHITE)
    grid.pack(fill="both", expand=True)
    for col, day in enumerate(("LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM")):
        grid.grid_columnconfigure(col, weight=1)
        tk.Label(grid, text=day, bg="#f1f5f9", fg=MUTED,
                 font=("Arial", 8, "bold"), pady=5).grid(row=0, column=col, sticky="nsew")
    for number in range(1, 29):
        row, col = (number - 1) // 7 + 1, (number - 1) % 7
        bg = LIGHT_BLUE if number == 23 else WHITE
        fg = BLUE if number == 23 else NAVY
        tk.Label(grid, text=str(number), bg=bg, fg=fg, relief="solid",
                 bd=1, font=("Arial", 9, "bold" if number == 23 else "normal"),
                 pady=8).grid(row=row, column=col, sticky="nsew")

    today = tk.Frame(middle, bg=WHITE, highlightbackground=LINE,
                     highlightthickness=1, padx=16, pady=14)
    today.grid(row=0, column=1, sticky="nsew", padx=(9, 0))
    tk.Label(today, text="◷  Agenda de hoy", bg=WHITE, fg=NAVY,
             font=("Arial", 13, "bold")).pack(anchor="w")
    tk.Label(today, text="Viernes 23 de octubre", bg=WHITE, fg=MUTED,
             font=("Arial", 10)).pack(anchor="w", pady=(5, 16))
    for time, title, color in (("09:00", "Plan de trabajo semanal", BLUE),
                               ("10:00", "Reunión de proyecto", ORANGE),
                               ("14:30", "Entregar actividad SENA", GREEN)):
        row = tk.Frame(today, bg=WHITE)
        row.pack(fill="x", pady=8)
        tk.Label(row, text="●", bg=WHITE, fg=color,
                 font=("Arial", 11)).pack(side="left")
        tk.Label(row, text=time, bg=WHITE, fg=MUTED,
                 font=("Arial", 9)).pack(side="left", padx=8)
        tk.Label(row, text=title, bg=WHITE, fg=NAVY,
                 font=("Arial", 9, "bold"), wraplength=180,
                 justify="left").pack(side="left")

    bottom = tk.Frame(content, bg=CONTENT)
    bottom.grid(row=4, column=0, sticky="ew")
    bottom.grid_columnconfigure(0, weight=3)
    bottom.grid_columnconfigure(1, weight=2)
    table = tk.Frame(bottom, bg=WHITE, highlightbackground=LINE,
                     highlightthickness=1, padx=16, pady=14)
    table.grid(row=0, column=0, sticky="ew", padx=(0, 9))
    tk.Label(table, text="▣  Citas recientes", bg=WHITE, fg=NAVY,
             font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 10))
    for row in (("Reunión de proyecto", "23 oct 2026", "10:00", "Pendiente"),
                ("Clase de Python", "24 oct 2026", "18:00", "Programada")):
        tk.Label(table, text="   ".join(row), bg=WHITE, fg=NAVY,
                 font=("Arial", 9), anchor="w").pack(fill="x", pady=5)

    activities = tk.Frame(bottom, bg=WHITE, highlightbackground=LINE,
                          highlightthickness=1, padx=16, pady=14)
    activities.grid(row=0, column=1, sticky="ew", padx=(9, 0))
    tk.Label(activities, text="◌  Actividades", bg=WHITE, fg=NAVY,
             font=("Arial", 13, "bold")).pack(anchor="w")
    tk.Label(activities, text="Progreso semanal                 70%",
             bg=WHITE, fg=MUTED, font=("Arial", 9)).pack(anchor="w", pady=(12, 8))
    tk.Label(activities, text="●  Revisar entregas       Completada",
             bg=WHITE, fg=GREEN, font=("Arial", 9)).pack(anchor="w", pady=3)
    tk.Label(activities, text="●  Preparar reunión       En progreso",
             bg=WHITE, fg=ORANGE, font=("Arial", 9)).pack(anchor="w", pady=3)


def main() -> None:
    """Inicia el flujo de dos estados dentro de una sola ventana."""

    window = tk.Tk()
    build_login(window, lambda: build_agenda(window))
    window.mainloop()


if __name__ == "__main__":
    main()
