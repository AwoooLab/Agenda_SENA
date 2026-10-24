ETAPA 10 — PRUEBAS, SEGURIDAD Y EJECUTABLE
==========================================

PROPÓSITO
---------
Revisar el funcionamiento de la aplicación y preparar una versión ejecutable
para Windows con sus instrucciones de entrega.

ARCHIVOS DE LA ETAPA
--------------------
- test_database.py
- test_auth_service.py
- test_event_service.py
- build_windows.ps1
- release.md
- preview.html

ADAPTACIÓN AL TAMAÑO DE LA VENTANA
----------------------------------
La comprobación visual final debe realizarse en tamaño mínimo, tamaño de
trabajo y ventana maximizada. El ejecutable no debe iniciar con componentes
cortados; la interfaz debe conservar la misma composición adaptable validada
en las etapas anteriores.

======================================================================
ARCHIVO: test_database.py
======================================================================

TEORÍA
------
Una prueba automática prepara datos controlados, ejecuta una operación y
comprueba el resultado. Debe usar una base temporal, nunca datos reales.

LECCIÓN 1 — AISLAR Y COMPROBAR LA BASE DE DATOS
-------------------------------------------------
El aislamiento garantiza que una prueba empiece con el mismo estado y termine
sin modificar el archivo local de la aplicación. `setUp` puede crear una base
temporal, habilitar las condiciones necesarias y preparar el esquema; `tearDown`
debe cerrar la conexión y liberar el recurso. Las aserciones relacionan la
operación con el resultado observable: una fila creada, un usuario recuperado
y una actividad vinculada al usuario correcto.

LIBRERÍAS
---------
- unittest.
- tempfile.
- sqlite3.

CASOS
-----
- Crear esquema.
- Insertar y leer usuario.
- Insertar actividad relacionada.
- Comprobar la relación entre ambas tablas.
- Cerrar y eliminar los datos temporales.

El orden de los casos ayuda a leer la historia completa: primero existe la
estructura, después se insertan datos y finalmente se consulta la relación.
Una prueba de integración de este tipo no reemplaza las pruebas unitarias,
pero confirma que los contratos entre esquema, repositorio y servicio son
compatibles.

======================================================================
ARCHIVO: test_auth_service.py
======================================================================

TEORÍA
------
Las pruebas de seguridad no deben imprimir contraseñas. Deben comprobar el
resultado del inicio de sesión y que los datos guardados no contienen el secreto
original.

LECCIÓN 2 — VERIFICAR AUTENTICACIÓN Y SESIÓN
---------------------------------------------
La prueba de autenticación observa decisiones, no secretos: una credencial
correcta produce un usuario o una sesión, una incorrecta produce rechazo y un
usuario inactivo no puede entrar. La sesión se prueba como estado controlado,
con creación y cierre explícitos. Las aserciones deben comprobar que la
respuesta es coherente sin revelar el hash, la contraseña ni datos sensibles en
mensajes de diagnóstico.

CASOS
-----
- Contraseña correcta.
- Contraseña incorrecta.
- Usuario inactivo.
- Usuario inexistente.
- Sesión actual.
- Cierre de sesión.

Los casos negativos tienen la misma importancia que el caso feliz. Comparar
usuario inexistente, contraseña incorrecta y usuario inactivo permite distinguir
errores de búsqueda, de credencial y de autorización; así la vista puede
mostrar un mensaje general sin filtrar información sobre las cuentas.

======================================================================
ARCHIVO: test_event_service.py
======================================================================

TEORÍA
------
Probar cada operación de actividad por separado facilita encontrar errores.

LECCIÓN 3 — COMPROBAR OPERACIONES Y REGLAS DE ACTIVIDADES
----------------------------------------------------------
Las pruebas del servicio deben verificar la secuencia completa de una
actividad: crear una entrada válida, recuperarla, editarla, filtrarla,
marcarla como completada y eliminarla. También deben demostrar que fechas,
horarios y campos obligatorios se rechazan antes de llegar al almacenamiento.
Cada prueba debe preparar sus propios datos para que el orden de ejecución no
oculte errores.

CASOS
-----
- Crear.
- Editar.
- Filtrar.
- Completar.
- Eliminar.
- Rechazar datos inválidos.

======================================================================
ARCHIVO: build_windows.ps1
======================================================================

PROPÓSITO
---------
Automatizar la creación del ejecutable en Windows.

LECCIÓN 4 — CONSTRUIR UNA ENTREGA REPETIBLE
--------------------------------------------
Un script de construcción convierte una secuencia manual en un procedimiento
que puede repetirse y revisarse. Primero verifica el entorno, después ejecuta
las pruebas y solo si terminan correctamente solicita a PyInstaller el
ejecutable. La salida `dist/` debe ser predecible y el script debe detenerse
ante un error para no presentar un archivo que no fue validado.

CONCEPTOS DE POWERSHELL
-----------------------
- Una línea inicia con un comando.
- $ErrorActionPreference = "Stop" detiene el script si ocurre un error.
- python -m ... ejecuta una herramienta instalada en Python.
- dist/ es la carpeta de salida.

`$ErrorActionPreference = "Stop"` establece una política de fallo temprano.
Los comandos se mantienen separados por responsabilidad: comprobación de
Python, pruebas y empaquetado. No se incluyen bases reales ni credenciales,
porque el ejecutable es una entrega de software y no un respaldo de datos.

FRAGMENTOS ORIENTATIVOS
-----------------------
    $ErrorActionPreference = "Stop"
    python -m unittest discover -s stages/10_tests_security_executable -p "test_*.py" -v
    python -m PyInstaller --onefile --windowed --name AgendaSENA main.py

ORDEN DE LA LÓGICA
------------------
1. Confirmar que Python existe.
2. Ejecutar las pruebas.
3. Detenerse si una prueba falla.
4. Construir con PyInstaller.
5. Informar que el resultado quedó en dist/.

La secuencia también sirve como lista de diagnóstico. Si falla el entorno, se
corrige la instalación; si falla una prueba, se corrige el código; si falla
PyInstaller, se revisan dependencias y rutas. No conviene saltar directamente
al empaquetado, ya que el error quedaría oculto dentro de una entrega final.

No copiar credenciales, datos personales ni bases reales al ejecutable.

======================================================================
ARCHIVO: release.md
======================================================================

PROPÓSITO
---------
Explicar a otra persona cómo usar la versión terminada.

LECCIÓN 5 — DOCUMENTAR LA ENTREGA Y SU USO
-------------------------------------------
Una guía de entrega describe el recorrido después de terminar el desarrollo:
requisitos, ejecución, pruebas, construcción y ubicación del `.exe`. También
delimita los datos que la aplicación guarda localmente y la información que no
debe compartirse. La documentación convierte una carpeta de código en una
entrega que otra persona puede instalar, probar y reportar.

SECCIONES NECESARIAS
--------------------
- Requisitos de Windows.
- Cómo abrir el proyecto.
- Cómo ejecutar las pruebas.
- Cómo construir el ejecutable.
- Dónde encontrar el archivo .exe.
- Qué archivos locales crea la agenda.
- Qué información nunca se debe compartir.
- Cómo informar un error.

El texto debe estar completamente en español. Los nombres de archivos, comandos
y herramientas se escriben exactamente como existen.

Las instrucciones deben distinguir entre comandos de desarrollo y uso normal
del ejecutable. Una ruta, un nombre de archivo o una opción mal escrita puede
impedir que la persona repita el procedimiento, por lo que cada paso debe
corresponder con lo que realmente produce `build_windows.ps1`.

PRUEBA FUNCIONAL OPCIONAL EN EL PC
-------------------
Ejecutar:

    python -m unittest discover -s stages/10_tests_security_executable -p "test_*.py" -v

Después ejecutar build_windows.ps1 y probar el archivo .exe en una cuenta limpia
de Windows.

INTEGRACIÓN POSTERIOR
---------------------
Mantener las tres pruebas, el script y la guía dentro de esta carpeta de etapa.
Después de validar la etapa, conectar la entrega final en `src/` y `main.py`, y
usar el script de esta etapa para preparar el ejecutable. Registrar en
`config/integration.json` únicamente los módulos aprobados que deban aparecer
en el visor web.

======================================================================
ARCHIVO: preview.html
======================================================================

PROPÓSITO
---------
Mostrar el estado de la entrega final: pruebas aprobadas, seguridad revisada y
ejecutable preparado para Windows.

LECCIÓN 6 — PRESENTAR LA ACEPTACIÓN FINAL
------------------------------------------
El preview final resume evidencias visibles del proyecto: pruebas aprobadas,
protección de credenciales, navegación de las dos ventanas y ejecutable
disponible. Cada tarjeta comunica una condición verificable y puede enlazarse
con el espacio que ocupa dentro de la agenda integrada. No reemplaza la
ejecución local; funciona como comprobación visual del resultado que se espera
en la aplicación.

CONCEPTOS NECESARIOS
--------------------
- Un resumen visual puede usar tarjetas de estado.
- El color verde indica una condición aprobada, siempre acompañado de texto.
- Un botón puede representar la descarga del ejecutable, aunque esta vista no
  descarga archivos reales.

Los estados visuales deben tener texto y contraste suficiente; el color verde
por sí solo no demuestra una prueba. La disposición debe adaptarse al ancho del
visor y conservar las dos ventanas de referencia sin crear un panel adicional
que no exista en el programa.

FRAGMENTO DE REFERENCIA
-----------------------
    <div class="estado-exito">
      <strong>Pruebas</strong><br />Todas aprobadas
    </div>

VALIDACIÓN VISUAL EN GITHUB PAGES
------------
Subir los archivos de esta etapa y abrir únicamente la página
principal https://awooolab.github.io/Agenda_SENA/. Comprobar allí que la
entrega muestra claramente el nombre del ejecutable, el estado de las pruebas y
las condiciones de seguridad.

FLUJO DE LA LECCIÓN
-------------------
1. Agregar o actualizar pruebas, seguridad, script y release.md en GitHub.
2. Actualizar preview.html con el nombre, estados, mensajes e iconos de la
   entrega final.
3. Subir los cambios y abrir únicamente la página principal.
4. Comprobar allí el módulo independiente de esta etapa dentro de la ventana integrada.

La vista HTML comunica el resultado de la entrega; no compila ni descarga el
ejecutable.

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
- Ventanas: login y agenda.
- Espacios revisados: todos los espacios registrados por las etapas anteriores.
- Estado: flujo completo aprobado.

PRUEBA DE ACEPTACIÓN
---------------------
La prueba final debe abrir el login, aceptar un usuario de prueba, mostrar la
agenda en la misma ventana, navegar por el menú, crear una cita, comprobarla
en calendario, agenda de hoy y tabla, cerrar sesión y regresar al login.

PREVIEW
-------
El fragmento debe comenzar con:

    <section data-screen="agenda" data-slot="agenda.activities">

Debe comunicar pruebas aprobadas, credenciales protegidas, navegación completa
y ejecutable preparado. No debe mostrar secretos reales ni crear una pantalla
adicional fuera de las dos ventanas de referencia.
