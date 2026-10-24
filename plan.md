# Plan del proyecto Agenda SENA

## Regla general

El estudiante construye módulos independientes dentro de stages/. Después de
validar cada módulo, se integra en una aplicación de una sola ventana.

La aplicación integrada utiliza main.py y src/. GitHub Pages muestra una
secuencia visual mediante index.html: primero la entrada inicial y después la
ventana principal de la agenda.

## Base de integración

- src/app_shell.py: una sola ventana.
- src/router.py: navegación entre vistas dentro de esa ventana.
- src/state.py: estado compartido, como el usuario autenticado.
- src/views/: vistas integradas.
- web/screen.js: secuencia visual de las dos ventanas de Pages.
- config/integration.json: módulos aprobados y visibles.

## Flujo visual inicial

GitHub Pages muestra únicamente dos ventanas, una a la vez:

1. Inicio de sesión con usuario, contraseña y botón `Ingresar`.
2. Ventana principal terminada de Agenda SENA con datos de ejemplo.

Los datos mostrados son demostrativos. Cada stage posterior reemplazará o
ampliará la función correspondiente sin crear otra ventana externa.

## Secuencia de construcción

### Stage 01 — Ventana inicial

Construir y validar una ventana inicial independiente. Después se registra como
la primera vista integrada.

### Stage 02 — Modelo de datos

Construir un modelo de cita independiente. No depende del Stage 01. Después se
conecta a la vista o servicio que corresponda.

### Stage 03 — Guardado JSON

Construir funciones independientes para guardar y cargar datos. Después se
conectan al modelo aprobado.

### Stage 04 — Base de datos SQLite

Construir la base y sus consultas como módulo independiente. Después se conecta
al servicio de datos de la aplicación.

### Stage 05 — Registro de usuarios

Construir registro, validaciones y pruebas con datos propios.

### Stage 06 — Inicio de sesión

Construir login y sesión como módulo independiente. Después se conecta al
estado compartido y al router.

### Stage 07 — Ventana principal

Construir el panel principal y sus vistas navegables.

### Stage 08 — Calendario mensual

Construir calendario, navegación de meses y selección de días.

### Stage 09 — Actividades, categorías y colores

Construir actividades, categorías, colores y filtros.

### Stage 10 — Pruebas, seguridad y ejecutable

Validar la aplicación integrada y preparar el ejecutable de Windows.

La documentación detallada del contrato está en docs/stage_contract.md.
