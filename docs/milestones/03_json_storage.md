# Hito 03 — Almacenamiento temporal en JSON

## Objetivo

Aprender a guardar una lista de actividades localmente antes de introducir una
base de datos.

## Archivos

- `stages/03_json_storage/storage.py`.
- `stages/03_json_storage/demo.py`.
- `src/storage.py`.
- `data/agenda.json`.
- `tests/test_storage.py`.

## Requisitos

Usar `json` y `pathlib`, codificación UTF-8, sangría legible y un comportamiento
claro cuando el archivo no exista.

## Integración

El módulo de almacenamiento recibe los datos y una ruta; no debe crear controles
de Tkinter. La interfaz lo utilizará más adelante.

## Comprobación manual

Guardar una actividad, cargarla nuevamente y comparar el resultado. Ejecutar las
pruebas del almacenamiento.

## Secuencia de solicitudes

Solicitar a ChatGPT `storage.py`, después `demo.py` y finalmente la prueba. Nunca
pedir la aplicación completa en una sola solicitud.
