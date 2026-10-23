# Agenda SENA

Proyecto educativo de una agenda de escritorio local desarrollada primero en Python.

## Ejecutar la aplicación

```text
python app.py
```

## Ejecutar las pruebas

```text
python -m unittest discover -s tests -v
```

## Estructura principal

- `app.py`: punto de entrada de la aplicación Python.
- `src/`: código principal dividido por responsabilidades.
- `data/`: información local de la agenda.
- `tests/`: pruebas automáticas.
- `stages/`: archivos que el alumno irá creando o modificando por etapa.
- `docs/milestones/`: hitos completos con requisitos, prompts e integración.
- `config/`: configuración compartida.
- `index.html`: vista informativa mínima para GitHub Pages.
- `plan.md`: plan de desarrollo.

GitHub Pages solo muestra la página informativa; no ejecuta la aplicación Python.
- `docs/file_status.md`: automatic checklist of planned files.
- `scripts/generate_file_status.py`: local checklist generator.

## File checklist

The [file status checklist](docs/file_status.md) is generated from each
`stages/*/files.txt` file. A green check means the planned file already exists.
The paths in each manifest are relative to that stage folder.

Run this locally after creating or completing a file:

```text
python scripts/generate_file_status.py
```

GitHub Actions also refreshes it automatically after each push to `main`.
