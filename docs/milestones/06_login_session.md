# Hito 06 — Inicio de sesión y sesión activa

## Objetivo

Autenticar a un usuario local y conservar la sesión actual en memoria.

## Archivos

- `src/security/password.py`.
- `src/services/auth_service.py`.
- `src/ui/login_window.py`.
- `tests/test_auth_service.py`.

## Requisitos

- Generar una sal diferente para cada contraseña.
- Guardar únicamente un resumen derivado de la contraseña.
- No incluir credenciales en el repositorio.
- Cerrar o limpiar la sesión al salir.

## Integración

`auth_service.py` utiliza el repositorio de usuarios y el módulo de contraseñas.
`login_window.py` llama al servicio y abre la ventana principal solo después de
un inicio de sesión correcto.

## Comprobación manual

Probar una contraseña correcta, una contraseña incorrecta, un usuario inactivo
y el cierre de sesión.

## Secuencia de solicitudes

Solicitar primero la ayuda para contraseñas, después el servicio de autenticación
y finalmente la ventana de inicio de sesión, un archivo por solicitud.
