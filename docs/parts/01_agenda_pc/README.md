# Parte 1 — Agenda local para PC

## Propósito

Construir progresivamente una agenda de escritorio local para Windows usando
Python y Tkinter. Esta primera parte establece la base del proyecto: ventana,
modelo de datos, almacenamiento, usuarios, inicio de sesión, calendario,
actividades, pruebas y preparación del ejecutable.

## Alcance

La Parte 1 contiene diez hitos. Cada hito tiene una especificación detallada y
una carpeta equivalente dentro de `stages/`.

| Hito | Tema | Stage | Especificación |
|---|---|---|---|
| 01 | Ventana inicial | `01_python_window` | [Abrir](milestones/01_python_window.md) |
| 02 | Modelo de datos | `02_data_model` | [Abrir](milestones/02_data_model.md) |
| 03 | Guardado JSON | `03_json_storage` | [Abrir](milestones/03_json_storage.md) |
| 04 | Base de datos SQLite | `04_sqlite_database` | [Abrir](milestones/04_sqlite_database.md) |
| 05 | Registro de usuarios | `05_user_registration` | [Abrir](milestones/05_user_registration.md) |
| 06 | Inicio de sesión | `06_login_session` | [Abrir](milestones/06_login_session.md) |
| 07 | Ventana principal | `07_main_window` | [Abrir](milestones/07_main_window.md) |
| 08 | Calendario mensual | `08_monthly_calendar` | [Abrir](milestones/08_monthly_calendar.md) |
| 09 | Actividades y categorías | `09_events_categories_colors` | [Abrir](milestones/09_events_categories_colors.md) |
| 10 | Pruebas y ejecutable | `10_tests_security_executable` | [Abrir](milestones/10_tests_security_executable.md) |

## Flujo de trabajo de la parte

1. Leer la especificación del hito.
2. Trabajar únicamente en los archivos de su carpeta dentro de `stages/`.
3. Consultar el `files.txt` correspondiente para estudiar cada archivo.
4. Actualizar el `preview.html` del stage para comprobar visualmente el avance.
5. Mantener y actualizar la tarjeta del hito en el `index.html` de la raíz.
6. Revisar el resultado desde la página principal de GitHub Pages.
7. Integrar la funcionalidad aprobada progresivamente en `main.py`.

El `index.html` de la raíz es el único visor. Cada `preview.html` se incrusta
como un componente visual dentro de su tarjeta; no se presenta como una página
independiente para navegar entre etapas.

## Regla de integración

Los archivos de `stages/` son ejercicios aislados y no se importan
automáticamente. El resultado funcional de la Parte 1 se reúne progresivamente
en el `main.py` de la raíz. El resultado visual se reúne en el `index.html` de
la raíz.

## Estado

- [x] Hitos documentados.
- [x] Stages preparados.
- [ ] Implementación de los archivos por parte del estudiante.
- [ ] Integración completa en `main.py`.
- [ ] Preparación del ejecutable de Windows.
