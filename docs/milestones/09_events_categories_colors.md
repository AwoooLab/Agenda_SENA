# Hito 09 — Actividades, categorías y colores

## Propósito

Permitir crear y administrar las actividades que aparecen en el calendario.
Cada actividad tendrá una categoría, un color y un estado de cumplimiento.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/09_events_categories_colors/event.py
stages/09_events_categories_colors/category.py
stages/09_events_categories_colors/event_service.py
stages/09_events_categories_colors/event_form.py
stages/09_events_categories_colors/color_legend.py
stages/09_events_categories_colors/test_event_service.py
stages/09_events_categories_colors/preview.html
```

## Archivo `event.py`

Definir una `dataclass` llamada `Evento` con estos campos:

- `id: int | None`.
- `user_id: int`.
- `titulo: str`.
- `fecha: str` en formato `AAAA-MM-DD`.
- `hora_inicio: str` en formato `HH:MM`.
- `hora_fin: str` en formato `HH:MM`.
- `descripcion: str`.
- `categoria_id: int`.
- `completado: bool`.

El título, la fecha, la hora inicial y la hora final son obligatorios.

## Archivo `category.py`

Definir una `dataclass` llamada `Categoria` con:

- `id: int`.
- `nombre: str`.
- `color: str` en formato hexadecimal.

Crear también estas categorías iniciales:

| Nombre | Color |
|---|---|
| Trabajo | `#2563EB` |
| Personal | `#16A34A` |
| Estudio | `#F59E0B` |
| Salud | `#DC2626` |

## Archivo `event_service.py`

Crear una clase `ServicioEventos` con métodos para:

```python
crear(evento: Evento) -> Evento
editar(evento: Evento) -> Evento
eliminar(evento_id: int) -> None
completar(evento_id: int) -> None
listar_por_fecha(fecha: str) -> list[Evento]
filtrar(fecha: str | None, categoria_id: int | None, completado: bool | None) -> list[Evento]
```

Reglas obligatorias:

- Rechazar títulos vacíos.
- Rechazar fechas con formato incorrecto.
- Rechazar horas con formato incorrecto.
- Rechazar una hora final anterior o igual a la hora inicial.
- Guardar la actividad relacionada con un usuario.
- Permitir marcar una actividad como completada.
- Permitir eliminar una actividad.
- Usar consultas parametrizadas mediante el repositorio o la conexión recibida.

## Archivo `event_form.py`

Crear un formulario Tkinter con estos controles, en este orden:

1. Campo `Título`.
2. Campo `Fecha (AAAA-MM-DD)`.
3. Campo `Hora inicial (HH:MM)`.
4. Campo `Hora final (HH:MM)`.
5. Campo `Descripción`.
6. Lista `Categoría`.
7. Botón `Guardar`.
8. Botón `Cancelar`.

El formulario debe mostrar los errores en español sin cerrar la ventana. Al
guardar correctamente debe ejecutar una función `on_saved(evento)`. Al cancelar
debe ejecutar `on_cancel()`.

## Archivo `color_legend.py`

Mostrar una leyenda con el nombre de cada categoría, un indicador de color y el
texto de la categoría. No depender únicamente del color: siempre mostrar el
nombre escrito.

## Archivo `test_event_service.py`

Comprobar:

- Crear una actividad válida.
- Rechazar un título vacío.
- Rechazar una fecha inválida.
- Rechazar una hora inválida.
- Rechazar una hora final anterior o igual a la inicial.
- Editar una actividad.
- Listar por fecha.
- Filtrar por categoría.
- Marcar como completada.
- Eliminar una actividad.

## Restricciones

- No colocar consultas SQL dentro de `event_form.py`.
- No eliminar usuarios al eliminar actividades.
- No usar colores sin texto.
- No agregar pagos, internet, notificaciones externas ni sincronización.
- No crear todavía un ejecutable.

## Flujo de la clase y validación en GitHub Pages

Los modelos, el servicio y los controles de actividades se implementan en
Python; `preview.html` muestra el formulario y sus estados. Sigue este orden:

1. Agregar en GitHub los modelos, servicio, formulario y leyenda definidos en
   esta etapa.
2. Actualizar `preview.html` con nuevos campos, categorías, iconos o colores.
3. Agregar en `index.html` la tarjeta de la Clase 09 con su preview.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Revisar allí formulario, actividad del día y leyenda.
6. Verificar la clase desde la colección principal.

El preview no crea actividades reales; permite validar que la interfaz comunica
las mismas reglas que el servicio Python.

### Validación visual específica

- Se distinguen título, fecha, hora y categoría.
- La actividad guardada se muestra en la sección del día.
- La leyenda permite relacionar cada categoría con su color.
- Los nuevos iconos o controles se reflejan también en el preview.

## Comprobación visual en GitHub Pages

Agregar o actualizar los archivos de actividades y `preview.html` en GitHub.
Después agregar la tarjeta de la Clase 09 en `index.html` y abrir únicamente:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se observan el formulario, las categorías, los colores, la
actividad del día, los botones y los iconos definidos para esta clase.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar las operaciones de crear, editar, completar,
filtrar y eliminar. Pages solo muestra el resultado visual; no modifica datos.

## Integración progresiva en `main.py`

Después de terminar la etapa, incorporar progresivamente en `main.py` los
modelos, las operaciones, el formulario y la leyenda de colores. Los archivos
de `stages/09_events_categories_colors/` permanecen aislados y la conexión con
el calendario se coordina desde `main.py`.

## Instrucción para ChatGPT

```text
Genera únicamente stages/09_events_categories_colors/event.py. Define la
dataclass Evento con los campos y tipos exactos de la especificación del Hito
09. Incluye validaciones simples de estructura, pero no uses Tkinter ni SQLite
en el modelo. Escribe los comentarios en español y devuelve solo el código.
```

Solicitar cada modelo, servicio, formulario, leyenda y prueba por separado.

## Criterio de terminado

La etapa se puede publicar cuando los archivos de actividades están en GitHub,
`preview.html` representa formulario, categorías y colores, y la Clase 09
aparece en la colección. Las operaciones funcionales quedan definidas en
Python y se probarán al ejecutar el proyecto en un PC.
