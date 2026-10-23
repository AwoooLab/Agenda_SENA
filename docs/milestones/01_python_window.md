# Hito 01 — Ventana inicial de la agenda

## Propósito

Construir una ventana de escritorio mínima para comprobar que Python y Tkinter
funcionan correctamente en el computador del alumno.

Esta etapa no crea todavía citas, usuarios, archivos, bases de datos ni
calendarios. Solo crea la primera ventana.

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

## Diseño exacto

La ventana debe cumplir lo siguiente:

- Título: `Agenda SENA — Etapa 01`.
- Tamaño: `520x320`.
- No permitir cambiar el tamaño de la ventana.
- Fondo principal: blanco o gris muy claro.
- Mostrar el título `Agenda SENA` centrado, con letra grande y negrita.
- Mostrar debajo el texto `Mi agenda local para PC`.
- Mostrar un botón con el texto `Cerrar`.
- El botón `Cerrar` debe cerrar la ventana sin mostrar errores.

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

## Flujo de la clase y validación visual

Esta etapa produce dos resultados coordinados: `app.py` contiene la ventana
funcional en Python y `preview.html` representa esa misma ventana para
GitHub Pages. El trabajo se realiza en este orden:

1. Revisar los requisitos de esta especificación.
2. Construir y ejecutar `app.py` hasta que la ventana funcione.
3. Actualizar `preview.html` para reflejar cualquier cambio visual realizado.
4. Abrir `preview.html` localmente y comparar título, subtítulo, tamaño y
   botón con la ventana de Python.
5. Agregar en `index.html` la tarjeta de la Clase 01, apuntando al
   `preview.html`; el HTML principal solo organiza la colección.
6. Subir los cambios y verificar la misma tarjeta en GitHub Pages.

El preview no ejecuta Python ni reemplaza la prueba local. La etapa no está
terminada hasta que el comportamiento de `app.py` y la representación visual
coinciden.

### Validación visual específica

- La ventana visual conserva el título `Agenda SENA` y el subtítulo.
- El botón `Cerrar` es visible y está ubicado dentro de la ventana.
- El tamaño y la distribución general corresponden a `520x320`.

## Comprobación manual

Desde la raíz del proyecto, ejecutar:

```text
python stages/01_python_window/app.py
```

La comprobación se considera correcta si aparece la ventana, se observa el
título indicado y el botón `Cerrar` termina el programa.

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

El hito está terminado cuando `app.py` abre correctamente, el botón `Cerrar`
funciona, `preview.html` coincide visualmente y la Clase 01 está publicada en
la colección principal.
