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
- `docs/milestones/`: contiene la especificación completa de cada hito.
- `config/`: contiene rutas y formatos compartidos.
- `index.html`: es la colección visual de clases publicada en GitHub Pages.

Cada carpeta de `stages/` trabaja de forma aislada. Al terminar una etapa, la
funcionalidad se incorpora progresivamente en el `main.py` de la raíz. No se
importan automáticamente archivos de una etapa ni se conectan entre sí.

GitHub Pages no ejecuta `main.py`; solo sirve los archivos HTML estáticos. Cada
etapa terminada se publica como una tarjeta de clase en `index.html`, usando el
`preview.html` de su propia carpeta.
