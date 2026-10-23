# Milestone 06 — Login and session

## Goal

Authenticate a local user and keep the current session in memory.

## Files

- `src/security/password.py`.
- `src/services/auth_service.py`.
- `src/ui/login_window.py`.
- `tests/test_auth_service.py`.

## Requirements

- Generate a unique salt for each password.
- Store only a derived password hash.
- Do not place credentials in the repository.
- Close or clear the session on logout.

## Integration

`auth_service.py` uses the user repository and password module. `login_window.py` calls the service and opens the main window only after success.

## Validation

Test correct password, incorrect password, inactive user and logout.

## Prompt sequence

Ask for the password helper first, then authentication service, then the login window, one file per conversation request.
