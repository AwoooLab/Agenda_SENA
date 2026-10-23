# Agenda SENA

Proyecto educativo de una agenda de escritorio local desarrollada primero en
Python.

## Punto de entrada local

Ejecutar: python main.py

## Estructura principal

- main.py: orquestador de la aplicación Python para PC.
- stages/: archivos de trabajo organizados por función y etapa.
- docs/parts/: especificaciones, teoría y requisitos de cada etapa.
- index.html: único visor de la aplicación acumulada en GitHub Pages.
- assets/: estilos compartidos del visor.
- plan.md: plan general del proyecto.

## Metodología de integración

La aplicación se construye progresivamente. Cada stage conserva las funciones
anteriores y agrega una nueva dentro de la misma aplicación.

01: ventana
02: ventana + formulario
03: ventana + formulario + tabla
04: todo lo anterior + datos locales
05: todo lo anterior + usuarios
06: todo lo anterior + inicio de sesión

Cada carpeta contiene el código Python de la etapa y un preview.html. El preview
es un fragmento de la aplicación; el index.html de la raíz carga todos los
fragmentos en orden dentro de una sola ventana visual. No hay tarjetas, iframe,
selector ni indicador de etapa.

GitHub Pages muestra la versión visual interactiva. No ejecuta main.py; la
aplicación real de escritorio se ejecuta localmente con Python y Tkinter.

## Pruebas

Las pruebas se incorporan en la carpeta de la etapa que las necesita. Cada
files.txt explica cuándo ejecutarlas y qué resultado esperar.
