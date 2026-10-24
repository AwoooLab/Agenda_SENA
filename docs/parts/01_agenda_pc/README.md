# Parte 1 — Agenda local para PC

## Propósito

Construir una agenda de escritorio local para Windows usando Python y Tkinter.
Cada stage se desarrolla como módulo independiente y, después de aprobarlo,
se integra en una sola aplicación navegable.

## Resultado visual objetivo

La parte completa debe reproducir dos estados de una misma aplicación de PC:

1. `assets/login-window.svg`: ventana de inicio de sesión.
2. `assets/agenda-window.svg`: ventana principal de la agenda.

Estas dos imágenes son la referencia visual fija del producto terminado. No
son dos aplicaciones independientes ni dos ventanas simultáneas. En Tkinter
existe una sola ventana principal; el contenido cambia de inicio de sesión a
agenda y las opciones del menú reemplazan la vista central.

El curso debe avanzar hacia ese resultado. Cada stage agrega una capacidad o
un componente a un espacio visual definido. Un stage que solo construya una
clase de datos también debe indicar qué ejemplo se verá en `preview.html` y
en qué parte de la ventana final se utilizará.

## Contrato de las dos ventanas

### Ventana 1: inicio de sesión

La pantalla de acceso debe conservar estos elementos, en este orden visual:

- Identidad de Agenda SENA y texto de bienvenida.
- Campo `Usuario o correo electrónico`.
- Campo `Contraseña`.
- Acción `Mostrar` para cambiar la visibilidad de la contraseña.
- Opción `Recordarme`.
- Enlace `¿Olvidaste tu contraseña?` como estado visual reservado.
- Botón principal `Ingresar`.
- Enlace `Crear cuenta` para el flujo de registro.

El login no abre otra ventana. Cuando las credenciales son válidas, el
contenido de la ventana principal cambia al estado de agenda.

### Ventana 2: agenda

La ventana autenticada debe conservar estos espacios:

- Barra superior: nombre de la aplicación, búsqueda y usuario activo.
- Menú lateral: Inicio, Nueva cita, Citas, Usuarios, Calendario,
  Actividades y Cerrar sesión.
- Encabezado del contenido: saludo, fecha y botón `Nueva cita`.
- Tarjetas de resumen: citas de hoy, pendientes, próxima cita y actividades.
- Calendario mensual con cambio de mes y actividades visibles.
- Agenda de hoy con hora, título y categoría.
- Tabla de citas recientes con título, fecha, hora y estado.
- Panel de actividades con progreso, estado y categoría.

Los espacios anteriores son componentes de la misma vista. No deben provocar
la creación de ventanas Tkinter adicionales.

## Medidas y estilo de referencia

Las medidas se expresan en píxeles de la referencia SVG. La implementación de
Tkinter puede adaptarse a la pantalla del PC, pero debe conservar proporciones,
jerarquía y orden.

### Login

- Lienzo de referencia: `1440x900`.
- Tarjeta exterior: margen aproximado de `80`, radio `26`.
- Barra superior: `64` px de alto, azul marino `#111d4a`.
- Panel de marca: ancho aproximado de `460` px.
- Panel del formulario: fondo `#f8fafc`, tarjeta de `520` px de ancho.
- Color principal: `#2563eb`.
- Texto oscuro: `#111d4a`.
- Texto secundario: `#64748b`.
- Bordes: `#cbd5e1` y `#e2e8f0`.
- Tipografía de referencia: Arial o una sans-serif equivalente.

### Agenda

- Lienzo de referencia: `1600x1000`.
- Tarjeta exterior: margen aproximado de `36`, radio `24`.
- Barra superior: `72` px de alto.
- Menú lateral: ancho aproximado de `250` px.
- Contenido central: fondo `#f8fafc` con tarjetas blancas.
- Barra principal: degradado de `#101a3a` a `#1d3f91`.
- Navegación activa: `#2563eb`.
- Estado positivo: `#16a34a`.
- Estado importante: `#f97316`.
- Líneas y separadores: `#e2e8f0` y `#e8edf5`.

Las medidas no deben convertirse en números dispersos sin explicación. En
Tkinter se recomienda definir constantes de color, espaciado y tipografía para
que todos los componentes conserven la misma identidad.

## Espacios visuales para la integración

Cada especificación debe declarar uno o más identificadores de espacio:

```text
login.brand
login.form
login.feedback
agenda.topbar
agenda.sidebar
agenda.summary
agenda.calendar
agenda.today
agenda.appointments
agenda.activities
```

El `preview.html` de un stage debe usar `data-screen` y `data-slot` en su
fragmento principal. Por ejemplo:

```html
<section data-screen="agenda" data-slot="agenda.calendar">
  <!-- validación visual del calendario -->
</section>
```

El fragmento sirve para validar el componente; la página principal sigue
mostrando solamente las dos ventanas de la aplicación.

## Stages de la parte

01 — Bienvenida, navegación y agenda base — 01_python_window
02 — Modelo de datos — 02_data_model
03 — Guardado JSON — 03_json_storage
04 — Base de datos SQLite — 04_sqlite_database
05 — Registro de usuarios — 05_user_registration
06 — Inicio de sesión — 06_login_session
07 — Ventana principal — 07_main_window
08 — Calendario mensual — 08_monthly_calendar
09 — Resumen, citas, actividades, categorías y colores — 09_events_categories_colors
10 — Pruebas y ejecutable — 10_tests_security_executable

Las especificaciones detalladas están en docs/parts/01_agenda_pc/milestones/.

## Flujo de la parte

1. El estudiante lee la especificación y el files.txt del stage.
2. Trabaja únicamente dentro de la carpeta del stage.
3. Ejecuta y valida el módulo de forma independiente.
4. Actualiza su preview.html.
5. La integración revisada se conecta posteriormente en src/ o main.py.
6. Se registra el módulo aprobado en config/integration.json.
7. La aplicación integrada se comprueba desde la única página de GitHub Pages.

Cada aprobación debe registrar también la ventana y el espacio visual que
recibe el componente. No se registra una nueva página: se completa la misma
ventana de login o de agenda.

## Resultado

La aplicación integrada tendrá una sola ventana con navegación interna. El
visor no muestra stages futuros ni usa la existencia de una carpeta como señal
de que una función ya está terminada.

La metodología de independencia, contrato y acumulación está definida en
docs/stage_contract.md.
