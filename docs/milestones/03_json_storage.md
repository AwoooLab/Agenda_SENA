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

Debe demostrar el funcionamiento de `storage.py` sin modificar el archivo real
`data/agenda.json`.

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

## Flujo de la clase y validación visual

`storage.py` y `demo.py` comprueban el guardado local, mientras que
`preview.html` muestra ese flujo de manera visual. Trabajar en este orden:

1. Implementar `storage.py` y comprobar guardar/cargar con `demo.py`.
2. Confirmar que el resultado conserva los mismos datos.
3. Actualizar `preview.html` para representar el archivo JSON y sus acciones.
4. Abrir el preview y comprobar que se distinguen archivo, estado, Guardar y
   Cargar.
5. Agregar en `index.html` la tarjeta de la Clase 03 con su preview.
6. Publicar y revisar el resultado desde GitHub Pages.

El preview es una representación visual; no guarda datos reales ni sustituye
la comprobación del archivo JSON temporal.

### Validación visual específica

- Se identifica claramente `agenda.json` como archivo local.
- Se distinguen los estados de guardado y carga.
- La estructura mostrada corresponde a los campos de la agenda.

## Comprobación manual

Ejecutar desde la carpeta de la etapa:

```text
python stages/03_json_storage/demo.py
```

Debe mostrarse la misma información que se guardó. Después de la ejecución no
debe quedar una carpeta temporal creada por el ejercicio.

## Integración posterior

La función se trasladará a:

```text
src/storage.py
```

El archivo real de datos será:

```text
data/agenda.json
```

Más adelante, SQLite reemplazará este almacenamiento como mecanismo principal.

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
resultado y no modifica data/agenda.json. Devuelve solo el código.
```

## Criterio de terminado

El alumno puede guardar y cargar los mismos datos, y `preview.html` explica
visualmente ese resultado dentro de la Clase 03 publicada.
