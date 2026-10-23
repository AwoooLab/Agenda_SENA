# Plan del proyecto Agenda SENA

## Etapa 00 — Repositorio y vista informativa

- Mantener el proyecto en GitHub.
- Usar `index.html` únicamente como presentación en GitHub Pages.
- Confirmar que la página muestra el nombre del proyecto.

## Etapa 01 — Ventana de Python

- Crear la ventana inicial con Tkinter.
- Ejecutar la aplicación localmente en el computador.
- Revisar que la ventana abra y cierre correctamente.

## Etapa 02 — Modelo de datos

- Crear el modelo de una cita o tarea.
- Definir título, fecha, hora, descripción y estado.
- Revisar los campos obligatorios.

## Etapa 03 — Guardado JSON temporal

- Aprender a leer y guardar datos localmente.
- Controlar archivos inexistentes o dañados.
- Revisar la lectura y escritura de datos.

## Etapa 04 — Base de datos SQLite

- Crear las tablas principales.
- Usar consultas parametrizadas.
- Preparar la base para usuarios y actividades.

## Etapa 05 — Registro de usuarios

- Crear usuarios locales.
- Revisar nombres duplicados y campos obligatorios.
- Separar modelos, repositorios y servicios.

## Etapa 06 — Inicio de sesión

- Proteger contraseñas con un resumen y una sal criptográfica.
- Crear el inicio y cierre de sesión.
- Mantener el usuario actual en memoria.

## Etapa 07 — Ventana principal

- Crear la estructura de navegación.
- Mostrar el usuario activo.
- Preparar las vistas de la agenda.

## Etapa 08 — Calendario mensual

- Mostrar días y semanas del mes.
- Navegar entre meses.
- Seleccionar un día y mostrar sus actividades.

## Etapa 09 — Actividades, categorías y colores

- Crear, editar, completar y eliminar actividades.
- Asignar categorías y colores.
- Filtrar por fecha, categoría y estado.

## Etapa 10 — Pruebas, seguridad y ejecutable

- Ejecutar las pruebas automáticas cuando se llegue a esta etapa.
- Revisar datos y credenciales.
- Preparar un `.exe` para Windows con PyInstaller.

La explicación completa de cada hito está en `docs/milestones/`. Las carpetas
de `stages/` contienen `files.txt`, donde se enumeran los archivos que el
alumno debe crear o modificar en esa etapa.
