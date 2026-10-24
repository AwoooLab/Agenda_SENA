ETAPA 07 — VENTANA PRINCIPAL DE LA AGENDA
==========================================

PROPÓSITO
---------
Construir la estructura visual que aparece después del inicio de sesión. La
etapa enseña ventanas, paneles, botones y funciones de respuesta.

ARCHIVOS DE LA ETAPA
--------------------
- app.py
- main_window.py
- navigation.py
- preview.html

ADAPTACIÓN AL TAMAÑO DE LA VENTANA
----------------------------------
La ventana principal inicia cerca de `1180x760`, con mínimo `980x640`, y debe
ser redimensionable. La barra lateral conserva un ancho razonable; el área
central crece con `grid` o `pack`. Si el espacio horizontal disminuye, las
tarjetas y paneles pasan a una columna o se ajustan sin quedar cortados.

======================================================================
ARCHIVO: navigation.py
======================================================================

PROPÓSITO
---------
Crear el panel lateral y sus botones de navegación.

LIBRERÍAS
---------
- tkinter.
- No usar todavía SQLite ni servicios de datos.

LECCIÓN 1 — FRAME COMO CONTENEDOR
---------------------------------
Frame agrupa controles y permite separar panel lateral y contenido.

Fragmento:
    panel = tk.Frame(parent, bg="#E5E7EB")
    panel.pack(side="left", fill="y")

El `Frame` crea límites claros entre navegación y contenido. Cuando el área
central cambie, el panel lateral debe conservar identidad, tamaño razonable y
acciones disponibles.

LECCIÓN 2 — BOTONES CON CALLBACK
--------------------------------
Cada botón recibe una función que se ejecutará al hacer clic.

Fragmento:
    tk.Button(panel, text="Calendario", command=al_abrir_calendario).pack()

El callback expresa la intención de navegación y deja la implementación fuera
del botón. Más adelante podrá abrir el calendario real sin cambiar el menú.

LECCIÓN 3 — TRES ACCIONES
-------------------------
Crear las opciones Calendario, Actividades y Cerrar sesión. Las dos primeras
pueden mostrar el texto Sección en construcción.

Las tres acciones representan el contrato mínimo del panel. Una respuesta
temporal es válida en esta etapa siempre que el clic sea observable y conserve
la misma ventana.

======================================================================
ARCHIVO: main_window.py
======================================================================

PROPÓSITO
---------
Crear la ventana autenticada con barra superior, usuario, navegación y área de
contenido.

LIBRERÍAS
---------
- tkinter.
- typing.Callable para documentar funciones de respuesta.
- El modelo Usuario de la etapa anterior.

DISEÑO OBLIGATORIO
------------------
- Tamaño inicial: cercano a 1180x760; mínimo 980x640.
- Título: Agenda SENA.
- Barra superior con Agenda SENA y el usuario activo.
- Panel lateral izquierdo.
- Área central con fondo #F8FAFC.
- Color principal sugerido: #2563EB.

LECCIÓN 1 — RECIBIR UN USUARIO
------------------------------
La función o clase debe recibir el usuario autenticado, no pedirlo otra vez.

Recibir el usuario por parámetro mantiene la autenticación fuera de la vista y
permite mostrar nombre, iniciales o correo en la barra superior.

LECCIÓN 2 — CAMBIAR EL CONTENIDO
--------------------------------
El área central puede limpiarse con destroy y luego recibir un nuevo Label o
Frame. Mantener la navegación fuera del área central.

Separar navegación y vista activa evita reconstruir el menú cada vez que cambia
Calendario o Actividades. El router reemplaza un contenedor, no la ventana raíz.

LECCIÓN 3 — CERRAR SESIÓN
-------------------------
El botón debe cerrar la ventana y llamar on_logout. No duplicar la lógica de
contraseñas.

Cerrar sesión elimina el contexto activo y devuelve la responsabilidad al flujo
de acceso. No borra datos ni crea una segunda ventana principal.

======================================================================
ARCHIVO: app.py
======================================================================

PROPÓSITO
---------
Servir como demostración independiente. Todavía no debe depender de login real.

LÓGICA
------
1. Crear un usuario de prueba llamado Estudiante.
2. Crear la ventana principal.
3. Mostrar la navegación.
4. Mostrar secciones temporales.
5. Permitir cerrar sesión.

La demostración usa un usuario en memoria para concentrarse en la jerarquía de
la ventana y sus callbacks. El preview valida la misma composición con barra,
menú y área central, aunque no ejecute Tkinter.

PRUEBA FUNCIONAL OPCIONAL EN EL PC
-------------------
Ejecutar:

    python stages/07_main_window/app.py

Comprobar que el usuario aparece, los botones responden y Cerrar sesión ejecuta
la salida.

INTEGRACIÓN DESPUÉS DE APROBAR EL STAGE
---------------------------------------
`navigation.py` y `main_window.py` permanecen como ejercicios aislados. Después
de validar la etapa, la navegación se conecta en `src/`, se inicia desde
`main.py` y se registra en `config/integration.json` si su salida visual queda
activa.

======================================================================
ARCHIVO: preview.html
======================================================================

PROPÓSITO
---------
Mostrar el espacio de trabajo que verá el usuario después de iniciar sesión.

CONCEPTOS NECESARIOS
--------------------
- Una barra superior identifica la aplicación y el usuario.
- Un panel lateral contiene la navegación.
- El área central muestra la sección seleccionada.
- CSS Grid permite dividir el panel lateral y el contenido.

FRAGMENTO DE REFERENCIA
-----------------------
    <nav class="barra-lateral">
      <a href="#calendario">Calendario</a>
      <a href="#actividades">Actividades</a>
      <a href="#salir">Cerrar sesión</a>
    </nav>

VALIDACIÓN VISUAL EN GITHUB PAGES
------------
Subir los archivos de esta etapa y abrir únicamente la página
principal https://awooolab.github.io/Agenda_SENA/. Comprobar allí que se
distinguen claramente la barra superior, la navegación y el área de trabajo.

FLUJO DE LA LECCIÓN
-------------------
1. Agregar o actualizar navigation.py, main_window.py y app.py en GitHub.
2. Actualizar preview.html con la misma navegación, textos, áreas e iconos.
3. Subir los cambios y abrir únicamente la página principal.
4. Comprobar allí el módulo independiente de esta etapa dentro de la ventana integrada.

El preview comunica la distribución de la ventana; no ejecuta la navegación de
Tkinter.

CONTRATO DE INDEPENDENCIA E INTEGRACIÓN
----------------------------------------
Este stage se construye como un módulo independiente. No debe importar archivos
de otros stages ni depender de que otra etapa esté terminada. Sus datos de
prueba, entradas, salidas y validaciones pertenecen únicamente a este módulo.

preview.html representa este stage y se revisa desde la única página principal:
https://awooolab.github.io/Agenda_SENA/
La página principal no carga automáticamente todos los previews existentes.
Solo muestra los módulos aprobados que estén registrados en
config/integration.json.

Después de aprobar el stage, la integración se realiza fuera de esta carpeta,
en src/, main.py y config/integration.json. El estudiante no modifica esos
archivos durante la lección. La acumulación ocurre únicamente en la aplicación
integrada.

Antes de integrar, comprobar la entrada independiente, la salida producida,
las funciones públicas, los datos de prueba, las validaciones, los errores y
el punto de conexión futuro. Este módulo no debe conservar funciones de otros
stages dentro de su propio código.

======================================================================
CONTRATO VISUAL Y DE INTEGRACIÓN
======================================================================

VENTANA Y ESPACIOS
------------------
- Ventana: agenda.
- Espacios implementados: agenda.topbar y agenda.sidebar.
- Espacios reservados: agenda.summary, agenda.calendar, agenda.today,
  agenda.appointments y agenda.activities.

PREVIEW
-------
El fragmento debe comenzar con:

    <section data-screen="agenda" data-slot="agenda.topbar">

Debe mostrar la barra superior con Agenda SENA, búsqueda y usuario activo; el
menú lateral con Inicio, Nueva cita, Citas, Usuarios, Calendario, Actividades
y Cerrar sesión; y un contenedor central donde se reemplaza la vista.

REGLA DE NAVEGACIÓN
--------------------
Los botones pueden cambiar el contenido del contenedor central, pero nunca
crear otra instancia de `tk.Tk()`. Los espacios no implementados muestran una
sección reservada, no un indicador de progreso.
