# Agenda SENA

Proyecto educativo de una agenda de escritorio local desarrollada primero en Python.

## Punto de entrada

```text
python main.py
```

## Pruebas

Las pruebas se incorporan en la carpeta de la etapa que las necesita. Cada
`files.txt` explica cuándo ejecutarlas y qué resultado esperar; al inicio no
existe una suite global independiente.

## Estructura principal

- `main.py`: orquestador de la aplicación Python; crece con cada etapa.
- `stages/`: archivos que el alumno irá creando o modificando por etapa.
- `docs/milestones/`: hitos completos con requisitos, prompts e integración en
  `main.py`.
- `index.html`: orquestador de la colección visual para GitHub Pages.
- `plan.md`: plan de desarrollo.

Cada carpeta de `stages/` es independiente. Cuando una etapa se termina, su
funcionalidad se incorpora al `main.py` de la raíz y su resultado visual se
agrega como tarjeta en `index.html`.

GitHub Pages solo muestra `index.html` y los `preview.html`; no ejecuta la
aplicación Python.
