# Assets de diseño

Estos archivos son referencias visuales editables de la aplicación completa.
No son módulos de `stages/` ni deben importarse desde un stage.

- `login-window.svg`: ventana final de inicio de sesión.
- `agenda-window.svg`: ventana principal final con menú, resumen, calendario,
  citas, actividades y categorías.

## Flujo visual en GitHub Pages

GitHub Pages muestra únicamente estas dos ventanas, una a la vez. Primero carga
`login-window.svg`. Al pulsar `Ingresar`, `web/screen.js` reemplaza la pantalla
por `agenda-window.svg`, que representa el programa terminado con datos de
ejemplo.

Los SVG conservan el texto y las formas como elementos editables. Se pueden
abrir en un editor de vectores o revisar directamente en el navegador.
