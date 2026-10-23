# Cómo trabajar las etapas

Cada carpeta representa una etapa de la clase. El alumno debe trabajar una etapa completa antes de pasar a la siguiente.

## Método con ChatGPT gratuito

1. Abrir el `objetivo.txt` de la etapa.
2. Copiar el prompt indicado en ChatGPT.
3. Pedir un solo archivo por vez.
4. Crear o reemplazar únicamente el archivo indicado.
5. Ejecutar la validación de la etapa.
6. Integrar el resultado en la estructura principal.
7. Actualizar `plan.md` y continuar.

## Regla de integración

Los archivos dentro de `etapas/` son entregas didácticas aisladas. La versión que usa la aplicación principal debe quedar en `app.py`, `src/`, `datos/` o `pruebas/`, según indique el `objetivo.txt`.

No pedir a ChatGPT que genere todo el proyecto de una sola vez. Cada prompt está diseñado para producir un archivo pequeño y revisable.
