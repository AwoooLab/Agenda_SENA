# Hito 04 — Base de datos SQLite

## Objetivo

Reemplazar el almacenamiento temporal en JSON por SQLite, que es apropiado para
usuarios, inicio de sesión y registros relacionados con el calendario.

## Archivos

- `src/database.py`: conexión y operaciones de la base de datos.
- `src/schema.sql`: definición de tablas.
- `data/agenda.db`: base de datos local generada.
- `tests/test_database.py`: pruebas de base de datos usando un archivo temporal.

## Requisitos

- Usar el módulo incorporado `sqlite3` de Python.
- Crear las tablas automáticamente en el primer inicio.
- Usar consultas con parámetros.
- No guardar contraseñas en esta etapa.

## Integración

Los servicios usarán `database.py`; la interfaz no debe contener consultas SQL
directamente. Mantener JSON únicamente como formato opcional de exportación.

## Comprobación manual

Crear una base de datos temporal, crear una tabla, insertar un registro, leerlo y
eliminar el archivo temporal después de la prueba.

## Secuencia de solicitudes

Solicitar `schema.sql`, revisar el diseño de las tablas, después solicitar
`database.py` y finalmente `test_database.py`.
