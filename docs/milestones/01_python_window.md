# Hito 01 — Ventana inicial de la agenda

## Propósito

Construir una ventana de escritorio mínima para comprobar que Python y Tkinter
funcionan correctamente en el computador del alumno.

Esta etapa no crea todavía citas, usuarios, archivos, bases de datos ni
calendarios. Solo crea la primera ventana.

## Plataforma de esta etapa

El resultado principal se ejecuta en un PC con Python y Tkinter. Las medidas y
controles descritos abajo corresponden a una ventana de escritorio, no a una
página web. `preview.html` solo sirve para representar esa ventana en el
navegador y revisar visualmente que el diseño coincida.

## Archivo que debe crear el alumno

Crear únicamente:

```text
stages/01_python_window/app.py
stages/01_python_window/preview.html
```

No crear otros archivos dentro de esta etapa.

## Requisitos técnicos

- Usar Python 3.
- Usar únicamente el módulo incorporado `tkinter`.
- No instalar paquetes externos.
- El archivo debe funcionar al ejecutarse directamente.
- El código debe tener un bloque `if __name__ == "__main__"`.
- Crear una función `main()` que construya y muestre la ventana.

## Diseño exacto de la ventana de escritorio

La ventana de Tkinter debe cumplir lo siguiente:

- Título: `Agenda SENA — Etapa 01`.
- Tamaño: `520x320`.
- No permitir cambiar el tamaño durante esta primera etapa de prueba.
- Fondo principal: blanco o gris muy claro.
- Mostrar el título `Agenda SENA` centrado, con letra grande y negrita.
- Mostrar debajo el texto `Mi agenda local para PC`.
- Mostrar un botón con el texto `Cerrar`.
- El botón `Cerrar` debe cerrar la ventana sin mostrar errores.

El archivo HTML debe imitar estos mismos elementos para poder compararlos en
GitHub Pages. No se debe construir la aplicación de PC dentro del HTML.

## Comportamiento esperado

1. Al ejecutar el archivo aparece una ventana.
2. La ventana tiene el título indicado.
3. El título y el subtítulo están centrados.
4. Al presionar `Cerrar`, la aplicación termina.
5. Al cerrar la ventana con la X, la aplicación también termina.

## Lo que no se debe hacer en esta etapa

- No crear menús.
- No crear formularios de citas.
- No guardar información.
- No importar archivos desde `src/`.
- No usar SQLite, JSON ni internet.
- No crear todavía inicio de sesión ni calendario.

## Flujo de la clase y validación en GitHub Pages

Esta etapa produce dos resultados coordinados: `app.py` contiene la ventana
funcional en Python y `preview.html` representa esa misma ventana para
GitHub Pages. El trabajo se realiza en este orden:

1. Revisar los requisitos de esta especificación.
2. Agregar en GitHub los archivos de la etapa, incluido `app.py`.
3. Actualizar `preview.html` para representar la pantalla de PC y cualquier
   cambio visual realizado.
4. Subir los cambios y abrir el `preview.html` publicado en GitHub Pages.
5. Agregar en `index.html` la tarjeta de la Clase 01, apuntando al preview; el
   HTML principal solo organiza la colección.
6. Verificar desde la colección que la tarjeta y su resultado se abren bien.

El preview no ejecuta Python. La etapa no está terminada hasta que la
representación visual publicada cumple los requisitos de la especificación.

### Validación visual específica

- La ventana visual conserva el título `Agenda SENA` y el subtítulo.
- El botón `Cerrar` es visible y está ubicado dentro de la ventana.
- El tamaño y la distribución general corresponden a `520x320`.

## Comprobación visual en GitHub Pages

La comprobación que el estudiante puede observar durante la clase se hace en
GitHub Pages:

1. Agregar o actualizar `app.py` y `preview.html` en GitHub.
2. Abrir:
   `https://awooolab.github.io/Agenda_SENA/stages/01_python_window/preview.html`
3. Confirmar que se ven `Agenda SENA`, el subtítulo y el botón `Cerrar`.
4. Si se agregó un icono o se cambió un texto en el diseño, comprobar que el
   mismo cambio aparece en `preview.html`.

GitHub Pages no ejecuta `app.py`. La página solo permite revisar la
representación visual de la ventana de PC.

### Prueba funcional opcional en el PC

Si se dispone de Python instalado, se puede ejecutar `app.py` localmente para
comprobar el comportamiento del botón. Esta prueba no se realiza en GitHub
Pages ni reemplaza la revisión visual del preview.

## Integración posterior

Cuando la etapa esté terminada, adaptar la idea en:

```text
src/interface.py
```

El archivo `stages/01_python_window/app.py` continúa siendo el ejercicio del
alumno. El archivo `app.py` de la raíz será el punto de entrada integrado.

## Instrucción para ChatGPT

```text
Genera únicamente el archivo stages/01_python_window/app.py para un proyecto
educativo llamado Agenda SENA. Usa Python 3 y tkinter, sin paquetes externos.
Crea una función main() y el bloque if __name__ == "__main__". La ventana debe
medir 520x320, no debe poder redimensionarse, debe tener el título
"Agenda SENA — Etapa 01", mostrar "Agenda SENA", mostrar debajo
"Mi agenda local para PC" y tener un botón "Cerrar" que cierre la ventana.
No agregues base de datos, archivos, inicio de sesión, calendario ni otros módulos.
Devuelve únicamente el código de ese archivo.
```

## Criterio de terminado

La etapa se puede publicar cuando `app.py` y `preview.html` están en GitHub,
`preview.html` cumple la validación visual y la Clase 01 aparece en la
colección principal. El comportamiento del botón pertenece al código Python y
se comprobará cuando la aplicación se ejecute en un PC.
