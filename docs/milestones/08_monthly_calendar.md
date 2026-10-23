# Hito 08 — Calendario mensual

## Objetivo

Mostrar un calendario mensual navegable con una cuadrícula clara de días.

## Archivos

- `src/ui/monthly_calendar.py`.
- `src/ui/calendar_cell.py`.
- `tests/test_calendar.py`.

## Requisitos

- Controles para ir al mes anterior y al mes siguiente.
- Botón para regresar al mes actual.
- Cantidad correcta de días para cada mes.
- Resaltar el día actual.
- Usar una distribución legible para el tamaño de ventana definido.

## Integración

El calendario recibe el usuario actual y las actividades desde la capa de
servicios. No debe consultar SQLite directamente.

## Comprobación manual

Probar febrero en años bisiestos y no bisiestos, cambios de mes y selección de
un día.

## Secuencia de solicitudes

Solicitar primero las funciones de cálculo de fechas, después la celda del
calendario y finalmente la vista completa del calendario.
