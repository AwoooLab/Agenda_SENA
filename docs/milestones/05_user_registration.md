# Hito 05 — Registro de usuarios

## Objetivo

Permitir que la aplicación cree usuarios locales antes de agregar el inicio de
sesión.

## Archivos

- `src/models/user.py`.
- `src/repositories/user_repository.py`.
- `src/services/user_service.py`.
- `tests/test_user_service.py`.

## Requisitos

- Nombre de usuario o correo electrónico único.
- Estado activo o inactivo.
- No guardar contraseñas en texto plano.
- Errores de validación claros.

## Integración

El repositorio gestiona las consultas a la base de datos. El servicio gestiona
las reglas. La interfaz llamará al servicio y no accederá directamente a SQL.

## Comprobación manual

Probar un registro exitoso, un usuario duplicado y campos obligatorios vacíos.

## Secuencia de solicitudes

Solicitar primero el modelo, después el repositorio, luego el servicio y
finalmente un archivo de prueba. Indicarle a ChatGPT que no modifique los
archivos anteriores.
