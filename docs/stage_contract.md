# Contrato de los stages

Cada carpeta dentro de stages/ es un módulo educativo independiente. El
alumno trabaja únicamente dentro de la carpeta del stage que está estudiando.

## Independencia

Un stage debe:

- Funcionar con sus propios archivos y datos de prueba.
- No importar archivos de otro stage.
- No depender de que otro stage esté terminado.
- Tener su propia entrada de prueba en Python cuando corresponda.
- Tener su propio preview.html para revisar su resultado visual.
- Cumplir solamente los requisitos de su especificación.

Que un módulo sea independiente no significa que quede aislado para siempre.
Significa que puede revisarse antes de conectarlo al programa completo.

## Acumulación

La acumulación ocurre únicamente en la aplicación integrada:

- main.py ejecuta la aplicación local.
- src/ contiene la carcasa, el estado y la navegación compartida.
- index.html representa en GitHub Pages la versión integrada actual.
- config/integration.json indica qué módulos aprobados están conectados.

Un stage que todavía no está aprobado no aparece en la aplicación integrada.
Que exista su carpeta o su preview.html no significa que deba mostrarse.

## Contrato de integración

Cada files.txt y cada especificación debe indicar:

- Nombre del módulo.
- Punto de entrada independiente.
- Archivos propios.
- Librerías permitidas.
- Entradas que recibe.
- Salidas que produce.
- Clases y funciones públicas.
- Datos de prueba.
- Validaciones y errores.
- Requisitos visuales del preview.html.
- Lugar donde se conectará en src/ o main.py.
- Qué archivos no puede importar ni modificar.

La integración se realiza después de la validación. El estudiante no necesita
modificar main.py, src/, web/ ni config/ mientras desarrolla el stage.

## Visibilidad en GitHub Pages

La página principal es el único visor y actualmente muestra solo dos ventanas
SVG, una a la vez:

1. `assets/login-window.svg`, con el formulario final de acceso.
2. `assets/agenda-window.svg`, con la interfaz final de la aplicación.

`web/screen.js` realiza el cambio entre ambas ventanas. No se muestran tarjetas,
menús de stages, indicadores de avance ni otras secciones externas.

Cuando otro stage esté listo, su componente se incorpora en el espacio
correspondiente de la ventana de agenda. La carpeta del stage y su preview no
se muestran automáticamente en Pages; la interfaz publicada representa el
resultado final integrado.

## Navegación de la aplicación integrada

La aplicación de PC conservará una ventana principal después del inicio. En el
PC, `src/router.py` reemplaza la vista central sin abrir otra ventana. En
GitHub Pages, `web/screen.js` muestra una pantalla a la vez para comprobar el
flujo inicial y la agenda.

Por eso el estudiante puede construir una etapa aislada como login, calendario
o tabla, pero la integración posterior permite navegar entre esas funciones
sin convertir cada stage en una aplicación separada.

## Contrato visual obligatorio

La especificación de cada stage debe relacionar la lógica con una parte visible
de las dos ventanas de referencia. No basta con indicar que una clase o una
función debe existir.

Cada stage debe declarar:

- `screen`: `login` o `agenda`.
- `slot`: espacio visual que recibe el resultado.
- `state`: estado inicial, vacío, con datos o con error.
- `sample_data`: datos de demostración que deben aparecer en el preview.
- `navigation`: acción que permite llegar al componente dentro de la ventana.
- `preserved`: elementos de etapas anteriores que deben seguir visibles.

Los espacios permitidos son:

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

El stage debe marcar su fragmento principal así:

```html
<section data-screen="agenda" data-slot="agenda.calendar">
  <!-- componente visual de la etapa -->
</section>
```

`preview.html` no debe convertirse en una tercera ventana ni en un tablero de
progreso. Es la comprobación del componente que ocupará un espacio dentro de
la ventana de login o de agenda.

## Contrato de navegación

La aplicación final debe cumplir siempre este flujo:

```text
Abrir Agenda SENA
        |
        v
Inicio de sesión
        |
        | credenciales válidas
        v
Ventana de agenda
        |
        | opción del menú
        v
Vista central seleccionada
        |
        | Cerrar sesión
        v
Inicio de sesión
```

Un stage no puede crear una segunda instancia de `tk.Tk()`. Puede utilizar
`tk.Frame`, `ttk.Frame` u otros controles dentro del contenedor que recibe,
pero la integración debe reemplazar la vista central mediante el router.

## Criterios de terminado de cada stage

Una etapa está terminada solo cuando se cumplen todos estos puntos:

1. Sus archivos funcionan de forma independiente con sus propios datos de
   prueba.
2. Sus funciones públicas y errores están descritos en `files.txt`.
3. `preview.html` reproduce los textos, controles, estados y jerarquía visual
   del componente de PC.
4. El fragmento declara correctamente `data-screen` y `data-slot`.
5. La acción principal del componente tiene una respuesta observable.
6. Se conservan los elementos que el contrato marca como `preserved`.
7. La navegación no abre ventanas externas.
8. La integración futura está descrita sin importar otro stage.

La validación visual no reemplaza la prueba Python y la prueba Python no
reemplaza la validación visual. Ambas comprueban partes diferentes del mismo
resultado.
