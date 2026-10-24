# Parte 1 — Agenda local para PC

## Propósito

Construir una agenda de escritorio local para Windows usando Python y Tkinter.
Cada stage se desarrolla como módulo independiente y, después de aprobarlo,
se integra en una sola aplicación navegable.

## Stages de la parte

01 — Ventana inicial — 01_python_window
02 — Modelo de datos — 02_data_model
03 — Guardado JSON — 03_json_storage
04 — Base de datos SQLite — 04_sqlite_database
05 — Registro de usuarios — 05_user_registration
06 — Inicio de sesión — 06_login_session
07 — Ventana principal — 07_main_window
08 — Calendario mensual — 08_monthly_calendar
09 — Actividades, categorías y colores — 09_events_categories_colors
10 — Pruebas y ejecutable — 10_tests_security_executable

Las especificaciones detalladas están en docs/parts/01_agenda_pc/milestones/.

## Flujo de la parte

1. El estudiante lee la especificación y el files.txt del stage.
2. Trabaja únicamente dentro de la carpeta del stage.
3. Ejecuta y valida el módulo de forma independiente.
4. Actualiza su preview.html.
5. La integración revisada se conecta posteriormente en src/ o main.py.
6. Se registra el módulo aprobado en config/integration.json.
7. La aplicación integrada se comprueba desde la única página de GitHub Pages.

## Resultado

La aplicación integrada tendrá una sola ventana con navegación interna. El
visor no muestra stages futuros ni usa la existencia de una carpeta como señal
de que una función ya está terminada.

La metodología de independencia, contrato y acumulación está definida en
docs/stage_contract.md.
