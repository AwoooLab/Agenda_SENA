# Hito 08 — Calendario mensual

## Propósito

Mostrar un calendario mensual navegable dentro del área principal de la agenda.
En esta etapa se trabaja la vista y el cálculo de fechas; las actividades se
agregarán en el Hito 09.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/08_monthly_calendar/monthly_calendar.py
stages/08_monthly_calendar/calendar_cell.py
stages/08_monthly_calendar/test_calendar.py
stages/08_monthly_calendar/preview.html
```

## Archivo `calendar_cell.py`

Crear una celda visual para un día del mes. La celda debe:

- Mostrar el número del día.
- Ocupar una posición dentro de una cuadrícula de siete columnas.
- Poder marcarse como día actual.
- Poder marcarse como día seleccionado.
- Ejecutar una función `on_select(day)` al hacer clic.
- No mostrar todavía actividades.

Usar texto además de color para diferenciar el día actual y el seleccionado.

## Archivo `monthly_calendar.py`

Crear una clase `CalendarioMensual` que reciba un contenedor de Tkinter y una
función opcional para informar el día seleccionado.

La vista debe contener:

- Botón `‹` para ir al mes anterior.
- Texto central con el mes en español y el año.
- Botón `Hoy` para volver al mes actual.
- Botón `›` para ir al mes siguiente.
- Encabezados `Lun`, `Mar`, `Mié`, `Jue`, `Vie`, `Sáb`, `Dom`.
- Cuadrícula de siete columnas.
- Celdas vacías antes del primer día cuando sea necesario.
- Todos los días del mes correcto.

La clase debe incluir métodos equivalentes a:

```python
mostrar_mes()
mes_anterior()
mes_siguiente()
ir_a_hoy()
seleccionar_dia(dia)
```

La semana debe comenzar en lunes. El día actual debe distinguirse visualmente
con un color y el día seleccionado con otro color.

## Archivo `test_calendar.py`

Comprobar sin abrir ventanas:

- Febrero de un año bisiesto tiene 29 días.
- Febrero de un año no bisiesto tiene 28 días.
- Abril tiene 30 días.
- Enero tiene 31 días.
- Pasar de diciembre a enero aumenta el año.
- Pasar de enero a diciembre disminuye el año.
- El primer día de la semana se calcula correctamente.

## Restricciones

- Usar la biblioteca estándar.
- No consultar SQLite.
- No crear actividades.
- No usar colores como única forma de comunicar información.
- No cambiar todavía la estructura de la base de datos.

## Flujo de la clase y validación visual

`calendar_cell.py` y `monthly_calendar.py` resuelven el calendario local;
`preview.html` muestra su resultado visual. El flujo es:

1. Implementar el cálculo de días y la navegación del mes.
2. Ejecutar las pruebas y comprobar selección, mes actual y cambio de mes.
3. Actualizar `preview.html` si cambian encabezados, controles, colores o
   actividades visibles.
4. Abrir el preview y verificar la cuadrícula completa del mes.
5. Agregar en `index.html` la tarjeta de la Clase 08 con su preview.
6. Publicar y revisar la clase en GitHub Pages.

El preview no calcula fechas reales; permite comprobar la composición visual del
calendario antes de integrarlo con la aplicación.

### Validación visual específica

- Se muestran siete columnas con los días de la semana.
- El mes y los controles anterior, Hoy y siguiente son visibles.
- El día seleccionado se distingue con color y texto.
- Las actividades no desbordan la celda.

## Comprobación manual

Abrir una ventana de demostración desde `monthly_calendar.py` o desde el archivo
que indique la implementación. Comprobar que los botones cambian de mes, que
`Hoy` regresa al mes actual y que las celdas responden al clic.

Ejecutar las pruebas:

```text
python -m unittest stages/08_monthly_calendar/test_calendar.py -v
```

## Integración posterior

Integrar en:

```text
src/ui/monthly_calendar.py
src/ui/calendar_cell.py
```

Después conectar la vista con `main_window.py`.

## Instrucción para ChatGPT

```text
Genera únicamente stages/08_monthly_calendar/calendar_cell.py. Crea una celda
Tkinter para un día de calendario que muestre el número, distinga el día actual
y el seleccionado mediante color y texto, y ejecute on_select(day) al hacer
clic. No agregues actividades ni SQLite. Usa comentarios y textos en español.
Devuelve solo el código.
```

Solicitar después las funciones de fechas, `monthly_calendar.py` y
`test_calendar.py`, cada uno en una solicitud separada.

## Criterio de terminado

El calendario muestra cualquier mes correctamente, permite cambiar de mes y
seleccionar una fecha; `preview.html` representa la Clase 08 publicada.
