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

Durante la Etapa 01, GitHub Pages muestra únicamente una ventana a la vez y
permite comprobar este recorrido:

1. Bienvenida de Agenda SENA con el único botón `Siguiente`.
2. Ventana principal de Agenda SENA con sus espacios base y datos de ejemplo.

En etapas posteriores, la bienvenida se ampliará hasta el inicio de sesión con
usuario, contraseña y botón `Ingresar`. Los datos mostrados son demostrativos.
Cada stage reemplazará o ampliará la función correspondiente sin crear otra
ventana externa.

## Especificación visual que debe reproducirse

El login debe conservar marca, bienvenida, usuario o correo, contraseña,
mostrar/ocultar, recordarme, recuperar contraseña, ingresar y crear cuenta.

La agenda debe conservar barra superior, búsqueda, usuario, menú lateral,
saludo, nueva cita, tarjetas de resumen, calendario mensual, agenda del día,
tabla de citas recientes y panel de actividades. Los iconos se toman de
`assets/icons/` y no se redibujan dentro de cada stage.

Cada hito documenta qué espacio recibe el componente y qué datos de prueba
deben aparecer en ese espacio. El preview del stage es un fragmento visual;
`index.html` sigue siendo el único visor de las dos ventanas.

## Secuencia de construcción

### Stage 01 — Bienvenida, navegación y agenda base

Construir una sola ventana con dos estados: una bienvenida inicial con el único
botón `Siguiente` y, después, una agenda base con menú, resumen, calendario,
agenda del día, citas recientes y actividades. Esta etapa no solicita
credenciales ni guarda datos; prepara la composición que las etapas posteriores
completarán con login, persistencia y lógica de negocio.

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

Completar los componentes que faltan en la agenda: formulario de actividad,
agenda de hoy, citas recientes, resumen, categorías, colores, progreso e
iconos reutilizables.

### Stage 10 — Pruebas, seguridad y ejecutable

Validar la aplicación integrada y preparar el ejecutable de Windows.

La documentación detallada del contrato está en docs/stage_contract.md.

## Orden de validación

Para cada etapa se sigue el mismo ciclo:

1. Leer el milestone y el `files.txt`.
2. Identificar `screen`, `slot`, datos de prueba y archivos permitidos.
3. Ejecutar el módulo independiente en el PC.
4. Actualizar `preview.html` con la misma jerarquía y estados.
5. Comprobar controles, mensajes, errores y conservación de componentes.
6. Aprobar el stage y registrar su espacio en la integración.
7. Revisar el flujo completo en GitHub Pages y en `main.py`.
