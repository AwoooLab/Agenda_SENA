# Hito 03 — Guardado local temporal en JSON

## Propósito

Aprender a guardar y cargar datos de la agenda en un archivo local antes de
utilizar una base de datos.

## Archivos que debe crear el alumno

Crear únicamente estos dos archivos:

```text
stages/03_json_storage/storage.py
stages/03_json_storage/demo.py
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

El alumno puede guardar una lista, cargarla nuevamente y obtener exactamente los
mismos datos sin usar la interfaz ni una base de datos.
