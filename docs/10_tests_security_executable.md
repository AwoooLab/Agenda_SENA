# Hito 10 — Pruebas, seguridad y ejecutable

## Propósito

Revisar la aplicación completa, confirmar que sus partes principales funcionan
y preparar una versión ejecutable para Windows.

## Metodología de integración vigente

El estudiante trabaja únicamente en `stages/10_tests_security_executable/`.
Las pruebas, el script de construcción, la guía de entrega y `preview.html`
cierran la primera parte del proyecto. El preview comunica el resultado final
en las dos ventanas de referencia, pero la aceptación real combina las pruebas
locales en Windows con la revisión visual en
`https://awooolab.github.io/Agenda_SENA/`.

Al aprobar el hito, `main.py` queda como punto de entrada de la aplicación
local, `src/` conserva la navegación de una sola ventana y
`config/integration.json` registra los módulos aprobados. GitHub Pages no
ejecuta Python ni genera el `.exe`; solo muestra la evidencia visual de la
entrega.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/10_tests_security_executable/test_database.py
stages/10_tests_security_executable/test_auth_service.py
stages/10_tests_security_executable/test_event_service.py
stages/10_tests_security_executable/build_windows.ps1
stages/10_tests_security_executable/release.md
stages/10_tests_security_executable/preview.html
```

## Archivos de prueba

Los tres archivos de prueba deben usar `unittest` y datos temporales.

### `test_database.py`

Comprobar creación del esquema, inserción de usuario, inserción de actividad,
lectura de datos y relación entre usuario y actividad.

### `test_auth_service.py`

Comprobar contraseña correcta, contraseña incorrecta, usuario inactivo, sesión
activa y cierre de sesión. No incluir credenciales reales.

### `test_event_service.py`

Comprobar creación, edición, filtrado, completado y eliminación de actividades.

## Archivo `build_windows.ps1`

Crear un script de PowerShell que:

1. Se detenga si ocurre un error.
2. Verifique que Python esté disponible.
3. Cree o use un entorno virtual local.
4. Instale las dependencias indicadas en `requirements.txt`, si existen.
5. Ejecute las pruebas antes de compilar.
6. Cree el ejecutable con PyInstaller usando:

```text
python -m PyInstaller --onefile --windowed --name AgendaSENA main.py
```

7. Deje el resultado dentro de `dist/`.
8. No copie contraseñas, bases de datos personales ni archivos temporales al
   ejecutable.

El script debe mostrar mensajes claros en español y detenerse si las pruebas
fallan.

## Archivo `release.md`

Documentar en español:

- Requisitos de Windows.
- Cómo descargar el proyecto.
- Cómo ejecutar las pruebas.
- Cómo construir el ejecutable.
- Dónde queda el archivo `.exe`.
- Cómo abrir la agenda por primera vez.
- Qué archivos locales se crean.
- Qué información nunca se debe compartir.
- Cómo reportar un error.

## Reglas de seguridad

- No subir contraseñas al repositorio.
- No subir datos reales de usuarios.
- No subir una base de datos con información personal.
- No guardar contraseñas en texto plano.
- Mantener los archivos temporales fuera del código fuente.

## Flujo de la clase y validación en GitHub Pages

Esta etapa reúne pruebas, seguridad y entrega; `preview.html` presenta el
estado final que se integrará en la única ventana de la aplicación. El flujo es:

1. Agregar en GitHub las pruebas, el script, `release.md` y los archivos de la
   entrega.
2. Actualizar `preview.html` con el nombre del ejecutable, resultados, iconos y
   estados finales.
3. Actualizar el fragmento final de `preview.html`; el visor principal ya lo
   cargará después de las funciones anteriores.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Comprobar allí que la información de entrega es legible.
6. Verificar la entrega final desde la ventana principal acumulada.

El preview no compila ni descarga el ejecutable. Solo comunica visualmente el
resultado de la validación local y la entrega preparada.

### Validación visual específica

- Se identifica el nombre del ejecutable.
- Se distinguen pruebas aprobadas, seguridad y compatibilidad con Windows.
- Los estados de entrega son claros y no muestran credenciales ni datos
  privados.

## Comprobación visual en GitHub Pages

Agregar o actualizar las pruebas, el script, `release.md` y `preview.html` en
GitHub. Después abrir únicamente la página principal:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se observan el nombre del ejecutable, el estado de las pruebas,
la seguridad y la entrega para Windows.

### Prueba funcional opcional en el PC

Si se dispone de Windows y Python, ejecutar las pruebas, generar el `.exe` y
probar la aplicación. GitHub Pages no compila, ejecuta ni descarga el
ejecutable; solo muestra la información visual de la entrega.

## Integración después de aprobar el stage

La entrega final usa el `main.py` de la raíz como punto de entrada. Los
archivos de `stages/10_tests_security_executable/` permanecen como material de
la etapa y sirven para preparar las pruebas, la seguridad y la compilación.
La aplicación integrada conserva una sola ventana y el visor web solo muestra
los módulos aprobados registrados en `config/integration.json`.

## Instrucción para ChatGPT

```text
Genera únicamente stages/10_tests_security_executable/release.md. Escribe una
guía en español para construir y usar el ejecutable de Agenda SENA en Windows.
Incluye requisitos, pruebas, compilación con PyInstaller, ubicación del .exe,
archivos locales y reglas para no compartir credenciales ni datos personales.
No inventes servicios en internet ni agregues pasos de GitHub Actions.
Devuelve solo el contenido del archivo Markdown.
```

Solicitar las pruebas y el script de compilación por separado.

## Criterio de terminado

La etapa se puede publicar cuando las pruebas, el script, la guía y
`preview.html` están en GitHub sin mostrar datos privados. La generación y
ejecución del `.exe` se comprobarán posteriormente en
un PC con Windows.

## Alineación con las ventanas de referencia

La validación final debe comprobar el flujo completo y no solamente servicios
aislados:

1. Abrir la aplicación en el login.
2. Registrar o seleccionar un usuario de prueba.
3. Iniciar sesión con credenciales válidas.
4. Confirmar que aparece la agenda en la misma ventana.
5. Navegar por Inicio, Nueva cita, Citas, Calendario y Actividades.
6. Crear una cita y comprobarla en calendario, agenda del día y tabla.
7. Cerrar sesión y confirmar el regreso al login.

El preview de la entrega muestra el resultado de esta comprobación sin
convertirse en una tercera pantalla.
