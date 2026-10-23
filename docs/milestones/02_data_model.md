# Milestone 02 — Data model

## Goal

Represent an agenda activity as a Python object.

## Files

- `stages/02_data_model/model.py`.
- `src/model.py`.
- `tests/test_model.py`.

## Requirements

The first model is `Event` or `Cita` and must contain title, date, start time, end time and description. Use `dataclass`, conversion to dictionary and reconstruction from a dictionary.

## Integration

The model must not open windows or read files. Later, database and interface modules will import it.

## Validation

Create an object, convert it to a dictionary and run:

```text
python -m unittest discover -s tests -v
```

## Prompt sequence

Ask for `model.py` only. Require standard Python, typed fields and one small example under `if __name__ == "__main__"`.
