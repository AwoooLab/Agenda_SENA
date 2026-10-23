# Hito 03 — Guardado local temporal en JSON

## Propósito

Aprender a guardar y cargar datos de la agenda en un archivo local antes de
utilizar una base de datos.

## Archivos que debe crear el alumno

Crear únicamente estos dos archivos:

```text
stages/03_json_storage/storage.py
stages/03_json_storage/demo.py
stages/03_json_storage/preview.html
```

## Archivo `storage.py`

Debe contener exactamente dos funciones principales:

```python
def guardar(datos: list[dict], ruta: Path) -> None:
    ...


def cargar(ruta: Path) -> list[dict]:
    ...
```

### Reglas de `guardar`

- Recibir una lista de diccionarios.
- Recibir la ruta como un objeto `Path`.
- Crear las carpetas superiores si todavía no existen.
- Guardar usando UTF-8.
- Usar `json.dumps` con `indent=2` y `ensure_ascii=False`.
- Sobrescribir el archivo si ya existe.
- No abrir ventanas.

### Reglas de `cargar`

- Recibir una ruta como objeto `Path`.
- Si el archivo no existe, devolver `[]`.
- Si existe, leerlo con UTF-8.
- Convertir el contenido JSON a una lista de diccionarios.
- Si el contenido no es una lista, mostrar un error claro mediante
  `ValueError`.

## Archivo `demo.py`

Debe demostrar el funcionamiento de `storage.py` sin modificar datos
permanentes del proyecto.

El ejemplo debe:

1. Crear una carpeta temporal con `tempfile.TemporaryDirectory`.
2. Crear dentro de ella un archivo `agenda.json`.
3. Guardar una lista con una cita de ejemplo.
4. Cargar nuevamente la información.
5. Imprimir el resultado cargado.
6. Finalizar y eliminar la carpeta temporal automáticamente.

La cita de ejemplo debe tener título, fecha, hora y descripción.

## Restricciones

- Usar únicamente `json`, `pathlib` y módulos estándar relacionados con archivos
  temporales.
- No usar Tkinter.
- No usar SQLite.
- No conectarse a internet.
- No crear todavía usuarios ni inicio de sesión.

## Flujo de la clase y validación en GitHub Pages

`storage.py` y `demo.py` comprueban el guardado local, mientras que
`preview.html` muestra ese flujo de manera visual. Trabajar en este orden:

1. Agregar en GitHub `storage.py`, `demo.py` y los archivos previstos.
2. Actualizar `preview.html` para representar el archivo JSON y sus acciones.
3. Actualizar el fragmento de guardado en `preview.html`; el visor lo cargará
   después del formulario y la tabla.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Comprobar allí que se distinguen archivo, estado, Guardar y Cargar.
6. Verificar la función desde la ventana principal acumulada.

El preview es una representación visual; no guarda datos reales ni sustituye
la comprobación del archivo JSON temporal.

### Validación visual específica

- Se identifica claramente `agenda.json` como archivo local.
- Se distinguen los estados de guardado y carga.
- La estructura mostrada corresponde a los campos de la agenda.

## Comprobación visual en GitHub Pages

Agregar o actualizar `storage.py`, `demo.py` y `preview.html` en GitHub. Después
abrir únicamente la página principal, que carga todos los fragmentos en orden:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se identifican `agenda.json`, los datos de ejemplo y los estados
`Guardar` y `Cargar`. Si cambia la estructura JSON, actualizar también la vista.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar `demo.py` y comprobar que los datos cargados
son iguales a los guardados. GitHub Pages no ejecuta el almacenamiento real.

## Integración progresiva en `main.py`

Después de terminar la etapa, incorporar las funciones de guardado y carga en:

```text
main.py
```

Los archivos de `stages/03_json_storage/` permanecen aislados. `main.py` irá
reuniendo la lógica que la aplicación necesita en cada hito posterior.

## Instrucción para ChatGPT

```text
Genera primero stages/03_json_storage/storage.py con las funciones guardar y
cargar. guardar recibe list[dict] y Path, crea las carpetas superiores, usa
UTF-8, indent=2 y ensure_ascii=False. cargar devuelve [] si no existe el
archivo y lanza ValueError si el JSON no contiene una lista. No uses Tkinter ni
SQLite. Devuelve solo ese archivo.
```

Después pedir `demo.py` por separado:

```text
Genera únicamente stages/03_json_storage/demo.py. Importa guardar y cargar del
archivo storage.py de la misma carpeta, usa TemporaryDirectory, guarda una
lista de citas en un agenda.json temporal, vuelve a cargarla, imprime el
resultado y no modifica archivos permanentes del proyecto. Devuelve solo el
código.
```

## Criterio de terminado

La etapa se puede publicar cuando los archivos de JSON están en GitHub,
`preview.html` explica visualmente el flujo y la Clase 03 se integra en la
ventana acumulada. Guardar y cargar los datos queda definido en Python y se probará al
ejecutar el proyecto en un PC.
