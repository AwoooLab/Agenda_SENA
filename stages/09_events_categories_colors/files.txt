ETAPA 09 — ACTIVIDADES, CATEGORÍAS Y COLORES
=============================================

PROPÓSITO
---------
Construir la lógica completa de las actividades y conectarla con el formulario
visual. Cada archivo tiene una responsabilidad específica.

ARCHIVOS DE LA ETAPA
--------------------
- event.py
- category.py
- event_service.py
- event_form.py
- color_legend.py
- test_event_service.py
- preview.html

ADAPTACIÓN AL TAMAÑO DE LA VENTANA
----------------------------------
El formulario, la leyenda de colores y las listas de actividades deben crecer
con el contenedor. Las categorías no deben depender solo del color, y los
textos deben envolverse o pasar a una columna cuando la ventana se reduzca.

======================================================================
ARCHIVO: event.py
======================================================================

PROPÓSITO
---------
Representar una actividad con sus datos y estado.

LECCIÓN 1 — MODELAR UNA ACTIVIDAD
----------------------------------
Una actividad es una entidad del dominio: reúne la información necesaria para
mostrar, guardar y modificar una cita sin depender de una ventana ni de una
consulta SQL. La clase debe describir datos y estado, mientras que las reglas
de fechas, horarios y operaciones quedarán en el servicio. Esta separación
permite que la misma actividad aparezca en el calendario, en la agenda del día
y en una tabla sin duplicar su significado.

LIBRERÍAS
---------
- dataclasses.dataclass.
- No usar Tkinter ni consultas SQL en el modelo.

CAMPOS
------
    id: int | None
    user_id: int
    titulo: str
    fecha: str
    hora_inicio: str
    hora_fin: str
    descripcion: str
    categoria_id: int
    completado: bool

El título, fecha, hora inicial y hora final son obligatorios.

`dataclass` genera una estructura legible para construir y comparar objetos.
Los tipos documentan el contrato que consumen el servicio y el formulario; por
ejemplo, `completado` debe ser un booleano y no el texto de un control visual.
El identificador puede estar vacío antes de guardar y recibir valor después de
la inserción. Mantener este ciclo explícito evita confundir un objeto nuevo con
uno que ya existe en la base de datos.

======================================================================
ARCHIVO: category.py
======================================================================

PROPÓSITO
---------
Representar una categoría y su color.

LECCIÓN 2 — DEFINIR CATEGORÍAS Y SIGNIFICADO VISUAL
----------------------------------------------------
La categoría es un dato reutilizable, no una decoración de la tarjeta. Su
nombre permite filtrar y leer la actividad; su color crea una señal rápida en
el calendario y en la lista. El modelo guarda el valor del color junto al
nombre para que la interfaz pueda representar la misma categoría en todos los
componentes y para que un cambio de diseño no altere la lógica.

CAMPOS
------
    id: int
    nombre: str
    color: str

CATEGORÍAS INICIALES
--------------------
- Trabajo — #2563EB.
- Personal — #16A34A.
- Estudio — #F59E0B.
- Salud — #DC2626.

No usar colores sin mostrar también el nombre de la categoría.

La combinación color más texto mejora la accesibilidad y evita que una persona
dependa de distinguir tonos. Conviene conservar una paleta con contraste y
usar códigos hexadecimales consistentes, de modo que el `preview.html` y la
ventana de Tkinter comuniquen la misma semántica.

======================================================================
ARCHIVO: event_service.py
======================================================================

PROPÓSITO
---------
Aplicar las reglas de actividades y separar la lógica de la interfaz.

El servicio es la frontera entre los datos recibidos por el formulario y el
repositorio. Allí se normalizan entradas, se validan invariantes y se decide
qué operación debe ejecutarse. El formulario no debe saber cómo se construye
un `INSERT`, y el repositorio no debe decidir si una hora es válida; cada capa
conserva una responsabilidad que puede probarse de forma independiente.

LIBRERÍAS
---------
- datetime para validar fechas y horas.
- event.py y category.py.
- sqlite3 o un repositorio recibido por el constructor.

MÉTODOS NECESARIOS
------------------
    crear(evento)
    editar(evento)
    eliminar(evento_id)
    completar(evento_id)
    listar_por_fecha(fecha)
    filtrar(fecha, categoria_id, completado)

LECCIÓN 1 — VALIDAR UNA FECHA
-----------------------------
Usar datetime.strptime(fecha, "%Y-%m-%d") y capturar ValueError.

La fecha se recibe como texto porque así llega desde un `Entry`, pero el
servicio la convierte temporalmente a un valor de fecha para comprobar que el
mes y el día existen. Después conserva el formato ISO `AAAA-MM-DD`, que ordena
correctamente como texto y sirve como contrato común para SQLite, filtros y
calendario.

LECCIÓN 2 — VALIDAR HORAS
-------------------------
Usar datetime.strptime(hora, "%H:%M") y comparar la hora final con la inicial.
La hora final debe ser posterior.

Convertir ambas horas antes de compararlas evita comparar cadenas con formatos
distintos. La regla de intervalo se expresa como `hora_inicio < hora_fin`;
con ella se rechazan actividades vacías, invertidas o de duración cero. El
servicio debe devolver un mensaje comprensible y no dejar que una excepción de
la interfaz decida la regla.

LECCIÓN 3 — SEPARAR CONSULTAS Y REGLAS
--------------------------------------
El servicio valida y decide. El repositorio o la conexión ejecuta SQL. No
colocar consultas en event_form.py.

Esta separación permite sustituir el almacenamiento o probar el servicio con
un repositorio falso. El formulario solo recopila valores y reacciona al
resultado; el servicio transforma esos valores en una decisión de dominio; el
repositorio persiste la decisión. El flujo queda preparado para que una misma
operación actualice calendario, agenda y tabla cuando se integre en la ventana.

======================================================================
ARCHIVO: event_form.py
======================================================================

PROPÓSITO
---------
Crear el formulario para guardar una actividad.

LECCIÓN 4 — CONSTRUIR EL FORMULARIO Y SU FLUJO
-----------------------------------------------
Un formulario convierte interacción en datos del dominio. Cada control debe
tener una etiqueta, una referencia estable y una validación asociada al campo
que representa. El botón `Guardar` inicia un flujo completo —leer, construir,
validar y persistir— y `on_saved` comunica el resultado a la vista superior sin
que el formulario conozca el calendario.

LIBRERÍAS
---------
- tkinter.
- ttk para Combobox y controles con mejor apariencia.
- event_service.py.

CONTROLES EN ESTE ORDEN
-----------------------
1. Título.
2. Fecha (AAAA-MM-DD).
3. Hora inicial (HH:MM).
4. Hora final (HH:MM).
5. Descripción.
6. Categoría.
7. Guardar.
8. Cancelar.

FLUJO DEL BOTÓN GUARDAR
-----------------------
1. Leer los valores.
2. Crear un Evento.
3. Enviar el evento al servicio.
4. Si hay ValueError, mostrarlo en español.
5. Si funciona, llamar on_saved(evento).

El callback de éxito permite limpiar el formulario, cerrar un panel o
refrescar las listas sin acoplar esas decisiones al componente. Los errores de
entrada deben permanecer visibles junto al formulario y no ocultarse en la
consola; así el estudiante puede verificar el comportamiento tanto en Python
como en la referencia visual.

======================================================================
ARCHIVO: color_legend.py
======================================================================

PROPÓSITO
---------
Mostrar el significado de cada categoría.

LECCIÓN 5 — CREAR UNA LEYENDA ACCESIBLE
---------------------------------------
La leyenda convierte los códigos de color en una explicación que la persona
puede consultar. Cada fila reúne un indicador, el nombre y, si hace falta, una
descripción breve. Al construirla con pequeños `Frame` se conserva la misma
estructura cuando se muestre junto al calendario o debajo de una lista.

Cada fila debe mostrar un indicador de color y el nombre escrito de la categoría.
Usar Frame y Label. El color ayuda a reconocer, pero el texto debe comunicar la
información aunque la persona no distinga los colores.

======================================================================
ARCHIVO: test_event_service.py
======================================================================

CASOS NECESARIOS
----------------
- Crear actividad válida.
- Rechazar título vacío.
- Rechazar fecha inválida.
- Rechazar hora inválida.
- Rechazar hora final anterior o igual.
- Editar actividad.
- Filtrar por fecha.
- Filtrar por categoría.
- Completar actividad.
- Eliminar actividad.

LECCIÓN 6 — PROBAR LAS REGLAS DEL SERVICIO
-------------------------------------------
Cada caso de prueba fija una entrada y una consecuencia esperada. Los casos
válidos comprueban que el flujo produce una actividad utilizable; los inválidos
demuestran que las reglas protegen el almacenamiento. Los filtros y el cambio
de estado completado comprueban que la salida puede alimentar diferentes
secciones de la misma agenda sin perder el identificador ni la categoría.

PRUEBA FUNCIONAL OPCIONAL EN EL PC
-------------------
Crear una actividad por categoría, editar una, completar otra, filtrar por fecha
y eliminar una. Comprobar que el calendario pueda recibir los resultados.

INTEGRACIÓN DESPUÉS DE APROBAR EL STAGE
---------------------------------------
Los modelos, el servicio y los controles permanecen aislados. Después de
validar la etapa, se conectan en `src/`, se coordinan desde `main.py` y se
registran en `config/integration.json` si su salida visual queda activa.

======================================================================
ARCHIVO: preview.html
======================================================================

PROPÓSITO
---------
Mostrar el formulario de actividades, una actividad guardada y la leyenda de
categorías que se implementarán en la aplicación de escritorio.

LECCIÓN 7 — REPRESENTAR EL MÓDULO EN EL PREVIEW
------------------------------------------------
El preview traduce el contrato del servicio a una comprobación visible. No
simula una base de datos real: presenta los campos, estados y respuestas que
la ventana debe poder mostrar. Los atributos `data-screen` y `data-slot`
identifican el lugar que ocupará el módulo cuando el orquestador lo integre en
la única ventana de GitHub Pages.

CONCEPTOS NECESARIOS
--------------------
- input recibe título, fecha y hora.
- select permite elegir una categoría.
- Una tarjeta puede representar una actividad guardada.
- Las categorías deben tener color y nombre escrito.

La composición debe conservar los espacios aunque la cantidad de datos cambie.
El formulario, la tarjeta guardada y la leyenda se organizan con CSS flexible;
las columnas pueden pasar a una sola cuando el visor sea más estrecho. La
validación visual revisa el resultado de las reglas, no solamente la presencia
de etiquetas.

FRAGMENTO DE REFERENCIA
-----------------------
    <select id="categoria">
      <option>Trabajo</option>
      <option>Personal</option>
    </select>

    <span class="etiqueta verde">Personal</span>

VALIDACIÓN VISUAL EN GITHUB PAGES
------------
Subir los archivos de esta etapa y abrir únicamente la página
principal https://awooolab.github.io/Agenda_SENA/. Comprobar allí que se
observan el formulario, las actividades del día, las categorías y la leyenda de
colores.

FLUJO DE LA LECCIÓN
-------------------
1. Agregar o actualizar modelos, servicio, formulario, leyenda y pruebas en
   GitHub.
2. Actualizar preview.html con los mismos campos, categorías, colores, botones
   e iconos de la interfaz de PC.
3. Subir los cambios y abrir únicamente la página principal.
4. Comprobar allí el módulo independiente de esta etapa dentro de la ventana integrada.

El preview no modifica actividades reales; permite revisar visualmente las
reglas que implementa el servicio.

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
- Espacios: agenda.summary, agenda.today, agenda.appointments y
  agenda.activities.
- Estado: agenda con datos de prueba, categorías y progreso visible.

COMPONENTES QUE DEBEN APARECER
------------------------------
1. Tarjetas de citas de hoy, pendientes, próxima cita y actividades.
2. Lista de agenda de hoy con hora, título y categoría.
3. Tabla de citas recientes con título, fecha, hora y estado.
4. Formulario de nueva actividad.
5. Progreso semanal y lista de actividades.
6. Leyenda con nombre y color de cada categoría.
7. Iconos referenciados desde `assets/icons/`.

PREVIEW
-------
El fragmento puede contener varios espacios, pero cada uno debe declararse
explícitamente, por ejemplo:

    <section data-screen="agenda" data-slot="agenda.activities">

Guardar, completar, editar, filtrar y eliminar deben producir una respuesta
visible. Los colores nunca deben ser el único medio para comunicar un estado.
