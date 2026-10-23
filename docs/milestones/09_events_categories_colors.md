# Milestone 09 — Events, categories and colors

## Goal

Manage activities in the calendar and distinguish categories visually.

## Files

- `src/models/event.py`.
- `src/models/category.py`.
- `src/services/event_service.py`.
- `src/ui/event_form.py`.
- `src/ui/color_legend.py`.
- `tests/test_event_service.py`.

## Requirements

- Create, edit, delete and complete an activity.
- Assign a category and color.
- Use text and icons in addition to color for accessibility.
- Filter activities by date, category and status.

## Integration

`event_service.py` connects models, database and validation. The form calls the service. The calendar refreshes after a successful change.

## Validation

Create an event, edit it, display it on the selected day, complete it and delete it.

## Prompt sequence

Request one model or service at a time. Do not ask ChatGPT to redesign the whole interface while implementing a single feature.
