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

El hito está terminado cuando el único archivo creado en la etapa es
`app.py`, la ventana abre correctamente y el botón `Cerrar` funciona.
