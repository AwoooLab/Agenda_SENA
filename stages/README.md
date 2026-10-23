# Cómo trabajar las etapas

Cada carpeta representa una etapa de la clase. El alumno debe completar una
etapa antes de pasar a la siguiente.

## Qué contiene cada etapa

- Cada etapa contiene los archivos que corresponden a su alcance.
- `files.txt` contiene la guía teórica y práctica de todos los archivos de la
  etapa.
- Los nombres de carpetas y archivos se mantienen en inglés para que coincidan
  con la estructura del proyecto.
- Las explicaciones, lecciones y ejemplos están en español.

## Cómo estudiar un archivo

1. Abrir el `files.txt` de la etapa.
2. Buscar la sección del archivo que se va a construir.
3. Leer las lecciones en orden.
4. Revisar las librerías permitidas y las restricciones.
5. Implementar la solución en el archivo indicado.
6. Usar los fragmentos cortos como referencia para completar la lógica.
7. Ejecutar la comprobación manual indicada.
8. Corregir los errores antes de continuar con el siguiente archivo.

## Cómo trabajar con ChatGPT gratuito

ChatGPT se puede usar como tutor de una sola lección o de un solo archivo.
La solicitud debe indicar:

- La ruta exacta del archivo.
- La lección que no se entiende.
- El código que el alumno ya escribió.
- El error que apareció.
- Que no se modifiquen otros archivos.

Ejemplo de solicitud:

```text
Estoy trabajando en stages/01_python_window/app.py.
Explícame cómo funciona tkinter.Tk() y revisa únicamente el fragmento que
escribí. No generes el proyecto completo ni modifiques otros archivos.
```

## Regla de integración

Los archivos dentro de `stages/` son ejercicios didácticos aislados. Cuando el
alumno termina una etapa, su solución se integra manualmente en `app.py`,
`src/`, `data/` o `tests/`, según indique el hito correspondiente en
`docs/milestones/`.

El archivo de la etapa no se convierte automáticamente en parte de la
aplicación. Primero se entiende, se escribe, se ejecuta y luego se integra.

## Regla de aprendizaje

No pedir a ChatGPT que genere todo el proyecto de una sola vez. Cada archivo se
construye con las lecciones necesarias que aparecen en su propio `files.txt`.
