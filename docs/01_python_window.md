# Hito 01 — Bienvenida, navegación y agenda base

> **Especificación vigente:** esta etapa construye dos estados dentro de una
> sola ventana: bienvenida con `Siguiente` y agenda base con datos de ejemplo.

## Propósito

Construir la base visual de Agenda SENA para PC usando una sola ventana de
Tkinter. La aplicación comienza con una bienvenida y un botón `Siguiente`; al
presionarlo, reemplaza el contenido por la ventana principal de la agenda.

Esta etapa crea estructura visual, espacios, datos de demostración e iconos.
Todavía no crea usuarios reales, contraseñas, archivos, base de datos ni
operaciones de citas.

## Metodología de integración vigente

El estudiante trabaja únicamente en `stages/01_python_window/`. `app.py` es
la práctica funcional para PC y `preview.html` representa el mismo resultado
en GitHub Pages. El preview no se abre como una página independiente: la única
dirección de revisión es `https://awooolab.github.io/Agenda_SENA/`.

La página principal conserva las dos ventanas de referencia:
`assets/login-window.svg` representa el inicio y `assets/agenda-window.svg`
representa la agenda. Al pulsar `Siguiente`, la vista pasa a la agenda dentro
del mismo visor; no se crea una página ni una ventana adicional. Cuando este
hito se aprueba, su salida se registra en `config/integration.json` y la
aplicación local la incorpora mediante `main.py` y `src/`.

## Plataforma de esta etapa

El resultado principal se ejecuta en un PC con Python y Tkinter. La ventana de
trabajo usa `1180x760` y puede redimensionarse. Las medidas de los SVG son la
referencia proporcional del diseño final. `preview.html` representa los dos
estados en el navegador, incluye su propio CSS y JavaScript, y no ejecuta
Python.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/01_python_window/app.py
stages/01_python_window/preview.html
```

No crear otros archivos dentro de esta etapa.

## Requisitos técnicos

- Usar Python 3.
- Usar únicamente el módulo incorporado `tkinter`.
- No instalar paquetes externos.
- El archivo debe funcionar al ejecutarse directamente.
- El código debe tener un bloque `if __name__ == "__main__"`.
- Crear una función `main()` que construya y muestre la ventana.

## Diseño exacto de la ventana de escritorio

La ventana de Tkinter debe cumplir lo siguiente:

- Usar una sola instancia de `tk.Tk()`.
- Estado inicial: marca Agenda SENA, bienvenida y un único botón `Siguiente`.
- No solicitar usuario ni contraseña en esta etapa.
- Al pulsar `Siguiente`, reemplazar la bienvenida por la agenda en la misma
  ventana.
- Agenda: barra superior, búsqueda visual, usuario de demostración, menú
  lateral, tarjetas de resumen, calendario, agenda del día, citas recientes y
  actividades.
- Menú visible: Inicio, Nueva cita, Citas, Usuarios, Calendario, Actividades y
  Cerrar sesión. En esta etapa son elementos visuales.
- Usar iconos textuales compatibles con Tkinter. Los SVG reutilizables se usan
  directamente en `preview.html` y en `assets/agenda-window.svg`.
- Mantener fondo claro, barra azul marino, tarjetas blancas, bordes suaves y
  jerarquía equivalente a las referencias.
- Hacer que los contenedores se expandan y se reduzcan con la ventana. No usar
  coordenadas absolutas para ubicar componentes.
- En un espacio reducido, reorganizar las columnas o ajustar el texto sin
  ocultar información ni producir recortes.

El HTML debe imitar estos dos estados para compararlos en GitHub Pages. No
ejecuta ni reemplaza la aplicación de PC.

## Comportamiento esperado

1. Al ejecutar aparece la bienvenida.
2. Solo hay una acción principal: `Siguiente`.
3. Al presionar `Siguiente`, aparece la agenda sin abrir otra ventana.
4. La agenda conserva barra, menú, tarjetas, calendario, citas y actividades.
5. Al cerrar con la X, la aplicación termina.

## Lo que no se debe hacer en esta etapa

- No crear campos reales de usuario o contraseña.
- No validar credenciales ni crear sesiones.
- No crear formularios funcionales de citas.
- No guardar información ni usar SQLite, JSON o internet.
- No importar archivos de otras etapas ni del `main.py` de la raíz.
- No crear una segunda ventana `tk.Tk()`.
- No implementar todavía operaciones reales de usuarios, citas o calendario.

## Flujo de la clase y validación en GitHub Pages

Esta etapa produce dos resultados coordinados: `app.py` contiene la ventana
funcional en Python y `preview.html` representa esa misma ventana para
GitHub Pages. El trabajo se realiza en este orden:

1. Revisar los requisitos de esta especificación.
2. Crear únicamente los archivos dentro de `stages/01_python_window/`.
3. Construir la bienvenida con el único botón `Siguiente`.
4. Construir el estado agenda dentro de la misma ventana, con sus espacios
   visuales e iconos de referencia.
5. Actualizar `preview.html` para representar los dos estados y la transición.
6. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
7. Verificar allí la transición `Siguiente` y la agenda completa de demostración.

El preview es autónomo: sus estilos y su transición JavaScript están dentro de
`preview.html`; solo utiliza los SVG de iconos como recursos visuales. No
ejecuta Python. La etapa no está terminada hasta que la
representación visual publicada cumple los requisitos de la especificación.

### Validación visual específica

- La primera vista muestra la marca, una bienvenida y un único botón
  `Siguiente`.
- Al pulsar `Siguiente`, la misma ventana muestra la agenda base.
- La agenda muestra barra superior, búsqueda, usuario de demostración, menú
  lateral, tarjetas de resumen, calendario, agenda del día, citas recientes y
  actividades.
- Los iconos se ven en los espacios correspondientes y provienen de la
  biblioteca reutilizable de `assets/icons/`.
- La vista se comprueba en `980x640`, `1180x760` y maximizada; en los tres casos
  los textos, tarjetas y paneles permanecen dentro de la ventana.
- No aparecen ventanas, páginas ni formularios adicionales.

## Comprobación visual en GitHub Pages

La comprobación que el estudiante puede observar durante la clase se hace en
GitHub Pages:

1. Agregar o actualizar `stages/01_python_window/app.py` y
   `stages/01_python_window/preview.html`.
2. Actualizar los dos estados visuales del preview: bienvenida y agenda.
3. Abrir únicamente `https://awooolab.github.io/Agenda_SENA/`.
4. Confirmar allí que la primera vista solo ofrece `Siguiente`.
5. Pulsar `Siguiente` y comprobar que la agenda aparece en la misma ventana,
   con sus componentes e iconos.

GitHub Pages no ejecuta `app.py`. La página solo permite revisar la
representación visual de la ventana de PC.

### Prueba funcional opcional en el PC

Si se dispone de Python instalado, se puede ejecutar `app.py` localmente para
comprobar el comportamiento del botón. Esta prueba no se realiza en GitHub
Pages ni reemplaza la revisión visual del preview.

## Integración después de aprobar el stage

El archivo `stages/01_python_window/app.py` permanece aislado como ejercicio.
Después de validar la etapa, la integración se realiza fuera de `stages/`:

- `src/views/` recibe la vista integrada.
- `main.py` inicia la aplicación de una sola ventana.
- `config/integration.json` registra el módulo aprobado para el visor web.

La aplicación integrada no importa automáticamente los archivos de `stages/`.

## Instrucción para ChatGPT

```text
Genera únicamente el archivo `stages/01_python_window/app.py` para un proyecto
educativo llamado Agenda SENA. Usa Python 3 y tkinter, sin paquetes externos.
Crea una función `main()` y el bloque `if __name__ == "__main__"`. Usa una sola
instancia de `tk.Tk()` y una ventana redimensionable cercana a `1180x760`.
Construye primero una bienvenida con la marca, una explicación breve y un único
botón `Siguiente`. Al pulsarlo, limpia el contenido de esa misma ventana y
muestra una agenda base con barra superior, búsqueda, usuario de demostración,
menú lateral, tarjetas de resumen, calendario mensual, agenda del día, citas
recientes y actividades. Usa datos de demostración y símbolos textuales para
los iconos. No agregues campos de credenciales, persistencia, base de datos,
JSON, internet ni ventanas adicionales. Devuelve únicamente el código de ese
archivo.
```

## Criterio de terminado

La etapa se puede publicar cuando `stages/01_python_window/app.py` y
`stages/01_python_window/preview.html` están en GitHub, la única ventana
integrada muestra primero la bienvenida y después la agenda base, y la
representación visual cumple la especificación. El registro del módulo en
`config/integration.json` identifica los espacios visuales cubiertos por esta
base. El comportamiento de `Siguiente` pertenece al código Python y se
comprueba cuando la aplicación se ejecuta en un PC; la misma transición se
comprueba visualmente en GitHub Pages.

## Alineación con las ventanas de referencia

Este hito es la base visual navegable de la aplicación, no el login terminado.
Su flujo cubre el estado `login` de bienvenida y el estado `agenda` de
demostración. La etapa permite aprender `Tk`, `Frame`, `Label`, `Button` y la
reconstrucción de una vista dentro de la misma ventana. Las credenciales reales,
la persistencia y la lógica de negocio se agregan en etapas posteriores.

El preview debe conservar una sola ventana visual. Primero muestra la
bienvenida con `Siguiente`; después muestra la agenda base con los espacios
reservados para las funcionalidades futuras.
