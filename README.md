# Agenda SENA

Proyecto educativo de una agenda de escritorio local desarrollada primero en
Python.

## Punto de entrada local

Ejecutar: python main.py

## Estructura principal

- main.py: punto de entrada de la aplicación integrada para PC.
- src/: carcasa de una sola ventana, estado, navegación y vistas integradas.
- stages/: único espacio de trabajo del estudiante.
- web/: comportamiento de la secuencia visual de GitHub Pages.
- config/: registro interno de módulos aprobados para la integración.
- docs/parts/: especificaciones, teoría y requisitos de cada stage.
- index.html: único visor web de las dos ventanas visuales.
- assets/: estilos compartidos.

## Metodología

Cada stage es un módulo independiente. El estudiante lo desarrolla, lo prueba
y revisa su preview.html sin importar archivos de otros stages.

Después de aprobarlo, el módulo se conecta a la aplicación integrada. La
aplicación final puede crecer de esta manera:

Stage 01 aprobado  -> ventana inicial
Stage 02 aprobado  -> se agrega una función
Stage 03 aprobado  -> se agrega otra función

La acumulación ocurre en main.py, src/ y en la salida publicada. No se cargan
automáticamente todos los previews existentes. La página solo muestra los
módulos registrados en config/integration.json.

## Regla para el estudiante

Durante una lección, el estudiante trabaja solamente en la carpeta del stage:

stages/01_python_window/

No necesita modificar main.py, src/, web/ ni config/. Esa integración se
realiza después de revisar que el módulo cumple su especificación.

GitHub Pages no ejecuta Python. El visor muestra únicamente dos ventanas
visuales: la pantalla inicial con `Siguiente` y la ventana principal de Agenda
con espacios preparados para los componentes.

El archivo `web/screen.js` cambia de una ventana a la otra. No muestra menús,
tarjetas de stages, indicadores de avance ni elementos adicionales.

La metodología completa está en docs/stage_contract.md.
