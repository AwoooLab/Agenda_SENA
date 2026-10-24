# Assets de diseño

Estos archivos son referencias visuales editables de la aplicación completa.
No son módulos de `stages/` ni deben importarse desde un stage.

- `login-window.svg`: ventana inicial de acceso y bienvenida de la Etapa 01.
- `agenda-window.svg`: ventana principal final con menú, resumen, calendario,
  citas, actividades y categorías.

## Flujo visual en GitHub Pages

GitHub Pages muestra únicamente estas dos ventanas, una a la vez. Primero carga
`login-window.svg`. En la Etapa 01, al pulsar `Siguiente`, `web/screen.js` reemplaza la pantalla
por `agenda-window.svg`, que representa el programa terminado con datos de
ejemplo.

Las etapas de usuarios y sesión completarán después los campos reales de acceso
en esta primera referencia sin crear una ventana adicional.

Los SVG conservan el texto y las formas como elementos editables. Se pueden
abrir en un editor de vectores o revisar directamente en el navegador.

## Iconos compartidos

La carpeta `icons/` contiene iconos SVG reutilizables para los stages. Cada
archivo es independiente, editable y conserva el mismo estilo visual de
Agenda SENA. La guía de uso está en `assets/icons/README.md`.

## Relación con los stages

Los SVG de esta carpeta son referencias del resultado visual final. Los stages
no deben modificarlos durante una lección ni convertirlos en dependencias de
Python. Cada milestone indica qué espacio de la referencia está construyendo:

- Login: `login.brand`, `login.form`, `login.feedback`.
- Agenda: `agenda.topbar`, `agenda.sidebar`, `agenda.summary`,
  `agenda.calendar`, `agenda.today`, `agenda.appointments` y
  `agenda.activities`.

El código Python reproduce la jerarquía y el comportamiento con Tkinter. El
`preview.html` reproduce el mismo componente con HTML y CSS para la revisión
visual.
