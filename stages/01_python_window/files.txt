ETAPA 01 — BIENVENIDA, NAVEGACIÓN Y AGENDA BASE
========================================

PROPÓSITO
---------
Construir la primera versión navegable de Agenda SENA en una sola ventana de
escritorio. Esta etapa presenta una bienvenida con un único botón `Siguiente` y,
al pulsarlo, reemplaza ese contenido por una agenda base con todos sus espacios
visuales: menú, resumen, calendario, citas y actividades.

La etapa define el chasis visual y la navegación inicial. No implementa todavía
usuarios, contraseñas, persistencia ni operaciones reales sobre citas.

PLATAFORMA OBJETIVO
-------------------
La aplicación que se está construyendo es para un PC con Windows y se ejecuta
con Python y Tkinter. La ventana de trabajo debe ser cercana a `1180x760`,
redimensionable y con una sola instancia de `tk.Tk()`.
`preview.html` es únicamente una representación visual para revisar en el
navegador los mismos dos estados; no reemplaza ni ejecuta `app.py`.

ARCHIVO DE LA ETAPA
-------------------
- app.py
- preview.html

REGLAS GENERALES
----------------
- Trabajar desde la carpeta raíz del proyecto.
- Usar Python 3.
- Usar únicamente la biblioteca incorporada tkinter.
- No instalar paquetes externos.
- No importar archivos de otras etapas ni del orquestador principal.
- No crear archivos adicionales.

ADAPTACIÓN AL TAMAÑO DE LA VENTANA
----------------------------------
La ventana inicia cerca de `1180x760` y admite redimensionamiento hasta un
mínimo de `980x640`. El contenido debe ajustarse dentro del espacio disponible:

- usar `pack(fill="both", expand=True)` o `grid` con `weight` y `sticky`;
- permitir que el contenido central crezca cuando la ventana se agranda;
- conservar textos e iconos dentro de sus tarjetas cuando se reduce;
- mantener la barra lateral y reorganizar el contenido central sin recortes;
- comprobar el resultado en `980x640`, `1180x760` y una ventana maximizada.

En `preview.html`, el CSS debe usar anchos relativos y una media query que
convierta las columnas en una columna cuando el espacio horizontal sea menor.

======================================================================
ARCHIVO: app.py
======================================================================

PROPÓSITO DEL ARCHIVO
---------------------
Este archivo será un programa independiente. Su trabajo es crear una ventana
con dos estados internos:

1. Bienvenida: marca, explicación breve y un único botón `Siguiente`.
2. Agenda: barra superior, búsqueda, usuario de demostración, menú lateral,
   tarjetas de resumen, calendario, agenda del día, citas recientes y
   actividades.

El segundo estado se muestra limpiando y reconstruyendo el contenido de la
misma ventana; no se abre otro `Tk()`.

LIBRERÍAS QUE SE PUEDEN USAR
-----------------------------
- tkinter, incluida en Python.
- No usar SQLite, JSON, pathlib, internet ni librerías externas.

LECCIÓN 1 — IMPORTAR TKINTER
----------------------------
Tkinter contiene las herramientas para crear ventanas y controles de escritorio.
La forma corta permite escribir tk.Label y tk.Button:

La biblioteca estándar ofrece una capa de widgets nativos: cada control se
crea con una referencia a su contenedor y conserva una relación de padre e
hijo. La raíz `Tk` será el único proceso gráfico de esta etapa; los `Frame`
organizarán grupos internos sin abrir ventanas adicionales. Esta decisión
facilita que las etapas siguientes agreguen pantallas dentro de la misma
aplicación.

Fragmento:
    import tkinter as tk

LECCIÓN 2 — CREAR LA VENTANA PRINCIPAL
--------------------------------------
tk.Tk() crea la ventana principal. Todo control de esta etapa debe pertenecer a
esa ventana.

La ventana raíz representa el proceso visual completo y debe existir una sola
vez. Los controles no se crean antes de disponer de esa raíz, ya que Tkinter
necesita un propietario para administrar sus recursos y eventos. Mantener esta
jerarquía desde el primer archivo evita que las futuras pantallas se separen en
varias ventanas independientes.

Fragmento:
    ventana = tk.Tk()

LECCIÓN 3 — CONFIGURAR LA VENTANA
---------------------------------
Configurar el título, el tamaño inicial y que la ventana pueda adaptarse a la
pantalla del PC.

`geometry` establece una condición inicial, mientras que `minsize` protege la
interfaz contra un tamaño que vuelva ilegibles los controles. La distribución
real debe quedar en manos de `pack` o `grid`; no se deben fijar todos los
elementos con coordenadas. Una interfaz que conserva sus bloques al ampliar o
reducir la ventana prepara el mismo comportamiento que se revisará en
`preview.html`.

Fragmentos:
    ventana.title("Agenda SENA")
    ventana.geometry("1180x760")
    ventana.minsize(980, 640)

El texto del título debe ser exactamente el indicado. geometry recibe ancho por
alto en píxeles.

LECCIÓN 4 — ORGANIZAR LA VENTANA EN ESTADOS
--------------------------------------------
La bienvenida y la agenda son dos estados de una misma ventana. Un `Frame`
puede actuar como contenedor de cada estado. La función de transición retira
el contenido anterior y construye la siguiente vista.

Un estado describe qué contenido está visible en un momento concreto. En este
caso, el primer estado solo necesita marca, texto y `Siguiente`; el segundo
presenta la estructura completa de la agenda. Reutilizar la raíz y cambiar sus
widgets es una primera forma de navegación: más adelante el mismo patrón podrá
mostrar login, calendario, formularios y tablas sin multiplicar ventanas.

Fragmento:
    def limpiar(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    boton = tk.Button(ventana, text="Siguiente",
                      command=lambda: mostrar_agenda(ventana))

La función pasada a `command` debe existir antes de que el usuario pulse el
botón. El `lambda` permite enviar la ventana como argumento.

LECCIÓN 5 — MOSTRAR TEXTO CON LABEL
-----------------------------------
Un Label muestra un texto. font recibe el nombre de letra, tamaño y estilo.
pack organiza el control en la ventana.

Los `Label` no son únicamente adornos: hacen visible el significado de cada
espacio. Un título identifica la pantalla, un subtítulo orienta al usuario y
los valores de una tarjeta representan datos que después vendrán de modelos o
de una base de datos. Separar texto, tamaño, color y alineación permite que el
contenido se mantenga claro cuando las tarjetas cambien de ancho.

Fragmentos:
    titulo = tk.Label(ventana, text="Agenda SENA")
    titulo.pack(pady=40)

    subtitulo = tk.Label(ventana, text="Mi agenda local para PC")
    subtitulo.pack(pady=10)

Se puede usar font=("Arial", 22, "bold") para el título.

LECCIÓN 6 — CREAR EL BOTÓN SIGUIENTE
--------------------------
Un `Button` muestra la única acción de la bienvenida. `command` recibe una
función, no el resultado de ejecutarla.

El callback es el puente entre una interacción y un cambio de estado. Al
hacer clic, la función debe limpiar la bienvenida y llamar a la construcción
de la agenda; no debe crear otra raíz ni esconder el resultado en una variable
que la vista no pueda mostrar. Esta relación entre evento y acción será
reutilizada por los controles de navegación de las siguientes etapas.

Fragmento:
    boton = tk.Button(ventana, text="Siguiente",
                      command=lambda: mostrar_agenda(ventana))
    boton.pack(pady=20)

Correcto: command=lambda: mostrar_agenda(ventana)
Incorrecto: command=mostrar_agenda(ventana)

LECCIÓN 7 — CREAR TARJETAS Y SECCIONES DE LA AGENDA
-------------------------------------------
La agenda se puede dividir en `Frame` pequeños: barra superior, menú lateral,
resumen, calendario y paneles inferiores. Cada sección debe tener un título,
un contenedor y datos demostrativos, aunque todavía no tenga lógica real.

Una tarjeta es un componente visual con una responsabilidad limitada: mostrar
un indicador, un grupo de citas o una lista. Agruparla en un `Frame` permite
controlar margen, fondo y expansión sin afectar los demás bloques. Los datos
estáticos de esta lección funcionan como contrato visual; los servicios y
repositorios que aparecerán después podrán reemplazarlos sin cambiar la
jerarquía de la ventana.

Ejemplo de una tarjeta visual:
    tarjeta = tk.Frame(contenido, bg="white", padx=16, pady=12)
    tk.Label(tarjeta, text="Citas de hoy", bg="white").pack(anchor="w")
    tk.Label(tarjeta, text="3", bg="white",
             font=("Arial", 22, "bold")).pack(anchor="w")
    tarjeta.pack(side="left", padx=8)

Los iconos de esta etapa pueden ser símbolos de texto en Tkinter. Los SVG de
`assets/icons/` se reservan para `preview.html` y para la referencia visual.

LECCIÓN 8 — INICIAR EL BUCLE DE LA INTERFAZ
-------------------------------------------
`mainloop` mantiene abierta la ventana y espera clics del usuario.

Tkinter trabaja con un bucle de eventos: espera acciones del sistema, detecta
el clic y ejecuta el callback registrado. Por eso la construcción de widgets y
la entrada al bucle son responsabilidades distintas. Si el programa entra al
bucle antes de crear la interfaz, no habrá contenido que mostrar; si nunca
entra, la ventana no puede responder.

Fragmento:
    ventana.mainloop()

Sin mainloop la ventana aparece y se cierra inmediatamente.

LECCIÓN 9 — ORGANIZAR EL PUNTO DE ENTRADA
-----------------------------------------
Es recomendable colocar la construcción de la ventana dentro de main y ejecutar
main solo cuando el archivo se abra directamente.

El punto de entrada ordena el ciclo de vida: preparar la raíz, construir el
estado inicial y comenzar el bucle. La condición `__name__` evita iniciar la
interfaz cuando otro módulo solo importa una función. Esa frontera será útil
cuando la aplicación integrada llame componentes de una etapa sin ejecutar
accidentalmente una segunda aplicación.

Fragmento:
    def main():
        ...

    if __name__ == "__main__":
        main()

LÓGICA COMPLETA QUE DEBE IMPLEMENTAR EL ESTUDIANTE
------------------------------------------------
1. Importar tkinter como tk.
2. Definir main.
3. Crear la ventana.
4. Configurar título, tamaño inicial y redimensionamiento.
5. Crear la función que limpia el contenido actual.
6. Crear la bienvenida con marca, explicación y botón `Siguiente`.
7. Crear la función que construye la agenda base.
8. Mostrar en la agenda los siete espacios visuales solicitados.
9. Iniciar mainloop.
10. Agregar el bloque de ejecución directa.

DISEÑO OBLIGATORIO
------------------
- Título de ventana: `Agenda SENA`.
- Tamaño inicial cercano a `1180x760`, con mínimo `980x640`.
- Bienvenida inicial con marca, explicación breve y botón `Siguiente`.
- Agenda posterior con barra superior, búsqueda, usuario, menú lateral,
  resumen, calendario, agenda del día, citas recientes y actividades.
- Fondo claro, barra superior azul marino, tarjetas blancas, bordes suaves y
  texto con jerarquía clara.
- El cambio de estado ocurre dentro de la misma ventana.

LO QUE TODAVÍA NO SE DEBE CONSTRUIR
-----------------------------------
- Campos de usuario y contraseña.
- Validación de credenciales y sesiones.
- Formularios funcionales de citas.
- Guardado de citas, usuarios o actividades.
- JSON o SQLite.
- Conexión a internet.
- Una segunda ventana.

PRUEBA FUNCIONAL OPCIONAL EN EL PC
-------------------
Si se dispone de Python instalado, ejecutar desde la raíz:

    python stages/01_python_window/app.py

El resultado esperado es que aparezca la bienvenida, que `Siguiente` muestre la
agenda dentro de la misma ventana y que la X termine el programa. Esta prueba
es opcional y no se realiza en GitHub Pages.

INTEGRACIÓN DESPUÉS DE APROBAR EL STAGE
---------------------------------------
El archivo `app.py` permanece aislado como ejercicio. Después de validar la
etapa, la vista se conecta en `src/`, se inicia desde `main.py` y se registra
en `config/integration.json`. El estudiante no modifica esos archivos durante
la lección.

======================================================================
ARCHIVO: preview.html
======================================================================

PROPÓSITO
---------
Mostrar en GitHub Pages una representación visual de la ventana que se construye
en app.py. Este archivo no ejecuta Python ni Tkinter; solo permite revisar el
resultado visual desde el navegador.

CONCEPTOS NECESARIOS
--------------------
- HTML define la estructura.
- CSS define colores, tamaños y distribución, y se incluye dentro de este
  mismo `preview.html` para que el archivo pueda abrirse de forma autónoma.
- JavaScript se incluye dentro de este mismo `preview.html` para controlar el
  cambio entre bienvenida y agenda.

FRAGMENTOS DE REFERENCIA
-------------------------
    <section data-screen="login" data-slot="login.form">
      <h1>Agenda SENA</h1>
      <p>Bienvenido a tu agenda local para PC.</p>
      <button data-action="next-agenda">Siguiente</button>
    </section>

    <section data-screen="agenda" data-slot="agenda.topbar" hidden>
      <!-- barra, menú, resumen, calendario y paneles de demostración -->
    </section>

La vista debe conservar los dos estados y la transición visual del resultado de
Python. El CSS y el JavaScript deben permanecer dentro de este archivo. El
fragmento de agenda debe mostrar los espacios base aunque sus datos sean
estáticos.

VALIDACIÓN VISUAL EN GITHUB PAGES
------------
Subir `app.py` y `preview.html` y abrir únicamente la página principal
https://awooolab.github.io/Agenda_SENA/. Comprobar allí la bienvenida, pulsar
`Siguiente` y confirmar la agenda en la misma ventana.

FLUJO DE LA LECCIÓN
-------------------
1. Agregar o actualizar app.py en GitHub.
2. Actualizar preview.html con los mismos estados, textos, espacios e iconos.
3. Subir los cambios y abrir únicamente la página principal.
4. Comprobar allí que el módulo 01 aparece dentro de la única ventana integrada.

La validación visual hace parte de la lección. Un cambio de diseño previsto en
app.py debe reflejarse también en preview.html. Pages no ejecuta app.py.

CONTRATO DE INDEPENDENCIA E INTEGRACIÓN
----------------------------------------
Este stage se construye como un módulo independiente. No debe importar archivos
de otros stages ni depender de que otra etapa esté terminada. Sus datos de
prueba, entradas, salidas y validaciones pertenecen únicamente a este módulo.
La agenda base es demostrativa: deja preparados los espacios donde las etapas
posteriores conectarán usuarios, almacenamiento, citas y calendario.

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

VENTANA Y ESPACIO
-----------------
- Ventana única con dos estados: `login` y `agenda`.
- Espacios iniciales: `login.brand`, `login.form`, `agenda.topbar`,
  `agenda.sidebar`, `agenda.summary`, `agenda.calendar`, `agenda.today`,
  `agenda.appointments` y `agenda.activities`.
- Estado: base visual, sin autenticación ni persistencia real.

Esta etapa usa la misma composición general de las referencias SVG. Las etapas
05 y 06 completarán el acceso real; las etapas de datos y calendario conectarán
los paneles de demostración.

PREVIEW
-------
El fragmento debe declarar al menos:

    <section data-screen="login" data-slot="login.form">

Debe mostrar la identidad de Agenda SENA y el único botón `Siguiente`. También
debe contener un segundo fragmento oculto con `data-screen="agenda"` y los
espacios visuales de la agenda. Al pulsar `Siguiente`, el primer estado se
oculta y el segundo se muestra sin cambiar de página.

VALIDACIÓN
----------
- Ejecutar `python stages/01_python_window/app.py`.
- Confirmar que la bienvenida se crea y que `Siguiente` muestra la agenda.
- Confirmar que no se crea una segunda ventana.
- Comparar marca, jerarquía, fondo, alineación, menú, tarjetas, calendario y
  paneles con la referencia.
- Subir `app.py` y `preview.html` y comprobar el fragmento desde la página
  principal.
