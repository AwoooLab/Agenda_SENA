# Assets de diseño

Estos archivos son referencias visuales editables de la aplicación completa.
No son módulos de `stages/` ni deben importarse desde un stage.

- `login-window.svg`: ventana independiente para iniciar sesión.
- `agenda-window.svg`: ventana principal después del inicio de sesión, con menú,
  espacios marcados para resumen, calendario, citas y actividades.

## Flujo visual en GitHub Pages

GitHub Pages muestra únicamente estas dos ventanas, una a la vez. Primero carga
`login-window.svg`, que contiene solamente el botón `Siguiente`. Al pulsarlo,
`web/screen.js` reemplaza la pantalla por `agenda-window.svg`.

La ventana de agenda está deliberadamente vacía. Sus espacios marcados indican
dónde se incorporarán los componentes de las próximas etapas.

Los SVG conservan el texto y las formas como elementos editables. Se pueden
abrir en un editor de vectores o revisar directamente en el navegador.
