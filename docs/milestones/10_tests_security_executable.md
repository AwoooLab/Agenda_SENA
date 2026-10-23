# Milestone 10 — Tests, security and executable

## Goal

Stabilize the application and prepare a Windows executable.

## Files

- `tests/test_database.py`.
- `tests/test_auth_service.py`.
- `tests/test_event_service.py`.
- `scripts/build_windows.ps1`.
- `docs/release.md`.

## Requirements

- Tests must run without internet.
- Database tests must use temporary data.
- Credentials must never be committed.
- The build script must create output in `dist/`.
- The executable must be tested on a clean Windows user account.

## Integration

Only package the application after all tests pass. Keep build artifacts out of the source folders and document the release steps.

## Validation

```text
python -m unittest discover -s tests -v
```

Then build and open the executable on Windows.

## Prompt sequence

Ask for one test or one build script at a time. Review every generated command before executing it.
