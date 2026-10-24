# Arquitectura de Agenda SENA

Agenda SENA tiene dos niveles relacionados, pero diferentes:

1. Los stages independientes que construye y prueba el estudiante.
2. La aplicación integrada que reúne los módulos aprobados.

## Espacio del estudiante

El estudiante trabaja únicamente en stages/. Cada carpeta contiene una función
o módulo, sus archivos Python, files.txt y preview.html.

Un stage no importa otro stage y no necesita que otro stage exista. Por
ejemplo, el login puede probarse con un usuario de demostración propio sin
depender de una tabla o de un botón construido en otra carpeta.

## Estructura de integración

- main.py: inicia la aplicación local.
- src/app_shell.py: crea una sola ventana de Tkinter.
- src/router.py: cambia la vista dentro del área central sin abrir otra ventana.
- src/state.py: contiene el estado compartido, como el usuario actual.
- src/views/: recibe las vistas de los módulos aprobados.
- config/integration.json: registra los módulos que ya están integrados.
- web/app.js: carga en Pages únicamente los previews registrados.
- index.html: muestra la única ventana web de la aplicación integrada.

La estructura de integración es una base preparada. El estudiante no tiene que
editarla durante la lección de un stage.

## Flujo de una función

Stage independiente
        ->
Prueba local y validación de preview.html
        ->
Contrato de integración
        ->
Conexión en src/ o main.py
        ->
Registro del módulo en config/integration.json
        ->
Revisión en la única página de GitHub Pages

## Ventana y navegación

La aplicación integrada utiliza una sola ventana. Las funciones futuras no se
ponen en el menú antes de ser integradas. Solo aparecen las rutas registradas
en la configuración de integración.

El router reemplaza el contenido del área central. No se crean ventanas
separadas para login, calendario, tablas o actividades.

La misma regla se aplica al visor web: `web/app.js` crea la navegación a partir
de los módulos aprobados y muestra una sola vista dentro del área central. La
existencia de una carpeta en `stages/` no crea una ruta ni una pantalla nueva.

## GitHub Pages

GitHub Pages no ejecuta main.py. Su función es mostrar la representación web
del estado integrado actual. La página no debe cargar todos los previews que
existan en el repositorio; debe cargar únicamente los módulos aprobados en
config/integration.json.

La caché se reduce mediante versiones en la URL y el botón Actualizar vista.
