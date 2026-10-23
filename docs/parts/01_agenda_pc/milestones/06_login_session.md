# Hito 06 — Inicio de sesión y sesión activa

## Propósito

Permitir que un usuario registrado establezca una contraseña, inicie sesión y
cierre su sesión dentro de la aplicación local.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/06_login_session/password.py
stages/06_login_session/auth_service.py
stages/06_login_session/login_window.py
stages/06_login_session/test_auth_service.py
stages/06_login_session/preview.html
```

## Archivo `password.py`

Crear estas funciones:

```python
def crear_credenciales(password: str) -> tuple[str, str]:
    ...


def verificar_password(password: str, salt: str, password_hash: str) -> bool:
    ...
```

Reglas obligatorias:

- Usar `secrets.token_hex` para crear una sal diferente.
- Usar `hashlib.pbkdf2_hmac` para derivar el resumen.
- Usar como mínimo 100000 iteraciones.
- Devolver la sal y el resumen como texto hexadecimal.
- Nunca guardar ni devolver la contraseña original.
- Comparar los resultados de forma segura con `hmac.compare_digest`.

## Archivo `auth_service.py`

Crear una clase `ServicioAutenticacion` con estos métodos:

```python
establecer_password(user_id: int, password: str) -> None
iniciar_sesion(username: str, password: str) -> Usuario | None
cerrar_sesion() -> None
usuario_actual() -> Usuario | None
```

Reglas:

- La contraseña debe tener mínimo ocho caracteres.
- `iniciar_sesion` debe buscar el usuario mediante el repositorio.
- Un usuario inexistente debe recibir el mismo resultado que una contraseña
  incorrecta: `None`.
- Un usuario inactivo no puede iniciar sesión.
- Una sesión correcta guarda el usuario actual únicamente en memoria.
- `cerrar_sesion` debe dejar la sesión vacía.

## Archivo `login_window.py`

Crear una ventana Tkinter independiente con:

- Título: `Agenda SENA — Inicio de sesión`.
- Tamaño: `420x300`.
- Campo `Usuario`.
- Campo `Contraseña` oculto con `show="*"`.
- Botón `Iniciar sesión`.
- Botón `Cerrar`.
- Etiqueta de error inicialmente vacía.

La ventana debe recibir un servicio de autenticación y una función
`on_login(usuario)` que se ejecute después de un inicio correcto. No debe abrir
la ventana principal por su cuenta.

Si los datos son incorrectos, mostrar el mensaje:

```text
El usuario o la contraseña no son correctos.
```

No mostrar si el usuario existe o no.

## Archivo `test_auth_service.py`

Usar una base de datos temporal y comprobar:

- Contraseña válida.
- Contraseña incorrecta.
- Usuario inexistente.
- Usuario inactivo.
- Contraseña con menos de ocho caracteres.
- Cierre de sesión.
- Que la contraseña original no aparezca en la base de datos.

## Restricciones

- No guardar contraseñas en texto plano.
- No colocar credenciales en el código.
- No usar internet.
- No crear todavía la ventana principal.
- No mezclar consultas SQL en la ventana gráfica.

## Flujo de la clase y validación en GitHub Pages

La autenticación se implementa en `password.py`, `auth_service.py` y
`login_window.py`; `preview.html` muestra la pantalla de inicio de sesión. El
flujo de la clase es:

1. Agregar en GitHub los archivos de autenticación definidos en esta etapa.
2. Actualizar `preview.html` cuando cambien campos, botones, mensajes o iconos.
3. Actualizar el fragmento de inicio de sesión en `preview.html`; el visor lo
   cargará junto con el registro y las funciones anteriores.
4. Subir los cambios y abrir únicamente la página principal de GitHub Pages.
5. Comprobar allí usuario, contraseña, botón y estado de error.
6. Verificar desde la ventana principal la misma composición visual acumulada.

El preview no autentica usuarios ni guarda contraseñas. Es la vista visual de
la pantalla de PC que se está construyendo.

### Validación visual específica

- Los campos `Usuario` y `Contraseña` están claramente identificados.
- La contraseña aparece oculta en la representación visual.
- El mensaje de error es visible sin revelar si el usuario existe.
- Los iconos y botones agregados al login también aparecen en `preview.html`.

## Comprobación visual en GitHub Pages

Agregar o actualizar los archivos del login y `preview.html` en GitHub. Después
abrir únicamente la página principal:

```text
https://awooolab.github.io/Agenda_SENA/
```

Confirmar que se observan usuario, contraseña, botón, mensaje de error e
iconos. Si se agrega un icono al login en el diseño de la aplicación, también
debe agregarse al `preview.html` para poder verificarlo en Pages.

### Prueba funcional opcional en el PC

Si se dispone de Python, ejecutar las pruebas del servicio y abrir la ventana
local. GitHub Pages no autentica usuarios, no ejecuta Tkinter y no guarda
contraseñas.

## Integración progresiva en `main.py`

Después de terminar la etapa, incorporar progresivamente en `main.py` la
protección de contraseñas, el servicio de autenticación y la pantalla de login.
Los archivos de `stages/06_login_session/` permanecen aislados y no se
importan automáticamente.

## Instrucción para ChatGPT

```text
Genera únicamente stages/06_login_session/password.py. Implementa
crear_credenciales y verificar_password usando secrets.token_hex,
hashlib.pbkdf2_hmac, al menos 100000 iteraciones y hmac.compare_digest. Nunca
guardes ni devuelvas la contraseña original. Devuelve solo el código del archivo
y escribe los comentarios en español.
```

Solicitar los demás archivos uno por uno y pedir que respeten las funciones y
mensajes definidos en esta especificación.

## Criterio de terminado

La etapa se puede publicar cuando los archivos del login están en GitHub,
`preview.html` muestra usuario, contraseña, mensajes e iconos, y la Clase 06
se integra en la ventana acumulada. La autenticación y la seguridad quedan definidas en
Python y se probarán al ejecutar el proyecto en un PC.
