# Hito 04 — Base de datos local SQLite

## Propósito

Reemplazar el almacenamiento temporal en JSON por una base de datos SQLite local
que pueda guardar usuarios y actividades de la agenda.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/04_sqlite_database/database.py
stages/04_sqlite_database/schema.sql
stages/04_sqlite_database/test_database.py
```

## Archivo `schema.sql`

Debe crear dos tablas: `users` y `events`.

### Tabla `users`

Debe tener estas columnas:

- `id`: entero, clave primaria autoincremental.
- `username`: texto, obligatorio y único.
- `email`: texto, obligatorio y único.
- `password_hash`: texto, puede estar vacío al inicio.
- `password_salt`: texto, puede estar vacío al inicio.
- `is_active`: entero, obligatorio, valor predeterminado `1`.
- `created_at`: texto, obligatorio.

### Tabla `events`

Debe tener estas columnas:

- `id`: entero, clave primaria autoincremental.
- `user_id`: entero, obligatorio y relacionado con `users.id`.
- `title`: texto, obligatorio.
- `event_date`: texto, obligatorio con formato `AAAA-MM-DD`.
- `start_time`: texto, obligatorio con formato `HH:MM`.
- `end_time`: texto, obligatorio con formato `HH:MM`.
- `description`: texto, opcional.
- `category`: texto, obligatorio.
- `color`: texto, obligatorio.
- `is_completed`: entero, obligatorio, valor predeterminado `0`.

Activar las claves foráneas de SQLite desde `database.py`. No guardar nunca una
contraseña sin convertirla previamente en un resumen seguro.

## Archivo `database.py`

Debe incluir estas funciones:

```python
def conectar(ruta: Path) -> sqlite3.Connection:
    ...


def inicializar(conexion: sqlite3.Connection, ruta_schema: Path) -> None:
    ...
```

`conectar` debe crear las carpetas superiores, abrir la base de datos, activar
las claves foráneas y configurar `sqlite3.Row` como fábrica de filas.

`inicializar` debe leer `schema.sql` en UTF-8 y ejecutar todas sus instrucciones.

## Archivo `test_database.py`

Debe usar `unittest` y una base de datos temporal. La prueba debe:

1. Crear una ruta temporal.
2. Abrir una conexión.
3. Ejecutar el esquema.
4. Insertar un usuario.
5. Insertar una actividad relacionada con ese usuario.
6. Leer ambos registros.
7. Comprobar que los datos existen.
8. Cerrar la conexión.

## Restricciones

- Usar únicamente el módulo incorporado `sqlite3`.
- No crear ventanas.
- No crear servicios de usuario.
- No implementar todavía inicio de sesión.
- No incluir contraseñas reales en el archivo de prueba.

## Comprobación manual

Ejecutar:

```text
python -m unittest stages/04_sqlite_database/test_database.py -v
```

La prueba debe terminar sin errores y no debe dejar una base de datos temporal
en la carpeta del proyecto.

## Integración posterior

Integrar la lógica en:

```text
src/database.py
src/schema.sql
data/agenda.db
```

El archivo `data/agenda.db` será generado por la aplicación y no se creará a
mano dentro de `stages/`.

## Instrucción para ChatGPT

```text
Genera únicamente stages/04_sqlite_database/schema.sql. Crea las tablas users y
events con las columnas especificadas en la documentación de este hito, claves
primarias, restricciones NOT NULL, valores predeterminados y relación
events.user_id con users.id. No agregues datos de ejemplo ni comentarios en
inglés. Devuelve solo el SQL.
```

Después solicitar `database.py` y `test_database.py` por separado, indicando
que deben usar una base de datos temporal y no modificar la base real.

## Criterio de terminado

El alumno puede crear la base, crear las tablas, insertar un usuario y una
actividad relacionada, leerlos y cerrar la conexión correctamente.
