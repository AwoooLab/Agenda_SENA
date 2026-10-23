# Hito 02 — Modelo de datos

## Objetivo

Representar una actividad de la agenda como un objeto de Python.

## Archivos

- `stages/02_data_model/model.py`.
- `src/model.py`.
- `tests/test_model.py`.

## Requisitos

El primer modelo puede llamarse `Event` o `Cita` y debe contener título, fecha,
hora de inicio, hora de finalización y descripción. Usar `dataclass`, conversión
a diccionario y reconstrucción desde un diccionario.

## Integración

El modelo no debe abrir ventanas ni leer archivos. Más adelante, los módulos de
base de datos e interfaz lo importarán.

## Comprobación manual

Crear un objeto, convertirlo a diccionario y ejecutar:

```text
python -m unittest discover -s tests -v
```

## Secuencia de solicitudes

Solicitar únicamente `model.py`. Pedir Python estándar, campos con tipos y un
ejemplo pequeño dentro de `if __name__ == "__main__"`.
