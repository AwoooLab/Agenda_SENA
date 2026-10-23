# Plan del proyecto Agenda SENA

## Regla general

Agenda SENA se construye como una única aplicación acumulativa. Cada stage
agrega una función visible y conserva las anteriores. El estudiante revisa
todo el resultado desde la única página principal de GitHub Pages.

index.html carga los preview.html de stages/ en orden dentro de una sola
ventana. No hay tarjetas, iframe, indicador de etapa ni selector.

## Stage 01 — Ventana de Python

- Crear la primera ventana con Tkinter.
- Mostrar el nombre de Agenda SENA.
- Agregar el primer botón funcional.
- Representar la ventana en preview.html.

## Stage 02 — Modelo y formulario de cita

- Definir título, fecha, hora, descripción y estado.
- Mostrar el formulario dentro de la misma aplicación.
- Conservar la ventana y el botón del stage anterior.

## Stage 03 — Tabla y guardado JSON

- Mostrar las citas en una tabla.
- Agregar acciones para guardar y cargar información.
- Conservar el formulario y la tabla al avanzar.

## Stage 04 — Base de datos SQLite

- Crear las tablas principales.
- Usar consultas parametrizadas.
- Hacer visible la relación entre usuarios y actividades.

## Stage 05 — Registro de usuarios

- Crear usuarios locales.
- Validar campos obligatorios y nombres duplicados.
- Agregar el registro sin perder las funciones anteriores.

## Stage 06 — Inicio de sesión

- Proteger las contraseñas.
- Crear inicio y cierre de sesión.
- Mostrar el usuario activo en la misma aplicación.

## Stage 07 — Ventana principal

- Organizar el panel principal.
- Mostrar navegación y resúmenes.
- Mantener formulario, tabla, usuarios y sesión.

## Stage 08 — Calendario mensual

- Mostrar días y semanas del mes.
- Navegar entre meses.
- Relacionar las actividades con una fecha.

## Stage 09 — Actividades, categorías y colores

- Crear, editar, completar y eliminar actividades.
- Asignar categorías y colores.
- Filtrar por fecha, categoría y estado.

## Stage 10 — Pruebas, seguridad y ejecutable

- Ejecutar las pruebas de las etapas.
- Revisar datos y credenciales.
- Preparar el ejecutable para Windows.
- Mostrar el estado final de la aplicación acumulada.

La lógica real crece en main.py. La comprobación visual crece con los
fragmentos preview.html y se revisa siempre en la única página principal.
