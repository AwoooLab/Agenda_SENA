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
stages/04_sqlite_database/preview.html
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

## Flujo de la clase y validación en GitHub Pages

Esta clase tiene una parte técnica (`schema.sql`, `database.py` y sus pruebas)
y una parte visual (`preview.html`). El flujo es:

1. Agregar en GitHub `schema.sql`, `database.py`, sus pruebas y los archivos
   previstos para la etapa.
2. Actualizar `preview.html` para mostrar la estructura de la base.
3. Actualizar `preview.html` con la estructura de la base. El visor principal
   la mostrará junto con las funciones anteriores.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Comparar allí las tablas visuales con `schema.sql`.
6. Verificar la función desde la ventana principal acumulada.

El preview no consulta SQLite. Su función es hacer visible el diseño de la
base de datos para revisar si la estructura se entiende.

### Validación visual específica

- Se muestran las tablas `users` y `events`.
- Los campos y tipos visibles coinciden con `schema.sql`.
- La relación entre usuario y actividad se puede explicar a partir de los
  campos mostrados.

## Comprobación visual en GitHub Pages

Agregar o actualizar `schema.sql`, `database.py`, `test_database.py` y
`preview.html` en GitHub. Después abrir únicamente la página principal:

```text
https://awooolab.github.io/Agenda_SENA/
```

Comparar las tablas, campos y tipos mostrados con el esquema que se está
construyendo. El resultado visible de esta clase es la explicación visual de la
base de datos.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar las pruebas de SQLite. GitHub Pages no crea
ni consulta la base de datos; solo muestra su estructura.

## Integración progresiva en `main.py`

Después de terminar la etapa, incorporar en `main.py` la conexión, el esquema y
las operaciones que la aplicación integrada necesite. Los archivos de
`stages/04_sqlite_database/` permanecen aislados y no se importan
automáticamente.

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

La etapa se puede publicar cuando el esquema, el código, las pruebas y
`preview.html` están en GitHub, y la Clase 04 muestra claramente las tablas en
la ventana acumulada. La creación y consulta de SQLite queda definida en Python y se
probará al ejecutar el proyecto en un PC.
