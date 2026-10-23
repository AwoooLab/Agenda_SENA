# Hito 05 — Registro de usuarios

## Propósito

Crear la lógica para registrar usuarios locales antes de construir la pantalla
de inicio de sesión.

## Archivos que debe crear el alumno

Crear únicamente:

```text
stages/05_user_registration/user.py
stages/05_user_registration/user_repository.py
stages/05_user_registration/user_service.py
stages/05_user_registration/test_user_service.py
```

## Archivo `user.py`

Definir una `dataclass` llamada `Usuario` con estos campos, en este orden para
que los campos obligatorios aparezcan antes de los campos con valor inicial:

- `username: str`.
- `email: str`.
- `id: int | None = None`.
- `password_hash: str = ""`.
- `password_salt: str = ""`.
- `is_active: bool = True`.
- `created_at: str = ""`.

El modelo no debe abrir ventanas ni consultar directamente SQLite.

## Archivo `user_repository.py`

Crear una clase `RepositorioUsuarios` que reciba una conexión SQLite en su
constructor e implemente:

```python
crear(usuario: Usuario) -> Usuario
buscar_por_username(username: str) -> Usuario | None
buscar_por_email(email: str) -> Usuario | None
actualizar_credenciales(user_id: int, password_hash: str, password_salt: str) -> None
```

El repositorio es el único archivo de esta etapa que ejecuta consultas SQL.
Debe usar consultas parametrizadas y convertir las filas de la base de datos en
objetos `Usuario`.

## Archivo `user_service.py`

Crear una clase `ServicioUsuarios` que reciba un `RepositorioUsuarios` y
implemente:

```python
registrar(username: str, email: str) -> Usuario
```

La función debe:

1. Quitar espacios al principio y al final.
2. Rechazar un nombre de usuario vacío.
3. Rechazar un correo vacío.
4. Convertir el correo a minúsculas.
5. Rechazar usuarios o correos repetidos.
6. Crear el usuario activo.
7. Dejar `password_hash` y `password_salt` vacíos para que el Hito 06 los
   configure.
8. Devolver el usuario creado.

Los errores deben ser `ValueError` con mensajes claros en español.

## Archivo `test_user_service.py`

Usar una base SQLite temporal y comprobar:

- Registro correcto.
- Nombre de usuario vacío.
- Correo vacío.
- Nombre de usuario duplicado.
- Correo duplicado ignorando mayúsculas y minúsculas.
- Usuario creado con `is_active=True`.

## Restricciones

- No crear interfaz gráfica.
- No pedir contraseñas en esta etapa.
- No guardar contraseñas en texto plano.
- No colocar consultas SQL dentro de `user_service.py`.
- No modificar archivos de otras etapas.

## Comprobación manual

Ejecutar:

```text
python -m unittest stages/05_user_registration/test_user_service.py -v
```

Debe observarse que el primer usuario se crea y que los datos repetidos generan
errores claros.

## Integración posterior

Integrar los archivos en:

```text
src/models/user.py
src/repositories/user_repository.py
src/services/user_service.py
```

La interfaz de registro se agregará después del inicio de sesión básico.

## Instrucción para ChatGPT

```text
Genera únicamente stages/05_user_registration/user.py. Define una dataclass
Usuario con id, username, email, password_hash, password_salt, is_active y
created_at, usando los tipos y valores iniciales indicados en la especificación.
No uses Tkinter, no uses SQL y no agregues campos diferentes. Devuelve solo el
código del archivo.
```

Solicitar los otros tres archivos por separado y pedir que no modifiquen los
archivos anteriores.

## Criterio de terminado

El alumno puede registrar usuarios únicos mediante un servicio, consultar el
repositorio y obtener errores claros cuando los datos no son válidos.
