# Hito 07 — Ventana principal

## Objetivo

Crear la estructura principal de la aplicación autenticada, donde funcionarán el
calendario y las vistas de actividades.

## Archivos

- `stages/07_main_window/app.py`.
- `src/ui/main_window.py`.
- `src/ui/navigation.py`.
- `app.py`.

## Requisitos

- Mostrar el usuario que inició sesión.
- Permitir navegar al calendario, a las actividades y a la salida.
- Mantener cada pantalla en su propio módulo.
- No duplicar la lógica de autenticación.

## Integración

La ventana de inicio de sesión abre `main_window.py` con el usuario autenticado.
El archivo principal `app.py` inicia el flujo de la aplicación.

## Comprobación manual

Iniciar sesión con un usuario de prueba, comprobar que se muestre su nombre y
confirmar que al salir se regrese a la ventana de inicio de sesión.

## Secuencia de solicitudes

Solicitar primero `navigation.py`, después `main_window.py` y luego adaptar el
archivo principal.
