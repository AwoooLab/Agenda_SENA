# Cómo trabajar las etapas

Cada carpeta representa una etapa de la construcción de Agenda SENA. El alumno
completa una etapa antes de continuar con la siguiente, pero el resultado
visual siempre pertenece a la misma aplicación.

## Qué contiene cada etapa

- Los archivos Python que corresponden a la función.
- files.txt con la teoría, ejemplos, restricciones y validaciones.
- preview.html con el fragmento visual que se agrega a la ventana principal.
- Los nombres de carpetas y archivos están en inglés.
- Las explicaciones y lecciones están en español.

## Flujo de trabajo

1. Abrir la especificación del stage en docs/parts/.
2. Leer el files.txt de la carpeta.
3. Crear o actualizar únicamente los archivos solicitados.
4. Probar la lógica local de Python cuando corresponda.
5. Actualizar el preview.html con la función visible de la etapa.
6. Subir los cambios a GitHub.
7. Abrir únicamente la página principal de GitHub Pages.
8. Comprobar que la función nueva aparece junto con las anteriores.
9. Corregir cualquier regresión antes de continuar.

## Regla del visor único

El index.html de la raíz carga los diez preview.html en orden dentro de una
sola ventana. No se muestran tarjetas, iframe, selectores ni indicadores de
etapa.

Cada preview es un fragmento y no una página independiente. Debe contener
solamente el HTML de la función que aporta su etapa, sin doctype, head, body,
navegación propia ni encabezados repetidos.

## Integración de Python

Los archivos de stages/ sirven para aprender y construir cada función. Cuando
una función se aprueba, se incorpora progresivamente en main.py, que es el
orquestador de la aplicación local para PC.

GitHub Pages no ejecuta Python. Su objetivo es permitir revisar la composición
visual y las interacciones web equivalentes.

## Trabajo con ChatGPT

La solicitud debe indicar:

- La ruta exacta del archivo.
- La lección que se está estudiando.
- El código que ya se escribió.
- El error o comportamiento observado.
- Que no se modifiquen otros archivos.

Ejemplo:

Estoy trabajando en stages/01_python_window/app.py. Explícame tkinter.Tk()
y revisa únicamente el fragmento que escribí. No generes el proyecto completo
ni modifiques otros archivos.
