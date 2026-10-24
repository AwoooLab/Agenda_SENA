# Cómo trabajar las etapas

Cada carpeta es un módulo educativo independiente. El alumno completa una
carpeta sin importar código de otras etapas.

## Qué contiene cada etapa

- Archivos Python propios del módulo.
- files.txt con teoría, ejemplos, restricciones y validaciones.
- preview.html con la salida visual independiente.
- Datos de prueba propios cuando sean necesarios.

## Flujo de trabajo del estudiante

1. Leer la especificación en docs/parts/.
2. Leer el files.txt de la carpeta.
3. Crear o modificar únicamente los archivos solicitados dentro de ese stage.
4. Ejecutar la prueba local indicada.
5. Actualizar el preview.html con la salida visual del módulo.
6. Revisar el flujo de las dos ventanas desde el visor principal de GitHub Pages.
7. Corregir la etapa hasta que cumpla sus requisitos.

El estudiante no modifica main.py, src/, web/ ni config/. Esos archivos forman
la estructura de integración y se actualizan después de aprobar el módulo.

## Independencia y acumulación

Un stage es independiente durante su construcción. La aplicación es acumulativa
después de la integración. Esto significa que el login puede probarse solo,
pero luego puede conectarse como una vista dentro de la ventana principal.

El preview.html del stage sirve para validar ese módulo. La página principal
muestra solamente las dos ventanas finales de `assets/`: inicio de sesión y
agenda. La carpeta de un stage futuro no se muestra automáticamente.

## Contrato del módulo

Cada files.txt debe explicar propósito, alcance, archivos, dependencias,
entradas, salidas, funciones públicas, datos de prueba, validación visual y
forma de integración futura. La referencia común está en
docs/stage_contract.md.

## Recursos visuales compartidos

Los stages pueden reutilizar los iconos de `assets/icons/` desde su
`preview.html`. Se debe conservar la referencia al archivo original y no
copiar ni redibujar el icono dentro del stage. Estos recursos apoyan la
representación visual, pero no reemplazan la lógica ni los archivos propios de
cada módulo.
