# Arquitectura de Agenda SENA

La aplicación principal está desarrollada en Python y se ejecuta localmente en
el computador.

- `app.py`: inicia la aplicación.
- `src/`: contiene el modelo, las reglas, el almacenamiento y la interfaz.
- `data/`: contiene los datos locales en JSON.
- `tests/`: contiene las pruebas automáticas.
- `stages/`: contiene los archivos de trabajo separados por etapa.
- `docs/milestones/`: contiene la especificación completa de cada hito.
- `config/`: contiene rutas y formatos compartidos.
- `index.html`: es la colección visual de clases publicada en GitHub Pages.

GitHub Pages no ejecuta `app.py`; solo sirve los archivos HTML estáticos. Cada
etapa terminada se publica como una tarjeta de clase con su `preview.html`, su
guía y sus materiales relacionados.
