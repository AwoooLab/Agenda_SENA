# Arquitectura de Agenda SENA

La aplicación principal está desarrollada en Python y se ejecuta localmente en
el computador.

## Plataforma objetivo

El producto final es una aplicación de escritorio para PC con Windows. La
aplicación se ejecuta con Python y Tkinter en el computador del usuario; no es
una página web ni depende de internet.

Durante la clase, la evidencia que el estudiante puede observar se publica en
GitHub Pages. Cada `preview.html` muestra la pantalla o el resultado visual de
su etapa. GitHub Pages no ejecuta el código Python; el HTML tampoco reemplaza
la aplicación de escritorio, sino que permite revisar desde el navegador lo que
se está construyendo.

- `main.py`: orquesta la aplicación principal y crece a medida que se
  completan las etapas.
- `stages/`: contiene los archivos de trabajo separados por etapa.
- `docs/parts/`: contiene las partes del proyecto y la especificación completa
  de cada hito.
- `index.html`: es la colección visual de clases publicada en GitHub Pages.

Cada carpeta de `stages/` trabaja de forma aislada. Al terminar una etapa, la
funcionalidad se incorpora progresivamente en el `main.py` de la raíz. No se
importan automáticamente archivos de una etapa ni se conectan entre sí.

El repositorio inicial no incluye una implementación paralela en `src/`,
pruebas globales ni datos de ejemplo. Esos elementos se construirán dentro de
las etapas cuando correspondan; así, el estudiante siempre sabe qué archivo
está trabajando y cuál es el siguiente resultado que debe integrar.

GitHub Pages no ejecuta `main.py`; solo sirve los archivos HTML estáticos. Cada
etapa tiene una tarjeta en `index.html`, usando el `preview.html` de su propia
carpeta. La tarjeta se actualiza conforme se completan los requisitos de la
etapa.

## Regla del visor principal

La única página que el estudiante debe abrir para revisar el avance es el
`index.html` de la raíz, publicado en GitHub Pages. Esa página muestra los
resultados visuales de todos los stages en una colección.

Cada `preview.html` es un componente visual embebible, no una página de
navegación independiente. No debe mostrar encabezados repetidos, enlaces de
retorno ni barras de desplazamiento internas cuando se visualiza desde
`index.html`. El título de la etapa, su explicación y la referencia a la
especificación pertenecen a la tarjeta del visor principal. El archivo puede
conservar una estructura HTML completa para ser válido, pero su `body` debe
usar la clase `embebido` para ocultar la carcasa de página al integrarse.

La colección no funciona como un medidor ni como una lista de porcentajes. Su
propósito es mostrar qué resultado visual corresponde a cada etapa y permitir
comprobar cómo se va construyendo la aplicación.
