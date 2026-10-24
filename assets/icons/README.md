# Biblioteca de iconos

Esta carpeta contiene iconos SVG reutilizables para Agenda SENA. Los stages
pueden utilizarlos como recursos visuales sin copiar ni redibujar sus trazos.

## Uso en HTML

```html
<img src="../../assets/icons/calendar.svg" alt="Calendario">
```

## Uso dentro de un SVG

```xml
<image href="assets/icons/calendar.svg" x="20" y="20" width="24" height="24" />
```

## Uso futuro en Python

Tkinter no carga SVG directamente. Si una etapa necesita mostrar un icono en la
ventana de PC, se puede convertir el SVG a PNG durante la preparación de esa
etapa y conservar el SVG como fuente editable.

Los iconos comparten color principal `#2563eb`, trazo de 1.8 px y una vista de
24 × 24 px.
