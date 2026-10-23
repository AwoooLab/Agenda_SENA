# Milestone 03 — Temporary JSON storage

## Goal

Learn how to persist a list of activities locally before introducing a database.

## Files

- `stages/03_json_storage/storage.py`.
- `stages/03_json_storage/demo.py`.
- `src/storage.py`.
- `data/agenda.json`.
- `tests/test_storage.py`.

## Requirements

Use `json` and `pathlib`, UTF-8 encoding, readable indentation and a clear behavior when the file does not exist.

## Integration

The storage module receives data and a path; it must not create Tkinter widgets. The interface will call it later.

## Validation

Save an activity, load it again and compare the result. Run the storage tests.

## Prompt sequence

Ask ChatGPT for `storage.py`, then `demo.py`, then the test. Never request the complete application in one prompt.
