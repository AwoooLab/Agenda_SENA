# Hito 10 — Pruebas, seguridad y ejecutable

## Objetivo

Estabilizar la aplicación y preparar un ejecutable para Windows.

## Archivos

- `tests/test_database.py`.
- `tests/test_auth_service.py`.
- `tests/test_event_service.py`.
- `scripts/build_windows.ps1`.
- `docs/release.md`.

## Requisitos

- Las pruebas deben funcionar sin internet.
- Las pruebas de base de datos deben usar datos temporales.
- Las credenciales nunca deben subirse al repositorio.
- El script de compilación debe crear la salida en `dist/`.
- El ejecutable debe probarse en una cuenta limpia de Windows.

## Integración

Empaquetar la aplicación únicamente después de terminar las pruebas. Mantener
los archivos generados fuera de las carpetas de código y documentar los pasos de
la entrega.

## Comprobación manual

```text
python -m unittest discover -s tests -v
```

Después, crear y abrir el ejecutable en Windows.

## Secuencia de solicitudes

Solicitar una prueba o un script de compilación a la vez. Revisar cada comando
generado antes de ejecutarlo.
