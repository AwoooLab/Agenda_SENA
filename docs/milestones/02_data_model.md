# Hito 02 — Modelo de datos de una cita

## Propósito

Crear el objeto que representa una cita o actividad de la agenda. Este objeto se
usará después para guardar información y mostrarla en el calendario.

## Archivo que debe crear el alumno

Crear únicamente:

```text
stages/02_data_model/model.py
stages/02_data_model/preview.html
```

## Resultado esperado

El archivo debe definir una clase `Cita` usando `dataclass`. Una cita representa
una actividad sencilla de la agenda.

## Estructura obligatoria de `Cita`

La clase debe tener estos campos, en este orden:

| Campo | Tipo | Obligatorio | Valor inicial |
|---|---|---|---|
| `titulo` | `str` | Sí | No tiene valor inicial |
| `fecha` | `str` | Sí | No tiene valor inicial |
| `hora` | `str` | Sí | No tiene valor inicial |
| `descripcion` | `str` | No | `""` |

La fecha debe manejarse inicialmente como texto con formato `AAAA-MM-DD` y la
hora como texto con formato `HH:MM`.

## Métodos obligatorios

La clase debe incluir:

```python
def a_diccionario(self) -> dict:
    ...
```

Este método debe devolver las claves `titulo`, `fecha`, `hora` y `descripcion`.

También debe incluir:

```python
@classmethod
def desde_diccionario(cls, datos: dict) -> "Cita":
    ...
```

Este método debe reconstruir una `Cita` desde un diccionario. Si no existe la
clave `descripcion`, debe usar una cadena vacía.

## Ejemplo obligatorio

Dentro de `if __name__ == "__main__"`, crear una cita de ejemplo y mostrar su
diccionario. Usar estos datos:

```text
Título: Clase de Python
Fecha: 2026-10-23
Hora: 18:00
Descripción: Practicar dataclasses
```

## Restricciones

- Usar únicamente la biblioteca estándar de Python.
- Importar `dataclass` y `asdict` desde `dataclasses`.
- No abrir ventanas.
- No leer ni escribir archivos.
- No importar Tkinter, SQLite ni módulos de `src/`.
- No agregar campos de usuario, categoría o color todavía.

## Flujo de la clase y validación visual

La clase se desarrolla en dos partes coordinadas: `model.py` define la cita y
`preview.html` muestra cómo se presenta una cita en la agenda. Sigue este
flujo:

1. Revisar la estructura y los métodos obligatorios de `Cita`.
2. Ejecutar el ejemplo de `model.py` y comprobar la conversión a diccionario.
3. Actualizar `preview.html` si cambian los campos o su presentación.
4. Abrir el preview y verificar título, fecha, hora, descripción y estado.
5. Agregar en `index.html` la tarjeta de la Clase 02 con el enlace al
   `preview.html`.
6. Publicar y verificar la tarjeta en GitHub Pages.

El preview no ejecuta la clase Python: funciona como comprobación visual de la
estructura que luego usará la interfaz.

### Validación visual específica

- La tarjeta muestra título, fecha, hora y descripción.
- Los nombres visibles corresponden a los atributos de `Cita`.
- El estado de la cita se distingue sin alterar el contenido del modelo.

## Comprobación manual

Ejecutar:

```text
python stages/02_data_model/model.py
```

Debe imprimirse un diccionario con las cuatro claves de la cita.

También se debe comprobar mentalmente que esto funciona:

```python
cita = Cita("Clase", "2026-10-23", "18:00")
datos = cita.a_diccionario()
otra_cita = Cita.desde_diccionario(datos)
```

`cita` y `otra_cita` deben tener los mismos datos.

## Integración posterior

Después de terminar la etapa, trasladar la clase a:

```text
src/model.py
```

En la integración se podrá agregar una prueba en `tests/test_model.py` sin
modificar el ejercicio original de `stages/`.

## Instrucción para ChatGPT

```text
Genera únicamente stages/02_data_model/model.py. Define una dataclass llamada
Cita con los campos titulo: str, fecha: str, hora: str y descripcion: str = "".
Agrega a_diccionario() usando asdict y la clase desde_diccionario() que
reconstruya una Cita y use una cadena vacía si falta descripcion. Incluye un
ejemplo dentro de if __name__ == "__main__" usando Clase de Python,
2026-10-23, 18:00 y Practicar dataclasses. No uses interfaz, archivos, SQLite
ni otros módulos. Devuelve únicamente el código.
```

## Criterio de terminado

El hito está terminado cuando `Cita` puede convertirse a diccionario y volver a
crearse sin perder información, y `preview.html` muestra los mismos datos de
forma clara dentro de la Clase 02 publicada.
