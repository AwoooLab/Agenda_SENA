# Milestone 07 — Main window

## Goal

Create the authenticated application shell where the calendar and activity views will live.

## Files

- `stages/07_main_window/app.py`.
- `src/ui/main_window.py`.
- `src/ui/navigation.py`.
- `app.py`.

## Requirements

- Show the logged-in user.
- Provide navigation to calendar, activities and logout.
- Keep each screen in its own module.
- Do not duplicate authentication logic.

## Integration

The login window opens `main_window.py` with the authenticated user. The root `app.py` starts the application flow.

## Validation

Log in with a test user, verify the user name is visible and confirm that logout returns to the login screen.

## Prompt sequence

Request `navigation.py` first, then `main_window.py`, then adapt the root entry point.
