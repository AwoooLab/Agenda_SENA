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

## Comprobación manual

Ejecutar:

```text
python stages/07_main_window/app.py
```

Comprobar que:

1. Aparece la ventana de 900x600.
2. Se muestra `Agenda SENA`.
3. Se muestra el usuario `Estudiante`.
4. Los botones de navegación cambian el contenido central.
5. `Cerrar sesión` ejecuta la función de salida.

## Integración posterior

Integrar en:

```text
src/ui/main_window.py
src/ui/navigation.py
app.py
```

La aplicación integrada recibirá el usuario real desde `login_window.py`.

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

El usuario puede abrir la ventana principal, identificar su sesión, cambiar
entre las secciones temporales y cerrar sesión.
