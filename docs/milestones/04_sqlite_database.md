# Milestone 04 — SQLite database

## Goal

Replace the temporary JSON persistence with SQLite, which is appropriate for users, login and related calendar records.

## Files

- `src/database.py`: connection and database operations.
- `src/schema.sql`: table definitions.
- `data/agenda.db`: generated local database.
- `tests/test_database.py`: database tests using a temporary file.

## Requirements

- Use Python's built-in `sqlite3`.
- Create tables automatically on first run.
- Use parameterized queries.
- Never store passwords in this stage.

## Integration

Services will use `database.py`; the UI must not contain SQL queries directly. Keep JSON only as an optional export format.

## Validation

Create a temporary database, create a table, insert one record, read it and remove the temporary file after the test.

## Prompt sequence

Request `schema.sql`, validate the table design, then request `database.py`, and finally request `test_database.py`.
