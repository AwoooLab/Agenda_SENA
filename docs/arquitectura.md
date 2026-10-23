# Arquitectura de Agenda SENA

Agenda SENA es una aplicación de escritorio local para Windows. La versión
funcional se construye con Python y Tkinter; GitHub Pages se utiliza como
visor visual e interactivo del resultado acumulado.

## Componentes principales

- main.py: punto de entrada de la aplicación Python integrada.
- stages/: archivos de cada etapa, organizados en orden de construcción.
- stages/*/app.py y demás archivos Python: ejercicios y funciones de cada etapa.
- stages/*/preview.html: fragmento visual que agrega la función de esa etapa.
- index.html: único orquestador y único visor que debe abrir el estudiante.
- assets/stage-preview.css: estilos compartidos de los fragmentos visuales.

## Flujo acumulativo

El index.html mantiene una sola ventana de Agenda SENA. Su JavaScript carga
los preview.html en el orden 01 a 10 y los inserta dentro del mismo
contenedor. Por eso cada archivo nuevo se alinea con lo que ya existe:

01: ventana inicial
02: agrega el formulario de cita
03: agrega la tabla de citas
04: agrega la estructura de datos locales
05: agrega el registro
06: agrega el inicio de sesión
07: agrega el panel principal
08: agrega el calendario
09: agrega actividades, categorías y colores
10: agrega validaciones y entrega

No se usan iframe, tarjetas independientes, medidores ni un indicador de etapa
actual. Los stages son el origen de cada función; index.html es el orquestador
que las reúne en una única vista.

## Regla para un preview.html

Un preview debe contener solamente el fragmento visual que agrega su etapa:

- No debe incluir doctype, html, head ni body.
- No debe crear otra navegación o una ventana independiente.
- Debe conservar los identificadores y funciones que necesiten las etapas
  siguientes.
- Debe mostrar una función real o una representación clara de su lógica.
- Debe usar los estilos compartidos de assets/stage-preview.css.

## Relación con Python

GitHub Pages no ejecuta Python. Las interacciones del visor son una
representación web para comprobar la composición y el flujo visual. La lógica
real se integra progresivamente en main.py y se ejecuta localmente en el PC.

## Actualización

El botón Actualizar vista agrega una versión nueva a la URL y cada preview se
carga con una versión nueva para evitar que el navegador conserve contenido
antiguo. GitHub Pages puede tardar unos segundos en publicar un commit nuevo.
