# Hito 09 — Actividades, categorías y colores

## Objetivo

Gestionar actividades en el calendario y distinguir visualmente sus categorías.

## Archivos

- `src/models/event.py`.
- `src/models/category.py`.
- `src/services/event_service.py`.
- `src/ui/event_form.py`.
- `src/ui/color_legend.py`.
- `tests/test_event_service.py`.

## Requisitos

- Crear, editar, eliminar y completar una actividad.
- Asignar una categoría y un color.
- Usar texto e iconos además del color para facilitar la accesibilidad.
- Filtrar actividades por fecha, categoría y estado.

## Integración

`event_service.py` conecta los modelos, la base de datos y las reglas. El
formulario llama al servicio. El calendario se actualiza después de un cambio
exitoso.

## Comprobación manual

Crear una actividad, editarla, mostrarla en el día seleccionado, completarla y
eliminarla.

## Secuencia de solicitudes

Solicitar un modelo o servicio a la vez. No pedirle a ChatGPT que rediseñe toda
la interfaz mientras se implementa una sola función.
