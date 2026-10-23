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

## Comprobación manual

Ejecutar:

```text
python -m unittest stages/06_login_session/test_auth_service.py -v
```

Después abrir la ventana, escribir un usuario válido, probar una contraseña
incorrecta y comprobar que la etiqueta de error se muestra sin cerrar el
programa.

## Integración posterior

Integrar los archivos en:

```text
src/security/password.py
src/services/auth_service.py
src/ui/login_window.py
```

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

Un usuario activo puede iniciar sesión con una contraseña correcta, un usuario
inactivo no puede entrar y la sesión se puede cerrar sin guardar la contraseña
original.
