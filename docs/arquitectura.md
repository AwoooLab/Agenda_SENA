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
- web/screen.js: controla la secuencia de las dos ventanas visuales.
- index.html: muestra únicamente una ventana SVG a la vez.

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
Incorporación en un espacio de la ventana de agenda
        ->
Revisión en la única página de GitHub Pages

## Ventana y navegación

La aplicación integrada utiliza una sola ventana. Las funciones futuras no se
ponen en el menú antes de ser integradas. Solo aparecen las rutas registradas
en la configuración de integración.

El router reemplaza el contenido del área central. No se crean ventanas
separadas para login, calendario, tablas o actividades.

La misma regla se aplica al visor web: `web/screen.js` muestra primero el
inicio de sesión y, al pulsar `Ingresar`, reemplaza esa pantalla por la agenda.
La existencia de una carpeta en `stages/` no crea una pantalla nueva.

## Referencias visuales y espacios

`assets/login-window.svg` y `assets/agenda-window.svg` son las referencias
editables del resultado terminado. La primera define la identidad, los campos
de acceso y sus estados. La segunda define la distribución de la aplicación
autenticada.

La agenda se divide en espacios estables para que cada stage pueda agregar una
función sin rediseñar toda la pantalla:

| Espacio | Contenido esperado |
|---|---|
| `agenda.topbar` | Búsqueda y usuario activo |
| `agenda.sidebar` | Navegación interna |
| `agenda.summary` | Tarjetas de resumen |
| `agenda.calendar` | Calendario mensual |
| `agenda.today` | Actividades del día |
| `agenda.appointments` | Tabla de citas recientes |
| `agenda.activities` | Progreso, categorías y estados |

El login utiliza `login.brand`, `login.form` y `login.feedback`.

## Composición progresiva

La página principal no debe mostrar una lista de stages ni un medidor. Debe
mostrar la aplicación y conservar los espacios que todavía no tienen un
componente aprobado. Cuando se aprueba un stage, la integración reemplaza el
espacio correspondiente por su componente, manteniendo los anteriores.

El registro de `config/integration.json` identifica la relación entre stage,
ventana y espacio. `web/screen.js` mantiene el cambio entre login y agenda, y
`main.py`/`src/` aplican la misma idea en Tkinter.

La composición no significa que un stage importe otro stage. La dependencia
solo existe en el orquestador después de que cada módulo fue validado.

## GitHub Pages

GitHub Pages no ejecuta `main.py`. Su función actual es mostrar una secuencia
visual final: primero `assets/login-window.svg` y luego
`assets/agenda-window.svg`. La segunda ventana representa el programa terminado
con datos de ejemplo.

Los previews de `stages/` y el registro de `config/integration.json` se
conservan para la metodología educativa y la integración futura, pero no se
cargan automáticamente en este visor.
