# Milestone 05 — User registration

## Goal

Allow the application to create local users before adding login.

## Files

- `src/models/user.py`.
- `src/repositories/user_repository.py`.
- `src/services/user_service.py`.
- `tests/test_user_service.py`.

## Requirements

- Unique username or email.
- Active/inactive status.
- No plain-text passwords.
- Clear validation errors.

## Integration

The repository handles database queries. The service handles rules. The UI will call the service and will not access SQL directly.

## Validation

Test successful registration, duplicate user and missing required fields.

## Prompt sequence

Request the model first, then the repository, then the service, and finally one test file. Tell ChatGPT not to modify previous files.
