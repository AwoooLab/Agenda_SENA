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
- No importar Tkinter, SQLite ni archivos de otras etapas o de `main.py`.
- No agregar campos de usuario, categoría o color todavía.

## Flujo de la clase y validación en GitHub Pages

La clase se desarrolla en dos partes coordinadas: `model.py` define la cita y
`preview.html` muestra cómo se presenta una cita en la agenda. Sigue este
flujo:

1. Revisar la estructura y los métodos obligatorios de `Cita`.
2. Agregar en GitHub `model.py` y los archivos previstos para la etapa.
3. Actualizar `preview.html` si cambian los campos o su presentación.
4. Actualizar el fragmento de la cita en `preview.html`. El visor principal
   solo lo mostrará cuando esta etapa sea aprobada y registrada en la
   configuración de integración.
5. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
6. Verificar allí título, fecha, hora, descripción y estado.

El preview no ejecuta la clase Python: funciona como comprobación visual de la
estructura que luego usará la interfaz.

### Validación visual específica

- El fragmento muestra título, fecha, hora y descripción.
- Los nombres visibles corresponden a los atributos de `Cita`.
- El estado de la cita se distingue sin alterar el contenido del modelo.

## Comprobación visual en GitHub Pages

Agregar o actualizar `model.py` y `preview.html` en GitHub. Después abrir únicamente
la página principal. Mientras la etapa esté en revisión, el visor integrado
continúa mostrando solo los módulos aprobados:

```text
https://awooolab.github.io/Agenda_SENA/
```

El fragmento de la Clase 02 debe mostrar título, fecha, hora, descripción y
estado. Si se agrega o cambia un campo en el modelo, `preview.html` debe
actualizarse y luego revisarse como módulo independiente. Después de aprobarlo,
se registra en la configuración para incorporarlo a la única ventana integrada.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar `model.py` y comprobar que se imprime un
diccionario con las cuatro claves de la cita. También se puede comprobar:

```python
cita = Cita("Clase", "2026-10-23", "18:00")
datos = cita.a_diccionario()
otra_cita = Cita.desde_diccionario(datos)
```

`cita` y `otra_cita` deben tener los mismos datos. Esta prueba valida Python;
la evidencia visual de la clase se revisa en GitHub Pages.

## Integración después de aprobar el stage

El archivo `stages/02_data_model/model.py` permanece aislado. Después de
validar la etapa, la versión integrada se conecta en `src/` y se coordina desde
`main.py`. El módulo también se registra en `config/integration.json` cuando su
preview deba aparecer en el único visor web.

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

La etapa se puede publicar cuando los archivos definidos están en GitHub,
`preview.html` muestra claramente los datos de `Cita` y la Clase 02 se integra
en la única ventana integrada. La conversión a diccionario queda definida en el
código Python y se probará cuando pueda ejecutarse el proyecto en un PC.

## Alineación con las ventanas de referencia

El espacio visual de este hito es `agenda.appointments`. El modelo no dibuja la
interfaz, pero `preview.html` debe mostrar una cita de prueba con la misma
información que utilizará la tabla de citas recientes: título, fecha, hora,
descripción y estado.

La cita de prueba debe poder reconocerse en la agenda final como una fila o una
tarjeta. El hito no crea todavía SQLite, login ni una segunda ventana.
