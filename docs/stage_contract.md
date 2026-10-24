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

La página principal es el único visor. Carga únicamente los módulos declarados
en config/integration.json. La configuración actual contiene solo
01_python_window, porque es el único resultado terminado y aprobado.

Cuando otro stage esté listo, se valida su salida y se agrega su módulo a la
configuración de integración. No se agregan funciones futuras antes de tiempo.

## Navegación de la aplicación integrada

La aplicación integrada conserva una sola ventana. El menú y el área central
son compartidos por todas las funciones aprobadas. En el PC, `src/router.py`
reemplaza la vista central sin abrir otra ventana. En GitHub Pages, `web/app.js`
usa el mismo principio: crea el menú con los módulos registrados y muestra una
vista a la vez dentro del mismo visor.

Por eso el estudiante puede construir una etapa aislada como login, calendario
o tabla, pero la integración posterior permite navegar entre esas funciones
sin convertir cada stage en una aplicación separada.
