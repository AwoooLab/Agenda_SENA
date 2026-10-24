# Presentación del proyecto Agenda SENA

## Especificación de contenido para las diapositivas

Este documento define el contenido literal y el diseño visual de la
presentación del proyecto Agenda SENA. Las imágenes se crearán después de
aprobar este texto. Por ahora solo se definen las escenas, los diagramas, los
iconos y la composición de cada diapositiva.

## Configuración general

- Cantidad de diapositivas: 12.
- Formato: 16:9.
- Tamaño de trabajo recomendado: 1920 × 1080 px.
- Idioma: español.
- Público: estudiantes y docente de una clase de programación.
- Duración estimada: entre 12 y 15 minutos.
- Tono: educativo, claro, técnico y fácil de seguir.
- Una idea principal por diapositiva.
- No usar párrafos largos dentro de las imágenes.
- No usar fotografías genéricas de personas trabajando.
- Las imágenes deben ser ilustraciones, interfaces, diagramas o composiciones
  relacionadas directamente con la aplicación.

## Sistema visual de la presentación

### Colores

- Azul marino principal: `#111D4A`.
- Azul de acción: `#2563EB`.
- Azul claro de apoyo: `#E8F0FF`.
- Fondo claro: `#F7F9FC`.
- Texto principal: `#101A3A`.
- Texto secundario: `#64748B`.
- Verde de confirmación: `#16A34A`.
- Naranja de atención: `#F97316`.
- Borde suave: `#E2E8F0`.

### Tipografía

- Títulos: Arial, Aptos o Inter, peso bold.
- Texto general: Arial, Aptos o Inter, peso regular.
- Título de diapositiva: entre 60 y 64 px.
- Texto principal: entre 30 y 38 px.
- Texto secundario y descripciones: mínimo 24 px.
- Etiquetas y texto de apoyo: mínimo 22 px.
- No usar texto visible por debajo de 22 px; si una miniatura no admite la
  etiqueta, se debe acortar o retirar en lugar de reducir la tipografía.

### Composición común

- Fondo claro en la mayoría de las diapositivas.
- Franja superior discreta con el nombre `Agenda SENA`.
- Número de diapositiva en la esquina inferior derecha.
- Tarjetas blancas con bordes suaves y sombra ligera.
- Iconos lineales azules, de estilo uniforme.
- Diagramas con flechas simples y etiquetas cortas.
- Mantener un margen mínimo de 70 px en cada lado.

### Reglas de lectura y dirección visual

- Cada diapositiva debe tener una escena principal, no una colección de
  tarjetas independientes.
- Las interfaces deben mostrarse grandes y completas; no se deben comprimir
  varias pantallas pequeñas en una misma fila.
- Usar el espacio para explicar relaciones visuales: una pantalla central,
  una conexión clara y pocas anotaciones.
- Evitar líneas de tiempo genéricas, diagramas circulares, filas repetitivas
  de seis cajas y paneles con texto diminuto.
- Los textos dentro de una ilustración deben ser etiquetas funcionales, no
  párrafos. Una etiqueta debe poder leerse sin hacer zoom.
- En las imágenes 08–12 usar como referencia: título de 60–64 px, texto de
  apoyo de 28–34 px y etiquetas internas de 24 px como mínimo.
- Las pantallas de la aplicación deben conservar la misma proporción,
  navegación, colores y jerarquía de las ventanas de referencia.
- La diapositiva debe entenderse en tres segundos por su composición y luego
  poder explicarse con el texto de apoyo.

---

# Diapositiva 01 — Portada

## Texto literal

**Agenda SENA**

**Una agenda local para PC construida paso a paso con Python**

**Proyecto educativo de programación**

**SENA · 2026**

## Distribución

- Colocar el título en el lado izquierdo, centrado verticalmente.
- Colocar el subtítulo debajo del título.
- Ubicar `Proyecto educativo de programación` como una etiqueta pequeña.
- Ubicar `SENA · 2026` en la parte inferior izquierda.
- Reservar el lado derecho para una ilustración de la aplicación.

## Imagen o representación visual

Crear una ilustración vectorial de una ventana de escritorio moderna de Agenda
SENA. La ventana debe mostrar una barra superior azul marino, un menú lateral,
una tarjeta de calendario y una lista de citas. No debe mostrar demasiados
datos ni texto ilegible; debe funcionar como una representación del producto,
no como una captura detallada.

La ventana ilustrada debe aparecer ligeramente inclinada o con una sombra suave
para darle profundidad. Mantener el fondo de la imagen transparente o azul muy
oscuro para integrarlo con la portada.

## Iconos

- Icono principal de calendario con un pequeño reloj.
- Tres puntos de ventana en rojo, amarillo y verde.
- Pequeños indicadores de cita, usuario y actividad dentro de la interfaz.

## Archivo de imagen posterior

```text
docs/pt/img/01_cover.png
```

---

# Diapositiva 02 — Problema que resuelve

## Texto literal

**¿Qué problema estamos resolviendo?**

**Organizar citas y actividades en un solo lugar, con una aplicación sencilla,
local y fácil de ampliar.**

- Las citas pueden quedar dispersas en notas, mensajes o calendarios.
- La información importante debe consultarse rápidamente.
- Una agenda necesita fechas, horas, usuarios, estados y categorías.
- El proyecto convierte esa necesidad en una aplicación funcional.

## Distribución

- Título en la parte superior izquierda.
- Debajo, una frase grande que explique el problema.
- Dividir el cuerpo en dos columnas: `Antes` y `Después`.
- La columna `Antes` debe mostrar desorden visual.
- La columna `Después` debe mostrar una agenda organizada.

## Imagen o representación visual

Crear un diagrama comparativo, no una fotografía. En la columna izquierda,
mostrar pequeñas notas sueltas con textos como `Reunión`, `Entrega`, `Llamar`
y varias fechas desordenadas. Encima colocar la etiqueta `Antes`.

En la columna derecha, mostrar una tarjeta limpia de Agenda SENA con calendario,
horarios y categorías. Encima colocar la etiqueta `Después`.

Entre las columnas usar una flecha azul con el texto `Organizar la información`.
La ilustración debe comunicar el cambio de desorden a estructura.

## Iconos

- Notas o documentos para representar información dispersa.
- Calendario para representar organización.
- Flecha de transformación.
- Check verde para representar una cita organizada.

## Archivo de imagen posterior

```text
docs/pt/img/02_problem.png
```

---

# Diapositiva 03 — Producto que se va a construir

## Texto literal

**¿Qué vamos a construir?**

**Una aplicación local de escritorio para administrar la agenda personal y de
trabajo.**

**Funciones principales**

- Inicio de sesión.
- Calendario mensual.
- Registro y consulta de citas.
- Usuarios y sesión activa.
- Actividades, categorías y estados.
- Almacenamiento local.

## Distribución

- Ubicar el título arriba.
- Colocar la descripción debajo, ocupando todo el ancho disponible.
- En la parte inferior, organizar seis tarjetas en dos filas de tres.
- Cada tarjeta debe contener un icono, un título y una frase corta.

## Texto de las tarjetas

### Tarjeta 01

**Inicio de sesión**

Acceso controlado a la agenda local.

### Tarjeta 02

**Calendario**

Vista mensual de actividades.

### Tarjeta 03

**Citas**

Registro de fecha, hora, título y descripción.

### Tarjeta 04

**Usuarios**

Registro de personas y sesión activa.

### Tarjeta 05

**Actividades**

Categorías, colores y estados de cumplimiento.

### Tarjeta 06

**Datos locales**

Datos guardados localmente.

## Imagen o representación visual

Usar una composición de seis tarjetas conectadas visualmente a una pequeña
ventana central de Agenda SENA. La ventana central representa el producto y
las tarjetas representan sus módulos. No mostrar código en esta imagen.

## Iconos

- Candado para inicio de sesión.
- Calendario mensual.
- Lista de citas.
- Grupo de usuarios.
- Gráfica de actividades.
- Base de datos o disco local.

## Archivo de imagen posterior

```text
docs/pt/img/03_product.png
```

---

# Diapositiva 04 — Dos estados de una sola aplicación

## Texto literal

**Dos estados, una sola aplicación**

**La aplicación cambia de contenido dentro de la misma ventana.**

### Estado 01 — Inicio de sesión

El usuario ingresa sus datos para acceder.

### Estado 02 — Agenda principal

El usuario consulta y administra su información.

**No son dos programas diferentes: son dos estados de la misma aplicación.**

## Distribución

- Mostrar dos representaciones de interfaz, una a la izquierda y otra a la
  derecha.
- Encima de la primera colocar `Estado 01 — Inicio de sesión`.
- Encima de la segunda colocar `Estado 02 — Agenda principal`.
- Conectar ambas mediante una flecha azul con la etiqueta `Ingresar`.
- Colocar la frase final en una banda inferior destacada.

## Imagen o representación visual

La primera interfaz debe ser una tarjeta de login con usuario, contraseña y
botón `Ingresar`. La segunda debe ser la ventana de agenda con menú lateral,
calendario y tarjetas de resumen.

Las dos interfaces deben compartir la misma barra superior, colores, radios y
estilo. La representación debe dejar claro que la navegación ocurre en el
mismo espacio y no mediante dos ventanas independientes.

Se pueden utilizar como referencia editable:

```text
assets/login-window.svg
assets/agenda-window.svg
```

## Iconos

- Candado en el login.
- Flecha de navegación.
- Calendario y usuario en la agenda.

## Archivo de imagen posterior

```text
docs/pt/img/04_two_states.png
```

---

# Diapositiva 05 — Recorrido de la aplicación

## Texto literal

**Del acceso al cierre de sesión**

**La aplicación acompaña todo el trabajo del usuario dentro de una misma
ventana.**

### Momento 01 — Acceso

**Abrir aplicación**

Abrir el programa.

**Iniciar sesión**

Acceder con usuario y contraseña.

### Momento 02 — Trabajo diario

**Ver agenda · navegar por el menú · gestionar citas y actividades**

Consultar y actualizar la información desde la ventana principal.

### Momento 03 — Cierre

**Cerrar sesión**

Regresar al acceso.

## Distribución

- Colocar el título y una frase breve en la parte superior.
- Usar una ventana grande de Agenda SENA como elemento visual central.
- Mantener la ventana central arriba y como el elemento dominante.
- Alinear debajo de ella tres tarjetas del mismo tamaño y sobre una sola fila: `Acceso`, `Trabajo diario` y `Cierre`.
- Usar una separación horizontal constante entre las tarjetas para que el recorrido se lea de izquierda a derecha.
- Conectar la ventana con la fila mediante una flecha vertical y conectar las tarjetas con flechas horizontales.
- Mantener la ventana central como el elemento dominante de la composición.

## Imagen o representación visual

Crear una composición centrada en una sola ventana de Agenda SENA. La ventana
debe mostrar el menú lateral, un resumen de citas, el calendario mensual y una
lista de actividades.

Debajo de la ventana, mostrar tres tarjetas iguales. La primera es `Acceso`,
con `Abrir la aplicación · iniciar sesión`; la segunda es `Trabajo diario`,
con `Ver agenda · navegar · gestionar citas`; la tercera es `Cierre`, con
`Cerrar sesión · regresar al acceso`. Las tres tarjetas deben compartir ancho,
alto, radio de esquina, icono, jerarquía tipográfica y separación interna.

La imagen debe comunicar que el usuario trabaja dentro de una misma ventana y
que la navegación cambia el contenido de la agenda, no el programa completo.

## Iconos

- Candado para el acceso.
- Ventana de aplicación y calendario para el trabajo diario.
- Cerrar sesión para el cierre.
- Flechas simples para conectar los tres momentos.

## Archivo de imagen posterior

```text
docs/pt/img/05_navigation.png
```

---

# Diapositiva 06 — Tecnologías

## Texto literal

**Tecnologías utilizadas**

**Python**

Lenguaje principal del proyecto.

**Tkinter**

Construcción de la ventana de escritorio.

**SQLite**

Base de datos local para usuarios y actividades.

**JSON**

Primer acercamiento al almacenamiento de información.

**GitHub Pages**

Revisión visual del avance del proyecto.

**PyInstaller**

Preparación del ejecutable para Windows.

## Distribución

- Usar seis tarjetas tecnológicas en una composición de dos filas.
- Mantener los nombres de las tecnologías como texto real y legible.
- Debajo de cada nombre colocar su función dentro del proyecto.
- No llenar la diapositiva con fragmentos de código.

## Imagen o representación visual

Crear un diagrama de herramientas conectadas al centro, donde el centro sea
una pequeña ventana de Agenda SENA. Cada tecnología debe aparecer en una
tarjeta con un icono simple y una conexión fina hacia la aplicación.

La imagen no debe depender de logotipos oficiales complejos. Los iconos pueden
ser representaciones lineales: serpiente o símbolo de código para Python,
ventana para Tkinter, cilindro para SQLite, documento para JSON, globo para
GitHub Pages y caja ejecutable para PyInstaller.

## Archivo de imagen posterior

```text
docs/pt/img/06_technologies.png
```

---

# Diapositiva 07 — Cómo se construye cada stage

## Texto literal

**Cómo se construye cada stage**

**Aislado durante la construcción; integrado al finalizar.**

**Espacio de trabajo del estudiante**

**01 — Leer `files.md`**

La especificación define el archivo, los requisitos y el resultado que debe verse.

**02 — Crear `app.py`**

El módulo resuelve un solo objetivo dentro de la carpeta del stage.

**03 — Probar `preview.html`**

La salida se revisa en la misma vista antes de integrarla.

**04 — Integrar**

Cuando está aprobado: módulo → `main.py` → aplicación completa.

## Frase destacada

**Cada archivo tiene una función clara y puede probarse antes de integrarse.**

## Distribución

- Presentar una sola ventana de trabajo, como un espacio de desarrollo.
- En la barra superior mostrar `Agenda SENA / stages / 01_python_window`.
- Organizar tres paneles grandes y consecutivos: `files.md`, `app.py` y
  `preview.html`.
- Conectar los paneles con flechas amplias y verbos directos: `orienta` y
  `construye`.
- Separar la integración en una banda inferior: `módulo aprobado` → `main.py`
  → `aplicación completa`.
- Mantener el texto principal grande; los paneles deben leerse como una
  interfaz de trabajo, no como una lista de tareas.

## Imagen o representación visual

Crear una representación de un espacio de trabajo con tres archivos:

```text
files.md  ──orienta──>  app.py  ──construye──>  preview.html
                                              ↓
                  módulo aprobado → main.py → aplicación completa
```

Cada panel debe parecer una herramienta real: `files.md` como una ficha de
requisitos, `app.py` como un editor de código y `preview.html` como una vista
de navegador con un resultado visible. La barra superior identifica la ruta
`stages/01_python_window`.

## Iconos

- Documento o ficha para `files.md`.
- Editor de código para `app.py`.
- Navegador para `preview.html`.
- Flechas de integración para `main.py`.

## Archivo de imagen posterior

```text
docs/pt/img/07_methodology.png
```

---

# Diapositiva 08 — Stages 01 al 03

## Texto literal

**Stages 01 al 03 — Fundamentos del proyecto**

### Stage 01 — Ventana inicial

Construir la bienvenida, el botón `Siguiente` y la agenda base dentro de una
sola ventana.

### Stage 02 — Modelo de datos

Representar una cita como un objeto de Python con campos claros y reutilizables.

### Stage 03 — Guardado en JSON

Guardar y cargar información local antes de utilizar una base de datos.

**Resultado de la fase:** una interfaz inicial y una estructura básica para
representar información.

## Distribución

- No usar tres tarjetas iguales ni una línea de tiempo escolar.
- Usar una composición horizontal de tres escenas grandes que compartan el
  mismo objeto: una cita de Agenda SENA.
- Colocar un rótulo grande encima de cada escena: `01 VENTANA`, `02 DATO` y
  `03 GUARDADO`.
- Reservar la parte inferior para una sola frase de resultado, sin tarjeta
  decorativa adicional.

## Imagen o representación visual

Crear una secuencia visual de una misma cita que se transforma:

`ventana de agenda → objeto Cita → archivo agenda.json`

La escena izquierda debe mostrar una ventana de Agenda SENA con el formulario
de una cita. La escena central debe ampliar esa misma información como una
ficha de dominio con los campos `title`, `date`, `time` y `category`. La escena
derecha debe mostrar un archivo `agenda.json` grande, con dos o tres registros
legibles y resaltando las mismas propiedades.

Conectar las escenas con dos flechas amplias y una frase corta: `la interfaz
captura`, `el modelo organiza`, `JSON conserva`. No mostrar código Python
completo, listas microscópicas ni puntos de avance.

## Iconos

- Ventana para el Stage 01.
- Objeto o tarjeta de datos para el Stage 02.
- Documento con llaves para el Stage 03.

## Archivo de imagen posterior

```text
docs/pt/img/08_stages_01_03.png
```

---

# Diapositiva 09 — Stages 04 al 06

## Texto literal

**Stages 04 al 06 — Datos y usuarios**

### Stage 04 — Base de datos SQLite

Crear las tablas y relaciones locales para usuarios y actividades.

### Stage 05 — Registro de usuarios

Validar y guardar los datos necesarios para crear una cuenta local.

### Stage 06 — Inicio de sesión

Proteger la contraseña, autenticar al usuario y mantener la sesión activa.

**Resultado de la fase:** usuarios registrados y acceso controlado a la agenda.

## Distribución

- No usar tres columnas de tarjetas.
- Construir una escena de acceso: una ventana de login grande en el centro,
  una fuente de datos a la izquierda y una confirmación de sesión a la
  derecha.
- La lectura debe ir de izquierda a derecha: `datos locales` → `registro` →
  `inicio de sesión`.
- La parte inferior debe contener una única línea de resultado: `Usuario
  autenticado: puede entrar a la agenda`.

## Imagen o representación visual

Crear una escena de control de acceso de izquierda a derecha:

`Base de datos → Registro → Login`

En el tercio izquierdo mostrar un cilindro de SQLite ampliado con las tablas
`users` y `events`, usando solo esos nombres. En el centro mostrar un formulario
de registro grande con `Nombre`, `Correo` y `Contraseña`, sin datos reales. En
el tercio derecho mostrar la ventana de login de Agenda SENA con el candado,
los campos y un botón `Ingresar`. Sobre la salida colocar un sello verde
`Sesión activa`.

Las tres zonas deben verse como partes de una misma aplicación, no como tres
interfaces separadas. No mostrar contraseñas reales ni información personal.
Los datos representados deben ser genéricos y ficticios.

## Iconos

- Base de datos.
- Usuario con signo más.
- Candado.
- Check de autenticación.

## Archivo de imagen posterior

```text
docs/pt/img/09_stages_04_06.png
```

---

# Diapositiva 10 — Stages 07 al 09

## Texto literal

**Stages 07 al 09 — Agenda funcional**

### Stage 07 — Ventana principal

Organizar la navegación, el menú lateral y el área central de la agenda.

### Stage 08 — Calendario mensual

Mostrar los días del mes, cambiar de mes y seleccionar una fecha.

### Stage 09 — Actividades y categorías

Crear actividades, asignar colores, filtrar registros y cambiar su estado.

**Resultado de la fase:** una agenda visualmente completa y preparada para
administrar actividades.

## Distribución

- La agenda terminada debe ocupar aproximadamente el 72 % de la diapositiva.
- No colocar tres tarjetas superiores que compitan con la aplicación.
- Identificar las tres funciones con etiquetas grandes y discretas conectadas
  directamente a la zona correspondiente de la interfaz.
- Dejar aire alrededor de la ventana para que se perciba como el resultado
  principal de la fase.

## Imagen o representación visual

Crear una ilustración amplia de la ventana principal de Agenda SENA. Debe
contener:

- Barra superior azul con búsqueda y usuario.
- Menú lateral con `Inicio`, `Nueva cita`, `Citas`, `Calendario` y
  `Actividades`.
- Cuatro tarjetas de resumen.
- Calendario mensual con dos días resaltados.
- Agenda de hoy con tres actividades.
- Etiquetas de categoría `Trabajo`, `Importante` y `Académica`.

Sobre la interfaz colocar solamente tres etiquetas numeradas, con líneas de
conexión cortas y gruesas: `07 Navegación` apuntando al menú lateral, `08
Calendario` apuntando al calendario mensual y `09 Actividades` apuntando a la
agenda de hoy y sus categorías. Las etiquetas no deben tapar la ventana.

La imagen debe ser una referencia visual limpia, no una captura con texto
pequeño. La aplicación es la protagonista; las etiquetas explican la relación
entre el stage y la zona construida.

## Iconos

- Menú.
- Calendario.
- Reloj.
- Actividad.
- Etiquetas de colores.

## Archivo de imagen posterior

```text
docs/pt/img/10_stages_07_09.png
```

---

# Diapositiva 11 — Stage 10 y entrega

## Texto literal

**Stage 10 — Validar, proteger y entregar**

**Antes de presentar el proyecto se revisan tres aspectos:**

### Pruebas

Comprobar base de datos, autenticación y actividades.

### Seguridad

No exponer contraseñas, datos personales ni información real.

### Ejecutable

Preparar una versión `.exe` para Windows.

**La entrega debe funcionar, poder probarse y poder explicarse.**

## Distribución

- Usar una composición de salida: a la izquierda un bloque vertical de
  validación y a la derecha una caja grande de entrega `AgendaSENA.exe`.
- El bloque de validación debe tener tres filas amplias: `Pruebas`,
  `Seguridad` y `Ejecutable`, cada una con un check y una frase corta.
- La caja del ejecutable debe verse como el resultado dominante, no como un
  icono pequeño.
- Cerrar con la frase final en una banda limpia, sin añadir otra fila de
  tarjetas.

## Imagen o representación visual

Crear una escena de liberación del producto, no una línea de producción:

`Código → Pruebas aprobadas → AgendaSENA.exe`

En el lado izquierdo mostrar una columna de tres comprobaciones grandes:
`Base de datos`, `Login` y `Actividades`, todas con check verde. Integrar un
escudo azul junto a la fila `Seguridad`, con la frase `datos locales protegidos`.
En el lado derecho mostrar una caja de aplicación para Windows con el nombre
`AgendaSENA.exe`, un botón visual `Abrir` y una etiqueta `Listo para entregar`.
Una flecha amplia debe unir las comprobaciones con el ejecutable.

## Iconos

- Check dentro de un círculo.
- Escudo o candado.
- Caja de archivo ejecutable.
- Windows como referencia de plataforma, sin depender de un logotipo grande.

## Archivo de imagen posterior

```text
docs/pt/img/11_delivery.png
```

---

# Diapositiva 12 — Resultado y aprendizaje

## Texto literal

**Resultado final**

**Agenda SENA es una aplicación local de escritorio que se construye función
por función.**

**Al finalizar contamos con:**

- Una ventana de acceso.
- Una agenda navegable.
- Calendario mensual.
- Usuarios y sesión activa.
- Citas y actividades.
- Categorías, colores y estados.
- Datos locales y pruebas.
- Un ejecutable para Windows.

**De una idea a una aplicación funcional, paso a paso.**

**Gracias**

## Distribución

- Usar una composición final tipo portada de producto.
- Colocar el título y una lista breve de resultados en el tercio izquierdo.
- Hacer que la ventana terminada de Agenda SENA ocupe el tercio derecho y el
  centro de la diapositiva.
- Colocar el login detrás de la agenda, más pequeño y parcialmente desplazado,
  para mostrar el recorrido de entrada sin competir con el resultado final.
- Ubicar `Gracias` abajo, con mucho espacio alrededor.

## Imagen o representación visual

Crear una composición final con las dos referencias del producto conectadas:

- Una ventana de login completa, pequeña y nítida, en la parte posterior
  izquierda.
- Una ventana grande de agenda en primer plano, mostrando navegación,
  calendario y agenda de hoy.
- Una conexión visual sencilla entre ambas, como una flecha o un recorrido de
  luz, sin texto adicional.
- Como máximo tres elementos flotantes: calendario, usuario y check. Deben ser
  grandes, separados y funcionales, no adornos diminutos.

La agenda debe ser el elemento visual dominante. La composición debe transmitir
que todos los stages terminaron reunidos en una sola aplicación navegable.

Se pueden tomar como referencia:

```text
assets/login-window.svg
assets/agenda-window.svg
```

## Iconos

- Check final.
- Calendario.
- Usuario.
- Cita.
- Ventana de aplicación.

## Archivo de imagen posterior

```text
docs/pt/img/12_final_result.png
```

---

## Resumen de imágenes que se crearán después

```text
docs/pt/img/01_cover.png
docs/pt/img/02_problem.png
docs/pt/img/03_product.png
docs/pt/img/04_two_states.png
docs/pt/img/05_navigation.png
docs/pt/img/06_technologies.png
docs/pt/img/07_methodology.png
docs/pt/img/08_stages_01_03.png
docs/pt/img/09_stages_04_06.png
docs/pt/img/10_stages_07_09.png
docs/pt/img/11_delivery.png
docs/pt/img/12_final_result.png
```

## Regla para la siguiente fase

No generar imágenes todavía. Primero revisar y aprobar el texto literal, la
cantidad de diapositivas, el orden de exposición y la representación visual de
cada una. Después se creará el JSON con la misma información y posteriormente
las imágenes para cada diapositiva.
