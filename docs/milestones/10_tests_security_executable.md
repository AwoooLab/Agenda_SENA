# Hito 10 — Pruebas, seguridad y ejecutable

## Propósito

Revisar la aplicación completa, confirmar que sus partes principales funcionan
y preparar una versión ejecutable para Windows.

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
python -m PyInstaller --onefile --windowed --name AgendaSENA app.py
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

## Flujo de la clase y validación visual

Esta etapa reúne pruebas, seguridad y entrega; `preview.html` presenta el
estado final que se mostrará en la colección de clases. El flujo es:

1. Ejecutar las pruebas y corregir cualquier fallo.
2. Revisar seguridad, archivos generados y compilación del ejecutable.
3. Actualizar `preview.html` con el nombre del ejecutable, resultados, iconos y
   estados finales.
4. Abrir el preview y comprobar que la información de entrega es legible.
5. Agregar en `index.html` la tarjeta de la Clase 10 con su preview.
6. Publicar y verificar la entrega final en GitHub Pages.

El preview no compila ni descarga el ejecutable. Solo comunica visualmente el
resultado de la validación local y la entrega preparada.

### Validación visual específica

- Se identifica el nombre del ejecutable.
- Se distinguen pruebas aprobadas, seguridad y compatibilidad con Windows.
- Los estados de entrega son claros y no muestran credenciales ni datos
  privados.

## Comprobación manual

Desde la raíz del proyecto, ejecutar:

```text
python -m unittest discover -s tests -v
```

Después ejecutar el script de PowerShell. Copiar el `.exe` a un computador o
cuenta de usuario limpia de Windows y comprobar que:

1. La aplicación abre.
2. Se puede registrar o utilizar un usuario de prueba.
3. Se puede iniciar sesión.
4. Se puede abrir el calendario.
5. Se puede crear una actividad.
6. Se puede cerrar la aplicación sin errores.

## Integración posterior

Integrar las pruebas en `tests/`, el script en `scripts/build_windows.ps1` y la
documentación en `docs/release.md`.

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

Las pruebas funcionan, el ejecutable se crea en `dist/`, la aplicación abre en
Windows y `preview.html` representa la Clase 10 publicada sin mostrar datos
privados.
