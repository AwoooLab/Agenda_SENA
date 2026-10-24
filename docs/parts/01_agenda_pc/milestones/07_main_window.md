# Hito 07 — Ventana principal de la agenda

## Propósito

Crear la estructura visual que verá el usuario después de iniciar sesión. En
esta etapa se construye la navegación, pero todavía no se implementa el
calendario completo ni el formulario final de actividades.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/07_main_window/app.py
stages/07_main_window/main_window.py
stages/07_main_window/navigation.py
stages/07_main_window/preview.html
```

## Archivo `navigation.py`

Crear una función o clase de navegación que muestre tres opciones:

- `Calendario`.
- `Actividades`.
- `Cerrar sesión`.

Cada opción debe recibir una función de respuesta. En esta etapa, `Calendario` y
`Actividades` pueden mostrar una etiqueta temporal que indique `Sección en
construcción`.

## Archivo `main_window.py`

Crear una ventana principal que reciba:

```python
usuario: Usuario
on_logout: Callable[[], None]
```

Diseño obligatorio:

- Título: `Agenda SENA`.
- Tamaño inicial: `900x600`.
- Barra superior con el texto `Agenda SENA`.
- Mostrar el nombre del usuario activo en la barra superior.
- Panel lateral izquierdo para la navegación.
- Área central para el contenido.
- Color principal sugerido: `#2563EB`.
- Fondo de contenido: `#F8FAFC`.

El botón `Cerrar sesión` debe cerrar la ventana principal y ejecutar `on_logout`.
No debe crear una segunda sesión ni abrir varias ventanas principales.

## Archivo `app.py`

Debe servir como demostración independiente de la etapa:

1. Crear un usuario de prueba en memoria con nombre `Estudiante`.
2. Abrir `main_window.py`.
3. Permitir probar la navegación.
4. Mostrar un mensaje de confirmación al cerrar sesión.

No debe depender todavía de SQLite ni de la pantalla de inicio de sesión.

## Restricciones

- Usar Tkinter.
- No duplicar la lógica de contraseñas.
- No implementar todavía la cuadrícula mensual.
- No guardar datos de actividades.
- No crear conexiones directas a SQLite desde la interfaz.

## Flujo de la clase y validación en GitHub Pages

`navigation.py`, `main_window.py` y `app.py` construyen la ventana principal;
`preview.html` permite revisar su composición desde GitHub Pages. Trabajar así:

1. Agregar en GitHub los archivos de la ventana principal definidos en esta
   etapa.
2. Actualizar `preview.html` con la distribución, textos e iconos.
3. Actualizar el fragmento del panel principal en `preview.html`; el visor lo
   cargará después del inicio de sesión.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Comprobar allí barra superior, menú y área de trabajo.
6. Verificar la función desde la ventana principal acumulada.

El preview no ejecuta la navegación de Tkinter; muestra el resultado visual que
debe conservarse durante la integración.

### Validación visual específica

- Se identifica el nombre de la aplicación y el usuario activo.
- El menú muestra Calendario, Actividades y Cerrar sesión.
- El área de trabajo está separada visualmente de la navegación.

## Comprobación visual en GitHub Pages

Agregar o actualizar `navigation.py`, `main_window.py`, `app.py` y
`preview.html` en GitHub. Después abrir únicamente la página principal:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se observan la barra superior, `Agenda SENA`, el usuario, el
menú, las opciones de navegación y el área de trabajo.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar la aplicación local para comprobar los
cambios de sección y el cierre de sesión. Pages solo muestra la composición
visual de la ventana principal.

## Integración después de aprobar el stage

Los archivos de `stages/07_main_window/` permanecen aislados. Después de
validar la etapa, la ventana principal y la navegación se conectan en `src/` y
se inician desde `main.py`. El módulo visual se registra en
`config/integration.json` solo después de aprobarlo.

## Instrucción para ChatGPT

```text
Genera únicamente stages/07_main_window/navigation.py para Agenda SENA. Crea
la navegación de una ventana Tkinter con las opciones Calendario, Actividades y
Cerrar sesión. Cada opción debe recibir una función de respuesta. Calendario y
Actividades deben mostrar temporalmente "Sección en construcción". Escribe los
textos y comentarios en español, no uses SQLite y devuelve solo el código.
```

Solicitar después `main_window.py` y `app.py` por separado.

## Criterio de terminado

La etapa se puede publicar cuando los archivos de la ventana principal están
en GitHub, `preview.html` muestra la distribución completa y la Clase 07
se integra en la única ventana integrada. La navegación funcional queda definida en Python y se
probará al ejecutar el proyecto en un PC.

## Alineación con las ventanas de referencia

Este hito ocupa `agenda.topbar` y `agenda.sidebar` y prepara los espacios
`agenda.summary`, `agenda.calendar`, `agenda.today`, `agenda.appointments` y
`agenda.activities`.

La ventana debe tener una barra superior, búsqueda, usuario activo, menú
lateral y un contenedor central. Las opciones del menú cambian el contenido
central; no destruyen la barra, no crean otra ventana y no muestran funciones
que todavía no tengan una vista definida.
