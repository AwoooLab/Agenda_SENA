# Cómo trabajar las etapas

Cada carpeta representa una etapa de la clase. El alumno debe trabajar una etapa completa antes de pasar a la siguiente.

## Método con ChatGPT gratuito

1. Abrir el hito correspondiente en `docs/milestones/`.
2. Copiar el prompt indicado en ChatGPT.
3. Pedir un solo archivo por vez.
4. Crear o reemplazar únicamente el archivo indicado.
5. Ejecutar la validación de la etapa.
6. Integrar el resultado en la estructura principal.
7. Actualizar `plan.md` y continuar.

## Regla de integración

Los archivos dentro de `stages/` son entregas didácticas aisladas. El archivo
`files.txt` de cada carpeta enumera los archivos que se crearán o modificarán.
La versión integrada debe quedar en `app.py`, `src/`, `data/` o `tests/`, según
indique el hito de `docs/milestones/`.

No pedir a ChatGPT que genere todo el proyecto de una sola vez. Cada prompt está diseñado para producir un archivo pequeño y revisable.
After creating or completing a file, run `python scripts/generate_file_status.py`
to refresh `docs/file_status.md`. GitHub Actions performs the same update
automatically after each push to `main`.

Each `files.txt` uses paths relative to its own stage. For example,
`stages/01_python_window/files.txt` only lists `app.py`, which must exist as
`stages/01_python_window/app.py`. Later, the student can integrate that result
into `src/` or the project root when the milestone requires it.
