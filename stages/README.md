# Cómo trabajar las etapas

Cada carpeta representa una etapa de la clase. El alumno debe trabajar una
etapa completa antes de pasar a la siguiente.

## Método con ChatGPT gratuito

1. Abrir el hito correspondiente en `docs/milestones/`.
2. Copiar la instrucción indicada en ChatGPT.
3. Pedir un solo archivo por vez.
4. Crear o reemplazar únicamente el archivo indicado.
5. Revisar manualmente el resultado de la etapa.
6. Integrar el resultado en la estructura principal.
7. Actualizar `plan.md` y continuar.

## Regla de integración

Los archivos dentro de `stages/` son entregas didácticas aisladas. El archivo
`files.txt` de cada carpeta enumera los archivos que se crearán o modificarán.
La versión integrada debe quedar en `app.py`, `src/`, `data/` o `tests/`, según
indique el hito de `docs/milestones/`.

No pedir a ChatGPT que genere todo el proyecto de una sola vez. Cada instrucción
está diseñada para producir un archivo pequeño y revisable.

Cada `files.txt` usa rutas relativas a su propia etapa. Por ejemplo,
`stages/01_python_window/files.txt` solo enumera `app.py`, que debe existir como
`stages/01_python_window/app.py`. Después, el alumno puede integrar ese resultado
en `src/` o en la raíz del proyecto cuando el hito lo indique.
