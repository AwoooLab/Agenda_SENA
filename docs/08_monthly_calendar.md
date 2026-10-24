# Hito 08 — Calendario mensual

## Propósito

Mostrar un calendario mensual navegable dentro del área principal de la agenda.
En esta etapa se trabaja la vista y el cálculo de fechas; las actividades se
agregarán en el Hito 09.

## Metodología de integración vigente

El estudiante trabaja únicamente en `stages/08_monthly_calendar/`. El
calendario, sus celdas y sus pruebas se desarrollan de forma independiente;
`preview.html` muestra la cuadrícula y sus controles en el espacio
`agenda.calendar`. La revisión se realiza desde
`https://awooolab.github.io/Agenda_SENA/`, que es el único visor del proyecto.

Al aprobar el hito, el calendario se conecta al área central de la aplicación
desde `src/` y `main.py`. Las actividades del Hito 09 se incorporarán después
en las mismas celdas, sin crear una nueva ventana.

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

## Flujo de la clase y validación en GitHub Pages

`calendar_cell.py` y `monthly_calendar.py` resuelven el calendario local;
`preview.html` muestra su resultado visual. El flujo es:

1. Agregar en GitHub los archivos del calendario definidos en esta etapa.
2. Actualizar `preview.html` si cambian encabezados, controles, colores o
   actividades visibles.
3. Actualizar el fragmento del calendario en `preview.html`; el visor lo
   cargará junto con el panel y las funciones anteriores.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Verificar allí la cuadrícula completa del mes.
6. Revisar la función desde la ventana principal acumulada.

El preview no calcula fechas reales; permite comprobar la composición visual del
calendario antes de integrarlo con la aplicación.

### Validación visual específica

- Se muestran siete columnas con los días de la semana.
- El mes y los controles anterior, Hoy y siguiente son visibles.
- El día seleccionado se distingue con color y texto.
- Las actividades no desbordan la celda.

## Comprobación visual en GitHub Pages

Agregar o actualizar los archivos del calendario y `preview.html` en GitHub.
Después abrir únicamente la página principal:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se observan el mes, los controles, las siete columnas, el día
resaltado y la actividad visible.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar las pruebas y comprobar navegación y
selección. GitHub Pages no calcula fechas ni ejecuta Tkinter.

## Integración después de aprobar el stage

Los archivos de `stages/08_monthly_calendar/` permanecen aislados. Después de
validar la etapa, el calendario mensual y sus celdas se conectan en `src/` y se
coordinan desde `main.py`. El módulo visual se registra en
`config/integration.json` solo después de aprobarlo.

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

La etapa se puede publicar cuando los archivos del calendario están en GitHub,
`preview.html` muestra la cuadrícula y la Clase 08 se integra en la única ventana integrada. El
cálculo, la navegación y la selección quedan definidos en Python y se probarán
al ejecutar el proyecto en un PC.

## Alineación con las ventanas de referencia

El componente ocupa `agenda.calendar` dentro del contenido central de la
agenda. Debe mostrar encabezado del mes, botones anterior y siguiente, acción
`Hoy`, siete columnas de lunes a domingo, celdas de día, día seleccionado y
marcas de actividades.

El calendario recibe datos de prueba sin depender de otro stage. El preview
debe conservar la barra superior, el menú y el espacio de calendario, aunque
las citas reales se conecten después de aprobar el módulo.
