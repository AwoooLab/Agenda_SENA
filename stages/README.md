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
5. Agregar o actualizar la solución en el archivo indicado dentro de GitHub.
6. Usar los fragmentos cortos como referencia para completar la lógica.
7. Actualizar el `preview.html` de la etapa con la representación visual.
8. Subir los cambios y revisar el resultado publicado en GitHub Pages.
9. Corregir lo necesario antes de continuar con el siguiente archivo.

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

## Regla de integración en `main.py`

Los archivos dentro de `stages/` son ejercicios didácticos aislados. Cuando el
alumno termina una etapa, su solución se incorpora progresivamente en el
`main.py` de la raíz, según indique el hito correspondiente en
`docs/milestones/`.

El archivo de la etapa no se conecta automáticamente con otros archivos. Cada
carpeta conserva su trabajo y `main.py` funciona como el orquestador de la
aplicación final.

## Flujo visible en GitHub Pages

El estudiante agrega en GitHub los archivos de la etapa, actualiza su
`preview.html` y, cuando la etapa está lista, incorpora su funcionalidad en el
`main.py` de la raíz. Después agrega la tarjeta de esa clase en el `index.html`
de la raíz, sube los cambios y abre únicamente la página principal de GitHub
Pages. Esa colección es la comprobación visual del proceso.

El `index.html` de la raíz solo organiza las tarjetas de las clases terminadas;
no contiene la interfaz de cada etapa. La interfaz visual vive en el
`preview.html` de su propia carpeta.

## Regla de aprendizaje

No pedir a ChatGPT que genere todo el proyecto de una sola vez. Cada archivo se
construye con las lecciones necesarias que aparecen en su propio `files.txt`.
