ETAPA 05 — REGISTRO DE USUARIOS
===============================

PROPÓSITO
---------
Implementar el registro de usuarios separando el modelo, las consultas de la
base de datos y las reglas del registro. Cada archivo tendrá una responsabilidad
específica.

ARCHIVOS DE LA ETAPA
--------------------
- user.py
- user_repository.py
- user_service.py
- test_user_service.py
- preview.html

ADAPTACIÓN AL TAMAÑO DE LA VENTANA
----------------------------------
El formulario de registro debe ocupar el ancho disponible sin salirse de la
tarjeta. Los campos deben usar ancho relativo, los textos deben envolver y las
columnas deben pasar a una sola cuando la ventana se reduzca.

======================================================================
ARCHIVO: user.py
======================================================================

PROPÓSITO
---------
Representar un usuario sin abrir ventanas ni consultar la base de datos.

LIBRERÍAS
---------
- dataclasses.dataclass.
- typing solo si se necesita compatibilidad adicional.

LECCIÓN 1 — ORDEN DE LOS CAMPOS
-------------------------------
Los campos obligatorios deben ir antes de los campos con valor inicial.

Campos:
    username: str
    email: str
    id: int | None = None
    password_hash: str = ""
    password_salt: str = ""
    is_active: bool = True
    created_at: str = ""

El modelo solo representa información: no abre ventanas, no consulta SQLite y
no decide si un registro es válido. Esta separación permite probarlo y
reutilizarlo en registro e inicio de sesión.

LECCIÓN 2 — MODELO SIN LÓGICA EXTERNA
-------------------------------------
El modelo solo guarda información. No debe importar sqlite3 ni tkinter.

Una modificación visual no debe obligar a cambiar la forma de los datos. Cada
responsabilidad queda preparada para probarse sin levantar toda la aplicación.

======================================================================
ARCHIVO: user_repository.py
======================================================================

PROPÓSITO
---------
Encapsular las consultas SQL de usuarios. La interfaz y el servicio no deben
escribir consultas directamente.

LIBRERÍAS
---------
- sqlite3.
- dataclasses o el modelo Usuario de user.py.
- datetime para crear created_at.

LECCIÓN 1 — RECIBIR UNA CONEXIÓN
--------------------------------
La clase RepositorioUsuarios recibe una conexión lista para usar.

Fragmento:
    class RepositorioUsuarios:
        def __init__(self, conexion):
            self.conexion = conexion

LECCIÓN 2 — CONSULTAS PARAMETRIZADAS
------------------------------------
Nunca unir textos para construir una consulta. Usar ? y una tupla de valores.

Fragmento:
    fila = self.conexion.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,),
    ).fetchone()

El repositorio traduce operaciones del programa a SQL. La vista solicita crear
o buscar un usuario y recibe un objeto, sin conocer tablas ni construir
consultas dentro de un botón.

LECCIÓN 3 — INSERTAR Y CONFIRMAR
--------------------------------
Después de INSERT usar commit. Obtener lastrowid para devolver el usuario con
su id.

Fragmento:
    cursor = self.conexion.execute("INSERT INTO users (...) VALUES (...)", valores)
    self.conexion.commit()
    nuevo_id = cursor.lastrowid

`commit` confirma el registro y `lastrowid` permite devolver un `Usuario`
completo al servicio. Sin ese paso, el formulario no sabría qué identidad acaba
de crear.

LECCIÓN 4 — CONVERTIR FILAS EN OBJETOS
--------------------------------------
Una fila de sqlite3.Row puede convertirse en Usuario usando sus columnas por
nombre. Mantener esta conversión en el repositorio.

El mapeo funciona como frontera entre SQLite y el dominio. El servicio y la
interfaz reciben atributos legibles en lugar de posiciones numéricas.

MÉTODOS OBLIGATORIOS
--------------------
    crear(usuario)
    buscar_por_username(username)
    buscar_por_email(email)
    actualizar_credenciales(user_id, password_hash, password_salt)

======================================================================
ARCHIVO: user_service.py
======================================================================

PROPÓSITO
---------
Aplicar las reglas del negocio antes de llamar al repositorio.

LIBRERÍAS
---------
- re, solo para una comprobación sencilla de correo si se necesita.
- datetime para la fecha de creación.
- El modelo y el repositorio de esta misma etapa.

LECCIÓN 1 — NORMALIZAR DATOS
----------------------------
Quitar espacios del usuario y correo. Convertir el correo a minúsculas.

Fragmento:
    username = username.strip()
    email = email.strip().lower()

La normalización evita que espacios o diferencias de mayúsculas representen
identidades distintas. Debe ser predecible y ejecutarse antes de validar.

LECCIÓN 2 — VALIDAR ANTES DE GUARDAR
------------------------------------
Rechazar datos vacíos y duplicados antes de llamar a crear. Lanzar ValueError
con mensajes en español.

Fragmento:
    if not username:
        raise ValueError("El nombre de usuario es obligatorio.")

Validar antes de guardar mantiene la base limpia y permite mostrar el mensaje
junto al campo correcto. Los duplicados se comprueban antes de llamar al
repositorio para traducir el error a lenguaje de la interfaz.

LECCIÓN 3 — SEPARAR RESPONSABILIDADES
-------------------------------------
El servicio decide si los datos son válidos. El repositorio decide cómo se
guardan. No mezclar ambas funciones.

Esta división permite probar el registro sin abrir una ventana y cambiar la
presentación sin duplicar reglas. El preview representa la entrada, la acción y
el mensaje; Python conserva la lógica.

ORDEN DE registrar
------------------
1. Recibir username y email.
2. Normalizar ambos valores.
3. Revisar campos vacíos.
4. Buscar duplicados.
5. Crear Usuario activo.
6. Enviar Usuario al repositorio.
7. Devolver el usuario creado.

======================================================================
ARCHIVO: test_user_service.py
======================================================================

PROPÓSITO
---------
Comprobar las reglas del servicio sin usar datos reales.

LIBRERÍAS
---------
- unittest.
- sqlite3.
- tempfile.
- Los módulos de esta etapa y database.py integrado o una conexión temporal.

CASOS QUE DEBE PROBAR
---------------------
- Registro correcto.
- Nombre vacío.
- Correo vacío.
- Nombre duplicado.
- Correo duplicado con mayúsculas diferentes.
- Usuario creado como activo.

El registro correcto comprueba el camino normal; los campos vacíos y duplicados
comprueban los límites. Probar ambos lados evita aceptar datos que después
romperían el login o la base.

Fragmento de comprobación de error:
    with self.assertRaises(ValueError):
        servicio.registrar("", "correo@ejemplo.com")

PRUEBA FUNCIONAL OPCIONAL EN EL PC
-------------------
Ejecutar:

    python -m unittest stages/05_user_registration/test_user_service.py -v

INTEGRACIÓN DESPUÉS DE APROBAR EL STAGE
---------------------------------------
El modelo, el repositorio y el servicio permanecen aislados en esta carpeta.
Después de validar la etapa, se conectan en `src/`, se coordinan desde `main.py`
y se registran en `config/integration.json` si su salida visual queda activa.

======================================================================
ARCHIVO: preview.html
======================================================================

PROPÓSITO
---------
Mostrar el formulario de registro que posteriormente será implementado en la
interfaz de escritorio.

CONCEPTOS NECESARIOS
--------------------
- label identifica cada campo.
- input permite escribir usuario y correo.
- type="email" indica que el campo contiene un correo.
- button representa la acción de registrar.

FRAGMENTO DE REFERENCIA
-----------------------
    <label for="correo">Correo electrónico</label>
    <input id="correo" type="email" />
    <button>Registrar usuario</button>

Esta vista no guarda información. Solo comunica cómo debe verse el resultado.

VALIDACIÓN VISUAL EN GITHUB PAGES
------------
Subir los archivos de esta etapa y abrir únicamente la página
principal https://awooolab.github.io/Agenda_SENA/. Revisar allí que los campos
tengan etiquetas claras, espacio suficiente y un botón visible.

FLUJO DE LA LECCIÓN
-------------------
1. Agregar o actualizar el modelo, repositorio, servicio y pruebas en GitHub.
2. Actualizar preview.html con los campos, botones, iconos y estados de la
   pantalla de registro.
3. Subir los cambios y abrir únicamente la página principal.
4. Comprobar allí el módulo independiente de esta etapa dentro de la ventana integrada.

El preview no registra usuarios; valida la distribución y claridad de la
interfaz.

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
- Ventana: login.
- Espacios: login.form y login.feedback.
- Estado: formulario de crear cuenta dentro del mismo flujo de acceso.

PREVIEW
-------
El fragmento debe comenzar con:

    <section data-screen="login" data-slot="login.form">

Debe incluir usuario, correo, contraseña, confirmación, botón de registro,
mensaje de éxito y mensajes de validación. `Crear cuenta` es un estado del
login; no se abre una segunda ventana.

CASOS VISIBLES
--------------
- Campos vacíos.
- Correo con formato incorrecto.
- Contraseñas diferentes.
- Usuario o correo duplicado.
- Registro exitoso.
