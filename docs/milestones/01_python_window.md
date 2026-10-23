# Hito 01 — Ventana de Python

## Objetivo

Abrir la primera ventana de escritorio de Agenda SENA usando Python y Tkinter.

## Archivos

- `stages/01_python_window/app.py`: ejercicio aislado para el alumno.
- `src/interface.py`: módulo de interfaz integrado.
- `app.py`: punto de entrada de la aplicación.

## Requisitos

- Python 3.
- Solo Tkinter; no usar paquetes externos.
- Título de la ventana: `Agenda SENA`.
- Botón visible para cerrar la ventana.

## Integración

El archivo principal `app.py` importa `ejecutar()` desde `src/interface.py`.
El archivo de la etapa es solo el ejercicio y se debe revisar antes de copiar
la idea que funciona a `src/`.

## Comprobación manual

```text
python stages/01_python_window/app.py
python app.py
```

## Secuencia de solicitudes

Pedir un solo archivo a ChatGPT cada vez. Primero solicitar
`stages/01_python_window/app.py`; después de revisarlo, solicitar o adaptar
`src/interface.py`.
