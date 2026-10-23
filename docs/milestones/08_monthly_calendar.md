# Milestone 08 — Monthly calendar

## Goal

Display a navigable monthly calendar with a clear day grid.

## Files

- `src/ui/monthly_calendar.py`.
- `src/ui/calendar_cell.py`.
- `tests/test_calendar.py`.

## Requirements

- Previous month and next month controls.
- Button to return to the current month.
- Correct number of days for each month.
- Highlight the current day.
- Use a readable layout at the target window size.

## Integration

The calendar receives the current user and activities from the service layer. It must not query SQLite directly.

## Validation

Test February in leap and non-leap years, month transitions and selecting a day.

## Prompt sequence

Ask ChatGPT for the date calculation functions first, then the calendar cell, then the complete calendar view.
